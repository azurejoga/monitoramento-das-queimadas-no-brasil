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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0383bee5-e661-30a0-b290-ea0549c86606 | -5.30589 | -60.20242 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee18dbc0-2a70-3274-b05f-e5ffb018049d | -6.76875 | -59.65825 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9d60884-850d-376e-905a-f9476d7abd9c | -6.82225 | -58.96474 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e9e77907-4bf6-39f7-a911-77947ec05dc5 | -6.2459 | -60.00112 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50750d40-f0c3-3ada-82cf-f5a912aff194 | -6.78624 | -59.64621 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e21a84d4-d00e-397d-8472-85772e3e2267 | -8.13856 | -62.86161 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78b074a0-82d3-3bf5-9485-2ae4552ddb4f | -7.37642 | -64.35957 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fb1d342d-7dc2-3add-bbef-65ea34ef8cc6 | -6.71268 | -58.57273 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93b9b68f-5719-3472-b8d0-314666e79761 | -5.52979 | -60.20667 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9cb846a0-d8de-3774-a725-077f4633412a | -8.10574 | -62.88274 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e88a433-78de-3384-be64-a33b7907e757 | -7.39182 | -64.34781 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15ff54c6-dd97-338d-954f-2aee75cc3202 | -6.78589 | -59.67551 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3bb5332c-2d9b-3b2c-80fa-8b649c90389f | -6.25796 | -60.00522 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65dad88d-acf0-313f-a551-172fba90767c | -6.68872 | -58.85537 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2df64c63-89eb-3f70-9200-9cef9c4ea46b | -8.10182 | -62.88582 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f626819-708e-3467-9bd0-54cd7c9663b2 | -7.53642 | -50.54512 | 2025-08-26 05:36:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d1118fd-2f90-37fb-ac69-92c70bfab501 | -7.54612 | -63.84058 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88b0ca98-ed25-36bd-86d7-80f772c79ccd | -8.11993 | -61.46407 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0dd26ee-90e5-3c3b-a7ae-6dddb4cdc4b2 | -7.49828 | -63.81847 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b500b6db-c7bd-3cf2-9d51-7cfcaab4e139 | -7.55004 | -63.85895 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 263dd23b-61a3-3345-aa92-dffaace7a1b2 | -8.24028 | -61.45705 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4310f4fe-b1f8-3dc5-8c14-991e0d946b5b | -8.08056 | -61.53327 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95da9f1d-909c-3053-aeeb-efc408ec2cf7 | -7.48046 | -61.36103 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b2f24469-ca7a-360b-8d50-1317b6d3caae | -7.37697 | -64.35611 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9a240f7a-e24b-385b-8c89-c09a8aa445c9 | -7.38304 | -64.36062 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b6c890f-d606-3f22-8ff7-64098d978612 | -6.87702 | -59.89948 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cdd5a110-76c9-31f2-8115-5e7234f625d7 | -4.95774 | -55.81276 | 2025-08-26 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ddd3cb93-f924-3bcd-a739-fd46e57a1ce3 | -7.53267 | -63.37821 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa366d85-cc1a-3abe-97b0-9cf13ec89216 | -5.45029 | -60.18789 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22599b27-9c35-3345-b3d4-3b2c0c964c32 | -5.43325 | -60.17648 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1f754d7e-1210-3732-b0b2-cbc87974508a | -6.6333 | -58.54922 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 202eb7c9-3d52-3c6e-8b07-a0ee4b963283 | -7.39843 | -64.34885 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 689d8b02-afa0-3aba-96ff-5cd0d9b05572 | -8.07522 | -61.54475 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d551f9a1-e709-3498-9c13-7b36cb3fbe11 | -5.43391 | -60.17215 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46cf6a81-72e0-39c8-8ba8-1615ccf9ea80 | -6.76665 | -59.67275 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 88b9eee5-da22-3cd7-a234-a4711f8adb80 | -6.30801 | -59.87289 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40659b03-a2ab-3b31-a269-aa0b6ab8d907 | -6.2408 | -60.00954 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e9f4bd68-41e8-3a06-ac52-1c18573ec375 | -7.40781 | -64.35387 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d00aa09-1833-3a2a-a050-78855d8050a7 | -8.53665 | -55.26462 | 2025-08-26 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe2e7c9c-626d-383f-a059-314cb1a5d056 | -5.31321 | -60.20351 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae4f482c-3429-3014-ad59-b97ede81614b | -7.47928 | -61.36901 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7f2813ff-792d-3908-ad1b-0a9a6b9be247 | -5.31816 | -60.1955 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0c6f545-1094-3761-89b2-b0a8354ff7a0 | -7.53941 | -61.37817 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52e0b4f7-d53d-37bd-b48d-34a8e72d949b | -7.47339 | -61.33533 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2c4f5dbd-9781-3914-a2fd-4802bedab451 | -7.65297 | -61.46429 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d6c1034-a196-3dd0-9dd7-e3f11b4b8a14 | -7.61962 | -61.04031 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d2f71c9-26a0-3fb3-8010-9d184492a951 | -3.39527 | -59.45163 | 2025-08-26 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd0a95c9-b844-3b28-992d-f69ba0f990f1 | -6.62918 | -58.54858 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 491bd153-e3f4-33d4-8861-316338334b20 | -6.31314 | -59.86427 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b84f420c-93d1-3d74-bf1e-6f3277bdb03e | -6.79043 | -59.67131 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f3a6d3c-c1fe-3f40-aaac-47fde8534b20 | -5.52612 | -60.20611 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6e2c2ad0-4cf3-3ff2-ab49-eb1771e50f6b | -3.97703 | -51.06153 | 2025-08-26 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 07b7b8d9-5189-3659-9e54-925b2195356b | -7.38634 | -64.36114 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 567f21cb-5d5c-3b28-869e-e35cea3bc85b | -7.40505 | -64.34988 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee81ac28-86f4-35ed-ab82-3f6155a0c295 | -6.91907 | -59.36787 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e80dea19-0988-37ea-a013-37283819757a | -6.77049 | -59.67334 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| b06ae03a-f7d0-3e33-b12a-8839e3a42ef9 | -6.71215 | -58.57639 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39b49338-4385-3f97-abad-657b0734811b | -7.10117 | -59.22039 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 651b9329-737c-348b-bae6-b69db373c3ad | -6.62865 | -58.55228 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eec13ca2-6ee5-318a-8655-8da65395cf26 | -6.93413 | -62.98279 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 830364fc-07c8-341d-8028-587b8f942d49 | -7.47398 | -61.33131 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d9dd4378-2fe1-3f2f-9c4c-fe4dbc52b55b | -6.79498 | -59.66711 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33d3f457-004c-34cb-97f9-e6141daaeb9b | -7.3819 | -64.34625 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 615c6df1-eabd-37f0-a523-095be571a233 | -6.25357 | -60.00916 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fda7a6c-d5c1-3ba8-b45f-7b68355c7034 | -6.78659 | -59.67073 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a047599-992f-3182-bae7-e0d9f1c679d7 | -5.40455 | -60.16766 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40da81ce-5380-39bb-97c8-39ceaba2bcfe | -5.31515 | -60.19065 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f47b02b8-b1c8-38df-91be-a32566249638 | -7.53223 | -50.53936 | 2025-08-26 05:36:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 73f0cb4b-8fac-3eff-9dae-71ddab5cc5e9 | -7.56212 | -63.84663 | 2025-08-26 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f80b5382-728b-305f-b434-774b77251407 | -6.65565 | -58.79521 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbd8e855-8a88-3712-89fe-9c299e858dfe | -5.31084 | -60.19439 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb982c9d-dc68-3802-8162-befdfde77188 | -8.22729 | -61.42185 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17afc7e2-0fcb-3e55-81da-2d3642031859 | -8.12572 | -62.87808 | 2025-08-26 05:36:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d65dc9c0-aec1-38c8-9f1f-c1a8b8fcb72a | -5.44819 | -60.15223 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb3986b6-b053-3bb4-afd6-a69b745f7065 | -6.76735 | -59.66792 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e0a5882a-dccf-3c74-b625-75f1f66e45b5 | -6.69829 | -58.55548 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 58d77c54-a735-3e74-8e5e-1674bf4caaad | -6.76079 | -62.87313 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77340621-9d4d-3fe1-9c7e-65018d819485 | -7.64945 | -61.46375 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63334a00-b375-339c-9452-9575ca668b96 | -7.43938 | -60.6223 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e3d9faef-83a3-3288-acac-af2e5749fa33 | -8.12171 | -61.45198 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3717935-dfcd-3527-9d70-dcb36281c651 | -3.98359 | -51.06227 | 2025-08-26 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 81a23255-f416-3030-b81a-5c56f8bf5566 | -6.65345 | -53.18363 | 2025-08-26 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d549c9d-b198-3357-ae6b-79bdaf2dbd36 | -7.29297 | -59.66833 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c82af376-0128-3ac3-a868-30ae7a1e487a | -6.81875 | -58.96059 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8b4d050d-db3c-3855-9396-49b309549b8c | -6.25441 | -60.02074 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30790b20-cbde-3861-9b91-bb43ef91e5b7 | -6.26394 | -60.0084 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 722c8f9b-2d92-3cb4-b9da-31d88cdecfa0 | -7.54356 | -63.04082 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73d64d67-4ae2-37cf-9d46-0dfcfb3788ed | -5.43627 | -60.18135 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b8abc8c-0bb2-3186-9e8a-ee8a1d666d28 | -6.70856 | -58.57213 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 383e3f71-a62e-3eb1-87f9-ac31d95cc336 | -7.54174 | -61.38672 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d55980f2-d89c-387d-87f6-0ec0f2b15804 | -7.62258 | -61.04501 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 094ae7b5-0363-384e-bba2-8961d7d6bcfd | -5.44753 | -60.15655 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3382daee-9e8c-32f5-affd-8f0a1ecf9f0b | -6.7096 | -58.56479 | 2025-08-26 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09fba431-a450-3fd3-8370-b52eea83736e | -7.47929 | -61.3445 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 99e4dbab-b535-3f2d-8884-2aea551cd8f6 | -7.89814 | -63.5213 | 2025-08-26 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7a26ace-2a59-34be-9a0b-ad72c1f65ac5 | -8.25034 | -61.46264 | 2025-08-26 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d50615ee-4b92-3ce0-947c-75f0b388e1a0 | -6.83619 | -59.35825 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c12378c-aef1-38f8-8ee1-ce958c7b8fe8 | -7.35253 | -59.667 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6e821a55-b7e7-3566-bdbc-3ba23ee0426f | -6.7733 | -59.65402 | 2025-08-26 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dc3c12b-25a3-3b50-9aaf-869e451ea87d | -6.24013 | -60.01402 | 2025-08-26 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |


[Clique aqui para ver as próximas entradas](README78.md)
