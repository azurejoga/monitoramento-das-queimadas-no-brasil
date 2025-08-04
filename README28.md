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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06b1810e-edd4-3250-a664-0c83072d58de | -7.7804 | -45.2093 | 2025-08-04 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 18e2a3db-7990-3c73-92c3-c57cd666d62a | -7.7801 | -45.232 | 2025-08-04 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b8e32ed3-f04c-3363-bce6-061dfbafbcec | -8.9478 | -46.7354 | 2025-08-04 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 43e922b8-a8b1-3842-8f87-78be8a8684f4 | -8.0324 | -43.1022 | 2025-08-04 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.1 |
| bc36d9f3-317d-3364-9bc3-491e17f23785 | -7.7629 | -45.0972 | 2025-08-04 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| d10d3746-870f-3b5d-b8c7-1984ed2d3819 | -8.9475 | -46.7577 | 2025-08-04 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| ad08366a-f229-36a6-8fa6-faadf2c30ab3 | -7.9934 | -43.2005 | 2025-08-04 13:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 193.9 |
| ac975a4a-8a94-3e16-a962-5b48470fb300 | -8.0324 | -43.1022 | 2025-08-04 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.0 |
| 6fcaa882-f425-33b4-8fb6-dd00bfcd49b8 | -8.0123 | -43.1984 | 2025-08-04 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 193.5 |
| 8644b77a-8736-30f7-b3e4-b13866ffc5c7 | -7.0946 | -44.3589 | 2025-08-04 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| e64ca75e-299d-365e-87e2-66b49dbac931 | -7.5585 | -44.8887 | 2025-08-04 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 722eb7ac-7bf2-39bc-adc7-55149b46f84d | -7.9468 | -43.9061 | 2025-08-04 13:50:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 63.1 |
| b772f0d3-e319-3b82-8a6d-1ef66f06012a | -8.9478 | -46.7354 | 2025-08-04 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 9f129761-5419-3121-be6e-554925fd0f46 | -7.7801 | -45.232 | 2025-08-04 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| c0fdce9d-f3fe-358a-acf4-f3e285214e71 | -8.012 | -43.2219 | 2025-08-04 13:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 355.7 |
| 5b114bfb-8641-31c9-ac5d-38e9d35ee75d | -7.4644 | -46.5875 | 2025-08-04 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| dc1b3698-ac8a-3c3f-8969-9482fecc4260 | -8.9478 | -46.7354 | 2025-08-04 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| c2948cab-01d2-3745-9ff4-899cae692b48 | -8.0123 | -43.1984 | 2025-08-04 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 135.7 |
| 97334612-876c-381e-9a05-c60f211b3292 | -7.7804 | -45.2093 | 2025-08-04 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 5db527eb-91ce-32e1-948c-54cb17bd9746 | -7.0757 | -44.3606 | 2025-08-04 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 4067688f-bba4-3897-a6c1-c8e145179e16 | -8.9475 | -46.7577 | 2025-08-04 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 6d612a05-0608-37d0-9083-1c8101c81cea | -11.5307 | -44.267 | 2025-08-04 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 72564c30-1048-3afd-930b-e61f1812256b | -8.0324 | -43.1022 | 2025-08-04 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.9 |
| eb9981ad-7573-3b57-9f25-99cc8e80e5c5 | -7.9934 | -43.2005 | 2025-08-04 14:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 108.7 |
| 22963c1d-8afa-3b0e-b006-80eaeda9549e | -7.5585 | -44.8887 | 2025-08-04 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 82fe1ac9-b674-3215-afd4-90d4b7151eb9 | -11.5111 | -44.2933 | 2025-08-04 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 8f123360-0e36-356a-9f13-1f30564d47b8 | -7.7801 | -45.232 | 2025-08-04 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 55a5fbe7-fb50-3e37-b790-0def9eea85c3 | -12.7676 | -45.8822 | 2025-08-04 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 2bb53d85-c85b-3530-b371-97fe18ada4dc | -8.012 | -43.2219 | 2025-08-04 14:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 141.5 |
| 726e092d-47a6-3365-b02f-b0c7b4ac0c50 | -8.3852 | -46.5468 | 2025-08-04 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| c09bb6dd-4724-3a84-8b77-b508de05d75b | -7.0946 | -44.3589 | 2025-08-04 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| bd1e5877-1c83-3760-b0ac-6cd8b78a8ff2 | -11.5115 | -44.2699 | 2025-08-04 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 261.6 |
| aa2300f6-30b9-3ff1-84a9-ab529f7d4db6 | -7.7629 | -45.0972 | 2025-08-04 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| b5bf142d-c44c-39f1-8a72-cb32eca6bbda | -8.3852 | -46.5468 | 2025-08-04 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 134dede3-0f1d-3be3-8bd2-acb45af1c928 | -8.3663 | -46.5487 | 2025-08-04 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 0d77aa74-f9e2-3bd0-b75a-e851e6544cbb | -7.7801 | -45.232 | 2025-08-04 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 95a2a47b-4482-3e1d-ae7e-225d7f73959f | -7.7613 | -45.2338 | 2025-08-04 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 4b4a8b74-61fa-38cc-8868-f4cea806fd97 | -11.5111 | -44.2933 | 2025-08-04 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 4bc84429-a0ca-3fcf-ab51-819ec1fda261 | -11.5115 | -44.2699 | 2025-08-04 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 377.4 |
| 2435e468-555b-3d85-8c4f-500f91841d5d | -7.5585 | -44.8887 | 2025-08-04 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 5f22f988-cabb-3f55-a2ba-4f4f9b31fec4 | -7.0757 | -44.3606 | 2025-08-04 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| f8b51f7e-b80a-36f2-9840-e80c4162ffcd | -11.5307 | -44.267 | 2025-08-04 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 1ff27f6e-70f3-36a4-9def-4c53bff19ff2 | -8.9475 | -46.7577 | 2025-08-04 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 45305013-539b-36e4-8978-1f09c7f2546b | -8.0324 | -43.1022 | 2025-08-04 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 115.6 |
| 83a1bd4d-c720-371f-aaf9-8402357141a7 | -7.7804 | -45.2093 | 2025-08-04 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| e26d52d3-39e5-314c-87be-afabc687ec1a | -12.7676 | -45.8822 | 2025-08-04 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| e4fdb5a3-361c-3071-891f-e4b5a21868e2 | -7.7616 | -45.2111 | 2025-08-04 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| d514550c-35b1-32e6-b28d-f8d873f49466 | -7.0946 | -44.3589 | 2025-08-04 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 648f46b5-a644-3168-b391-6fc7c58091f0 | -6.6329 | -59.9649 | 2025-08-04 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| f550a986-af6b-34fa-9288-1c21277d713c | -7.6476 | -45.3128 | 2025-08-04 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 7da8ef36-4e25-3524-a7df-ec930c3a1889 | -11.5307 | -44.267 | 2025-08-04 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 184.1 |
| ede10fec-340a-3638-936d-0fada91308ce | -7.5585 | -44.8887 | 2025-08-04 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| caf32607-f5fd-3ea5-9cbe-7469598952b3 | -7.0946 | -44.3589 | 2025-08-04 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 9faf3c9d-efa2-35dd-9bc3-b18ccb8651d0 | -7.7801 | -45.232 | 2025-08-04 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| b0e175eb-bae1-33c1-98be-f8a554e3b9a6 | -7.0757 | -44.3606 | 2025-08-04 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 2fb72f18-4de7-3f08-9cb1-0be8e52ff69b | -7.0943 | -44.3819 | 2025-08-04 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| ce608315-2b17-3542-9fa5-2ab7f51c5144 | -11.5115 | -44.2699 | 2025-08-04 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 469.9 |
| 8d102d71-1cad-32f4-a843-415fde1ab2f0 | -10.5593 | -45.2817 | 2025-08-04 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 190abe0a-dec9-3133-a70c-5394356e0141 | -11.5303 | -44.2904 | 2025-08-04 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 8a3d5a4b-9c05-37e0-b794-0bbf7e8b4717 | -7.9934 | -43.2005 | 2025-08-04 14:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 156.1 |
| b027cd24-34f2-3a78-a025-63b365ec0ba9 | -7.6479 | -45.29 | 2025-08-04 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 14e0d39e-9a19-3ebc-91e2-4055a13d5862 | -8.9475 | -46.7577 | 2025-08-04 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 3cba1f95-50a9-386c-9821-7b350041c9e7 | -7.7629 | -45.0972 | 2025-08-04 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 7ad64c9f-cb35-33c5-aabc-3a1ce8fc6346 | -10.5597 | -45.2587 | 2025-08-04 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 9a0b91b7-88b6-3f5d-9f1d-0ec2c6f048e6 | -11.5311 | -44.2436 | 2025-08-04 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| a1737fcc-3330-36d9-8982-6bc320e74e90 | -10.5784 | -45.2792 | 2025-08-04 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| b899cddb-61e5-3563-96cf-2a9c18997ebe | -10.5787 | -45.2562 | 2025-08-04 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 0d2477fc-8fef-3e2b-8824-a655dc658ce0 | -7.7613 | -45.2338 | 2025-08-04 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| ab0bb4e3-92dd-35de-ba77-18f9d17f26fa | -8.3663 | -46.5487 | 2025-08-04 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| d645156e-7eae-3a5b-b41c-8eb41a5882bb | -8.3852 | -46.5468 | 2025-08-04 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| c1df6e75-9326-3e46-837f-6be49179192f | -11.5111 | -44.2933 | 2025-08-04 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 231.2 |
| 7f0c9351-3471-39a4-ac61-d202d24282bb | -8.012 | -43.2219 | 2025-08-04 14:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 338.6 |
| bbe43ddd-7b79-3a9a-be14-2d051854b9ee | -7.7616 | -45.2111 | 2025-08-04 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| e344bc94-663b-3b00-a98e-b6e5c5b80349 | -7.7804 | -45.2093 | 2025-08-04 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 9094d004-1f61-34b7-9c0f-7335fca3506b | -8.9475 | -46.7577 | 2025-08-04 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 4b4ee0cd-024e-3e27-8d1f-79be7d2e45c4 | -7.5585 | -44.8887 | 2025-08-04 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| eafcbdd6-3776-3cb2-89ab-28ca10b782db | -7.4644 | -46.5875 | 2025-08-04 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 5f6efeec-0d31-3609-bee4-92286760084e | -11.5115 | -44.2699 | 2025-08-04 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 345.9 |
| 1464eba7-610f-394b-a8c8-8791d5f73d7a | -11.5307 | -44.267 | 2025-08-04 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| e6b842d1-a850-3b18-bd39-7c84ffbfbe80 | -7.0757 | -44.3606 | 2025-08-04 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 3138920e-0860-324f-bc46-6c34031ef3ae | -10.5787 | -45.2562 | 2025-08-04 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 40b6ba93-994d-3ddd-b080-92c1f0c427f1 | -11.5303 | -44.2904 | 2025-08-04 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 62e72ed5-f068-37fc-9807-7243f8ed6ac2 | -7.0946 | -44.3589 | 2025-08-04 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 2010ef02-f3fe-37d2-93dc-ec252df882c9 | -7.7613 | -45.2338 | 2025-08-04 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 3a94f816-baa6-3320-9940-048f143e6aae | -7.9934 | -43.2005 | 2025-08-04 14:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 185.6 |
| f8648fdc-e271-3c09-9734-97a1e750b28d | -8.3663 | -46.5487 | 2025-08-04 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| da33477e-1182-3dc6-934b-899affb1c1cc | -7.7616 | -45.2111 | 2025-08-04 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| f090f962-c93e-38b5-8089-8c5ab19d6ad1 | -7.7062 | -45.1254 | 2025-08-04 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 3caccbb9-2fcc-3405-88d5-b7851f68ff19 | -8.012 | -43.2219 | 2025-08-04 14:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 274.7 |
| 79ff5ec6-109a-30ea-a1c2-606e0bd5f5fb | -7.629 | -45.2918 | 2025-08-04 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| f9555cfc-8669-39a4-867a-dae17af90289 | -7.7804 | -45.2093 | 2025-08-04 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 3499f3f3-220d-3cd0-b154-2398e4affb2e | -10.5784 | -45.2792 | 2025-08-04 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 83ac7968-8b27-3a2c-a419-467ad262cba2 | -10.5593 | -45.2817 | 2025-08-04 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 72fb5eb4-9cc2-3f4b-b4a9-d18b876808ff | -8.3852 | -46.5468 | 2025-08-04 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 6a0ed8e0-1497-3ce7-95e7-3da3554eacf0 | -7.7801 | -45.232 | 2025-08-04 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 27242332-e35d-3245-859f-6066bb62c6c2 | -7.0946 | -44.3589 | 2025-08-04 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| facbf3be-0a5a-3020-bc93-28509f3061fb | -7.5399 | -44.8676 | 2025-08-04 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 483b9332-8a46-3fb0-b13c-2030853c4e8a | -7.9934 | -43.2005 | 2025-08-04 14:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 168.9 |
| cc1e78ef-2afd-302e-998e-15edd2c7e484 | -7.7804 | -45.2093 | 2025-08-04 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| b02b507b-4171-3726-a5b3-c65b3bbdf32d | -7.6876 | -45.1044 | 2025-08-04 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |


[Clique aqui para ver as próximas entradas](README29.md)
