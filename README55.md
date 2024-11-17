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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1ef28c2-ff9a-34e4-88c9-0c2d5c9bd422 | -1.68727 | -48.17894 | 2024-11-17 04:29:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73ed3b78-016e-352e-b45d-bc6e77a74a1a | -3.23834 | -43.43094 | 2024-11-17 04:29:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5f5fdff-08ab-342a-b610-da5e0cc76156 | -0.94441 | -51.72699 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9463edd-9b91-3673-8bc5-17062be37185 | -3.25345 | -46.53487 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fce92e1-ab19-3c81-8d8c-69c37568239f | -4.32258 | -49.39006 | 2024-11-17 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a85c87f6-7e17-3f5e-b087-0d96dc637ff3 | -3.53513 | -50.24985 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c72a0881-8ebf-34ee-bcb5-74069606c740 | -2.67906 | -46.81932 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1d6bacd-ecfb-3290-abd2-53a2f22eebe7 | -7.36089 | -43.53824 | 2024-11-17 04:29:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4294dcba-5295-37a0-b54b-2cc2ed095bb6 | -5.46546 | -42.15298 | 2024-11-17 04:29:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eb41e369-a282-30da-86fc-319ecd983f67 | -2.86805 | -46.71822 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 08a58fb9-e4ce-342a-86da-7bbdb2c9278a | -3.52437 | -50.24808 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| fb8e3a6a-74d9-3105-ba5e-61b13e4637e7 | -2.29968 | -49.12624 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 627d5709-9b9d-39f6-83ba-1074151521d1 | -2.07748 | -48.62382 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee9e9318-0dca-33c8-a820-97e9396a6402 | -2.79797 | -52.99385 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53be4e8a-4824-39bd-a04c-91fd6c4158b8 | -1.20735 | -51.77608 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47c98237-68a9-36a5-8700-af6bacbd12a5 | -4.8857 | -50.94221 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f85605fe-b724-3ac5-bd35-a3c2d29fce7c | -3.66168 | -50.61083 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 872a6cf5-af2c-39d6-bde3-fc5c96fa9e2c | -3.98105 | -46.70491 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1881ca9c-a362-393c-aa3f-a3b272190f43 | -2.34585 | -47.46741 | 2024-11-17 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f499c0e-f220-3a58-8588-bc532f9e003e | -2.10693 | -46.41621 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cfcb45ce-59f8-348f-8516-8c44589bd3e9 | -2.68962 | -46.68722 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 704eadf5-8879-39b5-9d47-14e0f1197d93 | -2.57473 | -45.59717 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db3dab46-c31d-365b-ad8f-b2a1ace66c2e | -3.03596 | -47.98138 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01593879-92e0-3f18-b59a-31507d10f3d8 | -2.39463 | -46.18449 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7dcbe28b-d8f0-3321-b82b-d57a3b2697ab | -2.94869 | -48.32064 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 012b90f7-b190-37e0-a2b6-b17f0758a6e6 | -0.9553 | -52.41642 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 53c0cc75-463b-3658-9e3a-2cb3d93965bc | -2.36651 | -47.94072 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6528ed2-301b-3713-8880-c175a0ff45c0 | -3.19759 | -45.76189 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b734969-cde5-3cd0-900a-17a79f784a5a | -2.6709 | -46.22082 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6dca7c93-78d2-3ddb-9676-ca231a76d9af | -2.16789 | -48.33791 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c48bc68-d091-301e-a678-7a1cf67a6181 | -3.71729 | -51.84505 | 2024-11-17 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 41511808-8e20-3d8e-b0a2-64e90198b928 | -2.68076 | -52.43705 | 2024-11-17 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8817439-8802-3899-ba08-1f987e73a6f4 | -4.00829 | -46.5315 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e88b0662-a9cf-30cc-871f-f9ff2b62c3f3 | -2.52292 | -46.21184 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edfaeccc-240c-3bf9-8e25-404b3342be2b | -2.93695 | -48.32971 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d784602-2fea-33eb-b50a-21143f7ac01d | -1.94532 | -47.95812 | 2024-11-17 04:29:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 203d64ed-75e0-3e5e-bddb-ae2141e2e554 | -2.00259 | -48.76261 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20cac4fa-204d-3575-9fa2-1ca2dfce0cb7 | -2.66202 | -46.21233 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28bd7beb-cb32-3514-9618-33cc0ef1f49e | -3.01925 | -45.39936 | 2024-11-17 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c87eeaf-9ec5-3773-a1b1-16559f856c62 | -1.28694 | -51.95865 | 2024-11-17 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20a07516-4577-3927-989e-0b1ec50ed7b3 | -2.03923 | -48.35438 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c67a283-3505-3c53-ada0-bf298258c288 | -3.91702 | -46.52798 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.8 |
| be178819-b607-35f0-a774-78a9506e0225 | -3.81895 | -50.23763 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dd361a2-720c-3a2f-b3bf-93152b94ffdb | -2.16149 | -46.41408 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4301cf9-ee29-3bd8-ac01-f89c4b976b0c | -0.89608 | -51.94993 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a511b250-d391-3760-b032-f4165015d674 | -3.88079 | -46.65056 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf943edc-3bcc-3815-b96f-f416b7965027 | -2.67145 | -46.21735 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 535f5fcd-c82b-3773-9dc7-6b1398f8ba4c | -3.71685 | -51.84743 | 2024-11-17 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c2e1e4c-19d1-3009-9e24-d06a900f7e02 | -2.65271 | -46.20701 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2b93a1f-235f-3d05-bb7c-1948fa1e9317 | -4.55452 | -48.00637 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| f10a2d31-10ea-3e4c-83b3-7b179ee7204e | -2.92131 | -48.32 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 782dc2d3-71a3-30b3-9eef-3757210a778d | -1.45983 | -48.19908 | 2024-11-17 04:29:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 629e78e1-d1a8-3087-8381-beacc3a50a1b | -2.86697 | -46.72509 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 3bc5e10d-6213-3103-8d86-3286f6657eb2 | -2.2852 | -47.4863 | 2024-11-17 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6c0c2db-71df-3972-93be-d395405ccfdd | -1.10875 | -51.92314 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11d49662-6692-3ebd-a17f-0a2a075612d1 | -2.08497 | -50.49998 | 2024-11-17 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2164448e-75e7-30c9-90b4-df18a8a3af40 | -2.62383 | -48.56293 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5dd873d5-cc45-3e43-a311-86fc695395f7 | -2.67259 | -46.86053 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef7a60dc-8555-3901-874b-05ce4bbef394 | -1.62817 | -47.40799 | 2024-11-17 04:29:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77105800-c1c7-3a08-a138-9f7f2a3853ad | -2.64522 | -46.8386 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 788eb762-2260-365c-af0d-e9db73da77b1 | -2.6764 | -46.20743 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f38cc59e-96ee-3df2-9e33-e2eea546c9b4 | -2.21964 | -46.4129 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93aa10b7-6267-372d-83c5-8662471cff94 | -2.08669 | -46.32827 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64856471-5e90-37f7-ac29-45fa5bde2d8f | -6.65904 | -47.10785 | 2024-11-17 04:29:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 535e799c-13b5-3f9e-b7e4-7ce9d0f7a9e4 | -5.13292 | -45.113 | 2024-11-17 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fafc4d3-0825-31b4-9018-b043da41be81 | -2.66466 | -46.17356 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca264f78-7ddc-3199-adb7-6e8c8f93cb3d | -3.97611 | -50.93375 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09a6ff2e-c66b-3a1e-9402-05e1697b5193 | -0.98983 | -51.78193 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45c836b1-b65d-3450-8b0a-1ebaa2a6e44e | -3.18296 | -45.44645 | 2024-11-17 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 458cc66b-ebff-395d-9c70-af5d8cd75446 | -3.20634 | -46.46732 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69c9017f-cb9e-3036-8c4e-3cbb2e85c574 | -2.21426 | -48.40377 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c090b45b-0c2a-391f-bdbb-9412834a235d | -2.94199 | -48.31959 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54b02cb6-c491-3dd6-9510-d9f6bfebb677 | -2.17217 | -48.55289 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f1a44fa-9d6b-3806-b494-c99731369e2f | -5.28137 | -47.51347 | 2024-11-17 04:29:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29bed56c-72c7-3d91-8114-f9dc26008350 | -4.24661 | -48.53094 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0e7a64c0-53ff-3cc9-aebc-a46fa41f094e | -2.14081 | -48.7762 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ff3f90b-f968-360b-afe0-04b09cb2d78e | -3.19496 | -46.53998 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 619c1ae3-2abb-3d9f-ac7b-d04c3d3de92a | -5.05797 | -44.22386 | 2024-11-17 04:29:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48791be0-7a75-340a-9b54-d4df13a7633e | -3.99528 | -46.39729 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 389c5484-995a-3d69-a131-29e240dbe35d | -2.58828 | -46.11864 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee279b0d-cb55-3541-83cf-d3f31aa7511c | -2.29606 | -46.44542 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e79b78c7-4bec-34f1-a200-60c22d488dd4 | -3.88574 | -46.64066 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a910b57c-2434-382e-abbd-0eceed8bbb68 | -3.19442 | -46.54343 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d190eed8-f6b4-36d1-b060-8190fdcf18a6 | -2.90262 | -45.02098 | 2024-11-17 04:29:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e460a495-9073-3922-baf8-6ab71a2b64e1 | -2.21633 | -46.41238 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a2b1c8d-4cda-3867-8559-6fb46f35cd73 | -3.17306 | -45.8091 | 2024-11-17 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7ebd150-4e23-3c02-9278-3f1d922a732f | -3.95401 | -46.70424 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e416a46d-aaa1-3849-9ce2-b894e7d8d868 | -1.96083 | -48.67306 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a94c8096-f724-3957-aeca-c36b3efb5219 | -2.54535 | -47.30136 | 2024-11-17 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcc1e068-6529-36fa-a9f7-16b16f9587db | -2.62894 | -48.55265 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c4248419-6938-3725-829c-ba6601988413 | -4.37378 | -48.56551 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 362fd76e-8ea4-3d5a-b1b3-e40b11d0f330 | -2.90724 | -46.83708 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65f76b30-be35-34ca-942e-5bc56c58b0c8 | -3.78814 | -46.67876 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8afd52d3-056e-3467-8edd-1164a7fa4d2c | -1.52039 | -47.46592 | 2024-11-17 04:29:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c77246e-efa9-3684-aa7c-66c228a5f728 | -1.99598 | -46.5821 | 2024-11-17 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c322958-bec3-31a2-8496-f9ce7a9557ad | -2.39264 | -47.94507 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a75d00df-1542-3c4b-afb4-90982c4c883d | -3.18502 | -46.53843 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ddfb54d8-55fe-3c63-a252-14d5e4ac6b9a | -3.94521 | -46.71707 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e47c96e-ac93-3d95-a43e-523cfd42bfa5 | -2.08761 | -48.26655 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6c347648-e554-389b-9922-67d6f08e8350 | -2.68026 | -46.20446 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README56.md)
