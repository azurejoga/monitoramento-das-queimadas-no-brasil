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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d9712a1-845f-3cc9-8c3f-0cafafe778be | -2.8197 | -53.0425 | 2024-12-02 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 6c7b174f-d621-3985-89d7-dafd3fc5babf | -2.8013 | -53.043 | 2024-12-02 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 289012ce-457f-3731-b78a-89ab2e5da226 | -3.259 | -53.6388 | 2024-12-02 02:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| d344a318-3640-3a36-97dd-10b7acef6653 | -5.1181 | -43.1964 | 2024-12-02 02:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| d644e86a-cde0-3005-a26a-25d11b55997f | -2.8012 | -53.0633 | 2024-12-02 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 47276170-2441-326c-802d-176b694a8c62 | -6.0858 | -48.0774 | 2024-12-02 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d0c2c86d-611f-35d6-9af5-bb50fc8859cf | -20.7217 | -54.4341 | 2024-12-02 02:20:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 55.9 |
| afd882ca-4606-398c-8c6c-a5762ed41d02 | 3.3841 | -60.4946 | 2024-12-02 02:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 66a25c34-c97b-38a3-9d78-edbffb15e44f | -4.8174 | -48.6272 | 2024-12-02 02:20:00 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| b829f108-f695-37d9-938b-772b65d7e553 | -4.5932 | -43.3471 | 2024-12-02 02:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| a7076ece-85a0-39d5-b0c2-2e2016e016fa | -2.5612 | -53.4133 | 2024-12-02 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 6b930aea-d2c8-3aeb-a0c2-f342b7cef245 | -5.118 | -43.2198 | 2024-12-02 02:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 15b31b73-2574-3d21-ad42-1eaab29caacd | 3.3658 | -60.5139 | 2024-12-02 02:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 91f72bd5-ad8a-310b-9e89-0d5cf1c971ac | -2.5428 | -53.4137 | 2024-12-02 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 311e2aa3-1988-38fb-acfd-b9a72d2eb0a9 | -2.8196 | -53.0629 | 2024-12-02 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 682ce8ac-1b98-3dc4-9db5-57dec743b0ac | -2.5612 | -53.3931 | 2024-12-02 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| c167d719-19f4-32c8-8e28-d4b121cf82a2 | -4.5745 | -43.3483 | 2024-12-02 02:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 0345e4e2-d610-37de-9725-156da9ceb86e | -3.4017 | -50.2381 | 2024-12-02 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| fb32d7dd-4f7e-3e1c-85de-68de650185aa | -12.4169 | -63.7465 | 2024-12-02 02:20:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 1dae872c-59f4-3654-b2d3-5f8e5a02bae4 | 3.3841 | -60.5135 | 2024-12-02 02:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| a49f997b-4db0-33a3-be00-1b5926b456b8 | 3.3657 | -60.5329 | 2024-12-02 02:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 1776be6a-35b8-3e43-8132-32c1988c5a4c | -12.4358 | -63.7455 | 2024-12-02 02:20:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 4160d5ec-d109-3337-84f1-ae260ea3bfda | 3.384 | -60.5325 | 2024-12-02 02:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 55cc5a9c-58de-32c9-b8cc-c2a72bc20aca | -2.6349 | -53.351 | 2024-12-02 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| f6d6766f-7dec-3400-b32a-9e412ee2d5bb | -9.3404 | -35.9565 | 2024-12-02 02:20:00 | GOES-16 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 73.9 |
| ef222f74-7628-33c2-9761-6c5603c0c6cd | -2.008 | -54.3091 | 2024-12-02 02:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 5d359ca8-8dbc-351d-8215-a72d410acf73 | -2.0263 | -54.3088 | 2024-12-02 02:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| c6775732-bed4-318a-99c6-03c8229f8c41 | -6.0862 | -48.0339 | 2024-12-02 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 46677431-2ceb-3d46-845f-73f13ff9c820 | -6.086 | -48.0557 | 2024-12-02 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 80e2d6ea-3c86-33fb-92dd-f53460c39929 | -6.1047 | -48.0544 | 2024-12-02 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| fe17e00f-fafe-3511-8361-44c0ec19fbd0 | -6.0674 | -48.0569 | 2024-12-02 02:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 85227d5c-c1d9-33e1-86b3-790344a450c6 | -2.5612 | -53.4133 | 2024-12-02 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 48703d77-e74c-3f0c-9a06-f377b8928c36 | -6.086 | -48.0557 | 2024-12-02 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 202.0 |
| 5e268c67-6428-35c8-9d05-8f7960ef9d52 | -4.5932 | -43.3471 | 2024-12-02 02:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| dfd601dd-11b4-3dc3-a15a-0068d6177f50 | -2.5612 | -53.3931 | 2024-12-02 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| a2f1b472-8b60-331f-9c1f-67fb58218cf9 | -2.8196 | -53.0629 | 2024-12-02 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| d3e02411-9481-3b99-b25a-9543a9ef06cd | 3.3658 | -60.5139 | 2024-12-02 02:30:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 75fddd13-ae0b-3688-a031-06b4b5955af2 | 1.1072 | -55.9874 | 2024-12-02 02:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| aff96302-a520-3379-a08e-7518ca2106c0 | 1.1256 | -55.9872 | 2024-12-02 02:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 540bad69-4f5e-3924-a863-a536bd5d0928 | -20.7217 | -54.4341 | 2024-12-02 02:30:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 0fd54c88-e159-375d-bef7-62ec591864fe | -4.5743 | -43.3716 | 2024-12-02 02:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| d911f2a5-5974-3d21-afb4-003216100b2d | -2.0263 | -54.3088 | 2024-12-02 02:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| b57b4f06-6520-3da8-99d6-019ace29fc07 | -4.267 | -50.8551 | 2024-12-02 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| ad0e8021-ff0f-39a2-b2bc-d4f9a85c3bc1 | -12.4169 | -63.7465 | 2024-12-02 02:30:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 7bf710ce-2a74-3eb9-9baa-bd806d179ad7 | 1.1255 | -56.0069 | 2024-12-02 02:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 2a4bbc74-df27-373d-8ed5-e596d7ee4920 | -3.2591 | -53.6186 | 2024-12-02 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 7a78df41-5be8-36d0-87e7-267fb8f64c42 | -6.0862 | -48.0339 | 2024-12-02 02:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| d10046cc-036a-32c7-9069-93c7e836078e | 3.3841 | -60.5135 | 2024-12-02 02:30:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 78853fec-bf23-31aa-a717-e6cd904306b0 | -2.6349 | -53.351 | 2024-12-02 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 06f91450-dcb0-3282-a4e2-f4ffb0b434ea | -5.118 | -43.2198 | 2024-12-02 02:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| a770d026-a546-3dd4-aef2-1b1f540b4f17 | -2.8012 | -53.0633 | 2024-12-02 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 7a6748d6-975c-3171-8631-37a2d77ed504 | -3.259 | -53.6388 | 2024-12-02 02:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| a1295579-93f7-3bb3-b34c-ec17d0f080d4 | -2.7759 | -55.3509 | 2024-12-02 02:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 87041f31-c115-39d9-b546-1722c531f2e6 | -2.5428 | -53.4137 | 2024-12-02 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 3af0bc1a-6403-32d3-a4cc-f5ed5b94b8ee | 1.1072 | -56.007 | 2024-12-02 02:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| bc47adf3-3718-3d79-bd6d-6f96e22f9763 | -5.1181 | -43.1964 | 2024-12-02 02:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| e4a28080-309d-34d8-a7de-fb81d0ef0351 | -2.8013 | -53.043 | 2024-12-02 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 5f4c9785-e66d-3390-9466-7df7a097e420 | -12.4358 | -63.7455 | 2024-12-02 02:30:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| e9b26f4f-57a4-3d91-916f-35dee85e6cc4 | 3.384 | -60.5325 | 2024-12-02 02:30:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 0a185157-baf8-3dc4-80e8-f7c59546eea8 | -12.4171 | -63.7274 | 2024-12-02 02:30:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d4d0c56e-e66b-36b3-9498-f2a02452be58 | 3.3657 | -60.5329 | 2024-12-02 02:30:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 17e84450-bcff-3a7e-9b16-4e513ec7cb0b | -4.5745 | -43.3483 | 2024-12-02 02:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 6d9d7da4-f9a1-3b46-990d-fa1c08251c5b | -2.5428 | -53.3935 | 2024-12-02 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 7e4ee883-1b32-3535-b64d-c72e1573145b | -2.8197 | -53.0425 | 2024-12-02 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 8a9c8cfa-0731-3f8b-a064-23c2a76d8ed3 | -2.6348 | -53.3712 | 2024-12-02 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b526d27b-cfeb-3df4-99be-69ef1d9e56df | -2.5612 | -53.3931 | 2024-12-02 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 2a1db505-b073-34c2-8692-957a9966ebec | 1.1256 | -55.9872 | 2024-12-02 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 09a95442-6290-35a7-87e9-2da8eddef105 | 1.1072 | -56.007 | 2024-12-02 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 0d3377eb-cc3c-3673-b4b2-dd99d4c8593d | -2.5612 | -53.4133 | 2024-12-02 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| ef418d55-4864-3386-98f9-425f7dccfe0a | -2.8197 | -53.0425 | 2024-12-02 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| c14cbac2-de7e-30c4-a4ed-258baa50cf34 | -20.7217 | -54.4341 | 2024-12-02 02:40:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 74662d17-551c-399d-b4fc-83f9551868cf | -2.0263 | -54.3088 | 2024-12-02 02:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 60c3f9dc-bfdc-38e4-94d9-b1e40fa7a14c | -5.118 | -43.2198 | 2024-12-02 02:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 30490250-8767-32dd-a8c7-de279a703e79 | -2.6349 | -53.351 | 2024-12-02 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 8606b618-bff1-3dbe-a0a4-22728e54e675 | -5.1369 | -43.1951 | 2024-12-02 02:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 65af65cf-2980-3038-b177-1b46ab924a59 | -2.6348 | -53.3712 | 2024-12-02 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| f3f57bdd-2401-3d75-b291-760eb67533dc | -12.4358 | -63.7455 | 2024-12-02 02:40:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 73.2 |
| b10e49f7-aae9-369f-8401-eef33b0fc0e0 | -5.1367 | -43.2185 | 2024-12-02 02:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 87b0aaaf-b4e7-3f02-a63e-d3d2a7344a1e | -6.0862 | -48.0339 | 2024-12-02 02:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 5dbf29ba-e716-3bbc-98da-d04cf690a5b3 | -3.4017 | -50.2381 | 2024-12-02 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| c4b9e77b-406a-3d81-ab70-6d6a10188798 | -12.4359 | -63.7264 | 2024-12-02 02:40:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 094cd959-5f50-3e63-812e-7496bfab2908 | 1.1072 | -55.9874 | 2024-12-02 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 4354f969-f9c6-3eaa-aa31-da65171d7741 | -2.5428 | -53.4137 | 2024-12-02 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 57beece6-0e6f-3d84-926d-d522e4a9ff66 | -3.2591 | -53.6186 | 2024-12-02 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 8082cce1-1bf9-3ea4-849c-f08282940b9a | 1.1255 | -56.0069 | 2024-12-02 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| c1a9bab9-adae-3304-8340-8e46e52e56e3 | -3.259 | -53.6388 | 2024-12-02 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 58e42d04-4a03-35ac-b02d-1b9231a93a63 | -12.4171 | -63.7274 | 2024-12-02 02:40:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 3f1a68f9-5a81-3fb4-8374-be57a6789c4d | -4.5932 | -43.3471 | 2024-12-02 02:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| e945e9ed-e125-339b-86a7-7f0e5ef5baff | -2.8013 | -53.043 | 2024-12-02 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 107f9bfa-1b91-37d9-95c5-98eda7829b69 | -6.1047 | -48.0544 | 2024-12-02 02:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 6d79de0f-cdd0-3bd9-8049-0ac0c96291d8 | -4.5745 | -43.3483 | 2024-12-02 02:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 39bbb401-b08d-3976-a93c-138ca6b2c857 | -6.086 | -48.0557 | 2024-12-02 02:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| ac658119-b96e-3256-aa95-9c0534ac7610 | -5.1181 | -43.1964 | 2024-12-02 02:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 5d758afb-1ce8-37c5-a721-8352f29172b6 | -6.0674 | -48.0569 | 2024-12-02 02:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| fc286b37-b1f8-32a2-b385-caa8db0aa576 | -4.5743 | -43.3716 | 2024-12-02 02:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| bcc6befb-0454-3c2b-b47d-5076d805837e | -1.0735 | -53.4562 | 2024-12-02 02:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 915ca28b-4c5e-389e-9e64-a6e3247bf593 | -2.8196 | -53.0629 | 2024-12-02 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| bd291aa4-13f3-37da-ae88-8fd87118f093 | -12.4169 | -63.7465 | 2024-12-02 02:40:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 2b7e9944-9468-313c-9786-143db9a3777a | -2.8012 | -53.0633 | 2024-12-02 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| e9351df6-ccba-3af5-8a4c-65a066f30f2c | -7.79914 | -35.30504 | 2024-12-02 02:47:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README20.md)
