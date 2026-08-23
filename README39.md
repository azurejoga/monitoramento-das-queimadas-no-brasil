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
| 1a400312-3725-3e71-8b06-15414a048c27 | -6.8062 | -58.6469 | 2026-08-23 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 72b4bc05-12b8-3d2d-83a4-351b044b184c | -6.6581 | -58.7306 | 2026-08-23 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c1fdfbe5-b717-3605-ac30-5167f3578759 | -6.6949 | -58.7485 | 2026-08-23 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| de9c3fa3-a461-3795-ad16-3282327a2495 | -6.9699 | -59.0658 | 2026-08-23 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 04c9f6bd-476b-33ae-9630-3011f6f56c71 | -13.1509 | -51.4068 | 2026-08-23 05:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 208a9969-b8d0-351d-a5e7-af19cd4351ed | -6.6765 | -58.7492 | 2026-08-23 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 1e4d7f76-7ee8-35fc-b4e4-fcbb4baa6062 | -16.0509 | -50.4363 | 2026-08-23 05:00:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 136.9 |
| e0096cfb-9e01-398a-a42d-8edd83e47589 | -6.6766 | -58.7299 | 2026-08-23 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 53063e04-0138-3076-830b-d1ebbfbef523 | -6.1285 | -57.8393 | 2026-08-23 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 5e099dd0-1847-3f1e-a61b-fb1dabede476 | -6.1286 | -57.8198 | 2026-08-23 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 27af74bb-a56b-3a16-be8e-275c49bbc7f1 | -6.8188 | -59.6696 | 2026-08-23 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 50dc2130-832e-3dc8-827b-3ba33ade75aa | -13.1697 | -51.4258 | 2026-08-23 05:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| d2e3deca-95d9-3826-9cdc-ffcbb93176dc | -6.695 | -58.7291 | 2026-08-23 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 188be504-6eac-36c9-b162-bc4e86f753d0 | -10.8361 | -50.9691 | 2026-08-23 05:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 32.9 |
| be3ae20b-cfaf-3d4f-bf58-c912ded3da93 | -2.53743 | -54.01339 | 2026-08-23 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 062bfa1a-7e2c-344c-baec-a312228cbd4f | 2.78683 | -50.94678 | 2026-08-23 05:01:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e318574-4345-3e82-a959-30bd395aaa5b | -5.1696 | -45.05894 | 2026-08-23 05:01:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b93e9369-11fe-35fc-9724-5b43ecf84a2e | -4.1719 | -42.44233 | 2026-08-23 05:01:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| eac579c8-7517-367f-af80-10a91c3ec23c | -3.69985 | -53.68919 | 2026-08-23 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea5f5c0a-8c95-3490-98f4-60b12addb20c | -3.7037 | -53.68627 | 2026-08-23 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7a10684-a11a-3f15-909e-12ae1f6b60f5 | -3.87092 | -48.0481 | 2026-08-23 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6adba911-cd7f-3a38-825e-5bebed7851b2 | -1.67304 | -54.72464 | 2026-08-23 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f359cd25-d4c1-3e12-9eb8-528bdaf9392a | -2.55827 | -47.25131 | 2026-08-23 05:01:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 86e4fab1-8b77-35c9-b4cb-5f595e3ae219 | -2.49967 | -48.13695 | 2026-08-23 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ace6bcfd-0133-33e0-b5ed-4b63a774f3bb | 2.79634 | -50.94162 | 2026-08-23 05:01:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c7fb593-25bd-308e-b142-8de917b9b10e | -1.33294 | -47.95889 | 2026-08-23 05:01:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da979532-cf4f-3d51-be59-d316d2fbc4ad | -1.74701 | -55.24954 | 2026-08-23 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09246d2e-4490-31d5-90f8-6e4ebd610eec | -1.32884 | -47.95826 | 2026-08-23 05:01:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4117bbb2-6d16-32d7-9fba-7c843dad99cb | -2.56266 | -47.25201 | 2026-08-23 05:01:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ab56e194-115b-38fe-849b-356d386ca51a | -3.01454 | -51.05856 | 2026-08-23 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7996632-8f60-3337-8faf-0a39076e5907 | -2.99109 | -48.96303 | 2026-08-23 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33efb81e-5475-3a1d-a7d1-8b87f71129b9 | -4.16501 | -42.4462 | 2026-08-23 05:01:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7e77d043-2b8f-33cd-b381-19ab80db332b | -2.95649 | -50.31781 | 2026-08-23 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10bbf881-6523-3b59-9777-271739512498 | -3.53865 | -48.18233 | 2026-08-23 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ce74638-cc4b-39c6-9d2f-48a58b389b34 | -3.2657 | -49.52456 | 2026-08-23 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37d977f4-2ecc-35e9-ad15-b874f96c0572 | -1.74359 | -55.24901 | 2026-08-23 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38cbc1ce-a663-30c9-ae58-31705d559207 | -1.61282 | -54.39946 | 2026-08-23 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23b5d966-ff23-313b-9277-8c21ec22ae5a | -3.654 | -49.44519 | 2026-08-23 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11af6606-03d5-3c01-8bc3-3da8d3d1c456 | -2.35325 | -48.83286 | 2026-08-23 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99b4bc8e-ddbd-347d-8832-a9be75cf3f15 | -3.69208 | -50.93425 | 2026-08-23 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c63ded1e-3ebf-3316-918d-8a4540424706 | -4.26325 | -48.19621 | 2026-08-23 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c67b7f95-b0d3-3094-a0c7-51d255241b03 | -4.16691 | -42.44459 | 2026-08-23 05:01:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cdeacecd-b0f7-3cad-a266-41bf3789388b | -1.41871 | -55.72474 | 2026-08-23 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7de5b081-d50b-3a6e-8cc9-d07d3faca301 | -2.45902 | -49.28647 | 2026-08-23 05:01:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 94bfa7ee-466f-3c8c-906a-2d0be765e93e | -2.98715 | -48.96245 | 2026-08-23 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b93e5b6-adb4-3c45-b933-29dda45e2997 | -3.70316 | -53.68971 | 2026-08-23 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2bcb2d4-9c91-37ef-a8f7-7404ac1c564c | -5.16427 | -45.05831 | 2026-08-23 05:01:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8ab2161-0f53-3f16-8653-9cb8cadd8f1f | 2.78626 | -50.94321 | 2026-08-23 05:01:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef1b8f62-4893-3b16-bb15-d6fecd7c2b22 | -1.71933 | -55.07231 | 2026-08-23 05:01:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 017024b3-067f-34e2-861d-454a2ca0af8d | -3.24792 | -54.30997 | 2026-08-23 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7555dfe8-c779-3798-b8f1-636ac1fe2fbe | -3.05697 | -50.34471 | 2026-08-23 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab528ee2-566d-31b3-8cbd-64a3c5df0fc4 | -4.31243 | -46.41758 | 2026-08-23 05:01:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c19bc548-ea66-35b3-a1fa-79ba03449f96 | -2.56332 | -47.24771 | 2026-08-23 05:01:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| aa1ab0ff-97a0-3aab-9e92-320ce8b6e054 | -3.58049 | -51.20927 | 2026-08-23 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 862efc9f-02f2-3031-b1a4-270556f693c5 | -3.42655 | -48.94048 | 2026-08-23 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c95452f6-f85a-3ce9-8b52-84d325e03fe5 | -4.16569 | -42.44134 | 2026-08-23 05:01:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 33e0f9f6-665a-3f20-afb9-53634fb7b256 | -2.99088 | -48.95983 | 2026-08-23 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7954aabd-fce3-3b45-bce8-a5359d1868e2 | -1.76672 | -55.32479 | 2026-08-23 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a1643d1-a5eb-3256-aee4-8bc0dc66215a | -4.26807 | -48.19292 | 2026-08-23 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c2c6b3d-4ef1-3c89-bdce-00b135384fbd | -4.30765 | -46.41689 | 2026-08-23 05:01:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48d8b82e-b461-3b21-b881-12617002af9f | -1.98524 | -47.96577 | 2026-08-23 05:01:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ec2ea9b-6791-3478-b100-0c1cebfc5c4f | -3.01514 | -51.05465 | 2026-08-23 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b8999ab-024a-3eb6-960a-aedc629ce68a | -1.61226 | -54.40298 | 2026-08-23 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 707d3fb1-c5b2-34eb-b226-937309169c38 | 2.79298 | -50.94215 | 2026-08-23 05:01:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d43500cb-6fb8-3445-ae08-038806c1624f | -3.01163 | -51.0541 | 2026-08-23 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2a2c140-cf95-36b8-937b-684fe2e5c22c | -2.91276 | -48.86848 | 2026-08-23 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 213920f6-7f18-3964-9ce0-571e55798bb2 | 2.79076 | -50.94981 | 2026-08-23 05:01:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c3d03c38-5595-3ef9-8339-221b7c3e9fb4 | -4.16763 | -42.43974 | 2026-08-23 05:01:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2d0dca5a-8ea9-3e81-8c54-a4d8d95d0715 | -3.26952 | -49.5251 | 2026-08-23 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c02e3d6-3201-3000-84ac-a188dec3b6de | -2.98694 | -48.95924 | 2026-08-23 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4e0abe34-9ad2-3c05-90b6-1cfca93a2c6d | 2.79412 | -50.94928 | 2026-08-23 05:01:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4073212-25e9-3552-b8a6-20805fb3517d | -1.9809 | -56.46928 | 2026-08-23 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7405f1a1-be88-3f9f-a950-5def1614c5a8 | -3.7004 | -53.68575 | 2026-08-23 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36e74c07-0482-3e24-bf02-79fccac0ee97 | -2.53798 | -54.00993 | 2026-08-23 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f45b1c21-7532-3e0d-8552-67f6fbebec92 | -2.99188 | -48.95801 | 2026-08-23 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4346f720-607e-3ebd-a735-7b67d86d1d59 | -3.62826 | -54.52661 | 2026-08-23 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| aafd7131-7d21-3e27-812f-e3a33ddb7e75 | -2.89278 | -48.79548 | 2026-08-23 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a13d6b6-7280-3242-843c-5d496900d7b2 | -2.98794 | -48.95743 | 2026-08-23 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ef67ac1-5aa0-3985-ab25-2eb58860c15d | -2.91198 | -48.87358 | 2026-08-23 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bb1068bf-28d3-37cc-bab2-a0db1a413649 | -5.16909 | -45.06239 | 2026-08-23 05:01:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c0b9983-04c9-3d08-97e7-eb517d2de1ae | -2.52115 | -54.88249 | 2026-08-23 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b04a89aa-fe02-3c5e-bb2e-ffec4a5ff994 | -3.62771 | -54.53008 | 2026-08-23 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 8bfda6ff-f993-38f3-86ea-b49e063c5bee | -2.148 | -56.66729 | 2026-08-23 05:01:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ced14b05-c910-3c9e-b13e-0bdfcd7c5177 | -2.56771 | -47.24839 | 2026-08-23 05:01:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 48f84059-757d-3556-994d-612000629819 | -1.7666 | -55.32367 | 2026-08-23 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 399837a5-a3b8-3652-af1c-6d00930d96da | -3.42836 | -48.93892 | 2026-08-23 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bdd522a-b87a-3c40-a9a5-3131581459c5 | 2.78791 | -50.93198 | 2026-08-23 05:01:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b5695e6-dc3e-3833-896f-98cab63a49e3 | -1.43194 | -54.19107 | 2026-08-23 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 060cdf9b-4449-3e83-854c-53bc8f144b6f | -2.55894 | -47.24702 | 2026-08-23 05:01:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8d8d94d8-7be3-3517-b7ae-7795a0af3957 | -4.17121 | -42.4472 | 2026-08-23 05:01:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a78df506-a31d-33c2-b417-571ccc5c4b7e | -4.17311 | -42.44555 | 2026-08-23 05:01:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 71d27d1c-8890-3a75-b63f-ed7c8515494a | -6.78814 | -59.41874 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac6840a1-33a4-380e-8f33-f4f916d1bc21 | -6.87009 | -60.01325 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cdf76cd-fdaf-3ee0-a11c-b3787070424e | -6.86609 | -59.02824 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 996268da-5d29-3a63-8916-2db6f000868e | -7.48888 | -55.33137 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6038e83e-5266-36ef-85a6-7884ba338d3b | -6.79839 | -59.43113 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47b1ab45-be07-31f6-b137-cb998caabc6a | -10.31018 | -48.21874 | 2026-08-23 05:04:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d56bf79-6a4b-3c84-9d95-55911cf6aa1e | -6.79835 | -62.91022 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1decea94-2a39-3519-a990-e88f4afda1f2 | -6.96666 | -59.05294 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71136b28-c7da-3bf8-b698-dff69747cb9b | -6.79949 | -59.67235 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README40.md)
