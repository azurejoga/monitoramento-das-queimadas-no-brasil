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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca21c836-f775-3cd2-ad2f-7fbd31d5e243 | -11.83248 | -45.0783 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c603853-8701-3b2c-9366-2752f968665d | -11.13504 | -47.9302 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53c56a31-9a55-381f-ac0a-b48b64708689 | -9.99986 | -48.29687 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 50743d02-39f4-3b68-ab85-f92f8f785335 | -9.1405 | -62.3695 | 2025-10-05 05:14:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49944fba-21aa-3d00-bed6-6a55e00632f4 | -8.61398 | -54.97058 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 449ef25e-aa2a-39e6-b907-cb2354d6103e | -9.84526 | -60.27305 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 712d7489-73d0-300b-89d3-e04b817aabd8 | -6.18784 | -44.62085 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e1dcc457-c338-38d6-b2ec-b61d464a3a17 | -11.80977 | -46.85634 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0c722ab-0cc3-38f3-b485-2ce0ba5adb58 | -9.01618 | -58.98774 | 2025-10-05 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d52bd671-1892-3919-bd0f-fc444c2b27f9 | -10.58056 | -48.69046 | 2025-10-05 05:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5005d756-90ba-3afb-bf28-b6d0b01a380e | -11.0989 | -47.73696 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10b887f6-c013-36d6-ba81-8780551fc52b | -11.07767 | -47.91221 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc4c867b-9cb2-35a1-9365-61ce86bb7407 | -8.5837 | -46.29677 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 96842699-0371-399e-9eb4-f22edbed44c1 | -10.05735 | -59.35428 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 162d5f96-37a7-3cde-be76-672c7c3d4172 | -6.16175 | -44.59307 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 10709afe-638d-3346-843e-df698f651cb0 | -10.39266 | -45.41381 | 2025-10-05 05:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da96a251-ce84-35b8-9c44-be80d997b919 | -10.84671 | -47.19946 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67dd98b7-e2fe-3ef4-b10e-407af3aa24bd | -10.45634 | -48.37753 | 2025-10-05 05:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6277bdd-1662-3420-8893-3184562106b1 | -11.15152 | -47.92613 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e154f09-e77e-30a2-9649-698aacf60593 | -10.94761 | -47.08948 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eebfa85f-26fc-3f1b-8a9e-0bc3c553e2c0 | -9.83769 | -59.46655 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e609c749-d740-365d-be36-1f4b028ac587 | -9.3013 | -45.98951 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a6bbbff-39cd-30b2-af5f-cd1195ff178f | -6.15929 | -44.61112 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 507b3007-c300-3fef-a585-4d6711bdd765 | -6.17431 | -44.61915 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3a6c8392-f52d-375a-9594-6806a1e3fe0e | -7.43562 | -46.51489 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 270ab927-24d7-36ca-96dc-dcd2b2c15ba7 | -8.57918 | -46.33143 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 4e9ae84c-f2d9-3b78-901c-7267d4a77520 | -8.5913 | -46.309 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 35a56e21-03b6-30ad-a56f-cf33477654d2 | -6.01485 | -44.02472 | 2025-10-05 05:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa298635-86eb-3adc-9711-54886f5b17b8 | -6.17033 | -44.63105 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b41c1c99-256a-3813-9a1e-75013fcc6c30 | -10.5005 | -48.10874 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30aae83d-7f77-3aa5-b591-ac97a63c2a45 | -8.57355 | -46.32565 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| b8d0c2da-d181-325a-a656-7b7ca265a72d | -6.17021 | -44.58161 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 93455304-22ea-34ef-8f70-57f94933fc96 | -9.60406 | -57.75172 | 2025-10-05 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc900a11-1c06-3d8e-81d2-24f9a901030b | -10.46545 | -57.50442 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 11b008d4-370e-3477-a1ad-f846b831afbb | -10.80958 | -48.8221 | 2025-10-05 05:14:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| daa777d2-9ff4-3c29-bffc-cd08228f0318 | -10.80408 | -48.82133 | 2025-10-05 05:14:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5466b04-0eac-34b5-b52e-b3e6a0151e8c | -10.8466 | -47.97637 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56969ce3-e755-3f14-8fcf-a44a98082d24 | -9.57359 | -46.12558 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 736b3d67-809d-32ee-83aa-401095ec1cc1 | -6.17698 | -44.58252 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8115c852-ed79-3f10-88c8-79a6aa6afd37 | -11.58039 | -46.77457 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a83fc2a0-c23a-37d2-a25a-1ff2200c87fa | -10.3515 | -48.1676 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 80177635-3db0-33a4-9dfe-7d1691345d0c | -8.60002 | -46.29025 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0cab7159-ca8b-3955-82b4-14d8bb091bfa | -7.31612 | -45.55943 | 2025-10-05 05:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c043fa8-5884-3806-a24c-7e05684e6f66 | -11.11241 | -47.20938 | 2025-10-05 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d47cb3c-1fdb-38fe-b535-04893f4115d2 | -10.35188 | -48.16459 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bcf691d0-9577-3031-9bd4-5870cba6872d | -8.57981 | -46.3266 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| e2f1d108-124a-3c99-93f1-f0f48015375c | -5.00733 | -47.2169 | 2025-10-05 05:14:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97d00eb4-28cf-3074-a24d-950aa5c94b71 | -10.466 | -57.50085 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd10ec08-e809-3fa7-8d9a-f931233dc2b1 | -11.81352 | -45.05598 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7a1d15aa-0264-3263-a979-1f5cae8fdedb | -9.8371 | -59.47016 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70192506-1b87-3c10-8c06-d29eae95c881 | -8.58867 | -46.30766 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f72179cb-7b4a-3a9d-8b36-49678ccbb94d | -11.23326 | -47.795 | 2025-10-05 05:14:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9d3ad4f-b4bf-3505-a586-707d7f31bd70 | -6.18592 | -44.58298 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71788b61-0ea8-34ae-a087-92649b7967e2 | -6.60419 | -48.05398 | 2025-10-05 05:14:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49ef5be5-b54c-3977-9c39-042f2e3d075d | -11.83418 | -45.06276 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6a90af4-357f-3e2b-8f63-1cdc0d900a23 | -10.80912 | -48.82568 | 2025-10-05 05:14:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61b80bba-3fb0-3181-96a4-1bc58b91a08e | -10.39342 | -45.40718 | 2025-10-05 05:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33ebf8e8-ec27-3598-a873-4e34e64affaf | -11.4889 | -46.78724 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 453bb15d-b6f9-3953-8ee6-08fd407dca14 | -10.10892 | -55.96537 | 2025-10-05 05:14:00 | NPP-375D | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 779ccfc5-6bba-3b29-b582-8a70cdf2bb9a | -8.61337 | -54.9747 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 064365bb-3e0f-33d8-ad6d-51491bcf8504 | -4.91542 | -48.0207 | 2025-10-05 05:14:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdff7346-732e-3175-87b2-c83a2ff90186 | -9.8041 | -56.16765 | 2025-10-05 05:14:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e786fcc-66f7-3430-82eb-0bbaf3369f89 | -10.0471 | -49.20609 | 2025-10-05 05:14:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c7a292e-241e-3da4-bd43-03661efe4375 | -9.3452 | -54.52829 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1a0d197-4f48-3936-be58-f9d61e5c086e | -9.04983 | -47.01867 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fcc62f7b-37e8-30ce-af74-fb2c02f16f4b | -11.45818 | -51.51507 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 026a1274-b29b-373f-8322-69826817c524 | -8.62947 | -54.66522 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30095d69-a839-3834-9680-d76fdfc470cd | -11.54556 | -47.68736 | 2025-10-05 05:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ef08e09-4f48-3c40-8d74-1210b4aa80be | -5.65056 | -43.91753 | 2025-10-05 05:14:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d2390c0-19f5-3888-85e7-72be31d50962 | -11.815 | -45.06257 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 35f58a18-3d77-3c7e-b6b5-2319f9fe587a | -6.1827 | -44.60759 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 099a22bb-32d5-3070-a3d4-c47047549851 | -10.84117 | -47.19384 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0115f780-e3a1-3e71-9aec-920688d31fc5 | -11.45691 | -51.52472 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c604af7-b362-3354-837d-e8c92a5662cf | -11.10485 | -49.8608 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 129854f9-55cb-3b09-b0ec-2a3941792d66 | -6.18033 | -44.6083 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f7aa2c2-e112-3d2b-b3c5-d2b70d0b7fcd | -8.51637 | -50.03006 | 2025-10-05 05:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1fffe12-34dc-38ce-893f-e44563c3f53f | -9.38174 | -45.87037 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83d952c4-2ca9-30b0-9c8b-c32285d14c25 | -8.43502 | -70.12301 | 2025-10-05 05:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf378c6a-ce4a-302d-b8b5-b52122980b78 | -6.16259 | -44.58689 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 13ed5058-abee-392a-95e9-0fdd62fc5006 | -9.63883 | -54.31097 | 2025-10-05 05:14:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ddcb6ca-438e-3362-8f87-85ea093f52ad | -11.05813 | -47.77586 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b358b5ae-5f6f-35ea-bea4-5335de4cd4da | -9.27641 | -45.66642 | 2025-10-05 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d703ec3-3b57-3621-8c68-f2a8bf1e09f8 | -6.16092 | -44.59915 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ff024bf1-a65d-3be6-817b-f5af2f99cb2e | -10.01809 | -48.28899 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b39b765b-60cd-363b-bb19-be0faab502bf | -6.17307 | -44.66109 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e9c331c7-eba7-3856-b204-c2c427115b6e | -5.83856 | -44.44948 | 2025-10-05 05:14:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| aaac4289-fc80-3c70-ba44-5e9e4b703977 | -10.84517 | -47.98806 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3c8cae8-8508-3288-8380-06e07a3c0e5e | -9.29068 | -46.02262 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 211bac4c-7343-3f6d-ae43-72754093bf54 | -6.14937 | -44.63343 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9803062f-7097-39e1-8b6f-792f6107d9d5 | -11.49326 | -46.78725 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d9a0a80-09c5-369b-a5e9-b443ffe4bcda | -6.25079 | -45.33806 | 2025-10-05 05:14:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c0a12495-49d2-352e-813c-80b355595bd3 | -11.13556 | -47.92603 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e7605fb-e7be-3289-86cd-33ab0fead3b9 | -11.83322 | -45.08998 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1fbcd40e-55ea-31c8-9058-73b0be653313 | -11.0729 | -47.90234 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 712d393a-16bd-39f2-89ef-8ce74b95e484 | -10.99996 | -46.5259 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8572d300-c372-3c0a-aba3-fdd0355f299e | -11.05222 | -47.77498 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08c2607e-6ed8-3978-90cf-2a7776fb8309 | -9.29828 | -45.96537 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90f29af6-6682-3ab8-8b5d-7664162d36af | -11.01751 | -46.70705 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9966ee6-84af-359c-8f10-4ac4c45e6561 | -12.4591 | -44.64189 | 2025-10-05 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d9975b6-a0ba-32aa-ba5d-2d3b6f061dd3 | -9.91203 | -50.19446 | 2025-10-05 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README124.md)
