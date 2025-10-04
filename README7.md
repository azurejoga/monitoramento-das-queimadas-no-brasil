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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 332ee310-5805-3945-bb94-eb2b3c8bc701 | -5.1967 | -45.0541 | 2025-10-04 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 707b45b7-9284-3a98-9298-0ae08be2dd61 | -11.9143 | -46.3953 | 2025-10-04 02:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 152.5 |
| e9ef5c05-111b-374d-b0e7-8ddf9e7e41f7 | -11.9151 | -46.3499 | 2025-10-04 02:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| c6f2642a-9df1-357c-b9b9-886470a397f0 | -12.0507 | -45.1872 | 2025-10-04 02:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 209.6 |
| efa0f7c9-16eb-3f6e-8557-890124483043 | -12.0502 | -45.2103 | 2025-10-04 02:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 205.7 |
| 0a4a8bc7-50ed-3992-9c35-52625c19d0a9 | -4.4258 | -43.2408 | 2025-10-04 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| c06622d4-c2d5-359b-a28b-86b8d529dc83 | -16.0212 | -50.9425 | 2025-10-04 02:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 92789603-a151-3da6-929d-6f25dc462bc4 | -3.8572 | -41.5719 | 2025-10-04 02:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 56.9 |
| 6aa4e9fb-4ecc-3247-9cc5-67023ba93c94 | -6.8774 | -47.2334 | 2025-10-04 02:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| cabfcebd-bb01-33ae-9156-e22df82d484e | -4.954 | -45.0694 | 2025-10-04 02:10:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| e2b7a2ed-a799-3f35-b65a-5b5050b29861 | -9.3276 | -54.5215 | 2025-10-04 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| d13a81a5-93cb-3113-9996-2647416d41ee | -9.3382 | -45.772 | 2025-10-04 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 27bf8f40-48dd-32d6-8b07-7a6c53a33117 | -17.7044 | -47.0821 | 2025-10-04 02:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 93391f34-ba70-3741-9b62-96ddf108aba4 | -4.4446 | -43.2164 | 2025-10-04 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 6054093e-4745-3d67-85b3-c355bc837c7e | -14.0509 | -53.9289 | 2025-10-04 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 044dbd96-a35f-3518-96fd-e33ecba3cdf5 | -5.1965 | -45.0768 | 2025-10-04 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| b3b19655-475e-3d95-b0d2-8ebb96e23197 | -8.6322 | -54.9949 | 2025-10-04 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| a9eb34f4-ddce-37d5-9c29-3b48f42afb92 | -9.3572 | -45.7698 | 2025-10-04 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| c849fb7e-d715-3d5e-9e74-52ff93c54e6e | -9.3464 | -54.5201 | 2025-10-04 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| b81cbb51-0068-34f8-9993-b937f149bce8 | -11.9147 | -46.3726 | 2025-10-04 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 210.2 |
| 1664ceab-c660-3951-b7f4-cfc0336e256a | -17.7044 | -47.0821 | 2025-10-04 02:20:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 596d3035-fbb5-3e1e-b82b-3b3ecd56aa81 | -12.031 | -45.2132 | 2025-10-04 02:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 180d6b75-ed92-359b-bf3a-8eda822a252f | -14.2131 | -46.0596 | 2025-10-04 02:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 8bc5a94b-bfaa-3871-81cf-93ca8f41e465 | -4.6135 | -43.1361 | 2025-10-04 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 93a50e7b-ff85-365a-9629-2773266c5184 | -12.0507 | -45.1872 | 2025-10-04 02:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 218.0 |
| 7d23ff2c-2b5e-3298-b439-5c1da8b70cd9 | -11.9143 | -46.3953 | 2025-10-04 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 158.1 |
| ba034150-6dc3-357a-8d3a-4dd1adf935ea | -9.3276 | -54.5215 | 2025-10-04 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| f66fbfd2-c51c-3cce-b526-958f0ae919a9 | -12.0314 | -45.1901 | 2025-10-04 02:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 175.5 |
| f6794881-b38a-3053-b50f-71b91f24fbd0 | -11.9343 | -46.3472 | 2025-10-04 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 71ce9f3d-595d-33d2-b2a2-b4c7835224d1 | -5.4556 | -43.1491 | 2025-10-04 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| fee59ce4-dcfc-3b5e-986b-519ca4b6fdd2 | -5.1965 | -45.0768 | 2025-10-04 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| b00e9a42-f7f3-3f17-aaba-ff6ecd7636af | -9.3569 | -45.7925 | 2025-10-04 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| c2fa71e8-b369-3dbc-a6cd-2acb0cc3f21a | -16.0212 | -50.9425 | 2025-10-04 02:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| d82335c0-fc24-3076-990f-0d67e7eecb80 | -15.6019 | -52.4888 | 2025-10-04 02:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 9efaa5f8-13b3-377a-8abf-f421aca050ac | -4.4443 | -43.263 | 2025-10-04 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 169a1bb2-6e59-329b-966d-958471a3f910 | -9.9172 | -50.5094 | 2025-10-04 02:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| b79fdf7c-a916-3cd6-b87e-33930ed393f1 | -4.9726 | -45.0683 | 2025-10-04 02:20:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 03e16bdd-231b-3a07-800f-d84e88eb2f66 | -4.4446 | -43.2164 | 2025-10-04 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| eadef6b2-0370-34bf-9e28-a77491b468ea | -12.0502 | -45.2103 | 2025-10-04 02:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 207.9 |
| 921036f5-b701-35f5-be1e-5cc55b730588 | -11.9335 | -46.3926 | 2025-10-04 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 806d2474-7db6-332d-b131-f1e552a0ae1e | -4.4445 | -43.2397 | 2025-10-04 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 342.7 |
| 322aa423-aeed-367f-890f-583174cb1bdb | -4.6133 | -43.1594 | 2025-10-04 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 6afff367-57ae-3aee-8345-dc48ce1b2b60 | -11.9151 | -46.3499 | 2025-10-04 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 20de9bf9-717a-3b1b-9198-f13774519606 | -4.954 | -45.0694 | 2025-10-04 02:20:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 0ed693ab-e73b-316c-bae2-4c0f1d072f0a | -5.1967 | -45.0541 | 2025-10-04 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 4bb4866d-07e4-3aaf-bc7a-0ba231778d9c | -4.4258 | -43.2408 | 2025-10-04 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 0679e569-e353-35c8-b60f-ecf60274598f | -11.9339 | -46.3699 | 2025-10-04 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 159.1 |
| a6fc57e2-0122-3aa5-a5d7-e08a23afd10a | -6.8774 | -47.2334 | 2025-10-04 02:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 50bf6de2-9e0e-399f-b7e7-75dc0fc68cfb | -4.6087 | -46.4558 | 2025-10-04 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.7 |
| fef5c71b-b245-357a-815d-b831fb6e02f8 | -9.9175 | -50.4881 | 2025-10-04 02:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| fedb7c0c-6e9c-3fbc-bbe2-8e201935570f | -12.0507 | -45.1872 | 2025-10-04 02:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| c332dbd7-e050-3603-9a8a-a6090f46c42e | -6.111 | -47.3116 | 2025-10-04 02:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| a46e757a-e18b-304c-921d-8d2dffa65e31 | -4.6133 | -43.1594 | 2025-10-04 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| e214d77a-0d7a-30da-84d5-f93f35899082 | -11.9339 | -46.3699 | 2025-10-04 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 42f1fe89-7c82-3717-862e-982cc3e16800 | -11.9143 | -46.3953 | 2025-10-04 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| ac3b45c5-b2d5-36b6-b07b-ec7ac2883c91 | -9.3569 | -45.7925 | 2025-10-04 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 5ebbaaea-6ca1-337d-b4b6-fc282d0bec04 | -11.9151 | -46.3499 | 2025-10-04 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| d2a64b28-d971-3a66-8e8c-9b105382fcc5 | -9.3464 | -54.5201 | 2025-10-04 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 338b9d32-0a1d-3241-9564-e75d4dc5c3b8 | -12.0314 | -45.1901 | 2025-10-04 02:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| ed63cc44-bab1-334b-9b16-4ad831a2202d | -5.1965 | -45.0768 | 2025-10-04 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| efc76e72-fb50-33c0-bf06-6994419c7a75 | -6.8774 | -47.2334 | 2025-10-04 02:30:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| dca392cc-4c39-3b43-81a8-174009fc5a89 | -9.9172 | -50.5094 | 2025-10-04 02:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e9236503-4434-3e8e-8e98-40cd68b9edbb | -3.8572 | -41.5719 | 2025-10-04 02:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 52.4 |
| b313d688-0304-3d20-8f66-b2a9b34aba82 | -11.9343 | -46.3472 | 2025-10-04 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| f74fbffc-5bb0-3959-a54b-cf80524eca68 | -5.1967 | -45.0541 | 2025-10-04 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| e9ddf1e8-9840-3590-b299-da86294287cd | -13.1353 | -47.8373 | 2025-10-04 02:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 97040e55-abb4-3569-9cf9-75906167d731 | -6.0923 | -47.3129 | 2025-10-04 02:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 193.6 |
| 2ae2c603-6d44-3a12-9d7e-848d5819d2db | -16.0212 | -50.9425 | 2025-10-04 02:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 140.2 |
| a7d3594f-06aa-3d71-89ab-46bda42b9a4b | -15.0374 | -49.4549 | 2025-10-04 02:30:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 55a46a8e-dd35-3917-a054-454f9b16c507 | -4.4445 | -43.2397 | 2025-10-04 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 377.8 |
| a045ec68-36b8-36b7-bee2-eca0249dafea | -4.4443 | -43.263 | 2025-10-04 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 156.4 |
| e8b41ba6-0959-306c-ad6e-21a8d6941959 | -4.954 | -45.0694 | 2025-10-04 02:30:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 9af4c68d-478f-3cdd-bb97-7f87c1592a97 | -9.3276 | -54.5215 | 2025-10-04 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| fe2be793-c5f7-32c7-8e0c-124c7bb1ae78 | -6.0737 | -47.3142 | 2025-10-04 02:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 80e7f350-844b-32e9-b580-ec3cd1d8a3b3 | -12.0502 | -45.2103 | 2025-10-04 02:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 85b42b4e-e643-3bc6-be57-d92edc7c28fb | -12.031 | -45.2132 | 2025-10-04 02:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| d0e8d84c-9d11-37b0-bd59-17793e1d4c35 | -11.9147 | -46.3726 | 2025-10-04 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 9abbe832-a4a0-3d4c-9776-afe2afcf79bc | -4.4258 | -43.2408 | 2025-10-04 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| db470829-991d-36f9-bee5-d5c403fc4a58 | -6.0925 | -47.291 | 2025-10-04 02:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 280a0968-bc80-3d8e-876c-5a6d5af41b3e | -5.1965 | -45.0768 | 2025-10-04 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 3fea8896-3ca1-315b-98cf-9b56707b97fa | -15.2399 | -56.8393 | 2025-10-04 02:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 36a60be6-a991-3567-b1e6-bbe0c3b01a6d | -11.4877 | -46.7696 | 2025-10-04 02:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 66e80374-43f4-3ad8-b2fb-57da7f864209 | -6.8774 | -47.2334 | 2025-10-04 02:40:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 554223b2-1461-38c4-9d46-431bb9f89871 | -4.4258 | -43.2408 | 2025-10-04 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 0337f63f-1474-34cd-8099-1c28a2b7dcb7 | -11.4881 | -46.7471 | 2025-10-04 02:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 5418300b-d7ce-362d-863b-b4d37082e7c1 | -4.4443 | -43.263 | 2025-10-04 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 4c71dca0-e2f8-362a-8eb1-9374601e1b91 | -5.2152 | -45.0756 | 2025-10-04 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 8d52e674-f3a3-3051-8209-c372198727db | -9.9172 | -50.5094 | 2025-10-04 02:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| a6fe2bc8-2870-3d04-8d54-339649a0230e | -4.954 | -45.0694 | 2025-10-04 02:40:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 6f3466a3-0d5a-3162-9c32-9d09473161bd | -9.3276 | -54.5215 | 2025-10-04 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a6434d94-53a0-3972-a5e1-9389befab399 | -9.3464 | -54.5201 | 2025-10-04 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 9c76afd1-f437-37e6-ba1c-e70120950065 | -17.7044 | -47.0821 | 2025-10-04 02:40:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 3d9ea03e-7db5-3b47-bb65-8e5914569272 | -4.6133 | -43.1594 | 2025-10-04 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 80c24473-707e-330e-9ba3-5cf4881161d8 | -20.1352 | -46.4218 | 2025-10-04 02:40:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 9920415e-da9e-3f53-9e2d-5218927155a8 | -5.1967 | -45.0541 | 2025-10-04 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 5b431895-599e-3b84-a02e-8861b24b611a | -4.6135 | -43.1361 | 2025-10-04 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| b22b22f9-c950-327f-b488-83db7287c2b6 | -15.2205 | -56.8414 | 2025-10-04 02:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 60d88a05-0938-33bd-be84-fa1ca5484aa3 | -11.9143 | -46.3953 | 2025-10-04 02:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 29266ae3-0c84-3851-b9ff-4bfe7846aa19 | -11.5069 | -46.7671 | 2025-10-04 02:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 22c9b59f-c7e7-3ceb-9012-36121910fdfb | -16.0212 | -50.9425 | 2025-10-04 02:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 114.4 |


[Clique aqui para ver as próximas entradas](README8.md)
