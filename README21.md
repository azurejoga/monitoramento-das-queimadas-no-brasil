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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4994593f-a708-3988-818b-1ad63a53143c | -4.5614 | -48.0141 | 2024-11-17 03:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e7b00969-470e-3b0a-bbbe-0eda41589433 | 0.6159 | -51.7881 | 2024-11-17 03:40:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 56.8 |
| bd263672-510d-3b88-b653-e93b8094efdb | -8.4525 | -44.1999 | 2024-11-17 03:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 2a4836e4-4252-35d1-82a3-08f660488181 | -4.5616 | -47.9925 | 2024-11-17 03:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| bbcde53d-364f-3680-b3e7-e1f7c6175fe3 | -3.5309 | -50.2547 | 2024-11-17 03:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 226.2 |
| fabc83cb-b142-3445-8978-9978374ca68a | -3.5124 | -50.2553 | 2024-11-17 03:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| c399781f-aee0-3337-beb7-3e6146377e6b | -17.6059 | -57.5921 | 2024-11-17 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.6 |
| 91d6e5ae-afc3-33e8-b87f-0c91e5bc5215 | -3.5308 | -50.2757 | 2024-11-17 03:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ceda2c59-aee6-321f-ae51-11bb3d54350b | -2.6322 | -48.5634 | 2024-11-17 03:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 5be8959b-791a-36ab-bad2-49f751df4f80 | -3.531 | -50.2337 | 2024-11-17 03:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 7966a854-ea96-3f56-8839-4ffb078f2cdf | -3.5125 | -50.2343 | 2024-11-17 03:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 144ecced-73ca-313f-ad4d-96fff2e5c765 | -3.5494 | -50.254 | 2024-11-17 03:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 15a86dd4-042c-3465-98c2-a05fe1c258b2 | -1.911 | -46.57066 | 2024-11-17 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 167164d0-7503-34a6-b495-504e2dd30430 | -1.49275 | -47.39554 | 2024-11-17 03:42:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b9e05dc8-b012-3ce0-b552-3560b14179b9 | -1.9101 | -46.57615 | 2024-11-17 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| bee27cc8-ed98-3dc0-a816-cccedcbf6af8 | -2.00672 | -47.4625 | 2024-11-17 03:42:00 | NOAA-21 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 42844174-55e3-3f0f-b4e1-311215eb7ca0 | -2.20468 | -46.0429 | 2024-11-17 03:42:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 50655063-ba4a-3661-9388-92c84c5f6e23 | -3.50152 | -39.31578 | 2024-11-17 03:42:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6df2cb56-2af6-3045-bdd8-72ac1db8654d | -2.47568 | -45.62182 | 2024-11-17 03:42:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac855906-26f2-3754-a9c0-50ba6e38611a | -1.22857 | -47.36111 | 2024-11-17 03:42:00 | NOAA-21 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9ec08058-c41f-321a-9c7e-716301dcefdd | -2.06277 | -46.5421 | 2024-11-17 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c81c4077-bbce-3066-a041-ba5738935a19 | -2.06186 | -46.54751 | 2024-11-17 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c5f144f3-9383-3c86-b78c-d063bb723b6e | -1.9102 | -46.57752 | 2024-11-17 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| e5e650a2-e3d9-37fe-bbc8-fb6e84f8ae13 | -2.00508 | -47.46452 | 2024-11-17 03:42:00 | NOAA-21 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7fc689c-fd3e-32c6-926f-22aa88742347 | -1.91114 | -46.57204 | 2024-11-17 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| da6a3d09-139f-3277-8d3f-7f7c87b0ae8d | -1.52234 | -47.47174 | 2024-11-17 03:42:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 730f9504-c476-35bd-ab48-2abe3ee1ae2a | -1.22957 | -47.35496 | 2024-11-17 03:42:00 | NOAA-21 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3617c67e-a333-3db6-b60a-3889bc6f1e77 | -1.83318 | -46.59772 | 2024-11-17 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 184ab9e2-2595-3814-ad4a-3832297fdbc7 | -1.83314 | -46.59858 | 2024-11-17 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6e07e6d1-a9ff-3b02-bd02-4744253e6de4 | -2.00608 | -47.45837 | 2024-11-17 03:42:00 | NOAA-21 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 87fb39ac-5eda-3b8d-8921-981061384527 | -2.21612 | -47.22275 | 2024-11-17 03:42:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 72d91d37-6957-365b-878d-1798d5404d32 | -1.49885 | -47.39553 | 2024-11-17 03:42:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fa945a0-8b02-33bc-b765-9821ba607c4d | -2.46429 | -45.61538 | 2024-11-17 03:42:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d8cfd67-83af-3b8c-8e86-9c758202e0b2 | -1.91207 | -46.56657 | 2024-11-17 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| b536fafb-218d-3fc1-9864-2559a43911dc | -2.06171 | -46.54564 | 2024-11-17 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 62e23f1f-a04c-3234-a626-d50ab564e0ad | -2.45976 | -45.60527 | 2024-11-17 03:42:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 40ac01bb-82fd-3a02-bb57-6b4f29be526c | -1.83403 | -46.59309 | 2024-11-17 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 572ef912-b636-3872-b0d7-7e43c13484f0 | -1.49201 | -47.39438 | 2024-11-17 03:42:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| afc9b67b-5f6c-3ec1-8bae-93f6eb38ce12 | -2.46506 | -45.61081 | 2024-11-17 03:42:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 76cc6030-9bb0-3615-b2d4-60927a386661 | -2.21713 | -47.21669 | 2024-11-17 03:42:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 75c5e830-cee2-3d69-b3d5-855a72e29b78 | -2.47492 | -45.6264 | 2024-11-17 03:42:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78649b93-78d0-3221-98bc-62fd18edbc0e | -1.8437 | -46.53311 | 2024-11-17 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c4f7749-13fe-372b-83df-2c0fb52b40ee | -2.45899 | -45.60986 | 2024-11-17 03:42:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 181e2a53-e5fd-3203-a689-80211dd631a3 | -4.54295 | -45.25083 | 2024-11-17 03:44:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3c7a6da1-e2b5-3bbb-9a37-2e6a9ea1f54f | -8.43938 | -44.19239 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 665c7ff0-ce31-32c3-8a8e-90fb21dd4f7c | -4.99955 | -44.33866 | 2024-11-17 03:44:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c404b31-43e3-3124-bbb3-470b744efc6f | -6.17441 | -41.16601 | 2024-11-17 03:44:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cd11b63a-a0c9-344b-ac6f-6b6fbf413c18 | -5.51365 | -46.41737 | 2024-11-17 03:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83acb37e-fed1-3553-aeee-a68a985fa12f | -2.67239 | -46.21497 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 94a4fe4c-d81c-33c3-859b-7ef4683269b8 | -7.30405 | -39.61955 | 2024-11-17 03:44:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5142cbcb-a9ac-3d4e-b937-e3e1f10dfe8a | -8.27809 | -45.96542 | 2024-11-17 03:44:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 33210cea-18cf-31a0-bd8b-8141cf8a25b5 | -3.20838 | -46.68326 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8085e472-2dd8-35af-ab90-546a7c4c35bd | -7.6598 | -38.84101 | 2024-11-17 03:44:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e1c7df1e-1a69-3d43-ae8c-452d4ee5acd7 | -5.33665 | -40.90133 | 2024-11-17 03:44:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 506fc02c-7571-39e4-8c0e-7dddc8101b44 | -5.33554 | -44.99739 | 2024-11-17 03:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4b0d8e1-32fb-3ca0-be70-63d5ba75ceeb | -7.83737 | -37.69655 | 2024-11-17 03:44:00 | NOAA-21 | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 04760dd5-bc48-3915-a764-0fd8b0d28f65 | -6.38656 | -45.68821 | 2024-11-17 03:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 233ddbbc-f20d-34ca-8522-87c30efc9631 | -5.31515 | -45.44808 | 2024-11-17 03:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ad755b7a-0f63-3548-b315-586e3fa10ddc | -5.49585 | -39.53222 | 2024-11-17 03:44:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d17738a4-baa7-3036-80c9-831b90bde5d0 | -4.23963 | -41.93386 | 2024-11-17 03:44:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 82a9c3f9-3df5-3174-8da4-ea7aba25ffa2 | -7.58336 | -39.05089 | 2024-11-17 03:44:00 | NOAA-21 | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2a844ea6-ea91-3564-91aa-f68dc8862b1f | -2.60662 | -47.56073 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 64ca1897-281c-30d7-addb-92fd1fc244db | -4.58208 | -48.02193 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6528b36c-30f3-37b8-bed8-67749d96acb2 | -5.42375 | -45.34106 | 2024-11-17 03:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6f0b4443-ca7c-33cb-a83d-53e2b2c74612 | -6.83185 | -39.82412 | 2024-11-17 03:44:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 07faae39-9316-3e6a-ad5d-4f6605180069 | -2.86826 | -46.71731 | 2024-11-17 03:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 7321df00-58bc-3acd-b3b5-7d0313057347 | -5.70614 | -41.65015 | 2024-11-17 03:44:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 34963f7d-68c0-373d-847d-49a77481c82e | -8.43835 | -44.1982 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 7b7d6cd5-b6cb-38fa-86f2-1a9cb4da7f46 | -4.55569 | -48.00319 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 844019a4-1a73-356f-8bd5-e4f36740bb31 | -2.65626 | -46.21052 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 62edbad5-083e-38ad-a029-68a828ff33dd | -8.44833 | -44.20019 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b64634e9-73a6-3508-9f41-242a78492639 | -4.55605 | -48.0111 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 1383cd62-8cc5-3a12-926d-a16b36db7ec2 | -3.74386 | -44.52847 | 2024-11-17 03:44:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e8fade2-40ef-392d-ab4c-727ae8f2bc65 | -8.44678 | -44.20892 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b70688e-3510-3373-a16c-3732c45dedd3 | -3.41718 | -46.13281 | 2024-11-17 03:44:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb900551-2256-3b27-b552-dce12d0fe4d6 | -2.35349 | -47.46666 | 2024-11-17 03:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a1621082-0139-3626-8dc4-cd303df64bc9 | -5.40548 | -46.35226 | 2024-11-17 03:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d843690b-0a10-3b50-8b6e-dd31e84ad310 | -8.4538 | -44.19841 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 227f9e3e-7f01-37f9-88e3-f9069c678c6f | -4.72545 | -46.84268 | 2024-11-17 03:44:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f866ec31-1ead-3255-b239-8b3caf6d4541 | -9.37222 | -40.34291 | 2024-11-17 03:44:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f51c19f0-ae3c-3c45-b135-75094655d8fa | -4.24742 | -48.53404 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 222e9188-cf63-3485-b3ea-e4ca04a67c75 | -3.50089 | -43.78528 | 2024-11-17 03:44:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f0625f7b-266d-3003-8f2d-a48babd87ae5 | -4.11872 | -40.54412 | 2024-11-17 03:44:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bd5ac71a-27d3-3c9d-a2d4-eb5217c7784a | -5.62992 | -46.36865 | 2024-11-17 03:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65ead2d6-afa3-3329-b0f7-104a98cd3380 | -5.51559 | -41.08079 | 2024-11-17 03:44:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 18f7a879-4058-36fc-a9b7-71703c8fe17f | -3.62699 | -43.15948 | 2024-11-17 03:44:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d96da2be-92f2-3824-81fd-0dfa646322f4 | -5.69491 | -46.56884 | 2024-11-17 03:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f19e151d-8019-31ca-ae14-94b955e3e3fa | -4.47447 | -48.10528 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 54c7adc9-84af-3be9-8dcd-e1f3f57f2688 | -2.60183 | -47.54756 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4c1d25bb-01e7-36c6-80e3-299a06eccda1 | -8.4473 | -44.20599 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 763b6d5a-08b7-3e30-8551-09a51a8b1215 | -2.59979 | -47.55977 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 38abc04d-a61f-399b-a6e6-5152c048dd62 | -3.78576 | -46.0439 | 2024-11-17 03:44:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f6a7c50-2e88-350f-9239-f4da892dd6f7 | -4.63589 | -42.91277 | 2024-11-17 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c573fc1e-dd48-3967-bbfa-050653bb7ebe | -4.2846 | -48.21217 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0ba44e5a-9b7e-3004-a2a2-a15ff58798b3 | -6.99063 | -39.657 | 2024-11-17 03:44:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6232f356-91fc-3955-87aa-9c3c87c94395 | -5.31444 | -45.45218 | 2024-11-17 03:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 24de958c-bb2c-3955-b99e-d7e86912100e | -2.67745 | -46.18505 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8c59ca0f-89f6-3f49-99d3-6a7281345c64 | -6.1523 | -41.14193 | 2024-11-17 03:44:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cf3735e4-11af-3679-9dc8-07776497f23e | -8.13079 | -41.12772 | 2024-11-17 03:44:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 6cd62a1e-ae71-358e-986d-ee578dbb21db | -3.9179 | -46.52155 | 2024-11-17 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |


[Clique aqui para ver as próximas entradas](README22.md)
