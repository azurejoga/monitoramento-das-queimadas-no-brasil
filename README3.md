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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 591bdd83-ca3b-352d-a3bf-be7bb9e8831d | -13.81083 | -47.51233 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| cedd138c-f1b2-3964-9f7d-5ea33b7bf798 | -13.2858 | -47.24843 | 2025-10-02 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| c0300549-745f-3092-aef1-aaccd52b4d41 | -15.94402 | -43.33278 | 2025-10-02 00:11:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 75618e9f-efb3-3bf4-91b4-249b44630276 | -15.49826 | -42.55141 | 2025-10-02 00:11:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 691fbd7b-7e19-3e81-9612-b348e3594db9 | -12.89719 | -46.89871 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 95422433-d0d4-3873-84ec-7e75f935ae19 | -14.21356 | -46.10616 | 2025-10-02 00:11:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 1bf5eccf-4d57-3e38-af4f-a483223e631b | -13.32576 | -43.10948 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 17a5561c-47f0-316b-a49a-ef9212be01b0 | -13.42015 | -47.78877 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c7d23279-7d0d-34ea-aa66-8d346f0e215c | -16.28037 | -42.5531 | 2025-10-02 00:11:00 | TERRA_M-M | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 148ecd76-3c3e-3662-8150-496382d6ac4e | -12.00688 | -41.14762 | 2025-10-02 00:11:00 | TERRA_M-M | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ecba5e8c-432f-347a-9116-013c10cbc8eb | -9.85592 | -46.88932 | 2025-10-02 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 868d9cdf-5560-3cc9-9eea-91fe907b7b92 | -15.22569 | -48.73366 | 2025-10-02 00:11:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 41fce853-37cf-3703-8f60-75d48a0fe034 | -12.72315 | -44.84756 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b1678813-9bf0-3487-9c13-e05d154b579e | -9.917 | -43.71775 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| e9ef4770-ada2-39f5-b594-e50d3fbedee0 | -11.27167 | -47.82156 | 2025-10-02 00:11:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| cde48f80-e471-3fd6-9c97-ea4a1952c334 | -14.4143 | -46.07952 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 900a51c4-bcc7-3ca3-a8c4-afc6ea068119 | -11.44378 | -43.88757 | 2025-10-02 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 33a7df91-cf4a-34bb-ba04-ad789f7380c3 | -13.15827 | -47.79756 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| a392f5dd-7f8e-36f0-bb83-ecb5e4972dd3 | -13.01002 | -45.22163 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| fb0c2ba0-78b3-34a5-a806-c06874dfcee7 | -11.81458 | -45.00486 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| ac86061c-7efe-337d-b447-f14489e9d160 | -15.55423 | -48.17561 | 2025-10-02 00:11:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 4af8c7b4-783e-3a03-b26e-0f97cc0efcd1 | -14.58394 | -46.71326 | 2025-10-02 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| d4f32b0e-cc60-395a-9780-4b3118067cc5 | -11.53561 | -43.55646 | 2025-10-02 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8814fd8b-82f0-355b-bd47-ea759f19d7a1 | -12.58117 | -41.2913 | 2025-10-02 00:11:00 | TERRA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| dc5c515d-36dd-3d04-8122-14bc3a2d5298 | -14.0274 | -47.98515 | 2025-10-02 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e34db636-d108-3b64-9c95-5fc6633b26d4 | -13.864 | -47.9528 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2f100d6e-6e36-3d9d-8db8-aac0ecf21dc5 | -11.54603 | -45.06125 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7650c6f3-7759-3a30-b02d-edc006ff072e | -14.30994 | -45.97761 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 99b512b6-6934-3574-a806-f3b45e311975 | -11.47219 | -44.9875 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f1208714-cb54-310e-a969-50ebf815ac29 | -9.59734 | -43.06803 | 2025-10-02 00:11:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ebed6f09-edf3-380f-8ee3-083e04e4d709 | -16.77875 | -43.03408 | 2025-10-02 00:11:00 | TERRA_M-M | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 28.1 |
| d37e0f46-674f-33d5-a97b-36fdb8e1eb8d | -11.79228 | -44.97789 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 663943be-6e18-3fea-bfa9-14c8ac0dae51 | -12.82857 | -41.53599 | 2025-10-02 00:11:00 | TERRA_M-M | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 4fc2d1c4-c548-39ef-a592-420bc202bb11 | -14.40573 | -46.0933 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 6a8f1059-593f-3405-96ea-d9021917a8e1 | -13.15202 | -47.84131 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| c165bb31-460f-3996-a35c-d8cc18360d18 | -11.52555 | -43.54876 | 2025-10-02 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 128c4501-10f2-3fb0-8c08-7016af93d7f3 | -15.22321 | -47.18082 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| da46f2d6-1641-3f8d-bf96-3c27d18604bd | -9.90574 | -43.70124 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4d19cfc5-09c1-3ef0-87c9-a8835bbd7839 | -13.8126 | -47.52754 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 44.7 |
| f4f555a4-9c71-3276-9d99-85c4ac284bb0 | -11.85886 | -41.91333 | 2025-10-02 00:11:00 | TERRA_M-M | BARRO ALTO | BAHIA | Brasil | 2903235 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| bdec634d-e28c-31dc-9e03-6c426b83d79a | -11.48054 | -44.9903 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7b7bf7e5-b650-3855-8246-78908790f0aa | -13.87045 | -51.26813 | 2025-10-02 00:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| f6e9fe80-b99a-3b31-984c-ad934da21d0e | -14.36932 | -45.96389 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 474f1298-6e87-391d-9972-aa2e96d72d0d | -14.34711 | -43.84634 | 2025-10-02 00:11:00 | TERRA_M-M | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5da701da-4c9d-39d1-babf-2c55ae986110 | -11.43517 | -47.28224 | 2025-10-02 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cd29a850-1006-3328-8baf-6644a365a360 | -12.11051 | -43.43941 | 2025-10-02 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 47816151-3310-3a6d-b836-05c0e10885c9 | -12.11688 | -43.42018 | 2025-10-02 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bcc072e3-afc1-3f05-a0e4-9671890e1977 | -10.85707 | -45.41611 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 010eb83b-fe87-3c5c-b768-1291c4f30c9e | -11.41861 | -43.50614 | 2025-10-02 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 461364fa-2ae9-39f2-962a-b2dd2ab9663e | -14.31802 | -45.88025 | 2025-10-02 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5f1d7a60-ce45-3754-a244-f436128c3a95 | -11.48181 | -44.99994 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 90b53bdb-d96f-3f9a-bc6b-d8b66c253ef0 | -15.01961 | -42.22771 | 2025-10-02 00:11:00 | TERRA_M-M | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 2151e9c1-bdbe-3737-868f-719d26fd1013 | -11.49293 | -43.5078 | 2025-10-02 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 108da9fe-ad4e-3b0b-997e-1dc45abea00d | -13.37849 | -43.76122 | 2025-10-02 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e8236b9f-6700-312c-8342-6a2db6d634ec | -15.01834 | -42.21862 | 2025-10-02 00:11:00 | TERRA_M-M | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 3ea71443-d998-39d8-83d3-774d12aec0ed | -14.41582 | -46.09169 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 5c5973ab-1a6e-3b64-991f-d7e97adbdf3f | -16.00186 | -40.01885 | 2025-10-02 00:11:00 | TERRA_M-M | SALTO DA DIVISA | MINAS GERAIS | Brasil | 3157104 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 53fb0369-23ec-3161-a12c-fc52d2f8d3bb | -11.42619 | -43.49591 | 2025-10-02 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b41c5da3-bb80-3b36-9606-2e7d8a642163 | -15.82942 | -42.6233 | 2025-10-02 00:11:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 8c92f50c-667e-3e04-8b55-cbb358adedd2 | -14.30843 | -45.96556 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 17b356ac-b0e7-31b3-9512-3b0fcd4cdef4 | -13.46668 | -47.22921 | 2025-10-02 00:11:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| bf8c98c5-587f-3aae-ac71-ea0a8e56e0b2 | -14.32797 | -45.87884 | 2025-10-02 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a615f316-bd4f-3012-badd-8019f673a1ee | -11.82378 | -45.00357 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| de57d726-cd20-3c68-a5e3-2b21a69739ed | -12.25521 | -47.80555 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 52fa3e17-0bff-3517-a909-6952bb5b931d | -14.35008 | -45.9724 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b1c9150a-f383-3356-ad4e-1ebfb7efed97 | -11.03419 | -47.83414 | 2025-10-02 00:11:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8de3cff0-5b28-352e-8a14-1da7878a5753 | -10.95159 | -48.56336 | 2025-10-02 00:11:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d9927d64-ecbc-32bb-8693-d6bf1b9b3ee8 | -13.81245 | -47.5333 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 8677f974-a22b-3337-b034-5df9ab232d2e | -11.61585 | -45.03484 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| a549b5f6-377c-34c7-9d00-f04a9f78ddfd | -11.67793 | -47.49669 | 2025-10-02 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7170f186-1ced-370e-855d-e9e93d6e254e | -15.78387 | -43.71698 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 358571c2-91ee-3a45-937a-a46f9d2590be | -11.67187 | -44.28053 | 2025-10-02 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 82728051-2a05-3e14-978f-a4dd0fdab72f | -14.9836 | -46.89881 | 2025-10-02 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 104432cc-0e83-3c26-9ffb-fd43a1f09db8 | -14.43934 | -46.36674 | 2025-10-02 00:11:00 | TERRA_M-M | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c04b5f64-973d-3826-9933-cc55b42df414 | -13.46818 | -47.24152 | 2025-10-02 00:11:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 8ea26490-372e-36b9-bd2b-a8b0be838e13 | -9.80129 | -45.92343 | 2025-10-02 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c00d8265-b225-3a15-8cf5-4186b6f758e9 | -11.83038 | -44.98284 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 132a9647-ab33-3aa0-95d2-2a5c22825177 | -9.95619 | -43.72387 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4476e05f-a379-3059-9000-906afdfd3601 | -11.44505 | -43.50231 | 2025-10-02 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a2f6c642-97b0-37ed-90c5-ccf55611f21e | -14.21701 | -44.94442 | 2025-10-02 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 29e42197-cae4-3b20-80b5-50589b0e22e7 | -9.9486 | -43.73404 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 314.9 |
| 14bc881d-739d-3200-81fc-44e95f9a58fc | -12.153 | -46.6691 | 2025-10-02 00:11:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 540f6d3f-7299-3c0a-a8c5-7cd0097e0b91 | -12.47644 | -47.28381 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e61861e3-7a36-31e1-bf2f-2de1352d7adc | -11.80017 | -44.96684 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| e047d5e4-54ab-328b-872c-f3f8ae27b355 | -16.88017 | -40.59656 | 2025-10-02 00:11:00 | TERRA_M-M | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 8ae3a621-b03f-3088-a410-010cbc2a63dc | -11.19056 | -47.18653 | 2025-10-02 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 915e4d5f-f389-3901-ac47-a0fac5ae8f41 | -16.77998 | -43.04332 | 2025-10-02 00:11:00 | TERRA_M-M | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0342cf39-515a-30e8-89d6-3b878198c898 | -13.5284 | -47.25557 | 2025-10-02 00:11:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1ee39f04-60f3-370b-b4ba-2edc72005c7c | -10.84388 | -45.38793 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| fe85953a-ffed-3a0d-a047-ae658260594a | -13.41058 | -47.80508 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 762eb694-c5b2-32de-a624-bf9e9f848c9e | -13.21725 | -48.49696 | 2025-10-02 00:11:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e0689ef0-90cb-3f24-8ea4-ce696d576729 | -10.95859 | -46.6564 | 2025-10-02 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b8ae4355-1210-3df8-95b8-df7261a5754f | -13.75988 | -48.70596 | 2025-10-02 00:11:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 31.7 |
| ca8dbe74-8e7a-318b-8173-cf65d4391d22 | -14.91063 | -47.24067 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5e284e68-06ac-3829-a1ac-f3e3aa57bdb2 | -10.91703 | -46.65022 | 2025-10-02 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c775bde2-57c5-3eeb-a10a-34577e576c3f | -11.35122 | -44.98082 | 2025-10-02 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 08b3217e-cc46-3bb1-945f-eabbedf3f7ab | -13.56448 | -47.27945 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 512cd0a7-c745-35b4-ac1d-2d923aa69159 | -12.70313 | -48.58065 | 2025-10-02 00:11:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 1e1c6345-9c48-3c93-a3e3-d14b156d32d3 | -11.60027 | -47.22154 | 2025-10-02 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 078d7024-c3d2-300b-b37d-74aa598c3997 | -11.91818 | -46.74368 | 2025-10-02 00:11:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |


[Clique aqui para ver as próximas entradas](README4.md)
