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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a8f2908-68ac-34aa-8345-e4c127f3c699 | -9.18419 | -60.80195 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 98e6be82-c969-3c90-976b-20946522cbdf | -9.19889 | -59.50837 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42973362-f573-3335-a694-8519bed1af0a | -9.18726 | -59.4451 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0933cc3-1747-3e11-8e7a-23d3187695dc | -9.07966 | -62.66404 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69cf34ec-8c74-392f-bac3-6828bf337cfa | -8.98932 | -65.41376 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e538d8d6-82ac-3e63-afc0-870175b749ff | -9.7968 | -64.25796 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed31e75c-97fe-3302-a331-ad7f440488c0 | -8.86916 | -62.45688 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef96f445-f4e0-3b3f-9c74-c16bafba1c52 | -8.87142 | -62.44187 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f680778-f5c3-3ba3-8dc5-32b01a8b185d | -9.22738 | -60.92156 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d491f3db-31ce-301a-9e24-b932a4466e0b | -11.56726 | -52.10432 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 798ea9b9-9dbd-30c9-a361-19dc22a5b482 | -9.19739 | -59.51894 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b60dc0ec-1e19-3c9a-93f5-59d90702ba60 | -9.79349 | -64.25744 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdd818e1-2396-306b-bace-a2b759823e09 | -9.81286 | -64.28554 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8b25cd8-b323-36ce-85b9-ba944aaad567 | -8.5772 | -63.92164 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b9d4571-91e1-33c3-9ea1-fa5b1b4b79d5 | -9.63087 | -61.46492 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04a80eab-2fb5-3774-be65-02cbdeb88b4c | -14.11158 | -53.98098 | 2025-08-26 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4ec733ff-e304-3ce4-a374-2d893485d0e1 | -8.61229 | -62.64996 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 52a15f63-3b09-35ec-bd3f-5ff144ee6c53 | -8.88513 | -62.44397 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0864645a-d964-37b8-a5c6-8fbcb25009b3 | -10.97978 | -61.12103 | 2025-08-26 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4dc331a-9ee1-30d8-ac61-026d553c9067 | -11.56527 | -52.09882 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 002c5021-eae0-3843-93e7-a629453d0744 | -11.55854 | -52.09778 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b841f7d-5324-3ead-9d22-29bf3dd7fe70 | -9.01378 | -65.38867 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bafd1791-0d18-377e-bfed-2f23cdbd9682 | -8.97764 | -65.42278 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58f8f6d0-be60-3370-8247-83b09c06fdcf | -8.5518 | -62.62994 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1326ad5-9775-36b5-8bf4-a8bac75436de | -9.17962 | -60.8603 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87eedcb4-12cd-31fa-b473-cc8ae6706f45 | -8.85944 | -62.45155 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 187d08bf-281f-3a80-a2f6-e294f3ec9f04 | -9.15609 | -59.46226 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| afc82199-e65a-38bb-b5f2-a054472255f4 | -10.6517 | -65.31496 | 2025-08-26 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cba2447c-55d0-3094-87c2-cf0c88efc71e | -9.25568 | -59.64134 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30c6479c-59ec-3324-8646-b4b9b4afbe96 | -14.4249 | -56.45008 | 2025-08-26 05:38:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e7c07f2-db38-3cea-bb64-21bd1a10cbdd | -9.16182 | -62.35401 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed471fb6-f47f-3558-9e0b-8f464a62603a | -14.97464 | -52.88159 | 2025-08-26 05:38:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dc2c9bba-3c39-35e2-bf32-5a5fec3d1537 | -10.25733 | -59.1063 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 464317a5-7b6c-39a1-998d-2693440bd314 | -10.89255 | -55.77744 | 2025-08-26 05:38:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dbf6fde-39a2-34ff-9493-10c4e66f120c | -11.55794 | -52.12759 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91daa117-87fe-3344-9b24-2fc0bb53d693 | -8.10718 | -71.2465 | 2025-08-26 05:38:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ee29982-2e3b-3821-9c22-62bcbfcd202e | -9.31428 | -63.44272 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5cb19b75-8543-3f82-981a-f8eb9179f289 | -14.43515 | -56.45473 | 2025-08-26 05:38:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25771f35-ef44-357b-a273-ab83edafffd9 | -8.99879 | -65.39713 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d6a90be-c31e-3a41-8a4c-cc5c4eb3b701 | -8.97989 | -65.40862 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ecfb3fcc-43f3-3efe-af66-0530e6108c9d | -11.56118 | -52.09718 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 38fbd543-7a39-3a41-846c-3eb97bcc0ca7 | -8.98097 | -65.42331 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bb8a476-34a6-370e-82a2-eb5805317dad | -8.9024 | -60.5542 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a53339a-5247-3f9e-b370-d09c7b8cac93 | -8.34726 | -62.94161 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| be8a5427-b85d-33c1-8306-8720c46f6a4e | -9.495 | -60.54633 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ead6cc4c-df17-3d39-82cf-d60de7a36f66 | -8.54444 | -62.63258 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b533c8c-4bc4-3a39-9f7e-3a463ed3365e | -9.03133 | -65.72685 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48278ba2-37c8-30ec-82c8-fb77d19a4b5d | -8.65657 | -63.43136 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d9d4ff5-25c7-3cc9-b490-60608654533c | -8.8577 | -62.43977 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3ab90b3c-5959-38d4-9502-219aaef2dae7 | -9.20191 | -59.516 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e6309ce-3434-363d-9e32-528ba4b179f6 | -8.98764 | -65.42438 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4bc7de1-040b-32c8-991d-4e0628b93582 | -10.39507 | -57.69773 | 2025-08-26 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4872bd62-e570-3263-a7ce-80caa192b421 | -10.41746 | -64.39974 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37b75fed-5d8c-3560-b844-5ac14eca1f08 | -10.64711 | -51.59649 | 2025-08-26 05:38:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 18ac0040-5064-3287-8842-720032a05c0d | -10.03113 | -59.35692 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7007ebb4-fd3a-3f77-a086-cf19f708845c | -9.16837 | -59.55063 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 232705f4-706a-3dfc-9520-c11c70d32e07 | -8.66045 | -63.42835 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88a870f1-57e6-34bf-bc77-21ec9770eac3 | -10.64023 | -51.59571 | 2025-08-26 05:38:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 595bc913-8f89-319a-93f9-b5ecafb34350 | -8.56652 | -62.62469 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab65ee25-ca07-37eb-8363-c7603cf657ce | -9.07326 | -65.72254 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56d0062d-adf4-304f-8d62-9379824ae632 | -8.54615 | -62.64414 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a2e5191-3942-3970-a2ca-8e8166e7fee6 | -11.54371 | -52.10804 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 664a1370-d670-3e62-b6e7-06f5a3a2ddab | -9.70039 | -57.88079 | 2025-08-26 05:38:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35230091-4a94-3684-8e5a-f275e6f34cf3 | -8.60085 | -62.61047 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e4dd2ae-a417-3037-968b-4a1c1d75fc92 | -8.99209 | -65.41783 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d8c4594-e32b-3b79-81d3-c4e381156df3 | -14.36431 | -51.91946 | 2025-08-26 05:38:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38b33ff8-88af-3b91-a445-16a4586b9b9c | -10.97768 | -61.12333 | 2025-08-26 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f8d7da5-58ce-36ee-afbb-6cdee4975909 | -9.16788 | -59.55413 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cca6623d-0987-3a54-bf79-9ecccd3eb540 | -8.92227 | -62.43048 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf682897-c17d-32de-8b34-efd64e9e8d51 | -11.54766 | -52.13352 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d14f65a4-f098-3c20-acae-e507a23fbeb4 | -9.01655 | -65.39274 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53cb37b3-ec59-3fb9-a620-3fbe6844589f | -9.79734 | -64.25446 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ffd22980-e0aa-3fa1-81c3-25df8cbed9df | -9.01917 | -65.69548 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be5c87e6-09f3-304a-9b08-f0c364217534 | -10.14642 | -67.67043 | 2025-08-26 05:38:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf5e1cc7-3c2f-336e-8e04-8e1328db99c7 | -8.6014 | -62.60678 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bac1330b-3815-37e0-8389-45af77233188 | -8.55747 | -62.63836 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf886077-d6ef-31af-9e5d-469c915868b1 | -9.22418 | -59.67332 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e5c1d572-eccb-3fba-ab3e-39bbcd14c039 | -8.84686 | -62.44194 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 5db59b87-1dec-364d-8952-ad5e42494d9c | -9.02913 | -65.71915 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e74da64-8bc0-37f4-8994-1f66ea91eae0 | -8.54672 | -62.64046 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59c1c883-e696-36b0-8f36-bc1a0bc0e431 | -8.35172 | -62.93493 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 111c00ff-7cc7-3be5-84ae-d263c6dc4156 | -9.15448 | -59.46541 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8d5ae090-ec2c-3250-ab55-eeb0995a78d9 | -8.8857 | -62.44022 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f95dbcc0-949b-3861-967d-3d31a1a9b4bd | -8.34781 | -62.93801 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 595df8f7-119f-3bf6-8e41-9ccea6764629 | -8.84629 | -62.4457 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| e3b081e5-7ea9-3314-9e8a-97a52cf68731 | -9.0825 | -62.66828 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7acceb71-f114-334b-83e5-7572c905b748 | -9.07923 | -66.06434 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd840333-73b8-3821-9c5b-29190a3e4650 | -9.19238 | -59.5254 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e7a091e-5775-37dc-a289-932ba8477680 | -8.55972 | -62.62363 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28228fec-9378-3188-a45e-98372b34fa51 | -9.16657 | -60.77868 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d51fcdaa-a1f6-37a0-9e11-1ddf55e3edb9 | -8.97239 | -67.48135 | 2025-08-26 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8ea6b49-9e03-378e-a273-4117c540f47f | -9.16733 | -59.52891 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd29b5bc-b4e6-3282-9b0f-38c7e39eef01 | -8.61147 | -62.12054 | 2025-08-26 05:38:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 752dbbbc-3f65-35a7-ba0d-c3a8d59c6ea8 | -11.56927 | -52.12365 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 246e83ca-d9f2-3a96-a9fb-e863c0d75831 | -9.17781 | -59.51256 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20638010-941a-36e8-87d7-af67b14e2a64 | -8.57996 | -62.63367 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0af1fa45-ab46-3a47-be66-bd53b73633da | -8.84343 | -62.44142 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7284f78f-991e-32d8-a854-37c19911933f | -8.97543 | -65.41517 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0253129-cb04-3be3-90f2-78e1dd410b30 | -8.53824 | -62.65045 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2d6a922-39d7-3213-8042-3027c8a65c80 | -9.07797 | -62.67516 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README84.md)
