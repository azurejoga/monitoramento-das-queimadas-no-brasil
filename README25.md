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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3eb03029-37c8-3eb6-a1c8-0ff604f97209 | -16.85077 | -50.50847 | 2025-09-25 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0113d68f-53fc-3794-bd04-bbd9ec3722ad | -15.89699 | -59.3455 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 086d00b3-4a2c-38a8-aea7-a3697530267d | -17.96007 | -55.85077 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b1266e0f-cbb7-3343-b28a-831e291c1ea1 | -15.91929 | -59.3466 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3878d8ae-0838-3719-8e69-230090ae3c58 | -20.99951 | -50.00457 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 49bdeb15-d17c-3afe-8624-cfec6567aca7 | -20.08366 | -54.61841 | 2025-09-25 04:36:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b23e12b-eeb6-3a95-9e8b-545569683eae | -17.95873 | -55.85804 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a802eb91-961b-3615-a68c-ba9a42930c3e | -15.83595 | -59.59665 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 654ef017-29fe-3686-8850-8b56500b487f | -15.24625 | -59.44161 | 2025-09-25 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f22c2a61-c7cc-3af5-82a5-d1c86012bd23 | -15.87554 | -59.3448 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3e955a7b-87e4-38e2-b6d3-9743d21ac3cd | -15.8851 | -59.40526 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 878fde17-3beb-3cd9-ad18-ebf9a6e910db | -16.85624 | -50.51675 | 2025-09-25 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 7e62ef7e-4b67-381c-99b2-41e04255d13f | -15.92391 | -59.35042 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aab30d5b-1dbe-3c15-9ffd-804bd5e7251c | -19.21912 | -46.72322 | 2025-09-25 04:36:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2293a220-c50a-3c09-b3fb-470938223626 | -17.93146 | -55.84883 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 30b116dd-e301-3d8f-94b8-d65c5bffb85d | -15.90726 | -59.34811 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| acae562d-e533-3c2e-9546-d1b8852f2a13 | -20.98216 | -50.02877 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.5 |
| fa7cc010-d4c8-39c3-b684-0e22767360fe | -15.8813 | -59.42435 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 73dbfc29-e571-3a08-b840-3be5e003ea1e | -15.9679 | -59.50829 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e8e44677-c1e1-3e65-9262-c0267df8d7fb | -15.76941 | -59.49438 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5c626c56-d044-32db-bbbf-98c40e13bc8d | -16.85737 | -50.50958 | 2025-09-25 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 8a549155-f6a5-33aa-88f3-fb57fd0e75fd | -20.99348 | -50.47433 | 2025-09-25 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 3edceceb-2c05-34cf-bdb4-0c8db0a309ff | -17.94276 | -55.85486 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9ce83d29-a60d-333c-8297-a80433d02084 | -20.9896 | -50.47749 | 2025-09-25 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6f5f0de8-f525-3d25-b4cf-01c1d9ce0c7c | -17.93877 | -55.85406 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| af850c0b-0ff9-3452-88dc-1bd6e541c985 | -20.39507 | -51.33603 | 2025-09-25 04:36:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 37bd03b9-559e-34d2-86fa-a9b805a4754b | -15.97315 | -59.50932 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 77df0475-bb62-3b94-8cf8-c5bb3c814a7f | -15.96859 | -59.50486 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9493bed8-d0a2-3b22-b9dc-5d6be853348c | -15.80821 | -59.49003 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b2cec7d5-5709-3481-8e51-468fbaa1b5f6 | -15.89095 | -59.40308 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7c7ea684-19a7-351e-bb03-495e7fa1b75f | -17.23124 | -52.40539 | 2025-09-25 04:36:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b84ceb6b-733a-38cd-80b5-bdc8daf2c878 | -17.9594 | -55.8544 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 11d0524d-11ba-322b-9ed7-f960a33f87a4 | -15.88601 | -59.34643 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d7040d43-0179-3271-824e-a1f2dbd0be9d | -20.98664 | -50.02177 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c4a9485e-b982-37cd-9672-195e77f6cd01 | -20.99292 | -50.47805 | 2025-09-25 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 401346fd-3490-3b8e-84b9-17f662e9122f | -20.97993 | -50.0206 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| 47989fec-449c-3df1-bfde-b09d37c6ba49 | -18.43185 | -47.35293 | 2025-09-25 04:36:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3169f76-de34-3b84-b7b4-4de2a028ed7a | -17.94074 | -55.8658 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.4 |
| 48bc155d-ec62-3d9b-b8b5-77338378fcd0 | -21.0174 | -50.02311 | 2025-09-25 04:36:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8e190bbc-e1f9-39a0-9cce-64813fd27b2e | -17.93742 | -55.86135 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.4 |
| cc261d94-2b38-3437-820f-4cf532798c22 | -15.35366 | -59.1794 | 2025-09-25 04:36:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c86b95f5-e183-3c3a-aaef-0fb05ee03cd5 | -20.99128 | -50.4663 | 2025-09-25 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4c4d8bfb-819d-3dc5-b1ba-a81a51fdfc8f | -15.82861 | -59.6058 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 740a6ce8-ccba-36a5-9110-420ad390c46e | -17.94209 | -55.8585 | 2025-09-25 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 3584679d-7693-3c2f-9137-9787e3368de4 | -15.88194 | -59.42115 | 2025-09-25 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3dfea27d-205b-3211-9c66-b6fb51bc6011 | -23.68697 | -55.25945 | 2025-09-25 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0a33d793-6eba-3432-b3b1-04cb819be343 | -21.97143 | -49.51083 | 2025-09-25 04:38:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| ad09c069-47cf-3c87-8ecc-a11d94d90275 | -22.60819 | -49.02136 | 2025-09-25 04:38:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc8e3c7c-ce76-3c81-9ec5-ecdc5352c221 | -22.36444 | -49.4767 | 2025-09-25 04:38:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c25a3ad-94e7-38b5-9fab-7f6ea4c56931 | -21.97543 | -49.50744 | 2025-09-25 04:38:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 7b468e82-c39f-3f19-8d3b-b9f79ae4b209 | -25.32931 | -51.47996 | 2025-09-25 04:38:00 | NOAA-21 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 629c22f4-d358-3716-9302-28d36094abf1 | -20.80095 | -56.95458 | 2025-09-25 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1cceb43-0af0-3a75-9608-3dc4ee10dd4c | -20.73958 | -57.86087 | 2025-09-25 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ae11dd4f-c66f-3f12-b4a4-1a3e41bbb75d | -22.35827 | -54.61753 | 2025-09-25 04:38:00 | NOAA-21 | FÁTIMA DO SUL | MATO GROSSO DO SUL | Brasil | 5003801 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 077f66aa-89a5-3779-999e-280eb486dda8 | -21.98285 | -49.50463 | 2025-09-25 04:38:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c5dec936-ab8d-3d08-b60e-5a1125e49b5c | -20.69916 | -57.86115 | 2025-09-25 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e190da22-c7e2-3ba6-b2b7-54f3539e0420 | -21.83462 | -50.57709 | 2025-09-25 04:38:00 | NOAA-21 | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 89a9957c-3fa7-35e4-9bb8-b0c645e9996b | -21.83348 | -50.58464 | 2025-09-25 04:38:00 | NOAA-21 | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7509f384-d86a-39eb-9779-9a81d8a9b556 | -22.38108 | -49.48354 | 2025-09-25 04:38:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb6ef0b9-b855-3c01-8757-8d76ba524da6 | -24.77418 | -51.10592 | 2025-09-25 04:38:00 | NOAA-21 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f2194d14-5348-3ead-ade6-3645cac38062 | -22.36271 | -49.46406 | 2025-09-25 04:38:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d8989159-1885-3971-b76f-344ae84186c2 | -21.99726 | -56.05583 | 2025-09-25 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 78e967b1-bc9b-3ef1-8490-90c21ee859bc | -22.38205 | -53.73674 | 2025-09-25 04:38:00 | NOAA-21 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3cacb61d-cd16-3526-aa05-dfe29b9288b7 | -20.76476 | -56.92301 | 2025-09-25 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e609cc03-2583-36d2-818b-8212a65a8c95 | -20.46853 | -55.78791 | 2025-09-25 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e7b935c-5359-3df6-8f48-82d17e7c3c07 | -20.69838 | -57.82 | 2025-09-25 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e7478a6f-1b5a-38c6-bcdf-59102b4cbc80 | -21.4327 | -50.44398 | 2025-09-25 04:38:00 | NOAA-21 | BILAC | SÃO PAULO | Brasil | 3506409 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 34efd944-6a38-336c-859e-e6f1d13fe137 | -22.64595 | -46.90447 | 2025-09-25 04:38:00 | NOAA-21 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6edb7e61-56e7-3806-9672-654f16346563 | -22.4117 | -49.14034 | 2025-09-25 04:38:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 593a269a-b92d-3c38-bd8d-3f7eb6593c87 | -22.61259 | -49.02089 | 2025-09-25 04:38:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c41eafa9-d82e-3e7f-a434-fcbc067c2594 | -22.08501 | -46.56881 | 2025-09-25 04:38:00 | NOAA-21 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 286719dc-e0cc-3254-b784-7e457ddde828 | -23.68797 | -55.26132 | 2025-09-25 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9bbe4b62-ef80-33bb-bd8f-90b51d3fdbdc | -20.47063 | -56.65353 | 2025-09-25 04:38:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b0dca58-ead9-32ff-bcc6-ccac3611d597 | -23.56781 | -49.77235 | 2025-09-25 04:38:00 | NOAA-21 | SIQUEIRA CAMPOS | PARANÁ | Brasil | 4126603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5fce4bb6-62c2-3184-8ca4-56660d5a6897 | -20.70433 | -57.85772 | 2025-09-25 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| fab8399d-6c5b-35aa-a077-1a241c5ed592 | -21.98228 | -49.50861 | 2025-09-25 04:38:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 35bbf079-32d0-37a7-90ab-0f9c2e6ceca0 | -20.70346 | -57.86208 | 2025-09-25 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 4b475343-64a1-363a-b2e6-a68b85c70fd8 | -21.97943 | -49.50406 | 2025-09-25 04:38:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d3f13057-48f6-3504-b275-997855388a4d | -21.97201 | -49.50684 | 2025-09-25 04:38:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 5107d9ad-c68b-3753-94f8-e4bf71e22866 | -21.9817 | -49.51257 | 2025-09-25 04:38:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2c38a84f-7db2-39f3-8b03-b236851d09d5 | -20.61151 | -56.71219 | 2025-09-25 04:38:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8e1c700-c78e-341c-99a9-412895a7c5ef | -22.36512 | -54.64103 | 2025-09-25 04:38:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7d2a8954-7398-394a-8776-3a826ac9aaf6 | -22.36387 | -49.48072 | 2025-09-25 04:38:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7508d72-bca0-3a37-80f0-a88f1554e411 | -20.73099 | -57.85899 | 2025-09-25 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| e2fb44ce-3c16-317d-a8fe-19139fae190d | -20.764 | -56.92699 | 2025-09-25 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9214f4d1-d313-32c9-be1e-e89fa7b91abf | -21.99348 | -56.05501 | 2025-09-25 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1c20af86-37f3-3d14-baaa-a907e08ef0de | -23.113 | -52.33374 | 2025-09-25 04:38:00 | NOAA-21 | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1063f077-b660-3dd6-b74d-375a12964b9e | -20.70038 | -57.82217 | 2025-09-25 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 15e0145b-2f2e-3825-800f-5f1745fbb0c6 | -22.26561 | -49.58132 | 2025-09-25 04:38:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ec677070-3d46-310f-a46a-472b2897bae4 | -20.60749 | -56.71138 | 2025-09-25 04:38:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99a50462-610e-3c6a-a90a-33dcfe1de7ff | -20.70863 | -57.85865 | 2025-09-25 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 66c35abd-70da-3fe9-9b36-757d32011a7e | -21.83015 | -50.58407 | 2025-09-25 04:38:00 | NOAA-21 | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a1e77224-550e-3675-9dd0-f69e579103fb | -20.70297 | -56.74099 | 2025-09-25 04:38:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ec8c763-7534-3e51-9391-83aec05d55f5 | -21.99637 | -56.0607 | 2025-09-25 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6bd21f70-d0dd-37c7-8f6c-e21490085bd6 | -21.97828 | -49.512 | 2025-09-25 04:38:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3ab1f2d2-2ea1-3ef4-a842-171f889422ce | -22.18274 | -56.00152 | 2025-09-25 04:38:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d698f6a8-14cf-33fe-8350-eab97d800519 | -25.36002 | -53.37383 | 2025-09-25 04:38:00 | NOAA-21 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2eb2a521-d691-3f1a-ad5c-391f159a966b | -20.70701 | -56.7417 | 2025-09-25 04:38:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d40e1d48-bd63-39c5-a70a-83dad8593ab6 | -22.32183 | -49.48359 | 2025-09-25 04:38:00 | NOAA-21 | FERNÃO | SÃO PAULO | Brasil | 3515657 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 76b03337-0dc0-36a4-883f-85af62ff987b | -22.38272 | -53.73278 | 2025-09-25 04:38:00 | NOAA-21 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |


[Clique aqui para ver as próximas entradas](README26.md)
