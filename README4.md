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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f1742ac-78a7-3c2b-a015-b98903cd26ad | -8.56322 | -39.47456 | 2025-12-17 03:36:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fb0e1847-544b-3700-954d-af2a40d59b6e | -2.94121 | -45.68444 | 2025-12-17 03:36:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d848ab0b-6289-3147-8fd2-256450dd3c46 | -3.25462 | -41.42171 | 2025-12-17 03:36:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7eab70dd-2fe5-3acb-91cd-91e864f55c2e | -6.57508 | -35.41297 | 2025-12-17 03:36:00 | NOAA-21 | CAIÇARA | PARAÍBA | Brasil | 2503605 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b48beb0b-d8d0-3a0f-b43e-61f79861969c | -7.84134 | -35.02168 | 2025-12-17 03:36:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 7e07fbc3-783a-3d99-97ee-ee248f5e8f71 | -2.04863 | -45.45306 | 2025-12-17 03:36:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 530f72ca-2359-3b01-8f19-144b51c9c950 | -3.33411 | -45.42285 | 2025-12-17 03:36:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d26d82ad-70c5-3dac-8e7c-c086ece72f16 | -8.51563 | -36.62157 | 2025-12-17 03:36:00 | NOAA-21 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6fa06dd4-c359-3551-9f22-9a3d4ea22cb2 | -3.25512 | -41.41871 | 2025-12-17 03:36:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 26f18a7b-418f-39d7-ac1d-6d2a8184335b | -5.55574 | -35.72356 | 2025-12-17 03:36:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 89328d1c-adc5-33ca-b28a-2ee8b7a1c44d | -2.63057 | -45.67032 | 2025-12-17 03:36:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8af913fc-ea0d-3bd1-a4a1-dd310659224f | -1.41425 | -46.06702 | 2025-12-17 03:36:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9549cb7b-4395-393e-af33-275d23042f22 | -2.90734 | -45.58071 | 2025-12-17 03:36:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9bcc5d6c-7f60-33df-a6b9-727b61cf4892 | -3.03339 | -45.34769 | 2025-12-17 03:36:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dc509c84-1e3a-3fba-9db3-a848931addd4 | -3.03244 | -45.35323 | 2025-12-17 03:36:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33bc208e-d4fc-3efb-9bfc-ea9e4b2c3639 | -2.63732 | -45.67145 | 2025-12-17 03:36:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9139e01b-45a1-3c2b-a13b-30126bc913ad | -4.99621 | -38.05861 | 2025-12-17 03:36:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 561da7ae-2b44-3cc9-bd49-69379b927f7b | -2.94978 | -40.44501 | 2025-12-17 03:36:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ec65eae-372f-3fc8-a9b7-a5f6777b2b83 | -7.83744 | -35.02471 | 2025-12-17 03:36:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 11a3ad4e-be1d-3565-ba9d-6ddf63029830 | -5.57618 | -44.88742 | 2025-12-17 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dab8f1a6-1a3a-3b28-ab48-31c528913aff | -2.93527 | -41.14774 | 2025-12-17 03:36:00 | NOAA-21 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 180c6662-bdfd-3078-9c04-78ddd67ba1d7 | -5.19472 | -35.77019 | 2025-12-17 03:36:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 177fc10e-1ad9-3851-9f4e-cee661048c6f | -5.32948 | -36.80466 | 2025-12-17 03:36:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 786cc39a-1593-37a1-aa96-2302d4e8c827 | -9.15915 | -35.68952 | 2025-12-17 03:36:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| f002b003-1f73-3363-b55f-24287763d974 | -2.90635 | -45.58656 | 2025-12-17 03:36:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a7e08e4d-03e0-3eee-bf4a-1e1a7394bf1c | -6.70524 | -41.19944 | 2025-12-17 03:36:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 123ac3e2-31d5-37d2-891e-8b4bb7ddcdfb | -5.55358 | -35.72305 | 2025-12-17 03:36:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5a5b5734-ba1d-3ed1-b3a4-3d15635e5746 | -8.58868 | -39.44864 | 2025-12-17 03:36:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 2670bb6d-973b-3d09-ac4c-d6df9db88a17 | -4.33073 | -39.14422 | 2025-12-17 03:36:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 68cca22f-44c7-34a2-a0d2-f8d74e4f93b8 | -7.838 | -35.02116 | 2025-12-17 03:36:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| ab9e410f-c8ba-31b7-b642-21e344013d20 | -4.43665 | -38.46283 | 2025-12-17 03:36:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 75514bb3-27fb-3bf3-bc03-8a2316c47934 | -2.91084 | -45.58213 | 2025-12-17 03:36:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f90fb9d2-bfc8-3f91-af01-d9b490856db7 | -5.5823 | -44.88864 | 2025-12-17 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d25ff06-a47f-3ad4-a154-f7a3cdcfe21e | -5.58142 | -44.89362 | 2025-12-17 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 203b7445-a970-3b7a-be4f-130ea4c8310b | -3.26022 | -41.41947 | 2025-12-17 03:36:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a15e04b1-bdd9-3acf-80b2-76ed37b0b264 | -3.87287 | -40.45142 | 2025-12-17 03:36:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 72dfda98-be25-3c15-bc74-1ee98ce5af3e | -2.88529 | -45.46922 | 2025-12-17 03:36:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 60d39898-0750-3345-8a77-7b85d758cf6b | -5.1982 | -35.77073 | 2025-12-17 03:36:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8dc47e37-3d14-3c44-9f54-32f8914e0b29 | -3.03903 | -45.3543 | 2025-12-17 03:36:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4c421f27-ff05-3d34-aa0b-98cae496ee55 | -15.46718 | -39.23714 | 2025-12-17 03:38:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 313cde73-b095-306c-8085-5d7da43ee44a | -11.96949 | -44.49764 | 2025-12-17 03:38:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01ab6668-59cb-3b03-9a6f-2fa8119233a4 | -11.74979 | -43.30699 | 2025-12-17 03:38:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa646e8d-fc80-31f0-8c0e-e6a623416100 | -10.37211 | -44.88208 | 2025-12-17 03:38:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06390ef2-6036-310f-903d-44bce91b6fa0 | -9.36306 | -40.52872 | 2025-12-17 03:38:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b0d20b01-c468-399a-aad0-dd2db13dd0da | -11.97018 | -44.49417 | 2025-12-17 03:38:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61bf5ea0-4014-3cfc-b2d6-8e5e7a6c673b | -9.26448 | -44.31271 | 2025-12-17 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f87529a-2e13-350e-afad-de95831d9121 | -10.37059 | -44.88987 | 2025-12-17 03:38:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f54c3c70-627c-397e-b764-2b6979e71eb1 | -9.15729 | -40.97515 | 2025-12-17 03:38:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c564bd65-4477-3c7e-a412-d1159a41dcf0 | -11.75006 | -43.30577 | 2025-12-17 03:38:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ba87772-96b1-3e46-bb4b-86b428c7b9fd | -11.41669 | -40.77501 | 2025-12-17 03:38:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 87ab1eed-016d-3b5e-9c70-1b631db8b9e2 | -11.96827 | -44.49183 | 2025-12-17 03:38:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e23956c5-c214-3646-8e21-3304ca21695e | -10.62191 | -40.52026 | 2025-12-17 03:38:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 881478c0-c3bb-3c83-bf9d-ac4d872ed48d | -9.26379 | -44.31646 | 2025-12-17 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5da7c26-e1a1-397a-87bd-5254558fb45c | -9.8217 | -40.57033 | 2025-12-17 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ef2401a8-dbdb-36e3-ad50-1333b16c6004 | -11.37695 | -39.26109 | 2025-12-17 03:38:00 | NOAA-21 | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d696296e-5354-3130-a125-e4146c5ae64f | -11.80063 | -41.77539 | 2025-12-17 03:38:00 | NOAA-21 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ff1301aa-4085-3c4e-8b44-b14ffdc36cf2 | -11.74923 | -43.30991 | 2025-12-17 03:38:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f55bd41d-3976-35c0-8ad7-89cc78cba2a3 | -16.27288 | -40.08554 | 2025-12-17 03:38:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bd303934-32e9-3d3e-8e24-a45c94b027d3 | -10.37136 | -44.88595 | 2025-12-17 03:38:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe485260-8ad4-3f82-a587-78132942be48 | -10.37464 | -44.88739 | 2025-12-17 03:38:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04c3c096-31fb-33af-9b8e-5e3cf3c2e3bf | -10.62163 | -40.51957 | 2025-12-17 03:38:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5b979e0c-3d8c-33f6-9512-08a31a43657b | -11.74952 | -43.30871 | 2025-12-17 03:38:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 482b76ef-6010-3c31-a25d-c189da215080 | -10.36967 | -44.88253 | 2025-12-17 03:38:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1a76f7f9-aa03-3188-9712-895f1c167e23 | -11.97086 | -44.49069 | 2025-12-17 03:38:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba0d1c56-f300-3ee0-95c6-de16a961c5f9 | -11.96762 | -44.49532 | 2025-12-17 03:38:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 495751fe-95e8-3ffe-87d7-15961a2fcb84 | -10.37537 | -44.88351 | 2025-12-17 03:38:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bd3157a-94bd-3e53-8018-4d071996d873 | -0.7077 | -51.9931 | 2025-12-17 03:40:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 42825b21-933f-3ac5-bbcf-52d292cb032c | -18.89438 | -41.05241 | 2025-12-17 03:40:00 | NOAA-21 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9e444a77-75be-38a9-9243-11028f5be720 | -17.00535 | -39.77758 | 2025-12-17 03:40:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a4fbc49d-43cb-3450-bd9e-89190582ff6e | -0.7077 | -51.9931 | 2025-12-17 03:50:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 32d5d74a-c6ca-31f3-9ffb-d457b1652694 | -0.7077 | -51.9931 | 2025-12-17 04:00:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 81ab42d3-3ba9-373c-b8b4-1f34f4e3db99 | -2.04981 | -45.453 | 2025-12-17 04:04:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eeec65e9-5ec8-3228-a1e8-d46ab93215d1 | -3.25704 | -41.42025 | 2025-12-17 04:04:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 309d6d92-df3a-3dd3-9535-92063d51a449 | -3.03581 | -45.3516 | 2025-12-17 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 333719cf-e95c-3574-b01b-7c1224d133b3 | -3.02828 | -41.12136 | 2025-12-17 04:04:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6d0136b8-b213-372e-85a2-87a2febfd6e5 | -3.35784 | -44.56682 | 2025-12-17 04:04:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20631a91-6f3d-3b05-8e2c-e19b2e1fd8f7 | -2.22954 | -51.94533 | 2025-12-17 04:04:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38462df9-b456-3631-bfd5-5fbf68be7d8b | -4.33417 | -39.15004 | 2025-12-17 04:04:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| feaddf9d-7ed7-32c9-ad1f-36574db6dd8a | -2.88707 | -45.4668 | 2025-12-17 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b211a23-1a9d-3146-ab9f-8cef8a0bdfda | -2.29957 | -46.14369 | 2025-12-17 04:04:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93d33de8-1eba-369d-a84f-265880fd940e | -3.03079 | -45.35501 | 2025-12-17 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8882b64-3606-387b-96ae-84e497b8ccad | -3.87319 | -40.45275 | 2025-12-17 04:04:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| acfbc10c-3a7a-3bc9-aaf8-83ecdf8dc18e | -3.2041 | -43.18753 | 2025-12-17 04:04:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 046c146b-96d3-364e-96e5-a675ee9d8430 | -2.23209 | -45.65904 | 2025-12-17 04:04:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8a71df2-20c5-3a1e-8e99-66c2115aaa7d | -1.42328 | -46.06313 | 2025-12-17 04:04:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a0ecc37-3ec3-35eb-84e3-1442557790b7 | -2.67534 | -44.94069 | 2025-12-17 04:04:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f3b656b4-354f-3e64-992e-5291fb132863 | -3.34535 | -41.79713 | 2025-12-17 04:04:00 | NPP-375D | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bfa165c0-108b-3e26-9a69-ff6ff340bc67 | -3.33833 | -41.79607 | 2025-12-17 04:04:00 | NPP-375D | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9f4194aa-989b-38ec-a521-63cb620f360e | -3.20007 | -43.18822 | 2025-12-17 04:04:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f6239d1-e53e-3216-92e0-d54dd965d4db | -2.84201 | -46.69418 | 2025-12-17 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e723863-7db2-3dd1-a5b0-d7571b6f8d8d | -3.42014 | -43.16669 | 2025-12-17 04:04:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e60d7ed2-6a24-3edb-9245-07bf5d0937ce | -3.35843 | -44.56317 | 2025-12-17 04:04:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59019c60-5e95-3e93-a178-7953a969e4cc | -3.87041 | -40.4487 | 2025-12-17 04:04:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 433cd1b6-f90f-3800-9f47-9fe842da6d26 | -2.90869 | -45.5844 | 2025-12-17 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 794ed4b1-3db2-3ea6-a3e2-cfbdecc1c28b | -2.92966 | -48.23084 | 2025-12-17 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58ceeedc-f4b7-38e1-9a59-a861db6d217d | -2.2285 | -51.95145 | 2025-12-17 04:04:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a45617d-b3f4-3eee-b90c-42f64067cf5b | -4.1293 | -38.18653 | 2025-12-17 04:04:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bd0c5f71-0990-3c93-8471-81cf4dc6f418 | -2.04607 | -45.44793 | 2025-12-17 04:04:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 614484cd-d128-377d-b2ca-bb53ec77472e | -3.49615 | -41.69053 | 2025-12-17 04:04:00 | NPP-375D | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 354905e1-0f62-3ac3-831c-e1de3ebb0be5 | -2.5689 | -45.32327 | 2025-12-17 04:04:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README5.md)
