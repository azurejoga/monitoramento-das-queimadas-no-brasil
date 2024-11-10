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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5303b8d-97f7-3249-9395-890e44e7c161 | -2.11354 | -50.13939 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88353d71-ca59-3485-8928-2a2f5f3898ec | -1.61678 | -47.35629 | 2024-11-10 04:36:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba700924-26f2-3343-bf30-9e9e27264af4 | -1.54912 | -52.27266 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc69c141-48ec-3d1a-b4d1-9d130c24b4db | -2.55113 | -47.32383 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ab98cd3-98f8-3599-a440-044bcbec7c32 | -2.1378 | -48.7972 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32ee8eea-b6e0-36af-a33e-658aff10b2d0 | -1.95743 | -46.80848 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7adb0482-6dbd-3bb0-8a9f-a5f70982e262 | -1.11497 | -51.7572 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7006fe90-57d6-3bd1-80dc-21b1ef29eb34 | -1.67688 | -52.05461 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| de430555-4b19-3111-9b6c-d8e9222fdee2 | -1.75841 | -48.52188 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8eedc66-5f88-3760-b79c-a797d9d7ae49 | -2.62731 | -46.15261 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53433b5f-5ea8-3c84-8957-e252c9774674 | -2.20122 | -46.79003 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ead51ad-8948-33e3-8161-59d4b262dbe0 | -2.09527 | -46.77383 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dce50632-9506-3e77-a225-5538274a77ab | 0.33522 | -51.54799 | 2024-11-10 04:36:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78b03e64-ed48-390b-a437-94fbae0f0ee2 | -2.6308 | -46.15314 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47452602-9eaa-309d-80af-770082fba9c6 | -2.35034 | -48.93005 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edc4c729-3697-3bca-b108-d042a27e44f1 | -2.407 | -46.29549 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0ae406f-ad7c-3d2c-9d50-ada5fb0cf305 | -2.38201 | -46.59311 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfd8f058-1554-3a26-baaa-bfa43e716074 | -2.02323 | -48.02018 | 2024-11-10 04:36:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9256aa6-a80e-3b8a-8376-efa3fdc739a9 | -2.18622 | -48.3174 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80d26c16-db5f-3f15-984c-ce92fef60bb6 | -1.23153 | -51.75107 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15a4cd8d-7c0a-3e72-8c55-8799bfd916e1 | -2.10424 | -48.90187 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d75b0f3e-f784-3a92-a113-22d70cc91cbc | -2.28507 | -47.92631 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 712f6759-0020-3de7-b1b4-f834bfae781f | -2.33381 | -46.56714 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08938c3e-6e57-381b-bb3c-cf5556c6a981 | -1.5898 | -52.18953 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 067719f2-9c84-372c-8163-7b0bd8b08760 | -2.20035 | -49.52228 | 2024-11-10 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 576a41e3-b29a-3e10-b2e1-9b4d61c5dfe4 | -1.57664 | -50.44653 | 2024-11-10 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb4f5421-607b-3e0e-a8f5-c53cfa41d3ca | -1.25169 | -51.76772 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 02397bf9-36b5-37b0-8526-fe39e5babf21 | 1.62124 | -56.05469 | 2024-11-10 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d628edcb-ec71-360a-ad79-36fce7cd08f8 | -2.29167 | -46.4773 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d25c3c0-354c-378d-909e-8826e7dee365 | -1.94891 | -51.10432 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d18b40dd-cab0-3e80-9fcf-110e79b0ea7c | -2.21377 | -48.85163 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b63d99a-e5c4-39b0-b261-9fb9cec7ac9a | -2.3087 | -48.55175 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f898045-4559-3712-a013-9386018c0bae | -2.63907 | -46.80064 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 278ba9cb-aa30-333b-a6ef-f60567722eb2 | -2.12516 | -48.55851 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 512f84a6-5010-3d8e-8fb6-a60f0570ba2f | -2.29971 | -48.50093 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d3d7c78e-8a67-376c-a257-b5d9b5a7b29d | -2.24775 | -48.70119 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0388ffee-4687-3068-82f1-13e2586b1832 | -2.07339 | -48.62815 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8131b7a7-3d1f-3148-a6dd-6c041ddfd1ee | -2.09715 | -50.2198 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5d14344-eba9-300b-bd1e-d2be52c81198 | -1.18443 | -52.16703 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0132abf3-a512-3297-a9b6-12c5b41f6d25 | -2.24362 | -46.56079 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 527733bb-6fd6-398d-8a2b-e509a304261f | -2.19196 | -49.53184 | 2024-11-10 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3534dfd9-f106-390b-8792-6181d32a4a71 | -2.16971 | -46.40899 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69c73aeb-0fdd-38d2-8101-d0b485d05f0d | -2.09796 | -46.53494 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb811a13-aa85-325a-8cdf-da0f6ebf3240 | -1.24728 | -51.77151 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a7f80f09-a497-328d-aa27-72a481380f43 | -1.19549 | -52.00037 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 56605185-0d88-365f-a1c5-ab6c0ae6c7dc | -2.18297 | -48.33806 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c721256-d241-3559-8237-c30c3abcbc54 | -2.20557 | -49.51974 | 2024-11-10 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48d87652-6ba0-39e6-8a38-1771b5454173 | -2.88837 | -45.36619 | 2024-11-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| da8b4b2f-fd3e-3185-89ba-bd638fa0de76 | 0.12658 | -51.23746 | 2024-11-10 04:36:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4ceeb70-40b5-38d4-942a-43a4e222246a | -0.4092 | -51.99069 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0850a3b6-1707-3688-9ebc-e79d26c9cc62 | -2.38252 | -47.93084 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91e1e3d4-0b40-3441-a68a-3d8512b08f12 | -2.21045 | -48.85111 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2d96a61-d393-35cb-b2a3-a419b47b6bf6 | -2.66973 | -46.78297 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9eac5ea-2486-36dd-b500-1f10d6fc916b | -1.62562 | -52.23278 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eec8e71f-69bf-3f17-acea-c25ee7603e9c | -2.22839 | -48.37335 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d93a06a-59c8-3fe7-917a-cf26e284f4b3 | -2.08721 | -48.82135 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9ad6c7ac-094b-33e7-a648-3aaad93933e7 | -1.39411 | -54.64935 | 2024-11-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e05e2f0-3b7b-308c-b70e-7aac10a0ffe0 | -2.562 | -46.53685 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5fb2664-6d80-3c15-9790-b63a131af387 | -2.32084 | -46.49321 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5df616f0-6408-3e35-87dc-1f9fd4e06be8 | -0.04626 | -50.77586 | 2024-11-10 04:36:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be76217a-e09c-3166-8b34-ce2e32e3a9a4 | -1.72973 | -47.97412 | 2024-11-10 04:36:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 941e5c3c-6a62-37e6-be70-b4a7a1e82b7e | -1.24867 | -51.76276 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15152a54-5201-332e-86d0-b53b4d3b4a59 | -2.59456 | -46.17191 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71e81375-d0e5-3206-8da0-0faa07651fef | -2.30186 | -49.10739 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1081f066-09dc-3b54-92a5-24cb5ddf4699 | -2.25948 | -47.06072 | 2024-11-10 04:36:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1b5f1021-a14c-31b0-a3f4-51e1fd40a149 | -2.14339 | -46.86986 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58ee1a5a-f3d3-3d13-bc16-f107c70adce0 | -2.0658 | -48.89249 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9bf5296-2e22-3195-a15f-c5586fd78f19 | -2.17475 | -48.32984 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 125902f8-41f3-31ca-924d-29c4be1d3837 | -1.79901 | -48.06958 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e25d1f7-107d-3dda-b960-3cc3d88f4353 | 1.62591 | -56.05086 | 2024-11-10 04:36:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe3500bc-f1f2-3c0a-9142-cca13f2cc276 | -2.2499 | -46.56554 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a2344ad-688c-3a0c-b3df-c8e9e4089cd4 | -2.67825 | -46.79549 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a67e3de0-f289-3b67-977d-ab83a0de46a3 | -1.46746 | -54.30967 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5be20959-96cc-38fb-bd4a-a6ad05917dab | -1.61733 | -47.35279 | 2024-11-10 04:36:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9d35f4d-2572-33cb-bfa6-68af40c07604 | -1.13088 | -54.19285 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c275e44-cdf7-3c48-97e5-458833e5c1b5 | -1.70324 | -48.16414 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d196c6e1-458b-3c68-a03e-abbdbff3a71a | -2.18415 | -48.5464 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b997dfd-94ac-36b6-a6b7-050438e1cc5e | -1.50945 | -51.50598 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91350d8a-6455-397a-baac-2d3ed499a0ba | -2.66348 | -46.77824 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40d1738e-618f-3e5f-b8fe-6766774673f1 | -1.34317 | -51.42615 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2411181f-7fe7-39da-bd50-8dcf81abf0af | -2.28788 | -48.425 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7f4c645-d6a0-332a-8d39-772d4fc35198 | -1.88113 | -52.12937 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff674ba0-472a-3d0c-ba14-0f5a154c17bf | -1.81641 | -47.98045 | 2024-11-10 04:36:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a327412-7ea6-3633-b418-3ad3ab649646 | 3.37075 | -51.26714 | 2024-11-10 04:36:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b83f3f53-9051-302b-bc8b-c928ce91ceac | -2.18226 | -48.86082 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2fd222f-f104-3d08-a702-21beff8d6ba6 | -2.36031 | -46.79955 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9405826e-024b-34ec-80e2-c3103368ce64 | -1.30638 | -54.66865 | 2024-11-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0462f2fe-0ddc-3ac0-9c6e-30efe17b2658 | -2.03285 | -48.5618 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53d8cc0c-e177-3193-a373-0cbd1d97e49e | -1.16015 | -54.07534 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4282096f-f1ec-345b-8ce9-5f73d52912f9 | -0.14845 | -51.56153 | 2024-11-10 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 87f68094-cc43-3466-a1b2-6f1a91fa4816 | -2.09431 | -50.21558 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56988bf1-f199-3b6b-bcab-c293a4a27173 | -2.20301 | -48.38352 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6930846d-2dc5-33fe-98f8-f8b3075415ef | 0.28326 | -51.26489 | 2024-11-10 04:36:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5b49e6e1-b130-304c-acd3-9ba50a0470dc | -2.05067 | -46.07963 | 2024-11-10 04:36:00 | NPP-375D | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9d69f39-4924-3751-9006-e92ff6ed7895 | -2.18629 | -48.33858 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d03758f2-02b6-3382-9bf9-c3f9be7982e2 | -1.72596 | -52.33163 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b05d40db-ee24-3499-87d6-f09919147272 | -2.20373 | -49.13094 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d42c302-2e72-380a-b4b5-f0cb6886e617 | -2.15304 | -46.6968 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77066a66-87db-34fd-a497-537887e2ea36 | -1.06084 | -53.64997 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab99ba1f-eb82-30be-9aac-f2af56c5763d | -2.29277 | -46.51543 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README69.md)
