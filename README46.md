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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ad2508d-2f09-3453-9f7f-49bca75e78c7 | -10.35634 | -47.17908 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4bd4a529-89ea-32d8-98c3-02b30768d5f5 | -10.87899 | -54.04736 | 2025-10-27 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28762c32-374d-3817-ab82-db262e258623 | -10.31431 | -47.18361 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be5a11a4-65dc-3f19-afa4-c9e60a4f8e00 | -13.26648 | -54.36762 | 2025-10-27 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 61e84a7f-343a-3af4-b961-99f161253222 | -13.42758 | -47.38802 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 419a305b-8b77-3709-a96c-8965ddaf3ee4 | -10.35408 | -47.17127 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 746dede5-73d0-3372-a6cb-545df0bf49b4 | -14.94402 | -47.33569 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b07f6cac-20df-3665-b6f7-37762b945373 | -15.45062 | -50.48591 | 2025-10-27 04:34:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a49f13a6-9d83-35ee-a688-e437b3b79e2a | -10.33381 | -47.1459 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 323eb089-a7d8-34ab-87ad-a46a7e6f3efc | -14.49841 | -47.88983 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aba9264d-7bb5-37bd-abf3-35401527cdb4 | -10.83186 | -47.62554 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6a8310d-3020-3246-ac6e-609d39a99a04 | -11.42919 | -46.11081 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d46cf7c-d46f-34e7-9da1-f556b01263b9 | -11.02241 | -47.80184 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2acc5d0-f095-3c9b-956f-a2ddab903d05 | -17.31758 | -43.65488 | 2025-10-27 04:34:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c76cc832-5ff0-30d0-8e9c-0d9483c2e4cc | -12.12896 | -45.21099 | 2025-10-27 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22fb6dcc-bdfa-3b76-8dc2-beb3fa67d756 | -12.85208 | -48.63707 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d71de60-4561-3d89-a653-60a0415f9d91 | -11.10783 | -55.55685 | 2025-10-27 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f80a685-5653-3c60-aea0-67bce67f0cb0 | -10.92564 | -48.03342 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5a9b453c-5097-3296-be9b-814a5c4bc983 | -10.85634 | -48.95795 | 2025-10-27 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdef1a2b-9f75-3123-a395-22fea565fa49 | -12.27933 | -43.75842 | 2025-10-27 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30cde354-283d-3846-83d0-cd5965142ede | -10.21353 | -52.65794 | 2025-10-27 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a507dee-6cd0-318d-aee4-a6a6af822d22 | -12.06168 | -43.98736 | 2025-10-27 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8a6aba65-2cac-34e1-9957-bad7a13c2d60 | -14.54388 | -47.98855 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d43fa095-d3a8-38ba-8cfb-664984e665a0 | -10.88011 | -44.33734 | 2025-10-27 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a08caa43-0c82-3454-b5ea-c6ed1a5418f2 | -12.8946 | -54.73292 | 2025-10-27 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f9042a2-d7c1-3a62-a440-23f21c68a032 | -10.92063 | -48.02176 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e3f0e73c-3c5c-3a4c-9c8f-ea95f46f0197 | -13.64033 | -48.4413 | 2025-10-27 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 58f5a29e-71fe-3faf-856e-35707594d01f | -17.32254 | -43.65108 | 2025-10-27 04:34:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d3cd4fff-9bd2-3877-8c07-f1a471edd4d2 | -11.0632 | -44.78658 | 2025-10-27 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef3a5901-db0a-3c56-93ce-cb21be2100f4 | -12.86922 | -48.65781 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cea3bbf4-34c7-31b2-9297-b4588cc1dbbe | -12.35585 | -48.1277 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5fe3eaa-d43c-3ec8-90c6-e1d2d3d2edb8 | -13.25812 | -47.98167 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb90f560-43d1-35c2-9e23-f13c8c1e6843 | -12.30711 | -47.4475 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d04ad718-a248-3319-a96f-3cbc765522ce | -14.57038 | -47.99639 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfdb0a03-2dd8-306d-b073-dd7483ec91a2 | -12.86591 | -48.65727 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c0aaf73-a56c-38b2-ab61-980b51ec4b21 | -13.26928 | -47.97598 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9503c712-a23b-30fa-978d-072b32af90e6 | -13.6007 | -47.59253 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a065d6d-a65e-3dbf-b1ba-3bbe0e670f1f | -12.39514 | -47.66389 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11f9bf0c-1a06-3f89-8382-807ea9412c18 | -14.26154 | -48.13393 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c2d77cf-1d4b-31f8-8761-3aff5427bc95 | -10.57161 | -48.01305 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e0211049-48ba-3e8e-844f-f759c1569c01 | -14.6401 | -48.41437 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 545b8ba9-0ba5-394d-b495-aa90c838ca55 | -14.55742 | -47.99051 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9cbe298-1278-3940-ae28-6e1490908235 | -15.51609 | -50.0095 | 2025-10-27 04:34:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 773df363-b1c2-35df-8711-afc5a3eee91e | -15.17735 | -47.22131 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66e3dd55-8369-3a27-b094-88d3f281af59 | -14.37002 | -51.52549 | 2025-10-27 04:34:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3664ecd-bfe2-3a36-a3a8-c993774d7012 | -12.28146 | -43.83261 | 2025-10-27 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44b908c7-f546-3cb9-ae2b-fa922d02d93a | -10.31658 | -47.19141 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3cee6654-e398-3eda-83ca-50689dd361e2 | -12.5569 | -39.62602 | 2025-10-27 04:34:00 | NOAA-21 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 92d0128f-3089-3d9b-bca1-847805870cc1 | -12.32758 | -47.48121 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6853a6cd-80de-3082-bec6-8b157c369fb1 | -10.20899 | -52.6619 | 2025-10-27 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e85c98fa-1d42-327c-941c-4e82fcb2188b | -11.44063 | -54.09187 | 2025-10-27 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 104950cd-42ec-3b52-a210-a5ab7c4f77d0 | -13.26584 | -54.37117 | 2025-10-27 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 258249ff-b314-3c82-855a-6f1eeeb099a8 | -9.84337 | -52.26968 | 2025-10-27 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66c746cc-4385-352a-9fb3-c54ced0688d1 | -15.45393 | -50.48648 | 2025-10-27 04:34:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50b6623f-71e8-3502-b462-99dd7ada6a4e | -15.24371 | -46.05352 | 2025-10-27 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d40cf94b-1477-3075-a11e-ecc9fb07a1b0 | -11.0203 | -47.85998 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a975620a-36bc-37ec-97d3-bdcfa3c1afb1 | -13.26538 | -47.97906 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| deb153ff-1698-3626-9175-5ca47c49288d | -11.33126 | -47.89376 | 2025-10-27 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1623e9a5-5433-3391-b798-1966151d0efc | -13.2832 | -54.3892 | 2025-10-27 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 592353a0-8cc4-325b-b7c8-f7f515caa8e0 | -17.40537 | -46.88605 | 2025-10-27 04:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07542953-32e7-3653-8a0d-79ea2adb9278 | -15.18491 | -47.21828 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34b72184-3fe6-3006-b8b5-e8658ed87b47 | -10.58156 | -48.01456 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4895c23c-8dad-30c9-80eb-b12b4920edb0 | -10.88462 | -47.96865 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4f5d2c64-7039-38e2-9885-de3db7d8f419 | -10.63079 | -52.19027 | 2025-10-27 04:34:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a5605d36-eda6-30f2-abf6-cdcce77e6f12 | -11.91723 | -43.82445 | 2025-10-27 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 03d2fcc1-6633-3869-9acb-3cd87bdfbc0a | -15.18084 | -47.22187 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cce7070-495d-371a-b48f-57001e529379 | -12.07411 | -47.99194 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c15cb87-2ed8-3c3c-ac48-68948289c3de | -17.43385 | -46.86792 | 2025-10-27 04:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba715f37-cc4e-356c-9673-6e2d331ac8f8 | -12.34383 | -47.11238 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 236ab6b2-3532-33b0-8b16-c8aff5010bcb | -12.65798 | -52.62556 | 2025-10-27 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6e3746d-f23b-33e5-830c-497d0927482a | -17.43686 | -46.87292 | 2025-10-27 04:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d6703af-268b-35eb-b52b-431342e488e0 | -13.04467 | -45.86531 | 2025-10-27 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2549a928-8080-3ead-a388-db4a0233306c | -11.03413 | -54.26202 | 2025-10-27 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed7a413f-314a-3eaf-bc9b-077f88464841 | -13.64548 | -47.61867 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09b625d0-3e20-3d6c-b0e4-2ab45d08f18f | -14.62447 | -48.40443 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c33c2849-51c5-37e4-bc51-992eb5d42eba | -15.51553 | -50.01306 | 2025-10-27 04:34:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b2e6cfd3-ff51-385e-8416-441e4f751517 | -13.65513 | -47.62381 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e906e5bc-d5c8-384b-861c-f418404da0cd | -10.31548 | -47.19867 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| be4edd8e-482b-3029-8302-fe70b1f6b177 | -15.24741 | -46.05409 | 2025-10-27 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b5becec-b047-32f6-a7a3-32a8a618f38d | -10.04867 | -48.16341 | 2025-10-27 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 92ae09e7-b2e6-3745-99fe-253ddecaa66c | -11.03309 | -47.86541 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37b6ffe1-dd49-3447-8c26-4292d7d8398e | -11.42624 | -46.10624 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d8ba21b0-ce3a-3e94-8434-1445d6fedb63 | -10.75176 | -44.20035 | 2025-10-27 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a8ebbd0e-9e95-3e32-9e15-48fb0ec7e99d | -12.33996 | -47.46781 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 430bb19e-0a77-3527-8d4f-b6ba94c977b3 | -14.98228 | -43.55119 | 2025-10-27 04:34:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b14913ab-db70-3772-9a82-7908dd7d681f | -13.65173 | -47.62336 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2152d775-c962-3c4c-8058-cb69588500fc | -13.55852 | -48.53157 | 2025-10-27 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5aa79b9-2d84-337e-aabb-15953f840e04 | -12.32075 | -47.45743 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dcc98e40-1f55-3b18-b5f5-b30aabd0b8c3 | -11.42002 | -46.09856 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9575a7b-58d8-3fb5-b492-4d3dea25ac80 | -10.92008 | -48.02534 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c1f3f125-dc49-3ac6-b3ea-6c0f580f0a8c | -11.42387 | -46.09761 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 331b04c9-04cb-3dd6-aabf-be3a8b319684 | -12.52902 | -47.56418 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eddb5cd5-4aa4-3fbf-aaad-6227e130b1ac | -12.86537 | -48.66079 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aaf29381-c0c3-349e-a781-d5792ebaf87f | -10.63882 | -52.18716 | 2025-10-27 04:34:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 37af5a31-6c52-3662-9398-a337e592350d | -13.26983 | -54.37189 | 2025-10-27 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 24523f54-ebaa-300c-896b-d1028cd89003 | -11.05291 | -47.86809 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cede53e-32d0-367f-98ba-36c498953cda | -12.31736 | -47.45694 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9415c6aa-4352-33ac-a511-43642593dd62 | -14.3979 | -51.54986 | 2025-10-27 04:34:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1dbb5f51-429b-346b-a189-20d05d2f5237 | -13.64092 | -47.60262 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df485c8e-f5f3-3a21-9efe-4aeed2f42f54 | -12.20736 | -46.49972 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README47.md)
