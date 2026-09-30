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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ba5c24b-2bb8-35f7-80c1-f9056420ccc8 | -10.71786 | -44.42686 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b94c15d4-a842-331c-a4a3-1b17e4b1dc8a | -11.39652 | -43.47269 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| db2a5a14-7595-3763-aa80-f1f703e9c983 | -10.83382 | -48.71489 | 2026-09-30 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24bfa9e9-9d8e-3e78-9d2d-bea5e005602a | -11.71321 | -43.44668 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf48b76e-1691-3f03-9375-3d5636555bd7 | -11.16944 | -44.82493 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a029d2c6-fb11-3b52-a71d-feaaf659e569 | -14.53425 | -48.29041 | 2026-09-30 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8314a3c0-1e8c-3d35-a727-2c9a78e44483 | -11.44085 | -43.43953 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5d8b2019-385e-36a9-a190-c905dfae9017 | -10.74936 | -50.50471 | 2026-09-30 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1a2fb9d-1205-313c-af84-f1f6d78d4070 | -11.84615 | -50.96717 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2314e693-765e-3e3d-99db-81d87e0322f1 | -11.31075 | -50.98207 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e754943-d259-33cf-a916-0d1cfa7bd625 | -11.38746 | -50.96925 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a2ded281-9216-3215-a268-a6ef32e288cf | -15.75206 | -46.04022 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00553dc6-f0ed-3730-a648-aa7dd0b18f6e | -14.60944 | -48.94025 | 2026-09-30 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00327411-4d5f-3c06-aa05-95c4897f02d1 | -13.37935 | -44.01971 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbd9abb0-e291-3682-afc0-fbd1ec6ec783 | -10.81299 | -48.72869 | 2026-09-30 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e6bd623c-89dc-3081-9e0b-5868568b3102 | -9.69504 | -47.65537 | 2026-09-30 04:34:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 207235f1-3fef-32c8-ad06-4458b48d6b06 | -10.25534 | -48.33077 | 2026-09-30 04:34:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfcd59c1-dbad-367f-8040-23341bc2de5d | -8.12272 | -54.85521 | 2026-09-30 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 287ef126-a8f0-3987-994c-880cc547bbcc | -13.93003 | -43.80051 | 2026-09-30 04:34:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6aff1403-5116-36e0-ac70-4815290669c2 | -11.16323 | -44.77623 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eda8b97b-192b-32f1-a73e-54c8f7c0c071 | -10.55155 | -50.87162 | 2026-09-30 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68a904a4-8b9a-3992-a647-508792dc7d83 | -11.16379 | -44.77264 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10b0d3da-3e4a-3536-b870-3c7bf9bd5525 | -11.84665 | -50.4761 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53e7e4cb-1eb4-3e56-9121-2c194c10cefe | -11.1946 | -44.83995 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| c92c476e-fbee-3ed8-98db-8047de69a0ed | -13.36732 | -46.81549 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3390a2ed-7e17-3c06-b575-a67766a6afcb | -11.36498 | -51.0253 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 422f9b46-0fa3-39ef-aab2-caa0528faee8 | -12.34205 | -48.19547 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dccdba72-3f48-308a-99d7-1296ad4e3961 | -11.43445 | -43.43453 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82121960-efe1-3aff-b99c-962997069446 | -14.13234 | -46.26257 | 2026-09-30 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e356dd5e-9630-3127-9f61-340c1509a4e2 | -11.62515 | -43.53061 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9dd04c4-2119-30ed-8e90-6e23a489c116 | -8.05862 | -55.34137 | 2026-09-30 04:34:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff5c6370-b0ed-3b27-98a7-6cdb07442e60 | -11.40059 | -43.46934 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9d1e4d03-a89f-3182-b545-897d1f849afe | -15.97794 | -48.14031 | 2026-09-30 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8254c99e-b5ec-3e11-942e-d4e976cecbaa | -11.82071 | -46.89759 | 2026-09-30 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e81f492-18ed-3ec8-9df9-418edab9d535 | -10.13416 | -45.13262 | 2026-09-30 04:34:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6eefc5ee-4ac6-3469-b709-d0140b67990b | -11.30261 | -50.98061 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 78e4379d-f189-3436-a575-34c2ff206783 | -14.79884 | -45.95623 | 2026-09-30 04:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 789309c1-d9f2-3f78-8a63-1942d6cc31b4 | -10.96146 | -43.88866 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21f8a495-40a5-3b34-9986-72858f9a695f | -13.38011 | -46.82125 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ce5a2575-184b-3cd8-93fb-c7df6e43b170 | -14.10291 | -46.27596 | 2026-09-30 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbd8985e-cdb3-3fdb-8a61-fa6f63de407c | -10.13471 | -45.1291 | 2026-09-30 04:34:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93c76831-ddb0-3c14-af60-1ec44310dbec | -12.78182 | -54.00919 | 2026-09-30 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f9b4331-5cfd-3287-badd-eea6de1babb5 | -10.68489 | -50.28854 | 2026-09-30 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c97138b-1e33-3e11-9be9-2bc519ba9343 | -12.69783 | -43.22995 | 2026-09-30 04:34:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65a7f98b-4e33-3cb6-8e48-8749900e455f | -11.29917 | -50.97623 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4a63fa27-250b-3d20-9ab2-fe2c8105aaf1 | -13.52863 | -49.1757 | 2026-09-30 04:34:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9685ac1-d528-3cff-b34f-7580d5781818 | -12.30766 | -47.95253 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4da0d4b5-7c2a-31a7-a4d2-c20b4dfcd0b3 | -15.19876 | -46.1432 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04d3107d-958e-3a62-8073-f8fc14a652f8 | -11.43025 | -44.93626 | 2026-09-30 04:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4959832-c030-397c-9dfe-57f611f311bb | -11.1672 | -44.81725 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 79bf8c58-de9a-368e-87b6-e296f5ed8288 | -15.97518 | -48.13602 | 2026-09-30 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c14e068a-262b-3f70-9c12-2ab77357180e | -10.73361 | -44.4367 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5fb888a-ac0e-3ccf-a7d7-62d75bde002a | -11.2627 | -43.52447 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ad68c20-ffe1-3dee-9473-bf112ee191ac | -14.85625 | -48.18163 | 2026-09-30 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11a438a2-3750-3ad4-83aa-ea63ac1935ee | -13.33053 | -43.93657 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22999f55-c001-37e9-af60-6a9ba1fa4e68 | -11.37046 | -47.44962 | 2026-09-30 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9eb05948-e468-3055-9cf2-c71ed9945820 | -11.81793 | -46.89343 | 2026-09-30 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf6f9236-a55e-336f-84d8-87f3573f725e | -15.78676 | -44.68873 | 2026-09-30 04:34:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ba3c4bb-c911-338b-965f-32ac2e126972 | -13.36562 | -46.82609 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4953a716-2537-32c5-8833-db33e84ba4d0 | -12.07647 | -46.4528 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80a9b0ea-5ca4-3746-8531-e796fb444ed6 | -11.83904 | -50.47722 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4cbd6f8b-caf2-30e9-af6b-a1f3b6afc9a5 | -11.3971 | -50.98601 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fda98e98-5594-3b55-bff4-c024062eaff9 | -11.85143 | -50.96076 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bec14d1f-9fe2-3981-a5ac-4d35900cc0c3 | -11.16098 | -44.76852 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d423408-7013-3b04-8b54-c805ef5f9db8 | -12.30703 | -47.95632 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| febc9fff-de6b-3c5f-8530-a43f0ffd22a7 | -9.86647 | -44.94617 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 987bf456-1fb2-3add-ab20-01f0b6cd74c0 | -12.07476 | -46.46345 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 821c0722-2920-3c5e-a74c-76a386cb0669 | -11.17055 | -44.81779 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 47864f27-e00e-3b4a-9110-31993ce19f24 | -11.42164 | -43.42453 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf1c9fad-859b-3f87-928f-e336a8306e9c | -12.23994 | -50.24949 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6101c142-8f20-318e-a4fa-f03560463dc5 | -11.26618 | -43.52502 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4153b070-e381-34b2-8bee-c317b3a507b3 | -12.44022 | -44.16997 | 2026-09-30 04:34:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94610e69-d75a-337c-b110-0cffaa22f630 | -11.392 | -51.01517 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4423ab0d-091b-3d2f-90d2-03051db84465 | -11.16775 | -44.81368 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8ab471be-3a30-3a14-a8c4-ff2641fccd00 | -11.39302 | -43.47215 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e7bbd771-d74b-3df6-bdbe-5ebdc626bc10 | -9.19745 | -49.63385 | 2026-09-30 04:34:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7bc248f-6188-31fe-b0e4-692b20257f7b | -17.57698 | -43.7038 | 2026-09-30 04:34:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a66caa5f-30b2-3ba4-9359-c6247e6ecf90 | -11.85205 | -50.95718 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ade2950-351e-36cb-a012-cf98278ebdfd | -10.17016 | -43.29769 | 2026-09-30 04:34:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9c8af8ce-f01d-3091-855e-d7518dfb1c43 | -11.07034 | -48.88564 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 493ba461-270c-3efc-aea0-dfe11dae44d3 | -13.3834 | -44.01643 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d6d819a-a60c-336c-bcdd-ee4c4def0204 | -11.39361 | -43.46825 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| af18c952-fe4a-3695-99e5-5a4d0705a2b1 | -13.56324 | -53.20258 | 2026-09-30 04:34:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30dbc766-f7da-3d9f-91d5-82bfebc24dee | -11.16489 | -44.76546 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 259b26c3-c977-359f-a085-8d0a0f32c534 | -11.38682 | -50.97289 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8021bdfe-3efc-3b85-986e-349b34a8834c | -11.86056 | -50.98056 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9344338-483d-32e1-94bd-f5564a9ec031 | -9.78025 | -59.02325 | 2026-09-30 04:34:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 77b0be48-d5fd-345f-b8bf-c57f5991a0c4 | -11.389 | -43.37928 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47e3a748-4b8b-3b30-b959-6eff41e437b1 | -9.06906 | -49.86918 | 2026-09-30 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1bca49f-1af4-383a-88fd-1570cbcf7439 | -15.13063 | -43.62055 | 2026-09-30 04:34:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cb617c86-6214-309a-8b30-15df5ec33653 | -14.22245 | -44.53214 | 2026-09-30 04:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f257f229-d30e-36a0-9037-cca714770964 | -11.32135 | -47.75019 | 2026-09-30 04:34:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce607539-ae40-3d63-a838-745da8bd0609 | -13.37457 | -46.81306 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfa3d535-7334-3448-bbe7-c165e5d7a21f | -11.17665 | -44.77838 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd61b47c-8821-3a99-83b8-f9610eba9982 | -11.81946 | -50.42717 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64d68733-f98b-34d4-905c-55e3cd141c32 | -11.39074 | -43.39162 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ffdfffc4-397b-3a5f-9443-3d8fb7efbb49 | -14.91134 | -43.4143 | 2026-09-30 04:34:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0722c70d-482e-3355-a272-f70cd888f3d6 | -11.40433 | -50.96861 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23621ca3-f3c7-376b-b76d-c98ad21c0d9a | -14.28076 | -43.56188 | 2026-09-30 04:34:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1191f3c-ba6c-353e-813f-a39d882d75c2 | -11.3571 | -50.97492 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README34.md)
