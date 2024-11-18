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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0797ce2b-228d-3da7-aee4-777db75ab01f | -2.56186 | -53.99199 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b91aec3-3dce-38dd-abd9-4cb1b41d9d23 | -3.52083 | -52.10686 | 2024-11-18 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7877e81b-3041-31e4-a309-a929b277bcca | -3.33341 | -53.35566 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a9c0f067-182e-3d51-9aeb-2b2c0b1fdd24 | -1.62632 | -53.29725 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e0365b7-b2a6-382f-8127-e21566ce3def | -3.33683 | -53.35619 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1d46a930-ea9b-332c-850f-baac0a427d10 | -2.72699 | -53.19297 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16cfbdea-dc37-3488-bbfe-b78440c7384a | -2.23103 | -53.60667 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5167c301-cc1c-3fa7-9b2f-9ecc96d713c8 | -1.22352 | -51.78902 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54ca3b3d-282b-3ed5-a0b7-d1f7e56f46f5 | -1.2134 | -51.78328 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82bdd52a-04ff-3fa3-b806-5542d7344faa | -3.37395 | -53.32015 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f88049e-0f97-3953-a627-d90a4652e422 | -2.46097 | -53.94045 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93703913-e6b3-3712-a66c-a4bb6f0339d9 | -2.2344 | -53.6072 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5a5c9c7-2040-35bf-850e-c497380e577c | -2.86564 | -51.78628 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 600093f5-9f9b-372f-b00a-8610c1f86023 | -3.19094 | -53.23174 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c915b70c-940b-3cac-9b42-ac37f3d434e8 | -2.71474 | -51.86615 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b96f663c-cecd-3049-9d63-123e578c8421 | -1.46422 | -52.35787 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfd6e1f0-3fc6-3a20-b51e-b99079e1134d | -2.6119 | -54.2616 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47449e4d-f775-33c8-87e2-e94d6ad0bf9a | -3.10884 | -53.74795 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b39e9d2a-5ed8-32c7-b644-fe043d5100d4 | -2.54904 | -53.98637 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89b11c17-a8a2-3577-958b-93b534374638 | -2.60078 | -54.37745 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fccbd43-a00f-3875-8725-a14f02fa0ca6 | -1.67482 | -53.83726 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 85b86f7e-ff4e-3b4a-bff1-ca62beb64fb9 | -1.72919 | -53.26803 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 192e207f-3266-38a4-8116-abdf0bc4d147 | -1.90622 | -53.3284 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38abad0c-6576-3e18-bcda-7bd448e8601d | -2.23173 | -53.73473 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06127fd2-44ea-320b-bf14-048144643e09 | -3.66698 | -50.44593 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4a489c1-1fbc-33ce-8ace-c6f72a8e7edf | -3.57369 | -50.56262 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27b91aaa-db7b-386b-90c9-7f1571a075e4 | -3.1921 | -53.24727 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cc53ac1-0965-3d80-b674-3f2990626d2d | -1.62237 | -53.30036 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cf73d317-1261-3105-972e-58ab98411109 | -2.9646 | -54.3124 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06e62714-fc8e-3e97-907e-68b7f90898db | -3.18867 | -53.24674 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f58a350f-9b68-326f-a18c-0a41f71385fc | -2.87872 | -53.96467 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1eee7ae-8725-35d8-b26e-2743d93edfb9 | -3.08056 | -54.66155 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8b33dff-9dc0-3b4d-b7f9-a50b511816b6 | -2.60148 | -51.79879 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 50ed961d-5fb6-33d6-9ece-a88c61de5180 | -3.06494 | -54.41058 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e2863f7-639e-3803-965e-ca5ed7d151a9 | -4.95009 | -44.84675 | 2024-11-18 05:03:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 383734a4-4727-3e9a-bb5d-082878f7800c | -2.28846 | -53.62623 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6ffdf62-4536-3cbc-b39e-a4fb51cdd954 | -3.0627 | -54.40307 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bb2d35ce-c674-34c0-92e7-06af8b913847 | -4.10898 | -51.05927 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b8f19f0-5867-3b9c-ac76-ab3bc47d732b | -1.67816 | -53.83777 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 01db1dde-6d14-3b59-9041-2c141ab1dfab | -3.3839 | -50.33182 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a86f818-7707-34d5-a51b-2b5f7aa80149 | -3.53395 | -50.25201 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a34a8f9-9cb4-3c3f-8379-6bdce6bdfb08 | -2.33959 | -54.59228 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad1e18c8-50a9-32af-aa1a-31105b7ad04e | -2.47316 | -45.61922 | 2024-11-18 05:03:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65607e86-3484-344b-8dd1-5c1d05195239 | -1.14214 | -51.69641 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0572ff68-01bc-37f0-bf0e-d59bd85e692a | -3.08002 | -54.665 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb087424-68c7-3c71-a170-ca3fc1dfdaf5 | -2.97433 | -49.11304 | 2024-11-18 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 919bcf56-f12c-33eb-866d-c85e79733f7d | -3.19809 | -54.32009 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffe1bc6c-1bab-3d73-8d3a-b770a4a9095b | -3.55523 | -54.58243 | 2024-11-18 05:03:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af180d4c-ea43-39f7-b049-fe96a13df6fa | -2.35826 | -48.56816 | 2024-11-18 05:03:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbe9801c-49d4-34b0-9dc9-94e37ccd2a05 | -2.34344 | -54.58933 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea881774-9565-3c69-b649-739355829699 | -2.4604 | -48.81434 | 2024-11-18 05:03:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ca56f54-3b63-3c69-b125-c26e439efacc | -1.68395 | -52.69995 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f55ec047-71a6-33be-8d91-999fbc3392a3 | -2.59759 | -54.02634 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 498dd49b-5825-3035-b82f-8ca26474811d | -1.31897 | -51.87341 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf4e43c4-9d04-3dd0-a839-8fe213378238 | -2.86994 | -51.78255 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 16b6cdf0-3168-3624-8709-5b4c35712ae6 | 0.29341 | -50.84883 | 2024-11-18 05:03:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 703700e9-4dbe-336c-8720-6648d096c8fd | -1.20878 | -51.76576 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ee1051e-a3f0-3596-afee-b4a9b0c0b2f2 | -4.10125 | -51.05789 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0ea6332-013e-3981-ae25-6302cef309a4 | -4.27545 | -50.58631 | 2024-11-18 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 39858352-4da4-394f-9bb0-c7d399cac9a2 | -3.69621 | -50.11076 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54b54b6a-d61d-3d22-bebd-beadd89f1b5d | -2.8451 | -53.96692 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d99c70f-98fd-359c-a2fa-dbd6f59491f4 | -1.14489 | -54.13767 | 2024-11-18 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4385e4db-bcdf-3167-9b8d-1da830385683 | -3.66349 | -50.44186 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f1a75c08-217c-376b-842c-696021a7e46a | 0.61253 | -51.77378 | 2024-11-18 05:03:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d75340ec-92a1-33d4-baa9-385a1d3fd7e4 | -3.57733 | -45.20541 | 2024-11-18 05:03:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6a33067-9bbb-3b27-84cd-19acce40843a | -1.81302 | -46.52962 | 2024-11-18 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b04b9c25-e207-3e41-a2d1-189e616f0478 | -2.60768 | -54.04945 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e841806-6c65-3f1a-9752-d02de233adb4 | -2.30086 | -49.13195 | 2024-11-18 05:03:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3855ffc8-3c4a-3966-88e8-8b733ca0603e | -3.18143 | -53.24949 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e7d8177-6367-3eb8-9130-cb2a2c1a06dd | -2.68469 | -52.98707 | 2024-11-18 05:03:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 705ac15e-147d-3d8e-9c24-218a806df4ad | -2.2423 | -53.66703 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39f65359-3fa1-3bd8-8a28-b8672dc82075 | -3.14569 | -52.97758 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f16a7c4e-eca3-3100-bd1f-1bcdead33d96 | -1.48659 | -52.09924 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 422ebe2e-8e1b-391a-ac4a-d8b171a42621 | -1.09357 | -51.73626 | 2024-11-18 05:03:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 685f1dbe-92ce-37eb-b07b-42eaa56bf8fb | -4.78616 | -46.48425 | 2024-11-18 05:03:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 815512d8-8ed1-32ec-bd6f-cd43ff4703c1 | -2.24286 | -53.66346 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00b9e835-3818-3b20-9ffa-23c9002dbad2 | -3.08719 | -54.66256 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cc1ce8a9-d473-3cf7-99f3-95cd13af9f28 | -2.55074 | -53.99749 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90420700-5ef3-3ceb-9e12-ece217f1c6b0 | -3.03942 | -54.39949 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 701b80e2-b708-3a35-9729-10d806b58b2d | -2.81901 | -54.02445 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d29cf748-2fba-32f9-9681-fdc25039c43e | -3.18765 | -45.44113 | 2024-11-18 05:03:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12521647-41de-39eb-8faf-9bd1a7a0af26 | -2.6692 | -54.57287 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fc64597-5601-3164-926f-d71a5284408c | -2.67801 | -46.21995 | 2024-11-18 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4a74269-dc79-3f3d-bfbe-7b51575bec5c | -3.39921 | -53.27066 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6508be4-c24c-3db9-8e15-58970f347fb1 | -3.65951 | -54.65543 | 2024-11-18 05:03:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f9b16a4-aea2-318c-8d94-4ec524f3c832 | -2.60729 | -46.2614 | 2024-11-18 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1289f1e-6fb0-381f-a018-ec4069fa3dcc | -2.82455 | -54.01084 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6e646969-6801-3263-8441-e32200a2946b | -3.45101 | -54.68388 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 039674cf-45a3-3863-99b5-5228f5213f9c | -1.32254 | -51.87396 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f8722eb1-ada5-36bc-9b27-e8af9f9fbb89 | -3.04275 | -54.4 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ccc9cc12-80f9-37a2-82b2-9cbd4cb2d88b | -1.76247 | -50.74675 | 2024-11-18 05:03:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f6ba6c5a-6177-33cc-a333-0fed4757ba75 | -2.36858 | -53.67848 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae79bcc7-9a7a-3043-9a10-7adf09d5687e | -1.61179 | -52.48561 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb859514-1a3f-3030-b1c8-eed5b3f233bb | -2.59255 | -54.01475 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f4d1a57-9c72-3292-9cd8-201427560a1a | -1.21232 | -55.82023 | 2024-11-18 05:03:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b055e52-a7c5-31ae-85ce-088014fc62bc | -2.86656 | -51.77974 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4b326a40-5546-3e8b-80ad-de415c63c107 | -2.36272 | -48.56884 | 2024-11-18 05:03:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89f892d7-3410-33e0-a9b2-1f979e5ab3a4 | -2.25385 | -49.04741 | 2024-11-18 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17d2831d-cfe0-3060-9577-ee619dfc4099 | -2.86627 | -51.78202 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 27c3778e-426e-3f72-96e3-c64fd63576bf | -2.8659 | -51.78399 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |


[Clique aqui para ver as próximas entradas](README37.md)
