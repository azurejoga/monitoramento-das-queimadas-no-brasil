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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73b5e67d-3ff4-3467-8837-16bf04c50165 | -3.82411 | -43.98486 | 2025-11-25 06:12:00 | AQUA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| debbbbff-ecc7-31b9-88d6-da0f8ca3bfa4 | -6.68584 | -43.93834 | 2025-11-25 06:12:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| a7d273f3-60c8-3d92-89a2-3a088f9a6a69 | -8.04853 | -43.14024 | 2025-11-25 06:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.5 |
| 6189057b-637d-365d-afaa-8c89ee688c12 | -7.55599 | -45.86348 | 2025-11-25 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b60c34e6-bd2d-3d46-9339-ae6c5754b686 | -2.93138 | -48.22866 | 2025-11-25 06:12:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9a805d50-b9b9-34df-b4d0-84206afa2a3a | -8.1602 | -43.17862 | 2025-11-25 06:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 9f79052d-ebf7-3f18-9d24-8e1ca66f87f3 | -3.3828 | -47.18751 | 2025-11-25 06:12:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1017e052-f3ca-3675-804b-5a7fd07bf775 | -8.05093 | -43.12262 | 2025-11-25 06:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| e34332d1-2665-30a3-96e4-de84839c803f | -2.98661 | -51.05835 | 2025-11-25 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 332d1c6a-4dc2-3301-860b-de81ca93c1b9 | -3.17379 | -48.0267 | 2025-11-25 06:12:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b68b4f6e-2567-3976-a3d5-a1a8751b24a1 | -3.20578 | -46.82383 | 2025-11-25 06:12:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 943cd478-3953-3d91-bc8e-4547aa541889 | -6.89887 | -42.83027 | 2025-11-25 06:12:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 066f92fd-40cc-3199-bd98-34dd76f0c439 | -3.96892 | -47.65782 | 2025-11-25 06:12:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 59bd3e13-9f2a-3bce-b4e5-d1bc3869815a | -3.15885 | -49.16227 | 2025-11-25 06:12:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 28608314-cfb7-3f41-a13a-1521b7215a7f | -4.8163 | -43.8268 | 2025-11-25 06:12:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d026dc04-14b7-371b-95a6-51f62d7fb933 | -3.7727 | -44.04293 | 2025-11-25 06:12:00 | AQUA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 423049a3-2ca4-3a28-9c01-6a0e1fef255e | -4.54901 | -43.28243 | 2025-11-25 06:12:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| f0a84478-63c1-3fe5-b945-eba4c1dc7fa4 | -6.67091 | -42.48383 | 2025-11-25 06:12:00 | AQUA_M-M | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| ca4c23fe-60d7-3cd5-8376-e892a3d17147 | -8.06067 | -43.14174 | 2025-11-25 06:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| c122e000-99a5-38c5-b632-c1f7bf3bf7ec | -3.6558 | -43.9765 | 2025-11-25 06:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| e920defb-3869-3e73-9b41-94fe48addb66 | -2.9294 | -48.2319 | 2025-11-25 06:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| acfd943b-0f35-33f7-92e5-525610f689ae | -8.051 | -43.1237 | 2025-11-25 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 5e92d2ef-f6c7-3124-86fd-5386350706e0 | -8.051 | -43.1237 | 2025-11-25 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 66892514-9e74-3633-91d0-99a6f8cd6457 | -3.184 | -45.1813 | 2025-11-25 06:40:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 23a1d006-d56c-3d0b-b9e4-6cbf283e2158 | -3.1839 | -45.2038 | 2025-11-25 06:40:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 29153bd2-f747-310f-a546-41d2bbaa2b0d | -8.0507 | -43.1472 | 2025-11-25 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| ed132e26-58ad-3b5c-82c9-d543f9bf4363 | -4.5562 | -43.3028 | 2025-11-25 11:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 188.0 |
| 493fc3e2-089a-3328-a4d1-543c044149a6 | -4.5375 | -43.304 | 2025-11-25 11:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 2f663d38-f98a-31e3-92b8-8155910bf953 | -4.5562 | -43.3028 | 2025-11-25 11:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 7c67b085-2e68-3968-ae50-50ce728af234 | -4.5562 | -43.3028 | 2025-11-25 11:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 4c9f909b-698c-39ff-8389-e3d924286448 | -19.2147 | -57.3483 | 2025-11-25 11:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 157.8 |
| 5b73baf5-07fe-317b-b87f-6020236b6b70 | -7.73139 | -37.6304 | 2025-11-25 11:57:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 40.0 |
| ad4ac642-a9e3-324a-995a-70579f76fb14 | -6.80657 | -44.61908 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a412c354-3743-3d34-9e26-ddfc3083a7cc | -5.84222 | -39.14429 | 2025-11-25 11:57:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 6c9e625b-017c-3f7c-a723-e3eddf33553e | -4.34508 | -43.83288 | 2025-11-25 11:57:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 421037f4-c519-3a8e-b401-7a7cce0a809e | -4.17555 | -41.61102 | 2025-11-25 11:57:00 | TERRA_M-M | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| bf55c860-b26b-3567-becb-ba32803c98b6 | -5.4166 | -38.06886 | 2025-11-25 11:57:00 | TERRA_M-M | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 38716482-78e3-386e-a3d9-dddf3fa8ebd1 | -3.7626 | -40.6205 | 2025-11-25 11:57:00 | TERRA_M-M | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 16.5 |
| fcd22fad-c993-3a37-8fbc-a151ad480ac2 | -6.41013 | -43.47015 | 2025-11-25 11:57:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1b517b75-0068-3169-811c-bf894226b174 | -7.59121 | -42.30894 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 22413d91-c70e-30f6-8e3e-0e817eb6d3d8 | -4.81764 | -43.8199 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 4967265c-89fb-3849-8d49-9edf75e4cdb9 | -8.83013 | -40.83205 | 2025-11-25 11:57:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 12.5 |
| b7e88c3c-f3a0-3554-99ac-379a2470df3b | -4.04636 | -42.51483 | 2025-11-25 11:57:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 02334dbe-cd9f-3b7c-b38f-157c5090d409 | -4.49617 | -44.257 | 2025-11-25 11:57:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6b449e0c-dcbe-3691-97b2-46c272bfafb5 | -4.56125 | -43.30145 | 2025-11-25 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ea94a214-5c11-34f5-86a5-943072f5202b | -3.69196 | -42.74142 | 2025-11-25 11:57:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| fa786bf6-3b93-38d8-95dc-31f96f8a6615 | -3.31012 | -44.41516 | 2025-11-25 11:57:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| af6bae03-fc31-3f6a-957a-c487a710e347 | -4.16534 | -41.61884 | 2025-11-25 11:57:00 | TERRA_M-M | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 12f9edb3-1aa8-34c3-b754-768a20944c80 | -3.56393 | -42.07951 | 2025-11-25 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| ded0fd1b-a2f5-3d54-b953-8f245c5eea43 | -3.79119 | -42.17464 | 2025-11-25 11:57:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 520de1ef-685b-3ef0-8b0c-72e79dd9842d | -4.34639 | -43.82381 | 2025-11-25 11:57:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| d2c5bc73-0923-349a-8b2a-ea87c75cfe3b | -7.51456 | -39.01981 | 2025-11-25 11:57:00 | TERRA_M-M | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 3196b57d-142d-34aa-bc9c-89ea70773069 | -9.32885 | -36.9626 | 2025-11-25 11:57:00 | TERRA_M-M | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 50.3 |
| 4b2d3921-1815-3f8b-9482-80221ec2cc51 | -8.21379 | -40.94107 | 2025-11-25 11:57:00 | TERRA_M-M | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 0a37b066-b6e4-38d3-8c14-dfa28ef96e5f | -3.38497 | -42.43306 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0daee374-6a6e-3167-bb24-a2dc8eead1ea | -8.96114 | -37.20394 | 2025-11-25 11:57:00 | TERRA_M-M | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 39.6 |
| f1ef24a3-b47f-3088-b774-a9b9b74eb0a1 | -4.33773 | -40.66674 | 2025-11-25 11:57:00 | TERRA_M-M | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| dd9c4a34-a0cd-3b3c-a6ba-7435434bfbf0 | -4.35533 | -43.82507 | 2025-11-25 11:57:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3274095e-5893-3dd8-aa23-cb1bb25cc462 | -4.01871 | -42.45741 | 2025-11-25 11:57:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 124.2 |
| 4950e9b3-77df-305c-b9d2-5685ceb50bf1 | -6.7694 | -37.89288 | 2025-11-25 11:57:00 | TERRA_M-M | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 24.2 |
| aa285ee7-2531-3a0a-bd43-3a223d10cc72 | -3.55637 | -42.06948 | 2025-11-25 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 84e033f6-e918-3eb8-a5f6-2915d2dc2ec7 | -4.24824 | -42.45699 | 2025-11-25 11:57:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f8c8f955-c93c-36b7-9788-ade0be6149bb | -7.57299 | -42.6288 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| a84c066e-efb1-38e6-a250-d7e20b2f1cf6 | -5.45114 | -43.26645 | 2025-11-25 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b5108522-3377-3b24-b3b4-ed16771473ec | -3.6907 | -42.75017 | 2025-11-25 11:57:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 91bc20bf-62d4-3cdf-992d-49b2c7ddeae6 | -6.35564 | -38.07468 | 2025-11-25 11:57:00 | TERRA_M-M | ALEXANDRIA | RIO GRANDE DO NORTE | Brasil | 2400505 | 24 | 33 | nan | nan | nan | Caatinga | 26.6 |
| de459299-2bb2-315c-b410-b2928bc6d222 | -9.33132 | -36.94184 | 2025-11-25 11:57:00 | TERRA_M-M | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 41.2 |
| 91a8b299-177c-34a3-9a17-537a5c7bef7a | -3.72682 | -42.16835 | 2025-11-25 11:57:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 8d227794-8c8a-3088-9329-b4b1cb8a7f18 | -7.10795 | -41.35639 | 2025-11-25 11:57:00 | TERRA_M-M | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 355c59ea-9585-38c9-b328-0ba6b40a601b | -8.96033 | -37.20973 | 2025-11-25 11:57:00 | TERRA_M-M | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 35.4 |
| e6c863b2-1cef-3ede-b750-151ae6c89150 | -3.80027 | -43.12964 | 2025-11-25 11:57:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b49b33b4-b588-35a8-96bf-aabd313fc108 | -3.91983 | -40.54448 | 2025-11-25 11:57:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| f6a283d8-3867-3d2b-a61e-60afc794b2a1 | -3.00972 | -42.20688 | 2025-11-25 11:57:00 | TERRA_M-M | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fec333a3-9269-3601-9893-84d0dd5539c9 | -3.5161 | -41.57791 | 2025-11-25 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| f4cf1f3d-9307-372b-82c5-21b92fd7c4d6 | -3.51738 | -41.56894 | 2025-11-25 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| e1821b16-1520-3953-844f-eff085e2d8fe | -7.57036 | -37.35866 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 47.9 |
| 37de9526-2ae1-3b66-b22b-1f978a8ce68a | -7.3723 | -44.22559 | 2025-11-25 11:57:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 9e264702-754f-3179-9cb5-f4f461fffcd3 | -7.46329 | -45.17858 | 2025-11-25 11:57:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 634685c3-52f4-30bb-9727-ecefba03032b | -3.77044 | -44.04171 | 2025-11-25 11:57:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 16a03446-9bb7-36ff-9240-e5f586e193e6 | -4.18776 | -43.84126 | 2025-11-25 11:57:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d6f5ee71-e062-35ab-bd43-dfe1116f48b0 | -9.62108 | -36.10615 | 2025-11-25 11:57:00 | TERRA_M-M | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 67.9 |
| e0545171-31ce-3e74-bf64-f18aeed82895 | -4.33825 | -44.32754 | 2025-11-25 11:57:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| bcb626c8-f1f8-3f65-8ff6-bd282b2687c9 | -7.5681 | -37.35179 | 2025-11-25 11:57:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 31.4 |
| ac4d3765-4907-3b05-8f5c-35d4e4e26cbf | -7.8779 | -38.01073 | 2025-11-25 11:57:00 | TERRA_M-M | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 29.2 |
| 75a1b5dc-6a60-3f4c-a9c0-6262fdbf0b7b | -5.90839 | -44.00937 | 2025-11-25 11:57:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4c643c0b-7c1e-3a26-bb9b-ebb5d6f723fd | -4.5537 | -43.2914 | 2025-11-25 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| df447e91-3b97-38ec-8650-0ea7ada7681c | -5.07286 | -40.68519 | 2025-11-25 11:57:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 453d4ceb-b1f5-3883-86cc-ad82db186555 | -3.52629 | -41.57016 | 2025-11-25 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| b4c443ca-a0cd-37b0-ae4c-aa1ff0b9ad66 | -3.72808 | -42.15956 | 2025-11-25 11:57:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 6778d82b-7fea-341f-bfda-ce2034f2b637 | -3.35824 | -42.16391 | 2025-11-25 11:57:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a389a9ee-9169-31e0-be06-2706be351b25 | -3.00846 | -42.21563 | 2025-11-25 11:57:00 | TERRA_M-M | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b2b64805-1ca1-3196-ba2a-6bb9743f6286 | -5.12833 | -43.02369 | 2025-11-25 11:57:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b92f287a-dee3-3c67-850a-8a8dc46c82c3 | -3.48297 | -41.29084 | 2025-11-25 11:57:00 | TERRA_M-M | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 613c2090-f9e3-3382-8414-25245055465a | -2.90299 | -44.1697 | 2025-11-25 11:57:00 | TERRA_M-M | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d604839c-52f5-34fc-a05a-d0322788248e | -9.62776 | -36.08678 | 2025-11-25 11:57:00 | TERRA_M-M | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 94.2 |
| 2592d629-3253-39b8-90fa-4efc1e44ecaf | -3.35647 | -40.2312 | 2025-11-25 11:57:00 | TERRA_M-M | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 2f6aee0c-f3e2-3694-b762-e4e5d2b13fa8 | -3.73058 | -42.32994 | 2025-11-25 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| d830c8eb-c084-3fb7-b7ec-3ce4466d20df | -3.64514 | -42.67501 | 2025-11-25 11:57:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f28d0a33-fcf6-31c8-8947-766c88730132 | -2.8716 | -44.00155 | 2025-11-25 11:57:00 | TERRA_M-M | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| af0c5403-01e8-32ba-a94e-460653c6f0aa | -4.33633 | -40.67654 | 2025-11-25 11:57:00 | TERRA_M-M | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |


[Clique aqui para ver as próximas entradas](README18.md)
