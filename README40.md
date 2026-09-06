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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21142d38-dd2f-361b-944c-bbf59dd7455c | -3.4185 | -61.3273 | 2026-09-06 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| e91198a8-cea5-3200-820b-5804fd22fd18 | -3.6033 | -60.5664 | 2026-09-06 16:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| cbac35fb-ddd5-3dfb-bc9d-4653cefd8d9e | -5.565 | -60.1739 | 2026-09-06 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 24c286b3-a7cd-3788-b88d-8c89baaad8b8 | -3.4003 | -61.3087 | 2026-09-06 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| e01ffedc-717d-3cc4-acbe-321b19cc58a0 | -3.1279 | -60.6509 | 2026-09-06 16:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 9a6ddae0-4336-3d0a-9b2a-f1c39a304760 | -3.4002 | -61.3276 | 2026-09-06 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 9ff8265f-489b-3710-82b1-1089a6d0e66d | -3.3688 | -59.4079 | 2026-09-06 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f8770558-e5d4-32cd-922d-40010a3839e1 | -3.7646 | -61.736 | 2026-09-06 16:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| bf45370e-98c8-3b6b-91c6-595569ab51cc | -3.3687 | -59.427 | 2026-09-06 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 00d4c653-ae40-330c-83e4-4fffcd31775b | -3.9363 | -59.3381 | 2026-09-06 16:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 6fdb3a57-3019-3367-82b5-38ef8a98a98e | -3.7828 | -61.7545 | 2026-09-06 16:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| bd43d0b5-c805-3a4d-9b16-b3a546d6f0f3 | -3.3871 | -59.4075 | 2026-09-06 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 02bf5e97-c1f1-3648-b305-191f91e6af48 | -3.4269 | -58.3104 | 2026-09-06 16:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 134.0 |
| fe2bb53e-c1a0-3223-9f58-106ad18ad5c6 | -2.88 | -50.45 | 2026-09-06 16:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7149043d-f337-3542-99bf-d67e70e16df9 | -15.48 | -43.86 | 2026-09-06 16:15:00 | MSG-03 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e135b1b5-327a-3b5d-b5b4-27ad837ee60c | -3.4002 | -61.3276 | 2026-09-06 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| eccc5fe3-453f-3b7a-b7b7-5070b4469096 | -6.583 | -58.9658 | 2026-09-06 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 9c578c42-1e60-3b5f-ada0-3c9edfc5715d | -3.382 | -61.309 | 2026-09-06 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| f16314c1-9694-3fce-852e-6f4b4c21c9ae | 0.2115 | -51.5217 | 2026-09-06 16:20:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c5ad4203-eca9-3086-bfb0-9e3b4f97d28d | -5.9635 | -57.6899 | 2026-09-06 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| f524c13b-3b05-3fa4-8725-6c34b0e3b155 | -3.3871 | -59.4075 | 2026-09-06 16:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 9731dbc2-52d8-3254-9eea-8fc7baff24b7 | -3.6033 | -60.5664 | 2026-09-06 16:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 45d1f867-7186-3727-8373-b51da225f4e0 | -5.5648 | -60.2121 | 2026-09-06 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| fa377eee-69a7-3e54-8401-89f6b2873375 | -3.3687 | -59.427 | 2026-09-06 16:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 34475158-7135-30b3-b40c-84023e4f7197 | -3.4391 | -60.4175 | 2026-09-06 16:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| ad6bb4ca-fc38-32d1-b891-e8b2fc6826cb | -3.4003 | -61.3087 | 2026-09-06 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 417efb18-57e4-3a2e-b479-c37a7c962be2 | -9.6848 | -48.0728 | 2026-09-06 16:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 7314e55d-34a8-3320-b37b-8d9609ec61ab | -3.8404 | -60.7704 | 2026-09-06 16:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| c1ae4568-d975-3ab2-b8bb-770254ddb884 | -3.1462 | -60.6317 | 2026-09-06 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 59d99e4d-b33f-39de-80ba-ba13b6ff6f55 | -3.7828 | -61.7545 | 2026-09-06 16:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| de07f4f7-bbfc-3ece-9e3e-e988772453fd | -5.565 | -60.1739 | 2026-09-06 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 462b1455-195e-3e08-8a45-c664dff127ca | -1.4944 | -54.2563 | 2026-09-06 16:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| b1c900fa-cea2-310b-93b1-8f6c1d799462 | 1.8029 | -56.0587 | 2026-09-06 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 06bcf157-3001-3a28-b3fa-c2dd33f2fa7a | -6.7833 | -59.4208 | 2026-09-06 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 463687b1-88c0-3a6f-9de0-7aeb6de4bd8c | -3.4392 | -60.3985 | 2026-09-06 16:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| d93c47b5-3151-3488-b36d-fa46c738e82f | -3.4185 | -61.3273 | 2026-09-06 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 6f508177-9439-3c19-914e-6806913594c4 | -5.9819 | -57.6892 | 2026-09-06 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 781b7482-bdf4-307c-bf6d-17b8f70b2acd | -6.0188 | -57.6877 | 2026-09-06 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| bb13fd6c-8b89-366f-b832-72c609a9d244 | -3.9363 | -59.3381 | 2026-09-06 16:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 43eb0a69-01c5-3338-9191-4193e9a7fa07 | -5.5648 | -60.2121 | 2026-09-06 16:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| c86ab4f2-bd7d-3326-bc3f-69827b0f877f | -5.9635 | -57.6899 | 2026-09-06 16:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 55968398-19f4-31bc-af92-3b3a458a3819 | -3.7462 | -61.7552 | 2026-09-06 16:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 3d628ea9-1b2c-3d8c-8860-d88ee4914e65 | -3.382 | -61.309 | 2026-09-06 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 2a0a03a8-1c40-3a42-98a3-dd64df4c6cc9 | -3.3688 | -59.4079 | 2026-09-06 16:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 80aeecee-e013-35fd-aa58-135a1cb32e82 | -6.0188 | -57.6877 | 2026-09-06 16:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| b32d836c-d61e-3375-8e3a-727aa0d197af | -3.4185 | -61.3273 | 2026-09-06 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 1a6db54f-6362-313e-9444-d1a06aeb32c9 | -9.6848 | -48.0728 | 2026-09-06 16:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 84892abf-7a3b-3d46-b20a-c04331935a12 | -6.6357 | -59.4459 | 2026-09-06 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 5ad09679-7e26-3c02-a272-4ad6af020f08 | -5.4917 | -60.138 | 2026-09-06 16:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 4d8e5dc1-4299-3a58-bf2b-a9bc23871451 | -3.4003 | -61.3087 | 2026-09-06 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 5e26af10-2860-339b-b60d-d6733ac18573 | -3.3871 | -59.4075 | 2026-09-06 16:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| ceb7775d-42c2-3261-a8d1-02a2e28df5ab | -3.4186 | -61.3084 | 2026-09-06 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 4a5b451a-90a5-3497-ad1f-20c524c54a8e | -5.9819 | -57.6892 | 2026-09-06 16:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a57467b0-ae43-3609-a9bd-22ac292076c1 | -6.7833 | -59.4208 | 2026-09-06 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 6b990eb2-b3e2-31af-a004-8df3e63fb3b8 | -3.7646 | -61.736 | 2026-09-06 16:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 06f8026a-64ce-30c7-812b-3820e1a2d944 | -5.914 | -60.2009 | 2026-09-06 16:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| de62d78c-4027-3edf-8ae7-bd97552dba0f | -3.7462 | -61.7552 | 2026-09-06 16:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 29502fb7-47bc-348d-a947-c0e0852d9d43 | -3.4185 | -61.3273 | 2026-09-06 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 5df00eb2-518a-37a3-a3ea-2ce43d765388 | 1.4453 | -50.7655 | 2026-09-06 16:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 47b1b8dd-3c97-3aa6-aa46-26b8456118cb | -3.9363 | -59.3381 | 2026-09-06 16:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 7baafca6-1935-3bcb-8dcd-33988e309b98 | -6.7833 | -59.4208 | 2026-09-06 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 88db52ca-901f-3d9b-937f-71ad9c9a1a0a | -3.4186 | -61.3084 | 2026-09-06 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| f2a62570-40bb-3276-b2ce-42d5bd85fc4f | -3.7646 | -61.736 | 2026-09-06 16:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 6c7c8f5c-aa16-31db-beac-cb756312ca01 | -3.382 | -61.309 | 2026-09-06 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 6ef1e939-69ff-38db-a83a-1570d6e66c13 | -3.4003 | -61.3087 | 2026-09-06 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 855da52b-e7db-3e92-b84d-63cc232fa9ba | -5.9635 | -57.6899 | 2026-09-06 16:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |


