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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb59c727-dd8b-3587-b0b3-83e6862820fc | -5.74882 | -42.55539 | 2025-09-26 04:14:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5ccefaf7-fa59-325b-8af6-856047d65eaa | -8.93727 | -47.9482 | 2025-09-26 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71f1ddea-3cca-3b2a-bafa-590f655fcdd3 | -6.26426 | -42.4803 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| db66f854-6d8e-3026-ad48-372a08bdd46e | -6.79723 | -45.52025 | 2025-09-26 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d2fba56-ec13-31f2-8392-6466a9025147 | -3.78489 | -48.63303 | 2025-09-26 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 332b05f1-511b-3a13-b91b-4ff05e957ce1 | -6.53448 | -44.33405 | 2025-09-26 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35a985be-4790-3c4a-8372-c37ccda24fa2 | -7.11145 | -43.74248 | 2025-09-26 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51f98fa7-732b-337b-b70d-d5a11d23925a | -5.80495 | -42.8078 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a44d158f-4452-3dfe-8b13-4deb8aa62417 | -5.74273 | -44.97461 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 011885d8-ccc9-37cc-87b3-528ea102a0fe | -8.72021 | -47.1277 | 2025-09-26 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a630221-ec58-3b7e-a661-ac851688c4c7 | -8.13643 | -42.37853 | 2025-09-26 04:14:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3391bff6-5bd4-35ab-9c0c-1f3f2b505b3e | -5.6456 | -43.92955 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 90338532-2701-3c9b-b1bb-d8fdc8d4ba5c | -7.66813 | -47.42136 | 2025-09-26 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd9e6682-2c23-3625-bd1f-acdeb9da8780 | -9.55661 | -47.52025 | 2025-09-26 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d2aec7ac-d33c-3e9c-a60a-de38715647fc | -5.78186 | -42.8042 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 67e1d817-b394-38d2-a21f-ec079b630fa8 | -9.69183 | -48.94403 | 2025-09-26 04:14:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| aaf6d47b-5e20-3af6-8f34-791f4be7179c | -5.78078 | -43.32913 | 2025-09-26 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88fb3de9-f9e8-33f6-86da-3d6cdf044612 | -6.69434 | -44.63307 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 582ed811-5ffd-3394-b5c6-a99798b85ada | -7.1035 | -44.48286 | 2025-09-26 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f4a2033-919a-3740-aa97-609834e925e7 | -6.13394 | -43.44577 | 2025-09-26 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d336b100-9d03-3fdd-9046-039d02ef678c | -6.82538 | -44.1751 | 2025-09-26 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a9c92ee-0786-3ff6-87d6-d329ddda66c8 | -4.48233 | -47.67072 | 2025-09-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf4ded45-c783-3fd4-80ab-18ec5f9834bf | -7.2739 | -43.01156 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 79030a9f-cfd7-3d9b-838f-02504868a09f | -9.86888 | -45.914 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e676c52-64b1-3ed0-80e8-cfb0006b8fb5 | -9.1122 | -48.89994 | 2025-09-26 04:14:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2019b41-c9c0-34a6-86cf-397663f36a30 | -7.13134 | -42.19466 | 2025-09-26 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bf4aaa41-2c4e-34f8-9df5-5c4d6f7ea91b | -7.12023 | -42.20021 | 2025-09-26 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 22bee7c8-46be-375f-a090-3df10319013c | -3.81764 | -50.79272 | 2025-09-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11650baf-602e-37f0-b149-394c403a354d | -10.11393 | -45.33017 | 2025-09-26 04:14:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4bc1bfd-c63b-31cf-a0d9-0db809994392 | -6.25496 | -42.49658 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2b418d19-ab70-3cc1-aaba-21c08e2baf1b | -2.91626 | -48.63672 | 2025-09-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a136cfc-dd5a-3dc5-92eb-16c249ec0d6e | -7.77818 | -43.92063 | 2025-09-26 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c159fa8c-519e-363a-9b64-8bcd93518f36 | -5.7359 | -44.97352 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 48e5883b-553f-3d33-81e4-1e42b5e70a4f | -6.67903 | -43.59235 | 2025-09-26 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25800b01-8fd8-37bc-98c0-4e64b0a78262 | -2.79281 | -49.59446 | 2025-09-26 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15781067-2068-30ec-aa91-e5b76bbd90d5 | -6.11622 | -44.22422 | 2025-09-26 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a18f1039-ae7c-391d-a62f-3f88b890de8c | -7.25571 | -43.01524 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ff151ff4-d2ea-3162-971d-10325532a919 | -6.06592 | -43.57242 | 2025-09-26 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6873917c-27d3-3cf1-bd31-545dba50d7e7 | -7.04652 | -46.41708 | 2025-09-26 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94d495b0-172d-39a3-9194-88fbf35fb7cd | -6.26703 | -42.4843 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2e2d909e-fe40-3acf-b6f1-f88b97eba3e4 | -5.36971 | -42.27981 | 2025-09-26 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bfa86224-3cdf-30e7-83bc-90fbf2db3497 | -4.48576 | -47.67476 | 2025-09-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 28cefd5a-0691-3f4f-8d69-a63eb8e6f185 | -4.0093 | -43.23259 | 2025-09-26 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 522e810a-d537-397d-b63e-5496a8aee550 | -5.76534 | -42.55794 | 2025-09-26 04:14:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| daa46e4e-43be-37af-958d-333832da8ab3 | -6.5952 | -44.10217 | 2025-09-26 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7822b72e-aae5-30cb-8b40-94cc83eee580 | -5.78539 | -42.8682 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7efd70da-885f-32e0-a12e-5812f32d1f36 | -5.46894 | -43.0612 | 2025-09-26 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| bd0f70a8-0350-3185-8360-e9ea7ab2e9c8 | -6.32287 | -41.88075 | 2025-09-26 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a5d7edd3-749b-36f1-87be-f624715972c4 | -6.85572 | -43.18195 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0c9164b1-8076-3f90-b792-21be7559c502 | -4.95896 | -42.64654 | 2025-09-26 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 316822d2-c091-3e4d-a9bd-2315b4cbc50c | -6.61589 | -42.92836 | 2025-09-26 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1774690-71e2-3048-a789-9465365255b6 | -10.10622 | -45.31404 | 2025-09-26 04:14:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b972ca0d-b25b-363b-b16b-9febee923fd3 | -5.12305 | -45.50201 | 2025-09-26 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d3b3a62a-0abe-3e9a-ae2b-5f59cb773958 | -5.43223 | -45.13682 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9da22afe-bca1-34aa-acb8-bc3bd98839d4 | -5.38133 | -42.29227 | 2025-09-26 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ca569f80-c5e9-34b9-a9eb-a42bb3e82e4e | -4.19786 | -38.12412 | 2025-09-26 04:14:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 916af488-d9b0-364d-9c4a-09cc9e6746d8 | -7.36754 | -47.04282 | 2025-09-26 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ed3d46b9-bbd6-37a5-ace7-7197243c8fb7 | -5.80602 | -42.80091 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4be0c4cf-bf1c-3fe2-a43d-22a416ee7d6e | -4.75536 | -43.61674 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ae3200a-af66-310e-a4ee-84edaaa63eab | -5.20442 | -43.72749 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fffb5dc6-44a8-36e0-9625-1298ebe2d482 | -7.81489 | -47.33205 | 2025-09-26 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6731e3ac-b859-3177-9044-c3c5ec589b38 | -7.77488 | -43.92011 | 2025-09-26 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fec6e286-13cc-3f08-a736-4832d287f471 | -5.40059 | -42.27748 | 2025-09-26 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 09b38209-53a6-371a-bc79-4ad176674652 | -5.73577 | -44.99647 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cebe2f7e-e3f1-33ff-a5e3-f57d73e3e025 | -5.74614 | -44.97515 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| a2f71cd2-79d5-3792-9817-78ca7b3ce007 | -10.94016 | -44.26181 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ad11e08-7a66-30ad-8d9a-ad9244310819 | -4.17185 | -44.27164 | 2025-09-26 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 961f1370-7e35-3280-84a0-a25e1e408f6d | -4.8215 | -46.00159 | 2025-09-26 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4964868f-d7c2-3f08-87c7-712e9eb298b7 | -5.78462 | -43.32619 | 2025-09-26 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 426b3319-cf2c-3086-92e2-a89075565779 | -6.87336 | -39.25971 | 2025-09-26 04:14:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5c5646b2-b8ad-3255-a1af-6195861b44ae | -3.7799 | -48.63647 | 2025-09-26 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38133098-f5f7-365c-9724-e07aed72e9ac | -4.39032 | -41.92785 | 2025-09-26 04:14:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5c14bfdc-60c5-3982-a2ea-d6f8e9d6a14a | -4.45171 | -40.97697 | 2025-09-26 04:14:00 | NOAA-21 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 623246f3-80f2-3d59-a266-5347e49d17d0 | -7.04426 | -46.41708 | 2025-09-26 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fada5029-20f6-37f9-a9ce-60a45f7ac814 | -10.41153 | -46.16372 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1955c715-7308-3274-ac16-1b7f961b0154 | -5.59719 | -45.37678 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e98001a1-3600-39b8-ba56-f4bcc448881b | -5.94445 | -42.93591 | 2025-09-26 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 19e722c6-f384-36f4-a19e-24e39f1e8a3c | -6.42338 | -43.07477 | 2025-09-26 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 24dfad88-99f4-3563-96f8-82feb1291cfd | -10.10287 | -45.31349 | 2025-09-26 04:14:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| acb76028-6de1-32a8-acb3-77f7bd7f3e6c | -6.55628 | -43.53045 | 2025-09-26 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e43da61-73ea-36e7-b1d5-59a358e99b47 | -9.24561 | -48.56228 | 2025-09-26 04:14:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 423293a6-8104-3f90-b879-c5ccd88b98c7 | -4.39086 | -41.92437 | 2025-09-26 04:14:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 46500339-767c-373a-a110-69ae426c21c6 | -8.13331 | -44.1269 | 2025-09-26 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3c72fe4-62c3-31ba-a6bf-ea88bc65b325 | -3.44598 | -44.12876 | 2025-09-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db497e4a-2b9e-3224-9db2-4020758b7319 | -3.2792 | -44.67289 | 2025-09-26 04:14:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e3a7801-3dfb-3505-b107-8f665facc2ce | -10.93686 | -44.26128 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2bfcd918-f225-30ec-9c1d-97dcf033edba | -7.31687 | -45.76318 | 2025-09-26 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7eb3ca4e-94a5-3cf8-af7b-5fdae91f528e | -5.17043 | -38.09114 | 2025-09-26 04:14:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5443b74f-3c00-32fa-a515-07ef95f447b0 | -8.13978 | -42.37904 | 2025-09-26 04:14:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 278ef24a-02f6-3988-98d3-7af36196baf9 | -7.18001 | -42.2308 | 2025-09-26 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 785abe69-951e-352d-96b5-71bc611a1dc4 | -5.53375 | -42.73318 | 2025-09-26 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1f451227-2678-3907-92b4-b026b273bd1d | -5.80111 | -42.81073 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 68237f94-fc34-3d67-aeef-82051249f7ce | -3.8146 | -41.55947 | 2025-09-26 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| bc2982e0-b48e-3016-94d0-e2847ef2660c | -9.30552 | -46.61999 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08fa6366-7a4c-3897-94bd-208a9cda1e73 | -3.44993 | -44.12566 | 2025-09-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 639f90a8-75c7-30ad-a465-29f195be372c | -3.80501 | -47.58757 | 2025-09-26 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b205bf05-0a67-3d0e-b62e-db00a45c5f73 | -5.74565 | -44.95612 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ec2a8b85-ee3f-342f-9dea-d77f33fff92a | -9.80523 | -45.72113 | 2025-09-26 04:14:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03294a61-aacc-380e-b8fa-e13d82a805e3 | -10.00436 | -44.1747 | 2025-09-26 04:14:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6eca58b8-ade4-3b38-902e-e1baf86b733e | -10.59733 | -44.08484 | 2025-09-26 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README13.md)
