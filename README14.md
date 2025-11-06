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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 969b4eaa-ff92-3657-8296-f4d921e8b6b7 | -4.89687 | -45.89858 | 2025-11-06 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8ee3b1b-2ec6-326f-88eb-d09fdfc16fd2 | -4.71843 | -46.43312 | 2025-11-06 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66a6a439-3fbf-368b-87c0-ddd95c95bd11 | -6.36136 | -43.75936 | 2025-11-06 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21e08f72-c012-3d90-ad04-968d8c672c3e | -4.7027 | -46.52784 | 2025-11-06 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c2e19b6-0e93-38d9-9e7e-2bd8d04aa898 | -4.10379 | -48.01851 | 2025-11-06 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6897a7d4-6081-332d-9b0a-443a0375507e | -4.71546 | -46.43741 | 2025-11-06 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f19ae294-f2cf-373a-b378-4c497fbaaef1 | -6.05414 | -44.16371 | 2025-11-06 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 551d4468-3efd-311f-810d-13c15db134a1 | -6.04987 | -44.16294 | 2025-11-06 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47a23a12-528a-38f6-ba00-dead7949a08f | -5.92663 | -43.52155 | 2025-11-06 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e7aac69-7c32-3f32-a3a5-b71a4ae97939 | -4.7032 | -46.52489 | 2025-11-06 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d9a5537-22d4-3443-8c5f-6dcaec1c1df9 | -5.94211 | -41.32966 | 2025-11-06 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 64a4f3c0-b188-37c1-8826-edbc4aa7bf60 | -5.39796 | -43.9352 | 2025-11-06 03:53:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e86b000-1dec-352d-9c9c-7386e80dc6d0 | -4.98434 | -48.47839 | 2025-11-06 03:53:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1f0e810d-6a04-379c-8281-49fdd3412eb9 | -4.10799 | -48.02815 | 2025-11-06 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 179c2048-4756-3007-863f-20594d0efc3f | -5.3659 | -44.4766 | 2025-11-06 03:53:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97c9fcc6-058f-32d2-8a81-fb56da87e152 | -4.64179 | -45.67263 | 2025-11-06 03:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f87582b0-a7ac-3093-b9ce-a83530621540 | -6.26613 | -43.68194 | 2025-11-06 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 6524cbda-8d8d-3d2c-a23d-b71e632727e2 | -4.716 | -46.43432 | 2025-11-06 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52f39cd6-823b-3d8a-bd18-d7d64a8b62c1 | -5.61934 | -41.08501 | 2025-11-06 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c4a54d4-8adf-365e-8c23-9b2577874da8 | -5.77339 | -40.80911 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 849a10be-dabe-3fc0-ace1-84a43314ce0d | -5.10283 | -44.70398 | 2025-11-06 03:53:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93afccdb-b762-3b34-a56d-ddee0943f4fd | -6.26675 | -43.6783 | 2025-11-06 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5ea17feb-1841-3980-a312-7270252cdb38 | -6.07133 | -43.25292 | 2025-11-06 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 67b25fc7-e809-383f-bc01-c3b5943d4f2e | -4.37427 | -48.69284 | 2025-11-06 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63b27375-ca4e-3ced-836f-8e903edd8f04 | -8.88965 | -37.10807 | 2025-11-06 03:53:00 | NOAA-20 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5ce91f50-85cd-3b25-b0f2-032dd466da7d | -5.20323 | -46.17365 | 2025-11-06 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 634afbd9-802f-3b25-9cce-f5f60cda460e | -5.76218 | -40.81142 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 860b1ffe-9101-3df2-be65-a97686754517 | -5.74536 | -43.03326 | 2025-11-06 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| eb778961-18de-3a06-8985-ebfe1a74be82 | -7.83515 | -40.84235 | 2025-11-06 03:53:00 | NOAA-20 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2667e1f2-6f66-33e4-a7e0-392553868190 | -5.49376 | -44.41169 | 2025-11-06 03:53:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bc415fc-7e3b-3cc1-9ed0-1b2107d29850 | -7.16599 | -39.52136 | 2025-11-06 03:53:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c08569d5-c0d7-31f3-87a1-9d6bafa582a4 | -4.4908 | -45.9217 | 2025-11-06 03:53:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0941f15e-0e44-3c86-a89a-9e21c60080c6 | -4.48974 | -45.92785 | 2025-11-06 03:53:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dad97afd-e31f-3799-a42c-956966a16155 | -4.53998 | -46.44711 | 2025-11-06 03:53:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d50446ca-cb6e-3fcf-8ae1-b968602e1f8e | -5.76729 | -40.82427 | 2025-11-06 03:53:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 951d7157-dc02-3f1c-bd7d-8381b4c02b66 | -6.23286 | -44.31266 | 2025-11-06 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1848541c-cc4f-3516-9f8f-470b7116d305 | -6.22336 | -40.44416 | 2025-11-06 03:53:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c643909f-23fa-36d1-a8df-bb9872498fcf | -4.87801 | -47.54913 | 2025-11-06 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a20bd151-d61c-32c8-b3cf-885b6741eb54 | -5.09189 | -45.42993 | 2025-11-06 03:53:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e97413c9-55b3-3088-a74e-b6a6adc2ee5f | -3.4667 | -43.65726 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1da17831-b4da-39a5-82d3-94bccff0e24a | -9.42161 | -43.6165 | 2025-11-06 03:55:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c06c3078-f33e-3dfc-894d-9b917ecbe3bb | -4.577 | -43.33603 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d5974106-7d83-3d06-890c-732e161252d1 | -9.77939 | -44.19908 | 2025-11-06 03:55:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f16aba0-e5d0-3dcf-bf8d-f4bf33157859 | -5.14992 | -41.22625 | 2025-11-06 03:55:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 049705f2-0661-32c3-a266-5d9eb789b4af | -11.8216 | -43.1577 | 2025-11-06 03:55:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 47185b8c-caaf-30eb-8b98-03db7ea78fdf | -4.67977 | -42.09187 | 2025-11-06 03:55:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 46f6f419-f081-3c1c-a953-26231b5062f1 | -4.85815 | -40.64184 | 2025-11-06 03:55:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ba8dd59b-48b3-3f75-909e-0c588ac0e8ad | -5.58198 | -35.40794 | 2025-11-06 03:55:00 | NOAA-20 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f40e77be-9405-326a-b72f-cc0633edfe3c | -4.57876 | -43.33908 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab545b2b-92a2-3706-9953-498f39ccd23f | -3.43567 | -50.24475 | 2025-11-06 03:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8a8ee09-69cb-3cf0-ad32-1f158f97ee7e | -3.47235 | -43.64985 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 60861be7-1627-30e8-aad5-6880cb4372c2 | -10.06896 | -42.7414 | 2025-11-06 03:55:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 55c16330-d37e-3ed2-bb35-35480190b9fd | -3.46804 | -43.64919 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 565736f4-aed6-3783-b46b-301efbd2a1c4 | -3.89938 | -42.55363 | 2025-11-06 03:55:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 1ddfdfd8-26e3-3665-bfcd-706b383490b1 | -3.47032 | -43.66208 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be7f5b26-4a74-3941-a58a-1f520e37ad1b | -3.92367 | -47.70197 | 2025-11-06 03:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3fbe5d6f-2f8b-3455-9341-458d215bb0fb | -12.09262 | -40.04259 | 2025-11-06 03:55:00 | NOAA-20 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 240a8c44-b43c-3769-b45c-6830d452500a | -3.46963 | -43.6662 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c7a6e23-73a1-3a0d-b75a-667b38c6124d | -2.43788 | -45.90274 | 2025-11-06 03:55:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 13392c20-0ada-3b80-9cd8-c73796ab7918 | -3.47302 | -43.64585 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5a0b7130-c0a4-3953-905a-c361b7fc7b00 | -3.13676 | -40.05525 | 2025-11-06 03:55:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 684af1c4-bbdf-3849-88fe-18fac7cb69aa | -2.96678 | -44.59326 | 2025-11-06 03:55:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71c78505-c4e0-3d7d-a129-5c9b78f5d10b | -4.58767 | -43.33666 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3ea6f4b-3ab2-386f-8029-5220e95fb2c2 | -3.58499 | -46.0536 | 2025-11-06 03:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 365c7d9e-97ee-3100-93ac-53e02ad16069 | -4.04087 | -46.0862 | 2025-11-06 03:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcf5f800-13a9-38f2-863b-adade2700a6e | -4.58704 | -43.34039 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e87878a-e5df-3bf4-9b15-531c97e6b217 | -2.973 | -44.59226 | 2025-11-06 03:55:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa75ae04-37d3-37ff-9dff-3560d00b63fd | -10.01827 | -36.06914 | 2025-11-06 03:55:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 11be2a62-ecc7-37b9-9699-3632a238f4c9 | -4.5775 | -43.34649 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d110e83-5cf5-333c-81d5-7032cb1a79ed | -4.75945 | -42.65274 | 2025-11-06 03:55:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 43.8 |
| eff50252-8e44-3171-ad1d-9012416a2d9c | -3.98596 | -47.29982 | 2025-11-06 03:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 478cb430-d0bc-3412-9411-8bb22aa2edf9 | -3.91823 | -43.15287 | 2025-11-06 03:55:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27fb849b-4696-3d74-9a19-c9c9ce9ef7a7 | -3.43923 | -43.16918 | 2025-11-06 03:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6586339a-a833-33fe-97ba-070afbc202f6 | -3.58866 | -46.05338 | 2025-11-06 03:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b14e455-05bc-3341-8898-46352c30a498 | -4.58235 | -43.32923 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5897f835-a63d-3e23-ace8-5589fb75161d | -3.62341 | -40.38917 | 2025-11-06 03:55:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 03462a47-be7a-3668-8b0d-c1fe1203c16e | -9.7754 | -44.19817 | 2025-11-06 03:55:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45fcfd8b-65e8-3de2-bb4d-4febf64cd236 | -4.04037 | -46.08915 | 2025-11-06 03:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6a2fe67-07b0-3c1f-98b0-89e27cd54a9e | -5.14948 | -41.27388 | 2025-11-06 03:55:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ed685b85-bb8d-3895-b113-bf2daa001023 | -5.15241 | -41.27863 | 2025-11-06 03:55:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c750f8f0-e00d-3904-b4b5-ef850d2adcd7 | -3.96522 | -41.81664 | 2025-11-06 03:55:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 15fddd47-80c1-31e1-b108-a44f09817ab3 | -3.42964 | -42.54658 | 2025-11-06 03:55:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 42137ad8-f595-3362-849b-c656616fc3e3 | -3.27121 | -40.02848 | 2025-11-06 03:55:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5ec5f24e-823c-3e05-8680-dd188726d86b | -9.77876 | -44.20267 | 2025-11-06 03:55:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad220457-094e-3f78-bd5c-fa7dd52a06cc | -4.58054 | -43.34043 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 534793d2-ad9b-3b98-a058-07033bb0c2ff | -3.40191 | -50.28088 | 2025-11-06 03:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e13866f-436f-3dbb-9ceb-777bd4c1fd75 | -3.48391 | -43.66006 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f911864-2fd4-3f8d-9e72-510d1807d26c | -4.10166 | -48.02368 | 2025-11-06 03:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 11db1eba-0f9a-3df3-a21d-45f0659a8835 | -3.58815 | -46.05636 | 2025-11-06 03:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 321927c8-99de-3112-8f58-09a1767a2877 | -2.43838 | -45.89976 | 2025-11-06 03:55:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9fc4abb5-c9cf-3306-b62e-0e14bd104f58 | -4.96678 | -38.65057 | 2025-11-06 03:55:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 471ab9a5-6ee1-37d1-8b0d-d835f7044485 | -2.97141 | -44.59403 | 2025-11-06 03:55:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dd05bcc-45f1-3913-b9a0-0e1f7f940ed1 | -3.98052 | -47.29866 | 2025-11-06 03:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5ded190-0fca-35e5-9fae-02d78d3bfe55 | -4.48222 | -45.93653 | 2025-11-06 03:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8881fd6f-d1a8-3096-9f5c-b7b419c17dd3 | -3.47666 | -43.65052 | 2025-11-06 03:55:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d66d5330-3c7b-30d5-92e0-34f487235901 | -5.1531 | -41.27444 | 2025-11-06 03:55:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 707dc3f7-8e8f-3ab3-964b-20a2e382e794 | -4.5883 | -43.33295 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca9bfda4-b232-380a-bf54-2f4e016103a0 | -4.57933 | -43.34788 | 2025-11-06 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 069138db-1e20-3a6a-8823-050d522b5dcc | -3.8306 | -44.4046 | 2025-11-06 03:55:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 568d85e1-2c22-3bb7-af8f-8c9de6aeb884 | -2.99961 | -40.23531 | 2025-11-06 03:55:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |


[Clique aqui para ver as próximas entradas](README15.md)
