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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 327aed77-472f-3d60-8cae-7fea1bebd9e8 | -2.9265 | -54.1305 | 2026-10-06 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 9bcf5982-3a69-334c-9990-c34ab204b52c | -3.0375 | -53.8865 | 2026-10-06 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| f31f0421-a054-3665-adb0-a32525331f80 | -2.7796 | -54.0937 | 2026-10-06 01:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| d5919258-32bb-3203-95c2-c373ee0275a6 | -3.0 | -54.1287 | 2026-10-06 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 0b68aa74-93c7-3f71-844f-f4d0380d0448 | -2.8897 | -54.1313 | 2026-10-06 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 43b1d94e-9b5f-32a4-a105-e9d69e770704 | -2.7796 | -54.1138 | 2026-10-06 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 1469638b-860d-3d25-9d36-5b689a75d91f | -11.29 | -45.54 | 2026-10-06 01:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 60816e91-1d71-3df9-b754-d6ac32aee99f | -11.29 | -45.49 | 2026-10-06 01:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a90fa882-452b-3836-904b-636cf04087ef | -11.26 | -45.48 | 2026-10-06 01:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be88ba9c-2085-3c3a-8612-320399fcae7a | -11.26 | -45.53 | 2026-10-06 01:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8548faca-4895-34e0-a9bb-674a63607eac | -3.08 | -54.24 | 2026-10-06 01:15:00 | MSG-03 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e6a65c9-797f-3aa1-91df-ae2576b3e419 | -3.3722 | -58.215 | 2026-10-06 01:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 1e584ee8-60b1-3adc-afe5-7721c705284f | -2.9265 | -54.1305 | 2026-10-06 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| ca0f7ee1-04b4-3608-94df-024bc720e654 | -5.8323 | -45.0105 | 2026-10-06 01:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 3cd00b80-2dd8-3c2a-a504-4aa156eedfde | -3.0 | -54.1287 | 2026-10-06 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 3516841c-2ef4-3392-8071-19a502360fbc | -5.8511 | -45.0091 | 2026-10-06 01:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d1349f5c-a30e-364f-9834-5d74b82c5c51 | -3.332 | -59.4852 | 2026-10-06 01:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| aa2317e0-54d2-3b91-95d9-35939f15161e | -3.0375 | -53.9066 | 2026-10-06 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 1de16005-41b4-3ef3-8fe9-e4c1ef3a1be0 | -3.0375 | -53.8865 | 2026-10-06 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 6446c41d-ee3f-3a4a-a4cf-7b318eae5bfa | -3.1116 | -53.7436 | 2026-10-06 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 2f10b733-d78e-3e62-81cc-b9a8ec9f8ecd | 0.4465 | -60.5442 | 2026-10-06 01:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 251e4060-0f96-31ea-8f3a-55cc297ecd2b | -2.8713 | -54.1518 | 2026-10-06 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 161.2 |
| 01d4b29d-2ab3-3418-9e14-a7665791010e | -11.2802 | -45.4823 | 2026-10-06 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.0 |
| db140f55-c494-3620-bc8f-29e6664d76d8 | -2.7879 | -57.6843 | 2026-10-06 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| e6f59679-9742-33bb-a9db-97a713865aab | -2.9448 | -54.1501 | 2026-10-06 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| fb2fee33-e861-3a5e-94e4-504920fe2036 | -5.8321 | -45.0332 | 2026-10-06 01:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 8a8e6f35-1d26-3349-a54d-b8f1620af82f | -3.0932 | -53.7239 | 2026-10-06 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 142.5 |
| f0e82596-9bc7-3a7a-8858-c20e82eccb7a | -2.9265 | -54.1104 | 2026-10-06 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 34a84966-5893-3932-a2f7-ea22f829f3fd | -2.7879 | -57.6649 | 2026-10-06 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| d6f2377e-5621-31cc-9f30-580427d4fb54 | -3.3905 | -58.2146 | 2026-10-06 01:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| b17cd38d-76cd-3c76-9996-f6fee09f1cb5 | -11.2607 | -45.5078 | 2026-10-06 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 5fbe18c0-95e3-308c-a4eb-795b2bede335 | -2.8714 | -54.1318 | 2026-10-06 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 495f7ca6-5225-3577-bd5f-520c3be2b9b6 | -2.8897 | -54.1514 | 2026-10-06 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| da185b96-1f3a-397d-a74b-06556000f9f9 | -2.9816 | -54.1291 | 2026-10-06 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| dc769db8-acc2-3c3a-9d79-1d9e610b55ac | -8.7033 | -45.2289 | 2026-10-06 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| f79aa3ab-4e19-3d34-a467-51d9161b67b5 | -11.2611 | -45.4849 | 2026-10-06 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| f9e05919-7b37-3208-b28e-57bb481fd1b3 | -3.6915 | -55.9618 | 2026-10-06 01:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| bae049a5-d1b1-3fd2-bf2f-a8d3b0170f17 | -11.2798 | -45.5052 | 2026-10-06 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 915d82ca-f7de-3649-84cb-4b5602213db8 | -3.3723 | -58.1957 | 2026-10-06 01:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 105.5 |
| ab84ab83-8756-3ffc-8421-1b3ef36eadde | 0.4465 | -60.5252 | 2026-10-06 01:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a2f0599f-da0f-3605-a34d-e9445e6217ab | -3.0192 | -53.887 | 2026-10-06 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| c80c2ea6-d4dd-3c4c-a5f5-b24a7a2d32db | -3.0001 | -54.1086 | 2026-10-06 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 366602b9-0ea8-33a0-8e63-1c88fbb8c044 | -3.0932 | -53.7441 | 2026-10-06 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 48e851a6-1cd6-3a2b-895e-fdc0f1e86ef3 | -5.8509 | -45.0318 | 2026-10-06 01:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 217c5148-abcc-3e2a-b758-9510a5e09f8e | -3.3906 | -58.1953 | 2026-10-06 01:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 142a8928-7def-3473-90bc-55d113140b37 | -8.7036 | -45.2061 | 2026-10-06 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 31a1495c-5ecc-39f8-a457-6c54f04ddc1e | -2.9449 | -54.13 | 2026-10-06 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 0362ea0e-9241-3e76-9059-ac323a1993cf | -3.6731 | -55.9622 | 2026-10-06 01:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| eb5812e0-e0dc-3e6d-b39d-286ffa9192d5 | -11.6946 | -43.6787 | 2026-10-06 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 2a122980-b477-3714-be6f-016ac4f590a8 | -9.7312 | -65.0944 | 2026-10-06 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 20d64ba6-8664-3841-80f2-09c6b4aed6da | -4.8075 | -47.3261 | 2026-10-06 01:20:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 494a8395-0fd8-3e87-a014-59863b34dbc9 | -2.8712 | -54.1719 | 2026-10-06 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 9d34e7bb-a5ce-343e-bc05-1696cb0e6fce | -3.0933 | -53.7037 | 2026-10-06 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| e515cd18-b50c-3919-8e1e-d9033f465310 | -2.7796 | -54.1138 | 2026-10-06 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 5c2d6e47-46c9-3fc1-8a24-ac8a2d51fb8f | -3.6915 | -55.942 | 2026-10-06 01:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| ee93ebf9-d4f9-386d-bd74-95e175bfdcaa | -3.1115 | -53.7637 | 2026-10-06 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 4a2b42a4-4506-3479-946f-5368b0ea2b91 | -3.0191 | -53.9071 | 2026-10-06 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| dfa5947b-4c02-336b-8447-08ccc93a296f | -3.1116 | -53.7234 | 2026-10-06 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d573d410-4999-3d97-84dd-074d75503cad | -2.7796 | -54.0937 | 2026-10-06 01:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 8955727c-8b6d-3e10-8475-81209604983a | -3.6732 | -55.9425 | 2026-10-06 01:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| d7397090-5469-30b6-8cc8-d1fc5160ff53 | -2.8359 | -59.247002 | 2026-10-06 01:29:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ac15858-c22b-369a-b405-d25fb185a566 | -3.0733 | -54.244202 | 2026-10-06 01:29:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb377677-87ec-3a8e-95d6-ef6874945e49 | -8.3399 | -62.826401 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f949b398-8168-3318-bd35-d82d91b24456 | -2.8702 | -54.167099 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74ebe963-11cc-3fd9-ae8f-63713224d27a | -2.8758 | -54.1478 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab1ba7f3-1441-36ef-958e-0a2bce0c714c | -2.3261 | -57.990299 | 2026-10-06 01:29:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6bd926e8-8718-30ba-b491-9f11f7045d8e | -3.5058 | -54.634998 | 2026-10-06 01:29:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e796e583-18a8-34db-8c20-1e3b74b195d8 | -8.3498 | -62.9165 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 88f968b3-2c6b-3eb0-91c1-5a1e60126c82 | -3.0813 | -54.277599 | 2026-10-06 01:29:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 016e9ef8-099e-3592-b5d7-724a846b0fd5 | -2.9422 | -54.168098 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e9fe343-ae98-393d-abfe-c1cd0497012b | -2.7905 | -57.687099 | 2026-10-06 01:29:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 65b461d9-ada7-3b01-8cb3-8d9756816a71 | -3.1681 | -58.638401 | 2026-10-06 01:29:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6c08ba80-e5b9-375f-b35f-b137bd51dd1e | -3.0239 | -53.910702 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9caff021-3977-33bc-a0fe-938a4ea70162 | -9.4827 | -64.041603 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ea52dfc2-6b88-3bcf-825e-79e3c5409e7b | -2.0715 | -56.860401 | 2026-10-06 01:29:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ba35329-0011-3391-b60f-0e482f51fd4a | -3.0335 | -53.908401 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2224de46-07cd-3962-aefa-1d5a64ff2e02 | -3.1207 | -53.717098 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff76959-a35c-334c-9d1f-fd9b4b2ff2f1 | 3.5791 | -61.325401 | 2026-10-06 01:29:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 09b26e96-d7d8-33cc-a16f-b0be2de78db8 | -2.7858 | -54.114399 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d72a68b-1cbd-3ccc-9119-5b4fb8560043 | -9.1021 | -67.751099 | 2026-10-06 01:29:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0ac4029c-7c5c-373d-827c-466f9b552224 | -9.6697 | -66.816803 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a8cb6c93-d6e1-3d65-b3a4-b033e47afa3a | -3.2317 | -53.8801 | 2026-10-06 01:29:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d64f28e-4d96-3552-bb36-b8dcad323a85 | 1.0319 | -59.449501 | 2026-10-06 01:29:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd7af31-83e9-3d90-a3c8-ba94eef35b7a | -3.091 | -54.275299 | 2026-10-06 01:29:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d1355bc-abf9-3428-b267-ed45660f5abd | -3.0515 | -54.196098 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9196bf64-ce60-3e01-9f18-ccd2a766daec | -2.7687 | -57.681599 | 2026-10-06 01:29:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aaab69a6-c69e-3011-a169-9d0777567206 | -3.083 | -54.241901 | 2026-10-06 01:29:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d78602c-cf8d-3a18-aa23-a9ed4d1b935b | -2.9575 | -54.1465 | 2026-10-06 01:29:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da6f2660-d481-3de0-a32d-ac7fbd8b5ec4 | 3.1233 | -60.567101 | 2026-10-06 01:29:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 90b5c671-4349-3854-b611-54c4d01fe19f | -2.7882 | -57.677101 | 2026-10-06 01:29:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea02e1db-496a-3ca5-9c3b-40b886e87dc7 | -10.2775 | -60.549999 | 2026-10-06 01:29:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 00082dd6-d1b3-3837-8542-10503f148c84 | -3.688 | -55.954601 | 2026-10-06 01:29:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d3c764d-72b3-332a-bd6f-50d3535f7b8e | -3.3837 | -58.194401 | 2026-10-06 01:29:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4e41ae6d-7240-355c-a56f-5107c6852a25 | 3.5693 | -61.3232 | 2026-10-06 01:29:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e68df820-d3b8-3b2c-a8a6-468d2a50a7de | -9.8249 | -65.050903 | 2026-10-06 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8a6a9762-e597-3268-a11e-116fc342d72e | -9.327 | -68.877998 | 2026-10-06 01:29:00 | METOP-C | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| f62650e7-74c1-3140-bce2-79c2723f6863 | -3.496 | -54.637299 | 2026-10-06 01:29:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a457116b-4825-3ec5-bf3c-be449268fa8c | -9.1397 | -65.910103 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 93c072cc-9c9f-3f5e-ac06-b21832b9ee7b | -9.0147 | -65.709396 | 2026-10-06 01:29:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8395db98-ec07-358f-bce7-8eac9040d5d1 | -3.982 | -59.340801 | 2026-10-06 01:29:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
