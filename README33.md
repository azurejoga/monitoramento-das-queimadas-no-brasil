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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6ade62a-d135-3470-ae05-6a0023ac44c3 | -4.69051 | -46.30354 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 598d7d6b-895b-3e62-8e32-5fc8cf8783c2 | -5.56661 | -47.10142 | 2025-11-17 04:38:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ab287b4-4f5b-35dc-8d83-883b7dfab585 | -4.73682 | -46.38174 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e1b6438-a605-3f26-a884-a224e9c87b14 | -4.81659 | -49.93928 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d4f4b36-8e3e-3dbe-b637-2c311717f003 | -6.50228 | -52.8237 | 2025-11-17 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a18a8437-704e-3fb7-8ebf-defa9327a9d3 | -3.59654 | -43.60238 | 2025-11-17 04:38:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 817e180b-1e5e-3d21-b18a-ba084941fe9b | -3.86385 | -49.98371 | 2025-11-17 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b9190ec-d465-3acb-bb60-88fdac4ab1b4 | -2.51854 | -47.82439 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f927f559-0963-3cb5-b7ca-fa94187cb801 | -3.00974 | -51.34485 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21e87d2b-835f-3283-ad01-427789827295 | -3.09042 | -51.54554 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 331028dd-6228-330a-98e2-8079322afe29 | -3.47236 | -54.15672 | 2025-11-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca7e85ef-52df-37fa-a7e8-5dce2b1ac15e | -6.32313 | -55.16494 | 2025-11-17 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ab860ea-bb6a-360c-a8fe-eae8ee96cf66 | -7.43663 | -48.93838 | 2025-11-17 04:38:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4973c9b9-269b-3478-be66-19061e523a8b | -4.09629 | -48.02388 | 2025-11-17 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cdb25c40-14f0-368a-9f43-6f5afa9fabaf | -2.70499 | -49.86803 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 898ed8e2-0870-31e9-8d5e-905e2041d034 | -4.10144 | -47.11608 | 2025-11-17 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d4228fd-41c0-353f-bb75-550b6cbac531 | -5.32687 | -43.03775 | 2025-11-17 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3f51da58-6efe-34f0-aac6-0e4b960a67b2 | -3.24071 | -50.50386 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92bb132a-5e6f-318a-8b3a-4a00bacd427e | -5.49564 | -41.38116 | 2025-11-17 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| aacf7eb1-5213-3a9a-b391-202438391ed6 | -2.51577 | -47.82042 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 6c198af1-2c85-3617-aabb-5c6037a9a103 | -3.35015 | -44.42843 | 2025-11-17 04:38:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2fb25b99-db2a-313b-b6cd-119969c40918 | -6.44926 | -44.21792 | 2025-11-17 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7daee9e1-bb3e-3374-81a0-6c36c61e80b1 | -7.65636 | -45.35704 | 2025-11-17 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3e32164-e312-3a91-882a-996eef4d4188 | -3.83522 | -55.80348 | 2025-11-17 04:38:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1993edcb-6e31-3c46-8b7b-3aa149c6f98d | -3.48152 | -44.74005 | 2025-11-17 04:38:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d15b001d-9b1d-3e6d-9835-da0c27cb8b9b | -4.02684 | -48.99084 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb17eb3e-1715-3097-9d95-ed73f52722a6 | -5.69962 | -45.98207 | 2025-11-17 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63d518c6-bcaf-3e17-8d80-cbde826e50fd | -2.88519 | -53.97136 | 2025-11-17 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e31dd8f1-6b14-35e4-863c-5a5a28213625 | -5.52527 | -44.98591 | 2025-11-17 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81d5565a-4e57-38de-8092-8573207b8d16 | -4.93926 | -44.53185 | 2025-11-17 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91c461d9-4b8c-3978-a234-d0524ee7d1fb | -4.65393 | -46.90066 | 2025-11-17 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f77346c-39e1-3a1d-8446-a1b3f8b4f045 | -3.39656 | -50.18484 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 668b6344-aa15-392d-991c-030f364869d6 | -4.86595 | -44.62465 | 2025-11-17 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00013ae5-3ff5-385a-9c13-08130211da9e | -3.96548 | -49.94231 | 2025-11-17 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5079267-5d72-399f-ab0e-98b82c2a8ee2 | -3.41945 | -50.35495 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36eb2874-711e-31e6-90d0-aae9b8df1b44 | -3.55193 | -41.72305 | 2025-11-17 04:38:00 | NOAA-21 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 02a5c355-b7a7-3fa9-b259-0884f3175ad1 | -2.17945 | -52.08671 | 2025-11-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edfb32b4-aff8-3037-b7f0-841cb55abb46 | -2.24871 | -53.62031 | 2025-11-17 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5f740adc-9d1a-3347-a99e-a84d1148aeee | -4.11271 | -47.29898 | 2025-11-17 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2b2fa29f-7a68-30ae-8b74-84fb7222ba52 | -4.25835 | -46.41114 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58e8b263-6812-39c8-86de-beb2799ad009 | -1.46768 | -53.41449 | 2025-11-17 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86976a97-efed-3754-82bc-38e7265f87fe | -5.05843 | -40.46686 | 2025-11-17 04:38:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5dba11a6-e2d4-3d8c-9758-b340ad9ddb4a | -3.6719 | -44.88998 | 2025-11-17 04:38:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0594e5bb-3477-33f2-85de-422040d36f65 | -5.49337 | -46.91343 | 2025-11-17 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3de7b4a-37ad-3803-89f3-83a1bcf93cbd | -3.3509 | -43.48938 | 2025-11-17 04:38:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9ff34ade-5346-3ca1-9723-419433f6ead1 | -3.40985 | -42.47416 | 2025-11-17 04:38:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d70330b4-5c94-3ecf-9e12-00c2037007a2 | -4.61595 | -47.26079 | 2025-11-17 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 299d1401-36cb-36a3-a14e-8a4dd1e55a09 | -2.46853 | -48.86188 | 2025-11-17 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 508ad6e0-cbd2-3a8a-a019-3be39b82ca68 | -4.31497 | -38.49058 | 2025-11-17 04:38:00 | NOAA-21 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eb92d525-b1cb-397b-993c-d71d7180294f | -4.65422 | -45.66693 | 2025-11-17 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7c8cdf6-4ed0-31ed-8507-0c5b0f8f19e2 | -3.34035 | -50.16878 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be169119-6731-3f97-ae40-7c3c00ed9d6c | -6.50219 | -52.82506 | 2025-11-17 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8c25c21-4208-3049-9a87-d51937033a6c | -6.85954 | -42.85336 | 2025-11-17 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5324a544-6e7d-3968-8811-3509874b9d49 | -6.22277 | -47.23687 | 2025-11-17 04:38:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cbc0004b-e1db-368a-a2fb-fe5c8f71eb61 | -4.76645 | -44.42583 | 2025-11-17 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ac9e2a0-4eed-3ecc-bf60-c45fafe649e8 | -2.52185 | -47.8249 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 087bb98c-d982-382d-b9f5-a067277f1cc4 | -3.4749 | -49.6882 | 2025-11-17 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58da60e8-93e6-3bb5-9be7-67b55251f162 | -3.33719 | -50.27543 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0f9a908-9304-3091-9972-e55393c52a37 | -2.50968 | -47.81593 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 69ac2c58-e57f-3c19-a3ca-e054a51597db | -5.87963 | -48.32288 | 2025-11-17 04:38:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 025b07cd-dd03-39cc-b064-9f1ed00f47f3 | -3.77526 | -47.74877 | 2025-11-17 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f623f864-ba46-3fa1-8f42-c5a98ae4fab4 | -3.78158 | -49.25235 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0455ceb4-9360-382a-8466-413ec1515e5c | -4.7292 | -46.38468 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8c2a817d-3be2-38a3-af3d-ab3630b6c740 | -3.21988 | -43.36298 | 2025-11-17 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6506f408-3da3-388a-93c1-ea9a86178cc4 | -1.877 | -46.36681 | 2025-11-17 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ac97b1c-84b5-310f-a14f-a84d4ade2336 | -2.86935 | -51.47521 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15c8097f-8154-3c02-9ee7-2ff7554d58e0 | -3.85437 | -51.14784 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3bd806c-a9b4-3ae7-964f-4e5df9600137 | -4.81624 | -45.39123 | 2025-11-17 04:38:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1013a015-dab4-345f-b9d7-0b91563ece88 | -6.70397 | -40.7929 | 2025-11-17 04:38:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8c7c5eac-5ad8-3642-8bc7-4161e198c97a | -4.69574 | -46.31628 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3106b04-30cd-3bb7-81ab-f680c63d6b6a | -5.09796 | -46.07841 | 2025-11-17 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5efa2b70-1b89-3f30-a84d-a026c7a646c1 | -4.69775 | -46.30747 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc6fa74f-36e3-31bc-a394-b588d3525171 | -9.06646 | -44.78999 | 2025-11-17 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4571d64e-fece-36d9-aea6-0cce3db04e17 | -12.85674 | -46.46478 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 511d7e13-adcf-326c-acc9-518fbaeb588c | -10.85744 | -44.88223 | 2025-11-17 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a62ee698-dbb9-336b-b546-2a6b62cc6f22 | -10.66324 | -49.376 | 2025-11-17 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2b439c29-afde-3921-9b32-b915d06f6348 | -11.84653 | -49.21823 | 2025-11-17 04:40:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b059d635-a235-36fc-be6b-8feced0349db | -9.32678 | -46.57633 | 2025-11-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f9af4ea7-d3c9-35cf-b853-efef389c2fa0 | -12.96753 | -49.97287 | 2025-11-17 04:40:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5bf7906-8f57-3d38-9d5b-102967971946 | -9.32788 | -46.57071 | 2025-11-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9960d5aa-9b97-3181-a8bd-40a4612d4684 | -10.79529 | -47.64448 | 2025-11-17 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60328ab6-9172-3b02-a2c1-9c19acb1103a | -7.81305 | -55.06886 | 2025-11-17 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f3b0a45-0f1d-3768-9dc6-e25281161c94 | -14.4945 | -47.98049 | 2025-11-17 04:40:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73be5750-a982-33e6-9d31-a610685be570 | -9.73759 | -43.96606 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d9d6746-3050-3c40-b019-679aa6260d9a | -9.48757 | -59.457 | 2025-11-17 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2360a166-5bae-3eaa-8dd3-43045931e59d | -12.85224 | -46.46889 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 46fe2446-440d-3df4-98fd-12e61c96b483 | -12.79379 | -46.44979 | 2025-11-17 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 491d3601-beb9-36aa-ae8d-ec392e1a0e1d | -14.65259 | -46.53252 | 2025-11-17 04:40:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e67ce310-b1d6-3395-ab0e-9faab340ec6d | -12.20443 | -49.63214 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c152a60-364e-33db-b83d-be0dcf8f1af0 | -10.95357 | -48.70346 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6011c75f-498e-3120-9ec8-9ba9b55c807c | -12.23057 | -49.61788 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c30dd63e-9d11-330f-9f30-53c3d804a22d | -12.87128 | -46.0397 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e52c535c-1ccb-37f7-a6e5-12e0bcb099ff | -14.65068 | -46.54671 | 2025-11-17 04:40:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62857266-6ebd-3900-89bc-439f0e53123c | -13.55223 | -47.38314 | 2025-11-17 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f20070d-9bcb-3f9d-aae4-d1043b51d90c | -9.15379 | -48.0677 | 2025-11-17 04:40:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c12bcb70-011b-324f-a251-f1889d3fda77 | -11.40558 | -43.32851 | 2025-11-17 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ce1b0bb7-472d-3400-b76d-c55e70134bd1 | -11.71584 | -48.86019 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fae3652-7814-32db-a7b1-d1804a9e2246 | -12.70191 | -46.77008 | 2025-11-17 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cd766a7c-8dc9-373e-865e-6c8d94a7e4aa | -12.87936 | -48.28062 | 2025-11-17 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44e0bba9-6713-3059-850c-27482fef485f | -12.22778 | -49.61377 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README34.md)
