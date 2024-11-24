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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99dce6a3-3252-3469-b223-db598fbad5a5 | -5.10364 | -43.15442 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d3d06483-421a-3a55-b24d-caa4bc8351d4 | -4.23775 | -48.70329 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d21d5381-79ea-3393-9000-0c13f7374989 | -5.06675 | -42.57061 | 2024-11-24 03:57:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 14ee1a1b-20a5-3067-bdc1-8b98afebad4f | -3.08327 | -40.05429 | 2024-11-24 03:57:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c005acb2-2e79-3c17-9ae1-7d5030d94e9c | -4.99809 | -42.94946 | 2024-11-24 03:57:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 08631694-775d-39c5-93ce-938bf662d739 | -3.4345 | -50.02288 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3de75c4a-53d5-33d6-bf11-fccc6813746a | -3.48165 | -50.08741 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d20bb4a-b3e7-3f39-bf9b-6e555c97bc1e | -2.21258 | -46.39126 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 60b3b231-2b2f-3a18-9739-3f3bc0b19636 | -2.71084 | -46.28473 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a920026c-81d9-3d58-b196-14d03d421abd | -4.11638 | -49.4442 | 2024-11-24 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19e71a5e-28c2-3177-b1a4-5d9105ca22ca | -4.35181 | -45.28079 | 2024-11-24 03:57:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e084eaeb-7d71-3ee1-b65c-b49b900f148f | -7.82141 | -44.18938 | 2024-11-24 03:59:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8291b870-3263-36b4-9030-9cd0771a8b59 | -7.57494 | -49.40827 | 2024-11-24 03:59:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8c793f9-f960-3048-8979-b14c488dd845 | -7.69152 | -42.98339 | 2024-11-24 03:59:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 887364df-c45c-38a8-b6b0-0397858eba8f | -7.6893 | -42.97477 | 2024-11-24 03:59:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 41c96117-effc-37dd-89a8-3af4fab96e72 | -7.74774 | -38.452 | 2024-11-24 03:59:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8910c057-506b-3ac9-992e-54ed4160814e | -7.56485 | -49.40308 | 2024-11-24 03:59:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48a8d2a1-9b72-3eb0-83ec-b1edd87d71a1 | -7.75576 | -46.21856 | 2024-11-24 03:59:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fa7b43c-4e0a-3565-a757-30cf4aa0c60c | -9.8098 | -48.16955 | 2024-11-24 03:59:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa0ae807-8255-346c-ae78-016f8896cf91 | -6.98971 | -46.31926 | 2024-11-24 03:59:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 284e5a42-6dc3-3b3c-9462-eb6913178ba5 | -10.18173 | -52.58255 | 2024-11-24 03:59:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9400036c-f381-36df-bd1a-439168a458c1 | -7.68863 | -42.97879 | 2024-11-24 03:59:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e97d510f-de6b-3383-aa5a-c996a77286e1 | -9.31936 | -40.72984 | 2024-11-24 03:59:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f1a999cc-9d79-3195-846a-433df17ade6c | -7.81764 | -44.18874 | 2024-11-24 03:59:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e7c4f84-9234-3770-aa6e-49de97ce1662 | -8.05214 | -47.0886 | 2024-11-24 03:59:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74a7d712-f6bf-3011-8d8f-124b4f758447 | -7.57436 | -49.41151 | 2024-11-24 03:59:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6dfa3cc-3c0a-3df1-9d4e-8d68152505bc | -7.67982 | -49.12436 | 2024-11-24 03:59:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f5bf212-ec3e-34a2-99e8-edad05f666bb | -7.56426 | -49.40639 | 2024-11-24 03:59:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c73e4e2e-22b3-3480-afa7-2a60d72d68e6 | -8.82746 | -35.67172 | 2024-11-24 03:59:00 | NOAA-20 | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bb052aeb-c31d-39cc-a1b4-f55b7107e193 | -7.75773 | -46.2207 | 2024-11-24 03:59:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b71ea232-1902-3442-a420-65aa6bb12dc5 | -6.84188 | -44.388 | 2024-11-24 03:59:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 92f52117-f86c-3bfa-beda-81d3b9755afa | -7.82064 | -44.19395 | 2024-11-24 03:59:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a4d4c5f-ff73-37ac-8a76-5962bf510999 | -8.50665 | -40.69249 | 2024-11-24 03:59:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a6cc7875-9725-3ccf-9936-bfd9fbf5a954 | -8.05161 | -47.0862 | 2024-11-24 03:59:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5075081f-a617-327f-b0bc-f51f8daf00e4 | -6.63647 | -47.34666 | 2024-11-24 03:59:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3418e5f0-d8a7-3835-a07a-df2df575f7b6 | -8.50996 | -40.69302 | 2024-11-24 03:59:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d2b8de41-2cc0-37eb-85a7-3bedfd52a23b | -7.32099 | -45.47377 | 2024-11-24 03:59:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07265337-a082-3aeb-81d2-3658c473bd95 | -7.32036 | -45.4775 | 2024-11-24 03:59:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 611be4bf-3866-3199-a14b-9c3f4e55f8b5 | -7.64326 | -38.33434 | 2024-11-24 03:59:00 | NOAA-20 | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| db21fdd3-3632-38b7-bfb6-b6bd9f11f297 | -7.69085 | -42.98742 | 2024-11-24 03:59:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2ca4ce92-52aa-31a3-91e0-ceb1288ce8ea | -8.3068 | -35.27975 | 2024-11-24 03:59:00 | NOAA-20 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 94aacf43-23c0-3c9f-a92f-5a4a9ca2d1a9 | -8.89855 | -44.2258 | 2024-11-24 03:59:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c636dc60-fa0b-391e-b819-e8cff183f89e | -6.49628 | -47.04292 | 2024-11-24 03:59:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efdc5619-e184-3ab1-88d7-b6cef14c99ea | -7.71375 | -45.66875 | 2024-11-24 03:59:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d1acd17-6c6d-3a56-884e-c990ec01b5ed | -8.04759 | -47.08793 | 2024-11-24 03:59:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fdab47f-80ab-312d-bb16-f03ef72ea7ca | -8.37601 | -35.80481 | 2024-11-24 03:59:00 | NOAA-20 | CAMOCIM DE SÃO FÉLIX | PERNAMBUCO | Brasil | 2603504 | 26 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 96c90965-689d-3373-8346-2b86fd570840 | -7.57945 | -44.59725 | 2024-11-24 03:59:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24220765-e987-317c-98d1-d0a7339953b7 | -7.71312 | -45.67253 | 2024-11-24 03:59:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbf24e25-8f82-30d3-8b7e-78cd96ad9edf | -8.21937 | -37.38311 | 2024-11-24 03:59:00 | NOAA-20 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4791b080-16d4-3f12-8c53-936ef90e9502 | -6.83802 | -44.3873 | 2024-11-24 03:59:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 20baf896-0ac4-325f-8891-4418738b66de | -7.68041 | -49.12115 | 2024-11-24 03:59:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 155e01c0-377b-3ca1-afbc-c5b9eb237ed0 | -8.10082 | -35.20985 | 2024-11-24 03:59:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0ba8185c-3107-3cd2-9333-75a9d3430085 | -11.50748 | -48.12897 | 2024-11-24 03:59:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 166551dc-efad-3280-b23e-8bcd16c686f6 | -7.5696 | -49.40733 | 2024-11-24 03:59:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cca63633-bdf7-3c36-ac4b-88d8268cbcb4 | -7.74533 | -38.69403 | 2024-11-24 03:59:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d569eb35-aba0-3b6f-9038-3fe4571d5a74 | -8.73916 | -35.53513 | 2024-11-24 03:59:00 | NOAA-20 | ÁGUA PRETA | PERNAMBUCO | Brasil | 2600401 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0cb3cee9-2f69-32fe-b688-82dc9c1d0c04 | -8.35853 | -44.60152 | 2024-11-24 03:59:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2878b4f2-7ac1-36c5-94fc-4aa113deb741 | -8.93572 | -44.25543 | 2024-11-24 03:59:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d558b42-b314-399b-89cb-fddee5322d08 | -8.93647 | -44.25089 | 2024-11-24 03:59:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2db06b19-7316-3a90-8be6-781dc9d83473 | -6.63557 | -47.35182 | 2024-11-24 03:59:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 61a34bae-9ce2-38b6-9a76-770b24cf972a | -7.75937 | -46.22337 | 2024-11-24 03:59:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 022b51e6-8661-3e71-8294-9ec2ad511b1d | -8.1428 | -34.97138 | 2024-11-24 03:59:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 59f99de2-f609-3b66-a30f-9aeffa0cc30e | -8.05078 | -47.09111 | 2024-11-24 03:59:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3e4eb43-1edc-3151-8d6a-ac1d124aaff7 | -8.92902 | -44.24965 | 2024-11-24 03:59:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b246b865-db3c-3a86-a674-61191c689905 | -7.68797 | -42.98281 | 2024-11-24 03:59:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| eb5607ed-c795-31e4-a4a3-1ccd49faacbc | -3.0355 | -49.4476 | 2024-11-24 04:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| e4db1cb3-8eab-348f-a207-ca3a97e76652 | -5.0998 | -43.151 | 2024-11-24 04:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 3bdcfe7a-205b-3d5a-af2b-953054bfe40d | -4.242 | -48.6978 | 2024-11-24 04:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| f360a07f-adda-36c6-abfe-80db762cbe60 | -17.7561 | -52.44186 | 2024-11-24 04:01:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bf4d74c-5a19-34c8-b4c3-f33436c00876 | -17.75688 | -52.43807 | 2024-11-24 04:01:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59e9e5bb-0f15-3d6a-a85b-c4d6b7a7ea8d | -18.86214 | -47.64173 | 2024-11-24 04:01:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73b561bd-a791-357f-ad69-ca7b2c8ca7a2 | -17.75153 | -52.43667 | 2024-11-24 04:01:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d124cf33-d7b1-3571-a84c-8c99860a6231 | -20.34955 | -40.36143 | 2024-11-24 04:01:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0b3efa83-5370-3936-b5dd-deb55dfd2f6e | -23.46834 | -47.51583 | 2024-11-24 04:04:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9bbb247d-16f9-3b5a-a190-22ce0ca50bfc | -20.22836 | -55.97085 | 2024-11-24 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 336339e0-2446-33cb-82bd-39c602c17d6c | -20.32019 | -48.81919 | 2024-11-24 04:04:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4d8d5c0d-315d-3c32-a234-5a941894ed0a | -23.45645 | -51.06726 | 2024-11-24 04:04:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8d366390-5190-3565-90c1-d14071a364a6 | -21.12093 | -50.59012 | 2024-11-24 04:04:00 | NOAA-20 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 03da8e5c-6f67-330c-9d10-699bf2715425 | -22.5403 | -48.81512 | 2024-11-24 04:04:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc6edfa5-2a60-3d8b-8b58-16ae12d74ec8 | -20.23003 | -55.97154 | 2024-11-24 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9ffbcbae-8cae-3bf5-bbac-81cff9076eb5 | -23.00641 | -46.59848 | 2024-11-24 04:04:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1fcbcb2e-6530-3d6d-a9cb-3367470e57a4 | -21.3199 | -55.95376 | 2024-11-24 04:04:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cc2fcdb-4fcf-3159-b299-2f39e7cbd7ef | -20.2211 | -55.98082 | 2024-11-24 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a7647a6b-8225-3777-a4df-b28e255bdb82 | -23.3388 | -46.77523 | 2024-11-24 04:04:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8fbda1df-b918-338e-aa93-f4ddcbf55efa | -20.2261 | -55.98794 | 2024-11-24 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5be2d32e-e6af-369f-bbe1-c0caa9843171 | -20.31945 | -48.82311 | 2024-11-24 04:04:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0d62b41-8c4a-3eb0-a318-f9449c8af4da | -20.76208 | -46.76873 | 2024-11-24 04:04:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 77c16a58-8096-3b91-ae9c-4fae18f2cc0c | -23.40652 | -46.55647 | 2024-11-24 04:04:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9cdbd4d4-1f26-3a7b-b46d-a27bd759b9f9 | -23.46752 | -47.52036 | 2024-11-24 04:04:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 98bfb2e6-8175-3368-8719-2b8ad3bcbe04 | -21.11645 | -50.58901 | 2024-11-24 04:04:00 | NOAA-20 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| eae0e612-f520-325b-b345-4606cac682cb | -23.58972 | -47.2426 | 2024-11-24 04:04:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 338d5dbf-15d8-32ce-8873-8687878aefc7 | -22.92103 | -45.41375 | 2024-11-24 04:04:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d5f78409-070b-3187-bf55-42e40b291080 | -22.81649 | -46.47852 | 2024-11-24 04:04:00 | NOAA-20 | PEDRA BELA | SÃO PAULO | Brasil | 3536802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 60502893-b913-3c5f-8a23-6f65ba66eba4 | -23.80702 | -48.15673 | 2024-11-24 04:04:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4705c3bc-c76d-3bdd-905d-d7bfa48b567e | -23.00568 | -46.60274 | 2024-11-24 04:04:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 96befe1d-dcc6-366b-ad41-566acefe7022 | -22.05552 | -47.10764 | 2024-11-24 04:04:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbef5077-3234-3f12-b40d-5de7ce9c7866 | -23.33959 | -46.77272 | 2024-11-24 04:04:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3376d78f-1e50-319a-8b4e-186b585e4dcd | -20.2258 | -55.98183 | 2024-11-24 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 43869488-2a99-3709-83eb-5370e32648d3 | -20.22453 | -55.9873 | 2024-11-24 04:04:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d9acffaa-3b34-3d46-9217-cc7de907e866 | -22.92012 | -45.4152 | 2024-11-24 04:04:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README36.md)
