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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fced8f36-3680-3636-93ab-ae5db80b6ce8 | -7.7223 | -55.686901 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9384ca67-e755-3489-8109-0e3ed8eb07ad | -7.7239 | -55.6945 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d20d772a-26ee-32ab-a0f4-4dd56f96714d | -7.7256 | -55.702099 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0193bcaf-ec2e-3b43-8784-474d2426c43f | -7.7273 | -55.709702 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f9afb16-3680-3888-a926-06c8d5c009ed | -7.7289 | -55.7174 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0d35927-9586-366c-ac0e-d14d7d18c17c | -7.5947 | -55.153801 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6589ed4-bfee-343c-b93a-db459024d8e5 | -7.5963 | -55.160999 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8699b43e-4d9f-33cc-805d-156cfcb2ab98 | -7.5979 | -55.168301 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 498a4d98-a4ac-39ac-893c-8a88c9917d42 | -7.5995 | -55.175598 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f18c0c92-ed1d-3fb8-bb81-d25d8b67b67a | -7.6011 | -55.182899 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c0f32b1-ce71-3521-88e3-e123fd7d3fe2 | -7.7141 | -55.696602 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 257a69d4-ec5a-3e07-b079-78bb72633dd4 | -7.7191 | -55.719501 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c168cad-769c-34e6-8d36-7e9746231828 | -7.7208 | -55.7271 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f927a718-af9a-31a1-9696-fce6fdfc4322 | -7.7225 | -55.734699 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaf59929-df1f-3a83-b650-078559f03f25 | -7.5817 | -55.141399 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00751aef-52c1-33b4-9ebb-cadb267f86dc | -7.5833 | -55.148701 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bba4b41-fe94-37dc-a188-eea418e3f550 | -7.5881 | -55.170502 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f208eb6-c37b-3782-8627-23d9845d20c9 | -7.5897 | -55.177799 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0f5c94b-8566-303b-9250-62592f4825e8 | -7.5913 | -55.185101 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9dccc41-d548-330a-8a1e-c845fc0fccc1 | -7.6107 | -55.272999 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2afd46e-0d41-30fa-a4fe-415fd10944e7 | -7.6123 | -55.2803 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddf7af66-609a-3991-afe7-4397212f6d64 | -7.5574 | -55.078201 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60e56f54-ef56-3d34-b6fc-25879f292a55 | -7.5719 | -55.143501 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aee1fd53-be80-31a5-b74e-05b2b0bd1fd6 | -7.5735 | -55.150799 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d152b12-fbd0-3026-bbc7-fc69d7bb668d | -7.5751 | -55.1581 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9b3b18c-496d-3e49-bea6-a565b8cac2a8 | -7.6155 | -55.3414 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40c82689-3913-34bf-89e8-d6695ee224ba | -7.6171 | -55.348801 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51ef6772-82cd-368f-817b-d4e6b5bbcbfb | -7.554 | -55.109299 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11bcf81d-bce0-3f92-bdf0-9a3e82d53e20 | -7.5556 | -55.1166 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3c817a2-67df-317a-9f8a-48517386f315 | -7.5604 | -55.138401 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f045ba2-052f-3ae0-9829-a961b490ac0d | -7.5621 | -55.145699 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68f4cffd-c9d7-3d9b-bbd7-27ac5a17cec3 | -7.5637 | -55.153 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c838421-2ea0-3f2a-bb53-6ed6df9336ad | -7.5653 | -55.160301 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d8c70e5-2cbd-349e-90fc-1978d7e69fa9 | -7.5669 | -55.1675 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f999cc1f-af82-30a3-88f2-46159a55a91c | -7.6057 | -55.343498 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09577fa3-aa71-356b-9d4b-bce3770d2da5 | -7.6073 | -55.350899 | 2024-09-26 00:56:56 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b1077e7-6d14-3b6c-af29-4c9feccba624 | -7.5474 | -55.125999 | 2024-09-26 00:56:57 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cce06d2-12cf-3aa9-b33b-3a0d322b2851 | -7.549 | -55.133301 | 2024-09-26 00:56:57 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cac15854-643b-3b26-bcd5-9354b40b2c08 | -7.5506 | -55.140499 | 2024-09-26 00:56:57 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be33e797-c194-3db7-a0b0-b34399ce8b06 | -7.5523 | -55.1478 | 2024-09-26 00:56:57 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3707759-923b-38fa-8158-68520f8d228b | -7.5344 | -55.113701 | 2024-09-26 00:56:57 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcdfef63-8ff1-3ce7-ab02-7422d75b74ae | -7.536 | -55.120899 | 2024-09-26 00:56:57 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cdbdbd3-efac-3006-87ac-03126b8224e7 | -20.399 | -41.886 | 2024-09-26 00:56:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.3 |
| fee4eef4-90a8-3879-a027-111529c66dc2 | -20.3999 | -41.8602 | 2024-09-26 00:56:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.4 |
| 5d791a47-0df3-35c1-914f-946e13f85017 | -20.4197 | -41.8798 | 2024-09-26 00:56:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 127.1 |
| 5286ac53-1472-3e52-bea3-18f48c5b6fd4 | -20.4206 | -41.8541 | 2024-09-26 00:56:58 | GOES-16 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.4 |
| b3fac325-63ab-3e25-8275-c0bcb644b063 | -20.4404 | -41.8737 | 2024-09-26 00:56:58 | GOES-16 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.2 |
| 8fd01424-c187-3e61-9d83-20f1eee0a7f5 | -8.0929 | -58.016602 | 2024-09-26 00:56:58 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b28c7c8d-17cd-3265-8bae-c0ada27b03f0 | -5.0876 | -45.1982 | 2024-09-26 00:56:59 | METOP-B | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d6096479-79c6-324c-b652-28a6f648be25 | -7.3875 | -55.100399 | 2024-09-26 00:56:59 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12106b4b-8933-300f-9342-abec19215a59 | -7.3891 | -55.107601 | 2024-09-26 00:56:59 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0509a48-236b-3eee-ab7a-21ccc06b69ef | -7.3777 | -55.1026 | 2024-09-26 00:56:59 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5ff4652-7602-359a-9bcf-64b13759a4f0 | -20.5881 | -51.4802 | 2024-09-26 00:57:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.1 |
| 23170e8e-42d9-3b69-9989-4881a92a5a2f | -20.608 | -51.4986 | 2024-09-26 00:57:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 167.1 |
| 5e9ed7c7-f65f-39da-8053-e958c5efe854 | -20.6086 | -51.4762 | 2024-09-26 00:57:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 154.8 |
| d7eb4997-06a0-3771-a91e-f94f0a8957c7 | -7.3152 | -54.9128 | 2024-09-26 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7bea47c-6f5c-33ca-bc12-81397d9aadbd | -7.3038 | -54.907799 | 2024-09-26 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcf679de-5cee-3244-82e4-fc9f0548dd11 | -7.3785 | -55.478699 | 2024-09-26 00:57:01 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 419bbea9-024e-3b73-9482-9387181d11ea | -7.3801 | -55.486198 | 2024-09-26 00:57:01 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8ff5724-e90c-303f-bb8b-33c0619c6044 | -7.3817 | -55.493599 | 2024-09-26 00:57:01 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ef4928a-9d18-313a-92dd-1d4f3d4241ba | -7.3834 | -55.500999 | 2024-09-26 00:57:01 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a0f95bf-50ab-3b6f-85ae-43f25be535f3 | -7.3687 | -55.4809 | 2024-09-26 00:57:01 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfd2259d-aeac-3841-9b5c-200727202a5d | -7.3703 | -55.4883 | 2024-09-26 00:57:01 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| decc03bd-ef14-3cdd-ac61-49fec89d2c14 | -7.3719 | -55.4958 | 2024-09-26 00:57:01 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b07b588-d962-3c89-8fbf-c681bda9ec04 | -7.3736 | -55.503201 | 2024-09-26 00:57:01 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6935901f-e70d-3646-b6cd-0b5c15d93bd1 | -7.3752 | -55.5107 | 2024-09-26 00:57:01 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95458589-b3c3-339e-9546-b2dc6ba73e0e | -7.3589 | -55.483002 | 2024-09-26 00:57:01 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48069c53-35bb-3d35-968f-3fcb6032f17d | -7.3605 | -55.490501 | 2024-09-26 00:57:01 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad15361f-fa82-3e48-8121-44a5a1bf1dfb | -7.3621 | -55.497898 | 2024-09-26 00:57:01 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dea49c58-a8a2-348a-ac02-6f3d30832552 | -7.3638 | -55.505299 | 2024-09-26 00:57:01 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea504598-7e42-30d4-9d44-e43d1b1f0978 | -7.3654 | -55.512798 | 2024-09-26 00:57:01 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b47ec89-6eb2-3214-987b-a65f6aeb8c0d | -7.1725 | -55.011799 | 2024-09-26 00:57:02 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f15e647-743d-387d-b27b-267695c40638 | -7.1741 | -55.019001 | 2024-09-26 00:57:02 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7821646-f540-390a-b365-9c789afca24f | -7.1757 | -55.026199 | 2024-09-26 00:57:02 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e678b65-00d7-3aff-8e85-ec07a8e16970 | -21.9166 | -48.5738 | 2024-09-26 00:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 0cfc1307-e2d1-3135-96eb-76635966fc51 | -21.9173 | -48.5504 | 2024-09-26 00:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 62.8 |
| e74ad696-6464-329b-8c72-a10fa5882e68 | -21.9374 | -48.5688 | 2024-09-26 00:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 44c640ee-1f68-3edc-be57-6b586c772c51 | -21.9381 | -48.5453 | 2024-09-26 00:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 9176d935-1d6e-35e9-a95d-2d3a1c0d2f11 | -5.2228 | -47.951 | 2024-09-26 00:57:08 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c7ad1de1-e013-31c6-8fdc-7fa040ecbd49 | -5.2257 | -47.9632 | 2024-09-26 00:57:08 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fe54f99b-4178-3653-894f-a1a031c472a8 | -5.2131 | -47.9533 | 2024-09-26 00:57:08 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e4d17425-bd51-3a05-a4a7-93c76d06fb96 | -5.216 | -47.9655 | 2024-09-26 00:57:08 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 23aa8a65-e0f7-3f48-8ef1-bb0da88c100f | -8.2135 | -61.4631 | 2024-09-26 00:57:08 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 078f1b53-f3b5-309c-a7be-fed83be9972d | -8.2171 | -61.480202 | 2024-09-26 00:57:08 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2496677-799f-3444-96a4-2a08eac70039 | -8.1633 | -61.367199 | 2024-09-26 00:57:08 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 15b57834-7f5a-3d7a-b873-5bd1482ab37a | -8.1668 | -61.384102 | 2024-09-26 00:57:08 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 29a04767-e854-3067-bc0c-255ea15b5eaa | -8.1536 | -61.369202 | 2024-09-26 00:57:08 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a4dbe3f1-9a26-3d70-82ba-2e2041ebb708 | -4.5766 | -45.671501 | 2024-09-26 00:57:09 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5250405c-e41c-352c-bd36-0c05669dd731 | -4.5809 | -45.6894 | 2024-09-26 00:57:09 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 959e94d3-f27c-34e2-a7ce-1bb65709d1f1 | -5.2828 | -48.817001 | 2024-09-26 00:57:10 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a49512c0-fa08-3870-bffa-b639b1bf573f | -5.2853 | -48.827702 | 2024-09-26 00:57:10 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37c1abcd-37dd-376e-a1c1-e2adf7b80e51 | -4.497 | -45.895199 | 2024-09-26 00:57:11 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bc55862b-b30e-3b34-a7a1-622ad66f07b6 | -5.9531 | -52.1115 | 2024-09-26 00:57:11 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 139d9264-ffb3-3856-a8e0-bf5a3cb3a236 | -5.9548 | -52.118698 | 2024-09-26 00:57:11 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8faae496-fd56-39ef-9e04-df11c0ab6bcf | -4.4873 | -45.897499 | 2024-09-26 00:57:12 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| add40b07-0032-3a13-b119-9cd5621f69b2 | -5.9417 | -52.1064 | 2024-09-26 00:57:12 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a79969da-713d-3e37-9ce5-f35b867c2ef8 | -5.9433 | -52.113701 | 2024-09-26 00:57:12 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6d7a1d8-ef14-353b-b85d-2c462d4e10fc | -5.945 | -52.120899 | 2024-09-26 00:57:12 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4279ae0-a380-3ca6-9957-06372378a727 | -5.2461 | -49.231602 | 2024-09-26 00:57:12 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e27dd147-6f67-3a77-97d2-83efdf408f4d | -7.3939 | -59.776699 | 2024-09-26 00:57:15 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README29.md)
