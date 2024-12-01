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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4ccf982-fa4c-3224-ad04-980f86b03bd9 | -3.26069 | -48.76367 | 2024-12-01 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 555f91a1-1119-3e89-888d-3f94ded92dd5 | -1.75575 | -55.41645 | 2024-12-01 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72325a01-9aa2-3bb2-82d9-00ceb2515520 | -3.1221 | -53.27439 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41e15ee2-8021-3c68-841f-84219f4f4022 | -3.39388 | -50.31239 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43cd4d0d-688b-321d-97ce-ed12c1ac5d10 | -0.01219 | -51.16565 | 2024-12-01 04:44:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1aeec038-ea51-3a77-8075-4b6e489bd74b | -2.6416 | -49.90804 | 2024-12-01 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7227f080-b0ff-3539-9a6c-549408cf68ae | -3.38091 | -49.85399 | 2024-12-01 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb678396-7976-3655-9e87-5f071934cf0d | -2.67266 | -46.61263 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68ed8bac-d9e9-3157-84e1-4750aeb174a2 | -2.69854 | -52.91659 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f55a4a65-8f36-3e17-833b-26d792cec6fe | -2.84164 | -49.883 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 27c0d73a-7a7e-3365-969e-a21ef6968f93 | -5.73293 | -43.98309 | 2024-12-01 04:44:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac0f001a-9619-30bf-bedf-84888e1abe6e | -1.19798 | -51.75296 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ea271387-f76b-3d53-b851-3c0a1be7e6f7 | -3.32937 | -50.18219 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abaaeb49-3045-337c-9842-c9e8851ab670 | -2.60148 | -46.57201 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e147372-6dc0-3295-bcb2-406210ed9908 | -2.33344 | -53.86747 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79eb30df-e9d1-313b-a029-f29774978918 | -4.17351 | -48.61752 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a0994ce-20c1-3939-921e-d09863cd0dc2 | -1.10153 | -53.38545 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a982dea5-f566-3c6d-91a8-408b797041be | -2.08518 | -50.64579 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17d7373a-eb8b-39ef-8e6c-597f79bbc843 | -2.7638 | -54.0249 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 813f37e9-2ff6-3b1f-857a-0e4d97dda49c | -1.77082 | -47.91222 | 2024-12-01 04:44:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bcb1a746-b9fc-3a03-8d2c-f6819ece2c35 | -2.78639 | -49.8286 | 2024-12-01 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31be5a80-0a52-3e83-aadf-79b8a21a96ed | -3.21075 | -54.1764 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 29dfb7b1-f731-3416-85be-eda3b01b4c09 | -3.26345 | -53.62849 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d33b6b2b-7572-3508-8217-c7b0c7f40f31 | -2.52762 | -54.07677 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db167195-d51c-31f3-b367-da9c82bd302d | -2.61022 | -51.80714 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b98ea319-1b82-3c34-b448-48bd16722e9e | -3.48911 | -53.8185 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76cad0b5-8d43-3c2f-8a7b-6fb214bad918 | -1.06558 | -53.63465 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0cca8a8-5054-384e-8f03-06dca4ba2dcb | -3.01363 | -54.05623 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef932f9d-0f2c-33e1-b611-26a5b782fe21 | -1.29126 | -52.10582 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f68d0619-f343-36f1-9b03-dec6980050ff | -2.62436 | -46.95536 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 792307ce-f46c-3e03-89d3-ff2e901e719b | -3.28944 | -53.67043 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0053081c-a01e-3d1a-ab00-10d45b8a8ca0 | -3.36719 | -51.12478 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d44eaf3c-0e0a-34b1-b7dc-77b77e1fee76 | -0.60243 | -51.69268 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f8a6abf0-e6c5-36ae-b134-3ee3fa097232 | -1.56519 | -51.17299 | 2024-12-01 04:44:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d12c757-f945-326d-9166-69b91863b37c | -3.18086 | -54.33031 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4acf1d9d-8000-345a-8637-4acf085513ea | -3.12863 | -46.04961 | 2024-12-01 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d5a243c-1864-3149-8606-f6ac92362a1b | -5.30224 | -45.2625 | 2024-12-01 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f5efb53-e5e3-392f-9410-43a65ca13fff | -1.6721 | -52.49984 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0268a876-84e1-3273-b85c-9ce776916eea | -4.1911 | -50.68523 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8dc449b5-5793-3c42-88ff-11eca27d3f67 | -2.44203 | -53.88712 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 138edb80-e241-30af-b70a-0e0e66f7c788 | -4.11111 | -54.40918 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1594b63-38ec-35f3-b47a-33f960a966e2 | -4.52852 | -45.69997 | 2024-12-01 04:44:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a06d1ab9-60c6-397b-8ee7-081d81d5037a | -2.69468 | -46.86158 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cba82de7-f6f4-37aa-9c1c-1be81927836b | -3.97387 | -49.91426 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b679115c-66d5-30e4-97d4-f7cc083b7dff | -1.24259 | -51.79741 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e343bef4-0665-3d38-90c4-35eb68c4df91 | -4.53722 | -45.6967 | 2024-12-01 04:44:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e7637d5-559b-3cd5-9f27-e017b61e0e69 | -3.00511 | -53.23552 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5518b69a-dcaf-3577-8f1f-1c63c83b5979 | -3.49996 | -50.32525 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d6e9726-998e-39ce-be9d-75862e67eee1 | -3.1046 | -50.32037 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 692d1f11-1008-34d0-a142-4c4da7210345 | -3.48317 | -53.8086 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4e657b6-2493-3525-a075-2af1637cc2eb | -3.80374 | -49.72787 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 091fdd57-bf82-3733-a5f6-85a72111eab7 | -2.89667 | -53.965 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f0980ce1-257b-3832-b433-eccbeeea1881 | -1.34781 | -51.9515 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7625a81-435b-3637-9844-1c2d55e23770 | -1.35979 | -51.85347 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b1d92ff-0e3d-3c8f-a3ee-0d092927889e | -3.17244 | -53.63779 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 005f7b06-88c9-3904-97c5-fa7669c914de | -1.31861 | -51.67257 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7772423c-c0e7-34b4-bdb6-d07cf3f253ae | -3.28664 | -53.67183 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db9f9506-81e3-3c4d-9777-4725a0fc8da6 | -3.7976 | -46.68959 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54e5f653-a840-3aca-8c65-aa1ded184ef4 | -2.80245 | -54.04707 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 447583f2-7b02-33a2-a5a1-99d7a398298d | -3.06058 | -53.8157 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fab8a7b4-b7bb-367e-a9b2-10a7a20f77c6 | -2.44688 | -53.62048 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a01926df-85e6-3a9e-98fd-b8389adeb657 | -3.068 | -53.81683 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c9f48e7-2827-3f04-bf57-b0c483268643 | -1.09763 | -53.6028 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea3cf29c-9bd3-346b-ab18-348d2e71dadf | -2.43877 | -53.62365 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db22b859-7316-3ff3-8e79-f7f572eb5085 | -3.29996 | -50.80047 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f35fbe7-99a8-321e-bbb9-d08b76a48468 | -4.55597 | -43.30349 | 2024-12-01 04:44:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 5c57bf71-c24e-38cf-9835-ddcc75861cc1 | -3.29098 | -53.6682 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c68a21c-bc55-30fc-be8d-4750dd96eac9 | -3.78978 | -58.97836 | 2024-12-01 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4c39dad-76bb-3982-bdd6-5c472cd5ebfa | -4.08108 | -50.03033 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef68e57f-b369-315f-85ef-3a42617e7acf | -2.69498 | -52.91602 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b1d332f0-1591-356e-b643-34c4e2cd6b42 | -4.8 | -44.99469 | 2024-12-01 04:44:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5caca2af-aefb-3fba-92e5-7e27121163ec | -2.58832 | -53.98737 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 902d77e9-16bc-38df-860d-5f83e2676d72 | -2.46031 | -46.5766 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c47599d8-a512-3914-a73b-208aab4284a9 | -1.00073 | -51.71952 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78e52472-4725-3bda-b399-711f5283564a | -1.07416 | -53.38995 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e37a0aa1-cf47-3840-b45a-186f95e820a9 | -4.64452 | -48.46231 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e91c7c7-c491-3677-9e08-79f0a8a7b726 | -2.98829 | -45.58107 | 2024-12-01 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 347a8de1-8b62-3d45-8076-c7b5e8ee5b2a | -3.84728 | -51.38343 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3928f6e3-fecc-3b42-92a1-9881438dfbdf | -4.14844 | -48.2229 | 2024-12-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d9ff0ad-31a0-354a-aa71-4f1757b5ad07 | -3.48149 | -50.24816 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e13a7a9-a198-32bb-b9f7-42e1035e9f16 | -3.20039 | -46.5593 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2e2a32a-75cd-3824-8051-3a772c611a87 | -4.0099 | -49.94117 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cb6192b-4823-3a5f-8a45-8af6da144ec1 | -1.2347 | -52.09369 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c748fbb2-44d2-3a1f-a207-92c85ee96a84 | -1.44221 | -55.128 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59a8b34c-a202-3089-82cc-bcf577901f37 | -2.70923 | -48.65408 | 2024-12-01 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4571b30-c5d1-3426-a802-9f74d650c8db | -2.65341 | -51.71301 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffdfb80a-6243-3aa2-b25b-8c5977ba05e2 | -2.37796 | -50.3792 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adbe81ca-2744-3d6c-b422-f505a990188e | -3.44752 | -49.98819 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb530e39-282e-31bc-99bf-5c9c2ac79268 | -3.48767 | -53.8151 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dae9696-6751-37f1-bd9f-b029ff097029 | -4.94203 | -49.93302 | 2024-12-01 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7aecc80-6839-352a-b088-a87d76e1fd61 | -3.31778 | -50.19098 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a20117b-a155-310c-83ea-b6874562b439 | -3.07386 | -53.8042 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c10a1249-4367-3750-aa52-90c0e2f043da | -1.70325 | -52.64656 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 862a52c8-7ceb-3fe3-a03a-412300544c75 | -1.00664 | -51.71969 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2a59a3ab-56e0-308a-9e88-dbfe52d94ffa | -1.2712 | -54.55302 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e4a9d2a-0205-361a-9690-145f3b0a7e65 | -1.58383 | -52.28348 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b109a370-f89b-3513-8d6d-75e9776446de | -3.71742 | -51.15112 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0970229-e6a4-3023-a8e2-b1674a1f6f8f | -5.5516 | -50.27464 | 2024-12-01 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe8a4f16-7d7e-3653-8309-2a33656b3efe | -1.69887 | -52.4679 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58e701b9-9720-3c83-bf28-e1ee2b8a85ae | -1.9738 | -46.46442 | 2024-12-01 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README63.md)
