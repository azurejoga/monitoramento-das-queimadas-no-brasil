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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9f7865a-08ed-36b8-ae89-7cfab7b993b5 | -6.35229 | -55.80219 | 2025-08-26 04:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4f165e8-e34b-3c33-a5c4-5c29ff3d8961 | -10.82179 | -46.37906 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89392101-6445-3254-ac19-e1853de80488 | -8.07099 | -49.67215 | 2025-08-26 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 381d5e62-5278-3cc5-853d-192c1c6c3c6c | -6.03324 | -42.70207 | 2025-08-26 04:21:00 | NPP-375D | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 156b769a-28c6-3886-b11c-9a4f3cce3c45 | -7.53657 | -44.93289 | 2025-08-26 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a00e71fd-c87e-31c5-baca-c338ffcaf6a1 | -4.893 | -55.81445 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ab75cf4-601f-38ce-a910-1ff011918bf7 | -6.29439 | -43.77725 | 2025-08-26 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2bdb047-0dd1-386b-91ca-0c2ffc4d781d | -5.46807 | -42.60918 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a1a6c76e-8610-3cfd-b327-51a92e0fc603 | -3.24896 | -46.91076 | 2025-08-26 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 999f03e8-ecf7-3674-b3c3-5bf923914eea | -5.87851 | -43.40593 | 2025-08-26 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1284902e-e0fe-324e-86dd-9faf29d5784d | -11.11684 | -44.74773 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b33381c6-cd17-3a10-b7f0-2f7706534273 | -4.9574 | -55.81491 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6d06797a-b9a1-34b2-bec2-45d3f296674d | -11.15728 | -44.69582 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19149ee4-c29a-3c4b-8aac-68bf830299d2 | -6.87109 | -45.65191 | 2025-08-26 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81ca065f-0a23-38cd-a324-85da9aa81f04 | -3.9218 | -47.69117 | 2025-08-26 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ca29013-6c64-3cf3-b463-0f4ec6dfa7fa | -6.29884 | -43.77074 | 2025-08-26 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3125936a-f2cf-316b-b7e9-89216a9bcc99 | -7.52883 | -50.54412 | 2025-08-26 04:21:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07c247a2-444f-31b1-b180-cdf51b721032 | -11.15525 | -44.79801 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 128acd04-066d-3b61-8359-de1421325929 | -7.21532 | -44.4365 | 2025-08-26 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24c85868-b9e2-338f-bec2-8912d243645f | -7.61446 | -45.22693 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57b8b57e-ce00-3263-989e-e8516b683420 | -6.12683 | -43.11105 | 2025-08-26 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 14e856e4-57c6-35ee-8297-4f353c8d542b | -5.74874 | -45.36102 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fb65fa9-ab72-3699-90cc-61aed8391494 | -9.84772 | -46.45877 | 2025-08-26 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a538093b-7544-3652-b91b-123a55a57108 | -11.15241 | -44.77199 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 1f33d43e-476b-3684-a2ac-dc1c82203774 | -8.38383 | -48.01819 | 2025-08-26 04:21:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdd8fa2c-9b8b-3069-8748-96dd542d15c1 | -5.87235 | -43.40134 | 2025-08-26 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4676dea-6ec7-342b-a43d-fb01a6ab7ff3 | -5.47434 | -42.61389 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b081c909-9be9-3d95-9cf7-b02873af8ec9 | -8.07823 | -45.01171 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20f99631-0c3a-3d6e-9b97-ce5b6d2d1ea2 | -4.79007 | -47.28251 | 2025-08-26 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f49e05f-5a68-309a-87a1-1ef851db43fd | -6.76319 | -42.98817 | 2025-08-26 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b7f7fd7d-cde9-3ddf-83e4-6317558a62f2 | -11.15686 | -44.76537 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| a448f8ee-8929-3a84-898a-e4aaead1305d | -5.78306 | -43.60773 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1aeb9144-d5d7-3c71-91d3-0869a0d95864 | -11.16131 | -44.75874 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| fb4cf87e-a94a-3f3f-bdf1-63b4bf5c3c88 | -11.16076 | -44.76231 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 034d11cf-1261-3a62-be5c-60ffe65ebd0f | -6.94815 | -44.17681 | 2025-08-26 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ae3f9d8-e465-389c-bc49-3a4898f30d49 | -6.31432 | -41.88738 | 2025-08-26 04:21:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 187e2554-0409-3937-b347-6132bb1b0841 | -11.14792 | -44.75662 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53537d93-fd00-3ce1-abe6-74562f6fad59 | -10.68605 | -47.17419 | 2025-08-26 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58dd0957-ca6f-3762-afb4-ab39f89389c7 | -6.517 | -42.97734 | 2025-08-26 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef4ce6b2-0346-3aa0-b5cb-ef1dc3d6164c | -10.53553 | -46.78924 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a67f8153-972d-35ed-81b3-54ba6df52720 | -8.9092 | -44.8512 | 2025-08-26 04:21:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fee6805d-48f2-3a43-8a1c-eb3cdc557ee1 | -8.15967 | -45.05676 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c620a0d5-1960-302f-a3a7-34b841f6cdc0 | -4.96003 | -55.81863 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| ae69256a-9cd3-3863-9be0-46cab1a9e721 | -7.66626 | -42.67593 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f168a680-c7e8-3af4-81d3-ee922d773f60 | -7.21473 | -44.41856 | 2025-08-26 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8239998c-dd3e-32cc-b12b-937f786d7ac2 | -4.82574 | -47.31382 | 2025-08-26 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b58265e2-5fab-3cab-a992-020d6033e128 | -4.79075 | -47.2784 | 2025-08-26 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e1efcc2-c1a1-32ef-b6e3-82076d04653a | -6.35193 | -55.80452 | 2025-08-26 04:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3541b072-a109-3f7a-9eff-d3b0b3605395 | -7.16869 | -45.16322 | 2025-08-26 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5f8db3e-2d6a-39e1-8868-aa5a1e210063 | -8.24832 | -45.09591 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32c42b3f-0c75-3b2c-9448-b9c0dac7aad8 | -7.08013 | -41.49898 | 2025-08-26 04:21:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7e505d1f-9aa5-3f29-9405-9225511c0acb | -6.67538 | -44.40474 | 2025-08-26 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3909c123-28ed-37ef-a73c-a7dbba4e853f | -6.49961 | -44.68301 | 2025-08-26 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4ca2046-1b8c-3b26-8921-8637eceecd0b | -7.2197 | -44.40863 | 2025-08-26 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b59f6168-4cc6-324a-98fb-a49f49be3aa9 | -6.87217 | -44.40043 | 2025-08-26 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e00aba07-8198-3fa5-aa35-cd19c7867c81 | -9.6937 | -48.34074 | 2025-08-26 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e076e82c-ddcf-33af-b48d-7fbe94b58346 | -7.27322 | -43.34509 | 2025-08-26 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bbe8e31-56ce-3e1f-a3e9-0163b2b372bb | -2.93203 | -53.69044 | 2025-08-26 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94259fd5-e393-3359-86c1-afdfe4b3505e | -8.24887 | -45.09243 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d7ef565-f7e0-383b-8883-130c9e1a230f | -5.98889 | -43.36832 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1a15e9c5-b8ff-3aed-a124-e1591283ebe1 | -9.06352 | -49.55535 | 2025-08-26 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6e8c9ca-1b9b-386c-8a3a-36857a77671d | -7.73894 | -50.29581 | 2025-08-26 04:21:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 352c4d88-04ae-3b78-b0ff-e24a1052319f | -9.16793 | -40.60561 | 2025-08-26 04:21:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| cd0ff66d-20d0-3a88-8f64-6a3d1dcecb89 | -11.14571 | -44.77092 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2223d9c5-dec4-33b1-af76-6d585ee9d587 | -7.21528 | -44.41508 | 2025-08-26 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aed9d8df-ad01-391c-9b14-4a301405dc61 | -6.56016 | -44.21596 | 2025-08-26 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e62fbfd4-ef40-3fab-b970-6bb008eba1f9 | -2.92576 | -53.69326 | 2025-08-26 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 750a6732-f1e7-3a4b-bff4-5e8c4854c78b | -4.01768 | -49.50544 | 2025-08-26 04:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22d2e9d2-5555-3b1b-93ff-66ec74e866e9 | -6.56736 | -44.21352 | 2025-08-26 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c5bc0efa-6f6d-3ad6-bccf-4de674a38637 | -7.73899 | -45.16869 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29ba3c4c-8aeb-348d-900c-b60a3c46ef5d | -6.06352 | -43.99177 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef346216-9f90-3e81-8b52-91f5cd859d92 | -5.74144 | -46.14151 | 2025-08-26 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20b2ce32-be32-3e34-97f1-1f57e0924bf8 | -8.07491 | -45.01118 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bca9ad14-9a95-3d59-bd0a-5616804372e8 | -8.24722 | -45.10288 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30a40a3c-11f9-33fb-aa90-64b16f3f4a51 | -8.2901 | -46.32924 | 2025-08-26 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff0e2453-4016-3c9b-ac87-79637495f1b9 | -6.44403 | -46.11703 | 2025-08-26 04:21:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee99f569-406a-3fb0-b45a-983f35e13955 | -8.16631 | -45.05782 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fda74338-396e-3d2a-aaef-545e2a923b1f | -5.57742 | -42.62556 | 2025-08-26 04:21:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 81f545bb-bb36-35c1-af69-6ecd1f504b02 | -7.63442 | -45.2301 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 93e74ac7-f964-3712-88c3-5ed66bebec51 | -8.23727 | -45.12272 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 646b7e65-9f80-3c2a-9775-7f14be5d9a80 | -10.53832 | -46.79342 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ec2bbe4-2c92-3253-ac12-e43eabfa0b62 | -7.46578 | -45.01426 | 2025-08-26 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8986627b-342b-3b71-862a-f1a842b92958 | -8.48259 | -43.66686 | 2025-08-26 04:21:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae35ca1f-a811-3510-8aee-b505742e8f0d | -4.96444 | -55.83 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8121a4f6-6d44-3eee-b482-8f94a5393db3 | -6.75209 | -44.0026 | 2025-08-26 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30724086-79a1-3ad3-8f8c-adacefef15c9 | -3.25617 | -46.91193 | 2025-08-26 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c57b4981-2c24-30b5-92e9-fc69f74e53e3 | -4.01705 | -49.50924 | 2025-08-26 04:21:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bfe0fbb-847a-37e4-9805-a420d1ba2a77 | -10.39902 | -47.15445 | 2025-08-26 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d4c31d77-b664-38bc-9cd7-4d938bf35081 | -6.89603 | -44.422 | 2025-08-26 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b946afd-f006-35da-8c56-72093ab8b2db | -4.93595 | -47.55434 | 2025-08-26 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9efbf15f-7451-32fd-84df-912e5ebe6093 | -7.58844 | -47.49918 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5ad8afc-df56-3ef9-bc8e-a002d6b8b435 | -8.16244 | -45.06077 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4902910d-b698-3ea9-a026-d09885b6283c | -7.6605 | -42.66722 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1e5db581-8d41-31ee-a1b5-59c898d821c3 | -5.55042 | -45.56979 | 2025-08-26 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fe28e7e-4974-38e4-b50b-f2cd87035249 | -8.40484 | -49.49373 | 2025-08-26 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b657daf-b82c-3dc1-bcc0-19d027d03e6c | -6.14374 | -44.38855 | 2025-08-26 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c55ae33-8b5b-380d-83c7-507658962f3a | -6.20136 | -44.15234 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9dd2c078-fc11-32a1-891e-88fa685fdfed | -6.38768 | -45.60026 | 2025-08-26 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5a61724a-c14e-3768-a8a5-48d7fcaad67f | -9.69444 | -48.33634 | 2025-08-26 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35f58eeb-4f53-3c96-afac-8ea6c849fc45 | -6.06854 | -44.00334 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README37.md)
