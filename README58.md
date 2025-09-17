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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e41604c-26a7-3e1a-b43c-e3c9b001a392 | -8.9536 | -46.2874 | 2025-09-17 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 54eb88d9-70d5-3aec-bf86-3a3c75808dbc | -12.0051 | -46.6763 | 2025-09-17 12:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 6376916d-7da6-3e6d-b882-5d93ae8b5157 | -9.0478 | -44.8936 | 2025-09-17 12:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 7a1fb685-38b4-368b-a427-2e025985db22 | -3.28817 | -43.52731 | 2025-09-17 12:34:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 4e6c63ea-c252-3521-955b-67492282576d | -5.80245 | -43.47655 | 2025-09-17 12:34:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| b10a04cc-52ba-30cd-982b-88a080a9a9bd | -3.8091 | -41.66175 | 2025-09-17 12:34:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 69071ee2-f533-3cce-b1c0-5052643693bd | -6.41018 | -43.35258 | 2025-09-17 12:34:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| d5438fa3-96c3-3213-8f6f-8fad409420f8 | -4.5457 | -46.67634 | 2025-09-17 12:34:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 49fe2f99-6bb4-36fb-a029-b4dd426d4b8f | -3.52282 | -44.02348 | 2025-09-17 12:34:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| fbc0fd03-3579-3b6c-8328-3553a0d88721 | -2.98905 | -49.29248 | 2025-09-17 12:34:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 399ab9b9-a7ea-3735-a84b-a1e3cdf62b98 | -3.81196 | -41.68989 | 2025-09-17 12:34:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 50.8 |
| a2f1d4f0-ad17-3928-b2c7-bfdf228d5662 | -3.80006 | -44.10034 | 2025-09-17 12:34:00 | TERRA_M-T | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 2b487678-0a70-380e-9346-db188cee26cd | -3.27243 | -42.06638 | 2025-09-17 12:34:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| ae1f78ad-d258-35f6-aad7-fe80b5f8b3cd | -6.1612 | -44.52502 | 2025-09-17 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 0fcb20c4-9ade-3cf8-9ae6-36392743905e | -6.0037 | -44.33776 | 2025-09-17 12:34:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| a1d12e89-2509-3baf-9507-6f6b0b48ef0f | -4.81204 | -47.33016 | 2025-09-17 12:34:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 371ae638-5585-3331-bf4f-505dc040241c | -6.15747 | -44.53048 | 2025-09-17 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 7557be2f-09ae-300e-a05e-543251c6257b | -3.79718 | -44.12134 | 2025-09-17 12:34:00 | TERRA_M-T | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 380a166f-f26e-3a33-ad25-3e9121f0ba96 | -5.94667 | -47.09796 | 2025-09-17 12:34:00 | TERRA_M-T | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 7b244212-1e82-340e-a1fe-968d6b0626cb | -6.00159 | -44.32049 | 2025-09-17 12:34:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| bb8cfb62-9eea-3c96-b7c1-ff99507c052d | -6.19924 | -45.11816 | 2025-09-17 12:34:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| edda4e9b-3c85-3721-99be-efe966f1585c | -5.99879 | -44.3424 | 2025-09-17 12:34:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| d20c93f8-0a7b-3dc8-af36-e7fa7cfdefe6 | -3.81325 | -44.10211 | 2025-09-17 12:34:00 | TERRA_M-T | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| cdf45be7-f7fa-3549-a88a-f41e2f2089ba | -3.81009 | -44.10732 | 2025-09-17 12:34:00 | TERRA_M-T | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| d46dc93d-6bcd-33ce-922d-e2f846356c46 | -3.80481 | -41.69451 | 2025-09-17 12:34:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 4364693f-b616-3974-a548-c054639025b9 | -5.95559 | -47.11259 | 2025-09-17 12:34:00 | TERRA_M-T | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 659c8567-3508-389c-95f3-d4705c831a9a | -6.53173 | -42.12711 | 2025-09-17 12:34:00 | TERRA_M-T | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 80456483-6f53-32da-8e99-0902d82e380a | -6.00668 | -44.31583 | 2025-09-17 12:34:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 494a65a4-db70-357e-91b6-08e2aadd2d9f | -6.12596 | -43.94898 | 2025-09-17 12:34:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| b7ffb2b0-1dfe-3b65-af78-0922d701971c | -1.27459 | -48.96634 | 2025-09-17 12:34:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ce473142-e90a-33b4-a042-6469c663af8a | -6.54003 | -42.12123 | 2025-09-17 12:34:00 | TERRA_M-T | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 38.5 |
| b13c65c6-a1e3-39af-99ae-92e7273f9b6b | -3.66539 | -43.64735 | 2025-09-17 12:34:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| a41c2074-18c3-393c-9c0c-215910d1a7b6 | -6.15827 | -44.5466 | 2025-09-17 12:34:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 0c08283b-65ef-3c03-b2cf-64c17dce54e8 | -5.78592 | -43.92231 | 2025-09-17 12:34:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 06e5078c-88fa-39da-957d-6f79f0530ae7 | -8.94066 | -45.53006 | 2025-09-17 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 273.8 |
| beafe73f-57a4-30a6-a2b2-a65a449177ae | -10.64727 | -42.33876 | 2025-09-17 12:36:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 67.3 |
| d834da88-7d42-390e-9576-df19ac0215c4 | -8.19592 | -44.79623 | 2025-09-17 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| e662b93a-4690-3eed-bf7f-314afd9ddf45 | -8.65772 | -46.44005 | 2025-09-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 55fbc36a-89c8-3ee4-b75b-ec28d73e1940 | -7.53908 | -44.75411 | 2025-09-17 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 142.2 |
| ad248b50-27b6-3542-b5e4-ef83088db1d9 | -10.17272 | -52.62522 | 2025-09-17 12:36:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eb07806d-9633-313f-ae54-5c454d975a91 | -12.42044 | -47.81949 | 2025-09-17 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| fa3cedb6-ba03-3168-abdc-db2425c02772 | -7.58577 | -44.56496 | 2025-09-17 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 59308e12-4204-3187-bc14-a0bacd4b2aea | -6.88089 | -43.97105 | 2025-09-17 12:36:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 37.1 |
| e4bf49c3-3bf1-3e4c-913c-32fc0028da20 | -7.6542 | -44.45851 | 2025-09-17 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 45ce2cbf-9afd-325e-9e48-807dfee70bc3 | -10.63042 | -42.33685 | 2025-09-17 12:36:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 51.5 |
| fa6da4f6-ea4f-3767-b515-ae5700bd77f1 | -10.91951 | -47.82164 | 2025-09-17 12:36:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 4dab518c-b5af-34fd-96ed-177b82262198 | -11.21476 | -47.39745 | 2025-09-17 12:36:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 308.7 |
| 395609f9-6b51-319a-987a-e0c2b6a5314c | -12.00765 | -46.70066 | 2025-09-17 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 0d10a8bb-38df-3fcb-b18d-c12f1666ca50 | -8.58197 | -47.57427 | 2025-09-17 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 7db8cb42-a1e7-347d-b674-d4c1a6db02a8 | -8.66225 | -46.35006 | 2025-09-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 5c8f6822-2793-309d-9d46-871b3fdd6e07 | -8.55733 | -47.5647 | 2025-09-17 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| a0485871-313d-3fad-9dec-ec046be7c344 | -10.63462 | -42.2991 | 2025-09-17 12:36:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 124.4 |
| 685a0309-abe5-3371-92b8-57655bcf908a | -5.62224 | -51.63081 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 8607effd-b80e-35e5-a201-4f278ac5af48 | -12.86324 | -47.12995 | 2025-09-17 12:36:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 558c669b-7101-3771-a7af-64c98b9b443f | -8.95321 | -45.5375 | 2025-09-17 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 22a725c2-ea4c-3c24-8173-76d829faa5d7 | -12.68312 | -45.28923 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 775caec5-704e-3bd9-b8f7-b7cf4aa13577 | -7.65134 | -44.48117 | 2025-09-17 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 2b1b2b0f-69e7-3864-9fc2-23a594b32816 | -12.2029 | -53.63074 | 2025-09-17 12:36:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 277ded53-00b5-3eda-9c73-21b5082d9ded | -6.87628 | -43.96367 | 2025-09-17 12:36:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| fb3cb51d-f236-3360-83c5-a0e982889df9 | -10.07499 | -48.17217 | 2025-09-17 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 2810e719-988a-395e-b03c-aa545addafa6 | -8.68984 | -46.37698 | 2025-09-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 98e77960-c155-34f7-993e-cb7cfbc40e26 | -7.07194 | -44.34236 | 2025-09-17 12:36:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| aedafa66-4824-3f3a-a1cb-96ba16a78cdb | -9.57743 | -48.09484 | 2025-09-17 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 7d84743c-dfd2-3281-a769-c2138f91d3ef | -12.44337 | -49.72807 | 2025-09-17 12:36:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 733de6ef-6d23-356b-857b-149dcbabf28d | -8.95604 | -45.5118 | 2025-09-17 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 36e77d7a-acf7-3185-abea-fecc9bce99fa | -5.61909 | -51.72726 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0357c2a5-e739-369b-b28e-e5a37b066bee | -12.72972 | -47.99739 | 2025-09-17 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 88b1cdc6-e40e-3de0-a6ea-38521394e5d8 | -11.99543 | -46.69919 | 2025-09-17 12:36:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 421cea1a-9f3d-3978-8ba0-a56e4f35513e | -11.34727 | -50.849 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 8618db37-0841-3791-a262-189991464ef7 | -8.44821 | -47.69424 | 2025-09-17 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| acee931e-e0a0-3490-a16a-c14eefeb2439 | -8.14883 | -46.74984 | 2025-09-17 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| c0b85517-b3cd-3bd8-97f5-963ad48ff96d | -11.3486 | -50.83942 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 31.0 |
| bd840b75-56ec-3a74-9ebb-50283edabb5f | -9.6683 | -45.87101 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ee931ef3-ddab-3ee9-a744-886a5c507aee | -12.11022 | -47.55476 | 2025-09-17 12:36:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a3cba56d-fd85-3a13-9b29-613a6dbf3357 | -8.90419 | -47.87801 | 2025-09-17 12:36:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9eefb73c-d54c-3ae6-a863-1d9580d4e706 | -11.64458 | -46.57864 | 2025-09-17 12:36:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| cd3f98e2-5815-34e0-9cf9-ffe766102e6a | -7.59137 | -44.5602 | 2025-09-17 12:36:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 19560257-c0b7-36ad-87ee-d794fa1e3914 | -13.95246 | -44.9309 | 2025-09-17 12:36:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 6f0cfa21-fb54-3176-ad6e-d9eb0bcfb486 | -6.86684 | -43.96938 | 2025-09-17 12:36:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 464c12cc-56e3-36b1-b98a-0e17d682fa4e | -9.03788 | -44.88247 | 2025-09-17 12:36:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 3ab5a42e-318e-359d-94cf-5ea976775179 | -9.96078 | -45.9275 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 7784fc34-0d73-38a1-8074-1b342154d771 | -11.17048 | -45.33317 | 2025-09-17 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 898fdc12-3b68-37a0-84ef-52cd94bb9273 | -9.12423 | -44.88202 | 2025-09-17 12:36:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| e5cfb73e-ae56-3392-b6fe-92a3585997b7 | -8.97711 | -46.27658 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| b733c36b-0a48-3f9f-a3ed-99b58577ddff | -7.8274 | -46.15447 | 2025-09-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 7e0e7420-22c5-36f9-8a57-4f909e1a3e22 | -12.71112 | -47.96538 | 2025-09-17 12:36:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 82fca750-8041-345a-9497-4179829ac2ae | -8.5837 | -47.56079 | 2025-09-17 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 8df6b533-df1d-322e-94b8-654a08a94642 | -8.97934 | -46.2591 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| a61fc721-929c-35e2-a79a-edcfce66d42a | -8.64386 | -46.45483 | 2025-09-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| e681e2ca-6d0d-3736-b6b4-a3e467e40022 | -6.48457 | -45.73358 | 2025-09-17 12:36:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 45003d0d-4e39-3976-99ab-caa2aae5d2a7 | -5.88843 | -51.96551 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ff5d403a-ea6e-341e-8d4f-a3f3acfc7dbf | -8.93573 | -45.88277 | 2025-09-17 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| be209768-ee95-3cc0-a098-b601adc77e09 | -8.94287 | -45.51586 | 2025-09-17 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 13d29f5b-b955-3f9f-b5a7-e14b1e933b5a | -7.82518 | -46.17132 | 2025-09-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 4df9c23e-7212-35f9-88ea-c22e7db57dc7 | -9.48349 | -48.26974 | 2025-09-17 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2bf0f1cf-ae66-3199-a88e-35744bf35459 | -8.56811 | -47.56614 | 2025-09-17 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 4ade54c0-8b28-37ab-be0f-10ddcb57353c | -8.9166 | -46.2269 | 2025-09-17 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 836109df-5286-30cf-9393-ab5a246fc8b8 | -5.95048 | -51.27232 | 2025-09-17 12:36:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ec623730-2e84-3987-be79-752fe792bafd | -9.47477 | -48.25598 | 2025-09-17 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 94355823-6e8e-3d80-9e01-725801914bf5 | -12.19212 | -54.74336 | 2025-09-17 12:36:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README59.md)
