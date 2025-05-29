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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5eaf868-41d2-3392-abd0-f84e01e91316 | -28.58682 | -49.4421 | 2025-05-29 04:17:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 70e5771c-c91f-3604-883d-46e363115f21 | -25.19103 | -49.32567 | 2025-05-29 04:19:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5ecd648e-3e0b-32c9-a248-0ad0bfbda30a | -24.24169 | -50.73954 | 2025-05-29 04:19:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b8931c6e-6b6d-32e4-9f8f-72f77d74bb74 | -2.65609 | -48.79824 | 2025-05-29 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d208a9d2-77ea-335d-bd44-5de24505200e | -2.44635 | -47.47228 | 2025-05-29 05:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 59178a27-825d-3217-93a0-119943e5672d | -2.65982 | -48.8031 | 2025-05-29 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3b075107-473a-3f83-bb93-5ad278788f0d | -2.65546 | -48.80246 | 2025-05-29 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cac74a3c-59c5-3b87-9c67-cdf386e48e0c | -8.01737 | -46.21552 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3cf60409-709f-3a24-a0c6-2535de75b73b | -7.06788 | -44.92998 | 2025-05-29 05:04:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5fc6c3aa-c226-317b-83e3-76ccbec6bec9 | -6.91395 | -47.85731 | 2025-05-29 05:04:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cdeccaad-8a35-3f61-af75-eb78490f83e8 | -4.23372 | -48.97203 | 2025-05-29 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ce1e604-37d7-338a-9fc9-cf4687586ead | -7.23992 | -43.09533 | 2025-05-29 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| d856fab3-a608-3b84-89e9-8a86c5f53749 | -9.08991 | -47.71876 | 2025-05-29 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8228ffcb-17e7-3ab7-bef5-3934cb2a0f77 | -8.197 | -49.81744 | 2025-05-29 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 38af6ace-914d-300b-b7e9-4bd947a1e680 | -8.74785 | -49.77191 | 2025-05-29 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 518e1011-bc6a-3a55-823f-173501bcd818 | -9.21186 | -49.47572 | 2025-05-29 05:04:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| e79badf2-f27a-301d-adeb-4db1cd69b3f7 | -7.07329 | -44.93562 | 2025-05-29 05:04:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 47a137bc-d9ac-36a6-a709-8ce88604157d | -10.64243 | -48.80637 | 2025-05-29 05:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ff5b1f77-f0c0-3aff-9438-bb5c90bd5ca6 | -7.95293 | -44.85839 | 2025-05-29 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d63a5b93-8eaf-331b-880d-3a597362cb2d | -5.21054 | -43.31688 | 2025-05-29 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 04dfec05-37cc-3ce3-94fb-dd99bbf0d260 | -9.3704 | -57.55025 | 2025-05-29 05:04:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 726372c4-c7f6-3f0d-8edb-3358c344744c | -7.4698 | -47.05551 | 2025-05-29 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a83b02e-26cd-3875-92d2-cc70b0629d38 | -8.0188 | -46.16191 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27e0b763-7b99-3695-b2ff-33731a3caf5d | -7.07507 | -44.92216 | 2025-05-29 05:04:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 79814c13-3749-3257-8d24-b871cd75fcb3 | -9.34985 | -57.55059 | 2025-05-29 05:04:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffdbff78-c70c-3550-93e1-e1c278bb6383 | -7.68434 | -49.6303 | 2025-05-29 05:04:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d37cb4a2-c3a2-3f1a-b00d-d55294a0d8c3 | -9.20728 | -49.47502 | 2025-05-29 05:04:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 3d32968a-a4c7-37b5-8164-c39666038927 | -6.83558 | -44.6477 | 2025-05-29 05:04:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18ffb3ed-3f3f-3835-8d99-76f6d9fe31be | -5.21687 | -43.32116 | 2025-05-29 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0b03db8f-b4ae-38eb-912f-3834a03badf4 | -8.78905 | -47.93978 | 2025-05-29 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6068cd27-26e0-3c88-8028-4b114c25d1ee | -5.21268 | -43.30351 | 2025-05-29 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ef699790-a9c0-34a0-9bc3-a5e8f79b8874 | -7.67834 | -46.09542 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 924e6303-e104-3f7d-bcb7-a188419632f4 | -10.53194 | -47.58391 | 2025-05-29 05:04:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4bc8c573-e532-37b7-a20c-d86005310c50 | -9.20339 | -49.47076 | 2025-05-29 05:04:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2f1f759d-fb67-3c59-855b-c708c2765d8b | -6.54183 | -44.4599 | 2025-05-29 05:04:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e06074d5-25d8-3175-a749-46b49f4ed8fc | -5.21039 | -43.31995 | 2025-05-29 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 19e815f2-dcf9-316b-be3f-5e9552ad1eb7 | -6.24388 | -43.37393 | 2025-05-29 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4094abc1-36eb-36d8-bc21-282cdc73cacd | -7.67218 | -46.09846 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| eeb41d92-77ec-392b-912c-bb2476528742 | -10.65404 | -44.49913 | 2025-05-29 05:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 838c2929-cc58-317a-a613-c4e019cbf832 | -5.21916 | -43.30473 | 2025-05-29 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1d874626-e600-308a-9802-a3cfe85788bd | -7.30918 | -55.30973 | 2025-05-29 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65904e9d-0ed6-368b-be64-adfadc5b5164 | -8.19754 | -49.81552 | 2025-05-29 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3121f8e-900e-3ebe-aff7-74cf77054ffb | -7.08051 | -44.92758 | 2025-05-29 05:04:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1a159a7a-5106-3270-88e7-c2aee238a67f | -9.20797 | -49.47151 | 2025-05-29 05:04:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 92960bf9-0ba2-39ca-a71c-dc57b6b60d87 | -7.98606 | -49.69018 | 2025-05-29 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0e11b60f-8d5e-3f45-9485-257fd7af20d3 | -5.2184 | -43.3102 | 2025-05-29 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 154c04c3-5260-3af3-9220-0f128a18e4a3 | -9.20276 | -49.47557 | 2025-05-29 05:04:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b1a06548-44b3-3a99-9871-d6189156639d | -9.35708 | -57.54811 | 2025-05-29 05:04:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a000317a-a9cc-3677-83b8-8a2bfa55464b | -6.22798 | -43.34223 | 2025-05-29 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| ffb104fd-8bbe-3d24-8c91-39b9a97653ed | -8.01761 | -49.68457 | 2025-05-29 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2e84320e-7de3-321f-8c9e-7854903bd5ef | -8.19817 | -49.81115 | 2025-05-29 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa825640-b2cd-34ea-8c21-f614f51f46bf | -8.79374 | -47.94342 | 2025-05-29 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e2c58b09-bcc6-31fa-b257-9d1f4ac89401 | -7.62355 | -45.74774 | 2025-05-29 05:04:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| def082e0-48cb-386a-8e39-5e546633e719 | -7.58934 | -45.96198 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f27b1a2b-5475-34bf-a5a5-95cd237001fc | -4.81377 | -47.32106 | 2025-05-29 05:04:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 234f8741-7d10-3e56-8b83-cfcc2b8cd3ea | -7.94743 | -44.85263 | 2025-05-29 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 583517b7-5b60-3593-b638-d0e6a604c81d | -6.23728 | -43.37319 | 2025-05-29 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5223d3a4-d81b-3dc4-981c-eb5147061449 | -4.48697 | -47.79126 | 2025-05-29 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf0864b9-73ea-3db0-8242-c59bbd27d52d | -8.01424 | -46.15296 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36c4ec82-c339-3093-b799-29a206bc4c1e | -7.63573 | -45.93422 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c58d6e71-9a21-34ae-aa53-ad212b8b7368 | -8.79413 | -47.94044 | 2025-05-29 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 475842b0-9c85-320f-8474-77e33dc5aef1 | -6.22718 | -43.34828 | 2025-05-29 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 04ac31e5-1523-3001-936d-b0108a6d20cc | -7.07388 | -44.93118 | 2025-05-29 05:04:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1f4adb01-ecd7-368e-95c1-1334784e86e2 | -7.94893 | -49.76072 | 2025-05-29 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f106dcb-f270-3cff-9b2b-92353bfac6fa | -9.10934 | -46.92866 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ac2c92f-b20b-3c96-b71d-e169bf105425 | -8.74247 | -49.76803 | 2025-05-29 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8a61054-6721-3f79-bcd1-958bfd2ca324 | -10.63752 | -48.80575 | 2025-05-29 05:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e285ca7b-e0de-3c65-a9df-04819a111af6 | -6.53565 | -44.45902 | 2025-05-29 05:04:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2f18f258-36a0-37ff-870b-7152c607a2ce | -8.01313 | -46.16126 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72bce878-9691-318a-927a-f2f8266d8f4a | -4.48713 | -47.79071 | 2025-05-29 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c3b44856-d4aa-358e-9bb8-cd0c02844056 | -9.35432 | -57.54404 | 2025-05-29 05:04:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99d8d15f-aeb5-3ee6-b602-75f2f1cc20a7 | -6.33592 | -43.37671 | 2025-05-29 05:04:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b12aad8f-2efc-31cc-973a-51c25afa7d7e | -7.67886 | -46.09151 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 42e29608-7e66-3f4c-a313-2ccc75a23034 | -5.21116 | -43.31442 | 2025-05-29 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 55ca29c9-c509-3309-92d7-ea67bac7797e | -6.34324 | -43.37212 | 2025-05-29 05:04:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 53a44914-ab64-33f8-9d62-f634e16f0d78 | -6.80853 | -45.37066 | 2025-05-29 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8a97d51d-05e5-3690-9155-f4024e197d37 | -7.58522 | -45.86088 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f82fe35-d115-3898-a426-5f676d9163c6 | -8.0029 | -46.15164 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5cca52fc-efa2-37ce-af73-a5237548589f | -7.97564 | -50.70463 | 2025-05-29 05:04:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4083d3b-cc5d-3f17-8200-92bef652e3c0 | -8.09763 | -46.28517 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 067de88d-c62a-36c6-8628-b15a6eae5c28 | -5.2192 | -43.30163 | 2025-05-29 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4445dce1-f2c7-352d-a6a7-7f6b9d84be27 | -8.75139 | -49.7694 | 2025-05-29 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ec7d0e98-bbea-362f-88a3-c68055323629 | -6.83422 | -44.65782 | 2025-05-29 05:04:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 026dc174-2e09-3faa-88dd-228454a84c39 | -9.36098 | -57.54511 | 2025-05-29 05:04:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf86b4df-8ac5-3bc5-8c45-a6c2a64ea10b | -9.29971 | -50.43195 | 2025-05-29 05:04:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 299c52bd-ce25-32df-b182-8140177be5b1 | -8.40148 | -47.09436 | 2025-05-29 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbb8d795-f7e5-3a32-81df-c16be8ff8a4f | -10.64315 | -48.80088 | 2025-05-29 05:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f27faeb7-ad43-3e98-9e79-aff769e94855 | -7.19023 | -43.10674 | 2025-05-29 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| b41a8ecb-cbb2-39e0-9ab8-52773a1506f5 | -7.24588 | -43.10247 | 2025-05-29 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 9fbcbb6e-640b-3708-97ec-0e8c0d06fcae | -7.07447 | -44.92668 | 2025-05-29 05:04:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c90e0907-bd04-33cd-8bf6-69b0dcdb3520 | -7.63964 | -45.93314 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b54a6cb-ce6c-372a-b003-e2fe2a9ef614 | -7.18778 | -43.10743 | 2025-05-29 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 1aaf8321-be12-3ce8-8875-56286f95bbb7 | -8.74693 | -49.76872 | 2025-05-29 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a718b5f-159b-304d-9719-4438afe951f0 | -10.46835 | -47.94845 | 2025-05-29 05:04:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9091eaa0-6e0d-3249-8cb8-d055c0767075 | -8.89964 | -44.77998 | 2025-05-29 05:04:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| efa64687-224c-3400-a9ef-37693e11f600 | -6.34983 | -43.37306 | 2025-05-29 05:04:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e4c3278e-9150-3ffc-91e9-0b4adf441628 | -5.41488 | -49.08074 | 2025-05-29 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e04f0f4-f53f-306c-a54e-f0dc961d8ec0 | -9.39012 | -48.41998 | 2025-05-29 05:04:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 70e6ae84-1fa7-35eb-a9d3-b4fb768c96cf | -9.35299 | -50.2345 | 2025-05-29 05:04:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61840745-d861-3ecc-80af-6942a0c24d4d | -7.63623 | -45.93028 | 2025-05-29 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README14.md)
