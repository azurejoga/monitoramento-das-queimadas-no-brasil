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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0d1c165-2650-3375-bbec-30e6e42d03bb | -8.36136 | -47.54023 | 2024-10-04 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a644515d-8e52-3fc0-adb7-621771e45f07 | -10.61389 | -48.05125 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 936f0d37-0f6a-3166-b9eb-fe68e20c3b8c | -10.61333 | -48.05545 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 03a0f0e0-bbae-3e5f-949e-d35e878457bc | -10.60984 | -48.04655 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0c63ece0-2b80-34b5-8f38-6e7b955df8f8 | -10.60865 | -48.05539 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f650166a-ab97-3dee-8f63-2da9715e3da1 | -10.59995 | -48.05047 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a9103a22-3570-3bd4-bfeb-617d51790713 | -10.59934 | -48.12449 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| abd138a3-ac57-3432-b6f6-42d6c7043dad | -10.59933 | -48.05513 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5cf76de9-bef2-38ee-80ee-f6128208e48c | -10.5987 | -48.12921 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 75059ba0-9b50-30ec-ab1d-5b7403277429 | -10.59532 | -48.05005 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d0414a9f-ac79-3b70-8443-24e604de7ad4 | -10.59414 | -48.1285 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bb594ed-0def-3e56-bdff-ff11b2565ddd | -10.5935 | -48.13322 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bc45811-1907-3c8c-a748-d64cfc56465b | -10.59286 | -48.13794 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 505e2006-a73b-3d20-9d46-509479ca654c | -10.59021 | -48.12307 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 510efed0-94b8-3fe7-b411-88937e0c321a | -10.58958 | -48.12776 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffac1bf1-301a-34a6-88d2-785a39a827a9 | -10.58894 | -48.13249 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db2eb142-4c3d-3bc3-9576-c728c1354220 | -10.58751 | -48.10843 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9663595f-a1f2-359c-882a-b77589b4ef62 | -10.55442 | -48.0776 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2a8da64d-2256-3667-9162-453a255790a5 | -10.52306 | -48.03346 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41941871-213e-353b-9d9d-c6ae298e0f7c | -10.4944 | -48.17553 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3f961cf4-12f1-3c2f-b479-976eea40ddb1 | -10.49378 | -48.18006 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d9152471-e50e-3942-a894-28109d8214d0 | -10.48979 | -48.17533 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 3edc0e7e-3fa3-3746-9196-254d257f7f4e | -10.48919 | -48.17973 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fff131eb-3458-3fe6-a2c2-61e6c0901a6f | -10.48858 | -48.1842 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d730a1ec-3fb6-3f10-8bce-ddb7d701dc63 | -10.48798 | -48.18867 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ec2b689-904f-33f3-9e21-7fdb1981387c | -10.48575 | -48.17086 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| ef7ecd1d-169c-3c24-a9eb-8e5e2a000936 | -10.48516 | -48.17524 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 4cb9de06-e9f4-3716-980d-2a3edd5cd683 | -10.48457 | -48.17961 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| bfec8563-8992-3608-b1a3-14e2847046ad | -10.48342 | -48.18812 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30a5b218-8dae-3a9b-8a40-14b005fafb92 | -10.48112 | -48.17081 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 882b2f69-d343-34a2-8564-4292d4092193 | -10.48052 | -48.17526 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37c18441-2f7b-313a-b757-e356142d6808 | -10.47652 | -48.1706 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| db9efe1b-48af-325d-9f41-ca5923697c01 | -10.4759 | -48.17516 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8fb682b-12f6-3668-b1a8-6c6044c75688 | -10.47129 | -48.17497 | 2024-10-04 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29859156-7ffc-30e3-aac5-893ec191c10c | -10.41101 | -48.16771 | 2024-10-04 04:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3bd083db-fa48-3047-824a-5e97c51f9412 | -10.28318 | -47.69032 | 2024-10-04 04:55:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a32a904b-4abb-3587-8501-389eb3a55067 | -10.2812 | -47.68749 | 2024-10-04 04:55:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bf399ae6-7bca-30ca-8ded-6a9d87345f90 | -10.2785 | -47.68954 | 2024-10-04 04:55:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2bf0221f-a03a-3d51-bc31-9d874b599000 | -10.27589 | -47.6914 | 2024-10-04 04:55:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b8ca3bb2-7014-3fe8-a515-8035e132e9f7 | -10.27384 | -47.68865 | 2024-10-04 04:55:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5671d1d5-6508-3e7b-b214-9b0632e110be | -10.11878 | -48.82901 | 2024-10-04 04:55:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa807703-a4e2-37de-b261-bb54584092d1 | -10.11681 | -48.82954 | 2024-10-04 04:55:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7857187f-1e46-3f12-8107-7a67dbfdb23c | -10.1131 | -48.82454 | 2024-10-04 04:55:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2799c949-ce8d-3381-a599-55b11c43ca7d | -10.11251 | -48.82875 | 2024-10-04 04:55:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1075a4b9-de73-364a-8699-1d57c7c4c363 | -10.10759 | -48.83232 | 2024-10-04 04:55:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 579bbb34-79fb-3834-a5e8-cccd2730815f | -10.10327 | -48.83172 | 2024-10-04 04:55:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 52ce3380-d91f-3e2a-b3ce-055c6d3bae2d | -3.695 | -47.61932 | 2024-10-04 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8eabf64e-d0e5-35c7-94f6-ab8331479469 | -3.48941 | -48.91005 | 2024-10-04 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b083bb22-6002-3cc6-81ab-dfbbef83766b | -3.46394 | -47.66003 | 2024-10-04 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de634048-1da9-315a-9871-96bf88263383 | -3.46332 | -47.66409 | 2024-10-04 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f718c213-104f-3f99-9ada-4edc38bc9a55 | -3.40959 | -47.58735 | 2024-10-04 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e109ed0-b09a-3803-a78a-5cbd23767230 | -3.40901 | -47.59134 | 2024-10-04 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75256d27-73b0-3f37-99b1-6d2836b27877 | -4.27573 | -48.06492 | 2024-10-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47cb4d74-5b24-3ae4-8c70-60f8a5425446 | -4.27515 | -48.06874 | 2024-10-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 548eba98-d87d-3059-9454-55d32ff65256 | -4.19632 | -48.22625 | 2024-10-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2144bb0e-ec2a-367c-91a2-195b3469b849 | -4.19578 | -48.22996 | 2024-10-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1222012-432f-3974-8fb6-1ec683723a01 | -4.19468 | -48.23735 | 2024-10-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d53f49d-b993-36ba-8ae3-0936372453bc | -4.19166 | -48.22921 | 2024-10-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcfafe48-4826-3289-aa51-6a2553b1fee0 | -4.17714 | -47.88753 | 2024-10-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49637cd4-211c-3041-b02f-b21825c39e3a | -4.17656 | -47.89141 | 2024-10-04 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca608706-1d63-30e0-b30d-f45d2c01af7b | -4.14601 | -48.39841 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 252b11ba-8cf9-3441-84db-edbc74090b95 | -4.14575 | -48.39853 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67992226-d8dd-3594-9382-548677ecc8bc | -4.09516 | -48.48608 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9738804-d223-3138-adba-f07145525632 | -4.09164 | -48.48191 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c904eefe-e9d5-309a-9152-0e074c953391 | -4.09111 | -48.48544 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 6458c70c-b413-3cf9-aa72-b8a877dd573e | -4.09058 | -48.48896 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 68f19500-aca0-35fb-bbe2-f477c4666104 | -4.08921 | -48.4706 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c9ff4ee-a144-3577-8c17-c64af0adb448 | -4.08867 | -48.47414 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea2b612a-00a5-301f-8ac5-f300284aed51 | -4.08814 | -48.47768 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2eb30768-3eec-3ba1-ab63-56e1dea9fcf7 | -4.0876 | -48.48124 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 08d95995-401b-3b11-8c05-2796549d9fad | -4.08706 | -48.48479 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 67e24b39-bd30-3d52-b3b8-cf4b1bd578aa | -4.08653 | -48.48833 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| b1ed66fb-f238-39ad-b82d-8fefba014435 | -4.08547 | -48.49533 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b91cd62a-6cca-3b5a-befe-92978f4a7c52 | -4.08516 | -48.46995 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 257c2d00-f70b-3af9-964c-b1122b0eddaa | -4.08462 | -48.47349 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06a7eec8-dfa0-33e5-817e-c6eabf274519 | -4.08409 | -48.47703 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2e5d846e-0961-3dcd-9fe3-f128d5e8c542 | -4.08355 | -48.48057 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8f82173b-3c20-357d-872d-51da1bae2eed | -4.08302 | -48.48412 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e3cbde51-74fa-3b42-853b-2dcaacefc668 | -4.08248 | -48.48767 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a7b5fe46-3bff-3ff6-bbec-8841b0abe723 | -4.08195 | -48.49119 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1ba72e74-ad1a-376a-8a89-42959b44b70f | -4.08142 | -48.49471 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 110be815-4906-30fa-846b-fd35d8032592 | -4.07897 | -48.48347 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 155528ea-8937-39cd-8494-36ce00246212 | -4.07843 | -48.48703 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c940197b-bf2e-3463-9c56-43e1875f8d53 | -4.02526 | -48.91916 | 2024-10-04 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33d8069d-0c7a-3db7-a8fa-ed749bf20d76 | -4.0245 | -48.9242 | 2024-10-04 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 021d8248-c690-34a0-bd1c-7d5ddb0a8797 | -3.80507 | -47.80392 | 2024-10-04 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72cbd8b3-86f5-3e0f-9c19-2f898326ac21 | -3.79899 | -49.13871 | 2024-10-04 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7543a15b-1188-3955-a951-cdea48827ea9 | -4.88097 | -48.98598 | 2024-10-04 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6220c7dc-700c-398f-9d64-12f709da5d1e | -4.82693 | -48.54393 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76c5ef91-b606-3cc1-9da0-403233631e9e | -4.8264 | -48.54751 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4968f43-e2ea-3a46-afe3-e4374df0edab | -4.80336 | -49.07269 | 2024-10-04 04:55:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ae22a12-b57e-3f1f-9d17-7455dc784052 | -4.72539 | -48.84005 | 2024-10-04 04:55:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08992db9-f980-35c7-a951-59212549b805 | -4.72298 | -48.84266 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80ceef96-8ac5-343a-9103-5f7c9b960291 | -4.71556 | -48.83776 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 842da9c3-3c2e-34c5-97fb-1b89292c14fe | -4.61269 | -48.06535 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ded3a45e-c788-3288-967a-85bf95cb2fb8 | -4.57267 | -48.01681 | 2024-10-04 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b2581fda-37a9-373f-ad5e-f9fadd8babf1 | -5.79107 | -49.33028 | 2024-10-04 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98247d4a-fabc-3608-b533-ad33ef15d810 | -5.50703 | -48.8069 | 2024-10-04 04:55:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b650a3b2-ff07-39b1-958f-00c6344a9009 | -5.50651 | -48.81047 | 2024-10-04 04:55:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a8f3a7c-c13c-3a69-9f81-b9526ebf3490 | -5.50245 | -48.80987 | 2024-10-04 04:55:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README142.md)
