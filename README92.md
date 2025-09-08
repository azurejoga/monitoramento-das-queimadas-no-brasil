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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9fae900-ed37-3dca-981e-1d897ca6e30f | -9.15545 | -60.85471 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e65e80c-d83a-360c-ab29-228a728d22cd | -12.83039 | -52.90059 | 2025-09-08 05:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7972d8c9-d27d-37a3-a977-12e9a0fc4dea | -10.17827 | -61.13631 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b006464-59a5-3cab-b1b6-b39712f74276 | -9.1727 | -59.38327 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4dd1af62-1a41-3728-a64b-be07f5e27e70 | -9.09363 | -64.51566 | 2025-09-08 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d0af7a89-35e4-3b84-9e24-c05d0fe10927 | -6.95238 | -62.93677 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbfaa5fb-7fcc-3465-ba50-2dc186998d7f | -9.20252 | -65.90649 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63b1afc9-61e9-3b62-900a-daf4a3651126 | -10.15189 | -61.14013 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d908d1f5-d750-3593-ac9d-6902e7c0bd24 | -10.34919 | -57.5088 | 2025-09-08 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43120f3d-c573-37d0-b759-02a0735c4a59 | -10.89717 | -55.71674 | 2025-09-08 05:42:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0b10d77b-5d57-31b9-83bd-7cdc64b56a2a | -9.16886 | -59.37817 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0ce93b00-eba1-3e78-9bce-515e797bf00e | -9.12644 | -65.9586 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46e8a55c-978b-3bef-8813-0337eb934c06 | -9.82361 | -67.64706 | 2025-09-08 05:42:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0620c467-92eb-3c7d-a07b-8859e5d40cc6 | -10.42776 | -59.60855 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b7b785e-4e84-3feb-a33e-ef0b474f2a5d | -7.40626 | -61.63452 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed5fca5a-7639-3b6d-a5e7-7b5137e91a56 | -6.82366 | -52.8064 | 2025-09-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 784ecf99-9b77-30fd-8cdf-531b03bbf0e1 | -9.45644 | -56.05115 | 2025-09-08 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25c2feed-96f7-3ab5-9244-bc096aeba8b3 | -9.4699 | -60.48547 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8b6288d-41a7-30ed-9a6a-9db2145077ee | -7.93896 | -61.7963 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35c6bbd7-c47a-340a-ad6c-68fb71ddc2c3 | -9.95509 | -67.19806 | 2025-09-08 05:42:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 299932a6-7880-3b71-a49b-901e236ae5fc | -9.43091 | -62.36586 | 2025-09-08 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a828651-0a48-3ba9-b8ca-d85d7e3ac340 | -10.88613 | -55.71618 | 2025-09-08 05:42:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 805ee1c2-a9cd-3e21-8a76-5cfa713fde7d | -9.0657 | -60.48641 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8221034-7c3d-39e5-a8d4-f0565a502a0a | -9.63098 | -63.10022 | 2025-09-08 05:42:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a262745-48d7-3b8e-a008-2a06adc02bb1 | -9.27574 | -60.91189 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c525161-d09d-3b1e-9097-7b2d7433adb5 | -6.95529 | -62.9412 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b31831df-8b60-3487-8b99-b7ea7b9307ee | -9.47822 | -60.48668 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35f35369-c984-3fef-a406-e2f9c65eacfc | -6.54113 | -54.99829 | 2025-09-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42db1e4f-da22-356b-b51a-58b7e97b655f | -12.83301 | -52.94368 | 2025-09-08 05:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 815a47b7-fe12-350a-89a5-8d053894b2c6 | -6.9676 | -62.93108 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0797d09a-cb9a-3a93-b280-0b92c64f5147 | -10.02926 | -63.47858 | 2025-09-08 05:42:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd042561-fd66-3c0f-916d-7acc792915b7 | -7.10963 | -63.07014 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 634f9794-9eeb-382c-92f4-d0d705a0e451 | -9.44105 | -61.82472 | 2025-09-08 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e2141b0e-9218-3fba-8af4-d981601e3710 | -6.54226 | -54.99001 | 2025-09-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| afa987fb-0733-364f-b1d3-47df4b1ae5e6 | -10.05413 | -59.36484 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 42be29df-e982-3479-a3cf-342ab47903e2 | -7.89787 | -61.78263 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bcec7ff-a802-394e-b975-91b7d248ada9 | -9.18042 | -60.76633 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb62ef1b-7a15-3588-a370-5a12af1a632f | -7.1201 | -63.07174 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d616ca8-fcab-34a5-8c28-aaf4f550683d | -9.44556 | -61.82054 | 2025-09-08 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1048838a-270d-3440-880a-12ba6115722e | -9.8953 | -67.04198 | 2025-09-08 05:42:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bcb1588-3ccd-3c17-8846-dd1319ede1fd | -9.84563 | -53.29565 | 2025-09-08 05:42:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6d67ecb-338a-3f0c-9757-f7ef968dab1f | -6.95589 | -62.93731 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ae5f89a-6065-30a5-a459-ca14b64e8a27 | -9.95232 | -67.19394 | 2025-09-08 05:42:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17ec94f0-eadd-346b-9aac-4972345eb365 | -9.30073 | -66.61621 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb725c67-af14-3e9c-b035-ae43d02397fb | -9.32613 | -67.53269 | 2025-09-08 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a344d96-b5e3-33ce-9563-1aab5bb259bb | -8.3581 | -70.29042 | 2025-09-08 05:42:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28548d7b-7c68-3139-b795-e3e54c248aa7 | -9.08381 | -65.42994 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c50be5fb-0f8d-3844-9741-e2437a587286 | -9.71667 | -62.3982 | 2025-09-08 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e1e187c-be3c-3992-904f-f367a0cfdecd | -7.47026 | -61.59255 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90e02409-37df-3931-b204-ba4ab5992cb4 | -8.87962 | -69.34753 | 2025-09-08 05:42:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28ab61c9-9779-303b-9f35-0446fcd8dd7a | -9.46481 | -56.04917 | 2025-09-08 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46b30920-69d0-37cd-be2e-9245db6c6555 | -12.93493 | -54.78416 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 233f2b35-35e5-3fb2-89cd-07f601d5d847 | -12.94709 | -54.79094 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 52df2175-54d7-3d9a-8012-c0360d70f361 | -12.9413 | -54.78498 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8246b36c-b09a-3ab9-8f72-67bceb93f1d4 | -12.60857 | -56.97667 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4e1376e-c0f2-3d8f-bf6f-5e5cea789cfa | -12.87641 | -62.1078 | 2025-09-08 05:44:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd93f008-6931-3353-b4d6-c95ab86da2a6 | -12.63157 | -56.97219 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f0c523b7-dd20-356a-979c-4c33d4296d78 | -12.63038 | -56.98183 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b24f23b0-b5cc-37c0-8b58-39dc7c085234 | -12.62004 | -56.97461 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cdd30e29-59bd-32dd-8667-befc6bbc278a | -12.62952 | -56.98927 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c7ce2c20-9967-36fe-ab56-028c55d5b741 | -14.88148 | -55.83264 | 2025-09-08 05:44:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 760dca9b-2286-3b8b-bfb8-adf9c40e18b8 | -12.61453 | -56.97382 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e387a21e-bad8-36d0-b3c8-0aaac0a981a6 | -12.95172 | -54.80717 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 105266df-3c60-312e-bf09-c5f9b7e10b07 | -12.42328 | -63.89494 | 2025-09-08 05:44:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86840761-e5c5-3861-bd5b-a3f6942bd118 | -15.66312 | -53.8668 | 2025-09-08 05:44:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9de4021-035a-32de-87e3-12d789a2b3dd | -12.64145 | -56.9831 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37effdbb-2e31-3346-b9da-3763d3d03ed7 | -12.41913 | -63.89848 | 2025-09-08 05:44:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1983a2e1-948f-395b-85f4-898eb2974479 | -14.52651 | -53.98781 | 2025-09-08 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50aa0973-a33c-320d-ac64-2eb7f0ac4e5d | -12.61914 | -56.98196 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 474b8f8f-68f1-3ceb-a89a-61e8a1cb5204 | -12.61959 | -56.97829 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a8348c8e-319c-3978-9ad5-bc9ae5bae098 | -12.60812 | -56.98037 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a95c1bf-7648-331e-8d54-4dff2254f053 | -12.41619 | -63.89386 | 2025-09-08 05:44:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08e0cb40-f6d7-31ef-9053-ae02200082c5 | -12.62603 | -56.97156 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f7f4af62-0d10-371b-be53-9b994abdcad5 | -12.41559 | -63.89794 | 2025-09-08 05:44:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afca7b95-1605-3818-a874-728701a26848 | -12.63126 | -56.9743 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a19d832a-0c69-3646-b20f-19c4d0aae028 | -12.61408 | -56.97747 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 144bbb9f-e077-307c-80c3-71f09b58878b | -11.90946 | -64.96806 | 2025-09-08 05:44:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| df9e9482-80b5-3120-be22-0cc22ce6eb46 | -12.41204 | -63.8974 | 2025-09-08 05:44:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe9b314f-d12a-3f9c-95cc-bb639af56ad7 | -12.61363 | -56.98114 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 40a0ae9a-1b79-3ea3-b515-efcdec77e591 | -12.62419 | -56.98642 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2922c269-a637-30fe-838d-d9eecdc7d7c1 | -12.63616 | -56.98036 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 444f158b-3178-3446-8702-d2f18b879e6b | -12.87247 | -62.10722 | 2025-09-08 05:44:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2338a8af-dfb6-3088-b1d3-e0921bcbbab4 | -12.92973 | -54.77283 | 2025-09-08 05:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72f350e2-2a14-3a02-82ea-148a327154c2 | -12.62465 | -56.98273 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 974b6748-a8d4-3e7e-a1f5-e5a1b9350cf2 | -15.76936 | -53.57418 | 2025-09-08 05:44:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa86e37d-a175-37ff-9884-b5aab7b72685 | -11.91286 | -64.96855 | 2025-09-08 05:44:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b93a79d1-689e-305a-af7d-c075b4e74bb5 | -11.90273 | -64.98965 | 2025-09-08 05:44:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddb27302-5059-3509-a43a-0aa73f2cd64c | -15.25576 | -53.82261 | 2025-09-08 05:44:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f777bcf1-2110-3672-8ebd-21ffe351c571 | -15.24816 | -53.82874 | 2025-09-08 05:44:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 320fadf5-c032-3c0f-8059-cde6934d2353 | -12.35941 | -63.64217 | 2025-09-08 05:44:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2af00d2-35ac-3762-b609-12b8756266a3 | -12.62995 | -56.98556 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f6c2bf7-f09d-300f-a242-54bf6e4b4ba2 | -15.76772 | -53.56792 | 2025-09-08 05:44:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cd7c12e7-09a1-37de-aa41-933a99a76b1a | -14.87592 | -55.82692 | 2025-09-08 05:44:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ce82716-4a29-3a66-bfcd-362125b9a37c | -11.89933 | -64.98914 | 2025-09-08 05:44:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ed7a05c-b2c6-3cc8-8c87-18e7a682c059 | -15.6625 | -53.87332 | 2025-09-08 05:44:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96170bcc-2746-3991-a68a-74c4180642f4 | -12.41973 | -63.89441 | 2025-09-08 05:44:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c3d7e5c-56ca-371b-ba6e-5e22f87d5dab | -14.88196 | -55.83335 | 2025-09-08 05:44:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d7a65dc-2b90-3f9c-9252-12835ababd7c | -12.62511 | -56.97903 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dcff3080-259a-3ffa-a9b1-f612e1d94472 | -11.90551 | -64.97124 | 2025-09-08 05:44:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0cf1300b-c7af-3859-ba28-df3c17d5477f | -12.63635 | -56.97871 | 2025-09-08 05:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README93.md)
