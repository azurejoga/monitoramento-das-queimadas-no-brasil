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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d4a9b1d-a9cc-3199-9227-57a70eb8cd27 | -10.01455 | -62.3926 | 2025-08-26 05:38:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48a7bc2e-29bb-390b-b91e-b82f04d8111b | -9.08591 | -62.6688 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f32a964a-03c6-3345-9981-ebb77653120b | -9.32823 | -63.19544 | 2025-08-26 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2a95c05-f4d1-3cfd-9d59-8ef48e24c098 | -9.15988 | -59.55292 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3e6163ca-80ea-353b-af2a-55f6a1d1605b | -9.20027 | -60.9265 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eaa3f6a3-e12a-3a48-bcae-ae19811d5f12 | -8.54464 | -63.51826 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea05c143-1987-3fe5-9da1-ae4f0e61b3dc | -8.87601 | -62.45794 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fe4d3eb-74f9-3c9d-b3fc-7318a826d9b7 | -12.43948 | -63.70123 | 2025-08-26 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 831b446a-2869-3781-a9ce-9762b40f73ef | -9.16529 | -59.5142 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b75e6842-8535-30f3-8e43-b77b0202f035 | -8.98708 | -65.42792 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03a8af20-21f1-3721-a8a0-62ac2668447a | -13.00911 | -56.89433 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20973e7e-11fb-3381-8d6d-ef54cf765dcf | -10.45775 | -58.00181 | 2025-08-26 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98b1e09b-bd0b-3fd3-a4c5-3e0682ad4416 | -9.02349 | -65.39015 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7bd7ab0-435f-3448-b5e1-0ba57fbb485e | -9.01696 | -65.68781 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42f380fd-258f-3f3c-8955-e3b068e169bd | -9.26385 | -56.90644 | 2025-08-26 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22bdb6c5-7663-31fc-86fd-5b9d6d2658f7 | -10.02207 | -62.38982 | 2025-08-26 05:38:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b959040a-7cc5-3632-8fb1-39dccb33fc0f | -9.16417 | -60.76918 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cfca9e0-2c34-3803-b04e-9ee5c1dfaf4e | -8.98539 | -65.43852 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9414e67d-117d-3a08-bc5b-4891e272fb2e | -8.98431 | -63.64135 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0dc59f42-af46-32a1-ae6d-7a6bdf0d0566 | -9.16563 | -59.45276 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ff56098-6d57-39e5-94df-1ddb7b0a05d4 | -8.98652 | -65.43145 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e2444bbd-8353-3d78-8bb3-8cbeaa346dae | -8.66099 | -63.4248 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bf6f5f3-53bd-3104-9bce-ccacf47b53d8 | -9.17368 | -59.45397 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2472330c-538c-3cfc-9e88-8ecab7575a7a | -11.0623 | -52.00838 | 2025-08-26 05:38:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 14181a9e-6220-34e2-96ad-9084a5aef244 | -14.29359 | -60.36527 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a327cd3c-7b0c-3e94-93a3-c1a68489db40 | -9.17651 | -59.60875 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4e26034-8f37-3a26-8b4f-227815a3c3f2 | -9.00824 | -65.38055 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 520b9d12-4597-34e6-ac29-9a0a33f5b59c | -8.86113 | -62.44029 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79b62a59-8886-347c-bf04-5dede3d597b6 | -9.67553 | -67.50779 | 2025-08-26 05:38:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae5b9e8a-320e-3e83-a048-109e15aba92c | -10.42239 | -64.38978 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd4b89e4-1b94-32b2-aba1-cda4c55ac4d3 | -9.04752 | -65.73311 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b10820cf-1845-3c6b-8134-9a4da154478e | -9.06264 | -65.72451 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d140a5e6-aa44-3a27-b0fc-c9224405aa16 | -9.8299 | -64.26318 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 887cde2a-fed4-3e08-843f-a683dd4a6f0a | -9.04866 | -65.72594 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d755ae9-3e03-3682-8010-dfb7af1ff46c | -8.6338 | -62.64574 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98dee90b-1b56-3324-a8bd-f051af258e46 | -9.20829 | -60.9232 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdfa9d01-d6ba-3ecc-b881-6beeb51609b6 | -8.63281 | -67.24802 | 2025-08-26 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 01a7c5e7-04aa-3533-a483-9f4a0531dd0f | -9.16578 | -59.51067 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71f4e56f-e311-3836-a985-44f46996c020 | -9.79457 | -64.25045 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44d6b19b-f4af-3bd5-8f5b-9afb8d445a49 | -8.68738 | -62.8714 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63e02b8d-7bae-3ee8-b23d-df32d00d3b34 | -9.64122 | -59.64088 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0c859f88-157c-3cfc-bf80-75eb2620fb02 | -14.2855 | -60.36357 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88743f1e-e8da-3f76-8b98-f2aab26dd021 | -11.56184 | -52.1289 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ffebb91e-a606-3760-866d-beb2a7e0ad9e | -10.25371 | -59.1017 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c9738f8-9174-3ee5-8619-6273d036b634 | -9.00934 | -65.3952 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e0ff864-3814-3e00-bc2f-9db7e80ccf97 | -9.16184 | -59.53886 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4f586118-f868-342c-9868-495bd037a968 | -11.56662 | -52.11033 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ef22d3f-8fda-38c8-b100-ac0be8851d0b | -12.00099 | -64.84304 | 2025-08-26 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b07c3be-d673-3c6e-a925-66405abad7ed | -9.00545 | -65.39821 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ebc0e0e-b030-30bc-9cfb-bfea3155644b | -8.85602 | -62.45103 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a289d1ef-2410-3f4b-9f5d-04698978308a | -9.47475 | -57.82154 | 2025-08-26 05:38:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 413f30b1-c017-3a75-808c-f4beffc6455a | -8.99766 | -65.40421 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7b3e8d8b-8665-3431-9ca8-a93faa7cfa8d | -11.30795 | -55.10524 | 2025-08-26 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 925dbf62-d8ad-3ff4-8784-516bc54fea8c | -8.87198 | -62.43811 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a265ab1-1521-3dcb-b4d1-8665ac737784 | -9.16012 | -59.46285 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 29957c52-c524-3e56-b864-2c412967896d | -9.64271 | -59.63047 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b1b6cb5-7651-3f01-bbaa-56308a8e12e4 | -8.54108 | -62.65465 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c7f1b229-6937-309d-9e90-29c8af1c95ee | -9.18187 | -59.54189 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 721328d8-a81c-34e6-b569-e39ecb063393 | -9.18887 | -59.52129 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b7be95b-1e28-3b7a-8b91-62ad7a6151e3 | -8.8363 | -62.451 | 2025-08-26 05:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 93.6 |
| af6b322d-4c99-3adf-afd0-d9ebf0d3ab6a | -9.1722 | -59.4629 | 2025-08-26 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| a3e18744-e73d-33fd-9b41-69705bc52c30 | -8.9874 | -65.4192 | 2025-08-26 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| f7383f5a-4bb3-32fa-b22a-405d7d92d8f7 | -9.1903 | -59.5395 | 2025-08-26 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 334f4695-39c7-368d-bd73-a30ef0426bcb | -6.2275 | -60.018 | 2025-08-26 05:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 25bbeeac-f174-3ef3-8279-4510d3ea9420 | -6.8229 | -58.956 | 2025-08-26 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 5c90b581-65ce-3759-a053-815f88f4bfef | -8.8364 | -62.4321 | 2025-08-26 05:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| abc20d10-4ca0-3854-ad22-6437e727863c | -9.1715 | -59.5599 | 2025-08-26 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| fef13d10-aab4-32e9-97b3-1e7317e6a378 | -8.8734 | -62.4495 | 2025-08-26 05:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 703e1679-55c7-397b-a4fd-c6788e8cd12f | -4.9605 | -55.8226 | 2025-08-26 05:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 1a30268d-60cf-3075-9e5c-f9112f956c3a | -9.1718 | -59.5211 | 2025-08-26 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 9fd0a1c8-db0f-386b-94da-b48a6fd57d3f | -9.1717 | -59.5405 | 2025-08-26 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| b019a850-e9ed-3c12-aa48-4c9a70512e9a | -6.2459 | -60.0174 | 2025-08-26 05:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 5464605c-2555-3374-9bcd-b0dc70a79d39 | -6.8228 | -58.9753 | 2025-08-26 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 1b896aea-833c-322a-9bb1-f4aca2c4cf6b | -8.855 | -62.4313 | 2025-08-26 05:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 0c4d4d15-bd13-33fe-9edd-58249312e30b | -8.8548 | -62.4503 | 2025-08-26 05:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 187.3 |
| cb12f67f-0293-3b29-baa3-35c9fdb0e612 | -9.1909 | -59.4619 | 2025-08-26 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 18b05932-97b2-37f3-864c-e7c61b0a1c29 | -9.1904 | -59.5201 | 2025-08-26 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 00d48938-9745-31df-a422-9952892204a9 | -6.7635 | -59.6718 | 2025-08-26 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| c86c84f8-c3ae-3cfe-bf68-f517386e6355 | -6.7819 | -59.6711 | 2025-08-26 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| a7aae2c4-6bdb-30c7-833d-641cb7536ece | -8.8734 | -62.4495 | 2025-08-26 05:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e15b31f3-caa2-3cd7-9d24-5422124c705c | -6.7819 | -59.6711 | 2025-08-26 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| fb0e3635-5c0f-37f0-ab6e-46ae02d3e839 | -8.8548 | -62.4503 | 2025-08-26 05:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 186.8 |
| 50618365-b6cb-3fa8-b252-089141afa00c | -8.8363 | -62.451 | 2025-08-26 05:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 75df9467-0937-31a8-afee-261a6d5f999f | -9.1909 | -59.4619 | 2025-08-26 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| b4929362-0673-3834-a3cf-300f260cfb29 | -6.2459 | -60.0174 | 2025-08-26 05:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| b214f02b-221f-3b83-a0a1-06c74623452f | -8.8364 | -62.4321 | 2025-08-26 05:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 7dda92e6-c7dd-3778-b153-ec2f27245cec | -9.1715 | -59.5599 | 2025-08-26 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 2814bf01-930c-3e18-bf46-6cb918201533 | -9.1717 | -59.5405 | 2025-08-26 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 45dc5fbd-2136-30ed-acbe-b2af99b2e79a | -8.8547 | -62.4692 | 2025-08-26 05:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 37e04e27-458b-3f3a-af31-e791700766b7 | -4.9605 | -55.8226 | 2025-08-26 05:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 11c099d4-9583-3af5-9aa5-6b861cf684ae | -9.1718 | -59.5211 | 2025-08-26 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ba97e8b1-610a-363b-a740-1e0f23f43b10 | -9.1722 | -59.4629 | 2025-08-26 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 3dce020c-4e3d-38b8-913c-dabecec18b60 | -9.1904 | -59.5201 | 2025-08-26 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 87400b38-a821-3efe-8158-bf9deee3725f | -9.1903 | -59.5395 | 2025-08-26 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 04e6618e-0243-3969-8626-4d096466d9d5 | -6.8228 | -58.9753 | 2025-08-26 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| e6fcbc43-aa2b-3a65-a8da-e0b54aa9903f | -13.423 | -46.873 | 2025-08-26 05:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 959cf09e-53ef-3e2d-aea6-fffa185e6fa4 | -6.7635 | -59.6718 | 2025-08-26 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 22a3cf3b-b87e-3e1b-8a15-c8c4aacf7b06 | -8.855 | -62.4313 | 2025-08-26 05:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 800f9d7f-3b92-37c0-9538-2d1bdf39e377 | -6.8229 | -58.956 | 2025-08-26 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| b0a34bfc-e505-3769-aeb6-8a26ab01eaaf | -9.1718 | -59.5211 | 2025-08-26 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |


[Clique aqui para ver as próximas entradas](README89.md)
