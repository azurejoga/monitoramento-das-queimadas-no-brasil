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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d8d2b00-7ba1-3012-89cc-3071965b040a | -1.93821 | -52.09755 | 2024-11-26 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea571ce5-fa06-3dff-937b-557b19a0cc7c | -1.92567 | -50.58151 | 2024-11-26 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 837d0ab8-cb37-363a-9407-9405849e0682 | -4.31513 | -47.51123 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| c32329d0-b511-38e3-9a45-e72df52d06bd | -3.9496 | -48.06958 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d29143d-8828-36d9-849b-93879cc33a09 | -6.3158 | -39.51933 | 2024-11-26 04:14:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 23dc88ef-47e9-3799-bcb1-05665e55bc15 | -3.95074 | -48.0882 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e36412b2-c752-3157-ae44-259cd725cd62 | -2.7214 | -46.2659 | 2024-11-26 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51894ea4-ddb6-3595-9147-e0382b074eef | -3.97483 | -48.06934 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 47d74a75-7190-3813-aa51-6b96a06b15a5 | -2.94504 | -48.55923 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b682f698-9d10-36a5-8aeb-46522baf01b8 | -1.98609 | -53.2914 | 2024-11-26 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc960730-9c24-3067-ae2d-a423134c80c4 | -3.97496 | -46.72772 | 2024-11-26 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12975fd5-9dec-3d78-afea-9e9ce0ea4c0f | -3.97588 | -48.11454 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed8cd5ac-c49a-3136-ab00-1d8b80a3aef7 | -2.32443 | -46.1244 | 2024-11-26 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9f9dee7f-9ae0-3b60-be89-b4cc7fdd7d1f | -2.59802 | -46.26195 | 2024-11-26 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eda43e71-391a-3fbe-8d8f-2568352cd671 | -3.38233 | -44.17299 | 2024-11-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f246191-1353-3f20-be14-2ef677c17f99 | -4.95162 | -47.8002 | 2024-11-26 04:14:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b3ccab4-d8b4-3f20-8c54-eb06d1a4c4c5 | -3.91581 | -42.42032 | 2024-11-26 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 1cb98583-924b-35c3-b57a-4c1b89e0b45e | -2.71782 | -46.28814 | 2024-11-26 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 99b9ed85-e018-38bd-8161-e7c71896ac20 | -3.90973 | -42.41586 | 2024-11-26 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 134703a2-6db9-33af-b53e-a92c4725e027 | -3.36168 | -41.6525 | 2024-11-26 04:14:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f80122e7-0eb4-3028-9bf2-cae6fb5b8b87 | 0.96943 | -50.13018 | 2024-11-26 04:14:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48e7c0fa-784a-34cb-a3e2-965bde0c76b4 | -2.54746 | -46.40302 | 2024-11-26 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ebda53b-e3f3-3954-9f49-0d405b19b710 | -3.96185 | -48.09736 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c02bc73-9d21-30b7-a483-63514201fb8f | -3.97126 | -48.09125 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 55c094f0-3c86-35d0-a534-9ad0252bf596 | -4.25073 | -48.66606 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e52a851f-f429-3267-b296-bee308573f12 | -3.97312 | -48.05415 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7a8520fe-8380-339e-959a-f2a847014723 | -3.96312 | -48.06398 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 09ecefad-9faf-3a74-be5b-1d440be8d545 | -3.9766 | -48.05853 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 554099b9-81e3-3c30-a9f2-c4c0d3fe922d | -3.9502 | -48.06595 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 081f1662-2fa2-3eeb-b448-10339eb7c25a | -4.81142 | -43.30904 | 2024-11-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4afb5a8-c6db-3ec0-8d4c-5a2b963df5b9 | -2.48937 | -49.03121 | 2024-11-26 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1541c889-3cfd-3c05-8311-6236111567b1 | -0.75543 | -47.27044 | 2024-11-26 04:14:00 | NOAA-21 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4dbe5e0c-cea8-3015-94ee-b1a578889c5a | -4.51482 | -42.06674 | 2024-11-26 04:14:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5ae2dc63-1d0c-3d36-8366-bd9c3f26ebe2 | -3.98414 | -48.0637 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c002ea5e-9d5b-3e0f-9a4b-791157e868e7 | -1.98949 | -53.29359 | 2024-11-26 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 688ed43a-1026-3b85-9e87-39b3ffcd4c08 | -6.03278 | -39.36384 | 2024-11-26 04:14:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 68b3ed35-3744-3a4b-83f6-3064e4e708bc | -3.07743 | -49.19827 | 2024-11-26 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 3fcb303c-9f45-36fb-bb89-2b4beeee8fa4 | -4.83817 | -42.91759 | 2024-11-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 706e1f85-1c1d-399e-80c9-08924d2708dd | -2.59896 | -45.40496 | 2024-11-26 04:14:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 675b6cc6-0044-308e-a3ae-36abcbb4679e | -3.97892 | -48.07 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 05140f0c-9d13-34ba-8e76-3c00a09f3308 | -3.97067 | -48.0949 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 81fd38df-addc-3cdc-bca9-da66892e093c | -4.95215 | -47.80349 | 2024-11-26 04:14:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38d34559-2828-30b8-93e4-02784aefbcdb | -3.59852 | -50.38911 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 2e658c42-c184-3d10-ad33-79e1f61b4379 | -4.95431 | -38.52658 | 2024-11-26 04:14:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| afccb6a6-bf65-357e-a9b1-8c7760282c6e | -4.80481 | -43.30802 | 2024-11-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd6d561d-78fb-39f4-8a2b-f25416433ccb | -1.99209 | -53.29234 | 2024-11-26 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f8a8162-ab04-3566-a1ee-a11513080cac | -4.35413 | -48.56269 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6e25225d-50af-3fda-96ad-14eece690c83 | -3.96132 | -48.07495 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 17296bef-3cf9-3e0e-9f73-cffa7b1e85db | -3.8381 | -41.56341 | 2024-11-26 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ba3a65f3-657f-303d-a353-ddb9054e0a02 | -3.97709 | -48.10711 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49979275-70c3-3d7f-8c16-4973759ef76a | -3.38054 | -50.09753 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 519a07c2-a0e3-3522-95c0-e110b436381a | -3.97829 | -48.09976 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c37c1f7-44ca-30a7-83cc-fd1e42daab80 | -2.60533 | -46.81438 | 2024-11-26 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae015b26-e0d1-32f1-9897-57e0a5f1dd0a | -5.31271 | -39.79434 | 2024-11-26 04:14:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 76c0d949-6a05-3986-bddf-c2922ed4174d | -1.63131 | -53.87133 | 2024-11-26 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6282b4d-16cc-3f9f-980e-cf34d9fa5ef9 | -4.42643 | -48.70535 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1afcd785-bebc-340a-9bfe-3f5d9c8bb27a | -1.43197 | -47.31766 | 2024-11-26 04:14:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5a6c0d69-77e5-30c0-8312-606c755357f9 | -1.78645 | -52.74035 | 2024-11-26 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1017383-df02-389d-b9b7-7c12059edc75 | -3.6577 | -50.23838 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9243c9e3-938c-3308-9cc2-067da7345dc1 | -3.9508 | -48.0623 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19992ef4-b4f6-302a-bde0-1a590f05aa75 | -0.94432 | -46.78253 | 2024-11-26 04:14:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd4d29b4-a064-32d4-a01b-bc4484e3ec26 | -3.97246 | -48.08391 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd786847-a19a-3532-81ea-17a93fb9659c | -3.96414 | -48.10909 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 431d78c0-7976-3fbe-a58e-0f0da78500b2 | -3.38908 | -44.17404 | 2024-11-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 42447574-d035-391c-95c6-8ca42784c47a | -3.837 | -41.57048 | 2024-11-26 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6e68850b-86fd-3272-adcb-076a438c73f5 | -1.98877 | -53.29805 | 2024-11-26 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a151050b-c0c0-302e-9768-efde60018bcf | -3.50371 | -50.4594 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d858ac51-42b4-304d-8518-a1b600a854c8 | -3.97134 | -48.06503 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 52d93570-dd13-3c24-9437-629f663dab35 | -1.73739 | -45.69045 | 2024-11-26 04:14:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef0a6abf-cecf-369b-9f69-d2a861d2e167 | -3.2769 | -50.01841 | 2024-11-26 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 08a9ece5-7fd3-3d0f-b7c2-8bebbea892c0 | -4.11476 | -48.48849 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df7524ed-c845-3900-9694-bab53e69c91f | -4.86722 | -38.38437 | 2024-11-26 04:14:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 86f8832b-8b94-36e8-97e7-5590f017613a | -3.95339 | -46.51841 | 2024-11-26 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05f4ed7c-c689-30b8-8f7f-b5b9a164a984 | -2.93816 | -48.82617 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be4553e4-17c1-31cc-9050-b2c68c1b934f | -3.96723 | -48.06449 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 194fd500-5e64-3f5e-87ce-449bc9c2845d | -3.95953 | -48.08586 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8da38b54-b9be-3ebb-9980-36d50511a6c3 | -1.78064 | -52.73944 | 2024-11-26 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a02fb0e8-3eb0-3c9c-b14c-a5afcaf39910 | -3.9777 | -48.1034 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ebcde40-6ece-3cb4-891e-fdb8078055ab | -3.59458 | -50.38299 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 958af52e-48fe-3fdb-993b-86749d3b652b | -4.26283 | -48.67197 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c7a4967-8046-32af-8527-1a1004e1cdb5 | -4.16441 | -44.06821 | 2024-11-26 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 600df15e-7a7a-31d5-8e25-d92a4fbac30d | -3.51842 | -50.21928 | 2024-11-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a70c8d21-f99b-341c-b7d7-0f0b9240bf56 | -3.97074 | -48.0687 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| dcb4dd55-1759-3f0c-bf89-211dc48e70bc | -3.96656 | -48.09431 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe009c52-ec29-3ec0-8f12-7cae80092dcb | -2.56025 | -48.1993 | 2024-11-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40a5a6b7-cb9a-3fb7-b2ba-1d87048391d5 | -3.95552 | -48.05914 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 488c3b3d-66a9-3a2c-9672-2b5128f6dba0 | -3.48047 | -48.22813 | 2024-11-26 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75c269af-4639-3e2d-a72c-352854ff2b26 | -1.92159 | -50.57495 | 2024-11-26 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61f957d8-2d59-3173-b981-bb949d4f73b4 | -4.24518 | -48.5929 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a22cc2b0-0e87-3d7b-a0e3-aa05ba6f2162 | -4.72492 | -43.25265 | 2024-11-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1b056079-e00a-3fe3-b4a9-368913f7f861 | -3.97424 | -48.07296 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c426df28-0ce6-3486-8e05-982ebe8b5f6b | -1.98534 | -53.29584 | 2024-11-26 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c9a0638-877a-38a1-baac-3b4ea762ba38 | -3.28075 | -48.75329 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6a6716b-8d9c-3ec1-b4cb-93aae0633b3b | -3.97656 | -48.08453 | 2024-11-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16398610-17d2-3172-b5fa-426b75f56662 | -1.48265 | -53.81235 | 2024-11-26 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 061e089c-3d37-3eca-8e50-15dcfaee5a01 | -2.64538 | -48.4818 | 2024-11-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5898ffc6-ea3f-3c11-8de4-1b88b05a84cd | -4.23715 | -48.6963 | 2024-11-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ec51f95-4aba-38ce-8b52-4ea975c33147 | -3.7007 | -43.42775 | 2024-11-26 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88bfb540-cf7b-3f2b-9c4e-3688f9fde904 | -3.05285 | -44.74313 | 2024-11-26 04:14:00 | NOAA-21 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79dafe1d-7fe7-3c74-92af-e3b53c0da2c1 | -4.54289 | -43.56766 | 2024-11-26 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README17.md)
