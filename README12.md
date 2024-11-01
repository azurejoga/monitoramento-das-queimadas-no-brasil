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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9527d354-e046-32c6-bd96-d5756174242d | -4.26532 | -45.75383 | 2024-11-01 03:42:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94949f52-d529-3aaa-9af1-5a20b109797c | -4.08703 | -45.66157 | 2024-11-01 03:42:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25e9999e-fed5-32e8-b50d-e97f207a8273 | -4.08561 | -45.65844 | 2024-11-01 03:42:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74ecce2f-3634-3081-9bac-d44ff3c6425e | -4.08484 | -45.66298 | 2024-11-01 03:42:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a3ca1c2-6ec3-34ee-b952-4862afe0c849 | -4.04648 | -46.0762 | 2024-11-01 03:42:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| aa27a8c9-9553-39dd-bc2a-3cd9fb0615d7 | -4.04594 | -46.07327 | 2024-11-01 03:42:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 1617203f-3b01-31e5-9a6c-b2a42ba4ee0d | -4.04561 | -46.08141 | 2024-11-01 03:42:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| ec0e29b0-24f6-3a31-948d-98f7371811dd | -4.04499 | -46.0787 | 2024-11-01 03:42:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 37e88f0a-1ff3-3e84-abbc-aa86d93e9a61 | -3.94252 | -48.35757 | 2024-11-01 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6219e8c6-b0d7-3f62-ab48-7ce9242cae4b | -3.94124 | -48.36493 | 2024-11-01 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 504aa891-0d98-34b8-a8f1-7f9d9d773a28 | -3.94099 | -48.34972 | 2024-11-01 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92b62a38-6c91-33a6-ac55-5cf2ddf95ade | -3.93972 | -48.35675 | 2024-11-01 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c01000d-275e-32f1-8128-ef8faa2cba5c | -3.93838 | -48.36417 | 2024-11-01 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b81c2f8-9a36-36b5-a2e2-80d8c2451277 | -3.88432 | -46.21246 | 2024-11-01 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 235bcc04-9c39-30a9-ae86-59c7fcca1533 | -3.8835 | -46.21727 | 2024-11-01 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5631567b-8fcb-3381-8871-a0064e65888b | -3.88239 | -46.21161 | 2024-11-01 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bdfbe4a2-60ff-3901-9c22-d5a23673f71f | -3.88155 | -46.21635 | 2024-11-01 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca6a6121-5313-30b6-bd07-bcd13907f749 | -3.56516 | -47.37807 | 2024-11-01 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 063acbac-9bf5-35f0-8a58-557119de58cb | -3.56412 | -47.38409 | 2024-11-01 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 2b88d27f-0045-39d3-9f72-8e1a835cb865 | -3.56305 | -47.39034 | 2024-11-01 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 027fe8bd-f101-3ea7-b235-149ce9bd837d | -3.55838 | -47.3772 | 2024-11-01 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f7945b7a-171e-3985-a62a-d789b797fdea | -3.55736 | -47.38308 | 2024-11-01 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 3393e8f4-bc36-34d8-a38c-d6d949bf11ca | -3.5563 | -47.38927 | 2024-11-01 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 99791057-3b17-321f-bb6b-5828132d58aa | -3.3749 | -45.90825 | 2024-11-01 03:42:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 756f4fd5-b6ba-3de2-af33-32d3feaa9838 | -3.37407 | -45.91311 | 2024-11-01 03:42:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9e24f06-7c36-3e84-8460-ca76d9c2f490 | -3.28106 | -45.97194 | 2024-11-01 03:42:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55120096-0ac8-3a60-a3e9-611cd2114887 | -3.25706 | -45.97108 | 2024-11-01 03:42:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39395c48-0a90-3eb7-90cb-f0f4ccb7e21d | -3.20832 | -46.18251 | 2024-11-01 03:42:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57f6af37-fee3-3ded-8fd0-8e8d77bdf920 | -3.16555 | -45.31479 | 2024-11-01 03:42:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06999e07-1c73-3cb8-9b80-9539770aaeaa | -3.12463 | -46.04552 | 2024-11-01 03:42:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0917d212-e5d1-34f4-9720-650e57344e80 | -3.12379 | -46.05049 | 2024-11-01 03:42:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fad194a3-54c8-3c78-a651-1a81686cea0c | -3.12071 | -45.11119 | 2024-11-01 03:42:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63237baf-404c-3bf6-b5df-0b48b77ffdc1 | -3.11997 | -45.11545 | 2024-11-01 03:42:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7c0ab65-f2e7-3435-967d-49cbbd2a9d90 | -3.11325 | -45.29723 | 2024-11-01 03:42:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 802024ba-c497-3dd7-8bea-8663e6213560 | -2.97538 | -47.92379 | 2024-11-01 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b10f4d37-a2d4-3b91-b2af-7e7b9615a88f | -2.92606 | -46.7769 | 2024-11-01 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0bf105b-fa09-3673-a9bc-241d353531a1 | -2.92508 | -46.78249 | 2024-11-01 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bef5ddf0-93b5-35a8-ac16-5ab5bb8737ee | -2.62103 | -45.14457 | 2024-11-01 03:42:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e8fa422e-2c82-3713-b688-086a494f0ac5 | -2.39856 | -47.72486 | 2024-11-01 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a95a890d-ae2a-3864-8924-896d3df88e4b | -2.33587 | -46.12688 | 2024-11-01 03:42:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5998747f-77bb-3e18-8c56-3586bce53a14 | -2.33501 | -46.13198 | 2024-11-01 03:42:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33a91525-0859-32ff-90b9-c6e4c1f38c11 | -2.31334 | -45.73993 | 2024-11-01 03:42:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38a0102a-4d54-3586-92d2-06a99f4ea271 | -2.30424 | -46.82402 | 2024-11-01 03:42:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9081a5d6-90eb-359e-8df1-3ad4bacbec1e | -2.30011 | -46.82251 | 2024-11-01 03:42:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8726967b-f433-336d-8c88-9b582a99aa7c | -2.29906 | -46.82887 | 2024-11-01 03:42:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0de26796-bccc-3ee1-9818-11708df05418 | -2.2976 | -46.82296 | 2024-11-01 03:42:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 858baae6-38ec-398b-837c-06ff69af6f64 | -2.29652 | -46.82924 | 2024-11-01 03:42:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a940cc4-cb38-3d76-89d6-3d0484c835f6 | -2.29242 | -46.82774 | 2024-11-01 03:42:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| de74a6eb-7ae7-3e77-96cc-b2010c1a8b5d | -2.25961 | -46.65777 | 2024-11-01 03:42:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5e7da18-2967-3296-a2c0-8faf2944c723 | -2.25866 | -46.66344 | 2024-11-01 03:42:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1f2b4b8-7e63-3b7a-9e41-c84159eb1c6e | -2.24984 | -46.60294 | 2024-11-01 03:42:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c56e6747-f02f-367a-8eb5-2b17382078ac | -2.24893 | -46.60854 | 2024-11-01 03:42:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92d3a091-a242-3fdb-8e0e-eb7651b6340e | -2.24842 | -46.60418 | 2024-11-01 03:42:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9298f78e-4047-333a-ac30-108d132b22c7 | -2.20646 | -46.4991 | 2024-11-01 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb2cb33f-11e6-36ad-92f2-be477f63f285 | -2.07381 | -47.12844 | 2024-11-01 03:42:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e982785d-dccb-3451-a4eb-a4d7fb9fffd9 | -2.07278 | -47.13454 | 2024-11-01 03:42:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3bac6a6e-0d94-3b70-98f0-58f97210cf40 | -1.98888 | -45.61303 | 2024-11-01 03:42:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fdd66b1d-1bdb-3309-9e37-96a09a2ddcd8 | -1.98838 | -45.60791 | 2024-11-01 03:42:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbaf8107-0d3e-3ead-ba86-de5e25d2f35d | -1.98758 | -45.61265 | 2024-11-01 03:42:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b0b7bc0-dde9-34ac-a677-f9835c5b80d1 | -1.97125 | -46.42719 | 2024-11-01 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccb3c987-393f-3893-a888-01ad442ebf97 | -1.96472 | -46.42616 | 2024-11-01 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f46fcf8d-08a1-3795-94de-dfef7e4abbcd | -1.23441 | -47.73845 | 2024-11-01 03:42:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce127ebe-9f15-3099-a129-e6c796bde74f | -1.04332 | -47.78851 | 2024-11-01 03:42:00 | NOAA-21 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8fa5aef8-d5b0-347e-8555-5799f24615f4 | -9.85138 | -36.50853 | 2024-11-01 03:45:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9e59f6ab-b6d1-3f7d-aa56-67805ec95984 | -9.84972 | -36.49749 | 2024-11-01 03:45:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1e5f2994-aab7-34cb-8426-b6e6adb52053 | -9.84917 | -36.50099 | 2024-11-01 03:45:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9dde5e9c-7b6e-312b-b49f-4df15b6a96a8 | -9.84862 | -36.5045 | 2024-11-01 03:45:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b3b0a08d-04d4-3859-8eb7-2e536ca49265 | -9.84807 | -36.508 | 2024-11-01 03:45:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| fc420656-0147-3820-9182-a8dbbed96fee | -9.84641 | -36.49696 | 2024-11-01 03:45:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3166d1c0-09ef-3e4e-b846-ce76bc53aa5a | -9.84586 | -36.50045 | 2024-11-01 03:45:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1d6fae17-92ff-32fe-9095-2e0333dc2eea | -9.84531 | -36.50396 | 2024-11-01 03:45:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| ab99d37e-820d-312d-87d1-666dce489877 | -9.84476 | -36.50747 | 2024-11-01 03:45:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 61974ca6-7e8f-34d9-95ca-6654ffc73f68 | -9.8431 | -36.49643 | 2024-11-01 03:45:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6ee05ebe-d337-3ba9-a713-a0924167e7a4 | -9.84255 | -36.49993 | 2024-11-01 03:45:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 930ea3eb-4386-33b1-a9fd-4d1b0a1fb316 | -9.842 | -36.50343 | 2024-11-01 03:45:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 11be8188-739c-39e3-8a9f-13b7b63e185c | -9.84144 | -36.50693 | 2024-11-01 03:45:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 219c3438-dc92-302d-bb99-11068789ae23 | -9.84089 | -36.51044 | 2024-11-01 03:45:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e8767ec9-baa5-36ea-ac5d-1a7564d7084d | -9.83868 | -36.5029 | 2024-11-01 03:45:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1750e1fb-a93a-3231-a0d9-c9fe63a7325a | -9.82767 | -41.79163 | 2024-11-01 03:45:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 28a5df47-25cf-3238-a79a-f200b9a74571 | -9.81063 | -35.8795 | 2024-11-01 03:45:00 | NOAA-21 | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4531b599-fd2e-3b77-bcfd-5ed7cef9a1f3 | -9.46931 | -40.5612 | 2024-11-01 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4d57becb-ba45-30db-ba05-21d4bd41b173 | -9.45656 | -35.53078 | 2024-11-01 03:45:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b8575a91-8c37-3feb-bd4f-8759f72dd4a6 | -9.38232 | -40.33775 | 2024-11-01 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 03aee679-a533-3899-a8e5-2150fc56e623 | -8.92917 | -35.22591 | 2024-11-01 03:45:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a3ace861-ee22-31c0-918f-8aaa1da93fcc | -8.90524 | -37.23428 | 2024-11-01 03:45:00 | NOAA-21 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9b1bc922-ab5b-3e1a-81d9-4cb3e53fe66f | -8.81632 | -40.17566 | 2024-11-01 03:45:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 254e1ab9-fb00-371c-ac4a-707a24fadbac | -8.81244 | -40.17501 | 2024-11-01 03:45:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 36c6e377-7e55-35cc-91d3-03a94f8628af | -8.68829 | -39.63276 | 2024-11-01 03:45:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 982e54ae-84cc-3833-90c6-5c3a4acb7a2c | -8.67866 | -40.20559 | 2024-11-01 03:45:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| dc3aad21-c1b8-3b61-bddb-6c2c0c4a13c7 | -8.39213 | -35.02745 | 2024-11-01 03:45:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6522883e-841e-39e0-af1d-97a5efe5a855 | -8.09466 | -35.36836 | 2024-11-01 03:45:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5ab90b48-9290-3a65-9955-7b057e1142ae | -7.22338 | -44.01999 | 2024-11-01 03:45:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39cf6454-d0a9-33a2-ba82-ccd9116b0fb6 | -7.21827 | -44.01899 | 2024-11-01 03:45:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00121fa3-a2a8-3186-a749-203473ef2ca7 | -7.21771 | -44.02207 | 2024-11-01 03:45:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a90503fe-263c-31ee-869f-417474f7c8e9 | -7.2115 | -42.18224 | 2024-11-01 03:45:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| a7366c4d-36b1-3f55-a001-e6a35065c5a9 | -7.20698 | -42.18138 | 2024-11-01 03:45:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| e6126b21-9f69-32d9-9c7b-7846d0f0f0ba | -6.91555 | -40.47083 | 2024-11-01 03:45:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2505940b-2dd4-3d5d-af6c-9934c108b399 | -6.90886 | -38.46309 | 2024-11-01 03:45:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d4196767-2b32-33e4-90c6-3346df18528d | -6.90819 | -38.46725 | 2024-11-01 03:45:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 39e5bbc6-49da-32de-89ee-83c21409b544 | -6.90751 | -38.47143 | 2024-11-01 03:45:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.7 |


[Clique aqui para ver as próximas entradas](README13.md)
