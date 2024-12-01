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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f42a430e-f332-3138-b1e7-0fa4a571bcee | -3.29435 | -53.6784 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d0cb515-4507-31fc-a7a0-685413a54a7b | -2.60751 | -51.80807 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da7c749b-7661-3f05-a6ec-cfabde78acc8 | -3.74963 | -51.78045 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 959ff27d-904f-3c00-9727-1b901706658a | -3.12307 | -51.79301 | 2024-12-01 05:08:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f7077e1b-d4e7-32fa-a7ab-5c628a94b55a | -2.83326 | -59.26359 | 2024-12-01 05:08:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 238af58a-feb5-3283-af96-453224f95e09 | -3.25947 | -53.64425 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c318e828-0e08-3512-b553-cc1807c0d3bf | -2.60954 | -54.07665 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4a2549b1-52d5-337d-961b-68dd7895e8b7 | -2.95164 | -51.78912 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5e93411-a494-3d56-9e05-129370ddef46 | -2.86339 | -53.98709 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4bcdf7b-3919-3c7a-a8e2-93e6bccb604b | -2.27458 | -53.46687 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c92da75b-b2e4-3659-9637-69cf4826e584 | -2.63975 | -54.07659 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c17b2e87-22eb-3a79-8a91-90d067b22ab2 | -3.22454 | -51.50505 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57ce79cf-9a3d-3c77-bd6d-e0eb7ad241f9 | -1.30147 | -55.74063 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1600a0bc-2a4a-3e02-856d-4f30364c17b4 | -3.01224 | -53.22934 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 650919bc-6627-3d2a-866d-dbcb6ecb885d | -3.50015 | -53.79808 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6b0cbe9-dec2-3fdb-a5ce-5fc4ece14cc9 | -2.87217 | -46.79945 | 2024-12-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e0690dc-bc37-36fd-a08c-9e3e5316d683 | -3.0037 | -53.23657 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0edfff8a-3550-3330-830b-a909f16e479c | -3.33379 | -53.72416 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffe121d2-1b82-3d99-9c64-158a6bd9fdc2 | -3.09665 | -54.02147 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2dfc8ba8-c5a9-34e4-be03-5e0df5a9d658 | -3.76316 | -50.17418 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3d84f09-02e6-3e08-969f-12a2bb597384 | -2.83405 | -54.09848 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8460f71a-c277-3c70-882b-613fdf7f3e5e | -2.87098 | -53.98428 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8ea7f7d4-d66e-322a-8bee-e2c392f51534 | -3.54169 | -50.1804 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e39b5692-f91b-3c7a-b421-3c5cafe3aefc | -1.65979 | -52.49809 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da65626c-d1ab-3556-b31f-d333d0faa062 | -1.6909 | -55.01369 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5921d2c5-26f5-36d1-a513-7a34a0cfae5e | -6.28861 | -43.85661 | 2024-12-01 05:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d726f422-7939-3522-a119-4294248f0b9c | -2.85381 | -54.09621 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a072130d-daa6-3182-a869-c87fb732c69b | -2.4345 | -54.02257 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29f3a2b6-b9fb-39d4-9799-2b5560a4fb1e | -2.53716 | -54.06153 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e5ed0ca7-926b-3d5f-a845-ce6f4ee683ab | -2.60592 | -53.98595 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50f610f3-c0fa-3a8e-b452-a80ae3910f09 | -1.66292 | -53.21386 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41a3a785-0479-3f21-987f-4aef224343eb | -1.82743 | -54.52764 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a73e5a0-79ab-310a-9e96-73a89ee04a01 | -2.83118 | -54.09411 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6c587e9c-4f73-355b-9ad0-11cbe3eff59d | -2.69445 | -52.91066 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce471fcc-6046-3545-a0c1-56e8d5a0ea26 | -3.42162 | -54.63971 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cfaeef5-fbe7-31f4-9e55-19482cd6b6cc | -1.27011 | -54.55093 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ce2927a-31ce-3bd8-87e9-89619af2d650 | -2.77386 | -55.33925 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebb81b6c-9af1-3698-8124-8994fb03a87b | -3.72424 | -53.91626 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6810937f-c9d5-3009-9f0e-b809c8867073 | -2.88139 | -54.00971 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2cbc9ef-c985-31dd-a1df-c7045c379fc4 | -2.52931 | -53.98615 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d05e6c8f-a400-3583-b0ad-6b49d8f61b8e | -2.75857 | -54.12605 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d47660ce-349e-34d4-90c4-ceb669aa040f | -2.01697 | -53.30476 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dbd739f-7987-3eec-af8c-f3fed88b0147 | -3.10704 | -54.04699 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea752e00-562f-3b11-919c-624f290655f2 | -2.80492 | -53.04493 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1036e197-81e6-3ab3-bd3e-0fba8fec81f8 | -2.84601 | -54.04519 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b207f9c-4a5e-3b7e-9642-222e86a01ae0 | -3.75118 | -52.67411 | 2024-12-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e1855fc-2569-3cf6-a65d-93cbd9dcb23e | -3.27073 | -53.41576 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52107ee2-9cf5-3827-b3fe-12891619cbb3 | -1.42565 | -55.27431 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4b51be1-0a38-321b-8545-93652412053f | -5.53697 | -45.4367 | 2024-12-01 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 995a9002-c5f5-3c85-8989-2f7b6ac6b369 | -2.37487 | -50.39508 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20bfef35-3094-351a-9cc9-8e67c442e7de | -2.63494 | -51.761 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ea475d64-4934-395e-86d3-4bb5f851b096 | -2.96938 | -53.29133 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b22e62e-e19d-3c70-952a-56cd682925ee | -4.33567 | -50.76622 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3ac9f9c-254f-357d-9c29-2361b6669456 | -1.76125 | -55.64632 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fd83f13-f3b1-3697-be9f-8468c9874260 | -2.77611 | -55.3468 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef2369ab-3c97-3d5b-9f19-9e0f44a734df | -1.66164 | -53.22197 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cb31fe3-9850-3b42-bb4e-253cffc57372 | -2.7351 | -54.03645 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b8eb543-71d7-33c2-b6bc-2da0036b65c2 | -3.18025 | -53.25405 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 278d070c-1518-3332-9b3d-4f4a2489e3f8 | -3.29916 | -50.79894 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d871285c-44f3-3fb4-90e3-ab58cf6cecde | -1.4206 | -52.66217 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a0d54452-a39b-3ffc-a4ff-8e26871e8707 | -5.23558 | -56.06116 | 2024-12-01 05:08:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d87cfcc-4831-3168-a651-4369c492a3d2 | -2.8773 | -54.01304 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32a41245-a5df-3416-b929-5939f2004eb6 | -2.66669 | -53.04406 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a925b788-39a8-3930-8ec8-c810ba86eb43 | -3.97633 | -46.75639 | 2024-12-01 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdb006bf-ff2d-379d-8aa6-2531178a56ec | -3.32424 | -50.18617 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8dbed0e4-c677-332a-808b-2b02040eeb0a | -1.99025 | -50.39794 | 2024-12-01 05:08:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2cba77a5-0bf3-335c-a91d-6201b031728f | -1.44532 | -54.37008 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1730c4c2-c7d8-3c18-b8f0-8ed70a2cb470 | -1.4309 | -53.39749 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc7041bf-ca49-3f23-9387-990244a04bbc | -3.4648 | -53.88596 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32ab5e90-3b2d-3a25-894b-0e6b62001f27 | -1.41453 | -55.25834 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27a1677e-a13c-3cef-bd03-77e7d61375cb | -3.06846 | -54.56811 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c766012-40cb-39eb-ac06-377da095c3ba | -2.58728 | -53.99098 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 200e3dc0-1934-3346-b4b6-4903bee57d44 | -3.49645 | -53.82192 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f9a5828-ceb0-3af2-abc4-dfb27de25bea | -3.67647 | -50.17492 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4de1fa24-997f-386c-a022-8d70831e8e42 | -3.21612 | -54.09052 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6664955-b1c5-393c-9ac6-b4fa56a75add | -5.41848 | -45.11427 | 2024-12-01 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16ef221a-e1fd-392a-bf58-839f0578ac0c | -2.87718 | -46.80394 | 2024-12-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38791d71-9800-3607-a7a6-1e680fce7174 | -3.26761 | -50.20546 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 649bb789-abed-3b15-80e0-9a160453d454 | -3.30531 | -53.8643 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2c30ad9a-05bc-390a-8455-e1df081e2220 | -3.22442 | -54.17505 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0d81dfc-8e1b-334c-9e8c-697d32e921ea | -4.03573 | -46.92806 | 2024-12-01 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7d777828-64f9-39b4-a86d-dcfed9236433 | -3.21896 | -54.23296 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b24aff3-3bf6-3f76-9d1f-4b6f1ee93352 | -3.70781 | -51.06765 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f270e51-093d-33ec-bd70-2a2065de0946 | -2.4572 | -53.70959 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7c49ba3-5e3b-3134-8378-264e163bc1b6 | -2.79736 | -54.12813 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b525351-3f32-343d-b919-1a714fa5162c | -3.0685 | -50.3306 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15c58e6f-9bb0-3225-9207-e81cd7f9cdfb | -2.73858 | -54.03701 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f74c1924-9013-3268-8f46-596bb671fef0 | -2.22412 | -53.62654 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9dc43096-b1c2-3d4e-976e-5baeed387ee2 | -3.45568 | -54.32536 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff6b9300-6446-3f56-9b99-7be573d45b73 | -2.96701 | -53.94318 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d157ef1b-7ed5-36d9-9d86-e8459f8c9635 | -4.55183 | -45.71428 | 2024-12-01 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a62c6e6-60de-3c50-9a9e-0ce4eab96750 | -3.02987 | -54.18952 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a01b27bc-0095-3553-83e4-460ce1b04292 | -2.46877 | -53.70575 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc8c9072-8b3f-3e6f-8439-a013d068d9da | -3.13279 | -59.15789 | 2024-12-01 05:08:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22bfccb7-6ffe-320f-8b56-163838eb74d1 | -2.86808 | -53.97987 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fada5897-0d94-33a8-bb42-40eabc8a943c | -1.62174 | -53.86854 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71b5110d-6945-306b-b501-cb64512c2e52 | -3.29614 | -53.83042 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bbf0f08-b6a0-3795-b251-7756aa8138f1 | -3.07081 | -53.8134 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be294f98-c205-3640-bda5-efada3cb7c8a | -4.54501 | -43.30818 | 2024-12-01 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e7c1dd0a-a0e3-3f01-b868-860559b509e4 | -2.29688 | -60.26587 | 2024-12-01 05:08:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README78.md)
