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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac7ce6b5-bb7c-3d3a-b978-dcc2de0d524f | -4.28658 | -49.08657 | 2026-10-09 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cab3525-261a-3496-971b-bd0d1f736c33 | -6.48786 | -55.95142 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc5aaf56-0062-3b8c-85da-a7e272a43918 | -10.99404 | -45.40288 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 18a6a3b5-4cef-3d34-acaa-7f08a22d7204 | -3.07643 | -54.24952 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 816cd28d-982a-3680-b29e-39b14c221613 | -7.53956 | -47.12501 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0a9e71e-a2e4-3b7c-8534-08670674c4bc | -6.00044 | -53.4939 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 683ff410-8685-377e-9515-947d2520c0f0 | -6.14301 | -47.92313 | 2026-10-09 05:04:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 457cbdb4-1904-3535-ba92-9f0ca5e9ec1f | -5.99719 | -40.98186 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9438fdaf-41aa-3446-b851-730631debd29 | -11.11536 | -47.79292 | 2026-10-09 05:04:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84f42e8a-f550-3d4e-85b5-53f0fc8f1081 | -4.74354 | -55.66403 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b94b5210-cce6-38d3-ba8d-f2cb2e920fd8 | -7.48556 | -42.83432 | 2026-10-09 05:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 076300fd-1dfb-3caa-b560-3e82c4f7b87c | -3.74577 | -59.62355 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 136d8d7c-4bc6-3728-8ccb-b7c5255086ab | -3.01692 | -57.78335 | 2026-10-09 05:04:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee05a543-33c1-33e5-bc50-c1eb0d11b452 | -6.96753 | -45.25309 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2f2aedc-9091-31d9-9460-444a32847121 | -3.28598 | -54.00107 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0b87f6d-c999-3ef8-8a94-09f3f08494d4 | -6.24261 | -52.84136 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cc4cee0-02ad-3e57-a311-754b0a7da525 | -2.58195 | -56.17427 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49228920-878d-3452-8b86-052a6a8faa89 | -4.55854 | -54.20987 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ac900ac-14ae-3e39-9592-c6af09b09fdb | -3.09635 | -54.28378 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f195b5c-cd79-3fa4-acee-fe9a7fd65553 | -3.57263 | -54.68045 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65e856ea-2b98-360b-8a3a-a468cba1ae6e | -6.94781 | -59.36596 | 2026-10-09 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f755f5bf-a8b0-33b8-a261-5dacfb962cea | -3.29174 | -54.07626 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac4af365-e303-3aef-a9ef-5bd74c75bb64 | -3.3072 | -53.71579 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9991a315-3ce4-35ee-a94f-d03dadeacf79 | -8.70732 | -62.41988 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cb896f6-83ff-3c61-b3c7-07b279033a2f | -3.31013 | -54.02834 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 369fc100-e989-38f4-86f1-82ec71d693bb | -3.52828 | -59.57822 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1018273e-3ddf-3ab7-98ff-418566e4d41f | -4.1498 | -54.03738 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbe4bd72-faeb-34c7-856a-7333f90cc057 | -3.54553 | -54.63242 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60f5c649-a4ff-397d-a6f5-4f9914159d76 | -3.06156 | -54.20721 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a3a06b7-7507-3279-b04d-70f17be8af04 | -9.21217 | -60.86929 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6343c7f0-3cc8-35e6-8f5e-f4be2294d0e9 | -3.66684 | -54.50372 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 349e37dd-abb2-39cd-96be-5794a5bc9499 | -3.31465 | -54.04466 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88950c5d-fa84-3ab5-a21b-5759255f6da5 | -3.67118 | -49.52475 | 2026-10-09 05:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0997bff-5f16-3c83-a5b8-3707bd2bc485 | -4.73317 | -55.65783 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7ead73f-1356-368f-8140-a3539ba4f5cf | -2.7104 | -57.46286 | 2026-10-09 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61196e96-c762-3aa6-98dd-86b1e236712e | -5.84806 | -53.46918 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b1049f0-bc7b-3551-8b2e-6d45ba87b956 | -3.65517 | -54.28524 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff975857-c6cc-3dc3-81a2-0d9eb99c90ca | -4.15567 | -54.02293 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e7b6e31-62ec-31c4-94c0-e31ec4c67a4b | -3.20801 | -53.88078 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51af8471-45d4-3fb6-9ee9-c05c17e30429 | -4.73983 | -55.66348 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ddb33a4f-fbf2-318c-ad13-67c3c40df5b6 | -3.05754 | -59.09092 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4ed907f7-2565-3be6-be0b-1814e2a2286b | -3.26083 | -54.02435 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00bff540-3a71-3c58-8673-fac9d3784d85 | -6.48986 | -55.29533 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 409cf807-867a-31d8-ab04-1fee8af764e0 | -5.95447 | -55.36107 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 806c5b98-8c60-3707-8296-1db43485a83a | -6.4613 | -55.49491 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b8f11be8-febc-3aeb-8ebe-4432439632ce | -3.1085 | -53.78087 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18016707-52e7-3d52-b72c-33d500f0af48 | -9.14581 | -45.8138 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4378b43a-cbf1-3eb7-9df5-f7eb67918506 | -6.92374 | -59.26384 | 2026-10-09 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 811ecb76-e4d1-3143-b5bc-2b20750c96a0 | -10.73471 | -52.03251 | 2026-10-09 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a67fe674-9586-3137-8e58-e3852b4d0b0d | -3.08411 | -53.95485 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97c904f7-63d1-328f-83cc-c9532dbe1f99 | -3.58303 | -54.66156 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62b0cc15-472c-3fc3-8f76-fb2795131d7f | -2.98203 | -54.02938 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c76735c-f7f3-371c-a310-b3e365189180 | -3.79268 | -50.79799 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d98dd9a4-7b7e-320b-af22-157e0e50f561 | -4.73838 | -55.67235 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c72d09bc-cf83-37f3-b7e5-d462394d083e | -6.88624 | -45.89665 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 122db10f-c0e1-3233-b75b-3f953363bbd4 | -3.18952 | -53.9516 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40ae3fc4-0c76-3283-ab15-274b23bff6e6 | -3.29641 | -54.00274 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74911001-b889-3f3f-980f-cf9f9a1f5b6e | -6.1254 | -55.70295 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3cfd63b9-1609-3fc1-b14a-86db4f3c9b2c | -2.97609 | -54.04416 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b4af5d7-04d8-313c-92f5-558284fc6683 | -6.67835 | -63.02348 | 2026-10-09 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3e2db50-9da1-3018-a19e-bbfe2f5fefee | -12.02431 | -43.44939 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4de0b781-6554-30a5-a60d-f24b475dc902 | -3.52197 | -50.34581 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e3e72f6-7b2c-39f0-9318-30bc81c21200 | -8.70173 | -62.41249 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aaf41751-32c5-30c7-8dc2-583dfc9f87bb | -6.89667 | -45.88868 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cad1a5ca-d9c7-34bf-bdff-b7b42f2f4e89 | -3.16735 | -54.73631 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 235d6c51-2228-3f20-8d21-fd965d74f5b8 | -4.74578 | -55.67351 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0c8d41af-2472-30b7-8736-f6d35a5307b8 | -8.33098 | -49.12866 | 2026-10-09 05:04:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 596e6aba-7539-3e5c-98de-a4b00bf113ce | -4.6363 | -50.96111 | 2026-10-09 05:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4dd64934-5df4-331b-8db2-06f12d97ae90 | -9.80296 | -44.76945 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43a26117-904a-3bd9-963c-8427e5d82f88 | -6.23205 | -52.88607 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d592ec08-3ad7-34d3-9b49-8050f4f7a4e4 | -3.56972 | -54.67588 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb49eda6-9b51-39d8-9dec-a6517045f0cb | -6.50646 | -55.38442 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a116c90e-5334-3d2f-89c6-cc10df5c1b19 | -3.28416 | -54.07898 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f87c1e8d-65c4-3140-ba07-49cdbe768334 | -5.86427 | -44.30321 | 2026-10-09 05:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e8bdc875-3904-38cb-8d34-eaf686cd9029 | -3.58754 | -54.67876 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12231e53-3d7a-3f9c-9044-71537f0ffe63 | -2.51323 | -56.33023 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71710e27-3d64-3811-80db-c139451d0b0c | -4.09924 | -54.02149 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eaef3bf8-2530-3c80-acbc-31f15ee88109 | -2.99036 | -53.84399 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01ccb97a-0843-3f35-8a91-fbb61c25b4d3 | -7.47315 | -42.84072 | 2026-10-09 05:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2e30bea9-23f2-3353-93fe-dc1324a1ea36 | -2.98001 | -54.06445 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 656eb196-5a6d-3cd6-acf2-216fe64d6c0d | -4.82224 | -45.83397 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a53218a5-47d1-3a7b-aa91-bed18db91fd2 | -5.09461 | -46.22402 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45563983-568b-3ed1-92f5-355cbe8bddd2 | -11.09232 | -43.99691 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 160bcafa-ba4f-327f-9f34-709e0c28243b | -6.12983 | -53.06325 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8286273a-4db7-36fe-a219-1b4f59236243 | -3.89416 | -59.43992 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d6e7917-a53e-3a31-8a43-4512e24789fd | -3.72293 | -54.22087 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9d255e07-02f4-3932-b944-df220fe3c2b2 | -2.98086 | -54.10406 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9053ba80-94cf-382b-ade3-ad3ef35e2e9a | -3.08655 | -53.93966 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecfc1263-6ffb-3ebc-95a2-4ce9c68c16ce | -4.08973 | -48.96209 | 2026-10-09 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 355568d2-6a05-30cc-afc3-25c92fc706ac | -2.39737 | -57.89645 | 2026-10-09 05:04:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 38557dd3-f4b3-3e2b-8201-77330e442a9b | -2.99604 | -54.14515 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f97576a-b0ea-3acb-b27e-4a3ae82ed6bf | -9.84764 | -47.47802 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48ef15ff-efc0-397c-962d-bdc1f7f741a8 | -5.37824 | -45.94314 | 2026-10-09 05:04:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc329088-635a-3c91-be85-429de611ab85 | -3.07942 | -53.96186 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cc3fcc1-cfd0-3856-b100-03845e8dcd07 | -3.55638 | -54.69019 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 012a4897-f6c2-32e5-8ec4-b96da694a16d | -3.09818 | -53.9337 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 76ce5b6b-ce50-3624-b1f1-69109d947417 | -4.82671 | -45.82861 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7ca692c-aa9d-3200-b27a-f8cf241d394c | -3.08431 | -54.29083 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24f15260-62c3-38dc-94ad-e12e04fd45ff | -6.23593 | -52.88313 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8a14103-ec59-391f-8946-c95a2e8b637a | -10.30486 | -46.59391 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README154.md)
