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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0f960c2-0e11-3ab4-8132-59e4656bbc51 | -7.0161 | -44.6642 | 2026-09-17 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 149.4 |
| b5799703-e5dd-3342-9265-18425a0bb91d | -12.5094 | -50.8664 | 2026-09-17 11:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 0b7752c0-4e3d-3b6f-9670-d6005c6f51bd | -10.8118 | -46.1594 | 2026-09-17 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 94d48e8f-7bf2-3131-9e78-d72c89fd4720 | -12.5097 | -50.845 | 2026-09-17 11:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| f4650bfe-7f57-3758-b1ca-d7f4e33dcfd9 | -12.5118 | -50.7164 | 2026-09-17 11:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 212.8 |
| 3c4b9f01-411a-32b5-a90d-0b54666d55e2 | -9.8694 | -48.3814 | 2026-09-17 11:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 7459e133-f00f-38f4-af54-f119d1cb6bf1 | -10.8305 | -46.1796 | 2026-09-17 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 762a39ed-4b5d-3477-8785-b96c51e6cc44 | -7.0081 | -43.673 | 2026-09-17 11:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 06a4b3b1-b8f2-37a1-babe-7ced6143901b | -8.5239 | -44.5153 | 2026-09-17 11:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 6dbff78d-eccd-3624-9e3b-32f455c46efa | -7.0164 | -44.6413 | 2026-09-17 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 40b5739b-9750-3eb9-b487-1bb538538c5a | -9.5909 | -46.6437 | 2026-09-17 11:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 941c3f49-a48a-33c3-9fb5-7a255c192880 | -4.38167 | -43.3773 | 2026-09-17 11:45:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4f2c0bad-be4b-3406-b0ed-50486fec343f | -4.5639 | -42.94517 | 2026-09-17 11:45:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| a370ad5c-9770-37ff-98ad-3e01c618930c | -3.79653 | -42.94287 | 2026-09-17 11:45:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 4a0ba10c-c2fb-308f-b59c-4c8ac7a0687f | -4.38402 | -43.38443 | 2026-09-17 11:45:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f8ea0757-fd26-38ad-be6d-1aff76757681 | -4.7157 | -47.92784 | 2026-09-17 11:45:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3d759b0a-5ce6-3d5a-b677-bbff9c38e751 | 1.26627 | -50.7639 | 2026-09-17 11:45:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 518bce30-017f-3c3c-bc31-66fdf391585b | -4.71442 | -47.93674 | 2026-09-17 11:45:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d9c33af8-12dc-3547-926d-42538caa0f8e | -5.14258 | -42.90533 | 2026-09-17 11:45:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b709bf7d-589e-3837-be39-bb3ab8f14872 | -4.55311 | -42.94381 | 2026-09-17 11:45:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8321f751-de78-37ba-ac54-93e87e2f8b67 | -3.80313 | -42.93721 | 2026-09-17 11:45:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 20ebd89d-4ae2-30d4-8f22-a38ea2317353 | -2.12911 | -47.43293 | 2026-09-17 11:45:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 116003a3-a349-34f4-a3ee-8e9e6b2b0828 | -0.89747 | -47.01295 | 2026-09-17 11:45:00 | TERRA_M-M | QUATIPURU | PARÁ | Brasil | 1506112 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 535844a8-f6bc-3fd2-be65-36d532418cbb | -3.92839 | -43.12498 | 2026-09-17 11:45:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 7b80f89c-3181-3cd4-95bb-59cdb4fdef41 | -3.80128 | -42.95032 | 2026-09-17 11:45:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 07ed3942-ebd9-3bb5-9c86-27612631f2c4 | -4.69123 | -40.5069 | 2026-09-17 11:45:00 | TERRA_M-M | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| fc5a6847-fa99-3385-856a-ce759a1053d9 | -3.93017 | -43.11217 | 2026-09-17 11:45:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 13d6ed63-bbdf-34d5-8c93-2acc824fb171 | 1.26659 | -50.7698 | 2026-09-17 11:45:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 144f7af5-fc58-3641-baea-802f42e078d5 | -4.3165 | -46.53276 | 2026-09-17 11:45:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 01073bb0-515c-3dbc-8382-69bd6bbd961a | -6.9097 | -47.42382 | 2026-09-17 11:47:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 51dcc681-06f7-3d10-8b77-531cdc24ab62 | -11.6649 | -47.30118 | 2026-09-17 11:47:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4881dad2-7d6a-3507-999a-215a9438e12b | -11.88281 | -47.58859 | 2026-09-17 11:47:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 9f7596d4-e09b-3082-8c3e-af675468c56d | -7.94492 | -44.83458 | 2026-09-17 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b82e2c35-a22d-3cf9-a5b0-dcd967ed358c | -8.47845 | -44.89638 | 2026-09-17 11:47:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3dad5db7-cebc-3084-964a-106b15e9f72d | -9.45747 | -45.4508 | 2026-09-17 11:47:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| dff33cd9-f917-36a6-b051-d1c6f5cf2ef6 | -10.81487 | -46.16262 | 2026-09-17 11:47:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d7600b03-f57d-30c9-b72e-b02f8f2b2278 | -9.55345 | -48.0985 | 2026-09-17 11:47:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4c84f3d0-a511-3513-8a5c-692f24d0bd95 | -12.5089 | -50.73191 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 339a4716-1967-3327-a175-ae2b9c06fd4f | -8.02165 | -45.47179 | 2026-09-17 11:47:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 168e6ab0-d5cf-3e8b-9aa2-881937d08d28 | -12.40318 | -48.47732 | 2026-09-17 11:47:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8b9add01-a636-3e60-8af7-47804d7c67b2 | -11.32319 | -46.77054 | 2026-09-17 11:47:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 1406413b-9679-3e14-989c-68aa3fbcb990 | -11.16511 | -42.78741 | 2026-09-17 11:47:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 09f6f5d5-c415-39d9-b771-fdb347f28fc1 | -8.70004 | -45.29419 | 2026-09-17 11:47:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7482e702-f89a-3c3b-92b6-95eb585dbc98 | -7.10571 | -43.57549 | 2026-09-17 11:47:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a3a2a2ef-c41b-3f46-9c84-1a2289630fdb | -8.61302 | -44.50454 | 2026-09-17 11:47:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 32788b12-a1c3-3adb-bf5b-a805be2eecae | -8.5307 | -44.51145 | 2026-09-17 11:47:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 7511edd8-c785-3e3b-b765-8b901026c407 | -7.54425 | -48.59879 | 2026-09-17 11:47:00 | TERRA_M-M | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0a537506-3c88-3e20-9086-d5e6ac6549cb | -10.63822 | -46.06812 | 2026-09-17 11:47:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e1977232-2f30-3f72-8a2f-a4d4aaad2a47 | -9.55219 | -48.10739 | 2026-09-17 11:47:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6a4f9136-6a7a-3c62-a1ab-7189ea8779d3 | -11.48736 | -45.76919 | 2026-09-17 11:47:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 7d470acc-6671-35e4-a423-cb4e9558b7c5 | -9.84811 | -46.91678 | 2026-09-17 11:47:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7cf1195b-70da-3397-bae4-3121eae8baab | -12.43552 | -50.7948 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 594ad576-9b6a-3fe2-9e9a-be2e79dfcf9f | -11.59431 | -46.87575 | 2026-09-17 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| f5b2dbd1-48c4-3553-a484-aa089f3c6928 | -12.34167 | -50.80494 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| e19a1bf0-c8f8-37be-a083-ce0cd5710d7c | -10.79794 | -46.17557 | 2026-09-17 11:47:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 86a65b5b-a08f-3ce4-977e-24fc196def30 | -8.46637 | -44.52792 | 2026-09-17 11:47:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e72cdccc-0135-3f3a-afbf-a29af86a339a | -12.01978 | -51.45879 | 2026-09-17 11:47:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1910df39-bc08-383e-8a13-8abb32470d5d | -7.35976 | -44.48066 | 2026-09-17 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d1169e18-08d2-395f-b925-7b23ea3cc3e5 | -9.61467 | -45.33384 | 2026-09-17 11:47:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 45c89971-9643-3199-9cfd-512453049200 | -6.7854 | -45.22985 | 2026-09-17 11:47:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 07c39d38-a71d-3fc1-893e-52b2f61d1b7b | -12.39085 | -50.77791 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4ff341e3-84f5-3c6f-b287-fbc9d7ef7245 | -8.79193 | -46.89316 | 2026-09-17 11:47:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6dbc5672-06ce-3e8c-b33a-2c2c90d4a2c6 | -7.11415 | -43.09772 | 2026-09-17 11:47:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 708fa769-5e2e-31ab-b3a2-bd41371dff09 | -9.58995 | -46.65138 | 2026-09-17 11:47:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 160.3 |
| b6ed8a0f-7487-3886-83e9-36f0e704e2ed | -10.54615 | -44.85526 | 2026-09-17 11:47:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8b6e9244-15e7-3221-88c1-f56e5be9142d | -12.35883 | -50.86433 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| d21cdb96-ca36-3e03-8693-d27eeae7e84f | -12.36034 | -50.85438 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| db87a69e-9a8d-35a4-8cf7-8f2cdca4c5e6 | -8.56432 | -44.55916 | 2026-09-17 11:47:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 9483177a-79dd-30c2-9cb8-581739d3f83e | -8.61466 | -44.49232 | 2026-09-17 11:47:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 28287324-7dc3-305e-aa09-7fdcd22f0518 | -9.82824 | -48.36434 | 2026-09-17 11:47:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 5829ea27-e041-3bac-af9c-cff3f308451a | -7.07499 | -47.49532 | 2026-09-17 11:47:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6fd4fcd1-e7f7-3eca-8bf9-4dfda88cb101 | -9.11096 | -45.72471 | 2026-09-17 11:47:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 30.3 |
| b4d9ef57-fe49-3938-93d9-84f940d501df | -8.69645 | -44.87407 | 2026-09-17 11:47:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 49e6e9fc-cba0-3ed9-84ac-713f9c201d68 | -9.61318 | -45.3448 | 2026-09-17 11:47:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 17505495-d72e-3fa2-93b5-e396fafec37d | -11.17136 | -42.77686 | 2026-09-17 11:47:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| ed94d6b5-8caf-3daa-9b19-7cf27bc55a7a | -12.50186 | -50.8418 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b716d7b2-a27c-30b3-88e0-09c2c5506fbb | -8.47186 | -44.56481 | 2026-09-17 11:47:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 75003e57-c853-3c37-b962-cb8121494ee8 | -10.50705 | -46.28339 | 2026-09-17 11:47:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 7372c2dd-e4e3-3f85-b7ba-ee4ce433f383 | -5.802 | -47.24015 | 2026-09-17 11:47:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9a455d96-7b16-353a-9448-72d0cf63d7c3 | -10.31152 | -46.8964 | 2026-09-17 11:47:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8ded6ec1-b8d8-3219-aff5-7db8c81e93a7 | -12.52507 | -45.25055 | 2026-09-17 11:47:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 92902bcd-2a65-3aeb-a6b2-c4809ecf4d33 | -12.51887 | -50.85454 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 91d31959-12f0-3660-b400-d06f01330761 | -11.48588 | -45.78028 | 2026-09-17 11:47:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0091d76b-81d1-3929-b3cf-fe934eedaa16 | -5.76413 | -47.17454 | 2026-09-17 11:47:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| eeee83b5-f802-360a-a7f7-38d0eb748873 | -9.37052 | -46.83926 | 2026-09-17 11:47:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5c405914-6609-35fe-bfd0-db985dd910ef | -12.50559 | -50.69135 | 2026-09-17 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| ff0143eb-c367-35f7-893c-d1d2cc53cc45 | -8.79065 | -46.90237 | 2026-09-17 11:47:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e815a040-a71b-38aa-9f5c-7a5bce0da59c | -8.47216 | -46.87089 | 2026-09-17 11:47:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 664dfb62-5e4a-3020-a734-7409087c2ece | -7.33909 | -44.62987 | 2026-09-17 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 973f0a1c-beb1-3815-9c44-c44b7ce7cc07 | -7.65038 | -47.86209 | 2026-09-17 11:47:00 | TERRA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2184888c-6db6-3636-9a25-d86fbc7dddaf | -10.15263 | -45.36265 | 2026-09-17 11:47:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 558f4d38-0807-3bf0-9463-a971d55013e1 | -12.31098 | -47.9522 | 2026-09-17 11:47:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7d8f05e0-e1fe-3684-9dbd-49b76ce1284c | -11.16922 | -42.79465 | 2026-09-17 11:47:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 3f4c5f62-87d0-3128-9b61-b708404b8137 | -11.60219 | -50.62241 | 2026-09-17 11:47:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6fbb4d5a-765b-3a5a-b70c-11ee17a34ed0 | -11.34061 | -47.24762 | 2026-09-17 11:47:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| aa233cd6-dbab-313c-b054-d468cdf4371f | -7.64742 | -44.32088 | 2026-09-17 11:47:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 010e5447-790f-379a-9204-c632300307f7 | -12.51713 | -45.94644 | 2026-09-17 11:47:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8714812a-7961-3a71-a402-d88cbf8d48f7 | -9.92323 | -46.5097 | 2026-09-17 11:47:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0225f743-b890-3778-92ca-1de015f590fa | -11.53243 | -46.86087 | 2026-09-17 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ad2bc7b2-4309-39e2-af73-9703976e7415 | -8.02022 | -45.48216 | 2026-09-17 11:47:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |


[Clique aqui para ver as próximas entradas](README84.md)
