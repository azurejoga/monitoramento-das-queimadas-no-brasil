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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8024b460-26a3-3f3d-850b-cff29388fbe9 | -4.27269 | -48.18683 | 2025-09-08 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 24f6c19f-3d21-3ebc-9ab5-b0eb64f3bbed | -7.11075 | -44.13604 | 2025-09-08 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b2d14b7-58a8-310a-9a4c-17d83c5df2b6 | -5.72293 | -43.89705 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8935b267-9dc9-3a11-a471-bbaf1fa4c138 | -3.63768 | -49.20626 | 2025-09-08 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee9b1183-1630-39b7-974a-39b889c8d274 | -9.16721 | -59.37601 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e457e12-086f-33ff-9ab7-d08b14012438 | -6.09134 | -43.11718 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df33fa40-1c0a-3c69-af74-c928502032b8 | -5.565 | -52.16727 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93835dfb-6522-3b22-8c77-7da776075677 | -10.18399 | -46.23806 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a89c283f-4854-372b-aab9-d0b0dd1708aa | -4.65181 | -55.8708 | 2025-09-08 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76e2eb7d-2f01-368b-83fb-33d336a61f0c | -9.67482 | -51.07079 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f79e7dc5-3978-30e1-85b1-6272a9eed05d | -7.66404 | -47.95048 | 2025-09-08 04:51:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b23c2285-6914-3bfb-969e-44b0d41b03b6 | -9.10211 | -46.99806 | 2025-09-08 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8e1695f-783b-3e70-8836-7d17a851f016 | -6.61446 | -44.00786 | 2025-09-08 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2f4950a7-f5be-301f-a72f-5a0920b9f5c6 | -5.88449 | -43.96067 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1a8f6ea9-aeea-3b9c-8cd1-f60e3f6eeade | -6.02618 | -45.88737 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 248e0bfe-6863-3bdc-bfbb-853e42b3d355 | -7.0196 | -44.94912 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e9f4aee2-d0a8-34a4-81b7-ec7a5aab6e7a | -6.26599 | -43.69271 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ac79ed4-7d2b-33a7-8e22-cbfb9b8b649e | -10.22019 | -50.51889 | 2025-09-08 04:51:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 874fd786-6f9e-3ac6-ba29-bcd64b7e3fd2 | -6.40106 | -44.45724 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d11c74c-cde3-3547-973c-1767e14e6cea | -5.42771 | -47.39113 | 2025-09-08 04:51:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24cc2f17-d3c9-30aa-9bd4-2db1dd4e4b41 | -6.82547 | -52.80793 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a908e498-ab1b-39dd-9341-991491d42507 | -9.33309 | -55.1902 | 2025-09-08 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 824a35bf-6a16-389c-8771-dc963140a4e2 | -11.31978 | -47.33339 | 2025-09-08 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8add3519-68e2-37b4-941a-e048d4f6f12a | -6.62752 | -53.35401 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50d9310f-106a-3c18-ac0d-76af95299364 | -11.42224 | -43.64016 | 2025-09-08 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| beda3714-0dcc-3add-bc71-9f7fad84752e | -6.27706 | -53.41926 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d73f2bc-9f2b-3e7b-89d6-520fb1686868 | -6.19973 | -40.96873 | 2025-09-08 04:51:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 42708e9b-8338-34c9-8b40-cb4b7dd84c6d | -9.82047 | -53.32401 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25c84e7f-1ab0-3e08-b9eb-8ce27ee26054 | -11.01542 | -46.03511 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c256fc35-7fdc-3b83-b45b-bc2224b104a2 | -11.33038 | -46.56474 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 86778a76-221c-3b4f-ba8d-09686a505150 | -7.75022 | -50.72448 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67e55fe1-0332-3e1a-9846-0657a4640f19 | -5.87946 | -43.97311 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 980f7209-f95e-3396-bcd0-c32057f46d80 | -7.83222 | -52.15105 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a47d52f-041b-3ef3-8fff-e5f18dd648ca | -7.07063 | -50.86156 | 2025-09-08 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c13f9689-a64e-3c03-bdcf-31d50fc145c4 | -7.61991 | -44.66283 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f5ec1a8-5b4e-3c41-adbb-23f2bd936c4b | -10.13824 | -46.17159 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a9603e23-77a6-3d2f-a069-1009d5f78215 | -6.03009 | -45.89251 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ded5d143-d5dd-33e3-a2dc-acd801ed04c3 | -7.43835 | -45.21503 | 2025-09-08 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e216818-a8b1-3766-8b69-a65c3737e98f | -9.99482 | -51.67127 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f551f567-1078-3343-a507-72f8f806fed4 | -9.87952 | -46.53291 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 24ae0e60-dfa5-31b2-8543-c62fe1366395 | -6.87022 | -47.91791 | 2025-09-08 04:51:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| aad69633-aa7c-3704-8ab3-153552ec056d | -6.10157 | -45.44541 | 2025-09-08 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9ff80b76-e27e-3033-97fb-09fb0dd7597b | -6.28424 | -53.41682 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f51ad53-19a1-3859-bcfa-becbb2a7c711 | -9.44144 | -49.44645 | 2025-09-08 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c342858-a066-3850-a590-cd33b96aba51 | -7.74849 | -50.75957 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6fa6cb9a-c917-3865-95b3-e0047cdbdc82 | -9.94962 | -51.19779 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73556862-ff18-3082-95ce-663771fdf971 | -9.98633 | -51.68132 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ff7c8fa-aa54-38c4-8886-2f38e39158d1 | -7.1065 | -63.06839 | 2025-09-08 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 255ea216-72b2-30fb-98ac-594b1682edc9 | -9.85198 | -48.83781 | 2025-09-08 04:51:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3201807c-e0b9-348f-a087-ac28588ffa66 | -9.18507 | -46.02743 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72d99490-ae5e-36c1-bb8f-e54eb4449038 | -5.88362 | -43.96671 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 693c3293-97ce-38ea-a973-3d03399585f9 | -9.8457 | -53.29232 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 999bede6-4647-37c9-8cc5-c82dfa51a38e | -7.54476 | -42.52233 | 2025-09-08 04:51:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8926759a-820c-389b-9e2c-094de014309e | -9.20182 | -46.04537 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d76e76f2-2001-38df-a07a-0e3e7f963444 | -11.32893 | -46.56029 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c7a9481-633c-3ae4-a68f-5e7e42ab43d8 | -9.98579 | -51.68496 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90f12fb9-73eb-3d5c-b46d-81147fe2d757 | -9.85123 | -53.30031 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9946be2-f460-3631-a812-54b7e235cfe8 | -8.67891 | -50.03554 | 2025-09-08 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8a42f61-99cc-35f2-81fe-1cc863b230f4 | -9.32909 | -55.19334 | 2025-09-08 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18c54738-ad93-31ce-a269-edf8ca3cc2a8 | -6.20033 | -42.64613 | 2025-09-08 04:51:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5ccb5663-8e0b-3205-ac57-a223c6eae28a | -5.87391 | -43.97517 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5a3a07a6-8058-3cb6-bb58-c59f01023862 | -4.41697 | -47.60757 | 2025-09-08 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4aed343a-c3fc-3647-a52e-a206bf0021c2 | -6.8426 | -52.85362 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8650e8c-a936-325b-895a-01104f8f5af7 | -7.09112 | -43.88804 | 2025-09-08 04:51:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0d2f31c-d058-3223-b2ba-c79923475488 | -7.8297 | -45.42921 | 2025-09-08 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a1d8a78a-623c-3b7d-aac2-ca34c00766e0 | -5.86162 | -45.29758 | 2025-09-08 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f800a05-4303-3612-adec-7a50f514100e | -7.81138 | -52.13344 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfe9a4af-a30c-3e8d-8181-76c27f48a9db | -6.63196 | -53.36893 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 638b9a71-b488-3c65-8204-e21e120fd720 | -6.83261 | -52.80551 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c07958a0-3dc9-3457-b8c0-cdac3f25845b | -5.4513 | -43.42278 | 2025-09-08 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39eefbcf-25ea-30dd-9970-564e96a6b916 | -6.2858 | -43.33179 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c7aea6b-1df7-31b3-961d-e0fe54cebe4b | -10.14619 | -46.22015 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| bb057ba7-f7b7-31e8-a713-a9a236d278e3 | -8.49989 | -51.3334 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f96556d-2966-3a65-a4b4-402536161106 | -11.03649 | -45.94893 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d9103342-6433-3121-a10d-afcb1fd8f88c | -6.80882 | -50.8532 | 2025-09-08 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6acff65e-4c61-3ef5-913e-e192b6e418f4 | -7.86275 | -50.97872 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6d50dc9-8d3c-3bc1-a186-36218dd5c1ce | -5.87719 | -43.97467 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 35c78d0f-5abe-37e7-9b89-d078370b1593 | -7.24538 | -44.8287 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b6fe4ed3-1216-35da-94b5-49a34cebf92f | -11.39636 | -43.55313 | 2025-09-08 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| daa42c68-ea55-3d7e-974e-4c8b4ca40fe8 | -9.96469 | -55.03789 | 2025-09-08 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22b11f13-d7da-35c3-8ace-cbf700686229 | -9.079 | -50.45292 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bca16980-10d9-32ee-a217-36f4a8578c73 | -6.21216 | -51.45527 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf939f49-ebc8-32fc-95f5-8edc29d9455a | -7.08362 | -43.90384 | 2025-09-08 04:51:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7cbde1b1-84e9-3dfd-b65f-824d33a86069 | -6.30734 | -43.82074 | 2025-09-08 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e53eef6-a906-3b2b-a4ee-4abf15085a5d | -5.43743 | -42.58693 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ceb79d4d-8e59-3704-af3f-4cbb769d3ed1 | -11.14673 | -45.25523 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 434e727d-aba1-32b8-bda8-d2c964b2ab10 | -6.27432 | -53.43665 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7e670ae-e1b3-3c9b-8d82-4464b3f0d5df | -10.00108 | -51.65282 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0dc43855-be2e-314f-9b8d-ac8c73d74603 | -8.61772 | -40.20044 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9da48c61-0a44-32e3-99c8-12205763c35a | -8.92165 | -45.99504 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 844cd9c2-d3cc-37fc-aaa6-ad45072289fc | -6.10718 | -44.14408 | 2025-09-08 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 59e2bad1-f117-388b-b200-f82f1a4e09a8 | -9.27832 | -60.91185 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66ad18a1-1f7f-3fae-a974-5882e3ff7697 | -6.20588 | -53.26562 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 133aebc1-2f14-31e2-bd16-7764b21c5cf1 | -6.19835 | -43.60326 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bbb7bfc1-04b6-3402-8b45-75770b2cc760 | -10.4761 | -53.61109 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85552f56-a942-37b6-bb23-b50142031b76 | -9.44073 | -59.20488 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 9a7c0cad-e359-3673-a2b5-3efabd004aef | -7.66053 | -47.94629 | 2025-09-08 04:51:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2ca7c8c5-367b-3d68-9c7b-a6b2508cd2fa | -5.58437 | -51.91145 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8a2c8b0-9120-3f45-b50d-79ab8903332a | -9.86672 | -46.59314 | 2025-09-08 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57eac22e-e32c-32e6-bcb4-b17f8579f1da | -6.39322 | -44.47658 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README59.md)
