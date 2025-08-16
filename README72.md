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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1db5fbcd-301f-3342-bd83-691412a6654a | -8.98973 | -60.51748 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d0a5be14-833f-3276-ab12-9293c634c97d | -8.81339 | -68.61654 | 2025-08-16 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f395c40-9071-3da4-bebe-8310e90467fe | -8.57421 | -69.69225 | 2025-08-16 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37efc41c-0c9e-3fac-bcdb-846077931c36 | -7.94585 | -63.22116 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8cce925-661e-3c3a-a81d-2e3bc144dc53 | -8.97959 | -60.54265 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8812c793-c859-35dc-b418-b24acd19aafa | -7.03552 | -59.62578 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff8a9186-68f3-32ea-8bee-6d2f9f5977b2 | -8.99218 | -60.49741 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 470af760-eb8e-3334-9468-d096ffeba722 | -9.34144 | -62.58978 | 2025-08-16 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82822a40-cd45-38ad-b95e-e666ecb3fe01 | -7.52319 | -61.32653 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc5b8115-259e-360e-9a63-b2854df65aa0 | -8.41417 | -67.74203 | 2025-08-16 06:14:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 983524ee-2c3f-341e-a137-710e9b57b6c9 | -7.95518 | -61.75864 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ed4b8c6-c321-3416-a53d-23461b85fd3b | -7.6173 | -63.32822 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47d92e71-b6b8-36a6-8701-3081ceeea17a | -8.98732 | -60.53715 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 515f4ca5-496e-322c-86f5-9efb172862ab | -7.03958 | -59.62013 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73dc6a37-99be-385c-81a7-996dbb035986 | -7.62434 | -63.32878 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c000542-dd24-30bd-9c1d-be23df8a94d6 | -9.5133 | -60.5355 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a825ae86-1974-3b16-abce-74a6b8e95d59 | -7.82018 | -61.3278 | 2025-08-16 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecce90f5-7464-33e5-b001-8df1832eb8ce | -7.93102 | -61.74496 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b4cd18a-3575-3906-ac45-14339edfe1ba | -7.95286 | -63.20988 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 69fc80f5-90a5-3909-95ef-8e9447031a75 | -8.98495 | -60.55659 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ad32d84b-7151-345a-bf02-062c021d3668 | -7.81295 | -61.33232 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58d5712d-2080-35e6-b530-6069dbf63d43 | -7.90479 | -61.74676 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce07d7be-aee7-3e86-a478-2ada99563f16 | -6.9345 | -59.54062 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a5f75e4e-8011-3a0a-8c9d-daeeb2a19774 | -8.97107 | -61.6827 | 2025-08-16 06:14:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 53963dbd-b2e2-3c90-a6b6-e1308ead4be0 | -9.5125 | -60.54213 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 16517745-5ef7-324a-b17c-b6579c6ee75a | -8.99055 | -60.51072 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5b4ff48e-1155-37c9-a08b-860829b84260 | -10.39468 | -64.50471 | 2025-08-16 06:14:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6584b5a4-51ba-3d31-9260-c87cd9deee0b | -8.4055 | -70.43846 | 2025-08-16 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dd8bf20-9a5c-3593-9422-6c0d3a723bad | -10.40021 | -64.50542 | 2025-08-16 06:14:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6db3c879-9a6a-33b5-b4b3-f7573c970832 | -9.50629 | -60.53471 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| da7ace47-2cfe-3487-acd5-38bcaa7e6153 | -6.94072 | -59.54885 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 140ed220-d00d-3971-8e53-0ab487889cb5 | -7.91187 | -61.74232 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ea5a3170-0f2c-3485-8349-7a94a7d7755a | -8.98119 | -60.52951 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9c34d6a4-0916-3f10-9718-ad23d4626a77 | -7.67359 | -63.31097 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cde2b2d7-3610-3e7d-a531-7323b9e9d4fc | -8.10286 | -61.19053 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c90b05f-2ced-3a2c-af62-dd19c3e92ab3 | -9.05225 | -67.42453 | 2025-08-16 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9ee5623d-05c2-3174-aefa-8ba1c4112fe2 | -9.50314 | -60.56105 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3b118220-3e02-3bed-afc7-a537b892158b | -7.91051 | -61.75268 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b3a29cf-41c6-3476-89a2-328735e5b49f | -9.50549 | -60.54136 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 226cf945-540b-3ce3-80b9-4a15805d9308 | -7.91962 | -61.73285 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b21d1f07-cfd7-3902-b071-addd440a163c | -9.04275 | -67.42768 | 2025-08-16 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 22817655-a5d3-31f7-93b5-923d59a007c8 | -7.91119 | -61.7475 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82b0a9c6-7249-367b-aa23-13f25ca154fd | -7.92618 | -61.74567 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6a2306f9-ae72-3aac-b590-7de715c4da16 | -7.52898 | -61.333 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ea2b22e6-e247-30e4-9583-d32fd298f174 | -8.98892 | -60.52408 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 32acc588-6cd6-3e9b-8a39-1fc55e8fed21 | -9.00279 | -60.52623 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 22e64885-77eb-3ed0-92ad-2185e8a943da | -8.98654 | -60.54356 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 4c7525a7-4aef-33dc-93db-a33eeb468f52 | -8.99833 | -60.50497 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9a3e3d72-e726-3043-9381-906bd4f38ac1 | -7.61675 | -63.33223 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28437e3e-081b-349a-a2f1-4049f9b7ebc5 | -6.93527 | -59.55472 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e31cd28b-d42c-33b0-901e-b93afb3f9259 | -7.92463 | -61.74413 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e88ca6b3-13ff-37a6-9836-4d65e9cda35a | -9.50234 | -60.5194 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72c9a9b6-5ba1-3bf5-8c85-aa66db13c7af | -9.5015 | -60.52608 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edca228d-4ef2-3223-8093-9e97a5d9d145 | -9.51092 | -60.55532 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f898ea01-38e9-3495-ba8e-8f671c3544c1 | -8.97341 | -61.71632 | 2025-08-16 06:14:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 25160888-6f6c-3c7d-a53a-6b0737c1bf5e | -9.04719 | -67.42831 | 2025-08-16 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7b21e6c1-2ecb-3eb0-8695-ac35d30b27e3 | -8.55646 | -63.92817 | 2025-08-16 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 563644eb-6f51-30c0-b75b-88102f0d4ee8 | -6.94164 | -59.54187 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 80594f98-ef62-3c1f-947d-9f50ef43e84e | -8.98038 | -60.53615 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 258e801b-9d43-32c0-a141-c0ed8db7db0b | -6.94258 | -59.53474 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99c3d461-69e2-3385-839b-56484baaa6f5 | -7.74977 | -67.14571 | 2025-08-16 06:14:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 186f649e-d48c-3ded-b211-efc51ddd631e | -7.52393 | -61.32091 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c432e27-b574-3a7d-97c9-f3c9fcf17481 | -7.62487 | -63.32478 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d070ae9-bc9b-3fae-87d2-01740697a7a4 | -9.03891 | -67.42265 | 2025-08-16 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ea98a2e-4238-3447-bcff-af426c0c7a50 | -8.99137 | -60.50403 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 02633f27-c15c-3d22-8cba-226fb393935e | -8.98415 | -60.56314 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f21fa877-0ec7-3cc5-8399-d35721370af5 | -7.61565 | -63.34024 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7354e3c1-e4b5-3dcd-b077-32c91bbfc429 | -8.98128 | -61.70621 | 2025-08-16 06:14:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a4a1a6fe-47dc-3f1b-a612-974fae251276 | -8.66578 | -62.46317 | 2025-08-16 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aeef65fd-833f-311b-b865-15b5330ee6bc | -6.9479 | -59.54981 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e94c1778-403e-3e0e-8015-60d314d46b91 | -7.9495 | -61.75251 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66a0d817-63c9-3e5b-849d-330a9f38eeb2 | -9.39311 | -60.55315 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccab31f1-4c64-3c8d-974e-9e862b2d8ac2 | -8.0593 | -70.57959 | 2025-08-16 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b415abc3-df9c-3f50-8710-0ca5dccca458 | -9.50392 | -60.55454 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7ede931e-2b7f-31b4-827c-50e853d2d4a0 | -6.93358 | -59.54757 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d52c2689-6b4a-3b94-933b-d85d8df52ad1 | -7.03869 | -59.62726 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a21df647-863f-330b-a40a-5e5e0f1258c2 | -6.9498 | -59.53545 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 159a6213-9040-3d82-acca-466fd3e824ab | -9.49737 | -60.55893 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5208e79f-1671-3634-a3e8-8aea07e54c20 | -9.02939 | -70.71289 | 2025-08-16 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7775e9b-adc7-30c8-8562-c7012e46dbb6 | -7.95223 | -63.21781 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1d2ef14-3498-3779-845a-3e6c64c45a2e | -9.00121 | -60.53905 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8e0576a4-42b6-3e19-bcfb-4941df6eda0c | -8.54987 | -63.93492 | 2025-08-16 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 164d8f5d-1fb0-30a1-b422-de809141d855 | -7.90411 | -61.75196 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6280812-1c3d-3228-9e74-8180793dbcb5 | -7.67828 | -63.31982 | 2025-08-16 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03b089d8-994b-382a-8e2e-6a495dadf4c3 | -8.99267 | -60.55115 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e9b8fc7a-39f8-3b53-a04c-835d2ef2afe2 | -7.56292 | -61.42696 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e07a8c4b-c9a9-377d-98ea-4dc4cef7fbb9 | -7.9502 | -61.74731 | 2025-08-16 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06d71bbe-c412-31ca-8f92-38fc300c47a8 | -9.03386 | -67.42641 | 2025-08-16 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fdc01c59-b0dd-30de-9aee-6a1f0729c8d4 | -9.84851 | -62.22269 | 2025-08-16 06:14:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0376ef55-8d4f-3b17-b09f-5983fcec7b56 | -9.49819 | -60.55238 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 151b77d1-f1dc-3f50-aee4-eb567968a0f3 | -9.39396 | -60.54646 | 2025-08-16 06:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40025cd0-def6-3f8f-9ba5-04696507e5e6 | -8.99187 | -60.55764 | 2025-08-16 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6a7bbcbb-dc21-3d84-8e8f-67800a02ada2 | -6.94885 | -59.54265 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 05b92b0b-371b-33f1-92ed-9bab3131c6f3 | -8.4121 | -67.74047 | 2025-08-16 06:14:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33a87a81-a494-3942-8958-5e27bccfd3d3 | -8.40186 | -70.43792 | 2025-08-16 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f046cba3-5df9-3e2a-8bec-c70efe84ac73 | -8.85898 | -69.15435 | 2025-08-16 06:14:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e611283-b655-334e-9883-a27d9e59e0c6 | -7.95107 | -70.84511 | 2025-08-16 06:14:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a779bcb8-9503-33d5-b4de-e6d9aa0e13ac | -8.97039 | -61.68812 | 2025-08-16 06:14:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ef90f377-5197-375b-9ddc-f1edceb7c758 | -6.94333 | -59.5487 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ab6140e3-4aaf-3aca-bf6f-d5e4ab935e28 | -6.95056 | -59.54923 | 2025-08-16 06:14:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README73.md)
