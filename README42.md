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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb9d82b6-b570-332a-a393-4b36f7c50be0 | -3.62257 | -55.28288 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf899f72-82bf-3522-85a2-a99a9a69e55f | 1.86694 | -55.76513 | 2026-10-06 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 12010502-11a2-3b85-8ea2-5e3d652de0fc | -3.32848 | -50.05398 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad563f41-b514-372c-a276-f8bbec9e9b99 | -2.96047 | -54.14458 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4cc3cddb-58c4-3027-a356-c63edbc39dda | -3.27269 | -54.19042 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c5b06d9-20b2-37ca-be0c-7d3d5ef177c9 | -3.32495 | -50.05342 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d2a3c6f6-2914-3cfe-9060-2a2bfd2a2a08 | -2.95665 | -54.168 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abcbd922-871e-341c-bf75-1e571793c898 | -3.23341 | -53.8813 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1d4b595-0bee-3d60-aa54-6bb6d9c13d4d | -3.23109 | -53.86728 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94e1869a-d551-3a92-abde-e4c851bc8f54 | -2.87267 | -54.1637 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8586468b-b0b3-36c8-80ec-1feb7954fff3 | -3.08456 | -54.2496 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 0313b12d-c6e6-356c-80bb-a384c12c39d9 | -3.95157 | -56.0523 | 2026-10-06 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1a56829-df03-30f5-8141-2fbe605b5b30 | -4.99568 | -42.42615 | 2026-10-06 04:38:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2fc4a356-2b3a-3e37-857f-5b622c72e743 | 2.45856 | -50.82816 | 2026-10-06 04:38:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d0273384-4c40-3c8b-a86e-d5ba731c81a8 | -3.27933 | -50.02171 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbb233f5-7672-344d-b636-5d8f6fa4596b | -2.47971 | -56.0965 | 2026-10-06 04:38:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b04e49d8-c03f-320d-9747-a1b58bc6f0c0 | -3.67245 | -55.94549 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 25324907-f452-38c3-bdea-4428a5d5b744 | -3.51021 | -54.6297 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 218a6d43-3039-3c4e-95a6-9cb796622819 | -2.99177 | -56.61449 | 2026-10-06 04:38:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18d45d4e-1582-3818-91ef-1495f7c390fe | -3.0776 | -54.17608 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cada2d0-9630-33b7-ad9e-28f9f340c54c | -2.77656 | -54.09247 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6e3b4625-0cf7-3159-bf34-cceef0399e52 | -3.08058 | -54.15772 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 98ab2a94-1828-3eae-846a-bf9082b48c87 | -3.06616 | -54.15989 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17df49c1-1738-304a-8ae0-6122ef34a9ca | -3.49061 | -54.63174 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f290a6d1-63c9-367b-b0aa-34a6024b7ce9 | -3.10875 | -53.75871 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a9567b8d-7fec-3673-89af-6a378fd8b1e8 | -2.99701 | -54.12444 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57035588-5443-3887-9ddf-94b2b65cea2f | -5.61335 | -44.84682 | 2026-10-06 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e69acb85-f1da-3024-a285-249b46fd3950 | -3.07843 | -54.25835 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7834705e-eceb-3209-9e02-8c474f8636ce | -1.61543 | -55.12054 | 2026-10-06 04:38:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6645607-4df4-3627-bdf7-b9d1b652dacd | -3.37357 | -58.20501 | 2026-10-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 914a93a8-6154-3a19-9ace-f5c7b221ff54 | -3.27344 | -54.18585 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b629abcc-7be1-3b87-b488-4c3319808c9b | -3.95105 | -56.05543 | 2026-10-06 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3f6b3ca-2415-3bf6-9b66-5e33e7d3d28d | -4.92675 | -45.69136 | 2026-10-06 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c18c6fd-6709-30c4-8ae0-f0638daaf837 | -3.10013 | -54.18202 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 76b17e47-e576-360e-8fcd-d713e3ce52cd | -2.896 | -54.08101 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea892731-488e-39d4-95df-9635c53f2fba | -3.33068 | -53.39029 | 2026-10-06 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d0a67689-406b-3a27-968c-20b7a80bd64d | -3.08148 | -54.23939 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e934e221-9d60-3836-be5c-dea5de40cc1a | -3.07378 | -54.17073 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54e38170-798f-3afd-bef1-ec54b52efc96 | -3.07449 | -54.25016 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| d7a6803f-5673-39e3-a216-4c2d2aa190b5 | -3.27725 | -54.19117 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86c22338-3228-3364-8305-9a24a61c3942 | -3.47947 | -55.43348 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b398e876-0128-3f54-a3aa-2f5d981c32c0 | -3.06312 | -54.17846 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 921f506e-e4fa-3eaa-a337-da970321bbcd | -5.73381 | -41.62746 | 2026-10-06 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4b8895b1-b3ef-3ef0-bbd8-f9a66c616f8f | -2.12878 | -56.70358 | 2026-10-06 04:38:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5681fd63-7e70-3651-b442-143a389bc971 | -1.61089 | -55.11691 | 2026-10-06 04:38:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9097cb86-8b12-3df8-b863-578891e11879 | -3.27452 | -50.40448 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ef2a116-3a91-34ca-9aaa-4a72975e5986 | -3.0654 | -54.16452 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 968b15a8-9f2f-3067-96a8-1c0c97861143 | -3.50459 | -51.67807 | 2026-10-06 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c064201-af41-3762-b9a0-279463126ca5 | -3.08369 | -54.25159 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| a29a4e20-decd-375b-8d67-9297dbab729b | -2.95971 | -54.14922 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 336ebca9-2fb3-30e6-b8b0-eb32ed45edc3 | -2.87172 | -54.14185 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4a55d724-f82f-3c36-9732-1316e8fbc977 | 2.26994 | -50.8249 | 2026-10-06 04:38:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 237c6381-8652-3fbf-8735-5285a51b4ec1 | -5.97367 | -41.36382 | 2026-10-06 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ab0631d9-ffd0-3226-9057-9643402da623 | -3.22519 | -53.87541 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ed2549e-00fc-3be6-8633-02538c339bba | -3.05701 | -54.21595 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| ba755ab4-4fb6-3538-aeff-148f1e62a806 | -3.07651 | -44.46008 | 2026-10-06 04:38:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 435fb023-2250-30c2-a8a9-bcec3956a6fe | -2.90268 | -54.125 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2ca44f1-1a07-3962-89a4-d346bc195435 | -2.98709 | -54.12764 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a826fc25-098c-307e-a0c9-a58f8473b3d2 | -4.36263 | -47.77534 | 2026-10-06 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f879d68c-332d-3966-801c-4e16bb257b88 | -2.94603 | -54.14672 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08b5c3a5-a00b-3f3f-b952-8178aa29750d | -2.88046 | -54.1454 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ddfa0163-1070-3a02-8f73-f212de20a39a | -3.11391 | -53.75507 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be816970-5b4b-3492-b86f-d5bdc27a86d1 | -4.23579 | -49.97883 | 2026-10-06 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18728d46-d7a8-341e-9108-35f9134eed06 | -3.11221 | -53.71005 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 815571a4-1ba9-30d7-af0c-154bf29eeb53 | -2.78112 | -54.09324 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e71baba7-ad0e-3abb-8ad3-9115424ff564 | -2.87633 | -54.17163 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01d37639-87aa-3386-a38b-ee41b0b8dba0 | -5.19082 | -48.31463 | 2026-10-06 04:38:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8274ebd1-1508-35ba-9ae1-28157e79c709 | -2.99558 | -54.10516 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe4ea56a-4d52-3ca4-abcd-5ffdd3ad3050 | -3.09738 | -54.16982 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1ba076a3-f705-3bf6-9bf0-152a1dae8b05 | -3.04001 | -54.2622 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e19fbcda-2e5f-3d27-8dd4-b4788bc65f49 | -2.98787 | -54.12015 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 513e985e-0609-3332-ad3d-b5c828ba673a | -3.08528 | -54.24216 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04a5a0ec-dc5b-3211-98e8-65118ef7aecd | -3.06692 | -54.15524 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e75d3199-793f-349c-991d-5ed5f2390e29 | -3.21344 | -53.94759 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8b367f6-a6a8-372a-9c11-eed40f4cbcb6 | -3.68401 | -55.95427 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fe12713c-8f33-344f-a59c-5a72b0690ef6 | -3.21926 | -53.88361 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e02b6166-ee6a-3f2a-be8d-36ab949317a1 | -3.58197 | -54.31026 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99a073c5-ca47-3673-9079-930496c214df | -2.87553 | -54.14739 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e00f102a-266d-3a79-809f-d8b3918a61e0 | -3.09664 | -54.17442 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| edd95b07-7edd-3588-8f8c-0c13494998f8 | -2.99402 | -54.11441 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b478a33-122b-3f4d-a984-f1c3fb7a6635 | -5.74416 | -45.05664 | 2026-10-06 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a0613ba-be9e-3eca-9eb4-b9cdb7a41a26 | -1.75559 | -54.94997 | 2026-10-06 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a80803ca-40be-3fa6-b2f6-ada61b89d6ae | -3.11175 | -53.76823 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| cf105a9c-520a-3d4a-a250-515bdc91c51a | -2.42423 | -54.75502 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b26a833-6681-34d3-99ee-2d9d53f34b11 | -3.08217 | -54.17683 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57c14de8-abce-3463-bc10-35e92bce78f6 | -3.68504 | -55.94821 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3f77c6b6-a798-3789-b1d5-9de5727c6d8d | -3.50551 | -54.62899 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b2634f0c-b7a7-301d-b4a9-2d5877ba073f | -6.06234 | -42.9103 | 2026-10-06 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| af41af7a-3e49-384b-aa7a-3b58e590c15c | -2.87668 | -54.13996 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d6f6c4a8-6873-38c7-9772-2692938ff03f | -3.00458 | -54.13522 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f37fe6b9-15ff-3bb0-8a90-c8ede0e4492e | -3.60027 | -54.05817 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d69e473-f9ca-3683-ae1e-921ba066dbb4 | -4.45509 | -47.92096 | 2026-10-06 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| f6b20a13-afc2-32ee-9e1d-0979cb09e535 | -3.10121 | -54.1752 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a2f83e74-5ad2-3218-85bf-639431ad9b50 | -3.09091 | -53.72886 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2754ab58-5336-3840-9887-abda48236fe6 | -3.71453 | -48.88154 | 2026-10-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 114aba78-f6b7-3167-9113-b1253df62ff0 | -4.35878 | -47.77826 | 2026-10-06 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a05f0b7a-96ca-3280-9b40-22a933d866a2 | -3.56392 | -54.22102 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be23fbeb-f65e-3f04-abf0-9945e56df704 | -3.07296 | -44.45953 | 2026-10-06 04:38:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e8e0e7f-6af8-3a7c-bead-f871b5dba5f7 | -4.063 | -54.0441 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44465fc0-551e-3860-a3b9-67b8799d2b0b | -3.07536 | -54.24813 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |


[Clique aqui para ver as próximas entradas](README43.md)
