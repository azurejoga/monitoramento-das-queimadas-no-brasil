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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5253fa36-02ef-31d1-a84b-d660b3c97d66 | -6.91864 | -43.53872 | 2024-12-01 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 098b6b64-4970-30f0-b836-95e8f9b0e1bf | -3.66631 | -51.72509 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca62fc2e-2c50-37b7-9bbf-d77f45b0a2d7 | -3.77359 | -51.61631 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ea4cd92-f529-321a-a9c9-89a59e35c7ba | -3.69073 | -51.81242 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 521bbef9-d405-3543-8e79-f6131de8c497 | -3.65131 | -51.96077 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 968b61a3-ba58-3ffa-9d79-dcfced4ecbe9 | -3.82421 | -52.25048 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97815744-869f-3ce3-9f6f-6cb14f6c1092 | -3.72211 | -54.5247 | 2024-12-01 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 562b244a-558f-3caa-8a82-e2fe093ee64c | -4.11472 | -48.53568 | 2024-12-01 04:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1378918-7e03-3c0d-be51-1dc25a4a6882 | -5.48739 | -46.34685 | 2024-12-01 04:23:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e56a434-f9cb-3200-989a-45cd4cb565c4 | -5.1119 | -50.61668 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95546ca7-2701-3e56-8bee-1becaf952df6 | -5.76675 | -43.84309 | 2024-12-01 04:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe6233c0-2d7b-3bed-888f-57d65d3b9ca6 | -10.6542 | -44.50146 | 2024-12-01 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8872412-cc3c-38f1-ab06-0ffda5a35c71 | -4.11548 | -48.53104 | 2024-12-01 04:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d1efcf6-8833-3eca-ba4e-b39ea3b4501f | -5.66184 | -45.86483 | 2024-12-01 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1f30a79-aa3d-39dd-b016-0255df473f2b | -3.13517 | -54.52856 | 2024-12-01 04:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| e1b71f53-9792-30ec-b78e-a15d8d82cfef | -3.25194 | -53.63141 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 07dcd2eb-4e9e-3d0a-9bf6-eb1bd837d7eb | -3.17977 | -54.33237 | 2024-12-01 04:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cada7cce-d319-379e-8864-2d7ad67941f6 | -3.33442 | -53.37023 | 2024-12-01 04:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bdb85775-37be-3d17-a0b1-ff3c8dc404b9 | -4.18798 | -47.98886 | 2024-12-01 04:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 812c30d7-1b81-3268-8109-beda4b6985bb | -4.76797 | -49.49777 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb7b1ba9-1f21-330f-8e8d-2868efc6eb89 | -3.50503 | -53.84134 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f8848533-997a-3829-8c6a-c5bbcba65a9b | -3.70779 | -51.68013 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ee10fac-3d8e-3d80-a49b-60c071613589 | -4.25319 | -50.84024 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ad6083a-a904-3a63-a808-c03729dad669 | -7.02858 | -44.84868 | 2024-12-01 04:23:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4ace8eb-7694-39a1-9bad-65c2eb59734a | -3.40691 | -53.03039 | 2024-12-01 04:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e02a8b08-f65e-3bfa-a9b8-e017c7f0b4f7 | -3.21933 | -54.23444 | 2024-12-01 04:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70bf2555-7147-3400-9d53-c702a858b904 | -3.28343 | -53.34825 | 2024-12-01 04:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0439faf-ed49-3c0f-892d-8ac7bcfe8d44 | -3.88372 | -51.41465 | 2024-12-01 04:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8fc7ee0-603a-37a8-b792-2c9d9c59c36f | -3.24836 | -53.92091 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a54440d5-36d2-350f-947d-ececa9d5d783 | -3.80505 | -51.00875 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aeafab06-b44a-304e-93f8-ebfbffb3ec96 | -6.7101 | -44.71001 | 2024-12-01 04:23:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c3502a8-6f5c-3dec-8e78-e18ad916926b | -3.26283 | -53.63292 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ba9d9f7b-5814-3d7c-bf63-28a9c81bc63d | -6.18983 | -44.42664 | 2024-12-01 04:23:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a7f7300-2b65-3ed0-9918-51b85546ebc1 | -3.74071 | -51.83857 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03895f6a-69cc-3d8d-80c8-939c5d69d9fa | -3.69158 | -51.80725 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7059ad6a-b15e-33fa-9569-362d98af3da1 | -3.12939 | -54.52768 | 2024-12-01 04:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 410fddf3-000b-35bc-a0aa-858cc5af7063 | -6.30721 | -43.84401 | 2024-12-01 04:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74aa8df3-3222-311b-a315-ad6a246e049b | -6.19314 | -44.42715 | 2024-12-01 04:23:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79cca4fd-3b04-3239-8ab4-b9850a806103 | -10.65475 | -44.49783 | 2024-12-01 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7b349760-00a6-3df3-8221-dd6b3c845e69 | -4.55523 | -45.71902 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0616a2f0-5932-30c7-a000-102921f80697 | -3.24477 | -53.64084 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6018dec9-6372-31e5-9d12-8e57e90d55be | -3.26342 | -53.62945 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| add099ed-e4a3-37ce-b773-a0d8b5da3f00 | -3.77744 | -51.62203 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d96596c-ffdc-318d-9e41-d3d4811e26df | -3.86868 | -51.01452 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bc2dbcc-eec8-3714-b4ca-ad1adb671ed3 | -3.25739 | -53.63212 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| edf027c4-e045-3333-869d-a14baf8eb713 | -3.42875 | -53.89249 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da818b6e-17f5-3aa8-9c17-ebae49ee1b3a | -6.92202 | -43.53923 | 2024-12-01 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 35b85bfb-f2de-3a8b-9c8b-7c3e13cec99c | -7.86438 | -45.91966 | 2024-12-01 04:23:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c05c984-6a87-3e74-8b29-0cc08539b9f6 | -5.57814 | -43.6118 | 2024-12-01 04:23:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7053c95d-2134-354b-9140-fbbf06afb15a | -3.71511 | -51.06519 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56cb8f55-57e9-368d-aa29-093874a34de0 | -4.61768 | -46.47482 | 2024-12-01 04:23:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96977f7e-23d8-3c73-b139-66233e1dd726 | -3.96168 | -49.90672 | 2024-12-01 04:23:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ca677d9-2299-3704-b831-5a1bb782fd6e | -4.72114 | -45.68353 | 2024-12-01 04:23:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bce098a-396a-3075-8a8f-2563138077a9 | -10.66203 | -44.49524 | 2024-12-01 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9934d093-d3ff-30ee-9764-c8e2f7a01a05 | -3.71888 | -51.0705 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf7dff4a-3128-38ad-bd71-68711cc565d9 | -3.72722 | -51.10484 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90423c2a-9da4-36b7-8601-8f4020615402 | -6.92711 | -43.53955 | 2024-12-01 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b88a1174-56b9-3ccc-bf1c-a7df3c8eebf8 | -7.38144 | -45.83215 | 2024-12-01 04:23:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c16a594a-f544-3ed2-b993-17bc4bcab31d | -3.89809 | -52.16711 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 672c6fa2-7726-39c9-8765-f69c23654d19 | -3.29723 | -53.83076 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 035d0eb7-2eed-312a-b66a-a10d9158f9e8 | -3.75443 | -51.78096 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c20dd853-9329-3c6a-8350-ed5d140cb6d4 | -3.21997 | -54.23056 | 2024-12-01 04:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee0a4224-d730-30f1-9061-6d077410e9f8 | -3.21134 | -54.1778 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11865003-219e-32ef-9084-a2818685439a | -3.50626 | -53.83389 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ea1f29d9-4107-3907-85d3-f5e26b60d908 | -4.54741 | -45.72508 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fe11ae9-42f8-322d-9fb9-21ddae932f52 | -7.78996 | -38.47231 | 2024-12-01 04:23:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 46a0dd3d-9c19-3282-a464-f94315c1eeae | -7.02912 | -44.84522 | 2024-12-01 04:23:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02b3628a-f3e2-39d6-9af3-595e51bcbaff | -6.14992 | -37.77835 | 2024-12-01 04:23:00 | NOAA-21 | ALMINO AFONSO | RIO GRANDE DO NORTE | Brasil | 2400604 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 46a78b37-2714-3d3c-9157-7bdc169a0cf2 | -6.26132 | -43.16381 | 2024-12-01 04:23:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 309c6d26-4ddd-3f01-8fe3-e2f55d20df86 | -5.73509 | -43.98152 | 2024-12-01 04:23:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d2abebe9-033d-36f5-bb86-10bf9b08ea5e | -5.53609 | -45.43159 | 2024-12-01 04:23:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 356e9001-e28d-336b-8e7d-2fea4a5c1af0 | -6.29331 | -43.84552 | 2024-12-01 04:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b0afb406-9e35-3456-aa86-aa5a53cec397 | -7.69045 | -47.73726 | 2024-12-01 04:23:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2c99cbe-e0e4-3117-acd1-8b5a77221713 | -4.84563 | -44.47731 | 2024-12-01 04:23:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36e6e11e-dfc2-3ab0-8812-0d60acd7dae8 | -3.6404 | -54.44315 | 2024-12-01 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61fad4e2-e420-3888-8aab-0d92bc109610 | -3.8193 | -52.24977 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3c636de8-87bb-3e2d-a737-e0f09f887b24 | -4.44696 | -46.35675 | 2024-12-01 04:23:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c43434b5-26ad-323f-b44d-9e828823ff8d | -6.92258 | -43.53561 | 2024-12-01 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b933f212-879d-3bc6-8083-10a168344ca5 | -3.72268 | -51.10414 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8742db18-0ea1-3a9c-9e47-2050b994ff2c | -3.19183 | -54.33018 | 2024-12-01 04:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e7f29307-cfaa-3ee7-b5d5-167726749c5d | -6.92939 | -43.5473 | 2024-12-01 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5560762c-8ad8-36d9-8f9b-b64be5630963 | -7.95145 | -44.88442 | 2024-12-01 04:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e5a13d1-0eb3-31d9-8306-f59221cd3aed | -6.92601 | -43.54678 | 2024-12-01 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8e77831e-b847-3095-80af-3321dd7ce566 | -4.07969 | -50.03051 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b108abab-8866-31b0-a811-6db58b6ffe06 | -4.93528 | -45.72782 | 2024-12-01 04:23:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad199bce-10e2-3ff6-9f4f-8ef634b42fab | -5.75081 | -44.27589 | 2024-12-01 04:23:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fbd7d77-e310-3ae4-8820-a90182c85ab6 | -3.86076 | -50.53804 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72ede25d-e34d-3215-8d53-d3e9081bcf3e | -3.96584 | -49.90738 | 2024-12-01 04:23:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db20fecb-84c1-3bc9-b6a8-67c8ed131043 | -5.20797 | -46.09172 | 2024-12-01 04:23:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e3e37e5-5b21-33ac-8d41-448de3e8471a | -5.8971 | -48.27592 | 2024-12-01 04:23:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c25cd87-325b-3b6d-a513-a78833701bf0 | -5.42203 | -45.11896 | 2024-12-01 04:23:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64527443-68ae-3d9b-a46f-b07d2718c38f | -4.19328 | -50.68334 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0214b8de-668e-3493-b6fa-d4fd74d3328f | -3.48803 | -53.80824 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 898365de-d770-3b43-9ad0-969adf90d313 | -3.31449 | -53.86476 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3ff03be5-1e18-3afe-98e1-78e7ee7cd80c | -3.49474 | -53.80166 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c5221ef-9d5e-3b0d-9361-6dcf56330adb | -12.93156 | -48.62929 | 2024-12-01 04:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9048fcd0-bab1-3fe9-815a-05bef25acb9f | -21.09401 | -51.58579 | 2024-12-01 04:25:00 | NOAA-21 | NOVA INDEPENDÊNCIA | SÃO PAULO | Brasil | 3533205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0524441c-fdad-3683-bc97-cdf1ee9e0300 | -21.41743 | -45.99233 | 2024-12-01 04:25:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c3cd3ad0-d193-3709-b4b3-37c08d49e7ca | -21.37437 | -47.23308 | 2024-12-01 04:25:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9ff96f36-5f11-360a-9ae6-38d1fe677054 | -12.77427 | -45.0134 | 2024-12-01 04:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README39.md)
