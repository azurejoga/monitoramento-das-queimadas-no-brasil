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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d605aba-137d-3c23-a957-45e26aac4012 | -1.68787 | -52.4503 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| bfe839d3-cebb-3c1c-9df8-3da43991ebad | 0.88939 | -50.95863 | 2024-11-29 00:52:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 90c91daa-ff8b-36fa-9cbe-00053f920656 | -2.42057 | -46.48697 | 2024-11-29 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 104e3860-dae5-3d48-a6ea-e19e017d218e | 1.30982 | -50.71276 | 2024-11-29 00:52:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c467051a-d109-3924-8164-05162f08bf2e | -1.61498 | -52.46045 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8cdab515-a141-3583-8f0e-180839c61301 | -2.71483 | -48.59669 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4dc45cdf-3186-32a8-8770-c67a8fa75344 | -2.58792 | -47.48522 | 2024-11-29 00:52:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 050cc377-d9da-343d-91f5-994eb9a2ba03 | -3.53312 | -45.08987 | 2024-11-29 00:52:00 | TERRA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c1e9ff3b-092d-3f29-8497-49f712cabacc | -1.03503 | -52.17246 | 2024-11-29 00:52:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b16fb17a-d16a-3633-9ad1-800d1cf34559 | -2.84044 | -46.85543 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 42585e3b-8251-3647-9edf-34e20f8c07cf | -4.33843 | -50.77069 | 2024-11-29 00:52:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2f958b11-4f3d-3154-b44e-8ff29a9565e0 | -4.86026 | -41.2604 | 2024-11-29 00:52:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 184.2 |
| 288dc836-c489-303b-8cfc-88f4a6934371 | -2.70474 | -45.95627 | 2024-11-29 00:52:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 0f07dad6-197f-3dbf-8590-cd7bc24c52e5 | -3.65184 | -50.70146 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a56e2b14-59fb-3ff3-83cd-e3c3db4419d6 | -3.93742 | -46.73116 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b16b4cbc-3a1c-3c2f-9dc6-777ed8c2e11f | -3.47841 | -49.92208 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b21136a5-3a6c-3ebb-ab7f-c7fd2fc0192b | -3.09705 | -53.81791 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 6a6bde32-21ec-34cf-8da7-7d4da0609c0f | -1.92288 | -52.89352 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 3a9c2be7-b54e-36da-94ba-e3ae6d9427b9 | -1.21063 | -53.54683 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f8477209-920b-317b-ae79-822b44910bd9 | -1.48892 | -53.81504 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 1b13f988-1ec9-3885-b23a-4ec02a1ab70e | -3.81236 | -44.04129 | 2024-11-29 00:52:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| df34bf04-2a06-38b4-aa10-03b262d8738a | -4.23899 | -45.50611 | 2024-11-29 00:52:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1d87528e-4867-3f56-a816-bcd0444db3fb | -1.21181 | -53.55602 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| a5464b40-3b48-347f-84e4-8a15df04df88 | -4.67372 | -42.38405 | 2024-11-29 00:52:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 56.0 |
| 2affb4da-40b8-324a-921e-71cb07ef4e28 | -1.44879 | -47.11663 | 2024-11-29 00:52:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 44f2c270-f055-3081-90be-6c060d7629db | -4.14589 | -48.22509 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d5234a6d-2118-3677-8202-e6d79efce97c | -4.69183 | -46.66334 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 53.7 |
| c3b10383-f2a7-3c6c-81af-e354eac0dd38 | -4.50994 | -42.06764 | 2024-11-29 00:52:00 | TERRA_M-M | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 5a35ae51-6c77-3cc3-b64f-832f0e7026e4 | -3.94523 | -46.72054 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c398ea24-734a-3b4d-96fe-39dd1fa30cac | -2.96134 | -45.2389 | 2024-11-29 00:52:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1dfff1ab-b499-3cc6-9e34-e1e2594ac23c | 0.73442 | -50.87253 | 2024-11-29 00:52:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9eca7f38-3245-376a-9755-ec7b358ecb59 | -3.9348 | -46.71251 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 877f5c91-a4df-3045-8669-ae30ef06701d | -2.96472 | -45.61248 | 2024-11-29 00:52:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d7706cd2-d90e-345e-a0cc-1242710463c4 | -3.19901 | -46.59893 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0235748e-8184-3d07-bbf5-0922c2577756 | -2.49157 | -49.04309 | 2024-11-29 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ef020477-7154-3774-9d22-31b68bf36c45 | -3.72549 | -51.0897 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ed16d4d3-f1a9-3ccf-af9f-836aef4a6354 | -2.88409 | -46.84341 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| b444a9d8-4150-36f9-bcef-2f538af9e5bd | -1.70954 | -52.7593 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 5583f6ae-b04c-3c1c-8598-6b3de11dcbbb | 0.94649 | -50.74158 | 2024-11-29 00:52:00 | TERRA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e59c0602-8082-30f5-be77-a749a38a3975 | -2.97633 | -53.28887 | 2024-11-29 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1056.3 |
| c3750e3a-ba7e-373a-8a2b-1356bc16604a | -3.34856 | -49.50992 | 2024-11-29 00:52:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0f3a1519-d11a-373c-a9c5-d84efef8f310 | -5.6387 | -46.97686 | 2024-11-29 00:52:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6283e895-3ebe-383c-8407-da894c19b5ee | -3.28235 | -48.76821 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 126ae84e-debe-3c4e-b66c-903c7e8bf076 | -3.21788 | -54.17243 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| cee864bb-ec25-31d6-9858-d169b2192c52 | -1.64661 | -52.73378 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d98d5fb1-02c6-3f95-b273-4226a9be6a49 | -3.17576 | -46.30384 | 2024-11-29 00:52:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 4c785a3d-8f99-3173-a5e5-9a59c0f91ebf | -4.06028 | -46.69175 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8613749a-46b3-35fd-8b4c-b07501c6ec95 | -3.86158 | -50.15384 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5d4afe76-cc34-3288-855a-0024173d1f79 | -2.66846 | -46.14694 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 367fd93f-87d0-3ffb-ac44-62eade99c5d9 | -1.58453 | -53.8422 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 9d0e9aa4-4e1b-3c09-9713-89b424109a04 | -2.68711 | -46.10646 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1188d4f0-34da-31a8-9407-2d48e656e6ec | -2.26511 | -46.44477 | 2024-11-29 00:52:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8cb9929a-4a98-317f-aef8-47e4387387ee | -1.21767 | -53.76004 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 4143f9e3-019e-34c8-b68d-1670006b093f | -5.62849 | -46.96909 | 2024-11-29 00:52:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1e438b37-bd19-36c5-9d50-be73c8061536 | -1.66108 | -55.05323 | 2024-11-29 00:52:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 23859e0a-620c-3c4d-8ee8-39e4d3d522ff | -3.47445 | -54.53963 | 2024-11-29 00:52:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5d7e19ff-25b1-31f7-bde6-8f8292993fc9 | -1.22312 | -53.55483 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1f537e92-5fd6-3b7a-9c55-e0800c7ba830 | -1.94322 | -52.95988 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 7483eacc-94c0-39ce-adce-0315aaf9e74b | -4.31135 | -48.09042 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 35f16f34-5e76-33f2-ac70-05742892b09a | 0.87248 | -50.81114 | 2024-11-29 00:52:00 | TERRA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 00faf553-d1ae-39a5-ae0d-deaae7321678 | -1.67875 | -45.78928 | 2024-11-29 00:52:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 531d708f-e3cb-3100-9b8a-1b62518b4b83 | -1.66159 | -52.72607 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 6d647f53-4b4e-3147-acdd-16f16cc4038a | -2.60905 | -46.85249 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4699e757-ad34-322b-b43d-2d903faf6285 | -2.61797 | -48.16089 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 73ff6b72-b18c-3d96-97be-90dd2b0e9b5d | -2.9743 | -53.27403 | 2024-11-29 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 6445f0ef-a94b-3bb0-8ed1-785cd7ae5bbd | -3.96992 | -46.96356 | 2024-11-29 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0dd4073b-0cbb-335e-b8b2-31fdcd40dbd2 | -3.80354 | -44.05626 | 2024-11-29 00:52:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1485db5f-634b-3f1f-8454-84632afe3889 | -2.64986 | -48.79201 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e5f7e6e7-1329-3568-a078-77964f7fde68 | -4.78643 | -46.94122 | 2024-11-29 00:52:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 592cc408-7606-36ec-ab87-98e600f2305d | -0.20254 | -51.46642 | 2024-11-29 00:52:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3807fadb-ff75-3f84-8c09-b0bb553df54a | -3.92217 | -53.67926 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 822b1fc6-8c17-3d2d-a333-aa205abfcf69 | -4.0694 | -46.69044 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 25e84383-8f3d-3f5e-bcf3-3ae7ce3a2573 | -3.81895 | -46.61009 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 30f1f764-aeb8-30b5-a7b0-53a55f59ba6d | -2.01714 | -46.50851 | 2024-11-29 00:52:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 07751258-f684-34cb-bddb-2e1ee61287b1 | -3.96094 | -48.07759 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 8399e15f-9879-3099-badc-9d4b2289f70e | -3.70786 | -47.13168 | 2024-11-29 00:52:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 23d19a2b-d67c-3ee2-9bcc-aaf82cf45218 | -3.4126 | -50.16777 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 36ca1a1a-4835-3a36-a366-6d385660d220 | -3.25244 | -50.61491 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 28c8f49d-420d-33a4-b502-af77c60e2cfa | -5.35633 | -48.98281 | 2024-11-29 00:52:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 21eab611-5cc4-3be7-a314-875eb498f742 | -2.85327 | -46.69246 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 781d2ff7-438a-3b60-a2e0-ca18449eada7 | -4.974 | -44.86851 | 2024-11-29 00:52:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f64095b2-a288-3774-91e8-c761a37899e1 | -2.25452 | -47.40841 | 2024-11-29 00:52:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cec2c6f6-8edd-3a73-b395-367b6f37a679 | -4.07415 | -53.94763 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6e76d654-63ab-31ab-a20e-5993f6806329 | -3.64545 | -49.39426 | 2024-11-29 00:52:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e3bcd5bc-448b-38ab-8cb8-89b37a8fb8b6 | -2.97838 | -53.30381 | 2024-11-29 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 140.9 |
| dfa94708-c7d3-3a01-b382-d27b4c322d43 | -1.0752 | -53.64632 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 034d13e1-dd7c-3b91-9266-62f38f1a254a | -1.65917 | -45.57639 | 2024-11-29 00:52:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| f3cd9463-777d-3dad-9fe0-d4a20061a536 | -4.89289 | -45.43319 | 2024-11-29 00:52:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1aca4a49-db24-325c-a803-a63b98d894ab | -3.96599 | -48.98375 | 2024-11-29 00:52:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a2ac3b74-dc7e-3405-8190-85b136c30365 | -3.26364 | -50.09631 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7acad26d-9dab-3ca1-afe0-6da431f30a55 | -3.49766 | -50.45992 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7ed652c2-f544-358e-845e-cbdb7ccfbc0f | -3.8752 | -47.07686 | 2024-11-29 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 2fd1e2e0-3e69-35c5-ad15-bfb18bde7016 | -3.4312 | -46.15698 | 2024-11-29 00:52:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 899087a2-7355-3a87-a3cb-75bb025e2686 | -1.50932 | -52.56386 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0e653750-db12-3ad3-a7b0-1ec402a84fe8 | -2.86264 | -45.54462 | 2024-11-29 00:52:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 239.7 |
| 62305dd0-be8b-3c97-a053-1a748d9b48ad | -4.05093 | -48.33474 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 5f416ae6-62bb-3797-9370-3a8bb14520ca | -2.42195 | -46.49685 | 2024-11-29 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3df3b671-1905-3bd1-8cea-8551a12701fd | -1.25473 | -54.55556 | 2024-11-29 00:52:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| cf9864e3-d113-37fe-a114-bd9d1a8544da | -3.41125 | -50.15812 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0b668b00-65dd-3cfa-9289-1be4473fa9fb | -3.41887 | -50.16064 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |


[Clique aqui para ver as próximas entradas](README9.md)
