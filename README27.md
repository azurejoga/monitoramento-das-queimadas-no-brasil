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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 588897c4-29fc-3694-9524-211758c9e29a | -6.71841 | -42.80124 | 2025-10-07 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 377a7bff-0530-348d-9b83-d2fc47018eaf | -6.05769 | -42.56556 | 2025-10-07 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 32566cbc-fb42-3b8a-9416-b5cb11506636 | -8.85905 | -46.08769 | 2025-10-07 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de2ed037-c7d4-3982-86c4-a8b7c2409cad | -7.02562 | -42.7524 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ce1b452e-c6ee-37b0-8398-8f58c75817ec | -10.55373 | -54.86906 | 2025-10-07 04:08:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5443336c-7a05-35ee-b8c9-d0b2c5cf93bb | -10.44965 | -50.35466 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ee7c37ac-6ade-3741-bea1-27a4a57bd9ae | -5.33772 | -43.38018 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e73b4ead-7cbd-3554-9223-16deb293861e | -11.15849 | -47.95345 | 2025-10-07 04:08:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3383531-aee5-34c6-835b-269ddd76406c | -5.50253 | -43.07648 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6ee9e136-b36b-3720-a870-d57a1cff7a57 | -12.01843 | -47.78466 | 2025-10-07 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bf301582-e7fe-3450-ae53-dc2c54e711b9 | -7.57262 | -43.97054 | 2025-10-07 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f7034b6-3724-3cd5-aebb-037736f61c51 | -8.65175 | -46.28216 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 774141a8-3f03-3fd3-8d9f-fa70b4344ab8 | -8.17762 | -50.3034 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c631c5cf-8327-32de-833f-23a3b9602a28 | -10.84871 | -44.16231 | 2025-10-07 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 002951ea-e756-3b80-bb50-39e58bf3f5a3 | -5.70905 | -44.83221 | 2025-10-07 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30e70323-14d8-32c2-948f-6f69723f58ef | -11.2333 | -48.69278 | 2025-10-07 04:08:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d27812cb-7f31-3445-81e6-cc5332bb75f1 | -9.73861 | -48.08017 | 2025-10-07 04:08:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d65c5dde-36e9-37e7-ab36-028f9a7bbcc2 | -9.02191 | -50.68615 | 2025-10-07 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bf21c5f-db45-3ac8-a9f6-28f1099bf0a5 | -8.88171 | -46.0442 | 2025-10-07 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f1cd508-a375-3540-a42c-2d907120945c | -10.45353 | -50.41711 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ba2d8834-9810-3fd8-82a1-7641aad08339 | -8.67745 | -49.94192 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bbf5f60f-6720-3c89-8387-a2e3353d1b38 | -7.56919 | -43.96998 | 2025-10-07 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 732af592-6bc8-3a13-a1de-07a18826bceb | -6.49407 | -43.64119 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36136595-0c0b-36e1-b90c-1f2c24bd134e | -11.95619 | -45.4828 | 2025-10-07 04:08:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 517e366b-8ffe-3ae2-bcde-459563265f56 | -8.56166 | -50.08022 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fc96cfab-635e-36ca-8307-1ac6f7e9cf49 | -10.7989 | -48.58772 | 2025-10-07 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3aad8c35-d696-375f-b790-ffaf69595df7 | -7.68285 | -50.21206 | 2025-10-07 04:08:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 228a8c95-01e8-3053-b937-3f306ac37cb5 | -6.45694 | -44.57998 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0f94c4a3-e680-3df7-9be9-e0d0510a44a1 | -7.03561 | -42.75402 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a46f2843-b498-352c-87b2-61cf1341df84 | -9.18571 | -47.83324 | 2025-10-07 04:08:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b9434d14-93e8-34ff-bb41-82c75a530b34 | -11.8009 | -45.05506 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1083140d-10c7-3b79-aa13-965d253d5e94 | -6.81577 | -42.78812 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6e422dbc-8e60-30fa-bad1-95bf26a18a86 | -9.96666 | -43.77595 | 2025-10-07 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 47aeedc5-8f3d-375e-b227-9678b5a69b93 | -10.36448 | -44.98087 | 2025-10-07 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 803786d8-2fa8-3857-afbb-0bdf10e11ae0 | -8.55187 | -50.07838 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 245da9bd-463a-3bac-a4f2-7e154fcbbf53 | -5.7746 | -45.74525 | 2025-10-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d25b6e34-1095-3d42-aeec-9c849e9cc68b | -8.64873 | -46.2767 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d52addd1-06cd-3eec-a9c7-d01a562993c5 | -6.25112 | -43.2729 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0edc1ff0-18ff-339a-95ac-9e869837d2cc | -8.17094 | -43.35947 | 2025-10-07 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 01fc1a06-5a41-3f53-b4c9-cc1425e60758 | -7.2907 | -41.98128 | 2025-10-07 04:08:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b5f20a47-0a68-3d76-bb4b-114cdaf260c1 | -10.09944 | -50.52272 | 2025-10-07 04:08:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fe2aaf6-bb42-3c64-bcef-53e50b2f8862 | -6.4498 | -44.57886 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| f50bf6d1-e1d3-36e6-889f-5e486cf7466e | -8.55041 | -46.25611 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c810e1cd-1238-3d12-81d1-77c4abf2d819 | -11.95721 | -45.48265 | 2025-10-07 04:08:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc93e469-8f74-3a8a-9b69-a0dd2951ad75 | -8.49865 | -46.3121 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a92c804d-0c17-3373-822b-66e51bc4d5fb | -5.7615 | -45.75299 | 2025-10-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a617e633-2e65-33c8-91b4-6f2b14ecb2b8 | -6.96762 | -42.00054 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7481f9e8-2137-37a2-96cf-66f7ad6ac6b5 | -5.5998 | -44.4249 | 2025-10-07 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8afc470e-7e43-34c3-aa7a-6b688dcaf84d | -8.52954 | -46.2444 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| cc567260-4da1-3fcc-bef4-b3fa986a43b7 | -8.06595 | -48.48142 | 2025-10-07 04:08:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 476089d0-1b44-3185-8b00-58421567b76e | -8.65781 | -46.2929 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ea63d085-4aa6-34a4-b0ae-b97c743322e8 | -8.54563 | -46.24169 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| eee2a884-9445-30c6-9a52-07366105477c | -7.46473 | -43.09233 | 2025-10-07 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d6e926d4-db05-3085-a482-95d9239a177e | -7.68694 | -42.40302 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 205c5699-83d6-34e4-b6a7-06e1738d37ce | -6.44912 | -44.58298 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| ae83eed7-8692-3525-a65b-c1cb122db6ea | -5.46851 | -42.91139 | 2025-10-07 04:08:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 11001e59-6b52-32a1-aa37-8629066d83e9 | -11.79341 | -45.10107 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a0f1018-bda4-3fb8-a284-63edf4d4953f | -12.21676 | -44.24924 | 2025-10-07 04:08:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81ab93de-cfda-392a-b61b-dfcbca86a7eb | -11.72186 | -44.44192 | 2025-10-07 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef69c1f8-cdb8-355f-8b00-c9716c95b1f2 | -12.02118 | -47.79226 | 2025-10-07 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c51a3666-91db-3920-9fd6-392430e220fe | -7.79034 | -42.60924 | 2025-10-07 04:08:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 24174553-814f-3f76-b438-dfc9417bf99c | -8.66162 | -46.29354 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 96659509-d0f0-39d5-ac26-0d6bf66ecb0a | -11.94575 | -46.43188 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14f4fe5b-f216-300d-97d1-16a191fc602b | -7.43701 | -41.12935 | 2025-10-07 04:08:00 | NOAA-21 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2d7e80ca-1315-3ffc-82f0-b777ddbfd74b | -11.15719 | -47.96089 | 2025-10-07 04:08:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb375a73-ba80-3fcf-ba2f-d42a3393a334 | -8.21923 | -43.75553 | 2025-10-07 04:08:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5ffca908-c468-313d-ade0-4b9c68e6b39e | -11.84511 | -44.91223 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c8e35dc-7e27-3dc2-8bcd-d4a5a5d044cb | -7.56858 | -43.97374 | 2025-10-07 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f833ed9d-87be-3e9f-a5f2-f60023fd5ce2 | -8.36428 | -37.60477 | 2025-10-07 04:08:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| adc523a2-4924-3117-8ec8-0a86e447ab4a | -9.41899 | -49.10806 | 2025-10-07 04:08:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d3744fd-4b45-3b04-a6bc-42b8edec3d2d | -10.15909 | -45.99546 | 2025-10-07 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dcab80c7-60c7-349b-aeaa-3d556c2ac490 | -8.49098 | -46.31097 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47346bc6-54f7-3d36-b640-aa30315bb461 | -6.98596 | -42.87304 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 37.3 |
| 7a6c9dd2-c2f8-3a14-90c0-8781a83468a7 | -10.26219 | -44.37877 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c920f019-d73f-3b91-a1b4-ef340678a17b | -8.18763 | -50.30524 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e49ecb89-f43c-3f64-9f25-4af44fe48646 | -11.60792 | -43.11592 | 2025-10-07 04:08:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6223c4f8-9b67-3384-a4a1-f7a8137f96f6 | -7.46832 | -42.62202 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fec2d0c0-3350-393f-b5f3-595bca9d9724 | -8.49544 | -46.33128 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 24e24b96-a192-3019-85c4-a2ee9dd79539 | -7.41612 | -41.1298 | 2025-10-07 04:08:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 77cd596a-80d3-3489-be16-bbfe6d53486e | -5.47533 | -42.89021 | 2025-10-07 04:08:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 13b12e1f-8955-3510-a8d9-38c2861905a8 | -7.01003 | -42.78616 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3d0bd5a1-ace3-3025-84f1-f0f27ee2aaa4 | -8.14249 | -44.46556 | 2025-10-07 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee8f8e79-5d04-35db-9466-15711cde88c9 | -5.48898 | -43.07431 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| de945f07-9b46-3dde-b04c-ae79685562dc | -11.56579 | -44.66494 | 2025-10-07 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d95b44c-785a-3c61-b59f-535bee50f744 | -4.69259 | -45.83631 | 2025-10-07 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| dd8637fe-b210-37e7-a049-ff5e8d958f20 | -9.33144 | -54.51814 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 952ebb8c-6e35-30cb-a9b8-e85e33ee71c0 | -11.94647 | -46.44985 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 29a97bed-25fa-375f-9248-1050b73665b7 | -8.18296 | -50.30148 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aaad152d-3d57-32cc-8710-34b733a90904 | -5.41265 | -42.66307 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 58686e4d-985c-3f2a-8236-817e9bcade93 | -11.77731 | -45.13446 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fef097fc-4cba-34f7-ab6d-a1952f617bb1 | -8.17863 | -50.29765 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0ab8623-df60-3fd1-a3bf-afbd6655e841 | -5.23862 | -46.56776 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e62bd3c1-c37a-3af1-85fa-7461a3ac2a01 | -11.73975 | -43.2927 | 2025-10-07 04:08:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 40971cb4-2aa1-3d01-9e95-ff60c7d1fe35 | -5.7061 | -44.82733 | 2025-10-07 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb97226b-1cb3-3f76-b22c-8c6434006226 | -10.4294 | -50.32862 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ccd95b63-7648-39cc-948a-41cd6187dd1c | -5.25415 | -43.15746 | 2025-10-07 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58bc0f19-7eb3-3127-ab45-5e33a1c91605 | -6.24713 | -43.27604 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7dbf4f85-3b0c-3ebc-8ee1-8fd76f6c5c30 | -11.95303 | -45.48602 | 2025-10-07 04:08:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18d00ec2-814b-33c5-9cd4-46d8fb5e6911 | -7.69851 | -42.39414 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b3936e1d-8b26-316a-a3cc-6cdbf3e59d0c | -10.84534 | -44.16176 | 2025-10-07 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README28.md)
