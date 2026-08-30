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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f859751d-71a3-35fa-ac79-eb9593d3f645 | -8.638 | -62.85124 | 2026-08-30 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08f1b625-5675-3db9-8617-84d53ce890d4 | -7.45887 | -70.13428 | 2026-08-30 05:53:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a01730e0-1a4b-3676-b2d9-a5395231bee5 | -7.40262 | -60.58567 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75a844c6-b160-3a9c-89e3-109d0567eba8 | -8.18415 | -54.9408 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 646ae068-9d88-3267-96c0-779b0a53eff5 | -9.85008 | -60.2697 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bddbf3da-b1c0-3024-b80b-9acd845d30f8 | -6.7823 | -55.68599 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d84d3c2a-2c86-326a-8bf3-7df6efd59d4e | -8.15201 | -63.99873 | 2026-08-30 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e26cf03-678f-34d6-bf26-d70bdf3f9537 | -6.77028 | -55.64944 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5072ac14-70f3-39ec-b2c7-ff5182b8a4b9 | -9.8957 | -60.2749 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 537f639b-6f52-31b3-946a-ecee59b1b4d8 | -7.84437 | -62.31523 | 2026-08-30 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6c6ce7f-31b7-3292-bfd2-cab70badb210 | -9.13638 | -61.01198 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c877f6e-c894-3596-8658-8468f1b1e4ce | -9.70964 | -60.74343 | 2026-08-30 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18d936f5-de87-333b-a338-292c0fbb5c4c | -1.24683 | -55.70196 | 2026-08-30 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e10d5fb-b05d-32cf-a4cd-dd0225768e70 | -8.95938 | -62.39216 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 821ff20f-c98d-3bd1-a896-b2f0f3615148 | -8.60062 | -54.81116 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a4aaf2c-0c94-31e9-b65f-a7088d462c63 | -9.23673 | -60.41666 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c35e7dae-abce-322d-b1b8-f0970f15ee74 | -8.58044 | -66.95338 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79759c89-93ea-3600-a825-6e6025d1e5ea | -7.51103 | -60.72365 | 2026-08-30 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7537a3f0-376d-3f60-b9a3-221c899fe637 | -8.60577 | -54.77247 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9df43262-f3de-3879-91c6-7eda7faaf9ba | -9.24202 | -60.40954 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57b9528a-53ae-3fc5-8efc-c22715055e38 | -9.04868 | -65.41721 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9b70b337-98a9-3031-b1c2-aebf44eadaad | -7.31312 | -60.60514 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4f650c53-72a5-3972-b324-f09a33f63e4f | -8.6104 | -54.78334 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58ec143e-7c11-3bde-b39e-dc4daaa915fc | -7.57814 | -61.29535 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 73fdbd60-5c1f-31b7-959e-cf1f929fec99 | -7.55827 | -61.32215 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3fabc0e3-63b9-3195-a374-8a885fafa58d | -9.05256 | -65.41423 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 90b1eea0-2870-3f9d-b898-5401218cb6a7 | -9.1395 | -61.10225 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbff9426-e3f7-38ab-83ae-1eb98c8ea95b | -6.71193 | -58.56279 | 2026-08-30 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 352ef2f9-991e-36a2-b0a1-999dda360099 | -8.65434 | -62.84086 | 2026-08-30 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf67db02-2d16-38a9-844e-ed535586be37 | -8.25446 | -62.75932 | 2026-08-30 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 408ee9c6-83a5-3383-98b2-c0434d85c9be | -9.16028 | -59.51218 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff184f48-da8b-37e2-a1e8-943379994dca | -1.44233 | -60.26255 | 2026-08-30 05:53:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d64a8bfa-3af0-36e4-a158-d2c173af4fd3 | -9.09649 | -65.48241 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 444d0c66-4abd-362c-bb1f-cecd810dba6b | -8.95453 | -62.3734 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ba170ea-4c76-3231-84f5-fd5807bf6f23 | -9.15726 | -59.51404 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16371385-39b1-3e77-8bbb-8297313be9d3 | -9.13678 | -61.10136 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7fbd163-5bcd-353c-8056-44361764366a | -7.31363 | -60.60162 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b29f5a4-77b6-39d1-9e8f-8bdb115cd233 | -6.68127 | -58.74469 | 2026-08-30 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67cd0219-8875-3572-b8f0-3aff84d30ed6 | -9.1579 | -59.50963 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa0260f4-b687-3aa6-846c-46398a2e8343 | -7.24005 | -60.61998 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6dc805b9-b91a-3881-9e5c-8af64f5eeefb | -7.05631 | -55.67921 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0cfbbb5-f4c1-3dfa-85aa-471df9790405 | -9.01376 | -65.4084 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78b1ee97-e0f6-3933-acbb-4445f3951933 | -8.9568 | -62.4098 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33572d70-62d4-3d37-a96e-55918fc1651a | -9.06311 | -65.41231 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 317ce3d3-878d-3ccd-8a4f-47ad42868d94 | 0.58068 | -60.44495 | 2026-08-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee1bdc54-711e-31ef-9526-5c906a305d1a | -8.94427 | -62.37862 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4ef4003-0c89-3766-9bbf-6f341bf69aef | -6.87012 | -56.56915 | 2026-08-30 05:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bab3ef0-5224-305b-9885-2ec842ef096e | -9.66363 | -55.10628 | 2026-08-30 05:53:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 24b925b8-5472-3f9f-a795-7fc33d802eb5 | -8.95389 | -62.3778 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f1bed53-7221-33f3-b3ac-b8af695e2abd | -9.17361 | -59.6128 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed87b493-85fa-3b2b-b26d-d034a9c98fae | -9.61136 | -55.13133 | 2026-08-30 05:53:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d84fc085-502d-39fb-ae68-64692f644646 | -8.9605 | -62.41037 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 865734e6-7059-36cf-8c0b-ab0bf86800aa | -8.06121 | -71.30408 | 2026-08-30 05:53:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1874e27-e0db-3433-885e-f8eb8db9b1c1 | -9.64911 | -58.9417 | 2026-08-30 05:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a34ff2d-47e3-33eb-a7da-90d967b14983 | -9.79245 | -59.44468 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0277f3d4-5870-3649-96d2-16ec549d3aed | -6.88473 | -59.44996 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 00c0c740-ade4-3c62-8a1a-c7fb3e8f3909 | -3.48984 | -54.65852 | 2026-08-30 05:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d42e2a44-4095-339e-b4d9-7c92ce75a0b9 | -8.64224 | -62.84757 | 2026-08-30 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 20470721-3a70-3dff-97d6-d404620d1861 | -9.89351 | -60.27192 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a2996c17-71fa-3e36-8b55-e2460fe6256d | -7.30152 | -60.59982 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca54330b-4cff-3c02-92c2-076fdeff5890 | -7.32472 | -60.61043 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a28e93e9-676d-3e36-a77b-de2d6611cc43 | -8.18023 | -54.93705 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b451b7ee-d177-3122-ac4f-cd617d5a0f37 | -6.79373 | -55.66728 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95c5bec8-30a7-3d9b-922b-bf41ce1e780c | -7.39908 | -60.58156 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e58b0f7-0241-3325-ae1b-ed646ee581e1 | -9.06534 | -65.41987 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95f42c50-376f-37e9-8bdc-16aa4540b4bc | -9.18446 | -59.6323 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecc95c2e-5f0e-3d31-8df5-6ccb3087e37b | -8.95873 | -62.39656 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 115bccfb-b2f8-3f29-8f52-ec5dca3306e8 | -6.94864 | -58.95455 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fe705f8b-13de-392a-9911-76c49f6f434a | -9.71129 | -60.73208 | 2026-08-30 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92c34bda-ca9a-3952-a90d-4c5fb6aee92b | -8.94711 | -62.37227 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0ae51a4-5a96-37c6-a6c8-4d007748cf69 | -9.17804 | -59.61349 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 07c022cc-68b0-35c3-8ddd-9e7356ca2631 | -3.59631 | -55.30114 | 2026-08-30 05:53:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49ed5889-c60d-3953-9fc9-04152ecc078d | -6.72806 | -58.70925 | 2026-08-30 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6731dee0-e68f-3de3-a7ee-ec49f27dc895 | -6.85884 | -59.47556 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3ce7e400-db88-3d9f-bef1-d1a20da8cb1e | -9.25513 | -57.52416 | 2026-08-30 05:53:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1983acfa-f533-3e44-8377-50526f4e902b | -8.25147 | -62.75465 | 2026-08-30 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d0cfe18-e5c8-3512-8b75-f0c14417a07c | -7.30754 | -60.61509 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f800c7fb-5457-33e1-86c4-0e664d8da2d6 | -9.24093 | -60.41467 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff39e379-864d-3798-a158-0e6a0bb6d443 | -6.94027 | -55.71099 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ffaf1ec5-4806-3db8-93d9-a27bf6210f19 | -7.59112 | -61.3489 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e9fea6f-9cf1-382e-a66e-52047b1f3679 | -9.05757 | -65.42583 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b8321f4-5895-32db-937e-557c3f497edf | -9.05812 | -65.42233 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a161f2e7-8032-34f9-92b0-e2608bf7d548 | -8.99824 | -65.44192 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7baf9dc-c4ae-33eb-92fb-0e7c4e050ddc | -6.7849 | -55.6676 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc90db75-4fa8-3939-a3fc-25257de98937 | -9.175 | -59.6353 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a8be662-03b8-3ac6-8a5f-37f774e39515 | -8.61098 | -54.77875 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd17efc9-f43f-3e4f-993c-e59053573679 | -3.40046 | -61.32399 | 2026-08-30 05:53:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aab87e0d-180d-3faf-8a28-295f63dd093a | -6.76414 | -55.65237 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84e9a580-a491-3e30-b8f4-cc1d9f110725 | -6.76705 | -60.01241 | 2026-08-30 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f3738bf-c09a-3553-882e-f127ecbfedae | -8.95302 | -62.37093 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e329523f-08b9-3d59-ac77-7cc705f93142 | 0.14162 | -60.40158 | 2026-08-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5afb169-366d-38ff-9196-f60bd7d6a95c | -9.01875 | -65.39839 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46eba1f4-3d6c-35c2-94d4-ad35637f6ec3 | -9.16414 | -59.51727 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a0a01a0-8e9d-3397-a7a0-37b2a7368501 | -9.13549 | -61.10166 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ca68364-2344-3dea-a223-7677ad2192b6 | -7.57668 | -61.3051 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3de52175-3770-390d-b2b3-b7dd213dc174 | -9.00818 | -60.60662 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8a98b37-c484-38c9-8d09-d1ec3d20e6e0 | -9.88747 | -60.2835 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61915602-de60-34b5-b00d-76beff22701e | -6.76826 | -63.04435 | 2026-08-30 05:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5f6245e-c525-396e-986f-1cc5f982a518 | -8.94647 | -62.37668 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0eb4394e-2cf5-38a4-9f8a-ed3f2fdfb803 | -9.06256 | -65.41582 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README64.md)
