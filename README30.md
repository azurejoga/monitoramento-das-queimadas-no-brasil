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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13564340-63b5-3125-a7c7-eb86a08f6067 | -8.10236 | -61.19367 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfc3280c-4085-3c97-8b72-471fcf35782c | -7.52747 | -61.38179 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 01e1980b-50ae-3c40-bc17-4ab2ffc9a34c | -7.55611 | -63.48002 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 819f9e19-9ce5-3c6f-a055-f957dd8b1f9b | -9.12854 | -59.66349 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db37acb4-64e9-3027-886f-7c2262b1c57f | -7.45572 | -60.63311 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7170c11-fedd-3010-8b35-a28b068d008c | -9.19586 | -59.66265 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a10476ca-24b1-3983-97d1-cc14fe91e3c9 | -8.10307 | -61.18941 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1419742c-5923-3b09-a4d6-c46d43f94450 | -6.10917 | -59.91406 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8148b88-403f-3f8c-a862-e66799c06a63 | -11.31249 | -49.95768 | 2025-08-14 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e156b232-f306-3840-b085-63e211a86457 | -9.12913 | -59.65983 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cecfb172-f47f-3854-a468-de18674d246f | -6.96506 | -59.29059 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78e46532-4709-341c-8a6a-c2f4bc1bca00 | -6.13646 | -57.82569 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 455aca21-a817-33d6-8cc0-69b14cbb7fc2 | -7.11641 | -59.4161 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6651d4d-d249-3847-ad41-09e59421105c | -6.09833 | -59.93638 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7903d3c1-f65c-377d-9d4c-2723f2c4e341 | -7.25497 | -59.99399 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4339281f-faaf-3d75-aeaf-066323de5308 | -7.12657 | -59.63461 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdfa3205-9c0f-32f4-9220-cd3e0d1b3bf2 | -9.1901 | -59.6767 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8877c861-79ba-3156-a330-be07895a592d | -10.00253 | -59.21845 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3cd448f6-e6e5-3b68-81d1-cddf9528fea8 | -6.64461 | -58.45745 | 2025-08-14 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7e2278e4-bb7a-31e4-8528-fb88fc7b4e21 | -6.9221 | -59.14203 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 94d62b2a-f22e-3814-b929-af1e7059ab31 | -6.09482 | -59.93584 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6774fa67-8f65-3213-a554-632f26e1cf97 | -7.13501 | -59.64758 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1425a47-ef7d-3da1-844c-c10610a90768 | -7.45158 | -57.65135 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf69019f-aed0-3258-8899-2a8852870ff9 | -5.79321 | -43.61845 | 2025-08-14 05:10:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96c75615-6540-3bd7-a8f6-406bc42a1f78 | -5.88512 | -57.73942 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6594a5b-a9d5-3111-bf1a-3098056c1f57 | -6.53705 | -56.20385 | 2025-08-14 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da0eeea0-9536-379b-8bd9-8f7deacf2de5 | -6.09225 | -59.95147 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8278489-92c4-3707-a7b6-bbd23018d95a | -5.75631 | -59.89635 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47a11604-bb70-301a-b99f-671e35958005 | -5.74604 | -59.87066 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84afaa4c-d3dc-37e1-b047-2edcadc8d8bf | -7.81804 | -61.32808 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 427896c7-9428-3b84-acbc-cb3830aa1f59 | -7.28961 | -57.64374 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e23641bd-1c73-34da-a3b7-9f1948742368 | -6.90623 | -59.15441 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b063efa-2793-32f2-bf99-74e1c123150d | -10.34623 | -57.59826 | 2025-08-14 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 960bc9eb-3f84-3882-bb11-9325fa58cecf | -7.88327 | -61.8089 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b3bf23b-d794-3db9-af3f-d4a3091fb69e | -9.16516 | -59.67326 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea618664-8024-30f1-978d-74d3f752480b | -6.9074 | -59.14715 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c140d828-43cf-3758-b5d1-99eb996f1be0 | -6.90064 | -59.14605 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2d199305-62d0-36bd-90b1-7d6f55be318c | -5.75694 | -59.89243 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56d9bd39-bd4a-34b6-ae96-ba654ab49dbb | -7.11741 | -59.84231 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f3a530e-80d7-395d-9b89-c819a1ff6975 | -6.0961 | -59.92803 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6f81975-3756-364d-bf39-d14acffd60fd | -9.60707 | -55.14236 | 2025-08-14 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab72013f-baf9-32c7-a4a2-1b7e66777f9e | -10.0053 | -59.22254 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e13b8a8-a100-3701-96de-36a2ca4dc578 | -7.26415 | -60.00342 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be5a7fe9-789b-377c-a896-9e471dbb4efe | -6.09705 | -59.94419 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ef7e019-dd53-3d74-9921-c63090304879 | -9.15619 | -59.66428 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 782f3bb4-fe14-330a-8a04-2434a4d51086 | -7.38413 | -56.6911 | 2025-08-14 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a01549b5-6155-3298-91ae-67ff66b09735 | -9.50044 | -60.54438 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2da3639e-c850-3702-be9a-d94793dc2c34 | -6.08588 | -59.94645 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d1d7540f-20f4-31f0-a688-960dbbc3fa89 | -5.78976 | -43.61745 | 2025-08-14 05:10:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5e32382-ee3a-3cf4-a042-56dc486d68b3 | -6.9102 | -59.15133 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c773a563-4667-345d-9c5e-68a3b94e1274 | -5.7627 | -59.90142 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b04a47ea-fa31-3abf-842b-005394aaf6ae | -6.89505 | -59.1377 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 163d595d-bbe5-32ac-a43f-aea0f03230b5 | -7.12806 | -60.1288 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 055fa273-f100-3da5-99dc-cd5830135a56 | -6.89843 | -59.13825 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34db1954-0dcb-3f21-a2b8-344374bd9b9a | -6.0846 | -59.95428 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ae004477-f916-3a1b-8cb9-b44c7201c5fa | -7.45639 | -60.62901 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 033f5e36-aeb8-3e95-965c-132ae05721d7 | -8.10388 | -61.20705 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47cdb469-8e43-3d10-b87a-f370c257bf15 | -6.90006 | -59.14968 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0e4f83bb-8329-3dd5-b32c-644bc62ef933 | -7.88018 | -61.8273 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 26ac4fe3-889d-354d-9687-fcb84c3fe4e8 | -6.89226 | -59.13352 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c6c8bd4-a1a3-3812-abb4-40656bfd1743 | -9.058 | -60.65397 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55a62a16-a405-3662-b0d4-bcd47ec8a8ae | -10.00586 | -59.219 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4fa15ec4-6fcc-3705-bf82-7a3c43eb9f31 | -8.0951 | -54.98587 | 2025-08-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7c79f98-8b97-34eb-88f1-ae4838d13f5a | -6.94571 | -44.55722 | 2025-08-14 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e971e122-866e-3907-9eca-c29d4b9b1aa8 | -6.94479 | -44.55665 | 2025-08-14 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 54e8f15a-1348-30e5-8cc0-76deda2d12f5 | -5.73237 | -59.88855 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07786410-5ee6-3fe2-970b-baa708574ffc | -7.12932 | -60.12099 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4630367b-a802-317a-9f27-14ba65ab75e1 | -9.2038 | -59.65648 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d7dc963-5145-3c98-8a0d-ceea887d9ee2 | -10.00643 | -59.21545 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a27c1c5f-fd8e-3caa-afd4-4acd4cc77a4c | -7.88404 | -61.80428 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6c6dca5-26cc-3fc6-bd7f-c66a6a4cb8a8 | -5.74929 | -59.89523 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4a33998-3953-3a7c-9eec-b7cca6f0e912 | -6.66054 | -59.09267 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b43dbad-02f7-3104-bc58-4cb643acc673 | -5.74992 | -59.89131 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74afae98-c037-362b-a18e-58c27ad4bc7e | -9.16016 | -59.66118 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8419cef4-e36c-369c-883c-fe92914c0147 | -8.65489 | -60.52565 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c076c50c-bbc3-3f55-af0b-532ac5c389f7 | -6.88256 | -59.15056 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 61ad1752-2a11-361e-b238-20e3d8f8af02 | -6.87183 | -59.15255 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 807a15b4-d43e-328c-bece-4d70ab3dedb2 | -6.89902 | -59.13462 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e9464ca-6923-3be9-a550-c39544a504b5 | -6.10854 | -59.91795 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a59be29c-1c67-3614-90df-26265b2e8f8c | -9.46198 | -63.14808 | 2025-08-14 05:10:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c540981-5a78-3c5e-947b-2064a2f7deb2 | -6.0964 | -59.9481 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e79dd37-771a-3fe7-a0a6-83120234f3fa | -7.87795 | -61.81747 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2f19b027-de0d-31ab-8f0d-5688927b02bc | -6.90975 | -59.13261 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 018b7a66-7d3e-3190-97cb-fd340bd2c7ac | -7.46152 | -59.88551 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 880a52e4-94fb-3e98-93ed-3a7d248c6c69 | -6.90285 | -59.15387 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4a6bbf49-8e1c-371a-a3e0-a597b47484f8 | -6.8877 | -59.14024 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68a8ff38-d6be-3893-ba87-5c823f1e587f | -7.60057 | -63.52413 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5e87ebf5-2697-3580-b411-6d04bbf9b5eb | -7.8704 | -61.81619 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 840d97da-1f28-3b48-8648-968292f92d1a | -6.89726 | -59.1455 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e3562fd1-fd02-34d2-bd23-b9566c60faf2 | -6.1047 | -59.94136 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ed52545-ebc2-38d5-b358-a4122b5a71fd | -9.15001 | -59.65951 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57447e68-9653-36b1-a43c-644f148b1ffb | -7.28797 | -57.65412 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98df941c-fc68-3278-baa6-0f8f5658d252 | -6.61804 | -43.88572 | 2025-08-14 05:10:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3af22112-c7f0-3fd8-b4d3-465cad9b21fe | -6.88712 | -59.14386 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 41eb290e-3316-31de-919d-f9419bbed9cf | -6.88036 | -59.14276 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eedda5c4-f90b-3900-b375-cde697f3558d | -6.09546 | -59.93193 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce54ac77-5a81-3491-a720-2a4e5281068f | -7.12321 | -59.41722 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c51f2e4-4b66-3816-b60e-1a05a273c855 | -6.11076 | -59.92631 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1451d66e-373e-3697-9fb0-79795cb48167 | -9.19248 | -59.66208 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d0ab8a2-fd2e-3d62-9672-ea486e6a492a | -7.3334 | -60.62731 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README31.md)
