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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18710cd2-3599-3ddc-8011-396b2f8ce5bd | -7.46277 | -44.82164 | 2025-09-01 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1137dadb-8d66-311c-9180-8a11f1f691c8 | -8.34225 | -47.44473 | 2025-09-01 03:45:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eede2c3f-200d-3a97-812f-23587cb69a7d | -8.47495 | -45.17409 | 2025-09-01 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47e628c0-2a0d-38df-a1f5-cd5a21168364 | -12.56017 | -48.22275 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 7e628077-2848-32cb-82a3-3c8f61b7c94f | -13.29714 | -46.91349 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 03a26cbd-ca5b-3d2c-9300-188d83a3dae9 | -11.89288 | -46.74986 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2596cc1-a74a-3c4c-9443-003ea743d20c | -12.9768 | -48.11479 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e7dbcfea-b809-33a5-ab4c-ee2c4cad15ae | -8.19856 | -46.7707 | 2025-09-01 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c9b38ecf-6eaf-3dbd-9484-58ee060109f5 | -10.60601 | -44.32729 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 0394f5a1-6ff5-35a7-b1c4-15b78e121ea8 | -14.02451 | -43.90824 | 2025-09-01 03:45:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 68e711b0-5ca2-3e16-8ad8-3b26bc04adaa | -11.95573 | -45.84574 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b570503-1dd3-35cf-b677-cbafb20e263b | -11.80516 | -46.43329 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d7f1e07-8852-31a6-91eb-7b03abe8af48 | -13.37222 | -46.32164 | 2025-09-01 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4616b364-ede0-3688-b79a-7cc8bedc367c | -13.37699 | -46.94405 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5810657e-a31b-3762-8910-9f40c74c50d1 | -11.08707 | -44.73807 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f651f5ce-69f6-37bd-986b-9eead817e845 | -13.37351 | -46.3149 | 2025-09-01 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8460c7ad-f858-3493-b945-0c388679cffa | -10.6257 | -40.51562 | 2025-09-01 03:45:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2198f059-e702-39b1-956e-6b57f9702f2a | -7.63267 | -44.03421 | 2025-09-01 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0233f474-71bc-3cf1-8ebc-06166d072762 | -7.62761 | -44.03347 | 2025-09-01 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| edf6efd7-4899-3a06-9f4c-40a4ecbdfaad | -9.64743 | -46.6297 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e8739539-2419-38df-bc65-6a29aab79a2f | -13.37563 | -46.95107 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 53959549-b998-3d11-baa7-9a24dae1c9c1 | -12.85119 | -48.07777 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bdace993-ea25-36a2-ae59-96aabbeacce5 | -11.80782 | -44.94579 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54425ac4-0316-3d87-9642-284cc84fcc7d | -11.79362 | -46.43409 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b57b5a4a-b6b8-3905-bc09-adf5939b1ab7 | -8.84777 | -47.51521 | 2025-09-01 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c3ea41ba-9e9e-34e3-8f6d-226476ffd45a | -11.38223 | -43.6395 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d780468e-b2db-3404-9e28-e3dd53383fe7 | -13.68586 | -50.77161 | 2025-09-01 03:45:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45655c44-b8ba-3f7d-9cd7-9c4cf270295d | -7.95269 | -46.36063 | 2025-09-01 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e43766ab-3562-3c2e-9c90-61f059ad6474 | -8.84602 | -47.79383 | 2025-09-01 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d7e8a27-9bc1-32d2-9db1-65a178b56c52 | -12.56626 | -48.22377 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| dbc97d09-3f29-3157-9340-7e3e3a8a897a | -10.58037 | -44.85165 | 2025-09-01 03:45:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a568b13c-38fb-37bc-8289-7f68641bf7e5 | -13.34579 | -47.04522 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78d6e408-97a4-3f33-81c2-6a1036fd4599 | -11.05297 | -46.90708 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc904291-7246-394f-8df8-c15e24cd5c72 | -11.79428 | -46.43066 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 779f16c7-966b-357c-a83e-8c5aaa301b9f | -13.66906 | -46.93855 | 2025-09-01 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c465263-e955-352e-8a66-7e3ce9e51956 | -8.85116 | -45.73368 | 2025-09-01 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d472ff2-c8bc-3e6d-b12c-6ef4945cbc0f | -11.37112 | -43.62477 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a96f3433-ffbd-3069-80ac-1f0df6212c22 | -12.55538 | -48.21996 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5bf2d01f-d800-3db5-928e-6db899adb154 | -11.80299 | -44.94632 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c9edc43-3c0d-39a7-9185-1539dbe15401 | -11.91664 | -46.44602 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b7b7528-d471-3201-8c18-a7756283fb37 | -13.68776 | -46.87242 | 2025-09-01 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ba6ee014-010c-3db2-96fd-911f0733ba03 | -11.87762 | -46.7086 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0343667-b8e7-32c6-99dd-8572b7d266c4 | -8.82474 | -47.83708 | 2025-09-01 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 16d66ac4-6f6f-3627-b538-025906c6824e | -7.40189 | -47.43698 | 2025-09-01 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 51122465-92cb-3cc4-b22b-5dc3918a9b78 | -10.61089 | -44.3282 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26785dc9-2346-3672-802c-089eea4cdb17 | -11.89895 | -46.68068 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c5fd887a-9e4b-3279-bd5a-9d5f0b5e340c | -9.66504 | -48.07761 | 2025-09-01 03:45:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 34e41d9b-c4ad-3ad4-83f0-8c62bf7de61b | -9.23365 | -47.08089 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ed3e1d8-8db8-333c-9e18-1e12ec0d9e00 | -7.38196 | -47.43908 | 2025-09-01 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98f37379-039f-36da-8d1e-23c60a7f4d2e | -12.22248 | -43.88241 | 2025-09-01 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0fb55136-f0b0-364c-93c5-4b33f35c3e42 | -7.66204 | -42.70726 | 2025-09-01 03:45:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c7710de1-223c-3c97-bcd7-0b2abd3c22e1 | -12.80457 | -48.08071 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da4bc553-df0e-384b-960c-6981eb7ed37b | -10.60172 | -44.33615 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4f63d906-807a-3100-b405-11ed942e144f | -11.01056 | -46.94151 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f278904-c998-3008-a632-d77fed27da34 | -10.0412 | -48.12318 | 2025-09-01 03:45:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dd3ccde2-c657-3b76-80e5-931467b0f2de | -13.52285 | -46.98469 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fad5441a-45e1-3a4a-a7d4-0a5dbb86ebb5 | -10.04218 | -48.11816 | 2025-09-01 03:45:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 58c724c2-ce77-3e96-bd14-b679e758a7c1 | -13.47717 | -46.98381 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 111c72de-7bba-3799-a363-7bbac02775ea | -12.95426 | -48.10346 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 34eadff5-577b-39ca-85b8-8396885c87a4 | -13.37066 | -46.94573 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c1204b43-234c-38be-9a0c-073ce0021445 | -11.89815 | -46.68471 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84cedc4c-dbea-30b9-9879-0df26c56da9d | -11.89116 | -46.74898 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ac33f47-69e8-33e6-bd56-5f1c43056bbb | -12.83323 | -48.07449 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4afcf737-44fa-3e10-b7b4-f427e4497a14 | -8.19114 | -42.30025 | 2025-09-01 03:45:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 71492c4c-33ee-37de-b810-830f0d47e20d | -11.01544 | -46.94704 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41890941-20f1-3e78-b521-df0f4a3612b6 | -12.4102 | -46.46278 | 2025-09-01 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da9babcb-f2a3-377a-a604-9c63ea0f7e56 | -11.02741 | -47.03907 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7e1ae168-07c6-33fd-807d-301e12e5e0b8 | -13.37684 | -46.94352 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 95d83a38-4be0-316a-8453-28bbbcfa2895 | -14.04428 | -44.55742 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0d8ecc6-ab1e-3a49-8511-90af82374ad7 | -14.53158 | -39.73853 | 2025-09-01 03:45:00 | NOAA-21 | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4c423b3b-b2c7-3c88-a54f-59cf050cb9d1 | -11.91361 | -44.88181 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca8188ad-7a05-39be-adc6-bb8bab7a6b58 | -10.88883 | -45.80574 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 857b51c1-7607-36c5-b073-ba7945aa59c2 | -12.97092 | -48.11313 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aeab2b29-803b-33c9-98bf-558537c3d878 | -7.5036 | -45.83569 | 2025-09-01 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c24fc157-bc64-39fc-b5f1-d69aaca8b8e0 | -12.55503 | -48.21695 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef6df7f6-c8e0-3833-acbd-05e07ce40a75 | -7.954 | -46.35804 | 2025-09-01 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14dc42ae-2d54-3779-8fec-051c1d10cc89 | -9.66659 | -47.05691 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f489f10-6a2e-3c21-a7d1-399eb43db4e8 | -13.36573 | -46.9418 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9fb118fb-4c47-36f8-98d5-a4e2861413ef | -8.8354 | -47.51298 | 2025-09-01 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3cf8ef7-3537-331e-b976-6599815f7064 | -14.50066 | -43.81181 | 2025-09-01 03:45:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6293f25-43e1-3324-9506-7f8fa0804254 | -11.35595 | -43.28376 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 529eab04-5f91-3098-8ec1-161fa0c2db30 | -11.02974 | -47.02705 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ec84655-2b04-3b67-b46c-659c8ba9c70b | -9.67273 | -47.03754 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2d53cf9-aed3-3489-9574-228538b122de | -9.63765 | -47.79477 | 2025-09-01 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f6709393-39f1-3ffd-b568-f8ae2520729f | -12.30788 | -45.67969 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 614b9ca8-1a27-3e60-ac63-2b862326b767 | -11.03645 | -47.05433 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c106fdc7-5bc4-348f-a610-3f19a7cbec5b | -11.0877 | -44.61963 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c388ec82-5f17-3862-8122-95a86ac99ff7 | -13.47405 | -42.48028 | 2025-09-01 03:45:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1fd8bd34-aa05-3107-94f3-34c3a0adfc15 | -14.04893 | -44.55839 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4d8b7a5-fdd3-380a-aea3-76ddcc40d2a9 | -11.08154 | -44.74012 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 422fff0c-e920-3cee-b35e-9d2ed39b47a3 | -10.76815 | -48.83228 | 2025-09-01 03:45:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66ca1bac-0764-3887-a1a7-83ac2aa075b2 | -8.17546 | -45.0364 | 2025-09-01 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0dec080-3615-3993-a180-8e46cc26b9fb | -11.89275 | -46.74101 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0b0516d-fdcd-395a-96d1-469b9ae86fe0 | -7.9435 | -46.44912 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87750b9e-e129-386c-ade3-b663841b2c6f | -15.58523 | -48.3412 | 2025-09-01 03:47:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f5c1b758-9977-3743-8f02-93412b184dab | -14.7886 | -46.73816 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e208b939-6f45-33b0-a353-f8d608852742 | -14.854 | -47.09627 | 2025-09-01 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4ad53e76-281e-3267-a4dd-3a5755e3b748 | -15.70027 | -48.89347 | 2025-09-01 03:47:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| aaf2b366-54d9-3f8d-8732-4bb22e1a0948 | -21.08728 | -48.23781 | 2025-09-01 03:47:00 | NOAA-21 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8d65b049-991e-3c00-995d-d4166f836805 | -14.78815 | -46.71264 | 2025-09-01 03:47:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README22.md)
