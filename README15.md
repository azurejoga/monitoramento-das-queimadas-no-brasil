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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62a5cd27-b162-3b25-939e-50520980d18b | -17.16969 | -45.90033 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cb00663-10c4-3299-9e74-2fc62f731278 | -9.51126 | -48.13555 | 2025-09-19 03:55:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72015179-dd60-377f-84dc-71e24c202805 | -16.01429 | -42.36442 | 2025-09-19 03:55:00 | NOAA-20 | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| be15a525-5e98-3041-bf0b-109bc0b4661e | -17.23533 | -45.95731 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3ac9c70f-a6e7-3053-aa14-b8e332205f1e | -11.21541 | -49.64154 | 2025-09-19 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fbe5148e-964a-3209-9cb6-d63e7347d200 | -10.30521 | -50.22062 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 56f76abd-65c9-3778-95cc-b65abb1afa4d | -17.45354 | -44.78978 | 2025-09-19 03:55:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f320bcc0-9526-37a3-a796-30cd49f4800c | -15.70458 | -41.74954 | 2025-09-19 03:55:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 83f361a4-119d-3e8d-9b43-b6990091e171 | -12.61884 | -45.0694 | 2025-09-19 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5deef08e-3ba3-3d4d-aae4-8e03f32e80cc | -13.3361 | -40.46371 | 2025-09-19 03:55:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9f4e6b8d-0cc3-3494-b746-1ae4c71232df | -10.04262 | -49.20027 | 2025-09-19 03:55:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 912ff26f-1dec-3114-a551-e140d81d35db | -14.58402 | -45.16693 | 2025-09-19 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e053e7d0-1cf1-3e15-874f-b73cde6b5503 | -10.30284 | -50.2165 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7e6cb341-5b3f-3570-aefa-39d72e55141e | -13.98317 | -44.97935 | 2025-09-19 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1613255b-575b-3d27-850c-40c1777d6428 | -17.33702 | -46.8188 | 2025-09-19 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59d26f9e-bac9-39e4-b3d3-419f13aa56b9 | -10.28813 | -50.24471 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3a2f9664-fbdc-30b9-b4af-2fc431c7f027 | -17.35126 | -46.81233 | 2025-09-19 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa551c9f-540e-338c-a99b-f09dd427138e | -10.93504 | -42.85131 | 2025-09-19 03:55:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c339da05-2191-3ae4-8938-bcf329cb4128 | -17.20279 | -45.95441 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7d53686-db10-3886-a40a-0d559104e530 | -16.51431 | -43.55376 | 2025-09-19 03:55:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9c67cd9-c059-3b0f-8be0-cd4e59c7bf58 | -16.11885 | -42.62387 | 2025-09-19 03:55:00 | NOAA-20 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41bb2713-64b8-3235-b80d-ba538a959a2a | -16.53941 | -44.89782 | 2025-09-19 03:55:00 | NOAA-20 | CAMPO AZUL | MINAS GERAIS | Brasil | 3111150 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9992d56-6387-3da6-af09-4e54f69f7337 | -13.78473 | -44.33234 | 2025-09-19 03:55:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8eb1c799-a55b-3b8b-a682-83175197b175 | -15.63682 | -39.13783 | 2025-09-19 03:55:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 087cdb6b-cb85-3462-9e2b-d575387da43e | -15.47866 | -43.58065 | 2025-09-19 03:55:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5b73743-0af0-3c79-bb8e-cc612ef229db | -12.14961 | -44.9544 | 2025-09-19 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90b7bad5-63bd-3af5-8fc6-b83cf23170d3 | -13.96032 | -44.54692 | 2025-09-19 03:55:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da49632e-fe6c-366f-801a-d5d3bec78b55 | -14.30345 | -45.1512 | 2025-09-19 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f578d02c-8625-30aa-80c6-7a02010e24fa | -10.04464 | -49.20034 | 2025-09-19 03:55:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8be5c02-c593-3427-8658-003e3a9b27d5 | -17.16148 | -44.78913 | 2025-09-19 03:55:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 26851057-d71f-3ff1-b135-f12475d4d719 | -10.67267 | -46.44666 | 2025-09-19 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed30fea7-c9e5-377f-8e00-a83bb6930e39 | -13.7041 | -42.4291 | 2025-09-19 03:55:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0b7662b5-3382-33ce-a9e0-8f46a4a7c9f0 | -12.89441 | -50.536 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5dcf560b-8a95-3890-a9d8-cb287060aaf7 | -11.20491 | -49.63537 | 2025-09-19 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| faeb3fb1-447a-39f9-bf89-cc556bc346cb | -11.97953 | -43.37712 | 2025-09-19 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dee85dd-15f5-30ec-8944-4f63a9081271 | -14.5791 | -45.17157 | 2025-09-19 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f28abb4d-1701-3837-9200-1d51c50ff4c4 | -12.09094 | -44.83752 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2137c74-fe2b-3f35-a4cd-88fa46a472f3 | -17.96063 | -39.71118 | 2025-09-19 03:55:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4715dca5-ec4b-3da6-8459-d6d743b0d853 | -17.22073 | -45.94683 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 499751ad-a446-3a34-9833-d9e29916aec6 | -10.28595 | -50.2406 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d5f449fd-5898-3cfb-9078-f07e0ec293df | -17.22007 | -45.95039 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 84ae8ff9-51fa-370e-825a-ed54d9d33b5e | -10.30434 | -50.22503 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 7bdac96a-43d1-3b6c-b59b-ef8c53282c79 | -14.60903 | -41.04399 | 2025-09-19 03:55:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9dce7c38-fef4-3384-acd5-75d9141d54a4 | -12.41429 | -44.71505 | 2025-09-19 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06716351-6109-3883-b99d-ac4ea6301467 | -12.15303 | -44.95879 | 2025-09-19 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a36334ba-7651-337c-9f5f-2caa9312845e | -12.92245 | -50.54638 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0530f24c-a677-3c1d-b82d-cf06933778e4 | -16.51456 | -43.54847 | 2025-09-19 03:55:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 89798479-b0d9-39cc-826c-154931ddecd5 | -11.21204 | -49.62875 | 2025-09-19 03:55:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5edd4462-4d40-3986-b96f-3ee4e1c80f8a | -15.44359 | -45.44626 | 2025-09-19 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9d903a0-c0df-3292-a2ab-4a273c7d0eda | -11.50394 | -43.62051 | 2025-09-19 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 573afdb7-b1b6-3e8d-bf29-4faa14828d35 | -11.98063 | -43.38021 | 2025-09-19 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27de317d-f0e9-3f92-8178-4bd45e326b57 | -13.16859 | -44.59822 | 2025-09-19 03:55:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cae1a47c-7790-35b5-9a90-1117170688ed | -16.31042 | -43.10908 | 2025-09-19 03:55:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f7f7ee76-7aa7-3d6a-8897-1d23487c78bc | -11.41677 | -41.40916 | 2025-09-19 03:55:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52b8b594-e973-3e58-9ec7-0e5fc52a8261 | -17.35105 | -46.81358 | 2025-09-19 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8d7be94-29e0-3bac-9684-fcf9ea812eb1 | -13.98635 | -44.99469 | 2025-09-19 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e403cafb-9d43-3660-a73d-f03092013621 | -11.19377 | -45.38167 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8067f81d-654b-3a01-8e75-457ca323b3ee | -10.289 | -50.24029 | 2025-09-19 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ba93e1e3-e0dc-326b-9bc6-3c8086a0d07f | -11.1798 | -45.36734 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c769ce4-855b-3587-8510-0c642097b6d2 | -12.08691 | -44.83668 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72216775-cd2f-393e-8750-86bbfc4a85a0 | -13.12517 | -41.05169 | 2025-09-19 03:55:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 1fb9cef0-db9c-39b3-858f-eda19b66af87 | -17.23068 | -45.96011 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2965b07-0142-39f4-a056-d6680184a6e4 | -10.48165 | -45.15894 | 2025-09-19 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b8f7ed8-a072-3ff5-a435-70de958ad8f6 | -16.5181 | -43.54913 | 2025-09-19 03:55:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 619a12c9-40f7-3ebf-8415-8712764439e3 | -12.08952 | -44.82198 | 2025-09-19 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f79b5ea-2f29-3b8f-9857-2aebdf17dfab | -17.33625 | -46.82293 | 2025-09-19 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7606aae8-cbca-328f-a841-cb7cdf3b6569 | -14.69816 | -44.35833 | 2025-09-19 03:55:00 | NOAA-20 | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e04224b9-b25e-3dc0-a276-ec9feac10c56 | -17.06091 | -45.96882 | 2025-09-19 03:55:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9ac107fc-69ca-34a5-bf75-9c9a92f97172 | -11.18408 | -45.36793 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95a4e0f0-ca56-3c18-8887-20fee2159172 | -17.16562 | -44.79271 | 2025-09-19 03:55:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b793e69-832a-3f47-b552-28dc4dfbc249 | -17.34564 | -46.79566 | 2025-09-19 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd2d1fb0-ee0f-384d-b755-e191ccb19cff | -14.13291 | -44.59179 | 2025-09-19 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c52dfdf-be85-3a9d-8cbe-310d47f9d3a3 | -17.23135 | -45.95647 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 313dbd2d-4af5-32d3-ab90-60d69ea6fb44 | -15.02541 | -42.14787 | 2025-09-19 03:55:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 377446c4-cf73-31e2-994e-0fbc30ac8a8b | -11.43628 | -40.66037 | 2025-09-19 03:55:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0730c914-5caf-332c-9111-98871ee2d243 | -16.42539 | -42.50998 | 2025-09-19 03:55:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9014b3e2-c9ad-3615-87f0-472bf6146af1 | -11.9814 | -43.37576 | 2025-09-19 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45a61537-9cb8-3408-90a9-51cfc68cd503 | -10.92211 | -45.65541 | 2025-09-19 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b970857-3a2d-3fb3-9622-de77350f7a4b | -12.88697 | -50.54314 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bb61057-5e50-396e-8604-24ffdbad5352 | -17.20278 | -47.34609 | 2025-09-19 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 676cc248-92ce-3af7-bfdc-0e39c7e1aeef | -12.88203 | -50.53771 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 12856dbb-2115-33e2-84b8-d0c8f51b0651 | -13.64986 | -44.26479 | 2025-09-19 03:55:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b0fd95d-7ede-3423-bcb5-f6980a3ee3ea | -17.08471 | -43.33421 | 2025-09-19 03:55:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f966e08d-ee07-3664-909b-7f5fbd349f21 | -11.44703 | -43.54237 | 2025-09-19 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b26b12d9-c3c0-3f3a-a7a4-7ace3df8fa56 | -13.71945 | -43.1772 | 2025-09-19 03:55:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9dcd958d-efb3-3d99-ae28-1544763f6bd5 | -17.16065 | -44.79385 | 2025-09-19 03:55:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c9cb83fe-46a0-3333-b260-15e895d69006 | -11.93057 | -38.3347 | 2025-09-19 03:55:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2058cb97-89a9-3f2f-afda-16795da32343 | -17.21478 | -45.95667 | 2025-09-19 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff5dfb8d-6142-3f1e-b1f8-717165c43cb8 | -12.14683 | -44.94647 | 2025-09-19 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f25e2ad7-2622-3965-ad73-31bf72babdb5 | -11.77982 | -40.90596 | 2025-09-19 03:55:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7b2ddb27-01b7-38b7-9711-e30a81354799 | -15.88126 | -39.00112 | 2025-09-19 03:55:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e1f0bcd7-84b9-37d4-982d-23718895dbe6 | -12.8812 | -50.54189 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 72a35ff3-e05c-3d4c-a3ea-e332ab2913da | -17.06275 | -45.91273 | 2025-09-19 03:55:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d778e31c-7117-3203-ab77-a66fa530436a | -10.66928 | -46.44541 | 2025-09-19 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 563d4c74-e746-38ec-b152-5ea5cfefced2 | -13.59466 | -42.49643 | 2025-09-19 03:55:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f630e58b-d2c6-3069-9bd2-4bb078ba6af7 | -10.22889 | -44.99305 | 2025-09-19 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48aa77ca-b21a-3d7e-ac25-ab64e5a013c0 | -17.08265 | -43.34648 | 2025-09-19 03:55:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 405557c5-1faa-3e4d-b865-0ca4bfe4fd82 | -11.46888 | -43.55117 | 2025-09-19 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f46cdb86-27da-3a56-bdb0-e6ebad8baab9 | -12.89191 | -50.54857 | 2025-09-19 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82aa0bc9-af1d-3ca0-abf3-bef1a9e6578c | -10.64599 | -44.23395 | 2025-09-19 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README16.md)
