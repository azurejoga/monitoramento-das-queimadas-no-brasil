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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5534a528-f68b-3a41-a417-1d0836e9c6e2 | -8.58459 | -44.66645 | 2025-10-01 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5aa947ec-d288-30ba-8f21-1fb7d69d279f | -8.86726 | -46.57898 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 39e7421c-98bb-33f9-8d09-d127f008f2e1 | -12.79164 | -46.85243 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e909ae00-e4da-3b7f-9e78-d8a956bc0f42 | -9.41893 | -47.32907 | 2025-10-01 12:00:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 52a61eb6-3b6d-3da6-ab95-1320077290ec | -13.22053 | -48.4985 | 2025-10-01 12:00:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 504477fa-cc74-301e-bd91-563c27100b53 | -10.90549 | -46.51987 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 5dae6751-d218-3132-a1a6-eab126678f07 | -12.21462 | -47.79597 | 2025-10-01 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2ee55033-5567-33d6-94b3-77f9b6bc8d76 | -12.8493 | -40.44239 | 2025-10-01 12:00:00 | TERRA_M-T | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| c3c5c7df-13e3-302d-9193-106d53514cb7 | -10.83041 | -47.94974 | 2025-10-01 12:00:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 39edae13-5c94-30b1-8f16-1aee54db3315 | -13.01776 | -45.19531 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| cd97d886-5c8c-34cf-8a74-755de765d5cf | -12.71342 | -46.89497 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 04852d56-1c3f-3f35-b0d4-08ce8426d95f | -10.98263 | -46.55058 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 3b706a6e-3c48-392a-9434-dca91ecf7c8f | -11.46483 | -44.96287 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b36d89fc-f535-3025-ae76-1f7bb5b6388b | -9.46707 | -45.47672 | 2025-10-01 12:00:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 18a1f759-2749-310d-a887-fa84985a50d2 | -12.24901 | -47.80763 | 2025-10-01 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| b3ecd2bc-45c0-3346-901e-1a109ff1fc0e | -11.46214 | -45.0427 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| aae7b8e6-2281-38bc-a532-33e858b91543 | -13.9184 | -42.7505 | 2025-10-01 12:00:00 | TERRA_M-T | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 02160e03-03cc-3786-b475-548b89d2d3e5 | -13.17433 | -47.79374 | 2025-10-01 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| db37d82a-ba5a-3615-ab55-08971d9dc70e | -9.12979 | -43.03426 | 2025-10-01 12:00:00 | TERRA_M-T | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 6cd99e86-de02-323e-a788-11f5bf366292 | -11.17946 | -47.19921 | 2025-10-01 12:00:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 18ad7708-ef32-3b4e-b67d-914a857cc54b | -11.7876 | -47.57964 | 2025-10-01 12:00:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 06fe9fb4-743b-3563-8069-3baeb0607596 | -8.52039 | -44.67152 | 2025-10-01 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 43.2 |
| affc96d2-11be-31a1-b13a-e2dd70b05732 | -10.97245 | -46.54895 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 15b1d8a5-c3a4-3dfb-ab78-64be4174891a | -13.41063 | -47.5403 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f7e8a08d-f902-332b-9727-1ce86b62030f | -10.54104 | -47.8848 | 2025-10-01 12:00:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| f05badb5-71a1-38cc-ae74-d1cb8c4cfeef | -13.53597 | -47.26681 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 70bdb5fc-d700-3736-8b5c-597898b2c904 | -10.9045 | -44.27139 | 2025-10-01 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 04ea9a79-b820-3b14-a12f-20e303ca2e7c | -10.62069 | -48.59396 | 2025-10-01 12:00:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| f7f71ede-90b8-382f-bca7-c3e164dce782 | -13.58393 | -43.35334 | 2025-10-01 12:00:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 09f0cac0-838c-3938-bbb9-8ead5da6dfe9 | -9.4748 | -45.5564 | 2025-10-01 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fe16ab10-2d9c-32fd-8224-6bed0dac88e2 | -9.02262 | -46.69665 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| e03184e9-1487-347d-8f99-853f89f02b6f | -14.35867 | -45.91806 | 2025-10-01 12:00:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 29.5 |
| f6dd5403-8576-3cb8-9369-eb086777396b | -9.34933 | -41.16864 | 2025-10-01 12:00:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 23.8 |
| cbe658f3-e7cd-3463-9b6d-ffda0409252f | -8.58168 | -45.49511 | 2025-10-01 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 9747a5fb-7cf1-3ee5-8b49-bd2795643134 | -12.77043 | -50.53725 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 8151f19a-cfd7-3397-bfff-fcce210aac40 | -11.65231 | -45.32029 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 758828c1-dec1-3e84-b04d-7e9beb2d0a40 | -10.94249 | -46.55074 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 3e38e053-8ef7-3031-b9bd-f230a4932644 | -13.24385 | -40.83407 | 2025-10-01 12:00:00 | TERRA_M-T | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 35.9 |
| 5fd23c7d-5b37-3bd6-873c-404e52e4a386 | -11.84764 | -48.07795 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 24f8d9b2-71f5-3f3c-8fbe-21c7f6ce30e1 | -14.22228 | -41.25659 | 2025-10-01 12:00:00 | TERRA_M-T | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 84db78d7-0d5b-3a09-8828-02a71cf8f3ff | -11.81637 | -44.90474 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c20446d9-ec85-3c0b-9e2a-ace1773cba29 | -13.21541 | -47.33987 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ddadbdb8-6d26-32f1-8873-14c58e4c8209 | -8.48347 | -47.78494 | 2025-10-01 12:00:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 00600ec5-3458-3d65-9b47-95e6f28a5b08 | -11.7776 | -40.90558 | 2025-10-01 12:00:00 | TERRA_M-T | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 7a40c069-3307-3df0-ae02-8803f163f1bf | -12.88532 | -46.90921 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 80d03351-a6ed-3d79-a49a-1f82717ed495 | -11.57896 | -50.17845 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| f96678ef-a070-3bb1-b39e-73ee7124a42a | -13.67198 | -48.07119 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 27.1 |
| dbf889b9-e414-347b-8e78-88eb78c6ade9 | -13.382 | -42.4323 | 2025-10-01 12:00:00 | TERRA_M-T | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 060a4cec-8456-32d7-ab1e-3ac5aff28456 | -10.852 | -45.4104 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| a449fe3e-57a4-35e3-8384-6d9309d46822 | -12.47042 | -50.21088 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 67.4 |
| f31fb62e-dd23-3436-8c53-2a6e42b1153d | -12.77803 | -50.54579 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 824726fd-922c-3203-8bb4-d9ab1505ba7b | -13.37665 | -47.30742 | 2025-10-01 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3d5809db-60af-30c2-ae9a-37a299d2a6d3 | -8.53475 | -44.70409 | 2025-10-01 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 5250519f-86d7-380b-ab99-997f48d4b3d5 | -11.9383 | -47.06554 | 2025-10-01 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 7f6a7b29-545b-3429-b2e0-e62b5dccaa39 | -12.83533 | -47.028 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e34543f3-1953-3976-9fd5-06c06319a9e8 | -13.49398 | -42.68719 | 2025-10-01 12:00:00 | TERRA_M-T | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e8098e65-6e53-3673-bd20-f3a763b93c38 | -13.56671 | -47.27241 | 2025-10-01 12:00:00 | TERRA_M-T | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 41407f9f-90f6-332e-b82c-6f8f880f37de | -11.40116 | -41.7122 | 2025-10-01 12:00:00 | TERRA_M-T | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| ae8ad2a8-a09e-36fc-b3de-c26cb63ac6eb | -12.47598 | -50.24071 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 13909314-affd-352e-9d30-e5a69a0a6b3b | -13.31853 | -47.2247 | 2025-10-01 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 22.0 |
| d32e6465-2020-3f48-b300-62f5ffbd3949 | -12.78009 | -50.56211 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 7bd3f799-8045-35c1-9b9a-b844d623e304 | -8.6589 | -44.85054 | 2025-10-01 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 44.3 |
| d295d37d-1e0e-3151-835a-3f84d8f2d9bc | -11.17738 | -47.21255 | 2025-10-01 12:00:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| de17f3ba-22f7-3680-81cb-6df7c4b6cf09 | -14.17873 | -46.11665 | 2025-10-01 12:00:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 508ad072-1674-363f-9399-f3fb9ff2987d | -8.16719 | -46.2648 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 772c9d54-f990-31ab-8617-dc2b643c5d0f | -12.25123 | -47.79386 | 2025-10-01 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 8c6f415e-e699-3b02-b6b2-a3c0091c98e2 | -11.84648 | -45.00529 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 217162fa-b1ce-350d-ba84-efef1f47bfcb | -13.45713 | -47.24874 | 2025-10-01 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5f66ad75-9f7a-354c-9c71-e4c74c0ce27d | -11.814 | -44.98372 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 8ba67b88-eef5-318d-8600-30730b043327 | -12.28174 | -45.36705 | 2025-10-01 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 646ac4f5-5b86-3ba5-9658-47822d43e5b9 | -14.18655 | -46.12885 | 2025-10-01 12:00:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 9a7a45fc-41b8-37dc-9c6c-348392263099 | -11.923 | -47.89233 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 6afcbf7a-9a61-3e5c-b01b-931614bb3d60 | -11.85009 | -48.06281 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 2781bf68-7654-3974-bc76-662ac6ff7244 | -10.9175 | -44.30812 | 2025-10-01 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1c92bce9-68e4-39b5-804b-56063625c3cd | -13.31216 | -47.19799 | 2025-10-01 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 85c0e14a-ea3f-362b-9042-84baf3397314 | -11.47112 | -44.9836 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 47eb8751-253b-3dbd-bd56-4d31b6d93c79 | -9.92297 | -43.67147 | 2025-10-01 12:00:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| cea16009-8664-3782-8698-5e3407a58a65 | -18.49918 | -44.03435 | 2025-10-01 12:00:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8103511b-bac5-308d-9b00-7edf77b4287d | -15.31343 | -46.41383 | 2025-10-01 12:00:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3db512b6-10bd-3d06-b848-23091c18b0b4 | -14.6326 | -46.82187 | 2025-10-01 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 1a54f51c-fc7e-3632-b512-9105ccc3fb93 | -15.28133 | -46.40234 | 2025-10-01 12:00:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a99c0687-85a3-3739-812e-2d5c7b6ecfa6 | -14.74945 | -45.77676 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d80b762c-82f3-3b10-aa55-eded6647c370 | -18.66162 | -43.66717 | 2025-10-01 12:00:00 | TERRA_M-T | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 11a4a25c-c033-32be-8b10-07c66e9c4895 | -18.22083 | -43.39005 | 2025-10-01 12:00:00 | TERRA_M-T | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2c9db125-4cb7-31b1-aa00-4169762acee2 | -15.26147 | -47.88839 | 2025-10-01 12:00:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 04234cd0-bcc1-3701-9169-f524a86d21a9 | -15.36223 | -47.07277 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 447ea2a7-6355-3caa-9c5a-4dd83614f31c | -15.36832 | -44.15619 | 2025-10-01 12:00:00 | TERRA_M-T | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 79d4d770-52fa-30ef-b81a-a5699a72ffa9 | -17.4118 | -47.16534 | 2025-10-01 12:00:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0ef8bc77-2ed3-3bc1-806a-3b91020145a9 | -15.53474 | -45.21359 | 2025-10-01 12:00:00 | TERRA_M-T | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d0fc13fb-71fb-364a-bb46-9b00fe77d2d9 | -14.97323 | -46.87707 | 2025-10-01 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 27.1 |
| a2120bf8-3fec-35b5-98f9-147c4f874d03 | -14.05488 | -47.98901 | 2025-10-01 12:00:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 7bd50f1d-e0e5-3650-9400-50eff635164c | -15.72472 | -41.78247 | 2025-10-01 12:00:00 | TERRA_M-T | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 8f6ff261-8826-309c-b24f-4f764f7c3ee0 | -17.40387 | -47.15311 | 2025-10-01 12:00:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fdcf3b14-17c7-3bd0-b1ed-c0f3aa7fab97 | -15.71927 | -43.30498 | 2025-10-01 12:00:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1378ecf3-9143-357f-840c-5234dd72301f | -14.80503 | -44.47274 | 2025-10-01 12:00:00 | TERRA_M-T | MIRAVÂNIA | MINAS GERAIS | Brasil | 3142254 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 00493743-f349-34be-a6b6-dedcb0f1b494 | -18.60516 | -43.27302 | 2025-10-01 12:00:00 | TERRA_M-T | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 29ab4cd5-2771-3ba8-9461-85b4bcdf53c9 | -17.38223 | -47.14362 | 2025-10-01 12:00:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6326ef3d-becb-3a77-af66-18e96679408f | -15.94017 | -43.30266 | 2025-10-01 12:00:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 86.3 |
| bec84680-a8b5-30c2-9869-bb7301f93bdf | -14.60682 | -47.30574 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4ec66508-733e-39e1-8499-689d18aa493e | -14.96963 | -46.89973 | 2025-10-01 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |


[Clique aqui para ver as próximas entradas](README146.md)
