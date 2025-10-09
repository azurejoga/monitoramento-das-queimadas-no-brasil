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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8b31e39-0550-3fd9-9931-a2dc8e4432fa | -7.50115 | -42.72814 | 2025-10-09 04:17:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 42d86108-f3d7-3452-abf1-3753214eaa05 | -6.74101 | -42.82341 | 2025-10-09 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 078ff4f2-8ca3-3dbd-bc61-f7b6c7345c33 | -5.44344 | -44.82854 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1e591d8-1062-30de-946a-8e94b0e2f501 | -5.33761 | -45.51212 | 2025-10-09 04:17:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e0789e4-82bf-30b5-a492-6bc83868e0ff | -6.646 | -40.87528 | 2025-10-09 04:17:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c05df803-e46a-3f08-a021-9cd7d65d4f32 | -5.35173 | -44.91328 | 2025-10-09 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79663cdb-ec26-35b4-9910-86be0964d7fa | -4.49716 | -46.35419 | 2025-10-09 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| dd89cd07-8abf-3819-9019-affe77191217 | -5.71905 | -42.7701 | 2025-10-09 04:17:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| cf8174e2-09e2-3afa-81f6-76b986b3f88f | -3.95687 | -49.89172 | 2025-10-09 04:17:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 523a0783-e245-300d-8a9c-a15b6da9f26a | -4.45363 | -43.22021 | 2025-10-09 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 218935d5-2514-37cc-89bc-7773470353c5 | -2.96012 | -48.95992 | 2025-10-09 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bf39fb4-b738-3ba7-a3a9-5f653c2847e7 | -5.41609 | -41.3395 | 2025-10-09 04:17:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 94b140ab-f160-3c65-b5d3-f50f05f5d60a | -5.33425 | -45.51161 | 2025-10-09 04:17:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a5389229-da8f-336a-a998-03a0efa17bca | -3.0018 | -49.77494 | 2025-10-09 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83f1b27f-a9f6-3f79-9b0e-f25e129c94af | -4.50063 | -46.35473 | 2025-10-09 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f384b9e-06bd-3f7d-a52f-fbb6040db985 | -3.26206 | -50.12074 | 2025-10-09 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c8ab5dbf-91fc-3545-a369-ccbcd3e715d8 | -4.45199 | -43.23069 | 2025-10-09 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6acfa3d-1f7b-3918-9640-7aff1466ca9d | -6.45864 | -44.57478 | 2025-10-09 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2bab5cfa-e698-3852-b5b6-ea6dbe302ea9 | -7.05311 | -37.69514 | 2025-10-09 04:17:00 | NOAA-20 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b879971a-3351-3fc5-a6cd-56041bc653ef | -7.02471 | -42.86661 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8c16e5ea-09cc-3817-9268-d3ff4bea92fb | -5.39997 | -40.98643 | 2025-10-09 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a33f1bd9-0a19-3eb2-9a3a-4d9025111568 | -7.48558 | -43.10513 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c8d61aed-3d61-3839-bd06-c1675f6fc54e | -4.77357 | -45.59484 | 2025-10-09 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a0ac584-170b-31c9-baf6-99ed6ede6a49 | -3.89194 | -44.90781 | 2025-10-09 04:17:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4b44b05-5563-3921-ab1b-6c23e796121d | -5.20731 | -37.63023 | 2025-10-09 04:17:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 18e73b9d-50c3-370c-8fa0-c8e025c0bb73 | -7.351 | -43.86472 | 2025-10-09 04:17:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77235b97-df57-3b44-abcb-8dee494d1378 | -5.13003 | -46.25457 | 2025-10-09 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef6109d6-d2b9-3377-8732-f9226f102aca | 0.34647 | -50.95273 | 2025-10-09 04:17:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e676bfdf-863f-3583-9df4-c5c89401bd32 | -7.0179 | -42.86555 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| da06e4e0-eb5d-353b-82df-472151914199 | -4.22914 | -47.78561 | 2025-10-09 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7be1d66-8908-3d2b-84d5-87fc08e4723f | -5.639 | -43.60837 | 2025-10-09 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1b36206-32d9-3bd9-8402-97403cd3ec6c | 0.89235 | -51.13845 | 2025-10-09 04:17:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc879ed9-9ae2-31bc-bb2b-61c8fefdbc39 | -6.50552 | -44.14694 | 2025-10-09 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed9a3931-5719-3767-b593-c6acdb863a71 | -5.60842 | -44.1928 | 2025-10-09 04:17:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3bf5b8b9-44a2-3b6f-a7ef-6aeafaa29f81 | -5.12719 | -46.25035 | 2025-10-09 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78421b70-9c5d-3e9f-be7b-ce56fd5cb78b | -6.94888 | -45.55079 | 2025-10-09 04:17:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5f2c64e-205a-3879-b156-fcd5fa347297 | -3.96113 | -49.89251 | 2025-10-09 04:17:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9017c2b7-c3be-353a-a172-e44d86212367 | -5.71622 | -42.76602 | 2025-10-09 04:17:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8d406c99-e801-3015-b9cd-3c0b10e02466 | -3.90629 | -44.34407 | 2025-10-09 04:17:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44dcc94c-00c0-3739-b75a-420675b429fa | -7.01733 | -42.86924 | 2025-10-09 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 70b6d069-9c94-3d08-8ed4-2e4be0788c91 | -6.92895 | -45.57297 | 2025-10-09 04:17:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ea3e03f-f4f7-3897-ab81-55ebd854214c | -5.20281 | -37.62959 | 2025-10-09 04:17:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c798ef0c-2200-3fb7-8708-317e83da5391 | -3.95991 | -49.89163 | 2025-10-09 04:17:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f931c5e-382a-3bf0-a9f2-459ce930c0a3 | -5.15207 | -46.05289 | 2025-10-09 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76d7d34c-d859-31e7-9108-1f077d407782 | -5.23711 | -45.80486 | 2025-10-09 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fd33b67-c5ed-3480-9161-be4e732c6e9f | -6.39522 | -47.71705 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2ad0f9d-44f4-3357-bf40-82e6cc6d849e | -4.27455 | -48.88102 | 2025-10-09 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a13b6f4-7400-36b5-9e9c-161cef303774 | -5.63596 | -51.08488 | 2025-10-09 04:17:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8aa72742-bdc6-3cf4-8b5b-e095bf62661b | -6.68644 | -46.30278 | 2025-10-09 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5f2b3ae5-3730-349d-b116-64257fa4d27f | -5.6439 | -45.04226 | 2025-10-09 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a505a01d-9bbd-33c2-a079-cbd38362b0d0 | -4.98866 | -45.12421 | 2025-10-09 04:17:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 776e443a-85d7-3a7e-a1b4-ac8aa41a09de | -4.73386 | -42.79677 | 2025-10-09 04:17:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d66ce65-43b6-3dc5-a9d1-2b4612b2658d | -4.25776 | -48.56705 | 2025-10-09 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e11f486f-c01b-35e2-b5cf-cbe201a59597 | -4.68832 | -45.83838 | 2025-10-09 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79b13a0f-67e9-30ce-b4ef-5b12d3f3ea9f | -6.73248 | -42.81078 | 2025-10-09 04:17:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 968c18e2-726e-3da0-816f-99e0f7a613e8 | -5.02808 | -45.13404 | 2025-10-09 04:17:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee50d4e4-7433-37d3-8d6c-3d77d23f3099 | -7.48377 | -42.72949 | 2025-10-09 04:17:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 28be6c82-d1e8-3d88-8c1a-4e18bfa35886 | -3.8606 | -42.90918 | 2025-10-09 04:17:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dff7c798-12be-3d1b-bd56-430dcb4a3031 | -3.69764 | -49.56714 | 2025-10-09 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b3a9e48-0a55-36e8-9132-cae89e6826fe | -4.69229 | -45.83528 | 2025-10-09 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 579fffc5-9d06-31b7-b688-2d0ff263e4e0 | -4.89579 | -42.2519 | 2025-10-09 04:17:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4d2f0669-89c0-34c4-9d25-4ec0372aaf32 | -7.02594 | -42.79108 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4869aecc-d157-39a4-8ca5-24b3e4ef0ead | -5.9297 | -43.96397 | 2025-10-09 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a954830b-2500-318f-88e2-cc08507b48b4 | -7.53677 | -42.03303 | 2025-10-09 04:17:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bd4cfda5-e6cb-396b-bb12-eb1f691402c8 | -3.09583 | -47.0116 | 2025-10-09 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16c12358-67f6-3fe1-8ac9-4cf4309a49a1 | -4.98922 | -45.12072 | 2025-10-09 04:17:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a57e3723-4ba7-3ad6-8e3c-0472202a94e4 | 0.89279 | -51.14136 | 2025-10-09 04:17:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 355cd306-21d5-308f-87b6-e60a4bb108b8 | -5.45898 | -47.43911 | 2025-10-09 04:17:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 19e6eb21-f846-3c74-a736-55c5acec834e | -3.13931 | -49.03636 | 2025-10-09 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 09f48747-f09f-3084-8bf2-084b85044786 | -5.30879 | -45.37656 | 2025-10-09 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a766ff8-0916-3eaf-9884-434c262705db | -5.60787 | -44.19625 | 2025-10-09 04:17:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8109d3f-2bf3-3006-83f7-2cda86955a6d | -7.06886 | -42.76332 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bef8339e-d11c-37ba-8a99-1213c6f2546d | -5.25329 | -43.1458 | 2025-10-09 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f1afb65-a511-3299-90e8-19e037370c89 | -4.3564 | -48.72433 | 2025-10-09 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e4dd694-748e-31e9-bcd4-c6ad86c3a594 | -7.42019 | -42.9824 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3be6f3af-c61c-368b-9ee6-eb2f21c07af6 | -2.88169 | -50.73197 | 2025-10-09 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c7bd078-0eab-3af4-a2e4-ccd90b08c16b | -4.01176 | -43.28711 | 2025-10-09 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 974e698c-3559-3f95-ba9e-061e42ac26d1 | -7.5233 | -42.00222 | 2025-10-09 04:17:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 576b46af-89a7-31a9-b96b-474c7114cbbe | -7.02483 | -42.753 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1471f32d-33f8-3434-be94-8c75cca5ce04 | -4.51515 | -37.92682 | 2025-10-09 04:17:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 08774dd6-2e4f-388b-8abf-4b4e00d42012 | -3.86394 | -42.90969 | 2025-10-09 04:17:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b76dcb4-7f2b-393b-a0e1-46692a80122e | -7.01509 | -42.83865 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3e1e5de9-a2a5-3a1c-9a23-83c79089c3b7 | -4.44588 | -43.22617 | 2025-10-09 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6942ad07-f4ff-34fb-8458-6ccc5c9fe3a1 | -3.39354 | -50.1441 | 2025-10-09 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 850db2d7-92a8-3680-9a35-eab0fe3cb565 | -7.14297 | -42.17856 | 2025-10-09 04:17:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a68b9bb6-8e47-33d0-8bad-c2ac21aa482e | -6.72691 | -42.87005 | 2025-10-09 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 20847a21-aa60-37ba-b635-9a5058e9de46 | -7.4589 | -43.02958 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f9cebf2e-d0fe-3396-9494-e434c36fe3ec | -6.42206 | -47.22546 | 2025-10-09 04:17:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c64bd89-b493-31b1-87cc-af234c682b85 | -4.48963 | -46.35686 | 2025-10-09 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2abe0a04-d7ed-3ffd-aa57-b9e30441eedb | -5.71825 | -43.64572 | 2025-10-09 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f2fb6541-963a-3c40-ab6d-8b24aef8aa49 | -5.04682 | -45.63472 | 2025-10-09 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e4b47ab-4b2b-32dd-9b97-a3f066a5c69e | -5.72761 | -43.60784 | 2025-10-09 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ec4cb06c-75c6-346c-bfe0-d80f8a565c66 | -6.5724 | -44.1534 | 2025-10-09 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3bd2f97-a1d6-3b17-bfb4-56e176797e9f | -5.48658 | -42.88998 | 2025-10-09 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 88a40049-82a1-3fef-a479-db5465e9e1eb | -7.01229 | -42.74346 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8433f979-9ce9-3da1-bf7a-3b1daf82758e | -3.89414 | -44.91204 | 2025-10-09 04:17:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc075634-7ee9-356b-9df1-615399b0b3b1 | -5.4849 | -42.90076 | 2025-10-09 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9ff8d035-8ac2-3926-a389-cf4a572d6af6 | -5.77234 | -43.49308 | 2025-10-09 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ff6200e9-612f-3776-885d-56e6f2a86d07 | -5.31157 | -45.38061 | 2025-10-09 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f426e49-7e0b-34d1-9f81-ebcc48013291 | -4.49655 | -46.35803 | 2025-10-09 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |


[Clique aqui para ver as próximas entradas](README34.md)
