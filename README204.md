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

## Dados Diários - Página 204

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cca37997-3b25-3ac3-a0db-e0b944b00643 | -6.48493 | -52.8236 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f5c87999-b373-3e83-ad18-f2eaeee5fcd3 | -17.02584 | -45.92521 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6b50176b-88e3-3b21-a399-2d43c0a8827a | -7.75049 | -54.96063 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 391bb0df-e7de-333a-82ce-b54367eb5809 | -4.67812 | -43.71634 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b2f7d122-4270-3dd7-b9e9-e1ea1cdbfb2d | -10.78425 | -46.55343 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6fe70882-0c49-3db1-9702-0cb5d901105b | -5.24873 | -50.91671 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| cf04ce58-acc0-3a22-8dd2-fc0f79c271cd | -7.53521 | -45.87394 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b89e3211-bdf0-311d-be54-615105fbadb0 | -10.1954 | -46.69428 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 996baa5f-9043-34ec-a009-ee30bef981c0 | -10.29711 | -47.82948 | 2026-10-07 16:37:00 | NPP-375 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8e07d889-67da-3509-ad8f-8a9ed5779153 | -2.94056 | -41.41455 | 2026-10-07 16:37:00 | NPP-375 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| b27322dc-48e8-332d-a762-4712d4406ed8 | -3.19886 | -42.95472 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| adc39a7d-4957-3637-b21c-7058280de8f1 | -3.28457 | -42.26468 | 2026-10-07 16:37:00 | NPP-375 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bb30bb9f-2f2f-3583-a1e1-59a695328f58 | -3.77249 | -41.77107 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 14ef187b-8d34-385f-8883-c4d6517af655 | -6.96417 | -56.41584 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 87e30444-fe98-3930-8959-d29b34669157 | -7.47733 | -42.81471 | 2026-10-07 16:37:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 99430527-11b2-35cf-aa2e-faf2217d5d31 | -3.88043 | -44.11407 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 273d68e7-f61d-31d8-a57f-84301366f157 | -9.37657 | -45.93034 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 3a470e38-0161-3e29-8331-dc9edbe8ebd6 | -9.80794 | -44.78018 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 32ee72dc-7ce0-3148-a552-ae12407e1f1c | -9.18604 | -45.68729 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a3d2f198-3864-3b5e-ac95-62ab7eedb16b | -11.10198 | -47.63353 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 51c0c855-7367-3fda-b52d-e75a9072b7c1 | -9.37419 | -50.65366 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6e0d1e6d-25d8-3dea-a56b-a5f800363e7a | -6.67797 | -44.94877 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e44e6578-3bc0-3149-b44d-8beae9fff095 | -14.57813 | -40.73778 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 92bc6d45-2433-3fb9-86e1-9f8a98fee9f2 | -6.82895 | -39.54951 | 2026-10-07 16:37:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 89822e64-813e-3c42-a6c6-d3ed45865d58 | -6.33033 | -55.32476 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0674e894-104f-31dc-82bb-b1ed0d9ddc79 | -6.54426 | -44.09129 | 2026-10-07 16:37:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9995bd89-9239-352a-a787-41609293273f | -7.70848 | -45.44893 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 00d51be1-f21f-3af8-90a9-c57f52373857 | -3.91614 | -44.65716 | 2026-10-07 16:37:00 | NPP-375 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 63274b07-040b-319f-b8a2-8f35bf6a44e1 | -6.03867 | -42.27468 | 2026-10-07 16:37:00 | NPP-375 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1f2084d8-f58e-38db-a9f2-f2c728432be9 | -5.38291 | -44.1664 | 2026-10-07 16:37:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1f857332-c0e4-3858-9efc-8615c05077df | -6.85454 | -43.88591 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 735ddc20-a381-38d5-9793-ef44758c0b6d | -3.57875 | -39.14132 | 2026-10-07 16:37:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cdcc2745-4936-3c48-8a2f-eafecb3ebcfb | -3.10688 | -41.16706 | 2026-10-07 16:37:00 | NPP-375 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a9ca8e62-0e09-3e64-b56d-506b52f149c6 | -14.70303 | -41.26519 | 2026-10-07 16:37:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 166.8 |
| fa25bfb7-d6fb-38f6-bccd-023bd5fb18be | -6.52381 | -55.28173 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 16b31071-1a68-3641-aa65-463ccc4e53b6 | -5.30937 | -49.48587 | 2026-10-07 16:37:00 | NPP-375 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 886fe24f-7221-3fcf-b368-f5535a7a0293 | -6.35444 | -43.33781 | 2026-10-07 16:37:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 43296122-8497-350f-beee-fe2515b8a98c | -15.91347 | -42.36643 | 2026-10-07 16:37:00 | NPP-375 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a5be2e9c-7c85-301e-8477-169d7214bb72 | -3.76469 | -44.65993 | 2026-10-07 16:37:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| b9fb5d78-9ab7-3f05-8852-a05a48ef19bc | -5.32673 | -45.68224 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 9eed3329-f5d9-3670-a08c-0345ca0884da | -3.1972 | -42.00627 | 2026-10-07 16:37:00 | NPP-375 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fd3455e2-0c63-3a20-aca9-4abdf60acecf | -8.00875 | -47.17367 | 2026-10-07 16:37:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| eb1106f4-4288-3f3f-b199-ee5b9df2d212 | -7.33445 | -50.82383 | 2026-10-07 16:37:00 | NPP-375 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ca1e1779-72c4-3766-b6c6-3994ab95bc0d | -17.19923 | -43.5287 | 2026-10-07 16:37:00 | NPP-375 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fc0347d7-e414-3399-9d91-c8bcdec997d2 | -6.48055 | -46.61854 | 2026-10-07 16:37:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| bb545be3-9985-3c9e-8697-62bb91e6c677 | -7.00906 | -44.05679 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 624a0a1c-81ad-323f-ab27-55b62cdbeb88 | -3.59723 | -43.00213 | 2026-10-07 16:37:00 | NPP-375 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b1b65925-a596-3d20-8c1a-f00916466e14 | -6.27462 | -52.84461 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| ddbe757e-d230-3fe1-9052-7cf8e9549d8d | -6.98289 | -43.29137 | 2026-10-07 16:37:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| af8699c5-1c86-3d8d-8b41-d0ed4682a8a7 | -3.76748 | -44.65598 | 2026-10-07 16:37:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| f650b5f8-3cf6-3b4f-9ea5-cbec36f42c1b | -6.93997 | -45.27614 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| d6deacd9-45e7-37ae-8149-4b365d064a95 | -5.50861 | -42.83555 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 861dfe5a-c5cc-3895-b483-c08397537391 | -7.00415 | -44.04689 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cf153b6c-9c02-3787-91f2-b550a89a1e11 | -3.29462 | -42.28316 | 2026-10-07 16:37:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 4060a7e2-2074-3180-87dc-ef994a14c1d3 | -3.76172 | -40.83702 | 2026-10-07 16:37:00 | NPP-375 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| e96781da-aca4-3ec0-9251-f0bdf03c31a9 | -3.92537 | -40.38555 | 2026-10-07 16:37:00 | NPP-375 | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 4a86f669-ee45-3178-92e0-63b7bb1b8f53 | -6.68185 | -44.95181 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0e2a4b48-0ac5-3fc6-ac04-3cbf75f11104 | -7.69393 | -44.74363 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1cf11e9b-f11f-3903-8097-d6afd6c9b5e3 | -5.81499 | -53.83794 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 85f2e51c-d52e-3aa0-aee6-e98ce1530d63 | -7.76147 | -43.82348 | 2026-10-07 16:37:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b9b6b381-60ab-3902-9f85-841c3382c0ea | -10.49552 | -47.28989 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 982e821c-9d3d-3ec9-bd3e-ef4a32610bbf | -3.68172 | -38.81486 | 2026-10-07 16:37:00 | NPP-375 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 737eee9d-46b0-30b1-b8a2-e96786b2da10 | -5.33365 | -48.55459 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0ce6c956-50bf-3665-bbf9-440169937b21 | -3.84134 | -42.64124 | 2026-10-07 16:37:00 | NPP-375 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 16061da0-adf2-3934-90cf-7f1750399fe1 | -3.90425 | -44.11399 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 3bfce942-b96b-3811-9acb-ce4e11e280cb | -8.76064 | -47.57778 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ffb1b6a7-0887-3b39-b63d-f196d4d45311 | -3.62474 | -42.79755 | 2026-10-07 16:37:00 | NPP-375 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d342cc35-d335-39ea-9d36-9c041bf4ffac | -6.13169 | -47.92272 | 2026-10-07 16:37:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| aec291e2-9918-3aa5-8a69-92654f0568d5 | -11.15 | -47.29619 | 2026-10-07 16:37:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ebca796a-0769-331e-b9c9-aa2d5d0c42db | -15.97052 | -40.7077 | 2026-10-07 16:37:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a27390c7-343f-35ec-91a0-9f0398c4f935 | -6.0967 | -53.89349 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0bf7733c-c401-3fad-ac3c-ee72130ffe31 | -8.33808 | -44.73749 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6120d6ea-a756-36e9-a713-1fa7f0de4af5 | -16.17472 | -41.6853 | 2026-10-07 16:37:00 | NPP-375 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 04b998d2-5489-373e-859d-08fc3273abb9 | -3.75357 | -40.03884 | 2026-10-07 16:37:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 36.0 |
| 577cbf85-fc8e-3264-9533-37f108076287 | -10.07542 | -45.9886 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 622dcd03-824f-31f1-bff3-f263a8399f8c | -6.71995 | -44.00319 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a4aeec4c-d26b-322f-991c-b132243d0ddc | -5.48604 | -42.84639 | 2026-10-07 16:37:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 365d6ff0-9dc2-3e3b-b587-3c0a18f3d6cf | -9.95483 | -43.55829 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 49c3322c-451c-3038-be93-dccca4b7ab22 | -11.1689 | -49.47995 | 2026-10-07 16:37:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0ce605dc-f2a1-37c5-8fc2-bbf598b32a0f | -5.24639 | -47.93568 | 2026-10-07 16:37:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e77a111-46cf-3866-85c2-065aea9657ce | -4.63083 | -48.85677 | 2026-10-07 16:37:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 0b8229c1-32c5-3546-86c3-495b06f676a4 | -8.79552 | -49.41891 | 2026-10-07 16:37:00 | NPP-375 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c0120def-f060-3b86-a69f-cd5642f62713 | -3.08393 | -42.61955 | 2026-10-07 16:37:00 | NPP-375 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7f3b2d29-5d67-3897-a10b-e92190694b96 | -6.90617 | -47.39354 | 2026-10-07 16:37:00 | NPP-375 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8b3d36c9-78d1-3680-89fa-2ebfc6d45a98 | -3.28421 | -42.58455 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d9b00fc8-2a6c-3147-8049-5e885d8fda83 | -6.68275 | -52.86253 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1e9caebc-d2a6-3b5e-9c79-611f2aa2b802 | -5.96043 | -46.36648 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 6aa51a33-a60b-3c82-94fb-7103d4c40c0b | -5.56174 | -45.66102 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d2104747-2a53-3abf-bbc0-989306099295 | -11.15329 | -46.11491 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| aafe6c00-a794-3efa-a0ba-2d2ec7bce439 | -6.14702 | -39.41977 | 2026-10-07 16:37:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 1543ff5d-48af-3e01-8f48-f89adf82895c | -6.73281 | -55.12194 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| e7d18b30-016e-3072-8994-a9435396c07d | -8.33033 | -51.30876 | 2026-10-07 16:37:00 | NPP-375 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| ea3a1d2e-6f36-339f-9b71-7b55ecd80b2f | -7.87905 | -54.99401 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 5c8a190d-1e71-3759-92cd-0a06e9c7af77 | -6.03434 | -43.02348 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d7532983-bbd6-3d4c-a57c-71b4d1cf339f | -7.16388 | -43.76552 | 2026-10-07 16:37:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8c3caf2b-5ad9-361e-9696-ea575289a55e | -3.62785 | -39.41532 | 2026-10-07 16:37:00 | NPP-375 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 02b95379-1a04-3e39-84d2-35dd35fa203a | -7.41237 | -35.09201 | 2026-10-07 16:37:00 | NPP-375 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 8013f2e3-e464-30a6-892f-48493c645547 | -5.74276 | -41.72797 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4dc0d363-d1d1-3ea3-90c0-9203aca22967 | -17.02901 | -45.91974 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 297d46e2-4c21-361d-b1ad-76e74504c655 | -10.3515 | -46.25497 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |


[Clique aqui para ver as próximas entradas](README205.md)
