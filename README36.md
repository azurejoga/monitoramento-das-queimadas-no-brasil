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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32bf0e7d-d8da-3d3d-9d90-d5ace5b22174 | -9.721 | -48.14358 | 2026-09-02 04:57:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42e1848d-be9c-3f7a-9344-8c6c2c4e6c7b | -6.94837 | -56.45248 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6a8a2cd-c73e-3d42-a369-1ae2a2f148fa | -6.77502 | -59.43713 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a870edcb-b2a9-3ecf-bcc7-e87bfe95560c | -10.91133 | -45.33121 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 0f34264e-212a-3cf9-a6f6-75fb06727b5d | -10.90222 | -45.32996 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6bf57b8a-6b46-363b-b0c2-aee38566dd2c | -11.34768 | -50.62517 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cef8a887-857c-3e1e-9054-2c38523467f4 | -7.93692 | -47.24376 | 2026-09-02 04:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7f68e4c-765d-3217-ae65-32198f7b0d52 | -8.11364 | -54.94977 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d48842e2-3b23-3163-8c32-7b7194e7d20f | -11.33748 | -50.57803 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca536a76-88e9-37fb-8cf3-97113e67a1e6 | -6.43606 | -53.56506 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 451d4c9a-0a54-3733-9ceb-7c72e999b086 | -10.96686 | -50.48573 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85f8fd7b-0cb3-339f-99a5-22ff565ba78f | -6.8786 | -59.40371 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb66e8b4-d4af-31e4-9be3-483c263589fc | -11.05275 | -51.519 | 2026-09-02 04:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3e592c1-1e49-338d-a40a-e8db2043fc4a | -12.37493 | -39.57574 | 2026-09-02 04:57:00 | NPP-375D | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f7d09ab8-11b1-31dc-9495-afeba0818584 | -11.82149 | -46.05965 | 2026-09-02 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de3b10df-e63c-3249-9f85-2b61b8960cef | -11.53378 | -45.48027 | 2026-09-02 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4720fc16-63b1-3541-be65-54c60549a0b8 | -12.3806 | -48.14396 | 2026-09-02 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 93d95636-e112-3260-a3cc-992f183a4f2e | -9.0224 | -65.45203 | 2026-09-02 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eafa77bb-63cd-3e2b-8919-063c281ee346 | -12.08456 | -47.10682 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d39e0429-4b76-3d7d-96c1-6d96977ca343 | -6.48771 | -51.44646 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88090e3e-2103-3f3a-90d1-82fcfc553c5a | -6.65421 | -59.43106 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 101db0a1-3729-31dc-8300-863b0501145e | -12.14057 | -47.06561 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc69a882-bfeb-3b44-8b78-5515ea91053e | -10.76358 | -53.99447 | 2026-09-02 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 532a6b4e-0c38-334e-898f-cf6f3a2e44b6 | -10.38293 | -49.98438 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b5c33c1-cdc0-3364-8aeb-c577603124f3 | -8.4583 | -54.71919 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| df27df85-bb43-34b3-9e29-367c20308e0a | -6.57039 | -55.61638 | 2026-09-02 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5a2e245-9031-3294-8a1c-7b76cfba53aa | -12.37538 | -48.15309 | 2026-09-02 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b045928-c0f0-320a-8c3c-05a26a0d050c | -6.94097 | -59.63932 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e30c361-7963-3905-ab3f-148947ef7940 | -5.33933 | -60.14794 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 776b98a6-671a-31b6-8ea4-c6aadb58591e | -11.35565 | -50.59607 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70228e0e-1252-3e9c-bb43-a930cd39e0e7 | -11.66037 | -50.18874 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fd9488bc-9e4b-30ef-b0da-286335562799 | -8.42879 | -54.71593 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 088da312-ce30-392e-9ec9-140e05be0128 | -5.97127 | -53.58435 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| adeccba9-c05d-3a67-b99a-92f1aab53e74 | -7.45155 | -59.92736 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a1772de-0908-33e6-9213-8d6a39b7e9a5 | -8.46695 | -54.71194 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6bef4378-6baa-36cc-9970-adb039326624 | -6.77136 | -59.43579 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 55b322e6-5621-36e5-a2c5-20d7e6c3bd1f | -6.4073 | -49.93745 | 2026-09-02 04:57:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efe6deb9-e5c4-3caf-bb71-ffc501826129 | -6.95119 | -56.46051 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd3232d3-3eb2-31ec-8ba1-21429b53f294 | -8.09878 | -51.67862 | 2026-09-02 04:57:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f847f0bd-969c-3dcf-89d8-9890f660ee2a | -6.76094 | -56.33205 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2141a5dd-278b-388c-aa55-97feca01ae0d | -10.67903 | -54.04323 | 2026-09-02 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| acbe9d9b-fa27-37f5-ad94-7e57937783f0 | -11.26905 | -45.12988 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6a4f8a7-ff58-3ddb-897b-d69f74380a50 | -11.1283 | -51.53054 | 2026-09-02 04:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8f6b9aa-7df3-3f45-a76b-caa3067f1f37 | -11.84404 | -46.05822 | 2026-09-02 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c52114c0-6a42-3a57-ae7f-f53740ee277b | -6.1448 | -55.66821 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d47d581b-195f-3f6e-931a-a684e8615a71 | -11.29857 | -45.14565 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc3a99dc-2ddd-3b63-a7a6-daa7b71e7de8 | -6.91403 | -59.64389 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 497ce3bf-f758-3a59-8eda-b88f7082357d | -8.76641 | -62.5841 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 14c092b8-a6d6-31fc-bf09-27c504dbf4f1 | -8.11484 | -51.66333 | 2026-09-02 04:57:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79ecbeef-feba-33b6-ac75-3c8609414655 | -8.43228 | -54.71915 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e5c6b3f-6ca3-3b1e-b554-ebe3921594f6 | -8.91573 | -62.3605 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bb1923f9-c34f-3f93-b7a8-9e94da5f6c5d | -11.3176 | -50.63939 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae9c32f1-0d18-31b0-9f5e-f79d312affa2 | -6.64791 | -59.4314 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8df84b56-6b7f-35ef-bd7a-ce9d0831b370 | -7.42826 | -59.77739 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a7bec99-a501-3839-969f-463cd21578b5 | -8.46121 | -54.72399 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1d42a97-e026-391c-b2f9-b2a9afd45fe6 | -6.76397 | -59.44101 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 977398bb-6891-3eb7-86a1-18dd06141f75 | -8.46191 | -54.71982 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| cf25614f-177d-3e56-9d31-b769bd840d1c | -6.64793 | -59.43746 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a2575936-22c5-34fe-9301-f360ea68a19e | -5.48982 | -57.14659 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7a7cfd9-cd35-3f09-b139-41004502de46 | -9.3979 | -51.67965 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b59c6390-d4a3-3dfb-9771-0a5d064843ff | -12.14005 | -47.1298 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f8558304-6aef-3d45-a343-e8c4c25771f8 | -6.2588 | -55.42179 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8a46b2f-d7b7-38b6-b3dd-09a4c17b8bd7 | -6.68445 | -58.76218 | 2026-09-02 04:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 54e9a9d9-7cd3-362c-8025-8d9b3252a66b | -12.13644 | -47.06502 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eaa2f9fb-3403-3a10-b606-9fbfef6f9ca5 | -11.67018 | -50.19421 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6b58217-9cf7-3bc8-a206-831fefcd2a0b | -8.48279 | -54.70603 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 83d50c09-3334-3c6a-9066-fa27d73cfe65 | -12.13593 | -47.06873 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bb8b732-d194-398f-a366-d89d419686ec | -12.12979 | -47.14337 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0af36c8f-56f7-3047-abbb-3f7367787601 | -8.46553 | -54.72042 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b990b3be-b43d-3ba3-a1ef-72a211b5dbee | -10.74596 | -47.97969 | 2026-09-02 04:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 163a6a45-1298-399d-9253-bc6878e6f540 | -11.30319 | -45.14643 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 52c2f264-1725-35b5-9fbd-fefbd07346ef | -9.71215 | -54.33123 | 2026-09-02 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3afd0150-0ea7-31c1-b2f8-7345dbeaa4b6 | -12.1483 | -47.07045 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| deabb56a-64e1-3b3a-b8df-967b9c670c8d | -7.42878 | -59.77442 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35a4b14b-8dff-36ba-bb32-134c21605385 | -10.37948 | -49.98385 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e7c7906-dde1-35f4-a055-8383ec106972 | -6.14757 | -57.75163 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c59b5cf4-51ef-3245-a2cd-dc93052ee75a | -9.47092 | -57.02965 | 2026-09-02 04:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44e81c91-e778-3ca0-b918-b3cdac00f0c1 | -11.30989 | -45.16711 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b34a775-f3ef-397c-a1eb-bab211574f73 | -9.40672 | -51.6023 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b27bb19-480b-3645-ae46-79688c8a9681 | -10.51665 | -57.44066 | 2026-09-02 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a077b8e-d912-3d17-8fb5-b4ad57d7bdf6 | -8.91495 | -62.35475 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 901edee8-9cd1-3434-84fb-ba5c9eb21d8a | -8.44816 | -54.71316 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a05c252-3f63-3769-81b4-24673737e38e | -6.80844 | -59.10752 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4b03c2e5-b05b-3f92-a664-e96cc1f1e825 | -6.25328 | -55.43084 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbe16f25-7e5c-369f-9018-59091e6f21af | -8.4561 | -54.71016 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 2978f744-36ad-39db-b7a1-b3cbcff901d0 | -12.14779 | -47.07418 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d88892a-bf03-381e-84af-eafcc894e031 | -11.29863 | -45.18106 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cb6b134-041c-370d-899d-dd6be1665301 | -12.07543 | -47.12405 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 224a0e94-77f9-3163-b4cb-0cbb228f5175 | -11.75573 | -50.54873 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3402d27-af6a-3c45-8554-d7378455ea2d | -8.90912 | -62.35355 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8cb09c71-4c54-3301-b648-97f3801e9dce | -12.07595 | -47.12037 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83311f45-7956-312d-931d-54bc003c4c69 | -9.71565 | -54.33183 | 2026-09-02 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30e33175-2ae9-37ef-b63c-4cf89d729495 | -12.08678 | -47.1032 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdcc6159-fa1f-3ab0-bc8b-f7620d614d79 | -12.14569 | -47.11934 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92f4c342-1c03-3882-a904-e1a8202ec53b | -7.19689 | -44.54294 | 2026-09-02 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5546fa8-ea76-3f6d-aa9b-f3c8eecbfc54 | -6.87963 | -59.39797 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 56daf535-07d5-3730-8508-a2a96ed31fcb | -12.13284 | -47.06064 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d8ff6f5-b5b1-32ab-9613-30a46b71ccd6 | -8.46775 | -54.72935 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3c86b89-af66-3d56-866d-38d7872ee8c1 | -12.09017 | -47.09632 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 593177d1-c183-327c-9070-0bcf2a3f3334 | -8.45099 | -54.69635 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README37.md)
