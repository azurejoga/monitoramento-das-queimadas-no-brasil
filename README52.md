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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bf3ec80-e726-3e67-8024-e29ea0012882 | -2.88987 | -54.12358 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2eaea609-2661-3310-b2f3-e1fc3e8967cf | -1.51745 | -54.81164 | 2026-10-04 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a62faa80-5e8d-347d-b5c6-e1990b10b13a | -6.23541 | -53.15519 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0966d192-3d58-3fb2-b289-cdf16fa5b780 | -4.25601 | -46.3658 | 2026-10-04 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dd544d48-b607-3ce4-8fa8-ffd983e6f24b | -3.09632 | -51.1041 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| af37c9c8-3b07-315b-9b0d-8b6c6c38eeea | -2.84809 | -54.13474 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2346e92-d5b4-3bbb-9ca5-38122910197c | -3.11888 | -53.72596 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a8b53246-09b1-3b6a-9501-512c1da165ce | -4.27724 | -50.27207 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| a134deec-50f9-3bdc-85a2-4daa6d572a22 | -3.16072 | -53.07096 | 2026-10-04 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6874a86e-ff12-3c57-bd09-2ef4e95ee8ac | -2.24505 | -51.9253 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9d5dacb-ff7e-37f3-965d-81c98626887d | -2.92815 | -54.10931 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3081f944-c7a4-3751-acaf-2b229498dde1 | -3.28602 | -53.83354 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3d07748-d0aa-32b2-9466-2bb8a4895a0d | -2.81186 | -54.11309 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1537d390-4170-3ad1-ba6f-be80a8ab08a3 | -3.59951 | -54.23569 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94845388-d3e3-37aa-a1e9-c63866e785b7 | -3.89444 | -49.69763 | 2026-10-04 05:16:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8825045f-39cc-385f-9b4e-dc5dfbcc45ea | -3.7687 | -55.54357 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22f2d2e2-4656-3e50-9167-51eeffbc6360 | -2.95512 | -54.12144 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 541ae287-0898-309d-876a-1c97d6cf6374 | 1.79828 | -55.55978 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18e90b5f-b933-3295-8c5b-a76450d7c6f0 | -3.42734 | -56.33239 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67790c9a-fe11-31df-a96c-0183694b8b3e | -2.92525 | -54.10483 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01f3b6d4-b881-313a-96a1-80e225f5c668 | -3.70604 | -50.65761 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3c00108-9f95-3ae6-8ae5-c5f74e378358 | -3.80719 | -50.85524 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb949bae-84b2-3f1e-a834-e2830dd66bbf | -6.2129 | -52.79753 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 586c8fd6-9e1d-3d0c-86a1-75ef11e6d16b | -3.58055 | -55.55531 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d36fc84-79c8-38ab-afc4-741a2f7c83d2 | -3.72606 | -54.21322 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13264623-f014-312e-a7ef-c03ddb75f93e | -2.81432 | -54.09739 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7201897c-1017-3a30-9df9-ca7b43c3a50d | -2.90008 | -49.40494 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ccece43-b158-3a3e-8e89-2a59e3a6a8d1 | -3.15328 | -53.06977 | 2026-10-04 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2582d67-bb9b-3ea3-80ad-c4498331775f | -3.18687 | -54.0983 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb060856-8b8b-3b3e-9b75-c570577614a3 | -3.1684 | -48.58698 | 2026-10-04 05:16:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b680d5c-5dac-303e-b785-15e3cfeaa28d | -3.64909 | -55.48175 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6914253b-a478-31a2-bfdb-6f1803fbfa34 | -3.13377 | -53.73536 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8778ca6d-7e37-3ece-a3dd-edeaed2e9511 | -4.42937 | -55.75158 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b303d60b-3bf3-37dd-a1fb-a0d105906309 | -3.87968 | -49.69979 | 2026-10-04 05:16:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ccab35a6-f03e-3d37-9928-1ceaab218bd6 | -1.62096 | -55.01957 | 2026-10-04 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4fc2e873-0527-3d8b-bd49-9d15fa6939cd | -4.26957 | -49.97646 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cc7c174-7f6d-3d90-a349-31675aa85ffb | -2.22358 | -53.70995 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 7c709e36-5732-35bb-a849-b4e554c46f11 | -3.18333 | -54.09782 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac2f2196-98a8-3741-89a3-2d343dc87d44 | -3.37323 | -58.23786 | 2026-10-04 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2696ecd-ef38-3696-a597-43d66bff864c | -3.1832 | -54.0984 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 455b5f42-e0d2-39a1-8694-4caa8de95e27 | -1.41199 | -49.26623 | 2026-10-04 05:16:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c713088-4b4c-3f37-9a2c-5d15e07344f8 | -2.80666 | -54.10023 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da655f85-37fe-3b51-8fcf-7747e226d6cf | -2.97273 | -54.10347 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 24773dcf-1d91-3b85-a5ee-5a4654b18d21 | -3.22973 | -54.31001 | 2026-10-04 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ca5b2e4-6888-3af1-b645-31f95eec6dbf | -3.07182 | -54.37322 | 2026-10-04 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36627734-b2f0-36c0-8ac9-a51d871d4188 | -2.8108 | -54.09684 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d37f8e5-9f77-33af-8456-e83479bacf47 | -5.22563 | -48.41288 | 2026-10-04 05:16:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0a9d6c4-50e5-35b5-b691-0880b708ae92 | -4.57237 | -54.94757 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1507851-a51d-3d44-91a8-9d9a8ecf9e39 | -3.10352 | -51.28538 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d3e1c3c-cd8e-33a3-8924-e94f54ab7c0d | -6.20821 | -52.80196 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7983b612-88b4-318f-beb1-e16c982f841e | -6.08079 | -53.30481 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ee0b515-4ca5-3a0d-8478-9041424abd78 | -3.04892 | -54.2158 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 34639d98-2518-3e06-a24a-2aafd759e55e | -6.21007 | -52.79472 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fe3b4f9-ca79-3dd7-a4f4-4ea6a24d4ba1 | -3.08464 | -59.18908 | 2026-10-04 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb31d251-377a-399e-b7ce-b711387985b3 | -6.01623 | -53.52777 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d969cd86-1c46-3186-bd5d-14820022faf9 | -3.05635 | -54.16877 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 526c342b-ef77-37ad-be35-1f10d83ae811 | -2.81231 | -54.13324 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8755d5d9-1b0d-3780-afa6-74976a29451b | -3.47459 | -50.0907 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6de62961-61cd-38d5-a381-d3db6f994cb5 | 1.75955 | -55.6572 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ec0e41fb-3767-3fe6-803c-d03ceba2b949 | -3.86985 | -55.81096 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| a638d0d4-26e8-35d3-a6de-596355410167 | -2.82304 | -54.11079 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6637349a-baa2-3294-a097-6cfffe497e6c | -4.26885 | -50.26601 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24d3e013-6a92-376a-9ea6-938a5a0edda5 | -3.28308 | -53.82885 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d6aa06b-c980-3b0a-99ec-c8c19fe21c9c | -3.20861 | -54.97953 | 2026-10-04 05:16:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63843c0f-cc3f-35a7-aa9b-e8a4c282c50a | -3.17155 | -54.08039 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d642eff3-45ac-39e8-a9fa-8428022ea68f | -3.30266 | -53.84447 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ba245ae-a7a9-33b2-a6a1-5bc2eaf1ba29 | -1.08513 | -54.11072 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c0dc3ab-7142-355e-9933-877fa62495b6 | -3.1878 | -57.86406 | 2026-10-04 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3da383ed-1096-3ae4-ae4f-00b9e33ca4d8 | -3.18459 | -50.53762 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 26c3fe64-8d45-31ac-ab30-fc72e6b7545a | 1.80488 | -55.55875 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d40ae92d-00bc-3d29-96b0-df9bc1c53d14 | -5.55131 | -45.26764 | 2026-10-04 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 68d0dbcb-e9b6-30c5-9543-4d46fc61087f | -2.97067 | -54.09162 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e905aa2f-534c-3dcd-a889-9705a0a228e8 | -3.07125 | -49.53755 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d16025e1-755c-39ae-9fa7-d42bd0bf2c09 | -3.04954 | -54.21189 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bc6f1443-712a-3cbf-829c-51ccabb7d54b | -2.97041 | -54.09504 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0d63227-0a1d-32b7-b1d3-c4c21d196b1f | -2.77862 | -57.68106 | 2026-10-04 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3bef53fa-3da3-3cff-a984-7a2fa17d6aef | -2.90977 | -54.13467 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81441f7b-094a-3508-92d0-d8364f6b9fc9 | -6.06988 | -53.47927 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2ef33e2-8d78-3758-9161-fca2c931f045 | -3.45231 | -53.16493 | 2026-10-04 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b86b752-0c16-3794-ae75-07a5705a66bf | -3.06048 | -54.16539 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ef8dc176-6caa-3941-b0df-3e20b6daf825 | -3.11111 | -50.28561 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b09067a5-e905-390d-9fa8-0f9d7e1f0961 | -3.11488 | -50.2803 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd75bd5c-3416-3533-a602-56815c1c44b4 | 0.69955 | -51.4317 | 2026-10-04 05:16:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a91cafd-8233-3a30-817d-d0eb539f2691 | -3.20554 | -50.75507 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 38308fc0-6903-3ce8-9bba-af62dbf5b8af | -1.98545 | -50.51686 | 2026-10-04 05:16:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2388d80-76d7-3f8b-a9ea-a816c88d4999 | -3.28643 | -53.85448 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4806ab65-216a-33ce-beae-d3624de6cb5e | -3.28244 | -53.83295 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e001706-73bf-3773-bdab-5bca145bb4c5 | -3.51583 | -54.6077 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2af1ee7c-146e-359b-b7fa-25bac73f6df3 | -2.90867 | -57.39799 | 2026-10-04 05:16:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5af2f861-40c4-33e0-86ab-c9028fbf3cb1 | -3.04251 | -54.2108 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 595e29b6-7fd4-3b23-8f93-ba40b71cc7e6 | -3.1635 | -59.08665 | 2026-10-04 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d0781c2-547f-37a8-8076-03da725074a8 | -3.46915 | -50.10053 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 558f12b3-a855-3a38-8edc-197e192aa6e4 | -3.3171 | -58.24362 | 2026-10-04 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8f7166c-6e28-39cd-98f9-626600d31f97 | -3.00591 | -50.46971 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5c94b1ad-cba0-3016-83ee-694ecee33e53 | -1.25032 | -55.87733 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f0596d9-29ed-302c-88d4-b2a9d9509559 | -3.01471 | -50.47107 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3572522b-b616-3191-be96-cba3b9a73e06 | -3.47004 | -50.09004 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 404b5458-04a6-3c21-aacc-3edd7f5a8af4 | -2.91882 | -54.0998 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6551038a-c2da-3f2e-a104-abefb1809e87 | -3.13205 | -53.72246 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff2cb18b-4e36-3f4b-946b-a928b7e75d41 | 1.77394 | -55.61979 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README53.md)
