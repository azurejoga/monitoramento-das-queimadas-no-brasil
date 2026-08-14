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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a36fba88-414a-3adb-a3b6-d04fba130da3 | -9.19489 | -66.10258 | 2026-08-14 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 535b1e97-8f9b-317a-bc27-91673ff3b41d | -6.61362 | -59.04258 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4931c1ef-99ac-3335-a0eb-a269a7f3c8ac | -9.59769 | -60.50708 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d061ef06-c191-3c80-bb11-6d17aa19fb66 | -10.97467 | -50.5411 | 2026-08-14 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a1708fb9-6598-3236-8006-97ba63c43b19 | -7.70417 | -46.23594 | 2026-08-14 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c5bb4b6f-ada5-336e-a321-5b20e04e676d | -6.60586 | -56.34756 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14990388-60e6-3b29-854b-6cf8832cfa42 | -6.60354 | -56.33894 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b7f54c4-821a-339a-a68a-93e92aff57f8 | -6.93987 | -52.79131 | 2026-08-14 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72387f1a-e64d-31be-ac62-4d72439994db | -9.18608 | -66.10114 | 2026-08-14 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bde51799-a3fe-3236-b7d5-bec69aa3e949 | -6.96064 | -59.28224 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5013137-a524-3ab0-83aa-140595dd2d38 | -10.59291 | -55.58491 | 2026-08-14 05:18:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01b0228d-7c60-3c99-9acd-318eb9a08b58 | -6.93547 | -52.79058 | 2026-08-14 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 513c9002-a0cd-3f9d-9533-052aa6b29e3c | -12.02884 | -47.82649 | 2026-08-14 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b005ad99-43dc-34dc-a568-a91219f6e485 | -10.82789 | -50.32342 | 2026-08-14 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56267971-ce39-3a3e-b5b5-c427b39e05ba | -6.60113 | -56.35491 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6806a92-3e41-32e8-ad0a-7a19e7aa21cb | -9.76296 | -60.75452 | 2026-08-14 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e3c218f-aa4a-3a75-bc93-9a9199eaab0b | -6.78425 | -58.75447 | 2026-08-14 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31ec0c28-e3e4-32e8-a204-6fd5e4c1752c | -6.83366 | -56.42064 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8fed95c6-e727-34be-a188-a65dee8906b4 | -11.62145 | -55.18294 | 2026-08-14 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26d105dc-82d5-30b6-a863-f774e3c423c1 | -9.59605 | -60.49599 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea830ad7-9c90-354b-bec6-872aae3c37ed | -11.20485 | -54.82812 | 2026-08-14 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11c0544b-312c-3da8-abb7-22041dbdad3c | -6.59347 | -56.35782 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fd22bb3-801e-3fbe-b7dc-baf77595c882 | -10.69803 | -50.51535 | 2026-08-14 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbe3e882-2ddd-326f-885a-a19d6b49bb36 | -6.61692 | -59.0431 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 62538056-294a-302d-af73-de167b5f0df3 | -6.83718 | -56.4212 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06f749c5-a997-344f-a39c-5c9855b77571 | -11.0677 | -50.94831 | 2026-08-14 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97438439-b458-3771-8078-a0453b96fde2 | -9.07957 | -61.38921 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99698919-58a9-3f9f-b133-6ebce8fb0731 | -6.78148 | -58.7505 | 2026-08-14 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd1459c1-76cb-3a3d-9fbc-e5a2e4a3b6ba | -9.59881 | -60.50004 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4ae3504-96d0-3343-b2ca-ab0d01f57a3d | -8.95497 | -60.56982 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae7518e4-e137-3e05-abb2-1a35a590ec29 | -7.37845 | -59.95675 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 846b121e-241d-3241-b012-47193aa9ccda | -6.96672 | -59.28672 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8968950f-2f74-39b5-a6dd-9d66fdb96974 | -8.96119 | -60.5092 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cb2b212-568f-3993-a2ef-bc5bc82934b2 | -9.77115 | -60.76371 | 2026-08-14 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83f4c014-5812-3c6e-ab55-8db3d821f7e6 | -6.60122 | -56.33033 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ff424f6-87bf-38a6-89dc-158d472b7d2a | -11.49411 | -54.62683 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 544d2369-5f44-38fc-a42e-c5fa9d74e2ef | -6.61731 | -58.99714 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33964841-20fe-3d83-945b-53e49a4e6e1b | -9.58632 | -60.49443 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b60ea611-23cb-385b-889c-09930b5e7093 | -7.40395 | -59.98928 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f253001-3d70-3101-88ca-5cbd30136d78 | -8.02075 | -55.11966 | 2026-08-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 395b71c9-2223-3d66-9ca3-ed4d782e0791 | -6.78202 | -58.74702 | 2026-08-14 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 736a20d0-5818-3fea-a19c-5a0074263705 | -9.77188 | -66.614 | 2026-08-14 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 163da88a-081b-372c-b9de-732bf85b21f0 | -8.95393 | -60.5334 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 361808da-c78e-3ae2-a958-59cd22bc8d27 | -6.58871 | -59.00685 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f594c62-933b-3fc7-8d3d-54c4ab41ef96 | -11.80655 | -51.80657 | 2026-08-14 05:18:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee170015-0d75-36e1-b32c-4f07badd1f57 | -8.95337 | -60.53693 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd5bd6a4-8d3a-3e30-ae70-5038f4f4c94b | -6.63341 | -56.26117 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f05ed9dd-d85e-34a0-bf31-f08666e595f5 | -9.33292 | -59.26581 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 692d1d75-a96d-30c2-9617-f438832a3462 | -6.6083 | -56.33139 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72f72651-a0ad-3c06-8628-c23b5ef92c25 | -11.80787 | -51.80405 | 2026-08-14 05:18:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2ec8b1e-3df2-311c-a469-05bfc5db74fb | -9.58798 | -60.50552 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2e91dc5-be45-34ad-864f-ee1f33f007b4 | -6.62408 | -59.04067 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ef0f535d-b43b-327a-836d-9d618b05ae21 | -9.58466 | -60.505 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81c12f10-7dcc-3cdd-80e4-a19a4d1a48f9 | -11.4988 | -54.62356 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d57c1b90-b46f-346d-afc3-c04f2955b4e5 | -6.79033 | -58.75897 | 2026-08-14 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b07e28c4-c5c1-33ed-8c13-04e827957f1a | -8.02272 | -55.12173 | 2026-08-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b65687d1-7d37-3893-9b5f-f42adf8ecfbe | -11.80336 | -51.87846 | 2026-08-14 05:18:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7294de4-81a6-3bfe-ae48-3f76a9e56276 | -7.58623 | -61.21908 | 2026-08-14 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f096c3d-19c6-385d-9faa-d2bbe1ab434b | -6.01832 | -57.83704 | 2026-08-14 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2d7998f-d66e-31db-b2ce-315359b6b4b5 | -6.5982 | -56.35038 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c66b9f6-32ee-3bc9-94d2-f0aa77286b09 | -9.76629 | -60.75506 | 2026-08-14 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e58a78e2-efb0-3279-90c9-ef904774d301 | -9.07617 | -61.38866 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb245b17-0ff7-3448-adcf-c10499678e98 | -10.37997 | -53.87259 | 2026-08-14 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48702d64-959a-37e0-ad62-a95830ed3c32 | -7.85313 | -56.59677 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4ea1f3d-eb61-3840-bbf1-7edb647baad0 | -9.75681 | -60.77174 | 2026-08-14 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f944d8d-6fbd-32ed-a45c-8d544b6e2f57 | -7.71166 | -46.23157 | 2026-08-14 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 76214ed7-f897-3ce5-a2c4-b7a0a294917d | -6.59586 | -59.00443 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b5927b6-b041-3fbf-a2ef-d8691e8d5450 | -11.23756 | -54.83296 | 2026-08-14 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 606710b8-b69c-3af4-b161-fd76e4240e5f | -8.89606 | -60.60041 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8051f8da-dcec-3712-ba0c-3c3af7c713ca | -11.24524 | -54.83775 | 2026-08-14 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41447fc0-4c8f-39c3-9350-02b423ffcb2c | -11.49099 | -54.61858 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0c45b9b-a09f-3ee7-a1fa-79b517b78add | -8.89611 | -60.55687 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3a022219-6ac6-3f77-8e13-dca0f87d880d | -11.27083 | -54.83367 | 2026-08-14 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95f3f861-7f7d-3c34-bcd3-b99945c2bf19 | -9.98598 | -53.95111 | 2026-08-14 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1baa96a0-000f-3bf6-b4ce-258d7f477c2c | -6.60233 | -56.34698 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a48e271d-6b0b-39a9-ade8-4d883597faf3 | -11.07255 | -50.94441 | 2026-08-14 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 071f4428-ab82-348d-908b-12f791196e01 | -6.98173 | -63.00902 | 2026-08-14 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d44b0a7a-57b7-3f78-9e4e-fc973dc0f015 | -9.07499 | -61.39605 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0266b00-defc-348c-adc4-8fd46ff448be | -10.6976 | -50.51889 | 2026-08-14 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5904f604-062e-399e-a427-aac9a60fc2d9 | -11.84995 | -51.91196 | 2026-08-14 05:18:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8f642c9-6cb0-31eb-a4f4-b626947f1579 | -7.05906 | -56.51267 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0864a9c-8c8d-3fc8-83e7-fefe64cd7840 | -7.3768 | -59.96724 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d48257a6-eec5-38f3-8716-0505ab29536c | -8.96509 | -60.50621 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 070f60ac-5787-301d-84b5-1e3246cec279 | -11.20436 | -54.83181 | 2026-08-14 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2ee3ecb-85e0-3cc0-a996-3c2a28d350f7 | -6.62684 | -59.04464 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bd48f7b-954b-3797-ae22-57c27b86275a | -9.98173 | -53.95044 | 2026-08-14 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 49559d55-0968-3001-8256-104048145b82 | -6.96564 | -59.29364 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cc2c6286-f852-3169-a525-0e8cc3c29a34 | -6.43144 | -60.07229 | 2026-08-14 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9467399-a81b-3263-af69-73042afaa52f | -7.41281 | -59.99784 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cda17b88-4a1e-35ca-9520-f8868e986bac | -7.40561 | -60.00029 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e52319fd-b1a6-3571-9f61-8e60e3889efc | -11.50087 | -54.63942 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| abce01d0-57a4-397f-99ca-cc2a7767a845 | -8.95947 | -60.54153 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33356916-17cf-31da-9a2f-ecc46dff3942 | -8.6073 | -54.67644 | 2026-08-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8e4c0c2-cdea-3e88-abfd-2b0c5e3f3071 | -6.89068 | -59.01197 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e4a2b7b-cf9f-3553-b35a-ff06abef7bc6 | -7.38399 | -59.96479 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e11c9077-adc3-3743-9c23-9e75a011b2fe | -6.59699 | -56.35841 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c83aec7-6021-3164-9b0a-888c70f3c79a | -10.98102 | -50.53474 | 2026-08-14 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 54f3dbdf-969b-3532-adcf-1691148c27db | -8.89555 | -60.56041 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 969a20de-e20e-322a-bafa-1606aeb8038c | -11.49568 | -54.6153 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9e9f9a55-b4d8-3a48-8ccc-04e0ac34a19c | -8.55628 | -54.60608 | 2026-08-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README31.md)
