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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7490ba1-ee8d-3846-bbd3-10f62b67df00 | -3.481 | -54.627602 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 021b90b9-291f-3654-b5e2-4cc484a34af0 | -1.2912 | -54.5672 | 2026-10-07 01:09:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ce287c5-1a6d-3a01-8f33-07622749edaa | -11.7427 | -43.669399 | 2026-10-07 01:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4c00a495-078d-3d0c-b4a7-3d157a8a138d | -3.0434 | -54.254002 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba8b9374-db97-35a9-9d0d-c041f7048276 | -2.8442 | -54.062698 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fa1a8ca-a744-3e2b-b8c1-c7a23913a3b8 | -5.9587 | -55.3452 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c518ba92-a9a4-3fff-9ede-e9b86bf2a475 | -7.7609 | -49.224499 | 2026-10-07 01:09:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 691c0836-c7b2-33d3-abe4-8f6a42bdf0fc | -4.3772 | -54.754601 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c84e56c-28e5-32d8-a1fe-18515da49711 | -4.9233 | -55.865299 | 2026-10-07 01:09:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dccc787-5a2c-3417-912e-3a1d7177d08b | -3.1018 | -53.752399 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eda3393a-1b16-3691-ada9-a37ecf74cbd6 | -3.7734 | -59.404099 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d66465e-96bf-30ae-bccc-27b302253a1e | -3.5605 | -54.481098 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fbd274f-0bab-3b1e-81f6-09fb24eadbe5 | -2.759 | -57.667198 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9fcd2d53-1725-3380-b566-538e969571d8 | -4.5671 | -54.950298 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4845854-7906-3374-8b70-e56a0fed4eb7 | -8.7084 | -45.172001 | 2026-10-07 01:09:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 777534f3-687e-3521-a666-bb33b4f541fe | -3.5055 | -51.699001 | 2026-10-07 01:09:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff3b30c2-7a65-34eb-837a-ae8be516bf1d | -2.8461 | -54.070801 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3e17e34-746e-3514-bbd1-22590beb3b80 | -3.286 | -54.055801 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 207b44ed-7d0d-3de1-9d7b-80ffb8a1a9bb | -3.5014 | -54.670898 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b5f111f-4d2f-3395-9a9e-a679e2e78104 | -3.2958 | -54.0536 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd022359-bef7-3807-bba6-053c8469251b | -2.9843 | -54.132999 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a309bd0f-ffc7-3af3-8e5c-f0e92016a1da | 2.7545 | -60.016899 | 2026-10-07 01:09:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c3408478-1a7e-32bd-9214-6aa8b3f69497 | -13.4972 | -44.3484 | 2026-10-07 01:09:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3989551d-ce9d-375b-a6a6-c6c3d23435f5 | -3.0918 | -54.284698 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24f07f22-af47-3c7d-afcb-6bb7ebeb00ee | -3.2916 | -54.079899 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 677d3f98-55ea-3c67-a1a8-1bb854f81b1e | -3.9843 | -56.222099 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b9bc4e3-3cb3-319f-aa1b-fd80f86f0921 | -3.4926 | -54.632999 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71ca7de2-18fa-34bc-9f9a-edc99c12780a | -3.9343 | -54.580299 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c9b5f51-2db0-33ac-b53b-117a3b1faa83 | -4.7528 | -55.662998 | 2026-10-07 01:09:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 970857a8-5b6c-368c-9b05-84023bc613c3 | -3.743 | -59.4515 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1be61e5c-2340-3a95-af5e-15b6e5c5c308 | -7.1887 | -52.6185 | 2026-10-07 01:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e50a8f78-d0bb-35b3-b9cb-3bda8edfdaf2 | -3.3031 | -53.863499 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a84fb1a-3ce1-323d-a650-33849824d9bb | -3.6634 | -60.645901 | 2026-10-07 01:09:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1130ad47-c1af-31dd-bcdc-e9041b6819ea | -2.0143 | -56.894901 | 2026-10-07 01:09:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38ad4f58-ae8c-31f9-ac3e-2568f8e88a12 | -14.2468 | -41.640202 | 2026-10-07 01:09:00 | METOP-C | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 122e1a8f-9767-3d68-a0ae-9e97a6935a04 | -3.0935 | -54.158798 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff864500-14ae-32fc-8881-0809673b13c6 | -4.9249 | -55.8722 | 2026-10-07 01:09:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4596735-6b47-376a-a9c0-742b9baefaf6 | -12.1917 | -44.716099 | 2026-10-07 01:09:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f57513af-df98-3bc8-b8b7-27b084378137 | -3.3439 | -59.507198 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b82527f-c149-38f0-a642-fadb10ecac31 | -3.7343 | -55.988201 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0e6c0ee-63f5-39c2-9d3b-d8e5320f929d | -3.4133 | -58.907001 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6f1a075-a7bf-3ebc-a420-6face13db578 | -6.772 | -56.234798 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3aae74df-4887-3424-9500-0d209fea1e2e | 1.7106 | -55.626999 | 2026-10-07 01:09:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e37cd61-d8cf-3407-a222-925a37028309 | -3.3274 | -54.189301 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b22ea760-4615-37ed-8288-68633092ab28 | -3.8129 | -51.042099 | 2026-10-07 01:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f263f6da-c710-3d82-b475-4171199a43e9 | -3.5585 | -59.500401 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43250d17-f20c-3ffb-9df1-87062674d05b | -3.2841 | -54.047798 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f10790ce-147c-3edb-9ca8-24834e956a52 | -3.1783 | -50.450901 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64481103-4891-3129-a73e-629793f43865 | -3.6031 | -54.576 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aeae1c01-ac43-3f53-b580-67481e01a7a1 | -3.57 | -59.506001 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bfb6f239-c188-3ccd-9614-5448c6a4fa35 | -3.0845 | -54.253101 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 394d712d-c9f1-35d9-8b03-d7f0e65bd255 | -3.5029 | -51.688099 | 2026-10-07 01:09:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 511fc007-e662-3b1b-93f4-d8c2f64de76c | -11.7503 | -43.697102 | 2026-10-07 01:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 11ec6f60-5db0-3f9b-bfe3-e3b50ff06041 | -2.9647 | -54.137402 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ff8f1d1-2951-306c-8dc4-8864ed1d9cf9 | -3.0641 | -54.165501 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47694bfd-d870-3ad1-980d-38854ed0e403 | -2.8064 | -52.096401 | 2026-10-07 01:09:00 | METOP-C | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adbda4c4-4bc3-3dd6-8bac-8c0da72e4940 | -3.2726 | -50.414799 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22ce9663-f95b-3c3c-96a3-c03f6f729469 | -11.7868 | -46.5798 | 2026-10-07 01:09:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96fea2b3-51fa-3839-ba40-0689ee5acc3d | -3.284 | -59.5611 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2fc6feef-212c-36e3-b9d9-f4e0807640a2 | -3.0795 | -54.187199 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa3d0621-2011-3b58-bd24-33c8c0ec7fcb | 3.146 | -60.5984 | 2026-10-07 01:09:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e7b49d0e-4a81-3282-bd8f-a06431ae4b75 | -5.9619 | -55.3592 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df178b06-50da-39eb-96af-50b9e02c7c85 | -4.3408 | -55.131199 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59429809-4ccc-363d-a770-8a48cdcc2571 | -3.5094 | -54.661098 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 760527ba-31da-3a9c-9071-c9214476828d | -3.0542 | -53.946201 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dd8bc1c-1e58-323e-9935-788ed80df9fd | -3.2743 | -54.049999 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d1e115c-5a85-3b02-8770-03dd295dcf9d | -3.4818 | -55.431499 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af0311d3-75c8-398f-ac95-b1efd5b99074 | -8.2828 | -50.2575 | 2026-10-07 01:09:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 832c2544-1671-3842-9879-66d09ba4f27e | -3.5255 | -54.641499 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5f65f2e-0eee-30c2-bc24-9a1150f4933c | -3.4862 | -59.589901 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b935d874-df21-3c94-b975-a6d43e7fb6e9 | -3.3887 | -58.211201 | 2026-10-07 01:09:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5fecfea3-dfbc-3990-aa16-84101742b93c | -1.7407 | -57.185398 | 2026-10-07 01:09:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3924d008-ec35-3615-a9d4-7afa3b82e07d | -2.4881 | -58.060299 | 2026-10-07 01:09:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 75c3cc87-7299-3fc0-a49d-8e2d4ab3c31f | -2.9666 | -54.145401 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0be1f8b8-4c14-3640-90bb-63485cfd1e8f | -5.2449 | -50.9147 | 2026-10-07 01:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04730ca7-9869-3593-8e31-9677c65d9bfc | -3.3351 | -59.4687 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ff03c92-3c41-3a26-b04d-ad800a9d3558 | -2.9316 | -54.127998 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c536d5a4-994b-3415-b1a1-01b39573bbfe | -2.9832 | -54.0396 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a785346-d6dc-34e7-93f2-61e5daeb89b6 | -2.877 | -54.115002 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7260bbd5-e72e-349c-a086-c1a3fc9a444f | -3.2879 | -54.0639 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a66762b-7088-3676-a875-7463b224685b | -2.8088 | -54.087898 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4deeb877-673d-3307-8196-afdb8e81b913 | -3.0556 | -54.2178 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3beb4a4-211e-3005-bd4b-c2e6f13865ba | -12.4856 | -51.306198 | 2026-10-07 01:09:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aadb5a2c-b4a2-330a-b650-45b14534f8dd | -3.671 | -60.5429 | 2026-10-07 01:09:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b1e0d1d-111f-3631-bc9d-83a3e9409b2e | -2.7931 | -57.681099 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5918cad4-8f71-3274-bce6-a9c65ef74e82 | -3.1803 | -50.588799 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1367692b-6fc8-3465-a572-cd39a645af90 | -3.5129 | -54.676201 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 070cc7b7-0307-32f1-90bd-2c82fbba6ed7 | -2.848 | -54.078999 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14c6cfa2-5794-3e70-9cfc-982046a75ff8 | -3.0406 | -53.932098 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abeb4c8c-f090-3032-806a-487a82fe83c4 | 1.7089 | -55.634701 | 2026-10-07 01:09:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c742188-5052-311a-99c9-45411e161f09 | 2.011 | -61.089199 | 2026-10-07 01:09:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5135c037-15b9-32fa-a166-9d258dea00ad | -3.1076 | -53.777401 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef063acd-6014-3f75-944b-da87beaa5cd3 | 3.1558 | -60.600601 | 2026-10-07 01:09:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9d04d01d-a9a5-3696-9ed4-e4304ad40a20 | -9.1699 | -45.128799 | 2026-10-07 01:09:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 99a3ed40-f469-3aed-80f8-81a8f64d6120 | -3.1253 | -53.764599 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 186b5bf0-733b-3531-b976-07e35ee580c6 | -5.2421 | -50.903198 | 2026-10-07 01:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4129086-e305-3e3d-93a0-7972c80b215e | 2.4298 | -50.8451 | 2026-10-07 01:09:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0725a0b0-e046-3d29-8052-6e8d2fa20df9 | 2.7102 | -60.029701 | 2026-10-07 01:09:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 85e32265-6046-3a16-866c-4817ca78031d | -3.4966 | -50.104801 | 2026-10-07 01:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7a771ad-b03e-3683-a382-e2cffd25345a | -2.4799 | -56.0952 | 2026-10-07 01:09:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)
