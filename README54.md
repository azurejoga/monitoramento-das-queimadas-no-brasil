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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdd53fe4-f7e8-376d-bbb9-0fc30dc64268 | -3.88071 | -51.94181 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 808f2db5-2839-3ed8-b296-825ad192a5bb | -1.44863 | -54.51176 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0cf5bb1b-2bef-3634-a568-377cb40ff1c4 | -2.10481 | -50.13607 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c80b9955-5a80-3349-8de6-de51e6a9dd68 | 1.47827 | -56.07785 | 2024-11-24 04:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c834530c-0595-357e-91ac-48e6881cad63 | -2.46428 | -50.22045 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 473870aa-6471-309e-833c-ce28a0f2f888 | -3.25847 | -54.21418 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 319f34da-9cf5-349f-a162-04aeed5d17ce | -2.85545 | -53.96598 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7f149959-d3e2-3a4c-9533-13347eedc92d | -5.08104 | -44.16577 | 2024-11-24 04:53:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05d12eef-0543-33d6-b493-e36a5eed488b | -3.24637 | -54.22384 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5b30f5b1-2b25-3fbe-a840-9376eebc957f | -1.26106 | -51.77146 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8e06649-fe3b-361d-9a29-8fac04322645 | -1.95981 | -49.53542 | 2024-11-24 04:53:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8332bcd0-fea3-38d1-b644-fc4ef6c49659 | -2.65406 | -46.13336 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71efd7a1-1a55-34c7-b2f0-6bce12112de1 | -3.19077 | -46.56128 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c2b093e-f0a3-33ee-adc6-e489f7de6cbb | -2.62531 | -54.3815 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a71feed-01d5-3621-8ba9-a45343d4b023 | -2.71492 | -46.27554 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59b74a7c-d238-340c-959e-a3ea59bc6f89 | -2.70262 | -48.66218 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28178ac2-24cb-33ce-ad60-3238870220f0 | -3.64495 | -49.88862 | 2024-11-24 04:53:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1aa99b9c-39e2-3358-900f-f5218eef0224 | -1.06635 | -53.19432 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 526a229c-9eb6-32e3-8a35-ab7aebaa4f57 | -1.46749 | -51.12418 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46e97605-6d8c-3f32-b173-4de3c43ed87e | -3.77477 | -52.40423 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8cbd5ee5-5ad9-3b9c-98bd-cf1336c11e52 | 0.05088 | -51.72071 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ad7cb34-344b-3a55-b0c6-12560e57e2c6 | -0.84407 | -52.54733 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49838272-300e-349a-837d-01a6257857b5 | -3.2519 | -50.1161 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 363584ea-d03f-3ae5-b023-9515fca8a752 | -2.39294 | -46.81739 | 2024-11-24 04:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6fc51d0-23d6-35e2-8972-52c49662a78d | -3.65802 | -51.25347 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c6caff4-ad92-3343-b304-4562a8c88bbf | -1.86548 | -48.1652 | 2024-11-24 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ceebece-dcc0-3bd6-8119-5105a55ec79e | -1.98972 | -49.53925 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 430a5172-3bf4-38d3-a992-9762545aa4ca | -1.6704 | -47.85081 | 2024-11-24 04:53:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4447a290-e0a9-30f8-9045-7f14265bab2a | -3.79114 | -43.60255 | 2024-11-24 04:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a7366bb-e28e-3a49-8473-d927bbce1942 | -2.31531 | -50.5919 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c245a61-eaab-3082-909a-3cba5a615e94 | -1.48452 | -52.51896 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 53a47e2c-318f-3f7d-9553-cfa45f336410 | -4.74194 | -49.89374 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04253655-ea08-3f52-b537-94bc77b573b6 | -3.98508 | -49.99648 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82f95eab-9336-35de-8232-667034480b38 | -4.93648 | -44.07291 | 2024-11-24 04:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54a088b8-1e60-30de-ba4b-402d13ec9c17 | -2.24372 | -46.86704 | 2024-11-24 04:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cec2469b-ff76-32dc-a15e-e3a1e2ecb78b | 0.10258 | -51.20308 | 2024-11-24 04:53:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db39853c-24e4-371b-8aa0-63ef675eb850 | -2.7107 | -46.27487 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36acdbdd-d7d7-393f-a124-b119c401e423 | -2.0883 | -50.6302 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84708754-023a-338c-bf19-d5f779e44969 | -3.53204 | -50.75241 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc5cce77-360f-372d-a3c8-4b9029338b2e | -2.69688 | -46.28071 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db1e79c6-b538-3264-b325-47a80d0772f7 | -3.48987 | -52.00752 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| defd65b8-65cd-37e8-b22c-83de26925e99 | -4.24117 | -50.38927 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ee52850-8002-3abc-8b18-b342ed4de7c1 | -2.78675 | -51.41098 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04226769-b9ff-3519-875e-a650bbf49465 | -4.03104 | -46.67502 | 2024-11-24 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4993566-a8d6-344c-94a9-0476d8afe679 | -4.1998 | -45.36316 | 2024-11-24 04:53:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 31729fa9-39f0-35a0-a16c-2044906c0b21 | -2.08553 | -50.21502 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 169e4c90-d96f-3d4b-b34b-9c2a4f5e58e4 | -2.44417 | -50.37341 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc8476e2-cae1-3663-b164-531e1bfcf51d | -2.82033 | -54.0326 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 862930a8-3a09-3e0e-9032-236bb5161ca2 | -2.61615 | -54.25879 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 544185e2-936c-38e7-9f99-ff220792c154 | -5.60617 | -46.29322 | 2024-11-24 04:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2299b6ef-2e94-357e-b867-3208b46996ea | -3.13251 | -52.98692 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db7641ad-4ba0-376c-8d90-99455cd048f4 | -0.04727 | -51.7464 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f35d30dc-19ca-39a0-bcc9-a678f6f59058 | -3.62543 | -45.06365 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce01bcc5-ad9d-3738-a917-bb64224dbbb7 | -1.77041 | -52.71337 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0faf8456-460f-3d79-a3bd-da0cbc925096 | -3.57866 | -50.52638 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed172c4b-5064-3c69-b5bd-8852fec26dff | -3.28575 | -53.84451 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37df6ee9-6a13-3ccd-ba41-d92e4fc70d1e | -2.21311 | -48.21055 | 2024-11-24 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff3d4db8-b1bc-3fa8-9546-79b9afaf8d99 | -2.78149 | -54.05667 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dbe6e4d-3839-3e5d-b563-ed29602b66f9 | -3.0922 | -54.55392 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 730a04f6-ac92-3d50-89f7-144bf0c577a7 | -2.70763 | -46.26634 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b4df9ce-947d-3c68-8dbb-7b9fd33de208 | -2.40726 | -53.84778 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa272829-dea9-3e90-af88-74ef574a2cb2 | -1.42483 | -52.81358 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13f19208-2420-30e6-b334-6e8ddf371a27 | -1.69779 | -55.02042 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d14ed334-cb28-36d5-9465-837dabea4cd6 | -2.63935 | -51.89931 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3bd1a347-f31f-31c8-b4be-f4d6519a9e39 | -4.59751 | -50.64994 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a87edc7a-bf46-345e-a2ac-91f04848e55d | -2.25989 | -50.47033 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 899ac15d-f4ea-3a4c-93c3-1f6682dd8a6f | -0.95144 | -52.40353 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aac02b58-e064-363a-aec9-b9bcdfce87af | -1.19676 | -51.76785 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e09ed127-d191-3475-8f7a-8961750ef2ad | -2.15265 | -50.9173 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd88572e-b2cd-3d8e-a91d-f3f798d58820 | -3.43889 | -50.75278 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1895ba8e-56f1-3849-8a75-e8e2690e5332 | -3.17874 | -54.32109 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff81cd1e-be9a-3b8f-8ff8-2d19a83d5b22 | -3.55201 | -50.19495 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40304bba-b2fc-300f-8094-d0b4be248629 | -1.94423 | -49.52131 | 2024-11-24 04:53:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 865e0348-160c-3f92-ac0d-bd287a2f64aa | 1.1569 | -50.69737 | 2024-11-24 04:53:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ecffab6-31ad-305e-94e4-bc332e44d3c3 | -5.10815 | -43.14866 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d6a15fb-17d8-364c-9f55-7544eed74b74 | -3.97891 | -49.92983 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 378e20c3-046a-3d8b-bb2e-2785ef58cbdd | -2.01865 | -46.29715 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 98b514d9-0771-377e-93b0-5e688b31cf21 | -2.56259 | -51.23391 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb38bfcb-44ee-3bfa-bc51-c1ceb4f58aba | -3.0927 | -51.32364 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6868fa98-62b3-37dc-a743-b2c2f2f0a363 | -4.40792 | -50.83768 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd80b1d3-2b58-32fb-af56-3b9559c2f5d1 | -2.34915 | -50.37343 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24b8e420-a8d6-3a05-a3a1-aabebb43899c | -3.17992 | -54.31356 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a100eb3-8509-308c-bef2-46b0b5a92006 | -3.43804 | -50.02109 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 767caca0-cafd-37f1-98e4-6a47f6555b4a | -3.0806 | -49.20103 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1456646-1dd3-3c79-b4c9-2f7c4078e1da | -3.01499 | -51.38635 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19e1d900-6775-3a71-8076-757db562b00c | -3.385 | -50.32143 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6d413a26-223f-3073-8ae8-69d26307d8f7 | -0.88015 | -51.7253 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74229f9e-2a8e-380c-a0bb-4f9c570c57e5 | -2.6901 | -46.26811 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bac7255e-c4a8-3010-9063-24ea71e339a2 | -1.25436 | -51.74937 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0107df0a-e36b-310d-8637-c0d053a8a9b2 | -2.21133 | -48.91512 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6690d901-40e1-3758-9bcc-3806fc2bf7b1 | -2.0623 | -48.96971 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d73e65f4-dd80-3903-b54f-6c50917eedaa | -1.69284 | -55.02822 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b0cce30-5eda-3c9e-ac87-ad4f12b0699c | -9.80903 | -48.1666 | 2024-11-24 04:53:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e14e8ae2-380b-3e90-950b-4fd74740bc22 | -3.08645 | -54.54512 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7fe9bd88-69ee-3021-8216-ec7ba0c8096a | -4.2368 | -48.63985 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a6a7225d-d4ef-390e-8b21-1556155da660 | -2.60983 | -54.25392 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9833c8c0-b429-3de1-8dc1-43f5ed694765 | -2.10015 | -49.00313 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7e756c4-d046-3942-a6e1-e3936002dcc6 | -1.61298 | -54.41212 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f01d2e7e-215b-3957-8814-acd0877b41e8 | -1.98683 | -53.13238 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f0f069c-e9f9-3779-9e98-43084503d927 | -4.02707 | -54.63313 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README55.md)
