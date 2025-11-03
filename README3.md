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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa2cf2db-bd39-3efd-9531-ef3b477bb60b | -2.79368 | -43.34669 | 2025-11-03 03:59:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1da214c2-18be-37f8-9729-30088bd5d403 | -7.03911 | -43.16774 | 2025-11-03 03:59:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c1386374-e05c-30ac-b6aa-c5b76463083d | -6.84796 | -46.29206 | 2025-11-03 03:59:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae3a1116-bf7e-3ae5-a334-bf390a7535a8 | -3.43264 | -45.90329 | 2025-11-03 03:59:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 94989e10-018b-3bb5-9825-a6f8712f5712 | -7.0876 | -44.98115 | 2025-11-03 03:59:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16eb1171-e4ed-3598-8e81-081a1a0e6bca | -5.03296 | -43.61782 | 2025-11-03 03:59:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 19289328-5fe1-3820-a775-8078bf576edf | -5.43375 | -46.36601 | 2025-11-03 03:59:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c2e548c-2b94-342f-bb75-84d5f73dfdb0 | -6.70885 | -40.83661 | 2025-11-03 03:59:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f074714b-4f08-34c8-929e-f6bd5777a483 | -5.13197 | -40.62645 | 2025-11-03 03:59:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 42c39a5d-21b8-3549-9582-b5e5a60725f0 | -5.52802 | -41.09038 | 2025-11-03 03:59:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2030b7d4-794b-34a6-9485-b788635a9787 | -6.10055 | -41.72663 | 2025-11-03 03:59:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 43f2f8df-fcbc-39fa-9ff5-854310828d10 | -3.95731 | -41.82645 | 2025-11-03 03:59:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 598539e1-55f0-3562-8a06-7ff038c3b968 | -5.08358 | -40.54604 | 2025-11-03 03:59:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 28838055-9c17-3f67-955d-536c7f10d06b | -5.72168 | -42.18536 | 2025-11-03 03:59:00 | NOAA-21 | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d12dab8d-28bc-3ca4-84d4-c294a03af103 | -5.03983 | -43.62368 | 2025-11-03 03:59:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 1766c164-0f9b-3104-991d-e7267224b38e | -4.62427 | -40.76072 | 2025-11-03 03:59:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f64a8ef1-d887-3432-95b7-fe8063b90d41 | -4.21744 | -44.23116 | 2025-11-03 03:59:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bcaebf0-cd2e-3793-9da4-526ca834fed3 | -6.68785 | -46.67289 | 2025-11-03 03:59:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce4f7ca4-3e84-3c98-90ef-ae1ef7b02c69 | -5.03525 | -43.6278 | 2025-11-03 03:59:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba0579ca-a6d4-3625-9389-3b5782bce4a6 | -2.31524 | -48.58353 | 2025-11-03 03:59:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e158f596-812d-3588-9b37-1e4cc650b8a6 | -3.81922 | -38.51974 | 2025-11-03 03:59:00 | NOAA-21 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e3fa1cca-d1e2-3761-9214-ad6e75e9cdd7 | -3.82253 | -38.52025 | 2025-11-03 03:59:00 | NOAA-21 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 881f0734-2ba8-3a11-980d-6b292b393fdb | -6.89648 | -40.40123 | 2025-11-03 03:59:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8750c76b-0be4-30aa-a2ae-fcc95c240cb6 | -5.68564 | -38.59268 | 2025-11-03 03:59:00 | NOAA-21 | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 991de67f-0291-3d2d-a6ee-729902268c35 | -3.17745 | -46.57972 | 2025-11-03 03:59:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a00dff7d-ccde-392c-907e-c8d1119cbbc3 | -5.78392 | -40.80848 | 2025-11-03 03:59:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ae9511dc-eaf5-34ad-ba42-2fc75952cd89 | -3.24044 | -50.79266 | 2025-11-03 03:59:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bdd16204-14bb-391c-b6db-8cfd56ff147d | -3.17693 | -46.58125 | 2025-11-03 03:59:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d31a4aa2-c70f-3e2f-91de-d53526494016 | -5.7895 | -40.81649 | 2025-11-03 03:59:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b6ac73ca-9029-3dbe-9de1-b755059bab04 | -3.2396 | -50.79767 | 2025-11-03 03:59:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f8a4452f-602c-352e-9c81-136e8c4b852f | -6.68332 | -46.67207 | 2025-11-03 03:59:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 476635ba-c9c2-31f1-9168-1fda98e6c522 | -3.42804 | -51.02832 | 2025-11-03 03:59:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a305ed4a-161d-3c23-83e8-ee9a9e92fd1d | -7.05249 | -39.47439 | 2025-11-03 03:59:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| acffabd2-5533-3adf-b38b-575efb9595e6 | -1.97127 | -52.10786 | 2025-11-03 03:59:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 477443ad-3fdd-3a12-bacd-097234f6d3be | -3.4281 | -45.90255 | 2025-11-03 03:59:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6bedaa1d-b169-36cd-a10c-d1a149c9a1d1 | -4.30344 | -41.4541 | 2025-11-03 03:59:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d8d68601-921a-3d30-b6b4-8ffae3965f11 | -4.218 | -44.22765 | 2025-11-03 03:59:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b02336a4-cabe-3f63-8bf8-6fe58de1a278 | -3.17214 | -46.58055 | 2025-11-03 03:59:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4c99200-6288-308a-b3a7-edce90b4efc2 | -3.01736 | -49.44242 | 2025-11-03 03:59:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c5e8d83-47cb-3335-ae3d-ab015b52acd7 | -7.23605 | -45.06582 | 2025-11-03 03:59:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46e58a58-360d-3bfa-b409-4c734d254028 | -2.48986 | -48.15028 | 2025-11-03 03:59:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c32f5a72-6985-3499-807d-0794a3ce1c2e | -2.49801 | -48.15118 | 2025-11-03 03:59:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f448535-dd2b-3d88-9e24-cba23e9a2326 | -4.65514 | -42.52193 | 2025-11-03 03:59:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bfe20086-9c0f-3104-872d-76a4e6ba928f | -7.96472 | -39.62129 | 2025-11-03 03:59:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8eb67bbf-359f-3374-9869-17c09fc3b03e | -3.63006 | -45.23241 | 2025-11-03 03:59:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 445302d4-c231-35ff-84cd-b9d230bb319c | -3.95817 | -41.82665 | 2025-11-03 03:59:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7f2b122c-5ac4-3bde-bb0a-6d21a118ab0a | -2.31463 | -48.58731 | 2025-11-03 03:59:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1bf609b-039b-3d8a-8099-84d9d0dc8053 | -3.24589 | -50.79881 | 2025-11-03 03:59:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d8bc603-bbef-3335-9174-29ab06110afc | -4.96554 | -45.5139 | 2025-11-03 03:59:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14e62868-e531-32f2-8a1c-36417dd1c80b | -4.29999 | -41.45363 | 2025-11-03 03:59:00 | NOAA-21 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0ac6e659-0652-3155-8e2e-f7f930254937 | -5.78448 | -40.80497 | 2025-11-03 03:59:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 232a646e-ed42-334f-ac1a-92b46625f6ea | -6.10115 | -41.72286 | 2025-11-03 03:59:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ab24455f-9551-30a4-9885-51fe87906948 | -3.43053 | -51.02795 | 2025-11-03 03:59:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28eb7af5-7e85-3971-b547-2c2586ed870d | -2.31409 | -48.58691 | 2025-11-03 03:59:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6aae2353-eee3-3899-aab9-6dff8982f0fd | -3.2062 | -43.24109 | 2025-11-03 03:59:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f14da65-1552-3587-beeb-c49b9f162ae3 | -2.53211 | -45.28475 | 2025-11-03 03:59:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7bc90c5-1204-33e8-9088-5fb1dabf831b | -7.62287 | -43.63456 | 2025-11-03 03:59:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 878cb4fd-0a4f-3475-83ff-8a77d064f657 | -6.68253 | -46.6767 | 2025-11-03 03:59:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a8e4c85-4ed0-39be-bbd0-08c5c47aeec3 | -2.90918 | -40.24044 | 2025-11-03 03:59:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aaafd3e1-6421-3040-9b3b-fc70d454f61d | -2.9426 | -51.41333 | 2025-11-03 03:59:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a2b230c-b426-30f2-be06-51e704023cc6 | -1.97021 | -52.11078 | 2025-11-03 03:59:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eacd7a17-669b-35cf-8d0b-a7085ea39f03 | -5.07141 | -40.47207 | 2025-11-03 03:59:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1631ab38-4ec7-3058-b7f7-7445af90733b | -4.96488 | -45.51796 | 2025-11-03 03:59:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed5aef2a-6e27-3aef-859a-7ab89bfafcf3 | -2.4958 | -48.14783 | 2025-11-03 03:59:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2013e4db-8f65-3e2c-a559-fe161feca925 | -7.54352 | -39.02575 | 2025-11-03 03:59:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7dc8c307-e18c-3dc3-a1c9-f2277090b0f9 | -7.04771 | -43.16056 | 2025-11-03 03:59:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 42fc715e-1caa-311e-9369-d1a214426cdb | -3.17658 | -46.58488 | 2025-11-03 03:59:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8760c65-7b64-3461-87ec-d9de2e3bc92f | -2.49264 | -48.15026 | 2025-11-03 03:59:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4f80ffb-2753-3495-bd6e-eb7ac53ea9d2 | -2.2695 | -47.86108 | 2025-11-03 03:59:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed98ee66-44a0-3367-a449-d69b5e2817ed | -3.0173 | -49.4416 | 2025-11-03 03:59:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef5cf634-8365-3500-8036-7447de2260a1 | -2.29064 | -47.86465 | 2025-11-03 03:59:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1496a026-8b34-3863-aafb-890ec0de7eb4 | -5.31995 | -45.33796 | 2025-11-03 03:59:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3af9bc49-5600-36ba-9e3f-bfeb0e8f208f | -3.9202 | -44.31722 | 2025-11-03 03:59:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb056e81-909c-3761-8268-aeca1cc10b72 | -5.03678 | -43.61841 | 2025-11-03 03:59:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| c6d3a174-2bd1-35df-9eb0-14b762c37c3e | -2.49522 | -48.15124 | 2025-11-03 03:59:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c893eae0-16bb-3f94-8a53-9088e0411fe3 | -7.23699 | -45.06592 | 2025-11-03 03:59:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7625870e-175c-380a-90f4-57799c90422f | -4.21947 | -44.2291 | 2025-11-03 03:59:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fe4ce64-30a7-3483-a20c-3d12b66f8007 | -5.0866 | -44.20404 | 2025-11-03 03:59:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c3e1cdf-8321-3be0-baaf-55cd49825ca0 | -5.0322 | -43.62253 | 2025-11-03 03:59:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 466a6764-6079-39d3-b8a7-dff270622810 | -3.24354 | -50.79491 | 2025-11-03 03:59:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dad0038b-e548-3cbb-9e6c-d9e880db1db3 | -2.27002 | -47.85786 | 2025-11-03 03:59:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63b9bead-70dd-3eb4-9447-454b5f112391 | -5.03601 | -43.62312 | 2025-11-03 03:59:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 664a5932-6630-31fb-b94e-7e69fc135b18 | -2.52757 | -45.2826 | 2025-11-03 03:59:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ac6bbad4-42d0-31b9-b7df-da04ad9452c0 | -1.96323 | -52.10986 | 2025-11-03 03:59:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4adb83f-db97-3276-bf27-f3cbf00bbdbd | -3.24441 | -50.78991 | 2025-11-03 03:59:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da7c8ccf-7e5c-3aca-a728-9c5118dee444 | -4.62763 | -40.76122 | 2025-11-03 03:59:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9db6babf-5a4b-3fdb-b6a8-e12d11c6b13d | -5.20428 | -37.6567 | 2025-11-03 03:59:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 12ffad98-1a77-328a-850b-a2f1bcbfdc45 | -2.52769 | -45.28405 | 2025-11-03 03:59:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4e772a52-0f80-3e1d-a94d-0883e68ae740 | -4.65875 | -42.52249 | 2025-11-03 03:59:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 88ddbc78-18db-36ed-85c9-201f2ca5cfa8 | -5.40084 | -46.05344 | 2025-11-03 03:59:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7eb70e15-6eac-3de0-91de-48aef7cbc5fd | -5.0399 | -43.6205 | 2025-11-03 04:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| a61dbdb4-d5d8-3a0a-9cba-0ec1a3ce10e0 | -10.40519 | -44.35743 | 2025-11-03 04:01:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 98676c91-3ece-3771-809e-d1fa2523d10b | -14.8776 | -43.55617 | 2025-11-03 04:01:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a1b06f7-217a-3f70-8cc0-c0ec0899b317 | -12.68417 | -41.57142 | 2025-11-03 04:01:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 71437e76-95ed-372d-90f3-d2c598cd5e4a | -12.40424 | -46.63227 | 2025-11-03 04:01:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a13d70e-f664-32a6-bbb2-7f62c57a1a53 | -11.41895 | -44.67879 | 2025-11-03 04:01:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87161276-3de2-364f-9f03-691c364416b7 | -14.97219 | -39.40821 | 2025-11-03 04:01:00 | NOAA-21 | ITAPÉ | BAHIA | Brasil | 2916203 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| e0a180fb-151c-3a65-9bd5-40d6fa0685fa | -9.39742 | -40.59993 | 2025-11-03 04:01:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1cbb2760-2cb2-317d-a1f8-41756b790118 | -8.43663 | -45.61455 | 2025-11-03 04:01:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aee2ff53-2fb4-3b40-a03b-3a30bb6a97b3 | -12.24901 | -43.07936 | 2025-11-03 04:01:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README4.md)
