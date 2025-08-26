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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e70927ff-0043-3d5a-a73e-9b4ec8a3377f | -15.63593 | -52.72352 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bffac73-8efe-33f6-b34e-6b69cd1a05b2 | -15.64145 | -52.7318 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70187d8b-5880-335c-83d9-d54f738b5078 | -15.61549 | -52.70172 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99de5d75-c517-39e6-9e66-56be2d37b8a4 | -18.24193 | -51.2676 | 2025-08-26 04:49:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0607ad04-c04d-3ea2-a3c0-e522b4b749ec | -19.18011 | -48.72953 | 2025-08-26 04:49:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e0f536fb-2287-322b-872d-75029c81da17 | -15.64201 | -52.72822 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 676fc534-72ed-36ed-a9c0-5d3e70c077fa | -15.63481 | -52.7307 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2cb84e4-147a-381a-b8fd-21bd3cae4171 | -16.22689 | -58.72552 | 2025-08-26 04:49:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ba8720b8-5651-35c6-801c-77f207323382 | -18.34294 | -44.96024 | 2025-08-26 04:49:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8bdd71c7-99f0-3ebb-bcfb-ff8796c0cba6 | -18.85516 | -47.01449 | 2025-08-26 04:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4461b52-e8ed-33e1-b250-7fc2055c7b11 | -15.62157 | -52.70641 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c37662fc-cd2a-3dd3-a9b8-5739ae50985b | -17.21279 | -47.224 | 2025-08-26 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31d95b56-e705-3bc5-b080-6dd71ebe239d | -15.6484 | -52.72935 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a902ec4b-d0a9-3e26-ac88-87fe0937e944 | -15.63149 | -52.73016 | 2025-08-26 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b7fd3ca-f3e5-396c-bc79-ebfe672916be | -20.88711 | -49.0286 | 2025-08-26 04:49:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 52fed090-6891-377e-a3a9-0da151bbe33b | -18.87091 | -46.99798 | 2025-08-26 04:49:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf90b2a7-8f00-3f59-b6a5-0a83c9ff35f1 | -20.04579 | -44.46448 | 2025-08-26 04:49:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8a63ea5e-89ac-3e27-8b54-2859ab54eb13 | -7.3854 | -64.3475 | 2025-08-26 04:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 9528ef31-f18c-3b81-a68c-87bd8b5dd8ca | -9.1718 | -59.5211 | 2025-08-26 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| d3c4cb12-4a22-389f-a86b-f02933a620e7 | -6.8044 | -58.9568 | 2025-08-26 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| b99f67d7-cc43-3375-b62c-0330d1a7a8af | -9.153 | -59.5415 | 2025-08-26 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| a02c2a35-34bf-39ed-9e76-404eaa7584e1 | -8.8363 | -62.451 | 2025-08-26 04:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 38c34c9c-45db-317c-bdbc-c28740b79b39 | -6.2459 | -60.0174 | 2025-08-26 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 77128e0d-e472-37c0-a2b7-cb954a0d5b67 | -8.8364 | -62.4321 | 2025-08-26 04:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 88.8 |
| d07c6ca1-1025-36b9-bb20-ac12fad9049d | -6.246 | -59.9982 | 2025-08-26 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 25767bf8-3531-38ce-b96e-225279d762a5 | -6.2275 | -60.018 | 2025-08-26 04:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| e4739d21-1d85-3178-a8c0-91e95e259460 | -11.1591 | -44.7395 | 2025-08-26 04:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 3f479fd4-cc4a-30bb-8c3a-e3d3afbfb75e | -6.8229 | -58.956 | 2025-08-26 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 139.5 |
| da11c436-5dae-33cb-a463-6b5bd0caec7b | -6.8413 | -58.9552 | 2025-08-26 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 24fa3232-337a-335c-8568-4386e721b153 | -9.1722 | -59.4629 | 2025-08-26 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 7ef1ad94-634e-3c05-ac5b-4f4b258008f3 | -9.0787 | -65.7151 | 2025-08-26 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 34e84f3b-660e-38f2-a180-ed99d82c5809 | -8.8734 | -62.4495 | 2025-08-26 04:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 0a8f05cd-89f3-35c8-bb79-aaa554b3b68e | -9.006 | -65.4 | 2025-08-26 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 9efc480c-71db-3c01-bc8e-c14dbfc1b31e | -9.1724 | -59.4436 | 2025-08-26 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| ce0e970b-72e3-39f9-af20-3282e2b2f72a | -11.1587 | -44.7627 | 2025-08-26 04:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 264.1 |
| e24868d1-451c-3971-b0d5-74b869e5ec4c | -8.855 | -62.4313 | 2025-08-26 04:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 130.5 |
| b41685da-c463-3c9e-a099-390121cd22cd | -8.8548 | -62.4503 | 2025-08-26 04:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 117.4 |
| c04e70b6-3586-306e-8eb1-81635ba38150 | -8.9874 | -65.4192 | 2025-08-26 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| f6cec4ee-010c-3cf8-b5db-f7f8fccdb044 | -6.8228 | -58.9753 | 2025-08-26 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 9c72a5b0-0484-36ea-98df-8f52d8d29aab | -6.8043 | -58.9761 | 2025-08-26 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| af4201c6-2f36-3d59-859f-49ef0a94757b | -9.1904 | -59.5201 | 2025-08-26 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| c6e6853b-8f3f-3225-8489-22214e7bfd44 | -9.1717 | -59.5405 | 2025-08-26 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| fc276135-55b4-3baa-8d46-ddaef84d7750 | -22.89423 | -49.05774 | 2025-08-26 04:51:00 | NOAA-20 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8adae761-4ede-3cd8-97be-4d6f53311888 | -22.8984 | -49.0584 | 2025-08-26 04:51:00 | NOAA-20 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 813ca7e5-a259-32e8-8cbe-6fdd21b188f0 | -22.55443 | -49.76807 | 2025-08-26 04:51:00 | NOAA-20 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1250d82c-6d3a-3ad6-9395-817464ee716b | -8.8735 | -62.4305 | 2025-08-26 05:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| cd662b66-8109-3271-98a6-7b9bb49edbcc | -6.7635 | -59.6718 | 2025-08-26 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 139cfa28-62f0-3609-ab3a-49b40226f003 | -6.2459 | -60.0174 | 2025-08-26 05:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 484ada6c-ec96-38ff-adc7-a7eb31ee5b55 | -11.1591 | -44.7395 | 2025-08-26 05:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 90029f22-c090-380b-a57c-85c6f9273cb1 | -8.8364 | -62.4321 | 2025-08-26 05:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 73ebd712-f6b1-35be-af9f-be0c83493eaa | -9.0231 | -65.7169 | 2025-08-26 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 59bf0592-3d21-3d4e-819e-7c610f630e02 | -9.1718 | -59.5211 | 2025-08-26 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 75ad5fef-908f-319f-a7a7-9f494a86d5a1 | -7.3854 | -64.3475 | 2025-08-26 05:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e78005cc-c35a-39ed-9f98-f3c033bc8e8a | -8.8734 | -62.4495 | 2025-08-26 05:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.2 |
| c223ff05-5059-3052-96cf-6aa998d5e456 | -6.8228 | -58.9753 | 2025-08-26 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 42f02438-bbe4-334c-962b-6bed6a7d2713 | -9.1724 | -59.4436 | 2025-08-26 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 1b361e80-a3df-3e3e-a2bc-d737cada36bf | -9.006 | -65.4 | 2025-08-26 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.3 |
| d19c5491-7d3e-3141-bcae-c67383f25826 | -9.1717 | -59.5405 | 2025-08-26 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| fc544da2-481c-3fc4-85d8-381e745f6e4d | -9.1904 | -59.5201 | 2025-08-26 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e353c769-c554-30eb-9c4b-7fb6148ffce4 | -8.8363 | -62.451 | 2025-08-26 05:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 2ccb0562-6150-3832-85c5-e16e18765295 | -11.1587 | -44.7627 | 2025-08-26 05:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 277.5 |
| 75086c74-c241-3c55-b0b4-62a48510e0f0 | -9.0787 | -65.7151 | 2025-08-26 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 208db953-bd04-3fde-add9-f5b43d1451dc | -6.8229 | -58.956 | 2025-08-26 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 59a8eb57-1132-31b2-8f19-ed97b5f12838 | -8.8548 | -62.4503 | 2025-08-26 05:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 4f60173f-2861-3971-9b8b-fff34000d002 | -8.855 | -62.4313 | 2025-08-26 05:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 158.9 |
| 21a5094e-e794-3eb6-a48b-1c3d761e59f6 | -8.9874 | -65.4192 | 2025-08-26 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 1cf3d6f8-2e26-33ef-ae66-1b3c22120bf8 | -9.153 | -59.5415 | 2025-08-26 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b1b32b2b-ff7f-3589-bd55-d0995cd55de4 | -6.8413 | -58.9552 | 2025-08-26 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 356b10d6-f51d-30ad-93f9-278b4d0181bc | -9.0416 | -65.7163 | 2025-08-26 05:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| ac13d0e4-f88f-31e0-a38a-9b0a9c396bfd | -6.246 | -59.9982 | 2025-08-26 05:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 67608d2b-fe54-3c81-940e-bfa24650f5e9 | -9.0416 | -65.7163 | 2025-08-26 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 2695a2ed-8c62-31ba-8b52-153648aa02d1 | -8.8363 | -62.451 | 2025-08-26 05:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 8fe4215d-33b6-3824-a528-32fcaa7a0ddb | -11.1779 | -44.76 | 2025-08-26 05:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 3c98aa15-5974-3ff9-ba8f-0faf01eb18f0 | -8.8364 | -62.4321 | 2025-08-26 05:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| cfd70052-0b76-356f-aff8-0e9c4e548bef | -6.7635 | -59.6718 | 2025-08-26 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| bb4cb926-9dcc-3999-8326-e432e482df64 | -9.1715 | -59.5599 | 2025-08-26 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 33dff94a-4d47-3198-b83f-ea0acb48b4d0 | -9.1717 | -59.5405 | 2025-08-26 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| a3c15add-b0a0-3ac8-8673-9a43e0792529 | -9.1718 | -59.5211 | 2025-08-26 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 31700d00-206d-3874-89f4-17d9d2691dc4 | -9.1903 | -59.5395 | 2025-08-26 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 233449d8-278d-38a0-bf2b-13adf10bf2c5 | -8.9874 | -65.4192 | 2025-08-26 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 6a8904e3-dd93-35d6-8dc8-fc39b434f305 | -6.2459 | -60.0174 | 2025-08-26 05:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 4d6ce9b7-d0fb-3b2a-bf92-891a841259a2 | -6.8229 | -58.956 | 2025-08-26 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.6 |
| a4c4650b-938d-326e-9b02-2981c7080aed | -9.006 | -65.4 | 2025-08-26 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| ec8ccba1-245c-3f0a-90f6-113d410dbbd4 | -9.0787 | -65.7151 | 2025-08-26 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| a1fa6f1d-8194-393f-9e0f-360daf04f8b9 | -8.855 | -62.4313 | 2025-08-26 05:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 133.5 |
| e5eff120-61db-3bb8-ab1b-03bb5cd83d83 | -6.8228 | -58.9753 | 2025-08-26 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| d1a69295-b8a3-396d-8c0b-c7c9a14825f4 | -9.1904 | -59.5201 | 2025-08-26 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c8110524-fe2d-3421-8827-d79900496e82 | -6.2275 | -60.018 | 2025-08-26 05:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| bc23c5d1-b5a2-3f89-aff9-1c1a4b526427 | -8.8548 | -62.4503 | 2025-08-26 05:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 132.2 |
| 549f754d-81b3-3e65-9bbc-20debabcf97e | -8.8734 | -62.4495 | 2025-08-26 05:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| fed9d040-09af-3fbf-a909-5135611e4807 | -11.1587 | -44.7627 | 2025-08-26 05:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 320.4 |
| 44745563-f19c-3ce5-aaa5-da83c9e049c9 | -7.3854 | -64.3475 | 2025-08-26 05:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d4748803-f414-36af-8f10-ee95130fb33e | -6.7819 | -59.6711 | 2025-08-26 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 522c1eeb-da76-39a3-8b27-59559c914b35 | -11.1583 | -44.7859 | 2025-08-26 05:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 6f0f6d79-df9e-3f40-95bf-f18b5af39839 | -11.1591 | -44.7395 | 2025-08-26 05:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 48218770-6864-33b8-b2c7-175681ac15cf | -9.1722 | -59.4629 | 2025-08-26 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| fe91b970-62ce-31ec-8c54-5a3d5b0862df | -11.1591 | -44.7395 | 2025-08-26 05:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 9599192e-484a-34cf-835c-361c8c1902a9 | -6.2459 | -60.0174 | 2025-08-26 05:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 83729775-0f53-391e-b827-92e353a3c6cc | -9.0787 | -65.7151 | 2025-08-26 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 895bb0a9-cf03-31b2-87b2-b8201c2b2dea | -13.5908 | -48.1931 | 2025-08-26 05:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 82.7 |


[Clique aqui para ver as próximas entradas](README75.md)
