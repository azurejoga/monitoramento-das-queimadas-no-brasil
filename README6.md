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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1e0887a-1465-327a-80a3-bb82c7b197bb | -10.4383 | -52.910301 | 2024-10-11 00:45:16 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59526c68-a289-3fee-a21f-55684ef5af63 | -9.8012 | -50.059299 | 2024-10-11 00:45:16 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 271c4196-013a-345c-8a57-a9115a0eb4ee | -9.8028 | -50.0662 | 2024-10-11 00:45:16 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e682949-7efb-33fb-860e-51d97527d53d | -9.8043 | -50.073101 | 2024-10-11 00:45:16 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c8cbc4f-503d-39be-8715-dd6917f354c8 | -10.2671 | -52.166302 | 2024-10-11 00:45:16 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db344959-5969-38eb-a3ce-0eece3ef7e1d | -9.7682 | -50.095901 | 2024-10-11 00:45:16 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 979573c2-05f2-3a87-afe3-c619f8174b1b | -9.7713 | -50.109699 | 2024-10-11 00:45:16 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5deb4a7b-db79-34d6-ae10-5fb2524b5e2b | -9.7631 | -50.1189 | 2024-10-11 00:45:17 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93e81de9-87ec-3578-acde-0a98e8392166 | -9.7647 | -50.125801 | 2024-10-11 00:45:17 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96677cbf-c52e-38b1-8b8c-b62268082044 | -10.4614 | -53.641499 | 2024-10-11 00:45:18 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 266ed1b0-93d2-3a50-966d-71114bca64d3 | -10.0058 | -51.5821 | 2024-10-11 00:45:18 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fca34607-c8e2-3d15-834a-611fc390fdb0 | -10.0073 | -51.589199 | 2024-10-11 00:45:18 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24af71fe-e960-39fc-93c8-2b4fbab8aefd | -9.1054 | -47.6464 | 2024-10-11 00:45:18 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7dfed57b-8c93-395d-8c08-a05656990334 | -9.1072 | -47.654499 | 2024-10-11 00:45:18 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c359e579-b809-37fa-8df1-2f564ba90a5c | -10.2238 | -52.6772 | 2024-10-11 00:45:18 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb52cacc-1ce5-3a0a-bf35-144bdd8a26e6 | -10.2255 | -52.684898 | 2024-10-11 00:45:18 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe4278ea-aeb4-3a8c-b495-3e2243228e6a | -9.1611 | -47.9757 | 2024-10-11 00:45:18 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf8d2650-b9f8-3549-a84a-ec05de5e459b | -10.2291 | -52.749401 | 2024-10-11 00:45:18 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f27bd2e-b491-31b6-aa71-e2c1613c83d2 | -10.2308 | -52.757198 | 2024-10-11 00:45:18 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c1f7641-0827-3882-9035-3fd296d8e4b3 | -8.9467 | -47.186901 | 2024-10-11 00:45:19 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb7844d9-8329-3679-9dec-0709cd6fe04f | -8.9487 | -47.1954 | 2024-10-11 00:45:19 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68189027-5700-3b85-bbb8-8f0346402527 | -9.7357 | -50.641102 | 2024-10-11 00:45:19 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdf833f6-e70c-31c4-b47b-0e69dd3b11c6 | -10.0518 | -52.073898 | 2024-10-11 00:45:19 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8490488e-1373-3d37-b7bd-5ecd7a076dea | -8.9369 | -47.189201 | 2024-10-11 00:45:19 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1084af0c-c1e8-3973-aed2-ded04cf84ef3 | -9.0406 | -47.6786 | 2024-10-11 00:45:19 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bdbbb70e-5852-3590-994b-28a03cfd0d90 | -9.0995 | -47.9324 | 2024-10-11 00:45:19 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a120c7e-e909-3a36-8734-078b2e63f0a9 | -9.0879 | -47.926899 | 2024-10-11 00:45:19 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ee8f1a0-f12e-3e0d-b40d-24f8a02aabe5 | -9.0897 | -47.9347 | 2024-10-11 00:45:19 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e677acb6-1d68-3080-868d-b6c8f81b1727 | -9.0915 | -47.9426 | 2024-10-11 00:45:19 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48b0dac5-b386-34a9-a8ce-0fadd29eb7c3 | -9.0409 | -47.813202 | 2024-10-11 00:45:20 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c88f39d3-58af-36c4-836c-735f80350df7 | -9.5794 | -50.2187 | 2024-10-11 00:45:20 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2bc4ee2-453a-326d-826f-d760d7b96715 | -9.581 | -50.225601 | 2024-10-11 00:45:20 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08438dda-210b-31d6-890f-eb1862bd1373 | -9.5469 | -50.211498 | 2024-10-11 00:45:20 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c01bae82-2d98-3801-92dc-61aa04715081 | -2.5444 | -47.2231 | 2024-10-11 00:45:21 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 5ee81f82-1c21-3481-8cb4-46b0bc7f21e7 | -2.6533 | -53.3506 | 2024-10-11 00:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 6c73031f-166d-35c3-bb1b-01cfb9469999 | -2.6533 | -53.3303 | 2024-10-11 00:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 61b8e43c-2f6d-3f37-b423-93063b07c769 | -2.6716 | -53.3502 | 2024-10-11 00:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 210e19a8-c7b1-3705-8b1c-7a4f00e57c28 | -10.3652 | -54.153801 | 2024-10-11 00:45:21 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84b01645-e258-3a9d-9736-4b21f6327e45 | -2.7663 | -52.4937 | 2024-10-11 00:45:22 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 0f209db6-4886-3e99-b71d-feb9f1745cb4 | -2.7664 | -52.4733 | 2024-10-11 00:45:22 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| c21aeabb-027f-3641-9713-ffabf2492ec3 | -2.7847 | -52.4933 | 2024-10-11 00:45:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 213.0 |
| f59d4b5d-2789-3675-bfaf-0e5b97e560f8 | -2.7848 | -52.4728 | 2024-10-11 00:45:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 171.8 |
| 5b16bef0-3e4d-3821-b1f1-c97c1dc40a39 | -2.8081 | -51.0084 | 2024-10-11 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 3e81e554-1ef8-3c27-a928-6e4ac0021e50 | -8.6105 | -46.458698 | 2024-10-11 00:45:22 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3bc830b2-0ca0-3440-960d-0f3d14c38d72 | -8.6127 | -46.467999 | 2024-10-11 00:45:22 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d6b8e3b-0227-36db-bd8e-ec582b5a08df | -8.6149 | -46.477402 | 2024-10-11 00:45:22 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6dd3fba5-9da8-3203-9be1-75cbaca6d438 | -9.0789 | -48.469398 | 2024-10-11 00:45:22 | METOP-B | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37046a98-0b40-3898-893f-0cde402ae3ce | -9.0807 | -48.476799 | 2024-10-11 00:45:22 | METOP-B | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43602d93-74f2-347d-8bb9-92fb3449160f | -8.6029 | -46.470299 | 2024-10-11 00:45:22 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2b808a4-ed8a-32fd-aec6-26063c598d23 | -8.6051 | -46.479698 | 2024-10-11 00:45:22 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e828110c-bd0b-38be-b51b-2c9f7420bc16 | -8.9185 | -47.908501 | 2024-10-11 00:45:22 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19260946-072a-315f-aa89-f5cda70f7be9 | -2.9674 | -47.9931 | 2024-10-11 00:45:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 6ac02c9c-5f30-3f0d-b74a-385f06e82bfe | -2.9673 | -52.9169 | 2024-10-11 00:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 141.8 |
| cddefd40-bba8-36ee-94fc-d71233f50345 | -2.9673 | -52.8966 | 2024-10-11 00:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 156.8 |
| 39c3d5de-502a-3859-a15c-b6ab1c3c5fd8 | -2.9857 | -52.9164 | 2024-10-11 00:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 931b3a67-c624-3670-9cf0-2d36ef7faf38 | -2.9857 | -52.8961 | 2024-10-11 00:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 177.7 |
| 465e605f-74f7-3e97-85da-74441dadf905 | -8.6975 | -47.092098 | 2024-10-11 00:45:23 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bccf2097-be07-38d3-9f8b-83ca3d6c853a | -8.6995 | -47.1008 | 2024-10-11 00:45:23 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e75123ac-8765-35f0-855c-e25cf22426c2 | -10.273 | -54.250301 | 2024-10-11 00:45:23 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5372da8-6e0e-3acd-9025-5915138782db | -9.776 | -52.034698 | 2024-10-11 00:45:23 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a499f1a-d1a1-3bf5-b9b9-5ca0d858a4d3 | -9.7776 | -52.042 | 2024-10-11 00:45:23 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c71b805-45b7-35f8-94bf-cae98cebb4d0 | -3.0343 | -61.6918 | 2024-10-11 00:45:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 3b582e00-cfde-3126-aaf5-5711db4f60ce | -3.0343 | -61.673 | 2024-10-11 00:45:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 7aebefe6-e16c-3757-aa8e-73e1ee76ba82 | -3.0525 | -61.6727 | 2024-10-11 00:45:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| f0e38988-6f6a-34b1-aa58-f46255d432d2 | -3.1422 | -50.4562 | 2024-10-11 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 3bfa2138-bdfb-3a3a-bb15-5cb6829143a8 | -3.1423 | -50.4352 | 2024-10-11 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| ccffb938-b926-393d-a298-b26758f28594 | -3.1607 | -50.4556 | 2024-10-11 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 22749e40-4e8e-329a-ac15-dbc28bb2cfa9 | -3.1608 | -50.4347 | 2024-10-11 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 169.0 |
| e7286109-565b-343a-a111-d538ef62caf9 | -8.0759 | -44.778198 | 2024-10-11 00:45:24 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f32e7437-fcdb-3728-923e-e2db941296c2 | -9.5003 | -50.970901 | 2024-10-11 00:45:24 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f03fa718-1cef-3160-a2b6-91c3e7ec27d1 | -9.5019 | -50.977798 | 2024-10-11 00:45:24 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53845aab-b4ac-34ee-81e3-618b7b3d34fa | -9.4905 | -50.973099 | 2024-10-11 00:45:24 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46fbc764-97cc-3ada-8f33-67cbe54f0c50 | -9.4921 | -50.98 | 2024-10-11 00:45:24 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1057e817-3584-3a3e-8867-d472907ad0c8 | -9.4822 | -50.982201 | 2024-10-11 00:45:24 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e83113ca-a69b-3a7d-99e9-893e8f72c1f9 | -3.2911 | -46.0954 | 2024-10-11 00:45:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 248ce8cf-34f2-3599-9f3e-f9659e06a827 | -3.2912 | -46.0731 | 2024-10-11 00:45:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 34e32f25-e00e-3f11-ae0b-51fbafc8f262 | -3.3097 | -46.0946 | 2024-10-11 00:45:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 584a746c-98ab-3401-9c35-f27dca937579 | -3.3098 | -46.0724 | 2024-10-11 00:45:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 180.7 |
| cf8d519b-015b-3503-858e-3bf213d243fa | -9.6324 | -51.7551 | 2024-10-11 00:45:25 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 917a0909-1c65-3f95-a510-f337d39cd2e9 | -9.6226 | -51.757198 | 2024-10-11 00:45:25 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ce46c76-921f-3036-a0c0-1d582d3d4fb7 | -9.6242 | -51.7644 | 2024-10-11 00:45:25 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7880befa-4fe2-3072-ae48-06cdc85a4c98 | -8.526 | -46.976398 | 2024-10-11 00:45:25 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96cae0aa-30cd-3e48-a7dc-efef1ef0b2da | -8.528 | -46.985199 | 2024-10-11 00:45:25 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36f6ba03-62ce-3afc-a3ec-06c261dfd133 | -7.8189 | -44.183498 | 2024-10-11 00:45:26 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9ff21770-3cc8-37e1-98c1-331c4218708f | -7.8222 | -44.1968 | 2024-10-11 00:45:26 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6a8ec9c1-91f2-33dd-97d9-9f348d576cda | -3.614 | -44.7783 | 2024-10-11 00:45:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 0988c632-73e1-3252-a277-43a4fec869e9 | -10.37 | -55.8391 | 2024-10-11 00:45:27 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a767778-94fb-3ce7-89b2-d750aa26268c | -10.3724 | -55.8507 | 2024-10-11 00:45:27 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3632647b-b845-3eee-a595-25689f7a8328 | -9.7191 | -52.811699 | 2024-10-11 00:45:27 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ff785a7-0cfa-373b-9ea6-5f37413edb16 | -9.7208 | -52.8195 | 2024-10-11 00:45:27 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d3c34d9-286e-337f-9d3a-a867b3d353d3 | -9.7225 | -52.827202 | 2024-10-11 00:45:27 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1747b1dc-add7-3b17-a471-268e810c6962 | -10.3602 | -55.841202 | 2024-10-11 00:45:27 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d2ad2b9-7e6a-3a52-8617-6b2aaf40ea98 | -10.3626 | -55.852699 | 2024-10-11 00:45:27 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a7ac7db-71eb-314d-8a6d-828191bf3b74 | -9.7093 | -52.813801 | 2024-10-11 00:45:27 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d647d991-10c3-3448-bad9-63e5a95ef95b | -9.711 | -52.821602 | 2024-10-11 00:45:27 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 65d4f9b8-91ef-3c64-bc76-b568edc0b8b1 | -9.7127 | -52.8293 | 2024-10-11 00:45:27 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e78fe06e-23d3-3044-99f2-b4c3fc41e842 | -9.7144 | -52.837101 | 2024-10-11 00:45:27 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68da3b5c-0c6a-3072-b926-2584fb77ed8d | -9.7694 | -53.139198 | 2024-10-11 00:45:27 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9be14f58-b5f3-3ddd-97f5-7c81d6f56a57 | -9.7711 | -53.147301 | 2024-10-11 00:45:27 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab7018a4-3287-3688-b450-5da24af281f2 | -9.7596 | -53.141399 | 2024-10-11 00:45:27 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
