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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c4cfb70-f830-3584-830d-7df0284fd48d | -7.00426 | -60.69177 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e52dffde-f2c9-36ff-a5e4-c6875bd0669f | -7.00256 | -60.68045 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b56d5b7f-4c57-345c-ad54-101e34ae2c3a | -6.99303 | -60.69745 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b14ad0f5-b735-3f0d-9525-95d12146c0fe | -8.57579 | -62.43748 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b14cfabb-eb8d-3a0b-93e0-dd99f58ddc58 | -8.5747 | -62.44442 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a88c3a9-f45d-366c-a57b-87687e840df8 | -8.57303 | -62.43348 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b3b776c-8b65-331d-862a-a6e4a02957ae | -8.57248 | -62.43696 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49423159-7aa5-3570-a40f-d9f55a9e70de | -8.56972 | -62.43296 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae5307ad-906a-304f-a4ef-6605496b6b97 | -8.56917 | -62.43643 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c231803-a1cd-3070-9228-4a39cb3b30ae | -8.5643 | -62.48905 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3d5b10c-bc7d-3c0d-bcf4-88d3ee517911 | -8.56154 | -62.48506 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3a0eb4f5-0190-301b-a854-14d433bc3156 | -8.56099 | -62.48853 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09996d50-c3a1-3886-b456-e4d851168d6a | -8.55111 | -62.50831 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c1fd985-fdc2-3ad7-904d-e8ccf0212a16 | -8.17097 | -61.39642 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f7dd21c-b612-3e73-90a3-d4ba248f805d | -8.17043 | -61.39996 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5c18444-0ab7-3fe9-b91c-7dad8afaf345 | -8.16818 | -61.39237 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45c6bedb-91ed-3d7e-b51b-472c4969a237 | -8.16764 | -61.3959 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e119b461-7893-3fb1-b895-fb641d00d36b | -8.16709 | -61.39944 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58b6b66e-158e-3dbc-8606-b1d37291a097 | -8.16577 | -61.54007 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a0f82a9-924e-3e4b-bab3-fd76e1388f79 | -8.16485 | -61.39185 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a33731c-0b84-3bc8-86a7-2220fbf5fd3a | -8.1643 | -61.39537 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a4cff68-7a6b-38ec-96e4-ff85703f0f7b | -8.16298 | -61.53604 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de6ae939-9886-32ea-b910-8f903cc1bd36 | -8.16096 | -61.39486 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9ec55e0-1a78-3829-ab50-3491bbd2c942 | -8.15741 | -61.52796 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3090c1c-8b9b-391e-b8c5-b5b7c51d25ee | -8.15349 | -61.31025 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5fa709d2-c656-3ffe-9636-62c353f96231 | -8.15178 | -61.2991 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ef7a895-2c12-30a2-b197-50b9ca312453 | -8.15124 | -61.30265 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee5a1cdd-1a03-3201-a876-fb1ac1237233 | -8.15015 | -61.30974 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 529e6bec-c55a-394b-a709-837a83ab58bf | -8.14953 | -61.29148 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4bf4743-fb64-3246-b863-644d0b32dd6d | -8.14898 | -61.29504 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a8e3892-540e-315f-b67a-85ddee7ede86 | -8.14318 | -61.39933 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 661ae754-6fd7-3dd9-ba8a-e2a93ec8357b | -8.13521 | -61.34007 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f82ab36-8d84-34f7-bc93-45d7f87f9eab | -8.13246 | -61.53493 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfda0bea-f1f6-3378-aad2-13f82f126101 | -8.13187 | -61.33955 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 18f39c7c-9c51-383c-8465-fe13b390f709 | -8.13172 | -61.29598 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 429734c7-219f-39b6-8244-f5a87f8611ac | -8.13132 | -61.34311 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e96fe966-3731-3965-b30b-705b92e2c628 | -8.13078 | -61.34665 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cc4239d-0b07-3a6f-bc57-2099030876e7 | -8.12913 | -61.5344 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0dc3ca7-eb81-363c-be10-2cb824d0318a | -8.12798 | -61.34259 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 07bce06f-5636-381f-bb76-ff9cdbb740b6 | -8.12783 | -61.29899 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afdb07f8-8960-3485-a098-97e90af04860 | -8.12744 | -61.34614 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18b539fb-11f3-36d2-909b-3b7d276fbdb4 | -8.12689 | -61.34967 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33af6d4d-1fa7-3176-8370-4ad10f99f37c | -8.12675 | -61.30606 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3936bc52-cbf5-3c3a-8ca1-d509b7a697a9 | -8.1234 | -61.30554 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07cbffca-6682-3be6-a2cb-28463abba70b | -8.11952 | -61.30856 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3eb600e-43fc-35e4-9bf7-a2c7ce8a6e46 | -8.07815 | -61.29502 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 104a4be1-d9b4-3205-811e-31589d4e2aad | -8.0776 | -61.29856 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df3a9bd9-e812-3f52-a743-31e9bf63f65f | -8.07371 | -61.30157 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e5d16b2-2890-36ff-bb3c-44330f3ad2e4 | -8.02228 | -61.4132 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcbd3518-5b3e-3363-b51b-b88967470efa | -7.99514 | -61.43426 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6048638c-9450-3195-a7e2-b159a7bb9da6 | -8.4511 | -61.538 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67bc9022-86c7-316d-9564-dfc07f8f3a12 | -8.43389 | -61.53893 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8cef26c-becb-37be-8b7b-02d51c9052c7 | -8.43334 | -61.54246 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33a52c80-9686-3b32-a6aa-42cd92460a2b | -8.4328 | -61.54598 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90d4841a-71b5-3295-9383-a387d149a13c | -8.43225 | -61.54951 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2dc4260b-3f6e-3295-a1c8-c2075be44d06 | -8.43001 | -61.54193 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f20c9701-20a4-3c6e-850f-d7d06026451c | -8.24098 | -61.42567 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96099378-b30d-3fbb-a6a1-6852bce8de28 | -8.23348 | -61.51845 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0619fae4-c7d7-3d41-8c8a-c2b7fd4afe63 | -8.23015 | -61.51794 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3db55f1d-e509-36c6-940c-bebd95dde456 | -8.23008 | -61.49627 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d1acbcf-9b20-3819-b1af-fe44fc1a7768 | -8.22845 | -61.50685 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5267b90f-ee5a-3b4e-8655-4d3540a1a9c2 | -8.22675 | -61.49574 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70137489-036f-3f07-9477-a41313f97b1f | -8.22621 | -61.49927 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3db0a27f-17a3-3543-8282-9a11c8824bfe | -8.22566 | -61.50279 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0eefb250-89f3-3959-9c6b-312688fdf664 | -8.22512 | -61.50632 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29bf7821-0dc8-37bb-987c-5f773d9225cf | -8.22342 | -61.49522 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bbe135f-3b6b-3b01-b89c-ed9c55879736 | -8.22287 | -61.49874 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 644264f3-b01b-32d4-bd20-662b4f6dc24d | -8.22233 | -61.50227 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 306e6b2a-3bfa-300e-bd2f-cb83dde1063f | -8.2204 | -61.34241 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4efb8876-d5bf-3a19-914e-03e48724972c | -8.22015 | -61.51638 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33933ebd-aab5-3204-9b5d-c7ec94ae7009 | -8.22009 | -61.49469 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4031d634-85c8-3f78-82c2-809d345c9f77 | -8.21954 | -61.49822 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb554d09-3be1-3407-b2fb-a0fff3a39705 | -8.219 | -61.50175 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0795fdb-cfe6-303e-9072-de5eeb6bcfd7 | -8.21846 | -61.50527 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2762cd2d-e74e-32aa-8b5a-bda832dddf64 | -8.21791 | -61.5088 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28139440-49b8-3d97-88a4-944fe0be4a64 | -8.21675 | -61.49417 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8685793-72c7-3d2c-8499-0256ef53d760 | -8.21621 | -61.4977 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a8d6f84-de33-3c5f-b9cc-915cb0d75747 | -8.21206 | -61.35201 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0853ac0d-1345-3552-ba8e-f58b5327b44c | -8.20102 | -61.40108 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a39667e6-8e39-33d7-a79d-05f7f1b148bb | -8.20047 | -61.40462 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e261559f-f612-3a03-ac6b-248d291ff8cf | -8.19768 | -61.40056 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0506ba90-519e-3d6b-b092-5f22b7934f3c | -8.19497 | -61.17445 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5a23ae8-6b5e-37cf-9a8d-94ab3164f1fe | -8.96449 | -62.16743 | 2024-09-27 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cf02b93-c2a6-3b43-a9d4-5e5a34e537e1 | -8.95883 | -62.18111 | 2024-09-27 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4229344b-3bb6-34cb-b22d-2d409767aee3 | -8.95829 | -62.1846 | 2024-09-27 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bef9e727-2d0f-33af-81b5-f450b7988716 | -8.95552 | -62.1806 | 2024-09-27 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f690c08-b2dc-3645-9433-c20f3ab4bb04 | -8.94999 | -62.17257 | 2024-09-27 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16ad16c0-fa9c-3281-a267-80b170a46a44 | -8.94668 | -62.17205 | 2024-09-27 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80b90e71-9249-3a34-9feb-49c23294cfd2 | -8.9317 | -62.13752 | 2024-09-27 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 006f49a5-a980-31e8-ba37-8435d605b1ca | -8.73271 | -62.02012 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 498f6803-e5dc-3df3-844b-9d4039efe5e2 | -8.73216 | -62.02361 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ebc23e54-685d-379e-8bdc-ae327877a08a | -8.72885 | -62.02309 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6bb6bd11-d172-3a51-96e9-588c10505e75 | -8.54559 | -62.02251 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e74f566-29b7-3a8c-8afc-937e626ea312 | -8.54282 | -62.0185 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a3589d5-8613-34fd-843a-8d21cd427c3d | -8.54228 | -62.02199 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 192fa7c3-e319-34c5-972e-81209d6bb1f8 | -8.5406 | -62.01101 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b2e3104-f224-3a62-a950-2cc19d7cc1fa | -8.54005 | -62.01449 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a0de6a1-53e4-3448-af6c-70daa775c184 | -8.53951 | -62.01798 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab2c5f85-a810-3c6f-bb88-89aaa9beaa7b | -8.53728 | -62.01049 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecc0d55a-46bd-3276-94b0-ea56178348df | -8.52081 | -62.05075 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README124.md)
