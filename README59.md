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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a920a398-696b-3ced-8069-d07252e28e1a | -8.68286 | -49.40165 | 2025-11-16 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2f97a13-7102-32c9-8588-f77da3d4d6f2 | -5.49244 | -48.00207 | 2025-11-16 04:57:00 | NOAA-21 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f1770e6-f3ee-30fc-b051-20b6275fa0fc | -10.31981 | -54.15633 | 2025-11-16 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5530e3c9-2d53-350d-9089-5529b05c8d77 | -9.85573 | -44.71415 | 2025-11-16 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c47b3fa-7ab2-3948-9d5f-52f668d45986 | -11.79228 | -45.53399 | 2025-11-16 04:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fcf6d027-adeb-3608-996d-d9b8d0cdb418 | -12.67846 | -47.16841 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 402fa24f-4cf9-3ad4-911d-392e11f674f6 | -7.21521 | -47.97884 | 2025-11-16 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 875877d1-72f5-32ef-9c88-1a2e2e85da39 | -10.66035 | -44.265 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d497e755-6f8c-3d20-ad9a-0cf13646bef5 | -7.44124 | -45.22752 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95764bb4-fca3-311d-874d-cf25857d55fa | -9.18673 | -48.84725 | 2025-11-16 04:57:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3d209e2-9703-3dfc-9154-aa1f80472a96 | -12.67235 | -47.17665 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 50ddeff9-f918-3753-a8fe-e913c388a02d | -9.72808 | -43.96559 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 944769c4-1ff1-3ef2-9a08-c4a75f0f6e82 | -13.55249 | -44.2785 | 2025-11-16 04:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1082b068-be8f-3c69-9a39-ee998ff293ae | -11.97774 | -44.96262 | 2025-11-16 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 6051bd50-657e-3160-85d0-8ab259a76da4 | -12.05901 | -48.20359 | 2025-11-16 04:57:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bdc4cb9-cdce-3fd9-bf61-3e8417067505 | -11.42102 | -43.33015 | 2025-11-16 04:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1511189-bfd1-3247-8820-5eaeb9e26efe | -10.87312 | -49.54322 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49e1e08b-dc77-35f6-9cbd-ca81aa4c9a2c | -9.71867 | -48.90304 | 2025-11-16 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f281f80a-1706-3641-a7ad-d00829c0b821 | -12.40012 | -47.56487 | 2025-11-16 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 785df992-5abc-3864-ab46-f273327cce11 | -11.90532 | -46.1985 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 878648c6-639b-3f4e-b57b-93b2474c9de1 | -10.93469 | -48.69237 | 2025-11-16 04:57:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c0c24bbc-b00f-3c14-b833-ac8a99b992bd | -11.41531 | -43.32419 | 2025-11-16 04:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 36394637-355e-30e8-a5d5-5142a76922aa | -11.91267 | -46.21847 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f45e97d8-51af-3fca-8c4c-a600e7c24fee | -12.19551 | -47.44696 | 2025-11-16 04:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 314f80d4-01b1-359e-a46a-43edd2feb085 | -10.00787 | -44.76477 | 2025-11-16 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcb9b769-2b6a-38e2-bdf8-946e95219d37 | -6.86285 | -47.35646 | 2025-11-16 04:57:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b29a81c-ecdd-3a52-9c1d-71e8a9de3f82 | -11.8447 | -47.60357 | 2025-11-16 04:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1127e5f5-8085-3b81-b161-f9027d2a0ac7 | -9.83468 | -47.08293 | 2025-11-16 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ca1e86a6-1924-3847-aed5-be072113c07d | -6.36083 | -46.15508 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f53c24a7-5e7c-3365-ac43-03ef671a8ec0 | -7.26641 | -48.03299 | 2025-11-16 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c38c77f-6384-39bd-8b9e-22107b598389 | -9.6373 | -51.76919 | 2025-11-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22222886-5cd2-35cf-a26d-905899d37c03 | -9.50702 | -47.27043 | 2025-11-16 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aa585df1-445a-3cee-9fdb-746af411acca | -7.22266 | -48.47109 | 2025-11-16 04:57:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38fdd4a1-8ae5-3c31-83bc-c42fb3e1f3e1 | -11.97242 | -44.95814 | 2025-11-16 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bb54df78-b389-350a-be7f-97fc32110dea | -9.73512 | -43.95746 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f56c122c-6dc2-3ca8-ad29-fea71ae08675 | -9.64371 | -46.02122 | 2025-11-16 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcba01e6-46c1-3539-8e5f-c8d92130b50f | -11.84647 | -49.21363 | 2025-11-16 04:57:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1eac3af-a043-3996-8bd5-eac5293a82e0 | -8.74036 | -45.64622 | 2025-11-16 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40d97e26-2121-3a07-acf6-8903fd764b4d | -8.20129 | -43.56595 | 2025-11-16 04:57:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdc23fc9-fa5c-3f6f-8efc-12d7e18e95ef | -12.40635 | -47.55462 | 2025-11-16 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39fa9696-81d0-340c-b525-40fcf2b994ad | -10.17038 | -49.31525 | 2025-11-16 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 950a6643-e793-3082-be26-5b4fd70c32d0 | -10.32313 | -54.15685 | 2025-11-16 04:57:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfd3265c-e0c7-3441-a4ed-1e3e4a0c2426 | -7.02093 | -45.16861 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee364c16-ea21-370e-be46-875e9e829317 | -12.67308 | -47.17075 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff955834-c416-3357-9e64-10e0413842c9 | -5.1268 | -55.9746 | 2025-11-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abb1c86b-48f4-3871-aa87-258d22ae6e50 | -12.06364 | -48.20428 | 2025-11-16 04:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 342c7252-e763-3c9f-baca-ae3b66501077 | -12.66028 | -46.74409 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 52c2f105-0f84-3bc3-ad32-97548030b515 | -12.68349 | -47.16905 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d7ce1f2e-65e6-3e6b-8e00-c1f41093b4dd | -12.69636 | -46.79057 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccd73f26-24bc-37af-9c0b-f03ca88e42b2 | -10.66652 | -44.79607 | 2025-11-16 04:57:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b50aff9a-2761-344e-a696-44f027a20b10 | -8.46469 | -45.14095 | 2025-11-16 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0085c25-857b-3ab7-ac56-c735a6961de5 | -12.15577 | -54.28381 | 2025-11-16 04:57:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00d5fe46-2fdf-3392-bb2a-d1ddef70a466 | -6.49944 | -52.82925 | 2025-11-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b3f11e1-bcf3-3588-b28a-5bc0b7f4f754 | -12.87749 | -46.45466 | 2025-11-16 04:57:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39e9334b-773a-3e55-8014-6abdb8c8c9e7 | -8.72184 | -49.59382 | 2025-11-16 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c358800b-9c8e-3525-b821-473ec1cdbb6d | -8.68271 | -49.40236 | 2025-11-16 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56b11176-e82d-3efd-aa1c-3c9472f4e8e4 | -9.34832 | -46.59341 | 2025-11-16 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e17145f-6d87-31ef-927b-e38a1b637002 | -7.57207 | -46.3079 | 2025-11-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a30e591-e48a-378d-8d6c-e483209bd520 | -9.6477 | -46.03112 | 2025-11-16 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88898e4e-3a8f-3c01-81aa-0e84b6056135 | -12.66734 | -47.17593 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9c154c16-b655-3121-8b8a-80e842625336 | -9.73781 | -43.95715 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5d8432bd-6cce-381d-b04f-4b9ac41840ab | -10.62678 | -44.59579 | 2025-11-16 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 82825a5f-793b-375a-b87b-3da98d22a574 | -6.71874 | -42.13145 | 2025-11-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b16de573-5cb2-3fc1-b899-a8372668f267 | -10.62204 | -44.58623 | 2025-11-16 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a44a6d71-775f-3312-9cb5-cfe611315d87 | -12.85437 | -46.42336 | 2025-11-16 04:57:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ada3a747-9589-36e8-bdc3-dc1a61254f7e | -9.72585 | -43.95587 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 26d10a33-12b4-3c08-84d2-a8054b231d55 | -7.36886 | -43.32584 | 2025-11-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20900e63-751f-38f8-8dac-9eda0a1f1b79 | -6.86913 | -47.07648 | 2025-11-16 04:57:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b97f417c-fac3-3a15-8722-daf76bb7903c | -11.91293 | -46.22328 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1b7478fa-70aa-3423-b0e8-786732989b16 | -8.86851 | -50.18786 | 2025-11-16 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a7b2155-08d4-35c8-9406-9f824d65d447 | -9.34756 | -46.59907 | 2025-11-16 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d40ba209-047a-3f0f-a65f-ef6dcc3cc0cc | -12.67199 | -47.17958 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8dc82749-ebf3-342f-a1ac-68c5f22883c6 | -10.65983 | -44.26935 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0c4746b-569d-34e5-a228-0a099b389fcd | -11.90983 | -46.19728 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a457a62-8e97-3a0a-b92b-80b975f58101 | -9.74759 | -43.95457 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be80041c-11ba-3aa0-af1a-e896110f66fb | -11.91718 | -46.22568 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75ee53a6-3c0e-3d8c-a852-b8d56b5c4ce5 | -12.67884 | -47.1654 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 314fce6b-31b7-3d9b-ad2e-8163fc40984b | -6.12991 | -48.04746 | 2025-11-16 04:57:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6457430f-0897-384b-b3ae-b50786fad2b9 | -12.86367 | -46.43559 | 2025-11-16 04:57:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0710572f-2707-3b3e-9b9c-8f1ba8975f75 | -10.66518 | -49.36108 | 2025-11-16 04:57:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0a59b2cd-9617-343b-aa1a-822268dca525 | -6.6719 | -42.03746 | 2025-11-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 68a0a2d0-09f9-3b19-92be-086a9104b492 | -7.02185 | -45.16833 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87bcfadd-2c5e-3a41-b192-3c59b0ee088c | -9.6473 | -46.03411 | 2025-11-16 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 672b2396-2cee-3b09-bdfd-313834fd6019 | -11.14212 | -44.93031 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73e5f1a9-7cf6-3986-a8ed-3f2df796b654 | -7.22322 | -48.46714 | 2025-11-16 04:57:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c139111f-17f3-3442-b5fd-48ea258076f6 | -9.64887 | -46.0222 | 2025-11-16 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83b5f550-4af6-3afb-bbbc-6eeb81047790 | -9.73836 | -43.95283 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a12795c5-d58e-35c3-8235-768de999b0d1 | -6.02784 | -48.18531 | 2025-11-16 04:57:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd8a7bd3-4d59-3099-ab95-14108b291655 | -9.57814 | -44.60794 | 2025-11-16 04:57:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 051479f9-1b02-3413-bf1d-c5ed09671ab4 | -9.72914 | -43.95678 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b9ed1740-9cec-3fdb-b8b5-01cddad412e9 | -9.85338 | -44.71265 | 2025-11-16 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c5e4f51-1a84-32e9-b76c-d38749b00452 | -10.12049 | -43.9089 | 2025-11-16 04:57:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d0c1a95-6474-362a-aaa5-879489dca808 | -12.39969 | -48.10064 | 2025-11-16 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e9e721df-4125-37ec-9d06-5f9ed026d861 | -7.0543 | -42.24838 | 2025-11-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0741e61f-b532-328a-b757-5f214028893d | -5.13085 | -55.97137 | 2025-11-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 253538d5-4f40-35fe-8ff6-765a64471448 | -7.15796 | -41.75457 | 2025-11-16 04:57:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b5d3a16a-ecee-3092-a54d-e2c81e9c4324 | -12.66306 | -47.16929 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3176cd7d-7a7b-39da-a24c-7c2c2e4ce720 | -6.30628 | -43.79667 | 2025-11-16 04:57:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 3ce7a832-8654-39af-9173-7b9b2d3d29c4 | -11.9615 | -44.95166 | 2025-11-16 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b3c411f-a6b1-3d11-9208-64110f77a44c | -9.72233 | -48.90147 | 2025-11-16 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README60.md)
