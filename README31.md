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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 816f77ea-7db7-3113-9c63-0bed1d57e620 | -5.65134 | -43.36708 | 2025-08-21 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20273773-8a49-34e4-b7bf-34b0ddf37ea6 | -6.4909 | -43.10507 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3e64801-5004-396d-92a7-d9b84a964ff8 | -13.01649 | -45.18233 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cde8f232-3c78-344d-843a-d15b180f58f6 | -8.36113 | -47.49911 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99e23a52-d120-32d5-8631-537f8ac76919 | -6.07538 | -44.12849 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 066ac65e-2d3c-3bd1-a4fc-20245e80e56a | -12.64454 | -46.89642 | 2025-08-21 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d24c2ecb-9552-3ac2-8fa2-70ee06d45126 | -7.70573 | -44.02479 | 2025-08-21 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b7c716e7-9c88-3444-8c49-d7fc4da2235f | -9.1071 | -45.17767 | 2025-08-21 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf0cadf6-3408-3f33-b70f-f58cc922596d | -13.39148 | -42.04737 | 2025-08-21 04:17:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e329aa55-5843-3236-86d7-eefaa5c75002 | -12.64144 | -46.87174 | 2025-08-21 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1308417-19f1-3b8f-8f77-3385cb66ac59 | -7.14688 | -44.17806 | 2025-08-21 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c912264-aaa0-3a5e-8b55-d0d0160a7405 | -11.81878 | -50.6487 | 2025-08-21 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32b8695f-eafe-3c6f-98ce-e459f344585c | -13.02144 | -45.19417 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 12afe33f-376a-3d85-a371-f048039bb0b6 | -6.2972 | -43.87956 | 2025-08-21 04:17:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11a5d459-4ad1-3e45-b925-a0b63b049956 | -6.95884 | -42.8626 | 2025-08-21 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5d58fc30-c233-35e5-8c94-c0ba80f9ac8a | -5.10473 | -46.17997 | 2025-08-21 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 769d3159-934a-3e65-a2bb-9bca97bf18b5 | -11.17659 | -46.13935 | 2025-08-21 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1efa1d24-77b3-380f-ab3f-4d434aee7b8b | -6.21838 | -43.33564 | 2025-08-21 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce41093e-1d06-3140-b869-6ec714ddc894 | -6.2007 | -43.56845 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 72251102-9db4-3c4e-ae15-1cac2f533061 | -12.64625 | -46.86458 | 2025-08-21 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c60ccd5-16a0-38a8-9fc9-8f7942444e42 | -6.85784 | -44.41465 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7624adf-82ca-3dd2-8a6f-19573f997533 | -8.37827 | -55.00138 | 2025-08-21 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1398bc3-5c9d-37a6-8f90-7e972d4f73dd | -6.34144 | -43.43041 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80d63793-f614-31c5-9129-3a62fb0e6c1d | -9.86752 | -45.97846 | 2025-08-21 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed1f6705-d2e2-3f50-9394-462d8ccc1c56 | -6.94043 | -44.3797 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d497bf1f-6862-3cfd-b40b-964073281ffd | -6.95456 | -44.17706 | 2025-08-21 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a3f1f2d-d525-34bf-9213-3797b1684ed1 | -7.28287 | -49.39579 | 2025-08-21 04:17:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a99b9918-39f4-3e80-8c01-1c3014815fee | -6.28658 | -43.88154 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 142f041c-a72c-365e-a185-67e6522d509b | -6.52964 | -45.45982 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e7f98c7-a0a7-38b8-b21f-4e916d6ec52a | -7.0264 | -44.62669 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| a3f7ea95-7539-3518-bd63-be517f31f33c | -8.09519 | -42.35154 | 2025-08-21 04:17:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b1777f53-bf54-3732-a34f-27340a8b4fce | -12.08712 | -47.90359 | 2025-08-21 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b979083-c2c1-39a9-9dd4-f883107cea9e | -12.98346 | -45.2172 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 051893be-17b0-339e-b84a-aa0a4de3fbf3 | -7.01961 | -44.62556 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 0a7cce2a-efc3-32ea-925a-f21c0616c776 | -8.17024 | -47.33065 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 282a437b-00fd-3eae-b345-1515f1d01113 | -11.02454 | -44.60008 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 296a51dc-7ca2-3732-858f-872b61c0bf05 | -9.86689 | -45.98232 | 2025-08-21 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81a6b519-c047-32c2-85c2-5da9a7ce9d83 | -11.90834 | -44.87596 | 2025-08-21 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cacaad53-246a-3d28-8754-69b9f40e0a83 | -6.74246 | -43.93284 | 2025-08-21 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dccd3726-d5c5-3e2c-8420-cc5c4e71d4ec | -6.10764 | -45.90431 | 2025-08-21 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 013a2ced-ffd6-346d-abf3-4d9180963fb2 | -6.56532 | -44.12532 | 2025-08-21 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb8c84d5-fd08-3bd1-9da6-228a132dd801 | -6.16412 | -42.71217 | 2025-08-21 04:17:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9787c7d7-a0db-3ad7-a6a3-21fd2f5aeb96 | -7.64197 | -45.25275 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3c2d17e-6d78-3291-a9ea-1e100c9bcf42 | -8.38256 | -44.59932 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4084686-d0de-3e26-9935-ed3bb85adccc | -5.99582 | -42.81367 | 2025-08-21 04:17:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d2579467-c155-39d2-9d85-91c271e8c30a | -6.21561 | -43.33164 | 2025-08-21 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0eb839d5-09c4-3893-b942-7c730d048e0f | -6.49145 | -43.1016 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1865272e-528d-3544-9843-99a60e67c423 | -6.08215 | -43.44613 | 2025-08-21 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c55cb88d-968a-3a7a-8154-cbc3f4586eef | -6.94778 | -42.86797 | 2025-08-21 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c08e8902-3abb-3625-a1cd-0985078e7bde | -7.15023 | -44.17863 | 2025-08-21 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bba4580-32a0-3734-9d00-dd7493b73e71 | -7.61823 | -45.26829 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e955c87-924c-397d-81ee-e2b16d8cd0f8 | -6.43124 | -45.48836 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3504351c-451c-3568-ae0f-8b43f020d78a | -6.00587 | -42.85785 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 30063c01-e365-368a-9dfc-3df5efdf4f03 | -5.96892 | -44.13741 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e2a6bc7-4e7e-33b4-92d0-0c0754e2ed01 | -6.36188 | -43.25889 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b678292-bd96-3480-86bb-c5b492fb67c1 | -6.0731 | -44.14281 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e400cf3-2871-3108-8013-d62d92e03a4f | -8.06388 | -43.00128 | 2025-08-21 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b2e64f44-26f9-3456-8816-88b1cbaa5cd0 | -11.81443 | -44.25475 | 2025-08-21 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8bd35bb4-7362-3d0c-9507-53142cbea781 | -12.0831 | -47.91481 | 2025-08-21 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e401d47-24f6-35be-a229-29c31b8f9724 | -9.29674 | -48.42199 | 2025-08-21 04:17:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18d555ce-905f-34cb-b0e0-7b74c0236bf9 | -5.86378 | -43.43626 | 2025-08-21 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5aa3cfd8-0937-3d3c-835e-890c7687f129 | -10.72761 | -48.24018 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11de3344-52b9-3c42-b543-f2f128bddc95 | -7.18971 | -45.17369 | 2025-08-21 04:17:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 007eb2bd-af77-3945-86e1-b19ff8975beb | -6.26515 | -43.72239 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00fb1da1-caad-3e9d-9ce0-51a8b27621a0 | -9.66553 | -48.38172 | 2025-08-21 04:17:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4bf83e19-4319-3878-8543-a8f5a2250037 | -6.49544 | -42.97427 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cfab7525-9e50-3a8f-b938-035097fad44b | -10.28313 | -46.76245 | 2025-08-21 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dfd5583e-a73a-3120-92b8-10f4c0881e6e | -12.64804 | -46.89706 | 2025-08-21 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 292f2815-16c6-3a89-bc59-045fbd30dc80 | -6.08442 | -44.42169 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 008f4728-03cc-328d-a18d-0cee88e18365 | -7.3839 | -44.27422 | 2025-08-21 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cdbd496-adc1-388d-a1e3-7cebf4dec1a6 | -6.9529 | -44.16584 | 2025-08-21 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 190fcf1c-71ff-3e82-a582-bff4a63fa6ab | -5.6683 | -43.51294 | 2025-08-21 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65238e43-3481-3a93-8a08-3405817f59ba | -5.97223 | -44.16008 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aae2ce5d-f117-37a2-8e6c-c6bc48df77f1 | -13.01707 | -45.17876 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 74526f44-61cc-3e82-b216-d5081b7759e0 | -7.12258 | -44.6575 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8a375f0-0dd6-3a26-b734-838639bce918 | -7.23271 | -44.71238 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b6f42a2-bf7a-366b-a847-28c0b9483f6a | -6.58676 | -44.47205 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ee94a2c-4189-3414-89b3-7ba783014f38 | -12.08788 | -44.72277 | 2025-08-21 04:17:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8228c51-e300-39af-8800-7d2c72b79545 | -6.73122 | -43.98177 | 2025-08-21 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35fd6ef8-f577-3866-8a55-8b7b0e5348c0 | -9.86405 | -45.97786 | 2025-08-21 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd8489cf-d5f5-3361-9136-af3115210012 | -6.01429 | -44.35889 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bde94be1-4963-3fe8-b191-faa52f0ce362 | -7.02359 | -44.6225 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| cb720bd7-ec7b-3822-86b0-d8237a0e57d2 | -7.02418 | -44.61889 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 9ded978d-8719-3b7e-bdd3-dc9f24b19dc8 | -13.02087 | -45.19775 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 450d65e9-93ff-3298-a3fa-8fc4460286c1 | -12.98403 | -45.21362 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c7f09116-d9c1-3e19-973c-6215862c8261 | -5.66886 | -43.50944 | 2025-08-21 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8074d01a-4cf8-38d4-a650-2cdd2cacb810 | -10.7169 | -48.23319 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fa2bcaac-36e9-38db-b2d1-107e231049dd | -10.72293 | -48.24449 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94776b92-875f-3562-a3a7-a9f2c50e5390 | -12.64387 | -46.90044 | 2025-08-21 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1149b4f2-87a3-3816-a535-3f2817f12cd5 | -5.78815 | -43.61084 | 2025-08-21 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8f0ad11-053f-324d-a23b-7c306c7fa4d5 | -12.51229 | -47.91979 | 2025-08-21 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce9091e9-d25f-3691-ad0f-a13fb2543a18 | -6.0642 | -44.11193 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6b8f036-f957-3914-9dd5-1620a32dc862 | -8.83457 | -52.03597 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7157fb6-0151-3e88-82b7-95c91f16b497 | -12.97967 | -45.1982 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bafbcb5-570c-31d6-8b07-b068c639069f | -6.1669 | -42.71616 | 2025-08-21 04:17:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 414c831e-1bfd-3b6b-9a4b-60ab10fbd378 | -5.98918 | -42.81263 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e8d22170-0f93-3f7b-bcda-860a9e7cfce0 | -7.24778 | -50.16127 | 2025-08-21 04:17:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d608482-818c-39e0-947f-97e969998ef4 | -5.59329 | -44.21808 | 2025-08-21 04:17:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64d94fce-e5a9-334e-81c7-58781b7b04c8 | -10.39153 | -42.57818 | 2025-08-21 04:17:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 173ac876-3216-31f7-8c39-bdc0e9d846ac | -7.28297 | -49.39529 | 2025-08-21 04:17:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README32.md)
