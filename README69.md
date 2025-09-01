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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ea75963-7be8-3eb6-b4f7-acf09565d986 | -16.0769 | -43.62437 | 2025-09-01 04:34:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6051216b-2ffc-30fd-b561-3837ab4c9341 | -10.23872 | -51.11712 | 2025-09-01 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cca3911f-de1a-3b76-b230-dc2da47c2611 | -12.79073 | -48.08348 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35173403-0134-342a-a6c2-a16380824b6a | -13.64762 | -48.15625 | 2025-09-01 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e92890a9-2a1d-3184-a4b5-b518bfe04d10 | -12.39238 | -46.46937 | 2025-09-01 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 849af332-4726-3c6b-82ea-11b258fc3b4c | -16.97224 | -49.30566 | 2025-09-01 04:34:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d72dfdc-b987-3184-a82d-bb82297f4b41 | -13.35627 | -44.62645 | 2025-09-01 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6516e086-80e1-380d-abf3-a59655f98883 | -10.2422 | -51.11772 | 2025-09-01 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d2367e4-461e-3c8c-94ce-cd93de5e6994 | -13.48904 | -46.99041 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cf8bac3c-0d38-31bd-97f7-ea3ee758ab0b | -15.71894 | -48.89548 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2652b3c0-ae7f-3a8d-8de9-a16e2862f00a | -11.05341 | -46.91709 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aaa11abf-a41f-3fa8-82fd-16ab2971841f | -13.97471 | -54.0671 | 2025-09-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af013760-afd5-38c3-a8fe-6dab3c88d56d | -9.44936 | -60.57547 | 2025-09-01 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a783b309-f51a-3b4a-8825-be4a61a829e1 | -13.52993 | -46.98044 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74ff462b-31c0-3382-8951-95f9c03b32b8 | -15.74095 | -49.95933 | 2025-09-01 04:34:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c1a3400e-a735-3181-8564-1600fe8c5f05 | -11.35202 | -43.52718 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6da991b7-239c-3dde-b3e8-5cadd94f9305 | -12.91114 | -56.98208 | 2025-09-01 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcbc56d2-4bfb-3293-87b0-ad50f084c7b1 | -11.51676 | -54.47619 | 2025-09-01 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a9c68ccb-c319-3128-b234-b8c332b58952 | -13.68352 | -46.9199 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e48381b8-665d-342c-874c-1ac1a3013506 | -12.56286 | -48.22163 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 46e590aa-605c-3018-825b-fe3d92850ca9 | -12.86459 | -48.06148 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f3660e4-5cf7-3238-9792-faaecb0a8c97 | -15.69 | -48.95036 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09e464c4-a589-3578-ae6c-457798aa7b7a | -14.79897 | -46.73545 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aaf66940-afeb-343f-aec7-402299d83010 | -12.57215 | -44.79634 | 2025-09-01 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8985214c-93f6-307f-9668-a85a983665ac | -11.89108 | -46.68763 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7adab3b-4ff6-3a41-9205-143bca4ccd3e | -13.37895 | -46.95446 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 086bb03a-eec0-33fe-8f20-56908a310299 | -15.72681 | -48.97878 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8f5805a3-f5ce-3c28-afed-6d075dac6057 | -13.49128 | -46.97512 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7bfb433-ad41-3ee8-b27e-ed3690e280c1 | -13.50876 | -46.97812 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34b098a0-fc4b-3cc7-9c5a-b8a54873f317 | -13.39064 | -46.94804 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88905bfe-1dc4-33a5-a6d9-478171af763d | -14.58787 | -54.54169 | 2025-09-01 04:34:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 898c8e99-3840-3a5d-91f8-58abb8f914a3 | -13.32317 | -46.86494 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 371d529c-5236-3dde-b819-5193f3fd8049 | -12.82657 | -48.07426 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a67d18d3-1f7a-3f23-8dec-cb4b50d40240 | -14.77113 | -46.76385 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1cb6060-62e6-3b04-b851-c9898c1bdc58 | -12.86686 | -48.06925 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26abffed-d645-3bfa-963a-37075a42aafe | -15.58602 | -48.33942 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 98cb0e95-3109-3990-87ff-8e0470a9a2ad | -11.48359 | -46.8003 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59cf13b1-f500-3248-86e9-468017912544 | -13.34876 | -47.03868 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c790273-9574-3e35-ac0b-149236662787 | -14.78869 | -46.73044 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| aec0185d-354a-3112-a1be-344aafd30f0d | -10.2359 | -51.11263 | 2025-09-01 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4fa83ea3-7ee8-3e3e-b14c-1125b91a922c | -13.37953 | -46.95047 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a1db7de-c94c-3f84-998b-a7e4ce441697 | -11.48761 | -46.82071 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bdf64709-083e-36dc-bdbe-cc615685b598 | -11.52217 | -54.46948 | 2025-09-01 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c985e1d7-3879-31f8-b853-88db0feb3875 | -11.05445 | -52.05162 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0639a69a-df08-3e31-94f9-3afcefbd9647 | -14.04489 | -44.57348 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0acaed55-2395-3a7e-b8ae-2be902fde20e | -17.14904 | -46.08603 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a7191ef-7ba3-3c9d-9395-c567b22e559b | -10.24502 | -51.12222 | 2025-09-01 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d0f6e91c-b88d-3a30-bfcb-aca80bce0691 | -14.75737 | -46.75766 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 67b3787a-e7f0-33e2-9605-a03a9fcc6f3a | -17.15222 | -46.09123 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5df9c484-dca9-3178-82f9-27d335b1b783 | -12.78629 | -47.64899 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 389e4f10-5bbc-33be-bc27-998084f4f3e8 | -11.87827 | -46.70184 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec8a71f6-42eb-342b-9c7b-c2dc9ce0a354 | -12.82993 | -48.07482 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d003693d-fb1f-3de9-a745-6db512acb59f | -11.05296 | -52.03862 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55d6f2c6-9676-373a-94a6-89ace18cccd1 | -12.81257 | -48.07573 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f647ccea-3c7b-3d61-ba8f-eb6bb3132902 | -16.96835 | -49.30873 | 2025-09-01 04:34:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e525b6d2-8956-30d6-ac94-479b969a42bc | -11.91259 | -46.44226 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4efe850d-ed20-3a1a-885d-33fd3c23f80b | -11.95735 | -45.84371 | 2025-09-01 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e48e77c-0e91-39a5-ba44-97fc0dc9c6c3 | -11.95698 | -45.79526 | 2025-09-01 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9758bedb-9c68-342e-871d-063515d05e9e | -14.79114 | -46.73904 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0529e77-20d5-3195-9739-cb544b165e43 | -14.80379 | -46.72734 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e3c1d00-7863-3e0a-98fb-8df993679ecc | -15.77353 | -47.80583 | 2025-09-01 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a72e4761-a28c-31a0-a1bd-cd5bc8d838c2 | -12.87887 | -48.1713 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ae892d3-ec11-36a4-9843-2042697e7da7 | -15.08043 | -48.11839 | 2025-09-01 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 954dc369-dc7a-367b-a75d-0e40aac07e5e | -13.58111 | -46.92991 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d9f0896-6375-3266-a839-abc58502b524 | -13.39589 | -47.05809 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19323ecb-7beb-301e-b487-0cb86976fc7c | -11.45301 | -46.81526 | 2025-09-01 04:34:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf0c2bf7-c773-30b7-a12d-9dede2c11779 | -12.40837 | -46.45923 | 2025-09-01 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e68cba0b-5a9e-3970-8bb0-4869a1ac717f | -13.49073 | -46.9789 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27ad2de2-dd82-3c9b-befa-6d92b5241c94 | -18.23039 | -48.13485 | 2025-09-01 04:34:00 | NOAA-20 | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a5db8e9-fde8-3a9f-90e4-6a13eaf6883d | -13.67776 | -46.93292 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67a74020-b618-37fb-aaf7-b467614a5c14 | -11.48589 | -46.80861 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3a7b97aa-4fc9-311e-9c72-bf2f0c257b8f | -8.62294 | -62.59579 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d70909c0-4195-359d-9991-666f0be38996 | -12.02382 | -49.71321 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b55fc9e6-9840-369c-bf89-795f6e5232cd | -16.97726 | -49.3177 | 2025-09-01 04:34:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b584feda-e17d-3b53-ba2d-e0118e17a274 | -12.57273 | -44.7988 | 2025-09-01 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8eab7586-99fd-3701-aea9-7a5ead2e69dd | -12.94092 | -48.10303 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92e1ce7d-dd62-3940-a016-1dee95fa99ab | -12.59856 | -48.21257 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad7549f7-24a2-35f9-a5f9-1a931e1615b3 | -15.72012 | -49.00005 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 17def4cf-8980-329e-8900-d49758276ae5 | -17.15519 | -46.08917 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d70f753-b86c-3afe-be91-1414cbc255a5 | -11.04308 | -47.00822 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 962a82a2-61eb-3630-aa86-b8b387ffb314 | -18.11953 | -48.5326 | 2025-09-01 04:34:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a56557b7-c1bd-3ebf-9ff6-a1354ec7a74d | -14.41836 | -51.67015 | 2025-09-01 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9f254b8c-b48a-3a16-8216-55a1daf1d53f | -11.37477 | -43.60809 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 084bbd28-ec43-3306-8efa-ad4e5c8d23d4 | -14.78996 | -46.72135 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cfa98e63-ea50-3aba-9336-7770b90417cf | -12.57341 | -44.79385 | 2025-09-01 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cfc1dc98-ef07-31ca-90b6-9dc081dbabf3 | -17.15963 | -46.08517 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7e3f25c-95d9-358a-8256-8143230dc777 | -11.45877 | -46.80037 | 2025-09-01 04:34:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e89002e-0651-3eb2-a727-785065deeffe | -15.69225 | -48.95814 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8a1580e1-b2ee-3367-ae77-421e675f1121 | -14.99148 | -48.15159 | 2025-09-01 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca20309f-6f2a-3a6b-85a1-7cfa616ee1f1 | -14.04393 | -44.58061 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ce72b0d-4a7f-3611-9180-31ca9941eb78 | -15.69834 | -48.89551 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f41332c8-9ac7-3d31-b180-f88597d4ce67 | -11.02823 | -46.94405 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0cdc1107-e9bd-38a9-a4bc-713ff4f8172f | -12.58237 | -48.20628 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e636b5c-e33a-3760-8dd8-5692f63ce1d2 | -12.66538 | -48.21552 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24251ca3-b824-3d69-a5fd-6917c4e6831f | -15.32706 | -46.10235 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 50f927c4-70a5-3f34-bf13-804da4227d1c | -13.17336 | -45.28194 | 2025-09-01 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f90163a8-69be-3e62-88ea-5ed44f3b5824 | -8.72581 | -62.41642 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b99efef6-053e-3f19-bc89-425b1cf8f293 | -8.7272 | -62.40947 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 10226c6d-2bdc-3330-b12f-516eda0805c3 | -15.72229 | -48.896 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0a2e6975-eb05-3b8c-90a2-40e015d323ab | -13.71099 | -46.92899 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README70.md)
