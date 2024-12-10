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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a044b04-2578-32c7-8923-dfbe3ac889c9 | -7.00407 | -38.65403 | 2024-12-10 03:57:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f67bfdbe-0d8e-30e8-9de3-216dbc3412ce | -6.97398 | -34.94334 | 2024-12-10 03:57:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a1892cb9-2848-3115-b4c9-3704874d73e8 | -6.91648 | -43.51773 | 2024-12-10 03:57:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 192fb28f-41ec-39b2-b0f5-03b9e18c828f | -7.74685 | -35.26303 | 2024-12-10 03:57:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 14b4aca7-8a2f-35aa-98dc-cdc40768a9c8 | -7.75284 | -35.13601 | 2024-12-10 03:57:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| ab5dde3f-53d0-3bc5-99c4-60e78d4256a7 | -4.56146 | -48.92226 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b19b60b3-6d78-37af-8ef5-aa3cfa311c8b | -6.90129 | -47.83713 | 2024-12-10 03:57:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 88a9be10-e9fd-3bb8-ad2e-d7d309148b3f | -9.07935 | -35.7057 | 2024-12-10 03:57:00 | NOAA-20 | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a006b3c9-9634-3ac4-ba2a-2e999ae1cdb4 | -7.75684 | -35.13663 | 2024-12-10 03:57:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 57132541-43b7-3525-8919-0df7a916c9bd | -3.38833 | -52.67369 | 2024-12-10 03:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70ef480d-227c-3a8c-9a4d-e6ec6e101c11 | -6.25827 | -43.55597 | 2024-12-10 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 663caa22-7a1d-3d5c-88f6-a78a3e5ee2d3 | -2.91142 | -52.97173 | 2024-12-10 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0ca06889-7c70-3c04-bcf7-f0660763a19d | -3.32311 | -45.60096 | 2024-12-10 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c681221d-4c87-3a26-a7e5-30b9f97c2c82 | -5.715 | -46.54883 | 2024-12-10 03:57:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5c28daf-272f-34c4-b587-330e59f9d940 | -6.83295 | -44.38291 | 2024-12-10 03:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fad31440-f372-3eac-aca5-7e21e9cb9411 | -2.99329 | -53.02436 | 2024-12-10 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 23cf3e79-4c0e-339a-8e13-b35b5eee8ab9 | -2.98627 | -52.85518 | 2024-12-10 03:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 405a6711-8d42-3bf9-8087-0c036cf45e10 | -3.07132 | -40.04468 | 2024-12-10 03:57:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| eb513b73-b52f-33d7-921c-4b34cfb4dd55 | -4.14699 | -44.2866 | 2024-12-10 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e629ccb-dac2-33a1-aba4-beefc9fd8366 | -5.34099 | -40.8579 | 2024-12-10 03:57:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b9cf70cd-498d-3f0f-ac6e-f6f215523369 | -4.55803 | -43.30346 | 2024-12-10 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a546795d-1616-3bc9-8b42-e10f0036e309 | -5.57962 | -45.21073 | 2024-12-10 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8f2802a-b701-34ec-8803-9543feb4317a | -6.91205 | -43.52153 | 2024-12-10 03:57:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95babb5c-d64b-35d4-9632-1160a64ea05e | -6.83683 | -44.38363 | 2024-12-10 03:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6251d3f9-2208-303b-86b7-293cb18f5ed2 | -5.85045 | -44.78197 | 2024-12-10 03:57:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f7823db-75b7-337c-847a-13fcb8605937 | -5.43941 | -39.43722 | 2024-12-10 03:57:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 15781d81-fdd4-346a-b4a1-1b15f3ab048b | -4.84436 | -37.46046 | 2024-12-10 03:57:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 7a1e0729-adb8-331d-9a5e-39e876284cc6 | -5.8475 | -39.04388 | 2024-12-10 03:57:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 94d89fd5-b197-3423-8bec-1678bb2a9c12 | -6.31737 | -46.93214 | 2024-12-10 03:57:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c231d166-19b7-327f-b9ec-a6af7a3ae441 | -3.85362 | -40.44568 | 2024-12-10 03:57:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 38f67d98-e194-3cd3-a482-55455e409d0b | -6.544 | -40.50976 | 2024-12-10 03:57:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2e576102-0383-3b99-8876-3ccb436aac72 | -3.66604 | -39.48264 | 2024-12-10 03:57:00 | NOAA-20 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 68c15ac1-1d68-34bd-ae59-0c3b8f58cf02 | -6.90033 | -47.84251 | 2024-12-10 03:57:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 82084890-83e4-3f5b-8947-fbb2a83fef22 | -2.98856 | -52.86718 | 2024-12-10 03:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d6e21178-cf8d-3656-9828-6656b2b309db | -4.54562 | -48.01711 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6be53b40-a25e-3c24-8c15-2f8b5dd3cc72 | -9.03598 | -35.70389 | 2024-12-10 03:57:00 | NOAA-20 | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8b274d20-b063-3180-abc0-196027a4001e | -4.87788 | -48.21753 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ba2c6d01-4610-32d9-862a-3a9c1c8054f3 | -4.60344 | -48.50519 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56dc462b-786e-3c42-ae57-f5fc406ac8e6 | -3.80739 | -44.0382 | 2024-12-10 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8245a91a-f4fc-3cd3-a21e-1ce7f0dcd6e2 | -6.9026 | -47.84726 | 2024-12-10 03:57:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8abed006-5272-3f88-b005-cc0c26ca7031 | -6.73503 | -46.2911 | 2024-12-10 03:57:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db781269-ab7b-31dd-a88b-6b191850f1e5 | -3.97279 | -45.626 | 2024-12-10 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5ef479e6-3dbe-3f71-b0b4-264042de8b48 | -3.07076 | -40.0482 | 2024-12-10 03:57:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5a8d0823-c450-3c80-8fb7-7d662aa05474 | -3.23504 | -42.43239 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b355cbe-797d-32b3-8dee-678d04f00e33 | -4.60462 | -48.49818 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4fed402-e03d-34de-b4ef-8bddc69e96fc | -3.61184 | -44.78761 | 2024-12-10 03:57:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1959951-f191-3f5d-add8-8fa210a73fa5 | -3.0741 | -40.04872 | 2024-12-10 03:57:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 59747c12-c858-3c5d-bcd7-679b15f847b3 | -5.99094 | -46.15958 | 2024-12-10 03:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39766e1f-8aee-35f8-ac5e-c6688fd7bff5 | -6.91575 | -43.52213 | 2024-12-10 03:57:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d474351-e80f-3bbb-93c9-e8eeded7061b | -8.11204 | -35.06092 | 2024-12-10 03:57:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f3c26626-f015-3104-98e7-199b76f9fb12 | -4.54719 | -48.00786 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3af8d02f-bb0d-3ed0-ae5d-40e906e998e7 | -7.86003 | -35.19787 | 2024-12-10 03:57:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 155c41d3-d102-3d47-974d-c273a7509443 | -5.68594 | -37.35756 | 2024-12-10 03:57:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 9d28dc67-7118-30dc-90c5-f7523836c48a | -2.98259 | -52.85911 | 2024-12-10 03:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 7f759e89-2caa-378f-bf9f-0c86956e9243 | -3.39538 | -52.67477 | 2024-12-10 03:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7ab483f-3891-31fc-a20a-970772266769 | -8.38931 | -35.44288 | 2024-12-10 03:57:00 | NOAA-20 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| aa3583e0-0ddf-30c7-89e4-f45da46eeb79 | -6.26128 | -43.56102 | 2024-12-10 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8030fd03-ce9c-3c97-b269-48d092fa09b5 | -5.90933 | -48.06168 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 42a49023-7312-3241-aabb-4f4859275077 | -4.24491 | -41.92836 | 2024-12-10 03:57:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d794c2fc-89ac-35a1-b9b3-ad32c23d8f16 | -2.77252 | -44.99578 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 88473d3b-d2f0-3f16-ac7e-fba4355ea89d | -7.9165 | -35.2026 | 2024-12-10 03:57:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b6719c77-0ac3-35f8-88b7-e77e0f94ce3f | -4.17094 | -45.54585 | 2024-12-10 03:57:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 125489f9-1421-3e6c-8a34-e07f7bfb8a1e | -6.59623 | -44.16318 | 2024-12-10 03:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a83146ee-ba07-3e73-961f-95d9f47d05b6 | -3.81743 | -52.24885 | 2024-12-10 03:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d0b518f-af43-3bb0-96b0-7932ded7f3cd | -6.33646 | -43.43962 | 2024-12-10 03:57:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 337beb95-2a82-3513-bfb3-e0ae28b5baf3 | -3.38023 | -42.32304 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.3 |
| d6e47cb9-3392-36d0-bdc6-0350b4b7868b | -5.44423 | -45.58829 | 2024-12-10 03:57:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d3700c3-07b1-3295-a268-314f7067b904 | -3.31712 | -51.48478 | 2024-12-10 03:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6a45fd7-2afa-3a08-a5b0-7e529001c0cb | -8.41771 | -35.41475 | 2024-12-10 03:57:00 | NOAA-20 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 487887fd-e8dd-3dbf-a1dd-65413829a7c9 | -3.85698 | -40.44621 | 2024-12-10 03:57:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3992897b-489e-3d98-a2df-30aa5668a4f5 | -8.35347 | -35.33713 | 2024-12-10 03:57:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b1775b01-e0df-35c9-8ac4-04f4281dcddd | -7.25054 | -48.42043 | 2024-12-10 03:57:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5700450-6188-310a-8f69-4e2cc833f59a | -5.34043 | -40.86146 | 2024-12-10 03:57:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bffd494a-df9b-34d3-8fe0-2165b3ca90a9 | -4.82821 | -47.31224 | 2024-12-10 03:57:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06f9658e-d877-3c77-a836-edee9c279992 | -6.94601 | -45.06817 | 2024-12-10 03:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 480ba7f2-1d0a-338e-930f-1c40f424ba91 | -3.68362 | -49.5762 | 2024-12-10 03:57:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ead2907-39a9-3416-a316-30860bacb704 | -3.79917 | -50.02108 | 2024-12-10 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f8b2340-2f9b-3f22-8a2b-3657445c2989 | -5.87562 | -40.16077 | 2024-12-10 03:57:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| feb3649e-6c60-378f-9277-e46272a4fe12 | -2.818 | -52.98396 | 2024-12-10 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 4daa7104-525b-357c-bc07-ca590ff47975 | -4.14415 | -49.31816 | 2024-12-10 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3f7fb0c-c6f0-34cd-a2db-5b3b0fbb298f | -5.12891 | -36.38439 | 2024-12-10 03:57:00 | NOAA-20 | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| abc0ef98-850c-3490-8e2e-13ca0465a3e7 | -8.8817 | -41.10633 | 2024-12-10 03:57:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 94e56147-a1d8-3488-96e3-86f3a97bba67 | -3.34821 | -42.33187 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c01028e4-e8d6-3e0b-aa84-a93e8f047b82 | -3.23071 | -42.43612 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa6785b4-7a5e-393b-899d-2b2a0557c44a | -5.91441 | -48.06243 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d6bfce4d-db43-31ff-8db0-e8389d56c39a | -5.92156 | -48.0513 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bd9f482-38df-3bbf-9830-53fe266a5301 | -2.91067 | -52.96221 | 2024-12-10 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 90afae62-87db-3506-bccd-7fe6138772e3 | -6.91793 | -43.50893 | 2024-12-10 03:57:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ab082db3-ed4f-3e4d-85d5-c6b9c5a399ec | -3.98984 | -44.17423 | 2024-12-10 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b05ad3e-d439-3972-ac81-36384a503f52 | -5.91038 | -48.05571 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d84ec743-59ed-3539-a211-6b2338e4aaff | -3.82785 | -52.35427 | 2024-12-10 03:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4be22d0b-26b4-35ec-ac35-6de627cb8733 | -7.75156 | -35.25851 | 2024-12-10 03:57:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a1a88cba-3d89-301f-bf49-a346082256af | -3.80275 | -52.25246 | 2024-12-10 03:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e0370d5-6409-3ecb-8bdd-aa18523fedb1 | -6.58537 | -38.45066 | 2024-12-10 03:57:00 | NOAA-20 | POÇO DE JOSÉ DE MOURA | PARAÍBA | Brasil | 2512077 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 44eb19e8-c13f-326c-b464-fe2a3adce5ac | -4.56123 | -48.92531 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da198798-4818-3d55-bde4-6f0246b471f7 | -7.75334 | -35.13254 | 2024-12-10 03:57:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 0e45df07-350a-3be1-8cc3-19559820d261 | -1.64256 | -45.906 | 2024-12-10 03:57:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 06bed6bc-39f1-3477-8686-ad0846927544 | -5.63194 | -44.84217 | 2024-12-10 03:57:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d7775c82-cd96-324c-b52a-dce15826c402 | -6.03252 | -38.0234 | 2024-12-10 03:57:00 | NOAA-20 | PORTALEGRE | RIO GRANDE DO NORTE | Brasil | 2410207 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a3d959bd-3ff2-3b03-9ff7-825aadeb399f | -2.91651 | -52.97153 | 2024-12-10 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README15.md)
