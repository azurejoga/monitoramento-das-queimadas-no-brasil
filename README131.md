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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa592029-7428-3416-9808-2bee06fc0359 | -2.97833 | -53.87363 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b482c05-1f11-31ad-a981-0f6049c192e6 | -1.64538 | -53.87602 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| b0d65a8a-fe65-314d-9a6f-f4ff019bb006 | -3.27023 | -50.20802 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| af872aaa-1030-356a-ae55-5d296644639b | -3.73286 | -54.23238 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d3ebe990-e8ca-35e8-b2ee-3699f3ae00f5 | -3.31575 | -50.02853 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63f5199e-41f7-3f43-82d5-6e9bd2a1e625 | -0.96132 | -51.65801 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2e9c30a-167b-3259-9935-8044c1b69ead | -1.38523 | -55.02271 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 735c96d8-5ef4-347c-9a6a-ad1c55c4438e | -1.59671 | -55.55398 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d38669d2-fcbe-39e0-be42-901cddf3a8a9 | -1.09774 | -53.39601 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4a37c7a9-a331-3507-b2b4-e12dae44db1d | -3.34472 | -50.74778 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3821cf2-8b9f-3a8d-8605-049085104e42 | 0.93489 | -50.74199 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 944c4728-2243-320b-b5a6-23349e7486cd | -3.59306 | -50.3631 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5c528f4-1a2a-3164-bb7f-025c80253af5 | -2.32629 | -54.50698 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b5bba85-bf50-3932-95cc-ae59dc8dd60f | -2.97521 | -53.89379 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8140ccd1-579b-3176-9687-ecfb7ac1ea58 | -3.39038 | -50.32411 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66f23c35-6a25-3465-9a33-4751a7886fb4 | 1.28121 | -55.91339 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 75e74bc6-d1e6-32c9-99f2-6d7796587f54 | -1.26613 | -54.54935 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f0ad3c6e-a54f-3051-afc3-873c5a3d7a16 | -3.29312 | -53.83306 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b03cde5f-76b9-3e15-9e47-d9225a24bdf7 | -3.11307 | -53.76197 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f817e558-6a72-3aba-aff9-d9e1d24f5ca6 | -1.08474 | -53.64204 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8882e2a-02cf-3e8d-8056-2c6c55ca8cf3 | -2.84618 | -54.02975 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac3161c8-f0c3-3bcb-925c-d5b587e6fb40 | -2.90119 | -54.77287 | 2024-11-30 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e33a635b-79bc-3937-b99a-f50c1737150d | -3.7709 | -51.6828 | 2024-11-30 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c06adc6-040e-37f4-bbb8-d88745ecc96c | -2.82669 | -54.0319 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 653817cf-073c-3726-b7c7-1d4cee8ef678 | -2.32885 | -50.67145 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cfd9469-3b27-367b-9077-d4e7a7cf33ea | -1.20113 | -51.74386 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1bbb183-d35a-3a3a-ac9d-2587149bdbbc | -3.74168 | -54.67625 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4132f70a-b880-3cf9-b923-e8207c695189 | -3.83063 | -50.1433 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 117933d8-65b2-37cb-a9ae-70930edd07c3 | -1.4487 | -55.1974 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 521b5ddd-d5dc-38c9-b9e3-08f8b2284358 | -1.35746 | -55.64652 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 372af456-b724-31d6-b0c2-4ca4442a988b | -0.57506 | -51.6963 | 2024-11-30 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc2a7ca8-e7ba-39b6-81ef-4119f183f133 | -1.53057 | -51.62407 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6396c78-7a63-3cf8-a54c-f0e03e6dac40 | -2.61594 | -54.21107 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2231220e-c90d-357e-b233-d00c984a230f | -0.26161 | -51.50171 | 2024-11-30 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1935853-8930-31a6-afad-c72e525fe96d | -2.86275 | -53.9996 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 845d18d5-2116-3fcd-bbcc-613fdf5b729f | -3.2157 | -54.08819 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01dcce3c-54ab-3be6-9b6b-ffb4f38eba03 | -1.69173 | -52.45681 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce94a53e-c41c-3b7b-aa4b-f315315c044f | -1.7368 | -52.31354 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 935f35d2-7af5-3af3-b27f-79b809c82e95 | -1.83256 | -54.52207 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a1c30598-6aba-3bc0-bbff-6837443d3dd3 | -3.11185 | -53.10694 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6291c9e-9810-3bf9-88f8-83e1b4bc883a | -0.09357 | -51.75064 | 2024-11-30 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26788b4d-2de6-329a-82b5-4e78f8d1a70d | -2.97598 | -53.88878 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2124f07a-e2ea-3493-9eae-f39e036a4cb9 | -9.27832 | -62.3753 | 2024-11-30 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5fdc56ac-35af-3716-82da-a8ab525b757d | -8.50831 | -63.40025 | 2024-11-30 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 708e1f63-244a-37dc-8961-5da650977dc5 | -8.64148 | -63.46179 | 2024-11-30 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 313e2ade-186d-3fff-8a66-47047f2836fc | -7.92543 | -61.55717 | 2024-11-30 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c35c578-185d-3d1e-a99f-b68432e66293 | -5.18303 | -60.26206 | 2024-11-30 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f69850a7-1c93-3a73-9c74-605d3c4d16c3 | -10.19343 | -64.24761 | 2024-11-30 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3408b2cc-ccad-351f-95c1-1fcbf39cb8dc | -7.89509 | -63.26202 | 2024-11-30 05:29:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df0949ca-3761-3e5c-9188-57cae0f959b0 | -8.66574 | -63.47647 | 2024-11-30 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa5e2c80-ecd5-333b-88de-d2a48fae45d3 | -9.20456 | -63.61423 | 2024-11-30 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f17f04a2-91b5-31bd-966c-0ecb47ea4b0c | -9.83551 | -63.36562 | 2024-11-30 05:29:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e45fab0-0f34-3c51-8314-7f9f861ba8af | -7.69989 | -61.06488 | 2024-11-30 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70263526-6c0c-3d09-a5e1-62e9d49f3c11 | -9.35658 | -66.4957 | 2024-11-30 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 544bdf13-0445-3a2b-9dfc-93aec10464fb | -9.738 | -63.03818 | 2024-11-30 05:29:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27492c77-6c8b-32e5-8083-1e35215598dd | -9.41275 | -63.22515 | 2024-11-30 05:29:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9bda431-90fa-35fd-b27a-d673e39a3d18 | -9.64325 | -65.73891 | 2024-11-30 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b5002e8-4c32-338b-ac8a-d33f57aac44d | -9.20122 | -63.6137 | 2024-11-30 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faa5def6-80f2-3cfb-8325-45f530214163 | -9.50944 | -63.1729 | 2024-11-30 05:29:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1714bd60-b7aa-3ae9-95ae-eb07e6dc1bab | -7.08998 | -59.7869 | 2024-11-30 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8dc7ef8e-2f77-3e3f-bf9b-7d82da7ab8fd | -10.18764 | -59.53035 | 2024-11-30 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9ab986f-0882-3705-8829-e327a57bee07 | -8.54715 | -63.41376 | 2024-11-30 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2a189d4-0de1-393a-8ae6-3ab2ebb77f50 | -9.63679 | -64.19801 | 2024-11-30 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b919258c-54fe-32ab-8ac6-9a16ad3c98bd | -9.1868 | -63.74612 | 2024-11-30 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e62477c8-1d35-3619-8c0c-dbb3c47f1014 | -10.257 | -62.21735 | 2024-11-30 05:29:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6c386075-51f6-347f-a96f-07dc1dac793d | -8.50498 | -63.39972 | 2024-11-30 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ef95a6e-6b35-3f3e-99d5-706906ab65f6 | -8.13957 | -54.86218 | 2024-11-30 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2600dd46-cfa8-3c75-9534-a0e05318739d | -7.21592 | -59.86039 | 2024-11-30 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec53ee60-1a88-389f-8d53-ff8fec9fec31 | -9.9013 | -63.07864 | 2024-11-30 05:29:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 404ef061-d9f7-33d4-bcd6-e1b913c15201 | -5.18641 | -60.26259 | 2024-11-30 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b4db4fd-e5bc-3be3-9013-290385e99430 | -9.66113 | -62.87898 | 2024-11-30 05:29:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb124775-3d31-3ac4-91b1-926174e1b979 | -7.59089 | -63.23183 | 2024-11-30 05:29:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb76e186-566d-33b2-825c-2e6e0b72d16b | -16.25208 | -59.95959 | 2024-11-30 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 626f48a0-3205-336a-9ac6-f8f665a6ddee | -6.00353 | -57.83781 | 2024-11-30 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae909ae2-2762-3bbf-8e61-e3e24cfea10f | -9.82346 | -63.24878 | 2024-11-30 05:29:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6fc3d05b-dfda-3ad2-9158-26d21864131e | -9.55155 | -63.95491 | 2024-11-30 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3393bfed-a7c7-3109-9097-d3da3ebf4803 | -7.89842 | -63.26256 | 2024-11-30 05:29:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74adebff-c137-3279-9841-438c5f372788 | -4.91632 | -60.17006 | 2024-11-30 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68663cb9-e828-3196-bbce-8aab74153ab2 | -9.57759 | -62.65495 | 2024-11-30 05:29:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4580691-fc21-3f32-a40a-a3f1db8029fb | -9.38071 | -63.57675 | 2024-11-30 05:29:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b865cecd-5bfc-385c-a77a-3b551ea24783 | -9.7399 | -64.64016 | 2024-11-30 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e33b5ac-767c-31ab-8bae-56573038cc02 | -9.65038 | -65.7401 | 2024-11-30 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ed72a02-e098-3293-ab14-360f63d3e7ae | -7.89453 | -63.26555 | 2024-11-30 05:29:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fb0f611-d671-3219-90f3-a96bb9a7354c | -9.91901 | -59.9081 | 2024-11-30 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d40a586b-48ea-3a59-b7bf-09d137a40620 | -9.38734 | -62.24228 | 2024-11-30 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b496a539-d40a-32b5-bf1f-20b3bdf458ff | -9.78727 | -62.61716 | 2024-11-30 05:29:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 143ef4f6-f63d-372d-9003-e0af973147c8 | -9.15365 | -62.7158 | 2024-11-30 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91b9b696-2123-3e01-8ea2-650a4bd3dcfe | -9.18952 | -62.37908 | 2024-11-30 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f2b2ec7c-5a39-328a-b958-ca23898cf9db | -9.87472 | -65.14822 | 2024-11-30 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49c44730-2ba5-3fa5-8e7b-134c86190a9d | -9.63342 | -64.19746 | 2024-11-30 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27ac3c90-d244-3f8f-96d8-687be90eb698 | -6.83092 | -59.34727 | 2024-11-30 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31af4e1e-a42d-3ea4-94f3-8bd2b9c85ead | -9.87409 | -65.15209 | 2024-11-30 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c784ab20-7754-3f81-9482-af2905d7c8cb | -9.27777 | -62.37878 | 2024-11-30 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5cebdfce-9c04-361d-9cc3-f7378f09ff9b | -10.22148 | -59.08891 | 2024-11-30 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c8b598e6-45a9-3271-b8c8-084f68f947e1 | -9.82014 | -63.24825 | 2024-11-30 05:29:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bcd18795-1a09-36db-90fb-b133dd153df6 | -9.15419 | -63.24848 | 2024-11-30 05:29:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8147b7b-d600-3675-9de2-b47ee40ec530 | -10.18399 | -59.52981 | 2024-11-30 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29672c7c-5b73-34af-9d2b-847fa722ef15 | -7.89119 | -63.26501 | 2024-11-30 05:29:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f80f24c-bdea-3136-a2b4-63405ce1cf67 | -10.49544 | -64.24805 | 2024-11-30 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b7306ee-03ac-39eb-bf41-00e5adf8a7f6 | -9.41164 | -63.23214 | 2024-11-30 05:29:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README132.md)
