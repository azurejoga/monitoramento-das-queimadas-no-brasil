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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cff9da9-5580-3c70-a121-6d8b2f548f08 | -10.9815 | -45.0874 | 2025-06-29 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 39b57cd5-7e10-3777-ad1f-55dc10f194f5 | -10.5576 | -52.0499 | 2025-06-29 02:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 137.9 |
| bf2719d2-b5ee-30da-82b0-00084f7f5450 | -17.4045 | -42.6186 | 2025-06-29 02:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 922e94a5-49e9-333e-a354-4342ec780774 | -10.9811 | -45.1104 | 2025-06-29 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| d6587cbc-9da0-3b26-ae6e-599195b56670 | -10.5579 | -52.0289 | 2025-06-29 02:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| df9bcf24-e293-3d8f-a8f1-170228ccf2a9 | -10.5576 | -52.0499 | 2025-06-29 02:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 1e9dcd35-48fa-371f-9af8-7cf027d745a2 | -11.0354 | -56.2844 | 2025-06-29 02:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| de70005e-c519-3c19-b8ed-34239b9c43f5 | -17.4045 | -42.6186 | 2025-06-29 02:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 66.9 |
| c21bfb61-9ab6-39c4-a2ba-7679ddd40753 | -11.0356 | -56.2644 | 2025-06-29 02:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 77c9ff07-d447-33f7-ac27-992c4e7527f3 | -10.5576 | -52.0499 | 2025-06-29 02:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 8f6d931f-879e-3a3f-8d99-59fdc7157f0c | -17.4045 | -42.6186 | 2025-06-29 02:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 52.2 |
| ebc2b56e-5a51-3555-831e-598d79bd1b38 | -11.0168 | -56.2659 | 2025-06-29 02:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 47f7b239-119b-3208-ae5e-26108d55db4a | -10.9811 | -45.1104 | 2025-06-29 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| c88ebabe-f28f-3e4e-84cb-304b89f98174 | -11.0356 | -56.2644 | 2025-06-29 02:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 1cd6921b-47e5-3ce2-b23d-efed1a1bac22 | -10.5579 | -52.0289 | 2025-06-29 02:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 3fc43274-a65f-37b4-a7d8-323316770c35 | -11.0354 | -56.2844 | 2025-06-29 02:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 21939689-c1c7-312a-a233-e8b0065a4a21 | -11.0356 | -56.2644 | 2025-06-29 03:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| fc8dca99-82ff-3a9a-81fd-956811ee1778 | -10.5576 | -52.0499 | 2025-06-29 03:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 94590975-5f87-3f66-8341-728cac362b4a | -10.9811 | -45.1104 | 2025-06-29 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 4471920b-57ad-39f4-a110-07aa0618b400 | -10.5579 | -52.0289 | 2025-06-29 03:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| af033acb-8278-34cd-89bc-484257329a7a | -11.0354 | -56.2844 | 2025-06-29 03:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 3185bb7a-de12-3858-b844-e1c9b035a109 | -11.0168 | -56.2659 | 2025-06-29 03:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 76570882-01c3-3383-8c41-17a0b7d85287 | -17.4045 | -42.6186 | 2025-06-29 03:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 7c3bfab1-1f60-388f-aa14-89ae48923ffd | -11.5496 | -52.8076 | 2025-06-29 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 23c6ab08-4326-3108-ae08-9c9e5b6d389c | -10.5579 | -52.0289 | 2025-06-29 03:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 5d54a250-4262-3690-8563-507fa3106cfe | -11.5502 | -52.7659 | 2025-06-29 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 253.6 |
| fb37b469-47b3-34c6-9448-ddbfafc7477b | -11.0354 | -56.2844 | 2025-06-29 03:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 5d94f3b2-b82e-34c9-bce6-75b7cb1944ae | -17.4045 | -42.6186 | 2025-06-29 03:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 49.9 |
| fbc98fae-b68b-34e6-af11-bfce5248a028 | -11.0356 | -56.2644 | 2025-06-29 03:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| f4b74c6b-631d-3a13-8a12-ead5224b4290 | -11.5499 | -52.7867 | 2025-06-29 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 346.4 |
| 9330cfb8-dee4-3f70-b157-11ac29fdf39c | -11.5688 | -52.7848 | 2025-06-29 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 154a0956-dff2-3810-9bc3-b4c1d797a4e4 | -11.5309 | -52.7887 | 2025-06-29 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 112.3 |
| f6822a64-3b60-3ee9-9771-23b26645ada6 | -11.5312 | -52.7678 | 2025-06-29 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 8c919619-b70a-382a-aacb-ca44dbbb26fc | -10.5576 | -52.0499 | 2025-06-29 03:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 128bc9a8-7744-3c43-aa5b-3d7f819d4895 | -10.9811 | -45.1104 | 2025-06-29 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 3302ec72-12af-34a0-8f9f-bbcc4bc27b06 | -10.5579 | -52.0289 | 2025-06-29 03:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| ae91e9b9-d278-38e0-aa7c-89865268280b | -11.0354 | -56.2844 | 2025-06-29 03:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1549c773-8b8b-3f9b-8912-2590efaf2d0d | -11.0356 | -56.2644 | 2025-06-29 03:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| f7806e6b-e9d4-31cd-a4c2-27318c7c5281 | -10.9811 | -45.1104 | 2025-06-29 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 0feaac40-6db6-3995-84ee-143a3cf89226 | -10.5576 | -52.0499 | 2025-06-29 03:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 2feae293-2456-3b07-bd29-97ab79a72fd7 | -11.5312 | -52.7678 | 2025-06-29 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| e6245fc7-600d-3108-942d-3fcb6d94c087 | -10.9811 | -45.1104 | 2025-06-29 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 973b6c4a-6032-37e9-b575-51132b185906 | -11.5688 | -52.7848 | 2025-06-29 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1fcaa94c-d8fb-36e0-aa39-cd832dc586ba | -10.5579 | -52.0289 | 2025-06-29 03:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 253b062d-6ba9-33e2-b905-45a4642803cd | -11.5496 | -52.8076 | 2025-06-29 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 9d91b863-c648-3179-96aa-8c9c51608f44 | -11.5309 | -52.7887 | 2025-06-29 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| bd3ebc53-8b57-3ea7-9f93-93982890af1f | -11.0356 | -56.2644 | 2025-06-29 03:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| a23006aa-355a-38f1-9f8d-1741c0f5287d | -11.5502 | -52.7659 | 2025-06-29 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 217.0 |
| 982e7c27-b71b-38fb-934f-113f3276c241 | -11.5499 | -52.7867 | 2025-06-29 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 251.0 |
| 0fb0203d-827b-3588-8292-6e1da5145d23 | -10.5576 | -52.0499 | 2025-06-29 03:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 9cba2386-0c1b-366a-96ec-f04e06e3e332 | -10.5576 | -52.0499 | 2025-06-29 03:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 1ce681c8-7557-314c-ac2f-e9c12e8bd991 | -11.5312 | -52.7678 | 2025-06-29 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| edeb7e33-a3d4-36b2-a7ef-44f4c01a28b8 | -11.5502 | -52.7659 | 2025-06-29 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 170.0 |
| d692bc10-903f-3b31-be12-89fe16716176 | -10.5579 | -52.0289 | 2025-06-29 03:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 024c12d5-09ab-3a90-9f68-24bbacc96285 | -11.5496 | -52.8076 | 2025-06-29 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 01d05808-de5d-3623-b0f1-b1bdc7097ac2 | -11.0356 | -56.2644 | 2025-06-29 03:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 30b9e9a7-9132-39d9-bc6f-ccc01864bed8 | -11.5688 | -52.7848 | 2025-06-29 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 713c56bf-00aa-3f6f-993f-7f85b13296ea | -11.5309 | -52.7887 | 2025-06-29 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| b95af752-9a76-3efa-be54-19e16f40dac1 | -10.9811 | -45.1104 | 2025-06-29 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| caffbf7d-ac4f-3494-88c9-69d97f38f63c | -11.5499 | -52.7867 | 2025-06-29 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 216.7 |
| 3a0fca65-5b36-31d3-8b0b-5aceb062009d | -4.55385 | -48.00633 | 2025-06-29 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86c0f278-304b-3485-9d86-e5ae2216175c | -7.49044 | -45.45487 | 2025-06-29 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8619e8ff-a41a-3347-a080-3167a9496ba6 | -7.09615 | -44.36458 | 2025-06-29 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11ddefbf-5b4c-3c68-b61a-e307a5d5cb14 | -3.6235 | -47.54474 | 2025-06-29 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad4f0660-6eab-3af1-87a7-2db96058eb55 | -7.1752 | -43.66758 | 2025-06-29 03:42:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03a22a29-eee3-3d51-a871-8480518cb619 | -7.10134 | -44.36559 | 2025-06-29 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03138036-1856-3d4f-87c2-8ccd0636a374 | -7.49109 | -45.45125 | 2025-06-29 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b90f0cd1-30b6-3389-a25f-a34282199553 | -7.21878 | -43.07565 | 2025-06-29 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a7c71eed-1117-3950-b9ec-4beeb2a0034f | -3.63021 | -47.54599 | 2025-06-29 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c2d6e17-a965-3973-b12d-2ac0f22a24b6 | -4.17554 | -42.03352 | 2025-06-29 03:42:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5056adaa-2f9c-3734-87d1-67e7f739a77d | -7.2613 | -43.14368 | 2025-06-29 03:42:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5fa470b5-b562-3b9e-bed1-70472ef96123 | -3.41906 | -43.16381 | 2025-06-29 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9946a8af-76c3-37ec-8633-09d51fc5981b | -4.54363 | -48.0241 | 2025-06-29 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d21fec5e-f523-3213-b1a5-8990f453147e | -7.1947 | -43.70274 | 2025-06-29 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b17ff0a-9a43-36ad-8137-d2763d55ae18 | -7.17594 | -43.66333 | 2025-06-29 03:42:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 814b9a92-1c33-3d65-9056-8469101cd1a8 | -7.25651 | -43.14287 | 2025-06-29 03:42:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d839ee50-af96-37bd-bc1d-8e3a3e10697f | -7.19324 | -43.71121 | 2025-06-29 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c03b00e3-5ccc-3553-8892-7b779100176c | -7.19275 | -43.71404 | 2025-06-29 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 653f863c-1edc-30ce-afbd-02fcad4b3ca6 | -7.21791 | -43.08079 | 2025-06-29 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 806e19b3-ceee-3e03-9350-2bd99a2a3728 | -7.19373 | -43.70839 | 2025-06-29 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| abcfa518-0855-35b6-9ca8-c6bd157f0675 | -7.26221 | -43.13845 | 2025-06-29 03:42:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 073d78c0-0a59-3e39-8af4-49e570f99d31 | -7.267 | -43.13922 | 2025-06-29 03:42:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4ddb9ce4-bb2a-3205-a83a-70fef98bf449 | -7.18777 | -43.71321 | 2025-06-29 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db3ccd82-e7f8-3db9-85e9-f7759c372e35 | -7.26791 | -43.13397 | 2025-06-29 03:42:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5768f9f7-09e1-3dca-9fc1-c1edb460dbed | -4.38387 | -41.91396 | 2025-06-29 03:42:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9aa07940-33f0-3832-8a8f-c51360748d7b | -5.08853 | -48.356 | 2025-06-29 03:42:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8465ab00-2837-31e9-9138-64ac702238eb | -5.08913 | -48.35262 | 2025-06-29 03:42:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b141a503-e86e-3a2e-9c5f-93194ee06c6e | -5.57397 | -45.21576 | 2025-06-29 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ea60172-8692-3263-aa49-1c42b936c74b | -7.26402 | -43.12799 | 2025-06-29 03:42:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 87109efc-82b6-3919-8c35-8d017cb67e45 | -7.21875 | -43.0778 | 2025-06-29 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2db79355-be38-3919-89d2-0688d79b5377 | -7.18826 | -43.71037 | 2025-06-29 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 386948d9-f2fd-30be-b9e6-e840074bf337 | -3.41961 | -43.14125 | 2025-06-29 03:42:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ea479ae-ac9f-39f4-8a27-f02ad6bd7c0f | -3.62533 | -47.54975 | 2025-06-29 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac4f1bde-f8a3-3270-83cc-c0f00f7d7f55 | -4.17087 | -42.0328 | 2025-06-29 03:42:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 95ecf0d6-4ee5-3b8a-a216-0cb80af5eebe | -7.12475 | -45.52595 | 2025-06-29 03:42:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 452ce243-bbfd-3c5b-b8f9-3ed0f9675c4b | -5.08798 | -48.3591 | 2025-06-29 03:42:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3cdc15ee-e2f4-3ffb-967d-777cc644399a | -7.19422 | -43.70556 | 2025-06-29 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b3d3cb6-dd8b-381a-bac4-d3a63e52e076 | -7.19226 | -43.71688 | 2025-06-29 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eeb485ec-b9eb-34a4-a05a-7accb275805a | -3.62637 | -47.54387 | 2025-06-29 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 44f8d383-379f-3762-9d22-db93d45e1482 | -7.09705 | -44.36388 | 2025-06-29 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README8.md)
