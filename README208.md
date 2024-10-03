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

## Dados Diários - Página 208

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff69ddf1-9f18-3f4e-a524-cc00c4cb24ed | -12.4038 | -63.0009 | 2024-10-03 10:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 119.4 |
| dfdf0468-b7a7-3a28-9418-0c880d48bed6 | -12.8996 | -62.4913 | 2024-10-03 10:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 146.2 |
| b663708f-ddd5-33e8-835b-dfa0454574c9 | -12.8998 | -62.472 | 2024-10-03 10:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 192.6 |
| 510c960c-d567-3d37-abb0-aae1962b6f31 | -12.8999 | -62.4527 | 2024-10-03 10:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 567f35a2-76ae-3d56-9e1c-0b68037a6b46 | -12.9186 | -62.4901 | 2024-10-03 10:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 27073f65-a822-36fd-9bbc-baa13a2280ea | -12.9187 | -62.4708 | 2024-10-03 10:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 140.1 |
| ffb29385-0680-3f21-aa9e-16574925fdd5 | -16.6297 | -57.3785 | 2024-10-03 10:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 454.5 |
| be12add0-146e-3adc-ac81-0f56bec6931b | -16.63 | -57.358 | 2024-10-03 10:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 537.6 |
| 5a9c4f1d-3c64-33d1-9701-9e838bbeb446 | -16.6492 | -57.3763 | 2024-10-03 10:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 270.6 |
| 1ae3d54c-9a5f-3133-a05e-0b4cc309f16f | -16.6496 | -57.3558 | 2024-10-03 10:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 280.5 |
| cabd0da9-0331-30fd-960b-e1ac277a4d3e | -16.6698 | -57.3126 | 2024-10-03 10:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 240.7 |
| 748d7d7e-1887-3be3-83ed-0d8ec5f5acce | -16.7455 | -57.4674 | 2024-10-03 10:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 182.2 |
| d7222644-9e9f-30d7-b2a3-de22a6473b26 | -16.7474 | -57.3446 | 2024-10-03 10:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.7 |
| d3430771-0683-3ccf-9d4c-0c4fa7dea3db | -16.7477 | -57.3241 | 2024-10-03 10:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 217.5 |
| 7f687ad5-998f-365d-9076-a89a9e9a044d | -16.765 | -57.4652 | 2024-10-03 10:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.5 |
| a9e848a4-903b-35bd-b89b-f46423c9cd9a | -16.7673 | -57.3219 | 2024-10-03 10:06:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| 052372c1-1bdf-3064-a5ae-f43be5ceb212 | -17.1577 | -57.3787 | 2024-10-03 10:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 131.5 |
| 181ded48-30d8-3cf2-b3d3-dbe44318525d | -17.1774 | -57.3764 | 2024-10-03 10:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 241.9 |
| e39590e4-0462-32bb-a770-dc43ac9b698c | -12.4228 | -62.9807 | 2024-10-03 10:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 214.9 |
| bf9a1f23-6408-301a-8844-2ef0f18349ca | -12.4227 | -62.9999 | 2024-10-03 10:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 470.0 |
| 13775e4e-de12-3725-ae48-740c253fc3ca | -12.4038 | -63.0009 | 2024-10-03 10:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 106.6 |
| af1886ef-4992-33cf-b20d-bc3f057e4e8a | -12.9187 | -62.4708 | 2024-10-03 10:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 156.5 |
| b120f020-4908-3a7a-abe8-e9d8926a629f | -12.9186 | -62.4901 | 2024-10-03 10:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 95d5ed0b-e979-3f01-be08-e899c7facefb | -12.8999 | -62.4527 | 2024-10-03 10:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 129.7 |
| ed666c3a-8d75-350f-bd38-ea8eafe36171 | -12.8998 | -62.472 | 2024-10-03 10:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 168.5 |
| 818decb2-364d-376f-90c5-033b628ab3a0 | -12.8996 | -62.4913 | 2024-10-03 10:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 129.0 |
| b03ff7f2-c4a6-3621-9d12-60361fc9867a | -16.6893 | -57.3104 | 2024-10-03 10:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 318.8 |
| 7c7b896f-d5ea-3b53-b270-3b420e364a97 | -16.689 | -57.3309 | 2024-10-03 10:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 147.0 |
| 34ba678b-5ebf-39a0-852b-812055494692 | -16.6701 | -57.2922 | 2024-10-03 10:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.5 |
| dbf0e8b5-da23-373d-944a-68fce4b55eb6 | -16.6698 | -57.3126 | 2024-10-03 10:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 696.8 |
| 8d02dc90-795e-3b8e-b86d-63edb785890f | -16.6694 | -57.3331 | 2024-10-03 10:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 261.3 |
| 4ff16225-f894-335f-81dd-d6f2ba69456e | -16.6502 | -57.3149 | 2024-10-03 10:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.3 |
| 18624fa1-177d-3430-ba63-5a155e273eb9 | -16.6496 | -57.3558 | 2024-10-03 10:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 268.6 |
| 4234575d-3d13-3c98-b0ee-1abe47994e54 | -16.7477 | -57.3241 | 2024-10-03 10:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.9 |
| 0079e0a0-21a9-3b37-9587-cbc63a98724f | -16.6492 | -57.3763 | 2024-10-03 10:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 341.4 |
| c928ba28-c659-3dee-9a6c-2fed6e91bffb | -16.63 | -57.358 | 2024-10-03 10:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 448.5 |
| 45f7c4ec-1fbf-3803-8328-b67c0978dbb8 | -16.6297 | -57.3785 | 2024-10-03 10:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 411.8 |
| aeb2e530-debb-339d-8f6c-3470fd6f736d | -16.7455 | -57.4674 | 2024-10-03 10:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 183.7 |
| d66e1eff-d098-3c12-b910-dfc9547bdb26 | -16.765 | -57.4652 | 2024-10-03 10:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 81b6e407-c039-3415-bcce-68d7621afb5d | -18.6098 | -43.9156 | 2024-10-03 10:16:49 | GOES-16 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 5f71e93a-aaeb-3747-a718-b7e38e60d18e | -11.2563 | -46.9348 | 2024-10-03 10:26:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 04f64b4e-bd1f-37ab-832b-0986e1d1d755 | -12.4416 | -62.9988 | 2024-10-03 10:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 7a7cea4c-b443-38f4-84b7-0b73cfca2668 | -12.4228 | -62.9807 | 2024-10-03 10:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 021f5da9-a3b5-38dc-bc8d-6772ec04cec7 | -12.4227 | -62.9999 | 2024-10-03 10:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 262.2 |
| 8d094bd7-770d-33f1-8818-8b74b537f785 | -12.4038 | -63.0009 | 2024-10-03 10:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 123.8 |
| a942c4d9-841b-3fee-9988-dc604712f351 | -12.9187 | -62.4708 | 2024-10-03 10:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 124.4 |
| cd241f82-b7ee-36d8-b3c6-6fe95001db51 | -12.9186 | -62.4901 | 2024-10-03 10:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 558a1418-0575-3b57-8c00-102af25d695c | -12.8999 | -62.4527 | 2024-10-03 10:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 165.8 |
| 1dde2a4f-d7a7-3435-ad04-cef26e1dba8a | -12.8998 | -62.472 | 2024-10-03 10:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 239.9 |
| adc1d1b5-47af-3a53-a380-51257419e877 | -12.8996 | -62.4913 | 2024-10-03 10:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 178.8 |
| 1bb83371-ec8c-33d1-aee4-79b06b06edb7 | -16.6893 | -57.3104 | 2024-10-03 10:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 274.4 |
| 5d5efb40-f28e-31df-a71d-4bfd6198c137 | -16.689 | -57.3309 | 2024-10-03 10:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.2 |
| 91985ecb-fb2f-3a8a-a520-9b3042e6f048 | -16.6701 | -57.2922 | 2024-10-03 10:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.4 |
| 794ce4e2-ce96-3b8f-9ab0-d6d486a2e948 | -16.6698 | -57.3126 | 2024-10-03 10:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 532.5 |
| 903d7dfb-f954-3339-9f1e-2803de37f730 | -16.6694 | -57.3331 | 2024-10-03 10:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 190.8 |
| 4ff03eb6-7916-30b2-bb6c-4337717e800f | -16.6502 | -57.3149 | 2024-10-03 10:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.6 |
| f7bd689a-81f0-3d33-aaed-e3be59ad88e9 | -16.6496 | -57.3558 | 2024-10-03 10:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 202.4 |
| 9f309772-8fef-315f-9c7f-d583c4bed2a6 | -16.6492 | -57.3763 | 2024-10-03 10:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 208.2 |
| c3f39c0f-c0cb-3249-bb46-e5a4bdfdeec0 | -16.63 | -57.358 | 2024-10-03 10:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 170.5 |
| 0324bc8f-8b92-3f2f-8d2e-285c65facf84 | -16.6297 | -57.3785 | 2024-10-03 10:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 154.9 |
| a74b1495-1226-3064-800d-ed583a3b9ef6 | -16.7477 | -57.3241 | 2024-10-03 10:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 187.1 |
| 95e8bfa5-ece8-3d4f-9e40-6d764a5f9cf8 | -16.7474 | -57.3446 | 2024-10-03 10:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.3 |
| e4024dd5-568b-39b6-a1ce-15d5028611a8 | -16.7455 | -57.4674 | 2024-10-03 10:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 167.1 |
| 079cc98c-6a80-3f2b-bc3b-0b558b6279a2 | -16.7673 | -57.3219 | 2024-10-03 10:26:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 140.0 |
| f1a666c7-8621-3935-91ae-2a8a16c24a86 | -16.765 | -57.4652 | 2024-10-03 10:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.1 |
| 0e775500-c41f-3f5f-9fe1-c4910a5863f1 | -17.1574 | -57.3993 | 2024-10-03 10:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 142.7 |
| fdcefc11-184c-31fb-8cde-1e85285fcebb | -11.2567 | -46.9123 | 2024-10-03 10:36:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 2b45cc9e-4e63-3317-8103-1401876dfcbf | -11.2563 | -46.9348 | 2024-10-03 10:36:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 84317736-bbd1-3e0e-9f48-ae00968055f0 | -11.2758 | -46.9098 | 2024-10-03 10:36:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 2d44bfeb-50ee-3e5f-b8ad-9e1e2a66ed9a | -12.4228 | -62.9807 | 2024-10-03 10:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 117.7 |
| d908d2d6-27e8-3977-b880-10acb18c9f85 | -12.4416 | -62.9988 | 2024-10-03 10:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 8e71fc2b-b18d-391e-8de4-14378ffb075c | -12.4227 | -62.9999 | 2024-10-03 10:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 246.9 |
| 3ca642b9-f823-34bc-bcd7-c1496dd0fb86 | -12.4038 | -63.0009 | 2024-10-03 10:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 3f6f15bc-8d2c-3e3e-b229-f517a7d3cec5 | -12.8999 | -62.4527 | 2024-10-03 10:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 195.3 |
| 02418286-2179-331e-ac85-56a975d783eb | -12.9187 | -62.4708 | 2024-10-03 10:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 9cca62d2-7c50-3563-9e9d-31faaa67abd3 | -12.881 | -62.4538 | 2024-10-03 10:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 09817eeb-58db-3bd7-9ff5-7d6a5cfdaf3c | -12.8998 | -62.472 | 2024-10-03 10:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 267.8 |
| 31ae59a9-d9da-3d76-b6c6-0e8de2d3e70f | -12.8996 | -62.4913 | 2024-10-03 10:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 183.7 |
| dc97866d-a5d5-3873-9d3d-72be7ebdf94d | -16.6896 | -57.2899 | 2024-10-03 10:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.3 |
| 1c2527c8-1b0e-38e9-bee9-33493937dc82 | -16.6893 | -57.3104 | 2024-10-03 10:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 265.2 |
| 3cddd4e3-3181-37bf-bc90-aed830f000dc | -16.6701 | -57.2922 | 2024-10-03 10:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 254.3 |
| 7df2699c-9dbe-3ae0-a6bf-0d4ad80a8ad3 | -16.6698 | -57.3126 | 2024-10-03 10:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 683.5 |
| 513e68e5-92bf-3550-9b3b-b9fbab2b2f15 | -16.6694 | -57.3331 | 2024-10-03 10:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 191.5 |
| 301a7733-330d-3af9-a9a7-85b6b681d7c5 | -16.6502 | -57.3149 | 2024-10-03 10:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 207.9 |
| 31ec23ff-7147-3e37-a212-3523f593bfa5 | -16.6496 | -57.3558 | 2024-10-03 10:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.8 |
| 1db65818-d667-36b4-b77b-785d97a380ab | -16.6492 | -57.3763 | 2024-10-03 10:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 180.4 |
| 093c0c1c-2eea-37ba-a886-6be3ab404a27 | -16.63 | -57.358 | 2024-10-03 10:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.6 |
| 626acbae-d90e-3265-81cb-ec6398e8d69a | -16.6297 | -57.3785 | 2024-10-03 10:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.7 |
| 771c0a3b-5e43-37c4-83dc-00c6793ee556 | -16.7455 | -57.4674 | 2024-10-03 10:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 146.6 |
| 26425e1b-baf3-3b43-9c21-7a027b8a7591 | -17.1771 | -57.3969 | 2024-10-03 10:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 195.1 |
| 644cefa4-5330-3090-8863-35e3793adeab | -17.1577 | -57.3787 | 2024-10-03 10:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 193.3 |
| 625d0da5-1943-322a-a6fa-a0563a86cc0e | -17.1574 | -57.3993 | 2024-10-03 10:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 170.7 |
| c6f636db-0b15-3d84-a8c7-c2135e8c23c0 | -10.9571 | -46.5918 | 2024-10-03 10:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 224dcfa0-f79d-3ab3-a1b3-fc9bfce47918 | -11.2563 | -46.9348 | 2024-10-03 10:46:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 279.7 |
| ada6463f-e587-34e3-a765-f1feaeafee02 | -11.2567 | -46.9123 | 2024-10-03 10:46:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 01091a1f-b2f5-3987-8b3e-1feb2cdb9f5e | -11.2754 | -46.9323 | 2024-10-03 10:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 237.1 |
| edef4162-2eaf-3598-bb29-a3d789dc9023 | -11.2758 | -46.9098 | 2024-10-03 10:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 154.4 |
| bb6fec31-a66f-3cf5-8bb9-af5734e8e259 | -12.4038 | -63.0009 | 2024-10-03 10:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 101.7 |
| e489c3d0-88f5-3b7e-b6d5-fd7ba88c8ef4 | -12.4227 | -62.9999 | 2024-10-03 10:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 336.3 |
| 01315db6-b6e4-3e82-a833-a62d6c1bc7b6 | -12.4228 | -62.9807 | 2024-10-03 10:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 159.8 |


[Clique aqui para ver as próximas entradas](README209.md)
