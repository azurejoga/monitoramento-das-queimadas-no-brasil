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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed7be06b-9283-3116-824c-170f2cafad23 | -3.8372 | -41.7644 | 2025-10-19 14:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 111.4 |
| 6777ceb0-1536-34a4-955c-e129a39a31b5 | -6.2032 | -41.5464 | 2025-10-19 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 164.5 |
| 17c289f8-b2c1-3b01-a5dd-bcd200774188 | -10.848 | -43.9455 | 2025-10-19 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 216.3 |
| f4063b21-3833-3441-bb0f-9774d5199ff5 | 1.7482 | -55.9216 | 2025-10-19 14:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 4c316a17-4a9f-367e-90a4-22f89010de7c | -10.8293 | -43.9248 | 2025-10-19 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 8d00f48e-fb01-37c2-963c-d618751b2f20 | -6.823 | -41.705 | 2025-10-19 14:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 25e2298e-2ea7-3392-bfbc-7ef9356713c5 | -4.4059 | -43.4049 | 2025-10-19 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 15f37f82-5743-36bd-aef1-2867ec91270d | -7.6238 | -60.9212 | 2025-10-19 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 6c28632e-f023-3adb-934d-9ff8770f5f70 | -4.3152 | -43.0138 | 2025-10-19 14:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| acf2062b-e71f-32dd-83d2-5e07db09d861 | -4.4066 | -43.3118 | 2025-10-19 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 221f5d23-51ca-3102-a761-3fa5e6e8d0ec | -10.514 | -43.3815 | 2025-10-19 14:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 81859ffd-50e8-3953-8e74-f88daf00e210 | -3.8371 | -41.7883 | 2025-10-19 14:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| 7c319887-43d8-3ce2-94aa-29e606fc1993 | -10.4945 | -43.4079 | 2025-10-19 14:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 32bc4374-6565-3169-af0a-3049d51e067e | -4.315 | -43.0372 | 2025-10-19 14:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| a25430c3-df76-3bf0-9e3b-80373ab5ae79 | 1.7481 | -55.9413 | 2025-10-19 14:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 7c894649-ac8b-3347-ad0b-13b1d09dfa5b | -10.8289 | -43.9482 | 2025-10-19 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 133.5 |
| bdcb5daa-dac1-3a4a-afc9-5c8227fbf976 | -4.7708 | -42.1365 | 2025-10-19 14:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| ae31a2a1-5d6f-3294-83c4-a63c3d21db2f | -10.6853 | -44.5506 | 2025-10-19 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 47a0b4cf-95e6-3e04-bec6-f7944aab508a | -4.3872 | -43.406 | 2025-10-19 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 68acc6cf-5904-3bf2-b923-1f92b002d37c | -6.4443 | -41.8848 | 2025-10-19 14:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 178417b5-ecf7-3c2d-afe2-ccafdf0e44f3 | -4.6509 | -43.1337 | 2025-10-19 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| a4e0fe74-a282-3366-869a-2bce76db8e3e | 1.7482 | -55.9216 | 2025-10-19 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 429f1833-422f-3696-b57f-a3be9c3b094f | -4.3152 | -43.0138 | 2025-10-19 14:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 95751f42-9ecc-36c4-94b0-01502e870c26 | -10.4941 | -43.4315 | 2025-10-19 14:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| a63cc24c-af28-3f57-9b94-e45ecba57b26 | 1.7118 | -55.784 | 2025-10-19 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 3d66eedf-e11a-3b74-88f4-bf978cd19798 | -6.0489 | -41.9198 | 2025-10-19 14:10:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 112.1 |
| 16481688-d06a-3e86-bbad-4ae3ff4b3751 | 2.0416 | -55.74 | 2025-10-19 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| e148fc2a-af34-3367-9746-342468d41eb1 | 1.7668 | -55.7241 | 2025-10-19 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 02cbea40-9ce2-3892-bcfd-c69aaafcc843 | -3.8372 | -41.7644 | 2025-10-19 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 169.6 |
| 19fc9094-f3bf-3d94-a96c-7976ff619184 | 1.7481 | -55.9413 | 2025-10-19 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 3bfc03e2-59f2-34c3-942b-2f309ea362d8 | -6.4634 | -41.8591 | 2025-10-19 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| e160c6cc-6b84-3100-9ef0-67e42b2896dc | -6.1737 | -42.5985 | 2025-10-19 14:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 240f83a0-6232-3a8e-ab92-75e4449b3f16 | 1.7485 | -55.7441 | 2025-10-19 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| a95f02d6-43b3-3538-a944-c5a45bdc273b | -10.8289 | -43.9482 | 2025-10-19 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| f9ec3567-f69e-380b-a7cc-ce5753e5a9ff | -6.4443 | -41.8848 | 2025-10-19 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 68b8a02c-d684-3441-a571-6afdf22d7b63 | 1.7298 | -55.9612 | 2025-10-19 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 140.0 |
| c1f2c0f2-e5ff-3014-a718-c55860518814 | -6.411 | -41.4793 | 2025-10-19 14:10:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 128.0 |
| ad4ed656-032a-3a23-b8bc-088606cb96d8 | 1.7852 | -55.7239 | 2025-10-19 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 121c953f-285a-3b7d-8c45-0d17f2d7381a | -6.22 | -41.7372 | 2025-10-19 14:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| d54181c4-5f13-3282-a662-be4ddf60d524 | -4.4066 | -43.3118 | 2025-10-19 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 1e5d0996-56f3-323a-b2e6-5aeffd5e7603 | 1.7481 | -55.961 | 2025-10-19 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 8f8f68ec-4167-3073-9e30-fe87e9fde8ff | -5.7534 | -43.3835 | 2025-10-19 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ac125cae-b163-3db7-9b9f-dce24a1994d2 | -10.848 | -43.9455 | 2025-10-19 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 298.4 |
| 4875343f-efb8-30ea-97fd-044049da2093 | -10.7044 | -44.548 | 2025-10-19 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 84632a3d-4062-3aab-b3ef-36ca6a1120bf | -3.8371 | -41.7883 | 2025-10-19 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 129.0 |
| 237ce614-18ce-34c5-b4ef-f8c94746276b | -10.6853 | -44.5506 | 2025-10-19 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 3582002a-4e84-3df4-ac4d-0347245ea8ef | -6.1549 | -42.6001 | 2025-10-19 14:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 404845ca-0b5a-3016-9712-0e03ec334925 | -4.3872 | -43.406 | 2025-10-19 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 3f9c6905-a215-39a3-b8d5-e17fecb1bae8 | 1.7481 | -55.9807 | 2025-10-19 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 83bdab23-c6ee-3001-8f4e-43246cb4b3e2 | -4.7708 | -42.1365 | 2025-10-19 14:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 77d5d5a7-b97d-348b-b52c-8bbc1c236d46 | -7.0082 | -41.9986 | 2025-10-19 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 59.9 |
| 6895622d-5bf9-3e9a-ab0d-6750da0f80a2 | 1.7301 | -55.7641 | 2025-10-19 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| b8f1bcad-2e24-3af1-8d73-9f77967d54be | 2.0417 | -55.7203 | 2025-10-19 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 9dc0fb72-d61e-3841-b540-43a6bc4b556d | 1.8402 | -55.6639 | 2025-10-19 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| b6faa6d4-ade0-3063-be42-b18d21234db7 | -6.4443 | -41.8848 | 2025-10-19 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 59f8a41a-3932-3a26-94f4-24e7ab89edc4 | -8.6096 | -41.0445 | 2025-10-19 14:20:00 | GOES-19 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 79.8 |
| f665f31b-3469-327a-abc1-829d6da26cb2 | 1.7852 | -55.7239 | 2025-10-19 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 8aad8047-0a49-3233-a1ea-531ae8f01646 | -6.0489 | -41.9198 | 2025-10-19 14:20:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 116.8 |
| c1732780-9fef-387b-9a64-3382a45a4b66 | -6.4257 | -41.8625 | 2025-10-19 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| 4896463e-03f5-304f-a1ff-9060188bc53e | 1.7485 | -55.7441 | 2025-10-19 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 0cd34976-c6a9-328c-b0d7-ce22ed02edc6 | -11.4935 | -44.2024 | 2025-10-19 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| d485dcf9-88b9-35c9-83f2-b5879fac1729 | -6.3921 | -41.4811 | 2025-10-19 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| c09ad98d-02f6-3750-a9b9-558a752c2912 | -6.4252 | -41.9104 | 2025-10-19 14:20:00 | GOES-19 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| d5db1c47-3145-3fed-a0fc-3a15be7f814b | -4.4845 | -42.8631 | 2025-10-19 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 162cd3f3-58f6-3b4d-933a-51206008a435 | -11.3776 | -44.2663 | 2025-10-19 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| a2071cc4-601b-382c-bd14-9bffe41c9d56 | -11.4551 | -44.2082 | 2025-10-19 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 045d7759-295d-364d-9d4e-b48284301641 | 2.0417 | -55.7203 | 2025-10-19 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 15c167ca-a3f5-3aec-b7dd-1f9b898d5ffe | -4.6509 | -43.1337 | 2025-10-19 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| a902296c-97cd-3a8e-bb6f-fee68f8b4954 | -10.6853 | -44.5506 | 2025-10-19 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 709c6b7a-340c-3838-bd82-2057e7957899 | 1.7846 | -56.0196 | 2025-10-19 14:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 97757c40-dbf7-334c-aa79-79585c94a94d | 1.7301 | -55.7641 | 2025-10-19 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| a87a6266-52c5-3dd6-afbc-a08e10b5fdc9 | -6.4448 | -41.8368 | 2025-10-19 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 76afaf99-d689-30d3-b9a8-30ee462ed2d9 | -11.4372 | -44.1407 | 2025-10-19 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 3be4f4f2-5fcd-3ab2-afa7-d83fefff3b4c | -12.0058 | -41.4875 | 2025-10-19 14:20:00 | GOES-19 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 87.1 |
| a8c23ef4-0cbb-34ab-8966-bb8693a5352e | -3.8372 | -41.7644 | 2025-10-19 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 118.5 |
| 97aa33d9-e0e7-3c2a-b9ac-82f96597f58c | -10.7044 | -44.548 | 2025-10-19 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 57d86114-0a1b-3390-9ade-8cba0470af9d | -6.4632 | -41.883 | 2025-10-19 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| e1fcd16b-72d2-3ba8-a24b-fd9a3f3b9a3c | -6.823 | -41.705 | 2025-10-19 14:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 6824a179-faaa-3b19-8a29-2bdda097f445 | -6.22 | -41.7372 | 2025-10-19 14:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 0f1adc52-8678-3fb1-b6ee-e34d328fc310 | -5.854 | -42.6486 | 2025-10-19 14:20:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 1ac314e0-a8c7-3748-9779-113b49e83141 | 1.7668 | -55.7241 | 2025-10-19 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| f366c7e6-7c53-3a8e-993b-97eca917d146 | -3.8371 | -41.7883 | 2025-10-19 14:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 123.3 |
| 01bf66c9-717f-313f-913e-47dcb08ec2f8 | -11.4752 | -44.1584 | 2025-10-19 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 7db4f64a-696b-3956-8977-ca9375465e1b | -1.227 | -49.041 | 2025-10-19 14:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 4a5011eb-3d51-312f-b705-c5cf9e2ea0f3 | -10.4596 | -44.3724 | 2025-10-19 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 21ecd6e8-e8a1-365d-82fc-a7b72885cee8 | -11.4372 | -44.1407 | 2025-10-19 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 18ab3dbb-bb1f-35be-b7dd-04298326c2fb | -11.4184 | -44.1201 | 2025-10-19 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 1e936fd6-0829-36dc-a7e4-25b8b02e5679 | 1.7481 | -55.9807 | 2025-10-19 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| e7e8d772-28b3-3ede-b258-8698e9c2dce2 | 1.7481 | -55.9413 | 2025-10-19 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 6266dd0f-10e8-3158-99c4-66b1eeb688ac | -4.3872 | -43.406 | 2025-10-19 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 4173cd2e-7345-378f-bce9-81c2a476c43f | -6.5412 | -41.6358 | 2025-10-19 14:30:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| 8c7846a0-58c4-3811-8b48-020f8a671358 | -5.7596 | -42.7033 | 2025-10-19 14:30:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 458f068b-d5f3-3927-afca-f87ec74e1f36 | -12.3395 | -41.2068 | 2025-10-19 14:30:00 | GOES-19 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 83.2 |
| 476e4915-b049-3175-b0b0-c485e8a28591 | 1.748 | -56.0201 | 2025-10-19 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 9e6bb08b-4d42-3135-8072-3daef0bb749d | -5.7549 | -43.22 | 2025-10-19 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 132625ad-b684-33dc-a5e7-c634c514105d | -5.7784 | -42.7018 | 2025-10-19 14:30:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 749a6d73-7e5a-372c-80a8-5ca0bd9e10f3 | 1.7846 | -56.0196 | 2025-10-19 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| e5125ec2-8a88-307d-900c-1a17f647ab60 | -11.436 | -44.211 | 2025-10-19 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 0606ab3b-419e-32fa-b586-a27c74fd8464 | -7.1944 | -42.195 | 2025-10-19 14:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| e49064d3-78a3-30a5-8e20-714b3d94143f | -6.0301 | -41.9214 | 2025-10-19 14:30:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 103.3 |


[Clique aqui para ver as próximas entradas](README66.md)
