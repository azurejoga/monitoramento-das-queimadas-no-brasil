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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c48ffe8e-b86f-37e2-8314-6757e93d0c04 | -7.28824 | -45.36118 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 179d93ac-c652-3c21-bb08-3583c2acd84b | -5.95298 | -53.59061 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c85dbe43-db33-32b5-81dc-9d14ce8bc7f7 | -6.32707 | -54.74581 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a20e46f-67c7-3bc3-b274-f3baeb4660c8 | -6.64376 | -45.17115 | 2026-08-25 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cc6f7adb-b5c7-3f3b-99a6-f465dfeff95b | -6.18072 | -55.43706 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8046e4fe-f7f7-344f-9e26-8b18524ad6d6 | -6.18296 | -53.52719 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebe98d9f-0ba4-3aca-8acf-2f5cd20a345c | -6.34466 | -54.77295 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4485081-3995-3a98-a192-c07a47ab473b | -2.89281 | -48.80867 | 2026-08-25 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3cafa60c-440b-32b5-9bd6-ad80910381ce | -7.26458 | -45.84779 | 2026-08-25 05:10:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 08c9d2dc-1ccc-32f6-a2f1-24d05b75b91f | -1.42024 | -55.72717 | 2026-08-25 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6253527b-2bad-359b-877d-9f997ec171a7 | -4.12944 | -49.45226 | 2026-08-25 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4fccb49-a737-3d69-a0f4-b41ee28095b7 | -6.33061 | -54.74634 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d77aeb0d-9134-3136-ac7c-636b69b3f615 | -6.3376 | -54.77188 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca8cccfc-a6b0-353e-976a-9957f1abe2fd | -6.23277 | -55.4871 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a304b6d6-c834-37bc-b8bd-9349111917bd | -3.62712 | -55.30574 | 2026-08-25 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ecb0742-56be-31a2-b1c6-0b80df8df2f5 | -4.99766 | -56.13842 | 2026-08-25 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a7ee4dd-3649-396a-86ed-5ce5aa03efd9 | -6.33175 | -54.76281 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97172547-f690-3fcc-83a8-350cc1caa027 | -6.23334 | -55.48336 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d40937e3-4050-3b91-b0c9-16dec7e7b75d | -4.78897 | -56.10312 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 970da891-22a3-3aec-9627-1f5cad8e10c4 | -5.78964 | -57.60806 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7eea30f4-b79f-3e1c-a325-96cd58c252f1 | -5.01156 | -56.13694 | 2026-08-25 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6eb9b543-50a5-36e9-87c9-31c6b8ee089c | -5.13455 | -60.36293 | 2026-08-25 05:10:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37644b04-11d1-3cb8-b014-e48a014e02da | -7.28135 | -45.35898 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2bd8bff0-a4c6-3c7d-9f28-3098285c40f2 | -6.41222 | -51.71218 | 2026-08-25 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 42af5044-d137-39fd-bbc5-05dee0c07c85 | -6.33828 | -54.74342 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3fd189b6-cc7c-339d-981f-ac5100e8e449 | -3.53364 | -48.18335 | 2026-08-25 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 49c42260-fc0e-3e06-aba7-00803befb81a | -5.77512 | -57.54925 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b9d6dfdc-5b3d-395a-ab7e-e0500a35a4f5 | -6.34759 | -54.77746 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a25e2fa8-92fe-3f4b-bd40-07dcddac9c5d | -6.16514 | -53.69935 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5fbe8a43-877d-35ab-92d2-67fb67a5afb1 | -6.08995 | -53.42252 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f469922c-0e66-3e51-ba39-5bbe774a2833 | -7.28097 | -45.36578 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 144b4e6f-6053-3338-8c58-d9351c3a2bd1 | -6.3488 | -54.76949 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31cdf0a1-c355-3b8c-bc15-66acb19e9ca3 | -5.86447 | -50.14519 | 2026-08-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e458571d-203c-3e85-8577-e5a50c8c3f92 | -7.28016 | -44.08263 | 2026-08-25 05:10:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d77a1ed1-68d5-303a-b4f8-8b02303e47e6 | -3.04243 | -48.98367 | 2026-08-25 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d5ce5d1-ac4f-37dd-a6ea-e48bb27e113d | -6.18081 | -53.48956 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 512c6940-65e4-3e34-b35c-f2da4bb3c3e6 | -6.16886 | -53.69989 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e2cc4b1-6269-3b68-ba46-b2cab10e53bc | -7.26714 | -45.36968 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d4c7708c-4121-3e5a-95a6-01631361a9a8 | -5.6136 | -47.00243 | 2026-08-25 05:10:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d55ed96-8a15-3423-b211-805d47a99ceb | -3.09865 | -61.20211 | 2026-08-25 05:10:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dca165ef-c19f-39fa-a205-08b1fe56ea27 | -6.18605 | -53.5323 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9143f113-855b-3345-b725-fd892d5c1577 | -6.18359 | -55.4413 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0022738-9fa9-32fb-8c16-df904251e780 | -2.89931 | -54.26376 | 2026-08-25 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01751141-ffa6-3d3c-a92a-c4f02f97db26 | -4.83555 | -55.91143 | 2026-08-25 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 829ae75e-ec05-31d3-9db2-c072848f2586 | -3.69885 | -51.11018 | 2026-08-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c6003df-acc2-3340-a203-fd4acae1224d | -3.54062 | -48.17182 | 2026-08-25 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b1f70047-ca9e-3ba6-8865-51f8431b1555 | -3.10776 | -61.22597 | 2026-08-25 05:10:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99479ed0-1651-37c4-a1f7-439e95bae95d | -3.72779 | -55.95333 | 2026-08-25 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9b461aa-1b56-3101-a1e2-0f45235f8d18 | -4.8389 | -55.91196 | 2026-08-25 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae97dafb-03b6-3817-8e8a-17743608b697 | -3.39084 | -59.56546 | 2026-08-25 05:10:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b83555d-057a-3252-aa9e-3c17d64a3364 | -7.26642 | -45.37515 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| df4d466c-baa1-370b-8f51-a2f48d9979fe | -1.86909 | -47.98351 | 2026-08-25 05:10:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dc0251e-8838-32b4-8d80-833470358da7 | -6.64448 | -45.1655 | 2026-08-25 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dc6decb1-6778-3a60-9030-9f5686b737d2 | -6.32648 | -54.74979 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6ff9e99-6d2d-3698-ba39-1b028a4766b9 | -5.00822 | -56.13644 | 2026-08-25 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c477fd0b-c691-324e-a438-baf40ae0f053 | -3.81391 | -51.91244 | 2026-08-25 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2090d797-fbb6-3c37-9572-2268c0d0bf97 | -2.81078 | -48.67092 | 2026-08-25 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ec4e0fe3-536c-36cd-8fa7-e8467f11f090 | -6.08336 | -55.54838 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a628d48c-6f8c-3100-92e7-9f9cf4dd4c23 | -5.76013 | -48.67341 | 2026-08-25 05:10:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0c9dca98-5c70-3050-8244-7f6c27099b22 | -4.23567 | -49.96452 | 2026-08-25 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d52cfcd-7415-3d80-bc77-7638e48205ac | -6.17622 | -55.4447 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc7dd4f1-fa10-376b-82cd-a67c5c617064 | -6.32941 | -54.75431 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d10fa8ba-2ee6-32c2-bf11-ae29186fe75d | -5.92084 | -43.6403 | 2026-08-25 05:10:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9680158c-d59e-32f6-ba40-5f63acb8b4bb | -3.01108 | -51.04966 | 2026-08-25 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 349a3fac-5702-3dce-beb2-a20eec07dd0c | -7.26757 | -45.36277 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 72f11779-01ff-321a-9081-41f3b930e639 | -3.93982 | -52.12164 | 2026-08-25 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70df92e7-86e7-3113-93cd-696162dc3e11 | -6.17222 | -55.44791 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30190631-79ae-386f-9f21-8c7482d94395 | -7.274 | -44.07467 | 2026-08-25 05:10:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2212883b-d74c-3258-99fb-cf33598b82ed | -6.18874 | -53.51411 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5656bd63-2ff9-34c5-bd6d-4bbc39da74f9 | -6.18415 | -55.43759 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59d10a85-1e20-3d63-af77-b062c821d1a2 | -4.8361 | -55.90787 | 2026-08-25 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b815be9-e57d-350b-8a55-9bb15f48f8b8 | -6.14302 | -55.73351 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 886ea487-5915-34a7-b5cf-7dadcb841466 | -3.31464 | -50.812 | 2026-08-25 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4404c9fc-57ca-3796-b390-7bd4a2d69d1e | -6.17279 | -55.44419 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97ad68d5-0394-308c-ab24-16aecf787f93 | -7.25757 | -45.85205 | 2026-08-25 05:10:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7f904bc8-73d7-39d2-a6ea-3a5ef053d979 | -7.28806 | -44.07695 | 2026-08-25 05:10:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1694f78f-848d-3627-9a73-6b38e69d7bb5 | -4.47535 | -54.80459 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cc801c6f-9ac7-30ea-886e-a381fbc08e33 | -4.14086 | -56.35994 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f68b3cb0-3245-3f21-b050-c3e29ed54584 | -5.78896 | -57.56908 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a8770b3-f546-3aa8-9e6d-b7355cdf8228 | -7.28751 | -45.36663 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5b1059cb-d9b8-3209-9b0b-4e703d09d63b | -6.24759 | -55.41287 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3dbb9a6f-6ec1-3c0f-a9ea-eba203657ece | -7.25822 | -45.84698 | 2026-08-25 05:10:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e3d46d55-39b0-3137-8e0e-e975b45dc8db | -4.12868 | -49.45734 | 2026-08-25 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ca52e9bf-be26-36b6-bd42-e47631f61644 | -6.33414 | -54.74687 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6d2b805-7525-345b-b11b-2b305138ab81 | -3.0147 | -51.05419 | 2026-08-25 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b2bbbc6-d63d-3ed4-974b-dbc113b5f57c | -5.77789 | -57.55322 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 808572f9-a04b-3bb7-a2ff-3174527ac295 | -7.27516 | -45.35941 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ccd2a3d6-d578-3bf7-9da1-158a8066cf7c | -6.23668 | -55.39209 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b581c82-7d4f-3a50-9fe8-ca57b2d3f761 | -3.54395 | -48.18507 | 2026-08-25 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea9acfaf-d896-338e-9d23-486567911ba0 | -5.95496 | -53.57725 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66c5a503-d65f-37b0-9d7d-f9096f4bad59 | -6.21566 | -55.48437 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b07ced43-8562-3de3-b58e-dc8daf89a3a6 | -7.28718 | -44.08383 | 2026-08-25 05:10:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e25fc06d-cd48-3a59-99e6-6f6c5497cd6d | -6.34053 | -54.77642 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a565f18-c61d-3778-8825-30d4cc7499c5 | -1.26215 | -55.84777 | 2026-08-25 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3694b67f-201c-39ad-8ba4-06493ac91e77 | -3.04321 | -48.97831 | 2026-08-25 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09d16ebd-9d2c-34d8-8b68-cad77a07216a | -7.26061 | -45.36873 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c02ccbbc-1533-3d2d-85f0-7b25eb2aff06 | -7.25245 | -45.37732 | 2026-08-25 05:10:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 64afc78f-f4a5-3722-a508-4b435473d923 | -4.96382 | -56.26989 | 2026-08-25 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 333d2251-7bb8-3f09-9f17-2d9c4410a5f8 | -7.25121 | -45.85128 | 2026-08-25 05:10:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1250227b-5568-37a5-b986-032d0fb9d738 | -6.22705 | -55.4786 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README45.md)
