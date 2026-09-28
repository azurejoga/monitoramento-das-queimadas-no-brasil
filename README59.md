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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 803af735-f3d9-349e-a93d-1978895e7ff8 | -20.17779 | -48.58906 | 2026-09-28 05:14:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 90965b97-59a0-3beb-97c5-00f2c9d7b706 | -17.6826 | -47.98497 | 2026-09-28 05:14:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c971e4af-0cc6-344d-a873-9dd338a9c686 | -21.52616 | -45.11012 | 2026-09-28 05:14:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9829cd12-505c-3af9-9fd0-71b60c52a217 | -21.51924 | -45.11518 | 2026-09-28 05:14:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e9589df0-d086-3f5d-9cc6-7f66b20a22e0 | -18.09602 | -44.38174 | 2026-09-28 05:14:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4702af2d-970a-3bd9-b1a8-c539e63bc5d2 | -20.34999 | -46.38819 | 2026-09-28 05:14:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05cd6e8e-a3bc-3ab6-ba71-84a2d2f54700 | -17.68733 | -47.98912 | 2026-09-28 05:14:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69c479ab-610d-30b4-b58d-e92745cddb26 | -17.683 | -47.98159 | 2026-09-28 05:14:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57f4a09f-42eb-3339-ad0d-afdc504dfe8e | -18.09652 | -44.37628 | 2026-09-28 05:14:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7849176c-7efa-3adc-a2a7-22d0e9557cc2 | -19.14732 | -43.8241 | 2026-09-28 05:14:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46ce78a5-c096-371e-a07b-fbf1363187eb | -21.5197 | -45.10975 | 2026-09-28 05:14:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6b5eea54-c9f3-37a5-9e81-8bb96f656a8e | -20.17269 | -48.58842 | 2026-09-28 05:14:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 471bf400-c27d-3c93-887c-8bdb4c70d304 | -18.10256 | -44.38189 | 2026-09-28 05:14:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d8011f0e-6203-34dd-b19b-281f090c7362 | -18.11613 | -44.37689 | 2026-09-28 05:14:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 20029c6f-b142-386c-8dfa-f495c192fcc3 | -19.15466 | -43.83245 | 2026-09-28 05:14:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 130f8b16-419f-370f-94a0-3d8cafcdb149 | -20.18356 | -48.58343 | 2026-09-28 05:14:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9a1c613-f17f-3766-95fc-f422dc19de34 | -20.1999 | -48.5759 | 2026-09-28 05:14:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 644c2793-ff0b-36c7-93ea-986d6cee8659 | -17.68439 | -47.98135 | 2026-09-28 05:14:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52ef8260-baf4-3de3-981f-d81430a29c76 | -18.11562 | -44.38238 | 2026-09-28 05:14:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7a1067fb-06ed-3e4e-b995-24f2107febb4 | -18.10308 | -44.3763 | 2026-09-28 05:14:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a766828-44c2-3276-bbf4-610ac6cfa6db | -20.19957 | -48.57903 | 2026-09-28 05:14:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4ca3bd48-9485-3078-95b8-62866ff9b0d0 | -18.10909 | -44.3821 | 2026-09-28 05:14:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ddbd5b3-6e08-3af0-92dc-4858182c1a35 | -18.74787 | -53.28426 | 2026-09-28 05:14:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a0dca1c-4327-36c9-b070-1405f0c227b9 | -19.14795 | -43.83108 | 2026-09-28 05:14:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da08f854-9000-3674-8e48-a6a233071919 | -20.19478 | -48.5753 | 2026-09-28 05:14:00 | NPP-375D | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44c5f5e3-00a6-3d50-b34c-e8f0eaecac14 | -21.17247 | -55.75252 | 2026-09-28 05:14:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc68f846-44ae-3b7e-8f93-af35673c75fd | -16.46475 | -55.07417 | 2026-09-28 05:14:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 766935d4-3f7a-3576-8b86-dc3e377a4e36 | -20.83858 | -57.69767 | 2026-09-28 05:14:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c29d0ec9-e48f-37b6-8223-6fb404a7647e | -11.16 | -44.8 | 2026-09-28 05:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 18be83ca-709a-3025-91cd-4787a8ea77bb | -11.19 | -44.8 | 2026-09-28 05:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03a8e56b-aa35-3905-8a02-3cdffb00b16f | -28.75492 | -55.60288 | 2026-09-28 05:16:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 3c5a90b1-63ff-346e-ac5d-38d648a39840 | 4.34414 | -60.7104 | 2026-09-28 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dcbf8824-ab7d-3251-a57a-d0b4ca9ea078 | 4.30931 | -60.81822 | 2026-09-28 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7c986453-53dc-317c-a8ea-f23201b0f9eb | 4.65536 | -60.64009 | 2026-09-28 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05a1211d-b2c0-30f3-9e5d-5789be7d3e53 | 4.65886 | -60.6397 | 2026-09-28 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fd8508c-ed9e-3ce4-9125-4a123e1087fc | 4.31279 | -60.81757 | 2026-09-28 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b30baf0-b05c-3605-89a3-bc872b9fa106 | 4.30991 | -60.82206 | 2026-09-28 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| edc1e196-c477-3990-9ee5-2c51b0c1e640 | -2.78781 | -57.69351 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f34876c9-dcc6-3612-9165-7133a4de0bd9 | -2.76887 | -49.47809 | 2026-09-28 05:27:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19124544-a90b-356c-aeea-d96648bc5410 | -3.23566 | -50.57938 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bf75c834-bc6e-3894-93f6-9685344d1a6d | -2.7861 | -57.69065 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5058cad4-bd53-33c2-a410-e3c70536931d | -2.94302 | -57.71332 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 161d51ef-403c-37f0-8912-3b0e8c55aa12 | -3.14827 | -54.07634 | 2026-09-28 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efb73b4e-aa80-369b-9de9-ec3242e43270 | -1.81134 | -57.10439 | 2026-09-28 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d739a7b-128a-38c7-84a7-b33f8367fb0a | -3.01147 | -54.21111 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 839d7f5e-b6a4-3d36-9cf6-c57624fa37a2 | 0.28376 | -50.91169 | 2026-09-28 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d615e7d-747e-3396-89d4-3e6adf786630 | -1.75319 | -55.65145 | 2026-09-28 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed4ef5c7-9040-35d1-92cf-ff16bc91d1da | -2.55269 | -57.40892 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ce79b3e-132a-3569-bf5a-a599860a221f | -2.78435 | -57.69297 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cee2092-22e0-33f0-8c0d-5d315d7b23c8 | -2.11695 | -56.88595 | 2026-09-28 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4e4cfd3-5494-33f3-88ed-7d6caae2ea9c | -3.42104 | -48.33493 | 2026-09-28 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| dec60a4b-b2ee-378f-a61c-877373cd2a7d | -3.20664 | -51.04127 | 2026-09-28 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 918d15c5-eaee-357f-b45e-0496f203a9ac | 1.66513 | -55.91882 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b574a7b-7326-3760-817e-829d8a396504 | -2.90933 | -54.20006 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76dadcea-94f5-3b55-90f9-67c593bb519f | -2.7843 | -57.70202 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cca55c5b-c21f-39d0-a0ab-148621d227fe | -1.7588 | -55.12654 | 2026-09-28 05:27:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4b62e4e3-fa21-3927-a760-1122a1fe57a6 | 1.24728 | -51.13008 | 2026-09-28 05:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a63989e2-df1e-3143-bf04-91b722a91198 | -3.68285 | -47.49484 | 2026-09-28 05:27:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 36b6c184-2567-383d-9fcf-3a62e5bb9925 | -2.91356 | -54.20069 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd45440b-b930-398a-9efb-a16de730dd14 | -3.51136 | -50.31988 | 2026-09-28 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab8e1d54-f47d-386f-8759-75d165c80dc4 | 1.65797 | -55.91995 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8874f51c-ae4a-39d3-b0af-7ec9177e1f68 | 1.57767 | -50.91224 | 2026-09-28 05:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51683069-ce08-3041-b5dd-265a03f27b73 | -1.76702 | -53.76075 | 2026-09-28 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2661bc28-e83e-31fc-9aad-e7f77ef3cfc4 | 1.67129 | -55.93451 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff2a8e6f-2b4b-3fc1-ae82-7cae15353998 | -3.19125 | -51.03569 | 2026-09-28 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac92edba-b2b3-36e9-82b6-34507607d4f3 | -2.86527 | -57.78669 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 311bdcd6-8c9f-316a-a851-452aca63ab7b | -3.19655 | -51.03641 | 2026-09-28 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c70c4a2b-723c-34ec-b4d7-c2ad09ad0fba | -1.04808 | -53.5634 | 2026-09-28 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb448b6c-00fe-3c46-90eb-7848845889d2 | -2.65672 | -51.737 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d1c0072-d415-3aa7-b4d8-f6f216265373 | -2.53016 | -57.22986 | 2026-09-28 05:27:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4dc223b4-e559-3b03-b521-216844a54beb | -2.54498 | -57.54934 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 094cb216-4543-3005-ab0a-c09cdae8ccea | -2.06122 | -56.86911 | 2026-09-28 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14fbbd70-759e-3f7f-9468-7eedc47f2a85 | -4.31072 | -50.40388 | 2026-09-28 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87ad15b6-9ab1-3c81-be5d-75759d99e7c7 | 1.67065 | -55.93046 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d5316c8-9ef0-33f1-bce3-9af84ed796a1 | -2.52958 | -57.23032 | 2026-09-28 05:27:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6512a258-8325-379a-a3a2-580fe1628cc9 | -2.05409 | -56.86803 | 2026-09-28 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 73057835-081e-379c-aad1-9ada149a375e | -1.8249 | -55.31953 | 2026-09-28 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9109cddc-53f6-3b82-971a-382fb710c078 | -3.41959 | -48.34467 | 2026-09-28 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 6e192b02-d34f-38e7-abb3-a0aba2f8e73a | -2.73171 | -54.20266 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6503ab61-2ab7-3e5a-9756-f61fe69e2174 | -2.94669 | -57.80289 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94556c32-5220-35f1-a90f-d8f0fc1cf85b | 0.28834 | -50.90799 | 2026-09-28 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3909dc82-aae6-3535-9999-5ea1850c889d | -1.74147 | -57.17885 | 2026-09-28 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48730ff9-da9d-3cad-a61e-67ae131b715e | 1.67 | -55.92639 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef354a42-3f54-374f-9594-bd37b66cfb52 | 1.66578 | -55.92289 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3529cb56-5bf7-3ff7-9eaf-b15bb61089d5 | -1.77432 | -53.77003 | 2026-09-28 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ff6c7278-308f-3a1e-980f-246bf770f87d | 1.58262 | -50.91146 | 2026-09-28 05:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c7c103d-9095-3b04-bb61-b7fee08e4f8e | -2.91207 | -54.124 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae68c457-e594-36ef-bd8d-672c4c85c45d | -2.76948 | -49.47396 | 2026-09-28 05:27:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4005b49-1d51-3080-9006-4b93a33948ae | -2.66682 | -56.45856 | 2026-09-28 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ceeb3b9c-ac19-37ca-a5e3-aae8497074fd | -3.20761 | -51.03481 | 2026-09-28 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 803aff66-ed61-321c-bda4-9531495a2408 | -3.14706 | -54.08441 | 2026-09-28 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4d46b89-ae53-384b-8336-194e30ee2917 | -1.77131 | -53.76136 | 2026-09-28 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f4aafd4a-1805-3418-b93f-552763d4874f | -2.94955 | -57.80719 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fc9ffe3-3b8d-3fc1-a4a3-d3433d240660 | -2.02782 | -56.78633 | 2026-09-28 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 30bcb974-8762-3fe9-9ebb-abf4ece2cb7f | -3.36048 | -50.46574 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2524452-24e0-3fe9-abf5-2bdb00b63e0a | -2.54075 | -56.42899 | 2026-09-28 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 710fdf79-6f63-3887-91ad-c183e975a8df | 1.67616 | -55.94205 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 555aed1d-f15f-3281-9993-75726bf19e7a | -3.20231 | -51.03405 | 2026-09-28 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 265d0374-9df8-38bd-972d-950ea7563b20 | -4.31489 | -50.39986 | 2026-09-28 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f3cb4f8a-83c0-318b-b192-54797ab7d6fa | -2.02425 | -56.78574 | 2026-09-28 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README60.md)
