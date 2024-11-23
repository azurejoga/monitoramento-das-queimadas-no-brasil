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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 564ae80a-683b-349d-a5b6-c750614d3a94 | -1.5352 | -51.9436 | 2024-11-23 13:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 24fcaf75-de39-3541-9f25-43e25d9f9d7e | -3.4102 | -44.6055 | 2024-11-23 13:50:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| a44fa34c-5c97-32d5-8f29-7dda5bd47b12 | -3.5397 | -44.759 | 2024-11-23 13:50:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 12a6304b-4631-336c-ba39-11dd4c8e8691 | -5.3295 | -44.7956 | 2024-11-23 13:50:00 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| f28f0a39-b8df-32d4-81a8-93e5504170fd | -3.5906 | -42.3476 | 2024-11-23 13:50:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 125d18cb-ef8d-3d22-8bce-d4a7c66e2391 | -5.1185 | -43.1497 | 2024-11-23 13:50:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| ed3274bb-0384-335c-b14d-30621381ae8b | -5.0998 | -43.151 | 2024-11-23 13:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| fc491e28-826b-3c12-b165-e2f281410f97 | -3.4612 | -42.0934 | 2024-11-23 13:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| b400fda5-0371-3c53-ac1f-55edddf6e7de | -5.3297 | -44.7728 | 2024-11-23 13:50:00 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 5275f6d4-141b-3b4d-98fd-e35eca419a28 | -3.5395 | -44.7817 | 2024-11-23 13:50:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 35a9d795-a040-3dfd-be14-01dcfaf32139 | -3.2386 | -54.223 | 2024-11-23 13:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 5388bd89-7bee-31f9-a98d-bb84caaf01f3 | -4.0737 | -48.9622 | 2024-11-23 13:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 42fb60d2-61a1-3c19-8c6d-032db47d9588 | -7.654 | -37.4046 | 2024-11-23 14:00:00 | GOES-16 | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 130.5 |
| 9dd11b93-c0fd-307c-92e9-effbadd9d227 | -2.3076 | -46.0614 | 2024-11-23 14:00:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 17037441-ec0a-39a4-b809-5c9015705969 | -3.8776 | -47.5461 | 2024-11-23 14:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 0d6975a1-c6b1-3e1e-8d5a-0800d484be90 | -5.0998 | -43.151 | 2024-11-23 14:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 9eb8d9cd-642f-33b2-8dfe-4a8b87df5735 | -5.3295 | -44.7956 | 2024-11-23 14:00:00 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| bfd37950-07e9-3440-92a7-9093cffcc285 | -4.2606 | -48.6755 | 2024-11-23 14:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 26961509-e041-3f44-b67d-d0c66efda6d7 | -2.783 | -43.3433 | 2024-11-23 14:00:00 | GOES-16 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 322.7 |
| bde239aa-4bdf-33c6-8287-00a04be45c80 | -3.3915 | -44.6063 | 2024-11-23 14:00:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 36985989-ebc1-3438-b091-6231c71f4e46 | -3.1831 | -54.3247 | 2024-11-23 14:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 90945556-9c51-3b25-aaf8-ca731d885a7b | -1.5493 | -54.3357 | 2024-11-23 14:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| ae52b769-0c43-303b-bc00-d5f9f40b26a4 | -2.3076 | -46.0391 | 2024-11-23 14:00:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 2ac0c429-14a5-3587-8d03-4da71292f579 | -3.5906 | -42.3476 | 2024-11-23 14:00:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 6db8e871-519f-36c5-81e4-b985c351795b | -5.6213 | -43.4866 | 2024-11-23 14:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| fff9ff11-8f0a-3c89-9f7d-1acebd1bd1ee | -2.4197 | -45.8355 | 2024-11-23 14:00:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 44a97806-891b-30ea-8711-ee82b690fc46 | -7.3916 | -39.9839 | 2024-11-23 14:00:00 | GOES-16 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 148.1 |
| 471431e7-fbf6-370f-ae2b-5136fbd21783 | -6.027 | -42.2316 | 2024-11-23 14:00:00 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 9153aacc-13ba-3698-b6d1-1791a40fe3e9 | -5.3297 | -44.7728 | 2024-11-23 14:00:00 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 561440af-a46a-37ba-a07d-ee7f71e5adae | -1.6245 | -53.3084 | 2024-11-23 14:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| e1beebc3-84b0-3cc9-9224-f5b8e9ed6be8 | -3.477 | -49.9197 | 2024-11-23 14:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| dca30eab-9b27-3286-8a88-be00212b4b5a | -5.0996 | -43.1744 | 2024-11-23 14:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 8fb009a0-656f-3cbf-8e82-c21341e747f8 | -7.3727 | -39.986 | 2024-11-23 14:00:00 | GOES-16 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 191.2 |
| bdd2662a-e1b1-3e4d-9875-ed304453f3d3 | -5.5665 | -43.3277 | 2024-11-23 14:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| c0b5d716-2464-3202-bb72-cc301b0566cb | -2.9619 | -44.9639 | 2024-11-23 14:00:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 91.4 |
| a717033d-a24c-30aa-bd98-27c18f04dcec | -1.9672 | -48.3865 | 2024-11-23 14:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| d475acfe-93c6-3c56-9327-79ca29da61fe | -2.7831 | -43.32 | 2024-11-23 14:00:00 | GOES-16 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 172.9 |
| a6c1d869-9b93-30ab-b53e-9389c74b856d | -2.962 | -44.9412 | 2024-11-23 14:00:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 147.9 |
| aa176e23-7368-3ce5-8d1d-9d3baf9e88af | -1.5352 | -51.9436 | 2024-11-23 14:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 8a276297-c33b-381f-964b-72e2cb73e373 | -3.2584 | -53.8204 | 2024-11-23 14:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 0735a20f-24cd-3d50-9d9b-ff56d117e4aa | -5.7146 | -43.5261 | 2024-11-23 14:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 5fe0bf8f-b767-307c-86e8-1c1b4ca82cf9 | -7.3723 | -40.0109 | 2024-11-23 14:00:00 | GOES-16 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 93.6 |
| 00c5ecfa-29d2-3409-b42f-90bb2822690c | -2.8 | -43.32 | 2024-11-23 14:00:00 | MSG-03 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 277a1ec3-e9db-3230-915f-af9e6e54c47c | -2.78 | -43.32 | 2024-11-23 14:00:00 | MSG-03 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3619a25f-8cc7-3680-90eb-9072f164a93c | -4.55 | -42.88 | 2024-11-23 14:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f74193e1-8afb-34af-bf5d-03bb058139b8 | -4.52 | -42.88 | 2024-11-23 14:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a903fd92-dfba-3731-97aa-43fb72005f80 | -4.52 | -42.92 | 2024-11-23 14:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39d29730-a6b9-3435-8a61-4676a604c0e1 | -4.26 | -48.68 | 2024-11-23 14:00:00 | MSG-03 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccd0b073-4ca1-3b53-b37b-ca5434eb24b8 | -1.5352 | -51.9436 | 2024-11-23 14:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 00bef738-bfa3-359e-8777-0990cbe044a1 | -2.7831 | -43.32 | 2024-11-23 14:10:00 | GOES-16 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 159.5 |
| c9266c66-df61-326f-a460-72e583d56bfc | -1.7892 | -53.6091 | 2024-11-23 14:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 45bc0474-a471-35b7-b064-5191558306ae | -3.8776 | -47.5461 | 2024-11-23 14:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 3b545e69-2b7e-3a94-a686-5d79afe4fc97 | -5.0996 | -43.1744 | 2024-11-23 14:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 3f30cd75-9463-3154-9371-beb3cccff638 | -5.3295 | -44.7956 | 2024-11-23 14:10:00 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| c745212b-4548-303d-abd9-f982e7031212 | -0.3402 | -51.5421 | 2024-11-23 14:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 70.2 |
| c0d7dd46-6e32-3120-be23-8d82bf3937c9 | -5.0998 | -43.151 | 2024-11-23 14:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 225.0 |
| a983db1b-ddad-3f93-a42f-5e1dabac4faf | -1.6245 | -53.3084 | 2024-11-23 14:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 5df73c14-6aec-3530-9500-8344f3a98bc8 | -3.685 | -42.1771 | 2024-11-23 14:10:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 220.3 |
| d9584e5c-50e3-33f9-8267-6ee6fc7bb435 | -7.3727 | -39.986 | 2024-11-23 14:10:00 | GOES-16 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 236.9 |
| cf68bd8d-e2d3-3f0c-a566-b6c7fbb7e279 | -2.9619 | -44.9639 | 2024-11-23 14:10:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 96.8 |
| ce78a03b-1bb0-3bd1-93ba-f28179c43175 | -0.2667 | -51.5629 | 2024-11-23 14:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 69563e93-f1e9-3d58-8eb5-89149da55e5c | -4.0737 | -48.9622 | 2024-11-23 14:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| ac9f4d4d-1c48-3c03-81d8-88eaf06d824a | -3.1112 | -49.0197 | 2024-11-23 14:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 1f1e3acb-41b6-31bb-9ddc-0c0d6e77751d | -1.2041 | -51.9478 | 2024-11-23 14:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 75e034b6-d90a-3460-a588-0c2f25b8d105 | -7.3723 | -40.0109 | 2024-11-23 14:10:00 | GOES-16 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 94.5 |
| 52d4d18c-6554-3c05-91c4-6c5bf223ae68 | -2.962 | -44.9412 | 2024-11-23 14:10:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 1f09eeb4-1572-36a7-b8d9-cafd7e5cf56f | -4.0682 | -50.0029 | 2024-11-23 14:10:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| a6ec9575-88e6-34be-b170-ee85670c8897 | -4.6775 | -44.6089 | 2024-11-23 14:10:00 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 248bcc1d-900d-3d7b-9446-c5d229d5f60c | -0.3402 | -51.5627 | 2024-11-23 14:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 7cacad68-93a4-38fc-9bb2-e673a88f5bc9 | -3.5144 | -42.5873 | 2024-11-23 14:10:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 156.7 |
| edc4b36c-e959-3389-bb96-70c15c35cc62 | -1.1103 | -53.3953 | 2024-11-23 14:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 94f8e31d-f81d-31ac-911a-638d61094626 | -2.1789 | -45.6858 | 2024-11-23 14:10:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 3850f44c-7e32-393a-8cfb-2fe30ec30890 | -3.477 | -49.9197 | 2024-11-23 14:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| a9a75314-800f-3e84-91e7-291a2e1b8fef | -0.3218 | -51.5421 | 2024-11-23 14:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 104.2 |
| f5136c10-771e-3f51-8cdc-31e67007c24e | -3.5331 | -42.5864 | 2024-11-23 14:10:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| f18df84b-edc9-33aa-9866-e46d1aa62b87 | -1.9672 | -48.3865 | 2024-11-23 14:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 195ca0e9-bafe-3a6e-af09-13d8e953c45d | -2.4004 | -46.0365 | 2024-11-23 14:10:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 225c1b67-2b08-3b44-893c-6f8873a25071 | -2.5011 | -49.0375 | 2024-11-23 14:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| bc6cd372-876f-3741-9b42-3a57d378600a | -7.654 | -37.4046 | 2024-11-23 14:10:00 | GOES-16 | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 122.5 |
| 26422eed-24e6-388c-9687-4011fff093bc | -4.2606 | -48.6755 | 2024-11-23 14:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 8c74ced9-c6ac-353b-91e0-6520d74cd003 | -1.5493 | -54.3357 | 2024-11-23 14:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 65291fa1-f20e-3a8b-a76c-4979d602518f | -5.1183 | -43.1731 | 2024-11-23 14:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| ce930119-840b-3bef-aea8-69ae6c1348bc | -3.7263 | -44.6822 | 2024-11-23 14:10:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| b9a35ba9-2576-331a-b09d-aede8aeb8908 | -2.783 | -43.3433 | 2024-11-23 14:10:00 | GOES-16 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 295.0 |
| 4ed2b9f5-eb2b-34d9-8e93-57f33f2d1c64 | -2.7798 | -48.645 | 2024-11-23 14:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| d3e1f991-4d08-35af-a2da-b0dd61380016 | -3.7037 | -42.1761 | 2024-11-23 14:20:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| d88b8459-ca7f-3335-b10b-c30c4dfaf6e4 | -1.4408 | -53.3715 | 2024-11-23 14:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 9f8cf45b-e276-3acf-8c11-7378aef52f79 | -3.477 | -49.9197 | 2024-11-23 14:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 4c6918e4-feab-3bbf-810a-3c3c2dbe4d18 | -0.9462 | -52.4214 | 2024-11-23 14:20:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 73.3 |
| eab4109a-9be4-39e1-85fb-c3343452d89b | -3.685 | -42.1771 | 2024-11-23 14:20:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 245.6 |
| 17d9621d-963a-370f-aa5f-0c7f04b098de | -3.5331 | -42.5864 | 2024-11-23 14:20:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| fccc266e-4bf9-3993-a517-d249db2d82bd | -1.7892 | -53.6091 | 2024-11-23 14:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 0660da38-6055-3df9-82d8-5c1ed4685334 | -1.6245 | -53.3084 | 2024-11-23 14:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| f9686138-f4e3-3305-9a97-cab7cf16f41e | -4.0682 | -50.0029 | 2024-11-23 14:20:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 2121b563-5ba0-3f3d-89c2-0ea1c15d786a | -2.962 | -44.9412 | 2024-11-23 14:20:00 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 5a7512be-afe6-3227-b882-007508a5fec1 | -1.4408 | -53.3917 | 2024-11-23 14:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| a3cd35c5-3d9e-3137-8ce9-a3e976dfa508 | -0.3218 | -51.5421 | 2024-11-23 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 0a1a70ef-57f3-30f8-9812-37db02bc6730 | -2.4197 | -45.8355 | 2024-11-23 14:20:00 | GOES-16 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| ae5a3d84-b673-363b-bd0e-179ff2f2deaa | -3.8776 | -47.5461 | 2024-11-23 14:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e6fb67a8-515a-3781-afcf-4bd6838c5deb | -1.5352 | -51.9436 | 2024-11-23 14:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |


[Clique aqui para ver as próximas entradas](README73.md)
