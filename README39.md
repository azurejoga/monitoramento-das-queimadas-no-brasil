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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddf3b8e7-6482-3621-bd44-d669c2488c73 | -4.47523 | -49.63832 | 2024-10-23 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9148a783-7bdd-305e-b945-4ded02e6005a | -4.4249 | -49.80412 | 2024-10-23 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 78eb41d8-1d1d-3251-b7b8-eccc8812aa17 | -4.42143 | -49.80361 | 2024-10-23 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a34250df-d668-3721-9995-2340fd43988e | -4.42092 | -49.76034 | 2024-10-23 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5804a05b-c823-3c67-8aec-568921c9319e | -4.41744 | -49.75982 | 2024-10-23 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1525fbad-540b-3966-aa4b-a696ed558007 | -4.38411 | -49.75552 | 2024-10-23 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6c1ae1b8-e597-3c39-a130-eaf09886e60b | -4.38352 | -49.75933 | 2024-10-23 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b76474e4-fe6b-3177-97e5-6665043fc851 | -4.37909 | -49.41565 | 2024-10-23 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 453762ea-ed89-3ff0-b2f3-fbaf872de838 | -4.19628 | -49.40169 | 2024-10-23 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cc25c81-f34c-3210-8312-94c42340f85b | -4.19276 | -49.40114 | 2024-10-23 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cdfafffa-b240-3855-8456-5ed6357b8e68 | -4.15528 | -50.21264 | 2024-10-23 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8f8c60e-3442-344e-9cb3-a087365856cb | -4.12985 | -49.29108 | 2024-10-23 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25832e25-1e8f-307b-a9f9-a7aa3282bba9 | -3.98371 | -49.95955 | 2024-10-23 04:51:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cee40ad1-f82f-3183-a374-4bd12e1b7174 | -3.80067 | -50.03106 | 2024-10-23 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e50782d-e55b-33b7-bf26-52a3824f9c5e | -3.79783 | -50.02683 | 2024-10-23 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 948daeee-de74-3817-ba99-11323908ef71 | -3.79725 | -50.03053 | 2024-10-23 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8718ba51-f972-3e8e-a911-c65ec66de47c | -4.9843 | -50.77082 | 2024-10-23 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ebcf556-5db1-3f41-8566-0123a3848afc | -6.44765 | -49.91516 | 2024-10-23 04:51:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d8665fa7-fe0c-3205-aacb-7b4a5157f636 | -6.43038 | -49.90587 | 2024-10-23 04:51:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1ec2979d-1aaf-334c-992b-721e62105055 | -6.4203 | -51.11214 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8657c4d7-7f2f-3bf2-b470-df94cca8d516 | -6.22551 | -50.89677 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 244c6a04-6b9a-308b-a707-d84a642850e5 | -6.22213 | -50.89626 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ce7f99c-4061-3eb2-b155-aef11ac7233a | -6.22097 | -50.88122 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 917ec516-9e9e-3c98-a86e-a382c17edc90 | -6.21758 | -50.88068 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ce03023-3f07-35d5-af23-12238fcaa106 | -6.21137 | -50.87596 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6404fb8d-9df1-37f4-a439-26bf7d4907ed | -6.20799 | -50.87542 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f30e816-80d9-3007-a1ac-61697d0e62bf | -6.20743 | -50.87907 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cb7dd1a-bf1b-316a-b035-7a0035b5039a | -6.20571 | -50.86762 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a56633ee-bd26-3e9d-bded-f5e64e1ad9a4 | -6.20232 | -50.8671 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69349563-d78a-3404-8991-ed406f4b8d7c | -6.18878 | -50.86493 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ab1df86-9357-389a-ab14-b1f542aafb24 | -6.1854 | -50.86441 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f5feec3-af92-3fca-8d8e-4817751fa1df | -6.18352 | -50.86839 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 359d1f18-ae99-3e93-bd08-0443eff209fe | -6.18014 | -50.86787 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b186cb6-4e09-3a2b-b858-dab1f972cfb3 | -6.10583 | -50.9681 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15663580-4c80-308c-85f8-b8ae4d2e940c | -6.10527 | -50.97173 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ebd97ae-47af-3742-b5be-88a27b6de0a3 | -6.10472 | -50.97532 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55b65a03-b27e-32a3-a1e8-443510074a5d | -6.10245 | -50.96759 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aeb7eacf-77ae-3991-b930-031eb49e2495 | -6.1019 | -50.97121 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5aab11a1-2bb5-3b97-ba96-f4e0ba03040d | -5.85404 | -50.0496 | 2024-10-23 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23211c9c-4c5d-3354-a456-0f22a1b8eb86 | -5.75676 | -50.22231 | 2024-10-23 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7070547b-4f97-3cab-a62d-13480f4c0d8b | -5.75619 | -50.22608 | 2024-10-23 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e384a2e-6971-3b61-9892-d8c94b36ff6b | -5.75331 | -50.22177 | 2024-10-23 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7ef39c7a-555e-3d09-9672-f067ba1720d1 | -5.75274 | -50.22554 | 2024-10-23 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5184f0d8-1003-3dea-81f1-a7e58f2bc03a | -5.67907 | -49.77338 | 2024-10-23 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 611ee001-0d74-3f48-8c0f-e6ed0f523899 | -5.61412 | -50.01045 | 2024-10-23 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cf3e92b-bd72-3bb9-9b59-8c4c0738bef8 | -5.26555 | -49.92379 | 2024-10-23 04:51:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e755244-15b9-3f38-a225-85d3cb48a625 | -5.24279 | -50.87628 | 2024-10-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| aa0503dd-4021-36cc-acc3-8fb4eb0acff6 | -5.24224 | -50.87987 | 2024-10-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7dc1f77a-7976-3451-8db4-b702d6dbe737 | -5.23721 | -50.89013 | 2024-10-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f252ba1-79af-34e0-a44f-e48fefec62ce | -5.22741 | -49.85898 | 2024-10-23 04:51:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85790678-015f-3858-bc79-ca293182968c | -5.20003 | -50.08229 | 2024-10-23 04:51:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 355f5812-a561-3a25-a65d-7012c75fca28 | -5.19404 | -50.16653 | 2024-10-23 04:51:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8b6bf55-bdc7-3815-9635-a56249b03b16 | -7.98154 | -50.16298 | 2024-10-23 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f1d77e2-24eb-371d-bb05-b2a8cf962e46 | -7.978 | -50.16244 | 2024-10-23 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13971ff6-d908-37c2-b5aa-375b915de49f | -7.9774 | -50.16644 | 2024-10-23 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d7e1ebd-aadc-30b4-a81f-541c4fda8941 | -7.41358 | -50.51402 | 2024-10-23 04:51:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ddefa5a-98ec-31a0-ba94-bf3875e08807 | -6.78576 | -50.88079 | 2024-10-23 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 132b6352-afd8-336b-9637-12ce0bcbec30 | -6.42367 | -51.11265 | 2024-10-23 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71faa961-d1b1-3657-b15a-caa66e941358 | -7.98453 | -50.6753 | 2024-10-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5f181a7d-e841-3eea-b2ca-7b3e4f346efd | -7.98396 | -50.67914 | 2024-10-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7471fe10-f59f-3614-a6aa-b31f6e5e57a5 | -7.98107 | -50.67477 | 2024-10-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 28df62fc-3aab-39e3-adea-fd3524cf3b54 | -7.9805 | -50.67862 | 2024-10-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fef0133c-a83f-3144-934d-60ee6a6c8b47 | -2.23658 | -50.45739 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df02c231-942c-3e99-9d95-90549216a551 | -2.21986 | -50.45863 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7f44133-579c-37bf-9cfe-9ac26c5e4569 | -2.20614 | -50.87152 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 170ea090-856c-3c52-8c12-c452045b0924 | -2.20282 | -50.87101 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd145dbf-7a63-333f-9bc8-c985f65e339a | -2.16465 | -50.70139 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11646934-1855-3ac2-8c30-f5a07e9371ee | -2.13727 | -50.8325 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4036913-65fc-36f9-a591-0ed350460266 | -2.13395 | -50.83199 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a28d767-ed6d-3455-81ec-bbb92988b467 | -2.11097 | -51.10801 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c303c2e-09ed-3873-9af2-e31f66a8fd3a | -2.10658 | -50.92 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f860680f-d0b0-357d-adad-47c5e448e79d | -2.23992 | -50.45791 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be7f3fc1-8563-3354-a41c-902886d04b87 | -2.07306 | -51.13386 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 339187b1-a68d-397c-ac5a-f6a039ed20df | -2.06591 | -51.13628 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ea38179-45a4-3dcf-aa46-74b5b871831f | -1.86829 | -51.35808 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed4c17c1-d0fd-379e-8475-13ac444d05f5 | -3.43131 | -52.02244 | 2024-10-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1ad5a4f-995e-3363-8252-4302c6009130 | -2.60876 | -51.77651 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d31fbb43-45cd-3c3a-9106-393e6fb09edc | -2.60493 | -51.77943 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 719e2717-bdf3-3a1c-b538-8beab1ad67af | -2.60392 | -50.83008 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d39e57d1-25fb-3499-8e48-d18fef3f857b | -2.47921 | -50.47337 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44671791-9196-3cf2-9332-3ea88dd6859e | -2.47194 | -51.97629 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f66119fe-e176-33d4-91ff-7e112769a318 | -2.46972 | -51.96892 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f29d501e-52d2-30d0-a504-e857d4895247 | -2.46918 | -51.97235 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 05892552-ef8b-35a2-8af2-bbd7b3b9d949 | -2.46864 | -51.97578 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1948354-08dd-3250-9bcf-6672de4d9077 | -2.46642 | -51.96841 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8c58b3d-ddf7-3d8d-9631-795bbed58b10 | -2.41361 | -50.48104 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0160382d-f938-30d3-8448-f13af82e2232 | -2.41306 | -50.48457 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76033169-5fa3-34b6-a7c7-64aa576075d2 | -2.41027 | -50.48052 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65eb179a-8ec9-3b8c-91ff-e17533fec5a9 | -2.41021 | -50.4371 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 869b94f8-077d-35c7-ae89-88a2e3a242ea | -2.38509 | -50.92454 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e1c9eec-3b54-3468-81f6-3e71060c2271 | -2.30315 | -50.75125 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a3c1607-b6c4-3ce0-82af-97248d4ddba1 | -2.29412 | -50.69982 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ed96844-a46a-3b94-8377-5ae49bf829b8 | -2.28672 | -51.13884 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e406dc86-996b-3d9d-bd34-81f9097c6fb4 | -2.28342 | -51.13833 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5c47046-3232-32ee-950b-7f3d4a4ab20c | -2.2106 | -50.88641 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 613e6437-effb-3c8e-b8fa-39b7eee75bdd | -3.45717 | -51.20544 | 2024-10-23 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d60ebdbd-11b5-3408-b168-92a2efa83a57 | -3.38949 | -51.18033 | 2024-10-23 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0049fd33-6091-3aae-afe1-fa8fd1226bd9 | -3.2772 | -51.40006 | 2024-10-23 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad46e707-b9f3-3062-9a91-a316eb94ccd9 | -3.24427 | -50.84759 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c942262-c79c-3a19-92b6-0d9bcb38d745 | -3.24094 | -50.84708 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README40.md)
