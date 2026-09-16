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
| 2e17b0e9-88c5-3c3d-b0d9-8a1b4ac036dd | -9.2267 | -46.70661 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10f2b77b-75fc-3ee4-b38b-1fbf6c5e91ca | -11.17168 | -42.81287 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 57753a85-40b2-3e72-b8d2-e9e4997ba7eb | -4.52234 | -54.96973 | 2026-09-16 04:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e56c83de-9637-3e14-87db-fabb42caadca | -6.72404 | -48.11165 | 2026-09-16 04:14:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7f6522ea-9a8a-3bed-b21e-a18012620953 | -8.21556 | -43.78226 | 2026-09-16 04:14:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 14d2e29d-fe2d-3d69-987c-a51246682323 | -10.76819 | -46.22281 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 29a0e7eb-0dd9-370a-ac1f-7256cefe0a77 | -10.59549 | -47.75885 | 2026-09-16 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 863d056f-343a-3cd2-94b4-3c0749ae81bb | -4.51583 | -54.94974 | 2026-09-16 04:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 753aafe1-49f1-3fbb-aec0-1d62395d5dac | -9.23669 | -49.58345 | 2026-09-16 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03fa92c2-d88a-3a22-a1bd-1eff43c72939 | -4.51186 | -54.97131 | 2026-09-16 04:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6dc0cdf8-2279-3592-b50c-e8583e375a49 | -6.34696 | -55.5633 | 2026-09-16 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76577ef1-2187-3eab-83d1-18ad987a28ff | -10.83625 | -46.1988 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c89899ef-00cc-34af-a3c0-e841da2db9a8 | -3.31672 | -47.14149 | 2026-09-16 04:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3c08f843-02c0-331d-ad6f-f72ea5007f8b | -6.15572 | -36.48243 | 2026-09-16 04:14:00 | NOAA-20 | CURRAIS NOVOS | RIO GRANDE DO NORTE | Brasil | 2403103 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ccccba9d-75cc-344a-90d4-cd8a1e485333 | -7.51791 | -47.33668 | 2026-09-16 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b5d60e7-d618-3af0-9497-513774446daf | -10.83036 | -46.189 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69ea4c2b-8a94-35c9-bc60-3647a85e95f8 | -5.64766 | -44.29966 | 2026-09-16 04:14:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbb8f76b-5d67-3ca7-8d16-e6ccedec1f32 | -11.17997 | -42.80342 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7c7125a7-02ff-30ce-9f0e-9e0961752e91 | -6.3504 | -55.56493 | 2026-09-16 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c8af793-cce1-3bbc-8589-29e225799a64 | -8.54351 | -44.4996 | 2026-09-16 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dbcf666-11fe-3609-8dbd-1acb77c423e9 | -7.34361 | -44.478 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd24d4da-5bc7-3a0f-bb5a-242c762e22ff | -2.89854 | -50.43797 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f901b835-d2c1-3cd8-9eb8-c50da58aa3f3 | -3.84149 | -51.76797 | 2026-09-16 04:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b0b114b-a4a2-3fcd-b31b-3673cf47925f | -6.82938 | -43.52703 | 2026-09-16 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b90fae03-66c7-3678-a20b-aa2ee0c9098b | -7.19377 | -40.15948 | 2026-09-16 04:14:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2a9b5a31-b760-3280-b5b5-83de50f23e83 | -5.12065 | -47.60772 | 2026-09-16 04:14:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4b6d2565-9d6e-3b45-9302-e86dbad78bdd | -5.98401 | -46.6347 | 2026-09-16 04:14:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3c620eab-e41d-3e35-b9bc-74cacff9e1e3 | -7.34232 | -44.48579 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c4cb7b7-6cf1-3e74-84ba-7791b44a071a | -7.03911 | -42.03346 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b1a42395-94d9-3ff9-9ef8-a7bd2c4c2fc2 | -5.62973 | -51.67475 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce40a4bc-89db-31bd-8971-036ef4c53d4b | -9.79314 | -48.80957 | 2026-09-16 04:14:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fe6e8de-a671-3eb1-a00c-fc96dd781753 | -4.30001 | -49.12749 | 2026-09-16 04:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9ebcf8d-76ce-3bd7-a8ae-f413c60d0ea0 | -5.71728 | -46.19218 | 2026-09-16 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6299d48e-b2c6-35f9-88c0-10c5aac87ad8 | -10.46239 | -44.95208 | 2026-09-16 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| efd88ec8-bb86-3ec8-a166-c00b887d9e3c | -11.37119 | -43.94353 | 2026-09-16 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89ed9137-586f-35cb-a4fb-07e645a4420c | -5.57743 | -43.56827 | 2026-09-16 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23e62a97-c104-3c8e-95b2-5de51443d65f | -7.09891 | -43.52852 | 2026-09-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03215fcc-f18f-341d-9105-08f99f2bff1d | -2.91789 | -50.42308 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a407c0e-5703-3ebf-b8de-13566c7eab25 | -7.15453 | -44.24034 | 2026-09-16 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2cedfb2-dde7-3ed6-9525-aa38cf32123b | -11.17608 | -42.82797 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2c6ec3c1-764d-3ea5-b051-7d1c417a5d4c | -8.84612 | -44.90546 | 2026-09-16 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01a4bef1-e73e-3ec1-82b1-770a1c93272a | -6.36269 | -55.83195 | 2026-09-16 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41e04499-c274-329b-bfdb-65b7204f2ef8 | -8.55042 | -44.50086 | 2026-09-16 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 105c5d43-e40c-3a62-b770-3e3cbcf94be8 | -5.71712 | -46.19484 | 2026-09-16 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 987b06e3-9791-3e14-b09d-1fd92736d4fd | -7.00954 | -46.52133 | 2026-09-16 04:14:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bca320e4-6bbc-36c7-904c-6c418ad50682 | -7.09005 | -42.09868 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3034e6e6-5bcc-30cc-9c9a-78e467222df4 | -11.36726 | -43.94656 | 2026-09-16 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b70ed59-a879-32b4-872d-52edfcdd9c84 | -5.6381 | -40.86048 | 2026-09-16 04:14:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 53aca1df-a256-3878-ad3e-243b4848b47e | -5.9897 | -52.1069 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 167ac2d9-f53c-3321-98da-860ff9146712 | -7.33466 | -44.48854 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c37343f7-cff8-3011-b811-5d74685bc1d4 | -8.39692 | -42.21165 | 2026-09-16 04:14:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 53ca5a00-96fc-3d61-a154-9c2535382be4 | -9.34752 | -50.17895 | 2026-09-16 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33aa3ce4-c0c6-3690-a981-ddd88d6708d1 | -5.99549 | -52.108 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff504187-f52f-37ea-aa22-305fbbbdba88 | -3.08032 | -50.56833 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb8de6a1-82f1-3e96-a061-d790b8c3bc71 | -5.63145 | -40.85944 | 2026-09-16 04:14:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 640f1f80-8160-3e1d-b89e-ff871445f614 | -8.7797 | -45.89656 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c4abe60-2919-319c-bf3b-1a5a6622a914 | -9.57075 | -46.59695 | 2026-09-16 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db213300-40a8-3af6-b4d4-3bf79a61b808 | -7.09072 | -41.77195 | 2026-09-16 04:14:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 77921a23-5ec2-36cc-97ce-4428fda935a9 | -11.24766 | -43.44528 | 2026-09-16 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edfc7e2c-4965-3c3f-a93e-ad99c3f2baf4 | -9.78646 | -46.49001 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd0cdf13-5d08-34a9-b72d-10ea3aedf88f | -9.75878 | -46.58515 | 2026-09-16 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26f9f1ac-3df1-369b-9c49-a883822d5dba | -10.83551 | -46.2005 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f80ec0f-9169-3a77-864e-7c1d83835ec1 | -10.83623 | -46.19632 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f565ee84-9477-37cd-9f6c-c624d3e8297e | -10.10538 | -45.57253 | 2026-09-16 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9bb27704-22d5-390b-bac5-aae6f836b483 | -4.51789 | -54.95385 | 2026-09-16 04:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 50d999de-d0b1-3c58-b000-fbb109117694 | -8.85317 | -44.90654 | 2026-09-16 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2de568a0-198f-3607-928e-46463fba7de3 | -10.56043 | -44.61107 | 2026-09-16 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c35dc98c-56be-39b6-a702-ac570d17ee30 | -7.13162 | -46.58484 | 2026-09-16 04:14:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c7625af-2af6-3cf4-8bdf-c3bb3e8891c8 | -2.90269 | -50.41321 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 042204ce-5943-3a56-b45c-9381dfce58b4 | -9.7606 | -46.10045 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4771b561-d6a4-3ed5-aebc-5cab581b0128 | -7.09343 | -40.65067 | 2026-09-16 04:14:00 | NOAA-20 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| eb4fcbef-a6d5-37a7-9d06-492903a9f14d | -4.40849 | -42.31467 | 2026-09-16 04:14:00 | NOAA-20 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 97d3505b-daa0-3566-8249-ab83adc92b1c | -8.47297 | -44.57173 | 2026-09-16 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4c0e75f-fab2-3f94-8765-80749e3da171 | -8.54416 | -44.49568 | 2026-09-16 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dd5978b-4b3a-3a1a-9c3e-7719d1a9f429 | -11.14161 | -40.47836 | 2026-09-16 04:14:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 2fcde8cf-885f-388c-a987-6c2932827e45 | -5.83804 | -51.95429 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4702d0de-db14-33a9-a1ed-9f6cd2e6dd20 | -9.5484 | -45.41788 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e4af8806-95e2-32d8-8219-bf9177b454a5 | -9.8107 | -48.91569 | 2026-09-16 04:14:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60c199a7-af6d-3e79-ba33-cc6163d14025 | -10.43997 | -42.73717 | 2026-09-16 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df089c3e-c73c-399c-a1dc-190ae82fb4d4 | -3.39965 | -50.75469 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 275828b6-0d97-37bc-b727-75fcd6b61eab | -10.59271 | -47.75107 | 2026-09-16 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4631519-e0c3-3a10-a324-ef415e8bf145 | -7.17806 | -46.11971 | 2026-09-16 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f59c846d-90f6-3b0e-a8aa-b68c1837b875 | -9.86149 | -49.82187 | 2026-09-16 04:14:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fc451308-09f6-3888-82c5-2d752da85d45 | -5.60609 | -44.84977 | 2026-09-16 04:14:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7860819c-7fe7-3909-8e2c-2e053e2e0ea1 | -9.84304 | -48.35149 | 2026-09-16 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e35109e-d4b5-392f-96b3-8a920d92356e | -2.90815 | -50.41413 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85a58ce0-b75b-3ea2-834c-8f7e18d98f02 | -8.83907 | -44.9044 | 2026-09-16 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55c900d9-78e9-31a7-9789-2d00da6049aa | -9.76225 | -46.09895 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37d56ead-2b95-3a51-aec3-8ceed8e8d196 | -10.59211 | -47.75452 | 2026-09-16 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d07b56ab-c3e1-3937-bfee-fae773e9f54d | -3.10482 | -51.83013 | 2026-09-16 04:14:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e4db11b-e13d-3410-a8c1-0a2f7e55a2e5 | -3.39224 | -50.76483 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47629887-364f-32b4-8a36-bc594488d2c7 | -2.9111 | -50.39652 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a8fad33-6780-3827-9b07-e3f3159051a1 | -9.33373 | -44.38944 | 2026-09-16 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 567ef1e6-b05d-3962-ba08-462f253c1ade | -10.89835 | -46.2966 | 2026-09-16 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c98f07d3-ca52-36d1-a7ff-a4c0bbed6f3e | -7.51299 | -47.56461 | 2026-09-16 04:14:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1005678-de6c-3f77-a931-4c96d86484cf | -8.37927 | -42.21595 | 2026-09-16 04:14:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1798baa4-0c5a-301e-9d93-a14fa3b1883a | -11.36217 | -43.95676 | 2026-09-16 04:14:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eeeed6ef-457e-3107-bf57-94340a6c89f6 | -6.78352 | -48.66047 | 2026-09-16 04:14:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c4dd7f3e-52e5-3882-99d6-27bf28f57923 | -10.41419 | -48.65617 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a0905eb-c996-3950-8363-35f01ecbe65c | -7.21724 | -44.45337 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |


[Clique aqui para ver as próximas entradas](README27.md)
