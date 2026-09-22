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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9fecc26-a6da-3da3-942e-5d9788561b64 | -3.55421 | -59.42379 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a221d931-d7bb-326a-9e66-2aa4b9a424c9 | -4.45114 | -55.43403 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fb08113-c5d6-3e73-b27d-8cf756526530 | -6.2974 | -57.78426 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b44f715f-5aa2-3780-b234-6609dd7a2221 | -2.4148 | -58.278 | 2026-09-22 05:23:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e02f022-d5d4-3392-b7e2-df91f658d6b1 | -6.39703 | -55.23856 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfe035e8-87cf-383a-ba99-d80ea838c042 | -3.04906 | -61.25769 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b601b383-3545-3a41-9d70-cb51066c5cea | -7.5798 | -57.6963 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e9cf112-6ebc-357a-8202-406dbabee46e | -3.33901 | -59.8546 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ebbbb3d-81d6-3cd4-b3b7-1853dca0cbd4 | -3.51109 | -59.57732 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5560bd1e-d306-3a49-97a3-a9910ad83659 | -15.35687 | -48.09877 | 2026-09-22 05:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c0e7ea0-cc37-3305-9406-e8f107053586 | -6.21194 | -57.728 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffb1af63-d188-3c05-9700-90899cb632e6 | -6.81487 | -59.43112 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab8626ac-df8c-391f-b367-19287a4dc4df | -14.04369 | -52.06165 | 2026-09-22 05:23:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9eda6428-b229-3c27-9e16-7642174fb284 | -2.90111 | -48.90276 | 2026-09-22 05:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a500dce9-a342-3371-9def-b7a7812dc573 | -6.13844 | -59.9491 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4380388e-88e9-35db-9b79-926bfe9efd6a | -11.88031 | -46.85481 | 2026-09-22 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ff067d18-7a5e-398b-a2c7-163227a4f70f | -12.95189 | -50.92088 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 819a2b80-45b0-3d3d-87f3-f4f4039c2933 | -4.85776 | -56.02293 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72156310-34da-3a0b-9fb1-04b2f2dcb760 | -6.09943 | -57.68868 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ba5ecae-2551-3e02-a9c2-c5a8f652983e | -13.92795 | -48.57186 | 2026-09-22 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87f08a59-3ddb-3ec8-ba2e-137739289016 | -9.10347 | -65.37524 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36517b72-be2d-34a1-a9f3-e8448ab082d8 | -5.38318 | -55.90402 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2cfe885-1952-394e-9995-04eb08c268af | -6.75512 | -59.06461 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1856e5ca-cb10-3e02-af88-ffce94acdd04 | -6.25136 | -57.78067 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6eee18a6-0a5b-3ecb-95a9-c39d94a51215 | -6.51518 | -58.30452 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 511034eb-154b-36e7-9623-ec72195a3e59 | -4.34402 | -55.65268 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c8c908e-cefb-3084-ad2e-b28a8757f625 | -7.13037 | -48.42762 | 2026-09-22 05:23:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ca74e72-dc7f-3c65-83a1-e2395b7cc7f3 | -6.09443 | -57.65581 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db300662-be70-318a-94b7-43852f2fc573 | -4.35076 | -55.65376 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 571b9316-723d-3422-abb2-f946a64e453a | -12.14033 | -47.39673 | 2026-09-22 05:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 63726d2c-7dd6-3b0f-b987-58c561093f1b | -10.91721 | -53.95771 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d1e7a40-bca5-3e57-a745-8aa2769421a5 | -4.54632 | -54.93248 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fab8453-bbf0-3599-8c6d-de4b7d14be9f | -4.34628 | -55.66033 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9fdf2f3-2213-3141-95a2-f0ae6ed6a419 | -14.92185 | -49.89709 | 2026-09-22 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43e309c7-5f77-3435-9c84-fc11bd0d3b8c | -11.32125 | -54.0303 | 2026-09-22 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 410db59a-c0a0-3269-bf86-ad1c4a31296f | -5.87589 | -53.63705 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b7baa0c-46c0-3524-8ae2-0233f43346e8 | -4.29956 | -56.26276 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21ec42e1-2a06-34d8-9c97-f38e5f7c235a | -6.27964 | -57.74574 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b6c42ab-19e6-38a6-8011-302d3b3c3d7f | -13.30203 | -51.79847 | 2026-09-22 05:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cf826704-e0db-3465-b74a-0f41a6742a62 | -7.32668 | -46.76754 | 2026-09-22 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a057bbb-135e-3995-a7d1-32ad2a046463 | -5.87285 | -52.06193 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57c5385f-f2f7-3730-8c5b-849e5b8b0cf6 | -6.07501 | -57.6278 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8eb79987-ce06-302f-9eb4-240af69fc90d | -6.09276 | -57.62349 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f009e83d-5952-35a0-813a-1815b555cd6d | -3.9231 | -60.55513 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 73cb2a54-7c11-36ab-ac05-11293f77a79b | -6.35143 | -57.89 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cbd5947-2776-314f-81c4-16489823e27f | -6.00454 | -57.713 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4f6ff01-8ceb-3e7f-b790-db45d7656b4e | -5.80572 | -57.73099 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82aa3e78-b4e8-35f4-bc11-c07e894384a8 | -3.29219 | -57.85555 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5f1aefd5-3552-34ea-9f09-bb9adf3e3444 | -12.35017 | -50.21985 | 2026-09-22 05:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19e7b7f3-4626-3f22-b39a-1913e02bd262 | -10.09782 | -69.13309 | 2026-09-22 05:23:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 159b28b7-0615-3563-981e-bc50ff922a05 | -4.9628 | -55.82461 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af724722-756a-3c42-a379-eb21c947ff4f | -7.60966 | -55.34571 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e242d78-064d-3f7e-a244-ca8a3749bcde | -6.33668 | -60.01599 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b7e7353-fd65-388d-a18d-80d53949afc6 | -5.93829 | -57.70549 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf7c58fe-7222-3a9e-a81d-2bf68dd0909b | -6.16422 | -57.7061 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d08043f-4184-31f8-837b-144a10f1f5e9 | -12.77208 | -52.84496 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01b6812a-c915-32eb-aacf-15b2adb66a62 | -5.75569 | -45.09358 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| bcc57a29-43da-3fc4-a061-8bd368da8541 | -6.8598 | -59.90822 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5cd3bcc9-ae43-3303-8506-8a5a96782534 | -6.64867 | -59.96404 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b96951ec-99cd-3a7d-8911-8087d07983f9 | -7.58035 | -57.6714 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0140c609-0bd2-36f0-92ef-3fa1b05fb9a7 | -6.12757 | -57.40473 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0cfd8a8-4ce1-382a-bed7-b0f64944c660 | -10.42734 | -57.22779 | 2026-09-22 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6525c4a9-f78d-3f1e-ad9b-2054745558a3 | -6.73945 | -59.42316 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5de23b06-0c0a-348f-8016-beee78854cf9 | -7.3249 | -55.59664 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3f3971ab-cddb-323b-b9fe-05373c38afa2 | -2.67425 | -54.96952 | 2026-09-22 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1a97e6a5-c236-3ce3-bfda-f89cc9f57a79 | -7.40215 | -44.81421 | 2026-09-22 05:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a48abc2-6ad8-3b27-b271-d20e8d085129 | -10.93552 | -58.33513 | 2026-09-22 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 19db026e-d04a-3b7c-8f97-2d12ea4a1e9e | -9.567 | -66.04126 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 846c9de6-be73-30ae-b61d-48d983d25442 | -6.62497 | -59.93189 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6fdf2f23-f5c9-33af-b3ee-bfbd81db9efe | -6.86682 | -59.90936 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 159d1c49-c4a8-311b-aa1f-9f88f89d8846 | -6.35757 | -58.27967 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24e9b4a5-7dc9-3c3c-840a-0d2c65acdc36 | -12.24091 | -54.28413 | 2026-09-22 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf44549d-0218-37fa-9a07-7706f613842b | -7.13526 | -48.43182 | 2026-09-22 05:23:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89e4ed84-4669-317f-9ccc-203fbd818211 | -3.44938 | -51.54699 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31691f50-3d8b-3596-90dd-0561bf837437 | -6.30129 | -57.73846 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98ed7f39-a695-3233-9e4c-0472e6ef5b35 | -11.96266 | -64.04181 | 2026-09-22 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a87ca1e-4fbc-3d7d-b4de-dff9c1cea4e1 | -14.6669 | -45.67638 | 2026-09-22 05:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 98c19a54-04c4-3d62-98bd-6e5905af35e3 | -3.16308 | -60.57713 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae2c28de-cc9b-3229-be01-cb184003e864 | -6.86456 | -59.90104 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2cbee8e8-f623-3345-b725-f87d7ba81d90 | -6.29352 | -57.74437 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a9a1b00-0fa8-33e0-a497-5f22d3991321 | -7.23785 | -55.59899 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b767d879-f4d1-3b77-9f2a-ce951a06fd15 | -2.40676 | -58.2843 | 2026-09-22 05:23:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12d0a0ee-68b0-3564-af2f-ee67814ffe39 | -4.95606 | -55.82355 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9e506af-9611-3a01-a5fa-bd2a8a16664c | -6.30517 | -57.73552 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64c80728-9ed5-3c9a-8cbf-7f67ce07f03d | -6.81751 | -59.45849 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de001756-0d7d-3687-b34c-71cac210af5b | -10.86653 | -57.16343 | 2026-09-22 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9faa0342-e054-3a06-b4fb-6afd71a2d935 | -6.24177 | -51.00972 | 2026-09-22 05:23:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7ffdf925-34a9-35d7-a77b-3d3c481d8c40 | -5.37588 | -55.90655 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc7b318d-c9b1-37c4-9862-da6b20fe1485 | -3.71889 | -51.26995 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1742a42a-a5cd-387f-aff4-864291bad7d1 | -12.87296 | -50.93738 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 57c53f9f-bfe0-361e-8cca-ad5095344c16 | -1.27185 | -57.02914 | 2026-09-22 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adb76bcb-9025-3c49-9f21-b721f2ca2549 | -6.57963 | -44.15879 | 2026-09-22 05:23:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c382ac5d-b01b-3343-8b29-5f53f8dccbb9 | -3.2424 | -53.95195 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8906fcb3-a99e-32e0-aa6b-256268bc1cc0 | -8.18737 | -54.73972 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f657fd70-dda0-3905-a988-3ed40a3a9d75 | -5.41423 | -60.21683 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea54f74e-6670-3547-8a7b-2c7505a089cf | -1.20658 | -54.01323 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02f4109c-9123-3bbe-9f5d-77ef13022e4c | -7.53599 | -47.12537 | 2026-09-22 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bc3f2f0-3074-3418-a5d1-a17e93a3c4ad | -4.94595 | -55.822 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3569490c-76e1-33e9-9fd2-0a886efc9488 | -4.45395 | -55.43819 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57b64c9a-0a1c-3197-947c-4454841a2965 | -2.2084 | -56.09065 | 2026-09-22 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README79.md)
