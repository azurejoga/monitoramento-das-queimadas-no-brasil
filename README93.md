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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c358d42-2724-3f2d-b3d5-7dbc15f41ee0 | -3.72071 | -54.22765 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1fa76b5a-55cb-3ef0-9fcc-4576bbe938c3 | -3.54676 | -54.62949 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e563932-69f3-31d3-9759-60f8c278c8ab | -3.18467 | -50.59303 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ad86c2a-2312-3d53-b228-90ddb079396f | -4.10376 | -54.02458 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0ea338e8-85db-384a-995e-b5fff0457014 | -1.30603 | -54.18733 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 09da38f0-8492-3fcf-b82d-1b9f792d96a9 | -6.88003 | -45.89414 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f537c6a6-d12b-329c-bdf6-4794f99910ff | -3.73934 | -59.45936 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f23bd2c5-5a5f-383e-b4f7-21c725e3d1f8 | -3.92533 | -56.03161 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3e7e46f0-32d1-3baf-8037-7db8d7a60cf6 | -3.29155 | -51.53689 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f9d1f2a-b857-33f0-b20d-1135fcd2dd9c | -4.27492 | -46.54034 | 2026-10-09 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b98b1998-7d42-344a-a99f-c2680450204f | -5.49656 | -42.85756 | 2026-10-09 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d6ede77a-834c-3a55-85f9-ee7df11fe1df | -1.1594 | -54.2281 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa2f80be-6e26-3601-ad36-a1c8f4c48d4f | -3.46073 | -50.58146 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2cc8df0d-5d8b-3e2e-ac4c-ec166e70fcc4 | -3.26452 | -54.06135 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdc0ac8c-c239-3f74-89ca-1c1632db4788 | -3.74397 | -59.47403 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7a35b9e8-e896-3cf9-ac40-496add2743b8 | -3.60377 | -54.58278 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a210b5c5-5caf-3575-99a7-730eb7866696 | -3.20466 | -53.86401 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9d2b7b78-8f61-3b54-9827-e308484bca3a | -6.89051 | -45.89219 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5482214c-fa49-353a-94a0-4f2e5047136e | -3.08152 | -54.29023 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d092fbb-a275-334c-a9bf-51b81f5144e9 | -2.99569 | -53.8515 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| edb21174-38a6-39de-ac1e-902718800ccf | -3.00381 | -53.89552 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 63812590-8c0e-3bc6-921f-6e9af1174d07 | -5.69944 | -41.73332 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 34cd320e-46cc-3f6e-8315-40a1b2dcbe54 | -5.99474 | -40.97814 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e2f0a8b6-8012-3a2e-a89f-2a932d5ad0b4 | -3.09228 | -54.28876 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8524a412-b477-3c98-be58-05992d26853f | -3.00881 | -51.0074 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 04c3cfed-461a-3076-8680-91036a4a49fe | -3.57466 | -54.69158 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d765442e-8c1b-3ab4-8ef0-e5e015b4b3cc | -5.71124 | -53.4878 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c6c45517-9474-36de-88ba-a4eda3b688b5 | -3.10024 | -53.93434 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0864cc5-6246-3ab0-a791-100fb331b5b0 | -3.62733 | -54.23408 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bcc64251-8658-3a79-911b-67a816fe749c | -4.74156 | -55.66753 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d8e4d3f6-6ec2-31cb-a396-b21fb747fb76 | -2.59361 | -47.35771 | 2026-10-09 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16fe81bf-6f2d-3a30-87c0-dd65192ba055 | -5.51135 | -42.83368 | 2026-10-09 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| bba298f6-fa6d-3aeb-8657-6fa234e0697b | -3.10887 | -53.78898 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2160c40f-81fa-37a0-9c67-71015ba8af1f | -4.32453 | -55.01366 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4268645-6a37-352b-9380-bd2146026e51 | -2.76372 | -54.10685 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ff1e0a7-e226-3906-af7e-f2429166f58d | -3.09834 | -53.94592 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb72e18e-3399-3dcd-ac0d-57874430462d | -2.98636 | -54.06558 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 974e2fd8-de4f-301d-9c2a-7fd358fc8578 | -3.20377 | -53.86944 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3af7adbc-212d-3507-a296-d0caf839e029 | -3.52924 | -44.33399 | 2026-10-09 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae1b82ac-9e04-3462-bfb3-7fafae3980b9 | -3.18541 | -58.63791 | 2026-10-09 04:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c858f5f3-470d-37c1-8517-7dec6877c453 | -7.18689 | -44.27736 | 2026-10-09 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5583fd63-1233-30de-b166-47fe6ec120be | -4.57633 | -54.95982 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d269d11-5ea1-32d8-8050-bbfdfaddc24e | -6.69149 | -44.01872 | 2026-10-09 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87f67d75-cbe2-32a3-9f89-df7e3c4bdc4b | -3.90954 | -55.8987 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0f827657-1854-34e5-b8dc-0bc61eee0509 | -5.93102 | -45.69606 | 2026-10-09 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 763d04be-336f-3111-91d9-85c41c38f64c | -5.17286 | -45.60612 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a221838-d44f-3c9a-b353-7d25a90a2bf7 | -2.74358 | -54.13428 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad5de69b-bb4d-3230-ace8-691cc9eebbe2 | -2.55414 | -58.03376 | 2026-10-09 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7236c922-9d20-3afa-9e63-46b0af449666 | -1.11193 | -54.15417 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 668ebb63-95d6-3d91-8841-08ba3d60ea41 | -3.49587 | -54.61436 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d27e84b-d7e2-35b6-aaea-9dccb2505ba9 | -4.53497 | -49.66818 | 2026-10-09 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e08e70f-e333-3f49-9550-2c06cd9c3e55 | -3.01231 | -51.01167 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 36f4a59b-9ace-3684-959b-95e2ffd89f52 | -3.17728 | -50.58836 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a541585c-b89d-344a-a91f-e8642459c22f | -4.90458 | -48.77171 | 2026-10-09 04:25:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a0bede8-bd92-3a7b-ba18-ad2d7dd10297 | -3.35008 | -50.41722 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ff6cb2a3-3073-3ad1-b178-843322052a8b | -4.35732 | -55.23022 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3ec64a6-35e4-345d-90b4-36a3bad59003 | -3.1098 | -53.78336 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 39679d74-b33b-3e99-9125-d9cc06a62c4b | -1.832 | -54.9943 | 2026-10-09 04:25:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2281bdb0-b336-32dd-ab4f-f7418f2a1a39 | -3.29075 | -51.56893 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b49970a0-a133-3715-b10c-e5ca3ed933d2 | -2.89104 | -54.16948 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0268a1a-7fe7-36a7-83a3-a350be47587d | -3.11111 | -53.93062 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c46f4b14-396d-3924-9fd3-1ed2ce36e065 | -2.82869 | -51.03891 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1c2a7c6-66cd-3fb5-b685-0fbd785523e4 | -3.01903 | -54.0557 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c09cb54d-73d7-32ce-88e0-9bba868f146c | -3.82254 | -44.59416 | 2026-10-09 04:25:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a630e79b-0d2e-392a-be93-99a50bde174a | -5.70589 | -53.49132 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2f60e19a-cef4-35d4-b378-84fb1116b90f | -3.54214 | -54.69012 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0aabc63d-8a0f-3a70-b9c0-316292025ae5 | -2.9359 | -54.18274 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 334750e6-94e8-3729-8113-f9d699ac3748 | -2.7642 | -54.10387 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f50185dd-3369-3612-bd9e-09af6cb7cefb | -6.12918 | -43.85085 | 2026-10-09 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26529650-1734-3129-be87-a2076adc93b0 | -6.15375 | -47.27479 | 2026-10-09 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fa07561-56d4-3a24-a9da-8280edc774b7 | -5.68968 | -53.4741 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 23e95daf-c9d9-39f2-8fd8-ada655bb8324 | -2.40062 | -51.3029 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 142d1c1d-694e-3225-ad21-78ac29e61d44 | -6.90152 | -45.88675 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9fa3c992-1687-3444-88d3-2a00d66bd72d | -3.28009 | -54.06078 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aff57d0c-2b3f-371b-b7b6-eb0eda94ff7f | -2.88138 | -54.19569 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32f76b57-6a8e-33b0-bfea-03ba5befccf0 | -3.16712 | -50.45222 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 825784ee-a5be-3082-9824-ced306da95de | -3.25682 | -54.04572 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 78586f83-358e-3867-aa25-5b1ef906d4a1 | -4.0393 | -54.23011 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07a08765-01d7-36b5-99dd-d25375ea5682 | -3.00098 | -53.91283 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f56a22e7-9b92-37b1-a3a5-b9a8c626ae37 | -3.10787 | -53.95044 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3f4cfc14-c534-3d7c-ae19-aa6a47b11722 | -3.93031 | -56.03662 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce602270-779d-3cf3-9f68-119bb45c937d | -3.16224 | -54.73735 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98f8f573-412d-3f4a-a878-c694f5513f2e | -3.01371 | -54.05167 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c892d5dd-beb0-34ee-ba5c-b610a688675e | -3.43139 | -54.54527 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 06e0d097-6dd3-351d-9d5a-a388494f26fc | 1.69293 | -55.61086 | 2026-10-09 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c59a22d4-7cb5-3986-a099-33e2e3c2b707 | -3.01727 | -54.06123 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 711d4c34-acf6-355f-8914-859bb30eb02c | -2.83477 | -54.1409 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c44d4d2b-46f7-3611-aa63-198f646ada41 | -3.73352 | -59.46154 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 4b633658-a1e7-3540-afd9-20991e3afc3c | -3.39471 | -50.21287 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f2e73af-fdaa-32e7-8057-2ceee42d4e18 | -5.09451 | -46.21813 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a619e02b-7ba2-3641-b043-691768ac6621 | -3.56764 | -54.66516 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 059b5a32-b0ef-3231-990a-b24e32e4d601 | -3.43405 | -59.54443 | 2026-10-09 04:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 601d48f9-8f44-3083-a912-55e71b93acaf | -1.05279 | -53.59181 | 2026-10-09 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34cac4be-37ae-323e-9dd6-3853e7fdc115 | -2.96311 | -48.751 | 2026-10-09 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1bf0afe-4ab7-31b8-8b83-fd1c1a6738f6 | -5.09674 | -46.22551 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 978968a0-9122-3c9c-a4a6-2d9c477ab9a4 | -3.92464 | -56.03563 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2d2a456d-e43c-3f37-9257-fc885ace0324 | -3.26678 | -54.01702 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d14a6ff9-7016-303e-ac2b-e78cc824738d | -5.0909 | -46.13312 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93d25bc2-6026-3875-ae5e-02ad4dda0118 | -3.93971 | -55.71561 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dcd42fc-7c6d-381e-a6c7-9d9546f08375 | -5.39524 | -45.90281 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README94.md)
