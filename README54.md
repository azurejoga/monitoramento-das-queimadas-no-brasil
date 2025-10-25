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
| d3a28991-d035-30f6-beaf-e3386801b97c | -4.6187 | -50.51113 | 2025-10-25 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5bb2d4d-26ff-39f5-9021-85deabaec193 | -10.5569 | -49.77377 | 2025-10-25 05:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3b98b8a-c5b1-3f01-9942-784f01ee003b | -3.48445 | -50.08044 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c40bcc60-2419-31ad-a9b8-93850f0a3f52 | -6.79156 | -45.42038 | 2025-10-25 05:10:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8a806937-45fc-3e68-8874-a6afa25f1747 | -10.94989 | -50.29705 | 2025-10-25 05:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb5dd969-de52-3d22-b769-8b1035781581 | -7.06612 | -47.23648 | 2025-10-25 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d41acdb1-aab9-3233-8b1d-56aaf68c3593 | -4.8424 | -50.93905 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8401a348-42d0-3e24-81d6-fe1480258a0b | -5.12516 | -50.61776 | 2025-10-25 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9765efd4-3844-336f-9911-82b86cba7400 | -8.14477 | -46.86629 | 2025-10-25 05:10:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3caafe73-81cd-35fb-8305-1c896da11d01 | -11.05572 | -48.32541 | 2025-10-25 05:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eca7bed1-1b73-3c89-9798-c75360d3f0f8 | -8.8686 | -48.2882 | 2025-10-25 05:10:00 | NOAA-21 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b3c09e6e-3b92-3696-867a-7dc61671f904 | -7.56094 | -47.11827 | 2025-10-25 05:10:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f0502969-9d3d-3287-9d94-1aa8c242aefd | -5.45311 | -45.40907 | 2025-10-25 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6beef6b0-c191-3b78-aa24-bbc1e530fe30 | -4.83563 | -50.92579 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e37fc7f-50dc-3819-8a7f-db3405701df7 | -3.25182 | -52.9098 | 2025-10-25 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9403936a-9992-3138-857f-3bca4ed0230d | -3.83277 | -50.19424 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 22d1118b-52d4-3548-8cc4-95fa9b4f8c52 | -4.55872 | -46.6812 | 2025-10-25 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 509c9a2f-6359-3aa4-8eff-5b93388ca4ce | -4.70584 | -46.44087 | 2025-10-25 05:10:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8daeb88d-4ec8-30e2-8fcf-6467ec278d3c | -6.91166 | -45.17099 | 2025-10-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2c509269-84f0-3a06-a7cb-3f4c5788dda9 | -3.693 | -49.94279 | 2025-10-25 05:10:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ead5aec-4344-396f-8933-5d3dc432406f | -8.31691 | -47.86544 | 2025-10-25 05:10:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7155e7c-2705-3ff7-ad1e-0b8bb5ecb5a7 | -3.99848 | -48.31882 | 2025-10-25 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bc929178-d6b4-32cd-a4cb-c28ee65802be | -8.64007 | -54.55553 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f11ec035-63d5-351a-ac0c-529f0ca5434b | -10.87124 | -48.04632 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e6af8312-c153-39e1-a0a0-7eb6f4bf792f | -10.46993 | -50.20947 | 2025-10-25 05:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dfce7e42-b4c2-35cd-9fa5-d4151f2ed5cd | -3.91891 | -47.69221 | 2025-10-25 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b4a02614-7a6c-33a8-bedd-6589cb136d91 | -3.92385 | -47.6905 | 2025-10-25 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 027516ee-0acb-3226-bef7-34b4cd66bff1 | -10.83853 | -48.81509 | 2025-10-25 05:10:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 818ab802-e4db-3238-a0ff-f38b0c5c6fcb | -5.02043 | -47.1535 | 2025-10-25 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d27cec5-d449-30d5-8387-297658c0333e | -11.43489 | -44.67704 | 2025-10-25 05:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| baa3c1d6-7d63-35cb-9f2f-489a0706f4ff | -6.26139 | -47.02905 | 2025-10-25 05:10:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b49196a5-e13c-36c6-822f-8b0cac6c3ab9 | -3.86796 | -50.50213 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4f56c43b-6aab-3f50-9396-323a4f330320 | -6.24098 | -46.39503 | 2025-10-25 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c653ada-7fa6-3869-8843-6ec9bff2d0bd | -10.64547 | -45.24067 | 2025-10-25 05:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 77f446d5-9671-336c-9194-13aebdd5a9a3 | -4.22307 | -48.36102 | 2025-10-25 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da8e7991-e84f-3e19-bfa1-0b47c777c08e | -5.65196 | -49.0647 | 2025-10-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 27b3029f-7a3d-3662-a98e-66a4d781077b | -8.56988 | -48.50991 | 2025-10-25 05:10:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc508b4e-fba0-3993-83a4-679c567c3738 | -10.64147 | -45.23804 | 2025-10-25 05:10:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0021b55-7515-3581-b753-c534944e698b | -10.52021 | -50.24483 | 2025-10-25 05:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ecfd151-5240-3dc1-b21e-95871c0c9405 | -6.55929 | -48.04809 | 2025-10-25 05:10:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 000a174b-04ea-3420-8dda-881da55460d2 | -11.05946 | -49.62296 | 2025-10-25 05:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 15291512-4858-316a-9dee-89ede947a219 | -6.89163 | -43.61538 | 2025-10-25 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1d911398-e546-3f74-a39e-ce8e61eebab3 | -8.56943 | -48.51337 | 2025-10-25 05:10:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 905b3e64-1b68-317d-82e3-aecbb8d0cd92 | -8.47797 | -55.1683 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b93f8b5-6b19-37a9-bb38-f53b09b4c218 | -9.45444 | -56.64575 | 2025-10-25 05:10:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bab39864-bd15-3f78-b875-f1c1f0651203 | -4.22779 | -48.60848 | 2025-10-25 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 649ed8c6-f086-3e71-80b9-78693b39ccd7 | -2.8569 | -53.91233 | 2025-10-25 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffc7ddeb-0138-3374-8f6b-9474d2534a62 | -5.02092 | -47.15001 | 2025-10-25 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74263287-579e-34a5-94e2-85c8862a7586 | -10.87086 | -48.04938 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e180f85f-0265-395b-8ee3-6252899a073d | -2.80427 | -54.38362 | 2025-10-25 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7e503895-baaf-3df0-823c-56d1c127d083 | -2.80827 | -54.38041 | 2025-10-25 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 09961813-ab89-36ea-8cff-60a13cc392d2 | -4.22656 | -48.61709 | 2025-10-25 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d8941fd6-bdb7-3fcf-b11b-0b428523f4c0 | -8.55861 | -49.86111 | 2025-10-25 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f515bdf9-71ba-3d2b-ad3a-b6524c74cccf | -8.60995 | -44.81401 | 2025-10-25 05:10:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d09bd3a-eeae-322f-951a-9554ec2a2c34 | -8.71959 | -49.60743 | 2025-10-25 05:10:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 34ff43f0-0458-3f71-91a2-d0ae6383f2a2 | -10.454 | -44.96388 | 2025-10-25 05:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0accadf6-7d12-3c33-9ef4-41876761215d | -9.32253 | -45.19762 | 2025-10-25 05:10:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bbce1641-345b-32e1-9c25-b2a9a7662f11 | -4.83383 | -50.93776 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 472226bf-ea5f-32fe-bd71-18fb730ea694 | -7.86701 | -46.73107 | 2025-10-25 05:10:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0245d571-c3ec-3247-a151-e6123396ae58 | -4.96278 | -47.59624 | 2025-10-25 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac316b4b-b578-39ef-941c-e5c9b527196c | -9.23684 | -57.17884 | 2025-10-25 05:10:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e201bcb7-2c93-3bdb-bf36-85e1d782ceba | -11.42783 | -44.67614 | 2025-10-25 05:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6bbc066d-cdf9-3122-922c-dd7209f4f983 | -5.54845 | -46.52753 | 2025-10-25 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93d4105f-f71e-3f3c-95fb-d3bbcf8ed06c | -9.45054 | -56.64883 | 2025-10-25 05:10:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5205fb20-0b7e-337e-b579-df6837a0c645 | -4.86097 | -49.31175 | 2025-10-25 05:10:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb42578c-2264-3abf-b003-cc941e31f62b | -3.78445 | -52.03016 | 2025-10-25 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc8c44c6-b3ce-3ae9-9896-05716598f280 | -4.51006 | -50.57555 | 2025-10-25 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 834cb40d-22fc-3cb6-8a29-293599901c42 | -3.39743 | -51.53475 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b911c13-dd17-359e-bd87-9b469af9fb48 | -8.71997 | -49.60453 | 2025-10-25 05:10:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f068ad15-9872-38e6-a4f4-928deca42819 | -4.81862 | -49.84523 | 2025-10-25 05:10:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09e72a9f-0dd8-30ae-8a1f-41b8a02d1d02 | -10.00335 | -47.60151 | 2025-10-25 05:10:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74cdb14d-2447-387f-8925-beecbb61f0ee | -9.28907 | -57.54485 | 2025-10-25 05:10:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6ef844d-827c-3a9c-b8da-9a9a4adb8d99 | -7.78378 | -45.39305 | 2025-10-25 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2547f647-b69c-33fa-80b9-4d6ce0510515 | -2.4413 | -57.13504 | 2025-10-25 05:10:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a2f4401-59bd-31ec-9e32-737f74206cbf | -8.72035 | -49.60164 | 2025-10-25 05:10:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4216fdf6-b19b-3e77-ac1a-5b034271248d | -6.89875 | -43.61632 | 2025-10-25 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ca3efed2-b2ce-332b-a843-7b0a6dc9d90d | -3.47926 | -49.89633 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec245de1-138e-329c-b914-24d12b0706dd | -4.00311 | -48.32259 | 2025-10-25 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1783ac44-4ed3-315e-8239-d805acd45c06 | -3.48169 | -49.89932 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ade496b8-73e9-3dbb-9142-ef38ac9094e3 | -10.00385 | -47.59738 | 2025-10-25 05:10:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c3fe8af-271a-333a-87d5-89e29b4bc457 | -9.96305 | -48.26148 | 2025-10-25 05:10:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2a40a77-97bb-3cd1-99f2-822ae46c01b6 | -8.11739 | -55.08109 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5ef8816-ee19-3a3a-a0ca-65bd728f6ec0 | -8.31133 | -47.86464 | 2025-10-25 05:10:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6abc242-a0e1-3cb0-847d-396844d19d66 | -8.63946 | -54.55975 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36c35ec9-adc3-3b7c-a778-8fa3648e18a8 | -8.34468 | -46.18745 | 2025-10-25 05:10:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c11ff131-a703-3699-b683-735e829807c6 | -11.0502 | -48.32386 | 2025-10-25 05:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6916f43-1b04-3f05-9051-42d8a3adf220 | -4.29269 | -48.2639 | 2025-10-25 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 424ef249-fe43-3d60-a423-3d63dda3c2c4 | -9.6173 | -46.902 | 2025-10-25 05:10:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f29ca1ed-3a4d-3c92-9fb4-e50630090de5 | -10.45323 | -44.97026 | 2025-10-25 05:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1e509bf-8a37-317e-9dd0-9e7b837651e2 | -9.49513 | -47.45526 | 2025-10-25 05:10:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46474abd-4d96-38a2-b37e-72a4f1bf4627 | -5.1762 | -50.12719 | 2025-10-25 05:10:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a243b5d0-6452-35ed-b6b8-7bcc9f95dff7 | -10.93621 | -48.05506 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d0d88d2-8b6c-38e2-a8d2-5fb9195f7f73 | -4.83796 | -50.92854 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e8b561f7-181f-3d8e-a564-09d89d767203 | -10.62485 | -52.19016 | 2025-10-25 05:10:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| be8d0fd8-2d18-39b6-9e98-1fababb8da2a | -5.57305 | -49.98061 | 2025-10-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22497b11-dacd-33a7-ab16-d106b9ffa6be | -11.43226 | -44.67817 | 2025-10-25 05:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6542b4f2-0385-3efd-8c23-86d2d16c6643 | -3.48379 | -49.89692 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1277a97-b178-3c7f-ac78-32e66e11609a | -6.91942 | -45.16196 | 2025-10-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e84f37f4-57a9-3f23-a9d8-6ab9218f1c1c | -4.83366 | -50.92791 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 76c1397f-7206-3bb4-a11b-5e457abbbf13 | -4.8368 | -50.93658 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README55.md)
