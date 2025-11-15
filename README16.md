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
| f0a39daf-6101-3e4d-ab12-36a21f116abe | -14.94631 | -47.50846 | 2025-11-15 03:38:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b4359002-880d-3e32-9948-6243f7a203a0 | -11.92029 | -46.20375 | 2025-11-15 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20eb7f04-8741-3381-a73f-53aaf25ef1bf | -16.45191 | -45.00988 | 2025-11-15 03:38:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a16c18ff-a48b-3b83-a80b-f0fb7804ad97 | -12.79231 | -46.38538 | 2025-11-15 03:38:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc2a9132-d8c1-31c3-bd30-46bc495052c9 | -11.3213 | -48.52742 | 2025-11-15 03:38:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d5c7ab80-eda8-35c2-b111-2727c0ff43b1 | -14.05187 | -44.47919 | 2025-11-15 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cae908d7-823d-3d41-af42-b40185d605e6 | -12.48061 | -43.73643 | 2025-11-15 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1cf3acfb-cac1-33a1-ba69-4ee3b81db241 | -12.00912 | -46.76808 | 2025-11-15 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a658493e-a31c-3e14-a6b9-4ee801dc08c7 | -15.9983 | -41.43542 | 2025-11-15 03:38:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a266176e-ced7-31b1-bc64-f804b5a36ab9 | -17.1591 | -43.07479 | 2025-11-15 03:38:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d32444d0-e839-3c4e-a752-fedc83d3516c | -14.65282 | -46.57024 | 2025-11-15 03:38:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 26e32faf-2b29-3e8f-b592-793ffc51f809 | -13.73928 | -43.6265 | 2025-11-15 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07d8d5ee-b32d-3c91-b2eb-98f03d23e887 | -17.58507 | -46.68465 | 2025-11-15 03:38:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 04eb87bc-fb71-334e-8bcc-4a1d746fe493 | -12.79831 | -46.38678 | 2025-11-15 03:38:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c7cb7aa-2f0b-3d85-a3ba-22d8a19aa9b9 | -12.83853 | -46.44221 | 2025-11-15 03:38:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b9eb41f-daf3-3b73-a965-a3208574808e | -16.56243 | -47.60784 | 2025-11-15 03:38:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7fd13e5-52ef-3b53-92be-fb7f6e639ef1 | -13.89779 | -42.89734 | 2025-11-15 03:38:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 53e1ed2e-d9f1-3002-a467-2d03ad50e39a | -12.84047 | -46.43269 | 2025-11-15 03:38:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 11c43a50-4a62-35f1-8a16-12b108678aeb | -12.39825 | -48.11011 | 2025-11-15 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ba29b493-943c-3b78-885c-1d95e21bda74 | -11.6801 | -44.73895 | 2025-11-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc380583-67de-38cf-965d-cb96b7d0d05c | -13.52642 | -43.41583 | 2025-11-15 03:38:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 219cb103-8ae1-342f-9332-c647a77db06e | -12.72529 | -44.55243 | 2025-11-15 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f61922c2-fc34-37df-bd00-5db500057c03 | -12.68178 | -46.77414 | 2025-11-15 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 8036cb5f-9a04-3fa0-979b-8ae37fd3eac1 | -12.25478 | -44.91753 | 2025-11-15 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27e06c2b-39cc-316d-9874-a1760a7bffb8 | -14.69194 | -46.6063 | 2025-11-15 03:38:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c692daae-9153-3cde-ba75-cc18a1877966 | -17.24943 | -42.66602 | 2025-11-15 03:38:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b59ef3ae-0f5e-3d7b-a869-1745381205ad | -16.66804 | -43.52832 | 2025-11-15 03:38:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35e0dc19-3f3f-3e42-a14d-b7d673b19d9a | -11.75609 | -45.33778 | 2025-11-15 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d98d4958-33db-34f1-bd82-ce960388050d | -11.74514 | -45.33263 | 2025-11-15 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 232852ef-2090-39dd-b180-0313b5e42990 | -11.80936 | -48.07488 | 2025-11-15 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90ef9711-2ffe-367a-8b1d-35648694e99d | -15.46207 | -39.2405 | 2025-11-15 03:38:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 61f6086a-3ead-3d3d-b3bb-59e6cc57ddc7 | -13.54483 | -43.72496 | 2025-11-15 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed1b1774-29b3-3af6-b556-00d27fea6c07 | -11.17246 | -48.14423 | 2025-11-15 03:38:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c2b74270-d7d0-3b24-8d7a-257700d186cb | -17.29464 | -46.83082 | 2025-11-15 03:38:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3472af12-1273-3a7c-ab21-f4b6b51ff46b | -12.4456 | -47.88425 | 2025-11-15 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| acfecd60-4e21-3d81-88d4-7d883b93cf4e | -12.60145 | -48.3354 | 2025-11-15 03:38:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dcb81cbd-66ec-325f-a53d-f1e0201b9625 | -16.56259 | -47.61014 | 2025-11-15 03:38:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ace65ed-1f5c-3e0a-910a-2eaee58c2c95 | -11.9548 | -44.84919 | 2025-11-15 03:38:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18d87cb2-71eb-371d-8eba-93888f680b30 | -12.0396 | -43.74306 | 2025-11-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9bd6d44-3cc2-300f-ad94-df09a49c754c | -12.36343 | -43.6987 | 2025-11-15 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2343e199-466d-39f9-aae6-cdbebc2dce9c | -12.75701 | -43.64954 | 2025-11-15 03:38:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5c6edec-1b1d-3425-b3b7-5df100eb4bf6 | -15.52294 | -43.88525 | 2025-11-15 03:38:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f532b63b-630e-3156-aa42-eface172bc04 | -14.68715 | -46.61275 | 2025-11-15 03:38:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d0933dd-5904-3439-a33b-d207620a708e | -17.01788 | -39.59204 | 2025-11-15 03:38:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 58120879-08f4-3ce6-876f-637478edf916 | -12.40486 | -48.11202 | 2025-11-15 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b88e262c-8fd5-3801-a90c-ae72eb5f73ee | -15.37151 | -45.63715 | 2025-11-15 03:38:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28002028-33f9-31d9-9ea0-7a18a5ac027f | -12.46157 | -43.75213 | 2025-11-15 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4a6678d0-ca00-31a8-807d-1dbe0cd6773d | -13.89305 | -42.89641 | 2025-11-15 03:38:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5f18d258-4fac-378e-8b1f-abc71fde404f | -12.42693 | -43.17983 | 2025-11-15 03:38:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dba7df09-d2a5-33f7-b154-cad15d4c4c92 | -15.45767 | -39.23792 | 2025-11-15 03:38:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 0171746f-634c-3200-979b-22cde6e40acc | -12.67142 | -46.76181 | 2025-11-15 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a9ef220d-0ef2-361b-8636-ae2480f923aa | -11.70717 | -48.3967 | 2025-11-15 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b5450044-15b3-39ff-8615-426522814971 | -12.76209 | -43.65054 | 2025-11-15 03:38:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6eb14fab-e8db-3e5f-9367-4fc0bb59e52b | -19.00834 | -41.06884 | 2025-11-15 03:38:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 890e1c90-162b-3e99-9275-6f0bee3c662a | -14.63778 | -43.82742 | 2025-11-15 03:38:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 057abfea-9a74-3565-9d23-d43862387c3f | -18.59902 | -43.98903 | 2025-11-15 03:38:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bc19cee-4a15-352d-ae2d-48a5341cad81 | -18.59793 | -43.99456 | 2025-11-15 03:38:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7814f458-b2d4-34a7-8126-29d65c377b8a | -13.6049 | -41.076 | 2025-11-15 03:38:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 592d1ddb-7e27-3cf4-bde3-1d1747c54dfe | -14.68993 | -46.61573 | 2025-11-15 03:38:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd362598-39e1-3c06-beb3-88540020e676 | -12.92974 | -41.10266 | 2025-11-15 03:38:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b8bde9e7-78d5-3001-abdb-11378689a304 | -15.46284 | -39.236 | 2025-11-15 03:38:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6ae7d1fe-ca5a-3d10-8d9b-d8b181b00bc8 | -11.17218 | -48.14513 | 2025-11-15 03:38:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 73506220-daa8-346d-a1c8-446a92aaf7af | -11.95407 | -44.85292 | 2025-11-15 03:38:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c94389a3-de7a-32c2-9733-73cb26584565 | -15.46135 | -39.23857 | 2025-11-15 03:38:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 2c3d8e8e-1966-31bf-ba3f-a84786ba5aed | -11.71531 | -48.87011 | 2025-11-15 03:38:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f0fdd06-44f0-3def-a2eb-363d746c5d81 | -14.7927 | -41.66385 | 2025-11-15 03:38:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 75f95ad4-81b4-3d95-80e5-1e6e050ec3c8 | -12.46005 | -43.75058 | 2025-11-15 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da65e10d-f39f-37f7-81fb-eaeebb540704 | -17.26872 | -42.6605 | 2025-11-15 03:38:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1a610043-5fa8-38c1-a73a-169e9de65a45 | -11.92132 | -46.19864 | 2025-11-15 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06fc5823-4e2e-31ef-95b1-de315d05f05e | -12.67761 | -46.76304 | 2025-11-15 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 595f4f7c-02f2-3bca-964f-f4d8298e2450 | -12.67242 | -46.75694 | 2025-11-15 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f850ebfa-2f7d-3466-93dc-25948550d680 | -11.80257 | -48.07358 | 2025-11-15 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b44a4a3-bf23-3df0-81a9-ffa35ed1c71b | -14.65802 | -46.57487 | 2025-11-15 03:38:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0b77d11f-8c27-3f8f-9d95-a630d2796b9d | -16.45269 | -45.01075 | 2025-11-15 03:38:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b2dabbe-bda0-3ef3-8519-9bb77d5627f3 | -15.45839 | -39.23984 | 2025-11-15 03:38:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| dd73ee05-91af-3946-a30e-6793f35c3357 | -12.47548 | -43.73544 | 2025-11-15 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9be54fdc-0f78-3138-a162-ae19f5954d7f | -12.65167 | -43.25348 | 2025-11-15 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6e511a9b-bf5a-3295-8d54-0de08d725e8a | -16.56367 | -47.60526 | 2025-11-15 03:38:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08331f74-61b8-3d0c-8ff6-f1ea460f8d0f | -12.4168 | -48.12192 | 2025-11-15 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4fcb8d97-a078-35cc-a497-5377c357869b | -14.66325 | -46.57933 | 2025-11-15 03:38:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 94622c66-44f7-3758-94b0-fdedb7d33d7e | -13.60502 | -41.07668 | 2025-11-15 03:38:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 167bfe80-3994-38c0-8b4b-335bebc44836 | -12.36857 | -43.69963 | 2025-11-15 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2853762b-bee9-3ee4-acc1-c5cf2ad03d07 | -15.45916 | -39.23534 | 2025-11-15 03:38:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| b95e1c66-3092-3bcc-be31-bdf288811445 | -11.80127 | -48.07991 | 2025-11-15 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e0d68f0-abd8-37ce-92c6-d1fdd3797c6c | -12.14932 | -46.67364 | 2025-11-15 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37f67d78-0a40-30a4-8e40-c33e94003613 | -12.15551 | -46.67495 | 2025-11-15 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| adf2d7a7-0111-35df-be15-75b3e6a98b98 | -14.65699 | -46.5798 | 2025-11-15 03:38:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0fe6ed5c-7553-39ce-9d0e-e26083026d3e | -14.95244 | -47.51016 | 2025-11-15 03:38:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d4fae803-9823-3ba7-b509-0cec4c5b15b5 | -16.30576 | -43.8082 | 2025-11-15 03:38:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be40207f-d55b-39b8-998d-706bea565e27 | -11.70852 | -48.39018 | 2025-11-15 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 677a7d3d-ebd2-3a34-8fbb-3996c38f54c9 | -13.80749 | -43.19079 | 2025-11-15 03:38:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ee3536dc-2bab-3ba9-9118-a2f3ec14fad4 | -13.35307 | -43.74857 | 2025-11-15 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36d93cf4-15fb-349e-85bf-a6602143f514 | -12.02593 | -43.73051 | 2025-11-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0fb0ed6-e616-3b05-88ca-1695f6ff8c07 | -14.57383 | -41.14468 | 2025-11-15 03:38:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b87b8848-89d2-356e-b47d-e630ee417002 | -14.71827 | -44.2383 | 2025-11-15 03:38:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77aa1175-3696-3a3f-bb4f-e357abb3d674 | -14.69096 | -46.61092 | 2025-11-15 03:38:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e356d4b-71e1-3471-926e-320916552d3a | -11.91928 | -46.20881 | 2025-11-15 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de9a48cd-300e-3212-8589-4ad71601b379 | -14.68889 | -46.62057 | 2025-11-15 03:38:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2555221-4857-3e35-8436-3ca301842ea6 | -11.67937 | -44.74272 | 2025-11-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b30450f-bb9d-35ef-98e7-da6c9343aaa9 | -15.78628 | -41.47285 | 2025-11-15 03:38:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README17.md)
