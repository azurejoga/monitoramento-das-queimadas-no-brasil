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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f742799-fb5b-3bcb-8d55-415e9df92d0e | -7.26985 | -45.5725 | 2026-10-07 04:02:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e1d0465d-3eee-34d7-b203-9fb7da855301 | -6.93725 | -43.67649 | 2026-10-07 04:02:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8bf2b279-9742-3e89-9e06-16c8e1c8acbd | -8.19922 | -46.35284 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e66937b0-b705-3ead-8f1a-a904a372f825 | -7.47828 | -42.7944 | 2026-10-07 04:02:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cf38d9d2-2274-3df2-a9ce-ac790f6f7dcf | -11.11091 | -45.72685 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ec890aca-65ac-3b99-abeb-c9d52d240810 | -11.23781 | -45.25286 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5cc9f4c-cfb7-3d51-9763-7456a07698d4 | -12.95612 | -42.43406 | 2026-10-07 04:02:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| af99a148-3002-3d26-83c6-5e64dc980253 | -11.24042 | -44.8705 | 2026-10-07 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 65537eff-e3a3-3c09-a2b8-08feba085442 | -8.69906 | -45.21022 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9373b2c4-9bd9-3113-94f6-22469359e77c | -10.49366 | -50.44006 | 2026-10-07 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 22f0b624-9978-3c86-b409-420b13dbcba8 | -11.11194 | -45.7213 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b494fdb-4a88-3da8-8f8f-470e4fe3ae92 | -7.108 | -42.53862 | 2026-10-07 04:02:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 059b0f8b-209c-3486-bc5e-905f0b9e0b4e | -9.79266 | -37.32178 | 2026-10-07 04:02:00 | NPP-375D | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dcb24289-8052-3b78-a2b5-d11f07b3abe9 | -11.73142 | -43.65683 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ca5ba18f-5de8-3fac-a9b3-63d8545c1372 | -8.58558 | -45.67131 | 2026-10-07 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ec2f5ab7-ab84-3d89-ad3b-b848781ea05a | -13.38155 | -43.87424 | 2026-10-07 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab5fdc73-fb86-33da-96e2-83f4824f70c2 | -11.10881 | -45.73813 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| d1202a73-5ccc-3b94-9227-840e1f36b372 | -12.41301 | -40.92422 | 2026-10-07 04:02:00 | NPP-375D | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 91a97ee5-4ad3-37b6-8215-055f5cd2cbed | -11.7516 | -44.93369 | 2026-10-07 04:02:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e0ebacf-9280-3415-ad8e-cb5e826fda4f | -9.45338 | -44.5972 | 2026-10-07 04:02:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8aaf1dc-450d-3bf4-8a72-b82440e4f994 | -11.25906 | -45.18943 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5e4474a-9bf5-3a81-84a2-ff4a55c47824 | -15.72791 | -43.92884 | 2026-10-07 04:04:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c1fe36b-5750-3783-a52f-165eea5c4375 | -19.65768 | -43.69439 | 2026-10-07 04:04:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c4b3b1a-2c84-30b1-afc1-458b758e80be | -14.78605 | -42.89917 | 2026-10-07 04:04:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 2585e2c5-5757-39c7-bb77-4698b3a67350 | -15.33579 | -42.76463 | 2026-10-07 04:04:00 | NPP-375D | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dcb654df-9522-3155-a735-10a0e0d78fb9 | -17.43523 | -43.63296 | 2026-10-07 04:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5312f9b-8b20-33fb-becc-6e7c458248b1 | -18.53475 | -41.91903 | 2026-10-07 04:04:00 | NPP-375D | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2b8d893a-6123-342b-91b9-7bca342d4c23 | -14.89229 | -44.811 | 2026-10-07 04:04:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12665da7-8389-3fb3-9d2c-e9eacc67c7c3 | -15.42175 | -43.70401 | 2026-10-07 04:04:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 63a975f8-08e5-32e3-a41f-08541746e011 | -16.02433 | -45.13343 | 2026-10-07 04:04:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc1b8e58-cd95-37ac-b843-6fce029cb8df | -15.23679 | -43.27606 | 2026-10-07 04:04:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 27.4 |
| a3104a36-a9c4-3f2d-8686-d7e126740c83 | -16.40853 | -43.72659 | 2026-10-07 04:04:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17fa4018-ce86-3561-a268-fd23b9fa816d | -16.63569 | -44.34644 | 2026-10-07 04:04:00 | NPP-375D | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75a9310b-9807-3f5c-826b-d1f8d17a41d5 | -15.81352 | -43.93713 | 2026-10-07 04:04:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbc4a7dc-a9ef-3e20-8849-7e7988ae330a | -15.3349 | -42.76966 | 2026-10-07 04:04:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6ebb3ec4-7224-3304-bb25-917452d63062 | -18.53127 | -41.91836 | 2026-10-07 04:04:00 | NPP-375D | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| f62c374b-e0c2-3443-a8d8-90a41abc5d7b | -15.25114 | -43.26327 | 2026-10-07 04:04:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 40.4 |
| 9037b5f7-b5fd-3f0d-9bef-147dafd435e9 | -17.87745 | -45.98965 | 2026-10-07 04:04:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d5b99f3-222a-3101-89dc-a6ccfa09a19f | -15.32236 | -43.0947 | 2026-10-07 04:04:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bf1d8b24-b46f-37b8-8bbc-415927ba1c54 | -15.25025 | -43.26826 | 2026-10-07 04:04:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 39.3 |
| d95f4a2d-e4c9-34aa-8a21-1cccd21efa30 | -16.91205 | -47.18859 | 2026-10-07 04:04:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fb45c40-d158-3cf5-8841-a2cd16671fbf | -15.24547 | -43.27252 | 2026-10-07 04:04:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 39.3 |
| 5e5c055e-a29e-39c7-8032-be6504727d78 | -16.04161 | -39.84764 | 2026-10-07 04:04:00 | NPP-375D | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6bea1033-701b-3d8e-9166-b863c950917d | -17.43436 | -43.63777 | 2026-10-07 04:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f0e9fa0-f7db-3433-8a53-805365573b90 | -15.11035 | -43.62842 | 2026-10-07 04:04:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 48148fd1-da4f-363f-9d02-6f005149c103 | -16.03669 | -39.83553 | 2026-10-07 04:04:00 | NPP-375D | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 99b1a3fa-9dca-3644-99e0-6e7498709b94 | -17.43347 | -43.64264 | 2026-10-07 04:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cc373cf-3245-3cc3-a068-171a6a0f1cee | -15.36053 | -39.48171 | 2026-10-07 04:04:00 | NPP-375D | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ab1a2aea-e981-3247-9335-952c2451c88d | -15.24636 | -43.26754 | 2026-10-07 04:04:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 39.3 |
| c4fb77b1-13b5-318f-8a52-fcf9accf07f5 | -16.04221 | -39.84399 | 2026-10-07 04:04:00 | NPP-375D | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 205be6de-4f1a-32ef-b2df-bc23da98372e | -17.77273 | -43.00826 | 2026-10-07 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 041efe1f-52f3-3771-b749-82423e801172 | -16.03728 | -39.83189 | 2026-10-07 04:04:00 | NPP-375D | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b824e29f-8748-34ce-98ea-d9893ae01f8b | -16.1257 | -42.07635 | 2026-10-07 04:04:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9474d8e5-577b-360b-8dd6-c6cedfb638e4 | -14.98504 | -41.66863 | 2026-10-07 04:04:00 | NPP-375D | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d2df2de6-8a4f-37a8-b6b4-06e4d63d7b06 | -18.38577 | -40.31775 | 2026-10-07 04:04:00 | NPP-375D | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8dd28c8d-cb71-3246-9217-6ee0ea8527ed | -15.24725 | -43.26257 | 2026-10-07 04:04:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 40.4 |
| 13d0ad1c-0d76-3387-b815-3f6f4df22253 | -16.03393 | -39.8313 | 2026-10-07 04:04:00 | NPP-375D | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 93736015-0bff-3587-889a-3bc8f3992721 | -20.46623 | -42.34079 | 2026-10-07 04:04:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e32510a9-22ff-3038-9ddd-83137a01d09a | -15.88046 | -43.60369 | 2026-10-07 04:04:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e211f51-1c9c-32ba-830a-c4a5d25f8ebe | -17.73387 | -42.3772 | 2026-10-07 04:04:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c3aeaab-bbde-3b8f-a70b-4905c2713c8a | -16.55835 | -46.80898 | 2026-10-07 04:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f87adf28-9002-325d-a8bc-cc0a279e02bd | -17.01973 | -41.03335 | 2026-10-07 04:04:00 | NPP-375D | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2a6cd9c6-740f-39c5-a18e-87a397a4b901 | -17.73508 | -42.37558 | 2026-10-07 04:04:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fea517a6-3436-3b19-8298-03c13e2a5abc | -15.32517 | -43.09304 | 2026-10-07 04:04:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0efc54d9-f00d-3c7f-a3e1-c832828570d4 | -16.61471 | -39.5909 | 2026-10-07 04:04:00 | NPP-375D | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 12c111ff-67f5-39e5-83fe-104eee8170bb | -15.24158 | -43.27178 | 2026-10-07 04:04:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 1798e803-f760-3a1e-933e-13f89ab2eca5 | -18.53058 | -41.92238 | 2026-10-07 04:04:00 | NPP-375D | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 32c8ce5f-652b-3b3c-b76f-579845b8bbc6 | -17.87659 | -45.99409 | 2026-10-07 04:04:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a045f81-77e4-3975-9cef-d69747de7c7c | -17.43257 | -43.64754 | 2026-10-07 04:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4bcc8ff-b86e-3292-8cfb-5aba775956ae | -15.24068 | -43.27681 | 2026-10-07 04:04:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 170ee1ba-9e60-3904-b072-f9878191dc85 | -18.1824 | -42.34289 | 2026-10-07 04:04:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 7419a762-970a-3cd8-ab7c-ddcd7ce3477d | -18.53407 | -41.92304 | 2026-10-07 04:04:00 | NPP-375D | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d01a98fe-6e80-3aae-bf16-5f3ac9731cb1 | -17.02036 | -41.02956 | 2026-10-07 04:04:00 | NPP-375D | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4b71ebc7-9b3c-3dbd-ae22-68fd6cfba849 | -17.373 | -42.13387 | 2026-10-07 04:04:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 529c71ef-f59b-3aad-8189-38bb083a5445 | -17.73744 | -42.37798 | 2026-10-07 04:04:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 875b1851-7020-3fb9-af9e-2e2fc2cce99d | -15.16142 | -41.29124 | 2026-10-07 04:04:00 | NPP-375D | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 97e75ace-c0cf-3d4b-8e41-b4cfbe13dd44 | -16.56309 | -46.81002 | 2026-10-07 04:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b3c0b3f-5ecb-3b30-990f-ec02e6083874 | -15.41777 | -43.70324 | 2026-10-07 04:04:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 16.7 |
| d84389de-9483-3c74-8250-2342ed38a997 | -15.41872 | -43.69796 | 2026-10-07 04:04:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 7af48c73-568a-3a76-8ccb-6162f553a111 | -17.43909 | -43.63359 | 2026-10-07 04:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a104e13-4e89-3f1f-9eea-c85adb576e8f | -15.37986 | -41.74366 | 2026-10-07 04:04:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 333baba5-057f-31e5-ba43-a6de8ccea8fb | -16.04004 | -39.83612 | 2026-10-07 04:04:00 | NPP-375D | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c0cf62f6-5a1a-33a2-9de5-30d97412c917 | -17.43733 | -43.64323 | 2026-10-07 04:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1360a26-23a7-349e-ba9c-48083583607d | -17.43822 | -43.63836 | 2026-10-07 04:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9616142-17ee-34de-b032-4c7d2900a0d7 | -16.03945 | -39.83976 | 2026-10-07 04:04:00 | NPP-375D | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d95fd24e-214d-35ed-8af6-ec76bc2ef0e1 | -15.3312 | -42.76855 | 2026-10-07 04:04:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b663f847-521b-3fd3-98ff-bc0c7114c8e7 | -16.04497 | -39.84821 | 2026-10-07 04:04:00 | NPP-375D | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| de74c3bb-382e-3145-b695-aaddc4e1420a | -7.8676 | -44.2153 | 2026-10-07 04:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 3318f7a5-ed98-3eca-852c-8f6a183f0593 | -5.7374 | -45.176 | 2026-10-07 04:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 093cad54-30c2-3ebb-8f68-3b1a93b05463 | -3.531 | -54.6557 | 2026-10-07 04:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 7e7f17df-a4fa-340c-a885-73b59ab215c0 | -3.0 | -54.1287 | 2026-10-07 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| c4ff673c-0f19-332b-83a6-c84186d34c17 | -2.9448 | -54.1501 | 2026-10-07 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 5356e85c-3ee7-3cea-8332-dc26001233d4 | -2.7796 | -54.1138 | 2026-10-07 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 168.9 |
| 17941636-191a-317b-be48-1c2b1fbe87da | -3.0191 | -53.9071 | 2026-10-07 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| ff9bdc3d-9e25-3b37-8b06-2c5eeb17b7ba | -3.0913 | -54.287 | 2026-10-07 04:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 138b05e5-f843-3cad-9421-da07e057d492 | -15.2511 | -43.2743 | 2026-10-07 04:10:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 138.6 |
| a833b07a-1e4f-3cb2-a48a-b4705a217411 | -6.1481 | -47.331 | 2026-10-07 04:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 297eaa27-2974-3832-b120-9520b2da6c70 | -3.658 | -60.6222 | 2026-10-07 04:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| c3e99eb8-9ad3-3195-8b40-acbb59b780e5 | -8.7225 | -45.204 | 2026-10-07 04:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 44e2303d-efe7-3044-8672-31bc91e931d9 | -3.1972 | -50.5592 | 2026-10-07 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |


[Clique aqui para ver as próximas entradas](README42.md)
