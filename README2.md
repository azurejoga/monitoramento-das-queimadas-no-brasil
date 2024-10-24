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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58ca13b0-bb44-340b-8c7c-885abec4aa37 | -4.5698 | -43.9967 | 2024-10-24 00:15:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| ba243f37-842c-347a-aec8-981f145c0ea9 | -4.6346 | -42.8068 | 2024-10-24 00:15:32 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| ca6218dd-4c7b-38ba-ad0a-de983c55cb25 | -4.6348 | -42.7833 | 2024-10-24 00:15:32 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 241aa7a8-e9d8-3657-9d44-c3b87ca00e5f | -4.5572 | -45.8128 | 2024-10-24 00:15:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 42e90056-be06-34a4-968c-ca572c4d98c9 | -4.5574 | -45.7905 | 2024-10-24 00:15:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 218642b7-f300-3b8a-af13-3deaa739ef28 | -4.6586 | -44.6328 | 2024-10-24 00:15:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 0a5b92b1-100f-30c2-be7a-767563e6e252 | -4.6588 | -44.61 | 2024-10-24 00:15:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 183.8 |
| b23bfdd7-1663-30fc-b5eb-96aa762b7be0 | -4.6775 | -44.6089 | 2024-10-24 00:15:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 11d0dcc9-f000-3721-81c9-0d8c54f8447b | -4.758 | -46.4033 | 2024-10-24 00:15:33 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 4f8becf0-9b69-341b-a70f-75c49ab18f51 | -4.8423 | -45.0309 | 2024-10-24 00:15:34 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| b2940f7b-e861-346c-9e39-43d3308e6b3b | -5.2935 | -47.0129 | 2024-10-24 00:15:36 | GOES-16 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 4c2585e8-1478-3b0d-8bcf-f83bbfcc656c | -5.5903 | -44.8914 | 2024-10-24 00:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 2a6d7f3b-8187-3740-9295-050abf97af92 | -5.8502 | -47.2854 | 2024-10-24 00:15:39 | GOES-16 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| dd440412-9eed-3f53-a0d8-e3c7c7d7ad68 | -6.7427 | -40.4735 | 2024-10-24 00:15:44 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 61.6 |
| 77f49426-a505-34fc-a09c-f07e33415c3f | -6.9272 | -40.8466 | 2024-10-24 00:15:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 167.4 |
| 058f9f39-bc2d-3aa0-b0d6-bb2f537632a1 | -6.9459 | -40.8692 | 2024-10-24 00:15:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 0d77959d-9e39-36f4-b782-3b22c38e812c | -6.9461 | -40.8447 | 2024-10-24 00:15:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 244.3 |
| e9f97adc-08f0-3d19-9e5c-11750a53ea79 | -6.9464 | -40.8203 | 2024-10-24 00:15:45 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 63.3 |
| cd8b7ed7-4435-397b-998f-dda8b2e9f493 | -7.0979 | -45.7914 | 2024-10-24 00:15:46 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 2f154ade-065c-3a97-bb33-e7e50812b806 | -7.481 | -63.5577 | 2024-10-24 00:15:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 87f00754-e485-3c32-b5cb-7eb3ca38020d | -7.4995 | -63.5571 | 2024-10-24 00:15:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 2c515eda-6d66-3fb3-8ef0-0e28c61f08ae | -10.1971 | -53.8617 | 2024-10-24 00:16:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| c0ed030f-7dba-3c38-884b-8790b3b19908 | -11.5924 | -48.5544 | 2024-10-24 00:16:12 | GOES-16 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| a84eeef3-7cb8-3eaf-8c01-d1a087f05276 | -12.1404 | -43.4659 | 2024-10-24 00:16:14 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 4648f2b4-7731-398a-9b7c-141780cc9dfa | -12.672 | -43.8517 | 2024-10-24 00:16:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 50ef28b5-b6df-363b-a999-1c942713ba34 | -12.6914 | -43.8484 | 2024-10-24 00:16:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 2316d3ec-928b-35ff-b206-1e58999bb64c | -12.6918 | -43.8247 | 2024-10-24 00:16:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 0c86f1d5-434f-3c3c-9186-6c720a37f63d | -12.3595 | -63.864 | 2024-10-24 00:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| d5eae929-e42e-3544-b106-216c0c4eefab | -12.3783 | -63.863 | 2024-10-24 00:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 89.8 |
| a24641e5-43a5-3b41-bd00-f30924d6e3f5 | -12.3785 | -63.8439 | 2024-10-24 00:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 26688e09-849d-3297-b23f-055400bf4d0d | -13.7609 | -54.0661 | 2024-10-24 00:16:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| cebde36d-7791-3c4b-bdff-650871b5b153 | -13.7612 | -54.0453 | 2024-10-24 00:16:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 6af2a251-94dd-3ab2-901b-8bbe7ce52d47 | -14.2703 | -51.1328 | 2024-10-24 00:16:27 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 1db91bcf-47cb-368f-bb65-e4c5265515e7 | -14.9145 | -45.1224 | 2024-10-24 00:16:29 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 2e51aa10-3e22-315c-9f26-ecd558e80175 | -14.9341 | -45.1187 | 2024-10-24 00:16:30 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 68.2 |
| fd0503de-1892-3052-87f1-b775b7e726cd | -15.5389 | -50.6688 | 2024-10-24 00:16:33 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 110c1d4d-764c-3337-8ef0-7a03c47b8985 | -15.5393 | -50.647 | 2024-10-24 00:16:33 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 128.8 |
| c1270c24-2d6f-3dc0-96d5-8ff67700bbcb | -15.5584 | -50.6658 | 2024-10-24 00:16:34 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 223.8 |
| e99933e2-4d2f-3d95-a5ce-32a5175cd8e8 | -15.5589 | -50.644 | 2024-10-24 00:16:34 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 250.8 |
| 5067b0fd-0e35-3b5b-9ae8-bc8f0f1c7def | -16.94 | -57.5268 | 2024-10-24 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 2f1ecb10-d8ab-326e-a29a-94e1cc013164 | -16.9596 | -57.5245 | 2024-10-24 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.2 |
| df7726f9-4bef-3bd4-877b-dca6641df289 | -17.0207 | -57.3743 | 2024-10-24 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 0c9caea9-416c-3cae-8539-0f973a78e261 | -17.0596 | -57.3902 | 2024-10-24 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.6 |
| d593a550-f348-3c40-9907-a413136f50d0 | -17.0792 | -57.3879 | 2024-10-24 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.1 |
| 28d0ee3e-3229-34a3-bc8a-71be1aad59fb | -17.2383 | -57.2462 | 2024-10-24 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.9 |
| bcb1e616-1168-3a46-908a-e3409a940fd7 | -17.2579 | -57.2439 | 2024-10-24 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.0 |
| 289c9d65-1fc1-37fe-968f-ea647554494f | -17.6671 | -57.4616 | 2024-10-24 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 0ac448fd-eeb5-380c-b24c-2d9d198c2e72 | -17.6865 | -57.4798 | 2024-10-24 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| c317fdcf-562d-35c3-a60e-4a0fe91318e1 | -17.6868 | -57.4593 | 2024-10-24 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 6258f8f8-633a-3ea4-8d10-d9486cd53b36 | -17.7062 | -57.4774 | 2024-10-24 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |
| 3f53ff11-8490-3858-b2b2-360edd036a94 | -17.7453 | -57.4933 | 2024-10-24 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 6b7dfb15-645d-3f9f-bc52-13da4c15927a | -17.7456 | -57.4727 | 2024-10-24 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 8bb4b154-137b-32e7-b40b-aa03448a9b1d | -17.7634 | -57.5937 | 2024-10-24 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 0aff5d26-6b67-39b5-ae9a-772067fd6db8 | -17.7637 | -57.5732 | 2024-10-24 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 17e51960-4440-3599-8971-f9bc90d07aae | -17.765 | -57.4909 | 2024-10-24 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 10eb90a5-36b9-324a-b2ba-1d9831b400e5 | -17.7831 | -57.5914 | 2024-10-24 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 181941bc-1a10-3e9f-834b-bf619eb48cc4 | -17.7834 | -57.5708 | 2024-10-24 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.0 |
| 403619de-894f-36a6-a5fd-7d42c31480ec | -17.7841 | -57.5296 | 2024-10-24 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.6 |
| 14e60e55-5800-3f97-b236-454d7756e9ca | -17.7844 | -57.5091 | 2024-10-24 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.2 |
| 17eeeea1-a343-3aef-b095-4ebbf1486d12 | -17.7848 | -57.4885 | 2024-10-24 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 61ac155b-7973-38ee-b8ee-30033b6d4d3b | -17.8423 | -57.5842 | 2024-10-24 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.1 |
| 94319bc2-f8e4-3010-b918-34aed362db28 | -17.9469 | -57.2216 | 2024-10-24 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 44993c31-80c0-3765-a6fe-050b24bf3a21 | -17.9667 | -57.2191 | 2024-10-24 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 9e70cec9-ce1a-3f24-beaa-a1931737611d | -18.0639 | -57.3101 | 2024-10-24 00:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.1 |
| 16a816f5-e0a4-36a0-833d-c9fd73fe4bb3 | -18.0834 | -57.3283 | 2024-10-24 00:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.2 |
| b63b20ec-75ba-3af4-b9ff-b86300920463 | -18.0837 | -57.3076 | 2024-10-24 00:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.8 |
| 63471a2b-8332-3228-97b8-e3e81668c345 | -18.1032 | -57.3258 | 2024-10-24 00:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.0 |
| 07dbc20a-5d0d-31cd-81ba-7643696cf64d | -23.816 | -55.2713 | 2024-10-24 00:17:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| 31a13a13-8334-3d77-a139-2896ea93873b | -1.5878 | -53.3089 | 2024-10-24 00:25:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 322db314-67ab-35ee-98b2-bd14a60923f3 | -1.6062 | -53.3087 | 2024-10-24 00:25:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 82526e04-3cda-356b-9ee0-1dbf6d544c3b | -2.9578 | -50.4407 | 2024-10-24 00:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 0f440d3f-ae52-3b7f-ae5d-709d35135827 | -2.9578 | -50.4198 | 2024-10-24 00:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| b20122d8-ab0d-338c-b7c8-d77f671e70f9 | -2.9763 | -50.4193 | 2024-10-24 00:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| d186f71f-71f5-35e3-8cc9-173903610df5 | -3.0745 | -53.8252 | 2024-10-24 00:25:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 1e50e7e9-e0f8-31e9-829b-4393cbb84488 | -3.1101 | -54.1661 | 2024-10-24 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| b4ad244d-d748-319a-ba65-af819162dbb7 | -3.1102 | -54.146 | 2024-10-24 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| d86edce3-1019-3dee-8f7e-82f1a4710383 | -3.1422 | -50.4562 | 2024-10-24 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 582377ff-fd84-39e8-9a27-6553b9ebf647 | -3.1606 | -50.4766 | 2024-10-24 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 0bdf4034-3d70-3b3f-9ec2-054ee242de7d | -3.1607 | -50.4556 | 2024-10-24 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 24457749-94f3-3121-a46b-b1971e656870 | -3.7066 | -41.6997 | 2024-10-24 00:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| c6859d03-8904-3d1b-8331-f2fe33b8ac03 | -3.7068 | -41.6758 | 2024-10-24 00:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 120.4 |
| b7bc576e-ad91-3dd5-9589-d0731247a590 | -3.7254 | -41.6987 | 2024-10-24 00:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 61.9 |
| 43f0e01c-3c85-3712-b382-1e324e38ac31 | -3.7255 | -41.6748 | 2024-10-24 00:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| de34efd2-7cc2-3de5-a77e-2a708ec99f5e | -3.6612 | -54.2715 | 2024-10-24 00:25:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 6a07cf6d-db39-3b73-beb3-b03632b13f24 | -4.2134 | -44.2696 | 2024-10-24 00:25:30 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 324149aa-9384-3ce3-881f-4679c3680dd9 | -4.2321 | -44.2685 | 2024-10-24 00:25:30 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| ddbac09d-1921-3258-98f6-af6f01a11ef2 | -4.5698 | -43.9967 | 2024-10-24 00:25:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| da1738db-710c-3b93-9b75-f1295d977f2c | -4.5572 | -45.8128 | 2024-10-24 00:25:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| b8a1d8a3-29f1-349d-8549-e69200a0bff8 | -4.5574 | -45.7905 | 2024-10-24 00:25:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 69956482-04df-36a3-acad-f3ebbc4292b8 | -4.5697 | -44.0197 | 2024-10-24 00:25:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| e36e0a71-4a76-34fd-b36f-2ce93fa0e875 | -4.6588 | -44.61 | 2024-10-24 00:25:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| b456f199-4f46-3dc7-9662-51f00761c2eb | -4.6775 | -44.6089 | 2024-10-24 00:25:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 97d7cc83-9aec-3c0d-9ef9-917e08ba052d | -4.758 | -46.4033 | 2024-10-24 00:25:33 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.4 |
| d6b23e04-1245-399b-9fdb-f8f627d53525 | -4.8423 | -45.0309 | 2024-10-24 00:25:34 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 5706008d-01ba-33a2-8e99-fe14afee096a | -4.861 | -45.0298 | 2024-10-24 00:25:34 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| e477693a-968b-3caa-b1fe-a9ccbdb31b95 | -5.2935 | -47.0129 | 2024-10-24 00:25:36 | GOES-16 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| b505e639-7169-39aa-b85a-09cda7c1ea79 | -5.5903 | -44.8914 | 2024-10-24 00:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| e8d8371c-2b04-3aed-b917-e3a1a590b15d | -5.8502 | -47.2854 | 2024-10-24 00:25:39 | GOES-16 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 2712fd2c-551d-3add-8585-21b4e338f7dc | -6.7427 | -40.4735 | 2024-10-24 00:25:44 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 12612962-f410-3adb-ae2d-9634c1dbd254 | -6.9272 | -40.8466 | 2024-10-24 00:25:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 192.5 |


[Clique aqui para ver as próximas entradas](README3.md)
