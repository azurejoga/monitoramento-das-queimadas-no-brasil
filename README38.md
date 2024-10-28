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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e02ee03a-f83b-3be9-ae70-be51298a8942 | -5.53217 | -42.22478 | 2024-10-28 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 73967ab0-0b7a-3509-a198-ed2984bd88ba | -5.49183 | -42.81465 | 2024-10-28 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e983394e-d067-3d28-90f2-522877033791 | -5.46743 | -41.96774 | 2024-10-28 04:06:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1aeb8242-a2ac-384d-8d23-7f6a3e863bd3 | -5.42165 | -42.83336 | 2024-10-28 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1eff360c-4f54-3ede-bec9-f8d9b4b13fbd | -5.42108 | -42.83697 | 2024-10-28 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1926933c-44c7-311a-846c-c6e4248d0423 | -5.16024 | -42.42594 | 2024-10-28 04:06:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 115ca12c-3381-36db-a59a-5b75d3f738db | -5.15746 | -42.42186 | 2024-10-28 04:06:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ec072c81-e2a8-3f9b-87b1-ee4e46049d9f | -5.1569 | -42.42541 | 2024-10-28 04:06:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 119f6303-af2d-3d9f-bb05-ace0225215f7 | -5.30885 | -42.94523 | 2024-10-28 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 052a7e11-1a22-3b29-98f3-0abc25b31487 | -5.30546 | -42.94468 | 2024-10-28 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6132271-c09e-3e42-b248-5419496d9d03 | -5.3043 | -42.95197 | 2024-10-28 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d20f8a5-f637-37c6-a860-54eb891db485 | -5.29647 | -42.93576 | 2024-10-28 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98f19897-5794-3a15-8fb2-462681bfa518 | -5.29308 | -42.9352 | 2024-10-28 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcb547ac-874a-30e2-b849-4512eb31891a | -5.15992 | -42.80682 | 2024-10-28 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b02054e-c5b9-35ff-97d9-db85b10b3cb7 | -5.00122 | -43.11549 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4f8bfad-0ac8-3ec5-ac44-c75492196725 | -4.95896 | -43.2044 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5f20f45d-11f5-3c22-8c8d-b65b452d60d3 | -7.9259 | -42.83585 | 2024-10-28 04:06:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2ee2071c-4b6f-3a58-9c6a-31ed838fde4c | -7.92534 | -42.83937 | 2024-10-28 04:06:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 81e7bfec-e2ee-3474-b52a-d69ff60b1ef9 | -7.58718 | -42.29394 | 2024-10-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e988ce7c-be57-325f-b463-143de4e7767e | -7.32692 | -43.57516 | 2024-10-28 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8e337d63-1b98-3d66-bfbe-bf8648c5edbc | -7.32632 | -43.57884 | 2024-10-28 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7df0ec15-b4fc-3621-a1dc-0fe3f446dcc1 | -7.36061 | -43.29556 | 2024-10-28 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe909267-edac-3428-903e-e387ba9d986f | -7.35723 | -43.29501 | 2024-10-28 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38459e90-8791-37d2-b5a2-2c1bf9ba11de | -6.80222 | -42.40158 | 2024-10-28 04:06:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4800b18b-99af-3580-98ce-340ee1377709 | -6.6244 | -42.7921 | 2024-10-28 04:06:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b440e518-ec9c-3556-b7de-7b31cb7b33c4 | -6.62219 | -42.78446 | 2024-10-28 04:06:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0b2d98ed-7577-33c5-924f-846cc3694152 | -6.62162 | -42.78801 | 2024-10-28 04:06:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a98cba70-e393-375a-9e1d-7ad359cf1e9c | -6.62105 | -42.79157 | 2024-10-28 04:06:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| df73423d-05e3-3d96-a19a-6cb8b55660a1 | -6.61941 | -42.78037 | 2024-10-28 04:06:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 35bc8fd3-afac-36d7-8e35-4e30e6f03f35 | -6.61884 | -42.78392 | 2024-10-28 04:06:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5895af17-5c75-3407-86a5-0db59b439aca | -6.59348 | -42.28205 | 2024-10-28 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 067a571d-4ff2-3a40-890f-3d654e0d4d9f | -6.59293 | -42.28554 | 2024-10-28 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 59d5137e-0de7-3855-97ce-8304bce52fa0 | -6.59016 | -42.28155 | 2024-10-28 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4d9f9583-56cf-33f7-b511-a6b879c8d4c9 | -6.58907 | -42.24559 | 2024-10-28 04:06:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 35b74400-5d9e-30bd-9199-8ab4325b3579 | -6.69717 | -43.56324 | 2024-10-28 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d03ad4c-e527-3c7e-b976-76d3a2b74636 | -8.9537 | -42.97523 | 2024-10-28 04:06:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7092265f-b5ff-3ee3-afc2-a25e081f13cd | -8.13643 | -42.79405 | 2024-10-28 04:06:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cef2e32f-60a0-3cee-8aa3-49c4dce185f0 | -9.36438 | -43.36222 | 2024-10-28 04:06:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f32927b6-3aa7-3281-af80-3b68ef48b77f | -9.36161 | -43.35812 | 2024-10-28 04:06:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 12a6a2f7-8965-3aa5-b66b-9164932eb1cb | -9.35826 | -43.35757 | 2024-10-28 04:06:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 98cbdac2-e5ad-30be-bffa-28108348fcff | -8.01442 | -43.33995 | 2024-10-28 04:06:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 064ff864-a4e9-39f0-aeba-02cab632362f | -8.71765 | -44.02208 | 2024-10-28 04:06:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27d680fc-8ecc-36c7-b12a-250877afa672 | -8.71704 | -44.02585 | 2024-10-28 04:06:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba92b178-4459-3d3d-abb3-131d81b4341f | -8.22524 | -43.55279 | 2024-10-28 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21fe1bc7-c21e-3759-9199-212763de8ac8 | -9.96829 | -44.16521 | 2024-10-28 04:06:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ac96812-8cac-3e15-987b-7b3b44a5fe96 | -9.76756 | -43.88328 | 2024-10-28 04:06:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3b1501e-b1d5-34e7-bb07-013f37a1dbeb | -10.6563 | -44.0988 | 2024-10-28 04:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7a059b8e-e682-3c6f-82f5-b82025daca49 | -10.65292 | -44.09824 | 2024-10-28 04:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 848ad986-c802-3313-97d9-b703b4e1dc02 | -10.59518 | -44.28152 | 2024-10-28 04:06:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f69e8de0-d5fe-3f35-9a8f-ca2a7d3c9965 | -10.59238 | -44.27727 | 2024-10-28 04:06:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d5fbee6-3761-3628-9bf9-3bc5846b6a30 | -10.59178 | -44.28095 | 2024-10-28 04:06:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93a7606d-86e2-3b54-8092-33d0fc24ac22 | -10.59117 | -44.28465 | 2024-10-28 04:06:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a61c9c4c-b40a-3050-b570-f62171580b2a | -10.58838 | -44.2804 | 2024-10-28 04:06:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8dfc7ba-3257-35ae-9764-560c1c59c383 | -10.58777 | -44.28408 | 2024-10-28 04:06:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0886cba4-d2f1-3b1f-bae0-c47e7b2b2c3c | -10.58716 | -44.28778 | 2024-10-28 04:06:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 050d09b9-025a-38e0-927b-8b60497212d7 | -10.57296 | -44.28921 | 2024-10-28 04:06:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3fa18284-58ba-3dd5-9ce4-570755e5b96a | -10.57233 | -44.28925 | 2024-10-28 04:06:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 295ca5c3-f7f7-3bfa-8b31-befb6aea7393 | -10.37768 | -44.1742 | 2024-10-28 04:06:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12cb1d39-cf62-3db2-90ca-cf06b07498a6 | -10.14197 | -44.0227 | 2024-10-28 04:06:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9fc8166-37c0-3a7a-910b-9e71aaad10ad | -10.01911 | -44.06731 | 2024-10-28 04:06:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d40edc5a-f7d2-331d-bd2f-49ce22ae58f1 | -4.81319 | -44.72672 | 2024-10-28 04:06:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50ee1dac-5eaf-366a-b3a8-01c6f126568f | -4.81248 | -44.73109 | 2024-10-28 04:06:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1dc287c-e1df-3dd9-a3f7-0fd290e19f0d | -4.65388 | -44.66727 | 2024-10-28 04:06:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb89add2-d6ad-3f71-894b-45326966abf3 | -4.65316 | -44.67162 | 2024-10-28 04:06:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 77094442-5db2-3371-b926-0d2f56465930 | -4.52301 | -44.62261 | 2024-10-28 04:06:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65a6424b-8575-3c27-8178-140fc2ac150c | -4.98334 | -43.71096 | 2024-10-28 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c91d882e-59fb-3a09-9002-0e50d1047066 | -4.98272 | -43.71486 | 2024-10-28 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 93021d62-46d9-37b1-a607-75ba7f9c94cb | -4.9821 | -43.71874 | 2024-10-28 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7f3034f2-1899-3b4c-b236-7b39db0cea5e | -4.97985 | -43.71042 | 2024-10-28 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ed37110e-036b-3031-96dd-dd6804d83381 | -4.97922 | -43.7143 | 2024-10-28 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ca718854-fd76-3c98-81ed-bd221785ea7f | -4.74406 | -43.25524 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfc27acb-5885-3f88-bdf9-eac15ea7b914 | -4.74062 | -43.25471 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce234fa8-7be9-3f6d-ad7a-5efa28883f55 | -4.73778 | -43.25042 | 2024-10-28 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3b79c0a-8fc1-3691-a3f3-3b35cc477fa8 | -4.51369 | -43.97576 | 2024-10-28 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53e19c18-660c-3006-8a98-cdc53d7ea655 | -4.4313 | -43.9666 | 2024-10-28 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89e6ff31-f09e-3ee6-b27c-28d60bd771ed | -4.81722 | -44.35628 | 2024-10-28 04:06:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63d7be05-5e87-3bab-8a63-e7428fa27dbf | -4.69571 | -44.48061 | 2024-10-28 04:06:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1dd61133-3f60-3f0f-a367-a2376a09097a | -4.68814 | -44.34534 | 2024-10-28 04:06:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1897c9f-3a01-32df-9c5c-fa8f6076c71d | -4.68673 | -44.34617 | 2024-10-28 04:06:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28bdaad1-1765-3dc7-9125-04e86e54534c | -6.09558 | -44.76634 | 2024-10-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3403bd89-cbc1-3daf-a96a-390e821d0e2a | -5.92036 | -44.66702 | 2024-10-28 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d67dc04-c07a-3a45-b312-7bcc23b1e04f | -5.9197 | -44.67118 | 2024-10-28 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24cbb685-47a5-31d0-8bd1-076d01d710bf | -5.84144 | -44.76271 | 2024-10-28 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c6e03090-c780-3e59-804e-f9f2e938629d | -5.0443 | -44.80504 | 2024-10-28 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f35af3c7-f63e-3677-ac4a-36409800d2f4 | -5.12646 | -43.86016 | 2024-10-28 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ab2eb2b-ce71-3592-8a73-5849f9eb9417 | -5.09775 | -43.85941 | 2024-10-28 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b064a143-bf2d-3ed4-ae28-ed668680858a | -5.09358 | -43.86284 | 2024-10-28 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df97ee5c-eb63-346f-9d4d-c46e841e012e | -5.06432 | -44.21989 | 2024-10-28 04:06:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 346f475c-6e94-380f-a7b2-6909d16a5a44 | -5.06075 | -44.21929 | 2024-10-28 04:06:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f1999865-8480-3ce8-8b46-4f5180a3b77f | -5.05718 | -44.2187 | 2024-10-28 04:06:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2fe9937c-d624-367c-930f-65fcba774c4a | -5.05651 | -44.22276 | 2024-10-28 04:06:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 01407675-ce47-3b1d-861f-8062fa7a6432 | -5.05585 | -44.22683 | 2024-10-28 04:06:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df042ab8-923e-3719-949f-1140e5eaebab | -5.05361 | -44.2181 | 2024-10-28 04:06:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da987331-7244-3354-a716-8fd7c984df89 | -6.45481 | -43.91386 | 2024-10-28 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7e1ed2ae-11fc-34d6-ae50-7e454a1f18a6 | -6.24351 | -43.52594 | 2024-10-28 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bda00dc-c7dd-32c2-ae68-29fd51304c66 | -5.93372 | -43.66431 | 2024-10-28 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 24d0db72-43c3-34da-9847-f622321949d2 | -5.91566 | -43.95347 | 2024-10-28 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4d13da4-c49e-3359-a8bc-d9669ed167ad | -5.80026 | -43.92764 | 2024-10-28 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcd23f33-777b-331d-bbd0-d603a3de1958 | -5.7377 | -43.88648 | 2024-10-28 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4281100d-c45d-3ddd-9788-0166b2b99559 | -5.70222 | -43.92882 | 2024-10-28 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README39.md)
