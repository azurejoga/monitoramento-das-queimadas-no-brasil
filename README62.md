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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06bd4f5f-2ca2-30d9-83a7-6b079df04722 | -13.00158 | -56.90683 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 698f3d03-2372-3edd-96ea-1cd3f585b515 | -10.46712 | -57.95838 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 570050f9-4300-3aca-8498-074c1be7a6e3 | -12.69109 | -48.17305 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e02422e3-9f18-310e-87c8-80d8fa80f0c9 | -12.12167 | -55.19364 | 2025-08-28 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c990523-0834-34dd-ae76-6a829cb2ccf3 | -10.52492 | -46.69199 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2943e1d-ec2f-3b2b-b28a-4591f10bad9e | -14.36493 | -53.21299 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2982a7de-1718-31ab-a887-d3701aaa3991 | -8.95673 | -65.95402 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b0eba03b-1acf-3352-8c95-cebe3d5d51a0 | -9.53833 | -62.408 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80e3084c-5a7e-3b8c-99d7-62e162ed82c3 | -12.68567 | -48.17756 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5d589fcc-b2ce-3264-a5c8-1bda72a3b9db | -10.53671 | -46.68124 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77cbde54-8f4e-369d-bda0-fd6dc16f5e54 | -13.54148 | -46.88935 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 114a1b75-3c8d-320f-a025-b2e4a33a6982 | -10.03055 | -59.35847 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a28d11b-594c-357e-ad39-f14afd5f5461 | -9.41777 | -60.52352 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 506fed05-61cf-3269-8ba0-7ed1b196287d | -11.22852 | -55.05439 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0eaf7337-756f-3aa0-a79b-4010ab7328ba | -12.79965 | -48.16164 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61bf298e-6b96-382f-af7d-74422ec2ccfb | -12.99491 | -56.90574 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3332d8af-5ce6-358b-8259-3d520564ce2b | -13.44659 | -46.96616 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b12cb066-92c5-3517-8086-f9c53998d012 | -9.53922 | -62.40301 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 128cbc05-0d4b-35d2-9714-a056e65538e0 | -12.68228 | -48.16572 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39c3fb93-cf18-3b7f-8665-9c946339345e | -11.93462 | -46.70542 | 2025-08-28 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0c363a2-b275-3388-952a-fbc9d1b58c8e | -14.30085 | -53.02816 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4131a3f3-4b47-3e09-a04f-ae353bad0e65 | -10.42317 | -64.505 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d193a55-8add-3b0c-8e64-d7d5cb8a9f32 | -13.54634 | -46.89341 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 006091b3-68b4-39c2-8f23-8a42bf523f0d | -12.7949 | -48.16067 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1818021b-7696-356c-9f92-93e5154b8aaa | -9.14032 | -65.7804 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96d36506-c838-3919-8a79-beaa457631b0 | -9.01965 | -65.68867 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a48eceec-b89f-31bd-b8ca-906c5e9d1513 | -15.62024 | -52.71506 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2770b007-7bd1-3941-affe-16625cd76530 | -9.10093 | -60.3234 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89cf1bf0-fc4e-3743-b046-b68ed9b5b0a2 | -9.21218 | -60.85443 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b4eb61c-befd-3245-8466-96b1b38a5482 | -13.51559 | -46.92699 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 070b3581-b5b6-3318-b3bf-555652e8786a | -13.55457 | -46.91371 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f3a120af-af06-3fab-a3f7-164bce66fdd3 | -13.4715 | -46.85019 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7aa2ace-247f-3cd0-8638-cb98071ff6ef | -14.3457 | -53.35023 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e970e6c-d2c3-3351-accc-d5a82a9a3b4b | -15.18474 | -52.33679 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cc71fdf-1649-3a21-ae71-98e4cf9864d1 | -8.9456 | -65.96315 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b3046b93-8298-367e-bf6a-d26b2270e234 | -13.43123 | -46.96128 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2181d90a-ea54-3061-abe4-f3a50f9c0a6d | -13.5023 | -46.85861 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce5f9afa-75e6-3696-a9bc-63949971692a | -12.86013 | -48.10759 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 252a32cf-7f45-31b2-a113-c2111b04df90 | -13.13777 | -54.92554 | 2025-08-28 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| de6a3419-44cf-35f9-bab3-7f417451f8f2 | -8.90008 | -60.59594 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ea0c076-3534-3947-9c4f-5ca47a07bc62 | -13.48182 | -46.85046 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 677af82e-89f0-3a22-923d-0fbed1f46c69 | -12.80637 | -48.14678 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1cf14996-4758-3dfa-b04a-3ed3b93d1453 | -11.79551 | -46.79629 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba649823-004a-3762-9d8b-2066fbc6f10b | -13.43481 | -46.97547 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f6c933ef-fb79-3ab9-a762-68482bcae14d | -9.2292 | -59.6779 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb4af0f8-5172-31f3-bc20-b83b10c017a1 | -9.64565 | -59.62599 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e949fcb-6fc4-376e-ae0b-7852fabb2faf | -13.63062 | -48.21702 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 209dc995-ac6f-368b-8aab-7673f0c7410a | -9.41626 | -60.50778 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1efb224a-5e0a-32ce-b2bd-48071170ec01 | -9.12618 | -65.79092 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 01dbad2a-fbe4-32dd-81a8-3759e07d3a64 | -12.96102 | -44.58009 | 2025-08-28 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| bfaebfd0-3d94-32e2-97d2-1dafea43d510 | -13.39177 | -51.75351 | 2025-08-28 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1e7c857-2fa7-3451-9a94-75e98d3b06a5 | -9.19075 | -60.80182 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e464bd9-55d7-3590-b1db-f71c4f5a421a | -13.67248 | -46.90752 | 2025-08-28 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3a655c71-2a37-3b59-b25e-0d498cef2fbf | -9.15082 | -59.56998 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d940cc0d-5787-3581-9739-4d83cfc6912f | -9.40802 | -60.50639 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27f279e6-5146-3813-b2d4-37a36c98b380 | -8.96352 | -65.95074 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 356f50d4-4b44-304f-b8b9-c7a45be693d1 | -12.95441 | -44.58404 | 2025-08-28 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| da019cf4-bfb2-306e-8397-6ddc31dd10b3 | -15.1891 | -52.33309 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42a24f10-6875-371d-b89c-747790a07752 | -8.87974 | -60.76564 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d3036db-092b-3c82-a7b2-ff511d2f0bb1 | -10.84583 | -54.02921 | 2025-08-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3d6c67f-cbc5-3ff6-ad53-26bef817d774 | -9.19948 | -59.54257 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52acb870-c0db-35cd-910e-d5263604da57 | -8.57603 | -62.60268 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 950b5bf2-57ea-369e-bd37-4274b3bc58f1 | -9.48881 | -62.38901 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 380bd109-5a07-39e6-91c4-7cbd15ce3d6f | -9.57019 | -58.07333 | 2025-08-28 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 544edaeb-cb47-3e47-abcc-f4d0649039fb | -14.27055 | -53.07296 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 04b29446-acdf-3f78-a32c-95b0f93f4ff2 | -15.07409 | -48.64293 | 2025-08-28 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ea306f0-0c93-3b28-b834-caa8bea11033 | -14.33922 | -53.34502 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 33d3dafa-cd97-39f8-91f7-4c8e40f0eaad | -12.96209 | -44.57076 | 2025-08-28 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| e6b1a36a-9f70-3546-b397-94548f808ca6 | -14.29008 | -53.05246 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe8edab7-c125-376f-a15f-24211e56918b | -14.26994 | -53.07716 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bfae7200-9dd1-319c-bc54-125958035571 | -11.34037 | -43.55227 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bb43518e-d3cf-3d8a-aa5d-a658836fc3e8 | -9.15607 | -59.58624 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6283be26-2b7b-3f31-9960-0eaef8746300 | -15.67403 | -52.73701 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5c23037-55cc-3600-a265-da45ee7ebeb4 | -8.88532 | -60.75842 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb151498-96ff-3394-8408-f7e8d5db4164 | -9.08822 | -65.7356 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| fc2876ee-b24a-3bec-b45b-1cd2a23a8bbb | -15.62027 | -52.74276 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b72018da-c0ab-361d-b74a-be4502bfddb4 | -9.47837 | -62.37833 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3646a5c8-7d3f-3212-bcaa-a55f3262ffd7 | -14.32103 | -60.36524 | 2025-08-28 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb3d5899-7599-3bbd-bbeb-bb1748978d8d | -10.47193 | -57.95103 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8ba77b31-b706-3e4c-b6aa-dffb246b3ce2 | -11.05476 | -54.26472 | 2025-08-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 541f18b9-10d2-3b9e-98bb-1022a936d5d5 | -12.68093 | -48.17662 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a64ea449-4b51-3993-80d3-92b1c189a836 | -9.73716 | -64.90426 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73247ec4-d756-34f8-98b9-cb0f917bea53 | -11.5795 | -44.64953 | 2025-08-28 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b16c5a6-9b6a-3aed-bbdb-9ca3a426c850 | -13.49774 | -46.85181 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b76400b2-b2c0-34d8-8a5c-bc3b6a53a25b | -13.67233 | -46.91095 | 2025-08-28 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5c74804-2b64-3306-8d03-22b2ad1a59ad | -15.62451 | -52.7506 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 274a6fdd-9d96-377a-b609-342a5d30ee8a | -11.32314 | -43.53379 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77d2f0cd-c27a-3210-84b2-355e9800a16b | -9.13827 | -65.2803 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f0eb34e4-ad70-31a1-b18e-5fa49c4a7245 | -13.67292 | -46.90614 | 2025-08-28 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1554f129-ffe2-315b-a38d-612ff2e80d41 | -13.41252 | -46.85041 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4401d0a-72a3-3b51-a130-8313191b2bf6 | -8.93189 | -65.93763 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7da74b4-cd86-374e-a8d3-46d388cb5624 | -14.26933 | -53.08133 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb951799-7a58-31ff-91f9-ad1dfdba2c6d | -9.40755 | -60.53339 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44504c81-016f-3b86-899e-9646ba5b9741 | -11.23351 | -55.06597 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 033c8545-8f7c-374c-9624-cd94cbdd1d1d | -9.24251 | -59.78944 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a30b1e8-9811-3340-b476-d0eff917ac38 | -12.92427 | -46.33134 | 2025-08-28 04:59:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 515fda04-00e1-32cd-a22d-28e2b673029c | -10.47063 | -57.95899 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c76c67e0-96b4-3fd4-9d18-5477996bb55b | -8.88403 | -62.47963 | 2025-08-28 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5100c9b6-8e2d-3a42-bcbb-f13f8381b261 | -11.3748 | -54.34359 | 2025-08-28 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ea47e1b-53aa-3721-b9ac-ed2798320d06 | -13.63549 | -48.21725 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README63.md)
