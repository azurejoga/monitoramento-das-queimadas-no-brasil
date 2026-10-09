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

## Dados Diários - Página 254

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e348e4e5-5a8f-372a-a92a-ac08b23b4e19 | -3.1833 | -60.4032 | 2026-10-09 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| a17895d4-2bbf-305b-a053-5bc2c8cfa34d | -2.0403 | -56.3895 | 2026-10-09 15:40:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 6c5f744c-cd75-357e-afa9-133af90491ab | -1.254 | -55.7496 | 2026-10-09 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 231.2 |
| ae453a6d-3fc8-3063-b704-b0d37d25ef3a | -1.4118 | -48.9318 | 2026-10-09 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| fb4caab7-74c3-3d29-97b8-0a8e3e515f30 | -3.5331 | -59.5194 | 2026-10-09 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 8e9141b4-8131-3791-81e7-e7ce5b0e6db6 | -8.0766 | -45.6112 | 2026-10-09 15:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 542dbbbe-c7cf-3922-a09e-88e019792aee | -8.969 | -45.1313 | 2026-10-09 15:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 0aab85a6-7933-3acf-929e-b5bda83cfe0e | -3.6815 | -58.8639 | 2026-10-09 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 16a21195-322b-3df6-87ca-d276ddf4bbb6 | -3.571 | -59.0777 | 2026-10-09 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| a31183f0-7b45-3fe8-b858-ddbe7c7e1e0b | -3.022 | -59.1462 | 2026-10-09 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 30a18867-5016-3cd9-b699-84953995151a | -3.9729 | -59.3564 | 2026-10-09 15:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 1d6df5f3-30ff-3cbc-b266-b2d15dd5bdb6 | -2.4032 | -57.8848 | 2026-10-09 15:40:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 6290e9c6-159d-3b79-b2d7-71a9f56e1641 | -5.29 | -60.0868 | 2026-10-09 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| a0a7e662-1704-34a8-992b-4b97f03e7d2b | -2.4623 | -56.0879 | 2026-10-09 15:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| bba939be-2044-386d-baaa-0e2a6c3fc461 | -2.4806 | -56.0678 | 2026-10-09 15:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 2d2ac4ac-2ae8-3c5a-a4b5-adc33c412b3c | -3.1697 | -58.6244 | 2026-10-09 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 146.4 |
| eeddb8c8-7fd3-33bb-b85d-2b7b43d2e540 | -3.533 | -59.5577 | 2026-10-09 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| da0908e9-b3ff-35d0-b7f1-c885d68c9c29 | -3.0605 | -58.4145 | 2026-10-09 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d3e033a5-70d4-3c4d-bdf8-78a0c6e66d4f | -3.5909 | -58.5577 | 2026-10-09 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| f0eead60-e953-3f49-9cfc-d22343f260d5 | -13.1636 | -54.3591 | 2026-10-09 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 340.1 |
| 2b2b7994-792f-3e02-9453-0415cdafcbd1 | -2.8433 | -57.4891 | 2026-10-09 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 393baa47-3a2f-3270-a8d7-268ba8ea1aa1 | -3.4214 | -60.2086 | 2026-10-09 15:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| a715e0a9-4f80-34e2-8766-188f8ddcd29e | -10.8909 | -44.8001 | 2026-10-09 15:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 336.8 |
| 86cb52ff-d1a1-3a79-98ff-90188d44d0d6 | -3.8082 | -59.3219 | 2026-10-09 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c6638656-decb-3e48-b10b-0df2f02e0d26 | -3.4095 | -58.0013 | 2026-10-09 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| c7b89fce-24e4-35cf-86e9-6ac5a8427e57 | -1.3277 | -55.4327 | 2026-10-09 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| ba701e5a-a392-312d-96f4-c79732ac99be | -3.0769 | -59.126 | 2026-10-09 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 501ef61e-5263-3628-bd3e-c827fce4c309 | -3.1697 | -58.6437 | 2026-10-09 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 955241e1-8fe3-30af-b61c-ce3a1d613189 | -3.4397 | -60.2083 | 2026-10-09 15:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 137.9 |
| b5dee630-1d00-38c9-a9ed-c624efcc6aef | -1.1094 | -54.1601 | 2026-10-09 15:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 0e6cd8bd-bc5b-3f35-99a8-0bc84386a892 | -2.4428 | -56.5399 | 2026-10-09 15:40:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| d2523b95-4f58-3c35-b74d-9c2d5ad0541d | -3.5862 | -54.6541 | 2026-10-09 15:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 47da90e1-845d-3060-8f4a-7febf5a8f6a0 | -3.4578 | -60.265 | 2026-10-09 15:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 6869fe0d-92b4-38d5-aa1b-b0d5bf4a2e37 | -2.4259 | -55.9901 | 2026-10-09 15:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 8d85930b-79b7-3430-8565-ccbe23a9d057 | -3.9912 | -59.3368 | 2026-10-09 15:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 772fa530-269c-394d-bd55-cbdd920c853c | -1.4753 | -54.756 | 2026-10-09 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 6c3fcea8-2f54-3272-95a2-a5ca438c0012 | -2.8434 | -57.4696 | 2026-10-09 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 0e9a5459-5d30-3c8e-bc9d-2bef06ab2cb5 | -2.9327 | -58.3204 | 2026-10-09 15:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 57be9bfa-2c5e-3772-8ffc-3ffafb2d7af6 | -3.5893 | -59.0773 | 2026-10-09 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 458a10c0-5e60-3410-9424-bc7fa83dcac5 | -2.9704 | -57.8942 | 2026-10-09 15:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 4804e4a1-ea1f-378a-99d5-fbf5f7659f45 | -3.0219 | -59.1653 | 2026-10-09 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 733548bf-dae0-3351-94de-9f5fb0df1459 | -5.2167 | -60.0507 | 2026-10-09 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 92a8ca1d-a338-33f1-a8c1-bdcbf4d5bfde | -2.0586 | -56.3892 | 2026-10-09 15:40:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 43a2e5ff-3fa5-38cd-bdde-765ee9f45b9e | -5.1606 | -60.3196 | 2026-10-09 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 69eae99e-c940-358d-8ae8-28d9e09796f6 | -3.4214 | -60.2277 | 2026-10-09 15:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 08d395aa-eafc-3bab-8621-0f5584c5eae2 | -2.2198 | -58.1003 | 2026-10-09 15:40:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0d86797b-fa02-35fb-b1d2-eaee9808cd81 | -11.2661 | -45.1859 | 2026-10-09 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.8 |
| 0834a574-19e0-375f-b402-16a067e497f2 | -2.9703 | -57.9136 | 2026-10-09 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 487c89d9-7d63-36ac-9c13-f9f624b94ef1 | -13.2015 | -54.3757 | 2026-10-09 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 5c62df9a-e6fa-388d-870f-d6be51de097e | -3.7347 | -59.4194 | 2026-10-09 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| e093232d-42c2-3f16-9671-87e60328991e | -12.2316 | -44.7427 | 2026-10-09 15:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 4634e7f0-64b8-374c-a265-0413db4dd322 | -3.6049 | -54.5736 | 2026-10-09 15:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 0b1f4528-a7db-3d76-b550-196bd8089c53 | -2.1361 | -54.4671 | 2026-10-09 15:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 0ce088d8-62f0-3034-b83d-ca4f47b1bb77 | -3.7346 | -59.4385 | 2026-10-09 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 50bba5bf-ae02-3e0a-b90e-e7181c3fdabc | -7.4097 | -44.7427 | 2026-10-09 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| de6a31f4-b247-3189-85a9-9339a4ee2f16 | -1.346 | -55.4523 | 2026-10-09 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| caecdb72-73cd-3e2e-90f5-702b74938ac9 | -3.8937 | -55.8969 | 2026-10-09 15:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 87d46333-a045-3efd-a4f8-5c96864ad59c | -8.911 | -45.229 | 2026-10-09 15:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 173cd389-f81b-3a6e-898d-b875d0401c10 | 0.4465 | -60.5442 | 2026-10-09 15:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 35e0aebc-937e-3041-86e2-73263654fb34 | -1.3276 | -55.4723 | 2026-10-09 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 6aaf2299-714d-3467-9982-2ed2362a5d81 | -3.0403 | -59.1458 | 2026-10-09 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| ef81fa28-6932-3fa6-88d8-917197af2b85 | -12.1948 | -44.6554 | 2026-10-09 15:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 182.7 |
| ff851acc-ae17-3dd3-8311-6a308f87b239 | -3.1175 | -57.6585 | 2026-10-09 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 1a034219-88f5-3630-b188-9e17795e6a92 | -3.9729 | -59.3564 | 2026-10-09 15:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| a0a52a0f-e936-3f73-bcf6-610dc6c633e6 | -3.5893 | -59.0773 | 2026-10-09 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 79bc671c-75e7-3e6c-9b17-7d5db7b7eaef | -3.188 | -58.6241 | 2026-10-09 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| dccbe573-eb5f-30f6-afda-8f4bad9290f1 | -13.1636 | -54.3591 | 2026-10-09 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 436.5 |
| 0f72ba91-afdf-3680-af18-a7a62d60efb0 | -3.6435 | -59.3064 | 2026-10-09 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 22eee788-d7f2-3b58-b38b-0f011bb499e8 | -2.9327 | -58.3204 | 2026-10-09 15:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b1a4bd79-ee78-3cd0-86fc-d75ba2f13316 | -3.1541 | -57.6772 | 2026-10-09 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| c7349afb-3eed-3ccd-9002-b95b8261ad44 | -2.9703 | -57.9136 | 2026-10-09 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a7023273-419f-38bf-9c07-82f67953bc50 | -2.4623 | -56.0879 | 2026-10-09 15:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 28868894-5a35-3ad4-9263-a203553539a5 | -12.2127 | -44.7224 | 2026-10-09 15:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 564.1 |
| b508fe61-84e1-39db-9fe9-3c1c1f4fa5d5 | -3.9912 | -59.356 | 2026-10-09 15:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 59d87739-7f5d-3737-b67b-ed954c7c6e96 | -3.5709 | -59.0969 | 2026-10-09 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 257d0c7c-6d56-3331-bfbc-c79a496a80eb | -2.8433 | -57.4891 | 2026-10-09 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 6a80d858-97d5-3098-bf2b-7aa9aad0dbc9 | -9.0829 | -45.0957 | 2026-10-09 15:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 8a2bbc45-1347-3c06-b737-b54f1ffdd28f | -2.5492 | -58.0373 | 2026-10-09 15:50:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 43daba36-9a5c-3d8a-b255-740984e678fb | -2.8434 | -57.4696 | 2026-10-09 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| a747139e-9f42-32e7-ab5f-75b888fb8ad0 | -10.8401 | -50.6712 | 2026-10-09 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 1186d897-faa5-3a06-921f-ee15c720890d | -1.254 | -55.7496 | 2026-10-09 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 164.8 |
| 9a5de416-b75d-373c-95d3-f8cbb6e7bf3c | 0.4465 | -60.5252 | 2026-10-09 15:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| fc40d330-cd12-3f22-a225-bb46bcb275a0 | -3.7529 | -59.4573 | 2026-10-09 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 1d5c5ede-97df-311e-b0bc-f9932ec9a26a | -1.383 | -55.1944 | 2026-10-09 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 9aa2e8cd-4435-387e-980b-2ec302c903d7 | -2.4949 | -57.7864 | 2026-10-09 15:50:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 6fa49d45-55ab-35d9-ab8e-24e1d8fac617 | -12.2316 | -44.7427 | 2026-10-09 15:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 270.7 |
| f4ee8cb6-6f87-31c9-84c2-d4967a18d61f | -12.232 | -44.7194 | 2026-10-09 15:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 531a36c5-8f26-3d1b-8aff-b1bbd922fb70 | -3.6815 | -58.8639 | 2026-10-09 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 11bd3563-47c0-3b75-a734-8c6c43f5a9ef | -1.3277 | -55.4525 | 2026-10-09 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 258.3 |
| b232e155-79ad-3932-99bd-41ca860150df | -3.0219 | -59.1653 | 2026-10-09 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 06d9b257-63c2-3243-a62d-5a6c06f881cc | -6.0423 | -42.5859 | 2026-10-09 15:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 150.2 |
| 4d5ccaf2-1540-3360-9055-11b072f713bc | -3.571 | -59.0777 | 2026-10-09 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 8078e689-f752-31df-8752-ddcae59feb10 | -1.4118 | -48.9318 | 2026-10-09 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| cb04e050-2cda-3930-a554-fbbf1e968b26 | -3.1697 | -58.6244 | 2026-10-09 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 59e1eb8b-c04c-3fda-8275-9dce907edb6a | -1.4753 | -54.756 | 2026-10-09 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 0cdeb163-d341-32ee-bd4e-2936bb7370b4 | -2.9704 | -57.8942 | 2026-10-09 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 54f9ef15-0720-3974-afe3-01f188417e40 | -1.4569 | -54.7562 | 2026-10-09 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 3c81e0c3-732f-3074-926c-98fbb0e14c33 | -10.8588 | -50.6906 | 2026-10-09 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 2e26d6cc-8a0e-3e5a-97bd-567c584c4027 | -2.4623 | -56.0682 | 2026-10-09 15:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| c2410879-7f37-3a8e-9d45-878f8a871783 | -2.572 | -56.1646 | 2026-10-09 15:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |


[Clique aqui para ver as próximas entradas](README255.md)
