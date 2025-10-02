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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b948b34c-b75a-3f22-978a-fbc73e5860da | -14.59443 | -48.33021 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46c39a99-34d1-363f-a629-c7d9fc090f3a | -15.92522 | -43.3 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbb4a641-9b49-3285-a02c-d70857592a3d | -14.30194 | -45.97182 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5b531290-55a5-3045-a85d-a5f470f8c7c6 | -12.68896 | -48.55247 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ccd3be71-8d46-3fba-9819-750970aed528 | -13.24116 | -48.50785 | 2025-10-02 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d31fbe1a-5ec1-383a-b1a3-d33d4b170e49 | -15.26515 | -49.31128 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 80eaacde-46ef-312e-b672-d7eebbfdb3d2 | -15.39759 | -49.18565 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b36b3cf5-49d8-3450-8306-e73a9b95007f | -14.30864 | -45.97802 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7d866eb8-a102-395f-8b1c-df8518feb4ac | -14.60286 | -48.32821 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e757f539-4fb1-398d-bd26-ee45c5f395dc | -14.47548 | -48.40512 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| febd8419-266c-3a59-b96f-e6ce8fd75f76 | -18.33266 | -41.81111 | 2025-10-02 04:04:00 | NOAA-21 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f3d54c40-9cb1-3fd4-866d-e2d6b32fa796 | -15.14733 | -48.38697 | 2025-10-02 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e32d722-0a63-36fc-b164-9e26932bbbbc | -13.31364 | -47.8364 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5437207-e768-396a-acc6-16b3391fc380 | -18.30322 | -43.71804 | 2025-10-02 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b924dd0-52c6-3b72-9d41-bf38b70246a7 | -19.00995 | -45.00256 | 2025-10-02 04:04:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| afac44a1-cb43-3680-a1ec-1dcfd87128a9 | -15.25704 | -49.30391 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 443ed507-2919-35ef-b61c-24c74dc71bcd | -20.24161 | -43.88226 | 2025-10-02 04:04:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| fa35653f-fa54-3b8c-85e5-9f04358670a9 | -14.97246 | -46.92791 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e8b3a64-c01f-3956-be07-8a9293cbfcc8 | -12.67072 | -48.57474 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b6397cbd-9e8a-319d-a1d2-b1b3639b983a | -12.50289 | -50.24512 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a01da39-bdcb-31f1-bd61-05b21c241256 | -14.60707 | -48.23075 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6eb54425-6314-3490-9729-54d9d4f9343a | -18.60601 | -50.70111 | 2025-10-02 04:04:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83f9ce6e-20e2-3992-b401-3c42b5c95c32 | -13.80487 | -47.53352 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3d962bba-4f0c-318a-8569-eeb49141d5ef | -19.89751 | -44.93769 | 2025-10-02 04:04:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f8c4ba34-588a-312e-a804-fe3a51409b8c | -14.97382 | -46.92611 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba40948d-b7d8-3038-8cb7-b7bfd7a7eed2 | -13.18609 | -47.84001 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72125032-c835-3e46-8609-b9b797bd1898 | -12.90967 | -47.17694 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8d20c74-204f-3ae1-90d1-4908a6ef462b | -19.69651 | -43.99054 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eee48b7c-0692-33af-9af5-3aa3b60e28f3 | -13.87219 | -47.95565 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39e0585a-d45e-3ca2-80d8-9f994266e29c | -14.21448 | -46.11697 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 114862f6-44c5-3e20-bdb1-3efbfd7ef6dc | -15.78778 | -43.68546 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1bcfd20f-a779-3fb0-9578-e9a7dcc01361 | -16.77834 | -43.03617 | 2025-10-02 04:04:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd28154d-5105-38e6-95f4-9857c7f767b8 | -16.00557 | -50.908 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83c11fdd-9dbd-3a06-8831-8f93727b4ba2 | -14.48035 | -48.40445 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64c9d174-54cf-3c5d-a1ac-370b603581f5 | -16.04981 | -45.72397 | 2025-10-02 04:04:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 578c216e-6d1e-309e-88c0-288af69eff47 | -15.33023 | -47.94714 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 020a1ea3-2c9b-370f-bf08-94e2800b0171 | -15.25965 | -47.90314 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1c977aae-fc50-3deb-9733-83c326a3965f | -13.7788 | -44.24614 | 2025-10-02 04:04:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc414852-5d9a-3011-80ca-c0dfd0ff9de4 | -15.76666 | -43.66651 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85f56671-2190-310c-a4a1-5d474ae5cd73 | -12.50427 | -50.25413 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2b32917-4d27-36f3-96be-2b54599538e0 | -14.64565 | -48.12943 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6030a607-ff97-3eb0-a832-067f56638643 | -14.47913 | -48.41001 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8c571be9-7074-374e-b7b6-0ed832921357 | -15.78502 | -43.68115 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 994757f3-0376-346e-9394-a4349a2c3f2b | -18.48617 | -44.03988 | 2025-10-02 04:04:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08307c60-f7bd-3ed1-9c8b-9125d0413bdd | -14.35151 | -43.84261 | 2025-10-02 04:04:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68d54844-a19b-342c-b185-6d3305bbbba9 | -13.30421 | -47.57807 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f492040b-0155-3f74-8ca9-4d020e12c142 | -17.9676 | -44.39501 | 2025-10-02 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64f49c23-676f-3c97-a31d-7e4bf0dc2a35 | -15.53508 | -45.21599 | 2025-10-02 04:04:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fee2838-0fd6-3862-b6d8-5d7034841d22 | -14.45434 | -46.34533 | 2025-10-02 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b67ecf72-1fad-3e57-910f-c5c904a94c6d | -15.93188 | -43.30116 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1185f251-11c8-3ee2-88c8-bc85da265956 | -15.21731 | -47.16753 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5edede6-c31f-3e1d-80ee-ee544c36d992 | -19.00081 | -43.01364 | 2025-10-02 04:04:00 | NOAA-21 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 59220d32-4669-309f-b401-5cfddc583d7a | -15.94797 | -43.30761 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| cb867cac-f456-3a79-b326-e641eec67f7c | -14.59038 | -46.71645 | 2025-10-02 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 566c477d-ee29-3e0c-82c8-3dd68d58b1ae | -13.05633 | -47.01323 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b30148d-131b-3a3e-a62a-e3ec71f6f091 | -15.79393 | -43.73246 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e843e91e-1208-391b-85a1-8b6a6f7b4018 | -14.22983 | -44.93483 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 654b37b8-3ce7-38e7-85f2-937df71f60cd | -15.36025 | -47.06873 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7966e8d1-f8b7-3ed2-a60c-d2284b904f53 | -13.15634 | -47.82143 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f255180d-de5c-35ce-bc95-dcaf0a8ac856 | -15.50932 | -45.90851 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3a49757-1520-3dfa-ad2b-cc4a5cecff9f | -13.77975 | -48.04562 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da630e9a-f130-35e1-bbf7-a5ca10aa1a84 | -15.60332 | -46.90449 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad3a22b2-9397-3f79-98f9-f9b6ddce9028 | -14.66083 | -48.11942 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cdf88807-b226-3c81-9d96-c38f977b5d70 | -16.02958 | -50.91852 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d094de0a-224b-3d04-9541-8a7e439db9d7 | -13.37745 | -47.29662 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe52f1e3-58c4-322e-ab93-8b930d07e139 | -14.31998 | -45.98 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85900217-311f-3b14-abee-1afd00d0ddfe | -15.22754 | -48.73249 | 2025-10-02 04:04:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 748fad73-d964-3576-97fc-323a347322bd | -16.0356 | -50.86171 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0dacc5b8-0664-3ba5-a251-7b5444c079e4 | -15.25248 | -49.30288 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c127e95f-bafa-3a90-be66-5c04c75d2b19 | -13.4019 | -47.77974 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 168d4536-5457-306a-aba2-99d4c1c55338 | -13.73909 | -47.91773 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c4820a5-b60b-319e-b2ae-599a8378ffe1 | -19.59211 | -43.81321 | 2025-10-02 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3296dcbe-d816-3052-9051-87775822a37a | -19.73697 | -44.13877 | 2025-10-02 04:04:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45518b10-1944-329a-a60b-05db2ee55711 | -16.04904 | -45.72834 | 2025-10-02 04:04:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f68b85af-a39f-3175-96d8-7b04d9519da7 | -15.18177 | -46.41658 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10a816e2-fb14-367b-8f40-ffe878348d38 | -14.21678 | -44.93314 | 2025-10-02 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1895fcc9-37d1-3c77-a29f-5ec379861567 | -19.50314 | -43.8166 | 2025-10-02 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa3be2ca-7c4c-337f-a168-47488d954e23 | -14.48349 | -48.43597 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ef09f19b-1810-314f-aa3d-ae67c733b895 | -13.56448 | -48.10262 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4f244099-5ad9-302a-8da0-9db798786b35 | -13.473 | -47.24121 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| afd396bb-43ad-37bc-a7d9-7e13a57f41f0 | -15.40386 | -47.04659 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b14a713f-7b69-380b-867b-44c9a087a67d | -14.43242 | -46.35694 | 2025-10-02 04:04:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59d81548-9373-3a6a-be8d-67555f080a25 | -14.47029 | -48.40873 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| abb35c5e-521a-3b75-98b0-8ece0894d7c3 | -13.79136 | -48.05549 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e2b41f84-4080-3df3-8aaf-dc1dd5fbcebd | -13.22592 | -48.43862 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3065cb3b-5049-34ef-b634-09f0c97eb18c | -15.10806 | -48.37235 | 2025-10-02 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09d71fa6-cde0-3371-b2e4-50a3d6befea1 | -14.64997 | -48.13008 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f1cf48c4-a4c8-3918-9af2-e5b9ed24b285 | -19.45626 | -44.27655 | 2025-10-02 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 267cbb30-22ae-35f5-8eca-081e125a98fb | -13.1706 | -47.85131 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57be25c9-be5d-3b45-a064-23ab15ea2bc7 | -13.704 | -48.62107 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41e4e497-0dde-39d0-a000-2a1b97c5f0e9 | -18.5046 | -43.39692 | 2025-10-02 04:04:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 64c7de52-6b57-3e58-a1b8-e615e1dd4975 | -15.92855 | -43.30058 | 2025-10-02 04:04:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f1ff6c4-2e4c-38f8-b75d-341a609ee69e | -19.88813 | -42.62245 | 2025-10-02 04:04:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e87fd0e7-2f73-3ad2-8efe-0285b743e098 | -14.31223 | -45.89095 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 704748b8-6787-3901-ae7c-540080bada13 | -18.50072 | -43.39993 | 2025-10-02 04:04:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 088bd044-c9fa-39c3-9d5e-e8d3a20d572e | -17.08809 | -48.56257 | 2025-10-02 04:04:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1b894494-34bb-3219-96e5-3068ac60b5a7 | -13.13222 | -47.42037 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef6b8089-3afe-3f68-9027-8d7a0b72b365 | -14.60621 | -48.23548 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea94b152-6959-3bc8-9928-b9d4e6dd464d | -15.23724 | -48.72957 | 2025-10-02 04:04:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ce2e21f5-9551-3852-9cab-11eeb6c1756a | -13.95741 | -48.1113 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README55.md)
