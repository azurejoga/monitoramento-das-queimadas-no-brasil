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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab5ffceb-c025-38b6-b7fe-2b95436d0419 | -10.44075 | -47.27798 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4007fe9-b1c6-3065-8236-00936bea712e | -2.93108 | -54.16441 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8fd3f23-3e97-3e2b-a07c-6957dc9d1a3d | -3.9732 | -56.11693 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 89c558b9-61d6-3b84-99e9-f3ad5b18ee2a | -3.98985 | -59.22226 | 2026-10-08 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af4f7039-63ed-33a0-ae0b-cafd97eeb60e | -3.27415 | -51.0667 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59d46702-b42c-3798-aea4-c16e092a1798 | -3.5468 | -54.67746 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 37f0b491-4362-336a-b08b-08c462ed05c5 | -2.82531 | -57.60793 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a47dd148-2911-37e7-a30d-e20e77422ead | -3.29325 | -54.03795 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9dd2c35e-dd1f-38fa-8d2a-4f08e887016d | -9.84113 | -47.47153 | 2026-10-08 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d9168d7-766c-3579-bfd2-35b487c64f9e | -3.02312 | -54.18326 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01e79083-1658-3c38-b0c6-b6980188bde0 | -5.24435 | -50.91583 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8739d581-f733-35fa-87ae-54255d5ebc77 | -4.34384 | -47.76462 | 2026-10-08 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 593e1a00-8ba8-3f2b-b760-8dab0fea4b63 | -3.30335 | -54.02197 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16c6dfae-261a-3fc7-9a63-f3fe3f68a62d | -3.27496 | -54.0365 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa386ccb-bf0c-3e4c-8c44-9e2e1adb342a | -3.32047 | -50.18096 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7776455-436c-3a9b-b42b-9227882c14a1 | -2.79269 | -54.07336 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d5fd8382-b961-3316-becb-3a172b031730 | -8.07622 | -55.30285 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ff0c27a-1b52-3690-95dc-8f7f4dc72c81 | -5.83413 | -52.05841 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8172e4f7-7e57-3966-ad6d-14bf5a6739a7 | -7.20163 | -45.35276 | 2026-10-08 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 574f1c71-6655-3f57-9862-0de0adef9442 | -6.81061 | -55.29834 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d0d4817-f2eb-36a0-89d7-abadff32aec0 | -6.82614 | -44.86863 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 43fa2d2b-a8ca-3e82-9afa-04167ff0ad63 | -3.16742 | -54.73894 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| eeb147d9-664d-3c86-a933-fb6bf8083f17 | -4.43373 | -55.65831 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7b5eb7b-6205-3479-b2ee-cb7b1a755e70 | -6.09106 | -53.49486 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b367a798-93cb-387d-abb2-c7385e25c81f | -3.04686 | -54.14473 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0e7f597-98cb-398f-98a1-e7e6290d46a6 | -3.52327 | -54.6311 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05a0be8d-6d9b-30e2-8650-385c59e4a238 | -11.23391 | -46.24281 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fd43c24-12ac-3b4d-9fd3-419e38a6cfeb | -2.7779 | -54.07103 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a7c870e-a8dc-3993-a026-db836cffb929 | -2.86829 | -54.47595 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 267091bd-6237-3679-ab98-0d2628a2e2b2 | -3.10202 | -53.77631 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4da1b761-4a51-3f26-bb25-564243e64424 | -3.07955 | -54.27231 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc26f172-d378-3d8f-8283-66f62c319876 | -5.20273 | -48.21412 | 2026-10-08 04:46:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1a769dd-1643-39c0-96e7-1b644bd27ac8 | -2.49926 | -56.1568 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4447b0e-c083-38f8-9308-72c8c0a11e54 | -3.01459 | -54.06947 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4176c1f2-01e0-3318-9ec0-1f0815de7e34 | -3.10113 | -54.1848 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9f6284ed-7375-38d9-bf0e-515b4ce4de50 | -10.83891 | -48.13253 | 2026-10-08 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 06adddca-6b2b-37a3-b04e-9deaba66454c | -3.53284 | -59.49892 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc36ce0c-a120-3a3d-b4e4-35dcd4c2b50f | -3.22865 | -53.38304 | 2026-10-08 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d087682-f089-3154-8513-eda8f702939c | -3.3011 | -53.86996 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30579bdf-f99c-3226-a970-8665ce9cbc30 | -3.56946 | -54.65733 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4a15cb9-de7d-36d3-9668-beb2d94bf8d1 | -2.80169 | -54.08825 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 59f72cb9-5c01-3613-a045-079ae5715770 | -3.01085 | -54.14073 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f632452f-3843-3621-b5b5-8aa8ba51aca8 | -2.99457 | -54.05297 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d35f0189-c916-39be-acaa-1e3e992e2acb | -10.43677 | -47.27745 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09227cb2-54b5-3241-918b-1ac8e3a4837f | -3.03452 | -53.94407 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a790dc1-ec0f-3b6c-8bc6-541d482feab9 | -3.30837 | -53.8711 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e6387c35-bd53-388c-a903-7c4fe008da2c | -2.48776 | -56.14717 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b7d2bf5-3f39-33ff-9aee-dc6168ad2c97 | -3.51134 | -54.63146 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7846cda5-6657-3db6-8b38-ef53dceb9224 | -3.75929 | -59.46703 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a37dfcc-7620-3795-94d0-9bc7490d05b4 | -3.27138 | -51.06274 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8861dc62-678d-32e1-8033-ef7c2c625201 | -3.35098 | -54.17209 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80796bd0-6dde-3d30-9f2d-e9dc922bd968 | -3.73513 | -51.21032 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdb77f64-0ed1-3ef1-bfdb-e80456d30f4e | -4.89756 | -54.99499 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e3977a0-9201-3511-84c5-2d47418967e6 | -3.28027 | -54.05058 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93aa8419-e599-3272-a2ca-92a69d24da5c | -5.89783 | -52.04322 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9964871b-f889-3abe-a642-63c946edd1b3 | -3.85093 | -50.42246 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbe444f1-7c09-33fe-aa2b-a9dfaf43080f | -6.09352 | -53.49458 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 83551af4-9fcd-3fd7-b534-84f856ede507 | -2.84885 | -54.1173 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdff782d-73c0-3220-a31b-efa34ebecdfa | -3.91813 | -52.03884 | 2026-10-08 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae2f4b16-7181-3097-880a-b1b01a321055 | -3.99868 | -56.24858 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1887ce12-9632-3a75-a94f-7dbcf857257e | -2.93104 | -53.93404 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 932f15c2-8dd9-3a6e-84da-d8a73dc0470c | -6.45421 | -59.94942 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71d91cbc-b3f4-36de-951d-30042038ee1f | -3.10615 | -53.78001 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3d50cf12-22b0-355e-8fb3-42f65da63304 | -3.84433 | -55.98266 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36e47b7f-46c7-392e-b295-9fc18c243b75 | -4.31972 | -50.77718 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d1d3e24-3060-364d-b568-8b1668cd23f9 | -7.07658 | -40.94178 | 2026-10-08 04:46:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6d09fb73-2394-307b-a2a9-ee08d036a3ca | -3.27929 | -54.03134 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74d8a353-7c3c-3063-9d5c-15136c873cea | -3.66427 | -57.08951 | 2026-10-08 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 048eeb3a-16d0-36b0-9b77-721c094fcb8d | -3.95897 | -56.12618 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b8c1003-bf3b-3301-be16-19a8fcfb934f | -3.1763 | -57.09434 | 2026-10-08 04:46:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b76fec4-0b85-3649-b069-9d76a89840b6 | -4.06757 | -51.04028 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5db49d76-2ea2-3119-a591-ba823d8390a8 | -3.00034 | -54.0405 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4648e501-26ad-37ca-8ad6-0635cdd39e0a | -11.74581 | -43.64297 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a739dbf9-edf9-3209-a626-a3d7930d3a29 | -3.04766 | -53.88487 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a745a318-1989-3ab1-8fbf-ffae2eb2afa6 | -3.28596 | -54.03823 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cda0812-bb49-32f6-be70-acd458f4614d | -11.06936 | -49.53451 | 2026-10-08 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28d79244-dbd6-3c49-be85-09f7d14f9f18 | -5.70015 | -53.49663 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b81c0e97-54b6-3151-8af2-c684d9b8ac48 | -10.30308 | -46.6179 | 2026-10-08 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddf3052b-a59b-3a09-ac35-53105459b9e6 | -3.51587 | -54.52912 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f3bbc98-e927-3763-8ddd-39b9436c8982 | -4.06803 | -59.84204 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1b4e831d-05d0-32f5-8532-b8c5882dc4fb | -9.91443 | -44.79549 | 2026-10-08 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c4832a9-d4fd-3d0b-a0cc-d8841780d7cc | -3.01989 | -54.08371 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6563b552-4ae1-3ecb-99a0-91b0490a8618 | -5.30041 | -60.09052 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4579c67e-1703-3cc9-ac87-0bb91a692d2a | -4.43116 | -55.65777 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 025938cc-b195-326c-94dc-75fa15d01055 | -3.01775 | -54.24154 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b96e0868-fc6d-3f7d-aee4-f4f9755aa1fb | -3.66434 | -57.09431 | 2026-10-08 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7358c879-8fd0-37dd-940d-b1ca2005f945 | -2.94065 | -54.15236 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ea51426a-379b-3788-9f4f-b6aa9f38fa8d | -3.28322 | -59.41128 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22ac6236-7bac-364c-abd9-94b8c0839fab | -7.22039 | -55.16485 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e5f8edd-44f9-356a-8905-588be8a28313 | -3.08088 | -53.95872 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 66a41a85-f13d-3cab-9209-9de2507cc943 | -3.07339 | -54.23935 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72c3ac12-72af-31ec-924c-850f013f95c8 | -3.00694 | -54.11759 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 51084707-057e-3363-8ffb-d0bb32cde225 | -3.38842 | -59.42862 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74ddfcfa-894a-3d18-94c3-3cbdc5771675 | -3.01689 | -54.07878 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b5f5c478-06a3-39f8-b0f7-c6f621231769 | -3.58995 | -54.67488 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 79d40851-1ba1-3014-aedf-80130e78fa7d | -7.88562 | -44.24003 | 2026-10-08 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a09b0031-16a6-3f1a-b025-11e43d911b0e | -3.05283 | -54.15467 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3433732d-4aba-3df4-ab45-9a80e702cbdb | -6.83122 | -44.8648 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4605e030-9429-32f4-83c3-3b425013de7d | -3.10902 | -54.15913 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7ef54cd5-4603-374d-bb14-4986f1c0008c | -8.38422 | -46.29173 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README90.md)
