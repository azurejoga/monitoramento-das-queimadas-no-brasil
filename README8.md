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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47496028-51b9-3249-984d-6cda09b9ec03 | -7.39488 | -45.92588 | 2025-05-24 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa520524-aad1-342b-8ea6-100c4563eecf | -8.74905 | -44.92374 | 2025-05-24 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1a9febd0-6283-3314-be73-a44bec212362 | -9.4959 | -47.48066 | 2025-05-24 04:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 512290fb-374d-333a-9196-439742cbc08e | -7.21864 | -43.12151 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fa38e1fc-085f-3e78-bd33-5595ff73af89 | -6.21496 | -43.34525 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0763fddf-c238-316e-b608-a598250727d6 | -6.22109 | -43.3728 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a798707-3a4d-3268-9d78-c3e75abd0dc2 | -9.49445 | -40.34439 | 2025-05-24 04:06:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| de09280d-0a59-3a7e-ab2f-04ae857c0acb | -6.7007 | -44.35711 | 2025-05-24 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dd3948f-cb8f-3801-9bf1-e7fec408a902 | -10.54929 | -42.42716 | 2025-05-24 04:06:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c3438074-a8b6-36ba-89f5-dc4cdc43d1b9 | -7.51235 | -43.17213 | 2025-05-24 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 50aebee7-42c3-3756-9f4d-7b05fcc3c874 | -7.48181 | -43.38329 | 2025-05-24 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58541bbe-2c6d-39e8-b490-55a1ad5154ac | -8.07166 | -43.11771 | 2025-05-24 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 0eaf1124-f173-3e46-8c30-057d566cdc77 | -4.28951 | -48.26687 | 2025-05-24 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b9664f5a-4fad-398c-a767-84bdfe55b926 | -6.21437 | -43.34895 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fa0de9f-1c90-35b9-802d-0ec8e07338b4 | -9.11448 | -47.65176 | 2025-05-24 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76748c30-3ae1-3a87-ac72-447a50834616 | -10.05339 | -45.3606 | 2025-05-24 04:06:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3ec4db4-0a6f-321a-b704-6a39c7a41b19 | -7.22317 | -43.11483 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8f5dd97a-cc08-30ad-ab0e-af4413b81298 | -6.22451 | -43.37336 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dab21e85-6d88-3589-9fc6-c8bcf193a125 | -7.22934 | -43.11952 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| c3f692f6-13a5-327d-89d7-84cb562aff35 | -6.69781 | -44.35247 | 2025-05-24 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7e059bf-2912-34b6-bb9d-28298e9a9796 | -7.20736 | -43.12711 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 21bdbbf6-3c57-3f62-bb73-6c7d2b551880 | -7.19607 | -43.13272 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 00c10cf0-5680-3b38-a63a-6f1ab73f4978 | -7.07227 | -44.9331 | 2025-05-24 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 19e3c462-071c-3deb-89b1-dc909adb28c1 | -4.28783 | -48.27692 | 2025-05-24 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e3917fbf-6d01-397c-9466-94a4f98eb2d6 | -7.65517 | -46.10478 | 2025-05-24 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ca433c96-79ee-335a-ae76-4b3cc81e8ae9 | -6.22793 | -43.37391 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f3ff5d4-a8b0-3a92-9e74-261c1a413b11 | -7.96376 | -47.21275 | 2025-05-24 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72680c42-94ea-3dfb-a2ab-846edc2e9b14 | -8.19647 | -49.16623 | 2025-05-24 04:06:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81c4dd2f-f04d-394e-b46c-be214e5ac23e | -6.22523 | -43.34685 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9a32bd48-f163-38a5-ba38-603b30e20824 | -8.75659 | -48.03405 | 2025-05-24 04:06:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb457884-1716-369e-81c5-90207f75401d | -7.06862 | -44.93256 | 2025-05-24 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 152c5159-0d92-3d5b-9c16-ae4ba7abb161 | -9.37539 | -48.39808 | 2025-05-24 04:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e25cbf75-4480-332b-bdf9-3658ce16cf3d | -6.69716 | -44.35648 | 2025-05-24 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2dbf38d-c5e6-36fd-904e-2885aa499f3c | -10.48953 | -42.41786 | 2025-05-24 04:06:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| be48fd03-4617-3304-b16c-4ed994ac6854 | -6.70136 | -44.35306 | 2025-05-24 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea1f679f-c46a-38ad-81ff-6f1e77f109ae | -7.65902 | -46.10542 | 2025-05-24 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 35d93f1d-b140-31de-94ac-b70ad8bb4db5 | -10.0283 | -48.69651 | 2025-05-24 04:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48b9e3ca-adf9-3e7e-9b9e-397d1079f494 | -10.55536 | -42.43172 | 2025-05-24 04:06:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 358bdb3f-89a3-3e1e-8b60-b89f83c51a2c | -8.06773 | -43.12075 | 2025-05-24 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a36a7cfe-6332-3eb8-8ed2-381b092cd22a | -7.20678 | -43.13072 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ce7f6918-b22a-3fc6-9b4c-b53e5d94075b | -4.29252 | -48.2777 | 2025-05-24 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d36b82ee-4156-34e2-8c68-1e822a974934 | -8.37317 | -47.08673 | 2025-05-24 04:06:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0960f64-c14d-36bd-8c59-6d06d9c42874 | -6.95138 | -42.79571 | 2025-05-24 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0df10b6d-cc06-3045-850f-f6c39ea9b849 | -8.7516 | -48.03738 | 2025-05-24 04:06:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8aef60ba-8fe7-3f49-a353-5847bcdfb245 | -10.5526 | -42.42769 | 2025-05-24 04:06:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9520535d-687a-373d-bb30-eb1216862310 | -8.07837 | -43.1188 | 2025-05-24 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| f7d2897d-8a96-3a07-b608-3b904f3ade24 | -7.79237 | -42.22805 | 2025-05-24 04:06:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ad945f28-71ac-300d-994c-ff201c7f3903 | -7.07973 | -46.05264 | 2025-05-24 04:06:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6deea33e-0a00-3e7f-bbd8-63f38557deb8 | -9.53154 | -44.06746 | 2025-05-24 04:06:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 028e6272-ca5d-37bb-a401-8095d03375aa | -6.21378 | -43.35265 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab815044-56ab-3772-bd6f-db57684ecabb | -4.28868 | -48.27184 | 2025-05-24 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 25dbd98c-d6f6-34ec-a648-3fe76028cc0e | -7.79917 | -46.22577 | 2025-05-24 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7823ba9f-6056-31e1-a678-8bb3a132dc23 | -8.07559 | -43.11468 | 2025-05-24 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| ef74533f-15f0-3bbe-8ca4-2c61417b75a0 | -4.29336 | -48.27266 | 2025-05-24 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e54de1cc-aa80-3dd4-a182-84a1ed7f6956 | -10.49229 | -42.42189 | 2025-05-24 04:06:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f666ce3-0474-3ed7-9d2e-bf956f163102 | -9.88857 | -48.77312 | 2025-05-24 04:06:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca526f45-6c77-3a85-945d-dff784be9d80 | -6.22511 | -43.36963 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5a6cdf1-eb61-3cb3-abcf-ea9f7667c3f0 | -7.0679 | -44.93688 | 2025-05-24 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d831263c-7218-3064-bd89-87505fc0640e | -6.94746 | -42.79872 | 2025-05-24 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cc664c1b-605c-3eb0-93d5-2ebf2c883063 | -5.57562 | -45.19801 | 2025-05-24 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be17578c-98ad-37e3-878d-c6254b524adf | -9.80717 | -48.25874 | 2025-05-24 04:06:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e30267e3-c987-385e-b665-9d8be41cc107 | -8.75589 | -48.03809 | 2025-05-24 04:06:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22cd6e10-6e8b-39c1-997f-c253b22a7d54 | -7.22597 | -43.11898 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| e97f9a89-f7d3-3406-bd9b-f326a776f452 | -9.8881 | -48.7717 | 2025-05-24 04:06:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43e2fa11-5cf7-30e2-84db-d476fc07a3bb | -6.22405 | -43.35425 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 206df895-fc71-3b33-899d-4122e0928df7 | -9.1158 | -47.64428 | 2025-05-24 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d751402a-59d0-31cc-8d4b-451638136ffe | -7.79998 | -46.22085 | 2025-05-24 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0a070c8-e095-3d0f-9e2b-ec8177bd9e70 | -5.35032 | -43.74846 | 2025-05-24 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee4c8732-8058-3876-b34e-af2ace19989b | -6.2178 | -43.34948 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7ce9a33e-04da-3594-b783-b94f77ed16c5 | -7.2198 | -43.1143 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 365dd02e-de26-3e2f-bbdc-66053174a95d | -7.21131 | -43.12403 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b013ca95-a2c5-340b-a583-cd756a7a227e | -6.22853 | -43.37019 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8713a930-9f1a-3710-9faf-66b898b0f4b8 | -7.0836 | -46.05326 | 2025-05-24 04:06:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5766611-1f28-3f49-a6da-81272331ea0e | -6.495 | -47.48824 | 2025-05-24 04:06:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b59d0640-837a-35b8-a6e1-7742e4b42e78 | -6.22688 | -43.35849 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d46a3e79-f1ce-3d76-ac6b-e31cc171ee4e | -7.22539 | -43.12259 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 1f69283e-7398-3c3b-a3f8-3c3c3c97cbbc | -7.22259 | -43.11844 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8f9dc552-9510-3620-8286-696d498ebc47 | -7.21922 | -43.1179 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2033d439-b469-33c0-8814-de9b32fbc980 | -5.57636 | -45.19347 | 2025-05-24 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9c5343b-88c6-32b5-90c6-2e0685d69cd0 | -9.73437 | -45.42639 | 2025-05-24 04:06:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8df11253-2339-33b3-8669-f5a8b59e457f | -7.95455 | -46.8255 | 2025-05-24 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 099db7e7-8b72-37f4-8352-858f15a7d0f7 | -9.49787 | -40.34492 | 2025-05-24 04:06:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2931335d-6e67-391a-834f-9eb4a6bdb27e | -7.27494 | -43.25299 | 2025-05-24 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8e78ec3-0dca-38ef-822f-36169ceb9e43 | -8.74549 | -44.92314 | 2025-05-24 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b788bbe4-cf5d-3712-ae55-462cebb754a5 | -6.22063 | -43.35372 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 808eaacf-8fe4-392f-b7b7-384c2045fec7 | -6.22629 | -43.36219 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c84e062-4796-36e1-b588-0d60ad84e38c | -11.12129 | -42.13458 | 2025-05-24 04:06:00 | NOAA-20 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 09a49402-39f5-3365-bfec-4207078dab52 | -7.19211 | -43.13581 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| abd82ad4-94f5-36ac-a425-7fc72302de4a | -7.54918 | -45.86221 | 2025-05-24 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d0f270e-5833-35b9-b7ce-b0541114a52b | -7.1927 | -43.13218 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e0045a12-f3ef-384a-9685-e3322f46d822 | -9.11514 | -47.64802 | 2025-05-24 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8af50914-edc6-30fa-8dc0-7d881bc4c77c | -7.19945 | -43.13326 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0ce1a0eb-d008-313d-858b-0d809a5638f0 | -6.95025 | -42.80283 | 2025-05-24 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 64a70290-64c2-3f00-8aab-7a8671dfa77a | -7.21469 | -43.12458 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fe2b58a4-4337-39d5-84a3-70a5e692143c | -7.06934 | -44.92828 | 2025-05-24 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d3b1f059-a30a-3b30-87c5-384fd2a24695 | -6.94916 | -42.78806 | 2025-05-24 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7b0e9351-d78e-3374-a1f2-2dbb2c85fef4 | -7.22992 | -43.11591 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e19383a7-9630-3922-93d4-6f215fce478a | -8.0683 | -43.11717 | 2025-05-24 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 171ea4df-90b4-3e94-8475-6c0d5d38ba42 | -6.70201 | -44.34903 | 2025-05-24 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bd13424-e98e-3322-890c-5e3891155ab2 | -8.07501 | -43.11826 | 2025-05-24 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |


[Clique aqui para ver as próximas entradas](README9.md)
