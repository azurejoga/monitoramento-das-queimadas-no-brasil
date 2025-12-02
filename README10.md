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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2366acd4-b6f0-3aa8-a8f4-ad21a1002b74 | -10.76508 | -44.94062 | 2025-12-02 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 230e072b-1801-3c6b-946c-0b0f806c3c6d | -5.17384 | -44.80216 | 2025-12-02 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1347e109-b4f7-3b72-8495-ea22789e8975 | -8.04747 | -43.09761 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f1a84932-4f41-3a3b-a65a-1e48b40dca1b | -6.68736 | -43.54933 | 2025-12-02 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 23e841d3-bedd-3bbd-bf73-c762f48815b0 | -8.05587 | -43.08804 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7c781cdd-37d0-3840-8767-eb9ee4bdfccb | -8.16168 | -43.17007 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9e2af51f-23e6-398c-8078-4e3e32868d80 | -5.11557 | -43.29061 | 2025-12-02 04:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ee540b5-c510-3e31-9c85-9cdea7646a0d | -6.67036 | -38.91099 | 2025-12-02 04:08:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b482bb7d-a746-35fd-8773-f22f5833b67f | -8.05473 | -43.09513 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 5ea3b6fa-3422-3a7e-aa04-9aee10659543 | -6.6802 | -43.59391 | 2025-12-02 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74729502-6b63-3730-9103-73bb49931c62 | -5.43366 | -46.36136 | 2025-12-02 04:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2fa4db9-f54b-3de6-86a3-a2fdf55d0645 | -4.83938 | -45.35754 | 2025-12-02 04:08:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cd709fe-a337-3887-b7e1-ffdfb62c36af | -8.05416 | -43.09868 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 5f072c41-5ee5-3610-9828-9dc5c471f81a | -8.04413 | -43.09706 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c9df20cf-c84e-322a-bc79-214c280e4cb2 | -4.38293 | -40.70887 | 2025-12-02 04:08:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 321ad9d6-f1b8-357a-b637-9cbca1a5392f | -5.3338 | -43.56756 | 2025-12-02 04:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3ee5cb0-874c-3df6-87dd-103d24c53c02 | -5.1658 | -44.80529 | 2025-12-02 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a81555a-de98-305e-830a-099aa7a2ef1e | -5.07738 | -41.79734 | 2025-12-02 04:08:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ee4c6d68-738c-3998-bb83-142a0c41f8cd | -6.47626 | -43.55351 | 2025-12-02 04:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8db0d5c7-a16d-3402-9a86-392aaa3151a4 | -4.0178 | -46.44734 | 2025-12-02 04:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5677e0d3-fdd9-35d8-9edf-b588c1329861 | -8.05637 | -43.10632 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| bdcebb74-b164-32da-8f6c-413ca1b750ed | -10.11825 | -38.35588 | 2025-12-02 04:08:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a9bb49a5-dae1-3824-9449-dfc4bc9cfd19 | -6.2841 | -39.68572 | 2025-12-02 04:08:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6aaef072-0a9b-3c96-b556-48f7ea1a22ed | -5.35123 | -44.88518 | 2025-12-02 04:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ee1862e-4411-3483-98fb-ab813ce8b999 | -8.6723 | -44.22194 | 2025-12-02 04:08:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9496150c-7952-393e-a3bc-809b56a33d6b | -4.37849 | -43.14186 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c041656-9bfa-352b-abef-b357b4d5f5f4 | -4.53194 | -45.66463 | 2025-12-02 04:08:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3595cc60-eb7b-3ab7-bfdd-2b7db6c2114c | -7.91146 | -43.78985 | 2025-12-02 04:08:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7cde4820-87f3-3f13-8034-b83240bdd0a8 | -5.1184 | -43.29488 | 2025-12-02 04:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af50e270-caa6-3534-9305-5b59ab8656bc | -5.17017 | -44.80156 | 2025-12-02 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9e70054-f275-36fc-9ca4-9810d560c95b | -11.16898 | -43.57215 | 2025-12-02 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71ffb556-75bc-3355-9342-f6ec566dc91a | -10.11743 | -38.35797 | 2025-12-02 04:08:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c009dd13-a81b-352a-8606-e1ae5d8b4fcf | -3.38475 | -50.00774 | 2025-12-02 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a787433e-3f38-3c63-88eb-c7ecc315ddb9 | -6.36113 | -46.15191 | 2025-12-02 04:08:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2f32c57-1ea8-3be6-97de-73a330f87013 | -2.96315 | -48.59229 | 2025-12-02 04:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19cdb7ce-bf04-3ab0-b5bf-d55c30470bd2 | -6.54574 | -41.70832 | 2025-12-02 04:08:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 41b8d549-3b5b-353c-83a5-8e85e64fc7c7 | -4.38192 | -43.14241 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b66c61a-5966-375a-8c77-c62a648e3ada | -2.70117 | -51.89877 | 2025-12-02 04:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c0eaf9a-e196-3644-968f-7eb09c107ecc | -4.38398 | -43.1492 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90dd3c1b-7a23-33b4-9521-5d5284efec46 | -6.28354 | -39.6894 | 2025-12-02 04:08:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ed68592e-add4-353e-90f1-8e285214d2aa | -6.31161 | -43.81324 | 2025-12-02 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e0d3c8a8-9040-3971-b1ca-b35066ef023f | -4.21886 | -44.31595 | 2025-12-02 04:08:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72dc41e8-f36b-3fba-9473-2cd298e50db1 | -8.32392 | -43.82159 | 2025-12-02 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5d517770-f578-35c2-8278-73969273fedd | -6.55789 | -43.84752 | 2025-12-02 04:08:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c686299d-70bb-3286-a021-35ea8e3af2e1 | -5.33097 | -43.56319 | 2025-12-02 04:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f948a63-aa51-342a-b98e-accaa4e91867 | -3.98653 | -46.4572 | 2025-12-02 04:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0091fb31-4f01-3c72-9141-cc791b467743 | -5.62404 | -44.89114 | 2025-12-02 04:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db739cc6-81c7-37b6-886d-c53a9f149014 | -8.05245 | -43.10933 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d2a38a3f-4845-34ca-988c-e3003dda686c | -8.38646 | -36.05462 | 2025-12-02 04:08:00 | NOAA-20 | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 6440a0e9-8fc1-3292-a5cf-a16685d72340 | -3.38532 | -50.00439 | 2025-12-02 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8921c03c-b288-3019-aa62-6dd486d1e08a | -8.04911 | -43.10879 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 37e511b1-a201-3f45-9f1f-1263b8ab6e97 | -8.16373 | -43.22166 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 32a0aae2-512b-3ed8-ba28-aade46593f87 | -11.16841 | -43.5757 | 2025-12-02 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b027ff6-feda-3ee1-978a-6f580214c855 | -4.38673 | -45.49357 | 2025-12-02 04:08:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 79072898-c934-3af6-bba2-f87e696022dd | -4.38594 | -43.13923 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 107754a2-1df4-3e7e-b1e2-87449cec3a28 | -10.48133 | -36.85125 | 2025-12-02 04:08:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 68f9ccd7-9af7-36a9-a814-8fc87c6ccbbb | -4.19166 | -44.76035 | 2025-12-02 04:08:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b479a86-1ad4-318f-a3bd-ae51601de614 | -4.38417 | -43.15042 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75f9b8e8-4d86-3872-b436-8518470c1474 | -8.05139 | -43.0946 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 3b344877-efbe-3288-a207-5b236ac2d702 | -7.90865 | -43.78558 | 2025-12-02 04:08:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5144d9c2-a1bb-33d7-96ad-379883e14e98 | -7.82419 | -42.94156 | 2025-12-02 04:08:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 03a76deb-f5f8-3880-abac-fbda395d9738 | -4.38862 | -43.1423 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d8b0a2fd-3572-3873-9fe7-f35c47fa1358 | -10.47712 | -36.85074 | 2025-12-02 04:08:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 463a12a5-3cfd-3f2c-9c93-2a2ebb72ada3 | -4.22247 | -44.31654 | 2025-12-02 04:08:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fa1fb0a-d781-3b9d-857e-4c048de06236 | -6.62163 | -43.86981 | 2025-12-02 04:08:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f7c5afa-5241-3d6d-b7da-70180fee2068 | -6.31506 | -43.8138 | 2025-12-02 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ce0b03d-d463-312c-86d2-1938a40a3591 | -9.71109 | -36.25414 | 2025-12-02 04:08:00 | NOAA-20 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| f84293f2-aa86-3be2-bbe1-e0d50f187120 | -7.91206 | -43.78613 | 2025-12-02 04:08:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6cab52e8-032a-399e-834a-9eb000f3b3e5 | -11.17174 | -43.57625 | 2025-12-02 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ab32e69-15b8-3bce-996b-c8e659f50300 | -8.05082 | -43.09814 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 51040d1a-0577-3a26-8ec4-dd0318078c73 | -7.91486 | -43.79042 | 2025-12-02 04:08:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e635840c-787d-35c9-9e7a-805a37c67e23 | -3.45595 | -50.00629 | 2025-12-02 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 737b7785-1f92-3035-877b-27ae5fdd9ef3 | -3.31619 | -52.54021 | 2025-12-02 04:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 53309983-e6ab-3908-9b12-eeb345442458 | -6.68312 | -39.50768 | 2025-12-02 04:08:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0e8930de-65b8-3044-81d6-c0cf61b77324 | -3.57289 | -50.29755 | 2025-12-02 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 817e1769-79f0-323d-8f04-a28da5bbdc94 | -8.05302 | -43.10577 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.0 |
| f0e88298-96b1-3ab0-8fa6-591913573830 | -4.38074 | -43.14986 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92400305-d555-30df-9d83-31c534ecefea | -5.35194 | -44.88087 | 2025-12-02 04:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2eb53e9-4d96-3874-b233-cf76f1b3cae2 | -4.4344 | -43.8617 | 2025-12-02 04:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b96b3e6-e116-377a-8d53-84f7c131ce3d | -7.34665 | -34.89274 | 2025-12-02 04:08:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 79c4f49c-7ccf-3b43-9bd7-8795c3d67958 | -4.37731 | -43.14931 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d941f24-3a3a-3eb3-9812-ae6f83aac83a | -4.38458 | -43.14547 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 378d7fca-caa3-3d0e-a74e-5d752636a3e8 | -5.43308 | -46.36481 | 2025-12-02 04:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed5d6e91-d1e0-34b1-935f-e81e1513533f | -5.33933 | -35.55085 | 2025-12-02 04:08:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ed36c586-e1f6-32dd-b331-62b4db7116e4 | -6.54519 | -41.71177 | 2025-12-02 04:08:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 29a3f7b0-2421-3c5d-a460-865034108486 | -4.38476 | -43.14668 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b72c7615-877c-33d9-9e8a-53b291a944bf | -8.17378 | -43.22332 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1300be57-900e-3f10-afbb-287e7bd29e4f | -4.01162 | -42.45222 | 2025-12-02 04:08:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6dbba943-28c4-34c9-8d99-27d668e30e63 | -3.4741 | -51.36955 | 2025-12-02 04:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 261e39f8-1637-357a-93df-c5a30cace0c4 | -9.32371 | -43.08562 | 2025-12-02 04:08:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d55e5cfc-f14e-3acd-be43-177987d8bbfe | -4.37403 | -45.5957 | 2025-12-02 04:08:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6501d213-e327-3500-b560-5b80bbea2e2b | -8.04918 | -43.08697 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ffcd6e90-4a34-3b0e-ab24-191ae9887a32 | -6.47566 | -43.55724 | 2025-12-02 04:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a8280b2-2cee-320f-8a7d-393defc3e606 | -8.16111 | -43.17364 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e830121e-79ec-335d-bb6a-48986e32a3f9 | -8.05694 | -43.10276 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 57ebc292-a8f7-3f09-8466-697772b22599 | -4.37388 | -43.14877 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e2733e9-6e31-348d-9ae4-e9a0040e1d6a | -8.04356 | -43.10061 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| a760ce39-87ed-3f49-a02b-d18ad385374c | -4.22179 | -44.32073 | 2025-12-02 04:08:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73490f97-e6d1-3593-8946-701f9b13fd81 | -8.02562 | -38.05282 | 2025-12-02 04:08:00 | NOAA-20 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 69fd1614-4eab-33ef-a7e7-36cce1ceafec | -7.82476 | -42.93803 | 2025-12-02 04:08:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
