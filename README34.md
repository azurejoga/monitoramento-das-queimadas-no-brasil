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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b728ac6-4e9b-3675-9aaf-7318bca05fac | -3.35366 | -53.222 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a951ce56-cb9e-3ecb-aff1-548a3cb7ee2d | -2.46034 | -49.37262 | 2025-11-08 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9cbdd850-0412-38c2-b09c-874fc4a48df5 | -3.09994 | -50.32889 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba05767e-e5be-3bf9-990f-c1bf4b9461b4 | -1.09572 | -47.51927 | 2025-11-08 04:55:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 154fcc62-868d-3d78-bd72-3cdfdd74110e | -3.60704 | -43.51501 | 2025-11-08 04:55:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c83578c3-c55b-3c7e-8e1e-9920dfa1435b | -3.76827 | -50.61077 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6fadece-dd47-3a64-b531-41113907fce7 | -5.41584 | -44.82713 | 2025-11-08 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c42e8868-087b-300e-93f4-4fc52bbede02 | -3.06833 | -49.37291 | 2025-11-08 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3d10d79-0202-3c01-823b-7fe79693b6d3 | -4.02939 | -49.27182 | 2025-11-08 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6a67f4d-575b-3000-85dc-187749984d9c | -4.38493 | -49.67296 | 2025-11-08 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b87ecbe-c9f6-32b0-8cb2-b796c807e649 | -4.80574 | -45.39976 | 2025-11-08 04:55:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4259d1a1-b3ff-30c6-bff5-4802f0823ef7 | -4.72515 | -42.9422 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f237dfa7-0429-39d2-b199-411e44422086 | -3.98192 | -46.03307 | 2025-11-08 04:55:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 124a7864-56ac-3e7d-bc50-4fc8c572ac98 | -4.81409 | -45.58184 | 2025-11-08 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98563a75-a3c0-32fe-a981-d5cc79e3e717 | -3.82987 | -52.19887 | 2025-11-08 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d2110ffa-4f7d-344f-94ea-55f644fac30b | -4.34017 | -45.53578 | 2025-11-08 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db6a9574-7673-34f0-aaf1-d64bdc1cad60 | -4.44897 | -46.43982 | 2025-11-08 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7810627f-1809-3d95-864e-f41cc2b17ee7 | -3.43889 | -52.63668 | 2025-11-08 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5348acc3-107d-3bdf-bf14-14c912e69d82 | -4.35895 | -46.81583 | 2025-11-08 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b42cd1c-19de-3e87-9453-d6544ab35fb6 | -3.61426 | -52.12159 | 2025-11-08 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c339536-a0a4-33b1-b6dd-7d5308679f0c | -2.70933 | -49.54305 | 2025-11-08 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6ba94846-7fcc-357b-b47d-40df99e86d42 | -3.69778 | -49.94674 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8e22d0d-3ec0-358d-9da9-616dd388701b | -3.40381 | -45.43359 | 2025-11-08 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 02c3f745-2012-3acf-b344-539be7dd5c29 | -3.31768 | -50.3115 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 098bd6bf-d559-3790-8cd5-db6ffa1a15af | -4.71698 | -42.9385 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 65d7a9b4-9b44-30b6-b47e-ee96b3730622 | -3.71844 | -42.72486 | 2025-11-08 04:55:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cdd84cf-5d77-38da-bc00-82f2733891a1 | -4.97721 | -44.82057 | 2025-11-08 04:55:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc71ee79-0a23-32a4-bef1-89322ea503e6 | -3.47694 | -49.9315 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45eb0c55-eb20-3779-9231-2d3838fa0536 | -3.24939 | -52.91298 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54b3dcd9-44ad-3470-84ac-1957e1fd74cb | -3.12152 | -50.14482 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ab636e07-623d-328c-8e03-a5295a6ab64c | -2.6241 | -50.07438 | 2025-11-08 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc012043-2ee0-3527-ae3c-5f59276494e0 | -3.44382 | -50.21828 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbc79c84-8d7f-3676-84a2-3a3f674dca3a | -3.9821 | -46.03016 | 2025-11-08 04:55:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8977dc5-cf36-34ce-ac2b-97b13b5ba16e | -4.46728 | -45.5064 | 2025-11-08 04:55:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec8e03e9-90d2-3c5e-b4da-66ecee29d440 | -4.44576 | -46.4411 | 2025-11-08 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e659791-04c8-30cd-90ca-67e3cdde6ff6 | -1.57853 | -53.78872 | 2025-11-08 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5310f47-2aef-3a51-bfeb-f891e352b54d | -2.55143 | -48.39477 | 2025-11-08 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9a1d9d1-2ecf-3c43-827a-bbcc565097c8 | -3.03715 | -50.3066 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e743b733-2d99-33fc-a353-253c3ed8f8c8 | -4.4629 | -45.32777 | 2025-11-08 04:55:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90fa0b2b-05fa-3ff7-909e-5959292cb043 | -3.33441 | -50.19542 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ada3378f-7e54-3e90-8c58-4f78602a4aff | -4.96817 | -48.02003 | 2025-11-08 04:55:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fd090326-7ee2-30b2-8c2c-b2d0f8e13c00 | -3.43834 | -43.1642 | 2025-11-08 04:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81583ddd-d72e-3ec0-bef4-fcce20bd9bd9 | -4.38458 | -45.36761 | 2025-11-08 04:55:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a2d9535-5cba-37c0-a31f-91f1fbcc19a2 | -2.82679 | -49.82896 | 2025-11-08 04:55:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4173948e-026f-3f15-8110-0c02ede4038a | -3.40376 | -50.45849 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f14de08c-6f2f-3250-812e-bda16f056e4d | -3.41324 | -52.19338 | 2025-11-08 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da96bf9a-516c-3072-80b3-8c31c2a84073 | -3.67326 | -50.45121 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23985e38-d68a-37c8-b626-60ad7e3bc70e | -3.43603 | -45.59204 | 2025-11-08 04:55:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ae17d5a3-2b5a-308b-87bd-2be883dbc622 | -3.44558 | -43.15415 | 2025-11-08 04:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c09d9cb-7381-31d6-bc88-afe6b27f8d54 | -3.44319 | -50.22247 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90e73db2-169f-3340-8c2b-256cc4d2b138 | -3.28126 | -49.77089 | 2025-11-08 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76bee39b-e79f-3e9e-ba22-0cc299dbaecb | -4.11295 | -48.01827 | 2025-11-08 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d798d95-0313-302b-9742-0a69eceb602c | -3.91516 | -50.04273 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5850620e-1da5-333a-b472-b741cc9ab1fa | -3.31585 | -50.12359 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45efdefb-48bb-3b23-bbfd-52c1e9b4510d | -2.43754 | -49.3459 | 2025-11-08 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1cfad6b-e094-3eaa-b888-adc2611a5501 | -4.72453 | -42.94671 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 04f30f19-8f89-33e4-8c07-e88f63712630 | -3.44649 | -43.14874 | 2025-11-08 04:55:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39b50f68-f754-3695-afc8-b5c43f2516d9 | -4.45043 | -46.44203 | 2025-11-08 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2c72ee6-2916-3639-9900-426a7efd015b | -4.2402 | -51.22947 | 2025-11-08 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45a530b9-e68c-32c0-af33-57365f4123ff | -3.84537 | -49.81297 | 2025-11-08 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fe16dce2-223f-3ccd-9f51-0b656330d6ff | -3.10508 | -50.20228 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb37ff2a-9699-3503-8ce2-8286639f54aa | -3.60447 | -43.5155 | 2025-11-08 04:55:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| be8f81f7-8843-3385-9e4c-aba504b21380 | -3.42207 | -50.04243 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73ef2d6e-a809-3912-99de-3c96bae96478 | -3.5851 | -51.25128 | 2025-11-08 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e2d6ac69-176a-3682-b2ae-31530c482a70 | -3.67687 | -50.45173 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1d13522-4fbc-3b9a-b378-82cf075b4740 | -3.46134 | -50.22526 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1c00246-5ac0-3fbd-b52d-9269544174d1 | -3.47832 | -49.92274 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a86d0f4-464d-372b-acdf-4b5df39f2921 | -3.44311 | -43.17035 | 2025-11-08 04:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3eb25f5b-ca0b-32bb-955a-61144c05f34a | -4.46683 | -45.5094 | 2025-11-08 04:55:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4909a95-3e38-37fc-b8ab-8c368ca82e63 | -3.35162 | -50.20991 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f0cd8ff9-85f2-31c1-9559-64a8ce0b88b2 | -3.33442 | -50.10025 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2d24644-1adc-3174-b729-af7baa92e55b | -3.14488 | -50.28833 | 2025-11-08 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 685f9ad4-091b-3639-9c41-16c268c5b77d | -3.64747 | -49.86423 | 2025-11-08 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ea928bc6-7969-3fd3-a716-d7dbf8d9d5b6 | -4.72892 | -42.94041 | 2025-11-08 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ccf649d-4bcf-3a95-bf45-2a00c63de6fd | -3.92253 | -51.01672 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5e03620-969c-3799-a6be-cebcd1b74031 | -2.71326 | -47.40887 | 2025-11-08 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1ad3ccd-2fb3-3943-a6db-28328defb4e1 | -3.44363 | -50.24406 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42b1034a-f402-3a76-a0c0-1e40b3fad644 | -5.77725 | -40.7997 | 2025-11-08 04:55:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0f91ebf3-4078-39e8-87ba-5e9b1f36b58f | -4.39159 | -45.36454 | 2025-11-08 04:55:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5125519-2a2b-3964-ac9c-8428ce2915f0 | -5.23126 | -45.53247 | 2025-11-08 04:55:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f06aaf11-53d1-3c0e-8fcd-c3774b1aa06a | -5.86152 | -44.70847 | 2025-11-08 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 738ab757-c8b2-3b6c-be18-1cc947535322 | -4.49663 | -45.13472 | 2025-11-08 04:55:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdde4a90-377b-3934-b0ef-58134d30eb1a | -2.94551 | -53.288 | 2025-11-08 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0d57af2-0a2f-36f0-a5ec-d439fdc49deb | -4.26565 | -48.55972 | 2025-11-08 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8188e55-0d46-3f8f-ace6-5457de46ea65 | -3.05108 | -48.72174 | 2025-11-08 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f937a01e-7907-34ed-8aeb-a42057aa99d4 | -3.91082 | -50.04649 | 2025-11-08 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 60d28029-4386-3bb1-a8fb-81038ce236b4 | -4.90914 | -45.10408 | 2025-11-08 04:55:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de988720-e3ed-3873-b6de-053b20fc4882 | -6.51879 | -55.03722 | 2025-11-08 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89df62b7-82a6-3184-8466-da9d93dffab3 | -9.38579 | -50.72856 | 2025-11-08 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cc2569e-a342-310b-9b45-ac3fda5684b2 | -6.22124 | -47.0165 | 2025-11-08 04:57:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d6762b1-fd80-389c-b0d1-8413b3dee4ae | -7.5501 | -41.6665 | 2025-11-08 04:57:00 | NOAA-20 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 1006f10c-b27d-3050-a149-962fbf662cd8 | -7.92925 | -55.01584 | 2025-11-08 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 791eb99a-6fda-3d80-8bfc-fa3ad33a8ed6 | -9.05134 | -46.99979 | 2025-11-08 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26c14887-9361-327c-8488-003548a86303 | -9.46359 | -47.87212 | 2025-11-08 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbcb4703-d13b-31f2-9df9-2685d92267c4 | -9.05676 | -48.83742 | 2025-11-08 04:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3028f91b-b121-3e43-bbdb-e701a7e35991 | -10.11279 | -47.514 | 2025-11-08 04:57:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d08633ce-022f-3657-886d-eff08b8202b0 | -6.13112 | -52.63846 | 2025-11-08 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94b48650-d8bb-3274-ad51-e23fa2cceceb | -10.55441 | -55.94463 | 2025-11-08 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2b1dcd9e-d4a0-3b32-afc6-74c3e3731110 | -10.98814 | -53.98601 | 2025-11-08 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68d072c2-f7d1-30d8-847f-b021efaa5774 | -7.77742 | -50.8023 | 2025-11-08 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README35.md)
