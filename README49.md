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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 976e2fcb-9233-3a89-a801-8989be2664fa | -7.47833 | -55.32605 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e5bd035-b12b-362c-9a78-76ad81d76fab | -8.55581 | -54.79377 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 844205d4-9bf3-37a9-9a47-686d01ded587 | -11.18393 | -54.01783 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bdc0ec04-6522-32b6-81a2-484b1aba260a | -8.66632 | -54.64566 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| db3ce064-9395-3a18-8a37-90d82d25e7cb | -9.46518 | -51.59839 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79a44a33-23a6-3db0-b38d-f28c81908d8b | -13.6563 | -51.77584 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73132c56-d724-3b18-b25d-180b23c2729c | -8.94929 | -60.57064 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 20cedf49-36c0-303a-a0e0-39c6ed850be5 | -11.22014 | -55.04578 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 37b503f7-12bd-3c87-9177-09b6050f9b83 | -8.03441 | -54.023 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bee3bb6a-f4b1-32e0-9d4c-049e14664553 | -11.81729 | -44.81282 | 2026-08-20 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fd51a003-d467-36e8-afee-e19d07496d92 | -9.11019 | -60.93968 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0815c5e8-cb7a-3cd7-9f2b-5249aa37958d | -11.20059 | -54.00344 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 557e87b6-81fb-3ba4-84a0-ce4de2f79dec | -9.21163 | -59.77557 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0bcdd696-b4a4-3a53-99d9-cfd8a47e143f | -7.53053 | -55.58165 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41ddcd62-ff4c-3889-89c5-985fd9e57fca | -8.66743 | -54.63829 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ab289ac-447a-385c-befc-f46b3c2c04b5 | -7.55644 | -55.56784 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e08269ba-1c89-3e94-9f2f-2521fc4ccbc9 | -11.18633 | -54.0266 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f63723eb-f79f-3157-b1e5-81bd38de4b78 | -10.83052 | -50.2934 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb12cac0-41e2-35aa-b1c1-8803e426260f | -9.07923 | -65.38512 | 2026-08-20 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f67f1d01-6b34-330f-8aec-3037d374c133 | -10.24937 | -54.37249 | 2026-08-20 05:06:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3fd58ed-0691-356c-a6cf-dccd650b0e1a | -11.99973 | -53.43151 | 2026-08-20 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6df3e3c3-fa84-3fff-bf17-ed4f08e0e1f1 | -14.44045 | -45.61818 | 2026-08-20 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 08d56f3e-58ee-3a30-973d-b4dbe910b12a | -12.78186 | -48.45349 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f8d218f-6b9b-3081-9992-1dacca13e510 | -11.21103 | -55.05984 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e01d7dab-190e-3204-be3f-de2da25a14c9 | -7.47609 | -55.31855 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e63f1e3a-900e-3425-9540-aede10dc1610 | -7.70905 | -56.7261 | 2026-08-20 05:06:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38a96246-85fd-32dc-903e-548df44b665a | -9.39285 | -60.54758 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb845944-2fec-30ca-80e3-80b9724ade86 | -6.97587 | -59.58421 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a288055-ad96-3dac-8483-c6a8fb42866f | -8.5098 | -54.86864 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a77f0dfb-2f6d-372a-b2b1-df1c61738010 | -7.53438 | -55.57868 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7bcf9aef-a4fc-3354-b52e-ada31f7f35df | -9.50134 | -51.674 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5500675b-3246-3d1a-9b58-df71053632bc | -9.45513 | -51.61136 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31157443-aeec-3aba-a629-3c28519f3f01 | -9.45973 | -50.31715 | 2026-08-20 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d001c40-2cce-31a7-94af-4a58d4b930ac | -12.83777 | -48.42826 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d70d7702-3f33-32ea-8f1f-e4e17c8a15c4 | -8.67879 | -54.65516 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c255b6ea-ca01-3137-bd8d-b9ff54f70857 | -10.8362 | -50.29692 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6b0921e-3f20-3e81-99dc-b7e8996b4325 | -8.6178 | -54.7135 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 106bd75f-4f38-3756-bf0a-0cf71cc2e888 | -12.79505 | -48.42466 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3753747c-9583-3251-a030-50552f4cab50 | -9.39207 | -60.55217 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e06fff3-1212-3fc8-92ba-d1c3251f4ce0 | -8.56704 | -54.76567 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdc584ad-7b15-34ac-8b77-bd2c32436da3 | -8.60991 | -54.71978 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12ed9709-9c16-38d1-b9f4-714c7423db3f | -11.219 | -55.05335 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a2f241c-372f-36db-a88e-1fdd6e6161a0 | -11.19346 | -54.02767 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 052254be-ab08-3cfa-946e-be03b374c643 | -12.47577 | -54.17851 | 2026-08-20 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 660d7b6e-6c1b-386a-9180-93dfc544d8a3 | -10.24647 | -54.36809 | 2026-08-20 05:06:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcce0c19-3ec0-3da4-b471-5e49e2fd4e3b | -11.19465 | -54.01944 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a4a0f5c-f7ce-33f7-90ea-e2842101061e | -6.76852 | -59.15184 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83fbb772-7e1a-3506-b041-5b95cf5ec29c | -7.87368 | -63.76126 | 2026-08-20 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f1cadd2d-3d16-38e3-bd43-00ae4e764629 | -12.79588 | -48.41806 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1b08f35-e759-3215-8e3a-646a6234d2c8 | -6.86102 | -59.02516 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31ef1545-5dd2-38cb-9193-bcba24aca057 | -7.54433 | -55.58024 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39f70431-f301-3177-ab10-9f4c3e358ee0 | -11.81741 | -44.8083 | 2026-08-20 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa5b24fe-a376-342c-86c0-69a6cb332cdb | -9.25378 | -59.81293 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27d35fc1-4a40-3b51-9d92-8055a7c85cce | -10.24995 | -54.36861 | 2026-08-20 05:06:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73714a23-3c61-3aa4-87de-bbe3bf98f39a | -12.79414 | -48.43193 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56de511e-2938-3d0d-b90a-2a8a8f292831 | -7.42692 | -60.0295 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77cf63ea-76f7-38e5-94b0-628f7b067de0 | -10.24806 | -49.42171 | 2026-08-20 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20ea76bc-7167-37e9-9c29-c2328c8d0196 | -13.54821 | -52.23265 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8e78da8-e796-3afb-a1bb-0d711168586a | -9.39131 | -60.55344 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f35ec55-fb40-3594-99d2-1bba76d72d7a | -9.25309 | -59.81718 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d5f57a2-f82b-3bf0-aa71-96be89be56c8 | -8.52331 | -54.87072 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5042523-f3eb-3dd7-bbba-aaf8ce33f9e5 | -9.39128 | -60.55677 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2175bf71-ae63-365c-8e8d-954b73c0e07a | -9.39661 | -60.54823 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54f1853b-057a-31c2-beb3-6463a5724896 | -7.60669 | -60.94773 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be1bb0ed-bb4c-36b3-b1cf-2cd675dc8357 | -10.39249 | -61.20664 | 2026-08-20 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3275c4ee-9b0e-3cab-ad7a-fe1a037ea309 | -8.54223 | -54.76931 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f897a05-0a21-3a60-a73e-6d79104f393e | -7.55312 | -55.56733 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7c0d64c-0c06-38b4-9e72-376cbc76e38e | -10.83896 | -57.52024 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec927ac4-40ff-3713-9a47-fadd882853b7 | -8.4061 | -62.6959 | 2026-08-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3839847f-40c9-3aee-bcd7-d39b5b75b28b | -13.63053 | -51.77631 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ff97772-7efd-3c86-8c5c-18d8a2ceb440 | -13.40598 | -54.37635 | 2026-08-20 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a57d609a-7b09-3074-9ea4-6d78a526f28d | -8.89919 | -60.54545 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22d45e81-2d8a-3986-a31a-863f3f8f9c30 | -9.46063 | -51.60157 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 591904a1-caef-3b4a-abb5-c3c4b9ca64a7 | -8.67708 | -54.64355 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 581257b7-fdec-37a0-9b68-37b3b0acbbe3 | -12.78069 | -48.45491 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f9fa6af1-434e-360f-aaf8-63d89d32b4e0 | -12.14205 | -48.26286 | 2026-08-20 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21d1cd4f-5cec-3dc3-9a81-2b20bca9934d | -8.5727 | -54.77399 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f4a2b51-2086-3fdc-abd6-63b690f808eb | -8.40461 | -62.70446 | 2026-08-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44d715f5-f094-31d5-aeba-d8310e4f9507 | -11.87104 | -51.65332 | 2026-08-20 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c34bfb1-ba5d-30ce-a934-0423ae9f7012 | -12.24688 | -43.16703 | 2026-08-20 05:06:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ab308fec-43c6-3251-80c3-387ee9532bee | -12.80501 | -48.43654 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ebc445c-a3d1-3db8-bba2-f51c8930d585 | -7.00461 | -59.59335 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d22dafcc-44cf-3913-9504-6129e7b555c2 | -11.69372 | -62.7493 | 2026-08-20 05:06:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16789968-00f0-34cf-b6db-8ce56675b88b | -13.25662 | -51.6393 | 2026-08-20 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0cd9134a-edef-3654-86fc-ff6404ec16b8 | -6.86752 | -59.03044 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f0f544f-6b44-3373-acec-c8f8d76363c6 | -8.55243 | -54.79325 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 561ed873-c203-36ec-baef-f3aa5ee2510b | -9.54233 | -63.56439 | 2026-08-20 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dd5d687-ed25-3a7f-9f63-b660adb91558 | -9.20871 | -59.77076 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2626cd1e-bfe8-3be5-9d37-07f14ed1ef72 | -7.53716 | -55.58269 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bacbd385-8414-347e-b30f-2df23f3e0229 | -12.95118 | -56.64069 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74f74eab-372c-3158-a244-b29f78fb7737 | -9.51421 | -51.64054 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fda2df51-83df-3d58-bc30-37fa777f7b46 | -9.46017 | -51.63309 | 2026-08-20 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24d815dc-b1bc-36a2-98dc-3d58babc506d | -10.27942 | -48.23755 | 2026-08-20 05:06:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfaf0996-0aaf-3afa-90ab-9445c680c333 | -11.44058 | -47.53673 | 2026-08-20 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 391d6e23-6a96-3bb7-87fa-60fd3c809e15 | -8.5601 | -54.65187 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6a8e24c-7e3c-3b85-9be7-4f86fd4b4aaa | -12.16035 | -57.22669 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98fee26f-b506-3187-b64d-39cc61b8144d | -8.19216 | -54.99404 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f2a2e52-f3aa-34bf-836a-4d3ec761c533 | -8.57145 | -54.66869 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59a8530f-c29e-37ab-bbd7-fe437de67500 | -7.60582 | -60.95284 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da206ba7-45e2-329d-b5dc-84d23104e072 | -7.53608 | -55.58966 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README50.md)
