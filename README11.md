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
| 2424acee-ac16-37a0-ad98-a9feca584c3b | -7.615 | -61.362301 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 585ec6d4-58d5-3afc-9a63-175235e44a83 | -11.172 | -51.280201 | 2026-08-29 00:52:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a0f415e-64f1-3120-848b-e2419803bc7c | -7.3433 | -55.167198 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61de5775-0256-3305-bdd7-012330db3d8a | -7.4891 | -61.397598 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8340305b-6c46-3d96-8868-0495086b5c40 | -19.224701 | -57.656799 | 2026-08-29 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 099bdeaf-b0f6-3e81-8f6d-02eb71cfecc8 | -4.1557 | -60.6768 | 2026-08-29 00:52:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 29d7caf5-affd-3017-afca-e9964128ab42 | -11.1827 | -55.087502 | 2026-08-29 00:52:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c91c8bce-12ec-3723-936c-cd490e5c941f | -8.5782 | -54.812801 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b19d23d-c08a-3ccd-96d9-e0727e6bc3c1 | -8.9694 | -50.798901 | 2026-08-29 00:52:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecb7e4e5-8673-3d86-b371-e756c7727efa | -5.8708 | -57.765999 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7860c916-5154-389f-aead-4d0d6c838ed1 | -10.5099 | -59.622398 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62fc973c-eaab-39a8-9e2b-df0779302e99 | -6.852 | -59.436901 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a873fa0c-76e8-37f2-a2c3-2704fe0c76f7 | -11.701 | -54.537498 | 2026-08-29 00:52:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc898053-562e-35c1-9603-ef47c47efae9 | -6.5711 | -55.429901 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0413581-53bc-3d58-b3ba-1dd2abad4716 | -10.7495 | -54.020302 | 2026-08-29 00:52:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71c703ff-4e24-39ef-bd30-e34be3c17dcf | -8.6029 | -54.829899 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea23733f-7123-355b-8987-769b7a0284e7 | -6.7325 | -55.458698 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac1ea525-0545-34ec-87e1-92a8908d2269 | -7.0423 | -55.6791 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dd321b9-9e14-355f-9804-f20942b7b48e | -10.2929 | -62.805199 | 2026-08-29 00:52:00 | METOP-B | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2ca529d9-d720-3a5e-8100-6796d21c4e89 | -14.1871 | -52.831001 | 2026-08-29 00:52:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 56f31afc-6e69-3551-a712-75f7f6490df4 | -11.0194 | -57.243099 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2dfee902-d584-3b22-9e18-51085f8502c8 | -20.9443 | -57.572201 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f50db364-3dc2-3bfe-9c07-72c729594966 | -14.1998 | -52.840401 | 2026-08-29 00:52:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 817e37b4-3415-3d8d-9167-ac38db79bd9a | -11.0318 | -57.207802 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dbfee457-8526-387f-8fc9-05e685896c7f | -10.3921 | -61.227001 | 2026-08-29 00:52:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14826198-e4f2-38c3-ba58-7d7e86638d6d | -7.9248 | -61.367699 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bf80c9e3-c4ed-3b5b-972e-8ca5122ab76c | -6.5648 | -56.540798 | 2026-08-29 00:52:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18f02297-09fd-346d-b841-45483ee81b47 | -6.883 | -59.437302 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 581f1fd1-3890-3eb0-82ae-71c103773a65 | -7.5828 | -61.310398 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4eaa323b-8504-3445-8946-83ee48299d0b | -15.1119 | -53.5592 | 2026-08-29 00:52:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cdfb4232-040f-320c-80a4-ce0e250f5790 | -11.0371 | -57.230801 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc1683ae-dcef-36c8-aaae-2d21607e7f02 | -11.7082 | -54.524799 | 2026-08-29 00:52:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be858ade-946e-39a2-87cc-07bb5006feb1 | -10.7522 | -54.031601 | 2026-08-29 00:52:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c9549e6-2bef-3cf3-9a07-2871c5360a24 | -14.8928 | -52.632 | 2026-08-29 00:52:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4cb30a0f-e2b7-351d-8d3d-4c1a3b163071 | -9.2553 | -65.487 | 2026-08-29 00:52:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7b4b1204-7cb1-3140-a8ac-f9e43923dbed | 0.1435 | -60.388401 | 2026-08-29 00:52:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0180dfbe-5044-36fe-b785-c2c7372f654f | -6.9444 | -58.938099 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d5a5c7e-4a6d-3029-b77f-b0ef7c2fe5fd | -9.9616 | -53.921299 | 2026-08-29 00:52:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a98796c8-564f-3aec-908d-a6423b850b78 | -6.535 | -55.2337 | 2026-08-29 00:52:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 341cd87e-7da5-3cc9-8492-bf12e87c52d6 | -7.5008 | -55.309101 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a386aab-3198-3b8e-9f64-b615c4c64193 | -11.185 | -55.097099 | 2026-08-29 00:52:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a677a7ab-6e8d-3570-9259-2eb23284e2e0 | -5.8787 | -57.755699 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae489452-0eb0-36fb-bcce-12994758a209 | -9.1395 | -61.001099 | 2026-08-29 00:52:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c97fa8e-20ff-318f-944b-fd8ed8d23b31 | -8.5853 | -54.799599 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 930a6951-951e-3214-a58c-1611d8f165c1 | -6.7509 | -58.723099 | 2026-08-29 00:52:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39593e5a-6773-3ea8-9e6d-74c6b64d7abf | -7.5318 | -61.358601 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39ac1ee2-208e-3e2d-8036-78236a05ee4b | -7.6005 | -61.3433 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ce55706-62fb-350b-a9ef-3b619b1bdb80 | -8.5925 | -54.7864 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc2c47d8-cb2c-34a7-ad52-53ef25889999 | -9.4116 | -51.572601 | 2026-08-29 00:52:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7d9d203-2697-3785-b4ef-ff96db0b4d52 | -9.598 | -55.108601 | 2026-08-29 00:52:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83b6af73-5563-39a1-b3cb-f868a3ff8106 | 3.1117 | -60.6945 | 2026-08-29 00:52:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b41a4869-9f80-3f4f-b66a-961a91329895 | -22.0292 | -56.034698 | 2026-08-29 00:52:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d73b1637-14f2-34a6-a965-27e6e82d1145 | -20.9557 | -57.577202 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2780685d-836d-38a1-bbf4-a6cd9dcbcb72 | 0.1419 | -60.395599 | 2026-08-29 00:52:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 07c8df45-179d-30cb-9b9e-b444ae6a0640 | 3.11 | -60.7019 | 2026-08-29 00:52:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0adacc5b-b11c-38fb-8b77-f3ad9a5b45f2 | -14.4743 | -58.518299 | 2026-08-29 00:52:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e2a4acb1-fba3-3f79-9891-cd55b4348e25 | -14.9426 | -56.315102 | 2026-08-29 00:52:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3b47650e-701d-3f27-a6a5-2441b1233a9f | -14.155 | -52.8265 | 2026-08-29 00:52:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2f92d097-3fd5-35f0-872b-d88679424dcd | -10.4739 | -64.481796 | 2026-08-29 00:52:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bec831c8-70f3-36c7-9692-b72453ae90d0 | -14.8964 | -52.605202 | 2026-08-29 00:52:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 965d4a41-fd4a-3aa5-be07-2a3d088f3786 | -3.6094 | -60.539001 | 2026-08-29 00:52:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cdca8040-82dc-3b76-bf74-0916f978693b | -7.4836 | -55.279999 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd4230d7-552f-33ac-969f-e34d629475e2 | -6.953 | -59.473 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b56d481c-1cb6-3b92-8af0-7c928fef7d5a | -14.3831 | -50.037201 | 2026-08-29 00:52:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4e02d4a4-9f07-3958-9caa-c5d1dc427f6d | -9.9177 | -60.4286 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34ef609c-101b-3869-8608-eecfe958a544 | -6.1652 | -57.791199 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18e1ae19-5da5-3f51-9ba1-afc9c61e9e7b | -3.2082 | -61.1325 | 2026-08-29 00:52:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9fc1524f-2d00-3837-a742-329f0294282b | -20.9589 | -57.5919 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8a81fed7-6f73-3a2c-97e8-f892a9f030f1 | -10.4935 | -64.477699 | 2026-08-29 00:52:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0633276a-8211-301b-a6e9-562b2376ebe3 | -6.7228 | -55.460999 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5193ee8f-79f4-3a85-8091-962450555a4a | 3.2389 | -60.126499 | 2026-08-29 00:52:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d0031583-333b-31d0-8123-5ce35ada0b24 | -9.223 | -59.761501 | 2026-08-29 00:52:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ccd57d7-e879-3a17-b3c2-bf18f0b1101a | -14.9025 | -52.629398 | 2026-08-29 00:52:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5334c26b-5c9a-386e-9cef-39cd416714ef | -13.4666 | -57.028599 | 2026-08-29 00:52:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 88acc3d5-7f7f-31ff-969a-009da5984e79 | -6.7547 | -55.639702 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1c39db9-2dce-37db-a570-f7328f00dc28 | -13.167 | -55.6572 | 2026-08-29 00:52:00 | METOP-B | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 94c478a1-ada3-3fdc-aedf-e2efcf07d224 | -6.73 | -55.448101 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8be14b6e-d15a-3a93-a00d-aad9c0c70495 | -10.5083 | -59.615398 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 529e6881-8076-35de-8ff5-be996ba8a990 | -11.0291 | -57.240799 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b72fe47-799e-3a35-98ee-9a75ebf74f8c | -7.4875 | -61.390598 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 183ef8d6-7c49-3e6b-ba1a-2ec3b3083d5d | -6.7571 | -55.650002 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84d7d43b-2b7a-371f-9795-26e150455453 | -14.2706 | -57.0252 | 2026-08-29 00:52:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79b09bf2-b3fc-3371-8313-aca98cd7853a | -20.962 | -57.606602 | 2026-08-29 00:52:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 58bdf6f7-818c-316d-96f1-9985a831b5b6 | -11.1924 | -55.085098 | 2026-08-29 00:52:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1d1805a-9233-3a05-9fd5-6276a65ea538 | -8.5277 | -55.335098 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cd1ba25-0cc8-376e-b799-aa4a48c4e9f2 | -9.9389 | -60.431198 | 2026-08-29 00:52:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42f532a6-c58d-385d-b67d-e31988d587ae | -7.5617 | -61.307598 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b715fa8-3e4c-3b12-8dce-45872e61c0a5 | -8.5846 | -54.753601 | 2026-08-29 00:52:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96840a6f-8784-3925-b7e7-8437a70857b8 | 3.2371 | -60.1343 | 2026-08-29 00:52:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b8ab82f8-9d75-3fc0-9d14-91cc8c04be23 | -6.9642 | -55.697601 | 2026-08-29 00:52:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87877954-c78e-3f21-89b3-d792f3b2a807 | -6.8848 | -59.399899 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 56084899-0fa1-3657-bb6d-fb13f8c2165e | -5.8983 | -57.751202 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0aa95a79-665f-30a4-b810-7afc2fc65e9a | -7.4777 | -61.3927 | 2026-08-29 00:52:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32c6860b-361b-3961-a001-53d69a84dcbf | -18.981899 | -47.419701 | 2026-08-29 00:52:00 | METOP-B | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5614e83c-bf62-3d38-9040-17659f7f8334 | -11.03 | -57.2001 | 2026-08-29 00:52:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f59fc8af-d7f7-372b-b636-2c5a2a45a025 | -6.1536 | -57.7855 | 2026-08-29 00:52:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff070c8d-55ef-31ff-8de0-816437b82f3f | -10.7398 | -54.0228 | 2026-08-29 00:52:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 276b9dc1-94d3-3ddc-9ec4-239be5bb3028 | -6.8418 | -59.936699 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34d570ac-3d7f-3540-a3ce-9c619cd132c9 | -6.9461 | -58.945301 | 2026-08-29 00:52:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d4ccb22f-3fb0-3318-9e4b-81d772a943cf | -9.4223 | -51.697399 | 2026-08-29 00:52:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
