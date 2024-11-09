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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a51b8ad8-fbf8-30c2-ab20-4697ffbd581c | -2.87037 | -51.47987 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce1d11bb-0294-33a1-8aa7-b8153045dc3e | -3.59425 | -47.35138 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 2ace5f61-80ca-3975-9c5e-c494359b2fc3 | -3.61068 | -48.91962 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 15939ead-cffd-3103-9712-1f006d42c93b | -2.36539 | -54.75145 | 2024-11-09 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d5ebd9d5-65f3-391c-872a-e202c078efb7 | -3.23676 | -53.39195 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dcdd11b-e207-3429-acdc-becb284a46ed | -3.65541 | -50.13568 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e6f0018-c865-380b-affb-5f21076bb8d5 | -3.67088 | -50.21991 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88ffcdfc-6841-3e99-937a-acfc217ce8cd | -4.75694 | -43.86136 | 2024-11-09 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55468c0d-958e-3fa1-868d-d441c945bddd | -6.54917 | -46.91636 | 2024-11-09 04:33:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 768a02d1-e95b-3d3f-9d62-46b3a44742fa | -4.08241 | -49.29169 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 574b1399-850a-316c-8468-c4e29b518fcd | -3.40866 | -47.58232 | 2024-11-09 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b40e8a95-e7ac-32f2-a48e-57630d128503 | -3.79954 | -49.94028 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 95b8db1c-f936-31f8-b921-fe69ec9004ae | -2.82459 | -49.43016 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1309bec6-38ad-381e-b939-4e3a7c4e5803 | -3.3534 | -50.11901 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8d68c252-4d5f-3971-b9d8-eb3ceeb2b153 | -3.07141 | -50.56541 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c73b5b49-279d-3226-a658-1eebb2e2689a | -3.05161 | -50.37865 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 807f754d-50a6-3942-8796-8e77d2d271a9 | -2.87435 | -51.30682 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ce1add3-5878-35f0-a340-7ad271409870 | -3.9564 | -48.1671 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e9aecf80-9eaa-34c8-a6e4-3876dc3ae3de | -4.2559 | -47.57839 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 7d7fa560-d383-3fb8-a547-6ed63f27b883 | -3.5857 | -50.27772 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be2b09b6-4a32-3ad1-9dc7-162508194442 | -4.24983 | -47.57394 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| c5f0b6af-df37-3a04-b5d3-2f8c2cc5a6e8 | -2.88521 | -48.29276 | 2024-11-09 04:33:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 360bce90-3c87-31e5-af13-887b613c08ff | -4.75693 | -48.98159 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 615de342-3896-3c22-b9ff-4a866a40340b | -6.27627 | -44.74084 | 2024-11-09 04:33:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e30bdfc-24cb-3d21-9668-d76410af91d7 | -4.07784 | -48.3256 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d67fd644-1d5f-3553-92fe-31212623b666 | -3.26909 | -46.31349 | 2024-11-09 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c8b65d4-4ff5-3715-97cd-28bc8114f1b3 | -3.05442 | -48.03965 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f011da97-e014-335a-9148-04529768413c | -4.94195 | -48.24068 | 2024-11-09 04:33:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2afa1f49-5839-317c-862a-43b28396127f | -3.23004 | -50.43882 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0bf96ca-4166-3722-840c-3e84b48ff4c9 | -5.20225 | -47.46656 | 2024-11-09 04:33:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb13038d-1939-3869-8d50-fb9b320bb871 | -4.21072 | -45.85695 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ff184250-ba55-3627-ae39-eea8f04df746 | -2.73599 | -51.74503 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ed1de988-0856-32e6-9892-5630e0a75c4a | -5.14744 | -46.20934 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c40c9e4-137b-3bd3-92ba-d67213e99e49 | -4.13028 | -46.85675 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df76864f-0a47-3d0c-9b6c-fc501ba81b3a | -2.77947 | -49.38493 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 645137a2-607b-39f1-9600-de1550d39c16 | -4.19257 | -48.54803 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06f73679-0315-397b-83bb-10740151773d | -3.05226 | -50.37451 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44c4150b-600c-3d99-8281-827b580e9863 | -3.9625 | -48.1716 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 60f11459-4321-3b66-9d9d-68a84b9263fd | -5.98331 | -45.36729 | 2024-11-09 04:33:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 66d4d172-62c7-33e4-8b8e-56a1ef97da2b | -3.11969 | -51.10734 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fb232ba-8498-3768-baa2-687948c18ce7 | -2.69533 | -51.69829 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6730f41f-3cf0-3655-a028-9d918bd4a29a | -4.20001 | -45.859 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2c92ea04-0582-3e48-89cb-035fcfe68278 | -4.38257 | -47.22499 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a9f3656-3db7-386b-9e50-69536f22d8aa | -4.83032 | -47.31961 | 2024-11-09 04:33:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5302740c-a23d-30fa-81d0-c73a2d367e4d | -4.12722 | -43.59046 | 2024-11-09 04:33:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| da05670f-3845-3a3d-8c04-713cedaa4896 | -2.84187 | -49.2326 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17e7632c-6ad6-321a-9e67-32f188f5d419 | -4.43112 | -47.2607 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 377210c2-9ba8-30df-9b34-58692179fb57 | -2.64493 | -54.36875 | 2024-11-09 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| db4463f9-e40e-386f-88d5-90a1983904a7 | -2.58271 | -51.92553 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bdeb06c-5486-3ef7-a273-46cbd5fbd6d0 | -4.2141 | -45.85748 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9b72df2-b4ac-3329-8a51-b13ffd95889d | -3.1987 | -48.66084 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 274e27c3-7195-33c6-82e2-7defd44fe4d9 | -2.45514 | -53.69248 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6e45e27c-19e4-3cb1-8f7f-76b5313c87a9 | -3.04391 | -48.04159 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 835b7ccb-79ac-3727-974e-b4612ea67c3c | -8.69248 | -47.96446 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03538863-532e-3bf9-91ff-0df22b3fa56e | -3.98295 | -48.14997 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 991296c5-0d3f-32bc-ab39-34cb49c721dd | -5.62614 | -41.65623 | 2024-11-09 04:33:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| da46e21d-9d71-3338-bd8b-f9234e80793f | -3.96843 | -46.47499 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fceaa4da-b9b7-37a5-a913-56709217df45 | -3.73902 | -50.45052 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a3f46f5a-9e48-3be1-ab85-fc7d25fa45c0 | -3.59922 | -50.23851 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c108807-f174-3799-923c-2d5cd44eca95 | -4.28783 | -48.5699 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 195a9343-24c0-3e73-9f13-0e64d8fd88c4 | -5.00374 | -47.7558 | 2024-11-09 04:33:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2be06e1-0c4f-3030-a542-12a995acd945 | -3.30168 | -50.07923 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87ad1bc4-632a-37ac-bb0c-3b1b222dd473 | -2.8934 | -53.97366 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e5f473a-d524-385d-9c2d-3e9c4c7932b4 | -3.65526 | -50.13645 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e20a25a3-1e61-30da-a93b-cc513d8b1fe3 | -2.61454 | -51.74952 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13fe0cde-1590-35dd-870d-cfa7dbfcea4a | -5.31271 | -50.70273 | 2024-11-09 04:33:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78c80238-bad6-3ee0-9cad-1e3651d81541 | -3.03786 | -50.41908 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f9733a68-5588-370f-a82d-3585f11fd5b7 | -3.24041 | -53.39674 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bab7dcb-32ff-37da-b02f-1c3d3ea8a619 | -4.03567 | -47.13891 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea494901-4924-3f3a-a609-be56cab79e7a | -2.81421 | -49.42858 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5cbf96a-7655-3902-a5c6-6364c40fe86d | -5.52575 | -50.06291 | 2024-11-09 04:33:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50a81d23-abf5-300a-b9a2-224950380e39 | -4.16179 | -48.24586 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e0e56a7-3370-3c0d-8a49-8b55e8af5e74 | -2.77888 | -49.38871 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e0f63559-0801-3204-ac7d-a736ee1ceaa5 | -4.04828 | -47.38372 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b33c3a84-b79e-346b-8956-d123344fa8a3 | -2.87143 | -50.31796 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e690611e-8cd1-3a14-95db-ae98b74c7437 | -4.21035 | -48.54358 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61d084e9-20ff-35a7-983e-5438f5a4ca2a | -3.03784 | -50.32576 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 083a36ac-d585-37b5-9a72-6577ab99592b | -4.87699 | -48.63031 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94f63e19-491c-3392-89bb-1b43a1d35281 | -2.92271 | -49.36431 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 015c5aee-155e-353d-87b0-6c0750d6b6c6 | -3.95901 | -48.98918 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d66fbb3c-23a9-3768-9b1e-a49ec52d72e3 | -2.90637 | -50.39973 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0bebfc6e-490f-3220-b001-807294ec9153 | -6.2338 | -47.28408 | 2024-11-09 04:33:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 663a1f47-4777-3b1a-8b03-1c7b60315eea | -2.86423 | -50.31686 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6e45db25-c379-39a8-aa44-e7d1741de757 | -4.21182 | -46.44095 | 2024-11-09 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50b3c6b3-4d7e-3b82-b69d-9e2ebe636633 | -4.43903 | -48.06253 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2593f32e-f4ef-3c30-807d-2e4428278be2 | -3.97666 | -48.40606 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f005537d-1d25-396e-a629-391339899f41 | -4.73989 | -43.86037 | 2024-11-09 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34f438c9-cf01-3989-82f2-582a17805d6c | -3.15945 | -51.12293 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2b706a70-616c-3651-b476-5088825c2c99 | -3.05774 | -48.04016 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c50ff5c-0746-3952-aa33-c50e715b8891 | -3.2739 | -52.7448 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 85b49fbd-653e-362b-83de-2a1bedb91417 | -2.46037 | -53.68858 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7a9e2877-dc4a-36c8-9d25-eee73d826513 | -4.81797 | -44.35576 | 2024-11-09 04:33:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a706ab57-b6e5-3d39-94b6-8012aafdd6b2 | -3.81754 | -50.79992 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d54f58c-1d41-38ca-9994-38f19adc37a4 | -3.9703 | -48.18713 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| b4698975-d2ca-388b-bb69-6dccf0027490 | -4.8892 | -48.63942 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54a0b716-6812-3a26-ab9b-fcf834b5d8be | -3.2663 | -46.30948 | 2024-11-09 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a10d98bb-c960-31d3-87c8-2e55b31f0274 | -3.34235 | -46.65283 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70e26c45-a08f-3c87-a25e-22978d8c536e | -2.79157 | -49.66045 | 2024-11-09 04:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| e07ff196-84cb-3943-9e69-4730f1c3eb5a | -4.1393 | -46.90775 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a54cbbfb-f440-3eb7-9314-470076fa979b | -3.72904 | -54.21986 | 2024-11-09 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |


[Clique aqui para ver as próximas entradas](README58.md)
