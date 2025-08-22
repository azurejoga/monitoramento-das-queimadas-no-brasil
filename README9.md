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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38b247f4-6b06-3949-b0dc-a289349a5f18 | -14.7612 | -45.42376 | 2025-08-22 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 01b3f955-6552-3a62-8fa1-f8cb1017c355 | -13.0241 | -46.33817 | 2025-08-22 03:32:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5d30e6b0-fad9-3853-82f5-531169fe31c0 | -12.9972 | -45.21425 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 544c985d-c110-3891-ad23-7eb525eb2a39 | -12.99732 | -45.24111 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b4bf3e28-c56b-33f1-acfe-2f2af2ddaa7c | -16.52202 | -43.45309 | 2025-08-22 03:32:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 329bf03f-0d36-3719-af48-7aceccecdb66 | -13.38004 | -47.49859 | 2025-08-22 03:32:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bf25a45d-4e19-3b56-bc88-d44347ea2637 | -14.89039 | -47.95014 | 2025-08-22 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3825af45-7638-38c3-aa24-3593a656cd81 | -14.82838 | -47.93807 | 2025-08-22 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 171c9ebe-c899-3043-b283-82f2cf8b65b4 | -13.35876 | -46.25555 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe65cb27-0453-33f5-87fe-f24bd4065ef0 | -11.12001 | -44.71917 | 2025-08-22 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ec98078-d5c5-308f-8dae-aec56f8e22ac | -9.58759 | -43.32856 | 2025-08-22 03:32:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 465ef988-9993-3a24-9d93-4035e221b647 | -13.03105 | -45.17255 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa2401bc-a774-3765-a57e-d5f3c5538426 | -12.00531 | -44.67216 | 2025-08-22 03:32:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a9e01da9-c483-35c9-9e5b-02edbf6a1ae5 | -16.52238 | -42.51612 | 2025-08-22 03:32:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37c910c7-0f82-322e-a11d-de7018a2eb25 | -11.99844 | -44.67555 | 2025-08-22 03:32:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5986563e-47c2-394d-985d-881d4d8c03bf | -14.8691 | -47.94929 | 2025-08-22 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 27d20163-1f15-3bd7-8002-6c8c6662d196 | -14.88339 | -47.94932 | 2025-08-22 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 765655b1-be5c-32d0-be82-7add53e7491d | -16.60949 | -43.35963 | 2025-08-22 03:32:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7338267-46b5-317a-b60a-1561259d63e0 | -13.02352 | -45.17306 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| adb438d9-62e5-3c01-947e-d241188762d1 | -9.58832 | -43.32463 | 2025-08-22 03:32:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 08ba1b09-7379-3204-ba0e-a05fd7401be3 | -11.28402 | -44.94999 | 2025-08-22 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbc40c58-0510-34b1-ae0d-68a35e723547 | -12.94839 | -46.28162 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 000d02f0-2f40-3913-9785-3a0cfefc2f2b | -12.996 | -45.21619 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dff7a27a-9981-3ddf-8172-941bbfe56edb | -12.92849 | -46.18048 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ec25eb09-749a-3dc8-91c2-027ed95cef88 | -13.36392 | -46.2628 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2ad11e9-55d4-3eac-8977-990dee6069aa | -12.98721 | -45.23189 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6ef09500-fc37-33e9-9a3b-d955fb8b793d | -12.95347 | -46.28954 | 2025-08-22 03:32:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0b3eafaa-ca63-3384-9602-ee58bbb59fec | -13.02536 | -46.33218 | 2025-08-22 03:32:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| efa01dc7-8478-3eb0-b137-add4beaa479f | -14.97821 | -47.13765 | 2025-08-22 03:32:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2a4bd058-6a05-3be8-9a8f-14d30da8d9d4 | -12.00621 | -44.66764 | 2025-08-22 03:32:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e07ce525-3121-3fe8-9f48-2a79dff372a4 | -12.9923 | -45.23784 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a27755a6-ff41-3ba7-9505-6aa11610cfc8 | -12.9922 | -45.23512 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e0f8e708-307b-37bd-8b16-3cc59d78d83e | -13.03322 | -45.19257 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d0592080-9e0f-3abd-8efd-7292f74f182c | -13.02405 | -45.17593 | 2025-08-22 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0dfd0cff-9c63-3139-b50c-3b5107dd2f35 | -13.49621 | -47.04961 | 2025-08-22 03:32:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e902af9-fc9c-3100-b37f-8ae7683f4fd1 | -13.71475 | -42.6907 | 2025-08-22 03:32:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0052fc71-3118-3b9e-a3f1-6f215433607e | -10.9853 | -45.60283 | 2025-08-22 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b878759f-42a0-3027-befb-cec4e779ed35 | -14.87804 | -47.9416 | 2025-08-22 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5fc0bd8f-ec6a-33de-b404-2522fed758fb | -22.78437 | -47.09094 | 2025-08-22 03:34:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50a69479-92ab-3c52-8a11-46fbaa545be6 | -18.79203 | -41.45754 | 2025-08-22 03:34:00 | NOAA-21 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 54f416ae-260e-3eec-9085-606b1bb9d9ae | -21.43044 | -45.97211 | 2025-08-22 03:34:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d71e0be0-4b01-375d-a643-f614bdc6df8b | -22.23552 | -48.39933 | 2025-08-22 03:34:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 417d0c87-0e9f-3e98-8aa6-bdd4aa348790 | -20.67413 | -41.42054 | 2025-08-22 03:34:00 | NOAA-21 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 0d0d07f3-6879-3c59-8e33-a50372aa70d2 | -20.67818 | -41.42185 | 2025-08-22 03:34:00 | NOAA-21 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ff28072e-5ef2-3b48-945b-fc57440554d1 | -17.39981 | -44.24479 | 2025-08-22 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c923bdc-74d4-3d25-8b36-38845e2ca9e4 | -21.0373 | -44.76134 | 2025-08-22 03:34:00 | NOAA-21 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 494d9409-7906-34d2-b655-4e28c9a46611 | -20.08086 | -46.12579 | 2025-08-22 03:34:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6dec17b-3a55-3ac5-bcab-f43d7154860e | -21.89911 | -48.16592 | 2025-08-22 03:34:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed8a9785-1493-3647-bdbd-749cec595c30 | -22.69489 | -43.74393 | 2025-08-22 03:34:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 9a948613-bc36-35e4-84e5-8ef218e58f7a | -19.71207 | -48.98267 | 2025-08-22 03:34:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7af4c42a-a1df-3e4d-8db6-2343fe111ee0 | -19.93723 | -44.57196 | 2025-08-22 03:34:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 6c5eed52-f7a9-3e39-a939-0c2f7e0e8ecf | -21.89794 | -48.17091 | 2025-08-22 03:34:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ebf6159-f4b7-3194-a048-67092de1d5ca | -18.28605 | -45.53615 | 2025-08-22 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9afd4e61-8205-39f7-a140-6ab8b3c1a584 | -18.28392 | -45.51882 | 2025-08-22 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d4f635a0-991b-31f1-a27c-a26cd1659c72 | -20.30528 | -46.6222 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 682e07dd-9540-3f09-bd6e-a1e2b0e85e87 | -22.55563 | -49.77412 | 2025-08-22 03:34:00 | NOAA-21 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c43bcb98-976e-328e-a57e-3a2678a67df1 | -18.61724 | -44.26269 | 2025-08-22 03:34:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8c40abff-ad38-34b1-9f51-bbde9be5da9c | -20.35911 | -46.51792 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 820978f5-e8fa-3cee-943f-46c86c0a5294 | -18.2877 | -45.5285 | 2025-08-22 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5fc8dd4f-3b35-318a-a8f5-4943324c7d7c | -20.14855 | -42.13654 | 2025-08-22 03:34:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 10a249ba-bbd4-3e73-8c28-ebf6e11894eb | -20.08001 | -46.12974 | 2025-08-22 03:34:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1c93911-6ae3-384d-ba32-8dd75bc594fa | -16.78815 | -47.66659 | 2025-08-22 03:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e3a7a05b-d968-3b44-8470-8aac63816556 | -18.88344 | -45.02052 | 2025-08-22 03:34:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 30.5 |
| d1d0677d-320f-3eff-856f-25111c98e4a7 | -20.26532 | -46.69137 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 973f3d9e-3f39-36d3-a92c-d74b016555fe | -23.97472 | -46.47129 | 2025-08-22 03:34:00 | NOAA-21 | SÃO VICENTE | SÃO PAULO | Brasil | 3551009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| abde6e10-1819-31ae-b926-242789d4e141 | -22.19 | -42.86905 | 2025-08-22 03:34:00 | NOAA-21 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 24b3efe4-acf1-3c05-acdc-fba7b5affb36 | -20.27408 | -46.57229 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e903595c-a505-3af9-8c9c-02c732ed2d0e | -23.59301 | -45.68135 | 2025-08-22 03:34:00 | NOAA-21 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| dd909e71-e970-386e-a2b5-cd5a0e760e89 | -22.5569 | -42.13456 | 2025-08-22 03:34:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 63275a86-5697-32be-aa1a-267438519e12 | -22.23673 | -48.39425 | 2025-08-22 03:34:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7db56864-c01e-3ae1-8c5a-4339245b1050 | -18.28519 | -45.54012 | 2025-08-22 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4843e6af-8765-3142-80bc-ae12683a96fe | -18.87881 | -45.01579 | 2025-08-22 03:34:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c4e29077-4393-3d2c-855b-8ca43806914a | -21.43129 | -45.96833 | 2025-08-22 03:34:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 21c3b5b8-d9be-3d54-8440-772b045f9170 | -17.39907 | -44.24838 | 2025-08-22 03:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55a639b4-c45e-3db0-aa5a-7f8f62fd3c5a | -17.61418 | -46.70304 | 2025-08-22 03:34:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb3064ea-95db-3e73-95e0-62ce03eba4a3 | -19.2822 | -40.05891 | 2025-08-22 03:34:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| cacc150e-c138-3243-aed4-491254c856a8 | -20.24866 | -46.65911 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f11a0e1-5f40-37c0-91c8-29da227d6a0a | -20.45384 | -41.6809 | 2025-08-22 03:34:00 | NOAA-21 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f5c8a01c-521a-360a-a24e-ecc6ad7e8c4d | -20.3535 | -48.34449 | 2025-08-22 03:34:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3dcde7bd-00b2-35d2-9186-df92a2d36fa7 | -19.5884 | -46.36156 | 2025-08-22 03:34:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b251bdf-b173-37f3-b972-df088cefcda9 | -21.04016 | -44.76302 | 2025-08-22 03:34:00 | NOAA-21 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ec734b96-63f5-32ce-8cd7-9148a128d2c6 | -20.30464 | -46.62552 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8e2d7a1-cf82-3b29-8318-3d54d3d5e5cf | -21.96019 | -44.97339 | 2025-08-22 03:34:00 | NOAA-21 | SOLEDADE DE MINAS | MINAS GERAIS | Brasil | 3167806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2c1aeb50-8727-376c-99a4-9d502be03e1d | -23.29177 | -47.4775 | 2025-08-22 03:34:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 683e34ac-19db-3d3b-914a-c27244812d62 | -18.29272 | -45.50526 | 2025-08-22 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8c354fc-7a22-3c7f-998e-209fe3ab8efe | -18.27917 | -45.51368 | 2025-08-22 03:34:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d38053c0-157c-3ca4-8335-aa1181addfa7 | -22.78362 | -44.79613 | 2025-08-22 03:34:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5b0c2de2-ad16-352e-a3f2-9e1e0824ae8c | -18.62096 | -44.26429 | 2025-08-22 03:34:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c752c285-259a-358a-991f-a8de1ed34152 | -20.26616 | -46.6877 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ada13363-b996-3320-bd20-126b78e9a1cc | -20.30355 | -46.63031 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5f429c7-7d59-3d18-9bdd-b12590d28e7d | -20.30433 | -46.62654 | 2025-08-22 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5186487a-feec-3a97-bc9b-3f5a03df461e | -21.59425 | -48.99334 | 2025-08-22 03:34:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 717a9f9b-2591-35fe-a3d6-67299024f901 | -20.45329 | -41.68063 | 2025-08-22 03:34:00 | NOAA-21 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c348d77f-c01a-30ee-9cf5-1f7ce4b2a1ee | -22.90388 | -43.49299 | 2025-08-22 03:34:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d22ec2b1-6753-30ec-a180-8d9748eca3d6 | -20.42923 | -46.50557 | 2025-08-22 03:34:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72ad4673-33ab-3570-8d72-03f67df415b6 | -16.78172 | -47.66474 | 2025-08-22 03:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| daef46be-71a3-3591-bd92-c5abdf1b01a1 | -18.62172 | -44.26699 | 2025-08-22 03:34:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1fcac785-a118-30e8-b958-5b2787ca9fa3 | -18.94302 | -48.35315 | 2025-08-22 03:34:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cd68496-92fd-3c95-96c4-485dd1579b90 | -16.78412 | -47.66032 | 2025-08-22 03:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8164c978-22f1-3b93-b5e3-2fdeef3a9595 | -18.62029 | -44.26755 | 2025-08-22 03:34:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README10.md)
