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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d766682-25ac-3be7-9212-344dce6598bc | -3.04618 | -57.48833 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c2f9dc31-d2ac-3d24-b664-b908401c9ce4 | -8.28662 | -50.26626 | 2026-10-08 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2f588286-2949-3c5b-ba61-f5cc1e460800 | -2.94031 | -54.16319 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e238c45-87d3-31a4-93bb-d7eb38514778 | -8.92095 | -47.45307 | 2026-10-08 04:46:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b07349ae-c35c-3cd1-8acd-8a43f7a381bd | -3.04984 | -54.1497 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb9f468e-5223-39fb-9e29-e6cf671a79ea | -2.88219 | -54.12243 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 98cac81e-111b-35ec-9de1-800406767a44 | -3.50069 | -51.6831 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3d14593-1de5-34f8-89ac-f5360b4a2c98 | -2.99247 | -54.06605 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8c6d99a0-c662-3eae-be65-6944abbf7a2d | -11.2252 | -45.24672 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 455b0695-4457-3321-9f24-abd76548ec4e | -6.95352 | -45.26972 | 2026-10-08 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4bd9d49-89fa-3e36-ba48-f55470d6b71c | -3.27649 | -54.04856 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1f775bf-19f9-3501-bb16-7534fea98b08 | -2.58139 | -56.15796 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8178c19-895b-38cf-b3ef-3138645cadf2 | -3.27033 | -54.68291 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d7423a90-ef6e-367c-886b-df7b15b3d04b | -3.10862 | -53.78158 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 316920f8-2f70-3d59-b490-a112db79b44c | -2.50263 | -56.16171 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 618be077-c172-38d7-9757-56e26e952457 | -4.12695 | -50.81744 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98a83a8c-96e3-3295-82f1-297194a3d468 | -2.78529 | -54.07219 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3846e735-be49-3c31-90b1-98fe2f6b5721 | -6.08699 | -53.49817 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b3f3230f-0de2-30d6-a7c9-db553c438900 | -3.28576 | -54.01473 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc091522-005a-3b50-8362-139cc258b78c | -4.77211 | -55.73249 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96622bfd-5850-39d4-8c71-7abd1ba9a024 | -6.04254 | -53.48732 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5da85de0-8402-330f-92b0-237bb8141ff1 | -2.96996 | -54.11191 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f7fc87a-5ea7-32d4-81ee-e7a3c7f0b018 | -4.80759 | -42.75099 | 2026-10-08 04:46:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc4788d4-7bd0-3d79-a1b9-53449221e684 | -4.06559 | -55.32773 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29dc231a-6810-3ab3-a5d2-7dd8f678af5a | -10.87955 | -47.60601 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25f458ff-bd99-3be4-830e-661454443e3b | -3.05755 | -53.9169 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 873020ac-372a-3f3e-a425-a5e5f3b497ac | -3.04968 | -54.26801 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a7384293-0be4-3d7d-aecb-b862e43ab38b | -3.03003 | -54.06742 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b677c818-b6da-3d0b-90cb-babb3045a6d5 | -3.05909 | -54.20987 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 137be666-abd8-3728-a09a-429ee0eb2498 | -3.27733 | -54.06644 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2498a570-8305-3bde-9cb1-b5d9e75cf58e | -10.99762 | -45.41508 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bd823fc-a933-3936-9a84-a3ca642c8b55 | -2.91227 | -54.10017 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7177c4c2-8ae3-3765-b05a-a6918dd672f7 | -2.48195 | -56.10185 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 11eea928-6a2b-310d-88d0-237152398c9e | -4.2978 | -48.61175 | 2026-10-08 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73c5c86c-8cfd-3ecb-84da-10923e3bf191 | -3.59753 | -54.67606 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8af1e3af-6389-36b7-bf1e-1e1fbe49c1ef | -3.31525 | -54.04137 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0eec13e3-4a23-34bc-ab50-8f90bb44acf8 | -5.86014 | -53.46609 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15a87335-8fda-386a-95a4-2ceaafc4d087 | -3.29534 | -54.02507 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32fbc37d-0530-3e3a-b061-45896d1d081f | -9.93132 | -48.78571 | 2026-10-08 04:46:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8169c08c-9efe-3ad6-a726-2c9bf12143c7 | -3.27875 | -54.05775 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb8309ac-e3e8-395a-9d07-099d098ab1ee | -3.01525 | -54.13689 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb8cdceb-0c61-3654-834e-076005f66d99 | -5.23905 | -48.40109 | 2026-10-08 04:46:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4da36ad-0393-36b9-a0bc-0f43ac35008e | -3.55978 | -54.478 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d050145a-a0d3-3b7a-8e69-f5770dffba13 | -9.90976 | -44.79487 | 2026-10-08 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afa701a6-90d3-37bc-bebb-b8fb910ddd7e | -3.27687 | -54.07231 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 822ec707-7556-32ae-b3c5-b6df19ff3e74 | -3.04297 | -54.26233 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c9cc64f7-9e42-3dab-82d0-cbb9a9193ec3 | -4.56398 | -54.21068 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 582693af-0160-314a-9c8a-0391e7fa4596 | -3.00332 | -54.04542 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f43dc77-5061-3f78-881d-05adcb3b4226 | -3.65437 | -55.50647 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ae4e596b-9dd7-3e52-89f1-14e8f0b21818 | -2.56977 | -56.17633 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 91c0ed8e-e27e-3560-9859-ad4617d0b23b | -3.31387 | -54.04997 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| adb2640f-c956-3098-9f50-cc7dd0646de7 | -3.57328 | -54.48956 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 794cec15-663e-3625-8252-29e1498f0f7c | -3.02559 | -53.92952 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b736614b-466b-3a33-9685-313875c9e595 | -10.26603 | -47.78164 | 2026-10-08 04:46:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e32dff72-9278-39a8-94cb-15b84913e889 | -5.75171 | -42.06081 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| af357ae7-2203-3cc7-a2c1-8a40b704c258 | -2.46209 | -56.09077 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3218143b-0ae4-3d37-a5c6-77c8a779193f | -9.5478 | -40.33985 | 2026-10-08 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 71ef61c5-b5dd-3e18-8207-bb35df4bd5a4 | -4.15609 | -55.13955 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b03256d-507e-3060-b16e-a9abe04485c6 | -7.90236 | -54.71326 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63523bde-ac92-3882-bdba-f07cc241fff4 | -2.46335 | -56.08296 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 61f08360-cab6-39fa-bd24-74224d35284d | -2.98897 | -54.0879 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| acce78d4-392f-3194-b072-73084b564b2f | -2.94501 | -54.06041 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73516752-fa90-371b-8ae9-e47c587a6345 | -2.8643 | -54.21049 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4800409e-74c1-368e-a124-77dbaf90c887 | -3.30964 | -59.60876 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7faccaf-b3c0-34e9-bad9-ba7d1d7a6904 | -3.02832 | -53.91238 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 876eacb9-ffaa-3d04-9204-49f83148ff00 | -9.51636 | -54.74676 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6917092-ee89-3525-afa5-68e00ea7de70 | -7.89301 | -54.99784 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e56f9600-6bc8-380e-b4dc-0bfcfec49ecf | -4.78175 | -55.72353 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 781d4bca-b8a9-3b6e-b04c-6d81bc447582 | -3.08312 | -54.24997 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8105424f-6cf8-357a-9333-9c0d3542c234 | -7.88278 | -54.99173 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27357a5d-a259-38f9-bdeb-9ec267a8d9bd | -5.88023 | -53.62002 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b77c0756-8a40-3c6b-afcf-0c389b6c7c23 | -4.66342 | -56.21663 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e48c8a9e-6354-3712-aa75-1378349ecd83 | -6.84011 | -42.29441 | 2026-10-08 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0ae6675f-c4ae-30a0-8f3e-a10fde446e77 | -3.05211 | -54.15908 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce5ce419-69ed-3d1d-a361-22cc1dd85a2d | -11.11033 | -47.70668 | 2026-10-08 04:46:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8016e58b-2322-3d94-acea-778e1a163034 | -3.00631 | -54.05034 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d6a725f3-b29f-3063-909d-00a4352707e4 | -9.5472 | -40.34478 | 2026-10-08 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 19.1 |
| a68a86a3-35b7-3476-ab4e-3c69d885eb0b | -8.71751 | -45.19473 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d3bfd293-c09e-38ad-b661-adf7a25599bd | -5.2923 | -60.10615 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2dd8763-d296-37e7-bfeb-9444ae8befdb | -5.11416 | -47.1224 | 2026-10-08 04:46:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 274ebb8b-822d-3c0a-a882-8ce84c9ef12e | -6.51286 | -55.38354 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 744224cc-eaae-3c36-9388-1c2c7a3aac5b | -9.72264 | -57.73184 | 2026-10-08 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 736a6b1a-58e7-3aea-b291-869a96d98638 | -11.72151 | -43.65643 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d09d033a-880e-3e28-99f0-8fe0651b6580 | -3.01042 | -54.0957 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 7c520abc-7a4e-31d7-aa72-fd9a87451d82 | -7.21594 | -55.16881 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1fcd7ad1-81c7-3bcc-ab38-0fa35063b328 | -4.06861 | -59.83871 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f9f0d088-ae96-3685-8310-2dd038c2d7a3 | -7.03263 | -45.44124 | 2026-10-08 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98360de6-fa08-35d6-89c4-fa199a62601c | -4.75171 | -55.65931 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| dab90af9-fabc-3618-ab0a-ad9b6fc52468 | -3.48082 | -59.58349 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c151c7b0-1470-3333-b17a-38573e5616c4 | -3.63275 | -55.5137 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ecc13438-795b-37f4-bb8c-411860003d5e | -4.42934 | -59.4921 | 2026-10-08 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8400256-476f-3e51-aa3d-4b21a6ea20a8 | -3.11342 | -53.78106 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ee8a9af3-ccb0-3ac2-8984-444cc4693669 | -8.06955 | -55.29717 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 876546a4-7e9a-3646-b478-0978e2e44e16 | -2.75326 | -54.03585 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 15023a64-d802-371f-b9a2-1f2925b36620 | -3.09414 | -53.73196 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9e64d32-1d95-3b91-aa2b-ef2a25a2ba1c | -2.77297 | -54.10186 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a264771-7cf6-3f46-b218-dc1a681793e0 | -3.27366 | -54.06586 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c827c1fe-55f8-3763-9b19-dc451005c29c | -8.45535 | -49.33827 | 2026-10-08 04:46:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27eb1307-e317-3d69-ab60-9eb012c9d439 | -8.214 | -46.37344 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ca2ef28a-4a8a-3a34-96eb-6fcb2bc17fdf | -6.99384 | -59.12288 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README108.md)
