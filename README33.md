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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a144d03-eddd-3ab1-b932-acc9f3c9e820 | -12.68324 | -46.98226 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4805232c-943d-39fc-8a9c-fecbf38fa4e8 | -10.40899 | -53.82212 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a635fe10-8024-346d-9e12-89d64dcf73be | -11.10406 | -51.3246 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 87f2cce0-170b-397d-941c-aa258cee3860 | -10.86511 | -48.51304 | 2026-09-28 04:34:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c809f54f-5a06-3253-b9cc-ef26c573ae05 | -9.09621 | -49.89678 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95f17e0f-25a7-3004-9c7b-30fce862aaf4 | -8.44664 | -44.66791 | 2026-09-28 04:34:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df512a13-dac0-3a12-9e42-3c75c4799603 | -10.79511 | -48.45897 | 2026-09-28 04:34:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d0318b10-0e29-395a-88d3-dbf94deedc3d | -12.74293 | -47.78837 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e1a6baf-7f95-382c-9cd0-b02e9cd2d81b | -12.14319 | -50.34238 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9aedceff-9625-3e45-9db1-dc9cc91123f2 | -12.697 | -47.32258 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7d902da6-038e-3f68-98fc-89519d605177 | -7.35094 | -42.07658 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 77399c2f-1b7b-3abf-b3dc-ee664ed3af52 | -11.70431 | -44.53344 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e8c67d25-d971-3145-be38-0bd9ec61094f | -6.07511 | -57.81673 | 2026-09-28 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e17f648b-c16c-39e5-be82-1fd1edfcd08a | -7.71401 | -44.91245 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e260123a-fed3-3929-ae53-b7202ad35651 | -11.17715 | -49.86692 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bd266108-f99d-305f-a8e7-ab9c25719fdc | -12.09609 | -50.31633 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9e6f8a82-4c62-3b8f-862e-b33aef9ed2ba | -13.08371 | -47.43043 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 192f6a78-e06d-388f-b436-a17e8af6c73c | -11.69996 | -50.59808 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ef4ad421-65e7-3c84-a8b8-8794f3850081 | -10.20553 | -50.00669 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1480fc03-4388-3a2e-b2a7-b4cbd3d8fd56 | -11.54564 | -50.52412 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9bfaa601-d19d-3dea-80d8-6e57189403bb | -11.21253 | -44.78245 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37d61e42-30df-3121-b06f-4f85e90adeaa | -8.86829 | -50.67846 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fcaaf171-2039-3682-b714-825438260dd6 | -12.73972 | -47.33983 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 865e138c-6033-336c-bd2c-e77f4c7a3011 | -8.28676 | -45.41543 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52460211-302d-3fbf-8f12-f90e9f12b4ef | -7.71832 | -44.90859 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b50c6d6d-3d94-305f-ab97-c844db5ad842 | -12.68786 | -46.97504 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a5480024-824c-3709-a18f-f5b041eb0f5f | -8.22937 | -45.4823 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 033ff344-8a4c-3f3a-a2e8-e4c7c1a315e3 | -6.69664 | -59.96094 | 2026-09-28 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd930a6e-5b89-34b1-9b0f-217aeb4db42b | -7.71081 | -44.93405 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 525d0023-8042-3a9e-a133-ea833b2895f2 | -10.45747 | -45.08931 | 2026-09-28 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50caaa53-4a01-3977-bcef-9485bf783078 | -12.68238 | -45.01712 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5372e90-d8f0-3cc8-9af3-4acad67ce783 | -11.68371 | -44.53946 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02cf0ed8-e38f-36b9-b12c-43461d9f40b8 | -7.39896 | -42.62016 | 2026-09-28 04:34:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 488d1ae3-b345-333b-8931-568e47da82ec | -7.94099 | -61.52605 | 2026-09-28 04:34:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 855a7c28-faad-3d94-9ee1-db43edf62df1 | -6.09742 | -57.62265 | 2026-09-28 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e2ba6a51-7bdc-3808-97d1-dc70d170f638 | -12.67976 | -46.98166 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69d49f55-1773-338e-96bb-425f0d0fa03b | -11.10124 | -51.3202 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48d6dfd8-3c22-34c1-8fbb-8ca82ffb4f34 | -11.30302 | -55.10898 | 2026-09-28 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a153d4f4-50a2-358e-9dfd-f04585f6c6f9 | -8.57808 | -45.08996 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1002fe3b-7b31-311a-9ffb-70ba28164afb | -6.70812 | -45.59009 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8229e1ba-21a2-3501-b18b-0b2d79a9f2e2 | -11.18845 | -44.81389 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| cb4418ff-db4b-3589-905c-8074e71ef154 | -11.70264 | -44.54742 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc2c3674-d4cd-353d-858e-68a19c9a80c5 | -12.71708 | -47.28248 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8aea73f-e9c5-35c6-a85b-3deb497d2561 | -9.98032 | -50.16097 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 651feb8f-e324-3346-b238-4a6be747186f | -9.16865 | -61.40948 | 2026-09-28 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 12f1ed50-f678-3b62-9066-eca6707de076 | -8.24011 | -45.4339 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e8d00333-6dcc-3b9f-aa04-0db5018c5eb2 | -9.458 | -45.81354 | 2026-09-28 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d38d3d0-4237-3c05-860c-9f7ce918305c | -7.89186 | -45.44513 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 83133e4c-e786-3c6b-9301-d12bba166ca9 | -10.54959 | -51.44067 | 2026-09-28 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b522a5d-a7f8-326b-9114-f41344b02c40 | -12.87825 | -44.78838 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 58d49f2a-5a1d-3684-939f-7beafc6b0ce6 | -8.24789 | -45.40582 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33dff945-ef87-38af-8bca-d9fe2eeca867 | -6.99999 | -42.62413 | 2026-09-28 04:34:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e028baeb-f78a-30b3-9feb-9a5d762eac19 | -12.74189 | -47.30091 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ab2d7a97-ad84-34a9-a02d-882f35a4ce0e | -7.00173 | -42.62323 | 2026-09-28 04:34:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 77a0837b-bced-33c2-9fac-0a13fa3f94ac | -12.63503 | -47.31295 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4a22347b-2643-3d5a-af86-aef23c3a7690 | -7.82936 | -55.14039 | 2026-09-28 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abb29f1f-25a8-3d8d-864f-226fac29da5b | -11.7819 | -48.32111 | 2026-09-28 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e31ce95-3bc9-3bc5-a74a-2deba333d5eb | -9.15201 | -45.63332 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 882c2702-54bf-3ef6-afa9-20e766632c55 | -12.14767 | -50.35407 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c3d4211f-33a2-3c5d-89c3-bd68919d349a | -9.09564 | -49.90036 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8d6d9b8-b95d-365e-855d-22bc33c7d283 | -9.13001 | -45.60897 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bb4c5625-a84a-3c30-843f-0ae17b807527 | -12.74077 | -47.30856 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 230ff6f0-7f96-37d8-8d85-4820b1dd2bd9 | -9.17002 | -45.77661 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cffc3e88-892d-36f2-928b-19fab4e161f7 | -11.19367 | -44.80472 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 3a6c94cf-d0dc-3caf-831b-782d56ffffdd | -12.68625 | -45.01768 | 2026-09-28 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| be003ac5-dd32-33f4-83f8-401edb5f8831 | -10.81865 | -60.73975 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cb754bf2-8b5e-3cda-8722-777863cb68d2 | -9.68187 | -47.62846 | 2026-09-28 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7600a90-9cc6-39af-9a32-6586355ef121 | -8.96942 | -44.15567 | 2026-09-28 04:34:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 575b6a58-b31e-3af7-b5bc-647374ab249f | -13.2022 | -48.322 | 2026-09-28 04:34:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7268db16-5951-3c0d-9232-9089f7d9dc49 | -11.44947 | -44.93206 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5d78d588-5a72-3b4c-a8f1-9ee0941ac3d3 | -8.36542 | -45.46849 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1e11963-b02e-3a05-8a15-e87c6968f456 | -11.14177 | -50.04644 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f3c8dba-203a-3c31-a805-ff4f09f87ad6 | -10.20944 | -50.00367 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed7ff715-5438-310c-ba05-5ed8dc0946d9 | -7.3834 | -47.01185 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f812aaa5-c013-34e7-a616-e834bfad985d | -7.38147 | -42.11116 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5fae55d5-81f1-3e59-88fd-93f6e6cfe744 | -11.10723 | -51.34879 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e409cbba-8fba-33a1-afee-31d46ae8a11e | -11.20445 | -44.75627 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fdd7349-91df-36ba-8463-9c1764aed7f5 | -11.78523 | -48.32163 | 2026-09-28 04:34:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3e5d51c-5a07-3ba6-81d6-abd7026cac02 | -8.24559 | -44.83159 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4485561-e0f5-3cf1-bb7c-75a086500328 | -10.54781 | -51.44054 | 2026-09-28 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8303634-32f7-3fea-afcc-efd5ffd6f047 | -8.03787 | -54.89817 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c4855a77-b9ad-3b57-9096-842ed1f47c71 | -13.10209 | -47.42511 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b1af1d78-1238-3922-ac24-88514d139628 | -11.44881 | -44.93681 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ad2fdd68-8794-379a-ab2d-891aac48eca6 | -9.92942 | -60.71816 | 2026-09-28 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ecc12949-29af-386f-874a-6342b6f33ad9 | -11.14673 | -50.05817 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c74fbc24-35db-371d-8200-a693a54f0317 | -10.21674 | -49.97926 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49abbc3b-efd5-3f7a-bfae-e060397e2eed | -10.10882 | -43.94416 | 2026-09-28 04:34:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e610cc9-49a4-3b39-b6ac-f59caabad842 | -9.08512 | -49.88032 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e180d5ae-5477-35ee-8dea-a55568d9484b | -6.69932 | -59.96563 | 2026-09-28 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a24e6bc2-a09a-3628-8548-80b670895a80 | -7.40898 | -42.11698 | 2026-09-28 04:34:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 00de3b9f-b88b-35d9-8ab7-248838204dcc | -12.31205 | -46.40269 | 2026-09-28 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad08d9ab-d307-3e3c-b3e5-cb1166f8956d | -6.69418 | -45.65936 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 285a5115-9d37-30a3-a8ab-e459f58751c4 | -11.68587 | -44.52416 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 079e1347-dee7-3f83-90b3-7db9fa038894 | -11.8468 | -47.07908 | 2026-09-28 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f91447eb-2242-3658-88e0-28695189dc4d | -8.45386 | -44.68055 | 2026-09-28 04:34:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8a7d9d57-6442-36b0-8654-076c7630b7a5 | -12.72344 | -47.28236 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35dec6c9-3d0c-3631-8cfa-96f4561123d5 | -11.86233 | -47.09327 | 2026-09-28 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb787fa7-f971-302a-ac2b-0a3cd9aa9584 | -7.38327 | -42.09868 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 96db07d4-3d29-3ff8-893b-be4a3fdc94f3 | -8.90245 | -46.19263 | 2026-09-28 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42ab1d8c-0920-3ed9-8bec-225cbe94ecf2 | -8.33388 | -45.40877 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README34.md)
