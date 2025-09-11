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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5d2f3f5-f883-3f55-898f-67fa43c75689 | -9.08196 | -47.07941 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af980133-c985-36c2-bd17-927652d675c6 | -6.40377 | -44.49965 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b94ab13-1454-34a2-85de-d57b33e4fadd | -2.43976 | -47.33028 | 2025-09-11 04:44:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1f1b488-188d-34ed-b564-6ae2321b0f6d | -8.35525 | -44.83828 | 2025-09-11 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 228918bf-81d5-30da-8afd-9161c00de20c | -8.0783 | -50.18402 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a3ae994d-156f-3f20-a24f-be6181846d89 | -7.65559 | -49.50211 | 2025-09-11 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 400382ad-11dc-3d9f-8370-763b182a92a3 | -3.41994 | -47.60943 | 2025-09-11 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 98266aef-0cef-3411-a1f2-b30133445952 | -8.08468 | -48.23093 | 2025-09-11 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 8e3a9b94-3974-3906-8e2f-118df6af6f3f | -6.66102 | -44.54442 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97bbaed5-bf38-33e0-8c6a-9b3e5c2610a7 | -7.91985 | -44.87455 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7f186a9-89ae-3679-af9d-07a62a08061e | -9.11098 | -46.96384 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cc7b414-7368-32db-9e4e-7d897d69e577 | -3.07722 | -48.82058 | 2025-09-11 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6cf9dd9b-6ac6-3ff9-b60a-15ce27658dbf | -8.16259 | -46.09113 | 2025-09-11 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 32eac98c-ae2b-38d5-a87a-9bfbb93e729d | -5.66351 | -43.33541 | 2025-09-11 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae925a3f-21c0-3034-a3f3-87b52cab2bb4 | -5.6965 | -45.31918 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eced2c39-4c30-31c7-967a-ce279b886b44 | -6.85272 | -52.84234 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c79c1e7-7bef-3f2e-b70e-1bcf19ac5523 | -6.99478 | -44.78826 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70329122-5347-3fdb-a6cf-c474f2602f9b | -6.18624 | -41.0588 | 2025-09-11 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 87455911-b680-38f2-a054-5f6e036da533 | -8.29657 | -44.91324 | 2025-09-11 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 568eeefa-04d5-35ed-89da-473dddb4658a | -9.06299 | -45.70222 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06a4c8cd-63a3-36da-9358-e3da87483b97 | -8.19951 | -50.10368 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 85044c70-df86-3508-8215-7f3d9071665f | -1.60619 | -54.65479 | 2025-09-11 04:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf8fe3a5-9b56-3cb3-90bb-2044649aca15 | -4.92764 | -55.78297 | 2025-09-11 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb82611f-98bf-3370-bd47-cc604a574674 | -9.09197 | -46.95634 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 590814ae-9e84-38cc-829c-b48e0c79013f | -5.94151 | -45.72018 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd9995c2-8466-3099-9aa1-180eb0562d81 | -8.62816 | -47.16814 | 2025-09-11 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 108f7974-790b-3bda-8f4e-fa379a4bc9a6 | -6.65809 | -44.54609 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c05998b6-8c1e-3140-8f91-9cb3f08f1300 | -8.1647 | -46.07611 | 2025-09-11 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b663fbf0-7554-363c-a43b-4f9d24472847 | -5.97958 | -45.79943 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c9f88ff-0d59-3e72-9a36-59e1c6920265 | -7.08423 | -44.85205 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23f9b29f-a042-34d2-a1a9-006e1ab40ca8 | -2.94578 | -49.35094 | 2025-09-11 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| afa0554b-90ee-3bda-a062-612bc10cfa33 | -6.85394 | -44.89285 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18723473-896b-393f-9075-a607a1bbdfe9 | -8.0202 | -49.0425 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 040c8e25-06f3-376d-abc2-a57a3df9ffa3 | -6.74651 | -51.95589 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43561734-b5a5-3050-b8ea-bf86804c10a3 | -7.39064 | -50.89055 | 2025-09-11 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1521531-ebd6-3fe1-909a-e07112b84bc9 | -5.36134 | -45.22178 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e41fbb43-2c5e-3ca4-866f-83494cbfca6a | -2.7422 | -48.68084 | 2025-09-11 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e93e0d94-3d3b-3bc9-a804-12f0797bb778 | -6.20789 | -43.35287 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e9cac6e8-4d4c-325e-a315-1a5ebe79876a | -6.5455 | -42.43791 | 2025-09-11 04:44:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a80adad3-7fdc-31d2-8f50-1c155ac7d51c | -6.19309 | -53.27455 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbc51d65-88f5-32ef-9104-77f949d63844 | -7.25841 | -44.61201 | 2025-09-11 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28b00ab7-3e2a-3791-b799-b838ddd39a2e | -8.64156 | -45.72321 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0bf906df-553f-3db3-b3ad-52eeb3028697 | -7.87498 | -46.01568 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d51a9e2-8dc1-3e86-8f78-b4b9d499be2a | -4.04385 | -49.07835 | 2025-09-11 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eed0d0dc-958e-378f-80f5-783a67cd3d4b | -6.61771 | -43.99539 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e3d47946-6a29-36ef-a58b-9aa8ceb12c76 | -6.56781 | -44.20769 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5e71d9fe-06fb-37b8-9932-2e35b30a36dc | -8.19446 | -50.11398 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6047110-5772-3695-a195-c9d77cd20fdb | -5.9453 | -45.72091 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a93393bd-4a22-3131-a608-bdcb11bb6352 | -8.20407 | -50.10723 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fe09bedc-8fa8-3fe2-917c-22209e0eda24 | -6.40426 | -42.60979 | 2025-09-11 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dca2c190-ce79-3e25-a43d-b02aa293cacb | -5.55449 | -43.04612 | 2025-09-11 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b191970e-eea2-3ff7-a9e6-8762b3f107c6 | -4.86484 | -42.76999 | 2025-09-11 04:44:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36a92e19-2bf9-31fd-bf1f-0d900b6e90b4 | -4.29244 | -50.5928 | 2025-09-11 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3f04e01-27cb-3808-b762-51255f96a13d | -9.06857 | -47.06098 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 74d80437-dee7-30da-b401-7f8b01b2b95e | -5.3601 | -45.22185 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5692cced-16a6-3879-9ac4-44ca8a201de4 | -8.43502 | -47.26456 | 2025-09-11 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ce79874-2129-3a07-8495-088f6d8229f0 | -8.47894 | -47.28551 | 2025-09-11 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b6574b5d-9f50-39d7-8f32-239ee7e335c9 | -6.32001 | -47.74154 | 2025-09-11 04:44:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8ac8581-bd00-3ca7-8ae0-f70a3a17f839 | -7.79241 | -47.93592 | 2025-09-11 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 554f4f03-5ec8-3ccd-a27f-8a6937b321a8 | -7.69714 | -45.14862 | 2025-09-11 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0b3ddff-f05d-3799-a2eb-0a104bed4c1a | -5.91374 | -51.93851 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e5a268a-119a-33a1-bdac-34928c71e224 | -5.97798 | -45.81019 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bcc35a4-3359-3e2e-aa0d-d4e1f0edfcab | -6.01885 | -45.89653 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fed1174-db92-326c-9f49-bd29043b3895 | -7.3281 | -49.60685 | 2025-09-11 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a2e47d4-478c-3749-a1c2-f7121572ef04 | -8.72799 | -47.08952 | 2025-09-11 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0cc2a00e-4ff1-3a7d-bad6-97137f21a121 | -9.05488 | -46.96238 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 27db2557-478d-3a9e-9f34-0d45cd8dac22 | -8.04108 | -49.04568 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a549ba27-b9b9-329f-8634-2e1c402f3261 | -5.74847 | -51.69655 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d72136ab-6dad-303a-bad3-f445fa4181f4 | -8.16617 | -46.09544 | 2025-09-11 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ee6e4fd-0fd2-3970-9d2c-de143a55964e | -4.40339 | -50.55761 | 2025-09-11 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c74bd64d-62fb-3be8-8657-f123b57d5207 | -8.16563 | -46.09926 | 2025-09-11 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e8ef704-bc2d-33fb-a73a-6f108ba17eeb | -7.39401 | -48.50271 | 2025-09-11 04:44:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e232543-1e08-314b-a9bc-f340e502d497 | -7.78127 | -50.78077 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a09b56e-8ea9-3d84-a4f5-c18a85b3ba23 | -6.69888 | -44.94474 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2061af51-26ff-3ec6-b6b4-194894883a9a | -1.60977 | -54.65118 | 2025-09-11 04:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af0a011c-78e4-3ec0-b4bb-6b515d0efc2b | -7.11154 | -50.76419 | 2025-09-11 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67fd946e-05f1-39a8-9821-2e7956273dca | -5.40181 | -45.93977 | 2025-09-11 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebda9dc9-a7f4-39eb-9a29-5795f877c2a4 | -8.02402 | -48.66219 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bde4f754-9d75-3e89-b255-8ac74c048acf | -5.94175 | -45.71666 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcc63b2f-8ee9-3e8d-a586-00f324eb53d6 | -7.58403 | -47.75874 | 2025-09-11 04:44:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26b9295e-2cdd-3140-a8d9-5ed3905dc091 | -7.66001 | -50.27223 | 2025-09-11 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| daf0601c-c5d2-3ebd-ac40-c55880aa0a66 | -4.96086 | -43.22532 | 2025-09-11 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68c84172-0526-3f89-9b28-306f74ead146 | -6.34543 | -45.18772 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2eb0c068-d562-38ba-8567-eb8d3f9a8787 | -7.62519 | -47.6783 | 2025-09-11 04:44:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2cedf43-942b-35e1-9abf-e0ab34a182ab | -6.90461 | -47.89999 | 2025-09-11 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9e05062e-522e-3463-bf46-6f9c5601d3d4 | -6.08404 | -44.81625 | 2025-09-11 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da651818-b2ce-3d86-aa57-26a1afdc89ef | -7.4193 | -45.87112 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b0f40235-416e-3c31-b5d2-8a18e177da47 | -8.56871 | -45.59407 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edd4e110-e389-3da9-a930-c156eabb0d97 | -6.17228 | -41.07608 | 2025-09-11 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f5e82af3-af64-3e84-9da4-9e77f9b11e79 | -7.26058 | -44.90567 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81028f7c-226c-3bff-93a5-f6b8d2401a9f | -5.59564 | -48.11205 | 2025-09-11 04:44:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe162871-59aa-3a9e-b72e-b6124a8e6b15 | -9.13584 | -46.19229 | 2025-09-11 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f3556fe-8905-34c6-bf5e-b55619e39f43 | -5.74514 | -51.69601 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c0066df-0a70-3af4-8964-df3aed9c1b72 | -7.055 | -46.23275 | 2025-09-11 04:44:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 363793b4-92c1-365a-aab4-6500946d2499 | -7.31908 | -49.6204 | 2025-09-11 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe47e605-a434-3aa5-b2d2-3ab10363717c | -6.43996 | -44.77428 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f538f123-e033-3b1b-959e-d8f3d51d41b7 | -6.37488 | -45.1644 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6cd4b173-e8d0-3dfe-b78a-e5c49cdb8e00 | -4.41276 | -48.95723 | 2025-09-11 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92fe7300-7637-3601-aeb0-22ba3b00f44c | -6.1556 | -45.81732 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20e6804c-c2bf-3825-a3a6-86cace85ba98 | -6.31742 | -43.40825 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README86.md)
