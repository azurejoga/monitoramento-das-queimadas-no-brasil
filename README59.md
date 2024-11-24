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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a20ccb9-2336-3307-9fa2-6c9ba48ab2a6 | -0.91727 | -51.64391 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22ab9340-a08b-364d-a58b-be961239a243 | -1.2327 | -53.36747 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bd56c60-c686-3318-8328-09e083204a8a | -2.70397 | -46.29029 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ccfc8308-8e82-391c-a5bf-489be4e6d17b | -1.22902 | -51.73846 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 950ad7b8-b0b7-3090-8dc5-f183376ceb44 | -2.15526 | -49.72289 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5872bc60-ff3b-3af6-a8da-5ddf57bb9dc1 | -3.02429 | -54.05234 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf846dd6-e0c9-3741-92c1-d160990ff402 | -2.64923 | -46.85935 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 75390eb3-1e93-3480-ba35-baac54934542 | -3.5764 | -54.68292 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9096b9ef-e089-3a84-abc5-a38c2ee6984e | -2.41481 | -48.98158 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2e540e2f-31ba-3d0a-b447-3cadeb215d93 | 1.47424 | -56.07839 | 2024-11-24 04:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42c8fa35-57e9-32bb-bae4-3b8daf8a3167 | -1.81658 | -46.63476 | 2024-11-24 04:53:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f228675a-1e0b-32a8-9033-d5790debcc5c | -2.8743 | -50.40517 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4779467-8818-384f-99c8-75da6501bb2b | 0.40281 | -50.85719 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 77b2216a-cff4-39d9-9c12-385da0604542 | -4.11556 | -49.44244 | 2024-11-24 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 801ccdd3-b05c-391b-879f-1c786c9a15e6 | -2.95324 | -51.43356 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cc4bdca-d7da-30b7-8306-b6398c54d913 | -4.10702 | -50.71788 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15b1ed2b-cddb-3a2e-aab7-233cc6f9838b | -3.08049 | -54.56007 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fdb75359-80c3-3aca-8135-0383cfbe4642 | -2.08547 | -49.60852 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 05827cfb-b635-3357-95cf-38ec57369f2f | -2.68026 | -45.65591 | 2024-11-24 04:53:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 59bddc1b-6c84-3073-8012-f5f9e4bfb0c1 | -3.8158 | -51.35346 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe3baef2-fdc2-3f15-9197-814889e898ad | -1.77293 | -53.61524 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25c860d3-a9af-3bf5-b109-36befc5376dd | -2.0347 | -49.00666 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e2819ff-15f5-3c7e-9a8f-167d17393e08 | -0.3743 | -51.54829 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e5adc91b-fcf5-36d9-9df9-24fcdbc54988 | -3.7685 | -51.68068 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 408af242-a317-3521-9086-e454b2a7d709 | -2.82954 | -54.01883 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 032962ee-73c4-39e3-8ba5-1038827a9008 | -4.44268 | -50.07909 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17171d2e-d564-38af-9a76-cc0ab1b63b88 | -2.89691 | -54.01404 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85d69af6-e97c-3e31-88ea-2369ec02cd5d | -1.60529 | -52.5946 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 682ced51-149f-3971-814c-b8002af12d82 | -1.19519 | -51.93341 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14e160af-b314-3d45-bd39-865dc1405b78 | -2.24424 | -53.61322 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edf0d874-f6eb-3cf3-af21-cfb746eab161 | -2.21991 | -50.68275 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17c2708a-c7e6-3e72-8eb5-35f41995e97f | -3.47214 | -47.68385 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d3581e57-fed4-3282-861c-6524a2df234e | -1.52919 | -51.55658 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c4429e0-dcbc-365e-aef5-7d8e830fe4e8 | -2.3757 | -50.51353 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d22811b-0f11-3bc5-bab8-fbf4743e5e68 | -1.31539 | -51.74823 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc59223f-0c93-31d2-bd18-07df07bcfbdd | -2.37701 | -48.24702 | 2024-11-24 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 769ae88b-e76d-39a1-9798-8ac39cbaa384 | -2.66635 | -46.60388 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 368a5a22-62fd-32e2-8875-59b3c6ff802b | -2.78091 | -54.0604 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 388f1e72-5c2b-3bef-a038-6572bb2b09dc | -3.18792 | -54.33024 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6fceda3-b36e-304c-a3c7-32d2badd5246 | -2.88155 | -54.00029 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a650d9b8-20dc-35a3-b243-303888506274 | -2.67994 | -45.65773 | 2024-11-24 04:53:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d397faf3-fead-32e8-b46a-3e88998e198f | -4.83671 | -50.68996 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7872d4e-15ec-36c2-b414-ba751fbb7606 | -3.31938 | -53.29217 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 548ccb76-1e77-37ca-96a9-b2c3a5e75243 | -2.7645 | -48.5756 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 207558cb-41f4-3e08-ac32-92f3f0a9b484 | -4.27263 | -48.60446 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 078ff570-6d5c-38f0-bd66-fd2703756a36 | -2.15374 | -50.91031 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb4523ae-076f-3936-9b4f-26004de920ef | -1.40151 | -54.25908 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 907ae6aa-fd03-35a2-a30f-16479eebae52 | -1.74677 | -52.38577 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b6b303a-7ddb-3dc0-afc3-005d78b4a2d6 | -1.73494 | -52.72221 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd62157a-5d1c-36d8-a76f-3142400a57a9 | -3.10556 | -54.00412 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cc3bf9f8-7c72-3d66-a2bf-457641c21fb7 | -1.72683 | -53.2562 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 09db700c-6623-3163-b960-b21a1affa22d | -2.69917 | -51.36198 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54f6691d-b59b-3f53-817e-393f46784913 | -3.75262 | -50.00971 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eabd56e1-a764-3f00-bb31-f6736dcc76dc | -2.14079 | -51.01559 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89eee4a4-cb79-3dbc-9ea3-e721ab11dbec | -3.07947 | -54.54408 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6041faf2-8fb9-37c2-a1fb-07c20fae7a1b | -3.25432 | -54.24037 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca62bcf5-b4cc-3cd7-8bd4-facedc349ea0 | -0.91674 | -51.64733 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 462b1238-e53f-3fc4-8e77-fd73bc315bc9 | -0.16436 | -50.40576 | 2024-11-24 04:53:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59994e90-6825-3c62-898f-34503f0ddf0b | -3.84004 | -51.30701 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67e2ab63-b6dc-30ff-a462-bfbcfd3f71cb | -0.34141 | -51.97546 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4e8dd83-6557-33a0-92d4-bbaca893c552 | -1.46364 | -51.12712 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a2603d4-2ad9-3ea9-8b88-e82909322bf1 | -3.63158 | -52.25179 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9aae33b-753a-3b70-a3a1-866efdd5e0ec | -2.74809 | -49.12448 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba743d7d-84c5-3ec0-ad01-3bfc286e0b1d | -2.24978 | -50.46878 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d00132f-e140-33c3-8421-aa242d6d8fee | -3.71055 | -51.79201 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68b78400-d474-3562-b66b-677e58d7373d | -5.10493 | -45.71755 | 2024-11-24 04:53:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e23b8ea-676b-358b-9eae-dc01383beb39 | -1.07953 | -53.3627 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc7656da-b78e-317a-897a-ef6724e7d32f | -3.28409 | -53.83308 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df989935-fcbe-3ecf-9dfb-b0ba61b92230 | -2.19717 | -50.74074 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e9582a1-0fca-3d75-9be6-0948389f895d | -2.08201 | -49.60799 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 49bf88ad-17c6-3067-82ae-60a06f026040 | -2.16621 | -50.127 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 844bef8a-e361-3d09-a96e-64e1509f92fd | -2.70647 | -46.10451 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4f35a15-2bcd-31b5-acc2-f4f281adbf54 | -1.33308 | -51.85627 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9aaef47e-9bb1-3c7b-85e5-1e7128e9ac00 | -3.84482 | -44.04457 | 2024-11-24 04:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71ac02b5-fc6e-3134-910f-4b24049ec6d8 | -4.05841 | -54.61491 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7ff8c7c-7044-3600-b62c-c73195012dfd | -3.29475 | -50.36397 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98ff7376-5d34-303b-8d44-33877f6b897d | -2.78367 | -52.86813 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97430853-3c0d-3f92-903f-1e391eab36be | -2.81708 | -52.959 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 718c9668-6f7d-3372-9b2b-298b18090728 | -3.84894 | -44.05143 | 2024-11-24 04:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 57305924-d829-3639-9dab-8c5182ffb745 | -2.76485 | -54.07318 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d53ecfb7-c6c8-34c2-82d1-2ff683a5994e | -3.43576 | -50.03612 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cb0a56e-a141-3166-87f9-3746d1740bf0 | -2.81065 | -54.02729 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da7af7b9-9445-38ca-95a1-c3ceec916b4d | -3.55615 | -44.98288 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7deed9f9-75be-3e3b-a616-5f12335fe14f | -2.11858 | -50.70003 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc905e0a-8995-36f0-8d2e-8c17db57aaf3 | -2.65772 | -46.13804 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ad193c9-5d06-361a-a63f-3936f800e487 | -1.22106 | -53.6884 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 80b774a8-66df-3724-a7db-0409508550c5 | -3.12496 | -53.1002 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4fe2710-d7f8-383c-a5a9-f1fa8041632f | -1.2093 | -51.75648 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ea98131b-0d6a-35cd-b61f-05359f7b8adb | -2.27587 | -46.20119 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0eed8405-1cd1-3969-b6c3-11684fc5b7ac | -3.64215 | -52.25344 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22e0af06-b0f3-3b89-aac1-0d81630fb0ca | -1.30325 | -51.73934 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ccc7001-026c-30df-bcfd-15fdea3f796c | -2.17188 | -50.13535 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91eb3279-dc8b-3e22-a13a-042fe6565481 | -3.60786 | -47.50826 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8935f4c8-23b3-3629-9e07-3d400699feee | -2.75292 | -48.62634 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dae2852e-a022-33dc-a5d7-53f74dc62294 | -1.21858 | -51.74037 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 875779d3-52db-3e04-8d5a-35f2c47a1089 | -0.90055 | -52.64196 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60253fa5-84cb-3429-a1d7-49e03680586d | -3.10789 | -53.9893 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3af97f72-f921-3a3c-90da-d359c87219bf | -3.09731 | -49.02003 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9743390a-570c-308a-846e-15c6b240f0dd | -1.61132 | -52.57773 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e411e2f8-49ce-3ea8-bb22-23c1bfa1d8b3 | -4.6013 | -44.72853 | 2024-11-24 04:53:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README60.md)
