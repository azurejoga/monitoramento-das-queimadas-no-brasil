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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3b5c3e6-b11f-312a-b82e-fdb6ca0414ab | -12.41347 | -46.45855 | 2025-09-01 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f647f75d-2929-31b0-ab73-2b8a50717279 | -13.69536 | -46.92478 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05bbf5d7-a6e4-3467-ad53-22f65b66d84e | -15.23285 | -53.79362 | 2025-09-01 04:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acc294c7-44db-38c1-a5e2-bde978129e8d | -13.358 | -44.6253 | 2025-09-01 04:12:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e285080-eaa3-378f-82e1-f2133b11c30e | -13.3645 | -46.9388 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3beab2d8-1bd0-37f0-96e3-8ad55359e81b | -13.49347 | -46.97602 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04522cab-f073-334b-a0b7-0d95ead40082 | -13.65936 | -46.93263 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec0e2cae-2ef5-3893-8651-3a743f4d3fca | -14.81987 | -46.72435 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c708b2e4-0337-329c-b39d-adf9ec8e2f9b | -15.32478 | -46.10669 | 2025-09-01 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84340ca3-8940-39d2-afbc-2d049243dcb6 | -15.59737 | -48.35995 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce80bd00-a70c-3360-bbec-d1b4ed3e945d | -12.86876 | -48.16938 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a663823d-b067-345d-be34-5ed3446ebd1c | -14.75266 | -46.76695 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| eea5223d-cde2-3974-a368-e6d4f2b22eb0 | -13.69431 | -46.88568 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9026181-7183-3f54-9159-26a30b25c4e0 | -14.7469 | -46.75665 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7d39fb9-f8df-3557-81bd-afaa757a4761 | -14.7482 | -46.77097 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c7ee6241-38ad-367c-8864-b6c97e68017b | -13.53625 | -46.97488 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ad6c62d-1546-3325-8b4d-8615062b8272 | -13.6886 | -50.76831 | 2025-09-01 04:12:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b150643e-9175-3cc6-b39e-875d6b4f1b5e | -15.70137 | -45.42021 | 2025-09-01 04:12:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ab3ee24-94f9-33dc-ab30-b69b093d9200 | -13.69569 | -46.8777 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01cee683-c557-3bf5-ae17-1025d0e0e169 | -12.84011 | -48.07244 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ec07c6f5-0f55-32fa-8c82-44624a65b137 | -15.22727 | -53.79227 | 2025-09-01 04:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a53dc7f9-591e-3b9c-ac07-47ef826dd9f0 | -13.3675 | -46.94387 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 29737804-f7ef-394c-8932-f4452ed72dfb | -16.13623 | -49.04829 | 2025-09-01 04:12:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d6e0632-4de3-3fed-8055-fca93c5c2117 | -12.87049 | -48.06615 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 535aabc4-eaf2-3da2-90a2-28b4d0399e44 | -12.86245 | -48.0644 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4af901df-a3d0-325a-b453-2538e424baba | -13.54162 | -46.96621 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ac959e3-fbcc-322b-9231-ac61d4bb4419 | -14.74323 | -46.7561 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e974050c-cce6-3b20-9771-a93dddf3d496 | -13.53995 | -46.97591 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 10fe3f29-5d0e-313a-9df6-1e120517f97a | -14.27705 | -43.52773 | 2025-09-01 04:12:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f711f244-37be-3d8f-b877-811d772769ec | -13.69558 | -46.92773 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0f09da4-161b-342c-bb85-300c7683c5a8 | -16.78081 | -49.31143 | 2025-09-01 04:12:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f228efa1-0976-3353-a7a1-937811eceea5 | -13.33239 | -46.85571 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae82eba8-5510-3bc0-b57a-197d0f87264d | -12.60329 | -48.20496 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 71229470-55c8-33ef-9b6f-7434b541770e | -13.58227 | -46.9319 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1277671b-843d-3c5f-830f-e8f58a6fcba8 | -13.48527 | -46.93464 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59dc59dc-4ea9-3dc7-a873-c3fab92ef8f3 | -14.7607 | -46.76398 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a3f26e09-b762-3716-8e71-dc97b8e510b1 | -13.68486 | -46.9187 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3798e41f-cccd-3950-9cde-dc0bf191ce02 | -15.08503 | -48.12548 | 2025-09-01 04:12:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80d359a9-4d95-3f9f-94c6-adbfe1b49e95 | -12.82729 | -48.07415 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b82b99b6-c6c1-30af-824c-b7c5cb86987b | -13.48546 | -46.99959 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 25223ae5-cb88-349c-8371-cebc38b60f10 | -14.76877 | -46.76083 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cc09398-9830-323a-b0a0-0dd05356f7f7 | -12.95093 | -48.10408 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e898bb6-d754-3940-a2c0-1ae24566f2b3 | -12.63423 | -57.0031 | 2025-09-01 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0043504-051d-311f-aeae-b26dabe63290 | -15.07812 | -48.11875 | 2025-09-01 04:12:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6989ac68-b428-312c-b8c4-e6dda2b2a605 | -13.29557 | -46.91208 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11a9f908-88a4-3bbb-bb40-fa13bc06e335 | -15.3283 | -46.10733 | 2025-09-01 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e3c6fdce-4a1e-341c-9718-14dae18e81fc | -15.70558 | -48.92157 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5110a40-3555-3beb-9897-a358cc8c3a6c | -16.20049 | -44.22177 | 2025-09-01 04:12:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4213836-ad09-3b43-822f-bc8d8c0ebae7 | -12.60149 | -48.22346 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| e437e929-40cb-3ac7-acaa-dd385363eb67 | -12.86582 | -48.06892 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9dee522-9bb6-361c-90c3-9980120d5a64 | -12.61352 | -48.19523 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 457acde5-df00-3916-9205-f151d1ede043 | -14.02422 | -43.90448 | 2025-09-01 04:12:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7a26f42-1dd7-3b90-b7d3-8717015f4c9c | -16.07941 | -43.62142 | 2025-09-01 04:12:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41d839e8-4a4a-3a5f-a931-c85ad5364032 | -14.86399 | -46.77337 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72899535-c53d-3732-98a0-144e84c20f6c | -12.63274 | -57.01001 | 2025-09-01 04:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 691b6efe-8de9-326c-bb7a-bf57ee7c1693 | -12.94795 | -48.10057 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f448fcc-fd52-3abd-a51c-b12a4d4d3b59 | -15.72673 | -48.98439 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| bd843199-7942-38f7-ab50-f55f5e5d1b31 | -15.73075 | -48.98554 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| dadee98b-de58-3056-9788-2168a294c2a0 | -15.77582 | -47.80703 | 2025-09-01 04:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 0aefdf63-0c6e-3646-89ce-09abd8acd3ca | -12.86469 | -48.16863 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07a88c3a-58da-33df-8fa5-6722a2b5b5f3 | -13.69908 | -46.90793 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31f2a592-48b1-3ba4-9337-c713ede55cc2 | -13.69532 | -46.9074 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6dab1b0-8267-33a8-b52a-f4f180858f80 | -16.20107 | -44.21815 | 2025-09-01 04:12:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 733f55cf-ebf1-39eb-8bec-05ac74fa70c9 | -17.20795 | -46.06604 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0fc4c316-f081-3550-9f92-87960a3f0a85 | -13.50669 | -46.98903 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 230ea0d6-ab61-3626-b0ac-04b5a654faa2 | -12.56525 | -44.7902 | 2025-09-01 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e6ff874-96fe-3e08-8598-8dc336e7a8d0 | -15.72598 | -48.89772 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9f761ef-d432-3762-9714-f811ecfe2173 | -13.49635 | -46.9817 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f0a1538b-f007-37b3-9df5-d6d8d7b4e54c | -13.36373 | -46.94333 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5ab61913-609b-31f5-9269-98a744f53b34 | -14.36694 | -53.30564 | 2025-09-01 04:12:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30037d19-a85f-3fa3-9ae0-6d3fa8545410 | -15.7729 | -47.8013 | 2025-09-01 04:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 33659ca8-bfca-34e6-8f43-4ce06330c293 | -17.83012 | -44.32746 | 2025-09-01 04:12:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 22dbdda1-1028-3528-9271-16b0fe773d20 | -13.47399 | -46.93287 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb980fc0-b5c5-32e6-9343-1cc621497752 | -12.955 | -48.10467 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fffab60-f0f2-341c-8ece-4fd8a786ff37 | -14.73814 | -46.74205 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2be09717-6641-38b6-90f0-3fd665ea20a4 | -16.51289 | -55.0337 | 2025-09-01 04:12:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7805ec8-96c0-37d2-b48a-7bf1420ec203 | -11.51616 | -54.47144 | 2025-09-01 04:12:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 545044c0-344d-30b8-9765-e989d35f6262 | -13.16978 | -45.27897 | 2025-09-01 04:12:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| b5059cf7-cabe-3b8c-ac47-46571e71b456 | -12.40901 | -46.46226 | 2025-09-01 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bc15887-c93b-3b0a-872b-fa093481e506 | -12.64501 | -44.89706 | 2025-09-01 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c706b797-007d-34e9-90ad-060b69c7a84c | -12.55567 | -48.21901 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 05931149-b4bf-3b76-955f-150101eebf60 | -14.74182 | -46.74256 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b68bbc2-cd7f-3a33-8e98-816b7bba9492 | -12.86852 | -48.07713 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a68d1d1-cb8d-3517-8062-b2d62ac305b5 | -12.83136 | -48.07479 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e836554b-65b7-3f92-888d-c1ef23953e45 | -13.34484 | -47.04866 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6cfff16e-4266-3fd9-95fd-8ebc21c352fc | -12.96644 | -48.11081 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7e98e5a8-8819-39f8-b9a9-d301f1e0b38b | -18.1213 | -48.5331 | 2025-09-01 04:12:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0a0dfd70-5d28-3cad-a138-161cc1ddc725 | -13.33561 | -46.97179 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 33722fad-6b78-35e0-8e21-6ade2602201d | -15.6946 | -48.95914 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b71cd5d3-86d0-31b7-a1a2-9f99a4b1f8c2 | -13.69787 | -46.9099 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3eb402bd-8964-3a47-8b87-f802589c8dc9 | -15.58451 | -48.3406 | 2025-09-01 04:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| bd07d4e8-8bc9-39a0-b343-ce79c8ba30cf | -15.23842 | -53.795 | 2025-09-01 04:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d64de29a-1d0f-3ea2-afc4-9aecf592962d | -12.59852 | -48.20796 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d3aa33f7-a69f-3b86-a8c8-791adf0b6bd2 | -14.75422 | -46.75789 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4ff59963-5d65-39e1-af09-44b8b2d8a0e8 | -14.78718 | -46.74113 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3694514d-c972-3eb8-9f41-c1af3979ee75 | -13.36758 | -46.94205 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54157f76-9fe3-3321-83f4-cbfc327da612 | -15.29417 | -52.79098 | 2025-09-01 04:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3fd3995-e937-3c1f-84c4-282dad613f0d | -15.69387 | -48.9632 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6fa8941f-bf65-35e3-9bfb-57103cb550fe | -16.292 | -52.93503 | 2025-09-01 04:12:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff09357b-ddcd-3517-873a-8c52975f89a2 | -12.95162 | -48.10029 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README46.md)
