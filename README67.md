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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f5c2f11-952c-32b2-8128-b97a2a375e05 | -6.91811 | -45.20234 | 2025-09-07 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9b0265f4-b163-36b8-b747-3b4d48d40663 | -6.19102 | -53.25952 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0aff3bb-1766-3396-abfb-394464f7c8cf | -3.83198 | -52.15386 | 2025-09-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63c118f0-bcdf-3f1c-b884-ab51dfaa3c40 | -6.26785 | -53.44465 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d219696e-c11e-3ae2-8f2f-cf5596d58c12 | -6.66233 | -48.39567 | 2025-09-07 05:10:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9717d046-17be-3395-8947-f2a68b74aefc | -5.09672 | -56.1494 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1072c33b-f73a-3af1-8c50-a7a5f6c2c4d3 | -7.67598 | -50.29537 | 2025-09-07 05:10:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8c4e8148-32fa-37d2-a2a0-08d92011f654 | -5.98875 | -44.152 | 2025-09-07 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| dda05e07-7c49-3a9d-8c20-a6cbe4eb4474 | -6.01689 | -45.88802 | 2025-09-07 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2e3d52b-41c9-3aa5-a9b6-157ca5c7e77b | -6.00317 | -44.15003 | 2025-09-07 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1f6f6920-8d60-307b-b308-d68a4d932286 | -1.96731 | -48.43818 | 2025-09-07 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f3307a2-4bf8-3a3a-9440-a066c9c02e45 | -3.90218 | -54.68629 | 2025-09-07 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a6ce2c8-52a1-3fb5-bb84-c6bef7f867a1 | -6.8153 | -50.85439 | 2025-09-07 05:10:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5050cf23-1ac8-35cd-9f6f-7cc5671db341 | -2.42782 | -49.29948 | 2025-09-07 05:10:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 281134c3-46f6-3238-ae2c-4f50d7cc83fd | -6.80788 | -52.81283 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4c76b36-7de9-344c-a1fd-5a298a911a1c | -7.67599 | -47.32589 | 2025-09-07 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2f8bf52-3b7f-38bf-af89-0f447e92259e | -5.04046 | -56.11549 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97a83124-145f-3dca-97a7-1936a1153c94 | -5.80416 | -45.65232 | 2025-09-07 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b48bb8c1-156b-3d50-a061-85dc8b98828b | -2.55448 | -48.39196 | 2025-09-07 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93d73021-4d21-3931-9194-048e88af0799 | -7.0611 | -52.71675 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f531e66f-9225-3d9f-b66f-3e310246476e | -5.90361 | -51.94309 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b5372c20-35f3-3c68-a630-cc1e0afba25a | -6.79798 | -50.84616 | 2025-09-07 05:10:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f2b37e6-5fb4-3147-b644-90b830caef80 | -6.30009 | -51.41196 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 82c29957-3a14-3f84-bc8a-3ff5e625bf42 | -5.10395 | -56.1469 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f849e5ec-18f4-3852-856b-df0cda7de9c9 | -6.2072 | -53.24908 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5060164f-ee34-3387-945b-b2516459fae4 | -6.20196 | -53.25831 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0eb87a4-1919-3f5e-ad70-f60c1ae6c835 | -6.81184 | -52.81343 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a3c3a557-6e6d-3aec-8b53-82ab93243552 | -5.21831 | -43.70125 | 2025-09-07 05:10:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 7e86e15a-dc8f-3bf6-9e8b-60e5abe601b7 | -6.29639 | -55.19441 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 544a75f5-81f1-3a37-b3ba-d2e4d8acfe60 | -4.4815 | -48.11526 | 2025-09-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 341b60d6-cc8f-3c88-bf46-7ef2aea2b62b | -6.28131 | -53.43241 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27333a9b-075a-3b11-a58d-9d35ee2c3070 | -5.48817 | -45.91053 | 2025-09-07 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9bf4917d-200d-329f-a5f0-7b7f73a2fe22 | -3.59602 | -47.51509 | 2025-09-07 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5c1c787d-15f9-3b0d-8eb6-7a6d90e72c02 | -6.13742 | -44.25124 | 2025-09-07 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbd73e58-76f8-3cea-8631-6fe68773d7fd | -6.63844 | -53.16805 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99a82578-3989-3fff-81d6-122d271f5953 | -6.20336 | -53.24861 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e623cd8d-422d-3a71-88d5-cdfb2272b17a | -5.69024 | -48.13737 | 2025-09-07 05:10:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f1d7dfb3-731d-3386-b272-4aa09e8a71cc | -6.84645 | -52.84605 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7719a316-a259-3abb-b21e-81bde836bccd | -7.76139 | -50.72493 | 2025-09-07 05:10:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 60c35e01-2ee0-391b-8081-205f352bbda0 | -5.09563 | -56.15644 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bc42ec0-e88a-3bc3-a728-ecb7ec83f49e | -3.20978 | -54.96496 | 2025-09-07 05:10:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0346b363-9ff7-3640-be60-555e718bc034 | -7.75244 | -50.75455 | 2025-09-07 05:10:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 317db07d-ed30-3fbf-b4be-ba3732f84ad4 | -6.63701 | -53.17767 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ecf96e75-9bb4-390c-9902-b01bd232d4a8 | -3.33082 | -54.90833 | 2025-09-07 05:10:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97bdede3-8e03-383e-83a2-a7625d235d39 | -5.95164 | -46.18443 | 2025-09-07 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bd806510-e0e4-3cce-b05d-2e13606037bf | -5.0087 | -56.03788 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7efeea81-ca20-3331-8e71-dddfe36e3579 | -7.81258 | -45.43807 | 2025-09-07 05:10:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1cbefc7c-3bb0-3bf3-b693-a9a2c8a32cad | -4.27347 | -48.65446 | 2025-09-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d385afd-65e3-3de8-a7f5-e52ea5c8c407 | -2.43102 | -49.3102 | 2025-09-07 05:10:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2203d800-b348-3cc2-aad6-9414a675e6bf | -5.78333 | -57.55207 | 2025-09-07 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1e36e16-6b8e-3a42-9259-9f9fd2428d2c | -6.15877 | -53.68832 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8470e010-e28a-3860-a205-110a9ab15f39 | -3.82194 | -54.12529 | 2025-09-07 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d44e7a98-1419-30b2-8c2a-d692cfaca1b0 | -6.70947 | -51.41383 | 2025-09-07 05:10:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4eaeeb1a-2a08-3e54-9b11-5116ac930d20 | -5.09454 | -56.16348 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0351e76-0d7c-3e3f-be01-4c9857a5609b | -5.78663 | -57.55259 | 2025-09-07 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| efe09fac-3726-3aef-b92c-79852a257262 | -6.66277 | -48.39252 | 2025-09-07 05:10:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 695e017a-9ea4-3c58-a45b-192c49c93861 | -5.09618 | -56.15292 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d84c026-c394-3d13-83dd-bd50b9ebb805 | -7.67546 | -47.33001 | 2025-09-07 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f9d1e5b-4b32-360a-b67a-7ba011e95202 | -8.34812 | -46.94137 | 2025-09-07 05:10:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58dd44ea-9c75-351d-831e-bc505c51a35b | -6.84571 | -52.85117 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a761d254-ecef-3b54-93f9-902606e345cf | -6.22877 | -55.93242 | 2025-09-07 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68c5d5b0-4496-3f56-81a1-bd23af7d5f26 | -3.82255 | -54.12128 | 2025-09-07 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c4f44e3-59f5-31a6-b253-3dbdd7fdd857 | -7.68128 | -47.33083 | 2025-09-07 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9c6ba9b4-0153-3fdb-8430-ff79154faf19 | -5.99653 | -44.14645 | 2025-09-07 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5725aedd-ed6c-3774-a030-a684ac9bbf18 | -7.75149 | -50.75566 | 2025-09-07 05:10:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 053e18e8-6629-3e03-a613-738f2e36b331 | -6.1852 | -45.4271 | 2025-09-07 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 0c4ece26-62d3-380d-b6c5-607aba338170 | -8.14847 | -44.87057 | 2025-09-07 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 94383a68-ea2e-3573-bd03-486098e030c6 | -6.63176 | -53.34348 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f875d4d-de4d-3203-91d3-a29d87bdfedb | -5.57736 | -49.08994 | 2025-09-07 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7eb81702-762a-3fb4-bb7b-3bc1ceeaf345 | -6.74298 | -51.97174 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afcf6809-e8fd-3223-8ba4-906aa900a834 | -6.19556 | -53.25535 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70c7cf58-13ed-3459-bb1a-3136befdedb5 | -5.95545 | -53.80182 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b043df25-a252-3c53-8fbe-b0ffad17ccf9 | -5.69515 | -49.19603 | 2025-09-07 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d593f01-79cb-33d0-8ca5-34ecb8cfb470 | -6.0902 | -57.72091 | 2025-09-07 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf87efe8-6a40-3e3c-8f5e-24527f1cf20a | -5.69473 | -49.19891 | 2025-09-07 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbdc5ae9-e5cc-33f9-9ba2-6b6c8e8ddfa3 | -6.63457 | -53.1675 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95672655-7409-3d8e-b2c2-c3ee2f76c384 | -6.27612 | -53.44114 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc77dbb5-91da-3c97-8eaf-43ef6fef6f7d | -6.20867 | -53.272 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07fe98cc-b135-3e87-bb91-3b31467a6023 | -6.01755 | -45.88318 | 2025-09-07 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a53a848e-905b-3597-aa64-e85dc6ac40b8 | -5.86871 | -51.95057 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ba015b0-349f-34a2-86c3-4a73ee521273 | -7.67585 | -47.32686 | 2025-09-07 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc47ec76-3ea5-3954-a092-e7947abbd150 | -8.33495 | -46.94846 | 2025-09-07 05:10:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f3b882c-2d03-3df9-a4f3-382d45cc0af2 | -3.15081 | -54.98582 | 2025-09-07 05:10:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9a8ba23-4cb0-3ace-8a04-ff5d140760ad | -6.27304 | -53.43591 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6f36cf3-c245-33c0-85e3-7d5c940c756e | -6.83252 | -52.80219 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9d3fc84-4b57-3d47-91e4-2f2a4d95d5da | -6.27443 | -53.42663 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94a12c91-215f-327e-8380-cba339551825 | -4.24148 | -54.96465 | 2025-09-07 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb7130f4-fea1-39b6-ba0c-29c470b50c5b | -6.27682 | -53.4365 | 2025-09-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5987b70d-db14-3c5a-98a8-7a1c90f059c8 | -6.20556 | -53.26678 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42ede6b6-0a26-3f01-a877-a2b608a04dc3 | -6.2085 | -53.24733 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a28d3e06-2b7c-3412-9309-f0cb03bd1f78 | -5.86815 | -51.95448 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40fa9bdc-52ca-3560-be44-ecaa8f68e439 | -5.79047 | -57.54966 | 2025-09-07 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 24bcca6b-6206-356f-91c3-c78a4325a091 | -8.0853 | -44.80996 | 2025-09-07 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 62f882c9-db09-3292-9e93-cf9db2646a03 | -6.81048 | -52.81465 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 33e6de70-f9d1-3552-a842-4cca56ee48c8 | -7.75033 | -48.82045 | 2025-09-07 05:10:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1bdcb4af-5044-38c3-8383-2949b35b649d | -7.2004 | -44.72821 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1046158a-0ea5-31bd-8101-0e9d3b2b24a5 | -6.81656 | -52.80893 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a43decf8-02f2-32c9-9eb9-956ddcce30da | -5.06813 | -56.06915 | 2025-09-07 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c5c70687-8fd4-3d48-a9b1-ced695e08006 | -6.19484 | -53.26014 | 2025-09-07 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b665d95-41ab-3ad5-a02a-2e8d5d1d0887 | -4.33308 | -48.3937 | 2025-09-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README68.md)
