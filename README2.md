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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2784e82-7217-3fb8-a57e-039d4f665872 | -22.52058 | -43.74438 | 2025-09-15 00:28:00 | TERRA_M-M | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 58b3260f-4d2b-3e69-9af0-46e1f35e5371 | -16.99143 | -45.87928 | 2025-09-15 00:28:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f22f9d3d-7c0d-3175-a33c-90d496dc57d7 | -17.10171 | -49.91256 | 2025-09-15 00:28:00 | TERRA_M-M | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b8d2fc97-cc63-3bbf-bc0c-4a182c02e337 | -23.25608 | -49.50763 | 2025-09-15 00:28:00 | TERRA_M-M | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| b234a8bf-1453-3c11-a692-3edd81f12f6b | -17.31844 | -46.11085 | 2025-09-15 00:28:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bff11ae6-a518-368f-a5b5-bf37c7de54cf | -18.61538 | -50.39565 | 2025-09-15 00:28:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 27.9 |
| 0c370750-18e2-34e9-b4e2-a68796aba978 | -19.21576 | -42.44205 | 2025-09-15 00:28:00 | TERRA_M-M | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 7e588794-15a6-3e05-9037-c94f5f5273e1 | -18.16537 | -49.2025 | 2025-09-15 00:28:00 | TERRA_M-M | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 63f15b5d-6927-3742-ac45-e756c7eb6682 | -18.03894 | -50.93807 | 2025-09-15 00:28:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 06e7a122-a728-32fc-808b-afb7bd9ea007 | -17.00157 | -45.88712 | 2025-09-15 00:28:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 58aa2153-0e15-34af-b40d-8b29af9e71c9 | -19.72207 | -45.44516 | 2025-09-15 00:28:00 | TERRA_M-M | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f95b4aa5-fef4-3909-83b2-ca791ccec272 | -18.71345 | -51.77628 | 2025-09-15 00:28:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| afc9668e-639d-3169-bd96-310a109435d5 | -17.76431 | -44.52066 | 2025-09-15 00:28:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7b688953-981e-39ab-a2e9-5e44a4ebb41d | -17.35083 | -42.65434 | 2025-09-15 00:28:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 5647c247-a555-3b8c-bfce-7cf90174afd6 | -21.925 | -46.55109 | 2025-09-15 00:28:00 | TERRA_M-M | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 72052007-208f-337e-ae2c-208ed78ee454 | -23.14578 | -49.63467 | 2025-09-15 00:28:00 | TERRA_M-M | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 34fba6c7-55b8-3c93-b53c-411abe021079 | -21.56989 | -48.0397 | 2025-09-15 00:28:00 | TERRA_M-M | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 6ee73230-2e87-34f4-80ce-2ba39d3074a7 | -21.25967 | -45.63204 | 2025-09-15 00:28:00 | TERRA_M-M | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 855048c5-865e-3e64-b23f-6632bb5d2e55 | -21.26097 | -45.64147 | 2025-09-15 00:28:00 | TERRA_M-M | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 9deef486-f407-3792-b5d8-4bdfce861f47 | -17.23985 | -49.4605 | 2025-09-15 00:28:00 | TERRA_M-M | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 309280e7-07fa-3eda-8e71-2c961bd951e7 | -17.73203 | -47.95113 | 2025-09-15 00:28:00 | TERRA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a73b783e-525f-3650-8363-81d0919d135e | -17.47869 | -42.42752 | 2025-09-15 00:28:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b6e9d3c8-141a-3c32-8277-c3248e2c5152 | -22.20661 | -48.34901 | 2025-09-15 00:28:00 | TERRA_M-M | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 781d6580-6224-3bde-84d0-934aa12e1dca | -21.30275 | -51.6799 | 2025-09-15 00:28:00 | TERRA_M-M | SÃO JOÃO DO PAU D'ALHO | SÃO PAULO | Brasil | 3549300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 49.2 |
| 181aaa72-fb5a-3dc0-8126-dba202a63362 | -22.20799 | -48.36046 | 2025-09-15 00:28:00 | TERRA_M-M | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 23d75e57-3a50-3743-829e-544e229d8cec | -19.6306 | -43.7332 | 2025-09-15 00:28:00 | TERRA_M-M | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1a145f1e-c167-392a-9cd0-45c69a25bdd5 | -20.55931 | -44.91179 | 2025-09-15 00:28:00 | TERRA_M-M | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 31efa897-fb50-31af-8535-2961a3b06046 | -17.34889 | -42.64196 | 2025-09-15 00:28:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 5a8a0ba7-d0ae-3ad8-b54a-1eb4d758ebab | -19.63217 | -43.74362 | 2025-09-15 00:28:00 | TERRA_M-M | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6656eb29-c9a7-38bd-a12c-5d132c0d327d | -7.8861 | -63.7135 | 2025-09-15 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| e28ab655-6b42-32db-bfd7-095640aaa649 | -7.8942 | -43.5857 | 2025-09-15 00:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 89c0bc15-c41b-301b-b99c-cbbd2d28325e | -7.8753 | -43.5876 | 2025-09-15 00:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 270.1 |
| fc35fa86-837c-3d50-afb5-1b97e8003b21 | -17.7632 | -42.6538 | 2025-09-15 00:30:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.7 |
| c0b14abf-02f2-32cd-8db1-e83bbb93909d | -7.8564 | -43.5896 | 2025-09-15 00:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 616.7 |
| d8ef4224-7902-3e96-8e77-b88e8bca2a8c | -7.8862 | -63.6947 | 2025-09-15 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 31242fda-0eb1-3006-a59b-ab21be006e17 | -5.7047 | -49.1998 | 2025-09-15 00:30:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| aa3e8790-c999-3510-a870-3ba142a19b9b | -12.7875 | -47.9541 | 2025-09-15 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 6bd0525d-bb72-37ae-8ef9-05d4efeda9f5 | -15.779 | -53.4608 | 2025-09-15 00:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| a10f7d75-e302-339e-bd19-25c1348d092d | -7.8567 | -43.5662 | 2025-09-15 00:30:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 387.6 |
| fb8599a5-01df-3364-8246-14e3975bbb04 | -11.78 | -47.5583 | 2025-09-15 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 9186af90-b102-34e1-8de6-3be00f92862e | -12.58 | -45.636 | 2025-09-15 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 11e290ad-225f-3213-9919-6704c21edf61 | -12.006 | -47.7505 | 2025-09-15 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 4e6b5f25-f9a5-3af0-8b51-2de5ac105d19 | -15.7981 | -53.4793 | 2025-09-15 00:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| dfb4b80f-d7d6-3615-8990-7c27b36c57c9 | -7.8756 | -43.5643 | 2025-09-15 00:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 185.7 |
| ed851413-516e-369b-addc-72a6dad94c3f | -21.2964 | -51.6957 | 2025-09-15 00:30:00 | GOES-19 | SANTA MERCEDES | SÃO PAULO | Brasil | 3547106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.7 |
| 422333c7-8385-3b7e-9f86-4135ac2cad35 | -17.3442 | -42.6333 | 2025-09-15 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 2b7d9f7e-b1e6-3079-be1a-4347ef46a770 | -16.491 | -55.1067 | 2025-09-15 00:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 107.9 |
| 119b45c4-1f96-34b5-b8d4-c0365b6f6bbe | -15.7985 | -53.4582 | 2025-09-15 00:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 127.2 |
| a91b8be4-2ff2-34c3-a065-e81b6a1739ea | -12.5607 | -45.639 | 2025-09-15 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 7cd9d4a6-c917-32c2-b388-76b2f9e8b948 | -12.62325 | -47.94018 | 2025-09-15 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c5c36ddc-18fb-37c9-a56c-1e1f3d952004 | -15.64902 | -47.29987 | 2025-09-15 00:30:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 86c25c65-1c14-3820-89c4-0ee52e5f27c7 | -15.42585 | -47.3452 | 2025-09-15 00:30:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4690ce23-b836-3184-b3fe-3419597392bb | -15.80149 | -53.47994 | 2025-09-15 00:30:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 3fccb6f8-9030-3970-ae66-870772584c61 | -12.96435 | -48.00555 | 2025-09-15 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f07af79b-cf32-3038-8944-cdac98d7d7ae | -16.38486 | -48.90713 | 2025-09-15 00:30:00 | TERRA_M-M | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e2fbb90d-292d-39a2-8742-91bb09e16877 | -14.94037 | -46.55907 | 2025-09-15 00:30:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 38.6 |
| b4c29b83-454f-327e-a587-e1eddc88cc40 | -15.89844 | -49.98895 | 2025-09-15 00:30:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| f97d53eb-c143-30c5-a239-45938b832b2d | -16.48021 | -55.12324 | 2025-09-15 00:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 27.0 |
| 07129a35-ad51-3e7d-94cb-c3c0a19543e4 | -14.94288 | -46.57713 | 2025-09-15 00:30:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 7d35910c-9d82-3878-999b-884ee720277d | -14.43602 | -43.22824 | 2025-09-15 00:30:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| bee16347-c0b1-3ab5-8ab0-7269638017ee | -15.78564 | -53.47491 | 2025-09-15 00:30:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| ac769c58-1b14-334c-84db-d2985ef9ff56 | -16.03418 | -47.55963 | 2025-09-15 00:30:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 52278a0a-397d-3cd2-9c81-0ddae01f1c5b | -12.11808 | -44.84475 | 2025-09-15 00:30:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9f1417b7-d714-34ae-bf0a-0623bdcd8f28 | -15.74286 | -45.08278 | 2025-09-15 00:30:00 | TERRA_M-M | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ed436f78-f920-3027-9db2-609219e6dad8 | -15.04862 | -48.17126 | 2025-09-15 00:30:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7e6b2baa-bb6d-3451-ad8e-e384cfebc0c9 | -16.49715 | -55.12831 | 2025-09-15 00:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 51280be7-9c9b-3848-89f7-f48bd335a8a2 | -12.11652 | -44.83429 | 2025-09-15 00:30:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ed4cde87-ff90-3f53-9305-37c85a99dca8 | -16.49538 | -55.12234 | 2025-09-15 00:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 104.9 |
| c1cc0a75-dd8f-3b4c-a2d1-734fc6e78b80 | -12.59792 | -45.72065 | 2025-09-15 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2748720c-20b8-3e10-b930-9dc98cc142c9 | -12.82632 | -47.1964 | 2025-09-15 00:30:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 998bb4d6-2c57-3ea6-b369-960bddefe592 | -14.43326 | -43.22235 | 2025-09-15 00:30:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 9d542607-d6de-3f96-b49d-7bd8e37f5e4c | -16.49259 | -55.09329 | 2025-09-15 00:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 128.9 |
| ad97ba9d-3920-30df-a0f1-6f8030e49408 | -12.98721 | -47.97401 | 2025-09-15 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 69e11a64-9dbb-3210-af04-3b2a3e562c46 | -12.80877 | -47.13479 | 2025-09-15 00:30:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e7a87bc-e1d2-3989-9afb-8aa3f60b4c3b | -14.3457 | -46.13634 | 2025-09-15 00:30:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cb565274-469f-32f1-b62a-fc636b26073b | -13.87497 | -48.13361 | 2025-09-15 00:30:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b76bfe04-23dc-384b-a274-66bfb03d833d | -14.25562 | -43.20053 | 2025-09-15 00:30:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| b9521b58-2ae8-3f40-be81-b14aa2bc13a9 | -12.68664 | -47.73116 | 2025-09-15 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| fbffe26a-bb97-3129-bed7-1c9ee74c9c7e | -12.56738 | -45.6334 | 2025-09-15 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bc8c4810-ddf1-3b35-bf23-128c71951452 | -12.98597 | -47.96494 | 2025-09-15 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 5c7b4637-af70-31cb-87da-b1c370b54c74 | -15.7883 | -53.48102 | 2025-09-15 00:30:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 30.9 |
| b2d541a6-7121-3287-bb93-4966dd570fc6 | -15.77294 | -53.46258 | 2025-09-15 00:30:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 610168fe-e0e1-38af-beef-0cfdbea7dab7 | -15.65028 | -47.30912 | 2025-09-15 00:30:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 395d03c3-9f57-346d-aee0-2c4267181064 | -12.83771 | -47.14886 | 2025-09-15 00:30:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3497f2cc-1f96-31d6-99c6-83930b91de68 | -15.4246 | -47.33598 | 2025-09-15 00:30:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7c8eda78-d279-35a9-9949-5fc28f2b1a55 | -15.7859 | -53.45981 | 2025-09-15 00:30:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 33.0 |
| d749bb1c-e538-3665-8e78-096f4731b3e0 | -14.9391 | -46.55 | 2025-09-15 00:30:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 25.0 |
| f75dcc1b-9d0c-334d-a3a9-01ca2e24cc53 | -12.08893 | -44.87704 | 2025-09-15 00:30:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 956300c0-0afe-3b9f-bd69-6c3d8ffa50fc | -15.57695 | -48.68646 | 2025-09-15 00:30:00 | TERRA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b542749a-2349-3c2b-b301-8000c513e2b8 | -15.10253 | -52.49658 | 2025-09-15 00:30:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 30a3cc6b-131e-3765-8315-8c1131087c97 | -14.81424 | -48.13885 | 2025-09-15 00:30:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| d755321f-858b-3322-8f82-24edd043bb33 | -15.10063 | -52.48027 | 2025-09-15 00:30:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ef5f5e1a-bd03-3dae-b82a-e4d162b1388c | -15.7753 | -53.48367 | 2025-09-15 00:30:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| db87d26f-2fa0-3d22-8d48-64bfb0ccb0dc | -12.6778 | -47.73244 | 2025-09-15 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| de26ae32-f905-3c37-b26b-987b8c51a8be | -16.49418 | -55.09949 | 2025-09-15 00:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 166.6 |
| 26339771-4e29-392a-9aa2-20b078fa0da5 | -14.50648 | -47.35493 | 2025-09-15 00:30:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 7ac68200-1922-3fdc-ad8b-1ed4f9206313 | -15.6428 | -47.04233 | 2025-09-15 00:30:00 | TERRA_M-M | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0bebc8c2-9381-31c9-b4df-691685c20cdf | -14.80525 | -48.1403 | 2025-09-15 00:30:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8e4898b7-4161-36b7-863e-5f680b39b058 | -15.02303 | -47.98097 | 2025-09-15 00:30:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5cac1198-9885-33ca-b001-f78c729989eb | -14.62881 | -46.37412 | 2025-09-15 00:30:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README3.md)
