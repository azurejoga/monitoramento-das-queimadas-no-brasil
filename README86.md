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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e819b706-3fba-3662-a088-8cae15cf31ba | -10.9709 | -46.9266 | 2025-08-29 05:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e4674ad3-732a-3960-8e3e-593a7dcb15a6 | -9.1155 | -65.7699 | 2025-08-29 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| c61e15e5-b2f1-3d9d-8069-ea71897d8ddc | -9.462 | -60.549 | 2025-08-29 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 9db28f2d-5180-3b0b-af00-6c23d6bcf6c6 | -9.4432 | -60.5692 | 2025-08-29 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| a81e4e9a-2dce-3a28-8729-02f86e2efa57 | -9.7728 | -64.2657 | 2025-08-29 06:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 857a3059-3782-3597-8241-fab1d12d8f60 | -10.99 | -46.9242 | 2025-08-29 06:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 67ae390c-fea5-38ef-8a46-697779544e6c | -10.3812 | -57.8245 | 2025-08-29 06:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 71b2be89-9586-3aa4-ae0a-12c269ae7c79 | -9.1155 | -65.7699 | 2025-08-29 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ed245937-6844-34ed-99b7-7a96933fde9c | -3.4254 | -49.0517 | 2025-08-29 06:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 302f59e0-e27a-35ff-ad04-32310ba07548 | -9.4618 | -60.5682 | 2025-08-29 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| b1193913-24da-3356-9a50-1784d3ba9deb | -3.7693 | -54.8286 | 2025-08-29 06:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e321a19e-0d0a-3b6d-8653-cb454f855c17 | -10.9709 | -46.9266 | 2025-08-29 06:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| c19a90ab-118d-384b-94df-f94e48fda4ff | -9.773 | -64.2469 | 2025-08-29 06:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| eea6387e-2e24-344f-9803-5337d5087dfc | -9.4433 | -60.5499 | 2025-08-29 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 0d8c5cf5-dda0-330a-a31a-abdc4b5f94d3 | -9.1154 | -65.7886 | 2025-08-29 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 248663f7-05f6-3788-ada0-559fb32e0666 | -14.3146 | -51.9183 | 2025-08-29 06:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 240.2 |
| ffa9d3d9-f709-3a4b-9281-ca8b3c5c2a5a | -9.4432 | -60.5692 | 2025-08-29 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 56c794bf-0e19-3c88-b120-7c0e41cecb23 | -9.462 | -60.549 | 2025-08-29 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 74d4bac5-9312-3ba9-9ea6-32133ca08921 | -14.296 | -51.8781 | 2025-08-29 06:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 52087397-20f4-33fc-9d38-b28018217273 | -9.1154 | -65.7886 | 2025-08-29 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 3eaf64a6-658c-3c04-8313-4e0e239745d1 | -14.2956 | -51.8995 | 2025-08-29 06:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 457.0 |
| 414c23db-1cec-3f9a-ab8f-1029e50c1827 | -10.9709 | -46.9266 | 2025-08-29 06:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 7c605ea6-d4e6-3e2b-9c0f-9d7bcf790955 | -9.4618 | -60.5682 | 2025-08-29 06:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| b12df184-2492-30ec-8627-e7619963a1c8 | -9.7728 | -64.2657 | 2025-08-29 06:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 6fc7ba15-ee5a-3083-aed5-7e2b59538b48 | -10.3624 | -57.8258 | 2025-08-29 06:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 54e4897f-6611-3df2-8fbf-de9b6941f0ed | -3.4254 | -49.0517 | 2025-08-29 06:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| b634a701-02a2-3fba-8843-95669835e07e | -10.3812 | -57.8245 | 2025-08-29 06:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 2152bc26-f288-34c2-80f8-f6124236dbb0 | -9.1155 | -65.7699 | 2025-08-29 06:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 7a63102f-8a57-3b89-9635-f58596996044 | -14.2952 | -51.9208 | 2025-08-29 06:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 4a93d7a2-ffc5-34a8-9d27-b30d9dfad836 | -9.773 | -64.2469 | 2025-08-29 06:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| a498d297-d88c-34c9-b5e4-a87f4badd6a4 | -14.3153 | -51.8756 | 2025-08-29 06:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 12159afe-9c8f-39b4-ab6a-c2854384a615 | -10.99 | -46.9242 | 2025-08-29 06:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 12463464-cbf6-3fb0-9644-078ae50453f5 | -14.3149 | -51.8969 | 2025-08-29 06:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 701.7 |
| 3ff2b6d1-6ffd-382f-afe7-0f177c9f0402 | -14.2956 | -51.8995 | 2025-08-29 06:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| d665b95e-5bc1-309b-ac60-e297a272cdab | -3.4254 | -49.0517 | 2025-08-29 06:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 8807cfac-30d7-3a7f-8737-8c2869684e7a | -10.3814 | -57.8048 | 2025-08-29 06:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 5d29387e-7b61-3151-9566-5ef874d42d66 | -9.462 | -60.549 | 2025-08-29 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 02b02451-fa94-3474-83ab-684b3d88c0b6 | -9.7728 | -64.2657 | 2025-08-29 06:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 57b2dd27-9c8c-317c-a304-5dcb11fa0650 | -14.3146 | -51.9183 | 2025-08-29 06:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 97a08f11-f193-38c7-a3af-9d101f9aa1f7 | -9.773 | -64.2469 | 2025-08-29 06:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 0522e3ea-3b2c-35b5-883b-21519ba68ddc | -10.9705 | -46.949 | 2025-08-29 06:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 64bdc4ed-b10d-3195-ad17-a9fb4117b44f | -9.4618 | -60.5682 | 2025-08-29 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 039f2a25-261d-314f-a413-d8ee2fda3d40 | -10.9896 | -46.9466 | 2025-08-29 06:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| ae8452d5-2735-3364-b149-b2fca21a34f3 | -10.381 | -57.8443 | 2025-08-29 06:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 285dac5e-a452-35bd-92c7-16a9dcda8bf7 | -10.3624 | -57.8258 | 2025-08-29 06:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 121.8 |
| eaaa189a-a4bd-39f2-a554-2f364d1d14d7 | -9.4432 | -60.5692 | 2025-08-29 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 89408403-fd04-36d1-a3c5-d4e34ba4ea1e | -9.1154 | -65.7886 | 2025-08-29 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 88d20bc6-274d-36f6-a4b1-892cdb7f3068 | -10.9709 | -46.9266 | 2025-08-29 06:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 4354d36c-e30f-3e1f-90de-796c514895eb | -9.1155 | -65.7699 | 2025-08-29 06:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 47f92793-7609-3ded-9d78-30d02d0139f0 | -10.99 | -46.9242 | 2025-08-29 06:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| b10ff5bf-efdd-30fb-bae1-1f139d1a4dd0 | -9.4433 | -60.5499 | 2025-08-29 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 0ca08dbb-67ff-3ebf-99c1-c5e1952fd2b5 | -14.2952 | -51.9208 | 2025-08-29 06:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 131b8b3a-09e6-3001-8ea5-b753e640b274 | -10.3812 | -57.8245 | 2025-08-29 06:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 176.5 |
| 1bb450d8-d155-30a0-878c-5a7e8731cab3 | -14.3149 | -51.8969 | 2025-08-29 06:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 8545f0c1-1465-3305-906f-4ed30c30071a | -10.3626 | -57.8061 | 2025-08-29 06:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 58c02626-6812-334f-848e-abd1590cfc86 | -3.7693 | -54.8286 | 2025-08-29 06:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 5d672219-9830-359d-a256-c66fa0448b2e | -10.3622 | -57.8456 | 2025-08-29 06:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| c0c34b2d-be78-31cd-935f-667146f9d29f | -7.42225 | -70.15842 | 2025-08-29 06:20:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28971ee0-90fc-3603-a099-a32f0b6f5843 | -7.6029 | -63.34096 | 2025-08-29 06:20:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68547e32-ac86-37b4-8d95-3f886303b5c9 | -7.60356 | -63.33575 | 2025-08-29 06:20:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8d57f0a-4944-3c91-b5cd-f18b88a3ec57 | -7.53242 | -70.11687 | 2025-08-29 06:20:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc587d2e-d01c-3455-9b60-8d79c6dcbc61 | -7.57133 | -70.02235 | 2025-08-29 06:20:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86d365c3-0913-3245-8127-ba3ef673f417 | -7.56451 | -63.84494 | 2025-08-29 06:20:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d10fe728-e98c-3b11-8075-326554519cc2 | -7.55834 | -63.84404 | 2025-08-29 06:20:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da8e4504-d53b-3531-bdbc-e0e22ce431b3 | -7.42278 | -70.15488 | 2025-08-29 06:20:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35007229-c5a4-3942-9db8-93c4ae8de947 | -7.42373 | -70.15532 | 2025-08-29 06:20:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e473d373-d899-3175-b2f2-4ba16c3d70fc | -9.116 | -65.7803 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 894c21de-859f-327b-967f-365478f2488e | -9.53658 | -65.69044 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb3e7fb9-570f-3bf7-b5da-a65136911a23 | -12.43051 | -63.92105 | 2025-08-29 06:22:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 90995f15-4ab6-3209-876f-042cf383d317 | -8.95853 | -65.96089 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37f32fd6-061b-32a7-a93b-62a464e2d760 | -9.01252 | -65.71064 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d16f3a38-017e-3d57-9951-4c653924cfa8 | -9.03202 | -71.92213 | 2025-08-29 06:22:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8676ea68-e428-34ff-983f-f98485c42442 | -9.11552 | -65.78407 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3124c7fb-4fbf-3452-9332-09ea57f0d741 | -9.11104 | -65.73945 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c2cbb72-67db-3707-8b4d-c47a9eca331e | -10.2872 | -64.49281 | 2025-08-29 06:22:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd7dcfa7-d4be-3ec1-891c-2b5749fcbbd4 | -9.10997 | -65.78322 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c6c8e4ca-22f5-3027-be86-2175daf8f41f | -9.13566 | -65.28832 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0875d54a-8bf5-317c-9ce2-a8d1e6fcbf34 | -9.16002 | -65.79034 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 348d56e4-57f6-3061-83a3-8f52621ae23a | -8.44486 | -70.13587 | 2025-08-29 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 893251c4-3af9-3b16-8c22-544e64c15726 | -12.44419 | -63.91697 | 2025-08-29 06:22:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42eae795-d7b3-37a4-a9ed-b2c7b82972d0 | -9.1651 | -65.79486 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a5352c5-76c4-3dfe-8780-4cecd6f48b1c | -9.1095 | -65.78693 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68837ab9-5738-390a-861f-5a4ff0172983 | -8.53794 | -70.74765 | 2025-08-29 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c5dbcbb2-c553-3d9e-b11b-81d9702d989c | -8.30843 | -70.86951 | 2025-08-29 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a995142b-03eb-3ea8-960f-7b045639ec0f | -9.16051 | -65.78658 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 25fb7e2c-913a-3a61-8abd-28daa3a74782 | -9.15494 | -65.7858 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 13908406-6456-3620-81df-17958bea9dd0 | -8.95316 | -65.95312 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae0d926f-9c85-3557-8529-61ab9ac361ed | -12.43112 | -63.91542 | 2025-08-29 06:22:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8fe533dc-fd4a-38a2-bda8-a4a04fdcdf37 | -9.25325 | -65.89569 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c956d33-4114-3820-a003-48f5080cc826 | -9.12523 | -65.7968 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0572bdd-d816-3d46-8678-e4d40d3b05db | -9.10498 | -65.74231 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 275ebb41-8efb-3d7f-8818-962eb1e67745 | -9.01857 | -65.70779 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c7a4850-9087-3ea1-96b1-250d4314247c | -9.12014 | -65.7923 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1bf16da7-07e4-31c9-86cf-5fcdfbaee21b | -9.17115 | -65.79185 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00c9daf5-c1d2-38ad-822c-a4f574bece75 | -9.72679 | -64.90505 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 33e3a722-4e6c-3baf-8bbe-966d6fdd92f6 | -9.54424 | -65.69366 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cfec013-7220-38ad-a085-aed7d1d0cbd6 | -9.66498 | -65.03182 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 214d7072-17ca-3336-bfba-677b7c8e3e8b | -9.13539 | -65.80579 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7c5b2ade-25a9-3737-8f16-6e9d85b6a170 | -8.44739 | -70.14754 | 2025-08-29 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 394eef60-838b-3955-8183-0336a4b391d7 | -8.53462 | -70.74584 | 2025-08-29 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.0 |


[Clique aqui para ver as próximas entradas](README87.md)
