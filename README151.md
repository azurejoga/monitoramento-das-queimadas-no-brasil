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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ff5f834-3cb2-33ef-802a-d490b86142a4 | -2.97548 | -54.048 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39303c45-1214-3284-9d33-3cd24b074f02 | -3.1136 | -53.79321 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 120d0abb-72e4-34e1-9fb2-b28883211025 | -6.15111 | -47.91582 | 2026-10-09 05:04:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae6c787d-0cfa-3d88-b5fb-08801fbdff3f | -10.24677 | -49.67943 | 2026-10-09 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c03260a1-8986-370b-b579-c5f5392a1b48 | -8.55282 | -46.9082 | 2026-10-09 05:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bad93dc1-85dc-342f-a812-49c095e04e4e | -9.25552 | -60.87735 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb6c2627-9afc-3431-a6f0-7dd3cfbfd806 | -4.29803 | -50.7846 | 2026-10-09 05:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ff61134-21a0-323c-a78e-bfe54547e30e | -3.32449 | -61.26522 | 2026-10-09 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f7b0515-b25b-31cb-9a15-11da6465136c | -3.90245 | -58.95103 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 399e12e4-ef9e-3c06-8291-ceb986669efe | -6.38179 | -56.22624 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75d49834-6b5f-36be-9e40-7437ee49f23b | -3.91013 | -55.89436 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed7870f7-5ac0-3209-9f74-765f8c62bc03 | -6.64041 | -62.90778 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc64f1df-0194-3c7e-aeed-c9b9d53c89fb | -3.59683 | -61.61525 | 2026-10-09 05:04:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db914775-b998-3b89-bfcc-f8dd71f312d6 | -3.06163 | -53.93954 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe777975-d106-3603-b77b-1a10ceff92f8 | -6.50513 | -55.39251 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7db0190f-aaf1-3273-a726-6df3bd36b39a | -3.74613 | -60.59603 | 2026-10-09 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed0a024e-0155-3aa9-a15e-449b68151939 | -3.40053 | -59.20579 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de99a22a-f278-31c5-bd24-e6efb4ffafc1 | -6.31678 | -54.80462 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a943788e-0fc5-3304-8379-0c1d8a73ba9b | -4.50361 | -43.62173 | 2026-10-09 05:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb6c5c86-03a4-3e41-816b-a74b938ccd29 | -4.06194 | -59.83775 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 596fc177-9c16-3ec3-920c-cfe1a0b3cfb1 | -3.20849 | -58.84864 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af91a773-7ca0-3f23-a1f2-13d9c6586671 | -4.08314 | -48.95691 | 2026-10-09 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f89cc8c-e495-3733-b0ea-a0199dd546f3 | -7.12957 | -41.80814 | 2026-10-09 05:04:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| aa324fde-561f-37a9-9b9d-5c904911da57 | -6.12761 | -53.05573 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bf9ded46-624b-39ea-b5d9-eb2c64ba86ec | -3.26695 | -54.05273 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e8b030a-10a1-3b8c-bf43-0984fbd76086 | -3.01236 | -54.04511 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 706b2615-5683-35cd-9221-892ca9d42bff | -3.08185 | -53.94673 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bb7f8be-0139-3d0a-a9c1-e96302b8b738 | -5.99918 | -40.96743 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 18b7a0c2-af92-3af9-9486-4548482cf712 | -2.99457 | -53.90637 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5998452c-851b-300f-af0e-1ae062a74c08 | -6.96791 | -45.25172 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 723a6185-1a10-3464-b618-e66ab6c6cd88 | -8.1741 | -54.72292 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3a742f0-b8aa-3068-8407-e4e13220cfc3 | -6.26037 | -52.85846 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c06e6e4-0cbb-308c-8a21-c3faa7d8229d | -3.09166 | -53.95218 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19feb5c5-ef5e-3b6f-8073-7f6f0d1041af | -3.92305 | -55.76804 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad5b6a09-86d0-3914-984d-bc45f9b9d36a | -3.06363 | -54.17177 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9dfe31f4-aa4b-3e3b-83dd-9faca9c4e8a5 | -11.2511 | -46.30273 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 386b8105-9d17-39bf-9b31-a70fb72d06db | -3.5895 | -54.66675 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fedcc9d9-9937-36ad-a393-aea92cc70dd9 | -3.90087 | -58.96058 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc9650ab-03a0-3fee-96e1-8a2ba7a9efb4 | -6.93815 | -43.66143 | 2026-10-09 05:04:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e19becc5-b103-3426-9be9-5001374682ec | -3.25468 | -54.66234 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26c8949f-c7ce-3522-98a9-dacdd8c3721d | -8.24686 | -54.7267 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d17ee4d-8cd3-3268-a24a-6661b8c727f7 | -2.88491 | -54.18426 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c45f102a-2c0d-34c3-b3cc-b97d24c8e2ca | -3.0131 | -54.08458 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24c0e551-3696-37a5-9ab2-5d4e27f9af56 | -2.92401 | -54.12268 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e04299e-ff31-3256-89cd-d178f8b12d7a | -8.23353 | -54.74362 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7761fe16-1fe4-3256-9066-b283fec8a6bf | -11.06088 | -44.06481 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62bdba1e-ce6c-335f-9d83-be2d64c40f01 | -9.01758 | -44.38198 | 2026-10-09 05:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5275181d-3d60-33fe-af3b-1f039cbd99fe | -4.61719 | -49.2123 | 2026-10-09 05:04:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ea27cd66-9b68-3afa-9b78-10b185ff674f | -8.97119 | -47.53507 | 2026-10-09 05:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2c8c692-6ba1-3a3d-a693-bed8d80d2493 | -5.09284 | -46.20658 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a467522-4539-3145-89d1-fc010ba6cde3 | -4.74725 | -55.66457 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b1f1038-f05e-3de6-b925-30244adb99a5 | -6.84408 | -59.39759 | 2026-10-09 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ffb5c977-79c2-3ac1-9f46-1ae83d157eab | -11.0573 | -44.05421 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c188261c-23c2-322b-a6bb-2e3a8afabed6 | -8.27696 | -45.73664 | 2026-10-09 05:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e551d152-e5b3-36b9-81f4-47603ed06a36 | -3.08036 | -54.27019 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f6d4057-5eec-3b05-8468-ca20c80936da | -8.16737 | -48.60406 | 2026-10-09 05:04:00 | NPP-375D | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 84059e6c-d482-32d4-a03e-cdb71f3e5896 | -2.90203 | -57.21623 | 2026-10-09 05:04:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10a0d0be-a84c-3608-922a-724687a204be | -11.18019 | -45.30438 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 68b9aae3-22c6-3ff0-9fc6-4dbb5bcd3af7 | -3.71112 | -59.65058 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb6b46d9-c725-3fea-bdc3-6dd4c658322d | -5.69241 | -53.45575 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61dd34f7-8137-3f01-b540-79ad921efcc4 | -3.00709 | -54.09943 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df0f2a96-d3f0-3315-86f4-e6d97738a3ab | -3.12335 | -53.79862 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80fcc723-d2ff-35f6-b0ad-1b272de1c428 | -6.41549 | -55.19276 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb5504d8-9bc1-3d0c-8659-3106179b4a44 | -6.48786 | -62.86189 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d85fd5d-2cab-3f9a-b5d6-33495f352fd4 | -6.48921 | -55.29934 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7202a7df-9589-327b-8656-caf1cc7359f1 | -6.25592 | -52.86489 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc09e12e-b7b8-3351-9036-4088c5d1388a | -6.13039 | -53.05976 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0d73282c-6cfe-3089-b76b-799d28c22b50 | -4.2916 | -48.60034 | 2026-10-09 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdc4b9cd-d450-3189-ab51-1448e33f2e59 | -3.17931 | -60.39682 | 2026-10-09 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 690df0f8-f02c-3799-83bb-ac6553bcdca8 | -3.00214 | -54.76306 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b0aa45c-b7e3-38b7-b19c-0d4a150aa691 | -3.22304 | -53.96461 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72dbce4b-bad6-3bef-92bc-0401b7b614b6 | -3.08636 | -53.96299 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18cfec82-6b0e-3ac3-8d09-3d735c94ed5b | -3.0049 | -54.08814 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20422421-5d0f-3e63-b6a9-0a834fddff17 | -8.84056 | -61.46795 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c69dc1be-0e35-36dc-a7b9-9188a8e9172b | -6.8804 | -45.9051 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ad28e09e-22f5-30e6-a7d5-26965209b02b | -11.25224 | -45.25031 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c6208d9-4872-31fe-9bd6-13bc3c9f31a6 | -8.7071 | -62.41359 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c1c83ce-04b5-30ff-bb19-622f59a522de | -2.50137 | -58.0785 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3c62962-b841-3c3f-9b21-f198766f79ae | -11.1159 | -47.78895 | 2026-10-09 05:04:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ff6dbe7-5466-3406-b7a3-14c96ccb6184 | -5.70136 | -53.46448 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c19b4b98-d326-37c8-9a2e-53499aa09bbb | -8.41161 | -49.54509 | 2026-10-09 05:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a3642a9-a265-3db3-9603-e4d0978b38f4 | -3.77952 | -59.1954 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0881fdbf-d0af-3e05-9379-d3fbfb1b2578 | -3.22411 | -54.29545 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f9d4b880-ac9f-3e1b-b48f-698b0f02d355 | -12.0274 | -43.47228 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf76dd2c-dc31-3363-bd6d-926c2fb964af | -3.09935 | -53.77175 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6d64ac2-1c18-3c65-9f6a-a59c0bdc227a | -8.97167 | -45.90762 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b96daa1-5db5-3da4-b77c-47a28b5f2554 | -3.26453 | -54.00154 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8503b2bb-d62e-3f8b-b587-dd5e175f61b8 | -3.46996 | -59.25899 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f980790-f29c-384d-99c1-83225252e0b6 | -11.64987 | -43.67707 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a9de5b2-acbe-31fb-ba9d-7ab644ae961f | -5.96929 | -55.33834 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65a5fd11-76cf-33f0-8266-0e5afefecd95 | -3.00996 | -54.10384 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 561567ab-3f48-3cfd-8be2-418b141ced08 | -3.45727 | -50.58244 | 2026-10-09 05:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 176dbbc6-46d5-32c8-b93c-1ce471e182a2 | -3.02782 | -54.23774 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27467cdd-5afd-38b8-971b-a9c8313d9c9a | -10.75182 | -46.58969 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 68d7cb90-4587-3562-9db1-3744006466e6 | -3.15475 | -57.67885 | 2026-10-09 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac3ca91d-63b6-3c90-a130-210d019bdbaf | -2.94418 | -54.15371 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 568c8070-ea98-39e4-b2ec-486de305ea87 | -6.11741 | -55.70597 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dc81cc46-fd67-3639-b3b3-fb5d3a5f64e3 | -3.07933 | -54.25396 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fba613b-f229-323f-b5a3-f62341ad1ca1 | -3.20383 | -58.84791 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac940e40-c5e0-3524-9fbb-774c6fd4e2cc | -4.08548 | -48.96567 | 2026-10-09 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README152.md)
