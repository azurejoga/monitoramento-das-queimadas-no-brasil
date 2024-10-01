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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d1fc294-ad56-394d-9271-101100a99b4e | -9.75692 | -41.88639 | 2024-10-01 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| ab06f678-f579-3522-9cf1-265d49394043 | -9.75462 | -41.87843 | 2024-10-01 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8351c4b5-23e4-325b-a805-ff5a78404295 | -9.75406 | -41.88214 | 2024-10-01 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| d246d60d-facb-3bba-87c6-a95bd6ac7ee5 | -10.38017 | -42.5921 | 2024-10-01 04:12:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c108434e-2b04-3357-8062-293a51668536 | -7.32198 | -43.32427 | 2024-10-01 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12c2a357-fa81-3749-9f72-84d71911f500 | -4.80021 | -43.05279 | 2024-10-01 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c995d4fe-93e2-3279-9b07-adeebb8ef24d | -6.1859 | -42.96744 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 55543341-8dee-3c32-aca6-3830d5e60779 | -6.18536 | -42.97089 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9a531d9e-156e-34fb-b353-8e6f807df651 | -6.18314 | -42.96347 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7d0c97bf-d39f-3b83-9651-65236520de24 | -6.18259 | -42.96692 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d9a4de61-cb5c-3329-a657-ee0c076efb3a | -6.18205 | -42.97037 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ce9dcbd6-eeb3-312b-9b08-b37b1103ced0 | -5.95813 | -43.27102 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 071f68bd-d9a8-30e1-aa49-c9cd30c7824a | -5.95537 | -43.26704 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ecdd8892-1a92-323e-bd70-9ffeb4827e91 | -5.95482 | -43.2705 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d5c065b1-02ae-381a-8279-cb23bbc30ebc | -6.44376 | -43.14231 | 2024-10-01 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55119bde-0f40-3f14-990e-875692bfba14 | -6.43378 | -42.88236 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d8394b4d-88aa-3fad-8bba-c84596981132 | -6.32793 | -43.46796 | 2024-10-01 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08b67c95-73af-3554-90a0-ae26d860c3d2 | -6.32738 | -43.47143 | 2024-10-01 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a9064a0-b996-3741-8c07-4f0acc581931 | -6.24025 | -43.31238 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb4e297f-04c1-396b-a5a4-447c1d0b79a3 | -6.18644 | -42.96399 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5866f62-c0c5-3c3f-a681-436efee4dc31 | -6.28017 | -42.53976 | 2024-10-01 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b19c2ee2-bd7e-30db-b94c-d00f0cb5338b | -6.27686 | -42.53925 | 2024-10-01 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a1bb0b65-b9ee-3fc3-89de-ac06643dbba8 | -6.27355 | -42.53873 | 2024-10-01 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c251a0e5-c2c1-3a31-8c90-3df9674b516a | -6.27024 | -42.53822 | 2024-10-01 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 520d8d93-39d4-3b11-a72f-121d97aac8dd | -6.26693 | -42.53771 | 2024-10-01 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2ad16409-5517-3404-85f5-7e6f77fa8e0d | -6.26639 | -42.54118 | 2024-10-01 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d4e5ec35-a426-3cea-9fab-e75682418ea3 | -6.26585 | -42.54464 | 2024-10-01 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b436084d-3577-3bf5-bd52-3c578502d5a4 | -6.26308 | -42.54067 | 2024-10-01 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| af966f0e-1b7c-30f1-85f0-9928e94bac71 | -6.26254 | -42.54414 | 2024-10-01 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f273d843-df94-3f59-9a43-7fc2137d84dd | -7.88259 | -43.15062 | 2024-10-01 04:12:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8b318bc1-b057-316a-a3a8-33545c63abe6 | -7.8549 | -43.08943 | 2024-10-01 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4a04da92-1f08-32fe-9ef9-9d479f61cc80 | -7.85268 | -43.08197 | 2024-10-01 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6c59c6b6-861e-307e-bc55-ac41058a5cb5 | -7.85214 | -43.08544 | 2024-10-01 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 16d23098-7387-3e48-b053-7c3001124214 | -7.85159 | -43.08891 | 2024-10-01 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8fdf42fe-e169-30e7-bc58-eda4b081b7c6 | -7.85051 | -43.09584 | 2024-10-01 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 25996637-a717-364f-b3dc-35c0ce0c83d6 | -7.84997 | -43.0993 | 2024-10-01 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 77bc5b7c-e12c-3861-b2c6-a86a8f0209df | -7.84937 | -43.08146 | 2024-10-01 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 32e4e60f-47b1-3d9a-890c-b21d9eeb07b4 | -7.84883 | -43.08492 | 2024-10-01 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 090b55a0-f1c3-3535-aa54-92b3112032a3 | -7.84552 | -43.0844 | 2024-10-01 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 089aa576-d6ae-3e9c-a79d-fe33d17256d2 | -7.84281 | -43.10173 | 2024-10-01 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c4fc98e0-94d4-3519-95f6-ec1b2c3e9e78 | -7.84222 | -43.08388 | 2024-10-01 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b67b869a-1eb7-3a09-83a4-4a518f6e21ca | -7.84167 | -43.08735 | 2024-10-01 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bf0fd64d-cdf7-3557-bf52-a546a3ca2246 | -7.84005 | -43.09774 | 2024-10-01 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 67b6847e-5692-3783-9d31-6d70601f3ad9 | -7.83674 | -43.09722 | 2024-10-01 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d2b7ae35-a635-3b0f-a6df-b18f9c2e9f4d | -7.8362 | -43.10069 | 2024-10-01 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1c51c159-b409-33b2-a56e-43719ca58f76 | -7.76284 | -43.7822 | 2024-10-01 04:12:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c1295b89-ace5-3820-9887-a13326326635 | -7.70216 | -42.97977 | 2024-10-01 04:12:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3738a28d-8c9c-3659-8400-26adde432a5d | -7.69614 | -42.99659 | 2024-10-01 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3e94cd6b-e422-3c65-8e59-5f0f6f6d131f | -7.69337 | -42.9926 | 2024-10-01 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 80eb8479-2154-3d89-bfed-1cd8ef867222 | -7.69006 | -42.99208 | 2024-10-01 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6760b1ef-dfd6-3c39-839d-af8d0deecbde | -7.68952 | -42.99555 | 2024-10-01 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4bf8cf28-0dfc-3a3c-802e-c1ec022321b4 | -7.17442 | -43.48547 | 2024-10-01 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 44e6eb86-9ca5-336a-a218-3016da9c2986 | -7.04995 | -43.34836 | 2024-10-01 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 245f0fbc-2a7b-3a36-aeb0-9ee3da2c5ba8 | -7.49061 | -43.78495 | 2024-10-01 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee69eeee-309e-332f-ab3e-0f3f9266e36d | -7.32143 | -43.32773 | 2024-10-01 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19952266-a0a9-3832-a7a9-aef7b85bd816 | -7.28626 | -43.37888 | 2024-10-01 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f202abbc-8c2c-3320-8d1c-9a2051bcb60b | -7.28241 | -43.38182 | 2024-10-01 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 889e2f66-8126-3ba4-a11c-5b218ce5b2c3 | -7.2791 | -43.38129 | 2024-10-01 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34950937-5eab-32ce-b562-3b113eb5ccef | -7.27855 | -43.38475 | 2024-10-01 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 193ce632-0282-3423-9aa0-9200a07d2e6b | -7.27525 | -43.38423 | 2024-10-01 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34735db9-dda2-3ebb-9c3c-e6e745bf3ea8 | -7.2747 | -43.3877 | 2024-10-01 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 911c845b-9a14-3bbd-83ac-443e702f45b3 | -6.84788 | -42.94809 | 2024-10-01 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 46ddad0c-58ec-3039-af9d-cab8f1c3bbaa | -6.72062 | -43.56288 | 2024-10-01 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab81fa3c-01ad-3559-8237-6143714b3713 | -6.71731 | -43.56235 | 2024-10-01 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c57c083b-f524-3c42-947a-46976dfaf2ab | -6.69963 | -43.0484 | 2024-10-01 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b017e18d-5d6b-3dec-8272-dae06ea6d1d9 | -6.69687 | -43.04442 | 2024-10-01 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c24056da-5779-38da-9a9e-0d07abd1671e | -6.69632 | -43.04788 | 2024-10-01 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a335d527-42ea-3762-980a-d8b71480d0a5 | -6.69578 | -43.05133 | 2024-10-01 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff38c1db-3f8b-3815-b884-18d5f3d45877 | -6.69302 | -43.04736 | 2024-10-01 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5ac3c11f-e033-3c80-8e84-8986af68faca | -6.69247 | -43.05082 | 2024-10-01 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dbfeccc-1806-363b-849c-d5ee43da20fd | -6.68583 | -43.54666 | 2024-10-01 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 145cc170-21e2-3e65-9c1b-f292b87bdd13 | -6.68251 | -43.54613 | 2024-10-01 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 16c2886c-0318-3fa0-96ce-5f17bd25f6f1 | -6.67202 | -43.54804 | 2024-10-01 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db212553-632e-352b-aa33-718388a0cbf7 | -6.54518 | -43.03825 | 2024-10-01 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82f46c7e-33e6-3344-8e55-0e8c5723333e | -6.54242 | -43.03428 | 2024-10-01 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7b422ba2-1042-3c0a-bcc6-160f1a9eaa1f | -6.54188 | -43.03773 | 2024-10-01 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3f2b153a-9e7d-3079-9099-56a5c735cf80 | -6.54133 | -43.04119 | 2024-10-01 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 68ef2243-702b-3780-b723-83632976345a | -6.53911 | -43.03376 | 2024-10-01 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 10224dcc-d082-3641-aa48-400b9fb7aa19 | -6.53857 | -43.03722 | 2024-10-01 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6f49f803-0c9f-3a27-90ae-efa706612701 | -6.53803 | -43.04067 | 2024-10-01 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 2908ce0f-94b9-302d-be17-bc9fd5f202ad | -6.53472 | -43.04015 | 2024-10-01 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bb37dcb-9549-3833-b92f-645a5867fff3 | -6.50525 | -43.16294 | 2024-10-01 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd336290-fbc8-3089-afed-6bbb3dd654e6 | -7.66225 | -42.43003 | 2024-10-01 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ee4ee39f-35ae-3348-9af2-38b0b2852708 | -7.65782 | -42.43656 | 2024-10-01 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eff44d2c-f687-353a-9c6c-b5ca90a8e5f0 | -7.6545 | -42.43604 | 2024-10-01 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 711c6db6-c2e2-39a1-99e2-79c9817835fb | -7.4553 | -42.5166 | 2024-10-01 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6325ea8f-a21e-3fdb-bd52-8d94e4a897b7 | -7.29378 | -42.26527 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aec78782-3d45-3214-99aa-5af24a82d2c4 | -7.29045 | -42.26474 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 95db4d2d-1c01-3811-a3be-8f9b7d087618 | -7.28991 | -42.26826 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0a8e4b7f-08c7-3407-a5a3-3d7bdb415654 | -7.28874 | -42.25366 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b32b64c5-27e1-387e-b16e-bcb50d208e2a | -7.28595 | -42.24961 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ae514017-010a-3874-85f6-0e789d0f4f09 | -7.28098 | -42.26299 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3c45165f-69f6-3d90-8088-dc4e106c9da1 | -7.27984 | -42.2484 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1be1f46b-bc9d-3e60-a7dc-0d1fdb63edf1 | -7.2793 | -42.25192 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e1aab7d8-b43a-35b0-be24-673d19d3445d | -7.27875 | -42.25544 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4f68d7f4-975b-3aa0-a28c-b1e7c0ac630e | -7.2782 | -42.25895 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c31ebb6f-acc2-3e1b-aaaf-bc51275440bb | -7.27765 | -42.26247 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bde0f211-fb39-3d7b-b131-93e07a79e387 | -7.27542 | -42.25491 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d8d18c63-e231-361e-915d-64e3c8e2bd6d | -7.27432 | -42.26195 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7c5eb2f6-ad99-3828-a8d9-a248d446064d | -7.27099 | -42.26142 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README68.md)
