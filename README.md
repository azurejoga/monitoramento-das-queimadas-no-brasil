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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d950991b-3392-38db-8a1e-cf4f7d50b47a | -14.9246 | -44.6744 | 2026-09-06 00:00:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 54.2 |
| d0675be3-6b56-31a0-bf51-d0c13cce4796 | -6.6515 | -59.9258 | 2026-09-06 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 41f011c0-0f14-3bee-b6fe-3602f7aa7b9f | -9.4925 | -68.9515 | 2026-09-06 00:00:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 60.0 |
| e2cd5a65-4a8a-376f-87c4-e551915852f4 | -13.8183 | -51.6634 | 2026-09-06 00:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 2b383084-219a-3839-b6f3-b5980a235c57 | -9.3665 | -67.8263 | 2026-09-06 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| a28586b8-d681-3d3d-a520-356a027e9291 | -6.6514 | -59.945 | 2026-09-06 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 1e341aeb-ff84-3f73-8ada-a88005ecbdd7 | -14.905 | -44.6782 | 2026-09-06 00:00:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 71.2 |
| a56bcba1-52b8-34ba-adc3-bdc7aed4b941 | -9.874 | -60.2762 | 2026-09-06 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 19da5c17-6498-3ba9-a9be-ed0ee4a1b8db | -3.2239 | -53.1742 | 2026-09-06 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 3da03556-2f53-39d8-9067-e33c9b2575d8 | -3.5591 | -48.1882 | 2026-09-06 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 8a4e4cb2-12f9-3f38-b5f6-7d8035c3eed6 | -6.6698 | -59.9443 | 2026-09-06 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 0f473225-c5d2-3d5b-99e2-aa4560593942 | -3.5406 | -48.1889 | 2026-09-06 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| e20ef5cf-8845-3be0-860b-de9bd5fef017 | -5.1439 | -55.9543 | 2026-09-06 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 6957d8ac-aeab-33c4-9b87-d7a886eddc08 | -20.4586 | -57.3864 | 2026-09-06 00:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 1edb5483-6b87-3d1b-9b2c-c23159d3d0be | -5.1438 | -55.9741 | 2026-09-06 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| e4ffdacc-8b21-3c53-bbb3-c6e2a77e7935 | -5.2537 | -59.9732 | 2026-09-06 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 48324274-fc93-3db2-9398-e7bea6c85151 | -20.4384 | -57.3893 | 2026-09-06 00:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 71.8 |
| 42873223-5c73-35ab-8f6f-0a5fc44d0501 | -5.1423 | -56.2703 | 2026-09-06 00:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 7f35b2b7-2e5c-3704-98e6-04f09538b785 | -9.3666 | -67.8077 | 2026-09-06 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 01ce72ff-915b-3556-872a-3004d4e51bfd | -9.1257 | -67.8322 | 2026-09-06 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 9062db96-ec31-3f8f-9c01-4746b7f5c6a2 | -12.5197 | -62.6871 | 2026-09-06 00:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 67ece828-a098-3d2b-911e-d6e46bf5c98d | -20.4582 | -57.4074 | 2026-09-06 00:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 74.0 |
| 23c24cb6-b798-331a-afea-52e1588ae836 | -10.7492 | -60.7097 | 2026-09-06 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 26a8954c-9416-31a3-b2e2-0e1064d34101 | -9.1256 | -67.8507 | 2026-09-06 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 7087ef36-3c5c-3a78-9d4c-ba2fa414a29e | -10.749 | -60.729 | 2026-09-06 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 6b7b9dcc-1d84-3e1b-ab66-b21b52cb5843 | -3.224 | -53.1539 | 2026-09-06 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| cfb10aef-36f4-365d-94ba-e4cb9f2936d9 | -13.7801 | -51.647 | 2026-09-06 00:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a989c71d-d097-3073-9882-299c2264d0fb | -9.1443 | -67.8132 | 2026-09-06 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 4c04c4ed-6778-3db9-a5de-56701a4f3bc2 | -9.1442 | -67.8317 | 2026-09-06 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 126.9 |
| df875dfb-39fa-3e79-8b57-7be392c0d741 | -13.3298 | -61.1064 | 2026-09-06 00:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 8a40d461-6adb-3f76-81a0-5f577af234c3 | -9.1441 | -67.8502 | 2026-09-06 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 0271577c-8490-36f9-af7e-40e35cbe062e | -6.8813 | -55.619 | 2026-09-06 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| ff892987-3296-3bd0-8d21-e0c4191f1093 | -13.3296 | -61.1259 | 2026-09-06 00:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 9dd91eaa-c34c-35b9-bddb-f6c29f274b0b | -13.7993 | -51.6445 | 2026-09-06 00:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 342a22a6-eb3a-347d-8736-f20c61dabdad | -5.5042 | -44.0277 | 2026-09-06 00:00:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 0c01b80d-bb7e-32c2-9e68-061503d5b789 | -13.8186 | -51.6421 | 2026-09-06 00:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 75cf6515-c2bd-3c08-8b54-559fef87efa9 | -9.3665 | -67.8263 | 2026-09-06 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| d2629269-31ce-3a7f-a47a-85710cd21b41 | -9.1256 | -67.8507 | 2026-09-06 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 1c5b42d8-cc2e-3c28-91a9-8e8b259ba273 | -5.5042 | -44.0277 | 2026-09-06 00:10:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 6f0c1bdf-1dfc-37bf-981c-14262f5d987b | -9.1628 | -67.8128 | 2026-09-06 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| e83adb83-99c3-3176-9cbb-dcdb3854aa0d | -3.2239 | -53.1742 | 2026-09-06 00:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 75114a57-b7f5-325f-92c2-17a7fe90ebdc | -10.749 | -60.729 | 2026-09-06 00:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 0ace95c3-22ba-3fe4-866a-560b1d5b9443 | -13.3488 | -61.105 | 2026-09-06 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 2dd65934-a0e2-3517-91ae-00b1cb4dc793 | -20.4582 | -57.4074 | 2026-09-06 00:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 75.3 |
| 19b5d733-e3b9-3444-bff9-00768f1bb50c | -11.6497 | -48.5473 | 2026-09-06 00:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 82119ed2-b70d-38b1-a409-4f25b27ba1f0 | -10.7013 | -45.9244 | 2026-09-06 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 595349ba-c24a-3a30-b9f9-6c1f1c1c602a | -3.224 | -53.1539 | 2026-09-06 00:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 69a01024-e7bd-38f0-8476-55e0e9c40e86 | -14.905 | -44.6782 | 2026-09-06 00:10:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 80.1 |
| d7bbdda7-9520-3f2e-9102-82b3a50a6b7d | -13.7605 | -51.6708 | 2026-09-06 00:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| d47202e8-93ed-3738-8092-d2b78a056c04 | -13.3486 | -61.1245 | 2026-09-06 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 93.8 |
| efda7362-6301-3272-9d43-886e59cbe83c | -12.9524 | -42.4157 | 2026-09-06 00:10:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 65.1 |
| b1c645b0-517d-3cca-be34-922f3c82eb66 | -6.0923 | -47.3129 | 2026-09-06 00:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 606e367d-80ef-333d-aa04-2976658c8603 | -13.3298 | -61.1064 | 2026-09-06 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 1ab1a71a-804c-3da6-8717-c0dd1dc8f323 | -9.1442 | -67.8317 | 2026-09-06 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 67ef9049-001e-348b-a7da-8139891c275b | -13.7608 | -51.6495 | 2026-09-06 00:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 6cc62a14-e49b-3dd0-924a-f6b9065778c7 | -10.6819 | -45.9496 | 2026-09-06 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 8e83dcaa-202a-39fa-bb62-a6571d8d1ee1 | -10.6823 | -45.9268 | 2026-09-06 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| a731a505-5cf0-3b9a-8fb7-1967136778b7 | -6.6514 | -59.945 | 2026-09-06 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.4 |
| fed95048-b729-3da7-bc6b-58439bb528f6 | -9.1443 | -67.8132 | 2026-09-06 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| e5ce6f2f-b50e-34e0-b834-316d4f744efb | -6.8813 | -55.619 | 2026-09-06 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 265a90d8-a3f9-36bb-9b41-3b249bb48581 | -13.3296 | -61.1259 | 2026-09-06 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 4222cdb9-2659-391c-ac01-e6ed6dd1ffcb | -5.1423 | -56.2703 | 2026-09-06 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 066d2a37-4f54-38d9-8c75-f6977df147a7 | -13.8186 | -51.6421 | 2026-09-06 00:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 20c0b2d1-139b-3e81-b819-6fcb698d79e8 | -6.6699 | -59.9251 | 2026-09-06 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| d28fab3c-6c18-3d6e-984a-05b7e155d4bd | -3.5592 | -48.1666 | 2026-09-06 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| c370dfbc-aff8-3020-a7ce-905714c53c96 | -9.1257 | -67.8322 | 2026-09-06 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 118.5 |
| d0bb2689-8191-3743-a2a6-b5eb38fd7d3d | -5.1439 | -55.9543 | 2026-09-06 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| a1ed0ab3-7d96-38ac-8035-d2d6ff022267 | -6.6515 | -59.9258 | 2026-09-06 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 7866d118-28a5-32cd-9c93-58a8cb58226b | -3.5591 | -48.1882 | 2026-09-06 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| c5ea5f4f-9ca0-3a4a-86b0-8e5624f53dbd | -6.6698 | -59.9443 | 2026-09-06 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| afd5849a-dd8e-37f3-8173-03243f628747 | -13.8183 | -51.6634 | 2026-09-06 00:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| dd9eeced-d58e-3a86-b9ff-7fdc6bddb3c2 | -14.9246 | -44.6744 | 2026-09-06 00:10:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 85.3 |
| ca4763c4-d0e4-3080-a54c-fb24b59bb2f0 | -10.701 | -45.9471 | 2026-09-06 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 3f1ad068-6f47-3df3-b21c-ef49cbf5399a | -13.7801 | -51.647 | 2026-09-06 00:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 153.1 |
| fdbd1588-8bf4-357d-9c0c-0987681c9003 | -9.1441 | -67.8502 | 2026-09-06 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 17aee1c4-0adc-3c7d-a326-a0e0d4ea3e0d | -6.6513 | -59.9642 | 2026-09-06 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 4943725e-57cc-3728-aa04-8152c8f8c1f9 | -13.7993 | -51.6445 | 2026-09-06 00:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 110.6 |
| deebd9f5-2f29-3e35-b75b-45141ffe7544 | -5.1438 | -55.9741 | 2026-09-06 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 6a20d707-2978-380a-a894-8d8d0b42bbf4 | -20.4586 | -57.3864 | 2026-09-06 00:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 32740dba-81d4-3cf2-9ef5-00864a164a0d | -13.3106 | -61.1272 | 2026-09-06 00:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 78cb6b62-215e-3230-a5f1-a58a9cb33c63 | -9.0515 | -67.871 | 2026-09-06 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 99b4984f-9030-3f87-a5d8-9df95bc2161f | -11.6493 | -48.5693 | 2026-09-06 00:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 7e599b28-69e7-3a29-b596-44ff854fcbfc | -9.3666 | -67.8077 | 2026-09-06 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 1a401916-b3d0-3228-8e5c-fa867cafad9d | -10.7492 | -60.7097 | 2026-09-06 00:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 7587a622-3ee6-37ad-89ee-c86f4d826cf1 | -16.753401 | -41.7159 | 2026-09-06 00:12:00 | METOP-C | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 148c4454-228e-32af-92b6-2f5d457b6e50 | -13.7384 | -51.654598 | 2026-09-06 00:12:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 40d5502b-e13a-3563-9006-4daf435cbb58 | -4.4508 | -46.147099 | 2026-09-06 00:12:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 330f7852-9414-3cb6-bcdb-dbc926636cd9 | -5.8924 | -44.734501 | 2026-09-06 00:12:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54ff3f8d-f782-3c44-908b-22c4706bf567 | -14.9185 | -44.665901 | 2026-09-06 00:12:00 | METOP-C | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 79ebdd72-acdc-3023-b4d2-38b3a5ac5858 | -5.4966 | -44.023399 | 2026-09-06 00:12:00 | METOP-C | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e66f875-252b-3b7a-abbb-971a9f1d90ad | -17.4207 | -40.034698 | 2026-09-06 00:12:00 | METOP-C | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e7e88591-bb0d-3b3c-ad04-5f385038127a | -13.7963 | -51.644199 | 2026-09-06 00:12:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 68e96306-587e-38f8-8836-d2c74adb1216 | -8.9521 | -44.4058 | 2026-09-06 00:12:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d9563fe1-cd2b-3cf7-9a9a-1a0a51229fd2 | -6.3339 | -43.3526 | 2026-09-06 00:12:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7353c22-600c-3096-9cb9-4a098c401002 | -8.9619 | -44.403702 | 2026-09-06 00:12:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 17c623ad-24bd-3ff4-a619-d9bb7a0116f8 | -13.7812 | -51.615299 | 2026-09-06 00:12:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 229eceed-239b-3710-89f6-158084d3c090 | -4.3505 | -48.971001 | 2026-09-06 00:12:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91b05b9c-33fb-3d7c-a01d-acf7b473353b | -5.8905 | -44.7262 | 2026-09-06 00:12:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c76120c9-1ea8-3d5d-b921-7d48add221ea | -5.864 | -46.227001 | 2026-09-06 00:12:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2f4c7a9-03f0-3d0a-97d0-1214a70f22ae | -2.7569 | -48.566601 | 2026-09-06 00:12:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
