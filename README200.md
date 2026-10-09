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

## Dados Diários - Página 200

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c4c64f2-c7fa-30d0-bc70-b0cb07733e5d | -5.10326 | -46.22957 | 2026-10-09 05:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de16a33a-1a1a-3ee8-9195-cdcc4e12b1c7 | -3.48988 | -59.38536 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f657635a-0732-3639-a92a-036660f7bb34 | -3.31065 | -53.86746 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9051791-2698-34aa-95cb-9e59e3be5ed7 | -3.54093 | -59.45086 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f624ca4-12bb-3be3-b3ec-4fb13c7b35d4 | -10.73213 | -52.03314 | 2026-10-09 05:23:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a926ffef-f02d-3b10-a16d-13cdf4c0ca7f | -2.9985 | -54.06723 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 558ee42e-b8c8-33b3-b718-57c28d72e20a | -3.72143 | -59.4043 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e31b0a73-69ac-377e-86ed-5e6d7e13f5f2 | -2.99552 | -54.08625 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 028307d4-2668-343c-9336-f5a931976a25 | -3.09945 | -54.28458 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1db106f2-f794-3acf-ac33-84c215cda3c2 | -1.12609 | -57.28025 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a5236ff-750f-35e7-908b-4f88daaf1d2e | -3.18289 | -60.39865 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea7a061a-a668-3602-8651-ca5ce52941ba | -2.3455 | -57.99141 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23e80381-74b9-39d8-bb6c-feebbdbcfbc1 | -1.61637 | -55.1224 | 2026-10-09 05:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a994b18-580e-3911-96d4-9adcf48ad4d9 | -1.10703 | -54.17352 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 545d8531-d7cf-3072-aa69-a7758aee8796 | -7.22854 | -55.08487 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b7dad532-cefd-37e1-92a4-c7bb7568dcbb | -3.1041 | -53.95744 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ddf402f6-094c-3371-856f-5f6f1beb0f81 | -3.17937 | -58.64766 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd3d27e1-9a72-3b8c-abec-3bb4335fe2b5 | -3.01248 | -54.09109 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bfbb398-d852-38af-8e63-97f1bab43d76 | -4.53603 | -49.6705 | 2026-10-09 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35bec59f-8e81-35c6-8ec9-95e95449cb98 | -2.89351 | -59.20504 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67d1a052-5216-3bf2-82c4-3b7fba3251df | -2.8791 | -54.18639 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6aba169-bb2a-3190-bc82-0b1ef489c3fd | -9.87567 | -50.48795 | 2026-10-09 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84fe7806-721c-33da-ae67-3446bae552ed | -3.82531 | -59.41387 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe5bd0fe-9862-34a1-8999-f69ab178c368 | -4.10078 | -56.34321 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05ad0a2b-b44b-3630-b227-cc3c655ee836 | -4.04047 | -54.23395 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b87273e9-1420-36b1-b071-985501bc0550 | -3.30764 | -59.39999 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01007ac2-b649-3d92-b1cb-da7e8c4acaa2 | -2.77859 | -54.0869 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a9b71c9-69b0-325a-81da-eb6583ac21fc | -1.51367 | -54.5155 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2f2af81-225a-336b-a3fc-d63545d0b821 | 1.15932 | -52.73484 | 2026-10-09 05:23:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73b7e62e-60f1-3b27-9fb3-6edf5cbd8fa1 | -2.52868 | -58.10096 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36a09964-dd60-3f6b-8e64-00cab71d4ec4 | -2.89296 | -59.20853 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b20098ca-f8e8-35be-b588-4ac4e2af0645 | -2.494 | -56.06505 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 217d05eb-f2c6-3a32-87c3-15586850b4c0 | -3.11824 | -53.78858 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b9e34c97-adc9-36c1-a677-0a1dfb693b66 | -6.68732 | -59.9622 | 2026-10-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0cde57d-9acf-3450-98a3-f1569ddcc811 | -3.57697 | -59.07465 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b36f1a8-e2e4-3218-9228-ea52d65b2f01 | -8.54028 | -46.91435 | 2026-10-09 05:23:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 580985d6-7b09-3d66-9a5b-760c8b1b1f1c | -2.73134 | -54.11343 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cabb5fd-80e0-3b9d-9631-8ae8e3ecfc4a | -3.63368 | -60.62549 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea4fe714-0061-36fc-b4cd-45289ba74862 | -3.52267 | -59.35114 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00fa3dc8-55c0-3d92-a3dd-4060fcb7475f | -3.07287 | -59.27298 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 620913d8-05c6-3514-964a-88d1b36d8223 | -4.55652 | -54.98023 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7103886-9dc2-34c9-9743-686668a09bfa | -3.08729 | -54.2664 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| de79d350-d936-3ece-9de8-7ae2c3156272 | -8.32704 | -49.1285 | 2026-10-09 05:23:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 954314bf-7797-3e85-bd6a-eb98aca655ad | -2.99858 | -53.91429 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 5609e81e-b758-3e04-9084-a86466f888b0 | -1.3449 | -55.44381 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7e316c7-8aee-3ac8-9fb5-6b776c671251 | -3.01439 | -54.05229 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 844a1890-94ee-3c10-ac93-da1df07f241e | -3.40554 | -58.9132 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31b374ff-b153-36c4-b16b-47ae82c8933c | -3.10749 | -54.18781 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7091cfa-1a08-3590-a226-0d7c1f923e3e | -3.35529 | -50.41957 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 24c71916-4e2c-371f-bf0b-87c3d8313237 | -3.43477 | -58.04297 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f87a22f-ce35-3109-867b-6054e287480d | -3.99132 | -56.25625 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13641799-8c4f-3694-8597-1650c3c5326d | -2.76105 | -54.09867 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebf7bc3a-abcc-3c06-a475-847f2138ef05 | -2.98639 | -54.76261 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 260b7dcf-1d8c-3970-a811-7c49560f1eec | -2.8567 | -59.11778 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d1280194-4115-32e5-a0cb-0af287539ef2 | -2.99816 | -54.75997 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60483b65-446c-3466-9701-d0de1a689387 | -3.56552 | -54.67438 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b75f938a-4f17-30ea-9c1e-1aa7266431e9 | -3.65704 | -55.47324 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a159e5ec-a53f-3f6c-8868-60fde9ad4f9d | -1.32325 | -55.44453 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 153b1754-ec14-3fd8-a5a0-303afc6f0572 | -3.20305 | -53.86374 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c0aa42f-d20f-3f08-89e2-0b4b582194bb | -3.29216 | -54.03977 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26c3f70d-baf0-34c5-8ee9-ad3f090c1c75 | -3.25582 | -57.04314 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4b2e788-670f-32e5-8c08-f492a626bf18 | -3.30153 | -54.05603 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d006929-3a2b-3df8-bd0f-10a1ac44ea63 | -3.7242 | -54.22736 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c72956e9-bc2a-38dd-8f0e-6fa237bd4dfe | -2.52571 | -57.56003 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 308de5f1-7c85-3869-83e4-f7ec2d1f7501 | -3.10333 | -53.78107 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9dd43596-3861-334c-87b4-ca2d7facc4c6 | -2.95871 | -49.18058 | 2026-10-09 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ad4a6e1-a5da-3843-92c8-3a50fe2b89b0 | -2.87308 | -54.19984 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e52618a9-759e-3b70-80d9-423478019281 | -2.83347 | -59.24277 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1352f6f1-c27e-396b-866c-1cdf8e160c77 | -3.09484 | -53.9659 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 449f264c-3621-3b8f-b10b-5f9f97f60197 | -3.10322 | -53.93748 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 17f2b098-cedc-3c48-a654-4f2ecdf88e12 | -1.15725 | -54.22978 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 7e6a96c7-831b-3bce-b1e6-6e591b1cdefd | -4.39079 | -55.44927 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7839bcb-1759-3dea-a135-01a997cc9224 | -1.55139 | -54.55966 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f20185b-b387-3c25-bb5c-aaaf0d91c644 | -9.25276 | -62.30699 | 2026-10-09 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36e0d39e-a868-3c93-9e68-02811e452430 | -3.08319 | -53.96422 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31b7c9c2-376f-3880-90ed-936369f96d3c | -3.16438 | -50.59538 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7eec8f2-c7df-333e-9d2a-f51b75e56c80 | -2.864 | -54.20795 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8f6fa5f-6f68-3f15-ad96-5fe6d06ddd45 | -1.20217 | -55.68297 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73153fd1-e59a-3a8f-aab0-b4d9934057c7 | -3.09623 | -59.19088 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 952a1b73-0341-380e-9586-99110b6615d9 | -3.20228 | -53.86878 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72b12702-3bfb-3709-951f-5b73aed26f19 | -3.4844 | -59.38095 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab0cfa81-7c20-369f-9854-682afcb8a651 | -3.72481 | -53.69735 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b589641-34a4-3bb1-99e1-df1de587ec16 | -3.91128 | -55.9043 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 475f78a0-517c-3e6b-a685-9ba1670c7025 | -8.17575 | -54.71684 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc810472-9e3f-303f-8498-5ac79ef05894 | -2.5846 | -56.14076 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca0c2b2e-89c0-381b-9721-9bdbb8b87c1d | -3.28573 | -54.00413 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74006b49-b4d7-3557-9f16-36acd3eff7da | -6.5956 | -60.04819 | 2026-10-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af9163d9-4835-37ba-9752-efea8d35e214 | -3.52573 | -54.65929 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 37203da3-409c-3ab8-9333-bda127fb20fe | -2.58055 | -56.14402 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf7f04a0-7a01-3bc8-b5cc-081ba994376f | -3.59902 | -60.58167 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3462ea24-f62e-3dc7-aff9-4dbae981661c | -6.49136 | -62.86106 | 2026-10-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71170b26-c1a6-3a47-940b-b17a835e7e6d | -3.83308 | -59.40794 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87431d30-11d3-3d43-8b93-37f912c87196 | -1.82865 | -55.03632 | 2026-10-09 05:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f00f997-25a5-3b96-923c-9288681f29f3 | -3.17413 | -50.59687 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a8240fb-352f-3567-b517-458e64f4299b | -1.73815 | -52.2469 | 2026-10-09 05:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a0524ab5-b3e6-3162-950a-fac4a616d51c | -3.50291 | -56.9196 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 721da380-fc7b-3833-a5b5-18aae9812279 | -3.09634 | -53.95621 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 035b4d71-24b8-3923-b7f2-87a9ee23a606 | -11.6737 | -46.77784 | 2026-10-09 05:23:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| db5dc3c2-fbf0-3a99-beeb-a14a49469f3e | -3.01473 | -54.08922 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9127ef6a-e4cd-3f55-b2e3-09578cac3d8a | -3.9485 | -56.10865 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README201.md)
