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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 501d44ba-8c0a-3efd-84e6-3395becc3caa | -12.1115 | -54.58143 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21a7e82c-5728-3ce5-aede-d020eedf637b | -11.88336 | -58.73306 | 2025-06-28 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56bc91ee-5662-3404-ad17-09a9caa3b874 | -13.95011 | -54.49269 | 2025-06-28 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67ab60ee-e35e-3e03-8942-b95a3db3a95b | -11.0353 | -55.3759 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0dd0e064-ed43-335a-9d6b-5686db0fc57c | -9.11456 | -49.47684 | 2025-06-28 04:51:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 835d7d68-9a5e-3bfd-97c4-36f89cbe5efe | -11.05681 | -55.37193 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec5289bb-9b46-3cd8-af03-c4b65f8699f5 | -10.84277 | -53.75513 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4190010-42d9-368f-95c5-ac58ce7bf81d | -15.15558 | -55.35077 | 2025-06-28 04:51:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c5e2f4e-2bbb-3e8f-b582-54b304ca3c51 | -11.05621 | -55.37561 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a86d60f-a47e-3aa4-a890-a6df99e98308 | -14.88996 | -48.3969 | 2025-06-28 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7162d39c-5945-3d88-8fba-05720a3a8b10 | -9.11829 | -49.47744 | 2025-06-28 04:51:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 54a2edcd-d1ec-3922-a1d4-0c546fe35a44 | -13.64 | -47.68288 | 2025-06-28 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45a145b8-7bc6-3b33-8e0e-eb06afcae481 | -14.53525 | -53.83383 | 2025-06-28 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00d56dc4-5463-3f1f-aea4-63ed3efc3265 | -12.02482 | -47.77496 | 2025-06-28 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 424c0f70-a365-3f5d-bf0c-ef5b4481c3c8 | -9.7096 | -56.18909 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4b63e0a9-d50c-345e-a579-336e633683f2 | -13.94349 | -54.49159 | 2025-06-28 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0dd1d3e3-de4c-3c44-98d5-3c819b23a98f | -10.52707 | -53.62521 | 2025-06-28 04:51:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6613ad6f-b0c1-3cd5-af99-48b5d4b5ad3a | -11.06019 | -55.37248 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01bc816c-ac3d-3d72-90a5-79879dbb6e21 | -9.68932 | -48.32973 | 2025-06-28 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1b43cb8-ec52-38ab-9c3f-a60a078895d5 | -13.93962 | -54.49459 | 2025-06-28 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1325ab13-bc2a-333e-9d36-ceb04265398d | -11.04327 | -55.36965 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 81769fed-bf0a-36af-a510-6e7dc0b6e860 | -10.28743 | -57.00216 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee070eb7-12ba-332a-bf8b-dd3639ebd51c | -10.29035 | -57.00713 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89356df7-8eed-3fc7-abb9-94a03e08a293 | -9.70385 | -56.17988 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55ce1190-c5ea-3bd3-a147-583dbdf94c01 | -9.79344 | -48.5581 | 2025-06-28 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c4c40b4-2b5c-3f4d-b418-ec45975deb9d | -10.83781 | -53.76508 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a638020-4be9-39b4-818c-5a7089a9bbd3 | -13.14369 | -56.804 | 2025-06-28 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f492903d-a4cc-36fe-886c-ad7b2f138024 | -14.47666 | -51.06803 | 2025-06-28 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78d67161-84be-364e-b29c-ebed3c46f20b | -10.03486 | -54.32897 | 2025-06-28 04:51:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12dbe7ee-6123-34d3-b99e-bbdbce8f3338 | -9.71026 | -56.18506 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b143dc65-eb53-34d4-b079-6319de036cbb | -11.87941 | -58.73242 | 2025-06-28 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc81c6ca-f3b8-3711-a62d-d076dd0b5c82 | -10.29107 | -57.00282 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98a5f627-1450-34d8-9f9b-5bc652ba98b1 | -10.16032 | -53.92408 | 2025-06-28 04:51:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 310dd1be-8d60-3acc-b9d4-c467a880db7c | -10.87672 | -56.45424 | 2025-06-28 04:51:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1437273c-1474-36e7-84e9-1a13442eff9e | -12.02106 | -47.77009 | 2025-06-28 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1454520a-2ba0-34b9-bd1e-bd7d242d619a | -9.43582 | -63.45701 | 2025-06-28 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d56db5d9-7af5-3013-a56c-5acd45c3b2cc | -15.56805 | -47.85417 | 2025-06-28 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 023ae0c1-9250-34c2-9ae4-51c602ed9938 | -9.0893 | -47.96484 | 2025-06-28 04:51:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91663158-89e0-3b2e-b9e3-61b5c1501c32 | -11.0596 | -55.37616 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb595557-104b-3ce0-bab1-5cc20c2871dc | -11.04267 | -55.37333 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| ef55160d-396d-37f1-b8d4-dbe78672a9d5 | -11.13713 | -53.91391 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f4baa1a-b410-30d8-b76c-ffb43a677fbc | -11.56715 | -54.52087 | 2025-06-28 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6766f908-6137-3f06-a768-8656a67926a9 | -9.91786 | -59.90753 | 2025-06-28 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83405415-3ab8-3fca-bb74-a18f36baf1f1 | -14.83366 | -59.801 | 2025-06-28 04:51:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8cc229d-a724-39ed-82fd-b244e13f00a0 | -10.87473 | -53.76746 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a70198a-c48a-3317-9d37-5e6f0dcfe13d | -11.80702 | -56.96093 | 2025-06-28 04:51:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e309940-af8f-36bc-a944-14d72456ec92 | -14.53857 | -53.83438 | 2025-06-28 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13f2a46f-0717-36ee-bed6-3d8225901470 | -12.26102 | -46.76145 | 2025-06-28 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e40d1e88-9e18-3e19-ad35-137782923957 | -10.96 | -48.15409 | 2025-06-28 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 63afd3ae-9373-3c9a-9690-61ff2e4a4a94 | -10.36832 | -52.28426 | 2025-06-28 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9270c14-10ba-37db-ac2b-a7b956fdf1ce | -9.70319 | -56.1839 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4121b4a7-c761-3639-a86d-8fc44ccc0ab9 | -9.11083 | -49.47626 | 2025-06-28 04:51:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2bc6bb01-a1f4-3887-8107-12678da981db | -11.05283 | -55.37504 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 13d5484a-b08d-31d5-beb1-5ae6eded6e77 | -11.04207 | -55.377 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 49fc7495-bdb0-3364-83ed-c06a9a1e76ae | -10.82624 | -53.75246 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db21fcc2-54a9-38f2-9251-58df4eb21edc | -11.82672 | -57.77262 | 2025-06-28 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f581ca94-dc21-34c8-9277-97f4c7fabe8d | -11.91848 | -54.81229 | 2025-06-28 04:51:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fada15a5-2bfb-3ec2-bf2d-dcd1a618bce2 | -9.35319 | -58.83747 | 2025-06-28 04:51:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8387ca24-640e-30fb-80d5-c561a6d54b4b | -10.30068 | -57.12467 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fe81ee9-97b6-35ec-9510-ec5b95ab4814 | -10.95189 | -54.37312 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b02fbade-ac39-3a82-a8af-d9350157d007 | -9.87443 | -48.05183 | 2025-06-28 04:51:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f37ef57-4d78-399b-8999-d7c86150d632 | -13.94191 | -43.24181 | 2025-06-28 04:51:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2e315256-67ad-3f23-a310-bac46ea2a59d | -11.57047 | -54.52142 | 2025-06-28 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d67bcda8-f326-3c26-8347-66661d14cc40 | -14.21472 | -57.40413 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1446cf8a-d4a4-3c01-85b7-50304e4bf795 | -11.84295 | -43.79644 | 2025-06-28 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b50cebf1-07df-3c78-b1fe-9096749c2b96 | -10.82662 | -54.02867 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e25ab65-214d-3527-8298-f5f906eea3c4 | -11.04944 | -55.37446 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c7d46441-f73a-398c-b24c-14a0419a6311 | -9.4389 | -47.96091 | 2025-06-28 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a158d3e-63d2-37b0-af4d-71a8cec97c1f | -11.05394 | -56.74306 | 2025-06-28 04:51:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04a0c3ad-6764-3bca-80fa-122a1d48d186 | -11.56871 | -52.09732 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fa81ea3-d65b-3bf0-a79a-2bd1a3264ccf | -10.96169 | -48.15346 | 2025-06-28 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7a14242a-391b-393f-b812-1093a12fa456 | -11.27122 | -52.74802 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 72c58667-3b06-3ccb-be41-2dc63f7c579b | -13.94405 | -54.48805 | 2025-06-28 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f2ee980-3975-39f3-9880-ca016d6203cd | -9.73777 | -48.33679 | 2025-06-28 04:51:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d5edc3f-1d84-369f-bc96-f637d6485c6e | -11.56896 | -47.62491 | 2025-06-28 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 935b2487-570e-301d-9d52-9e69c4dd7715 | -8.84511 | -49.85809 | 2025-06-28 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d20b3c0b-f942-3e12-a529-be2fee62b3b2 | -13.9468 | -54.49214 | 2025-06-28 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 285db583-e396-3056-8a3b-50e35392041e | -10.30215 | -57.13844 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f742a3ca-15da-3456-a69d-e95e94ad1b1d | -8.33366 | -55.09505 | 2025-06-28 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8ebc7d0-e6e2-39ce-ba0a-98927f06e38d | -12.11312 | -54.59259 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3308fbb2-9bad-366f-8c89-d45c1ba5fa02 | -9.4311 | -63.46388 | 2025-06-28 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce137273-21f9-3c81-9056-0b047d009abc | -12.11037 | -54.5885 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce5731f7-351b-3bb7-9408-566b3bfcf063 | -11.27008 | -52.47157 | 2025-06-28 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 342e7617-4a02-35b2-8e10-192b40541e60 | -11.14043 | -53.93591 | 2025-06-28 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e43d2407-2565-313c-aa04-e435bb2715af | -14.68837 | -53.38847 | 2025-06-28 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 36930a8b-b337-3b7c-849a-f1a81d3438a3 | -9.11628 | -49.491 | 2025-06-28 04:51:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c463407d-9d2c-3ee1-80d3-99334ab05790 | -11.07784 | -55.04918 | 2025-06-28 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b8eadd5-f5ff-3210-852f-955531ee9170 | -10.28597 | -57.01079 | 2025-06-28 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3dea8ff0-2b58-3f9f-b33a-ba4e956ba817 | -12.10924 | -54.59559 | 2025-06-28 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27947db0-527b-3063-8234-96c0ae34b301 | -9.35885 | -58.85406 | 2025-06-28 04:51:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9adc58fb-df78-3beb-9c00-7c91ef462d75 | -11.77674 | -59.32115 | 2025-06-28 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e398649-3c88-31de-b157-381e0b53f5d5 | -10.03706 | -54.33659 | 2025-06-28 04:51:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e9c8df15-e403-3a79-8f38-750893416a34 | -9.97125 | -48.2447 | 2025-06-28 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cb8ae18-f58c-3eae-a14c-575d6cf1480c | -8.57646 | -51.58385 | 2025-06-28 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80849d2a-ee43-3f71-a600-2bb7bd78eb05 | -12.02539 | -47.77068 | 2025-06-28 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1038034-ab54-3e26-a718-a157cc4d09c0 | -11.57104 | -54.51788 | 2025-06-28 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b2d41a5-c95b-3460-8408-0742cfe901c9 | -14.69228 | -53.38533 | 2025-06-28 04:51:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8af9f676-6da9-35f1-9848-4d88e0fe2a1f | -9.4663 | -56.05967 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f066ea8-9a54-348f-a53f-f52283cce77e | -9.69899 | -56.18735 | 2025-06-28 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0d11b72-15ed-36cc-8098-707fb83dc7d8 | -13.94361 | -43.24411 | 2025-06-28 04:51:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README25.md)
