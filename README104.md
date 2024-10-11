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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e05374a8-994c-3b94-a23e-00d205cd8f6c | -1.11362 | -54.0601 | 2024-10-11 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ecdf308-6ff7-3e09-82f9-eea498e5e7bd | -3.12193 | -53.73947 | 2024-10-11 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddbec8fc-cf52-37b1-a584-6ebe6a9150a2 | -3.11664 | -53.73428 | 2024-10-11 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4c30f32-22bb-33a1-93be-f59cc1cf5a26 | -3.57654 | -54.53427 | 2024-10-11 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 950be7de-3886-34dd-968b-135c3e4f4674 | -3.57598 | -54.53814 | 2024-10-11 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ec297a3-0099-3704-bcbd-f9e61a8cc986 | -3.33987 | -54.61644 | 2024-10-11 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27c0be6c-f968-3b09-9ad0-630469667ccd | -3.33932 | -54.62014 | 2024-10-11 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f29ec8d6-4451-3a87-ada2-1f97f4de64bf | -3.2621 | -54.18044 | 2024-10-11 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c751bdf9-f2d6-3d86-a02f-533edf34d557 | -3.26158 | -54.1822 | 2024-10-11 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7016ea8-9606-3cd3-8ba5-f334579a3a42 | -3.25576 | -54.18155 | 2024-10-11 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7575ff98-9ae9-3de3-ac2b-9471e1dc3db4 | -3.25567 | -54.18407 | 2024-10-11 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 697b6378-9a60-3641-bbd9-428ee99faa44 | -3.25511 | -54.18592 | 2024-10-11 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24d7f3ec-62ce-3082-ac04-e0a4671d0580 | -3.25505 | -54.18838 | 2024-10-11 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ddf04766-b808-3dae-bcb2-94290f01f7d9 | -3.25447 | -54.19012 | 2024-10-11 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7ac63057-a500-30ad-8bb7-f42df8774e71 | -3.25446 | -54.19247 | 2024-10-11 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4a2d87ff-862e-30cc-8709-7dda15cae09d | -3.25386 | -54.19417 | 2024-10-11 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf3d496c-f896-36c6-8956-18a568417280 | -3.24985 | -54.18338 | 2024-10-11 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db9ce67b-88e7-3c61-a4d8-3948a2164d3f | -3.2493 | -54.18519 | 2024-10-11 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27e278ba-c09d-3960-9d66-d64a39cca10d | -3.24925 | -54.18759 | 2024-10-11 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62d1890f-3472-3ecc-8cb6-d5f8df0da8a0 | -3.071 | -54.7752 | 2024-10-11 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 45dd2b20-315a-3a14-94e4-a994d04e1615 | -3.06989 | -54.77189 | 2024-10-11 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 404016c7-fd03-3a27-99c2-c89c067158bb | -3.06935 | -54.77562 | 2024-10-11 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7356f8f7-5229-3825-a1fd-b883556fbe42 | -3.04075 | -54.27247 | 2024-10-11 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 014a7cda-9d44-328d-8942-b49ed3f95a3f | -3.04016 | -54.27633 | 2024-10-11 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29d7ff45-ac20-31df-9967-1c855b20d87b | -2.97422 | -54.62082 | 2024-10-11 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efad429c-eb1b-38d7-9d0c-7b9586c347aa | -2.97369 | -54.62447 | 2024-10-11 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11262303-6118-35d8-a85d-42c45a3c1644 | -2.94305 | -54.80075 | 2024-10-11 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6329c56-652c-358c-997f-7c8fa698ab76 | -2.8039 | -54.07877 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5856137d-5116-3838-a2ba-ac0ac5ae90dd | -2.80329 | -54.0828 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53e51d03-0bb5-3788-915f-c4fb24ea725e | -2.79811 | -54.07785 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54b390ab-cb9e-3659-a0e5-006bf67d6ddd | -2.79751 | -54.0819 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cea33990-57a5-3a30-b96f-768a1987f749 | -2.79511 | -54.098 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72d979fd-9dce-3a03-be12-60171fb21a48 | -2.78993 | -54.09306 | 2024-10-11 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 839c1516-67ae-34ff-bf86-9779dd799e02 | -4.47172 | -55.09021 | 2024-10-11 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac901b42-d9bd-3018-9268-daa24045a352 | -4.47119 | -55.09386 | 2024-10-11 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 100a5592-e212-38a1-afd6-324bc09468ba | -4.44933 | -55.48083 | 2024-10-11 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44096d4e-5b23-3a0e-a857-45f6c4311683 | -4.44884 | -55.48431 | 2024-10-11 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bc8f8d8-1e8c-317e-bf6c-ae29a8c97eaa | -4.44738 | -55.48479 | 2024-10-11 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 095c146b-6474-3852-88f8-6e127d71cf2b | -4.44199 | -55.48396 | 2024-10-11 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1536b49-5d2f-32ef-bcd2-ed25d07d701c | -4.26615 | -55.15458 | 2024-10-11 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4872935c-9d05-3681-8ceb-f02f2b255a6e | -4.26565 | -55.158 | 2024-10-11 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f8c1dd3-2fba-3601-a8e1-349c256c687b | -4.2626 | -55.45036 | 2024-10-11 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9889664-3a38-3eea-b75d-78d1bca9a2b5 | -4.08806 | -54.60106 | 2024-10-11 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f50f6a6-79c0-3189-8c57-5d972d4ed2b0 | -4.08749 | -54.605 | 2024-10-11 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad4ff5b9-be01-3828-b227-8f4490d53a92 | -3.90918 | -54.16336 | 2024-10-11 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| decba4b0-9c1a-3c2d-a3e9-f1231bfca337 | -3.90828 | -54.16486 | 2024-10-11 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 675b89be-a094-365b-b2f2-20400ffa8067 | -3.90334 | -54.16245 | 2024-10-11 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 860164f0-c16b-3a61-8405-71106b6e6fb4 | -3.90274 | -54.16649 | 2024-10-11 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47cb535a-a042-3e6f-8d4d-3a789ebc9544 | -3.90244 | -54.16388 | 2024-10-11 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34c8c199-252d-3794-b271-4f1667d50586 | -5.80436 | -55.73899 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 91dc2a5f-ed72-30d2-b770-472404324c00 | -5.80389 | -55.74242 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 092e3ba3-622a-3e8e-8806-5e86196bc55e | -5.80342 | -55.74583 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd200ff9-83bd-3ab4-83ec-dbb4efdd64a0 | -5.80296 | -55.74921 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 43236011-f714-3292-a74c-e23c56f8a15b | -5.80288 | -55.73593 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 30deee60-1405-314d-9f57-ca06c4eeaca7 | -5.80238 | -55.73938 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8e29e758-10e8-3753-afa3-c456d274189b | -5.80189 | -55.7428 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a2710c9f-7eef-3417-bf42-953339dd0135 | -5.8014 | -55.74622 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f9f0e58f-d9e9-3dfc-8880-3d4bc43bcda1 | -5.80091 | -55.74959 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b9700e80-6775-3f99-a751-5736b1619d13 | -5.79894 | -55.73819 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e38f27c2-a770-3717-bd7c-180c3ebe6346 | -5.798 | -55.74511 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9021206a-aade-364e-9dff-d2359614fc15 | -7.40024 | -55.49359 | 2024-10-11 05:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96076d6a-d1c9-3ed2-b577-0ffb608280af | -7.39973 | -55.49734 | 2024-10-11 05:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96921af8-900a-3ee0-b9cf-78190d6ffb68 | -7.39461 | -55.49277 | 2024-10-11 05:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dd9458a-413a-3d82-b491-fb6e679c51e1 | -6.87581 | -55.09893 | 2024-10-11 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f45d38e4-70a2-3056-9e65-42d2e4cafe33 | -6.86168 | -55.07083 | 2024-10-11 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7483bea5-fb51-3f7f-846c-2bd07dc44136 | -6.86112 | -55.07475 | 2024-10-11 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33cb913c-108c-34ad-bcc4-6e35fa08baab | -6.64918 | -54.9454 | 2024-10-11 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62ba6f96-f106-3ddf-b867-b479f3303123 | -6.64341 | -54.94455 | 2024-10-11 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57fcbaf4-ba6a-34bd-ace1-834151500675 | -2.06147 | -55.2154 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f71b2e9e-9c81-30a5-a7b1-01a9a0a42d1c | -2.05616 | -55.21458 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fb93705-6dd9-3be2-87bd-1728d291ac09 | -1.75553 | -55.32954 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87ceb6b9-3079-33da-a5e2-8280572655a7 | -1.75505 | -55.33273 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9293b7ce-71d3-3d39-af40-12c31610c60a | -1.52873 | -55.41362 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90a7f4f7-4402-3d03-8ab7-11a8b76900e5 | -1.52826 | -55.41672 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c328d01b-edbb-3f79-8eb1-8dbcdff44cbc | -1.52778 | -55.41984 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28f7bd23-3f6c-3e80-83c8-7a2dc5b55f21 | -1.5273 | -55.42293 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 842202d5-091c-3eba-85d2-273c61e35596 | -1.52683 | -55.426 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d702570-14b4-34c5-8be7-a22123f80e6b | -1.52355 | -55.41273 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b7f0ca3-216a-3241-8eb1-38aa0b5e25c9 | -1.52307 | -55.41586 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bc59e57-8580-3959-b283-713ee17673a0 | -1.52259 | -55.41901 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a3a4890-bb87-3b79-b6f7-ce247f35004e | -1.52211 | -55.42213 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6268668-6371-385c-87d3-6b417cbafa7c | -1.52165 | -55.42519 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba50f3b7-675c-3cd2-9ef4-da5ae162fe5f | -1.51836 | -55.41189 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 897b6949-be5a-3aef-aa29-9bc0b5c35fc7 | -1.51788 | -55.41504 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be3eba6e-f7d4-3976-a464-d2a8fc74eb00 | -1.5174 | -55.41819 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d46dceb-2b64-3be9-bfdf-b3d858c51d55 | -1.50008 | -55.9339 | 2024-10-11 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e12e6401-970b-3ae8-a8ce-cc804eaee628 | -1.49979 | -55.93454 | 2024-10-11 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92f7a358-12f4-3aac-a93f-6c369680a192 | -1.47401 | -54.96907 | 2024-10-11 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2ccb32c-d6d9-327b-a0ed-34f4eb652800 | -1.4735 | -54.97242 | 2024-10-11 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce1b93ea-1234-3e3b-913c-db65181543b1 | -1.34291 | -55.47124 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 281db106-daa3-3854-81f2-b742ca87227b | -1.34244 | -55.47423 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff9e4e62-cfb7-30b3-a979-4690522a041d | -1.34197 | -55.47723 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 829108cc-4d00-3f17-8599-7cf30679cddb | -1.25428 | -55.70548 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d393a13-f772-343c-bf2a-ae6b65131b82 | -1.25384 | -55.70838 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18e9acfd-bd4e-3739-8531-b16d33fdc855 | -1.25057 | -55.6958 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf498a5a-aaf5-324e-a803-fca98fbd7c86 | -1.2501 | -55.69887 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d68c225a-61ae-3698-9378-2bcfe9e9e37f | -1.24964 | -55.7019 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9777cd9-1881-322b-9dcb-5848346f5c30 | -1.21073 | -55.86207 | 2024-10-11 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 908a58e8-9f30-3236-b3d7-aa7c7bfea41e | -3.60352 | -55.45098 | 2024-10-11 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1ec80f36-cf9c-3c37-b5b4-925a504f6044 | -3.60302 | -55.45429 | 2024-10-11 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README105.md)
