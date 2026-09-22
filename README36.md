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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebb0be77-45b0-3126-b66b-41a0dfef48c3 | -5.98621 | -44.72787 | 2026-09-22 04:02:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a72d217c-a19a-3101-9e67-d3eccba45938 | -11.87428 | -46.84729 | 2026-09-22 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f83ffd08-2cf7-3f57-832b-912e8033e8c2 | -7.90028 | -49.01381 | 2026-09-22 04:02:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce58a6c2-0c9e-3de5-9a57-0c1124eaceaf | -11.41587 | -47.34364 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 47affdea-4c78-3a69-afa4-2e2c194f7ceb | -8.7887 | -44.27984 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 446fabdd-8cc6-3754-a280-30d8946a69f5 | -6.88446 | -41.71372 | 2026-09-22 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 467d96e5-94dc-3505-8c49-5099f85c93bb | -6.29237 | -47.65843 | 2026-09-22 04:02:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58d703d3-fcfe-3ea0-a685-927fc9fde887 | -8.78427 | -44.30564 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53b01607-4ffc-3fb9-8ea6-dc484152cb68 | -7.13231 | -48.44136 | 2026-09-22 04:02:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 078f3b92-4de1-3c4c-a91c-2485133b1b87 | -9.53305 | -45.38906 | 2026-09-22 04:02:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a8f392c-d6d3-357d-9761-b3ee5e834e6b | -7.9472 | -45.64769 | 2026-09-22 04:02:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32cfa9da-a4d2-37bd-8b69-91643126102f | -7.4458 | -44.74547 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e89d86ca-16d4-394b-bd54-277311f91710 | -10.91067 | -47.38155 | 2026-09-22 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0b31937-0a9b-389d-9401-9ca9951adbe7 | -5.75341 | -45.09389 | 2026-09-22 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 97acf173-a8be-3628-99ab-787764daecc3 | -11.43017 | -47.34616 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a459ed4c-06cb-33eb-8297-99bc86dbdb70 | -6.92855 | -42.89075 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5c2ffdb6-1258-337a-bf5e-b8c96b7a57ca | -11.38507 | -46.76115 | 2026-09-22 04:02:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02ddf094-2b1d-3ae2-ab2d-feaefa7cd01f | -9.49602 | -48.50946 | 2026-09-22 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 273b04db-4c1c-315c-9a3f-9f36c765206f | -6.58412 | -44.14998 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a919d7c7-1a91-38a1-8750-eb298481ca19 | -10.68257 | -50.76849 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ced83eed-2574-32b1-8a46-e221a443f4e8 | -6.87435 | -41.70789 | 2026-09-22 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9ac63875-494c-36c5-9899-9e63ffe3c87a | -8.31612 | -44.7543 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5b7c8c6-39b9-3b6c-ade1-c2cd4219c176 | -12.56314 | -45.97425 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 211c1dba-0efc-3a68-b880-160045976e89 | -11.43101 | -47.34352 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28863dd7-386e-356d-b443-ab18ac752bd4 | -11.80118 | -49.81136 | 2026-09-22 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6538e394-157a-3a26-8689-fe679a3adfe9 | -7.42333 | -49.85736 | 2026-09-22 04:02:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3d7a51ea-944e-3755-b68f-e891cf3a9fe3 | -11.31814 | -51.36036 | 2026-09-22 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01a148e3-dfbe-3e7c-adf0-297c6b2a2b26 | -7.40401 | -44.8097 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 892ae0dc-569e-3028-bfaf-2d529232f7fc | -8.91416 | -50.93095 | 2026-09-22 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0fc10138-2f37-31f1-85b2-a376a7b74e6a | -4.18539 | -51.24643 | 2026-09-22 04:02:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 839a2ab4-09c8-3e7e-be49-7d7766578b4e | -11.4294 | -47.3504 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e98be341-ffff-3d34-bd51-02d6ecff611b | -6.71761 | -43.9811 | 2026-09-22 04:02:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2ad8e9d-abed-3ec4-9710-9473a3910f30 | -9.60536 | -43.92917 | 2026-09-22 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5b7ac373-9159-3e05-bd46-66bedc9d9a4b | -12.56596 | -45.98318 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2f68b18-feb7-3af8-944f-d946b8ef91c9 | -11.38169 | -44.23068 | 2026-09-22 04:02:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ba31603-6928-3479-9516-5d02fdbd0bc0 | -9.50132 | -48.51053 | 2026-09-22 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e968014-6fc6-32be-a768-34d3b7c07cd8 | -6.44468 | -48.44989 | 2026-09-22 04:02:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80acc52b-eb9d-359c-b6f3-f4b9663e075e | -6.48515 | -44.1685 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff08845c-2d80-3ae9-983d-f42d81697242 | -6.57247 | -44.15996 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f4ed1cf9-a3b1-3717-979a-1ac0b7e7fc79 | -11.65102 | -43.43799 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b514e20-6c05-3396-9224-ac31e7bc0aa8 | -11.09919 | -48.33016 | 2026-09-22 04:02:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30fe08ee-d772-3fd9-8b4b-16b2a2b2cdf9 | -10.83692 | -50.14309 | 2026-09-22 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6db5ef8c-fa9e-37c5-b1de-1f925e47406c | -7.01916 | -42.08461 | 2026-09-22 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 60fbf95d-e704-3493-9c38-612f101665a0 | -11.40611 | -40.29978 | 2026-09-22 04:02:00 | NOAA-20 | SERROLÂNDIA | BAHIA | Brasil | 2930600 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6de5c401-20aa-3076-a67a-484406d2e8bd | -5.53679 | -43.38908 | 2026-09-22 04:02:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4366585-1e9b-3904-abbc-30526cc1587b | -9.62238 | -43.94767 | 2026-09-22 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| eb919503-be3d-37f4-8375-303b9259a956 | -7.31164 | -42.26529 | 2026-09-22 04:02:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 16fa2f56-6ca0-312e-8e50-3499b8756fac | -6.89963 | -42.95751 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 94f8d4f1-5e26-325f-b726-63d99ce82aba | -6.57184 | -44.16377 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48f32546-436f-372d-ba07-11feaab66ee9 | -7.55776 | -42.65707 | 2026-09-22 04:02:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 61a321f5-f50b-3953-a219-3d8176805b8e | -7.12808 | -48.43306 | 2026-09-22 04:02:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e8e84a0-856d-3033-99b2-3defeb046e29 | -5.77358 | -47.3633 | 2026-09-22 04:02:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30c163af-d03e-39be-bb87-c1aa4ad91e66 | -9.6154 | -43.94123 | 2026-09-22 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b37427fb-fe0c-33d3-8042-7bb2b12cb50a | -7.34295 | -44.45522 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ad6a067-6718-33f1-8030-d84fde6d5f50 | -12.56512 | -45.98123 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adb0a25d-0aee-3427-9feb-3353278d88a7 | -7.13664 | -42.07586 | 2026-09-22 04:02:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b12c98ab-acbf-343d-b784-1254c1a83ad1 | -11.41 | -46.78025 | 2026-09-22 04:02:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d500f0dc-5872-3855-b2fa-e958d58df885 | -6.55931 | -44.83546 | 2026-09-22 04:02:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5d8e5e3-7876-3aea-a238-e0000ce4f172 | -7.92011 | -43.13794 | 2026-09-22 04:02:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f221951a-f1bd-3c54-88fc-24e4493bafd6 | -10.55648 | -46.72811 | 2026-09-22 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f39621a2-b5e2-3670-81b5-da7009861056 | -7.42042 | -49.83915 | 2026-09-22 04:02:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 696ca00f-66b8-387d-8f70-d709979c3676 | -10.01742 | -45.20799 | 2026-09-22 04:02:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86666b63-ddd4-3d13-b1cc-e1763aef77ed | -12.19457 | -47.03085 | 2026-09-22 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 71f5abf9-3f3a-3743-b3d8-3d75cd9575dd | -6.87084 | -42.86898 | 2026-09-22 04:02:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 38e56b1d-de0b-3e35-9719-9734abf0b99d | -11.16339 | -51.12278 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 26defe3f-b5f6-3479-a93b-d1cdc59d200b | -5.68151 | -43.42089 | 2026-09-22 04:02:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 620f0e8d-4164-3ecf-849a-1c9207d1ea42 | -6.5827 | -44.14996 | 2026-09-22 04:02:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7369496a-1e09-3bf8-a8fa-5dbe8a5e39b0 | -7.4501 | -44.74607 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 29391f0f-5f28-3284-9d63-5afa46e16efd | -11.32945 | -51.36782 | 2026-09-22 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c620e4e-cc33-3d4c-8ca8-93b0531ecb8f | -6.77593 | -48.66475 | 2026-09-22 04:02:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebdabdd2-25d8-36fa-bd2c-b2190b4eb862 | -11.02198 | -48.27657 | 2026-09-22 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af470c78-0f20-35ce-8f8e-b8e039545abc | -12.02164 | -47.80515 | 2026-09-22 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 45f9c2c1-4235-39f9-b10b-5eaf0dced0fe | -7.50146 | -45.4506 | 2026-09-22 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2c6531a8-28f3-3de5-867a-cbe2e137e749 | -9.89795 | -48.41655 | 2026-09-22 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60b83c6c-5ad8-3398-9061-9125d49fb82b | -3.90041 | -51.89465 | 2026-09-22 04:02:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ec58fb52-d1fc-3c4f-b661-e94a4b37bfc7 | -7.58689 | -43.42285 | 2026-09-22 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45632af6-557d-3e05-a58a-6e9ca35f9e8c | -11.6657 | -43.46362 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 93c58b75-92a1-32a7-8bad-3842e62a73dc | -11.32846 | -51.37268 | 2026-09-22 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8584cd25-1337-306a-a631-2337c80cab8c | -6.90057 | -41.69366 | 2026-09-22 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 95ecbeb7-abf5-3f4a-8918-9da8ab255e98 | -11.13698 | -42.79585 | 2026-09-22 04:02:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0910d3b3-1da7-3a5d-b61d-de4d9d357c5d | -7.82847 | -45.25698 | 2026-09-22 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f554324f-6e37-3da1-b10e-ad58097f57b1 | -6.78156 | -48.66578 | 2026-09-22 04:02:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a40972cc-77bd-3c06-bd64-33758044ca1b | -7.45508 | -44.74264 | 2026-09-22 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 45168fe8-0f16-3293-b514-8d9948d7d453 | -10.85876 | -50.89843 | 2026-09-22 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 381ee368-3dad-37a2-acf6-61b827b1901a | -11.26352 | -43.40522 | 2026-09-22 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c053e888-b12d-306d-9fe9-6cb6bac60b6f | -12.13127 | -39.41109 | 2026-09-22 04:02:00 | NOAA-20 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a316228f-f991-355a-9f8c-db93b5519856 | -6.00938 | -44.96731 | 2026-09-22 04:02:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8d24aec-8d3d-3e91-a05f-0d6b872c1a1a | -8.31746 | -44.74644 | 2026-09-22 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1b2c6a7a-0cc3-3295-8d32-90a215d5ce1c | -11.14867 | -42.83697 | 2026-09-22 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cfdc977f-c2ef-3bf8-b7a1-bcc644f35d4d | -5.7587 | -45.08996 | 2026-09-22 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 97f719e2-d1dd-30d6-ba39-68d605e1bcb4 | -7.41797 | -49.85273 | 2026-09-22 04:02:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c0f5a33a-c227-358e-9f93-3069be35354b | -11.42936 | -47.35224 | 2026-09-22 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5f2edc6-e05c-330c-a8ad-98680b66790e | -7.72424 | -43.88735 | 2026-09-22 04:02:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d69d83e0-6d5b-339e-9781-31cc5342235a | -12.56458 | -45.96615 | 2026-09-22 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 25aed95b-a16e-3f6d-a73f-3c21dd4703ea | -9.61797 | -43.92619 | 2026-09-22 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 32d339b1-7f27-3c08-9ec4-12f05ec94119 | -8.9205 | -50.93171 | 2026-09-22 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9c204a2-e2f6-37d0-8cf4-e3017b8efe1b | -5.33843 | -43.30236 | 2026-09-22 04:02:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 567bad31-4d9b-3181-a71c-39223b995bb8 | -6.66682 | -47.3736 | 2026-09-22 04:02:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f7b38b3-1f93-3dd2-a6ff-3dd0e6c2d710 | -11.84238 | -46.81557 | 2026-09-22 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ef4dbd3-55a1-3f51-8d3d-6034aa7881ac | -11.84608 | -46.82119 | 2026-09-22 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README37.md)
