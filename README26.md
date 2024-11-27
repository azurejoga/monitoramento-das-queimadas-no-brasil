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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84a0989e-bab3-3cd8-80d5-15bffa71e6e1 | -3.01937 | -48.60096 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a9e8de4-d670-323a-b032-f6bd75109549 | -3.1713 | -48.43988 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| f44d3d63-38f9-3002-8cca-7e6fa63254dc | -5.1464 | -37.74515 | 2024-11-27 03:55:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 388d58b0-47ae-3230-ab8d-604e55512d17 | -5.90978 | -43.40667 | 2024-11-27 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66ef2d59-4449-3180-800c-bd72ea5c7ec0 | -3.04608 | -48.51232 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 639c6d76-ebb2-3e0a-9772-c5dabd180507 | -2.8275 | -46.81143 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f23a004-fcf4-3c60-b280-e3f24e8b7f2d | -3.10915 | -51.25835 | 2024-11-27 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74165434-26c1-3887-9762-4d778299cf4a | -1.45138 | -47.11705 | 2024-11-27 03:55:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f0d5367-6a4b-385d-afa7-25a6ffcec836 | -3.9751 | -48.08686 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a212016d-f3e8-35e9-bcde-9fe2e73a2682 | -4.21183 | -50.90095 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 71861f8a-7d0e-367d-ab65-562b87b2748a | -4.21576 | -50.90009 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 10c46a16-25ab-34c9-8ca9-d7c4c95147d0 | -2.81471 | -46.82296 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fef706b9-4da1-364a-9c80-c2a8dc174962 | -4.01551 | -46.43993 | 2024-11-27 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9d60e2c6-2974-340f-bf14-441e33a6d31f | -5.30134 | -44.43747 | 2024-11-27 03:55:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35389034-5f79-3fac-a9dd-6fed902621a3 | -9.23936 | -35.6789 | 2024-11-27 03:55:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2c7d2406-27ec-36dc-8312-28b4fed23617 | -3.00144 | -45.46054 | 2024-11-27 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 8859838d-6d45-303e-bb1c-76046d27d316 | -1.94207 | -45.72734 | 2024-11-27 03:55:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6cbc4366-01a6-3106-9429-bcd081ae12c1 | -7.8615 | -41.0487 | 2024-11-27 03:55:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7fc8a022-ee22-3fee-bc1a-39dd6965ed84 | -4.14772 | -43.79988 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f2b752ff-20c5-389f-8a00-1deb67b18d3b | -3.17198 | -48.43568 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| a1ec629f-bd03-3a5d-b4c0-54be6fff7caf | -4.21582 | -46.25538 | 2024-11-27 03:55:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7101e12-90d7-3610-8ce3-66dc0d0ab73d | -4.14251 | -43.8036 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d206b4d9-aadd-34c1-99bb-68e0bbab8b12 | -1.94781 | -46.26078 | 2024-11-27 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ed1ad1f-eaf8-3eea-9738-97abc9e35596 | -3.2549 | -50.62387 | 2024-11-27 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d6edf77f-7d1e-338a-bbda-166cbed51e24 | -4.17781 | -48.4497 | 2024-11-27 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cca6e123-7aad-34bc-a519-21255ff7cfd9 | -2.89109 | -51.38297 | 2024-11-27 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 784e3b22-f79a-3428-8050-0468810a7f9c | -2.83644 | -46.82307 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9d20392-769a-39f7-965a-8e868e1e362a | -4.21532 | -46.25836 | 2024-11-27 03:55:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a456b0d0-b42c-337a-8fed-8d71faff080b | -3.71025 | -47.66968 | 2024-11-27 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d571f4e6-b230-34d4-abd9-f283c7c92a7b | -3.50898 | -50.31203 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17306a49-27bf-338e-afc2-a8485f62b72d | -5.98077 | -45.36865 | 2024-11-27 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 73f086e3-83c7-332e-b39b-cab08c3b0b6d | -5.36091 | -42.12712 | 2024-11-27 03:55:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 78ac58c8-e101-3469-92f0-7ea96bb49104 | -3.14751 | -48.53689 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df240ccb-bfa2-3d08-8429-c37541ce31c2 | -3.97954 | -48.07899 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 524f6190-32f5-3ad2-83d4-43ce6b6a9d52 | -2.81907 | -48.6099 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 803410c0-d89d-3a95-ae7e-c598cb878c5c | -5.74047 | -38.84295 | 2024-11-27 03:55:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2ce65d11-75bc-3911-b14c-d307514ac551 | -3.72467 | -50.18585 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f4820e07-9a93-37a1-8176-c53110dcc7e8 | -5.19807 | -48.18401 | 2024-11-27 03:55:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33e37810-4030-3beb-b086-703e95d76fd1 | -3.58306 | -41.9568 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c393d157-b10c-3da9-a3fb-5264547c17e1 | -2.69424 | -45.65737 | 2024-11-27 03:55:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b931f9db-040c-34f2-924d-bc1edb075306 | -3.57751 | -41.96662 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ffb8f135-4e88-35ad-884d-0723b73580af | -3.98146 | -48.06792 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3551463b-dcdb-3319-a1fc-a7c7a8e3fa10 | -3.08847 | -41.14465 | 2024-11-27 03:55:00 | NOAA-21 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7e4cfa6c-db6a-39b3-b35c-6b4b42a277a7 | -2.01978 | -46.3816 | 2024-11-27 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7e33577-ce97-3a59-9182-6b920986c24c | -2.92214 | -48.6345 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29f872c9-f6a2-35ce-9e61-5891704af3bd | -6.82779 | -44.39626 | 2024-11-27 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| df188b0f-e3f3-34fe-84da-541a9e6be995 | -4.8118 | -46.84536 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cc1b956d-d929-34af-b6c8-c3ce6e222e85 | -6.53693 | -40.79258 | 2024-11-27 03:55:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| daa4e348-b404-3ed4-b7f3-f783eff1aa0a | -3.09389 | -50.35935 | 2024-11-27 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7fdc192b-6ef3-308b-82b5-ddacb5a86d48 | -3.72549 | -50.18238 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b2aa0c0-2079-371d-9516-0817c11cbf8a | -2.92887 | -48.63095 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6850f897-abc4-3f3c-bd8f-d6bbe01ada7b | -3.16613 | -48.43473 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 9c636911-c2c5-3045-848e-c8be0198c7eb | -5.36568 | -35.61871 | 2024-11-27 03:55:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 104cbc07-4d6a-3910-97d2-8268bd1a2694 | -4.67264 | -46.38429 | 2024-11-27 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f7a003d-b89f-384d-b173-b63406430a73 | -2.83428 | -46.83614 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 154955a5-c5c3-381c-9f70-164f154d52ef | -4.21395 | -50.88925 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| a4be634a-e69d-3e6e-bd26-4e53d629d87c | -1.5115 | -47.27135 | 2024-11-27 03:55:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12f05d14-4ad9-3d1d-9036-142d095d5642 | -3.96953 | -48.06974 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51c47a00-10d8-3564-9c3d-c1647de447bb | -2.93855 | -49.12864 | 2024-11-27 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6c1ce19-6a97-39d1-a389-0849ae9a1d57 | -2.54938 | -46.40896 | 2024-11-27 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3abe4a6e-ac8e-383b-866a-c09a16aa4de2 | -3.16682 | -48.43052 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 060d24e4-35a9-3ac2-bfcd-f993fa2fcb01 | -4.21574 | -47.21835 | 2024-11-27 03:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b86d66e-196e-320e-8dc2-a09bba56b35d | -4.58936 | -44.80934 | 2024-11-27 03:55:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e37f7463-788e-39c0-b43f-4e1a7d1b94b1 | -7.11715 | -38.97942 | 2024-11-27 03:55:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| da27c8e5-0375-35e2-8f1b-2c299f2c39ee | -3.81108 | -47.47342 | 2024-11-27 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e8a4e33-330d-3869-90d8-216d35058f54 | -6.63258 | -43.86301 | 2024-11-27 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d24773e-e9ef-32f4-9945-7a00f7d22488 | -2.57233 | -49.0961 | 2024-11-27 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e7f9f527-d4be-3680-9ca7-9362136a9d4a | -4.21782 | -50.88826 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 77ddff5e-7ebc-3e33-923a-16d0bb9c97cb | -5.36628 | -35.61472 | 2024-11-27 03:55:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 133eab08-83ca-3a7a-870a-adaac76a1b53 | -4.72392 | -46.56992 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| aaff0417-04e6-331c-9f60-5b14d644edb2 | -3.97187 | -48.08972 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 145b8076-37d8-3344-bc75-381573906082 | -1.94751 | -45.72527 | 2024-11-27 03:55:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5d5a5cff-022d-3d69-9bc4-b2d9ff22ff99 | -7.07596 | -35.26435 | 2024-11-27 03:55:00 | NOAA-21 | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7e13e83d-3827-3c12-9153-468a24bd5121 | -3.51648 | -50.30764 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ff7ea93-eb38-3ac8-83e3-db90877e7c06 | -3.57777 | -41.96541 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7a7850cf-37a3-37ce-bc61-fc0d33146c3c | -3.58231 | -41.9614 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0aec3e5d-5104-341a-849f-b96ff774f222 | -3.96877 | -48.08995 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 43b387c5-2e12-3b3a-aa40-e6e9eb9b2f91 | -4.72315 | -43.25447 | 2024-11-27 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55d36062-ff4f-3b17-b838-c8e2f0362151 | -4.24585 | -48.67948 | 2024-11-27 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 69c6a08f-b211-396d-badc-c1da22aad328 | -3.97947 | -48.06048 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 423a7356-90b7-391d-ba6f-322b22d50316 | -3.27122 | -43.03955 | 2024-11-27 03:55:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1b57449-9de3-36db-b183-f19c93e6340a | -3.71709 | -47.13115 | 2024-11-27 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d2f689e-573e-3fc0-afdc-63e2f0af9c0a | -3.04679 | -48.50803 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| e4a7c658-2024-3514-9199-b63cfacf00a2 | -3.57551 | -41.95556 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 301b408c-606c-38b6-95c3-6e014a58cbe7 | -2.99124 | -45.46629 | 2024-11-27 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e81ba1e-4961-34bf-a1cc-71f26532eb05 | -4.24658 | -48.67526 | 2024-11-27 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 970caa5f-0b80-39e3-ac60-9ce354ff1a8f | -3.71783 | -51.79992 | 2024-11-27 03:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba35df0b-4dbe-338c-a75b-9a4eb1c89f0a | -2.28303 | -47.39503 | 2024-11-27 03:55:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22e82fcd-bae0-3e12-b1e8-ea4012d9ffd6 | -4.01842 | -47.65517 | 2024-11-27 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 486cb988-e231-3d24-90ea-08d8a08e8218 | -3.18322 | -48.4341 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c4cad387-ad62-3fc7-aa06-e03355ae0b89 | -3.99631 | -43.25587 | 2024-11-27 03:55:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7dfa4bb9-63bc-3a94-9004-54d695402b99 | -3.81709 | -47.47096 | 2024-11-27 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e009f3fd-b15d-375b-8946-12b23cd17040 | -3.94084 | -46.89239 | 2024-11-27 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f8e24a2c-4a73-381a-a5cb-7152202f53ad | -4.27291 | -42.44074 | 2024-11-27 03:55:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 52564317-96e8-3adc-a847-b431ba98d385 | -3.89105 | -46.10022 | 2024-11-27 03:55:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bf24f551-47e9-36c0-88d0-cc9a7accc386 | -3.7182 | -50.18476 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 331bc78d-1a90-379a-bee6-ceb87cf1f46e | -2.79273 | -48.6008 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37f75c02-0807-3d88-b3a7-5142d8daa36d | -3.97714 | -48.05933 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 981e59b9-0b35-36a6-b99e-7c35b0692240 | -4.61203 | -44.24137 | 2024-11-27 03:55:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12d17557-55ae-3178-a944-b9b462a39375 | -1.52069 | -46.07289 | 2024-11-27 03:55:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README27.md)
