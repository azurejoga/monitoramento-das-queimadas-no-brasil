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
| 8a428acc-847d-3a6f-aaa7-542329229adc | -2.63155 | -46.17246 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 104612c2-282e-34e1-b77c-1467603a50b8 | -3.06734 | -50.35704 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b281be36-59a3-34f5-ad7e-76400535f2f5 | -1.39995 | -51.11466 | 2024-11-13 04:04:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cc5c1bb-da37-3c2e-bd3c-6a32c3142ef2 | -1.65903 | -52.54816 | 2024-11-13 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 690a28f6-85a1-383a-84f7-98c3a81bbdc8 | -2.72008 | -44.85695 | 2024-11-13 04:04:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a864772c-916c-3b98-a3ed-65f68a9d688c | -3.48451 | -50.84771 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31d2c66a-9654-331b-a450-4e31874c92d4 | -2.63093 | -46.17622 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec14926e-ee9d-3675-8d93-1b9091174296 | -3.06855 | -50.34982 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43755ae0-74db-32a6-8a3f-802e0d5062c3 | -3.3476 | -48.98038 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 871641e9-6b5b-3e13-998e-53d5f5f52cb5 | -2.11197 | -46.66894 | 2024-11-13 04:04:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cfee7ba-8d3b-3bdd-93fb-4ec1cf48378c | -3.02796 | -50.98015 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33d272f0-27ce-350c-a261-7fdb46f2362f | -3.3585 | -48.97635 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c38d94b8-3ac2-3fe6-9b6e-b830d4b19e69 | -3.07034 | -50.33906 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 2eacc577-313f-3b38-93f7-88b900a21d58 | -3.36036 | -48.96481 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f2c0199a-07c9-3979-b9b2-a1cfa5c036cc | -3.14279 | -54.48651 | 2024-11-13 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45ad063e-e5ea-3899-b36e-f233ba76380a | -4.1397 | -43.97631 | 2024-11-13 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0eae3c70-9268-37bc-9738-bb5577877a6a | -3.48513 | -50.84392 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb286dba-10b3-3a22-be4b-239a5138a634 | -2.49159 | -46.01356 | 2024-11-13 04:04:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 631f120c-247c-380d-ac41-ad19cc059eb0 | -3.51511 | -49.95933 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0bc395e-4bdd-38dc-a9d3-a3ada961f2d4 | -4.14914 | -48.39713 | 2024-11-13 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6160e62a-52cf-32a1-9519-dfe7eaa70a07 | -3.03747 | -50.57019 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8cbfaf9-9b10-36a8-8a27-452f8cf0b840 | -3.95456 | -48.18065 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5aed1550-7a8e-3ac9-a9b2-0991117bd5a4 | -3.3563 | -48.95829 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e826cd29-fa56-3497-b69b-6514ca5ad5bc | -3.51985 | -49.96356 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edaf7a49-1cba-3c27-ba6d-7fb1e0485add | -3.52042 | -49.96022 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c28d531-e8e5-36a6-90cf-cd7e6a78fe2f | -3.05876 | -50.34081 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ccc34050-2005-318d-9cdb-e1589d4fbbdd | -1.85573 | -47.82983 | 2024-11-13 04:04:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afef6cb1-1472-3a15-865d-019ad6ed118f | -3.14747 | -45.97887 | 2024-11-13 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a67bada-df6a-3490-84fa-a4e502f3f63a | -3.04718 | -50.34253 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| af304692-6c7d-3aae-8b04-03654ce87eeb | -3.35953 | -48.97165 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec83a72a-1848-3abf-b72b-499164b06443 | -3.09975 | -54.3163 | 2024-11-13 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e9ccde48-3a44-3c3d-839c-8a42165225ca | -3.09609 | -54.30849 | 2024-11-13 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7fefffb9-031e-3079-8d22-390807ad5249 | -2.24836 | -53.74957 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 31714ed4-f412-3178-b775-7e28e512093b | -2.24728 | -53.75592 | 2024-11-13 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a1414a00-036d-3b47-9a39-8f895543f727 | -3.34854 | -48.9746 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d663b77f-c151-3f63-9ac6-e6dd00bf5b0b | -3.1641 | -50.45468 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ccc5a99c-9147-3b86-b3ec-2013c2ab3a36 | -3.06915 | -50.34621 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80911a41-c8d0-37fc-bb84-4a9d498df508 | -2.66043 | -51.73042 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 486dfc91-2c35-3707-b789-8acecb230e62 | -2.12858 | -50.69508 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 428375fc-c182-3114-bebc-e8e0144953e4 | -3.35151 | -48.95857 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1bd93fce-2154-3bd6-b260-25a9ed97faae | -1.03369 | -48.84761 | 2024-11-13 04:04:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4cdbf321-ae16-3bea-8f43-a23ac61095ea | -2.7349 | -45.29785 | 2024-11-13 04:04:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8bc6724-34b6-39ae-a5fc-14f319943eeb | -3.05505 | -50.3293 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 92e3a141-9218-3954-be00-a3d86f68f243 | -3.3486 | -48.9757 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 557258de-75c1-316a-a444-f3b871809435 | -2.93314 | -40.22008 | 2024-11-13 04:04:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 880c2795-b0a1-3094-b2ea-49d8e7bfe571 | -2.28149 | -48.81297 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2ffc4151-8c3e-3fc6-8061-7920d6f1007e | -3.1635 | -50.4583 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8520eb22-9d70-3d94-a94e-46fa0a14c27e | -4.57856 | -43.9723 | 2024-11-13 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5702c44d-8a1a-3b3d-8c39-c7df7eaa9074 | -2.99065 | -51.34704 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7bf1aea8-bfdf-3558-8447-bca96c14d079 | -4.34122 | -43.82499 | 2024-11-13 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 746fb31a-89bb-319f-ac42-9914a7f7a508 | -3.76118 | -50.70564 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bfdd60f-3aaf-386e-a8ef-3ebb36524ed0 | -3.95372 | -48.18567 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9602a2e-c261-3e66-8a15-6bd703430410 | -2.37609 | -48.5183 | 2024-11-13 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35c9c1a4-3d0d-3f18-bb73-bf89b2e8720e | -2.63571 | -46.17312 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc0f945f-993a-31c6-9a2f-15faa1a1deee | -1.82676 | -45.92065 | 2024-11-13 04:04:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e45239da-7005-314a-9fe1-151f3ec6d7af | -4.36619 | -44.10284 | 2024-11-13 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1c0c818d-ebb8-3528-80b4-72f1f273d1b7 | -2.52948 | -46.21141 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af76c17b-d966-3c0c-b8c7-ac1abfaa3125 | -3.35745 | -48.9537 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d64fb207-ea75-3194-8c33-f9335f152669 | -2.69705 | -49.34438 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0f2635fe-2ce6-387e-8099-c75c6a2113e9 | -2.8758 | -40.30259 | 2024-11-13 04:04:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dc951282-31b7-38ee-9b90-1ef61fc75ed8 | -4.15385 | -48.39801 | 2024-11-13 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| afceadca-6820-3e06-aac6-d8132521cf8f | -3.76794 | -50.69944 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19da785b-2f94-3a84-b0ed-064a20422fed | -3.34762 | -48.98143 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9242a87c-e361-3ff4-b404-ac33dae6b696 | -2.59077 | -48.19989 | 2024-11-13 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6aa72d88-da6a-3ff5-ad19-1c742df8ab62 | -3.29728 | -43.51288 | 2024-11-13 04:04:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb86cf34-0101-3013-af68-cb5afeafab87 | -3.34168 | -48.98621 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd9d322b-469f-335b-ac4e-a6a23ba6121c | -3.72703 | -45.95155 | 2024-11-13 04:04:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| feadb333-9fda-3eff-b696-4b8f4013abc4 | -3.35358 | -48.97657 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 29657050-d5c0-3f28-87bd-4eb59020927d | -4.37116 | -44.10658 | 2024-11-13 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 59c9717c-8795-3823-a76d-bc4d61186d5a | -3.25325 | -50.39618 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de6b5668-e111-3e43-a0fa-8fb19d56adc7 | -4.06478 | -45.87386 | 2024-11-13 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26b56f77-d322-3f57-9dce-58d1c4953c08 | -0.66083 | -47.31992 | 2024-11-13 04:04:00 | NOAA-20 | SALINÓPOLIS | PARÁ | Brasil | 1506203 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bd0c780-edbb-3f48-a973-696aa162746a | -2.46062 | -50.12611 | 2024-11-13 04:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d7b7900-8636-39f2-8401-24a12fc4016f | -4.71135 | -42.78919 | 2024-11-13 04:04:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85cf417d-a5e3-362b-a000-35437f312e71 | -2.71854 | -44.85895 | 2024-11-13 04:04:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 20c52830-0d72-33a5-9e58-ef9e6c0cbf4a | -3.34148 | -48.98658 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5360f337-504b-3a6a-9c8d-e85fb612e7bd | -3.51928 | -49.96693 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9de5f55-998b-35e3-80f8-5b0456af788c | -1.20691 | -52.12893 | 2024-11-13 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad8dbad7-1910-3d1f-ab54-978622c5cc39 | -4.36757 | -44.106 | 2024-11-13 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 4d433ccb-2e78-3748-b6ce-9c72bf4c8df3 | -2.69602 | -49.35067 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2f3b0124-264f-326a-a500-9e30babc0cde | -2.63633 | -46.16937 | 2024-11-13 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7201a8a3-8567-30b3-8b83-08ebc0de5c4c | -2.77535 | -50.30901 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8598ea8-b644-34f3-9e63-2f7620dcfb10 | -3.02287 | -50.97527 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| becfb18b-ff13-3f95-935a-60ee618e4640 | -3.3365 | -48.98566 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f0c6dd5-ef94-3823-94dd-ade6dd2f6b41 | -3.15871 | -50.58988 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cf22d288-f38e-31a2-bbaa-8bf743c623ab | -3.04837 | -50.33544 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1fd07eb6-7df2-3a53-ac17-a3f9b1a83da8 | -2.70796 | -47.73009 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39e0124f-c7ad-3bab-bffe-b34aa08de2b3 | -2.99133 | -51.34304 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 53085c3b-718b-3c81-aab5-16b1c8ed48f2 | -3.33198 | -48.98196 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bb75403-9a7c-3fe9-91ef-9018a3a2d050 | -3.02494 | -50.97029 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f01855a4-e8e3-3786-8a01-a95597d67f1e | -4.13812 | -43.08184 | 2024-11-13 04:04:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cde937fa-6496-3a0d-8779-a471d6e9f01e | -2.69549 | -49.35384 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54f78e15-45dd-3d34-ac7f-2e45f2d27f57 | -3.35943 | -48.97057 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0cd31440-4a54-377f-b665-e7f8483735c3 | -3.51565 | -49.96525 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eabe88ce-d87a-3854-8fd2-89d0f3186a9b | -2.66296 | -46.82782 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4dde08c-62b9-3182-b32d-703eddad0482 | -4.42867 | -44.02378 | 2024-11-13 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba43f35e-a2c7-3fc9-aad1-dbbdda45ffbd | -1.65258 | -52.54703 | 2024-11-13 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ff2b5c47-033b-30d1-997b-e6ee8db5808e | -2.78145 | -50.3063 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6c6eaaa-c3fd-3e17-b581-70d4d66de3bc | -3.3336 | -48.97203 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f42463df-b606-3b35-ac82-66f76e22bc6c | -3.74992 | -46.17164 | 2024-11-13 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README18.md)
