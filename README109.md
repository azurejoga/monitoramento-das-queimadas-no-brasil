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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6851dd16-f05d-326b-b728-ca2057eecda8 | -17.30903 | -54.93386 | 2026-08-28 17:26:00 | NPP-375 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8e05e1b-ec87-331d-916f-83ccc2c6d7a5 | -9.51303 | -45.65308 | 2026-08-28 17:26:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b954e976-89ef-3808-9c7a-776c46abe0f8 | -11.8443 | -47.20967 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a5d0d6cd-f870-322e-91d7-9b62d591b5af | -13.39659 | -51.78753 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17ec3a02-861e-3a3a-bf76-5d03e7d5d43e | -11.24559 | -47.05972 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 475512d1-b197-3bbd-b1ed-4061274b73b3 | -11.14285 | -45.56507 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 25410384-baf4-36dc-9b35-8180e79c2ea9 | -14.42836 | -52.5926 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 80f8a882-eda0-3792-aa12-eac0c91a38b7 | -14.45344 | -53.38243 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 10666bb6-bd2f-398b-b1f3-2c08b826852d | -15.35875 | -52.82735 | 2026-08-28 17:26:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9e56ebcc-3834-3352-a32f-17cf04e07495 | -10.05977 | -48.6779 | 2026-08-28 17:26:00 | NPP-375 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4ade393e-ce4d-3ee2-940e-ed9f78c76268 | -14.58896 | -58.6479 | 2026-08-28 17:26:00 | NPP-375 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a374b704-2b3f-3685-81eb-69d6584b451b | -13.38115 | -50.22848 | 2026-08-28 17:26:00 | NPP-375 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8481709e-7a8b-394a-9670-05b26d4aab76 | -9.6934 | -46.57189 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| d3d258a3-2c83-3afc-ab52-bdf7afce2b49 | -10.32465 | -49.96396 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 99300598-45d5-396f-8639-78a2c3053352 | -14.41438 | -53.3972 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 58283f92-f900-3733-9584-08377fd29c02 | -10.84972 | -50.21766 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 3e181cb9-129c-3ed7-ba86-7fd93326b4fa | -14.3384 | -47.24702 | 2026-08-28 17:26:00 | NPP-375 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a968a67b-a084-33fc-81d0-93ef2838e4af | -14.11124 | -42.62728 | 2026-08-28 17:26:00 | NPP-375 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 8def8c1d-11f8-33c1-9d77-fa43c2058409 | -9.86037 | -43.61762 | 2026-08-28 17:26:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| daf2429c-248e-3ac8-a907-df8c03206559 | -14.65059 | -57.00101 | 2026-08-28 17:26:00 | NPP-375 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 1f505dd8-783d-3b36-bce3-f25c2cbdf4c2 | -12.39359 | -48.19966 | 2026-08-28 17:26:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c00215d2-90b8-3a13-abd0-f576b337279f | -11.23153 | -53.99368 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 662fb776-b42b-3231-83f5-708be4531ca7 | -10.99798 | -49.64492 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e232f5c7-92ab-38dc-a0e6-c405b9ff1dc9 | -11.83082 | -47.22168 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 89e49acf-e736-3348-9e7c-fb7709291159 | -11.82069 | -47.22346 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 77a9fac7-8662-3cfc-9cbf-60def4fa2555 | -9.68725 | -46.56879 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 5d1a2722-11e8-337c-98e1-f63052f6426c | -10.93202 | -46.62304 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 511a1d44-f110-3d28-9df9-ec1e3de8c26d | -14.88533 | -52.626 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 2bf0c62c-932a-384e-9ad0-e1d6cf4285a1 | -11.21654 | -45.0474 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 9518d209-0d54-3a8d-9f9e-e1d797b5126d | -11.22991 | -54.00553 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d14e6830-61ed-322f-aa66-24a823ff7166 | -11.34146 | -48.38141 | 2026-08-28 17:26:00 | NPP-375 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e1e74adc-57c3-3daf-904c-f6487cc3eec7 | -11.0191 | -49.66316 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1ddf8c7f-fa71-3b70-a9fc-78e6a7160a22 | -16.57512 | -49.78754 | 2026-08-28 17:26:00 | NPP-375 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 616db8fb-fcaa-383a-a3e6-99a40f997927 | -11.69772 | -47.61508 | 2026-08-28 17:26:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8dd9e248-40f4-3fcc-9246-e30361bcb984 | -11.84485 | -47.21264 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ee29aba9-f280-3c58-a762-bac92880cdf2 | -14.03492 | -47.80012 | 2026-08-28 17:26:00 | NPP-375 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d62c995c-5cdf-3d12-b879-c1ee792fe983 | -11.48668 | -46.93811 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d4e150b2-6db1-3f4f-b592-0da7cde47826 | -11.25013 | -45.06389 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1203989b-3aa0-378d-a059-a566ff4a74ac | -11.65637 | -55.68925 | 2026-08-28 17:26:00 | NPP-375 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| c0c65121-9c3f-3837-82c0-d13fe7f9a716 | -9.87038 | -45.87207 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cab559cc-4621-3d78-be4b-788c8920b0a6 | -11.27064 | -54.01816 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0e515d48-e005-3246-b98e-ca29dcf096f7 | -9.86342 | -46.33405 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76efd25c-7501-3bd8-88d4-87d926349c98 | -14.56811 | -53.20322 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| dac3e31f-d97a-3e1d-8391-38ace6d6f0fc | -11.00962 | -49.63409 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 35c21665-8bf4-3221-a288-bb75bc3a413b | -11.2384 | -53.99254 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 479a24c8-7432-31e2-83d9-ba17c0467dfd | -13.75236 | -43.5056 | 2026-08-28 17:26:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1b10cd1-5cdf-343e-a238-4650198cb359 | -12.91215 | -59.89759 | 2026-08-28 17:26:00 | NPP-375 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 61ea4bce-9d6c-3e56-a903-fab7536b4ac3 | -10.3419 | -50.38197 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 58d700b5-1ef6-3fb4-8868-4523680e33f6 | -14.58643 | -58.64486 | 2026-08-28 17:26:00 | NPP-375 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ff51f8c9-3be9-3137-b577-f269d75bd875 | -15.45795 | -53.85966 | 2026-08-28 17:26:00 | NPP-375 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8b28cf9-79ec-32a6-b83f-88f8ea950b60 | -10.18021 | -46.8549 | 2026-08-28 17:26:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0d9b467-b3b8-3eee-a127-e824900850d4 | -9.8398 | -45.87078 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 6d2d0536-1e33-3e51-8aff-abc85a699844 | -11.34894 | -48.39561 | 2026-08-28 17:26:00 | NPP-375 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bce915d9-b505-3d39-9954-61e14d41c175 | -11.2172 | -53.99216 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| efb382fb-571b-38ba-8ad8-726ac151dcef | -15.46627 | -53.97816 | 2026-08-28 17:26:00 | NPP-375 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 66842a0b-140f-354d-a210-47b05d92318b | -10.02655 | -45.81656 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ea3eb4df-54e0-3bf8-bf98-ac3085b395c3 | -12.05633 | -47.18924 | 2026-08-28 17:26:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b34054ab-95a5-3d24-bb7e-565bb5faf590 | -14.92389 | -41.26101 | 2026-08-28 17:26:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 45.8 |
| 45a0559f-7622-3bc7-8a51-cc9e63d46c6a | -13.65143 | -49.0094 | 2026-08-28 17:26:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2388dcad-1686-348c-b265-500b5c1a9079 | -11.22346 | -53.98727 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 30fcb3f1-aaed-363c-ad3c-9ca5ccae1e35 | -11.20355 | -55.09939 | 2026-08-28 17:26:00 | NPP-375 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2c5cd86d-3734-3ea5-91d0-4f67e88b4929 | -13.5945 | -45.77777 | 2026-08-28 17:26:00 | NPP-375 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1dca4a45-23dc-3871-9491-1d557f082601 | -11.26547 | -50.70127 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3f4e856e-3cf8-3bff-a0b4-d7d7cfa09447 | -9.50723 | -45.65434 | 2026-08-28 17:26:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a209cc03-0ef2-3c7c-9f01-cdb28cca7758 | -14.91273 | -56.31783 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 4188017c-a032-37e8-bf06-6b3b4f239a3a | -11.96817 | -45.50214 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a1d0f7d4-b72e-353d-b8f5-b80e1805c749 | -10.55036 | -50.41378 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| df24a62a-75ae-3b40-9e7e-d4680377ad6d | -13.42459 | -51.77319 | 2026-08-28 17:26:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3f57d526-6812-3a10-95c8-7fa6324b56ae | -10.17907 | -46.86229 | 2026-08-28 17:26:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7ddf6e5c-2e42-3650-abe5-d1e6600cba36 | -14.87639 | -52.61539 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| df9749c9-38f7-3ce3-be35-6ff753702c7e | -11.24425 | -45.06499 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| eb37db2d-b7a0-369d-80f3-b90781aa9aa0 | -13.40098 | -51.76833 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| d2c6d629-ea70-37d1-845e-5bf499a49b16 | -9.86471 | -46.33472 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 29abc790-34b3-3633-94cc-e523162f55c6 | -11.83984 | -47.21384 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9e881f70-f90e-3f61-abd9-d852139ce07f | -15.46131 | -53.85911 | 2026-08-28 17:26:00 | NPP-375 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 65279698-d265-3e8f-a9d3-2d25a6d17ff0 | -14.60072 | -53.14289 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 4c62b2e8-ed37-3c70-b1f0-5767704dc3da | -11.83928 | -47.21084 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9a75cdc9-3937-3404-81c0-a4f28c1fc3ca | -14.17531 | -52.83229 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 6a060c6d-86ac-3844-8af1-a08deabe21a0 | -14.45075 | -53.38329 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bcd34bd4-1886-377d-af12-a75793042738 | -10.89036 | -50.50322 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 8a273621-ea71-3c3a-80a3-1eef81074f53 | -11.19031 | -46.24986 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c8361930-bcc8-3a3c-94fc-510fa94c9ae3 | -13.64718 | -47.75377 | 2026-08-28 17:26:00 | NPP-375 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4cf0bdef-3aae-3e30-8f7b-08bda70755b3 | -16.2999 | -56.598 | 2026-08-28 17:26:00 | NPP-375 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1ce2b5aa-bdc7-3a73-9aa5-6e819a51c545 | -11.20579 | -55.09172 | 2026-08-28 17:26:00 | NPP-375 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 742d2c38-bf95-324a-93ed-d7feaf9dc3ec | -15.73478 | -51.17587 | 2026-08-28 17:26:00 | NPP-375 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8ca85c82-d25d-349e-8642-a6bd8484a1f4 | -17.58957 | -51.64476 | 2026-08-28 17:26:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 72a760f2-bf06-3637-8922-b5e7e9bca30b | -11.23051 | -54.00928 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 25edd161-4b4a-3203-9bb6-1852583c2622 | -11.27014 | -50.70417 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5cfcc41d-b79b-3913-a509-8b2e37a4a6e7 | -14.91951 | -56.31678 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 1f793eaf-e8fe-312e-9f89-ed68242cbcb6 | -10.99785 | -49.64509 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0c4b3e90-abb4-38fc-9286-f31c1e073d8d | -15.64131 | -45.91352 | 2026-08-28 17:26:00 | NPP-375 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2767876b-4324-39e8-afcb-1a0fc7c1217f | -11.225 | -45.04112 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3095e40a-f341-3e07-8167-d86bd4400797 | -12.21619 | -50.54337 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cf30a909-6a7f-3499-aff2-eea9752b54d8 | -13.42914 | -51.76521 | 2026-08-28 17:26:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1828e996-e92a-3b83-8dc4-2a412b0ea8da | -14.88882 | -52.62541 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 253.5 |
| f65c1aa6-b9a4-3be0-89c2-d39d1af452f1 | -10.0769 | -48.66418 | 2026-08-28 17:26:00 | NPP-375 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 6b39b451-ca39-32c9-97bc-5c377084f295 | -10.54684 | -50.41836 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 398813c5-90d4-3853-8eb1-85d3f2f47224 | -12.19228 | -50.57339 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 25b742d8-b858-3717-9211-86d80503db44 | -14.90651 | -56.32259 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dddfbe5f-6c6b-3ef3-90e2-5f5aafb4489a | -12.69546 | -48.43188 | 2026-08-28 17:26:00 | NPP-375 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README110.md)
