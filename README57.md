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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 788e0fcd-5d0b-33db-800d-94d78d94102f | -19.2239 | -57.66042 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c38bea02-e520-37a0-96be-2db8a756c27f | -14.93706 | -56.32881 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c5993397-f0c4-30ae-ab73-22ebaabfcf37 | -20.95298 | -57.57124 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| cf207ba7-de03-3492-846f-cc69ff56707c | -21.71215 | -47.14232 | 2026-08-29 04:55:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c37e472-2c6c-3ebf-8b8e-1ba542c50945 | -14.89901 | -52.61905 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee479f4a-d688-3f2a-a136-4b1e1d1782d7 | -23.15176 | -48.67022 | 2026-08-29 04:55:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8b3952a5-6260-3047-8d20-2bb405d23995 | -23.58156 | -47.28474 | 2026-08-29 04:55:00 | NOAA-20 | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 055b3766-7994-3a92-a773-bfc9f5865cc9 | -19.22748 | -57.66135 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3758b32e-1296-38ae-a7b6-d3f9566c835c | -14.76298 | -48.75298 | 2026-08-29 04:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 692fc14b-57bc-3af7-ac15-fc690e96b4cf | -14.75984 | -48.74741 | 2026-08-29 04:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00d2ac9f-a981-32ba-935d-49173b861209 | -15.64672 | -45.9306 | 2026-08-29 04:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cc10e8b1-b0d3-31f0-a66b-4e160c38bf2e | -14.44535 | -52.61118 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a522700f-5e89-3d60-884e-2a1aae3d274b | -19.22188 | -57.67057 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f4080e52-c7bb-3871-8b9c-0e0d8c3a8082 | -15.37106 | -52.68138 | 2026-08-29 04:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| adb278f6-5f4a-3e76-b5a1-ed60cec05ef2 | -14.19941 | -52.85892 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b26cc5c4-7a2b-31bd-951e-f093c4273839 | -16.17944 | -45.63856 | 2026-08-29 04:55:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb57be53-e913-3cf8-9ddd-528c4ea490ef | -23.15227 | -48.66567 | 2026-08-29 04:55:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1bfbeb81-c745-3f6e-8164-79d11f81d8a7 | -14.46534 | -58.52679 | 2026-08-29 04:55:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14ec6fa8-643a-3e0a-a389-d4a629aaf9e9 | -15.10535 | -48.15558 | 2026-08-29 04:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9903fab7-d6e8-3f6f-9cae-d417ec7d360f | -14.40756 | -52.57228 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c1d0599-ea87-3eed-b1f0-8be2f62350c7 | -23.62346 | -53.20517 | 2026-08-29 04:55:00 | NOAA-20 | MARIA HELENA | PARANÁ | Brasil | 4114708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e899e4a1-da2a-3e0c-b847-a1748abc00d9 | -20.95503 | -57.58044 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 3cff14b8-5e64-3d1c-8de6-b20a23ce0b28 | -14.41605 | -52.58081 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4612e4a8-f888-305f-accd-63966c7b25ed | -14.91769 | -56.33395 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff80c66a-0dc4-3a0e-a5a0-ebf77c87c886 | -13.86738 | -54.12326 | 2026-08-29 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7255edd7-530b-3b69-b2e8-bce4413a5337 | -14.40368 | -52.57531 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f38a8c63-830a-3383-b7c9-3297b25f8e9b | -14.4048 | -52.56816 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 176acb02-15a5-3dbb-929f-b2e949bf0123 | -13.74054 | -52.03514 | 2026-08-29 04:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c692f28-70c6-3b09-8ee4-b599523e93d7 | -14.93275 | -56.33239 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 827cac8e-36d6-35b7-9475-6b993fc81dc4 | -14.19279 | -52.85783 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa8877af-71c6-3553-baf6-20c3c4f808b4 | -23.1503 | -48.67233 | 2026-08-29 04:55:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4931008f-ac55-3d52-9b23-f9967159c24c | -14.17873 | -48.75997 | 2026-08-29 04:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b11e9af1-702d-37c3-8037-0a9546d97628 | -14.92127 | -56.33462 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f96096e1-22f6-340c-a878-2e5c0df861e2 | -20.93606 | -57.56345 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| a4252357-d39d-39a2-b8ad-6a0f34443bc1 | -22.25595 | -47.52511 | 2026-08-29 04:55:00 | NOAA-20 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f13c2e46-b0f6-3d44-beac-007b9df1fb29 | -14.90786 | -52.62785 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58cde730-555f-3e7b-98ad-a164b2ed089c | -22.31014 | -51.88766 | 2026-08-29 04:55:00 | NOAA-20 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5bc90c88-0b71-37ae-97bd-b90bb10d9ca3 | -15.64265 | -45.92509 | 2026-08-29 04:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cc24ac56-aab5-3150-87a2-68dd1eb20cc3 | -15.56261 | -49.95529 | 2026-08-29 04:55:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78686c43-0ee1-3103-a759-1d46e503ccbb | -14.27373 | -57.03761 | 2026-08-29 04:55:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05fb85b4-793f-3e35-b631-e8b61dc07db6 | -20.93736 | -57.5769 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 94985123-fb6a-3b16-aced-069fd0f8a763 | -14.76368 | -48.74804 | 2026-08-29 04:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df00348e-4413-3c74-9c87-99b121dfa1db | -14.16027 | -52.82695 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11b9883a-3aa8-380d-a0ec-cb598a8e9cff | -21.52991 | -48.62575 | 2026-08-29 04:55:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ce2e7ee-e9f8-3208-a9d1-a56bf29c2dde | -15.27196 | -53.16373 | 2026-08-29 04:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f73edf18-7f3b-3ac7-a64c-6c95eaddfbe1 | -14.17515 | -52.84034 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f528a149-7a61-3b04-9d3b-488545835ba8 | -19.22315 | -57.66458 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d287c36e-82c0-3cdc-addb-bfb251a2789a | -15.12394 | -53.58172 | 2026-08-29 04:55:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 76c67d03-feec-39c6-bac7-fc9fd294fc8c | -23.15882 | -49.24007 | 2026-08-29 04:55:00 | NOAA-20 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 764f9058-d733-31f6-86d8-642b3eac38b7 | -14.47419 | -58.52456 | 2026-08-29 04:55:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa88ddb3-aab7-3be4-9e14-0ec2369790da | -14.9217 | -52.62647 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 834a2621-6575-3116-a318-9f593536fd89 | -23.07675 | -48.62223 | 2026-08-29 04:55:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce5aaa6e-b02a-3899-977f-3d932a968600 | -19.22465 | -57.65626 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| dc60d73d-7ba7-34c8-b975-5a2a51ae0629 | -19.22597 | -57.66977 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2ea54988-cb91-3d9f-9c75-3170f881e503 | -14.41274 | -52.58027 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bac029c1-9598-3069-aba5-805c9985675c | -21.90051 | -55.36866 | 2026-08-29 04:55:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92fc379f-8301-3561-8a42-b91ec76d4816 | -14.40793 | -50.0484 | 2026-08-29 04:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dc504345-dfa2-37eb-ad9c-bdb4338f97ec | -14.20276 | -52.83763 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cc4e5bf-1ee5-3410-9ea2-64a76e62bd92 | -22.31217 | -51.88546 | 2026-08-29 04:55:00 | NOAA-20 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4fa2f882-afc3-3688-a652-672f13c2071f | -19.22261 | -57.66639 | 2026-08-29 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bf2e56a4-f60f-3d6b-a423-5a326710359f | -14.91842 | -56.32972 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8aa40d2-1133-3fdb-89fc-c9a2763e38e1 | -26.57281 | -51.509 | 2026-08-29 04:55:00 | NOAA-20 | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6923ecca-8a88-3fb6-9a0e-772f2793d044 | -20.95651 | -57.57194 | 2026-08-29 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| d134f76b-2dc3-3951-852c-9aeb551f244c | -14.8996 | -47.74085 | 2026-08-29 04:55:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bcbc22dc-8381-3060-bf52-989ac9bff0c9 | -14.91229 | -52.62126 | 2026-08-29 04:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d3495b9-6c30-3dbf-ac32-73a11d1b7f7f | -23.1474 | -48.66987 | 2026-08-29 04:55:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 92e361ea-df8f-3ca2-a7bd-2afc35699ce3 | -15.65084 | -45.93578 | 2026-08-29 04:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 038bcc6f-c44b-3283-b982-f2567567d8d8 | -14.90776 | -56.3059 | 2026-08-29 04:55:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d898657-c3d5-3e6b-9355-ec3085e8d549 | -15.1212 | -53.57759 | 2026-08-29 04:55:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 00dba8a9-f0f7-348f-a81a-3f619143462a | -6.7884 | -55.6635 | 2026-08-29 05:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 87ab5546-3e6a-31ef-8493-18e71206378c | -6.7699 | -55.6644 | 2026-08-29 05:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| cbfa30d3-3de2-3c32-8c92-8ea5939412eb | -6.77 | -55.6445 | 2026-08-29 05:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| dd5c64a4-ed27-3a05-be9a-29c2dd686234 | -10.4794 | -64.5012 | 2026-08-29 05:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 8b23c883-ae4f-3346-bc93-6a619418d28e | -5.8894 | -57.7708 | 2026-08-29 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 18b0d5b6-e445-3f2f-bded-411b4f902e3d | -6.6129 | -43.7317 | 2026-08-29 05:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| ea6cb410-7f09-3878-99a7-f22b327737f5 | -7.5137 | -55.3051 | 2026-08-29 05:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 7133d289-33d8-3de6-907e-c7b6008e32e0 | -5.8895 | -57.7513 | 2026-08-29 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| affa73e1-e426-3696-874b-15df01d1727e | -7.5139 | -55.2851 | 2026-08-29 05:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 43614b9b-5ddb-3563-836c-ad76c2ee126e | -6.6315 | -43.7533 | 2026-08-29 05:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| e5b2dd19-3165-321c-8a77-3657d4f5c4c3 | -5.9079 | -57.7506 | 2026-08-29 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| cd2f1950-cc9c-3e9e-bb25-bc6898b94ea1 | -6.6317 | -43.73 | 2026-08-29 05:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 7990f5d5-eb67-333b-82b4-0edc2e0d2e61 | -10.4795 | -64.4824 | 2026-08-29 05:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 0e4bda9a-531a-374d-8561-c61c92e8388a | -7.5137 | -55.3051 | 2026-08-29 05:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 1db43053-afbf-3d9d-844a-d9955b239df5 | -5.8894 | -57.7708 | 2026-08-29 05:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| a296aec4-7919-3e57-9370-3d81230203ed | -5.8895 | -57.7513 | 2026-08-29 05:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| eed9657f-05ee-3116-8648-9a698c3757ca | -6.6315 | -43.7533 | 2026-08-29 05:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 46c1e70b-b737-324d-b7dd-574c4d0f1348 | -10.4794 | -64.5012 | 2026-08-29 05:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ebf31012-1234-3198-bd8d-ebd58f1e80ea | -6.7884 | -55.6635 | 2026-08-29 05:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| b3d45a0a-db2a-31e3-abd1-4f1b6fbd6456 | -6.7699 | -55.6644 | 2026-08-29 05:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 1118fe78-cf87-39f9-95d2-3b62a0102e6b | -6.6317 | -43.73 | 2026-08-29 05:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 4e678f66-f400-3760-9391-4062324be169 | -6.6317 | -43.73 | 2026-08-29 05:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 49ffc028-c346-3ffa-a605-169c264773aa | -6.7699 | -55.6644 | 2026-08-29 05:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| af42264b-3cf6-37dc-8098-d5d978221af2 | -10.4794 | -64.5012 | 2026-08-29 05:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| ebb8b2dd-4c09-39fc-84e9-4a0a695680be | -6.7884 | -55.6635 | 2026-08-29 05:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| b21fe7aa-bac7-3d7b-9f5d-633b90ceb7a3 | -5.8894 | -57.7708 | 2026-08-29 05:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 355b2827-de62-3569-bda7-cfb958ceb758 | -7.5137 | -55.3051 | 2026-08-29 05:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 5abd5e19-ab16-36ef-b9c3-2782654114ba | -5.8895 | -57.7513 | 2026-08-29 05:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 80725905-e34e-31d1-aa71-63f68032b005 | -6.6315 | -43.7533 | 2026-08-29 05:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| e7f25965-706b-3d57-8580-c50c137b5f7b | -6.6317 | -43.73 | 2026-08-29 05:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| eb5da9a2-0c27-306a-8ace-161cb3d2957c | -5.8894 | -57.7708 | 2026-08-29 05:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |


[Clique aqui para ver as próximas entradas](README58.md)
