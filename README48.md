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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d142d1b8-580c-322a-9f55-262403d09351 | -20.41179 | -46.40292 | 2025-09-01 04:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b9007eb-f446-3cf0-9d1f-702dbfcef2a7 | -21.08657 | -48.22382 | 2025-09-01 04:14:00 | NPP-375D | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3748604f-e334-35a1-820e-f0454abcf305 | -19.97215 | -50.21849 | 2025-09-01 04:14:00 | NPP-375D | INDIAPORÃ | SÃO PAULO | Brasil | 3520707 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 67a7b6ba-27d4-3ad7-afab-6551cde487ff | -19.63813 | -48.01062 | 2025-09-01 04:14:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1574635-2c1b-3a58-8c67-dbef2fd86061 | -19.09142 | -46.16601 | 2025-09-01 04:14:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31355224-c3e4-3246-80b2-e02f26cbab65 | -20.40305 | -46.41313 | 2025-09-01 04:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c6a6f33-6380-3b93-bbdd-88bcd10da7eb | -19.87227 | -44.95437 | 2025-09-01 04:14:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 54a30726-eb38-323b-9a90-87da711fb926 | -19.49294 | -46.58899 | 2025-09-01 04:14:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db7e43b7-0378-3822-9623-94de7d548f77 | -20.40989 | -46.41421 | 2025-09-01 04:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b944b05-9077-302f-b58e-8ab88ec28568 | -21.35547 | -49.05066 | 2025-09-01 04:14:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 7538805c-3f4b-3d77-b5b1-448a6e87e126 | -23.11175 | -46.61453 | 2025-09-01 04:14:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b4efb51d-6ee8-3222-91bc-a0ede730c22b | -22.25179 | -54.89056 | 2025-09-01 04:14:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7662132c-8de6-3373-99d4-497bd5dd39a3 | -24.14609 | -49.8352 | 2025-09-01 04:14:00 | NPP-375D | ARAPOTI | PARANÁ | Brasil | 4101606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 1fc41bf1-1a36-3242-905c-b4514c976bea | -21.08499 | -48.23267 | 2025-09-01 04:14:00 | NPP-375D | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ff864876-d58a-3724-919b-201e586f69c6 | -23.73275 | -54.94198 | 2025-09-01 04:14:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1fe9a052-4c9b-33fa-8545-f283b2aa3135 | -18.66367 | -52.59236 | 2025-09-01 04:14:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 243dc981-6b66-3cfe-9ff5-7f683daff6b7 | -19.69624 | -49.33284 | 2025-09-01 04:14:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5358e984-860e-36ea-84ed-fdaf5fd5e856 | -19.48192 | -46.5911 | 2025-09-01 04:14:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 360512e4-ee18-3f9f-a341-5db4b41fa481 | -19.49637 | -46.58968 | 2025-09-01 04:14:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 747f6032-8e6d-3148-b205-cb3a84c6487d | -21.35135 | -49.05268 | 2025-09-01 04:14:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| bf28efa4-d290-3d91-987a-b3d16f0a6bc2 | -22.25255 | -54.88717 | 2025-09-01 04:14:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c84cd401-b2f4-3b45-9291-f969ace1654e | -23.18917 | -45.748 | 2025-09-01 04:14:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d9e3f7bc-33ae-32cb-b0ff-36bbd330fc07 | -19.7205 | -45.25754 | 2025-09-01 04:14:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ecf65a06-500c-32df-9330-2f993ae3a3b5 | -23.35978 | -46.90851 | 2025-09-01 04:14:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 419a6d96-15fa-3766-a568-273f97cabf38 | -23.80485 | -48.14802 | 2025-09-01 04:14:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d5be04c6-e48e-396a-bacd-fb852227f81f | -22.91294 | -47.02682 | 2025-09-01 04:14:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 235dc6bd-ca5b-3a90-a5c6-019ce82966e9 | -19.85893 | -45.01638 | 2025-09-01 04:14:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55818294-c628-3ad4-9880-0e5a156df952 | -23.73777 | -54.94361 | 2025-09-01 04:14:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 353730d5-952a-30c1-bd4a-10464ec1e942 | -20.13602 | -44.97392 | 2025-09-01 04:14:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f19edb2a-35f5-39e6-b9b3-3d7a00b9158b | -20.40579 | -46.41766 | 2025-09-01 04:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9270aad5-d77b-34aa-bfbb-28434fab9fd1 | -23.44036 | -46.9488 | 2025-09-01 04:14:00 | NPP-375D | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 388b1114-15bc-34b9-8991-deda97eb62ed | -20.40647 | -46.41367 | 2025-09-01 04:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de75c182-43a5-3cbd-bfcb-68b9e9b77bfd | -23.80412 | -48.15215 | 2025-09-01 04:14:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 53bb8b2d-33e8-3137-8798-d9af62fc4429 | -19.93292 | -47.06503 | 2025-09-01 04:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcdf1e22-dfa8-3b00-a5b3-af8fe63ec06c | -21.87168 | -46.7499 | 2025-09-01 04:14:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 0781c480-28b5-3a07-8d1c-b626cd3f9769 | -19.4895 | -46.58831 | 2025-09-01 04:14:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f86e55c-9392-3275-bcee-de98a464d338 | -20.40236 | -46.41714 | 2025-09-01 04:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79603906-5493-33d6-8fa9-84740bb54bff | -22.34736 | -48.38047 | 2025-09-01 04:14:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 462edcc7-94f9-3c6e-95fa-d3f8da4877b6 | -23.80062 | -48.15145 | 2025-09-01 04:14:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cdd5f79e-eead-349c-b4b5-97c9ccda976c | -26.32244 | -52.70449 | 2025-09-01 04:17:00 | NPP-375D | VITORINO | PARANÁ | Brasil | 4128708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| da2dc74b-9b51-3362-8dad-93cf95c25fc7 | -29.80071 | -50.97295 | 2025-09-01 04:17:00 | NPP-375D | GRAVATAÍ | RIO GRANDE DO SUL | Brasil | 4309209 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| b10e6663-b6c6-367a-8330-4c6410ad2738 | -29.63917 | -50.92639 | 2025-09-01 04:17:00 | NPP-375D | ARARICÁ | RIO GRANDE DO SUL | Brasil | 4300877 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5d01ecc9-9b27-3e05-b9dd-11917e8a9394 | -29.7998 | -50.96923 | 2025-09-01 04:17:00 | NPP-375D | GRAVATAÍ | RIO GRANDE DO SUL | Brasil | 4309209 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c44994ce-e3dc-313b-a7c0-240e3cda02a9 | -29.06458 | -51.67148 | 2025-09-01 04:17:00 | NPP-375D | COTIPORÃ | RIO GRANDE DO SUL | Brasil | 4305959 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8a23d3e4-edef-324b-ad56-583c295234c8 | -26.32668 | -52.70545 | 2025-09-01 04:17:00 | NPP-375D | VITORINO | PARANÁ | Brasil | 4128708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| e1ee7c74-27d7-38e9-b278-dca0b63bd279 | -29.63826 | -50.93122 | 2025-09-01 04:17:00 | NPP-375D | ARARICÁ | RIO GRANDE DO SUL | Brasil | 4300877 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ed1e94e4-de11-3315-907f-e9c237bc8eb6 | -6.8281 | -52.8143 | 2025-09-01 04:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| b36c5ae1-073a-37c2-886b-6dfe02e0755e | -9.1165 | -65.5459 | 2025-09-01 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| bafaaf33-d401-3276-be71-2400450b3774 | -7.076 | -44.3376 | 2025-09-01 04:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 79c1ac2c-40b3-3bd5-852f-beabe0980374 | -7.6783 | -61.0908 | 2025-09-01 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 23ec236f-e2da-35f4-94a4-db3e6edeb021 | -7.0757 | -44.3606 | 2025-09-01 04:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| df6461ee-45bd-3326-98c3-3ce6124d95c8 | -7.0948 | -44.3358 | 2025-09-01 04:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 71907a80-dd6c-319d-94e0-2060a0605b78 | -7.0946 | -44.3589 | 2025-09-01 04:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 3006918f-cfaf-394e-a115-475b965dd62a | -9.135 | -65.5453 | 2025-09-01 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c8277d22-6b56-3b3d-a790-94c20a6157c4 | -1.54252 | -47.55911 | 2025-09-01 04:29:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07e03bd0-f273-3259-95df-9d01e5592601 | -3.42597 | -43.33342 | 2025-09-01 04:29:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f534868d-962e-3041-bf24-c980af0109ff | -2.6439 | -48.81205 | 2025-09-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ce4c540-1c6a-3626-b86a-ca263f05591a | -2.74305 | -42.78895 | 2025-09-01 04:29:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 625e7a3a-d7b3-346e-b659-e5b927bce9b6 | -2.4152 | -49.3476 | 2025-09-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84c4b037-d2e0-3d12-b9d1-1e756ece5436 | -2.34744 | -48.58303 | 2025-09-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a7fb5a1-64c8-3e2a-ba6c-f1430d64c0e3 | -2.26627 | -47.85811 | 2025-09-01 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03924ba1-bfa9-38c1-adbd-cf3ec47fac4b | -2.44061 | -49.36734 | 2025-09-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f552897-3a15-3bad-8660-8ec7ee26fd52 | -3.25436 | -45.20028 | 2025-09-01 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 266b8195-0e95-317c-8c56-961db3a88f35 | -2.41868 | -49.34814 | 2025-09-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7189ed0-846f-39fd-bbb3-d7740b0e473d | -2.45044 | -49.3603 | 2025-09-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3b45517c-d4f0-337c-a792-84c9b0bcafeb | -2.44982 | -49.36413 | 2025-09-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7cfd16b1-2cda-3f85-9721-08d1ad4db91d | -2.44287 | -49.36303 | 2025-09-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 82068004-a5d5-384c-9d25-1b293f1a9cca | -3.14789 | -43.87964 | 2025-09-01 04:29:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d86db5fc-4c78-342a-a428-86b25e854af8 | -2.44122 | -49.36351 | 2025-09-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58b3e579-51d3-34ad-903c-192ed617b566 | -3.60327 | -42.85441 | 2025-09-01 04:29:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b40f12b7-f550-3f2a-8068-4d0b908289e3 | -2.48216 | -49.38497 | 2025-09-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb7c4566-bdaa-30f0-a6d8-d46ae43557b3 | -2.44573 | -49.36741 | 2025-09-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 17715a4b-f496-380e-b7c2-98166793de9c | -2.44634 | -49.36358 | 2025-09-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9c9ff446-69df-36fb-badb-4d0be7179ffb | -3.42221 | -43.33282 | 2025-09-01 04:29:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2bc0cd8-d5b4-391c-bed8-5af1022869c5 | -2.40764 | -49.35032 | 2025-09-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5f3866e-c9a3-3b7e-bd49-4fd7a3cd2f17 | -2.34641 | -48.58315 | 2025-09-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 141547e1-b3f9-3f29-bb56-6279e370bb7d | -1.95429 | -48.11533 | 2025-09-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c059e410-dd49-3fb4-8aac-b36c431d9b8d | -3.25378 | -45.204 | 2025-09-01 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8af2553-8c11-3dee-a680-d2a47b655478 | -1.41765 | -48.38757 | 2025-09-01 04:29:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d52a65b6-5fa4-3174-bc89-eff624bdf976 | -2.43877 | -49.36631 | 2025-09-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c43bcfa0-b816-3f97-a2a5-5b315dc4f829 | -2.4158 | -49.34376 | 2025-09-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92ec5a3f-48e3-3b63-94d2-75409fce9c77 | -2.41459 | -49.35143 | 2025-09-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f1616e7-08d2-3dc6-a612-7891c8e72a95 | -2.34353 | -47.58536 | 2025-09-01 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c10e98f7-559a-3075-8069-2718cd1a1a2c | -2.41172 | -49.34705 | 2025-09-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0eade97-200c-38a9-81a0-9f99c4f08d6a | -2.34684 | -47.58588 | 2025-09-01 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 807fd5b5-4b42-3320-a02f-e26da797bae7 | -1.5392 | -47.55859 | 2025-09-01 04:29:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7bd302f-4d96-3b29-a6e6-69de0af7f47e | -3.16658 | -42.77395 | 2025-09-01 04:29:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f516abd7-38c8-3d0e-bb7e-54b9d78e056f | -2.41112 | -49.35088 | 2025-09-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bed1eab-5678-3baa-94b0-1cc88a7d5393 | -2.43939 | -49.36248 | 2025-09-01 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6a08a410-1665-3e1d-8233-aadb4e69aaed | -7.0757 | -44.3606 | 2025-09-01 04:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 87a1303e-04a6-3d40-836b-adef50ed01cf | -7.0948 | -44.3358 | 2025-09-01 04:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 165.5 |
| eac870c7-b7e4-3282-9a52-820ae87a49ff | -7.076 | -44.3376 | 2025-09-01 04:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 3b203f51-4549-3eae-8393-0f09a04b7865 | -7.0946 | -44.3589 | 2025-09-01 04:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 88371e7c-de14-37c6-8e20-71cc49c36a0b | -8.7684 | -61.4261 | 2025-09-01 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 8ffece80-28cf-3754-8ac9-4301aebd19f7 | -6.8281 | -52.8143 | 2025-09-01 04:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 69c86ddf-3202-3ec4-808a-368b7d280ed4 | -4.91145 | -43.18623 | 2025-09-01 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7620e52-f1d5-34cd-884a-7a6b2f9fb953 | -11.03203 | -45.14574 | 2025-09-01 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b6190dae-3b59-3e2a-b50e-a28a6a825da4 | -8.19695 | -46.78304 | 2025-09-01 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 081ee97c-b152-3b08-906f-e11647e2ba0e | -7.87244 | -46.95433 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 169f1107-2a1d-3682-ad69-c84da15b82f2 | -6.18596 | -43.34819 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README49.md)
