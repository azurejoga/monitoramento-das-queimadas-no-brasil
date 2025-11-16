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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6c163f7-a52f-3798-a99a-3a6399a3d373 | -2.81 | -52.97008 | 2025-11-16 00:15:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| eafb8a8e-78ac-3788-a501-dd1f37651670 | -3.26149 | -45.78339 | 2025-11-16 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 5f12a431-f5e2-35b0-8c5a-d5a74ce45e19 | -3.17107 | -45.73024 | 2025-11-16 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 026fa739-0561-328b-b7cb-a3aeed7c2d47 | -1.9961 | -47.36045 | 2025-11-16 00:15:00 | TERRA_M-M | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a0b17710-ded9-3fa6-9bf9-0c97c61af59c | -3.58466 | -50.42405 | 2025-11-16 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 433b567e-4b22-3eed-8c17-f9839ae8ee26 | -1.79343 | -46.08723 | 2025-11-16 00:15:00 | TERRA_M-M | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 23c5a5c4-a0e7-3a7a-8620-c1c8db8abdda | -3.33913 | -45.61343 | 2025-11-16 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| aa9a7e89-d136-32d7-b722-aa68cf9e4661 | -3.7248 | -49.53891 | 2025-11-16 00:15:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 61cd29b3-0a4a-3c17-819b-2c3534de1614 | -3.17913 | -44.39774 | 2025-11-16 00:15:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| aba1c00a-affd-36ad-9f25-6906f61cfebf | -3.58143 | -50.41648 | 2025-11-16 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5aba5715-8bd6-3dd7-b10c-feb739eb4c9b | -2.99421 | -45.44602 | 2025-11-16 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8dda0c5a-0ebd-3383-894e-a9540692cced | -1.18019 | -53.59316 | 2025-11-16 00:15:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2279aa91-2d7a-3e48-a11c-488d944102b3 | -2.59101 | -51.83303 | 2025-11-16 00:15:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 259ee181-0615-30d8-99fd-14b4ba8c439a | -3.30811 | -45.79477 | 2025-11-16 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| cd65cbbf-3b61-3a36-a1f5-58bed81070e5 | -2.68949 | -49.06765 | 2025-11-16 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 96b4a949-a721-3b34-b917-44bfa32e399c | -3.32792 | -45.85743 | 2025-11-16 00:15:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 5f2480be-3c18-31f0-86ef-f46a15d89ebc | -3.39118 | -50.18244 | 2025-11-16 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| b1864c01-aef4-34a0-b3dd-7739d4ee43ab | -2.64051 | -45.76062 | 2025-11-16 00:15:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 7732743e-81ef-3d9e-9e85-d3ef702e2f4c | -2.17879 | -52.0814 | 2025-11-16 00:15:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d92ca802-7872-3b70-b839-72c0f4c845ab | -2.71952 | -47.39762 | 2025-11-16 00:15:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6ea33cbe-3069-3e75-936b-a18b64eccf6d | -2.51761 | -47.80573 | 2025-11-16 00:15:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| f0dc9e2c-4767-3293-9a5f-92b2eb6a8110 | -3.57023 | -49.54147 | 2025-11-16 00:15:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ce539935-c0b0-3721-a4fc-a53538e85717 | -2.71049 | -47.39891 | 2025-11-16 00:15:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| efcddd20-69ca-3077-97e3-d8645d049c64 | -2.78597 | -43.35066 | 2025-11-16 00:15:00 | TERRA_M-M | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 7552e11a-87e5-3a1f-8106-fc44c485b164 | -1.17532 | -49.21388 | 2025-11-16 00:15:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4a7900eb-99dd-35f0-8cb8-dbadaca3f470 | -3.33255 | -45.16474 | 2025-11-16 00:15:00 | TERRA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 021f9cab-9c57-3c70-be6c-c8ea45073853 | -3.38404 | -50.12915 | 2025-11-16 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 38b6d332-739c-382a-8515-6b9c715701fb | -3.33818 | -45.54153 | 2025-11-16 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 7e110bdd-f014-3720-afd8-7cf49b646ddd | -2.37642 | -44.85205 | 2025-11-16 00:15:00 | TERRA_M-M | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 029dcb8d-c66e-3779-94cf-6018f209d9e7 | -3.16999 | -44.39899 | 2025-11-16 00:15:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0631934d-81dc-373c-9d00-2149a0f01d2a | -2.7898 | -43.35464 | 2025-11-16 00:15:00 | TERRA_M-M | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| bca0e86f-8050-3ff9-a65c-761f66ef6ee1 | -2.34025 | -47.45248 | 2025-11-16 00:15:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 75ce7cb9-20af-33b9-bf74-3f5896ec5e6d | -3.33941 | -45.55037 | 2025-11-16 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6e39b39a-6ebe-329a-9a37-7e4e301e4373 | -3.84334 | -49.81016 | 2025-11-16 00:15:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 662f6850-d137-37cd-9c74-caeacfbae9be | -2.93564 | -51.76235 | 2025-11-16 00:15:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| cfc5e6b4-4a2b-320d-93ac-aa7dcd0e7b9c | -3.88463 | -49.99749 | 2025-11-16 00:15:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 134841a4-1dc9-3d3b-b21b-542c3764710a | -3.46372 | -45.65293 | 2025-11-16 00:15:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 74e1e010-cf2b-3457-8768-b5153d6adcf2 | -3.33554 | -45.84739 | 2025-11-16 00:15:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 53c864e7-9b29-3cdf-a5b0-8777db9f061c | -1.98587 | -47.35261 | 2025-11-16 00:15:00 | TERRA_M-M | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 86cfb48c-35fa-379d-96a5-6ee1456ce0be | -2.46841 | -48.86694 | 2025-11-16 00:15:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| efd6e787-e1de-36bb-ae2c-89848d372be7 | -3.21598 | -43.34503 | 2025-11-16 00:15:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 56cddc49-6fa3-3284-aff8-ae1a754d5914 | -3.35544 | -46.86747 | 2025-11-16 00:15:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c225d5d5-0aa5-3a80-8077-35fe701fe971 | -3.46263 | -50.11242 | 2025-11-16 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 244403a9-91f9-34f7-b98e-9261b8826476 | -1.99523 | -46.55412 | 2025-11-16 00:15:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 57569341-cea9-3d5e-ac22-fccde9b5b886 | 1.7455 | -50.92289 | 2025-11-16 00:17:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 12.1 |
| fc1d8092-9db3-3c5e-9c4d-8e8f97d55e0a | -4.4246 | -43.4038 | 2025-11-16 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 5583a356-c8e3-366a-8e2c-8414c4ff810a | -2.5238 | -47.8115 | 2025-11-16 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 244.3 |
| a79dbd25-2741-342c-9337-95088d5526fa | -6.6875 | -42.0296 | 2025-11-16 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 9552ec2c-1a8c-321e-bb08-d83be609b6a5 | -4.6841 | -46.3186 | 2025-11-16 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| bb6bd2ea-f0e9-3c26-b60b-afd8c1590fc6 | -12.6553 | -46.7633 | 2025-11-16 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 87a0f7d6-1231-3832-9efb-50567e2cbbc2 | -3.2554 | -45.7846 | 2025-11-16 00:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 7a14fa4f-9649-30e9-b0bc-a96f36bddb85 | -1.9886 | -47.3465 | 2025-11-16 00:20:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 31218cb8-8048-3929-848f-1dc39bdb4526 | -4.7395 | -46.3821 | 2025-11-16 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 6b0b7643-2048-31b1-9c89-987ac0cc7a03 | -4.7027 | -46.3176 | 2025-11-16 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 91.3 |
| ec1f004d-355a-362c-8f34-d8f85ae58952 | -6.6687 | -42.0314 | 2025-11-16 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| c8087903-911c-3c87-ac2a-2061e9476aa4 | -2.8016 | -52.9617 | 2025-11-16 00:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 0d62ef9e-7c05-39db-8381-b15e4549e6b8 | -4.8432 | -47.5428 | 2025-11-16 00:20:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 7baf24dd-1798-3fc0-a431-1032bbc11995 | -8.07 | -43.1216 | 2025-11-16 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| df558ee6-2e4e-3794-817c-174c3f2ddda5 | -12.0 | -49.2901 | 2025-11-16 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 445648c5-a12d-3d7f-9723-7a656e4a9bdd | -12.0004 | -49.2683 | 2025-11-16 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 140.1 |
| ff8f1301-60f5-3838-b7e8-a83368fd07ca | -6.7013 | -40.7962 | 2025-11-16 00:20:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 98.5 |
| 04e49800-494b-3528-aa3e-72d3dbe3b696 | -2.5053 | -47.812 | 2025-11-16 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 02a06c42-9c9c-32e8-9a42-37900b9d149a | -2.5238 | -47.8332 | 2025-11-16 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 819ad406-6074-3e0d-a2b1-0eb9ae77a9c4 | -12.6672 | -47.167 | 2025-11-16 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 402e499b-2d9b-3874-9044-f9b865d5d9b4 | -16.5637 | -47.6042 | 2025-11-16 00:20:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 1eb6bee1-5153-303a-b3dd-c61b070c3736 | -2.8925 | -53.2842 | 2025-11-16 00:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 3ada9bce-1881-3741-bc21-11acfd8b37b8 | -4.4059 | -43.4049 | 2025-11-16 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| ce416e7d-f447-31b0-a410-e6525b968e60 | -4.7209 | -46.3832 | 2025-11-16 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 4abbaea5-99f7-3b15-855a-61fa3c35ed59 | -3.3294 | -45.8487 | 2025-11-16 00:20:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| bc8b66b6-e206-31ce-b95a-16c57c27ce1f | -12.0191 | -49.2877 | 2025-11-16 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| f4b2680b-df7d-3022-b4ae-bda5b7f6f6f0 | -8.0703 | -43.0981 | 2025-11-16 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 283.5 |
| 3899cba7-d7c7-3840-a58f-5c3b2c06b56b | -3.2488 | -43.3942 | 2025-11-16 00:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 3359c6f5-c63e-3219-b5e4-275834e671bc | -4.4245 | -43.4271 | 2025-11-16 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 669822b8-95c3-3e7f-8ff6-3daa56271b36 | -12.0195 | -49.2659 | 2025-11-16 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 498483d4-93c9-3d40-85ad-104be3af305d | -12.6557 | -46.7407 | 2025-11-16 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 2e0b4ece-ff0a-35f0-96e2-1d2fac2eddee | -6.3119 | -43.8036 | 2025-11-16 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| b4d1e226-46e0-3e57-aa46-33d7cdc184dd | -8.0513 | -43.1001 | 2025-11-16 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 161.7 |
| 91528cf1-90a0-38cb-9d71-fa5f5a3fa6d1 | -4.843 | -47.5646 | 2025-11-16 00:20:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 92f44e0c-b845-34fd-907e-0f683e8be8ba | -12.6864 | -47.1642 | 2025-11-16 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 789e93e4-4f32-368f-ba5a-303d8fc528a2 | -12.2047 | -49.6121 | 2025-11-16 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| e48bc3d2-0651-3259-b12b-3cfa5e28321d | -14.649 | -46.5807 | 2025-11-16 00:20:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 08a42d79-615a-397f-b83f-084ae193ad86 | -3.3294 | -45.8487 | 2025-11-16 00:30:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 8e95a54a-4c88-3ff0-8210-5974b5b6a490 | -2.8925 | -53.2842 | 2025-11-16 00:30:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| ecfb819a-8aef-345a-884d-67f559f2e091 | -8.0513 | -43.1001 | 2025-11-16 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 155.0 |
| 0fb98976-8487-318d-9ec8-7b0f576ea985 | -12.2047 | -49.6121 | 2025-11-16 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| e01bbe1b-9195-3fcd-9930-00ac126a722e | -16.5637 | -47.6042 | 2025-11-16 00:30:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 116.8 |
| f11e4f73-69ab-3993-a746-85b1d4943ace | -3.6038 | -43.285 | 2025-11-16 00:30:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| c0cca939-28df-38e3-bdb2-4e76fb533d52 | -4.4245 | -43.4271 | 2025-11-16 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f7c6dd26-1277-3403-a9da-82bb9a0d4275 | -2.5238 | -47.8115 | 2025-11-16 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 249.2 |
| a0bd99ac-47eb-386a-96b7-985f56372e3f | -4.7395 | -46.3821 | 2025-11-16 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 24716c71-6455-3949-b872-3fca2bd82a3a | -6.7013 | -40.7962 | 2025-11-16 00:30:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| 7cbd8ab2-36ea-33f0-901d-9a242415d2bf | -4.4059 | -43.4049 | 2025-11-16 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 2ff768bd-8db4-37ad-8a5d-60423eb2306c | -1.9885 | -47.3684 | 2025-11-16 00:30:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| fc425acf-1db5-3988-933a-2e99497f4384 | -1.9886 | -47.3465 | 2025-11-16 00:30:00 | GOES-19 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 4755587e-0b2d-308c-b08e-2dc6b1445975 | -2.8016 | -52.9617 | 2025-11-16 00:30:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 91700fb3-ed1f-3fa6-b099-d6a1ba66edaf | -8.0703 | -43.0981 | 2025-11-16 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 263.3 |
| 303ab898-6132-36a4-a693-6fcc863652a9 | -3.2554 | -45.7846 | 2025-11-16 00:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b4a36d62-d4c3-39b8-b793-c1e135cef006 | -2.5053 | -47.812 | 2025-11-16 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 376898f4-f6dd-3f04-8395-c4c26ffcaf7a | -12.6864 | -47.1642 | 2025-11-16 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 8fed3609-921f-3f73-9901-777c42e295d4 | -12.6672 | -47.167 | 2025-11-16 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |


[Clique aqui para ver as próximas entradas](README10.md)
