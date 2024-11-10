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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f30bae4d-0d72-3231-9775-3c5560f52c95 | -2.43438 | -50.51906 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dce71337-a2f3-3252-a99d-b8f026ff714b | -3.24284 | -48.74375 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f41a3f86-de58-381a-82bb-fdf6aa7d14b9 | -2.10914 | -51.09104 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c364b88-b6a6-339b-8a6b-41602f41a79f | -1.51982 | -54.99836 | 2024-11-10 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| dae35dff-f303-33da-89ef-8c276a6c4320 | -3.45805 | -50.18615 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 38f1c1c0-32ff-3db1-ba1f-4bea94413307 | -2.85215 | -51.36472 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1e8922d-6a42-3e93-b41d-276331e0bb14 | -3.08797 | -50.42869 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 414b048d-b580-30cb-86cd-8463e2b5a2f1 | -3.34893 | -54.12782 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9770d789-3a1b-3f12-8702-15caa2fec415 | -4.05969 | -54.42689 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5bff023-667e-340c-b1f6-3bc9d0569b99 | -2.89626 | -49.39319 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9e9149a-19e8-3c1c-9610-c6d037e2c1f9 | -2.3801 | -50.42265 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d781058a-5cfd-3690-8962-0e52f5b2e065 | -2.52607 | -48.20128 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b88bfe4-adaf-35a9-b55e-fc7b1cfa3404 | -3.11654 | -45.96959 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2de78c9e-016c-3718-b652-944fb5400e94 | -3.63941 | -50.18873 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d6b3d2c-aab5-3d6b-b63a-a0b7315f43cc | -5.81766 | -44.12193 | 2024-11-10 04:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 624412dd-f579-3098-9556-2c1f576a922c | -7.97248 | -50.03433 | 2024-11-10 04:38:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aae6beac-83f5-324d-bada-7f5d3be595b1 | -4.09119 | -48.51631 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4aa1596d-c8da-34c4-ab9a-092c511b1e5f | -4.37734 | -47.22709 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a2b771e-abfa-3258-bc8d-e799936d6df4 | -4.18884 | -49.7829 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb809251-0bf6-35c7-8685-ef965d8e697e | -2.71876 | -49.297 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de6ed6c3-03b5-3c61-8ae7-85cbad4567fb | -4.14265 | -48.40019 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be53d6cb-b17b-36ae-b739-cddd6c7e21ae | -3.74839 | -49.89442 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2546f2d-8f1c-38d4-bcf9-f837e079d7d2 | -2.87592 | -51.3068 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d41cc82-54a5-341c-9ca2-da40a13989bb | -6.45093 | -42.74873 | 2024-11-10 04:38:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 113ec2b1-c3a5-39e6-a43c-4ae7f6fe75b5 | -3.86183 | -52.37603 | 2024-11-10 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fc5628e-3aa4-3b1b-b1e4-9697b7d28f04 | -3.80716 | -44.68245 | 2024-11-10 04:38:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3fb3e0c-a73a-3824-bf5e-0eee07c118ae | -2.13663 | -50.80587 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f04aca96-b750-3413-b3e2-23f2dc29f2af | -2.03938 | -51.45859 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 429abac6-5c54-3f25-94b1-8f4a9bd23732 | -2.25615 | -50.41175 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb9e88f6-e198-36d6-a3ad-033daf4bb6e6 | -2.93754 | -51.05349 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abb85681-11b0-3b16-83a2-d836c29a6178 | -3.26912 | -46.31401 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6aaeb9f9-4d89-394f-8a81-1aad48938545 | -3.41559 | -51.20189 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ba6211a-1430-3eff-b794-d5ab57accbca | -2.36622 | -50.61275 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fec54d4e-fd01-3e2b-aeed-7d6ca4435a4e | -3.30251 | -54.49179 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3092aad-aa6b-30cc-8048-6c6c4949c713 | -2.02958 | -51.42737 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1596df1d-46a3-34c7-a277-22253d06581d | -2.7264 | -49.18393 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b18e8d46-3ffd-3a9c-944c-eebc9f089bb7 | -2.92447 | -48.31595 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a460048-baa7-37a7-90f3-7d2396c3c928 | -3.14442 | -46.51221 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 575810cd-c50c-30a7-86d5-301a09ae23a8 | -4.71497 | -50.8464 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5ba96e8-2b0d-3859-bb9f-639fe04d1147 | -3.06987 | -49.53485 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54e83240-4683-369f-b886-c08ea0088570 | -4.27501 | -50.67235 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d6120af-5758-37ac-a5b3-085fc4bcf70b | -3.50299 | -52.12891 | 2024-11-10 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8d881c3d-cbf3-33d0-9f4f-a0ce1bd20ef1 | -4.37844 | -47.28693 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dd905d1b-fc2f-35b6-9d00-6893b04a0ce4 | -2.20311 | -50.236 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9963ab87-fd2d-350d-9702-cb703d472d69 | -3.84004 | -44.12984 | 2024-11-10 04:38:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8828774b-a83a-3705-a45b-999c85b1a971 | -4.38751 | -47.27347 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4a69dfa-2c88-3947-a603-5dfb65154dbe | -4.11128 | -50.73452 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56148223-9fa6-31bf-8386-a04771f531d6 | -3.9604 | -49.00164 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b7a58e9-a555-3983-9739-afe0c0159f00 | -2.41785 | -50.48954 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08d22116-5f59-327e-8d40-15282f7fff6a | -5.67016 | -51.14021 | 2024-11-10 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e829a98-b4d8-392e-87aa-214a2073c4d0 | -3.05272 | -48.03901 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5570abab-cf86-3420-a908-4e2911336915 | -3.0971 | -53.32281 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7498b493-f0fe-305c-8039-3fed9012d71c | -2.46761 | -53.97501 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c1206c2-f041-3582-bc80-d908849f7de3 | -4.05816 | -46.07642 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1232725-c891-3c86-8038-4ac2e02245b4 | -4.3372 | -48.60475 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f2009f9-b7ab-3973-8b5c-451fc6284a30 | -3.12896 | -45.95939 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac7d04be-0689-3293-925f-17db33abc3ad | -2.39579 | -50.42859 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70f00554-39bc-3d0a-b228-c1a119a29519 | -2.65114 | -48.63348 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7dbbddfe-dff8-3320-8baf-30ef6a2e9810 | -3.42765 | -51.39282 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 03bdcd87-eb6d-3605-b22e-78f0a20062ef | -2.38967 | -49.83242 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13f138bc-dcbe-3086-8049-2a788a0ebd88 | -2.85035 | -49.43284 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5bcc7e2c-1876-319f-b1b2-ba6f28bac5cf | -3.02754 | -47.96048 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f0e53ae-ff62-3db8-84c3-bd74fca631e2 | -3.2288 | -50.28855 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a03533c0-77c9-3f6d-b1ab-181996900c59 | -2.88946 | -49.22786 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2b40b9b-83b1-3174-a29a-cc7e5cc57dd2 | -2.63708 | -49.87806 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 08b424da-3db7-3b80-a15c-3dcba3b153e4 | -3.31635 | -51.6627 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 54365ee7-6a5e-3fdb-b7c7-0d862933e90b | -2.14714 | -50.80752 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ebf1fd7-eb82-3c65-9648-0f9a0312f323 | -2.43352 | -49.22072 | 2024-11-10 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2233b7c-1a79-3f5c-a4bd-9f1cce93fe6d | -3.96764 | -48.17764 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 533f0d68-695e-30d7-949a-5123a188bd9f | -2.8628 | -49.22369 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5821c00-3a75-321b-aca7-820babca2b22 | -8.89605 | -44.22467 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| deaa7475-0906-3526-a8ad-2c5a18a33853 | -4.07227 | -50.01058 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0dec9090-5c7e-3cd8-9490-8be01089fbf6 | -2.85354 | -48.44266 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef426d83-88cd-3720-93ec-fdb3f6aba670 | -2.66072 | -49.90384 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d41fc01-3900-3a72-acc9-0751ecaef9eb | -2.65838 | -48.65226 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f745011-6813-325c-b360-27cca26d2d67 | -3.46483 | -50.18722 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a075a81d-553d-303c-9cf1-772f0b16b075 | -3.18476 | -51.24718 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7fd27984-5862-3b32-ba19-430a046aaa8c | -2.95981 | -50.41966 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02b7ed2c-3ade-36df-be0b-ff10a778fe1c | -7.4604 | -43.59263 | 2024-11-10 04:38:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 194cf954-ea89-3dde-9d9c-fad6902324e0 | -5.92508 | -44.86769 | 2024-11-10 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bbffcff-cea6-36c6-bbc2-72748f4b2c37 | -2.92501 | -48.3125 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e92e436c-795a-32e5-bdf1-4e16e9b1122a | -3.98803 | -46.41556 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 92817813-987e-3f24-8024-54e3744e062d | -3.66953 | -54.04375 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e382d7e9-2423-3ea3-9f91-1d7fd1dfd0e9 | -2.47361 | -54.56256 | 2024-11-10 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20716b0f-0054-3dc1-82b6-1a4f5c0b6b2f | -3.11361 | -45.96509 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc4fabb2-bb24-30e2-b266-b420e345490a | -4.36374 | -47.22495 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 516b3bcb-c25a-3a3c-837e-2f6b5c7fe5de | -3.16622 | -49.0999 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c89d449-c710-3f71-9664-8a4eb9e5caa5 | -3.90087 | -51.92629 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8dd89058-2ed2-3d67-a0e2-f242b2b75f36 | -8.37556 | -44.14049 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a68b2e85-e5ab-32f4-ac14-85179faffb95 | -4.1209 | -48.24064 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 889bfc43-ddad-3485-ab26-f4978050a307 | -1.60662 | -55.15757 | 2024-11-10 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 210ad21e-9ced-3be8-8791-ed620c1ac941 | -3.25382 | -46.45972 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bee9aa2e-7e73-3685-8794-d3219caa6c69 | -3.35737 | -53.43898 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 963f71ed-8368-3830-bf4b-59840842c85a | -4.0707 | -48.3217 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2efa824d-9ccd-30ab-ab91-cdde344825d4 | -2.56353 | -50.67794 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6984d5d0-7a57-3ad7-8e14-75d70eea3d66 | -3.18363 | -50.59525 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c259a0a9-330d-399b-a1c1-9f516e40c220 | -2.94426 | -49.50127 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d564d016-51eb-3031-b8a1-4a174af8111c | -2.63876 | -49.88935 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbc1fdf7-0414-303f-ab62-81f09ce22db9 | -4.43429 | -47.2433 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dad58c96-8ba7-3101-a6ed-fbcf8e9dd98b | -4.88889 | -48.60579 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README104.md)
