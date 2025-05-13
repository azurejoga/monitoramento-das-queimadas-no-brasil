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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 559345f8-1088-3e4b-90e1-cfdccea795cb | -13.971 | -56.8077 | 2025-05-13 05:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 32.4 |
| fefc430b-6bf7-3bde-b483-31bc03199e73 | -13.9902 | -56.8058 | 2025-05-13 05:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d99490ca-3bf8-3043-aa93-99b434440c15 | -13.56362 | -52.87623 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 80a94694-9c19-3059-85a2-dfa00e14e3fe | -13.98263 | -56.798 | 2025-05-13 05:31:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1740d459-d354-379c-a762-422fc89f3881 | -13.07019 | -52.01741 | 2025-05-13 05:31:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 977ab3cb-d0e9-368b-b5ec-5815b1477eb0 | -13.04876 | -53.72174 | 2025-05-13 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f536d58c-cbfc-3a17-b1fd-041e95e2146d | -13.97738 | -56.80223 | 2025-05-13 05:31:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a72da63d-ffcd-3018-bbfa-ec68516c0858 | -13.04829 | -53.72559 | 2025-05-13 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2940d67-3d28-34d0-9794-a4b12be68106 | -13.56312 | -52.88078 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b319e189-4d18-32be-92f5-b4e197d8bdc9 | -13.98202 | -56.80278 | 2025-05-13 05:31:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| f7e394a4-29b8-3163-bb21-52ab0d470ba3 | -13.57061 | -52.86775 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 397e413a-6fe7-37ca-ad95-21439d65e2eb | -13.56203 | -52.86541 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e4ee0a1-5318-3f6d-92f4-bc71968afe43 | -13.67502 | -53.93764 | 2025-05-13 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa55c7e0-c6bd-3cd4-9536-4fc7c7763a86 | -13.57658 | -52.86855 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 00e3d663-9aef-320a-bdf7-6c7b18295f06 | -12.01532 | -62.83955 | 2025-05-13 05:31:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29c6eb99-21f0-33d4-b984-f0bb7b2d9641 | -13.67354 | -53.93675 | 2025-05-13 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad33ee2e-f8ff-3989-b23a-8ffedaeacf9b | -13.56748 | -52.87064 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d5fcde1f-79f4-3e57-96df-4e80daf8c7c2 | -7.92855 | -61.555 | 2025-05-13 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6df1b62-be06-385b-9865-dba07793f1ec | -13.98667 | -56.80329 | 2025-05-13 05:31:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 149aa95f-a82e-3b73-8e6a-f557f36b3bca | -13.0524 | -53.72084 | 2025-05-13 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89643d30-4b31-3d23-b080-062b050323a1 | -13.06634 | -52.01593 | 2025-05-13 05:31:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfaaaf28-8a15-3bb4-8b93-7aab03128674 | -13.555 | -52.87373 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36b5fe11-47da-3e8b-aab3-fca6bac765d3 | -15.29214 | -53.20704 | 2025-05-13 05:31:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5420278a-a8ae-312c-91cc-00668d6a73df | -13.57998 | -52.86753 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb29d5aa-62d9-3dd5-bc12-cf987e6fd006 | -12.00919 | -62.83493 | 2025-05-13 05:31:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c1239ff1-a133-3845-baa5-fd0f7e41b005 | -13.98727 | -56.7985 | 2025-05-13 05:31:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a49f7121-7c26-3438-ae52-52d3954ffb08 | -13.06394 | -52.01647 | 2025-05-13 05:31:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce667a71-0f99-390f-b4ea-8ef8bff666f6 | -12.68373 | -58.15017 | 2025-05-13 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d0a2772-f1d0-35c4-a23f-392d6ab5a176 | -12.09561 | -64.25555 | 2025-05-13 05:31:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 822d7052-671a-3c16-b0d8-12d59c3c7ac0 | -13.57346 | -52.87136 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d1f76130-767b-3c1a-92a4-32b436c1cb9e | -13.98606 | -56.80804 | 2025-05-13 05:31:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 1ad491db-1ec3-3e23-ac62-30fc2702b9cd | -13.55553 | -52.86917 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5bac6c3-534c-3e4e-b9dd-9973fa004790 | -13.56695 | -52.87519 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6f2b138e-0d0b-31d4-9d8e-b415855a779f | -13.04631 | -53.72414 | 2025-05-13 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6fdc66e-c514-3ad0-b2c8-fc1452407311 | -13.55605 | -52.86466 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b395ae27-ce30-30cd-8528-ef1ccd3e960e | -13.674 | -53.93266 | 2025-05-13 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65d436f3-8687-3223-a23c-5bdb90c825a7 | -11.05965 | -60.88295 | 2025-05-13 05:31:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bf23602-e525-315d-a9a3-ac523539e7bc | -13.57608 | -52.87306 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ebcb4f60-2c9d-3f4e-bb5e-8923ddeb953b | -13.0544 | -53.7223 | 2025-05-13 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66fbe979-c936-329c-a0e2-0d3b709c61ad | -13.57242 | -52.88026 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 95397856-d053-3471-b6ea-2ce80355c445 | -13.67552 | -53.93358 | 2025-05-13 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64ad44a7-447d-3b64-b3b7-244e5885b708 | -11.14203 | -56.79353 | 2025-05-13 05:31:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cf8b1f1-af0a-3c70-aaa1-19540170228e | -13.05195 | -53.7247 | 2025-05-13 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e656c580-7b86-36b2-b999-69beb244527d | -15.29811 | -53.20777 | 2025-05-13 05:31:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d0b7d529-b226-3511-a308-b8ae1899d931 | -13.97861 | -56.79251 | 2025-05-13 05:31:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9aba1599-7fbc-3924-9b55-bceb540ed44a | -13.04265 | -53.725 | 2025-05-13 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37d674ad-21b5-3a3d-96d4-10666a0f5c06 | -13.5701 | -52.87239 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 36134d5a-8eb9-35c7-bb7a-fe5831b3fc8d | -13.06009 | -52.01505 | 2025-05-13 05:31:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21eceb14-0b9f-36b7-8e8d-c81d607b9ed1 | -12.21747 | -63.78298 | 2025-05-13 05:31:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb52a8b5-4b89-36df-b66b-7eb76cac6fa7 | -13.57401 | -52.86672 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7c8d2dc1-0508-38bb-9769-428a5f444fe7 | -13.56911 | -52.88138 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8b7a93fc-6c0a-3a9f-9d8f-34678c1f857d | -13.57294 | -52.87581 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ebcb7cba-ac0a-3d87-8b22-1e9422511c18 | -13.96935 | -56.79116 | 2025-05-13 05:31:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a505514c-db52-3565-a39e-a229c17d75e5 | -13.97678 | -56.80698 | 2025-05-13 05:31:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f08fa65a-ed6e-3a86-8bfb-58f071f405ae | -11.25541 | -52.47172 | 2025-05-13 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7019d11-a079-3b31-ae70-3efe22e188d9 | -13.96997 | -56.78618 | 2025-05-13 05:31:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 757c16da-42dc-3e14-b30c-c923e46cc51d | -12.00864 | -62.83849 | 2025-05-13 05:31:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b395b00-6aa4-3917-adba-e133e12f1637 | -13.5659 | -52.88419 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| adaa5bba-b703-3d48-ac37-dcea69edbd54 | -13.55009 | -52.8638 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| babf09dc-946e-3a15-9910-72529ede38e2 | -13.97798 | -56.79745 | 2025-05-13 05:31:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4071538d-0c52-3487-bf8b-1dfece87cbd1 | -13.56642 | -52.87971 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4156a706-6fc9-3c55-955b-8264797e8b2b | -13.04312 | -53.72116 | 2025-05-13 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d4a168e-07bb-3ab3-bb73-f507a6a0ce51 | -13.98142 | -56.80752 | 2025-05-13 05:31:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 12d283ce-f5f8-32d8-89be-0a40b31e5375 | -11.26135 | -52.47261 | 2025-05-13 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bd8b17d-3d28-36ff-9ac3-d7d3c0434dc7 | -13.04675 | -53.72028 | 2025-05-13 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1106aba4-f472-34ad-95cb-aab63e862885 | -12.2208 | -63.78353 | 2025-05-13 05:31:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad74e8d0-f66e-3d3b-96df-efe7b9080803 | -13.06575 | -52.02097 | 2025-05-13 05:31:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad086f5d-f277-3d66-abf2-44fda4707d0d | -13.5696 | -52.8769 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 06461118-87fc-351b-a801-ca99b39c9a95 | -13.5615 | -52.86992 | 2025-05-13 05:31:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ee0692c-7ccc-3767-953b-1abb4a8f7908 | -12.68787 | -58.15078 | 2025-05-13 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ef7757a-73ea-3841-b92c-92ca47035e02 | -18.33901 | -55.58747 | 2025-05-13 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| fe75e906-96c0-32e0-82d4-e05e10c77528 | -15.42917 | -60.19762 | 2025-05-13 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98a6e53e-36c2-3f39-9b2b-53f691fe4564 | -15.22484 | -59.35958 | 2025-05-13 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45ccf583-a6a5-335c-9ef5-f878acbc398c | -18.33863 | -55.59089 | 2025-05-13 05:33:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9f37181f-56a4-3353-a902-73b5ed5f69ec | -13.9905 | -56.7855 | 2025-05-13 05:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 46.4 |
| affac341-31a6-3a04-92ab-6a7b180c01d7 | -13.5683 | -52.8783 | 2025-05-13 05:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 97ec13f5-3c97-3930-a406-86a413027219 | -13.9902 | -56.8058 | 2025-05-13 05:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 9fe47941-850c-3f1c-a261-bac585b5f466 | -11.7921 | -47.40419 | 2025-05-13 05:46:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 549e72f8-c9b0-3777-b2ed-b5e9b821518b | -10.00065 | -47.84025 | 2025-05-13 05:46:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0f059fa9-7364-374c-b1e7-ebc7f262eacf | -12.14604 | -48.01114 | 2025-05-13 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| f139d168-30dc-301d-8184-3b02bd1277dc | -13.57065 | -52.86067 | 2025-05-13 05:48:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6db4177b-52ae-3f50-a670-ebc8da4a5213 | -12.18743 | -46.70826 | 2025-05-13 05:48:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8c18e10a-4755-38fd-a4da-0def8978722f | -13.56774 | -52.86691 | 2025-05-13 05:48:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 0cfbe287-e535-3442-8a78-9091d43f7935 | -13.36132 | -47.58543 | 2025-05-13 05:48:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a6eb9391-0474-397a-a2cf-938e34cb3612 | -13.56871 | -52.8727 | 2025-05-13 05:48:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 45e68f18-3e9f-35cb-8b1b-525cb7428a93 | -12.17658 | -46.71719 | 2025-05-13 05:48:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 09ffd00f-e844-3f5b-b5fe-eae3f3ca2b12 | -12.17805 | -46.70694 | 2025-05-13 05:48:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| aad2bb71-73ab-3088-a6ee-def5c7f13e87 | -13.56572 | -52.87891 | 2025-05-13 05:48:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 91f1fd5f-f314-3d8b-a82c-d709dec40280 | -13.55859 | -52.87094 | 2025-05-13 05:48:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 5dbf13da-5024-3142-9162-fb5ab38caf17 | -12.15629 | -48.00329 | 2025-05-13 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7162969f-82a7-3bd8-a811-9e9c5fd63c44 | -13.55662 | -52.88305 | 2025-05-13 05:48:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4e5d200c-c8fb-35c0-81e7-0270b5799013 | -12.14738 | -48.00198 | 2025-05-13 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0bb50c84-51bd-3ab6-bf53-f6002eb7cdfe | -12.15495 | -48.01246 | 2025-05-13 05:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4fd2adf8-b603-3a80-ad2d-44da1aa39346 | -13.35996 | -47.59484 | 2025-05-13 05:48:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| f0ddce45-3eb9-3541-b95a-4237296bc00a | -13.5683 | -52.8783 | 2025-05-13 05:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 712c293d-4bac-3f8b-94b9-cb7418de4977 | -8.0889 | -43.1196 | 2025-05-13 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.1 |
| 18002796-9624-3c03-8e6c-4b707f30afa6 | -8.07 | -43.1216 | 2025-05-13 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.9 |
| c8833350-a14d-3bcb-82be-733cbd21fe64 | -13.9902 | -56.8058 | 2025-05-13 05:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 909da965-8408-31f4-b1ee-ce7854753df2 | -12.21556 | -63.78404 | 2025-05-13 05:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 780833f4-f5f4-356a-869d-c89312c16d4b | -12.0089 | -62.83757 | 2025-05-13 05:53:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README12.md)
