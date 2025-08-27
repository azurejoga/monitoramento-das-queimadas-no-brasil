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
| 57cc655f-2fe4-36f6-b681-23e1560ea3d9 | -20.324301 | -46.8722 | 2025-08-27 00:22:00 | METOP-B | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8e8488be-0aa1-3553-a784-694fae18126f | -7.6981 | -45.755299 | 2025-08-27 00:22:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8236782-7b51-3831-89ee-950f9424159d | -16.7068 | -50.398399 | 2025-08-27 00:22:00 | METOP-B | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4023b315-02d5-3933-9024-9288606dadf9 | -13.0593 | -46.299599 | 2025-08-27 00:22:00 | METOP-B | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bd69e2c1-6237-3e78-ab7e-43e0473b3394 | -9.5696 | -45.732498 | 2025-08-27 00:22:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3c7045ac-63f6-32ad-9f9a-3403839bc1cd | -12.747 | -48.1623 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 989439cf-f5d8-37a0-819c-9366dc08dca8 | -9.947 | -52.1479 | 2025-08-27 00:22:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc27adb1-80b8-33d6-914e-2091a6549fbc | -9.306 | -48.2686 | 2025-08-27 00:22:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68975bf5-1d18-3459-93e2-0127e067998b | -21.5753 | -47.503201 | 2025-08-27 00:22:00 | METOP-B | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e5269bcc-b321-340f-8140-36fc1f7492b6 | -6.7677 | -59.6175 | 2025-08-27 00:22:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45a959bf-0916-3e66-8216-6d8fae3057ff | -7.438 | -49.615002 | 2025-08-27 00:22:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3107d9a5-1b0f-3301-809f-c0cc46e8ef3d | -9.0814 | -49.590698 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3da8732-99a1-39c7-8f76-2a920bc62bf5 | -16.500099 | -49.479099 | 2025-08-27 00:22:00 | METOP-B | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 87cf888a-2afd-3729-9085-2f9e38944562 | -6.8348 | -58.9175 | 2025-08-27 00:22:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 49d6cb08-9bcb-375a-84ef-a50209317a8b | -17.558901 | -46.597 | 2025-08-27 00:22:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ee0d7741-2f87-3a57-9669-d7738b1f1129 | -13.6205 | -48.194401 | 2025-08-27 00:22:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 213ddd18-f2e4-3aa6-86bf-8c96a922243d | -11.5313 | -52.114399 | 2025-08-27 00:22:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91572fcf-a819-3814-bfc3-b4363e43c105 | -10.5036 | -51.59 | 2025-08-27 00:22:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48adb7b1-99b5-324a-807c-b4b87dc2eccd | -11.3885 | -55.338402 | 2025-08-27 00:22:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 983e6432-2d43-3edb-9224-cfe65df5bcda | -11.2395 | -45.4636 | 2025-08-27 00:22:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 00910ac6-6751-348f-bc11-0f2f5550ac63 | -12.7453 | -48.154999 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c30b8564-e4e2-33c7-99cc-fdf73735a8a2 | -13.4272 | -46.991199 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 38255a9d-a190-3a4d-af9d-5b09c35b22fc | -18.1378 | -44.437 | 2025-08-27 00:22:00 | METOP-B | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| eecbc0ca-6e8c-3507-bea2-ed6d257d880b | -4.9639 | -55.8032 | 2025-08-27 00:22:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e205038-3287-3f2c-b8ae-262caad90869 | -9.083 | -49.597801 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bad2e2e-22c7-3109-869d-0fbd42a62ebe | -13.0475 | -46.293499 | 2025-08-27 00:22:00 | METOP-B | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 205754ed-2c65-38a5-8d13-22ee56be747b | -20.7976 | -44.564899 | 2025-08-27 00:22:00 | METOP-B | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 45059f99-5eaa-3d50-9b58-637ef539ff8b | -15.0964 | -48.617001 | 2025-08-27 00:22:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2a0c01b6-3077-375b-803f-661ef524bb30 | -9.1782 | -59.424599 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ba210c0-6748-38ec-b9ae-91a318460802 | -10.3183 | -46.7616 | 2025-08-27 00:22:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1d2d782-1986-320d-87a4-f784117cb0ed | -8.2554 | -45.108601 | 2025-08-27 00:22:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| baed4a2a-b735-3484-88d8-07b4a12b394f | -9.4169 | -60.474201 | 2025-08-27 00:22:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b650d920-c041-3ed5-9ab6-56cd490a7828 | -9.5955 | -55.353199 | 2025-08-27 00:22:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48f4cc8d-35cf-3760-be7d-b09735fa0f20 | -9.1405 | -50.7729 | 2025-08-27 00:22:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d10b416-d7dc-3f32-b569-d3a050015dbf | -13.4563 | -46.849602 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 68ebddff-c8ed-3d5a-9287-a50ae388f1f4 | -19.9049 | -41.566799 | 2025-08-27 00:22:00 | METOP-B | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ee769433-ea38-3bb2-953b-30a3824d8965 | -21.582001 | -47.486 | 2025-08-27 00:22:00 | METOP-B | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bd1a288d-7fb3-3c43-98ba-b86687b8c180 | -21.590099 | -47.476299 | 2025-08-27 00:22:00 | METOP-B | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c20f2446-5b53-3e95-8969-81d98ab86dc9 | -6.9494 | -44.087101 | 2025-08-27 00:22:00 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b1c2067b-8e43-3c8c-bd9d-0eb1f051309d | -6.4822 | -44.670399 | 2025-08-27 00:22:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9386d285-ffe9-3399-81ea-247bba8c75a5 | -21.5804 | -47.478699 | 2025-08-27 00:22:00 | METOP-B | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| edb6b6d1-7c5a-35f6-b6c6-bf5053b001f6 | -6.9231 | -52.841 | 2025-08-27 00:22:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29bca897-d1d9-376e-af75-a727d1f72771 | -9.6995 | -48.320599 | 2025-08-27 00:22:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c148886a-6ede-349e-b451-c1933d411276 | -9.5672 | -45.722401 | 2025-08-27 00:22:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 673cab38-df6d-3279-a45d-805fd0c0b235 | -10.502 | -51.582802 | 2025-08-27 00:22:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a60b4aac-1cd7-316e-bdf7-bf1bcfd9e727 | -9.1743 | -59.4053 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 73569c41-19bd-3e78-9f50-2c1de5602f8c | -12.7682 | -48.165001 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53d09207-a8da-3f8e-9d4b-802f748baf0e | -8.684 | -47.1852 | 2025-08-27 00:22:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d34f11e-5e44-3bfe-8a2d-25ee93719d0b | -6.5731 | -47.375 | 2025-08-27 00:22:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 335c7d15-76a7-3534-99c9-fa5a4583c3e3 | -13.6487 | -45.689899 | 2025-08-27 00:22:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| db5d1671-a0a3-3aab-96df-eca6a797558f | -10.7128 | -47.303001 | 2025-08-27 00:22:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd7cb5b9-8539-3e87-93f7-787582c7e277 | -12.7584 | -48.167301 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ac2279d-73bc-3c3e-87d0-6d7c3177daf8 | -14.1267 | -45.396599 | 2025-08-27 00:22:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| baaa8a7f-881d-3f38-bfa0-1e4b3a5d4c69 | -9.07 | -49.585899 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53f79ddb-bc55-339b-bedd-366882cd5fa3 | -7.2856 | -46.981998 | 2025-08-27 00:22:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a8afb47-da4a-3b73-bbef-39a18418f97a | -9.393 | -60.454899 | 2025-08-27 00:22:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a84054b-17eb-3719-951c-9345829edeb3 | -7.7438 | -61.023399 | 2025-08-27 00:22:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 699f4cc0-443b-3c82-b754-c7bd37532656 | -7.1679 | -59.690399 | 2025-08-27 00:22:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa674db1-4d16-338b-bb1c-acde5c0374e3 | -9.4124 | -60.451199 | 2025-08-27 00:22:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6258c16-0c37-3017-bd79-85b24051bec3 | -7.75 | -50.2659 | 2025-08-27 00:22:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a67b44f-3d09-3b19-92e5-9831a897ea1a | -6.6581 | -53.178398 | 2025-08-27 00:22:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dc3a763-10aa-3255-8a95-ce3ffcd1a532 | -13.8401 | -46.679798 | 2025-08-27 00:22:00 | METOP-B | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 072cc132-de2a-388e-b7c4-67fe57a3229f | -7.1672 | -43.838501 | 2025-08-27 00:22:00 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cc1e37f9-5a3e-3379-a6a3-ed2d8197fb75 | -20.5327 | -46.101002 | 2025-08-27 00:22:00 | METOP-B | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c3486125-4788-353a-8abc-adf8b353ec5b | -9.1899 | -59.482899 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0833564-0294-3c75-9861-3687dc751cd3 | -9.1092 | -49.577 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e0e27c7-845c-3d01-9d8c-5fa7ed862321 | -3.7386 | -48.938202 | 2025-08-27 00:22:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e07c3a8-ca7e-3eb9-b0eb-a276b473e296 | -13.4529 | -46.9683 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9a71e03c-efa6-326d-a431-02bd8fd8826d | -21.107599 | -45.7229 | 2025-08-27 00:22:00 | METOP-B | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 28c00cf0-1f0c-3f9f-ab18-c78b4b727bed | -5.5303 | -51.988098 | 2025-08-27 00:22:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d47cc872-c2c3-37b9-af60-85c78117fbd6 | -16.530701 | -42.330601 | 2025-08-27 00:22:00 | METOP-B | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 52d31f79-8d11-30e9-9f6f-8603c35c2a3e | -6.8153 | -58.921501 | 2025-08-27 00:22:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ed79562-9d94-3cc9-b859-63d125f7fcdc | -9.1549 | -59.510201 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca932534-3879-3e2b-b1d4-599e8cb96570 | -17.552601 | -46.614799 | 2025-08-27 00:22:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 83d01535-0f87-3f3b-80d1-59309cdf6e85 | -18.2185 | -44.514801 | 2025-08-27 00:22:00 | METOP-B | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 553e9708-5c52-3144-916e-935485904ddc | -15.1002 | -48.541199 | 2025-08-27 00:22:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d598dd48-284c-31a2-8b05-fb17e7586a4e | -15.0781 | -48.396099 | 2025-08-27 00:22:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 01c0e93a-2798-3670-90d1-6f1aab7759c2 | -7.5671 | -47.482399 | 2025-08-27 00:22:00 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cdd9037d-c9b3-3ff8-85b5-cd7d251c561a | -7.362 | -57.597599 | 2025-08-27 00:22:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dea41a13-53ee-3c1e-99e1-ee745c317e06 | -9.1646 | -59.508301 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71000764-3843-38d9-ab55-b470dbc43376 | -17.775999 | -44.482201 | 2025-08-27 00:22:00 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b7ed37ce-7d46-34e9-a202-831b75ff3be0 | -9.5857 | -55.355301 | 2025-08-27 00:22:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 596d0087-e755-3edc-9203-24bb64739a5c | -8.8875 | -60.698898 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b58c38e-2ddb-3e79-991e-ed092199a709 | -21.5788 | -47.471298 | 2025-08-27 00:22:00 | METOP-B | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b181c82c-14af-32a7-9afc-b1cdf61998a1 | -9.4072 | -60.476002 | 2025-08-27 00:22:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 664fb676-d181-3dc5-ba2d-0b01db743a21 | -8.2952 | -46.318699 | 2025-08-27 00:22:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bcf78c33-8612-3e85-bf95-2be1fbaf4b0e | -9.088 | -49.574402 | 2025-08-27 00:22:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b35d0d67-2fb5-3e21-8a6d-7c83228b5da5 | -12.7826 | -48.092098 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43fee280-d549-344c-b0d9-40d72be6888c | -13.501 | -46.864101 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| abc296fd-b893-3fff-a99f-17c70db6f8c2 | -8.8824 | -60.7243 | 2025-08-27 00:22:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57e47ed1-e3a1-3e28-a55e-5d7fcdd36b4d | -5.6376 | -44.191502 | 2025-08-27 00:22:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f04d0013-ca50-31eb-aa5a-7a846944d24f | -5.7691 | -53.762199 | 2025-08-27 00:22:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b885ccb2-7281-3826-b9ca-456456ee4a4d | -7.7006 | -45.7659 | 2025-08-27 00:22:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e62307ca-bd4c-302d-aa25-a1d5ac559066 | -13.5396 | -46.896999 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2caed815-83c1-39fa-9f30-66073aeab44a | -13.4254 | -46.983299 | 2025-08-27 00:22:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8e429bfd-3587-3246-aaf1-c93e15f3edb8 | -12.7957 | -48.1045 | 2025-08-27 00:22:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33ceb80f-7b72-3e53-bdf3-71f80106431c | -15.6511 | -52.7169 | 2025-08-27 00:22:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 32fd8117-40a7-3f27-acda-aca5efb50d59 | -18.194901 | -45.550701 | 2025-08-27 00:22:00 | METOP-B | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 870ade99-8028-34a7-843e-d85c65122cf2 | -10.3261 | -55.478901 | 2025-08-27 00:22:00 | METOP-B | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 347b821a-0e9d-3c98-8685-225ff46d3e96 | -14.1245 | -45.387299 | 2025-08-27 00:22:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
