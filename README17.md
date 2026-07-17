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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97481aa5-5121-3345-9ed6-b7596d881e51 | -13.2456 | -45.0909 | 2026-07-17 07:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 5943be80-892c-3544-8cad-6f4c2758d2cd | -13.2451 | -45.1142 | 2026-07-17 07:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| fb9f16a7-471c-32d7-9547-8038322e91d5 | -13.2649 | -45.0877 | 2026-07-17 07:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 006a7974-ae0a-39ea-9d6b-76cb3ad890aa | -13.2456 | -45.0909 | 2026-07-17 07:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 35e59b45-6d81-3b3c-a81c-f507560b3803 | -13.2645 | -45.111 | 2026-07-17 07:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| c97262c4-fba2-3318-a7f4-89312c5cbe75 | -13.2649 | -45.0877 | 2026-07-17 07:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 465e3530-9708-3fb6-92d9-44f35dfef933 | -13.2451 | -45.1142 | 2026-07-17 07:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 1125cfc3-35ae-3148-a172-ba028cc7f1e0 | -13.2456 | -45.0909 | 2026-07-17 07:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| c4622ed8-381c-3247-8b6f-03e8b8d4c738 | -13.2645 | -45.111 | 2026-07-17 07:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| bee675bf-1ad8-3a8e-9c81-ecee111be9fe | -9.45819 | -64.03785 | 2026-07-17 07:48:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 7452d23f-caa2-3592-be36-207e57c9960e | -13.2451 | -45.1142 | 2026-07-17 07:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 1b7c10e3-bc5f-393d-9c4e-2a827d3e69a6 | -13.2649 | -45.0877 | 2026-07-17 07:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 4463716e-91cc-3fde-9394-4071eb5ea1bc | -13.2645 | -45.111 | 2026-07-17 07:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 0c3775b0-6610-3f03-8ac4-5a00e87fc778 | -13.2456 | -45.0909 | 2026-07-17 07:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 82f2076e-87c3-31e0-9eba-32c4526fd30e | -13.2649 | -45.0877 | 2026-07-17 08:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 60be48bb-4df4-3896-a917-b62cbb772b03 | -13.2456 | -45.0909 | 2026-07-17 08:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| a4ccdc48-cc06-3d99-88c1-e5942b85f8fb | -13.2645 | -45.111 | 2026-07-17 08:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| e0424eeb-7154-3a1f-a134-21462de86df3 | -13.2451 | -45.1142 | 2026-07-17 08:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 9f28e105-23de-376b-96be-f0fe7b544d7b | -13.2456 | -45.0909 | 2026-07-17 08:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| e43a181d-b0ed-3b5b-ae20-04686c9221c1 | -13.2451 | -45.1142 | 2026-07-17 08:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| c9fa2c46-b81a-32e0-acff-c128825c45ab | -13.2649 | -45.0877 | 2026-07-17 08:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 43714fef-c8f2-32a8-8003-7bd2a6b78c02 | -13.2645 | -45.111 | 2026-07-17 08:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| b7b13216-1277-37f6-865f-a6f2302c2a29 | -13.2649 | -45.0877 | 2026-07-17 08:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 9eb8df1c-ab6d-3a1b-b88a-3e332592a160 | -13.2456 | -45.0909 | 2026-07-17 08:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| ceef9f05-11aa-391a-89bb-2257b0205e80 | -13.2451 | -45.1142 | 2026-07-17 08:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| f5463c6a-4937-3901-866c-b87b9af94ec8 | -13.2649 | -45.0877 | 2026-07-17 08:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 0438ffd2-65cf-353c-920e-277efa8ebde9 | -13.2645 | -45.111 | 2026-07-17 08:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 5ed8e87d-82b9-3b13-843b-262d291eb41f | -13.2456 | -45.0909 | 2026-07-17 08:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 3da92a13-8242-36df-9753-d571728294aa | -13.2451 | -45.1142 | 2026-07-17 08:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 2d69974f-a941-3a35-8bb6-fba477718597 | -13.2456 | -45.0909 | 2026-07-17 08:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| d206a114-62b0-3686-9261-6d20044d43b9 | -19.8239 | -57.9735 | 2026-07-17 09:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.3 |
| bcf7d106-78db-3f7d-8aa4-902729e4ceae | -19.8436 | -57.9917 | 2026-07-17 09:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 6d0b4102-7335-39a0-8255-cccd698065a0 | -19.844 | -57.9709 | 2026-07-17 09:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 277eff26-5655-38af-bee5-dac218d888dc | -19.8239 | -57.9735 | 2026-07-17 09:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 7c7fbfcb-3c1e-3615-8de5-75855c8f0aad | -19.8436 | -57.9917 | 2026-07-17 10:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.7 |
| 32b06122-7029-3078-9f45-ae410b81a1f4 | -10.8632 | -46.5138 | 2026-07-17 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 006c0f89-def0-366d-bac7-2af6edac4423 | -10.8632 | -46.5138 | 2026-07-17 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 96b6c98b-4baf-364e-b6ec-f2973426eb67 | -10.8435 | -46.5613 | 2026-07-17 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 9d088a37-22a8-3543-9f02-53dfab512ced | -2.77757 | -49.45311 | 2026-07-17 12:21:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d7cb1891-7bfe-3d23-ada5-7e08396a6352 | -2.77556 | -49.46797 | 2026-07-17 12:21:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 3dd43cf4-49c8-3f36-8cdd-a262bd6596b6 | -7.91807 | -48.24567 | 2026-07-17 12:21:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 37.8 |
| c6e0f5c1-fe69-345f-a0a2-05e4a5aa8d8a | -2.77617 | -49.46236 | 2026-07-17 12:21:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 98d08a46-8740-3dc6-b0cf-8dc5637aab87 | -11.74611 | -57.81648 | 2026-07-17 12:23:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 42446563-c8c3-3c58-93e0-38bb76ba1fd0 | -12.69434 | -46.50384 | 2026-07-17 12:23:00 | TERRA_M-T | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| f9186014-b0ed-3611-9ca9-643168db8946 | -9.50822 | -47.14832 | 2026-07-17 12:23:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| c3fc9646-1bf8-3676-a2ac-1331f2dcdcc4 | -10.86686 | -46.51598 | 2026-07-17 12:23:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 159.3 |
| cfc5d5c6-93f4-3316-8b20-88b8a9adab8b | -10.82697 | -47.39219 | 2026-07-17 12:23:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| ceb6d4b2-edde-36c6-bba8-a132f17bf0b4 | -9.52691 | -47.12064 | 2026-07-17 12:23:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| dc640667-5b54-38e7-a41c-e466ccffdb53 | -12.41601 | -58.39891 | 2026-07-17 12:23:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d080d73c-0e9a-35d6-b8f1-b8af6590bb1c | -10.8118 | -47.39019 | 2026-07-17 12:23:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 18f61ac5-4035-3194-8a26-937c0cb1db40 | -12.69955 | -46.51115 | 2026-07-17 12:23:00 | TERRA_M-T | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 611780b4-c11a-32bd-a8fd-28d4313d818a | -12.49915 | -48.26556 | 2026-07-17 12:23:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| f4f17c4d-bd00-3920-b6c3-733cf2020a69 | -10.84675 | -46.54885 | 2026-07-17 12:23:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 219.8 |
| d1e1d24e-a4f3-3151-ac37-302e3028844d | -10.86301 | -46.55024 | 2026-07-17 12:23:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| a91d8eae-5a78-3d46-bbf8-41dd7a5be1bc | -10.85057 | -46.51451 | 2026-07-17 12:23:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 41e17e12-53e2-3764-9547-416daa40f592 | -11.94747 | -55.53036 | 2026-07-17 12:23:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c5d9fb84-8734-3b69-bc63-cc4bb84f6233 | -10.82937 | -47.38589 | 2026-07-17 12:23:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| a4a5ca9f-78c6-3332-89c6-0008a6ddc042 | -9.90627 | -53.36016 | 2026-07-17 12:23:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c5ef5612-2f12-37f5-8031-69833f67a11d | -11.94875 | -55.52131 | 2026-07-17 12:23:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 846c4958-5ce9-3bb6-b633-283ce41020cf | -9.90767 | -53.34978 | 2026-07-17 12:23:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| acdce671-3e40-3a48-9219-4d587856b2e1 | -12.50081 | -48.27254 | 2026-07-17 12:23:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 6dc5bc24-0861-3554-894b-e73214232ba4 | -10.84362 | -47.26711 | 2026-07-17 12:23:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 83d03fbd-1075-39ea-8672-428f92a26cd9 | -18.55967 | -56.82408 | 2026-07-17 12:25:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| a76b6677-646e-3eb3-afdb-876e19b885d3 | -18.56098 | -56.81466 | 2026-07-17 12:25:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.7 |
| e8e84b90-9593-3fa5-8c41-7f7fe1d1a027 | -16.50457 | -52.82493 | 2026-07-17 12:25:00 | TERRA_M-T | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b14e4fd1-f9e5-3a57-b5cf-c1ff0bf0149a | -19.82477 | -57.97832 | 2026-07-17 12:27:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| c6904cde-57c7-3e1c-a44f-7a86a3202f30 | -19.86122 | -57.99001 | 2026-07-17 12:27:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| dbf6e7ce-1cb0-3796-8e1a-a15d66d2c8ac | -19.84356 | -57.98726 | 2026-07-17 12:27:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.6 |
| 4eb2fe12-359d-3359-91dc-682a5abc726d | -19.83607 | -57.97656 | 2026-07-17 12:27:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| bd797d81-5ca2-3d84-8e71-2ba3537f7b3d | -19.8301 | -57.94104 | 2026-07-17 12:27:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 6a0109e3-6003-3b25-9c02-9fa970eed872 | -19.83143 | -57.93172 | 2026-07-17 12:27:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 2d82831b-a992-3715-adc4-ee8bb6a28af2 | -19.85239 | -57.98864 | 2026-07-17 12:27:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.6 |
| 60159009-baf3-3bcb-97a1-c2b5d4a133cb | -19.8414 | -57.93927 | 2026-07-17 12:27:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 014212ac-56e2-328e-adad-03d68fedf01b | -19.83474 | -57.98588 | 2026-07-17 12:27:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 4757e02d-39a3-3574-84dd-e75ce366cdac | -21.76789 | -56.2977 | 2026-07-17 12:27:00 | TERRA_M-T | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 15.2 |
| d72f849e-62a2-3832-842f-6ca8021d8f78 | -29.36303 | -53.77719 | 2026-07-17 12:29:00 | TERRA_M-T | SÃO MARTINHO DA SERRA | RIO GRANDE DO SUL | Brasil | 4319125 | 43 | 33 | nan | nan | nan | Pampa | 15.1 |
| b9d7c1ef-cd05-362f-b3fc-008a6a015277 | -10.8632 | -46.5138 | 2026-07-17 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 191.3 |
| dd0a4978-d5c6-331f-a228-076f086dd0a9 | -10.8636 | -46.4913 | 2026-07-17 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 94f8c770-9e66-3db8-a042-5d734637af9a | -10.8435 | -46.5613 | 2026-07-17 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 3be0c52e-4c8e-3fe8-a159-8cbd87be67f8 | -10.8632 | -46.5138 | 2026-07-17 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 296.8 |
| 93d894fa-e365-3d0f-854e-af5a2bd57952 | -10.8632 | -46.5138 | 2026-07-17 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 24c0ff40-d34d-30e5-89ae-fa8df77bbd06 | -10.8632 | -46.5138 | 2026-07-17 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 093b60a1-8bd4-3509-b8d7-70d7786a1fa8 | -10.8435 | -46.5613 | 2026-07-17 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 7805d5f7-8ce8-3930-bb80-6a61fe0f7016 | -9.902 | -53.3736 | 2026-07-17 13:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 5c667179-d0e0-387b-92f6-e17b2a25cb88 | -10.8632 | -46.5138 | 2026-07-17 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 669fd723-9c91-3bc1-b84a-78df46058e8f | -10.8632 | -46.5138 | 2026-07-17 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 140.1 |
| e6174cc4-c79f-32e9-a258-6dadddf87c3f | -10.8435 | -46.5613 | 2026-07-17 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| d5ff6222-e011-30d3-9d9b-a533a2d8f305 | -18.5675 | -56.8109 | 2026-07-17 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 91ce2885-ace9-3e21-86e9-19cdefc9dbbc | -18.5476 | -56.8135 | 2026-07-17 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.1 |
| 68800cb1-8d73-387e-992a-4ab3c2fc0234 | -2.8814 | -42.214 | 2026-07-17 13:40:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 3228ff33-f228-3442-b947-a41376a49810 | -18.5675 | -56.8109 | 2026-07-17 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.4 |
| 1fb98062-26f7-3c41-b95d-b80db65fcdd6 | -10.8625 | -46.5589 | 2026-07-17 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 6058078a-58b5-3df7-94b4-a7ce5a7c3b80 | -18.5476 | -56.8135 | 2026-07-17 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.0 |
| 680c436a-d7ca-30ad-b14c-69c7dc8c983e | -10.8438 | -46.5388 | 2026-07-17 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| b6358457-07e0-361a-bf6b-3fee96350ad4 | -18.5675 | -56.8109 | 2026-07-17 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 61aa5678-3f54-3504-85fc-b6009055ddd3 | -9.5085 | -47.143 | 2026-07-17 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| d346d4dc-1c3a-3797-af88-5dfd54bb809a | -9.5085 | -47.143 | 2026-07-17 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 9a1c29ef-9c03-3460-b0d2-fec6f1b5f9f4 | -18.5476 | -56.8135 | 2026-07-17 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.6 |
| 2ca9353d-d5f7-39ba-a00a-27f29e253351 | -18.5675 | -56.8109 | 2026-07-17 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 17c60822-2a70-3cf2-9fb0-a701d7cf4823 | -10.8435 | -46.5613 | 2026-07-17 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |


[Clique aqui para ver as próximas entradas](README18.md)
