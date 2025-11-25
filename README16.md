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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0e8617f-395b-379d-a207-6bb19689aaa7 | -21.25005 | -52.06083 | 2025-11-25 04:44:00 | NOAA-20 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e8c90e31-3cdd-37cf-b52e-a929df1f8399 | -22.97887 | -48.66645 | 2025-11-25 04:44:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e5e0d02-41a4-3877-acdc-3030d47b1d4c | -22.47636 | -49.1357 | 2025-11-25 04:44:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b6159e7-7636-3dda-be82-43e0ee0dddc1 | -19.22331 | -57.3326 | 2025-11-25 04:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 93bdd6e3-69eb-3d22-abc6-d7a256bb2085 | -20.40902 | -57.99319 | 2025-11-25 04:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f65b7c31-9455-31d2-89d2-9a2ab4eaf1bf | -21.70406 | -57.66399 | 2025-11-25 04:44:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 492301de-a609-3256-82da-fbb23b4bd81c | -22.11593 | -54.95392 | 2025-11-25 04:44:00 | NOAA-20 | ITAPORÃ | MATO GROSSO DO SUL | Brasil | 5004502 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5f6ffcd7-1b86-3398-9f8e-4e6e3e323d95 | -19.21357 | -57.34141 | 2025-11-25 04:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 7e036849-8e82-3d12-92b0-d13d7b959608 | -28.71354 | -52.18779 | 2025-11-25 04:46:00 | NOAA-20 | NOVA ALVORADA | RIO GRANDE DO SUL | Brasil | 4312757 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c2a50c64-23fa-3a1f-a4a7-170c0765946a | -8.051 | -43.1237 | 2025-11-25 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 135.2 |
| 3d8ed8d7-6be4-370c-9e79-c7fba0f06eba | -8.07 | -43.1216 | 2025-11-25 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| a2cb5e56-d945-3c01-8dc4-a5589632557e | -8.0507 | -43.1472 | 2025-11-25 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 5ce5fb18-9958-3bbf-8319-fead10408321 | -8.0696 | -43.1452 | 2025-11-25 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 2a815509-dde4-37e3-889d-41ce76947364 | 3.11299 | -60.76871 | 2025-11-25 05:27:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4e1d198-a790-3da3-b774-cec5aaaabde6 | 1.98554 | -55.79056 | 2025-11-25 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d7d4ab8-db7f-374d-82ba-40cace84e785 | 1.32715 | -50.86003 | 2025-11-25 05:27:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 637ad185-691e-37c2-babe-61755d953fbe | -1.33812 | -53.1532 | 2025-11-25 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d3848ea-418b-397e-a7e6-09b7cd91a43f | -1.15633 | -54.19883 | 2025-11-25 05:29:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 587931ba-9c9f-37a2-b29f-171494cc9a98 | -3.02384 | -51.03718 | 2025-11-25 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a84d6b7-454f-312c-9679-36d996bdc510 | -3.03199 | -51.02936 | 2025-11-25 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f07410e2-7e9c-3820-8dcb-a06bf65b0e8f | -2.94409 | -54.79977 | 2025-11-25 05:29:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 273bddd6-a88b-36e6-99ec-e243b775cf92 | -1.29922 | -53.14692 | 2025-11-25 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35b52e99-b894-3bcf-9ac8-f9aa2a8e1455 | -3.03022 | -51.03401 | 2025-11-25 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 983e3ef2-e605-3b4d-8899-bce637b68f59 | -1.85835 | -54.05745 | 2025-11-25 05:29:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d6a3e0b-339f-36ee-b828-1559354b69d3 | -3.02565 | -51.03249 | 2025-11-25 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1a0beb7-3d26-3654-add2-8ad26397e44a | 0.65942 | -51.54042 | 2025-11-25 05:29:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c9b4296-3964-3606-b981-b0470ca419be | -9.09703 | -63.54016 | 2025-11-25 05:29:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 963aa8d9-a349-3f97-bdf0-e1faf0ec82f8 | -2.99088 | -51.06071 | 2025-11-25 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53c98c3d-f279-387e-8e49-eb3f22709410 | -2.98718 | -52.62557 | 2025-11-25 05:29:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 778a24f9-3a75-36b9-bf9f-566e14aebbd9 | -1.29434 | -53.14619 | 2025-11-25 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91c81b35-3381-398f-816f-05328280a6b1 | -11.49278 | -58.44016 | 2025-11-25 05:29:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6da5ec76-21cd-373b-8c3b-c44bcb829f19 | -1.63773 | -53.19147 | 2025-11-25 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a554c21d-2194-3dae-9a94-a2c06fb7fe82 | -1.96699 | -54.70748 | 2025-11-25 05:29:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 7146391b-16d9-3fcd-92c4-ef3b952efbd6 | -1.30119 | -53.14624 | 2025-11-25 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea40d994-c7aa-3db5-8f1e-cfdd9fddbf59 | -3.03141 | -51.03341 | 2025-11-25 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1541f843-a684-300e-8cd0-821bf73f1fa9 | -1.34297 | -53.15408 | 2025-11-25 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c5a5e66-1fa2-35d4-a5b6-0670fbb0e39b | -0.99686 | -53.17352 | 2025-11-25 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 851f9923-808e-318d-866e-0d4a2682b331 | -3.02445 | -51.03314 | 2025-11-25 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14e204c2-bef2-3cc1-8643-da2fb1fdecc4 | -3.03083 | -51.02999 | 2025-11-25 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92816509-34e3-3c43-8fbb-d13f02659cb6 | -1.41588 | -55.37554 | 2025-11-25 05:29:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b1f7be7-7385-3d0e-a9ca-fa0923b30c44 | -9.22932 | -65.7476 | 2025-11-25 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94d29f3c-2dac-3049-ad79-e49a2995302f | -9.85728 | -62.53505 | 2025-11-25 05:29:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3877dac4-bc40-3d72-a887-8bdc0735b4c2 | -3.02507 | -51.03654 | 2025-11-25 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 524871dd-c831-3225-b130-2a24185cc57a | -9.97346 | -66.73784 | 2025-11-25 05:29:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24aea578-23a8-338d-908a-b390419c54a9 | -1.29631 | -53.14558 | 2025-11-25 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dd61e09-f016-3a52-b638-c12e2ce6c19b | -2.99028 | -51.06473 | 2025-11-25 05:29:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e879ce2-c881-3b65-8a24-6e490187af5b | -9.85674 | -62.53854 | 2025-11-25 05:29:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f425eccc-5c69-3925-bc29-e6cff5870f90 | -8.0507 | -43.1472 | 2025-11-25 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.4 |
| 272ba160-d353-38fe-9355-3f6bd01b263e | -8.051 | -43.1237 | 2025-11-25 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.8 |
| 2ae2e75b-2a9e-39b2-9e09-7bc8869ee298 | -8.0696 | -43.1452 | 2025-11-25 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 15332b98-782c-39e9-8b0e-cd7fa8aa87fe | -2.4867 | -47.8342 | 2025-11-25 05:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| b6399329-56bb-3ebc-971c-352149133dad | -8.07 | -43.1216 | 2025-11-25 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 1f0b0603-2501-3c35-a369-7f193c976726 | -13.45162 | -60.42928 | 2025-11-25 05:31:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 339c9acf-f8aa-3a5f-907f-1ffe1f8fff87 | -17.24836 | -56.01903 | 2025-11-25 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1ad84836-3c48-3419-8d1f-13b99fdf8e00 | -15.94279 | -57.90129 | 2025-11-25 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0d33d082-0b49-34c5-9a18-c7d7a2267fd6 | -15.60561 | -59.93701 | 2025-11-25 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db777d21-b2d2-321f-b005-beae478da062 | -15.60495 | -59.9419 | 2025-11-25 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e94977b-22b3-3535-865a-385e71106926 | -16.21748 | -59.94441 | 2025-11-25 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c89e5d4a-51ac-3597-8296-54eb86289376 | -15.60113 | -59.94133 | 2025-11-25 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8f9f250-3580-3596-a57a-3953e7182590 | -11.71322 | -62.97594 | 2025-11-25 05:31:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ef85104-f07c-35f1-9eb0-9228ca7a78e0 | -19.33612 | -54.35611 | 2025-11-25 05:31:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a7a9733-195c-30c4-b14f-07b1e4d56a0f | -10.52244 | -68.04873 | 2025-11-25 05:31:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72e13024-cc9a-3812-96af-eb3d8671ef02 | -19.33726 | -54.35317 | 2025-11-25 05:31:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e9fccc3-b2d3-3399-b0d1-0b041f4e2f88 | -12.29198 | -64.45719 | 2025-11-25 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12c2a410-7d49-3b0f-879a-407ad6b443bc | -19.33655 | -54.35184 | 2025-11-25 05:31:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1b10a77-eae5-39db-bef8-828d9709710c | -12.13965 | -64.09163 | 2025-11-25 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29f7ab50-ce02-3ee6-a2d2-ccd1d7d0682b | -16.30863 | -52.92327 | 2025-11-25 05:31:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ca0d177-361b-3895-acf8-8c9e4316bcb0 | -16.30819 | -52.92736 | 2025-11-25 05:31:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cc2f041-f6ea-3336-8f4f-52fd794ce1ac | -11.88438 | -62.85936 | 2025-11-25 05:31:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca7a5d11-7b85-315e-9a3b-2f3263a1b330 | -17.24803 | -56.02206 | 2025-11-25 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a51c2bbb-689f-32d9-83a9-17e90169b3e1 | -15.47489 | -58.70725 | 2025-11-25 05:31:00 | NOAA-21 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13d2f84c-bba3-34f3-b464-0a5640a12813 | -13.45525 | -60.42983 | 2025-11-25 05:31:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6152c41-e7e8-3e3c-a610-c551497a1337 | -19.33151 | -54.3523 | 2025-11-25 05:31:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45593ad6-9d04-35a3-ba03-8261351d83e3 | -20.38929 | -57.99388 | 2025-11-25 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| acd6dc36-d9f4-3c7c-b94b-953c401d5db6 | -19.7972 | -56.0986 | 2025-11-25 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 553e9a2d-b5e6-34fa-ac88-3cc22b1be9f8 | -19.79202 | -56.09795 | 2025-11-25 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ac5ec95d-92e1-3c90-b7ee-fa57710d0aa1 | -20.38468 | -57.99326 | 2025-11-25 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 34204f3f-f48c-3191-9034-36c6a178cf0b | 3.11362 | -60.76799 | 2025-11-25 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6443004b-2333-3f1e-8648-9c6c689948a1 | 3.11781 | -60.76734 | 2025-11-25 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b56961f3-f957-3779-a99a-001cc5b3db0e | 3.11425 | -60.77182 | 2025-11-25 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17b58fa8-3fd4-3f50-90d9-fd9810b23177 | -1.96395 | -54.70957 | 2025-11-25 05:59:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3a01e9d-d573-306c-89ec-5ec2c95fb1cb | -1.97078 | -54.71018 | 2025-11-25 05:59:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ab61f0c-ec3c-3c4b-a2c3-d7fbb81be15e | -2.48276 | -47.82223 | 2025-11-25 06:09:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 889a3045-f7a5-3688-8c6e-fd70c9095d08 | -6.68907 | -43.92944 | 2025-11-25 06:12:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 20638650-a4b4-386c-8a9b-79f7035ff634 | -8.1641 | -43.18613 | 2025-11-25 06:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.1 |
| e58a8ec6-cdb0-30d5-80b9-575b02afcb9c | -8.06307 | -43.12425 | 2025-11-25 06:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 2189fd2b-0477-3aa9-b5ba-95e6595c1168 | -4.72683 | -44.73563 | 2025-11-25 06:12:00 | AQUA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 745cf6fe-bd89-3260-ba17-fe433da0fa90 | -8.15778 | -43.19609 | 2025-11-25 06:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 150ba0ea-e3b3-313f-a678-f019d8f88b33 | -6.68709 | -43.94394 | 2025-11-25 06:12:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 2ec01ddc-0321-3745-8617-10d6ce72c8ff | -7.45827 | -45.17826 | 2025-11-25 06:12:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0f05aad2-fa93-3e86-904d-4d7c69e91559 | -4.54684 | -43.29744 | 2025-11-25 06:12:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 320df8fe-67dd-3162-97cb-aa7e6818097a | -3.96761 | -47.66658 | 2025-11-25 06:12:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 83c7c00e-df3c-3de1-b604-cee04e25a86d | -7.56731 | -45.85391 | 2025-11-25 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9982734c-6cd0-37e7-8a84-3e8017c0a81d | -3.09191 | -50.5681 | 2025-11-25 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5e107a7b-a228-378c-b735-efc4aeebdb84 | -4.81827 | -43.81306 | 2025-11-25 06:12:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| caea3e12-321b-3f94-8b00-8e1411a8e465 | -7.86117 | -46.74778 | 2025-11-25 06:12:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 64584029-de22-3006-b098-49fc4deed911 | -7.45658 | -45.19032 | 2025-11-25 06:12:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c01c0960-cecc-30c1-9715-acbb9ebc9509 | -3.02166 | -51.02868 | 2025-11-25 06:12:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| d3513a39-e1a0-3427-af51-26175c8d3c54 | -3.15745 | -49.17141 | 2025-11-25 06:12:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6e910b6c-7448-3d63-8892-f354bfdf29f8 | -7.56574 | -45.86489 | 2025-11-25 06:12:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README17.md)
