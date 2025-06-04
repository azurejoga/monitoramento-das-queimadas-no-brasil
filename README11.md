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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06ee12cb-e0ac-3d56-8356-bb67bf00ebd0 | -11.90767 | -47.44678 | 2025-06-04 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c92885a5-d00c-3f24-9bdb-b8a80cc04a81 | -7.88958 | -46.19204 | 2025-06-04 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 430a32f3-ea8b-3802-83c5-835e96df561d | -10.69614 | -57.64627 | 2025-06-04 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 39a4975c-92eb-3c80-a0fe-6cc0394e2488 | -8.19534 | -49.80038 | 2025-06-04 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6291f64a-f5f2-3a32-8de1-ce306d95b192 | -10.68411 | -57.64889 | 2025-06-04 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adf5af91-46fe-3617-9854-d5f72ff03214 | -6.86302 | -47.84563 | 2025-06-04 04:51:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c3902c9-4967-325f-a84d-d8ebeb006fca | -8.2248 | -45.70374 | 2025-06-04 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a89fb90-cf57-3db2-8ea1-900d2fa29495 | -8.19621 | -49.80281 | 2025-06-04 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0eb47220-273e-342d-977e-762c3f062d1a | -8.07085 | -43.11315 | 2025-06-04 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| c68e707d-fc0f-3f78-8bd4-0f3a81aa98aa | -4.13095 | -54.89978 | 2025-06-04 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e90cefe-4e1d-34c5-9dcc-86e3af3b2440 | -10.05506 | -44.64692 | 2025-06-04 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aaae9edc-da42-3a3e-80fb-23a1f69967ef | -9.56807 | -50.51717 | 2025-06-04 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6371bb52-786c-3d70-894e-70db2275bcfc | -8.75726 | -49.7744 | 2025-06-04 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 19952989-5330-3f35-a9d2-2b63346e698b | -7.22601 | -43.12542 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f6097255-22e6-301f-a601-08ccfdcd60bb | -7.01407 | -44.58574 | 2025-06-04 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8625d7b3-29c0-3c37-b2bb-dd05d9b61846 | -10.14577 | -52.13967 | 2025-06-04 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 002f47a3-fe22-3ec6-aaf0-f22f4310f487 | -7.89416 | -46.19243 | 2025-06-04 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c0e0b7c-801e-3865-8e4f-c7e0668626d7 | -8.5143 | -46.3502 | 2025-06-04 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c416ceeb-1e8c-3073-bf89-7fed0b5df91e | -9.31507 | -49.49292 | 2025-06-04 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af2e2372-f9d7-3ef9-a524-f848e10f9054 | -8.55591 | -44.55979 | 2025-06-04 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f176b7be-13d1-3db4-9aa0-4f0d1a00e84a | -7.69098 | -44.57097 | 2025-06-04 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b6c177b7-3a13-3243-ab96-cfc87cb48436 | -11.56145 | -47.62422 | 2025-06-04 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5360d24c-7365-359a-84fd-0fae6b12d71b | -7.01941 | -44.58408 | 2025-06-04 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bc77aef9-5b49-3e46-889c-bcab7556feb1 | -8.89867 | -44.78016 | 2025-06-04 04:51:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9276b938-5276-3942-b860-f21018db46e4 | -7.21901 | -43.13563 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b11a0f45-a219-373f-a56f-9c64b02cb3ac | -8.91282 | -48.90507 | 2025-06-04 04:51:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d057f24d-3667-3332-b7f1-5e7482a18609 | -9.25284 | -56.31649 | 2025-06-04 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da088c81-b4bc-3c42-a1fd-2469ec662ddc | -6.37449 | -43.6833 | 2025-06-04 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2ea7b25-9cf6-3947-9540-0f2e151f68d4 | -10.56585 | -48.51509 | 2025-06-04 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 649075e3-619e-3802-8965-bb4d514e57fa | -7.08408 | -49.60006 | 2025-06-04 04:51:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c6d6115-427b-3853-b9dc-6d971add1922 | -7.88726 | -55.36498 | 2025-06-04 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07e29cca-cef9-36eb-9e04-b0f19e351a4a | -7.68552 | -44.57317 | 2025-06-04 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2716bb9-1358-3251-abdf-4721486ef392 | -11.14284 | -53.94346 | 2025-06-04 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b9f162fe-3955-3489-b14f-e26950bb170d | -7.23203 | -43.1226 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f62986c4-ba42-389e-847b-3154c87469c6 | -7.01822 | -44.59281 | 2025-06-04 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c9ebda58-252b-38af-8cb5-89be1d602f06 | -9.39969 | -48.43868 | 2025-06-04 04:51:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efeeb080-e602-3500-bf5d-3509a19164f6 | -8.95556 | -47.28275 | 2025-06-04 04:51:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f36a8e1c-abd5-37c0-8f8a-f1f341ce43d2 | -6.21756 | -43.33955 | 2025-06-04 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38b47574-7995-3b0c-8494-38a864c57053 | -10.05329 | -49.66123 | 2025-06-04 04:51:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c56f6d69-0886-37c2-8604-e20729b5ba6b | -7.21949 | -43.13196 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 641543da-d170-36fe-a4f3-cb11e5ef1dbb | -5.18713 | -48.08045 | 2025-06-04 04:51:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 671845cc-9b18-3e52-94f9-4b75c00002bf | -6.96765 | -42.91388 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 5fce8c1e-3def-332a-b531-d3d7ef742fd2 | -8.69161 | -48.29369 | 2025-06-04 04:51:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ab4745cd-e5a5-3bec-9ba8-e468dc9dd0b9 | -7.0198 | -44.58118 | 2025-06-04 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 369051f2-76a9-32ef-be00-28059077a323 | -9.56452 | -50.51665 | 2025-06-04 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd289d2c-9e3a-3d99-a9c2-66e7b80dd311 | -7.90171 | -50.35867 | 2025-06-04 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| aae935f0-d890-3bd1-bcdb-68704f411cc8 | -7.98226 | -47.23028 | 2025-06-04 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb3b2e03-1aa1-36f0-bb02-5e857c3fd763 | -6.21489 | -43.33994 | 2025-06-04 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3dcbf749-193c-36c1-b13d-be8535a12cbd | -8.91166 | -50.04331 | 2025-06-04 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| af353615-75e1-39ed-b3b4-e4b560bddfb2 | -9.38413 | -48.40411 | 2025-06-04 04:51:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc885e61-0769-322c-a8f6-e6af9194cfe8 | -11.83941 | -51.28542 | 2025-06-04 04:51:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d180e3d7-4c6f-3d58-a146-1198faf98d85 | -9.66542 | -48.71529 | 2025-06-04 04:51:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4507295a-9f85-3c64-95c7-646b266896d7 | -9.37246 | -57.44193 | 2025-06-04 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9025d184-482c-3202-bdcc-91630ca6fd78 | -12.31968 | -47.25436 | 2025-06-04 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 540721af-4258-3292-87cd-a78134c721ee | -7.98337 | -47.22247 | 2025-06-04 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec5a7b40-325f-30f6-adbe-3f094ee2d180 | -10.29756 | -57.13874 | 2025-06-04 04:51:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49eec432-8d6e-39c4-9857-fb663cdb985b | -10.76127 | -54.78463 | 2025-06-04 04:51:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed7b3323-7256-3ee7-a780-c9b1dbc9abcb | -10.0685 | -55.55017 | 2025-06-04 04:51:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a758f65-c82f-3dba-a75b-e06348d7411d | -10.69535 | -57.65091 | 2025-06-04 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| caf3771d-c773-3dac-a682-d7d21f5d8e76 | -11.84233 | -51.28995 | 2025-06-04 04:51:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dd748152-e8c2-3370-a653-300d22756dc2 | -7.58778 | -45.86573 | 2025-06-04 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c94b754f-e0cc-3d3b-8526-efd16992d4cc | -7.0847 | -49.59587 | 2025-06-04 04:51:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60292e8b-bf12-3524-8d61-b7e4a7c5022e | -8.84054 | -49.84614 | 2025-06-04 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48e7c4e5-baed-3515-87f5-cfe3c173ca09 | -7.88568 | -46.18671 | 2025-06-04 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bee7fec2-f28a-32f7-b4dc-e0d94073d0e4 | -11.40838 | -54.7191 | 2025-06-04 04:51:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fae9a547-02ae-34fd-a204-066425158a28 | -7.90522 | -50.3592 | 2025-06-04 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 9422c10c-3b64-3024-851f-9143c0254324 | -8.84418 | -49.84671 | 2025-06-04 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4080587f-3722-3962-8a32-9533c33298bd | -9.60595 | -49.01436 | 2025-06-04 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae9c55b5-74c0-3e0b-a468-1619b7de436d | -11.40417 | -52.93996 | 2025-06-04 04:51:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0992d099-25c6-3c6d-8b4c-a1ad35f3aaa9 | -6.69137 | -43.68357 | 2025-06-04 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b6e92b8-fa14-37ec-9639-d038b160b866 | -10.38408 | -53.51049 | 2025-06-04 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18e97512-289a-3e27-9a9f-250b532cb2eb | -8.19897 | -49.80093 | 2025-06-04 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9178163-ae6b-3a46-b764-0a4b57535fda | -6.2131 | -43.3319 | 2025-06-04 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2facb3b9-8c10-3063-a5e1-8bb83ccfc130 | -8.68782 | -54.87066 | 2025-06-04 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99c20f67-284b-3379-9370-7b5fc3ac8127 | -6.5443 | -44.64698 | 2025-06-04 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61b3074e-b139-3298-b970-3e53e769c2d2 | -10.61786 | -49.55943 | 2025-06-04 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 370f0dbb-432a-3bd9-a1e6-e4ba4eb52f81 | -11.83123 | -51.29227 | 2025-06-04 04:51:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40e6ae46-8d21-3e52-9d90-07bdd27e2823 | -9.20289 | -49.69067 | 2025-06-04 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67bfb603-dc5a-382b-ab2a-6af2dd65ebc5 | -7.32583 | -45.56049 | 2025-06-04 04:51:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 671a2e32-ab0b-3bc8-b46a-58061e1638ed | -7.98597 | -47.23462 | 2025-06-04 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 277ea7fe-db26-3837-bdcc-5acc128f3400 | -9.49314 | -51.34802 | 2025-06-04 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a4363bb-7ba2-31b4-bfac-eaf6659e58d1 | -10.49391 | -53.65632 | 2025-06-04 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 28670dfe-4986-3574-a997-742afeb31dad | -9.45452 | -48.87524 | 2025-06-04 04:51:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13cf60eb-f3bc-3d1e-bd24-640edb33b587 | -7.14558 | -44.0428 | 2025-06-04 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb804209-5009-32eb-8799-a5d88155ec52 | -9.62413 | -62.81731 | 2025-06-04 04:51:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cea635e4-0134-3b5d-90c1-a85f2f5f04e3 | -7.15078 | -44.04358 | 2025-06-04 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3d56c0a-1366-3959-ab58-323967fd5bbf | -12.31847 | -47.26348 | 2025-06-04 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6fd7ab6-199f-3b0c-8e66-204fff933b2a | -6.21 | -43.33564 | 2025-06-04 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3341b2f4-3384-3d2b-96ee-cdb011fd9f68 | -10.49775 | -53.65337 | 2025-06-04 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 94be4c75-64f5-38db-bd54-7c4e13ad34db | -7.64223 | -49.54638 | 2025-06-04 04:51:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7529d4a4-0d1b-3bc6-b779-7990e1a94387 | -7.99871 | -50.70064 | 2025-06-04 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6aee1907-9575-3ca3-87d8-7eb39d50fad1 | -10.69319 | -57.64095 | 2025-06-04 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b99bd90-e257-342d-a39f-549558d9ba00 | -8.90668 | -49.32076 | 2025-06-04 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c27577f-9441-329b-b607-773424005f09 | -11.83882 | -51.28941 | 2025-06-04 04:51:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a7e4d43a-3253-3bff-8cee-c18136736579 | -7.21348 | -43.13475 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fb877421-bb3a-3992-9ce3-b05c0f24a533 | -11.57913 | -47.45586 | 2025-06-04 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3f903df-acf5-3efc-bd26-c8f68252497e | -6.24654 | -43.3686 | 2025-06-04 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5792c69e-0352-315d-81b3-e17f11baf4a7 | -7.89476 | -46.1881 | 2025-06-04 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2be0bee-0769-347f-9aef-c12f6ac6d1b7 | -11.5484 | -47.31576 | 2025-06-04 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb5d54d9-a2f4-31e4-9553-a5606c2b73ec | -11.61531 | -47.61869 | 2025-06-04 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README12.md)
