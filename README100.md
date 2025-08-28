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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 378d5a0f-3df2-3424-acc6-9c51a46dbab1 | -10.4549 | -57.9576 | 2025-08-28 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| a4af0bed-3dcd-3a45-a1b5-4368c41f477b | -9.6794 | -47.0798 | 2025-08-28 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 0f84c4cf-42e6-3a29-a4e0-0ac81819c404 | -11.3517 | -43.566 | 2025-08-28 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| b3f2784b-6901-3272-afa7-863c54117f00 | -10.308 | -46.8068 | 2025-08-28 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| eac4aace-5781-3881-ad9d-830790f2df34 | -10.2743 | -64.4907 | 2025-08-28 14:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| b6095c2f-cf69-3d2e-ab92-efe6df138194 | -11.6127 | -47.2907 | 2025-08-28 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 5c956f9b-d866-3eb6-a04b-716a97511fbf | -6.4355 | -44.5764 | 2025-08-28 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 6ab45463-a283-3fe8-8361-1043799453d6 | -8.9479 | -65.9616 | 2025-08-28 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 0ff80a75-d540-33d1-b6c5-d278b84e4b48 | -13.3843 | -46.879 | 2025-08-28 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 80.6 |
| db95a154-4510-335e-b6fd-afa74514b56e | -13.8198 | -52.743 | 2025-08-28 14:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 1946b11a-3fb7-3c68-86ce-befdab7b1cbe | -8.8842 | -60.7507 | 2025-08-28 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| c04d4a2f-032d-36ac-b193-c6b343d87178 | -10.2743 | -64.4907 | 2025-08-28 14:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 308c052e-4779-3107-82ed-f85f7b1640ee | -8.4403 | -43.69 | 2025-08-28 14:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 6f7bbd5d-8aef-3b15-9511-5b56ca5e5a34 | -12.9963 | -56.9 | 2025-08-28 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| a670028f-70a4-3fac-a5ca-36012cd51392 | -5.8297 | -45.3051 | 2025-08-28 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 059959a6-f0e3-36b7-9996-58f75542aa26 | -7.3541 | -59.6669 | 2025-08-28 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 27e658f6-8eb9-3442-9aea-3a1cea5d0e43 | -7.925 | -42.6414 | 2025-08-28 14:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| 8ff269f7-aded-368d-92d0-fc0280543aaf | -6.4105 | -45.216 | 2025-08-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 7c380550-a74f-3b91-a771-558220834839 | -6.3883 | -45.5793 | 2025-08-28 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 70865e01-e76b-3df8-a2b4-3cc50cedd4d4 | -10.8049 | -60.7644 | 2025-08-28 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| aae85dc5-7291-35e7-aec5-9ee68edb4f90 | -9.7322 | -64.9067 | 2025-08-28 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| e964faf8-4b48-300b-8bb8-2b8093516da0 | -9.1363 | -65.2835 | 2025-08-28 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| ea543ccc-5b5a-302f-bf63-5eea6664fbd1 | -11.3325 | -43.5689 | 2025-08-28 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| eb644cbe-c5ae-341d-a962-7d74b57f264c | -9.6794 | -47.0798 | 2025-08-28 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 78c029cd-d4f9-3d00-a513-aa36661d0926 | -13.5571 | -46.9199 | 2025-08-28 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| b1204cb5-3116-3169-ae67-215912ea9e7a | -11.2378 | -55.0569 | 2025-08-28 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 49d4ab32-0d88-3f9c-8ef9-d1a75b24dbe3 | -12.6878 | -48.1677 | 2025-08-28 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 55cd6b10-afc8-3c04-8642-604c83f39b31 | -6.1783 | -44.0457 | 2025-08-28 14:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| df93d986-bd21-348f-b4cb-c925fba963be | -11.2189 | -55.0585 | 2025-08-28 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| b1faa0ef-a687-3211-96cb-5e0caac43c14 | -9.5842 | -45.7665 | 2025-08-28 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 6a497727-5060-3ccb-9804-5eb2c0616217 | -9.218 | -60.8497 | 2025-08-28 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 3ec5b42a-f21b-38fc-b0a0-edec26ca1941 | -14.3116 | -53.2501 | 2025-08-28 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f0305f04-4b25-3a95-b1cb-5c963b806a13 | -6.178 | -44.0688 | 2025-08-28 14:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| d38c47a1-74a5-3f80-a93f-73c9f4f45298 | -11.3526 | -43.5187 | 2025-08-28 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.8 |
| d5f0f59c-92a8-3e25-a539-4af2e6dcecb2 | -10.308 | -46.8068 | 2025-08-28 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 0dc5be1f-9be1-3913-bc9f-ff90177e4b49 | -8.8669 | -47.1658 | 2025-08-28 14:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 593de0db-1456-3d39-b885-9f58b04e8a2f | -7.3196 | -46.109 | 2025-08-28 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 8760745b-67cd-3614-9296-1a5b82322a2d | -7.1917 | -44.0732 | 2025-08-28 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 145.1 |
| a27317ee-02b3-39e0-aa0a-db90c2edfbb2 | -9.4372 | -48.2518 | 2025-08-28 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 7dabcbda-465c-3bca-acde-4afe8531c4ed | -11.3334 | -43.5216 | 2025-08-28 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 3a744c66-ec45-389e-9331-41b18e75e7f0 | -12.8032 | -48.1516 | 2025-08-28 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 002dc4db-d578-341f-b938-00d8cfa58697 | -10.4549 | -57.9576 | 2025-08-28 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| af034f73-8366-3b86-8482-36b6c6f7379e | -13.5382 | -46.9002 | 2025-08-28 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| de4f8805-5e63-3af0-ba8c-19e0ad6a92db | -7.9439 | -42.6393 | 2025-08-28 14:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 145.0 |
| 25aa5bcb-ebb6-3615-9351-93b82da81e0a | -11.6127 | -47.2907 | 2025-08-28 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 8aa7a9bc-99a6-3da2-aaa2-18c11254f445 | -10.4736 | -57.9563 | 2025-08-28 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 66962cdd-cdf8-36ec-b1d5-621d53d743e4 | -15.1906 | -53.811 | 2025-08-28 14:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 3ea67b5e-126d-3a5f-93d0-15c6b8018042 | -18.2025 | -45.5723 | 2025-08-28 14:30:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 3195ab47-6076-3499-b276-323451aadf5c | -8.9479 | -65.9616 | 2025-08-28 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 250358f4-0ad3-3c1b-9275-900dff17c3d8 | -9.5424 | -62.3823 | 2025-08-28 14:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| b456725d-5891-3627-ae41-6e6641aaae61 | -13.0154 | -56.8982 | 2025-08-28 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 1621d235-3b79-3fe0-b62e-e56589e2454d | -7.0569 | -44.3623 | 2025-08-28 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| a379963e-9066-32f7-b237-e0402f28a510 | -13.5576 | -46.8972 | 2025-08-28 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 199.0 |
| aa317665-1d82-376e-9152-170bf0453471 | -12.8224 | -48.1489 | 2025-08-28 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 188.2 |
| cc9d9c48-4636-394c-b17a-85f2f49c3e38 | -7.6222 | -42.6975 | 2025-08-28 14:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| adf56873-60d5-39ca-b4a7-75ab6c38ac5f | -10.8419 | -60.8202 | 2025-08-28 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 1a29b66c-a56f-3168-a634-777d1d01e372 | -6.1595 | -44.0472 | 2025-08-28 14:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 496825cf-37e8-34db-b9bb-36ce370c768d | -12.8228 | -48.1267 | 2025-08-28 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| a04c1774-cfc1-3d89-a203-4a1f6998ac7c | -12.8613 | -48.1213 | 2025-08-28 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 9aac16ea-3d3b-3af9-a5b4-e27e5165171b | -13.4208 | -46.9864 | 2025-08-28 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| eedcd9c3-9dd6-3a82-9d3d-261d501d6559 | -14.3309 | -53.2477 | 2025-08-28 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 417b0ff6-6da3-3170-a409-79fbfe2ab001 | -11.2375 | -55.0772 | 2025-08-28 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 2f7b1d47-b1a6-3730-a783-b1df9751d8bd | -9.4363 | -48.3174 | 2025-08-28 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 00eace40-ad73-3dde-ac88-4c557c7f3d63 | -7.6225 | -42.6738 | 2025-08-28 14:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 153.9 |
| 727eb9d9-4fe5-3225-acfd-3ed70f39d0a6 | -6.4355 | -44.5764 | 2025-08-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 164.2 |
| b2c5fcee-409f-3323-8ef2-1ffacb8e0ac8 | -8.8919 | -62.4487 | 2025-08-28 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 3da61f9c-5fc0-33b5-82dc-b1df433a7ca7 | -9.5846 | -45.7438 | 2025-08-28 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| a8929da8-ce49-3434-a1f6-c407208d974f | -13.8006 | -52.7454 | 2025-08-28 14:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 3bf49bb0-eacc-39ed-84dd-873709ddfd8c | -8.2455 | -47.2263 | 2025-08-28 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| ed04d817-603e-3b09-837a-b0f4edc7ceaa | -10.4738 | -57.9366 | 2025-08-28 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| bcebcd03-1390-39b7-bb71-5eb87c5ca70e | -6.6759 | -58.846 | 2025-08-28 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| bd00e812-8f00-3e0f-94e3-7455b965e664 | -9.6797 | -47.0576 | 2025-08-28 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| daac8655-226e-3c02-81bf-5e7edc05a522 | -6.0627 | -44.3769 | 2025-08-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| f19490f3-2b82-38a9-9b55-41c4b0645df0 | -10.8421 | -60.8009 | 2025-08-28 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| c4434040-6eaf-35b4-a001-e95fdf61308f | -7.3193 | -46.1314 | 2025-08-28 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| cd0a39ef-fcd7-3b28-8ea1-cf3cf0ed01ac | -12.9961 | -56.9201 | 2025-08-28 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| ef207066-5457-3426-8fcc-7317bce751ea | -6.4293 | -45.2145 | 2025-08-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| e0ddfbd1-a435-3e39-8205-86f5b8128ec2 | -4.8751 | -43.1661 | 2025-08-28 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 3480fe32-1ded-3403-b08d-bfb7b2b1ce36 | -6.4357 | -44.5535 | 2025-08-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| f21c8adc-6378-349b-abda-286024fbbcde | -13.0151 | -56.9184 | 2025-08-28 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 177.2 |
| 3e6f4418-3216-3159-85ac-857bd5b61f4d | -11.3669 | -63.2663 | 2025-08-28 14:30:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| dc1916ad-6d73-39a2-a31d-1d19222a1894 | -11.1017 | -44.7476 | 2025-08-28 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 7f45453d-133c-3aa8-992d-5c927d7dba1b | -9.4369 | -48.2737 | 2025-08-28 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 2222ef2c-c66e-39d5-843e-84d050d0103d | -8.4407 | -43.6666 | 2025-08-28 14:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 286.3 |
| c3940950-1fa4-3945-a128-7ab870288d2f | -6.1372 | -44.417 | 2025-08-28 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 3285ac60-e49e-310a-9434-e28b2f59c6fa | -13.4204 | -47.009 | 2025-08-28 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| cf8f1b48-0031-322c-861f-ed4e5c0a8a80 | -8.4596 | -43.6645 | 2025-08-28 14:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 0a704de0-839d-382e-a955-ceb4a99d199b | -5.8295 | -45.3277 | 2025-08-28 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 2d65ae9c-0481-355c-b12b-9c7cc9f7649a | -13.5378 | -46.9229 | 2025-08-28 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 1c7022c9-50b5-311e-a693-f3782b743835 | -7.3357 | -59.6484 | 2025-08-28 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 39722f92-9d14-3543-936d-1a0ae2d7e2a5 | -7.6414 | -42.6718 | 2025-08-28 14:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 132.2 |
| 1f497e5e-2100-321f-8032-c5a08e39df6c | -8.7325 | -47.3783 | 2025-08-28 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 2be05d20-057f-3e76-b671-fcee42f5a371 | -13.0863 | -46.3352 | 2025-08-28 14:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 3bc141e3-d06a-31b4-9164-abe27cc79f23 | -11.3517 | -43.566 | 2025-08-28 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| fef94e6e-c32c-3700-afbd-eca6d7e32d96 | -9.6816 | -48.3139 | 2025-08-28 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| a50661de-f8b4-3113-83ed-299452c401ac | -8.7322 | -47.4003 | 2025-08-28 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| e9a75c4d-b6f2-37fb-9144-47f95062b592 | -6.3881 | -45.6018 | 2025-08-28 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 49c6e489-82e7-3295-9962-9f81c60b4b93 | -7.9442 | -42.6156 | 2025-08-28 14:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 142.1 |
| 82ea3813-e60c-318e-9d24-4f64b2ff5a49 | -9.6574 | -64.9845 | 2025-08-28 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.4 |
| a921356a-efa7-3a90-ae16-523e9d02c9e4 | -8.4599 | -43.6411 | 2025-08-28 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |


[Clique aqui para ver as próximas entradas](README101.md)
