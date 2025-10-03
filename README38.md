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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8719ee99-1d20-3464-8810-657d101b1aa9 | -13.74924 | -47.98865 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c50d84a3-efbf-3c8f-bc0a-fe3d242d9bd5 | -14.56898 | -48.33489 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e6f7e15f-9411-3b50-972d-bb3eb31babcc | -13.63755 | -48.67133 | 2025-10-03 03:45:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1f206a35-6434-3e6d-80cc-8af2f9723502 | -12.90169 | -46.8963 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fc6fbda-f3ad-341c-8984-cbf2b321fdcd | -12.6112 | -46.97581 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 92d3d677-41a5-3a22-8197-5b661f6eb824 | -15.31915 | -46.89501 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec0eb321-fe89-32df-97d7-00f578c97870 | -10.82817 | -46.58918 | 2025-10-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c4d8e4d-d1e4-3908-8928-237ccfdb7fa9 | -13.77924 | -44.24425 | 2025-10-03 03:45:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88555a82-b537-30d2-aedd-4259da3d5abe | -13.75292 | -47.979 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3719a49c-a778-3216-89c9-42ad58c3e127 | -14.43273 | -46.10486 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b593e750-47cd-323c-96a6-c3f2411f1478 | -15.21412 | -47.9904 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2931b0e4-1d01-3986-88de-96b8070b5619 | -9.92358 | -43.73397 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d0ea3b61-7a28-35e6-9e9b-6717de57a9df | -11.83711 | -45.04356 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09dee7f4-d1ba-3ffb-ac23-e9bc84821374 | -11.06735 | -47.80094 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 39653170-c560-362f-b326-e1399b12290d | -14.89076 | -46.973 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0f37dfb-824d-3f7a-b805-99188d3ddbb4 | -12.91143 | -47.16144 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 185f639d-5d48-33d1-8723-bf9e1d983c8e | -10.96466 | -44.33517 | 2025-10-03 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 403b0848-5c00-3309-ae2d-ca01dc1b2fcc | -12.63659 | -46.99555 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69cb659f-d3d1-3df6-b8da-7a809ccdf6f4 | -13.15153 | -47.83111 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8cb54963-2eea-3b19-8594-b4499726e076 | -15.75013 | -43.70967 | 2025-10-03 03:45:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dfb85d8-0bb8-371f-9cbc-9b7016cc065c | -12.68488 | -48.5462 | 2025-10-03 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b4129d1-753c-30af-8c40-887cf94fb956 | -14.73991 | -48.09532 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e765c703-3f68-31bf-9a79-556fdffec200 | -14.98201 | -49.9718 | 2025-10-03 03:45:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 76ffef00-950e-3d0a-b07f-632cd5189520 | -15.92223 | -43.34451 | 2025-10-03 03:45:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cc50ba44-fba6-3128-ad96-09acd7980e51 | -11.14254 | -47.19646 | 2025-10-03 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 44a29e07-9fa8-37d9-9e23-d1d9eb74789f | -12.63276 | -46.95537 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 829eecfb-b5c4-3548-921d-cc0039ddec36 | -13.16069 | -47.89737 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4a04619-888c-3b1c-a155-588c2a8086dc | -9.91024 | -43.72602 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 60bbd516-c0e3-3025-9c57-e61f470b983b | -12.68993 | -48.54487 | 2025-10-03 03:45:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 807857b1-4ea4-3de8-9da3-caace2d581d4 | -13.7694 | -47.54108 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c861b7e0-2034-36fe-a4f1-76f18493b0ac | -14.35947 | -43.84126 | 2025-10-03 03:45:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 386b8d2f-c6e3-31a5-8a15-f2d8e3f0f70f | -15.28751 | -49.30566 | 2025-10-03 03:45:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5209aa1d-d8c1-3bb6-a280-106dc6a8a1fa | -9.06946 | -46.64675 | 2025-10-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 41616744-f5d9-39d3-b45e-7a96963622a4 | -13.12678 | -47.88295 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d6137cf3-c1a3-38ab-b3dc-32db3591ce7b | -9.937 | -43.58086 | 2025-10-03 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8845e624-9074-397f-a9e0-57b2d8b8b444 | -11.91812 | -46.28761 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 550a9c5b-4fc0-330c-8263-a4fe83e4196a | -15.2977 | -46.29269 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a8f92b5-9dbd-36ee-a036-c21207e8d040 | -11.11844 | -47.86395 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cf507042-786a-3e23-8d84-06fe65694f32 | -13.24106 | -48.49676 | 2025-10-03 03:45:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 92a43d78-c225-3d20-ad13-d0dd1d31a033 | -15.49152 | -45.93342 | 2025-10-03 03:45:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7e7d719-dadd-3116-902f-a577b9ac6c2b | -13.5668 | -47.58794 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 384affbb-7a40-30db-8259-da86b7ee0811 | -13.80111 | -48.06399 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0380bd0-83b1-362b-9ef8-52093c48e1a3 | -13.31623 | -47.18847 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6497078-628c-36ec-b6f2-6c7c3a2d21be | -12.62461 | -46.9969 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8bd68e08-7732-30d6-b7b1-8ba72fabaed8 | -12.62703 | -46.95484 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0d45075-d408-346c-a934-fca436a01f44 | -13.38163 | -47.28487 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 541c59b1-a602-3585-bb81-d7696cfa7ef9 | -15.34886 | -47.06256 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e10a5ae0-2283-3fac-b5a0-fd14c158707b | -14.11475 | -45.65845 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d43630ac-b693-38b8-8a82-e1172bf8fa00 | -14.87099 | -48.30983 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 06c97b74-4411-39b0-908e-25139dfc3bad | -11.91456 | -46.75038 | 2025-10-03 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb12fea5-4972-385c-a593-be9d4ea08de7 | -14.88206 | -46.84986 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c51d7fd8-7048-3aa2-9ccf-a6e84abe3f3b | -11.49378 | -43.50116 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f49169ea-9975-32af-9641-63edbc1d2950 | -11.07118 | -48.36184 | 2025-10-03 03:45:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 53f21db1-38f5-369a-823b-deb7e05cf0d8 | -12.40877 | -40.92089 | 2025-10-03 03:45:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 33eb355f-baa8-370b-af48-0b5eaf958186 | -14.90753 | -48.30209 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 25b300c6-bebf-37ad-8812-2598814a69ae | -11.81053 | -45.01821 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7e60062-b4d1-34f4-8792-79e024f85314 | -13.11916 | -47.87062 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e4bbd44a-1480-324a-9675-1c3f056435ef | -14.7439 | -48.10524 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0093c5ff-a630-33a2-9b9d-93c96a3d1ff0 | -13.797 | -47.58105 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4fde760e-19ae-33eb-93f5-ecce624b1acf | -11.10428 | -47.83873 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 48370ead-bbea-331a-8cf5-e00aad92259c | -14.66917 | -48.2668 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b77f3d34-d158-3d39-a6e0-a90b60443123 | -13.6672 | -47.30882 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14ec1d15-fd62-3892-8f1c-a730eb62128e | -13.97986 | -48.15868 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0e754049-3a97-3d5b-b015-e08bf7db11bc | -13.13815 | -47.88742 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3aecc45e-8e8f-3967-b9d2-5090131a57c7 | -12.61032 | -46.9803 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ec8d0928-c538-3177-b761-e70f5ebb888e | -13.97243 | -48.16483 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cba5828b-769c-3e21-aa7e-121832590215 | -10.856 | -47.22095 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 29303d8f-f8d1-34e5-a3fa-350e2de0f5c9 | -15.92894 | -43.07599 | 2025-10-03 03:45:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb9a6df0-959f-388b-8155-a41e344e1b1d | -15.35976 | -47.06411 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89fdeb90-005b-333d-acee-75ce29066ba7 | -11.85189 | -44.96342 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2c7d8da-6f3d-3bcd-8bf1-c3654ed9badf | -11.55956 | -47.66309 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c789310-4393-3200-a916-1973f80bb570 | -14.11543 | -45.6605 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39d9de99-972b-31a0-94ab-483d5c8fc07e | -14.29203 | -45.88825 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c44da1df-bdc1-3f7f-ae3a-f7c56ee6983f | -11.84198 | -45.03942 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73a6b7e8-199f-3d02-9a26-4824d5d13f7c | -13.05358 | -47.04913 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c2bd38d-f9e6-38fa-b76a-def9a5409dc4 | -13.55843 | -47.29642 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e3cfb275-eec5-354c-b4c0-f8d8402ecead | -13.66839 | -47.30302 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9917eba-6146-3eaf-8122-a04899af6e9e | -12.89921 | -46.93909 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08135f63-00a5-3738-b99e-e6e91863870a | -15.28168 | -47.90311 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53d4dcf6-0c63-3d01-98a5-47e6f8c501fa | -12.62343 | -46.97314 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a3090ab1-cd66-34a6-a5c9-b46b38dae19f | -13.74145 | -47.9966 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7585f5b5-0ec1-37c3-9262-922f1bfc97ce | -13.75787 | -48.07646 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1690f2ae-2291-36e4-bfa9-2c6027951862 | -14.71731 | -48.20333 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0f599a4-df1c-31f1-b69f-604b5c75c530 | -13.31234 | -47.59591 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 53e3f1c3-e1f7-3cc3-ba8d-ed2b1074afde | -15.35369 | -47.06632 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78f5b0a7-2912-3614-a32f-76fb389854ca | -14.28844 | -45.91993 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b3c7cda-47ef-37a9-94e5-06dc9a03ac64 | -12.75076 | -44.91855 | 2025-10-03 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3a97a59c-7aaf-3182-8266-c96055ea144a | -12.61605 | -46.98089 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a18a5e64-d14c-3fb4-9388-cb599606850f | -13.47837 | -47.24173 | 2025-10-03 03:45:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac3e8df3-132d-34d2-a55f-440ce999e20b | -11.60496 | -47.65367 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e93e88dc-7b93-327e-88fb-aa6cf0e4c227 | -13.15597 | -47.8306 | 2025-10-03 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ca6253ff-c95b-37dc-996d-a7ba82832de9 | -14.57278 | -48.32846 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 613fad25-3742-32ea-be93-5dc0d2468cc5 | -14.91405 | -48.30016 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 310f6312-afc2-3eae-a28d-10b646516f5a | -9.94075 | -43.74801 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f322e872-09b6-37b4-9f15-80fb252a0147 | -11.87456 | -45.00529 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5d600e3-3bf1-33e1-abce-e2415ac89e83 | -9.71254 | -45.43346 | 2025-10-03 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f233c9cd-7349-376e-b92f-0f95d9017b3f | -12.93622 | -48.43172 | 2025-10-03 03:45:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8080f337-c6c4-3251-b11d-150ef5608312 | -9.95208 | -48.7803 | 2025-10-03 03:45:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 94ee536d-e191-3ead-bbc7-ebdfa62d35b0 | -14.30353 | -46.01799 | 2025-10-03 03:45:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 08d0e01d-a210-3a05-9e02-35181ce05ad3 | -15.31997 | -46.2979 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README39.md)
