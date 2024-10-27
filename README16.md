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
| 44b25496-ef84-3863-9caf-a3a95d37ce35 | -8.1845 | -50.280499 | 2024-10-27 01:08:29 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14c907e9-7c9f-3447-95f8-edfe8541922c | -6.7227 | -44.664902 | 2024-10-27 01:08:31 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 222d0b69-3395-32d1-ba36-f90a5aec8f86 | -6.7276 | -44.684299 | 2024-10-27 01:08:31 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 875adddd-a1f3-33e7-8b1d-e499e16c167d | -6.3673 | -43.986198 | 2024-10-27 01:08:34 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db20629e-c051-3214-ab72-3a0c94998de1 | -6.3728 | -44.008099 | 2024-10-27 01:08:34 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 51a86a04-c629-3a39-a91a-970f99083e77 | -6.9537 | -48.1978 | 2024-10-27 01:08:41 | METOP-C | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| cd286d10-ebb2-3edf-b8fb-9a41f34c336c | -5.4185 | -43.350601 | 2024-10-27 01:08:47 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1941a2d-74bb-34e5-b1ff-4b2d53689af8 | -5.4248 | -43.375702 | 2024-10-27 01:08:47 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 081f1014-699a-353a-b400-d7e6a030bbd4 | -5.6298 | -44.811298 | 2024-10-27 01:08:49 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 90f4101d-7d05-3338-8399-0546ecba913b | -5.6201 | -44.813702 | 2024-10-27 01:08:49 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf682d83-a857-3b38-b8bc-c911615f693e | -5.625 | -44.8335 | 2024-10-27 01:08:49 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 795203ac-1bf5-36bf-ace3-df9e65ad046e | -6.1668 | -47.247398 | 2024-10-27 01:08:50 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa75d840-8bce-3886-829e-7bdc1825553e | -6.17 | -47.260502 | 2024-10-27 01:08:50 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8eb7e6f4-0b79-366a-97c5-b8ea2ecea528 | -4.2825 | -45.506001 | 2024-10-27 01:09:14 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 11f3f55f-6588-3c03-8804-126c050ef0b9 | -4.2728 | -45.508301 | 2024-10-27 01:09:14 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1e4598f7-13a9-38d5-aead-0edbfddc9be5 | -4.2774 | -45.526901 | 2024-10-27 01:09:14 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e25fe5a1-4780-3d86-9d79-0d0cc8aade8b | -3.1263 | -44.963001 | 2024-10-27 01:09:31 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8af51e3c-266f-305d-8d2d-312de87d1d6b | -3.1166 | -44.965302 | 2024-10-27 01:09:31 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5ca33241-07a6-3c8e-aeac-09bed5e528e1 | -3.1218 | -44.9865 | 2024-10-27 01:09:31 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 070aa0e8-2b4c-3570-898a-1528db1fc426 | -3.107 | -44.967602 | 2024-10-27 01:09:31 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6a55dc39-cec4-3620-a477-06043b7f9f70 | -3.1121 | -44.9888 | 2024-10-27 01:09:31 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 950f1132-754c-3934-ade9-8d62cebae965 | -3.0836 | -45.633099 | 2024-10-27 01:09:34 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e35407b-724b-3d02-b596-5729b42ea0f3 | -3.0882 | -45.6521 | 2024-10-27 01:09:34 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d148e02c-5ce7-3f7c-b8f9-0c3c9d91f693 | -3.0739 | -45.635399 | 2024-10-27 01:09:34 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3ee8dd2f-0193-3190-86b7-b711f846fce0 | -2.8646 | -44.980301 | 2024-10-27 01:09:35 | METOP-C | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f919ac7a-3525-3351-95ae-13ea254d598d | -2.8698 | -45.001598 | 2024-10-27 01:09:35 | METOP-C | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 881bcabc-f566-3802-b85d-6493591b9e60 | -2.855 | -44.982601 | 2024-10-27 01:09:35 | METOP-C | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| db0c74cd-8908-3621-bea5-4eac1adb8ad0 | -2.8602 | -45.003899 | 2024-10-27 01:09:35 | METOP-C | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0e13d3db-bd58-3c08-8705-34418512949a | -3.7845 | -49.474602 | 2024-10-27 01:09:37 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f0a8243-b5bc-3513-bf1d-0036127f27ef | -3.7825 | -50.165798 | 2024-10-27 01:09:40 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 263e462c-4f92-3a95-87f2-9903e7494a81 | -3.2631 | -48.793098 | 2024-10-27 01:09:43 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0015bcf9-8a16-35a5-9f55-48fc21de35e3 | -2.4727 | -45.817699 | 2024-10-27 01:09:45 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| be816537-4a9c-3417-a2f4-232472d4d4ad | -2.4773 | -45.836601 | 2024-10-27 01:09:45 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5706aefc-92e5-3904-8e06-992c12c13aaf | -2.4818 | -45.855499 | 2024-10-27 01:09:45 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 63be7eb1-d101-3b1f-bfa5-c7b7ab8c75ca | -2.4631 | -45.82 | 2024-10-27 01:09:45 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ba5a082-f069-3109-9ca6-48f5bf5f51b3 | -2.4676 | -45.838902 | 2024-10-27 01:09:45 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f59db63b-7b60-3b3e-a20c-9b4917d3b9e0 | -2.4721 | -45.8578 | 2024-10-27 01:09:45 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2fe9ffb8-4ae0-335c-a2f5-a75ffacde8b8 | -3.4416 | -50.075199 | 2024-10-27 01:09:45 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 413b22e1-b1d0-3586-8e01-50952fd0dff5 | -3.4439 | -50.084801 | 2024-10-27 01:09:45 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7aa517b1-5f2e-3ff7-b641-ad1db872ae41 | -3.4461 | -50.094299 | 2024-10-27 01:09:45 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ac81cbf-e65c-3729-b90d-41005ba983e8 | -3.7335 | -51.632198 | 2024-10-27 01:09:46 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8aa4c65e-03f3-378f-ac4d-34cb22e32824 | -4.499 | -54.9538 | 2024-10-27 01:09:46 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aa94547-60d2-305b-b9f9-1fdf6576282e | -4.5006 | -54.9608 | 2024-10-27 01:09:46 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcba995e-3487-3383-8e97-887a2dc3d6a7 | -3.4076 | -50.281601 | 2024-10-27 01:09:47 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a629eca6-ab47-349e-bd46-e583ac43d116 | -3.4098 | -50.290798 | 2024-10-27 01:09:47 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b362616-a448-330f-85df-ac9a31063917 | -3.8461 | -52.249901 | 2024-10-27 01:09:47 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8ce656e-c4a8-3b8e-b76e-d4d6bc9b94ca | -4.1641 | -53.6264 | 2024-10-27 01:09:47 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 492f69ef-591b-3ba9-a7d1-40b8b3ac30fb | -3.3363 | -50.109501 | 2024-10-27 01:09:47 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83936cac-f98e-3ed8-bc4d-369a2d919680 | -3.298 | -50.077999 | 2024-10-27 01:09:48 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e089ca49-e946-37e1-8ff7-81fb4221bed4 | -4.4619 | -55.107498 | 2024-10-27 01:09:48 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd7067c2-ec0f-3133-81fe-a50530902bf8 | -3.3216 | -50.2225 | 2024-10-27 01:09:48 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2a340bb-76ba-37c3-8d7d-bac46800c633 | -3.3238 | -50.231899 | 2024-10-27 01:09:48 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eef450df-f2fa-3818-8ac6-be2d5c58498e | -3.314 | -50.2341 | 2024-10-27 01:09:48 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f4c029a-2e3c-3d49-8f8b-2c5c36eb3f94 | -3.5584 | -51.4118 | 2024-10-27 01:09:48 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d416acb-990a-36e8-b819-391554d9cb83 | -3.5603 | -51.419899 | 2024-10-27 01:09:48 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f689d33-33af-33c6-acc5-65bf25d4d279 | -3.215 | -50.207298 | 2024-10-27 01:09:49 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 264de255-4f1f-3fa9-aa86-b22e91a1e79a | -3.2172 | -50.216702 | 2024-10-27 01:09:49 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a317ea7-6fcd-3ace-adf1-f7aed3ce418a | -3.25 | -50.356701 | 2024-10-27 01:09:49 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ba929c0-9d95-3aa1-bce7-1f9d9416e7f9 | -3.3406 | -50.743999 | 2024-10-27 01:09:49 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34c7f976-c182-3fd2-a9c2-3aed36e2dcf5 | -3.3427 | -50.752701 | 2024-10-27 01:09:49 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3beeb7c7-96ee-39d0-8b77-295338fcd424 | -3.3447 | -50.761501 | 2024-10-27 01:09:49 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19b1f2a8-e564-3066-88c0-99c3ae29c79b | -3.2052 | -50.209599 | 2024-10-27 01:09:50 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d9709c6-3086-300f-8fba-23d0fef8f67f | -3.2074 | -50.219002 | 2024-10-27 01:09:50 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 345563a7-c5c9-33ca-ad20-d2318742c8c4 | -3.3308 | -50.746201 | 2024-10-27 01:09:50 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93a6f828-8373-3c03-b43f-42e9eb3f6300 | -3.3329 | -50.754902 | 2024-10-27 01:09:50 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34b3ed4b-ca40-38b8-b3c1-6d6d6c215f51 | -4.3253 | -55.050598 | 2024-10-27 01:09:50 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 786366a5-ff87-3228-96e8-8f4c4d2d47b2 | -4.3269 | -55.057499 | 2024-10-27 01:09:50 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03da6a96-d833-330b-af19-7c256e3a0bc7 | -3.3231 | -50.757198 | 2024-10-27 01:09:50 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d379056b-b514-3cce-a83e-32b4e8bb8141 | -4.119 | -54.283298 | 2024-10-27 01:09:50 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55d7d335-4ef2-3301-bdb1-2432e5b15092 | -4.3021 | -55.0849 | 2024-10-27 01:09:50 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b653977b-ea90-3eb6-bddd-d7f5a33a1d80 | -3.2529 | -50.633499 | 2024-10-27 01:09:50 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14a5a581-887f-3e43-97a8-3e0d7d77e49a | -3.255 | -50.642399 | 2024-10-27 01:09:50 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a760d78b-4a8c-3988-87ca-0eb283cb4a89 | -3.2571 | -50.651299 | 2024-10-27 01:09:50 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff577b44-52d1-37ae-9387-c12bcb6d03ae | -2.7604 | -48.712002 | 2024-10-27 01:09:51 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f8531a9-3396-3cf6-8ba7-49348b9078e4 | -4.2559 | -55.1534 | 2024-10-27 01:09:51 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6cf72eb-b388-3ee8-a8ad-b3f9946c2e55 | -4.4197 | -55.9193 | 2024-10-27 01:09:51 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7891f72-5137-3dca-8415-0c6066f8276d | -3.1218 | -50.337299 | 2024-10-27 01:09:51 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fbc240c-919b-31b9-a187-8a606615698e | -3.124 | -50.3466 | 2024-10-27 01:09:51 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b1e39ec-d3a2-347b-a964-95c176b26ecb | -3.1262 | -50.355801 | 2024-10-27 01:09:51 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4216bdf8-cc8b-3357-9215-97d82c8926b3 | -4.0701 | -54.430302 | 2024-10-27 01:09:51 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f29ab51f-9170-34f9-b6dd-79190b32552c | -4.0716 | -54.437099 | 2024-10-27 01:09:51 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ec2b984-208b-3103-ba56-c440c9a8a705 | -3.1142 | -50.3489 | 2024-10-27 01:09:52 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39ad76d8-9970-3342-becc-27feedb3e897 | -2.8422 | -49.2342 | 2024-10-27 01:09:52 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0d7cd44-7c15-35c3-932e-0bb6b07f73de | -2.8448 | -49.245098 | 2024-10-27 01:09:52 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9b93a19-9661-3601-aa1e-f816c21b6173 | -2.8299 | -49.225498 | 2024-10-27 01:09:52 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a340dd31-33f8-301b-b327-c12095254d63 | -2.8325 | -49.236401 | 2024-10-27 01:09:52 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac391fda-1836-33c8-828e-13c1ed3383bc | -2.835 | -49.247398 | 2024-10-27 01:09:52 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6192ca16-8a5c-3b45-bcc6-efd55f5a86fe | -2.8227 | -49.238701 | 2024-10-27 01:09:52 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a69e269-c238-3524-bee1-0674a305a1b8 | -2.8253 | -49.249599 | 2024-10-27 01:09:52 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 708c486c-f209-3af6-803f-15ea5857e678 | -5.2832 | -60.152699 | 2024-10-27 01:09:53 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad18217e-2e1f-3cf8-8b27-573e75e67792 | -2.4966 | -48.030701 | 2024-10-27 01:09:53 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d611ca0-f541-38f3-bd13-6fe07509a21e | -2.4997 | -48.043999 | 2024-10-27 01:09:53 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4892695c-06ce-3e77-87aa-ab46682ee037 | -2.49 | -48.0462 | 2024-10-27 01:09:53 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b03f30ad-d6a7-3589-a6cb-e1747d7764e5 | -2.3666 | -47.654598 | 2024-10-27 01:09:53 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8124dfad-ed1e-3347-85c9-6ce7d1207cf9 | -2.3699 | -47.6688 | 2024-10-27 01:09:53 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49822dfe-1bdb-3943-900c-7945e1389366 | -2.706 | -49.3116 | 2024-10-27 01:09:54 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ed98158-b7b1-31d8-8ed9-ec4ccd3fcbcf | -2.7086 | -49.322498 | 2024-10-27 01:09:54 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ab14626-8e99-3561-a912-c0f4d8334fcd | -2.9292 | -50.262901 | 2024-10-27 01:09:54 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ee58072-c0f6-3b9b-9e6d-ed7d1477ae24 | -2.9314 | -50.272301 | 2024-10-27 01:09:54 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9d31990-88ea-3333-a545-cf0178a4596b | -2.9336 | -50.2817 | 2024-10-27 01:09:54 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README17.md)
