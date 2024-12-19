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
| 747d2c62-227b-3f8a-8537-7d43562f2ff0 | -3.78402 | -44.06773 | 2024-12-19 04:29:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0490cdaf-c300-3e38-aae1-c4158144f9d1 | -2.87552 | -45.24654 | 2024-12-19 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c77fd6e7-c84e-30b0-828b-9b08cf1713d1 | -3.16653 | -45.97853 | 2024-12-19 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d72b869-fa8e-3896-b728-02eb18137a66 | -4.99661 | -48.27052 | 2024-12-19 04:29:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76d577da-3393-39ea-a0ca-aed972849f04 | -6.07348 | -46.125 | 2024-12-19 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4af3ea04-0ad6-3557-bced-4fdb46006906 | -4.03666 | -49.76652 | 2024-12-19 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ac1d7a3-bb61-3350-b821-f28368eb53b7 | -3.39662 | -41.64095 | 2024-12-19 04:29:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2fe49e10-79c4-3d3d-8568-2b3a046286ea | -2.7009 | -46.15352 | 2024-12-19 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c941a001-d814-3b49-bfdd-023cbae33dbd | -3.01337 | -44.39576 | 2024-12-19 04:29:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca0495c7-f70d-3f23-8473-6bca85bbcaba | -3.16708 | -45.97502 | 2024-12-19 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cadaf64a-6257-3e3d-83d1-eba944866aed | -9.67427 | -36.20401 | 2024-12-19 04:29:00 | NOAA-20 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| aa146293-c0c0-3553-ab44-9aae3138accb | -3.20985 | -42.69779 | 2024-12-19 04:29:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd8b90ef-faf4-38a5-b98d-214a1f6e8afa | -9.35418 | -37.96629 | 2024-12-19 04:29:00 | NOAA-20 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3ac1ab40-e941-3866-b462-274555738aa3 | -4.45788 | -45.52256 | 2024-12-19 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d440919-012a-36c6-80ed-5464ba1a16a8 | -6.2104 | -39.4011 | 2024-12-19 04:29:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eadd5a7f-a117-3fbb-b481-2f2daa64f1e9 | -4.32589 | -48.30188 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61c31ea2-ce4e-3783-9e4e-89e4e030f75a | -4.88492 | -41.39698 | 2024-12-19 04:29:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bd34ee69-12dd-3cf3-baee-026dcedcbb5b | -5.30552 | -46.06307 | 2024-12-19 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6916932-ebad-353a-bc03-020480632c96 | -4.25567 | -43.45158 | 2024-12-19 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46acd893-11af-38f9-8dbb-a5f5092d7d41 | -4.77702 | -46.44694 | 2024-12-19 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ec712a2-4933-3d9d-9c49-535761763ca0 | -9.68147 | -36.19919 | 2024-12-19 04:29:00 | NOAA-20 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| ca3a1a77-bfcb-38be-a246-37c8f8dccc91 | -2.70085 | -46.13214 | 2024-12-19 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32456bce-6eb2-30fc-979a-fe703cede891 | -3.22159 | -42.07545 | 2024-12-19 04:29:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b5c0688-9796-3566-92e7-aa7b6ff2b829 | -5.33769 | -37.44994 | 2024-12-19 04:29:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.3 |
| f7de26ba-ad0a-3b3b-8cd6-cb9ab9f7aa9b | -4.67343 | -43.29775 | 2024-12-19 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1af878ff-ee1d-3fee-b738-655677a824af | -4.17727 | -48.76028 | 2024-12-19 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0186ac05-090d-3154-819f-fed80136572f | -1.26859 | -54.14083 | 2024-12-19 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef11908b-becf-31a3-bd5f-4007374d1807 | -2.5994 | -45.64918 | 2024-12-19 04:29:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 983ab759-64b6-3352-8698-ba02a1bdca4c | -9.35365 | -37.97039 | 2024-12-19 04:29:00 | NOAA-20 | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1128753a-6eba-3cea-bf3d-21ab543ceb69 | -4.99947 | -48.27131 | 2024-12-19 04:29:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 743217e3-1bf5-379c-bb51-dffe484d2697 | -9.67561 | -36.19296 | 2024-12-19 04:29:00 | NOAA-20 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| bd3bd191-b134-39fd-9108-22df7906aa1b | -3.85148 | -40.45278 | 2024-12-19 04:29:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6ccbe688-faa7-3278-97b2-371d8f59b9c8 | -3.68305 | -43.7537 | 2024-12-19 04:29:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5325d5df-a36e-3b0d-aaed-cbf0ee67cbc6 | -4.04368 | -49.76765 | 2024-12-19 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e8abf9e-a896-3da2-8651-07e7d5454c03 | -5.21482 | -43.30051 | 2024-12-19 04:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 77393dd1-553f-3eab-84dc-e956706953ae | -4.47974 | -48.12094 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 576b12f4-4f15-38df-94be-04e22dcf6719 | -7.7854 | -34.99147 | 2024-12-19 04:29:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1b286b42-cf8f-3670-b642-dda7ed7ee2aa | -4.35307 | -48.19463 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 535db41c-f24a-39d7-92e6-cc287da449b7 | -2.64482 | -45.75402 | 2024-12-19 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc2b0a64-1de8-3557-979f-2714186aa2e9 | -2.64426 | -45.75755 | 2024-12-19 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f786777b-d05b-326b-aedd-72fc14fc9606 | -4.79644 | -44.02772 | 2024-12-19 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10d41403-e4e3-3bb7-9b3e-8abbf9d25dd4 | -4.88435 | -41.40085 | 2024-12-19 04:29:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3620b295-8420-3f5e-8e2f-57691c892cf1 | -3.01689 | -44.3963 | 2024-12-19 04:29:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00f0a5f7-32ee-3985-8357-74cd121851b8 | -3.2278 | -45.49997 | 2024-12-19 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 23.3 |
| b04124c0-69d3-3c02-b7a7-c2e5c1e97456 | -1.69198 | -54.01363 | 2024-12-19 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 945666e3-9855-3313-b29b-cd61825c2116 | -4.66626 | -42.71967 | 2024-12-19 04:29:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7effaded-f311-3b74-9cab-e48a54bf79fb | -4.10087 | -42.85677 | 2024-12-19 04:29:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51c88ed6-d09e-3a54-ae9b-5e70474de0bc | -6.14948 | -38.21828 | 2024-12-19 04:29:00 | NOAA-20 | PAU DOS FERROS | RIO GRANDE DO NORTE | Brasil | 2409407 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fb772fda-50b4-37a3-aa21-7e6fd6de2ed2 | -1.69484 | -54.01668 | 2024-12-19 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0999a077-ef99-3d61-9601-b2c0a0ec08c4 | -4.32978 | -48.29888 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 14a19788-be83-3e76-813f-79821eb9e777 | -3.22442 | -45.49946 | 2024-12-19 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25b0790a-79bc-3644-bb40-7012bb01378c | -5.21101 | -43.2999 | 2024-12-19 04:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 62ec672b-72f9-3ff4-8eca-d0287a10bce8 | -3.4286 | -41.94789 | 2024-12-19 04:29:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 13d9ecc0-de3d-346a-962d-8c9cbe8cb541 | -3.23118 | -45.50049 | 2024-12-19 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 23.3 |
| e686a4b1-8355-3ee7-bfa9-a6082982ddc8 | -6.67898 | -41.03693 | 2024-12-19 04:29:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fb4aec63-b362-3e47-82fe-a30c7d17c366 | -3.98775 | -48.40071 | 2024-12-19 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec866b6c-291c-372f-aab7-4305aba9d614 | -4.88866 | -41.4015 | 2024-12-19 04:29:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| df5e927f-6b1f-3099-b2c6-cd216e8a497e | -4.03522 | -46.06964 | 2024-12-19 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5ec9c5c-b890-3a9c-89ed-f9a578dadf60 | -5.2617 | -43.57486 | 2024-12-19 04:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e899e8ab-7eb7-39ef-83d0-1df9561f7ab8 | -4.47598 | -45.42723 | 2024-12-19 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37db7691-292a-3a8b-be87-b5001ca4d0c3 | -5.90671 | -46.23216 | 2024-12-19 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbd54646-5979-332f-9fca-5053ca3d52b0 | -3.63517 | -50.25806 | 2024-12-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90d16d98-cce1-304b-957c-ea99d4c6c086 | -4.34664 | -48.46774 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a595098-7852-33f9-831c-e0c3c39938a4 | -1.56201 | -53.78046 | 2024-12-19 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d30fcdc-af6a-3a7e-adf3-332cd6255dbc | -1.27016 | -54.13117 | 2024-12-19 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3a4396ed-2cae-395d-abfa-902ea3a94ad7 | -7.58564 | -38.32292 | 2024-12-19 04:29:00 | NOAA-20 | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0a4e021a-a3af-3bb8-99d4-8b7338ec978c | -2.44345 | -47.48734 | 2024-12-19 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b721be77-b286-31c4-a8f2-3e50048824da | -4.34886 | -48.47535 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4af2938d-ca11-3b29-8e96-ac3ec00dd731 | -3.74404 | -43.12454 | 2024-12-19 04:29:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c73ab0c9-1806-3671-9f59-d23dbd869df2 | -2.73131 | -45.20231 | 2024-12-19 04:29:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fee84dd4-1213-3cec-9ddd-08b16fc77400 | -3.68671 | -43.75421 | 2024-12-19 04:29:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b7d7784-f3d7-3162-92cb-7961a18f04a6 | -4.47654 | -45.42354 | 2024-12-19 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e6c8271-f746-35b8-9455-e0765b8a4d86 | -5.47657 | -46.35994 | 2024-12-19 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dbc705ae-6604-33bd-ae47-7ec4aa12cae5 | -5.66041 | -46.24231 | 2024-12-19 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a30b63c-dc0a-3878-9ff1-85e412c8e7b2 | -4.37762 | -50.05741 | 2024-12-19 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cefe1b74-2618-3871-bc8e-e73aa9295f11 | -3.9844 | -48.40019 | 2024-12-19 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45fb9510-d454-329b-8bde-c1d482442bb9 | -4.03955 | -49.77097 | 2024-12-19 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47328e62-bfaf-39e3-b713-cdb2ff2c5c14 | -4.21185 | -48.69558 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 280ecf71-c069-3ee9-9d51-26056ce5b1e3 | -4.33257 | -48.30294 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0c44546-589d-36a5-88f1-e9d9107e97dc | -5.54845 | -45.1022 | 2024-12-19 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0ccfb87-10ee-3145-b551-3ec0ddf0d850 | -2.51754 | -47.06075 | 2024-12-19 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 18b27fd3-d5d1-32d9-b275-68c470998ade | -4.80009 | -44.02828 | 2024-12-19 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7d6c8659-88be-3eac-8553-039020570b47 | -4.73538 | -46.80107 | 2024-12-19 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4d811f43-d012-3526-9fc8-28aba3c2fc46 | -3.78043 | -44.06718 | 2024-12-19 04:29:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d94626c-56fa-3afe-b226-8a756df5bf8f | -1.69561 | -54.01176 | 2024-12-19 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc36321e-4a30-3ca4-915c-02aaa68e0729 | -2.87212 | -45.24601 | 2024-12-19 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80cd38b8-297d-3e72-ae75-2d4b92915d22 | -3.68258 | -49.57711 | 2024-12-19 04:29:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 57420906-b309-3946-b1c6-d7e945380f29 | -7.42153 | -35.24515 | 2024-12-19 04:29:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 11e62462-0ea2-3c2e-a130-2111d3a43eca | -3.94747 | -41.49008 | 2024-12-19 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3342cf33-db69-3c9d-8134-9c63522a4710 | -4.34999 | -48.46825 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| adb1c7dd-a789-322a-885f-3e7943bab9bf | -7.79327 | -34.99404 | 2024-12-19 04:29:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 57ff5df0-4d4f-3a05-b009-d91415583c49 | -5.17561 | -37.59276 | 2024-12-19 04:29:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3c499a1b-3753-3c45-ae26-5b99bf8a3cb2 | -5.09054 | -44.18387 | 2024-12-19 04:29:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a149df8-9850-3028-b176-48b08a98831a | -3.18064 | -50.57024 | 2024-12-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46787628-bc53-34b6-aef1-b21c726c13ce | -5.82869 | -35.48098 | 2024-12-19 04:29:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2d645a41-9b17-3638-84fd-9fcdaee2f144 | -4.48117 | -47.98557 | 2024-12-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fdde1f49-2a18-33ac-947c-5304cab19620 | -2.4851 | -50.23656 | 2024-12-19 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58a02bfc-faf0-32d1-a20d-a300699df9cb | -6.29634 | -46.04363 | 2024-12-19 04:29:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 888240ed-6c10-3338-b051-4ca3cf9ec2bd | -4.80373 | -44.02885 | 2024-12-19 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 03c426a2-ee01-30a8-a87e-f981e0ce3b6c | -1.69668 | -54.01447 | 2024-12-19 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README11.md)
