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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b084b3b-27e9-3193-a6a8-00eeba249d13 | -10.42992 | -44.89716 | 2025-02-22 03:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7fce7a5-fbe7-3fb4-a2f4-04fb14750643 | -7.89096 | -43.55034 | 2025-02-22 03:23:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4ec83fcc-a2df-3ec3-82ae-69170ce04a1c | -7.37825 | -34.88627 | 2025-02-22 03:23:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d7336d37-ff90-3c56-91a0-f2b7daecd0b0 | -7.89205 | -43.5446 | 2025-02-22 03:23:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41016e39-a928-382a-903b-036c6e28056d | -10.8243 | -37.16673 | 2025-02-22 03:23:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8f054925-6214-300f-affe-7d0a7db36138 | -7.45833 | -35.13432 | 2025-02-22 03:23:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 010bc27a-532f-3729-9e64-0bb018ba5ede | -10.15885 | -36.47624 | 2025-02-22 03:23:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 628ae985-26ee-3e3b-9567-a9406e83356e | -6.91397 | -35.57571 | 2025-02-22 03:23:00 | NOAA-21 | PILÕES | PARAÍBA | Brasil | 2511608 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 894bec83-fbd3-3d0c-9917-a9400200e2e0 | -12.27602 | -44.83502 | 2025-02-22 03:25:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a813e6b-8b1a-359a-9a97-79259e0e3ae5 | -12.81779 | -44.98593 | 2025-02-22 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d991cf94-7494-324c-ae6d-9c0761d04112 | -12.81654 | -44.992 | 2025-02-22 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 00f9901f-ff3d-347a-bbd6-010a2d610e88 | -12.82093 | -44.98832 | 2025-02-22 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d071f5a9-60a6-31a2-a3fa-7d77ba293aa1 | -12.82756 | -44.98978 | 2025-02-22 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f5cd2e6f-ef71-313b-adde-afe261ac2aae | -12.28012 | -44.83399 | 2025-02-22 03:25:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3cf625d7-b575-387e-9750-3835aed3c818 | -19.71717 | -40.35205 | 2025-02-22 03:25:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5379ebdc-cd61-32ae-ac3a-3bba74870783 | -12.2838 | -44.83083 | 2025-02-22 03:25:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1229fa0-aaa2-3982-b75c-15cdf1afb262 | -12.8143 | -44.9869 | 2025-02-22 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c67b37e-4059-3ba6-a271-c43b64157f66 | -12.82626 | -44.99591 | 2025-02-22 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b4a3af52-36aa-3cc7-b17b-b886e163f8c5 | -17.77859 | -39.57363 | 2025-02-22 03:25:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bde72bce-9c3a-3b9f-a6d2-63531d597e65 | -14.43045 | -45.62744 | 2025-02-22 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab73df20-16f5-3af2-ab7a-40ea6fe3171b | -19.71721 | -40.35422 | 2025-02-22 03:25:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e45ce02b-fd68-3ae9-8bf6-2dae2cbe4950 | -12.81301 | -44.99295 | 2025-02-22 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dbb13ad8-91a7-346b-8beb-b58d03ffaaa5 | -14.43714 | -45.62891 | 2025-02-22 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51572800-9a6b-39d3-a293-653e5aada938 | -12.81964 | -44.99441 | 2025-02-22 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 831ff53e-ad40-3845-b873-32e2e37b979b | -20.99899 | -44.16491 | 2025-02-22 03:27:00 | NOAA-21 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e603d172-e954-3d40-9f6c-186d3410a0d7 | -20.62091 | -42.48481 | 2025-02-22 03:27:00 | NOAA-21 | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| c68b5ac0-a3bc-32e0-854e-97e9dfcdf38a | -20.12658 | -45.44421 | 2025-02-22 03:27:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 99306ae0-71d8-3963-b3da-58a72719b81b | -20.12545 | -45.44918 | 2025-02-22 03:27:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fa938ad7-5cbe-3774-92c5-3a274bb12b48 | -20.76743 | -45.84122 | 2025-02-22 03:27:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 09ac8277-3912-36c6-9c2c-3fbb16883159 | -18.87011 | -47.65882 | 2025-02-22 03:27:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abc917c5-d0f4-3ef8-b9d3-61e488aada88 | -20.88842 | -46.17389 | 2025-02-22 03:27:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fa48799-8d74-34b5-96fd-938a6939fbdc | -20.88227 | -46.17252 | 2025-02-22 03:27:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c19b15ea-ebdb-3c49-9ea1-688deb428d19 | -20.99831 | -44.16496 | 2025-02-22 03:27:00 | NOAA-21 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f13a36f9-5dbf-3d17-8353-061bceb07687 | -19.83634 | -40.86728 | 2025-02-22 03:27:00 | NOAA-21 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a5b7d8b4-a316-37a9-aca5-179bdcad1c6b | -19.83176 | -40.86651 | 2025-02-22 03:27:00 | NOAA-21 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8a642074-bfd0-3d3a-8866-3a831acba610 | -20.99356 | -44.16364 | 2025-02-22 03:27:00 | NOAA-21 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d7b4a903-e704-36d4-bb8b-16ee45726862 | -22.71694 | -43.23765 | 2025-02-22 03:27:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5be3f11c-e401-36f0-a00b-6399305cf641 | -6.18354 | -37.13036 | 2025-02-22 03:46:00 | NPP-375D | JUCURUTU | RIO GRANDE DO NORTE | Brasil | 2406106 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 388a57cf-36af-3afd-8ee2-cce865b9d652 | -5.83071 | -35.52352 | 2025-02-22 03:46:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5bdc7b41-301c-38b5-9218-2ec057416f7b | -5.56877 | -39.25035 | 2025-02-22 03:46:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4df6668e-8cb3-3607-9217-b1af2fde5883 | -6.91156 | -35.57523 | 2025-02-22 03:46:00 | NPP-375D | PILÕES | PARAÍBA | Brasil | 2511608 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 944346ae-595d-3dcc-9446-27b53dc069ec | -4.59234 | -37.90527 | 2025-02-22 03:46:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 67699f8e-d62b-331f-90bc-d4f7d77a7cc4 | -10.35707 | -44.9156 | 2025-02-22 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c962493-a0f8-3bcc-8ca7-075ac1c9f975 | -12.84269 | -45.00244 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0afe25b5-c75d-332e-8d89-414d0aac6047 | -12.51438 | -45.49319 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da3696f4-a2ea-3ef5-b7db-4082b6592f86 | -10.35618 | -44.92039 | 2025-02-22 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03c3bbca-4605-31c2-ad98-e7802bde21e8 | -11.4885 | -38.01112 | 2025-02-22 03:49:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 5a272e72-21a4-3163-b43a-04ca579b1580 | -12.83261 | -44.99289 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ec1c521-d8d6-335b-9ac6-352c99e8bbc7 | -12.83176 | -44.99744 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 598d4fa6-4b2f-3e4a-afe6-9b29cd40ae46 | -12.82732 | -44.99654 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7af5c9cc-e3fc-3b06-b2f3-da1b7dbee06e | -12.83017 | -44.99514 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 934d3a6d-5dcc-33f7-aba2-b07316867890 | -8.14023 | -44.39978 | 2025-02-22 03:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa63f5c6-96f6-3c7e-9d68-caa915cb15e5 | -7.89679 | -43.54995 | 2025-02-22 03:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3ac5352-ceaa-3dd2-aac5-2d84f8d6029a | -7.45734 | -35.13463 | 2025-02-22 03:49:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b3e69fc7-dd73-30da-93e2-08ae00bb821a | -10.46708 | -38.45963 | 2025-02-22 03:49:00 | NPP-375D | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 39a93229-5830-3776-b396-a98cec8f1b5b | -12.84065 | -44.99924 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49834703-8395-378e-9462-51d2d2d42bdb | -7.06933 | -40.79599 | 2025-02-22 03:49:00 | NPP-375D | SÃO JULIÃO | PIAUÍ | Brasil | 2210300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| db2aa875-446c-3540-8cf0-035383c77034 | -7.06916 | -40.79835 | 2025-02-22 03:49:00 | NPP-375D | SÃO JULIÃO | PIAUÍ | Brasil | 2210300 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ab87dc28-2afb-3bee-988b-d63c8715c4a0 | -12.82572 | -44.99425 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de5f16ba-0af0-3d4b-b649-08aeafc8e6ea | -10.5704 | -37.97462 | 2025-02-22 03:49:00 | NPP-375D | ADUSTINA | BAHIA | Brasil | 2900355 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d393b87c-d830-31d5-87b4-a9fbce8fbc37 | -10.43247 | -44.89513 | 2025-02-22 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b5706be-aa31-30f6-bd87-c52600aa1498 | -12.83462 | -44.99605 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6dcd9bd-fc94-3bd2-a1f4-31cea898fb98 | -7.47669 | -34.84254 | 2025-02-22 03:49:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 48da414c-a587-3a66-a2b5-c8b1e2ab033a | -10.35833 | -44.91853 | 2025-02-22 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d0e3f6e-e320-3a63-b4e0-a0380a05344b | -12.82934 | -44.99974 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5979398b-db6f-3050-89ee-b209fd994a47 | -7.46078 | -35.13517 | 2025-02-22 03:49:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 5d772cc5-573a-3642-b297-05c8882660ea | -7.4579 | -35.1309 | 2025-02-22 03:49:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 003fe94b-f027-3130-8e58-6157202b674b | -8.65438 | -36.77956 | 2025-02-22 03:49:00 | NPP-375D | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 99b9c241-f6a1-32e9-af22-720a37560b5e | -12.81764 | -44.98796 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4c89f48-89a2-3942-a6a0-257ccf708b53 | -12.83621 | -44.99833 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 775b3596-4e01-32a0-ae71-663ac4f5333f | -9.27168 | -41.21853 | 2025-02-22 03:49:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d9768cb4-5a7b-3839-a4aa-dd7085deaaa9 | -10.36082 | -44.92122 | 2025-02-22 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 136f733f-61b0-3f9e-94f2-4c543c25c227 | -7.89631 | -43.54743 | 2025-02-22 03:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 47df9879-9344-39a5-8dbc-e4c65a0897c4 | -12.82127 | -44.99337 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 513c335b-80b6-3365-abd8-309e4b99b224 | -12.27671 | -44.83423 | 2025-02-22 03:49:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64bf0ee2-fb22-3f21-9785-c252ee99c052 | -12.82209 | -44.98883 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d43615d0-64fc-3e36-95c6-96ddd96ee85e | -12.82654 | -44.98971 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52d13e71-03d5-3ab1-ad67-4adf39ffeb5a | -12.81845 | -44.98346 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d92c896e-5ff5-372f-855f-08535132340b | -7.89239 | -43.5492 | 2025-02-22 03:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68cdb16b-4ec7-3f24-b077-7e09a63e6aca | -12.28195 | -44.83071 | 2025-02-22 03:49:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7cde3582-0721-3c3f-bfad-5f4a2e13d874 | -9.93219 | -37.23602 | 2025-02-22 03:49:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0d4388e6-9dd7-3b7c-a18d-b7c150a5b920 | -12.83825 | -45.00149 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68e99d25-5431-3eb2-a04a-8d8d2bd9fb19 | -12.81682 | -44.9925 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3804efd-28a0-3107-a1ec-253d73d55b1a | -10.43334 | -44.8903 | 2025-02-22 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3027f907-cbe7-33a5-b759-8bee56d9a96a | -12.83981 | -45.00375 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 230da03e-7781-3c9d-842f-efb53df72261 | -7.37597 | -34.88665 | 2025-02-22 03:49:00 | NPP-375D | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f7d81119-80c1-3bf1-a227-c5e8f16ed36d | -12.83536 | -45.00286 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c94b5951-0fc2-3aa9-b1a3-bdbee393697c | -7.47508 | -34.84304 | 2025-02-22 03:49:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9f662471-16dd-35be-a45f-8bfeda9f56bc | -7.89311 | -43.54492 | 2025-02-22 03:49:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3923e1c-30b8-378d-9ed7-975c3bd651c5 | -12.82817 | -44.99199 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8abd5bc7-8ec9-3ab1-b82e-edc2def7eb4a | -10.69599 | -37.04982 | 2025-02-22 03:49:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| afd98bff-2fea-3978-8422-1fd5b4a41161 | -12.8338 | -45.00061 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73bc073f-4d44-34c5-a086-7b681dc97dab | -12.8229 | -44.98432 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d270a95-1a2d-35e5-bac0-ecddac959238 | -12.83099 | -44.99059 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45c5de09-ab14-3546-9854-ece9fd394651 | -8.52624 | -36.27882 | 2025-02-22 03:49:00 | NPP-375D | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3d2a5411-8965-3db6-8191-5b085ae26d8e | -12.50975 | -45.49231 | 2025-02-22 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44a6a0e1-4d00-385a-a13c-11d1fb3c1a17 | -7.22763 | -37.74014 | 2025-02-22 03:49:00 | NPP-375D | OLHO D'ÁGUA | PARAÍBA | Brasil | 2510402 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 97cfe13c-dcaf-3a6a-a92e-daf5dab89ab7 | -20.61986 | -42.48177 | 2025-02-22 03:51:00 | NPP-375D | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0e945489-a381-3a5d-87a5-ca61551ce8e1 | -17.05903 | -45.04173 | 2025-02-22 03:51:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a28f960-3920-3495-93ba-8092d957f941 | -15.05083 | -42.42641 | 2025-02-22 03:51:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README3.md)
