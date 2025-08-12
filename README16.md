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
| 603ca8e3-0994-35f0-a449-73201060c126 | -11.47227 | -50.15646 | 2025-08-12 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ac81717-8f3c-3baa-8144-b30fbff49bb8 | -8.56432 | -54.71276 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| dc73f152-7cdf-3605-90af-943f97c7febf | -12.66725 | -46.98005 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94728534-718f-3c57-bef3-5531210484ba | -8.57089 | -54.71395 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3ee5e3e2-4194-3470-8d05-01160428d7e2 | -10.34986 | -50.83204 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94b28349-7609-3360-98d1-a40de941f80c | -11.45454 | -50.17381 | 2025-08-12 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50496995-7f92-3365-9a09-fda0b0530413 | -12.13792 | -44.92461 | 2025-08-12 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db9f138b-5413-3661-a2af-08108cc523e0 | -13.35342 | -50.25019 | 2025-08-12 04:08:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| d078b8f9-04a4-393e-94f9-8d04463f093e | -8.51853 | -43.32031 | 2025-08-12 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9de57ab8-4672-3035-b124-343d7444c498 | -12.1377 | -44.9243 | 2025-08-12 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 822f9b7b-7d33-3552-b1f6-51e97e8e06b4 | -12.56897 | -46.99046 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d9111c18-5ede-3ec1-892a-7d5dac29c8ac | -14.13818 | -44.90522 | 2025-08-12 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 475548d6-ff36-3587-9145-0b198409fd82 | -11.74722 | -44.97334 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08604333-4afb-3cc6-9ca1-607d12534ab2 | -13.02669 | -46.67132 | 2025-08-12 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f48c0ca1-96aa-38f3-a6b6-4baa547bd18c | -11.46853 | -50.15056 | 2025-08-12 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cba74fbf-0f1a-3252-8a3a-64770a7ff87a | -13.87447 | -45.56836 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abf5b313-31b3-3ad9-b47b-d49dd496b4dc | -11.4508 | -50.16791 | 2025-08-12 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c47ed7e8-823d-3199-9810-2af74d905216 | -12.56947 | -47.00975 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 69bac333-5306-3c6f-ba00-27338711b27e | -11.71552 | -50.11931 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8ef0878-0039-3837-852b-4d376cc8c3b2 | -6.30819 | -51.39923 | 2025-08-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 39275083-15ad-308d-a375-eea1739820a9 | -13.11645 | -44.52203 | 2025-08-12 04:08:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da65bb9c-4072-3e97-9472-9dca3158051e | -11.68238 | -51.60019 | 2025-08-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0b2065c0-abab-34f2-a30f-341de799c41a | -11.54487 | -47.31334 | 2025-08-12 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0952cb3-9b5c-34a7-8179-f6da523e3e1a | -11.70408 | -51.59763 | 2025-08-12 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daab8dad-61ec-324c-b1be-5228ee519da0 | -11.94302 | -43.41137 | 2025-08-12 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b97fda08-6d26-30c0-ae77-5ec8af25cdec | -6.30201 | -51.40181 | 2025-08-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f5a9a5da-07f5-3c07-b973-0bc3d1e82e9e | -12.57192 | -46.9957 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ac433fa0-aaae-3428-b64e-f8969d281a44 | -12.56274 | -47.00396 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fe50b61f-9bbd-3d09-a737-b51efdea1e77 | -13.58229 | -46.95235 | 2025-08-12 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 601d1da3-1f5e-3abb-be98-afc24e68ad26 | -12.99904 | -44.89348 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b60a8add-d78a-3e52-9f23-0a0f43b0b6dd | -9.06862 | -45.05318 | 2025-08-12 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad49f378-9aeb-371b-8460-78143e8b5032 | -11.7562 | -45.02625 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24a2025a-cffe-3261-b780-cc174c3b8dd7 | -12.54733 | -47.04686 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1826174e-1ccc-31f3-b97e-940adf07caef | -14.12098 | -45.3924 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 488dd02b-21bf-34b7-9e54-aa4b4ccfc4b9 | -13.60146 | -46.92939 | 2025-08-12 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 584ba5e0-2b68-395f-9a5a-79ebacf59ddf | -13.02377 | -46.66628 | 2025-08-12 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bc72610-4706-3e60-aae0-468699ddeb3c | -9.30088 | -40.21854 | 2025-08-12 04:08:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 0a8c1544-1693-3f92-9863-de5706fa8ff9 | -12.57454 | -47.02504 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 97a85826-e24d-3f70-a305-8edd24de0162 | -12.98267 | -44.88678 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56453e0c-5fa9-30e5-bb42-39899757fc89 | -7.21218 | -46.22875 | 2025-08-12 04:08:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfd84d32-d7f8-326e-8e10-0712e1225370 | -12.98607 | -44.88734 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e700a46-a2f2-37d5-91e3-f663d138fc2a | -14.03481 | -47.41286 | 2025-08-12 04:08:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4544aca1-127e-3ea7-8cd8-1ac8a805cec2 | -14.10603 | -45.39765 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 484bab4f-5b72-3a50-8216-acd603818127 | -12.98668 | -44.88361 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c453c24d-4cad-3b33-8b27-02fdb3ea5611 | -10.35206 | -50.8203 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3c6cc56d-b47b-38a5-a189-da97128962d1 | -8.20855 | -45.05681 | 2025-08-12 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8cac047f-6f3d-3412-af43-55489aa18a40 | -11.75903 | -45.03063 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17fbb8a0-4c4b-316d-bb47-31647e2224f2 | -12.5749 | -47.06756 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0069509c-0aed-3851-a060-e85e9aae494b | -10.33989 | -50.83021 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79806f33-21c7-332e-843f-9052e632118f | -12.78059 | -45.45384 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13d89a02-0a17-3777-95f8-9bff957a3c32 | -13.4487 | -41.32259 | 2025-08-12 04:08:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e8d3ce62-09dc-3ad1-8eec-325fcde3ce4d | -12.49824 | -46.33554 | 2025-08-12 04:08:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfaf3830-bcad-3a05-8cf1-144b49289e7c | -13.59777 | -46.92878 | 2025-08-12 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b6d28d8-73a9-328b-b574-c4154d1775ff | -13.62522 | -46.92362 | 2025-08-12 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45a1541f-7c2b-331b-afb8-c4528dae8194 | -9.70984 | -49.4754 | 2025-08-12 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a4a0fce9-d0a1-3dfd-959a-1469c3cf5683 | -10.36694 | -50.8234 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 148868b3-86e1-3b58-8f28-101917711689 | -9.71736 | -49.48672 | 2025-08-12 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7c101d2-2d1a-3dd4-9422-171af7a07772 | -13.87824 | -45.58009 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ae7f457-6471-3149-b353-8cb49927026b | -13.02743 | -46.66691 | 2025-08-12 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00d7b3f5-a130-39e2-8771-432e8913dcc7 | -11.79948 | -44.93481 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1f96a25-54ce-3644-b18b-db368bbc60fa | -10.23979 | -48.25101 | 2025-08-12 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6fe1e7bd-8a55-3c32-8f05-a3f0398cf834 | -10.34707 | -50.81945 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7e450b8e-b297-333f-a0eb-90ee98fd602a | -8.52361 | -43.31014 | 2025-08-12 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4b9ccb19-ef2b-3af0-92dc-d780b5674680 | -10.62888 | -44.7556 | 2025-08-12 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbc4569f-af61-37a9-9635-ae13f7d20343 | -11.54187 | -47.30767 | 2025-08-12 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05052ec3-af30-37e0-82cc-ff1c46504704 | -14.12035 | -45.39622 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 917ea69e-01c4-387c-b5b9-042884187f42 | -7.55215 | -47.04471 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 370100c9-dc1c-35c6-96c8-2bf9fe969816 | -7.21285 | -46.24875 | 2025-08-12 04:08:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a36fad2f-7342-35d2-9d6a-fea018f9d779 | -13.57872 | -42.53275 | 2025-08-12 04:08:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b0d7ea46-9625-3a01-a348-9bb6e6a9c40e | -11.76859 | -49.10804 | 2025-08-12 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 621c0723-9ec5-3366-b591-92c3a9a36b18 | -12.49751 | -46.33981 | 2025-08-12 04:08:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39331cb7-ced0-346d-a0bb-9289874c861f | -13.33982 | -50.2474 | 2025-08-12 04:08:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 66f73a59-53d4-3e56-a5b5-a3cea8be2c46 | -9.06697 | -45.06606 | 2025-08-12 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eea48185-b110-3412-b211-7a8eaddd9f11 | -10.35373 | -50.83888 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98296c16-b73b-3472-a2f0-4508a5e67c5a | -12.45044 | -48.72773 | 2025-08-12 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07873b4d-d03c-3b93-b117-d4333830d63b | -10.35981 | -50.83397 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ee450d2-739f-309b-9526-60aa42d79d08 | -8.55968 | -54.71108 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 845ce3ca-005b-326a-a640-48016b77b50b | -10.64422 | -45.23894 | 2025-08-12 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ad89358-fe45-3047-bb7d-26af767afd68 | -11.44986 | -50.17292 | 2025-08-12 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af058bed-f60a-350b-a1cd-20281d1978b5 | -12.49533 | -46.3307 | 2025-08-12 04:08:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 836ffdce-1460-35a1-8095-382f2178ca70 | -13.96426 | -42.58397 | 2025-08-12 04:08:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 13b4b1a1-51ed-37a7-a675-a7c71a3b72d7 | -11.75993 | -49.10642 | 2025-08-12 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff74b9bf-c01b-3065-9c88-f4807dc6ab41 | -10.3609 | -50.82812 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7de12d6-e37e-3b20-995f-09014d13c117 | -11.80354 | -44.93158 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2712a266-0fad-3897-95ef-dee269c2f5d9 | -12.56571 | -47.00914 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 88a2cb15-b98b-32d1-abd6-33e7e98a796a | -7.21379 | -46.21903 | 2025-08-12 04:08:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e6ded9b-8d3d-318b-be37-d9e0bb35beda | -11.45864 | -47.32117 | 2025-08-12 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 269e1ba5-eef7-3d63-a6da-febf6142deb3 | -9.76897 | -48.74947 | 2025-08-12 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e26a4bdd-7a92-36a4-9dfe-b40159a7bfc4 | -10.97105 | -49.56829 | 2025-08-12 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e4820be0-04be-3d31-bfa2-ae62eacc708a | -14.11756 | -45.3918 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97c2780f-331e-3d87-9771-6e330ee92c75 | -14.11414 | -45.3912 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60627782-caa2-3099-a132-04a741771d60 | -12.56522 | -46.98978 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 6a9c8d21-48d6-370d-8bee-fbb05f31130d | -9.71147 | -49.48777 | 2025-08-12 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6504cd3b-e05b-3f19-9ebd-e84b57628c24 | -11.80635 | -44.93598 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d57c5c29-6ca4-325b-b435-7c9917921391 | -10.23918 | -48.25448 | 2025-08-12 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b201cd3f-1c38-33a0-a5d2-31727dfd49a0 | -12.57696 | -47.07808 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1229c0c0-e1f3-30ba-b0f5-febfd400864f | -12.55897 | -47.00342 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cb623c3d-8ca6-34ed-9b2a-042f2aaf8aee | -10.06358 | -46.39697 | 2025-08-12 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23408cf9-be91-34cb-819d-82938ce2c477 | -11.80918 | -44.93575 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d28a1df8-2e9f-3c32-b8bc-ba02c3ed3779 | -8.98489 | -46.59931 | 2025-08-12 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README17.md)
