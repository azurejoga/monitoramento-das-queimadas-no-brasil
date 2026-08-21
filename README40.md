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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd04412b-6ad6-3c67-9630-6bbd7669623f | -11.4863 | -45.09412 | 2026-08-21 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ece3f407-1c47-3516-ab48-434e9cadf506 | -6.00158 | -57.84081 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3cf0096b-15aa-3ec1-a187-1c033b754331 | -6.67127 | -52.8958 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dc66944-3c11-3155-9388-6a63e80d0cec | -8.62141 | -54.71906 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a5a4786-59c8-3b44-9598-c38d05027d8a | -8.09163 | -51.66191 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd3167ca-9109-38c4-9f3b-cffbebe209db | -6.76479 | -59.46533 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c404f25c-f934-3dab-b4d4-59af880569d3 | -6.86106 | -59.44325 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8903bf0-f6d0-3547-8a5b-fc1b9de2cf2b | -8.37634 | -62.69554 | 2026-08-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 36.3 |
| a4d0a949-5cb3-3460-878f-6a019cde2ca3 | -9.05201 | -57.07074 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c0a5bcb4-f4d0-3c17-aac5-441ea114127c | -6.12305 | -59.90757 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| df6adac6-f9f7-3483-9d57-d022ce8fde21 | -5.6039 | -44.00773 | 2026-08-21 04:46:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 8d2b7ca2-4ccb-38fd-bbf3-b97d19f997d3 | -6.01309 | -57.80017 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6347baf3-b04b-334a-810e-861db8f0f732 | -5.81237 | -55.72201 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf9d9223-b4dc-34b2-a598-4e28b1425074 | -9.11475 | -61.59919 | 2026-08-21 04:46:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90dbe50e-b358-38de-ae47-b1a7ed60d9a5 | -6.41894 | -54.93296 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a4b3391-5259-37f5-87ec-0457c08d2797 | -6.17249 | -55.44272 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 5fcc3a84-cf6f-3dcc-8edc-3693e5adbb54 | -7.00574 | -48.03647 | 2026-08-21 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c5dcead-6a8a-3c97-9033-32ddae098936 | -6.31578 | -55.91458 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04976602-3663-3b0e-8d50-cd455915e5a7 | -6.36029 | -58.33738 | 2026-08-21 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ee75cbb-de41-3864-b004-0f0d84f7285a | -8.54078 | -54.78265 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63be6e43-c525-3460-bcdf-796e8a4d75ec | -6.81344 | -58.99938 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d0d82f35-106a-3a53-9a56-d733008cc972 | -6.42091 | -52.76649 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0959d2ce-eac0-328c-afe0-73c3b9ca9cc2 | -8.10431 | -51.66746 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2c82836-b8ff-32aa-96f0-68fd6cc2240f | -6.43172 | -52.74211 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7db18f11-63ea-3b67-93ec-25a3111fc31e | -9.50994 | -51.68116 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4154e52-37cb-3708-a45d-775aef3d3b1d | -8.39354 | -62.70308 | 2026-08-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9ab5af4f-3705-3329-adcb-0db843bc98b8 | -8.54008 | -54.78686 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10837eec-6d69-3f18-8bf9-2402ad6433ab | -6.42387 | -52.72599 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97327fd5-665c-3dc0-b68c-78ae4041a0af | -7.46842 | -45.15997 | 2026-08-21 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b4a7c22-0840-3818-8579-25e194fd3148 | -9.40478 | -60.4249 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1ac3de63-2f0a-3154-adf4-74fdc1192dba | -9.22077 | -59.78263 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a0aacd2-1fbb-3f59-a61d-61f3a132be76 | -9.41147 | -60.43378 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd994776-cb45-30d5-8106-0b617dbfc586 | -6.34783 | -44.0823 | 2026-08-21 04:46:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3f69a99-fd59-3eda-81a8-792e6da33fc7 | -9.47566 | -51.64009 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91046700-99c3-3a38-8c78-a0b210b583c4 | -8.45717 | -51.56361 | 2026-08-21 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 379f5013-7ca1-3072-abed-6df750857637 | -6.58171 | -58.97245 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57cbaad3-96d4-3ea6-a728-e2f6e9621b1c | -6.66846 | -52.89159 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bbbbab9-1e5a-31a4-92e6-6622650408e5 | -8.07603 | -50.10735 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bf7620c-f54a-30a8-8a0f-821bd7914176 | -8.3892 | -62.69308 | 2026-08-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c7c1ef8-e8e2-3aa2-8c2a-e3edd786e7b9 | -10.76853 | -50.30719 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a1bb0006-3538-30f9-afb1-ae2a2b756400 | -4.01277 | -48.06112 | 2026-08-21 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a4133fa-85d4-30d1-ade9-1905f403ae98 | -6.12846 | -59.91272 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f606d07d-3289-333b-a313-50afedaf095a | -8.22239 | -55.02637 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 053972c5-60c6-39d0-a88b-b0e0041ed5fc | -6.88314 | -59.43394 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d95fb1a0-6449-3093-9b4b-cd32f40832fe | -9.41601 | -60.43772 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c9c5f424-5c2f-398e-aaf6-99148684fb96 | -6.70963 | -59.09097 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e44163cc-e7cd-3c29-b336-ad59077dddb3 | -6.00226 | -57.86434 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fdf43a6-bb2c-3828-a2db-00f201b6a663 | -6.09588 | -57.86952 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fb8f7ee-ec47-3ff0-9422-5c49f1ae289f | -6.43957 | -52.75829 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91a779ad-45d9-3ed3-8c45-4830f2a1c50b | -9.3883 | -60.55915 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddf463fd-e378-3f7c-8b23-263f076629af | -8.71458 | -49.61142 | 2026-08-21 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79618f81-a3f6-35e1-99a6-4f066697000c | -8.5854 | -54.78134 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a50df780-9310-3509-9cfc-cadf539ab2a6 | -6.01827 | -57.82457 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 604735d7-7194-31a3-92f6-e6f2d2aca5ec | -6.16783 | -55.44694 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| caf8a98a-cb5e-3b60-a6a0-a4ddd8322bb9 | -8.39521 | -62.6941 | 2026-08-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8eca9436-53b3-356f-8f92-4f11168c717b | -7.77849 | -46.03707 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ab828eb-900e-3c0b-9591-2971b08de18a | -9.9905 | -53.93925 | 2026-08-21 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0f0405f-128f-3343-848d-dba54b57d6c6 | -7.3651 | -45.81799 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 79ac9ed8-fce3-3abd-ae9d-6ab32e53bcb2 | -8.54136 | -55.31607 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 784f0177-2166-31be-a944-4ab13bd043b2 | -7.25406 | -49.90825 | 2026-08-21 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9526f447-6de9-3712-8ba0-94109f673794 | -7.72339 | -46.15775 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28902581-beb5-3787-b3cf-f0c5893b424d | -7.36003 | -55.52012 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca4f5073-6f26-3681-831b-e68d4898e897 | -10.63332 | -51.62671 | 2026-08-21 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 265f3189-9203-3049-a574-efbbe85b3e4b | -6.42884 | -52.76028 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7354a57f-9bc1-3d13-8b5c-b784c933660a | -10.51445 | -50.78301 | 2026-08-21 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c44c2337-e450-3f23-9ef6-9f92833ef159 | -9.21198 | -59.77537 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44d34f85-fc83-3738-a2d5-b265c778325e | -6.42195 | -54.93807 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d04e0166-b8f7-3f2f-b26e-ea2af5f27cf2 | -7.37398 | -45.81542 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 21881565-6ff9-3765-bba0-07b3fff38694 | -11.48716 | -45.11493 | 2026-08-21 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60266a3b-7297-35dc-9c29-bccf7bb87623 | -7.53725 | -55.57453 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ae35a2a-b2f4-391f-ae94-f25c0836f708 | -11.5525 | -46.93772 | 2026-08-21 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2cae62d2-dd3f-3554-97af-399a610c0f56 | -6.42896 | -56.18617 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9c006ab-208a-38f5-aaa8-d03914f3edad | -9.44547 | -51.63535 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb759be2-82e9-37ee-8a85-ab98fd69ff9e | -9.40239 | -60.426 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d57c89cf-7645-30e3-839e-41857dfb1d5e | -9.21311 | -60.77339 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8ac87cd-1af4-379a-887b-f65c9b53541a | -6.70049 | -58.93941 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 57e99e51-e7a8-30f7-aac7-d986ecd6b89f | -9.41657 | -60.43467 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9bae8502-c4e6-3b84-8868-bd1a44424d71 | -10.28659 | -48.22515 | 2026-08-21 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98b79920-a609-3958-81b1-428e62212d43 | -8.54418 | -55.30898 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bd8f2008-2d51-34ae-821f-901bd16930cf | -8.66755 | -54.58646 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77bacbfc-c6b2-3f13-a359-8224fdd8ab97 | -7.00833 | -59.54568 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1d2f66c-9d15-3f4d-94ae-188aa3e7d755 | -7.36149 | -45.81355 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 5451b3ba-2d73-3cfe-ba4e-c1ac903040b1 | -5.32602 | -50.94762 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a93afe3-d66f-3013-9fdf-944b8b000a66 | -9.80641 | -46.64952 | 2026-08-21 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcba490e-e316-3c6c-a7e3-b7bf4f838f67 | -8.54998 | -54.86138 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1c1c0abc-5484-3aa8-a047-2899bb2c4002 | -5.71537 | -46.18776 | 2026-08-21 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d785b2b5-b943-366e-8fa8-239bfb43b296 | -6.38097 | -54.95446 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a846fe6c-68d1-3d60-8ec4-b99854db9cd6 | -6.81743 | -59.3993 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 07ce8895-59e6-3ecb-8eb8-90994d7522b3 | -9.41595 | -60.40955 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 76089f4f-36fd-31e6-a8d2-9627dc40ba87 | -6.43619 | -52.75774 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77e3b4fb-11eb-37d6-b7e4-a21b1dad1657 | -6.43229 | -52.73849 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 459bf5e2-b0ed-38e0-b87d-d43d068d1a2f | -7.59641 | -60.9479 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8f1415f-a422-307c-a7b2-0870e47f0f71 | -6.64231 | -56.41261 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f1044ca-8b1b-3143-b2e1-11394b18ee2c | -5.94461 | -51.94823 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 054ce9ed-8976-3d22-8d8c-305336bbbe5f | -6.91432 | -59.34767 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca08ff18-d8ce-334b-a851-bb8e605886c0 | -6.94083 | -52.789 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22d5ed18-f462-3502-bd68-e874014ad69d | -10.90575 | -50.2786 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4b356c6-4ef8-327f-b491-2da6175088e5 | -8.61287 | -54.72624 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02f4d355-c1e9-351e-8ad1-f7868d40e174 | -6.16942 | -52.4895 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b90a5dd8-7624-3d19-bc16-dc412bb51791 | -8.58523 | -54.75986 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README41.md)
