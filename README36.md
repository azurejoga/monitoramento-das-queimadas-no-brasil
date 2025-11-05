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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64fb013d-2c14-3bad-8df4-e55d1fb423fc | -4.4073 | -48.9474 | 2025-11-05 05:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 5e6ba369-e7c2-356c-88a5-7e6c6412ff6e | -4.4259 | -48.9465 | 2025-11-05 05:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 5097cc3c-f54f-3e8c-884d-ba8ea982708f | -2.6508 | -48.52 | 2025-11-05 05:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| cb569a71-0e9b-376c-9570-dc5542d35ae1 | -2.6508 | -48.52 | 2025-11-05 05:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 79122c92-ab9f-3cb7-a1d1-3b2e1cc554e8 | -4.4633 | -43.2152 | 2025-11-05 05:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 03b40bcd-1eb5-3f15-823f-38e53acfc178 | 3.40663 | -51.28355 | 2025-11-05 05:29:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e7664224-ffa9-317f-bf96-b74877ad6f54 | 3.24191 | -60.686 | 2025-11-05 05:29:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5c7bd38-0410-369d-a07d-087d3bd226ee | 4.26296 | -60.39466 | 2025-11-05 05:29:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 263180cc-9303-3488-ba65-8463e6143424 | 3.40145 | -51.28442 | 2025-11-05 05:29:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e17d6dcf-da0f-3fb5-9a74-e38a7a5bbc95 | 3.29467 | -60.67422 | 2025-11-05 05:29:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4a43f1a7-2d66-311b-abdc-8aa20ea562a3 | 4.8772 | -60.25462 | 2025-11-05 05:29:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f0578ce-b4bf-3e0d-b94c-d89c0a2f3806 | 3.1462 | -60.72197 | 2025-11-05 05:29:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ba030ca-72a2-3d43-9f95-f0ecf3de9d8f | 3.298 | -60.67371 | 2025-11-05 05:29:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 45bc7733-b53b-3459-81bf-da869ac9cac4 | 3.24857 | -60.68496 | 2025-11-05 05:29:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e07f042-53ee-36b7-9a65-334a6065818a | 4.86229 | -60.24637 | 2025-11-05 05:29:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67f111d2-4bb7-3e05-a8a4-f55f567ad5c7 | 3.90271 | -59.63669 | 2025-11-05 05:29:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f53e74f-5483-300d-ad15-22f771506f7b | 4.01396 | -60.82007 | 2025-11-05 05:29:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3de1c752-0d17-3cc8-9ea6-16d352c8087d | 3.3192 | -60.07786 | 2025-11-05 05:29:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c2c413a-d950-393f-bc6b-7f44cd7b6759 | 4.44351 | -60.49054 | 2025-11-05 05:29:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a4a00e9-0932-3e38-8937-695e9261fc0c | 3.24912 | -60.68845 | 2025-11-05 05:29:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ce2552f-b359-3d0c-8748-ffdf429be792 | 4.8656 | -60.24578 | 2025-11-05 05:29:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6152565c-edbc-3114-a103-5c8e1346ec08 | 3.31588 | -60.07838 | 2025-11-05 05:29:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5eda33b2-1dd8-37fb-85b8-23333b7ebe6b | 3.27418 | -61.1878 | 2025-11-05 05:29:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2a4fb40-1d44-37b1-bd95-56b5f09b3e78 | 3.12284 | -60.80768 | 2025-11-05 05:29:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12f1189b-4f2e-3850-b137-6359b8872979 | 4.01451 | -60.82358 | 2025-11-05 05:29:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b396fcd-5c4f-3ac8-bd43-8e8ef7e380bf | 4.87776 | -60.25815 | 2025-11-05 05:29:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9a4bb5c-fa05-3da9-8e68-bbae4e3fb195 | 3.31866 | -60.07441 | 2025-11-05 05:29:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e4d5998-8549-369e-8a9c-10200894af28 | 4.87444 | -60.25867 | 2025-11-05 05:29:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f387cc05-04d5-3cc3-89de-d77dab5b296d | 3.14286 | -60.72249 | 2025-11-05 05:29:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 011c2065-a5fd-3a70-b0ac-0bd3bb965d1a | 3.36518 | -51.29051 | 2025-11-05 05:29:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b701667-ffdc-3903-aafd-8091c1210706 | 4.23009 | -59.86759 | 2025-11-05 05:29:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 514e2589-4a0c-3cc0-b2a8-3f19c2d8ef75 | 3.24579 | -60.68896 | 2025-11-05 05:29:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b33b5cc-7b87-386d-93d8-ad6b97990e63 | 4.0173 | -60.81953 | 2025-11-05 05:29:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff93ba8d-646d-3273-939a-32d27c707e5d | 3.30702 | -60.08683 | 2025-11-05 05:29:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac22804b-a7f6-3a80-be73-6c5edc4bcd1a | -6.7399 | -44.1602 | 2025-11-05 05:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 518cddd6-fb81-3e6b-ba3c-cac241ab0a38 | -4.4259 | -48.9465 | 2025-11-05 05:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a4538ca5-c606-3b5e-8570-1b8d07926083 | -4.4073 | -48.9474 | 2025-11-05 05:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c044269b-b77e-38a5-a2c6-83a0d83fb492 | -5.24343 | -48.50583 | 2025-11-05 05:31:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb416e74-d8ad-3c99-a3fe-88115c7480f0 | -4.10855 | -48.02398 | 2025-11-05 05:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2b433573-0f01-349e-97cf-d4bbef0c087f | -2.9752 | -48.705 | 2025-11-05 05:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34a061ac-7b1c-3bd2-91a3-4944ed4df6f0 | -2.48437 | -55.72963 | 2025-11-05 05:31:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0792059a-27d6-3e0b-92c3-af6e90ab651d | -4.59525 | -49.55474 | 2025-11-05 05:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eceb675d-8f58-3e32-9b91-1fecfbad7824 | -3.24018 | -52.92178 | 2025-11-05 05:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d930c176-ffe9-3ffd-8e97-7d485c1b130a | -2.72492 | -47.38514 | 2025-11-05 05:31:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 984e349f-30c0-3249-b49d-88a2054b08e1 | -1.30005 | -49.15621 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ecc9d625-ff11-338f-a93c-1611b5306bfc | -5.23641 | -48.50484 | 2025-11-05 05:31:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8bb9a41a-22a3-3411-aba4-4c6bf6801053 | -3.82364 | -48.67061 | 2025-11-05 05:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3e8f541-9916-3bf0-8451-fea897ae960c | -2.79357 | -50.3149 | 2025-11-05 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d37e9591-de7f-3166-9e81-7f69f092793d | -2.9639 | -48.59318 | 2025-11-05 05:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdc4e3ce-5f6c-3cfc-bf08-34f071201827 | -2.72386 | -47.39211 | 2025-11-05 05:31:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c80da7e6-f561-38d6-95d5-42f39d82bdbf | -1.28807 | -49.14906 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 36561372-ea37-3f8c-8691-b57c95795b75 | -3.44538 | -50.21679 | 2025-11-05 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c43b089-1007-3375-a3f3-4ce311ff5a08 | -3.81116 | -51.28888 | 2025-11-05 05:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad4dc74a-4bc4-3e0b-a293-6a40514b80a9 | -1.26247 | -49.14509 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2890a2fa-e211-3d85-b113-174a96824c3e | -1.28915 | -49.15224 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d1621a32-bb79-3189-abcd-1f3c6919ccf9 | -4.40851 | -48.94543 | 2025-11-05 05:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b5026f51-1f81-3311-a310-a7d2ef0def27 | -1.27713 | -49.14499 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e71f92f-0908-3465-8212-3ece3d5a437a | -4.60177 | -49.55577 | 2025-11-05 05:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a726051f-23f2-3df5-b2b2-11b104113fe5 | -3.82058 | -52.36026 | 2025-11-05 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e3b792b-09bf-329e-a5ec-69ec6572d055 | -3.44481 | -50.21525 | 2025-11-05 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 04592961-16f5-3cfe-8880-15ef0bb670a7 | -2.9618 | -48.5997 | 2025-11-05 05:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7491e46-d275-3d6a-91a6-817b89d86d10 | -2.38253 | -53.97952 | 2025-11-05 05:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4efb7bb4-e59d-3239-a41a-326af65cb80e | -1.26887 | -49.14609 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0b6e9cf0-7226-34bf-b4cb-110d113aee7b | -2.79426 | -50.31036 | 2025-11-05 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ecc0c454-0c7b-3716-a2d8-2d429c971b88 | -3.82319 | -48.67073 | 2025-11-05 05:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03da4efb-5b19-316e-82f0-bc4ca5f16d77 | -2.62164 | -49.22547 | 2025-11-05 05:31:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f325da77-4d01-3e49-9180-b6af45069b9f | -2.37307 | -53.97813 | 2025-11-05 05:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4113a104-f0d0-39ab-81ef-20607989c334 | -2.78748 | -50.31409 | 2025-11-05 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dcf2e48a-93c4-3637-89e3-26c9d6741771 | -5.2355 | -48.51145 | 2025-11-05 05:31:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ea3e1bfc-8e4f-37fe-a82a-28489fd51340 | -2.79288 | -50.31944 | 2025-11-05 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b412d3db-1745-38a4-9600-8699dcdfd64a | -4.41528 | -48.94642 | 2025-11-05 05:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bdc1b8ec-50c5-3fc9-8a9c-74b5140f9119 | -2.65847 | -48.5076 | 2025-11-05 05:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 925e0e5b-6999-3627-bccf-c3593d4f641e | -3.44417 | -50.2197 | 2025-11-05 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9dc58190-06c4-38c4-a159-0f68af8791a4 | -2.72611 | -47.3833 | 2025-11-05 05:31:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5398a85-bbcb-3752-b800-0bc7274c7303 | -3.49614 | -50.46542 | 2025-11-05 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dd111dc6-96b8-3ad1-806c-04989ec00135 | 0.25849 | -50.958 | 2025-11-05 05:31:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a9100eb9-1392-3339-aac6-26d09f848634 | -2.78817 | -50.30954 | 2025-11-05 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ec75b3e-5bc0-353e-b289-69763b4f92ca | -1.25688 | -49.13888 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74a4e91e-682e-333d-a975-dc90c2741b7c | -4.11155 | -48.02328 | 2025-11-05 05:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33b66ab1-b2af-3290-9a12-331266837090 | -3.50124 | -53.45476 | 2025-11-05 05:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02490593-c40e-3786-8f6f-d81bfeb6afd0 | -3.82414 | -48.66442 | 2025-11-05 05:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c8a8338-0eb5-3a7e-9842-ec77ce1a182e | -2.65364 | -48.50689 | 2025-11-05 05:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 60122771-b2b6-3959-b240-d796ce9c32cf | -1.25607 | -49.14409 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4963c7b-6489-3576-a833-48860510ff47 | 0.25954 | -50.95677 | 2025-11-05 05:31:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b040f740-f35c-3d02-afc5-7ed8b0e2b8e9 | -3.72202 | -54.2127 | 2025-11-05 05:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dff73cd0-b95c-347e-945b-9198ae1fa9e1 | -3.83835 | -55.97185 | 2025-11-05 05:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3da7f7df-cfaa-356e-9a53-94ad6e210697 | -2.79416 | -50.31688 | 2025-11-05 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0481ecbd-e7c0-3d55-bd34-81c0fc43d6c0 | -3.07553 | -52.63123 | 2025-11-05 05:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb48e696-fbc4-3859-b38e-d947dd72cc9e | -1.29634 | -49.14804 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a9e94cc8-196e-3edc-a2e6-ee3eee29da2e | -1.28167 | -49.14807 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ebdca460-5e46-38d2-a7b2-1ba0c66a34e4 | -2.73112 | -47.39308 | 2025-11-05 05:31:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aaa33903-8a8f-327d-8b20-5b91f9db63f2 | -2.72509 | -47.3903 | 2025-11-05 05:31:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbae0c0e-b2fd-389d-9ed6-8ee07e845f22 | -3.82455 | -48.6643 | 2025-11-05 05:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c191ed4d-9a41-3cdd-9076-3b3b67be4868 | -2.73235 | -47.39128 | 2025-11-05 05:31:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17f891fe-2359-35f4-999a-25f9e181bf00 | -3.91008 | -54.56244 | 2025-11-05 05:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6171d74-2fcf-31cd-8fca-4dcda66783a8 | -2.42522 | -49.29779 | 2025-11-05 05:31:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 974fbdef-6f9a-3fae-9262-81f915cf2560 | -2.73219 | -47.38603 | 2025-11-05 05:31:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e7f540a-f697-3910-9337-7878c93690c6 | -1.24967 | -49.1431 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00f34439-c8de-376c-af3e-d085685681b5 | -1.30088 | -49.15102 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5bef76b9-dfe6-3418-ba24-54bc96640ef2 | -2.48558 | -55.72184 | 2025-11-05 05:31:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README37.md)
