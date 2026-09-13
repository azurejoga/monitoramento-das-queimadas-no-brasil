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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b60603b5-95c9-3979-93ed-13803440a92b | -6.106 | -57.6521 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2c3d5ab-4102-3878-91c9-6f343ab88e0b | -2.6642 | -57.5084 | 2026-09-13 01:05:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f93d6e6c-5ce3-3ed5-8c43-f07814c0c26d | -10.9579 | -58.955799 | 2026-09-13 01:05:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e10bc177-6df2-33be-aa58-6b36a6a64944 | -7.1945 | -45.895401 | 2026-09-13 01:05:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c15ed2b3-c990-39f3-96eb-862acf09c73e | -2.682 | -57.541401 | 2026-09-13 01:05:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2bd81831-75fb-3a59-b1af-75925c058b67 | -13.6125 | -47.885201 | 2026-09-13 01:05:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 44d26eba-854a-3e01-af7b-c455355e3391 | -13.4051 | -57.027302 | 2026-09-13 01:05:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2e40bc39-5aee-3e0a-969a-75fa3fb89406 | -2.6722 | -57.543598 | 2026-09-13 01:05:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06537743-6d89-3497-a17e-e1e0a61bc9d5 | -8.5328 | -54.716099 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bf5246f-4df8-33be-b6a3-9798a1685e66 | -10.917 | -47.821201 | 2026-09-13 01:05:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 713eea13-629e-358b-b3fb-5940cc0120dd | -6.2419 | -51.701 | 2026-09-13 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26c08f7f-bdde-3588-b48a-1ccd6022ea4a | 0.1454 | -51.4729 | 2026-09-13 01:05:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8c982173-a9e9-396d-bcca-871046137632 | -17.6262 | -46.663601 | 2026-09-13 01:05:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d240b034-dbdf-3c0b-99a6-ffc0c565c001 | -15.5673 | -53.782902 | 2026-09-13 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1da10b6e-6be3-3113-b6c4-610e1da63f40 | -9.4193 | -50.134499 | 2026-09-13 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f99c06d3-6409-3b11-877f-b1ec8307f0ca | -8.1163 | -54.788898 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c3f7dc1-468c-332d-ac34-1d1d39c98609 | -9.7099 | -54.360901 | 2026-09-13 01:05:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 225460a4-33ed-3acf-8359-739a94103794 | -9.7185 | -48.110401 | 2026-09-13 01:05:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7bce071c-4f1c-3bea-9f36-276f318dd12d | -10.5301 | -51.3633 | 2026-09-13 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 64627814-990b-3e86-8361-1dd2683cea6f | -8.5442 | -54.720798 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a3b68f4-a11d-39b2-b868-a00cee1b6bbf | -2.613 | -54.7659 | 2026-09-13 01:05:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45b98b78-7a48-388c-81e3-20ba52a49c84 | -10.579 | -51.351601 | 2026-09-13 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 182da43f-e1d0-36fd-bc5b-d082c675840f | -7.5337 | -47.329899 | 2026-09-13 01:05:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99e79fca-5ac6-377a-9120-0ac43c161a59 | -16.3016 | -53.844799 | 2026-09-13 01:05:00 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 57768d17-5211-361b-a828-d9999cdb93f1 | -12.1505 | -48.9562 | 2026-09-13 01:05:00 | METOP-C | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 687bdf72-b6a4-3b8b-89a6-5601ffe9eaec | -6.7374 | -59.4286 | 2026-09-13 01:05:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ac278cb-9017-30f1-bc9c-a29ba3e29852 | -2.9641 | -50.391399 | 2026-09-13 01:05:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f49a457-abfd-36ca-8579-3f7234c25d59 | -6.6693 | -58.702499 | 2026-09-13 01:05:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55423dcb-6e1b-3889-99d0-3868aab1f2f2 | -3.8717 | -51.183498 | 2026-09-13 01:05:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25f66e6d-110d-3ea3-8f93-c9d61efc8932 | -6.1018 | -55.675598 | 2026-09-13 01:05:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82014776-3dc5-3074-a2f8-21e614862a80 | -3.8839 | -51.191502 | 2026-09-13 01:05:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee801c88-cdb7-3d8f-b3aa-458c98f7c047 | -6.1374 | -57.700401 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f408bbe-c2f6-3adf-9369-689e0014b767 | -5.1169 | -55.968102 | 2026-09-13 01:05:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ae3d067-eb17-3df3-b839-fe08fb4d345f | -3.7217 | -61.737 | 2026-09-13 01:05:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2146b31c-a41d-332c-8f61-5ea7a96b7ab8 | -5.8047 | -53.801102 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 168e073d-eb16-33a6-9415-c7d990b4e1fd | -9.1784 | -59.438801 | 2026-09-13 01:05:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5712322e-b3fe-30fc-8c4f-d18676cf9b9d | -13.4547 | -48.497101 | 2026-09-13 01:05:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b73d6dc4-30ed-3fc0-ab71-0f309ab5d397 | -12.1531 | -48.9669 | 2026-09-13 01:05:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4853085c-587b-3338-a32c-d0c2f36a3bcf | -6.0799 | -57.856499 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 036ed06e-de13-3cc1-8720-406c5475c3b3 | -4.9352 | -45.843399 | 2026-09-13 01:05:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a15ac897-9abe-350a-a8d9-35bea72709ea | -10.5809 | -51.359798 | 2026-09-13 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69dd623f-4780-3b44-94f5-2867e8aa4d08 | -15.5689 | -53.790001 | 2026-09-13 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8128d788-5560-33e1-94d9-45c309991f2e | -10.6864 | -54.166401 | 2026-09-13 01:05:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd9f9191-06f2-3c90-bc64-f027fe6bc8d7 | -9.4169 | -50.124599 | 2026-09-13 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 333592d9-ac85-3cce-bedb-ec3e458a6d8f | -4.9199 | -45.8232 | 2026-09-13 01:05:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cf8764a6-63b5-337f-98c0-96cdbf8265a6 | -6.1108 | -57.627399 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6cfc52f-7bf1-3de1-91fd-260a3519690b | -12.8532 | -44.355301 | 2026-09-13 01:05:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd26f8e8-914a-3b0d-84d1-563bc84e8e9a | -9.712 | -48.084 | 2026-09-13 01:05:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c27a3f70-ecb5-331b-8629-769b7f4a0776 | -8.0391 | -54.856998 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d47c78e-3880-3b50-9335-fcfa70ce0fb0 | -6.1357 | -57.692902 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 587ac520-17b4-3b32-9125-1b28654734c4 | -6.1835 | -57.722 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 794aeba5-f50c-3bc4-8bf9-e5ea2ddf6a03 | -5.8128 | -53.791599 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cecab913-b6d8-36ad-9137-9f77e9177fab | -6.1002 | -55.6688 | 2026-09-13 01:05:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 503d6fbb-c9f3-3b6e-8e01-16b5c81eaa48 | -3.0464 | -51.2659 | 2026-09-13 01:05:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04e0ef53-d1b4-35cc-a284-ff19c7acc118 | -5.9677 | -57.769501 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f8a6dc2-2e77-37b0-ac81-ed300c72ee2d | -6.3417 | -55.823601 | 2026-09-13 01:05:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41eb81d1-8899-3fe0-b5ad-3d613ccff2e2 | -10.6978 | -54.171101 | 2026-09-13 01:05:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8b93d6a-63aa-317c-bbcd-20ec5a78b684 | -2.6674 | -57.522499 | 2026-09-13 01:05:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cb38508b-d409-3d0c-a427-50291b2c1e78 | -3.7341 | -61.746498 | 2026-09-13 01:05:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb121587-1d4b-3cbe-aa1d-bdc165f7e477 | -7.8754 | -54.727699 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee9da599-77f3-3c15-8ec6-cf6fa62f3673 | -5.7983 | -53.817902 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 120daea2-8521-336b-9844-b4778095c717 | -9.7212 | -54.365601 | 2026-09-13 01:05:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75fd57be-aa01-35ed-801d-cc86703b410c | -6.588 | -58.8452 | 2026-09-13 01:05:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fb00a2c6-eff7-347f-90a3-6bfd0eadcfe1 | -8.608 | -55.227501 | 2026-09-13 01:05:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2d3c693-b509-3f00-990f-8c8550ca84b7 | -13.6222 | -47.882702 | 2026-09-13 01:05:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 95300e13-6fba-3361-b4cd-fe9f64e7d35d | -8.0587 | -54.8526 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0ae7ced-a558-3769-9e4e-285d09ad1490 | -6.8645 | -55.583801 | 2026-09-13 01:05:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c4ef9cf-1f4d-3cd1-8178-9ad9f4dba07e | -6.8525 | -47.447102 | 2026-09-13 01:05:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e97fb2cc-f5fc-3034-b868-bc1e211e1754 | -10.6946 | -54.157299 | 2026-09-13 01:05:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef8d55bc-2821-3028-9584-81a9396b75a7 | -6.7597 | -55.6217 | 2026-09-13 01:05:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d662985-7ab1-32e9-88ed-b3002355cd54 | -5.8243 | -53.7966 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59c467fb-f756-3447-aab8-1ca23a5cff39 | -12.8491 | -44.378799 | 2026-09-13 01:05:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eaf1076f-e564-3fce-a75b-45c7acdc2960 | -10.5711 | -51.362099 | 2026-09-13 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 028fadb7-6d98-36d4-b383-5ae6699a48b1 | -8.5411 | -54.707001 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aa6ce51-8f1d-3160-9fd1-881058873df0 | -6.8598 | -55.563202 | 2026-09-13 01:05:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b990bd26-a4a8-3323-9a4b-253eaf3696f4 | -3.4068 | -48.8783 | 2026-09-13 01:05:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1543b3eb-78f7-346e-bee9-16ae3cbb0add | -7.3653 | -45.354 | 2026-09-13 01:05:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8b1788b-a30f-3937-a7dd-9df3a0cb3edc | -3.7243 | -61.7486 | 2026-09-13 01:05:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42fee3a4-7b00-35b5-ae3a-656933653863 | -10.532 | -51.371498 | 2026-09-13 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4902be9e-7b40-3c03-9f37-d8ec604914bc | -8.0458 | -54.841099 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32d8e7df-4064-36bf-a343-b664d04f61b1 | -13.4617 | -48.483601 | 2026-09-13 01:05:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 44745e30-683f-3d17-a3c5-8c4d906dc602 | -6.1638 | -57.726299 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b22c834-b1f0-36a3-8d5e-4d13c2d3af15 | -7.0218 | -44.611801 | 2026-09-13 01:05:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34c60e58-dee7-3715-b8f5-ebf463b53921 | -5.8064 | -53.8083 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbf2eef8-b943-33b9-8703-6dc1a95572e5 | -10.5457 | -51.385799 | 2026-09-13 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd0acf6d-651a-37c1-92e2-fa1c8dedef09 | -11.2491 | -54.146801 | 2026-09-13 01:05:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23b52d80-8f3b-3b1c-b8f1-c353ae40ddb7 | -8.3193 | -49.686199 | 2026-09-13 01:05:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c5f2eba-4e9d-3a6e-86c9-2a6493890cc9 | -6.8613 | -55.57 | 2026-09-13 01:05:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3a0cbe6-25a1-36ac-abc8-2d80b64ad88b | -7.0187 | -44.6395 | 2026-09-13 01:05:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 966054e8-995b-3f04-9bc0-f8ce1af0f82d | -15.0221 | -48.511799 | 2026-09-13 01:05:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 15c0df65-ea53-3124-a0ec-b6a6de42fecd | -7.8723 | -54.713902 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac574c9f-b66e-39a9-998a-fc6a42b370c3 | -6.0731 | -57.861 | 2026-09-13 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| a3529d0a-241e-3d76-ab93-f9c255cde817 | -10.6827 | -54.1679 | 2026-09-13 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 332.6 |
| 70d0da66-0f9f-39a5-b957-199d252ec2f4 | -2.6602 | -57.5119 | 2026-09-13 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 29.2 |
| ccdaa65e-3c9c-3081-9c1f-d259bff9c17d | -15.579 | -53.782 | 2026-09-13 01:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 9b65154e-18ea-3ff9-8b31-c342ab0a8acb | -10.6829 | -54.1475 | 2026-09-13 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 161.4 |
| c55ec7a8-cd6c-30a6-a9fb-0198243382c4 | -6.1111 | -57.6645 | 2026-09-13 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 51bd9b7a-8335-3a98-88d7-2c33f9d58aa2 | -12.8543 | -44.386 | 2026-09-13 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 174f8321-3130-3592-90c9-0c0797fc88a4 | -5.1254 | -55.9748 | 2026-09-13 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 2453b1c3-1a8c-31a4-89a5-06dcba62aa9b | -10.7015 | -54.1663 | 2026-09-13 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.9 |


[Clique aqui para ver as próximas entradas](README15.md)
