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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c86b60bb-03bb-3299-877a-b572bdbeb353 | -12.84071 | -48.45182 | 2026-08-21 05:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05a96d93-040c-32f4-b409-7657eb872be7 | -12.80262 | -48.42356 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23f71352-3767-3cec-9f19-bc07674816bc | -9.41466 | -60.42784 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb718245-faa0-3fb9-a4fc-6d09da492290 | -11.20735 | -55.06533 | 2026-08-21 05:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5938fd1-fa4c-321a-b311-05527f793eb6 | -12.85482 | -48.43264 | 2026-08-21 05:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 877f2e14-cf3a-3d22-b46e-a9484a2ea3b3 | -12.12424 | -57.20953 | 2026-08-21 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54f48b70-4b21-3bb8-9d3f-9c534435dcc2 | -19.90829 | -47.38013 | 2026-08-21 05:25:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02595026-c250-32c0-8c8e-ab6c16b20f1b | -20.27047 | -46.74988 | 2026-08-21 05:25:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 790b89e8-7d8b-36af-a2cd-aee8e0b0c6ad | -10.45335 | -54.66322 | 2026-08-21 05:25:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b4ae161-3f1d-37f1-b8b9-25a2081d275b | -9.40824 | -60.55395 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f123c72-334c-3a80-b7fc-eaab38ed00f7 | -11.18349 | -54.0137 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5eab0bd0-18d7-3f1a-a8a3-86121ed9e535 | -12.00364 | -53.42729 | 2026-08-21 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15008b76-4a9a-35bc-894c-1d20cfda570a | -10.84079 | -57.52357 | 2026-08-21 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a762353-e374-3340-aa74-959df609d2e9 | -19.73802 | -57.97563 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ffb9f4e3-be7b-313a-a5f9-33445dbf9d68 | -12.80373 | -48.41397 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8eaa8740-209b-3631-a6eb-be1a4fdaf692 | -11.81856 | -56.60021 | 2026-08-21 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f31c161-c8df-31c2-bb1e-dae70188d5c5 | -9.41876 | -60.42455 | 2026-08-21 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9690f2b-3774-3a24-81ca-5a8ed69326ff | -11.16852 | -54.0064 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 437313a7-96da-3ada-ad90-6a240b87300e | -12.76147 | -48.47329 | 2026-08-21 05:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1af0b23-42bf-34e6-b6a2-0fe7cb567bf2 | -10.76095 | -50.31202 | 2026-08-21 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 621c8124-8851-3dad-8ae5-83db0811251f | -11.16315 | -54.01589 | 2026-08-21 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e0684119-09ca-36cb-829a-069a75e4059b | -19.72922 | -57.9615 | 2026-08-21 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 2daf8b37-960f-386f-9d54-3ec0eac64115 | -11.84425 | -58.84789 | 2026-08-21 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 752deb7a-7e1f-3c1e-9464-4818161aa9b1 | -22.29603 | -51.83203 | 2026-08-21 05:25:00 | NPP-375D | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 05b8a447-b2ca-3d1a-9d94-d61f8d3dbf97 | -10.24243 | -54.37081 | 2026-08-21 05:25:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff6d1935-db7e-3922-b7d1-6589fbab4485 | -9.21589 | -60.77721 | 2026-08-21 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0682f618-dc35-31d2-9d0e-a7c27c2f6849 | -13.3731 | -54.3986 | 2026-08-21 05:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| b2fd15ad-42f5-38c0-8158-45f3647c8ab4 | -19.7438 | -57.9633 | 2026-08-21 05:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.1 |
| 41fa8c00-fecd-3e42-ac3f-34527e6f39e7 | -13.4117 | -54.3737 | 2026-08-21 05:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 854ea391-2288-3ad2-accf-099c9050c3d0 | -9.4069 | -60.4362 | 2026-08-21 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 121.6 |
| b556aea9-bcc9-31db-b617-519a88e27657 | -6.2341 | -55.6109 | 2026-08-21 05:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 75898f45-caef-352b-b0e0-1c52c48b6e20 | -19.7435 | -57.9841 | 2026-08-21 05:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.5 |
| a81e9ca3-621b-3f34-9729-c1043af3bf04 | -3.5406 | -48.1889 | 2026-08-21 05:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 2f6010d7-9e53-300a-a673-6dbb0a77850c | -9.4071 | -60.417 | 2026-08-21 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 303.1 |
| 9f5e5dc2-f979-3ba4-b21a-fb63ed96f820 | -19.7238 | -57.966 | 2026-08-21 05:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 784c6b21-2347-3499-bff4-b945e0eac648 | -13.3734 | -54.3779 | 2026-08-21 05:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 160.5 |
| 625086e8-70b3-3f7e-8bdf-4ccfcc88afab | -6.8755 | -59.4364 | 2026-08-21 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 23b8ea79-94dd-37d5-af0d-bc4f6bc6dd30 | -9.4257 | -60.416 | 2026-08-21 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 08dca75c-ed22-3b14-9a7b-5ce6d47d9984 | -13.3923 | -54.3965 | 2026-08-21 05:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 2266a6be-658b-3400-b3f6-6359c825bf9b | -9.4072 | -60.3977 | 2026-08-21 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 6eb6659e-c82e-3ec9-9aa9-623ba8b83f04 | -7.3791 | -45.8119 | 2026-08-21 05:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 839b0979-6fc6-340f-bf46-71b5c36c0407 | -11.1747 | -54.0216 | 2026-08-21 05:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| ced2055d-ca50-31d8-adc9-21ecdece3e73 | -9.4259 | -60.3967 | 2026-08-21 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 41b079c0-373d-37b0-8130-ebd136520cfb | -7.3603 | -45.8136 | 2026-08-21 05:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| b0bd6694-9377-3943-b57e-c822fe569b37 | -13.3926 | -54.3758 | 2026-08-21 05:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 218.3 |
| 6eb8d5e8-7e87-3d8d-9dc5-970b91197cb2 | -6.2156 | -55.6118 | 2026-08-21 05:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| ad4732dd-2d96-391a-802a-864e160d0632 | -8.3718 | -62.697 | 2026-08-21 05:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 5e72c186-e3ef-3122-8961-c9b00aa66902 | -8.3903 | -62.6963 | 2026-08-21 05:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 123ea591-64ab-3e78-a703-f2f850cc661b | -14.3149 | -51.8969 | 2026-08-21 05:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| b87872df-5186-3cf3-a8bb-d3091320b044 | -9.3885 | -60.4179 | 2026-08-21 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 6acebcc8-3e0f-38f8-81c9-4600cadc0b74 | -6.8939 | -59.4356 | 2026-08-21 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| eb7c82bb-e447-3fb1-9687-015e24b25828 | -6.857 | -59.4371 | 2026-08-21 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 28812a88-3e8a-3bd2-93a8-2aa28daf2a4f | -9.4072 | -60.3977 | 2026-08-21 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 8f9b3e7c-868a-3b6c-8dfc-75490609d581 | -13.3734 | -54.3779 | 2026-08-21 05:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| e41fb322-c817-3248-a6a1-1f4f43176a3e | -3.5406 | -48.1889 | 2026-08-21 05:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| f0054aa0-4d1a-3faf-bd16-b6a930193c41 | -13.3923 | -54.3965 | 2026-08-21 05:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 59d813a0-b57e-3372-92d4-23442c2c6349 | -9.4069 | -60.4362 | 2026-08-21 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 460110b8-0dbb-3618-a4d4-3c18e2dca9be | -9.4257 | -60.416 | 2026-08-21 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 500e789d-00eb-30c9-b7b0-4d79350bbaa6 | -19.7238 | -57.966 | 2026-08-21 05:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.7 |
| be980f89-452a-3877-a36f-ed88d58e1522 | -9.4071 | -60.417 | 2026-08-21 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 342.8 |
| 8fb8385b-1606-3a59-8b0a-de689e93dd9b | -6.2341 | -55.6109 | 2026-08-21 05:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| ca7ba001-00d6-32c6-a99a-1ab56c18783c | -11.1747 | -54.0216 | 2026-08-21 05:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 2926b21b-03ee-33cf-8d83-86e247beb0e3 | -6.8755 | -59.4364 | 2026-08-21 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 3b14d50d-8ef4-3928-84d6-8f3c7b5580e9 | -13.3926 | -54.3758 | 2026-08-21 05:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 175.6 |
| c863b347-ccbe-35fd-91cc-fa1278a7ccef | -7.3603 | -45.8136 | 2026-08-21 05:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| d59cbc09-d6d9-3bce-97c0-2b1870ff7401 | -7.3791 | -45.8119 | 2026-08-21 05:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 78144201-4682-328a-aabf-68afad8b418e | -3.29738 | -61.32211 | 2026-08-21 05:40:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e8434a2-0236-3cf9-93ab-fea8d85d29db | -3.84247 | -59.37662 | 2026-08-21 05:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 32d1ccdc-7da1-32a1-8f34-1ff76084f134 | -3.93091 | -59.33194 | 2026-08-21 05:40:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03255572-2cad-3ec1-8bd1-f6d2429c6f0e | -3.10187 | -61.20599 | 2026-08-21 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ffb5c8ea-e2c3-343b-b79b-5131c1f58c97 | -3.09903 | -61.20177 | 2026-08-21 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 403f4ead-8bbd-3aed-83a5-0530c118ac09 | -4.45242 | -55.39063 | 2026-08-21 05:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eefbec78-b04b-3978-b90b-438340540d33 | -4.34766 | -59.543 | 2026-08-21 05:40:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd31dada-c899-35f5-b6d8-5eb83b2f3cae | -4.04745 | -50.29897 | 2026-08-21 05:40:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11a888b8-6022-3286-ab36-eed80a8f6a07 | -3.38048 | -59.53073 | 2026-08-21 05:40:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edfdef9c-293c-3092-b8a2-559f8b55568d | -4.46653 | -55.39837 | 2026-08-21 05:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d2f86f1-b710-375a-bbef-888e747b2529 | -3.09786 | -61.20918 | 2026-08-21 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54c28657-d4a2-3210-bf49-1e2029893f97 | -4.53606 | -55.62318 | 2026-08-21 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad33fa1b-9571-3063-a7f0-aa09d09f5bb4 | -2.85728 | -60.86177 | 2026-08-21 05:40:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4077288-2008-3313-a511-344d3058d6dd | -3.9347 | -59.3325 | 2026-08-21 05:40:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5ddfcb9-4321-3216-b493-8c444930023c | -4.92122 | -56.26316 | 2026-08-21 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61d83c0f-22c3-3ad3-81c5-c764b7880469 | -4.95646 | -56.26492 | 2026-08-21 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84b0e7f8-9014-3708-991b-fbf07473c7f8 | -3.84311 | -59.3749 | 2026-08-21 05:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bfc10320-81c6-363d-9913-a87da0156612 | -1.41835 | -55.72241 | 2026-08-21 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 325acfd8-7b11-3a89-b6dd-fe8eca970665 | -4.44745 | -55.38988 | 2026-08-21 05:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36b44d60-f319-3e03-948b-1011566d349a | 0.3043 | -60.44395 | 2026-08-21 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0646d2ce-1c1d-39d7-be09-c330a4992466 | -4.44595 | -55.3935 | 2026-08-21 05:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 815d38ec-4dd4-3e15-82a5-a4216ea3e1ce | -4.1581 | -60.72888 | 2026-08-21 05:40:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff13c3b0-b5e5-35c2-a004-9fa7c200fb5a | -4.10977 | -56.36333 | 2026-08-21 05:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92c15370-fd13-3c8d-bdcd-cfb7eadb0f9b | -3.38279 | -59.52874 | 2026-08-21 05:40:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 15960a02-15a2-373b-b6e5-2a8983df22d2 | -4.95573 | -56.27001 | 2026-08-21 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fba84d33-8c4d-3bea-b884-e998fb552179 | -4.93767 | -55.78324 | 2026-08-21 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4d61a81e-8ee6-30e6-8f76-093fb4f13678 | -4.44683 | -55.38774 | 2026-08-21 05:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce2a8d51-9f88-3f8b-9556-0bd5eeece20f | -4.9165 | -56.26244 | 2026-08-21 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0f9059b8-3d5c-374b-929c-2388cec450af | -3.09844 | -61.20547 | 2026-08-21 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4686fc4-d3b8-30f0-8f2b-f59386e8db9c | 1.67897 | -60.13609 | 2026-08-21 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65682908-a9ed-3356-b017-096969712bc6 | -4.95492 | -56.26333 | 2026-08-21 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac8b8243-4dcc-36aa-9202-04bcee53848e | -2.32281 | -60.06441 | 2026-08-21 05:40:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ac3c2252-02be-3096-a92a-ac5e7acffdcf | 0.30772 | -60.44342 | 2026-08-21 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 60466033-ca01-3f03-9db3-90e5b40fc400 | -3.12755 | -60.70228 | 2026-08-21 05:40:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README74.md)
