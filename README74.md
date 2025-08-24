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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a19a3d2-304d-381b-b1c9-f05e40938164 | -7.42857 | -60.62132 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b86d03ca-989b-39f1-981c-0c958fcabffb | -4.96303 | -55.8247 | 2025-08-24 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 0321ff83-dcd9-3ce7-bff5-5a08fadf5abb | -10.95213 | -63.01098 | 2025-08-24 05:23:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30cddb96-b944-37fb-937a-09c2ae38fe94 | -5.85898 | -52.08847 | 2025-08-24 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ebf9973-1fef-314e-b57a-615302c4131b | -6.74561 | -62.87053 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5ccf392-e88e-3408-b903-0cb23c9471ad | -6.90547 | -62.98548 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4edc5e02-18ed-3427-a194-6328f3f6bee4 | -14.84415 | -48.31791 | 2025-08-24 05:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ef5badaa-70ce-3f87-939d-34c0066b139b | -7.43133 | -60.62531 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 953bda25-e6d2-3cab-8b4a-43383389426f | -3.5159 | -47.21042 | 2025-08-24 05:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9b75f0ea-2725-38d6-b9dc-4bf213cbb1df | -14.82091 | -55.97071 | 2025-08-24 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1ef5bad1-518a-3795-b310-779ab00b76c1 | -5.87635 | -57.76135 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 111bac7f-961b-3e73-b847-36abd99e7e26 | -6.74967 | -62.86729 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f076ec2-d10e-37c2-801d-bd316c2bee4c | -8.84036 | -49.90066 | 2025-08-24 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43b3b9c7-3e7a-35c6-ada8-e22363a16ae8 | -3.78526 | -47.56789 | 2025-08-24 05:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b870fef-380a-3c64-bb15-aa64c38818a3 | -11.69361 | -60.19085 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 803d6212-5280-3ef1-b617-9fa1dd6f7909 | -14.29617 | -60.37974 | 2025-08-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4bdb0e5-1693-36d3-98e4-0707fddb9862 | -6.78034 | -59.643 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67ad03bc-a381-3b5c-bf01-ed41d52a70e9 | -9.02066 | -47.64735 | 2025-08-24 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 85da6f4b-3746-36a6-8103-5ab047042369 | -5.61401 | -60.23893 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6f6a6d3-cfaf-3860-a664-fa69592640c6 | -6.06017 | -57.86006 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8624827f-3871-366b-98dd-8f84b967ac16 | -13.18262 | -51.92125 | 2025-08-24 05:23:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62a0da53-4847-385e-90c3-987effcce7bd | -2.58114 | -51.91213 | 2025-08-24 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c828da7f-1978-3f0f-b36c-c6651c40cfcb | -7.05675 | -59.23896 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba391185-52a3-31e2-a2af-a113d6a4b63e | -5.80761 | -59.21312 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ab1d1ac-b374-3da7-bc2a-a264c5a784d9 | -1.55764 | -54.54207 | 2025-08-24 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b26b06c-85ae-372e-b7cf-7511bc0704c0 | -5.87281 | -57.76082 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6df7334-4910-3844-90a9-750d0cb65487 | -5.79506 | -59.21495 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d3883af-aead-3528-bdc0-365ca195e594 | -1.59353 | -55.89472 | 2025-08-24 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a84893f-11c6-3cc2-933f-77df79e7c4d9 | -5.64775 | -51.84684 | 2025-08-24 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e200cb7-71fa-3842-b611-cee7fa9ba95f | -7.02897 | -55.43895 | 2025-08-24 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a313e191-e0ec-3415-8425-65e9fa60e7cc | -6.31506 | -59.88361 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5f28e05-1015-339a-a802-56f02f539467 | -14.28593 | -60.3777 | 2025-08-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e57c3f26-1627-307b-8bc0-6e8d2b1bdf63 | -14.33058 | -58.59446 | 2025-08-24 05:23:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7b4f616-7454-39f9-b7ef-bbd5311f1781 | -6.91717 | -62.91311 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ff30833-dd70-3325-bbd3-d801df772257 | -2.91826 | -48.30722 | 2025-08-24 05:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d61e89dd-a0ae-3c5a-9949-3adb4de047bd | -11.64852 | -61.64561 | 2025-08-24 05:23:00 | NOAA-20 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 491c2a44-b86e-3a62-b0c5-0a7d18fcca91 | -6.57657 | -59.88118 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9466c20-fb0f-3268-a781-f9b049c5afb0 | -6.74907 | -62.87109 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2b13433-19e7-3267-848c-cec7f2bfbe52 | -9.50171 | -68.47096 | 2025-08-24 05:23:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4726b9b-6301-30cf-8ff0-4f132729b2e6 | -7.56763 | -63.4387 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e90b660e-301b-319e-b0ad-5a6ab0eea0d6 | -3.59255 | -47.52823 | 2025-08-24 05:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 75dc4835-98ad-3bc8-ad50-a8f7a20866c3 | -14.30316 | -58.49124 | 2025-08-24 05:23:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11853dd5-c138-387e-97dd-91051422702b | -3.89961 | -54.68617 | 2025-08-24 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 658334a3-1301-369d-8999-13b149d8b3a4 | -5.74486 | -57.60299 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e71ebb0-b8d5-3528-9b9f-88f18af6befa | -6.43407 | -53.38196 | 2025-08-24 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7faff2bc-b506-3706-a6d1-759aaa5590e7 | -13.68907 | -57.75784 | 2025-08-24 05:23:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fe1dd8b-4eba-33f0-93a2-914d2a7983ab | -6.94362 | -59.55572 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 968b261b-45a6-3ae5-b44b-5637e164b15a | -3.90108 | -54.69347 | 2025-08-24 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7072eae7-0ba1-387c-a53a-5c952c675cc7 | -6.56602 | -60.05822 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad593296-b5a5-355e-8215-15a35371e9ea | -6.46 | -53.40087 | 2025-08-24 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7830908c-50f1-3639-a73f-a3b265818f10 | -13.03185 | -56.87967 | 2025-08-24 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67137bd5-9dda-33e3-92fa-f6170cdad123 | -8.06663 | -49.65708 | 2025-08-24 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a1e5ae3-180c-3b0e-b949-e51ede452b91 | -5.64344 | -51.84018 | 2025-08-24 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c8ed995-85ad-3b7e-a57b-9ef9ea263d44 | -3.66373 | -54.7576 | 2025-08-24 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5799d8e9-ddf5-3de0-9f8f-53586ea1aedf | -7.57464 | -63.43986 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d378a82-abdd-3c0f-86bf-f71ae72c0dcd | -6.68483 | -58.85741 | 2025-08-24 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8855c992-690b-362a-938b-b5652304b11c | -5.74313 | -57.59032 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4959e93b-dcc1-3334-ab12-cd595803efe4 | -2.5831 | -51.91649 | 2025-08-24 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18baa2d8-dc96-3e28-9310-958daffd86fe | -5.85942 | -52.08542 | 2025-08-24 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 917992e7-a357-3327-8ce4-372c70bda47f | -4.47787 | -47.67202 | 2025-08-24 05:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee7a9896-6404-35dc-9407-787b2ff08d89 | -8.07836 | -61.53954 | 2025-08-24 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53f9a347-be55-3aa3-b818-9459cc5df99d | -3.79191 | -47.56862 | 2025-08-24 05:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a593bba-08fa-35b8-854b-1eddc6028c74 | -3.79108 | -47.57444 | 2025-08-24 05:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f7cebd3-c383-3fd8-9fc7-9b7183e64f93 | -3.43585 | -49.0454 | 2025-08-24 05:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0680f9f5-9c75-34a3-8761-b864fe9928f4 | -5.76493 | -59.88305 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b04f5e7d-2cb4-370e-ade5-8dbcba993c55 | -7.54619 | -63.85942 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2447fb47-f590-33aa-bd5c-050bd888dec5 | -4.95914 | -55.82413 | 2025-08-24 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 32cad217-36bd-3001-b334-0b0a0400eb62 | -5.43095 | -60.17154 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8a3fc0ca-49ce-3545-8f48-a9df8d249f62 | -14.46217 | -52.03992 | 2025-08-24 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 508d3ce2-f67d-3f1b-929c-576383b0898c | -2.53316 | -57.8453 | 2025-08-24 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 499c5c1b-4efd-33e5-863b-2cfaf303eb4a | -5.61786 | -60.236 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbe994e0-5f9d-345b-80f8-037306d32ccf | -6.92875 | -62.9072 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7c103ab-c46f-3c28-ba54-7c073b6e61b0 | -11.69756 | -60.18769 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c570da32-ba0c-39b5-87ae-0f03f520574c | -14.81417 | -55.9817 | 2025-08-24 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16b860d4-9e80-3775-974e-aae95e52f516 | -14.33805 | -58.59554 | 2025-08-24 05:23:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c914d12-1361-3196-945c-b67ff536c57e | -5.45205 | -60.18905 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2180bc9-9a0d-36bc-8bb0-1eb5b5662a04 | -14.28252 | -60.37705 | 2025-08-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb2c7aec-ef97-3331-832a-fbc02729a3d4 | -8.76263 | -49.97377 | 2025-08-24 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e95a3c0-ad01-3094-9587-ac249ff46b26 | -7.56299 | -63.86063 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54c22085-8cb5-3a53-a74e-eedf55c6df20 | -5.79171 | -59.21442 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65e33b60-337e-3b9b-b120-70c631134918 | -14.29561 | -60.38348 | 2025-08-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92aeda6c-60d9-3295-b7f9-26ffb917d21a | -7.29537 | -59.62414 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd545dfe-3168-38f1-a4f0-8da4d9c16dfd | -5.64905 | -51.83767 | 2025-08-24 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96784b6e-fe8f-329a-a448-e1ce6b45503e | -5.45259 | -60.1856 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f45473e-02fb-38cb-9d1a-94ec29fec62c | -5.80121 | -59.21958 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27540c5e-6ddf-3327-b0a7-7697214e9daa | -5.7945 | -59.21851 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2e9efcf-77f2-3ee7-93bc-9d9c50e2c39a | -6.87549 | -59.81666 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b830b6f-d0d8-3bb3-8ad6-9cf1268b9214 | -12.73451 | -48.11111 | 2025-08-24 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f28aa739-2d03-3046-b235-db3c3ab86f32 | -11.22176 | -63.7702 | 2025-08-24 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7880e82-0c03-333e-be1c-7660f30fc4a9 | -5.42709 | -60.17447 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2b400de-3af7-3449-a1f2-d39799a12e25 | -6.38163 | -62.90714 | 2025-08-24 05:23:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b8da421-c8b6-37f8-a44a-1ff03d2e3148 | -6.92185 | -62.90607 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1244e45c-1e85-3521-bb4f-5b0f349c2309 | -7.0237 | -55.43788 | 2025-08-24 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a6a7fc81-3c79-33c6-9e8a-bc01c193f351 | -5.43149 | -60.16809 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9613a7b6-3f4e-3614-a742-c0336bb0fe66 | -9.55835 | -68.58189 | 2025-08-24 05:23:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf2ccf7d-155c-38f2-b28f-22a15509c33f | -5.87696 | -57.75739 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94f035a7-026b-3059-8d51-10b2066b8928 | -8.76146 | -49.98298 | 2025-08-24 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4fe04a79-97b7-347d-9d5f-1433ec4ce78e | -7.02541 | -55.43469 | 2025-08-24 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e5e92b84-de7e-3528-8737-8750612d5037 | -7.62439 | -63.48851 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0e308b5-05ee-3030-9046-713fcd50c742 | -5.75147 | -57.58334 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README75.md)
