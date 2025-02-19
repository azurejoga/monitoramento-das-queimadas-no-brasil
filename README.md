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
| af9dc906-4fdf-3e0b-95a1-72eaa9fea6a3 | -3.2727 | -42.3864 | 2025-02-19 00:00:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 2b19ce7d-b88b-3b04-bf59-b81505384a8f | -7.0946 | -35.1218 | 2025-02-19 00:00:00 | GOES-16 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 86.0 |
| 6f8b9804-964f-351a-85db-cdc5e71f4a9d | -7.0949 | -35.0943 | 2025-02-19 00:00:00 | GOES-16 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 134.9 |
| d8b6c8b5-c234-3385-89fe-7fe6255585b7 | -7.3995 | -35.1631 | 2025-02-19 00:20:00 | GOES-16 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 99.3 |
| 5700b829-5c13-3f83-aab9-ab1df7519aa0 | -22.6796 | -42.8573 | 2025-02-19 00:28:00 | METOP-B | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f5e27a2d-e875-3552-8259-ca953622fabd | -13.8063 | -41.709 | 2025-02-19 00:28:00 | METOP-B | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2179780e-104e-3087-b11a-4d66f566ccc4 | -3.2751 | -42.3881 | 2025-02-19 00:28:00 | METOP-B | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9129d347-1661-3dd0-b9a5-cb3e085599b2 | -21.418501 | -48.542 | 2025-02-19 00:28:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ef28fe64-d7eb-3997-859e-3dd23ae8c514 | -10.5463 | -45.213299 | 2025-02-19 00:28:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 15a2e013-3304-3e8b-b4cf-3da003975ca2 | -11.5824 | -47.632599 | 2025-02-19 00:28:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 18e61018-8f07-3d58-9ebe-72021d67dbb5 | -13.8029 | -41.6954 | 2025-02-19 00:28:00 | METOP-B | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 64280961-4189-33b2-afa3-e359056247c6 | -3.2848 | -42.385799 | 2025-02-19 00:28:00 | METOP-B | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d60b0c0-1baf-3b17-9e64-411e9c09a271 | -10.95 | -45.173599 | 2025-02-19 00:28:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d29ae8ab-3725-375a-8f15-3d84bd3c5b72 | -19.7785 | -42.013199 | 2025-02-19 00:28:00 | METOP-B | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e12792e6-f8b3-31d7-8250-efbb7899d851 | -3.2708 | -42.370201 | 2025-02-19 00:28:00 | METOP-B | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 256676e0-97e3-351b-934c-e9d075053c8e | -19.537001 | -45.907101 | 2025-02-19 00:28:00 | METOP-B | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 121c7c9e-de53-30c9-bfbf-ae3b6c8ff37f | -13.7995 | -41.6819 | 2025-02-19 00:28:00 | METOP-B | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 553a24d7-c865-3ea7-b07d-4e088ca08875 | -13.7932 | -41.697899 | 2025-02-19 00:28:00 | METOP-B | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d356473b-cd78-3f6b-9328-a4bbb014a666 | -22.6775 | -42.8484 | 2025-02-19 00:28:00 | METOP-B | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1944e3df-a8f2-3880-a7e6-e7b1a1f234d4 | -19.535299 | -45.899601 | 2025-02-19 00:28:00 | METOP-B | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 837bab69-45d1-346c-b9bb-b9fbfe50ee57 | -10.6526 | -44.488098 | 2025-02-19 00:28:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 32ef9b8d-6855-3bf3-979c-b4a850514ebf | -10.6502 | -44.478001 | 2025-02-19 00:28:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aa41ce42-0c3d-3bd4-9db7-bdf8a832f2e7 | -1.581 | -54.518902 | 2025-02-19 00:28:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45e621e1-8e1f-36dc-9783-2e2437a2ee5b | -11.0356 | -45.055901 | 2025-02-19 00:28:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca73ccba-07e0-35fe-9a04-6551c28be79a | -15.8114 | -42.1037 | 2025-02-19 01:00:00 | GOES-16 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 54.6 |
| c4890b34-3804-32e5-929d-8fba8a0c9254 | -20.68959 | -48.81459 | 2025-02-19 01:06:00 | TERRA_M-M | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| c2000567-cbc6-32e2-a6e3-790df59735ae | -15.80884 | -42.13299 | 2025-02-19 01:06:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 662ea1f0-fec6-36a1-92fe-7ed8aa379e26 | -19.53749 | -45.9175 | 2025-02-19 01:06:00 | TERRA_M-M | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 47e5321c-e614-373d-aa34-83fabd8a8960 | -19.53419 | -45.91263 | 2025-02-19 01:06:00 | TERRA_M-M | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 25.1 |
| f7c08481-49fa-3c6b-a578-f6a0149ff83d | -19.53472 | -45.90099 | 2025-02-19 01:06:00 | TERRA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6fe6f2f4-b5b2-37ce-82e4-c4dc0288df36 | -15.81422 | -42.12502 | 2025-02-19 01:06:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 0071fcfe-752a-33c5-b8b1-ab26409136b4 | -14.97449 | -50.76693 | 2025-02-19 01:09:00 | TERRA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b01df3a3-66ee-34f1-ad1f-5b77265330e4 | -13.80496 | -41.7153 | 2025-02-19 01:09:00 | TERRA_M-M | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 44.9 |
| eef61c3b-7a43-36f3-8a5a-5a5922ae9833 | -10.63999 | -44.49648 | 2025-02-19 01:09:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 04f9cf45-3bb3-36df-9f99-4efb699514d7 | -1.57792 | -54.52278 | 2025-02-19 01:11:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c3d64fc7-2e5e-38a2-a776-83dff37d0916 | -1.83092 | -54.09472 | 2025-02-19 01:11:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 98576128-bc2b-3040-b0d6-cbd4ef7761e2 | -1.82966 | -54.08568 | 2025-02-19 01:11:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 39baf8a5-56d7-337c-83cf-75d7e350470e | 2.6379 | -61.13289 | 2025-02-19 01:13:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 16524e7b-8d6c-3436-b624-4a8c9831bb3f | 2.6296 | -61.1381 | 2025-02-19 01:22:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6940b38a-0a5b-34bb-8b71-6d4a4ec8f0a3 | 2.6327 | -61.1245 | 2025-02-19 01:22:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 96454ee2-58e4-3055-ac04-af1803ff68d8 | 2.6311 | -61.131302 | 2025-02-19 01:22:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 76dc7bde-2d95-351d-bfc1-b7a9bcacc080 | -6.76505 | -35.18065 | 2025-02-19 03:04:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 36477b37-ea81-35dc-9be0-a0c6f927ea43 | -15.81209 | -42.11876 | 2025-02-19 03:08:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e0890e9a-f8f2-38a4-a597-033d9b85d5ad | -15.0538 | -42.43081 | 2025-02-19 03:08:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5004668d-8fce-3f8c-bb63-987b8cf174e7 | -15.81751 | -42.11617 | 2025-02-19 03:08:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e668214c-c150-370e-97b8-7c3532587921 | -15.81907 | -42.12042 | 2025-02-19 03:08:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 18b1b50c-720a-36e8-bf66-eced11e1ff91 | -20.20884 | -40.73191 | 2025-02-19 03:08:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0e98013a-34a7-3148-85a2-898dc47254ce | -15.81364 | -42.11185 | 2025-02-19 03:08:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bd656316-b7f4-32c9-8415-6d457bcccb9d | -13.7961 | -41.70251 | 2025-02-19 03:08:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 7e8fc579-f044-3c51-9c01-122be6422b4a | -15.05564 | -42.42973 | 2025-02-19 03:08:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| bab607e4-0e23-3113-b0a3-fd70744086b1 | -20.21102 | -40.73031 | 2025-02-19 03:08:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1b60e9c9-b595-3063-8eee-322dee662579 | -20.55341 | -40.92908 | 2025-02-19 03:08:00 | NPP-375D | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| e04f0e27-d100-3096-9757-a093bdf1c025 | -15.81052 | -42.11454 | 2025-02-19 03:08:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4825e82c-1bc2-3f15-9269-9947f0d83f1d | -22.67301 | -42.85741 | 2025-02-19 03:10:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| fdcebdbc-3450-3a97-9d85-2a87fe1e892f | -22.67161 | -42.86308 | 2025-02-19 03:10:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9fda530f-e6cb-3b70-b3f7-bbf4ede6f6ce | -22.67352 | -42.85741 | 2025-02-19 03:10:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9667d46b-b8b4-316f-87fb-50b980a961f5 | -22.67215 | -42.86312 | 2025-02-19 03:10:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6f3c5fac-a35f-3ebd-87e1-326b62af1f70 | -5.50106 | -35.59119 | 2025-02-19 03:27:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 169b781f-a7c1-3572-8a94-c69c485b7706 | -7.73116 | -38.96879 | 2025-02-19 03:27:00 | NOAA-20 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 674397a6-309a-3012-b96e-05d46815d841 | -7.42725 | -35.27423 | 2025-02-19 03:27:00 | NOAA-20 | CAMUTANGA | PERNAMBUCO | Brasil | 2603603 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 06831285-31bb-35ef-845c-6756fb84b175 | -5.98461 | -35.37816 | 2025-02-19 03:27:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0edeffc1-3d1e-36e5-8dce-a196ee33a503 | -3.27218 | -42.37908 | 2025-02-19 03:27:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fa1c464b-3ca7-3ed6-ae1c-2023b27e014a | -11.6187 | -38.05051 | 2025-02-19 03:27:00 | NOAA-20 | ACAJUTIBA | BAHIA | Brasil | 2900306 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c3ec082f-6c84-37a0-b69c-00697242137f | -5.98465 | -35.37994 | 2025-02-19 03:27:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1725f7db-1691-3076-8ca9-5de42251cee4 | -3.27141 | -42.38365 | 2025-02-19 03:27:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ea97110-26ce-3b23-99d1-ccc58950e472 | -6.76566 | -35.18272 | 2025-02-19 03:27:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3cb0a9fc-a7e4-38a5-9669-ddfc9329e27a | -10.69372 | -37.04782 | 2025-02-19 03:27:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8753f93b-a91f-32fd-8fc7-ea027790a63a | -5.50034 | -35.59564 | 2025-02-19 03:27:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d13de933-2392-3f56-9d5a-caf1d1662062 | -7.73563 | -38.96954 | 2025-02-19 03:27:00 | NOAA-20 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ad33fcb2-bba1-3f31-add9-a1348bf70698 | -7.63123 | -34.93942 | 2025-02-19 03:27:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 94dca281-85d2-340e-b87a-9619c67cc229 | -5.98533 | -35.37566 | 2025-02-19 03:27:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1df6e87a-e8b1-3b81-b22d-895ed065cc1b | -11.62131 | -38.05184 | 2025-02-19 03:27:00 | NOAA-20 | ACAJUTIBA | BAHIA | Brasil | 2900306 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7425d585-efa1-33e0-addb-db189dc0a60c | -8.12384 | -43.14061 | 2025-02-19 03:27:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9a2d1f33-487f-3197-a6d1-03eb577b940c | -6.73324 | -38.96463 | 2025-02-19 03:27:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 727644ec-7278-3d10-af94-8c70015d7406 | -15.05049 | -42.42725 | 2025-02-19 03:29:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fc87276d-9991-3cb3-94dd-9ffb71e5c749 | -13.79923 | -41.70411 | 2025-02-19 03:29:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 726a26c2-b036-3bee-9487-60915c04905c | -15.05003 | -42.42527 | 2025-02-19 03:29:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 133a8c18-5df6-3a33-b113-075c629550ed | -13.03474 | -40.24645 | 2025-02-19 03:29:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4e1945fe-ea71-3103-8fd1-14ff63f66069 | -15.81072 | -42.11461 | 2025-02-19 03:29:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6d0218df-0491-394d-995e-c46e87abedb7 | -16.63728 | -39.8675 | 2025-02-19 03:29:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 50be666d-0028-3620-b38d-2009ffd9d2e3 | -11.02598 | -45.18781 | 2025-02-19 03:29:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b0a0103-55a9-3de9-a415-bc3f55c229f7 | -10.54374 | -45.21689 | 2025-02-19 03:29:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c7cf0db-d815-3412-9213-061d4376f6bb | -15.8155 | -42.11558 | 2025-02-19 03:29:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0c8ab5cb-ad0a-3aba-9ede-655ffe4bda6a | -15.81445 | -42.12096 | 2025-02-19 03:29:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6725b8f6-f726-33cc-aa43-44292af5c852 | -17.50126 | -39.95443 | 2025-02-19 03:29:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bacdf2bf-d8a9-3100-be5e-78639c975ba3 | -11.02699 | -45.18273 | 2025-02-19 03:29:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e76e43c7-1b1f-335b-9b12-8dee70c56ef5 | -13.79625 | -41.70216 | 2025-02-19 03:29:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 918262f8-1d1f-36b2-886e-52b436847065 | -10.64387 | -44.48997 | 2025-02-19 03:29:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb96486e-88df-3244-be97-f94e09d1b2a1 | -16.34749 | -43.69709 | 2025-02-19 03:29:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd4910f3-06dd-30ac-90b8-4deea89b416e | -15.4228 | -39.79863 | 2025-02-19 03:29:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6b13d3d3-ee14-3ab2-8267-27f449802d07 | -16.63794 | -39.86386 | 2025-02-19 03:29:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 38a1e1e8-1212-3fb5-81bc-b3c34f5c59c7 | -13.79442 | -41.70306 | 2025-02-19 03:29:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c929111f-dbef-3321-9cfc-cc78a0253917 | -10.64439 | -44.487 | 2025-02-19 03:29:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 21cfd679-74cb-3ac9-bd31-7080c73447f5 | -16.63735 | -39.86359 | 2025-02-19 03:29:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 5a3da440-b441-3253-94e1-32168ea8dcc0 | -10.54269 | -45.22215 | 2025-02-19 03:29:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 771fb56c-3a18-3497-b658-f311373635c2 | -17.52508 | -39.41367 | 2025-02-19 03:29:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a1b1da5e-093e-30b9-99a0-376b08b604d1 | -15.055 | -42.42612 | 2025-02-19 03:29:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 84a77291-5d6f-3f57-ac23-f91228f4db29 | -16.64073 | -39.86807 | 2025-02-19 03:29:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 15b186b0-0e97-3b61-9771-48cc8ca9ca0a | -10.64477 | -44.48531 | 2025-02-19 03:29:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7571294d-4be1-3427-8a60-761854b767f1 | -19.53646 | -45.91148 | 2025-02-19 03:32:00 | NOAA-20 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README2.md)
