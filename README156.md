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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be45e3f2-febd-3ad5-94b4-d2b62100477c | -11.86363 | -46.84254 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1c185b7a-4c9a-3b89-a5c7-6608c97672f9 | -11.53523 | -45.36886 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4b1d98cb-fe67-3d91-acc3-b8cf71c39d2b | -9.38671 | -48.31995 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b0f99142-7bca-3a6b-9ad2-c10992f0577f | -9.54664 | -46.51817 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| faf7c014-86b6-3bdb-bacf-346b1b0fe864 | -8.7556 | -44.28728 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 533b0d99-dfa7-370e-8481-2aa606518caf | -8.77111 | -44.29986 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 52.2 |
| d56db2a9-b084-3872-a407-8eb06df3a42f | -12.38066 | -48.12526 | 2026-09-21 16:01:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 233ba6e2-d2dc-3d32-8229-d8705d5685cc | -11.84392 | -46.82136 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| d52a81e9-16e5-3810-8652-547c33e3e19a | -10.86318 | -50.15593 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| f21415c8-9dbe-3e36-9351-7cb45becf5ee | -8.78547 | -44.26934 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 96e9922a-4479-3746-a295-fa46c532c22c | -10.09481 | -45.83182 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 45bf531f-6bfc-3446-acb5-11003379b59f | -11.43546 | -45.38512 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 6d977c27-bb9b-3db0-b2c7-2b0c2fbf5dab | -12.39885 | -47.00751 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0b93c187-6e1a-3c07-b9b9-13829631bce5 | -10.54993 | -43.91674 | 2026-09-21 16:01:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 44142be3-b134-36fe-bfe3-e24dc0f25453 | -10.27532 | -49.98759 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 08690598-355f-3c18-8ea6-4618c09b9895 | -11.04072 | -48.34772 | 2026-09-21 16:01:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 217ab8b5-22c2-313a-89d3-7dea4474e383 | -9.40289 | -48.32877 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1e513b82-fce0-3ae7-9509-67bfbb9d5e57 | -11.44486 | -45.3779 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 160eebde-0bd0-3058-99f7-dd22559d449b | -11.46982 | -47.64025 | 2026-09-21 16:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| baacdbc0-6c1e-30a9-a7d7-51773bbd962d | -12.80168 | -44.2039 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 05552341-5d5e-3f62-8fbd-fd566b7b2ae5 | -9.37559 | -47.77192 | 2026-09-21 16:01:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| d56b95ee-5bf5-3605-9391-ac5d12447980 | -8.76569 | -45.85187 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f9335569-a61a-3e3a-ba4b-f627646bc66a | -11.81674 | -50.02118 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 4667c0e4-3fef-30a5-a520-7005f1fc2b83 | -11.93345 | -46.49535 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3f4e2b37-37c8-36ae-bec8-f661f364c10a | -11.43689 | -47.31249 | 2026-09-21 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9c53e881-1f46-3019-b980-1a96956aa319 | -12.48285 | -44.71852 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| cb2c4110-2cba-3928-9a36-cff5dc283266 | -8.7539 | -44.28613 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 80fd428a-48a2-3c24-86cb-9a43e413cc89 | -9.9746 | -50.25542 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 4e4be344-08bf-3526-b0af-59c83f486860 | -13.03384 | -46.97935 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3a471fa5-9b5a-3d55-8755-258e5a43b92f | -11.9514 | -46.50941 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| cb8fe4bb-8565-3b8f-9bbd-dbd30d78ac7e | -9.91151 | -45.8297 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d5e91b3a-e71d-3409-9265-3da9774af940 | -10.81461 | -50.15462 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 00c76010-d6d5-346e-b63f-f7d28b667eca | -8.32321 | -44.76195 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8bc09d00-4b2a-334b-a4b1-f352fb783dfb | -11.67592 | -43.43867 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 852b3973-96cd-30cc-b73a-b81412e7e619 | -8.78403 | -44.29301 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 1e73708e-0406-3c86-abf6-2c193b50d062 | -11.85287 | -46.84797 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| daf589ba-67af-3539-a964-9f53b627a4a5 | -12.29436 | -50.15439 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| dd73dc40-e783-3430-964d-f5ab313f5718 | -9.8233 | -48.31123 | 2026-09-21 16:01:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 50a79350-7775-3665-992d-0a353cf62354 | -10.14614 | -45.55762 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| db8b6c6f-e437-3d3f-aa12-cba2f2d00814 | -10.73221 | -50.77943 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 4c484009-a46f-3b37-92cb-8fdf79599003 | -11.86115 | -49.97457 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 9572935c-b860-3881-8a04-add4ee7779d2 | -11.09967 | -48.31601 | 2026-09-21 16:01:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 282e57a4-5629-36b4-af86-318961d4a8de | -9.54348 | -45.39345 | 2026-09-21 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f457c27d-979b-3d50-87b0-417c7f8f9bd6 | -11.09981 | -48.32228 | 2026-09-21 16:01:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 676f90ec-c7e6-32b5-9cef-003bc1bfcbef | -11.87119 | -46.85751 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e6617d8b-543c-30ab-9225-74d65c066a1f | -9.23401 | -46.17813 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8bfe15a4-44d7-3a19-b6b6-87d9306c5c53 | -11.42963 | -45.3798 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| f8cc96b2-deea-3c4c-b9a0-ee05217a4a2c | -8.65505 | -47.36337 | 2026-09-21 16:01:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7f63316f-b06c-3599-a089-ec07955c2103 | -11.93436 | -46.50732 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cda74b17-41bc-30ac-b0d4-3c05cbe3ccb7 | -14.334 | -44.79902 | 2026-09-21 16:01:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dfca14e8-8a94-3cf0-bc34-e27ca23cf229 | -10.71885 | -50.78772 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| fa2fefe2-5135-353d-a079-3f5af5197233 | -8.76077 | -44.29146 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 50fef24c-2b67-3c29-add0-89b4bd849c24 | -10.09008 | -45.83559 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6a8f0015-bc5d-3ad7-a833-5336f3418c5a | -8.76094 | -45.86024 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0b0c3288-fce3-37d8-9bd9-7e8196da2bb8 | -14.45407 | -44.86839 | 2026-09-21 16:01:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a8c095b9-303c-3966-842b-05d6823998fa | -10.73248 | -48.80547 | 2026-09-21 16:01:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2cbce18c-eb3e-3582-857a-d62f99721f48 | -9.00617 | -44.34447 | 2026-09-21 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| e02db88d-f04c-34d4-b8e5-e8f8add6e426 | -9.02841 | -49.82672 | 2026-09-21 16:01:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 50f78ed8-ae90-32f4-b5c6-c323621474c7 | -11.43584 | -45.38809 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| c8caa483-7f25-3ffb-ab99-0b68c27d3b36 | -11.44111 | -45.34845 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4b78a8e7-8876-3832-ab0c-dc18a8d2ede1 | -12.43245 | -47.03087 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4e76e021-2ea0-34c1-9d4c-ceb084fc54b7 | -11.43738 | -47.31656 | 2026-09-21 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d265e889-d8f7-3fa3-87e4-d25578f94e8a | -10.484 | -46.27856 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6669e1ea-3fc9-3d73-abf0-d8bb68792720 | -12.39602 | -47.03251 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 9db2b25b-7139-3cd2-8550-5c936d465745 | -9.38326 | -48.31753 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 105d1d92-5a0c-3455-815b-daed06021111 | -10.71726 | -50.77394 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 12a8c022-ca70-3861-a516-85449b8c97b6 | -10.6749 | -50.71587 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 591139fa-f44f-3a31-9be6-1653565b08fb | -10.09071 | -50.28704 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1416221b-d0b8-3a8d-a5fb-3a2ae288bd5b | -11.14098 | -42.80202 | 2026-09-21 16:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| f52fb94f-6a95-3a53-8ca6-1c4c646335bb | -10.72426 | -50.71095 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c42cbee9-8523-3ba0-bc6c-e0efac47292d | -10.61839 | -50.59211 | 2026-09-21 16:01:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| e1583a0d-bdc6-3364-a319-a0969d807b3a | -11.80124 | -49.80463 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| a5d6f1c9-98dd-3431-902a-b58eca7804cb | -11.95698 | -46.50927 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3dc7a6bb-c805-3548-bdd8-a8aea51e5bba | -12.42996 | -47.02447 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0884bcd0-059f-3fbf-af54-61b53ba1ccdd | -10.12476 | -45.55061 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bee387a8-2f1b-353d-a220-4046eea65d6a | -9.40888 | -48.32788 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6306df48-3091-3236-a305-2b63661d5ffe | -9.17474 | -36.04693 | 2026-09-21 16:01:00 | NOAA-21 | UNIÃO DOS PALMARES | ALAGOAS | Brasil | 2709301 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 4154f478-203b-3e0a-a56a-2fca3a0b4190 | -12.4486 | -47.07022 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| bb043252-6a48-389f-9616-3d686601a804 | -10.11012 | -45.55642 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 85bf4bac-5a47-3d47-b687-ecf42c5710eb | -14.1177 | -45.60147 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0ea9a849-2488-336e-a295-1c428ea449c7 | -10.2679 | -49.98233 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 73c566b8-10f5-3442-916a-d15f888b0006 | -11.81276 | -50.04718 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b9f00cdd-fe1d-363d-9d45-1492ccc97cb4 | -8.76184 | -45.86124 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7f750b17-c6e9-3be4-a4f4-f560f1347d80 | -11.96289 | -46.50797 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fac7e9a4-2bd7-33ad-852c-3b205d005bfe | -10.08312 | -50.28152 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 04387ee2-7a06-3414-b77e-cc05148824f3 | -8.73142 | -44.88425 | 2026-09-21 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3ca71842-3814-3743-91ed-c9967c33aa24 | -9.60976 | -43.92463 | 2026-09-21 16:01:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 38.8 |
| b37165ea-639d-3e10-937e-3c0f46977c89 | -8.75714 | -44.27635 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| a4755cd1-9472-3a07-a672-d6e67aa822fe | -11.6466 | -41.69537 | 2026-09-21 16:01:00 | NOAA-21 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 66123bd9-4564-33c2-aa3d-9465845f1802 | -9.88517 | -42.09915 | 2026-09-21 16:01:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 49b1438d-b6a4-3fd4-8f52-88f30d716b9c | -11.4537 | -47.65578 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e03a420e-3f55-385f-a463-f1c02ed123b1 | -11.42889 | -45.37387 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ae3562d4-6bd6-35d6-b587-46acab52e47c | -9.24034 | -46.17547 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ec3f8ced-6fe6-33a0-8ac6-3febb8e0e091 | -11.66803 | -43.41248 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| af62b9a9-62b9-3a9a-ac39-b4ee7342e159 | -11.47263 | -47.74974 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 41d3cc8d-face-39f2-a44b-4ff3602dcde4 | -10.09148 | -50.29328 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 65c2afc0-2ee9-353d-9e67-99a415cea5b2 | -11.45246 | -43.3051 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 88410a1d-51b2-3166-a387-5438449b5fba | -12.40269 | -47.03968 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8f7ce67a-e524-337c-a212-e2f1ce0ca70a | -11.14412 | -42.79348 | 2026-09-21 16:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 4c199c9b-269f-3e35-b300-bce52f607f8d | -11.33998 | -43.37088 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |


[Clique aqui para ver as próximas entradas](README157.md)
