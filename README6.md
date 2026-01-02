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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcbe4a12-7142-3f02-b1f3-a363475107e2 | -14.49671 | -52.56017 | 2026-01-02 05:20:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d4291ba4-5364-3045-aee6-71a644d82b85 | -12.31517 | -57.36648 | 2026-01-02 05:20:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c0583019-51da-38a3-9b1e-76b3f9764867 | -14.50137 | -52.56373 | 2026-01-02 05:20:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9ab108da-ac48-3e2e-8593-d7584bba1c82 | -12.29606 | -57.3977 | 2026-01-02 05:20:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4dc0b0be-57e0-3ecc-87f5-f64a121eb1ce | -17.3844 | -42.6235 | 2026-01-02 05:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 662a3281-1748-3ab7-850d-edcfffb7c1b5 | -17.3844 | -42.6235 | 2026-01-02 05:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 77191baa-3d64-337f-9810-04b78753d1e7 | 3.13352 | -60.7238 | 2026-01-02 05:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d03347c3-265e-383d-8b8c-d5b05465a88f | 2.5456 | -60.36367 | 2026-01-02 05:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96f61fde-69f9-3f14-b9c4-19f4db1d9be6 | 3.13063 | -60.72826 | 2026-01-02 05:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a2c74fb-b1d0-3773-9824-158c975acc91 | 2.54919 | -60.36307 | 2026-01-02 05:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea6c9761-3b77-32e6-b757-cd481817c2ca | 3.13415 | -60.7277 | 2026-01-02 05:44:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a70e9b19-5f56-37e3-bef9-4b1a98b624ae | 0.40892 | -60.57775 | 2026-01-02 05:46:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d13e6997-db17-3440-af3d-047124ed4868 | -0.08897 | -51.28296 | 2026-01-02 05:46:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 25d7ee51-38bc-32f1-9fba-503146ee5c03 | 0.41489 | -60.56815 | 2026-01-02 05:46:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdce37d5-40de-396e-be75-9d15656fe7c7 | -0.08993 | -51.2769 | 2026-01-02 05:46:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2020be32-df79-3503-a685-0a90f56e44b5 | 1.81971 | -60.46947 | 2026-01-02 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19c8f1ef-027a-3951-9aea-6656967bfbc7 | 0.41556 | -60.57238 | 2026-01-02 05:46:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b88d48c8-d2a6-3ec3-b49b-6a0dc97f7ad6 | -10.92045 | -54.24955 | 2026-01-02 05:48:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 137191d6-9a59-3e06-bad3-d866dc38fe92 | -10.92636 | -54.24519 | 2026-01-02 05:48:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 867e0e27-405f-34fa-99ba-5bceee3bd8a3 | -10.92571 | -54.25078 | 2026-01-02 05:48:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33844afa-8423-3f50-ab02-d3057d295c62 | -10.91921 | -54.24998 | 2026-01-02 05:48:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c75fff91-7e3c-36f7-b22f-07a7f6cfb63f | -10.92764 | -54.24473 | 2026-01-02 05:48:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4c7881f-aa50-3ee6-a92f-f18bd2b3e82e | -10.92696 | -54.25031 | 2026-01-02 05:48:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50d561e3-95b2-39fc-b5ac-7e1bd9f23432 | -17.3844 | -42.6235 | 2026-01-02 05:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 78.8 |
| af81053e-959b-3088-81dc-f17399bb40b7 | -5.71764 | -45.03244 | 2026-01-02 05:57:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9d845c5e-8542-3c82-a1f4-abd597dacfd0 | -17.36409 | -42.63013 | 2026-01-02 05:59:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 9080ea9e-b83d-39eb-b215-f560fda408aa | -19.69505 | -42.6844 | 2026-01-02 05:59:00 | AQUA_M-M | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| d7368822-fce7-332f-883c-f6d46c6bb1c8 | -19.69309 | -42.69926 | 2026-01-02 05:59:00 | AQUA_M-M | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.9 |
| d5afb87c-e4be-3654-b140-daf15f866068 | -14.49493 | -52.55792 | 2026-01-02 05:59:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| d80f9905-6ab8-3d0c-bf8a-e31f5dba8e71 | -17.3657 | -42.61796 | 2026-01-02 05:59:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fe9c4172-c14d-303e-9b72-2541ce279864 | -17.37413 | -42.63158 | 2026-01-02 05:59:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 7608f3d0-8a1a-3268-a525-77b34deab042 | -14.45011 | -45.50004 | 2026-01-02 05:59:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a51ca4db-1512-37f3-be75-f81a5c915590 | -17.37575 | -42.61942 | 2026-01-02 05:59:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 53.9 |
| cea8f7d5-5ce7-366a-b446-6052ea81ea89 | -17.3844 | -42.6235 | 2026-01-02 06:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 87.4 |
| aaf168fd-22ef-32ae-a413-275f9ef37a65 | 2.54877 | -60.3632 | 2026-01-02 06:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39830da9-d9f4-3685-8077-0172557dde40 | 3.13338 | -60.7285 | 2026-01-02 06:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cca88885-7cd2-3cae-b4d7-2e74ea88e94d | 3.13393 | -60.73172 | 2026-01-02 06:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2517a035-e85c-3d56-9568-eef2f2bab390 | 3.13283 | -60.72531 | 2026-01-02 06:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 743df8e4-17a7-329b-ad8a-2b6080a246ce | 3.13358 | -60.72979 | 2026-01-02 06:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18596a6c-d3b9-35e5-9b86-f1a02ea96aa1 | 2.548 | -60.36677 | 2026-01-02 06:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60ccd3ce-6038-3422-a45a-1fe6559d4492 | 3.13306 | -60.72658 | 2026-01-02 06:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da8d03f2-fe81-3564-bcc2-ffd9254a12db | 2.54744 | -60.36335 | 2026-01-02 06:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81f05968-b0ff-37e0-8ff5-8f45418037f0 | 2.54936 | -60.36665 | 2026-01-02 06:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c2665cd-3b14-39e6-9683-73898ac0fd5e | -6.5631 | -51.1126 | 2026-01-02 06:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 2b97ca98-f0a7-3229-8953-2e64932068fa | -1.0809 | -47.9916 | 2026-01-02 11:40:00 | GOES-19 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 74b0a114-d935-3629-8581-b19b8fbe616f | -8.7025 | -38.6586 | 2026-01-02 12:10:00 | GOES-19 | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 110.3 |
| d6625ae6-b26b-3136-8950-fca05b45ebb0 | -8.7029 | -38.633 | 2026-01-02 12:10:00 | GOES-19 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 207.4 |
| 90025b36-9ce6-326d-9833-1e3b047ca7db | -2.89527 | -42.31368 | 2026-01-02 12:14:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 03682da8-54a4-3dd1-a614-1ce9d40fc3b5 | -2.3683 | -44.88724 | 2026-01-02 12:14:00 | TERRA_M-T | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 10838529-ab78-3f11-aa3e-07f157dcf34f | -4.78566 | -48.41844 | 2026-01-02 12:14:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 19c41139-97e0-3d3c-bc9d-769c7afc62c7 | -3.45667 | -42.32272 | 2026-01-02 12:14:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 51b1dd5a-2092-30c2-af6d-c5cf22837067 | -3.63015 | -43.86203 | 2026-01-02 12:14:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9225270f-64bb-358e-bc94-3bfb2b0e662f | -3.09944 | -41.98581 | 2026-01-02 12:14:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| d69fc167-36ee-3795-bfbe-39c3229320fa | -8.71323 | -38.63739 | 2026-01-02 12:14:00 | TERRA_M-T | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 303.9 |
| b92bd43b-3cc2-3fd0-9f67-78d350a71e9c | -8.71477 | -38.64291 | 2026-01-02 12:14:00 | TERRA_M-T | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 197.8 |
| c9bca9bf-efa2-3a54-adbf-3aab077c86cf | -3.48669 | -42.41813 | 2026-01-02 12:14:00 | TERRA_M-T | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| b8744bba-70af-3ba3-94f2-2cc21c034392 | -3.6682 | -44.81477 | 2026-01-02 12:14:00 | TERRA_M-T | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b432b4bd-2d71-3ff1-a04e-579f35171553 | -0.95851 | -46.93246 | 2026-01-02 12:14:00 | TERRA_M-T | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6287d6f2-765e-3ca0-bab6-b43cc7d177f2 | -4.65456 | -42.40975 | 2026-01-02 12:14:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 174ed52a-f65b-39ba-9775-c361b4a0e4a6 | -8.69737 | -38.64086 | 2026-01-02 12:14:00 | TERRA_M-T | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 82.2 |
| fd585a2b-27ea-30d1-993f-5d0bd12dd7f8 | -2.59324 | -45.41968 | 2026-01-02 12:14:00 | TERRA_M-T | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6ddea8cc-3032-30db-acd8-0e9ac3118062 | -12.42168 | -52.06323 | 2026-01-02 12:16:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0c80b83a-ad42-3b1c-9a46-39e14177cf4e | -15.98913 | -47.51274 | 2026-01-02 12:16:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 19133271-2f3a-3b89-b667-8828d5ef9128 | -16.66677 | -43.52613 | 2026-01-02 12:16:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 300d64ca-32a8-39f9-bf3f-880913439f15 | -9.90777 | -49.47992 | 2026-01-02 12:16:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 89a9d681-4f01-3027-a6b9-bbc10a0f184e | -13.08878 | -46.04342 | 2026-01-02 12:16:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5998661c-8b94-3281-a3cd-24a5b39105da | -14.44787 | -45.5098 | 2026-01-02 12:16:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 24a16da0-faf6-351a-9213-368945824392 | -14.44966 | -45.4951 | 2026-01-02 12:16:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 0b6df4da-8806-328d-84e0-27adec8ed26a | -12.4134 | -40.47256 | 2026-01-02 12:16:00 | TERRA_M-T | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 32.4 |
| c1015962-ef51-3cba-9644-4d853fc7b9de | -14.29086 | -46.68944 | 2026-01-02 12:16:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 3d223a3e-3dd1-30d7-9993-3bf48b58a02c | -29.03133 | -51.17234 | 2026-01-02 12:21:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 1f361c89-cab9-30db-9522-89f1242ea1d1 | -29.02994 | -51.18365 | 2026-01-02 12:21:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |


