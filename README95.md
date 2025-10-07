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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97eaa62c-ef3c-34b9-b999-b032fb4dc7c2 | -14.76443 | -46.0536 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd3c4c85-657e-3036-ae77-e70d9169bc6b | -12.94727 | -54.72411 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c30bcee-c357-377b-9c9b-ed432d3a2804 | -10.41971 | -50.28627 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fd92c5a-adab-3a56-87cf-e2d8c95ab235 | -14.92589 | -46.80855 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fda9ac8b-7961-3b04-91d4-93776aef38ce | -15.27194 | -46.35525 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b4acbdb-5691-3cf6-9da4-b34d5922cb54 | -14.90768 | -46.87024 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 530cca0f-de40-346b-a190-dd07bfc9020f | -7.86123 | -54.78321 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b32bd12-4e39-3982-81a0-961b3fbd406d | -10.95148 | -51.18402 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 428466b9-43f8-3fee-85f2-b1f383fc4d9a | -13.22692 | -48.45784 | 2025-10-07 04:57:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cf2bee4e-827c-3a61-95ad-7e62bb998fb7 | -10.80531 | -56.23691 | 2025-10-07 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcc01efb-3590-35d8-b454-071809c085bb | -9.5549 | -54.59801 | 2025-10-07 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9f94768-073f-3bb5-8ea7-ad0a8cf9364b | -10.18176 | -45.5399 | 2025-10-07 04:57:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1770450f-59f0-39c0-91d3-7c87bf265b4f | -12.02118 | -49.71785 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b91d6e5a-4792-37ca-bdfb-8d1a071f9efc | -14.91294 | -46.87095 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4c4def1-19ec-3c38-bc5f-7f6822954223 | -7.56155 | -55.15056 | 2025-10-07 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84dc899a-7ac0-3b0e-9558-24c65226dec4 | -10.25713 | -44.36711 | 2025-10-07 04:57:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72d87809-0323-39d0-bf09-9e6752eae4b6 | -10.45018 | -50.40881 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 21e6ee5d-c553-3451-aa87-0a4be1e90ffc | -11.02996 | -50.90943 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ecb2cb4-dcc3-3cdb-acdb-b55d82123b2a | -13.13067 | -48.0103 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16a05e91-27f0-37e6-9869-afd746354da9 | -9.02174 | -50.69522 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b5a0fe0-8d4d-316b-9c5b-8d35d96cbf2e | -10.39243 | -45.37774 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d70ff3c-2b3d-3574-a278-90eeaf96416a | -10.35824 | -44.98232 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 408f673e-e5ad-3ec6-97f3-a0a4eb239e00 | -12.25569 | -47.847 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7156f85-a69f-35a8-b542-af8bfd7b5672 | -9.9173 | -49.96545 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10dbae46-5f3c-35f4-99e9-e6f3ba01827d | -10.88496 | -51.03019 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 53030d12-ad77-3222-ae82-f1e8ae645c9a | -10.34223 | -46.9461 | 2025-10-07 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| aa45a7e4-7494-3b1d-8e36-f0ee479921b6 | -14.91334 | -46.86772 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2924b2c-03f9-3ab5-8f06-0ca06c9aa4ca | -14.91273 | -46.82854 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69c4eefd-1277-3674-9f7b-ca2770e2266b | -14.72428 | -46.01065 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0bbe86f1-8566-39e5-bd0a-ba40f350107d | -13.23157 | -51.68271 | 2025-10-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13ba7b30-d8da-3509-92f5-d684f7784548 | -13.28344 | -47.16777 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 068e0449-822e-3a7e-a044-ab72490150d7 | -14.92297 | -51.4463 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b9075b26-dbec-3481-9928-d750ebcff1c7 | -14.93146 | -51.4424 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3e49ebc-efaa-3e6b-9ba8-4076a077531e | -9.33946 | -54.52107 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cefe0e3-1ce8-3c4b-a1ad-655d205c12a3 | -14.91682 | -51.40424 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f58f77fd-7874-31c0-9be4-c2ff51082d34 | -9.00068 | -61.54993 | 2025-10-07 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 514a3d03-1199-3770-b853-001ddb6c238c | -6.69606 | -62.84169 | 2025-10-07 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae61b58d-3ae7-314a-a3e6-bc41700374f5 | -8.61763 | -54.96175 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 101c03cf-84cd-3efe-9639-2933a1c43301 | -15.05442 | -42.34019 | 2025-10-07 04:57:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e4868b2d-a42f-3561-96d7-30ed15916688 | -12.91175 | -54.73309 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0db78736-ba43-356a-a1c4-e463c658c564 | -8.96709 | -50.80263 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2737dfa-dd91-3dd9-a13a-600c2d562866 | -13.76179 | -45.73308 | 2025-10-07 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d8354ba8-0569-3650-a18f-846d8ce66e2f | -15.55733 | -46.83009 | 2025-10-07 04:57:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35f4611d-4369-3480-bbed-2fcb2c4fd794 | -14.36422 | -47.72769 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d891bd34-da4f-3c3c-8a81-d4028dd27533 | -14.56246 | -48.94951 | 2025-10-07 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a17440a-8e84-3755-a32c-5845f607cf37 | -9.60836 | -63.18853 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 555a87c4-ec15-3f01-bafb-9b639a3710fe | -14.90964 | -46.85406 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b71e0e1d-1d32-3324-89bf-d8d4ac46c789 | -14.96693 | -49.95987 | 2025-10-07 04:57:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ec1e2907-d836-3a66-9902-6b71a14221c3 | -10.21855 | -57.68417 | 2025-10-07 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b880baa0-613f-3180-96b7-5515cf737c5b | -10.88709 | -56.07029 | 2025-10-07 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b887fbf3-7ea6-3e9f-bdf2-a4f3d80aa414 | -14.76706 | -46.03103 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ee840367-a471-3d9d-8b91-38bd5c9ca562 | -9.03992 | -50.70261 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4367e92e-369f-3c8e-a47f-032046ea91f6 | -11.12404 | -47.21554 | 2025-10-07 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 833a19d8-d640-3f50-b355-a0215d1b02f9 | -12.0146 | -47.78778 | 2025-10-07 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 922dfdbb-6e96-391f-a601-be062ebc5a6b | -13.65734 | -48.73112 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 817dfa61-ca86-3bf9-a034-2c94875dd2d1 | -8.85396 | -46.09498 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2912fde3-c0f0-3ddd-a5bd-aaf458ca2dd0 | -14.28469 | -45.84069 | 2025-10-07 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fc8420f-d701-3521-92c7-b4bc7c7bdcce | -9.60833 | -57.14096 | 2025-10-07 04:57:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 921d4bcf-e0c0-3cb9-b89a-14ea4c716dfe | -14.9048 | -46.84321 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 362eed0d-340d-3d68-9c04-c324fd764ed3 | -15.39335 | -48.01109 | 2025-10-07 04:57:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06d4a104-2047-3b94-a3f4-4aeaf34d78f6 | -10.5996 | -54.36663 | 2025-10-07 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e24fcb4-ecf0-392f-ae05-a78287e9421c | -7.49316 | -63.67237 | 2025-10-07 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cc3e77f-1782-316b-9646-100830786c9c | -14.49615 | -46.92389 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f833caec-2885-3e56-9e08-a987f525ff24 | -9.69923 | -45.93019 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e3b75c8-c7e2-3c85-bd78-76c5e5ae5afe | -11.67077 | -46.34488 | 2025-10-07 04:57:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87c68324-8d35-3a42-8fb9-e74e40e05527 | -11.84296 | -44.9141 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30b36c0d-4bd2-3509-995b-d25adf88d5f4 | -9.39974 | -49.3714 | 2025-10-07 04:57:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f05ddb5-8e1a-3075-b231-803c3cf3370f | -10.4004 | -50.30928 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b5b667e-a364-3c12-9110-5ee8fcf3cae3 | -15.29208 | -46.33178 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ddc3b3bd-bc0e-3c61-be6d-ffc0e9996b97 | -12.6117 | -44.75059 | 2025-10-07 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b5957d5-4bc3-3c1b-9bbc-40c735bdaa65 | -11.29067 | -49.99466 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c89f495e-fa91-3482-b82c-b4b8a59fe070 | -11.03551 | -50.92481 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 2f4e5b49-9add-3564-9bcb-b09b417504b2 | -13.34106 | -47.77082 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16f9c4d0-06c3-3b42-8c30-84974cf3ae7c | -13.67523 | -47.33495 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dc485df-71d3-3377-9ed7-0e4e8ed08a3b | -10.18219 | -45.53645 | 2025-10-07 04:57:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9707b6a7-3f12-356e-af94-294582159882 | -13.59368 | -48.68262 | 2025-10-07 04:57:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dc6a7d1-fc66-3dfe-937e-a5debfe5c5c6 | -11.15492 | -54.87593 | 2025-10-07 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe269ed2-78aa-369c-b286-945245166156 | -10.39647 | -50.30871 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c869b55-3f38-376d-986e-36f8e645e3d8 | -10.67389 | -54.69452 | 2025-10-07 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b8ee0d7-5505-386b-a436-c5e8435543ff | -8.52 | -48.23517 | 2025-10-07 04:57:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a95b21b-5302-3c4c-9b59-36971f87a3ac | -14.64886 | -48.36621 | 2025-10-07 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c891225b-78b3-3797-b1e3-1dbdf4e8e3f0 | -12.38984 | -51.08845 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dfcb438-a1d3-3ff8-b3cc-756c7fdd330c | -6.70176 | -62.83952 | 2025-10-07 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d34fd528-ab0c-3ea3-974e-0a40fd5ccc44 | -11.15547 | -54.87242 | 2025-10-07 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 786574c5-6cad-37cf-a3e8-3e3efa899ce7 | -11.67115 | -46.34184 | 2025-10-07 04:57:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32beb5e9-37fa-386e-929f-a1ae6b38433d | -10.39074 | -50.29239 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94dae675-391a-37c3-a751-11c4c2b48101 | -11.25632 | -50.27514 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 133121cf-23bc-32b2-93e2-d13fec187dfc | -10.63163 | -57.6191 | 2025-10-07 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fa85180-9840-3aa6-8add-33e72123b2f1 | -14.73374 | -46.02658 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| eed7b08e-8ad7-3f3e-aa87-77aedcc42e9b | -11.64613 | -46.87365 | 2025-10-07 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f91413c-33cd-3b06-b6f8-669e03dc68a3 | -13.28117 | -48.05445 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3e919e1-1d82-360e-bc70-d38b16df1ceb | -10.99903 | -51.25174 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f40f8f8-8038-3ba5-b8c9-9d21a690795c | -10.34938 | -51.65528 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7daa826-9853-3a02-92e2-af3349313251 | -11.94766 | -51.47615 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5ee85a2-77e3-3754-9cf6-421d77cb78e2 | -13.09671 | -48.01073 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e792a9c8-e95d-37d4-a94d-fdc6f2395bd0 | -11.04072 | -50.91586 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 23f12a14-72b7-305d-909f-f3d9eed55565 | -9.33339 | -54.51653 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 962f5c8c-5758-31b4-ab0b-b8f617eb09c8 | -14.6436 | -52.53343 | 2025-10-07 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98f918d3-445f-3178-b32c-f0cedba9387c | -12.99155 | -46.78854 | 2025-10-07 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60b80fa6-9422-3d65-b2a4-a8a93d918721 | -12.38255 | -51.11211 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README96.md)
