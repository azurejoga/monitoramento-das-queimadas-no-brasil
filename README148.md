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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d598f70-7993-3918-b363-c0ae22422e44 | -14.1268 | -45.5439 | 2024-10-07 12:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| afb8db07-6cc9-384f-9333-c24c709e2ae5 | -14.1258 | -45.5904 | 2024-10-07 12:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 206.0 |
| 0b300812-bf61-3d0a-9a74-192b8adcb75d | -16.8899 | -47.1532 | 2024-10-07 12:06:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 560501c3-37a0-3d7d-9c48-ddcb370600d7 | -16.8894 | -47.1763 | 2024-10-07 12:06:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 100.6 |
| b0db5452-dfc8-326f-bae3-dd9ce5eb5ef4 | -17.6877 | -53.0788 | 2024-10-07 12:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 226.6 |
| 2e4d51fe-b7c1-33f5-aff5-8182cb4eb3fd | -17.6675 | -53.1033 | 2024-10-07 12:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 201.6 |
| 7c1b72ef-0609-377e-9663-84a93740653c | -17.6873 | -53.1003 | 2024-10-07 12:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 1cba5b14-b941-32f6-acdc-c7e0d0b4edd0 | -17.6679 | -53.0819 | 2024-10-07 12:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 353.7 |
| ac3319a5-ed55-367b-a272-92e4ce6534a4 | -17.8319 | -53.7829 | 2024-10-07 12:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 07e77d04-3cd2-33b6-b22b-6ea452e006fd | -17.8314 | -53.8043 | 2024-10-07 12:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| acd3178e-6278-328e-8dab-bb45793db823 | -18.8899 | -54.4947 | 2024-10-07 12:06:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 79.2 |
| e55a90d6-1d50-3ca4-a1dc-f2285ae4cff4 | -18.8886 | -54.5587 | 2024-10-07 12:06:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 4ee944e4-4d8b-3e61-8d1e-e3b320f1362f | -11.7561 | -44.513 | 2024-10-07 12:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| de034256-0285-36db-8180-7bc23f7e3464 | -11.7566 | -44.4897 | 2024-10-07 12:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 370415f8-92f9-302a-a498-450563eadd6e | -13.8359 | -44.6162 | 2024-10-07 12:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 716ba49a-70c3-3219-9d90-3a892eddfb74 | -13.8549 | -44.6363 | 2024-10-07 12:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 12376373-acfa-389d-82f8-540e34a0f8d4 | -14.1258 | -45.5904 | 2024-10-07 12:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 521.1 |
| 159e36c5-a1ba-3962-a7c7-3480a9091e9c | -16.8894 | -47.1763 | 2024-10-07 12:16:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 87595b81-c498-3ccf-97dd-0b0a4e3c1d5b | -16.9098 | -47.1493 | 2024-10-07 12:16:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 111.4 |
| d122080d-3efa-3ce6-8526-cebd1abac3cc | -16.8899 | -47.1532 | 2024-10-07 12:16:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 152.2 |
| c965dc23-6d00-3830-9186-d32a7b886f63 | -17.6675 | -53.1033 | 2024-10-07 12:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 43158a83-cbfa-3a48-9a0b-a81b84a32cb0 | -17.6684 | -53.0604 | 2024-10-07 12:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 692bd573-5106-3fd8-a682-2cd0a2a6d131 | -17.6873 | -53.1003 | 2024-10-07 12:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 14e5d817-0ee7-350e-b38b-111faeb7ae18 | -17.6679 | -53.0819 | 2024-10-07 12:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 235.0 |
| e08e2b98-558e-3a64-b0fc-d7edb7803607 | -18.3211 | -47.1382 | 2024-10-07 12:16:48 | GOES-16 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ab94bac6-c0c4-3dbd-9325-dffc7cf971fe | -6.28433 | -36.19324 | 2024-10-07 12:17:00 | TERRA_M-T | CAMPO REDONDO | RIO GRANDE DO NORTE | Brasil | 2402105 | 24 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 9a0dcd47-d879-3b67-b69c-22d256b3c429 | -5.74474 | -38.18497 | 2024-10-07 12:17:00 | TERRA_M-T | POTIRETAMA | CEARÁ | Brasil | 2311231 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 8ffc8aa5-9f01-3e60-8d22-c736e320db48 | -5.16911 | -37.96988 | 2024-10-07 12:17:00 | TERRA_M-T | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 6903d109-04b0-3f22-b9f0-dbaac2a24d86 | -4.881 | -38.8208 | 2024-10-07 12:17:00 | TERRA_M-T | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| ad3f2a47-f686-3e36-8f8a-c5190d5273a5 | -3.3731 | -42.04231 | 2024-10-07 12:17:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| e75de7b9-ff46-34e0-a6b5-b1adc834da7c | -3.02068 | -41.7345 | 2024-10-07 12:17:00 | TERRA_M-T | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| b2a10926-b9b3-3b73-a83f-bf1e78ce1bf2 | -3.01137 | -41.73319 | 2024-10-07 12:17:00 | TERRA_M-T | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 56b43aa0-2b70-34cf-8774-bb84def5f6fa | -3.29587 | -42.23867 | 2024-10-07 12:17:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2d4e22bf-85e6-3def-b02e-53079e087eb2 | -3.20652 | -42.48609 | 2024-10-07 12:17:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a7a766fc-097c-3e08-9119-c32ddf1677e1 | -3.19684 | -42.48471 | 2024-10-07 12:17:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e8e27af9-ad0d-3bfc-9b53-01d7711dedaf | -4.59101 | -43.09642 | 2024-10-07 12:17:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 02a4adaf-0bd0-3bc3-abbb-ea6cfd9253c2 | -5.32164 | -43.07312 | 2024-10-07 12:17:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3172e3cf-037c-3aea-959e-7fa0544c502c | -5.27283 | -43.06607 | 2024-10-07 12:17:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 09153c95-0594-3d98-b4b0-787413b2fe00 | -4.27936 | -43.74329 | 2024-10-07 12:17:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| c4ba313c-33af-371a-947e-05815e700ea2 | -4.0474 | -43.2409 | 2024-10-07 12:17:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| bfafd1d5-0abc-3b2d-b69f-f896d5714743 | -4.04697 | -43.24583 | 2024-10-07 12:17:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 2be336a4-c1ca-3383-ba79-cb19f19450f4 | -3.77238 | -43.23483 | 2024-10-07 12:17:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b2033c29-4d87-37b3-b89f-1a0dbe09c40f | -6.3454 | -45.72889 | 2024-10-07 12:19:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 7939d3a2-6bee-3fed-8eac-7a0a56b068f5 | -6.34791 | -45.57772 | 2024-10-07 12:19:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 2cbaf66c-1c9a-3af5-b070-1bc724c03f8a | -6.34965 | -45.72333 | 2024-10-07 12:19:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 3cf71d8d-c15f-3156-b0a9-6b3fc945415c | -12.65923 | -40.14374 | 2024-10-07 12:19:00 | TERRA_M-T | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 40.8 |
| b2506bdf-57cd-324a-b1f1-661bc9520c7e | -9.38832 | -40.74079 | 2024-10-07 12:19:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| a1a053c9-d43b-30ec-ac8e-d60d573f2e35 | -10.7793 | -40.48661 | 2024-10-07 12:19:00 | TERRA_M-T | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 2e3f2347-4dc5-3949-af6c-ab2fcf8ff1b1 | -10.77799 | -40.49581 | 2024-10-07 12:19:00 | TERRA_M-T | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 4f6e2088-f7f0-35b3-90d9-9b4cda9cc273 | -10.52198 | -40.15786 | 2024-10-07 12:19:00 | TERRA_M-T | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 721635a1-ca87-3121-b471-f24541869466 | -10.51294 | -40.15658 | 2024-10-07 12:19:00 | TERRA_M-T | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| e6176382-5139-30c6-9bfc-da2226cb25ec | -10.49302 | -41.19947 | 2024-10-07 12:19:00 | TERRA_M-T | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 7f796f82-7dfa-3186-830f-ecc26821661a | -10.49173 | -41.20842 | 2024-10-07 12:19:00 | TERRA_M-T | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| ffef09dc-cd15-3a8f-be8b-26697519935f | -10.38371 | -41.06744 | 2024-10-07 12:19:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| df3cc89c-6bc1-3e7d-844b-c20df55026da | -11.21543 | -40.20328 | 2024-10-07 12:19:00 | TERRA_M-T | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 9b34f9ed-829f-32e1-a36c-9640b87b1628 | -13.66828 | -41.54455 | 2024-10-07 12:19:00 | TERRA_M-T | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 5a48b99c-e87d-3c4e-a25a-800c32e0b3ee | -12.76223 | -41.76408 | 2024-10-07 12:19:00 | TERRA_M-T | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| a2f5e8e2-4b20-3438-ad1a-6dc755d943d2 | -14.01668 | -42.07306 | 2024-10-07 12:19:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 2610ef9e-d395-311d-b031-8ee7ec77e263 | -13.69646 | -41.92659 | 2024-10-07 12:19:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| cd1f5900-ce11-3ed2-bb92-d1c3b574e56a | -15.10485 | -41.99517 | 2024-10-07 12:19:00 | TERRA_M-T | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 42eab2bd-593c-3e97-a43f-8f2f0982cc18 | -15.25971 | -41.94634 | 2024-10-07 12:19:00 | TERRA_M-T | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 6f492ec4-26dc-3ac1-96ee-b713698db0d1 | -15.25081 | -41.94503 | 2024-10-07 12:19:00 | TERRA_M-T | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| e715dd72-9fcc-3f5f-a394-65a978801099 | -6.27421 | -41.87195 | 2024-10-07 12:19:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 3a2ca19d-8051-3ab5-839c-4b025c66e5db | -7.83604 | -42.22063 | 2024-10-07 12:19:00 | TERRA_M-T | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 9615139e-e1c5-38b9-a220-41d7a380ddcc | -7.83464 | -42.23006 | 2024-10-07 12:19:00 | TERRA_M-T | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| c3c8111f-d4e4-32d7-9a55-dd38ebf4cb85 | -12.17482 | -42.43591 | 2024-10-07 12:19:00 | TERRA_M-T | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 9e07d8fd-c34b-3dee-a54d-9a5ae9f5ba24 | -12.17348 | -42.44506 | 2024-10-07 12:19:00 | TERRA_M-T | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 13ede0ce-da52-313f-a346-e3e69fdf8531 | -11.5879 | -42.47881 | 2024-10-07 12:19:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| de3aab1c-0e07-36ac-9a9c-44b3029a0883 | -11.56892 | -42.73144 | 2024-10-07 12:19:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 2dfbaa59-1216-3213-b7cf-41a10b5c3e23 | -13.53638 | -42.71172 | 2024-10-07 12:19:00 | TERRA_M-T | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 19.1 |
| d26f8e2a-f5d2-3423-a9b7-a3351db19369 | -13.49495 | -42.92534 | 2024-10-07 12:19:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 4ef188c9-4cdf-3505-baa0-3c7625da09d4 | -13.49358 | -42.93466 | 2024-10-07 12:19:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 48.9 |
| aa17ab9e-2528-33b6-9d31-5da78e98276b | -13.46177 | -42.39855 | 2024-10-07 12:19:00 | TERRA_M-T | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| ff2edde6-9abd-3d62-aeee-e11791dff450 | -12.84192 | -42.22502 | 2024-10-07 12:19:00 | TERRA_M-T | NOVO HORIZONTE | BAHIA | Brasil | 2923035 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 2bd92c7c-ceb2-33a2-ada9-b40009cacd26 | -12.5966 | -42.95238 | 2024-10-07 12:19:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| e95cb229-b070-379a-bb1b-ca8f050ad630 | -12.58898 | -42.94167 | 2024-10-07 12:19:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 77e657f6-38ff-3f08-a88f-1923af6d84cc | -12.58758 | -42.95103 | 2024-10-07 12:19:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 79d7d366-44d4-3cbc-8fe6-737680742bba | -12.56404 | -42.6754 | 2024-10-07 12:19:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 62aeb81e-e38a-3d38-a66b-83faaa4e0fac | -14.15294 | -42.77677 | 2024-10-07 12:19:00 | TERRA_M-T | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| ba8a9abe-2416-3331-bdf6-ed8b39a09f68 | -13.96395 | -42.11445 | 2024-10-07 12:19:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 89d0db40-e1f7-38ec-9535-364e83c787c0 | -13.8044 | -43.01666 | 2024-10-07 12:19:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 5ca2fff5-1690-3721-8312-86172fe8e448 | -13.80302 | -43.02596 | 2024-10-07 12:19:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| c47f5a63-f424-3c1d-b601-4fcddb4cfe36 | -14.48704 | -43.75007 | 2024-10-07 12:19:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 90939f9f-5f48-32e8-8282-b755fce786ea | -15.78021 | -43.863 | 2024-10-07 12:19:00 | TERRA_M-T | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 4cf43f5a-9bc9-300e-a2ab-163cd53c9fa5 | -15.77876 | -43.87255 | 2024-10-07 12:19:00 | TERRA_M-T | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 14e70492-1d8b-386b-bde3-dda7c8e5a551 | -13.8543 | -44.63783 | 2024-10-07 12:19:00 | TERRA_M-T | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 17f79e25-12b4-3310-88d7-e5bf3a16dbf7 | -5.87998 | -41.98282 | 2024-10-07 12:19:00 | TERRA_M-T | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 34fa1375-2638-3c0a-bba9-6da8c18b5264 | -7.64755 | -42.50148 | 2024-10-07 12:19:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 21.9 |
| c567f274-1dea-337e-81a7-3831571688c1 | -7.63546 | -42.51952 | 2024-10-07 12:19:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 2caa5bc6-de0d-305a-9142-bdc61191c7fb | -7.62624 | -42.51815 | 2024-10-07 12:19:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 2fb03984-760c-34cd-a229-d6b9c76871a6 | -7.30632 | -42.25055 | 2024-10-07 12:19:00 | TERRA_M-T | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 5a76b88e-f9c0-3b8e-acad-8f3017f9c42e | -9.43027 | -43.02548 | 2024-10-07 12:19:00 | TERRA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| cd96d728-473c-3cf2-8e7a-30abab5e93bc | -8.93293 | -42.60131 | 2024-10-07 12:19:00 | TERRA_M-T | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 2ced307c-ab64-3c3c-b5bc-4a5af3ab134b | -8.20272 | -42.55162 | 2024-10-07 12:19:00 | TERRA_M-T | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 8872edad-1e44-3f72-b240-52435c596f57 | -11.76446 | -44.4968 | 2024-10-07 12:19:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 743b28c3-021d-3a54-a135-2d918134b9fd | -11.76276 | -44.50785 | 2024-10-07 12:19:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 40a49162-2376-39d2-b956-76e3492fac8d | -11.75469 | -44.49527 | 2024-10-07 12:19:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 2f8acd54-e2d6-3faf-97c1-2535190d8ec3 | -11.75299 | -44.50633 | 2024-10-07 12:19:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 4027600f-ba6a-32eb-a173-a492f843658f | -11.74493 | -44.49376 | 2024-10-07 12:19:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9cc4ef1b-de6d-3222-9364-6ca5b279e307 | -13.49534 | -44.38279 | 2024-10-07 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |


[Clique aqui para ver as próximas entradas](README149.md)
