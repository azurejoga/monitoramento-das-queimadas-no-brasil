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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69e4808b-4545-34aa-a50d-056ea226469e | -6.31091 | -44.3415 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f88e0ce5-a614-3cc6-92e3-a9df20486687 | -6.25206 | -44.14381 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4e9b873f-b8f2-3ff8-80f5-03940031c3c8 | -6.25143 | -44.14775 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 25cab369-7ac2-3641-89f0-75738704fea2 | -6.25079 | -44.15171 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0e1d697b-f126-3d34-8305-dd907e4802bc | -6.25016 | -44.15566 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c94d5780-3b53-34b4-b89d-f6c97df4fdd0 | -6.24918 | -44.13932 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| de8de518-8b96-353d-a420-631207dcb8e8 | -6.24855 | -44.14323 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0792cac1-a394-3ea2-8432-fbfbcda57cd0 | -6.24791 | -44.14718 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 18c1c8ed-5db5-3c63-811a-54ed96b79b2b | -6.24727 | -44.15118 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 893eebfc-abc7-3591-a579-8c497087ee57 | -6.24566 | -44.13875 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 1179bf58-d561-3f9b-b979-7a533374ae6c | -6.24503 | -44.14267 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 9e43fb46-9391-3bec-b26e-5dd40e57f73a | -6.07838 | -44.71471 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2303c7f2-d61e-3979-848b-3118a59a131a | -6.07703 | -44.71594 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| adff823c-db84-3fc1-b221-a865e69d2d31 | -6.07475 | -44.71416 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0369a2b8-d4a0-3a4b-b9cd-ffeebb19bcad | -6.06817 | -44.63256 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| a8328d01-7b26-3988-bd1c-294b66ef3f6e | -6.06749 | -44.63677 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a49e0957-35e5-3e32-890f-26f76fbd8db2 | -6.06456 | -44.63196 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 256b2921-498f-3f5b-bcf8-fd8d481f1c32 | -6.06388 | -44.63617 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 18d08070-ff03-3cec-8560-c8aee7b6976f | -6.0092 | -44.56341 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13017211-8d2b-3740-a74a-7ee305d4c297 | -5.42415 | -44.83185 | 2024-10-04 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e8721b79-6767-3b83-872f-01898d0c511f | -5.33324 | -44.83681 | 2024-10-04 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88ae1870-aade-310d-8565-44dec08bc898 | -5.31051 | -44.86014 | 2024-10-04 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 72c52ffc-7316-3a57-bf49-447790ef198a | -6.14518 | -43.82035 | 2024-10-04 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01d6fb22-5e0f-303b-882d-91bf1248de65 | -6.14456 | -43.82418 | 2024-10-04 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db5c07de-251e-323e-819b-75c8cc8ed419 | -6.14234 | -43.81596 | 2024-10-04 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 25f5e9f6-d01c-3298-95d8-eac0e08e87d3 | -5.89674 | -43.87636 | 2024-10-04 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b35abc9-fef1-3f80-83b7-dcececc0609f | -5.89611 | -43.88023 | 2024-10-04 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1328fe27-2cb3-3064-861f-8e0014d7a08b | -5.89388 | -43.87194 | 2024-10-04 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db2b37e5-f874-3cd1-a41a-a17fb696bcd3 | -5.89325 | -43.87582 | 2024-10-04 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1766fbbf-af88-3aec-91cf-c55f55fb82cc | -5.89262 | -43.87968 | 2024-10-04 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7ba1fee0-6223-32b9-bc80-42f0aef70ef7 | -5.89039 | -43.87141 | 2024-10-04 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 29b2a721-a672-3eba-93b6-b0f3494cb890 | -5.88976 | -43.87529 | 2024-10-04 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 48afd878-6acc-3cf6-8cdf-084daea05c57 | -5.85223 | -43.74345 | 2024-10-04 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a780dcea-127c-3c30-b6c8-4f2accaddec6 | -5.84876 | -43.7429 | 2024-10-04 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5d82afc1-6eb5-3cbf-9882-d25147943c20 | -5.84031 | -43.88395 | 2024-10-04 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 010c6ea2-5240-3c4f-9b45-cd85d0ad7c14 | -6.20824 | -44.32584 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6cab800c-e50b-3ecd-a696-654c053c14c1 | -6.2057 | -44.14058 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0750510b-6df5-3424-b70b-7907fa4d7335 | -6.20345 | -44.13219 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f871c60b-cdd8-329a-af60-e42e9fa8de92 | -6.20217 | -44.14008 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 04ef1117-6b0e-3751-8bce-9c01cb19a92c | -6.20113 | -44.32479 | 2024-10-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7b403fd3-91eb-38d4-a9a6-7646dca97284 | -6.19864 | -44.1396 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0d203758-aa92-36a5-903c-1c024c629b80 | -6.19576 | -44.13513 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 287d85b7-347f-3ea6-990e-88ff954308f4 | -6.18585 | -44.12951 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8db9b5f7-22c6-3b33-b6d4-1a8f36c6927e | -6.1852 | -44.13351 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f608a9c1-8344-3c76-8527-b39911f1b5dc | -6.18235 | -44.12889 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a7d6d8c-5c67-355c-9085-339d30fd1e2e | -6.18037 | -44.14091 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 55447de1-d90f-38c3-994f-c0b87b476824 | -6.1795 | -44.1243 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ea510035-2948-35d6-961f-de4a1ba10738 | -6.17753 | -44.13625 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65271f0c-93a3-30b8-aaff-a1a8f19025c1 | -6.17686 | -44.14032 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 468ac3d2-f4c6-3018-8dc9-37f613135e15 | -6.17402 | -44.13567 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30d2b967-6467-365c-b5c5-cfbe9ce86906 | -6.17335 | -44.13975 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3afaebc-b512-3e92-8a2f-caeae3e4d9ce | -6.16983 | -44.13916 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1dfbd86c-fe10-35fb-9b3d-e4fa9f021a42 | -6.16916 | -44.14323 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c4860bcc-71a4-34b0-8664-5e6c00a51eb0 | -6.16901 | -44.13997 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 86d84232-2e3e-3e05-80bc-c898ceffdde4 | -6.16849 | -44.14729 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7edd5d56-4a82-34eb-b1fb-8d2b649c078e | -6.16836 | -44.14405 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3c5d1b1-d531-3351-b7e6-78e4d1b64f90 | -6.16771 | -44.14811 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 575be610-c8cd-321c-8995-310910c524e0 | -6.16199 | -44.1387 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f479c65-bd7b-3f7b-9ae3-02f633b9d1a5 | -6.15912 | -44.13408 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 643c68f5-bc9c-30de-b4de-b02a7f039d23 | -6.15432 | -44.14155 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92b329c1-3e05-3beb-8153-f91ee078b7e6 | -6.15081 | -44.14094 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c21e73d-b4b4-3d21-9ba2-933057df1504 | -6.15016 | -44.14499 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96f18882-20a6-3ff4-ad07-242ec8f74516 | -6.14665 | -44.14434 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1db6bb99-3a99-3457-9535-dccdbda32e89 | -6.14599 | -44.14844 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8ca1e24d-a130-39b4-8ed6-2bf3c8d93a20 | -6.14442 | -44.13574 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fd576b3f-0014-3934-8d13-ebfa5a3797bc | -6.14378 | -44.13975 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bfad99f-443c-31b8-a3be-2a4413d46654 | -6.14313 | -44.14378 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4e7d946-32a8-3b05-9dee-78a07b34237f | -6.14248 | -44.14787 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| eeb09b7b-cd79-3a04-b5c8-a79edcbfc088 | -6.1409 | -44.13519 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 15c1111f-c2cd-3991-b308-8e93abb7af71 | -6.14026 | -44.13919 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02b27af2-0192-31a3-979c-2f0b9f666a9c | -6.13961 | -44.14323 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c3da8ad-3a21-36e7-99a0-f24be3746310 | -6.13895 | -44.14731 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40aaff2b-9c4f-35bf-b094-dd1257fbc88d | -6.13609 | -44.14268 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c84ffbfa-6944-32f5-8ffc-3b43a4d55c0a | -6.11436 | -44.05421 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eebb6302-9f2d-3210-88ed-4600c654f0d6 | -6.11374 | -44.05804 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15116fb6-da90-329d-ba24-b768e99d864c | -5.97292 | -44.00422 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ec07816-a465-3025-a6b4-05a061454415 | -5.97231 | -44.0081 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96a800be-09ad-3a12-a78e-b65a356e01d5 | -5.97068 | -44.00306 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6e7db80-c38c-31a0-b268-841c150eb8c0 | -5.97004 | -44.00695 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4fc934b3-17a1-3501-94bd-25aea665f36b | -5.96942 | -44.0037 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb32041f-a611-36ff-b0e3-2b64186850d5 | -5.9688 | -44.00758 | 2024-10-04 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 348abd52-f036-3538-a228-48974d76d253 | -5.82985 | -44.12861 | 2024-10-04 04:08:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d3fa0265-842f-3631-a73d-dcfcc8f5f6be | -5.82632 | -44.12803 | 2024-10-04 04:08:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c7188621-6a5b-38c6-b3a7-3240bd737e38 | -5.82569 | -44.13201 | 2024-10-04 04:08:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 34825f53-c890-3d96-8031-8a614eb66001 | -5.82343 | -44.12349 | 2024-10-04 04:08:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7730c982-617a-3b97-a027-2f0ca253ae83 | -5.8228 | -44.12746 | 2024-10-04 04:08:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b6743d2e-9b00-3f9b-acdd-a367d6fadc17 | -5.82216 | -44.13143 | 2024-10-04 04:08:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| eab9fd7b-b666-33c5-abf2-c4142c6fa858 | -5.8199 | -44.12294 | 2024-10-04 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ef06012d-460b-32d0-89e1-e6f24f590a21 | -5.81927 | -44.1269 | 2024-10-04 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a936a2cb-701b-380a-bb6c-3ef04248d08b | -7.87747 | -44.95584 | 2024-10-04 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95d5720b-bb39-383d-8af8-a0883112c147 | -7.87388 | -44.95527 | 2024-10-04 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9cc0c34-b3d1-39dd-a4b2-8ce2bdd22ff7 | -7.86801 | -44.81104 | 2024-10-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 875c9087-c6b5-357c-a5b7-1a8ec901dc29 | -7.86511 | -44.80641 | 2024-10-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cd83fdd0-79a4-3241-9582-d849130e91a3 | -7.86445 | -44.81044 | 2024-10-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 954228b4-5114-345b-85e1-9628f576edc1 | -7.85293 | -45.33703 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d26f2bff-bb19-3c0b-ad51-d4ee0d1aaada | -7.85148 | -45.34567 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 04ecc9db-ec1b-3f73-8de3-e7a793dae876 | -7.85076 | -45.34999 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c074dcc5-aef6-3f69-95d5-9afbbe9ad1ac | -7.85004 | -45.35432 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f2ef9169-1b36-3233-9095-32b2201ae05c | -7.84932 | -45.35867 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1f93e197-fa78-3d2c-8c6f-b1f23cfc817e | -7.84638 | -45.35372 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |


[Clique aqui para ver as próximas entradas](README60.md)
