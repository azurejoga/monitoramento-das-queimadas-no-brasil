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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96e99b3b-6c98-3148-8547-e8d2a572a582 | -16.2123 | -47.4874 | 2026-09-02 00:50:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |
| d9ccf88c-7e7a-3cf0-9a57-e504e79d6d1b | -16.7339 | -47.0688 | 2026-09-02 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 262.1 |
| 183b4a35-3b37-3c4c-a413-d032755855b7 | -16.1931 | -47.4682 | 2026-09-02 00:50:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 80d9f3d1-a537-37c5-b682-13d8133334c1 | -8.5727 | -63.1996 | 2026-09-02 00:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| fd5bba1e-cb8f-3ae8-bbcd-49339b780285 | -16.7136 | -47.0957 | 2026-09-02 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 3e942838-f408-3b71-b1ba-0c7bc5fb7182 | -8.5542 | -63.1814 | 2026-09-02 00:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 9e23870d-69e2-372a-b7af-f64c20bc5b37 | -11.7713 | -50.5472 | 2026-09-02 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 4b2b57e8-035d-3dc7-8881-e0f793e4b819 | -7.2191 | -60.6699 | 2026-09-02 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| da188447-a7e7-3586-a013-34b5e01969d8 | -6.6948 | -58.7678 | 2026-09-02 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 4c4b19d4-2953-3ca0-a979-ab511a17def4 | -11.6624 | -50.1954 | 2026-09-02 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| a7895de4-c25d-3154-a2bf-b5fa83903e07 | -16.7532 | -47.088 | 2026-09-02 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 76.8 |
| a9724f5b-aa18-380c-9da7-e4d813f29511 | -6.6949 | -58.7485 | 2026-09-02 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| d4024765-e966-3ccf-b040-f4636b396b7f | -8.911 | -62.372 | 2026-09-02 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| c54a5c16-3322-3427-b895-9f5ee582edea | -6.9495 | -56.4487 | 2026-09-02 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 8be57cf6-0bda-317a-aca4-21a555c2d655 | -7.2005 | -60.6897 | 2026-09-02 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| fd45a44d-8e59-308e-b5d2-c66ad6f616cf | -9.8806 | -64.9764 | 2026-09-02 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| cac9fc55-20fc-303b-a577-a2084b85c702 | -16.7334 | -47.0918 | 2026-09-02 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 9588a14b-8d3f-3626-970d-15c62477e1c1 | -10.6841 | -54.0451 | 2026-09-02 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| ae8dc9c0-76de-35b9-b7bc-38437b1d0212 | -16.7141 | -47.0726 | 2026-09-02 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 290747d6-a233-3c7f-926c-e59d4290e014 | -16.7538 | -47.0649 | 2026-09-02 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 7994677c-c4ed-325b-90a4-c752c28c069b | -11.3579 | -45.4027 | 2026-09-02 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| bc02fe78-cdd0-3542-8917-ef33818fc05e | -11.7903 | -50.545 | 2026-09-02 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 0627d6d9-e389-3202-aa6e-3b6a46831c36 | -6.9494 | -56.4685 | 2026-09-02 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 0a5c61f5-3d20-3b78-897b-918268658372 | -16.2128 | -47.4645 | 2026-09-02 00:50:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 0c6ea613-0d78-35ce-9a08-2a297d92272c | -8.7613 | -62.5869 | 2026-09-02 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 728ec9d2-1cf6-318a-b8a4-3e90915ed609 | -8.5541 | -63.2003 | 2026-09-02 00:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 902276a8-ff16-3098-8ac2-98f1f879cf77 | -5.8537 | -57.5576 | 2026-09-02 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 2040bcab-afb8-3ed1-8672-b3cf7c9ee0a8 | -11.478 | -45.0868 | 2026-09-02 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 8eccd157-e859-3d12-a5c7-10c2488dd491 | -8.5728 | -63.1807 | 2026-09-02 00:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 9cef7b91-bc5a-340e-b69f-4eb20042ead3 | -12.1704 | -47.0806 | 2026-09-02 01:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 83204c04-88ec-320e-93f6-a30494f8f2a3 | -6.6764 | -58.7686 | 2026-09-02 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| f0266aac-abaf-372c-8d27-9132c916d0f2 | -11.478 | -45.0868 | 2026-09-02 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9186e6f8-b44b-30e0-b952-61baf214e70d | -16.1534 | -46.6286 | 2026-09-02 01:00:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 123.0 |
| a305b411-9388-3c03-94c2-1169049106f0 | -6.6949 | -58.7485 | 2026-09-02 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 74375ba5-bc31-3f70-b196-1d79fd46557d | -12.1504 | -47.1283 | 2026-09-02 01:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 2139098c-fd8e-338b-b497-68ba000a1c40 | -1.4944 | -54.2362 | 2026-09-02 01:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 55618c7c-f420-321f-95a3-e4d2835054ad | -16.1726 | -46.648 | 2026-09-02 01:00:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 92b850c8-3a0a-37b8-9351-0fa9c16abac4 | -6.6948 | -58.7678 | 2026-09-02 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 6ff22169-5188-3f8e-ae6c-0b72684b6ba0 | -8.5542 | -63.1814 | 2026-09-02 01:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 169ba3a5-d22c-32fd-a961-6d7a0eb38fec | -12.1516 | -47.0608 | 2026-09-02 01:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| a5c26f4e-d0ae-3725-8f94-373a073dac89 | -5.8537 | -57.5576 | 2026-09-02 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ab1257d4-d835-3980-8da8-402bb3c78cf3 | -7.3671 | -60.6067 | 2026-09-02 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 3e2fa962-cb35-3a94-a8ec-7fcf2bac494f | -12.1312 | -47.1309 | 2026-09-02 01:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| b3a11cd8-6ae2-334e-8e1c-b315608eb045 | -11.6624 | -50.1954 | 2026-09-02 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f57be784-b4b3-3e7a-a789-f6b99af35bd1 | -7.2006 | -60.6706 | 2026-09-02 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 76ac52e1-f9a4-3508-a377-569de17fd81f | -16.1528 | -46.6517 | 2026-09-02 01:00:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 160.5 |
| feabe879-512e-33d6-92b2-b941cc1e635b | -7.2005 | -60.6897 | 2026-09-02 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 72ee10ea-8a3d-315d-87da-e6e2ff92b2af | -8.5728 | -63.1807 | 2026-09-02 01:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| fa2dedbb-33eb-3798-be90-34ccf3a0fc5f | -8.1112 | -54.9483 | 2026-09-02 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 01cb2b5b-52b2-31f8-a084-86b100dadb43 | -9.8806 | -64.9764 | 2026-09-02 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 1e7660ad-ad0e-36ff-935f-625efe5aeecb | -8.5541 | -63.2003 | 2026-09-02 01:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| c71aa45f-9cb3-3af3-b5db-f027210870a1 | -12.1708 | -47.0581 | 2026-09-02 01:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| f0c4035d-c9bd-342d-a882-3f5754ffba57 | -12.1512 | -47.0833 | 2026-09-02 01:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 3c1c4b83-ddd0-36c1-82ed-e97ef1f66333 | -10.9009 | -45.3509 | 2026-09-02 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 329945e0-ab4f-33ee-9bd8-82584d48fbad | -12.1508 | -47.1058 | 2026-09-02 01:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 2a9ee486-5cb2-36f9-9648-5a99f8d3459b | -8.1298 | -54.9471 | 2026-09-02 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 2b3c25ae-4abe-3828-995c-97215983738c | -6.9495 | -56.4487 | 2026-09-02 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 67382e9f-eec7-3978-a7b2-e7c2267c71b8 | -8.911 | -62.372 | 2026-09-02 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 0a6af4b2-eb3e-38f1-b764-14cb9d484449 | -7.2191 | -60.6699 | 2026-09-02 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 757284c0-031c-3e3b-833c-1ecaebd36e91 | -9.44861 | -64.5666 | 2026-09-02 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a0235a2c-3ad5-328a-98f0-6742508410a2 | -7.5148 | -60.76691 | 2026-09-02 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f93ba6bb-36ff-3b49-ad05-f7a3a35f1911 | -8.44856 | -54.70587 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 605.6 |
| e5721fc7-f1c5-307b-87f7-ae7e810afceb | -7.19849 | -60.66974 | 2026-09-02 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 1d44359b-b890-39bf-9550-958adacba427 | -10.68189 | -54.06371 | 2026-09-02 01:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| dc191157-49f2-3fdb-ab17-f4ae929c5e60 | -7.69401 | -67.12714 | 2026-09-02 01:05:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 593b58d5-a736-3c1d-9bc8-8ea2ae4e7475 | -9.09031 | -65.38126 | 2026-09-02 01:05:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 2a2d690b-0b18-376b-907e-c4defe3dfc90 | -10.46736 | -64.47053 | 2026-09-02 01:05:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 91f1ae1c-def8-3476-a623-c38f46771c3a | -7.94589 | -63.45196 | 2026-09-02 01:05:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ff8d3eae-a9dc-3d31-ab30-4a2760c945ca | -12.01128 | -60.54181 | 2026-09-02 01:05:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9aa4c7ae-1686-3b94-a70f-2ba8d458f1e5 | -7.36387 | -60.61758 | 2026-09-02 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 42de9b8b-68d7-3d2f-9e87-1753c9a4497e | -7.20055 | -60.68388 | 2026-09-02 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b24783ce-ea7f-37bd-b900-e409e8ba4cb8 | -9.92537 | -60.49429 | 2026-09-02 01:05:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f2286f43-fb9e-3626-aa9c-66969c15a5f7 | -9.14355 | -60.96096 | 2026-09-02 01:05:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9436ce5f-5515-3a4c-9c2a-2a048b1da744 | -9.4419 | -67.45212 | 2026-09-02 01:05:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 85843960-fc30-36f1-a966-e54d63022dd1 | -6.69385 | -58.76032 | 2026-09-02 01:05:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| aa2d5194-18b3-3e11-aaab-4467f09129fe | -9.44599 | -67.45682 | 2026-09-02 01:05:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 3ec19102-554b-39a5-9bec-ab25412a80cc | -8.76519 | -62.59267 | 2026-09-02 01:05:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 3da6e1fa-63ea-3a05-adb4-5ee8a712a212 | -7.66734 | -62.55057 | 2026-09-02 01:05:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 95ad8f88-4846-3309-8e39-0f8e76dc7d78 | -10.49491 | -59.60811 | 2026-09-02 01:05:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 2b3948a9-4621-3b8d-9359-3c6d65840dbb | -10.94651 | -61.66118 | 2026-09-02 01:05:00 | TERRA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5e6952dc-f77d-3442-a8a5-55ee334eaeeb | -8.99961 | -67.80992 | 2026-09-02 01:05:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| be048c61-e741-3379-8a77-37a971b1f6e1 | -9.8372 | -64.99023 | 2026-09-02 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c81ed223-eef7-32f0-840d-e563ef53fe18 | -13.99457 | -58.69407 | 2026-09-02 01:05:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 622.1 |
| 6259caf9-dfb1-31a9-aef0-d01778c85a1d | -8.1329 | -54.97839 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| d0057941-b0e3-3ac4-8142-ad7e99490575 | -7.61926 | -57.61589 | 2026-09-02 01:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 4a0e639f-c361-3b7f-bd19-3f794208cae3 | -9.44983 | -64.57545 | 2026-09-02 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 21f14edb-0891-37f5-b279-177d4b7454a6 | -6.76061 | -59.44645 | 2026-09-02 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| dd9ca554-ddb7-3ec5-b57b-56288f0602e3 | -9.18428 | -65.54178 | 2026-09-02 01:05:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 521c8e14-5017-39ef-b0dd-8e6bfadccdf0 | -8.23685 | -62.90171 | 2026-09-02 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 57a234d9-d0e0-3cc9-879c-d713e11c5a09 | -6.81652 | -58.87761 | 2026-09-02 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| fe34d6af-56d0-3d1e-937e-45f09c90326a | -7.76612 | -61.21247 | 2026-09-02 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e5ac64c0-49b2-304f-8bb5-ad5b56819d9c | -8.22487 | -62.75059 | 2026-09-02 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.5 |
| fd56aa64-cb54-3201-8b5e-0b806dc1a460 | -8.10243 | -58.26966 | 2026-09-02 01:05:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 3b90d3fc-5cba-36c8-8ec1-b0a995422330 | -8.21676 | -61.48252 | 2026-09-02 01:05:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 88473763-0ef5-3c5b-9a4a-e421cdc6df5b | -9.86509 | -64.98039 | 2026-09-02 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e94676f3-78af-366e-a251-5647a5eaa8cb | -6.69017 | -59.95485 | 2026-09-02 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 023e53d8-b394-33be-a1fb-768d889db60c | -8.90683 | -62.36021 | 2026-09-02 01:05:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| ac3ae7ed-6e95-31a1-bf05-e10d4e4549d1 | -10.46859 | -64.47942 | 2026-09-02 01:05:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0cd91826-5c4b-386e-8976-80bd5ccdfce4 | -7.73147 | -60.98145 | 2026-09-02 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 457432c3-dcca-3c21-96cd-b12dc479c61b | -10.94938 | -61.65444 | 2026-09-02 01:05:00 | TERRA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |


[Clique aqui para ver as próximas entradas](README4.md)
