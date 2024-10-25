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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1621e940-a792-3412-b4ed-124d08fba3c0 | -3.15056 | -50.45573 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fca466a3-da34-36b5-8492-375163f18836 | -3.14986 | -50.45996 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f2ea8865-f019-3c92-8bea-a3ad1f6d5ffd | -3.14939 | -50.46279 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 12657c72-dff9-316c-b327-d45572ce49a6 | -3.14559 | -50.45491 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fdfe9d14-5dbc-3f16-b578-c0e27b70f6b7 | -3.07494 | -50.50766 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a094707-eb37-3b00-84ab-c581fc230074 | -3.07316 | -49.5812 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47f69185-f830-3fd6-a3c8-49066600185f | -3.0718 | -50.49541 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2fa4d807-ab1c-380e-8eb3-28521601c7d1 | -3.07134 | -50.49828 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b7cdca57-02c2-364d-bb97-5bfa689e329c | -3.07088 | -50.50113 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 02ab56e5-0390-3d4b-a8c6-f7a4dc8b517f | -3.07041 | -50.504 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50c67c19-2dc2-3717-894a-db20fab0ade7 | -3.06995 | -50.50685 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10c4fcec-ac1e-3ee6-b978-3b755b194175 | -3.06749 | -50.36559 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d8cbf61c-c296-36fa-af4b-84f70aabe54d | -3.06729 | -50.49171 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf4112f4-82fb-3297-9ad6-6c125b3c84a8 | -3.0623 | -50.4909 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50da8e79-84f7-3d56-8132-81c6c865fb9d | -4.81783 | -50.88968 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e2655e7-7b52-3f2e-ab68-ca4092f519d4 | -4.72157 | -50.78921 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15c8c596-9bd5-35e1-9434-1df9f51ab9f2 | -4.61771 | -50.7935 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd604463-b05c-3170-8f57-2c858b814445 | -4.2342 | -50.63209 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 31402275-34d5-371a-b5ee-0482cbb450bb | -4.23214 | -50.6347 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 84ee45db-8005-3218-9990-05b3fb54b56b | -3.79702 | -50.62117 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 732e2a31-f814-3014-9d27-4a180f9a619c | -4.91944 | -49.8317 | 2024-10-25 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f5a51b82-24b4-3a3b-ae8c-4a179b4b9748 | -4.91863 | -49.83644 | 2024-10-25 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5457cb75-ec94-3f23-8a24-1e18cf02d468 | -4.91398 | -49.83581 | 2024-10-25 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 14c08099-116e-3eaf-a2b5-517beaefc84e | -4.91149 | -49.82795 | 2024-10-25 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e1dc9d0f-43c9-38ef-a977-29bd890bb947 | -4.91069 | -49.83277 | 2024-10-25 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ab30de3e-7638-34ce-9bd5-72a889a66dbd | -4.23751 | -49.91705 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1dbaaf4-054b-3240-a6db-a2a72f79ed3b | -4.18566 | -49.40319 | 2024-10-25 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d565ad30-5f93-3119-bf64-eb4b9a5f9ecf | -4.10569 | -49.28794 | 2024-10-25 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 28cb0618-4bf0-3415-bb95-c55f3b76c08b | -4.06632 | -50.03229 | 2024-10-25 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a5060c0-e721-3e53-bce9-078c05f0b7b7 | -4.02235 | -50.44342 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1237f380-cef4-3ca8-b9e0-75fe3ef804de | -3.94674 | -49.88749 | 2024-10-25 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ca9976c6-6b14-343f-8b6b-b36e8bfe70d9 | -3.92019 | -50.16986 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6a136ba3-275a-33c5-8f1b-1d6af1e4220a | -3.91537 | -49.38382 | 2024-10-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8492bbd0-d2ba-3917-bcb9-3eebf9b0bd26 | -3.76338 | -50.38329 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 914c706d-c86d-3ae1-b4f2-ff51a32af421 | -3.7606 | -50.38464 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9a818219-cb89-3337-9056-4439f5cfef2f | -3.66302 | -50.12112 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6be8eb6a-0c08-3e9c-948f-5bb0ea906b4e | -3.65904 | -50.11525 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dfbacb2e-45d0-3ba5-9fd3-3161d3108de6 | -3.65735 | -50.12558 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 43df7524-8727-3f1a-a663-134e5655e474 | -3.65649 | -50.13083 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6342c03f-0b96-323c-bb79-473f7ac34d23 | -3.65338 | -50.11965 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5abb16fd-9c91-3d85-bcdd-85f69fee51ba | -3.69997 | -50.16305 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0cdeb1a2-5222-338a-8dd1-c08b04987ebf | -3.66217 | -50.12631 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 589a95bf-f8b5-347b-b2af-746b31076cb9 | -3.6582 | -50.12039 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 831f9ddb-e5d1-3256-bdc6-0e5e1e72a6d7 | -3.65252 | -50.12484 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 85ab3639-9bc6-300b-acad-25152fa7e50e | -3.60406 | -50.57936 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ed2a6ac-07f5-31e2-876e-dee7c771df01 | -3.91636 | -49.38188 | 2024-10-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c607eabd-f946-3a10-a8a9-a4596dfb5e57 | -4.9724 | -49.77148 | 2024-10-25 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c235a9d-438c-3dc6-b640-6042d95904a6 | -4.91997 | -49.83414 | 2024-10-25 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d85dfe64-739b-32af-875d-a14595630de5 | -4.91611 | -49.8287 | 2024-10-25 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 88b7a1a0-d760-3d9a-959c-6a93070e4210 | -4.91564 | -49.82621 | 2024-10-25 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9f7726fb-56c4-3201-8e2d-7c42f086187c | -4.91532 | -49.83349 | 2024-10-25 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f5a5e2ed-57bd-3cf2-ab65-c3e21fc374c8 | -4.91481 | -49.83104 | 2024-10-25 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dea50606-4bd1-35c0-8028-6087c33b937c | -4.8183 | -50.88685 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f07d6afc-f085-3d8d-977f-68e6795a645d | -4.72656 | -50.78985 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5280b190-389a-3e2c-baef-fe17e8633162 | -4.43736 | -50.13971 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94c2444e-a355-3212-b271-42db4dbbf449 | -4.4233 | -50.78493 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c03e3b69-a0a4-34f6-855d-e1e1dc532469 | -4.23832 | -49.9121 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b604e2b6-cb9d-3b2e-ab1b-fca2da9a2267 | -4.23494 | -49.73 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d74aa61d-ce05-3371-bdd9-172b6ccc7320 | -4.23436 | -50.69002 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 67b1fbc0-cda1-3499-b973-7ca1f6e3a4df | -4.23309 | -50.62898 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a3d323c5-8c60-3a89-a2e9-fa14ecacbcff | -4.23274 | -50.69271 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8ecb5f93-41c1-32dd-82ba-98c1c0f5e8d6 | -3.51785 | -51.06905 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c090208-8053-3a1a-a1d3-b898bd287e4c | -4.21314 | -50.50618 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77b88072-b367-3580-b2df-de08a9444cbb | -4.10527 | -49.77144 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d70a1ca0-6fec-3469-9994-43fd749a588e | -4.06546 | -50.03738 | 2024-10-25 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| afdc88b1-b924-3cc5-b8f9-65dffdf60a52 | -5.29681 | -50.98355 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c6ce478-5eef-3773-bf11-01a073ca8e65 | -5.11358 | -50.71736 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8be34da3-60f2-3c19-a5c1-3443f4462215 | -5.11267 | -50.72289 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fbabe35d-e168-34a9-a008-a8b2055d23de | -5.11175 | -50.72843 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ecca14d1-9a05-3658-aa47-32f4d8cb3306 | -5.11089 | -50.71877 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 793ba873-b295-322d-ade8-98e8a8705b50 | -6.20473 | -50.85942 | 2024-10-25 04:14:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d55a996d-8e20-3d02-9c0f-897e080628bc | -5.79685 | -50.16451 | 2024-10-25 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2e08d9b-1850-3b36-b6a2-679239fabc45 | -5.67702 | -49.95275 | 2024-10-25 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14898d43-a098-3a85-a5e0-31e352689158 | -5.55785 | -50.43987 | 2024-10-25 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| add31916-5f07-3484-9ff7-c41d0116bab1 | -5.30528 | -50.56606 | 2024-10-25 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3977d1b6-0ac9-36d9-acce-be8525dc735f | -5.10993 | -50.72428 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e5ae9b7-6c4a-3b34-871d-0952c4bac0af | -5.10897 | -50.72985 | 2024-10-25 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8f57014-4a30-36f5-8192-a03426ff4802 | -5.0639 | -50.44942 | 2024-10-25 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 16a53efe-465c-3119-94d8-883cdc5f656c | -5.76857 | -49.94168 | 2024-10-25 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8786869-5dc5-31a5-ae37-8765301d566f | -7.44805 | -50.79064 | 2024-10-25 04:14:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8cdffb33-93f3-38b5-8e7c-4910e9d3279e | -7.44418 | -50.78487 | 2024-10-25 04:14:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86dbd51c-3650-3a56-8059-40f85a15a2d6 | -7.44331 | -50.78993 | 2024-10-25 04:14:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c69f59d9-9c15-3410-801d-9ac539de3f4f | -6.896 | -50.32717 | 2024-10-25 04:14:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4068cb5d-08cf-3277-bf4c-b7e20c328ead | -6.81512 | -50.86286 | 2024-10-25 04:14:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d337e570-6871-34f6-9bae-9e45c949954e | -6.8151 | -50.86074 | 2024-10-25 04:14:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0cccec4e-2197-3762-9270-8913bb8f933c | -6.80755 | -50.8754 | 2024-10-25 04:14:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2f18d4ca-1d4a-38f8-a048-6f5a49257b09 | -6.68256 | -49.9749 | 2024-10-25 04:14:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b917e693-043d-3bab-a00b-2938aeb46a44 | -6.68176 | -49.97951 | 2024-10-25 04:14:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| cd6c6041-6005-37a9-a0c4-89e1a872267a | -6.53482 | -51.13257 | 2024-10-25 04:14:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d446760c-0160-33aa-b906-2717b9213e16 | -2.23437 | -50.67738 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5728d13c-d2dc-3587-a32f-f721315a97b1 | -1.52501 | -50.62373 | 2024-10-25 04:14:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 160b79c2-c032-3ee2-923a-ae3951ac3135 | -3.6398 | -51.24965 | 2024-10-25 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c6f6647-2773-3aad-b5b3-7f8eae149cae | -3.51836 | -51.06593 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9f5dbf3-96aa-3849-b085-c888d71357da | -3.51563 | -51.01832 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12bc6886-6ddb-3896-81b8-eeb08a31ef38 | -3.51321 | -51.06513 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1e84d256-4502-31b4-9181-227de1804886 | -3.5127 | -51.0682 | 2024-10-25 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1b1257b8-ad69-38fb-9f87-1e4bbef38b9d | -3.29721 | -50.74907 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e672db1-e0cc-3cd3-bd3d-b8be5b7f2a45 | -3.29672 | -50.75201 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b100ee88-c1c3-33ec-9f17-63dcb95d0918 | -3.29265 | -50.7453 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0370067b-2abd-3965-8c51-872e5d4ce618 | -3.29216 | -50.74825 | 2024-10-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README34.md)
