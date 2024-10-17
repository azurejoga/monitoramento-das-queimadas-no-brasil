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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac0af044-8fc6-3aab-84c1-e22ccbad7728 | -10.19529 | -52.32062 | 2024-10-17 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7983e185-3d1c-39e2-b317-480b594f2243 | -10.19461 | -52.32546 | 2024-10-17 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c69297a1-d322-3fe3-aad5-cfad14907ca8 | -10.19392 | -52.33029 | 2024-10-17 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7d629b56-be07-3cc5-b15f-1dae2e1ea7a3 | -12.4305 | -53.16137 | 2024-10-17 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf61b879-6648-3c73-9f90-f6b02ced9186 | -12.42915 | -53.17068 | 2024-10-17 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 700a1489-7827-3ab7-9952-94e2bda695c9 | -12.42569 | -53.17294 | 2024-10-17 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 044ee302-92a9-34ec-ac68-813b9299d8fc | -12.42472 | -53.17475 | 2024-10-17 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60eb6e29-fe9e-3d49-80bc-cd187d3816d5 | -12.42129 | -53.17701 | 2024-10-17 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 205d5518-7173-342f-b025-346439b2fd77 | -12.41753 | -53.17644 | 2024-10-17 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a346b57-c288-3e22-ad85-5068c9f0756e | -12.3807 | -53.10629 | 2024-10-17 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eeec6565-0f51-3c6b-af25-cf8fdc3cb42c | -12.37627 | -53.11039 | 2024-10-17 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 446018f3-6264-3d5c-b5bd-5280fd3c67b9 | -12.37052 | -53.12381 | 2024-10-17 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36023bc0-cdc8-3127-bf68-e61a18962565 | -12.36986 | -53.12847 | 2024-10-17 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 948c9ee3-ad2b-3e52-b27e-b7173207a0b2 | -12.36855 | -53.13778 | 2024-10-17 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e196fa87-2f30-3126-8a91-6d43cfc27adb | -12.36789 | -53.14241 | 2024-10-17 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59fd5fea-cb57-3cd2-8448-6b315fd238a0 | -12.36544 | -53.13256 | 2024-10-17 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a19f1a9-6607-3baf-9bd0-666b3c3c33f9 | -12.36478 | -53.13721 | 2024-10-17 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02664762-c769-37af-9f03-7dec4054308b | -12.36413 | -53.14185 | 2024-10-17 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 077ee0ab-aa34-3805-b8aa-03711f378a6a | -7.45095 | -55.12727 | 2024-10-17 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e911a38-9440-3f17-951e-51184c1b404e | -7.44763 | -55.12675 | 2024-10-17 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d9e3f28-b75a-337c-8c74-08addba6ccb3 | -7.30708 | -55.30897 | 2024-10-17 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83a42371-bd14-3d52-9229-758e7ae47365 | -7.06083 | -55.42665 | 2024-10-17 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d85d0c8-69ef-3cc6-93c2-077de48a9383 | -9.61599 | -55.81606 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1221e312-2cc8-3920-913d-8fbee65372af | -9.61545 | -55.81957 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14df4785-74d9-3e22-bd6d-265c9721207c | -9.61268 | -55.81554 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| aa4ff61f-cb7a-3fcc-8630-e2134dcbeb6a | -9.60219 | -55.8175 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 543b102e-89b5-30c7-a9b4-f47ac95d82c0 | -9.60164 | -55.821 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d684f36-275f-3265-8dd8-d43bedcba401 | -9.59887 | -55.81699 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 158da08a-b171-3a30-be9b-7233e7d92d88 | -9.59833 | -55.82048 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad81ec61-b14e-3c35-9749-a915ebf465fe | -9.59556 | -55.81647 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8141e8cc-5a6b-3fea-b7ad-c718e969a6fb | -9.57839 | -55.79579 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fee6e563-5376-3bd1-8056-477b896d2364 | -9.57784 | -55.7993 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e2685e6-f43b-34f6-b76a-37bdb58d8f20 | -9.57676 | -55.80631 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2997bac-3f3e-3524-af75-031ab74c5ae7 | -9.57507 | -55.79528 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05f604e6-96ab-36b6-a82c-83d9b6c58d8c | -9.57453 | -55.79878 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67e5dd95-03e6-3eb8-a158-a08477878dd3 | -9.57344 | -55.80579 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8f5ab24-51a4-38ac-ad9d-157c54953051 | -9.57175 | -55.79476 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c79c77fc-4599-348d-803f-70bb39536b29 | -9.57121 | -55.79826 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd86db31-1ff1-3a79-ae8a-8ce5c1a20057 | -9.57067 | -55.80177 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be2e9e4b-1d79-3816-b4d9-f162eabbdb5a | -9.57013 | -55.80527 | 2024-10-17 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae3288c2-59c2-339d-9d63-e6bed1a993a5 | -9.34635 | -57.57165 | 2024-10-17 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 486692e6-626b-3834-ab88-2ee731d81cf4 | -9.92279 | -57.52008 | 2024-10-17 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6e1acbf0-dac8-32b2-9574-05fe5c680627 | -9.91946 | -57.51955 | 2024-10-17 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c98ce1a0-5b4b-3854-8516-8ec4882d7a6a | -9.8561 | -57.74665 | 2024-10-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 213b6c33-de6f-396f-a138-495b60be4785 | -9.83672 | -57.71783 | 2024-10-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6341abf-c7e4-32b6-8f37-e9b58ed6fdde | -10.31114 | -56.81051 | 2024-10-17 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2c043d5-7b9c-36c4-a34d-ca3f568f42fe | -10.12958 | -56.77381 | 2024-10-17 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4f45a260-d347-32c2-9008-f5e7d83d10df | -10.12628 | -56.77329 | 2024-10-17 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c7c0ed7e-ba7f-3e1b-9ff0-d78c1fba7e67 | -10.12353 | -56.76928 | 2024-10-17 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eaf9d71e-5102-38fe-8cac-b5fb0dad2438 | -10.12298 | -56.77276 | 2024-10-17 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1244fe5-cfd8-3aeb-9196-b00b5a1026f8 | -6.63413 | -58.72807 | 2024-10-17 05:06:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 258e0903-7236-390a-84e4-753c03067583 | -6.6319 | -58.71939 | 2024-10-17 05:06:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 388b6e1f-0ea1-3b5f-9cf9-023025ba7c3a | -7.34331 | -59.78894 | 2024-10-17 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d86a1605-4163-338b-ab8a-5ae295002ddd | -7.34258 | -59.7934 | 2024-10-17 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c78a07bd-daf1-331b-9be7-850fc531edac | -7.33961 | -59.78815 | 2024-10-17 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8292eabb-969c-3827-949b-5c3772b6dc7c | -7.33888 | -59.79263 | 2024-10-17 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffb859c7-16be-32d3-a0d7-ec1b4b61e466 | -7.0712 | -59.52578 | 2024-10-17 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8167250d-b71b-30ae-9b4c-b67faa96aace | -7.01328 | -59.35199 | 2024-10-17 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0786eea-44a6-30a3-a211-0ccdc48638c3 | -7.00963 | -59.35139 | 2024-10-17 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 384e4562-0505-39b2-b296-198a0078cc36 | -7.00598 | -59.3508 | 2024-10-17 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6b21d58-848f-3216-917b-a73f46a062fa | -6.99141 | -59.32361 | 2024-10-17 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a3486cb-2e97-3b57-96e5-66f6bb53edc4 | -9.16212 | -61.90198 | 2024-10-17 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f1dfbc1-b679-3085-b9bb-6aeebc86dcb5 | -9.16148 | -61.90574 | 2024-10-17 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3852482f-5a42-3cad-83a5-75ee74610852 | -9.16083 | -61.90954 | 2024-10-17 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a391e06f-c2d5-3c03-8b77-e5b27ad78910 | -9.15799 | -61.90127 | 2024-10-17 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 91f26f72-2108-3067-8fe9-f67f2bf333ba | -9.15735 | -61.90502 | 2024-10-17 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 15.2 |
| f725a862-293d-3c72-9667-5375689be9a4 | -9.1567 | -61.90882 | 2024-10-17 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 1f87f24b-42c8-3cf5-a2c8-bb12625b0d8b | -8.8238 | -62.35131 | 2024-10-17 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 629fe657-ead7-360a-bca9-b8d80392fa0f | -11.66227 | -64.83714 | 2024-10-17 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e439d38d-1597-31b7-b015-230f749a5d84 | -11.65266 | -64.8353 | 2024-10-17 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7dc008b2-76ac-3d37-b909-7e8507d2c128 | -11.64785 | -64.8344 | 2024-10-17 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ffd2683d-a954-3d44-9604-bb5ac1e7a5bc | -11.50342 | -65.21847 | 2024-10-17 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e96a4685-8ef5-3400-9a35-f848e9085ccb | -11.49079 | -65.12153 | 2024-10-17 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dff8d7d2-3781-36ac-841e-b823f37d158c | -11.48588 | -65.1206 | 2024-10-17 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dedcce35-e587-3483-8a63-c127b7b869f0 | -9.39814 | -68.98726 | 2024-10-17 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be6be559-8104-3a1d-b4c2-efbbac07ddf5 | -9.39805 | -68.98579 | 2024-10-17 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 234dfa91-8c9e-32d6-985f-12fd4de55e8e | -9.39164 | -68.98603 | 2024-10-17 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9872f3a4-8b20-30f2-ac4f-0bdab59a0a38 | -9.39154 | -68.98458 | 2024-10-17 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c865a9bb-d356-3aab-af87-11b2250b3800 | -10.86298 | -69.39567 | 2024-10-17 05:06:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4b5ff56d-c32e-34bd-8dd8-a8979615fecc | -10.84572 | -69.48056 | 2024-10-17 05:06:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8c65c91e-7cb8-3e52-b7f2-8e08bde4e8fa | -10.12019 | -69.17361 | 2024-10-17 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3408b4a5-e13d-361b-ade2-5e21be960d62 | -10.11367 | -69.17249 | 2024-10-17 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2021bdaa-8f7b-37fb-a968-5c51dbeff1ae | -20.59062 | -47.55311 | 2024-10-17 05:08:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5ebbd66-e77d-3644-b169-3b41faf3896e | -20.58891 | -47.54974 | 2024-10-17 05:08:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0958776d-72dc-32ff-8782-3d41e6c448e7 | -20.47388 | -47.51843 | 2024-10-17 05:08:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f190d298-037e-3241-ac54-ec8358bdadda | -21.8173 | -48.41837 | 2024-10-17 05:08:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 4b81f849-ad88-3317-98f8-3f8bc49871c1 | -21.81691 | -48.42275 | 2024-10-17 05:08:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 19.7 |
| cb63a32c-28ac-3800-8fec-636f6c719155 | -21.8111 | -48.42229 | 2024-10-17 05:08:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 84d341a8-c136-3f08-9509-3e706c2c7c71 | -17.63171 | -56.23152 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d3df003b-b9b0-3464-8b14-51417da64a92 | -21.49442 | -51.48668 | 2024-10-17 05:08:00 | NOAA-21 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0f415b82-8504-3d07-979c-5bfb489da49c | -16.62305 | -51.49635 | 2024-10-17 05:08:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07245f9d-6582-3b5c-b8f6-3dc7b3894c7b | -20.1959 | -52.13944 | 2024-10-17 05:08:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfbee833-7a52-310f-b820-88193ad3869a | -20.19198 | -52.13433 | 2024-10-17 05:08:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d294f8a-18d4-3e69-83fd-79f81c1278d3 | -20.19143 | -52.13896 | 2024-10-17 05:08:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dedd68e-16cf-36ea-82ab-3829b3cbef16 | -20.99635 | -51.79461 | 2024-10-17 05:08:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3ef9687a-33dc-3e4b-90fe-734af5e6b572 | -16.55002 | -52.47194 | 2024-10-17 05:08:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f1dac36-5d9f-3e49-8363-ef3f4da10235 | -18.93941 | -54.53687 | 2024-10-17 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 18b19277-47bd-3d5d-86f0-2275048f34b5 | -16.00635 | -54.15747 | 2024-10-17 05:08:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76b01573-5cf7-361e-a4aa-059059331b0f | -19.01098 | -54.83003 | 2024-10-17 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7475a291-fb8e-3471-8dac-ca7b23d2c2cc | -18.94319 | -54.53736 | 2024-10-17 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README46.md)
