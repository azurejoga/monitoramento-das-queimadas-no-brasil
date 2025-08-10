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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdf21531-94bb-3d88-8c25-cede6287a53e | -7.36639 | -46.65598 | 2025-08-10 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d251b1ef-f169-3b6a-a8b0-c5a0acbeef3a | -6.55898 | -42.85214 | 2025-08-10 03:55:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 88fd75e1-cf81-3baa-a2f5-85ff856b14be | -8.501 | -44.75714 | 2025-08-10 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a72856c4-eef0-313e-8d00-d17195c0ea32 | -11.40329 | -42.29583 | 2025-08-10 03:55:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3704804c-582e-3aa2-8ca3-7a53abfebe5f | -7.29788 | -39.63723 | 2025-08-10 03:55:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0b24a633-eef3-3abf-9e5d-8385edef91ed | -6.55264 | -42.77261 | 2025-08-10 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 0999ccec-d582-3215-bf8e-249d9e4604ff | -7.70383 | -45.54547 | 2025-08-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a5c1619-a572-3559-bfd8-b38c190206c8 | -6.05836 | -43.74104 | 2025-08-10 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 036adbe6-5d5e-3ec5-89d9-96e43187d348 | -6.52326 | -47.43053 | 2025-08-10 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f70d21a-6862-3b81-ae23-7aa5c54a0acb | -7.30064 | -39.64127 | 2025-08-10 03:55:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d0003f81-8a2b-3545-98e4-147f6ab8bcff | -7.70013 | -45.54003 | 2025-08-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 764f0b38-66a1-392e-bc81-84aaad14f3a5 | -7.70172 | -45.54307 | 2025-08-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bcc73780-da48-374c-9e33-11d51db7c1e9 | -7.13144 | -39.46399 | 2025-08-10 03:55:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1cded2da-1dd6-37dd-83a9-ec17aecffac8 | -8.98482 | -45.69403 | 2025-08-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a70e61ad-87e6-3069-a431-079818e6986d | -10.96256 | -44.85588 | 2025-08-10 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5135596f-64e4-3d51-92ee-d9a489ca1fc5 | -11.73013 | -45.01493 | 2025-08-10 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f8fa4341-64b4-373c-b576-bb0c0d07e5b0 | -6.97966 | -43.8569 | 2025-08-10 03:55:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c1c4c85-d8c7-3be3-8c88-95a1352bdec1 | -8.98557 | -45.68314 | 2025-08-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74e0f73f-d19b-370a-bc28-c53c25b4854f | -11.3755 | -50.53311 | 2025-08-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d207bf14-cdc9-36bb-b4e1-c07f6bc34a29 | -13.19858 | -42.24855 | 2025-08-10 03:55:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b6125712-f280-3e6f-bd08-aa4eebc255d8 | -8.37168 | -46.98464 | 2025-08-10 03:55:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d87418b6-5e76-3564-b669-1bdc3483586a | -12.53089 | -45.67328 | 2025-08-10 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a4f8deca-a2e7-3a56-a508-8dcf3d32395e | -12.57388 | -41.28128 | 2025-08-10 03:55:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 51048011-b805-356a-8632-0c912630a1f2 | -6.97499 | -43.85986 | 2025-08-10 03:55:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86ce9e16-6eb7-3666-b615-e8779a4678d3 | -11.43551 | -50.59081 | 2025-08-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60ede660-d978-37dd-aa01-4bc24b6f2bae | -8.50968 | -41.43159 | 2025-08-10 03:55:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9ee5c289-32bc-367f-9fa2-3a8846239072 | -7.34587 | -44.59929 | 2025-08-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| baed5bdf-732f-35f3-a6b4-059ac6eb3c0a | -12.23616 | -40.56889 | 2025-08-10 03:55:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ebfc03da-2d67-3790-8510-325595a4a668 | -12.13959 | -45.64461 | 2025-08-10 03:55:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e52c9007-abca-3437-b5ca-e293225e6a0d | -5.47753 | -44.70098 | 2025-08-10 03:55:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4dbd3172-7535-3c08-b341-ef58dcb34e7c | -12.64232 | -44.50986 | 2025-08-10 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2461215e-418c-377d-a1ce-b3a823c0a36c | -7.39571 | -39.68556 | 2025-08-10 03:55:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 078d2d2b-9bab-3da9-93ea-a98006ec0f82 | -6.97632 | -43.72776 | 2025-08-10 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dba1a83f-80d8-37b4-bc61-f4509a4978ab | -9.86784 | -44.70113 | 2025-08-10 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ab077141-ebac-34f6-b3d2-bbe595c3e977 | -6.21457 | -41.40453 | 2025-08-10 03:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 72849b57-b8b8-379a-a953-1295655739dc | -5.47313 | -44.70024 | 2025-08-10 03:55:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ef582927-5993-3c38-b93b-fe01dbd48148 | -9.6569 | -46.76854 | 2025-08-10 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8326ff4d-ff5e-38a6-9d11-b1e0d1a0e9d1 | -5.82625 | -44.1059 | 2025-08-10 03:55:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 00e6630f-a438-3fe1-a6c7-052daf85530a | -7.16778 | -44.39577 | 2025-08-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6431e16d-90b4-3ef9-aefb-5d7c9fd01612 | -9.20612 | -49.67695 | 2025-08-10 03:55:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ff4a396-38c6-3051-b55e-09d097238670 | -6.54881 | -42.77198 | 2025-08-10 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 0241fab1-3a7f-363e-bdb0-5ff8b34c4fc8 | -7.88645 | -45.55674 | 2025-08-10 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ef4ddd1e-a63a-3d4b-b902-072a7ccb42da | -7.34236 | -44.59437 | 2025-08-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02e4d2da-8e31-37cc-90ac-b0ba6c92eca6 | -6.54666 | -42.76833 | 2025-08-10 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| d073a5ee-0f92-3a5f-86e7-d46e895dfac5 | -8.11066 | -47.4382 | 2025-08-10 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81ff4497-7d17-3673-9c73-198cb4f61f9c | -6.99814 | -45.62197 | 2025-08-10 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83c7fb56-cd72-3ee6-8c0f-a47122c4512a | -6.19754 | -46.09885 | 2025-08-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c782081f-699f-328d-87ae-0f510ef023da | -12.53438 | -45.67794 | 2025-08-10 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c51deb27-708d-33fb-9300-4920f392b969 | -6.3952 | -38.91143 | 2025-08-10 03:55:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0442a5eb-28d7-3097-b9c0-4e6360fab51b | -9.52924 | -45.3988 | 2025-08-10 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e79928da-d51b-31a8-bb79-d449f29aab67 | -6.55279 | -42.77896 | 2025-08-10 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 9c08b5a4-5189-38f7-b2ad-18c11e2b08d0 | -11.77823 | -44.95543 | 2025-08-10 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34c00109-aba2-3e9a-b33e-6d5d5e91fc8c | -9.52415 | -45.42797 | 2025-08-10 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d73d382a-ab5f-3db5-9382-31e7f8440857 | -8.50094 | -44.76038 | 2025-08-10 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 800d5d0d-15db-3027-8450-aba63c87a29c | -6.05774 | -43.74469 | 2025-08-10 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1711bd29-0bd5-3530-8e1b-ba2243a6f9d4 | -5.85225 | -42.95743 | 2025-08-10 03:55:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 6aed1a9f-5737-3d4c-99ef-69306c3b4984 | -11.38299 | -50.55684 | 2025-08-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b377afcb-8455-3723-8ddf-d92d1e53696c | -6.57744 | -44.5681 | 2025-08-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd68991c-3f8a-3553-8169-ff0a795b851f | -7.3012 | -39.63775 | 2025-08-10 03:55:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a1dc7203-b465-358c-a47b-e78e3ccad32f | -8.11171 | -47.43224 | 2025-08-10 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f7bc6fa-80ec-39d4-a1d3-02d17fe1fc38 | -11.43157 | -50.58889 | 2025-08-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cf84a4aa-e6d8-39bc-b320-410d99aec255 | -6.54959 | -42.76733 | 2025-08-10 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 4619e286-7a13-326e-a711-d0e8e0566de8 | -6.98042 | -44.80239 | 2025-08-10 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37105ab4-2e81-35a7-a072-c4889bdb0ff8 | -11.78358 | -44.94864 | 2025-08-10 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f1dc3d0-d0c5-30a4-9ffc-4a4a7611f3af | -7.28444 | -44.16053 | 2025-08-10 03:55:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7146e199-1d29-3bfe-a5c0-ef0f06d9323e | -7.58878 | -44.40149 | 2025-08-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fee03054-50a3-301b-b53f-9a17bbb1e07c | -8.88332 | -44.78487 | 2025-08-10 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8e02d87-29aa-3107-9335-46f58bfd9915 | -7.88883 | -43.54712 | 2025-08-10 03:55:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2faf7a75-31db-3a2d-91f5-9cd7fa8bc158 | -10.34602 | -44.9085 | 2025-08-10 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e45418ba-c64a-31bf-aeb5-301721db6d5d | -11.73354 | -45.01927 | 2025-08-10 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae96487a-b403-3782-9ead-924ef077fe7b | -12.64188 | -44.85876 | 2025-08-10 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 955bba5f-fbae-3634-83b8-c0964f785c22 | -9.49239 | -46.27991 | 2025-08-10 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b41ae4cf-eaf4-3583-bb2a-9a790c4e9196 | -9.57367 | -48.44438 | 2025-08-10 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f3f2412-3eb3-37ab-a7bc-f93f43466818 | -7.598 | -44.42276 | 2025-08-10 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b5fbdc4-5f38-35c7-994f-0d1f83d4cccf | -11.4305 | -50.58535 | 2025-08-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2968f94c-e158-36db-8b05-345a99116b7d | -11.49106 | -50.28301 | 2025-08-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1be564e0-fa54-3f4b-9e5a-e59c4ffa8deb | -11.65781 | -48.32309 | 2025-08-10 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3eb89131-457b-3c19-baf4-2ca70339318d | -12.58001 | -41.28605 | 2025-08-10 03:55:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 006a390d-8f25-3126-ba16-0836e0ffff48 | -12.5806 | -41.28241 | 2025-08-10 03:55:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0c1edf2a-c835-3ee0-a61d-20d2fabe7e49 | -11.43637 | -50.5865 | 2025-08-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef655a75-ac87-3071-8109-92188941470c | -11.72949 | -45.01851 | 2025-08-10 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c7cb5b7-8493-37fd-aa8c-84886b2055ba | -9.65872 | -46.75819 | 2025-08-10 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9aedff36-ef8e-351b-b711-3391b34f24ab | -6.98379 | -43.73265 | 2025-08-10 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0eb1c923-e0db-36a5-ab42-ce069feeecac | -6.57674 | -44.57216 | 2025-08-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2010c90e-8606-3548-b19b-00186b9ecb65 | -11.33139 | -44.85397 | 2025-08-10 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56127eaf-2bf3-3517-bb11-5ffe385373a6 | -6.44957 | -41.74359 | 2025-08-10 03:55:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3348215e-2249-366b-bd8a-034f9b102637 | -7.88568 | -45.5612 | 2025-08-10 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dfa85256-b2f4-3de6-807c-d3915e6ae1ae | -7.54032 | -44.00312 | 2025-08-10 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e820d8bc-9f30-33ea-a89e-bfca7153825f | -6.52789 | -47.4347 | 2025-08-10 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59f47f92-2315-31ae-a302-4b61f06ed316 | -7.70335 | -45.53387 | 2025-08-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 79919e48-fb71-317b-a34c-e9eb7f0eb819 | -6.5683 | -42.84358 | 2025-08-10 03:55:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| e4177a69-d026-3dff-87ae-a8e2585ff55e | -7.39515 | -39.68908 | 2025-08-10 03:55:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 28900b63-8331-3ba4-a701-25ed3120d102 | -11.77886 | -44.95178 | 2025-08-10 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 095924d8-a944-3cbb-a7ae-72477d5bc506 | -5.47239 | -44.70454 | 2025-08-10 03:55:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fa119e07-925e-3880-8f28-fde13e08ec79 | -6.93369 | -42.9655 | 2025-08-10 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a53b9013-1cf6-38ca-b3bc-2c17b984036c | -11.4257 | -50.58771 | 2025-08-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6516985e-855f-3cad-9573-f21e36aeb7cc | -6.19272 | -46.09821 | 2025-08-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d32a309a-fe25-3b01-89df-8078996dfcc9 | -6.55431 | -42.76959 | 2025-08-10 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| c469e62a-e48d-33c9-a8a9-3e861510e781 | -12.04569 | -41.69369 | 2025-08-10 03:55:00 | NOAA-21 | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7a979023-b682-304e-b65e-bef4e25ee869 | -7.87748 | -45.55516 | 2025-08-10 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README9.md)
