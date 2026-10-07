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

## Dados Diários - Página 172

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 346cc691-b1af-3d50-9397-29f9983fd1ee | -7.55923 | -46.7112 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0c23e270-dfbf-36f6-978f-9746b0a7450f | -6.02734 | -42.26043 | 2026-10-07 16:03:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| d35d74ce-4d65-3d5e-bf95-6b78bfd7f932 | -6.95035 | -45.2713 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| cbc8f077-927b-36a6-bf40-7fc1eaf05c91 | -5.72713 | -45.1596 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 244.3 |
| 5fa8c108-7208-3473-a307-ab9d24ac4e64 | -5.96779 | -40.93233 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 27.2 |
| f9d4a197-e715-3242-a7b4-bc72b2844a88 | -3.5012 | -41.95322 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| d0066018-530d-3114-8379-c1420cd98561 | -3.5042 | -41.94857 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 39.7 |
| a9a7e30a-c930-3b3a-bc8d-f3ee74c062a0 | -6.19991 | -51.43531 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f415a2b2-8d73-3e5a-97a0-9a5f1c178dcf | -3.80625 | -49.11555 | 2026-10-07 16:03:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 5b67f30e-0fe1-306d-90fd-a034cd87f6bb | -5.7254 | -41.73589 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ae464075-2c68-3ec8-be39-6681933d8f00 | -8.21666 | -46.34482 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8b564a51-6380-3936-b933-d1356e7cef53 | -5.73697 | -45.16298 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 46250768-11f5-3411-85ce-4b38f8aae30f | -6.98548 | -43.29428 | 2026-10-07 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| a82c1f75-eccf-35a2-a8ec-34b5ce7827c4 | -5.1735 | -48.62519 | 2026-10-07 16:03:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| c59a4383-11b5-3b71-b41f-5231e3e559d6 | -5.96666 | -40.94889 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 6d18bd9c-e73b-36d7-8c62-c30b7d4b4906 | -4.24199 | -49.98563 | 2026-10-07 16:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 29d602bc-3234-3164-a68c-e401867678b7 | -3.12847 | -43.83949 | 2026-10-07 16:03:00 | NOAA-21 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ebad2f6b-9d66-3f3b-a04f-01edc9dfd6d6 | -6.60265 | -37.89449 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 7867b436-48df-3758-bcc9-8433bb3dc241 | -5.37679 | -44.17065 | 2026-10-07 16:03:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 578a4625-8702-3b33-a973-a97bb0690404 | -4.83285 | -40.72714 | 2026-10-07 16:03:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 7a4d3b3f-0816-3e11-abc7-0a2a5985fd74 | -3.76255 | -45.05592 | 2026-10-07 16:03:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3f8ba4ec-f6fe-3f99-a0d5-e90f2147398d | -6.62036 | -37.87763 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 204c71db-041b-3856-a645-e252ab6950cc | -2.17181 | -48.37015 | 2026-10-07 16:03:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 6959eb8c-7792-3f2b-b558-4426222ab633 | -3.66638 | -41.44217 | 2026-10-07 16:03:00 | NOAA-21 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| b805688e-8788-36c9-8b1f-9bfe4d4e3bf4 | -6.84311 | -39.55245 | 2026-10-07 16:03:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 2d6a6b7a-c852-38fe-a004-8073192242db | -4.91665 | -43.22208 | 2026-10-07 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5a2f6d95-0644-3b2c-a4a0-604c48271b98 | -7.29666 | -47.27753 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| cbc26c23-6a91-3264-aa92-24cb69231228 | -4.2778 | -39.55085 | 2026-10-07 16:03:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 384100d7-e2af-3b62-a8a6-5bfd787b4004 | -3.27383 | -51.05192 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e766ab89-c2a2-3c57-ba1e-447e3300ffd3 | -1.8839 | -45.43962 | 2026-10-07 16:03:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 3741ebf3-2e48-33f1-b362-0976e034b162 | -5.96303 | -45.69839 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4954ab98-3fa3-3b9a-ad83-0c21fa5a4575 | -8.5644 | -51.23244 | 2026-10-07 16:03:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4374776d-7eed-3b28-b693-1bf782557241 | -7.12517 | -43.91728 | 2026-10-07 16:03:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 695ee0fe-92d0-3d23-8c45-8642a37291e9 | -5.53389 | -44.95667 | 2026-10-07 16:03:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 8b52e41a-5226-3a24-80f4-779a038041b6 | -7.27679 | -46.16232 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a49b88e3-dcb8-33ce-850d-063237878049 | -5.74157 | -45.16236 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| d3ed5e48-07dc-3018-bfce-e265613d1644 | -4.71591 | -47.93101 | 2026-10-07 16:03:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a6d6ce68-a09d-3806-bfaa-c9cac7d75a24 | -3.51017 | -41.93916 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| be83a700-c2b9-31fa-a6d7-ff2467d87386 | -4.62493 | -48.86141 | 2026-10-07 16:03:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| aa254af4-500e-3b9d-b378-83d2991825ea | -3.87872 | -44.12514 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ae49d129-e659-33d9-addc-418e333b2a0b | -6.71222 | -45.77562 | 2026-10-07 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c6e19d98-71fb-300b-acc4-1ac65d066100 | -5.47996 | -45.63531 | 2026-10-07 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| be35d680-af1e-3da6-a8d6-dea92c4c3252 | -3.92963 | -40.38783 | 2026-10-07 16:03:00 | NOAA-21 | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 925467e6-962a-31c3-9cba-64f534d584fb | -7.01079 | -44.05886 | 2026-10-07 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 27ee30d1-ccea-3470-8f88-9ea80e9fc034 | -3.12764 | -51.14563 | 2026-10-07 16:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6119fa39-da12-3fd3-a27a-fcbef1ee506a | -3.74704 | -41.71577 | 2026-10-07 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| dc812b90-88c7-3a1a-8d43-5ef3c6ff3e8d | -6.36 | -42.55609 | 2026-10-07 16:03:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 0108fe09-a19c-34ba-bab3-3bcce321d9a0 | -6.94015 | -45.26694 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| d5736348-ca61-3da3-a570-4e4961c3b2aa | -1.92122 | -47.92355 | 2026-10-07 16:03:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b50f0acd-d69d-390a-a30d-4979234a647b | -5.72847 | -45.16917 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| dded7325-7c51-3b4c-a866-47433deef51b | -5.24549 | -50.91582 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| df334beb-e068-3468-9b4a-475de8261d91 | -6.84842 | -41.76595 | 2026-10-07 16:03:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 5d35dcbb-ae94-32bd-91dd-94ea12275676 | -3.75002 | -41.71112 | 2026-10-07 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| da090e23-122f-3c87-b3a3-416097aef84d | -2.94487 | -49.03808 | 2026-10-07 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e220c102-7657-367c-8717-8260865ab94a | -3.50294 | -41.94027 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 48.0 |
| 75c1f1f9-8444-36a0-a69f-b4548c7373c1 | -5.61964 | -46.67625 | 2026-10-07 16:03:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 29f4264c-ea4a-3d61-9cdc-6cc9fffc1aa3 | -3.26049 | -50.39987 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| ccdaae88-6310-3cb2-a09f-b0d091a778bc | -5.24902 | -37.57994 | 2026-10-07 16:03:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 26.3 |
| ca06c370-1fec-3299-890e-117d52896625 | -6.33589 | -37.75312 | 2026-10-07 16:03:00 | NOAA-21 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 6.5 |
| e4d788dc-d392-35c6-80f9-1bd1042d242e | -1.42644 | -49.11211 | 2026-10-07 16:03:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 752a4114-b7bd-37d3-92c4-993201750f06 | -5.73772 | -41.74297 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 5c6070a1-5c2d-39f0-9db7-f955ef1119c6 | -5.98275 | -40.90991 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 77c6e901-1368-3f50-becd-ff756c0dd6ef | -5.96251 | -40.94539 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| f14835d4-653a-3a49-ac33-8f526a09f14c | -5.49559 | -42.84552 | 2026-10-07 16:03:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 327.0 |
| ca335510-6449-3f6d-b71f-d4575f3b76d2 | -4.49631 | -43.85275 | 2026-10-07 16:03:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ba2a4068-c30d-38e3-8903-d7defad1ad74 | -3.19256 | -50.55395 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 18fed6c4-c7a8-3533-8e7d-f4e4129d3e23 | -6.18566 | -35.48778 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA DE PEDRAS | RIO GRANDE DO NORTE | Brasil | 2406304 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6297e6a5-93db-3808-90e0-ef61d952b7ef | -3.54378 | -50.10321 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 04862b99-ce72-3b60-8cbf-7320b2e35d2b | -4.46029 | -38.62435 | 2026-10-07 16:03:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e1122fe2-e7cc-3ab0-ae60-8da9d8c03f98 | -5.84848 | -43.84079 | 2026-10-07 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a4d289c9-bff2-3fcb-b37d-32e157032051 | -5.73882 | -41.72508 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| ecab26e7-e508-3a9c-9d7d-850678e6afc4 | -6.67971 | -41.77088 | 2026-10-07 16:03:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 3a1f50cf-861e-3182-87d3-b9cedf810a22 | -4.56771 | -38.30429 | 2026-10-07 16:03:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| e4a141b6-2e0b-30be-8fc3-d9362a25f4c5 | -3.58733 | -39.14212 | 2026-10-07 16:03:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 15.2 |
| f92558c3-a7f0-34b0-926e-28dab007698b | -6.92053 | -44.56137 | 2026-10-07 16:03:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4c6d45de-0e80-3184-bd85-3f74f243b343 | -2.27451 | -48.75487 | 2026-10-07 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c1eeee9c-bb11-304f-802f-86e54b8e184c | -2.87994 | -43.71035 | 2026-10-07 16:03:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 97e4ecd8-99c7-3676-99e8-6294ab418921 | -7.2385 | -50.81328 | 2026-10-07 16:03:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3710d73a-ec72-3e5d-8124-2cb04cac8148 | -6.34098 | -43.84268 | 2026-10-07 16:03:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 1de85a02-614a-3606-ad91-7d35ea9ac682 | -6.64247 | -43.77462 | 2026-10-07 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7c636ae5-966a-35e8-9f5c-7cd08e41b80f | -7.29078 | -47.28954 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 342533ac-9455-38a8-9d55-2eb0b71ff330 | -6.58932 | -44.19409 | 2026-10-07 16:03:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 63fdb25a-86c0-3798-aae3-086df6a5b0ba | -5.94708 | -46.38057 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3a6bbccb-4bf3-38a3-85ff-dfaff8ed2b8b | -8.00958 | -47.18845 | 2026-10-07 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 70ddaaae-08f2-3a8d-88dd-91097c80ce0f | -3.00089 | -41.42556 | 2026-10-07 16:03:00 | NOAA-21 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2fb496c6-4388-3861-b718-cb7453aa7d5b | -6.84643 | -41.76817 | 2026-10-07 16:03:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| abc32630-52c8-350f-a674-d11dfa07f1c6 | -5.97273 | -40.91553 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 33.3 |
| 6bdc95fe-6097-3d1a-9293-8ed119fa51e4 | -4.36527 | -41.82511 | 2026-10-07 16:03:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| eb4cea6c-d80d-31b2-8af6-4e2052f04325 | -3.4163 | -42.79889 | 2026-10-07 16:03:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 70607209-a18f-31e1-a9f9-f01821aec24d | -5.47912 | -44.25539 | 2026-10-07 16:03:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7f16357a-03fd-3658-a322-300d551ce217 | -7.10632 | -42.53256 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 284d0038-3099-38f4-a68a-0c017f210f6c | -7.40203 | -45.63391 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| a359c590-d522-3e0b-8018-440a58019094 | -4.11873 | -41.77759 | 2026-10-07 16:03:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 28.8 |
| daf43e78-12da-3e40-a195-fa1c5403f294 | -7.21426 | -44.29288 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 913aea12-01e2-3b30-853e-56e801c83372 | -6.94419 | -45.26138 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| d0dbf311-9203-3a4f-8b77-94d54edca5ed | -5.23049 | -50.90574 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7e9a7987-4ebc-39b5-982b-399e5f1fe34b | -5.58716 | -35.25516 | 2026-10-07 16:03:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1acdc1a6-b379-355e-96cf-b26c44bb1afe | -5.98269 | -40.93429 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 706353fa-bf1e-39cb-81dd-3cecc45c4410 | -4.37631 | -46.34286 | 2026-10-07 16:03:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| edd04106-b4ab-30ae-ad72-5491642ebcd4 | -3.50592 | -41.93557 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |


[Clique aqui para ver as próximas entradas](README173.md)
