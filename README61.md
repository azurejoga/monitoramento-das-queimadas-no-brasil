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
| d7d4a90f-399a-3bec-9d59-80ad9ee9e55d | -6.86624 | -47.91713 | 2025-09-08 04:51:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 02e0468c-a40a-3256-8e41-2975859a749d | -7.39858 | -61.6248 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0c8adf73-f425-3ff0-ba3b-c83eb6056ba9 | -9.96234 | -51.2078 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7b3a0c6c-e150-3360-b676-63ee1c3a93d4 | -7.56944 | -43.67703 | 2025-09-08 04:51:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc205320-f478-35d3-83e8-46201e3b8274 | -9.18571 | -60.76708 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 87e8719e-e800-3b26-b343-ef840489b4ab | -3.33035 | -54.9101 | 2025-09-08 04:51:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ebd305e9-30d4-38a7-90d7-48884ea96654 | -3.26037 | -52.58643 | 2025-09-08 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3e76149-a5a3-3b2f-a8f7-d8587f326c05 | -7.04087 | -43.2525 | 2025-09-08 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 286bdf05-3235-3199-b694-a6e40b2f7e91 | -8.67988 | -50.03805 | 2025-09-08 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3411e85-cdef-3207-9910-93ae3461eb26 | -9.81771 | -53.32 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4fcf6d87-be5a-35b6-a70c-5f7eb3b6b54a | -7.67188 | -50.25525 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e501cf93-06f8-3ea2-8916-56039c634069 | -6.46577 | -43.95462 | 2025-09-08 04:51:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6cb9b9e3-fb04-38fc-9ada-1acd7dcc00e2 | -5.94346 | -46.16267 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1275ab8-eea7-34cc-9748-c4c82def4d43 | -10.18249 | -46.23558 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c15ab4b-3e37-3940-bb12-ce9b9223901a | -10.00278 | -51.64148 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a961f9e5-4c4a-3ebc-9bd8-cf2ccbd6c0d2 | -9.17077 | -59.38076 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 58b0a160-2895-3269-a12c-278976208561 | -6.54314 | -45.83967 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18ae3717-803d-3600-ad52-c786d479cd58 | -5.6402 | -43.64473 | 2025-09-08 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15f681c0-3d14-3e63-99da-b79bc9cb2ef0 | -7.22201 | -46.20968 | 2025-09-08 04:51:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5815dbf4-5846-3ae2-b5d3-21edf8a05dbf | -5.87987 | -43.97012 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f793dc3-dc56-3880-99bc-7de8e1c340a1 | -9.32744 | -46.53149 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 415ea20f-54a5-3285-abe0-608c59fb1c09 | -9.99427 | -51.67499 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc281044-2502-3ffb-a1a2-19839b8e1ebc | -6.2032 | -43.60738 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b040a858-9cf5-36f8-bdda-cc3a1b8b4aad | -7.98007 | -44.83648 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77bd287b-a747-3b99-86d1-664b649829f4 | -9.04956 | -50.45851 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04ff9788-b6f0-33ad-9a8c-439d6a16254d | -5.91799 | -50.00166 | 2025-09-08 04:51:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81650c8d-5974-3819-8b76-0056103fddfa | -8.20127 | -44.7892 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68d2e0ce-c37e-3b6b-88bc-12e7a030fda5 | -6.97868 | -45.57158 | 2025-09-08 04:51:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0998f28-78ac-3f84-80ba-d3007202beef | -7.55852 | -40.10418 | 2025-09-08 04:51:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e83dbff4-5e8c-35c7-b067-a7339e2fff0d | -11.28768 | -46.45423 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe26b9ab-2e64-39d6-a13c-80c1b0687163 | -10.47334 | -53.60708 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b305668-255e-394b-b41e-39f30e7d42c4 | -7.11216 | -63.06937 | 2025-09-08 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9df86e0c-2482-3933-a02e-564f09c92bc0 | -6.64373 | -44.81213 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 978617bf-3d86-3d24-8af0-f58142ffdc1a | -11.28295 | -46.45372 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90891ec6-90f4-3857-a549-780f7fa4abaf | -6.25495 | -43.6945 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c378b0ac-f095-3a5b-bc10-88e679913334 | -6.20085 | -42.64229 | 2025-09-08 04:51:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 38a54f97-c196-32f4-8aaa-e677b9e7e2b2 | -10.45686 | -53.6259 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 323b7667-a487-3a14-869e-6dd6bda30fb6 | -11.34166 | -46.57261 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbe8f7ae-2c80-3d1c-90be-82cb610d582b | -6.12216 | -44.25998 | 2025-09-08 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e62b0c59-bc3a-3f61-9a35-1e670bbb5a97 | -7.08472 | -45.19753 | 2025-09-08 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 447e0a69-c5cd-3a2f-8cf1-cf47d3c4f2c8 | -6.63803 | -53.37344 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 280efbd0-7274-3371-9a72-665482e82d28 | -5.76999 | -56.51872 | 2025-09-08 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 065a91a6-f338-36ff-8080-79df518e47d6 | -6.29342 | -44.3861 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c39417a-5b3e-36f4-b4c6-66ac995817b2 | -8.18418 | -50.14513 | 2025-09-08 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cc98a4ae-0334-33f3-b5fc-c5fb704f4a9e | -6.40606 | -44.45827 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e35a45f4-191d-3992-aaf2-4a036bdf6f54 | -6.63472 | -53.37291 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1e9106f-c1ec-3ade-a80e-546af00407e8 | -7.59423 | -49.28509 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40bb51a1-ebab-3122-bcb3-8fa78db456ee | -6.12339 | -44.25126 | 2025-09-08 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d319afc-b28f-356d-b9f9-b6032b12ece8 | -7.22329 | -46.20058 | 2025-09-08 04:51:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c63436b-6b5f-3b3b-a006-83c98a8f529c | -5.45971 | -51.41925 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 687e54f9-cc67-3f25-8fc4-481d61e75301 | -4.66237 | -46.35992 | 2025-09-08 04:51:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 283670c5-305e-35d0-bb36-688fab286fb6 | -7.75541 | -50.76065 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3b9dd8c-aa11-3bc8-a611-de9af6a387f3 | -6.19927 | -53.2646 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18535d36-96e6-380f-b616-b855e274f03a | -11.15297 | -45.24714 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07bc9ea7-ff8b-3f5b-b1a1-c5a473ff6a59 | -7.9063 | -61.78427 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3602d657-5147-351f-a85b-8fcdaf652c56 | -10.45356 | -53.62538 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 258b9231-fa27-32a2-aa91-a4d1da806304 | -9.99709 | -51.65609 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b460fadd-ce91-352b-a926-2cf3142ad66e | -6.62865 | -53.3684 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a26857e-98df-3d6e-a575-23593db7c098 | -7.75019 | -50.74831 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 977a9a03-570b-308c-93ad-a16bf046d09d | -9.06964 | -60.48618 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a86b7746-1a23-3245-9a7b-d27563dcb538 | -6.62534 | -53.36789 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b54552cd-127d-3ee4-a035-d34ed774da38 | -9.82213 | -47.77011 | 2025-09-08 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 95464378-84d5-3ffb-8483-e1cb09da0baf | -6.87919 | -44.25793 | 2025-09-08 04:51:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b01c39f9-9a7d-3c7d-b2a8-1b19ba20eef2 | -7.83834 | -52.15561 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1c4052d-b6a0-38b0-8e3c-6f9cef7f35fc | -9.18037 | -46.02667 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e63cc9a6-9273-3785-a756-6abbfb7dcbee | -9.03531 | -49.80102 | 2025-09-08 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bfc7bbcc-c18b-3455-b352-8238c30de679 | -5.97788 | -53.58969 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eedb5c59-079a-3e30-ad54-04bbe24a6fd6 | -9.14022 | -46.0599 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| eb8356b7-09ae-3b83-b37c-08a88278ea70 | -11.33296 | -46.56612 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e4d03f7-5177-3cab-a720-e6fd2e54a433 | -5.75452 | -47.46085 | 2025-09-08 04:51:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ec545d7-bb85-365d-85d8-1277c8e90604 | -9.88341 | -46.53873 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 85ae0d72-0bcf-3c49-b16d-a43f69bcf47b | -6.26686 | -43.68642 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf0041e3-7aad-34ca-83b1-88184fb080b6 | -4.99344 | -56.25779 | 2025-09-08 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 07a3b7cb-4d92-3393-b1ba-902a8f0ee1f7 | -6.25538 | -43.69133 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 158d2a28-c5ed-3635-bc41-abab1a09582b | -4.99716 | -56.25843 | 2025-09-08 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b8b23e81-b8c5-34b3-9849-7ebff2f6b482 | -9.70037 | -51.06668 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f54843dd-79f1-333d-802a-740bf9b6c4ac | -6.74042 | -51.95639 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 579c2cab-28f1-30b7-8746-3e61f89efffd | -10.99902 | -49.77845 | 2025-09-08 04:51:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb12c976-237f-3af5-8451-abc664531a5d | -7.74128 | -50.32312 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 076f0648-6572-374b-9247-2ca2aa3b6f0e | -6.62312 | -53.36043 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5b7f4dd-6cfe-38be-8299-2b99faf144cc | -6.40292 | -42.97868 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85842a9f-4859-39ab-8609-d77d6a424276 | -6.19908 | -40.97366 | 2025-09-08 04:51:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8bd68ed0-98ab-3153-8b3c-cc3811dfd4dc | -7.42894 | -49.25778 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0d04cd00-53db-34c1-a95e-c006ac05c17f | -11.03231 | -45.94297 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 747c185d-9480-36c5-896a-f63aeed4fb65 | -6.20881 | -51.45475 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd2535e9-0688-3fa7-9b3f-f6002dc4f8e3 | -6.6281 | -53.37188 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d29c958a-cea5-370f-9ec7-3dc04d3fea64 | -6.12297 | -44.25426 | 2025-09-08 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 914a7695-6db4-3deb-b5d5-ceb3e7d42636 | -7.74187 | -50.31921 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c78046e4-3dcf-377d-a101-07758dd01056 | -6.97863 | -60.13878 | 2025-09-08 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 47752126-ccb3-3d48-aa18-49ae66791b7d | -9.06237 | -50.46717 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55c6440e-762c-349c-bd44-1ac36bd61a11 | -6.63305 | -53.36199 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 176566db-ba2b-32c4-a5a9-6f8f406d0baf | -5.64527 | -51.80327 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f02e417d-8530-3818-900d-f4370ebd4f77 | -6.44035 | -45.99726 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 157df58f-96fb-383b-b80d-b477a50afaa6 | -6.62421 | -53.35349 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff4051a1-7262-302a-a812-83ed487d505c | -6.84206 | -52.85707 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbf107c3-6293-396f-970a-5aedbb6af9c3 | -4.80648 | -43.54638 | 2025-09-08 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 94915ca5-486f-3d25-9010-6bb71d6f7357 | -9.37892 | -50.38648 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea77a0f8-6fba-3fbe-8028-e347371e9299 | -9.88407 | -46.53389 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ce7e15d4-8c83-30a3-beeb-cf4c6000936d | -6.13616 | -44.23445 | 2025-09-08 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9d0a692-7b91-3872-8e7d-d0b04635f70c | -8.69639 | -45.33184 | 2025-09-08 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README62.md)
