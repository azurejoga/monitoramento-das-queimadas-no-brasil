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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4dce22c-a137-33a6-9862-56fcea275d49 | -6.7975 | -59.60434 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ef2219e-4f2e-364c-b01f-9607c1b6eea7 | -6.15304 | -57.94138 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bdc5bfda-7813-31b2-8cc0-3165b4df9807 | -6.61376 | -58.39262 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f21b3d6-47a1-3f30-a87a-fe69f378c09e | -6.81854 | -58.65415 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ed685ac-106e-3fa7-8b6f-a7ee35b65d62 | -6.6326 | -58.50731 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0f720a50-6938-3687-87da-13850643a5c5 | -6.13933 | -59.91708 | 2026-08-25 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b3c938d-fae9-3c65-ad11-0a3697997673 | -6.64099 | -58.49294 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2c4538b2-4065-389b-ba61-991922cbc46e | -6.13932 | -57.84845 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d03a9435-ff29-3fdb-8ca3-7b1832954231 | -6.76726 | -59.44613 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ced6b1fa-dd60-3c5a-b26f-570b3bf30c8d | -6.61448 | -58.3874 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 468b09fa-b6a2-3439-bfe4-2f9d67f98ada | -6.60884 | -58.38112 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b385ef23-207c-3720-9cc8-aca3ff7a52f4 | -6.71875 | -59.44369 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d00ee93-6ca1-3ea8-9f1b-593c61aa46c8 | -6.14654 | -57.94025 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e1b04802-7a1a-3130-88a8-11f0a85f9d7d | -6.82412 | -58.66041 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 34d49151-449e-3650-b119-3d88af3f1744 | -6.80833 | -58.65857 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a6f9f028-ed2c-315f-b819-ea0277499fb5 | -6.68627 | -58.72504 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7133f9b-86e8-3101-b85b-79d3be71126e | -5.78857 | -57.61653 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8824bece-3954-3ad9-b62c-bf9082e5b39d | -6.72412 | -59.44909 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb7600fc-0226-3d3f-bf8b-b6319064f7eb | -6.63961 | -58.50323 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 23234a78-d8f5-3b72-9e60-d5e9ae0861b1 | -6.62761 | -58.49624 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 17d24e41-e041-3722-9edd-cf6ff73ed60d | -6.81586 | -59.60276 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5b509a0-3ba6-3b7b-a708-bf1b752cee22 | -5.77021 | -57.55507 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb042e48-5d32-339b-b461-24fe6bf540d5 | -6.63327 | -58.50229 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 253fba97-4377-358d-9a66-1f71a80fefd9 | -6.63531 | -58.48705 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fb0e8234-fc39-3200-b4df-7f7650218bcf | -3.38984 | -59.56911 | 2026-08-25 06:05:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 452b3c61-1fa7-3791-b5f4-7d706b36fc86 | -6.8041 | -59.68913 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4107df68-4170-3dd5-a182-b5304b25fb14 | -6.62621 | -58.48933 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5ccf0c54-b786-384d-b2ee-07fdbf9cee77 | -6.63395 | -58.49722 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 60658d86-4430-3468-8e89-43710e8968c4 | -6.62897 | -58.48606 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 61146fc3-3c6c-32a8-b15d-4731e28fb46c | -6.13877 | -59.92109 | 2026-08-25 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c23b94b-cc82-35f4-a1cc-f21a859ec13f | -6.68995 | -58.72878 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ea1d9a5-d2bb-3e41-853f-9f0e0f70bf11 | -6.80578 | -59.58789 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a04c0d3a-e174-39fa-acb0-d74778d95ea9 | -6.79925 | -59.59141 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3ba34b1-406c-32fe-80c0-1f12b44b30ed | -6.14454 | -59.92187 | 2026-08-25 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ab3e7eea-007d-37dc-b5b3-576377b1f37c | -5.79367 | -57.61385 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b9b846db-e223-3363-b34f-ca5bad490026 | -6.71815 | -59.44813 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4f36206-19ba-3a3a-ab8b-2eb4b3670579 | -6.1451 | -59.91788 | 2026-08-25 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| af682f63-7469-3e26-a9b8-ef356d112c46 | -6.14656 | -57.69873 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0263b6a0-21cc-3a59-a62f-0c3d1022cbd9 | -6.12426 | -57.81205 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d33cb92d-f169-33d9-abc0-882772ca597f | -6.80999 | -59.69003 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa9ef055-c1bb-3ca6-b8ed-f5d7c318daa4 | -5.78939 | -57.61079 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 121d2bb7-296d-33fa-b985-4b1e4ed4c288 | -6.80458 | -59.59673 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| affca18a-9b99-3383-acf2-16b4c5b34169 | -3.13505 | -61.188 | 2026-08-25 06:05:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c33579f1-53f0-33da-b238-96853e087840 | -6.804 | -59.60104 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10e35368-81f5-3b21-a9e3-4dc11fd1030b | -6.63463 | -58.49215 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 67c44a2d-c9ac-393f-bf85-f46cdef9d693 | -6.79373 | -59.80883 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b943c263-5806-3770-af1c-7e3c2255c10e | -6.80762 | -58.66367 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4854e0c7-dbe7-3eb5-ab5c-56f4cc6aefce | -6.63601 | -58.48186 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee8fd6fa-d260-39ac-bbb1-fea871d2a502 | -6.15168 | -57.94912 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8445f5b4-3c5a-309f-a692-245e5762c944 | -6.60954 | -58.38788 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2415ca06-e392-30c3-8ec3-ecc68931f79f | -5.78783 | -57.60704 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 207f7e40-cd69-3b84-862f-c67b18a65f10 | -6.79314 | -59.81313 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4109334e-ccac-3f3c-9bcf-be7c81703fcb | -6.13008 | -57.81847 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8ea9e142-fe22-3174-bbac-4f9f7287df0d | -6.79257 | -59.81727 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e648f0a-f37f-3edc-a455-82e5e60ef285 | -5.78706 | -57.61274 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f8a38ce5-acb1-3382-9882-f318835a2236 | -6.86009 | -59.41266 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a05f327b-800f-3b34-95a1-e773bb16c082 | -6.81051 | -59.59763 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ccd953e-60a0-386c-b305-1484c116281c | -5.77415 | -57.55797 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cec85ead-8ad7-39c1-8c00-3ea200513a41 | -6.132 | -57.85301 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef4d1207-1606-3e09-a507-e70d9bbd1e21 | -5.94188 | -57.73447 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f737332a-2370-3a46-84b4-9ed85c2631f0 | -6.62829 | -58.49118 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a8dd2d0c-6c46-3911-b0e7-228bb74f4ff8 | -6.81111 | -59.59325 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 675931c0-2303-3281-b0d1-8f3e96a347b8 | -6.6255 | -58.4944 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 79d6c7a7-1083-377c-9107-3d9567e24cd9 | -6.1293 | -57.82411 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c717736-23e5-3cdf-ab43-11682349463e | -6.80637 | -59.58354 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 275e1c1a-86b1-3447-afc5-caab016ccf09 | -6.8873 | -59.0293 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e74f70e9-d331-3640-a62c-cea1039a41e2 | -5.77493 | -57.55214 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f132750-c560-37ff-a54c-3c79a2018ba2 | -6.15227 | -57.94687 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 315b2763-f552-3265-951f-2e3f820a03ad | -5.94366 | -57.73229 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47339416-89ad-3482-be11-accb6b385546 | -3.10427 | -61.22663 | 2026-08-25 06:05:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d0abdc8-4f42-3606-b2e4-ba864aad6aa2 | -6.12352 | -57.81744 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| f0dc25b0-e854-3b78-8e67-d1499ac7bb63 | -6.79222 | -59.64346 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42e02b96-133c-3710-b219-73e8ee6fff76 | -6.85347 | -59.41628 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 80ed39ac-b763-3cea-8159-7e20a3fc4fee | -6.81702 | -59.59428 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8d802fd-befd-35e9-82cd-8962670bde58 | -6.6159 | -58.38899 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9eae6149-6484-3dc0-8ace-1e844e13579a | -6.14497 | -57.71029 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e2f1b46e-e7c6-354a-8929-612be16428fa | -6.1459 | -57.94263 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fc129682-b4d4-3056-b24a-8432cfea2899 | -6.14576 | -57.94586 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d200ee0-6cd2-3ca1-8c28-f6bc1fdd99af | -6.81644 | -59.59856 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6203dfd5-7e37-3b95-9d2d-43ab536677f7 | -5.77684 | -57.55611 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b838da5-e5be-3ca6-b278-4e19fdef5cbe | -6.1524 | -57.94373 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a48f774b-2227-3085-880a-a5f3bf989ac5 | -6.72473 | -59.44464 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 944e9185-c359-3e63-a2d9-dea356025dcf | -6.81923 | -58.64893 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7c9ab03-8e48-39e7-852e-9597dd0c0a3f | -6.8935 | -59.02994 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8e24c80-3df9-3f52-a6e9-fd1308a2133f | -6.77325 | -59.44697 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eed79e7f-b212-3ba9-9e3f-29217eb91fc8 | -6.78746 | -59.63402 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 725061c9-3dc6-3584-b583-0ca21d2f06a8 | -6.01227 | -57.66151 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 85833e63-cba5-395b-b689-74c6d1cd4b98 | -6.14574 | -57.70465 | 2026-08-25 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a76990e7-76c9-3239-91b0-7b68ff95b5d5 | -6.7928 | -59.63916 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90f3c61d-eefd-31d4-a937-a080266e6af2 | -6.80461 | -58.66236 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 618f50f5-7f94-36ca-a5c9-0d42a2f6a6f2 | -6.86071 | -59.40815 | 2026-08-25 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 18188026-059e-3541-a0de-02bb15af7ca6 | -6.82483 | -58.6551 | 2026-08-25 06:05:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d018217-0545-3044-a0e6-fee6f5d0073e | -6.98894 | -59.24659 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 83d0670f-fd3b-3628-883c-a143a28bcbfe | -7.53593 | -61.35978 | 2026-08-25 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b137143-8f7b-3762-9ef9-1a5031ac9601 | -6.9683 | -59.07905 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 466cfcc6-86cd-33a9-8dbf-41581a8b3acf | -7.54128 | -61.36048 | 2026-08-25 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b29a0c76-034c-34da-bd36-cc1d075e1486 | -6.99307 | -59.26178 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 41b51ed6-26f8-3e32-b81d-f52e309b6244 | -7.01323 | -59.25036 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 447c3cc4-d700-3aa1-aa99-eb4bc635588a | -8.81998 | -62.33745 | 2026-08-25 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a83b9d3a-03ab-3973-97fb-7f2a9b84cb66 | -7.21542 | -60.62084 | 2026-08-25 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README67.md)
