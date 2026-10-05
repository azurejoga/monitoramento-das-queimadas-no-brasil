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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cfff22f-0815-30f7-b934-9017d5b99c82 | -5.98592 | -53.63935 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 109a131f-e63b-3a17-8559-a1f7f2b3ca0a | -6.26698 | -55.4347 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcf967c2-18b9-3f11-996f-48e20739ae7e | -3.18738 | -50.54198 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6db04128-7faa-3056-87a5-1f6780a4189d | -2.67469 | -49.03275 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ad3fb36-d740-3e53-9724-97c1cfe35fc1 | -2.05222 | -56.88546 | 2026-10-05 04:57:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0905dd27-c022-332f-a22a-1c33c9dee9b3 | -2.68119 | -49.0379 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a7e3e6a6-22cb-3962-bacf-ffb7d72de8fa | -2.97787 | -54.09903 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 442f8001-a036-3860-9918-e7f9e31f4948 | -2.90139 | -54.11376 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09f485ac-82a8-3e00-a360-ef1f48322f4a | -6.03134 | -53.88603 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c10e985-4457-3ed8-8530-1ce5de809990 | -6.20579 | -52.83407 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89272994-0039-3e8c-b60c-66284ea3584e | -3.66354 | -54.28176 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2376db9d-64ef-3cc2-a83f-d27983c9fab3 | -2.85743 | -51.29985 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 956658b9-fd22-3a89-9833-f9987101bc05 | -4.1069 | -50.8045 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d18493dc-aa4c-3d21-a9ac-244f93821206 | -3.8424 | -50.32063 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 24140ab6-91e2-39a8-b0cd-fa6189a69a6e | -2.89957 | -54.12502 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7697c76b-0da3-3bda-9eda-984c013fddd8 | -6.91279 | -43.6674 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5723feb9-8179-306f-997f-8313cb4b657b | -8.66039 | -54.54971 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aad6b38a-0c4c-3300-8fae-3ba61992b4a0 | -3.18452 | -54.07772 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df124d28-4bf3-3d29-9302-790dc576fe6b | -4.28876 | -50.26578 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fe95516-de3e-3d07-9b13-014ec8c63de4 | -2.90404 | -54.14117 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d631cdb2-37ad-3a62-a53a-886179f1c08b | -7.51251 | -54.99035 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1b4a4c6-294c-3889-8778-0c75c99e5035 | -4.11363 | -49.07298 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b39ddf5-4267-378c-9f0f-e60f8210bf25 | -7.43351 | -63.5644 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de74a46f-85f0-3ce6-a78d-43b1c4ed0418 | -4.07726 | -48.96518 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc79ff44-02cd-3655-be21-9a5004793b35 | -2.81909 | -54.12466 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d853973-c836-3290-a810-9e8e807174c6 | -5.68301 | -53.49382 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98dfe89d-d29f-3e46-8283-19773e372fd0 | -3.85952 | -55.826 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c529ec1-adfe-3821-a204-eeb52d2c0125 | -2.84857 | -51.29136 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5ee563e-c24c-3915-ba40-d87a2acf7164 | -4.25401 | -55.04553 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11cb6565-e3e2-3ed2-8cdd-edba655db204 | -7.50285 | -54.98492 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23d17500-71e5-3564-9cac-bc026f903ac2 | -2.9018 | -54.13309 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58f829f6-7e8f-3c1f-9688-9a9f1d118fab | -3.10803 | -53.72212 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da0d1fbe-ef1a-3ddb-9101-92765e002f48 | -4.11001 | -49.07241 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c42a3c78-eff5-3545-bad3-1f52d10d0781 | -2.93867 | -54.12357 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 572c2bcc-6b02-3777-be11-9d5ee6024a7e | -2.80693 | -54.13431 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 503e4b9e-a519-3325-afd4-dd626c84b672 | -2.80246 | -54.11815 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13f25180-8e5c-3bfb-a6eb-e943328f5345 | -3.13293 | -53.71862 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 11c28ee0-d02b-33d8-ad41-192f741dedca | -2.94328 | -54.20543 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ae8ecf60-c2b0-3615-b28a-e5897b9ec914 | -8.66709 | -54.55082 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db56926f-79aa-3ef0-8ece-a44353bf807b | -6.31604 | -43.34753 | 2026-10-05 04:57:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70a24ebf-64c9-38f3-89e0-b8c8be1d39ea | -3.90802 | -56.1016 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8f6360a-92a7-390d-a1b5-b881700204fb | -7.89383 | -44.19133 | 2026-10-05 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 714873a9-c2b6-323d-93cf-445f5364f98a | -3.11239 | -53.76015 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 49cdc4d3-219b-3917-ab9e-e292c4233b6e | -5.68578 | -53.49784 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69e4bf8e-ca22-3080-a886-b963a495462a | -6.81027 | -55.29979 | 2026-10-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb3eef2a-3e52-3c6e-9c52-c90e2ac9d003 | -3.07089 | -54.17482 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8afafdba-1446-371a-9a5f-cbb18ff6cb34 | -2.95102 | -59.15997 | 2026-10-05 04:57:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa61e48f-436b-3e08-acc1-457e7a38302c | -3.05382 | -54.39444 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3c3ce15-a02a-31cd-9a30-8b528566dd53 | -4.45927 | -54.96231 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9450e56-7f67-3b44-96c3-b4a3d8b81969 | -8.21956 | -50.21756 | 2026-10-05 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11644be3-1083-39be-bfa8-0862df6a30e1 | -2.95573 | -54.14946 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| dc5b76fa-b8bd-3ff4-947b-fbf45768bd73 | -6.1953 | -52.8147 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcd0e963-5a43-386d-8170-56aeef77d539 | -6.01156 | -53.52123 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bfdcb60-baa3-3b31-9bfe-8953948fa894 | -4.11299 | -49.07718 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f729dd20-3241-3c20-b9c0-a39e9f93d640 | -6.21403 | -52.8035 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 510d20c0-ea7f-3e77-8890-3ef9a551e679 | -3.13914 | -53.72333 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 849bab3a-844a-34ec-87c6-6d237a893f52 | -6.01793 | -52.7544 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3054fb01-9697-3c2c-bf6b-1cade41e64c8 | -3.58491 | -55.55672 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8357374-115d-3a3b-a7e2-d82180caae40 | -3.07635 | -49.54399 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b77496c3-8a45-3dd0-a92f-e159505c10cf | -2.89329 | -54.12017 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47170548-667b-3189-af7e-520b179b9826 | -2.57845 | -51.88157 | 2026-10-05 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8590759-0f86-326f-8d2a-f33e67ef08db | -3.70836 | -50.66253 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00ee4610-0a32-301a-8fae-4c2920047ec2 | -5.96788 | -55.38008 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32ac00ac-8e3c-3832-a275-d3a3611bcf2d | -2.946 | -54.14401 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 17bec1a1-b80d-357f-bf72-4a4330b1e39c | -6.20965 | -52.83114 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08fc4957-5556-3327-99c2-a2c0a0b709f7 | -2.05166 | -56.88894 | 2026-10-05 04:57:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94981115-293d-337b-8394-628bebbfc7df | -3.51435 | -54.62262 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f57810b-6c8d-355e-a3d3-18582223d1cc | -3.05499 | -54.23026 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d75003e9-f384-3918-af15-1108f95dfd2b | -2.81927 | -54.10155 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f7ff16e-97a6-3431-ba21-87ab3d310128 | -6.17613 | -52.93555 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 823c49fe-203e-3258-8ce0-55fd16253bed | -1.61513 | -55.11363 | 2026-10-05 04:57:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f181e16-d6e1-3fb5-b7fe-9e12f74cb80c | -2.8047 | -54.12622 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c66be57-8972-3210-9fc9-fddbf12b9354 | -1.42197 | -57.85607 | 2026-10-05 04:57:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dd4d2eb4-127b-39fc-8e85-227b6b296d73 | -3.51334 | -54.60658 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37cf0c63-76f5-3a33-9c01-ddc83aa6447f | -2.03198 | -56.93338 | 2026-10-05 04:57:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbdf8234-197d-350b-b60d-7c357e2112f6 | -8.65981 | -54.55328 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1cf16b85-1e0c-3471-9c52-eb8d99df0030 | -3.91867 | -49.71181 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8fec880-f68e-3943-b8b4-f3094fb571bd | -3.30953 | -53.84345 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b129049-1609-3ca7-8f78-94dcbc6c19bf | -3.46854 | -50.08961 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea7b5c72-9552-31b1-a18b-fb37e4b0d8e7 | -3.05545 | -54.16079 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 662e9e3d-c75b-302f-9be8-06ca644897eb | -3.04194 | -54.20111 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0eecb708-a102-3a25-8c8e-b5f01cd04b67 | -3.12267 | -53.73937 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d94bf88-5f6c-3a3d-aa61-1f5c034b1c21 | -3.13459 | -53.73007 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04da30a0-d0c3-3709-8004-8c210792dffb | -2.92266 | -54.1133 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef585719-ae09-39d9-bcdd-3dcd62aa65c3 | -3.12731 | -53.71027 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e32d1686-db56-370c-8653-7962263c4c1f | -2.95888 | -54.10756 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b3e8039-8559-3b6b-b53d-9ac2c0860b40 | -6.00102 | -53.52314 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 732b0570-b7a1-3423-bd54-f760fc414c4e | -2.91535 | -54.09293 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e83b2db-3758-3457-ad0d-341637e86605 | -5.63712 | -51.76688 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52e72ad4-1d05-3f16-a38a-09e398d0810e | -2.57678 | -51.87075 | 2026-10-05 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27b6cfbb-f8f3-3490-beb9-d3dd713ccd02 | -3.04989 | -54.21783 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aadf4ba9-4f32-3125-964b-8a128ec6fb10 | -3.87273 | -55.81467 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41d43864-031f-3b00-8f87-fc8abc0d7409 | -3.10744 | -53.72576 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5506da24-efe1-37f6-9504-871d003b8207 | -2.79901 | -54.11761 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f409e8ca-cfa4-399f-ae2b-9413c27871d9 | -3.29252 | -53.84076 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3667f6f0-75c2-308d-80af-b0d8123e8dd7 | -2.6961 | -49.03605 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d9130d3a-8166-362e-89ff-d3ecd487c9fb | -3.07267 | -54.16359 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| b453b70d-99ac-3710-94ca-6892bbac6fb5 | -2.99079 | -54.03978 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b24d319b-2d4e-34e4-bd68-40ff2bdff999 | -8.53459 | -54.59198 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac6903e5-b3a0-38e2-ab93-06e964734b33 | -6.90988 | -43.68818 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README43.md)
