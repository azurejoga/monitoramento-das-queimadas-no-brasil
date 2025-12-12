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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18056748-d1ff-393e-98c0-e90a079dcf74 | -19.86566 | -46.56052 | 2025-12-12 04:04:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4dbb354-c17b-3fd7-99ff-f507b80a1b9b | -23.5029 | -45.93858 | 2025-12-12 04:04:00 | NPP-375D | SALESÓPOLIS | SÃO PAULO | Brasil | 3545001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ba34e404-5b04-3521-8a86-d2f640a9cda4 | -23.4285 | -46.40971 | 2025-12-12 04:04:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 26022a9a-ab09-3045-86d3-040780711f44 | -20.96013 | -48.76884 | 2025-12-12 04:04:00 | NPP-375D | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9bf9b04b-8630-3d97-be89-8f1c12da9b8f | -21.33299 | -44.9497 | 2025-12-12 04:04:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 5c9a6afc-6cd9-3028-b447-6d12c983b689 | -22.12688 | -43.25902 | 2025-12-12 04:04:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e8616df1-df5a-3cf1-8577-fe090d325081 | -22.68441 | -46.88166 | 2025-12-12 04:04:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 17c135fe-d833-3b80-8f3a-4f162b496fd4 | -20.53705 | -41.82888 | 2025-12-12 04:04:00 | NPP-375D | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b577f425-7e21-39c0-8b1b-6174e566be10 | -23.4702 | -46.28619 | 2025-12-12 04:04:00 | NPP-375D | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 95dc25a2-4cbf-31cc-add8-ec635f7163dd | -19.30349 | -46.0915 | 2025-12-12 04:04:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54390a5c-2a2d-33e4-a533-72c9d145431b | -20.54038 | -41.82948 | 2025-12-12 04:04:00 | NPP-375D | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 10db6986-62a2-379d-841e-ba2aa001daef | -21.65603 | -42.45384 | 2025-12-12 04:04:00 | NPP-375D | ESTRELA DALVA | MINAS GERAIS | Brasil | 3124609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9a7f611b-abd4-37fd-baaa-a686063fd941 | -21.31902 | -49.17775 | 2025-12-12 04:04:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 50e4273e-1b6d-378d-839a-39f24852978e | -22.67448 | -43.47924 | 2025-12-12 04:04:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 72321560-de25-35df-9c8b-33aa2b241f50 | -2.4183 | -51.9278 | 2025-12-12 04:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 554c2b2b-4b6c-377f-8c64-ef4f52ce240a | -8.0324 | -43.1022 | 2025-12-12 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 0fdc0a88-34df-3065-9c3b-0af36c565999 | -2.4367 | -51.9274 | 2025-12-12 04:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 8c00b72f-7eda-3843-b1f7-a434f3643f51 | -2.4923 | -51.8027 | 2025-12-12 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 33ed9fd6-314f-301a-9833-1a1a9033e8e3 | -2.4183 | -51.9484 | 2025-12-12 04:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 691e3562-8dfa-3e09-adde-e6558b1c2fad | -2.4367 | -51.948 | 2025-12-12 04:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| d42b195c-32ab-3487-87c7-635f5468da9d | -14.9134 | -58.1263 | 2025-12-12 04:20:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 05764aee-7e5f-3ce0-b8b1-7412fa6b961b | -14.8941 | -58.1282 | 2025-12-12 04:20:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 8a71ebe0-6d20-36b8-91c1-01831379dcf6 | -2.4367 | -51.948 | 2025-12-12 04:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 773b0b09-4fc2-3750-a760-ef6e18865855 | -2.4183 | -51.9484 | 2025-12-12 04:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 702cf4aa-8075-3cc3-8a60-44373d41a57f | -2.4183 | -51.9278 | 2025-12-12 04:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| ff2a3ba7-7ca3-339a-9f2b-095f2371e1d4 | -2.4367 | -51.9274 | 2025-12-12 04:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 5db1ab76-537c-3d86-9726-cef87f54cc6e | -3.30973 | -42.53777 | 2025-12-12 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2aeb98ff-cfa8-3e7b-a574-a207cbe24df1 | -3.2721 | -45.70512 | 2025-12-12 04:21:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d65eadc-ed45-33f8-bf19-b0135b62db9b | -2.22627 | -45.40154 | 2025-12-12 04:21:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47cfadea-c0ee-32b6-9802-5dee621724be | -2.11864 | -45.35166 | 2025-12-12 04:21:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10444076-f614-3ba1-bbc1-f3dba005e808 | -7.47325 | -35.31049 | 2025-12-12 04:21:00 | NOAA-20 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 239dee68-c8c4-369e-8ca1-4ea45d7910e3 | -2.32929 | -46.28149 | 2025-12-12 04:21:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77a29072-20a1-3e10-ad05-b5e877e903fc | -3.69305 | -52.05919 | 2025-12-12 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 619a155f-c10d-3dea-9d64-d03d24093433 | -1.7975 | -45.76267 | 2025-12-12 04:21:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b70ede3-dd90-3995-aec1-c7ff01031bbc | -1.31564 | -46.5309 | 2025-12-12 04:21:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f2b27603-47d8-341e-9241-2cfecbd38335 | -3.95559 | -41.52712 | 2025-12-12 04:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fc56ab5a-e5c3-3261-a965-bbf13fac1b22 | -3.35307 | -46.86049 | 2025-12-12 04:21:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6a9d614-c7d2-3b5d-86d3-3638a2d4e997 | -1.34052 | -54.61036 | 2025-12-12 04:21:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3beef2e-0253-3389-a278-4cf4b9431e3a | -4.49461 | -43.42966 | 2025-12-12 04:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac1f218d-f2fe-346b-8c43-64ef33e81818 | -2.29467 | -45.59065 | 2025-12-12 04:21:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8c9be775-2714-38c8-bc2b-8d6808563241 | -3.95268 | -41.52262 | 2025-12-12 04:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f3bcd1db-fe09-3847-8e1c-1506e44ea639 | -3.85552 | -45.30307 | 2025-12-12 04:21:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09f9bd8b-6043-3b59-8cb5-70fbfb0045bd | -2.42964 | -51.92789 | 2025-12-12 04:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 934fe406-b620-3632-85a2-374f041b7a7a | -1.03184 | -53.73903 | 2025-12-12 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 664ee329-498e-3e84-bcbe-599a5fb05acb | -6.11846 | -41.28695 | 2025-12-12 04:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5d9a5f74-e1cc-3d32-abcc-6d270a26900c | -2.65435 | -51.64317 | 2025-12-12 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4a61924-6f58-30f6-ba57-e11c6220ebfa | -4.39068 | -46.67093 | 2025-12-12 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b1ed5293-8258-3ff8-8c0f-7e96af0327c7 | -3.38453 | -47.18904 | 2025-12-12 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42710087-4ed2-319e-a003-1a00caf01e6b | -9.40491 | -35.64923 | 2025-12-12 04:21:00 | NOAA-20 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5e7f7ca8-1015-3382-88f0-9616261f5c1d | -2.21952 | -45.40047 | 2025-12-12 04:21:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad823bf8-c7e6-369b-883d-b9c7cc0ada2f | -4.76659 | -43.60091 | 2025-12-12 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cea0b0e-6b27-307b-a072-e83c09ff41b2 | -4.43388 | -38.97145 | 2025-12-12 04:21:00 | NOAA-20 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 39411625-d6df-3a23-9152-03e974c42bd7 | -2.97097 | -52.72161 | 2025-12-12 04:21:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62af45a3-a1e1-342a-941f-b087533b8f2a | -3.69065 | -51.99771 | 2025-12-12 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79541b51-9f26-3716-bcd9-0cf18c73145c | -1.02362 | -53.74389 | 2025-12-12 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2be5696e-4d8a-39cb-8b30-b91f78e71d42 | -7.64382 | -48.03525 | 2025-12-12 04:21:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25222513-431b-3640-b107-06f2919b6395 | -2.48418 | -45.89912 | 2025-12-12 04:21:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e51b704a-dbab-3a97-a7dc-6058712d5732 | -3.82056 | -47.7672 | 2025-12-12 04:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| beb18dbe-b2e3-3a70-90fc-bb9dbd7cd23b | -2.22851 | -45.4093 | 2025-12-12 04:21:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd31aca5-f9f0-3a67-9266-01d6718a42f7 | -3.42335 | -42.28274 | 2025-12-12 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a157e43-c712-3329-b48e-624c6f01c68d | -2.48242 | -47.77443 | 2025-12-12 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0084bdf0-4319-3d5b-a491-f898f07cea08 | -2.65917 | -51.644 | 2025-12-12 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 383942c5-8419-3355-b73b-fef552e9d795 | -4.7331 | -43.07503 | 2025-12-12 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3348088e-406d-3137-869b-d83443c58f56 | -3.01107 | -52.83508 | 2025-12-12 04:21:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31f345cd-d6cd-30c9-8858-3b424d351fd0 | -4.33138 | -44.33706 | 2025-12-12 04:21:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1784ea41-8941-32e5-9ec5-6c639d475f44 | -2.43367 | -51.93427 | 2025-12-12 04:21:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 52278805-d546-3474-9b6d-9d6b8c0d857e | -8.04225 | -43.1033 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a4c5e4a1-a3df-3077-b0c0-bdd2b3f60bc0 | -4.68977 | -43.24312 | 2025-12-12 04:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e49c69f6-f7d1-38cd-b53d-b9e46272614a | -2.49478 | -51.80809 | 2025-12-12 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d85e7475-8612-346c-88b6-b48276db4f23 | -2.93651 | -53.02737 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a555700-9370-369b-8b38-9be2ad48b884 | -2.89908 | -51.94378 | 2025-12-12 04:21:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 336876ba-97a3-3459-a5eb-5438d729b20b | -3.95225 | -41.526 | 2025-12-12 04:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cfca8a92-aa66-3bd6-a2fa-5e105667c8ee | -1.03004 | -53.74033 | 2025-12-12 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0e78b5e2-a287-3584-aaa8-c0464e52702a | -4.514 | -40.85061 | 2025-12-12 04:21:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 44b7248d-e97c-3cab-833f-b83f88c9f193 | -1.29045 | -53.16521 | 2025-12-12 04:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68dc861f-74bb-3496-8512-db2779ba7ad8 | -2.23787 | -46.51837 | 2025-12-12 04:21:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e7912ad-91bc-3e5f-9950-1d4246194c9e | -3.12821 | -54.1807 | 2025-12-12 04:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db8138e8-29e6-3061-a200-53c1986843d4 | -2.29525 | -45.587 | 2025-12-12 04:21:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 73a047f9-daf7-318b-8035-56d08825610e | -3.23179 | -42.07179 | 2025-12-12 04:21:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e5b6925-cdec-3ad5-9e30-6ece7e3f84fe | -3.91392 | -46.05951 | 2025-12-12 04:21:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f03f9fd-4ed5-3e29-ba8b-1f6c8b97d895 | -8.03136 | -43.10549 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ac105b0e-4d52-3441-98e5-fec7ff265321 | -2.2257 | -45.40514 | 2025-12-12 04:21:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c8776ff-da0a-3afd-bf40-ae78ecd16c9e | -4.10499 | -46.48626 | 2025-12-12 04:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3680a96-f8e0-33e8-a880-316989b07b03 | -8.02792 | -43.10496 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2ff98eb6-16ca-3ad1-bb4b-c356f0213e70 | -5.06461 | -44.47038 | 2025-12-12 04:21:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3eedb74d-1793-3187-8d79-50d5733657f0 | -8.04511 | -43.1076 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 52aa6dde-14bf-3efe-b2ab-f10750648b77 | -3.51097 | -45.9256 | 2025-12-12 04:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d5b7e9c-bf8b-3ff1-83dc-0c641c461563 | -2.79816 | -47.34586 | 2025-12-12 04:21:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b95b203-bd77-3d0c-bc8c-e8a7678d0f8c | -4.42973 | -38.97092 | 2025-12-12 04:21:00 | NOAA-20 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 68713f27-f844-3e07-a52d-6bf1496bdd2f | -2.63974 | -45.75988 | 2025-12-12 04:21:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1e6b0f2-af16-3891-8ab7-932ecb7d0dd6 | -8.0285 | -43.1012 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0f995e41-6793-37aa-ba3e-7cc93ad75f40 | -8.03537 | -43.10225 | 2025-12-12 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 705fca16-8459-3f80-935a-939e3ff300df | -4.72974 | -43.07451 | 2025-12-12 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2473d19-71ea-3726-90d6-476b63e18d8c | -3.33077 | -45.03307 | 2025-12-12 04:21:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05f424ea-d5c9-307c-910c-6dc55ad455d1 | -4.3914 | -43.63173 | 2025-12-12 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f79524f-f148-31ca-a05d-122a30ea8d89 | -2.88419 | -53.01535 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c179b4eb-7244-3ff3-8863-f42fb85aa10c | -2.88526 | -53.00898 | 2025-12-12 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8cd6f388-af2d-38b1-82aa-0eb40f4bc72d | -3.95621 | -41.52317 | 2025-12-12 04:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 15f7c98c-decd-3b36-9fdf-d0e308bd79f2 | -2.2229 | -45.401 | 2025-12-12 04:21:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 281910e8-2154-3bfb-92ed-b2ff0d92a264 | -8.20307 | -43.56351 | 2025-12-12 04:21:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README15.md)
