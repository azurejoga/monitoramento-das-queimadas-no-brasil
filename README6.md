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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f04eb33-f91d-3802-bd1e-afee317d9ce1 | -6.77061 | -59.76581 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 902a0d0d-a61c-3821-8e07-086bd0c7072a | -6.63424 | -58.97218 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| ac290ace-bafa-3b31-90b7-709e7db515d7 | -6.62305 | -58.96253 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 443ccac7-b647-3d70-a651-e198bb9cd7e5 | -6.82904 | -58.97842 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 81e9d210-fd14-3f82-ab79-993544b8e540 | -6.18275 | -57.66489 | 2026-08-17 00:33:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b5d20f89-ecfa-3383-8279-acf1435b6c01 | -6.10725 | -57.71922 | 2026-08-17 00:33:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bb776632-4474-30d3-8834-987f0fc3f8d1 | -6.11106 | -57.74733 | 2026-08-17 00:33:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 5888b212-904f-3d8e-b02b-405be8527a9e | -6.6278 | -59.07391 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 7dc723c6-efc2-3e77-9996-0b6d3396b1df | -6.70435 | -58.95692 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 7d8c40fe-af9d-332e-b004-c559a964e02c | -6.6866 | -59.06602 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 6539c0cd-14c7-3a54-baa3-12569e21b3a4 | -6.60361 | -58.96528 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 9755bfe5-5d45-3835-ac3c-d48716b57bb9 | -1.8344 | -54.49188 | 2026-08-17 00:33:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e2fe45ba-ddfa-3757-9515-00f27469228b | -6.69084 | -59.08221 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 80584b4d-74a9-326f-bd5b-9e27b19ab7fd | -6.11504 | -57.70863 | 2026-08-17 00:33:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1a906805-e966-306d-adea-99d68835194a | -6.59673 | -58.98843 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6de62123-b58b-31ec-be95-3bca1943c956 | -6.11886 | -57.73669 | 2026-08-17 00:33:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| e954c8f7-92d7-396a-8c7d-f2e8f33879b6 | -6.65224 | -58.95861 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 9942a21e-e9d8-3a03-9ba7-23594ed5cd29 | -6.84676 | -59.11144 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7c9ef4e2-7612-3fd4-a365-db6560a6e2c1 | -6.89507 | -59.00864 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3f554ebd-e144-32b4-9c7f-e64811a9d9fc | -6.7796 | -59.45308 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d6552b2f-831f-32f5-89ac-2956fa58865f | -6.10072 | -57.73916 | 2026-08-17 00:33:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a4dd984c-3baa-35d3-a4c5-be212ca8809f | -6.61333 | -58.96391 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9a5042bd-f3f6-3eeb-9a46-f085b7b9c33b | -6.62926 | -59.08502 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| bd4fe71a-ec86-3e76-a47d-5d0e198b256e | -6.77773 | -59.75905 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0c03f48e-f884-3c76-8d70-e38360042112 | -6.68798 | -59.06009 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| ced8d256-7cee-31e4-82e7-77948c32218b | -6.85005 | -58.98675 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| be966528-977b-32b0-b4bc-7fe8888836d6 | -6.64252 | -58.96001 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 30b4c58e-469d-3b07-a8c7-76f2952757e3 | -6.70148 | -58.9351 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| aa33c564-0a95-3596-8a5e-e8d2a17f335f | -3.46589 | -56.79905 | 2026-08-17 00:33:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3b43585a-4373-3108-b847-26b743de4f95 | -6.02906 | -57.82224 | 2026-08-17 00:33:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b11442cf-858a-32dc-9bf2-8c063f648431 | -6.8614 | -58.97939 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8907a263-85c1-3315-bd69-98facb25bc7b | -6.09945 | -57.7298 | 2026-08-17 00:33:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 15d45903-9fc2-31b2-b204-3a99fcd14ec7 | -6.59388 | -58.96658 | 2026-08-17 00:33:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b87622ff-369f-3cec-8063-c3da4e2fd1de | -6.0187 | -57.81409 | 2026-08-17 00:33:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6254d0a5-f6e7-333c-99b6-a98052efae54 | -2.80597 | -48.58636 | 2026-08-17 00:33:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 069e0e3a-27aa-3114-9200-32ae730446f1 | -6.12013 | -57.74604 | 2026-08-17 00:33:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 9d3f9b25-24d6-3d05-a0c8-a9e8990e3c5c | -6.72855 | -58.5892 | 2026-08-17 00:33:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ca86cf07-1741-3789-a71f-12ad4d5a439a | 1.59517 | -55.79436 | 2026-08-17 00:35:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0ff84d25-1c4e-3b36-80cc-9441e107c9a6 | -6.1107 | -57.723 | 2026-08-17 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| b924e8ab-6752-3170-a4d3-5283d82a7736 | -6.1106 | -57.7425 | 2026-08-17 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 0ee0a18b-948c-3a42-a67e-85c656cfbfd4 | -11.1296 | -46.5244 | 2026-08-17 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 5b80db0c-34de-3ffd-920a-aeceac9b8886 | -14.4739 | -45.6682 | 2026-08-17 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 7d02ac99-2902-3dfb-8e30-471fef2473ba | -10.4658 | -50.3907 | 2026-08-17 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| cd2dc0cb-13ec-3e1c-a723-927e7b0603c3 | -6.6015 | -58.9651 | 2026-08-17 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| c2948d27-accc-38f1-9e86-4d7a910d18a2 | -6.6199 | -58.9643 | 2026-08-17 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 57368c6a-0722-3bbe-9b8a-f61d4a1525c1 | -15.8994 | -55.5334 | 2026-08-17 00:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 06ca0c9f-5b53-3581-af74-9afcffeede3b | -7.3824 | -55.4924 | 2026-08-17 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 65d60ae7-4a42-36dc-85cc-2fa1dcac0d9c | -6.6384 | -58.9636 | 2026-08-17 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| b309e7d0-7937-37f8-a2c4-25169851ce29 | -12.3565 | -50.8848 | 2026-08-17 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 0584d8f3-6fb5-3479-b257-1cb753722b23 | -6.6014 | -58.9844 | 2026-08-17 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| ce4f3c8a-1185-38aa-a5c7-ed96290de8c0 | -8.9038 | -60.5962 | 2026-08-17 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| d9750081-ffc2-3f33-aaa8-e3a348e24b09 | -6.6938 | -58.942 | 2026-08-17 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 3cb4f851-4477-329e-b327-b0c89373c48c | -6.1291 | -57.7418 | 2026-08-17 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| f42191ed-dac6-34fc-829d-70e2719babb6 | -11.7157 | -54.6063 | 2026-08-17 00:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 66b85616-34ff-3c22-a322-a6e02cb96b94 | -7.3639 | -55.4935 | 2026-08-17 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 60d4161b-07f5-3c69-962d-341b7f4cdbbc | -11.1299 | -46.5019 | 2026-08-17 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 98e8d989-f4b3-365a-b039-b3c7f09b0b00 | -11.1487 | -46.5219 | 2026-08-17 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 044aa701-4183-3044-a9cc-c869e54c3402 | -15.9189 | -55.531 | 2026-08-17 00:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 4a7105e0-d137-3eef-b0d2-775daedc73ca | -8.9788 | -60.4964 | 2026-08-17 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 31af624d-acf6-3576-bf25-973b0026652a | -8.9787 | -60.5156 | 2026-08-17 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 6a8e2d62-444c-3d39-9939-1747f61c04d3 | -6.7123 | -58.9412 | 2026-08-17 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 1a5e92b0-162a-31a6-aaa5-084d288953e0 | -8.9041 | -60.5577 | 2026-08-17 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| fd66db58-cbcb-3d2a-9c27-82d815d33d77 | -10.4655 | -50.412 | 2026-08-17 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 0635cf57-11bd-3db1-b7bf-8887dde3420d | -11.149 | -46.4994 | 2026-08-17 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 087e3b96-cd46-35a8-ba3f-542f55df2d2f | -8.9601 | -60.5165 | 2026-08-17 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 879e3745-f6fa-3000-bbee-e7a0f2ba1970 | -6.6568 | -58.9628 | 2026-08-17 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| cc3e7d77-68eb-3a79-bb81-d859cd0ef50d | -14.4934 | -45.6647 | 2026-08-17 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 2ba70869-af88-32bf-b5b6-c50d512367b3 | -12.3756 | -50.8825 | 2026-08-17 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 19001efc-8627-360e-acd2-5cdfe55e4444 | -11.6967 | -54.6081 | 2026-08-17 00:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 8aba220f-d607-3caa-aed0-d6b1438acace | -8.9039 | -60.5769 | 2026-08-17 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 9e096f92-3b27-3013-a905-85eb594e161e | -6.6568 | -58.9628 | 2026-08-17 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| ee0778ff-a1f2-3300-addb-ea9285fafbf9 | -14.4934 | -45.6647 | 2026-08-17 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| c6002f55-c572-3cd8-90b3-1cf61e68bf9e | -11.7157 | -54.6063 | 2026-08-17 00:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 924d0b39-4cfa-30a1-9f80-c13451818d05 | -6.1106 | -57.7425 | 2026-08-17 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 3bf4bb1c-e112-3353-b95b-fefd46667133 | -6.6014 | -58.9844 | 2026-08-17 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| db0e999f-b665-33b6-9a32-8f8cc6c72fd6 | -10.4655 | -50.412 | 2026-08-17 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| af879005-4399-3706-bf28-f358764224ef | -8.9787 | -60.5156 | 2026-08-17 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 14284456-7d60-3964-9d0f-199c995ab483 | -12.3565 | -50.8848 | 2026-08-17 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1914cdd2-0519-31ab-aab5-91de13441823 | -11.6967 | -54.6081 | 2026-08-17 00:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 62a2e4a9-e081-36bd-a330-19b33ffa5cd1 | -6.6938 | -58.942 | 2026-08-17 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| a60163d3-549d-3555-afb9-3bde8283d3ec | -10.5088 | -50.0013 | 2026-08-17 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 9b72c250-1838-37fb-a617-283ddcc457a7 | -12.3756 | -50.8825 | 2026-08-17 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 885065ac-3cf3-3996-a9dd-222bb2fb3e6d | -15.9189 | -55.531 | 2026-08-17 00:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 35ff0988-aaa4-3d5c-bed6-22d51e62c26e | -8.9041 | -60.5577 | 2026-08-17 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 2ec22c18-8642-35b0-8090-caf45a001b83 | -6.6199 | -58.9643 | 2026-08-17 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 8ec3be5f-f2c0-3acd-be6f-9b34416e89d7 | -6.6384 | -58.9636 | 2026-08-17 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 52157385-44b8-3a58-bb6b-704d8a049b9b | -15.8994 | -55.5334 | 2026-08-17 00:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| e064a435-9890-3d41-b161-b1538dce1daa | -8.9788 | -60.4964 | 2026-08-17 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| bf3006e2-2f25-39f8-ad79-22d948841587 | -6.7123 | -58.9412 | 2026-08-17 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 1c1ff79a-b809-3046-bc50-e0e669482dc1 | -6.1107 | -57.723 | 2026-08-17 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 2bc8ee4e-5a2b-3739-a15d-bbcd28b9e111 | -14.4739 | -45.6682 | 2026-08-17 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 1eac2260-50d1-3ec1-a3a2-4cc9a0c56986 | -8.9039 | -60.5769 | 2026-08-17 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 38ae5d06-d410-3fa2-b980-ddc525891576 | -6.6198 | -58.9836 | 2026-08-17 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 6a936e6f-cea1-3fe6-bfd3-203f4e468178 | -10.4658 | -50.3907 | 2026-08-17 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 97f14f8e-c793-3f3d-80e4-58caf44777d6 | -6.6015 | -58.9651 | 2026-08-17 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 83488ca0-0c14-39f1-89df-c36148a5dae0 | -7.3639 | -55.4935 | 2026-08-17 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 7ba5ae4d-bdd4-320f-9735-c56a70b36566 | -7.3824 | -55.4924 | 2026-08-17 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 540a79f0-ef79-3d70-952b-dbb8be2f7486 | -8.9038 | -60.5962 | 2026-08-17 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 50bac81b-dd0f-3132-973f-23a638c2b93e | -6.1106 | -57.7425 | 2026-08-17 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| f2edc535-0c67-33fe-8a04-aa46547deba8 | -15.8994 | -55.5334 | 2026-08-17 01:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |


[Clique aqui para ver as próximas entradas](README7.md)
