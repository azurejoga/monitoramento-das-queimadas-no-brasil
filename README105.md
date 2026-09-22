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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c78324f-f9c5-3ae2-a251-3e4edb96ce2f | -6.1306 | -59.94445 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a23fb9d5-ba51-3b04-93af-cadce3ff2c28 | -3.0722 | -61.17994 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac01031c-433d-31df-9156-634f4d2a7129 | -5.41723 | -60.21491 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8d431c4f-a331-3bc8-98b0-63b25b125aa3 | -5.85648 | -52.03303 | 2026-09-22 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27fa3491-2e72-3085-af34-344d1ca4a6ba | -8.91888 | -50.93411 | 2026-09-22 05:42:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ac7ce72-f4ad-3dab-97e7-e9aa11d8ede1 | -6.70075 | -59.95784 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3df499a6-f880-3b48-96f6-947351ce12a0 | -3.36361 | -61.28814 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e42162a3-4152-3d3a-bd2a-b5bdd1abab08 | -8.48776 | -57.61368 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6aae5a07-6e2b-30aa-bd7a-10f3ec620cfc | -4.26369 | -60.00966 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac02adad-828e-3c74-ab5e-cda7e4f30f8c | -6.13709 | -59.92686 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2dd199b5-5e0a-32e9-af33-644711941225 | -3.06112 | -54.41678 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbf017c0-c21a-38a9-8319-603d1a46e56d | -3.49012 | -59.57158 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 79718b83-41f8-3bf4-9dfa-988f98f2dfd9 | -6.46479 | -59.98389 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9fc31ade-0b8b-370c-823f-f6571efdc429 | -6.09549 | -57.68277 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bd3f9a08-23f1-3495-9ef4-025d0830803b | -3.92656 | -60.49242 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63f4f113-483e-3eef-b729-ba8249133165 | -6.43262 | -55.61478 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2cb37b24-2de0-3bb6-857f-d853c137dc31 | -6.73392 | -55.06962 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 396da727-79ec-31c2-b267-2eecd0f9a2ab | -6.30674 | -60.00875 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8cf334cf-44ed-34c7-8bc4-4ebb253a2090 | -3.38868 | -59.52713 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54c70d08-b2d7-3366-9aee-88546ef3068c | -3.33941 | -59.86984 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a422bec-78b7-3576-b582-5724f807d721 | -3.92685 | -56.05352 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71cfa537-d0ba-30f2-a954-82f26a6486ab | -3.29809 | -57.86445 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f34430f3-ebeb-3e6f-86d0-76c601c095a9 | -3.52601 | -58.6609 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 350d5550-17e6-36aa-b390-4cf16bbec695 | -6.80915 | -59.39754 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 657b45d5-16ba-32ba-b0b9-ddaae95f382b | -8.91191 | -50.93269 | 2026-09-22 05:42:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aa6150c3-1f82-3f87-aa74-6f4be4582b7a | -3.10914 | -60.72049 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e26e681-2902-3c09-9b87-15f381ad9a11 | -7.72189 | -61.2291 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13261fc7-4067-3676-b7fc-3d3bdb763cc6 | -3.46155 | -58.32137 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c39f57f0-d967-3f78-a69a-6d43449a12b7 | -8.11556 | -54.80531 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f503982a-8650-3397-942c-dd373a0d9387 | -5.80598 | -57.73176 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75618eaa-7af1-36f2-94b8-e1be07d48d90 | -3.0646 | -61.27342 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb6c0694-d957-3a6b-870b-db0f7b58e829 | -2.86049 | -57.81491 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5137fc73-a14b-38e4-80cf-eea06a9edd73 | -3.60048 | -61.72093 | 2026-09-22 05:42:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 54fa3406-0f94-3c67-95d4-b0ae51d8a685 | -3.15223 | -60.42196 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5330614-e423-3845-b4e8-d345b92d3d26 | -6.75185 | -59.1166 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd96a6ac-6740-37ce-a80c-0662bcece08e | -3.7945 | -59.70757 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f67037b-b8ef-324a-be46-824220011a2b | -2.93081 | -57.79548 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 079abac5-3593-34f0-a199-d0d8862901e3 | -3.17104 | -58.5949 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f094478-57b6-3040-bb97-94fd9dd40694 | -8.91401 | -50.93325 | 2026-09-22 05:42:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50dbcda8-e725-340e-80b1-6c1740292063 | -3.48709 | -59.5666 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20ac6e67-2f4f-3c3e-91bb-ac83e041f358 | -7.72126 | -61.23319 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10ba5c04-2519-34c7-88ad-49bd65e566de | -6.77814 | -58.60816 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65a10f44-6241-3295-8320-3f6f36150060 | -2.85749 | -57.80694 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c89790f-c4ea-32bb-9d60-a076f3732a70 | -3.78235 | -58.84682 | 2026-09-22 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a2e8177-c518-3978-b67c-a33ee35f349a | -6.077 | -57.62769 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 88a9bc9f-c41e-34a1-9710-f2554659260a | -6.64944 | -59.96448 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35dfe42e-c7d7-3f38-be89-316cce720a82 | -2.61227 | -59.92255 | 2026-09-22 05:42:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 306af00e-20ac-39e8-9d63-a376fcaf3014 | -3.68605 | -60.57254 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9cb3048-739d-37c2-857b-f6471ed0968f | -3.06517 | -61.26973 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbc0a338-dc82-3964-a6e3-f7bad28e1011 | -6.12739 | -55.81955 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4156d08-5366-396d-8f47-a9950c2009dc | -8.10222 | -55.35188 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc1ad2e7-6edc-3d28-bbeb-f81cac64cc68 | -3.42792 | -61.32418 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20770bc5-215f-3b63-bba4-396280d2c57d | -3.0835 | -61.1739 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b35e4113-b03e-3328-b475-609073ad7c87 | -6.31176 | -57.74697 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 692be93f-61ed-3abd-921e-ca2c50a5140f | -3.42681 | -61.30883 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b0386ae-5dc3-3d9b-9973-15cc79fdbab8 | -3.71457 | -60.55245 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9bcc3305-edd2-3704-ba61-c2dc2980014a | -7.61075 | -55.34803 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0415e4c0-8877-378a-8451-de5cc2ffca9f | -2.99497 | -60.80208 | 2026-09-22 05:42:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56be30f9-cb84-3bbb-8ca4-86a4329c0d86 | -6.64733 | -59.92633 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 28.5 |
| fab9d4df-da7e-321f-a190-5c55584822b0 | -5.87689 | -53.63974 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e64f4a47-41c0-33f1-97b1-3bff404e4f3a | -3.23693 | -53.95344 | 2026-09-22 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 463d37b8-12d2-3b92-9638-4760e200f637 | -6.12547 | -59.95295 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b3735e6-24ed-3df9-a446-6404bdfcbf43 | -3.86673 | -51.18781 | 2026-09-22 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af6aee8c-f8ad-3aa8-bc44-6e2d2b2fe034 | -3.72014 | -60.5848 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d84ad322-ce5e-3e66-84ae-003732f91885 | -4.51671 | -54.98266 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb500dd9-1a19-3a37-ba83-ee4589aa52c4 | -6.80554 | -55.83219 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f9898c4-58fa-3fdf-acf0-9a2ace74b49d | -8.83456 | -50.4938 | 2026-09-22 05:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 221a1ea8-f2de-37cb-a7f9-ed0d2494c038 | -6.29722 | -57.74733 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a020191-06a6-32aa-8613-7156aff3af53 | -5.72537 | -53.45757 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f612cc0-3a6e-36a1-bb08-fdd1393a9421 | -7.72764 | -61.25377 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b826b31e-6939-3223-8a25-76ca29394ce3 | -3.60644 | -60.57248 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18f84c88-4a85-356b-85b4-f213231f5883 | -8.25842 | -55.30027 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1e2e31f-f5c3-328e-a3d8-fde11655d637 | -3.82148 | -59.33077 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7a11066-78d6-3f3b-b1b3-e85647ffaa3a | -6.30801 | -57.74215 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86033f09-1fb1-3ffb-ae4c-4d873a865d6a | -6.09509 | -57.62608 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 689f1fa4-df6d-3674-8d2e-ebbdb26f3448 | -4.48339 | -55.48849 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd0a6157-f44a-3ce7-8fa5-0c07bc64433a | -3.90943 | -59.61478 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50a23f35-a290-3cb6-b049-176d888a3b24 | -3.15022 | -61.39861 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4118e823-a3d2-3ef9-8b09-7a4a96c7c855 | -6.15897 | -57.71164 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2cf8593b-36f2-3963-8762-535457305d95 | -3.41938 | -61.3115 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e111fb5f-aa8b-386e-8401-c627689b484b | -6.43304 | -55.61185 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b247aa50-82b3-326c-b7ad-0dbf703f0d6d | -6.10245 | -57.70346 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba0f4bdd-2a8e-3269-aee7-3b35f5dce55c | -8.92175 | -50.92854 | 2026-09-22 05:42:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6ea1de6-0aee-3b0e-8bba-266d54395f06 | -6.64802 | -59.9217 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| aacde1e5-3e3e-3c41-b19d-382b958b4f6c | -4.56221 | -54.9236 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5f1444f-9ecd-30c5-947d-55b7b289ebdd | -6.8328 | -55.53798 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86330255-96de-33fd-9f70-0ceab7165bc4 | -4.26867 | -55.44425 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6202497c-6db9-3cee-8606-ec7bed62323a | -3.82308 | -58.89297 | 2026-09-22 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c116cd7-6d94-3bba-8136-b40b49b14691 | -6.0986 | -57.69165 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6a4401ed-b822-3e40-835c-882a5e789cc7 | -4.2075 | -59.91478 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6d3addc-4863-3f0d-90ef-4f5b9cf397f9 | -6.04795 | -57.82316 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1fe6191c-d291-3df2-b080-26bc4aedbf98 | -6.92264 | -59.63282 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55b3ca6a-a676-31bd-9256-783a9a11d61d | -3.68462 | -60.60477 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 439729d6-dd51-3a3e-8549-4c993db753c4 | -2.65401 | -59.68281 | 2026-09-22 05:42:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9726e8c1-a0c7-3b78-b216-2977676a4bc1 | -6.13812 | -59.94556 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f67429c7-7194-30a4-a9b2-fad01ceb8745 | -6.86203 | -59.91135 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67282623-77ab-307c-b9fa-0ea6e10ecd24 | -2.78299 | -59.95902 | 2026-09-22 05:42:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5169d12f-6acc-3528-8a16-3e06c7d4d758 | -3.14346 | -61.39481 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 222abff4-2663-3e55-b399-4e8f7f5ef15f | -3.04126 | -57.42008 | 2026-09-22 05:42:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58fea519-3555-362b-a278-bd1e456ff3cc | -6.73773 | -59.42006 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README106.md)
