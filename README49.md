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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3de67c6d-de5f-34f8-89c8-a55f67cf754c | -10.34536 | -54.19777 | 2025-10-27 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7584035-57f3-31d4-8f42-bf161d9b6fbb | -14.71696 | -52.80658 | 2025-10-27 04:34:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53caef63-db3a-3076-a9d2-bec1802a076a | -10.33908 | -47.22461 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb1a0ac5-71b4-399a-98e0-02912dc63368 | -10.31932 | -47.17329 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2278ca7b-fa9b-354a-9fff-26ab505c5ea8 | -10.92355 | -48.26698 | 2025-10-27 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2d91531-db3e-3985-8e41-81e72a70882a | -11.05515 | -47.87569 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 330f2d2a-2caf-3848-a604-db5062b002d3 | -10.63161 | -47.88923 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc02dd3f-6b9b-38d1-b1ca-44dca93be0b2 | -10.51322 | -47.81951 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf64ae9a-e13a-3922-9a04-00924cee408d | -11.02084 | -47.85643 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7feadc50-c6e1-36f3-8074-3c01940407aa | -17.79027 | -46.71968 | 2025-10-27 04:34:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7729055f-3f63-3fa0-973f-fbd190418a89 | -12.8987 | -54.7337 | 2025-10-27 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 858fabdd-79bd-3daf-9aa7-0a0874b5d1d8 | -10.20521 | -52.66131 | 2025-10-27 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b596c13-f69f-3f63-9561-fd52849ef280 | -10.40768 | -47.10165 | 2025-10-27 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bb5d3b2-0d0a-35b3-b35d-e8c4aecfd9f4 | -11.41941 | -46.10263 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4859a2a8-bc2b-3c7d-9f78-b921df115498 | -12.23721 | -46.499 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e368093e-8ac4-3b8d-95d2-d15aa6f59d32 | -14.44842 | -47.78224 | 2025-10-27 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d56bce4d-3058-39b6-9954-f02b2491e814 | -15.51883 | -50.01361 | 2025-10-27 04:34:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 55ccafa4-b1d7-32db-8535-37f7f6119f4c | -12.89936 | -54.72997 | 2025-10-27 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 919e0b39-77e5-3f7a-9ed2-2294a1e44688 | -17.03926 | -47.05381 | 2025-10-27 04:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ccb46df0-5052-3f26-94d4-b0ff66d2dc8d | -10.3569 | -47.17544 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0d7387c2-60bd-3156-994b-2998a4873883 | -12.3287 | -47.47372 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64f9608e-33a6-331f-9d5d-f3fc522593e5 | -10.90422 | -50.23537 | 2025-10-27 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f058612-7181-3f91-bc2a-f94bd791b4c5 | -11.91269 | -43.82747 | 2025-10-27 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| baf3a295-755d-3f94-881d-7f7a6f97da7e | -14.63285 | -48.41697 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85d0257e-4751-3076-8667-dc85ae7529fd | -10.98149 | -47.84645 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fba73010-b2bc-3638-88e7-d48e343c0771 | -15.19783 | -47.22761 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e5838e2-4981-3d55-b3e8-2e602ca60ff2 | -10.95703 | -47.58603 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f025af34-f847-3a5b-a11f-99481da087e5 | -17.21125 | -47.655 | 2025-10-27 04:34:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f48ba53-0754-3a39-a0eb-1b0f77817507 | -12.28556 | -43.833 | 2025-10-27 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06f33972-5ff9-34f7-8a12-ca76840ae1b8 | -11.98386 | -49.76945 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ce2d960-e313-3cca-8fa1-1fe30382100a | -9.60472 | -50.79005 | 2025-10-27 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bf62a76-b454-3568-bc7e-e421b7537030 | -17.31417 | -43.60923 | 2025-10-27 04:34:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d184174d-a514-312f-a44e-3b1aa59c92f0 | -10.93851 | -48.08212 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 708f08ec-fe63-3b82-9ccd-b8448699cc7a | -13.60016 | -47.59618 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c1370b4-eda7-3040-a6ab-ee9eeeb2d562 | -12.41159 | -44.70848 | 2025-10-27 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a23a9ba-e33f-343a-9315-845bb5725797 | -11.03129 | -47.81066 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b1c61e7-d9b4-33e3-8c96-9277f5af574a | -12.33657 | -47.46734 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2d54dab-1097-3cc8-93ab-f03c7b68534f | -10.99227 | -47.93147 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c21285c-c161-3ff2-b05a-b8b546b2c6bb | -14.5405 | -47.988 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23c32948-9c0c-3918-b78a-32476d92052c | -13.63751 | -47.60218 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c026e7d1-614f-3e8a-be7e-e5fbdedfe341 | -10.73299 | -44.19259 | 2025-10-27 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71ea0d64-7469-334b-8d79-407b629160b0 | -12.65724 | -52.62991 | 2025-10-27 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a6c97d35-bccf-3fce-96e9-275763198221 | -15.51334 | -50.0054 | 2025-10-27 04:34:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00b919a1-61a0-3dfd-b716-95d495888fec | -10.9234 | -48.02584 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ec4ac22f-9a73-3b52-996f-faebec8afd6d | -14.49501 | -47.88935 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 792d2b9e-a1ef-3ffa-86e9-7c2b351d4116 | -14.63341 | -48.41331 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2210b1a-3354-375d-9f26-75645ffd1875 | -10.31774 | -47.20644 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 15cbf3b1-2a9b-374b-ac2f-baa1b479b2c6 | -12.08468 | -46.40084 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 47d8b3b5-8e36-32b9-97a2-cfa0b02a960d | -14.4888 | -47.88457 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fc8436e-8d25-3bee-bcd1-e0f05acd6380 | -12.35803 | -48.11341 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89c43bf0-be18-3ab2-9b2d-896bdd419b6a | -10.75565 | -44.20094 | 2025-10-27 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 05801be7-0c46-3f2c-b424-7f544cd502fa | -11.15588 | -48.32526 | 2025-10-27 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4995f0c7-c790-3c7d-ab4a-950f26e8d36e | -12.28599 | -43.8319 | 2025-10-27 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22d50aa0-9678-358d-8ddd-cde1a83430f6 | -15.91683 | -47.45831 | 2025-10-27 04:34:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cff7b81-80ec-3db1-a34b-cca924537870 | -14.62556 | -48.37461 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b19dc1e-a917-331c-b8f1-27c2bbba310f | -14.54334 | -47.99218 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 21b8e803-5542-324b-a3c8-13466ff8b873 | -13.30158 | -47.07965 | 2025-10-27 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b670d37-013f-3cef-af60-a8e6630b5afa | -10.35915 | -47.18323 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d6aa64fa-01f1-31c7-a654-58bc47758cc3 | -14.40131 | -51.55045 | 2025-10-27 04:34:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 051a56d8-277b-30dd-b9c9-92f66e07c603 | -12.22483 | -46.52659 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d805cb6-a434-3a8c-a9f8-8883e871e7cb | -10.69336 | -48.06147 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f3175e51-d184-3bae-a3f1-a67bd480a602 | -13.04831 | -45.86584 | 2025-10-27 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f9b3494-7206-3aa4-a283-5de477861755 | -13.25639 | -47.97038 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25451efa-086a-3d33-9834-ea3c7158f7f6 | -17.32694 | -43.65178 | 2025-10-27 04:34:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5259cd04-b99d-3029-a8d5-ba052ddc446c | -13.03607 | -42.32204 | 2025-10-27 04:34:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c873a9d6-9464-3886-a581-a749dac56a49 | -10.91735 | -48.02077 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ce3fa548-04e2-3dff-805f-4f0a4bd38549 | -10.35187 | -47.18582 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad45f261-a932-3d29-bdf4-440c301ad9a7 | -16.62941 | -44.58258 | 2025-10-27 04:34:00 | NOAA-21 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c743b8c-c84c-3859-8bd6-6fe6495e4940 | -12.23303 | -46.49554 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59069f42-4c10-3b47-b605-395910bd38a8 | -14.50124 | -47.89408 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86c1bccb-813c-340c-8ae4-b1381c9f23c0 | -12.64123 | -52.63602 | 2025-10-27 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4de0ed2d-a8cf-3ec3-8f76-cabac9e1f30b | -11.4221 | -46.10991 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 25fe8efa-c391-3b74-96c6-0c21a3b21625 | -12.23428 | -46.49453 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 023b5b91-aeaf-39c5-ab92-14e5466813f1 | -12.28196 | -43.82904 | 2025-10-27 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 448319c1-cc71-374e-9738-b64ced9465bc | -10.91058 | -50.28127 | 2025-10-27 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2e087d4-1dc9-317d-a589-a4fef525e1ea | -11.42356 | -46.09898 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6cee2e5d-8259-305d-b286-e71faf2db681 | -13.25304 | -47.96981 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3c4dd49-4bc4-3d13-89a4-70f1be13e9c0 | -10.31321 | -47.19087 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b07e6228-5c34-3bfe-8fe3-d55e735d0dd3 | -10.9956 | -47.93197 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5e9c918-7b8f-3c6a-b35e-fa463eff060a | -10.35127 | -47.16712 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 56f8bcf0-4dfd-350c-b7b8-598ea9182123 | -14.67706 | -46.34277 | 2025-10-27 04:34:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1237fe96-e742-3822-a0c0-f329c2d7adf9 | -17.07966 | -43.1894 | 2025-10-27 04:34:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8050e97-c2b6-3033-bfa4-fad675442dfa | -14.62279 | -48.39293 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cd11cd7-ae4f-327b-be95-c0a1caec4809 | -11.06958 | -48.33332 | 2025-10-27 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1834804b-08bd-395e-8101-e8ac557ce93f | -15.96714 | -43.01849 | 2025-10-27 04:34:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19bfb2a6-75b1-354f-ac07-0970ebbd7d1a | -13.53812 | -49.56163 | 2025-10-27 04:34:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa2acf70-9cf1-3694-a384-79ef5b037c7f | -10.21276 | -52.6625 | 2025-10-27 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5c86867-e7e8-3b34-95e5-dbe6209dc694 | -14.67647 | -46.34699 | 2025-10-27 04:34:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 26459c7f-710a-3895-a598-b4d196704e5b | -17.5094 | -44.32857 | 2025-10-27 04:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9b084a3-56a0-3ee3-bc8f-0ce2dfe7e025 | -10.62976 | -48.01187 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a353d0e8-f1ab-3347-a728-c70583ab31cd | -17.31859 | -43.60989 | 2025-10-27 04:34:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 881cfb25-847c-3211-9241-c38def1e5d75 | -11.59952 | -46.79299 | 2025-10-27 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d3901dd-8c6c-3abc-ac5e-0e9fa8bcaa9e | -13.28656 | -54.39346 | 2025-10-27 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ccde431-9050-362c-95a6-a14a945bebbe | -11.03348 | -54.26572 | 2025-10-27 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a570fde7-ae46-3f53-84cf-64d16a0a6d28 | -10.67674 | -47.79463 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a115bfaf-f418-3024-8b68-450acaaa6bd1 | -13.55905 | -49.5578 | 2025-10-27 04:34:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 778b594c-55b4-3201-8a5f-17f563a9eef1 | -12.35693 | -48.12058 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4cd81d39-6e53-3f54-8743-ca655fa6e4d2 | -14.62393 | -48.40804 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0d0534f-caee-3dba-895e-8e8f9599e62c | -18.15374 | -44.25954 | 2025-10-27 04:34:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfe05942-244c-37ab-8b08-133636d42a1e | -9.75323 | -50.80173 | 2025-10-27 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README50.md)
