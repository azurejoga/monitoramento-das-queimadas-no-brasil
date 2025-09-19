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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1f713e0-0b02-37ed-b168-3a1b0785e858 | -7.58408 | -45.48266 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a4b1009-24d6-303e-ad93-b0069af97824 | -7.54369 | -45.50795 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08aefc4c-7e1e-38b4-8f9c-3c1342980095 | -5.79904 | -45.36966 | 2025-09-19 03:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 229b21ea-0f0d-3edc-a7ea-78e2906e58f6 | -7.56659 | -45.49982 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 849d1507-33e0-370a-a342-fa6e3150c3e1 | -5.5013 | -37.79526 | 2025-09-19 03:32:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 16f7da2a-aab8-3dd7-861a-22c914964aa5 | -7.57856 | -45.47444 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0665c68e-87d6-3825-97b2-0e43e06b8c5f | -7.70978 | -44.40099 | 2025-09-19 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e841e587-3491-30ee-b224-6b7001ccb2e9 | -7.55304 | -45.49642 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a67d62e-6923-3a4e-af41-1924cfbc32a6 | -3.89555 | -40.83252 | 2025-09-19 03:32:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 69b449bf-1176-3abd-a964-f37822ba612d | -7.55652 | -44.74457 | 2025-09-19 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 219ff326-7899-3688-83d4-56c418948154 | -8.13637 | -44.46906 | 2025-09-19 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3eeb2158-d3e1-3318-98ca-2d61e8939e0b | -7.23245 | -39.35561 | 2025-09-19 03:32:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2ee534f7-6607-348f-9056-d8356c06f1dc | -7.5542 | -45.49016 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c95f9f7-ea7a-3a7c-8c55-a9982cea577c | -6.9099 | -44.77834 | 2025-09-19 03:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 83dda31a-5570-378d-8587-363e5db4479c | -6.56542 | -37.17766 | 2025-09-19 03:32:00 | NPP-375D | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c9b525a4-a6be-3b9b-8c3a-f26c504add35 | -8.13542 | -44.47417 | 2025-09-19 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 15c973b0-f7bd-3564-bd9d-8767db9dcd10 | -6.72285 | -38.25649 | 2025-09-19 03:32:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0d29d712-60ee-3b6a-8fe7-77639d7aac90 | -8.13711 | -44.47091 | 2025-09-19 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6425f8de-c6d5-3104-9071-4f34d8a67f67 | -7.70275 | -44.47173 | 2025-09-19 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65e22e91-c9a4-3411-8a81-0f27f4c15b1a | -3.89497 | -40.8359 | 2025-09-19 03:32:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dcc5fc71-8f3c-3594-8c4a-80c8f603d06b | -7.23712 | -39.35641 | 2025-09-19 03:32:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b7c4c4db-4688-3186-a28c-b14a2ea126f3 | -8.37793 | -44.67558 | 2025-09-19 03:32:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa1d76ad-fab0-3429-a6ac-9b77b7795fa0 | -7.54386 | -45.50757 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 52585775-16ca-3253-b11c-673ab4e4ff7d | -6.1653 | -45.11183 | 2025-09-19 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e78d0f94-4544-329f-a9e3-800d437e894c | -6.17217 | -45.11301 | 2025-09-19 03:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14e800df-1b7a-30b2-a092-85cab62a0c9c | -7.56226 | -45.48538 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2b8679f5-0651-3ef2-886e-06c8847304c3 | -6.83324 | -41.04282 | 2025-09-19 03:32:00 | NPP-375D | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 29b5ca73-18d3-3148-91ac-ee342763f530 | -6.90048 | -44.77577 | 2025-09-19 03:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 76e60e71-909c-3bde-be0a-e080670b1a61 | -7.55857 | -45.50456 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3e5c5908-2d76-3f7d-b1bd-43691b27fe5e | -7.35881 | -44.59262 | 2025-09-19 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f25895d3-6a44-3ebb-b7dc-1f80a4b1d8e4 | -6.90707 | -44.77729 | 2025-09-19 03:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 21eebed6-8477-3cc8-9e0c-94be8c0fabe6 | -6.07964 | -37.46631 | 2025-09-19 03:32:00 | NPP-375D | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4ac4a4f6-285c-305a-affc-15c0965870c6 | -3.85488 | -40.34829 | 2025-09-19 03:32:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cb819342-cde7-3a82-aea8-eece25554126 | -6.19281 | -41.19612 | 2025-09-19 03:32:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1be69f0a-5e8d-3015-af8c-dec4425e0d9a | -7.56909 | -45.48678 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 69b66fde-198e-3a7c-a86d-d2e209f753d4 | -3.85698 | -40.34538 | 2025-09-19 03:32:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 46369ce4-8729-387e-a7e9-74c9926a1bfb | -5.78239 | -38.0462 | 2025-09-19 03:32:00 | NPP-375D | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0b9bbe6a-82f5-3baa-ab21-7f37969a4d7a | -7.92824 | -43.88852 | 2025-09-19 03:32:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20162b3a-c54f-3214-8aab-23772b5e1865 | -3.85544 | -40.34504 | 2025-09-19 03:32:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5a455d55-0c82-3eaf-be0e-f15c1f3fcede | -4.77932 | -42.75526 | 2025-09-19 03:32:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 0050b423-eab0-340f-8d24-1c1e3919f81e | -7.36 | -44.58647 | 2025-09-19 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd448e21-5695-33a3-9b2e-11b4e5050a84 | -7.56778 | -45.4936 | 2025-09-19 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3b9af1d5-8ac6-3aa6-96e0-398a3275cc76 | -7.92722 | -43.89383 | 2025-09-19 03:32:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 415db754-0b1a-34b9-95be-32646c2b0fbb | -11.9822 | -43.38108 | 2025-09-19 03:34:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df69fe80-c514-3cf6-983f-87de36a9315d | -11.08928 | -41.06612 | 2025-09-19 03:34:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| f86143f3-794f-3d36-9a97-73adba22e9b6 | -14.13312 | -44.59592 | 2025-09-19 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98931152-de58-38c1-b199-ddac1a5de239 | -14.55113 | -45.52965 | 2025-09-19 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf2cc4d6-eb08-3b87-9350-481818efb800 | -14.69249 | -43.98196 | 2025-09-19 03:34:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f6f74416-a4d1-34c6-83de-121b576a94b9 | -12.09851 | -44.81544 | 2025-09-19 03:34:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f0662eb-b114-3074-9ec6-87a113e3f411 | -9.1697 | -45.31742 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 95487c1a-88f3-34ad-938b-ad78cf506b80 | -10.37342 | -42.46251 | 2025-09-19 03:34:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cc01c653-7d05-3416-ab38-3a69c6948d2a | -11.93383 | -38.33333 | 2025-09-19 03:34:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9e3ebaff-87c1-30de-8726-32837ea26f97 | -11.18289 | -45.36943 | 2025-09-19 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29703615-b437-3ae9-a893-92ef00adbef0 | -10.19684 | -43.85501 | 2025-09-19 03:34:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 637c0c01-821e-3338-bb99-a265b7ba748a | -11.08826 | -41.07162 | 2025-09-19 03:34:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 67727a32-e090-390c-ab26-8719f4110f6e | -10.1019 | -40.93283 | 2025-09-19 03:34:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7097c38b-b243-31e8-874c-a849f1a59666 | -13.16818 | -44.59844 | 2025-09-19 03:34:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a57482c7-5dc5-3610-adf0-82c31c7f3134 | -12.61569 | -45.07266 | 2025-09-19 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d947257-e457-37f5-8228-cc128d99be41 | -9.1774 | -45.31305 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1de668e7-2900-3ebd-ac0d-63a1d29ff500 | -12.09956 | -44.8102 | 2025-09-19 03:34:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75af0cf6-1a34-336d-b178-eeedbfc2b57c | -14.55014 | -45.53438 | 2025-09-19 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29b5bc9a-db59-3660-8c57-b9e0ab30e495 | -12.08739 | -44.83896 | 2025-09-19 03:34:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97be87ff-fd0c-3b51-b9e2-f93587bbf5a9 | -9.16638 | -45.31703 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cadab73f-c1e4-341b-b144-767160f61785 | -11.18258 | -45.36813 | 2025-09-19 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13c6f93c-08e7-3221-ab06-8dbcce4e07cc | -9.17187 | -45.32397 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9fd65f04-1cbe-3c8b-bdba-10a86943d8be | -11.18149 | -45.3736 | 2025-09-19 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe7bc994-ce70-3171-ab06-5f9ea0295571 | -12.35113 | -47.0523 | 2025-09-19 03:34:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c358929-d9b6-3827-84b4-700e99cbf271 | -12.62178 | -45.07423 | 2025-09-19 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea138260-dc55-3619-964e-f12aedf4d12b | -9.18073 | -45.31394 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7dfd08f3-8861-32ec-b506-e6efa9ccb021 | -11.41489 | -41.41421 | 2025-09-19 03:34:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f0882390-2117-38aa-8f9c-7a4dfbf4d114 | -10.92011 | -45.64689 | 2025-09-19 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf7024b6-8aa8-3e47-9410-44687ad38d33 | -9.18186 | -45.30825 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 503801a7-5907-3c94-8f42-3bc9623affca | -14.58193 | -45.17238 | 2025-09-19 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 549f89a1-550b-358e-8127-a6e003f719c4 | -9.14441 | -44.85444 | 2025-09-19 03:34:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 473c2197-f1d9-3ddd-8563-137dd25a873a | -10.19772 | -43.85038 | 2025-09-19 03:34:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1994b1d3-cd36-3998-b9e7-c4f407bd3b5b | -10.92248 | -45.66013 | 2025-09-19 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1def956a-1e43-3b89-80ac-9755411d3c6b | -9.17522 | -45.32442 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 399cdc9a-01a1-3ecc-964e-8e8bf07919bc | -9.173 | -45.3183 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1b3ac1ed-6cc1-35ad-a0b2-f61f58096dfa | -14.2486 | -44.38577 | 2025-09-19 03:34:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82e11e1c-0a28-3827-9888-4126293745ff | -11.46076 | -43.54663 | 2025-09-19 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 183e97d0-469a-31c7-b494-a9d3a9ee4cd1 | -9.14326 | -44.86045 | 2025-09-19 03:34:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e152d95-687d-3111-bbed-a4ee29fd09b9 | -12.09145 | -44.85042 | 2025-09-19 03:34:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa660726-f774-3eca-95c7-ee3012859e41 | -15.44373 | -45.45058 | 2025-09-19 03:34:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9facfe13-3747-3d84-98de-bd9690c2c7eb | -14.35538 | -42.34425 | 2025-09-19 03:34:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cbd8de47-6572-3e66-94a8-2eb8a736bf80 | -12.6203 | -45.07293 | 2025-09-19 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1669357e-74c9-3527-aefa-f9f1f5dee044 | -9.18291 | -45.32011 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 305d907a-6e46-3c30-afd2-814d99f19ee6 | -10.9179 | -45.65803 | 2025-09-19 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 578d34ad-cc73-3e7e-9764-4a0bdaf65c70 | -11.42092 | -41.40962 | 2025-09-19 03:34:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b2fe3e1c-0fab-3720-9a4a-22360e5cafe2 | -12.09247 | -44.84538 | 2025-09-19 03:34:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e521d75f-403c-3060-9bd2-88fd987d68d1 | -10.9194 | -45.64186 | 2025-09-19 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8e6f72b-d0f7-38a0-9fcd-0bc9a4bb56ee | -14.35406 | -42.34503 | 2025-09-19 03:34:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 02472444-aa00-317c-969a-3c633b5994c7 | -12.34846 | -47.05887 | 2025-09-19 03:34:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6301a28-dfb0-3806-a7c3-c2430194b302 | -11.09417 | -41.06704 | 2025-09-19 03:34:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 570ee6aa-453d-338a-aa5f-ff7e434a498d | -11.41586 | -41.41226 | 2025-09-19 03:34:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b0c9aab2-9f11-33a1-a780-c21c42882268 | -9.17736 | -45.33095 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 57ecbfab-e21b-31c8-bde6-505ed370f33c | -14.69335 | -43.98501 | 2025-09-19 03:34:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6b8cf90c-4071-3cf4-8b73-a73209b755f0 | -10.91714 | -45.65287 | 2025-09-19 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14ede934-8b55-35a7-965b-2716b96fc5bd | -14.12851 | -44.59406 | 2025-09-19 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 321c35c5-c556-3b97-874f-f2ca3c262a7f | -9.17848 | -45.32529 | 2025-09-19 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cb77b9e9-71a8-332e-b087-dc519db098f5 | -12.10476 | -44.84759 | 2025-09-19 03:34:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README7.md)
