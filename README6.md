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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1891d2f8-354c-3c87-b833-002a0d255a68 | -2.27205 | -46.44373 | 2025-11-23 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b4f6c61-4731-3ab3-ac45-89a6e3176210 | -2.88197 | -45.27095 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffa1aae3-fcd3-3bab-962f-ad2dcfb54f93 | -2.56468 | -47.63247 | 2025-11-23 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 871f2325-8df3-3f56-958c-498bb2407d28 | -3.79737 | -46.04894 | 2025-11-23 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef3809d1-5cec-3ca2-abe8-ecdc76700cfb | -4.45851 | -44.10443 | 2025-11-23 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fdcbe204-7469-3ef8-8b6c-21646241a926 | -5.55006 | -47.23163 | 2025-11-23 04:25:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93eb2b73-c30f-3c58-a673-7e9fc30bcc33 | -6.37664 | -46.32687 | 2025-11-23 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80952c65-d944-3e8d-8233-bd3f5f6c8a4c | -5.69133 | -46.16529 | 2025-11-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf39b5a6-b96d-3221-bbd5-575791cd6d32 | -1.1933 | -53.71614 | 2025-11-23 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 394a346c-d9e6-39b4-9e9d-609b3b6b58b6 | -5.97966 | -40.38747 | 2025-11-23 04:25:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 21.5 |
| de73906e-5c57-34b4-9209-d74f6934accc | -2.88642 | -45.2857 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 874e77cc-6fd2-35a9-afdc-5e5b75989783 | -2.99104 | -44.39798 | 2025-11-23 04:25:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d855600-ade9-3490-8c5a-b948e78968bb | -4.5573 | -45.08466 | 2025-11-23 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf85279f-471c-31e8-b7c8-ffb208793dde | -2.88089 | -45.27781 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b750a7fe-131d-3080-99a1-27197c2feb79 | -7.29907 | -48.41869 | 2025-11-23 04:25:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b94182f6-996b-3e44-9485-52c6d72cae72 | -5.67778 | -48.7896 | 2025-11-23 04:25:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cdd117cc-b4d3-3ca7-aab0-d6a1fa338df8 | -2.963 | -45.01239 | 2025-11-23 04:25:00 | NOAA-21 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7428bab5-af3d-34da-bda2-7c07761fe099 | -2.02607 | -47.15147 | 2025-11-23 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c33d0a9f-5a50-3e4f-999e-a48ea850b960 | -4.61131 | -45.63151 | 2025-11-23 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acdf30c6-2884-3e47-b99d-9a3935bb3170 | -3.38895 | -47.19354 | 2025-11-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0adf24a9-dd71-32ee-a1a7-5839cf6eab54 | -2.49535 | -47.09526 | 2025-11-23 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17000bda-485c-3035-b02f-64726952bf7b | -2.87813 | -45.27387 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6d7b76d-1900-3aa1-adfd-2f5eb7bc817e | -4.55102 | -45.49456 | 2025-11-23 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 30321215-b268-3196-af80-d0785d1be5c1 | -7.74138 | -47.25316 | 2025-11-23 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7dd0e1cc-f8de-3483-a585-6636b2b1b43d | -3.9192 | -46.74557 | 2025-11-23 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2263c9e4-5ff6-3ed6-b257-8740ec8dbcce | -3.72251 | -43.22021 | 2025-11-23 04:25:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e57b8e34-7ffa-30e4-9aa3-498f22f9d670 | -6.93634 | -39.23244 | 2025-11-23 04:25:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cfd84ce3-9ab6-31cd-bb82-58ba6e3a4c0c | -4.04974 | -42.5247 | 2025-11-23 04:25:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 55621012-2d03-343d-9dc0-b43b7f3128a9 | -3.3964 | -47.56731 | 2025-11-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eac52504-ebd6-370c-91d3-892294775bfb | -4.55784 | -45.08119 | 2025-11-23 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fa73ad40-7d6a-35bf-9d48-954916ed13bc | -2.88804 | -45.2754 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b4e3c0f1-b899-3032-a244-fbcd5d6eb0b1 | -5.72923 | -46.46532 | 2025-11-23 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03da6f9c-be63-3c3c-be85-847e6028d1fb | -3.52481 | -42.37179 | 2025-11-23 04:25:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cf879cae-d706-3ab3-8832-1b5fd62765d8 | -3.13655 | -41.47586 | 2025-11-23 04:25:00 | NOAA-21 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bd281aaf-1aa3-3618-94ca-6ec6242148d9 | -2.44614 | -49.09399 | 2025-11-23 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9eef212a-b378-3a5b-a223-9d3874572020 | -5.02823 | -47.62085 | 2025-11-23 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cb6f633-ff5c-31d6-b30d-6cbe79b39159 | -3.91975 | -46.74205 | 2025-11-23 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59701c5a-66ec-36fa-a2e5-818a6042a193 | -3.41477 | -43.14749 | 2025-11-23 04:25:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9af6fa3-8fb4-3951-8862-f24ba0c2ee46 | -2.99049 | -44.40149 | 2025-11-23 04:25:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5e1a5f3-ed63-37f5-a0d3-a4e659fedb0d | -2.44607 | -47.15926 | 2025-11-23 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 284f8c47-d420-39ed-87cf-bf20aaf9b7a4 | -2.8667 | -45.45485 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c2116e77-4caf-3fba-a1d7-0bfc1cf1c71a | -4.11349 | -46.18018 | 2025-11-23 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f4e3048-994f-3a1e-a3ec-5cd7eae41d1a | -2.95577 | -45.43061 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d883932d-a3e2-3da4-8bb2-b1c55f07ab82 | -6.91058 | -39.87198 | 2025-11-23 04:25:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 398ddd7c-6c2b-3a6b-a01e-790675fb07fe | -4.16718 | -46.12204 | 2025-11-23 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f107b567-6176-3440-a12d-63ec7cc73be9 | -4.045 | -42.52074 | 2025-11-23 04:25:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| b2e45672-02c9-366b-b744-771e9eb59f54 | -4.15849 | -46.1772 | 2025-11-23 04:25:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48e88fda-e019-30d8-b778-18535b41f48d | -5.70555 | -37.94738 | 2025-11-23 04:25:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 068758ac-884f-3d01-afba-84e6ad153b25 | -3.41666 | -43.14687 | 2025-11-23 04:25:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df487eac-d236-30a4-b22a-9e47ef2df216 | -4.30306 | -47.54154 | 2025-11-23 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 21293c37-ea53-3785-933e-452315efc8eb | -5.6736 | -48.79306 | 2025-11-23 04:25:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 355b7ab2-cc03-36a3-8b8c-ae915c80aa3d | -2.49593 | -47.09162 | 2025-11-23 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b329f8db-9f95-343a-bf9e-dc8930c17cc4 | -1.7461 | -52.02212 | 2025-11-23 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cca11c97-4f9f-3cec-94ff-2829c3f3e93e | -1.31905 | -53.14859 | 2025-11-23 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1af7c109-70a4-3f94-8524-35df4d650b2d | -1.74461 | -52.03141 | 2025-11-23 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a4e4959-f5fb-37d7-9824-186ab7c5ca7a | -4.5637 | -45.50004 | 2025-11-23 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aa4780f4-8d28-3510-a1ba-afba0982f6f6 | -1.86397 | -54.07259 | 2025-11-23 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea2bca3e-5dd1-3228-801e-02143db39810 | -4.71484 | -46.46693 | 2025-11-23 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87c5519e-0c2d-363d-99db-490157119aa7 | -4.71539 | -46.46346 | 2025-11-23 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| dbc39cea-af8b-3f4d-b7f5-4e05b0c25965 | -4.7187 | -46.46397 | 2025-11-23 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| a55791c7-02df-3863-b59d-9d3e5b58a607 | -4.60518 | -43.28518 | 2025-11-23 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 96cc6103-e107-3203-a04f-e386a7a2b994 | -2.46935 | -45.42744 | 2025-11-23 04:25:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ee8f0c39-7ad2-3ec2-bd1e-e4c4a73ef377 | -2.89464 | -45.27642 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 173ae052-e022-3b84-bed0-a1af78735dd7 | -5.9669 | -49.37828 | 2025-11-23 04:25:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33c40655-dac6-38ec-9fda-8e23f9cf5546 | -2.27539 | -46.44424 | 2025-11-23 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0dbfa637-8e18-3697-8eed-661907ba3aae | -2.52447 | -45.98658 | 2025-11-23 04:25:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 656f4fdc-1861-307a-9ddc-b75b3f658a30 | -4.3427 | -45.58915 | 2025-11-23 04:25:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65fb9688-9b2e-3a50-a4f4-97ee44182076 | -4.01921 | -44.13046 | 2025-11-23 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afd59ead-2353-3f9d-97bd-d4927f9025c5 | -1.86351 | -54.07549 | 2025-11-23 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d57e2910-f9da-3576-ab36-c259c47f7966 | -4.64269 | -45.47416 | 2025-11-23 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbed7b59-5903-3f2a-bf06-f53accecf1cb | -2.50099 | -47.10363 | 2025-11-23 04:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb5c5ff4-956a-3628-bde7-a4f6a447cfc1 | -4.75555 | -47.52221 | 2025-11-23 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56e513c8-9126-3304-be08-bdbbc5fd5f6b | -5.40366 | -46.41281 | 2025-11-23 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4c9bf84-4d48-3db2-a4bc-33380b9e8875 | -2.93531 | -51.07189 | 2025-11-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc89d6d0-ea8d-3e85-b18d-9d80f394d9f9 | -6.72184 | -39.68503 | 2025-11-23 04:25:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7d66c4d2-12c5-307b-93e7-17e032c40145 | -8.72777 | -48.318 | 2025-11-23 04:25:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b36bcbfb-ea8f-352d-855a-8cbb1ee43228 | -1.19511 | -53.71586 | 2025-11-23 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04d78004-5642-3491-b8be-57dd6d559e1b | -9.9327 | -44.71698 | 2025-11-23 04:25:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 68cffcdc-c5cb-3377-808b-14f15a92d468 | -1.73697 | -52.02071 | 2025-11-23 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c44110f8-d165-3601-aec1-18f6b43ac339 | -2.87054 | -45.45192 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 9cb3d9c0-f4d6-32da-bfe8-2ba8791930a1 | -6.06562 | -46.53275 | 2025-11-23 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4d6b15f-ced6-3b5d-b5bf-0b20b80a8f8b | -3.58331 | -42.40901 | 2025-11-23 04:25:00 | NOAA-21 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d3615659-f76a-3ff6-aacd-aec05f3e8e46 | -2.87705 | -45.28073 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6727ac6-4bc7-3b8f-9d81-efdbbaac5d80 | -2.98944 | -44.43005 | 2025-11-23 04:25:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 302d6bf8-221a-395a-9bce-3af42b830fa0 | -2.87438 | -45.449 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0712761-54d2-37f4-8050-0c2f1302fefc | -6.27087 | -44.68745 | 2025-11-23 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| def6bd5a-e510-355a-8d56-c51e35d54f13 | -4.52106 | -45.42637 | 2025-11-23 04:25:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7de1211e-398f-32e3-bc30-d3f0399e2682 | -2.39289 | -45.7852 | 2025-11-23 04:25:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa7469cc-2465-3637-840e-89f328ff06cd | -2.98775 | -44.41902 | 2025-11-23 04:25:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6cfa182-8c68-3cec-8e5d-b4c428b8a15a | -2.56408 | -47.63627 | 2025-11-23 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af27f3a5-0ae3-33b6-ab66-7a9b88e3117b | -5.61536 | -47.14387 | 2025-11-23 04:25:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3aab1425-36f5-38a6-9f80-f867b21ffc6d | -4.55833 | -48.48775 | 2025-11-23 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 934fe273-a991-33d0-b4a8-afbb527209d9 | -1.31407 | -53.14793 | 2025-11-23 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4eb60a13-09b1-32c6-9d3e-fe8c93bf0b24 | -7.30611 | -48.39687 | 2025-11-23 04:25:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 19326631-e02d-3ce1-94aa-20be25318f0f | -2.22999 | -53.64648 | 2025-11-23 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6f8f2f1-b684-35ce-afcb-409574f4952f | -2.88143 | -45.27438 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7793ffb-bb1d-3dec-8cf4-a18113df6fc5 | -1.31002 | -53.14151 | 2025-11-23 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8dfa9b7-e626-3e0e-8b4b-52d311532ad6 | -6.72252 | -39.68039 | 2025-11-23 04:25:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 38c407d7-40c1-3646-8527-6dbde52edcde | -7.73751 | -47.25614 | 2025-11-23 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d758eac3-d8a6-37f4-a8c5-acc3f01e355e | -2.88036 | -45.28124 | 2025-11-23 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 77.7 |


[Clique aqui para ver as próximas entradas](README7.md)
