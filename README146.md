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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88d200ab-0612-3824-b30c-4d4931126d68 | -10.6084 | -48.2995 | 2024-10-10 12:36:06 | GOES-16 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| cceb1584-a179-3594-9820-0373fcb07800 | -11.29 | -51.0059 | 2024-10-10 12:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 18cbc7f6-3c58-3da9-8d33-2e618d22945c | -11.2894 | -51.0484 | 2024-10-10 12:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 174.9 |
| 4f48bb98-7dea-34f5-962f-20d8f5543ee9 | -11.3087 | -51.0251 | 2024-10-10 12:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 411.1 |
| 0ecf37c4-23b0-395a-8e74-cabbcea6308f | -11.3084 | -51.0464 | 2024-10-10 12:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 48dc311e-d5d8-327b-ba9a-ebd1b3bd7faf | -11.309 | -51.0038 | 2024-10-10 12:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 256.1 |
| 9ebb491f-5372-3b00-9ba3-565d9c15904e | -11.3286 | -50.9592 | 2024-10-10 12:36:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f004efe2-eb3f-3bcb-8fbd-274b568a2000 | -12.2083 | -50.603 | 2024-10-10 12:36:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| c1665dcd-fabb-3e2c-bc19-cf2b309fb877 | -12.2978 | -45.3112 | 2024-10-10 12:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 274.0 |
| 47ca9d23-bb9b-36dd-81ff-3a19dc380852 | -12.1895 | -50.5838 | 2024-10-10 12:36:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 4dd0a16f-37ae-328d-be13-83eaa5dc8c90 | -12.1892 | -50.6053 | 2024-10-10 12:36:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| bff336f2-037c-3ede-86a7-fc2570605574 | -13.1276 | -51.6649 | 2024-10-10 12:36:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| c0b3a391-c3c1-3f6d-9a00-43d0ec00c41b | -13.8374 | -44.5455 | 2024-10-10 12:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 167.9 |
| e4f35215-0ecf-3f17-b61a-044b25e903a0 | -13.8369 | -44.5691 | 2024-10-10 12:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 0da24fa2-2378-3a8e-a95e-79704449397e | -13.8569 | -44.5421 | 2024-10-10 12:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| ee37a3ca-f9ca-35f4-9e67-cd2af0796ab8 | -13.8574 | -44.5185 | 2024-10-10 12:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 61885a25-d17a-361a-a730-bd0000caacff | -13.8564 | -44.5657 | 2024-10-10 12:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 2b19784a-45ce-322f-b32f-e93ecbc95b8e | -13.8379 | -44.522 | 2024-10-10 12:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |
| a360a124-982d-30dd-8883-159c3038b007 | -14.043 | -44.0129 | 2024-10-10 12:36:25 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 4c54f2f5-f600-3ed1-9448-cc0149151882 | -4.49618 | -40.92453 | 2024-10-10 12:38:00 | TERRA_M-T | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 15.1 |
| b69dce17-0f5f-3b5d-b166-48fd267aa7b2 | -3.9586 | -41.48 | 2024-10-10 12:38:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 121.8 |
| 11ab6281-8c05-385b-ae48-11c490df5084 | -3.60586 | -41.52624 | 2024-10-10 12:38:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| a6377d54-e410-32fd-8e54-0fb81e0424ae | -3.57652 | -41.78326 | 2024-10-10 12:38:00 | TERRA_M-T | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 2f1b7152-5f6a-3a9d-adb8-8eff2786b474 | -3.57484 | -41.79545 | 2024-10-10 12:38:00 | TERRA_M-T | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 39.9 |
| 6fa15548-aab2-3942-a084-96f853da417d | -3.77682 | -42.61927 | 2024-10-10 12:38:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 28.5 |
| 366002be-2482-3fd7-823a-2612024840e9 | -3.77835 | -42.60838 | 2024-10-10 12:38:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| dca0668d-09de-3cc0-b770-3f3b4e51df96 | -5.15716 | -43.06175 | 2024-10-10 12:38:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4d3bbff3-0b6e-3fa2-983a-26efcc854f52 | -3.42369 | -43.16243 | 2024-10-10 12:38:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e81f7e0f-42b3-3d29-9b56-3ee2152cc02b | -3.22509 | -43.39675 | 2024-10-10 12:38:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 734a02fa-9b7e-349d-9e4c-202cbe59d608 | -3.22369 | -43.40652 | 2024-10-10 12:38:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e4a7812f-5260-37a1-8532-edae7f9039d1 | -4.79919 | -43.78502 | 2024-10-10 12:38:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f4013db2-5832-3949-be5c-a2847cbb5d33 | -4.73336 | -43.79993 | 2024-10-10 12:38:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 29740df8-b594-3564-a3d6-b9c4bc24a4f5 | -4.40506 | -43.519 | 2024-10-10 12:38:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 2bd6e4cf-cb64-3d78-a844-daa1efa1004e | -4.39426 | -43.52766 | 2024-10-10 12:38:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 11c72730-d635-39bb-a709-80d48e3447e5 | -4.393 | -43.85265 | 2024-10-10 12:38:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 21ffa77b-4636-3cd8-981d-0ff793f6cc94 | -4.33584 | -43.493 | 2024-10-10 12:38:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6c7ce7c9-ac38-3f4c-872a-70e340280b8b | -4.28189 | -43.73637 | 2024-10-10 12:38:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fda77cff-bb19-3ce3-bf25-7a42fd4318d3 | -3.78539 | -44.37105 | 2024-10-10 12:38:00 | TERRA_M-T | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 409cde49-dc63-32c3-a32b-56cddd42ca80 | -3.55401 | -44.37636 | 2024-10-10 12:38:00 | TERRA_M-T | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d8669fd3-fb90-31ee-80c6-94616ebc8782 | -1.72019 | -45.20585 | 2024-10-10 12:38:00 | TERRA_M-T | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5089c085-affe-33ff-a2ea-3c04db49166d | -1.71891 | -45.21466 | 2024-10-10 12:38:00 | TERRA_M-T | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4a466534-107c-381b-a9fd-c154e253ace7 | -3.49712 | -44.90582 | 2024-10-10 12:38:00 | TERRA_M-T | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 015a5512-f87d-36fb-b353-24389db99e8f | -2.89732 | -45.66733 | 2024-10-10 12:38:00 | TERRA_M-T | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 10cfb931-06f8-3fbc-a832-fe3a4fe1806e | -2.89604 | -45.67617 | 2024-10-10 12:38:00 | TERRA_M-T | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d24685fd-80ff-3784-b53c-d3600f369acf | -2.88845 | -45.6661 | 2024-10-10 12:38:00 | TERRA_M-T | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 63.1 |
| f3aeeaaf-f4b9-353a-aec9-b433794fe660 | -2.88717 | -45.67493 | 2024-10-10 12:38:00 | TERRA_M-T | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 8050e2a6-da8b-358e-94e8-daca4c13780a | -3.83434 | -45.56391 | 2024-10-10 12:38:00 | TERRA_M-T | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 37df9a4f-5435-31ef-9633-189503706bac | -2.18192 | -46.08732 | 2024-10-10 12:38:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 97e2a243-9b71-3d85-bf09-08ac66077a62 | -2.17596 | -45.93987 | 2024-10-10 12:38:00 | TERRA_M-T | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9540d65a-4d7d-3560-b3bd-14d74e63908b | -2.17466 | -45.94882 | 2024-10-10 12:38:00 | TERRA_M-T | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 6ac4be63-813b-3258-9dd1-f034a166541c | -2.16703 | -45.93863 | 2024-10-10 12:38:00 | TERRA_M-T | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 11936302-340b-3040-8341-78757ec0bc50 | -1.65701 | -46.14859 | 2024-10-10 12:38:00 | TERRA_M-T | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3f811438-d35c-305f-ac45-7e8f6ff8e231 | -4.10632 | -46.80267 | 2024-10-10 12:38:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 4570c871-aaa4-3d0e-a182-be1b85715cb9 | -2.29759 | -47.89724 | 2024-10-10 12:38:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 525e8f34-43c4-30cf-b838-df468539fcab | -4.4886 | -48.10264 | 2024-10-10 12:38:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0aa9f5c0-ca85-3690-919d-a8daa52a7c4a | -4.48709 | -48.11298 | 2024-10-10 12:38:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| ae9878df-0aa9-3709-a337-7a84151f8246 | -4.10564 | -48.26958 | 2024-10-10 12:38:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 34cdfecf-7552-37a7-b6e9-fd6698830809 | -6.96852 | -37.97461 | 2024-10-10 12:40:00 | TERRA_M-T | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 34.2 |
| 9b857201-fa2f-3a87-9406-732a9f97f82b | -6.93558 | -37.99208 | 2024-10-10 12:40:00 | TERRA_M-T | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 34.4 |
| 34dd1a1a-c737-30d4-b3d7-60c7be0a877a | -8.68747 | -40.9344 | 2024-10-10 12:40:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 185cd3a0-fed9-3674-94ab-37f0caad4852 | -8.56546 | -40.65736 | 2024-10-10 12:40:00 | TERRA_M-T | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 7b1a0cd4-81ee-32fb-8a88-85a86709d7a2 | -8.85232 | -41.43591 | 2024-10-10 12:40:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 74a07eab-f95b-3139-b9a6-aebf0c2d9ca0 | -6.00593 | -42.90791 | 2024-10-10 12:40:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 31.2 |
| 220a4e51-6e69-33e7-856b-804cf406437d | -5.9865 | -42.3764 | 2024-10-10 12:40:00 | TERRA_M-T | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| de7d5030-5b77-311e-a362-5ed695912674 | -5.76032 | -43.19178 | 2024-10-10 12:40:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 14593659-fd12-3c81-ac0a-ce01da578ca9 | -5.75215 | -43.17959 | 2024-10-10 12:40:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 7704d803-f8f1-370e-a626-f101c5d2d9f6 | -5.75062 | -43.19041 | 2024-10-10 12:40:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 40.2 |
| 5af674e6-692a-370e-9835-fb18e00337d5 | -5.51071 | -42.79237 | 2024-10-10 12:40:00 | TERRA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 25aecbf0-9004-3cc6-b4b2-f55c68cfd01a | -6.26911 | -43.42854 | 2024-10-10 12:40:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 466a97eb-a9af-365a-9dae-8e1f150ee680 | -6.19052 | -43.42912 | 2024-10-10 12:40:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 850fa7cd-e75a-3c7a-bb51-5ceb836788a8 | -6.18908 | -43.43962 | 2024-10-10 12:40:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| dfece3ef-ec43-3c74-936c-a5fdb955dbce | -6.18631 | -43.43289 | 2024-10-10 12:40:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 78f5d68a-3e16-3883-b6ef-332da86b83d8 | -6.00307 | -43.45485 | 2024-10-10 12:40:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 13b129dd-1bea-3717-833d-15ea931f6947 | -5.99853 | -43.45839 | 2024-10-10 12:40:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 9bbfb5aa-4c95-311a-abf6-584d1e4acb68 | -5.56563 | -43.19659 | 2024-10-10 12:40:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cdd5f496-5c4e-31ea-9102-169118eee614 | -5.29315 | -43.0313 | 2024-10-10 12:40:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 697031d4-a1d5-39a6-9428-2d14531e6e4b | -7.67597 | -42.49877 | 2024-10-10 12:40:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 6e2c1376-9246-39d1-9fcd-0c107c721bc3 | -7.22383 | -42.29078 | 2024-10-10 12:40:00 | TERRA_M-T | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 153a0352-c981-3815-bebc-55a057b47c22 | -7.2221 | -42.30356 | 2024-10-10 12:40:00 | TERRA_M-T | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 14b47a8a-2068-36d3-96fc-a155f0e191b1 | -6.64856 | -43.06132 | 2024-10-10 12:40:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 412fcc3b-af4f-3278-920a-08f9b5ebae1c | -6.61503 | -43.15901 | 2024-10-10 12:40:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 9a6e0ace-a475-3377-a435-15b43f5b5975 | -6.46747 | -43.32733 | 2024-10-10 12:40:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 20602595-cc89-3542-82cf-6e4f44b8859e | -6.30221 | -45.00655 | 2024-10-10 12:40:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0c430378-ff39-3d41-be4e-5c5828bb6011 | -6.13545 | -44.68968 | 2024-10-10 12:40:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 70ed0bb3-2cb0-3097-a128-4308d22eb135 | -6.11948 | -44.9315 | 2024-10-10 12:40:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| de6a4727-d57c-3f29-95ec-ab3cbc5785d6 | -6.11817 | -44.94063 | 2024-10-10 12:40:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 9fc6d083-b1a2-3628-acfa-c34bd4acf5ca | -6.35099 | -43.81036 | 2024-10-10 12:40:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 188bb9e6-a243-3a05-9cd6-c5a793bce6a9 | -6.34957 | -43.82059 | 2024-10-10 12:40:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fe6c4602-8e41-3dd6-b541-dc21edf335c4 | -6.32822 | -43.7662 | 2024-10-10 12:40:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e7de54f0-89bb-3b5a-b5b0-1dda11a6f62f | -6.32399 | -43.75919 | 2024-10-10 12:40:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 23cd87ac-182a-3942-a85d-00eae7429d04 | -6.24609 | -43.52216 | 2024-10-10 12:40:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c5242158-670d-3d72-aed0-df69b367f475 | -5.99556 | -43.47926 | 2024-10-10 12:40:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 81982160-4a3e-3e9b-aaf8-c722801467bc | -5.35752 | -43.43321 | 2024-10-10 12:40:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 611f4684-4053-33db-8da1-20529b283c38 | -6.20786 | -44.10862 | 2024-10-10 12:40:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| fff51626-34e1-3c67-a988-f73f3798ffdc | -6.18844 | -44.38071 | 2024-10-10 12:40:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5929bb6c-1a3c-31ea-87bc-6b899cd18233 | -5.4948 | -44.27396 | 2024-10-10 12:40:00 | TERRA_M-T | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 985bae4d-3090-3b54-99c9-e4245f1915fd | -5.49344 | -44.28344 | 2024-10-10 12:40:00 | TERRA_M-T | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| ce48b649-a178-3e4a-88fb-d957ec9116d1 | -5.47513 | -44.28091 | 2024-10-10 12:40:00 | TERRA_M-T | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7b3de55e-5253-3970-8162-3fa658bf379e | -7.91784 | -44.85397 | 2024-10-10 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 812f8732-bfed-3fad-8eb3-b5c75d58ee83 | -7.91648 | -44.86349 | 2024-10-10 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |


[Clique aqui para ver as próximas entradas](README147.md)
