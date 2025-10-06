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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f683b696-32d9-3781-a76a-25ef18342ab0 | -7.0384 | -44.341 | 2025-10-06 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| ba118445-bc06-3936-862c-c829a7a678ad | -13.2586 | -48.4635 | 2025-10-06 14:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| c184804a-a9cf-3f34-833e-a7bd69f39e20 | -10.8597 | -47.9842 | 2025-10-06 14:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 9a28ad63-c95b-337c-be8d-42164691d0cd | -11.487 | -43.4981 | 2025-10-06 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 73a51435-31d1-3d8d-abba-9b33415ebe57 | -11.0697 | -47.9147 | 2025-10-06 14:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| f445f395-28c0-3722-81ea-3cd2fc898a9d | -6.9987 | -42.8308 | 2025-10-06 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 177.2 |
| 533ce2e6-38fb-3e14-86b3-d3c4e6291f0c | -11.6849 | -45.2872 | 2025-10-06 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 2aeee2f2-7ae3-3506-b3c8-da99a02ebeeb | -11.4298 | -43.4833 | 2025-10-06 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 91fe2510-e403-39ab-a4ca-b7b9f5b19f26 | -10.1383 | -45.4725 | 2025-10-06 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 136.8 |
| bda64085-1b65-33d6-a83a-0751e2209c73 | -8.6141 | -46.3003 | 2025-10-06 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 7c4c7a1b-c097-37c0-90b0-a073bb2959fe | -15.3546 | -47.3007 | 2025-10-06 14:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 5c2180eb-7fad-31be-836b-f1a9ee398aa5 | -13.057 | -47.9155 | 2025-10-06 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 02c59767-9a0a-317c-94d0-273d18ee5eb0 | -7.2094 | -45.8942 | 2025-10-06 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| bf58345c-749c-3964-819a-fb89914db6e7 | -10.1389 | -45.4268 | 2025-10-06 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| ab3a17a6-7009-3c98-8d05-816c015c58a2 | -9.6617 | -45.644 | 2025-10-06 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| b4d36bfd-6b30-32bd-8f0e-9c8871b8a1d5 | -10.1199 | -45.4292 | 2025-10-06 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| dd5f12b2-fa31-3885-b775-dfd462d91d9c | -7.2392 | -44.8727 | 2025-10-06 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| adb3fe71-6bce-39e5-baa2-d649c7de147e | -6.5989 | -45.1101 | 2025-10-06 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| cb5957ac-59cf-38a5-8f1d-e620599c3eeb | -8.5193 | -46.3547 | 2025-10-06 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 949ab880-0141-3686-9f34-d9e2c6a67838 | -10.1573 | -45.4701 | 2025-10-06 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 6535e200-7e92-3bbd-ba70-d41a4f740288 | -9.6804 | -45.6645 | 2025-10-06 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 6397426f-2784-3a47-a706-39dcaf64b38f | -6.6758 | -41.3819 | 2025-10-06 14:00:00 | GOES-19 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| c14222cc-89f5-35ed-ac56-5b08797b2712 | -13.2393 | -48.4662 | 2025-10-06 14:00:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| e66936f7-a24c-3442-9252-95a5f6b81c02 | -9.959 | -48.7425 | 2025-10-06 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 626112aa-2b6b-39c5-9138-d48717b314ee | -13.3237 | -48.0547 | 2025-10-06 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 0c0e9026-8ca0-365d-986c-9761ee50d733 | -7.348 | -45.227 | 2025-10-06 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| c42b0b69-1d42-3105-8617-7c2154dbaf8e | -7.272 | -45.3019 | 2025-10-06 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 1e8eb16c-d714-3e14-aece-dabad0949ff8 | -11.8033 | -45.0856 | 2025-10-06 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| ba46097b-9ac1-3f8b-8c66-f2077f17cd51 | -8.6703 | -49.4511 | 2025-10-06 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| be39a148-2db8-3d42-acad-9e3f7362163b | -18.2862 | -45.4348 | 2025-10-06 14:00:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 108.8 |
| cb1e4b79-2c31-3883-b8f7-2bed3e8a406e | -7.4091 | -46.5033 | 2025-10-06 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| d67a1dbc-db78-337d-befe-d6dbe19f3bf6 | -17.9616 | -57.5286 | 2025-10-06 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 7de5ac77-3555-3a72-a130-8d0d34aa5ff0 | -11.7908 | -48.0669 | 2025-10-06 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 786767a3-7f8c-3d15-bffb-c2c1228bca96 | -12.8954 | -47.2909 | 2025-10-06 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 94535ffe-abc1-3b70-ada7-7c2a1bc7548a | -16.0038 | -50.8365 | 2025-10-06 14:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 57.8 |
| f8284326-5514-3dde-ad4b-b2149e43029c | -7.2389 | -44.8955 | 2025-10-06 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 3d5d6ec7-b367-3a96-b775-56cff2650836 | -11.1181 | -47.243 | 2025-10-06 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 81d0cc5d-1b9c-3df1-9138-f61ded4966c0 | -7.2964 | -44.799 | 2025-10-06 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 6ba3c864-5c8b-372a-8250-d8f2629cfeef | -15.6616 | -47.5642 | 2025-10-06 14:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 7558564d-d8d4-36b1-9468-c7eec8d2d3e1 | -7.64 | -44.3534 | 2025-10-06 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 58bb18a1-e86d-3d57-b79d-96520448a6c0 | -6.7051 | -42.1473 | 2025-10-06 14:00:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 63.7 |
| 551ce633-4299-3818-a7d1-f8e0e064e4b6 | -7.7885 | -44.5228 | 2025-10-06 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 8a126072-3874-30c4-8a89-357df6d8f826 | -11.4482 | -43.5277 | 2025-10-06 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| e45df572-88fa-3ead-b456-c7d511cb0823 | -8.5004 | -46.3566 | 2025-10-06 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| e158ee6a-c6e2-38a3-8a13-ffcfd1b76923 | -7.5329 | -43.8552 | 2025-10-06 14:00:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 8324e8e0-c0d0-38ad-ab56-215fe8d968f7 | -10.6184 | -46.3646 | 2025-10-06 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 293.4 |
| fef44604-7131-319e-aa5d-f7c8ba1b4b0e | -7.6804 | -42.5728 | 2025-10-06 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 79bc0e5b-eca4-3cab-8a4f-e87ebbe702a2 | -15.2156 | -49.2945 | 2025-10-06 14:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| ae8cbda7-293e-306a-8e22-438e81b2405d | -19.5986 | -44.639 | 2025-10-06 14:00:00 | GOES-19 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 110.3 |
| a1ff79f7-00aa-3fcf-9ed2-1c18337a0725 | -12.4099 | -51.1344 | 2025-10-06 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| d3bfb655-8512-3277-b8ae-3bb01551b6e2 | -8.5196 | -46.3323 | 2025-10-06 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 2e7232b2-65f9-308d-95c8-97f14b529d95 | -11.6845 | -45.3103 | 2025-10-06 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| aadc1a4e-fbc3-3b8e-945e-bdfefed98a44 | -10.6335 | -50.5651 | 2025-10-06 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 6855b9c7-f628-3120-9d61-15cde32cbbe4 | -7.7932 | -42.6082 | 2025-10-06 14:00:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| c18209bc-9a48-3b1f-9c54-15cda193d2dc | -9.9587 | -48.7642 | 2025-10-06 14:00:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| e2d22594-041e-33da-b260-a63347ef8e83 | -10.1393 | -45.4039 | 2025-10-06 14:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 146c9ef3-d63a-36cb-a25f-bbe0fbf6d5db | -15.8868 | -46.2641 | 2025-10-06 14:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d9939c46-df49-375b-a7a2-8d25a2838990 | -9.9215 | -50.1682 | 2025-10-06 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 72bab5b2-6dc5-37db-aa9c-32313dfbbbdb | -14.8626 | -51.5234 | 2025-10-06 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 63b4ee5a-c72a-3126-8d70-aa5cc34ab898 | -10.0028 | -48.3015 | 2025-10-06 14:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 9d3b3ba4-cd02-3d18-aa61-22a6a3d95876 | -6.8454 | -44.8391 | 2025-10-06 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 31dd25ef-a8ce-30d7-9ea2-59f14b9d7dda | -7.2911 | -45.2775 | 2025-10-06 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 25576be2-67cc-3161-9f36-e57618f5bfbf | -15.2351 | -49.2914 | 2025-10-06 14:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 823d4d95-a539-33df-9f12-9597258acd56 | -15.5699 | -47.2854 | 2025-10-06 14:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 3f8d0789-1992-3141-b6bf-a7559bac7165 | -10.86 | -47.9621 | 2025-10-06 14:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 764d4947-0a0f-35d5-922e-3dfbc14a2b6e | -7.7935 | -42.5845 | 2025-10-06 14:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| cc2d41d1-88d0-355a-9c79-5aa8c8b68c89 | -7.7563 | -42.541 | 2025-10-06 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 92.9 |
| 9cdb603d-369c-3cf6-a8ed-de0ea51a6d0d | -6.8388 | -45.4753 | 2025-10-06 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 968b9392-2106-38f1-bd22-3132af3710db | -11.9519 | -46.4352 | 2025-10-06 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| b68d471a-b80e-353d-8f0c-8943ab3b6c02 | -14.9161 | -46.8312 | 2025-10-06 14:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 2509f481-fa70-352e-9c7e-5d70c745b69b | -8.6144 | -46.2778 | 2025-10-06 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 582e0074-25db-3d71-869d-96ea5aa574b1 | -14.6985 | -45.1858 | 2025-10-06 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 61cf5d66-9d9f-369e-96f8-abe9a10317f8 | -17.9813 | -57.5262 | 2025-10-06 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 13191799-dd74-3fdd-9e42-ab149b7e6b9f | -18.018 | -44.9965 | 2025-10-06 14:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 79.1 |
| e7fd3487-4fa2-30b8-a6b0-da08a0a89f2a | -14.882 | -51.5207 | 2025-10-06 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| fe893a4f-83c5-33db-8dd3-30afa063f92c | -7.6993 | -42.5708 | 2025-10-06 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| b00eb60c-fee1-3f7d-b67b-f53356de8d32 | -11.7221 | -45.3508 | 2025-10-06 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| dd065d3a-1189-354c-bc4f-23f23e76644e | -12.4853 | -45.5587 | 2025-10-06 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| f7446949-30c4-37bf-9dae-343e12dec330 | -14.6325 | -52.5137 | 2025-10-06 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 1dbf32e6-2222-3467-a561-403aea69d5cb | -8.633 | -46.2984 | 2025-10-06 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 393.2 |
| 426aee00-b079-3710-89eb-949e6250f05a | -7.6804 | -42.5728 | 2025-10-06 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 59e6a07a-dc1f-3273-a22b-a118a5a7fc2a | -14.6135 | -52.495 | 2025-10-06 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| bbe33cd8-8200-3909-83cf-a2c1b2ce551a | -6.8386 | -45.4979 | 2025-10-06 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| debb2aa6-a44d-3faf-8d49-f7b6ab0848a7 | -7.0367 | -42.8036 | 2025-10-06 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 0df3222d-3c97-3477-bb87-f43affdf47b8 | -7.2776 | -44.8007 | 2025-10-06 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| ac2c4cd3-e5ce-33b7-829a-4b42a6bdffbb | -17.8413 | -57.6459 | 2025-10-06 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.3 |
| 4a55707e-3285-38af-85f0-1d9bcecf30c9 | -7.348 | -45.227 | 2025-10-06 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| db911afc-3ec9-3c62-8dd3-80bf31ffdb1a | -17.8614 | -57.623 | 2025-10-06 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.5 |
| f7028eda-108b-3674-a58e-2da204e738af | -7.4672 | -43.0438 | 2025-10-06 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 5363e934-b225-3879-b677-2a929ded3617 | -15.8868 | -46.2641 | 2025-10-06 14:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 56.8 |
| f6cf8df2-9198-36e7-868f-6db9d6ded4da | -8.5576 | -46.306 | 2025-10-06 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| d9bf5b80-d0d6-30ab-9f31-255fb15be700 | -9.9773 | -50.2267 | 2025-10-06 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 9db99555-7514-3a3d-b7bd-6a72353c4abb | -11.9327 | -46.438 | 2025-10-06 14:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 58eed9e6-9305-3018-bacc-24004f24f8fc | -7.0866 | -45.0914 | 2025-10-06 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| ef196334-e47e-3ded-84a6-693d8f439e9a | -7.0372 | -42.7563 | 2025-10-06 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 5291ab6d-131e-3e7d-8bef-8414572035d4 | -15.5704 | -47.2625 | 2025-10-06 14:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 85.9 |
| d336918a-acc5-3412-a081-8c3e84832f9e | -17.842 | -57.6048 | 2025-10-06 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 4362bc46-87fd-311f-883f-760537ac2553 | -14.8828 | -51.4777 | 2025-10-06 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 476.5 |
| 28697c4a-2d39-3ddd-8d8e-d9eb9efedd7f | -6.7051 | -42.1473 | 2025-10-06 14:10:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 437a41a1-12b6-36eb-8cc8-48de292eeee0 | -17.8417 | -57.6254 | 2025-10-06 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.7 |


[Clique aqui para ver as próximas entradas](README94.md)
