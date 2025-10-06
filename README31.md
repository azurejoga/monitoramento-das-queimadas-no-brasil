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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e65f3114-feaa-3eb2-94ba-238627909423 | -8.53816 | -47.21914 | 2025-10-06 04:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77bc391b-49c2-3886-905b-90d7b386a74b | -4.7682 | -46.60303 | 2025-10-06 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 141c888e-e139-3537-b6fe-54ae81214ea2 | -6.25219 | -43.26147 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c239c4e4-f542-3f23-b01f-2aa8c12f1c4d | -7.36706 | -45.23446 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32dc746f-215e-33cb-893d-50c860f5ae34 | -2.24766 | -47.86904 | 2025-10-06 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9dd863b6-a1e5-3648-9a4c-77488ce1eafb | -5.64573 | -50.3127 | 2025-10-06 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f31b1449-b21d-3e63-9df3-22630686cd3c | -5.8937 | -38.48905 | 2025-10-06 04:25:00 | NOAA-21 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6114b846-0774-3b8a-9298-cffbe0386a26 | -5.73642 | -45.50686 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f78718c-5806-3822-aafe-781e01c59714 | -7.02387 | -42.78522 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| b4c9a8cf-a939-325e-a6d9-d9d3af21fb5e | -5.46204 | -42.79116 | 2025-10-06 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 04262ee6-5e43-3cb0-875a-a8ecd555e514 | -8.61522 | -46.29024 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2a30d6e2-c4dd-3687-b2e5-89a8ac8ea1cd | -8.87296 | -46.79686 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf2f5754-1b1b-3ee9-a5a3-42afaebdc878 | -5.26229 | -46.49409 | 2025-10-06 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38ee75aa-cb46-3971-8051-8931be66e030 | -7.68737 | -42.59066 | 2025-10-06 04:25:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 8a750a36-f49b-3cd9-8c0e-fb9b1222d2ff | -8.55376 | -47.67983 | 2025-10-06 04:25:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27796b73-0c63-35c9-aafe-d2fa256c8e48 | -4.64344 | -43.18951 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c6dc40e-a432-36e6-8075-bfd2eb1d48f5 | -2.85626 | -54.09504 | 2025-10-06 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 617c337f-b1e4-3700-a37b-14c5fdd60255 | -5.76721 | -45.80898 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca5e0f60-0f0e-33ed-b404-db05bea3922c | -3.53985 | -52.80482 | 2025-10-06 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42bf54dd-a390-3393-a5f0-3d3d2ed7b53f | -7.18693 | -41.69001 | 2025-10-06 04:25:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5b599631-98b0-38e5-be3e-9d8b59431d38 | -6.25316 | -44.26481 | 2025-10-06 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf11b09a-0484-300a-b334-a61947cc437c | -8.36339 | -48.9036 | 2025-10-06 04:25:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c37e2b7-2578-3515-8bb2-34cef26d59f1 | -5.46371 | -42.80449 | 2025-10-06 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| fd9bb98b-ab11-3cce-8ccd-3b26d212f896 | -6.7613 | -44.5905 | 2025-10-06 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e8907e3-9ecb-3a26-beef-1122d8ca1303 | -5.48413 | -43.2611 | 2025-10-06 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9b0f79d1-42ff-321c-8c53-ef30eb6edcbd | -7.21893 | -45.90615 | 2025-10-06 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a355687-52ae-3718-956a-13b5fe80c385 | -9.32026 | -45.99902 | 2025-10-06 04:25:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e88433cc-982e-3cab-8087-3fca62a925c1 | -6.11957 | -48.08523 | 2025-10-06 04:25:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c94ee5a0-0497-32d9-9467-257ca62c2740 | -5.46566 | -42.79172 | 2025-10-06 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 405162e5-fdd1-3f50-901a-0af258ecc88a | -7.31073 | -47.31831 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a996ba3e-164d-3904-9681-c8fc0084f8a6 | -8.51647 | -46.38157 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95892844-64a6-303f-b258-8e5b7f40ce3c | -6.72496 | -42.15738 | 2025-10-06 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f56d7a30-3259-356b-b072-da2ec75e057f | -8.17955 | -44.23705 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df8d2fc1-7d17-34ac-bf5e-48f398b2e511 | -7.82139 | -47.38254 | 2025-10-06 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3f8fd49-f619-38ef-8d6c-a44ebf7f9acc | -7.25448 | -44.90047 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1a9641e-a18f-378e-8309-ece9db4a791a | -4.91338 | -48.02458 | 2025-10-06 04:25:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd21d2fb-0b31-3dcf-a153-a73f5ede5f81 | -7.41818 | -46.52924 | 2025-10-06 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad5e6ca5-769a-3699-a9d1-47406ae3d86f | -6.36508 | -41.63279 | 2025-10-06 04:25:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a292d5eb-4540-3707-abff-76b3ffaaafc7 | -8.16964 | -43.33809 | 2025-10-06 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 18796263-49a0-3250-95b5-d0e2b12fda71 | -4.23012 | -46.75706 | 2025-10-06 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24a559bf-36fe-370e-84d4-51bca9129908 | -3.53917 | -54.07293 | 2025-10-06 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| becf6a4c-e16a-3b81-9be5-b888b4c98e2e | -6.87466 | -47.23437 | 2025-10-06 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3fcbe488-13c3-37c6-a4a5-cf8cfddd662e | -5.76922 | -45.7528 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73474169-7986-367f-bd97-e9e06c56852a | -3.78409 | -51.37251 | 2025-10-06 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ac5716a-27f7-3b7f-953b-9a68344ca6b2 | -8.52752 | -46.39753 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3aa2452-da71-3e25-83a3-0882a0cdd6d6 | -5.78128 | -45.74051 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75bce4c0-f22c-3256-87a8-1ea330b50ad4 | -4.64405 | -43.18555 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4baf7f63-459f-3e4a-9f53-d82541814efe | -6.75174 | -46.41272 | 2025-10-06 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72195d8a-48de-38d8-9f00-d27f3ce59f49 | -5.36672 | -45.95737 | 2025-10-06 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3dc9363-bf06-3d2c-9dcc-088f3aaabd07 | -5.88987 | -38.48794 | 2025-10-06 04:25:00 | NOAA-21 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b2fc4d26-1160-3578-baf8-24c681ce4948 | -8.2693 | -43.83462 | 2025-10-06 04:25:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 36164046-87d6-3b57-89d2-6ae547c283bb | -5.69428 | -44.83535 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6a7467a-e5ef-3146-985a-6949ae167797 | -8.68202 | -49.46615 | 2025-10-06 04:25:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0206de86-b58e-361c-9b9a-50861d487cde | -9.31863 | -45.78774 | 2025-10-06 04:25:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11d36995-6f9d-361f-bd56-0657e29fa48a | -3.83778 | -51.74224 | 2025-10-06 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cba0bbf-c20b-36ff-9f4a-8d772a7b6078 | -8.54313 | -50.15886 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55dabef5-01e4-39ee-8b5d-c36ec680e3d0 | -6.75885 | -42.24081 | 2025-10-06 04:25:00 | NOAA-21 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 71a8a6dd-478b-3e22-a372-3417c2df0627 | -6.79671 | -46.03841 | 2025-10-06 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 924c8908-64ce-36f5-bac6-d1739302356e | -6.33316 | -55.18764 | 2025-10-06 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46cb44a3-4569-39cc-96d8-41c678abaa54 | -7.40255 | -47.27619 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae4ebc78-23c1-351d-aed4-39574b98c79b | -6.74911 | -44.00022 | 2025-10-06 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 707ce785-b1d9-3ae4-8cae-0271766e7e89 | -8.91255 | -46.58657 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8d039f7-b471-3264-8db3-11602d9b9a1a | -5.69258 | -44.82415 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ec5a04d7-6b4a-3102-ba14-61d8286a675f | -6.57457 | -49.86744 | 2025-10-06 04:25:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b08142c-502f-3ada-905e-8e665d74939e | -7.68359 | -42.5901 | 2025-10-06 04:25:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 74b320ee-3e26-3334-9576-33d2c033040e | -5.8341 | -45.8405 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 534e729b-23c0-34cc-a041-efe383b2e2df | -7.87701 | -44.12936 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f13557c-d4f4-3c5e-bba8-be807088880c | -4.22956 | -46.76055 | 2025-10-06 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b302374f-13c7-34b9-af9b-a1412bf94bb5 | -8.61077 | -46.27532 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a5e36b24-74d4-3944-b717-ba0ad94b2622 | -7.2217 | -45.91014 | 2025-10-06 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3e5520a-777a-3091-a4e9-2800c330204a | -5.334 | -47.28778 | 2025-10-06 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 22.8 |
| fe40ce9a-2e7d-35f1-bc89-9d527135d6c2 | -4.96518 | -42.71341 | 2025-10-06 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be9296e1-c6e9-3920-a19e-dbf34b0c3d2f | -5.26613 | -46.49115 | 2025-10-06 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01f902ee-8167-3388-a395-7f735c506558 | -8.51417 | -46.37002 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f65d1ce4-a60f-3717-8d27-0e582a8a24a2 | -8.61967 | -46.30519 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11fed240-7774-308d-8aa0-2fcaf4e80edb | -6.72565 | -42.15279 | 2025-10-06 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 42e6b90a-3116-321a-8d09-9998aa8e7ae6 | -6.11911 | -46.32286 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ee28cc3-8b0f-395a-8aa9-c41d7707b5f1 | -7.61583 | -45.47288 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bc63673-9f04-3b7e-9fa3-d3c86b67b638 | -3.62078 | -51.4986 | 2025-10-06 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90a6a2ca-10d4-3ae6-9ffb-56fd555c242b | -7.01518 | -42.79289 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9f22fde4-1a81-34a5-95a6-c95d04b2c0c5 | -8.63559 | -46.31479 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7ae7631d-b75a-3c46-b4e7-510cfb9c5e9b | -3.83527 | -52.23439 | 2025-10-06 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a93f2b7-fd8f-349f-b26b-9d2daa589ed9 | -4.19202 | -46.4593 | 2025-10-06 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9839282f-bb7c-306c-9e65-3258675e4b36 | -7.01454 | -42.79729 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5d075d6a-b308-365f-9444-b688a608a85a | -7.70612 | -46.253 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cad32813-de43-3966-92b2-6e62c52c6678 | -2.99039 | -48.0812 | 2025-10-06 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c95fcf77-2836-30c4-8450-4deb3d0cad24 | -5.33066 | -47.28724 | 2025-10-06 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 22.8 |
| f7ce2e92-3d92-37e1-b4a0-00c1cf4a103b | -6.64401 | -41.97274 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1a367849-b272-309d-b157-e72221bb7b59 | -8.67501 | -49.465 | 2025-10-06 04:25:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 243ca22f-e3ee-3489-af5c-7253d415ecd5 | -6.64329 | -41.97758 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a367b75e-cc9f-399e-b93a-be8ccfdf0f39 | -9.31137 | -45.99038 | 2025-10-06 04:25:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 070942e5-f572-34ee-a210-71361aa8e621 | -7.01647 | -42.7841 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 64f9f9b0-5f5c-3985-a5b9-8d548112cd60 | -6.80256 | -46.15243 | 2025-10-06 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e98807df-3888-37f9-95ac-b777c0ce64db | -8.18572 | -44.12573 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2c66858-b8b6-3007-8e56-eec2993dfc63 | -9.01707 | -47.35714 | 2025-10-06 04:25:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b565baf3-bbf8-3740-a333-fd197aee32e8 | -9.29983 | -45.66405 | 2025-10-06 04:25:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66cf2403-c38f-307e-8b5f-d47f797c7595 | -7.45587 | -43.05344 | 2025-10-06 04:25:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 704feb7b-8081-3e87-a391-6779c3fba042 | -6.36493 | -44.65453 | 2025-10-06 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 294b0e89-174e-34f8-8fdc-e63c216486e8 | -7.77529 | -44.11736 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73ada3c5-a4d6-3fa4-832e-70611d423331 | -8.51869 | -46.38902 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README32.md)
