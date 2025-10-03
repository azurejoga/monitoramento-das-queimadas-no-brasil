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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0f39404-99df-302b-aa25-3472cf3fcb5b | -11.01518 | -49.81957 | 2025-10-03 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 776843da-2e78-3be6-8197-057409f38bef | -7.25066 | -49.40957 | 2025-10-03 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d898ade-1bd9-3239-a6f3-df1c29892ea2 | -8.56261 | -48.64765 | 2025-10-03 04:32:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89d84a36-da25-3242-b35f-b0e781b453f4 | -7.76769 | -46.27531 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25ee81b4-1584-39d4-9c50-5e3dc5b89c2a | -11.90705 | -46.2655 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02987b10-5047-32b1-a94d-61929d500ce9 | -6.67363 | -42.81951 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 87ecb825-92f5-38ad-846c-b2e95d6d6b10 | -11.10233 | -47.82432 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddc3be8b-efbd-35ae-b7ae-75ef3cbc3a11 | -5.16837 | -46.05576 | 2025-10-03 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4db61d0a-c09a-3600-855c-f8a615514fb3 | -11.56162 | -47.66036 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 722102fd-12b9-3f15-8087-7c1634b5c49e | -7.55526 | -42.40111 | 2025-10-03 04:32:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5d621930-1057-3875-a649-6cb07e10bc23 | -11.80705 | -48.90231 | 2025-10-03 04:32:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0dbf5fc9-086b-3c91-a53b-7bf5180c3b5a | -11.92304 | -46.27943 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fb05499e-40eb-393c-934c-f4e6bcd42999 | -6.95411 | -45.34524 | 2025-10-03 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4bdceed-6d17-33c6-bd36-d8cf92ab6e1b | -9.65096 | -48.20836 | 2025-10-03 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f7e822f3-368d-35c0-ba45-58c67e757801 | -4.9552 | -45.77559 | 2025-10-03 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4801d9ee-b03a-349c-93da-324101253280 | -11.34631 | -44.96583 | 2025-10-03 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61799cfd-9ee4-31de-abb7-ea4f095c8dc5 | -10.10413 | -50.34953 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9770ea7c-7b7c-3a82-8507-109f2259860f | -7.30568 | -45.26691 | 2025-10-03 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb701837-5c60-37c5-8d49-1f2bd1b84ec0 | -11.10567 | -47.82483 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 432be855-098b-3d37-988c-413e38a8aa60 | -6.94594 | -45.35184 | 2025-10-03 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7be87100-2662-37fc-983f-31b14e6bd45b | -7.77739 | -42.50639 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7e80cdbc-3ac6-3cd9-8e3e-25b62d7d65bb | -11.82547 | -45.04156 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdc870e1-b95b-31f9-8f33-fc23c21ec5e5 | -11.63362 | -45.06324 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0d494961-dfe2-3cc7-bcc7-eb0b43b14c4f | -5.73813 | -44.26534 | 2025-10-03 04:32:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66016c20-2db2-3f17-84b0-3db9800bbdf5 | -7.29461 | -44.19318 | 2025-10-03 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 830476be-c2b6-335a-ad41-e41328396ed1 | -5.3438 | -43.75939 | 2025-10-03 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c4a3cffc-9b0f-3413-bf44-4f1e79aa6760 | -11.44696 | -44.96372 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39447006-46fa-3cb5-a151-fb83c3eebd04 | -7.7568 | -42.56189 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 9d7087fd-7ffa-3079-af71-ee634397a6df | -7.79164 | -42.55548 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e404dff0-941f-3010-bb2a-f5f1d8585dfc | -11.62492 | -45.07067 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ec3fc1f-de27-347f-b3b8-7135509856e1 | -10.87707 | -47.04695 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77e6fcf1-0a72-3f2a-87aa-a7cd86d8e396 | -10.89317 | -46.73564 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cec4cdf-fb3f-3bb9-8897-45da35753fa1 | -11.86873 | -44.98402 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a50dd8bc-c625-32fb-9ff5-035527f76431 | -7.75342 | -46.25454 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0d57a97e-d2be-381f-822b-344153e35129 | -9.44936 | -47.58677 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 464cb815-f06f-34f6-bc30-e94e079bb6b1 | -7.77822 | -47.37519 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b25c3304-d981-3a32-b148-ee30e74a518d | -11.43736 | -43.49843 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ad2f8a7-dfde-3414-bb51-25b13a153c8d | -8.64874 | -47.71301 | 2025-10-03 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ac97a20-85d1-3d79-b3fe-1eb86ebd8e0f | -7.25124 | -49.40596 | 2025-10-03 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2f08047-5d1f-3285-a3a8-ede1e4cce4dc | -6.91122 | -45.64989 | 2025-10-03 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb4c1446-a108-3755-a0ef-b4eb4f91c80f | -10.29753 | -48.28582 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9129903f-1aeb-3060-bb1c-1499c237664b | -6.55054 | -43.88691 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff52e45f-40a8-383e-9a5d-746e6b9c8e20 | -7.75419 | -42.56559 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 58.2 |
| 264dfeff-a30f-3552-92bb-2dac9e8a7be6 | -4.51328 | -55.45882 | 2025-10-03 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b66fdd33-a912-39db-9e00-92ee0589efb2 | -7.29469 | -44.18128 | 2025-10-03 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4553fcb4-fa12-3796-8c8c-9e10c9731572 | -11.55435 | -47.66296 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 424bc911-fc2b-32d0-906b-f89223e39974 | -6.6871 | -42.83957 | 2025-10-03 04:32:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 50e53fff-663d-3830-a558-bc81f8a3853b | -10.26741 | -50.36098 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0882cac6-0a2c-3f40-b9f4-dcf3b4b0c596 | -4.62578 | -49.37302 | 2025-10-03 04:32:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e411f5c3-a9f9-3112-b535-06bc311b7d6a | -7.72526 | -46.23143 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0fff4cd6-b9d8-34a4-90ea-4aa2f80b46ac | -10.10596 | -50.27384 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f442b0a9-536b-3ef1-b97a-6105bdfa28e1 | -11.42554 | -43.49284 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4cc13f2-a6eb-32c0-9db5-d9c6463ea212 | -11.1857 | -47.74981 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d06c9f2-7526-3f65-b80f-13f87e50248f | -8.12536 | -50.24241 | 2025-10-03 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48b920d0-e298-3610-a9eb-903729a4ecee | -9.09961 | -46.7247 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c824ee95-568e-3e4b-bc4c-551aa7e86ddf | -4.67071 | -45.80716 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53b60f3a-03f6-30b1-bc6d-000734922e7b | -9.95546 | -43.70094 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1897b914-48e3-3b79-bb39-7e85b80dd0cf | -7.90281 | -43.52906 | 2025-10-03 04:32:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c2fe95b7-d58f-362e-982f-69a203f41e5d | -5.78536 | -51.74409 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7891622d-2127-38a9-a1d2-29dbb2fd11fe | -4.67689 | -45.7895 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8efbf55-865e-3a75-b7aa-459146a30566 | -7.87689 | -47.32967 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a4e5ee4-8fdc-31b1-addc-252cee5ef79e | -5.48984 | -52.132 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03c480ee-522a-3e85-8da5-7b384878fcc1 | -11.35033 | -44.93794 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 053e510a-71ec-3128-a192-34086667e0f9 | -7.75265 | -42.56127 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 0648aa79-959b-3857-ace7-f3f048a7c1c8 | -7.37594 | -48.16233 | 2025-10-03 04:32:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 99ee8944-2920-383b-96c5-19548e952e7b | -8.79487 | -46.67845 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8775f9e0-e9f0-3814-9ae1-d4a12a06cb97 | -7.70824 | -46.20596 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1b477277-3c7e-3fa5-8900-2f0955f085ab | -8.61643 | -49.24677 | 2025-10-03 04:32:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78c095b2-0009-3f5a-9c37-0864595d6cd5 | -7.7738 | -42.59132 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a417ffac-31b8-30b5-bf95-c3a8de29f641 | -10.59699 | -48.71439 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f082849f-7722-34ea-a8e8-6bc07734b302 | -7.05481 | -43.30506 | 2025-10-03 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 82968109-4580-3ef0-a501-adfe04883336 | -9.91831 | -50.49866 | 2025-10-03 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 044681e1-2706-3158-9aae-3f14cea0d6d1 | -9.94797 | -43.75225 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ea63556a-058c-3234-9201-da1737c184ca | -11.29066 | -47.83915 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a75d99b-d3fc-35aa-8c16-3ebe2699eec9 | -10.90176 | -46.72535 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb32f82a-02bb-36a4-8167-34a01dbc36d2 | -11.10736 | -47.83607 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc88952d-c98e-3ae7-ba35-5f5accb98b0a | -11.00898 | -46.64006 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22c6c29f-a71e-3349-bc3e-ba4227be9dfd | -8.17261 | -44.15715 | 2025-10-03 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6653071-0e86-3546-b501-517fa08a1b51 | -10.28893 | -45.1829 | 2025-10-03 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d66c8aef-d5ec-3090-bbfd-87a6f90cbbce | -5.78309 | -45.74633 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8598fc6d-0fd6-3518-9a3d-b70697ac20af | -8.89749 | -46.6038 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afa5d872-b54c-37d6-b668-066cf640c11f | -7.76095 | -42.56251 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a6a47124-e6da-3150-80f0-3e7f71f95e1b | -11.62634 | -45.03366 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83e319ec-26cb-33ce-bb8b-f820a9114487 | -12.02451 | -47.8989 | 2025-10-03 04:32:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f64becb-fdc6-37d2-81b9-6fd570190e06 | -9.33696 | -45.74431 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4501149-63c4-3e21-9dd5-9f87147d255f | -10.28887 | -45.18111 | 2025-10-03 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 674ea046-a275-357e-b1d4-97c957980fbc | -8.55212 | -48.64959 | 2025-10-03 04:32:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1e801a5d-8486-3f1f-a863-d52e25f19f5d | -7.07443 | -45.81747 | 2025-10-03 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0275642f-5a35-3826-9dfc-936caca5b8ae | -8.75992 | -49.92029 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d797004-aaf2-3645-99b6-5aa303c74770 | -11.17458 | -47.7553 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1c5bfea-b29b-3498-96fa-cd020c8a930d | -6.23368 | -44.27577 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0f7c2487-701e-373c-bf6d-b82f86779127 | -4.66203 | -45.80936 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a53c04cb-06bf-3cad-95fb-111d24afb8ee | -9.62683 | -54.31139 | 2025-10-03 04:32:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9645312f-c947-35aa-80ea-27191e87c5e0 | -5.23786 | -45.17032 | 2025-10-03 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcde3b6f-ba83-3a6f-90c0-884e2891b27b | -5.90877 | -43.90818 | 2025-10-03 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cd4d58eb-eb65-3376-b5c9-e0f4368f22f5 | -11.18236 | -47.74926 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4bc22bbf-5a4c-3b5e-99f2-0945746d250e | -11.0699 | -48.36293 | 2025-10-03 04:32:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94f586d1-9b18-37b0-bd53-94964c1faded | -11.18681 | -47.74267 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3df16290-1c44-3706-bb6d-41520641cf15 | -10.93786 | -46.71483 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8256913-77f2-3240-a0f2-8db68ab1a7fc | -5.50505 | -51.01562 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README109.md)
