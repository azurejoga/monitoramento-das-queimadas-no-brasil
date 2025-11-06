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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd1aa26c-c5bc-3de8-a1fd-94e2b43f6bb5 | -10.04254 | -36.46803 | 2025-11-06 03:34:00 | NPP-375D | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e592eda8-ed4c-372f-94ae-c6473338e0ad | -7.18159 | -38.35705 | 2025-11-06 03:34:00 | NPP-375D | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 407deb19-820a-3b93-a032-e0f34ba8fd71 | -6.98998 | -39.07663 | 2025-11-06 03:34:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b3929341-e747-34ca-b32f-c5c9bba8525a | -10.06948 | -42.74222 | 2025-11-06 03:34:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8f4f5e67-5562-3d08-b7cb-4c237adebc10 | -6.97407 | -38.12224 | 2025-11-06 03:34:00 | NPP-375D | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1229bf8f-56ba-36dc-8950-710fa64b739c | -5.7545 | -40.81986 | 2025-11-06 03:34:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 26bb2baa-d0dd-3ae4-9500-64cfb3cd8688 | -7.17471 | -38.35039 | 2025-11-06 03:34:00 | NPP-375D | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3e579075-f02d-3267-a575-884db49f9a3d | -5.24729 | -44.39391 | 2025-11-06 03:34:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67166461-65a0-308f-9ba4-c98d46f8f0d4 | -6.2851 | -44.74477 | 2025-11-06 03:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce8c41fd-51e1-32b2-90e6-3483cd1e2d77 | -16.66353 | -42.2644 | 2025-11-06 03:36:00 | NPP-375D | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbd009c6-c528-3c52-b304-2f74868af203 | -16.66239 | -41.35498 | 2025-11-06 03:36:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1cb11bdd-b37e-30fc-ae9c-0f7223aaeee4 | -16.66687 | -41.35598 | 2025-11-06 03:36:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fff9a7d3-2086-3275-b193-55bf4fc088c6 | -3.9324 | -47.6962 | 2025-11-06 03:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 6e4ee8d3-38cc-3ab8-9380-44061c1021db | -6.2757 | -43.6675 | 2025-11-06 03:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 89b9b81d-b06e-3975-a458-e74615f4d148 | -4.748 | -42.6584 | 2025-11-06 03:40:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 5a87d243-e81b-3970-bac6-39682be6f1f9 | -4.7668 | -42.6572 | 2025-11-06 03:40:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| a4ce71d2-b82d-3f56-bec3-93153347b749 | 0.4466 | -60.4873 | 2025-11-06 03:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b05b0c02-8832-35bb-952c-ec2b7cc92cc1 | -3.9324 | -47.6962 | 2025-11-06 03:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 8412f6e2-70b6-32f3-b8f0-ada84d6fd6ad | 0.4466 | -60.4873 | 2025-11-06 03:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 050924df-45f6-337c-a8e1-c3a56773df91 | -3.4711 | -43.6623 | 2025-11-06 03:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 4d83a41e-abed-3f29-9ca0-3289d3db5c93 | -4.748 | -42.6584 | 2025-11-06 03:50:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 61fec609-ea29-3925-8708-87e5a97b9efa | -3.4712 | -43.6392 | 2025-11-06 03:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 4e958c71-4829-3a5b-875b-ab86f4840e3a | -6.2757 | -43.6675 | 2025-11-06 03:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| ad2aab01-53c2-3955-9215-a441b2ea193d | -4.7668 | -42.6572 | 2025-11-06 03:50:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| 6a4ce6da-1bbb-3b75-a981-2cae4df82dab | -6.2696 | -43.68642 | 2025-11-06 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c8168143-526f-31da-a6aa-e2c9094c4a39 | -5.76152 | -40.81543 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a3ad1745-ec70-33a6-9d85-16dc07528417 | -6.12276 | -41.53166 | 2025-11-06 03:53:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 59a238fd-30af-3f0e-8f63-aeb82e9286d1 | -6.26354 | -43.68149 | 2025-11-06 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bce7dc6b-36aa-355e-906a-0345fc323e92 | -4.64087 | -45.67799 | 2025-11-06 03:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4ef63c3b-8763-3dc6-abb1-30ab551050e4 | -5.59612 | -45.18616 | 2025-11-06 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba7eb7b2-3bbc-3c78-9dff-685653612bf3 | -5.85641 | -43.99617 | 2025-11-06 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a788527b-1438-3590-9c0e-15c56b000557 | -4.70519 | -46.52672 | 2025-11-06 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5702f54-1c3d-33b8-8cba-6c84509ef6a3 | -7.01479 | -40.27739 | 2025-11-06 03:53:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 29d3b05c-3244-3c70-9261-0564ba9d564f | -4.1023 | -48.02696 | 2025-11-06 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 30a9d9e0-e853-349a-b27f-4ca28e1ddbaa | -5.76374 | -40.82393 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2d5b9fcc-928b-3153-bc10-8a81c63a03d0 | -4.53945 | -46.45019 | 2025-11-06 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf61abf6-5cc4-3fd7-abe7-84264120ae96 | -6.23356 | -44.30843 | 2025-11-06 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 910d594e-2090-3378-a039-babc38e3d246 | -6.36614 | -43.75626 | 2025-11-06 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47130740-8a91-3322-b346-8102f9443905 | -5.75687 | -40.81992 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f49a4d01-e54b-3c05-b36c-a05e216efde1 | -4.97853 | -48.47734 | 2025-11-06 03:53:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9d23ac89-aba3-3c65-be62-c46c5585a0b4 | -7.17577 | -38.34965 | 2025-11-06 03:53:00 | NOAA-20 | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 37758487-09cb-3ae9-baba-e7cc8564bfcf | -7.52736 | -40.14816 | 2025-11-06 03:53:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6946e703-3672-3463-9e16-d69935c07f23 | -5.61576 | -41.08449 | 2025-11-06 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 11d35f9a-1607-3c4d-8fda-2e2403a9e47e | -4.78209 | -45.13361 | 2025-11-06 03:53:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a71901b1-a56c-33ac-b550-6f1f4e88d4a5 | -8.65767 | -36.81523 | 2025-11-06 03:53:00 | NOAA-20 | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6f84552e-d2c3-3514-831b-6077b6a5d71c | -4.64658 | -45.6738 | 2025-11-06 03:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b55eac03-ec5b-3838-805e-80fe020ea362 | -6.26292 | -43.68526 | 2025-11-06 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ee10c173-aee1-3a9d-9aae-230dbf32682b | -6.22681 | -40.44471 | 2025-11-06 03:53:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a6c57df8-7090-3ead-ad5b-fce5fb0fde8e | -4.69986 | -46.55738 | 2025-11-06 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53248369-6411-37f7-9494-10f3e7f6389a | -5.34841 | -43.50649 | 2025-11-06 03:53:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3725df03-e1ef-30bf-b8b7-ec6ed2511c4f | -6.26548 | -43.68571 | 2025-11-06 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| af3fe1cd-73ac-35c4-aacc-162c155c3f4d | -5.58538 | -43.77238 | 2025-11-06 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 306eed1e-a8e4-31d8-a099-58d3ddac9359 | -6.07074 | -43.25648 | 2025-11-06 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4a9ece44-fd57-3939-9e12-4121e11eb94a | -5.76572 | -40.81188 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b69f0ce4-5af7-368a-a00c-d8c545511d9d | -5.98116 | -44.57544 | 2025-11-06 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3069a70-76e0-3eed-a765-1af4eeffc581 | -5.20479 | -46.16863 | 2025-11-06 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a87056dc-337e-3c09-8756-09e7b58ea9ed | -5.19747 | -45.12354 | 2025-11-06 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b676255-9309-3d3a-b5fb-82c3fc2686da | -4.87251 | -47.54827 | 2025-11-06 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea97079e-83b5-338e-9bdb-5f10942cce7a | -6.12219 | -41.55785 | 2025-11-06 03:53:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 43b66165-193e-3099-9be6-a5b4e495d50b | -5.75928 | -40.80715 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cb6a98cf-3d90-342e-96ef-33d75a8877bd | -5.42618 | -40.66842 | 2025-11-06 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 280d41e9-1303-3fcb-82b9-37624afd1e71 | -5.75751 | -40.81594 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f07906c9-3939-3394-9fc5-1255a344715a | -6.28427 | -44.7327 | 2025-11-06 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc8d5913-8697-3b33-a71e-70761c145de0 | -5.20383 | -46.17417 | 2025-11-06 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f194e9d-3bca-3734-bdf8-0068ab934d9e | -4.49473 | -45.92846 | 2025-11-06 03:53:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c71175ad-c617-3a81-b2eb-0ea9afee97a2 | -6.99501 | -38.05178 | 2025-11-06 03:53:00 | NOAA-20 | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 674f0566-85f1-3d9d-85ed-b49c49319a98 | -4.7813 | -45.13838 | 2025-11-06 03:53:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1da67e7-46ae-343e-be5d-847cc2c04b15 | -7.94996 | -40.33259 | 2025-11-06 03:53:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 669db20a-4942-3cc2-b84a-397ca1373b54 | -6.69991 | -39.69131 | 2025-11-06 03:53:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f5f8edd4-2cfb-34ba-9d65-30111d28fdb9 | -5.93058 | -43.37191 | 2025-11-06 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6bc80b45-1333-3cf2-8a21-40566543a217 | -5.92118 | -44.02217 | 2025-11-06 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18430dde-1677-31b0-96d6-f4b03b2efeac | -6.03684 | -45.79514 | 2025-11-06 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75c00646-d5fa-39ef-9035-4bc4744d9de6 | -5.26873 | -44.81273 | 2025-11-06 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9fe141c-5d4f-3e46-9001-3be361306f5b | -5.37086 | -44.73867 | 2025-11-06 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0585d59-1392-3f76-a5e2-d87a70766585 | -5.57005 | -42.29582 | 2025-11-06 03:53:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 492fa6a4-d735-3fc8-91cf-801bab009949 | -5.97645 | -37.83074 | 2025-11-06 03:53:00 | NOAA-20 | UMARIZAL | RIO GRANDE DO NORTE | Brasil | 2414506 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e672243c-b4f6-3aea-a66a-3387bdc5089b | -6.28355 | -44.73697 | 2025-11-06 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8a5f2f5c-3d3f-333d-828b-d935e3448670 | -5.5278 | -46.50363 | 2025-11-06 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62458b1f-c0f9-3276-b4b6-7d1f0cfb41db | -4.96593 | -44.9347 | 2025-11-06 03:53:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea653cd8-19bc-33df-a23a-a6ac11a84f53 | -5.85575 | -44.0002 | 2025-11-06 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a977bca-c248-38df-b70a-808a2930293e | -5.75397 | -40.81547 | 2025-11-06 03:53:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f80a95fa-7cbf-32ff-8202-3a01033f35ee | -4.64566 | -45.67914 | 2025-11-06 03:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 32f7f930-7ce7-3eed-b185-e6d4a494bbde | -6.30452 | -43.78144 | 2025-11-06 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a8c6694-890a-3ebb-bdee-ba11d229cc19 | -4.74054 | -46.59825 | 2025-11-06 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c83b260-357c-3c2d-8f40-24b108523e04 | -5.9428 | -41.32549 | 2025-11-06 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0fae9bf0-ad6f-3e77-9185-df8013313d5d | -4.10307 | -48.02262 | 2025-11-06 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2fb959df-c59e-3e93-9f93-49aff7135d36 | -4.70008 | -46.52571 | 2025-11-06 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb1d4ab1-62dd-3cd6-83a0-be57619d0b87 | -4.64362 | -46.31881 | 2025-11-06 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d689e15b-a023-307e-9276-e5cf402d546c | -5.53233 | -46.50761 | 2025-11-06 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9225baab-bc85-37d8-9674-0e095715bb15 | -6.12149 | -41.56214 | 2025-11-06 03:53:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9c180f20-afdb-3d0a-b01c-755e150fbb24 | -6.28283 | -44.74127 | 2025-11-06 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5ad29b79-093a-33d6-8aa0-f6494be59852 | -5.9227 | -44.11705 | 2025-11-06 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5dc5a8f-400c-355a-97b7-5e3c187e7d7c | -4.71281 | -46.43538 | 2025-11-06 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 361b5f77-4509-3f12-b873-98ba8a2befb3 | -5.79292 | -40.80004 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| faa4e48b-028a-3782-aaa2-edf4a50f129d | -7.28012 | -39.38458 | 2025-11-06 03:53:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 95a46d3c-a8f7-327d-810c-71e70a9d4610 | -5.2395 | -44.39389 | 2025-11-06 03:53:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f14f008a-d421-3ce0-b842-01b7a65efb42 | -5.20063 | -44.00268 | 2025-11-06 03:53:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4610b1c6-d00f-328e-8835-a0d53b530d5b | -5.78863 | -40.93727 | 2025-11-06 03:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3f35e425-75fa-301c-b2a7-4b5e103f9f3a | -7.52794 | -40.14456 | 2025-11-06 03:53:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0ee1c969-ae24-369b-a5ae-021409b760a3 | -4.74003 | -46.60122 | 2025-11-06 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README13.md)
