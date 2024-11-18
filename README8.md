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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 858e98d0-e07c-3e01-9731-553a77a9b366 | -2.5808 | -48.306099 | 2024-11-18 00:49:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6eb1652c-1756-3c2c-a059-6ea0df86135b | -0.9423 | -51.729801 | 2024-11-18 00:49:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2b23e6bb-1ecd-34af-83b0-127fd79701a2 | -1.358 | -54.152901 | 2024-11-18 00:49:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44713dfd-af36-3b7b-98fd-9f8bdeb12247 | -1.7242 | -53.267799 | 2024-11-18 00:49:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae3b0032-4d74-3ed6-96e2-07c6592a1773 | -1.0874 | -51.7346 | 2024-11-18 00:49:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 935823cd-2a16-3879-8528-6ce3e5c9b642 | -3.0659 | -53.276501 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2125bf4e-31dc-3cb6-8b94-e377e93da28e | -3.0518 | -54.396198 | 2024-11-18 00:49:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 222b3724-e966-386c-a6b3-9a80a30c03b0 | -3.302 | -45.713699 | 2024-11-18 00:49:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa8b6821-419a-3a6c-b634-a54e63514944 | -1.6295 | -53.304401 | 2024-11-18 00:49:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20d9e998-5587-3a8d-b2ed-5e0219ee20eb | -3.3668 | -53.330799 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 972f5765-d04c-37d1-b84b-2c73f2bc0b1d | -3.5695 | -53.2701 | 2024-11-18 00:49:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 780d6896-27af-363e-be64-2f5171f78e4e | -2.6216 | -48.569199 | 2024-11-18 00:49:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d43ac9a-8a8d-3046-9d74-9231a55c6557 | -2.6591 | -51.719002 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7fc1691-fa28-3e46-bab6-4b13e267ca45 | -3.1819 | -53.242802 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee1a86f1-1a0d-3d61-af09-a69eccc4c92b | -1.3251 | -51.874599 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3d1b212-2792-33da-b460-10961923e407 | -3.1579 | -46.615101 | 2024-11-18 00:49:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b305ccf1-4567-3145-aaff-12ea15ee0c33 | -1.6896 | -45.849098 | 2024-11-18 00:49:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ad32955-237e-3f3e-a648-bf52c3653377 | -3.5814 | -53.730999 | 2024-11-18 00:49:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea50d3ac-5e95-3800-abb2-3a7234dc042a | -3.303 | -53.367699 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2383044b-062f-34ff-86a1-5734caf3722a | -3.0796 | -54.6562 | 2024-11-18 00:49:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 164a570f-1ccb-3c63-9a46-6cdc88511f58 | -3.0642 | -53.269199 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa19dc95-f0c3-34ee-896f-9546350fe7ba | -3.4027 | -53.307499 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57187564-a062-31d3-a583-6f81ece20fd7 | -3.1332 | -52.983601 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bbc9554-4c1e-38cc-a91c-af642f67f551 | -0.3826 | -51.530201 | 2024-11-18 00:49:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6602f029-5f4c-3e04-b50e-d376227117bd | -1.7574 | -50.748199 | 2024-11-18 00:49:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b741de39-8bc4-3715-bfcc-f2751ff1b8ee | -4.5445 | -48.531601 | 2024-11-18 00:49:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98e88234-a724-3a61-aac7-9e97b01fa04f | -3.3325 | -53.315701 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2d76112-df4a-37ec-9c3d-56031963ceb1 | -3.0616 | -54.394001 | 2024-11-18 00:49:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa48af25-397f-346f-8f44-e61885d05bd0 | -3.4274 | -50.804501 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f74a09dd-5ed7-3554-9df2-79dc1374ac4f | -2.965 | -49.1185 | 2024-11-18 00:49:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1716c781-aae6-39e3-b9cd-2038e1e7ed2c | -1.7138 | -46.214001 | 2024-11-18 00:49:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59bede4b-9eae-3517-a101-e297bae1ac18 | -5.9371 | -48.069199 | 2024-11-18 00:49:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de6deef6-c414-3fe7-9958-d397b0ce91dc | -5.2464 | -44.077301 | 2024-11-18 00:49:00 | METOP-B | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| daf57bde-6035-306f-8e15-f28bc90aa396 | -2.5905 | -48.303799 | 2024-11-18 00:49:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7acae4d1-c3dc-335a-ba80-12ae033b7716 | -2.567 | -51.721699 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76c533f5-fe91-30f1-9d2e-e7ff14155d73 | -3.5117 | -50.233799 | 2024-11-18 00:49:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1daf47a7-c441-3548-8e46-4ffa46501aa5 | -12.5771 | -57.758701 | 2024-11-18 00:49:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5bccc72-6fc0-3b0c-9eb6-57d441c026f4 | -3.379 | -50.327599 | 2024-11-18 00:49:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f525158b-860a-31de-a76b-e7321c75ff17 | -2.7623 | -52.621899 | 2024-11-18 00:49:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 872f96c2-b44d-3aff-85b9-c46f50932c6b | -3.6187 | -52.265499 | 2024-11-18 00:49:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f7bdb21-8efc-326b-98c6-020596d54382 | 1.6274 | -55.992599 | 2024-11-18 00:49:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a5ac608-f5ec-3845-a814-39699e4a8b56 | -2.6473 | -51.7127 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7fc0b88-1624-3734-88fe-70e86eac8367 | -2.9552 | -49.209202 | 2024-11-18 00:49:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0ef8641-cb3a-31e7-8c7e-caf969e86a23 | -2.6239 | -54.281399 | 2024-11-18 00:49:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fe35e20-93e2-3c37-bfa5-ff6486d1195c | -1.3231 | -51.865898 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 813f8ee3-f420-3df1-9672-62832b85107d | -3.7635 | -50.165501 | 2024-11-18 00:49:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d193e3ed-4a4c-3dd7-84ce-d5c30bcf322c | -2.6788 | -52.4361 | 2024-11-18 00:49:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08ad6cf7-751e-3367-bd10-e9ae823bb6d8 | -4.274 | -50.591099 | 2024-11-18 00:49:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24079225-1cac-3e35-b06a-8d4cf10eb8b7 | -2.3416 | -54.583 | 2024-11-18 00:49:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2230c5d8-6e5d-3537-a285-bd9d2e75c5a8 | -3.5455 | -54.5742 | 2024-11-18 00:49:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcd8b601-c7b0-37da-a9b1-9f2772fc6c1d | 1.6477 | -56.040001 | 2024-11-18 00:49:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5db6ec2c-6ec3-31e5-94c8-3c10c9b80514 | -2.6822 | -45.728699 | 2024-11-18 00:49:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 56b3b230-fe39-3c79-9b2d-42b338705a6d | -2.6094 | -54.262901 | 2024-11-18 00:49:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 031711e8-6457-31a8-941d-9fce3383c3ad | -3.3652 | -53.323601 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cefe5c50-9199-3efd-aabd-88ac47f41a92 | -3.5676 | -50.2528 | 2024-11-18 00:49:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 294519b7-8b4a-3295-847e-fd0488e9a870 | -2.1946 | -53.660801 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 232db2bb-c5f7-3890-80fe-801812baa9ca | -4.2642 | -50.681702 | 2024-11-18 00:49:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9c67813-9f62-3e9f-8a4b-200430fac02c | -3.3916 | -50.292999 | 2024-11-18 00:49:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9108def7-1c5e-3d39-bd6e-d5e9da546d2c | -3.0675 | -53.283699 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03d9fdc2-b15c-360f-b61c-6443532af650 | -3.7604 | -45.9627 | 2024-11-18 00:49:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c42a6e64-aff6-3644-ade9-b58538837322 | -3.0577 | -53.2859 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be81d3f2-6785-3d3d-89f9-cec25215589f | -3.098 | -53.100201 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 226d110e-1153-3af3-a93c-53694f707ecc | -3.045 | -54.412102 | 2024-11-18 00:49:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81c75e19-2133-3748-bf59-0be15aea89d2 | -2.363 | -53.6758 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67059eb7-ace6-3232-9d1d-0170dc8a0bb3 | -2.6362 | -53.9716 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02f31114-13e6-35f6-b1ce-39ed5d0fa540 | -2.8996 | -53.0438 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b5190b9-b7e6-3416-bc65-b0d98997ec09 | -2.5923 | -51.787498 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aed2c877-9986-3f4d-b4aa-07504516e66f | -14.2854 | -57.6339 | 2024-11-18 00:49:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b790101c-2dc5-3c11-8118-264a6638a09d | -2.1962 | -53.6679 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05128acc-ff02-30b1-a56f-beb021d27094 | -11.8275 | -47.096699 | 2024-11-18 00:49:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ad22144-0dd1-3694-ad80-dc3f1739bcf0 | -2.2339 | -53.6068 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f912233-a19f-39bd-a856-b29169f519a0 | -2.3318 | -49.135101 | 2024-11-18 00:49:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27e43f5d-46e0-3e1a-b298-49b99293fb84 | -3.3047 | -53.374901 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeae6830-92ad-33d6-83e7-625d78c1f8c8 | -3.3813 | -50.337502 | 2024-11-18 00:49:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d8ae0a5-ee2e-3098-b012-7a06a58941f3 | -2.9747 | -49.116299 | 2024-11-18 00:49:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c94ddd4e-ba33-3b9f-895a-2be0866e837e | -2.9678 | -49.130501 | 2024-11-18 00:49:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3b5eb80-bacc-3e7f-ab58-0b244fea53ec | -1.6846 | -45.827702 | 2024-11-18 00:49:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 95b44050-52b7-3ca6-ab0c-b699dfd8aa8c | 1.6462 | -56.046799 | 2024-11-18 00:49:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8110479-6cf7-38ff-aac0-aea99b39c8e9 | -1.6278 | -53.297001 | 2024-11-18 00:49:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c89d7ed-ea4d-37f2-afed-7924f0894268 | -3.3309 | -53.308498 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15e26f71-142a-3024-9738-8b0ed92ca633 | -2.7606 | -52.614201 | 2024-11-18 00:49:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41ad20ab-5d0f-324e-b442-3757164ee801 | -3.4011 | -53.300301 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65e0108f-6e27-3805-8d11-89acb54bd75a | -1.6232 | -55.144199 | 2024-11-18 00:49:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a84db1a8-a528-33f7-9868-6268cc826a46 | -0.1518 | -51.6012 | 2024-11-18 00:49:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3d49353c-8d6d-3b66-9ff9-89259c65f8d6 | -2.8586 | -51.780701 | 2024-11-18 00:49:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4c691ce-697d-3944-a28d-23ffc5c40173 | 0.6215 | -51.773201 | 2024-11-18 00:49:00 | METOP-B | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 41c0e14b-aa68-3fa4-acd4-c56fc2e95bce | -3.2972 | -45.6931 | 2024-11-18 00:49:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 661ca9b9-afc5-3b40-bc5b-ef5c1aace7b0 | -3.3325 | -53.361099 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c8122a1-707c-38b6-bf2e-7594233f0df7 | -3.143 | -52.9814 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 799cea59-0909-3a29-ae39-c05a0863163d | -3.0549 | -54.41 | 2024-11-18 00:49:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63aef9d7-c5ba-35f0-89a9-0e992708389a | -1.6993 | -45.846901 | 2024-11-18 00:49:00 | METOP-B | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| db8b6f02-590f-3cc0-89a1-23a34d663cb8 | -1.7091 | -46.193901 | 2024-11-18 00:49:00 | METOP-B | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1508d240-cd87-32f7-ae5e-05fb6f8f4736 | -1.2835 | -51.737099 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d382462-156f-306f-9554-5953a704c042 | -1.1401 | -51.694901 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 103a5755-cf45-3eaf-ade2-315dfca070b5 | -3.3945 | -53.2714 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a054588-2b0a-387c-8571-f2915924fc01 | -1.1994 | -51.774502 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7902e433-f6b9-3700-85db-c6b2f43a84e0 | -1.432 | -53.387501 | 2024-11-18 00:49:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f5c6b9f-f790-3ba8-8bfd-00b29202e696 | -1.6174 | -52.6161 | 2024-11-18 00:49:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 253bca5f-67a2-3baf-bde4-d6fa3039470d | -1.6334 | -52.595901 | 2024-11-18 00:49:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d89d9200-2443-3f43-8318-1d318d18a5c4 | -3.1414 | -52.973999 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
