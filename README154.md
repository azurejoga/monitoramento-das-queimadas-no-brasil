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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ca043d8-0a71-369b-9137-fccae47316f6 | -19.98395 | -55.48942 | 2024-09-26 05:44:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7fcb6771-c46c-33e2-be01-5c4eb5e18d26 | -19.98248 | -55.49903 | 2024-09-26 05:44:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 14.7 |
| fc4ab138-88d9-3c8e-895c-649ca04f2612 | -19.98099 | -55.50873 | 2024-09-26 05:44:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 608b9411-f7a2-3f14-8103-72f53addb2f1 | -19.7798 | -51.48278 | 2024-09-26 05:44:00 | AQUA_M-M | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 3eb32beb-7e91-3398-8b41-5bd6d14284f1 | -19.11188 | -57.48088 | 2024-09-26 05:44:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 47fcb4d6-dbb2-3fcd-9b7d-ef406fe0fead | -19.11015 | -57.49134 | 2024-09-26 05:44:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 6ba7bf11-2dce-39c1-8c6e-2067f27d40ac | -17.46294 | -52.57938 | 2024-09-26 05:44:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8efacef8-ba41-367e-8616-98a5f76b2739 | -1.88447 | -54.719 | 2024-09-26 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2f7f3b3-ee46-3cc0-9c00-72596107b4e1 | -1.8834 | -54.71646 | 2024-09-26 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e5e81354-fe4f-3915-b99b-7b381c90460b | -1.8827 | -54.72093 | 2024-09-26 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b82f62f-cb2a-3dc5-ac7c-79b2cdb8b8c2 | -1.88244 | -54.89586 | 2024-09-26 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8721d261-528c-3752-a22d-a9b9ff7a9495 | -1.88178 | -54.90025 | 2024-09-26 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0897b577-092d-3725-87e5-9b0151c1823c | -1.8791 | -54.71362 | 2024-09-26 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c884396d-caab-3d19-87ae-74543f79059d | -1.87843 | -54.7181 | 2024-09-26 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3314f4c3-ffe5-34e5-9b1c-ea19c586bdfc | -1.87736 | -54.71556 | 2024-09-26 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fcd19961-eadb-3345-bc9b-c21c825c4243 | -1.87666 | -54.72003 | 2024-09-26 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| becb2ffb-1173-3c2f-aba1-2b16c4120ab9 | -1.34209 | -54.65734 | 2024-09-26 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d192e62e-1e90-3ebf-9895-761bc659cbc0 | -1.34145 | -54.66154 | 2024-09-26 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63ab9377-20dc-3a09-8325-28f9babdece6 | -1.34082 | -54.66579 | 2024-09-26 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dab9df60-bcc6-3666-b43a-489daf8e5107 | -1.33972 | -54.65805 | 2024-09-26 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3869cfce-c5d6-328c-ab78-1f849114aaf0 | -1.33905 | -54.66227 | 2024-09-26 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7e78a47-c878-31eb-9f2b-148d2007ac2a | -1.33839 | -54.66651 | 2024-09-26 05:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9e800b5b-f007-3d13-a2d2-2ac20cbae14c | -1.05079 | -53.36609 | 2024-09-26 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee25e209-6dd1-3566-a088-617dfa59b8e7 | -1.04599 | -53.35408 | 2024-09-26 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 62cc5c3e-3b11-3df3-a7b2-6acdbfe568a1 | -1.04516 | -53.35947 | 2024-09-26 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ba1ff728-72c2-327d-8da8-ee6fc52eae91 | -1.04433 | -53.36483 | 2024-09-26 05:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| de5954d2-108b-306c-a02f-fba49191c254 | -1.29259 | -60.40631 | 2024-09-26 05:44:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 185bee88-f776-3372-8f33-74f063beb82c | -9.06952 | -61.36686 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2730fa7d-8e84-37ad-81f5-c568a7426de7 | -9.06896 | -61.37096 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6c75700-0454-30f1-9f67-4835cc821db8 | -9.0684 | -61.37505 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c4937a87-cf54-365d-86f5-23c392ca2bec | -9.06299 | -61.38262 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b44c3c9-819d-3337-9925-fa53f44d970f | -9.06243 | -61.38668 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc76a52b-0390-3d2c-8c69-6b15b9a79257 | -9.06006 | -61.38343 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec65bc08-b0ff-3d2c-9924-aba2cb50c250 | -9.09206 | -61.13107 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 12665802-673b-36ab-bfd5-7b4296f714cc | -9.08443 | -61.1284 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 14693355-4a6f-3e14-8fa7-9b3626d133c5 | -9.11437 | -61.4518 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16b5f48b-9024-32fc-91b8-bb4368006f4e | -9.1138 | -61.45584 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f2cc7d2-a9cf-320f-acb9-12b11ad7c97d | -9.04935 | -61.42734 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e0ad350-ca9e-3dd8-bc72-f12f9cd0e942 | -9.04877 | -61.43137 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| caf370e3-a4a2-3022-a6bb-e8496e51d016 | -9.04777 | -61.43007 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62a76e2c-3773-378f-ac12-627081ffa57d | -9.04722 | -61.43409 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b77fc90-fdfa-3114-80b7-fbe953fe5ded | -9.0445 | -61.4308 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21d8d159-e46c-338d-8b34-a1cd66093f12 | -9.04392 | -61.4348 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79ddfc77-ae91-3d52-b836-fc5b03cea485 | -9.0435 | -61.42949 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8c5a42a-8e28-397a-9a5b-be69e199b00f | -9.04295 | -61.4335 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 506dc169-5733-3c74-9e2d-edde80e6f510 | -8.97818 | -62.40406 | 2024-09-26 05:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17dc4c33-2a7f-37f6-9780-ea43236230cf | -8.96619 | -62.14153 | 2024-09-26 05:46:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7102335a-7928-36ff-83a5-a58b66c7b517 | -8.96212 | -62.14097 | 2024-09-26 05:46:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 55ea1f26-9113-36e8-8f16-8116b49f004a | -8.95805 | -62.14038 | 2024-09-26 05:46:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1143d44e-79f2-39a8-97a4-87f60e6c6291 | -8.93421 | -62.13342 | 2024-09-26 05:46:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 566d5f4c-cba3-34c5-916f-1963dcf8b7df | -8.93369 | -62.13702 | 2024-09-26 05:46:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75f2d70a-9f69-352e-bb09-440a28d4f8d4 | -1.88906 | -61.46608 | 2024-09-26 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d54d377-43bc-3771-859c-ac7b065df46d | -1.88832 | -61.47084 | 2024-09-26 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14c1b02c-d8ab-3f2d-b03c-b5180cddeef9 | -1.49681 | -61.59542 | 2024-09-26 05:46:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d68eba3-5b60-3029-a9cc-cd2a166acfbe | -3.33987 | -61.55939 | 2024-09-26 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d94cc8c1-8720-3403-9e3f-119a989c1466 | -3.32283 | -61.56676 | 2024-09-26 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6c92346-ae45-30d2-b3f8-b7b2e2852ac4 | -3.31967 | -61.56126 | 2024-09-26 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2732530-b4b6-3cd7-b0cf-c4e80aed0254 | -3.31577 | -61.56069 | 2024-09-26 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4981418a-be01-3930-ae9d-133bdb5ba188 | -3.09548 | -62.07277 | 2024-09-26 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab36233c-0ed6-3639-9f72-9161b7a12b25 | -3.02525 | -61.67353 | 2024-09-26 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bec7de53-d6e5-3030-b667-1245dc95daff | -3.02451 | -61.67831 | 2024-09-26 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c51ebb3-1a4d-38fa-a6c7-ee4fa1e9e113 | -3.02378 | -61.68307 | 2024-09-26 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 532b747a-bac7-3136-9452-9ea4aa49c555 | -3.02066 | -61.67772 | 2024-09-26 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a620cb8b-12ca-3f84-ae16-0effaafa9da3 | -3.01993 | -61.6825 | 2024-09-26 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1afe7733-ff71-390e-92bf-da32273658f5 | -3.0192 | -61.68726 | 2024-09-26 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05b091a6-22e7-3038-a384-4588d3497ef2 | -3.01608 | -61.68192 | 2024-09-26 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef5d6793-eead-3dd2-a15e-29a07f7244c7 | -3.01535 | -61.68669 | 2024-09-26 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b08a607b-0e7d-3eab-ba2b-de3b312cad02 | -2.88514 | -61.88084 | 2024-09-26 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7c2ba6b-e68a-32ec-b479-fc39998594bc | -2.88443 | -61.88546 | 2024-09-26 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35d44059-ac12-3eb1-b110-7298f0412aaa | -2.88064 | -61.88486 | 2024-09-26 05:46:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25ec5a16-905c-32dd-980d-f5f52abe28ca | -5.64778 | -63.17215 | 2024-09-26 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d96ce4a-f866-3128-94cb-7fee100aeba0 | -7.95769 | -62.94337 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f12d5614-6115-3125-b85e-474d7e2f153c | -7.95388 | -62.94279 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| feb10a4a-b8fd-3114-8c08-c9c6531e14c9 | -7.90437 | -62.98821 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08fd9bab-c237-31fb-bf68-8acbd07b4904 | -7.90058 | -62.98764 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65a3d998-2bba-3eeb-b6fc-b20e56e703d6 | -7.59925 | -63.40976 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7563d6c-3931-32a1-8e63-b40f071768b6 | -7.59556 | -63.40918 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa1c0f53-62df-356e-9232-154c836236d7 | -7.58676 | -62.78063 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6aca9428-942e-3a2f-a637-c9283d47b509 | -7.58538 | -62.79011 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b8b2f0a-059c-33a2-9be3-e28e17b4b9da | -7.58293 | -62.78004 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c141cb62-0863-3ce1-9ded-438563ff126a | -7.58155 | -62.78953 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ce1a758-76f0-3458-b553-15db3cda6573 | -7.57772 | -62.78896 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7300635-e2e7-3ed4-9173-0f5b485ba4f9 | -7.57704 | -62.7937 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0ceaad4-65f3-35bd-9abf-c4b46ab6d006 | -7.52447 | -63.46271 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a71684b-5354-3585-8c96-cd42c09f8cc9 | -7.52382 | -63.46705 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50e59b02-147f-397e-9851-a7ddbeeec93d | -7.52342 | -63.36852 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72196955-b18f-3245-91cf-07005177b385 | -7.52014 | -63.46651 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdc1d6b0-0dfc-3d59-bb62-215eb601a863 | -7.51949 | -63.47085 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80ba6f89-02be-3c78-b982-bf848a71745e | -7.50834 | -63.64502 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3cf611d-e1a8-339f-a30f-bf6e185d26a5 | -7.50406 | -63.64872 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4c3c303-4f14-3c19-8fed-8d6d854f1e13 | -7.46922 | -63.00411 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97687f59-c5a6-3310-8b9a-0dc460bbda7b | -7.46545 | -63.00356 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f6027d2-aefa-3adb-b278-66f1b007f1f6 | -7.46167 | -63.003 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88b4c6ab-90ac-3aff-b2a3-1868ab6d5372 | -7.43659 | -62.98992 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32ae3149-8a18-3784-8f0a-54c8a08a9536 | -7.43585 | -63.07404 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53e4436f-5af6-354e-97c2-c4fc7dfccbf6 | -7.43281 | -62.98934 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a133d4ac-a13d-3bd8-88d5-dc9d6170c25f | -7.4022 | -63.83557 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b42a058-2eff-3069-b90c-61cc7ca14301 | -7.40124 | -63.83257 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2bd1f36a-66e6-34dc-97ac-79b2ce36c067 | -7.40061 | -63.83672 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a365e9b-ccc6-33df-a64a-a4373e817136 | -7.39934 | -63.84502 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README155.md)
