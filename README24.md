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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aafa4c00-7f56-3d2b-8b49-e3fc7abe1cee | -6.21321 | -43.37286 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be9ace5e-6627-30c8-add2-653c5fd6a056 | -11.38826 | -45.58419 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3aab87e1-e1ad-3cec-aafe-c267962de7d8 | -11.43371 | -43.57031 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4a1187d-dae9-3634-b1f7-d4145f0db633 | -8.16557 | -46.08526 | 2025-09-11 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8e105d7-5865-34ac-bf98-88db8b2fa663 | -6.80186 | -43.26828 | 2025-09-11 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e57dcd79-59ca-3e96-8027-e0d7e101593f | -7.91033 | -46.8528 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a42fe76-dd7f-3f9b-acb1-e219ec8bf3c1 | -7.38584 | -47.38008 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3d64afa-d4cd-3888-a06c-17e64501c4e4 | -10.20439 | -46.8359 | 2025-09-11 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9b1a8bfb-b722-3cf4-826c-d0f9751c264e | -11.48226 | -49.25843 | 2025-09-11 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c824f18-d15f-3f76-8f59-cd5813c815c1 | -9.00764 | -49.5238 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ccb676b-d43f-33a6-b158-986b6c1785dc | -9.0233 | -49.76213 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4c77d282-b143-3c55-a58b-93933f70fe38 | -10.78516 | -47.78394 | 2025-09-11 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2bbec3f-3350-3cbd-ae75-898b55bce7aa | -6.31833 | -43.4449 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 94052f76-27b7-3e03-9b49-fcb833b2bf7d | -9.06859 | -47.06022 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c420637f-054d-3610-8c20-08a310d245a7 | -11.47279 | -49.24925 | 2025-09-11 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fafe255e-5853-34e9-a21e-29759b69de0c | -6.21911 | -43.49604 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 87bc4bab-c88b-3837-a375-7ee79739b98b | -8.75015 | -47.12191 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2f59fd1-8fc2-3ab8-a92a-25effde45695 | -12.1398 | -44.85094 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fa83c80-71a3-34b0-8ba7-eadb31cfcb94 | -11.1026 | -48.41732 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a63741da-4012-3ace-b952-a41f144a90e0 | -11.48604 | -43.67783 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0733b871-b8d6-3cd3-9757-1091d6d09edf | -6.30909 | -45.66063 | 2025-09-11 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf2eb340-d241-3862-ab09-5bca768b1e87 | -11.48158 | -49.26205 | 2025-09-11 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1c8466e-1d23-34c4-8da8-b651e0dda7e6 | -6.58122 | -47.34832 | 2025-09-11 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 90d18496-6d2e-3ffa-9ef8-3bd54cec547e | -12.591 | -44.78587 | 2025-09-11 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7aaaeab-8b93-3efd-8398-2e6cbee3f6ee | -5.6976 | -45.32261 | 2025-09-11 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 541da9b2-4dd4-3c5f-9ca8-04f151ceb9e1 | -5.94 | -45.71735 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b92ed71c-f41f-3201-b623-27d3614d2ace | -6.67255 | -44.12571 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 678f984f-6a44-3ecd-a914-010cab673cad | -11.47889 | -43.62881 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1c52075-18ef-35c4-8c81-2cd5a6aff5ef | -7.71435 | -44.79944 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f013e69b-d5c0-3669-b2ac-775768f98aa3 | -11.39047 | -43.53008 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a064eea-78fc-3837-aac3-117716fc54d1 | -8.03863 | -48.67479 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93cbc088-35b2-3c54-8529-94f32bca3da2 | -11.9916 | -47.59995 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e940b132-50db-39ef-8b22-215744f7277f | -13.26638 | -43.74425 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6978a4d1-79db-3b6c-a04d-3aaeebebafe8 | -7.39241 | -44.36717 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abcdbf70-b40a-3389-bc15-325532087f7e | -10.78456 | -47.78708 | 2025-09-11 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4baeb0e8-aaec-3c7a-88d6-d0fe69fe151b | -11.10374 | -48.44016 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04fd563a-36dc-373a-8a6f-946504502d4a | -11.47297 | -43.61824 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ee13637-64be-349a-8aab-470543975464 | -12.47691 | -47.48431 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a9bfd90b-e7b0-33d2-a18f-6e61680b6ae7 | -7.16915 | -44.13799 | 2025-09-11 03:55:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3c694360-32f7-3d5c-b1ec-3ae1378600c3 | -6.7663 | -43.46378 | 2025-09-11 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3947e52d-eb9e-32ef-a033-ad2177e59ef3 | -9.08051 | -47.09049 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19c8d832-5149-3b09-8b91-ffd511fcb2a2 | -9.00106 | -46.08105 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 79a4c44e-482c-395c-a442-45bdb05e97a1 | -9.06693 | -47.04193 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 00a9ec22-1290-3076-ade4-b807349f2964 | -8.75211 | -47.11064 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0bba4bb-c035-3c11-a998-9993891c37fd | -6.20989 | -43.49387 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9582e7b3-eec0-3d44-84c2-f15126cf02fc | -11.02314 | -45.05872 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| d163144c-b977-37b0-bfe2-7728940d0275 | -11.40251 | -45.60287 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcd7939d-8ddc-3265-9fcf-f5abf44572f3 | -6.99354 | -44.78837 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9e4aaa6c-6eba-35e8-a345-d95f301b56bc | -6.83493 | -47.90415 | 2025-09-11 03:55:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e03a99a-7c8d-3617-b5d5-e16753a53c29 | -11.38751 | -43.52488 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ce33846-6f0d-3cbe-8c55-89ec0eae05be | -8.1686 | -46.0881 | 2025-09-11 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e4532cae-a7f7-327b-a1fd-ce13dd290bcb | -6.30976 | -43.42196 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e770dd2b-2096-344c-bb9b-e9e80160df21 | -9.02621 | -49.77616 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 64bf126c-cc95-3264-b1af-74dbf588b3db | -11.36257 | -46.56538 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1a74f8f7-5e07-3b8c-ba96-14fe0b04751f | -9.13301 | -46.19137 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5ceb530-8446-34a5-b733-ab06ff35fdc8 | -7.04865 | -44.69979 | 2025-09-11 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a726110c-39a7-3d23-ad24-4a6138fb02f9 | -6.34799 | -44.09125 | 2025-09-11 03:55:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 117b851f-6066-31af-8e04-4e7a0188b113 | -9.08093 | -47.07523 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 325670f0-558f-3265-98b9-5a9d41b18426 | -11.48294 | -49.2548 | 2025-09-11 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3882f3c-0398-37d0-842c-bd957dec44fc | -6.30244 | -44.59132 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b52aa818-32c2-3d7a-8ea0-9a635e401be1 | -11.94816 | -46.64338 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82342f4c-951a-3b51-aed9-5b9c3337396e | -8.02548 | -48.65352 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 471d4ba0-fd2e-38ba-865a-c34ba52d85d6 | -10.17759 | -44.76745 | 2025-09-11 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8eaacd5-38e7-34d5-b862-08d193953498 | -9.34351 | -48.94201 | 2025-09-11 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a36f0db-cf39-30d8-9df2-2eab8c3f9a97 | -12.10052 | -51.01051 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da5ee238-46e0-35d9-9f0e-79e69006d3c7 | -10.89407 | -47.25829 | 2025-09-11 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe451d76-641e-37fe-a45d-137530b54e05 | -8.1702 | -46.08613 | 2025-09-11 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59f0f3e2-1d3e-3282-9149-d9f69b40028f | -6.17556 | -41.0808 | 2025-09-11 03:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 41d15ca7-ad84-32f9-b508-21208a6419dd | -5.86385 | -44.20319 | 2025-09-11 03:55:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7797bc6-c0e5-3eb5-a8dc-a56630bba214 | -13.16515 | -45.28692 | 2025-09-11 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5ef33108-8b73-3f06-809e-20862996a506 | -11.15291 | -45.29079 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78b80d94-e3ef-3422-a06c-731f905e6fe1 | -9.06241 | -47.05032 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ac755728-c8b0-377f-ae17-57cbf7936b87 | -9.86296 | -43.12653 | 2025-09-11 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f02baf91-471a-3406-89c3-434350445b14 | -5.60539 | -48.11525 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70cde34f-1828-3b58-8cc3-7b5614ae6da9 | -8.7462 | -47.11544 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 742daafd-b6e0-3cd8-983b-0b21b1a6bbee | -13.1577 | -45.28187 | 2025-09-11 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3d489082-6c11-377e-9a59-3f5bbc61b313 | -6.99424 | -44.78434 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66ef3a85-5eac-3660-85f2-396305b1038b | -9.60967 | -40.61855 | 2025-09-11 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 3380837c-ae51-31c3-a059-19abfa53064b | -11.43888 | -43.56976 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 148f8266-bd7c-3cf6-bef7-30e21deab261 | -5.43309 | -45.88219 | 2025-09-11 03:55:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eec1a4ad-fd29-3e1c-9e0c-6d80e3e8edab | -11.74503 | -48.12441 | 2025-09-11 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b71f66d6-e4eb-39db-ad9e-e520ad586f22 | -10.26155 | -48.82442 | 2025-09-11 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ffd43bd0-9b01-3ffd-baa8-af9939ca01bc | -6.83033 | -45.61913 | 2025-09-11 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebb44a46-f290-334d-a803-9d820ed0171b | -5.96832 | -44.72123 | 2025-09-11 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91eecd64-fd9e-30c3-bd64-e58fc3530073 | -13.25045 | -43.79217 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 91481ce9-3ecf-35f2-9adf-e458f06ea720 | -8.66236 | -45.73091 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4ab2cb81-1d56-3198-9259-720ae8b62117 | -9.02604 | -49.78006 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0f32fd77-bb96-3d8f-9c0c-5de16db71ca2 | -11.34645 | -46.50069 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ae6f3993-9ae0-37ec-9c94-449a73f1ad66 | -9.06171 | -47.07021 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2ff5e360-3f3d-3a75-b5c4-07aef5db7e9a | -9.91232 | -49.91204 | 2025-09-11 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a22a696d-3a0f-3d94-99ec-6926eda174cf | -11.72099 | -50.64929 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3cb2f2ba-a9a5-3835-a93c-05cdc0008b95 | -6.40108 | -42.60239 | 2025-09-11 03:55:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 1dd55cdd-6a8b-3075-8e43-d984d93ac457 | -7.93849 | -44.88916 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55334627-d5c9-3956-8e30-918f49cfcb75 | -6.54191 | -44.78325 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d001390c-306c-3e6c-997c-67d8936c6611 | -6.34711 | -45.18621 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e47732c-6cca-368b-8d20-97f8772cf11a | -11.49074 | -43.65003 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4e267585-7310-306c-b2fd-c12ac1dc3c08 | -6.5524 | -43.97783 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f105350-cab1-35f3-b366-183a851eb9cc | -11.35397 | -46.5358 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8de64f22-e9ac-379a-8509-52557a71979e | -8.19553 | -50.10678 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a9310221-d9e9-3c2c-b855-4004cba10ab2 | -12.0725 | -50.99546 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |


[Clique aqui para ver as próximas entradas](README25.md)
