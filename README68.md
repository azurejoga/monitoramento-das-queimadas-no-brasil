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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89010ede-5403-376f-b3d5-b0008039aa62 | -13.01493 | -56.88665 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a228919b-7204-3fad-b366-5b60fc2d3fea | -14.77664 | -59.73893 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 600849d3-fe39-3c03-8e9f-e12a0bc53404 | -9.11819 | -65.78154 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b628f1d-469f-3f51-bd4c-3c7f45a37008 | -12.43612 | -63.91261 | 2025-08-29 05:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7002e983-9c98-369a-b52f-fe33b413a2bd | -12.93334 | -56.97157 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d4800bc-8d5f-3fc0-a37e-c5426f008b28 | -15.19125 | -52.34001 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e5d2070-0e13-3315-a67f-c0ce10e7f60b | -12.85346 | -48.14032 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c892ad0-7285-3fea-a05a-47c951ce5e96 | -9.11013 | -65.7681 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 6cd2016f-3b45-3801-bab4-0d76a1c0f41c | -13.42253 | -46.98047 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 6d19bb6a-9e35-35ef-9ec5-7cbe474d9b66 | -13.6369 | -48.20208 | 2025-08-29 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb6f7851-39b8-3522-8bb9-8dc7b1f6587d | -11.35394 | -43.56455 | 2025-08-29 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 249a7d96-699e-3362-b6b6-25545171f26d | -10.72769 | -47.01854 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7d421ca-7a2c-3b8e-8d5e-9d5be62ddeda | -10.36643 | -57.81791 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 89492175-fb48-3c26-9051-5e02d0c7b96b | -10.94928 | -46.85752 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f643fa38-e18a-36eb-9716-de3ffc5f521c | -13.67238 | -46.91372 | 2025-08-29 05:08:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9011b290-3ade-36e2-a391-e5b4687165c1 | -9.11502 | -65.79913 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba7e2028-4db3-39ee-8e26-82c5c8d3d681 | -13.19506 | -45.29241 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2138d9d8-0493-3661-bbaf-2a49154f3930 | -11.09126 | -65.15509 | 2025-08-29 05:08:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 353c166c-7c64-3954-ae20-e4645d504b1c | -13.50313 | -46.85251 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a480d474-cd1a-3b9c-8d2e-e2a514febe98 | -13.56604 | -46.86385 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b98a000d-5b1f-3e07-a63f-1aadb3ef1b71 | -13.40224 | -46.96595 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7849e381-dd4a-3298-8f36-dacb1c833f72 | -9.29782 | -56.81699 | 2025-08-29 05:08:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cda89182-3d2a-3a58-ae60-3e2d57c5952d | -9.15228 | -59.58781 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b1d17ec-d11c-3ea3-9e39-b0637d0fd863 | -10.37759 | -57.83461 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 071266b3-26c3-3dc2-adf4-1904d5aac1ff | -9.31585 | -57.70287 | 2025-08-29 05:08:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6fbc0915-70cf-3ad2-93b9-9974b7d53ae4 | -9.16092 | -59.5586 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e3f931c-6b03-3c0f-9416-6b580de8ad49 | -10.46863 | -57.96789 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2442b382-3075-3b34-afde-c44a43a4f24a | -9.16174 | -59.57604 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d67957d1-e264-3449-bb51-99797a6f6e0d | -12.99548 | -56.92352 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2deb03d2-e58f-3b45-a8cb-331bdc7619ca | -9.54979 | -65.69242 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c192fc0-1ef6-3733-af5c-b6cca578b2a3 | -14.77254 | -59.74219 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aaaa4c39-55ec-3514-ad71-3e8751784c65 | -13.17163 | -50.59074 | 2025-08-29 05:08:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb8daa45-26af-3f05-8fad-aa1a21c09d57 | -9.32161 | -56.90369 | 2025-08-29 05:08:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42065936-276c-30c3-9134-278f41f60cbf | -10.37817 | -57.831 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 70c5a3e4-529e-3039-9ced-07933e7a407c | -15.21914 | -53.79604 | 2025-08-29 05:08:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 096afcca-ac63-355c-b669-80d55cb2f062 | -9.13329 | -65.79419 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33a8c99f-7dfb-3eff-b8c7-2570e01f918e | -13.50406 | -46.84464 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 37489154-18e1-34d2-91dc-cc6171346a5a | -9.46051 | -60.55978 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e3807bf2-c73e-3526-a67b-99f35f88445d | -12.09774 | -44.72765 | 2025-08-29 05:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7740718e-2d00-30ff-ab72-32ac4907f206 | -12.84699 | -48.09894 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 21245e7e-3903-3b6a-9e57-bbaf3f7ed23e | -11.26138 | -45.49419 | 2025-08-29 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bf491d4-e475-3b95-bf7d-e6bbb43c13b9 | -9.08662 | -65.73949 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3db4cfe8-a8a3-3c79-9d6f-89a119ba7492 | -12.22682 | -64.22894 | 2025-08-29 05:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a3364ee-66e6-326e-95e3-c4586e3c37e3 | -9.11341 | -65.77699 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 79e28aed-4f08-36e3-9e43-9b590287363c | -9.1149 | -65.77258 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 3f29c5f4-3bff-3c11-9bf2-403e59e6a1da | -11.93381 | -46.70179 | 2025-08-29 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ae6d873-f7bf-3210-b2d7-dc4ff72585e0 | -12.87413 | -48.14108 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d897de95-7548-3caa-8d93-ba9ad51b5b91 | -8.17789 | -61.37375 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fc434973-9d96-3078-994a-65facbf736aa | -10.98084 | -46.92178 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 48b43415-675d-3356-a5a7-e0a965da0343 | -9.60379 | -55.38142 | 2025-08-29 05:08:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ca6b874-7c2a-3195-9595-e6e0cd7ac578 | -9.16776 | -65.78989 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0727dabc-1269-3012-b8ca-6dbc7a556c4c | -9.54218 | -65.6917 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81ff49e1-50e3-32a2-a782-ae0d4149a0c3 | -11.95406 | -44.8435 | 2025-08-29 05:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e3a3422-b2f7-331f-b7c8-7f6e7c92b5f7 | -8.18482 | -61.38252 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e47382e6-4fad-3cea-8c06-a9fe8d298f5d | -12.08911 | -44.97817 | 2025-08-29 05:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 25c7a9d7-b335-3472-99d5-1848d2f99249 | -11.31565 | -55.2255 | 2025-08-29 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d7b24c2-330a-3f67-aaa6-0624d0dcac35 | -9.80344 | -67.84705 | 2025-08-29 05:08:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d23f93f5-c520-36a0-b223-661e44b14dca | -8.18009 | -61.38544 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0397cf71-def1-3e1b-8455-a9b28f70e0a0 | -12.91741 | -48.13826 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85621c87-4c67-3883-b959-c4a5b610555d | -12.83856 | -48.17307 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cb77b259-121e-3d32-aaf5-8cf72082b191 | -14.78554 | -59.72824 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73f4a059-7ee2-3b9e-a883-c02ecaa79a6d | -8.95074 | -65.95538 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9ebb942-a1d3-3ccc-af3c-3c7d0150d004 | -12.63223 | -60.24377 | 2025-08-29 05:08:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6880b14-706b-3b8f-9d25-3aa7ee4b3a37 | -9.46353 | -60.56525 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fff97102-1543-36a0-81e1-cba8efefb06b | -9.17421 | -60.78377 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e9d0df6-9624-362a-a1bd-2e194be6a647 | -13.37264 | -51.75801 | 2025-08-29 05:08:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 348df15b-7f51-3239-84b7-57c107137d7b | -9.22989 | -59.68268 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65e5530b-057a-3412-b233-40e1a894ccd3 | -13.57767 | -46.86499 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 399fd420-5bae-36c5-b1e7-bf401ca1947f | -13.41799 | -46.98111 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 22.0 |
| b0f4395f-aa1f-394b-a592-6c7c8ff1dd77 | -10.85089 | -47.49919 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a1018b8-c4f6-32ac-a1ea-84b22607dfec | -13.00602 | -56.9216 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d50c18ae-ba2a-3364-ac0b-a5690fbe64d1 | -13.54682 | -46.8778 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dfa7d031-4274-388a-9d59-6af10b4edb81 | -12.86884 | -48.14051 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db57af38-491b-30d5-afd1-82edd7e85e14 | -10.97991 | -46.91251 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a25535be-064a-391b-a440-fb3d463b98b8 | -10.35173 | -58.04289 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e02b91c-0aa0-38ec-b332-53cc3483d6df | -8.12271 | -61.21425 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 799fc3f0-7113-3256-ab92-1d4c04e2abe4 | -10.02514 | -48.07792 | 2025-08-29 05:08:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f101661-6d73-3f00-9fac-d6437edc4596 | -12.96006 | -44.57673 | 2025-08-29 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a97c026-9869-3538-80d9-11af29d8cdbb | -12.9966 | -56.91643 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9abe77c-13fb-35d9-ac82-76b7b5bb0375 | -15.66263 | -52.76805 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17215487-b8ec-356d-86d7-a23676b82959 | -13.55356 | -46.8702 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b121cac1-15fa-32d9-80e3-d582b831fc87 | -10.85496 | -60.81214 | 2025-08-29 05:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9b18d5e-4318-3284-8507-b55b319639cb | -9.17795 | -65.79545 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9d42355-4c92-30d5-8bc8-a6c59f978f9e | -9.80796 | -61.19897 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c5f3d57-d429-39a9-aa54-2d997a65d6dd | -14.31838 | -60.35513 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f68dda5-6675-38df-b089-fa672883b392 | -15.19172 | -52.33642 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9ede3b2-9766-3fee-ad39-2dcd2e015aff | -14.79227 | -59.70913 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0ca7d1d-e562-3958-ab14-f8a7690d0f22 | -9.10883 | -65.77501 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c8bf2cac-5236-3c5d-b299-0aee661cf660 | -8.90633 | -60.7571 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f80629a0-58e1-3cec-b153-fa69ae04a6d6 | -12.43161 | -63.91173 | 2025-08-29 05:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dc09139-25f0-39c6-bab0-dc4755c5bebc | -11.37361 | -63.25888 | 2025-08-29 05:08:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c188ca8f-9838-3c74-8ec5-8500c980ac52 | -9.93544 | -46.71017 | 2025-08-29 05:08:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ecb5d4d3-3b18-3e66-a475-f0685a1e5c50 | -9.12067 | -65.76781 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e90b9b09-a73a-3f50-84f8-00670be91c39 | -9.78672 | -64.25443 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 793ca1b0-9476-377a-a9d0-e54ca4ee13eb | -14.77322 | -59.73812 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48df035a-b660-3a0a-ae71-421c5ea383c0 | -12.45632 | -47.99645 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ccf753f7-70b8-3c26-9897-e121225aaadd | -8.95516 | -65.96014 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 154ddeed-6d01-3541-ae67-0dacac7f411d | -10.97766 | -46.90242 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 60a13702-51bc-378e-a3b3-7736702149d6 | -13.50458 | -46.84028 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b6000b20-8698-39f2-aadf-ee6b4c64b1e4 | -13.36795 | -51.76131 | 2025-08-29 05:08:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README69.md)
