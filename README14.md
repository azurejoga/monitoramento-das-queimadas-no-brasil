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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7082e0df-53aa-3d43-b7b2-6bc208789f2c | -8.33044 | -47.12237 | 2026-06-26 04:51:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff6689de-977a-304e-86b0-15cd458ed740 | -11.77673 | -46.44722 | 2026-06-26 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f921e221-376f-3f71-9706-d8c473951f36 | -11.47699 | -47.34317 | 2026-06-26 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4444c202-8f4c-3c42-bbac-06e6338e0a38 | -9.88968 | -57.40092 | 2026-06-26 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe9aacbe-bf8d-3097-a146-5f8e2cee54db | -10.63222 | -47.03853 | 2026-06-26 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f15b660-2e13-3246-b7f2-07bdf8bc98ab | -8.44097 | -51.5574 | 2026-06-26 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f02e5db-a3bd-38e2-9a1d-c4ad228f78cd | -7.74783 | -44.62224 | 2026-06-26 04:51:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8421a87d-47ec-3ecd-a8f7-44d836de6524 | -7.62841 | -47.29643 | 2026-06-26 04:51:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d45f58de-465f-3f18-9547-40d8b6ae1d11 | -9.70183 | -47.69934 | 2026-06-26 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 501f2307-2a97-3a84-8715-42002d27d719 | -10.12759 | -52.10655 | 2026-06-26 04:51:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16d10c3a-f74f-3b50-ad97-be9b986f0f77 | -9.89157 | -57.40199 | 2026-06-26 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e728450-5a85-3c05-b268-bd0d40e4abcc | -8.01119 | -49.64524 | 2026-06-26 04:51:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c5f9262-d704-3028-9eb5-4a5124a3b499 | -10.1126 | -47.56172 | 2026-06-26 04:51:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 72675140-dc32-39bc-b0a6-64f7802a051b | -9.49995 | -57.31413 | 2026-06-26 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24fbd6de-161c-31a7-8d96-721d2aafcef4 | -6.98655 | -42.89409 | 2026-06-26 04:51:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| db25d9d8-6f8c-3369-9d9b-11f0a10d4760 | -12.07957 | -54.60201 | 2026-06-26 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b49b2be-bf7d-340c-9bbd-030357a9c2c9 | -12.74569 | -44.49096 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 62b3225c-7aa4-315c-b084-67e11fa33623 | -9.70301 | -47.69807 | 2026-06-26 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07fa9930-8b1d-311d-8856-31ec93164831 | -6.30256 | -44.64627 | 2026-06-26 04:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b5c8af6-fe39-3cd3-8731-ea46ccd755a5 | -8.50432 | -50.15055 | 2026-06-26 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4dca276-e52b-3594-85d7-7d443fca41a4 | -8.22664 | -47.12035 | 2026-06-26 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aa182d2a-968a-37be-ac31-9d614fb365af | -8.33431 | -47.12295 | 2026-06-26 04:51:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e38f111-d568-3fc2-95d6-12c61c5f68c3 | -7.93374 | -47.81412 | 2026-06-26 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85bad9f9-1297-3a26-82f8-1d3893257fe3 | -11.87211 | -51.72643 | 2026-06-26 04:51:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 984fee1c-b4ec-3faa-9a8f-ce7dbd016f3b | -9.40092 | -50.67502 | 2026-06-26 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64dceaf2-f0a1-3df9-8488-4094365100a0 | -11.51675 | -56.12681 | 2026-06-26 04:51:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9a956695-bb98-3420-a88d-6e9bae58d339 | -12.03753 | -49.20155 | 2026-06-26 04:51:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf461e5c-9915-3dba-a19d-8b9bc2546ba1 | -12.75795 | -44.48674 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| af6dbf5b-06f9-3b01-9d09-39e198657eb9 | -12.74317 | -44.48473 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19f33c12-c55c-3443-8141-b389fdb498c1 | -6.50184 | -42.22237 | 2026-06-26 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a7011139-8567-3f83-9f4e-d978fe796dea | -11.77618 | -46.45119 | 2026-06-26 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f82589a-5a30-3b83-9c3e-d45777cba03c | -7.63523 | -50.21882 | 2026-06-26 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74f3a2e1-a218-3102-9ed5-533d366269f5 | -12.8724 | -44.34683 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d61101f7-9886-37cd-85c4-79a4cdadc232 | -11.21388 | -54.33747 | 2026-06-26 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43a077db-ba27-3801-a2c2-7fb084600bd4 | -6.93627 | -43.66918 | 2026-06-26 04:51:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28ac9115-bad9-3737-a7f2-a61cd08162fe | -11.48048 | -47.34722 | 2026-06-26 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0a24211-584e-3151-a1c2-b475a69b1643 | -12.75302 | -44.48608 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2e641a90-1cbf-3e76-8c8e-b41f3d6a7913 | -12.51549 | -48.27518 | 2026-06-26 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10ad4b88-7482-3862-939b-e81fdf7e94dc | -12.75232 | -44.49168 | 2026-06-26 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e8150e2e-0a6b-35d2-bc46-9b5a7cf5759b | -9.69921 | -47.69746 | 2026-06-26 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b372804-ce36-3074-ba1c-1f8f6b5b42f7 | -11.20116 | -43.35158 | 2026-06-26 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bb446585-be0c-3ff4-b9a8-9c0bf9f1293a | -11.20981 | -54.3407 | 2026-06-26 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6f3ebb1-7f25-3308-bad8-2e83fa45ab40 | -8.63154 | -47.17425 | 2026-06-26 04:51:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 084903bc-7fb3-348c-92d5-a0c8ff97c1f7 | -6.50095 | -42.22858 | 2026-06-26 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e1a55e9c-630e-3e76-b030-1be49d98ddce | -10.39359 | -56.76707 | 2026-06-26 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2350a799-0ec3-3c0c-b00c-388b93128512 | -9.89034 | -57.39719 | 2026-06-26 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13a18b13-5053-3410-bf63-768c61ffee76 | -11.5764 | -54.71012 | 2026-06-26 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 03b8570d-56f9-3675-93d5-cd93ec2c54c1 | -9.48558 | -57.32314 | 2026-06-26 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2549d79f-6bf6-31c9-b14e-e077607ba572 | -8.68469 | -47.86234 | 2026-06-26 04:51:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8cac21af-322f-3a64-aa4f-e62fba746d64 | -6.97602 | -42.89568 | 2026-06-26 04:51:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b4c30d8b-b712-34e9-a999-f39cae1d891a | -11.4775 | -47.33963 | 2026-06-26 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db624181-a2d0-3908-a0d4-24d745e2987d | -9.48145 | -57.32242 | 2026-06-26 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8b40ec8-a44a-3356-8763-61011fb4a72e | -10.09793 | -49.59054 | 2026-06-26 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1c975f0-ce5b-3850-9fce-cffa6159f2f8 | -6.50713 | -42.22289 | 2026-06-26 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 60fcd4da-0895-30c3-84b1-91c8eac77e99 | -12.50609 | -48.25904 | 2026-06-26 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fa9b036-58cc-3ec3-87b3-6ff041345a34 | -9.95944 | -51.1007 | 2026-06-26 04:51:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01c5a710-1dab-3e5e-adc5-0e5d9883a9be | -10.80611 | -55.86059 | 2026-06-26 04:51:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87adee12-c5cb-34b1-84f2-8da9de6ab43c | -8.2344 | -47.12139 | 2026-06-26 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c4b2378-2bdc-3e47-a0fa-38a80c3e1363 | -7.93811 | -47.81026 | 2026-06-26 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 594bcbd9-4f17-3b55-89af-8949cdfffa01 | -6.50129 | -42.22655 | 2026-06-26 04:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 74bbf30a-bb3c-3ca1-ad2d-a5bed3710abf | -5.72733 | -49.10073 | 2026-06-26 04:51:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb685b1f-3930-37de-96a0-70cfc7335d7d | -7.6517 | -50.02354 | 2026-06-26 04:51:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0987fab5-4971-329b-9e46-e497179c83ed | -8.50769 | -50.15107 | 2026-06-26 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50545a75-043f-3c95-95f4-e0d9d2eaef66 | -10.80772 | -55.86296 | 2026-06-26 04:51:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1dbd4d0c-fd96-3087-b240-aca9511696a8 | -9.42439 | -50.72251 | 2026-06-26 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c40661a-ddd3-38d1-9109-a32705953e98 | -10.77829 | -54.10546 | 2026-06-26 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e09bfa8e-ba91-38b9-9947-2cd67929ad56 | -11.63851 | -52.86003 | 2026-06-26 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a911ec8a-7bd0-3f52-b839-b63c21328ee9 | -7.63243 | -50.21474 | 2026-06-26 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7061e5d9-7759-319b-8e3b-9292bf7586d4 | -9.09709 | -47.52897 | 2026-06-26 04:51:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7e7bf79-34ab-3bed-ae5a-d65917625fc8 | -10.80238 | -48.56024 | 2026-06-26 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f3f3796-70ac-34ae-8e2c-8c38901f6fc7 | -12.62724 | -57.89079 | 2026-06-26 04:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5821e364-5789-3799-b4a7-83992345215f | -12.62659 | -57.89454 | 2026-06-26 04:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 012516f0-b53c-3016-b3db-5940f4b4aca9 | -15.59977 | -48.35173 | 2026-06-26 04:53:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e347083a-9b8d-3cf9-ba10-3e68a676355f | -13.73053 | -54.04526 | 2026-06-26 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfb322e1-94aa-305f-acdf-f659891bff47 | -13.87209 | -47.12668 | 2026-06-26 04:53:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 33e69f75-be0e-3562-b97a-0304dec76431 | -13.90574 | -47.32806 | 2026-06-26 04:53:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c787823-94e5-3d82-bb9e-ec8729c2ffcc | -13.07565 | -57.76605 | 2026-06-26 04:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ace018a7-2353-320b-b4d6-00532e0c46e1 | -13.72838 | -54.03743 | 2026-06-26 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb93dc30-9978-38a8-bc1a-eaf613fac79d | -14.6296 | -54.46135 | 2026-06-26 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be4b4aaf-a8c4-3084-ac74-6b4ac5c30488 | -15.16454 | -49.82419 | 2026-06-26 04:53:00 | NOAA-20 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a35c4de-36e0-32cd-a0de-b6bb5a7c13bb | -16.11719 | -49.21912 | 2026-06-26 04:53:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82220d4d-c45b-38b2-9281-94aaf83f05a8 | -12.76932 | -59.00733 | 2026-06-26 04:53:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f587b899-cac2-300b-8be6-31d766d52a76 | -14.21193 | -45.62512 | 2026-06-26 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b1dc850-9341-397d-8ae3-d888388735f8 | -12.62318 | -57.88998 | 2026-06-26 04:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 68b80bad-2c47-371d-81ea-34dc94c8c096 | -14.84056 | -48.12766 | 2026-06-26 04:53:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 578649cf-7609-3290-957f-238e7746c369 | -12.54527 | -57.2034 | 2026-06-26 04:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4bd2f2c6-1531-33e3-8d6f-e0416977cf15 | -13.72718 | -54.04469 | 2026-06-26 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36d53dbb-b0a1-3016-99bc-a86ac11d5df5 | -14.6302 | -54.45763 | 2026-06-26 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 693532e3-c721-3fef-99e0-285d49862c47 | -13.84407 | -47.14473 | 2026-06-26 04:53:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b68b2044-9b47-325b-98a3-3978fe7f78da | -13.26698 | -54.42611 | 2026-06-26 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 62c4aca6-134d-3352-89c1-b815d908c3b3 | -13.2568 | -54.42435 | 2026-06-26 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2225bc27-b99e-3601-bdb9-cb2630f1181f | -13.73664 | -54.05006 | 2026-06-26 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9aa7e9f0-5843-3a49-8af4-7b4b909b08ad | -13.92014 | -47.34604 | 2026-06-26 04:53:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e1f59cb-7baa-3962-bad7-08230a4b85ac | -14.87933 | -54.54926 | 2026-06-26 04:53:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5823eb68-7e2d-3c4d-9adf-8887c980bef9 | -13.26976 | -54.43044 | 2026-06-26 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b06acb27-6509-302d-b5ad-c84c86e35572 | -13.92473 | -47.34321 | 2026-06-26 04:53:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03370287-2518-3b1f-bcd4-c98fb3e56d54 | -13.73723 | -54.04641 | 2026-06-26 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f5e8f716-0e75-37a4-93e5-258583a6b950 | -13.92983 | -47.33665 | 2026-06-26 04:53:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b71d8437-1057-3cb5-9cc5-5ab271157ede | -11.90994 | -57.1058 | 2026-06-26 04:53:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 481f9a8e-c561-3d74-8b12-78f882411e7c | -13.72993 | -54.0489 | 2026-06-26 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README15.md)
