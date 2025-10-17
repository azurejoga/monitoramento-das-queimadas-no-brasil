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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 606dda9a-2094-30fc-93c8-dfcbdd6a8430 | -12.78528 | -44.88275 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7cffdc15-1763-3b57-9b0e-ad702bec5ca5 | -14.32804 | -51.47657 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 91fee020-1c06-3427-b2de-bcfc6c64d8e3 | -13.57686 | -48.49426 | 2025-10-17 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f64ebf2b-bf8b-314a-a790-0d2ef8b5002e | -15.7879 | -43.65177 | 2025-10-17 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f4650f0-2e2d-3dbd-a90c-d5c4e1f76247 | -18.08983 | -42.44913 | 2025-10-17 04:21:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 45.4 |
| 00ef4eae-e287-3a49-874d-c95d923cefb3 | -12.92653 | -41.82363 | 2025-10-17 04:21:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 137d2cf8-4111-3e1c-925c-2eea4a9da7d3 | -13.43135 | -48.56409 | 2025-10-17 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7afbaf1-e38f-39f0-9303-b583179e03e3 | -14.3253 | -51.4688 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d27d973-3b14-3a99-b47a-c177f32e6fa2 | -15.3283 | -47.764 | 2025-10-17 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 392cc4f8-c23a-38e6-90a4-d608aa500e78 | -13.70636 | -44.38106 | 2025-10-17 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f163912-20d2-38ac-a9a2-cb8f3e4a96a6 | -14.92181 | -46.72698 | 2025-10-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a8de6b73-4cdd-3fea-91df-5f2e40cafddc | -14.32826 | -51.42857 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3fe681f-ab60-3705-8ba3-c11d9a91b3e5 | -10.98307 | -47.91102 | 2025-10-17 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3789d16-6020-3b58-b994-7f2a1d1e2ca7 | -13.2747 | -43.13472 | 2025-10-17 04:21:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e5174871-d4bd-3d07-bd6f-50c9801554a0 | -13.50797 | -47.16274 | 2025-10-17 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1c97e19-b7dd-31a2-b0f1-8d8ca56a60dc | -12.58952 | -43.36521 | 2025-10-17 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 416c7340-374f-36e8-9e2b-1c3f8f78c657 | -14.33708 | -51.42479 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ac2aa72-6138-30c4-b450-50a0beb06e1f | -12.17151 | -45.07275 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e9bc696a-fcb6-3646-9c62-da2c5cdfdac0 | -12.42977 | -51.31275 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d43aea50-78dc-387f-a580-59117fc68676 | -13.45008 | -47.94058 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83f04ec9-715f-39cb-86f4-5426b725cc9e | -14.33119 | -51.47359 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9d97b962-a614-3c98-8dd4-8d861a0c9364 | -11.54553 | -47.04319 | 2025-10-17 04:21:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3df34896-a511-31a0-8d77-c1aee341b0c9 | -14.23502 | -54.9023 | 2025-10-17 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f56867c5-e3e9-35ad-9697-ef336f4b1bca | -11.54445 | -49.92129 | 2025-10-17 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c85eadb-78b6-32a1-9650-d8426dd4a662 | -13.76004 | -48.10801 | 2025-10-17 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73bf2187-13f0-3d85-879d-eaca89badfcc | -13.43575 | -47.9645 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 521f1ad6-ff24-3100-8c3f-c7430b097f9c | -13.95108 | -48.69592 | 2025-10-17 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0192ef2-d393-3945-b8e1-3b95f980f977 | -12.43172 | -51.30182 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c52adac-fc53-3d5c-a72b-de5c2ee8c948 | -14.56514 | -41.80024 | 2025-10-17 04:21:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 972b217e-fbb7-3419-896e-7dbed5b15719 | -18.26076 | -47.82091 | 2025-10-17 04:21:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55df789d-c565-3565-85fa-4ae8ffc5570e | -14.33262 | -51.47379 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a23a8e7c-ddf1-30e7-892f-5e7358e8a5d5 | -14.34437 | -51.45329 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.5 |
| a2e4f691-346b-305e-b174-fc07f6da453c | -14.30477 | -51.44594 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57153985-41a9-3f86-847d-4095cb24007d | -14.92238 | -46.72343 | 2025-10-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2af1564f-2e5f-3e4c-99ef-139df9f07596 | -15.7921 | -43.64805 | 2025-10-17 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 218a5698-c1a7-3bff-adf4-d9e79a5e5196 | -13.24048 | -47.11038 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d230a9b6-9f2e-3bf6-a7f9-4f1838fa363c | -13.75518 | -43.80894 | 2025-10-17 04:21:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd6dc000-3667-39e9-b286-d76a2009025f | -11.59087 | -44.06503 | 2025-10-17 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 10198c6e-68bf-365a-8372-946a29dd969a | -12.16003 | -47.93724 | 2025-10-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a78acbe3-ecb1-3fa6-82da-493e797b97b3 | -10.95549 | -49.76861 | 2025-10-17 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 81e7a8df-e810-3003-b34c-66047a6ad128 | -10.98215 | -47.89501 | 2025-10-17 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0273f845-5994-3bc0-befe-ad7b4a420c21 | -12.60539 | -56.51274 | 2025-10-17 04:21:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d851148-8350-3fa2-8870-b075b7ca95d6 | -11.75328 | -51.15535 | 2025-10-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15afc63e-26cf-337c-82fb-9cd1c3aadb4b | -14.23878 | -54.90734 | 2025-10-17 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7890565b-6c15-372b-9d14-9690bc5a08f3 | -14.33525 | -51.43529 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 95f9913e-f9bd-34ac-bf08-d2089990cf67 | -13.25306 | -47.13825 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 396254ca-21d6-306e-88e9-7f25cf2678d4 | -13.74291 | -48.21244 | 2025-10-17 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0df3e44a-3254-3fc4-a62b-b8706d82a832 | -13.0468 | -47.32129 | 2025-10-17 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af79be7d-5097-3927-8d07-618dddb72067 | -14.89238 | -52.42867 | 2025-10-17 04:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 01bd61dc-0a77-39b3-b9b1-99fbfb97d4e2 | -14.34529 | -51.44802 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.5 |
| a7eb45f3-c4a0-3e8a-b01a-7c36acf253a4 | -11.76264 | -51.1495 | 2025-10-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8fcc517-9169-3a4b-8c29-716f817f451d | -14.32694 | -51.45197 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 25f959e0-779a-3584-9f46-891d9faf45e1 | -12.2839 | -47.10973 | 2025-10-17 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 110977aa-a221-3714-8ec2-e22c35c6e94d | -12.16541 | -45.06811 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 002bb985-159a-37be-a095-c81aca41ecd0 | -11.57747 | -48.564 | 2025-10-17 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0c9b6980-5a28-347d-81e5-16ee90b67eba | -14.33772 | -51.43768 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| bc4a5ef1-f18c-3175-9ebd-731a89cf3a21 | -11.35263 | -47.28592 | 2025-10-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45c566fe-fad7-3911-ae1d-ef30a2a2dea7 | -12.4554 | -54.48746 | 2025-10-17 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad787299-90ba-3d44-b1b3-8e76762cb292 | -11.11917 | -49.22721 | 2025-10-17 04:21:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 786cc491-2fcc-3fa8-bcd6-abea85587040 | -12.92109 | -41.82557 | 2025-10-17 04:21:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2015b73d-7027-3820-bc05-a653c8958eeb | -15.65212 | -48.36715 | 2025-10-17 04:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9561d374-8eed-30cf-b6e7-e4fe8c929aa2 | -12.77804 | -44.88531 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 30f5e51d-e915-31b7-9bca-e3eb0922448f | -13.23933 | -47.11756 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bde6bc99-1721-3c6a-9ad7-e42377aa6ef9 | -12.46229 | -51.48564 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c40443b-2bad-3a73-befe-fb7ee960a0cf | -14.33201 | -51.47731 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3eb3aca3-d7e8-37ca-b79e-3fde499683b5 | -17.99809 | -43.41912 | 2025-10-17 04:21:00 | NOAA-21 | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca81ed7c-7b3c-3cb0-975e-3900d2582e52 | -15.04447 | -52.99531 | 2025-10-17 04:21:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bddb61b6-9fb3-3d9a-8a4a-26e74c079efc | -12.44532 | -51.31931 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5509c39b-36ec-36d9-a070-1f187973cabc | -13.41639 | -47.93438 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8902cab9-bd0a-3d32-832e-8a9db3b25e8f | -13.73274 | -48.21054 | 2025-10-17 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f167278-2507-3294-97c4-1ac81e563bbd | -10.98278 | -47.89112 | 2025-10-17 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bafdcdcb-ae93-3a08-8729-731eabad8f4e | -12.76521 | -44.87959 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b6edb041-b3d1-346c-a2ff-0ca6a8a16026 | -12.16764 | -45.07582 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ea821091-e960-388d-ae8d-9d4de86a8a22 | -12.94737 | -47.93692 | 2025-10-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0af0a00d-41df-3113-a98b-5b2c27fc050b | -12.06804 | -46.62816 | 2025-10-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f72108f0-3fd7-36ef-9076-a22c03396b33 | -13.01513 | -48.444 | 2025-10-17 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab4bb607-ebf4-3bab-b37c-5afb15ab7d9b | -14.3255 | -51.44434 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dd9b09c1-1951-3910-b9ee-f20c61e56b50 | -14.72285 | -48.30495 | 2025-10-17 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62f78b5a-a131-3b44-8fe5-6a9264e72a4e | -11.58521 | -44.05655 | 2025-10-17 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 61185b33-2bb8-384e-85cc-9497803916d6 | -14.33183 | -51.47009 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1835e062-de13-3ccc-bbcf-5c1b5f861a1a | -13.93883 | -48.68983 | 2025-10-17 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c536659b-0e17-3f98-bb54-11daaff34883 | -13.73889 | -48.21563 | 2025-10-17 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85f1b802-fe3f-3771-9a0b-c79c6eeaf650 | -11.75922 | -51.14513 | 2025-10-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 620b3e4b-dd78-33f5-91e9-34cd80430827 | -14.33249 | -51.45108 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 538b09e0-4766-3493-994a-62b441ea3c9d | -11.7295 | -45.2272 | 2025-10-17 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d639a86e-4cc7-3778-9e03-6733308f8bab | -13.65593 | -46.81091 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 282802e2-5489-3b9b-9a8e-a0c3f81520e6 | -11.97035 | -46.55778 | 2025-10-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fa03c0a-bb90-3bce-9e07-ce68090563e9 | -14.35625 | -51.47095 | 2025-10-17 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 65511692-b5e1-349e-a14f-72bf02289476 | -13.94636 | -48.7029 | 2025-10-17 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dca32bf9-960c-385b-9249-cc32d70e9d99 | -12.79197 | -44.8838 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06e31387-8e7b-32ce-9d9f-c9ef0805087f | -11.36863 | -45.29587 | 2025-10-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 311d1f24-2f80-3dea-84d5-f68dff800bda | -12.77245 | -44.87703 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01724a9a-cc2c-38fa-b4da-544d5b686dd1 | -13.44611 | -47.94363 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d19d9dde-11b4-3343-acef-5f20504ca20f | -11.06528 | -47.5988 | 2025-10-17 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7312cabf-4658-3803-8589-53aaed25bd86 | -16.39361 | -53.31709 | 2025-10-17 04:21:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8abd3496-def8-3ca1-afd5-a643a76b3e10 | -14.24041 | -54.89871 | 2025-10-17 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dab4d1c3-6aae-34af-9bec-47d31cb7db94 | -13.73953 | -48.21174 | 2025-10-17 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2cd7099c-b0ab-35fc-932e-a5d2130bbc2d | -14.86938 | -52.43645 | 2025-10-17 04:21:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e4e0e5f-b19f-30a5-b507-7d36d2ad4d1f | -12.76736 | -43.8849 | 2025-10-17 04:21:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e03f61a-4876-3756-b464-105d8aebd3c1 | -11.71519 | -44.26929 | 2025-10-17 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README71.md)
