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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10f16c68-55ad-31ee-a430-61298882e7d3 | -6.79285 | -59.80079 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5aea6e17-d718-371c-ad71-61912cf6d513 | -7.14914 | -42.79434 | 2026-08-23 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 65a34ab7-bccb-3d3b-9af4-4a5cca2683b3 | -6.78455 | -59.42612 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02fda6ec-ee29-3ae6-85ea-76bd3cce52fb | -6.2607 | -55.41709 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ead9860-5757-3d2d-ab06-8df2aa73dc66 | -6.79488 | -58.65763 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18248c97-3c63-3495-8e87-71a327d4a284 | -5.00315 | -56.14019 | 2026-08-23 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22f588f4-817e-35ca-9931-f284a542ce69 | -6.80154 | -58.66558 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 19e84332-bb00-3610-850a-fd6c38e23552 | -6.81403 | -59.66763 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9fd15086-a474-3840-bc73-fffed7207719 | -6.80302 | -59.42924 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2308054b-85ee-3e50-b12d-b0bf4b7d1059 | -6.94297 | -59.07304 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9530cfda-9ff9-3365-8e06-2c83849eb217 | -6.80285 | -59.67461 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b68eb03-c4e9-31bf-afa5-591d455cf136 | -7.15001 | -43.10243 | 2026-08-23 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d6c6b8a6-46ba-3d95-9406-90fc90b735c3 | -6.37839 | -54.96936 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0edd945a-86fc-3498-8da2-735e86e7acac | -7.72874 | -46.13557 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a1b741e-2835-3355-b278-5852790c6a8f | -6.84165 | -59.46122 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8031f9c0-3c9d-3b41-b973-8bbcec0e699b | -6.67466 | -58.72946 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d67e0558-15f9-32bb-9218-28307a416cff | -6.55077 | -56.17355 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50d5492a-a6a4-3b08-9192-ba1afc3f07e7 | -6.2559 | -55.41646 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb96334a-d08e-37cf-83f5-bd34ba958a60 | -6.77536 | -43.08702 | 2026-08-23 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 084656bc-16b4-3437-bcf5-ab207adbe079 | -8.81282 | -46.62183 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e46f6c55-eab5-3b8b-b4ac-bd713c391fd5 | -5.76777 | -57.57664 | 2026-08-23 04:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ca75be0-68bb-33b1-b4e1-702b26f6315c | -6.80387 | -59.42466 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1d36e27-b444-39fd-b209-98024479dcca | -6.97137 | -59.06114 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f1bf2045-8c1d-373e-bab1-c84370cfa756 | -2.99189 | -48.95637 | 2026-08-23 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f50f4870-3551-3aa7-9119-4109a24ad0c0 | -6.8096 | -58.65417 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9ed0ec1d-d627-300a-bd8a-790434832e86 | -6.80526 | -58.64462 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 473ca0e0-f978-3b55-93d0-d7e4a39e7888 | -6.66468 | -58.79774 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f06c1068-afb2-3cd5-8101-8bb7d8fc2fcd | -6.37501 | -54.9706 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33b208f1-a2e9-3290-9103-dcf99b94b82d | -2.5209 | -54.88538 | 2026-08-23 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f529355f-1720-37c9-a33b-f1c6b4978df3 | -4.99849 | -56.1367 | 2026-08-23 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7a644ab-f53c-38c0-b8bd-ff98af1146c3 | -7.73795 | -46.14492 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72d115ab-83e0-3449-ad9c-1cdd6b39be24 | -7.17744 | -42.74503 | 2026-08-23 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 43d0d0bd-e3cf-32c5-8e7b-c1b810150fa7 | -4.998 | -56.13951 | 2026-08-23 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0d866ae-c33e-3da9-b169-06a730fbb819 | -6.83805 | -59.95726 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 689d199a-7d17-39e6-a65a-5863ef2331da | -7.14861 | -42.79805 | 2026-08-23 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 29fd7506-7432-36ff-8d23-2302fa09148b | -3.59587 | -54.04289 | 2026-08-23 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fec684a8-4545-37f8-908b-7ac2bec1b524 | -6.67458 | -58.74205 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 9fd0eb4c-bf02-35e7-a8d7-49710dea785d | -6.92078 | -59.43784 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dd7e51b-94f8-39b5-95ad-20e82e6d67fa | -6.80816 | -58.98532 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fbfc22b-6c7b-3e19-be31-7a4db2f6e761 | -8.93061 | -48.5447 | 2026-08-23 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4b86cf8f-5ac7-312f-b404-f88f4a5047ea | -6.6998 | -58.72514 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 67aae394-788a-3d97-ad0a-2352eda3cd6d | -7.03035 | -48.02042 | 2026-08-23 04:44:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcf0313a-c002-3712-aea3-4aef4f2d4d96 | -7.48652 | -45.1468 | 2026-08-23 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f97a878-cda7-3c10-af4a-1f62b67c03bf | -6.66566 | -58.74513 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0f9afe07-d13b-3c3e-bb97-72a493a32088 | -6.85027 | -59.41371 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a8225ae-79a2-31e2-97ac-5d1e9f1fcefd | -6.81475 | -58.64828 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| afc9dc0f-62aa-32de-8463-eaf8fc09cfd2 | -8.6765 | -44.30105 | 2026-08-23 04:44:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02921d28-f184-3a82-8e2e-1459fd5e1cb5 | -6.82325 | -59.6687 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eb954c79-efa8-3ca1-90bb-98b9ec0a8468 | -4.16744 | -42.43697 | 2026-08-23 04:44:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 16296171-b8ec-3d25-974d-df6c78a1acc4 | -7.26292 | -49.90311 | 2026-08-23 04:44:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abaf1ddc-b0b3-3083-9f9a-5fe5601f6cba | -6.13992 | -59.91208 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 544f023d-2087-324f-bad1-90cfda3b0d4b | -6.18423 | -55.43407 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f7edfe5-37af-3481-beeb-a20c2a4988b6 | -6.8016 | -59.66519 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3864c2c8-8f27-3b33-8566-fd8d4769c209 | -6.80638 | -59.65519 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdd13343-f245-3a60-bc36-cdfa171d53a6 | -8.1048 | -50.05637 | 2026-08-23 04:44:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d04d3b5b-7260-3afa-83ff-15fc6cc1e00f | -8.17381 | -44.44603 | 2026-08-23 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3be736b-32c9-37bc-b0c6-30209c936432 | -6.57883 | -56.24977 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4a668cb-344e-35b5-9773-b3e20b683035 | -6.80376 | -58.65307 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 58cefd21-8c16-38a9-b4d7-c6373dcf8d4c | -8.82107 | -46.62992 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a02983df-87be-3f1d-9340-a4e4e86ccc81 | -7.07248 | -45.00393 | 2026-08-23 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8066d89a-9bbb-33a0-8195-5511511059ac | -6.85918 | -56.86929 | 2026-08-23 04:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d42f6f12-ea4c-30a9-89cf-61dbb56c9328 | -7.48109 | -46.09567 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a9ed363c-9ce5-3487-97a1-cc180fdb2cf6 | -7.6882 | -50.74801 | 2026-08-23 04:44:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 939b0aac-afa2-3a2a-a982-109f8109fec8 | -4.92809 | -56.13339 | 2026-08-23 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 801fa82c-b691-3b2f-94a4-3a0c5f0632a5 | -6.69904 | -58.72928 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 43ee142c-6002-3ba0-817f-d2440605f294 | -6.19299 | -53.49862 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b34a310-9b84-3c2a-9f1a-b46d96d6124a | -6.82945 | -59.67 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ff5de858-1d6d-3bf3-8332-b07a9680c386 | -6.7517 | -58.67351 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c0561cc-f020-3a01-bbd2-cd9aea816a3b | -6.19541 | -53.53467 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa38f1cd-d2d6-3382-b3e6-7fb1bdba422e | -6.68134 | -58.72629 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f7500289-1994-33db-908d-dd47a4e993eb | -7.26587 | -49.88496 | 2026-08-23 04:44:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 64e3b397-36e4-30d9-9d2b-4a1bb88fa59f | -5.5304 | -46.60941 | 2026-08-23 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d69381f-2954-3dbc-9157-cc3316a36fb1 | -6.79539 | -42.67561 | 2026-08-23 04:44:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aa380a7d-409c-304b-8609-91486a5b5008 | -6.24227 | -55.38186 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c8c485d-ee49-35c8-a651-8063bdc89ec1 | -7.30043 | -42.98123 | 2026-08-23 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 46b49e6b-4a17-3315-960b-c148d55d0ef1 | -6.96701 | -59.05126 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f1d04db-628c-3e59-bb65-3b795ae84ce4 | -6.68723 | -58.72732 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1d48d22f-6f8b-33b3-88d6-65b2b91ba2c9 | -6.76269 | -58.67978 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eec8f237-dc89-3942-bd08-0dc8d8a993e1 | -8.53672 | -48.50627 | 2026-08-23 04:44:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9894d2b-775d-385f-9015-8a8e20fbe3fb | -6.79649 | -58.64894 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f1e9c3d5-d9bb-33f2-b6d5-8cd801f08ae6 | -7.98358 | -45.25798 | 2026-08-23 04:44:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dce2c89-4560-392e-9475-39c9c6510171 | -6.66645 | -58.7409 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 588a6543-c77e-300b-a8c0-4cef5db3da33 | -6.82556 | -59.67488 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1f2a39c7-f0ef-30f8-8434-fb17fc6be812 | -6.67747 | -58.7472 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 90cda014-3536-311d-be9e-7e45851edff5 | -6.80068 | -59.67005 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f45bdc5-db0d-3154-bfec-4db8a35a891a | -6.86324 | -59.03481 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49bc52fd-7900-36c5-ad99-b12b9ae3904b | -6.55196 | -58.5263 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09ac9e40-fc21-39f8-90aa-732aacfa3ed9 | -6.68801 | -58.72309 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 46aa47f3-6d5a-3a23-af95-1da2b888414a | -8.09518 | -50.051 | 2026-08-23 04:44:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 63fd10f8-df78-3574-9c76-4a2a6cefb6bd | -6.81398 | -58.65245 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9cda8c81-a731-34bc-bc2d-53f6e51b829e | -5.60212 | -45.65862 | 2026-08-23 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a24a1e1-6ce2-37e5-b434-4336d42395d5 | -6.94897 | -59.07413 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 561c40b5-18e8-3333-8791-176518987443 | -7.3713 | -55.67942 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35eac18e-3469-3c0c-acf4-43972d075bec | -6.77587 | -43.0835 | 2026-08-23 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3b13f2f-1729-3914-86bf-c34a0b38474a | -6.57732 | -56.25161 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b6b408d-b1be-3102-a301-eef5b2574917 | -6.80074 | -58.65867 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8d570dd2-9c9b-355e-addd-b22b7ec765ff | -2.56003 | -47.24536 | 2026-08-23 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8ac0144-402f-31ba-b045-69c8ed0bf9ae | -6.19069 | -53.51107 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e9c581e-a18d-3042-a940-5f763875bdad | -6.81495 | -59.66273 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf0f47cc-2f56-305a-bcae-140ef1ecf6b4 | -2.95932 | -49.27079 | 2026-08-23 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README26.md)
