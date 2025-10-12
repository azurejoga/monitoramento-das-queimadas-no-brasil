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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0b4c74d-7ef1-3f86-9f19-b204c4ded01a | -19.0319 | -57.5382 | 2025-10-12 04:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 46.2 |
| b57bb6c8-65a6-347e-aabe-65b2a0bbe5ac | -9.4143 | -45.7407 | 2025-10-12 04:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 8c5d724a-c27c-3a9b-b023-bfc259b88dc9 | -9.414 | -45.7634 | 2025-10-12 04:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 3401ffc5-55bf-3b94-ad1b-5b218e81d68e | -9.3954 | -45.7429 | 2025-10-12 04:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 98edb84b-adcf-3549-b1a6-7dcc29db8c92 | -2.5423 | -47.811 | 2025-10-12 04:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 7757828a-db06-3320-9264-7498b8458722 | -14.4068 | -47.9781 | 2025-10-12 04:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 13dac2c3-fb29-3da8-90e3-197cfcb27124 | -9.3951 | -45.7655 | 2025-10-12 04:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 044d8dc3-5d0b-3cb8-8e04-4a89a9a31a7b | -19.0319 | -57.5382 | 2025-10-12 04:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 51.0 |
| ab7c29ef-49d8-3d37-8382-01a7f2cd5b4f | -6.5851 | -44.6098 | 2025-10-12 04:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 5fd8490d-9cf1-3527-bae0-9ec29bb8d0c2 | -2.5423 | -47.811 | 2025-10-12 04:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| a2d8fef5-f062-3ff7-9ab0-3ebbaa595b11 | -2.5423 | -47.811 | 2025-10-12 04:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| a1820e7a-cdb2-3862-97bf-0e8587f27f37 | -1.13496 | -47.80236 | 2025-10-12 04:40:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff0d1096-9750-3cae-99b1-c79b498e3b3f | -1.89862 | -51.0089 | 2025-10-12 04:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a8ca22d-dc9f-3ce7-93ee-05af59b57767 | -0.90467 | -47.54897 | 2025-10-12 04:40:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6145ead9-1eec-3b81-b2c2-8c66c682a0d9 | -2.53097 | -47.80587 | 2025-10-12 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 50e6a03b-8107-3030-a961-ef2dbcf8d0c6 | -3.34605 | -42.16039 | 2025-10-12 04:40:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 406a1a55-95fb-3168-bd5e-a9ed66d3414b | -3.52926 | -39.77963 | 2025-10-12 04:40:00 | NPP-375D | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ce2511ca-b8ac-3ec2-987b-6de64c902350 | -1.89799 | -51.01281 | 2025-10-12 04:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1827ad36-1bf0-3359-ac67-1786a8f07608 | 1.85684 | -55.84409 | 2025-10-12 04:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ffddcc12-ddff-38b5-983e-1a06d30b5ea9 | -2.2708 | -47.85463 | 2025-10-12 04:40:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f8fbd96-5487-3ba9-a700-bd25f8def4a8 | -3.29306 | -43.50264 | 2025-10-12 04:40:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ac7bfd9-48c7-311b-8876-2f3beae27c27 | -3.29472 | -43.50337 | 2025-10-12 04:40:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac7c80e6-5dee-3932-b6f1-6279add5f1f1 | -3.52977 | -39.77629 | 2025-10-12 04:40:00 | NPP-375D | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3cc247e6-ca23-360f-86f9-dd8a6de9d172 | -2.27135 | -47.85114 | 2025-10-12 04:40:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 808d7cf5-fcd8-3709-84d1-1871ed663ba8 | 1.82415 | -55.8329 | 2025-10-12 04:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86265c25-3612-3fad-9de3-51af1be75a3e | 1.84676 | -55.84564 | 2025-10-12 04:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34d6afe7-1afd-3d64-b5a4-2b82c1fe4411 | 1.85079 | -55.87168 | 2025-10-12 04:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5e6df0b-295d-3aba-a439-a9afc4bf2897 | -4.00766 | -38.73327 | 2025-10-12 04:40:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 151b6348-cf60-3e8b-aceb-eb20d4439380 | -0.90133 | -47.54845 | 2025-10-12 04:40:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 62592558-5a70-3867-b15f-46715d2daeab | 1.8518 | -55.84487 | 2025-10-12 04:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85ac3c48-dfe2-36e6-bcf2-5086b24c33ca | -2.45036 | -48.62073 | 2025-10-12 04:40:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16326e51-d8f9-39cf-9b00-f4ee9bdbbb0b | -2.541 | -47.80743 | 2025-10-12 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| abb16e3d-3476-3e4d-8995-2950328e9d13 | -3.14333 | -44.42375 | 2025-10-12 04:40:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23c6d71c-182e-3db8-8340-1e732b993e43 | -0.42853 | -52.07106 | 2025-10-12 04:40:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06095d8d-f2a3-348b-84ca-0a554022a655 | -1.9014 | -51.01413 | 2025-10-12 04:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e09ffca-36d5-3ee8-8a1a-a5ece6dc7ba5 | -2.75608 | -45.34158 | 2025-10-12 04:40:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83846653-fcf3-3a63-b8b8-ed565d62876b | 1.85225 | -55.84777 | 2025-10-12 04:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3788c39-999f-39c1-bdc8-55101f04a016 | -3.14591 | -44.42693 | 2025-10-12 04:40:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75c0fd80-6b59-36cd-9247-20242d9e68f7 | -2.53766 | -47.80691 | 2025-10-12 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c8aaef7e-404c-3bd6-a01b-31e5149767a0 | 1.94124 | -55.69622 | 2025-10-12 04:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73a9a5f1-61ab-32b1-ac5f-c85ed963506b | -2.292 | -47.99316 | 2025-10-12 04:40:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e020272b-ae3e-3057-a06a-82c44688e48b | -2.26467 | -47.8501 | 2025-10-12 04:40:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d91608e7-7265-3008-8007-7ee11b424392 | -1.89787 | -51.01357 | 2025-10-12 04:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f5abc5b-7e64-3dab-92e0-b737702401d2 | -2.26746 | -47.85411 | 2025-10-12 04:40:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0bad7df1-c0db-30bc-ad61-eab576fe73b7 | -2.63365 | -47.30406 | 2025-10-12 04:40:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8350ad19-5950-36db-8348-d6417d7b50dd | -4.00822 | -38.7293 | 2025-10-12 04:40:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 696ffad0-8509-3e0b-844c-7f0c96443322 | -3.48373 | -41.60215 | 2025-10-12 04:40:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 589be9b5-33b9-32b6-ad79-caf3ada8ca95 | -1.90201 | -51.01021 | 2025-10-12 04:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17550f67-1905-3791-bb00-b9abf7f73b36 | -3.34673 | -42.15587 | 2025-10-12 04:40:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 611729f4-1c91-329c-8eee-779b58420b88 | -0.4322 | -52.07006 | 2025-10-12 04:40:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f71ad07-7140-392f-aa78-ef9cb1209b0f | 0.3692 | -51.11761 | 2025-10-12 04:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 846f2976-742d-3730-ab44-b2d1ad31a8e6 | -1.13441 | -47.80583 | 2025-10-12 04:40:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1113a9d2-315e-3f33-b7d2-4b6a822d8675 | -2.53875 | -47.79991 | 2025-10-12 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 7a9ff400-b407-39dc-9b92-a604e9db0519 | -1.13829 | -47.80288 | 2025-10-12 04:40:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f8254ea-2d20-3e52-929b-911a394e2e34 | -2.53486 | -47.80289 | 2025-10-12 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9e6b2bfd-cc84-3ca8-8473-a7dc10f8940d | 0.25969 | -51.08657 | 2025-10-12 04:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bffc9a9-5e84-3dec-8b82-e9c250545678 | -0.43231 | -52.0717 | 2025-10-12 04:40:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e2dd2af-02a8-357f-aac1-97f8886116fc | 1.84529 | -55.86958 | 2025-10-12 04:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 52439aaa-5600-3bed-bf7d-28d9d65e014f | 0.25903 | -51.08242 | 2025-10-12 04:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 07a0905c-51e4-3f4a-8d5d-51d87d590780 | -2.54544 | -47.80095 | 2025-10-12 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1a9a773d-5430-3b30-bb78-708f5cf69117 | -2.25829 | -49.53022 | 2025-10-12 04:40:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4cfb837-17fc-319e-8bbe-738e1bcf6979 | -2.29534 | -47.99368 | 2025-10-12 04:40:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9da0bac0-5617-3d19-9560-ebba5fac550e | -3.14203 | -44.42633 | 2025-10-12 04:40:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63a0123e-991d-3c67-b1a7-3894d146f2bb | -1.37811 | -48.85268 | 2025-10-12 04:40:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd86f4aa-4691-3e99-a254-8b8f3fad03aa | -1.89849 | -51.00965 | 2025-10-12 04:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9ce9b1c-fb4c-32b1-a014-0894a6586724 | -2.53821 | -47.80341 | 2025-10-12 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| eba37f60-69f9-30f8-84e2-5f005591de26 | -3.14261 | -44.42857 | 2025-10-12 04:40:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e596b4a-c588-3229-9b54-cdb4be459a6e | -2.26801 | -47.85062 | 2025-10-12 04:40:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82707076-b77b-3b32-a8b0-ab2396e41487 | -1.90214 | -51.00946 | 2025-10-12 04:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36a3b906-e73d-31c1-9a2f-49c3558a4434 | -1.38144 | -48.8532 | 2025-10-12 04:40:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9b00ef2-8179-3404-a22b-53993a0c0d32 | -0.42842 | -52.06942 | 2025-10-12 04:40:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e740f012-8fc9-3d61-bf70-76ecaddb45ed | -2.53431 | -47.80639 | 2025-10-12 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 39bd46ee-6381-3ec3-8450-7585d8552336 | -2.29255 | -47.98969 | 2025-10-12 04:40:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44bdaca4-19c9-3fc6-a07b-8787d900ce66 | -2.54155 | -47.80393 | 2025-10-12 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| dd9e6f44-8920-3823-9049-3257e6d6c3ff | -2.31947 | -49.16735 | 2025-10-12 04:40:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47465606-d350-3dfc-aac6-1edc33c4e9d5 | -1.90151 | -51.01336 | 2025-10-12 04:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ff96ad9-8b92-34d0-86b3-4112af7c7a64 | 0.25541 | -51.08299 | 2025-10-12 04:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b95a418-bada-31ad-ad2f-2e696f7e8163 | -2.54489 | -47.80445 | 2025-10-12 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9dd55517-0544-37ce-a3db-c0b8b272c0b5 | 0.26264 | -51.08186 | 2025-10-12 04:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 97058ff2-9479-3c1c-a86e-b8ca23c75e2c | 1.8472 | -55.8485 | 2025-10-12 04:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 307da02b-4e85-30cc-951c-f441b85ba3bb | -2.43608 | -49.37491 | 2025-10-12 04:42:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ee24ea8-0768-3792-87e9-6c61b771f338 | -7.74084 | -42.40553 | 2025-10-12 04:42:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 767236b5-e59d-33ae-b24c-ab21fec81598 | -8.32844 | -46.23855 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de9706e7-2ad7-3f6d-b83e-a6be76426f28 | -7.05159 | -45.21515 | 2025-10-12 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef7d8dc8-766d-38ae-a087-946d5deb1dfd | -3.53599 | -48.92189 | 2025-10-12 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3f060565-81ab-30ab-ab8e-1054e063929c | -8.14875 | -47.09615 | 2025-10-12 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2589d9ad-d579-3611-8017-9a718c3d9ff5 | -7.88053 | -44.45959 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 797deec2-7e33-3937-80f4-909298cd5eca | -3.51638 | -45.84423 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 598c439e-de7a-3dd1-9996-6e9269dd5039 | -8.02245 | -44.45281 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0a6ed0c-0209-341c-888a-1293a93d8594 | -4.66056 | -49.38301 | 2025-10-12 04:42:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9897a15-6b1b-3b8e-b2fc-ffe27d427338 | -6.59318 | -44.61678 | 2025-10-12 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eecab85b-0fe8-3bbf-8e2f-0027e4560b46 | -8.48212 | -46.18673 | 2025-10-12 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fafbe034-921b-3245-a1ae-414ecd98b613 | -8.31975 | -45.93067 | 2025-10-12 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0708798c-f2ec-3e1c-85c2-4e3ce972016c | -4.27001 | -46.9287 | 2025-10-12 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e3b829cc-9c8a-332d-97c6-56085e246655 | -7.04696 | -45.21949 | 2025-10-12 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb1fac43-a10f-3ae8-a1bd-8ef7c21d9f5d | -7.54674 | -43.84181 | 2025-10-12 04:42:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fad8320e-cb43-384d-a6d3-63e712cf0330 | -7.50889 | -44.60836 | 2025-10-12 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 615c18ac-8e53-358e-a5e0-9aae0899cd74 | -4.42368 | -47.75373 | 2025-10-12 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ba363a90-2a3c-3aee-bf44-53a429386ff1 | -5.86399 | -42.84526 | 2025-10-12 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0e401076-3978-393b-8f90-b67e3180a33a | -7.70614 | -42.37298 | 2025-10-12 04:42:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README27.md)
