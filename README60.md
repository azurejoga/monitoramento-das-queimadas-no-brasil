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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bbd83e5-8f6d-3898-835d-ceef24107971 | -6.90134 | -58.99189 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c696098-f7ec-3759-9f88-ebdad62689d8 | -13.39163 | -54.37508 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bd403c3a-8c3b-3b83-be60-0325250bb3fa | -7.01392 | -48.03871 | 2026-08-21 05:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cad90857-444b-3e6e-bc5f-9a135fda4f92 | -4.11498 | -48.9302 | 2026-08-21 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ec9d15c-3180-31b1-984c-632a7e431d8c | -8.58533 | -54.78825 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cf7d904-80b7-3fd0-a1fa-ad3312295665 | -14.3113 | -51.90867 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab1e963c-9bf8-35fd-851a-33f66ac42a83 | -6.10132 | -57.69405 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00e78436-8ed6-3583-8e5b-649696c99ace | -6.42787 | -52.72156 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cab7100d-31fc-3d31-93d2-c71d46b435c6 | -6.24315 | -55.39765 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b31c2cba-4b16-38c6-96bf-ce498edbf343 | -7.4598 | -46.15152 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3863a2a5-cb52-3470-90a8-3a5c55219c6f | -15.05947 | -48.70386 | 2026-08-21 05:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25dbd907-e6a1-3fa8-abdb-5f45fcf7c08a | -8.37253 | -62.70085 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 766d16d6-1372-38f9-8789-e4073b6c001c | -6.87721 | -56.63585 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12568aa0-2573-3e13-bf3a-27f37f10d2ed | -8.68226 | -54.73634 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69f87ff9-db00-3543-a29c-23703bffa4f0 | -6.35994 | -58.33962 | 2026-08-21 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eac13bf9-f112-38b2-9b2e-6bb0c25f4e21 | -6.86336 | -59.03011 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e1987e2a-9912-3c6d-b873-e6b8adfe2bb5 | -6.58667 | -58.99347 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 47733cea-516c-3e6e-8c7b-cd6ae7dedb94 | -4.91746 | -56.25821 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4953c93-9919-3969-8664-512d14246b00 | -13.25901 | -51.62895 | 2026-08-21 05:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 984dc71c-4e3d-3c99-972d-c99c6ca3b5b9 | -6.8212 | -59.39817 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7e59cd0c-cb64-358b-8dea-c23be8c8e01b | -3.84477 | -59.37608 | 2026-08-21 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28990d21-3ea6-3422-9394-0e1f9078ad14 | -6.89506 | -59.44059 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2df9a54d-fe3a-3df7-915a-3be2e1d812a1 | -6.82341 | -59.40612 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 490922bb-357d-3d03-aa62-573947c0f625 | -8.40113 | -62.70043 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 873e87c3-e534-341b-aa8b-4f712145bb73 | -6.89061 | -59.42465 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3a88654-b11e-3a0f-b298-39a4fb7b5318 | -6.89036 | -56.4416 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d18d3022-2fa5-3c00-8bba-4ff72b3cca82 | -13.95029 | -53.85936 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1313b1b1-a158-34f1-9bca-7c564e6e60b2 | -6.8707 | -59.02757 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c181ff6-3faf-3ab1-b81d-b4b7a7dc5be5 | -7.06727 | -59.96703 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b38e4574-16fd-3fd6-930e-25bc2a5638e2 | -6.36384 | -58.33665 | 2026-08-21 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba647e1a-057a-3bfb-93a6-2e9219798dd8 | -5.60274 | -44.01134 | 2026-08-21 05:23:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9c6117e7-e336-30dc-89a9-c8dd9b1b470d | -16.30328 | -48.90345 | 2026-08-21 05:23:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df4b3163-6504-32e8-88c8-e34203f23fa9 | -13.43859 | -51.79307 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f242ba0f-bb8a-3d76-895b-bc37106dad4e | -6.37818 | -54.94931 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7000343-86b6-33da-8040-3f55f66477e6 | -6.0832 | -57.93317 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 605bfe35-f199-3d19-8d26-1b74a105391d | -9.805 | -46.644 | 2026-08-21 05:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 3dfdb8aa-1ca5-392c-89a9-b373db759999 | -14.10705 | -58.84949 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 81f4b16c-b66f-326f-a478-1a1804617519 | -14.09545 | -58.81465 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3ada0a4-4fc1-3862-83cb-3e4acb11d586 | -6.12088 | -57.73974 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad7dfcdf-0169-395d-b614-6b2cf2dc2f9e | -8.45328 | -46.95725 | 2026-08-21 05:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf5fa21c-c9d8-329e-8d1f-95e966ee9f94 | -8.10051 | -51.66919 | 2026-08-21 05:23:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a1dea65-fb50-39fd-ae02-3ac5eef583d5 | -6.88867 | -56.43036 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00d19874-01f0-3d37-b059-4ad6650f91f8 | -7.53304 | -55.57624 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 867f4795-d3da-3582-9943-29b4b81513cd | -14.06821 | -58.87966 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b728576f-89ae-31d8-b3ca-399b268df5aa | -7.24975 | -49.90803 | 2026-08-21 05:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ccae566-b8d0-37fe-969e-acd05b940fea | -7.14342 | -47.50948 | 2026-08-21 05:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d937f9ff-caef-31b6-b789-d8d02b0ddc11 | -5.8651 | -57.66741 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7af13a1d-9b37-36e0-b2ef-ea1186597481 | -6.57107 | -58.96125 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 778aec84-dd4e-3167-8847-c2f115382d97 | -6.31552 | -55.91827 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0f05ba8-3aef-364d-a390-8eaf5ef32bea | -6.8034 | -59.42578 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9f1602b-b7c7-32d9-9e82-0844f2a950a1 | -5.81554 | -55.723 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12e2fd5a-0f23-3259-b098-7ab9a405a861 | -8.61316 | -54.7274 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ceca1a5-7316-326d-ad3c-afd09b020046 | -8.09612 | -51.66861 | 2026-08-21 05:23:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 546c0fe2-e985-357c-b6cb-287361e4e3a2 | -9.51039 | -51.67975 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d93359fa-e965-377d-8f16-8b9e44376828 | -7.39441 | -59.97511 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af842449-7724-3db9-9afb-89a7766444dd | -14.56513 | -52.99173 | 2026-08-21 05:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77ccb674-0e3f-3fc0-8636-38918c08feb2 | -6.89446 | -59.44429 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bad96ff-bf75-33a8-98c0-10b632be67a4 | -7.44278 | -60.00665 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16d5c091-3878-3c5c-9834-466f51d1c810 | -6.72104 | -59.08909 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65411b74-36d0-356c-ae19-a8a2cfb6797f | -8.9003 | -60.54819 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ac0169fb-f541-3027-aad9-c5785282cbe3 | -6.69777 | -59.10392 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3db63f2-b819-3b46-8f10-fafaaed6a85a | -4.88685 | -56.27863 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecbec75b-a83f-3849-bfa9-41c9bf007879 | -14.33549 | -51.90707 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 460508f2-add7-3d4d-a18f-e137429b22af | -13.44986 | -51.77941 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5aacb6ea-e087-34c4-80fe-ceab8f5dec16 | -6.38874 | -54.9509 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c58594b0-f29a-3d1c-a00f-5bada72c1ed8 | -14.02766 | -58.88432 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4ca0c846-6f72-3c0c-a2c7-4e542db6881a | -6.92699 | -59.35097 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f8c9604-b7c4-3681-9699-eecff03fd297 | -13.67018 | -51.80072 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| aeaeb1ef-4c54-341e-bb31-0adf47eb2a6c | -7.37328 | -45.81439 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9b33974e-636f-38b4-96a5-94b52baadc42 | -6.88756 | -56.43752 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b4e2dfa-4728-3994-a356-02210075810d | -7.77822 | -61.15298 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 01221d16-ead0-34b8-9ef1-8e1ce73052c5 | -6.20446 | -55.48752 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44ff18d3-449f-3db5-9a05-8ea80a7c60e8 | -6.01615 | -57.82278 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6d18d59-6c71-3d75-9885-251c888c5ceb | -3.2081 | -50.91878 | 2026-08-21 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 085be383-cbd5-3b33-afb9-9af0725797fc | -9.11112 | -60.33927 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e429f009-9ff7-3d8e-a756-a6bded94ab94 | -6.86709 | -59.43982 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ec914d04-60e6-3371-b1e2-6d63a5e5144b | -6.69926 | -58.9444 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eff4d009-aa3a-3daf-a86a-3805913dfee8 | -3.15525 | -54.6054 | 2026-08-21 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 599f1511-fdb1-3352-b25b-23452818047b | -8.54791 | -54.86439 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6be855fd-a876-3605-9be8-359af3697d48 | -6.10409 | -57.69805 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5799e821-af1d-3355-a54b-7a8659420342 | -12.52027 | -54.76257 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9416312-8f40-326c-a713-2a8e314b9552 | -8.40681 | -62.69091 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3969ccc3-e5fd-3f5a-81f8-84d5ef5db43a | -13.39236 | -54.36996 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1b4a900e-bca9-3221-94f2-fe7490bbd7ef | -6.12209 | -59.91457 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86613715-0a3f-3245-979d-e5c8f4504709 | -14.71883 | -47.14475 | 2026-08-21 05:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 609bbac4-9605-3a44-90f6-829dd19f3636 | -6.1615 | -55.44637 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0ff19ef-598c-34f0-8bc4-797fdc3c5f19 | -6.11315 | -59.92516 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 082b0414-fa22-346e-a021-609f9d9e668e | -15.06542 | -48.7041 | 2026-08-21 05:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b88f264-4240-332c-a3d3-eb2604abc874 | -6.42719 | -56.1867 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1170ce1-6156-365e-9f76-c42664973eab | -9.21949 | -59.78247 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3378db2-4c6c-3c0b-aa17-b0a63f5b357a | -5.49456 | -60.13612 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8338683d-1f48-3ed4-be2d-da183cf3c2f1 | -8.61873 | -54.71525 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1747076-208a-36a4-ab54-d4a72e0ba8c6 | -4.01617 | -48.06261 | 2026-08-21 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d6406b1-bc87-3a21-8e0e-5f9843e7eb80 | -4.4536 | -55.43436 | 2026-08-21 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 247525f2-58c2-3dce-8465-8e3243bf9255 | -13.39414 | -54.38587 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| c0a5efd3-0bb0-3cb3-a43b-24aeaf59f652 | -6.1004 | -57.86818 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ae68499-fb7b-3235-874e-183a148f33a9 | -6.95288 | -52.815 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c9862da-cd78-3eaf-a661-fa247b53d393 | -8.54352 | -54.7948 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2917783-1600-3f01-9d14-7936837ddbc8 | -9.21535 | -59.65758 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2541ca5-0c11-31b4-86e2-6e606a2bd6c4 | -6.89362 | -55.72344 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README61.md)
