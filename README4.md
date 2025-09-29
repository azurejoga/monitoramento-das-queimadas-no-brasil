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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b14d34fc-cfff-3e4b-aa76-933085954e9a | -16.02118 | -59.49567 | 2025-09-29 01:30:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a1fd0e64-0e51-3678-a5fe-4310d89ce218 | -16.01176 | -59.49711 | 2025-09-29 01:30:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6815ef7f-99dd-3dba-9bd8-4697b561bfea | -11.6215 | -52.86792 | 2025-09-29 01:30:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 36.5 |
| a15a2182-2f30-31a0-b35e-276ea5171de4 | -11.62655 | -52.86171 | 2025-09-29 01:30:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 2ba91491-c3e5-32aa-b356-ada9f5fc3864 | -16.02268 | -59.50571 | 2025-09-29 01:30:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 6ed0deb4-6952-34ec-8fe2-22dbecf61bdc | -7.2402 | -44.7812 | 2025-09-29 01:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| e13cab9f-c000-3be5-a2f7-b628b43a072b | -3.1012 | -47.0301 | 2025-09-29 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| bde1fd55-cf1b-3011-b46d-b9a85ab2d7d8 | -4.7159 | -41.9736 | 2025-09-29 01:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 038d6ea3-09f0-3c68-a3d1-2570b69fbe76 | -15.2893 | -49.5035 | 2025-09-29 01:40:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 530be4a5-8972-39b4-bbbe-763e5e5ccaa9 | -4.7157 | -41.9974 | 2025-09-29 01:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 49.7 |
| 120ffeeb-7703-333d-9206-b2950b68bef1 | -20.0491 | -41.3251 | 2025-09-29 01:40:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.8 |
| 8122a5d9-a858-31aa-a089-d814c24871e8 | -17.0938 | -48.5699 | 2025-09-29 01:40:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 69b8b0ba-6947-3e7d-9a63-faa88a229733 | -2.5772 | -48.4146 | 2025-09-29 01:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 073352fa-05d1-3a24-8800-8c94829f79cb | -11.9442 | -48.0248 | 2025-09-29 01:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 3cf695c5-27df-3583-9c29-bfe450a14290 | -2.5773 | -48.3931 | 2025-09-29 01:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 1452191d-8791-3097-849e-d158e1bdd23f | -11.925 | -48.0273 | 2025-09-29 01:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 879811b2-885f-32c0-bfb6-78f0d499d98d | -12.6913 | -46.8934 | 2025-09-29 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 8b3fe081-6944-3ad4-85d0-fa471cc31bf8 | -10.0531 | -50.1978 | 2025-09-29 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| e47bbf17-808d-32d0-bccd-ed779c5845f8 | -17.0739 | -48.5735 | 2025-09-29 01:40:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 867033d9-46b1-3280-b70b-6f9901d4d7b7 | -15.2888 | -49.5256 | 2025-09-29 01:40:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 8ad8dbd3-5a37-3090-81e0-1a63a5cd1b74 | -4.4013 | -44.0755 | 2025-09-29 01:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 0cbc8a87-8d17-33b0-826d-bca9585438f2 | -3.1013 | -47.0082 | 2025-09-29 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 3e7c1d96-d4c1-3b94-8b71-074a5c69eab4 | -14.553 | -48.4237 | 2025-09-29 01:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 1f3c0849-cc71-344e-8a79-b31f382167ba | -9.4194 | -54.697 | 2025-09-29 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| d4f8b640-13f8-3386-82ef-edbc08c1a342 | -7.2214 | -44.783 | 2025-09-29 01:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 0306f6c2-ffdc-3507-a67b-851f51d2b6d9 | -9.4007 | -54.6984 | 2025-09-29 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 97542987-faf7-323b-919b-2839930b9b09 | -15.0868 | -49.9085 | 2025-09-29 01:50:00 | GOES-19 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| b5eef4db-0911-3506-b949-2e3379f1c2c4 | -15.0673 | -49.9115 | 2025-09-29 01:50:00 | GOES-19 | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| dc3870ba-731f-3a86-b0ff-4c2c4897bb8e | -15.0678 | -49.8895 | 2025-09-29 01:50:00 | GOES-19 | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 6ec8b94b-1fd6-3580-a119-061a9ec03d75 | -15.2893 | -49.5035 | 2025-09-29 01:50:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 3744b1c0-9d5a-35ed-a74b-ce68951d8564 | -7.2214 | -44.783 | 2025-09-29 01:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 169.8 |
| caa8633c-6b89-35d3-bc0e-082709300de6 | -15.2698 | -49.5065 | 2025-09-29 01:50:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 8d16a11d-e5ca-3d71-870d-7b7f689f5514 | -11.9442 | -48.0248 | 2025-09-29 01:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| be05b492-395a-36ee-8d85-98d01946dfaf | -15.0872 | -49.8865 | 2025-09-29 01:50:00 | GOES-19 | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 24da7418-31d1-30a8-976f-3caf77d6ff86 | -3.1013 | -47.0082 | 2025-09-29 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 563b6acf-7fa9-3bb3-9cba-fa76d674eda1 | -17.0943 | -48.5472 | 2025-09-29 01:50:00 | GOES-19 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 24bd5253-7adc-3d88-9c15-c283a4f8c6e8 | -0.1012 | -51.2738 | 2025-09-29 01:50:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 31.9 |
| f5a74fa5-e7a5-3097-9c33-42e9e32af79a | -4.7157 | -41.9974 | 2025-09-29 01:50:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| d407c4b5-b3e8-346d-b692-0f3cbdb0b5ca | -4.4013 | -44.0755 | 2025-09-29 01:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| afc500f8-5479-317c-b608-c681fece1553 | -7.2402 | -44.7812 | 2025-09-29 01:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 6f0e7bf9-f280-35b0-8d99-c41d172d94c5 | -2.5773 | -48.3931 | 2025-09-29 01:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 0c4165c9-fd73-3580-b591-63d292a39f76 | -9.4007 | -54.6984 | 2025-09-29 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 4611d331-b5f3-3c1b-8f2c-b24148982925 | -15.2888 | -49.5256 | 2025-09-29 01:50:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| f1942cad-e454-3fa1-ac33-732886420381 | -14.553 | -48.4237 | 2025-09-29 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 48.1 |
| d9ea64d8-7b4e-3d2b-951e-b4f3a25e8dd1 | -2.5772 | -48.4146 | 2025-09-29 01:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 49b53488-e618-370b-98b1-1133efc94f0a | -4.7159 | -41.9736 | 2025-09-29 01:50:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| f48db550-7fa5-3e7c-920d-2ddc8ea77a1d | -17.0938 | -48.5699 | 2025-09-29 01:50:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 0f0aa510-46b2-3857-952b-66ce597569a4 | -3.1012 | -47.0301 | 2025-09-29 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 297983b5-0286-3167-8f2e-96df1509bf15 | -15.2897 | -49.4813 | 2025-09-29 02:00:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| abceefe2-3fb8-3e84-b3dd-0ceadd8fc70e | -17.0739 | -48.5735 | 2025-09-29 02:00:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 59c31148-1cb9-3cba-9493-368860fb61e4 | -11.925 | -48.0273 | 2025-09-29 02:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| e7fcfd34-1554-3e11-a38d-09401fcf603a | -4.4013 | -44.0755 | 2025-09-29 02:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| f253b857-95b5-3d94-92b3-a7d2cf182686 | -11.9442 | -48.0248 | 2025-09-29 02:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 79cc7659-1213-393b-a494-3749212c4ce2 | -4.7157 | -41.9974 | 2025-09-29 02:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 62.2 |
| 232af624-ad73-3dcf-bad3-7e383b775a17 | -15.2888 | -49.5256 | 2025-09-29 02:00:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| b03bcce3-9a09-3369-b1d9-9267eb906eaf | -9.4007 | -54.6984 | 2025-09-29 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 406c4c77-7d2e-38a1-b948-ec61fc5814dc | -3.1012 | -47.0301 | 2025-09-29 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 61876989-b98f-3b26-a462-522ee1c807cb | -8.1423 | -46.414 | 2025-09-29 02:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 5c1721a1-fe79-3cab-9fb0-96f5383b207e | -8.1425 | -46.3917 | 2025-09-29 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 73468a64-cf27-3f91-8251-8b770974e3f9 | -2.5773 | -48.3931 | 2025-09-29 02:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| e62a9d0c-2b8a-38c6-b3ae-09424751c9b2 | -3.1013 | -47.0082 | 2025-09-29 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| aafc974d-f380-37c9-aba1-169758fa2c05 | -0.1012 | -51.2738 | 2025-09-29 02:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 38c6a655-9325-31c2-b705-5a080135d41c | -15.2893 | -49.5035 | 2025-09-29 02:00:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 216.8 |
| 3d9ec636-fb98-3c58-86c4-d8cd3f86b5c6 | -7.2402 | -44.7812 | 2025-09-29 02:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| c8827361-354b-3dc1-8eb0-b7267c891ee4 | -4.7159 | -41.9736 | 2025-09-29 02:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 1a37f4e8-0176-390e-9576-4916cfa6a7d8 | -7.2214 | -44.783 | 2025-09-29 02:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 152.4 |
| c29d24bf-043d-3f71-bbf4-1e03a9526b2c | -17.0938 | -48.5699 | 2025-09-29 02:00:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 113.9 |
| a2544d6f-d1cd-3fdf-951b-4f8023127e80 | -14.553 | -48.4237 | 2025-09-29 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 12131b03-5700-3016-9bcd-24def961c61a | -2.5772 | -48.4146 | 2025-09-29 02:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 04ae43c1-e6e7-3f7b-9489-35ab8967382e | -14.5526 | -48.4461 | 2025-09-29 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 522ffde8-b594-316f-85f2-af783aba2714 | -3.1013 | -47.0082 | 2025-09-29 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 099cf98a-e54f-35d0-8e23-51692864ec70 | -11.5012 | -44.8525 | 2025-09-29 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| f65fef53-70ee-3197-a270-9d79f887cc7d | -17.0943 | -48.5472 | 2025-09-29 02:10:00 | GOES-19 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 1caf5244-1e2b-3aa7-8953-0fdafab7dad6 | -3.1012 | -47.0301 | 2025-09-29 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 3099a471-d968-34be-9a3c-ab261b18f0a2 | -7.2402 | -44.7812 | 2025-09-29 02:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 723833d2-8e02-38f0-b0d5-5e09bee4f586 | -12.8103 | -47.7505 | 2025-09-29 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 257560fd-5e4a-3019-9f91-1181fcf95231 | -10.8238 | -45.407 | 2025-09-29 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 86574104-6f43-3160-b3a7-c3d2fe5c0530 | -14.553 | -48.4237 | 2025-09-29 02:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 5da8c50d-d949-39d7-b7e1-f668549ee44f | -15.2698 | -49.5065 | 2025-09-29 02:10:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 08f99418-84ae-3b0d-b8a2-48c3aa9f83ce | -15.3088 | -49.5004 | 2025-09-29 02:10:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| be6c002b-a23b-3aa9-bcf4-f5e8c9113586 | -14.6049 | -45.0161 | 2025-09-29 02:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 23cac024-52d2-3ce3-9535-934ac68270a3 | -8.1423 | -46.414 | 2025-09-29 02:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| f11904e8-3fbe-3ec7-a8ba-c4862f56156a | -15.2888 | -49.5256 | 2025-09-29 02:10:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 98e9177f-5d40-31bf-bdf5-59c712e66990 | -12.791 | -47.7533 | 2025-09-29 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 7df97919-6fd4-3591-9230-2ed719c6bb84 | -17.0938 | -48.5699 | 2025-09-29 02:10:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 31869a97-b78d-338e-aab7-de75fb7bf2db | -2.5772 | -48.4146 | 2025-09-29 02:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| aaa66311-339d-3c62-856a-8a83f9df4b2c | -12.8585 | -45.1541 | 2025-09-29 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 556f7424-c0e8-3103-ab82-39782fd8142e | -11.925 | -48.0273 | 2025-09-29 02:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| bbed86d9-d66f-355a-9a15-7c66367c98cb | -4.7159 | -41.9736 | 2025-09-29 02:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| c0824280-1558-3555-85ef-a8ebd3981da4 | -11.9442 | -48.0248 | 2025-09-29 02:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| f189dfa1-f048-36bb-ad8a-b82444343fff | -4.7157 | -41.9974 | 2025-09-29 02:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 64.9 |
| 2697315a-4301-3cb6-b931-9a29e87110d1 | -10.8429 | -45.4044 | 2025-09-29 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| ac4d506f-d94d-3716-822a-f70d3f6a81cc | -2.5773 | -48.3931 | 2025-09-29 02:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| ae35948b-9b50-376f-81a9-6e586ae6a10a | -11.8291 | -51.7937 | 2025-09-29 02:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| af5b8af1-39bb-348c-8fec-d92103dd7a3a | -7.2214 | -44.783 | 2025-09-29 02:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 153.1 |
| cea9152f-97eb-3928-be3a-f1a1d3f5b494 | -15.2893 | -49.5035 | 2025-09-29 02:10:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 181.7 |
| 0937c699-4711-3da6-8347-e20d7d22de0f | -11.9442 | -48.0248 | 2025-09-29 02:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 2d64ce19-0d1e-353b-ad22-f214b84afeff | -20.0491 | -41.3251 | 2025-09-29 02:20:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.7 |
| 9e5c6f33-0e57-3fea-a4f8-0d1026671081 | -14.5526 | -48.4461 | 2025-09-29 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 61715db5-2985-3587-ace8-464e77e75283 | -2.5772 | -48.4146 | 2025-09-29 02:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |


[Clique aqui para ver as próximas entradas](README5.md)
