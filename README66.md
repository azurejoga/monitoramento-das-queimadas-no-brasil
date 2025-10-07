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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a324ab2-df50-3477-a662-322cd8b253b7 | -10.08709 | -50.52225 | 2025-10-07 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4dd09674-a118-305b-a5a2-222bb14efff9 | -16.20094 | -43.6574 | 2025-10-07 04:38:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54b1db66-443e-345c-9414-8ece23e44afe | -15.49711 | -46.83514 | 2025-10-07 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b05bc80-092f-3916-80f9-8f7a6416088c | -15.59214 | -42.36171 | 2025-10-07 04:38:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d25a9ef-75fe-3034-b76b-5911db52fb03 | -10.4355 | -50.33561 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0ad0740-989b-30af-94db-968ea864e1c9 | -14.77433 | -46.07476 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 276f452e-5e65-3237-8ee6-277cd1a4ef5c | -14.66887 | -48.39359 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c84e0145-71b3-375b-8f0f-2456a2412922 | -10.41878 | -48.09832 | 2025-10-07 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd8e9930-dc93-336d-93d9-642d1519243d | -11.1002 | -47.20019 | 2025-10-07 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f76b859-2f85-32e3-b0c1-f018115927a7 | -12.21097 | -44.25495 | 2025-10-07 04:38:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cec723d-fadc-3f75-b1d8-213ba915b62c | -13.93827 | -43.73896 | 2025-10-07 04:38:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4306026-6b9a-3ed9-b770-1d7ead9644b6 | -10.5312 | -58.03455 | 2025-10-07 04:38:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be283750-6f31-3e8b-95a7-6e558adba94b | -10.84478 | -47.86505 | 2025-10-07 04:38:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52175c14-f977-3303-83d5-0673dda25c19 | -14.70466 | -48.38791 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7706fa03-fcc4-3ceb-8370-b192fae4fe30 | -12.90302 | -54.74481 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cdf6fc5d-55d9-3106-9a59-76f5b6fc1c3d | -10.99849 | -57.05629 | 2025-10-07 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21183738-5b48-32a8-bd87-3d5b04b7ef6d | -10.74587 | -49.71239 | 2025-10-07 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 949c137e-27f4-32d5-a8d9-dea01df45b24 | -14.91163 | -46.82749 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3e2eb77e-ae33-3e9a-90c5-03d7349ad6bc | -17.98818 | -45.00011 | 2025-10-07 04:38:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8352aaee-f17d-30c5-ae57-6a8dd3538818 | -12.25897 | -51.34298 | 2025-10-07 04:38:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e64fe2a-cb0f-3f9c-a2c2-82b4732f1f70 | -15.17055 | -52.76392 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea867212-da0a-345f-a8d3-17a89e467d27 | -10.79773 | -48.59564 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed460c41-ca1f-3574-a5ab-b9befa9e7c5b | -10.4305 | -50.32347 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 41f37539-1629-36bb-9f14-f57994235d32 | -14.24877 | -54.24697 | 2025-10-07 04:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55224f7d-1a72-38ac-b57e-ee082b52a1f0 | -17.71974 | -40.23829 | 2025-10-07 04:38:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cf50dd60-0f73-308a-8753-93b7688db9cd | -13.09937 | -48.01019 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f82e375-6f3f-3f21-abe6-ba4f6e0a7ee8 | -13.65581 | -47.28355 | 2025-10-07 04:38:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ac6eddf-f392-39fb-ab28-70dea8fd2fa1 | -16.0203 | -51.05575 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ef657d6-095d-3158-846f-f4ee42eb76ab | -13.72813 | -48.20591 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d33c2be-74e4-32ec-b78c-01af79b5f866 | -11.68076 | -46.34417 | 2025-10-07 04:38:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1c64b1a-6be9-3417-a3a4-ad088d4d50b7 | -11.71513 | -45.44457 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ef674ad-bf90-368d-af87-1ea19c2d40ea | -13.06864 | -47.89239 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 771f938b-9a52-326f-97a1-23e8d2310058 | -10.09051 | -50.52282 | 2025-10-07 04:38:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e6c8c5c-17c7-3822-bae7-fb8a58743dc6 | -10.81383 | -48.60182 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a8436021-3bb3-3c86-837c-8d592d7b9202 | -13.36617 | -50.46363 | 2025-10-07 04:38:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 063abdd2-98aa-38fb-b88b-bf40ff0ed9d6 | -16.18204 | -43.42754 | 2025-10-07 04:38:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74b9c7a5-ca45-3d1e-8e37-68ce391e08f7 | -14.93227 | -51.42512 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f7be85c-63a2-3bcf-96a5-ed585c1ccf38 | -16.29078 | -50.9786 | 2025-10-07 04:38:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0125e75f-3168-38c7-b727-001b2d34e207 | -14.93371 | -46.80164 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| abc7a011-bb37-327a-a10b-9176f31f3a4f | -13.09031 | -48.0013 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7453112f-4a38-3bdf-bf78-5a5f20a17603 | -14.66268 | -48.38873 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 385cd08d-9697-3523-a6c1-fd854cac1f54 | -15.58404 | -52.56641 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6888a6be-6772-377e-9fe3-5ab4f3893b8d | -11.7466 | -51.49739 | 2025-10-07 04:38:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e4a8063-20ff-311c-8384-0a8bdad37c9f | -16.00074 | -50.82831 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 127222d7-3b2c-3fdd-9013-f76ed3bc7a8a | -13.26767 | -47.19099 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c268cfd-93d0-3d49-a4f8-09be14fe128c | -15.99755 | -50.95468 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30397624-e10d-3f7f-8f88-8ec3fd466155 | -14.93435 | -46.79713 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dff7c7ba-ab1f-36fd-94c9-04c269f8ae10 | -14.98742 | -49.96786 | 2025-10-07 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35677239-32bb-3657-8d00-cc3cbdc9d2da | -15.23397 | -56.75994 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b68fc031-e3a3-316d-98d8-d4c2ee390412 | -16.02059 | -50.96937 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a92f58c5-2585-3a11-95e4-f04aecee755e | -12.16815 | -50.91227 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67b10f64-0169-30fe-b00e-19b373794b3c | -12.38133 | -51.1059 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39d444d7-28a6-3b52-b27f-8a7a0e0e3f3d | -15.59646 | -47.26979 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1c266f2-2561-3971-8894-e4476c17a1a7 | -13.26478 | -48.48456 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f8518ed-1e0c-3518-a765-4da70ec01010 | -11.15858 | -54.88171 | 2025-10-07 04:38:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83be196c-a69b-35b2-a8a7-474a83798445 | -14.73347 | -46.01264 | 2025-10-07 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8b463b3a-276c-312b-9ad3-a6cb63460a8e | -14.75454 | -46.05302 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2957695-c922-399d-b126-c4b01f7c8503 | -13.3405 | -47.18106 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5069b25e-a4bd-3af6-b47f-80b3549df4fe | -15.2943 | -46.33416 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efaf5f47-05e0-3b0d-b0a7-2ba80a17397f | -13.10277 | -48.01072 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44998114-6b7c-30f5-bbe7-4789dc8a494a | -14.93509 | -51.47186 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88098afd-20fe-31e2-9a3b-41af3dfa5f74 | -14.62503 | -43.88836 | 2025-10-07 04:38:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4fcc3a6a-37fb-3cb1-801e-01e1ca5de871 | -11.74175 | -54.71823 | 2025-10-07 04:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6077ce8f-0c99-3986-94f4-ff26ea2949b9 | -11.80775 | -45.04415 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87a21420-2309-3aa4-8a73-acc3c85be757 | -12.92875 | -54.71917 | 2025-10-07 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 647c008a-040d-3112-b187-780b7478ed3c | -13.51065 | -48.627 | 2025-10-07 04:38:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70f79f77-99fe-39de-aa2f-3b07c25f6e2b | -13.27719 | -48.05621 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a40ddc03-dc1a-3fca-9002-9b8819e09c8c | -10.59168 | -51.60503 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60b9d840-763c-312d-a5ae-a66f9f970b5c | -13.25049 | -47.7983 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6eac89a7-99f1-3345-b3e6-e73f2b4712f2 | -18.525 | -43.42321 | 2025-10-07 04:38:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bfa43299-9266-3d2b-8bc9-edbe6c6057a6 | -11.75095 | -51.51441 | 2025-10-07 04:38:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb3e7f09-6d3c-3d10-ad7a-f43f996ebbc8 | -11.12589 | -47.21572 | 2025-10-07 04:38:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ab5ce21-61c1-3937-92c4-7cf31b14f6c8 | -10.91749 | -47.07267 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afe17cb2-bcc9-357b-b282-c18254e6dc38 | -13.28506 | -47.57136 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c372fedf-12ce-3dcf-abe1-3a88dd41d4d7 | -8.23264 | -61.17408 | 2025-10-07 04:38:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1098644b-37ce-3043-8dd5-ec9e609648f8 | -15.03392 | -56.02921 | 2025-10-07 04:38:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b027b5fa-a735-393c-8cd4-14b9ec373b9c | -12.38161 | -51.08272 | 2025-10-07 04:38:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39819c76-9f8e-3d55-8f7c-88ed6cf4eda6 | -14.64914 | -48.36366 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18b45e5a-8b95-31e7-a2dc-6cdd93b28908 | -15.62741 | -52.54496 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 928d3717-a360-34ca-94b4-75825274983a | -13.26615 | -47.58002 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca33dbb7-e41c-3cf6-94eb-c0f2a0a05225 | -11.6778 | -46.33958 | 2025-10-07 04:38:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6e0c8eb-e1ab-3571-8c69-cde142b63619 | -15.02325 | -47.55184 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| de445ff9-0d02-37a8-8a0a-4fcbaca2ea20 | -15.16839 | -52.77637 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04243a5d-96c3-3b86-860e-77fc23129ca8 | -18.28465 | -45.45496 | 2025-10-07 04:38:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2eb85b35-bc53-3598-9b28-8f1f32a2e5e1 | -15.18927 | -56.82278 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dec27d2a-32ad-3636-b9e0-8723228cac98 | -10.45757 | -50.41485 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a55a912c-1f6f-35b5-8e1e-33f49addae59 | -11.95503 | -45.48591 | 2025-10-07 04:38:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d590753-e8d5-3759-a4b2-c500e28c8ab3 | -14.65027 | -48.35624 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3dac761-9a42-3a18-a1a4-f3086d1fab22 | -14.66436 | -48.40042 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4417526d-079e-3f31-8c3b-77c54f67f77e | -9.44931 | -56.65256 | 2025-10-07 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1aa28464-59ba-3cf7-b234-512a50332299 | -13.25789 | -47.7956 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4efe5313-b0f9-33f1-a869-177f8d274385 | -16.06842 | -47.77554 | 2025-10-07 04:38:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 190ba545-c8c2-39f0-910b-eb3ea60be140 | -16.01875 | -51.04414 | 2025-10-07 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fdddeb0-8209-3c11-a16d-a6559d4c195a | -13.70961 | -48.09992 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a87783aa-e14a-3b84-8915-df7186044478 | -13.22959 | -48.45675 | 2025-10-07 04:38:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1df993dc-83f2-3e9a-8906-5a5c7f288aab | -11.6855 | -45.27737 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab26cfd2-c705-396b-81af-7af66393a4d4 | -13.32451 | -47.55722 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0517c702-f418-3deb-952a-d4b15351e8a1 | -17.98132 | -44.98751 | 2025-10-07 04:38:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a58c7e02-7e26-3b19-9626-96043d77d384 | -18.28372 | -45.46205 | 2025-10-07 04:38:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6c707c2d-9026-31e3-8a27-dcc4db20317a | -14.76444 | -46.06388 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |


[Clique aqui para ver as próximas entradas](README67.md)
