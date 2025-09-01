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
| 306c1300-eed2-3a81-acf7-cd8ca61ca150 | -6.33033 | -43.56693 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 491e1c62-4ddd-30fe-9d7e-c7d74da051c1 | -10.24772 | -51.11558 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 159c282f-d3fd-3731-a8e0-a241d99980fe | -5.86564 | -43.00058 | 2025-09-01 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 36fac98e-7cab-3413-8497-0a213c418e5c | -11.45263 | -46.82071 | 2025-09-01 04:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70f0c3fb-234d-31c1-a045-52bccd5bd33c | -6.18524 | -43.31175 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa5fac12-ea9b-34f3-b717-38d774a45260 | -12.30449 | -45.7175 | 2025-09-01 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 543ec864-93f3-3709-9931-f3f9ad7dce90 | -8.05888 | -48.42391 | 2025-09-01 04:10:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 58597487-a0a5-3fa7-8e18-d207b2d6e70b | -9.64202 | -47.80508 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef80f2ad-fa0f-397c-9409-fe8d87519e76 | -6.2623 | -43.54784 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7568c95-643e-3dcc-8d12-95dd5519fee7 | -9.23573 | -47.08698 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bb355c1a-1388-3614-91d6-597df3f63ac4 | -11.02366 | -46.95599 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 0d0a2a2c-5966-360a-a81d-eb24bd3f0467 | -9.63555 | -46.61151 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f530cc6-06ff-3470-9b92-8ae0f8b92f44 | -7.9909 | -44.05476 | 2025-09-01 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28f6e5d0-db31-31cc-be8f-3d9868422bac | -10.59696 | -44.32742 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 4b630617-bc5a-38cb-90e7-22d38e61068e | -11.02555 | -47.03797 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 5970e101-397e-372b-b947-fa263fb4ab8e | -6.9558 | -44.34107 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5f09978-b773-36c1-81b7-920b901b3578 | -6.81477 | -43.35046 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| fdc2a87a-17d2-395d-9c08-695cf8458bb7 | -6.43968 | -55.62222 | 2025-09-01 04:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f5fa7764-f28d-32df-baad-9e2e4ca38f2f | -6.84243 | -52.82516 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3221e565-ec6c-3742-8aa6-df0a6f3584ad | -6.85119 | -52.81193 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 378d35ca-841a-37de-81f5-4c89723dca4d | -9.23366 | -48.73671 | 2025-09-01 04:10:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b435e2f5-7aa8-3509-9e7a-c7a8b2714b0b | -6.1646 | -43.31677 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0b92dae-7cd6-3758-9610-9bbaf8c83600 | -6.28819 | -43.5636 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7f5418a-556c-3c28-be61-525df3cba062 | -8.19543 | -46.76816 | 2025-09-01 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6d801f33-c2c9-3138-aca9-68449a8ae250 | -6.45372 | -42.40748 | 2025-09-01 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1ca7337e-b558-366f-85b9-cef45d9b8fe8 | -6.15031 | -44.12596 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63f38505-d4da-3439-8ecc-c275ecd9bb97 | -6.97898 | -43.11614 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d03122f-f061-3e1b-b8a3-983343e2f54e | -6.54459 | -43.51471 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 980cef7c-ae00-3601-9a47-9fb43e1c3a1f | -6.43248 | -55.62059 | 2025-09-01 04:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7857fef3-f582-3dbc-ab49-4a32034edca5 | -5.98881 | -46.48836 | 2025-09-01 04:10:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23e2a0c3-4817-3366-8479-202fd0ff8eb5 | -6.38117 | -43.54708 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76b26930-c59a-3c1e-8b2d-f27a1e8fc083 | -12.30519 | -45.71339 | 2025-09-01 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fbadb3f5-0dee-34be-90e5-9e0a8a73a13d | -6.48229 | -43.57076 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfccdf80-7dc1-3563-bcfc-916667b4ebd9 | -9.53153 | -45.84039 | 2025-09-01 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15c4e1c9-526d-354f-a714-a3f37ae4452a | -6.31306 | -43.63006 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3931bb32-5053-3f3c-8d5e-4a9b7de04a3e | -8.87448 | -45.09622 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1e23afa-877f-37d9-b7a1-317f5c766fbb | -10.75132 | -46.35897 | 2025-09-01 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a78d40e-c20c-3938-94a9-ca2e53aa3be1 | -8.82838 | -47.80784 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bec807a-e658-3779-a962-29318cf43bc3 | -7.23944 | -44.05996 | 2025-09-01 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c0a3636-69bf-3db6-a169-d64e851dbf8e | -11.37488 | -43.60626 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 868b0d37-87f5-3b91-bd71-2b1cf72bb05f | -7.39326 | -45.9338 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ec8c808-af2c-3a82-8505-38eb3663ee1e | -7.57218 | -45.20785 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa141f8e-be04-312c-804f-87acf054cdfd | -11.88357 | -46.74657 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bc53afe-1921-34f7-994c-5eea1758dfa2 | -6.81521 | -45.69791 | 2025-09-01 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 5f40775f-24bd-3c14-af2e-9008fb37815f | -10.47938 | -51.62865 | 2025-09-01 04:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52e8d3dd-bc78-3d71-83b7-36fc5b1f6bdb | -6.83367 | -44.24825 | 2025-09-01 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e63529c4-1e54-3bb2-be79-63f665dca727 | -11.08861 | -44.61084 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 901e8348-7cd6-3773-9363-70564032e0f7 | -6.49938 | -45.40896 | 2025-09-01 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3040876d-6a13-3930-8175-623762f18eeb | -5.86623 | -42.9969 | 2025-09-01 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b296bda5-4375-393b-9bf8-d78f34ec9b5e | -9.64219 | -47.80198 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aaffb7f0-c227-3768-891f-1ec6caf1c654 | -7.08297 | -44.35178 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 05f2c488-8fe6-33f0-925e-826e5330dbbe | -7.07783 | -44.34751 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 181e88b9-7541-34bb-ad6f-42128122e1e9 | -6.45451 | -43.96156 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5b55ef46-5cb2-330c-ada4-0c893e91d1b5 | -6.41452 | -43.62667 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 849bf263-e79f-30db-ac46-439ae7d5b70e | -12.32594 | -45.72123 | 2025-09-01 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb7df7bf-cdb8-3cc0-a87d-0bfda4e97908 | -11.02239 | -46.98645 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 88c36814-fb38-3305-a314-006cf4e302f9 | -8.05968 | -48.41936 | 2025-09-01 04:10:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c8d7efa-7964-3397-89eb-563de59c8c5d | -7.3832 | -47.43768 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1aff8651-e5a2-3a20-83df-3e23d5224625 | -7.09043 | -44.3373 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 47114b5a-0cfd-34a0-8485-bcec12947ab1 | -6.85034 | -52.81657 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ffc2b0d1-63f7-3b7c-8d17-e56e4e9446ce | -6.85819 | -52.8082 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 856c3626-ddc2-3659-9eb6-33a8384d3aeb | -6.93954 | -42.01379 | 2025-09-01 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7a17f84d-e4c4-395f-ac37-b02afe8cafea | -6.1737 | -43.31757 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 453726e2-9b72-3511-af09-a7524951abfa | -6.51025 | -43.55169 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44724dc8-345a-334a-bec5-5cb6c28e998f | -11.35292 | -43.52903 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d762a2a-5d06-3f7d-a05b-d774b60c2132 | -6.46765 | -42.42785 | 2025-09-01 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 90aa770c-f52c-33b0-8556-4f2e07097c67 | -11.32266 | -43.47304 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90270baa-5f60-373f-9030-8b7370feb4db | -11.02153 | -46.99143 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dbeac722-e318-3ba1-a335-48638e49c12f | -11.03672 | -45.14101 | 2025-09-01 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 253c6487-55c8-3b44-b24c-365187ec8ba5 | -9.22324 | -47.11102 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1240f789-2e4a-3eb6-9af0-fcbec309bcd7 | -11.37184 | -43.64641 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4d9a591-42c7-38c5-8772-0f161d91aef8 | -11.46064 | -46.79741 | 2025-09-01 04:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 595388c2-25c5-3175-9c45-1d0efd0d7630 | -11.0263 | -46.98708 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cf38d6d2-4ee7-30d1-9886-47d25ea19983 | -6.28831 | -43.30165 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6bd710a-8d59-3b07-ae62-5adf5752f0aa | -10.6795 | -51.56631 | 2025-09-01 04:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84cba8f8-a903-3dc4-bff9-0586eb91ec97 | -9.14142 | -47.94748 | 2025-09-01 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21872631-c2ea-3159-98f6-6d3ec71dc765 | -7.08913 | -44.34533 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 3710aa86-35cc-3674-9307-9dba73a91013 | -8.33812 | -47.43974 | 2025-09-01 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38e3df7c-8cb8-3aa3-b387-695a80f17fcc | -6.29462 | -43.78928 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 575aea87-5300-3b88-a1df-aa412be4e2fb | -11.42767 | -46.91291 | 2025-09-01 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6402a872-9729-3b11-b61d-8df9faf38106 | -5.91713 | -43.44407 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca8c94e0-cc6d-3316-8dc0-9a848cbfbf85 | -6.26415 | -43.53646 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64316552-5045-361f-aa88-2e442491551b | -5.4059 | -42.33921 | 2025-09-01 04:10:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d60507d8-ff02-383c-b5ae-ee25a30dda52 | -6.25818 | -43.38497 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02c1e6fa-3394-3e19-9a49-61656ea26614 | -6.15294 | -44.12593 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71257a20-c861-3c9f-bddf-b38f746a00cd | -6.3426 | -53.43439 | 2025-09-01 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b555d7c-322e-323a-9d62-3f22826266a8 | -7.90172 | -45.85825 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72446beb-6e6c-3b75-a49c-3fa8f662a271 | -7.7281 | -50.25723 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54890232-1436-31cf-acf5-782c840cbe6a | -12.31148 | -45.67632 | 2025-09-01 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e4c3ce3-b6a9-302b-b13b-c39e054b06f9 | -6.33525 | -53.43841 | 2025-09-01 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48cc01f8-a177-384c-a08e-1bc2b56cde46 | -6.15293 | -43.34558 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dee36d3b-2bcd-338e-aaa4-ef3af6b40fea | -6.82497 | -52.81693 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0ae73b00-33b1-31ee-87ea-ceb3c738df8b | -11.02382 | -47.04796 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8a8e1fe-0d25-3071-ad52-aa5f370de129 | -10.05226 | -48.10415 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1a85b0fd-aed4-30ae-8954-0db88d548658 | -6.71269 | -42.24979 | 2025-09-01 04:10:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4dda1f5c-5286-3ad8-8d5d-8475707c0f5e | -6.8643 | -52.80937 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f8564ff-4ad1-3028-ad99-e9a781f92eeb | -7.07652 | -44.35563 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1151bab6-cf41-3214-b215-35282f1e1146 | -11.89363 | -46.73375 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad1db67f-a697-3a8f-b362-27cb15bb0c6e | -7.06783 | -44.34166 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 08e0e6f7-f4b4-3a80-a1e9-0b2b6161fdf5 | -6.57196 | -43.70559 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README39.md)
