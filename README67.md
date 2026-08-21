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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7320e81-3887-3134-a14e-0b62b028a775 | -6.82622 | -59.41039 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b37d71b3-cd1f-3479-9145-c8ccf412985c | -4.44964 | -55.39269 | 2026-08-21 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0c7abc2-5c0e-3465-b864-ec19386a201c | -8.15853 | -46.73398 | 2026-08-21 05:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2e819fd-1efe-34a2-a53a-e976ca33cebd | -8.54522 | -55.30886 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0864f0f7-c5b6-3a34-a370-b92c6258b25d | -12.51645 | -54.76198 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91b3757b-f003-3334-abb9-e71697428303 | -14.32071 | -51.91011 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1518bc5-e579-3b67-add9-fe0e44067584 | -8.55029 | -54.77429 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0355f3c4-5034-3b1a-8114-e2c409eff3d0 | -4.92081 | -56.25873 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1d6451b-c168-3960-a189-98b22c5c4aa1 | -5.13773 | -56.27841 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d115572-0419-37ce-b73d-37bbd89ddf26 | -6.85776 | -59.02176 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fa30969-c632-3033-83b8-a9f559f1fd6c | -4.46949 | -55.39949 | 2026-08-21 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 938d3a02-d742-3f24-9818-8c555c6766d6 | -14.45563 | -45.61865 | 2026-08-21 05:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 052cf37f-3b24-3ef3-8ba8-9caef55bdbf2 | -14.31729 | -51.89918 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 96381d5e-e065-3618-82d5-52c225f16d84 | -13.43263 | -51.80261 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd90cb1f-42cb-3ce2-b9f0-b96e0f2f392a | -6.86607 | -59.42442 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfecc1c2-b001-3270-b453-fae010122f66 | -9.22009 | -59.77878 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce43fb8e-1a94-361e-afc9-760e47cde65b | -8.5836 | -54.77509 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8858414a-2624-3020-9a00-36f82582edf5 | -10.72645 | -44.78358 | 2026-08-21 05:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7f13c346-f601-3227-bf05-91b92812a51f | -9.21448 | -59.77029 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 250e6b4a-3830-3ae1-964d-26a2616b9483 | -8.4985 | -54.87368 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93d36b98-2d89-3f30-998f-a085975ee1b7 | -15.71846 | -47.79163 | 2026-08-21 05:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4701923b-3ad8-3c0b-b95e-c433c4d0203d | -4.05045 | -50.29591 | 2026-08-21 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04647541-fe1a-3539-8a9f-d46e828e577c | -8.58378 | -54.74925 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0417f18-f698-3ed2-b126-a1661677d063 | -13.41155 | -54.36451 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55ea4e65-1e7b-3baf-a1e4-5cb574d4f494 | -7.60653 | -60.94898 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54266f9e-596f-3712-b8e8-2d0cb281987c | -6.55109 | -56.2613 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8957884e-56dd-32b7-bed1-0694737f5d7e | -9.44619 | -51.63525 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e01e976-7037-34eb-be33-0d3d9af16245 | -8.89265 | -60.5478 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 86d237e9-e6ae-34ca-9c0a-1c10d5a34d39 | -16.73405 | -49.36646 | 2026-08-21 05:23:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06512f32-a529-3295-ba34-f361905606c1 | -6.1173 | -59.92182 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4edb6f7a-2c42-36db-827d-be6026d1972d | -6.86547 | -59.42812 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7e5d71a-26fd-3c95-bf6b-0fa60a7438e5 | -6.86394 | -59.02649 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 333ea02a-5a7e-341e-9900-c90853ea5691 | -7.88641 | -61.71095 | 2026-08-21 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e98a049-1dff-3d47-bab5-79d0a49ac398 | -12.52094 | -54.75779 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab30359e-467d-335d-a3fc-8553f2c109b0 | -14.24455 | -52.13885 | 2026-08-21 05:23:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41e98fd4-1f2a-3519-9c0b-986670af0b0c | -9.21874 | -59.65814 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 639b1161-7919-3f2a-9f82-a926909aff63 | -6.22985 | -55.41496 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 929443fd-218f-3be0-9c40-b80e06e8c97e | -6.81275 | -58.99966 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44e23da2-79ba-35d0-a971-c6e82a957733 | -9.15533 | -59.66264 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04d25491-f338-358c-a630-277ec30cd0bc | -9.20887 | -59.76184 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db092d8f-0703-30a9-b280-019d4641fdf2 | -6.86674 | -59.03065 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| abd857a6-3775-3d0c-ac11-acf8f8a73b1d | -6.8942 | -55.71972 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89dc3c8d-cfe5-3597-a8a2-229af455495b | -6.8753 | -59.41076 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f37720e-a6bb-3a01-bd0a-0e888853174b | -6.38643 | -54.94252 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 113a56cb-6d9e-37ce-a666-3539dc4d3ea6 | -6.80365 | -59.01301 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94424775-b75a-3e96-9ecc-4db1e9938b7c | -14.45314 | -53.06299 | 2026-08-21 05:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1ff3f38-a703-33d7-a0fc-3a324115d138 | -6.87009 | -59.42128 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 118d065f-c2d5-34b8-a4cb-bb60c0952c9b | -6.24962 | -55.41718 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64f91297-ac11-3ab8-8c76-c14e7d390d94 | -4.93727 | -55.78162 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60add24b-702d-3e7f-b752-346af76eb0ab | -14.00861 | -53.67806 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57bbd630-e604-3066-b73d-8f6a33b87093 | -8.03379 | -54.02398 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e7c05308-7a81-3c87-b5af-a157993859e9 | -5.82348 | -55.71676 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1316f1c9-0839-3d5a-a892-66b411d396eb | -6.01283 | -57.80089 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f61cc99e-a954-39ed-8f76-546da53f7a04 | -6.01559 | -57.82626 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b90bb0b-dfba-38d5-99d4-b99be1d6a310 | -7.01086 | -59.54218 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9691b7db-654d-387e-b12d-97f9fb29b102 | -6.65428 | -56.34636 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e083035-0c29-35d4-bd97-f593b3dad6f4 | -7.34921 | -55.68836 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d8d0cb9-e00c-3ab9-8333-f7c8af65ae06 | -6.42346 | -54.93612 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e85f7f4d-5e72-3741-8488-4bfe17acc3e7 | -6.92017 | -59.34986 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7bd9232-f151-3024-93c4-f7f2cd5b76c8 | -7.54922 | -55.56315 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1accdc5-c37a-3c26-9be4-7e0b1451ca4d | -13.39952 | -54.3763 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 6987f554-1e05-3769-9434-547156fb1a3f | -6.97301 | -59.58671 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c20c1d45-b7ce-39e9-b587-eec8356cefcf | -6.42054 | -54.93166 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 746f2b10-2862-3ca7-9cfc-a4660d1a69b6 | -9.21137 | -59.66066 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17c82d38-6836-3039-afe6-4b5dba7abc8e | -6.92417 | -59.34674 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46ac1d5a-97b5-3056-8712-a519c212afd3 | -6.11478 | -57.69258 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce26df9b-be08-3b04-9dfa-b468edac35af | -6.25077 | -55.40962 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bbd2c1c-45da-34e0-a6e2-da02b2750ea0 | -6.9264 | -59.35464 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f35707c3-98fb-3c2e-aa24-b8be09df9403 | -6.20741 | -57.76821 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e9bb33a-7121-3ad4-9e3c-210c1f0455e4 | -6.97644 | -59.58727 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2880f95-464f-34d3-aa46-4298058f5c82 | -6.89192 | -55.71171 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28499c4d-7ca7-305b-80f4-25c63e132553 | -6.70175 | -59.10083 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d3b6f71-5733-38f9-b49e-9d294da8db16 | -7.35407 | -45.8117 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e7d0d775-f525-3f93-8fa8-c92a11b06e14 | -5.49521 | -60.13208 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cdd12e5-ab45-3fb8-a51b-4eaa1a6234f6 | -14.3469 | -51.89291 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3849cbc7-2181-303b-ae45-1d14690bfcd9 | -7.59928 | -60.94781 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c1d6739-6706-3d1f-8d28-529949041bd3 | -6.2539 | -48.6545 | 2026-08-21 05:23:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| eb144288-e9a7-3350-962a-e2e808aad432 | -4.8863 | -56.28212 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bbed05d-8996-3280-a324-171077a2b7aa | -14.57389 | -52.99317 | 2026-08-21 05:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac861681-f7c2-3fd2-b7f5-31dd8b6d9c6b | -7.10338 | -59.76905 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f716cc30-df7f-3936-8029-b7c614dae8da | -6.91334 | -59.34876 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35452788-4a30-3489-a5dd-1fcb3c32e842 | -9.21329 | -59.77766 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c4cff07-fe0e-373b-9957-6a38df151f69 | -13.41132 | -54.39592 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c921ccd-19e3-3b71-ac27-bc008d11804f | -9.45038 | -51.60518 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a6139e7b-003e-32bb-937f-9b0af8ee25e0 | -6.20044 | -55.49072 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94d5257a-11fa-3ebf-b62d-8f836abe6903 | -8.54048 | -55.31633 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e401cdb2-e70a-31b6-8d63-9d3abaf7b718 | -14.316 | -51.90939 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff54dcc6-39d1-30a7-83b8-7a9c53182be6 | -6.72385 | -59.09327 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcabed92-da39-3790-bd1e-92ca50aa253c | -6.57666 | -58.96956 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24e1f78c-057b-3e08-8826-85904beaa105 | -8.49243 | -54.88206 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4428517-4b2a-3179-b13f-077230d89009 | -6.87291 | -59.42556 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a273d2b1-23bd-3593-aaf9-f8e6f00b2839 | -6.89913 | -58.98413 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 32521c6a-fc5e-3156-8998-a10ea1c7e226 | -6.88077 | -59.44206 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8df44dba-0289-34e8-9466-4943d91c9660 | -6.43832 | -52.75979 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d90af3c-cbb3-3373-8145-c9b8e768168d | -6.22915 | -55.61998 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| f5846086-0d76-39fe-9423-95d28d6d57d8 | -7.3655 | -45.82387 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1ab4b00e-7911-39bb-a1ce-0bef5034d6f1 | -5.71652 | -53.72345 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21a42433-9bfe-38bc-8ede-a4c86806b331 | -8.62097 | -54.72244 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96fb156d-e2e9-3388-9e31-7e24f84b9ad7 | -3.54454 | -48.18465 | 2026-08-21 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3f892d17-e796-38de-a707-1726bc0ec101 | -6.16494 | -55.44693 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README68.md)
