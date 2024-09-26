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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b7f3d97-9ec7-3d87-a8c3-90f0bd9cc8e2 | -9.42134 | -65.45553 | 2024-09-26 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 753e8dc4-13a9-3cfe-91ed-bfa07a3b35b1 | -9.42052 | -65.45973 | 2024-09-26 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ca6494d-0cca-33cb-bba3-c998b09052ac | -9.42024 | -65.46067 | 2024-09-26 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6352268a-9f28-3aa8-bc80-688fb1c9c415 | -9.35788 | -65.63197 | 2024-09-26 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0da8abf8-0fa3-390e-aaab-ed6bf5b59b90 | -9.35202 | -65.63089 | 2024-09-26 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99de6a86-ad10-35b0-8f15-3b59bfd9ebe4 | -11.96976 | -64.95603 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30dffad4-3dd3-3eef-bcca-8c96dc788f2f | -11.96909 | -64.95951 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcf08bf3-8a89-37cf-9c89-c1aa7e3d7bc8 | -11.26803 | -65.28385 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c12b908b-58e7-35ab-9ad3-bf1bd7f4a434 | -11.26731 | -65.28758 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c8c97eed-f2b6-3a30-be5c-5dac64eaa179 | -11.2666 | -65.2913 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a7dc735f-5330-3fd8-883a-41328dcf702c | -11.26249 | -65.28275 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1e9c60f7-24c2-3594-9d53-1fb195f66b01 | -11.26175 | -65.28654 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1adc2a68-02d4-349b-a47b-438546a69141 | -11.26104 | -65.29028 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7761dc6b-c4f2-3222-a307-a5e15aeaf1cc | -11.26032 | -65.29398 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ef654c83-e11a-3140-b5ba-7773b7066f7d | -11.25623 | -65.28535 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e8033dc3-b273-3a4f-b7a3-6fda475101f2 | -11.2555 | -65.28916 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6049a8dd-a840-35c3-a4b8-ab4f925f55dd | -11.25477 | -65.29295 | 2024-09-26 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6de906a7-9907-33b9-ac3f-64ad9bcaab26 | -18.38492 | -42.8009 | 2024-09-26 05:01:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9b445b4f-a7e8-3ae8-9446-d0bac4bb121d | -18.37845 | -42.79296 | 2024-09-26 05:01:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c3a3d324-e5d2-3280-ad38-b5a7ec9d8e91 | -18.26866 | -42.68359 | 2024-09-26 05:01:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 1ee45c76-4552-346a-82ab-0004710faa82 | -20.12327 | -43.43999 | 2024-09-26 05:01:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 29bda295-dcf6-3546-bce4-6dcd7bae4bb1 | -20.12292 | -43.44539 | 2024-09-26 05:01:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 73fa93a2-a9a4-3559-802b-217f6b56522d | -19.58988 | -42.62888 | 2024-09-26 05:01:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.0 |
| 7c96e577-ff22-3d6c-ab20-a3bed2f5724d | -19.5852 | -42.63048 | 2024-09-26 05:01:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| d3d0e0e8-9d06-3be8-bf2a-2151ae6eb902 | -19.58276 | -42.62697 | 2024-09-26 05:01:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f6375948-53ef-31dc-bb10-a1402e8c8153 | -22.1748 | -43.44055 | 2024-09-26 05:01:00 | NOAA-21 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e773ef7c-4d6f-3a73-bb1d-4e1ceb4dd694 | -22.17428 | -43.44827 | 2024-09-26 05:01:00 | NOAA-21 | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3a780f0f-2ffb-3e61-a191-0bb606932f75 | -21.40315 | -42.96568 | 2024-09-26 05:01:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2fb1c513-89da-3985-9ef2-10311d853518 | -21.39893 | -42.9627 | 2024-09-26 05:01:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 7d2e0d92-a8c1-317d-95f1-8984313a0f82 | -21.39856 | -42.96836 | 2024-09-26 05:01:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| a229b461-2d79-3dc2-8652-c9af959b5702 | -21.39626 | -42.96069 | 2024-09-26 05:01:00 | NOAA-21 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 04c2419f-4e7e-363c-9181-f337028e4332 | -21.39586 | -42.96639 | 2024-09-26 05:01:00 | NOAA-21 | GUARANI | MINAS GERAIS | Brasil | 3128402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| bb354a70-13a6-3256-b27d-39b37f0f32d5 | -17.92781 | -44.27065 | 2024-09-26 05:01:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43c820bd-aa9a-38bb-af8e-99a28a7b8db9 | -17.85227 | -44.45931 | 2024-09-26 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3922917-d04e-39fc-950c-2bf848ea685b | -17.8518 | -44.46452 | 2024-09-26 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fbc5e83-ef25-3aa8-a187-bcf8f12cf6bc | -17.8503 | -44.45945 | 2024-09-26 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c66303d7-706f-3c11-a6ba-d4969cd33fc1 | -17.8498 | -44.46465 | 2024-09-26 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 78e1ba3e-b440-3b06-8a0e-ab5b59aa01a5 | -17.84545 | -44.46344 | 2024-09-26 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5dcb8483-33be-3dfc-ae37-ed10c8e6c838 | -18.68665 | -43.85823 | 2024-09-26 05:01:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54e800d0-2786-3bd0-83a5-3c03cd55bf4f | -18.28357 | -44.04557 | 2024-09-26 05:01:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b2c8e6ec-35ae-39e9-8cf7-27837e7dc94e | -18.02888 | -44.3876 | 2024-09-26 05:01:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 802669a3-17cc-355e-a8f3-39401b7a4e6e | -17.98982 | -44.46032 | 2024-09-26 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f16616f-1c9b-3a0f-bba0-16b69e783299 | -17.98935 | -44.46553 | 2024-09-26 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dd783107-a0f4-3266-80ed-16749bad6cfa | -17.98888 | -44.47067 | 2024-09-26 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 828e6cba-3011-3757-8643-396110836991 | -17.9884 | -44.47597 | 2024-09-26 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c5ac54b-ce87-3f8f-b7eb-038e0dc9247f | -18.86306 | -43.43002 | 2024-09-26 05:01:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| b23d62a1-1180-3eb3-b00a-b12444c72105 | -18.86241 | -43.43847 | 2024-09-26 05:01:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 1619b7bd-7796-366a-abb1-65058979e0fe | -18.86151 | -43.43362 | 2024-09-26 05:01:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| bfa32ce1-082c-36cd-91ca-1b759b262880 | -18.86088 | -43.44113 | 2024-09-26 05:01:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| ca0d9549-ef46-3afa-b86d-0afc86f6fc11 | -18.81089 | -43.62686 | 2024-09-26 05:01:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9f080e33-1b35-3d18-8fc4-6b0e8e14d1f8 | -18.8041 | -43.62632 | 2024-09-26 05:01:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| de9970ae-5e9c-3360-8cf7-8c37786e87f4 | -18.61243 | -43.41467 | 2024-09-26 05:01:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 79d046c7-4800-353c-ab84-58d87d8329e8 | -19.78613 | -44.13024 | 2024-09-26 05:01:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9da42085-02f5-33a0-843a-3a0a718f16bd | -19.78558 | -44.1366 | 2024-09-26 05:01:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12f75cab-e07f-3f56-bb8f-041afa361e88 | -19.78382 | -44.1287 | 2024-09-26 05:01:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b859c3bd-f93d-32a4-a2f7-96964ea4cc8d | -19.78331 | -44.13506 | 2024-09-26 05:01:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c70ea4d-6813-3622-8810-1f2b5923f7ad | -19.75206 | -43.97696 | 2024-09-26 05:01:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8415fecf-1178-3223-a723-ed9213856df7 | -19.60019 | -44.92674 | 2024-09-26 05:01:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc77f2b7-5a5b-3423-be96-566fceb06fc0 | -19.52338 | -44.50628 | 2024-09-26 05:01:00 | NOAA-21 | CACHOEIRA DA PRATA | MINAS GERAIS | Brasil | 3109600 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34b4d720-346a-3da2-8f94-6e3ca265c731 | -20.52247 | -43.9366 | 2024-09-26 05:01:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 08a00a35-0630-3a8a-b438-607f1e7024fb | -20.5182 | -43.93699 | 2024-09-26 05:01:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| dfad0e4d-8eee-32b1-8c1d-2f46f7887b44 | -20.42755 | -44.10666 | 2024-09-26 05:01:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 08da6182-1b64-3e13-a6e6-961df9346f5e | -20.17731 | -43.55429 | 2024-09-26 05:01:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 828e74f2-3787-3f7c-b818-fdee26af4616 | -20.17697 | -43.5586 | 2024-09-26 05:01:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 421dc975-88dc-30fc-a773-c93b24654605 | -20.17003 | -43.55862 | 2024-09-26 05:01:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| af5bf631-db8d-3ff1-a1e5-5b42a35f8859 | -20.1697 | -43.56288 | 2024-09-26 05:01:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| c0d83603-ba73-3a88-b4d2-8e2a0f503885 | -20.1693 | -43.56808 | 2024-09-26 05:01:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 6e33db2a-269d-3c61-8496-ecd6aaa91b94 | -20.16575 | -43.52359 | 2024-09-26 05:01:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4b98d7f0-1eb7-3dcf-a0ee-7d605889af94 | -20.16488 | -43.52896 | 2024-09-26 05:01:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2ec88117-8519-3a61-add7-d564c9855e2c | -20.16319 | -43.55733 | 2024-09-26 05:01:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| b8354a73-e2e6-37d4-baa1-51acae978fe5 | -20.16285 | -43.56184 | 2024-09-26 05:01:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| e9bdaf25-bc0f-3842-882b-afe7b8bf7d36 | -20.1628 | -43.55428 | 2024-09-26 05:01:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 575084d9-db6c-3030-9241-89d40f32243d | -20.1624 | -43.55908 | 2024-09-26 05:01:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a6acd0f2-0ca5-30ac-80b3-52ea5a94cdab | -20.162 | -43.56382 | 2024-09-26 05:01:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 1ae8ffca-a6fb-39ed-979e-687ca8e40e45 | -20.15886 | -43.51763 | 2024-09-26 05:01:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 58595c55-e6c2-355a-a209-b291e5244d14 | -20.15884 | -43.52309 | 2024-09-26 05:01:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a1c08810-7bfe-388d-aff6-ab619e284627 | -20.15642 | -43.55509 | 2024-09-26 05:01:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 66397787-564e-334a-9b0f-9f63c9ce9e22 | -20.14836 | -44.33553 | 2024-09-26 05:01:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5b212699-11e8-3675-9180-6a81370d1d30 | -20.14787 | -44.34138 | 2024-09-26 05:01:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 237f2ec9-3392-3378-b502-f69d55c8aa54 | -20.14699 | -44.3519 | 2024-09-26 05:01:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d55c2a2d-69ae-31d6-b3b9-b307944f04b1 | -20.13733 | -43.53203 | 2024-09-26 05:01:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4da2d734-08d9-33de-922c-5869499877ab | -20.13664 | -43.5345 | 2024-09-26 05:01:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 515aa637-9567-3808-93af-8ffd94097b48 | -20.13052 | -43.53018 | 2024-09-26 05:01:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 573b5f1f-e0c0-3272-a820-a993696872d0 | -20.12984 | -43.53278 | 2024-09-26 05:01:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 38e19233-d08d-3b90-ac3d-7f9f2a20a156 | -19.93699 | -43.77586 | 2024-09-26 05:01:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 03f9774d-17e5-3994-bb5d-e784162b1e80 | -19.93602 | -43.78816 | 2024-09-26 05:01:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a52f6c51-a0ff-32df-878b-6c8b133c4c0d | -19.93513 | -43.79941 | 2024-09-26 05:01:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 5fb95311-621e-3a4b-9d0d-94746f61fc3a | -19.93484 | -43.77555 | 2024-09-26 05:01:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 6065d289-170a-3aab-8f6a-86feb44d4c83 | -19.93382 | -43.78759 | 2024-09-26 05:01:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| fa716fbb-0ca3-3f79-a5b6-f5e11e0973fc | -19.93334 | -43.79314 | 2024-09-26 05:01:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1756d280-78dc-3400-a736-43fca6427df5 | -19.93287 | -43.79865 | 2024-09-26 05:01:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 853659a2-9e6a-334d-a93b-e63bfe3abf98 | -19.92921 | -43.78785 | 2024-09-26 05:01:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 4665958c-c5a1-371c-8eed-bf8882dd7979 | -19.92879 | -43.7932 | 2024-09-26 05:01:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a7f6cf4e-7b7f-3ab5-913b-f186e55d7bd2 | -19.92836 | -43.79867 | 2024-09-26 05:01:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d13e6d3b-7f26-329f-b16a-a0ecf645bbab | -19.92703 | -43.78699 | 2024-09-26 05:01:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a9742d77-572d-334c-8ba0-7cfb762de0fc | -19.92609 | -43.798 | 2024-09-26 05:01:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| a05fcbc3-603a-3567-950b-428ff14a74cc | -22.30754 | -44.04189 | 2024-09-26 05:01:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 470a4e41-8da2-3af2-ab96-c142da5a82b4 | -22.30708 | -44.0485 | 2024-09-26 05:01:00 | NOAA-21 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 29.2 |
| d03832bc-4ad7-39b9-b361-7d196e05394a | -22.30626 | -44.04396 | 2024-09-26 05:01:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 72987466-bd32-3171-8262-9ad91af012f5 | -22.30579 | -44.05027 | 2024-09-26 05:01:00 | NOAA-21 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |


[Clique aqui para ver as próximas entradas](README142.md)
