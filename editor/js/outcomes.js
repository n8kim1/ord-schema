/**
 * Copyright 2020 Open Reaction Database Project Authors
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *      http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

goog.provide('ord.outcomes');

goog.require('ord.products');

goog.require('proto.ord.ReactionOutcome');

// Freely create radio button groups by generating new input names.
ord.outcomes.radioGroupCounter = 0;

ord.outcomes.load = function (outcomes) {
  outcomes.forEach(outcome => ord.outcomes.loadOutcome(outcome));
};

ord.outcomes.loadOutcome = function (outcome) {
  const node = ord.outcomes.add();

  const time = outcome.getReactionTime();
  if (time != null) {
    writeMetric('.outcome_time', time, node);
  }
  const conversion = outcome.getConversion();
  if (conversion) {
    writeMetric('.outcome_conversion', outcome.getConversion(), node);
  }
  const products = outcome.getProductsList();
  ord.products.load(node, products);

  const analyses = outcome.getAnalysesMap();
  const names = analyses.stringKeys_();
  names.forEach(function (name) {
    const analysis = analyses.get(name);
    ord.outcomes.loadAnalysis(node, name, analysis);
  });
};

ord.outcomes.loadAnalysis = function (analysesNode, name, analysis) {
  const node = ord.outcomes.addAnalysis(analysesNode);

  $('.outcome_analysis_name', node).text(name);

  setSelector($('.outcome_analysis_type', node), analysis.getType());
  $('.outcome_analysis_chmo_id', node).text(analysis.getChmoId());
  $('.outcome_analysis_details', node).text(analysis.getDetails());

  const processes = analysis.getProcessedDataMap();
  const processNames = processes.stringKeys_();
  processNames.forEach(function (name) {
    const process = processes.get(name);
    const processNode = ord.outcomes.addProcess(node);
    ord.outcomes.loadProcess(processNode, name, process);
  });

  const raws = analysis.getRawDataMap();
  const rawNames = raws.stringKeys_();
  rawNames.forEach(function (name) {
    const raw = raws.get(name);
    const rawNode = ord.outcomes.addRaw(node);
    ord.outcomes.loadRaw(rawNode, name, raw);
  });
  $('.outcome_analysis_manufacturer', node).text(
      analysis.getInstrumentManufacturer());
  const calibrated = analysis.getInstrumentLastCalibrated();
  if (calibrated) {
    $('.outcome_analysis_calibrated', node).text(calibrated.getValue());
  }
  setSelector(
      $('.outcome_analysis_internal_standard', node),
      analysis.getUsesInternalStandard());
  setSelector(
      $('.outcome_analysis_authentic_standard', node),
      analysis.getUsesAuthenticStandard());
};

ord.outcomes.loadProcess = function (node, name, process) {
  $('.outcome_process_name', node).text(name);
  $('.outcome_process_description', node).text(process.getDescription());
  $('.outcome_process_format', node).text(process.getFormat());

  const stringValue = process.getStringValue();
  const floatValue = process.getFloatValue();
  const bytesValue = process.getBytesValue();
  const url = process.getUrl();
  if (stringValue) {
    $('.outcome_process_text', node).show();
    $('.uploader', node).hide();
    $('.outcome_process_text', node).text(stringValue);
    $("input[value='text']", node).prop('checked', true);
  }
  if (floatValue) {
    $('.outcome_process_text', node).show();
    $('.uploader', node).hide();
    $('.outcome_process_text', node).text(floatValue);
    $("input[value='number']", node).prop('checked', true);
  }
  if (bytesValue) {
    $('.outcome_process_text', node).hide();
    $('.uploader', node).show();
    ord.uploads.load(node, bytesValue);
    $("input[value='upload']", node).prop('checked', true);
  }
  if (url) {
    $('.outcome_process_text', node).show();
    $('.uploader', node).hide();
    $('.outcome_process_text', node).text(url);
    $("input[value='url']", node).prop('checked', true);
  }
};

ord.outcomes.loadRaw = function (node, name, raw) {
  $('.outcome_raw_name', node).text(name);
  $('.outcome_raw_description', node).text(raw.getDescription());
  $('.outcome_raw_format', node).text(raw.getFormat());

  const stringValue = raw.getStringValue();
  const floatValue = raw.getFloatValue();
  const bytesValue = raw.getBytesValue();
  const url = raw.getUrl();
  if (stringValue) {
    $('.outcome_raw_text', node).show();
    $('.uploader', node).hide();
    $('.outcome_raw_text', node).text(stringValue);
    $("input[value='text']", node).prop('checked', true);
  }
  if (floatValue) {
    $('.outcome_raw_text', node).show();
    $('.uploader', node).hide();
    $('.outcome_raw_text', node).text(floatValue);
    $("input[value='number']", node).prop('checked', true);
  }
  if (bytesValue) {
    $('.outcome_raw_text', node).hide();
    $('.uploader', node).show();
    ord.uploads.load(node, bytesValue);
    $("input[value='upload']", node).prop('checked', true);
  }
  if (url) {
    $('.outcome_raw_text', node).show();
    $('.uploader', node).hide();
    $('.outcome_raw_text', node).text(url);
    $("input[value='url']", node).prop('checked', true);
  }
};

ord.outcomes.unload = function () {
  const outcomes = [];
  $('.outcome').each(function (index, node) {
    node = $(node);
    if (!node.attr('id')) {
      // Not a template.
      const outcome = ord.outcomes.unloadOutcome(node);
      outcomes.push(outcome);
    }
  });
  return outcomes;
};

ord.outcomes.unloadOutcome = function (node) {
  const outcome = new proto.ord.ReactionOutcome();

  const time = readMetric('.outcome_time', new proto.ord.Time(), node);
  outcome.setReactionTime(time);

  const conversion =
      readMetric('.outcome_conversion', new proto.ord.Percentage(), node);
  outcome.setConversion(conversion);

  const products = ord.products.unload(node);
  outcome.setProductsList(products);

  const analyses = outcome.getAnalysesMap();
  $('.outcome_analysis').each(function (index, node) {
    node = $(node);
    if (!node.attr('id')) {
      // Not a template.
      ord.outcomes.unloadAnalysis(node, analyses);
    }
  });
  return outcome;
};

ord.outcomes.unloadAnalysis = function (analysisNode, analyses) {
  const name = $('.outcome_analysis_name', analysisNode).text();

  const analysis = new proto.ord.ReactionAnalysis();
  analysis.setType(getSelector($('.outcome_analysis_type', analysisNode)));
  const chmoId = $('.outcome_analysis_chmo_id', analysisNode).text();
  if (!isNaN(chmoId)) {
    analysis.setChmoId(chmoId);
  }
  analysis.setDetails($('.outcome_analysis_details', analysisNode).text());

  const processes = analysis.getProcessedDataMap();
  $('.outcome_process', analysisNode).each(function(index, processNode) {
    processNode = $(processNode);
    if (!processNode.attr('id')) {
      ord.outcomes.unloadProcess(processNode, processes);
    }
  });
  const raws = analysis.getRawDataMap();
  $('.outcome_raw', analysisNode).each(function(index, rawNode) {
    rawNode = $(rawNode);
    if (!rawNode.attr('id')) {
      ord.outcomes.unloadRaw(rawNode, raws);
    }
  });
  analysis.setInstrumentManufacturer(
      $('.outcome_analysis_manufacturer', analysisNode).text());
  const calibrated = new proto.ord.DateTime();
  calibrated.setValue($('.outcome_analysis_calibrated', analysisNode).text());
  analysis.setInstrumentLastCalibrated(calibrated);
  analysis.setUsesInternalStandard(
      getSelector($('.outcome_analysis_internal_standard', analysisNode)));
  analysis.setUsesAuthenticStandard(
      getSelector($('.outcome_analysis_authentic_standard', analysisNode)));

  analyses.set(name, analysis);
};

ord.outcomes.unloadProcess = function (node, processes) {
  const name = $('.outcome_process_name', node).text();

  const process = new proto.ord.Data();
  process.setDescription($('.outcome_process_description').text());
  process.setFormat($('.outcome_process_format').text());

  if ($("input[value='text']", node).is(':checked')) {
    const stringValue = $('.outcome_process_text', node).text();
    process.setStringValue(stringValue);
  }
  if ($("input[value='number']", node).is(':checked')) {
    const floatValue = parseFloat($('.outcome_processed_text', node).text());
    if (!isNaN(floatValue)) {
      processed.setFloatValue(floatValue);
    }
  }
  if ($("input[value='upload']", node).is(':checked')) {
    const bytesValue = ord.uploads.unload(node);
    process.setBytesValue(bytesValue);
  }
  if ($("input[value='url']", node).is(':checked')) {
    const url = $('.outcome_process_text', node).text();
    process.setUrl(url);
  }
  processes.set(name, process);
};

ord.outcomes.unloadRaw = function (node, raws) {
  const name = $('.outcome_raw_name', node).text();

  const raw = new proto.ord.Data();
  raw.setDescription($('.outcome_raw_description', node).text());
  raw.setFormat($('.outcome_raw_format', node).text());

  if ($("input[value='text']", node).is(':checked')) {
    const stringValue = $('.outcome_raw_text', node).text();
    raw.setStringValue(stringValue);
  }
  if ($("input[value='number']", node).is(':checked')) {
    const floatValue = parseFloat($('.outcome_raw_text', node).text());
    if (!isNaN(floatValue)) {
      raw.setFloatValue(floatValue);
    }
  }
  if ($("input[value='upload']", node).is(':checked')) {
    const bytesValue = ord.uploads.unload(node);
    raw.setBytesValue(bytesValue);
  }
  if ($("input[value='url']", node).is(':checked')) {
    const url = $('.outcome_raw_text', node).text();
    raw.setUrl(url);
  }
  raws.set(name, raw);
};

ord.outcomes.add = function () {
  return addSlowly('#outcome_template', '#outcomes');
};

ord.outcomes.addAnalysis = function (node) {
  return addSlowly('#outcome_analysis_template', $('.outcome_analyses', node));
};

ord.outcomes.addProcess = function (node) {
  const processNode =
      addSlowly('#outcome_process_template', $('.outcome_processes', node));

  const typeButtons = $("input[type='radio']", processNode);
  typeButtons.attr(
      'name', 'outcomes_' + ord.outcomes.radioGroupCounter++);
  typeButtons.change(function () {
    if ((this.value == 'text') || (this.value == 'url')) {
      $('.outcome_process_text', processNode).show();
      $('.uploader', processNode).hide();
    } else {
      $('.outcome_process_text', processNode).hide();
      $('.uploader', processNode).show();
    }
  });
  ord.uploads.initialize(processNode);
  return processNode;
};

ord.outcomes.addRaw = function (node) {
  const rawNode = addSlowly('#outcome_raw_template', $('.outcome_raws', node));

  const typeButtons = $("input[type='radio']", rawNode);
  typeButtons.attr(
      'name', 'outcomes_' + ord.outcomes.radioGroupCounter++);
  typeButtons.change(function () {
    if ((this.value == 'text')
        || (this.value == 'number')
        || (this.value == 'url')) {
      $('.outcome_raw_text', rawNode).show();
      $('.uploader', rawNode).hide();
    } else {
      $('.outcome_raw_text', rawNode).hide();
      $('.uploader', rawNode).show();
    }
  });
  ord.uploads.initialize(rawNode);
  return rawNode;
};
