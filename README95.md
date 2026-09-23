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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e02d376-5855-37c9-98b1-707b2f36fcf7 | -9.54885 | -45.77021 | 2026-09-23 05:04:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8313c105-1ee9-350a-98a6-20615696b241 | -6.71191 | -59.45911 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7e64f76-09c3-35e3-92fb-604c7cb16cc0 | -5.95918 | -51.94283 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e54e1a71-74cd-310b-b08c-84e9e99a8543 | -11.4059 | -44.05051 | 2026-09-23 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ede8692-d28c-3e9a-840c-1a0a39c468df | -6.61709 | -59.96396 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0b5a344-dadd-3553-ab05-8f224b11e418 | -6.89513 | -55.33276 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86675b2d-dbf3-3322-9c78-d3781851c29b | -5.98221 | -57.77927 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33d1fcb4-f372-3bb0-954b-3d93b3545115 | -4.5426 | -54.93779 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ef23492-2cbe-3c82-b883-9675da81df70 | -11.47239 | -47.35834 | 2026-09-23 05:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bdec94fa-a67b-3623-b042-41c8e1003980 | -11.66627 | -43.48367 | 2026-09-23 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9d6a7cd-df27-3c74-aaae-d2ae4d11109a | -4.0941 | -62.09425 | 2026-09-23 05:04:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b8b0f6e7-8c0a-3f6c-a75b-0766a39ff2a9 | -6.35618 | -58.28071 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 920cdd53-a2e2-3f53-84e3-b998d34a25e9 | -6.88098 | -59.85929 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eaa6f237-d0b6-3c82-b93a-35df0856a14f | -11.11316 | -48.31321 | 2026-09-23 05:04:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d03a1320-f0df-3525-adc8-ce616348f7ee | -4.00395 | -52.09339 | 2026-09-23 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbd58716-0591-34ba-bad1-26dca70ceef8 | -8.08299 | -44.34882 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e91707f7-a8b9-3467-b759-8ded761007bc | -3.18261 | -61.1032 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3526320-37e7-3a9f-8fc4-7de08d3904bc | -6.31202 | -59.94776 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e2260a6-0b4a-3ba2-b545-1496bbddfbce | -5.22078 | -60.05376 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| caac77f2-5c1c-3949-8f36-3e1264412785 | -6.46586 | -59.96168 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1300c18-e58e-37d4-9618-6ed3512abe4a | -6.68752 | -55.05505 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 99eb655e-66e3-3704-a118-db0f1c8af48f | -3.72096 | -60.57727 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02c0ace5-300c-3b5f-9321-1c549da82664 | -6.5422 | -55.47871 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f12a18f-c889-3ece-b11b-75cf97707098 | -8.9199 | -61.49527 | 2026-09-23 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6ac6bf2c-0080-3568-8d31-76ba825aa190 | -8.89692 | -45.9507 | 2026-09-23 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de905e0f-51d2-3230-9a28-cf985c58a750 | -7.42921 | -49.85081 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07760727-61ec-39ff-871f-1c2de9e4fdb9 | -8.59592 | -54.61212 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bdabe847-9a42-3f7f-8d25-d7a08d08bc69 | -9.16938 | -51.47345 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48a8c339-681c-3f47-86d8-f947001dd8b0 | -10.7509 | -54.08145 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9f95d31-1806-3723-8ccc-7ec2ac804d8d | -10.89854 | -54.06913 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8fd01ad-93d9-3283-a3d3-4374f9d447cb | -8.12525 | -44.43589 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1ad13c6-f025-303f-8d8c-641235791378 | -10.70537 | -48.70887 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f8f5691-2907-32a5-8fc8-cbb4f5293294 | -9.05208 | -65.42247 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7bacf133-128d-3308-b65b-b20a862cc3b9 | -8.30778 | -54.77326 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6998b46e-d89c-393f-8ed2-2d571612cb2a | -8.9181 | -61.49682 | 2026-09-23 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e813f41f-b9ae-32f8-bd00-f1abdc5bc8fa | -9.84251 | -46.38353 | 2026-09-23 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa23d096-69c9-3458-9477-da17f5d7aa17 | -5.92222 | -52.11205 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af3052e8-d3fc-3210-ab86-bf2c873ad075 | -3.08289 | -61.16703 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 814ec013-f952-35a8-883d-ed94c9c99350 | -6.59399 | -51.32426 | 2026-09-23 05:04:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bad110f-cd4d-3ff1-9490-be5fb5c923cc | -6.67172 | -50.93779 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 509f6ebe-0d38-3ae1-8067-485d1955e36a | -6.07391 | -57.80233 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5258f47-7b79-398c-910e-61559cc6c1c9 | -10.04555 | -50.21656 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d17acbe-51fe-3d26-82a3-a8fb103907d3 | -6.61903 | -59.92989 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 93f1b6c5-081a-3f3c-ae2a-f2e1d83c9cc6 | -5.16247 | -60.30104 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 22ddd556-7c25-3fb1-a75d-3e55059e1eb9 | -8.45722 | -48.70394 | 2026-09-23 05:04:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d05ea2f2-cfe1-3798-8214-96b351f534fb | -5.74514 | -51.92676 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52239cbd-47ab-3e7a-b5cf-8043cdfec6ac | -6.62215 | -43.73935 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dffb2700-17eb-32d1-bc1b-49ec524892fb | -6.72875 | -59.44313 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d3e47337-30aa-3b06-b0d1-a88772204d0a | -7.13745 | -48.43026 | 2026-09-23 05:04:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c79e685-764e-3a5f-a38f-e4227b9abdb4 | -6.74394 | -55.30989 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8197bee-4226-3752-8c65-049ba16b9a8f | -8.92199 | -61.48359 | 2026-09-23 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2f5d36d-2ef8-3136-8405-a3e5f00f8412 | -5.82787 | -52.04377 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5bddf71-b0af-37ce-b31f-9cc9b9c0c2f4 | -8.35993 | -45.61937 | 2026-09-23 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb5c3e17-1d2c-3aa3-8d84-80f7e53806a1 | -9.86654 | -48.39245 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60de98e6-1fe6-3afa-a754-52b75c327486 | -9.25588 | -65.44006 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eced9414-64e8-3912-8ca0-51fe54dc1cd6 | -8.91168 | -45.94796 | 2026-09-23 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79ebdf24-5fa1-38de-a73e-de7895f3b29a | -5.80743 | -57.73478 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64f1d0fb-9d45-3f5b-9f28-b4f69a781b35 | -6.62754 | -59.93656 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a67aa978-8428-3635-b824-23e1d1e52284 | -3.6845 | -60.56778 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bbe4ae1a-9f60-3b7c-9d64-f38e4b465dc9 | -6.6081 | -59.96402 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a5140068-5c95-3388-925c-15c0e95e4e09 | -9.7139 | -48.33504 | 2026-09-23 05:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2e33d7c-1fe4-3130-b128-8527b7e20d2f | -7.15079 | -48.44707 | 2026-09-23 05:04:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6af74973-e578-3640-b36a-973895d0ab3f | -5.85271 | -53.53092 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a0553d6-5b42-3a7f-8d8c-1e1851e69217 | -5.29147 | -49.26949 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c120abf5-19b9-372f-8a78-8e43a3db4a7a | -6.12694 | -57.76249 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| db843e2d-4d04-3f3d-ad61-2a7d17c95be0 | -11.63699 | -50.94251 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a2e56c53-3b74-3d03-9b28-b4be04a2e7ff | -6.67676 | -55.07721 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf226ecb-86e7-3d10-b013-97cc192b0255 | -6.66463 | -55.06331 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| efdaf7d8-7ec3-3c75-8915-7476207298c0 | -6.74914 | -50.6827 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50ad6ec0-e31e-3299-9a13-525d47239d6a | -4.05145 | -56.31101 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 78774184-353f-3f89-9e26-555a96f94af9 | -7.61681 | -50.41926 | 2026-09-23 05:04:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d058b945-e47f-397e-bb45-720636d1285b | -6.51513 | -55.36413 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1ec0108-12fd-3943-9d55-392f91fdef50 | -6.42194 | -59.99004 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2df6d17-2d92-3516-90ec-1b8330fb1ec8 | -6.10219 | -57.68392 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f978a19-4007-3c11-8ef4-f27e49cb21ce | -7.31727 | -55.22528 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d34d62d-53ea-3989-bc81-e5135984589d | -8.92028 | -61.48519 | 2026-09-23 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 430b0063-0f53-3e93-a091-0c380d7e021f | -3.68556 | -60.59319 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3676c91e-09d4-3c01-9312-03238ea286cf | -8.83361 | -50.48809 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a34beb9-d4fe-39c2-b8f7-0474166c82f2 | -12.0926 | -47.48935 | 2026-09-23 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a73fcea0-948d-3bfc-8d87-ac3526a7abfb | -6.8973 | -42.92134 | 2026-09-23 05:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fc932221-8f01-32cf-bf3c-9d08d9e7fb0f | -11.65673 | -43.46593 | 2026-09-23 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd15d9e6-5621-3606-b315-61edc5b9957c | -6.62261 | -43.73608 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69dd696f-8261-3036-a73a-320f40b4289a | -6.61532 | -59.91739 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 17f92a59-a70b-3b96-a9e6-bff3a5f407df | -5.34871 | -45.16519 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| da8725ba-69fb-373a-8072-5030e20ccc0a | -6.6164 | -43.74191 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 20b9f7b9-3229-36de-9b29-ae45393244fd | -5.8716 | -51.93992 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff6a572f-79d3-3c7f-bfed-1447d3be15b5 | -11.3522 | -44.20876 | 2026-09-23 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c2d9a134-c1e4-3ec7-b251-0ac64e4e5916 | -8.20464 | -54.71886 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 441681d9-8e09-322e-b9d9-e1814a5af499 | -8.94895 | -50.9151 | 2026-09-23 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b948f87-6bb0-32e9-8c37-499a0976a651 | -10.26456 | -50.24447 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21ed394b-393f-3a0e-9107-0a49f261bdd2 | -7.32918 | -55.5929 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4574e7d7-445a-3724-89b8-c715ea80b9d1 | -6.62283 | -59.93576 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| db7991ff-a8a2-3550-beae-229e6f3ee1ad | -5.99636 | -45.23279 | 2026-09-23 05:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b08f45a-6b61-3291-854f-3fd5bcc728dc | -5.14507 | -60.30786 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39d57bec-299a-36e9-854d-d59438623281 | -7.98129 | -47.46573 | 2026-09-23 05:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2989df2e-2e08-3bcc-8e2d-60566d9012a6 | -7.13851 | -42.06533 | 2026-09-23 05:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fe43fb95-cf66-3795-8282-ee5ef8107773 | -5.82626 | -52.07555 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4578a2c-25e2-38c2-8bee-fe1907cbfa10 | -6.88756 | -43.63821 | 2026-09-23 05:04:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 58277502-cd69-3000-bbe1-ecb7a7c8a035 | -6.11258 | -59.88309 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 685ac5ff-3081-3da8-b632-977af6eb8e40 | -6.62301 | -59.9291 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |


[Clique aqui para ver as próximas entradas](README96.md)
