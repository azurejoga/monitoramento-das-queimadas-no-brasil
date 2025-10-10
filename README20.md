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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 807e55cb-dd52-3784-a11a-4dfcfa736273 | -4.0105 | -43.28716 | 2025-10-10 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcf292b6-c334-3e8a-8946-b9eb2660414a | -3.0603 | -39.66154 | 2025-10-10 03:57:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 130f5445-6f7a-3e8e-a7f1-6ede8bb872e8 | -3.00074 | -48.7362 | 2025-10-10 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 927b4ed6-3e35-3bbd-abe9-c0c2746224ac | -2.68429 | -48.3952 | 2025-10-10 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e40d041c-509e-30ab-bd0c-0de20f117b36 | -2.88059 | -50.73365 | 2025-10-10 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78aa21e1-2dbc-3be4-acc7-7b5961803fcb | -3.97586 | -44.15462 | 2025-10-10 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19d80c9a-61c8-348f-a011-f374da0f9afa | -3.72885 | -40.52248 | 2025-10-10 03:57:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 784ef220-b814-304a-892d-603a99d87206 | -3.14308 | -44.43098 | 2025-10-10 03:57:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8cada29-bcf9-380f-bbb5-bade48649b00 | -4.44242 | -40.77743 | 2025-10-10 03:57:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a3d03852-03f8-34a4-8166-8e42fb5c6ed3 | -3.17338 | -43.88102 | 2025-10-10 03:57:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fde06dbc-31e9-36fc-986c-73622f5cb243 | -14.8869 | -48.2362 | 2025-10-10 04:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 55.9 |
| a3412c84-a2d1-3904-9623-9000358d9d2d | -17.9376 | -45.0148 | 2025-10-10 04:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 130.7 |
| cae533af-916f-3bd7-9eee-64876dfb52e6 | -10.1517 | -44.5984 | 2025-10-10 04:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| e0fa7bb7-bef6-3093-a739-105758365a84 | -17.8832 | -57.4971 | 2025-10-10 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.9 |
| eef8d4fb-92fd-38df-aa45-f9ba9cc1eafe | -4.5515 | -46.6801 | 2025-10-10 04:00:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 57426098-8628-3b0d-9f2f-21f613f2b5ff | -10.1707 | -44.5959 | 2025-10-10 04:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 9651d910-3308-3101-8161-3e89a75d835e | -12.6294 | -45.0517 | 2025-10-10 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| b7a43fb6-27ac-3114-847c-f5105cdb8316 | -7.40238 | -39.78941 | 2025-10-10 04:00:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4a63da00-b4fc-3205-b157-7b7285ec2983 | -8.20713 | -43.37975 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 47867968-258d-320a-bade-8a13a5707e5b | -6.73909 | -42.84818 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b9cde9f2-83ba-33f2-a22b-45460abff126 | -6.81581 | -42.79646 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 64df55a1-d4f7-340c-972e-684d4eb79b81 | -7.7383 | -42.41201 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c55d514f-af25-3abd-be85-d4dc67795db3 | -4.13832 | -47.65738 | 2025-10-10 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e1e09f8-6465-39dd-8d53-3d890cc156e3 | -9.43937 | -45.45851 | 2025-10-10 04:00:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65493ab5-6f80-37fe-af3d-4eee3ee91ea4 | -7.77609 | -44.04972 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1aa6b0da-0e03-35e7-8aa1-2fd06028dff0 | -8.37235 | -47.76344 | 2025-10-10 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a8fb150-ff47-3fd5-aee5-f7b145342d61 | -6.07322 | -42.59507 | 2025-10-10 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| baf9523c-5e2a-3eb7-9e2f-cad868a12024 | -6.74626 | -42.84931 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e85f5e95-bdea-3b93-a652-6eb0d1ca6a6c | -7.54803 | -44.60678 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 92465faa-0cd5-38bb-a93d-d2bb57f9b63d | -7.7753 | -44.05439 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb74e4b2-8bb7-3514-ba6e-ff0c17a1dc5a | -10.15971 | -44.60361 | 2025-10-10 04:00:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b77f3e83-0c05-3420-90dd-bb2729824ff6 | -8.16485 | -43.32115 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a675e10b-3dcd-369e-8523-66ce3a8d297c | -8.16056 | -43.32467 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 865043b7-10e5-3619-9406-9a0a4c20f95f | -5.08589 | -42.47919 | 2025-10-10 04:00:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 68e0a990-19d4-3f11-bf02-ca48e1ccfdc6 | -4.69263 | -45.8388 | 2025-10-10 04:00:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9f66c60-6786-3e2a-ad1d-08cf90abb096 | -4.48194 | -42.86045 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc7fb819-9e6d-3545-8261-141ef25ce024 | -6.98915 | -41.93156 | 2025-10-10 04:00:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fcd4c3c1-b3ef-33be-abcf-00a3ca1f7264 | -4.65358 | -43.19981 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b1f4466a-dd7c-3505-b1ec-3b0e1d6a49c1 | -7.67938 | -42.39135 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f57d7b3e-d4fb-32bf-bc1d-a3d5d0248ea8 | -7.53595 | -44.29874 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2cea11af-243c-3347-b24d-bd2bd836c29d | -7.78515 | -44.18005 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2575ae2-4de4-36b8-87fb-2adb2da3f232 | -6.75251 | -42.83339 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5ca61769-7346-3ab5-adcb-bff15b419b59 | -7.79388 | -42.60448 | 2025-10-10 04:00:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 625ad513-f87c-37a1-abdc-c0ace01f2688 | -6.74984 | -42.84987 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 52539da8-3169-39ef-8df3-eb8b043e150a | -5.14215 | -46.2728 | 2025-10-10 04:00:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 753d2035-c7b4-3dfd-b055-70f13a508127 | -6.64155 | -43.68066 | 2025-10-10 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 80c25c71-0e74-3d24-9d5c-360388a9d770 | -7.40676 | -45.91732 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f440e561-7d64-37e1-9d3f-acbbdbfb1df4 | -7.49441 | -43.10723 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a4da949d-9663-307d-a099-4c91e8d35333 | -9.29896 | -40.23364 | 2025-10-10 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1b73381c-29c6-3e08-be19-c6553eaaec5f | -4.39249 | -44.08825 | 2025-10-10 04:00:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 208ce086-12ab-3a4e-b80d-270aea8f66ab | -8.53034 | -46.17161 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1806ea76-d8f3-384a-9708-52f1d5ec3cbd | -7.77688 | -44.04509 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| edf9490a-fc44-3be2-aac0-23035fad6b32 | -7.5529 | -44.2918 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a99a026-1d3d-3827-929a-afa5962806df | -4.47388 | -42.8636 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a9fdbe0-871a-3069-b88f-7216142bc624 | -7.77548 | -44.05153 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9fb82fa-024f-3a49-97cc-12c61189d2da | -7.42374 | -42.977 | 2025-10-10 04:00:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0be64203-1d6f-3d18-8419-d72c303076ad | -8.89679 | -46.01195 | 2025-10-10 04:00:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8e471c2-5c11-3e41-9445-68d3b951ebc0 | -7.70209 | -42.38316 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1ff783b7-0930-3883-ba0b-dadd149e1cb3 | -5.05365 | -43.33353 | 2025-10-10 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 56460821-9c6d-3715-8810-6b54b9098c76 | -7.73894 | -42.40816 | 2025-10-10 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 120600e3-79f5-3ab6-9a3c-783e42a49902 | -7.79503 | -44.19091 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21c0748f-077a-31b6-b111-fbe780d44689 | -6.72588 | -42.88408 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 873e0e4c-9fa4-3a79-99db-619e4d8f619d | -6.74267 | -42.84874 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 248972e7-14d2-30c1-941e-e74d683ce7fb | -4.68306 | -45.84147 | 2025-10-10 04:00:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cda936a-c5c2-3887-b4ad-e2cce5968842 | -8.50975 | -46.16394 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68e1c853-e608-3509-b729-e866e9505009 | -8.19764 | -47.85919 | 2025-10-10 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c2cdc44-faf0-3ece-af8e-b2606412b280 | -8.52324 | -46.16202 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6e2cb49-6acb-348b-be6c-7b089eebbe55 | -8.20848 | -43.37144 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| c8330b6c-4255-38f7-90b6-2e0ac8023a44 | -7.00042 | -46.99515 | 2025-10-10 04:00:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d233f645-6c08-3c35-af01-2f60c09be4a2 | -4.8488 | -42.7676 | 2025-10-10 04:00:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6587851-73a5-3601-9137-04f6d647a33b | -7.79454 | -42.60056 | 2025-10-10 04:00:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b223b2a6-54b2-3f9b-b95d-40470a19bd79 | -6.65989 | -41.99504 | 2025-10-10 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0cb3acf6-c3af-3d1f-a846-85a23e2ef4f5 | -6.66402 | -47.74553 | 2025-10-10 04:00:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b6fbfdc-61a8-3629-bc3b-61323de89897 | -9.33152 | -46.10928 | 2025-10-10 04:00:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2a51a65-c99a-374d-896c-8197feb2e817 | -8.17924 | -43.32366 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2855fcab-40e6-3aff-8c54-f4630e46d206 | -6.59389 | -44.80174 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ba1dd6e-6035-3aaf-a2fe-adbf05408129 | -6.18666 | -39.69957 | 2025-10-10 04:00:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9ff4d248-06db-3bba-b507-2a8ba502e96f | -8.51178 | -46.17736 | 2025-10-10 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 814f1512-dcc7-3fb5-8925-928338a3b187 | -10.15827 | -44.58914 | 2025-10-10 04:00:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3d65e49f-de00-3022-80de-8600209756f0 | -4.64967 | -44.92636 | 2025-10-10 04:00:00 | NOAA-20 | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1180f40f-79ee-3b60-aa1d-76a39dd1c12d | -6.70996 | -42.20301 | 2025-10-10 04:00:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 245706ff-6148-3fda-aa1a-a9420948257d | -7.57689 | -44.38468 | 2025-10-10 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4ac0933-691e-3e57-87ee-94b7b6e110a0 | -8.52701 | -44.5963 | 2025-10-10 04:00:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8bd6860-0cf7-38f6-8e4c-b3c9a0f4360a | -7.33282 | -47.82108 | 2025-10-10 04:00:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 70850553-13ad-389d-93ef-fbfa5e64782b | -7.26686 | -44.09976 | 2025-10-10 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee52b2e5-65ee-3b4e-aaad-7543a2fc7dfc | -7.77987 | -44.0503 | 2025-10-10 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8c3f68e-6a0e-3c35-b7e1-4513edb23eb5 | -7.79324 | -42.60839 | 2025-10-10 04:00:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5b40d755-0516-3ee0-841a-4c510133b365 | -8.60223 | -41.41049 | 2025-10-10 04:00:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6ec16423-5c20-3457-a9fb-439173250179 | -8.20351 | -43.37915 | 2025-10-10 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c446e336-338f-3c1e-8d14-ca9d2faff2e5 | -7.6659 | -42.58477 | 2025-10-10 04:00:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fda06b00-0b13-3101-ad15-b9fdf9ce444e | -5.74758 | -42.52432 | 2025-10-10 04:00:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b3739198-0edc-3c02-9f83-3be3d9ec09d7 | -7.27361 | -41.97243 | 2025-10-10 04:00:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5518ec64-3634-315c-addb-b023c546d947 | -6.73194 | -42.84694 | 2025-10-10 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 0fd3b6dd-4658-3056-8462-8aaf494bd75f | -6.59274 | -44.62386 | 2025-10-10 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b997c13e-ccbe-303e-8c6f-bcce13a15ff2 | -10.1575 | -44.59372 | 2025-10-10 04:00:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6e6567bc-cf07-3dae-b0e9-7251be13665c | -5.83732 | -42.44395 | 2025-10-10 04:00:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 16eaa874-e7d3-396e-a0e6-80e7f5418383 | -5.419 | -41.33747 | 2025-10-10 04:00:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 85e6fda6-2773-3da5-9e84-aabbcad02fb7 | -9.66435 | -43.84269 | 2025-10-10 04:00:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c757b9bf-c966-35c3-af43-f1100e56a89c | -7.78608 | -46.55338 | 2025-10-10 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 619dc98d-e3f5-3162-9551-938a8af75693 | -7.14273 | -42.17269 | 2025-10-10 04:00:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README21.md)
