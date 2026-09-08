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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ede60139-4554-31fb-886a-9c78b342835a | -9.08026 | -65.38821 | 2026-09-08 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1eac6d1-6002-30f3-bc74-efa1eb6d9340 | -8.55964 | -63.88134 | 2026-09-08 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a61834e4-5469-3aa1-b5f4-772aa844734d | -9.02312 | -65.44682 | 2026-09-08 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 861b222f-4fe3-3b7b-8da7-e351c0b108cf | -6.79777 | -58.95333 | 2026-09-08 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ff3a56d-68cc-3476-8250-6fb76878f2fa | -7.06765 | -56.4698 | 2026-09-08 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac325281-b997-3043-9f9b-0c919a5d1a94 | -8.53733 | -63.90503 | 2026-09-08 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c512fb8-ee94-3951-ac87-2569b77fb93c | -12.27134 | -63.41937 | 2026-09-08 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 365e2d6b-dd70-3ea9-8695-82ddcf2d7e52 | -11.40566 | -62.12521 | 2026-09-08 05:50:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c22cd9c5-f5e8-3e9a-bfa8-95e665e3a546 | -8.98619 | -65.38645 | 2026-09-08 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8746adfe-73ed-3659-88dd-3e670cf779bb | -13.27044 | -61.70546 | 2026-09-08 05:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 775f1df4-fb25-3daa-a653-fbd64d5ee0d3 | -13.27521 | -61.77741 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63976ef9-4b72-3399-9b9c-7c123d7aafce | -13.26077 | -61.70888 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 807139e0-c115-3520-9f5f-f4bff83882c0 | -13.2217 | -61.71622 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a4e3c1a7-f201-36f8-b67c-62f1fa9db385 | -13.23138 | -61.71281 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c69732c-4d8a-36f6-a8ed-2f5ad53dfcea | -17.09531 | -56.87329 | 2026-09-08 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8e87c292-ca1e-35e2-a219-4f7dfda3b394 | -13.25682 | -61.70354 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1633af02-f8eb-3582-be61-4890ca4694e0 | -13.23652 | -61.70876 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7d72b4b-ea14-32a9-bb84-83473d61f5ac | -13.25111 | -61.7123 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4519e702-796e-32c9-abd8-f6e77f48a936 | -13.22684 | -61.71218 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1ef17b8-8158-3969-86fa-72ed8d079fa1 | -13.25014 | -61.71064 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56cf404e-0794-3002-ae04-abe7f7014ca8 | -13.26531 | -61.70951 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 001598ea-34fb-3c4c-83fe-8e80c8708303 | -13.27463 | -61.78205 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8390f08-3c3f-37a6-92fa-d1631860cea3 | -13.28032 | -61.77339 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fd53f7e6-0d8e-3860-959b-e053785d2156 | -13.27568 | -61.14681 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36d025ab-a517-333a-a542-1cc091d53848 | -13.27503 | -61.15192 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a350fed6-1b3a-3471-9b92-8afc3c9a2c3b | -13.27698 | -61.76347 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 16ca087c-35d2-3e8f-bf25-0036a1864bda | -13.28091 | -61.76874 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ca7564e9-0a7c-3dbf-a69d-01ccb11d6fc8 | -13.26473 | -61.71421 | 2026-09-08 05:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ec10fcc-71d9-31c3-abbf-f12fdc6c1894 | -13.21716 | -61.7156 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 024b6699-07c8-3f2f-b45d-100d149aca66 | -13.27973 | -61.77804 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ba673f2-abd7-3bbe-82f2-7b1dbfe518e8 | -13.27439 | -61.15702 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 982113bd-0410-3d1e-8e58-76b6d74efef1 | -13.26437 | -61.70786 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73f1efcb-cf76-3a18-9f76-6e0525dcde90 | -15.83826 | -56.60979 | 2026-09-08 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 82161b3b-4811-3861-b352-1dca3ede4990 | -13.26374 | -61.71254 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d59bac3f-bf6d-3dae-a252-566363497463 | -13.25529 | -61.70659 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 997b7d7d-5bf9-3fa5-a2e7-54fc98bcba93 | -13.27639 | -61.76812 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 98982d3f-b726-3bde-a7c2-ba09889f0a6e | -13.2815 | -61.7641 | 2026-09-08 05:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f0d2e008-667f-3e38-b050-260e49ad4fdc | -13.27498 | -61.70609 | 2026-09-08 05:53:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36f249f1-7afe-3fc9-aee9-18079a28f940 | -13.25983 | -61.70722 | 2026-09-08 05:53:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0cb8b12e-9c06-3efd-91ec-f5cdc86fd16d | -13.3004 | -45.2442 | 2026-09-08 06:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 94b41aac-f36c-39b6-a757-75c344f4e3d7 | -13.3009 | -45.2209 | 2026-09-08 06:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| eb3072b5-4b21-33c3-8f12-b699e1be3783 | -13.3004 | -45.2442 | 2026-09-08 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 82289957-d5de-3e6e-ab65-0f9ec3aad044 | -13.3009 | -45.2209 | 2026-09-08 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| ff99c371-115a-3956-9f2c-80c99e9dea00 | -13.2815 | -45.2241 | 2026-09-08 06:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| dd326382-0b43-3884-955e-91fc5b4f920a | -13.3009 | -45.2209 | 2026-09-08 06:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 2db83ac7-c511-3412-8dff-fa51e9c2f837 | -13.3004 | -45.2442 | 2026-09-08 06:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| d8063c03-487e-3d2a-a791-170c3ae5867e | -3.69729 | -58.94677 | 2026-09-08 06:22:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 94160f6d-4550-3d72-aa35-fc76f7247074 | -3.45637 | -59.51376 | 2026-09-08 06:22:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 383eb5d6-35e4-3263-8456-2c62f19a1b00 | -3.77432 | -58.85426 | 2026-09-08 06:22:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a9f15e6a-0be4-37e5-8b1a-df0f1603e93a | -3.45692 | -59.50985 | 2026-09-08 06:22:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f64b1dfc-daa6-3d9f-801d-981408265aab | -3.45732 | -59.50737 | 2026-09-08 06:22:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 311fd426-d03e-32f7-a6ac-f84c767bbe4d | 2.46118 | -60.77439 | 2026-09-08 06:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 895a04ed-e33b-344b-aa35-0aaf16dd0a7d | -3.46424 | -59.50834 | 2026-09-08 06:22:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6139b8c2-a713-32fa-be23-aef86b4e6a76 | -3.3779 | -59.43135 | 2026-09-08 06:22:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31e970bf-d8fd-3851-92df-27603535d9de | -3.46384 | -59.51084 | 2026-09-08 06:22:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5699429a-3e78-30af-8d84-58bad60b3bb9 | 2.4604 | -60.77693 | 2026-09-08 06:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fa86a17-38a2-3c85-940b-29e700e30d52 | -3.70084 | -58.93825 | 2026-09-08 06:22:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 732ca146-ad06-3ac2-9aeb-897bea66535f | -3.69983 | -58.94528 | 2026-09-08 06:22:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b2eeedb0-2de9-309e-9f17-e51c403689bb | -3.45602 | -59.51623 | 2026-09-08 06:22:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 171ebf1a-a69d-319f-9472-0120a6172e91 | -8.51013 | -69.79934 | 2026-09-08 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8727a460-2106-3793-8496-e60af697c1d4 | -9.36096 | -66.66838 | 2026-09-08 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 22bd2422-fc38-3d26-bdbb-e101c7423d8d | -6.63694 | -59.43647 | 2026-09-08 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 393cfca3-f38c-3e50-8659-a8170eef4510 | -6.63609 | -59.44309 | 2026-09-08 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f57a77b5-e358-3301-9ea8-463205e93b36 | -5.28637 | -60.11533 | 2026-09-08 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e80bbd57-41b4-3145-b5c6-a1cb93ac3117 | -9.36633 | -66.67057 | 2026-09-08 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f88d75f-f2f0-3da4-a36b-d1c80e5e09c7 | -8.51081 | -69.79471 | 2026-09-08 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9185113-7b62-37ef-9c9b-6f0a2fd4b3b3 | -11.40815 | -62.12901 | 2026-09-08 06:25:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6214574-e0e3-33f2-afd1-d21010dc34d2 | -11.40878 | -62.12373 | 2026-09-08 06:25:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1df5a9cf-2a32-3f95-9695-6549d5706dfd | -9.36568 | -66.669 | 2026-09-08 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f48951fe-958e-3851-a131-66ded1813952 | -5.28549 | -60.12148 | 2026-09-08 06:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 451f992d-3fd2-3d0b-a36a-977a886d4ed1 | -6.63442 | -59.43803 | 2026-09-08 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 10e2f442-7e55-3e87-b901-d7bd6c04c92e | -8.50762 | -69.79694 | 2026-09-08 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b28754c-9607-31f7-8877-491e8ad05dad | -6.64163 | -59.43904 | 2026-09-08 06:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 460009ba-a13e-3fa4-b552-f9860279858e | -8.98575 | -65.41191 | 2026-09-08 06:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7eb0c4e5-28c7-3bcc-b005-4bf76b510990 | -13.28155 | -61.76678 | 2026-09-08 06:27:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8c1834f0-9178-3ba7-b499-f77d6c62901a | -13.25901 | -61.70777 | 2026-09-08 06:27:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88d8d9ab-a29f-34d1-b6b2-5ccc5bf75711 | -13.26012 | -61.70726 | 2026-09-08 06:27:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02ef725f-ce68-3cb8-8437-b2a7bc231f2b | -13.28024 | -61.77922 | 2026-09-08 06:27:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6f183a5-8fb6-3956-9d30-6d3932b68566 | -13.27869 | -61.77954 | 2026-09-08 06:27:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| da48e963-b4f7-34d0-aa96-7b20f17a8e94 | -13.21661 | -61.71557 | 2026-09-08 06:27:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d08da230-5bb2-3f7c-b835-834b69a284c7 | -13.28089 | -61.77299 | 2026-09-08 06:27:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 32fc919c-dac1-3da6-8e2d-fcf9ea1ca47e | -13.22345 | -61.71635 | 2026-09-08 06:27:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb8132fc-f979-322d-8ae5-b2f8362d9244 | -13.28008 | -61.76714 | 2026-09-08 06:27:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f9d03a18-d9d9-3dac-9914-d458a88cbdbf | -13.25217 | -61.70697 | 2026-09-08 06:27:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a58e44a0-2ff5-3d5d-a59e-064b67b591a0 | -13.27939 | -61.77333 | 2026-09-08 06:27:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7f418ecb-1f74-3317-953a-91c7f4ca2047 | -13.25328 | -61.70643 | 2026-09-08 06:27:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b468cb5b-4bf1-36b0-98e7-e02d24dbfa01 | -13.27473 | -61.766 | 2026-09-08 06:27:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3502590d-6c96-36f7-b658-6b60571e0e75 | -13.3004 | -45.2442 | 2026-09-08 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 46caca8a-74f4-3e00-aaba-3a23f4aa3757 | -13.3009 | -45.2209 | 2026-09-08 06:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| d01fe056-9f64-3722-85f0-6a052b03a228 | -13.3004 | -45.2442 | 2026-09-08 06:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 49a40ea6-24c7-389e-844b-e4bccfa145ce | -13.3009 | -45.2209 | 2026-09-08 06:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 31a41a99-cf2d-3b84-aa5f-e67dda7cb098 | -13.3009 | -45.2209 | 2026-09-08 06:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 8a5dc9e3-87dc-3fa4-a489-432a127f0be3 | -11.48909 | -51.11348 | 2026-09-08 06:59:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| c582b804-1c1e-3934-b5fe-a1bc3ad43808 | -4.10491 | -49.06713 | 2026-09-08 06:59:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9fef652f-abc8-3aec-bb34-030f00dbbf96 | -4.03586 | -50.87399 | 2026-09-08 06:59:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0775ab70-d4a3-3d2f-903c-27e3b8ded055 | -3.06646 | -49.51616 | 2026-09-08 06:59:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f5105e7d-acf2-3d27-9a19-388641a61155 | -7.06446 | -56.46572 | 2026-09-08 06:59:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 06e2c93e-ce18-35d6-80b1-b3b7dab6893c | -3.5458 | -48.17083 | 2026-09-08 06:59:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 93df9946-9a05-38b8-9ad7-18e4b9275df1 | -4.04463 | -50.87529 | 2026-09-08 06:59:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7d2d3f2a-c9b1-3f2a-8f27-18324e748b92 | -3.2471 | -50.82645 | 2026-09-08 06:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README26.md)
