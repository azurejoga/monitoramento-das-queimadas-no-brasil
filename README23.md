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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 022ba142-aa2e-3cef-af53-8cbf693af42c | -22.89706 | -43.65972 | 2025-11-13 04:18:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f0b5f61b-489f-302a-ae4a-27816d7551da | -22.47216 | -44.19783 | 2025-11-13 04:18:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 74502df0-4105-3ca4-b278-a5d115d505a1 | -22.46809 | -44.2014 | 2025-11-13 04:18:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 7d950ccc-8153-3259-85d8-f6148a8dd76a | -21.8542 | -45.01493 | 2025-11-13 04:18:00 | NOAA-21 | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 823803da-6530-3b02-9b52-7c33cb01415b | -4.2056 | -48.5706 | 2025-11-13 04:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 6744d4f6-81b4-3422-9dac-88bc758d39f3 | -4.7204 | -46.4497 | 2025-11-13 04:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| dcdc6966-91d3-327e-83f9-09cdc20786f5 | -12.6557 | -46.7407 | 2025-11-13 04:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 36ea1303-4cb5-3eda-b5d1-a6111e9fb492 | -4.7018 | -46.4508 | 2025-11-13 04:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 33.2 |
| c882ec73-8538-366c-b1f4-7f86ca346268 | -4.7206 | -46.4276 | 2025-11-13 04:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 43.2 |
| f39a5bb9-3af9-3209-93b3-e7a64af3726d | -3.0916 | -49.2759 | 2025-11-13 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 025826ff-6873-38e4-911e-28c9cda26365 | -4.7206 | -46.4276 | 2025-11-13 04:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 05229d63-9416-3dde-8d99-0723a8027e76 | -12.6557 | -46.7407 | 2025-11-13 04:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| c17c4ed0-815a-3ea2-9ed3-7c64852a3c47 | -3.0916 | -49.2759 | 2025-11-13 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 86ae08a8-cf52-37d3-ac9b-af2f128b2e1e | -4.2056 | -48.5706 | 2025-11-13 04:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| ca077720-1c93-3a3e-9d53-edaa362ac4a9 | -4.7204 | -46.4497 | 2025-11-13 04:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 36ed94cb-829c-3a8e-9205-9b1ece7c4989 | -4.7018 | -46.4508 | 2025-11-13 04:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 33.9 |
| da2c6b3b-d601-3399-b4c9-471abb6a60c1 | -4.7204 | -46.4497 | 2025-11-13 04:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 3154c7bc-dda9-33c2-a535-f6c04bc823d7 | -3.0916 | -49.2759 | 2025-11-13 04:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| e0e354f5-1602-3cd3-b8e5-c69867af67be | -12.6557 | -46.7407 | 2025-11-13 04:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| aefbc76b-dae3-31bd-8987-a059add56a71 | -1.24873 | -47.05805 | 2025-11-13 04:40:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ddc98fe-999d-3684-bcd5-6aa35fb40b5d | -1.34226 | -46.69025 | 2025-11-13 04:40:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e014cb6e-282a-3a63-be57-646e353e0a6a | 3.29827 | -60.12894 | 2025-11-13 04:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee3873d1-f441-3e15-b5ce-03d641a98143 | -0.99413 | -48.09222 | 2025-11-13 04:40:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5787cac5-5257-3e14-b06e-69c0c3f61c36 | -0.72379 | -48.64302 | 2025-11-13 04:40:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2223f1d-8a99-3f2a-8b9e-e6e462a7f779 | -0.75235 | -48.52718 | 2025-11-13 04:40:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c2acbd59-3ee4-3126-b80c-a37f019c29f3 | 1.45538 | -55.85919 | 2025-11-13 04:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd5eb78d-40b7-3292-a956-b5683c075c29 | 3.32732 | -51.33703 | 2025-11-13 04:40:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc9e628a-b557-37db-80ba-179cbbe7c013 | -0.03082 | -51.09412 | 2025-11-13 04:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf388501-2ecb-3d42-a756-f08c3ce0fedc | -0.50651 | -48.50239 | 2025-11-13 04:40:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e718346-18c1-37b5-801e-967b4b07076c | -1.02575 | -47.63383 | 2025-11-13 04:40:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4c447c4b-0db9-3a1e-b955-5931f0c1c647 | 3.53792 | -51.7755 | 2025-11-13 04:40:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b90d191-5728-39e8-8baa-4e9a9cdffee4 | 0.6591 | -51.54288 | 2025-11-13 04:40:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f370335-0fc3-3b3b-a3ba-4197e740429d | -1.14396 | -47.91413 | 2025-11-13 04:40:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 51c25fa9-69a2-351e-a268-8dc27a367ed3 | -1.14397 | -45.71505 | 2025-11-13 04:40:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 417bff51-4321-3ba4-a257-a03c3f362bdb | 1.45996 | -55.8555 | 2025-11-13 04:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2aebd7b3-5f03-367c-8af0-04ff12c03603 | 1.45493 | -55.85627 | 2025-11-13 04:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a612e96-1030-37b3-9583-4758d051773f | 0.6196 | -51.565 | 2025-11-13 04:40:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbeaf647-3b89-3e27-9ab1-0799c6517f76 | 1.45929 | -55.85119 | 2025-11-13 04:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9a44e894-4445-370d-ad96-497fc3af19a4 | 3.30514 | -60.12829 | 2025-11-13 04:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 909b35f5-8cd0-3e3f-836d-dc75510597e8 | 1.46041 | -55.85842 | 2025-11-13 04:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1f137e2-9610-35d4-8e1c-f35f7598e647 | 0.79516 | -50.8657 | 2025-11-13 04:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a36e71b0-4eac-35a5-828d-be22d52106bc | -3.09388 | -49.28164 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20b04ce3-c147-38d4-a370-370116e1d983 | -5.5622 | -50.02133 | 2025-11-13 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 654b1524-5c99-364b-9c36-36360e7ab673 | -3.34155 | -48.37919 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7100b103-ac45-3340-86f6-1544b1520259 | -5.83767 | -38.34939 | 2025-11-13 04:42:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 594622ac-6aa4-321b-87f5-da5bc25dce9e | -7.47739 | -42.56608 | 2025-11-13 04:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f2498a53-8054-35c8-b678-8c1b792145a6 | -3.85852 | -49.79489 | 2025-11-13 04:42:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04736906-d952-3975-9262-38d217febcd6 | -3.46726 | -43.18748 | 2025-11-13 04:42:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 415e34d6-818c-360e-a388-cb70920d56e2 | -3.57184 | -44.16273 | 2025-11-13 04:42:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9b9c2bd-a5e6-3ff3-adc4-41648198c810 | -5.0889 | -40.24115 | 2025-11-13 04:42:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 841bd26f-ae13-3d27-9419-e720ddeea613 | -5.35735 | -46.76108 | 2025-11-13 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8bbdd949-00e6-3514-be7f-5bf72ee44142 | -4.0122 | -48.80252 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 919f44a3-7fd9-37d1-860f-e218726c99db | -1.76491 | -54.13518 | 2025-11-13 04:42:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e66ddda6-31a2-3346-8890-c2f5f1717771 | -4.10141 | -48.01963 | 2025-11-13 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b652c91-2f8f-3ed3-a9fe-36cb1f664d4f | -5.04152 | -49.97837 | 2025-11-13 04:42:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8be2003d-9de6-39c7-87cd-c9f5ccbe82b0 | -7.82231 | -41.76064 | 2025-11-13 04:42:00 | NPP-375D | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7184d5eb-6c27-3d74-aec0-b67f912b23d6 | -3.94116 | -50.66033 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2dad6aca-883a-3358-94b4-7d54af5b891f | -6.68729 | -47.79937 | 2025-11-13 04:42:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9e1997a4-422f-34c1-b970-b189c5dbaac2 | -3.84602 | -50.05759 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6542f412-1b1b-34ca-8595-7d78f6e016b9 | -7.21811 | -47.97742 | 2025-11-13 04:42:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b89f98bb-c596-3af2-8c09-8314423d2d0d | -3.03303 | -50.28738 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f18f30fa-80c4-3c5f-a179-70e4862d8c5f | -3.34487 | -48.37971 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2f48a12-5d80-3ddd-baec-71208c10e9ee | -7.49194 | -46.97911 | 2025-11-13 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0337e5dd-65fc-3c26-9e2a-cda3f026a00c | -2.52462 | -47.80692 | 2025-11-13 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb6c886c-bf50-3c04-bf06-3c786f731bef | -4.71793 | -47.22434 | 2025-11-13 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76745569-9e99-37e0-b362-d2d3d153e389 | -1.7928 | -48.06937 | 2025-11-13 04:42:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d85f3ed-0a2a-3134-8881-52e3b3f7bac2 | -3.46727 | -50.58653 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6b3be98-5497-302e-971d-64d081352283 | -3.09498 | -49.2747 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d7dcc488-80a1-34af-90ef-df6b9a8fc664 | -2.9709 | -47.89788 | 2025-11-13 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6aa6bebe-fca6-35bd-b323-d524e21b8ad6 | -4.62597 | -42.79147 | 2025-11-13 04:42:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b11dd4b0-8051-3db2-9131-70263307051f | -5.76203 | -46.5201 | 2025-11-13 04:42:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c5147d1-6f0a-348d-b75d-d6ac9673afb1 | -5.44615 | -44.65564 | 2025-11-13 04:42:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e7a30e3e-a3c7-34ce-b897-87ad862a18df | -6.58786 | -48.03813 | 2025-11-13 04:42:00 | NPP-375D | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b64dccc-effe-331c-a8c7-5c86128cad2a | -3.85797 | -49.7984 | 2025-11-13 04:42:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ab917b8-6c5d-3e12-b61b-6f411143d10b | -3.09651 | -49.28208 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9549e4e5-1e2b-3914-aa25-cdc66936c06e | -4.19698 | -46.22388 | 2025-11-13 04:42:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 447eac2b-6c15-3c68-a333-b3fa777db335 | -2.46796 | -49.06542 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dbf86da-6a4a-307f-9671-3743b0beba3c | -5.55289 | -46.87223 | 2025-11-13 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7469f412-014a-3ba4-b0c7-b1077faaf0b9 | -3.40616 | -46.90602 | 2025-11-13 04:42:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bc74292-0e5b-3af8-baa0-1d5f007f2f7b | -1.93704 | -52.09444 | 2025-11-13 04:42:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b58386bd-3045-3a8c-acdb-289a2ba6d2c4 | -4.31081 | -48.23888 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fae97fb9-358e-3ebe-8771-dedca173cc54 | -4.64291 | -48.74995 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6348cf14-521a-3fed-8603-cd5a4105f0ec | -3.15747 | -45.8156 | 2025-11-13 04:42:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49f11567-e979-3726-8048-fa834aaa8859 | -5.60997 | -41.06465 | 2025-11-13 04:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3678b682-aec8-3d52-abe5-248b79521a6a | -6.35539 | -39.79321 | 2025-11-13 04:42:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 074c5aeb-f567-311f-ab9f-bc0ed64eb894 | -3.86131 | -49.79893 | 2025-11-13 04:42:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 949160d6-70d7-38bf-a184-9f5868bef0cb | -3.37292 | -48.41223 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cd8b670-6e6d-3284-b516-ae4655f2cc19 | -7.10059 | -42.36875 | 2025-11-13 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6e75de5b-e07a-3a71-b986-c232e8c2a240 | -5.66191 | -46.22687 | 2025-11-13 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 775e0a5c-2e4e-3dc3-a317-70754da196ca | -3.10937 | -50.20243 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 500b5b1e-3848-3ab1-a020-0317eb4a8bd5 | -4.21121 | -48.56857 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 8c0c2051-c719-389a-866e-8e0ccb27c7d6 | -3.26294 | -50.02793 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eda5da20-8fbd-3c75-837d-2c9e8f0a3aea | -2.72291 | -47.40898 | 2025-11-13 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e42680c3-78b9-3c46-840a-ff4075f7975c | -4.68003 | -45.84955 | 2025-11-13 04:42:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14d0cc82-d749-38b5-8eed-092f3f09746e | -3.4861 | -44.04446 | 2025-11-13 04:42:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ace40d7-df5d-35fb-8cc0-e30671d7c4b4 | -4.62662 | -42.7872 | 2025-11-13 04:42:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09244746-c9e5-3e47-abd0-4a8bd5070034 | -6.29378 | -41.74016 | 2025-11-13 04:42:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6330ee19-4c42-30fc-bc39-b87ecd3025b8 | -3.78502 | -42.75074 | 2025-11-13 04:42:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 60369ff6-de96-34ad-bb44-cdfa9e587485 | -3.13973 | -50.2739 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 862d3db6-29f3-3a41-ad0c-026813954ad5 | -7.45794 | -44.73867 | 2025-11-13 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README24.md)
