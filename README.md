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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b63cb2b1-2141-3c1a-811d-57dcb184c806 | -4.3013 | -48.07 | 2025-06-09 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 9e8bf1c5-8c49-36c0-88ef-0970db3995b5 | -10.2864 | -46.9881 | 2025-06-09 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 91ce2a7f-372f-38ba-9023-3885a66ec55f | -3.35113 | -39.12762 | 2025-06-09 00:01:00 | TERRA_M-M | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1644b1d2-20d9-3223-a9a2-0b4f62a77c24 | -3.09176 | -40.06398 | 2025-06-09 00:01:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 991777ef-7234-3e75-8067-c05d9db538a1 | -4.30367 | -48.07907 | 2025-06-09 00:01:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ef6580cc-09af-3e1e-85ff-22672563c36e | -4.29827 | -48.07436 | 2025-06-09 00:01:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 64d4b697-a349-3624-a6d6-c448a5530732 | -5.63235 | -43.72634 | 2025-06-09 00:01:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c5eb5695-1d9b-3a05-bf77-fa18350ff263 | -4.49192 | -43.77808 | 2025-06-09 00:01:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| d81c2a7d-191d-3bbc-9f7d-450becc4189d | -6.00919 | -45.76616 | 2025-06-09 00:01:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 14735b22-da73-398c-86d4-9bc0c7c8b1e6 | -4.2994 | -48.084099 | 2025-06-09 00:08:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cec7e00-c9a2-39e7-80e4-14f37b514527 | -9.5045 | -40.321201 | 2025-06-09 00:08:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ab4f4bbe-5a7a-371e-a342-95ce98caae6c | -9.4072 | -48.435501 | 2025-06-09 00:08:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7eb90e5-f766-3a42-b3cf-0f2e8cb74710 | -10.2781 | -46.997002 | 2025-06-09 00:08:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cb11be3e-7eb1-3cb9-b6ad-0d69f89d52d3 | -7.0096 | -44.599499 | 2025-06-09 00:08:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cff23714-7ce6-3f16-9759-3a1f88c2f89b | -6.0075 | -45.772499 | 2025-06-09 00:08:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3290c6e3-2fbb-3df2-be03-92587cc70820 | -7.0246 | -44.574501 | 2025-06-09 00:08:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 915da139-ed30-3fb0-9a2c-6af7f0994312 | -7.2753 | -44.222099 | 2025-06-09 00:08:00 | METOP-C | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 34ecd02d-467b-352c-8b40-c6becd173987 | -10.2816 | -47.014 | 2025-06-09 00:08:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| febb2b77-8851-36e4-a0f3-17c811541042 | -7.0141 | -44.620399 | 2025-06-09 00:08:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f40adc8-8d05-3735-9742-c5d90a0f81b3 | -4.4865 | -43.7691 | 2025-06-09 00:08:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d68f3322-1394-379c-ac5f-74751ee4e4b3 | -7.0194 | -44.597401 | 2025-06-09 00:08:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f7b7389-b366-35aa-b650-8293ccdd1201 | -4.4885 | -43.777699 | 2025-06-09 00:08:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5405a8f3-e878-3dea-a8cf-a5abd7aa099f | -14.9353 | -42.299198 | 2025-06-09 00:08:00 | METOP-C | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d36c8c65-e1a4-3d85-97cf-5a35014faf23 | -7.0119 | -44.610001 | 2025-06-09 00:08:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8403fdd3-e116-3e4d-9749-82311092b19f | -14.24 | -45.482399 | 2025-06-09 00:08:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e489e7b5-23aa-3448-b163-6cb6597ad872 | -7.0021 | -44.612099 | 2025-06-09 00:08:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 554a2f02-82f6-3ed7-9ded-c5c397a212ea | -7.0148 | -44.576599 | 2025-06-09 00:08:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30e9099b-0bb7-3e10-bbd2-022288a00b66 | -7.6506 | -46.099098 | 2025-06-09 00:08:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc6d04db-d92e-3d23-90c2-86346a49706f | -7.0217 | -44.607899 | 2025-06-09 00:08:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd3769a5-60c6-37ac-881a-d3b46c09e2e5 | -14.243 | -45.497799 | 2025-06-09 00:08:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0ae92ae6-c76c-38ec-8f25-c139ae014a2f | -14.9333 | -42.289299 | 2025-06-09 00:08:00 | METOP-C | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f64bccba-4b43-3ae0-a215-43a091385af9 | -7.0043 | -44.622501 | 2025-06-09 00:08:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c83029f-9d34-3378-af91-1790a0f3b925 | -13.5602 | -44.203999 | 2025-06-09 00:08:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 082e8692-59cb-31e5-bc29-0e62ceb5e6b2 | -10.2913 | -47.012001 | 2025-06-09 00:08:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bddd2f8-5b14-37ac-a776-40e057ff6205 | -10.2878 | -46.994999 | 2025-06-09 00:08:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef1211ac-2dda-3044-82ae-b32b89b925eb | -4.2958 | -48.067902 | 2025-06-09 00:08:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4e4b3a5-d74f-387d-90d8-41abf7a66d1e | -7.0171 | -44.587002 | 2025-06-09 00:08:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd0bdaa2-6f0b-3f77-ade8-3d8b5f52a40d | -10.6462 | -44.4963 | 2025-06-09 00:08:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4a0fdcdf-865e-38fc-aa54-a4a93658f4a2 | -10.6437 | -44.4846 | 2025-06-09 00:08:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5744a12c-2f81-3334-b316-7a0d2fa25f4f | -4.3013 | -48.07 | 2025-06-09 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 1ad2c927-9a40-3e86-a850-3f4701f01150 | -4.3013 | -48.07 | 2025-06-09 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 2c829954-fd01-3a2d-8ca7-b472e51b30ba | -4.3013 | -48.07 | 2025-06-09 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 4095e9cf-604b-372b-b48f-884dde5aa040 | -4.3013 | -48.07 | 2025-06-09 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 40469e97-d315-33d2-98a5-34170ec25a95 | -10.8521 | -53.774502 | 2025-06-09 00:55:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 512bb953-593a-3bdf-88af-a8744d443d51 | -10.2814 | -46.9991 | 2025-06-09 00:55:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17d61d4f-ece4-313a-8683-4baa956651c3 | -14.2621 | -52.466499 | 2025-06-09 00:55:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6ebc812f-35e5-305f-b2a5-2a9535c7f79b | -10.3731 | -57.503399 | 2025-06-09 00:55:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0458f43-8965-3949-a46b-41925f127b39 | -10.8403 | -53.7682 | 2025-06-09 00:55:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b40e58dd-97f3-39b7-9b8f-1a067e761db7 | -12.5315 | -58.339298 | 2025-06-09 00:55:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a3749385-e2d9-39e9-9390-850fc56c0067 | -12.3522 | -57.422401 | 2025-06-09 00:55:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3c303e5-3d72-3344-a80b-324f3f86c40d | -10.3715 | -57.496399 | 2025-06-09 00:55:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aeacc503-6a58-3b66-914d-a377ef86aacb | -12.1626 | -57.7309 | 2025-06-09 00:55:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6fb74062-65e8-3475-9e30-bce80e1de271 | -9.4045 | -48.433399 | 2025-06-09 00:55:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 735afd3e-df08-3451-80ac-7feac498a9fd | -12.3769 | -57.3946 | 2025-06-09 00:55:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a970de76-b5df-3d77-b695-a07f37b2959d | -10.8542 | -53.783199 | 2025-06-09 00:55:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dbf7c852-4d77-30d9-a8fc-36624aa6310a | -11.1254 | -54.636799 | 2025-06-09 00:55:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85f6897f-aa3d-32c1-a003-300c1d95b545 | -12.1611 | -57.723801 | 2025-06-09 00:55:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22756226-1a2c-3c9f-a44d-d4665e9423b9 | -10.8501 | -53.7659 | 2025-06-09 00:55:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2140f79f-994f-3146-8d09-73b6cf2e809f | -12.3785 | -57.4016 | 2025-06-09 00:55:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f76772d-ff08-33a7-8630-108ea17ea752 | -10.8423 | -53.776798 | 2025-06-09 00:55:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f060a52-11d3-3644-a74f-a49e77132e35 | -11.7868 | -54.7747 | 2025-06-09 00:55:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 318942c0-ffbb-324e-bba5-df711dd36c40 | -10.37 | -57.489498 | 2025-06-09 00:55:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37ebf897-3f5e-3b3b-9b60-943bc6c4b7fb | -9.4964 | -40.3088 | 2025-06-09 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.5 |
| bc30e09e-747f-3e0b-bd66-40c37ebc5497 | -10.85445 | -53.79123 | 2025-06-09 01:37:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| c033301b-88e0-3c8a-b593-b2bd9127d4e2 | -12.37368 | -57.41175 | 2025-06-09 01:37:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8f1a13b5-2455-3d82-87f0-4dce0c92d7ed | -12.35401 | -57.43008 | 2025-06-09 01:37:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 502825fb-8edc-3d3f-876b-2dc5e5ac0d04 | -12.53059 | -58.34652 | 2025-06-09 01:37:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| dad61f69-0e9c-3d4f-83d8-b8bde821bf67 | -12.15784 | -57.72738 | 2025-06-09 01:37:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| eef8621d-7948-3035-851c-bfb391935235 | -10.85226 | -53.78641 | 2025-06-09 01:37:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 841a0712-4b3e-36bd-ad33-9692e584bba6 | -10.3747 | -57.5 | 2025-06-09 01:44:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 873da71f-6735-3f28-b8e3-827335180ee3 | -10.8594 | -53.782799 | 2025-06-09 01:44:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83022cc3-d5fa-3623-bc36-7716a4e7627f | -10.2864 | -46.9881 | 2025-06-09 01:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| fc4eb944-9a83-3fe4-add0-620df2f0dd40 | -10.286 | -47.0104 | 2025-06-09 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 3dcffee6-bcba-345b-8a72-bb53491d7336 | -10.2864 | -46.9881 | 2025-06-09 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| a7246bdb-4392-3c23-a840-bf1a63cfc93b | -10.2864 | -46.9881 | 2025-06-09 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 4015a0b4-644a-3fe5-924d-1dcb301d1c88 | -10.2864 | -46.9881 | 2025-06-09 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| d131139b-312c-3651-b6a5-d074ab75f24a | -10.286 | -47.0104 | 2025-06-09 02:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| bc4c1256-09a3-3b05-b7e0-2fbbb42efe6e | -10.2864 | -46.9881 | 2025-06-09 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 5635b470-6db4-3070-a396-cad72935ed7d | -10.286 | -47.0104 | 2025-06-09 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 2be0d40c-968a-341b-a95b-40e6b13657bb | -10.2864 | -46.9881 | 2025-06-09 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 41.4 |
| de3152f5-fd91-3782-b1b8-8568ae1179d8 | -10.2674 | -46.9903 | 2025-06-09 02:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 37.9 |
| b3bac8d3-fee1-3ab5-8424-5315d517a855 | -10.2674 | -46.9903 | 2025-06-09 03:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 06032f32-27f5-3180-a60b-5bf149cac1c9 | -10.2864 | -46.9881 | 2025-06-09 03:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| f3d65219-bea6-34d7-a181-a6d88f407cf4 | -7.47538 | -34.84418 | 2025-06-09 03:15:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fe58683e-25bf-3f89-8eee-fe7f12b1896d | -8.07401 | -34.97659 | 2025-06-09 03:17:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c0ae6cd1-4dc0-39cc-b60b-28309d161bc7 | -8.07517 | -34.97612 | 2025-06-09 03:17:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b8c6f3b0-8b4e-31cd-bb92-674692a0a264 | -17.77854 | -42.8119 | 2025-06-09 03:19:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2e174dba-cfaa-30f4-ac90-4ccddd165978 | -16.68229 | -43.88646 | 2025-06-09 03:19:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e2cc732-f809-3c7e-862f-7f7cd7931594 | -17.77446 | -42.80841 | 2025-06-09 03:19:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9d3fa32-7055-310f-bdd6-c7fa208d8500 | -17.7803 | -42.80968 | 2025-06-09 03:19:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 51266f43-d24f-39ed-9f34-0d671495cca7 | -13.55567 | -44.19575 | 2025-06-09 03:19:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f8bfbd53-0479-3db5-91ae-68c61ed96086 | -17.77955 | -42.80734 | 2025-06-09 03:19:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7a2d6873-6507-37f7-8d59-0f588ed90a6d | -14.93583 | -42.28728 | 2025-06-09 03:19:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9447daf6-3d78-302e-9d7d-c620efde6743 | -14.93482 | -42.29216 | 2025-06-09 03:19:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7cce616c-a1f6-3982-bd4e-5b045aa431eb | -14.93755 | -42.29085 | 2025-06-09 03:19:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6189551b-d0ac-364a-b171-6a303c83d844 | -18.0579 | -39.9172 | 2025-06-09 03:19:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0039a12c-5305-3a32-afd0-92fcf11dd714 | -4.05287 | -38.20851 | 2025-06-09 03:42:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d4a4e9f0-8a05-39da-a64e-93f49d7260f6 | -4.05357 | -38.20415 | 2025-06-09 03:42:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 088c7bcd-0c18-3ac7-ab40-83f98a6f2c15 | -10.26771 | -46.99484 | 2025-06-09 03:45:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f10d1d24-5114-3b2f-82e3-657b48308df2 | -7.27731 | -44.21969 | 2025-06-09 03:45:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README2.md)
