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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41e8d031-7f17-31be-bb60-75e1788d7733 | -12.49222 | -57.74764 | 2026-05-17 05:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3613fc30-8536-3be7-bd5d-eeae6ad6bdd8 | -12.49459 | -57.20731 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f336cd17-d2c4-3dfc-9bab-22c5682dfbde | -12.52426 | -57.2197 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8dc0b6ab-16de-3e24-8688-ba6eaaefba45 | -14.34246 | -56.84813 | 2026-05-17 05:23:00 | NPP-375D | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| deffc551-7f72-32bb-a15e-876fabb33ef4 | -12.50486 | -57.20893 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74f3e706-9c32-3d7e-a5dc-bf4d67b493b6 | -12.50257 | -57.2009 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f645cf2-ed9b-3be1-ab07-7d306ea55f38 | -12.50828 | -57.20947 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6df53035-d1b2-33da-80de-ada36c734fdf | -12.50712 | -57.19391 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c11760f-fbdd-3dc5-b256-efe5fcae0c5b | -12.72821 | -54.19323 | 2026-05-17 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6babd74-56e4-3782-bb57-6dd8b7543ad3 | -16.04656 | -47.23121 | 2026-05-17 05:23:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96554596-77fa-39be-b33b-bdc865ad7abb | -12.98882 | -54.68272 | 2026-05-17 05:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa6799eb-3995-3d8a-809c-7b360d8bab71 | -12.50772 | -57.21322 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e44c60fa-f935-372b-b5ef-da4dee7df04b | -12.52539 | -57.21217 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06a93d0c-2936-3210-b0e0-e3b641b74886 | -12.52483 | -57.21593 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 197a6164-fbbd-3309-a714-a24729d7b264 | -12.49802 | -57.20785 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6b0b092-33de-34d7-8101-d7edee57f788 | -12.50144 | -57.20839 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62b99169-5967-38bd-b712-da1f18d10761 | -16.04708 | -47.22589 | 2026-05-17 05:23:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3141832b-a68c-3826-8fb1-019c1a01bffd | -16.05309 | -47.23208 | 2026-05-17 05:23:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4cce98f-178a-3c33-9e7d-210d42073238 | -12.49465 | -57.20793 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45aa065a-edc8-352b-92ed-d08741b0bcf2 | -12.51054 | -57.19445 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edf65736-2768-39c0-90f6-84de09989d8c | -12.5043 | -57.21268 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a71f9b99-8aaa-3c99-ae08-8bc846b7fd77 | -12.51454 | -57.19121 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 996c89a6-54c7-3b86-8a8a-06c74b885a57 | -9.84448 | -68.63674 | 2026-05-17 05:23:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c28abbd-d2cb-3e04-91fc-ba938261d17a | -12.50599 | -57.20144 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68dd5a9b-f8e2-3825-979c-f484d8eb5026 | -12.49858 | -57.20411 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f4ebbfa-e456-3d44-a91e-bb7d23c302fe | -16.04602 | -47.23657 | 2026-05-17 05:23:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80f843bd-b519-34c9-ba8f-9716c2a20a42 | -11.85639 | -63.72279 | 2026-05-17 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2657d8e3-1a6f-33b2-978b-3f827a20c6e7 | -11.72933 | -59.28817 | 2026-05-17 05:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 35d4b0af-42d9-349a-aee8-bab3dc25d07e | -12.50941 | -57.20197 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e579a13c-6450-3e52-ab20-bfcfc2033658 | -12.50998 | -57.19822 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b12454e-0f39-3137-b08c-159768162370 | -12.50885 | -57.20573 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e938688b-495e-3b9c-b7c2-9a61cc88eed4 | -12.51171 | -57.21001 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 813cd493-5933-3a94-90a4-672cabf4cd5c | -13.31296 | -47.51627 | 2026-05-17 05:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00dea457-7305-39dd-a848-605895cfc76a | -12.51397 | -57.19499 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b72fb74-a8a4-34d8-9c94-385cc468697d | -12.57647 | -54.75255 | 2026-05-17 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8c28ee67-0ff4-33f2-a7be-de5d77c5120b | -12.56042 | -54.75516 | 2026-05-17 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae495b0a-0d26-32eb-82ec-4fc62eb6b854 | -12.51284 | -57.20251 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efa8325c-82db-305e-af70-1fdee4e14b5f | -12.51111 | -57.19068 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 643fa549-4170-35c0-ba59-0e12e8fe9d71 | -12.50313 | -57.19714 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6102960-d8c8-3a23-b524-19b5489f5f5a | -12.50542 | -57.20519 | 2026-05-17 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc518377-d9d9-36bd-a92a-672244332412 | -16.05363 | -47.22671 | 2026-05-17 05:23:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48c6c288-ab16-3c21-9ac8-f1451608183b | -10.81911 | -58.01614 | 2026-05-17 05:40:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32f34802-b7ca-3e47-9795-4a726bb57380 | -11.48093 | -52.91693 | 2026-05-17 05:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 079273fa-55a2-3b82-824a-05f097664795 | -12.5085 | -57.2063 | 2026-05-17 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08e57c60-0513-3c15-8ef7-fc8702c7c9a9 | -11.44618 | -54.09391 | 2026-05-17 05:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d714cf6e-3ae5-3f75-92a9-42d3641eb7b6 | -9.84173 | -68.63707 | 2026-05-17 05:40:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76854b30-2aa2-3e46-b306-2e1f1d329e6c | -12.5092 | -57.2009 | 2026-05-17 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 873de55b-dad9-35b8-a31c-fb9eb7d97486 | -10.91162 | -54.11951 | 2026-05-17 05:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bd999bb-dd19-3395-b24d-201ba37e40ec | -12.50366 | -57.20565 | 2026-05-17 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59fb5a9a-2c3d-3990-96ec-6f5a7309e287 | -12.50435 | -57.20026 | 2026-05-17 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90866ea3-5aa8-3dda-a5f1-7c01d5d0dff3 | -11.85532 | -63.72284 | 2026-05-17 05:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4baab2d-b5e9-3c73-8feb-8e29eba54a1a | -12.51475 | -57.19609 | 2026-05-17 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cd69c5e-8150-3ec8-90b5-7d0b1d1e9b6b | -10.91111 | -54.12359 | 2026-05-17 05:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d976069-2db5-3fef-9f3a-2c24e5caef06 | -11.43443 | -54.09242 | 2026-05-17 05:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6f44b8f-b0e7-36b9-8091-fb2f87660b45 | -12.50504 | -57.19481 | 2026-05-17 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ca85e1b-1278-3c2a-9d34-ae1830a54e45 | -11.85588 | -63.71922 | 2026-05-17 05:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc000df9-31f6-3e2b-995c-25ec5978e3ea | -12.49082 | -57.74635 | 2026-05-17 05:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e65ba6ac-a24a-35f9-b85c-64e4d26380a4 | -12.5099 | -57.19545 | 2026-05-17 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fc02e17-bbc1-3cc0-bebc-356793cdc427 | -10.91745 | -54.12022 | 2026-05-17 05:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44619259-6e9d-3417-9108-edccd1d1399a | -11.48034 | -52.92211 | 2026-05-17 05:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23eb4401-d073-39d4-855c-ba47d3584e2e | -12.4995 | -57.1996 | 2026-05-17 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| efa8f4f3-9dfc-331e-b528-32d865152896 | -12.49311 | -57.74846 | 2026-05-17 05:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a59873f-c77d-3d90-b39b-121c9833b8a7 | -11.4403 | -54.09319 | 2026-05-17 05:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 460690a0-891a-37df-af0f-307a94348fc7 | -12.51404 | -57.20155 | 2026-05-17 05:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b553c4e-abbb-3815-8416-678d165c8489 | -14.15869 | -52.8814 | 2026-05-17 06:48:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 74301501-2569-340e-bc6a-2d215b073d9d | -9.23 | -46.65199 | 2026-05-17 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 817598a3-fb9e-336c-a468-db88c2e81bed | -5.97437 | -42.44103 | 2026-05-17 11:57:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 2ca1ca7b-2429-3157-817d-70a97fadedff | -8.72298 | -48.33069 | 2026-05-17 11:57:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 17f701c3-f632-318f-8a98-72206aa7c22a | -10.18734 | -46.45897 | 2026-05-17 11:57:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f8bad38e-3ba8-3bb9-9625-9dbef29bb163 | -10.11605 | -50.62975 | 2026-05-17 11:57:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 242736c8-b267-3217-8ccc-36a2708ba5ad | -7.71651 | -44.56 | 2026-05-17 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5290fff1-debe-36b7-8f1f-2ea1499ce8dd | -8.72429 | -48.32169 | 2026-05-17 11:57:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ed18f304-45b8-3bc5-b5a9-6e87553dc0b9 | -10.4049 | -44.93562 | 2026-05-17 11:57:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0ca11c0a-b481-38c2-874e-918ec9219260 | -14.06769 | -44.469 | 2026-05-17 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a7f05b94-205c-3543-abe8-f97a8cba9951 | -14.05528 | -44.48112 | 2026-05-17 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| d9a99871-4e3e-3860-9d88-a4cea7cc7a5a | -11.60893 | -47.09734 | 2026-05-17 12:00:00 | TERRA_M-T | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 90f6cf7a-f55b-3165-9684-1c651fa84cbe | -12.2662 | -43.50884 | 2026-05-17 12:00:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0d3bc242-98de-3c40-afb9-bd922ced8f75 | -11.88633 | -43.80358 | 2026-05-17 12:00:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 04a6bb97-f66c-3961-b96c-eecf176e0047 | -14.06595 | -44.48261 | 2026-05-17 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 29e29252-7227-3dab-ace9-0bc56addd5ba | -12.90043 | -45.05205 | 2026-05-17 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 83c136b8-40cc-3a1e-bfa1-20ce97cd8ddf | -12.9002 | -45.05774 | 2026-05-17 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9b5e6c63-db0b-360d-ac27-5ed4bc213b0c | -11.88459 | -43.81752 | 2026-05-17 12:00:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a15687db-5041-3aef-9108-29c1c84681fb | -14.05701 | -44.46749 | 2026-05-17 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| f08bc1a7-dbf0-36cd-91a1-a16258808e6a | -12.26647 | -43.50299 | 2026-05-17 12:00:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 81453e6c-4446-3551-a3d8-a1308cdf7398 | -10.8336 | -49.773 | 2026-05-17 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 37c43b57-ce50-3b52-a79e-d80ae55bfcee | -14.0523 | -44.4835 | 2026-05-17 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 3549564c-5385-330a-9678-4a6804cdb653 | -14.0718 | -44.48 | 2026-05-17 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| f5ee85ae-86f9-3eba-9b50-2bd40c432ac4 | -14.0523 | -44.4835 | 2026-05-17 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 32bcef48-6300-32ce-bbaf-cf778978e339 | -14.0523 | -44.4835 | 2026-05-17 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 72941a5f-b1b5-340d-843c-d6ea3513ba57 | -14.0523 | -44.4835 | 2026-05-17 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 0e0ee4cf-059a-33ae-813b-e3de35c832d9 | -14.0523 | -44.4835 | 2026-05-17 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |


