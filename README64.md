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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7c55dec-adc1-37ce-9848-8b539b9f21e0 | -8.40236 | -46.26014 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be26476e-8bdc-31cc-807e-f34a8897b55d | -12.68421 | -44.39728 | 2025-10-16 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a65696b5-5fd9-3f35-9ff1-858726c295aa | -10.12573 | -44.56867 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97ba6ad2-fdf1-3193-8b07-456e4062b826 | -10.50679 | -43.38295 | 2025-10-16 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dfb5a924-baa1-3389-9516-e56197d1633a | -10.61952 | -45.24354 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d433be5-1180-3c76-af48-989dabf367ca | -11.43735 | -44.15458 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e03579cf-7d16-303a-939a-1c69d776d1a8 | -10.05607 | -43.84374 | 2025-10-16 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ba230c2-9c93-3261-8bb8-610c5ebd969c | -8.45828 | -46.18777 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 672d196d-7894-37d0-a28a-9f652d0daa8f | -9.22903 | -48.59881 | 2025-10-16 04:40:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 01901330-6525-340c-92e2-d71bedcc02f6 | -10.67333 | -45.32836 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e396d171-d542-3025-b16c-1add7900466c | -10.66276 | -45.31622 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 109e2732-07bf-312b-a714-1a6f612ad127 | -12.60746 | -56.50782 | 2025-10-16 04:40:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14f27f7e-0cb7-36bf-88fc-15bb721a40b4 | -11.57376 | -48.55488 | 2025-10-16 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b50a553e-e633-34dc-8d44-dd4076c57eb9 | -10.70439 | -44.43518 | 2025-10-16 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 23015612-b565-3f89-b530-1a44e45fb733 | -10.91781 | -47.58398 | 2025-10-16 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 789c5773-df1d-34f1-9771-c150b2beab81 | -8.46201 | -46.1881 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 97edbd37-5485-3688-a1f9-21e8e2509b2f | -8.41658 | -44.7345 | 2025-10-16 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56b295d8-2449-3a27-8802-644ee7477b99 | -15.59958 | -42.39423 | 2025-10-16 04:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66827808-d680-3d5c-9342-bf6cf4626d61 | -11.43296 | -44.15396 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d6a7c7c2-9eaf-3d21-8a38-bef387489c88 | -8.45563 | -44.18375 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f6c16fff-2380-30f7-86bf-8e5a9f8fb316 | -9.22958 | -48.5952 | 2025-10-16 04:40:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4317c9f9-cfca-372a-a098-4423910ba801 | -11.47809 | -44.15155 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cee7ba26-8732-39f4-b5bf-e792f27d12fc | -11.76413 | -61.07365 | 2025-10-16 04:40:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96b90eb7-2cdf-3f32-aa01-d8e138d0fb92 | -10.66876 | -45.33162 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a53c53c3-739e-3dee-9ce6-dbfbf204e75c | -10.72276 | -47.58204 | 2025-10-16 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c742d49b-e70d-37d5-86f0-00889fb59288 | -9.68465 | -44.53256 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9b831e61-a513-3687-a8cf-fb57b3306cd2 | -10.17075 | -47.10662 | 2025-10-16 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 295f4dfa-d3ee-3f7d-a947-4e6283363757 | -10.50932 | -43.36344 | 2025-10-16 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17d9c813-4a88-327b-a32d-70c67f839a6d | -9.22935 | -46.8924 | 2025-10-16 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ae08ee7-1157-3082-abdc-c0b4b400d059 | -10.72629 | -47.5826 | 2025-10-16 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c4efec26-17e3-3590-801c-f59b43c9b0c2 | -10.81491 | -43.94272 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| db9e9b7f-e60a-3371-9007-e5759208b06d | -11.57968 | -44.06576 | 2025-10-16 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8b98d216-a01a-3fd9-8b81-56f65bf2fa6f | -11.45316 | -44.1701 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2efbfb49-302e-3d3f-b077-7923153a1d14 | -10.14196 | -44.54351 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 975afa4f-b831-3bf1-b4f8-7b9ae5cfd7f5 | -10.81172 | -43.99941 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf18031f-a8c4-36d3-b4db-48a280e67954 | -9.14092 | -48.43964 | 2025-10-16 04:40:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd781247-da28-3ba5-b37c-5d1dd0297fc5 | -10.83583 | -43.95441 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cef2e1fc-2887-3b9a-81e0-7c0bdbbb8846 | -11.34791 | -45.26567 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b05f180-af83-3300-8c91-c98efb22ec44 | -12.64264 | -44.30152 | 2025-10-16 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 458fb745-52ab-3812-b8a2-0190197fcbe3 | -10.15037 | -44.5447 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c4ac978-6eb0-3797-8eb5-b59dc5bc8c5d | -13.98932 | -41.78947 | 2025-10-16 04:40:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0125e56a-5b19-3df2-abb2-136c881cc2f1 | -10.13089 | -44.55433 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ea43911-8089-34bc-b54d-683694290e8f | -10.88901 | -47.92762 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f34ed04-0816-39d2-bae0-0dbd6e6abc87 | -14.65062 | -42.38378 | 2025-10-16 04:40:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e8a6b3f5-275d-3d21-801f-3fb91c63e49b | -12.13229 | -46.72102 | 2025-10-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cfc9cb9-980d-30a8-96f9-8660704f174f | -9.68483 | -44.50119 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3993ef34-bf80-3768-89f9-fdd04fedf94c | -12.17266 | -45.06462 | 2025-10-16 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fdc6d27-1894-3d5b-abfa-c93e8425f8b0 | -10.12887 | -44.57708 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 97ec21f2-9628-3919-84c3-5555ff14f3a0 | -9.71567 | -44.5042 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 039e9174-a74c-37f3-9664-75cca1039c21 | -10.13938 | -44.56256 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9e756267-06ea-3b13-8492-f079cc5bfcb4 | -10.65535 | -45.25249 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eae87de2-8fb3-3d83-b757-b009d75cd46e | -11.4276 | -44.05949 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fb3ce88-8748-3e0e-8c09-a3a8a6a1f733 | -10.17373 | -47.11135 | 2025-10-16 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2999b60-9aa1-3a85-8e0b-7558c4e9d1e5 | -14.01143 | -42.14387 | 2025-10-16 04:40:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a55b2da3-f36c-30d2-89ac-72d85cdc3eeb | -8.46287 | -46.2333 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 77edb7c5-fa72-3cb8-9746-ad6ae8c926b0 | -10.0402 | -43.82833 | 2025-10-16 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bdf45e6-0a6b-399f-8550-6b78000b853f | -8.55464 | -44.58122 | 2025-10-16 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04b5d104-52ad-308e-b148-2437bc09044a | -10.77625 | -47.26648 | 2025-10-16 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 795bf419-221c-3bd4-a7dc-91e2618418f3 | -8.20083 | -47.01663 | 2025-10-16 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 855a124d-3af1-325e-9c8a-6fa15e427034 | -11.56976 | -48.55814 | 2025-10-16 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e454b496-1aaa-38c6-a155-a68e1d06ce71 | -15.59321 | -42.4035 | 2025-10-16 04:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7652b1d9-95a3-3425-aed7-2a53cd45a32f | -11.5865 | -48.18294 | 2025-10-16 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cefe3f65-891a-3a11-a0c1-42dd8cb347ab | -13.8087 | -42.85971 | 2025-10-16 04:40:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9a995d40-eb65-378a-930f-c984e4c652c2 | -9.90189 | -48.15653 | 2025-10-16 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ff938cf-1e1f-350d-a067-43616f64bd6e | -10.82374 | -43.94403 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a09a636f-ea2b-35b6-a8ae-cbc12471bf36 | -11.75532 | -61.06914 | 2025-10-16 04:40:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ddfdea7-db35-3652-a6b6-ededf49c44b0 | -10.66732 | -45.31301 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 905c468f-05e7-30e5-b6d2-93abe7ffed54 | -10.13724 | -44.5468 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dd94da19-5fd2-3eae-a0d4-f4e5579d75fb | -8.19849 | -47.008 | 2025-10-16 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a66afc4-ee90-39a2-b007-9b041d23ce04 | -16.05166 | -43.70135 | 2025-10-16 04:40:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc8230cf-6001-3c75-b59a-4e546210406b | -10.91487 | -47.67842 | 2025-10-16 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b87529ef-70f1-3c1b-905c-9f4b433eb573 | -10.91012 | -47.58704 | 2025-10-16 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9924d4a7-4dd9-35c4-9d51-76663ddf2960 | -11.58733 | -44.07584 | 2025-10-16 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0a933ce1-767c-3325-9c14-eac167b517ce | -8.11789 | -55.28696 | 2025-10-16 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6935765-6eae-30bc-bb37-426cc3ecfb37 | -14.01105 | -42.14718 | 2025-10-16 04:40:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0a9b6ba0-21cb-3591-ae6b-056e46f788ed | -10.67087 | -45.32806 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7eba5a65-81ae-308b-b3ea-a0db762bc64d | -11.46134 | -44.17573 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0df962f8-f89a-38dd-a00f-64857af31ac3 | -8.29226 | -44.9619 | 2025-10-16 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3d1c59c-f1fa-30be-bdf3-11a59ac67d6c | -12.55238 | -52.21637 | 2025-10-16 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86fa5bf7-482e-3066-b303-46038b80b54d | -8.23454 | -47.86595 | 2025-10-16 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d78607a-f973-3824-b0c8-d0c60aaef803 | -9.25947 | -45.26403 | 2025-10-16 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9488b7b4-69bf-3f26-86a1-9aea205e15f2 | -11.87817 | -49.90734 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d184dcf-3692-3916-8cb4-4243f67d0d62 | -12.83883 | -43.81957 | 2025-10-16 04:40:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5157c17e-aabf-36d1-a09f-cc3a09b1e0f5 | -10.13252 | -44.55003 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6ecf8f96-74c2-3434-b26c-b9029f17e7c4 | -11.74205 | -44.22686 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ed704cb-2af4-3400-bbed-e8000a7465b8 | -10.82314 | -44.01435 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f97459bd-1161-3e8b-97de-bd79d4cd3e60 | -10.80675 | -44.00305 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a71f53d6-7d86-3a74-97a8-0eec6d0db908 | -10.42313 | -48.88509 | 2025-10-16 04:40:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72540d1f-2834-39cc-9274-d9a031654311 | -12.04606 | -47.66138 | 2025-10-16 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9cdca285-55b7-3345-a11d-b9f0193fbb9f | -13.65615 | -43.93016 | 2025-10-16 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1c987d95-182e-3106-a41a-f43982456cd4 | -9.69046 | -44.52165 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f6070117-0093-3983-8091-31415c21ca9a | -8.55821 | -44.5855 | 2025-10-16 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9f7ca82-8d7c-3a79-a562-b0cd1bb193a8 | -10.66929 | -45.32793 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f9bd3e9-38b9-3ce0-8cab-c97278a375b5 | -14.21579 | -48.78286 | 2025-10-16 04:40:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b828ec4b-5e5b-3a4d-b52e-f97e20ba117b | -9.68065 | -44.50052 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85be3574-6806-3502-a60d-beab25f787ae | -10.86372 | -44.40987 | 2025-10-16 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89aa7fb2-8550-30ae-9088-d2489307d700 | -10.12655 | -44.58482 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c1ef3e16-7c1d-3b7b-adcf-d7dc425feb58 | -8.45589 | -46.17827 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d9a0a3b-c0d0-3927-84fd-b1e369af3451 | -11.58028 | -44.06134 | 2025-10-16 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c94bcebd-ae0f-38e7-bfab-251a831242a5 | -11.05793 | -44.78497 | 2025-10-16 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README65.md)
