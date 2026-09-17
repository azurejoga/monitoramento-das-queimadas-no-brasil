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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a2270f3-f7c4-38fc-8978-23c8cfc3da83 | -8.4797 | -57.6282 | 2026-09-17 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| bae7bf28-2dd7-37fc-a40f-fc9b08146ed3 | -4.5229 | -54.9639 | 2026-09-17 00:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| b4f6a1f8-b8fe-3f7f-8136-b42c12de1d33 | -2.908 | -54.171 | 2026-09-17 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| a7feeba3-9901-3f82-93b8-846aa6a1c283 | -10.8499 | -46.1544 | 2026-09-17 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 83d1a251-c616-3b44-8d16-25f6e12ccfa3 | -9.4102 | -62.7113 | 2026-09-17 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 134.1 |
| cd4fbfc8-9b03-3455-8802-24296a04101a | -6.9309 | -63.0301 | 2026-09-17 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 434d3d86-abf0-396a-985e-3ea9906ccb9d | -9.8884 | -48.3794 | 2026-09-17 00:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| c8004f77-4e70-3469-a753-726e3d4fbd14 | -14.1405 | -48.7317 | 2026-09-17 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 616ee7ad-0087-3c19-94dc-a26b03983ce0 | -11.2766 | -43.4829 | 2026-09-17 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.5 |
| f3bf8814-62c9-3478-8684-b680378b5556 | -6.713 | -58.8058 | 2026-09-17 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 81a35f17-3f22-317d-bdf8-e09969cd74e9 | -9.2753 | -60.6355 | 2026-09-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 1b73d2a2-69dd-33c5-a100-1d7dbe523bbe | -9.2939 | -60.6345 | 2026-09-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 5358b3a5-d6ed-3628-bd6c-795cf89056f7 | -9.1056 | -60.9703 | 2026-09-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| ea7374da-16ad-3cdf-84e4-a2d92ecc1258 | -9.6094 | -45.3315 | 2026-09-17 00:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 4368b608-5592-390a-9b97-d7e8ee97a903 | -5.6472 | -44.7964 | 2026-09-17 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 3c617552-ec97-3801-b5c2-7b94a51652fa | -12.8543 | -44.386 | 2026-09-17 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 5e3f9544-5afd-3533-9b69-379bf67a897d | -2.9582 | -50.3149 | 2026-09-17 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 468ec593-2add-3713-80f4-c219af54b98c | -8.4796 | -57.6478 | 2026-09-17 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 94ed81f5-14b2-3dd6-a6ae-2c134ec242d3 | -9.2754 | -60.6162 | 2026-09-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 3574d6dc-1d4f-3df5-90ef-e9946f9cfdcb | -9.8694 | -48.3814 | 2026-09-17 00:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 95dc45b6-7ac1-3df3-b557-6b5587bddc4a | -10.7729 | -46.2096 | 2026-09-17 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| e70994ee-2f0f-3f47-a785-ad2b98bc11bb | -10.8308 | -46.1569 | 2026-09-17 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| cff9bf72-28d2-3d27-ae55-2104da976fb5 | -4.5228 | -54.9839 | 2026-09-17 00:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 1fc8f9ed-f813-3623-871b-971a6294b4ef | -9.6091 | -45.3544 | 2026-09-17 00:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 274.4 |
| 64babd91-bee3-3d18-9608-9a7ed4f9fc13 | -2.9079 | -54.1911 | 2026-09-17 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| c14fd253-96f7-383e-b390-556bc58705c9 | -6.9147 | -59.0295 | 2026-09-17 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 16f44ad1-738e-3bf6-8285-b7f27f54c14d | -2.6965 | -57.6278 | 2026-09-17 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 52f11b09-cdaf-3577-bcd2-ea9f505759b3 | -10.3827 | -46.8873 | 2026-09-17 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 0be63788-c70e-32cb-a3f2-38d10168a909 | -9.131 | -45.7273 | 2026-09-17 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 173.9 |
| fa5b6473-b27f-3a94-9715-a8388701f181 | -2.9581 | -50.3359 | 2026-09-17 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 6cc4e645-d708-3b44-858f-b66a7d0a258b | -9.112 | -45.7294 | 2026-09-17 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 158.1 |
| c44df69e-f22c-3824-bb64-9616d7dec40a | -8.4982 | -57.6468 | 2026-09-17 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 183.3 |
| b7dc4f63-0a5f-344a-8ef1-c2a3fbae9011 | -6.8216 | -59.1686 | 2026-09-17 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 17ef49b5-69f4-381d-966f-91e4f03360f7 | -8.4983 | -57.6271 | 2026-09-17 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| ba01fc9f-5ba1-3baa-a769-7576170d07b4 | -5.647 | -44.8192 | 2026-09-17 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| cfd59dcd-e94b-39fb-93bf-dea1e1fbb957 | -11.277 | -43.4592 | 2026-09-17 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| deaed9e6-abe6-3558-a572-f96b30f47802 | -6.8396 | -62.8824 | 2026-09-17 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| c13c7123-f9a2-363b-b994-07fd3378b903 | -6.8032 | -59.1693 | 2026-09-17 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 7ea97a4e-3f96-330d-b512-427a46b3a895 | -3.8096 | -58.8994 | 2026-09-17 00:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| a9c7bda9-37ee-31a6-81f5-596042e54e8a | -6.931 | -63.0113 | 2026-09-17 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| f3cd2b0a-a1a0-3641-a05a-838f6aad2deb | -9.3916 | -62.7121 | 2026-09-17 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 4358494f-0bfa-3564-856a-73fe02bc33f6 | -4.5045 | -54.9646 | 2026-09-17 00:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 194.1 |
| 82d99268-c6f5-3673-ad44-0e254877d63b | -2.6966 | -57.6084 | 2026-09-17 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 990d2962-a4b6-3e97-8d74-d27a75931099 | -10.792 | -46.2071 | 2026-09-17 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| e6d0e713-d6ce-311d-8b1d-e9f1f85cf351 | -6.8395 | -62.9013 | 2026-09-17 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 67788f5c-55f6-360d-889f-ab26fb2ba187 | -6.8215 | -59.1879 | 2026-09-17 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| b4ea4a1d-d57f-3f31-802f-010043647d22 | -10.7923 | -46.1845 | 2026-09-17 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 02b59ef1-eb6c-318b-9abb-5e6360b04804 | -6.8962 | -59.0303 | 2026-09-17 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 67676b31-5126-333b-919f-64f61c9b5519 | -13.3949 | -57.0242 | 2026-09-17 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 53b5d108-647f-341b-959a-daaa23fa5951 | -13.3758 | -57.026 | 2026-09-17 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 0343c9a6-dbdf-393a-af37-2e170bb1115e | -9.5769 | -66.2592 | 2026-09-17 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f256a907-7891-399e-ad4d-7f07e30878b9 | -6.8031 | -59.1886 | 2026-09-17 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 8aa7a65a-1ebf-31dd-b4c5-a6950c635c3d | -4.5044 | -54.9845 | 2026-09-17 00:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 6c4d0ab8-ed0c-383d-ac9e-141bf4f0ee57 | -14.1401 | -48.7539 | 2026-09-17 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 7debf7c8-9309-33d0-918d-ec3ec7e79439 | -14.9599 | -47.5274 | 2026-09-17 00:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 55.0 |
| cbca89fc-28ad-3585-80dd-e663d6a265bc | -8.0993 | -61.8165 | 2026-09-17 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 5f51aafa-a3fd-3389-8276-1f704c9a1242 | -9.1057 | -60.9511 | 2026-09-17 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 8f07e8e3-2440-372e-842b-8f861558bd08 | -9.6091 | -45.3544 | 2026-09-17 00:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 396.4 |
| 2560b3e6-44f0-325d-9362-0948ff280e93 | -2.6966 | -57.6084 | 2026-09-17 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 3de5c3af-5d20-3624-8f94-81ae6a85a068 | -8.7604 | -66.5623 | 2026-09-17 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| e84616ae-e1c8-3bef-861b-b03a48149c69 | -3.4757 | -54.7171 | 2026-09-17 00:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 167.9 |
| e1b011c5-a7d1-3dbe-b3bf-8ceb361909c8 | -11.2766 | -43.4829 | 2026-09-17 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 6bc7ae7b-c247-3c1d-9283-f8b73d1abbcc | -9.8694 | -48.3814 | 2026-09-17 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 23223c9e-52fe-35bc-9d35-86894ae51e28 | -8.4983 | -57.6271 | 2026-09-17 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| e3c00fec-154d-3136-a0d8-ba5e7597b63b | -4.5229 | -54.9639 | 2026-09-17 00:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 136e7308-a208-3d8b-8309-b350d19cd7e5 | -6.713 | -58.8058 | 2026-09-17 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 00e34cfa-0ff0-3078-bc64-f4d1dc6083bf | -9.6284 | -45.3293 | 2026-09-17 00:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 32ac3752-f115-342d-9f59-4ee9b5514982 | -3.494 | -54.7166 | 2026-09-17 00:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 0e5d6a6c-8b2c-38f3-89db-b9f5a7faea94 | -9.131 | -45.7273 | 2026-09-17 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 85c584a2-c87a-374d-a36c-a12c518f48dc | -9.8884 | -48.3794 | 2026-09-17 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 611e0544-9302-37f7-86bf-03e9dae4d067 | -2.9766 | -50.3354 | 2026-09-17 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| aec3820e-6c8b-3778-99e9-b743fc2e8b9b | -11.277 | -43.4592 | 2026-09-17 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 86395848-0a9a-31c7-9a49-49760e62a436 | -6.8401 | -59.1678 | 2026-09-17 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 70e42744-4bea-3864-a18d-8c64e8710ed9 | -9.4102 | -62.7113 | 2026-09-17 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 197a1770-a170-3448-884f-91a11e8f48e3 | -9.5156 | -40.3061 | 2026-09-17 00:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 77.7 |
| 8837290b-50dd-347c-8e22-100f91fffd5e | -9.4101 | -62.7303 | 2026-09-17 00:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 676e6b47-242b-31ff-ac60-c80658ba3cf2 | -10.8308 | -46.1569 | 2026-09-17 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.4 |
| e25da985-fe15-343e-a741-7db7fa8726f6 | -13.3949 | -57.0242 | 2026-09-17 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 2d23ff8d-14f4-395b-a3d1-21ae914f997d | -12.8543 | -44.386 | 2026-09-17 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 6edcf866-9c5b-3b60-81ce-0e3412ebbf56 | -6.8032 | -59.1693 | 2026-09-17 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 261b9ff4-07cc-3655-ba76-d06f38fc4b23 | -9.1056 | -60.9703 | 2026-09-17 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 0911fe86-0c95-3db5-b22a-93e0810be13d | -10.8499 | -46.1544 | 2026-09-17 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 0897d064-0fbb-3ed6-ab21-0bdc1dccbc2a | -9.8881 | -48.4013 | 2026-09-17 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 3ab81809-e6f2-39d8-95e8-53b35a1c50d7 | -10.3827 | -46.8873 | 2026-09-17 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 2915f305-8dd3-3fa3-8362-f37f0920045b | -3.4941 | -54.6967 | 2026-09-17 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 1b6b15ab-2e70-3662-9703-e893687642a5 | -9.628 | -45.3521 | 2026-09-17 00:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 213.7 |
| 2afe7379-b3a1-304b-a417-cfb0b105107c | -2.908 | -54.171 | 2026-09-17 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 2d5e69e6-932a-3b59-a81c-6a984e83a609 | -6.8962 | -59.0303 | 2026-09-17 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 27839dc4-9d79-3a79-8d3a-8500414e122d | -3.8096 | -58.8994 | 2026-09-17 00:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 2049c2a1-110b-3a59-838a-92cb4a27bc02 | -9.496 | -40.3337 | 2026-09-17 00:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 113.1 |
| 00edbae4-8bb4-37ba-a9c7-759866393221 | -6.8031 | -59.1886 | 2026-09-17 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| c46ef674-2d69-3952-97f9-3792b0104a89 | -6.84 | -59.1871 | 2026-09-17 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| ff65a72c-4cc6-3c19-b0b1-2f0ee21791d0 | -6.8215 | -59.1879 | 2026-09-17 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 13ff68d3-190e-3c0a-a9a3-b1bb31074b0c | -10.7923 | -46.1845 | 2026-09-17 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| e902cdfc-9285-3b2a-ab7a-d6ab5c7c5ab8 | -8.4797 | -57.6282 | 2026-09-17 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 479a57c5-8fce-3bc1-a00b-e74c74cc60e5 | -9.2754 | -60.6162 | 2026-09-17 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 5df28a60-19bf-3f3e-addc-c0d5df1a89a7 | -3.4757 | -54.6972 | 2026-09-17 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 6b9a2d3e-239e-31b9-a045-6210522c00d8 | -9.2939 | -60.6345 | 2026-09-17 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 44e9aeb4-9696-3570-8031-516070662808 | -6.9147 | -59.0295 | 2026-09-17 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 07d692c0-ac73-3523-a9bf-47494cc3dca9 | -6.9309 | -63.0301 | 2026-09-17 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |


[Clique aqui para ver as próximas entradas](README2.md)
