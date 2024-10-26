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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28bd5de5-94f2-3826-82a8-47f5856b1283 | -17.254 | -57.4903 | 2024-10-26 04:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.3 |
| cf3a39ba-54ba-346e-89ce-f2a6173312ed | -17.6667 | -57.4822 | 2024-10-26 04:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 5926656c-b512-3257-b57a-727b4113c6e2 | -17.6865 | -57.4798 | 2024-10-26 04:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.4 |
| 06324da1-1862-3b74-8f1b-53bafa31278b | -17.745 | -57.5138 | 2024-10-26 04:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| c61dd8a4-cc2a-307d-bc0f-1808fe3f29d3 | -17.7647 | -57.5115 | 2024-10-26 04:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 0770a6d0-83d5-3836-ae80-b82c8bbd87e4 | -17.7674 | -57.3467 | 2024-10-26 04:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| c1d055f9-1047-3451-9467-dd98e5412bbb | -17.7868 | -57.3649 | 2024-10-26 04:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 919e5c50-e90e-34a7-b983-be4e5e646408 | -17.7872 | -57.3443 | 2024-10-26 04:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 336d0442-6dc2-3c0e-9c63-da434becdfba | -17.8239 | -57.5043 | 2024-10-26 04:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| ea693059-b799-3956-8e86-5cf0dbf33369 | -17.8243 | -57.4837 | 2024-10-26 04:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.7 |
| 0e258d31-44ef-379a-8490-2c6ed3f44e74 | -17.9418 | -57.531 | 2024-10-26 04:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 484f7e84-42b1-3e35-9444-6f4a9fbea082 | -17.9415 | -57.5516 | 2024-10-26 04:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 6fdb6a8f-d9de-3a50-a621-077615405aa6 | -17.8828 | -57.5177 | 2024-10-26 04:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.0 |
| 55b4e98d-ccee-3e8f-9127-998084b77079 | -17.8634 | -57.4995 | 2024-10-26 04:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.2 |
| ab2a033a-fd5d-3595-ac0b-73ba94d790e3 | -17.8631 | -57.5201 | 2024-10-26 04:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.3 |
| 8bdc9a7a-d787-3bbf-971c-57e7ca108afe | -17.8628 | -57.5407 | 2024-10-26 04:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 9a2cf8bd-54f3-38ae-83c1-f7fd572617dc | -18.0629 | -57.3721 | 2024-10-26 04:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.4 |
| c848323a-481f-35c7-8d1d-688b3d5892a8 | -18.0827 | -57.3696 | 2024-10-26 04:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.1 |
| 970171c5-89c3-3f8a-82c6-2f2b1258e2e1 | -18.64792 | -57.33553 | 2024-10-26 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 789dabeb-0dd2-340d-a561-3e93acd46ef5 | -22.69593 | -43.34897 | 2024-10-26 04:49:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 82c04219-dbe9-3a4d-a949-774f9a054262 | -24.88952 | -49.55004 | 2024-10-26 04:49:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 73820d8b-693c-3983-9b67-37f8484b7a61 | -24.88723 | -49.55169 | 2024-10-26 04:49:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 09bc2c8b-9276-34a0-b799-ed5976b8cf3d | -24.88537 | -49.54958 | 2024-10-26 04:49:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5b3ffa95-9dd2-3d47-ac08-03bd8245a651 | -22.60416 | -53.05851 | 2024-10-26 04:49:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 41f3c540-7db7-31c4-a6fb-26bbe8b53e22 | -20.47591 | -53.67622 | 2024-10-26 04:49:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86b0cde0-5a56-31ca-843b-f6ffdf2d3f5d | -21.23035 | -57.39327 | 2024-10-26 04:49:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2b63f95-68b2-3699-b164-67a95d270764 | -18.94726 | -56.32944 | 2024-10-26 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1df0b5a8-7a6a-3197-a344-21c8dd2ef549 | -18.51305 | -55.9707 | 2024-10-26 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1cbdc155-2267-3584-a5eb-d7aaa9b7b1be | -21.22683 | -57.39257 | 2024-10-26 04:49:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95479b9b-a707-33f0-ab45-141f4e3da060 | -29.19002 | -51.96406 | 2024-10-26 04:51:00 | NOAA-20 | ENCANTADO | RIO GRANDE DO SUL | Brasil | 4306809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 38c56a3a-ba66-3d17-8a24-56b33cb3bc11 | -25.7119 | -53.16247 | 2024-10-26 04:51:00 | NOAA-20 | DOIS VIZINHOS | PARANÁ | Brasil | 4107207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1501afb0-f3ed-3d81-9d86-b2a4c92cf258 | -25.70783 | -53.16608 | 2024-10-26 04:51:00 | NOAA-20 | DOIS VIZINHOS | PARANÁ | Brasil | 4107207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 962797c0-80eb-3712-9bdd-92d37e00d7c8 | -2.9945 | -50.4816 | 2024-10-26 04:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| c9b5df46-a291-372a-a000-88574b0537c1 | -3.013 | -50.481 | 2024-10-26 04:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 1b0f3b8a-db51-3a6d-a870-260c6f55b0cc | -3.4729 | -43.3377 | 2024-10-26 04:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| ae9e5d37-68b9-3852-ae36-9883e45e8413 | -3.473 | -43.3144 | 2024-10-26 04:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7e2b04c7-d6a8-370f-871d-5c46c0015159 | -4.5613 | -48.0358 | 2024-10-26 04:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 474259ac-0104-392d-a75b-b5cfa81b2b30 | -4.5614 | -48.0141 | 2024-10-26 04:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 3ad221c2-ee73-3c2e-8b31-da38b090b972 | -4.5799 | -48.0349 | 2024-10-26 04:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 141.1 |
| e00cfec0-d376-3657-a116-7fe37d95c00e | -4.58 | -48.0132 | 2024-10-26 04:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| adc6e465-f3bd-35ec-8cd7-a3bd297a4c55 | -17.254 | -57.4903 | 2024-10-26 04:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.3 |
| 722620d1-7ffa-3afb-bf0f-3acb74bc938a | -18.2649 | -55.9975 | 2024-10-26 04:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.5 |
| e0c2c0d1-ee46-3db5-8e80-179e0e70640c | -2.833 | -49.2413 | 2024-10-26 05:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 8e473064-d214-3ab8-bb12-d03b2e8d9516 | -2.9945 | -50.4816 | 2024-10-26 05:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c1cdbe31-8777-382f-a576-38cffc68f8f9 | -2.9501 | -52.5708 | 2024-10-26 05:05:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 64415f62-9b23-3be0-b522-25e536456344 | -3.013 | -50.481 | 2024-10-26 05:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 6eba2a7a-d3f6-31af-9787-edb9d0765740 | -3.473 | -43.3144 | 2024-10-26 05:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 3a02d826-231b-3410-b5ca-abdbbda8ec67 | -3.4729 | -43.3377 | 2024-10-26 05:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 26079e81-5889-3ca7-8fa3-c63d40e87714 | -4.5614 | -48.0141 | 2024-10-26 05:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| c76232d0-c8a0-3366-8988-7130a650c086 | -4.58 | -48.0132 | 2024-10-26 05:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 173.9 |
| 9c4ff583-c37f-3812-93a4-55e732db07c0 | -4.5799 | -48.0349 | 2024-10-26 05:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| aaaccd61-12d3-3aa2-923c-d928ce82e137 | -4.5613 | -48.0358 | 2024-10-26 05:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| fc554095-9e20-3e79-9eae-6c2362038f10 | -2.9501 | -52.5708 | 2024-10-26 05:15:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 75d1b0a2-2e8d-30fb-8b34-00b99496e527 | -2.9945 | -50.4816 | 2024-10-26 05:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 2df72dd3-fcb9-3428-8065-de61830cc706 | -3.013 | -50.481 | 2024-10-26 05:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| db116d88-304e-37d3-9292-ebad10162bfa | -3.473 | -43.3144 | 2024-10-26 05:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 81587932-16ff-3005-88b1-ed08f4817da7 | -3.4729 | -43.3377 | 2024-10-26 05:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| d2e562dd-28b1-347e-9d3e-8f784e1c332e | -4.58 | -48.0132 | 2024-10-26 05:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 145.9 |
| 740859c5-9174-3926-85d3-d1b9887a4191 | -4.5799 | -48.0349 | 2024-10-26 05:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 42331ac3-2922-3003-b9d1-1a8026323e1d | -4.5614 | -48.0141 | 2024-10-26 05:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 891af82e-fed0-3281-b259-c4b61b016ecd | -4.5613 | -48.0358 | 2024-10-26 05:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 638ac23c-da38-3038-ab25-d69e9868586f | -2.9945 | -50.4816 | 2024-10-26 05:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 87feae67-22cf-30e4-b584-76877bfcf141 | -2.9501 | -52.5708 | 2024-10-26 05:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 4d3ba51a-4708-34f5-a3bd-90c9a8a20b4e | -3.013 | -50.481 | 2024-10-26 05:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| ff01faca-2650-3868-8006-47fabae1574e | -3.473 | -43.3144 | 2024-10-26 05:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 7be7d487-c6a5-3318-ab0e-fd7b2b69f8e9 | -3.4729 | -43.3377 | 2024-10-26 05:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 3cffc35a-2150-3cc5-a25a-04c80889ca85 | -4.58 | -48.0132 | 2024-10-26 05:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 205.2 |
| b7bd0878-9f27-3192-82b2-8a6ed4d83c93 | -4.5799 | -48.0349 | 2024-10-26 05:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 30432851-00f4-325c-9cc1-35162bbede1b | -4.5614 | -48.0141 | 2024-10-26 05:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 9df35d95-020a-3b95-ba04-3fedcf80407d | -4.5613 | -48.0358 | 2024-10-26 05:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| b0326a4a-c50c-3e1a-bb98-7cda727571cd | -2.6581 | -49.51092 | 2024-10-26 05:33:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2a63963-89c6-31ef-8ecd-4e64301c14b8 | -2.65805 | -49.50818 | 2024-10-26 05:33:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a4337ae-fea5-33ff-bdc0-12bc27e4c60e | -2.65116 | -49.50983 | 2024-10-26 05:33:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15afee5d-5102-3fc7-97c8-09f6e901ee76 | -2.65111 | -49.50708 | 2024-10-26 05:33:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c5935de-f681-332d-9f49-b27029043019 | -2.60037 | -49.0999 | 2024-10-26 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a7f651d1-29f4-3ea8-89c9-f88a7dc105b9 | -2.47572 | -49.10831 | 2024-10-26 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e3db2d1-24bd-3b05-9d76-4a12cd5e4366 | -2.4721 | -49.10366 | 2024-10-26 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 25a2f062-50e1-3ecc-8035-c8e832ebec15 | -2.47107 | -49.1105 | 2024-10-26 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ccebd967-c149-392b-91ef-735b2ca1c398 | -2.46864 | -49.10715 | 2024-10-26 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9f7f973e-793f-3ec6-8226-be751e537bb5 | -2.46398 | -49.1094 | 2024-10-26 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1f48b92-2ffb-3147-ab51-b9e65101b5b6 | 1.79199 | -50.46194 | 2024-10-26 05:33:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 288b2d40-5ce8-3c73-b379-4f6ad26cf43f | 1.79168 | -50.46183 | 2024-10-26 05:33:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 66b11d2a-af7e-37cc-a395-4e92cee38664 | 1.79123 | -50.45718 | 2024-10-26 05:33:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a419664d-e463-3e29-a9ed-5f21c7e9bdeb | 1.79089 | -50.45709 | 2024-10-26 05:33:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dc547135-142c-3113-a5f9-e77478b08e1e | 1.78584 | -50.46304 | 2024-10-26 05:33:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0bb56732-cb9b-3dbf-a4b3-3c1204763fe2 | 1.78554 | -50.46292 | 2024-10-26 05:33:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8b3d4590-84a0-3a8f-9298-75a9301d323c | 0.31078 | -50.99994 | 2024-10-26 05:33:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf7822d3-c4b4-3ef8-beab-b935a3f01cd8 | 0.31006 | -50.99538 | 2024-10-26 05:33:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e5022b0-72f3-31c6-b177-2b88528dfef3 | -0.09886 | -51.32616 | 2024-10-26 05:33:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03492645-2fee-30e0-92d7-89e76faffac1 | 3.64378 | -51.28455 | 2024-10-26 05:33:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb01da6e-7a74-3633-a5f0-60e491fc6fd6 | 3.64108 | -51.28447 | 2024-10-26 05:33:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1b13c240-b629-31da-a01c-c3a7d981634b | 3.63879 | -51.28947 | 2024-10-26 05:33:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f65ecba6-7d67-3b0c-85a2-f5538e029c26 | 3.63812 | -51.28556 | 2024-10-26 05:33:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d6fd8d90-c2d4-35d9-bb2b-e3060ab97352 | 3.63606 | -51.2894 | 2024-10-26 05:33:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8aa2bd33-ed91-344a-b77d-54eea482055a | 3.63542 | -51.28549 | 2024-10-26 05:33:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65f7cd8c-d2a1-3f46-a1e1-7a39ff4265bd | 3.6134 | -51.29345 | 2024-10-26 05:33:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06f2609a-b127-3cf7-873b-8853e4c6bcd2 | 3.60773 | -51.29446 | 2024-10-26 05:33:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff31c037-5bee-3135-876b-36ce5dfbe330 | 3.43266 | -51.27494 | 2024-10-26 05:33:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58b74e08-3b09-35d4-96d2-f6d945e4a99e | 3.43069 | -51.27669 | 2024-10-26 05:33:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1ac300f-a817-3ff1-8c2c-d650d35b13f5 | 2.78964 | -50.9326 | 2024-10-26 05:33:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README92.md)
