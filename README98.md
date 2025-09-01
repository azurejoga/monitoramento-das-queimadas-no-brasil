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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5969f51f-1496-3c58-87e6-6b86d431b9ac | -9.65138 | -63.11608 | 2025-09-01 07:14:00 | AQUA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a130a6bc-231d-312d-ba0d-6ebc36228616 | -8.76383 | -61.43405 | 2025-09-01 07:14:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 17d39bed-6b8f-3859-94bc-3f3cab234f92 | -9.7074 | -64.53828 | 2025-09-01 07:14:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 809b2aec-0975-33f5-9f64-2db658ffc0b2 | -9.44524 | -60.56466 | 2025-09-01 07:14:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e437d34b-1918-3af6-9158-0e6cfdceb143 | -8.65068 | -67.24483 | 2025-09-01 07:14:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 282a41fc-0b5a-3742-8edf-91ff51f3b840 | -9.13811 | -65.84521 | 2025-09-01 07:14:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6c264cd2-648c-3b80-bd86-059992fc0e82 | -9.83639 | -65.05181 | 2025-09-01 07:14:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 51a449ea-ca1e-3d7e-a689-009df06b6db0 | -9.07926 | -65.42656 | 2025-09-01 07:14:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 24c0b9c9-c586-3db0-89d2-5e7cc8548fcd | -11.0381 | -45.1256 | 2025-09-01 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 07bd60f0-685a-379a-8587-a9db3aae3564 | -7.076 | -44.3376 | 2025-09-01 07:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 5853097d-db54-31eb-a4ae-c020e5a2afcf | -12.9385 | -56.9655 | 2025-09-01 07:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 989d1c5b-bd4c-3918-9638-19b777eb5682 | -11.0377 | -45.1487 | 2025-09-01 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 37a6b47b-4a9a-3a1f-8c39-044a33c907ac | -7.9539 | -46.4542 | 2025-09-01 07:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 27201972-7d98-3084-a9dd-e66f702fd45a | -12.9194 | -56.9672 | 2025-09-01 07:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| f910f604-1e8b-35bb-8770-909433019fd7 | -7.0946 | -44.3589 | 2025-09-01 07:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| a1f73360-4bfc-3f77-85f9-18565a00b2ca | -7.0757 | -44.3606 | 2025-09-01 07:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 7a2c80b1-4aaa-32d4-9c10-e182d51f2cf3 | -15.7289 | -48.9892 | 2025-09-01 07:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| c904e61a-2249-3263-b962-5eedd382958a | -12.9197 | -56.9471 | 2025-09-01 07:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 155.2 |
| d3fb1824-bfa3-351c-a458-f6e6ae0800a7 | -15.7116 | -48.8809 | 2025-09-01 07:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 5c62e183-3107-378a-9283-17c1f09bd50d | -15.7121 | -48.8585 | 2025-09-01 07:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| ad92d742-ef48-320b-8530-151c204c321d | -11.0568 | -45.146 | 2025-09-01 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 218.3 |
| 72541e14-890d-33e4-99c3-550af8dbc29b | -7.0948 | -44.3358 | 2025-09-01 07:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| c0c7488b-a47b-3b55-9879-132afc932a80 | -6.8177 | -45.7025 | 2025-09-01 07:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 828fefb4-5bba-33f2-bc11-8f97f4e671d2 | -6.8365 | -45.7009 | 2025-09-01 07:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 77cb3e67-08b4-37b4-9c32-a55a027a4c72 | -11.0572 | -45.123 | 2025-09-01 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 93e88662-e590-35bf-b8f1-60b83bfa7e35 | -12.9387 | -56.9454 | 2025-09-01 07:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 64ae6d6e-ff48-3075-9f8f-08d3d1591edf | -15.5862 | -48.3435 | 2025-09-01 07:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 82.2 |
| b37ae273-4289-31d1-9eee-81dd4ce87f0e | -10.6128 | -44.3284 | 2025-09-01 07:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| a4eeee96-2a62-393f-b79c-439f12adca6f | -10.2488 | -51.1128 | 2025-09-01 07:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 9100fa7d-70eb-3af8-b59f-4f1ca275739c | -7.076 | -44.3376 | 2025-09-01 07:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 132a3f65-23bb-3c4d-b863-fcefd7b41e87 | -7.9539 | -46.4542 | 2025-09-01 07:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 3c246587-1725-3967-8a0c-42b07c661560 | -6.8281 | -52.8143 | 2025-09-01 07:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 3e602346-8c64-32a0-b62e-b13d50826e9b | -11.0572 | -45.123 | 2025-09-01 07:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 219f2d11-2ff0-3a1c-ab2e-f8b6a6048429 | -15.7289 | -48.9892 | 2025-09-01 07:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| f1500262-ec7a-3353-a43b-9093da4c5ae8 | -7.0948 | -44.3358 | 2025-09-01 07:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d24cb9a4-5926-30d0-856a-8d62c50fa7e0 | -7.0946 | -44.3589 | 2025-09-01 07:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| f4ae446a-4354-3712-a286-61d7208d52ad | -12.9194 | -56.9672 | 2025-09-01 07:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 111.7 |
| ffae1764-480e-3e40-be49-d4dfc33a486c | -6.8177 | -45.7025 | 2025-09-01 07:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 45e1524c-e63b-3419-934a-21593711bb5b | -15.5867 | -48.321 | 2025-09-01 07:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 7dd2d984-79d1-3eb7-af2a-aaeec981a940 | -15.7116 | -48.8809 | 2025-09-01 07:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 8927714f-2a6d-3707-8dcd-0c0086000205 | -11.0381 | -45.1256 | 2025-09-01 07:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a1c52638-6c8f-3a6a-be4b-dafa88a49011 | -12.9197 | -56.9471 | 2025-09-01 07:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 157.1 |
| b874949e-7511-307c-abf1-2972056e8714 | -12.9387 | -56.9454 | 2025-09-01 07:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 42c6eb46-154d-38a8-a7c2-f0635b8dba15 | -15.7121 | -48.8585 | 2025-09-01 07:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 4362dfb4-2d61-35a3-8d58-af0ef158d1cd | -15.5862 | -48.3435 | 2025-09-01 07:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| c343935b-b50b-3d8a-84ec-9a930f0d704f | -11.0568 | -45.146 | 2025-09-01 07:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 574b1ad3-b762-3288-a80c-7480c4474e37 | -10.6128 | -44.3284 | 2025-09-01 07:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 5d1c77fc-da22-3ccf-aaf5-9cb619f40451 | -11.0377 | -45.1487 | 2025-09-01 07:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 484ea36b-88f3-3a5a-b57e-325919786e26 | -12.9385 | -56.9655 | 2025-09-01 07:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 7aaa15d0-2b35-3cbb-8e0e-b27983d95a09 | -7.0757 | -44.3606 | 2025-09-01 07:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| e7be1235-e6d9-3ff7-b342-7fab03ede6c0 | -10.6131 | -44.3051 | 2025-09-01 07:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 7ec7d159-a855-3779-a674-e8ba3838d7cf | -11.0381 | -45.1256 | 2025-09-01 07:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| f81780c0-75c3-34c2-a781-57433e0e54bc | -11.0377 | -45.1487 | 2025-09-01 07:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 1e97a358-3fda-3de7-a413-be9f00a989c0 | -12.5718 | -48.228 | 2025-09-01 07:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 9632be5d-8006-3ad2-bf91-7cfa0067b9c6 | -7.076 | -44.3376 | 2025-09-01 07:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| bf8dacae-d054-3d7e-8f85-20872145fe88 | -12.9387 | -56.9454 | 2025-09-01 07:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 3f54059b-280c-32b5-91cd-cfb572575f68 | -7.0948 | -44.3358 | 2025-09-01 07:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| aa7f482c-4004-3150-a45a-140f801d8a83 | -12.5914 | -48.2032 | 2025-09-01 07:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| a2e453ad-a646-37b1-9e38-59ba7c0c73e9 | -12.9197 | -56.9471 | 2025-09-01 07:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 854a2f5b-cbd0-3965-845c-38687e7d74d7 | -7.0757 | -44.3606 | 2025-09-01 07:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 3362ea68-7d3a-3cd1-a080-2f8a447a30f5 | -15.7116 | -48.8809 | 2025-09-01 07:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 1c237d32-fa59-390e-b048-165ddd33fcfa | -10.6128 | -44.3284 | 2025-09-01 07:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| c690aaee-c8b1-3518-91b2-718cfb1883c9 | -12.9385 | -56.9655 | 2025-09-01 07:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 0136fe2a-cab3-3832-9e44-80c08aefa62f | -12.5722 | -48.2059 | 2025-09-01 07:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 571ad7ab-e8e3-3e06-8bfc-0e60f517741c | -11.0568 | -45.146 | 2025-09-01 07:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| ebaf3cff-7e8b-37e8-84ff-9b8e013cb712 | -15.7289 | -48.9892 | 2025-09-01 07:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 7d058317-e799-3943-8b71-7270483777f1 | -12.9194 | -56.9672 | 2025-09-01 07:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 1d6b6042-3577-3e62-9adb-7298432a3905 | -10.5937 | -44.331 | 2025-09-01 07:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| f40f043b-b79c-3aee-9394-ee0560c7febe | -10.0434 | -48.0998 | 2025-09-01 07:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 70080590-8387-3b3d-bb93-a6a961498a08 | -15.5867 | -48.321 | 2025-09-01 07:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 9c20b5e6-4f6b-318c-822a-8eb1111a098d | -15.5862 | -48.3435 | 2025-09-01 07:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 770b5645-9d96-3db0-850a-0462ae291b79 | -10.6128 | -44.3284 | 2025-09-01 07:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 4d340017-0f4c-325c-a2f8-2bc4902a5974 | -10.2488 | -51.1128 | 2025-09-01 07:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 46.4 |
| d76b2fc6-7e1c-3146-ae22-af73e7bda4b4 | -10.5937 | -44.331 | 2025-09-01 07:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| cbacda3d-385f-3e75-a1ba-30e6daef9169 | -10.0434 | -48.0998 | 2025-09-01 07:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 5352a836-a9e3-33c2-8a10-675fb0001287 | -11.0377 | -45.1487 | 2025-09-01 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 39ce2da6-4bce-3f92-ab83-334c444fbc55 | -15.7116 | -48.8809 | 2025-09-01 07:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 116.5 |
| e880facb-a277-3575-8e57-475d53d79d50 | -15.5867 | -48.321 | 2025-09-01 07:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 732799d2-014d-35e6-b123-db094e36a41b | -15.5862 | -48.3435 | 2025-09-01 07:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| c9eefe20-1300-3ece-a54e-fd8b92e0b5e1 | -7.076 | -44.3376 | 2025-09-01 07:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| b454ac6c-de57-3a65-bed6-ba2cb3f65e06 | -11.0568 | -45.146 | 2025-09-01 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.8 |
| f7d1735a-f476-3dc7-b054-57574f1954db | -15.7289 | -48.9892 | 2025-09-01 07:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 32590fc5-4899-3ddd-ab8e-bf636411a8e6 | -12.8044 | -48.0849 | 2025-09-01 07:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 8d5376cb-40a4-36bb-a21e-e108af96c54a | -15.6063 | -48.3177 | 2025-09-01 07:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 395dbaa1-aff8-30d3-8143-8d39d0774655 | -15.6058 | -48.3402 | 2025-09-01 07:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| fcb7fc3f-117f-3b7f-b93f-c0e4ac96b7d1 | -12.9385 | -56.9655 | 2025-09-01 07:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 25d1a540-8c1a-3bf6-8fbd-6675d3e09099 | -11.0381 | -45.1256 | 2025-09-01 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 011aefba-bfe8-3b2c-8fbe-56735fe90115 | -7.9539 | -46.4542 | 2025-09-01 07:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 678eb64c-890e-3b91-bcd0-3199604fcd09 | -12.9194 | -56.9672 | 2025-09-01 07:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 5dc84fb5-1d9f-3a04-a9cd-ea49523eb1f0 | -12.5722 | -48.2059 | 2025-09-01 07:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| b7ccc646-de50-3a21-8d10-552c5b1a715b | -7.0757 | -44.3606 | 2025-09-01 07:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| ccc8731e-ff1a-3fcc-8b3d-fd1a22564927 | -12.9197 | -56.9471 | 2025-09-01 07:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 21846f30-bad6-3f01-91b8-f118c0f42974 | -12.9387 | -56.9454 | 2025-09-01 07:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 7946e29b-6591-392a-991c-704bb8c849ba | -11.0457 | -47.0066 | 2025-09-01 08:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 0c8109e7-7a6c-3524-a693-0162c2030fda | -11.0572 | -45.123 | 2025-09-01 08:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 881b33fe-3276-3705-b088-c23144afba55 | -10.0434 | -48.0998 | 2025-09-01 08:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| bd741bbc-d1b6-34cd-88df-9f7d59e7cc1d | -11.8185 | -46.4087 | 2025-09-01 08:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 46213b39-2d94-3b75-b4ec-d62d8bd54eca | -7.0757 | -44.3606 | 2025-09-01 08:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| dab3ce63-379b-3dc6-ac89-bee7d14dd378 | -10.2488 | -51.1128 | 2025-09-01 08:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 115900a9-4eff-3e79-9048-106c67e2e509 | -11.0568 | -45.146 | 2025-09-01 08:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |


[Clique aqui para ver as próximas entradas](README99.md)
