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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ba30844-f02e-3e0d-a423-5525409c09ed | -17.9858 | -57.258 | 2024-10-18 08:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 2fdd3b1b-2437-3440-8f1c-bed52f1684e8 | -17.9855 | -57.2786 | 2024-10-18 08:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.7 |
| 4be22ca5-66a7-341a-880a-4ff9772726d3 | -17.9234 | -57.451 | 2024-10-18 08:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 00c6bf68-e3a5-34de-b7be-fb31bcfd5f3c | -17.9036 | -57.4534 | 2024-10-18 08:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 44a868b1-e4d7-3e50-af73-8c0e62c5e070 | -17.8876 | -57.229 | 2024-10-18 08:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.7 |
| c3ffa8d6-b9df-3eab-98f1-91dbd9a394cb | -12.4958 | -63.3024 | 2024-10-18 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 9652f50a-9846-3291-b9d5-76201456cb84 | -12.5338 | -63.2812 | 2024-10-18 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 9d4e078c-bdaf-3b75-81f8-e981fdc1a6c1 | -12.5336 | -63.3003 | 2024-10-18 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 10831087-074b-3b86-836d-b5da387dc60c | -12.5155 | -63.2055 | 2024-10-18 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 86656a9f-92ce-311b-9470-d08643e013a6 | -12.5149 | -63.2822 | 2024-10-18 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 23346331-e4ec-34ef-851a-a8fb48c32bab | -12.5147 | -63.3014 | 2024-10-18 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 1b500492-84c8-37f3-b2a3-9bf655f27816 | -12.4967 | -63.1874 | 2024-10-18 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 28b2fb07-29a2-3dca-a875-7aa7d1eafec4 | -12.4966 | -63.2066 | 2024-10-18 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 0a24f9c5-f8e4-3ee5-8688-67083c62882b | -12.496 | -63.2832 | 2024-10-18 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 721967fd-e5f7-324f-8c0b-677eb559e670 | -17.2277 | -56.6922 | 2024-10-18 08:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.9 |
| 72ea6126-c274-398c-8de4-bb84f6247769 | -17.2177 | -57.3102 | 2024-10-18 08:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| abd19e4e-d37f-3d5d-a9f8-0eb9aef29d3e | -17.2373 | -57.3079 | 2024-10-18 08:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.8 |
| 3773cd32-0041-35fb-961c-8017a8443576 | -17.237 | -57.3284 | 2024-10-18 08:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 56f08a36-401b-311b-88cf-7073f5e7774d | -17.8246 | -57.4631 | 2024-10-18 08:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| bd4b9205-6aec-3a9c-9511-22d800f4e7a5 | -17.844 | -57.4813 | 2024-10-18 08:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.7 |
| 8430a3ba-24dd-3545-9c02-7b0c41fd35a4 | -17.8444 | -57.4607 | 2024-10-18 08:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 52425ee1-39a3-3419-8301-33617cb100c4 | -17.8059 | -57.4037 | 2024-10-18 08:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 3d05270a-0863-3afb-b8d5-8830de3497e3 | -17.8243 | -57.4837 | 2024-10-18 08:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.7 |
| db5395e6-43f2-36fd-a342-34678b2e6103 | -18.0056 | -57.2555 | 2024-10-18 08:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 1ce68db8-01eb-3b00-9ac4-60cb6359360a | -18.0052 | -57.2762 | 2024-10-18 08:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.8 |
| aa6f035f-6b00-3f66-863d-68ffa838e49d | -17.9858 | -57.258 | 2024-10-18 08:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 1800f54f-8cb3-333a-82b9-76f0a7c9a964 | -17.9855 | -57.2786 | 2024-10-18 08:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.5 |
| 2f9d9c85-10d2-3bde-aa3b-7d04170d128c | -12.5338 | -63.2812 | 2024-10-18 08:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| b128c207-2bcb-3871-972c-7f89cb3ad4be | -12.5149 | -63.2822 | 2024-10-18 08:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 4cada49f-5b1e-31dc-bd3f-c7068d041abb | -12.5147 | -63.3014 | 2024-10-18 08:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 598c7463-a39b-34ce-a90a-a2177694c2e3 | -12.4966 | -63.2066 | 2024-10-18 08:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 3b38788b-8da0-3f1f-ba19-29aa4afb5199 | -12.5336 | -63.3003 | 2024-10-18 08:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| a18d2443-09be-3aae-aee9-06e89d1d88bc | -17.2177 | -57.3102 | 2024-10-18 08:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.6 |
| 1cf70e96-e3f6-3454-97b1-45d1cbd50b85 | -17.237 | -57.3284 | 2024-10-18 08:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.2 |
| 29c55ce3-6827-3d5a-873c-f3c12660eddf | -17.2373 | -57.3079 | 2024-10-18 08:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.6 |
| 9642c89c-f62a-31b0-87d5-51df939687cb | -17.8243 | -57.4837 | 2024-10-18 08:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 172.1 |
| efd142d0-7b87-38a3-a84a-79d57bd9f63e | -17.8246 | -57.4631 | 2024-10-18 08:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 2407645f-85ff-3d35-98f6-24ffbd112d38 | -17.844 | -57.4813 | 2024-10-18 08:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 201.8 |
| 3932ac6d-4281-308f-9557-50ff6f63cfed | -17.8444 | -57.4607 | 2024-10-18 08:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 2a13d6c4-ab5d-3089-8a76-0362af1c1f54 | -18.0052 | -57.2762 | 2024-10-18 08:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.7 |
| 5789a274-e6af-3dc4-88cb-7359a7d7e595 | -17.9858 | -57.258 | 2024-10-18 08:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 161af9df-ec52-3a9a-b44c-4aaa7b6bd6d3 | -17.9855 | -57.2786 | 2024-10-18 08:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.4 |
| f950ac6d-89a8-33c7-8af2-c5cdb637fee0 | -17.9234 | -57.451 | 2024-10-18 08:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.3 |
| de370643-ba60-3917-b924-38068f19c3ab | -17.844 | -57.4813 | 2024-10-18 10:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| ab3b2d55-1ebb-31b0-895f-c281d1f83c4b | -17.844 | -57.4813 | 2024-10-18 10:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 171.8 |
| 90e5a465-93db-3cda-83b4-b9af484059ad | -17.8243 | -57.4837 | 2024-10-18 10:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.1 |
| 84ef0ef1-f103-37b1-adc6-3f69c59253f2 | -17.8876 | -57.229 | 2024-10-18 12:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.0 |
| fb4d81fa-7859-3236-83a1-e933e04771e4 | -17.2177 | -57.3102 | 2024-10-18 12:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.7 |
| 2c3dd35b-265e-3560-90a6-af32331389c2 | -17.2277 | -56.6922 | 2024-10-18 12:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.8 |
| bc11cbf8-1b6e-3d1f-a85b-5dba4d5aaef8 | -16.9995 | -57.4791 | 2024-10-18 12:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.5 |
| 7128789a-8699-3efa-ba4f-22d7fe95b36e | -17.2177 | -57.3102 | 2024-10-18 12:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.5 |
| 5760778c-c9e9-321f-8b46-570573981e3c | -17.2173 | -57.3307 | 2024-10-18 12:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.7 |
| 7c157fe9-86cc-30aa-aaa4-222db720256d | -17.2277 | -56.6922 | 2024-10-18 12:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.3 |
| 9c22ad04-a141-3d8f-879c-906c926213c7 | -16.9995 | -57.4791 | 2024-10-18 13:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.2 |
| ae49c212-1cf2-3f92-bf9b-524841c70f4e | -17.2173 | -57.3307 | 2024-10-18 13:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.2 |
| afd88e88-7237-3bdd-b3e7-0deb84f0a733 | -6.6886 | -70.1171 | 2024-10-18 13:15:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| c8187b6d-a2bc-3967-bbe1-4ee841f07200 | -16.9992 | -57.4995 | 2024-10-18 13:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.7 |
| d568d57c-8d4a-3304-8234-00517cd4d244 | -17.2081 | -56.6946 | 2024-10-18 13:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.6 |
| 329a484e-542d-34b1-b899-e41b747fca7d | -17.2173 | -57.3307 | 2024-10-18 13:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.7 |
| 917820f7-4341-36ad-923d-45221f01039a | -6.6886 | -70.1171 | 2024-10-18 13:35:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 807ca339-b19b-3a24-9f29-a622d961d87d | -6.6703 | -70.1174 | 2024-10-18 13:35:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 82b2439e-7a5b-314d-93cb-33e3948759ee | -17.02 | -57.4153 | 2024-10-18 13:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.0 |
| 837b7709-218e-30be-9635-83ac96f45c52 | -16.9805 | -57.4404 | 2024-10-18 13:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.8 |
| 8001d859-322b-3abf-898e-229442e995cf | -16.9802 | -57.4609 | 2024-10-18 13:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| 20ba4ca4-9bde-365f-a617-7304af359169 | -17.0878 | -56.8534 | 2024-10-18 13:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.9 |
| 2eb4b7f9-94d7-3360-bed2-8246dfcda2b7 | -17.1071 | -56.8716 | 2024-10-18 13:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.6 |
| 1883b3a2-4b82-3481-b56d-0cf338a84916 | -16.9714 | -56.7852 | 2024-10-18 13:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.9 |
| b1b63cc5-fb57-3baa-957b-91564dd3e114 | -16.9998 | -57.4586 | 2024-10-18 13:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.7 |
| 206c3478-a384-30ac-8a52-9fea49bf5e26 | -17.0001 | -57.4381 | 2024-10-18 13:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.3 |
| f2c7bc62-222d-3bcb-9977-faa0f59ab0e7 | -17.0795 | -57.3674 | 2024-10-18 13:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| 2284ead8-9498-34b4-8ad2-94f0de9ae9b3 | -17.1529 | -56.4745 | 2024-10-18 13:36:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 106.9 |
| d1dc263d-fcdb-3ff5-8cc7-21862680a6ee | -17.2177 | -57.3102 | 2024-10-18 13:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 177.0 |
| 5ab55701-bbed-329c-9ecb-31bc8addb782 | -17.1267 | -56.8693 | 2024-10-18 13:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 92b97aa0-53ca-398d-8104-18c9fbbbdb9e | -17.2081 | -56.6946 | 2024-10-18 13:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.9 |
| 439d31db-6972-3f84-8fe3-f2e8f43bb038 | -17.2173 | -57.3307 | 2024-10-18 13:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.8 |
| 1c6c3b99-adf5-3a84-847e-d0c42efa62cd | -17.8277 | -57.2776 | 2024-10-18 13:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 98bb4452-32c8-3208-be50-2220b80a337c | -6.6886 | -70.1171 | 2024-10-18 13:45:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 1a983956-489b-3a63-82e1-e137747f4983 | -6.6703 | -70.1174 | 2024-10-18 13:45:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| ab3be592-2ab0-3fee-a7c2-ccbb1a980e87 | -10.5749 | -67.7755 | 2024-10-18 13:46:07 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 74.4 |
| cb41762e-eb0b-33bc-8918-38e52c450082 | -17.0599 | -57.3697 | 2024-10-18 13:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.9 |
| a5bb7c10-f594-3964-9f63-ff6e667733d4 | -17.0603 | -57.3492 | 2024-10-18 13:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.5 |
| f7297ae8-ab7d-3b0d-9118-12bc99520e7a | -17.0001 | -57.4381 | 2024-10-18 13:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.8 |
| f9968a74-bba1-3ec7-8bde-e78313b7c939 | -17.0795 | -57.3674 | 2024-10-18 13:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.6 |
| 6e76e8a8-7389-3f3d-a63d-70c1127f6209 | -17.02 | -57.4153 | 2024-10-18 13:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.5 |
| 22661634-11b0-37e4-8401-51c36a735a7e | -16.9805 | -57.4404 | 2024-10-18 13:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.8 |
| 2dc424ba-44d7-3d4e-a82a-8186b2ed629c | -16.9802 | -57.4609 | 2024-10-18 13:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.4 |
| fd993a1c-acf8-3ce5-a509-f615a91c5bc2 | -17.0406 | -57.3515 | 2024-10-18 13:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.6 |
| 20c46eb8-ff48-3bef-99eb-96ebf70ebc94 | -17.1671 | -56.8026 | 2024-10-18 13:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.1 |
| 231082bf-a34b-31f9-aedf-cf1528cebde4 | -17.2081 | -56.6946 | 2024-10-18 13:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.6 |
| 26090e8f-3d6c-303e-aaa6-e78c834fd0ed | -17.1529 | -56.4745 | 2024-10-18 13:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 111.7 |
| 4d0d268c-c99c-3b43-84e0-04d228abdff2 | -17.1784 | -57.3148 | 2024-10-18 13:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.0 |
| 08e5f354-17eb-3743-acac-c0ea1b80e8d5 | -17.8277 | -57.2776 | 2024-10-18 13:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.2 |
| 6b5e4bbc-fcb0-3cd3-90f2-e15ef6659ad7 | -6.6886 | -70.1171 | 2024-10-18 13:55:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 04d03dd5-e1ab-33de-9332-2ec75882ea82 | -6.6703 | -70.1174 | 2024-10-18 13:55:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 9ae94372-ae5a-3a96-a4e9-ee5f8949607b | -17.0204 | -57.3948 | 2024-10-18 13:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.3 |
| f2069b8b-8706-3ace-af35-6e41b2200b8e | -17.0001 | -57.4381 | 2024-10-18 13:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.3 |
| d3538576-273f-3e91-b1a8-2ca71ea78a56 | -16.9802 | -57.4609 | 2024-10-18 13:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.7 |
| a782d963-4057-3a89-aa50-8cfb8d2c636d | -17.02 | -57.4153 | 2024-10-18 13:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.1 |
| 3827ebdc-3d4b-395e-a330-cba4d14eb050 | -17.0564 | -56.3832 | 2024-10-18 13:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 102.5 |
| 0df4bc99-9fb6-351a-8cfc-a639fffb321c | -17.0197 | -57.4358 | 2024-10-18 13:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.7 |


[Clique aqui para ver as próximas entradas](README33.md)
