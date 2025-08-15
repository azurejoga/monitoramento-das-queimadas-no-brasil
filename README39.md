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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe46452c-d91e-31d3-b346-b58e896fdddc | -19.47827 | -43.61393 | 2025-08-15 04:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54e240ab-b462-33d1-8d23-dff61dd65ca3 | -16.30268 | -52.91937 | 2025-08-15 04:32:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13e56295-3abb-33d8-a92c-9401c02ed4c9 | -19.55275 | -44.84003 | 2025-08-15 04:32:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d7b530b-feea-3588-88e3-a4a91f2d35a5 | -16.47843 | -51.99229 | 2025-08-15 04:32:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9f7720d-0f0e-3a94-a9eb-028a7a2266d6 | -16.68401 | -49.35733 | 2025-08-15 04:32:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1545c462-fb72-3b6d-ae54-569ba43da116 | -17.6462 | -44.4939 | 2025-08-15 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b91ba71-4d8f-3dc5-be85-56c44a3feaf1 | -19.90569 | -47.47632 | 2025-08-15 04:32:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12b0e50c-3c80-3e2d-b26e-dc8c8696677f | -17.49834 | -47.84172 | 2025-08-15 04:32:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9e3c417-6eb6-38d9-923e-e4ccb7c5459a | -24.3241 | -51.30931 | 2025-08-15 04:34:00 | NPP-375D | RIO BRANCO DO IVAÍ | PARANÁ | Brasil | 4122172 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5ee9412b-e3d2-3302-ab7a-c41674c3e94a | -24.93017 | -49.63572 | 2025-08-15 04:34:00 | NPP-375D | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| efa808cc-acec-382d-a248-eba97d87cf20 | -25.16719 | -53.42263 | 2025-08-15 04:34:00 | NPP-375D | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| f7e920f6-45d1-3433-a6b9-563eb785ecd6 | -28.60382 | -50.63379 | 2025-08-15 04:34:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7fce4ed7-5d67-3a38-88b2-05686130c938 | -28.73134 | -52.35639 | 2025-08-15 04:34:00 | NPP-375D | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e60c6940-6ec8-3445-8e52-16a0daa0cc2f | -9.1708 | -59.6568 | 2025-08-15 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| da55502d-9f0f-3352-a290-c8c5112c7ad5 | -11.3468 | -55.4124 | 2025-08-15 04:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| ff24b0e6-bb1b-380e-a8b4-efde3c590eea | -6.0991 | -59.9459 | 2025-08-15 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| f3b68aaf-e517-3340-b1a1-35503a6a7602 | -6.6945 | -58.8259 | 2025-08-15 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 0558fbd6-34af-31d5-b9c9-7a8ada08b3c2 | -7.5292 | -61.3254 | 2025-08-15 04:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 363aab32-c24f-3652-bcdc-be64fe83488e | -6.9303 | -59.5305 | 2025-08-15 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 74b82c72-2dcc-31e1-af26-5beb3cdfc480 | -9.4992 | -60.547 | 2025-08-15 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| a30d3bec-0185-3534-a037-7e8a53ea1de7 | -6.0808 | -59.9274 | 2025-08-15 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 3b76daf2-227d-30f9-8782-94dbdacfa241 | -6.0623 | -59.9472 | 2025-08-15 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 24cd3fc3-2c44-32cf-8780-72f28152548f | -6.0807 | -59.9465 | 2025-08-15 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 10c16fb3-aa9d-3997-8792-37b4af9b7b67 | -9.1894 | -59.6558 | 2025-08-15 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 5a9f12af-79ef-3e07-898e-d2f3490b98f3 | -6.9302 | -59.5497 | 2025-08-15 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| e34c3b0b-a6af-3ffa-b509-993260ac4da2 | -9.1706 | -59.6762 | 2025-08-15 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 79849af9-27be-34fe-be80-b17f776b0faf | -9.4994 | -60.5278 | 2025-08-15 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 44de1f93-5be1-328f-a1da-c80e0a449b8e | -2.77422 | -49.19735 | 2025-08-15 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea75716c-2e53-3b99-91a1-cdfe80759467 | -7.42781 | -44.58554 | 2025-08-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2e4c92a0-6437-3816-a977-ab73e46869b3 | -6.96716 | -42.87508 | 2025-08-15 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 490043fb-fe2b-31ae-9093-2d45faa94c53 | -4.78602 | -45.33167 | 2025-08-15 04:49:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d83aa90-7edd-3f25-acef-f85ab82e6a8b | -4.59086 | -43.32335 | 2025-08-15 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f431673e-c79f-3db8-82ac-06178062f1bf | -6.22198 | -43.34105 | 2025-08-15 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f4596b5a-9319-3ed3-83f7-6fbfece265b6 | -5.75773 | -46.6687 | 2025-08-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7ad5e7e0-bc37-314b-b7ee-f1efb4f813b1 | -6.33616 | -42.80772 | 2025-08-15 04:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8d94b175-0de2-3fa4-b1d9-7cd86c1c3215 | -6.91072 | -45.20351 | 2025-08-15 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a87e6393-2620-3e84-812e-bd53d046fb5e | -3.43136 | -49.04479 | 2025-08-15 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9f8c1b72-61c2-36ee-8a06-7272cd70d395 | -5.2256 | -43.18894 | 2025-08-15 04:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f2a3d0a-b798-3644-ae2f-092f0c9dcaaa | -5.76628 | -46.66992 | 2025-08-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ea87d796-309b-34fd-a14c-393e7eb10215 | -5.76046 | -46.67257 | 2025-08-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7cb23fd4-fe62-30e3-a0da-9866345f1396 | -2.58573 | -51.92476 | 2025-08-15 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c4ac0a3-2c60-31a5-834f-1177d9061020 | -2.84873 | -48.78144 | 2025-08-15 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cf7d549-cbf5-3b25-883c-977cc40855d2 | -7.15836 | -40.41948 | 2025-08-15 04:49:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 94d194cd-ecc1-3f50-9fe5-b29d09857c14 | -7.14176 | -44.40547 | 2025-08-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18fcb123-74da-3718-9165-d2bb66c752b3 | -5.36732 | -41.23942 | 2025-08-15 04:49:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fe6f3edf-e8d0-38e3-a481-a111d8a81e62 | -5.78169 | -43.60817 | 2025-08-15 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bf0d573d-1aef-3c3f-ae7e-0e633d449008 | -7.38615 | -44.88113 | 2025-08-15 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb451435-0b77-3f51-a0c6-8d78f015476b | -3.95184 | -41.48159 | 2025-08-15 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f7784025-6a90-30eb-91ab-8da629145b65 | -6.96204 | -42.87041 | 2025-08-15 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 02dbd904-49c1-323f-a4c5-387063a5c526 | -7.38695 | -44.87551 | 2025-08-15 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d39aef8-8d27-3894-9334-9cc93234ac28 | -3.43494 | -49.04533 | 2025-08-15 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 24ab13f1-a1e6-34f4-a3e3-0a70f5fd40ae | -3.8269 | -47.7408 | 2025-08-15 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0cab347f-26ca-3be7-a04a-944016d1b057 | -7.42738 | -44.58856 | 2025-08-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 479d2f04-cbf7-35d7-9105-9d86a1150dc7 | -3.81138 | -48.98904 | 2025-08-15 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20691f6f-d59e-3322-a9d3-e38d8f284139 | -4.55554 | -55.96504 | 2025-08-15 04:49:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fb1a9eb-145d-31cd-b515-3585278b6149 | -4.66809 | -48.86335 | 2025-08-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81b94f7c-6826-3cb3-bb7f-9d5d3432de98 | -3.08119 | -48.84851 | 2025-08-15 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0577e527-5755-364a-b0cf-23ae3efd188f | -3.49825 | -43.31527 | 2025-08-15 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9eadd1a2-cc11-3c68-857f-a5d3bb7117bf | -3.32138 | -48.72055 | 2025-08-15 04:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af7c5490-9adb-36b7-9ffe-976e90b93f77 | -4.22821 | -47.2118 | 2025-08-15 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55b5d43c-7ce9-39a4-846f-025c72612879 | -7.29307 | -43.82398 | 2025-08-15 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77ae8f2b-cd9a-35de-8a42-52496919ca3f | -4.59565 | -43.32745 | 2025-08-15 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d89ccf3e-6302-36d9-922a-5eb2855b153a | -6.95256 | -44.54929 | 2025-08-15 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4315a446-c05c-381e-9768-268998c82394 | -4.12309 | -49.43597 | 2025-08-15 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 615f1a16-1f0d-370b-bf70-bb5235cd61ce | -3.37798 | -47.61003 | 2025-08-15 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c21757bd-88c3-31f7-b43d-b37871aa0a44 | -4.22713 | -47.21887 | 2025-08-15 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6458cc3d-ad6d-30d5-bd80-d107314c740b | -4.60718 | -43.32251 | 2025-08-15 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f4541ef-f59d-3903-8445-2ccb7418f54c | -5.61385 | -43.47092 | 2025-08-15 04:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e25214c-6c79-338e-9777-8e7bd3358500 | -6.96152 | -42.87433 | 2025-08-15 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e1b7bc2a-c704-3f50-a5d3-dd73cee01621 | -2.53832 | -47.71621 | 2025-08-15 04:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01293895-b9a1-33b3-b762-85017a42e6a1 | -5.7614 | -46.67332 | 2025-08-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a7cd5aa5-1a08-3e1c-b8aa-a0ef34ae3f74 | -7.61353 | -45.19953 | 2025-08-15 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b327a5a-f832-36ee-88c2-e3beca2a9f1d | -2.91519 | -48.30181 | 2025-08-15 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e3ef7635-69b9-3321-b545-55111f25f64b | -4.2439 | -47.27071 | 2025-08-15 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fcadd311-2efc-3ffa-9d5e-5c77149b960e | -5.75712 | -46.67273 | 2025-08-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cb9d79a3-705c-30bc-8713-2137e77927b6 | -5.70212 | -53.65469 | 2025-08-15 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c3b344c-611a-30ef-b689-0477b4bf8f3a | -7.42821 | -44.58268 | 2025-08-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c52591eb-05ba-344b-b0d2-9af036386b66 | -5.31876 | -45.21928 | 2025-08-15 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec81d870-924e-3549-8035-31ddad9c9b3e | -5.368 | -41.23475 | 2025-08-15 04:49:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 58970595-8e04-3379-bbe2-8ac150670d96 | -6.33152 | -42.79979 | 2025-08-15 04:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c8a336c7-6ead-35d4-afc1-1568485f06ee | -7.39114 | -44.88158 | 2025-08-15 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09e0cb6e-f584-31aa-ae48-d5926e58646c | -3.95838 | -41.47828 | 2025-08-15 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0c9d851b-0601-3994-a832-171f2251a883 | -7.01852 | -44.29832 | 2025-08-15 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca8b39b1-b2fc-3235-9f38-0b3cdbb4e4a8 | -6.95843 | -42.87192 | 2025-08-15 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 1a41655f-4d4c-3b72-91c4-425f011ae80a | -3.64768 | -48.32787 | 2025-08-15 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45196cb5-56c9-3cc1-b469-e8a9aa23480c | -6.96134 | -43.86189 | 2025-08-15 04:49:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 706eb8a4-b8e3-365f-92ce-ab2cb5fa60e6 | -5.82338 | -47.87202 | 2025-08-15 04:49:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a81fd60-5410-36b3-a77d-1dd0710e2f6e | -4.29602 | -48.06237 | 2025-08-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b21a03e2-b886-3358-82cb-80d78aadc88b | -4.60189 | -43.32175 | 2025-08-15 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f54890e-beca-394d-84f2-8f4b6951a8a9 | -3.98957 | -47.88778 | 2025-08-15 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36c7bf81-8793-390a-9c85-dd60e44b76e6 | -7.15906 | -40.41402 | 2025-08-15 04:49:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f3460d7e-6875-3762-b883-f0a05e4ce6a6 | -6.21659 | -43.34019 | 2025-08-15 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6aeb4f24-4d50-32d6-bd94-01f40e9394e3 | -4.66745 | -48.86745 | 2025-08-15 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4c2a5675-3433-36da-bf5a-a53adcacd402 | -3.4935 | -43.31139 | 2025-08-15 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81e1ef98-71b4-38d4-85fc-918a2ba6aa47 | -7.29263 | -43.82721 | 2025-08-15 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d002334-2b92-303d-945b-2fddc1592c51 | -4.70896 | -47.44697 | 2025-08-15 04:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e10c382-ca72-3238-8f47-468c8c35c18b | -5.75676 | -46.66793 | 2025-08-15 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7bc77146-51e3-3856-8256-197a497f90f4 | -7.14765 | -44.4006 | 2025-08-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bed34666-2def-3888-b6f9-28353dfe3207 | -2.90779 | -48.30067 | 2025-08-15 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5db36c37-623d-33d8-b2c0-92df15382b69 | -5.3207 | -45.22215 | 2025-08-15 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README40.md)
