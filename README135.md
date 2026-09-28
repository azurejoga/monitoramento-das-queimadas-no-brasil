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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 148e6e95-d859-35bc-ab32-0209a6df50a2 | -15.09917 | -53.88877 | 2026-09-28 17:07:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 795e3f13-6405-3bd5-9532-044f0d5bf41c | -18.74068 | -48.1294 | 2026-09-28 17:07:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 140be062-7052-3d6e-aeac-a0d3b443f6a1 | -12.67374 | -46.98193 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d629d6c0-1abc-3293-8e6e-676007dc833b | -13.08894 | -47.44092 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 18e7d3eb-c148-38ec-8f80-008b292b9353 | -15.75789 | -42.28426 | 2026-09-28 17:07:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0e873d95-c915-3d08-9275-572a1b58d916 | -12.75542 | -47.35263 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e28ac16a-f5fb-35e9-b752-b203999abccb | -18.08115 | -44.53769 | 2026-09-28 17:07:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c74edf34-7912-34d2-8847-1df24e0a8232 | -13.16182 | -48.54848 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 68adcdcb-e67c-341a-881e-fba90f8a0aa0 | -17.81833 | -44.44294 | 2026-09-28 17:07:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5c636d95-03ed-36b0-83fc-98c3047c6eaa | -14.45906 | -41.60981 | 2026-09-28 17:07:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| cf3e8dfd-92b4-3762-b49f-d59a16eb87aa | -12.83032 | -49.67554 | 2026-09-28 17:07:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9f8d1830-19dc-3bf1-8020-2d998a51a632 | -13.48996 | -48.60197 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 38896db0-296b-3954-9583-807054c199c5 | -17.84221 | -52.22562 | 2026-09-28 17:07:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2aad58bb-6007-33f5-bd5a-d22b3dad5cb1 | -12.43723 | -48.22452 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 94f14641-286b-381f-abf6-4406095f1629 | -13.97056 | -54.01744 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0b16af06-8853-36b0-9dbf-71d51f4c7fd5 | -15.18927 | -46.12988 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b73205f0-3235-3d18-b8c9-e9b8bc8272cd | -17.94321 | -46.99988 | 2026-09-28 17:07:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| bc2a6ca7-e5d8-3ceb-97d3-85a0faa2b7fd | -14.64445 | -52.11772 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6bd51372-0e58-388f-b51c-22b0077b16f0 | -13.96821 | -40.45459 | 2026-09-28 17:07:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 8d81d804-8bde-3667-8402-41d5651091a4 | -15.00402 | -47.85983 | 2026-09-28 17:07:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8e10a856-b0c1-3955-8f9e-60d4adf655fc | -15.23637 | -48.56718 | 2026-09-28 17:07:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| edcf9ace-134a-34ad-9de7-4dd8e8056c33 | -13.31794 | -43.95261 | 2026-09-28 17:07:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 0256b3a9-bf9b-3cf1-b999-d68e3a4df925 | -18.21628 | -42.50877 | 2026-09-28 17:07:00 | NOAA-21 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 59b1c890-1184-300c-97ff-f86a239388ea | -17.67381 | -42.01148 | 2026-09-28 17:07:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| ce6c8e96-cb5e-3f39-8505-638f873be8dd | -13.36468 | -40.96803 | 2026-09-28 17:07:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 190b9ebd-008b-3c3b-979c-4c19412e00b3 | -13.47787 | -48.60747 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ce15aae7-dee3-3e51-ae4e-51497f645ef0 | -12.8515 | -51.00639 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e0e7daa5-6793-3385-a1f4-3188a8024d93 | -14.90554 | -41.1029 | 2026-09-28 17:07:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 67ad7699-ffc7-3500-8f3b-f2d138650c0a | -12.52014 | -49.9776 | 2026-09-28 17:07:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 9e1dabf9-d59f-330c-bc4f-103b8da6496b | -15.55282 | -47.92557 | 2026-09-28 17:07:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a1eb29f9-0aab-3c94-ab1d-eab8b718d326 | -13.4655 | -48.58414 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2839d5ea-fdc8-3634-b777-2e06fee6b154 | -15.27123 | -47.6257 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 593e0006-5667-3c2e-8603-7a587eb8235e | -12.87579 | -44.80151 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a6d14e01-6e11-3bc0-ada0-027c3e88e304 | -17.20203 | -42.20958 | 2026-09-28 17:07:00 | NOAA-21 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 30833631-4e41-3293-bf10-e94a497885d1 | -11.69156 | -43.48385 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| ea21d49c-dffa-32ba-a680-3d5891b0defd | -12.24115 | -42.0303 | 2026-09-28 17:07:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 16.0 |
| e4d6ae69-6e74-35f8-8432-ea16e1ec5583 | -14.66549 | -48.76227 | 2026-09-28 17:07:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 132f3a78-5795-3b90-8512-8cf48e2e463d | -11.89966 | -47.01691 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f04acf91-de9d-33f0-a4c1-49b035668ba2 | -13.71718 | -48.82895 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ae9aade8-5ea2-3e9c-a58b-5e696b025e5b | -20.8281 | -57.78796 | 2026-09-28 17:07:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 0aa10235-6953-38e7-ae73-595f44ff731d | -12.6202 | -47.28336 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 50bb9756-4a75-3ffd-8596-7fb4c54e228e | -12.43768 | -44.14853 | 2026-09-28 17:07:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 09767566-f14c-3951-9cfc-bbd2f3fc1818 | -15.73362 | -44.84329 | 2026-09-28 17:07:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ee66c2db-f611-3957-9413-24a1b7c8c8ba | -14.64108 | -52.11829 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 230592ce-fec8-3746-8865-bf9a5b58f1f8 | -12.10364 | -45.21711 | 2026-09-28 17:07:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 284db606-7bb6-313a-8d02-4c816bae41de | -12.64068 | -47.34517 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| b584a13b-b857-3363-b83b-96d067b4a2e3 | -15.6832 | -47.59635 | 2026-09-28 17:07:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5332f824-81cc-3b2d-a62a-86ab9c00b978 | -15.16838 | -43.57623 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 74345957-a67b-3f0b-8ef8-47a2340615f8 | -13.45391 | -48.58954 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d2d451a3-8068-3ec5-8bcd-8ac13d24eefa | -12.67347 | -47.34853 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 8c8de0ac-ade6-3f07-9876-cdeacdf46bdb | -17.33402 | -53.96215 | 2026-09-28 17:07:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 87af4aed-f917-3707-ab65-072665c27362 | -14.53239 | -48.31261 | 2026-09-28 17:07:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 26d049dc-e43f-325d-96b0-329dce229d30 | -14.35304 | -52.12111 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| e606f0af-35d9-38d3-9c68-17db2f309d82 | -16.24179 | -40.68277 | 2026-09-28 17:07:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 2550d3dc-3f7b-33bf-a137-51d593b0c991 | -14.63654 | -52.1115 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d00abfc3-c86b-36af-a65e-3ea450da6381 | -15.45634 | -41.44337 | 2026-09-28 17:07:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 49f59d5c-bb6b-371f-b59f-21b55fdf560b | -13.26617 | -47.44437 | 2026-09-28 17:07:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 111d5cd0-234b-3231-a9cb-438087e87793 | -15.45025 | -41.445 | 2026-09-28 17:07:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| f3535101-d08b-365c-a7b2-af01891ecf12 | -18.06333 | -41.43299 | 2026-09-28 17:07:00 | NOAA-21 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| c63f87f5-ae89-3f33-8660-6b74090f1a6d | -15.17261 | -46.14294 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a1c18ce3-bf59-36c7-aff0-01b6b72902ff | -15.19012 | -46.13445 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e06b7006-3c18-3e02-9ecc-a29cae1a12dd | -14.5884 | -41.23095 | 2026-09-28 17:07:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 7d966732-3bd4-3b0a-b601-01e358336536 | -14.69386 | -42.61843 | 2026-09-28 17:07:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e80c0374-43be-338f-b493-4b46bdef8016 | -18.21248 | -43.15729 | 2026-09-28 17:07:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4214d5ce-b68b-3b09-9f90-6f396d652113 | -16.79161 | -43.0093 | 2026-09-28 17:07:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ebd32994-177b-34fa-b84e-28e91d89d6f7 | -17.9481 | -47.00311 | 2026-09-28 17:07:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 84e143cf-7ddc-373c-9b90-84096a7c40bd | -15.02577 | -40.97276 | 2026-09-28 17:07:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 3675c683-623a-36d9-b413-50ddb584dfe6 | -13.26877 | -48.51303 | 2026-09-28 17:07:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b0116c84-a30e-311e-b2fc-3357b59dceeb | -11.903 | -47.00422 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 080e6a2d-6bbb-31f1-8da5-f59cee1dc0f6 | -18.09024 | -44.381 | 2026-09-28 17:07:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 75a004ef-87f7-3186-b94a-398aa6b758af | -14.71745 | -41.59427 | 2026-09-28 17:07:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 105.3 |
| a75b5672-103a-3f3b-91f6-bbeed06e9a05 | -11.64076 | -43.49913 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| bb5c184d-fb49-3728-84b6-2ea9150d75a8 | -19.00549 | -47.25533 | 2026-09-28 17:07:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1376830e-05d0-31ac-97aa-db0eda4d5868 | -15.342 | -48.12997 | 2026-09-28 17:07:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 21c4f587-aa08-372a-ab77-56283166c1b1 | -13.15409 | -48.54898 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9693bb59-fca2-3d8a-b950-1c405550e254 | -18.5311 | -41.89179 | 2026-09-28 17:07:00 | NOAA-21 | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| b18ad511-9ce9-3151-b03e-f918d5d02b86 | -14.48497 | -53.64664 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 28a0ee0e-25e6-35a1-ba3a-8556b50ca643 | -14.63272 | -40.712 | 2026-09-28 17:07:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 953007c0-d14c-3ffd-9a4d-87c7166341c9 | -16.68955 | -50.67043 | 2026-09-28 17:07:00 | NOAA-21 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2658226d-dd52-3012-b80a-4f159e2e2a49 | -11.71157 | -44.5232 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 92e8597d-67c3-37f9-9c2e-9c690a7dfda7 | -11.29843 | -43.56111 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 7f362ae6-1d29-3cfc-aaf8-632dde805c41 | -15.22918 | -46.19117 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1ee84be9-3e80-3930-a5b7-475fb7a22aaa | -13.15363 | -48.5498 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f19f3b46-2a65-322d-abcb-5e8b27f94286 | -13.48591 | -48.60268 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 58d9f16c-ca1a-3793-aa1d-45a5cdd9a841 | -15.22102 | -41.47645 | 2026-09-28 17:07:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 31ea398a-c79b-30b3-b695-881f23c14778 | -12.90867 | -52.07134 | 2026-09-28 17:07:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bef753ba-5a72-33e2-89ac-45c2690883b2 | -14.97843 | -41.53633 | 2026-09-28 17:07:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 248e1d65-e56d-3fac-85fc-b51d3ec5cdcb | -18.91121 | -46.94606 | 2026-09-28 17:07:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d6a8ede-c57b-300c-ac19-9a7c8fce9c9c | -17.94468 | -47.00786 | 2026-09-28 17:07:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a4940781-03d9-38f0-9614-644c783988fb | -15.66951 | -50.21931 | 2026-09-28 17:07:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03a91a90-ef91-361b-9a78-a458bcd8f51b | -12.96179 | -51.08164 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d0888a3f-c077-34b9-9c07-a860617fbed9 | -12.00541 | -44.95887 | 2026-09-28 17:07:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6df34798-f38d-3ab1-8f71-4c4a6f81672e | -16.98344 | -41.94609 | 2026-09-28 17:07:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 1a700c34-21ac-3d26-bdf8-f7e133fba10d | -12.90806 | -52.06758 | 2026-09-28 17:07:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 6cffde73-5c22-3ded-b2f4-7ab703e139eb | -12.00605 | -44.96223 | 2026-09-28 17:07:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| e545ac10-12a2-338c-b519-e50495a8d3f8 | -15.21928 | -46.19102 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1b490098-d274-3d5e-960d-1ac37bfcd39f | -15.72056 | -42.62588 | 2026-09-28 17:07:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 49e81ae3-f971-3406-9119-ec161c0c74d4 | -12.62905 | -41.87963 | 2026-09-28 17:07:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 9153e8fa-437f-3d8a-ba45-f820d07c86c1 | -12.67712 | -47.34323 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| dd6c6f68-f9cd-357a-aef0-550ab6aba6ff | -12.1024 | -45.21684 | 2026-09-28 17:07:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |


[Clique aqui para ver as próximas entradas](README136.md)
