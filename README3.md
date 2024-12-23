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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7afe4185-addd-3700-b026-9e78eaca6624 | -6.7354 | -34.9887 | 2024-12-23 00:24:00 | TERRA_M-M | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| 6d6fa6fd-f170-37bd-863f-ca29105f4622 | -4.17996 | -43.66367 | 2024-12-23 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 98b46e02-eb16-3fa6-83aa-60d375336189 | -4.17013 | -43.65219 | 2024-12-23 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c6262e3e-81b2-382d-b231-ddf9ebbb0041 | -4.03935 | -46.4137 | 2024-12-23 00:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| c05a831c-287c-3ee4-ab98-be01e8925b68 | -4.06501 | -44.10421 | 2024-12-23 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| fbc24f3b-e0f7-3819-9163-53d6bc997ee4 | -9.8303 | -36.33868 | 2024-12-23 00:24:00 | TERRA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| f5839eeb-d912-34b0-a9a4-e07d796042ad | -11.97218 | -44.24237 | 2024-12-23 00:24:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7e782d76-4f9b-3b9b-a795-dfaa6b8521a4 | -10.4328 | -44.89159 | 2024-12-23 00:24:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8cf36408-6f62-31a8-8ccb-b1b22519908e | -1.6948 | -52.601101 | 2024-12-23 00:24:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b34c066-646e-30c7-9db2-92dbd8fda7aa | -6.0045 | -45.418201 | 2024-12-23 00:24:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b710cce2-df65-3f57-a8d3-9ef6178baa75 | -3.922 | -46.357201 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d7bbbd86-0665-336b-95b8-45098875e4e2 | -4.03 | -46.785599 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa5c3680-4e24-3d74-a4bb-dd8552479ce3 | -1.7382 | -52.5653 | 2024-12-23 00:24:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0051025-9eb7-33bc-95fd-abf61672d288 | -4.0714 | -44.099701 | 2024-12-23 00:24:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9a86e6f-4dce-35a4-97a2-2a41604612d2 | -4.1925 | -43.646599 | 2024-12-23 00:24:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a808e090-e14c-307b-8d22-b40024f2d19a | -1.0672 | -53.606499 | 2024-12-23 00:24:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 096cc7d3-5492-35b7-b0bd-538c72bd28c4 | -4.2245 | -43.783901 | 2024-12-23 00:24:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32a414b7-c26d-3120-ac86-4d64889f9514 | -3.9854 | -46.725201 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ecf9b324-7aa1-3b8c-a638-89fd370c0a8e | -3.8731 | -47.272999 | 2024-12-23 00:24:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76083044-1124-3b47-97bc-32e246307823 | -4.0084 | -46.329601 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a4396485-9262-3ebb-b23c-ee7ecdba73a4 | -3.979 | -46.3363 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| af7d8d9a-02de-3a57-b1f6-79ab9f2d745a | -10.4286 | -44.882599 | 2024-12-23 00:24:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dae9e8b3-6980-38b7-8a8e-77b4478369a4 | -4.1729 | -43.651199 | 2024-12-23 00:24:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8bab26e-3268-3548-a38b-ea8a96af51a4 | -4.1071 | -46.807098 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d047bbaa-ac57-3a9a-90e0-9b61d9e26dbd | -1.7224 | -52.5863 | 2024-12-23 00:24:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e38e738d-f95e-3b1e-94bb-b9536281b0fe | -4.0101 | -46.337299 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0cf45d3c-a6e0-3075-b8c0-d859a2c302db | -4.1485 | -43.6343 | 2024-12-23 00:24:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 471293f6-96fd-3405-b451-11fa9378b0d3 | -4.1534 | -43.655701 | 2024-12-23 00:24:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0a1adf9-9280-3efa-a736-21670df35e34 | -4.0415 | -46.790798 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6b6c968e-5a50-3beb-99c4-c4fb3fe0a685 | -3.7965 | -46.845901 | 2024-12-23 00:24:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8531dc06-301c-3015-89fc-3885a3462cf3 | -3.9195 | -46.8881 | 2024-12-23 00:24:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e6dd023a-ca5e-3cac-91b1-479eb388bc52 | -1.665 | -52.055 | 2024-12-23 00:24:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7e94316-0a90-315f-b9e9-0964f8b6538d | -3.8747 | -47.280201 | 2024-12-23 00:24:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66ef3f4d-be12-35f9-ba25-d028a74b73a9 | -4.1754 | -43.6618 | 2024-12-23 00:24:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e00428f-9bd9-3c47-8788-73140275d15c | -4.1802 | -43.638199 | 2024-12-23 00:24:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b38a29e1-9785-37b3-99ba-7fc82f759c54 | 0.064 | -51.096298 | 2024-12-23 00:24:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f34a0a40-08a7-3a97-a1ee-aa644fa98ece | -1.7932 | -52.168301 | 2024-12-23 00:24:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab541e55-f1a9-3bef-b9b9-fb03f1bf587a | -1.7322 | -52.584099 | 2024-12-23 00:24:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b85a6f68-c239-35fe-b6e8-aa4e7faa96d1 | -4.1087 | -46.814499 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0384e5b8-ffb0-3769-a991-a989a7f7d7e5 | -1.3534 | -53.691399 | 2024-12-23 00:24:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbe10f65-5bb7-3ff1-9145-12f4de84c3f3 | -3.8392 | -46.6717 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d5dc4f16-bef5-3ef3-ab7f-eb9f246b2349 | -4.0658 | -47.077999 | 2024-12-23 00:24:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8baafa2d-18ad-34f2-8dd9-52c75401e6bf | -1.7303 | -52.575802 | 2024-12-23 00:24:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 830f193f-4ade-3986-9537-cbd3fb1443d5 | -3.9102 | -46.9828 | 2024-12-23 00:24:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 826823c9-f18e-339b-aeb4-4279f24030d6 | -4.0275 | -46.910198 | 2024-12-23 00:24:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0055e19-79b5-3b63-a18e-0d4f9a364c0c | -1.7009 | -52.582199 | 2024-12-23 00:24:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e76bf338-9669-3d03-b053-d53b5f915e37 | -4.0082 | -46.554401 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e14dd93f-4581-3b67-a141-b6d9c8310de5 | -4.4924 | -49.055698 | 2024-12-23 00:24:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 664e87e6-97bd-38e7-a2f7-bdf223ddcfdd | -4.4374 | -46.3134 | 2024-12-23 00:24:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f2e84a5-8b54-3ba8-adb5-a0dda8cc5f95 | -4.7759 | -46.396801 | 2024-12-23 00:24:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b560dd7a-f0da-378e-9115-2ab22357f598 | -1.3555 | -53.700901 | 2024-12-23 00:24:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3ba961c-7a3d-34ed-8019-dc79213e518e | -4.1436 | -43.657902 | 2024-12-23 00:24:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e05148b7-bee0-351c-8fb0-7f7f6b46780a | -4.0974 | -46.629299 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 895ec820-7f9c-39be-9a03-29b31c585125 | -4.0099 | -46.561901 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 73064868-d9e4-30d2-a261-aa2402812c1b | -0.3605 | -50.056198 | 2024-12-23 00:24:00 | METOP-B | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36a9c6df-654d-30cd-bc86-b1458ef918ca | -4.5182 | -42.971699 | 2024-12-23 00:24:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57b4957c-9003-36f8-9234-7a9eec978059 | -3.9212 | -46.8955 | 2024-12-23 00:24:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2fcb3abf-551e-31cf-8f4d-e3977dbe68c3 | -1.699 | -52.573898 | 2024-12-23 00:24:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f00e741b-7449-3a40-a4b7-932482940f9c | -1.7049 | -52.416698 | 2024-12-23 00:24:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abafec20-2efa-3e95-8667-55d64f82148b | -4.0617 | -44.102001 | 2024-12-23 00:24:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39c01a9a-206d-382f-b263-9a6bf3ddac2e | -1.7284 | -52.567402 | 2024-12-23 00:24:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97869fe3-41e2-3b25-9c83-5087e5284c10 | -16.3668 | -39.5462 | 2024-12-23 00:24:00 | METOP-B | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0f222896-1ea3-3635-9293-4f15f92e15ba | -1.7031 | -52.408501 | 2024-12-23 00:24:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4171e90f-e866-37e4-b309-350534d0da93 | -4.1461 | -43.668598 | 2024-12-23 00:24:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5499a16e-7431-37fc-bc9a-c09391d914eb | 0.0624 | -51.103401 | 2024-12-23 00:24:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 27c140d8-98d0-3f30-80ad-2341c350777c | -5.4493 | -44.800301 | 2024-12-23 00:24:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 076b35d2-7731-38bb-b815-fe498bb223ff | -3.9164 | -46.919701 | 2024-12-23 00:24:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a78e6202-2ca5-3c4a-85c1-ba2ea9cc8b42 | -1.3632 | -53.689201 | 2024-12-23 00:24:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8966ebfb-21af-3738-94f5-8ea1b2d3af22 | -1.7205 | -52.5779 | 2024-12-23 00:24:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a99dd5b-0cb3-30c4-bfef-0d84d463d9ec | -3.9317 | -46.355 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| af537826-1416-3d2e-89d7-7ed8afc28675 | -1.373 | -53.687099 | 2024-12-23 00:24:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efe478fb-78e9-3847-bb0a-1128644d31d0 | -1.7266 | -52.559101 | 2024-12-23 00:24:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1496ac42-5755-30a7-a799-f512a5dcb4f7 | -4.3227 | -48.942402 | 2024-12-23 00:24:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ff702eb-9f9c-3c2d-a629-a84160c3bd25 | -4.0738 | -44.109699 | 2024-12-23 00:24:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b75d7e2b-e498-39e3-9925-c52316c76a7e | -4.1411 | -43.647202 | 2024-12-23 00:24:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a72ed4bc-49a0-3fce-a312-92700f251c70 | -4.1509 | -43.645 | 2024-12-23 00:24:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 516bb75f-19c6-3974-bea0-f9a51d4c91db | -1.3611 | -53.679798 | 2024-12-23 00:24:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5a3841f-33fa-38c8-9580-a075ccd8cee8 | -4.0858 | -46.8041 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 85cde247-c41c-383b-8bef-fd89cf9a2473 | -4.1778 | -43.627602 | 2024-12-23 00:24:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78808de2-b002-3005-a686-58c8e052a90e | -3.8063 | -46.8437 | 2024-12-23 00:24:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ec0eecf4-69d0-3615-bf18-a313f0b51d6f | -1.0651 | -53.597198 | 2024-12-23 00:24:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be350183-77ac-3a98-a574-592e5d035235 | -4.19 | -43.635899 | 2024-12-23 00:24:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36f0afbd-2599-30e4-9cd0-7072178c112b | -1.7067 | -52.4249 | 2024-12-23 00:24:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2c56d1a-5157-36e4-966d-9444d97b831f | -6.0026 | -45.410099 | 2024-12-23 00:24:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48f59c2e-ab14-3d1a-9527-4d4a230312ba | -4.4526 | -45.302101 | 2024-12-23 00:24:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2654051-4ab3-31c4-b170-48cbb33531fe | -1.795 | -52.1763 | 2024-12-23 00:24:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14620b6d-d4cd-32d6-9abf-2062d16f34bd | -4.064 | -44.112 | 2024-12-23 00:24:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89d5b288-8a5a-3aff-9a5c-789da3731e33 | -4.0161 | -46.905102 | 2024-12-23 00:24:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 07d76934-0c8f-3a20-bd80-8c9a0f5f0c93 | -3.9807 | -46.344002 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 290ad260-c92e-36b5-a898-dfd9446f72ae | -5.4513 | -44.809101 | 2024-12-23 00:24:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03b6d93e-1715-3bf1-a94d-32f69a0830c2 | -4.1607 | -43.6427 | 2024-12-23 00:24:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 460f969c-971a-3804-abfc-4aa1441e2d57 | -2.4073 | -54.182598 | 2024-12-23 00:24:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8ef2f33-5d77-3f04-9f86-b27da8050d10 | -3.9228 | -46.902802 | 2024-12-23 00:24:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4a9e5007-5894-3585-ac2c-1ef59bda97ef | -4.5155 | -42.959999 | 2024-12-23 00:24:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c54311c-9438-3be6-b2ff-8a045b69d041 | -4.0455 | -46.402 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ea5b0bd1-140a-304b-9cc8-370cdf36724d | -4.0824 | -46.789299 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d6cda14-eb1f-3701-aaf1-a4a0adae50be | -4.2402 | -46.939301 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 31910ab4-e5a1-32b9-b004-5edf46c56d06 | -3.9871 | -46.7327 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4d1f5bdb-6286-3278-8b57-eda5acc4a957 | -3.9181 | -46.927101 | 2024-12-23 00:24:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 42839254-3bc8-30cf-8bdc-8510e89662d0 | -4.7268 | -43.247299 | 2024-12-23 00:24:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
