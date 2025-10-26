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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fe05a76-db01-313b-974e-343905880587 | -12.76424 | -48.62965 | 2025-10-26 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8694b0a6-84b7-315c-be0b-a2e4a2116eae | -13.88719 | -48.4154 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2b2ab9f-a022-30c9-a6fc-6d087e4d6bf4 | -12.45239 | -54.30377 | 2025-10-26 04:51:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e37c7b6-12b2-315d-82a7-7615e9ad3aee | -10.84925 | -48.97305 | 2025-10-26 04:51:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67f6edbc-e8d8-3de2-bc30-e625b2adce10 | -10.86434 | -47.94932 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8916bd4-26ae-3354-bab2-732fbff76a38 | -7.9324 | -55.01757 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbf7068b-4e48-35d0-b985-058c75bc8293 | -6.80853 | -49.35487 | 2025-10-26 04:51:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aba70486-43e8-3c88-8172-ee71b476bd6d | -10.80589 | -47.86921 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 585688f8-2163-3a95-99e4-0b6dafc6531c | -13.8468 | -44.35888 | 2025-10-26 04:51:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74b08090-0079-3508-98ad-122d6fe41ef2 | -13.85314 | -48.50358 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4792e36f-1d4d-3e16-87ee-9172c73abfa9 | -12.84821 | -50.32486 | 2025-10-26 04:51:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b4012f2-a795-3702-bdb8-8b367a95917f | -10.63488 | -52.18398 | 2025-10-26 04:51:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 57344275-1498-3144-adcc-ed8d09ae5df2 | -10.8318 | -47.62271 | 2025-10-26 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b406128a-921a-31f3-8853-eb8a609c6b61 | -7.40317 | -45.75828 | 2025-10-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91385a56-420b-3300-bbca-5565f94909ef | -13.05886 | -50.28841 | 2025-10-26 04:51:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7ab440e-0a21-3a42-96f5-e32ab466897f | -9.44033 | -46.33821 | 2025-10-26 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b516d5d6-b1f9-348b-ab35-afa37efcb50d | -10.82756 | -47.62207 | 2025-10-26 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f6ecfbc-4b36-302f-bc08-924ecd69f5fe | -10.22528 | -49.84966 | 2025-10-26 04:51:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b54164c-5bd6-3673-b485-d144c314baf8 | -13.26576 | -54.39095 | 2025-10-26 04:51:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 286edacf-d097-356b-9edc-4c74874b257c | -7.69639 | -42.18955 | 2025-10-26 04:51:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8da38f45-d88e-3f0f-b01f-c36524435fc2 | -10.62428 | -52.18602 | 2025-10-26 04:51:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9484cb36-e5fb-3ee2-86ed-023d830adbb7 | -10.97755 | -52.02858 | 2025-10-26 04:51:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8ca556d-9763-3bb7-ab6f-5478ea24cb7b | -11.05039 | -48.31588 | 2025-10-26 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e891715c-d988-34eb-a50a-d4ea0d4476a1 | -12.86494 | -48.65477 | 2025-10-26 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a14d04a-ab80-3055-ab41-adf122301919 | -8.04953 | -46.7438 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 0ca24bbd-4068-3391-90e0-fb273f3287df | -6.81337 | -49.3471 | 2025-10-26 04:51:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04967fee-0eb9-3bb4-a44d-7e0c5dccf96e | -13.43664 | -47.3884 | 2025-10-26 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76b756e3-b16f-3e48-a0d2-c99e172d6658 | -13.8397 | -48.50845 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41e22651-d1f0-36eb-a2f6-ad259ae8cf73 | -7.7711 | -42.92346 | 2025-10-26 04:51:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 98c80ca7-f96d-33b8-9700-decb809696d6 | -9.58077 | -49.68121 | 2025-10-26 04:51:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f63cd9e-b81a-36a3-8459-5a7d16f1a6d2 | -8.48942 | -44.72287 | 2025-10-26 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02c6787a-0c05-3e7d-80e3-e682834df637 | -13.89656 | -48.44225 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 205d948c-8204-3cc5-b232-49402a27a838 | -12.32051 | -47.48438 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bdb7d0d1-d626-34f6-9204-395e16ab165d | -10.9473 | -48.07009 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9b7837aa-a154-38c9-a840-7ee9995553fd | -10.94262 | -49.48229 | 2025-10-26 04:51:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c60618b3-0373-37b7-bab8-3a8e0a775727 | -8.03134 | -41.20183 | 2025-10-26 04:51:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6117bcb0-ac35-3133-aaf4-036e3f2bd8a8 | -8.10625 | -44.49517 | 2025-10-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd3993fe-61c7-3078-9378-ded5275ce44c | -8.60637 | -54.65686 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| b09403c7-555b-3469-bfb1-5103fcf1cdcd | -8.53671 | -47.20315 | 2025-10-26 04:51:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0fec5731-e0d2-3a90-a552-06d9e446bf1c | -12.1718 | -47.01329 | 2025-10-26 04:51:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c255ddb-877d-3b90-a74a-3657818a0d91 | -10.4119 | -45.32357 | 2025-10-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f6ecd56d-b881-3ee7-9586-eabdfc58db84 | -8.49401 | -44.72669 | 2025-10-26 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b46c698a-28af-3885-80d9-8c7814f4e02c | -9.58062 | -49.67969 | 2025-10-26 04:51:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2f0bd94-fd58-312b-82fe-de076db4d4ac | -7.38077 | -48.08243 | 2025-10-26 04:51:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9daf509c-a1fd-319d-a3ad-dddd627c3dc2 | -11.6781 | -49.06362 | 2025-10-26 04:51:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4abf4eff-b3b9-3209-84cd-24569e370beb | -8.53821 | -48.98269 | 2025-10-26 04:51:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 586ce4e2-dba8-3d44-b102-1746346ac794 | -8.72729 | -49.60791 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04186a7a-061a-3972-9927-5db834371689 | -10.88462 | -47.95601 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32a3e1e0-083c-3dcd-933e-bb20a63e8762 | -11.47249 | -46.12412 | 2025-10-26 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be600696-ef7b-3eda-9824-3d0199d37399 | -11.67404 | -43.90476 | 2025-10-26 04:51:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71f62826-e39b-3ab1-ab25-9c6d0ac56977 | -7.69544 | -42.18839 | 2025-10-26 04:51:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8ae9b990-087d-310d-8af0-fae9f4e8e11d | -11.26974 | -54.18533 | 2025-10-26 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28b2a6be-5dea-3fa8-a06d-d505ad00e1a3 | -6.63024 | -49.19215 | 2025-10-26 04:51:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca35c77a-435d-382e-a4bc-49e3b348a04d | -11.44082 | -54.09479 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 276058e7-d228-3007-9a0d-e4a856049b73 | -7.48955 | -46.96876 | 2025-10-26 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68f22b28-33b8-3565-82f3-e7978dbf65fc | -10.9817 | -47.88187 | 2025-10-26 04:51:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c1d754a-e6b5-3cda-895c-4a85f105e4b1 | -10.63153 | -52.18346 | 2025-10-26 04:51:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2629a6e3-7b95-3d08-8ff8-d53fd914a26c | -10.41341 | -45.31245 | 2025-10-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7cd5d3f0-cabb-3738-a011-9cea51f6adad | -8.15705 | -47.75381 | 2025-10-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e8c58660-b3c1-365b-94c2-53b3987a5a7d | -11.10245 | -55.56039 | 2025-10-26 04:51:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9252db68-6e59-3a0f-8ce4-dfed7aeab849 | -10.21525 | -52.66134 | 2025-10-26 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fd5045c3-3666-369d-b4ff-f4387287b6ae | -13.88561 | -48.46065 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| adde75fa-9f01-3e72-8609-f40ec99b4516 | -8.21582 | -46.9373 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee5a6391-ae00-3754-89e5-4b699801bedb | -11.49936 | -54.62562 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcca5b23-28ac-30e4-96ca-f412b5f3f75a | -11.41461 | -46.0406 | 2025-10-26 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2d2046b-b3a9-3ea2-aaed-6aab75b04263 | -13.84684 | -44.36043 | 2025-10-26 04:51:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbb2c8c1-13c2-38da-8726-f09420979b72 | -12.13857 | -47.02137 | 2025-10-26 04:51:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bcfff14-a86b-3f2a-9232-75dcb7829e11 | -7.42297 | -48.77117 | 2025-10-26 04:51:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a660d32-736d-33a1-beb3-1f6f7841eeb7 | -8.54093 | -47.20378 | 2025-10-26 04:51:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e93d8c05-fe24-3099-979e-8cee0ed49436 | -9.86442 | -50.54387 | 2025-10-26 04:51:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7c83ed1-c7e5-3ac2-b7c9-b611bc336e28 | -7.77063 | -42.92706 | 2025-10-26 04:51:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 953c5a79-6f6a-3481-b319-dcb9940d4c5a | -10.41183 | -44.7382 | 2025-10-26 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0df5711-e214-3083-ac2d-4be1dd02a05e | -9.57261 | -46.91934 | 2025-10-26 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 80fdbc74-6a85-31cc-b35f-a893b46b706e | -6.80757 | -49.35226 | 2025-10-26 04:51:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 09fdcc25-0944-360a-8a76-c99393efbc55 | -8.31093 | -46.81147 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9c2f037-4b15-38f0-aeb0-a483efd746b2 | -13.27567 | -54.39258 | 2025-10-26 04:51:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 828168e1-13f1-3770-8101-30427baee6d9 | -9.0913 | -47.81963 | 2025-10-26 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7864ec30-8595-39b2-85f1-7cfe5a6a7bf8 | -13.63976 | -51.96154 | 2025-10-26 04:51:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4eb74882-984b-39a9-9268-2a8ef7073fec | -13.53918 | -43.00124 | 2025-10-26 04:51:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 36.6 |
| ed47fb4f-b92b-355d-86d8-12588e987af4 | -10.99054 | -47.87964 | 2025-10-26 04:51:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d71c1518-5b04-3d5a-a9d2-a3b3fb322fff | -7.84179 | -46.4368 | 2025-10-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35251c86-5166-3df9-a162-7628edc4f7bb | -7.87763 | -45.71853 | 2025-10-26 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7c867bd-07e0-3ec6-99f3-b6407b5e29e8 | -8.21809 | -46.8287 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23e3d1fe-4822-35a0-b1e5-66d4b5541f0a | -7.56541 | -46.2628 | 2025-10-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f28bcdc3-490f-3544-837e-769586d42697 | -9.6325 | -57.01281 | 2025-10-26 04:51:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a77dc19b-4ab4-3639-8283-11bf03b19de9 | -13.53869 | -43.0056 | 2025-10-26 04:51:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 27.9 |
| fb2f1785-c678-3c5c-bff5-f5df264d0aad | -10.59887 | -47.86528 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fe72866-ce18-3d23-a756-cb5a662577f6 | -8.63049 | -54.89493 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c887ffb-a9b9-34d0-8d78-a0215d93d95a | -10.87558 | -50.13587 | 2025-10-26 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fed7b97-53ca-35f7-8b42-84e0a9bc6ee3 | -8.05107 | -46.74706 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74242c2e-cc2d-3b84-9435-62e3074b7e5d | -9.24829 | -45.6158 | 2025-10-26 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 416be8cd-91ac-359f-bdba-efd42d31624b | -8.73041 | -48.56677 | 2025-10-26 04:51:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f1d10f2f-9a56-3d8c-8bdf-19c6f82b530c | -10.81046 | -48.4257 | 2025-10-26 04:51:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd5444e5-e3c7-32f3-abf1-e0530bbec92f | -12.76478 | -48.62555 | 2025-10-26 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c91462d-973a-3d95-8a9d-ecb6857d9a30 | -13.41128 | -43.55315 | 2025-10-26 04:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2936ac84-3eef-39d0-8e9e-7af4d1027c33 | -12.041 | -54.23634 | 2025-10-26 04:51:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24e60bc0-1f4b-39f8-8649-07109166a2ac | -9.29131 | -57.54633 | 2025-10-26 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9971e706-ed37-3e18-a94c-41572c4f73f4 | -10.61203 | -46.60204 | 2025-10-26 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e451d9bc-4523-37d6-9aed-d37a1b0ba840 | -8.16142 | -47.04488 | 2025-10-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6d67a2e-f09d-3a72-8863-37eaec8f9cac | -13.32507 | -47.9345 | 2025-10-26 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README40.md)
