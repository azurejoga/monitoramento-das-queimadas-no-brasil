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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 335b6bb1-c8b3-3670-9c87-95a6937bc5ed | -10.85145 | -61.96529 | 2025-07-24 05:55:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70e09d57-f4b2-319e-8101-783880dced9b | -8.95576 | -72.84138 | 2025-07-24 05:55:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 434271e3-2ccf-33d2-b617-f3c668b73ee3 | -9.60425 | -63.46178 | 2025-07-24 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc0ac3fa-fba6-3277-bdc8-98010c9703eb | -9.5337 | -63.6273 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44bd79cd-74a9-37ac-844c-3ab9f0f17345 | -10.044 | -59.09554 | 2025-07-24 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ddd7f5a8-d235-3ebb-980e-8434464c0177 | -8.92905 | -63.89975 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7aac789f-e921-3659-a3c6-d3e31145863d | -8.56059 | -63.88857 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ba395132-6d35-3f9c-b670-06588e270ea1 | -9.76049 | -65.09569 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88a28ff9-59a2-35d8-a9ee-752ce3a5b8a9 | -11.95003 | -58.76255 | 2025-07-24 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 98b564e5-0920-343e-b641-80b8f5a5f546 | -7.46296 | -57.66833 | 2025-07-24 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20e8eae7-55d8-351c-a97c-964634bd1a7a | -9.46284 | -63.14724 | 2025-07-24 05:55:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eaa09a47-5361-3bd6-938e-76e4a47fcc39 | -11.94954 | -58.76674 | 2025-07-24 05:55:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b946cc32-64d2-3d13-afff-db6c348a2e21 | -10.29729 | -60.54013 | 2025-07-24 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 021ebc9a-ff85-3606-a6f2-342241f7466e | -9.13426 | -63.91766 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f341a216-0a84-3bba-a016-54b82725bbc3 | -7.46373 | -57.66875 | 2025-07-24 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5caf783d-5404-3231-8aaa-074b41fe2341 | -10.0435 | -59.09962 | 2025-07-24 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 318543c2-bed4-31fa-8e6f-126a95c743f0 | -9.13373 | -63.92138 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 466aed7b-aac8-32f1-affc-331214f09965 | -7.45202 | -57.66318 | 2025-07-24 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0df4356-0a6f-348e-9703-aeed3285c831 | -8.61468 | -64.03683 | 2025-07-24 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18f4c2f3-7be7-3fc7-8166-d8bb234097be | -10.0426 | -59.09803 | 2025-07-24 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c2f9b5c-4950-3fec-93fd-423c2faa91aa | -7.45759 | -57.66818 | 2025-07-24 05:55:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1e65e41-a8ee-3ea6-856a-46aa0c59082a | -9.53314 | -63.6312 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d268a6be-b2cf-3f6c-a07b-beaef649559a | -9.53381 | -63.62978 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa243373-09af-30b7-8514-637c1d24a641 | -7.27173 | -60.17723 | 2025-07-24 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1460f4f3-fdff-39df-ab2d-6c3fe83ea11e | -8.56467 | -63.88917 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 89a78f69-3b14-37ad-bdb9-349a3bee015b | -8.9599 | -62.21417 | 2025-07-24 05:55:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a72badb8-dd93-39f9-840d-523fe2a38e17 | -9.62546 | -67.25506 | 2025-07-24 05:55:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fa2194e0-4377-3c4a-b418-4186a78c4167 | -9.75875 | -65.09281 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7dc22ff9-b407-3887-ae9e-f197ed14500d | -12.50025 | -57.77345 | 2025-07-24 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 18463e86-78e6-3ba1-9dee-b8e58561833e | -10.04312 | -59.09397 | 2025-07-24 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc7ae471-25da-3e3f-bc59-97d4e0ed6b12 | -9.52948 | -63.62672 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc5ebb37-db19-30be-9d79-5d2f34687c97 | -10.12257 | -57.76735 | 2025-07-24 05:55:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c1f74a3-cff5-30b3-b5b9-b3c646669496 | -8.56927 | -63.88613 | 2025-07-24 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94aa3d6b-d4b1-3dad-ba4d-0c2a07ba6164 | -7.2597 | -43.0645 | 2025-07-24 06:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| e9678ff9-388f-3bbf-8047-0f140d3a9cd8 | -21.2122 | -48.74 | 2025-07-24 06:10:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.8 |
| 2e1b57d3-9b30-3385-b324-37c6e2eb9985 | -7.2597 | -43.0645 | 2025-07-24 06:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 2d209ea9-8f6c-3e9d-9f49-1b43fdd0c628 | -21.2128 | -48.7167 | 2025-07-24 06:10:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.6 |
| 117595a6-c298-33ee-90ab-fbf4948720e6 | -7.2597 | -43.0645 | 2025-07-24 06:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 4d0fc287-1f07-39a6-b377-bc522acd27f4 | -8.95659 | -72.84177 | 2025-07-24 06:22:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6df3b2ac-b981-3e76-936b-d2d47cc32085 | -9.53003 | -63.6277 | 2025-07-24 06:22:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f333397a-b2e0-3259-929b-dc029cc57975 | -9.76146 | -65.0967 | 2025-07-24 06:22:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01b5b4c5-1842-335c-b9f7-e901376aedcd | -8.61456 | -64.03933 | 2025-07-24 06:22:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc8ff032-2786-36da-b5a3-3370556ad683 | -9.37768 | -66.57958 | 2025-07-24 06:22:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae356021-a2ac-3189-9156-464d74636cd8 | -8.95609 | -72.84266 | 2025-07-24 06:22:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bcbf0b4-b373-3f9e-8007-3844323ace25 | -9.62595 | -67.25712 | 2025-07-24 06:22:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 731babc7-93a1-3cb1-8107-a29d79caf66c | -7.9795 | -70.99487 | 2025-07-24 06:22:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc01ef9f-7f17-3b3b-93f5-9a1e958f668a | -9.37811 | -66.57634 | 2025-07-24 06:22:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1c1097e-2b4f-3da0-b302-2cb552a10e2b | -9.62747 | -67.25554 | 2025-07-24 06:22:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d45108fc-ff56-3765-962d-d523aa36bd54 | -9.76197 | -65.09264 | 2025-07-24 06:22:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b412e908-59aa-35f6-92f6-7c46f72e9079 | -8.56659 | -63.88714 | 2025-07-24 06:22:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e5f6e04e-f8db-3a15-99e2-5054bd7ede6e | -8.56596 | -63.89194 | 2025-07-24 06:22:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4b776ba-984f-30ab-8820-86aa95da073b | -21.2122 | -48.74 | 2025-07-24 06:30:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.2 |
| 07841cef-239b-3860-9d26-60e1cbba0797 | -7.2597 | -43.0645 | 2025-07-24 06:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| dac05db6-b3d3-327f-9d30-f5f44d2e8bbb | -3.17597 | -49.43988 | 2025-07-24 06:31:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| fa41610c-4ac6-3218-8642-857e91df843c | -3.16707 | -49.44384 | 2025-07-24 06:31:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 73637b24-f030-3ad5-bf44-44601596d213 | -11.94321 | -58.76174 | 2025-07-24 06:35:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 36.8 |
| e2a0dfaa-b807-3c5e-b7e1-b35f5fbe8917 | -7.2597 | -43.0645 | 2025-07-24 06:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 3b0fd3f8-d8f1-3364-b839-55d3faa0e9a4 | -21.2128 | -48.7167 | 2025-07-24 06:40:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.8 |
| 335d9f3d-b63f-3b98-8993-252619107987 | -21.2122 | -48.74 | 2025-07-24 06:40:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.0 |
| db0ecc3c-7a35-3e2a-a8b5-2b856668016e | -7.2597 | -43.0645 | 2025-07-24 06:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| b0cf2226-81ee-3490-9646-626bfca9218a | -3.1833 | -49.4429 | 2025-07-24 06:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 7d993d6e-9e80-30aa-8105-a131be3ae955 | -3.1832 | -49.4642 | 2025-07-24 06:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 1d3a169d-06fe-3ca7-90a1-f3939caa5d62 | -7.2597 | -43.0645 | 2025-07-24 07:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 1d32bcf6-0f18-3a9e-a575-ad010d467fb3 | -3.1833 | -49.4429 | 2025-07-24 07:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 241ca0d4-0f0f-3fab-9867-94e75d3aefbe | -16.2368 | -49.9673 | 2025-07-24 07:10:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 2760d4bb-8575-3a73-88c7-ac324e125e27 | -16.2372 | -49.9452 | 2025-07-24 07:10:00 | GOES-19 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| ec1e8daf-9e96-39b6-a303-c4c4bc7aab0a | -16.2176 | -49.9484 | 2025-07-24 07:10:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 128.2 |
| ea477e32-70e6-34eb-9bf1-03f7738e5314 | -7.2597 | -43.0645 | 2025-07-24 07:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 90cadc32-a136-363a-9f8e-3736792efcb1 | -16.2171 | -49.9705 | 2025-07-24 07:10:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 91909308-080b-3341-9eda-357c1c9f98e1 | -3.1833 | -49.4429 | 2025-07-24 07:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| c47dc8ff-2f6a-32b2-93f4-e35128436df8 | -7.2597 | -43.0645 | 2025-07-24 07:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| ce3a87ce-6f7b-3b1f-b536-9ce2e9382123 | -7.2597 | -43.0645 | 2025-07-24 07:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| 384f9618-17b2-367f-a1ac-2f4758abe748 | -7.2597 | -43.0645 | 2025-07-24 07:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 31409227-e0e0-3fb5-9e03-c7beab3b8a9e | -7.2597 | -43.0645 | 2025-07-24 07:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| 616cf222-a8ca-3349-9ffd-32c78aaee3cb | -7.2597 | -43.0645 | 2025-07-24 08:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 3f44dd80-aa0b-36dc-9467-c85fdd1a28c4 | -7.2597 | -43.0645 | 2025-07-24 08:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 59.6 |
| 12c6b37b-5d35-3466-9b2a-2b90e65871d5 | -6.9804 | -42.7854 | 2025-07-24 11:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 116.1 |
| ecb9ca46-7578-3090-b3c8-e99dd82ed780 | -6.9992 | -42.7836 | 2025-07-24 11:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 9d119f08-b7ee-369b-8fd6-563717d58fb1 | -6.9804 | -42.7854 | 2025-07-24 11:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 128.2 |
| b5076a90-d93f-31b6-9921-90f4b36c934d | -6.9992 | -42.7836 | 2025-07-24 11:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 4fce848e-96f9-34b3-9f07-951b74b3225c | -6.9992 | -42.7836 | 2025-07-24 11:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 23d5cc93-574a-34f1-8fc2-63f2dddff3b2 | -6.9804 | -42.7854 | 2025-07-24 11:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 165.6 |
| 2983bc17-e49c-3867-9ff7-94f614e7309e | -7.9557 | -46.2976 | 2025-07-24 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| c5f64bc1-edd1-3c82-b7c2-6a70a27600ba | -6.9992 | -42.7836 | 2025-07-24 11:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 4e1714b4-25dd-3087-818d-bd4a2c05108d | -6.9804 | -42.7854 | 2025-07-24 11:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 136.1 |
| 49758319-c043-3747-8038-cc78d9dee414 | -6.9804 | -42.7854 | 2025-07-24 12:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 102.6 |
| 53ad9d34-b150-3b5c-86c6-29c97c29779a | -6.9992 | -42.7836 | 2025-07-24 12:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 103.9 |
| b19f9d38-f848-3341-b93f-490a95955db2 | -6.9992 | -42.7836 | 2025-07-24 12:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| c7583b1c-7335-3c00-873e-4d4bdaff8196 | -6.9804 | -42.7854 | 2025-07-24 12:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| e9d6e5c9-4ccc-3ea0-91e8-3c0495ed3ee5 | -6.9804 | -42.7854 | 2025-07-24 12:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| a433e2ed-fa66-3d75-b684-af443ef08bee | -4.0569 | -42.5118 | 2025-07-24 12:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 9380ba76-aa38-3880-8a43-29c8f8995ea4 | -6.9992 | -42.7836 | 2025-07-24 12:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 122.0 |
| ca89764b-7b9a-3384-acbd-9187c150a8f9 | -5.82065 | -44.11275 | 2025-07-24 12:29:00 | TERRA_M-T | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 13b7ce23-b9c9-3491-a41d-efe38eff15bf | -5.63306 | -43.14331 | 2025-07-24 12:29:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 16.7 |
| bbec4835-f103-31fb-885e-d3b62e711575 | -4.78484 | -45.33087 | 2025-07-24 12:29:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5e218228-6dc2-3bbd-a56d-c2579bc40027 | -3.17731 | -49.44975 | 2025-07-24 12:29:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| c311fe4e-5ef1-3fbc-bdbf-01e2bec97d50 | -7.35315 | -45.30241 | 2025-07-24 12:29:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5d44e454-b185-3d03-b69a-540a025cc835 | -6.98037 | -42.78812 | 2025-07-24 12:29:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| e76cca95-fdcb-341e-9404-50472d183051 | -6.85974 | -42.79892 | 2025-07-24 12:29:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 9a1f0694-bacd-3e77-aed5-4dd68f40d12c | -5.62681 | -43.14805 | 2025-07-24 12:29:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 20.9 |


[Clique aqui para ver as próximas entradas](README26.md)
