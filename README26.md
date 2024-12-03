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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55a2f7c4-2c2b-34a7-b1f3-73e9d7e49a67 | -5.58317 | -45.1447 | 2024-12-03 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94c125f0-cb0f-329b-a93a-9aa974245562 | -1.36502 | -47.68657 | 2024-12-03 04:06:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bdec273-408e-3b8c-9ae3-3dbb8957b074 | -4.04121 | -46.93426 | 2024-12-03 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4159863-10b8-389a-ba07-bf73435afcca | -1.80066 | -46.65344 | 2024-12-03 04:06:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 55b9dd46-bc72-3f2a-adef-67392da2e084 | -4.07021 | -46.67657 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cb32df6-9f87-3ed1-89e8-231d5decebc3 | -1.9435 | -45.81744 | 2024-12-03 04:06:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce43a76a-bd29-315c-b3d6-cd37e7b17776 | -3.69976 | -51.83401 | 2024-12-03 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08f2c935-401a-349d-9652-e354b9c98604 | -3.28472 | -50.32647 | 2024-12-03 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83978643-ca75-3b7b-b2f8-53a75a87b503 | -2.92734 | -49.43491 | 2024-12-03 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 927d241a-befa-317c-b51a-c6963a6fe879 | -3.16104 | -41.85037 | 2024-12-03 04:06:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a3db020-bfb1-3ecf-9851-1e97dfcfdcc2 | -3.3461 | -51.20816 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a57d904-41fe-304d-812c-6e4cb865dbaa | -1.08081 | -53.44884 | 2024-12-03 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 99bb386e-17c1-3bb7-a981-c55831171bec | -2.96026 | -39.96279 | 2024-12-03 04:06:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 3e81bd95-d466-3218-82cf-2174b3936100 | -4.17073 | -48.61401 | 2024-12-03 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9af353e-03a6-3e8b-80e9-9a0a30da0384 | -5.46616 | -35.55249 | 2024-12-03 04:06:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 301b6867-03d3-3a7d-9d78-2c146b5f67a1 | -2.61636 | -46.88556 | 2024-12-03 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c665355-933d-375b-8313-e3cd5e4b50a6 | -1.79559 | -46.65697 | 2024-12-03 04:06:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7c59dcb1-ca54-3e4a-b233-18c513b2496d | -4.74024 | -45.7106 | 2024-12-03 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 23e9cd5c-3273-3432-b47d-a1739672dc03 | -3.54516 | -50.18115 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eba51bf9-d19d-3cd1-8ba3-979c4c1a4be6 | -4.05968 | -46.82107 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 009a9c61-2734-3a0d-b19a-ac46088813c6 | -5.79759 | -46.47563 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e75fc9d1-a5c8-36e5-8898-7341b2287be9 | -5.81449 | -46.47459 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bae89eb3-b730-3ead-a722-3de0ed2c0a1b | -3.26715 | -53.62492 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dbfc7323-160d-3dab-ae4d-ced448ffd773 | -3.25265 | -53.6343 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbd7560b-2b07-3c88-9236-eb7c30649af0 | -5.79699 | -46.47922 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e8faa617-a476-3cf4-b5c5-6846688d0b5b | -5.45331 | -43.57946 | 2024-12-03 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94a1ae1b-6572-3759-a3a7-da1c37cadc70 | -1.75916 | -52.80293 | 2024-12-03 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d81ab459-1825-327d-9080-a579e128abaf | -3.17536 | -54.33801 | 2024-12-03 04:06:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 68e77d46-b1ca-3878-b429-3b01f46190f5 | -5.81509 | -46.47101 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4ea4bc06-80af-30d8-ac89-762c8349daad | -2.21038 | -53.78587 | 2024-12-03 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e846a3a3-83d4-34e9-b117-671f513dcffa | -3.17651 | -54.33117 | 2024-12-03 04:06:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07d0aacb-9577-3778-af73-a634fb678423 | -3.90317 | -46.66639 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0435266-f5b3-3eb0-8fd3-0af4bdf37f56 | -3.66761 | -50.19623 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4168ef1c-ef6f-3f6c-9896-f7ad906da80c | -2.85154 | -45.38935 | 2024-12-03 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c5bebe3f-fa88-3084-9a05-902bc3989c55 | -5.12034 | -43.21222 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1ee147df-9eed-33ef-baaa-2eb16c9f5aca | -2.66196 | -46.09841 | 2024-12-03 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2015b62c-0400-324d-ac9c-14b7836ba3f6 | -2.65417 | -46.12024 | 2024-12-03 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3465e6fd-c571-363b-8c27-020ea3016e8b | -4.05277 | -46.99966 | 2024-12-03 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f360b427-0128-335f-bfbd-183bfb040ded | -1.69966 | -52.60512 | 2024-12-03 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 994792bd-0d83-3d7e-a6db-e8b21e9b8b4c | -3.53571 | -50.17913 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cdad04b3-eee3-3a00-8f54-f3b4a83cb92e | -3.97016 | -46.62986 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 47bb0b7c-f5b2-304b-94b3-635666e19769 | -1.74786 | -52.78948 | 2024-12-03 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75093438-b89a-3487-a7a8-dca60703a8a5 | -5.63687 | -47.3732 | 2024-12-03 04:06:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42812345-3869-3eea-9018-4ccdaf290415 | -3.28402 | -50.32968 | 2024-12-03 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab310f3e-a705-358e-b1cc-a50a7ad4e4fb | -2.81868 | -53.05619 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1a341e3-68de-3418-a2a5-1e90361f467e | -1.84143 | -46.23687 | 2024-12-03 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 167c5231-b288-3ccc-84f0-a03981bd3b52 | -3.7577 | -48.15676 | 2024-12-03 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad0712f4-cad0-32ca-a852-97a90dbee50a | -3.26645 | -45.37181 | 2024-12-03 04:06:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38a7fac7-1e07-361a-9e0b-3594938dffdd | -1.51022 | -45.90931 | 2024-12-03 04:06:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 619f4eee-b816-39cb-80cd-e48fe0714e45 | -3.52255 | -45.00988 | 2024-12-03 04:06:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cc4f9bd-2ef8-395f-9ece-9b86633df80e | -3.07771 | -53.38384 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4ce016b8-cfc0-3d0f-b274-4ee9a32b7347 | -3.53431 | -50.17923 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f456c047-c1cb-3850-a49a-1d9398f053a2 | -5.80107 | -46.47984 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| e3733680-23b6-35df-87ad-54f1ebd41e96 | -3.12739 | -45.99361 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d707fbae-368e-3dc9-bb9d-5890f6ded1cb | -2.64999 | -46.11958 | 2024-12-03 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 598eb980-9d93-3d9a-8588-50e7f007ad36 | -4.16617 | -48.20163 | 2024-12-03 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 65adf6e5-6815-3ce7-ab9d-453049a61ddf | -3.85474 | -46.51584 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54670d9e-4868-355b-8da9-3cc13ded3ba0 | -1.08608 | -53.45678 | 2024-12-03 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| f8325a14-3905-31a5-b121-de6e15908607 | -3.34329 | -46.04625 | 2024-12-03 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| edde9d76-5aa8-348d-9f79-527d17113d5e | -4.82404 | -43.43132 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 351a0dea-7e3e-3968-893e-e3a7ac85074a | -3.75364 | -48.15738 | 2024-12-03 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c799123d-0f06-3fa3-b094-767f2ad420d0 | -3.37878 | -51.01585 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 036a308b-1889-3c25-878b-84dbd5e9ff6e | -5.80634 | -46.47331 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 977b4a46-1c75-3779-824d-014fbac06ce4 | -2.81199 | -53.04464 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b4ed9b1-6528-342a-bbac-e25d92f7e405 | -5.14547 | -43.23172 | 2024-12-03 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8020abbc-530b-31f3-8684-522ab69b5978 | -3.19806 | -46.36218 | 2024-12-03 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfeb0aa8-eb65-30f9-8a6e-c4214a8e617a | -3.37604 | -45.8413 | 2024-12-03 04:06:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d290f508-49d0-3761-bf1c-fd8e3daf3ffe | -2.68688 | -46.616 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a34495c2-90e4-3a47-9e07-dbb8b553f778 | -3.76465 | -52.08145 | 2024-12-03 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3b35f23-8690-3eb2-b76c-ccd52f4db166 | -3.34511 | -51.21825 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| addcb32c-b54e-34bf-987d-451ca1575253 | -4.56639 | -46.62751 | 2024-12-03 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23b4b4a2-faca-35dc-b14e-62f6f5d5a92e | -5.42149 | -46.11541 | 2024-12-03 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 537cfc61-91bf-3c3a-bbf0-8d070c671ec0 | -2.32966 | -45.86292 | 2024-12-03 04:06:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fda44152-93e7-350c-8fe4-dc7be8e00558 | -4.18642 | -51.19201 | 2024-12-03 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a3bc99b-1981-3199-b691-1f719552a686 | -3.26038 | -53.62372 | 2024-12-03 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f2a8d52d-72f4-39dc-8588-4567c1dfbab4 | -5.81042 | -46.47394 | 2024-12-03 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1cd3dc73-a856-34a6-92b2-78603bb89e69 | -5.73791 | -44.43146 | 2024-12-03 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c484077-cf2a-3b2e-871e-0b2f7ce22e55 | -6.03649 | -44.03629 | 2024-12-03 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ccf67c8-16be-35e5-81ed-12937ff5f403 | -1.07977 | -53.45536 | 2024-12-03 04:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| fc7f12fc-4561-3abe-944d-e61216413303 | -5.44994 | -44.82475 | 2024-12-03 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 94ab1e3e-b4b2-38cb-a08d-4df9017b0430 | -5.5364 | -46.45058 | 2024-12-03 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff553703-91ec-3a60-8b00-6c4304525d11 | -3.92425 | -52.38959 | 2024-12-03 04:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f923b393-9194-3108-9917-2750bcc0bc1a | -4.48794 | -46.02922 | 2024-12-03 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5b5a45c-393d-3b0d-b06f-e915d7a6b760 | -4.7497 | -45.11451 | 2024-12-03 04:06:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9d1ce5ad-6c78-302d-b773-0da024acba16 | -3.10139 | -40.08096 | 2024-12-03 04:06:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 599ebf07-c563-3249-a5af-d3f6ecc26a1b | -3.28464 | -50.3261 | 2024-12-03 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72558d6a-25db-30af-a867-3ea0110e91e9 | -3.35048 | -51.21743 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fa73362c-92ea-38fa-8a23-fd22739c0672 | -2.66796 | -46.59625 | 2024-12-03 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8431fa1e-8396-34aa-a4da-8fe8f86383bf | -2.51989 | -47.06664 | 2024-12-03 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7796305-cf7e-3531-848c-a772bd2abc27 | -2.12699 | -45.3437 | 2024-12-03 04:06:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1a5ead56-4592-34c0-b8e1-837214dbcc30 | -3.84775 | -46.55812 | 2024-12-03 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9946c319-5204-3f9b-9865-226e8fdef13b | -3.64737 | -52.64114 | 2024-12-03 04:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6dead1d8-6fdb-396e-aac6-f156e242721d | -3.54595 | -50.18456 | 2024-12-03 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4f2c0578-9611-3736-96fd-1a48558bbe52 | -2.3318 | -53.81236 | 2024-12-03 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cd7deee9-7654-3679-961d-f02fcc4e09cb | -3.7005 | -51.82956 | 2024-12-03 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9f4302b-014c-3283-b5d8-cfc31b62f400 | -3.75753 | -48.16298 | 2024-12-03 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb89b7d6-4be4-36fc-ab8f-bf74a8decea3 | -1.75164 | -52.80744 | 2024-12-03 04:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad6f599b-c828-301d-9e6f-7afe59ba10a5 | -6.18272 | -42.61999 | 2024-12-03 04:06:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1c06d3be-f8cb-3023-9b03-16358a494698 | -3.46613 | -41.99943 | 2024-12-03 04:06:00 | NPP-375D | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a00f1cf4-c34c-35b0-99b8-84408225a6fa | -3.0976 | -53.23224 | 2024-12-03 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README27.md)
