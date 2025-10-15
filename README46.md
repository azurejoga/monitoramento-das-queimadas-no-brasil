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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db61c45c-8a09-3031-9b6b-56f255096a99 | -6.8061 | -44.54107 | 2025-10-15 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3bd486c4-8168-3c6c-ae5c-66a7ad8cd1f0 | -8.21753 | -44.09541 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46a72017-ea95-38ea-b44b-f68838b080f8 | -6.05635 | -41.89508 | 2025-10-15 04:57:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| aaffd064-7306-3c3a-b879-cb32f86f7f2c | -6.88912 | -43.96853 | 2025-10-15 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70181b3c-2526-3e76-b846-2bb8dbd4f729 | -8.21912 | -44.08294 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1065dbd5-fb18-385a-bc86-3aaee5ecabd0 | -6.23321 | -44.16313 | 2025-10-15 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28e8aff6-5097-3f46-825a-5d3bb907e327 | -7.25175 | -44.9137 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a2fef5e7-f17c-33d1-9a1b-7caae6e19730 | -5.58341 | -44.7469 | 2025-10-15 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1eb9a8a1-2ed7-3bab-9004-e143f75aafa2 | -5.57806 | -44.74597 | 2025-10-15 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 242fcb92-20a4-3e34-afbb-df3085c62662 | -8.20679 | -43.99863 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f07c3e39-c774-3035-9b5a-d81bca9734ea | -5.58736 | -48.10132 | 2025-10-15 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98edf238-3d5a-3488-aee3-47d458ab4f7c | -6.3313 | -44.0149 | 2025-10-15 04:57:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02457ee1-5c00-37d9-9709-d0dd84c4ffe6 | -5.42549 | -44.21765 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0ee0a24d-750f-3df5-8ce0-6eb9b8b3eb6e | -7.03967 | -42.74124 | 2025-10-15 04:57:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f3d1cdb1-23dc-3e10-bbf5-50f912e6cac6 | -8.26024 | -43.35736 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| de3190ba-cfc4-3933-ba47-d911f36d7ca1 | -6.46253 | -41.83409 | 2025-10-15 04:57:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 76773624-2aae-3baf-8416-93856c0dd688 | -5.86532 | -43.85762 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 22d8cc9d-8650-3e6e-970d-89b31a4ae971 | -8.21782 | -44.09412 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d46b1357-8780-3aee-9e9a-8f7229a92789 | -5.86424 | -43.86537 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6009408-93fe-39af-a04d-6bb3b430c053 | -6.8949 | -43.96924 | 2025-10-15 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94cf85b0-27e1-3d28-94f6-66ce399bf408 | -8.28171 | -43.38936 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fa32eb54-fd03-3f40-85f9-319b65c2912d | -8.18333 | -44.04103 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e113ce8-a0e2-36b4-9ec6-2fd8ca8d1680 | -6.42983 | -41.82907 | 2025-10-15 04:57:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ebe037ae-7958-3882-899d-e632a2c970ed | -7.94575 | -44.13521 | 2025-10-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5b875b60-fc9b-3b5c-94e9-53ce4bd3bc21 | -8.21838 | -44.08997 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75d452ad-84c0-3a13-b520-04d0ad8e0aa3 | -7.57092 | -42.68811 | 2025-10-15 04:57:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d2279c46-bd0d-364b-a003-b48360dd1df7 | -8.2244 | -44.08801 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b6f6617-0178-3170-9ade-0f08dd575abe | -6.63489 | -43.92252 | 2025-10-15 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5a9cb2e7-75ea-31fa-9b0a-9903a44e5704 | -5.26322 | -45.61228 | 2025-10-15 04:57:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f52461cb-43e9-3f20-8768-7612fec06bb0 | -8.8603 | -49.89211 | 2025-10-15 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0030629-f331-3e7f-a236-44c525a6d9db | -5.42952 | -44.22958 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f7b3ab03-5f04-3503-a563-4aa092e2786a | -7.92841 | -44.1327 | 2025-10-15 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d92e1ade-538d-362e-8fbf-af80f3409efc | -8.72723 | -43.86143 | 2025-10-15 04:57:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d002023c-d702-35ec-9b96-fee41d5d5fe5 | -8.22362 | -44.09505 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe1b2029-eb74-3968-84fa-06dfad8d8a35 | -5.83778 | -42.33461 | 2025-10-15 04:57:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 0abbda15-845b-39b5-bb64-dd0f4a29ef16 | -8.82521 | -50.05399 | 2025-10-15 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 867e5bbd-a8a2-39aa-9a79-98bccde6d55e | -5.56473 | -42.99685 | 2025-10-15 04:57:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 22c883f3-0317-3e82-94f5-50d2265ba9e3 | -8.24985 | -43.34146 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| e2ca4511-9925-3d38-beea-7df4ab911733 | -5.7656 | -47.90882 | 2025-10-15 04:57:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a4ca867-7a08-3579-863d-f0cf8b5d5503 | -6.45684 | -44.58359 | 2025-10-15 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 75d62a39-9744-36f7-a4f5-b98dcfe69aff | -5.42447 | -44.22514 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2b0d08a9-58e4-38a6-b494-d67af8143b3b | -5.79715 | -43.88717 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8436fdd0-b16a-35ec-af61-7a0bf29793eb | -6.57278 | -42.96232 | 2025-10-15 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eccf5534-6e83-3afd-917f-36cdc087eb0d | -9.01308 | -62.00718 | 2025-10-15 04:57:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a04a9eb-e3d2-3174-b80a-40c9c96e52cb | -6.55545 | -43.93663 | 2025-10-15 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f697ff5-6d33-3794-b43a-00d31cd9a153 | -5.86481 | -43.8613 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a3c74e35-a331-3b1e-9890-f2c2987de44a | -5.24882 | -44.46979 | 2025-10-15 04:57:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e96674be-26fc-382b-8b43-9c71c2b09613 | -8.21806 | -44.09126 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d8b7113-7bf3-3122-bba6-dea7dd23f618 | -5.43003 | -44.22589 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f8fba8d4-3e46-3279-ab55-46fb666c2d6e | -5.39417 | -44.04255 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2ce5770e-302f-30c7-81eb-a55b193d490f | -5.1696 | -45.16779 | 2025-10-15 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f228359-0f8f-36c3-baf3-30c662172732 | -5.42396 | -44.22884 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 75e75a33-a3fe-3a75-aaa3-2cef5e9c1c81 | -7.495 | -42.14198 | 2025-10-15 04:57:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3a44d170-95c3-3f87-9b02-dd20897c17a9 | -6.30044 | -42.98204 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 30af8d5c-d296-3843-ac5c-ab1ac5b9186b | -7.75369 | -42.44611 | 2025-10-15 04:57:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fa4bb2d9-126a-3ed0-a6fa-d780a74318fb | -6.57891 | -42.96314 | 2025-10-15 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 737b7133-b3d6-32cb-ba28-df27a64e1ed4 | -5.87166 | -43.85404 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 73de1f37-68f8-3c86-90c5-f0e9f6249d4a | -5.14895 | -45.69616 | 2025-10-15 04:57:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f397317-dd9a-381b-bf0f-ef3d413471b8 | -5.83973 | -43.95757 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe4390c9-b77d-34cc-8106-e5f2ed2eb9ba | -6.30721 | -42.97786 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c6e0396f-1885-31f7-8cd3-e45846770f37 | -8.22721 | -43.32391 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3f271b6d-a474-30a3-9f1f-c34f994fc399 | -6.30659 | -42.98244 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c9a92c9a-07e4-302d-aa20-e61c0b95933f | -8.2187 | -44.04329 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d15b0e90-64fd-34c8-b613-676b9b2ad1cf | -7.48779 | -42.1466 | 2025-10-15 04:57:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 55646392-37d6-3728-a875-04a1dfd37040 | -5.7429 | -44.98688 | 2025-10-15 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb0f7a00-18a8-3912-bb05-d407005be4fd | -5.39469 | -44.03885 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 45b0fa93-e5eb-3dd3-b7c2-ea7b93e1f126 | -5.87798 | -43.86248 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3ffc2f0b-560f-3939-8304-45915647f1a7 | -5.65604 | -51.30189 | 2025-10-15 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef88bebf-541a-3ece-83c9-20bbd7fae835 | -7.07566 | -41.95592 | 2025-10-15 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9b0dab8b-0768-3297-879a-61ba27ad49e1 | -5.43662 | -44.21912 | 2025-10-15 04:57:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| df710403-658e-3961-95cb-2840b2bde38b | -8.19938 | -44.09911 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5e08994e-5b82-31cb-9a0d-64cbf5b96b5c | -5.73869 | -44.9854 | 2025-10-15 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 10508405-d48d-3f20-92a2-102e65cdaa3b | -5.87274 | -43.84634 | 2025-10-15 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f92a05bd-40f6-3a75-800b-34a0be57c720 | -9.25455 | -44.36443 | 2025-10-15 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f81f073-8d36-3fb5-b629-ac6111e59b24 | -10.04597 | -48.70873 | 2025-10-15 04:57:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ce2cc49-8438-32b2-943c-55a718127dfb | -5.58923 | -44.74447 | 2025-10-15 04:57:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a36f361f-23d5-39de-a5ce-d9f13cbd27bf | -7.48112 | -42.14693 | 2025-10-15 04:57:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2523599c-ca09-3f7d-9955-e0bd3eb3cbd4 | -7.50429 | -46.64278 | 2025-10-15 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2f3098da-6deb-307b-bac6-02c040fd6790 | -8.2104 | -44.0163 | 2025-10-15 04:57:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f802e18-d77b-3ff4-b5ea-3955e3ab6f0c | -8.20829 | -43.32591 | 2025-10-15 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 292dcb56-0950-323f-9029-52751e5f1587 | -12.24927 | -50.39814 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 4f6d916c-e523-3409-a225-0f44b94af72c | -12.26185 | -50.39631 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| a585ea28-402c-3a8d-94fa-5f7f273bb262 | -17.60548 | -46.69327 | 2025-10-15 04:59:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 218bdf30-44bf-31ac-9f1e-a05ca7b6293b | -12.26637 | -50.3933 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b90fbc24-f946-32b1-bff7-aa44d5dd21c9 | -12.26234 | -50.39271 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b7a89a4-bebd-369d-b656-9856eeb6e962 | -18.20234 | -50.74038 | 2025-10-15 04:59:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65294fba-ff53-37ac-90e6-2b65cc94cc64 | -13.38478 | -43.66049 | 2025-10-15 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| eb545edc-1a96-3870-b8c4-d6b25644f5dc | -15.87223 | -53.98007 | 2025-10-15 04:59:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1586802c-7688-304d-bdfa-fac94d1d3715 | -12.25182 | -50.40952 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c14f42e1-3629-3a96-a213-ea9bf3344e20 | -13.48002 | -43.69872 | 2025-10-15 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 69b3f016-8d5d-3a22-a316-a94d9fafbcd0 | -12.20207 | -50.41321 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a0c5b26-9171-3f2b-8a5c-6c238e53c5dc | -15.85898 | -53.99815 | 2025-10-15 04:59:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 503719ee-cab7-3109-baba-a7179dd8d359 | -12.25782 | -50.39573 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 894c6c45-7adf-3d71-8272-f999ddf028c0 | -18.2018 | -50.74467 | 2025-10-15 04:59:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5eb816a-318c-3828-91a7-5aa59f48f610 | -13.36631 | -43.63407 | 2025-10-15 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a1bedf09-8766-3fa3-9f49-ef5a9fde0af3 | -12.25987 | -50.41069 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c914c04b-1925-38c9-9c92-46e3d3bd9974 | -12.26086 | -50.4035 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d06eb832-e6bf-32d9-909e-5e38a7c5a38c | -13.36571 | -43.6394 | 2025-10-15 04:59:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 132b12b4-143f-3b62-ad0b-290c6ef1376b | -12.24682 | -50.41611 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21ec0ecf-8a2d-3d34-b46e-3727933bb3c2 | -12.26842 | -50.40828 | 2025-10-15 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |


[Clique aqui para ver as próximas entradas](README47.md)
