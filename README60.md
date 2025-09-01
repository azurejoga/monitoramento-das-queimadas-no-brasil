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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b01ebd0-dc05-3710-8ca6-8287d8400e3f | -7.07884 | -44.34999 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 07a2c137-80c2-31d7-8185-3346bb5ff828 | -6.17018 | -43.32058 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 368e667a-1947-31f2-92e4-f74d4d8059a3 | -9.68781 | -48.29059 | 2025-09-01 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a646ef55-4cb3-39e0-a9a9-1b212aa66bd2 | -6.34207 | -53.42994 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 936cfed8-c274-332d-bee5-f0024fbaee32 | -6.8979 | -44.38987 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4171d302-a148-35de-b7b8-097e1d73f1ce | -7.38696 | -47.4365 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90ba8b13-a0c9-35bb-89a4-ca35395ff68b | -4.09263 | -55.80906 | 2025-09-01 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9705b6ba-9c80-33ec-a172-39082a8749e8 | -7.57758 | -45.21154 | 2025-09-01 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8a25987-5402-3a32-b1f8-6f8d7ef29f75 | -6.29943 | -43.61274 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2ec9ccee-5214-3f5c-a285-784818e3d718 | -5.72874 | -43.93948 | 2025-09-01 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06e1a948-d477-34ef-8867-473442a74705 | -8.19916 | -46.76855 | 2025-09-01 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 265f36f1-1ace-33c7-a1f2-43d8f11a8dbe | -6.33229 | -53.42899 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 763585a8-b3c4-3e78-9f84-2fbd86920072 | -9.28099 | -47.10793 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90d2a2c5-7068-3ea5-9301-cc4f1faa5076 | -6.63354 | -44.38029 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99134435-64d8-39bc-ace5-f26ceebb73ed | -7.38309 | -47.43948 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 244b0cb8-00db-3e57-a26a-385e320253c7 | -6.2895 | -43.29902 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ffa10232-3dfa-3d0d-83fb-b810b91c6708 | -7.66337 | -49.8508 | 2025-09-01 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5821186-656a-338c-a863-bb603e846be0 | -4.15069 | -46.78814 | 2025-09-01 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 998718a7-9b92-3b2f-83cc-2d59504277c6 | -6.33727 | -53.433 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c210be8a-ea1d-3575-9865-5b128404d121 | -9.6348 | -46.60128 | 2025-09-01 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2ae34ef-9712-3ade-bcc1-d5847b2a191b | -9.26415 | -47.1276 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5b2df40f-0308-3b59-9a49-b2f570add563 | -10.04899 | -48.08529 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a035963f-78d5-39ff-b96a-81bb6af95a64 | -7.94499 | -46.41434 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 368fb156-9794-3d5a-ba52-96eb4c98bfca | -6.53229 | -42.95843 | 2025-09-01 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ae3d4dc-3dc1-385c-b7ce-5217ade613f1 | -7.41756 | -44.80709 | 2025-09-01 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a132cc71-2333-3caa-bcf2-f33ade9eb125 | -7.07818 | -44.35439 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6d5ddd4d-994b-3b46-887b-1f03213d2edf | -6.16476 | -43.99693 | 2025-09-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23466aa7-75b6-32e7-a784-f151690da0d4 | -6.43643 | -55.63272 | 2025-09-01 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e53640d4-e787-3e5d-a705-e9cf309e1fbf | -9.14252 | -47.95665 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| baad1dc6-e9a9-3de1-b1ca-4e1dbb35cba2 | -7.98841 | -44.05527 | 2025-09-01 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c087f5d6-7e17-39cc-8bcf-e2e8d972dae5 | -7.07687 | -44.36317 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f3c66f60-7a1a-3f3b-95df-95ebdd42ff12 | -6.8355 | -44.24865 | 2025-09-01 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddafd15d-82c1-33e7-aba3-1f7dcad0fab6 | -7.70318 | -50.27945 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7db7fa16-5323-33d2-b4cd-e07a2c98bd1c | -8.35481 | -52.53267 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55e01f6d-42ae-3209-b5ba-b52305a93214 | -4.15491 | -46.78173 | 2025-09-01 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12bf03fe-6eb1-33da-b9c3-e3cfed754452 | -7.06067 | -46.24442 | 2025-09-01 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2ecefed-e5bc-3d54-a397-5eb988dca3de | -6.93709 | -42.01715 | 2025-09-01 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f41862be-14ea-3b6d-90b5-828eb862bc59 | -6.79934 | -52.80508 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a0f461bf-265d-3d17-bed0-77cadd1cd050 | -9.62611 | -47.79472 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 215a43bc-17e6-319f-bcc7-1e678eb604bb | -6.16332 | -43.3397 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e18887c-2da2-383e-981f-0b9501103301 | -7.07032 | -44.33062 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f76cb7d-2c6b-303c-8673-ba0ce79f171c | -6.84124 | -52.82288 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2351c49c-b80e-38cc-af7a-7d8b0939a4b9 | -8.84193 | -47.79388 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aea72cd9-90c8-3a6f-8ebf-f9a46bb4a519 | -6.42868 | -55.6202 | 2025-09-01 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 204c2400-39de-3c22-a6ef-beaf5e3d4ded | -6.26335 | -43.5507 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5222f08-89ee-3c4a-a6fa-c7b5ca8d8e49 | -10.01911 | -48.36438 | 2025-09-01 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0560140a-2fb7-358a-8cd6-042437ae00db | -6.56871 | -43.70548 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d6e8bc18-533f-3bd8-ba1e-aec1a6f33ca0 | -5.64019 | -51.08186 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 966e3d42-ffce-3010-a474-3957c4f728aa | -6.15317 | -44.12415 | 2025-09-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d62db574-d8cd-3238-abb8-d4382172350e | -6.64758 | -44.26118 | 2025-09-01 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4fbad2e-2ccc-32fd-8d43-7908c9364ee4 | -6.83104 | -52.81059 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fef91c96-5cdb-3b2a-ba3d-5f40d5c480dd | -6.09684 | -43.19493 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5df89f62-c505-369b-a177-d1eb0734ffea | -9.67006 | -47.04005 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c540a81f-41e2-399c-9cc4-c4b0c6f03e7b | -6.86053 | -52.80482 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0736756c-0a47-3e73-ac74-5b29b23eca13 | -8.84409 | -47.51643 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b7009813-9fde-3293-ad22-5d1cfc8e1703 | -6.36735 | -43.55352 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3074fa76-e3df-3595-8e3a-ece4f7588e9d | -7.94845 | -46.46014 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05bcc144-ee7e-3043-aaea-6e4dc0af3788 | -8.08043 | -49.93984 | 2025-09-01 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 268250d4-7a79-3883-9efa-3d0287fb90a7 | -6.46784 | -42.4334 | 2025-09-01 04:32:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e3040ec6-5a68-3f1b-9d72-cff2df6417c2 | -6.14208 | -43.32161 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 36886715-c080-3a36-9c3d-c6e3408119b3 | -4.92081 | -43.18478 | 2025-09-01 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d25be8b5-86e9-3456-90dc-141119dbad06 | -6.33852 | -58.18702 | 2025-09-01 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a267212c-fc45-34ec-86ce-4ec457ed8bbf | -7.75872 | -50.32364 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 710b6e52-4e55-32db-956f-17c5029c0760 | -6.99961 | -44.35806 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10544087-6379-318e-8aa3-74646aceb0ed | -4.484 | -48.12082 | 2025-09-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04f9f269-eeae-36d3-80ad-4f7b70bd1761 | -9.23536 | -47.06741 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aac66c3a-c6bb-3462-b1f6-5adf07320671 | -10.05176 | -48.08938 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6704510d-2a24-3229-ae8a-b9c095ded1ce | -6.28875 | -43.30398 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56b296bc-7b84-3820-86bf-0a74d8e8bbbc | -7.40412 | -47.43563 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e827bd3-4db6-361c-98d4-4fed3641f82b | -5.72964 | -45.54474 | 2025-09-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c87d058-4bfa-366c-8edb-b456886a9c7c | -3.80989 | -48.95506 | 2025-09-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d44291ea-d4f6-3df4-897d-f1fc162fd01b | -6.78659 | -44.63007 | 2025-09-01 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6b4bcc3-0d89-3cfb-a07e-6b1813832804 | -11.07879 | -44.74125 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13ebd508-6c56-3589-81f6-8f4c7aa2853e | -9.73788 | -47.1404 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd8c29f7-5d5d-37e0-b403-469548b365c9 | -11.06142 | -44.6454 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 395e211c-be65-3fea-bf22-ac6b09c582f1 | -8.83735 | -47.49364 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 074e9ae7-554b-3713-85eb-370822154010 | -7.40079 | -47.4351 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 905e4047-6c39-3d47-b911-b683edb1c0d1 | -8.884 | -47.21262 | 2025-09-01 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a967ff4-0ab2-36d6-8ee1-050c31d2d843 | -6.33596 | -53.44061 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73ac5bea-74fe-303e-803c-6e9e7447c19d | -3.68021 | -49.19407 | 2025-09-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fc8d6b65-615c-3d4e-b899-af6ffae32ab2 | -7.10699 | -44.55814 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d49b8290-fe08-35c1-a141-2c3d3422c628 | -7.62717 | -42.65369 | 2025-09-01 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| efa6caa6-6795-3aab-b40c-8dd1beb3a9f9 | -6.32876 | -53.42445 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 660657a7-9cd0-3410-a00a-874752732d70 | -5.35973 | -41.14842 | 2025-09-01 04:32:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 366f9db7-f07a-3c50-b8c1-65bc99d28d68 | -7.3936 | -47.43755 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93ccb0f0-ed83-36ec-992b-ab80b1f057bd | -5.75202 | -43.68136 | 2025-09-01 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c68632c2-4d39-3be4-925c-03f46f58eba5 | -6.57709 | -43.70192 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0899f320-be50-3aeb-b227-455342ecd272 | -7.8865 | -46.99678 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8737fe8a-a4c1-3e0e-bd26-f935d49b9433 | -6.4974 | -43.56529 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9c7d4409-3f53-33c2-b85b-17aca139d7fd | -9.7088 | -48.3083 | 2025-09-01 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| caf1b51a-265b-373b-93bd-dd2873a4a8c7 | -6.15403 | -43.34843 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cbeab474-1f8d-3d5c-94f9-e04d6dccf75a | -7.10924 | -45.34702 | 2025-09-01 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cb35d43-816e-31eb-b21d-cf5fd6f528de | -5.99127 | -43.36716 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 393f7fb8-c1bc-3b02-9ea0-22582b108e75 | -9.66839 | -47.05108 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30adf349-56d5-33af-be24-e41612441a05 | -6.28318 | -43.2878 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0283e0f-1d43-351e-aa0c-eb771c122078 | -6.4296 | -55.61491 | 2025-09-01 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ca41bad-56e6-34e2-b271-e0a2cef9d3b9 | -4.12548 | -47.66068 | 2025-09-01 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33860446-f2df-3d39-bd23-4c84f829dd03 | -6.16627 | -43.32002 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d4d8f95e-9586-3ba8-a116-74b5198ae6de | -8.00823 | -44.05348 | 2025-09-01 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 972fac12-cb1e-3c2d-84ef-2c7785db5282 | -8.84463 | -47.5129 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |


[Clique aqui para ver as próximas entradas](README61.md)
