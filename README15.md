# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d10a5a64-f042-301e-bf00-7775a32f2fca | -9.0141 | -57.541199 | 2026-08-29 01:16:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f79b4496-6d08-3454-9fcf-ac98b48ac4f6 | -4.3402 | -55.434601 | 2026-08-29 01:16:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b458ca1-31e0-3a75-8cbb-73b2ac0089ab | -9.9334 | -60.4319 | 2026-08-29 01:16:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44a46159-9c2e-3dfb-94f3-97fe9e720b87 | 3.2871 | -60.615398 | 2026-08-29 01:16:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 49728c5f-2f71-3b02-b227-80a674d607ea | -19.2283 | -57.6628 | 2026-08-29 01:16:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2a332d92-0d0b-31ed-b9b6-2c9b14b7a13a | -11.1954 | -51.2924 | 2026-08-29 01:16:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e41fac4a-9ae4-3f03-b29f-14618f335334 | -4.3421 | -55.442799 | 2026-08-29 01:16:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05f72d52-bf14-3c5d-a927-5f82bbe9f3f3 | -11.7184 | -54.540798 | 2026-08-29 01:16:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62db6703-84a8-3d78-84f8-066120bdc4c2 | -7.4945 | -55.288502 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f323617d-217f-3b5c-832d-f045cc6c12c1 | -5.9824 | -57.6758 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d514030d-2c4e-38bd-bb53-a0a049a46a3f | -11.0288 | -57.244499 | 2026-08-29 01:16:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cac2c923-84ff-332f-ac89-da202fa3e683 | -20.224199 | -47.390999 | 2026-08-29 01:16:00 | METOP-C | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 69743376-29f9-355e-b114-c50ef7e0f3b2 | -9.8734 | -60.297699 | 2026-08-29 01:16:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c961608c-50ba-3169-bad3-48b744aac784 | -9.9217 | -60.425598 | 2026-08-29 01:16:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 36e6cb97-4185-34c6-b5a0-319a4cb6f6dc | -6.9403 | -58.943298 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f33f9d6-7d74-35c8-8941-92f4b795f703 | -11.1988 | -55.102798 | 2026-08-29 01:16:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dfccd4df-f45d-3497-a549-69ff7552c689 | -7.344 | -55.174999 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91410da3-0fa1-31c0-ae69-ba3b13ee1ae7 | -6.8786 | -59.401699 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38946462-a384-3002-b5bd-72fc29a21a81 | -5.8886 | -57.761799 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 128dcf1c-1a0f-36bb-a032-28ed88009a77 | -10.7594 | -53.978401 | 2026-08-29 01:16:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd1aacdf-d1ef-3fb4-b424-aa79714535f5 | -8.5532 | -54.784302 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4815582b-0049-38a5-8835-a62520a3a221 | -14.4152 | -52.574501 | 2026-08-29 01:16:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1b117021-7492-3417-89bc-b59403ac2eeb | -14.1646 | -52.823502 | 2026-08-29 01:16:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3df8b407-08a9-32b2-968c-bd195528770b | -7.5573 | -61.300499 | 2026-08-29 01:16:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c3d19c43-419b-33e1-aeaa-ffd1ceac1dd2 | -8.9546 | -50.7934 | 2026-08-29 01:16:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1010789-de1c-349b-8746-bfeefcebd717 | -14.9001 | -52.611599 | 2026-08-29 01:16:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b39bd60-e699-3664-ae3a-422dc55ac427 | -6.7674 | -55.667198 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 374361c9-ae94-3426-a30c-3decda3d40b1 | -4.1897 | -54.569 | 2026-08-29 01:16:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a264dac7-7c38-38fe-b04d-c27956f27fe7 | -9.9254 | -60.442299 | 2026-08-29 01:16:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95883ef2-dcc1-3bd0-a99c-a5505c135e83 | -14.2022 | -52.850899 | 2026-08-29 01:16:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5bf06384-0472-3d90-9863-f21c1b708230 | -8.604 | -54.7808 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6adbd80-2bbb-36ec-b55f-0e14d4bd3b27 | -13.175 | -55.660301 | 2026-08-29 01:16:00 | METOP-C | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0d0c14ac-e52f-31a4-ab15-d6b39734c455 | -14.9043 | -52.629002 | 2026-08-29 01:16:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 906f9894-6871-3b70-92b5-13ac65ff1182 | -8.9838 | -50.786201 | 2026-08-29 01:16:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22f3748a-8403-3482-ad34-4b480583ffb8 | -7.514 | -55.284 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ffbcb78-c534-3e55-a398-eda8b8038ea5 | 0.9148 | -59.623001 | 2026-08-29 01:16:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 28eec292-d3b9-33ca-aece-345814b86654 | -4.0533 | -56.2868 | 2026-08-29 01:16:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8801bb88-8d39-36be-b8bf-56a35454f307 | -8.5939 | -54.825298 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 961f64ed-3ec9-3c2c-a3a6-42dd6b290118 | -11.0453 | -57.2262 | 2026-08-29 01:16:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 802d2d30-5735-3d72-9390-e8e8a7bcf2bc | -8.9417 | -63.255699 | 2026-08-29 01:16:00 | METOP-C | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5b9c2b21-3b62-386b-a69b-1e4352d5b5e1 | -22.037001 | -56.033401 | 2026-08-29 01:16:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2cd09db4-c8b5-3f95-9365-691e6e2ccd9f | -23.1511 | -48.673901 | 2026-08-29 01:16:00 | METOP-C | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8cd180cb-b5ac-35e1-a54a-2a37d39a3ebd | -9.8752 | -60.305901 | 2026-08-29 01:16:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d46bb94-c18e-37f5-b914-f1f5efb0450e | -7.2803 | -45.8647 | 2026-08-29 01:16:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69ffab9b-ef3e-3f93-8019-b17cbd8858a9 | -7.5661 | -61.200001 | 2026-08-29 01:16:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c37fa06-8a42-333c-ba2b-a77581b8e4ef | -9.9236 | -60.433998 | 2026-08-29 01:16:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2fe9021b-44a2-31b0-bb17-e7bef92819b8 | -6.1707 | -57.777802 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f68ff51a-da89-3de6-a6ce-278ac0404f76 | -14.1945 | -52.8619 | 2026-08-29 01:16:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56c6a1d7-d154-370a-ae7e-f32790675859 | -7.6234 | -61.367599 | 2026-08-29 01:16:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0126ded0-f1af-3374-bf18-1dd353021b41 | -20.2299 | -47.373199 | 2026-08-29 01:16:00 | METOP-C | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 37b6b43a-3530-3780-a250-144a019c39cf | -14.914 | -56.3302 | 2026-08-29 01:16:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f0a800be-c37a-3f5b-aa28-398029ce1479 | -8.5337 | -55.362701 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86e6cedc-b6e4-3bf6-a33c-38601427553a | -13.4757 | -57.0396 | 2026-08-29 01:16:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 535dc129-de12-3135-a64e-8389480b6817 | -8.9449 | -50.795799 | 2026-08-29 01:16:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 713f6182-6dda-3874-b95e-4feb8009f3bc | -9.9725 | -53.927799 | 2026-08-29 01:16:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7064a037-1514-3d83-9b97-097409518ef7 | -7.4926 | -55.2808 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e76d6f9-1a8c-3642-ad88-d24c0aa22e96 | -9.609 | -55.103802 | 2026-08-29 01:16:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53868965-13bd-3771-a009-7bbbdae1f336 | -11.0371 | -57.235401 | 2026-08-29 01:16:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d2a31b2-0ba1-3d18-b895-e96dbc1bed29 | -6.1762 | -57.711601 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b03f59f-5a3a-3ddd-afc1-f51776d3b98d | -11.2206 | -51.310699 | 2026-08-29 01:16:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1754ad8a-02d8-3791-a844-fe2fd78b09ea | -5.9444 | -57.734901 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9511ada0-7d21-3866-8133-34bedc74cc2c | -11.1896 | -51.269199 | 2026-08-29 01:16:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ce1a0c29-7e82-3f72-a51c-02309fcba1f3 | -9.1817 | -59.625401 | 2026-08-29 01:16:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3c95f29-a46a-3adf-92a6-8e035483c9eb | -6.7706 | -59.470699 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e6d8f45-8d15-3016-9037-d44a681121ae | -8.9483 | -50.809299 | 2026-08-29 01:16:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06304e8e-0441-3610-a787-822943295adc | -11.0469 | -57.233101 | 2026-08-29 01:16:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0793d389-a0ca-3ecb-a12f-50e84878aa65 | -19.289101 | -49.5168 | 2026-08-29 01:16:00 | METOP-C | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2d7c35e5-1546-3260-aef6-fcef6a1c008a | -8.5923 | -54.775101 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8f0d336-f5ca-33b9-819e-13a16d5e5b7b | -9.2032 | -51.551498 | 2026-08-29 01:16:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a898ee69-6523-3caf-b393-5378bba665e2 | -6.7954 | -59.397701 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3133718e-7a8c-3f4e-a506-2770cb399a17 | -8.5905 | -54.767101 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79e41564-26e4-3daf-a840-d4ca3953557a | -10.5053 | -59.6166 | 2026-08-29 01:16:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9a664b2-a93c-3e23-9a94-446c87ec8a66 | -11.1971 | -55.095299 | 2026-08-29 01:16:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1b078a6-3240-3e62-a0e2-d9e60924e14e | -14.2078 | -52.8312 | 2026-08-29 01:16:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8841ae67-5a26-3bcf-87e0-80505f76e602 | -6.9435 | -58.957298 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dce0e5e8-4841-3ce1-be93-7dcd3dfdbd58 | -7.5864 | -61.339298 | 2026-08-29 01:16:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc204349-d1c7-3e58-af7f-ed65f142a19f | -11.7166 | -54.5331 | 2026-08-29 01:16:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5867118-548a-3d27-85b6-c519a5f5dca3 | -6.769 | -59.463501 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 401577b5-13e4-39a7-96fb-f72ca1a73d41 | -7.3636 | -55.170399 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b67bcecb-7734-3c2c-9e20-5b6b74ede202 | -14.9099 | -52.6091 | 2026-08-29 01:16:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54d5367d-7424-34b1-ae33-99c37c73c3af | -5.9938 | -57.680401 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ae106ae-3a1e-3546-9dbf-79ff7695851b | -9.4182 | -51.586399 | 2026-08-29 01:16:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fd920c5-a529-3546-a936-c774f630d788 | -20.9527 | -57.587299 | 2026-08-29 01:16:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 752f49a5-f3db-3edc-877d-d20b5c8702aa | -9.2234 | -59.767899 | 2026-08-29 01:16:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1175ae0-4ce5-3ace-b6f3-c556f4de9ed2 | -9.1838 | -56.973099 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2b864d3-106f-3f5b-8abf-4df4f27f4c8c | -7.5024 | -55.2785 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a62c200-f0b7-38d1-a927-935a24600950 | -6.9568 | -59.474602 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bdf21cb5-0f78-3edd-bceb-1dd9fb47c229 | -20.9475 | -57.562 | 2026-08-29 01:16:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 35cafb16-910e-35e9-bb4f-be7f268a3aaf | -7.5122 | -55.276299 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b15292c-9065-34f1-9863-af8b54501565 | -6.7771 | -55.664902 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfe4d3ab-b893-3ad1-a61c-53e9cf7f0749 | -8.958 | -50.8069 | 2026-08-29 01:16:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6f375d9-a746-3f4b-9fb5-31a16486e470 | -5.7696 | -57.557201 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9e4f30e-c9af-3740-80fb-6b750d3312c7 | -6.7662 | -63.029099 | 2026-08-29 01:16:00 | METOP-C | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc2118b9-70b9-3909-b711-378ec3a2390e | -14.2791 | -57.041801 | 2026-08-29 01:16:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c7e2aa9-346f-3791-ae45-7605b8176eef | -7.4745 | -61.3908 | 2026-08-29 01:16:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9dcb98d-2731-3896-90c7-838af8192fa5 | -4.1504 | -60.6833 | 2026-08-29 01:16:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ccac5c48-3beb-3187-81b0-6978f5ee4add | -6.7594 | -55.676998 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48b037c5-db73-3916-8dcb-b9602a992a92 | -6.5349 | -55.245399 | 2026-08-29 01:16:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30e78d8f-c3bb-35d4-adf1-8e23b31581e9 | -8.9467 | -63.279202 | 2026-08-29 01:16:00 | METOP-C | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 69e498c8-4b54-3a21-8a96-299ec2f1d835 | -11.0257 | -57.230598 | 2026-08-29 01:16:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)
