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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a78809fe-533e-321a-a4e8-8ac0210e533a | -6.1292 | -57.7223 | 2026-08-09 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 5d55cdd2-bc10-336e-b36c-8cfa409ac229 | -6.1476 | -57.7215 | 2026-08-09 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 549c5494-0048-33a0-86d6-692524a7eb41 | -11.0334 | -44.2696 | 2026-08-09 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 7c083538-6a9f-31d0-bf58-36197c3f411d | -8.6856 | -62.874 | 2026-08-09 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 02cde030-5f8b-3e0d-9817-def80b754d2c | -13.9541 | -58.1162 | 2026-08-09 00:00:00 | GOES-19 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 83432258-16b1-3cb2-99d1-1bb2366bac65 | -20.56955 | -47.16101 | 2026-08-09 00:09:00 | TERRA_M-M | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4829fc6f-9779-3275-876f-adae2ca350cf | -21.74868 | -43.56631 | 2026-08-09 00:09:00 | TERRA_M-M | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 680a184f-fde8-377e-9d1d-e880c1548e4e | -20.3908 | -49.3124 | 2026-08-09 00:09:00 | TERRA_M-M | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 9df696d3-6dc6-3111-bab5-9a7be7e58a6f | -21.74627 | -43.55204 | 2026-08-09 00:09:00 | TERRA_M-M | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 52936cb0-8a2f-3543-aea0-8992b395e5f5 | -21.28172 | -42.93334 | 2026-08-09 00:09:00 | TERRA_M-M | ASTOLFO DUTRA | MINAS GERAIS | Brasil | 3104601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| cc545170-0a5d-307e-a01b-5befd107685c | -21.26354 | -49.58788 | 2026-08-09 00:09:00 | TERRA_M-M | MENDONÇA | SÃO PAULO | Brasil | 3529500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 7dc536a9-921a-34dc-9cb4-0620e894459a | -20.38953 | -49.30286 | 2026-08-09 00:09:00 | TERRA_M-M | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 0b5cc61e-4271-3d51-9642-2451ee04df58 | -21.27255 | -49.58651 | 2026-08-09 00:09:00 | TERRA_M-M | ADOLFO | SÃO PAULO | Brasil | 3500204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| b64a6df5-6264-3fde-b986-2fd1c3454aad | -20.37789 | -42.0031 | 2026-08-09 00:09:00 | TERRA_M-M | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.6 |
| 172e061d-0014-3eba-a0f8-71a5a7e3e2be | -20.57097 | -47.35988 | 2026-08-09 00:09:00 | TERRA_M-M | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 22.7 |
| e81e1c91-ec48-399f-957a-705a7ebb59e4 | -19.58311 | -42.59515 | 2026-08-09 00:09:00 | TERRA_M-M | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 69a554f7-3d65-39f7-8d5f-878a356e4af5 | -19.19194 | -47.20185 | 2026-08-09 00:09:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e1c113b5-259e-366a-872c-fe97489004e1 | -18.96739 | -41.12863 | 2026-08-09 00:09:00 | TERRA_M-M | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| 676f2b43-e507-31e4-92dd-2f0747ba0570 | -18.97326 | -41.12034 | 2026-08-09 00:09:00 | TERRA_M-M | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| 94b809c0-d89e-3b74-88b0-ec437b926dbe | -20.21473 | -42.57748 | 2026-08-09 00:09:00 | TERRA_M-M | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 16368f84-d6e8-3789-8026-1622b8c6ae01 | -19.1814 | -47.19344 | 2026-08-09 00:09:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 484eb024-c895-31a0-88af-453e547c6c1f | -20.57238 | -47.36954 | 2026-08-09 00:09:00 | TERRA_M-M | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 19bf5be9-5d1a-38da-8eab-7aaf494c6641 | -19.94211 | -44.37565 | 2026-08-09 00:09:00 | TERRA_M-M | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 98e8e53f-e244-3f51-9198-fd4479854625 | -22.22625 | -43.04622 | 2026-08-09 00:09:00 | TERRA_M-M | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 34.0 |
| 51553339-4120-37e2-9850-5e91bea120a5 | -16.73236 | -54.77237 | 2026-08-09 00:09:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| f993ffec-2706-393d-af30-1ab78a6f6b2e | -18.42682 | -50.59969 | 2026-08-09 00:09:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 00a20342-c916-3683-9093-6444c0724fee | -18.45263 | -50.51919 | 2026-08-09 00:09:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| e17f8a01-c197-36e6-afe0-71c6f36a1284 | -18.42812 | -50.60963 | 2026-08-09 00:09:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 34.0 |
| 8fcb3521-5ac3-312c-9005-c7a1f9cdb2ad | -16.72834 | -54.76683 | 2026-08-09 00:09:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 083814dc-9ddf-3212-86c2-65685d8c9208 | -18.41899 | -50.61093 | 2026-08-09 00:09:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 5370a0f1-d5ba-34ee-839e-ea6580079f8e | -18.64382 | -49.87291 | 2026-08-09 00:09:00 | TERRA_M-M | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 840cce06-27ed-373d-8cd9-a5fbac5079f3 | -18.42942 | -50.61956 | 2026-08-09 00:09:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 75dcf75f-8bdf-3e61-b54e-485be7936ad1 | -18.41769 | -50.60095 | 2026-08-09 00:09:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7c84ec61-2e04-38e0-8877-749e1f8272d5 | -18.42029 | -50.62088 | 2026-08-09 00:09:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 35.0 |
| c7589388-608a-343a-b595-f8154ca39e37 | -18.63489 | -49.87423 | 2026-08-09 00:09:00 | TERRA_M-M | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 4bd2211d-3821-34d9-8529-b20d86b8f915 | -15.7597 | -47.76294 | 2026-08-09 00:09:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fc23a1fe-501a-3574-96a7-a6b1f71d15cb | -18.42159 | -50.63081 | 2026-08-09 00:09:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 54871f40-5bb7-3ff7-a8c1-0e2f2246b674 | -15.76116 | -47.77287 | 2026-08-09 00:09:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a4d8241e-de9e-3c5d-bfc5-3f0911db4bd7 | -11.0526 | -44.2668 | 2026-08-09 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 92f1aa61-ab3f-3ef9-8637-1e0d764ae806 | -6.1476 | -57.7215 | 2026-08-09 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 77fe6fea-ed79-3f8c-a42f-25a37f4fc19a | -18.6528 | -49.8703 | 2026-08-09 00:10:00 | GOES-19 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.1 |
| 052e6b2f-6366-34af-940a-d7d5885f8add | -11.0334 | -44.2696 | 2026-08-09 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| a43dfe1f-6872-3a40-a380-5286ad5e6091 | -18.4159 | -50.6047 | 2026-08-09 00:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| c39e314f-f3bc-32c9-8700-422616be2b45 | -8.6856 | -62.874 | 2026-08-09 00:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 0125abcf-f1e5-373d-9b72-584f7f9c949f | -18.4359 | -50.601 | 2026-08-09 00:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 97.4 |
| 19b700c4-87ab-362c-89eb-58ecefc02a94 | -4.109 | -49.2807 | 2026-08-09 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 7b0a54d4-b6e4-3723-af64-b349dbf245dc | -6.88048 | -44.93005 | 2026-08-09 00:11:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| ea529f80-f15f-3e7b-8eac-838dc3ee0919 | -13.92918 | -58.14982 | 2026-08-09 00:11:00 | TERRA_M-M | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 24865fa4-0c75-3447-8611-8aabdaecc2dc | -14.0609 | -53.82024 | 2026-08-09 00:11:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e419390a-f200-3e70-afcc-50459a1272bc | -13.52515 | -44.03674 | 2026-08-09 00:11:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| f0707d29-7a98-365b-8870-ee85f7ced49e | -8.15655 | -55.39626 | 2026-08-09 00:11:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 0634c65c-641a-3b0e-bde0-dd93301f797e | -14.09159 | -53.9885 | 2026-08-09 00:11:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9297fee1-ee39-327f-bb0c-3ae0a96bc0f7 | -14.17357 | -53.99879 | 2026-08-09 00:11:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 85b662bd-acc8-3e2b-bb15-55ec8ebc1524 | -7.68803 | -49.5293 | 2026-08-09 00:11:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 93b96be9-a4e2-34c6-9241-7379022539e6 | -13.94294 | -58.15356 | 2026-08-09 00:11:00 | TERRA_M-M | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 5a1ed6d4-14e7-3905-8a2c-4b18468ec7de | -14.08105 | -53.99005 | 2026-08-09 00:11:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ee889c42-dc1e-318e-a59e-50a01f2c0147 | -10.71363 | -49.3469 | 2026-08-09 00:11:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 004117c0-d2fc-3d6b-9fe5-0844f8becabe | -10.87591 | -50.37 | 2026-08-09 00:11:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 35db6185-9e3d-318c-8bba-dbfe435097ef | -7.59715 | -49.53922 | 2026-08-09 00:11:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f8601656-ae46-3683-92fe-f31aaac88262 | -13.93988 | -58.12633 | 2026-08-09 00:11:00 | TERRA_M-M | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 25a3c5a0-9abb-3c6e-ba3d-e4e512d869fc | -13.84645 | -53.71201 | 2026-08-09 00:11:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 44aad278-c02d-3a9a-a355-9491ae219916 | -13.9585 | -58.14647 | 2026-08-09 00:11:00 | TERRA_M-M | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 7eb49b57-508f-3bb5-a6e1-8bf48b874ddf | -7.38191 | -49.65115 | 2026-08-09 00:11:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 97aa61f6-7680-3d0e-a3e4-384c795bc5dd | -12.60963 | -52.4662 | 2026-08-09 00:11:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d5b5b03d-59e5-33af-8ba6-caa1c933448c | -12.32585 | -53.15111 | 2026-08-09 00:11:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| ab16d35a-6056-3ce3-9897-3c0a9cdaa9c1 | -11.0498 | -44.28755 | 2026-08-09 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 9922d0b8-ff6d-3522-990d-98e81ed43737 | -11.05078 | -44.28082 | 2026-08-09 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 833bca19-417d-37df-b239-237d584e2d2e | -6.78074 | -46.48106 | 2026-08-09 00:11:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 8a3bea1d-bc0c-32ca-a89b-e618366b8148 | -12.10917 | -47.21261 | 2026-08-09 00:11:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a23fa778-bfb9-35e4-bea5-ccb9ba3346b9 | -14.9171 | -48.24562 | 2026-08-09 00:11:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4befb56c-ad99-386b-ba86-12b72e795f2f | -11.03728 | -44.28971 | 2026-08-09 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 07c3f5d6-905b-3fd3-9f7e-e378d5ca00e4 | -11.03509 | -44.26378 | 2026-08-09 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| ef4b8692-44ab-3b0f-adb2-632c41d20311 | -12.32792 | -53.14445 | 2026-08-09 00:11:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| aab3bf87-396e-387f-af5a-611358ac353b | -8.15827 | -55.40967 | 2026-08-09 00:11:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c6664196-28f0-3e14-857e-9aff8f31a80e | -6.78025 | -46.47206 | 2026-08-09 00:11:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| d8657be8-c069-35ba-897c-fa9032ff6456 | -14.07132 | -53.81874 | 2026-08-09 00:11:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9fa3f916-86bf-3d17-9ed0-2a3c5129ab77 | -14.92333 | -48.22479 | 2026-08-09 00:11:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 689d18e9-3520-301c-8ad7-1e424c6a2afc | -8.14582 | -55.3976 | 2026-08-09 00:11:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5c047611-be2e-3add-8144-57500bec887a | -9.68335 | -47.84883 | 2026-08-09 00:11:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 35693c13-32c8-3959-88ac-72c4371efb41 | -12.61901 | -52.46492 | 2026-08-09 00:11:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0697fde3-10e5-342e-8a77-73d245a40be1 | -12.35015 | -53.16393 | 2026-08-09 00:11:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| daddbfc6-483d-3d38-a095-e7b7179f0f5c | -11.28581 | -53.94476 | 2026-08-09 00:11:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 90c73a6b-e564-3889-8522-d1ffe4515266 | -13.94099 | -58.12101 | 2026-08-09 00:11:00 | TERRA_M-M | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 29.6 |
| d98f754c-9fd9-3525-af44-1c1d8128848c | -11.198 | -50.50559 | 2026-08-09 00:11:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| acf9e9bf-a7a5-35b6-a9e2-4ea0948d9669 | -9.69314 | -47.84728 | 2026-08-09 00:11:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 60c64f93-c041-3597-87f5-08960b91c1e4 | -13.93937 | -47.37593 | 2026-08-09 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1ac919e0-028e-3246-9136-4d6dbb5de17a | -14.92475 | -48.23456 | 2026-08-09 00:11:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 27.9 |
| c4dd26f1-b835-31fa-b2fc-e848d666850b | -14.0236 | -53.83164 | 2026-08-09 00:11:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b69c49e5-8587-3b14-96e6-aaff01c64ff2 | -8.33216 | -46.38183 | 2026-08-09 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d5860f50-e9cc-389b-9188-a077063de490 | -7.59849 | -49.54883 | 2026-08-09 00:11:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6cc01792-4121-3563-8644-6eefa0c6e27b | -13.94384 | -58.14815 | 2026-08-09 00:11:00 | TERRA_M-M | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 5eca1672-ace2-37ed-b1e0-1695ee504023 | -14.06246 | -53.83329 | 2026-08-09 00:11:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b6f15056-d436-3619-a13b-5c36a6eed6f8 | -12.1272 | -47.19813 | 2026-08-09 00:11:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7ab49bb2-ce85-3a7b-b20b-aa05f55112b6 | -14.05486 | -53.82737 | 2026-08-09 00:11:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 62334cca-74e8-3f4a-8126-8c32cff32e7f | -13.95562 | -58.11937 | 2026-08-09 00:11:00 | TERRA_M-M | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| de48d8ce-2ba7-3bd0-9ded-44188ecd23dd | -11.19677 | -50.49666 | 2026-08-09 00:11:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 772ad3bc-db6d-3d7b-b901-28f8405b480b | -13.97026 | -58.11784 | 2026-08-09 00:11:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 6b09c1bc-39c9-3406-a094-a2da557cf167 | -14.9157 | -48.23597 | 2026-08-09 00:11:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 29.2 |
| be6591b4-6164-39cf-943d-2111b63109fa | -14.08662 | -53.99541 | 2026-08-09 00:11:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f62b97c6-71d9-3970-8b9a-6b1c5f055723 | -11.03425 | -44.2705 | 2026-08-09 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |


[Clique aqui para ver as próximas entradas](README2.md)
