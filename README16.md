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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cb7ba7a-bf11-365f-b65b-5217aac68182 | -1.91274 | -53.28976 | 2025-11-28 04:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6955f9b8-561a-3b81-a015-d1405e4db8e6 | -3.09102 | -40.65661 | 2025-11-28 04:59:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 12c615af-c3de-3d49-9010-8ce272a4fd7b | -2.43527 | -50.26247 | 2025-11-28 04:59:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02e69d1a-3493-3cb4-b1c2-33ff32225e96 | -2.66101 | -46.96749 | 2025-11-28 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1453b4f4-f858-38b0-854c-d086f55fbc46 | 0.4647 | -60.45336 | 2025-11-28 04:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e8b8e2e8-7b1e-3a92-b04f-c24d217c95d6 | -2.54956 | -49.06799 | 2025-11-28 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c02c35a1-0edb-33d6-be6b-6dd4f2519a78 | -2.14346 | -53.64746 | 2025-11-28 04:59:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c920161-5cb1-30a7-8b72-bb7747a876c9 | -1.33758 | -53.2206 | 2025-11-28 04:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c222439b-ea42-33d2-bc0b-9302fcdf8a68 | 0.46382 | -60.44788 | 2025-11-28 04:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6aceeed2-750f-3018-9aab-d6d1f683a21a | -2.26869 | -47.09713 | 2025-11-28 04:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50d7bd6e-ed8f-3fcd-9cfb-6977ce9640b9 | -1.64603 | -52.03985 | 2025-11-28 04:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6ea6a24-4b81-3d20-a87f-a4626adaee89 | 0.61856 | -51.80281 | 2025-11-28 04:59:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6eff581-4a63-370d-9169-76bd0e7f4478 | -3.51584 | -43.67666 | 2025-11-28 04:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 446a1585-5658-3ecf-9901-db963d5a5cb9 | -2.21481 | -51.377 | 2025-11-28 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 405adc38-0c92-3bd3-a0bc-0d82b81e3e69 | -2.57287 | -49.09602 | 2025-11-28 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c05bf993-4292-3863-bb2a-c53def2e693e | -2.79788 | -48.5642 | 2025-11-28 04:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d18ea86-3a52-3ec5-891c-15db8ba08ec2 | -2.61582 | -47.3493 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc6e593a-793c-3c3c-900e-c489c65f1969 | -2.71243 | -45.22047 | 2025-11-28 04:59:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 89309fca-f9aa-36e5-b682-c1246ffba237 | -2.60346 | -47.34325 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 559d7f57-3016-3e94-80ba-c52137b7c6a3 | -2.74805 | -47.12951 | 2025-11-28 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f47319ea-23fb-3c09-8634-9a9e2e6a660a | -0.86432 | -47.65896 | 2025-11-28 04:59:00 | NPP-375D | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68e6e59a-fc5a-34dd-b760-0074f93e8065 | -1.44802 | -55.29488 | 2025-11-28 04:59:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25089357-3927-323f-9eaa-14b49bb22bfa | -2.71812 | -45.21685 | 2025-11-28 04:59:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1bc1bfb1-a3de-3ac0-bb7b-45728191b7fc | -1.83751 | -55.34616 | 2025-11-28 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e03c8106-a493-39d3-826d-dc52e3672a59 | -2.70826 | -45.67409 | 2025-11-28 04:59:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3b7a8d27-3a66-3cfa-872a-427a8b401217 | -2.71309 | -45.21615 | 2025-11-28 04:59:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5d8e9735-4034-3a05-8e47-9a1bddceeb89 | -2.7055 | -45.67472 | 2025-11-28 04:59:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 51d85b9e-e4a9-39ee-bab9-584b6044e6c9 | -1.47608 | -54.20248 | 2025-11-28 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c26ac3c0-bda5-348f-8231-a2cffca75d9e | -1.36295 | -55.44178 | 2025-11-28 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdeb67bf-477d-359a-ab9f-805eb642545c | -1.91089 | -46.28156 | 2025-11-28 04:59:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 039812b2-a321-37f9-b745-18f6c662fa36 | -2.65278 | -46.96181 | 2025-11-28 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aecc4ce4-7ee4-3eec-a283-6736c916509a | -1.34491 | -55.44278 | 2025-11-28 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2db8842-6b72-30f8-83ca-971ed74ff634 | -2.62141 | -47.34184 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34db30b6-61c8-3cb7-954f-aea924d7ffe7 | -2.42724 | -50.29072 | 2025-11-28 04:59:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0f208444-f9e4-3794-a207-fc52335f4a17 | -2.70532 | -47.40824 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c7619cf-4289-3c3c-91f6-d0861fba2b54 | 0.65746 | -51.53824 | 2025-11-28 04:59:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cd166d6-932d-34bf-a8b9-c6c67999227d | -1.35947 | -55.44122 | 2025-11-28 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e13b54c8-9439-3560-8e1e-d01ccf8d14ad | -1.45584 | -55.51531 | 2025-11-28 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c476c748-2a35-319a-9d05-92fd55f6244e | -2.71381 | -48.35185 | 2025-11-28 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| decab35a-af78-3b26-a746-8dc54b13c9e4 | -2.61645 | -47.34526 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 001b7fa2-4a2d-3c06-817a-106f36523537 | -1.8293 | -54.3267 | 2025-11-28 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d3fc66d-29c2-35bc-b2f7-2eeb15249f68 | -2.42763 | -45.74768 | 2025-11-28 04:59:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7b239e2-5466-33d0-af12-3ff171687118 | -2.4228 | -45.74693 | 2025-11-28 04:59:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b46adb2a-c6dd-38e9-b46d-abf64980ce49 | -2.06002 | -52.09653 | 2025-11-28 04:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2afd7e9a-c409-3cb9-b4cc-58e69c75129f | -2.71352 | -45.21326 | 2025-11-28 04:59:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6747fca2-3334-38a0-87bc-1bab7961014e | -1.82203 | -54.32917 | 2025-11-28 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8231c6c6-0640-339e-b818-e80ed0dabde3 | -2.61212 | -47.34459 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1adc5487-c57a-38d3-bbd8-68c8d5b8e057 | -1.38413 | -55.17287 | 2025-11-28 04:59:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f87ee54c-53a0-3a0a-a1f7-c74944b0fa52 | -2.41879 | -45.74092 | 2025-11-28 04:59:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57486ee3-744f-347a-9ac4-565fd4a66be5 | -2.2805 | -49.77571 | 2025-11-28 04:59:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b702a574-2f07-3888-8be8-b2cbf6f40853 | -1.37811 | -55.86929 | 2025-11-28 04:59:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1be48f3-5e11-3576-9f5c-9967bb39084f | -1.85218 | -54.79941 | 2025-11-28 04:59:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1aff453-498a-325b-b9c8-14206c55b3fd | -1.82594 | -54.32617 | 2025-11-28 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8127ef0e-e031-39e5-930b-576582e8d973 | -1.33481 | -53.21664 | 2025-11-28 04:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fd64706d-c7e3-3f5a-9867-693a87f8d567 | -2.42682 | -45.78498 | 2025-11-28 04:59:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd66edd0-68d8-302e-845b-7f3aeb3814b1 | -1.88296 | -55.28382 | 2025-11-28 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5430da71-43ad-33d2-b3cc-1057eb6d9dd3 | -1.82146 | -54.3327 | 2025-11-28 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b839edcb-91c9-30a9-94c1-9ac431e02453 | -1.62173 | -54.7119 | 2025-11-28 04:59:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ae54728-cd58-3bc9-b955-cc4d9ea843fc | -2.43126 | -49.08195 | 2025-11-28 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44d5b99a-3081-3e1b-b371-c503b7188137 | -2.39415 | -48.51726 | 2025-11-28 04:59:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2410803a-0c52-3602-bc31-7cfaa6fb0446 | -2.57673 | -49.09662 | 2025-11-28 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba406626-7b8f-39d2-8369-ed9f31111c8c | -1.4741 | -54.20238 | 2025-11-28 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b7543ed-dd7c-3d97-8780-135abb1f93ac | -2.69708 | -49.56054 | 2025-11-28 04:59:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6036745-819b-3d02-8e15-5669a4defe9b | -1.47887 | -54.20653 | 2025-11-28 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16153796-6ee4-3735-85b7-0b0c0963d22b | -1.24585 | -54.05858 | 2025-11-28 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90fe12c3-4d23-3ebe-bc79-fd858187af0d | -2.43464 | -50.26659 | 2025-11-28 04:59:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0721ba5-b12f-3e2c-b512-8a92aed20f4e | -2.69402 | -49.55547 | 2025-11-28 04:59:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d4447c8-45b4-37b4-92ce-3755ff336cbd | -1.36477 | -55.43024 | 2025-11-28 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d048427-827f-34b9-a67c-9c1339041ab7 | -2.62015 | -47.34998 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 76515244-9296-34ca-9016-cfe695b2bfa5 | -2.26942 | -47.09479 | 2025-11-28 04:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a3cbe58-7774-39a7-bcb6-31813ff021d8 | -2.62574 | -47.34249 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38bf8a55-30dc-3d0b-95ed-d20815e2979b | -2.62448 | -47.35064 | 2025-11-28 04:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6aca3e12-e1fd-32f8-9e76-24c832b4aeaa | -0.8602 | -47.65833 | 2025-11-28 04:59:00 | NPP-375D | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb134961-7f19-3b3d-bfb6-e7187a61750a | -2.80836 | -46.76561 | 2025-11-28 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91215b25-32d8-3230-b74f-aa54030a7ba5 | -2.23222 | -51.88592 | 2025-11-28 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c78c8131-32d4-3f3e-984f-e8d9e1e89c05 | -2.42266 | -47.23467 | 2025-11-28 04:59:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b2a95e69-3b1d-3e4c-9932-a4a4af6b5460 | -1.41137 | -55.39038 | 2025-11-28 04:59:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e4fbfcd-4542-37d3-bded-130ae900cf20 | -2.16281 | -50.62745 | 2025-11-28 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f577d093-1430-3cb5-b24a-e75d7c3f5e32 | -2.98759 | -45.4231 | 2025-11-28 04:59:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b00472d1-dd52-3040-bb3d-e4e7ad2df44f | -2.83345 | -46.72298 | 2025-11-28 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55ceb149-05f1-3f1a-91e9-4c36a77145f5 | -2.69332 | -49.55997 | 2025-11-28 04:59:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 323ad8ce-cc05-378a-bbaa-08b2415b93ba | -1.24864 | -54.0626 | 2025-11-28 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92627dfa-7db9-3a68-890c-23af586481fa | -1.41485 | -55.39094 | 2025-11-28 04:59:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d1325a9-2206-3e41-a83f-d94a0b7bebb5 | -3.51529 | -43.68051 | 2025-11-28 04:59:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72255957-8593-334c-aec1-50a59d8a0434 | -2.70339 | -45.6734 | 2025-11-28 04:59:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9bb461aa-54b7-318f-a14a-1306bc0a584d | 0.4598 | -60.45409 | 2025-11-28 04:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f221c75-d66f-3663-9bf7-a26cb804d40c | -2.26876 | -47.099 | 2025-11-28 04:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85480a08-a02b-3c29-9fce-89ddd0613023 | -1.33704 | -53.22404 | 2025-11-28 04:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2d697c7-faba-3025-a487-23f4898741ee | -1.34142 | -55.44222 | 2025-11-28 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87bd8e51-99e9-3d23-a9f1-a093353283ab | -3.7694 | -46.96 | 2025-11-28 05:00:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e4b4cfde-e46f-3cb0-a88b-b2c2d6c977b2 | -3.7508 | -46.9608 | 2025-11-28 05:00:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 7a050eda-5322-312c-85f1-dae650fefb6e | -3.02255 | -51.0332 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c088aeb-011f-3f49-9dae-88f9b774f32c | -3.35262 | -54.08931 | 2025-11-28 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d878e1dc-cbcf-3435-af87-44d54f08c1c8 | -3.15638 | -50.1768 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 155ba615-20ab-3720-b92f-20fb6526e546 | -2.85456 | -53.0069 | 2025-11-28 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92529795-7db7-33cc-86da-fb639a320100 | -4.39712 | -48.92102 | 2025-11-28 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a61edfa0-6ce0-3d2c-bfd9-9480ffb1411b | -3.23608 | -50.70106 | 2025-11-28 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41318a5a-e1d5-38e5-aef6-173ae035fbe1 | -2.58992 | -53.97296 | 2025-11-28 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f97b7100-ff7e-3097-b356-eb539c66faab | -4.23423 | -55.67699 | 2025-11-28 05:01:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6094781-6d2b-3a75-81c5-91b81c65ce00 | -6.17954 | -44.54023 | 2025-11-28 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README17.md)
