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
| c70a4950-c074-38ff-b3cd-59f9f5794b08 | -18.32656 | -55.04396 | 2025-09-20 04:57:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 7d7c4d51-9f50-342c-8428-1918d26422a7 | -23.28921 | -45.78201 | 2025-09-20 04:57:00 | NPP-375D | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b4584dd8-03a2-32b9-a714-8a42c56efd08 | -22.25713 | -55.99153 | 2025-09-20 04:57:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5bdc09d9-0afd-371a-9126-d25d0d28bb8c | -22.98095 | -49.9491 | 2025-09-20 04:57:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ca86c352-900d-39f6-9977-6eb3e6fa868a | -20.50315 | -56.87395 | 2025-09-20 04:57:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a565580a-8142-3749-b054-ed477bcf1eba | -23.51097 | -47.19329 | 2025-09-20 04:57:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c9765332-a35f-37a8-92b2-47ac8270c0ea | -21.292 | -54.80171 | 2025-09-20 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5732b6e3-9a12-3c20-a351-7a7c0ebea384 | -15.34031 | -59.40237 | 2025-09-20 04:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb60fb33-daf5-369e-8455-25d0cc7a99d9 | -23.20854 | -50.25369 | 2025-09-20 04:57:00 | NPP-375D | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 78367a35-5e09-32b2-a55c-2c8e59dffe1d | -15.34803 | -59.40036 | 2025-09-20 04:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f2899483-742b-33b0-8aa5-5aad866a7a51 | -22.27424 | -56.01384 | 2025-09-20 04:57:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0be2d892-1ee2-3ddd-86e8-0e7f24246d72 | -22.26105 | -55.98838 | 2025-09-20 04:57:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb877ee9-c32f-3a0a-993d-7e828334f7c6 | -23.27685 | -46.39846 | 2025-09-20 04:57:00 | NPP-375D | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4c55d7ea-3589-3d04-bcce-f6179b76c9fe | -22.62555 | -54.96811 | 2025-09-20 04:57:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| d8ed8f69-82c8-3917-b7ce-00af69f5e232 | -22.26047 | -55.99212 | 2025-09-20 04:57:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1ba0718-8c18-3064-a653-e0bf76fabce0 | -23.53379 | -46.25399 | 2025-09-20 04:57:00 | NPP-375D | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 14cddf26-e30d-3891-93b2-5b7ce6a77ab5 | -23.82151 | -47.58138 | 2025-09-20 04:57:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fa2f0996-573a-3e51-8e82-198cbce223b2 | -16.47295 | -55.13452 | 2025-09-20 04:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fe5c5dab-cb2f-33cf-ac06-cfe71bbf4598 | -16.47514 | -55.1423 | 2025-09-20 04:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a95a820f-1356-39a6-8523-cfc64095b82c | -18.32714 | -55.04031 | 2025-09-20 04:57:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0653beb-7e53-3a13-b42e-6e5f9de77d58 | -19.54259 | -48.04259 | 2025-09-20 04:57:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ba3c9a5-195d-3945-8391-00cb24c5b5a8 | -18.19059 | -47.23989 | 2025-09-20 04:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 01672971-1d67-3dbb-bde1-19e55d19c41b | -23.1841 | -50.93039 | 2025-09-20 04:57:00 | NPP-375D | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3e0442ce-f89d-3ec2-a004-0c0174c670f7 | -15.92488 | -59.43323 | 2025-09-20 04:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 20df5644-4aa8-3f0d-abbd-4260381826c1 | -23.5106 | -47.19201 | 2025-09-20 04:57:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b9ff4d34-fb4e-3b7f-9987-c64d0532c022 | -23.79098 | -47.56425 | 2025-09-20 04:57:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 96ad815a-437f-35c4-be02-4c50d535bdd9 | -22.80309 | -45.27291 | 2025-09-20 04:57:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| bfb75dc6-3fd5-337e-bb50-0fe28b215e27 | -21.28862 | -54.80113 | 2025-09-20 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8d9258e-14be-36dd-a87b-eea9945873fd | -20.35095 | -48.78706 | 2025-09-20 04:57:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 038f252a-54df-3e21-8a9f-516c142f138d | -14.84328 | -60.25612 | 2025-09-20 04:57:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 579ff6b7-72a1-3ab0-9286-66e7ed8e48a6 | -22.63942 | -44.5169 | 2025-09-20 04:57:00 | NPP-375D | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6fcf6cfe-39a9-3c55-a0cd-d23c4ca3ac1d | -20.32676 | -49.20272 | 2025-09-20 04:57:00 | NPP-375D | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 165118de-b127-3ec1-9039-051389449d75 | -22.62895 | -54.96868 | 2025-09-20 04:57:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 037d4e90-77bf-39c6-874e-0112232cceeb | -19.61752 | -57.74642 | 2025-09-20 04:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| c197a2a7-91ba-3d45-8902-da4240068a6e | -18.03747 | -50.95062 | 2025-09-20 04:57:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ea93498-0cf6-3e37-9b0d-732f7412461c | -23.54983 | -50.86679 | 2025-09-20 04:57:00 | NPP-375D | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 847001df-1cf3-3d18-b426-ecad79629060 | -23.31932 | -45.9779 | 2025-09-20 04:57:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 22220c69-57c6-376e-849e-7878b11594cc | -23.2765 | -46.40241 | 2025-09-20 04:57:00 | NPP-375D | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1e982501-b567-3c6b-8071-ace7c63eefdf | -23.51062 | -47.1968 | 2025-09-20 04:57:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 23cb06a8-61e3-3d0b-9ced-987c072ffd81 | -19.60786 | -57.74052 | 2025-09-20 04:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5062e2a3-b42f-3e97-bbe9-38609297ddfe | -21.29654 | -54.79462 | 2025-09-20 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff728f2b-11e9-32f6-97d3-44ef8f84cc35 | -15.33928 | -59.40382 | 2025-09-20 04:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9825d7cb-af94-31bb-af53-5693d3df76e8 | -22.80819 | -45.28246 | 2025-09-20 04:57:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 65ec99b0-f1ee-3105-a46e-92b29b94409e | -20.60125 | -56.72576 | 2025-09-20 04:57:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5775e46d-ad5e-3a39-a3cd-0808c9bab3d8 | -23.32499 | -45.97864 | 2025-09-20 04:57:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ca2ce48d-789d-3b6d-af72-fbcb415d1805 | -20.3561 | -48.78267 | 2025-09-20 04:57:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51bd44db-d83c-3c05-ac35-0cea35ac42ce | -19.0941 | -56.50434 | 2025-09-20 04:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a2f52ae1-c9df-3528-9df1-0c24e96687c4 | -16.68795 | -54.97033 | 2025-09-20 04:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07e94af2-d651-3a40-938c-9bb21496a6be | -22.8027 | -45.27735 | 2025-09-20 04:57:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| a2cb3754-f048-314e-8442-2ae3ce1d2919 | -22.18602 | -55.99489 | 2025-09-20 04:57:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f22a850-a4e1-3587-8126-b76aee3f8700 | -20.35552 | -48.78757 | 2025-09-20 04:57:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a64a958c-5715-3207-b271-a865df7dcba4 | -20.60064 | -56.72949 | 2025-09-20 04:57:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cfe8b39-d4ba-340e-9eb1-948c4cc74c23 | -22.19447 | -49.65079 | 2025-09-20 04:57:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d065555b-0a22-3970-ad73-7d5299de8bc2 | -15.77249 | -59.38761 | 2025-09-20 04:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0307ab14-6dfa-3f31-b93a-4af31a34ef45 | -15.7729 | -59.38586 | 2025-09-20 04:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4561a92c-ae43-3290-af33-aa4d39cf9d39 | -21.3019 | -54.78672 | 2025-09-20 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 628ed46a-2efe-34d7-afe9-9a0247f2f34b | -16.11199 | -53.80544 | 2025-09-20 04:57:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2dc065e1-ea81-3f48-a1b7-336d28a6f76c | -23.09052 | -46.67293 | 2025-09-20 04:57:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 31e04428-94b1-3d84-8fc7-21f243a257c5 | -22.80898 | -45.27347 | 2025-09-20 04:57:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 3a83efa9-ffd0-3b5b-ac0c-d8ab11266ba2 | -21.93914 | -49.47079 | 2025-09-20 04:57:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0dc034f1-39f9-335d-90d2-be2a41ce85f3 | -23.48111 | -52.1857 | 2025-09-20 04:57:00 | NPP-375D | PAIÇANDU | PARANÁ | Brasil | 4117503 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f1704df1-532d-316a-a89c-2bb5c7af7347 | -15.76899 | -59.38526 | 2025-09-20 04:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32020bd5-ea7a-3b41-a973-b94ec2f1b2e9 | -19.6113 | -57.74117 | 2025-09-20 04:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| cd94823c-e4e9-3cf9-9695-a1d91303af36 | -20.6052 | -56.72265 | 2025-09-20 04:57:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34388f6f-5ee0-3d03-ae69-5435d3cda9aa | -22.25771 | -55.98778 | 2025-09-20 04:57:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6acdcb3d-e6fc-3aec-88fd-27217884f136 | -23.32287 | -45.98109 | 2025-09-20 04:57:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2547fab1-5836-3f73-b101-e820eb40873f | -23.18362 | -50.93427 | 2025-09-20 04:57:00 | NPP-375D | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ed903be9-3e57-3f10-81bb-f235c3a29b98 | -22.80231 | -45.28186 | 2025-09-20 04:57:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 2db1d23f-ffef-37b7-9455-4bfede3bc313 | -14.83488 | -60.25484 | 2025-09-20 04:57:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 121240f8-aadd-3061-8e67-3637cc0a6855 | -19.61819 | -57.74247 | 2025-09-20 04:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| a2400757-7b93-32b7-a1f7-0599c74df0a7 | -21.29316 | -54.79403 | 2025-09-20 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80ffb596-8f6e-3225-9fea-6d4b4b92ac1c | -22.79719 | -45.27236 | 2025-09-20 04:57:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c16e4f8e-6a9f-3a77-be29-688e069f02c7 | -15.91358 | -59.45128 | 2025-09-20 04:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d795ca68-df7d-3c44-a73b-fef795ec8b75 | -23.59641 | -51.05154 | 2025-09-20 04:57:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6dee61d5-1548-3bd8-9a71-cf2746f87fa7 | -23.79131 | -47.56097 | 2025-09-20 04:57:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9221b62e-d016-3346-836b-dd9227d6d3fd | -23.21283 | -50.25448 | 2025-09-20 04:57:00 | NPP-375D | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bd13225b-1df0-35e4-827a-3f02522972ec | -23.54706 | -50.8647 | 2025-09-20 04:57:00 | NPP-375D | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3dc79b50-245b-3079-877c-616263cd3a50 | -16.86029 | -51.4459 | 2025-09-20 04:57:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f29f387f-0ba9-323a-a1fb-79b5313d9bc0 | -15.92577 | -59.42829 | 2025-09-20 04:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d130e854-eca9-3d61-ad85-40994f320729 | -14.83908 | -60.2555 | 2025-09-20 04:57:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 211ef07f-9cdd-37a0-ba0d-c5d38d095bb8 | -20.32817 | -49.20348 | 2025-09-20 04:57:00 | NPP-375D | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e5454d71-ff0f-3588-9f39-b0bd058b4e67 | -22.80859 | -45.27797 | 2025-09-20 04:57:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| d28dc66a-ac9a-3891-88f1-11d3a8caad5e | -23.79202 | -47.5624 | 2025-09-20 04:57:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| aa62c107-ea89-3d56-a414-548eb81322c9 | -23.55123 | -50.8653 | 2025-09-20 04:57:00 | NPP-375D | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4d4f3346-f099-3b2d-9d8c-45a5fe302467 | -25.14067 | -49.5561 | 2025-09-20 04:59:00 | NPP-375D | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 24f5b8d0-459e-3b59-b773-49fd9811a60d | -25.0444 | -49.23887 | 2025-09-20 04:59:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 6d11209c-6a50-3fe1-9a5e-7f48fbe2f2f0 | -25.04493 | -49.23372 | 2025-09-20 04:59:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 14553d2a-1776-3959-aed1-d061d07f3255 | -25.04548 | -49.22842 | 2025-09-20 04:59:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9ebeaa77-5e84-3bb4-b8c2-b22915168257 | -3.51424 | -49.44541 | 2025-09-20 05:14:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cf5f5a1-6233-3458-abe7-5217b880de8c | -1.27021 | -47.87265 | 2025-09-20 05:14:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bc6a4c9-5cd1-3778-a610-066c7610abbe | -2.83031 | -48.65863 | 2025-09-20 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6292f303-9e31-38d1-b393-62e448dcd467 | -3.519 | -49.44938 | 2025-09-20 05:14:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79d13656-3e6b-301c-b40b-2d739c05178a | -3.45886 | -51.21759 | 2025-09-20 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| bfca2cd9-dad5-3957-86a0-2cb012e74619 | -1.19526 | -54.22448 | 2025-09-20 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee2d8595-7332-32e9-9fd5-c22a3e687d19 | -2.98452 | -49.29166 | 2025-09-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 42b43072-1435-34ee-8691-e5bd8dc749cd | -2.63277 | -54.94146 | 2025-09-20 05:14:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cdba78c-a56e-3caa-8c95-870e082c304b | 2.41607 | -60.70271 | 2025-09-20 05:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 297f3149-557f-3a88-a130-76bd2cfec380 | -2.95819 | -48.60009 | 2025-09-20 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a6b76af-7135-34ca-8b76-8895363f4eee | -3.51285 | -52.74929 | 2025-09-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3635124c-365c-3008-9897-95d89c51a4f1 | -3.51702 | -52.74994 | 2025-09-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README26.md)
