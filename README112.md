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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87b047fc-3d98-3d73-aaf1-a11e92f4cc18 | -9.0579 | -46.9688 | 2025-09-10 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 17bedb6b-4c0d-3d28-9ed5-83c680fb1def | -14.5612 | -52.1623 | 2025-09-10 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 6cd17003-079b-3b27-90ed-b86787e670c2 | -5.57 | -42.9297 | 2025-09-10 14:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| e3489a11-ddaa-367b-8a59-0a410e4eff4a | -9.0232 | -49.7834 | 2025-09-10 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 18cf5b2e-ac3e-3482-806e-928293379094 | -14.8877 | -55.8567 | 2025-09-10 14:00:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| cfbec095-3d96-3da3-b3c3-56125ead8e94 | -6.8897 | -47.8897 | 2025-09-10 14:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 176e2467-28d0-32a7-b276-1a7178aa4410 | -11.1689 | -45.2914 | 2025-09-10 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.4 |
| defedbe6-16d3-3ae0-b772-4086b5b82b87 | -13.1176 | -54.9191 | 2025-09-10 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| d89bd782-547d-3aba-85fb-8e42768b2f12 | -11.1247 | -52.0149 | 2025-09-10 14:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 325.5 |
| b17427eb-59c7-3cf3-abc0-8a31400b10d4 | -9.042 | -49.7817 | 2025-09-10 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 191.6 |
| be51b285-8a5c-3165-a79e-41a748a06134 | -11.7706 | -50.5901 | 2025-09-10 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 039f812d-6c41-3d64-b541-424c536f0aa3 | -15.2877 | -53.7987 | 2025-09-10 14:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| df045352-0d5f-3539-8307-7cb67ca6a1f2 | -9.7011 | -46.877 | 2025-09-10 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 831ad410-21e0-3ca6-a9b4-ab8e5a830a20 | -11.3905 | -43.5365 | 2025-09-10 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 278.0 |
| d67ebbb8-c148-3116-a9b0-0fb6e37f8dbf | -9.7223 | -48.0907 | 2025-09-10 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 358be3b9-a4c8-306b-af8d-56c95eed3c5a | -10.4077 | -50.5032 | 2025-09-10 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e08f4279-8ac7-3946-a5c6-665765753cbb | -8.49 | -45.6826 | 2025-09-10 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 446af068-1813-315f-a660-0214463ed834 | -6.3808 | -44.4205 | 2025-09-10 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| f81d6716-8762-36a3-a1b4-f5dd0d660498 | -14.5122 | -53.9576 | 2025-09-10 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| ebcf7de7-b48a-3fc4-abf1-5e0a4b8b803c | -6.9451 | -44.2803 | 2025-09-10 14:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 2041e4bb-2975-34db-9e2c-0b4094c2c027 | -12.5796 | -44.6412 | 2025-09-10 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| d0cb4683-6852-354b-b104-38bd6142ea0c | -15.6745 | -53.8745 | 2025-09-10 14:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| ead050d2-abd0-37fe-94d8-93dd17c588b7 | -8.9943 | -46.0583 | 2025-09-10 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| c54b4c7d-8747-3359-b495-249444b007a4 | -12.5286 | -45.2987 | 2025-09-10 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 12570bd3-415c-3f55-b40c-a5909fd7a20f | -7.4845 | -48.2349 | 2025-09-10 14:00:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 9e6b580e-7a6e-3671-a1a3-48e68579409e | -9.0229 | -49.8048 | 2025-09-10 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| e67ec5d3-26bb-3399-928c-3c8eadba7a04 | -13.937 | -48.2522 | 2025-09-10 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| ebbfec1d-4a2e-31a1-a68d-bc850a52e4e1 | -9.6818 | -46.9015 | 2025-09-10 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| f8efd8a9-819e-30fd-ba3b-e3eecdc614d0 | -9.0262 | -49.5261 | 2025-09-10 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 2282f79c-30e2-35a2-8744-f96c0f5538ec | -6.8523 | -47.8925 | 2025-09-10 14:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| bbbac0d9-76dd-3f17-aa4d-1d4f539f652b | -15.1374 | -52.4039 | 2025-09-10 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 2a4fe8a4-cd5a-343a-9659-2cf12246f877 | -5.6788 | -43.3425 | 2025-09-10 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 66f3dd4d-229c-365c-9320-ade4614e17c5 | -9.9762 | -50.3121 | 2025-09-10 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| a8ddfd2d-808b-3171-af8d-068179c8af66 | -14.4247 | -53.4039 | 2025-09-10 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| b27ac096-9862-34ca-b668-6f461ea62d31 | -9.055 | -45.7583 | 2025-09-10 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 8bd52dff-e6ff-32ea-b6e9-73bbaa6f6e7b | -7.5218 | -48.2536 | 2025-09-10 14:00:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 331.3 |
| b21d0e14-4c30-309a-bae3-661cd1f21eed | -11.1693 | -45.2683 | 2025-09-10 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 360b56ef-d16c-33bc-ad0e-ec27b06e27a3 | -13.1367 | -54.9171 | 2025-09-10 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 141.0 |
| e9df7338-f119-32f2-9f90-c0dbf61e6b91 | -10.1467 | -46.1747 | 2025-09-10 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 279.1 |
| fb8423aa-7c5d-3bd3-9bf2-b75bcf9a6e56 | -9.6821 | -46.8791 | 2025-09-10 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 215.0 |
| 76adefab-7e15-3322-a8eb-8cdc39bbcddd | -11.4702 | -50.3461 | 2025-09-10 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 17d92f0b-1c54-335c-8cc6-2916d747308d | -15.2881 | -53.7777 | 2025-09-10 14:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| f98ad395-d8ea-3659-9d18-bc8623a8e3f2 | -11.7602 | -46.4621 | 2025-09-10 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| adcda796-14e8-373f-bb3c-fe168cfa8711 | -16.0604 | -49.9741 | 2025-09-10 14:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 29f75990-4b58-330d-9bef-c72ff74c268a | -8.7361 | -47.0904 | 2025-09-10 14:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 410ec896-6b90-3ef4-8603-fbc48dac8c60 | -6.2595 | -43.4129 | 2025-09-10 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 196.7 |
| 9fef7a5b-df59-3d43-92ce-23569524822c | -9.7589 | -51.1383 | 2025-09-10 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 232.1 |
| 228b6e85-8677-347f-9e5c-a5063b62e23a | -15.2686 | -53.7801 | 2025-09-10 14:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| a3a56829-9916-31a8-84d5-1c148ac3e892 | -10.7369 | -46.0785 | 2025-09-10 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 22a27bc9-5b97-37ea-9c38-21a753293100 | -14.5125 | -53.9367 | 2025-09-10 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| ef6309cc-0740-3fd7-818d-c6f962a56a45 | -11.4097 | -43.5336 | 2025-09-10 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 99ee093f-1e7e-300a-9b49-08e881e80820 | -14.9067 | -55.8751 | 2025-09-10 14:00:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| b57be15f-b123-39bc-85d4-5b5cbc0c6830 | -5.6272 | -42.8313 | 2025-09-10 14:00:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| aa7445ab-117e-378f-800a-8f380f2557fc | -6.3804 | -44.4664 | 2025-09-10 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 8e600332-c382-3aff-92d5-9411e9a5a010 | -6.1896 | -41.0398 | 2025-09-10 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 149.7 |
| 9f0a1dfa-24cb-3d9c-9ea3-84d129e26af8 | -7.5409 | -48.2085 | 2025-09-10 14:00:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 197.0 |
| d23fa62c-e290-3a74-aeb8-20cd22e1d390 | -14.907 | -55.8546 | 2025-09-10 14:00:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 299ceaf6-eecc-38a1-afb4-e8c8e98893a8 | -9.7777 | -51.1366 | 2025-09-10 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 161.3 |
| fb8fc921-4448-3ff6-90c5-bd99d3c6424f | -5.5702 | -42.9062 | 2025-09-10 14:00:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 4b472b0f-3538-308e-a740-164df9aaf174 | -6.3806 | -44.4434 | 2025-09-10 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 139.4 |
| a279d7be-a84f-397a-b017-515926ad5144 | -12.1803 | -53.863 | 2025-09-10 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| ae9f0289-2d33-36ff-b5c2-79cc157f773e | -9.8263 | -46.0549 | 2025-09-10 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 96b18fd3-999e-3157-b836-8822fa75d5c8 | -7.5033 | -48.2334 | 2025-09-10 14:00:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 047979fe-4901-32ed-bf26-c404bb97560e | -9.3437 | -46.7603 | 2025-09-10 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 82a7d299-1153-3e5d-be7c-44e5640b1f61 | -6.2597 | -43.3895 | 2025-09-10 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 77a834c6-efe4-37d0-9c07-62f90af8e81a | -9.8838 | -50.1719 | 2025-09-10 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 3a792c34-0bac-3aa5-97f7-4d4ddc584001 | -8.0794 | -48.6407 | 2025-09-10 14:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 161.5 |
| c63c7f5a-b369-3adc-8d7d-6edc3442c460 | -8.7549 | -47.0885 | 2025-09-10 14:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 54383299-fb36-3dd2-b1ce-32b5eb28fc1d | -10.3885 | -50.5264 | 2025-09-10 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 217.5 |
| df340f83-edc8-365d-95cb-092309c05019 | -11.2196 | -54.9975 | 2025-09-10 14:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| dc61c80c-93ba-3a8a-bac6-f7939dcf3b49 | -6.2407 | -43.4144 | 2025-09-10 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 157.0 |
| ce1032f9-43c5-333c-9e96-7857f24253aa | -10.0137 | -50.3297 | 2025-09-10 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 59bdabe4-5905-3d53-88fd-6f2739ec5d94 | -9.7591 | -51.1172 | 2025-09-10 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 386.6 |
| ee861a75-a8f6-373d-82ee-817c3bea2fd3 | -9.0132 | -46.0563 | 2025-09-10 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 85c1e475-488c-315d-86cf-d40c6acafe17 | -8.0416 | -48.6656 | 2025-09-10 14:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 165.5 |
| 63485921-112f-3c53-851e-437736d09fdf | -6.3993 | -44.4419 | 2025-09-10 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| cd509f0a-d7f0-3630-9fa7-8fae959e7b48 | -7.7104 | -44.7598 | 2025-09-10 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 2443e87d-3c2f-3664-aa0b-cfdc82dbf84b | -15.1903 | -53.832 | 2025-09-10 14:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| da7e7834-e865-3b23-8b98-444c17d23a23 | -14.4054 | -53.4063 | 2025-09-10 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 6a56954a-0130-329c-9731-3802a3705bdf | -9.1142 | -46.9851 | 2025-09-10 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| bd64e2ce-f154-3ba4-af3d-adab98bad4a1 | -6.2409 | -43.3911 | 2025-09-10 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 0b52ff19-7c56-3930-96bc-907434e42576 | -7.5594 | -48.2288 | 2025-09-10 14:00:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 2848c162-3e32-32df-a164-8472838a674d | -9.0417 | -49.8031 | 2025-09-10 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 486ea294-6746-3eb1-b592-4d22a5373abd | -6.8895 | -47.9115 | 2025-09-10 14:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 137.5 |
| d38fd24f-dc67-3fea-8064-6ec0dcc533f4 | -13.1364 | -54.9376 | 2025-09-10 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| c75784eb-09b8-341e-9454-3ca616eeb771 | -9.0768 | -46.9668 | 2025-09-10 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 1659d17b-9713-3d0c-b00c-22e321dbdd4e | -6.2043 | -43.3008 | 2025-09-10 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 5c0c5794-9cd0-35e1-91cd-16b73d8eba6c | -6.204 | -43.3241 | 2025-09-10 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 49d28edb-ab4e-342a-8411-41fa9946b3f3 | -9.0605 | -49.8014 | 2025-09-10 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 224.5 |
| c9460b20-fae4-3377-bef6-6c8ef3c91efc | -6.8519 | -47.9361 | 2025-09-10 14:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 3fbc7d82-17cb-313b-95e7-5628ba0c37ec | -5.397 | -43.4332 | 2025-09-10 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 32468d77-7333-3806-a248-7493fbf64a03 | -14.5609 | -52.1836 | 2025-09-10 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 24ceb5c9-6c41-3ed4-9d6f-558e82c33aae | -14.5315 | -53.9553 | 2025-09-10 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 3f8e79f9-f4c3-3ed3-b547-1a0c8e153ce3 | -11.9535 | -51.081 | 2025-09-10 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 663aa489-acb3-3be7-92f4-4f1a99712aeb | -10.3882 | -50.5477 | 2025-09-10 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 282.0 |
| 158aedbf-9531-3d5b-95ed-4b3552cdaef2 | -14.4004 | -47.327 | 2025-09-10 14:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 49.2 |
| dc2e6e56-3648-3bad-a796-4b0fa640044e | -10.1654 | -46.195 | 2025-09-10 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 152.9 |
| fa7b4b79-11eb-35df-a552-97aa2f687c13 | -11.1245 | -52.0359 | 2025-09-10 14:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 296.3 |
| 5e857ac7-ccd5-3e3a-af10-3ec8f956bcc5 | -11.4705 | -50.3247 | 2025-09-10 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| a0eda594-f5c5-32e1-bf7b-70afa6827fc8 | -13.1367 | -54.9171 | 2025-09-10 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 163.3 |


[Clique aqui para ver as próximas entradas](README113.md)
