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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b3e827a-cece-34fc-9539-f182dad10ee3 | -10.00657 | -59.22253 | 2025-08-14 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 64d9749a-2fa7-3e3b-b3a7-e0c1aeb0bf2c | -6.95584 | -44.56437 | 2025-08-14 00:50:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| f8afab4d-cd0e-393b-8a08-11d7d7980d9f | -8.73858 | -44.01631 | 2025-08-14 00:50:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 44.7 |
| eb589c2d-3d15-3fac-8dca-1ab3ec69c7ec | -6.89443 | -59.16827 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 592.1 |
| 88d41e6a-4861-3fcc-8f7f-384a06b473b3 | -9.74621 | -48.57219 | 2025-08-14 00:50:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 35cb9f13-1ea2-3a9c-83d8-fcc92082825e | -7.12967 | -60.11324 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.8 |
| e4937a3f-5831-3590-957f-aede2c7bc2a5 | -6.90806 | -59.16668 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 184.7 |
| 8b8a1ecc-c04d-3d70-be4b-2d1e03b952f4 | -7.87662 | -61.80879 | 2025-08-14 00:50:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 43c1d856-a5c9-3c67-a19d-089c4ace6185 | -7.11873 | -59.63362 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 3d70058b-db35-3229-962d-cadd07a8f93b | -6.27238 | -53.67531 | 2025-08-14 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2e2311a2-c17a-39b8-8265-6244256d8e4d | -8.51535 | -43.30848 | 2025-08-14 00:50:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 8a1b3384-bd8c-3e06-ae69-03a899f53145 | -6.89169 | -59.14583 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 837.5 |
| 453320e7-a0cc-3b56-9d31-1dc898cc5902 | -6.88083 | -59.17005 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 336.9 |
| 2091781f-ace9-3880-8b6a-690cd501caf1 | -10.09484 | -50.34673 | 2025-08-14 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9480bcbb-c941-33ee-b6ea-0a9b489b731a | -9.14912 | -59.65197 | 2025-08-14 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 25677473-468b-3ed1-8f6c-6e2a1e008194 | -5.74891 | -59.87868 | 2025-08-14 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| be5b3eaa-1dea-3b88-b752-07747b2edf46 | -9.15019 | -59.6465 | 2025-08-14 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| f655412c-c717-3d6d-ab9c-d0e8e7712290 | -5.8876 | -57.74223 | 2025-08-14 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 7ebb12dd-2fbc-3713-9873-d0346aede6f3 | -5.89368 | -57.73529 | 2025-08-14 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 2de8c014-c973-3c57-9bca-0bed61abbc8b | -6.5346 | -56.21298 | 2025-08-14 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4656457e-da30-3cf2-b323-a8bb7a4f0045 | -7.13295 | -60.1401 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 898d2678-4be3-3bfe-b485-b7932fcd841a | -7.87784 | -61.8539 | 2025-08-14 00:50:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 318d0129-1845-3942-a997-f6fab5912d08 | -6.8781 | -59.14748 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 443.4 |
| afa74596-8e98-3a5c-a734-02d921641607 | -6.10313 | -59.94149 | 2025-08-14 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 65c864a9-7d20-3034-b923-d101238ef06d | -9.50885 | -60.54047 | 2025-08-14 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ad611042-2946-30ba-8c00-64941a41c4f9 | -6.88703 | -59.17443 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 301.0 |
| 4c03204c-72cf-3c27-b7ec-c56268560451 | -6.54353 | -56.19838 | 2025-08-14 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| fbebdaac-7c56-3f47-a892-2c8e99c8d1d8 | -6.90528 | -59.14415 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 461.3 |
| 89cd94c5-5d5a-3f0e-92f3-d3892daf4852 | -8.10725 | -61.17796 | 2025-08-14 00:50:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 37.0 |
| f431e731-c3ff-33eb-b9b6-20d569b579f0 | -6.89053 | -59.8852 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| dda90b1f-c1b7-3e7c-a502-d1fad7e76aa0 | -8.18433 | -49.03128 | 2025-08-14 00:50:00 | TERRA_M-M | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 21.7 |
| b4435ec7-71ad-3fef-8452-92b20fa8edb7 | -8.51987 | -43.33689 | 2025-08-14 00:50:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 312e0c7c-d5b2-36a1-87db-c2afcc1fae74 | -8.53476 | -43.33438 | 2025-08-14 00:50:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 66bbde90-056c-338c-951b-b8bab85dde26 | -6.60852 | -43.895 | 2025-08-14 00:50:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 74477603-6807-3380-8f38-dd0c18663c99 | -5.75517 | -46.66706 | 2025-08-14 00:50:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| d162b41c-8166-301f-94ac-56f7749759a8 | -9.13866 | -59.6755 | 2025-08-14 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 3957a97c-58e0-38a1-812b-7a54b6f1222a | -9.13554 | -59.64835 | 2025-08-14 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 1dcacb94-56de-31c4-9d75-ddae1b594493 | -8.18277 | -49.02047 | 2025-08-14 00:50:00 | TERRA_M-M | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 23.8 |
| aea7f5b4-bf80-3f2a-b89b-bdf3bd78fcc0 | -5.88104 | -43.92533 | 2025-08-14 00:50:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 3921419e-4b4b-3c79-b90d-3030ae83cf28 | -5.81129 | -59.22625 | 2025-08-14 00:50:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 8c32c53d-c8fc-313d-9bbd-62a306f784dd | -9.49526 | -60.51575 | 2025-08-14 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| b587d977-2e50-3c63-962c-680ea12c402c | -6.08888 | -59.94364 | 2025-08-14 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 205.1 |
| 54cd6460-ca07-38ed-a9fe-78f1321908a9 | -4.23076 | -47.21569 | 2025-08-14 00:50:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 23.2 |
| f38ba70c-067f-3238-94f8-538dc4a6b619 | -6.89478 | -59.12777 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 95161777-f43c-3ec0-9d8b-dfbf9a487c5d | -5.89578 | -57.75184 | 2025-08-14 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| bf688fcd-78e7-3484-8648-3b498097d40d | -9.49907 | -60.54803 | 2025-08-14 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| f0e4dabc-c621-321b-a3d6-99235e775a2e | -8.53359 | -43.32916 | 2025-08-14 00:50:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 3a69ae23-62f7-320d-96d4-6a5b2a7ac682 | -5.97722 | -44.15697 | 2025-08-14 00:50:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 70451b28-333a-309f-89a6-8b88813c577e | -5.75205 | -59.90327 | 2025-08-14 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| a6b53a60-ede7-39dd-bee4-134299d59ee1 | -9.15247 | -59.67914 | 2025-08-14 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| c94c0559-ab7a-3159-a93e-7473fe9442e0 | -6.94712 | -44.55918 | 2025-08-14 00:50:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| f726104a-b472-36e9-a8f3-dcc5c1cc379c | -6.90065 | -59.17276 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.7 |
| aa593887-56fd-33b3-bbb0-44f419ea81ad | -6.10623 | -59.93582 | 2025-08-14 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 5a5a8677-f0c7-34f4-8f2c-f8166e4fc4f2 | -6.8881 | -59.89216 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.9 |
| dd3a0cb9-a3d7-3109-ae6c-4a3fb71dafea | -6.94305 | -44.53415 | 2025-08-14 00:50:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 605f32a1-9d67-3cf6-b7bb-1699712e1b1b | -6.87053 | -59.15358 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.3 |
| a07a069c-6aab-3fc5-a8ef-535836af84a2 | -6.09198 | -59.93801 | 2025-08-14 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 20e412a6-3e86-30e7-8bd2-7349187c7a23 | -7.12895 | -59.63778 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| fd993aad-68db-3477-a95c-8176754fbe62 | -6.09218 | -59.96875 | 2025-08-14 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 168b37fb-6578-3ed3-b312-e993445e80d2 | -8.74257 | -44.04072 | 2025-08-14 00:50:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 37.8 |
| ce0eca7f-69e4-38f3-bc9f-a61a2e4fbf85 | -8.73432 | -44.02375 | 2025-08-14 00:50:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 81072f8b-97ac-398b-b99e-0b180f01c4ee | -6.5329 | -56.1998 | 2025-08-14 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 376a8e3d-881c-3f52-9146-6f0f32cde96c | -6.07766 | -59.93962 | 2025-08-14 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 191eff4f-e16b-366c-8e5f-9be4a362ef0e | -6.92168 | -59.16499 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| bef1efd9-a46e-3fbe-a9d4-6713e1c12fd3 | -6.94196 | -44.56688 | 2025-08-14 00:50:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 5ecdf911-49ec-37a4-8635-94a6247bf8a4 | -6.91428 | -59.17116 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| b9314378-3373-3b24-b9c2-d8002eec9d5a | -9.71347 | -49.48158 | 2025-08-14 00:50:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5065d0bf-2aa2-39f0-a18e-1bf3aed0436f | -9.77336 | -48.75691 | 2025-08-14 00:50:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 90b8b63c-076e-3bed-8c22-3638809a39dd | -8.52887 | -43.30061 | 2025-08-14 00:50:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 257cb72c-2539-3110-a621-16ae1935aa3d | -6.90834 | -59.12601 | 2025-08-14 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 925e51e6-8333-34b1-809c-f5de4d8cc8df | -22.302 | -49.5486 | 2025-08-14 01:00:00 | GOES-19 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.4 |
| ae49b096-2c1c-38db-b4ea-65213f5d85e6 | -8.5397 | -43.3277 | 2025-08-14 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 98d3fd2e-2cc6-33d6-8036-b5ed16c05cfc | -7.8775 | -61.8063 | 2025-08-14 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 35327768-d45f-3ef5-bf94-9560b7306c72 | -5.9899 | -44.1528 | 2025-08-14 01:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| cd9280e4-27e6-3bb8-a0b2-25888790d313 | -6.0807 | -59.9465 | 2025-08-14 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| c958999b-be2c-3a97-bbf2-7fc4d13d625e | -6.9422 | -44.5562 | 2025-08-14 01:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| d9cfd4ec-fba6-3316-96af-f2013b147c90 | -7.6103 | -63.516 | 2025-08-14 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 9c35c1e4-fcb9-3643-b3c4-2323a111437b | -6.0992 | -59.9267 | 2025-08-14 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 0e936aca-5f6b-36ce-80c5-0018ee7c28df | -6.0991 | -59.9459 | 2025-08-14 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 3153c77b-6a57-3828-820b-43b24518fb2b | -7.5918 | -63.5166 | 2025-08-14 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 21ac23d9-cf5c-3db5-97f4-bb3b68ea8ea4 | -9.1522 | -59.6578 | 2025-08-14 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| cf510b06-c7b9-3fdf-b5ba-a3d2093b1e19 | -7.8774 | -61.8253 | 2025-08-14 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 2aac124c-5949-3df6-bfe9-9d00b471ddd2 | -8.5211 | -43.3063 | 2025-08-14 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 083d6c61-2f77-3132-a3bb-05dc08d4c84b | -9.152 | -59.6772 | 2025-08-14 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| fda6e781-b371-3339-8cff-14d009d00ee7 | -8.5208 | -43.3298 | 2025-08-14 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 46b590f4-c480-38dd-9d05-f30e5b3f1d37 | -7.6287 | -63.5154 | 2025-08-14 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 59a2ff8e-ef5c-312a-ac65-3d935f344d26 | -12.575 | -46.9555 | 2025-08-14 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| b2fd6628-4abd-3c78-8c26-ea07fc9d19b3 | -6.0807 | -59.9465 | 2025-08-14 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| bf0762bf-7f7a-3291-8784-41d1abd9549b | -7.8774 | -61.8253 | 2025-08-14 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| a2a5b5dd-ec83-3837-a4ad-f6a4a9523017 | -6.8299 | -34.9362 | 2025-08-14 01:10:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 56.2 |
| 1c96bafd-b152-3455-9d79-0b405b164457 | -6.8296 | -34.9638 | 2025-08-14 01:10:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 63.8 |
| f5a10c75-c002-367e-a7d2-dfa7f38b8f15 | -7.5918 | -63.5166 | 2025-08-14 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 1dc11e3e-b426-3d99-a4c6-6f4a9a3f91f6 | -8.5211 | -43.3063 | 2025-08-14 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 13562fa9-e7e2-37b9-906b-2dff0b0c0ac1 | -7.6103 | -63.516 | 2025-08-14 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| f032e118-8473-3884-9384-709fb98b9349 | -6.0991 | -59.9459 | 2025-08-14 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 02074e34-1b1d-3096-a6fd-285b3ec35b35 | -9.1522 | -59.6578 | 2025-08-14 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 3d6365b4-50ad-3761-ae33-d14c8fcb858d | -9.152 | -59.6772 | 2025-08-14 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 715ee341-7644-30c8-a6a7-b1b2f004af53 | -7.6287 | -63.5154 | 2025-08-14 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 4c6eedfb-5540-3c1e-8f95-df7cbe33da7d | -8.5208 | -43.3298 | 2025-08-14 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 02932672-46dc-38ec-97a2-3a4ee0e7c7a5 | -20.618 | -55.481 | 2025-08-14 01:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 49.9 |


[Clique aqui para ver as próximas entradas](README6.md)
