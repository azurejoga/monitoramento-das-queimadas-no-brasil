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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fea3e88-c88f-3f05-a4be-fff3ac1ed433 | -22.0285 | -49.7042 | 2025-10-07 00:40:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.7 |
| 100e3930-a15b-3e60-b866-620d0aec170d | -18.1769 | -53.3669 | 2025-10-07 00:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 951a297d-376d-3430-b614-cafde4f9fff0 | -10.8542 | -51.0308 | 2025-10-07 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 233.3 |
| 003f5a10-29b6-3bfc-b141-42de6d8584ee | -22.0279 | -49.7274 | 2025-10-07 00:40:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 210.4 |
| 3324be0e-6bc0-3caa-946f-0850bfb6a1f9 | -21.4993 | -46.005 | 2025-10-07 00:40:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| 3279e99d-b59b-3483-8070-1d66ed724f98 | -10.8922 | -47.093 | 2025-10-07 00:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 72a6f07a-5b69-3e0d-94ad-76615f7f9ffe | -4.6875 | -45.828 | 2025-10-07 00:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 7e813340-57f9-3ba6-b7ec-140a385bdfb1 | -12.9103 | -54.7352 | 2025-10-07 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 8d07cb7e-a902-39dd-ad19-494e4f37ca7f | -11.7833 | -45.1347 | 2025-10-07 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| ab525ef0-86b9-30e6-bf8a-df61fc35da35 | -22.1621 | -49.3737 | 2025-10-07 00:40:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 4e15dd6e-b626-300d-8e35-468d34071de2 | -11.7401 | -43.2928 | 2025-10-07 00:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 164.1 |
| df330d3c-e79d-3ef6-a28d-b81943bfa505 | -8.174 | -50.3035 | 2025-10-07 00:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 3aa470d7-7236-375a-826b-2baef677ec23 | -8.5007 | -46.3342 | 2025-10-07 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| c9c9a4da-49fa-3523-b872-82e481c1b6a4 | -8.613 | -44.9189 | 2025-10-07 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 789808f4-67ae-3477-a282-9ae7968e481b | -10.2693 | -44.3745 | 2025-10-07 00:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 60dd98fc-b4e1-371f-8a58-f6ae16364bca | -22.3128 | -49.8915 | 2025-10-07 00:40:00 | GOES-19 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.8 |
| ccc8ca05-6a6a-3570-a210-88bd65290187 | -7.5874 | -64.5097 | 2025-10-07 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 38b02d6f-ff85-3894-8c1e-494753331434 | -6.454 | -44.5978 | 2025-10-07 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 6e29d892-048e-3b4c-b7bc-8d7907db2ea5 | -8.501 | -46.3117 | 2025-10-07 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| a595fc6d-e417-32fc-b60d-00e59c5406d0 | -14.7199 | -45.9942 | 2025-10-07 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 062a5197-25f2-3d63-b1ee-fe22ca26b578 | -6.2609 | -43.2727 | 2025-10-07 00:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| a5bd81e8-ba87-36f2-a7ac-de3d7781646a | -4.6873 | -45.8504 | 2025-10-07 00:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| e3982789-667f-3967-a1d6-5d7b07a13395 | -22.3337 | -49.8867 | 2025-10-07 00:40:00 | GOES-19 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.4 |
| 69a85122-2087-32a1-b388-32f0f48ae9bb | -10.9113 | -47.0906 | 2025-10-07 00:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 4a54bda2-3a11-33e4-b748-1174147a7761 | -18.1574 | -53.3485 | 2025-10-07 00:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 66.4 |
| b0951023-29b9-343c-8f20-0a84e3dd0501 | -10.8728 | -51.0501 | 2025-10-07 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 145.2 |
| ff1b038a-57f8-3621-abee-39c4f3e0adc1 | -18.1172 | -53.3763 | 2025-10-07 00:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 60.9 |
| a5686b53-cd8e-33d1-9cf4-aa539635c763 | -5.4937 | -43.0761 | 2025-10-07 00:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 5437ce61-3d4c-3c90-a1fb-8769720c5046 | -12.1655 | -50.9073 | 2025-10-07 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| b0a66e58-c0d0-3829-bd7a-14878e3da069 | -4.4445 | -43.2397 | 2025-10-07 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 86bdd2a6-d6ec-3110-93aa-5759e01ccb7a | -8.6521 | -46.274 | 2025-10-07 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 148b079e-42a2-3dc4-88d8-5284ed77bb09 | -5.4937 | -43.0761 | 2025-10-07 00:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 194.8 |
| f305b892-6d0b-38a0-80f5-1a213c37da62 | -22.1621 | -49.3737 | 2025-10-07 00:50:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 118.7 |
| a5aa14b2-9d4a-3733-a47f-eb675542c9d3 | -4.6875 | -45.828 | 2025-10-07 00:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4c94a13f-68e4-3d9e-8b43-360091cec724 | -18.1172 | -53.3763 | 2025-10-07 00:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 9656a644-a376-3843-af61-e463d4263a8e | -22.0285 | -49.7042 | 2025-10-07 00:50:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.4 |
| a8f13301-b60c-37bc-8118-48004b479b5d | -4.6873 | -45.8504 | 2025-10-07 00:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 1713158b-0ecd-35fc-9874-344e0188d855 | -6.4543 | -44.5749 | 2025-10-07 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| d0f95c49-fd55-3728-8acd-483c3332381f | -10.8542 | -51.0308 | 2025-10-07 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 399.0 |
| f72cc29f-fed5-3946-967b-b7074823c7d8 | -8.6127 | -44.9418 | 2025-10-07 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 6de85afd-16c8-3730-9658-140d6bed08e5 | -20.7824 | -48.7458 | 2025-10-07 00:50:00 | GOES-19 | SEVERÍNIA | SÃO PAULO | Brasil | 3551900 | 35 | 33 | nan | nan | nan | Mata Atlântica | 111.3 |
| f5e25036-e635-3390-bb25-c5720fa3bc52 | -8.5007 | -46.3342 | 2025-10-07 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 04919ce8-2987-33e0-9715-fb5386eeb3c0 | -8.6333 | -46.2759 | 2025-10-07 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| b9c28a03-f1b2-3878-ae53-0de5c77f9e2a | -8.6316 | -44.9398 | 2025-10-07 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 7c641345-64a6-3761-a170-7efce14bdf92 | -10.8731 | -51.0289 | 2025-10-07 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 233.3 |
| e1c1a8a0-246a-3d27-b908-09bf08ad3bb5 | -10.8539 | -51.052 | 2025-10-07 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 220.6 |
| 70d0c7b0-1285-3528-b291-9510e24521d9 | -5.494 | -43.0526 | 2025-10-07 00:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 1dfb76b7-f3b5-3424-9d72-c6095adf56cc | -18.1769 | -53.3669 | 2025-10-07 00:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 11ce7665-561d-3204-8437-98a6d9a6d02e | -21.4993 | -46.005 | 2025-10-07 00:50:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.9 |
| 4bfbc099-03dd-325b-90df-2b82cac09a8b | -6.2421 | -43.2743 | 2025-10-07 00:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 82ec39ea-cddd-3fe5-a2ef-18dda01c3a63 | -22.0077 | -49.709 | 2025-10-07 00:50:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 168.1 |
| ccbadd18-629b-37f6-a39d-3801620d4823 | -10.8922 | -47.093 | 2025-10-07 00:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 1f3ecb51-883e-3639-9226-f06b2bf20853 | -22.0279 | -49.7274 | 2025-10-07 00:50:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 150.0 |
| 2b8c2897-f805-3381-a5a8-cb100978bfa5 | -8.501 | -46.3117 | 2025-10-07 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 8a72ee38-f020-31bd-a310-f539585bf9ec | -4.4445 | -43.2397 | 2025-10-07 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 48912329-2bfe-3abd-95bf-c12ccd4b2c3f | -22.0071 | -49.7321 | 2025-10-07 00:50:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 239.6 |
| 81d74280-7027-3c2b-b371-4a34b0d9009a | -4.4446 | -43.2164 | 2025-10-07 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 90778a9b-5fa7-3d83-a6b7-02fdf59e0e01 | -20.783 | -48.7226 | 2025-10-07 00:50:00 | GOES-19 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.3 |
| f4b49b3c-5114-3482-8e58-8b43abeaa74e | -10.8728 | -51.0501 | 2025-10-07 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 167.6 |
| a7ec86ba-fd25-3866-a6d0-b3289027cb4a | -10.8545 | -51.0096 | 2025-10-07 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 4a4f8c0e-a040-31d3-92a7-3f0024030f0c | -5.4935 | -43.0995 | 2025-10-07 00:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 094a6876-69d4-35aa-ab9a-93d8b0af67cc | -5.5125 | -43.0747 | 2025-10-07 00:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 73fe03ac-e39d-3801-8bbe-1a6dd81a8aba | -8.174 | -50.3035 | 2025-10-07 00:50:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| d41fbea0-3be4-3782-bb13-044b3d9be7f7 | -14.7199 | -45.9942 | 2025-10-07 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 2b956bc1-d91d-3607-bf41-dbc277296e5c | -8.6519 | -46.2964 | 2025-10-07 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 1a4e641f-469d-3624-8700-398b1d249505 | -22.1829 | -49.3688 | 2025-10-07 00:50:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 101.7 |
| ed5083b9-0e36-3a3e-86dd-bf8c2a3756ae | -8.6319 | -44.9169 | 2025-10-07 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 9681d990-430e-32ec-8ac3-d7d765fbaaf6 | -18.157 | -53.37 | 2025-10-07 00:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 106.0 |
| f237c4ea-5a04-3a35-bcce-2f3f3af3602a | -18.1574 | -53.3485 | 2025-10-07 00:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 60.4 |
| e6c3ec65-89f4-3e5f-94f6-6a966ec47a38 | -10.8919 | -47.1153 | 2025-10-07 00:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 3c028013-a403-3434-a00b-7b3e519fc43c | -11.7401 | -43.2928 | 2025-10-07 00:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 108.0 |
| c0d18c21-b523-3276-a3a0-45d4ecd93755 | -20.7618 | -48.7504 | 2025-10-07 00:50:00 | GOES-19 | SEVERÍNIA | SÃO PAULO | Brasil | 3551900 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.5 |
| 82128776-dcde-3bbd-b0e7-69ad2d449902 | -8.1927 | -50.3019 | 2025-10-07 00:50:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 402767a5-0b82-34c3-b681-a72ac3dea30e | -8.613 | -44.9189 | 2025-10-07 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 202.3 |
| ee619a2d-4cec-3872-a134-21cad4d9b88b | -12.9103 | -54.7352 | 2025-10-07 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 660a0369-8c2e-3749-bbf7-986a4337d3ac | -18.1176 | -53.3548 | 2025-10-07 00:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 84.0 |
| eae42221-dacb-35b3-bd4c-ae52981a4c15 | -10.8728 | -51.0501 | 2025-10-07 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 67c8adab-9231-394c-83dc-ec7808a4f383 | -4.4446 | -43.2164 | 2025-10-07 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 993482dd-b5b9-3bd2-a0ac-ef5756dfdab2 | -8.6519 | -46.2964 | 2025-10-07 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| e7f5c02a-111d-3d4f-a72a-08af76744da5 | -22.1829 | -49.3688 | 2025-10-07 01:00:00 | GOES-19 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 104.1 |
| f2c033d3-e692-3b1e-b197-4759a3049ec6 | -5.4937 | -43.0761 | 2025-10-07 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| c66e7239-7a9d-3642-b361-046016b2762f | -12.9103 | -54.7352 | 2025-10-07 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 87575e97-89be-377b-bef4-a67d6ef20f06 | -22.0279 | -49.7274 | 2025-10-07 01:00:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 117.8 |
| 9e6e7738-adbe-36ba-85dc-d9c0af75ba69 | -22.0077 | -49.709 | 2025-10-07 01:00:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 179.0 |
| 97c563e3-3172-3f2b-a8c4-a86aa4f1ac00 | -8.671 | -46.2721 | 2025-10-07 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 8134dcfc-eea0-3c01-bd27-f57fb6e3449c | -5.5127 | -43.0512 | 2025-10-07 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 98d3aaa0-c398-3c85-9007-b229950c9f8c | -5.5125 | -43.0747 | 2025-10-07 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 68a01337-8558-3d8c-8215-6ee3ad649893 | -4.6875 | -45.828 | 2025-10-07 01:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 79.4 |
| f3b20a92-d3c9-33e9-9471-ef5e278df062 | -11.7401 | -43.2928 | 2025-10-07 01:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 2e2ebc27-1b4a-3777-b964-94d3797e3a30 | -12.1655 | -50.9073 | 2025-10-07 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 25629057-3484-37ed-bf39-26cebd09adaa | -8.501 | -46.3117 | 2025-10-07 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 0b403f19-b179-354a-822d-16937b515c11 | -6.5849 | -44.6327 | 2025-10-07 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| ea871e6d-f61d-39fc-88c8-4b0a39268987 | -8.5007 | -46.3342 | 2025-10-07 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| b9d2fb4e-9cb4-350b-99d6-2208364f09ce | -8.174 | -50.3035 | 2025-10-07 01:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| d555966f-49df-3f7f-86fe-2e905559c839 | -6.454 | -44.5978 | 2025-10-07 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 2a5769c4-c466-3324-b901-6ecaef65a76d | -6.4543 | -44.5749 | 2025-10-07 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| ee2e8800-4dfc-38a0-8e78-05c4ec9a7b07 | -4.6505 | -43.1805 | 2025-10-07 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 04d5c337-47b8-37be-b7ad-e4b9d3ca6008 | -4.6504 | -43.2038 | 2025-10-07 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 0d62ce43-7cab-3da3-acfb-6efe15c473a2 | -8.613 | -44.9189 | 2025-10-07 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 5afc9c14-6cfb-3ce9-a090-db6e2af2340d | -22.0071 | -49.7321 | 2025-10-07 01:00:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 269.3 |


[Clique aqui para ver as próximas entradas](README12.md)
