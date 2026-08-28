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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e54a41a-0c3f-3644-9a89-0b66a3aa1a5f | -11.21425 | -53.98878 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 82ad66b1-d00c-3d0a-b6dd-423a1d923f6e | -13.63788 | -51.70501 | 2026-08-28 17:45:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1f29fb6d-da42-397f-920a-42a64b06d18b | -9.85348 | -65.00766 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e110f907-965a-382f-bd7f-a005f9bc527f | -10.76329 | -53.97753 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5994101a-2c6c-3ae7-958e-dbc2880c98cc | -9.96791 | -53.93241 | 2026-08-28 17:45:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 476536c5-cd24-396f-ac79-a1c64db0ab09 | -11.48137 | -60.50701 | 2026-08-28 17:45:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 303ed2dc-2e0a-36c9-93d2-00893a111d3b | -9.01081 | -57.54334 | 2026-08-28 17:45:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 583dc4b0-2b24-3aac-ab16-a775ccf3d1d2 | -11.00827 | -49.6516 | 2026-08-28 17:45:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 9c52bdd7-f481-310c-8c07-d9c9d5f9ed8e | -14.18517 | -52.82347 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 31063915-f796-31a2-b84f-b7b10d1626b9 | -9.20366 | -61.1105 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 894d2b80-1e4c-309f-993e-aef8e8666254 | -10.50241 | -64.5162 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 19.7 |
| cc791d1a-2a79-3035-a03a-1c2acc15d7e9 | -14.56797 | -52.0297 | 2026-08-28 17:45:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c291f8f6-d6d9-3fcf-9713-575c818f4f5b | -14.88161 | -52.63514 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| ba36f0b1-0b2b-34d3-9fd0-f93ac8f01605 | -9.16639 | -59.57802 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 699017a7-f54c-3ee8-8603-be3b937f1424 | -14.19107 | -52.85434 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2338f074-a330-340e-9373-e1dc7520d05e | -11.19617 | -55.10109 | 2026-08-28 17:45:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 389c24a8-9019-3963-b5ee-da272e86ab21 | -10.47048 | -64.49009 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 21.9 |
| e3f73c7c-0b0d-32b9-ae56-6ded79e4022e | -10.83678 | -50.50579 | 2026-08-28 17:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9984685c-e94b-38ff-88d3-65bf29dc904c | -13.88696 | -53.23861 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 90dfb98f-3507-367d-9dc4-5442684695d6 | -14.64569 | -57.002 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f042bf48-898d-3f68-9152-f90f0b19e3dd | -8.59217 | -54.76332 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 8a0c52b7-8036-35ec-aec8-e0bb848a07c5 | -11.7149 | -54.53871 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 98ef66e7-1120-327b-b273-0c4721451649 | -10.07246 | -48.6828 | 2026-08-28 17:45:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 91742c6d-707d-3f72-abf0-bcea15e2b72f | -8.59167 | -54.70435 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e3e8082f-60e2-3936-bc0b-79d187ba8aa0 | -11.61011 | -50.19763 | 2026-08-28 17:45:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 6ea885a3-fc65-3901-9928-0eddabdd31c2 | -10.42391 | -62.99507 | 2026-08-28 17:45:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28fa869d-ddcf-3ffb-89a0-80672c5cb38a | -9.61634 | -55.11439 | 2026-08-28 17:45:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5c84ea94-a503-3b95-8b3a-96cc67fdc01e | -8.24665 | -54.99548 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| df178912-9f31-3775-b9a4-f0a3260cea5a | -9.1102 | -60.31385 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 34e3df14-8e1c-3dd9-bd87-13d89477e946 | -8.54444 | -51.50409 | 2026-08-28 17:45:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c3101515-511d-3db1-b41b-bb84aba09bb7 | -10.58231 | -63.5504 | 2026-08-28 17:45:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 37ed2925-a629-3da8-a839-58044af8b430 | -10.47623 | -64.48151 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 6fc4f4fd-e690-307a-bb5c-3a1964de81aa | -10.76452 | -50.64031 | 2026-08-28 17:45:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e93d412f-4539-3b87-9e7e-e78a9f27c9c5 | -11.27242 | -54.02584 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| b54dc149-c6d2-3967-b302-a28861f20785 | -9.93797 | -60.43489 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f1e92ca1-fa41-323c-8ac0-28a62d18836b | -10.25001 | -55.877 | 2026-08-28 17:45:00 | NOAA-20 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 16016373-c67a-3889-81fb-255962887127 | -11.27166 | -54.01805 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 26b717ca-d72f-3a33-82fe-419df68f2804 | -9.86386 | -60.26139 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d9b90105-037e-3bc3-9eca-f40339df31f0 | -14.86286 | -52.62041 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 88b0c0bb-3260-3556-b71f-54b5e0351eee | -8.77719 | -50.07015 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| bdef617d-1dae-3572-a0cf-f71202552ada | -12.89639 | -59.90571 | 2026-08-28 17:45:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8d9f3593-59cf-3e88-b481-0e5bddf6c91a | -12.91329 | -59.87941 | 2026-08-28 17:45:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 5df12241-20d8-393d-a4f5-6537bfbf22db | -11.19263 | -55.08157 | 2026-08-28 17:45:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a38680c1-045d-3d92-867d-c1f615621492 | -8.59772 | -54.83052 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| be34d6af-d845-3b3c-9482-ef182ff09774 | -14.88103 | -52.63215 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6f87e3be-43fc-347a-8727-6752c70c8a33 | -15.56545 | -56.29082 | 2026-08-28 17:45:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5a56bff2-2a3f-3149-a1e5-f15344439a6f | -13.63715 | -51.70126 | 2026-08-28 17:45:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6065578c-3f94-3f92-a18e-92305f1f8e1c | -12.33459 | -63.73383 | 2026-08-28 17:45:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1127a4ed-d746-32d4-b26a-18d285fbf1d2 | -9.20705 | -61.10997 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 06b97e07-348e-3b66-8fc8-e387a6af6ab1 | -10.26585 | -64.50115 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| aa231694-be3d-375c-9a8d-593d851474f6 | -10.31106 | -68.45226 | 2026-08-28 17:45:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d1293b0-48ae-3a7c-8f04-1a13fb5f73b8 | -14.92484 | -52.59831 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6762a046-5128-35f0-abef-780d705d202a | -13.10198 | -50.04452 | 2026-08-28 17:45:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5f7bf34f-9416-3c89-9d23-c4ffdbcdd54b | -10.75826 | -53.97837 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 6b9b5851-4994-3efa-bdfd-13b06bb8098e | -8.78156 | -50.05708 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 153141e0-24be-39b3-885a-5fa9aae1c9af | -9.94203 | -60.43814 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 473723cd-5839-366c-8e02-dbbc077f4720 | -11.27346 | -54.03159 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 0d97898b-3e35-3eae-8738-ba68a49f73bf | -14.18123 | -52.83051 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5fc90267-f392-345a-ae1c-c7206772b736 | -14.43943 | -52.59314 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 87973419-b18d-37e2-8af2-747357063360 | -9.91259 | -60.43118 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e95b2e53-91b3-3daa-8846-179d9b7a9244 | -13.43374 | -51.76748 | 2026-08-28 17:45:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| c2bfda60-e289-3595-8455-be74f8c3bcd7 | -9.1523 | -49.97195 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 2a74538f-4c45-3b79-a9d6-93626e38c702 | -14.44126 | -52.60255 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4f31b03e-2d87-32a3-a762-144d96b97a5c | -14.19555 | -52.85018 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5ddb3628-d260-313c-9ee8-3b2c75cded9a | -11.61369 | -50.19931 | 2026-08-28 17:45:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 397db49d-bb8b-387f-979e-2da22de2d29d | -9.88187 | -60.2625 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3b02a8fa-061d-39a2-85e0-1937101890d8 | -14.89833 | -56.3262 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1fd9596a-c16a-35fe-b5f8-e6f22aa1de11 | -14.88672 | -52.63427 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b8e1c815-b980-37e7-8f09-d8fd8e87039a | -8.59869 | -54.83611 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 45e51ba6-6703-3188-a110-0101786021b9 | -14.24343 | -51.76861 | 2026-08-28 17:45:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c3a19c10-12bd-33ad-85af-034a0ca7adfd | -14.92655 | -52.60689 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 91abe115-6983-3ff2-bdc4-6be0f4910160 | -13.46171 | -57.04757 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8ac994bd-77df-354e-bfff-f0f2ec11de47 | -14.89633 | -52.60197 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eff567ce-0a98-3694-b3c8-50e54d37a39c | -10.77217 | -50.6246 | 2026-08-28 17:45:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 42d41d98-89dd-3a4d-ab75-0c75210a92a2 | -14.16654 | -52.83652 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b233a8a8-458d-3986-8ea4-ca7617bf434d | -13.47828 | -57.04984 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 36908dbe-e447-3b17-ba19-8cf9c82eea89 | -14.43843 | -53.38742 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 2033b36e-2582-3797-8ee9-2bce6c5aba82 | -14.63495 | -57.00905 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 65505b0b-7b10-3a6d-9c2e-7bde163e43bf | -8.58089 | -54.8215 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| f8a2b2ef-21f4-3bf7-8646-b5da1178b197 | -10.40234 | -61.19948 | 2026-08-28 17:45:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c38ac83e-41c0-3ae6-87dc-60da9353ed3a | -8.95084 | -50.7931 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4078f977-4ab4-31d6-8001-753be89efbcf | -10.50675 | -59.62371 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 346240ac-129b-3408-8ce2-d0325cda5caa | -9.97178 | -53.93843 | 2026-08-28 17:45:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| f999ae4e-9525-3528-842f-f7b71b88eb53 | -12.14227 | -50.6288 | 2026-08-28 17:45:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 694957f4-8c57-3a29-8912-eb224b7c6b6b | -8.60413 | -54.77292 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 34755afa-9e40-365e-b729-f6e3af82bc14 | -9.41934 | -50.44706 | 2026-08-28 17:45:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| d442813a-841a-3ff8-b1f6-078e7d0a9252 | -9.84652 | -65.00868 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 472fcc1d-2902-36ec-a86d-deb9764b5743 | -13.55526 | -52.61885 | 2026-08-28 17:45:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2b81ffeb-2bb7-35ed-9015-ac2ec5337cbb | -10.16941 | -68.61779 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c37a52ad-d458-39d2-849b-63f976b267bb | -10.39898 | -61.2 | 2026-08-28 17:45:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 18d72413-f808-31f0-aa3b-dda5deaf3494 | -10.49051 | -64.48322 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa12f75a-5d94-3e1c-9abf-a2ba53a457cd | -8.11771 | -51.65516 | 2026-08-28 17:45:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8ec73980-315e-3e74-847f-ddf995fa01a4 | -8.81989 | -49.62745 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e3c07760-c46b-38d2-a751-1ff8793d03dc | -9.43128 | -51.69973 | 2026-08-28 17:45:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 5fa7d834-088f-3dc6-9c69-d5ddc9bae29c | -12.38594 | -48.20087 | 2026-08-28 17:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 42a53798-cd8b-310e-9a1a-2f34beec1d9f | -11.19762 | -51.26303 | 2026-08-28 17:45:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6c14201f-87ce-3675-bcaa-fd2e6d1a57bb | -11.62421 | -54.58134 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 43d2fcab-c6fc-3476-822c-ef270e9b7452 | -14.19439 | -52.8441 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 115ae5a8-9e98-3c05-afd7-32ac8baab748 | -10.23973 | -69.31323 | 2026-08-28 17:45:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c59461c6-95d6-3806-971e-1984c80d6d6f | -14.15635 | -52.83847 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README141.md)
