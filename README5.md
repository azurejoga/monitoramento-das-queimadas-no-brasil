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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0de1cc9f-8d0f-3195-9c6f-b2637a55121c | -14.3747 | -47.36488 | 2025-12-29 04:04:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fbd629ba-76b9-33c2-99c5-f1f9139e2ba5 | -11.54208 | -46.3125 | 2025-12-29 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 319eb2f1-86ae-3142-b8fd-55bf95931753 | -14.50091 | -52.55893 | 2025-12-29 04:04:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff589fdf-046b-33ef-9b15-ee3015535964 | -14.15185 | -44.25814 | 2025-12-29 04:04:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb24659b-6cd9-3ed6-86c7-e53c6c17af55 | -11.54794 | -46.30261 | 2025-12-29 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 041ad9a7-0e12-3367-9579-fe7fd0aa7ff0 | -10.63512 | -44.88318 | 2025-12-29 04:04:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2f562d0-ce53-32f1-88cb-5bceb1dd1697 | -13.51624 | -43.6743 | 2025-12-29 04:04:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a16b778-8945-380d-b69c-9e09903ce195 | -15.12688 | -45.28959 | 2025-12-29 04:04:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40bd4824-f0c7-38fc-8434-bf3f597095a0 | -10.47607 | -45.09073 | 2025-12-29 04:04:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f94896b5-d130-311e-8c83-53b8801c20eb | -12.6508 | -46.75949 | 2025-12-29 04:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b50b98d-0e9f-3999-ac59-657a726ff2e0 | -15.12975 | -45.29452 | 2025-12-29 04:04:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6367673e-e08c-356d-855c-a44ca9b60e86 | -15.84791 | -42.6308 | 2025-12-29 04:04:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 482a482a-7044-3cd0-a861-25f671d850ea | -11.54608 | -46.31324 | 2025-12-29 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 742bb04c-ee38-39f9-8497-6734dc692352 | -15.1348 | -45.28664 | 2025-12-29 04:04:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3551fb5e-c7b6-3e09-841f-5a8c025f930d | -17.29183 | -41.82305 | 2025-12-29 04:04:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d4d0e81d-91a3-3f49-9cda-0de56054f5fd | -13.4709 | -44.01071 | 2025-12-29 04:04:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ed5eba5a-dc2a-3f86-8ede-c1f7e6dee922 | -12.51518 | -44.98232 | 2025-12-29 04:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75a4fa0a-961e-33aa-89c2-a255c9494f2c | -13.38068 | -41.33226 | 2025-12-29 04:04:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d3a240a0-1099-3261-b610-5364876e5b95 | -13.47654 | -44.01968 | 2025-12-29 04:04:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3eed4c37-4c84-3a66-b04c-b422ec1dddca | -13.65059 | -43.73223 | 2025-12-29 04:04:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3871a76b-14d7-3b42-886a-c19793fd9e86 | -11.96628 | -44.15823 | 2025-12-29 04:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 485a9774-782c-3d8d-9eba-f1344683fa90 | -11.5538 | -46.29276 | 2025-12-29 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01b0e136-206a-3f52-a8d1-09f83144e835 | -15.12616 | -45.29384 | 2025-12-29 04:04:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aebbbda6-bb40-3128-a47b-fdf571969a74 | -13.47372 | -44.0152 | 2025-12-29 04:04:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 699cd5f4-38c6-3539-a228-e6f7673881c9 | -12.66635 | -46.76611 | 2025-12-29 04:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 041b3d94-10de-3786-866c-6531e640ecd3 | -15.13048 | -45.29025 | 2025-12-29 04:04:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad191680-cad1-32b5-a464-7412e2c3fdcc | -11.96433 | -44.21239 | 2025-12-29 04:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc91b090-c940-3d9d-8ce9-e2ea4a8e354e | -11.16502 | -43.31225 | 2025-12-29 04:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8955fe0f-b083-3cda-b61c-ff639e218fac | -11.96079 | -44.21178 | 2025-12-29 04:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b721b3bc-b22e-319d-8261-f05e34cdbe7e | -15.96663 | -43.28543 | 2025-12-29 04:04:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0842978c-0933-31c2-bc6c-ab0a1eb862b6 | -15.1233 | -45.2889 | 2025-12-29 04:04:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61b227a2-c2eb-32f1-80c8-64de4835ef78 | -13.71046 | -45.51283 | 2025-12-29 04:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4583ffda-ae1c-3135-ad01-7da4d4daff31 | -10.68967 | -44.99905 | 2025-12-29 04:04:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac41f8ac-7aeb-3f8a-90b6-5f5a916ff23c | -11.75203 | -44.5945 | 2025-12-29 04:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6137a78f-be83-3f1c-bc41-531a1bf04e53 | -11.55318 | -46.2963 | 2025-12-29 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4190f291-d901-32c5-965f-07142992d7fc | -11.75275 | -44.59023 | 2025-12-29 04:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 03578f89-f044-3c08-956f-ac3c7a9ce952 | -13.70226 | -45.51598 | 2025-12-29 04:04:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 373f603c-6188-34cc-977e-060404c18ed4 | -12.66571 | -46.76976 | 2025-12-29 04:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8aac1b91-2188-3e7c-9755-3cadc4c65903 | -12.21086 | -38.98431 | 2025-12-29 04:04:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b06eeea3-723b-353b-ade6-13332c636229 | -11.75637 | -44.59086 | 2025-12-29 04:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e77ccc42-7a28-360f-953d-f284a46ea6f0 | -11.01802 | -45.25752 | 2025-12-29 04:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8d95d48-95d6-3a0e-a73b-1b06ef03a203 | -13.47025 | -44.01461 | 2025-12-29 04:04:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 2c935332-f213-3846-a7bf-625c79fa9dbb | -15.37145 | -53.03387 | 2025-12-29 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec6c4bcb-086b-30f1-9bcd-4e324b30acb7 | -15.3773 | -53.03477 | 2025-12-29 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27d85927-ac02-32c5-989e-d378ba4d7bf0 | -15.13408 | -45.2909 | 2025-12-29 04:04:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbebe75b-5685-3e6d-99e4-a61e29d00ec3 | -16.91633 | -43.78102 | 2025-12-29 04:04:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e99fbc0-ff04-35d2-833d-d372e43960bc | -11.66912 | -44.88359 | 2025-12-29 04:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db142219-6589-38b1-80f7-08aae7a24315 | -10.52952 | -43.62058 | 2025-12-29 04:04:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77c0b319-6776-3478-948e-666971253daf | -17.29516 | -41.82361 | 2025-12-29 04:04:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 5ed8eaa6-28db-3b37-a486-afc911ab6523 | -11.55256 | -46.29982 | 2025-12-29 04:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 959c4b55-7a86-3d0d-a80b-eb7b96172c56 | -12.6623 | -46.76537 | 2025-12-29 04:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4eb3c793-7e12-36d3-bdee-94f6027504b8 | -10.86168 | -44.00063 | 2025-12-29 04:04:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9baa3858-36d4-3a23-80de-11c5ca18edd7 | -17.41619 | -42.46354 | 2025-12-29 04:04:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 986b56e2-d8ec-3817-b49f-d8e9bcee7734 | -12.66911 | -46.77416 | 2025-12-29 04:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95b7aca2-0e53-3ae3-9d5a-81eae8d5ce86 | -20.5052 | -41.71786 | 2025-12-29 04:06:00 | NOAA-20 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 93f4fdb1-9392-3d96-a7da-88919c955311 | -20.18129 | -40.2178 | 2025-12-29 04:06:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1f8e497f-44f5-3999-81ac-6d7ac5ca415c | -20.21114 | -40.21366 | 2025-12-29 04:06:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 69e2cee0-c806-3554-afa0-23f11977452b | -20.62447 | -48.94171 | 2025-12-29 04:06:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 29ffe690-3153-3cb3-92c9-f357d66e62dd | -23.03632 | -45.32801 | 2025-12-29 04:06:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9e7865b4-c992-35ba-a70c-386ff57c3715 | -22.5248 | -44.31783 | 2025-12-29 04:06:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5200bf48-cc76-37ed-883d-fb70d302f54b | -22.05365 | -44.43589 | 2025-12-29 04:06:00 | NOAA-20 | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6e653636-d1c1-39dc-b167-0fb9655e57a3 | -19.34012 | -40.8945 | 2025-12-29 04:06:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| ac2cc87c-0b15-33dd-af26-e4e5f48017de | -22.02887 | -42.3105 | 2025-12-29 04:06:00 | NOAA-20 | MACUCO | RIO DE JANEIRO | Brasil | 3302452 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2cddaf0a-626c-3b6a-90c1-58d76252f1b9 | -22.73531 | -44.19054 | 2025-12-29 04:06:00 | NOAA-20 | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 22d2b29b-c504-3988-a96b-73d1a1a0740b | -19.33263 | -40.89746 | 2025-12-29 04:06:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 66955e00-b771-3321-8284-99aee1bb4d4a | -20.23417 | -42.45201 | 2025-12-29 04:06:00 | NOAA-20 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ec09a3c8-6ed4-3c51-b258-5628068f4115 | -22.05758 | -44.43277 | 2025-12-29 04:06:00 | NOAA-20 | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d46e39d5-c098-3ec5-b101-30d1709b5473 | -19.42255 | -40.46753 | 2025-12-29 04:06:00 | NOAA-20 | MARILÂNDIA | ESPÍRITO SANTO | Brasil | 3203353 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 59e9b814-3bd5-370f-a2b0-0dd8f4c37d85 | -19.0286 | -40.34705 | 2025-12-29 04:06:00 | NOAA-20 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 79c2352b-87cd-3b16-9803-9bb8d9afa957 | -22.47631 | -43.53115 | 2025-12-29 04:06:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 508fa6b5-1ef6-32be-a0bf-6e35f49b2e83 | -19.25885 | -42.92128 | 2025-12-29 04:06:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6910ee30-83aa-3741-81d3-0a22864bd7af | -19.33957 | -40.89831 | 2025-12-29 04:06:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| c02ce9f5-35b4-3d18-a353-84e50a788eda | -22.19356 | -42.65687 | 2025-12-29 04:06:00 | NOAA-20 | SUMIDOURO | RIO DE JANEIRO | Brasil | 3305703 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| cb5e2ddb-aede-3bd3-855b-8e8e4e867e07 | -19.33319 | -40.89361 | 2025-12-29 04:06:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0ada8ca1-c914-3dde-a43d-729bbed28b0a | -19.33609 | -40.89794 | 2025-12-29 04:06:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 86ae644f-b7ff-3e60-abf0-e2a454bcfa3e | -17.61102 | -46.66092 | 2025-12-29 04:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f4a1776-9475-3c27-98d0-5cc6af5ebe62 | -22.54917 | -44.73178 | 2025-12-29 04:06:00 | NOAA-20 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 940dd346-c44b-383f-b8af-a53edaa9f1a0 | -22.37473 | -43.61657 | 2025-12-29 04:06:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f979da75-7993-3385-af28-a76ac8ee2635 | -21.90138 | -44.20162 | 2025-12-29 04:06:00 | NOAA-20 | ARANTINA | MINAS GERAIS | Brasil | 3103603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 06feb1c5-8fae-34a4-8bbe-64adb0ec7177 | -19.33664 | -40.89415 | 2025-12-29 04:06:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| ed64edee-c66e-3bb5-af30-e54a1bd9fe9c | -22.5254 | -44.3141 | 2025-12-29 04:06:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8c37cc81-7fdd-37fb-beaf-68bd834a7b30 | -20.38971 | -40.56068 | 2025-12-29 04:06:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| c3ed9ece-dfbe-32d2-be79-33532d1cf659 | -19.32302 | -42.68491 | 2025-12-29 04:06:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3b1beb15-37fa-3870-80d2-04118b8f0440 | -19.38832 | -41.47291 | 2025-12-29 04:06:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 369a62d2-48f9-322e-996d-1f523e5ea393 | -22.51876 | -44.31286 | 2025-12-29 04:06:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 05070e3c-7cbf-3a4a-9c3d-15d958aa2e80 | -17.61392 | -46.66633 | 2025-12-29 04:06:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27198edb-71f2-3494-ab3e-233dca6c8381 | -22.52209 | -44.31348 | 2025-12-29 04:06:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e96b6aef-356f-3aad-9e15-d4ff9be1e6ea | -24.94727 | -48.48966 | 2025-12-29 04:08:00 | NOAA-20 | BARRA DO TURVO | SÃO PAULO | Brasil | 3505401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 16435bd0-f24a-349b-b8d3-df4930deb8ae | -24.94357 | -48.48892 | 2025-12-29 04:08:00 | NOAA-20 | BARRA DO TURVO | SÃO PAULO | Brasil | 3505401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5be0b33c-b92b-3300-902b-65e1dbe8f20e | -24.94636 | -48.49449 | 2025-12-29 04:08:00 | NOAA-20 | BARRA DO TURVO | SÃO PAULO | Brasil | 3505401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d869cc54-44b7-3b51-92df-7dbb8e11b890 | -6.5631 | -51.1126 | 2025-12-29 04:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 56027f8f-4a22-3657-9b17-dfe4a87d85fc | -2.28967 | -47.02925 | 2025-12-29 04:50:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a57e91c-0918-32e8-896e-7f3b5ad40318 | -0.08772 | -51.27814 | 2025-12-29 04:50:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29b63527-fbbe-374d-b332-ad02461ccc7b | -0.09049 | -51.28207 | 2025-12-29 04:50:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb124dc0-b5a0-366e-a2f6-d997ec25fe43 | -0.09102 | -51.27864 | 2025-12-29 04:50:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52f00543-8210-307d-9c43-d1c7b45028f0 | -2.04601 | -48.03548 | 2025-12-29 04:50:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49ba1fbb-ed9b-3e83-acd3-daf416e71716 | -0.73366 | -48.06636 | 2025-12-29 04:50:00 | NOAA-21 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21eb5185-532e-3505-b7c7-e61464880093 | -2.77304 | -42.56989 | 2025-12-29 04:50:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee640762-9928-36bd-9e4e-d8648b365d31 | -1.12158 | -47.74238 | 2025-12-29 04:50:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d70e1436-70b4-3b9a-a293-0932d4caa43b | -1.99329 | -47.9819 | 2025-12-29 04:50:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README6.md)
