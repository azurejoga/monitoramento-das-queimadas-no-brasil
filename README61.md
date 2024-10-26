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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f64fb79-c835-3e8d-8836-87aba5d82c00 | -17.7872 | -57.3443 | 2024-10-26 04:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.4 |
| 916bcc56-fca1-3bc2-8bb5-6d4164b8ea48 | -17.8628 | -57.5407 | 2024-10-26 04:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.8 |
| 4471eb30-9f11-362e-aa27-d62d917f6fe9 | -17.8631 | -57.5201 | 2024-10-26 04:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.1 |
| a4bee990-d3f0-35d2-a238-b5e197d25943 | -17.8634 | -57.4995 | 2024-10-26 04:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.9 |
| e0037874-2c09-35c7-9c64-10c21a1d2a69 | -17.8828 | -57.5177 | 2024-10-26 04:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.8 |
| bdd88597-4d87-3d96-a57b-efacf9deffef | -17.8832 | -57.4971 | 2024-10-26 04:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.2 |
| eef69384-f8db-3846-b0b8-33cbd9dd942a | -17.9415 | -57.5516 | 2024-10-26 04:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 10bb9125-ad4e-32ce-8956-bbdf030ea458 | -18.0629 | -57.3721 | 2024-10-26 04:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.0 |
| ea3bc781-6f16-37af-a3b4-2576728f2eec | -18.0632 | -57.3514 | 2024-10-26 04:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.5 |
| b4aa12b8-9b9b-34a3-bc01-abe192d3e732 | -18.0827 | -57.3696 | 2024-10-26 04:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.3 |
| 06f5000b-fa41-39ea-b542-27542a520895 | -18.083 | -57.3489 | 2024-10-26 04:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 1d3c4e2a-333e-310a-b1e6-044a50278124 | -18.1025 | -57.3671 | 2024-10-26 04:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.9 |
| c6f045dc-0786-3ee7-aa6f-3b6cb49c08a5 | -18.2649 | -55.9975 | 2024-10-26 04:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 8bb614a2-6c95-3e18-9b95-2b4542aae988 | -11.88708 | -43.04699 | 2024-10-26 04:29:00 | AQUA_M-M | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 06dc839f-0960-33ab-818f-f0388209649b | -2.9501 | -52.5708 | 2024-10-26 04:35:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| d5010f6f-ec27-32f1-ab0c-4a991f21b397 | -2.9501 | -52.5504 | 2024-10-26 04:35:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 734a0c04-ad42-3d6a-a9b8-25dcc80a3e49 | -2.9945 | -50.4816 | 2024-10-26 04:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 28539588-754e-39ea-b14b-0141450d1579 | -3.013 | -50.481 | 2024-10-26 04:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 8537ff1c-19f4-38ce-a290-1667b53a9b22 | -3.2213 | -45.1572 | 2024-10-26 04:35:23 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| a6972dae-0bdd-3caf-85ca-31094dc571f9 | -3.4729 | -43.3377 | 2024-10-26 04:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 72395977-fd29-3f37-a9a3-58b6002f6678 | -3.473 | -43.3144 | 2024-10-26 04:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 99c530d0-8279-3e41-a28b-621e22525122 | -3.6084 | -45.8147 | 2024-10-26 04:35:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 78.8 |
| b92a0b98-4e48-3651-ac31-3bdabd256061 | -4.5613 | -48.0358 | 2024-10-26 04:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 43569c1a-2d83-3d2e-9292-348addf33199 | -4.5799 | -48.0349 | 2024-10-26 04:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 182.9 |
| 85fcf9a2-c495-381e-90e0-18ea39444a3c | -4.58 | -48.0132 | 2024-10-26 04:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 189.5 |
| 49d3ec1d-2072-3b61-bbb7-244b9be26b97 | -7.6474 | -63.4584 | 2024-10-26 04:35:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c8083cfd-8e93-3c44-bf22-9c4b4d787d66 | -17.0499 | -53.452 | 2024-10-26 04:36:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 9bfbd069-ac01-3644-aa6e-159ef06a9175 | -17.254 | -57.4903 | 2024-10-26 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| 018133b6-bc24-3c58-ae13-4bd0e77f6bd0 | -17.6865 | -57.4798 | 2024-10-26 04:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.1 |
| f3d9c971-e85a-34c3-95df-e273b797a547 | -17.7446 | -57.5344 | 2024-10-26 04:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 102ceff9-f666-3c4a-8150-4d2019f56cec | -17.745 | -57.5138 | 2024-10-26 04:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 49f5a89c-09fe-3946-bae5-e6e57706d824 | -17.7647 | -57.5115 | 2024-10-26 04:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| 21a67d70-5c12-3474-8c4e-e10189e01b3c | -17.7674 | -57.3467 | 2024-10-26 04:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| ee2fb07b-688e-3a90-a85d-9343ab9c210f | -17.7868 | -57.3649 | 2024-10-26 04:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.5 |
| d35104e9-a115-3a66-b467-172ab975dedf | -17.7872 | -57.3443 | 2024-10-26 04:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 515210ff-e757-34a4-b7a1-b98c13889c54 | -17.6667 | -57.4822 | 2024-10-26 04:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 193171e8-1ac6-3501-9004-ea40966cf330 | -17.6861 | -57.5004 | 2024-10-26 04:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.1 |
| bc9de88f-b2bd-3e5e-bb7a-15fd337f322e | -17.8617 | -57.6024 | 2024-10-26 04:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.9 |
| a4ce0e36-dc2b-31bc-9f0f-947734bab9bf | -17.8621 | -57.5818 | 2024-10-26 04:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.0 |
| 3fe68f00-0ac1-3ff3-9fe6-6b02dea32b8c | -17.9415 | -57.5516 | 2024-10-26 04:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 074a50d8-8a88-30dd-99a7-ee140b4dd18f | -17.9418 | -57.531 | 2024-10-26 04:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 0dd52faf-54b5-33a5-87ce-740ef74154c5 | -18.0629 | -57.3721 | 2024-10-26 04:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.1 |
| 2695d06e-6e82-3548-a70f-25cefb748910 | -18.0632 | -57.3514 | 2024-10-26 04:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 69cf9001-af00-399e-8c7f-0b9d11759cec | -18.0827 | -57.3696 | 2024-10-26 04:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.4 |
| bf2fe36d-1cc7-3d94-9ee6-260affd33adf | -18.083 | -57.3489 | 2024-10-26 04:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.7 |
| 89d534a9-55d2-3507-bf57-cc5cf416864e | 3.77754 | -51.81654 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 541100a1-d53d-36f3-a8cd-23e51f7d6c9d | 3.6499 | -51.28898 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf5e2e6e-ba8f-3294-a3a1-39fddcac22a5 | 3.64582 | -51.28564 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c3b2384e-1943-38ee-939a-2f356f7ec479 | 3.64233 | -51.28617 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 872c925c-1521-371e-898f-a8c0355bd607 | 3.6415 | -51.28872 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dfa78d95-7973-3239-8b51-a75b693438f8 | 3.64089 | -51.28485 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d337f323-fa55-3f97-9904-51abd6b09ade | 3.63942 | -51.2906 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d00523e-fd19-351e-8c1d-48e18e9b8b41 | 3.63883 | -51.28671 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b5459f2c-7531-3201-ac71-e9d4b33265ae | 3.638 | -51.28926 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61056e02-4bff-37ea-82ab-3b274cf29de2 | 3.61355 | -51.29301 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c46383af-36da-3783-a384-4273aec47b36 | 3.61006 | -51.29354 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| db16463e-eb31-34ac-aa42-260a5846a64c | 3.46406 | -51.26012 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84433598-dcf1-3f52-ba89-610c262c90d1 | 3.46057 | -51.26065 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9540440f-260d-3183-baa5-39f40374db7f | 3.43629 | -51.31187 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecef45d8-6304-3517-bb00-a8dba5753c9e | 3.43447 | -51.27652 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f15fe118-6cb5-3a68-955c-39704e6478e4 | 3.4328 | -51.3124 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4ed7b96-e894-3b23-b36a-7179cfbc3ea6 | 3.43221 | -51.30854 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6743a607-cf44-3a79-b9bb-cafd3e08f11c | 3.38532 | -51.29119 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15e833e7-62ab-3ccb-bb7c-e53bd9d0a219 | 3.38472 | -51.28733 | 2024-10-26 04:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21a18e8e-235f-3b49-bedc-06bf272c7c8b | 2.80326 | -50.92944 | 2024-10-26 04:40:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0507a43-6504-3b03-8c70-324e406b5a37 | 2.80268 | -50.92574 | 2024-10-26 04:40:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2bf1082-e808-32de-8c21-2727f90a71d7 | 2.79984 | -50.92997 | 2024-10-26 04:40:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 390a9d32-0865-37d5-8db8-4c4da5919bbd | 2.79243 | -50.92732 | 2024-10-26 04:40:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd64cc69-4f45-3f55-a7b2-61022a1aa706 | 2.7919 | -50.94636 | 2024-10-26 04:40:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5df32375-7e66-360a-8478-f0d1a66396df | 2.79016 | -50.93525 | 2024-10-26 04:40:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b6624909-5273-3a6c-be97-d5af548b495c | 2.78958 | -50.93155 | 2024-10-26 04:40:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7d620afa-2019-3b00-873b-d14dd87c9e6a | 2.78901 | -50.92785 | 2024-10-26 04:40:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9329858d-f596-31e9-b2f7-cc45e4be72d8 | 1.57508 | -55.6417 | 2024-10-26 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c16014f4-bcbf-3bff-b5ce-a9598ffbaec5 | 1.57067 | -55.6424 | 2024-10-26 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 255675ef-e348-3605-afb9-a624dba17d1d | 1.56625 | -55.64308 | 2024-10-26 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd644806-49de-3a46-ad5b-fb26d73d1e5c | 1.56182 | -55.64375 | 2024-10-26 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce87244f-e807-37de-b4e9-74d6cc367868 | -2.04464 | -56.09261 | 2024-10-26 04:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2deef5ab-4c61-31f6-988b-5cc95ba00bd8 | -1.96351 | -56.39974 | 2024-10-26 04:42:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f9f6226-7d5e-3a66-ac23-9913c74857fe | -1.79721 | -55.58517 | 2024-10-26 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc4508c2-04bc-3c16-b0b4-5ec1fd204922 | -1.6797 | -55.3095 | 2024-10-26 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 71e33fd3-ecc0-350e-a052-9b4ba5658527 | -1.52624 | -55.40847 | 2024-10-26 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02632d33-da0d-3803-a1c1-467b858c6421 | -1.52388 | -55.90969 | 2024-10-26 04:42:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90e8ef35-14a2-31ad-81fc-1b0b2cd8e611 | -1.51976 | -55.36913 | 2024-10-26 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a5b69fc-42e7-3ac7-adbe-088f119020a8 | -1.48875 | -55.86515 | 2024-10-26 04:42:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e9271c8-3d2a-3c7e-a1ab-75920c35dbb8 | -1.48812 | -55.86918 | 2024-10-26 04:42:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 512a6250-e454-3c8a-850c-42c9da279ef7 | -1.45288 | -54.95347 | 2024-10-26 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f358608f-60e4-3595-aae6-a22d4dc52d5f | -1.38427 | -55.40518 | 2024-10-26 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 52587845-bdec-370b-9122-bfda4c48ded1 | -1.38368 | -55.84469 | 2024-10-26 04:42:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d7d6e07-5185-31e8-855d-a7b19f3bec7c | -1.38065 | -55.83602 | 2024-10-26 04:42:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5af9d002-ab8f-3773-b278-3fa80e3e5284 | -1.38002 | -55.84005 | 2024-10-26 04:42:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cf3b287-06bb-38c0-ba45-d536460653f2 | -1.37939 | -55.84407 | 2024-10-26 04:42:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1049b988-eb9e-36b0-9b52-6196acbaacac | -1.37876 | -55.84809 | 2024-10-26 04:42:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7c15050-198e-3d8f-970d-01e4c5fa5a41 | -1.37257 | -55.85957 | 2024-10-26 04:42:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15697947-8b8d-32aa-91f9-a668660c9ac4 | -1.37194 | -55.86361 | 2024-10-26 04:42:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa176900-4482-3990-b267-767b3029e0aa | -1.36764 | -55.86296 | 2024-10-26 04:42:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a060b384-4158-3747-83a5-2afa09ac8294 | -1.35287 | -55.49359 | 2024-10-26 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 213710ed-d94c-387d-b836-dd7d58bb7e96 | -1.35224 | -55.49743 | 2024-10-26 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0272ce27-5b8e-38f4-a18e-c7c77542d24d | -1.34869 | -55.49289 | 2024-10-26 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9782feb5-27b8-3751-b45f-dc8c71354e5a | -1.34402 | -55.73605 | 2024-10-26 04:42:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fff71a0f-632e-39d1-949b-711975ad599e | -1.32438 | -55.96902 | 2024-10-26 04:42:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README62.md)
