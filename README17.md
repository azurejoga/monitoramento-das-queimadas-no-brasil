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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 539319e4-8c7a-3169-ad16-94aaacfd8ea8 | -3.0932 | -53.7239 | 2026-10-06 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 3e0487d7-b73d-3c45-bcc1-c0c1c65245ff | -3.073 | -54.2674 | 2026-10-06 02:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 8fd47480-e663-3f6f-ba72-b9683de7f7fc | -9.0231 | -65.7169 | 2026-10-06 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 9b092a44-42b4-3ab5-a3c4-83d743c36f71 | -2.9265 | -54.1305 | 2026-10-06 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 9cb9bf18-142b-30f7-9613-76ec1f25eb7a | -3.6732 | -55.9425 | 2026-10-06 02:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 233bb188-47f4-3f67-b577-44ff8265ff5e | -3.0548 | -54.2277 | 2026-10-06 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| adabdd60-eb43-32a7-9a30-a8b3d61117be | -3.0731 | -54.2473 | 2026-10-06 02:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 173.1 |
| 3398a594-bdf5-3666-b702-2cd8dae6c1fa | -3.0191 | -53.9071 | 2026-10-06 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| bc14f630-b964-3142-8347-3cfcf8499777 | -2.8713 | -54.1518 | 2026-10-06 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 937fd401-1803-32d9-99aa-de022a77601b | -2.9449 | -54.13 | 2026-10-06 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 5e00c80f-e9f6-3a09-9b0d-efb090d2b155 | -8.7036 | -45.2061 | 2026-10-06 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 5600b0b0-0a1d-3c02-938f-51042fb8f03b | -11.2611 | -45.4849 | 2026-10-06 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| aa7a96b1-ed19-34a8-9bf1-dbb9c04e0a42 | -3.11 | -54.1862 | 2026-10-06 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 485d58b3-49be-390e-ac9b-b04633cf2ae6 | -9.7312 | -65.0944 | 2026-10-06 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| d303e564-c8ef-3264-a478-48551503c70b | -11.2798 | -45.5052 | 2026-10-06 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 203.3 |
| 9fac67cd-b6e6-3ab5-950a-70c397cebbd9 | -3.0 | -54.1287 | 2026-10-06 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 765f8d14-b0d7-3db7-98cd-51c4b3f63ca9 | -11.2607 | -45.5078 | 2026-10-06 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| fba479d1-957e-3863-b659-15941f627478 | -3.0734 | -54.167 | 2026-10-06 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 1e11ffe3-cdd6-38e6-a282-6aa781aaebed | -11.2794 | -45.5281 | 2026-10-06 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 597d6bd5-c250-388a-8682-c4256b4a2ab6 | -2.9816 | -54.1291 | 2026-10-06 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| fd5914ca-752c-3256-9f49-f2cc18f810ba | -3.0917 | -54.1666 | 2026-10-06 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 188cf79f-9a2f-32f4-962d-71347ab6a275 | -3.6731 | -55.9622 | 2026-10-06 02:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| e34c74ce-1b90-3f08-b5ce-06c9c1e16b00 | -3.0192 | -53.887 | 2026-10-06 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 188e9803-a265-3eaf-82a2-edd83e50ce51 | -5.8323 | -45.0105 | 2026-10-06 02:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 32a0eb95-41a4-3e7a-9621-a353f451b5b3 | -3.0732 | -54.2273 | 2026-10-06 02:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 606aff88-fbaf-3a05-952f-e510884ed9af | -3.0375 | -53.9066 | 2026-10-06 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 1fed4d78-5411-3f49-bb60-69f7bf4c82a9 | -3.0548 | -54.2076 | 2026-10-06 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 6e8e354d-0cc2-37db-8ebb-9d45788751e3 | -3.1101 | -54.1661 | 2026-10-06 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| f0297c12-43f4-35b7-a767-fc23e0583cf4 | -3.6915 | -55.9618 | 2026-10-06 02:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| ddd04b85-e6a1-32ea-81dd-d1bc447ca3db | -2.8714 | -54.1318 | 2026-10-06 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c71ad2cd-8040-30c0-bb14-0d3d72236c8c | -3.1115 | -53.7637 | 2026-10-06 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 614e0b5c-45bd-3fa2-b5af-62530e10ac77 | -2.7796 | -54.0937 | 2026-10-06 02:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 111803fc-9e18-3b82-88c7-d4d7527f2a40 | -2.8897 | -54.1514 | 2026-10-06 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b2090acd-7c20-3a0d-806d-764839441283 | -3.0375 | -53.8865 | 2026-10-06 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| f8dddb72-1a93-3051-9097-05fe058c91aa | -5.8511 | -45.0091 | 2026-10-06 02:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 9a50c72b-c312-3d9f-b414-2a951131ab94 | -3.0917 | -54.1867 | 2026-10-06 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| fa4924db-30fc-3f3c-8367-0fd81022a767 | -3.1116 | -53.7436 | 2026-10-06 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 304c1e48-ec97-3e9b-9d7e-f4502e05d4a2 | -2.7879 | -57.6843 | 2026-10-06 02:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a96afcbb-1b90-3234-80c1-4b73a1f23d3b | -2.9448 | -54.1501 | 2026-10-06 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 72e7d275-4813-3be2-8ebb-2baaa8210474 | -11.2794 | -45.5281 | 2026-10-06 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| f3c2a6e3-9e58-3f15-9617-27bfb2774b33 | -3.0 | -54.1287 | 2026-10-06 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 84cba72c-46c1-3a82-ae60-b2557f8adaca | -3.1115 | -53.7637 | 2026-10-06 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 1898aa16-0fbf-3754-a1f4-4eb3af7bdc22 | -3.6732 | -55.9425 | 2026-10-06 03:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| e51a24a2-daa9-3686-a838-30f3500abeab | -2.8714 | -54.1318 | 2026-10-06 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 2e58b685-c2ca-3479-80bb-8415513bad7e | -2.9449 | -54.13 | 2026-10-06 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 601106b3-a770-32b8-a62c-4a9d935fc0d8 | -5.8511 | -45.0091 | 2026-10-06 03:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| d617b799-21b2-35f8-882d-3590b6afdac8 | -3.0932 | -53.7441 | 2026-10-06 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 56f8a860-51cf-3a15-b1b4-23a0059c2f2b | -3.0932 | -53.7239 | 2026-10-06 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 4ff657bd-aa86-32ac-bf3f-25184e0ce19a | -3.0375 | -53.9066 | 2026-10-06 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 3ee8d322-cc16-36da-8038-830ade0fbf30 | -3.1116 | -53.7436 | 2026-10-06 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 9c0e4757-2b2f-360b-9239-a148dd66d22e | -3.6731 | -55.9622 | 2026-10-06 03:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 13791964-1280-3215-952d-144250fbece8 | -3.0191 | -53.9071 | 2026-10-06 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| f63b7737-95fa-33f4-bce2-ea6818c632bc | -11.2607 | -45.5078 | 2026-10-06 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| a2a1c815-e41e-373e-9b56-0fa0ebcd26ed | -3.6915 | -55.9618 | 2026-10-06 03:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 605c592f-99c8-3ef1-8c76-f6e2c635348f | -5.8323 | -45.0105 | 2026-10-06 03:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 3430e172-2a15-3b7d-8167-b0c3f1a8500d | -2.9448 | -54.1501 | 2026-10-06 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| c8efaeb6-fa13-31a2-871e-dc7dde253257 | -2.7879 | -57.6843 | 2026-10-06 03:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 39127ea8-9f29-3c77-ac32-725f2ef811cd | -9.7312 | -65.0944 | 2026-10-06 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| ea360a24-c94c-38b3-b465-a9921c9d56c0 | -2.9816 | -54.1291 | 2026-10-06 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 824cef08-5b19-3ee8-a27c-48bce319fe1f | -2.9265 | -54.1305 | 2026-10-06 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 8dc4faa8-8336-3a4b-be47-093992f165f5 | -2.7796 | -54.0937 | 2026-10-06 03:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 7bc91971-0d41-3878-96e3-e67814ecc41b | -2.8897 | -54.1514 | 2026-10-06 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 805aa4a7-a6be-33f2-907c-30c93a3181da | -11.2798 | -45.5052 | 2026-10-06 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 64fe5dac-0f46-34a8-8131-f1514aa8eb91 | -11.2611 | -45.4849 | 2026-10-06 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| c1f93bf7-43b0-3ac6-be55-ace7353f5cdf | -11.2802 | -45.4823 | 2026-10-06 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 9adf9b07-8a83-360f-9d88-f6e291725566 | -3.0375 | -53.8865 | 2026-10-06 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 5c6efcc6-fd98-372b-b99d-56a450121249 | -2.8713 | -54.1518 | 2026-10-06 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 269305c6-333a-38ba-a905-ce3358cca54d | -9.0231 | -65.7169 | 2026-10-06 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 31a2a0b8-33b8-35ac-a74b-c102812533bc | -3.0192 | -53.887 | 2026-10-06 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 26f1a8d7-64e0-3783-9ad1-cf5c91898498 | -3.6915 | -55.942 | 2026-10-06 03:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ca20d3d0-0322-3b4e-beac-33519c2d4117 | -2.8713 | -54.1518 | 2026-10-06 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| b6a96ea7-cd7d-361f-8432-115ce324a955 | -2.8897 | -54.1514 | 2026-10-06 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 087e69f9-2496-3f1d-87bc-e0d9b3fdc457 | -2.9265 | -54.1305 | 2026-10-06 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 2094a7f0-1211-33fb-91ba-be2228787758 | -3.1115 | -53.7637 | 2026-10-06 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 775716e4-f25f-3636-a87a-cea6fb9faeaf | -3.6915 | -55.942 | 2026-10-06 03:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 0353c995-b7f0-3f17-b31f-d6e068476dac | -3.0375 | -53.8865 | 2026-10-06 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 78a6f501-42e1-33af-abaa-19d07bf5e4d2 | -3.3723 | -58.1957 | 2026-10-06 03:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 5480010d-5d63-3538-8a90-f64d644efc8a | -5.8323 | -45.0105 | 2026-10-06 03:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| b18c42e1-8355-3320-aed3-aed6aec0cdbd | -3.1101 | -54.1661 | 2026-10-06 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 7280e921-bdda-3f67-ba59-23d92b5dfaa5 | -3.0932 | -53.7441 | 2026-10-06 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 9730c03a-3c49-3d3f-b93e-40a0a6973855 | -3.0915 | -54.2469 | 2026-10-06 03:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 1faab763-f2b8-3243-8032-0d2b77c94a9a | -2.9449 | -54.13 | 2026-10-06 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 8e18fbe9-6cdb-3d5d-b899-9d0635f31023 | -3.0191 | -53.9071 | 2026-10-06 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 1f190022-8768-380d-ad53-dee35ca9ac57 | -11.2798 | -45.5052 | 2026-10-06 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 207.9 |
| 4bae5d73-7eda-3e55-aba7-21020b1441bf | -5.8511 | -45.0091 | 2026-10-06 03:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 142d9a86-c357-358c-8c0c-10702b971e48 | -3.0548 | -54.2076 | 2026-10-06 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 927db1a0-ab44-39f4-8540-c65846cb8d4f | -3.0932 | -53.7239 | 2026-10-06 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| e15c04be-00ce-36e5-8d4a-055f3ca84cf3 | -9.7312 | -65.0944 | 2026-10-06 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 581f4b27-e915-3d36-8a00-007b79f1d272 | -2.7879 | -57.6843 | 2026-10-06 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 5c3b7c8e-8a7c-3b51-8d5b-523caa4f7c0a | -11.2611 | -45.4849 | 2026-10-06 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 7e5acee7-6781-387a-8e32-6d4e77868831 | -3.0192 | -53.887 | 2026-10-06 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 4a3788bd-c17c-38a8-8eb5-bbdeec10eabf | -11.2794 | -45.5281 | 2026-10-06 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| ddb78cdd-6ca6-35f7-b817-3f861aeda19a | -3.0 | -54.1287 | 2026-10-06 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 6c579cc3-0e47-316d-9006-564564ef638b | -3.0548 | -54.2277 | 2026-10-06 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 8852e49c-8fc8-34d9-8d67-c53b846428b9 | -3.6915 | -55.9618 | 2026-10-06 03:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 4c6d47c7-6fb9-3247-92fc-2d17ab14228f | -3.6732 | -55.9425 | 2026-10-06 03:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 53fbdee3-f968-359b-a1c2-cb82a50eae15 | -2.9816 | -54.1291 | 2026-10-06 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 5c43c752-65e1-37a9-a623-a237a0f17508 | -9.0231 | -65.7169 | 2026-10-06 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| c838de28-ba7f-39b4-a6af-de43aa3ba5f4 | -3.0732 | -54.2273 | 2026-10-06 03:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 53cfffd5-280a-3c2a-9788-ca65b0bad670 | -2.8714 | -54.1318 | 2026-10-06 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |


[Clique aqui para ver as próximas entradas](README18.md)
