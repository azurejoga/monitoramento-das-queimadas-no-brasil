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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a30caff6-92c7-306c-be56-57a6aa32e757 | -7.03464 | -55.49881 | 2026-09-11 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b21cf237-531f-3c8f-875d-41613b942f0e | -8.78054 | -44.18267 | 2026-09-11 04:51:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0531355c-5880-3f5b-ba9b-fcd526671359 | -3.97278 | -53.43597 | 2026-09-11 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8ab9323-5f8f-3a40-b537-24b5da74117a | -4.02284 | -50.45565 | 2026-09-11 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f981d93f-f9c9-32e2-bc73-ecf843b159d5 | -3.37317 | -50.75927 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff4d327e-1dda-3761-8168-7541aa1b4e5f | -4.17411 | -48.7062 | 2026-09-11 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd8744fb-022e-364d-8317-f0388888a4a9 | -2.67914 | -57.5097 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d237357-a5bb-3d67-9672-cae194c82898 | -8.48227 | -54.94336 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eaa240fa-df4c-301c-b178-3e1ac9e73bd7 | -5.28037 | -55.96307 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68fc2054-16b7-3577-aa38-cb750e1da7d2 | -3.37262 | -50.76283 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d17e343b-6d00-3f83-80f5-165cfc5276cc | -8.51056 | -50.15324 | 2026-09-11 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 505f795f-e4a8-3954-a169-27b096406ae3 | -3.37988 | -50.76029 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51789717-feac-3f21-b569-ece651d8e8d8 | -7.80981 | -42.78133 | 2026-09-11 04:51:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ca2d0d56-209e-34c0-87cc-d4972ae91aa3 | -7.76295 | -44.57851 | 2026-09-11 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af76422c-a491-343e-a8f9-feffd83c5160 | -6.19186 | -57.7547 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56a3c624-3af9-3418-87e5-848a64d2f793 | -4.86022 | -56.01079 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c45eedf-5fc8-38bd-a63f-be227682c699 | -7.92997 | -49.7334 | 2026-09-11 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 254d585f-08c6-35c9-a2ab-386fccfe5ef4 | -2.94292 | -50.45917 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74647cb2-fbae-3e6d-8339-264e749c69cd | -6.1931 | -55.27211 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cc899c8-531c-3fc9-82ef-ac68abcd02a9 | -4.08367 | -56.30283 | 2026-09-11 04:51:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 008a2210-cff3-3871-82ba-640e7b04fc74 | -3.24801 | -50.82039 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cb22ac8c-3afa-346b-8b0a-34b3415d3abd | -4.30465 | -49.10131 | 2026-09-11 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b6426902-6042-36fc-9bec-9fccc5d2e42c | -7.97053 | -43.99843 | 2026-09-11 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 516a64c8-18f6-30c8-ba76-c780d38789a5 | -7.96964 | -44.00493 | 2026-09-11 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1706c9ee-8589-34c2-82a3-f660549c5023 | -8.58305 | -54.55056 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f30751b7-b2f2-3726-b997-c94c94407c2c | -6.50455 | -58.38588 | 2026-09-11 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf174830-bf27-35a6-8d65-9bbec6031ace | -3.07322 | -51.33491 | 2026-09-11 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 84b91822-8fa6-3992-aa46-7414c6ba33e3 | -3.37934 | -50.76385 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| babfb4bb-d73f-346b-b2f4-1bf89b412050 | -4.52151 | -54.95465 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4238821c-7381-3a20-8b3a-ac128e9831a8 | -3.06702 | -49.51704 | 2026-09-11 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4b8869a7-aca0-3f2a-96c0-fda8cbac7e59 | -8.48631 | -44.74189 | 2026-09-11 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2de2f64-9205-36db-9830-b01c720c751e | -3.07653 | -51.33542 | 2026-09-11 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 96b510a7-266b-3ed2-8b44-89f02ef143d7 | -9.32517 | -45.65075 | 2026-09-11 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8297611c-913a-39d4-b3d6-c1b1eec5f843 | -6.79733 | -58.89576 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc822cdd-28a0-3b38-a4cd-030ea19db326 | -7.15724 | -44.74573 | 2026-09-11 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7556a07-ccd2-3cff-8353-bebe653132c0 | -8.9365 | -50.26998 | 2026-09-11 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6ab2502-c0b0-3f2b-b672-cee533ad44b9 | -7.62014 | -44.72423 | 2026-09-11 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec0e145a-07ce-3668-a31c-e2ae640d4497 | -7.72025 | -44.62547 | 2026-09-11 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23cca933-ae05-3198-ad50-7b14059598a6 | -5.76713 | -45.08573 | 2026-09-11 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a9bc406-61cc-3175-a3ad-67709b9b213a | -6.15413 | -47.24086 | 2026-09-11 04:51:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a91d7461-a707-36fa-ab30-7ba45c2e92b0 | -9.40951 | -49.39339 | 2026-09-11 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aad5e4ed-617d-3d9a-9cb8-a42c95160dcb | -2.69307 | -57.51228 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67c9d55f-b608-3a4d-bfe1-52b333a32a2c | -10.22118 | -45.20782 | 2026-09-11 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d785538d-7005-3d3b-b8de-c5f07f897c4d | -1.70235 | -55.02769 | 2026-09-11 04:51:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f483fec-25c7-3572-9c43-d923989fd556 | -4.82967 | -42.88148 | 2026-09-11 04:51:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 06042928-dd20-3578-928f-a8cce7280c63 | -2.93562 | -50.46173 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96ee13b3-f82f-316f-a3a2-215fdef5224a | -5.77894 | -45.07166 | 2026-09-11 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1537fcbf-d97f-37c9-832e-49b309035388 | -5.36878 | -56.01978 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd26bdd5-2f5e-3a59-a839-5b701fd48290 | -7.18415 | -43.60666 | 2026-09-11 04:51:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5f20c33-395b-34fb-bb1e-8214f31419e9 | -6.10781 | -57.65501 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d9311f7e-3257-314d-a847-d698a1a334bb | -2.9441 | -50.47408 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1543ae3a-a267-38ad-b524-431acfa5f886 | -4.53202 | -54.95643 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a411342f-2d23-3ee4-84db-a23e9d7d2eef | -3.24396 | -47.24973 | 2026-09-11 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b249eed-20b1-3013-9329-3510b5c18e1e | -7.34934 | -44.19532 | 2026-09-11 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42252593-3195-3807-9214-70f53137427b | -2.93679 | -50.47663 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49ab2a18-730c-35aa-a007-792c6c3de40f | -2.94692 | -50.47819 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fd3de48-2577-3005-9d33-594002a0c90c | -2.85994 | -49.54201 | 2026-09-11 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8592d37d-474b-384b-918c-740d302f44c5 | -8.50696 | -50.1527 | 2026-09-11 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4075b5d7-6781-36ed-ae2e-d31609fa67c1 | -5.97683 | -57.76623 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 22207ca1-1213-37fa-8eca-09221ecd5f9a | -9.31381 | -44.36088 | 2026-09-11 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d44d99b8-e671-30b8-9873-1632030bcde9 | -3.37653 | -50.75978 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df5a3986-9bc3-36ff-bac9-58d124b78d81 | -5.77969 | -45.0665 | 2026-09-11 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09fc16c2-4433-33f6-90a8-c58a3bdf6b34 | -2.69107 | -57.51549 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d6231279-5ab7-3903-9f57-f90661068538 | -6.10671 | -57.66169 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cb25b45-9276-3b79-bfc9-338b2d29269e | -4.86456 | -56.00731 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c23aeef-9eab-3363-978d-3c9984ebc371 | -4.17654 | -48.70907 | 2026-09-11 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d8b01bf-9e5f-397a-8058-2aa22d90bb3e | -3.09917 | -48.68171 | 2026-09-11 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c02b9a3-b22d-32e8-a368-3b9914e16c94 | -7.17958 | -43.61831 | 2026-09-11 04:51:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5cb270f-07a5-34ad-91fc-e402c16f2146 | -3.20682 | -49.53253 | 2026-09-11 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 905fb67e-0712-36da-9799-6a0dc39b5bc4 | -3.1563 | -60.65127 | 2026-09-11 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f94d5635-607b-3913-9346-07cd43e2d840 | -3.09736 | -51.28892 | 2026-09-11 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fe17549-bc96-3d51-aa98-09cc2849b3ca | -6.62969 | -55.12977 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67142bbe-0c5b-3448-a656-9dd22c0aa3e6 | -6.02508 | -51.32961 | 2026-09-11 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c65b1a95-6c44-3cb4-889f-a05b30f44c3a | -6.50518 | -58.3821 | 2026-09-11 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef677da7-93e6-3142-8fe0-3854910b7cdd | -7.97446 | -43.99931 | 2026-09-11 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 42692f58-11e5-326a-8d81-bd475f7f123b | -2.73304 | -57.63663 | 2026-09-11 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40f9238c-b1df-3347-a2b2-c06554b3bc1b | -6.20299 | -55.27766 | 2026-09-11 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1e7eb42-7a42-396f-afad-84cd6f08bd22 | -7.40558 | -49.74057 | 2026-09-11 04:51:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6f079c8-2ec1-30d1-a5f8-7f2b205f6eea | -4.86889 | -56.00383 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3023357e-6b40-351e-8c51-8284de7dbf37 | -5.28403 | -55.96364 | 2026-09-11 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8313938c-cbcc-373c-a57d-dcb87523beba | -6.24463 | -51.69036 | 2026-09-11 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 343af6df-94e7-3627-80fa-fedcc94a0cb8 | -9.78567 | -43.44747 | 2026-09-11 04:51:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16e60180-c6f1-30ff-b2c0-f5acee6b3a61 | -4.53138 | -54.96037 | 2026-09-11 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9ed61fec-0a9f-3706-b331-4b79eba398f5 | -6.77177 | -59.42767 | 2026-09-11 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a10d766-c646-34e7-a544-a449671b4bcb | -7.09735 | -45.03939 | 2026-09-11 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3610f68-c064-3ef9-9cf5-254f4404276d | -6.23849 | -51.68581 | 2026-09-11 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68ded010-9533-312d-a984-3cf2abddf78e | -2.93955 | -50.45865 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efc54344-02e3-378c-b4d8-6f96a0cee6c6 | -7.26028 | -45.35123 | 2026-09-11 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c356b2e6-f313-30b1-9bae-7d694b77bbbe | -6.7913 | -48.66523 | 2026-09-11 04:51:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a8b5919-3289-3868-9165-6ae95a44a1b1 | -3.13839 | -60.66413 | 2026-09-11 04:51:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8b92a97-ec3b-30ac-acff-ab6e03f33480 | -7.90661 | -56.63337 | 2026-09-11 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e13f63db-3037-3ff2-8b52-c99af8ad9ed2 | -6.1346 | -57.82507 | 2026-09-11 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f80e792a-5031-3ffd-960f-8c50f68c7a79 | -5.77265 | -45.08135 | 2026-09-11 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 72883b2a-fbde-3ebd-859a-7744df3fa37d | -3.1529 | -60.65355 | 2026-09-11 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e08d719f-13be-36df-ab17-8c922bfa0850 | -7.84706 | -56.58378 | 2026-09-11 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b381073f-6644-3412-9758-98eaa00b0a90 | -7.35454 | -44.19613 | 2026-09-11 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a8db4f4-baba-3e92-9bbe-bc285fec39f9 | -8.70872 | -49.61849 | 2026-09-11 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ce36ce9b-2614-3b80-bfa9-a89180f27463 | -3.37146 | -50.74806 | 2026-09-11 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78bfb497-b198-37b0-b098-2d7f212cb67b | -9.74685 | -41.96796 | 2026-09-11 04:51:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| dd8a1254-a84e-388b-9459-d8c78a725e7f | -6.50039 | -58.38517 | 2026-09-11 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README17.md)
