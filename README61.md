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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab12e245-cc17-39dd-beeb-dc07afc000f4 | -11.88964 | -46.68508 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97ac1335-49bb-32a3-aa80-b4a27de3a0c4 | -12.92463 | -56.97044 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 891d8b54-311f-33e0-a33b-0159bb1787c9 | -7.59729 | -61.63759 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62940487-0a98-354a-8493-566df7aa4fd9 | -11.21592 | -55.06466 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a66d3b65-f264-3360-8a64-c8c429344b94 | -14.79159 | -48.18776 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfb01409-590a-3c26-b4d6-7e878cacd5bc | -12.79763 | -48.07745 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9ffa509-c0a6-362d-ba10-fed3622fa328 | -11.67487 | -52.18697 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 32ef30ec-a093-3220-944b-30acbf17b8ee | -9.48077 | -46.50736 | 2025-09-02 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64e55d91-0a9c-36f8-b639-2eef002bf3e8 | -11.84435 | -51.46204 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f8132ff-6699-3788-8ba7-b8658c9c2442 | -12.90804 | -56.94603 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2f56e0f-f28c-3e3b-b330-68b72fb36640 | -12.87234 | -48.04505 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0248fb96-e6d7-3a75-a84a-0c1ea9ca8d6e | -10.83364 | -47.44584 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a20343c7-8adb-3dc0-ac8a-1bc7027edd7c | -12.9379 | -56.99429 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 502cd52d-a0f5-39fc-9c49-06d4466559c0 | -10.89815 | -50.84057 | 2025-09-02 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b02f3c89-c442-3ec5-8d3e-19587975de82 | -9.65524 | -47.03888 | 2025-09-02 05:06:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4375e48-fe8f-3743-acef-9bfd99400b06 | -9.31595 | -59.20663 | 2025-09-02 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 030bb1a0-ad53-3e9b-a279-555736825c96 | -12.98171 | -48.09464 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f5301d50-fc96-351e-aa9e-f2c7472ea985 | -12.76639 | -48.08205 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f04ffb7c-2ca2-3b41-a4db-e3e292426b9b | -10.76305 | -59.83713 | 2025-09-02 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7b73647-9d38-3101-b86d-8b5fcbdfd73b | -8.65086 | -62.60477 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3f862bee-e813-3f56-872d-d68fa76b0cd7 | -12.42229 | -63.90675 | 2025-09-02 05:06:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e139b759-25df-3674-a95d-ebc690ab5e28 | -13.89452 | -48.0961 | 2025-09-02 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7530f8ac-56ab-39da-afe6-7ee4666111f0 | -11.00109 | -46.83426 | 2025-09-02 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d6eee57-a627-3360-9540-23bc74e47e1f | -8.68905 | -62.40516 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 428efd77-3393-356b-b4be-d82d0284cb2c | -13.2825 | -46.89025 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0901078c-874b-3017-9521-3e9fb155d6c0 | -12.92569 | -56.94162 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3928b509-8a8e-340d-b4a8-aa0dba819879 | -9.48195 | -54.42866 | 2025-09-02 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a755858-f0c6-34fb-8e30-081851decf88 | -9.09073 | -58.87933 | 2025-09-02 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aae00ace-77ef-3818-b6fd-892d23ffe96a | -12.97575 | -54.75664 | 2025-09-02 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfe0a2b3-ab44-3a1d-8ba2-90717a9ca341 | -7.5862 | -61.62803 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8eafff09-d3ae-32be-ad67-be2bbbb7e143 | -12.91852 | -56.94409 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d02dfd53-9837-3cae-94e1-02b92560593c | -12.80423 | -48.06758 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00f0a922-3eab-328f-bde8-0e8586e403ad | -9.2613 | -59.75596 | 2025-09-02 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a44e238-6ce2-36f0-a7e1-0db14e126cca | -7.70679 | -61.10411 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a508501-3011-31d6-a47f-0d8e4ad4cef2 | -9.92779 | -51.63108 | 2025-09-02 05:06:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a157e288-3947-3b87-af5d-6edafce254aa | -11.42915 | -55.18531 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1d26fec-791f-3311-b87d-1678e088f1cd | -13.72582 | -46.93456 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b57e1c65-a140-33f7-8069-cb72bfea493d | -11.04811 | -46.89768 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 120d7ac2-67c3-3cb1-93f5-4d2e49d8af5e | -14.49267 | -45.95446 | 2025-09-02 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 62c9c8c2-eb32-31f0-8207-908671026fa1 | -7.4816 | -63.82634 | 2025-09-02 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5ccea4b5-7751-3b76-a08e-453c1acf6ff9 | -11.05599 | -52.06248 | 2025-09-02 05:06:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b75e7bf-9ddc-3bfe-bb26-15cd364e91e2 | -12.85529 | -48.05067 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a170aaa3-2cd4-3e79-ac94-f6a498c9de24 | -10.39242 | -59.41584 | 2025-09-02 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af85f191-a3f5-3998-8a80-ecf52046c587 | -13.09677 | -57.13233 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 680ec461-2985-3f2e-ad34-010304f6fc2e | -11.01019 | -46.83013 | 2025-09-02 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 57e0b873-ac48-3e7a-a85d-f99a494111d9 | -11.65249 | -52.20146 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2bcf40da-a2bf-33ce-9cd5-1360ce004678 | -14.55595 | -48.96022 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56b352f6-b0a3-32de-a793-e9de20097419 | -12.49301 | -53.84002 | 2025-09-02 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0361b316-b767-34b7-adfc-c5d340d24c25 | -7.08565 | -63.18406 | 2025-09-02 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e41ab726-8682-3ce8-8b5e-e34b2313fc0f | -11.4212 | -55.19173 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b8fcd66-e0fd-3252-ba51-c3222d54a641 | -10.05134 | -48.11559 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91475106-680b-3825-acfc-50501179b3b2 | -15.13147 | -48.11256 | 2025-09-02 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bfbb57c-f9ad-3b04-b0e4-d2b43aa21819 | -11.09647 | -44.63876 | 2025-09-02 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| de21058c-d27f-37cd-9937-84f34d669e00 | -11.86146 | -46.71902 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 07cbbd76-75e1-35a9-a85a-b081ba6db11b | -13.68979 | -46.93908 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| ed80cd61-ff59-3f2e-84cf-9e2858b3b148 | -8.72677 | -62.41065 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89babbba-1b70-3d31-a27a-6cf2b73c7f1e | -12.619 | -48.19268 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 89505638-fa44-304e-a330-8505998b2b02 | -14.49366 | -45.94467 | 2025-09-02 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3a5d58d3-7210-3b25-80bf-1b97d59d6c72 | -12.93417 | -48.09972 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49b5839b-5bbf-3bf7-bd6a-50930bb3f6f8 | -11.10107 | -44.65635 | 2025-09-02 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 04007c09-f969-3c8a-9222-aae966b5226b | -8.75448 | -62.42775 | 2025-09-02 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 671dd6e9-fefd-3b71-9883-a4758fb02746 | -12.81616 | -48.05882 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f47370c6-6424-33ea-bee4-12e13472c6c6 | -10.66858 | -47.33603 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a6a13d81-e81e-355d-970b-d73e06f87f1f | -7.6766 | -61.08936 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 005dd053-976e-3f66-8011-0487f720f75a | -9.25385 | -60.49131 | 2025-09-02 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57b1ecc7-86e1-3db1-af06-e90461a0a945 | -11.67185 | -52.1794 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| e13332db-ce01-30c6-a99d-6093722a3be7 | -12.97869 | -54.7612 | 2025-09-02 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8fa63a0-511f-3676-a6ba-0d430530cc22 | -11.64077 | -52.04819 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85bdbe40-f3fd-34b2-8518-739b71ebd24d | -14.23177 | -51.66349 | 2025-09-02 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6265330c-63db-3256-b387-9a30864feb70 | -11.66687 | -52.18586 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 92763255-532a-354a-9a72-f8b3124b409d | -15.12635 | -48.10832 | 2025-09-02 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae520b2f-5459-384d-9ceb-7017c171f85c | -14.48949 | -45.9444 | 2025-09-02 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 642af078-1a29-372b-8c31-dd5a8cbbe048 | -12.99668 | -48.10634 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 65ecb4df-280b-34a1-914e-f7f5bac5bae5 | -11.67242 | -52.20451 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| a2efad98-ac24-3240-be68-fc1807df4d9f | -10.47384 | -51.62177 | 2025-09-02 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39ee8b77-396e-31a2-a305-c27cfd52199f | -10.05564 | -48.12278 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87d9da85-a977-3f72-a9af-82bde875617c | -8.73886 | -62.41668 | 2025-09-02 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ad561a6-8709-3dc8-9153-18ffaff4d572 | -12.06987 | -45.81348 | 2025-09-02 05:06:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87f9aef8-6e71-34f2-81a6-6652672bb91d | -12.92408 | -56.97396 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4aa0323-7033-3ca5-ad10-4efb42e68511 | -8.697 | -62.40548 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b44c83ee-10ce-3d55-b268-e2d2f706d02e | -12.77829 | -47.66531 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d9a624c-0878-3149-90b8-4c0ac2e9e018 | -11.75991 | -47.8319 | 2025-09-02 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34049142-b68c-3897-a4ad-8202b199f679 | -12.75698 | -44.41275 | 2025-09-02 05:06:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f148a716-f8d7-35ff-ae8c-212e005a58e2 | -14.58297 | -48.05986 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb1af6ee-e469-3726-93af-38d768d5c35a | -11.91903 | -50.62368 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96e4a6a0-3850-3b13-a844-31365ee26deb | -10.45355 | -54.77436 | 2025-09-02 05:06:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ccfda04-fb58-3725-b192-6f232315c7d3 | -12.93675 | -56.95791 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52dd642f-ec7e-3f81-b4b5-831480abdb19 | -8.55869 | -63.01236 | 2025-09-02 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27938ee4-6f63-3ea0-8353-d8dd0cb48ffb | -11.67585 | -52.17994 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 06d2b175-fe4e-3b18-a4e7-5b7c417c0c08 | -8.67763 | -62.39499 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a091768-552b-3e7a-a3ed-ec9acfaf17e4 | -13.69066 | -46.93124 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| d931035c-c29f-3b83-a7d6-8253faec290d | -11.97043 | -45.86794 | 2025-09-02 05:06:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e682953-00ad-3a01-a9c9-ed708d2a7ba3 | -11.16796 | -65.05555 | 2025-09-02 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2958543-6243-3afe-95df-805e3cae749a | -9.49965 | -57.80811 | 2025-09-02 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09cd37bb-d1f6-39a5-8f64-b0a5aaa2e14e | -10.83226 | -47.45657 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f54d9a82-5cef-3303-889a-2894015152bb | -14.60171 | -48.03736 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 875ee1ee-0b4d-381a-8afe-19d409af13d8 | -9.35121 | -65.44384 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30c58780-68c8-3966-811d-70dd607ad56e | -11.64126 | -52.04458 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e74677e-6c64-3f7b-a643-b68a2b442c0e | -14.58762 | -48.06248 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1797b861-ba9e-376b-96ac-1a0a5fac9720 | -12.97517 | -54.76068 | 2025-09-02 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README62.md)
