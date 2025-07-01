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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 282bb1d0-7242-3abd-9db7-456c7d6235bd | -9.25061 | -58.75183 | 2025-07-01 06:27:00 | AQUA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6b919f92-cbde-352c-9e0c-ef335f90b8db | -10.88635 | -56.44292 | 2025-07-01 06:27:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 95d6bae6-3edc-36ff-a406-708fdba30ec3 | -9.69772 | -56.17692 | 2025-07-01 06:27:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 817b7c8f-c8b3-3dd4-8d0c-dfe421295856 | -9.24134 | -58.7504 | 2025-07-01 06:27:00 | AQUA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f5c773a8-ae1f-3b60-90b1-0115b7875ba6 | -10.12154 | -52.34969 | 2025-07-01 06:27:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 426c10dc-b280-3471-b8c0-84a3e7d12bc3 | -10.02434 | -54.31843 | 2025-07-01 06:27:00 | AQUA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1980f514-9c3b-33ef-89bf-a904bef4d9ee | -6.2945 | -43.6659 | 2025-07-01 06:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 58d78ce0-83b2-3667-a92f-e3323bd62a5e | -6.2943 | -43.6891 | 2025-07-01 06:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| ab8d17fb-490f-3c7d-aa58-96898ecb0ff3 | -6.2945 | -43.6659 | 2025-07-01 06:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| ee6d86b7-6cdb-3f42-925e-84675ac8e6fb | -6.2943 | -43.6891 | 2025-07-01 06:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 4f5beeb0-77fc-3706-b7e6-295578ba510f | -6.2943 | -43.6891 | 2025-07-01 06:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 210b1911-6fd6-3282-85aa-58a07b1fb6f8 | -6.2945 | -43.6659 | 2025-07-01 06:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 19ea0cb5-5d99-3a36-be4b-3742659a6ca9 | -6.2945 | -43.6659 | 2025-07-01 07:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| ccddfb49-00c3-3ce1-941a-088be88d0e35 | -6.2943 | -43.6891 | 2025-07-01 07:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 30ea2833-ded2-3af0-8b8d-308083b2de47 | -6.2945 | -43.6659 | 2025-07-01 07:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 2bb71b62-1d09-3dbf-ab53-4ce5a9c87d2b | -6.2943 | -43.6891 | 2025-07-01 07:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| eb8425b1-195d-3191-bc3f-ac3b6df209d4 | -6.2945 | -43.6659 | 2025-07-01 07:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 50d808cc-b188-375c-91ef-311da2460abf | -6.2943 | -43.6891 | 2025-07-01 07:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 38d0505a-1c67-3744-999b-95db2883228c | -6.2943 | -43.6891 | 2025-07-01 07:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 350ea8c9-2432-3070-83bb-b88b39db4a38 | -6.2945 | -43.6659 | 2025-07-01 07:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 780026c9-bb41-3ee4-8409-dc9803fa0e1a | -6.2943 | -43.6891 | 2025-07-01 07:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 97c9d39f-4128-357c-8f52-9d1ca531bb0c | -6.2943 | -43.6891 | 2025-07-01 07:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 47d27b02-4958-3fd4-97aa-f1421decd917 | -6.2945 | -43.6659 | 2025-07-01 07:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| cb68fa0b-bc02-3b5b-8841-10b80c57b7ad | -6.2943 | -43.6891 | 2025-07-01 08:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| e2a79a2f-54a0-3988-94e9-6d32a04a7b50 | -6.2945 | -43.6659 | 2025-07-01 08:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 0d9389cd-0588-32e3-bb34-870ba807280c | -6.2943 | -43.6891 | 2025-07-01 08:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 9db20bf1-8bc6-3835-bc8a-d43173f9d02a | -6.2945 | -43.6659 | 2025-07-01 08:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 6296935f-dc53-32cb-868c-0f47d8170325 | -6.2943 | -43.6891 | 2025-07-01 08:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 8e4d2e71-b04e-3af5-a386-8f6abe29fdca | -6.2943 | -43.6891 | 2025-07-01 10:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| d0e1b2e1-8e37-3125-94a2-54f24bc89058 | -7.0943 | -44.3819 | 2025-07-01 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 4d530146-1731-3f0e-8301-eb558a3cd212 | -7.0943 | -44.3819 | 2025-07-01 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 3b4bb208-18c5-355c-8950-c879c6f91f5f | -7.20472 | -40.24201 | 2025-07-01 12:06:00 | TERRA_M-T | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 1a596d3b-1024-3e9b-8597-173f53da3414 | -6.77196 | -43.85563 | 2025-07-01 12:06:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1d1d912d-4a05-3369-afba-231d2c70ff05 | -6.28155 | -43.67944 | 2025-07-01 12:06:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| b1c45a7d-4758-30f6-be2f-cf815d6b043b | -6.29942 | -43.68199 | 2025-07-01 12:06:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 2108f07d-74a0-3d02-bf07-5a78b8e3aecf | -4.38644 | -41.90863 | 2025-07-01 12:06:00 | TERRA_M-T | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| d3682cc0-df39-3c25-a7ff-3fb5be938322 | -7.08943 | -44.39937 | 2025-07-01 12:06:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 4ca7f49b-d1a1-3917-bf60-28a5c7b460da | -7.09217 | -44.38056 | 2025-07-01 12:06:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 4b69a015-f286-372f-a0a2-b6a844d486bf | -7.0908 | -44.38995 | 2025-07-01 12:06:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 166.4 |
| e471734d-63f2-3f2f-a43a-7e0a6ff1aec9 | -6.21693 | -43.35524 | 2025-07-01 12:06:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| b3440558-be30-36b1-b4ce-25dfa60f19a9 | -5.99752 | -36.51758 | 2025-07-01 12:06:00 | TERRA_M-T | BODÓ | RIO GRANDE DO NORTE | Brasil | 2401651 | 24 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 189742ba-1347-31c9-8c7d-bafdacd1e392 | -6.29049 | -43.6807 | 2025-07-01 12:06:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| f6a04e22-bcfd-34a7-ab63-9d155fa9f69a | -7.08033 | -44.39804 | 2025-07-01 12:06:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 8bd17d73-4883-3260-8c34-516b17958360 | -7.08171 | -44.38858 | 2025-07-01 12:06:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 1f5779e3-cbc8-3305-bbeb-58fcf7acfdc8 | -7.08308 | -44.3792 | 2025-07-01 12:06:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a691fee3-445b-3a70-b5fb-16fa85aa67d3 | -6.29182 | -43.67163 | 2025-07-01 12:06:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e4692128-1485-35f1-9a0b-d9f33b7c7257 | -6.28022 | -43.68851 | 2025-07-01 12:06:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| c9f21aaf-9618-3eec-8fb2-c6563bcdc739 | -5.10192 | -36.15813 | 2025-07-01 12:06:00 | TERRA_M-T | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 18.2 |
| c719d498-02bb-31c7-889a-97025370a657 | -9.11753 | -51.17397 | 2025-07-01 12:08:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 74bdc90b-d8b3-312a-949c-024b38824e7e | -11.14062 | -43.32323 | 2025-07-01 12:08:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| d02268e3-4f31-32c3-b354-abd1cb5bc866 | -7.8389 | -44.19582 | 2025-07-01 12:08:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 39.7 |
| a07f3c62-ea7d-3934-b691-49df9cdff846 | -7.70868 | -47.84554 | 2025-07-01 12:08:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b68b54b0-6be6-36ac-921e-6677bd76086f | -10.93248 | -41.77934 | 2025-07-01 12:08:00 | TERRA_M-T | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 5cf3ff21-adec-3863-8dbe-7c578dc3670f | -13.42247 | -47.8352 | 2025-07-01 12:08:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1a00441e-ba82-328d-9318-558089ec31b5 | -11.56365 | -47.45752 | 2025-07-01 12:08:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ce6b517f-0481-320d-97fd-93de544b20c0 | -9.57299 | -49.10714 | 2025-07-01 12:08:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| bde5bfff-0e56-3cca-94ba-0d9f0e806d35 | -7.72228 | -47.83236 | 2025-07-01 12:08:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| addbc347-d908-3603-8377-7c8150ca2baa | -12.02495 | -47.77502 | 2025-07-01 12:08:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 899f806a-3fec-3bf7-a020-5eb87afb4f4f | -12.43903 | -50.03279 | 2025-07-01 12:08:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| a6d121ff-f22e-338a-85cd-e68ebdf3d5ea | -12.01923 | -47.76746 | 2025-07-01 12:08:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| e7beb103-67e0-34c2-9ba7-2312525ca564 | -7.61809 | -45.76042 | 2025-07-01 12:08:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5383c4fa-56db-3213-b7f0-d2f538700f65 | -12.42675 | -50.0306 | 2025-07-01 12:08:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| a2bcb8c0-ab2e-38d2-9ea5-17dfe8d03b61 | -12.01726 | -47.78016 | 2025-07-01 12:08:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1280cd7b-207b-39e6-bc7e-e487e06764ed | -8.25511 | -44.94003 | 2025-07-01 12:08:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 2d28aad4-6254-32d2-b80c-0a576859fee0 | -11.56558 | -47.44525 | 2025-07-01 12:08:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 88fc06e7-9c73-34b0-a1ae-942fcdfa0979 | -7.82992 | -44.19448 | 2025-07-01 12:08:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 92bbeef0-efbe-3943-acf9-fea518fef2b6 | -7.6197 | -45.74953 | 2025-07-01 12:08:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 6a912b62-afe6-36c2-ac48-e21751b246c9 | -7.71995 | -47.84732 | 2025-07-01 12:08:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 3ea3bf99-4e7a-3acc-b12c-40024b4f7052 | -13.90163 | -41.29581 | 2025-07-01 12:08:00 | TERRA_M-T | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 18.1 |
| b27b5ece-417e-35d2-a597-89dab6bf25d5 | -7.83126 | -44.18537 | 2025-07-01 12:08:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 42.5 |
| c961ec72-0de9-33f5-9be9-b03647f83198 | -12.8123 | -44.89546 | 2025-07-01 12:08:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 09054325-d81e-318c-ab45-d9c9398d68e5 | -8.25368 | -44.94961 | 2025-07-01 12:08:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 4b3f6c93-d5bc-37d6-8315-5476de8d11cf | -7.0943 | -44.3819 | 2025-07-01 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 16a3c65d-f76c-331c-ad1d-12c029eb5bc6 | -17.29303 | -46.05521 | 2025-07-01 12:10:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7f9d4a4f-2d21-3089-864e-3a19f1e74bf6 | -15.41383 | -48.42078 | 2025-07-01 12:10:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c82d5333-eb5c-3877-a326-af7127dac5f4 | -14.13721 | -46.34497 | 2025-07-01 12:10:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| dc8a7e4d-0159-3c00-bcf5-1cba2aa33940 | -14.14904 | -45.47176 | 2025-07-01 12:10:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d083e6c4-4ea3-389f-a11d-20aa139656fb | -15.5822 | -41.06975 | 2025-07-01 12:10:00 | TERRA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 41dddc99-e5b8-37c8-82e3-0ea2cfdf5a6c | -15.41587 | -48.40792 | 2025-07-01 12:10:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 27.1 |
| d6d3eb0a-91cb-30f2-b8e4-04a748283a5e | -13.48297 | -52.95695 | 2025-07-01 12:10:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 29.8 |
| a0555936-f3ef-3de5-a8a9-9ec6c58e3a7a | -17.07867 | -43.14524 | 2025-07-01 12:10:00 | TERRA_M-T | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cb702a6d-a6a1-36af-a1fd-546624c7f552 | -14.86176 | -46.85199 | 2025-07-01 12:10:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e609d707-9b3c-3826-b265-696aeef31d50 | -16.30889 | -42.99078 | 2025-07-01 12:10:00 | TERRA_M-T | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ee94a183-5f08-3c54-be21-e030f4d4c68a | -14.20622 | -45.51874 | 2025-07-01 12:10:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7b38c311-3592-3c1c-a431-026206e04fb6 | -17.358 | -46.96408 | 2025-07-01 12:10:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3b147328-57ec-3017-b95d-cd89210f8a73 | -15.52696 | -46.98078 | 2025-07-01 12:10:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4f56f1f4-0010-3bc3-8951-756b2c3d42f4 | -21.46294 | -46.37019 | 2025-07-01 12:12:00 | TERRA_M-T | CABO VERDE | MINAS GERAIS | Brasil | 3109501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 02d758d8-e6d5-3418-8fdf-addd13c75700 | -20.66166 | -42.81781 | 2025-07-01 12:12:00 | TERRA_M-T | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 33d8818b-79ce-30c1-a228-7ea112baa50f | -18.41041 | -44.18146 | 2025-07-01 12:12:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 088d14da-1374-363b-9b78-3868fc0346d7 | -21.46432 | -46.36071 | 2025-07-01 12:12:00 | TERRA_M-T | CABO VERDE | MINAS GERAIS | Brasil | 3109501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 0e854d7e-0fd8-39f0-b9fd-ed411f4bef0f | -19.22328 | -43.75426 | 2025-07-01 12:12:00 | TERRA_M-T | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bd07a360-0028-3107-b62e-14ca7203e516 | -19.72907 | -45.02367 | 2025-07-01 12:12:00 | TERRA_M-T | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 67995587-9ff1-3aec-8b8b-cd62c65618d0 | -7.0943 | -44.3819 | 2025-07-01 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 14552609-c68e-3da1-b0f7-51e3adb24166 | -7.0943 | -44.3819 | 2025-07-01 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 389969b4-9c11-3235-a771-1eea83eaf05c | -7.0943 | -44.3819 | 2025-07-01 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 257.2 |
| 432f16a2-740c-3a29-a5f6-2c7cfc5a9071 | -7.7133 | -47.8453 | 2025-07-01 13:10:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 77adeb82-de40-3c8d-8882-58de39ba542e | -7.0943 | -44.3819 | 2025-07-01 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 97bd7a96-723e-319e-8edd-40ac4d2bf185 | -8.2356 | -44.9359 | 2025-07-01 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 181afb07-521c-3d4d-bc77-21559f0bacf5 | -7.7133 | -47.8453 | 2025-07-01 13:20:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a566ba1c-0d7f-3985-aa14-96666df54d8b | -7.7133 | -47.8453 | 2025-07-01 13:30:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |


[Clique aqui para ver as próximas entradas](README20.md)
