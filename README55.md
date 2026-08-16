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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e95be27-0bea-3f41-87ec-9f43e93532d6 | -16.33234 | -55.38086 | 2026-08-16 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16c697f1-607d-3b00-a69d-1c7a39c65b95 | -16.33775 | -55.3805 | 2026-08-16 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e9be47f-048e-3f08-8b0c-f46307c737f7 | -16.33161 | -55.38161 | 2026-08-16 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6026b12-9bcb-37af-aeff-b6d006ccc7d7 | -13.79296 | -53.78351 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21ead48f-e14b-356b-914c-a9785787b900 | -13.81663 | -53.77822 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ddc05a5-7ac7-36b7-bed9-d7281ea94614 | -13.79368 | -53.82698 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 782337b9-c0b3-3ae5-939e-5ccb2c9a60e4 | -13.81613 | -53.78245 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d8be3c3-8274-3b9b-bebe-aa5ed1b85bed | -14.48531 | -54.02595 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbf77131-87e2-387f-8e4f-d4fa65584d8c | -13.7991 | -53.78018 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 145f2582-ea0a-350a-ad40-4714bdf7ba9a | -13.7972 | -53.79661 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b23304b-589a-3e5d-92a0-7c3cdf3cfe63 | -14.07012 | -53.72374 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23f8b762-0749-34d0-b7cb-287f488877cd | -13.80501 | -53.82841 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16219b37-0d6a-3421-9bbb-0ef95643bfcb | -14.78045 | -56.95066 | 2026-08-16 05:38:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9b646bd-6330-39c3-a596-39b8521fb8dd | -13.79934 | -53.8277 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70afa67a-c62d-3e49-a0da-dead732a327e | -14.0722 | -53.7184 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0ba5a47-7ae4-3150-92fe-4e7ca576bb28 | -14.32438 | -53.31243 | 2026-08-16 05:38:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4aea82c0-1faf-36cf-acd7-30b2ba3b5b35 | -14.06855 | -53.6877 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcb2fb6b-9d22-32d0-843a-a4fd846545b3 | -14.48574 | -54.02209 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80d6ad4b-c813-3185-9c2d-cc731c82f461 | -16.33663 | -55.38462 | 2026-08-16 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c1175b97-8cac-3861-9334-14eba2834a28 | -13.42117 | -57.04618 | 2026-08-16 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ade34a9-d729-3700-a547-00e3496d4e8b | -14.38588 | -51.8797 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f40f739a-e18c-3c8e-8939-da2e31e6f8d3 | -16.21386 | -57.64025 | 2026-08-16 05:38:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4e644ac5-d802-3075-a4b0-e9fed6f0951b | -13.41603 | -57.05014 | 2026-08-16 05:38:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 015b4a4d-9ffd-3729-b2b7-047e3b0fe1c3 | -13.79857 | -53.78477 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b016d15-fe95-3dd0-8a80-a039c5a4e776 | -16.33735 | -55.38385 | 2026-08-16 05:38:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07de42d5-67b7-3186-b49e-36e04cac2f5c | -15.16783 | -50.06943 | 2026-08-16 05:38:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f624d3f8-eee1-3ca7-9312-84193119f172 | -14.38645 | -51.88492 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 50182a7a-575e-3b29-bf1f-2b5d7464e4a6 | -14.37833 | -51.90046 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fe52679-7799-32bc-b6e3-be8987c93e78 | -14.28779 | -51.94482 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5244385a-3a84-3d5f-bfb9-dcdf77565a85 | -14.29829 | -53.06358 | 2026-08-16 05:38:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e8e4950-85d8-3161-b297-27cfebd36b33 | -14.31285 | -51.95332 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 41d8f6ed-d9e1-3332-adf3-ad7ba95f96b5 | -14.3829 | -51.90686 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 39f50005-ea11-38a6-9680-d49799fb8696 | -13.80474 | -53.78128 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 90e68ad8-0fa2-314a-89ae-9e204753f0e7 | -14.37765 | -51.89529 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ecd0510b-d7ba-3f70-a0a0-cca863132cbb | -14.38874 | -51.91296 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 34ba7fa3-63c6-362f-b930-80292bc7ccd0 | -16.20933 | -57.63958 | 2026-08-16 05:38:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ad002d11-3b99-3972-91e6-e708974b0500 | -14.37706 | -51.90071 | 2026-08-16 05:38:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8176e2f-3cef-36ca-a66f-b5c926a021fc | -13.81044 | -53.78185 | 2026-08-16 05:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ec471d3-8c39-35e4-b738-8cc99f778dea | -12.0091 | -46.4498 | 2026-08-16 05:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 263.7 |
| 79c1bb0b-49cb-326f-8f65-35a7c1b48ee3 | -6.7123 | -58.9412 | 2026-08-16 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| dddf6568-8405-3eed-9989-174ab7e538ee | -6.6377 | -59.0795 | 2026-08-16 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 125b8fab-4676-3b3f-a9f4-97c3b00533b1 | -8.446 | -62.6752 | 2026-08-16 05:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 5bdb7032-5678-3e9f-a3b8-5f244edb7328 | -12.0282 | -46.4471 | 2026-08-16 05:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 344.0 |
| 8292a8d2-e0a5-303c-9039-196a79492c61 | -12.0095 | -46.4271 | 2026-08-16 05:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 74c2f8ab-e5c2-3d33-b0f3-eef0c60f828f | -8.9601 | -60.5165 | 2026-08-16 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 30911059-492f-3df1-b126-5adec67ebcaa | -6.3137 | -43.6178 | 2026-08-16 05:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 0cd2fa3f-20d8-3918-b47a-3db329ff6092 | -12.0286 | -46.4244 | 2026-08-16 05:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| b4125de9-6495-366d-b788-bd59d9f117de | -8.9787 | -60.5156 | 2026-08-16 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| b112752b-5963-3ae2-82ac-5e299e1f66fe | -8.4275 | -62.676 | 2026-08-16 05:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 5469bad2-02b7-3e66-ba1c-6512dcd539e2 | -12.0087 | -46.4725 | 2026-08-16 05:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| ec65ec10-5b93-3f6f-8f10-08f0056422fa | -12.0279 | -46.4698 | 2026-08-16 05:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| bcf9ffcc-a446-3cfa-a8a1-22094c8f3227 | -8.96 | -60.5358 | 2026-08-16 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 9dd7ceaf-1b54-3b82-8a73-1817a2470e7e | -8.9785 | -60.5349 | 2026-08-16 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| b72c2d1e-7816-342d-a40d-b6be7f1bc2b8 | -22.78411 | -51.39288 | 2026-08-16 05:40:00 | NOAA-20 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 74f1b671-bd86-3645-a2e3-0f9421b854a5 | -12.0095 | -46.4271 | 2026-08-16 05:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| d8166cce-55dc-3b84-bae5-e872030313a0 | -6.3137 | -43.6178 | 2026-08-16 05:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| ace96c17-062c-3df4-a5e2-0a8bd09b25b8 | -8.9785 | -60.5349 | 2026-08-16 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 89e5ec65-a620-39b5-b4e9-80bae94b865c | -12.0091 | -46.4498 | 2026-08-16 05:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 263.3 |
| 662a2de2-c90c-3ad3-8b9d-ba16d80386af | -8.9787 | -60.5156 | 2026-08-16 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 8165b098-5bb9-36db-a75e-dd538cb54f49 | -12.0282 | -46.4471 | 2026-08-16 05:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 216.3 |
| 1ec927eb-83d7-3d29-800b-b86d7e9569f5 | -12.0279 | -46.4698 | 2026-08-16 05:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e94130ba-31c0-3a0b-9c42-d338c6ad7c1a | -12.0087 | -46.4725 | 2026-08-16 05:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| b914009f-381d-3147-98f7-dde64954bee1 | -6.7123 | -58.9412 | 2026-08-16 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 37d3fd20-9ed1-3321-8c60-cb5103e15cc5 | -8.96 | -60.5358 | 2026-08-16 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| fdf7bff4-f3b4-354a-bb5a-bff253fc2191 | -12.0286 | -46.4244 | 2026-08-16 05:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| a5409103-b6c9-32ab-a4d0-d442e63f1cd9 | -8.4275 | -62.676 | 2026-08-16 05:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| dc9d9b76-155a-3e6e-858d-31977c6d7f5b | -8.9601 | -60.5165 | 2026-08-16 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 3e4081ac-9e62-331b-811a-8eaf44bbff56 | -8.96 | -60.5358 | 2026-08-16 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| fd0f5376-5ec6-3d8a-85f7-1cee81243855 | -8.9785 | -60.5349 | 2026-08-16 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 648b0d6b-9dea-31e2-9158-073af200c179 | -6.6194 | -59.0609 | 2026-08-16 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 46790de3-4ac0-31f0-951f-f2e8c40f14ba | -6.3137 | -43.6178 | 2026-08-16 06:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| f3851c49-1971-3438-97ae-f67bf2e95059 | -8.9601 | -60.5165 | 2026-08-16 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| f562fe7f-c17d-314f-b7fa-5fff4d9a0832 | -12.0091 | -46.4498 | 2026-08-16 06:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 233.6 |
| cd6cf0f4-5465-34bc-a758-07c6c91fd612 | -8.9787 | -60.5156 | 2026-08-16 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 57cd1ac7-361e-3fe2-b697-9a9b6397a617 | -6.7123 | -58.9412 | 2026-08-16 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 46d659bc-ad85-38c0-bf72-5d00b2e5db5d | -8.4275 | -62.676 | 2026-08-16 06:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 07be3f56-22c6-399b-9208-c795ac33d25e | -12.0087 | -46.4725 | 2026-08-16 06:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 884a6655-b443-3c9b-b6d4-a83d2f553d63 | -12.0282 | -46.4471 | 2026-08-16 06:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 135.1 |
| c1da1b97-4abd-35ee-9843-3948eddca76d | -12.0095 | -46.4271 | 2026-08-16 06:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 70de376b-4ed3-3248-aa01-f98100ae807c | -17.7857 | -49.4743 | 2026-08-16 06:10:00 | GOES-19 | JOVIÂNIA | GOIÁS | Brasil | 5212105 | 52 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 0fd837f6-c576-3d4e-8b8b-ebd41de8a152 | -8.9785 | -60.5349 | 2026-08-16 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| e5965bcd-9879-36e3-97d0-476084e769b8 | -12.0091 | -46.4498 | 2026-08-16 06:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 200.7 |
| f3fa27ab-3eee-3131-9510-3efe780c7d45 | -6.7123 | -58.9412 | 2026-08-16 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| f3dd3536-cc43-3f3e-a8aa-7815bc2e76d3 | -6.3137 | -43.6178 | 2026-08-16 06:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 439dc74a-91a4-3c93-b216-d9456eec02e7 | -12.7017 | -48.4753 | 2026-08-16 06:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| afaabc92-b77d-30f9-9c8f-31372723bc5b | -11.08 | -47.2479 | 2026-08-16 06:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 6506efed-d4ff-3e63-b833-cc08a724fc54 | -8.9787 | -60.5156 | 2026-08-16 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 2becfcad-e307-39d7-8467-85a54e23b744 | -8.9601 | -60.5165 | 2026-08-16 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| ed1c3ffb-8d30-31e3-b57e-627ed851cb00 | -12.0095 | -46.4271 | 2026-08-16 06:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| c4d7a600-905c-3eba-a1fd-d4c6657d6f6d | -8.96 | -60.5358 | 2026-08-16 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 06e82a01-c884-354c-9c92-56660071aac5 | -12.0282 | -46.4471 | 2026-08-16 06:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| fb46b76e-1b76-37d5-8b2b-6acfa0e720ec | -12.0 | -46.46 | 2026-08-16 06:15:00 | MSG-03 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26442f59-5930-3bf0-a3d0-9b11ba134f50 | 0.4928 | -60.59722 | 2026-08-16 06:18:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3c8fb49b-86b6-3fa7-b432-833ce012e638 | 0.49181 | -60.59097 | 2026-08-16 06:18:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 58a2b3eb-e8cd-3c2e-bb3c-57c0368a9b16 | -12.0282 | -46.4471 | 2026-08-16 06:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 01fff85d-ddde-32c5-aea6-a86c3e62495d | -14.901 | -46.6283 | 2026-08-16 06:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 154.5 |
| ec545623-ef26-35de-aa04-000cffcb3e87 | -12.0095 | -46.4271 | 2026-08-16 06:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| fdc4a1bc-4263-32fd-b2b2-2759ad5a14a1 | -6.3137 | -43.6178 | 2026-08-16 06:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| c5a882eb-e671-31db-bf61-b53e07325f26 | -12.7017 | -48.4753 | 2026-08-16 06:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 9811dbd0-af03-37c0-8338-1db2418a1b92 | -12.0091 | -46.4498 | 2026-08-16 06:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 241.9 |


[Clique aqui para ver as próximas entradas](README56.md)
