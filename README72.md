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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f75ce30-1d75-3345-bd0f-c677bc2a46b2 | -6.9699 | -59.0658 | 2026-08-23 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 7ac46f20-a66c-377e-be96-385392c8a683 | -6.1285 | -57.8393 | 2026-08-23 09:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| eaadfe66-5e80-3a34-9f07-e803bd109d52 | -10.84 | -50.99 | 2026-08-23 09:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 79920d8c-f25c-3531-ab6d-27077579f457 | -6.9699 | -59.0658 | 2026-08-23 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 4e81a85d-f144-329a-81ce-320edf9e49a3 | -6.6766 | -58.7299 | 2026-08-23 09:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 503d6d7d-f709-399b-a9a8-a81c660eafd9 | -6.6949 | -58.7485 | 2026-08-23 09:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 99e476c5-ff47-3cf9-8774-febb97712485 | -6.6765 | -58.7492 | 2026-08-23 09:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 6d622cae-565e-34fd-9fb8-663e4a7a953c | -10.4716 | -49.9624 | 2026-08-23 10:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 658b2a31-e32d-3e11-b3f5-1d3ba605b898 | -19.0252 | -47.055 | 2026-08-23 10:20:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 22c5750a-3e25-3ef0-8c2f-000bc0e8b98f | -13.1509 | -51.4068 | 2026-08-23 10:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 84a7dc7f-a35e-37a5-b6d3-bb056c22d228 | -19.0252 | -47.055 | 2026-08-23 10:40:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 2d5ef956-855b-3e0b-acd4-e743cf8fd6a9 | -19.0252 | -47.055 | 2026-08-23 10:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 4e5d0858-feda-38e5-a09b-b3b312ad6646 | -19.0252 | -47.055 | 2026-08-23 11:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 115.5 |
| d9b46e78-37d6-3432-918e-d0806d06a49f | -19.0252 | -47.055 | 2026-08-23 11:10:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 6197a523-2aed-3a89-8a22-57b581aea01c | -9.8182 | -46.6179 | 2026-08-23 11:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 302.6 |
| 418089b9-d1b6-3f45-9040-8751e9d20afc | -9.7992 | -46.6201 | 2026-08-23 11:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 75da56d5-0bdf-3e8b-afd5-134d28d76335 | -11.5804 | -46.9369 | 2026-08-23 11:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 818855a6-479b-386c-96c4-53e7bc6fcf07 | -11.5804 | -46.9369 | 2026-08-23 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 9bd79638-d4a5-3a06-9921-0320bd7910de | -11.5995 | -46.9344 | 2026-08-23 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 718ee2cb-914b-3338-9247-d2f9fc8cb61c | -10.4716 | -49.9624 | 2026-08-23 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 7882400b-f0c4-3a3d-a409-e453eb783cb6 | -11.5804 | -46.9369 | 2026-08-23 11:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 3e7491ff-3427-3dad-ac6c-6e304a9525c4 | -8.8171 | -46.6374 | 2026-08-23 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 0361d587-c07f-37f5-ad3d-5aa0786fdb24 | -10.4526 | -49.9643 | 2026-08-23 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 78d694c0-96bd-3026-abcb-72081befcc2f | -2.35367 | -48.8246 | 2026-08-23 11:51:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b12fdb7b-5ff3-35fc-b14f-ac665591dc5a | -2.56211 | -47.24244 | 2026-08-23 11:51:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 51995001-60f5-36ca-81b1-0894b062a017 | -2.98939 | -48.95695 | 2026-08-23 11:51:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 18fa291e-9a83-35a3-8c3f-7470e442da56 | -2.56085 | -47.25132 | 2026-08-23 11:51:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| d645ed68-b537-33d8-9991-c987965f40f5 | -2.46309 | -49.28124 | 2026-08-23 11:51:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d47f7a2e-566e-379e-aced-f12856fe4ade | -2.35237 | -48.83363 | 2026-08-23 11:51:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1ca856b4-ea90-339d-b68b-c2d6581b7b03 | -11.94728 | -45.49645 | 2026-08-23 11:53:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 25e4fc53-d039-3616-9b25-3f47a6bddebf | -8.82763 | -46.63515 | 2026-08-23 11:53:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 42588448-ad1c-3058-8590-f188c95a6cc3 | -8.93477 | -48.52867 | 2026-08-23 11:53:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c6967771-bb1f-3716-8381-53888cb0b813 | -6.20213 | -53.51616 | 2026-08-23 11:53:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 2e56d895-e79f-3ed0-9b4d-85debde6912b | -9.81195 | -46.61733 | 2026-08-23 11:53:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a60d49ef-3317-37d4-8e8f-a9e016911783 | -10.33061 | -45.39809 | 2026-08-23 11:53:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 29.3 |
| dbfe4cd8-ef16-3275-a1f0-6d2a83d405d6 | -5.94834 | -52.1317 | 2026-08-23 11:53:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 97c94159-732d-3571-aaaf-8b9f10be106e | -8.08922 | -50.05047 | 2026-08-23 11:53:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 352cf331-2399-37d3-a340-c8fa0592f578 | -7.97901 | -45.26153 | 2026-08-23 11:53:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 8afe7ef7-5bd2-3736-9b7f-9e9caa415aa5 | -8.96337 | -50.75728 | 2026-08-23 11:53:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cf3728e3-8ff2-359e-afdd-d4f26fb0fa2f | -10.8065 | -50.96086 | 2026-08-23 11:53:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c7809289-b8f1-3063-96dc-52a16152a193 | -6.19987 | -53.53122 | 2026-08-23 11:53:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e44232f8-42a1-32d3-a638-6319a4bcda74 | -10.30594 | -48.20976 | 2026-08-23 11:53:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0444eda8-98f9-3b28-99cc-c11eeceb6ab8 | -6.10851 | -49.40119 | 2026-08-23 11:53:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 79469c63-bf0e-319f-8fed-13ea7b46eda6 | -11.58319 | -46.94939 | 2026-08-23 11:53:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 64d03839-c553-3e2f-90e1-58a97688f0e2 | -11.57347 | -46.94809 | 2026-08-23 11:53:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| a4266576-5485-34f2-aeae-e8d1ab42ee2d | -7.76856 | -46.15846 | 2026-08-23 11:53:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 93aee329-d417-3888-b2c8-fd999ac8452c | -12.06839 | -50.59645 | 2026-08-23 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 4d1c912a-8cd3-3c21-9f3e-63beefa4df78 | -8.82905 | -46.62465 | 2026-08-23 11:53:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| c0cbf0c2-4e62-3d9f-b223-ec12f382fc77 | -10.32886 | -45.41129 | 2026-08-23 11:53:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 83ce8e3f-0b94-3d0b-87d0-8f3267e7d747 | -7.27087 | -49.90538 | 2026-08-23 11:53:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f730ce0b-770b-3def-aae9-42874812cfe9 | -10.64429 | -47.34559 | 2026-08-23 11:53:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| a7b923b2-8379-3c18-a9ea-409a4e9f902d | -7.7292 | -46.13541 | 2026-08-23 11:53:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 685a1988-5ebb-3cc8-a62f-ae4d59f851d9 | -11.59292 | -46.95053 | 2026-08-23 11:53:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| a59842ab-8513-3e95-83bc-7a98f6707370 | -8.3804 | -46.46924 | 2026-08-23 11:53:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 730b4efd-68aa-3f5b-ac7c-43b5bdfcdb6c | -7.01563 | -48.01572 | 2026-08-23 11:53:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ba8a3111-970b-3203-83dd-b95d33ef901b | -7.98937 | -45.26291 | 2026-08-23 11:53:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 57ecd3c6-0a51-3273-8497-603c87ec74ea | -11.1503 | -46.21698 | 2026-08-23 11:53:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 050471f1-7b98-3a32-8c8a-5ef61d6af1da | -8.81947 | -46.62342 | 2026-08-23 11:53:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 5317c850-92e0-35bc-a7ba-26fdb4a53927 | -9.02347 | -50.72768 | 2026-08-23 11:53:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 64d47ae8-049e-313d-8b3a-3ff0f1c0bbc8 | -7.76714 | -46.16904 | 2026-08-23 11:53:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d5e15363-bb44-36a2-afb1-6def37912706 | -12.26282 | -45.08747 | 2026-08-23 11:53:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 411d8f08-76cd-322a-93db-3dd78d90f172 | -12.06971 | -50.58735 | 2026-08-23 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 5568cb49-4823-3ab7-aa51-0a73cd737442 | -11.59441 | -46.9395 | 2026-08-23 11:53:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| a09f1f6b-90d6-3998-80ee-777355a66ae0 | -12.26478 | -45.07182 | 2026-08-23 11:53:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 29a07776-0d7b-3db5-a54f-dc51c9d6d47e | -8.92462 | -48.53644 | 2026-08-23 11:53:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 254a6eea-0308-333d-b979-fa3a0ecf125d | -10.47379 | -49.95712 | 2026-08-23 11:53:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 2276e4e0-7ab0-362f-b0df-c6ed686fa415 | -8.81807 | -46.6339 | 2026-08-23 11:53:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0052d5bf-8394-3dc5-a8e6-3c815a904a83 | -10.51399 | -50.43966 | 2026-08-23 11:53:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 743e1a5a-8e68-316c-befd-528764a19ec5 | -10.31498 | -48.21092 | 2026-08-23 11:53:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1d472d25-e4dc-333a-9e69-de0062057893 | -11.60694 | -46.77227 | 2026-08-23 11:53:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b2d23c4e-b2cb-3d89-92c4-88f9b323ca93 | -8.9335 | -48.53767 | 2026-08-23 11:53:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6bbcacaa-ae6c-3439-a9d1-a991def8ce9e | -11.78985 | -47.24644 | 2026-08-23 11:53:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 6758602c-9307-3945-9b25-849b22dca06c | -9.02208 | -50.73714 | 2026-08-23 11:53:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| cfb4f0bb-79f3-3574-8767-1eb247b6bdc1 | -10.38105 | -50.39848 | 2026-08-23 11:53:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 02670317-44c3-3b5f-8fc2-bafb9f40d0ae | -11.15194 | -46.20474 | 2026-08-23 11:53:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 4f2df793-5acc-366f-8823-59cd9ee52f23 | -10.47249 | -49.96608 | 2026-08-23 11:53:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 064e0705-7163-3f85-973c-8c88baa0b5e3 | -10.48134 | -49.96735 | 2026-08-23 11:53:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 80545a15-b4b4-3917-b62f-247c52bf932b | -11.58468 | -46.93827 | 2026-08-23 11:53:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| b9920e4b-9cf4-3d6a-a450-4c47224e7d71 | -12.28785 | -43.1601 | 2026-08-23 11:53:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 4943f8f8-1af1-3c5f-80c2-e9f2d4562a5e | -11.99356 | -45.50826 | 2026-08-23 11:53:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5c7c44aa-0f2a-3335-a7b6-78914540a064 | -8.96476 | -50.74791 | 2026-08-23 11:53:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 8858431b-a71a-3e9b-abfc-b4b5101aed86 | -9.80965 | -46.61111 | 2026-08-23 11:53:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 827080f0-5065-3525-af55-c85c066fc312 | -8.82089 | -46.61289 | 2026-08-23 11:53:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 84836b5e-2eab-3228-8c1b-cdbc27ebd62f | -11.94551 | -45.51027 | 2026-08-23 11:53:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| f4bf77f5-db99-3f15-812f-bfba9c2b74fe | -8.34268 | -46.50107 | 2026-08-23 11:53:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1d1ce1ba-5267-3c0d-89df-c2f19fd2b027 | -11.15022 | -46.21069 | 2026-08-23 11:53:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 8bf31add-a688-3455-bd8b-b6d05a583ef4 | -12.05949 | -50.59514 | 2026-08-23 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| d6e2e332-4ebe-3e4c-9d64-c496eec7438f | -9.99895 | -45.33459 | 2026-08-23 11:53:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 97cd8a3c-c0b1-327a-87b2-f22438c4d85a | -10.84897 | -50.98633 | 2026-08-23 11:53:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 05eec4de-ab91-3698-93df-57fcb30e3fd6 | -10.06739 | -46.45176 | 2026-08-23 11:53:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4e6ef1ca-6b06-3839-b9f6-ada5813d6e40 | -11.63997 | -50.55832 | 2026-08-23 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 9133a0bf-467f-394f-a2fb-c93853a6bd3d | -6.24417 | -55.38993 | 2026-08-23 11:53:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| ee424349-0c8b-3b76-9804-b10e4685442d | -10.8476 | -50.99574 | 2026-08-23 11:53:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 6bb29cf9-5753-3d8d-8fca-ae8eaed13c79 | -5.96454 | -51.95261 | 2026-08-23 11:53:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| fb64cf0e-b3c9-33e2-8459-42b59d8de067 | -7.26792 | -44.19436 | 2026-08-23 11:53:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a3fa43bb-44e5-3ad4-948b-1e8db5c6a26d | -10.33525 | -45.4046 | 2026-08-23 11:53:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| c7a4f049-36c4-3fb4-8e4f-6409fe3526fe | -12.7401 | -46.46114 | 2026-08-23 11:53:00 | TERRA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0caba904-797a-3291-bf85-212411e36eca | -14.36609 | -51.8446 | 2026-08-23 11:55:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c78b3329-85ab-32c9-ba4f-8250987fe4d8 | -14.31494 | -53.32447 | 2026-08-23 11:55:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cb4c5139-8a46-39b3-a41d-c779a97ec49b | -13.25957 | -51.59047 | 2026-08-23 11:55:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README73.md)
