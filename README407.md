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

## Dados Diários - Página 407

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a6e34e7-0229-310e-91e9-70f090de01e0 | -4.6364 | -50.9437 | 2026-10-08 19:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 395.4 |
| b0935482-284c-3b6d-90f5-5562d56a0d37 | -2.8347 | -54.1125 | 2026-10-08 19:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 998a7a3b-192c-3d9d-b144-551810a9ccc6 | -2.6079 | -56.4782 | 2026-10-08 19:20:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 11c51e11-5def-36b2-a44e-04ecfa4b0979 | -3.1602 | -50.5812 | 2026-10-08 19:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 6166c8a4-5e0b-3290-9e41-b3cc5e1e6e89 | -15.9788 | -44.8676 | 2026-10-08 19:20:00 | GOES-19 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 9a7968c6-a27d-3535-8aba-44752835508e | -2.572 | -56.1842 | 2026-10-08 19:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 297.4 |
| d23d8f71-6227-3d5c-b634-1346c15e7ed3 | -6.2164 | -52.7671 | 2026-10-08 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 202.8 |
| 3e72bd90-08ea-383a-8f1d-1b70161a213a | -3.1114 | -53.7839 | 2026-10-08 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 97ab5ebf-e40b-3b62-a848-351f36555e2a | -5.0631 | -45.4466 | 2026-10-08 19:20:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 2f0aa791-ae36-3c76-a677-d20a568422ec | -11.0758 | -44.0299 | 2026-10-08 19:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 8f88b2dd-2a2e-33ca-bed8-6d8ed1018972 | -5.8599 | -53.4586 | 2026-10-08 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 7a1db324-11bd-3290-90bd-43f61b925272 | -6.0021 | -40.9594 | 2026-10-08 19:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 363.7 |
| e472a951-9f87-37b5-8433-21335d23dd7e | -9.5124 | -46.8534 | 2026-10-08 19:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 1c22269c-cb31-32e3-bf73-44ba28ff6155 | -2.5903 | -56.1839 | 2026-10-08 19:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 59292757-7db4-33f6-b7ea-bcba802c72f2 | -6.8319 | -39.3213 | 2026-10-08 19:30:00 | GOES-19 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 116.3 |
| 45ef1ff2-e965-3125-acef-25283898c488 | -3.188 | -58.6241 | 2026-10-08 19:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| e8ed7ebe-9c71-3653-aa0e-88876bf6dec1 | -3.9121 | -55.8964 | 2026-10-08 19:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| cf7679aa-c076-3081-8fb6-7c634e5c21d6 | -3.1115 | -53.7637 | 2026-10-08 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 03db6dbb-6d26-3858-b43a-db64d95107c5 | -5.6934 | -53.4667 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 429.7 |
| be2293b5-6a15-31b7-8bba-f96dbf1522f4 | -11.8503 | -43.5598 | 2026-10-08 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 304.7 |
| d8e26250-835b-30d7-b089-36c99d3f60cd | -13.3671 | -43.8742 | 2026-10-08 19:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| b9fe5cf6-fe3c-37b6-8c30-56faeb56caae | -6.4596 | -55.0415 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 150.9 |
| dd4c1223-8813-343a-a158-72f68d7b5dae | -2.4942 | -58.0768 | 2026-10-08 19:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 31c67f68-c9d3-32ec-8859-07008b8cea1f | -2.572 | -56.1842 | 2026-10-08 19:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 257.8 |
| f58fcf69-f198-33be-8549-184931bad92a | -14.4339 | -43.9396 | 2026-10-08 19:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 745692f2-2292-358f-9fbf-f2cd8721a325 | -2.8228 | -58.361 | 2026-10-08 19:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 77450f09-327d-3c4d-b598-4288c07052dc | -5.1133 | -46.2048 | 2026-10-08 19:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 83.4 |
| c95f1288-d52b-3037-9ac6-0cc8ef552e5b | -6.6814 | -55.0903 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 658ca734-c450-36e0-a6ef-2aff32b46183 | -8.9302 | -45.2041 | 2026-10-08 19:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 236.8 |
| 80dfeaa3-30ce-3b84-831e-c61410c3d5a4 | -4.6642 | -56.2083 | 2026-10-08 19:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 0ac319f7-2bc6-36ec-865a-d7a05c269c1a | -3.8911 | -42.1187 | 2026-10-08 19:30:00 | GOES-19 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 29a3f4cc-dde9-3a51-a9c3-b448d66eb347 | -3.2533 | -50.3899 | 2026-10-08 19:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 414edbec-dbbc-30f1-aa2a-f955df9df697 | -14.4591 | -41.1854 | 2026-10-08 19:30:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 137.3 |
| f8c0fb29-6f91-3ec9-a380-4a0a85e9d88c | -3.2582 | -53.8808 | 2026-10-08 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| be547b16-aae0-3eb0-816d-b18bdd9a14f0 | -5.7119 | -53.4658 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 348.8 |
| 17ed79e9-262f-3691-89db-91774189949e | -6.2157 | -52.8695 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| f8b1210c-8c36-320b-bed2-7e49a5145866 | -11.8311 | -43.5628 | 2026-10-08 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 243.4 |
| 91b610fe-792d-382e-a71a-bd78ae47977b | -2.8256 | -51.2779 | 2026-10-08 19:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 134.2 |
| affc33e7-d884-3b87-bc57-1eec05d3c152 | -6.0076 | -53.4919 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 168.3 |
| 6bc53634-249e-3247-97d8-7a9fea8646fb | -5.9586 | -55.3648 | 2026-10-08 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 4ff9339f-6825-3e25-bd08-7eb058a3e316 | -9.0362 | -44.3654 | 2026-10-08 19:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 678d9e3d-da6f-33f5-adc5-64cc772a1e31 | 1.6937 | -55.6263 | 2026-10-08 19:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| c2571ed2-e1d8-3f8f-a216-87c66b938b88 | -6.0024 | -40.935 | 2026-10-08 19:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 144.8 |
| 049b263f-1552-3b69-9358-055f1f71fa6a | -2.4623 | -56.0682 | 2026-10-08 19:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 5c3f7338-4f86-374e-9302-9d2f1f2341a1 | -7.1825 | -52.6283 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 152.0 |
| 428a89e0-e7e7-39f1-80c3-3e527e983dc6 | -6.0075 | -53.5122 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 0281fbdb-f4ec-3878-93c6-50dd737dd3ac | -6.1242 | -47.9444 | 2026-10-08 19:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 6e968da4-e5ce-3c92-b431-c447344986f5 | -3.4312 | -56.9307 | 2026-10-08 19:30:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 90e3e875-ff98-337a-8c03-df3f816b2a8e | -6.5322 | -55.2577 | 2026-10-08 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 87bd992a-7ee9-3418-9580-d5518a8fee60 | -3.2532 | -50.4108 | 2026-10-08 19:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| da9bfbd6-8073-3bc3-a407-9abbd2f45138 | -9.017 | -44.3907 | 2026-10-08 19:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 721ab2d9-5434-3c4e-994e-db5fe2d17811 | -6.2164 | -52.7671 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 145.2 |
| ed1f8940-2994-32f6-b095-bb0dd265a81b | -2.4988 | -56.1462 | 2026-10-08 19:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 98d4bc78-9bcc-3cf6-a073-105b2baad656 | -8.9305 | -45.1812 | 2026-10-08 19:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 7c70a0e7-5d0b-3983-bb38-46d76ed5b87b | -1.5302 | -54.8151 | 2026-10-08 19:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 40f3ad15-3f94-36a7-bbe8-f39fd93e4249 | -5.2352 | -56.109 | 2026-10-08 19:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 62a4a95b-ca10-301e-8fee-33cd125726d0 | -3.1697 | -58.6244 | 2026-10-08 19:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 24a0f51c-b819-34e2-9ee0-662d094c1929 | -3.93 | -56.0143 | 2026-10-08 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| bfb7e51c-f95e-3c6c-b9d4-11fa94e11deb | -5.8842 | -43.4199 | 2026-10-08 19:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 176.5 |
| bc37141d-4538-33b9-b18f-ce592368a248 | -2.5125 | -58.0765 | 2026-10-08 19:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| c4110429-725a-3d55-b768-cc671e97e1f2 | -3.3912 | -58.0017 | 2026-10-08 19:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| f88d8e53-8689-36d2-97bc-5526118377ed | -2.4806 | -56.0875 | 2026-10-08 19:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 6508f837-7615-342f-8ac6-a14efba50311 | -6.1429 | -47.9432 | 2026-10-08 19:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| d29a6fbe-34b5-3d22-8d49-d228098611f2 | -11.0754 | -44.0534 | 2026-10-08 19:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 9a50155d-69a8-3dd3-b8bc-de9a10f2eede | -5.712 | -53.4455 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 157.6 |
| 520648bb-5f07-38a1-a84b-e34c7b4e080e | -6.1041 | -55.7162 | 2026-10-08 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 153.4 |
| 2d0da9e4-e1b8-3c28-a39e-d4314d1bde5c | -1.3447 | -56.3979 | 2026-10-08 19:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f2277120-8842-3e6c-bcd2-5df99dc091af | -1.7864 | -55.0306 | 2026-10-08 19:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ec639c0d-5adf-3c41-af30-9ef4d78cd687 | -3.2136 | -42.9764 | 2026-10-08 19:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 9bd4cc8c-c07c-3d8f-ac77-ed24619c9b88 | -11.755 | -43.5275 | 2026-10-08 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 0ca1c92a-2b89-3c2d-b16e-a22b53942400 | -2.6262 | -56.4778 | 2026-10-08 19:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 6773ad3c-a405-3048-a703-2700e2ed291b | -3.7439 | -41.7217 | 2026-10-08 19:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 8f882d1d-3b3d-3726-8419-4bc5f18ea664 | -14.0472 | -43.8222 | 2026-10-08 19:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 9f9457e8-a654-3dd4-9192-67a9a9f45bee | -6.6027 | -37.8944 | 2026-10-08 19:30:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 128.8 |
| d60b3ddc-007d-325f-b68d-f8ec93a3f7d2 | -2.9005 | -56.6685 | 2026-10-08 19:30:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| e02ddeda-5428-3f29-b337-f1b5d517b902 | -6.234 | -52.8889 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 184.7 |
| e509dea4-31aa-3737-a883-31b2d41d5e3f | -2.5903 | -56.1642 | 2026-10-08 19:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| f7ff545a-2ff8-3d60-82f2-86cc35d3b2ab | -3.2956 | -53.6984 | 2026-10-08 19:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 137.6 |
| e5eae89c-8054-3b33-ac94-251b0dc0b1c0 | -4.0838 | -44.1159 | 2026-10-08 19:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| b9f907ac-30cf-32bf-8012-4284782e7ce5 | -3.5726 | -58.5581 | 2026-10-08 19:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 27179c94-a7f0-39a8-9e5f-066d87bc36ad | -7.4694 | -42.8551 | 2026-10-08 19:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 95642eb6-c9be-34f8-80a9-ec7cfd8f4785 | -2.77 | -57.5293 | 2026-10-08 19:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 70c9d903-2e78-3df0-8427-ae543166b9e4 | -2.8895 | -54.1915 | 2026-10-08 19:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 690fc4fb-4be4-37e5-a668-b95979dfc0f2 | -6.0386 | -51.7261 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| d11db433-89a9-33f3-99eb-8b14784d70c7 | -2.0834 | -46.5765 | 2026-10-08 19:30:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 8c8b9341-123f-396c-a6bc-9151896468ba | -15.4026 | -44.3207 | 2026-10-08 19:30:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 115.5 |
| ced40305-30cd-39fa-91e9-5d8a9b6d5d69 | -7.089 | -52.6958 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 266.5 |
| 02327656-1fe5-3716-87fd-9e37a0982bb5 | -5.6932 | -53.487 | 2026-10-08 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 291.1 |
| c2ad13c6-58d6-330f-b1af-7cb8db091c2c | -2.4623 | -56.0879 | 2026-10-08 19:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| eabea46c-1d4f-36d4-aad1-6ac208dcc99e | -2.8346 | -54.1326 | 2026-10-08 19:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 7a69fcb2-6917-3094-9894-bdfb2104cb8d | -6.1042 | -55.6964 | 2026-10-08 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 63cbb43d-b53d-3b41-9902-2ad13af60fd9 | -2.8896 | -54.1715 | 2026-10-08 19:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 04d6d06b-09d7-3822-99a9-8d5e9c8d5db5 | -5.4958 | -42.8413 | 2026-10-08 19:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| ddc040ca-0493-33ff-bbb5-8e5d2d75bee0 | -8.0766 | -45.6112 | 2026-10-08 19:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| fcef48df-47d7-3397-b54c-494af4ecc02d | -6.1484 | -51.927 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 9bab5860-c114-3f02-ba88-5163073d00bc | -6.1617 | -52.6471 | 2026-10-08 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| d5e316ec-59b8-334a-8166-2bfec6cca36b | -4.6364 | -50.9437 | 2026-10-08 19:30:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 451.2 |
| 97121aa5-0c32-3f9b-a9d8-5fd2aa538594 | -2.4987 | -56.1856 | 2026-10-08 19:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| fa37d4e5-b801-3bda-83ec-3fde467fc98b | -11.7335 | -43.649 | 2026-10-08 19:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 82949105-a770-307e-bca8-892820c27706 | -2.8434 | -57.4696 | 2026-10-08 19:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |


[Clique aqui para ver as próximas entradas](README408.md)
