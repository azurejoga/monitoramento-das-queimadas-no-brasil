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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de151933-3c13-3c6d-b15f-489cf20fd5bb | -11.3513 | -43.5897 | 2025-08-29 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 8b49c70d-7411-3e5e-a744-627b94fdbce3 | -13.558 | -46.8745 | 2025-08-29 12:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 24f53612-ebfa-34c0-a086-c57a5fea1b4f | -6.4105 | -45.216 | 2025-08-29 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 84b09914-6f74-393e-bd5c-81afdf71c16e | -13.3543 | -54.38 | 2025-08-29 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 6bf043fa-d84a-33b8-95ef-b755b7744435 | -13.558 | -46.8745 | 2025-08-29 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 189.1 |
| d7b691cc-6d06-3c3b-9159-ff645da26327 | -12.8994 | -48.1381 | 2025-08-29 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 6c3e5096-5002-30b0-846b-9499b478b0f8 | -13.354 | -54.4006 | 2025-08-29 12:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 46c937da-180f-364f-9f66-d0b637ad3610 | -11.553 | -46.287 | 2025-08-29 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| cdfcbed4-ef5b-3df9-a3db-11d1818d0c0d | -11.3325 | -43.5689 | 2025-08-29 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| abb8ab75-e1aa-3f57-a494-efee611a0015 | -11.5722 | -46.2844 | 2025-08-29 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 206.0 |
| 34bb177c-8b9a-3baf-98b3-6786915ae980 | -13.5576 | -46.8972 | 2025-08-29 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 0132146d-5c9f-34a1-a752-621d0b279be4 | -11.3521 | -43.5423 | 2025-08-29 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 9bb89b68-293f-3835-9662-034516a080b6 | -9.5447 | -45.8842 | 2025-08-29 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 388.7 |
| 5a51cad5-8022-3e66-a6b2-ecacd2601a4a | -9.5637 | -45.882 | 2025-08-29 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 98bf9c26-1e13-3cca-9553-039acaffd3b6 | -11.5714 | -46.3298 | 2025-08-29 12:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 6a7a6545-272d-39a8-b0f0-a4bc909fd039 | -10.9525 | -46.8841 | 2025-08-29 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| a478b8a6-f76c-3916-b6a3-7678952828e2 | -10.848 | -47.4991 | 2025-08-29 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 156.7 |
| e7ffb092-8eee-362e-93de-93b665bfa8a7 | -13.5774 | -46.8714 | 2025-08-29 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 103.9 |
| ddbfb56b-f43f-3179-b8c5-7f3d1cc572dc | -9.545 | -45.8616 | 2025-08-29 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 6114528c-b5a7-310a-b6b0-cdb9c96f2813 | -12.9182 | -48.1576 | 2025-08-29 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 7f4533ae-330f-36a4-903c-f38ad966af25 | -11.5527 | -46.3097 | 2025-08-29 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 202.3 |
| e1b18717-dd70-396d-8911-3f39f487ff71 | -12.9186 | -48.1354 | 2025-08-29 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 1d7f3a2e-b525-3e1b-8a85-79f51c0082cf | -7.1106 | -44.6099 | 2025-08-29 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 43a10ad4-369a-3c47-b083-9f8b511ddcba | -10.8483 | -47.4768 | 2025-08-29 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 183.1 |
| e20fd949-20a1-3867-a817-2dba4cf2ea08 | -11.3517 | -43.566 | 2025-08-29 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 340.1 |
| 5b1b2554-0f8f-3ad7-9e6c-6942d5462e2b | -11.3513 | -43.5897 | 2025-08-29 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 1bc016d0-3982-3396-8b81-3647c3aaf24f | -14.3306 | -53.2688 | 2025-08-29 12:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| ee7ef9f1-dba8-3551-ab13-1abc5223524c | -9.545 | -45.8616 | 2025-08-29 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 176c2946-a038-3eff-b46c-ac3d2f38c064 | -15.0835 | -48.1367 | 2025-08-29 12:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 113.9 |
| b8f7a503-a26c-3610-978e-5d73468ab3e1 | -11.3513 | -43.5897 | 2025-08-29 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d538b3b9-bae1-34be-8369-a088e8b65966 | -11.3325 | -43.5689 | 2025-08-29 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 04c3e6d7-ae3a-303b-aed1-0b7631fcb7c4 | -9.5447 | -45.8842 | 2025-08-29 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 348.0 |
| db2a3e7b-ab34-37f7-ba96-44d791ab8b82 | -12.9379 | -48.1326 | 2025-08-29 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| ad858df1-421c-31ba-8dd8-438639416079 | -12.9182 | -48.1576 | 2025-08-29 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 199.9 |
| 1e86a3cb-b889-31f6-9302-0dde6c325a84 | -13.5774 | -46.8714 | 2025-08-29 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| a9c4dc64-677b-37ee-9253-fa669e1f2745 | -11.553 | -46.287 | 2025-08-29 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 751aa54e-18d4-3bd6-8770-69123c3afc31 | -12.8413 | -48.1685 | 2025-08-29 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 6ab5cb2c-8e8a-33b6-b625-612d483fab32 | -13.558 | -46.8745 | 2025-08-29 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 100.3 |
| a85f8d56-aa4c-3604-8695-6dde78315ecc | -11.5714 | -46.3298 | 2025-08-29 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| e25820ca-6d67-3460-8e28-c9a6487dc134 | -11.3517 | -43.566 | 2025-08-29 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 308.6 |
| bc56af77-7749-394e-bc15-27abe4b0931a | -11.3521 | -43.5423 | 2025-08-29 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 8a4c6cdb-03d0-39e8-b47f-1a145b40b60c | -12.8994 | -48.1381 | 2025-08-29 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 1b03cbb5-ba94-32d4-ab68-e2c110019426 | -12.0362 | -50.6448 | 2025-08-29 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| ca92108d-e6c6-3975-9614-59bc085fbc72 | -13.354 | -54.4006 | 2025-08-29 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| aada1f9c-fc56-3749-baae-7a33112d6589 | -12.9186 | -48.1354 | 2025-08-29 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 198.9 |
| 35a5d8f7-421d-3c78-a8db-131a49a1f103 | -6.3883 | -45.5793 | 2025-08-29 12:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| c43ab77b-f472-387c-87f5-c282bd66638a | -8.7511 | -47.3985 | 2025-08-29 12:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 931de8e9-61b3-3e40-9d41-c50d74d869c9 | -10.8483 | -47.4768 | 2025-08-29 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 9b8e2fdf-6d56-330d-aedc-7787d775dff7 | -11.876 | -46.4007 | 2025-08-29 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 881db41e-4d3f-36f5-8852-98096542d319 | -11.5722 | -46.2844 | 2025-08-29 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 238.4 |
| 342fe19f-358c-3bd5-aad8-f84dcae5692a | -10.848 | -47.4991 | 2025-08-29 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| c8152069-a935-34d3-9e54-bd10106f2b1c | -11.5527 | -46.3097 | 2025-08-29 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 476.5 |
| 0ce165c8-eab4-3817-8357-9f1e4ad94a59 | -9.5637 | -45.882 | 2025-08-29 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| bd3cad7a-1e54-31a6-9b29-41f6be2352ce | -7.1106 | -44.6099 | 2025-08-29 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 777c8ed8-4b9b-364c-a17e-28729c40d15f | -14.3502 | -53.2453 | 2025-08-29 12:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| d4b7b65c-5279-3bd8-bd65-4e3bb57a4908 | -13.558 | -46.8745 | 2025-08-29 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 112.2 |
| edb22dd8-3a52-3011-84b9-14f66be2525a | -12.8413 | -48.1685 | 2025-08-29 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| f70ead52-de61-3a2c-8a42-8ddfa06e9b51 | -11.876 | -46.4007 | 2025-08-29 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 1669c083-ca22-3785-b3f8-ca27a7261a9d | -11.3517 | -43.566 | 2025-08-29 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 229.0 |
| 9305825c-e0c8-3d0f-adcc-e033d1781fce | -11.3521 | -43.5423 | 2025-08-29 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 4afd91f5-3eab-3b05-bc1d-ad3a90c06010 | -11.5722 | -46.2844 | 2025-08-29 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 174.2 |
| a5f407d9-d553-378c-be1b-a6fb7f683592 | -12.9186 | -48.1354 | 2025-08-29 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 5aa21bda-cc0d-315a-a3b6-3c9cdf5d9461 | -13.3543 | -54.38 | 2025-08-29 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 1327f938-bbc8-36c1-b436-b1ec731d0769 | -12.9182 | -48.1576 | 2025-08-29 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 80a42fe9-f9dd-3f4a-976d-59d483919892 | -10.3812 | -57.8245 | 2025-08-29 12:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 5c30d68b-907e-3d98-9d2f-9414586d26c6 | -13.354 | -54.4006 | 2025-08-29 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| b85aa4d0-da3c-303f-9c77-eb3733f5be63 | -14.2949 | -51.9422 | 2025-08-29 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| cf19ea15-ee33-3bd9-bf05-4ee59123df86 | -15.0839 | -48.1142 | 2025-08-29 12:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 13b06841-8027-3dde-8478-749099b1aa21 | -7.1106 | -44.6099 | 2025-08-29 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 5d3b396a-31db-3c32-8031-f3c8927f4e0c | -11.8756 | -46.4234 | 2025-08-29 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 1ab38b19-e139-38eb-9e62-4309cc2ea4e4 | -13.5774 | -46.8714 | 2025-08-29 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 0d12643d-0850-3a16-b2a1-2b91d490e04a | -11.5527 | -46.3097 | 2025-08-29 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 250.7 |
| 958a40fc-1f93-3c73-bf85-9c7c08b27fe7 | -14.3306 | -53.2688 | 2025-08-29 12:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 134.5 |
| ad46a0e1-afbd-34a0-9961-8f5c04fa218a | -15.0835 | -48.1367 | 2025-08-29 12:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 313a1669-eaaa-3c98-b575-ed1e0d55ba2c | -12.8994 | -48.1381 | 2025-08-29 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 7dae0e91-c71d-3985-9e15-69cbb93e5214 | -8.0647 | -45.0446 | 2025-08-29 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 91acb34d-052d-3a15-8ce6-c045b48e8534 | -11.5722 | -46.2844 | 2025-08-29 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 3c9d25d5-7989-37f0-849f-f9065e3bd3fc | -7.1106 | -44.6099 | 2025-08-29 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| ee109ac5-aed7-3876-8974-3c2ec20d62bb | -12.9318 | -46.359 | 2025-08-29 13:00:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 2b647657-0750-3625-bd0e-0003e68cc9b7 | -11.5527 | -46.3097 | 2025-08-29 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 232.1 |
| 89b78c93-0e1a-378f-a230-9bb9692e1130 | -14.3343 | -51.8944 | 2025-08-29 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 9d468e3c-abae-35ab-be73-a7a60e5c1f53 | -14.3532 | -51.9132 | 2025-08-29 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| f46f1b31-82f5-36b8-baca-2e50e419a7f9 | -10.848 | -47.4991 | 2025-08-29 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 62bdf1f3-e78c-375f-82a5-7abc7b00cab6 | -15.5783 | -43.5436 | 2025-08-29 13:00:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 10e1a19f-bc04-3cac-a067-c759965a4b75 | -12.9186 | -48.1354 | 2025-08-29 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 0e446e45-3e6b-3919-a057-78d8517556cd | -6.3881 | -45.6018 | 2025-08-29 13:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 49c9235f-37ae-3732-b60e-000f5e42e975 | -14.3339 | -51.9157 | 2025-08-29 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| d8c3a6bd-fcda-3be2-83d2-a9f72edf996a | -9.462 | -60.549 | 2025-08-29 13:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 308.3 |
| 2b1b3060-ca25-3546-8b84-830b6753de9a | -11.3713 | -43.5394 | 2025-08-29 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 3adcd45b-14a3-38b9-9a50-49f869a8dd38 | -9.5637 | -45.882 | 2025-08-29 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 815.5 |
| a5fe5e37-bc32-3c35-bb96-b3b3e2f0dfe8 | -11.8756 | -46.4234 | 2025-08-29 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 018395bf-64c0-3c27-acfe-7c9c867301f3 | -9.4432 | -60.5692 | 2025-08-29 13:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| a7232c5b-ddbb-3a13-8f78-b239a04c0034 | -12.8994 | -48.1381 | 2025-08-29 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 86726402-212c-36b2-a4db-39aca76f403b | -9.4433 | -60.5499 | 2025-08-29 13:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 261.1 |
| 69f42a1c-630b-3de9-a4e4-35ce1d6320e0 | -12.9182 | -48.1576 | 2025-08-29 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| a20a3237-9ce7-3654-b490-e78dede984dc | -15.1225 | -48.1302 | 2025-08-29 13:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| bf861e11-9c0b-32f8-8522-ed911692d6fc | -11.3521 | -43.5423 | 2025-08-29 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 233.3 |
| 203db355-9576-3d37-a660-c6ebd5c4104f | -9.5447 | -45.8842 | 2025-08-29 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 509.5 |
| d5c82470-405c-3bab-a0d7-b38fd953e643 | -9.4618 | -60.5682 | 2025-08-29 13:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| d95be722-5dfe-3358-9d40-24af4c931a6b | -11.3517 | -43.566 | 2025-08-29 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 209.4 |


[Clique aqui para ver as próximas entradas](README94.md)
