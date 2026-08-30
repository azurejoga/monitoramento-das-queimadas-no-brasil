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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23fbd171-79ed-3744-beae-7fc9fd237ea6 | -20.10921 | -48.26966 | 2026-08-30 03:40:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e7870d8b-462c-3b3a-992c-fa559a532407 | -22.51678 | -46.03217 | 2026-08-30 03:40:00 | NOAA-21 | ESTIVA | MINAS GERAIS | Brasil | 3124500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9b7d48fe-27b2-3fd5-b368-faeeb15af5c8 | -18.82368 | -47.45772 | 2026-08-30 03:40:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58089c46-3885-3abe-a203-fec7ef3873e1 | -14.90214 | -47.74384 | 2026-08-30 03:40:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5af17c90-a1ce-3d03-9dd7-4fca04f56193 | -16.14212 | -43.04871 | 2026-08-30 03:40:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0140d3b1-dfcb-3a7d-b0c4-d46f4d07f345 | -20.50997 | -49.05171 | 2026-08-30 03:40:00 | NOAA-21 | ALTAIR | SÃO PAULO | Brasil | 3500907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d6018b3e-6ad1-3c67-b7d5-a3bd6e72b5ba | -16.89323 | -39.31307 | 2026-08-30 03:40:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| a1a83d5d-34e2-3897-bb63-386b38ca7abd | -16.33784 | -43.44094 | 2026-08-30 03:40:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1e86d395-cb0d-355a-ac2f-c42c18bcef01 | -16.89681 | -39.31372 | 2026-08-30 03:40:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 0e14d05f-61f9-34bf-b1dc-7cbd05e7bf74 | -20.11019 | -48.26524 | 2026-08-30 03:40:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 17aa9f37-80b0-37e2-9752-fbde996ce3e4 | -19.74113 | -48.96978 | 2026-08-30 03:40:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6e3223e-bd34-3580-a65b-6d7de9a2cbd4 | -20.59462 | -47.65683 | 2026-08-30 03:40:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 270bd7d2-bb25-363e-a722-7641e98ca4d0 | -16.33612 | -43.44265 | 2026-08-30 03:40:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f28254f7-9305-33ef-a7b6-c38fd3b19659 | -16.22563 | -39.14249 | 2026-08-30 03:40:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e3bd387b-00a6-3da5-aac1-9bfa8ae93bf6 | -18.52675 | -42.14896 | 2026-08-30 03:40:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f2ce2052-28af-324f-acd0-869c0389d9c9 | -17.27506 | -46.01156 | 2026-08-30 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eaa6f674-aae7-3b18-8e99-b2f3dfd01f09 | -18.4632 | -44.90604 | 2026-08-30 03:40:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7aab054d-6be7-3e7f-8807-a7cae2878b58 | -16.28079 | -42.57847 | 2026-08-30 03:40:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0e43356-9d96-37d7-bfda-a8b520916530 | -14.75872 | -48.74223 | 2026-08-30 03:40:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7b69e5ce-5d61-3c58-a2ce-1a9879ae78ea | -20.10875 | -48.26784 | 2026-08-30 03:40:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 2a6df0bc-2a1c-3e19-b0fb-63e5b553a7c5 | -19.74 | -48.97476 | 2026-08-30 03:40:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e0f2bce-cbba-3249-8188-b33e5f9237e8 | -18.82279 | -47.46181 | 2026-08-30 03:40:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcdbfa50-1a4d-3326-8415-449d4d15b713 | -19.09696 | -46.23666 | 2026-08-30 03:40:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f2c3560-38d2-3ed1-bb51-b9dacee12946 | -17.28101 | -46.00979 | 2026-08-30 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f6f96ee-f5dc-3cda-9522-069b1034f2a4 | -20.59547 | -47.65289 | 2026-08-30 03:40:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e8c885e-a8f6-3506-9d19-6ca376a670d8 | -17.4201 | -42.63269 | 2026-08-30 03:40:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 59.5 |
| f8402a00-e1af-3c56-b103-fed2fd357ba9 | -21.60777 | -46.06845 | 2026-08-30 03:40:00 | NOAA-21 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 138807d8-7405-3954-aecb-8e6f5590f725 | -16.28131 | -42.5768 | 2026-08-30 03:40:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ab8b014-96fa-3274-9aaa-c92a36495021 | -17.79206 | -39.70412 | 2026-08-30 03:40:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9e664066-c006-3ee4-a771-c370d73c1e56 | -17.90677 | -39.92933 | 2026-08-30 03:40:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 17646cd3-3a97-3826-b5b6-4847e4b1d727 | -20.11398 | -48.27568 | 2026-08-30 03:40:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| a07d92aa-400c-3bd3-b564-97fe424254f7 | -14.76654 | -48.73796 | 2026-08-30 03:40:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c2da1b40-93ec-3907-9092-0bd59ee50591 | -17.29539 | -44.87525 | 2026-08-30 03:40:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b1b5787-2c5b-3e0a-81dc-f3fb7efede37 | -20.40588 | -43.66535 | 2026-08-30 03:40:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 366359f0-5ac2-3be4-8b46-513f3962d612 | -18.52532 | -42.15673 | 2026-08-30 03:40:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e339bf2a-e040-33a0-9732-c4a4bf8a5df7 | -17.28633 | -46.01109 | 2026-08-30 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbcbce21-1c02-34be-9be8-3990b5195e2c | -16.86871 | -43.58107 | 2026-08-30 03:40:00 | NOAA-21 | JURAMENTO | MINAS GERAIS | Brasil | 3136801 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d3d0908-0708-302a-b60e-6c1e5d4866cd | -16.89607 | -39.31799 | 2026-08-30 03:40:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 9f26166e-f7c4-3fac-bfdc-d2724bb9129f | -20.11598 | -48.26667 | 2026-08-30 03:40:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 57bb353a-3fef-3a3e-a02c-1d30e918e000 | -24.28875 | -49.60269 | 2026-08-30 03:42:00 | NOAA-21 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef5bde7c-4d1e-3ca6-ba8f-689cd59c0e2e | -24.28979 | -49.59824 | 2026-08-30 03:42:00 | NOAA-21 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 189bf61d-af15-3c15-8cc6-7cd70475213d | -23.24156 | -46.46871 | 2026-08-30 03:42:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cdaa99d8-a178-3d3a-b98b-b86990fdf1b0 | -23.15527 | -48.67076 | 2026-08-30 03:42:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7d92239-e93f-32f8-a02f-6f8885521d93 | -23.38797 | -46.29315 | 2026-08-30 03:42:00 | NOAA-21 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e32f2ca1-8393-34f9-8517-34ab0b333313 | -24.28871 | -49.60091 | 2026-08-30 03:42:00 | NOAA-21 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c082038-7c9a-378a-b518-af1044856ed9 | -23.39344 | -46.78383 | 2026-08-30 03:42:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a1c21bf0-1ffe-3d28-9bb6-3d123da0fd11 | -23.39282 | -46.78673 | 2026-08-30 03:42:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| db024379-fd5e-37f0-9b9f-8a451a789623 | -23.24232 | -46.47207 | 2026-08-30 03:42:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 71543862-e993-36f4-9f3a-c803b3e82c45 | -23.15615 | -48.66689 | 2026-08-30 03:42:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5591282e-be78-327b-82e9-6ce045c41a4e | -22.60408 | -46.25723 | 2026-08-30 03:42:00 | NOAA-21 | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 299d6446-39fc-3012-a983-c02f13aba6f9 | -9.0615 | -65.4169 | 2026-08-30 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| be34b200-0f92-37fd-928c-fd8e61cc00c2 | -5.4876 | -57.1416 | 2026-08-30 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 3b84c4ce-37d4-3366-9aba-4da2c7a63c9b | -9.8927 | -60.2752 | 2026-08-30 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 3f20d7cd-07d7-3a3b-ae55-0b8ea42921d6 | -4.9604 | -55.8424 | 2026-08-30 03:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| b111a042-6d18-32d9-8891-51359b95acd7 | -5.4876 | -57.1416 | 2026-08-30 04:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 679cd589-70e8-3395-8803-f8bcd525d59c | -9.8927 | -60.2752 | 2026-08-30 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 5a459566-79c4-3faa-b353-fadcc147e036 | -4.9604 | -55.8424 | 2026-08-30 04:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 5df10b98-9145-3153-a71e-4cc746397258 | -9.6586 | -55.1036 | 2026-08-30 04:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| be7d2640-b2d7-3cf9-b90a-edc8077c0a6a | -5.4876 | -57.1416 | 2026-08-30 04:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| cfc40db2-d017-309c-867f-adc282ac2051 | -4.9604 | -55.8424 | 2026-08-30 04:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 30b993b6-af79-3961-bb31-f5d27780e8c4 | 2.22726 | -50.76257 | 2026-08-30 04:10:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f4e6651-6d26-3482-b53c-4e5c025b3167 | 2.52257 | -50.85575 | 2026-08-30 04:10:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f91aa46-9eb8-3a9e-8310-90ecd4fb14b7 | 2.51432 | -50.85314 | 2026-08-30 04:10:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53f7900d-c0df-3a84-877a-08068dc9656f | 2.23981 | -50.75438 | 2026-08-30 04:10:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69c8b6cd-91ce-3e20-b6e0-27ac11087b18 | 2.52111 | -50.85207 | 2026-08-30 04:10:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 108cd6ab-4e10-3545-8978-431ccd5673c4 | 2.23399 | -50.76151 | 2026-08-30 04:10:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 967f7568-99d0-3002-a5de-0228b4552d12 | 2.51578 | -50.85683 | 2026-08-30 04:10:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4225c276-e46e-3a66-b8c9-92198b51c38d | -4.36585 | -47.77647 | 2026-08-30 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 08231a3c-65ac-3762-8d17-de9276eda907 | -4.07875 | -45.943 | 2026-08-30 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8759a5d8-30b8-38d2-a78d-36784bac8bda | -4.36549 | -47.77122 | 2026-08-30 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6b9dfb20-fcfa-3b58-be78-f2a9df523ae9 | -5.76955 | -35.74499 | 2026-08-30 04:12:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO NORTE | Brasil | 2409332 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| da277b2f-5856-3934-b3d9-66dfdc2de91b | -6.86223 | -41.67374 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8b01effa-c40a-352b-8ac0-31d6ca7cfb1b | -5.58078 | -45.10328 | 2026-08-30 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb451b13-1937-37f9-9c98-4e465f9799b0 | -5.89164 | -47.72301 | 2026-08-30 04:12:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ee0ebeb-4fcd-3d75-b284-f6f8ec88afc8 | -6.86445 | -41.68158 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 54a949bb-daa1-3f89-bb43-2d302368aa98 | -4.36681 | -47.77069 | 2026-08-30 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| a24cde3a-7dbe-3fbd-8413-7b97845eb8fa | -6.88269 | -42.88381 | 2026-08-30 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9e4042de-26e2-3a0f-b315-67c6c8835d0a | -6.87848 | -42.88726 | 2026-08-30 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a26c3744-c52d-30f8-b036-5e3831f3a312 | -6.87418 | -41.66435 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 70c03e80-c0c4-340d-a94e-881f868fd04b | -3.43371 | -43.20376 | 2026-08-30 04:12:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f466006-0d47-340f-8097-7e47e0422dfa | -6.864 | -41.66274 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 739a06a7-5a67-3191-8e9c-97fd4a01d7e2 | -6.06415 | -44.87813 | 2026-08-30 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7a98c9e-199e-372f-a0f9-d401111bf1b6 | -6.86164 | -41.67739 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| c527e64b-c47f-3e65-a620-0f0b3821d0c5 | -2.0293 | -48.78352 | 2026-08-30 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bd9eceb-9fc2-32f4-b59b-31fc4a2edeb7 | -6.43567 | -41.546 | 2026-08-30 04:12:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 728d0277-35bb-300d-977d-873d675ac481 | -6.92044 | -42.67425 | 2026-08-30 04:12:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| af4c5b51-8a6f-301e-a127-932146bdbc26 | -6.86282 | -41.67009 | 2026-08-30 04:12:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cd3d3c9b-a9c4-3226-ad7c-478bdd649b4d | -1.58835 | -47.74072 | 2026-08-30 04:12:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f4195e8d-c4e8-3b5a-92f8-89773bc6fb96 | -2.00162 | -44.80172 | 2026-08-30 04:12:00 | NPP-375D | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ba63f5b7-7fba-3a4b-8b79-8bbaeeb5930b | -6.87493 | -42.88663 | 2026-08-30 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0b1833fa-c091-3296-b3b0-5ec34d2ab788 | -5.88483 | -47.73309 | 2026-08-30 04:12:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac7f761d-ae16-331f-8f17-cb01d72ccf6b | -2.79985 | -49.58109 | 2026-08-30 04:12:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8305fff-e61a-3bcf-b6d0-f392947c774a | -4.36449 | -47.77696 | 2026-08-30 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bebdefa1-a3e8-3dd7-802a-570acbd3af0f | -4.0832 | -45.94378 | 2026-08-30 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 090a303a-afcb-3f9e-903d-a9c3d941081f | -3.2216 | -49.23008 | 2026-08-30 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0f43b2d4-3eeb-32cf-9142-38da9a8dd690 | -6.87204 | -42.88199 | 2026-08-30 04:12:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d75bd27d-db83-3561-a910-f04174dd8206 | -5.61368 | -44.12276 | 2026-08-30 04:12:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93361376-3398-32dd-a126-82ef8873c666 | -2.47752 | -46.85658 | 2026-08-30 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c8ec0f7-e506-3794-92d6-ee92bac03462 | -6.77434 | -38.21452 | 2026-08-30 04:12:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 251a5870-a4ff-3ea5-afb5-2c10974001c6 | -4.86857 | -37.44869 | 2026-08-30 04:12:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |


[Clique aqui para ver as próximas entradas](README26.md)
