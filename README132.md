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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 035fc858-f8d8-3a7f-8fb3-226a2b19e8f2 | -11.0863 | -45.6688 | 2026-10-07 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 7c264eb5-b3f1-369b-b6dd-1ea0d8330a16 | -11.1556 | -46.0916 | 2026-10-07 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 195.0 |
| a3d619b3-501f-39eb-bb0b-bdbcea4f71cb | -1.2086 | -49.0412 | 2026-10-07 14:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 4e38e621-38cc-34fd-b3fc-ae2f44b1b95e | -6.9143 | -43.6583 | 2026-10-07 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 81286124-4e58-3f65-a72a-f5861381a429 | -6.9925 | -45.1223 | 2026-10-07 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 0e058491-8690-325d-b8c3-0834f0b0c97b | 1.6385 | -55.8047 | 2026-10-07 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| fdf2d123-d330-35fe-94c1-e21ead1ea510 | -9.1362 | -65.3022 | 2026-10-07 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| d02b0427-6309-3cef-8d06-6d6e5e5c6713 | -6.4413 | -55.0224 | 2026-10-07 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 354c8604-6424-3051-b92b-09c3220836e6 | -11.7335 | -43.649 | 2026-10-07 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| f068fa47-3747-309f-9b04-a14d723006ee | -9.9589 | -43.5516 | 2026-10-07 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 6ffb2366-86c8-3fc5-9483-84e62c6ed672 | -7.2027 | -46.5209 | 2026-10-07 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| a878f9c4-343b-3b2d-bbcd-2603e5e6c1ad | -11.3742 | -46.7173 | 2026-10-07 14:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 222.2 |
| 10b3132f-de38-30bc-83a4-61385d9e95f7 | -7.89 | -54.7206 | 2026-10-07 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 82b9f6aa-1c0d-3709-bf4f-2e238a746e79 | -11.7947 | -46.683 | 2026-10-07 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 4b9db74c-3ec3-3fc2-b93e-64e06bed924c | -11.1054 | -45.6662 | 2026-10-07 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| a7c1ab95-c9db-3ce5-b672-a8214d51d77d | -11.0867 | -45.6459 | 2026-10-07 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 4a95311f-1380-3786-9ea5-9fd3d3a0021b | -11.1988 | -49.4297 | 2026-10-07 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| d9da8770-c771-3f93-9744-f95fbdf5bd12 | 2.1267 | -50.8371 | 2026-10-07 14:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 69.5 |
| c195f5f1-10c6-32f9-93db-5a589c97d3fb | -7.7399 | -45.4627 | 2026-10-07 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 2905bf07-37b3-31af-8633-8c5f02d96c08 | -7.7595 | -43.8092 | 2026-10-07 14:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 159.2 |
| ae1cb1f1-fe69-3b23-9fb0-e257a7f38ea6 | -11.3937 | -46.6922 | 2026-10-07 14:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 7f3aa9b2-9dc2-387a-a66f-bdac832568eb | -10.8591 | -50.6692 | 2026-10-07 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| e72eaeec-1e34-3ff3-ad4f-9feb53274cdf | -9.1363 | -65.2835 | 2026-10-07 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 046af66e-e173-349c-86b0-f54419e8e37d | -8.8365 | -62.4131 | 2026-10-07 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 32f82ec8-3323-30ba-b8ea-80a6b0efd087 | -10.6199 | -60.4852 | 2026-10-07 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| fe6a134c-e7c0-3f6a-8642-6404f2c87d83 | -8.6033 | -45.6709 | 2026-10-07 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |
| b6abac3b-8e09-3578-b29b-7b2703a2dff5 | -12.1746 | -44.7051 | 2026-10-07 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| fa6b56da-4289-3b55-9765-8cef714124f5 | -11.7143 | -43.652 | 2026-10-07 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| b2ac7933-7e3b-3210-9474-a8233808bf24 | -7.2179 | -55.1817 | 2026-10-07 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 2d89950f-c0e8-3c9c-93a6-39e36b1dd2cb | -12.1554 | -44.708 | 2026-10-07 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| da597dcd-a7e5-34cd-9799-b1bdd8eaba3a | -11.065 | -45.8084 | 2026-10-07 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 4f0f1749-eb82-3854-ae11-243bd75970f7 | -10.5097 | -47.2733 | 2026-10-07 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| c7fd725d-e0be-34af-aa1a-728ba220335f | -11.1047 | -45.7119 | 2026-10-07 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 16f33471-5392-3851-b48a-cc7a3af40b80 | -5.76 | -45.14 | 2026-10-07 14:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5203e9a0-f9a0-3661-9b0d-22022543a0a7 | -6.22 | -52.82 | 2026-10-07 14:15:00 | MSG-03 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff134eef-547c-348b-9034-f430da2f17c7 | -5.73 | -45.18 | 2026-10-07 14:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f07eeaa8-9f7e-3de5-828a-028576e883c9 | -5.76 | -45.19 | 2026-10-07 14:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42319b7a-e755-3c0c-8792-36fd1442c895 | -5.99 | -40.93 | 2026-10-07 14:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 757863a4-a52a-3527-80bc-d19d593cdbe2 | -5.73 | -45.14 | 2026-10-07 14:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80fb8cb6-6b4a-393f-ad7d-d3439dcd0e47 | -3.29 | -54.01 | 2026-10-07 14:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8eb4524d-999b-3699-8e45-60caff30e4b0 | -6.6753 | -44.9674 | 2026-10-07 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 190.2 |
| 131272de-bcd1-32b5-b68d-0cda26b6c331 | -10.5287 | -47.2711 | 2026-10-07 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d4f7436a-337c-3604-b236-1674eadc950f | -6.2159 | -52.8285 | 2026-10-07 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 290.3 |
| 29287e34-044a-37c7-96bb-b35df4b9c071 | -9.4492 | -44.6167 | 2026-10-07 14:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 8ca64814-2922-3ac2-ae8b-16228b6b351c | -1.2086 | -49.0412 | 2026-10-07 14:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| ef3dda31-8539-35cb-acc9-76219bd4c0dc | -6.8832 | -55.3397 | 2026-10-07 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 12e1607a-2af3-3d57-8409-1f45f0567f8c | -11.7751 | -46.7082 | 2026-10-07 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 2c7a0c8b-db88-3a02-86a6-945b4fabe301 | -11.8315 | -43.5391 | 2026-10-07 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 775e8677-7164-3c8c-a58d-8a7d7b344aa5 | 1.6385 | -55.785 | 2026-10-07 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 207d69b6-e6cf-3077-9193-26e6fc0b47d4 | -10.6199 | -60.4852 | 2026-10-07 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 9fca4d62-d4d1-3d49-913b-ff3c240d29a0 | -7.3935 | -46.2144 | 2026-10-07 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 5a0b8faa-af84-3648-b9d9-79a6b39ef45e | -11.7143 | -43.652 | 2026-10-07 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 77387cc5-9b6a-39f8-90cf-43993c84fe35 | -11.1556 | -46.0916 | 2026-10-07 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 327.8 |
| 25353f75-d0e6-39ea-8c40-fe38f049c7c7 | -7.8789 | -72.3674 | 2026-10-07 14:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 75.3 |
| da1cbcf3-ef1a-387e-981f-2f00f0f431a5 | -6.1973 | -52.85 | 2026-10-07 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8236169e-2b04-3239-9bb5-7f90bf76ffd0 | -9.343 | -45.431 | 2026-10-07 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 116cbd76-66fe-3228-bd85-9ef84df666e9 | -11.8216 | -47.3521 | 2026-10-07 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 4dedee23-73c8-3b4f-9e37-42d327ff03b9 | 0.7266 | -51.3749 | 2026-10-07 14:20:00 | GOES-19 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 94.0 |
| cf63d355-0d7a-31a8-9adc-3fdf17dbacb3 | -11.7755 | -46.6856 | 2026-10-07 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| c787f589-6e44-38cc-949c-1007973c756b | 1.6385 | -55.8047 | 2026-10-07 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| e99ab2c6-fea1-3bde-8439-6720f7b8af67 | 1.5283 | -56.0227 | 2026-10-07 14:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 518a30c8-3821-3fc7-82af-134e1ebbec0e | -3.1969 | -42.6019 | 2026-10-07 14:20:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 25dfda63-8eea-3d4b-bfb0-aae567752781 | -6.914 | -43.6816 | 2026-10-07 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 207.0 |
| 7b8a5b8e-e663-3f16-a3ae-91cb248ac726 | -11.0863 | -45.6688 | 2026-10-07 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 25fe7a41-1a38-314f-af4a-6854222e1374 | -7.8679 | -44.1922 | 2026-10-07 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 410f7dc1-e631-3c78-825b-cd65fdf46a4a | -11.7947 | -46.683 | 2026-10-07 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 40e36cd6-acf9-34e2-ba44-941a6c81f1dc | -6.9925 | -45.1223 | 2026-10-07 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 132.9 |
| af369432-8bde-3261-b33f-c89c2ef7ddfa | -7.8676 | -44.2153 | 2026-10-07 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 126.1 |
| f21bbe5d-58a3-37ea-89fc-608c41af292b | -7.7579 | -54.9499 | 2026-10-07 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| e4e13198-3b93-3745-b58f-2d56ef1caa5c | -7.7592 | -43.8325 | 2026-10-07 14:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| a90bcf52-0569-3ff7-bb29-3f1fc4c5a8d7 | -17.5269 | -45.4622 | 2026-10-07 14:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 172.4 |
| ced72da2-9804-38e1-b2f1-7a253177589f | 3.1463 | -60.5937 | 2026-10-07 14:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 818a3b8f-96d7-345e-8562-a1e6f908c9fe | -8.8278 | -45.8054 | 2026-10-07 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 93658ca9-d38e-355b-a170-999c9508ece5 | -8.5844 | -45.6729 | 2026-10-07 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 129.9 |
| ffe6f1f3-7654-3662-8f93-2346656a931e | -7.2027 | -46.5209 | 2026-10-07 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 9ed085bd-be98-3d22-879f-c554bd9baae8 | -10.4594 | -46.8333 | 2026-10-07 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 66f94810-d71b-36e4-9982-8054c8c08b4f | -10.9949 | -45.4298 | 2026-10-07 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 206.7 |
| e5c03da6-8637-3601-9993-dbeaf9fc8db2 | -6.4756 | -52.8142 | 2026-10-07 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ccf35852-0aaf-3ccf-96e0-00f58944f86b | -6.9143 | -43.6583 | 2026-10-07 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 183.4 |
| b54bcb1e-3ba8-325f-837d-9f7b4534e7d9 | -7.5284 | -45.8885 | 2026-10-07 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 9337c9e2-09a0-3b3f-a6b1-d24f02ba8491 | -1.2455 | -49.062 | 2026-10-07 14:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| e85c0345-baf0-333f-9b1a-4c5b7ac3beb7 | -4.1178 | -41.7963 | 2026-10-07 14:20:00 | GOES-19 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 120.7 |
| 068823ad-c814-31ff-bbf0-eb2aa572f02d | -11.3937 | -46.6922 | 2026-10-07 14:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 8d96d5ef-7e30-320c-9252-a5a6cd276406 | -6.1974 | -52.8295 | 2026-10-07 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 85735c46-c6a3-30d0-9828-fdc1ea5e5a4e | -11.1051 | -45.689 | 2026-10-07 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 44fb4977-8e88-37c1-a6d7-69e9a1fbb018 | -7.2179 | -55.1817 | 2026-10-07 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c0427907-1e26-36fa-a0fc-59c0adee63b2 | -11.0867 | -45.6459 | 2026-10-07 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| ef018e53-4658-3f41-9525-2a8af82b2db1 | -11.1047 | -45.7119 | 2026-10-07 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 95d0aa41-42bc-3312-a8d0-4116148eed7c | -11.2295 | -46.2403 | 2026-10-07 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 199.3 |
| 9c4a2ba5-d0cc-3a37-8405-af538631ba42 | -6.6943 | -44.9431 | 2026-10-07 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 289.7 |
| b7672fff-65de-3af4-a6f8-0abd35dca452 | -7.7213 | -45.4418 | 2026-10-07 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| e953222d-b067-332e-a6e2-cd37cdf12b71 | -11.7335 | -43.649 | 2026-10-07 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| f4a890f1-22cd-3313-afdc-38a3127880a4 | -9.1363 | -65.2835 | 2026-10-07 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| e99d22c9-f602-3dd6-b6c7-dfa92f503f05 | -7.8146 | -45.5009 | 2026-10-07 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| ff481604-59e1-3b0a-9a1a-dfaab3ce1b6b | -10.5097 | -47.2733 | 2026-10-07 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 972d4bf4-dbcf-34df-b21e-54c1e52592dd | -7.2 | -55.1026 | 2026-10-07 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 9c131acd-540a-3b07-9be6-1debb0e51441 | -7.2884 | -47.2885 | 2026-10-07 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| a73b8976-95d0-323e-bfc2-8d7eecbf3ac0 | -6.2161 | -52.808 | 2026-10-07 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| abf852c6-9c40-3a5f-ad5e-3e29cc075985 | -9.1362 | -65.3022 | 2026-10-07 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| a6efde6c-7972-3830-81e5-83bc59151927 | -10.9953 | -45.4068 | 2026-10-07 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |


[Clique aqui para ver as próximas entradas](README133.md)
