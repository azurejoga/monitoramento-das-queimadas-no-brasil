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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec605b65-033f-3aa7-b5f2-7063add6e3eb | -11.94301 | -50.61345 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 568232b9-f024-3346-9700-38d1edb133f3 | -11.66843 | -52.20393 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 40d1c8da-2a7f-347f-bcf6-7e37a334477a | -11.83335 | -51.54404 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12a62020-86b6-35b1-bcc9-450c6481553c | -11.66493 | -52.19985 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e056af79-97c9-3486-97c0-d82df53478c4 | -7.54384 | -61.33162 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9936509e-eff1-3778-85b8-2fd8a41f1b3a | -11.67747 | -52.22655 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ff5ef839-22cb-3b9f-9650-5fff761db310 | -11.052 | -52.06192 | 2025-09-02 05:06:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0868639-a1aa-34b7-bfba-005280ba2ba0 | -13.6889 | -46.94706 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 0ada0f94-a0b7-3cc1-95de-27b472389d88 | -11.81181 | -51.44923 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2fe0b08-20bb-3c58-ac21-0cde647c0eaa | -11.51243 | -57.9907 | 2025-09-02 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5f5e46d-fc67-3db7-9778-f4e88e68888d | -14.77074 | -47.49863 | 2025-09-02 05:06:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0511430f-5e8f-3c1c-b9a1-8de90bdeac24 | -9.49745 | -57.80043 | 2025-09-02 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e9285fb-e95b-345b-83aa-edf6e39c493c | -10.44326 | -54.77268 | 2025-09-02 05:06:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d946366a-c4b1-3f88-8e05-dc1c2da845ef | -12.98135 | -48.09777 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d60b7559-7692-308a-a93b-b1e7fd85a1b4 | -9.43738 | -60.57983 | 2025-09-02 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddf18182-618e-3286-a234-fc02af27ed2c | -14.60343 | -48.07003 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6d38a913-4064-3ad4-84fe-e002811149d0 | -11.92191 | -46.45672 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5990ff13-4267-3799-94ae-a1071ad38fdf | -9.75859 | -46.93402 | 2025-09-02 05:06:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec01f3e1-3bff-3401-a63e-2f629cb8e00d | -10.83876 | -45.04012 | 2025-09-02 05:06:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05e42db6-f4ce-343d-a779-0b32b3e3d4e8 | -9.48545 | -46.51605 | 2025-09-02 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c24a1626-debf-3d0d-bf3a-a202551a3ad8 | -14.59555 | -54.57645 | 2025-09-02 05:06:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a15ce10a-ccda-356b-b6a4-fc016fef1949 | -11.89009 | -46.68121 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e8f41b6-967b-3f23-b902-1a11da136f39 | -13.69644 | -46.93254 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ac883189-b238-3682-afdb-7f61d76c5f1f | -11.4297 | -55.18157 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f73bf8d9-e96c-3320-9c3f-b05aebde7304 | -6.9287 | -63.1353 | 2025-09-02 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcf2cea0-16c6-3b5d-904a-3c9abdc45ea4 | -12.94196 | -48.08025 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5214026b-533e-3440-b232-ef577d48df19 | -11.00536 | -46.93705 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62bb383e-7a78-339d-b958-21367152d148 | -8.75804 | -62.43254 | 2025-09-02 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f10962c0-ba52-3faa-835c-5ee3f04eb9e6 | -11.65286 | -52.16932 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e885927-bce7-3b47-a852-c03fb82d0e5c | -10.34242 | -48.14503 | 2025-09-02 05:06:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc493504-2860-3cff-9e44-4ff01a4096db | -11.67641 | -52.20507 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 221ece77-bdc2-3b91-9166-163d50e6fb94 | -14.60778 | -48.03688 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c12f8a1-2d43-34b0-ad53-098f5864e132 | -14.58887 | -48.05183 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dac54c39-b6da-345b-82f1-41f06a7c87e6 | -9.33819 | -55.22244 | 2025-09-02 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a60c19d-049b-3fd3-9183-690c31534489 | -11.00416 | -46.83233 | 2025-09-02 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| bd400719-fea2-3742-a86f-7007466a8fdd | -11.47185 | -50.48537 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44ec22e0-567c-3068-9eca-a75c8a869cee | -10.25593 | -47.52516 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93357ae1-7258-3cfb-80fb-2df6a1727bd2 | -8.86129 | -52.02687 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76fbbb9c-5b78-3357-98ea-1c40c4d31f30 | -13.6956 | -46.94002 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| fa442e03-4eec-3683-97a4-cd14f6649cf6 | -8.68616 | -62.39631 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0b821a6-d9d2-3079-a0f9-b28ad4fa192d | -11.82032 | -51.54602 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40f2523b-d983-378f-a799-69aac42f6b9d | -11.91846 | -50.62815 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0bbd540c-f09a-3764-a6bd-99cd008b2256 | -8.50213 | -63.90884 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ccae071-0814-3615-b13a-639edc15e455 | -11.65718 | -57.35636 | 2025-09-02 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cdf95fed-45b2-33aa-874b-2810aa0e39c4 | -12.93234 | -56.96445 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72f9d849-0f16-3f35-bd0c-34093ab167ca | -10.83907 | -47.44666 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 003da360-abdf-3102-b3ba-78679c29f570 | -9.29993 | -60.92919 | 2025-09-02 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 913d6426-01e4-312b-8e7b-534a02c9d266 | -8.64131 | -63.2708 | 2025-09-02 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec48ffb6-6f64-3ff4-9751-9e43d53cd718 | -7.69488 | -61.10212 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46045814-e751-3286-840e-3b0c6e7628af | -8.73816 | -62.42074 | 2025-09-02 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bed81404-1e69-30a0-8177-d2ec93a9ad9f | -11.17126 | -65.05243 | 2025-09-02 05:06:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1da5c25-e770-3bd2-9e6f-225bffa799e5 | -11.65696 | -52.19859 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| dfb00e98-ca94-3143-9eee-aadb3e320ac8 | -11.84269 | -51.53788 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34d467fa-071d-3bbb-a712-3842d503058f | -9.61715 | -47.83418 | 2025-09-02 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 80651e23-70bb-3405-bd46-07ead0b493de | -13.35973 | -51.73791 | 2025-09-02 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f34df7ca-f0ce-38df-a918-a2a0cc01bd75 | -10.05445 | -48.09162 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 76071179-0418-3b46-a271-58ba1b76b2c0 | -9.0901 | -58.88317 | 2025-09-02 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 52c62fa1-61b8-3023-ba2f-82165d8d3d3c | -9.06789 | -65.42057 | 2025-09-02 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9364aec-bafe-3513-9d6f-74592f38f076 | -11.65587 | -52.17701 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6c33e6a9-ff4c-3cce-a113-fc27b8c6dbda | -14.58476 | -54.54865 | 2025-09-02 05:06:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06aefc12-f6c9-39e3-a130-8fde2f90be10 | -11.21305 | -55.06036 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b53b2bd4-2e8e-3b30-ab38-2aeddce4a3db | -11.93856 | -50.61281 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37f8c833-300d-303c-986b-f7f60fef90be | -11.68379 | -52.15229 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cde2c047-3a60-3ce0-940c-563e0d7132e1 | -9.50528 | -57.79436 | 2025-09-02 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 838f40c7-47a5-382a-bcce-b7bf7536a18d | -11.65773 | -57.35286 | 2025-09-02 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ea7babad-280b-30fd-af1b-88d91c457be3 | -11.66932 | -52.16829 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 064d403c-6562-364f-8ddb-5a3ca6680b46 | -14.62482 | -48.0342 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b2d696e-bd4f-34b8-b5f5-ce79b0911e23 | -10.83859 | -47.45033 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f02bbcb6-f0d9-3e7f-8723-88d014bc55fc | -7.69885 | -61.10278 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09f6aec4-32f7-3ffd-bc77-d791bb903520 | -12.33079 | -45.7167 | 2025-09-02 05:06:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b452f0fe-6084-35f5-a16c-39e96708c548 | -13.30037 | -51.79813 | 2025-09-02 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 722a1afe-0a19-3e49-8419-0869296ce7e4 | -8.75379 | -62.43177 | 2025-09-02 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32ddb150-b5d8-31e4-b8e3-7e1bf5aff98c | -12.88479 | -48.16426 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0930900-63de-3f71-aebd-fe9d3b40d293 | -10.84075 | -47.44569 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eba5e6f6-2d3f-35b9-9d06-e98d76970916 | -7.55072 | -61.34017 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 37fdae15-4b90-3c88-b845-7c4582d82664 | -13.89965 | -48.09926 | 2025-09-02 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89f0a6ee-e83d-3c44-96c3-c88d3c3be564 | -12.59545 | -48.20929 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3572c91-82a6-38ca-9711-4ec7b8ee86f4 | -9.12004 | -61.48817 | 2025-09-02 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 680f86d4-1bf0-380d-bc36-793059a0f29d | -6.92454 | -63.13559 | 2025-09-02 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1bc0770f-d9c3-37b9-b5de-a636f93eb016 | -11.00374 | -46.83585 | 2025-09-02 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| f9664612-e233-3fb6-8084-27c16b5e9d22 | -11.3778 | -43.57063 | 2025-09-02 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e2543c8a-872a-3047-ad7b-4a3f7c386636 | -12.62018 | -48.18308 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 66606b1e-4417-38ef-a59b-5415405dafdb | -10.04697 | -48.10887 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6881452a-de77-329b-af98-44a0c30c7807 | -11.0137 | -46.82578 | 2025-09-02 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 01bfdaac-6c26-3b91-94f5-75bb5d92810c | -11.92366 | -46.45186 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0f22bd97-7a0f-305f-b227-c0a8760e7ffe | -11.67096 | -52.21496 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 493.4 |
| 8c7320d5-c782-3627-beec-366b694ec681 | -10.25076 | -51.12503 | 2025-09-02 05:06:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45120ad8-733a-3a20-8ada-6042c39b170e | -12.91685 | -56.93295 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11c4629f-b4c4-3e04-9443-747b7ad76248 | -8.6668 | -62.83194 | 2025-09-02 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f2f44cee-0b55-327e-8c56-d8991cabaa48 | -10.05403 | -48.09482 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 198dae0a-556c-3845-8d8d-542c0e47dd02 | -11.65993 | -57.3604 | 2025-09-02 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a1f3b762-03ce-347e-93e0-d7f1930ef14e | -12.93561 | -48.0878 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24d36988-e6f5-3f30-bb93-dfb1ef774f3b | -14.61395 | -48.03155 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad7062a5-3886-38d8-80c0-36ada4214d48 | -11.08935 | -44.64325 | 2025-09-02 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 9ee40f7e-9662-37a7-ba97-5699a7560ea9 | -11.6734 | -52.19753 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 87a9ad25-348d-3e7a-a371-811c4fc5afb2 | -14.61358 | -48.03493 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89b544c0-713a-39d7-b815-d97f8014be8c | -12.92293 | -56.93755 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbddb6eb-eefd-37f5-8508-e325a661ab5e | -13.49934 | -47.00622 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8cdffe4-b543-369f-b8b9-0a15d0706020 | -10.04576 | -48.11823 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2041f4b1-008e-3fd3-adef-5fc2cad54370 | -11.97029 | -45.86314 | 2025-09-02 05:06:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README67.md)
