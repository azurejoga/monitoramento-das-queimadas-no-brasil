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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78c5c05d-0d67-3b98-ae09-9ffdb4d15578 | -7.78081 | -42.60384 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1d32b3cc-01a0-3b69-aa2d-48b72f4ac29a | -13.71642 | -47.35288 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f2ed85c-de0c-3558-9876-8039341ec7cf | -13.14476 | -50.9357 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbd58528-22ac-3e27-b118-428330779ae2 | -12.31659 | -55.15911 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1ffe4b6-97b5-33d2-8023-c6915df6a9ad | -7.29229 | -39.27102 | 2025-10-05 04:46:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 00f098de-ba0d-3599-83b8-0f71f8df79e7 | -12.30701 | -55.12525 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 948458bb-9d8e-312e-93b0-6f9488406739 | -10.45923 | -47.80877 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| eef9608c-b6b2-3126-99c9-4f581ebbf92d | -9.20632 | -46.92565 | 2025-10-05 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d22f921a-ca2a-3570-9b48-12edd56cd4ed | -7.46255 | -47.1762 | 2025-10-05 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6046cc20-bea1-3701-81dc-f098f862701f | -11.78196 | -47.55495 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 836d7eb3-edb6-3a8b-8ec6-d313d9705fbe | -8.9394 | -48.66138 | 2025-10-05 04:46:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0fbd2cc-3c61-3eed-8603-df6dd00c42f3 | -10.36133 | -48.17169 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b309636-f5ad-3967-834f-983b97f0e717 | -13.09713 | -47.91951 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6a6b6411-d488-3f64-b1e3-a69955ea522f | -11.51321 | -54.4749 | 2025-10-05 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82dafa27-116c-3f2c-81a3-59c86fb1d218 | -9.10314 | -61.5299 | 2025-10-05 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2b1aa77-100b-3b00-8eed-513ca182987b | -11.63873 | -46.87445 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca140e76-3b13-31b0-ad41-d58137e6fc54 | -12.16908 | -51.43159 | 2025-10-05 04:46:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3733406-a1d5-31b8-8c4e-bfc8cc2bc303 | -8.57879 | -46.31516 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5f3ccf84-e201-3ab9-8bbe-0a29f567260b | -12.59551 | -48.15147 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01d6fa98-eedb-3ab7-88e2-fbbd594a608a | -6.74775 | -44.57892 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0716d9a-86ac-383a-a648-cdd1a934ff0c | -10.34657 | -48.15531 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 511b4278-f534-3d3e-ae32-46953d318f47 | -7.71619 | -46.26911 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 691a5e61-74d2-3982-ad67-597a9dcf71e5 | -8.88799 | -47.59449 | 2025-10-05 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dabc14f0-c41a-398d-a833-cff232193af2 | -9.14248 | -50.05955 | 2025-10-05 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9019b29d-c84f-3fdc-887c-1f3717bb8adc | -7.69819 | -42.58851 | 2025-10-05 04:46:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 67e2387e-8fab-3123-bf80-48a2df44099e | -10.78735 | -50.99907 | 2025-10-05 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c196221d-7794-3a30-b11a-5225ed6bcac3 | -11.31258 | -53.96198 | 2025-10-05 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f1b678f-4e8d-3781-a43f-9961feadeb7e | -7.52201 | -43.85362 | 2025-10-05 04:46:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e8819db5-08d9-3b90-b126-42b43e942eb7 | -13.0959 | -47.84166 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c4b432c6-677e-3e63-9883-ced1f4aeec76 | -11.09981 | -47.7345 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ec687056-a6e0-364b-8ca2-d7d09f955286 | -12.59412 | -48.16135 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3dd47709-29e6-3cbe-aea4-4ee250228fd7 | -7.6934 | -42.58471 | 2025-10-05 04:46:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 78c0b655-6c9d-354f-a516-6b487a412c22 | -13.68187 | -43.18382 | 2025-10-05 04:46:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bdfe173a-3a26-351e-bb7d-0cc4397c0aa6 | -8.56098 | -46.32357 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7094db76-1a5b-3ba4-a3ba-e4c3dad934f6 | -8.53951 | -46.32855 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e66b3dd0-702a-35c2-92d0-51e2b4e99b29 | -7.44281 | -46.5273 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 42f6d1f8-e715-3743-9c2c-ed7cc2f2888e | -10.83611 | -57.18771 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02c77e6f-6666-387b-9521-d1ad9ee640a9 | -12.09075 | -42.73963 | 2025-10-05 04:46:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 65270ce4-9a53-3436-8489-3239d61a829e | -13.32077 | -47.78069 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c33a49cc-133b-3dfa-aa6c-b2462a8e0417 | -9.32891 | -45.76717 | 2025-10-05 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0400b4cb-5e46-3539-b6e2-f85a7b4c7fd9 | -6.65937 | -46.12241 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de563e79-0200-3dab-b2b6-794d0356ccc8 | -13.38474 | -47.56796 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68de9514-e8ba-3f5d-b49a-106beaaa0dd3 | -11.86898 | -44.95963 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8ec3d7f-4523-3327-84fb-3c14490afaa3 | -11.6336 | -45.07487 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6670f6ac-6f76-36b2-93cf-a7dfc999c1bb | -7.81132 | -42.54339 | 2025-10-05 04:46:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d3c60b04-3164-3c11-a412-5ce2209b7258 | -8.56199 | -44.63629 | 2025-10-05 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0f6d4f0-4a8f-3b99-94cb-92ee353a6eef | -8.54208 | -50.16074 | 2025-10-05 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed357994-0a84-391e-acf0-162deaec36f5 | -13.11674 | -47.8033 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c535652-1823-345d-80b3-ff483f3ada55 | -12.31184 | -55.11784 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc70a541-bf6d-3d2b-933e-28dbdfae9e62 | -6.73915 | -48.17402 | 2025-10-05 04:46:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8df84c3-7101-3854-9e95-ac03df55b340 | -9.6335 | -54.31344 | 2025-10-05 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47f9d274-b52e-3b6a-817f-78b6c910e889 | -13.14299 | -50.90115 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bbedc3cf-1f09-345a-981a-1afd732d1e83 | -7.55877 | -42.63144 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9afc1cec-b619-3a47-aa35-37e666fde92d | -7.46684 | -43.05499 | 2025-10-05 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 406b59b6-799a-3702-85ec-ca727c035f7d | -9.61611 | -50.54323 | 2025-10-05 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a718fb1a-b01c-30d5-957d-352b01800774 | -12.8946 | -47.32146 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 52577f57-e874-3dcf-b854-4ac2f3bc0fff | -11.85957 | -45.05383 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c492ca3f-6cf1-3536-ace2-fb706e5e94dd | -12.92095 | -47.31031 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 21facdae-7c31-351a-9a39-434fedc33393 | -13.08859 | -47.95318 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04417981-81f4-3ebe-888b-7af676c4b29b | -12.98159 | -51.04625 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 70ae04a3-1e7d-35c1-8ef4-bcde6e02908c | -9.36179 | -46.24633 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32713bd9-948a-3221-b526-b1b8f8cc12d8 | -13.37336 | -48.06262 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6dbfe66-426e-3789-b0f2-30f4c00d6343 | -8.13963 | -44.09369 | 2025-10-05 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 323cd419-c029-3c9d-9f0f-a6886097b472 | -10.39924 | -45.40398 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1f64725e-f7b9-32cc-8b3f-ae93c49416e6 | -8.86511 | -46.84479 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f2386b7-304a-3b54-b840-8099377ec7bd | -11.23541 | -47.79103 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 935bba7c-25bc-3f60-8c6d-7261c8d6c52a | -11.78301 | -47.92775 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd2768a3-e330-3f41-97c0-36d57c7a763a | -10.83656 | -46.57728 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33299b3f-0952-35b0-9a18-244ea35546d9 | -10.1913 | -45.50943 | 2025-10-05 04:46:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 769e8107-d332-3682-b07b-320071d636ad | -13.31084 | -48.08394 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c84b099c-f551-3c01-9d71-1af88c334c39 | -6.73141 | -50.94126 | 2025-10-05 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6a8022f-6ad6-3569-b48c-a3370f6c8841 | -11.53295 | -54.50583 | 2025-10-05 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a947bab0-9cfd-3766-8af7-e801407ca323 | -7.34977 | -45.22253 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7bc3987c-b29f-37be-99b0-3329862145fd | -9.26174 | -51.8014 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0361f9d0-83c4-3433-8c7f-6919aeb937b6 | -7.24767 | -44.89466 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d171f91b-3001-3b7b-8c0b-7398b011bf81 | -13.50169 | -47.28181 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4089308-5f52-3de3-a647-89b4bb66a0ec | -13.30696 | -48.08331 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a897b401-4090-3299-94db-80e7477ae54f | -6.72942 | -45.98083 | 2025-10-05 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62d2db8c-903f-3b97-8f48-02cc3209da5a | -11.30913 | -49.98956 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d60ca6cb-26d9-3dd2-91b4-321db155b511 | -5.48423 | -51.06149 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b177d41-9603-34f4-bcdc-f16793b31fa4 | -13.27846 | -47.61609 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8b48ef96-8bb1-3fda-94c4-b58d1bb38102 | -8.5905 | -46.32067 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ad36fb0e-dcbc-31bf-8d70-a69c8792701f | -11.20806 | -54.98333 | 2025-10-05 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f7560e07-3a54-33e9-985f-e72ed6debd2f | -6.461 | -44.57541 | 2025-10-05 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f9bf9de8-d558-30dd-891e-32a2550c6100 | -13.52547 | -47.29159 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a11b45d6-bacf-3e44-8b39-70560c341fab | -11.13089 | -47.92247 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0531a68f-f5fc-30e9-ab68-ca146d919665 | -10.46572 | -57.49142 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 13df34cd-f702-3ca8-8ffd-609bf9f861de | -8.66835 | -45.79662 | 2025-10-05 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c21323a6-dee9-341f-881b-5b3a909f69d1 | -13.14758 | -50.93995 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d21e8a56-e32f-3188-adc8-2b13afe92616 | -7.72469 | -42.3899 | 2025-10-05 04:46:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 04e79bc4-330e-3c19-8bcf-eb2e448ba624 | -11.02373 | -50.69709 | 2025-10-05 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8dbd5f7f-73a4-3d75-becd-c3d508893e84 | -11.01083 | -50.69136 | 2025-10-05 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e03a46a-8c39-39c0-b362-4e0846a9aa2c | -13.1356 | -50.88093 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| b71ab6a0-580d-3509-abbb-6dc326c09f55 | -10.57849 | -51.60204 | 2025-10-05 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a02fd97-2ff1-3407-b4d2-b95b90f37e45 | -11.38215 | -54.35136 | 2025-10-05 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bb2b674-c174-36bb-8cba-19b49f289106 | -11.95242 | -51.47037 | 2025-10-05 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62bb0f3a-a7da-3710-a41f-d82d6c2f65bd | -13.09913 | -47.84719 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4999df8a-f2a4-3e44-af88-3854154caaef | -8.42115 | -46.80871 | 2025-10-05 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a90210f-f801-3b72-b524-24a9cecf3148 | -10.46237 | -47.81397 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0dc4443f-cbab-345e-a262-99fe0f18a446 | -11.1678 | -47.82518 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README84.md)
