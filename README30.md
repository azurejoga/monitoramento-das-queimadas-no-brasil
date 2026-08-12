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
| 1ea7dc40-d018-391d-ad70-0b9c645e8b6a | -9.47696 | -60.51373 | 2026-08-12 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 666c1c20-234b-31e3-b52d-f842dcfb337c | -11.9553 | -46.38249 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3dc1020e-07ce-3768-a7fb-e456e384be11 | -8.9577 | -60.55507 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1403ada3-3791-3381-83eb-d83f0dea34d1 | -9.71959 | -60.20575 | 2026-08-12 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e0decc0-7941-3962-b7c1-c6361694c2a2 | -11.88994 | -45.83411 | 2026-08-12 05:10:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c976e90-8007-37bc-b9b0-689394ddd67c | -8.95612 | -60.56426 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 090b1401-1500-35fd-ac61-e0490f612244 | -8.96103 | -60.51022 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c7e4e506-fcc9-368f-9c3b-88e90c8999d7 | -11.97741 | -46.39884 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 230f8375-53fa-384f-9c9c-016a339980f5 | -8.95794 | -60.5523 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1909603e-55d9-3906-b8d2-38b26c869fde | -11.98585 | -46.37906 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1ab59e6f-bd20-3a93-9549-9b9adc7dac8a | -11.82482 | -51.84837 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8e47adf-3283-3388-a01e-95198edb9eb6 | -11.94757 | -46.34639 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 796d494b-0402-3538-b164-b619cd3388f8 | -11.98136 | -46.39507 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c51effe0-ec4a-3730-ae40-57c5b340b06d | -11.98372 | -46.37466 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 732a03ef-07b4-3d5e-ada5-d97df8eec732 | -9.13083 | -46.38968 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 546ef63f-cb08-3a8b-8c9c-36a62f3ba91a | -8.78326 | -45.79299 | 2026-08-12 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9e324ab-7446-3057-bc67-03b39a6e2a05 | -7.39784 | -59.99165 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b994dcd4-c06f-3ca5-a0b2-9056befe787f | -11.46569 | -44.55337 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4b74f909-fada-38d3-b866-8eb5931164bb | -9.34157 | -47.50692 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5f9eaf3-e9c1-3626-96ae-50a2423698f8 | -9.34112 | -47.5103 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d50bc39-91ac-396b-b682-8ebf517bdef4 | -8.96007 | -60.5413 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e351b5a1-f7f9-3a6f-b99b-8f44334837f0 | -11.49587 | -54.60924 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8ff5dd6-9ce3-312e-8eb1-a7a6ce7e535c | -8.62183 | -47.45654 | 2026-08-12 05:10:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b28c5c23-9256-3d28-a69f-ca9f81ee1105 | -10.10074 | -46.2125 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 291d15b2-692f-3ca2-9334-4ccc92560a29 | -8.95235 | -60.56361 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0ebb9605-b3c0-3392-ba80-1837c469482b | -8.59871 | -45.41359 | 2026-08-12 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5062f70-4d04-36cb-a543-b31820ab8ef5 | -11.9502 | -46.32448 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| df595089-5fa8-394b-80fe-8248fa6b8913 | -11.98131 | -46.36687 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1165ca2e-4567-3500-98b2-bbb077770f0a | -8.95879 | -60.50042 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3c6f9b2-c05d-3ee5-aa6d-e88a533d0f46 | -9.1385 | -46.39054 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1fe7a302-c7a8-350b-b643-7a55186f4e87 | -8.95631 | -60.54066 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 882d89ad-3c29-349a-915a-08193b844995 | -6.58721 | -59.01275 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fba270b2-a1fc-319c-95bc-ff34ee05ea5e | -11.98631 | -46.37528 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8517b242-e04e-358a-b500-5f7299ae0d4e | -8.95052 | -60.50369 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38d8f2bc-bbab-3436-9687-d51305ce7dd6 | -11.80466 | -51.81978 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acb8167d-8df6-305a-97fe-d2bf65ab4aac | -6.60351 | -59.00277 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0818cf35-fad5-342d-b409-b96d5e2e1675 | -9.36554 | -47.44882 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7dbf05b-2487-33e1-8a50-00fa5b1e4e1f | -8.5489 | -54.58946 | 2026-08-12 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14a7f99b-79f8-39b2-9e3a-74b74db95cac | -8.9437 | -60.52144 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6e50dd4-03d7-36a3-9c79-19f74d5dbcea | -7.01046 | -44.62431 | 2026-08-12 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f389c08c-e698-32f5-a850-5b149c4a48a5 | -11.80654 | -51.56326 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 60a4504f-458b-3004-9677-762458cae252 | -10.90469 | -50.28652 | 2026-08-12 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5b36bca-8bd6-3dd4-bd89-a31f4b9f5a87 | -8.77951 | -45.78955 | 2026-08-12 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de7cb3e4-a9c5-3c64-89bf-fcf8c33fcde0 | -4.07413 | -54.70406 | 2026-08-12 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c78627df-4da6-36e7-bedb-18e1e59a67bd | -7.41227 | -60.00484 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 937fc31f-f7a0-386e-b021-0bcb710766b9 | -11.82044 | -51.85637 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4235302f-e7a2-340f-98dc-c1ef48670d50 | -8.78375 | -45.78912 | 2026-08-12 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85368b35-9dd8-312c-abed-5aa172f63cd1 | -10.09383 | -46.21987 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc02be2a-904f-3d49-a7ea-72954ba6c3b0 | -11.92826 | -47.37852 | 2026-08-12 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f922f4f-c536-32a7-8964-f2bbec12c1da | -7.45482 | -46.14485 | 2026-08-12 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22dd3e53-1edb-36ec-9e1e-cf18c0409145 | -6.53418 | -43.1216 | 2026-08-12 05:10:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1403f3f-ae8a-3fbd-bef0-d6b7ffce8c86 | -7.72117 | -46.2225 | 2026-08-12 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91c7d1aa-2c29-3a36-9494-ceaa341af646 | -15.29956 | -48.88108 | 2026-08-12 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06388ae1-7509-36e8-b029-12827877764b | -14.51347 | -49.28588 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7a27eb5-8ba0-3eb9-ae06-233723dc0493 | -14.52873 | -52.7854 | 2026-08-12 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47bf9266-71f9-3c92-9ad3-b1a908db8fca | -13.89123 | -53.82922 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 42f9c7af-9e2f-34fa-9188-4c050de70d6a | -15.30477 | -48.88222 | 2026-08-12 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 10b023c9-3a68-3b04-a39b-cbe190ce70fb | -13.839 | -53.79342 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e4aa842-d3bf-3b54-9142-7f1026effa97 | -14.48366 | -51.86115 | 2026-08-12 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 325be066-4019-3129-a4a4-593d64e97d08 | -11.99772 | -53.46131 | 2026-08-12 05:12:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4944ac7b-81a2-38e1-adee-133721013b6e | -13.30158 | -49.70442 | 2026-08-12 05:12:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7b4b43ee-77d0-3f11-b017-b8d1ce4d181e | -14.52182 | -49.30148 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 189ba29b-3639-3f78-9026-728ba86d4dbf | -13.57116 | -46.25769 | 2026-08-12 05:12:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6e4394b-2035-301a-9376-e6e825c4c822 | -14.03578 | -53.60153 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b5500b5e-dc94-3be9-a752-290ac5650f2c | -13.89499 | -53.82966 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 422cc966-3bda-3e83-9323-bd545dd4570e | -13.57064 | -46.26218 | 2026-08-12 05:12:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f96ce6ab-0dc6-3612-a899-8c19f7b927c5 | -14.50423 | -49.27732 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa1f20e5-c60e-34b6-9afc-90719878f67c | -13.60455 | -46.24203 | 2026-08-12 05:12:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fea437e-9492-3701-9143-352cda0ff467 | -14.32917 | -54.0431 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2702a73b-8e8b-3581-afe4-fc886e28b9d6 | -15.29549 | -48.87042 | 2026-08-12 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c41d382-ed58-3f02-a0b5-dfacf9122d52 | -13.53758 | -46.28117 | 2026-08-12 05:12:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32959b33-3f62-329d-acf8-149f2f0e8427 | -13.604 | -46.24139 | 2026-08-12 05:12:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd48b58b-fa7d-3b09-adb7-ddebe2ade1e1 | -13.8576 | -53.82406 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4abdf29-cf30-33c7-929c-b184975afbb8 | -15.29473 | -48.87677 | 2026-08-12 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 732fca71-c40c-3c6c-8510-d1e15e0f1c6e | -14.4794 | -51.86053 | 2026-08-12 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba511857-f998-3d36-bba0-48b9969050c7 | -14.44689 | -52.2597 | 2026-08-12 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f89c8c4a-f6a9-3c62-b23d-ca023393af5b | -13.83702 | -53.80757 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03c2695d-5f5f-3163-ad91-2420c7c4ffa5 | -14.03647 | -53.59668 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b26f9bf7-a7bc-3563-a53d-90b09aa909ea | -13.83834 | -53.79813 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d41c577b-5846-392b-84bc-02cedaa94148 | -13.89645 | -53.79279 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cd8daafe-40be-3e78-a4f5-5b8795efa3e7 | -16.34007 | -49.46523 | 2026-08-12 05:12:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c95d500b-2a27-3b37-9531-9568e2fe9a9d | -13.30258 | -49.70874 | 2026-08-12 05:12:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 658aefc9-4cb9-322e-ac1a-b4514bd9c16b | -14.33134 | -54.04055 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9752ef1b-fe66-3ac9-9516-98a4cfebb52f | -13.53861 | -46.27203 | 2026-08-12 05:12:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00e69e40-a23f-347c-9292-f4f2df5fac02 | -14.5178 | -49.29245 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9330a26-3393-3cec-9a20-28ab90d5d8e0 | -16.15914 | -46.81327 | 2026-08-12 05:12:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf84fc4e-694c-3488-8a43-2284514106e2 | -13.30226 | -49.69894 | 2026-08-12 05:12:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| adac60b8-85ad-3d29-8299-30d8b1a3085b | -14.33662 | -54.04406 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e638d506-52ee-3d09-bd2d-16c6ac9ad1d4 | -13.28945 | -49.69596 | 2026-08-12 05:12:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc54f6cb-f8b0-3dc9-90c9-85ac1a7832bc | -13.89434 | -53.83413 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8c85c66f-9984-37c4-8721-f4c5ced5622a | -14.50802 | -49.2883 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b9b8bf1-e0c8-31b8-ad6f-e93c0392279f | -13.59841 | -46.2415 | 2026-08-12 05:12:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81802b7f-e7da-3de8-be04-ebc1cbb78ad5 | -15.30029 | -48.87504 | 2026-08-12 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 09a8ac07-14d2-37f9-961e-916626ea5c9b | -13.29773 | -49.70811 | 2026-08-12 05:12:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f322d738-6d9d-35db-9dfc-e93fb9b753fe | -12.14202 | -57.20045 | 2026-08-12 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 516796dd-b505-3a0d-abb1-34048dbdfb60 | -14.28044 | -45.27716 | 2026-08-12 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 158da4b0-75a2-3821-9d43-87d1d123d9fa | -13.88748 | -53.82876 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 296837a0-925d-3ceb-a8b3-2ed70bdf6f77 | -13.42593 | -57.04673 | 2026-08-12 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbc2c1ff-3ac8-35ef-b1de-91b3243a018f | -13.89954 | -53.79789 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5df4c708-726f-3cb9-9d15-8ee233c8cca3 | -15.30066 | -48.87194 | 2026-08-12 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |


[Clique aqui para ver as próximas entradas](README31.md)
