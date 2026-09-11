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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79b0cf8f-8a24-363f-ad35-0d4829866698 | -13.2088 | -61.8338 | 2026-09-11 15:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 91.6 |
| c9c1335b-2970-3676-b02c-297dfa8ba774 | -13.3623 | -61.6683 | 2026-09-11 15:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 3a71c422-8d74-35f4-ad44-caaa44c77dbe | -5.9817 | -57.7282 | 2026-09-11 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| a29bd72b-77c6-3d0b-8f1e-04c210e24009 | -13.2863 | -61.6734 | 2026-09-11 15:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 26b2554e-ec44-34a6-a4fb-182129a6e5bd | -9.1512 | -66.0672 | 2026-09-11 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| d32f0899-6996-31ad-a624-2d52f441ecdb | -10.4722 | -51.3442 | 2026-09-11 15:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 78636ae7-f65e-3bf8-9acf-15e6cbc98aa2 | -6.2427 | -51.7146 | 2026-09-11 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 56258cb4-025b-38b4-9e27-220b0d0f99a3 | -6.8062 | -58.6469 | 2026-09-11 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 21237eb0-f1be-3300-8e4b-2b2fb1137667 | -10.5478 | -51.3367 | 2026-09-11 15:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 442e03c7-4f20-3237-aaba-978c9b9d7dcf | -13.4198 | -51.3731 | 2026-09-11 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| c62639f8-533b-305f-babf-008f2210cf70 | -13.2105 | -61.6591 | 2026-09-11 15:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 13044ebc-82db-360e-9a0a-12f05cce8a9e | -6.1993 | -55.2739 | 2026-09-11 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 212.0 |
| fc7ad43c-ae0d-3ea7-95bb-2456575c405a | -6.4045 | -54.9842 | 2026-09-11 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 7b2e32ea-a47a-3288-8704-bc0a5e2a1664 | -8.6311 | -66.5287 | 2026-09-11 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 847eafcc-1b39-3e8e-bffa-375331da2992 | -6.6226 | -58.4995 | 2026-09-11 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 335593d3-cd0f-3337-8da2-884a662c6a74 | -11.2488 | -54.1378 | 2026-09-11 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 174.2 |
| 33222a66-a2c4-315b-826b-94bcaba75676 | -7.5553 | -45.1624 | 2026-09-11 15:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 169.1 |
| a53a0ad3-a496-30da-9105-873e8bf8ca5f | -6.325 | -55.8451 | 2026-09-11 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 7b210984-6c66-36b1-87ae-16079f4b68e3 | -8.0748 | -54.8499 | 2026-09-11 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| b1c50285-2779-35c5-8745-1895b0b7ab0f | -9.9045 | -45.8873 | 2026-09-11 15:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 22f19286-4397-3bf9-95ac-c51c32039e8f | -3.1697 | -58.6437 | 2026-09-11 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d9b79386-cec7-3c6f-98b1-d1a101ad9781 | -5.802 | -53.8264 | 2026-09-11 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c147c991-e9e4-3c0c-89ec-e997cfcb2604 | -6.5853 | -55.614 | 2026-09-11 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| eefe7726-6496-3a07-a22e-cf0b5791ed73 | -5.6314 | -51.6444 | 2026-09-11 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 5588b113-2b59-3107-b838-c5c1f9a0c73f | -10.7359 | -46.1465 | 2026-09-11 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 177.3 |
| c3c71b50-e673-379f-af07-49058f18a453 | -11.3513 | -45.7922 | 2026-09-11 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.5 |
| cbf64877-e01d-358e-a54a-f07364afe7ef | -5.6313 | -51.6651 | 2026-09-11 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 0779d619-c129-3db0-9e40-3696e9a480cf | -13.2297 | -61.6384 | 2026-09-11 15:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 54819f3a-21d4-3450-933a-747a9e9738a3 | -10.2559 | -45.2292 | 2026-09-11 15:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 407376b8-f69c-365c-9160-6231bb68b600 | -5.963 | -57.7874 | 2026-09-11 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| c4ea1aae-8dc2-3942-82bc-131b2716bc4e | -13.3038 | -61.8275 | 2026-09-11 15:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 0f911d8f-e941-3674-a9bc-97ac09a2b833 | -13.4198 | -51.3731 | 2026-09-11 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| c24cfa26-e473-38c2-99bf-c51a0952b3cc | -9.9041 | -45.91 | 2026-09-11 15:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 142.7 |
| cb1ced77-ab07-32bc-9c3b-383444e539a0 | -9.18 | -68.2009 | 2026-09-11 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 72d334b8-791e-31e4-b785-f72a75e41201 | -8.2015 | -55.2639 | 2026-09-11 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 24cfbb9c-93f4-3d23-a026-f82a0dae8556 | -9.6038 | -68.9491 | 2026-09-11 15:50:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 6b94ab51-f948-33f1-aec2-182fa5bf8047 | -5.963 | -57.7874 | 2026-09-11 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 61a83aa6-d0a6-3dcb-9f8d-7cd089783f86 | -8.2201 | -55.2627 | 2026-09-11 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| ff8d82a7-07d0-3f3a-bf32-78a8ca67308f | -8.6311 | -66.5287 | 2026-09-11 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 39e3d267-fbc2-3cbe-bccc-a65723088fc4 | -11.3513 | -45.7922 | 2026-09-11 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 7c56c84c-457b-3fa6-aaab-f421d1957096 | -3.1697 | -58.6437 | 2026-09-11 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 1b216326-d7c0-3255-b3f3-e9cf1af1be79 | -10.5475 | -51.3578 | 2026-09-11 15:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 266.7 |
| c990478e-a80d-3fff-9944-31b20968af94 | -13.249 | -61.5983 | 2026-09-11 15:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 2690274f-2eb9-30f7-b9db-9bdd5b205d64 | -8.5322 | -63.8604 | 2026-09-11 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 3a32cd57-6f76-3482-b84e-b0ffcc58b508 | -6.5853 | -55.614 | 2026-09-11 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 80f7fbf3-7420-30c8-8e46-6c7f4f91a26b | -6.641 | -58.4987 | 2026-09-11 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 44c4212f-82bd-36d0-94c4-c544b5743190 | -10.4722 | -51.3442 | 2026-09-11 15:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 12dc0eea-de84-34c1-8ac0-0cb4f0488032 | -5.9814 | -57.7867 | 2026-09-11 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ba8c088f-ccfd-3c8e-8ccc-c8c3e73c79d4 | -6.7263 | -45.4846 | 2026-09-11 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 70a98d58-7ff7-3d30-aa42-abf63aac4eac | -5.6313 | -51.6651 | 2026-09-11 15:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 768b1863-c20a-37bd-a4d4-b7a03adfeccf | -5.802 | -53.8264 | 2026-09-11 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| bd662e97-ae8a-365a-a722-2d9a5f4cb256 | -10.2556 | -45.2521 | 2026-09-11 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 014eae25-fb68-3a16-99d9-3088d718962b | -8.5506 | -63.8786 | 2026-09-11 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 85af77d8-52d6-32b3-945a-68dc9c809091 | -5.9815 | -57.7672 | 2026-09-11 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 2f45256a-9a4b-3aec-91db-8e03ae2baa37 | -5.9817 | -57.7282 | 2026-09-11 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 3537b28e-2772-3ec3-b938-ee6d66551f4e | -6.4045 | -54.9842 | 2026-09-11 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 6dc26614-d95b-341f-8ab3-f460b9fb0464 | -9.1711 | -49.9835 | 2026-09-11 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| b4ea05d4-255d-39e9-bc27-b700b7756645 | -6.6226 | -58.4995 | 2026-09-11 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| e8363e83-1774-3c3e-9a9a-2e3469406cae | -8.9428 | -63.2797 | 2026-09-11 15:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 23681e01-65a7-34ae-a488-8b4b3152156b | -6.7692 | -58.6679 | 2026-09-11 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 675741a1-4841-3def-b28d-f84808303c13 | -10.2743 | -45.2726 | 2026-09-11 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 195.9 |
| cf7e6c10-88c6-3a34-b7de-5a9593e69fe0 | -3.4241 | -59.2343 | 2026-09-11 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 86aa3c11-d969-3693-887d-17cec2f10c8e | -8.4715 | -70.4779 | 2026-09-11 15:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 43.2 |
| c6fbe931-ecc8-3686-bb08-45256063b63d | -5.8021 | -53.8061 | 2026-09-11 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| dfac2892-f8fc-33b5-88cc-e7d755885edc | -6.7448 | -45.5056 | 2026-09-11 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| db226f86-aa01-329a-beab-1d4567171c5a | -11.9547 | -49.7512 | 2026-09-11 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 5aded13a-fe28-3646-8e53-97e962b80163 | -7.5553 | -45.1624 | 2026-09-11 15:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 235.2 |
| 324a3377-06b6-3079-a939-d03da1ea3aa8 | -9.0415 | -65.7349 | 2026-09-11 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 9b9a01b1-25ea-3b25-9bdd-2fbbda955107 | -13.2487 | -61.6371 | 2026-09-11 15:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| b14def43-7a2f-3ae2-82b7-e98d8c150ed5 | -5.3645 | -56.0447 | 2026-09-11 15:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| fae238f2-bb7d-3816-b5f0-bd008aa517f1 | -6.1808 | -55.2748 | 2026-09-11 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 1ce30f0b-2ec0-3019-802c-6c35744b2953 | -3.3688 | -59.4079 | 2026-09-11 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 61db47ba-23a1-34c9-91e7-a5ed9ff20603 | -10.5478 | -51.3367 | 2026-09-11 15:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 9ae1cda1-3d36-3d0f-8b42-e88166a1919e | -5.8571 | -53.8844 | 2026-09-11 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 04fae053-58ae-3793-9cfd-72429683d17f | -9.7889 | -43.48 | 2026-09-11 15:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 332.6 |
| c25cecc0-68db-34a0-bcea-a1ee4c79a4e8 | -6.055 | -57.8032 | 2026-09-11 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 8c4d2eff-d8f7-33a6-8707-4bf241bcc99b | -6.8281 | -55.2826 | 2026-09-11 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 5652d10c-fcd4-3d45-8f89-352b5fcd108b | -10.4911 | -51.3423 | 2026-09-11 15:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| e246731a-8138-3c11-a963-1fb5c0126448 | -6.8062 | -58.6469 | 2026-09-11 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 6ac7ce25-31f3-3d97-b070-c8401ecf320b | -6.8813 | -55.619 | 2026-09-11 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 79117167-bc66-3938-a69e-35224f9239db | -6.745 | -45.483 | 2026-09-11 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 887011c1-f193-38ce-b852-dbc687ace630 | -8.0747 | -54.8701 | 2026-09-11 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 084103c2-3e6a-3507-8ffa-94f5c3616e52 | -10.4909 | -51.3634 | 2026-09-11 15:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 1b92f0a8-163e-3184-9328-d901ba2c20a8 | -7.9749 | -69.9719 | 2026-09-11 15:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 15d85716-74bf-3b42-aa84-20ccb9915637 | -13.3555 | -51.7855 | 2026-09-11 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 6924158b-90f9-3e9f-bee9-c1c194a632b3 | -6.4047 | -54.9642 | 2026-09-11 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 5b3d4b01-19ac-395e-9f69-eb06073d8538 | -11.0434 | -49.6851 | 2026-09-11 15:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| c509059c-72e6-317c-be90-c46e72be584b | -6.6888 | -45.4877 | 2026-09-11 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 313.6 |
| a88b9e3d-2d85-366c-ac83-ab2a3e117b09 | -13.2293 | -61.6772 | 2026-09-11 15:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 61dc3c53-849e-32b5-b745-dfbaf9667268 | -9.3854 | -49.3631 | 2026-09-11 15:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| a2786ffb-0b1d-3599-ba89-56357fd1242a | -6.5668 | -55.6149 | 2026-09-11 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| be2f8a65-12ce-376d-995d-12b7fc788f98 | -6.1994 | -55.254 | 2026-09-11 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 164.9 |
| 33be5985-12c6-30a7-a914-e63556f780d5 | -9.3852 | -49.3847 | 2026-09-11 15:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 190.4 |
| b26535bc-bf9b-3bd5-a138-cbb0070c7e5f | -13.3552 | -51.8068 | 2026-09-11 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| d4c3b812-0d50-3293-836b-c78c389ea547 | -6.8062 | -58.6469 | 2026-09-11 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 5b42e3cf-f421-3670-bdd7-7b4855418585 | -8.5506 | -63.8786 | 2026-09-11 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 3677f72d-79be-3502-9360-322be59e0632 | -11.0434 | -49.6851 | 2026-09-11 16:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 447a6ae6-4a99-35e8-8db1-9202ea8fa6c1 | -6.055 | -57.8032 | 2026-09-11 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 2a199bb3-ff93-3fa3-9c8d-68e73dde6e18 | -9.9041 | -45.91 | 2026-09-11 16:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 870fe8ca-fe18-33ea-a9fc-51cc92631ff5 | -6.3846 | -55.2051 | 2026-09-11 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |


[Clique aqui para ver as próximas entradas](README46.md)
