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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56bf7b98-4a73-345c-ab5e-3c7103931967 | -9.54177 | -62.39613 | 2025-08-29 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d72684d0-2679-3b43-a79a-e87080337fe0 | -9.15942 | -60.92477 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a743a35b-339f-35a8-bd21-51cb3e831070 | -9.66822 | -65.02844 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 435604f8-926f-3c67-90f5-8b31772d9b17 | -9.12471 | -65.77856 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ba7d3d3-1af4-3640-8444-9af5e9c38ac6 | -9.45253 | -63.09341 | 2025-08-29 05:29:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8c2af5c-e19c-3574-8f8f-5efc570173d7 | -9.80084 | -67.84217 | 2025-08-29 05:29:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c2d55f0a-b49d-3f31-8b07-fc65dfa0c244 | -10.4553 | -57.94398 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 578ab804-d16c-39c5-a915-5e79a4ac45b4 | -8.18919 | -61.38128 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 329f65b0-f9d8-37b2-9baf-c42fa0ebe11e | -9.20643 | -59.54034 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d702cbcd-494a-3a7e-a094-bf51337655a7 | -8.88961 | -60.74223 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e208c363-46f3-31a7-8cea-ecbe76db9df3 | -6.89501 | -64.24299 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d570b0a-0cf6-396f-9747-a0764fb60d0c | -9.15752 | -65.77985 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 08280f4e-c584-36b1-b445-e8905e047534 | -9.78511 | -64.24428 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aecd930f-19e3-37a9-beb1-5b3b4db6b720 | -12.4375 | -63.91225 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e35f584b-e029-3cb4-b1b0-ea3530b51ae6 | -8.18303 | -61.37667 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f71cc542-c704-3d93-8d70-61cc32923512 | -9.10754 | -65.77139 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 752935f8-48f5-3b9e-bf11-ccea02593287 | -10.36844 | -57.82726 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2c2a0652-8264-328d-9d7a-cb9db841ddc0 | -10.38019 | -57.82817 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 41e2114e-f3f9-30ad-9a2a-556473032a0a | -13.02437 | -56.92019 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf570961-9c2d-3229-bdc2-5038cc69f84b | -13.01594 | -56.91446 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f11253dc-c83f-3730-ac12-0e0468565e3f | -9.00684 | -65.72227 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b2a2e14-b6a7-366f-b316-8a1de5f3fd9e | -9.20217 | -59.54401 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e8f2c98-1916-3b2b-8f6d-9b582751cd69 | -12.43363 | -63.91524 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f0eea66-78fd-3a3d-b09a-faaa8c0208e6 | -7.62355 | -60.84838 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d32f1c48-bf72-3418-8c2d-f6065e491930 | -9.13951 | -60.77979 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47bc73f7-ab68-31dd-a177-f09e8bbb312d | -10.45218 | -57.96572 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18a1a837-194c-329d-baed-9dc8cb216866 | -9.12781 | -65.80437 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5017171b-d6f7-32a2-80f8-70ab0551e2e6 | -9.73028 | -64.90685 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9b079a83-b53a-36c7-b331-637ea9215148 | -12.93301 | -56.97154 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 50347655-ed48-38e9-8e9d-9f578411dbf2 | -9.78453 | -64.24788 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4e4d7ec6-c881-3928-a2f7-a8a9aa5a5751 | -9.10446 | -65.74564 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a65ca6dc-4c3e-3944-b47c-ec1d4f41c655 | -9.45813 | -65.42676 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3440075d-ebc6-30b5-8789-7219e2b02af7 | -8.5669 | -70.06335 | 2025-08-29 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15cbb440-4f72-3761-a84a-ff7b72bf7113 | -9.45553 | -60.56071 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 80765782-3f2f-3e05-b0ff-3475353f5ac1 | -11.22444 | -55.05817 | 2025-08-29 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fcd07059-6ae9-32aa-ac9f-79fb0afc966a | -9.06942 | -60.40987 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e44684b-3e32-3921-91e5-623b1114afaa | -9.41593 | -60.57483 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5de836a7-9b86-3bcd-8c17-05a65e4a2fc4 | -9.12819 | -65.29057 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e7b76ba-0fb0-31f1-95ff-99b958066fde | -9.46386 | -60.30683 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57809b80-bcab-3b7e-9412-2fd13cf121b2 | -7.53978 | -63.85695 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 306afd77-dbbf-357e-a19c-c3729d5ecdc5 | -8.95901 | -65.94402 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e3d370d-154c-3718-bfd6-d42db613bcd4 | -9.09156 | -65.73507 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b21788c9-1675-3fb2-84f3-18f934ad6a3d | -11.08936 | -65.15495 | 2025-08-29 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a09d6e7-c47f-3bd2-b738-b44bf6fde9d8 | -8.66861 | -62.44321 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 692b01ad-898b-3f00-9e37-bd799e9c0441 | -8.9519 | -65.96443 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4d86a17-f6a3-373a-8135-d39fd1ed060b | -9.11911 | -65.79022 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 431795ad-bcb1-30ff-ada1-2dd81b085b9e | -10.46879 | -57.93849 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d129caa-ca68-3e8b-9c18-9f944b08e213 | -9.79993 | -67.84739 | 2025-08-29 05:29:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fbe2a691-0dc3-3865-a18f-11d7c0209c61 | -10.48161 | -57.96563 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64ef5796-4caa-3933-b813-42f041124e48 | -12.4397 | -63.91986 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a0fc19cc-59bb-34fb-a337-3f6f555b7f41 | -9.21649 | -60.87215 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70b3a052-76df-3096-9db3-10d74dfc79e7 | -9.65188 | -64.95575 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce9a314f-ad57-3101-b558-ce4a100f132d | -9.11486 | -65.79375 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f36cf044-1d65-3027-ac5d-65e530205eb7 | -7.54664 | -63.83587 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ac729fc-feca-3feb-a767-7ba063866172 | -8.94517 | -67.71442 | 2025-08-29 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1abc2c24-576d-33dd-bbc7-bee061ad4712 | -9.15255 | -59.57249 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6626ee41-8196-3af5-8ac7-e6fa65e4c7fc | -7.56336 | -63.86077 | 2025-08-29 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c414e6b9-be90-3ea2-8d13-725af336c4be | -9.52749 | -60.50829 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0987f49b-9326-3533-a963-ff932d17b42d | -7.78781 | -61.32317 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aea7751a-ba58-335e-9c76-2ffcc184d75e | -8.69127 | -62.47177 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db6a812b-877b-342a-a5bc-8e40490f1c5a | -10.45778 | -57.95554 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b783cb3-914b-3b88-a4b1-2568a8236147 | -14.26653 | -53.22796 | 2025-08-29 05:29:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 07a09052-ffcd-30a7-8c35-6572e7dd20db | -9.46597 | -60.56225 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffffc7d6-1390-3a17-b990-5fafa9a8edbb | -10.36648 | -57.81185 | 2025-08-29 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 25313a15-4f9e-3d1f-9558-3e4a87bbeed7 | -8.09814 | -71.24956 | 2025-08-29 05:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22b8f36e-8bf6-38e6-b19f-af08788f18bc | -10.07518 | -62.89248 | 2025-08-29 05:29:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1b69590-593d-3585-bacb-637ea45c1ea7 | -9.17927 | -65.79485 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3eb4a110-ee8f-32f9-9966-e08276faa2e5 | -8.24623 | -61.44887 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9223936e-29dd-3c92-a9b2-2eaa59b6d9d6 | -11.2252 | -55.05225 | 2025-08-29 05:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 380303fc-0a21-3854-83d1-7ef33540fb3f | -7.4225 | -70.1577 | 2025-08-29 05:29:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1af6495-12c5-354a-abd8-8a083eec747d | -9.45463 | -65.4262 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55a6f134-f77c-3446-927e-91eb45648e05 | -12.63449 | -60.24207 | 2025-08-29 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df16226d-ae3b-3dc9-a371-191e5cf84668 | -10.53625 | -64.37 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 28cb9718-e7d3-3092-9335-cdc9898f2a91 | -9.15328 | -65.78335 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8ecb0249-674b-3983-a835-0b530a56a1b0 | -10.29247 | -64.48997 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46ede796-f30e-3e6c-8b8d-c5b9ac4d3917 | -10.08552 | -68.46454 | 2025-08-29 05:29:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7952d264-33a8-3721-a637-06dcca3b8da2 | -9.15685 | -65.78396 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9ae975f1-122c-382a-a507-6f27d6346bb3 | -9.45668 | -60.55303 | 2025-08-29 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| e01f684a-979e-363e-9b19-c90d1fe35cb7 | -9.88428 | -64.69447 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96284d7e-1411-3b01-a4f1-329b8418adba | -9.77606 | -64.2576 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 75f58244-ebbe-38bf-983c-740b83e58c0d | -8.9045 | -60.75987 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6eaf4fe0-3ef6-31e6-a29d-7bfafbcd078f | -10.8625 | -60.81273 | 2025-08-29 05:29:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 106623e4-dd27-37f9-823e-1fce2712fc0f | -8.18359 | -61.3731 | 2025-08-29 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 46bf8fbd-a2eb-3ce3-bbc9-34c51690b46e | -8.24568 | -61.45245 | 2025-08-29 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 489db0e2-abc5-331c-b32b-a7c40a91df1e | -8.64971 | -69.57056 | 2025-08-29 05:29:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81c4fcf7-ef35-3ab7-af7d-6c4146d53faf | -13.01022 | -56.92315 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc9bd08d-d991-38f4-a1f3-0a6bb2192172 | -12.92792 | -56.97541 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 891a86fb-50e4-39c6-9492-a9e063543651 | -10.17668 | -68.15587 | 2025-08-29 05:29:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5270329-f2ba-3e26-a6ac-6885d8f43f2b | -7.99079 | -70.28487 | 2025-08-29 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e3aa354-00a4-3743-adec-010d52756074 | -11.9257 | -63.94772 | 2025-08-29 05:29:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ff632b4-b720-350a-a0d9-ca7ab0805aff | -9.66416 | -65.03168 | 2025-08-29 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 828dcb3d-582c-3f91-bd4b-fd99ecda7297 | -8.96122 | -65.95303 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 079d2e36-f86b-3652-9e60-72c390f0b5ff | -10.45831 | -57.95187 | 2025-08-29 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be00f1ae-f2e5-336d-979c-0c7f226fb425 | -9.1621 | -65.78773 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32c75dca-4d3b-3142-a573-d9bf01e7647a | -9.16087 | -59.5727 | 2025-08-29 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 524eae20-fe46-37cc-90c8-c83949f85de3 | -9.16636 | -65.78424 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a18d419d-2f2b-3004-96d1-36626af4570f | -8.8056 | -69.30191 | 2025-08-29 05:29:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41fcd157-ee1c-3e34-85bb-f5ea1f6e0419 | -11.72768 | -61.75649 | 2025-08-29 05:29:00 | NOAA-20 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 75954e6a-a32a-3f8e-9404-2ad984e7b3b3 | -13.01082 | -56.91851 | 2025-08-29 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6682d944-a69b-3626-8d5e-17e7a2297122 | -9.13649 | -65.29073 | 2025-08-29 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README80.md)
