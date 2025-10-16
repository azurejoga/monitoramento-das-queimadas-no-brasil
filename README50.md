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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c40dc04f-5cfb-3bef-bd0e-f7cb79555c10 | -5.67045 | -45.10802 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8d4a6274-2f55-3903-898c-8d1fab4cb3b9 | -5.30126 | -43.85892 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14b0e5a4-20e0-388e-bfe8-14c4b982c636 | -4.39676 | -43.38524 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f10b9d4f-8e7b-317b-93ec-a7b17cacb61a | -6.83036 | -44.64686 | 2025-10-16 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe236049-5dd2-3556-96ec-5dd4c5b57b4b | -7.96952 | -44.13387 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d2d5c2a-0efc-3ae8-8380-d9d6b466d32c | -6.27402 | -52.62643 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1c33e28-14f2-3bb3-8756-8c5c888ff727 | -6.18955 | -44.10483 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2eae7c61-78de-37c5-b6e8-04e5b7efaad8 | -5.47109 | -44.64119 | 2025-10-16 04:38:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95a12ef3-d59f-3fee-ad49-e099ca3a71eb | -5.45001 | -41.00346 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 431f6b8e-167e-3ee2-9bc1-1bc9d6cd692f | -8.2506 | -44.13626 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7ec6b36-add8-39d3-83dc-6a461a70f418 | -6.58136 | -42.97482 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33712117-60f3-38dc-9faf-410fd84b3de5 | -6.1933 | -52.73417 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57c414ab-d3b9-36c0-955a-7adcca1cfa20 | -7.178 | -46.95285 | 2025-10-16 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43e6571c-b30f-31cc-943a-85af2f3e8bd5 | -8.19151 | -43.32273 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 274cda3d-8545-3ddd-b4c6-e6c71290069c | -6.5172 | -42.19308 | 2025-10-16 04:38:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ae16eaad-61da-3bb2-90d3-33c48de48407 | -1.89465 | -51.01216 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f27cd60b-d1ba-3c19-9790-7225ffb7e84f | -3.56091 | -50.12446 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4d0e62f-f44d-3fbe-810f-21543f199adf | -5.44457 | -41.00577 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0970df68-f8a3-39fd-a9cf-ac548fd42096 | -2.70542 | -49.8558 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be514055-03cd-3e03-a961-42c08bb01c5e | -3.84829 | -41.56291 | 2025-10-16 04:38:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 332eb124-4574-3312-af3d-7f06775e60c3 | -4.64854 | -50.9286 | 2025-10-16 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f0064aa6-9e66-374b-a39a-e81159ac44e7 | -6.894 | -43.05399 | 2025-10-16 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c32ff20-acdb-3159-9ce5-7433a49c43a5 | -4.3944 | -43.45865 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 857f3e06-ed5f-3645-aa98-5cf0437de280 | -6.03691 | -41.9179 | 2025-10-16 04:38:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b1034633-18fc-3dcf-bc21-8dac68833e6b | -7.22316 | -45.16615 | 2025-10-16 04:38:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11737565-1301-3165-962c-eb91e371801c | -5.87325 | -42.77018 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b2d0aa58-6839-3fe7-8433-247c596511a8 | -6.4435 | -43.37785 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 334de68a-f69d-3b03-b057-a45bc1daa60a | -4.36077 | -45.52815 | 2025-10-16 04:38:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d34151cf-2c0d-3716-b606-8639d95ca7fa | -4.45635 | -50.36381 | 2025-10-16 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b93636d6-1d91-3368-bc19-2ab1f22c83eb | -2.64275 | -48.05972 | 2025-10-16 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 93eee9da-e052-35b8-b29f-ccce450beae2 | -4.89168 | -48.58917 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18e67471-d9a1-3a8d-8649-6c091bc01c64 | -6.45827 | -44.58136 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f09b2d66-4931-330d-bfc8-22fa8128f6b0 | -4.39506 | -43.39673 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| cc7c95af-611f-3cb6-9e55-ae4d134862a5 | -7.57701 | -42.68645 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 23a79f54-b30c-344e-a6e7-029a926a1689 | -7.57957 | -42.70127 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 75f55e7c-0db0-35dc-9329-c8b4dcaeb047 | -7.26012 | -41.74621 | 2025-10-16 04:38:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 7a824887-8b27-3146-ab4d-5e6e5673a3ec | -8.23139 | -43.32878 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 05dc4974-e457-34bb-9d76-4232e490633e | -4.77106 | -48.66513 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e1a7135-641f-3113-8e05-e69c4dbfb1d1 | -5.03149 | -49.49842 | 2025-10-16 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 510d9542-5cec-3c58-9a88-5e1234514042 | -7.48403 | -42.74967 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| bcf1cafe-e861-38f6-b514-6608ae467b76 | -4.36699 | -43.38463 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d6d676c-c6c5-39f7-bc06-0dc2461fcded | -6.15997 | -40.90588 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 8dc142ff-5c87-36af-be5f-e80c602b99b8 | -1.49197 | -55.44417 | 2025-10-16 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04397299-73a1-30d9-b736-7362d164178e | -2.70674 | -49.8639 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0cde8f1e-5b0a-33c7-b349-273febde08e2 | -4.28342 | -48.58182 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5d7ae98-f03e-351e-aa92-6ebb0e6ef157 | -6.56983 | -42.96669 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 52ad71b6-3733-3197-b04d-2377ec29711f | -3.2101 | -54.96325 | 2025-10-16 04:38:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68ac758e-f8ab-326f-9c57-5b935a026fc8 | -7.61527 | -46.47409 | 2025-10-16 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee2ee322-10d0-3b9f-baa3-36bec0f3a152 | -6.58724 | -44.37078 | 2025-10-16 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 263fd923-1467-30bf-9604-fa722eb32698 | -8.28892 | -43.39723 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d9d6ae58-147e-3aff-a3f0-a0ec96db1171 | -4.92827 | -41.55491 | 2025-10-16 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6002704a-d33f-338b-b856-e83224962fba | -4.67545 | -44.08484 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99eb0de7-b7e2-3bd9-bab0-7969853b90e6 | -7.10671 | -42.03719 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fc17c780-945d-35ae-b5cd-0baa9f877c2b | -6.77575 | -42.84684 | 2025-10-16 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3a9e4886-fff8-34c4-8d9a-470f6da77670 | -4.11334 | -51.09005 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f505732-e42a-3d42-b646-5246a168ff05 | -4.62111 | -49.55722 | 2025-10-16 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b93e585-8a14-3c9a-8d7b-95c8bdef2ee5 | -6.19291 | -44.10823 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ebb8cc21-00d4-3a5f-a963-d3e2913a2a68 | -5.99741 | -44.2225 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da6f384e-cb49-32bb-917b-2d47710728d0 | -4.36534 | -43.39598 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6090b1e9-6b3b-3ed0-824a-a36a20ad8162 | -7.3975 | -39.68778 | 2025-10-16 04:38:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 27.6 |
| c861a47a-9b67-3e1e-a1c8-27dc733161f3 | -1.98984 | -56.91945 | 2025-10-16 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da9fc94c-3bb6-36c1-bf87-ab646020d7cb | -2.21617 | -49.50204 | 2025-10-16 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 760823c8-e266-36c2-9b30-6232ba242b4f | -6.18155 | -44.30367 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 020c07e4-14df-3e91-b892-49598557f6fc | -3.16052 | -51.81736 | 2025-10-16 04:38:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24d2e527-c2f7-355a-913c-6032c0e9e618 | -0.82046 | -48.6758 | 2025-10-16 04:38:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b63f9268-d772-37fd-a101-12c861457f11 | -5.24805 | -41.02342 | 2025-10-16 04:38:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c1833041-fac7-3385-b030-7dd007205899 | -4.28012 | -48.58131 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbbb7f2f-55b3-358f-90af-a4d0a5926a02 | -5.35102 | -43.74968 | 2025-10-16 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ded8a65d-6d3f-3b9c-9c93-89ebb2cd720d | -2.70842 | -49.85328 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85f0f27d-93b3-32f3-b101-833255f10698 | -7.58016 | -42.69788 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5f019d65-f044-377e-bddd-509185e5e8ee | -5.83006 | -42.34576 | 2025-10-16 04:38:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 709368fc-fb3b-3310-ad6c-b875c8e8de2e | -3.67924 | -47.63344 | 2025-10-16 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93e86c10-5729-34e9-85a1-54a45720f9eb | -3.23228 | -43.45915 | 2025-10-16 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a1d897ba-a9e2-3367-a7e8-ea9641e8b6eb | -8.24688 | -44.03629 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e7b5aa3d-1a46-303d-a973-1dd7f2f50d42 | -6.13294 | -44.29063 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 743f3392-e5b7-34df-9da6-bdb03efd804b | -8.06805 | -45.42297 | 2025-10-16 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4c35f43d-f382-3f96-bf09-8c334478a43d | -5.83528 | -42.34189 | 2025-10-16 04:38:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6b5e27d7-50b2-3c75-ac39-cccf5760e3dd | -3.07786 | -49.49784 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb5e210a-1f9a-3aa4-80a5-276b96c6b100 | -6.45351 | -44.03239 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba915f98-cf93-3cbf-868b-d664f3ab2406 | -6.77959 | -42.85206 | 2025-10-16 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d2433fbe-77a3-3391-8797-9dd2d9a5bd41 | -4.37311 | -43.40109 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7ec3b1a4-6293-3314-ad7d-739e5dc53116 | -6.63116 | -46.83398 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8fb840f-2fb4-3bf1-b995-724289c068db | -7.17046 | -42.50862 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3a0fb65d-2364-30bc-a25f-af3db7bae252 | -5.74678 | -44.98156 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de795adb-140f-3c8d-a8aa-b450f222faf7 | -4.10799 | -48.02657 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 842babd8-6c29-358e-a981-215bb1ef3cda | -7.90362 | -44.98546 | 2025-10-16 04:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0515c281-ae01-3263-9cc5-ad8c3e226b89 | -5.04765 | -45.02407 | 2025-10-16 04:38:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95954fe2-8e5c-323a-a031-9a6b739f5e9c | -7.6793 | -42.55954 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 90f0000d-729a-369f-9d97-f4e365e561c2 | -5.88095 | -42.81166 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b2bb0d50-afb2-3fe8-971f-abd16250b2fb | -5.74609 | -44.98626 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e79e104-37a4-32e3-8497-f506e49db968 | -7.47362 | -42.75763 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3dabe9c4-40a5-3caf-92b6-c06b4af87f25 | -5.10101 | -42.63928 | 2025-10-16 04:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 139686bc-99a9-3b5d-86fb-0d372c774baf | -5.8714 | -42.81505 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 60beaa2a-78f6-3d99-974d-f2ca66a08798 | -5.23155 | -43.79607 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba0ca723-7b72-3346-bf21-a0e9de3bbd55 | -6.16038 | -40.90294 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ba8ca21b-7e43-3b4d-b557-330b2599d9ef | -3.84929 | -41.58814 | 2025-10-16 04:38:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 4abfdf3c-9cd2-3952-98b1-93ada4c09e88 | -7.10881 | -44.71502 | 2025-10-16 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4871889d-9c47-3601-b4ed-99a882a055e6 | -7.03621 | -42.73722 | 2025-10-16 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 89a3e10a-5505-3f09-a84d-9fa1e26a4fb2 | -6.20501 | -45.52036 | 2025-10-16 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b04e8cbe-2291-3f3e-8ff1-00276a4cfa19 | -5.87203 | -42.81069 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README51.md)
