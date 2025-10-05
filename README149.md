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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61304cef-5112-36f7-9f93-85efe08c45a0 | -12.98168 | -51.04172 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e539b770-65e8-39cc-866e-96fc325727f5 | -10.94048 | -47.10139 | 2025-10-05 06:14:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7daa69b5-fdea-37d9-806b-9eca62343a4a | -16.0118 | -50.95207 | 2025-10-05 06:14:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2ab1d13d-87ea-30c3-b925-d57502e8b994 | -12.93972 | -51.01032 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ea33fa52-6ce8-3f4b-976f-48fc6026f225 | -17.87831 | -57.58037 | 2025-10-05 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 46ec67f3-10ba-3204-956e-63ad224370c0 | -11.10751 | -47.87116 | 2025-10-05 06:14:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 25d58763-dc92-3349-9567-0364301798dc | -13.27504 | -47.18231 | 2025-10-05 06:14:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 337f8dfc-36f5-386d-a9b3-2767fa349f5a | -10.45595 | -57.49831 | 2025-10-05 06:14:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 01dd73e4-813e-3721-a4f5-5a2a45a9204c | -13.35182 | -48.05708 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| fa05b7d2-c78d-3b44-bac4-1b4d6d1d73fc | -15.24234 | -56.76342 | 2025-10-05 06:14:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 9f0e5c33-9a83-3052-b398-c031b18afc7f | -13.09458 | -47.83998 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ed80619f-02ff-3175-8af0-3f47c3d86aaa | -13.58227 | -48.15793 | 2025-10-05 06:14:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 056023da-dabe-3888-bfdd-8302d6f98a07 | -10.46208 | -47.80787 | 2025-10-05 06:14:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ef3f10d2-b9e8-34b2-bed7-b07e93e33a2c | -15.2346 | -49.29855 | 2025-10-05 06:14:00 | AQUA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4541e343-aa75-393e-800a-08f2bac12c3b | -16.03693 | -51.03905 | 2025-10-05 06:14:00 | AQUA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d3629952-4a31-3aae-8f43-ca7d3e5bc45c | -16.03558 | -51.04846 | 2025-10-05 06:14:00 | AQUA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 899331d1-0186-3bd1-ac22-4d8f16d1f5e5 | -14.33424 | -52.96857 | 2025-10-05 06:14:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4b2ca96f-09b5-3225-9d69-7d03b8923003 | -12.56328 | -54.76719 | 2025-10-05 06:14:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 91bf2701-6b13-3c8b-adb5-002443114fe6 | -9.33782 | -54.50832 | 2025-10-05 06:14:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 392a4c4b-f157-3f84-8a16-a6772efe4317 | -14.58875 | -52.45095 | 2025-10-05 06:14:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1b09cedc-7787-35c5-99b0-62cafc636822 | -15.98899 | -50.91911 | 2025-10-05 06:14:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ea04c211-8725-3446-b3df-1dedee666665 | -10.84775 | -47.97629 | 2025-10-05 06:14:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 175df694-38e6-3510-bdb9-007234ad5e7f | -13.49388 | -47.27224 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 92c35f87-510f-3aec-a3da-bdc86c0d04ec | -14.93641 | -46.82847 | 2025-10-05 06:14:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f2178ad5-8b8c-3391-9a75-60527b219192 | -11.95643 | -51.46798 | 2025-10-05 06:14:00 | AQUA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d87b85e4-5288-3cc5-bf0d-0d8967c70082 | -12.40967 | -51.10202 | 2025-10-05 06:14:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c44104f6-dd58-3503-88fb-b10dffdd55b9 | -14.92479 | -46.83755 | 2025-10-05 06:14:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 6ba471cd-9870-3f0a-b924-a9bb61d7e9ce | -16.34271 | -51.47512 | 2025-10-05 06:14:00 | AQUA_M-M | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3143d267-58c4-3e50-8444-5363d8c01413 | -9.45233 | -56.64782 | 2025-10-05 06:14:00 | AQUA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d6e8edd1-1092-3fb1-bb95-fdcb9c4da4dc | -13.37864 | -47.5407 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2d0587e4-335c-3e63-8c39-7b33f1b154ca | -13.16183 | -50.87991 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| c99a1a8e-84f4-3a19-85ea-8221ec496ef1 | -11.35058 | -47.66914 | 2025-10-05 06:14:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 999abdd2-aa4f-35ab-92a6-d48a8a050fb2 | -13.15161 | -50.88768 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f5609664-22c5-3946-bcae-841d58422fdd | -13.12637 | -50.87457 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 41.6 |
| fff9c030-c85b-37df-af31-de417239dac9 | -18.33349 | -45.89671 | 2025-10-05 06:14:00 | AQUA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 24.6 |
| c10e9438-bef1-355c-9750-ec1a30bc66d4 | -10.80306 | -48.81924 | 2025-10-05 06:14:00 | AQUA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fdd6d96a-5546-3b46-8dba-13056fb44dac | -10.59589 | -54.35204 | 2025-10-05 06:14:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 90b450c1-f4ac-3872-90ac-4655e4ac1d45 | -9.32555 | -54.51913 | 2025-10-05 06:14:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| b6c13c8a-f71f-3d8a-b01f-fd4df5a1edd7 | -12.60667 | -48.12452 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 335fc448-3735-3f20-b8fc-26d595ee3147 | -11.02227 | -46.69373 | 2025-10-05 06:14:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 1060e623-ddfd-3229-b5d1-dbfea0f4cf22 | -13.30615 | -48.08786 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 926898a5-05db-3a12-a8a6-675f781b9bd8 | -13.14622 | -50.92409 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1dc4149d-670f-3a1f-b4fd-6aba2c5ddfc1 | -13.14275 | -50.88635 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 353.8 |
| 6152c261-3f3c-39e0-9412-0a2e40118cd0 | -12.81398 | -46.85423 | 2025-10-05 06:14:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f4ccda01-a3a8-3abb-8e6c-0056ca576d5e | -15.91398 | -48.81889 | 2025-10-05 06:14:00 | AQUA_M-M | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3eac0cd5-a3a2-3dab-a81e-79003cfc65f6 | -13.17353 | -50.86958 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4fccf1ea-1926-31d0-b06f-e84c9ed0f725 | -16.34543 | -51.4565 | 2025-10-05 06:14:00 | AQUA_M-M | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fa60618b-f844-3cdb-a36f-d846bfe9092d | -11.71022 | -45.34787 | 2025-10-05 06:14:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8061c1e9-cc5a-3965-bb4e-efcf813005fe | -10.35251 | -48.15939 | 2025-10-05 06:14:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 3f6599fe-cd1c-3bb0-b910-3cc8d981892e | -10.5946 | -54.35878 | 2025-10-05 06:14:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 5620172a-2b37-35a8-8086-fd9fa8b6f4d1 | -18.24366 | -53.32581 | 2025-10-05 06:14:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 49feab61-768b-32cf-b2ea-6a3de024d6f9 | -12.56167 | -48.15464 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 98bd1578-3c2c-3546-9db7-09f59dde3807 | -18.17616 | -53.3526 | 2025-10-05 06:14:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f8615427-e676-30bb-b6c6-ed5da94c749e | -13.30289 | -48.11218 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| da4883b2-17e0-3756-8a0e-19d7b4f2850c | -12.27263 | -49.19162 | 2025-10-05 06:14:00 | AQUA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0bf63d88-4a0a-3c29-ad12-d5c5a40f55c2 | -15.5444 | -46.82837 | 2025-10-05 06:14:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7f03c3e9-bd08-323f-8e3e-9a05519134cd | -13.25052 | -47.81185 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cfb1e7af-bb37-3221-a9af-70a228b3c9c8 | -11.80927 | -46.82571 | 2025-10-05 06:14:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c2d0f5ba-56c2-3763-b333-6e57bf82bb1b | -16.12716 | -53.97854 | 2025-10-05 06:14:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3b623a95-090a-3d8a-a102-e0eb6950293a | -12.59337 | -48.14682 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7359ffa0-3461-3f45-a01a-eefc59ac651d | -13.362 | -48.05861 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 3832824b-45ff-39e0-a45f-4ef389cbd3d8 | -18.17473 | -53.36188 | 2025-10-05 06:14:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7c2f3256-1b3b-3db0-849c-28a7201810f6 | -13.16318 | -50.87079 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 15cdf865-6981-32f2-9bdb-67f33e0eca87 | -11.2309 | -47.79288 | 2025-10-05 06:14:00 | AQUA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f79908f9-ed8d-3810-b015-2ad97a9cd6a8 | -14.65135 | -48.33215 | 2025-10-05 06:14:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 9b40e7cc-f467-31bb-a1d2-d46ed17df8ff | -16.34406 | -51.46585 | 2025-10-05 06:14:00 | AQUA_M-M | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 8d1a3ec4-8e50-36bb-b3f3-f1f0c70df1bd | -13.09621 | -47.82793 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| da8af8f3-886c-3ee7-b609-8eeb3483a7a4 | -18.25121 | -53.35165 | 2025-10-05 06:14:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 38080516-68aa-3f52-b14b-6b5a72b07374 | -12.81378 | -46.84723 | 2025-10-05 06:14:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 65e71c22-4339-3f35-9147-a34115b91c3c | -16.11962 | -53.96728 | 2025-10-05 06:14:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 95c1814d-59b3-3de1-bda7-9ff8a2f3d753 | -15.29816 | -46.31135 | 2025-10-05 06:14:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4bc816ec-ca2f-3454-83ae-1efc32a26080 | -18.14062 | -53.33982 | 2025-10-05 06:14:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 22178707-ce5a-3218-89c2-856ef41e0c43 | -13.34161 | -48.05571 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 724f66f8-1ede-31a1-b39d-aff5b4bad434 | -15.58182 | -52.48197 | 2025-10-05 06:14:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 83d7a5e1-3c7b-3a21-bdda-bfd528c95c93 | -14.9892 | -49.9761 | 2025-10-05 06:14:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3fe84128-3dbc-346c-b54a-5d00b1403efc | -17.96181 | -57.57247 | 2025-10-05 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 1fbf0f50-2d53-324e-b916-e85f76ceb1b9 | -12.98703 | -51.00552 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c2a55cbc-d047-349a-8e1a-2f85443ef094 | -17.93458 | -57.59757 | 2025-10-05 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 83c2544e-cc40-3b72-8052-d674cda9b10f | -10.36083 | -48.17061 | 2025-10-05 06:14:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 16e8a543-636f-32e2-b41d-ec45594f47a1 | -17.94544 | -57.60065 | 2025-10-05 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 7d092092-604e-301b-a8bb-2c334e0cc219 | -10.00885 | -48.26229 | 2025-10-05 06:14:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cd455619-32cb-3e38-a17b-a34ea1fa0110 | -13.31795 | -48.07716 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 4940d9d6-bfb4-3ecf-8cc8-47111ba0aa7a | -13.36239 | -47.5827 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0fcdeb18-1a81-33dc-b7a5-62ad2935658a | -16.07276 | -50.91785 | 2025-10-05 06:14:00 | AQUA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| ab08673e-7466-39ff-89aa-de2aae8f62e1 | -16.11806 | -53.97705 | 2025-10-05 06:14:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| e3766864-febf-35a7-b366-59deea7d0179 | -14.75124 | -54.65445 | 2025-10-05 06:14:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d274e872-8c70-3d67-ba63-ff8f721b68f9 | -15.59529 | -52.51199 | 2025-10-05 06:14:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 04dfb8f8-ec8d-38a4-a8eb-544423bae3dc | -13.33141 | -48.05431 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 28ba25b6-db35-370b-a6db-c092cd9e49de | -16.12872 | -53.96877 | 2025-10-05 06:14:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5cf5033f-0b5f-38bf-bcf1-f66b331c18d4 | -18.33607 | -45.87479 | 2025-10-05 06:14:00 | AQUA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 91.1 |
| f876442b-9a17-369a-8e48-04d7fa876b6b | -13.25961 | -47.61899 | 2025-10-05 06:14:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 51e176f2-44ab-3025-8d69-b8442fdd1580 | -18.25406 | -53.33315 | 2025-10-05 06:14:00 | AQUA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 60.9 |
| b748de6a-2937-3000-97dc-dbf5da7dba5a | -10.45278 | -48.3769 | 2025-10-05 06:14:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2bd33bc2-a8a2-3059-a6ce-7cee4c845768 | -13.23257 | -47.81485 | 2025-10-05 06:14:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 690b433f-943a-3c86-89c5-8f8d7c24ae3f | -14.6868 | -48.30024 | 2025-10-05 06:14:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 160e749d-44c2-3d66-863f-f4d14f0e3a9a | -12.97418 | -51.03133 | 2025-10-05 06:14:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 761eccc1-68e4-361c-b00f-3c09d984999e | -15.57577 | -52.46237 | 2025-10-05 06:14:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b49c306c-a335-39e6-8525-e3070ae7add0 | -12.81583 | -46.83982 | 2025-10-05 06:14:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 41557fed-58d4-3c45-8647-c6feefea58e6 | -11.15114 | -47.92993 | 2025-10-05 06:14:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 84465767-760d-3d68-acb2-044e757144f7 | -17.92385 | -57.59382 | 2025-10-05 06:14:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |


[Clique aqui para ver as próximas entradas](README150.md)
