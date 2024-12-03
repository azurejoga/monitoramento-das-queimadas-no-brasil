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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96dd0e41-da4a-3e15-87f9-6dbdd944bc41 | -11.4355 | -55.9098 | 2024-12-03 03:30:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| ce36dad6-cf01-38d9-92b9-ac874ba8336d | -3.0944 | -53.3804 | 2024-12-03 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 09551da1-ff0c-3373-b8c8-0c68ffdf6997 | -2.8197 | -53.0425 | 2024-12-03 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 025732a3-4b77-3d9d-8137-5532f8bb3a85 | -3.2589 | -53.6792 | 2024-12-03 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 64fa6318-d17e-3904-bc85-e8e963bca219 | -2.8196 | -53.0629 | 2024-12-03 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| d0b869ca-2427-307b-aeee-5ab70aa37dc9 | -3.259 | -53.659 | 2024-12-03 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| e8a9a98d-5d78-3467-b9fa-1d5047878c16 | -1.0736 | -53.436 | 2024-12-03 03:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 8509b256-2196-36d6-beb7-e159bfa60273 | -2.8012 | -53.0633 | 2024-12-03 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 76c9b7df-ac62-396c-81e5-0777a19eac75 | -3.2775 | -53.6181 | 2024-12-03 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 10b1da30-e09f-37fb-b554-193f6acab40f | -5.801 | -46.4719 | 2024-12-03 03:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 217.6 |
| df3a8c0c-48a0-3989-b083-e87c8f193ee4 | -1.0735 | -53.4562 | 2024-12-03 03:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 157.6 |
| bb30247f-0328-3586-8732-080bb369a2ed | -3.2591 | -53.6186 | 2024-12-03 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| f370e910-993c-3fae-bbe8-507d7b746380 | 2.7267 | -60.3916 | 2024-12-03 03:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 26f79f77-3682-3b7b-ac86-370d0ad49b4f | -2.8196 | -53.0629 | 2024-12-03 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ccbf164f-26de-3f3c-af5d-42bbd6e203fa | -2.8012 | -53.0633 | 2024-12-03 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 81b4483a-1dab-3fa8-a781-c95f6ab547b6 | -1.0736 | -53.436 | 2024-12-03 03:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| c4a1bced-8c1d-3954-9f98-a3329fa71f76 | -3.076 | -53.3808 | 2024-12-03 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 142.2 |
| d770a10f-102f-340b-86aa-c3c2f79503c5 | -5.7824 | -46.4732 | 2024-12-03 03:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 1f6e812a-fc58-3464-86b3-3ee848eca555 | -1.0919 | -53.4359 | 2024-12-03 03:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| f620ac5e-9b4f-332e-8d8b-d7e041b17875 | -3.183 | -54.3448 | 2024-12-03 03:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d729a873-10c4-3140-aa04-999dff8e42ad | -3.0944 | -53.3804 | 2024-12-03 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 94646a02-6e1d-364e-ad82-c702811b768b | -5.801 | -46.4719 | 2024-12-03 03:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 191.3 |
| 7791f8e3-b086-33aa-b7a2-1c4fb26ae727 | -2.8013 | -53.043 | 2024-12-03 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 91c26d0f-8ebd-3693-9178-4288323c693a | -5.8195 | -46.4929 | 2024-12-03 03:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 729a688e-774a-3e86-99c2-538367a0f335 | -1.0735 | -53.4562 | 2024-12-03 03:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 4ca29a14-9430-30ae-844f-deed207f6296 | -5.118 | -43.2198 | 2024-12-03 03:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 9e7c7a70-7775-3a70-9136-04ac00e70dbe | -5.1181 | -43.1964 | 2024-12-03 03:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 96a600d8-1716-3334-a2ce-cdf31279ddfd | -1.0919 | -53.4561 | 2024-12-03 03:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 52b7718f-faf0-3d14-b31c-3514422f61d4 | -4.1914 | -51.1914 | 2024-12-03 03:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 9b191e7c-baa9-3d63-96bd-53c4964d2981 | -2.8197 | -53.0425 | 2024-12-03 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 75ceb3aa-76ec-3659-90e1-78a3948338d4 | -5.8197 | -46.4706 | 2024-12-03 03:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 157.3 |
| b8394054-652c-35f7-a710-b7b50bc50ff5 | -5.8009 | -46.4941 | 2024-12-03 03:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| eedb0a2c-f833-3874-9ce4-cc7cb15d2b58 | -3.347 | -46.0486 | 2024-12-03 03:40:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 80.8 |
| c3f76741-e7ac-30f8-a9aa-15b742b59056 | -2.84868 | -45.39709 | 2024-12-03 03:42:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| fbba1256-03df-3c15-97fa-38ecf7d41c4e | -2.95816 | -39.96297 | 2024-12-03 03:42:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 50c995c0-9ef3-39e0-98c6-521c0b6d9ec5 | -2.72462 | -45.20747 | 2024-12-03 03:42:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| fafb8b31-6843-31d5-9cab-d103d6fc928c | -1.03499 | -46.83527 | 2024-12-03 03:42:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e398706a-8514-3768-8420-bd9eb74aaffb | -1.80259 | -46.66128 | 2024-12-03 03:42:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d7a94a39-9525-3123-87a2-b92767c74cec | -2.66095 | -44.98384 | 2024-12-03 03:42:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8362ae0-6668-3e2f-96b2-cdc9d8e7dcfd | -2.7305 | -45.20839 | 2024-12-03 03:42:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d691283f-037e-3dda-b640-f2e571cd563e | -2.66162 | -44.97972 | 2024-12-03 03:42:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 771f96b3-f9f5-3580-aefc-d7d8afb4c449 | -2.67004 | -46.61992 | 2024-12-03 03:42:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fee10eef-baea-3b4d-ba9c-4bc216cc6ab2 | -2.72588 | -45.20868 | 2024-12-03 03:42:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d8582ba9-70f1-3bfc-8d80-33e44fd58082 | -2.29324 | -46.36837 | 2024-12-03 03:42:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b4bf8f3-aa58-3021-a8dc-29a4ea6902d5 | -2.12476 | -45.34635 | 2024-12-03 03:42:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 167494f2-f61a-3b6a-87b7-1f7a8f990671 | -2.84941 | -45.39276 | 2024-12-03 03:42:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 03552a40-8885-3b08-ad95-9d88c80f5da9 | -1.94017 | -45.55377 | 2024-12-03 03:42:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0940956e-7429-32e5-9013-eaed9093f368 | -2.66106 | -44.98476 | 2024-12-03 03:42:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f22efacb-efdc-3976-aaed-f8312c0f0109 | -1.8035 | -46.65576 | 2024-12-03 03:42:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4518793e-0967-3be7-a6d8-4343f46eabdc | -3.50165 | -39.31731 | 2024-12-03 03:42:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 047a9ebf-8dbc-30d7-976f-63dfbd9b3f67 | -3.10226 | -40.08362 | 2024-12-03 03:42:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cb4aaeac-544d-3175-ad47-0f1753916a47 | -2.85535 | -45.39368 | 2024-12-03 03:42:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 23036279-53d4-372a-875d-0516ce294646 | -2.35539 | -45.70901 | 2024-12-03 03:42:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 426820c8-4ae4-35d3-9c5d-ed83cced87aa | -2.67648 | -46.62086 | 2024-12-03 03:42:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8aa90544-43ca-3eb9-a22d-58f5fcca7bb5 | -2.21153 | -45.73996 | 2024-12-03 03:42:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4ef7a6ca-5bda-3749-9503-65cf63fd1fad | -2.2123 | -45.73572 | 2024-12-03 03:42:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6482af8d-d947-3c5c-ad40-067b0a04e1c9 | -1.79606 | -46.66028 | 2024-12-03 03:42:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 32c5c8bd-e23f-36c8-a837-f0b6dfd9b54f | -2.88311 | -45.44725 | 2024-12-03 03:42:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e343e91a-3cbb-3c0c-93b8-2483336c7b14 | -2.73177 | -45.2096 | 2024-12-03 03:42:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 1addd002-dfd7-3685-a9e1-e5433487fb1e | -2.21228 | -45.73535 | 2024-12-03 03:42:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ba906b93-d5df-3e96-bf65-3eff7b13a943 | -1.94673 | -45.81964 | 2024-12-03 03:42:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f503b38a-bc90-3b8e-ade9-12da7a6d8928 | -2.72979 | -45.21255 | 2024-12-03 03:42:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7fb5caf5-7ce8-3a40-bbc6-276aadd65377 | -2.85013 | -45.38844 | 2024-12-03 03:42:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cf2e18db-a5ea-3786-ac5c-c42b611278a1 | -2.2905 | -46.37105 | 2024-12-03 03:42:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 690f557f-6581-3f09-b158-515e05f85312 | -2.66176 | -44.98062 | 2024-12-03 03:42:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfcf643f-9f48-3bcf-91f7-15945890d5ba | -3.08637 | -40.05066 | 2024-12-03 03:42:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d906eef3-5432-31b1-bb7e-af1e30e56c19 | -3.16567 | -40.1788 | 2024-12-03 03:42:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4f4ded1c-58ad-35a2-89a0-9889b4173230 | -2.29237 | -46.37347 | 2024-12-03 03:42:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5726cf7-8a3e-3337-b7a3-14336ea1101a | -1.79697 | -46.65474 | 2024-12-03 03:42:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4c6a65bc-a164-37a7-9124-d3c2e24d7024 | -1.94751 | -45.81487 | 2024-12-03 03:42:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d580159-1bab-3b46-95fc-00718b6e664a | -2.85607 | -45.38936 | 2024-12-03 03:42:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7d07e73d-15de-3fe2-a6de-5335abf44973 | -2.88383 | -45.44285 | 2024-12-03 03:42:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8280c813-d577-34d5-83c5-68ab8d2cf6e9 | -5.80853 | -46.47369 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| f29a599f-47a0-321c-a350-ff7c2b2eed03 | -9.16261 | -43.11838 | 2024-12-03 03:44:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| af2c159f-24d7-375a-8a2a-30aca53f52e0 | -3.46824 | -42.00436 | 2024-12-03 03:44:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d3b8ef72-30ff-34bc-b697-1aea993c7e1a | -6.98637 | -43.51633 | 2024-12-03 03:44:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 5548007b-2417-364f-9089-9cee6dd2e3f7 | -5.22186 | -44.92093 | 2024-12-03 03:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5767181-149e-322c-8c3c-473cc8edec24 | -4.80715 | -44.99686 | 2024-12-03 03:44:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a8a911a-7ed4-3e84-b68d-40de2bd00910 | -3.34885 | -44.367 | 2024-12-03 03:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d23154b-f1c3-3688-a52b-e658ed30351b | -5.80334 | -46.502 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 259bc4be-99e6-3a3e-9879-643d9a87020e | -3.61352 | -42.74121 | 2024-12-03 03:44:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09ea8344-db6f-3fcb-abea-c38bbb4c4ffd | -4.94645 | -43.78 | 2024-12-03 03:44:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0cc1b1d-5ef6-3922-954b-af110b690093 | -5.80275 | -46.49946 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24b18a34-a5c9-3e33-8124-c041e5840b48 | -5.80417 | -46.49747 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9120ef5-d752-3278-b77e-b83849aeb3f7 | -7.80433 | -38.73393 | 2024-12-03 03:44:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 11.1 |
| e77dcb18-5663-30a5-8355-2df6e56c8dcf | -6.03589 | -44.03624 | 2024-12-03 03:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1213271e-4e1d-38c4-9e63-64b33b0ad8fc | -9.44352 | -43.21082 | 2024-12-03 03:44:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8535052e-4fef-30f5-87ab-b6a1fb733d53 | -5.82068 | -46.47565 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3fe61ae-aa34-3678-a7f3-133af954081f | -5.99828 | -45.41534 | 2024-12-03 03:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edcf6adc-4c2f-3d04-9581-301d6439b369 | -4.80475 | -44.99965 | 2024-12-03 03:44:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9647badd-7945-3441-8395-d2a458a7f8b0 | -5.11344 | -43.21743 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 8dc40aba-00d5-3cfd-956a-f9f38316f936 | -3.34425 | -46.04977 | 2024-12-03 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| d99a5e55-06c4-35bb-b934-fa03cfc53289 | -2.67777 | -46.6205 | 2024-12-03 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd262b33-e680-31e4-a25e-6cda28a38230 | -5.14312 | -43.22975 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1d660111-4f1a-3d61-9193-9191eff7ab98 | -5.57344 | -44.88762 | 2024-12-03 03:44:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2c54c1b0-154d-3eaa-9d58-8a66fcac6ad3 | -4.54902 | -42.93581 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 58096c2c-5f34-3d4f-b427-b6f336e6b476 | -5.80694 | -46.47565 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| dadd5e9f-470b-3e8c-abc8-7224bb4a8743 | -6.1255 | -43.95868 | 2024-12-03 03:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1130bf2d-026f-393b-9a1e-2cb058416940 | -3.34193 | -46.06321 | 2024-12-03 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 0d95f206-b324-316e-8010-47941cefa68d | -6.99421 | -43.52898 | 2024-12-03 03:44:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |


[Clique aqui para ver as próximas entradas](README21.md)
