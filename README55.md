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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 208f8e10-cf98-37c0-b205-97b03e2d77ca | -10.43548 | -46.72393 | 2026-09-02 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| bf6f993f-83a1-3467-b3ec-2c1ec7299725 | -12.13703 | -47.09932 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4aa5f918-db5b-3db4-b68d-d6c59c8608d2 | -9.39174 | -60.56994 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 653bd6fa-65a1-3289-b135-f8e1bc944d67 | -10.96998 | -50.48074 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82d73514-1a8e-3f92-9bfb-9bf2027a8ec9 | -9.02495 | -65.45315 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d62e187-f39b-371a-acda-4c11514375a5 | -10.48803 | -64.32585 | 2026-09-02 05:18:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6d7b2e1-100c-3da4-91f2-158b264797c7 | -12.12614 | -47.05164 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 237206e0-de77-342a-b5e9-1b3a9d4c7936 | -10.9025 | -45.33344 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 11f30f43-f3d2-376d-ba6d-8e68c272f3df | -9.46229 | -56.74389 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3e75297-f2b5-3d22-b59a-e1b881d72ad7 | -11.35339 | -50.62939 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7ac6461-57ed-3255-82e5-be50ff923b65 | -11.2994 | -45.16669 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 525341a9-23ec-3025-a8be-8ee607d48d9d | -9.36451 | -57.05449 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a3c27cb-415e-38e8-8c37-2d45630f924f | -10.37871 | -49.98476 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb8ac5f8-fe0f-365f-b582-1147b0ed4786 | -8.56095 | -63.18732 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 824a0890-6589-364c-b5f4-58e9e1368208 | -9.92836 | -60.49194 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8479d05b-d778-34cc-bb13-e0d5bd7c2a9b | -8.76367 | -62.58643 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 283cfcfb-42f6-372f-99c3-e249599f4fff | -10.78692 | -44.76525 | 2026-09-02 05:18:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b1fd3f1f-ecce-34ef-a091-437ed0869e0d | -10.39313 | -61.24047 | 2026-09-02 05:18:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 974a77c4-a0ad-3b67-9994-1f01ceb7cade | -10.45002 | -46.7098 | 2026-09-02 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73ef9ec8-f017-3f85-b80f-e17bf187de9f | -9.89568 | -58.25729 | 2026-09-02 05:18:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26af6f7d-83f8-3d6e-880d-765d1236c9ab | -13.5545 | -59.74938 | 2026-09-02 05:18:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59c4ae39-048d-35a4-9c81-363a06d3a599 | -12.14276 | -47.10513 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40ccba7c-e3bb-3d82-a858-39e1bd9de0be | -11.6524 | -50.20007 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 943b1a06-d72a-3b2a-b37b-3087cbb701ae | -7.76422 | -61.19545 | 2026-09-02 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9336fa1c-b42f-34fe-b133-fdf98f8b0738 | -9.87769 | -64.9786 | 2026-09-02 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e2e0963-ee0c-3d49-842a-b884db310a9f | -9.38827 | -60.56936 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f4e8128-c47a-3d64-b63c-64b81e90f962 | -10.48732 | -64.32981 | 2026-09-02 05:18:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fa3e674-7889-34d3-a11b-1fc9beab802d | -10.15001 | -58.75301 | 2026-09-02 05:18:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5652a8a-048c-3322-949b-34b99cbe705c | -10.32071 | -49.95239 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7c507e6-a936-3628-922e-5b29943d6714 | -10.98112 | -60.78416 | 2026-09-02 05:18:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2d1346a-a284-370a-911d-e6ab77932016 | -13.55782 | -59.74994 | 2026-09-02 05:18:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45d64343-6f8d-3412-b5cd-11386d27c790 | -10.50211 | -59.61125 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 403c452c-aff3-32f3-917f-8e5db4c2b292 | -12.14739 | -47.14103 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6c6199a6-a151-3060-bfc1-05ff328c14c7 | -11.29936 | -54.06258 | 2026-09-02 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6a337853-673b-3106-8c7b-9db217e34503 | -7.47028 | -63.75069 | 2026-09-02 05:18:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5a8870e-27a3-36d1-8671-dc1dfb10ef47 | -15.36276 | -47.03867 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7173837d-7e80-3814-9794-576d202f1ce4 | -11.30718 | -45.16042 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e12ccc1b-23ff-335a-b199-621d878fc100 | -10.78069 | -44.75677 | 2026-09-02 05:18:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 7ebfa34a-f792-334b-b705-c6d72770f86d | -7.76714 | -61.20029 | 2026-09-02 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd03a61c-a801-36b0-950d-97a464661076 | -10.44054 | -46.73498 | 2026-09-02 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 96cef1d9-54eb-352e-9e04-9431310063fa | -12.14565 | -47.13585 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 19b4b007-4fdf-304c-88fc-4cce3627bbbb | -10.49876 | -59.61069 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbfadcd9-2042-3c00-9f41-4d98a2a7c02c | -9.38891 | -60.56549 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47000234-49e0-3726-9fd0-1a3dabcb07d4 | -9.41106 | -56.98803 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0a4c7f3-dbf7-3760-a436-3e1c96685e64 | -10.04427 | -48.68881 | 2026-09-02 05:18:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45759995-4401-3cb5-8c12-db30a2424231 | -11.3064 | -45.1675 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b4951801-ac5c-3e38-9074-18f68f695289 | -9.08501 | -65.37515 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f83d7c1-b79d-38dc-a3cc-46281b418da0 | -12.12898 | -47.05718 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 85437d95-e1d9-33ec-a850-7fd6dda43f81 | -7.79906 | -62.39058 | 2026-09-02 05:18:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca31df50-179e-3bd3-af03-131a4e26316b | -11.33384 | -50.58646 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f20dc4be-a566-3237-a8d3-88f07ee92632 | -8.77617 | -62.84227 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 957b7977-28af-3186-93aa-c938b34d43bf | -10.35443 | -49.97234 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2c7980f-1e5c-33b8-9250-a031191353bf | -10.32581 | -49.95309 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48c4b0bb-c7f0-344f-b1ad-aa6b39761276 | -12.14859 | -47.13102 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ad6e51fd-c3b9-3d93-9896-d1c62af3a555 | -10.49016 | -64.33829 | 2026-09-02 05:18:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92d2fac4-ed28-3f41-9757-f202ee0913e0 | -12.37036 | -53.1897 | 2026-09-02 05:18:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc82a2d7-036f-315b-8ac4-344126f2979f | -11.81682 | -46.06778 | 2026-09-02 05:18:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6dcc985-f2eb-39d6-937e-651f83a0e135 | -9.05355 | -58.96019 | 2026-09-02 05:18:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85ec00dc-5eea-3f83-95b3-ccaba49568ba | -12.87139 | -45.82266 | 2026-09-02 05:18:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8a98e56e-db74-3ff9-a9ad-a295523a59fe | -12.12763 | -47.09307 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d95f3308-6f2c-3344-81c7-adfc433eec9f | -11.75667 | -50.54832 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c55247da-b789-355e-8e02-7c1d9f799afb | -11.89102 | -63.18522 | 2026-09-02 05:18:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d947362-7e32-32d8-9863-e4147314f314 | -10.91047 | -45.32946 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 4343c358-c6ce-3c19-aa17-7faaf2cd20e1 | -15.34212 | -47.04613 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16b96b9d-62ed-3fc2-8f57-bfed2ea9f077 | -9.37092 | -60.31569 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba603fc2-bb1c-3090-9ea2-18ef2fcac0ed | -11.66376 | -50.19227 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17a9f2a1-91d8-3d12-9804-b7ce0e7fec75 | -12.14112 | -47.14019 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c0af9883-ee7e-3ed6-851f-84b264eb95fb | -9.44145 | -67.45274 | 2026-09-02 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75798403-0085-3de9-be2c-fcdd01aaef63 | -12.13987 | -47.07407 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea16ce5c-f87a-3c60-bcef-8144c73af997 | -8.92978 | -62.3642 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae0e514a-a054-3c53-95be-a25505060130 | -11.33362 | -50.62673 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0e812312-e178-30c6-a3ac-180a511a34a2 | -12.15306 | -47.07046 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3a0c6d1-4528-3b37-9651-79d877696df7 | -10.76943 | -54.04666 | 2026-09-02 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 10f75d8b-83ca-34a1-b977-e304bcff8cb4 | -8.77312 | -62.83652 | 2026-09-02 05:18:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ef4f539-13fe-3cb6-8551-a1b8ae01fd28 | -10.51243 | -57.44232 | 2026-09-02 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14989ce1-fc6d-30e4-a4c4-8e5fcf6b0ff2 | -9.71646 | -54.33204 | 2026-09-02 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e04c4f27-8892-3983-b534-3ccfbef0e642 | -10.45632 | -46.71066 | 2026-09-02 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be47baba-ff19-3834-bdcc-332ca1e8cb0d | -9.46567 | -56.74444 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c23bb81f-93cc-3b06-9ed7-68eee97ad0d3 | -10.3783 | -49.98776 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f045d6d-72d8-3207-9429-d5c9e4275630 | -12.14735 | -47.12085 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 84beb0e0-cdcc-3779-ab22-de03ec7b8f2f | -10.06275 | -59.40405 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 636cfd57-060f-33eb-9734-b9114ad6cc34 | -11.65903 | -50.18852 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d33a51f-5ce4-3cea-af8d-8348a9afd238 | -10.77438 | -44.74886 | 2026-09-02 05:18:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8988054d-e64e-3eee-bedd-9c124f7b5b2e | -11.29858 | -45.17418 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a48082b-a975-3eb9-a6dc-0a748397a99c | -10.73968 | -54.03198 | 2026-09-02 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b2fa656c-1158-3c4b-abfe-c12d3f6f5d49 | -9.47605 | -57.03501 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32f72da1-73c7-3c6b-b239-794a97615d92 | -8.9336 | -62.36485 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37768e23-0b51-3bfe-9f21-58843c0120ef | -12.14292 | -47.12519 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c81ea4f0-6484-3369-896d-200aab2c237c | -12.09492 | -47.09992 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2caa309c-ab3c-3c2f-97aa-dc1ab6d99fe8 | -11.81975 | -46.06615 | 2026-09-02 05:18:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 648de228-b541-3af3-9eda-6446ed219ec4 | -10.68124 | -54.04759 | 2026-09-02 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a8f115fa-914a-33a5-881a-bdd1dadb7b1b | -9.00698 | -65.41933 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43f4848e-79b2-3bfc-bb8e-9b71ec5f941e | -12.37653 | -48.15053 | 2026-09-02 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a1b7a59-ddb8-3024-9846-1730fe4d5417 | -9.03459 | -65.39907 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| edd5c538-fd09-3800-86f0-7b380a30de69 | -9.9278 | -67.84691 | 2026-09-02 05:18:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23782ddd-5503-36a0-923a-7e223a8d2bc6 | -12.14508 | -47.14087 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f2f62b13-fb2a-3c58-b477-a4d35404b2b5 | -12.63149 | -45.06932 | 2026-09-02 05:18:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b02d1e42-e960-36cd-88e8-65f549ab610e | -9.45891 | -56.74336 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e8c433f-7717-3098-aa48-164eb5661b94 | -12.14471 | -47.1103 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 501cb92e-9d4e-3147-ae92-d0e29e28b502 | -12.11864 | -47.06102 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README56.md)
