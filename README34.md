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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ceb32b04-d632-361f-b551-a9baa823bcd6 | -3.17678 | -48.44263 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 95e1f2f1-4a1f-33ea-bd50-ce1d07a0abe7 | -4.2732 | -42.43284 | 2024-11-27 04:18:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fdfef9d4-6f19-35d8-9ae2-3a0339804249 | -1.79711 | -52.74265 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1046195-b959-3661-890a-6955b1f0b215 | -1.717 | -52.49423 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54ad2644-919d-31ed-8f63-cc9b6e578f76 | -1.90331 | -50.59532 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8fed1416-1b54-3957-99c5-cf402353c04a | -3.34493 | -50.19119 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4eb1e83-6644-3026-bdaf-80ef4b14875c | -2.82447 | -46.81243 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 138965ac-3817-33e5-80da-a12ecaaeb9a0 | -4.14251 | -43.8055 | 2024-11-27 04:18:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| fe739399-3447-32ab-9c63-6e70fc252bbd | -3.97629 | -48.08553 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 767e8989-4510-39d8-8f33-227a891c27f5 | -1.79603 | -52.74944 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7e0c059-bacf-3888-be66-e77231d047f7 | -2.99587 | -45.46775 | 2024-11-27 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90737dff-a8e0-3156-b1ae-3281bed1ef77 | -5.19577 | -43.07962 | 2024-11-27 04:18:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 975fcadf-3710-334d-aa29-4108b6f8a467 | -5.03015 | -43.6021 | 2024-11-27 04:18:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42b8cd98-6aea-39af-9245-3547759065d2 | -4.48771 | -44.4716 | 2024-11-27 04:18:00 | NPP-375D | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0486152d-aef5-323d-bce1-bca096cd36a5 | -1.1561 | -53.68129 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bacb067a-960a-3298-8793-a94a2a66ed7f | -4.35466 | -48.08738 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8269644c-0bf1-3ddd-b78a-9262e9f22899 | -3.08942 | -41.14349 | 2024-11-27 04:18:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 64ae23e0-bd23-3e8d-b9ed-d3b4f62a9262 | -3.99901 | -43.25254 | 2024-11-27 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86e7f57b-472b-3d9e-bc6f-482991aaee97 | -3.50299 | -50.45824 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b629e6af-14d5-32d5-b8a5-d97107d15bd0 | -3.9816 | -48.07694 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0eaddf6-1046-33b2-85da-52aca1b65b43 | -3.24296 | -46.42733 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9433b5cd-ec83-3f8c-9dca-d84132ac9114 | -4.14318 | -43.84455 | 2024-11-27 04:18:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af877ab9-5fb4-349d-b6c3-7a05d45d8e53 | -5.35572 | -42.1289 | 2024-11-27 04:18:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0c39b68a-6f11-3c09-9277-44baa8b88a50 | -2.02579 | -52.41422 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ba429c4-f580-330c-af52-d6112ed304b4 | -3.09288 | -50.35868 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f21fcf72-a17d-3131-930a-9690a6cd5b65 | -2.88615 | -51.38708 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8aeeebf-4ed2-31ea-9a79-67659f644785 | -3.10533 | -53.25644 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccc8c619-7f58-392c-aaf0-28b8ec753cb2 | -3.93672 | -46.71311 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e85d7a8-ddac-35cc-ad7a-b4861216e763 | -3.33352 | -53.72017 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1c9ce17-3def-390e-a0cf-18527ae193be | -4.17683 | -48.44815 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8603c24-d4bd-31c3-a8ac-95e15ea2a817 | -3.08773 | -53.26637 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc7e9541-1c14-3947-8bb8-1dc56a290e24 | -4.10996 | -46.10455 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fede861-93b2-37b9-ac8d-e0ca3f5ac550 | -3.77429 | -46.51137 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 730003f6-05eb-3bb8-b33e-26602a8f2588 | -3.23376 | -53.93466 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a78d6e5-9b74-3817-8ca5-3bd20cca6741 | -2.58984 | -46.20114 | 2024-11-27 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5467e429-b4fb-3055-a421-a96a5921ad7e | -3.1658 | -48.43575 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 00eb497a-7110-3aa8-9cb4-51091ba269b0 | -1.90795 | -50.59608 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2e159f19-a354-312b-9e11-a09ede2907ac | -3.68023 | -49.93102 | 2024-11-27 04:18:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 71aa0f20-27ff-389e-b987-0cd8fef358ff | -4.35183 | -48.12911 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8bc0f2f-6006-3206-a83e-add01ed157cc | -2.68319 | -46.27084 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff6d0538-f48a-3762-a6f9-821daf981061 | -2.82841 | -46.83415 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2cbda45-42ff-3cf6-bb5f-999548f2d5bd | -2.59955 | -54.2126 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5d044289-59f3-39e3-bb31-545d32382bad | -4.61228 | -44.24032 | 2024-11-27 04:18:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24fd1ae1-9b12-3091-96a8-f7782dc95c27 | -2.25546 | -53.74803 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2973ca70-bbc3-32c5-a27b-4a39a63d38de | -3.13016 | -50.27024 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0be58123-fbe3-3dbf-a8d2-487bf2d87270 | -4.70856 | -47.92981 | 2024-11-27 04:18:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2b7bbc6-0ba2-3fad-94da-ee96c477ddd6 | -3.9403 | -46.88911 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0eae9c19-12ed-378d-bc44-76d9974e4e52 | -1.23118 | -51.79491 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70a40f81-4af4-306e-b6f3-798c1b453010 | -3.04066 | -48.51664 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 42e16aba-1b9f-3213-b606-4722b9d9ba36 | -3.28689 | -51.11634 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4be7d5c-0536-3f67-9b1a-13cb799e9347 | -3.84153 | -44.34175 | 2024-11-27 04:18:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66316475-91b8-30dc-9699-140314540664 | -3.71869 | -50.18573 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 200eb287-751d-3ec6-ab48-3f66e162808e | -3.11565 | -53.26719 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c902c43-1973-398b-8543-8659fd61343b | -2.8179 | -48.60727 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 817ce41e-a58b-3829-bbf1-0ba2d3f60111 | -3.97247 | -48.06123 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88002c65-ff98-31c9-b6e5-9f3cba97e135 | -3.57155 | -41.96143 | 2024-11-27 04:18:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 46e6ed40-18a5-3152-9e61-b280708dfe0b | -3.47732 | -50.31031 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a8cf934-c75f-331c-a494-dee9585de30a | -3.26551 | -46.44256 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c3d62db-17ef-334a-90b3-c8c863c87896 | -2.71568 | -48.6713 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96d576d0-c41d-3523-915e-b15bfefa0782 | -3.31759 | -54.10343 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63962006-c4ff-3a5f-8325-f659630aa371 | -3.18313 | -48.42834 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 91194678-255a-35fd-9e67-e9d7967993c1 | -3.77945 | -49.92909 | 2024-11-27 04:18:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f198f9f-5d94-3916-afd3-26c3cba5bed4 | -2.63023 | -48.43229 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99bd0dab-d43e-300b-8b63-a27c103a1f95 | -4.39341 | -41.70547 | 2024-11-27 04:18:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 889bc173-2ac5-30a8-b9b9-d9dcaae407c2 | -3.77315 | -52.40022 | 2024-11-27 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ddf8d07-8f0c-3f46-b286-6de51c831f5b | -5.37239 | -35.61351 | 2024-11-27 04:18:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 266366f1-23fb-3a9f-9cdb-2701ef0ddfeb | -2.8435 | -49.40117 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2efcee66-7c72-3b4d-9ddf-3fc0eec1085d | -3.25875 | -46.41738 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 612308d0-4c61-34a5-adfd-ca07d376a6a7 | -2.69696 | -45.65882 | 2024-11-27 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 444a66b6-a7ec-3118-9711-815f98575828 | -3.93728 | -48.15595 | 2024-11-27 04:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30875c19-dbc6-37a8-bbc4-624e7730aed6 | 0.9832 | -50.06625 | 2024-11-27 04:18:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7658ea8-2ac8-369d-a78c-a35906b9fd95 | -2.83263 | -54.12988 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9d0f564e-d2f6-3647-9072-f9ce2a81f9e2 | -3.29101 | -50.27067 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c2684bb-50f9-372e-a422-3fb531874be7 | -3.67076 | -53.55199 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e573eabf-7ab9-30e9-b6bc-cc588a1b53b5 | -1.44811 | -47.11757 | 2024-11-27 04:18:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cad59045-60e1-3417-a470-48bc7dfc3806 | -3.28554 | -50.61161 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b15cc01f-7459-3527-9f1e-b865b3391884 | -4.29418 | -48.19582 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b9383dd-0458-31e2-b8da-1724de3313c5 | -3.0953 | -53.28362 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3931bac1-b0d4-310f-a9dd-0ebd5b8cc824 | -3.32972 | -53.72608 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be51ee75-1902-384c-94f6-3750c7c716ee | -3.17465 | -50.21997 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56387ab3-8d1c-39a3-8003-b054e1e28ca5 | -4.08783 | -49.73792 | 2024-11-27 04:18:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3775ad0c-5f09-3ae3-9640-24872f635a07 | -3.92785 | -45.84493 | 2024-11-27 04:18:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 118e08ec-928d-3ccf-b810-5b15367292fd | -4.05177 | -46.69402 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6745edee-73bb-3277-8127-5962f4da31c1 | -3.50384 | -53.8088 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f298daf8-9649-37fb-a3f1-2c2ff8c09c9e | -3.08725 | -53.26423 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0b69189-747f-3cea-9cea-c6a7d9e13e80 | -4.9249 | -47.14095 | 2024-11-27 04:18:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 775e2033-5895-33cd-8f5e-419259a7fb5e | -4.2178 | -46.44813 | 2024-11-27 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fdc08b3-7f23-3fb4-9c35-ee6523dc312f | -0.48087 | -48.63257 | 2024-11-27 04:18:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c10661f-2d13-3467-aa88-cd471d9ce6b2 | -3.10353 | -53.27249 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99fae545-87a1-3bde-9df0-c2693db24162 | -3.6077 | -45.11428 | 2024-11-27 04:18:00 | NPP-375D | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f68f0d4-9942-3e5c-a02d-d9b9170cda0b | -2.89563 | -54.1764 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0780c69-4de7-34d9-90ba-eaf24f815bb8 | -4.3093 | -48.07966 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9ee1bec5-4da6-3594-8282-6a6ce5203e79 | -4.49514 | -46.60529 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2275928-c2cb-3220-8904-b798706b103b | -3.90075 | -47.74424 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67c5463f-d273-3a1c-b36e-0af5988b4181 | -4.21907 | -47.21556 | 2024-11-27 04:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8749dbc6-ee87-338c-b406-3b329e611127 | -3.09627 | -53.28213 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d9e77ca-1731-30f2-a074-17694228390d | -2.71528 | -46.29592 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d164a0cb-8af4-388e-891c-7f272c92cbf6 | -5.25524 | -40.59756 | 2024-11-27 04:18:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 54e32483-6cf1-3c9d-8e5e-c88d508445b5 | -1.79824 | -52.74734 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d950893-2efa-3a0f-bfac-77061ca50bc7 | -2.93694 | -54.79514 | 2024-11-27 04:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README35.md)
