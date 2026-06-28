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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac76ad47-e890-3ae6-a713-0b543aea7832 | -11.95045 | -54.09369 | 2026-06-28 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2287d789-6e1d-3779-b589-eabf6febf421 | -12.1873 | -52.89603 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35ba68ba-27c6-383d-b4cf-de75d872d1ee | -12.17611 | -57.12858 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e85160c-c433-38b9-9382-003b543132a5 | -9.08899 | -59.40447 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 13ab82fd-bdf1-384a-ba73-b9762062b12b | -12.60213 | -57.88277 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f69cf584-3396-3793-947f-ef4cc60ecc74 | -11.37837 | -55.2693 | 2026-06-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec1ebf3b-51e3-34a2-aee5-b972706e47a2 | -12.18041 | -52.90815 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d8fa4896-9615-37d2-8f76-e7b8a2f85a33 | -11.94471 | -58.61476 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5123bcdf-eb54-30a8-b7ba-800050a87cef | -12.1787 | -57.15575 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a7e2efa-c921-38c8-a467-0b85956c29fc | -12.08881 | -52.00689 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6baf8f43-1fab-35ad-9847-4e400793985e | -11.2093 | -54.2848 | 2026-06-28 05:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| fe8beed2-9cdc-3761-a554-504fb303216a | -11.2279 | -54.3036 | 2026-06-28 05:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 7898a0a2-f70b-3e87-a66a-de58056d7c58 | -11.209 | -54.3053 | 2026-06-28 05:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 186.3 |
| 19d0186c-d3e5-30a6-9bbd-2d84e9312c3a | -12.1937 | -52.8866 | 2026-06-28 05:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 983ee688-e2ba-3204-b951-cef62eaf1a1d | -12.194 | -52.8657 | 2026-06-28 05:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 5077ee1e-485c-3394-aee2-02c82835dcdb | -18.47434 | -54.09764 | 2026-06-28 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0a87840a-f73b-3432-b664-b3e65d93b664 | -21.27478 | -56.03278 | 2026-06-28 05:01:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1cc1bc0-ebe2-3e96-a2da-105971a01923 | -16.19175 | -59.327 | 2026-06-28 05:01:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5542284c-2700-33f5-9e38-c37766e5dc1c | -16.19529 | -59.32766 | 2026-06-28 05:01:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7f23434-c0ac-31ca-8449-3fb69668120a | -18.48021 | -54.10711 | 2026-06-28 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f093ead5-e5fb-3e93-bd73-91bc0071dd95 | -17.70473 | -46.7741 | 2026-06-28 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f7c1b38e-8f44-3156-9755-a13ea2143dd3 | -16.23503 | -59.30915 | 2026-06-28 05:01:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1c4bf7b-caa2-3c71-9078-2b35453f56d4 | -18.48079 | -54.10298 | 2026-06-28 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c16a3e98-9d7c-356e-bded-cad9be411bf0 | -15.44031 | -59.23332 | 2026-06-28 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1abcb837-7917-3622-abcc-d15cdedc412e | -18.49591 | -51.61593 | 2026-06-28 05:01:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a3f6751-5dc1-3c30-aec1-ac6358300e38 | -20.97613 | -49.74257 | 2026-06-28 05:01:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 822ab03c-f941-3632-b97d-cd3ef54f55bf | -15.43757 | -59.23418 | 2026-06-28 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9489d0ea-7978-34b4-a3b8-157290d41e99 | -15.44388 | -59.23392 | 2026-06-28 05:01:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5c1a9d7-2127-39de-810b-3d874dc9ab3f | -18.48373 | -54.10765 | 2026-06-28 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d0f9c4de-3cb2-39ba-9747-8bf7354d4743 | -16.23149 | -59.30849 | 2026-06-28 05:01:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7beee176-e62f-3258-ab0b-af063a7b01cf | -15.37462 | -60.1602 | 2026-06-28 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 308273b1-be9d-3a4c-a564-eb646ce3ef18 | -21.27422 | -56.03661 | 2026-06-28 05:01:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19c8ddbd-4900-3926-afe0-b62ce3896d64 | -18.48431 | -54.10354 | 2026-06-28 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c4af03b1-fb4b-3d80-a185-8960335f37a2 | -20.10026 | -57.23269 | 2026-06-28 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c27360ac-54fa-321d-a92c-0e75e9deb058 | -18.47376 | -54.10182 | 2026-06-28 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 44f2d502-5b27-3f83-b46f-e98aa60da140 | -18.76896 | -57.36948 | 2026-06-28 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2019a3b5-d676-3ace-9b6d-79c2447a751a | -17.70531 | -46.77412 | 2026-06-28 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 917a3e48-b495-386d-a0bf-4be775d7205e | -18.48725 | -54.1082 | 2026-06-28 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 857bb2cd-4cca-321c-9784-04862132c538 | -17.70493 | -46.77784 | 2026-06-28 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3f5ee129-220c-31c2-8ddb-658d6f04ff9e | -20.97554 | -49.74788 | 2026-06-28 05:01:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3ef24201-adab-3d2f-826f-fafdb08bc21e | -18.47787 | -54.09823 | 2026-06-28 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e4465644-a217-3101-83fa-11bbdaf48f1e | -17.70432 | -46.77781 | 2026-06-28 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2de903a2-9eb2-3f74-aa13-73f3df6e57c1 | -18.76839 | -57.37312 | 2026-06-28 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 89b2e0de-97bf-390a-aec8-0ef4872168aa | -18.47727 | -54.10241 | 2026-06-28 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5c91b70a-a24c-3c84-8092-be09f46cf606 | -11.2279 | -54.3036 | 2026-06-28 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 0cae090c-a6a8-33d7-b72c-4e2a79800a4b | -12.194 | -52.8657 | 2026-06-28 05:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 9737e06e-babd-32ac-b5e5-d135fc7ec269 | -12.1937 | -52.8866 | 2026-06-28 05:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| cf0fc912-993a-3921-af52-ad5582169341 | -11.209 | -54.3053 | 2026-06-28 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 167f59c6-4549-3565-8ae8-fd1813f1638f | -11.2093 | -54.2848 | 2026-06-28 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ce89c453-412e-3425-9494-17dbc5759511 | -11.2279 | -54.3036 | 2026-06-28 05:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| a7473610-6298-351a-a2eb-319defd7749c | -11.209 | -54.3053 | 2026-06-28 05:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 41a3b6ab-3835-3aca-b7ca-ca64c919a633 | -12.1937 | -52.8866 | 2026-06-28 05:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 69c2c565-53eb-375b-9790-a285caf68f10 | -12.194 | -52.8657 | 2026-06-28 05:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| cdadc1a7-2ce9-3da4-99d8-eb788cebaee1 | -12.1937 | -52.8866 | 2026-06-28 05:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 5383b4b2-405d-3370-a9c6-a956d06e3f74 | -12.194 | -52.8657 | 2026-06-28 05:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| de25e1d2-287f-34c1-be69-4ca4a58a61c2 | -11.209 | -54.3053 | 2026-06-28 05:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 54b24204-bfa6-3953-9752-69dc9edbf082 | -11.2279 | -54.3036 | 2026-06-28 05:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 0655f697-015a-3c16-9607-fc61e8ce79ed | -4.28232 | -48.36495 | 2026-06-28 05:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 39945b65-498d-38dc-b545-3e0c83024b62 | -4.28305 | -48.35984 | 2026-06-28 05:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e0a22eb6-5c09-397c-9beb-1ebe119fd5a1 | -4.28952 | -48.3605 | 2026-06-28 05:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 180f1b77-bce0-3e7f-97dd-f7fc48d2e173 | -11.88544 | -57.11039 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6130534-083f-3420-a5fb-6adb967b5fdd | -12.18678 | -52.89071 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74355525-5e45-3aaa-810e-ac64ba6034fb | -9.03495 | -61.33161 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbdabe17-d91e-381b-9cd5-e7416082a929 | -12.18935 | -52.87027 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 768ce02b-8547-3ee5-94a4-92ca3e01842f | -11.2183 | -54.30848 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a7d7891d-9c6a-35d0-b230-92fe47b04784 | -11.92138 | -58.66001 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cbd014a-4c82-3353-afa9-099a6a08730b | -10.29893 | -57.13575 | 2026-06-28 05:33:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9602e3f3-cb1a-3303-976d-9c2a8e99818c | -11.88267 | -57.11138 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad0d195d-ff72-3e3e-8bf8-e3e8d6dceb60 | -12.19212 | -52.89146 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28107116-201e-3d93-8000-4d661ca17805 | -11.94306 | -58.61427 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62b270a7-3f14-363b-9612-73b3c94d838e | -12.20049 | -52.86833 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b5531c62-3af5-31b6-bd0b-d38d100dd287 | -9.08231 | -59.41214 | 2026-06-28 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 266cb986-2053-3c33-94a9-9f11fbe7fb68 | -9.16702 | -58.07362 | 2026-06-28 05:33:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57d88546-cd85-3100-9531-87f5e558fb7d | -11.94003 | -58.60933 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e81178c-12f1-38ef-9410-2e0232b03839 | -11.92505 | -58.66051 | 2026-06-28 05:33:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3277dd51-8bd6-3d7c-80da-4240cf983662 | -12.18016 | -52.90014 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99d195e4-de4d-3fb5-a0c3-2b6ce2e93621 | -11.53152 | -54.79393 | 2026-06-28 05:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb269a3a-9641-3337-9d0f-a2860df027f7 | -10.63668 | -50.54043 | 2026-06-28 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97423716-f625-3a48-910c-c16218267eee | -10.35957 | -50.18042 | 2026-06-28 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24116e21-89bb-32de-b31d-62b046d8917f | -12.19662 | -52.89892 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3e2f3ee-bd21-3511-97bc-383da49db375 | -10.7737 | -54.11197 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 518cb713-cb8a-37cc-8ffa-dc7f7bf469d0 | -11.91356 | -57.41115 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38cb2d7c-8f81-3940-976f-03b094777863 | -10.80688 | -56.61535 | 2026-06-28 05:33:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34cf88b6-076f-3cb7-87c8-13b215a9615b | -11.34612 | -55.26884 | 2026-06-28 05:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb479235-d3f4-3b7f-9164-59c36571c7a1 | -11.21899 | -54.30322 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bf49612c-6395-3fab-ab25-9e6d018502e0 | -12.18635 | -52.8941 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfa29d86-6e72-3e23-b1ad-31afda6f2f0f | -11.3186 | -54.46606 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35033fd4-1413-34b9-a111-10f5a5c72978 | -10.05556 | -59.11512 | 2026-06-28 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5050eaa-994e-311a-aee5-9717a1373499 | -11.56111 | -54.5754 | 2026-06-28 05:33:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc140136-781f-37db-9ad4-908cc2967834 | -12.18624 | -57.15554 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef479644-8f2b-306c-8350-cb13ccb81f2a | -12.19471 | -52.87101 | 2026-06-28 05:33:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f2c4b43f-488f-31a1-9af4-8ab86cfa1be3 | -11.90923 | -57.12617 | 2026-06-28 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e475471b-4aae-300f-bcea-9a6f65d75d46 | -11.32267 | -54.47185 | 2026-06-28 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e537de77-8caa-30ad-af80-61166c3508aa | -11.87986 | -57.81972 | 2026-06-28 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7275c86f-94be-3c74-888d-ce9b9062f153 | -11.87405 | -57.82181 | 2026-06-28 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13d09636-661b-35c2-8d7d-143c8d731f3d | -12.09021 | -52.00978 | 2026-06-28 05:33:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5444f499-83dd-3b98-bf97-413936309578 | -12.08549 | -52.00135 | 2026-06-28 05:33:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e59c223f-10ab-3f99-8381-edbb4dc20e9b | -9.12634 | -58.24952 | 2026-06-28 05:33:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 069fe219-0621-398f-90cb-41741d08f8d9 | -12.18832 | -57.16438 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be541b4e-9d9f-3d10-8bce-e5cc29129274 | -12.18581 | -57.15329 | 2026-06-28 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README20.md)
