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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41469342-fd55-37e3-9f2e-cfa165633d3c | -6.31163 | -47.63617 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9ebcbbb2-dc7a-3e06-b14c-577cab22492a | -8.93345 | -44.3916 | 2026-09-20 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a049b6fd-8bde-35df-bb66-c91386f30945 | -7.87446 | -44.87344 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86053649-e58c-3ef5-adeb-b371f30fbcb2 | -7.54487 | -45.38553 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2094eff3-ef90-32a4-907d-ca8c596aa0bb | -13.02007 | -46.9087 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a152d55-8ebc-3139-a2d7-f828ffe1ab19 | -7.88442 | -44.84801 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a77decb0-f2fa-3382-bc41-d6e0c4ce2b13 | -9.83619 | -46.43494 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d0399c16-2a9a-3e27-a88e-6634de25a90a | -6.30179 | -47.61728 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 279c41c9-1bf4-38c4-8244-d2473f6eaace | -11.83456 | -46.85085 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e6a6d7d-cdd8-3b2b-8f7a-a36d6ec5f00e | -13.01825 | -46.91486 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9420d30b-e4b2-3941-b67e-dca3269aae20 | -11.86048 | -46.86794 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5ebb5ea2-dde5-3981-845f-3e9eee364256 | -7.42746 | -44.74065 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3a404db4-d514-3d39-96c3-7614e333cc2d | -7.62724 | -46.12563 | 2026-09-20 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 760776b5-165f-3728-82e7-1983e1873f63 | -7.37219 | -44.71397 | 2026-09-20 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| def12b92-b3e7-3c76-be22-df2f723b4121 | -12.15533 | -47.03633 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 563d2af6-3149-3989-8015-db1b5d3fc2fa | -8.41622 | -45.8759 | 2026-09-20 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f63cefb2-f7fb-3021-8661-d3d5b86c8f4b | -11.8564 | -46.8745 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 88b69add-318b-3309-be69-b9a0ef34d785 | -11.6695 | -43.41663 | 2026-09-20 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48e3421c-d915-3085-b456-ec3a8aceb52a | -9.82795 | -46.44753 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 71f58822-60be-311c-9751-ac3c81afb62a | -6.8138 | -47.89394 | 2026-09-20 03:45:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d9bf9d0b-3500-3276-ba09-99388d3b4d10 | -7.44995 | -44.73703 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a688fcc4-7c70-34de-8664-ae5d11db3546 | -10.49077 | -46.28059 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73b787e0-adfa-3484-9db6-105b6b086d58 | -6.51604 | -46.77402 | 2026-09-20 03:45:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5562b368-0a70-37c1-ad99-92103b010ff9 | -9.26102 | -45.94934 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2a2595a2-495b-3c35-8e3a-725e3a47c9f4 | -11.43844 | -45.42295 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df4f664e-c631-334e-8fb0-9c07aa417853 | -9.36353 | -40.31247 | 2026-09-20 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| c37b3eb5-d4cd-37bb-8a09-258087f5bbb2 | -9.02488 | -48.777 | 2026-09-20 03:45:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 386d9b2c-599f-3674-a2ba-10f46400ad02 | -13.02898 | -46.91866 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d150b31e-aa6f-33cc-ad26-06d0bc48f0a0 | -7.02754 | -45.26054 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d05b9642-e1ca-37e6-b24c-767f340eb8b0 | -11.45056 | -45.38661 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51ee99cf-e2d6-3322-8c46-a5571f4c5421 | -10.30991 | -50.24111 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 2062cc14-9c9d-36c8-9210-52be12003942 | -12.29339 | -47.12382 | 2026-09-20 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a0be7ba4-30da-392f-a131-fbc3b96380ad | -6.3063 | -47.62893 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 82104fd0-dd8d-3476-b21c-ad9479c7ec52 | -6.29653 | -47.60854 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9b4b1a91-477d-32a4-ac1c-8d91df6553de | -7.63072 | -46.76495 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6e15df6-a2f8-3929-bff5-4a6e12b70e81 | -13.02068 | -46.90554 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfc2b79e-92a9-3c9d-b0a3-7f6424cbdd80 | -9.22579 | -43.18539 | 2026-09-20 03:45:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3cca0d0d-e3e2-3f3f-8c50-5b6e7cfc50f3 | -7.54933 | -45.42432 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bc53c92e-be06-38df-b63e-21bab7b914f6 | -7.62338 | -45.45399 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 470006e2-7ff4-3177-98ee-ebc5385f7a1a | -9.79774 | -45.06551 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29b727f5-7368-3eef-8b77-8e4e9235ed9f | -8.38211 | -47.18824 | 2026-09-20 03:45:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 970bbd4b-42fb-3c0b-9875-7047c552edc0 | -10.46263 | -45.08026 | 2026-09-20 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebb48674-095b-37f2-9f29-e329c6b38b04 | -7.1599 | -47.43406 | 2026-09-20 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dea1461d-8016-39de-a64c-ffd76dd3f215 | -7.52622 | -47.33556 | 2026-09-20 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0f839531-ebb1-3c56-b24e-1679ffffa876 | -7.42566 | -44.75076 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9113908c-1703-3227-823d-6cf1c9dde14b | -10.46717 | -45.08439 | 2026-09-20 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79d72764-eb58-3c86-bbc1-51b9b9f2f2a4 | -7.59196 | -43.44371 | 2026-09-20 03:45:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5898ba8e-f601-3c92-adb8-05097c2e2b9b | -6.32562 | -47.63288 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 964d4400-a891-3c69-af0c-eaadd5d5bd2c | -9.72971 | -46.08879 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 055a4f9e-31b1-3096-82f2-116f2cd4a6b5 | -9.26404 | -46.19992 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 015712ad-8f3d-31cd-98a7-96d6736557f1 | -8.05302 | -46.25448 | 2026-09-20 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1959671c-6ab2-339a-b156-0631b8358404 | -8.75294 | -48.6598 | 2026-09-20 03:45:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 89002648-abbc-3069-a020-8fb46ee68a54 | -9.88914 | -46.53997 | 2026-09-20 03:45:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| deaf5898-0809-3507-a0de-d8debfeccfed | -7.28118 | -45.55654 | 2026-09-20 03:45:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 86871a7b-6c54-39c6-8510-6d2546f1f8cb | -11.48288 | -47.75603 | 2026-09-20 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36811be9-2643-3f10-9062-767ca21e7a76 | -10.77901 | -46.32101 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e9481f38-d80c-3cc8-9ec2-ca5786e54d0e | -7.77078 | -44.05527 | 2026-09-20 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 991f3ef7-24a9-338e-8da8-df75a3b912e7 | -10.78171 | -46.33682 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1fe9ce9d-52ab-3728-92f1-8b3730819d56 | -12.11452 | -47.02142 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f18581f-90e9-3ef2-97a5-a588abd0d740 | -8.76491 | -48.66881 | 2026-09-20 03:45:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b7d4a726-9b45-33c9-8445-1ed68ac810f9 | -12.1292 | -47.03661 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3cfb1bbc-e636-3fef-972b-275c6579f5b5 | -12.2957 | -47.11201 | 2026-09-20 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b2c29a4e-79b2-3cc3-81b6-c28a7a2f84dd | -8.86974 | -45.94683 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7cbfaf3b-25f8-328c-9cf6-06e705bb3fcd | -9.24058 | -46.18425 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 000a6f4a-aa05-35fa-a2b7-b0c4ecaa635f | -10.59987 | -46.52077 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 32d7b88e-be78-315f-850f-e4d4b9f271fe | -8.87456 | -45.95215 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 23e324f1-60f0-364f-9d55-e4084ba52e20 | -10.60779 | -46.52576 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f6f09482-e4ad-3fa1-9de6-64f5a99cc69b | -11.4806 | -47.73631 | 2026-09-20 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c77d4fbf-e397-3ced-a5ae-1855b88c5b3c | -9.26401 | -48.20587 | 2026-09-20 03:45:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 193de146-056b-37a8-8864-b49e8ae603ca | -12.75876 | -46.12179 | 2026-09-20 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c0dd076-1964-3225-9b2d-08f9f448143f | -7.5467 | -45.43905 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 029d6aad-e821-3e9d-85d0-63d84cedf413 | -9.79914 | -46.08652 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a244c2b3-25b0-317d-881f-d6e54e5c8dc8 | -8.42182 | -45.87697 | 2026-09-20 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4450be0e-c171-3487-b010-17189e28212b | -12.12354 | -47.0355 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b60d885b-45e9-31cf-8347-3c8f5850f2a3 | -6.29535 | -47.61599 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4078d829-9435-3a7b-9c4b-e4e00f0298e3 | -6.313 | -47.62834 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| bcfeb4f9-3d84-3f9c-90d2-6992f162719a | -13.01805 | -46.91907 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a37dd258-7355-30b0-9183-3206f9a0249a | -9.90279 | -46.5303 | 2026-09-20 03:45:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0dc86b26-c9a7-3b82-a65b-76b50bf053b2 | -6.44625 | -44.5722 | 2026-09-20 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44bcf146-a2da-38eb-bbec-dcf05967a381 | -11.45463 | -45.36481 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 774c4838-316e-33f9-b496-7c138a3fcbbe | -13.02023 | -46.90499 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f515aba7-6d61-3a62-9451-dec82c9e2ad5 | -10.47612 | -46.29704 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca16f2fd-46f4-3c92-a9cc-4aed27e8bf9e | -9.699 | -48.31768 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3947e7a7-8868-3349-8a04-c521f48a67bd | -6.29636 | -47.6106 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| bcf03655-4970-3c62-b258-ff816b2cb7e2 | -8.66873 | -45.432 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a18ff256-79b9-3136-a445-c983a516b371 | -7.4358 | -44.69386 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79bf012f-d2ae-3ac0-ae01-f442baa72c32 | -9.83553 | -46.43847 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6325e1c3-e54e-33da-9c0a-5b730127ce34 | -7.01788 | -45.25089 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| b2fc3e5f-1688-3f53-954e-c8fed1afaaca | -7.06076 | -47.532 | 2026-09-20 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c384c947-55f2-3197-8691-0e78b6ac57c4 | -9.22202 | -43.17975 | 2026-09-20 03:45:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 429f939d-03df-3a77-bcb6-1e388d17a02a | -8.66066 | -45.43732 | 2026-09-20 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43a5b75c-7dde-31cc-b13d-ac803088d25f | -13.01752 | -46.91845 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7760e93a-6c76-3c8a-8390-57c64a0866a8 | -12.37006 | -45.80165 | 2026-09-20 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5eaeadf0-61ea-3267-bac8-95081a210089 | -12.76142 | -46.13613 | 2026-09-20 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24f3c345-708e-3591-a4e5-ad505a52e663 | -10.66732 | -47.4327 | 2026-09-20 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d0631be-fbb9-3dc3-afc4-4d4953152585 | -9.73678 | -46.08192 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e46132bc-e187-31d3-850d-2581cbba48e6 | -7.35947 | -44.87425 | 2026-09-20 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 791d1a4d-deb7-3ece-80b8-6768c13062f5 | -7.53347 | -45.88508 | 2026-09-20 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0f1076fa-4d00-3939-bdc5-f8b9ea2ad10d | -7.63154 | -46.76041 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d708cbd3-2cc9-3e48-943c-c831deeda9e7 | -11.32274 | -47.29038 | 2026-09-20 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README18.md)
