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

## Dados Diários - Página 235

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d21440e-d13a-37c9-b938-74e2ce5803f5 | -5.38972 | -42.96114 | 2026-10-08 15:41:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 38a9a1f3-d885-3ae9-8ce3-02a981f010c6 | -5.70898 | -41.73066 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.0 |
| 428b37f8-ab5d-3810-90c8-8bc3234adf2b | -6.18159 | -44.1081 | 2026-10-08 15:41:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0e894c00-d53c-3c98-aba4-f1e187be4713 | -10.22758 | -40.04218 | 2026-10-08 15:41:00 | NOAA-21 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 12dfd20e-1ad3-3a31-afef-bd1597098080 | -10.59926 | -43.84178 | 2026-10-08 15:41:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7ab22c09-5a55-3917-8e40-ab61adf0642e | -6.04984 | -42.59108 | 2026-10-08 15:41:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 808654e1-dbc5-3717-a332-db510750d7a7 | -7.20502 | -46.52883 | 2026-10-08 15:41:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5cb8af8f-ac76-3b77-8c83-d69d1f01bab4 | -7.26233 | -43.50762 | 2026-10-08 15:41:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| eac93687-f26a-3a1b-af71-7a1cc9a2311a | -4.57885 | -38.94894 | 2026-10-08 15:41:00 | NOAA-21 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| a55f2484-fdca-3d28-b50f-da6f2dc94a7e | -10.11245 | -42.35633 | 2026-10-08 15:41:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| bb962813-28ff-3323-9a9c-00c0a883060e | -5.7169 | -41.64392 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| f05721aa-7332-3dee-8df0-9ac60a428f58 | -6.67423 | -45.37078 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 051b5279-26dc-3ab4-9935-aa06fafa1735 | -8.96608 | -45.13002 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f7980c20-a6fc-35aa-b479-f2dca1760d6e | -5.76338 | -42.07255 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 8f966575-ca85-3593-a536-cb201f7e0c82 | -11.09229 | -44.005 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| c6080e5e-f30b-3ca7-b2cf-dcc9474a6db7 | -5.76811 | -42.06886 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| e95c085f-bfdf-343d-a8f2-d60fc1b9afc3 | -5.76206 | -42.06334 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c0e83c3a-fc4e-3687-9abe-3dc5cba16ade | -5.72135 | -41.63767 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 36b313c2-7a0e-335d-8ae5-9c78ad75593f | -6.82862 | -39.55872 | 2026-10-08 15:41:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 48.6 |
| 81ce3984-9609-32ec-b998-1ca8e02559a3 | -8.68255 | -41.20489 | 2026-10-08 15:41:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 26.5 |
| c747a4b6-c991-3948-ab12-9d5a73bd110f | -6.72323 | -45.18292 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 7f5e63e2-948e-3538-8ad8-24cbc5c2b233 | -9.93477 | -43.57747 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| c07c8d73-afa9-3352-b5a9-5df62bcff556 | -5.76859 | -42.05715 | 2026-10-08 15:41:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 5556ca16-d97e-3129-974d-18815722987b | -9.7581 | -44.79482 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 396eac59-4e0e-307a-bd33-eb2a6119f630 | -10.60601 | -43.8456 | 2026-10-08 15:41:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 974f3fd1-eb75-3bed-8bba-a6673163078c | -4.49075 | -38.69044 | 2026-10-08 15:41:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 99fdd6a9-0b72-36e1-9cee-51c329d60483 | -5.71832 | -41.65276 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 4664db74-2108-3aac-94a8-67b6e4758fa6 | -11.08088 | -44.01649 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 19e6022c-f4fe-3398-92be-0753ad2db9ee | -6.94745 | -43.06973 | 2026-10-08 15:41:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| cf2751b5-90a4-3ee9-b876-ef6d49ad8552 | -10.56565 | -46.2926 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f87cddb5-9863-3a9c-b8e6-72461d20f346 | -8.57961 | -35.95998 | 2026-10-08 15:41:00 | NOAA-21 | CUPIRA | PERNAMBUCO | Brasil | 2605004 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 37adab3b-48bb-3ac9-8265-5dba5b4e6328 | -7.76155 | -39.41693 | 2026-10-08 15:41:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 63.4 |
| 0ae26e87-5e8d-3027-bfc5-5abbcdb77e1b | -5.8803 | -43.45803 | 2026-10-08 15:41:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a07d3525-4802-3a85-97ff-62c7df3e359d | -10.59935 | -43.84697 | 2026-10-08 15:41:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5f6212fb-b012-317e-895e-e76351288e28 | -5.70563 | -41.74306 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 25a5de5a-d55f-3175-b81f-77c3c47e003d | -6.68647 | -41.76908 | 2026-10-08 15:41:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 8eda33a7-6c0e-3a01-9c50-812a51ce1705 | -7.85892 | -44.96027 | 2026-10-08 15:41:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1c88ee68-a046-36b5-b505-2378a7fa15da | -5.38647 | -44.17872 | 2026-10-08 15:41:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ac1186e6-4da6-3075-baf2-2cf2368b292e | -11.20341 | -45.21879 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 6e0663ff-933a-3cb1-b857-9fd6e6668dbf | -6.79801 | -45.06105 | 2026-10-08 15:41:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 44549b46-526b-30ae-857b-dc91bd1afc76 | -5.53679 | -44.29249 | 2026-10-08 15:41:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b5df4d07-4dee-32d0-85b4-c144a4431880 | -5.70815 | -41.72485 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 55bc734b-c1d1-3eb2-8cb6-b2f14783cc70 | -4.58609 | -40.6476 | 2026-10-08 15:41:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 609fba7c-5d80-3f38-9995-8ca39ace0771 | -10.30812 | -42.384 | 2026-10-08 15:41:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 9b728872-eb3e-34a5-9783-ee15a64a6039 | -8.59072 | -44.86902 | 2026-10-08 15:41:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| f59b65e1-032d-3826-a397-8cecd93b7023 | -5.95045 | -44.26823 | 2026-10-08 15:41:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a5e99a42-2d58-3238-9715-9739a9e3dca2 | -11.11059 | -43.998 | 2026-10-08 15:41:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b3d20f3d-2bff-3a1c-b041-1fdc533f3464 | -6.5956 | -37.89438 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 19.2 |
| af2d729f-2a0b-3957-a7d0-a1008359a52e | -8.94781 | -45.13552 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e84706db-87ff-343a-a8c5-4fb5973b3514 | -8.99269 | -42.33973 | 2026-10-08 15:41:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 19c728ed-a14c-3ae5-99d4-e510ce20551b | -6.49417 | -41.83365 | 2026-10-08 15:41:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 0e5e61ff-3447-3767-a896-e8e05aee7b01 | -11.21983 | -44.86641 | 2026-10-08 15:41:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 521827b8-469f-3af9-918c-55d36b6e6146 | -9.97089 | -43.50524 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 0894bace-c314-35f9-af3f-48a28afc7c0f | -9.89789 | -44.85707 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 352.7 |
| 19a45bd4-a265-3113-a3c0-82334954ab84 | -9.93967 | -43.56787 | 2026-10-08 15:41:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| fa263a4a-3389-3c07-841c-bbf88b02f234 | -6.60793 | -37.89654 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 20.9 |
| d57d7f94-987c-34f5-9135-c9db5c9d8f1a | -6.237 | -43.86114 | 2026-10-08 15:41:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 96af6626-4347-36bb-a237-f60a718c79f3 | -8.60404 | -45.62617 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 3a801345-5983-3598-a4d8-bd8544bdda1e | -9.95154 | -45.96786 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2236bccd-9018-3f30-9a99-fa200910e0d4 | -6.49957 | -44.70727 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 915b5176-81c9-39ba-9c77-82bbb8aebf13 | -7.38484 | -46.23183 | 2026-10-08 15:41:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| ebb2efbb-a855-34aa-b0bf-ff19b08c076c | -7.60122 | -42.37344 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 278ce681-969c-3531-b2b4-7c3291582634 | -6.31528 | -43.34549 | 2026-10-08 15:41:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 78536d9b-62a6-3ba7-8eb3-58cd5ed8918b | -11.19904 | -45.21853 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b866ab00-a5df-3429-9154-509932f409f9 | -6.67163 | -45.35636 | 2026-10-08 15:41:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 8b02fbda-947c-30c1-a5c5-24c23b2f5642 | -6.46746 | -46.53901 | 2026-10-08 15:41:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| b067343b-6024-3359-999f-754b07d86d5c | -6.6165 | -37.90039 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 1c3cf296-a353-3b2f-9dc3-a9275e7d66e3 | -7.37733 | -46.23278 | 2026-10-08 15:41:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 496744ca-ed7d-3c4a-ac3a-f5817f90a9ff | -9.37232 | -45.93571 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| b256f71a-1947-35f5-a0c1-6c646284c61d | -8.21553 | -46.40955 | 2026-10-08 15:41:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 624098b9-fe0a-3e41-b979-23930f882b28 | -5.73013 | -41.77607 | 2026-10-08 15:41:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 64b89027-ab99-3758-9d62-e274ff740e8c | -5.71274 | -41.65045 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 59533d27-0db8-3130-9dd4-a6fa58965a6a | -5.94031 | -44.32701 | 2026-10-08 15:41:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 166f911c-9ffb-3e8f-b6f1-e931a73d59e3 | -6.85622 | -41.74673 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 8ed2916b-ec0a-3e0c-96aa-0de683e9aa05 | -10.59879 | -43.84224 | 2026-10-08 15:41:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 7e961b34-59e2-3142-a75a-3c5ab24df7a9 | -8.96166 | -45.13951 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| d858a375-e777-380e-84f1-f86de8a5e6da | -5.71531 | -41.66799 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5fb67aa3-379c-398a-8784-285b7a027716 | -7.47377 | -42.84935 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 35.1 |
| 6afaa88b-1975-343b-88dd-f5c2abc8df4d | -6.46887 | -44.03096 | 2026-10-08 15:41:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4e0c049f-8966-343d-870f-2009b60bb74f | -6.85025 | -41.74129 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ccd8e4ca-e30a-31d9-9b00-cfaf20affda1 | -9.82055 | -45.69168 | 2026-10-08 15:41:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 18237054-fb8a-32f0-bd72-ce3cd418a026 | -10.1665 | -44.67152 | 2026-10-08 15:41:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 78297d94-57b5-39ae-9aa2-fe6bd3018dcf | -11.25646 | -45.18069 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e290f1a1-5347-33de-80ae-92d681fcee9d | -5.73527 | -45.15354 | 2026-10-08 15:41:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2a306cb3-4a58-3b29-9eef-d19e662f63c1 | -5.74099 | -42.063 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 5a4333a1-f505-3bf3-b29e-4a71ebecd6b8 | -8.5603 | -40.28236 | 2026-10-08 15:41:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 8b9144df-d94e-31a5-bd4e-a01f3ed4b5f6 | -5.74808 | -41.71991 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 52.6 |
| 2eb93bae-645a-3df5-a2f1-14b08fe1d955 | -5.70856 | -41.72775 | 2026-10-08 15:41:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| c41f114d-d44f-3844-9b65-3fbfcdaa2b73 | -9.7644 | -44.79079 | 2026-10-08 15:41:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ba66a52d-90e2-31b3-b517-229bfeb82c09 | -10.07501 | -46.00175 | 2026-10-08 15:41:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 9e8f657d-84bd-30dc-a7e0-185ea6e7296f | -7.86955 | -44.1458 | 2026-10-08 15:41:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 0d500172-d224-3ff0-b2e4-4beb4e22cbdb | -5.99117 | -40.93925 | 2026-10-08 15:41:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 46.0 |
| dfa3891c-7cf2-3642-8e26-0b8c70c97b8e | -8.60201 | -45.63313 | 2026-10-08 15:41:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 0a8a5627-ee5c-3510-8bb0-2450b08b5a86 | -7.47417 | -42.84694 | 2026-10-08 15:41:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 46.9 |
| cd287614-6578-3aa5-b1c7-87af38bcd4c9 | -6.84594 | -41.74793 | 2026-10-08 15:41:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 183.2 |
| 92a8cd5d-5488-3e14-997e-451110369d86 | -9.73931 | -42.24592 | 2026-10-08 15:41:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 8785d01b-6187-3bb9-8151-9572d1a00ed0 | -11.11189 | -45.69115 | 2026-10-08 15:41:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 46a3cd76-7df9-34d9-9ed2-b942d4b90b93 | -8.94177 | -45.14952 | 2026-10-08 15:41:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.2 |
| f8adefce-d0ba-3314-8282-88ea99c2cc8e | -10.34254 | -46.2437 | 2026-10-08 15:41:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 8682595c-cb3e-3c28-bfba-26102dd4c659 | -7.76726 | -44.16883 | 2026-10-08 15:41:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README236.md)
