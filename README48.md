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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b88f06bf-cada-3f24-a4ba-23c5ac0784f0 | -15.1872 | -46.23683 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d377de7-7a24-3988-a19d-c91a57825ec8 | -15.18068 | -46.24553 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 007b365f-2264-3075-a880-25164d9ea55c | -15.17974 | -46.25055 | 2024-10-01 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75a8146d-6029-30f9-81bf-243f64ff79df | -14.77778 | -48.07548 | 2024-10-01 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fabe8f5-bb40-3ebb-b488-2a17baba7ff8 | -14.77699 | -48.07941 | 2024-10-01 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f365a14-4447-3b6d-9abb-4eea08de36da | -14.77234 | -48.075 | 2024-10-01 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f88c100a-3b1e-3806-a2fd-00bc88557429 | -14.77154 | -48.07895 | 2024-10-01 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34e41bfd-3416-3b8d-bc6b-1f8b9454d702 | -14.77071 | -48.0831 | 2024-10-01 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc474357-4e84-3452-a39f-90ca4f867583 | -14.76453 | -48.08628 | 2024-10-01 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 964f3400-9415-388f-b6c1-c092bf9025b1 | -7.53344 | -35.20678 | 2024-10-01 03:49:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4fbbf51c-3087-325c-8cb0-970318bc9eb0 | -7.5333 | -35.20613 | 2024-10-01 03:49:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6b40313f-945c-306d-a1cd-501faa152cf2 | -7.33338 | -35.19196 | 2024-10-01 03:49:00 | NPP-375D | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c0867d81-075a-3189-ace0-744cc1089801 | -6.09039 | -35.10953 | 2024-10-01 03:49:00 | NPP-375D | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 385d73e3-9201-356e-9a87-0b971de9a10c | -18.53423 | -42.65735 | 2024-10-01 03:49:00 | NPP-375D | CANTAGALO | MINAS GERAIS | Brasil | 3112059 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2b19eeed-d448-3463-99ac-c3289722b26a | -18.34323 | -42.76601 | 2024-10-01 03:49:00 | NPP-375D | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c3b8e74b-4888-3a53-83ae-ceab47256eba | -18.04068 | -39.92498 | 2024-10-01 03:49:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a18540f0-c14c-34a2-ac12-578a9ee211a0 | -18.00371 | -40.33692 | 2024-10-01 03:49:00 | NPP-375D | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 14d8a9fc-8336-370f-baca-c28f8f909d47 | -17.20304 | -39.50929 | 2024-10-01 03:49:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bb687fb6-93d3-339c-94af-46f593419dff | -17.20246 | -39.51291 | 2024-10-01 03:49:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 78c55e64-e40c-3e22-be85-57afe13af988 | -16.95133 | -40.76089 | 2024-10-01 03:49:00 | NPP-375D | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 502e9f4e-5e57-3c54-b5d9-8eabee30b315 | -16.49725 | -41.44126 | 2024-10-01 03:49:00 | NPP-375D | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f00e7f3c-c724-3b3e-8da9-37034fb71c5e | -16.49627 | -41.4423 | 2024-10-01 03:49:00 | NPP-375D | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 131a3229-949a-3a8b-b1de-0a9cc5cacb13 | -15.9135 | -42.67129 | 2024-10-01 03:49:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f6a6360e-4f42-3842-bb49-f197132c890b | -15.9098 | -42.67056 | 2024-10-01 03:49:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b190c916-9df7-324b-8fbe-5d39ca85d005 | -9.58639 | -50.12459 | 2024-10-01 03:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 788a5b29-6fdc-3392-9a4a-27f955fbe437 | -9.5798 | -50.12318 | 2024-10-01 03:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f6ae8b6-56bc-34d7-a612-1aec2bdf6c32 | -9.5732 | -50.12184 | 2024-10-01 03:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10a14982-70e2-39cc-b17d-22395cac46ba | -6.25038 | -44.14725 | 2024-10-01 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a4df1ed0-c1d4-3621-8ac0-8ff2b69d6f76 | -6.24949 | -44.15247 | 2024-10-01 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 34650809-3794-33ce-9105-81cfc580cbde | -6.24649 | -44.14133 | 2024-10-01 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ea722028-f50f-3ba0-a24c-728b1c44fa3e | -6.24562 | -44.1464 | 2024-10-01 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b39ce594-297f-3ab0-b6e2-5fc55e21c8d6 | -6.2447 | -44.15177 | 2024-10-01 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 67b977d5-d4a7-3567-9961-54511d2c14d4 | -6.24255 | -44.13568 | 2024-10-01 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 78ecc59a-f84a-3d0e-b737-fd3da5d7ef4c | -6.24169 | -44.14069 | 2024-10-01 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0cd14808-093e-37dc-8993-14dbfe55cd65 | -6.09793 | -44.70928 | 2024-10-01 03:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 154fe1be-7518-3b29-aa9f-158875a45348 | -6.09768 | -44.71003 | 2024-10-01 03:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7d63bc1-0dc4-39f1-9f2a-48597861c57b | -6.09057 | -44.30807 | 2024-10-01 03:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b08c71d-29ee-386a-abfc-58bccd8c6a3e | -5.98623 | -45.37179 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9aa0b309-c819-313b-944e-021c5cdb5dd9 | -5.98162 | -45.36781 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b20038aa-070a-3587-98b6-fe43741fff12 | -5.98157 | -45.3678 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5ec2335c-17cd-3b06-af5c-14deb29f3ee1 | -5.98109 | -45.37095 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c0d8f126-8e1a-3ac6-925f-dd125ae459c6 | -5.98101 | -45.37094 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a870104e-8480-37f8-ad9b-24c0dc348e63 | -5.98056 | -45.3741 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4de01c1c-460d-3aeb-b072-edb540f7a777 | -5.98045 | -45.37408 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e8afab08-227e-3d38-bf03-95b191951be3 | -5.98002 | -45.37726 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e142bd43-5425-3ed4-931d-a99cb5b04b79 | -5.97989 | -45.37724 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 05476056-6fb0-3732-9fca-e7477c07cb57 | -5.97949 | -45.38044 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 046bb541-e14f-3cc9-b235-39e5615ddd6f | -5.97933 | -45.38042 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f3805869-61ce-3542-b161-14a46f232112 | -5.97587 | -45.37015 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 19cd3671-0638-3c4a-b298-8c5660f37058 | -5.97578 | -45.37015 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0b7914a8-ac4e-380d-bdca-e54a395f43c1 | -5.97533 | -45.3733 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 861b360f-d3e2-3818-9a8e-dd73505500d1 | -5.97523 | -45.37329 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9ae37050-a215-3482-9e97-951362b2b6f8 | -5.9748 | -45.37645 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3a1f3ea4-f49a-36ad-bafb-1cfe0701eb3d | -5.97467 | -45.37644 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ffd853d5-d02b-34cf-afcf-7b673870d50c | -5.97426 | -45.3796 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 89b641fb-6e86-3ef0-b226-cc46d697f90b | -5.97411 | -45.37959 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| edf95c5c-b8f4-31f8-818a-36a30b01ba94 | -5.97372 | -45.38278 | 2024-10-01 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 568fad8d-59d7-31ea-9db5-7cee2ceb19df | -4.57895 | -48.00949 | 2024-10-01 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f75ded94-ec92-3476-81bd-e931021e7adf | -4.57806 | -48.01452 | 2024-10-01 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 17d6a095-3c2d-318f-9653-af56ea5801ea | -4.46686 | -48.11365 | 2024-10-01 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f515e855-9422-3d8b-b3db-c689ec84a135 | -4.46595 | -48.11881 | 2024-10-01 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 72349f0d-d269-3f48-b816-0e29bf4d1f83 | -4.45956 | -48.11787 | 2024-10-01 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9abdbeec-08b1-3352-a4f5-77a4a162ce79 | -4.152 | -48.39668 | 2024-10-01 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f40e93e7-cc83-3cfe-be47-db6c48576590 | -4.15098 | -48.40262 | 2024-10-01 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10c3b15e-0d68-39f7-bdf2-b66fd86320da | -4.15075 | -48.39662 | 2024-10-01 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a905df30-dc0a-333c-9fad-09fb35e17180 | -4.1497 | -48.40249 | 2024-10-01 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e7c3956-9310-355f-97b5-a228bea30304 | -4.14455 | -48.40102 | 2024-10-01 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7440c262-e09f-3ebf-86b9-074b40cb8b74 | -4.1436 | -48.40655 | 2024-10-01 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 758c5283-df16-37c4-960b-f29b44d3f8b8 | -4.14326 | -48.40098 | 2024-10-01 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d253cf2c-d874-3c84-8f93-519777b2c289 | -4.14228 | -48.40646 | 2024-10-01 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3483ecf-7de2-3e71-bc6e-4c6356da068e | -13.79304 | -52.70852 | 2024-10-01 03:49:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35175b70-824f-363d-a542-76e95731042d | -13.79154 | -52.70549 | 2024-10-01 03:49:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2693c5e-8b43-3aeb-b407-ff771f1ae640 | -13.64617 | -51.10936 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 39cc72d7-7548-368b-a766-978a93db2a90 | -13.64086 | -51.10217 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34b1f941-b2e5-38d1-a266-d18990e8668b | -13.64069 | -51.16784 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c51549f7-bef3-3518-98c0-596e16bb0e19 | -13.63966 | -51.10785 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d4975861-c9c4-375d-b563-f553c8afcd16 | -13.63884 | -51.16455 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 701e684f-b71a-3b10-b2de-31703959702a | -13.6376 | -51.17023 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1231fdf8-5b6e-38e1-bccc-8c6505e529f5 | -13.63637 | -51.17592 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de3ed9cc-81bd-39cd-b589-c44d441eca6f | -13.63536 | -51.16063 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 77f1dfbc-d417-3de0-b196-a2cd393fa96d | -13.63512 | -51.18164 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8385ae5a-f96d-3fdd-b006-c5ccf99e031a | -13.63416 | -51.16633 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6fb139ef-f60b-3fb5-a826-4c78dc4f05fe | -13.63315 | -51.10637 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 8ca0a9e3-fc41-3f49-a0f3-3044d3aaba50 | -13.63295 | -51.17204 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fc81de55-4b20-3ac9-9b1b-912ca137068e | -13.63195 | -51.11205 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 1526cd68-7300-36fc-abe0-9a1456d2f0d3 | -13.63175 | -51.17775 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7e308061-8118-3b08-bde8-afd411eb8562 | -13.63054 | -51.18347 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ffa2a4f7-063f-3ba0-90bb-3fbccec5bf23 | -13.63004 | -51.1534 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 15638da9-5eba-3b7d-bd24-58b92435aab0 | -13.62883 | -51.15912 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ea01ca66-1d5b-3e15-ba0d-9cc2b95de249 | -13.62785 | -51.09919 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 48dd0389-ef69-3220-8abd-0eeacf007145 | -13.62762 | -51.16483 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1166fbae-9949-39a4-b65a-2811787a8fea | -13.62664 | -51.10488 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 2d91301e-b353-3925-8f16-f569141c03f7 | -13.62642 | -51.17053 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5aabfed8-37b9-33af-adcf-257b0e3af87d | -13.62544 | -51.11056 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 48be25b2-6b39-3c85-886b-97e484373328 | -13.62423 | -51.11624 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 6e9721e7-5d32-34fc-bee8-f87b51ceacd2 | -13.62351 | -51.15192 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 79988c81-0907-3a60-859b-0178f9060676 | -13.62255 | -51.09203 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.7 |
| d9e49519-faff-354d-9053-63355c0ac9db | -13.62134 | -51.09772 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.7 |
| eb8a6f64-bed7-3670-8acd-e3606072849a | -13.62013 | -51.10339 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 86b921d5-3fbe-30e5-9433-e01864640cd8 | -13.61893 | -51.10907 | 2024-10-01 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |


[Clique aqui para ver as próximas entradas](README49.md)
