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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7190bfbb-55f4-3816-aa8d-726a4470a674 | -2.95421 | -50.31317 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d534cc9-5a8b-339b-8ceb-fcabcbd1d54f | -2.95644 | -50.32059 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4ee7ecc-d5f7-374f-aca9-e635d9dd5d31 | -4.51404 | -54.98307 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9f3ab40-c16e-3f9b-b5f4-887de5d13329 | -3.44081 | -58.20354 | 2026-09-18 04:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a92f3432-7cee-3526-9592-cc79729faa8a | -4.58849 | -42.96056 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fd8eb9e9-bb66-3703-99ed-8c1ded41e86f | -3.37965 | -50.44763 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 941d9b26-6bbf-3403-95ec-dc4af784d5eb | -2.95589 | -50.32404 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48baaf2f-69e8-35a1-bf4a-24b5abb592b0 | -3.74611 | -51.12374 | 2026-09-18 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a974777-6539-30d2-893e-d3c56ca96e69 | -2.64093 | -54.69031 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 98b8cb15-69fb-36bb-9da5-661a0b6d0955 | -4.38165 | -55.03527 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ec87095-1471-3cb1-8bd1-8acbc7dcecb9 | -4.56597 | -54.9079 | 2026-09-18 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7b0df6b-c077-3efd-a100-b66bc4b6a44c | -2.82434 | -50.46905 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 0430c908-0340-33f4-8ae0-bf9a643c0af8 | -3.43991 | -58.20897 | 2026-09-18 04:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8dac2ba-9ebb-371d-943e-5a1be1033355 | -3.75724 | -51.1398 | 2026-09-18 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f3fd4203-42e6-3e84-bfcf-e27c97cddc56 | -3.3669 | -50.44209 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d23c2c8-e54a-3a57-8491-9fd7b81b9c64 | 2.09017 | -50.86744 | 2026-09-18 04:55:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4aee544-71b7-3710-b1f1-196f55440f3f | -3.47193 | -54.69739 | 2026-09-18 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b558aa51-3ba7-3f0a-8e67-b78c50f1a33b | -3.26709 | -54.27245 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b205b6ca-2f02-3cc9-909a-639e6bc2b9ee | -2.96476 | -50.33252 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 250a45c6-feb6-349c-a8af-155ed4c59943 | -1.70899 | -54.88891 | 2026-09-18 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b59e5ac-687c-379c-9423-2ff048ca2e45 | -2.16729 | -47.88302 | 2026-09-18 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd22c536-108b-35ac-a3a6-d687f7efcd0d | -2.70469 | -57.59768 | 2026-09-18 04:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34e9fe7b-2f3d-3e70-a48b-902a3c3b3048 | -2.36808 | -48.4278 | 2026-09-18 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a2a3108-5506-3925-9b68-5ea5373c72d2 | -4.55058 | -54.92952 | 2026-09-18 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4bbfd79b-edcf-3c22-9ad8-29307b729d05 | -6.29021 | -41.79691 | 2026-09-18 04:55:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 72206e52-ca3e-3f7f-a17c-fc0417ca3b09 | -3.35916 | -50.44795 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 424facf0-d558-3a70-acc9-1cc8f48dd3f3 | -2.29364 | -47.88239 | 2026-09-18 04:55:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e02ac5d3-47e3-3c98-892f-8f7bf91226a0 | -4.43142 | -55.51351 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0deb8b8-29cd-3705-a95f-aafff92cf593 | -3.4322 | -50.66825 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1103a516-12c1-3c60-8272-70c89905b906 | -4.37773 | -55.03471 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43a5a39d-abb3-34b4-a3ef-2dcf061ee667 | -2.29425 | -47.87859 | 2026-09-18 04:55:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81eaba62-a26d-3748-9880-2fe924acfabe | -4.51172 | -54.97291 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 923a082e-ac59-3772-8c09-71bfb6bd352f | -3.10457 | -48.69248 | 2026-09-18 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae4f4530-8592-345a-9bbb-feb64ca14cfa | -5.64048 | -44.80509 | 2026-09-18 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4425b799-eb65-3b0d-98b5-e38196256893 | -5.12132 | -37.71255 | 2026-09-18 04:55:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bb614068-19c3-3caa-89c1-918a4df3cedd | -4.48298 | -54.97798 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b00fa836-d36b-3944-bf79-4b2034083136 | -3.43771 | -58.19184 | 2026-09-18 04:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dad307ed-1d66-3812-9810-9064d2b23533 | -1.16066 | -47.63193 | 2026-09-18 04:55:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d5a890b-dbbd-3a17-beda-b445fec02949 | -5.19277 | -49.33031 | 2026-09-18 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89eae608-a084-3f8e-9f72-6dd9eb2f5ec4 | -3.49546 | -51.2524 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9053ef8-682f-3938-9203-9151e7fd6c07 | -2.70434 | -57.59908 | 2026-09-18 04:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d2d52e69-5835-357a-b0cb-d2df6a976f3b | -4.5578 | -42.94971 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0020d03-f2b4-305f-b5e0-497485630533 | 1.25932 | -50.76068 | 2026-09-18 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6295d7af-3919-3b02-9ab0-4e99d72bf4a4 | -6.29068 | -41.79353 | 2026-09-18 04:55:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1f9b475c-1a46-345d-8ef1-ada46145ceed | -4.16757 | -54.40766 | 2026-09-18 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a3be493-2d63-336e-9dea-288743c4209f | -2.89082 | -54.18522 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2d39b9a-84e7-3592-8911-8205cede885e | -2.96254 | -50.32509 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 713c61e5-9f01-3e51-b332-14f0a4c0f992 | -3.36748 | -50.45988 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc3db8bb-a0b1-3779-8a54-265c3f345697 | -4.51093 | -54.97768 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05f3340c-4634-3284-878a-580ba215a71a | -5.77481 | -47.28247 | 2026-09-18 04:55:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43c3f3da-80c0-3ead-85c2-2c6121a3c514 | -6.34482 | -43.37743 | 2026-09-18 04:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a92900d8-fd7f-3567-92ae-555ba0e2d235 | -2.81437 | -50.46748 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69edbbe9-e596-3008-b9b5-a23c2c8bfb60 | -3.03656 | -51.37144 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f8de44a5-b682-3c02-988b-2a45f4ef3359 | -3.01699 | -51.343 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd5340ed-dd04-3050-abe3-a9f350d4b7bc | -2.05753 | -52.17039 | 2026-09-18 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f2d555e-16cc-3211-b48d-0ed11ee32ea2 | -4.58696 | -42.95396 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3a4e409b-9e4c-3755-869c-168415102c98 | -4.53819 | -54.93248 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e562bdb-f4c5-335f-9d8c-671095683821 | -3.70634 | -54.181 | 2026-09-18 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3eab8b0-df1a-32d8-b8bd-63db6a59e7f2 | -2.82379 | -50.4725 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| e2b89551-cf29-38ae-8778-237014c26852 | -4.4936 | -55.49241 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4d0733d-77df-37c9-b60b-142524ae68a4 | 1.2726 | -50.86584 | 2026-09-18 04:55:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13f81f4a-7b54-3586-8db1-6beccca873db | -4.98217 | -37.39706 | 2026-09-18 04:55:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 11.5 |
| ea3c998a-0cc3-357f-9f39-a23c2e3c4653 | -2.97031 | -50.34046 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3942ba6c-0bd1-3255-b906-c9e5d853bdcc | -0.78186 | -47.54763 | 2026-09-18 04:55:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aeb9f644-5801-37e9-9e72-30ddab9063c4 | -5.75009 | -45.0891 | 2026-09-18 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d633f347-8e4c-3c3e-9eb4-99a50c8b93ee | -2.95198 | -50.30575 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f5cefb5-c229-39e3-839f-930821b6a921 | -3.43681 | -58.19727 | 2026-09-18 04:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e562f49-4a3e-397a-9d6b-146887542c0e | -3.26855 | -54.26326 | 2026-09-18 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1ab0191-cc48-304d-ac5b-8730fbe2da12 | -3.92219 | -55.75417 | 2026-09-18 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d4bbc5e6-631f-36fc-8788-5e548b23fdfc | -2.37906 | -48.22628 | 2026-09-18 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b767177-7b33-3792-b040-c82b59c9833f | -3.06577 | -49.52112 | 2026-09-18 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc9be7cd-17be-3398-b6aa-028f4424036d | -3.99484 | -48.395 | 2026-09-18 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fce6e2b5-f209-34c2-bd24-eda76035e541 | -2.89987 | -54.17729 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32eba222-6007-356a-b9b1-1be23b92d976 | -2.82133 | -51.34149 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86e0954e-5e6c-33c4-b5f1-a758357a7e52 | -2.56383 | -54.74366 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e266d196-3698-3e51-b143-9e1f91111fd5 | -5.33272 | -45.14697 | 2026-09-18 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3562a090-0c32-32a7-a7d1-4ea1dd043775 | -2.90744 | -54.17849 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 590b8c88-7576-3715-b6e7-7b8cf50cad3b | -2.49496 | -49.41376 | 2026-09-18 04:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37101c02-9c08-35e3-a2d8-004d2b20c35b | -5.25789 | -47.93329 | 2026-09-18 04:55:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 199566a9-cf1d-3d51-b97d-4968ed13eeda | -2.54605 | -48.15952 | 2026-09-18 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ff70d26-6322-3789-917a-95372be55bf4 | -3.38187 | -50.45506 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a36ecca5-8350-32bc-bca8-d0585cc1e0fa | -6.37873 | -42.79473 | 2026-09-18 04:55:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 098eaae7-cc89-3e6d-8399-b4f3ec537b76 | -3.04328 | -51.3725 | 2026-09-18 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b5f20d66-e4cd-326c-af80-5846912a50b6 | -2.82269 | -50.47942 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| e7738447-cb71-3bb2-ae21-2ed5f879fbec | -4.57157 | -42.95719 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c5d02248-c59d-3026-8d16-a419c346185a | -3.54415 | -53.99322 | 2026-09-18 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a452c207-f089-3ee7-8038-3603d6f8c5ab | -3.4727 | -54.69263 | 2026-09-18 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 420d6329-16ac-3145-a786-a43ce5e55b5d | -3.96811 | -56.12883 | 2026-09-18 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1233a606-b12e-35e9-8c5d-1404468e28f9 | -4.56445 | -54.91739 | 2026-09-18 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e46172b-5228-302e-9a32-8246aae4f8de | -3.1775 | -48.58419 | 2026-09-18 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17570fd6-a3eb-3700-bac5-788c70af57f8 | 2.09301 | -50.86325 | 2026-09-18 04:55:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50f31e29-00ab-3f24-b430-5eef6c9b8a0f | -2.73693 | -49.45878 | 2026-09-18 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1930914a-7760-3460-b8f8-f668d5c46af0 | -4.42907 | -55.52788 | 2026-09-18 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64fba78b-f55a-387e-8593-c654553f62c1 | -3.7069 | -54.17959 | 2026-09-18 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bd8a47c-bbc9-3286-b59c-1a52eecc3dcc | -4.40753 | -42.313 | 2026-09-18 04:55:00 | NPP-375D | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fd457575-3058-3d9e-a917-8a461b35a653 | -2.61024 | -54.75633 | 2026-09-18 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| ef382474-01c2-3b14-a09b-3c7334a4e2f8 | -2.05813 | -52.16661 | 2026-09-18 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 143d11c4-87ec-3243-890c-6449dfce1932 | -4.55542 | -42.96563 | 2026-09-18 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 179a95f8-1f3b-3b95-82d4-cdb16f92be5d | -1.21121 | -54.22392 | 2026-09-18 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25ac17d2-f20c-3050-844c-cdcf7de504e5 | -2.82712 | -50.47303 | 2026-09-18 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |


[Clique aqui para ver as próximas entradas](README55.md)
