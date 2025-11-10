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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 711e6e26-4781-32fc-ad46-f907e9f12f4b | -3.1023 | -50.32103 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8594466-1778-30a1-828a-ea7ba99ba14b | -2.63796 | -49.21938 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed12bf9a-07c2-3b49-baa9-a4f74c98d9cf | -3.10849 | -50.19897 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cee2a49f-7bb4-3c2a-bc13-e5c24c0c054d | -3.19717 | -46.58928 | 2025-11-10 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99015249-725f-36e7-a3df-55c352463b5b | -2.97155 | -47.90012 | 2025-11-10 04:18:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41845801-533d-310d-9cc1-11e5b708fee9 | -3.07733 | -49.37987 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1f3c78dc-91db-3a21-b5ab-c8bf3989f034 | -2.9697 | -49.82735 | 2025-11-10 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7cde014-980c-37a7-b969-637b662de875 | -3.33448 | -43.53708 | 2025-11-10 04:18:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6c6c000-72bc-3448-ac69-d702565a72ce | -2.84822 | -48.64698 | 2025-11-10 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3990f36a-4b04-32ea-8c9c-0f27ad9beff0 | -3.09277 | -50.32385 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4489e9c-c116-3602-ae11-c7e8d2023a04 | -2.48011 | -48.36818 | 2025-11-10 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 674394c6-b1f7-325c-b629-719b0db16eaa | -3.89557 | -43.44777 | 2025-11-10 04:18:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21ee59df-d15e-3c7f-8b1d-ac199f16f6fd | 0.9768 | -50.06764 | 2025-11-10 04:18:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd08bcdd-e9dc-322a-a07e-683e821a092c | -3.06751 | -50.28426 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b281b41-8b24-3a0c-81a6-92599a9c09e0 | -3.41685 | -42.68798 | 2025-11-10 04:18:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 293181fc-9ca4-3821-8f2f-a37a51126ff6 | -2.97815 | -44.5882 | 2025-11-10 04:18:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03d38927-9920-3661-9108-cb0926d3fc07 | -3.75154 | -40.76911 | 2025-11-10 04:18:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f50467ad-c837-39fe-a9a1-ad733e006888 | -2.96323 | -44.59651 | 2025-11-10 04:18:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86004601-0a2b-380a-989a-e9d317d6ea4d | -3.18594 | -49.48286 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f89741f-89ae-3b8c-a515-1c5ba136bc86 | -2.24629 | -48.37199 | 2025-11-10 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36a10ccb-f356-3553-b3f2-3d8b06ff9342 | -2.44617 | -49.33998 | 2025-11-10 04:18:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ea113c8-ebcb-35d0-b498-8e8dbbc46229 | -3.09904 | -50.20175 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8381063f-c854-392c-8a23-be3f21a44137 | -1.79334 | -48.06609 | 2025-11-10 04:18:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34a97a5a-4b7d-3f32-a356-329e06c9be99 | -2.41924 | -49.34734 | 2025-11-10 04:18:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b134d4f-1342-3524-838c-12aaff4577cb | -2.96378 | -44.59304 | 2025-11-10 04:18:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 120476f5-a1b1-3817-93e0-51c693d9711d | -4.02323 | -41.62837 | 2025-11-10 04:18:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 59e3e69c-7713-38b6-bf91-d83129aa1acc | -2.9939 | -49.5954 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 80ba9acd-fee4-34f8-adc2-370833d208ce | -0.95289 | -46.81503 | 2025-11-10 04:18:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 693c70b5-0bf5-3ba6-b7d7-87833e524f2c | -3.09207 | -50.32822 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b9d2bf9-52a3-36e1-92cb-329de40cd1bb | -2.96777 | -47.89951 | 2025-11-10 04:18:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71c3bf11-b2b0-344f-9d89-7526f865585f | -3.18658 | -49.47899 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12a0132f-00c6-3147-85cc-946793529111 | -2.53992 | -49.45636 | 2025-11-10 04:18:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bbb0055-57b5-3ce7-9e20-eb6bc15c3d1f | -2.60607 | -49.23323 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e6d4e78-f72d-3543-b11e-0369e3eab3a7 | -0.81211 | -47.1534 | 2025-11-10 04:18:00 | NOAA-20 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f8f8b5a-f739-3575-bbb1-6007971247d9 | -2.79853 | -48.94266 | 2025-11-10 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f44e1d58-4684-3b37-b828-45503f312f9e | -2.87779 | -44.36301 | 2025-11-10 04:18:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71c1c6f9-070e-3c59-97fb-43e3f22b8478 | -2.64269 | -49.21629 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d970475-2b34-3b98-9b88-fe711c3de480 | -3.75517 | -40.76966 | 2025-11-10 04:18:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9a589ee1-043a-33be-9075-0610f2ecbd40 | -4.14847 | -38.48099 | 2025-11-10 04:18:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 809e6727-c139-30d3-a669-d487ce32720f | -2.4061 | -44.78765 | 2025-11-10 04:18:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ed83ebd-8fc5-3261-94d2-188322897c52 | -2.92073 | -40.0066 | 2025-11-10 04:18:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 85769b41-de18-3027-a04c-8c3b900e49ea | -3.07902 | -49.47327 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9902838-8af9-3eb4-924f-13e67111cc11 | -3.09789 | -50.32024 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abe52f17-bbd3-38eb-8ca6-f2af7f89251e | -2.93559 | -51.05747 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd757bb5-4fd2-33b7-8d24-778f763f5dfb | -3.76449 | -43.97826 | 2025-11-10 04:18:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bcf81af3-6d24-30bd-8bd4-0c507769aa63 | -2.42226 | -48.59693 | 2025-11-10 04:18:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e99dba9-9583-3041-97fd-b74d8bf02fc0 | -2.96817 | -47.8977 | 2025-11-10 04:18:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2e2305f-532b-3e29-810b-c70af49df3b7 | -2.91698 | -40.00602 | 2025-11-10 04:18:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 02295b55-ee3d-3ec9-9a79-37e7fe3dfec4 | -2.9776 | -44.59166 | 2025-11-10 04:18:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 089a50a6-0605-3082-aa21-5608f62a6b72 | -2.34472 | -47.03383 | 2025-11-10 04:18:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 749c98ec-20da-34e8-b40f-ecb427ced0d7 | -4.26863 | -40.86042 | 2025-11-10 04:18:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c0c2f51a-4faf-3209-bca6-4b303a5bd90b | -3.1016 | -50.32535 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1865800b-7605-3a0a-9d5a-c9888f2dd4d7 | -2.54265 | -49.41336 | 2025-11-10 04:18:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39e65931-612c-34bf-af75-33c3b1fede06 | -2.82755 | -48.657 | 2025-11-10 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0346998-4be4-3a9c-9f62-80cc802061bb | -4.1479 | -38.48484 | 2025-11-10 04:18:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 505b6fe4-14fe-345a-919f-2201bd29d510 | -2.63915 | -49.21193 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adf93a62-ea75-3917-b0e9-183ab1b0f443 | -4.02263 | -41.63225 | 2025-11-10 04:18:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6e8a4abc-97ed-3c64-a650-226038341ba5 | -2.41808 | -49.348 | 2025-11-10 04:18:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7c53830-d9a4-3b7c-b968-2e7503f6c173 | -2.60667 | -49.22949 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4744577e-8006-36c9-8ac3-1d54b61d671c | -3.09974 | -50.19745 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c0d5594-9b0f-3b3a-8c22-2a951f28d7f1 | -3.03157 | -49.49472 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 12bb2119-5058-3c48-9b73-a5b4f698639f | -2.46738 | -48.79921 | 2025-11-10 04:18:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3df3a5d-34b6-32ed-8368-23cd07b8e7ca | -4.01975 | -40.89886 | 2025-11-10 04:18:00 | NOAA-20 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ec5953c2-34fd-362e-8703-e8e6c8891ee2 | -3.34081 | -39.99689 | 2025-11-10 04:18:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d25b8380-dacb-376d-b8a6-23fdd73e6db4 | -2.84505 | -48.64935 | 2025-11-10 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 69ed9c1b-3c8a-3575-9f66-477fea15eba1 | -2.53929 | -49.46021 | 2025-11-10 04:18:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f6b3ab2-8742-3913-a268-0c19d385d2b3 | 0.98143 | -50.06689 | 2025-11-10 04:18:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8368a53d-2e6c-3721-bb91-6f501b07de6b | -2.442 | -49.3393 | 2025-11-10 04:18:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8465988d-d14e-3a00-8c88-254865592c68 | -1.44624 | -49.08768 | 2025-11-10 04:18:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e044bb40-9ccb-3381-9b82-4c8871172987 | -2.84426 | -48.64636 | 2025-11-10 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 60c1c281-530f-32fd-826d-0dfbcbb67baa | -2.19856 | -48.2448 | 2025-11-10 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94d554dd-7d1a-3a9f-9c9b-a9be0ee546a3 | -2.60193 | -49.23257 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| bac2ee67-4a21-33b8-a912-a8c93aa93bec | -2.96206 | -45.07668 | 2025-11-10 04:18:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 223be252-5e38-3489-a652-274f5f1015b0 | -4.1469 | -39.53905 | 2025-11-10 04:18:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| eb726f18-32c7-3ef1-b9a8-1362889268fe | -2.19777 | -48.24972 | 2025-11-10 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b12fa772-1216-3a6b-924e-ffc399ceeedd | -2.34109 | -47.03327 | 2025-11-10 04:18:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 52881dbb-0f6e-3a69-b2d2-ee655e56f761 | -3.03575 | -49.49541 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 021e9839-127e-3612-858b-e257d815da07 | -3.09247 | -49.6822 | 2025-11-10 04:18:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb832d02-16dd-32a7-a1aa-3a7114034a3e | -3.10482 | -50.1939 | 2025-11-10 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10f984c6-e5f3-38f6-8f05-2dfd28eeaed2 | -2.62616 | -49.21368 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2473acc2-0b25-3212-b0a5-c7b959201803 | -2.79314 | -49.65563 | 2025-11-10 04:18:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15de4bdd-aeea-33a1-baff-7be787797d5a | -3.09165 | -49.26765 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a95de4f6-f3cc-38f9-985d-08a7b7b96ce0 | -1.55698 | -46.06236 | 2025-11-10 04:18:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a257fc8-57b4-3d4f-b481-0766416a2c1d | -2.99328 | -49.59929 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 07b5ff04-293a-322a-ba0d-d349c6f9e3b6 | -2.97483 | -44.58768 | 2025-11-10 04:18:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63dc9661-d1da-3c2d-b827-9680632737b7 | -2.62323 | -49.20556 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01ec0e94-4fff-38c0-a016-19a2fd818e90 | -3.12935 | -49.24355 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa4d1c30-4abb-32ac-8580-4c34b268a3a1 | -2.79064 | -45.80472 | 2025-11-10 04:18:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3030618c-25e5-3b26-95ab-1129ea5223ef | -2.84238 | -49.51546 | 2025-11-10 04:18:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6aacbb21-dff3-3cea-9314-30991f89f11a | -2.83152 | -48.65764 | 2025-11-10 04:18:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 665570c7-c738-3cd8-b144-8c202ef626c2 | 0.66061 | -51.54423 | 2025-11-10 04:18:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae7d2c98-93c6-3389-b471-34168997c8bd | -2.5193 | -49.09858 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 179d22b3-f7f9-300d-b818-03bcef7d25a2 | -2.63855 | -49.21565 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91c352bf-6c0a-39f2-a9ae-918b7ee681e3 | -2.44137 | -49.34311 | 2025-11-10 04:18:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d179c1d4-9508-3ca9-928e-bc02b059968b | -2.60787 | -49.22205 | 2025-11-10 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee591fc0-80e0-3bbb-9567-8261ad0f7cb9 | -2.18607 | -48.24779 | 2025-11-10 04:18:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3452fb6-a7f2-3115-86f7-b6a1a4f07c9e | -2.97195 | -47.89831 | 2025-11-10 04:18:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8300b11d-3fbf-3d72-9937-e36b4a745240 | -2.64325 | -45.23766 | 2025-11-10 04:18:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3caf5767-64a4-3957-bfcb-a92f1150f2ec | -2.24694 | -48.36969 | 2025-11-10 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c54c27f1-b2c8-3f45-a6cf-a26ae1ca4290 | -4.1943 | -50.6281 | 2025-11-10 04:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |


[Clique aqui para ver as próximas entradas](README10.md)
