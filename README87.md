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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93cbfbe0-59bd-3d9d-8835-3b741cb67caf | -14.89713 | -48.15653 | 2026-09-18 05:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f539741-ecd8-3df3-ac22-d22e624bb121 | -14.80379 | -48.54778 | 2026-09-18 05:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb2c62c2-6785-3caa-81c6-fb8e2bca459a | -14.89763 | -48.15176 | 2026-09-18 05:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 256ce8f4-6d03-3ef7-965d-058581300243 | -15.4683 | -52.87711 | 2026-09-18 05:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| db9efb5c-0e6c-33a8-aa02-0155ca863e82 | -14.89112 | -48.15505 | 2026-09-18 05:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b789600-927c-3e4b-8587-4f2465aba617 | -16.79596 | -49.10061 | 2026-09-18 05:21:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f6cde28-05d4-37c2-b398-e00ea2512d9e | -14.80873 | -48.55746 | 2026-09-18 05:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf730372-6533-36f3-8a05-3688f1bb8a53 | -19.18825 | -48.79795 | 2026-09-18 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 235af275-f0eb-36fc-8b89-7d6e4b04c668 | -15.46891 | -52.87239 | 2026-09-18 05:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 5bb13147-1f43-39cd-882f-73fd7d11002c | -15.46169 | -52.85728 | 2026-09-18 05:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1144b8a3-f1ef-3e47-b4a3-13e3835c43fe | -19.18256 | -48.7923 | 2026-09-18 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 753ba076-84ed-3b51-b505-d36d62e5b4ac | -21.45954 | -48.68286 | 2026-09-18 05:21:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46ae660e-51a7-3132-abfd-30d7045345d9 | -14.89043 | -48.15526 | 2026-09-18 05:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9ed9d18-ae0a-367a-86ca-56d3ac90a807 | -19.55549 | -47.63906 | 2026-09-18 05:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1e17d72f-2065-3dcd-83a7-ec08902734f5 | -21.45996 | -48.67763 | 2026-09-18 05:21:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6aa9ce23-26dd-3f69-9223-c8720c0d3ce0 | -14.94335 | -49.9193 | 2026-09-18 05:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f786d905-97f1-3239-8e88-8df223084183 | -19.55407 | -47.63057 | 2026-09-18 05:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ca584de7-1a07-354b-9dd4-3cddfbe512b2 | -21.45691 | -48.68047 | 2026-09-18 05:21:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e7535d1-6349-338f-aa67-b9247a6903a9 | -12.14278 | -64.14227 | 2026-09-18 05:21:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00a3ffea-d204-387c-82db-b2ea29bd1c29 | -19.55495 | -47.64522 | 2026-09-18 05:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b72efdab-686d-3ead-b4e9-b503de16bc30 | -18.02376 | -50.94484 | 2026-09-18 05:21:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b5049308-cc8d-316a-b912-84d3997dbead | -19.18303 | -48.78731 | 2026-09-18 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e39cf3de-6913-3c42-8ca5-61960b49d862 | -15.46619 | -52.85785 | 2026-09-18 05:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5af35bf3-d854-327f-a342-194556f11585 | -20.09789 | -57.21122 | 2026-09-18 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 347af4b5-b919-3d86-aab9-59d81208d5e6 | -14.80269 | -48.55768 | 2026-09-18 05:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 08aca23c-0d32-3496-82e2-64deba855cd5 | -17.77482 | -46.48352 | 2026-09-18 05:21:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 191da8c7-5f40-340c-bc80-f6c26f82fa4b | -14.89698 | -48.15196 | 2026-09-18 05:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f8eed6e0-569e-316e-bb0b-38b923a371af | -19.18394 | -48.77749 | 2026-09-18 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfee79d0-f1f2-3825-9060-cd0db4827748 | -21.45647 | -48.68559 | 2026-09-18 05:21:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5c8b307-a18d-3845-9516-794bc2aaa856 | -14.80318 | -48.55327 | 2026-09-18 05:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d646ac00-2ac3-3bac-94d8-b1258a75a596 | -12.14286 | -64.14275 | 2026-09-18 05:21:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70ce2327-b10f-383e-8278-866aa55ef128 | -14.80222 | -48.56187 | 2026-09-18 05:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34be7f3d-2942-38ed-a791-0c9a360c11c8 | -18.02338 | -50.94833 | 2026-09-18 05:21:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 53222c43-8add-3a42-9391-b67a8d5394ad | -19.54989 | -47.62708 | 2026-09-18 05:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7d4d75a4-01d6-38e3-aa7c-eef12dc39b31 | -19.17779 | -48.77674 | 2026-09-18 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1d55d19c-e4de-33f1-8006-b77df0d1e6a7 | -14.8018 | -48.56564 | 2026-09-18 05:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5b95fd40-3bf7-3418-ab45-3a64a443d066 | -20.09861 | -57.2093 | 2026-09-18 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dfa4b666-e6d9-3956-9b59-3cc792f599ef | -19.17689 | -48.78647 | 2026-09-18 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d6c3c281-cd05-311a-86e6-7e9a2a6868c5 | -14.96162 | -47.53961 | 2026-09-18 05:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc4224f4-e5b8-3e8a-a96f-b0eeeb5005ac | -16.79548 | -49.10498 | 2026-09-18 05:21:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc099054-ecb2-38e9-a35b-67ad5bd8a54f | -15.85581 | -57.57005 | 2026-09-18 05:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8529c1cc-1559-3e3f-a4c4-b48dbb29c8d6 | -19.55603 | -47.63306 | 2026-09-18 05:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5623af99-4889-31e4-8d38-d4a70128db08 | -18.02414 | -50.9414 | 2026-09-18 05:21:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 577fc49a-b047-3039-9fd6-4eb2538c1de9 | -19.18441 | -48.77242 | 2026-09-18 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27eeef7f-8d25-3d27-bbb0-6c3deedaad4a | -19.17734 | -48.78161 | 2026-09-18 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7b3e924e-470f-3d7f-a29b-a4a50a185887 | -17.76861 | -46.48314 | 2026-09-18 05:21:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a77f770-b132-3537-b06b-cd4c9465992d | -15.4734 | -52.87299 | 2026-09-18 05:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d718225-739a-390a-8f49-25d7fdfe152c | -19.1901 | -48.77813 | 2026-09-18 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02bef58e-24ae-31a6-b0e0-f90815f905e8 | -19.55358 | -47.63655 | 2026-09-18 05:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 76deaa45-c41c-357e-9846-146c8be1398d | -19.18348 | -48.78242 | 2026-09-18 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| eec64d91-b031-3e01-b1ec-4ee27c7134ae | -15.85926 | -57.57059 | 2026-09-18 05:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f6cd6b6-c25b-3c46-805e-a0c8fa2f1458 | -22.24447 | -52.88849 | 2026-09-18 05:23:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 09f8bf37-9519-3546-bf35-eab98fdfed09 | -28.3502 | -52.1841 | 2026-09-18 05:23:00 | NOAA-20 | MARAU | RIO GRANDE DO SUL | Brasil | 4311809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3e6c5b2b-c63d-3fc2-a0c4-4a01538302c3 | -28.3503 | -52.1847 | 2026-09-18 05:23:00 | NOAA-20 | MARAU | RIO GRANDE DO SUL | Brasil | 4311809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7da3dcc0-8db5-3244-852f-8d0e6375cab2 | -22.24276 | -52.88902 | 2026-09-18 05:23:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ae637015-3b68-330a-8621-a37b7df08364 | -28.34469 | -52.18336 | 2026-09-18 05:23:00 | NOAA-20 | MARAU | RIO GRANDE DO SUL | Brasil | 4311809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a52bab77-a84c-3d38-95a7-38dc884b0cbc | -28.3448 | -52.18399 | 2026-09-18 05:23:00 | NOAA-20 | MARAU | RIO GRANDE DO SUL | Brasil | 4311809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7c5f1d4f-62c7-358c-9918-389557fbf406 | -3.13409 | -59.02131 | 2026-09-18 05:59:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4397ae9c-fd7d-3d44-aa18-a9b6dac4db2f | -3.13347 | -59.02543 | 2026-09-18 05:59:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a019fd43-ecad-3f8a-bd14-0e0c1fa921b8 | -8.901 | -62.40304 | 2026-09-18 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8548e53a-2858-3860-a6ec-7e80b4af90f6 | -8.90059 | -62.406 | 2026-09-18 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fde3bee4-0b4c-3986-b287-5ad1fbecdf8c | -3.70484 | -60.63085 | 2026-09-18 06:01:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71e6c7db-45b3-3446-92cc-3341e3083e03 | -3.70437 | -60.63412 | 2026-09-18 06:01:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 446c8428-f599-3e3d-913f-3ebcd9e054e4 | -3.73128 | -60.59777 | 2026-09-18 06:01:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f21be953-7bc1-38ea-8e34-e9d290ef6186 | -4.79893 | -56.11519 | 2026-09-18 06:01:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 881f1a3b-73a2-3c89-a891-ea04d69eab4d | -8.90514 | -62.40232 | 2026-09-18 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f3097d47-96ff-3965-8937-cd035b9229e6 | -8.90476 | -62.4053 | 2026-09-18 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bc0c956a-b333-32d8-bb9a-73fb659d3af4 | -3.81586 | -58.89378 | 2026-09-18 06:01:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 957270df-227f-3bfb-8bd8-1d8cb67e96d5 | -8.8997 | -62.40454 | 2026-09-18 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b27631e6-dd35-32cf-85a9-795737167dc1 | -3.69956 | -60.63005 | 2026-09-18 06:01:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60e3294f-beec-3fd6-8a59-245ecb86f812 | -4.79786 | -56.12291 | 2026-09-18 06:01:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 035dd862-cf45-348a-9217-d3ab688765ab | -3.80932 | -58.89723 | 2026-09-18 06:01:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0ce6455-6599-3b60-98b8-6a571e45dc33 | -6.9324 | -63.02599 | 2026-09-18 06:01:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 71514049-52c2-3284-afde-1fde95f0ecfb | -8.8922 | -62.4107 | 2026-09-18 06:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| c5907a5f-f0f0-3d5c-a456-b475532a35ef | -8.9107 | -62.41 | 2026-09-18 06:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 205ef904-6df4-34b5-898a-2965799b43c0 | -9.699 | -54.8176 | 2026-09-18 06:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 398563e2-3238-306c-98f8-991cd09f6568 | -9.7177 | -54.8162 | 2026-09-18 06:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 2c85932f-bc4c-3efe-8bc7-aab9cad587c9 | -8.9108 | -62.391 | 2026-09-18 06:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 2b45cacd-76d8-3f8b-80c1-fd81a537217d | -8.8922 | -62.4107 | 2026-09-18 06:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 99.3 |
| e034a3e0-8b90-341a-8000-d9ea67e71a42 | -8.9107 | -62.41 | 2026-09-18 06:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 274326ab-55da-330f-a79b-652f6ff7ca68 | -8.8923 | -62.3917 | 2026-09-18 06:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 24a4f21b-1c38-3967-9245-e3acd17927ef | -8.9108 | -62.391 | 2026-09-18 06:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 09f7a95c-4983-365c-bdb5-858771fda102 | -8.9107 | -62.41 | 2026-09-18 06:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 3f70c75f-be52-3986-b9e0-9a73173b3836 | -8.8923 | -62.3917 | 2026-09-18 06:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 72a7bbc1-1c23-3e5f-823b-4202214f096a | -9.699 | -54.8176 | 2026-09-18 06:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a2d63724-e72e-3428-b2e5-e976da0fb6d3 | -18.0303 | -50.9385 | 2026-09-18 06:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| fc3eb9e6-8cac-3a65-8c6a-08b486784420 | -8.8922 | -62.4107 | 2026-09-18 06:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 9adcd8d0-71f9-36b1-9c75-748c7b42ad89 | -9.7177 | -54.8162 | 2026-09-18 06:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 93567e58-cb5e-3a07-acac-f0a78c8240eb | -2.8131 | -50.482 | 2026-09-18 06:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2358461b-7490-3db6-839a-a96b1dbde132 | -4.57776 | -42.93969 | 2026-09-18 06:44:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| a24770d5-5d3b-324c-a457-acaaca14ed65 | -5.51735 | -43.66526 | 2026-09-18 06:44:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 39f8e96c-91b0-398e-9e7a-a97a7a7072e0 | -2.81708 | -50.45628 | 2026-09-18 06:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| ad4de71d-fbd6-3345-acd1-7cb5658415bc | -2.8236 | -50.48355 | 2026-09-18 06:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 73aa5123-e641-3dcf-9520-ff1bd9301a47 | -3.37436 | -50.43596 | 2026-09-18 06:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 63202911-291f-3c64-bd10-072162d5ef41 | -2.96169 | -50.32885 | 2026-09-18 06:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1409eab9-9c87-3948-9d92-2e383de347f5 | -3.36206 | -50.44684 | 2026-09-18 06:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 7068e3a9-9a4f-3720-895a-93536b6799ad | -4.55502 | -42.94958 | 2026-09-18 06:44:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b2e49330-7f64-39fa-87de-67c2d1680eb4 | -2.96732 | -50.33648 | 2026-09-18 06:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6407ec98-aa7c-3661-b327-ecdf47ac21de | -2.82559 | -50.47062 | 2026-09-18 06:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 214.2 |
| a4e3e4bc-262d-3130-8845-df644c9b03e2 | -3.37243 | -50.44839 | 2026-09-18 06:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |


[Clique aqui para ver as próximas entradas](README88.md)
