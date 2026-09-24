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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa50f64d-4b60-3678-a4f1-98318d67f505 | -6.1361 | -59.9063 | 2026-09-24 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 401fcf69-2daa-34ea-95b2-617071690f24 | -9.0344 | -60.5129 | 2026-09-24 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ad48f490-793b-3ead-bcd2-85433887cb06 | -7.952 | -72.9322 | 2026-09-24 15:00:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 0a64ab69-983a-3521-ad7a-b99caaa24f57 | -12.8244 | -54.0649 | 2026-09-24 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 4558e4f5-1166-33ab-94b4-aa4167e78973 | -7.4092 | -44.7885 | 2026-09-24 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 250f3d8d-2c75-356e-a504-62f2a635b685 | -13.8154 | -51.834 | 2026-09-24 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| ea4069d1-632f-3cd4-ad7f-4b32332073eb | -11.9908 | -52.4485 | 2026-09-24 15:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| edb8b66a-a01a-368b-8385-f48bf893746a | -6.9871 | -47.4885 | 2026-09-24 15:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 95c32f6f-41b9-3445-9bd3-57c86c65fd43 | -3.9546 | -59.3377 | 2026-09-24 15:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 2e146246-121c-3fa0-88e2-7f23b641a787 | -9.1912 | -59.4231 | 2026-09-24 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 561973a8-e397-329e-9fe1-edb97080cf60 | -7.8213 | -44.9319 | 2026-09-24 15:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| a50f14d8-ad2b-341f-b5e4-aa0b2d9167b2 | -5.6567 | -60.2092 | 2026-09-24 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 0160d8a5-70e4-347c-bdae-453c59b40640 | -7.7441 | -46.7406 | 2026-09-24 15:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| f75a4576-c5a1-39e6-8f9f-b84e32abd122 | -7.4683 | -44.5539 | 2026-09-24 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 464b7a1d-2092-39bd-b2a7-621e556fbc07 | -7.81955 | -34.85812 | 2026-09-24 15:03:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 39313a8d-3491-3c1c-bca8-7c7c781606d2 | -9.34786 | -36.94942 | 2026-09-24 15:03:00 | NOAA-21 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 16e20888-3e46-3ecd-8d5d-ec37ef8c49f1 | -9.97439 | -36.13003 | 2026-09-24 15:03:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| fb685701-e1d1-3868-acef-c5f970275b06 | -7.82 | -34.85812 | 2026-09-24 15:03:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| 465a35fa-516d-3626-90cc-3149560868f7 | -9.34871 | -36.95673 | 2026-09-24 15:03:00 | NOAA-21 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 00af70f0-fcb0-302f-abbd-c22abdfdd2a3 | -9.35164 | -36.95299 | 2026-09-24 15:03:00 | NOAA-21 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 21.5 |
| b73623ec-c9d1-397d-bc0f-d1067e3ab5f1 | -7.3824 | -36.93741 | 2026-09-24 15:03:00 | NOAA-21 | SÃO JOSÉ DOS CORDEIROS | PARAÍBA | Brasil | 2514800 | 25 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 389efc32-1202-3b33-9301-b19c5373d596 | -9.97542 | -36.13032 | 2026-09-24 15:03:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| fcdfe9bd-3516-30ae-9857-ebeb7fffb5f1 | -7.5845 | -35.36396 | 2026-09-24 15:03:00 | NOAA-21 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 2ac11852-9a16-3ac2-ae3e-4aa5ac6b50d2 | -7.89561 | -36.12565 | 2026-09-24 15:03:00 | NOAA-21 | TAQUARITINGA DO NORTE | PERNAMBUCO | Brasil | 2615003 | 26 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 87ae9da1-af5f-3f18-8cf5-ffa225557f71 | -7.4092 | -44.7885 | 2026-09-24 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 73de8095-f4da-3554-9878-a727602b9020 | -9.1912 | -59.4231 | 2026-09-24 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| d92027d7-77d1-39c5-94fd-fe8ebb0668b3 | -5.6566 | -60.2284 | 2026-09-24 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| a7a9a8c7-a989-392c-a8a5-7d2027a5ea62 | -7.468 | -44.5768 | 2026-09-24 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 243731db-433a-30ec-99da-924a7721e2de | -1.8402 | -55.7034 | 2026-09-24 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| d95b99aa-42a3-381b-97be-3a8213b03a67 | -9.2021 | -60.466 | 2026-09-24 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 87d371df-066c-31ce-9625-77e7a16af82f | -6.1839 | -47.5039 | 2026-09-24 15:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| a5d96067-8a9f-36c1-a62c-f977634683ab | 1.261 | -50.8512 | 2026-09-24 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 79.7 |
| d07ffb8b-025b-30b4-8975-b733514ad380 | -3.4058 | -59.2347 | 2026-09-24 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 9ec7ec20-ea0e-3f06-a387-34fd27a2a9a3 | -12.7865 | -54.0482 | 2026-09-24 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 54fc2206-e275-3932-a958-1075bbf4a33e | -6.2573 | -47.6519 | 2026-09-24 15:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 52e81322-0d90-327a-a385-aef86020c3b7 | -11.9908 | -52.4485 | 2026-09-24 15:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| d5eb5b12-f9b1-38ec-a3dd-49f6b8f22ee9 | -3.4975 | -59.1752 | 2026-09-24 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| b1bd376d-1d44-3cec-b010-6a706d0e539f | -13.8154 | -51.834 | 2026-09-24 15:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 368fbfb9-9bf1-3ffd-b5ea-ea0fbfdec99e | -2.7713 | -57.0229 | 2026-09-24 15:10:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| a4ce23e3-8dd1-36e7-bba2-13fcd4d1f489 | -9.1392 | -58.9207 | 2026-09-24 15:10:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 317f703a-415a-3a71-814c-04c5b63bea1d | -6.0004 | -57.6884 | 2026-09-24 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| a3cac832-e74e-3e19-b536-16cc60e6a3d0 | -12.8246 | -54.0442 | 2026-09-24 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d0cf0a00-4235-31a4-b045-faccbdbfef72 | -14.08 | -52.1188 | 2026-09-24 15:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| d5c3f716-d2af-32df-9f6e-f3df8b1bd9ae | -7.952 | -72.9322 | 2026-09-24 15:10:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d4c820c3-fdf2-348b-89b2-1ec823e803c4 | -11.1372 | -54.0045 | 2026-09-24 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| cf29d8ef-f0b9-3f28-9605-e4c67a9055c5 | -6.2026 | -47.5026 | 2026-09-24 15:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| b251d24b-dc3e-374e-9586-3d60c91d132f | 2.145 | -50.8992 | 2026-09-24 15:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 5f8917be-b7e8-3b87-91f2-3d24f00e6136 | -9.1895 | -65.7863 | 2026-09-24 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 9ad68995-d62a-3bdd-9668-081ff257723b | -13.2225 | -51.717 | 2026-09-24 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| f76ff3be-be13-31bd-a5dd-105db3c18c88 | -11.7351 | -54.5636 | 2026-09-24 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 156fbbbf-579c-334a-8a3d-735771f9839f | -6.0462 | -53.2662 | 2026-09-24 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| f041c2f4-8770-39f4-8e2b-2be2e2b88742 | -6.9868 | -47.5104 | 2026-09-24 15:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| d7791f31-d8a3-3dbe-ae21-b5d010ab53dc | -9.0344 | -60.5129 | 2026-09-24 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 9c4bdb77-c7f9-3d52-a015-e0930641a825 | -9.1725 | -59.4241 | 2026-09-24 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 27d02c14-c23c-32ad-b506-a4dd3e514733 | -12.8056 | -54.0462 | 2026-09-24 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 1b70c26e-c4d7-34fc-aa93-f964abc4254d | -5.6567 | -60.2092 | 2026-09-24 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 03fab883-27b1-36c1-91a8-df9f28742e4f | -7.5337 | -45.4141 | 2026-09-24 15:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 0fd69cf5-0fec-3061-972b-eeec94eac8bd | -14.061 | -52.1 | 2026-09-24 15:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 35103f27-5fc5-3c97-9837-0baf4d13391c | -7.7441 | -46.7406 | 2026-09-24 15:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 6e6d18d7-f731-3fb2-b4fc-6bf9c2ffeacf | -10.8569 | -57.1568 | 2026-09-24 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| e90c4ec5-2df6-319a-afad-d59b8e43320e | -5.6016 | -60.1919 | 2026-09-24 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 236.1 |
| 4a777ab5-55b2-359f-91da-14a0a5cb67d9 | -6.2767 | -47.5631 | 2026-09-24 15:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 8aa487fc-e65d-3892-804e-21cf48bebbb4 | -6.1361 | -59.9063 | 2026-09-24 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| cce8ba42-cead-3617-a376-ad4def76ee3f | -6.136 | -59.9254 | 2026-09-24 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 8ee676b9-3b15-3a1f-a626-4aaae614dad9 | -6.2213 | -47.5013 | 2026-09-24 15:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 8a687ab8-bc65-3d9e-b684-4494822f2783 | -11.118 | -54.0268 | 2026-09-24 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 2825547a-c195-30be-8c78-84ddf3ff05e8 | -12.0096 | -52.4675 | 2026-09-24 15:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| de97f357-1104-3863-80d6-c2827cdaa6b2 | -12.12 | -50.67 | 2026-09-24 15:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d489887-edeb-3d94-bba4-a58e7785782a | -7.89 | -54.73 | 2026-09-24 15:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 338b4b96-ee99-38e8-869c-51bab54cfc79 | -7.92 | -54.74 | 2026-09-24 15:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b92bde38-2148-394f-8e07-0b87bab2093d | -12.12 | -50.73 | 2026-09-24 15:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6f82cfa7-83d6-32e4-acdc-f3865d38657e | -6.9414 | -42.907 | 2026-09-24 15:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| 1642e106-7135-38b2-af83-29c78bb4f9bd | -3.4975 | -59.1752 | 2026-09-24 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 8c74631f-9788-313a-98cf-1ca5b19d7424 | -1.8218 | -55.7234 | 2026-09-24 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 8eb7e013-6018-3aea-83d8-a2ce6a8829f4 | 2.145 | -50.8784 | 2026-09-24 15:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 489fbb18-a0e2-3207-853d-e1443a065cb9 | -14.061 | -52.1 | 2026-09-24 15:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 2bfb2ffc-2a25-3311-9f69-f41b39169201 | -6.2026 | -47.5026 | 2026-09-24 15:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| e0aa3ecf-7460-3904-aeb2-2461a8030173 | -6.0004 | -57.6884 | 2026-09-24 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 61006934-2731-3ff9-abcc-f858b09d994c | -6.2765 | -47.585 | 2026-09-24 15:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 741acd5c-3ac0-3270-adac-24757a99e7e1 | -8.6757 | -69.9611 | 2026-09-24 15:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 7bf7e293-8c14-3cec-bd3a-300064001cc9 | -13.2225 | -51.717 | 2026-09-24 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| d3accddc-e2a0-30cb-81c0-84531d2c0c96 | -6.5444 | -44.9327 | 2026-09-24 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 5c0a29f4-66d8-3936-a3a3-2c5be5b7f549 | -12.0096 | -52.4675 | 2026-09-24 15:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 9307d32d-490b-3a27-9d10-7057f8c7a913 | -5.6567 | -60.2092 | 2026-09-24 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 9bb09b8b-a8e4-30d6-b532-bdc2c30ae0d2 | -2.7713 | -57.0229 | 2026-09-24 15:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 8ae38635-4ca3-344a-88b2-e23cdad47b16 | -9.1912 | -59.4231 | 2026-09-24 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 0c38c8b6-bb6f-3e4c-be34-8d7ac8fe6c69 | -1.8218 | -55.7037 | 2026-09-24 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 3c14b33a-ef30-3d50-9aaa-de06d5a9c1bb | -4.4488 | -55.0662 | 2026-09-24 15:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| d696bc44-0d7c-3def-9118-0d4cadd4e060 | -12.8056 | -54.0462 | 2026-09-24 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| d6bd5018-eb6a-36e6-a373-ea96d879ecad | -3.4059 | -59.2155 | 2026-09-24 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| ad9552e0-2958-3d5d-91c3-05d0cdc54706 | -7.952 | -72.9322 | 2026-09-24 15:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 01ca6c17-34b9-3121-a3ae-b4dc5b43810b | -14.08 | -52.1188 | 2026-09-24 15:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 4af31260-b639-38ab-973e-85d90e4f4d6a | -7.9519 | -72.9504 | 2026-09-24 15:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 252536ae-679f-30e2-84d3-8e1f6e74e3d0 | -9.1392 | -58.9207 | 2026-09-24 15:20:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| df6754e0-b1ab-3566-a280-245c24110183 | -14.0425 | -52.06 | 2026-09-24 15:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| d268e669-b5de-3ed3-b2ea-ab10d0b1a389 | -12.8246 | -54.0442 | 2026-09-24 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 09dcdbe2-0dc1-3dbb-94a1-b8f79d78d112 | -5.9818 | -57.7087 | 2026-09-24 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| c0ae2026-0fcc-3e96-a9b9-e7f3c0107d3f | -10.8569 | -57.1568 | 2026-09-24 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 74c5629a-0d4a-3b33-b59e-6786f2e1ae08 | -3.4058 | -59.2347 | 2026-09-24 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| b64613a3-ef63-327f-a446-04af6ae4275e | -9.9266 | -60.7171 | 2026-09-24 15:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |


[Clique aqui para ver as próximas entradas](README98.md)
