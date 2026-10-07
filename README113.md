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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecd5ea8a-eacc-31fd-bb61-00a7dfe15d51 | -5.23737 | -50.91184 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a948976-712e-346d-b4c7-99c0279da9b6 | -4.06187 | -59.83655 | 2026-10-07 05:42:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b2045b4-0235-3d69-bbff-d4f9820e6d3d | -9.05575 | -65.48489 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a0517d8-5077-379e-a677-d61b15dc9d8b | -7.18797 | -52.62231 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c4831a0-433e-3ba5-a558-3b68a83d397a | -5.37419 | -56.06392 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9933a29-565c-381b-bc4f-7c79b3876709 | -5.67664 | -53.49683 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7337dcf3-67a7-3de4-94a1-801d815795f7 | -8.82934 | -62.41777 | 2026-10-07 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d315fba-c3f1-303d-b982-8bdabded04cd | -9.1384 | -65.29626 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e644cea8-8e03-38b7-9129-ccc46bdd4838 | -3.66107 | -60.62734 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7c70460d-5888-39de-8d57-e92ceab00c6a | -4.76617 | -55.66618 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d26aa629-1037-3e22-8d41-d6bfb8d8df74 | -8.59825 | -67.05488 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2001d2f7-3902-3b3c-9075-9f4737c9b564 | -4.38299 | -59.90422 | 2026-10-07 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51726c3c-2a20-3ab3-a235-714c5f4e7699 | -9.51956 | -54.74048 | 2026-10-07 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98bc8a79-32e7-331a-946d-f9b9a8a43c44 | -5.89046 | -53.63836 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10b44bb0-e3b6-3c6a-a962-003beb5987df | -6.21584 | -52.83305 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d83d764b-d64b-360e-97c9-7ae0eb05e1c9 | -3.65883 | -60.61982 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a675ad4-6efb-35a6-a37c-73628a3ad782 | -8.15061 | -64.0765 | 2026-10-07 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c0df1bc-555f-3dac-9873-a37fa57798b2 | -6.40618 | -52.72232 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06cbe5c1-3ae1-3a6b-8e0a-8e066c89015c | -6.44203 | -55.01958 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b6ad0f3-763f-3328-8e1e-d5ae33bcc444 | -8.63033 | -67.0554 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 612b0849-946f-35a1-85d1-7c334cadade3 | -6.44821 | -55.02697 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4ff9d62-d9f8-3982-af54-ce3ff2e2dd6e | -3.58975 | -61.62881 | 2026-10-07 05:42:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3457c002-b5b5-3e08-a424-8c66b91e34b0 | -8.63117 | -67.05045 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 338d86bd-0659-3287-b3f8-78abe9da97ae | -6.00115 | -53.50796 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b41e29f-c5ba-3047-b02a-b8970efa010e | -7.74785 | -54.94923 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a795d448-b924-37cc-b5a8-51f1c66048c5 | -7.70145 | -72.80969 | 2026-10-07 05:42:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f213a511-908b-38f0-a186-e9db61028f97 | -6.00158 | -53.50497 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fce5f7f-0292-3719-90d5-969ea3e564a1 | -6.40765 | -52.71185 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec0bc9f6-0c84-3998-b995-3fc190273e8c | -5.23557 | -50.90992 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e317cf78-6cc6-3b10-b139-4cd066f7979b | -4.75869 | -55.65685 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6efbf70-5ad7-3bf3-9c79-fbf55b09d248 | -6.15432 | -51.73641 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e937ccba-aef5-3095-8683-784eca9f9534 | -9.22524 | -63.60917 | 2026-10-07 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6301526b-e21b-31e6-813b-0017f424e5bd | -5.23797 | -50.90753 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b68bcc08-8a11-34f4-8f12-e7dfa4c298bc | -8.99246 | -65.43369 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8e38f5b-7776-387d-ab80-5be5be1371de | -3.75087 | -60.59079 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c288faa-5407-3b82-ba86-5fce35f0c3f8 | -7.03093 | -71.75124 | 2026-10-07 05:42:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cae0b327-cd89-32cd-ab68-28afe43e0b94 | -3.59696 | -61.6264 | 2026-10-07 05:42:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8a5433b-9548-3b7a-b098-f805ab4f492a | -4.75273 | -55.65662 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 610498f5-a460-38d0-b1c8-fa29fc42ef74 | -5.67752 | -53.49081 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7049699-e300-3700-a631-1f17aac48f20 | -6.00669 | -53.50581 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68c149ed-8eb2-3b6d-8564-6672579a0bc3 | -5.99609 | -53.50679 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1b54062-a028-37dd-aff9-02c1389dde28 | -8.97329 | -65.4388 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c433b58d-c3e4-3b46-a5cb-ea978ee9c6a3 | -8.97974 | -65.44405 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd67f9f6-fa83-3cd2-a86d-88726ee044db | -3.66671 | -60.62432 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4661003e-c07f-38c5-9a8f-3bcf00ac0107 | -4.75336 | -55.65258 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29ca76fb-ad5f-34a6-8c2a-6d2ade374ca3 | -7.8817 | -72.35347 | 2026-10-07 05:42:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e4dcbae9-ea94-31e0-b615-438df5d8fbcf | -4.76365 | -55.65318 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94a5c1c9-2fdb-3ac3-95c0-1296f58d1c2a | -9.59963 | -61.82137 | 2026-10-07 05:42:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb583deb-56ce-346e-8d27-19617e1274ae | -8.18844 | -70.10515 | 2026-10-07 05:42:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cf028a7-4b0c-3e3a-ac46-a9587b487c4a | -7.89556 | -54.72413 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f4a0a0d-9c60-3a05-b2b7-73d0adf82f4e | -7.74823 | -54.9453 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86b8135d-fca3-3305-8810-9ced80b9ca9b | -8.61528 | -67.19158 | 2026-10-07 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f03c6967-ea9c-3032-8c4f-0e3756bbc220 | -4.65771 | -56.21795 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 961658a0-b56f-35c7-bb2b-f6a9fb44afec | -8.54314 | -66.97742 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 09461161-df4a-353c-bd72-9e95fa1f956c | -8.28644 | -50.27303 | 2026-10-07 05:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1da73b55-ce34-313e-b51a-eaa7b2891cdf | -7.44533 | -73.20177 | 2026-10-07 05:42:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d51600ec-4374-35db-8517-2e250f55e3e7 | -4.75061 | -55.65156 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6a0622e-1ecd-3f25-b7d7-1c1d7e6dc6de | -5.95549 | -55.34366 | 2026-10-07 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bae88ae0-7f1e-3132-9877-a948c879144b | -15.25078 | -43.26346 | 2026-10-07 05:44:00 | AQUA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 1cc9ba3c-dfc1-3c22-b819-5d47a9ad684a | -15.24946 | -43.27097 | 2026-10-07 05:44:00 | AQUA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 52.3 |
| 8c05f1a3-4c95-3286-b4d4-f51165190bdf | -9.1572 | -65.9445 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5829a9ed-4f45-387b-9b95-de20b8bee6f9 | -10.27929 | -60.54534 | 2026-10-07 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7d90d4d-0cc3-3f7c-bf84-b03d4c044adc | -9.22727 | -67.89166 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12c4e07d-1da8-3259-b621-39c6c76dd133 | -9.46044 | -64.33685 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 937e8559-9253-3ab5-a49f-b3abed9ace6d | -9.89212 | -64.27962 | 2026-10-07 05:44:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 837a25b8-541f-3d67-aca4-dd81a11f0f61 | -10.1573 | -69.3382 | 2026-10-07 05:44:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f043d1e1-fb24-3d86-b779-dcb696eaa24c | -9.45892 | -67.08628 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5296bd1d-92e1-3d1c-8be7-41f6632def84 | -9.33961 | -65.45538 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 820a94ce-fba4-3881-9f6c-6262430cd96f | -9.60929 | -63.80695 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9e0214b-7735-3f36-88eb-f8791c6eab2f | -9.59131 | -65.24289 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c52fa34b-bd2a-3b7d-b3b8-50151b02f93e | -8.73854 | -69.41528 | 2026-10-07 05:44:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d372667-cc0f-33e8-8da8-42e94b04dd5b | -10.58497 | -69.24108 | 2026-10-07 05:44:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ef02a474-91d9-34ba-85bf-23dd17643db0 | -10.24621 | -68.30118 | 2026-10-07 05:44:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ed54b123-32de-32db-8b73-fb115f649528 | -9.67195 | -66.8176 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6095ac16-ea55-3c56-a339-ff2a987dff57 | -9.59196 | -65.23895 | 2026-10-07 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 97eff2ac-0af1-3a8d-82c6-dd69dfb2c760 | -9.10283 | -67.93804 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c174cf2c-fca8-3003-8190-403a0ba6af68 | -8.87102 | -69.17517 | 2026-10-07 05:44:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1cc18549-b9a6-3985-927c-65d010246cb7 | -9.08868 | -67.68317 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74136285-2446-3ff5-9ee7-240a28aafe01 | -9.52624 | -67.4156 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a21b6ebf-9dac-347c-93bd-11d65d5bc868 | -9.28997 | -65.64349 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f92a9198-5182-38ee-9c8e-37599eb59c07 | -10.61892 | -60.48552 | 2026-10-07 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d1ec4f0-b47d-38be-a7fd-e57591195d74 | -9.5223 | -67.41492 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc8ae27c-1381-3086-820e-6a181521e73b | -8.45326 | -70.21243 | 2026-10-07 05:44:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2af649e4-3c38-3435-8f7d-2292f8de5b28 | -8.20962 | -71.00792 | 2026-10-07 05:44:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50edd013-6030-3550-b9a1-60803d99f9b0 | -8.20908 | -71.01088 | 2026-10-07 05:44:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a028c578-d4f7-336d-8b95-ac93e1b3a573 | -9.10688 | -67.72301 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b45f420b-1b7d-388b-b575-5930be97944d | -9.16013 | -65.94939 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bc41f4e-47dc-34a4-9220-6a339b9b8492 | -8.24634 | -70.83633 | 2026-10-07 05:44:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3660e0e6-f6f9-3ae9-91a4-84a6ca20a98d | -9.11373 | -67.8274 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb01ca89-3e9d-3694-80e1-2dead00c7171 | -9.67117 | -66.82224 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 430cadb3-cb3e-318f-8124-b54c8f448680 | -9.33606 | -65.45477 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b586eea1-b708-3e8b-bfcd-0c7980efdb15 | -8.91168 | -68.79287 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e362ab4e-22ea-39bc-b442-e2f72c01f211 | -9.15961 | -65.99767 | 2026-10-07 05:44:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc0ded29-1616-3956-aee5-01c5e349b401 | -12.47475 | -51.28777 | 2026-10-07 05:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| baa7cff7-b34c-3645-83d3-f30991e66677 | -9.23071 | -67.89603 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d6c7955-793d-3d16-8930-9c71490fdfe5 | -12.46848 | -51.28702 | 2026-10-07 05:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f548fd42-03eb-3f71-b742-c5333b953e44 | -8.71121 | -69.46291 | 2026-10-07 05:44:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8aed6f9-911f-3553-99bd-51c99e222591 | -8.73483 | -69.98569 | 2026-10-07 05:44:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c4f6b85-5232-3aa3-8d1d-a1df0f470850 | -11.01652 | -68.56919 | 2026-10-07 05:44:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64bd893e-a2dd-3eb1-9dfb-5a43496b5050 | -8.86094 | -68.77531 | 2026-10-07 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README114.md)
