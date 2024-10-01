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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ef5e70a-ac77-31b4-8766-4a8dd74aa0c5 | -12.06589 | -44.9591 | 2024-10-01 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64982d3d-cf2e-3647-9a66-4d30c87372ea | -11.26303 | -45.64901 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adf21874-7553-3cf1-a602-4de8c59120d9 | -11.26202 | -45.65448 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b653460c-24d7-3d11-beac-be36ff43cbf2 | -11.26101 | -45.65999 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 16227125-63dc-34fb-96c0-7bdeb9c4a9aa | -11.25999 | -45.66556 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a4387c9f-3378-33fe-be46-264fb62aeaaf | -11.25938 | -43.38176 | 2024-10-01 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb897b9d-c15d-390d-9d31-d449c2e52fb9 | -11.25895 | -45.67122 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dbd1e43b-e0a9-3786-8d7d-dd4dcb0db892 | -11.25871 | -43.38561 | 2024-10-01 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb82a99f-4b29-3f7d-a059-ca9eb3c139f6 | -11.25715 | -45.65376 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dcd2417-70f0-36e5-b022-486ce81ff4f4 | -11.25522 | -43.38099 | 2024-10-01 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b58f4151-3e8b-3fdd-8e1a-f7d19c8c2e29 | -11.25455 | -43.38484 | 2024-10-01 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7df2f10a-f176-3783-a03d-643961e80098 | -11.25387 | -43.3887 | 2024-10-01 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 2c17fae3-2c19-3921-b9ab-f74c28fd5786 | -11.2532 | -43.39256 | 2024-10-01 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| eb8ae773-5adc-389a-afa5-065ada14304f | -11.25106 | -43.38022 | 2024-10-01 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e966277-3a50-326a-81fa-acd4926595bf | -11.25038 | -43.38408 | 2024-10-01 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36246177-a519-3b42-b4d8-aa7caaf287f5 | -11.24971 | -43.38793 | 2024-10-01 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 9e6596ba-1cdb-30d0-8f5b-f821d3b67b05 | -11.24903 | -43.3918 | 2024-10-01 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 311956f8-988d-3249-8069-35c282364f76 | -11.24554 | -43.38717 | 2024-10-01 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1d6d6fe-ca2d-30c1-b5d4-1a1c0b245f7c | -11.18955 | -45.73454 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62ec1f40-f550-33f6-abb6-f944f9935f0d | -11.16221 | -45.74619 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92299a7c-9840-3652-9a6f-f62f9563d5e9 | -11.14401 | -45.68055 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 302469c9-f1d5-3334-89c5-a51867b035d9 | -11.13915 | -45.67962 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 99f2d425-39d3-3c01-a369-0bda4fceb85a | -11.13815 | -45.68502 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5b431370-7ba5-3e09-870d-86aa4aa6da5b | -11.12475 | -45.64884 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6adf3745-d9ec-3ffc-b597-d9f9af734d37 | -11.12389 | -45.62646 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88871aea-6479-33da-8fb8-017d9eb13f8a | -11.1229 | -45.63178 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1b8c37c-eea5-348b-82dc-6b4285daf6d0 | -11.12191 | -45.63712 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e4688485-93db-3db8-9ff5-1a3afd8fd667 | -11.11991 | -45.64787 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ecad2417-2b05-348f-8b01-d790f7bbc5a9 | -11.11891 | -45.65326 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0e0e3930-c80d-33b5-b126-e9f23bbc455c | -11.11807 | -45.63081 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c612e1fa-aaa4-3f4b-a568-a08002ddea5a | -11.11707 | -45.63614 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fb0ef291-d18d-3235-914e-8124bb046f56 | -11.11406 | -45.65229 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4918cd2e-c3dd-3d50-bc1e-81a346b0a367 | -11.11384 | -45.68045 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 712b7d28-1c9e-342e-8e65-f34bd32b11f7 | -11.10896 | -45.67963 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8fb2ecbc-bc32-3462-8aed-989b569da575 | -11.10794 | -45.68512 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fef7699a-54ce-3a9c-a18b-57ddf0f40302 | -11.10615 | -45.66778 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| daff1859-d45b-3e0c-b4c5-d6b1de947ee6 | -11.10511 | -45.67331 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6e6cfe02-0179-393b-a4a2-b36773c5ed7a | -11.10421 | -45.66661 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5a4aa1d-7258-387a-84b1-0ba36df17c07 | -11.10321 | -45.67218 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 01cee703-3812-3853-b6bc-f165a801801c | -11.10128 | -45.66694 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c2e6935a-a709-334e-b9d3-07c863fdfa0b | -11.10023 | -45.67252 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7f04a55b-d665-3d53-93de-853c6ae1621e | -11.09833 | -45.67138 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8a7c9659-3aaf-3aba-ba5e-43a6e4ef5872 | -11.09745 | -45.66055 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8718b0c-67bf-32d8-8b7b-03b3b69d6f69 | -10.8736 | -44.79312 | 2024-10-01 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6f13c73-6eb0-33d5-9c10-51e22f9c7d70 | -10.87275 | -44.79787 | 2024-10-01 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfdd4f20-b8bb-3633-89b8-fb6cd93bfc04 | -10.87188 | -44.80265 | 2024-10-01 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9ddad9d-7c69-31f3-9e50-1fa84472630e | -10.87102 | -44.80745 | 2024-10-01 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f794d4cf-b0d3-3938-b23e-6327918d2300 | -10.86728 | -44.8018 | 2024-10-01 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2028efa8-bb32-3c68-a4c3-1eb7a73f1187 | -10.86641 | -44.80659 | 2024-10-01 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11fe812f-8e11-3741-9cbc-be52f8da3812 | -10.86354 | -44.79616 | 2024-10-01 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b49e429-1f3e-33e2-96e1-6cadd3b88ba5 | -10.85894 | -44.79533 | 2024-10-01 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 852dde5a-14ab-3f68-a533-c61bb293a92c | -6.72031 | -43.56351 | 2024-10-01 03:49:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eee04288-6501-398c-b195-4a260bf871fe | -6.50654 | -43.63242 | 2024-10-01 03:49:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6663ce0-5d2f-3737-b6f6-6bfafc9e7fa6 | -6.50197 | -43.63158 | 2024-10-01 03:49:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c20d7dc-8f4d-3c9b-ad0f-075d4edecea9 | -6.34895 | -43.91976 | 2024-10-01 03:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a478c3fe-4ce6-36a7-a014-2cf602e91f5b | -6.32795 | -43.47188 | 2024-10-01 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f2ddb87-abbe-301c-a6b1-56bc0eb77411 | -5.96854 | -43.62652 | 2024-10-01 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9db2acb8-2d1e-3daa-9974-5165369eeb60 | -5.88768 | -43.71866 | 2024-10-01 03:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec3f06ab-0598-3487-a907-a7e5d4f9c808 | -5.88685 | -43.72356 | 2024-10-01 03:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5ee56008-33ba-3677-a884-f1e68cc7e935 | -5.88303 | -43.71785 | 2024-10-01 03:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28a0c1b3-7c84-30ee-a274-6909233d5974 | -13.00399 | -45.45418 | 2024-10-01 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfff63e9-7a1f-3bd0-af17-90b34db45166 | -11.14719 | -45.97154 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc0d4438-0bde-3d5a-8cde-1a10d9f1f78d | -11.14696 | -45.97026 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30e92d34-f6fc-3841-9653-f785379c075b | -11.14614 | -45.97709 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 29ead0a6-e2db-341a-aef2-e668501ef84c | -11.14595 | -45.97583 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f24bace-3a4c-3771-8be7-2cb99276c08c | -11.14115 | -45.97633 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a6c8319-d8c7-328a-85b6-4de95931458c | -11.14007 | -45.98203 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 339b1d63-ce84-3436-90e9-0c6f3cdb4cc2 | -11.13994 | -45.98071 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9ed6a760-4ad9-3bff-92f4-83185669ead3 | -10.87387 | -45.97422 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bb042b9-808c-366e-81ee-4082078dce91 | -10.86889 | -45.97327 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e51b01b-d443-3a6d-8598-1a5de57233ac | -10.70353 | -46.17145 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdff7e1b-2e4d-32da-bfba-5f3e8432c2af | -10.69901 | -46.16756 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baa4c806-8ff4-38c7-a249-eb62b875ee01 | -10.69848 | -46.1704 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82446d0e-b9b4-31d9-bdbc-97f387cca620 | -10.69398 | -46.16645 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 714ef756-4abe-3a79-a46e-3702c1a0359c | -10.6895 | -46.16246 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 28184323-afbc-3009-a0ac-d2577feddb42 | -10.68499 | -46.15856 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c3ce04a-12ad-3e2b-b549-520dc40d340a | -10.68445 | -46.16145 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3a771d5-06b1-3aed-a40d-a49366212bb3 | -10.68191 | -46.15709 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e61b6454-00d5-355b-996b-c1d3d52f78f6 | -10.68138 | -46.15998 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9172f34a-9225-3713-8606-4ace35733bdb | -10.68048 | -46.15473 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b9f7fe5-d4ea-399d-878c-41442d61757d | -10.67994 | -46.15761 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 294ae59d-8253-3309-96cf-7259fd183781 | -10.67737 | -46.15325 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1886937-bd78-3ce3-91e8-7649245b4cb5 | -10.67684 | -46.15614 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ea23745-70d5-3dec-a903-1dd66a73ba21 | -10.67632 | -46.15903 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba496deb-5529-34cb-b3b8-ff3882b9f005 | -10.67542 | -46.1538 | 2024-10-01 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb704765-4957-3cd6-9076-eca9a04cf905 | -18.18913 | -43.82008 | 2024-10-01 03:49:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cfd8d3f-2b3c-3d86-9301-267861cfa3d5 | -17.78785 | -43.31345 | 2024-10-01 03:49:00 | NPP-375D | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1062c708-0dbb-3f83-9868-ed6af17aa318 | -17.78586 | -42.89102 | 2024-10-01 03:49:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afe1afa3-8cf8-3f18-b556-a4dad1fb8241 | -17.72358 | -42.34728 | 2024-10-01 03:49:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b89d666c-539c-31b4-9a27-dca5271f8897 | -17.72286 | -42.35147 | 2024-10-01 03:49:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfc5b7e7-7e4f-31bb-8d56-e4e909995f01 | -17.63529 | -42.33619 | 2024-10-01 03:49:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c83881f-6db9-38bf-ae53-8cd3dd20949c | -17.63022 | -42.99619 | 2024-10-01 03:49:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1d3d842-86b5-32b2-a22a-c053293b4d89 | -17.35734 | -44.91697 | 2024-10-01 03:49:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26202610-4df6-340a-9be3-322e538a7cfc | -17.28345 | -43.18509 | 2024-10-01 03:49:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61324916-881d-3683-93fa-8f6b0c271612 | -17.28325 | -43.18749 | 2024-10-01 03:49:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d46dfa1d-740b-3c2c-80a1-ea962a7e9a07 | -17.28242 | -43.19211 | 2024-10-01 03:49:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cbf45e6-a634-39d4-bdb4-cecd33405f5a | -17.28183 | -43.19437 | 2024-10-01 03:49:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e446dd90-62c2-3c37-aeb7-d05bff3f259b | -17.28158 | -43.19679 | 2024-10-01 03:49:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3b163f9-74e9-3874-812b-588ed9800d2a | -17.25811 | -43.17495 | 2024-10-01 03:49:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37e964ef-fe43-33ce-b1ef-81c7e24df3a0 | -17.25444 | -43.21799 | 2024-10-01 03:49:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README46.md)
