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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d92c291-dea7-35af-a9fd-84d4c4faec5d | -4.65374 | -42.52192 | 2025-11-03 04:50:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0552d15c-ce73-3bcc-959f-d0cc95db62fb | -3.43293 | -45.90316 | 2025-11-03 04:50:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bbbead75-7585-39d0-bd4e-cfa0d07a51b2 | -3.14427 | -50.20218 | 2025-11-03 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 195e584a-d158-318a-b2c1-f3a4d8b52797 | -3.24491 | -50.79694 | 2025-11-03 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 914a08d5-6678-335b-96dd-2a6a6fa62bca | -2.8031 | -52.90574 | 2025-11-03 04:50:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 397dd8b6-23a1-38f3-8bfa-b70b8f991d52 | -5.26758 | -50.9645 | 2025-11-03 04:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a60a7c34-ca15-35bb-b62c-bc5451730a92 | -5.03506 | -43.62178 | 2025-11-03 04:50:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90ae8795-c2b6-3623-baa0-024b273571e9 | -1.261 | -53.84079 | 2025-11-03 04:50:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0396a3bf-5364-339a-b028-4d21b1c9bdda | -2.80366 | -52.90221 | 2025-11-03 04:50:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75af3e2c-a41e-30ea-9869-9b03f8d9789b | -2.91182 | -54.02488 | 2025-11-03 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9cb52a81-fa14-3d11-846d-edfcf7d9f7fe | -2.31277 | -48.58461 | 2025-11-03 04:50:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad8cec5d-b3b8-3ff1-a30a-38749f762f83 | -5.71732 | -42.19005 | 2025-11-03 04:50:00 | NOAA-20 | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5d128ade-513d-3cef-a9dc-5ca09e545850 | -2.26855 | -47.86094 | 2025-11-03 04:50:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1baadfbe-a279-3cba-87b1-944ae82bf5c6 | -5.02946 | -43.62403 | 2025-11-03 04:50:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5388c90f-1d44-3c4e-98fd-b4bd482cd4ca | -3.24158 | -50.79643 | 2025-11-03 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 304cc35a-81a5-34b8-b58f-de63eb5fdc10 | -3.02066 | -49.43834 | 2025-11-03 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42858cb9-063b-38fa-a8d0-9aa68746800f | 0.98904 | -51.29229 | 2025-11-03 04:50:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5a8b4e1-a83a-3e6e-b4fd-483b5aaeb97e | -2.73741 | -49.39281 | 2025-11-03 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 238541b4-59d1-3d60-90c9-adfaeba5166d | -3.84329 | -51.31523 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b4d107a-f45a-3298-aa6c-23afbb940466 | -3.68812 | -49.42617 | 2025-11-03 04:50:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60482087-7bb3-3838-9973-c1b777c9d69c | -6.84783 | -46.2915 | 2025-11-03 04:50:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8131ee78-3518-3f37-86d0-293d95d2c031 | -2.53702 | -54.73966 | 2025-11-03 04:50:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7f79ac2-2f4f-3aba-94c6-2d6ab3ec761f | -3.83335 | -51.31368 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80aebf07-d2bf-3976-89a2-203aef986d8d | -2.60759 | -54.32292 | 2025-11-03 04:50:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fd43138e-7a96-312b-940a-9e6b3b9c8984 | -3.17285 | -46.58615 | 2025-11-03 04:50:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f89c082-72ba-3195-9067-b61e98b3e87d | 0.99751 | -51.21708 | 2025-11-03 04:50:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc91e884-4495-38e5-b114-215acecfb228 | -3.46376 | -50.22078 | 2025-11-03 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d511e5a9-f557-39fd-904f-474f57731d08 | -2.82972 | -49.40671 | 2025-11-03 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d14bfcb-7ef0-3575-be36-a8051704b76f | 1.00742 | -51.21553 | 2025-11-03 04:50:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66a2988e-c49c-3fa7-a339-68a6ca6859dc | -4.70666 | -46.45103 | 2025-11-03 04:50:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa94aa42-b9be-3a37-80e1-98ba9fde54ed | -0.86564 | -51.88019 | 2025-11-03 04:50:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b8052b7-6210-31ac-9d43-c4beedb26644 | -3.77123 | -51.79508 | 2025-11-03 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96340db1-a32c-3a05-befb-0de7d4efd879 | -3.29995 | -51.91809 | 2025-11-03 04:50:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19ba5971-130f-3028-bd4f-b24f6105ca39 | -6.69038 | -46.67227 | 2025-11-03 04:50:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c065349-f226-382f-ad58-2d1963659c35 | -2.30918 | -48.58407 | 2025-11-03 04:50:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efcd7b49-a354-3753-aaf5-edd256738456 | -2.88056 | -52.61241 | 2025-11-03 04:50:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 680a993a-d6eb-3434-9fdf-2fcc4fec7ddc | 0.86376 | -51.25242 | 2025-11-03 04:50:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f79414d6-e74a-3e69-a33b-9b6f5b3e945e | 0.86707 | -51.25191 | 2025-11-03 04:50:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aeb25e80-4dd6-32d4-89eb-9f017629d827 | -3.07767 | -51.1709 | 2025-11-03 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d924cf0-8f2d-3223-b97f-67136edc81c6 | -2.49266 | -48.14583 | 2025-11-03 04:50:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d147a447-8f8e-35e9-b0aa-774cded4d83a | -5.0355 | -43.61873 | 2025-11-03 04:50:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d6f5a0d-55ed-3921-8d43-53c2c4d47c11 | -3.14088 | -50.20166 | 2025-11-03 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3d43459-5979-3848-8864-e88ce9ffbf2b | -5.0402 | -43.62263 | 2025-11-03 04:50:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4d5dbf0-f60b-3d29-a564-0d943f0a366a | -4.70245 | -46.45033 | 2025-11-03 04:50:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44522c74-3d25-3f02-b176-5eefa6a1d74d | -3.55693 | -54.5713 | 2025-11-03 04:50:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 450bf451-a530-3277-95dd-c5dc984bbbea | -2.49567 | -48.15069 | 2025-11-03 04:50:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be82da90-c137-3607-b38b-8c5a4a2a73c4 | -3.08384 | -48.67667 | 2025-11-03 04:50:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3584c5c3-860c-3192-9990-8a2075390c4c | -3.5563 | -54.57523 | 2025-11-03 04:50:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91f7f651-1152-3edf-8edf-13999209c73b | -3.14745 | -51.35491 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a838c70-ad9f-330b-aa82-33e25d8bc2cb | 0.45802 | -50.88066 | 2025-11-03 04:50:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3de5da28-b9b8-3254-b278-928af14c97a9 | -2.84073 | -49.40447 | 2025-11-03 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0a43d9eb-cf7b-3cff-aa76-604d3d205778 | -3.69162 | -49.4267 | 2025-11-03 04:50:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4664ee37-69bd-319b-8534-34b03e566bcf | -2.9448 | -51.41165 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 404b5979-76b2-3502-89fc-116c5548049c | -2.90883 | -53.95451 | 2025-11-03 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f89e9c12-9c45-3188-9cc5-287ce25a7a39 | -3.43268 | -51.50574 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bca4aaa-8b26-305f-aa1f-87adcafcc28a | -2.94426 | -51.41509 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dd86aea-85d3-3224-93b6-4fa67d325f6d | -2.26482 | -47.86039 | 2025-11-03 04:50:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14f2604a-20dd-318d-9435-ef647d1bb01f | -1.26221 | -53.83319 | 2025-11-03 04:50:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6c1e2f9f-cd60-34aa-a032-a56a68dba9ff | -2.83319 | -49.40725 | 2025-11-03 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4291ebef-22ed-37bc-a951-7eb76530e916 | -1.94139 | -52.70908 | 2025-11-03 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 360e7472-11bd-33b0-bfcd-8ea455e4f19f | -1.26161 | -53.83699 | 2025-11-03 04:50:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a3611f2-ee17-30be-aa25-b336463c8689 | -2.93574 | -54.17732 | 2025-11-03 04:50:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eeddaac1-d94f-31c0-b04a-34f0b18973ac | 0.86431 | -51.25586 | 2025-11-03 04:50:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7d31e968-7b23-357c-ac8b-c834454ed9b2 | -5.03975 | -43.62572 | 2025-11-03 04:50:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8c23c36-7688-3e75-a12a-f01c96534643 | -6.84718 | -46.29589 | 2025-11-03 04:50:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 83a27f75-8caa-3020-97de-6a9520615453 | -3.55846 | -52.87999 | 2025-11-03 04:50:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4bed058b-d96f-374f-bdab-d817f2a184e3 | -3.07845 | -51.25246 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 516f5432-6c35-3378-81d5-0b90af491459 | -5.03461 | -43.62487 | 2025-11-03 04:50:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58c825af-b790-3072-b90a-03db56e0e5ca | -0.8926 | -52.033 | 2025-11-03 04:50:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 128ce020-c5b5-3360-8d5b-1ec15fd9a4c0 | -3.02651 | -47.79607 | 2025-11-03 04:50:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ae6554c-23f6-322d-b15b-7356cced086e | -3.43757 | -51.47476 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac614f03-1c88-3a6a-a003-5ae7c676256d | -2.09304 | -49.97536 | 2025-11-03 04:50:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 982e37ea-72d1-3163-9fef-f31c3604e7ac | -2.9415 | -51.41113 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b2cced5-66fa-3540-81d2-d87d2be4a045 | -1.25115 | -53.83532 | 2025-11-03 04:50:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24dbda8d-eeb1-359e-a47d-d53c4b680fca | -2.44973 | -57.8964 | 2025-11-03 04:50:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c216c5f-894e-342d-b64e-e0bb7a162008 | -3.07623 | -51.24504 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b371b0aa-b981-3422-be3d-60534bdcb5d2 | -4.79301 | -50.71229 | 2025-11-03 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 97cf7bb2-a7ca-30dd-91ed-fdade83deb65 | -3.42265 | -51.2247 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eef0177f-dc40-3f8f-9a9a-2352d7d0cab2 | -3.65596 | -54.58599 | 2025-11-03 04:50:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f3b45b9-ab3c-3bab-8a68-d577b87efd6c | -4.65977 | -42.5192 | 2025-11-03 04:50:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c710bf2e-3215-3075-be2e-ca471983cd31 | -2.49199 | -48.15015 | 2025-11-03 04:50:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16dd05c3-b2ef-3874-b523-e0aff51cefdd | -1.97128 | -52.11026 | 2025-11-03 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3438a7e1-3448-3707-849e-f38a2751cd83 | -2.91009 | -49.81431 | 2025-11-03 04:50:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa0b548e-2a46-380c-a6c8-9478411b27b5 | -3.06665 | -51.37074 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 802cc26d-7541-3a08-863d-c85e12f57d35 | -2.2883 | -47.8665 | 2025-11-03 04:50:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43d1399e-b18a-3b34-8891-291e7a467858 | -2.92953 | -51.46565 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cb2daa8-82d3-3f27-8e8e-df798641dd3f | -3.65532 | -54.58993 | 2025-11-03 04:50:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96f3e189-52e2-3451-b29d-0a649c5882ae | -3.0166 | -49.44162 | 2025-11-03 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f976f3b-30eb-3c18-b538-2f6b6d6c7751 | -2.80422 | -52.89869 | 2025-11-03 04:50:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f96b3711-b689-3418-9288-f13e6a672903 | -2.96627 | -54.07615 | 2025-11-03 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17c7ba65-fc8e-3f4e-b413-a2553bf6a19a | -2.93922 | -54.17789 | 2025-11-03 04:50:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 462397aa-38cb-38e9-abf9-0f94774f5bc0 | -3.78674 | -50.95987 | 2025-11-03 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef66cd87-9aa6-3ba1-8f57-e7017fdadbb2 | -3.23106 | -50.00296 | 2025-11-03 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a05e0ad-3b84-306f-a187-bd5a1350cd1f | -2.92713 | -51.30618 | 2025-11-03 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea4a6587-f99e-376e-aa44-753e38742d94 | -3.26676 | -48.84953 | 2025-11-03 04:50:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f49a8a4-d730-3306-b9c8-81e514173d4d | -3.42801 | -45.90658 | 2025-11-03 04:50:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a2b9047-db1f-367d-83f6-2414866eaa4c | -3.24103 | -50.79993 | 2025-11-03 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03c83e0f-a423-3f7e-abd5-7554f5c9e552 | -4.10805 | -51.09999 | 2025-11-03 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d98c1102-d1a6-3d51-89a1-d57e67f2d81e | -2.96049 | -47.0037 | 2025-11-03 04:50:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f19c06bb-35f8-3f84-9fd4-d617132c2e60 | -1.944 | -54.14697 | 2025-11-03 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README10.md)
