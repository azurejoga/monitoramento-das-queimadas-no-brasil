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
| d4a6118e-09dd-3a39-b8e5-a470769defb2 | -9.1375 | -46.6485 | 2025-10-17 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| d974188f-84f2-3adc-8dad-9593e4b8648f | -11.5729 | -44.0501 | 2025-10-17 01:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| f07d65c5-1d7d-3102-9dbd-bd563ac30a57 | -4.3872 | -43.406 | 2025-10-17 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 7297b3e6-4448-3f30-928c-ec216e7a3042 | -14.3034 | -51.4501 | 2025-10-17 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 3f6aae5b-1c5f-35b9-86d0-f15827719937 | -4.4248 | -43.3805 | 2025-10-17 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 4e1ba96d-b73e-3d2f-9a64-7622245d539f | -3.2545 | -45.9855 | 2025-10-17 01:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 184.4 |
| 8899d590-2d6b-3fef-8c23-642e70b2ad05 | -9.0821 | -48.0252 | 2025-10-17 01:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| ea9f9ccb-4909-3c36-86c3-cee67a1a81f7 | -3.2359 | -45.9862 | 2025-10-17 01:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 214.9 |
| 2c8301c8-d6f4-3086-8fde-4501e7f6f5bb | -4.4061 | -43.3816 | 2025-10-17 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 736eb2cc-9d94-3d98-978e-cf665e7c8c5b | -9.879 | -47.6779 | 2025-10-17 01:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| ec2c0182-0fa7-3a07-9b4f-7838e160afa9 | -10.1139 | -44.5801 | 2025-10-17 01:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 846fa753-bca0-3b56-a881-2299bbf3315f | -8.389 | -46.2333 | 2025-10-17 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 8f1313e2-d798-3c9a-a9a1-927bbdc8f4be | -11.398 | -44.1933 | 2025-10-17 01:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| b5244d1b-9352-3ef0-bea5-778cac7710a9 | -3.5028 | -52.4938 | 2025-10-17 01:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 0157e059-44c2-3c48-98d2-beb2969c7196 | -11.4748 | -44.1819 | 2025-10-17 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c80e5a10-a0f0-3cee-a850-737b4ca97261 | -10.5136 | -43.4052 | 2025-10-17 01:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 529f07a8-ee25-34f6-b1d5-3a538a0563a1 | -9.898 | -47.6758 | 2025-10-17 01:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| b74bf37f-7591-30fe-948e-b305c908235d | -3.236 | -45.9639 | 2025-10-17 01:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 256.9 |
| b91d78a1-77ce-3280-893d-bfd7f0b8c57c | -3.7752 | -49.4219 | 2025-10-17 01:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 1f8b442e-539b-3ab1-9eb5-210189bf77b1 | -10.2939 | -44.0221 | 2025-10-17 01:30:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 137.5 |
| e6a84b80-769f-3410-bf8b-6c436bbaf0cc | -14.3227 | -51.4475 | 2025-10-17 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 116eeba4-1cc1-33c0-8e18-6ab0936115c7 | -8.4081 | -46.209 | 2025-10-17 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 4c37166e-703e-3ec3-b126-653477ec7e0c | -3.7937 | -49.4211 | 2025-10-17 01:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| b73c1e39-f3a5-33f7-ace8-dbee923f8fe8 | -11.4539 | -44.2784 | 2025-10-17 01:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| abd9fcc4-ee8a-3755-b59a-764f2786862c | -3.5028 | -52.4734 | 2025-10-17 01:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 6721ea81-1a57-3e0c-8a98-00f8d21485a4 | -3.2546 | -45.9632 | 2025-10-17 01:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 195.0 |
| a45ce430-e21c-3b3e-bbd6-c49a1f1de712 | -10.5128 | -43.4525 | 2025-10-17 01:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| a8a8038f-868c-312c-97d8-4095c99f5b71 | -10.4941 | -43.4315 | 2025-10-17 01:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 219d227c-53a9-31c8-9baf-5a463f4413c9 | -4.4059 | -43.4049 | 2025-10-17 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 264.4 |
| ac8ab9dd-5663-3394-a195-36b5979aef2a | -8.4079 | -46.2314 | 2025-10-17 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| cb5c89a5-e6f3-3f05-8cd6-a91e3e012e63 | -10.2745 | -44.0481 | 2025-10-17 01:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 65a0e4ba-28ef-31f2-b7dd-9aeedd7a829b | 1.7848 | -55.9014 | 2025-10-17 01:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 0c1d2e4e-4c61-36fb-9c49-916c265c6f9f | -4.9548 | -44.956 | 2025-10-17 01:30:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| a579f77c-afc8-3363-b629-5f009c647afd | -8.7404 | -43.8659 | 2025-10-17 01:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 3dcf95a6-3880-3405-aa5e-dde81c04130a | -10.4945 | -43.4079 | 2025-10-17 01:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| ada1e253-dd9f-3e5a-979e-7ebcd8bf6938 | -11.5921 | -44.0472 | 2025-10-17 01:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| d66f1d83-a08a-38fb-a68f-1d2969a2515c | -11.4735 | -44.2522 | 2025-10-17 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 17aa9535-ec04-36ee-9a1e-79f25b9bec1b | -11.4731 | -44.2756 | 2025-10-17 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 5db91350-1a43-387d-ac85-abff38d33b10 | -2.7401 | -49.3927 | 2025-10-17 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| dec3584d-ea2c-30de-a83e-4e177b52f598 | -11.4543 | -44.255 | 2025-10-17 01:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 233.0 |
| 271511a8-fd34-3b0d-b16f-50e30236524e | -11.3976 | -44.2167 | 2025-10-17 01:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 7a15fc2a-05fa-3d15-8135-82aa7971442a | -4.4246 | -43.4038 | 2025-10-17 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 69e83957-7468-3d25-9c2a-da0680a2839e | -8.1996 | -43.3189 | 2025-10-17 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 15e41020-bfe4-36e5-95b4-7f31fac6c1e5 | -10.2748 | -44.0247 | 2025-10-17 01:30:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 174.3 |
| 96063e46-fed9-33d6-957e-64774d49fc3b | -4.4058 | -43.4282 | 2025-10-17 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 34c5a52c-b399-3534-a569-8a5da29c48b4 | -11.4939 | -44.179 | 2025-10-17 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 9f3aeda1-b5c0-3c8b-b864-3f44858f180f | -11.4547 | -44.2316 | 2025-10-17 01:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 67f967aa-fb34-324b-8f56-20d6940d0c50 | -10.5132 | -43.4289 | 2025-10-17 01:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| eee2378d-79c8-35a7-9781-41a3c0ca1549 | -10.2745 | -44.0481 | 2025-10-17 01:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 130.9 |
| e11676ba-fbd3-3d63-99cc-e1a56e0d3002 | -10.4941 | -43.4315 | 2025-10-17 01:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 7eb45c1d-0425-30e2-b395-97918dcb455b | -11.398 | -44.1933 | 2025-10-17 01:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| db800edf-26d2-34ba-8b74-ac7fbb8789cc | -3.2359 | -45.9862 | 2025-10-17 01:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 243.0 |
| 5932755c-af50-3a03-90c0-68662c3ac177 | -4.4653 | -42.9346 | 2025-10-17 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| a05e981c-dfb8-3455-a343-d6a00399453d | -11.3976 | -44.2167 | 2025-10-17 01:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 7d5ed8e4-2c9a-365e-8422-6fac019ede9c | -2.7401 | -49.3927 | 2025-10-17 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| b5440267-a8d8-3bd6-b1a0-c41ede7b4e4c | -4.4059 | -43.4049 | 2025-10-17 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 245.6 |
| c2094b49-4dca-3bd9-a757-4122845d75d1 | -10.5132 | -43.4289 | 2025-10-17 01:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 501e0a9e-c51e-3e16-95d5-1d16725f056a | -3.2545 | -45.9855 | 2025-10-17 01:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 121.4 |
| c56bcbdf-5eb1-3fb6-9d51-c539b8facf7e | -2.7585 | -49.3922 | 2025-10-17 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| f4ab2ff5-93b2-3a7b-9602-bf5144370675 | -11.4735 | -44.2522 | 2025-10-17 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 4d17ddf3-b47b-32f2-836f-5dfce8418d30 | -9.1375 | -46.6485 | 2025-10-17 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 949c8d5a-ad76-3a33-8137-e4af2c2a3403 | -4.4248 | -43.3805 | 2025-10-17 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| fc857d59-437e-3ac3-be63-205e7c864376 | -3.5212 | -52.4932 | 2025-10-17 01:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8082a958-d572-3357-b49b-de6cffe7b2fc | -9.0821 | -48.0252 | 2025-10-17 01:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 92d87a5b-a488-3c91-bb33-e3220281db95 | -10.2935 | -44.0455 | 2025-10-17 01:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 81a86c8a-ec54-3073-be53-bb48bdb2aeaa | -11.4939 | -44.179 | 2025-10-17 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| f668281e-66a2-361c-9c11-ed0d0447fdc5 | -11.4752 | -44.1584 | 2025-10-17 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| d7ef1075-9b57-3899-a3d3-451b8f176c6e | -10.2748 | -44.0247 | 2025-10-17 01:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 6dc42b69-9a11-379a-970b-9d8732b98c1e | -4.3872 | -43.406 | 2025-10-17 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| f12af772-0ccb-3efa-9777-9ddc433c2e53 | -11.4739 | -44.2287 | 2025-10-17 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 672b1b23-d743-3c0f-a4ac-755ca7658163 | -3.7937 | -49.4211 | 2025-10-17 01:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 7dfab4f9-71d9-3d01-99e5-e1c7c508d673 | -11.4944 | -44.1556 | 2025-10-17 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| e8d00a4f-f1d1-3d94-9186-fb20337cd3c9 | -10.5136 | -43.4052 | 2025-10-17 01:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| b2054121-e731-3c97-b5b2-29c4d0b0dd2a | -4.4058 | -43.4282 | 2025-10-17 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 2542d227-38f5-3ea9-9bcc-358112021478 | -11.4547 | -44.2316 | 2025-10-17 01:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| efa168ce-8bdc-30d6-93f9-33101fc6aa60 | -3.5028 | -52.4938 | 2025-10-17 01:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 961044db-700d-3d65-905e-a4484e769458 | -11.4543 | -44.255 | 2025-10-17 01:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 123.7 |
| c82099a1-27cd-3371-9e09-427f172bdc54 | -3.5028 | -52.4734 | 2025-10-17 01:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| f9b23340-1d07-37e5-87a0-7219d9dd2b90 | -4.484 | -42.9335 | 2025-10-17 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c192f029-4e58-313d-8762-1ecd96479cd0 | -3.2546 | -45.9632 | 2025-10-17 01:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 142.8 |
| edf9e15c-c8a8-357f-8d2f-814a9197bc63 | -11.4731 | -44.2756 | 2025-10-17 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 27421e98-d7a3-3075-8360-551ca028c1e2 | -10.2939 | -44.0221 | 2025-10-17 01:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 209.7 |
| 88a33703-f744-3686-84ca-e577e6c4fef8 | -9.879 | -47.6779 | 2025-10-17 01:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 9220f9e7-99be-36a4-a37e-67850e330d12 | -11.4748 | -44.1819 | 2025-10-17 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| a0102456-24b6-3a49-861b-ea0d20d9988e | -3.236 | -45.9639 | 2025-10-17 01:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 334.0 |
| 4d7cde21-5402-3b4e-9b81-dfeaec0cf3f4 | -11.5921 | -44.0472 | 2025-10-17 01:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| af6fdba9-8e5e-3ea5-8d2f-4a69f27f2dd3 | -11.5917 | -44.0707 | 2025-10-17 01:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| cce86fd1-dbe5-379c-8643-c601077f8d3d | -4.4061 | -43.3816 | 2025-10-17 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 99bccbd4-5ddc-3881-b816-c146760ef6f5 | -4.4246 | -43.4038 | 2025-10-17 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 512616ad-a2a6-38ac-a79a-42efcafa54e2 | -8.7215 | -43.868 | 2025-10-17 01:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| ec2f9043-40a2-3424-8e4f-d972e3b64c47 | -9.0821 | -48.0252 | 2025-10-17 01:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 1f19acc4-8793-3188-8045-2447034ca2c3 | -11.4748 | -44.1819 | 2025-10-17 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 1034d6b6-6a44-376a-9849-825d9e106d41 | -4.4248 | -43.3805 | 2025-10-17 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 2891ba12-e34b-3d33-ab0b-8136cb93bcf8 | -3.5212 | -52.4932 | 2025-10-17 01:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ccc03a5b-3ac2-3e13-933b-89fccb3a2ff5 | -10.2748 | -44.0247 | 2025-10-17 01:50:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 489b17be-7483-3714-a740-f23fe9653202 | -11.5917 | -44.0707 | 2025-10-17 01:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| d303cc4a-74dc-3d3d-9362-60d8b6a1dac4 | -11.4543 | -44.255 | 2025-10-17 01:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 293fc5ab-f13b-306e-9405-c756b3a7f329 | -11.4939 | -44.179 | 2025-10-17 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 6d6d79a6-4474-3fac-adea-802ccbd858f9 | -10.2745 | -44.0481 | 2025-10-17 01:50:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 37ebf1a9-8fe3-3afe-a9b0-0cb637c27843 | -3.7937 | -49.4211 | 2025-10-17 01:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |


[Clique aqui para ver as próximas entradas](README18.md)
