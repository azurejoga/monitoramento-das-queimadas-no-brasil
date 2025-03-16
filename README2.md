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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4503df25-9f14-3eb8-84df-2b7c3bd70879 | -13.42459 | -41.32221 | 2025-03-16 04:00:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7b6d1772-0527-345c-ba2c-f36f6e5eeaae | -12.47065 | -44.32763 | 2025-03-16 04:00:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 59c2f248-3c2b-31d7-b707-6384956460af | -12.30614 | -47.27185 | 2025-03-16 04:00:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6eb13e67-2d69-3386-849c-959235e8ef11 | -11.08169 | -40.40715 | 2025-03-16 04:00:00 | NOAA-20 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8f16e3f6-8f3d-31f9-b204-e631d49cf9d5 | -13.40017 | -44.15317 | 2025-03-16 04:00:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b70b71b5-48c8-3985-b64d-a3fbd9e1a04e | -12.82786 | -45.00644 | 2025-03-16 04:00:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4dad4de2-0168-3f91-95e5-230ba67e77e9 | -13.42789 | -41.32275 | 2025-03-16 04:00:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5d9a1039-83eb-38f5-bd13-576ecec32366 | -12.30262 | -47.26692 | 2025-03-16 04:00:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e249a7e8-072a-314f-b5d1-d062b3f8bf06 | -7.47327 | -45.76502 | 2025-03-16 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1428e46-57b5-3a53-8048-79e10fbf075e | -9.76811 | -37.66158 | 2025-03-16 04:00:00 | NOAA-20 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 25d99095-5836-3f1b-8100-6027f670b324 | -9.23156 | -40.42309 | 2025-03-16 04:00:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 004e89e8-3de0-3229-a30c-3a239bd49319 | -8.38355 | -42.26355 | 2025-03-16 04:00:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b46fde6a-3a26-3450-8740-74b481234dee | -8.04359 | -41.78188 | 2025-03-16 04:00:00 | NOAA-20 | BELA VISTA DO PIAUÍ | PIAUÍ | Brasil | 2201556 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0ebf6de7-4d51-3938-880f-e319ac56d929 | -7.47746 | -45.76576 | 2025-03-16 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b5089534-9998-3717-a439-12424accb9e2 | -10.69517 | -37.04882 | 2025-03-16 04:00:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 02386c7f-e376-31bf-a0bc-9a5d2e38347a | -14.13395 | -41.69218 | 2025-03-16 04:02:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5f94ba9f-a5cf-3644-8a5c-692f75a67f35 | -13.0905 | -47.14368 | 2025-03-16 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68bdf2ee-bc24-3d7f-b6ad-77793863722e | -17.70815 | -42.22364 | 2025-03-16 04:02:00 | NOAA-20 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 96f92da6-f3e9-3736-80f1-ec17627e77a0 | -16.71922 | -45.60783 | 2025-03-16 04:02:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3922265a-1139-344b-ab91-c29a07d1018f | -18.91642 | -41.48997 | 2025-03-16 04:02:00 | NOAA-20 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 178a1560-9b74-3021-bf90-4b44ba7bbb9d | -15.2567 | -51.47339 | 2025-03-16 04:02:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 873a7dff-008a-30a0-8b38-440e756bf7b1 | -16.36035 | -43.87892 | 2025-03-16 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83be3050-3d4b-3ff2-ad68-e6b08948a138 | -15.80173 | -41.34077 | 2025-03-16 04:02:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a370b3e8-96c9-3e1a-8380-e08aad4cda65 | -15.88611 | -46.00849 | 2025-03-16 04:02:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f20de27-0526-3835-b236-bff17f126e88 | -12.95294 | -48.64791 | 2025-03-16 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28432967-8677-3799-82f7-a05781bbf2eb | -20.35271 | -47.52406 | 2025-03-16 04:02:00 | NOAA-20 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6c8891b-98e2-36b7-baad-a9c38b103c48 | -15.41201 | -39.20822 | 2025-03-16 04:02:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ddb19cb1-1841-34cd-b867-d8ec9ff63855 | -15.60974 | -41.37558 | 2025-03-16 04:02:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0d593d0e-3c51-3053-ba50-bddfb47d6deb | -17.59426 | -43.19849 | 2025-03-16 04:02:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87fac81b-2a12-3cef-9912-6c8fbdf90846 | -15.47125 | -39.07354 | 2025-03-16 04:02:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 42851fee-ab05-36c2-8ec8-c6a64a3da69c | -15.83342 | -40.73774 | 2025-03-16 04:02:00 | NOAA-20 | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 633bee41-9653-39c2-8a5d-1f0eb2e31f9f | -20.34828 | -40.3608 | 2025-03-16 04:02:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1a3685f6-c70e-3c03-9a78-72895007e1b9 | -15.80118 | -41.34437 | 2025-03-16 04:02:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 97136684-e320-32f0-a8f4-4bf42b0746d5 | -17.37893 | -42.48232 | 2025-03-16 04:02:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 930caa15-a5ef-393f-bf12-5e12fcd8598f | -15.47184 | -39.06942 | 2025-03-16 04:02:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 324af201-afd9-37e6-a4bb-45f78afb48c6 | -16.34793 | -43.69555 | 2025-03-16 04:02:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91587d7a-41a0-305c-9b32-9e1fb6518ca6 | -19.94065 | -40.73403 | 2025-03-16 04:02:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3b2b07d0-46b5-3251-a6af-24758b68326e | -14.11911 | -41.67883 | 2025-03-16 04:02:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 45d8be3a-7b59-3058-9acc-7b9945d1a0d8 | -17.78228 | -42.80987 | 2025-03-16 04:02:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 620147d2-732a-3044-afff-7688ec9819d0 | -16.41222 | -43.77586 | 2025-03-16 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3a5ad9f-cffa-3251-85f0-e118afc19a2d | -15.89066 | -46.00456 | 2025-03-16 04:02:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65f4252e-fbea-3d04-9d0e-a2caca441fa3 | -15.25953 | -51.47489 | 2025-03-16 04:02:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bb8b5fe8-a2b0-3ac0-b0cf-6ad9c7f010cc | -15.83677 | -40.73832 | 2025-03-16 04:02:00 | NOAA-20 | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9488e938-9082-3259-a3ca-deeb9b2b8879 | -17.77897 | -42.8093 | 2025-03-16 04:02:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17e77e12-853a-3a83-8057-9c03c3615e9d | -16.0124 | -38.94276 | 2025-03-16 04:02:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5a1b8b80-aad2-3d6c-9a4f-c2ff59316a9a | -17.67713 | -42.74402 | 2025-03-16 04:02:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7c1443a-21cc-3e4a-87e4-afcd8d6249bc | -16.41561 | -43.77645 | 2025-03-16 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6c7237d-b491-3aca-9aab-eed551904fdb | -17.0202 | -41.06845 | 2025-03-16 04:02:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c251a708-353e-3f5f-a61a-de3684be0b33 | -18.74561 | -43.07582 | 2025-03-16 04:02:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f59dcbab-a11a-3b2a-ade9-0d8eda6d380c | -15.91592 | -43.91165 | 2025-03-16 04:02:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 13b01a62-56c1-3a7b-9956-8d1b4fae19fb | -16.67932 | -43.88341 | 2025-03-16 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d3ac2cc-9924-358a-a1ae-545e03e855d5 | -20.67975 | -40.56755 | 2025-03-16 04:02:00 | NOAA-20 | GUARAPARI | ESPÍRITO SANTO | Brasil | 3202405 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3e1d1a08-d814-3f26-bc67-68e7181711a8 | -20.17971 | -40.25182 | 2025-03-16 04:02:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 142808cb-34e7-3876-913f-bcf7981d5857 | -12.95664 | -48.65382 | 2025-03-16 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 987f09a2-ae58-3997-9074-36c08af33075 | -17.75194 | -42.89376 | 2025-03-16 04:02:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 346c8a4e-3d51-36ee-a0ae-ba5ba37aa144 | -17.09494 | -43.80558 | 2025-03-16 04:02:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ffc999f-00a0-36fb-a2a4-2b483f78d2cf | -21.89264 | -55.37171 | 2025-03-16 04:04:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7046aa54-f067-3d4d-8e11-d75566058dce | -27.33658 | -50.57437 | 2025-03-16 04:04:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 84e803fd-9ef8-3e21-946d-6233d97b1a0f | -20.40974 | -51.35747 | 2025-03-16 04:04:00 | NOAA-20 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 88a817e2-10df-3bf7-b55d-803553fa3e38 | -22.53913 | -48.81158 | 2025-03-16 04:04:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1654fc36-a2e5-3fb8-8e3d-41312994a637 | -22.53981 | -48.81548 | 2025-03-16 04:04:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e463c7d-a684-380f-b018-a02452d2a506 | -23.40455 | -46.55389 | 2025-03-16 04:04:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3b24701a-2155-32f9-b176-812812bf542c | -27.33646 | -50.57739 | 2025-03-16 04:04:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 91a5f3b4-75cf-3d31-8110-9a059f922e7f | -27.33727 | -50.57343 | 2025-03-16 04:04:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c67951e6-d901-389f-83f3-eb826ff702ae | -21.89158 | -55.3763 | 2025-03-16 04:04:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 057dac60-593f-343f-93be-827e9f28df3c | -27.33581 | -50.57833 | 2025-03-16 04:04:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 110316ca-fda8-3be6-98a0-f093813399c9 | -23.40384 | -46.55798 | 2025-03-16 04:04:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a67af567-8db7-3944-a18f-f614bbe8c829 | -29.86366 | -51.16531 | 2025-03-16 04:06:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| fed82aa5-7166-3333-8d2f-7df911ee21b1 | -29.87391 | -51.15572 | 2025-03-16 04:06:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| e2d7e4c6-f348-3f37-8949-502823b8af2d | -30.45673 | -54.63245 | 2025-03-16 04:06:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| eee1ef0b-905c-316b-af6c-fa0a74b7995d | -2.36551 | -51.88254 | 2025-03-16 04:49:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 13a0cc86-cdad-390d-8a95-3f42d1e0aa26 | -5.42625 | -49.08191 | 2025-03-16 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8abeec6-1006-38e3-ac81-bb70d1ce2bb4 | -12.30282 | -47.27119 | 2025-03-16 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a55f5fa5-c633-3128-a904-d8b398d1d1fc | -6.79605 | -47.59412 | 2025-03-16 04:51:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b95dc35-30e8-3dc2-b0f1-f4b50765d851 | -8.05424 | -49.97259 | 2025-03-16 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93805c0e-d538-37d6-8546-bba872943cd6 | -12.30732 | -47.27176 | 2025-03-16 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40751518-e5f7-3609-b377-f448b905ac6d | -7.05183 | -44.39283 | 2025-03-16 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f05b108b-efeb-3562-a645-fe337ee28336 | -3.88325 | -54.21463 | 2025-03-16 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d604684e-6233-31df-a4b1-4fca402bb9ca | -12.30343 | -47.26661 | 2025-03-16 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1291ce3c-1a86-3c60-8a46-e517c66c450b | -7.30744 | -55.30982 | 2025-03-16 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30537490-fbd1-3361-9447-b1ec2d8819bc | -15.63191 | -57.31085 | 2025-03-16 04:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6b8cf25-0740-3d5e-9b62-64d2c7bbd43d | -15.6382 | -57.31609 | 2025-03-16 04:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce3c8cfd-f766-3c6f-b8e4-06f1859893ae | -12.95492 | -48.64933 | 2025-03-16 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1839f39c-a8d2-3fc8-a381-bf72faa945e1 | -12.95906 | -48.64986 | 2025-03-16 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 377d3a58-79c5-3661-8408-03470246cac2 | -15.89056 | -46.00476 | 2025-03-16 04:53:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82f2f7d9-6ae4-3dc8-a61c-5b1ce81b2c9e | -15.8902 | -46.00793 | 2025-03-16 04:53:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75091d0f-e0ea-3529-92e9-2ca0858a46da | -16.67938 | -43.88467 | 2025-03-16 04:53:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1680620e-5f6a-3e84-9f42-30c4ae729d02 | -12.22717 | -54.31183 | 2025-03-16 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9521d776-6cb2-377e-8c0b-1bacfac2d3d6 | -17.71066 | -54.07955 | 2025-03-16 04:53:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85641648-56af-3c00-9970-186eef9d8d41 | -13.42703 | -41.32467 | 2025-03-16 04:53:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2afc1266-9d7e-352c-88f1-bd5489227b3a | -12.08595 | -54.5812 | 2025-03-16 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cba7caa1-9e15-3dc0-a50e-a8682d568d9f | -15.8553 | -54.13209 | 2025-03-16 04:53:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50596a81-5160-30ef-beec-7afe3faa132e | -11.42556 | -54.30329 | 2025-03-16 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69e64334-7644-37de-82e1-f2f15c65f8fc | -17.71401 | -54.0801 | 2025-03-16 04:53:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f143c13-ba3b-3e1a-a350-26c8c092a954 | -13.09086 | -47.14297 | 2025-03-16 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e53abcd2-1f5d-3d7c-944f-522a7a8627ed | -15.63471 | -57.31549 | 2025-03-16 04:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 526ba73c-5185-3b3e-b79d-c9a1fbea1dd7 | -15.6354 | -57.31144 | 2025-03-16 04:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 995fd107-5c04-3f10-8a9f-49b64af61a81 | -12.08263 | -54.58066 | 2025-03-16 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bd0bd73-23bc-34d1-aff2-a2027cb9d73b | -14.66642 | -53.01713 | 2025-03-16 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7362aa7e-ba41-3251-96d4-7c427271a748 | -17.71736 | -54.08065 | 2025-03-16 04:53:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README3.md)
