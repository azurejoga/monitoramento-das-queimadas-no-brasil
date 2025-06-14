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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7ae6ec4-43eb-300b-9504-bd3e69620f63 | -21.083099 | -54.627201 | 2025-06-14 00:51:00 | METOP-B | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| eedaefa9-2e53-3736-a713-e56a874bbdb2 | -10.5568 | -54.824699 | 2025-06-14 00:51:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7f7d782-3ac2-3bc8-839b-b4064d9ef4d0 | -8.5584 | -49.909199 | 2025-06-14 00:51:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e282ec23-ba29-3324-afd4-2744be0ce64e | -13.6685 | -55.178799 | 2025-06-14 00:51:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 13738863-7ed6-3268-8712-e1722a143272 | -9.1002 | -57.887299 | 2025-06-14 00:51:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8581c138-405a-37d6-8558-62a58a88428b | -10.5559 | -56.8367 | 2025-06-14 00:51:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 202b81c1-d25d-392b-a1ac-f91dc6d478f4 | -13.8492 | -57.462502 | 2025-06-14 00:51:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f021866a-4a1c-3c16-be7f-f2dd05f7d2b8 | -10.6475 | -55.131802 | 2025-06-14 00:51:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac865d1a-5c67-30c6-b51c-81d6dc4c3b19 | -10.5569 | -56.8876 | 2025-06-14 00:51:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26ed785b-91bd-3c5e-9e53-c9a4e803d40e | -10.5019 | -54.359501 | 2025-06-14 00:51:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27cc2c4e-f83d-3c2e-be7a-122d6bbac309 | -9.0192 | -57.567101 | 2025-06-14 00:51:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8f04907-fcea-3f94-bd02-d4905874ab36 | -10.5602 | -54.839401 | 2025-06-14 00:51:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cff16460-3385-31a3-8370-bdeda1be415a | -13.8476 | -57.455101 | 2025-06-14 00:51:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3614a775-b6d0-3e6a-a092-659244974ad9 | -13.8558 | -57.445499 | 2025-06-14 00:51:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d1fce48e-410d-35c1-a102-0f7c9f111cf8 | -13.5352 | -54.677898 | 2025-06-14 00:51:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 473fbc37-5443-3ba3-8f68-df0202e891dd | -18.3762 | -54.245499 | 2025-06-14 00:51:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b3a4dda8-1a3e-3c51-871d-fa65add3ca69 | -10.578 | -56.890099 | 2025-06-14 00:51:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7650bf69-a03f-3ef4-aea9-7ef44cb5e67f | -13.8378 | -57.457298 | 2025-06-14 00:51:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ba27f70d-5fbc-33fa-8ba0-93754e845faa | -21.081499 | -54.6199 | 2025-06-14 00:51:00 | METOP-B | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9d3b9543-839b-3594-b267-a11e6e39f4ee | -9.9325 | -60.601299 | 2025-06-14 00:51:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02b234f7-d24d-3517-8d1c-a899a90e7e8f | -10.6491 | -55.139 | 2025-06-14 00:51:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51bd2f1e-98fc-3d10-b306-919d21fbb298 | -12.2458 | -57.934299 | 2025-06-14 00:51:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08c3291c-bf4d-385f-85b3-d37a6c5b1b69 | -10.5134 | -54.364899 | 2025-06-14 00:51:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8fdad5f7-dd7a-3f8d-84d4-47f5e8ee54bf | -9.0222 | -57.581001 | 2025-06-14 00:51:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e10c8575-744e-3785-a491-dd9f865a5594 | -15.8353 | -46.5494 | 2025-06-14 00:51:00 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1dbe7386-5e89-38e9-8ced-f4cdd422f81d | -10.5584 | -56.894501 | 2025-06-14 00:51:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5b5e0af-8c82-32ae-b08e-d67ad64102c6 | -11.5586 | -57.513199 | 2025-06-14 00:51:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80692d8b-fd2b-33ec-a8f8-a44b752f8bb8 | -9.029 | -57.564899 | 2025-06-14 00:51:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 413bff5a-5e0e-3a35-8d3f-97b743a40bc9 | -11.4422 | -57.404202 | 2025-06-14 00:51:00 | METOP-B | NOVO HORIZONTE DO NORTE | MATO GROSSO | Brasil | 5106273 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2df82478-adb3-3839-85a3-6c1a9fc84109 | -18.3778 | -54.252701 | 2025-06-14 00:51:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 200311cf-dadb-38eb-91a5-e03f16bef6db | -10.4854 | -53.841 | 2025-06-14 00:51:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff25b613-b509-3b27-938a-9260a2cc36cc | -9.9286 | -60.583 | 2025-06-14 00:51:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1148bf0-d453-374b-98da-53b6e487015a | -11.7422 | -48.934799 | 2025-06-14 00:51:00 | METOP-B | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b66c6d2-9217-3660-90be-09e9c05dd1c3 | -12.267 | -57.937401 | 2025-06-14 00:51:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad0cfb4d-3d40-3c07-936d-fb4b8b315759 | -14.3229 | -53.426899 | 2025-06-14 00:51:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2eec35db-07ff-313d-bcda-4a939724d196 | -10.5554 | -56.8806 | 2025-06-14 00:51:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e784f81f-3960-3343-8c31-24a13f321ee3 | -10.5652 | -56.878399 | 2025-06-14 00:51:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 206fa93e-4c9e-3f8a-ac90-0d4597e99ceb | -12.2073 | -57.8032 | 2025-06-14 00:51:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d4cf8f2e-ecf4-3805-b1c5-823fda04e7ab | -15.6314 | -49.8909 | 2025-06-14 00:51:00 | METOP-B | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8e7c14d3-a003-3a09-9fed-09ca828d535e | -15.6286 | -49.8797 | 2025-06-14 00:51:00 | METOP-B | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 88364b6e-ad97-3778-ab05-4b166f05fc5a | -10.7738 | -53.971901 | 2025-06-14 00:51:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b702269e-3001-3f3b-956a-2465265bcf56 | -9.7244 | -52.792099 | 2025-06-14 00:51:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0763aeee-71cb-3ceb-8088-870f472abe4c | -13.8574 | -57.4529 | 2025-06-14 00:51:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e547816f-742c-33e4-9a82-f0aff62f50cf | -11.8007 | -56.599899 | 2025-06-14 00:51:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86fa2d80-0451-3116-8e74-94ce4b8688bb | -10.5796 | -56.897099 | 2025-06-14 00:51:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f48ebf23-0f21-34b4-b402-b6bcc6cc002e | -14.3087 | -53.4547 | 2025-06-14 00:51:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 426e1378-6bcb-3759-98c5-7592fc7965fc | -12.2088 | -57.8106 | 2025-06-14 00:51:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e070ece-fda0-33a2-85f9-2db073bee9fc | -11.9176 | -57.320599 | 2025-06-14 00:51:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cadfa631-a26c-3f4c-987b-17fd42913a5b | -12.2654 | -57.93 | 2025-06-14 00:51:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d6d13e1-0468-3a22-a268-dfc45719d9a6 | -8.5619 | -49.923401 | 2025-06-14 00:51:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4b164a7-1f93-3085-85a8-d8d0c39cb6de | -12.8611 | -49.901798 | 2025-06-14 00:51:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e0ef259-bc48-3b73-ac47-3369558c19ed | -9.037 | -48.467602 | 2025-06-14 00:51:00 | METOP-B | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b8e8dce-b476-3684-a96f-f2e4e00da047 | -10.5667 | -56.885399 | 2025-06-14 00:51:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93d532b7-652f-3ced-af20-03bff4e3aeb0 | -13.7112 | -53.4604 | 2025-06-14 00:51:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e8df2a1b-ed0d-3fa6-8d02-09e3cebed3cb | -10.5765 | -56.883202 | 2025-06-14 00:51:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d34f4c5-04e7-3d42-b51c-c121f0225162 | -9.032 | -57.5788 | 2025-06-14 00:51:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80e8c0bf-e64e-38a3-9d48-355f435a7f97 | -10.0058 | -57.2813 | 2025-06-14 00:51:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 791cc0b5-6434-3f2a-82d1-ec8e3175ff90 | -9.7265 | -52.801201 | 2025-06-14 00:51:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4498b36-5c69-3f13-832b-a9a042df2b42 | -10.6393 | -55.1413 | 2025-06-14 00:51:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d45c1c9-0e3e-3599-a66e-6d758a303bcf | -13.5418 | -54.661201 | 2025-06-14 00:51:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4db07e4d-ea16-3477-bfeb-b3c3ff11259e | -11.5157 | -54.732201 | 2025-06-14 00:51:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 992ed2b7-2c60-32ff-92fa-8416df41a974 | -15.8256 | -46.512798 | 2025-06-14 00:51:00 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 13c85a79-2ca8-31ba-9b98-2ec05062685f | -21.4315 | -54.5711 | 2025-06-14 01:00:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 60.9 |
| d851eaf4-961a-3dc3-8919-a442bc75c64b | -16.1967 | -46.4589 | 2025-06-14 01:00:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 45.2 |
| ac528fc5-fe31-32b0-b217-09630b57fdcb | -21.452 | -54.5675 | 2025-06-14 01:00:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 31d65fb3-2faf-306d-90d0-eb3bba4e286f | -6.9602 | -42.9052 | 2025-06-14 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 8aff9dda-b219-31cc-8efc-11df292ff100 | -7.2214 | -43.1153 | 2025-06-14 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| b24c6c93-85b4-3169-80aa-0cd249175c8d | -13.9059 | -54.6291 | 2025-06-14 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 45.1 |
| bcd2953b-8f79-35eb-97d1-4ce2bca521e4 | -11.8158 | -57.3413 | 2025-06-14 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 1c53f192-7c61-36f7-83eb-3b3f8bb0f522 | -6.9416 | -42.8834 | 2025-06-14 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 822b7e20-a8a1-3d43-b984-22885a445fc7 | -13.9062 | -54.6084 | 2025-06-14 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 6092dbf3-b446-3b89-b16c-4b7d37e41ec7 | -10.9205 | -54.7795 | 2025-06-14 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| b182f26b-4f33-30d3-8699-56f298327d3b | -10.9353 | -56.8522 | 2025-06-14 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| c80737be-272b-355f-9db7-289c5dbb8124 | -14.2121 | -57.4098 | 2025-06-14 01:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8342a701-f6ac-348d-92d4-93acbeb9ba1f | -11.0113 | -55.0764 | 2025-06-14 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| cb0f4f61-e729-3974-b84e-12dbd396f27f | -10.9355 | -56.8322 | 2025-06-14 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 04a1dc6d-0017-305d-b03b-69c159a24951 | -6.9605 | -42.8816 | 2025-06-14 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 9a44637d-bc79-3ad4-9ac3-2e8643204690 | -10.9167 | -56.8336 | 2025-06-14 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 78dadebf-4518-3579-aa00-32fc7f44e972 | -13.887 | -54.6106 | 2025-06-14 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| b3c3cdc3-5ade-3c19-92e8-b637c74149ea | -11.011 | -55.0967 | 2025-06-14 01:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 2ef69315-10d7-36b9-873d-ddf2feacd257 | -11.7969 | -57.3428 | 2025-06-14 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| aeac1e31-5a25-343a-91c3-52f260ba500e | -10.9355 | -56.8322 | 2025-06-14 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 3fb61002-1bcb-3234-ad64-2daec3b93a96 | -14.2121 | -57.4098 | 2025-06-14 01:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| a6a1cf63-28b4-34b4-92ff-dea58353f28f | -13.9062 | -54.6084 | 2025-06-14 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |
| a70491de-d5e9-31f8-b5d6-39c7fcfd537b | -7.2214 | -43.1153 | 2025-06-14 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| d89d1786-536d-34ad-9479-bdbdd3eea1a2 | -13.887 | -54.6106 | 2025-06-14 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 9501861c-52b1-3313-b719-c6ede69249a6 | -6.9605 | -42.8816 | 2025-06-14 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 3ced150f-9c27-3640-9eac-eee01030a02a | -6.9602 | -42.9052 | 2025-06-14 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 7024e3de-518c-33ed-a0ec-4349d4108e2a | -11.011 | -55.0967 | 2025-06-14 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 2769fcd3-ae4c-3a72-951a-8b0a7d1086fa | -16.1967 | -46.4589 | 2025-06-14 01:10:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 3af6ee85-98b2-3996-8d37-c8708d7de367 | -21.452 | -54.5675 | 2025-06-14 01:10:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 7a2f0b35-8101-34d9-b2f2-af29abf78715 | -10.9205 | -54.7795 | 2025-06-14 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| f0d78af0-43da-3d9a-9aff-b9737b5177b4 | -11.0113 | -55.0764 | 2025-06-14 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 55f847a1-39a3-32bf-aa9a-7b95d7e6f131 | -21.4315 | -54.5711 | 2025-06-14 01:10:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 62.5 |
| cb97e54e-e45b-330d-91d3-2e97b5abb8bc | -11.7969 | -57.3428 | 2025-06-14 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 64e8ac38-a9da-3025-958a-64d4584d91f1 | -10.9353 | -56.8522 | 2025-06-14 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f6539b8b-0ae6-3463-8d2d-305481bfd4a1 | -10.9167 | -56.8336 | 2025-06-14 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 092e4761-e659-3f30-908b-b691eea24899 | -16.1967 | -46.4589 | 2025-06-14 01:20:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 13b3ca74-be13-3b99-97e6-d5bc81e0e3d6 | -10.9167 | -56.8336 | 2025-06-14 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 3da5964c-cecd-30fb-9b94-64f3392d8721 | -10.9353 | -56.8522 | 2025-06-14 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |


[Clique aqui para ver as próximas entradas](README5.md)
