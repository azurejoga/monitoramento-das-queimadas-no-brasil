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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2298a112-b5a8-3f34-98e1-1f4562f2051f | -13.12872 | -47.88923 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 607cbab7-9a27-3f8d-9dd9-20e68701942f | -12.80848 | -46.86055 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4786f680-a814-3229-8f18-b7a06bb528b2 | -12.64766 | -46.99828 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8834c65-b76b-32a1-ae58-074012b88357 | -15.83576 | -42.62247 | 2025-10-03 04:34:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8dc7f241-e1a2-3821-8ed1-5f1af3ab2547 | -15.49946 | -44.36877 | 2025-10-03 04:34:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8017de6b-5394-31c3-a690-a8ca27e3a7e5 | -14.18856 | -46.68101 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 635c14f2-b1ed-3bb6-be6a-324b5d5e6dd9 | -14.59869 | -46.71902 | 2025-10-03 04:34:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42b392ad-1c83-30fe-ad90-d450bbe4d0ef | -12.19609 | -47.79254 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5434b662-590e-31ad-a3ac-fc0cce5bb5b1 | -18.16521 | -53.34292 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 68864fb6-c077-3a9b-abac-1e480a057c88 | -12.61635 | -47.00278 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c3d54f6-152a-3bb5-b918-c6bb11274e78 | -15.21261 | -47.64537 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a02f7699-6f0d-311c-84e1-4bb172386879 | -13.30606 | -47.60246 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ea8a2f7-984a-33e5-813d-67657f525e05 | -19.45533 | -48.92825 | 2025-10-03 04:34:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4cbc1569-bb3c-3ffd-a6db-9053cb280029 | -14.87116 | -48.33356 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2c6d24f-a9a1-36a4-a410-0b247d31b8ce | -14.72899 | -48.11417 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c90c3db7-82df-39ec-b9e8-fb637a064008 | -13.12592 | -47.88501 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aef0ef56-de66-3b3e-a9b9-8e5d1ca8b344 | -14.89805 | -48.33797 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7175e6d-f2f8-38c8-a02f-b0a0bf999839 | -13.66156 | -47.3031 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 425939ff-1c5a-32ee-9e27-006cc472613f | -18.28242 | -43.56936 | 2025-10-03 04:34:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d6a2cbf-2d1f-37a0-ab61-f985a92edc3d | -12.61402 | -46.97146 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a6cac66-d6b9-33a4-a038-1b08361a798a | -12.62516 | -46.9833 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| a50075ef-bcab-31aa-b114-6fc189907838 | -15.11768 | -48.49175 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e9debf9-0853-3ac0-8c2d-d5676aa65c89 | -13.96667 | -48.10965 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf281b07-cb8e-3652-9095-aa30197bd949 | -13.80394 | -48.05758 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00091978-b56e-3c1f-a970-98d4a52b2dfa | -13.36333 | -48.07824 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbc26dd1-5019-39a4-8e41-a7c2a6f25df0 | -15.57073 | -46.95355 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e357d852-fcd3-3e0c-b8be-89fc0d4150ef | -16.02095 | -50.85466 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1536d199-04c7-322f-ae54-ea60e9b0e821 | -15.24969 | -49.31371 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e7c92e9-81c9-33d2-adeb-e3a57f15d03d | -12.37606 | -46.51521 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 857d9a23-f56c-3955-831d-8880525723f1 | -14.30218 | -47.11406 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cde3533-9c63-369d-a693-7c07f68e7aa5 | -14.22911 | -46.10645 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f109ea23-c27b-3e82-8385-1050ad791916 | -12.62208 | -46.96485 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a77e9f4-935b-3106-8b6e-b7c2b1748a04 | -14.68611 | -48.10014 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c74b015-fc26-3800-8dd5-41b2566d8504 | -15.58644 | -49.06586 | 2025-10-03 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c9b85b0-869e-3018-91c3-6da6cd8c4d16 | -16.05785 | -51.04471 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd536a61-d73f-399b-bd41-aeabfdc2775c | -13.18968 | -47.8156 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5309555f-d34b-300d-ace9-53a7e717a630 | -12.6373 | -46.9967 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db5c0007-2fd5-30f5-82a2-4407bebddd00 | -15.19314 | -46.40408 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15537027-44b6-3162-b181-0086fb5f75fd | -12.1972 | -47.78521 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd9204d6-1022-3912-af97-d5b3719c24bf | -14.38092 | -48.47691 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2d59065f-4d75-3db2-a884-6f530e09a91f | -12.76088 | -44.89714 | 2025-10-03 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33ec8b5d-2e73-3be0-8760-af983f98a416 | -13.96451 | -48.15722 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c680c487-9e20-303e-899d-d019d23d142e | -18.66364 | -46.54236 | 2025-10-03 04:34:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 695faa4e-3670-34b5-b813-e69688d0dc25 | -18.27731 | -43.57383 | 2025-10-03 04:34:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a75d169-5b52-307f-9045-61a34e5aa464 | -13.30453 | -47.26183 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85577f0b-665b-3156-9461-66cc4c487590 | -18.15747 | -53.34553 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2126f34-20ac-35f0-a67d-8247a8d3b32f | -14.73175 | -48.09596 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06e24cb8-3aef-3aff-912a-856594c6c3ed | -15.23653 | -48.71662 | 2025-10-03 04:34:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 667e8e8f-986f-3273-bb2d-55e6ccebed94 | -14.87508 | -48.33043 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9e04c87-ad5b-37f3-b0f4-553b6dfb0e8c | -13.12423 | -47.87349 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea483d13-f382-3aac-b770-2f9d0a9fa63d | -13.7374 | -48.00915 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8b534c32-5a8e-38c3-911b-94408f1123f0 | -13.23837 | -47.3522 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ff66cf1-ba93-3ca8-8a6e-5cc75eee4683 | -15.22094 | -48.72898 | 2025-10-03 04:34:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc7872fc-00e4-3cef-ac2f-dab0352f54d0 | -14.40877 | -47.87447 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86b36a27-66c1-3f34-9e61-18864baedddf | -14.93805 | -46.91404 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c775c838-7d23-311c-a230-e14554c24f0a | -14.9014 | -46.96707 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 11de81ec-4cf4-339b-aac9-d28f5bad9faf | -15.27171 | -47.90524 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7616858d-7369-3a4b-a0cb-2bc1cf17ceab | -15.55701 | -49.27884 | 2025-10-03 04:34:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 200a5343-0fbb-3a91-9656-b3208bd5cee3 | -14.62224 | -48.24862 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21d33905-a914-3e47-adf7-bf15eccf01e9 | -17.16302 | -47.02375 | 2025-10-03 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1938d43b-8b97-3381-a02f-5cd53498b71e | -14.93863 | -46.88487 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c2a9709-62bf-3a73-9ccd-50b098324b68 | -13.28494 | -46.98912 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f52d451e-a078-3c6f-9b0a-fedfe74960ad | -13.75422 | -48.07964 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 09bf38c4-0777-3c63-8b04-a28ba5c9428b | -13.269 | -47.24068 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 51b52460-cd7a-36ec-9e69-eb93091d82ea | -14.21518 | -44.95986 | 2025-10-03 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6396d07-da92-3dc9-9163-4fb5d99f60c3 | -15.51955 | -46.80907 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eeda791d-8fe6-3893-9a6a-db5c1b7ea390 | -13.15258 | -47.83246 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c49651f-55e1-33db-bb25-d25c25f398d5 | -13.28841 | -46.98969 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb56e158-c003-3e57-b646-4d5b2cb0231f | -17.62696 | -44.44391 | 2025-10-03 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5aab6060-f234-32f1-b1fc-6dedb01cbcc2 | -12.84374 | -46.86245 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebc06bf7-9bf7-3dbc-a5bc-c9520491c321 | -14.94212 | -46.91088 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1577967e-9eda-3b75-90a7-a45b3062369c | -15.11609 | -46.68158 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 980997e5-7997-3b8f-95e4-efd4001ffa4d | -12.755 | -44.91108 | 2025-10-03 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b5fbf108-15b8-317c-9140-3f67659c6e4e | -13.68429 | -48.63902 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33f790d4-0f6c-30a0-af9e-033f90d41c37 | -14.59775 | -48.24108 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b650bc3d-7dc5-3b37-8d5f-ef3036cce94d | -13.12478 | -47.84733 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55d8d62e-fff2-3cd2-b6a4-5c12600d544e | -18.24845 | -53.32375 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4bd569a6-808e-3410-b5d9-76f34ee792d3 | -13.63498 | -48.67522 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35534710-196b-3b00-a1c5-da37ba568c81 | -17.16365 | -47.01942 | 2025-10-03 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d83f857-08d2-3d89-90a1-7e6d8ca7332e | -15.3451 | -47.83416 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3fe4997-ecba-3192-9dac-7b614cf60d4a | -18.23148 | -53.36055 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f925d3b2-c416-395a-aef8-95e8a8dd1959 | -15.2624 | -49.31945 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad581d3d-80cc-3c8d-8a6c-9fd2dd99ff13 | -13.68762 | -48.63957 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a221a87-935d-3f00-a7af-9eea6e42bc63 | -16.27472 | -47.1036 | 2025-10-03 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e763581c-77a8-34dd-861b-e17b5eb8609d | -12.92558 | -46.38294 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90ba9b6f-bb9f-378d-b7d2-edc1ee597711 | -12.60529 | -49.9048 | 2025-10-03 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c664dad-777f-3d62-ab30-cd43efeb2c57 | -20.08668 | -44.31436 | 2025-10-03 04:34:00 | NOAA-20 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2f17c5bc-99e3-345d-89df-ed2213219955 | -18.19992 | -53.31073 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39040f84-3596-3750-a4db-d1bb6d0ca625 | -13.76742 | -47.53395 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b5d35ab3-ba77-3783-8879-2ed00f6fcb14 | -14.46797 | -48.41545 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76ddef25-af96-37ae-ae86-ae3cf8f907db | -13.76757 | -47.57968 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ff938981-ced8-3331-a9ad-630c47230cf0 | -12.68177 | -48.5844 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43b5657f-6e93-370a-a636-acb5761820b5 | -13.13207 | -47.88984 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 5195220b-1ecd-3b2e-b628-d54988ad6b37 | -15.80647 | -46.25926 | 2025-10-03 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7d29331a-9357-3673-b595-c9fcfcf91f1a | -13.77545 | -47.55034 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13df2caf-8ca7-3afa-8d44-b325de2557a0 | -16.06178 | -51.04163 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 141810de-c8a1-30fe-825d-18ec9d017b29 | -15.75646 | -47.77501 | 2025-10-03 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 729b9189-3526-3ee6-931a-135ca9073fa1 | -15.3037 | -46.28504 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6c87510-e1c8-3a2a-82c0-0027546e0e40 | -17.25353 | -47.01781 | 2025-10-03 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 446e1e1a-8c95-3497-b91d-b6903e05dd4b | -14.89805 | -48.29273 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README123.md)
