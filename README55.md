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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5307208-c780-3369-b304-466699e597c0 | -2.74291 | -54.11116 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c24115c-ba51-378f-ba24-97b276954ca9 | -1.03721 | -52.99434 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c38d2aa9-8ab3-31f4-ab6f-2ba683486517 | -3.07112 | -49.20551 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| dcb08b22-7b33-3aee-b93d-9d223f10d2ab | 1.40502 | -55.90483 | 2024-11-23 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d51f0e9c-1218-31af-8e24-d341842b57ae | 1.31931 | -50.61563 | 2024-11-23 05:10:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c09a0ee-edb2-35b4-87f1-94545f635c9e | -1.73218 | -52.73166 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 1a4f53b2-98cd-32de-87a5-3a42f000e0e3 | -1.28112 | -54.53847 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 321832c5-5e2f-3466-b60f-e8578df6f417 | -1.1309 | -53.40508 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b1ee2939-1365-3a4b-8aeb-f5f9e9b167f5 | -2.59858 | -54.05819 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f6e5292c-2741-3111-84b8-4f0d0382ef19 | 1.23576 | -50.72168 | 2024-11-23 05:10:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f6379d7-0b04-3316-9288-7b68e4385850 | -2.28953 | -48.43064 | 2024-11-23 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f55255da-d486-3f65-928b-ff6c4573cf97 | -1.65783 | -52.70882 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 639c1c7d-1198-3754-8e91-76f2874bc0a7 | -1.52104 | -52.08117 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7a4ad45b-0d1c-3901-bcf2-86bba7631649 | -1.45098 | -53.39566 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 52275b07-6be2-3329-b7db-83d3c0cf1c3c | -1.62753 | -52.42623 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28d26e1d-7778-3f10-9cad-3e8605192f15 | -3.27024 | -53.81633 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 83a9bc22-3e43-3795-8c23-89b640b878e4 | -3.46188 | -51.58918 | 2024-11-23 05:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13c09a60-0b23-3ab0-b79f-49ad1d23a549 | -3.19312 | -51.35863 | 2024-11-23 05:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4ce69df-62e3-3cfa-a302-2cb7cf262143 | -5.23542 | -50.89869 | 2024-11-23 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b33b198e-626c-3757-9b16-97f6268bddd4 | -4.72317 | -45.49091 | 2024-11-23 05:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93dca831-0697-3f94-8ac8-be36e152f435 | -6.05877 | -44.04653 | 2024-11-23 05:12:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b4657185-4de8-34e7-b43b-c0340b6481ef | -4.16437 | -54.57755 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99cdb2f7-4047-30fd-988b-b9fa049205ec | -4.02955 | -54.63237 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7280cac6-3800-3daf-859f-c353544e913f | -3.70272 | -51.7884 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec388387-84d1-3b27-ac0d-7e1755eeacfc | -4.15444 | -50.0887 | 2024-11-23 05:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 65b78319-f7c6-3391-b833-3e52da322ab9 | -3.2366 | -54.24681 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0acb9495-1909-364d-80ab-dc2834d70f97 | -3.23193 | -54.23005 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce1e5fa4-3099-3355-b583-f59456f30f52 | -2.83013 | -54.01377 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cccd578e-ab6c-3656-afbd-c2e64156c095 | -3.33731 | -53.33306 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f786bdf-782d-3728-90e1-b2ff71b96a04 | -4.25881 | -48.69757 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| bda775fb-4bf1-372e-b7af-adbf8f75fcf8 | -4.73373 | -50.81891 | 2024-11-23 05:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74626ab5-1eef-30a2-b66a-3c7d964c6d75 | -2.95287 | -54.79944 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2f0a156-6dee-3501-a5f0-7b63af622f9e | -3.5054 | -53.80649 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad6e9204-0870-3e08-97af-c4d87ffc01a7 | -4.60339 | -46.49748 | 2024-11-23 05:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d8cf9503-6b1e-39a4-b118-4e455e5cfdd5 | -4.25286 | -48.70262 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| adee2189-9fc3-3013-bb13-0ab74363556b | -3.23053 | -53.9313 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3917a31-50ef-337c-80a8-8327fe340997 | -3.32145 | -54.09348 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42489c14-d995-38a3-8463-04a991e4cca9 | -3.21715 | -51.42394 | 2024-11-23 05:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 334413a4-5d00-313e-9267-9737c9d20e65 | -3.10866 | -53.99309 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c17e56a2-3ec3-31f5-9ae0-7b56a01bf48a | -3.29955 | -53.85399 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4536e8e0-22d1-3ea7-a115-1836aa642983 | -6.1471 | -46.67836 | 2024-11-23 05:12:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8413007-0fdc-3540-845b-f13c9f5e653f | -4.48276 | -48.12102 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 852ec24c-2235-3dbb-aac3-48b6fbd327e5 | -3.24482 | -54.24011 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b4bce66-3f65-338b-846e-a95970ba0fc4 | -2.80344 | -54.02318 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c079c0c6-2218-3795-85d0-bcfab193c6ea | -3.57437 | -54.68403 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04fa630a-3090-3854-b3ec-ad217e601a07 | -2.80894 | -54.08089 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c3c69fd-330f-3d30-91b7-d7179b0c812f | -5.12742 | -47.03438 | 2024-11-23 05:12:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d8215150-5610-3c17-b196-ace2b4234d9c | -3.25597 | -54.23786 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d8d188e8-73b9-3243-baec-92cdce5ca16e | -3.28285 | -53.84299 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8e9e5df-d217-300b-a062-38344d46f08b | -7.07599 | -49.20589 | 2024-11-23 05:12:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| abe6d0d7-7f69-3de9-84a8-e632df355a92 | -4.56199 | -48.02411 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a40534fa-547d-3920-908e-6415f9fa1904 | -3.9479 | -47.96886 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4db19a7-64d3-33b3-9eba-1a4986039de5 | -4.44722 | -48.18151 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e348e10-31a0-304c-aa6d-6af98db40595 | -3.3179 | -54.093 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 286d215a-6192-34f4-95ce-5fe5ab708ed4 | -4.45203 | -48.18571 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 609dbc4b-f6e3-3ab0-b9c0-6ed70b97c205 | -2.93393 | -54.28316 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b2df893-f8fb-3e08-8952-39eea429dbf6 | -3.22194 | -54.24852 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b56f71c5-2196-36aa-bf21-4ed50add82f8 | -6.49634 | -47.04232 | 2024-11-23 05:12:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 75d13700-7512-3ec2-8801-65bf4147d5aa | -3.10326 | -54.00452 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b31971b7-fd04-3b51-919c-d20c802006c1 | -3.2413 | -54.23957 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ca946a7-3ba6-36f7-9125-2eff2e067e51 | -4.19581 | -53.49799 | 2024-11-23 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 470d4520-520e-38b4-a981-024b02402b09 | -3.67371 | -54.27742 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0590da21-ff91-3f18-981b-e2390255dd35 | -3.25525 | -53.27602 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 238c33cc-f586-3db3-8c62-e8733f1f69c2 | -3.10633 | -53.98452 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98c2762a-344d-3667-8c95-18f3e2b2384e | -3.1834 | -54.33105 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a667835-3692-3062-80c2-af403ccedbae | -4.38883 | -47.77885 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47c69d85-434e-3d92-9b48-7534de7d01c2 | -3.20723 | -54.24678 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b50d505f-d1b7-33bc-ab9a-8922b80dde05 | -6.14652 | -46.68275 | 2024-11-23 05:12:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c1b0bc09-cb92-3970-bfa3-55429983611c | -4.0232 | -48.86931 | 2024-11-23 05:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa4792ae-e4ee-3a04-a13b-16c7af36bae4 | -3.28582 | -53.84766 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07fb64b3-de34-3c1f-8f81-fe36c8f7eb89 | -3.88157 | -52.07381 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 162b1cae-5eb7-3cc7-a0dc-9daa6df288c6 | -3.24721 | -54.22435 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b14c210b-db84-3603-927d-9627c218b336 | -5.75009 | -46.26752 | 2024-11-23 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8ed6f5a-5b63-3bd5-a278-8151347afabf | -3.80611 | -51.98997 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d44b6959-242a-3501-a9a5-7f5ddeb89bb4 | -3.1747 | -54.31768 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c1cb92a-e2f8-3ed1-9bba-431d986e3d0c | -3.68052 | -50.12032 | 2024-11-23 05:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 83622875-0665-3d63-93c8-8f1ae68bc4a1 | -3.2152 | -51.42254 | 2024-11-23 05:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dfef6bbf-cc61-3051-8af4-e317c621e049 | -4.17883 | -48.63904 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e300f1a0-8755-3a49-9cc8-274ced2b6b38 | -3.57882 | -51.56002 | 2024-11-23 05:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d99bbf5e-6ed4-3540-90b3-4613c6973d54 | -3.74871 | -50.00696 | 2024-11-23 05:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bf16d0b0-992c-3a93-bc6c-31ee6b444af5 | -3.1782 | -54.31824 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8994e97f-1aef-333f-9803-aba252a83d8e | -4.44584 | -48.19141 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 743f7b6c-01b5-3bf8-93ae-6ba37eb43737 | -4.44537 | -48.19471 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 17b0f7c0-688a-3a16-beb0-089e1111f059 | -3.64827 | -52.11667 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e1e2fb8-10ba-3ce5-8937-56820c7ff252 | -3.22192 | -54.24493 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62bee287-1483-3dfc-9eb1-d3857290d432 | -4.25789 | -48.69133 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8e7f83f4-ea72-3f8c-b9da-c57002d7b60a | -3.31888 | -54.76982 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79ed6082-aad9-39d5-9af4-f0b9fcf586df | -3.28346 | -53.8389 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebd9a65e-3378-39ac-aa05-08d7d4e35119 | -3.28756 | -53.86053 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c13eeb7-71eb-3c81-9173-162a4bb46724 | -5.75749 | -46.259 | 2024-11-23 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 188e48dc-fb6a-3067-917a-85cc11db6109 | -4.72509 | -45.50163 | 2024-11-23 05:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a4f82027-f7fc-3b58-8946-a25fadc8f667 | -3.75386 | -50.00659 | 2024-11-23 05:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17122639-d86f-3515-ab38-d1777a7b8db4 | -5.97035 | -46.30527 | 2024-11-23 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7455a45f-e87f-36ae-8162-73630bd95cd9 | -4.6373 | -49.54264 | 2024-11-23 05:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a552fa6-cd10-3001-8905-c5f72254b287 | -2.81344 | -54.02878 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32c98992-4f3c-3662-8ea1-e598c8561dea | -4.54405 | -45.88724 | 2024-11-23 05:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1eb4ab50-cfe5-33a4-815e-a3b4db4608d4 | -3.22781 | -54.23344 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e2822d9-f67a-306c-9054-981b8fa09f68 | -3.89748 | -50.08065 | 2024-11-23 05:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16e07859-762c-38e4-b658-0ef57d2eef68 | -3.51718 | -54.68707 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34004107-84a2-3ba0-83b1-b83954e2051e | -2.84075 | -54.0154 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README56.md)
