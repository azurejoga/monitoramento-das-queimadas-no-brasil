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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a98f8bf-8110-3a2b-8d23-45076da634e2 | -1.06805 | -53.64207 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01e911c5-895b-344a-a398-e83df4232232 | -1.65708 | -55.23749 | 2024-11-28 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf2c68c4-c679-3b59-abcb-5b13c5392a56 | -3.24369 | -50.76858 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 97934855-3ae2-3005-b8b6-f3de6a98fc57 | -1.68425 | -52.49697 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25cc8735-606f-34f6-a762-43fbf50caa98 | -1.32293 | -51.91952 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e1b572fe-32fb-3d8a-9de8-e317c98ea344 | -1.65565 | -52.4718 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fe1af67-c31d-3b9d-b706-abe9ab1dc7ba | -1.58672 | -52.27115 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 16fd276d-c28a-3f7e-941b-714d6a2d3d1c | -1.70302 | -52.62757 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cbe4176-d6bc-3581-8131-0f58e538e56e | 1.26044 | -55.91697 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1600c017-6d92-3aea-9a13-9146601b2639 | -3.05819 | -53.28436 | 2024-11-28 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e6ad61e-01c9-3432-a509-326606519c77 | -1.16157 | -53.57124 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e1a39a1-4bcf-3446-ac3c-ffe230cc9a95 | -3.80827 | -52.3551 | 2024-11-28 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 94cb6ab7-bdaf-3343-a920-5056b6559b26 | -3.74017 | -51.83748 | 2024-11-28 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5302988c-3552-3086-a2af-c844f561551f | -2.80017 | -51.58741 | 2024-11-28 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 34db5d47-f7b4-39e7-9750-15d5401b3d7e | -2.77714 | -54.03039 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0458a50d-c0da-3413-9bf1-3c791e5e0aa8 | -3.63309 | -54.4413 | 2024-11-28 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c18b44e0-e01a-3943-afda-df5b522f2692 | -2.17591 | -52.13406 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9294925f-1e42-3e78-bc4b-079a74ac090e | -0.58713 | -51.70314 | 2024-11-28 05:40:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e7d9faa-2cd7-315b-8ba1-eb500620aa0c | -2.89508 | -51.37033 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6381cb48-96b4-341c-9713-3abe11ce104e | -2.82418 | -54.03139 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57859835-2682-3dcd-8d03-4ed9e6514191 | -2.59082 | -53.97291 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7cca1af-82bd-38bd-b6ef-c1866b54a0ae | -2.91335 | -51.71835 | 2024-11-28 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2a9e0e7-f1f9-3457-9f28-98b310629dab | -3.34806 | -50.51303 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9b017db2-d4f7-3dba-b846-301f06b2a53f | -3.11193 | -53.25798 | 2024-11-28 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9ef8c14-709c-3b14-98ca-27513d9dd968 | -3.56985 | -52.28026 | 2024-11-28 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6dcfdf92-7f00-3846-b239-4b52a76fab91 | -1.04514 | -51.74009 | 2024-11-28 05:40:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45c0b8f8-6458-3a1a-86d5-51261dcec613 | -1.06875 | -53.63766 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f6f952f-0f33-3ce7-a502-200648c10cdc | -2.17509 | -52.13948 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b8fff42-71e5-3561-bb94-2afb352a1f9e | -2.25789 | -53.46397 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1a08fc1-5fba-36d3-a842-519463f2edf5 | -2.16858 | -52.1385 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87222154-7692-3f9e-be9b-ab1504377cb9 | -3.09882 | -53.81519 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 73bcdcb9-e6a8-3824-97ca-1f8e678d5faf | -1.67301 | -52.43207 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71583d74-f12f-36ca-9179-d6d23fd21106 | -3.57228 | -53.02056 | 2024-11-28 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd8f77e8-b504-390f-b304-2b5923cbfa65 | -3.55693 | -51.03395 | 2024-11-28 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62851209-9965-3dd2-9b07-9385d6cef89f | -2.94778 | -51.58146 | 2024-11-28 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2cc511f4-0542-3844-ac1e-7bdb297da13a | -1.36135 | -51.96479 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a1feea8e-8b20-35e2-b282-f47b29891f60 | -2.58934 | -53.97897 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d7ba0b6-6ef6-3f73-b16d-94b7319256b8 | -1.6597 | -55.23156 | 2024-11-28 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3f27475-001e-36fc-b1fc-ea21e433c312 | -3.23973 | -54.22113 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c36a444c-a0b1-36e0-98e3-f4df3eb32a32 | -2.36734 | -56.12185 | 2024-11-28 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b75a6cea-9cfc-3d5e-b8b0-8f55b216e93b | 1.43923 | -55.89756 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5748ec4a-1813-35b1-b300-792f04272b70 | -3.9197 | -53.67371 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a602457f-55af-3f38-a7e0-a37df767779d | -1.15503 | -53.5746 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7189a49e-c6c4-30cc-a1fe-3048a0fa8a52 | -2.59019 | -53.97704 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f13ad8eb-4b1c-33d7-ac00-fb1b1675618f | -2.59054 | -53.9707 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 730a58bd-7330-3552-9f33-b5bd3807a088 | -4.22296 | -50.89358 | 2024-11-28 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b14e1768-cfd2-3ac5-8b89-13787c1477ab | -3.96794 | -54.61197 | 2024-11-28 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b61bb178-4905-3bd7-a778-16128b2014d1 | -0.35461 | -49.95345 | 2024-11-28 05:40:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d414ba4-b31a-359c-9a62-24913406a20c | -1.66225 | -52.72657 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c53111cf-24ae-3068-a5f0-d30a5953e498 | -1.59832 | -55.3834 | 2024-11-28 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7e19686-17c7-3ee6-883a-3520ff58f154 | -2.70053 | -51.68313 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 718e18bf-9896-3f8d-8693-de2b0adfd4c7 | -3.34691 | -50.52064 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 85714b3c-7a38-3838-b4da-226bd44fc258 | -2.63704 | -51.77012 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2560cd54-a862-3dfd-ba53-915a2c9599af | -2.75782 | -54.11883 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bf7fc30f-4639-33ab-9665-364b55a6bfda | -2.62945 | -54.30449 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9414caa1-ad45-37cd-a0f4-364e7ad0f18e | -1.70023 | -52.75848 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09cabd4a-a3c3-393f-8189-185a0d1d788e | 1.24802 | -55.96175 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7035edb5-6029-36c5-b22e-f3ae1bffef78 | -2.6025 | -53.97464 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4f5e067-d3bf-30aa-b613-f035ab2ab342 | -3.40197 | -54.28128 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be3eb62e-0a0f-3202-94e4-c0f8e31a5f63 | -3.46565 | -50.53476 | 2024-11-28 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d1e1400-b88e-3c54-a16b-d3a1946753b4 | -2.63617 | -51.7758 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 304bf6c8-67dd-31fd-8fa2-d1afcfb2d537 | -3.91939 | -53.66745 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bf8f1d6b-f281-3524-945d-615ee2053801 | -1.35952 | -54.63327 | 2024-11-28 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 177145cd-35a9-3bf4-a66f-4bd1247e7c41 | -3.23276 | -54.22826 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01904784-7a32-37cd-8956-9158cdd2cf05 | -1.15709 | -53.67258 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8af620d4-afc1-36f3-8b41-f73e66d27ac3 | -3.46094 | -54.48272 | 2024-11-28 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d73389c-5266-31b9-93d7-bd0c2e6ad9c9 | -3.27331 | -53.30747 | 2024-11-28 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 01ccf847-135b-38be-9e97-b54a38e3b4f5 | -1.66373 | -52.71684 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59d5711c-3e3f-3807-9556-4824d05958d9 | 1.31471 | -60.40927 | 2024-11-28 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00e1f28e-e3cb-345e-99fd-10db042f3373 | -1.68571 | -52.434 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7eea1358-7e33-3936-a90a-3c0019cb013b | -2.31615 | -51.95272 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 276faeb5-a529-3472-8dfc-3caa3cf75fcb | -0.24008 | -51.59837 | 2024-11-28 05:40:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63f13049-04c8-395c-888f-ef58910467d6 | -1.58032 | -52.27015 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6a5bfac1-0c9f-3704-8164-731f5a113309 | -4.2176 | -50.89081 | 2024-11-28 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8567cdbe-5f39-39f1-aabb-fd78035a4cb2 | 1.25506 | -55.9673 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96d15131-0ce5-38d9-b663-79d3f94c9c85 | 1.44512 | -55.91137 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87f3c19d-ae42-3a3e-a6e4-85ab0e6e3fec | 1.25166 | -55.92373 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae8213aa-762b-3806-8dbd-10aa2fbdfbd4 | -2.95831 | -51.00617 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 891821b9-fdab-3e7d-8448-7d9e979456b6 | -2.59666 | -53.97377 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdb35799-7f9d-3da6-bc73-458351913513 | -3.19602 | -50.8272 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0e5b7f8-066b-308f-8125-f6dea5b54fd9 | -3.569 | -53.02348 | 2024-11-28 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8406b45e-3562-31f9-8da6-b2a8d37584a3 | -2.90336 | -54.17634 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d76bf91-de44-3c3b-9138-a26e18ed860a | -1.1031 | -54.14391 | 2024-11-28 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd8e5aea-1c56-3da6-a695-7c5a8be515a8 | -3.80969 | -52.36073 | 2024-11-28 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7303302-9762-307a-94aa-f5686ace37b0 | -3.09993 | -53.25719 | 2024-11-28 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c610e18d-eb09-3b66-befa-7d181580f539 | -1.70641 | -54.71942 | 2024-11-28 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f78a6ff2-1ee5-34b0-85a6-5cea194d6420 | -3.43501 | -54.53924 | 2024-11-28 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 874ca279-82da-3c83-811b-f194535187e1 | -1.08428 | -54.03853 | 2024-11-28 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19b4e663-2014-3692-9c61-58128ea67f16 | -2.83745 | -51.84247 | 2024-11-28 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27e45db9-de63-3412-a67f-9852c81e1716 | -1.66299 | -52.72171 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9680ead6-c444-356a-8aa8-647ff3d1216e | -2.75661 | -54.12689 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e976d8e6-29b2-3aca-8a19-36dceb74758c | -2.94085 | -51.5926 | 2024-11-28 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bae8dd89-ad4d-354c-a308-c381f0182425 | -1.6234 | -53.87565 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c05892cc-04fa-315d-94ab-a951fe1728f4 | -1.08997 | -54.03939 | 2024-11-28 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3041d676-4937-3932-802c-4a5d5999be5e | -1.58533 | -52.2701 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ddee3412-ecc4-34a6-b869-e3f27832c61c | -3.11346 | -53.75748 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d57ff746-18dd-3952-b848-6867599906f0 | -1.64764 | -52.4697 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a3af419-710e-366a-b86c-7c5fcb0ca9bb | 1.26526 | -55.91619 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d8b639f-cf37-3600-ac52-1cd8b11c90f5 | 1.44249 | -55.91828 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 051e3776-c18c-3a11-85b9-53a646ac60ac | -1.04684 | -51.73717 | 2024-11-28 05:40:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README96.md)
