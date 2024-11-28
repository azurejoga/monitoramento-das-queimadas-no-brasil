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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad748349-10a9-3335-9a6f-c8fcbe8eddcb | -4.65796 | -49.51862 | 2024-11-28 03:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1585f93-3d8e-3224-aaa1-35681a93eb1f | -2.84627 | -46.86326 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4e438c49-40de-3690-87ab-680fff5ac8dc | -3.96907 | -48.08162 | 2024-11-28 03:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 58bcc5b5-69ab-32a0-baa4-dc42197a0ff5 | -2.77798 | -48.58543 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d88d179-200a-3a25-ae70-d306545473dd | -6.17006 | -42.6081 | 2024-11-28 03:59:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d7f09bbd-f510-32f6-ab70-932702d2689d | -5.40014 | -43.6023 | 2024-11-28 03:59:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d294be6d-6dbf-34cb-9d78-4fa6ae7d66b7 | -4.08652 | -48.81721 | 2024-11-28 03:59:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62033366-81d1-3fdf-bd3b-cee63ebf9c9e | -6.37366 | -45.69013 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 416f5d08-6420-340e-a2cb-1d149452ae42 | -4.11188 | -48.24912 | 2024-11-28 03:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f016fa3-c265-3edc-9327-6afe4fa67fea | -4.18629 | -44.2711 | 2024-11-28 03:59:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 621ad00c-4d6f-3ac3-b398-c1da2d5a071d | -4.21128 | -50.89111 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6a2d4a1-ca2a-3134-98cd-147817439989 | -2.63804 | -46.95627 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 376dfa5f-7e59-3b46-b2aa-089acfa5a07e | -3.46593 | -43.53016 | 2024-11-28 03:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b914bcc5-1237-3a7a-9a48-b4782cc02a9f | -3.20573 | -46.59872 | 2024-11-28 03:59:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9849d45-a52f-3e22-a27f-b55c0c84dfbd | -3.37642 | -50.12124 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf9ebb9b-51ee-39c3-aa80-017008946536 | -2.84574 | -46.83525 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24d941b0-3801-366f-b5ca-2d59110cbc1f | -1.3349 | -51.94287 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c28adbc7-92b8-338c-af2a-d80488996acc | -4.30159 | -48.20869 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ce08cbe-fdbc-36e9-babd-a09f41fb6480 | -4.49568 | -46.49063 | 2024-11-28 03:59:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da3ef6cf-4f00-3000-9171-48c01d521436 | -3.35094 | -50.52512 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6398ed6-c8f8-35b5-9b26-acd25bf81cf4 | -2.31394 | -48.14779 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72b1f1c6-5364-3814-ad58-4b25c91048ee | -6.66702 | -47.87907 | 2024-11-28 03:59:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d755d4f5-863e-3861-9ecf-485102b9086e | -3.26834 | -45.37278 | 2024-11-28 03:59:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 350b3caf-0209-3a69-af2b-062d17229ff4 | -4.18689 | -40.55954 | 2024-11-28 03:59:00 | NPP-375D | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b531043f-c32f-312e-9ebf-2340c167db6b | -3.48852 | -50.08067 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7aa5026c-4865-3274-bd18-cd010bc29884 | -3.96612 | -50.18984 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 60706415-749d-3068-b426-48d17dedcaee | -3.91319 | -47.19953 | 2024-11-28 03:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a2ce5ad2-beb3-3491-a0fd-8481d25a84ae | -2.05212 | -47.12424 | 2024-11-28 03:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 885cc7ae-27c0-3d08-be0a-ec392514e9c8 | -2.85695 | -46.85935 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13d32242-18f4-3868-ad10-13c071659f53 | -4.6691 | -44.61935 | 2024-11-28 03:59:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a20b45db-0991-3e1e-b1fd-7f19dbd3ae1d | -4.35645 | -48.68602 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35436b42-d49b-3b0b-ba48-eb541addca24 | -4.214 | -50.89493 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20ce4eb8-9587-3813-bdc7-aec2be1e7b42 | -3.50801 | -45.22486 | 2024-11-28 03:59:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 812178a0-3e22-31c3-81e5-7a267fd4823f | -2.53074 | -47.33118 | 2024-11-28 03:59:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21394e8e-102a-34d0-b4ee-b0a5eb092374 | -3.67251 | -45.79367 | 2024-11-28 03:59:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c9df200-fad7-3f63-ade0-e3a9980dfd9a | -3.37568 | -50.11634 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d761f44-a5e6-392c-b927-8ab858a07c90 | -3.39005 | -50.11416 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2b79401c-f131-3abf-ac8c-b7804cfb100f | -3.32738 | -50.21925 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c3fa35f3-3dca-372c-a7a0-2841eaa51324 | -4.86131 | -42.66692 | 2024-11-28 03:59:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2805b5e2-b913-3d68-90eb-6db2f6d711e2 | -2.12729 | -46.41207 | 2024-11-28 03:59:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 530b3f2f-e803-30e7-8999-f218a4663296 | -2.90094 | -51.36833 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16b8e439-3776-3af6-9353-3e11364c7fbf | -6.83213 | -44.39651 | 2024-11-28 03:59:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b9fd3acd-d116-3c03-9530-ad3fa19f47bb | -4.30683 | -48.20961 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9b027db-5bd7-33a8-96ae-720e8ff4c0af | -2.83213 | -46.8402 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7c37438-e392-340d-b0cc-6a40111a81cf | -3.64773 | -51.39184 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b4f44682-765c-332e-93d4-a3a30364176c | -1.65952 | -52.72106 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f84a1ef-08c0-3f89-afbe-a371db771b9e | -3.08523 | -49.21717 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c92bf0e9-974b-356f-8594-ed84d3cf9b5b | -1.43903 | -52.59997 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d55a281-5d77-3416-a4e0-3c784bf4c8eb | -6.34957 | -44.81229 | 2024-11-28 03:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d94df178-54d6-3fb9-9ffb-0d845e044595 | -5.2139 | -41.28537 | 2024-11-28 03:59:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c54317d2-e958-34f8-abcf-f16eb87b6c55 | -3.6468 | -51.39726 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 30ad5c08-9067-3447-b07d-d2bbf24de0f3 | -4.13281 | -44.83342 | 2024-11-28 03:59:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed33af99-8d9b-3e6d-83d4-e06e36643c51 | -8.21095 | -40.89301 | 2024-11-28 03:59:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 59f773c2-8a7e-324a-803e-2daf029e846d | -2.7241 | -48.90131 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d7c4ac3e-bb42-3d4c-92f7-1c018676ffa8 | -1.66436 | -52.73682 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f43890cc-047a-30c2-b9d2-8afeb1c63c39 | -5.98566 | -45.35688 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e440cd0f-975d-39c5-8f97-d2e8305d5a3c | -6.99092 | -34.90822 | 2024-11-28 03:59:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ec255429-8602-38a5-ae37-278ad0d5ae65 | -6.17095 | -37.41399 | 2024-11-28 03:59:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9327fb18-2658-38d9-9c49-fa2513235724 | -6.36259 | -47.06489 | 2024-11-28 03:59:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eac9efad-f804-31d8-874b-263540c27ed3 | -3.41253 | -50.1641 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 04d7bd83-5950-3078-9c90-8bfcd89c494d | -3.38245 | -50.11288 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 75d0dd3c-bf75-38a1-bcd1-9657839a4d22 | -3.46172 | -50.53616 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6000446-8a41-377c-ac9d-e89ff47bd98f | -3.37294 | -50.82808 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6e8a6e44-1e34-3c94-8d96-f929010cbe71 | -3.22416 | -45.64513 | 2024-11-28 03:59:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1a44623-6f2c-3689-8c05-9cd831501090 | -3.46516 | -43.53499 | 2024-11-28 03:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ce0a4ef-6edd-386f-be78-2c436dfd8bcb | -3.56393 | -46.33678 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4102d686-3d58-31a3-9588-213939481de9 | -7.22078 | -39.05851 | 2024-11-28 03:59:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b3c0ec97-65bb-3982-b8c9-1aeb274fe576 | -3.18088 | -48.4325 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c8f6d4f-73c0-3447-8143-b3c66132da76 | -2.65525 | -49.51842 | 2024-11-28 03:59:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f58543d9-bf00-3698-b983-1390220b1149 | -6.77341 | -35.42449 | 2024-11-28 03:59:00 | NPP-375D | PIRPIRITUBA | PARAÍBA | Brasil | 2511806 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9618d469-a960-33b0-8ac1-4f68f9ed7e17 | -8.50426 | -43.28466 | 2024-11-28 03:59:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6431155f-3b4e-35d7-9580-880cc9af7fe5 | -2.01238 | -46.39552 | 2024-11-28 03:59:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23df7ea4-884e-3f2b-abcc-b0f4096e950e | -3.24381 | -50.77318 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cdba2410-fe7a-3fd0-b5e1-2a83e87accd5 | -3.09736 | -50.357 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e47cda1-8ae8-319c-8a72-600fc976e83d | -5.75766 | -46.26125 | 2024-11-28 03:59:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b12f6f15-6d93-3a9a-9c20-f028e5304e92 | -2.3887 | -47.16407 | 2024-11-28 03:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 23e90eb8-2dd0-3769-aec0-8c0dbe7cd5e0 | -2.52703 | -46.0806 | 2024-11-28 03:59:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5fd7b2a-4636-3bbb-9a5c-626778dbea8b | -3.09043 | -50.36062 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 210910b3-215b-387f-9166-2ab39a87cb4f | -3.78964 | -50.13038 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63d36be2-8aae-3874-8953-57436045d18b | -3.89517 | -40.92525 | 2024-11-28 03:59:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 81d3f773-64a0-35a0-9802-060801194d38 | -3.53221 | -50.19575 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 89f9ded1-2680-3189-9d37-2592dd42e5b1 | -4.31139 | -48.08682 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af75ddc7-b29b-3407-8a67-d8c062456958 | -3.4116 | -50.24285 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d72d84a6-4601-310d-a439-316d869d2a1c | -3.07371 | -48.6677 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c90d641-2e6a-36c5-8a48-e03c39465bc2 | -3.84512 | -50.09471 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15e042ed-502c-3c8a-b468-a5987f6543e5 | -4.44108 | -46.33926 | 2024-11-28 03:59:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbd7a36e-2675-32cc-8278-e87d489dd589 | -2.15449 | -48.71112 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ba8cb38-e9f6-3371-9597-5896d8fbc582 | -4.93226 | -45.42697 | 2024-11-28 03:59:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9cc75fdc-a044-3fd0-a5ed-e82684f46798 | -6.53674 | -44.65905 | 2024-11-28 03:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1255b199-fec5-3a69-8471-1900a2af63a4 | -3.4889 | -50.08685 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb7e816a-83b8-3992-ba25-a731ab555cf4 | -2.8606 | -46.85016 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 226834d2-0418-35aa-88bb-840cb972e2d4 | -3.67975 | -49.57056 | 2024-11-28 03:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77325b35-138f-39c5-a91c-9084bef9790c | -3.81581 | -47.47263 | 2024-11-28 03:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c860f49-cc42-3553-be67-b239b8fcec23 | -4.54906 | -46.30483 | 2024-11-28 03:59:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99398ae3-b221-3449-951a-1b254b4b5f86 | -5.52622 | -38.26833 | 2024-11-28 03:59:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 185ace6a-56e9-31f5-9981-7879ead45f25 | -3.69801 | -50.21939 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22e0879e-3328-3906-89ac-e360868adb04 | -2.93458 | -49.44274 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbe6028c-0553-38d8-9014-f75cf120531e | -3.93984 | -46.71782 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84bf4912-f415-3528-a43d-d527f6d184a5 | -3.96688 | -50.18542 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a352cdf8-c817-3d41-a39b-9a5a262de4b6 | -3.10261 | -50.3601 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README40.md)
