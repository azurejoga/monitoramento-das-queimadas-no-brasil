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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3954ae2b-8ad7-3c08-aecd-250c9c2b49b1 | -10.58927 | -49.63728 | 2025-06-24 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d4285d8-e3d2-34b7-88fe-768b3ea0e2d9 | -10.583 | -49.64056 | 2025-06-24 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c0620c45-9dd0-3e21-bdba-0d5a2934c97c | -10.59384 | -49.45765 | 2025-06-24 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc27ce4a-4970-37a7-885d-456affbae1a1 | -8.56168 | -51.55261 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 8a8752cc-c67e-3d80-b136-c25b628cb75c | -8.57913 | -51.57237 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f8dfd0b0-956d-3844-9326-eb06cd8ac7fb | -10.50572 | -53.5905 | 2025-06-24 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 144f9955-bd6d-34b2-b2d3-f2499c03c702 | -10.8643 | -53.76227 | 2025-06-24 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4822da2-14ad-373d-aae0-b4d538a736fa | -10.14416 | -48.98912 | 2025-06-24 05:18:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c7e1f72-ec10-3491-9a34-7ef0ebacc48e | -13.06973 | -48.83106 | 2025-06-24 05:18:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30378f46-8b8d-3988-8ad5-0a6dda7dc6b0 | -10.07847 | -52.74068 | 2025-06-24 05:18:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0e21c923-180d-3f22-be17-b19da27fe3d1 | -8.33963 | -48.52576 | 2025-06-24 05:18:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f53caf20-fb25-3b43-836b-4a824a6bd989 | -8.56243 | -51.54695 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 059e8d80-6214-3158-bb3a-e86657a04b0f | -8.98729 | -49.86733 | 2025-06-24 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4ec055b-8636-3d37-8a1b-ddb2eb278dd1 | -10.58876 | -49.64136 | 2025-06-24 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c06aa20-c024-3297-b108-bc53f5acc5a6 | -11.80623 | -56.95942 | 2025-06-24 05:18:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91bade05-f5a0-3088-b6fa-be683a5a93cf | -8.56426 | -51.55684 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| b950f23d-8345-3c6e-a028-c39b1c92b3cd | -10.59916 | -49.46264 | 2025-06-24 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c16aa27e-6aff-3154-a9a6-d4f810a8cf05 | -8.31732 | -55.10903 | 2025-06-24 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4fbdfb3b-fd74-3e00-8790-87e54f486bdd | -8.58748 | -51.58496 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 414ca5ab-29a6-318d-bd2c-a932cc5305c9 | -8.57763 | -51.58368 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df8acbbc-50b0-39bc-add6-ae32b09e8c14 | -10.06518 | -49.66149 | 2025-06-24 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 553f26e0-8762-38c8-a25f-0203aa1eaa47 | -7.87318 | -47.87725 | 2025-06-24 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a78aed21-d7ec-3bfb-918c-3e55a382da01 | -10.87078 | -53.78046 | 2025-06-24 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe038c01-695d-39db-9c08-ae5f3298440f | -10.58825 | -49.64545 | 2025-06-24 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bbb2fa7-4212-303d-8796-738c93076414 | -8.56584 | -51.54554 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66579f5c-11db-380c-8ef1-cdff83f5c50b | -11.93855 | -48.42338 | 2025-06-24 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cda271f9-7944-3f2a-ade0-12ae3da33680 | -8.55676 | -51.55187 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| dff2a5ff-030f-30a0-b94d-a41475e4335c | -7.86697 | -47.87636 | 2025-06-24 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a8e10128-ca80-35bd-8138-11f0f00048dd | -10.86373 | -53.76652 | 2025-06-24 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9253eb5e-6bbb-36eb-a231-ad1f48f50a71 | -10.05947 | -49.66071 | 2025-06-24 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df576d72-ad38-3c68-8f48-7b14e170ecca | -8.99291 | -49.8735 | 2025-06-24 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3f90a44-a4c0-35f7-8362-597ff0d7ad74 | -8.57195 | -51.58869 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b417b15-f3cc-389f-b4bc-fc1dc9667337 | -12.80116 | -48.73373 | 2025-06-24 05:18:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8e4ac76-cd5a-3b6d-b09b-b1300eac190a | -9.64726 | -48.56369 | 2025-06-24 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26c2c8ce-454c-33a3-aac8-871359f4c06b | -10.28016 | -47.61199 | 2025-06-24 05:18:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8983a1dd-2faa-3b4f-aae0-27296a6a346f | -11.28255 | -52.46728 | 2025-06-24 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aceb834d-719f-3063-8ff2-15a79c037d65 | -10.86147 | -53.78349 | 2025-06-24 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a286a90e-36e4-36b1-8b98-adac3f107f75 | -10.86811 | -53.76711 | 2025-06-24 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2887cb6c-3456-3439-b9d9-a47f809a5a10 | -10.8626 | -53.77501 | 2025-06-24 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be2cce5d-c227-3899-b195-497ec89b307b | -7.86764 | -47.87136 | 2025-06-24 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab8eb8a2-0b6f-3f9f-9128-c6de62287707 | -10.05997 | -49.65675 | 2025-06-24 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 217050d2-4227-3949-b6b2-4eb39c53faaf | -11.94131 | -48.42923 | 2025-06-24 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83e2a64e-dd10-324c-b446-2813c6a810f8 | -8.56012 | -51.5505 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| fbf14b13-c7d9-3d65-90bc-be850df5dc07 | -10.08708 | -52.74688 | 2025-06-24 05:18:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1724a59f-0290-38b6-9820-0cd701b1ae47 | -8.70633 | -47.17878 | 2025-06-24 05:18:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24b74a67-9e91-32a3-a1e7-a228d48b7143 | -8.56661 | -51.55333 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b8e799d9-a93f-3978-ba92-4ea7e986cbc2 | -10.45977 | -46.9792 | 2025-06-24 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| addb52cf-f193-3cad-bc82-52a24bb98cc4 | -12.28803 | -48.80328 | 2025-06-24 05:18:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a6a7e545-91c2-3154-8df3-622aed53dcaf | -10.86316 | -53.77076 | 2025-06-24 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b4e321e-4e76-3344-a14c-422a7df27db5 | -10.08311 | -52.74136 | 2025-06-24 05:18:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a8e48429-2030-383c-84d3-b001f785d43f | -8.56929 | -51.57092 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16164623-2ca0-3419-aa25-adc5bdec479c | -11.27773 | -52.46666 | 2025-06-24 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 710cce3a-ba5d-350c-81dc-52f06a167055 | -9.40104 | -48.43526 | 2025-06-24 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c884851a-c369-30cd-912e-8f2f4571b8ec | -9.64667 | -48.56845 | 2025-06-24 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a89a0ae5-a0c2-3cc0-a73f-56c8f0bc5ea7 | -10.86096 | -54.29978 | 2025-06-24 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03cf7dfb-89ba-30f4-a381-f5ef20789851 | -10.86641 | -53.77985 | 2025-06-24 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 160a8a86-29ab-30a7-89d4-c0933297292a | -8.98683 | -49.87104 | 2025-06-24 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a16b9fb6-b170-323d-8f8e-a517a3f808de | -8.56512 | -51.56459 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 35dad59d-43a5-30af-99e3-fecc3ad9a52e | -10.50308 | -53.57694 | 2025-06-24 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57d3722a-2bb0-3c0e-84de-e83e2097910c | -10.59401 | -49.64622 | 2025-06-24 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa01b418-bd5b-343d-9e94-3e6b0091481e | -11.57421 | -47.4347 | 2025-06-24 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 45f1820d-ca90-34b0-a32d-f2adc422a896 | -7.91856 | -61.55781 | 2025-06-24 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ddc562b-6871-3f89-9cf1-fa89285927b4 | -8.98785 | -49.86904 | 2025-06-24 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 99f91c9d-8401-3947-8e83-4944a5f84ccd | -10.5825 | -49.64463 | 2025-06-24 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| db6c889b-2aba-3b12-a11f-ec3c5b1dfa3a | -8.57153 | -51.55404 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c7f1c856-97e0-37cd-a9e9-d9a7398b3b3b | -9.41504 | -48.42267 | 2025-06-24 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8589b332-7f3d-368a-8c56-dd39e72ea5b5 | -11.94193 | -48.42405 | 2025-06-24 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22b12dea-582e-3d09-8629-6523c3651133 | -8.56094 | -51.55824 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 971ccd82-e4ef-3900-ad07-ba152eb17497 | -9.40034 | -48.43897 | 2025-06-24 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9cf30de3-fb4a-37d6-a983-6cdd88d030db | -8.56505 | -51.55121 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| fb5743a3-78b8-3d6e-87b6-10a620a3e0c2 | -13.07546 | -48.83666 | 2025-06-24 05:18:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| ea737ba4-13ec-3bd4-a813-b3d966d0c8fe | -7.87189 | -47.87708 | 2025-06-24 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b4a7833c-3237-33a4-9056-ec951bb57e42 | -10.28666 | -47.613 | 2025-06-24 05:18:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55fa6d1d-4ad5-399e-acc3-5d31b288fa56 | -10.57698 | -49.15132 | 2025-06-24 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47f4a4f9-9c66-3779-9d4e-806c9cb6b7ae | -10.59864 | -49.46679 | 2025-06-24 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d409b9b6-e4fd-321f-b407-6042d87e1bc6 | -10.57749 | -49.14696 | 2025-06-24 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38a65f06-6774-3906-a223-09fa0e78104c | -10.86487 | -53.75799 | 2025-06-24 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73cbab27-4b9e-3676-91f2-623995c17577 | -11.93797 | -48.42857 | 2025-06-24 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38a31d19-91bd-33c6-b5ab-a0bcca0faf12 | -8.57346 | -51.57728 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7e24fc1b-7a9c-3d93-9271-f4f24ef65265 | -7.86568 | -47.87614 | 2025-06-24 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49f4508a-7cca-3c56-995c-da967d5fad56 | -7.91977 | -61.55025 | 2025-06-24 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7af6b75-9da9-3cad-add5-75766519c056 | -13.076 | -48.83177 | 2025-06-24 05:18:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0d23f64e-183e-37ae-8351-8440221a8540 | -10.85991 | -53.76169 | 2025-06-24 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c01e288-b4cc-3f7f-b38f-d6e4d3a880b0 | -8.56586 | -51.55898 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5131b949-6453-3661-8c88-1cb4ce6b3f63 | -10.08245 | -52.74623 | 2025-06-24 05:18:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| c4ddc5b8-1a28-3568-97c0-d6751eca3754 | -9.40047 | -48.43995 | 2025-06-24 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5eb15535-5635-3590-8268-bb1586c3efad | -9.41564 | -48.41783 | 2025-06-24 05:18:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5d4771b-10d5-3678-8a74-daec28d4ea04 | -12.28935 | -48.80324 | 2025-06-24 05:18:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 922881bf-befc-33b2-a90f-ebd39b64a158 | -8.55855 | -51.56173 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 0759ff98-046a-3596-8478-d99bcd199325 | -10.49927 | -53.57195 | 2025-06-24 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 894477c9-3f09-3dcc-a0b2-b891448c3235 | -8.58255 | -51.58435 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6f19ba99-e4d8-3e48-b3e7-2d8f63c335ff | -8.56347 | -51.56245 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 5e0d56f6-b720-3cd7-a5ac-4e5099dd9562 | -10.51506 | -47.58179 | 2025-06-24 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7802e2ea-8536-3073-8a0c-e89a5a3e6913 | -10.45903 | -46.98562 | 2025-06-24 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71686db8-138c-372a-be4c-a543a3b63bc6 | -10.05243 | -59.35795 | 2025-06-24 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b69cb48-539a-30c9-958a-46bda6ae182b | -8.55602 | -51.5575 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| a2b99eb7-e31c-3d4d-93ea-f096b60de7c8 | -8.55442 | -51.55538 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba5ab634-581f-3267-b52a-75afd4d3539f | -8.89468 | -47.47737 | 2025-06-24 05:18:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8362c27a-1c2b-3773-a982-8f07a6c9c7f8 | -8.55934 | -51.55611 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 22b0d658-77dc-3ca5-8b7c-ab65c56b7ec0 | -8.57421 | -51.57165 | 2025-06-24 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |


[Clique aqui para ver as próximas entradas](README17.md)
