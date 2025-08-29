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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e5331b7-b169-332b-b27a-0105222cb3a9 | -16.07948 | -43.62214 | 2025-08-29 04:42:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6aac01e-533f-3a49-b4b1-befb12f718b5 | -12.99608 | -56.91649 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 345cc8b4-e834-383c-855a-960f85fcb4e6 | -19.90792 | -43.83931 | 2025-08-29 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| df24389f-ea9f-35e9-b76b-a549c89b8ccd | -15.19548 | -52.3401 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1f28128-3f8f-3334-9711-68ca738a820f | -15.21755 | -53.79822 | 2025-08-29 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 026d1c28-d936-394c-b962-85f7c6f10a20 | -14.90496 | -46.45571 | 2025-08-29 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25db8a8d-87e7-3e58-90f4-62791d0422d7 | -16.5098 | -45.10548 | 2025-08-29 04:42:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19b39677-5e29-39dd-9e28-813c0cbf715c | -14.31854 | -53.04607 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93bf9dd7-b2dc-3e4d-a2e9-300db734b362 | -13.59225 | -48.23568 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b028fc0a-2d7b-3c98-a688-f63169e95d4e | -12.93399 | -56.96968 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bd8eb0dc-46ed-30ca-83fa-26f4bba9c930 | -13.40705 | -46.964 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9014844a-3841-3177-b9ff-391e0a9992fe | -10.2926 | -64.48935 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bbc7b77f-20d0-317f-9d5d-422ee5d2049c | -15.82761 | -45.77016 | 2025-08-29 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1116097e-e1cb-3e3f-9869-a32445bca381 | -13.00376 | -56.92187 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da8d9e2b-ae50-3d63-bed7-92fc1a75359f | -15.17342 | -52.32893 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7668a428-9680-389e-bd1a-7f6438c572c1 | -15.53918 | -54.27036 | 2025-08-29 04:42:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdce2ebe-e1ad-312c-b790-dba94909f7d0 | -13.36871 | -46.87331 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72117f30-1483-34e0-bfe9-049826fa63af | -11.70417 | -60.19444 | 2025-08-29 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 527c5c62-e76b-328b-a479-63d117edbb02 | -14.50956 | -52.0746 | 2025-08-29 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e71cd53-4914-3822-adf4-e1c3730724db | -15.18884 | -52.339 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8eef223-0eb8-320c-a86c-284f42caf411 | -17.75784 | -44.50306 | 2025-08-29 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78adbeb3-5f28-39bc-9635-a668bf9ffd32 | -15.04363 | -48.12328 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2aba8535-9227-36d9-95c1-56c1b0620ef3 | -14.77899 | -59.73524 | 2025-08-29 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8c8411f5-069e-36e4-8f55-e0c7a4bc0210 | -13.00936 | -56.91478 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba4a9e58-a038-31d2-ab6d-3cee4539e675 | -13.47459 | -46.84469 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f868993d-ff6c-3449-a08c-c0b7c2fe0af7 | -13.53924 | -46.8745 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 272e9e86-b9ea-3694-b473-c654c2f4b060 | -15.07371 | -48.63201 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d652d88-4543-3d72-a26f-07ba48c22586 | -13.23186 | -57.13116 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3634729b-37fb-339f-9923-421d18d54860 | -14.24503 | -48.06574 | 2025-08-29 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9917a2c-8747-3aad-93f2-dacc937b4224 | -13.00027 | -56.91722 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5aa1da94-7e42-3a53-997f-14cbf51e9107 | -15.17731 | -52.3259 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bc4b431-26a7-3051-b0c8-f2746cf84334 | -13.50336 | -46.85007 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0c934542-4ffa-3d67-a468-acfa4910b48f | -15.04913 | -48.13731 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abe90c2e-26d2-3004-bd11-075526bb5207 | -18.16093 | -44.41986 | 2025-08-29 04:42:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ba0ff29-9899-398b-afe0-2fca2e3bfad7 | -15.21475 | -53.79376 | 2025-08-29 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebb18468-4d28-3247-9a0a-cc5576a02179 | -13.59066 | -46.87175 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ffcb7918-611a-3a51-bc61-a2c0a6f2bbac | -14.47241 | -48.44227 | 2025-08-29 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5330873-03aa-35df-be71-86226d38b6b0 | -15.30316 | -52.81101 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3687f8c3-6086-399c-8b94-36c76cc91ae3 | -13.23113 | -57.13523 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23108705-7831-38c6-b02a-d419e30ac2c5 | -15.05997 | -48.63152 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c59e236e-d0f8-3892-9cfb-c945d64eb23e | -14.79105 | -59.7252 | 2025-08-29 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 73924862-2a5d-3385-a3b5-5f933b910488 | -16.2878 | -53.62073 | 2025-08-29 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 113d004c-1e27-3ab1-a3d5-1c97042f6d05 | -13.57774 | -46.86728 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 99066b9b-abe3-3d8e-9ee5-2132f6461168 | -13.683 | -46.90109 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a7384e7-99fc-309c-8c90-93b8f562c1f6 | -13.81948 | -52.74521 | 2025-08-29 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9e47a5c-d973-326c-ae5a-5c3c731b7ec0 | -13.63601 | -48.2031 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f39c36c7-1d00-3786-8e5c-9a7ad051d419 | -16.28441 | -53.62015 | 2025-08-29 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 828c0dca-f4c3-376c-8dbd-2e2d4dcb5e22 | -13.54886 | -46.94587 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 410af121-8f8c-3647-a187-59b563f97ab2 | -12.42682 | -63.91176 | 2025-08-29 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9394e9cb-14af-3b7d-abf6-a787575c25b3 | -13.62948 | -48.24908 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c64daf8f-4e39-355e-85cd-e60c1e6d1c50 | -13.5047 | -46.84026 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 89481c1d-c112-38c6-b0f5-11cfb8b884f0 | -15.08499 | -48.62947 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8cc61190-6f01-3320-9350-47e88302e9e8 | -13.54111 | -46.94537 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40764385-a8fb-357f-b18e-cdefe9761e44 | -13.62529 | -48.20132 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 443d7893-4507-35d1-a46c-08a9cb279052 | -17.49913 | -45.17494 | 2025-08-29 04:42:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8771208b-213b-3889-a11b-a9d9146b7c0e | -12.63038 | -60.25212 | 2025-08-29 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58178c9d-ec15-3c82-a5da-86267c3168fe | -13.49243 | -46.84393 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 505e7366-0db7-35d7-abee-060aaee18f1a | -14.33431 | -48.65069 | 2025-08-29 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e132413-48f9-3a03-b44c-57746e9463ad | -14.32712 | -51.9378 | 2025-08-29 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c91b6799-5b37-3491-a6f7-85424c3e5380 | -14.31732 | -51.89235 | 2025-08-29 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48d576fc-5e0e-3904-bbe0-87de77bf1933 | -14.90545 | -46.45209 | 2025-08-29 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80979d43-3318-37d6-8381-747ced905012 | -17.37491 | -47.01498 | 2025-08-29 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07e8f46a-9262-33a5-8471-90db68223d35 | -13.55032 | -46.93543 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c69f78d7-00cb-3001-a3a5-1ba9df2c1c46 | -12.99397 | -56.92815 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50b295d1-cb65-3b5f-b30b-b25767271e1a | -13.35732 | -54.38667 | 2025-08-29 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae5ddc04-967c-3a2b-a166-8b5c7d34a016 | -16.28165 | -53.61579 | 2025-08-29 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4c5f520-d5b7-338e-b2e2-8816cd4115d9 | -15.67404 | -52.75095 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6504d6f-d5d9-33d9-bd98-de5c18e7c70a | -13.3482 | -51.78226 | 2025-08-29 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 528f99a3-e546-3096-be2e-4f03d3094439 | -13.42548 | -46.97141 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a999b357-c59d-32db-ae72-557386277f1c | -17.75754 | -44.49793 | 2025-08-29 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47629c80-8460-3957-84de-01a47caf25d1 | -13.5104 | -46.94158 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9309481-10fd-33c8-9243-56ce79a41306 | -15.21819 | -53.79435 | 2025-08-29 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d100552-cfa7-3cdd-b0d6-aa5e51f64c7c | -13.53989 | -46.86982 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 61e000f9-6f18-378b-93f9-db4d3984fa5e | -12.99957 | -56.92112 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d1f78157-c4e8-3fa4-a0c9-64770c0b5705 | -18.20002 | -45.59536 | 2025-08-29 04:42:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f084a2a9-0a84-3996-8855-7f9cc0d30d36 | -13.40332 | -46.99067 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 21e124db-7725-3559-872f-aaccf45f07b9 | -14.34136 | -48.65194 | 2025-08-29 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e9a351c-6422-34db-b561-2521f93e335e | -15.04728 | -48.12379 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2a4733d-f878-3502-88bc-3da71adab4fa | -14.52598 | -53.0043 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37c8e898-28fa-3ab5-ac90-cf35f9bbafd1 | -16.28566 | -53.6126 | 2025-08-29 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a87c1955-952f-3a62-875b-e2010819354c | -15.83937 | -50.58067 | 2025-08-29 04:42:00 | NOAA-21 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d2c4e9f7-2832-3557-b21f-faba0344d563 | -12.51953 | -53.81596 | 2025-08-29 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 161abfc3-114c-3f57-a2d2-af79eacd1b70 | -12.93747 | -56.97451 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 330e1e7a-865c-3924-a72c-4fb4771094a3 | -13.34489 | -51.78171 | 2025-08-29 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c687ac6a-b7de-34f8-b6c5-e8eb32177b73 | -15.04302 | -48.12766 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67a7e0ce-5b87-3d2f-a0de-d8dc1d74d767 | -15.3243 | -48.22367 | 2025-08-29 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 216f3bfb-8907-338f-a5f6-21e2720d7bf6 | -13.54311 | -46.8749 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1e68aca3-440d-3d8d-81f8-a3ea01f99777 | -13.01424 | -56.91163 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a57f6ee-32a8-311a-8098-d1594c806d84 | -13.59314 | -46.8695 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f8dd3c2-e44b-3c25-837b-523536c6e3b0 | -13.53475 | -46.87854 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9db2f3f7-7b53-3aa1-a126-84b69753b1f7 | -13.01006 | -56.91086 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bdf0eba-8c48-341a-a618-0e4cb5cf699d | -13.37187 | -46.87886 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d80e7e3-db62-3028-9026-4859007b5fa2 | -16.28843 | -53.61696 | 2025-08-29 04:42:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac9746cf-e40d-34d8-bba9-3c38320a5721 | -12.93327 | -56.97372 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bf6aed74-998d-33ca-ab00-440f279c3c3a | -13.59602 | -48.15942 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0edf4db5-8313-359e-8350-3e0c488e9543 | -13.54245 | -46.87962 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a40f2d4d-c262-3837-93db-7d4b67cb6589 | -13.60379 | -48.1564 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 359b7c7b-493d-365e-8189-97ff62b4ec06 | -13.81035 | -52.75882 | 2025-08-29 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baad75bd-61bc-307e-8758-32991a8a41ee | -14.36181 | -53.23374 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97e09bd4-6f61-3797-8b42-424680168685 | -13.63195 | -48.12796 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README57.md)
