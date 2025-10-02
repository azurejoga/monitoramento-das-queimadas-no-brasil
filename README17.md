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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b59ab199-baae-32b0-be2c-abf78b1a08a3 | -9.9365 | -43.7657 | 2025-10-02 03:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 162.2 |
| 13e5649a-3744-3bf9-8866-fcc5d80dac8f | -10.8047 | -46.6112 | 2025-10-02 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 90d843a1-b152-35b7-9eef-3d60cbf69cb7 | -5.3193 | -43.7636 | 2025-10-02 03:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 9dd03726-7c41-30c0-af3b-c254e617b1d6 | -12.5001 | -50.2453 | 2025-10-02 03:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| bac73eae-b408-34c7-bb47-9ba359390a3d | -9.9182 | -43.7212 | 2025-10-02 03:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 8972418e-631e-3bc4-a98d-71e8de5d4dc4 | -7.7755 | -42.5152 | 2025-10-02 03:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| c58089fb-5c5a-366c-9b01-fdb5e61044ab | -14.4255 | -46.115 | 2025-10-02 03:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 81072659-6745-3b09-b5cb-cffa28456db3 | -10.8428 | -46.6064 | 2025-10-02 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| a91ce975-f31a-369f-8ff5-522a6d07a158 | -5.338 | -43.7623 | 2025-10-02 03:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 163.7 |
| fd5125cb-1ea8-3d55-ac15-65813aa72a6f | -10.8424 | -46.6289 | 2025-10-02 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| bda33c85-d082-3957-b1b3-3804718fbb60 | -7.7752 | -42.539 | 2025-10-02 03:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 198.3 |
| fedd8545-03e3-3057-9d0b-c77a17d7eb2d | -16.0421 | -50.874 | 2025-10-02 03:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 0d1f0b01-b4ac-35c8-b6a2-9223a7500233 | -11.1746 | -47.2805 | 2025-10-02 03:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 14147b17-ae33-32da-8943-47b322009a45 | -7.7563 | -42.541 | 2025-10-02 03:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 137.4 |
| 083cf036-8ac0-3d4d-bb87-0066a48e9cb4 | -9.9369 | -43.7422 | 2025-10-02 03:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 299.7 |
| 859e3a2a-84ce-34ed-8a74-232f159afb26 | -16.0221 | -50.8989 | 2025-10-02 03:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 52.3 |
| e2febb05-8e9c-30fe-aa5b-8087a88cec6d | -9.9182 | -43.7212 | 2025-10-02 03:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 109.1 |
| 179e2e67-3ff1-3631-a5f9-6cd85272ceef | -11.175 | -47.2581 | 2025-10-02 03:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 6e9e993a-3156-3be0-a588-adaaf55573fc | -13.1739 | -47.8317 | 2025-10-02 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| aa093c13-8a17-3852-b07f-09705860669e | -13.4248 | -47.7945 | 2025-10-02 03:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 380d92cd-f89e-3e5a-8244-dbf8e7d47fe8 | -10.8428 | -46.6064 | 2025-10-02 03:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 1abd513e-8197-3e5d-8b3a-9a68a699348c | -7.7941 | -42.5369 | 2025-10-02 03:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| af979d32-1cf0-3c93-8f12-fd77bcb43dbe | -9.9365 | -43.7657 | 2025-10-02 03:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 163.0 |
| b8be475b-3d8b-319b-ade9-76efac56481c | -9.9178 | -43.7447 | 2025-10-02 03:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 143.3 |
| 5ab7b698-9c04-3820-90e2-bea799be1e36 | -10.8234 | -46.6313 | 2025-10-02 03:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 236.9 |
| 25938d26-9592-305a-b924-5a2e4a6c3a13 | -5.3193 | -43.7636 | 2025-10-02 03:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| b8570a29-e988-323d-92e8-d456e73d87eb | -5.338 | -43.7623 | 2025-10-02 03:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| ba53849f-a195-38be-b525-d45d24cfa368 | -16.0025 | -50.902 | 2025-10-02 03:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| b80ef3dc-9b44-308a-98b1-2ea9138c9160 | -6.6955 | -48.7062 | 2025-10-02 03:40:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 53.4 |
| c2374e94-6b0f-38b6-8823-8c5aaeb34861 | -10.8424 | -46.6289 | 2025-10-02 03:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 2e1e529c-5bc4-3450-83b1-627091b04daa | -7.7752 | -42.539 | 2025-10-02 03:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 271.0 |
| 111b4635-9130-387f-927e-07779346425b | -9.9372 | -43.7187 | 2025-10-02 03:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 185.4 |
| 4092d771-e1f8-31cb-b1c8-1287d6176ea6 | -14.3114 | -45.9967 | 2025-10-02 03:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e2d9c859-63a4-3554-a446-c548620c45e8 | -16.0426 | -50.8522 | 2025-10-02 03:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 37.3 |
| fdeb2ad7-054b-3037-9eac-ca4b2d6c0d89 | -7.7749 | -42.5628 | 2025-10-02 03:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| fe2e2f6a-4dea-397f-82e0-f5abeebd2665 | -10.8237 | -46.6088 | 2025-10-02 03:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 176.2 |
| 214c41c8-fde1-34d2-8462-08f3ae3f7ef7 | -7.7755 | -42.5152 | 2025-10-02 03:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| c072531c-4cb3-3b11-b3f6-266817db35ba | -5.3379 | -43.7855 | 2025-10-02 03:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 1315cb96-b151-38e6-ad04-bc9e22afec2b | -10.8424 | -46.6289 | 2025-10-02 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 4aa1ac8c-9945-3ffe-84b8-1bdc6054f29f | -9.9369 | -43.7422 | 2025-10-02 03:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 271.6 |
| 6bbbd5b8-cf85-3213-9b05-18640b4c7b90 | -13.4248 | -47.7945 | 2025-10-02 03:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| c5af7fc0-a5ca-3bda-a089-c475e9fdc635 | -16.0021 | -50.9238 | 2025-10-02 03:50:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 1bcc9a2e-0902-32c6-9634-121431268d1c | -14.4753 | -48.436 | 2025-10-02 03:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 105.0 |
| fb9ec952-9fba-3199-a36e-fc4d3fabc77b | -10.9953 | -46.5869 | 2025-10-02 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 36dff0a9-9e06-38e8-8f22-401bdf33a375 | -7.7749 | -42.5628 | 2025-10-02 03:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 96dbf34f-6358-3ad0-9db2-5977aafab094 | -7.7944 | -42.5132 | 2025-10-02 03:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 11e25858-12d5-3b93-b6bb-cfc3cc84373f | -9.9365 | -43.7657 | 2025-10-02 03:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| 853a4659-7efa-38a1-b087-e26676953428 | -11.1746 | -47.2805 | 2025-10-02 03:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 35960bfe-8055-373c-9218-fb335fe8605a | -10.8234 | -46.6313 | 2025-10-02 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 164.1 |
| c68e2079-55a2-3192-be55-19540978210b | -7.7755 | -42.5152 | 2025-10-02 03:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 6c4c8e9b-bd97-33f6-9ff0-d2e23d7bd5f5 | -7.7563 | -42.541 | 2025-10-02 03:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 330b797d-5fa0-3599-a134-7b7dedffba70 | -14.4947 | -48.4329 | 2025-10-02 03:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 5ec3373a-3b94-390f-a684-d48b938f7831 | -16.0025 | -50.902 | 2025-10-02 03:50:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 30779b56-7d59-3f70-8902-c53428d83f8f | -6.7213 | -44.1387 | 2025-10-02 03:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 5b802cbb-f2a2-316d-a445-f1f69c3b6053 | -5.338 | -43.7623 | 2025-10-02 03:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 190.7 |
| f588ed63-1a8d-3a47-8bb3-54e237a4ff72 | -14.4757 | -48.4137 | 2025-10-02 03:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 32ca3d1b-4d98-3a28-b410-7fa70f30d123 | -10.9949 | -46.6094 | 2025-10-02 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| b8812038-a7db-332d-9c2d-cd6afdebb72c | -15.9829 | -50.905 | 2025-10-02 03:50:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 7d5f4c55-cfe6-36df-b40c-4b94445bd0e3 | -5.3193 | -43.7636 | 2025-10-02 03:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 851230f8-8f41-3a87-886b-c94374b34ed6 | -13.8156 | -47.5332 | 2025-10-02 03:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 32bad896-2b0d-34b3-b197-6eeb0ba08c0e | -9.9372 | -43.7187 | 2025-10-02 03:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 176.3 |
| e772a729-9484-300d-973f-8cca3df05610 | -9.9182 | -43.7212 | 2025-10-02 03:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 133.5 |
| 372649b9-29b2-377a-9a27-39be993e499b | -14.3114 | -45.9967 | 2025-10-02 03:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 16b75343-ab0e-3f58-b229-3b4f4621398f | -16.0029 | -50.8801 | 2025-10-02 03:50:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 09fae879-8d9d-3980-a85d-07c143d970fc | -16.0221 | -50.8989 | 2025-10-02 03:50:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 510894c8-4db0-30bf-bdb2-3bc69e31291d | -10.8237 | -46.6088 | 2025-10-02 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 81e4dc42-35c7-3efc-b8f3-35e661bfa9c6 | -7.7752 | -42.539 | 2025-10-02 03:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 193.5 |
| 4033b859-1d6f-3abe-87c8-acb519c181f4 | -9.9178 | -43.7447 | 2025-10-02 03:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 200.0 |
| 98d34125-00b6-3b0e-a5c3-3df6322a6949 | -14.4753 | -48.436 | 2025-10-02 04:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 2d18bcc6-9b76-3f1b-80d4-416cb2d2f8a1 | -9.9182 | -43.7212 | 2025-10-02 04:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 102.1 |
| 7df6a789-fcab-36a4-bdb2-0ce5d8de4e86 | -14.426 | -46.0919 | 2025-10-02 04:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 839fd5f8-2cff-3c23-9e77-19f5e850e452 | -9.9369 | -43.7422 | 2025-10-02 04:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 297.7 |
| 7f15a536-bf93-36f3-9c08-18eff4e0452b | -9.9365 | -43.7657 | 2025-10-02 04:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 105.7 |
| 64dc2a8f-b62e-328e-bcf2-70bb65035d85 | -9.9372 | -43.7187 | 2025-10-02 04:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 212.2 |
| 2b7afe5c-d47d-31f9-afd1-fbe69676f3d1 | -14.4757 | -48.4137 | 2025-10-02 04:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 19b9a1ed-2d46-3e30-976c-f74c37c981f8 | -9.408 | -47.5963 | 2025-10-02 04:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 16aeb332-b860-3697-a70b-819d54a07ce2 | -10.9953 | -46.5869 | 2025-10-02 04:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 81a59f26-3e83-3ac0-9a64-e62dfa4b9927 | -9.4083 | -47.5742 | 2025-10-02 04:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 8872d6ed-3ca3-3321-a7d7-78c8df2ffdaa | -13.4248 | -47.7945 | 2025-10-02 04:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 009f3d1f-a731-3ea3-9cce-0222ebe93ae1 | -14.4255 | -46.115 | 2025-10-02 04:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 1d191d29-1ffe-3488-b537-7e1031bd698c | -11.175 | -47.2581 | 2025-10-02 04:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| dc563a13-6801-3059-bc25-2caf75d30c9c | -14.3114 | -45.9967 | 2025-10-02 04:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 2617fdda-68b9-370c-912c-785d63607fa7 | -7.7752 | -42.539 | 2025-10-02 04:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 204.6 |
| 2abb1fbf-c86d-3f98-8d5f-2758259836d5 | -9.9178 | -43.7447 | 2025-10-02 04:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 134.5 |
| 16a72ac2-f157-3884-8d07-2db0b516eb48 | -11.1746 | -47.2805 | 2025-10-02 04:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| fd2493bb-aa7d-3943-8a44-2723c8501b53 | -10.9949 | -46.6094 | 2025-10-02 04:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| f9c99d04-cc5b-355d-a472-d66d4ec2a437 | -7.7755 | -42.5152 | 2025-10-02 04:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 02ba5472-453b-35ca-9b26-1543a5cf699f | -5.338 | -43.7623 | 2025-10-02 04:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 132.9 |
| f4eb6484-f5dc-3b88-8eff-57844534d3f1 | -4.05476 | -49.0768 | 2025-10-02 04:00:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88a4f5d9-4516-393c-a3e6-c28c5f0fce63 | -2.2671 | -47.85103 | 2025-10-02 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24a3c4b1-4a90-3d80-b5eb-17b5bbfbc87b | -4.42716 | -47.7583 | 2025-10-02 04:00:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cb7cbb72-5a61-301e-8fba-7bc4526b72ef | -2.59497 | -48.12109 | 2025-10-02 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f42917d3-1776-3b0b-8fce-e1f9434b6338 | -2.24478 | -47.88931 | 2025-10-02 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fac7f88d-8a82-3633-b163-dd7d2ead34af | -3.35076 | -43.19242 | 2025-10-02 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d8554be0-23cd-3bed-9864-79f5e4d2fead | -5.71451 | -42.68391 | 2025-10-02 04:00:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d5336df1-15cd-3ebd-832f-6dd374125255 | -4.45903 | -43.62041 | 2025-10-02 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c2468eb-7b11-324b-a5a9-a528adbd01e3 | -4.86594 | -47.40732 | 2025-10-02 04:00:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97297e75-8a08-3969-83c5-d5c1a00cdb43 | -2.42831 | -47.1427 | 2025-10-02 04:00:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 43e317e4-6f3c-3260-aff9-296142022f45 | -5.81564 | -42.84486 | 2025-10-02 04:00:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c6f8be8e-1499-38bd-a48f-917c04e2ff75 | -4.11489 | -47.93347 | 2025-10-02 04:00:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README18.md)
