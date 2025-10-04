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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 267bc580-2b0f-3ce4-87ec-0a96b8547fcb | -11.71835 | -44.43971 | 2025-10-04 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa9e2e5e-1c02-363d-ac3c-77b29580e158 | -8.13676 | -44.08272 | 2025-10-04 04:14:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cda1be9b-5b27-3bf8-a260-7a4d28f7ab73 | -15.30856 | -46.30561 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f88c62c-ed0a-3187-8f73-50615856e623 | -10.33222 | -50.32946 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fe806461-85aa-37ae-9027-47c16c5500ef | -11.79016 | -46.82278 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 61466cca-4828-3678-9f7d-9be4df154ef0 | -10.93124 | -44.26156 | 2025-10-04 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a858d41-c245-3a68-b91e-d3d1152ff894 | -14.69483 | -48.09187 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50a2bfe0-ae17-3df7-b2ad-eed9332567bd | -11.66327 | -44.27212 | 2025-10-04 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38ecbe6e-3c57-310c-b780-a6300b2bee1f | -14.91563 | -46.89608 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64f1417b-ff47-3f40-a408-ed7b80729852 | -14.32087 | -45.86073 | 2025-10-04 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6706c1ff-6a31-370c-b1c0-630e3428b28c | -11.82896 | -44.91719 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48ad2769-6f97-3198-98ed-e449978ad443 | -12.68513 | -47.56772 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f761afb3-d9e5-3314-b31b-fe936589ebba | -10.53334 | -44.52027 | 2025-10-04 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11239e38-c02b-37cf-8130-3ef1d2492171 | -12.04926 | -45.1757 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf23e7f8-f1cf-35f2-ab62-c6834c15ec65 | -13.20681 | -47.8161 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7bbcd675-af9e-3ebc-8cfd-a049db5d50ee | -11.9061 | -46.3574 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01429556-227c-3994-af51-5b0a91169267 | -13.33459 | -47.19553 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5123f4d1-9af9-3862-90ed-7dfdf4797dd7 | -13.70134 | -47.34362 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 696b79b0-d45a-36c5-b54c-82996262170c | -14.94263 | -46.86041 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0b54e8cc-fdf8-35fd-8464-f08af296bb77 | -11.79636 | -48.92237 | 2025-10-04 04:14:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1c0c6e5-8b1f-322b-8e6f-423489507141 | -11.82556 | -45.04433 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51527f29-f2b3-3cee-b8b9-e4b92800cb0c | -15.31385 | -46.37851 | 2025-10-04 04:14:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef56910d-bf42-385b-9f4b-71259e69de59 | -11.87415 | -44.97561 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32979902-9e57-3d13-8946-6eb76f2cdf62 | -11.45277 | -45.14703 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 14cb2818-4f70-3407-b2f1-0659692bfd2c | -13.99868 | -48.18855 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a9b6e1a-8b20-3e84-a5e4-f80486108746 | -13.30793 | -47.5698 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e7bf2b9-3173-3761-9b43-216544bf4722 | -11.85763 | -44.95099 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 191ecd64-1868-3b7f-ab3e-f316232f64ef | -13.97999 | -48.12167 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 941dcf4d-d5fc-3f20-a81e-76991b7092e3 | -11.45636 | -45.14006 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 472a67e1-3e07-3f81-a003-fc9a0104a6d0 | -11.85706 | -44.95454 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76c295aa-5f05-3072-8d3c-fa10402f3f75 | -8.5386 | -50.16177 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c22e36b-8b46-38f8-b08a-cba29734af62 | -12.23575 | -44.02287 | 2025-10-04 04:14:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29835fed-35d0-3fdc-93bc-95bbb6533e52 | -9.9345 | -50.89681 | 2025-10-04 04:14:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42fc7726-1c50-3e7a-b055-aea9860be346 | -14.21629 | -46.06739 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37687cc0-20ad-36b9-9719-b2b0e2cbc571 | -11.86331 | -45.04327 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc6d8ef3-9114-35cf-b57e-bacc5543d632 | -8.61824 | -54.97711 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78a098be-87e5-3a43-8536-9ccb3d79701a | -11.48146 | -45.02723 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c743d84c-7fd9-3a55-b77d-9910a31d3cfc | -14.38869 | -45.94291 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61579316-0852-3eb4-bd20-ff6923000ec9 | -8.96282 | -46.75348 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbfa9665-1ce8-368f-be3a-250cac8d171f | -11.95685 | -51.47976 | 2025-10-04 04:14:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddc210e3-2f49-3ca9-bebd-2c056290041e | -10.32706 | -50.33299 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 92153da9-a759-3f21-ab9c-d41c5ea14625 | -13.11969 | -47.842 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3913922e-e18b-3e29-9635-066efca3a20c | -14.24203 | -46.09051 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| b326bf7d-9a57-3be1-81e2-ae62ecda9148 | -14.97985 | -46.84756 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fb8b891-37c5-327c-bd7e-52b9e2bfaeea | -10.33676 | -43.74611 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79a71f04-8a20-3e99-a090-8bb908183384 | -11.14674 | -47.1751 | 2025-10-04 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e89dcb02-c7ac-3337-8815-4da12e645667 | -13.32812 | -47.62487 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cda757f9-0255-33d7-8d72-6c600624703f | -10.59566 | -54.35226 | 2025-10-04 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b263e217-d269-3578-91e9-61e5f4542cde | -9.92479 | -50.90219 | 2025-10-04 04:14:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f000bad-c2b3-38a8-84ba-982d48ec7a1f | -13.96837 | -48.10204 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5415b1f9-8201-36b6-b601-89652eb2394a | -11.91371 | -46.36977 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 470a91a7-0ab9-3087-a3b3-fead42b8d8d3 | -11.69712 | -47.51239 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d3a5bb67-c1be-3c23-90dc-ac6aa6f45bba | -11.49112 | -44.98859 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8dd0088-316f-3501-aafc-5436bf6c3e2e | -10.27704 | -44.33852 | 2025-10-04 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 962a42f2-e1cb-3cdb-84ee-517a0ecf2607 | -11.15391 | -47.1764 | 2025-10-04 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53b567da-9581-3368-9313-01587363ec6f | -15.33657 | -46.30309 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c18fc8dc-65e6-3132-9767-2c23d0b22d61 | -13.13123 | -47.81812 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 70a887c8-cae1-3c82-b511-c010a9144ae5 | -15.32652 | -46.30121 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e8ad9262-b7ec-3971-9479-0a6287e52e10 | -12.38223 | -46.5106 | 2025-10-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5eebf90f-6605-3d81-a852-582c0c827570 | -13.35313 | -47.23565 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c956ae4c-417c-385a-9e48-98f8797785d1 | -11.07938 | -47.88449 | 2025-10-04 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5cc08ac6-60e7-3767-81d9-f48abcff441f | -8.53972 | -55.02154 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5664dcc3-ff86-3b38-84c0-3bf24f9528f2 | -14.59351 | -48.35248 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 899b47e6-ff6f-3fb8-861e-00be928d5999 | -8.63423 | -43.98705 | 2025-10-04 04:14:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a373b6b0-a5f0-384a-b2ec-c859478abba5 | -14.41944 | -46.3552 | 2025-10-04 04:14:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e96f22dd-ae68-3bc5-8324-66bc91d7a3f9 | -8.84705 | -46.81775 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9837db52-97f1-32d4-8578-08c192612729 | -10.71482 | -47.88375 | 2025-10-04 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02a9e830-e045-30fa-bf4c-b0736318b2c5 | -11.91016 | -46.3542 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84458a73-669f-3d33-9ee4-f29a5f192d59 | -14.21115 | -46.07786 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c83c20dd-fd78-36d8-9bee-5ce74d1e0912 | -11.13933 | -47.85646 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7a2854e7-7b29-32bb-bdc5-69435c35fc1c | -13.93187 | -48.16172 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e77d9735-8566-3717-8993-696a6efa38d9 | -14.16829 | -49.20925 | 2025-10-04 04:14:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d677d214-0368-3239-b94d-b2fa73ad3621 | -12.07448 | -47.99143 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e8b2d5e-eb38-3307-bd4e-609a309a12c9 | -13.10378 | -47.89121 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 5dc13790-72aa-3a8b-aaeb-13d3872413cc | -8.42631 | -46.80034 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 005432c7-e687-30ab-af54-c7c1aeb5e12e | -11.92237 | -46.40276 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae9cf15a-096b-3ced-89c2-a3c99a907d1a | -7.74205 | -46.31285 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 2a0d7914-dc47-3294-9180-c8fe5dcc1c52 | -14.6398 | -48.12489 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a7ea33e-2807-3ee9-87b1-1db45fc78b01 | -11.11139 | -43.39484 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c6555c84-54b2-3c34-b8fc-3a11999ef891 | -11.62682 | -47.97645 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c19e72ab-51f7-3f3d-a387-fbff9ad20051 | -10.9308 | -48.82895 | 2025-10-04 04:14:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0772716-5381-3e10-8b7d-27ed64b3045d | -8.20038 | -46.98972 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 24d0d2af-246d-3557-b03e-17b2a04433b2 | -13.13207 | -47.83498 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e10093b-94d5-3895-bef1-70c06b4fea27 | -9.63328 | -54.31145 | 2025-10-04 04:14:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d64980e8-bcba-3e7c-9748-f20eab7805c6 | -14.2845 | -45.87325 | 2025-10-04 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b2a3479-283c-3456-b195-445799d84b09 | -8.92167 | -46.0613 | 2025-10-04 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc924451-8995-3a65-911b-37a2a9a64076 | -8.62428 | -43.98547 | 2025-10-04 04:14:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 292f1c77-08d7-3425-a7da-893bca2e63ad | -11.80853 | -47.93962 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97147f4c-ece0-3982-97d7-6234fdfd1cba | -12.818 | -46.86153 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 73eeaaf0-c218-3002-85c1-9562c8ee7aac | -8.84925 | -46.82693 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a854a8a-4604-355d-8eec-771d073e1c4f | -11.11471 | -43.39535 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a6f07db1-a9c8-3aa1-ba95-75a146c3e095 | -14.23899 | -46.109 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 633b6d96-c2fa-3ac4-a27b-227b3354166a | -13.13266 | -47.8097 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e30e0657-e7e6-331d-b76b-4f0bfa979029 | -15.34053 | -46.29994 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91b223f3-344c-38f5-8bbb-89aec8006581 | -8.13897 | -44.09027 | 2025-10-04 04:14:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 543e5835-1155-3d52-892b-42602b81b97c | -14.98281 | -46.85168 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90cc2d81-0d44-3a65-bed9-446bda7d5938 | -13.31179 | -47.26623 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fcdebe7a-cd27-3000-9333-094cc42f085f | -12.41614 | -45.15613 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 923f7b00-cc02-3ce6-bae1-fe01a84959d1 | -14.98963 | -42.01717 | 2025-10-04 04:14:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7d7c4867-3eba-30b1-8010-3fddd9c8ebd5 | -15.91146 | -43.34156 | 2025-10-04 04:14:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README83.md)
