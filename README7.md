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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc2b60ba-45a8-3d3d-9228-71f85024c56e | -8.06765 | -48.67833 | 2025-09-10 00:33:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 567e76ae-52cf-30ea-b07c-fa83d32382b8 | -9.16517 | -46.05342 | 2025-09-10 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ff2b019c-5fac-31ec-a6cb-c675b2b6b014 | -8.41022 | -49.10044 | 2025-09-10 00:33:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7d04fd74-f5fd-3b31-953f-e59752d3da1e | -6.68053 | -51.4083 | 2025-09-10 00:33:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 37ee79c9-3a63-3fea-81bf-0c1700971c49 | -3.67937 | -49.01986 | 2025-09-10 00:33:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3033f988-3960-3260-9957-58bcda0340bc | -5.8655 | -48.16355 | 2025-09-10 00:33:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 25.8 |
| fa3c6737-cbf0-34a6-bba9-1c7eae6ccc23 | -6.26528 | -43.42279 | 2025-09-10 00:33:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 4baaee89-e6f7-3f92-877d-9960bdb8ad39 | -5.66956 | -43.90664 | 2025-09-10 00:33:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 41e1d7b7-3e13-3bc2-a789-1ca2c83f828a | -8.98222 | -46.06351 | 2025-09-10 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 746804f3-4e53-37c7-9bfa-ed452b4870e4 | -4.48752 | -48.11989 | 2025-09-10 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 3d435e25-326f-3dd4-a5c7-79a253734af0 | -5.67422 | -45.47057 | 2025-09-10 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9cf4772b-cea8-303b-abbe-36d13f40c7d2 | -6.20731 | -45.62092 | 2025-09-10 00:33:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| dc5a716c-aad6-3268-87c0-df92b5b04099 | -9.98065 | -50.31977 | 2025-09-10 00:33:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 35.6 |
| fe86183c-cf8d-3d07-bdd4-ca5eb480534c | -7.76644 | -46.0734 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 8b351e64-e237-3641-9969-f2e5635bf379 | -9.09197 | -46.97146 | 2025-09-10 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 78044fbd-3973-36d2-b3b3-118e795d7f1d | -10.30584 | -48.81872 | 2025-09-10 00:33:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4ea6759e-7f92-3968-9267-a1789507161b | -5.58383 | -42.92062 | 2025-09-10 00:33:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 0de0e8ec-4323-30a0-8ba6-53d8285b6c90 | -10.03212 | -51.68135 | 2025-09-10 00:33:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 6e03828e-0e92-3576-ace5-5fdf17ccce65 | -9.0742 | -46.9743 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| e4a578f2-b64a-324a-827e-a23c5c65df92 | -9.99167 | -50.32915 | 2025-09-10 00:33:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6128e6bb-6701-3e61-917b-6cfc322ed623 | -10.00769 | -51.70303 | 2025-09-10 00:33:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 90feb317-09c9-30bb-9ad3-490694199b76 | -9.07754 | -45.7051 | 2025-09-10 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 775ea416-407c-3fef-a66a-26f58da0d1e1 | -9.676 | -46.60056 | 2025-09-10 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 685db174-bae6-36da-8016-95c0b8a89066 | -9.69549 | -46.80295 | 2025-09-10 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b48704fd-4471-3ed4-83c3-6decfbb80f21 | -8.92961 | -48.11372 | 2025-09-10 00:33:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 3215d481-4fe1-3505-a0a2-acb1c955b97f | -7.5479 | -48.24911 | 2025-09-10 00:33:00 | TERRA_M-M | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 60aeda97-08da-34fd-970a-350768abbeeb | -8.06893 | -50.18279 | 2025-09-10 00:33:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8f7f8e9f-9bfa-322a-b118-5bc88aa9264b | -6.34392 | -47.09751 | 2025-09-10 00:33:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 4de02660-7af4-31fa-bbff-9f651418a6c9 | -4.47639 | -48.11869 | 2025-09-10 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6a2381a7-052d-355a-94a1-0f4f2a270042 | -10.01993 | -51.66959 | 2025-09-10 00:33:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 79e36daf-cd92-3379-9e86-d41a841cde8e | -10.73108 | -48.28942 | 2025-09-10 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b3bd2b55-3e19-39f7-b266-172c132ce31d | -7.55224 | -44.65751 | 2025-09-10 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| d19db5a1-69b5-3b77-a6e6-09186473cf7a | -4.83772 | -45.35591 | 2025-09-10 00:33:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 31c943b5-4aed-3dee-9776-f7e25b6ffc4a | -9.2203 | -50.53215 | 2025-09-10 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2abc605e-00e7-3657-97fb-b84fa22d8e54 | -6.68206 | -51.41953 | 2025-09-10 00:33:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f477941e-438b-3f76-a6aa-b24c3dc598b8 | -7.80158 | -46.07274 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8eb282e9-a393-3b70-88c2-b94a369fca8f | -7.10616 | -50.76411 | 2025-09-10 00:33:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a82cf548-dbc4-3f43-a5b7-d4ff8d6bd40d | -7.07881 | -45.20421 | 2025-09-10 00:33:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 31523647-52b4-3acb-90dc-1134cd238a7f | -9.61274 | -48.06424 | 2025-09-10 00:33:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7b35df7c-8a88-3055-8ff1-b7fbbaf1e764 | -10.74411 | -48.18604 | 2025-09-10 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 01c96f98-a5f6-335d-8fab-cfb97dd504da | -7.99747 | -46.33607 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b21e0328-3be3-3f12-bce1-f5496d16e0b9 | -5.79774 | -51.67422 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b257db1a-b35b-30d3-8778-2c743f3f91e6 | -10.01825 | -51.7016 | 2025-09-10 00:33:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| bf987bbe-bc59-36b9-8d3e-433107ebeb76 | -8.38693 | -47.99306 | 2025-09-10 00:33:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 2048427c-3cf6-351d-8ed2-7f7616897d6c | -8.97302 | -46.06479 | 2025-09-10 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| bd7114f9-cf45-3b43-8e40-013c80fd9895 | -7.81337 | -47.50871 | 2025-09-10 00:33:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 6b5e4dd4-3870-3d4a-8e30-12daea572547 | -8.70259 | -48.88279 | 2025-09-10 00:33:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ab14f305-1882-3d48-9859-651954defe09 | -9.06967 | -45.71651 | 2025-09-10 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 85c7528f-6ef3-3e22-b849-34104264a749 | -8.061 | -50.19441 | 2025-09-10 00:33:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dd26d7be-318b-3a56-ac82-421bb89f5e4a | -5.74498 | -45.25573 | 2025-09-10 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 84c9ff64-929a-3866-9ae7-0a584fb8503d | -5.53241 | -46.5039 | 2025-09-10 00:33:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| daa7a3b0-6866-3f76-a653-98494692b8ac | -5.57651 | -42.915 | 2025-09-10 00:33:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 6ecaaf20-ae7b-361a-9f80-95bcf07fb209 | -8.04641 | -48.6694 | 2025-09-10 00:33:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 4aa93d21-0969-342e-ad88-76f580248767 | -7.44808 | -49.27399 | 2025-09-10 00:33:00 | TERRA_M-M | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e1eaa5cd-f666-3eb8-9546-ceb1d402f591 | -7.87163 | -46.03186 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 13ead562-c6c1-30ad-a72e-b3ef6f3e03d1 | -8.42041 | -49.1083 | 2025-09-10 00:33:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5b57afa2-1cca-3b91-aaee-8c8de39e0848 | -9.66461 | -46.64912 | 2025-09-10 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 02eaac0e-a998-35b9-b7d3-a516765c8883 | -7.9961 | -46.32635 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ddb7362a-3e68-33d2-845b-ed3f0979a1d4 | -5.72703 | -45.41687 | 2025-09-10 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 98037ae7-5cc8-393d-8bf7-38f02f7cfd80 | -9.69806 | -46.82112 | 2025-09-10 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6e70fe72-7921-3f84-a3c9-993ede8c51d8 | -10.03971 | -49.16736 | 2025-09-10 00:33:00 | TERRA_M-M | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5db64cbb-7c50-3266-9849-a96c0eb2c4ea | -10.74288 | -48.17701 | 2025-09-10 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4e981d61-fead-307c-a9d3-3255c095f536 | -7.37418 | -49.54368 | 2025-09-10 00:33:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 65bddccf-2a44-3218-97f7-2cdc97a45289 | -9.67469 | -46.59135 | 2025-09-10 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 845b6ce0-fe0c-3e05-88ae-9fd9c35130a8 | -9.05888 | -49.82299 | 2025-09-10 00:33:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 24d2e0b5-6085-365c-8685-2e0332b17e23 | -6.34521 | -47.1067 | 2025-09-10 00:33:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a48e3b37-2432-33c9-a0ee-867459a3ce06 | -8.05775 | -48.68614 | 2025-09-10 00:33:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e2a06acb-2982-301b-bed5-ef8b35a7825c | -10.73232 | -48.29849 | 2025-09-10 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 913eb058-7327-3652-a76b-024b02011eba | -6.7497 | -45.12226 | 2025-09-10 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| d1c0ea04-4ba1-3ce0-8c18-1b9ac75acef1 | -10.18778 | -49.58411 | 2025-09-10 00:33:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b0617a7e-0ab9-3b37-a8cd-452da0cf4e5b | -10.27668 | -48.81031 | 2025-09-10 00:33:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| fc28b793-55bb-34fd-9a1f-53b693204a03 | -6.87992 | -47.89148 | 2025-09-10 00:33:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 97e2022c-6625-3ee0-8bb7-34abe6a6c360 | -8.51721 | -45.72266 | 2025-09-10 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 413ad18d-96c2-3a6d-99c5-33915a8e0ad5 | -10.18911 | -49.59397 | 2025-09-10 00:33:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 793afc6f-8741-3e79-ac8f-781f1cde7f29 | -8.98819 | -45.72443 | 2025-09-10 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9694db34-cb67-3bb6-8787-6f229e3d1837 | -4.72693 | -44.45816 | 2025-09-10 00:33:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 3a9449cf-c817-3964-8a5f-69ca0da0b2f4 | -6.19666 | -43.50305 | 2025-09-10 00:33:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| d490233c-8c83-363e-adfd-d17893b1688c | -5.22307 | -43.68539 | 2025-09-10 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 89dce381-abb3-33e4-91cc-2c20e5e6a5a3 | -5.6798 | -43.35729 | 2025-09-10 00:33:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 8be61824-2d63-367b-894c-02ea157d2739 | -6.44198 | -44.07223 | 2025-09-10 00:33:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4261cdea-a6ed-316e-b660-fa8dc3f7f88d | -9.67095 | -46.62946 | 2025-09-10 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0fe0ae4d-783a-3849-915c-80d4323f062f | -9.10212 | -46.97909 | 2025-09-10 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| a82a5f40-bdc7-3709-b674-242573477fa4 | -8.05651 | -48.67715 | 2025-09-10 00:33:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8342682d-3a55-3d0e-856b-b1e6410c2c0b | -9.07267 | -50.48117 | 2025-09-10 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| cf4cc99f-ff63-3fc7-af5d-17b4314faca2 | -6.5681 | -43.14319 | 2025-09-10 00:33:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| bf978391-0307-338c-93db-390301a3141c | -5.88677 | -46.09163 | 2025-09-10 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 957c4be2-e7ee-39b7-8ef2-27fa9c4cf204 | -6.38432 | -44.45147 | 2025-09-10 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d3e9ae53-5831-3b53-8579-07e9333440cf | -8.43061 | -49.1162 | 2025-09-10 00:33:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2625abe6-8d20-38b7-afe9-65f009fe6c68 | -4.48627 | -48.111 | 2025-09-10 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f5bf0c6a-4f65-3bc3-9076-e757cc358637 | -5.6495 | -43.92414 | 2025-09-10 00:33:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| a8f2aa56-281b-37a6-ad42-41269f1d2ace | -4.86106 | -45.6634 | 2025-09-10 00:33:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| bb660f01-17d5-3577-b5c7-3010e6938652 | -9.51691 | -54.65063 | 2025-09-10 00:33:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 524d9afb-a597-31a0-b70e-6f94fd4c8af9 | -7.08865 | -45.20268 | 2025-09-10 00:33:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2b054990-263c-3d9a-bf64-7debe9ac000c | -7.70787 | -44.74349 | 2025-09-10 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5bf07f2d-668d-3e9f-9dba-139a91c54e99 | -9.35833 | -46.50557 | 2025-09-10 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9605780f-4673-33aa-b2ce-e84328c7984a | -7.88509 | -46.2599 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8618c5d4-1552-3fed-b62e-db36645365a4 | -8.07039 | -48.63235 | 2025-09-10 00:33:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 7a362c30-0a6e-3be9-a883-ce51963e2692 | -9.01243 | -49.54242 | 2025-09-10 00:33:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 41a1c201-8c45-3c35-8acc-e304897e8123 | -5.87101 | -51.7684 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bfe1fdfb-c51f-3887-add4-bf4cb4aa159d | -4.48566 | -42.91981 | 2025-09-10 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |


[Clique aqui para ver as próximas entradas](README8.md)
