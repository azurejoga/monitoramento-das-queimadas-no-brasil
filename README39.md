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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec2c11f2-b6a8-3825-a729-b68f5ca64348 | -14.9879 | -49.96523 | 2025-10-07 04:10:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1cb0ebe-9aef-3cfb-a3bf-a64aad14478f | -14.91801 | -51.40808 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 07f87050-6415-3d2d-800b-e145ad82db7b | -14.01323 | -43.85329 | 2025-10-07 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3abba4a-33e5-3a46-8373-c6054db5171d | -12.89718 | -54.75809 | 2025-10-07 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 058f7b3c-20a1-3fd4-9d8f-73533e2297e0 | -18.97216 | -47.8322 | 2025-10-07 04:10:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8e58d53d-1230-32f6-87cf-9e0d3f545acc | -15.21734 | -56.77303 | 2025-10-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 857a1635-10c3-3991-9874-36a825374be9 | -15.2804 | -46.34 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21c7bdeb-6185-3ba9-83b1-d74d11da4531 | -12.85856 | -43.81411 | 2025-10-07 04:10:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87802fdf-1de5-38a1-97d0-ed5221d4c198 | -16.29208 | -45.24322 | 2025-10-07 04:10:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2589fff9-2057-35b8-9707-a00723d9117f | -13.36159 | -47.56748 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 23941667-43ca-35e7-a741-99a2a5bf2578 | -12.72627 | -47.94345 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fff2c041-a770-39e9-b253-c6600adac08b | -14.76453 | -46.03566 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c11bfebb-b11f-3f6d-9a3f-58865c332efa | -13.98546 | -53.91454 | 2025-10-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ae3479ca-2e42-3ba7-bac3-e64e2860a145 | -14.41923 | -41.45831 | 2025-10-07 04:10:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 52e05e1d-5e7d-310c-8011-bd2fad9349a7 | -15.36783 | -47.30849 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a51c5c9-9d1e-34ce-acea-72ebe5596c73 | -15.60979 | -52.57077 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a424f3a-82e3-33fa-bdf5-4aac53e71af5 | -12.25836 | -47.846 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b8f0fb2-3ac1-31e3-aa77-e0b2a6af0eda | -13.37571 | -48.03259 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dfb9cc74-ffeb-3c7e-846f-8205f696662e | -20.32426 | -45.11652 | 2025-10-07 04:10:00 | NOAA-21 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| a077816e-9ea8-3151-8d71-df7fdad7aee9 | -18.11813 | -53.36185 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b07610fd-19ed-33d0-b147-5a50df64e89c | -14.76319 | -46.04364 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 236df07a-59e0-3ef8-9317-13809d48e6cd | -14.92512 | -46.80214 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5cc293c4-eb06-3e3f-8cc4-f2de4a113f13 | -16.02314 | -50.97338 | 2025-10-07 04:10:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d2429226-e87f-3cef-ac93-98798a0d2f02 | -13.39485 | -42.69812 | 2025-10-07 04:10:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5732667e-5fda-34d3-9f0e-705eaa48767d | -14.76252 | -46.04763 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b9deb952-03a9-3e11-aa01-c719bdd7b8c2 | -15.39187 | -48.00985 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bd020604-27b3-375b-b664-d0ca09038e68 | -15.6 | -43.17247 | 2025-10-07 04:10:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e060e6f8-7104-3653-820e-57861c08a81f | -18.11952 | -53.35503 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 143483d5-7491-3e8b-810a-08fc9c55d9b6 | -17.98197 | -44.98879 | 2025-10-07 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14040468-b221-3967-8ff8-669f1aa24c3f | -13.17576 | -43.55406 | 2025-10-07 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a18fd7c-e153-32aa-875e-0419a7c82f03 | -14.54192 | -46.64302 | 2025-10-07 04:10:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6ce1b01-e22a-3cc2-91dc-5a5010d64b5d | -18.28617 | -45.46458 | 2025-10-07 04:10:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2f35e3f8-0a67-3eb3-a290-7d4af04fa710 | -15.09483 | -46.64264 | 2025-10-07 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5d8a8554-e613-3c0b-a6d8-3218a76a2ddb | -14.91021 | -46.86687 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9a648b15-ad5e-36f8-bc41-9c72d2628f47 | -15.6006 | -47.26875 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 090489c7-b1c9-34ca-8a4c-c0d974a14e6e | -14.72543 | -46.01233 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 337504cd-018f-3fd3-baf5-cd7f0528fda4 | -13.27195 | -48.07139 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98cb9105-edcb-3e70-9e9e-664dcaaea99d | -14.87941 | -51.42827 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cad9b6e3-f38f-3ce4-a5e2-f86389ac1626 | -13.78556 | -45.78498 | 2025-10-07 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27cc6c16-c6ff-3633-bc72-b3c9f8ec8821 | -15.50079 | -47.92243 | 2025-10-07 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5db30679-d626-36e0-86c3-650eff346822 | -18.60412 | -46.80063 | 2025-10-07 04:10:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 517cfbba-dd7a-3536-bcf1-d0a791ac7361 | -14.9469 | -51.46215 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25b3112b-ec03-36ea-973e-1343ce2391da | -15.60028 | -42.36949 | 2025-10-07 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed2e5c98-a797-3f03-8843-c31673887736 | -16.01864 | -50.97222 | 2025-10-07 04:10:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c55b68df-c7f9-3315-a707-3a6353fc602c | -18.15784 | -53.36295 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90c5d98b-1d44-38e0-9103-b64e8f1565e1 | -10.56031 | -56.55801 | 2025-10-07 04:10:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f4d4006-6802-3842-b318-eff091830e23 | -16.29148 | -45.24693 | 2025-10-07 04:10:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a74d1b5-8cc1-34c9-8e8c-1d577dfe49c9 | -11.15174 | -54.87848 | 2025-10-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9321cc5c-73b1-352c-9424-e0e35e39a8ea | -14.76749 | -46.06085 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dc6e6aec-e49e-32c1-bc91-35e54895bd3b | -17.54778 | -46.76117 | 2025-10-07 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3262d2ff-e4bf-3533-9359-7320fff93c6d | -14.75394 | -46.01326 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b498b24-7b02-30ad-bd61-4934b291e82e | -20.19159 | -45.41408 | 2025-10-07 04:10:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 2486d705-b9d4-3251-a53a-6edc69c105df | -15.22353 | -49.31437 | 2025-10-07 04:10:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd279653-271c-3de2-975f-ad1ebedaba8f | -14.92858 | -51.40462 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c10e9930-1d70-3b30-a38a-6207c9b49223 | -15.63574 | -43.00571 | 2025-10-07 04:10:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3a628780-070f-3cc6-aec1-f66379a12ef5 | -16.29124 | -50.98307 | 2025-10-07 04:10:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6005b5b-e63d-325e-bd58-8f98dd4975b6 | -18.67234 | -44.04061 | 2025-10-07 04:10:00 | NOAA-21 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9982a7ba-cbf4-3f86-a8a1-9b2231f79fde | -14.93091 | -51.44213 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d63c2ab-531c-335c-8632-56d9f3e2d7f9 | -13.86161 | -43.99258 | 2025-10-07 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff10523f-dbb1-3ca5-b6d3-76a4d98e82e1 | -16.38174 | -49.00123 | 2025-10-07 04:10:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f106ee04-aa10-3b46-9b57-6324825955d6 | -13.24406 | -48.45971 | 2025-10-07 04:10:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc82c38b-43c5-34ea-9ae4-8ecf58e84cab | -12.72958 | -47.93978 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 18cb1e58-3116-30cc-9bc4-796e61007f19 | -15.63648 | -47.61963 | 2025-10-07 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9069e01-0b1a-3006-a1c9-6103f721f5a8 | -13.28042 | -48.4673 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c7d0759-dd66-3aee-ac9f-0ae98f2f114b | -15.27513 | -44.13794 | 2025-10-07 04:10:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5e0f6f48-a466-3c0b-a1d9-c81be08ff27b | -20.20745 | -43.91577 | 2025-10-07 04:10:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 113a513d-2692-3e4e-a3f3-80a875c4bc26 | -15.99663 | -50.83603 | 2025-10-07 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76821608-217b-3854-a33f-8f2a62a91bb9 | -13.25471 | -48.06012 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 99505436-3f41-3540-adb7-cf5289b1393e | -14.91176 | -51.43832 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe5f4305-5eac-3c02-b3c4-46509c1aa4ef | -20.09639 | -44.19875 | 2025-10-07 04:10:00 | NOAA-21 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 392f742f-166c-378a-ba1d-dad90d649e6b | -13.50383 | -43.67374 | 2025-10-07 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 6ca5b7a5-dad4-380e-9e13-19d989711504 | -12.58878 | -48.10887 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d79bba2d-c987-3ffa-bc67-378515e84193 | -15.38891 | -48.0043 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11a3ddc2-173d-3f84-b717-e2c77dde39e6 | -13.68833 | -47.95617 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7cfc724-296f-3f56-9263-2c916ec39f03 | -14.71784 | -48.34829 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73534e52-dcff-36ed-995a-13c001506475 | -13.27 | -48.05952 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 96b88f43-8450-3511-b576-d6e8bc6899ef | -17.0687 | -43.37007 | 2025-10-07 04:10:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 997d0947-39ce-348c-b5b5-836fe1b5f850 | -14.24787 | -54.24781 | 2025-10-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91436f1a-563c-389a-bbba-94295a7b9f0b | -13.37002 | -47.56453 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04c5c12a-f53d-3df8-b895-28796be72861 | -13.25014 | -48.05633 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 70419306-23fc-3f3c-9421-c9a77c0e2c3e | -15.1948 | -56.82394 | 2025-10-07 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 337cf089-6a62-31e6-ab93-24baf699b200 | -13.10086 | -48.01357 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 21c99de6-9057-3923-9efd-fe03c7e9200f | -19.88982 | -42.60455 | 2025-10-07 04:10:00 | NOAA-21 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| aa8690b8-18b1-3997-bb76-e1c9783645e7 | -14.76305 | -46.02304 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 80f94b93-e442-3924-8e4a-5adcfee743cf | -14.76654 | -46.02366 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 950bc301-c118-3ac0-ade1-70986c52af2f | -19.38335 | -47.429 | 2025-10-07 04:10:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d003327c-ac00-333b-8805-fe809478a25e | -19.89673 | -44.05993 | 2025-10-07 04:10:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 82f7f1a3-20bb-3701-8031-acf1af78c176 | -13.78957 | -50.78391 | 2025-10-07 04:10:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d14012e-7030-3f07-9f2f-76fa57db30b2 | -14.92767 | -51.40798 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8f1923ea-fac7-3ae4-ab0b-240a038508ee | -14.92027 | -51.44561 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 86e606bf-021d-3d50-93f8-82faed4554f8 | -15.61182 | -52.56061 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 27804669-cdc2-3d25-89a4-4c30da132041 | -15.38594 | -47.99879 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b27c0e41-12c3-35f3-8f8d-1e4b15c347d3 | -15.65391 | -43.67876 | 2025-10-07 04:10:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b73b000e-fec6-3f9b-bd5e-79c46b4704a6 | -15.53515 | -46.85776 | 2025-10-07 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c5c4153-7b7c-3063-9843-bcbf1a220905 | -18.66903 | -44.04005 | 2025-10-07 04:10:00 | NOAA-21 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 197deb69-87f4-3c26-b6de-3fa5026f3875 | -13.08279 | -47.86415 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f1dfaa3-1152-3639-a6bd-a439567f1b6b | -15.38465 | -47.98388 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f863ab0c-9ae5-3524-bc80-2229062425e0 | -15.61624 | -52.56497 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f93f3397-f6cf-3812-a7e7-7a43c5acfdcc | -20.25999 | -41.93794 | 2025-10-07 04:10:00 | NOAA-21 | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8f040703-5f4c-336a-b11c-cb0b61aa0fb2 | -19.44677 | -46.46299 | 2025-10-07 04:10:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README40.md)
