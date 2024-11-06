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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 774cda18-ad56-33a5-9aed-881de16aacc8 | -4.03697 | -48.29592 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 821b7b27-575c-3bc8-b87b-908b1d799d92 | -1.47799 | -47.21752 | 2024-11-06 04:36:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eedb4269-1234-37ec-9d50-f2a1018f65e1 | -4.1315 | -46.90659 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa9470a1-9470-31bb-8d05-75e4b861d75c | -2.37931 | -50.40762 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a55537b-16fb-3ba0-aba6-14e7bebf294f | -3.61894 | -51.34237 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d17cdb78-417a-31ff-9da2-da84542a1f67 | -3.3353 | -51.61936 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c12c89bb-6069-3491-a3f3-cd495f93c687 | -3.82087 | -46.46508 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73db6b9a-8ad5-31d8-b2d5-eabb77d9ee2a | -2.83578 | -48.46133 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09c05535-f6d6-3f16-8ef4-70a21e694517 | -3.22721 | -53.39906 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d81b663c-0a7f-35e6-9dfa-4425aec6ce2e | -2.91547 | -51.05057 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7d81e232-2735-3d6f-9517-fa12a91738ec | -5.37388 | -46.43242 | 2024-11-06 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75ab5720-af57-3110-a4bf-40f73764230c | -2.38554 | -46.75407 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 818191df-5a06-319b-a764-5f49d8095c7f | -2.88786 | -49.27252 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 610991b0-51c2-3012-9efa-89c6fea6e8a7 | -3.48055 | -50.38381 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84100830-e454-3b5e-8b28-1d1233b2ced1 | -2.91596 | -48.59686 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2deb3d64-8a30-3b5d-abbc-d78031906062 | -3.03687 | -53.28251 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23452676-4632-345f-8cbd-bffbdeecfd6e | -2.8859 | -53.97107 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91325217-532a-3f6e-9a6d-66e54af22c4f | -3.03739 | -53.27948 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0374ac27-2b5a-33ed-a28a-d4625ab6a402 | -3.55598 | -47.39051 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bbe6e7f-ca7c-3c64-8f8c-7c1af6258fab | -3.9597 | -48.15984 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 32db1e5f-1637-3212-876e-2bdf49ea2789 | -2.83908 | -48.46184 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06deb2e2-91f0-393b-ac14-0122c01b771b | -3.04293 | -53.27024 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9623029-6600-31ad-849b-4fc8b84672d1 | -2.4144 | -48.86994 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e655b89b-5725-3ebf-bc97-6ff65f650db9 | -2.85481 | -51.7786 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 8c8a0be7-b5a3-3b40-aa09-04d903a1795f | -3.52416 | -44.72218 | 2024-11-06 04:36:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b919a080-d046-306f-bdc6-fd5285f98487 | -3.76027 | -51.65811 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bef9abad-dab4-37d1-b058-78079c38437f | -2.99389 | -53.84384 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f888b8a6-2c0c-36d5-ac83-5ba06ef4465f | -5.71304 | -43.81524 | 2024-11-06 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a460b8ee-7f7d-3fb1-85d3-c7894030612d | -2.97817 | -50.29829 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 988c8709-124b-3b67-bb31-b4d05b37d74a | -2.5244 | -51.16514 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6de9ab43-3e34-3e1a-9392-62c31f8daed3 | -2.81033 | -51.3458 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60892ae7-cf56-34e2-b3c8-19709c6d4052 | -3.41797 | -50.38507 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 303d41c7-7cbd-3a90-b6b9-f6bfcdeb6a85 | -2.82912 | -48.45697 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 215ad141-d2f4-3a71-9dff-b49b28d3e7ce | -1.3321 | -47.32429 | 2024-11-06 04:36:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cecbe0c-38de-31b6-8547-aab7bf97d41c | -3.21465 | -53.10436 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3ae6fd58-3b34-3d8d-86d4-f19af242d89c | -2.80973 | -46.64007 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90a38659-5baa-3955-bd08-d99fe607c94e | -3.38625 | -50.35779 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5852d85-c172-3a3e-a140-6cc087cccf88 | -4.12544 | -43.58757 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 6e95e6b2-0b17-394a-a6b8-04331927cd02 | -2.84609 | -49.38663 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73022fd6-76bd-39fc-a697-6402f8e0419a | -4.10635 | -50.75253 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d081c06-1336-342c-b2a9-551d25f7d46e | -4.82389 | -48.56452 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 581267c0-9692-3063-98e1-70e04adbc20b | 0.18341 | -51.06146 | 2024-11-06 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad566080-5bcd-3f6f-b513-7de871c861aa | -2.97421 | -53.2727 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 25553e9a-a009-3332-8e46-39ac24a7488e | -2.80681 | -52.94177 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cb1acff-1709-353d-b052-db13130c6cf4 | -5.00299 | -47.80232 | 2024-11-06 04:36:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e41f12c5-b43a-3a7f-a1ae-4cd04b30b5bb | -2.8444 | -52.9039 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4456fe60-2884-3620-b989-59a191931a5f | -3.66349 | -50.23147 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 35af99fa-6a78-3f4b-89c9-265e16dc2f74 | -3.23115 | -53.39966 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 15a4fa8c-1948-3689-be07-3514ef404578 | -3.66742 | -50.22842 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| de3eb477-d2fd-3ecc-ab25-4429e8f30dce | -1.53693 | -52.01413 | 2024-11-06 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9828e55-a419-3032-bbbe-a3750b60cd36 | -2.60624 | -51.76704 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfb2fc7a-aec4-34a1-9f77-a03bddc99df0 | -3.36785 | -51.57529 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2316503f-9b6b-37c5-bb2f-0c06115a55c0 | -3.43353 | -51.61717 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3c3fc11-6ac0-354a-a5d0-fb64e42afc2f | -2.28422 | -50.67445 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05fd2571-4096-323b-9f55-f661fe2e4473 | -2.78719 | -52.87743 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 227376db-08f9-31b6-af1e-fc2647a50f57 | -2.89965 | -51.46928 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7acfd935-8b2c-31cf-b73b-6c5503eb7f8d | -3.22089 | -50.21397 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddead724-980b-3e83-80da-64657f4e07e1 | -2.49271 | -49.90704 | 2024-11-06 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4f2824b-d363-3791-ac50-34d12be201d5 | 1.20422 | -50.7641 | 2024-11-06 04:36:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe059c2c-26db-3cc4-9f62-5e96ba44325d | -3.15461 | -50.20706 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 46904434-4a09-338d-95b3-6ec260765d9e | -2.83245 | -49.5377 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 315acd0b-8a78-3fc6-82ef-7866ed049902 | -3.18548 | -50.58783 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2516ad8d-5923-30e6-9bc4-f70978aac711 | -3.89476 | -50.25323 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11b1c75f-764c-389f-b3ff-7af68cddc7a5 | -5.35506 | -46.85807 | 2024-11-06 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f84a67f-68c2-37a8-97de-f1fe59ba57dc | -2.92017 | -48.95982 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fcaa6a4d-af79-3d25-834d-94aa9d660afc | -3.45293 | -50.38317 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df7b8352-bdfd-36b2-9115-296585f71c76 | -4.08375 | -51.04547 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1bd1950-fdcd-356a-b45d-59718cc7a577 | -5.1724 | -44.31036 | 2024-11-06 04:36:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75d7b53d-5a72-323f-b284-6f9091da0499 | -2.79881 | -51.48614 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6c773d3-dba7-3ccd-a8dd-288cb60bf638 | -3.17982 | -49.74607 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4491adcc-c4a3-39ba-9dd1-7f9b51fc462f | -3.96079 | -48.15292 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28028605-c349-3468-a04d-9af639c4a66a | -4.09981 | -44.272 | 2024-11-06 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81ba1184-d9ee-326e-acbb-26977faa87d0 | -3.05351 | -51.06705 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e0de8237-60ab-399d-9026-9c33b53f4622 | -2.05626 | -52.66527 | 2024-11-06 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b3483cb-541d-3d42-bc5e-625807195ff5 | -2.81348 | -48.5565 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ef25a89-4187-303d-a5cf-09a82bbe3221 | -3.24295 | -53.4015 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 232b9fc0-1dbe-3fd6-92c8-b704a6e735de | -3.48393 | -50.38435 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eae5184b-5646-39e0-9393-6e66289835aa | -3.66628 | -50.23555 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2b8c29fd-bf5b-3875-8712-e2d80cc6da84 | -3.96907 | -48.14352 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5a23f74-b6af-3870-8357-52c25082d7c8 | -4.58171 | -48.07003 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 59e4d92d-4623-34aa-b9c3-0427da6230af | -3.34372 | -50.25509 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f4fba7d-09dd-3c63-b720-3560a78a7ede | -5.55784 | -43.70395 | 2024-11-06 04:36:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 455d0251-979f-34e8-a02b-cb98eba1b6ce | -2.33734 | -49.12255 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 969192f8-7461-30a3-9525-8cb6be9f678c | -2.85731 | -49.48805 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17c1a151-112d-3cba-816c-875963a721e2 | -3.52004 | -51.66802 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 776b7c6f-07de-3e2c-a185-a7d32fd4f5e6 | -2.93281 | -52.54329 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c7df81b-5d06-3854-a777-950a02c5e0b0 | -3.30915 | -50.0923 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94988a80-dcfa-3a26-993e-e3ab0b2cb73b | -3.44732 | -50.37489 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5739b467-c20a-3337-95de-12492ac3b5ba | -1.55394 | -52.26825 | 2024-11-06 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db767148-9aee-366d-9117-d3e97c3eb9c3 | -2.97946 | -50.29855 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfbe4996-9e3b-31ba-891e-d377ad59af42 | -3.69193 | -49.81966 | 2024-11-06 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3feed174-5ea5-3c60-8db6-3da51af97bfa | -2.91956 | -51.04728 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 10a28a41-89ed-363e-bda3-b38069a4f26a | -3.47436 | -50.37912 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24a77e2b-43aa-307e-ae0f-41a4923dc5aa | -2.66607 | -48.50185 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da02122b-ecf8-325f-823d-a9d9f4899065 | -2.60391 | -51.30194 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e06d180a-7600-36fc-8e0a-473d6d66f11b | -5.06344 | -44.23457 | 2024-11-06 04:36:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 73740f36-9907-3e04-b68d-68b84feb0a9c | -2.77509 | -51.95468 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d163f074-b17a-3336-be09-708a83b44159 | -4.24174 | -48.02861 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfcf4987-9e2a-37c7-b029-d3913257a690 | -3.10163 | -45.94107 | 2024-11-06 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 426e70b7-367c-3793-9398-a86775f0073a | -3.19518 | -48.65848 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README35.md)
