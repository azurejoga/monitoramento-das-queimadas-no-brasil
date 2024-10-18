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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9118a050-8a1b-3ce0-900c-8ce814056e8f | -4.4072 | -45.9773 | 2024-10-18 04:05:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 71cfff6b-0774-32e4-8bc4-26a336128af2 | -9.962 | -67.4394 | 2024-10-18 04:06:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 4392fdf6-5b21-32f7-9c8d-8632e9163eb2 | -12.4967 | -63.1874 | 2024-10-18 04:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| ab21f53a-c82b-3fb9-baa7-bd80967d308c | -12.4966 | -63.2066 | 2024-10-18 04:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 82f58123-b5af-3239-9a40-4690f2ce4adc | -12.5155 | -63.2055 | 2024-10-18 04:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| e8a2f87b-1932-3a8d-b31e-204e16eca62d | -12.5339 | -63.262 | 2024-10-18 04:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 7496dd31-accf-3e99-a056-06b68c434062 | -17.2373 | -57.3079 | 2024-10-18 04:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.8 |
| 34ffb838-159b-34ea-8deb-2ef06ed05a88 | -17.2177 | -57.3102 | 2024-10-18 04:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 706a1521-4f3e-3c0f-87bb-2aa075296926 | -17.8246 | -57.4631 | 2024-10-18 04:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.8 |
| e98b1354-0283-3e38-9017-2f4b4aff44af | -17.8049 | -57.4655 | 2024-10-18 04:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 5c9178f7-48ef-3553-965c-43f3a1281ca1 | -17.9432 | -57.4486 | 2024-10-18 04:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.6 |
| 778dff51-920d-3484-87fd-477f72b00995 | -17.9036 | -57.4534 | 2024-10-18 04:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.2 |
| 7fec1a6f-aaf0-3272-a0a4-c15e5d65f385 | -17.9234 | -57.451 | 2024-10-18 04:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 166.1 |
| 2e7d9de2-7765-318c-802b-1a3e72f347ff | -18.1993 | -56.3399 | 2024-10-18 04:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.1 |
| 0dd06d57-497d-3cb4-9326-719b4366a1ff | -18.1986 | -56.3816 | 2024-10-18 04:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.1 |
| 20ef2bca-903c-380f-87f7-a1328aab4efb | -18.1989 | -56.3608 | 2024-10-18 04:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.5 |
| 6da8d57d-a848-3cb2-8816-8c4fee316b43 | -18.1997 | -56.319 | 2024-10-18 04:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.4 |
| f3c7b2c7-a91b-3e80-9e1c-bf7e260109f5 | -19.6005 | -57.0253 | 2024-10-18 04:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.9 |
| 3b7e4953-464c-3cf1-8122-f28865a633a1 | -19.5804 | -57.0281 | 2024-10-18 04:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.2 |
| d1111079-45d9-3c5c-8e6a-c368c53e7801 | -19.6009 | -57.0044 | 2024-10-18 04:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.5 |
| cbbc4b86-57e0-3d01-a600-cd274327d1ba | -19.621 | -57.0016 | 2024-10-18 04:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.1 |
| 1a1dbf3d-37bf-3df9-a458-90221c6d4ca9 | -19.6206 | -57.0225 | 2024-10-18 04:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 247.8 |
| 07758af2-5cca-33ad-ab15-5cf45560534a | -19.6202 | -57.0435 | 2024-10-18 04:06:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 168.5 |
| 5fa2c176-9abb-3290-949b-dd10b0d26ee3 | -21.9662 | -49.7186 | 2024-10-18 04:07:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.5 |
| 779be9f5-2c36-38a9-a890-f3de6990e5ff | -3.7009 | -45.9 | 2024-10-18 04:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 0598294f-cf0c-3dce-9b56-c60701f21512 | -4.4072 | -45.9773 | 2024-10-18 04:15:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| abbc5d07-c97c-365c-814a-3687f074818e | -4.4258 | -45.9763 | 2024-10-18 04:15:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 6b5c79f2-ecf9-3144-8a75-4ca530fb30c0 | -4.426 | -45.954 | 2024-10-18 04:15:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 9d7481c9-a557-39ca-b8c8-c517b8948132 | -9.962 | -67.4394 | 2024-10-18 04:16:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c0218e66-38fa-3c52-97d0-257de50b2493 | -12.4966 | -63.2066 | 2024-10-18 04:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| fd226987-ec64-3b48-a12f-1f44cb3c96e6 | -12.5155 | -63.2055 | 2024-10-18 04:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 736559b4-f603-3478-962c-b650a3f554ca | -17.8045 | -57.4861 | 2024-10-18 04:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 953f3565-f332-3503-bbfb-6d6ca3dbe560 | -17.8049 | -57.4655 | 2024-10-18 04:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| db548faf-b191-3a27-9fb0-5b87ab03211f | -17.8246 | -57.4631 | 2024-10-18 04:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 3d97d8ea-493e-30ae-9c9d-1cf2e2e43334 | -17.7855 | -57.4473 | 2024-10-18 04:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.3 |
| 703984f4-a79c-30ac-9833-50d9b87c9953 | -18.0632 | -57.3514 | 2024-10-18 04:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 4e611903-f089-3b1f-88bd-87211d3faf92 | -17.9629 | -57.4462 | 2024-10-18 04:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.4 |
| e211067f-2e70-3d7e-b066-b455ef19a0be | -17.9234 | -57.451 | 2024-10-18 04:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.0 |
| 74e32e0e-f3ad-39e9-b26e-965d3ad040d3 | -17.9036 | -57.4534 | 2024-10-18 04:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 0e3015c3-79d3-3acb-9b69-5462f1cace93 | -18.2537 | -56.6237 | 2024-10-18 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.4 |
| 56b9cddd-5cfa-3e0d-b8c1-b13fd391c1df | -18.1997 | -56.319 | 2024-10-18 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 213fe496-1186-3b2d-8278-6300dc83969a | -18.1993 | -56.3399 | 2024-10-18 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 09e2ad4c-9cfe-3100-9844-ec983d78b564 | -18.1989 | -56.3608 | 2024-10-18 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 65d4d27d-de51-30ee-bef0-452b75721c9b | -19.6005 | -57.0253 | 2024-10-18 04:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.6 |
| 94da8df8-f61d-3e58-98d8-d5a2985335dd | -19.6001 | -57.0462 | 2024-10-18 04:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 28f9bc1e-2baa-3aa2-bead-d479270f98c3 | -19.6009 | -57.0044 | 2024-10-18 04:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.0 |
| 680518b1-db0a-331d-bb36-90b9e4acf569 | -19.621 | -57.0016 | 2024-10-18 04:16:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.0 |
| 3012bb4d-6cc1-3dc5-9847-bce40cad95dc | -19.6206 | -57.0225 | 2024-10-18 04:16:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 292.3 |
| 1576d89d-7c42-3119-b8d2-bde0002370cc | -19.6202 | -57.0435 | 2024-10-18 04:16:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 163.6 |
| e92be6cd-d44b-34f3-a60e-c8f7ee8bb6ca | -4.4072 | -45.9773 | 2024-10-18 04:25:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| fd314d14-d6e8-3af9-ac46-e0e9c9eb4096 | -4.4258 | -45.9763 | 2024-10-18 04:25:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 635c68fd-3f5b-38d3-a495-37e16397d053 | -4.426 | -45.954 | 2024-10-18 04:25:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 67cbf8da-8af8-36df-98b5-24dd0a024439 | -9.962 | -67.4394 | 2024-10-18 04:26:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 8da9637e-a969-3498-8d55-a81ddfa94390 | -12.4966 | -63.2066 | 2024-10-18 04:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 89654096-3011-3292-85cc-9771f0332a5f | -12.5155 | -63.2055 | 2024-10-18 04:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 734bebce-cffc-363b-b3c1-8b190a0dc191 | -17.2373 | -57.3079 | 2024-10-18 04:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| c12ad8c4-1b78-3a23-91c1-98e8a3a3fb43 | -17.8873 | -57.2496 | 2024-10-18 04:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.6 |
| fbdc6d0e-18af-337b-a78d-b5b211cc9140 | -17.8876 | -57.229 | 2024-10-18 04:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 7d9f39d9-5782-3cdb-a23b-7325ed829c57 | -17.8045 | -57.4861 | 2024-10-18 04:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 745d28a8-4ae6-3b44-9896-056d02b6d3b5 | -17.8049 | -57.4655 | 2024-10-18 04:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 62e215a5-27c7-3217-afa7-c81437c562c6 | -17.8243 | -57.4837 | 2024-10-18 04:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| c99f9c15-c3b9-3484-a4bd-c447a9718838 | -17.8246 | -57.4631 | 2024-10-18 04:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| 36729e82-29f8-3bc8-8296-825edfb14938 | -17.9036 | -57.4534 | 2024-10-18 04:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.6 |
| 478a5e88-8fc1-3592-bcf4-4ca17deaa28e | -17.9234 | -57.451 | 2024-10-18 04:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.4 |
| 179280a8-593e-36e8-80e2-9b9f7d404f62 | -19.6005 | -57.0253 | 2024-10-18 04:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.2 |
| 057705d9-cd3f-3298-ba05-2e1d4d76adae | -19.6009 | -57.0044 | 2024-10-18 04:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.4 |
| e58b9690-6b87-3bd8-a952-b7c0b9f2bc90 | -19.6202 | -57.0435 | 2024-10-18 04:26:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.9 |
| efcc0816-accd-302e-8452-7a10e89c784c | -19.6206 | -57.0225 | 2024-10-18 04:26:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 245.9 |
| 9f832d14-ce1a-3e3b-825e-a9bdfe9cbd9e | -19.621 | -57.0016 | 2024-10-18 04:26:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.3 |
| 14a9d9f2-3a8f-305b-9ed0-f93b5502821a | -3.7009 | -45.9 | 2024-10-18 04:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 60.6 |
| a11d6015-d260-3501-ae05-4178d12f1ca9 | -4.4258 | -45.9763 | 2024-10-18 04:35:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| ed2acc20-3bcf-37f5-bbfd-5ab04d9d0be3 | -9.962 | -67.4394 | 2024-10-18 04:36:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 8e003442-f0c7-3c1c-b074-9d3fbaee84c1 | -17.7858 | -57.4267 | 2024-10-18 04:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| b94cb2bd-54b1-3632-b5f7-85d789839a51 | -17.8049 | -57.4655 | 2024-10-18 04:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |
| d2681a56-2439-3389-9190-f7fd1985bb33 | -17.8246 | -57.4631 | 2024-10-18 04:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.1 |
| e41025af-f490-341a-a867-21fd4433f963 | -17.8876 | -57.229 | 2024-10-18 04:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.9 |
| b86c2b0e-5875-3a43-bc5b-4d11fea7d120 | -17.8839 | -57.4559 | 2024-10-18 04:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 64558311-d710-3aba-9369-785741043b4c | -17.904 | -57.4328 | 2024-10-18 04:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.4 |
| 8c44e7ab-dbf7-30e6-9906-a67948ab365a | -17.9234 | -57.451 | 2024-10-18 04:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 155.9 |
| f6fa79de-ba01-3032-894b-49e94a59701d | -17.9237 | -57.4304 | 2024-10-18 04:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 09d685b3-efbb-310d-a6a1-738025a73ec0 | -18.0632 | -57.3514 | 2024-10-18 04:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.4 |
| a1dcd841-d790-3617-b7f7-9ce355103ba0 | -17.9033 | -57.474 | 2024-10-18 04:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.3 |
| c38b1a58-a619-348d-bef9-cac6a4165860 | -17.9036 | -57.4534 | 2024-10-18 04:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 178.7 |
| f6bab9b7-c824-37d0-8e37-ae340b7123f4 | -19.6005 | -57.0253 | 2024-10-18 04:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 7a5a56b5-0bb1-3164-aa43-36864ddb6f9e | -19.6009 | -57.0044 | 2024-10-18 04:36:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 98a1e2a5-ecf6-3508-a634-188096a62167 | -19.6202 | -57.0435 | 2024-10-18 04:36:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 0024eae4-746b-37b6-8f4c-f43e29dcfd98 | -19.6206 | -57.0225 | 2024-10-18 04:36:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 191.7 |
| 16db3145-e154-35fb-8723-27ea1fc10826 | -19.621 | -57.0016 | 2024-10-18 04:36:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.6 |
| 3ee508fb-de9a-3fe8-8e96-98a31e4ead37 | -3.7009 | -45.9 | 2024-10-18 04:45:24 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 66605636-ebfe-39cf-8bbd-4d20f180427d | -17.2081 | -56.6946 | 2024-10-18 04:46:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 6a846ec2-770f-35e9-9651-14aab00f6bf1 | -17.9036 | -57.4534 | 2024-10-18 04:46:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 178.3 |
| 1fbb2623-efec-3f14-8005-dbb3b2fbca67 | -17.8839 | -57.4559 | 2024-10-18 04:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 3d27454a-87f1-33ef-8ad0-5bafb17f177d | -17.9234 | -57.451 | 2024-10-18 04:46:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 148.7 |
| b871c217-b74e-3f4e-92d7-20c2662e6f6f | -17.9033 | -57.474 | 2024-10-18 04:46:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.4 |
| f3efc411-3e27-35c3-9451-ad89adbd615f | -17.9858 | -57.258 | 2024-10-18 04:46:44 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 60005c58-a64d-3a74-8fb5-146ebc1a6bce | -18.083 | -57.3489 | 2024-10-18 04:46:44 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 348d80ef-c8db-3604-a6a5-2b3d0e487333 | -18.0052 | -57.2762 | 2024-10-18 04:46:44 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 07433519-7732-35bc-bde5-626b13b9e370 | -18.0049 | -57.2968 | 2024-10-18 04:46:44 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.7 |
| 4f502ec5-9f84-3b91-b17f-1da6f7af2662 | -17.9855 | -57.2786 | 2024-10-18 04:46:44 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| b729ce50-4528-3ed5-8298-2dac337554ce | -18.0632 | -57.3514 | 2024-10-18 04:46:44 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.4 |


[Clique aqui para ver as próximas entradas](README30.md)
