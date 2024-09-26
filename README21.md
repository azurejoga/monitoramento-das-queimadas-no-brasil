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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b82e296-a7a7-3778-bdbe-e5e347203bb0 | -11.8557 | -49.617298 | 2024-09-26 00:55:27 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9da98983-2c0c-3d77-8d0f-10be8190a37a | -12.8443 | -54.018002 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75fad4e7-4546-3b6a-a345-11660853000f | -12.8459 | -54.025398 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9917dc53-5cbb-3465-aafd-b6ae5c0efbdf | -12.8475 | -54.032799 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e42b1e6c-5e9c-3f87-af06-d5bab204c890 | -11.844 | -49.611599 | 2024-09-26 00:55:27 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd6ed5b6-3fb4-3f9e-8380-1cf8600c4bfa | -11.8459 | -49.619701 | 2024-09-26 00:55:27 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 80034876-c7ae-324e-af84-ad02dec0229d | -11.8478 | -49.6278 | 2024-09-26 00:55:27 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a073c2e6-9ac4-35bf-bca1-213f2e85c7fd | -11.8497 | -49.635899 | 2024-09-26 00:55:27 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0e27ece-c44f-3962-8491-0917fbd699d9 | -11.8516 | -49.644001 | 2024-09-26 00:55:27 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67aa080e-6f54-3722-9dcf-d05714c808fe | -11.8535 | -49.6521 | 2024-09-26 00:55:27 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8040bb2f-bdfb-3222-a658-5d6f92b13b51 | -11.8554 | -49.660198 | 2024-09-26 00:55:27 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6827a4f8-ccb5-3e64-bbb2-4f98c1436af8 | -12.8313 | -54.005199 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4738e557-e062-3570-aba7-ed51431ccdc7 | -12.8329 | -54.0126 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea64bc3a-2f94-3eae-bb21-bdd44a1bbec6 | -12.8345 | -54.0201 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f3011a8-9d03-3e8e-9458-32d243e06d90 | -12.8361 | -54.0275 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f86128d8-09bf-34b5-8c67-f6737ee4d205 | -12.8377 | -54.034901 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84eac2b9-e3b9-3844-9786-b2ce3c0cc665 | -12.8393 | -54.0424 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fcb7245d-c0ae-3de6-9c3b-1f8255727966 | -12.8215 | -54.007401 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e1e8e43-af25-3146-8f3c-5b23c59548b0 | -12.8231 | -54.014801 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 099f4108-067c-31fc-b836-e2caa1257221 | -12.8247 | -54.022301 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e646611-8a67-306d-a5f3-6c322e86b0df | -12.8117 | -54.009602 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1c898fa-ca6c-3192-ac88-2f6c7784f80d | -12.8133 | -54.016998 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32565422-0e40-3c8f-8aa6-d25014d8ed28 | -12.8149 | -54.024502 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 408fd4a4-f4a6-3cae-8e95-814b1688a5df | -12.8165 | -54.031898 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8f6e77f-6c23-3192-9aae-98690289e4b3 | -12.8019 | -54.011799 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25761ad8-2547-3fa9-8615-1fce5202f1bc | -12.8035 | -54.019199 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e05294c8-0f31-3b34-9912-9669c80a1e75 | -12.8051 | -54.026699 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1bbcdca8-af4b-3a55-ad74-4994f8055151 | -12.8067 | -54.0341 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 793267cc-bc91-3612-8301-16cfaabce201 | -12.8083 | -54.0415 | 2024-09-26 00:55:27 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 050d0fee-e6c4-3fc8-a34f-7de20e56f9cf | -3.8008 | -41.5989 | 2024-09-26 00:55:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| c1193d61-4edf-3f59-846a-31cfdc7fead5 | -3.801 | -41.575 | 2024-09-26 00:55:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 55.7 |
| 22d5376b-1486-38c0-b2a0-59346b5be088 | -3.9208 | -46.4459 | 2024-09-26 00:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 20e48041-9766-3180-9e36-3c3cd9ef9261 | -12.7937 | -54.021301 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8940cb55-1f5f-3cc7-b0f9-26837633b47d | -12.7953 | -54.028801 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4abaa28b-c702-3955-a64f-e6b867eda091 | -12.7969 | -54.036201 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27210a64-2011-357a-addf-4e3390d621fc | -12.7985 | -54.043598 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa90b399-21f3-3aa8-89c1-eb6dea92e568 | -12.8017 | -54.058498 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9129aed-2ab2-332a-aa8f-c90a0003bdcd | -12.8034 | -54.066002 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa56d7dc-7fd3-334e-a8ec-6645db70b6e5 | -12.805 | -54.073399 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 507e392c-89f4-31c4-8bac-47cbbdccf89f | -12.5951 | -53.1553 | 2024-09-26 00:55:28 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f828949b-6bcb-3884-90db-9b0652088c09 | -12.5967 | -53.162399 | 2024-09-26 00:55:28 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9bd3da52-5ec6-3a50-9fc7-35b8d476ae31 | -12.5982 | -53.169498 | 2024-09-26 00:55:28 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f2ef245-20c6-3f20-a220-a74901067c95 | -12.7855 | -54.030998 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27acf0b7-45f0-3a73-a197-58ab4ff4b52b | -12.7871 | -54.038399 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0eacd444-a796-33dc-a8c0-57600e397b12 | -12.5838 | -53.150398 | 2024-09-26 00:55:28 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 773dbe37-2a93-3811-8929-cf6d565cac3f | -12.5853 | -53.157501 | 2024-09-26 00:55:28 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de94b3cd-2dc2-3d16-b4bf-6b53ff7015ff | -12.5869 | -53.1646 | 2024-09-26 00:55:28 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5a9e10d-673d-3831-b625-d1d082b40919 | -12.7741 | -54.0257 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20405470-af62-3b48-9ba0-6e02edf63542 | -12.7757 | -54.033199 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02805b90-8323-311a-94d2-89d0db93ab67 | -12.7773 | -54.0406 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0bf76cb-ce5f-37c1-90c0-b2af3f47d431 | -12.5755 | -53.159698 | 2024-09-26 00:55:28 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dec2d255-e15e-3a45-9163-abc3861d3a5e | -12.7643 | -54.027901 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca6a2703-f3f4-33d3-b4ac-b2fdfa4d4bae | -12.7659 | -54.0354 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 88f25abf-a228-38c2-bdc3-6260857895f0 | -12.7675 | -54.042801 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f072e0a-695a-3d9b-b82e-4771b4a7b207 | -12.5657 | -53.1619 | 2024-09-26 00:55:28 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9691872-ecb0-33a8-a794-116c855af7b4 | -12.7545 | -54.029999 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d6fc29b2-1b5c-3841-90ba-19a5d782abbe | -12.7561 | -54.037498 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53d80c8d-9e79-32a0-9847-f827e32b5d81 | -12.7577 | -54.044899 | 2024-09-26 00:55:28 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe51cb36-a376-3c97-81cf-2d4affbb667c | -10.8028 | -45.888199 | 2024-09-26 00:55:29 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30851cc3-e07d-3d0a-a7ff-804ea9110e74 | -12.543 | -53.1521 | 2024-09-26 00:55:29 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10f21549-060e-35d0-816b-e9afeba333b3 | -12.5446 | -53.159199 | 2024-09-26 00:55:29 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10bbb0f1-1e44-381f-8a6b-5a18439b58f5 | -12.7429 | -54.071602 | 2024-09-26 00:55:29 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5d726cb-3a9e-3cb3-b2b3-09127f5a006a | -12.5332 | -53.154301 | 2024-09-26 00:55:29 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c450373-946f-3396-8cf7-27fc8734bc69 | -12.5348 | -53.1614 | 2024-09-26 00:55:29 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94a8d565-8311-339b-a86b-cb27ca074eab | -12.7315 | -54.066299 | 2024-09-26 00:55:29 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf39538f-8c2e-3b32-96f9-1d92c0cf2f7a | -12.7331 | -54.0737 | 2024-09-26 00:55:29 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92f0ecb9-8354-340a-b91a-89ccb8efea1d | -12.5265 | -53.1707 | 2024-09-26 00:55:29 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 709925d8-e2c2-3ee1-8ab5-dc7fc2f688c4 | -12.7201 | -54.061001 | 2024-09-26 00:55:29 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b3a5b67c-113d-3617-836f-6707d7082011 | -12.7217 | -54.068501 | 2024-09-26 00:55:29 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e4c499e-fccb-36b7-b44b-09bc9081f8fe | -12.5183 | -53.180099 | 2024-09-26 00:55:29 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 259fbbb9-7b66-3c2d-8e73-efcaaaf71bad | -12.5198 | -53.187199 | 2024-09-26 00:55:29 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a2e9751-594f-3c97-89ac-810bc18e393a | -12.7071 | -54.048401 | 2024-09-26 00:55:29 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ccff79a-ae86-3c0a-9ed2-7eb0f19a17aa | -12.7087 | -54.055801 | 2024-09-26 00:55:29 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9c52e14-3dc6-3da6-9f3e-c9cc272d458c | -12.7103 | -54.063202 | 2024-09-26 00:55:29 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db5b4d00-6616-3f2d-865e-5744d5de8c62 | -11.7321 | -49.883999 | 2024-09-26 00:55:30 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a13c7176-b66c-3fe7-a976-fef5096f4942 | -11.7339 | -49.891998 | 2024-09-26 00:55:30 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b008f155-f75e-3d74-845d-6daffd8a24f5 | -12.5332 | -53.483299 | 2024-09-26 00:55:30 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8cf04423-d34b-323c-ac3a-e8e90442f365 | -12.5348 | -53.490501 | 2024-09-26 00:55:30 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7879c267-cd1c-3b32-af33-187285b03b34 | -12.5363 | -53.4977 | 2024-09-26 00:55:30 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ee8ddce-6b83-3166-96f1-0871d48e827a | -12.5203 | -53.471199 | 2024-09-26 00:55:30 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f02ba79-d6a3-3eb0-b5df-f423133730f6 | -12.5218 | -53.478401 | 2024-09-26 00:55:30 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1127ae0-54f3-3dca-a918-896949c29f69 | -12.5234 | -53.4855 | 2024-09-26 00:55:30 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cabdb28a-f9e1-3c03-9b94-858f7dc73c5a | -12.525 | -53.492699 | 2024-09-26 00:55:30 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b883b533-9cdb-3f59-a0b2-916256f1552a | -12.5265 | -53.499901 | 2024-09-26 00:55:30 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b7f26e4-1128-32d1-bf59-1aa83f857852 | -12.5105 | -53.4734 | 2024-09-26 00:55:30 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce92a497-e7a5-32a1-bd70-0b398f07befa | -12.512 | -53.480598 | 2024-09-26 00:55:30 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e5a35980-b833-3888-a383-cc4fef0cc02c | -12.5136 | -53.487701 | 2024-09-26 00:55:30 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c1fa521-2f42-3a97-a684-6b47be087950 | -12.5152 | -53.4949 | 2024-09-26 00:55:30 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9598ed27-3432-300f-99ce-28fb7da5210c | -12.5167 | -53.502102 | 2024-09-26 00:55:30 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7dc29e9d-db5f-33e9-a1ba-e515d925e39c | -12.4991 | -53.468399 | 2024-09-26 00:55:30 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 796e26a8-6596-37a9-b364-b2ac5182e651 | -12.5007 | -53.475601 | 2024-09-26 00:55:30 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b77efa0d-c10d-3fec-9f21-af79c541ecbb | -11.685 | -49.903599 | 2024-09-26 00:55:31 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ffee26cc-9bbe-383b-8c7f-fc6545b27326 | -11.6868 | -49.911499 | 2024-09-26 00:55:31 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc7e155d-f3db-3264-96df-82b3ea45b123 | -11.5978 | -49.662102 | 2024-09-26 00:55:31 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd65138d-591b-3df9-a4ed-9719a0f4bf2d | -11.5996 | -49.6703 | 2024-09-26 00:55:31 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b181d28-cc1f-393a-acc0-8e0cfa63a17c | -12.6725 | -54.652 | 2024-09-26 00:55:32 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b397826-a232-378b-9621-91687fbd98cf | -12.6742 | -54.659801 | 2024-09-26 00:55:32 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c6f80c2-5259-359c-8b74-5ea874f7bef5 | -12.6627 | -54.654202 | 2024-09-26 00:55:32 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ac242fc-2907-35b9-9586-3a69b87a8559 | -12.6644 | -54.661999 | 2024-09-26 00:55:32 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec9cb29a-843d-3ab5-86c6-58396b74ef0a | -12.666 | -54.669701 | 2024-09-26 00:55:32 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README22.md)
