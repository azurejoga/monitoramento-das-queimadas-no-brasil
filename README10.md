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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d564c2f-49cb-38e6-a761-5888806e4204 | -6.1011 | -42.46784 | 2025-10-29 03:53:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 24f4a414-a5f3-3d2a-9a49-a8a9efd8092d | -6.13353 | -41.83877 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a26249f3-0345-3715-b2fe-df2f8bca4935 | -8.54812 | -45.70697 | 2025-10-29 03:53:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fcbd616e-80d8-3fed-a578-21d436b56d08 | -5.85897 | -47.69365 | 2025-10-29 03:53:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47e4dde6-1eb1-369d-8689-6075f77436a2 | -6.29431 | -41.88495 | 2025-10-29 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d0ec416e-66ba-3932-a5f2-943f31370d9b | -7.4439 | -45.11599 | 2025-10-29 03:53:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5291e2f4-960a-3ea1-a4ef-d608017133f7 | -6.88097 | -42.84646 | 2025-10-29 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 6a29b0dd-faf0-3ae5-8be6-0bd920228cfc | -6.85894 | -43.44489 | 2025-10-29 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f1ff89a-b748-30e0-b754-17ea41d0cf96 | -7.79513 | -46.44294 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3a8bcfe5-5542-35d6-beee-8bb4aac50031 | -3.81285 | -48.65279 | 2025-10-29 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e0977ce-cd2c-350e-9f52-28409101b0f9 | -6.10572 | -42.46373 | 2025-10-29 03:53:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 60e5dbe0-584c-3d35-940d-d83f8295f022 | -7.06164 | -44.47321 | 2025-10-29 03:53:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0102da9-7fa4-3f3d-a866-3302d004c33a | -2.96262 | -48.59407 | 2025-10-29 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e27a06f-e6f3-3ee0-89aa-2126ef162893 | -4.14375 | -50.68507 | 2025-10-29 03:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7806574c-0a13-32f3-9d35-5c13e32b5adb | -3.15839 | -49.25264 | 2025-10-29 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0b48bbde-0590-33ab-9771-fa0ac85adc84 | -5.62676 | -44.94328 | 2025-10-29 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42d853ff-00ee-3862-95c9-6536eaac1ca1 | -6.14424 | -41.56336 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 95789ff3-5e3d-39c1-b6c1-d7cda3309ce5 | -8.18809 | -44.44563 | 2025-10-29 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fc5a80b-1829-311e-b03c-ac63158910a7 | -2.76678 | -45.39961 | 2025-10-29 03:53:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 722f0141-d3dc-32a3-868f-2407862ad71c | -2.43112 | -49.30134 | 2025-10-29 03:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 56298cf3-b4e4-33e0-8733-50d2a3f2ddbc | -5.06933 | -47.1117 | 2025-10-29 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51892cda-74f0-3b3f-8f36-4bbc38d51854 | -6.14366 | -41.68248 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 5ea50f6f-cec5-3b94-b943-a83dee6d99f2 | -5.06989 | -47.10852 | 2025-10-29 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 704dcc19-ccda-36d6-ab54-92c8ccabd0d6 | -6.18948 | -41.58431 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cc7730fb-ddb3-38dc-a20e-f7bbf5098ce3 | -4.64516 | -47.95618 | 2025-10-29 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27b0a036-d7df-3abf-8245-13a90aea137e | -7.95566 | -45.45266 | 2025-10-29 03:53:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bb30f53e-b44c-3c76-aa5f-a9c01782d0b8 | -3.4417 | -42.40837 | 2025-10-29 03:53:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c7d2786a-9611-3617-8afa-d550f2c01e24 | -6.97966 | -39.09465 | 2025-10-29 03:53:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7d007f9e-58af-3e59-8227-2268291806dd | -3.71213 | -41.56131 | 2025-10-29 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6338d749-c925-3465-a0c5-8ddf92cae1cb | -7.93336 | -45.49545 | 2025-10-29 03:53:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 414149fb-c14d-3784-922e-48e0d943b476 | -8.5542 | -45.7007 | 2025-10-29 03:53:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7f18bff7-a64f-3472-b6f1-2942d75247b7 | -4.92236 | -44.01579 | 2025-10-29 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a89d9043-5c86-3f5c-9f85-c0cd0fcc919c | -6.30425 | -44.69778 | 2025-10-29 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 043200cb-8a57-3b8e-90cb-be135071f280 | -2.42498 | -49.30976 | 2025-10-29 03:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 945c8894-f13c-3b17-8e88-42e9cac6925f | -5.33071 | -45.4307 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c7e8072-afc9-3d5f-a5fe-f88cbf18e3e9 | -5.05214 | -44.53944 | 2025-10-29 03:53:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a13f7298-2c03-3a03-9356-fc17ab3ec32e | -6.1254 | -41.84209 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 37.0 |
| 109512ce-3bae-3450-9e04-02a2a0ea84b8 | -6.10729 | -41.74381 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e2cfeac8-77f2-3431-b6d4-d3d0710c1986 | -4.6384 | -43.45524 | 2025-10-29 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10cc07c2-12c8-3f1d-879c-222685a05023 | -7.82304 | -40.59134 | 2025-10-29 03:53:00 | NOAA-21 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 576c8b49-91c6-38ea-8d7a-ca22ac86fe9e | -6.9725 | -39.11849 | 2025-10-29 03:53:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ad60b265-9d63-3ca5-aa7b-68e42209a045 | -6.67572 | -44.69289 | 2025-10-29 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab33610e-000e-3dd5-a383-4f37a4b5aecb | -5.51712 | -41.70757 | 2025-10-29 03:53:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8910c11f-6243-3f6c-b890-b6e4f47f44c3 | -3.10917 | -42.61253 | 2025-10-29 03:53:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d22f7807-7fa1-38a6-bcd3-a6898bb3256c | -7.0875 | -47.25531 | 2025-10-29 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b7abf76-d7de-3932-ae7c-4cc0467a09dc | -4.14954 | -43.36196 | 2025-10-29 03:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5290cd3-de01-3a21-a3ed-cf3a460c2893 | -6.12844 | -41.7067 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| c7014952-6a7b-36ec-839a-c90ec674dae7 | -7.81547 | -46.4129 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2e599f9-94e3-321a-8898-0ca22136b910 | -4.20948 | -50.08696 | 2025-10-29 03:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| f5927efb-9fba-32b9-9de2-ea14a81b20ec | -7.42854 | -41.85952 | 2025-10-29 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 79082f0b-c44d-3ae0-a65a-66bc0893b718 | -8.21714 | -43.80482 | 2025-10-29 03:53:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8940050e-d82a-38cc-bacf-5b86458e5359 | -4.54972 | -42.02579 | 2025-10-29 03:53:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 135dc2e8-67ad-3c79-a841-23f575862c1e | -6.17205 | -41.6697 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e162f95b-a014-3634-a764-e65d8b897d4d | -8.19587 | -44.45095 | 2025-10-29 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5f62361-b0cd-34b5-abb8-f157d018a39b | -5.49213 | -45.23607 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48f00e86-26ac-3b7c-af3a-2be61c03a3ba | -7.92903 | -45.49735 | 2025-10-29 03:53:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 97b863af-b367-36dd-bc30-2885caba95ce | -3.71817 | -41.57159 | 2025-10-29 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a961b1ff-86e8-3490-bceb-af6b6d0cc672 | -7.90225 | -45.67904 | 2025-10-29 03:53:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 78d46de2-7c82-37b5-b219-2e0fe7709db0 | -7.07754 | -44.93528 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1d9955fc-e6df-37c3-912b-8ac89ad7ca55 | -8.32407 | -46.15466 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e2ab2a26-a9ce-378d-9fee-b3a37ce28a12 | -7.92936 | -45.51908 | 2025-10-29 03:53:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b963332-a48a-3efc-a1c9-1a6f2c07e2db | -5.65309 | -41.14472 | 2025-10-29 03:53:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c6ca96f4-8679-3a85-bdc9-c3625d55a383 | -7.5995 | -43.57486 | 2025-10-29 03:53:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76b528e8-8083-39ff-a8f2-b34daf93c25c | -4.02259 | -42.8786 | 2025-10-29 03:53:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9f874f7b-418b-3bf6-a6bb-799907fe0836 | -7.85567 | -44.22917 | 2025-10-29 03:53:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b05186b8-b980-378c-b9e5-72d576452f89 | -7.41207 | -38.03247 | 2025-10-29 03:53:00 | NOAA-21 | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3cef7331-dd35-3608-a4ac-a4efff44f058 | -6.48976 | -42.2075 | 2025-10-29 03:53:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| abdb4f9c-1c00-3beb-8217-e0e38bc7a8a9 | -7.31201 | -45.68078 | 2025-10-29 03:53:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 465f17b5-0a99-3454-a473-bafcf8773370 | -6.14507 | -41.67379 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c103b9c7-3ec7-3aab-a745-a690140ebc2c | -7.79216 | -46.45967 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5cb4bc2a-fa50-3e74-8e81-ba4b0b93270b | -4.22007 | -44.24126 | 2025-10-29 03:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a20a8da-38d0-30dc-90ad-76de80bc3ef3 | -5.61346 | -45.18832 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6561d6b5-25b4-3e29-8c65-bd87e0f94963 | -5.57303 | -46.53274 | 2025-10-29 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ceef0562-89e9-314c-ab9e-8eacc4334d6b | -9.44969 | -40.38046 | 2025-10-29 03:53:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2e306290-6ece-34e9-a89e-3919c8d6955d | -7.74378 | -44.72372 | 2025-10-29 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 198f1ce5-c31f-3fb2-b2ad-da79ab26ce18 | -7.28109 | -46.89642 | 2025-10-29 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8d4e5017-2199-37b3-901f-76e6e08d346d | -7.28158 | -46.89363 | 2025-10-29 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0752cdc7-cdff-383f-96d0-42926910e6f1 | -7.066 | -44.47364 | 2025-10-29 03:53:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97f6b377-13a3-3f9a-928f-a3f794f39630 | -4.00465 | -49.0355 | 2025-10-29 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ee8eeee-85ce-32d7-9fc7-6ee46c077453 | -6.64083 | -44.60424 | 2025-10-29 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d56bbce-8d0c-3a9b-9538-f2990218a1f9 | -8.00337 | -46.21378 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e6865e68-99ec-3a99-87cd-b0620f97540c | -3.58224 | -41.04493 | 2025-10-29 03:53:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c91fd97c-d4f5-386b-a989-1d51e2911625 | -7.68033 | -38.66636 | 2025-10-29 03:53:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e5f2e01b-44fe-3177-8873-56b3367dfffc | -6.29873 | -41.88118 | 2025-10-29 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 88c6f7a9-1eac-386e-8d34-0cdf50fc9a7d | -6.16109 | -41.66772 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f080850a-edb0-3294-8074-ee4aefccf831 | -3.66276 | -44.19519 | 2025-10-29 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c20eb102-7b65-300a-9384-9caa9c7b63ff | -3.72569 | -41.57284 | 2025-10-29 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 40e289e3-3268-3b71-acc9-881c1a896bb2 | -2.42473 | -49.30027 | 2025-10-29 03:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 482549e3-fbac-351b-a963-c483a69be604 | -8.54678 | -45.68955 | 2025-10-29 03:53:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 417ad251-7fe2-3f31-b9a0-5546083d5563 | -7.08564 | -44.94134 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 17849927-78c0-3068-bc62-22ff5f25a76d | -6.54214 | -43.56506 | 2025-10-29 03:53:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 473708bd-a73f-3496-9f7e-beb3d46bccf4 | -6.63046 | -42.22449 | 2025-10-29 03:53:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8f6cbef3-c2a4-3617-8c42-78584568209e | -7.61195 | -43.59883 | 2025-10-29 03:53:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c71edef9-e44d-3f43-a212-de98a11a4ac0 | -7.30576 | -46.31506 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 617e395d-188d-3e19-929c-a3fc72afce0c | -7.8145 | -46.41837 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7dfc319c-dce1-352f-ab25-5e2fc0c7a2bf | -7.12773 | -46.98505 | 2025-10-29 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 667dcc06-be4b-34bd-b6b2-88294af558db | -8.0396 | -47.40836 | 2025-10-29 03:53:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9c9add2-ffbb-3981-a075-550714b134ae | -5.16706 | -46.16192 | 2025-10-29 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bf1f5311-d5da-3c25-a0b2-b6e1abefea93 | -6.14725 | -41.83952 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ad22f1e0-b4cd-378d-a8cc-56cfac1373a7 | -6.15601 | -41.67594 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |


[Clique aqui para ver as próximas entradas](README11.md)
