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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69822e9f-123c-309d-9492-b191d542061b | -7.96079 | -46.42483 | 2025-08-31 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f200e77d-3e12-370d-abf0-b9bf6ea425ce | -6.17145 | -43.321 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 5bfd5b38-65c6-3353-970d-6dfc45ca1e5b | -8.33596 | -47.41543 | 2025-08-31 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04cc663c-21cd-38fb-80d8-bd822317782a | -8.12056 | -45.00709 | 2025-08-31 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 341ba6e9-0916-3dbc-aa68-817e1a3cd940 | -11.31231 | -43.68927 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c9918dc5-abb8-36f7-9ffd-6debf912047a | -8.10005 | -46.26799 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 947c2e86-617b-3a94-8a52-b5ed376b08c7 | -7.38811 | -46.6602 | 2025-08-31 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c4f2ba1-58d3-38a6-a3fd-c505d2161a1f | -7.14778 | -44.91999 | 2025-08-31 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 100f119f-442a-3b7d-860e-57296638f2c7 | -9.66022 | -48.34142 | 2025-08-31 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72c4be78-cf77-3494-97ba-9ec9fbe1941d | -6.42651 | -43.95984 | 2025-08-31 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bcff1f05-7727-3190-99c4-0d1748b17ac2 | -5.99682 | -43.35844 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 50ed89a4-4ce9-31d9-ab78-930405809477 | -9.74956 | -47.13836 | 2025-08-31 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 791aec6e-d465-3c25-9cb6-a09e05c11f16 | -11.36471 | -43.56569 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7f2c174-97a7-36e9-a41d-943c9c942bf9 | -9.59817 | -40.35854 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fe20bc58-2765-3d5b-98f7-e67756b8ef00 | -10.02529 | -48.37533 | 2025-08-31 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6d984f1f-8249-3fd0-8f81-f6c499672f4a | -11.06837 | -44.6353 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9127394-1200-398b-b884-9b9e5238433c | -6.09161 | -46.80836 | 2025-08-31 04:02:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49bd9da4-159c-362e-a796-b47e7b675258 | -11.06031 | -44.61617 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a3c74b5-8c8d-308c-9756-2fb047b994a2 | -6.13815 | -43.31988 | 2025-08-31 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7608c0cc-2cb1-3ed0-b264-a714c1a05da3 | -5.69285 | -45.95939 | 2025-08-31 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e34c819d-bd78-3b3e-afd6-6ae1697c29a6 | -6.18081 | -44.12749 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42dc3696-c261-368d-98a5-9e547ba70f72 | -9.11818 | -45.20773 | 2025-08-31 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1554d6eb-57b1-3b47-8f49-57dd6a80fe8e | -11.3251 | -43.65507 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fd31e5a-86a9-349a-944e-648bd4633089 | -6.52078 | -42.95268 | 2025-08-31 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f868b30-b077-364b-889e-ce39e0389ba0 | -11.31644 | -43.68593 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be3e667b-f883-3f8b-b583-016ffd14e691 | -6.28516 | -43.54552 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24873c11-234b-3539-9cba-e94548237a8b | -4.27412 | -48.6405 | 2025-08-31 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9731552-e288-316e-aecb-67888c43e13f | -11.01222 | -46.95789 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2b58fd0-23c4-379e-bdfe-245a1504be29 | -10.03559 | -46.0205 | 2025-08-31 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1f633c2-b993-37d5-ad95-c1e27afdb98f | -10.61243 | -44.90446 | 2025-08-31 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12527b8e-e3bf-3947-82f3-19de3ee94c56 | -7.10971 | -44.3148 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 71f1b826-f2e4-3b0f-87d2-bcdd05bfc7bd | -6.49753 | -43.5558 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a5dcff4-de38-3826-aa56-730b0377ae7a | -11.01816 | -46.87374 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f7de6282-7560-3f99-b62f-06b2056cc39c | -11.30229 | -43.66329 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5aec3223-9543-35e3-92ba-ce96f4c56523 | -5.47641 | -44.40506 | 2025-08-31 04:02:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cad5d110-06f8-32ed-9e5c-ce6b678445ce | -6.28587 | -43.54122 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 144e20ee-cc62-3e95-b109-4a6a30298fc5 | -4.15991 | -46.77771 | 2025-08-31 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3921079d-5a2f-3e53-bb7d-f3c5b83a4363 | -11.35045 | -43.63115 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dfd3caab-55f5-3e8b-9def-c5331a87f22b | -6.13076 | -44.05306 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4149f3a0-25d1-31f1-a85d-b9faa5324fe2 | -6.64162 | -44.25509 | 2025-08-31 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 56325a16-3988-3cd9-ab2a-722de134b9e1 | -10.10586 | -49.28391 | 2025-08-31 04:02:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73587dc6-4d18-3b69-9b9f-8c31c955d734 | -8.17087 | -45.04076 | 2025-08-31 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3fb130d-7896-3dd2-b491-51dad26be6e5 | -5.49098 | -43.19254 | 2025-08-31 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6fe05e44-6fb5-3ed2-98ad-fdc1bd714f52 | -8.15763 | -42.30323 | 2025-08-31 04:02:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2aabf0de-0c2b-3f93-9ec4-d0a771d7c001 | -6.20917 | -42.74908 | 2025-08-31 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 18a263b6-9a1f-3ccf-ab1b-70f9b91c19c9 | -6.87245 | -45.1513 | 2025-08-31 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60ffb4ec-3954-3ae5-a4ec-dccd2bf5f7fd | -6.24579 | -42.41423 | 2025-08-31 04:02:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1f9db5b7-ef28-3e1a-b9b0-753bcc103d9e | -9.60202 | -40.35558 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8ab64e43-75de-364c-9a38-ae0ca26655df | -9.5877 | -40.36047 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 22c5e3f1-3e64-318d-9dee-c5e3b7cb22eb | -8.17477 | -45.04138 | 2025-08-31 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79cd6986-b69e-3f81-86eb-c27c7dc1e1d9 | -11.326 | -43.67135 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a20dc63-a9fc-343d-a83e-ff9980e7a593 | -9.6943 | -48.29587 | 2025-08-31 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c3f7748-65e4-36eb-bf2e-fbaf14fecf82 | -9.59377 | -40.365 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 946b1f5d-44d8-3a92-a31f-e64aa74e42e2 | -10.60234 | -44.32652 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 0dc1d46f-af75-39f5-8ca3-44eac0c927d5 | -6.1661 | -44.00254 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 650a30ff-f5b1-3e64-8d92-4e5f495e390e | -11.06034 | -44.6384 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6b93319-76b0-36a8-80a3-46ef6e7285e7 | -5.79378 | -42.55857 | 2025-08-31 04:02:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 46890643-4187-3655-abe5-260ad84a4929 | -6.36495 | -43.56326 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f138db2-ae6f-3986-a23e-7d07fa36f40d | -9.59925 | -40.35157 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9a91d204-65f3-3373-ba5c-b34f33840452 | -6.43385 | -45.60707 | 2025-08-31 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69076882-a3db-3c7f-935b-1cd8cb8adaa0 | -6.55102 | -43.68877 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4ac39e9e-a5ec-3dba-998c-6fb9e3f3a291 | -7.95367 | -46.41489 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 919b1428-2c13-3f08-bdc1-ac120f71bc32 | -11.00622 | -46.8434 | 2025-08-31 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ae7ce40e-8dec-31a3-b555-7ca7173d4d8e | -5.90857 | -36.85834 | 2025-08-31 04:02:00 | NOAA-21 | SÃO RAFAEL | RIO GRANDE DO NORTE | Brasil | 2412807 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 792a6e30-221b-385b-bd56-80fe6ff37df6 | -5.47771 | -44.40245 | 2025-08-31 04:02:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6a865315-cd39-3669-9dac-3daa23db7773 | -8.55849 | -51.30299 | 2025-08-31 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5f9d93ed-9691-35e1-b870-6b0ccb173e2c | -7.10519 | -44.31876 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 20d77ad6-8e51-3a19-bfa7-1b3fe53c884d | -6.58496 | -43.63946 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0c5d0ba-3151-312c-aad7-a97bb018360e | -10.77741 | -48.82349 | 2025-08-31 04:02:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2c5c03f-e0cd-35cf-b7cc-2f47727b7326 | -6.50923 | -43.55309 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae281392-687a-3466-b7f1-c8904bec9e00 | -7.4163 | -44.08381 | 2025-08-31 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42ab3ba2-f868-3e6e-9c10-9eb38c40e392 | -6.1725 | -44.13076 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9e1b229-fb85-33ce-98b3-c454a85a799f | -7.33332 | -44.08973 | 2025-08-31 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c11a7db5-5ddd-3861-8a2d-50342bd1e0af | -6.44444 | -43.99067 | 2025-08-31 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a7cbdbb3-1a6a-3630-8857-5ce3ee1ea57a | -7.22951 | -44.22301 | 2025-08-31 04:02:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 89e89262-7f0d-35f7-9746-0f306ee795e8 | -6.5806 | -43.64304 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a74fff2e-a115-303d-bd33-d0f9ea14a4b9 | -11.3533 | -43.63558 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d665fbb5-6a22-3788-b414-b97ca8a701f6 | -6.17916 | -44.20673 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c30870f-5ae2-3538-99a1-175bcae3d364 | -7.39866 | -45.92374 | 2025-08-31 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b97e51e-6e7b-3234-b196-b6d2a1fce2b6 | -6.61763 | -43.73872 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27d7c6c3-1e29-3d6b-8d82-4ed454ab9a8b | -11.02301 | -46.87064 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bab6a91e-1fb4-3957-8cb6-9d85d3c3eaea | -7.41088 | -49.5162 | 2025-08-31 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2dd6da4-1454-3d00-9434-ce27778365ae | -5.80368 | -43.86985 | 2025-08-31 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e0ad793d-c58f-3ffe-b978-b4807085aeb6 | -6.49314 | -43.55958 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1136ae8e-dab5-346a-babd-3253c65e6236 | -8.85911 | -45.73193 | 2025-08-31 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ff326c8-8c61-3ac5-ba67-46555da44d07 | -10.93388 | -46.83855 | 2025-08-31 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f39f385c-a7e5-39fa-a659-a1c0565da774 | -6.96584 | -40.94228 | 2025-08-31 04:02:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b57e813a-9ac3-3fd6-ab0f-1d7c34c30750 | -5.40361 | -37.70925 | 2025-08-31 04:02:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 987a28c8-99ad-3e94-bdef-b5ce909c5e22 | -6.12945 | -42.9506 | 2025-08-31 04:02:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 3e170120-e42f-3f54-ad48-15bbf37beeb6 | -11.35016 | -43.2871 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fea999ac-3056-31a6-9668-decd50510ce3 | -6.82023 | -43.34665 | 2025-08-31 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 15ce7feb-8639-3b65-a4d1-b58e81d745a5 | -4.50511 | -42.90403 | 2025-08-31 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbdf8b28-e02a-33b7-891c-d7f0d6640ecc | -7.6476 | -42.65411 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2779156e-249b-3754-b491-0baf10c13e75 | -6.51431 | -43.54506 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3602d3a6-766f-3b23-ad92-5b7ac7f58536 | -6.94947 | -44.0566 | 2025-08-31 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93e66497-8eac-3a1a-9982-fd934d03decf | -10.48746 | -51.62918 | 2025-08-31 04:02:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1385dcbb-ccff-33d7-9652-a39367630097 | -11.29655 | -43.59015 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8402893d-73cf-3d7f-99fe-aa0b80cf2e4b | -11.33783 | -43.62106 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| affde241-db1d-36e5-97ba-d156cd6bc384 | -6.69436 | -44.05175 | 2025-08-31 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60f414a0-4eb8-3241-a477-635125bfd117 | -11.36155 | -43.58503 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README20.md)
