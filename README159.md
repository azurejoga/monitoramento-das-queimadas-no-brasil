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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe16e3df-9f9b-3b01-b38e-389bf9364dd3 | -2.49565 | -56.06708 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aba6f436-8272-3b90-a071-38d0503eae7a | -3.96328 | -56.11596 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 201dd881-6289-3a38-b637-4a530a42effb | -3.00399 | -54.07051 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 2d0f93bc-0a7c-37fc-bb2b-555d595ea081 | -1.28222 | -55.41809 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c52c38b1-37de-3d79-9c62-a8fc9f6c4fd7 | -3.64768 | -60.63117 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5272f5b9-1b9d-38bc-b94c-862b8f38faa7 | -1.44926 | -54.46789 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a35eadb-58f1-3b26-a317-fad586b5ee5c | -2.856 | -59.11499 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cb8097dc-4d46-3b3f-a86f-427dc2f515b6 | -2.77681 | -54.07218 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 13666e9b-b0cb-3614-a80b-2d1f8babf0d9 | -10.17947 | -59.25908 | 2026-10-08 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 124e358d-da1b-3bd0-be2f-91dce5f41d3b | -3.15394 | -54.10054 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f974361-6ba4-3c38-bcb3-584e76043bca | -7.22187 | -55.12022 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cecc3f8c-5a34-3c89-a296-01cfed4dc3d7 | -8.72041 | -45.18224 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 72f1e419-4b4c-3a5e-84bf-0085f13f9e8d | -3.07562 | -53.95779 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 70da7d9f-5768-3725-b0d2-3324cd549476 | -3.25453 | -54.65828 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e71b24ca-f98e-3c14-b4cc-e53732c9b5b4 | -3.4631 | -54.59431 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 604da402-061d-3624-8b4b-1749b827e653 | -3.59054 | -55.56178 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c24d7cc-5813-3e32-9934-e725f4667301 | -3.05105 | -53.92985 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9418b674-ceb0-3354-8bd0-0b1d094a5b08 | -6.72747 | -55.10628 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 382ffaf5-9834-32eb-88bc-9310d63d7099 | -2.78792 | -54.06993 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c78eeae-bb25-339a-bb06-86945cb073b0 | -3.5181 | -54.67183 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1934f04-2d15-3b40-ac85-e2a1888d4f62 | -5.69782 | -53.49841 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c88b11c-a8a1-380a-9afa-3cc6214cff39 | -3.02373 | -54.10529 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f4313d42-f574-3728-b5db-737ebba751f2 | -2.57792 | -56.14359 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1488e9e-d447-3391-863f-f84d5d4d9820 | -3.72108 | -54.23074 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9da82a2a-381c-3d51-8ebc-dd7a9c8d812e | -2.50074 | -56.12104 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06e2863c-2bd0-38e5-b7f9-19d2895606e8 | -1.50568 | -54.83907 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 498a6662-cf3e-3368-8d3b-205b9ddb40af | -3.44659 | -56.93951 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7db00d92-edd1-3401-8fbe-5d9b30955136 | -4.27596 | -55.71516 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30d115ba-48e3-3489-bca3-43e1ea3b1527 | -3.19823 | -50.56585 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d038c183-492d-3f5b-a2f3-ccabdc258e90 | -3.66202 | -60.61464 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b7297bc-286c-3935-8e41-52a19dc63c64 | -2.10818 | -52.06762 | 2026-10-08 05:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6165795-fc2a-3618-a818-cbf1f767d521 | -3.99263 | -56.2488 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d1d2938-e87a-3cce-b9c3-c99489801832 | -3.01191 | -54.13512 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d5e3c4e-c1dc-3cdc-9131-5767d408a9a4 | -4.46595 | -54.97096 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c1c8ed8-fea7-3030-b0fb-48c6141bfdc8 | -2.47021 | -56.09854 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77a5b8ab-dfdc-3f27-9400-14b7fb0a39e5 | -3.30665 | -54.04759 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bfbd1fe5-0a60-3445-a272-a789cdb3a273 | -3.8382 | -55.98579 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e33d648b-37bb-3e31-b496-558549744332 | -9.48462 | -64.35379 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cad29d1e-ad9b-3362-9783-2cb3421c6daf | -3.25131 | -56.80607 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fae3ecf0-6036-3b1f-ab22-d438950979d1 | -3.1047 | -54.27815 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c14b4cb6-384a-3ed9-95dd-4c4e8e423f28 | -4.11424 | -54.01905 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb521e4c-d3b2-363b-8627-1b760b9a011f | -3.19084 | -50.55638 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1eb76c88-4d15-3ff9-9c0a-5ce8a9e5b665 | -1.20294 | -55.68671 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fdf87b20-be96-3ce1-a276-3704433abebc | -2.99167 | -54.08049 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 366bccaa-2a02-3060-9525-90d641083ecd | -4.07055 | -59.83627 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 68a56f0c-a355-30c4-8a15-ee8bee1c6f29 | -7.66531 | -44.94609 | 2026-10-08 05:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f22f4c3-5869-3672-826e-fc51c9ebc531 | -2.8825 | -54.20168 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 72de3a5f-015a-358f-83da-7bd29c739836 | -3.27249 | -54.05834 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 11cc0c2f-baf5-380f-8e4b-8360dcbae828 | -3.00782 | -54.13843 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8285e3d0-533a-3411-afcd-bbb355a09fee | -1.10836 | -54.15322 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad0b95e5-0aee-36cc-aaff-b24e1e3d1c8c | -3.1783 | -57.093 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77a5148c-6b60-3187-8df9-49932fc98bdd | -5.01187 | -49.94155 | 2026-10-08 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00dcecfb-f63f-3648-a3ee-4d2a1dc03adb | -3.28215 | -54.01975 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ebd6e8d-877f-3d1e-929c-05b260b2d501 | -1.50624 | -54.81353 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8175b7d-42d7-3f64-8ab4-2c48cdc8df4a | -3.02324 | -54.08542 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7a389919-d594-3c62-91d4-7c7720142c84 | -4.26239 | -54.86754 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9fafbc68-e2d0-33f7-b20d-6707393d6811 | -3.17135 | -50.4522 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 202e0c12-0348-3537-ad7d-8dd9fcc0dc6b | -2.77119 | -54.08008 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 621cf5ad-cf59-3f57-8dd6-86a03f98c797 | -3.28428 | -54.05217 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba8cdcee-1e3e-36df-80e8-cc1936387cc4 | -9.48022 | -64.35297 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9581e7b1-381f-391c-9e8c-a1f61a161966 | -2.83958 | -54.12925 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec0d7bbb-7cd2-3eea-86aa-687e89229afd | -1.124 | -54.1214 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a5480a0-cf07-3a1e-bd09-097095f253e3 | -3.28842 | -54.0488 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72fd80bc-1cdd-3a12-be25-57a59f00c7a6 | -8.53331 | -66.9757 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5287042a-f845-3d52-9ecd-1c01f754b96e | -3.99431 | -56.25974 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68f2e406-6694-3297-acbb-8ee870ffae87 | -3.30983 | -53.86632 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| efe09e35-c319-3a87-a7e0-a386cb981447 | -4.34589 | -55.13325 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d0f4b4a-010a-3573-958c-5e8d3c6100d0 | -2.7622 | -54.11412 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5fd06d2b-afdd-3bbf-932c-9564ff1ab847 | -4.17286 | -56.34858 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b060717-4bad-373d-95ba-c04576d0b7c1 | -2.99697 | -54.06942 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a463bdbc-5894-3586-ab8e-927fbd20f771 | -2.91671 | -59.31551 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a6b0baa-68c3-392b-9b83-ec86f9d6eede | -3.04386 | -53.95285 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4460adc0-c346-3b42-a4d1-06b209aba2c2 | -3.06838 | -54.2539 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6b6c389-0867-365e-aa35-51a75cd425d4 | -3.28703 | -54.08051 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d1937c4-4a9f-38d7-baaf-6490badb7f7a | -2.72398 | -57.46241 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d5799054-8462-3d33-9c15-401894585529 | -3.50424 | -56.9202 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 6f123b94-da5f-38ae-bbc3-4cda07dd0bc4 | -3.09472 | -57.63671 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad5819b4-e1aa-3d15-9843-32a9d4c98efd | -3.01832 | -54.14003 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e787e103-79b4-345b-9348-1b0a94fa6a73 | -3.46978 | -50.08543 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed737e31-7f29-39c5-9371-bfdaea793b7c | -2.97845 | -54.04684 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e481b647-739a-316b-86c2-fc53df5f4027 | -3.3199 | -54.05248 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a84c14b8-b325-3ab8-a8ad-1c76e7913b8e | -4.24675 | -50.74433 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf79139c-2227-32e0-a95b-fe69622e4f73 | -9.48902 | -64.35459 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bcbf4726-6742-3b6b-90e3-8b66cfa4d835 | -3.15043 | -54.1 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89f83870-dc48-3cc4-bd98-fe0b16fbb234 | -3.42474 | -50.43602 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7bf32aa-c2a1-37a0-bd34-de23c3fcd12c | -3.57035 | -54.48679 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c8333e78-d9cf-38a5-ad7b-d667e2151678 | -3.3166 | -54.05316 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ee76106e-116c-36a4-9c64-7fc3c1752585 | -2.99927 | -54.23931 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47fb106a-d8ff-369d-8d1a-7d0e40c95994 | -3.0239 | -53.94168 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9e2b15d-538f-3aa1-8d40-1777dc95fcbf | -4.46107 | -55.39989 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 024eb876-1c90-30d7-a1f2-8f2322be1adb | -9.48614 | -64.34518 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bbac73f-2c7d-3a44-ba5b-1c81c46a00d2 | -5.98143 | -53.52826 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6235b2d1-e88d-3ff1-a25e-c23cd74ad89c | -3.02203 | -54.09317 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 60c52acb-c4a2-38f5-95ee-0de4720cd522 | -2.49283 | -56.34281 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64a2f6f5-e209-3921-b2f8-c5be95a50064 | -3.51514 | -54.53302 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4277545-e6a4-3fd8-b1b4-c21cb33e9d3b | -3.29775 | -54.05823 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a631d5ad-ad1f-3e8a-a75a-caf2c8a88197 | -2.87422 | -54.88314 | 2026-10-08 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aeab1946-8b34-3f1f-a3e3-b9fe1dc1b692 | -6.12644 | -53.05655 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c062c74-489d-3fd6-9365-1788f16f8942 | -5.74124 | -53.46348 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26df1aee-3bc1-3ef5-8576-b2c120694f4f | -7.38705 | -55.21904 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README160.md)
