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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06268392-c729-3464-8e9a-eed8a4e268cf | -11.64752 | -43.54332 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 9892f796-24f8-362d-83d7-39caddc301c1 | -11.15397 | -44.61193 | 2026-10-02 11:45:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 194fe0fc-92b6-3b90-aa37-0ff2ff869348 | -13.54015 | -49.15361 | 2026-10-02 11:45:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4b4007a0-8901-330d-aac2-6c32fd480ccb | -11.66036 | -43.61665 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| b6e4092a-d068-354d-a83d-476ed34610e9 | -16.99104 | -45.46784 | 2026-10-02 11:45:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 3203b593-1923-341a-a547-2587eeca88ae | -11.73104 | -43.42924 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 77da5047-0d63-3c50-9f2f-2bac1c7462aa | -11.25234 | -44.2577 | 2026-10-02 11:45:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 73b78a3f-2693-3e8b-9ae6-69e4995302ba | -13.48887 | -48.60672 | 2026-10-02 11:45:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2819a374-10e1-32da-870a-f6cfae245535 | -11.16398 | -44.6132 | 2026-10-02 11:45:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 266.2 |
| c1174b05-b067-3a8d-89b1-84dd98085308 | -11.6947 | -43.60691 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| a53ccbb6-78c9-38c7-a964-37b07637c7a4 | -11.13701 | -44.58573 | 2026-10-02 11:45:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9a3d3013-9bbb-36f5-992d-9dd9d87d8acc | -11.75701 | -43.57781 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 00548c63-41b0-3c2b-a2d6-c245c31f7985 | -11.73527 | -43.57467 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| c2bf215e-7f34-3462-abd3-289041cbdec8 | -11.46828 | -43.4217 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 01b111a2-c86c-3099-8def-cf9a8e2be25b | -11.24938 | -45.20828 | 2026-10-02 11:45:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| e3b82e2f-084b-395d-aa4e-dbe0f2c1cb94 | -13.96842 | -41.4962 | 2026-10-02 11:45:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 25.7 |
| a3aed772-52fb-3fbb-ae11-5948b981065d | -12.18784 | -48.42125 | 2026-10-02 11:45:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 853657a8-40f6-3f92-9205-c5d301d3afe7 | -11.70779 | -43.52797 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| afda4713-35dc-31f1-883b-496e140f0435 | -12.32731 | -46.37148 | 2026-10-02 11:45:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4a4ed922-f217-3a31-b217-b767cbaafdb6 | -11.70757 | -43.50772 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| a7e243fc-aac5-3bbe-b1ab-0bd271632460 | -11.73705 | -43.56046 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 84814ae6-de04-30c1-9452-7935cdac92aa | -11.44476 | -43.41217 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 9cd3ac7f-0016-3760-845d-a6deae6da247 | -11.70742 | -43.5941 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 398f68a0-af41-3e4c-a98d-648353d86b45 | -11.24263 | -45.18505 | 2026-10-02 11:45:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| eb57b160-c96c-343b-bad1-4c9f03fc3e79 | -11.37072 | -42.27299 | 2026-10-02 11:45:00 | TERRA_M-M | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 259e73c5-67c1-3f2a-af1f-dd1f83942dd2 | -12.86173 | -43.80597 | 2026-10-02 11:45:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 1e6d030f-ea3c-30d8-8503-1b3f7fd5edd1 | -11.79356 | -43.57551 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 641d0358-8cf8-39c9-903b-1c9e83db1054 | -11.71349 | -43.57182 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| aab872e2-d955-39c0-a7f2-781b5e634ccf | -11.41363 | -43.39369 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| dbcacb40-6d2c-30c4-9f2e-f4ccc3888542 | -11.25266 | -44.23856 | 2026-10-02 11:45:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 6b57fb76-958c-33c1-bbb6-4b6ef425a4c2 | -14.63475 | -43.64084 | 2026-10-02 11:45:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| fa768454-6de7-3df9-82f6-bb6c0bb251f1 | -11.70953 | -43.51375 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| b6c05b55-6e1d-365f-9a74-2f74d4657520 | -11.79536 | -43.56077 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| a2cbe3d0-c4d2-3b41-aa0e-a589ea92b43e | -11.74614 | -43.57623 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| ed15bedf-a653-36ee-af2f-b38b5a97bb8a | -12.01359 | -43.26839 | 2026-10-02 11:45:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6b7105f1-3e23-32b2-9012-81bb503541e8 | -11.45761 | -43.39927 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 7c61408c-557e-3741-8c16-808677dce645 | -10.26173 | -49.65669 | 2026-10-02 11:45:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 61fdbf95-69a5-3f5f-819f-7345cf19c729 | -13.78814 | -45.23946 | 2026-10-02 11:45:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 7fb7c5cf-9ce8-3c70-81dd-181653799559 | -11.66217 | -43.60241 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 22a4aff7-9d96-3b5b-81b6-83d9302e77e0 | -12.19665 | -48.42253 | 2026-10-02 11:45:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| c919af5c-ea9f-3044-9e6c-8e74b0758a72 | -11.25109 | -44.25096 | 2026-10-02 11:45:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 7bd79298-6c13-3128-ab33-c8efb3096380 | -13.33837 | -43.85984 | 2026-10-02 11:45:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| fb6f1472-7bf0-3a4a-a159-3921c9e18b53 | -11.16245 | -44.62485 | 2026-10-02 11:45:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 34a01482-453f-34cc-9e32-5c459743f647 | -11.76229 | -43.44792 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 6cc5e5b5-c3cd-3e74-b69c-eedc3a893a02 | -12.78182 | -45.19595 | 2026-10-02 11:45:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| dd40dcea-e619-3911-81a7-64e1306e8db2 | -11.25084 | -45.19725 | 2026-10-02 11:45:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| b79edce0-11f3-3f3a-a9d2-786e44ed9968 | -11.26256 | -43.51224 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 6114207e-9b5b-38f1-b33c-9fe28cd9ed16 | -12.85992 | -43.8201 | 2026-10-02 11:45:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 84408ac5-d078-3b2a-bdf8-390c7a021fd9 | -13.80802 | -45.2422 | 2026-10-02 11:45:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| e2675eb8-8fd6-329d-870f-b2bc2b1808eb | -13.49145 | -48.5887 | 2026-10-02 11:45:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 02ce63d6-84c1-3d42-a323-4dcab1fc60e3 | -11.27007 | -44.26601 | 2026-10-02 11:45:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 48b034b4-bdd2-31b3-a07a-7ef3becb27d5 | -13.79661 | -45.25249 | 2026-10-02 11:45:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d0733496-e3c2-33ba-819c-57691a574097 | -14.63596 | -43.63511 | 2026-10-02 11:45:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| bf4d32a9-dfdd-32c5-8c3f-fcd22dd936cd | -11.15244 | -44.6236 | 2026-10-02 11:45:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 997800b3-7117-36cc-9af3-81a82f3dab4f | -11.80236 | -43.56977 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 6a9a7c4e-717f-3043-9f8d-3b42dc834397 | -12.86398 | -43.81275 | 2026-10-02 11:45:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 737713e0-d583-391a-b8d3-c01768dce8ea | -11.26295 | -44.23989 | 2026-10-02 11:45:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 716422b9-17ac-3fd5-bea8-549adc5acbd4 | -11.79143 | -43.56856 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| ee69b2c8-8c0e-3c75-a905-d798c3dd26b6 | -11.70573 | -43.52192 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| c9675d2d-e472-34b0-8431-48ddb0efbba0 | -11.42279 | -43.40939 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| b3b4cfe8-542c-34ae-87c7-bb8d93e542cc | -11.43377 | -43.4108 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| e74ada73-6779-398d-aecf-32781f55f8a0 | -11.45574 | -43.41358 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 205.9 |
| 80bc7481-57dc-3ed5-8552-76fe139a567b | -12.82821 | -44.448 | 2026-10-02 11:45:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e4ba08dd-769e-3f6d-8b10-5f6bddf16668 | -14.89347 | -44.804 | 2026-10-02 11:45:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 6b458914-5516-37ef-98b5-b9b09f81d658 | -19.23151 | -44.60144 | 2026-10-02 11:45:00 | TERRA_M-M | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 975444d9-cf90-36e7-8952-65454dd1b50e | -11.41181 | -43.40803 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| fafca282-2075-3bb8-a65f-eafdf3e862f8 | -15.24288 | -47.06881 | 2026-10-02 11:45:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8d0b0b20-8e0b-3813-af6f-c8759934d13a | -12.78291 | -45.20206 | 2026-10-02 11:45:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 6be13d11-94bb-348e-aa3d-5999a6da165a | -11.69738 | -43.6129 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 019c0231-4e0b-3a1d-bf92-43122d0a4760 | -10.46363 | -47.11438 | 2026-10-02 11:45:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 500a8d74-df2d-33c9-8427-5c274ab64d28 | -13.91511 | -48.91272 | 2026-10-02 11:45:00 | TERRA_M-M | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 66565dba-9e6a-36f0-82a4-56eb89f48c93 | -11.71172 | -43.58609 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 305.1 |
| 3e86eae2-3de4-3ab6-8fee-2473b67eb12e | -11.43562 | -43.39646 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 446.0 |
| 87b7a82c-43b2-313e-8a3d-5a22d18bd609 | -13.49016 | -48.59771 | 2026-10-02 11:45:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7e13f9f2-b573-3f02-b11e-92fc32286e7c | -10.90813 | -43.84121 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 6ff05275-4e4b-3b07-95b2-29157ab21d88 | -11.25831 | -43.51957 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| be62e02a-d1a6-38ed-875b-d3f7638d4efa | -11.25399 | -44.24534 | 2026-10-02 11:45:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 97a21578-2c81-3f0f-a05d-3769fe8b3a42 | -11.70928 | -43.57984 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 289.9 |
| 686b519c-f265-387b-8de5-8efe3fe4c9d2 | -11.2598 | -44.26465 | 2026-10-02 11:45:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9cd2be3b-11be-3420-a83b-8ee653278a77 | -15.47159 | -46.10941 | 2026-10-02 11:45:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 44047f6b-e0d8-3ac1-9b93-924b5feb53fb | -11.64575 | -43.55743 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 64375b73-f459-3a53-bb86-fff5d75d09b6 | -12.18655 | -48.43022 | 2026-10-02 11:45:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f4c03839-ab37-3161-83c2-61fb7061e61b | -11.69911 | -43.5988 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 798a4883-f8c9-3417-92c4-252a898de5f6 | -11.14549 | -44.59887 | 2026-10-02 11:45:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| c756d9cf-ef54-39eb-af6e-0ff599a5996c | -13.80654 | -45.25386 | 2026-10-02 11:45:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 288.3 |
| 76e50bd5-e73f-3007-9b5e-99d607356a0b | -11.27166 | -44.25361 | 2026-10-02 11:45:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 763d91c9-e437-3081-8407-2fecb93bdfc1 | -11.67301 | -43.60397 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| d359df83-3983-3366-8619-88568cefe34b | -11.27343 | -43.51362 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 7f13c822-7763-3973-91d1-8f71a733b91a | -13.78823 | -45.23314 | 2026-10-02 11:45:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cf063655-9372-38ee-b286-d5ac672085d4 | -11.45729 | -43.42034 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| c785af1b-1c53-3327-9e1f-ffd78c26f714 | -11.44661 | -43.39785 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 219.0 |
| 444dea94-ee1b-3523-96aa-2a59f79537d2 | -11.42463 | -43.39506 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 409a34cd-0672-343b-bcc2-2de956933eed | -11.45906 | -43.40603 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 1e14e15e-860d-3fcd-86cc-38ec42f20351 | -16.1509 | -43.48196 | 2026-10-02 11:45:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 34dddbc0-6a36-3385-819a-1836782bde39 | -11.26137 | -44.25229 | 2026-10-02 11:45:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 3ecd760c-0e43-355f-8abc-68a191c4ea64 | -13.7867 | -45.24475 | 2026-10-02 11:45:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 85dbb2c5-0c59-32ec-a420-b95722cd64d2 | -11.16552 | -44.60147 | 2026-10-02 11:45:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8ee69f7b-f9bb-3cd2-8c9e-cef65b7c818d | -15.47017 | -46.12026 | 2026-10-02 11:45:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a965abd1-3053-3650-8d6d-7217450efb0b | -11.72223 | -43.50093 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 14e9cafb-95d6-3596-a5a9-17a4e57a06ee | -11.44806 | -43.40461 | 2026-10-02 11:45:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 222.3 |


[Clique aqui para ver as próximas entradas](README84.md)
