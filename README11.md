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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dd5015f-b755-3026-8103-0492d856428d | -3.12814 | -54.66256 | 2024-12-04 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| db89abda-959f-3d7b-bc5b-9429dfcca26b | -3.3318 | -53.54745 | 2024-12-04 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 720c3051-abc3-333d-8843-db8ed768b77f | -4.33027 | -48.0975 | 2024-12-04 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 6fa70056-ff88-37f1-8dbb-c97c58f54d9d | -2.61541 | -45.40804 | 2024-12-04 00:54:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5093fdb7-5bc0-39e2-8c39-5d15dbe47403 | -3.75476 | -51.18576 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ea1bea2d-35da-3a2e-bd3b-f1125cb70b43 | -4.51304 | -48.02225 | 2024-12-04 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8d319357-3224-3f1f-8f5b-0ae7d60738cb | -3.33527 | -51.20362 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| c141265a-8db5-3415-b60b-a42038841254 | -2.93481 | -45.48496 | 2024-12-04 00:54:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 21c6736a-53a5-36ff-a394-c07299c9862c | -4.43941 | -47.49918 | 2024-12-04 00:54:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 197cbe73-0414-3d95-8bec-8b39bf597e54 | -2.83301 | -46.76635 | 2024-12-04 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 74e179f5-f359-3b08-a27a-a3710f6eefc6 | -3.31752 | -50.08397 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7d6968a5-ed93-33e8-96f3-c15164cc7152 | -2.94847 | -51.41351 | 2024-12-04 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| aefa4605-6ac0-3c7a-95bc-1d71c102f696 | -2.98019 | -46.94907 | 2024-12-04 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b02f8fa6-1579-372b-88bc-c8c830da9af0 | -2.97076 | -46.95058 | 2024-12-04 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6af46622-ba3c-3b07-a97b-9370dd15e554 | -3.59211 | -50.53804 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 45dfd834-8734-38e8-8a6a-254a66c2ec21 | -3.97173 | -47.24894 | 2024-12-04 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e8854fe8-f031-31d3-9e37-3222882245d1 | -2.02223 | -45.53716 | 2024-12-04 00:54:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 95c97b26-9e62-364f-bf87-6cbab89ce106 | -3.84813 | -52.16272 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 14ab4a44-c8d6-36e4-8ce1-c1af2aa03a86 | -2.16106 | -46.14723 | 2024-12-04 00:54:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6701e187-93ba-3c5e-bfca-6d070bac9ca7 | -6.08283 | -48.05062 | 2024-12-04 00:54:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b717432d-f104-30c4-9fc8-95f6fb914f41 | -5.61968 | -43.95652 | 2024-12-04 00:54:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| ff6f7532-95da-3b5a-ac60-3bf74de0912f | -3.13163 | -45.99825 | 2024-12-04 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fcc24204-16a9-3ec8-8683-47556e036e5f | -3.3809 | -52.78922 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ad2c081c-f232-3a55-8555-086db38e7256 | -3.21626 | -53.71701 | 2024-12-04 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 82f731e4-1eff-3af9-8547-31447c05bfac | -2.42176 | -54.02739 | 2024-12-04 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 088e6b8f-29cb-3502-8c47-449a231618a5 | -3.24612 | -51.29303 | 2024-12-04 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c06dcc4b-5f01-3b74-ae90-1b57f6e8a5b9 | -5.62021 | -43.96227 | 2024-12-04 00:54:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5d59f6f1-6cdd-3a47-8dbe-c204d7402206 | -2.72732 | -49.08539 | 2024-12-04 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 33f38687-238d-3f39-98d0-89e72039345f | -3.0879 | -53.37818 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e97c39a7-6827-3a82-84d3-61a7ddeb5064 | -3.93222 | -46.72404 | 2024-12-04 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 871505d3-8647-3a13-92e6-8af5731e1098 | -3.5533 | -51.33814 | 2024-12-04 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| eabdc1f0-8cc3-367c-9fe4-15808aba397e | -2.84563 | -49.14334 | 2024-12-04 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 895ecafa-d0af-36ec-9788-c70521099733 | -5.27357 | -46.17301 | 2024-12-04 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6f6b2bb5-a840-37a3-b0ff-44a7d406e154 | -1.70237 | -52.60597 | 2024-12-04 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 162a1f4d-e6d8-3c28-b124-4e85733065bc | -1.39245 | -46.42279 | 2024-12-04 00:54:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 159043ad-a6b9-3aed-a79d-efe694ef7cce | -2.69216 | -51.8698 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 7e083683-b445-32e6-9b7e-fd4965cc8479 | -3.61037 | -50.80481 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 91ac5d11-fbde-31c0-9aef-7468efc57d97 | -3.83698 | -50.90806 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 99d2aa9b-85d7-3d3e-b237-8ddfb743f4dc | -5.98539 | -45.36026 | 2024-12-04 00:54:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b27aa562-c798-33bc-aedf-7816b1d897b7 | -3.58187 | -46.21106 | 2024-12-04 00:54:00 | TERRA_M-M | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b22ca992-e668-39b1-9805-506fe402dda5 | -4.31112 | -48.09107 | 2024-12-04 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 593fbb9d-0959-34fa-93dc-d8245200a452 | -2.67602 | -45.22813 | 2024-12-04 00:54:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 109cbd08-2337-3e62-b9a4-5bc8bc0630a3 | -4.5855 | -50.4665 | 2024-12-04 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 24b7d721-1f17-381b-8b33-994aa5a1542e | -5.81985 | -46.46505 | 2024-12-04 00:54:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fe47252c-538f-317e-b180-0cb13a8da5e5 | -3.19251 | -50.64682 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3b19c512-4fe8-33df-88d2-3b8c4184891f | -3.98133 | -50.3586 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| d0db7ecf-6db2-39eb-99c6-f2e8ef76e91d | -4.11548 | -49.0673 | 2024-12-04 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b8c85b59-48d7-34d3-b794-9ff11359c6f8 | -0.02017 | -51.2725 | 2024-12-04 00:54:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a39f8606-f964-3efc-8e06-d9802b61c784 | -5.3525 | -47.90223 | 2024-12-04 00:54:00 | TERRA_M-M | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22f7f7b7-4411-3fc2-a249-2e1b1627f77a | -4.39099 | -46.00492 | 2024-12-04 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0ea82375-b9b0-38b0-90d0-f530414180d8 | -3.087 | -49.21698 | 2024-12-04 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3b710e41-3ff6-3380-bda9-a06afa0e4a68 | -2.63509 | -45.74094 | 2024-12-04 00:54:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 9ef0cd58-7112-3314-8ebb-6d20c2da53a0 | -3.9648 | -48.11875 | 2024-12-04 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7c524ec1-b210-3b20-83f9-c40d2c9db9b0 | -5.56869 | -45.16956 | 2024-12-04 00:54:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9f9b9b08-a186-33a3-abac-9242746132c3 | -1.70965 | -46.20684 | 2024-12-04 00:54:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6d38fade-52d0-3fed-b064-9029c0060e38 | -2.81862 | -53.07231 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 06c9fae3-2d8e-3c65-a003-676a73e74a89 | -3.70634 | -51.36201 | 2024-12-04 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| fa611ed9-8786-3955-878e-9894b7ab8b9c | -3.80895 | -46.94867 | 2024-12-04 00:54:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| b791fa84-bdd5-396e-896b-b1d2fc98d818 | -3.17448 | -44.44733 | 2024-12-04 00:54:00 | TERRA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d18cd40f-038a-3443-a531-0db2efb89815 | 0.42863 | -50.76534 | 2024-12-04 00:54:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 85cdb9b7-ad16-3def-8a05-d33044bb43d2 | -3.422 | -50.1742 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0f8dcb61-009f-30a3-aa17-15a3ea2438ef | -3.10952 | -54.61457 | 2024-12-04 00:54:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 8e0ecea1-59d1-3007-8333-7fb590441ed2 | -2.53017 | -45.57397 | 2024-12-04 00:54:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1a7a0fd0-08f2-30e4-a0ff-753efcdd8a88 | -4.11063 | -43.93278 | 2024-12-04 00:54:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 1243146b-47db-3d7a-ae1a-4359536f2d55 | -2.77632 | -50.29792 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4d5e31a3-7c56-3f7b-820b-daf1f557207b | -3.72785 | -50.05738 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4821b6e5-c73f-38ff-a2a4-991243ab52d2 | -2.89322 | -51.82404 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 344056ae-9f99-3a91-9700-d3b75b071bd1 | -4.01565 | -48.81767 | 2024-12-04 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 8aacaed2-921b-338f-bbbf-e2ff4304082d | -4.19866 | -50.67073 | 2024-12-04 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3c09e1ab-150f-3a90-8782-ed7a327ba7f6 | -4.44169 | -48.69953 | 2024-12-04 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 785736d3-ad07-3da5-accd-684a1a9a101b | -3.65904 | -47.12356 | 2024-12-04 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| ea963f33-2172-3b87-bd85-a24f884ce8d2 | -3.41783 | -50.27695 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d4d08b8e-bc34-3267-be61-8e37e918e394 | -2.69507 | -51.86374 | 2024-12-04 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 32be4fdf-9e0b-378a-9402-5fc57f47abf9 | -3.92078 | -52.39786 | 2024-12-04 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 319557a3-dd88-3cee-b480-1d5cdacbb231 | -3.55126 | -50.17769 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 4eec8051-d40a-34e7-987a-78066871281d | -3.53405 | -49.91624 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ff95c7d9-5749-3132-8a68-3b5095a242f3 | -3.48778 | -49.98363 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 300fdf90-d380-3510-9a38-82335a2a1896 | -5.56693 | -45.15755 | 2024-12-04 00:54:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b41e37fc-f00d-31dd-a050-9d785bbc92f6 | -5.57892 | -45.16806 | 2024-12-04 00:54:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 0df0b155-5411-3353-9f71-0f91d7bed2cb | -3.57031 | -50.31469 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0c4ae9ef-5da4-31a0-b90c-c52ef2a12045 | -3.56904 | -50.30553 | 2024-12-04 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 38b0cc02-6c50-3e7d-8df4-4ba5ded3e833 | -3.06682 | -53.26796 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 1277b963-cb71-3d41-86ac-d987348cd313 | -3.26663 | -53.66064 | 2024-12-04 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 9b68de6f-6cc7-309a-8094-5dc0fa7f5706 | -3.21072 | -50.64426 | 2024-12-04 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a8cbd4dd-98ca-37f2-87b5-11a8620b10f9 | -4.32133 | -48.0988 | 2024-12-04 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 7965c33e-8f1f-3012-a785-445d163d6a30 | -4.05529 | -47.00638 | 2024-12-04 00:54:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9af76a4a-9f3f-3769-8189-8fe416034d4a | -1.7039 | -52.61724 | 2024-12-04 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 0a701a71-74fe-3ed6-a4d2-5f7680f46e66 | -1.88298 | -53.30805 | 2024-12-04 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8c73077e-2d2a-320f-9edf-48f1bce15fb3 | -3.50077 | -54.03186 | 2024-12-04 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a19eeb93-3f2a-3412-8ed7-3c91e39fd518 | -4.08721 | -48.86429 | 2024-12-04 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3085e0bc-6818-3775-833d-a91eb45143cb | -2.91392 | -52.21066 | 2024-12-04 00:54:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fea75f57-9650-3610-a468-589490148f57 | -4.91553 | -47.86974 | 2024-12-04 00:54:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b79a6bf3-71de-3350-acdd-0ce7169bb006 | -3.93092 | -52.39665 | 2024-12-04 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 32047ccb-52ca-3c87-a785-a19a8b1c932b | -4.07698 | -46.68682 | 2024-12-04 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 12b80e0f-d8e0-325e-8c77-5f67ba76cead | -1.83683 | -52.31589 | 2024-12-04 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5af23f68-bcea-36f9-92d5-e0db36cbee2b | -2.78917 | -51.66459 | 2024-12-04 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 146d9a45-1fe6-3b8f-8e95-5b110b9cfbbc | -2.8169 | -53.0598 | 2024-12-04 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 8e84a5ab-f06d-3a2c-b846-69c40f2aa845 | -4.7556 | -45.69857 | 2024-12-04 00:54:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2a1f2f6d-5d2a-3927-9cab-9fcb923f52b7 | -2.67992 | -46.1296 | 2024-12-04 00:54:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a34eae8b-1110-3807-8d8e-bf39552a61f5 | -1.48294 | -53.80461 | 2024-12-04 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |


[Clique aqui para ver as próximas entradas](README12.md)
