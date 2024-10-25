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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5da30fbe-8ae6-37bf-8b70-4846c0bd93ff | -9.24944 | -48.32178 | 2024-10-25 05:04:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f854795c-b97f-345c-95e9-2341d5e7a0c1 | -9.24528 | -48.32298 | 2024-10-25 05:04:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9e40fa6-7c97-3049-b706-72bcb80df7b9 | -9.24455 | -48.32862 | 2024-10-25 05:04:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2857670b-4bd9-35bc-89b6-41f3350c0993 | -9.24447 | -48.32111 | 2024-10-25 05:04:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 059168ef-34fa-3040-b51f-9c4ed841c776 | -9.2437 | -48.32673 | 2024-10-25 05:04:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a65e6fec-d110-36ad-b4b0-2928430c7b08 | -9.24293 | -48.33237 | 2024-10-25 05:04:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51fc338e-90e9-3cab-b073-9d5b6af375c1 | -9.0335 | -48.71745 | 2024-10-25 05:04:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01a6c3e8-2a74-3adf-ae57-57c61c40394d | -8.91021 | -48.54108 | 2024-10-25 05:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 67eff08f-adab-337f-a184-dc19654c7ac9 | -8.90751 | -48.53912 | 2024-10-25 05:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e08c371d-409c-3bbf-9f2a-ec1a3118e962 | -8.90674 | -48.54456 | 2024-10-25 05:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 94053020-01af-3b0d-987a-cbe5e8a8ade4 | -8.90611 | -48.53457 | 2024-10-25 05:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d544dd1a-7d78-3b3c-b190-5723b035921f | -8.90537 | -48.54017 | 2024-10-25 05:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c3903e96-e8c0-32ce-996c-9870f6e56fd5 | -8.90465 | -48.54565 | 2024-10-25 05:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dcf63629-3e22-3cca-9f9b-9262d79bffb7 | -8.90266 | -48.53827 | 2024-10-25 05:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| da3c0890-0749-3fa3-85f7-fc620244ba73 | -8.902 | -48.5281 | 2024-10-25 05:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58187a77-2c4f-3f04-95a3-6b9023615374 | -9.63182 | -47.71965 | 2024-10-25 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c58be137-9746-330a-8251-270d015c6fdb | -9.62661 | -47.71901 | 2024-10-25 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce2be360-efa7-3cb1-b8a7-0f725dae2356 | -9.55531 | -47.72792 | 2024-10-25 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b86b217-9afb-33d8-ad49-139af7d02ca0 | -9.55488 | -47.73109 | 2024-10-25 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4eb3a989-3508-3b15-8bd9-7559bda63ec3 | -10.68773 | -49.1093 | 2024-10-25 05:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b130cf8b-6d77-3b72-832e-9d30302729f9 | -10.4735 | -48.2837 | 2024-10-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82b1f011-8aaf-3dc0-b943-75f41e969e07 | -10.47311 | -48.28672 | 2024-10-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b48c039b-34b3-3d42-b490-5287a2622426 | -10.46842 | -48.28313 | 2024-10-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1e7311e-027e-3e70-ae44-7d0054744c70 | -10.46803 | -48.28614 | 2024-10-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88958540-1f0e-3e4f-8bba-577526489315 | -10.46764 | -48.28915 | 2024-10-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81dd5692-9b32-387b-9536-f7d8a542c31c | -10.1092 | -48.19059 | 2024-10-25 05:04:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1781404d-668d-385d-bd9d-b05465b507a5 | -10.10881 | -48.19356 | 2024-10-25 05:04:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28d91c41-32e1-3712-ac51-e277845734ff | -10.01155 | -48.23648 | 2024-10-25 05:04:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6cd73b3-85ac-3691-9698-84834ac23b0d | -10.90549 | -47.83139 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6ac2e5d-7fe9-352a-9016-379fa09dd680 | -10.90021 | -47.83088 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87d06c69-f177-38e1-834b-45f4ac055406 | -10.89573 | -47.8242 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46812ec7-bcf9-3102-add9-992cc905c6c4 | -10.89531 | -47.82741 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 334b7e81-0a93-3016-96be-fd7a080d7f8a | -10.70984 | -47.94233 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27fcc74d-0568-3660-af48-ed617439d9ac | -10.70941 | -47.94575 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bb2d06a-c481-36e3-a1e4-f883a2e26d5a | -10.65232 | -47.93032 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46575182-8c17-3471-87d7-ba8660cd4d0f | -10.65192 | -47.9334 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e534e0c8-97e7-3dbf-889b-77c531b2a775 | -10.6483 | -47.92038 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fe7d626c-118a-3973-8499-da959f6207a7 | -10.64792 | -47.92334 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 81691d72-7bd5-313f-b578-b63ea9636f63 | -10.64756 | -47.92618 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 493c5bdd-39a3-31c6-8255-ce6e47f55187 | -10.64279 | -47.92206 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 77ae79bd-a2c5-3bdd-b471-6496c5876f4d | -10.64242 | -47.92496 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 483d1726-2612-3281-a3f7-8a3656cc0e89 | -10.44476 | -48.08307 | 2024-10-25 05:04:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f8e1c73b-b2fd-3bde-90bb-1ff8ae055cb0 | -10.43962 | -48.08243 | 2024-10-25 05:04:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7ccf55eb-4ad7-330f-b213-273e396afa85 | -10.43921 | -48.08554 | 2024-10-25 05:04:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b84a52b6-4204-39f2-ade4-1aa4000886aa | -10.43881 | -48.08858 | 2024-10-25 05:04:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8353ba0-4cf7-338c-9386-24ead1bf1050 | -10.42244 | -47.5209 | 2024-10-25 05:04:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03618abe-fde7-3928-8fb0-a9dd2f8c1e7b | -10.41711 | -47.52017 | 2024-10-25 05:04:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b345f5dc-c92c-3cf7-ba04-2082a263941f | -10.17827 | -47.90919 | 2024-10-25 05:04:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7f1b735-440c-38fd-8302-2f3f5e4f2207 | -10.17783 | -47.91241 | 2024-10-25 05:04:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60359cd8-94e2-3eb9-b413-4462ff5f5281 | -10.17481 | -47.90841 | 2024-10-25 05:04:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9b3b846-f917-3015-b314-646aed2d5186 | -10.1744 | -47.91164 | 2024-10-25 05:04:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1ca7205-8b2e-3e99-bc71-ee766e980a92 | -10.17309 | -47.90849 | 2024-10-25 05:04:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3bf80111-ccfb-3e20-a4e4-df3332ddbaf9 | -10.17266 | -47.91171 | 2024-10-25 05:04:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e88fe8e9-1ee5-3b36-9d00-401f85eeb74b | -10.05334 | -48.06271 | 2024-10-25 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b7a9ef6-8ceb-397d-a7b9-265acaa18816 | -10.05076 | -48.06152 | 2024-10-25 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08a061d1-1d94-3a72-8cfe-c0583cf67ab9 | -10.05034 | -48.06464 | 2024-10-25 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ecd42406-f30f-3ffd-b6ba-f455a627865b | -9.93792 | -48.87827 | 2024-10-25 05:04:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d1e6ad2-a640-3ea9-96bc-5e6d080bbfaa | -9.93435 | -48.87619 | 2024-10-25 05:04:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7541636f-f258-3597-9dee-3f038af2bc70 | -9.9331 | -48.87756 | 2024-10-25 05:04:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c0aab35-3cb0-345b-b360-f3e92374a54e | -9.84855 | -48.57263 | 2024-10-25 05:04:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad2f5d8a-698a-3a3b-862d-060f24fd1350 | -11.72612 | -48.35883 | 2024-10-25 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d48162a-2bb0-3522-a90c-4a2f80af47ea | -11.72575 | -48.36189 | 2024-10-25 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a539ddac-4dcd-30ad-8c8e-296e9686d8d0 | -11.6313 | -48.47167 | 2024-10-25 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de5f4884-e824-38eb-b773-f884cd756671 | -11.63091 | -48.47471 | 2024-10-25 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc505f8a-4a88-354f-9ee5-bfd885f3d792 | -11.6303 | -48.39705 | 2024-10-25 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a68dd9e2-4015-3460-a022-1b0cba8bb838 | -11.62595 | -48.3903 | 2024-10-25 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8687c7d9-99e2-333e-8955-e2d7f7a8db60 | -11.62557 | -48.39334 | 2024-10-25 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f9da2c3-4d4a-3764-a4c7-3ecb1fc8e39a | -11.62519 | -48.39638 | 2024-10-25 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d5c3fe0-790f-3960-87dd-e0fe3b0620dc | -11.62083 | -48.38961 | 2024-10-25 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32f443d7-7a6d-3d60-b03b-91190f2ce0d7 | -11.62046 | -48.39265 | 2024-10-25 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c3423f9-3b2c-375b-a7dd-e029ec566e98 | -11.6161 | -48.38587 | 2024-10-25 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f7767cda-ea17-3dd2-bcff-2436fd36ff1b | -11.60028 | -48.59527 | 2024-10-25 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 788b2346-c059-3fcc-a659-316530dbe94c | -11.59991 | -48.59821 | 2024-10-25 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4519af8d-ed9d-3193-aacd-2b597082de60 | -11.59524 | -48.59459 | 2024-10-25 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99e98cfd-e86d-3cc5-a924-4e0641b8931c | -11.59498 | -48.55558 | 2024-10-25 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ea7f19c0-4107-3c72-837d-84ffbacb9b68 | -11.59487 | -48.59753 | 2024-10-25 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d73396a-3e04-32ab-9ef7-c1fa90b82d94 | -11.5942 | -48.47894 | 2024-10-25 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7916c678-bdcd-3daf-8acd-bc774aa2b6d4 | -11.59382 | -48.48197 | 2024-10-25 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2131bedf-89ff-3f7f-a034-dc59e0667ec3 | -11.59034 | -48.47997 | 2024-10-25 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61a9ee07-0241-3b2c-9af9-4498af50d984 | -11.30384 | -48.48248 | 2024-10-25 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f53474fe-ab86-3f3e-9531-52dd5c904ff3 | -11.30346 | -48.48553 | 2024-10-25 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1934d473-e468-3c9e-b08e-f5bd96243c8e | -11.2996 | -48.63592 | 2024-10-25 05:04:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dffa1d3a-6e1d-3fc6-a1e9-eeccad7ec66e | -11.29917 | -48.47873 | 2024-10-25 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8696ced-5aef-3751-81b5-720f3ac1333a | -11.29878 | -48.48185 | 2024-10-25 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa520ba0-32ac-31cb-bb00-5e193289cc68 | -11.29757 | -48.49142 | 2024-10-25 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a932bc47-1377-3ee2-a6cc-3c8e24912569 | -11.29716 | -48.49466 | 2024-10-25 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f4d21944-c7d5-3fc6-bf7f-c4b84bd7a4d8 | -11.29496 | -48.6324 | 2024-10-25 05:04:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6f2dbe4-c57d-336c-b6a2-cb9d86ba8a52 | -11.29454 | -48.63566 | 2024-10-25 05:04:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 101edda3-5c5a-380b-97a0-9b9ed300e006 | -11.29331 | -48.48441 | 2024-10-25 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08ec2721-22e7-3125-b752-ff54db55c220 | -11.2921 | -48.49395 | 2024-10-25 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1050073b-bcc6-38dd-9f0e-e2ffed6288d7 | -11.2917 | -48.49711 | 2024-10-25 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 790c2410-c6c2-3640-9d9c-b24000ceeb82 | -11.28746 | -48.49003 | 2024-10-25 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0471189c-bf16-345c-9ab2-e352ca0d6949 | -11.28708 | -48.49303 | 2024-10-25 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 836adc10-ae0b-3670-a559-20cfbe16847b | -11.28283 | -48.48589 | 2024-10-25 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77583aa8-645d-38f1-9284-5a63265e84ba | -11.01997 | -48.27468 | 2024-10-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5aabf874-4a69-31eb-9311-0af7980f49ae | -11.01958 | -48.27776 | 2024-10-25 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18922451-94e8-38c2-b0ea-09fddfcd7eda | -11.16971 | -47.76531 | 2024-10-25 05:04:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c7b1c16-807c-3607-a539-20d3759cd5d8 | -11.16936 | -47.76814 | 2024-10-25 05:04:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73d8b3d7-49e4-3f6a-8630-da0238553389 | -11.07872 | -47.89687 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40306664-9d57-3f29-9cbf-d4223994cb57 | -11.07833 | -47.89995 | 2024-10-25 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README97.md)
