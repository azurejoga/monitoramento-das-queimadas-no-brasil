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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3ca35a3-cd3f-3cc9-b29a-3c45438b9374 | -6.23648 | -44.44962 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44780738-6b7b-3505-b049-8cfbdbe255c4 | -5.11304 | -43.21265 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0c97138f-bd6c-35b3-910f-0be614395a9b | -6.96978 | -42.86852 | 2025-08-20 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 952b587e-2f54-3b37-8dee-7716bcc414b6 | -6.00856 | -44.28886 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bcbd77f-242c-3c0a-99ca-4f350010ec18 | -5.98101 | -44.14717 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9db442e1-3a5f-3d97-b489-f50b807225ec | -7.63632 | -45.27087 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad91d076-7a99-371c-b982-4db870d42baa | -5.87762 | -48.12511 | 2025-08-20 04:08:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| acf42483-75a2-3612-bc94-1ebb01af5d25 | -8.03189 | -47.67366 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| de6ed487-fd23-3b16-87c6-207b1d5612bb | -7.22698 | -44.69692 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ac49c85-ea0f-3906-bf32-6ea0e6c721bd | -8.83034 | -52.03887 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a741846d-29f9-3348-a5ce-445ab69f3921 | -6.05356 | -44.1427 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de505a3b-26d1-31e4-9f7c-cf37f212d604 | -6.36931 | -43.26407 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e56cc8eb-4962-356b-9d77-d2cfc4200048 | -7.02632 | -44.59207 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b1614b0-7238-382b-a12c-e1f8069111de | -6.96922 | -42.87205 | 2025-08-20 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 32d4be40-a1a4-3d81-8f65-e35a22b309db | -10.31234 | -46.67788 | 2025-08-20 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89364cc7-c99b-3001-9b05-d9509d4b92a3 | -7.63338 | -45.26616 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8e8e8ae-8165-3de4-84b4-ec258e265041 | -6.0101 | -42.82826 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 67b64596-8563-3885-b339-1ab910cee15d | -7.64583 | -45.28094 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01221a87-8df6-3ec8-a6cf-205879f56f03 | -6.02307 | -44.35646 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e51e7f9c-e830-317d-8eb1-ad67579f600e | -10.12426 | -47.43124 | 2025-08-20 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bad2e94c-d170-34a6-ac13-90496aee539e | -7.58933 | -45.41811 | 2025-08-20 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28460f22-c0b5-3406-967d-8c2b7ed93774 | -4.00291 | -47.09212 | 2025-08-20 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce33d38b-710f-32c1-a0e2-74678bc83331 | -6.5469 | -43.00517 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 546f260a-1fc4-32b9-af8d-2b8c1c58ec6f | -5.65974 | -43.50669 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68107170-55be-3228-9309-0fafd90a7676 | -7.5998 | -44.39068 | 2025-08-20 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6704b5d0-af5e-3102-9a88-205022d59a05 | -7.2793 | -50.18674 | 2025-08-20 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b9308ef-cd5b-3063-8f57-3de233b0028f | -8.83435 | -52.04683 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9755978e-d182-30ab-bb5f-ec96f4f95de1 | -9.0263 | -45.10202 | 2025-08-20 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4a8cad6-b78e-3600-bb6e-58f7cbfe853c | -7.65366 | -45.25621 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04d62603-226d-32e5-b849-ba9752e3a68e | -6.76498 | -44.34458 | 2025-08-20 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03b562a7-06db-31e9-b722-d1da7e59d2ff | -6.73421 | -41.5344 | 2025-08-20 04:08:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 30504a50-d4cf-3507-99df-15e2a4f5af22 | -6.95008 | -43.78222 | 2025-08-20 04:08:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70c92f15-15d0-3a65-9596-05fd86fc92a5 | -8.83015 | -52.03888 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ff6d235-6a91-3017-b897-428820f21fd1 | -8.7948 | -45.47981 | 2025-08-20 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2f98953e-2649-3e55-b7df-a1312cee204d | -6.73181 | -43.98402 | 2025-08-20 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9510a77e-d55e-37fc-982a-0ab14251065e | -8.7925 | -45.47884 | 2025-08-20 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1beef0e3-c433-3335-bf30-f3e6372ef53c | -6.06782 | -44.12067 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee0c7ecc-d360-31c8-8371-8faa8c51bd49 | -7.14158 | -44.18878 | 2025-08-20 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c80f49f-b133-321f-b103-efad4d833e7d | -6.86368 | -43.59795 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d800333c-4e54-3337-b336-e0f9d77c936a | -6.54298 | -43.00821 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a397776f-5713-3087-8964-6162cde5bab2 | -5.11587 | -43.21685 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 876edb73-6ec8-30e2-8cae-6484722882cc | -7.65379 | -45.27785 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81112a90-cdc5-377f-8f97-ebe12fab7acb | -7.12655 | -44.6447 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee4896d9-5a24-31d8-bf11-9835e1942d99 | -6.03452 | -44.35336 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c67171b-5d57-3669-9f9a-39deeaffebe7 | -7.63679 | -46.22054 | 2025-08-20 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c911de32-67e7-315e-b363-0555158246e8 | -7.65016 | -45.27729 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 277db8f5-f76d-387d-9f81-f2c398a30ae8 | -5.9855 | -42.83172 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fe7f89cb-2715-3948-b3dd-134b1f21a9e6 | -8.30155 | -47.61759 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5fcedfac-d5a1-392b-b204-748575085159 | -6.44645 | -45.49912 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20a2acc6-426c-3b64-bf7f-c3a1440ef32c | -4.39137 | -47.77185 | 2025-08-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f135c1e9-98db-3a8e-98fd-d35b9e13fe6b | -7.73462 | -44.01387 | 2025-08-20 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae190636-e896-3fae-9636-b41cba95e049 | -6.16486 | -42.71113 | 2025-08-20 04:08:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c8092e2d-ecd1-3850-bf47-40e0d78cc4d7 | -6.86131 | -43.6127 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1bcf658a-5731-30ec-9863-48e8db66b1e1 | -4.90984 | -43.23394 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 781c8ba0-0e50-35a3-9662-49ddb257304b | -2.83406 | -49.14533 | 2025-08-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5197dcb9-8e08-3cbc-a2a3-322e1b64fdae | -7.6993 | -44.01552 | 2025-08-20 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 236ed242-a8b8-35ac-a19e-d74ea9d1fdfe | -7.64289 | -45.27616 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68d03f21-248f-3ff4-a7b2-15a0e621d1ff | -5.87437 | -50.14886 | 2025-08-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3e2efd5-c7a3-3266-8d62-abfcc8dd7b60 | -7.39076 | -44.27107 | 2025-08-20 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 558d1291-7ba6-3ee0-960f-f19ccf24be60 | -6.27052 | -43.70515 | 2025-08-20 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33497595-666f-3769-b0bc-35b4ccd893b2 | -7.64078 | -45.28884 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dfccfa4-f216-3e6d-a03e-e459955b1427 | -6.02661 | -44.35699 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aae7b462-8368-3e51-a6ec-53a3a790112f | -8.07095 | -43.6691 | 2025-08-20 04:08:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc17354e-8a4f-366f-b6e4-3d0ddfb22033 | -6.57039 | -43.00888 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a003cc2f-de87-33d4-82f2-55c127d38bac | -8.82542 | -52.03461 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 34b1c836-a112-36b3-aec1-a44b9251db93 | -6.42505 | -41.85667 | 2025-08-20 04:08:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 07570745-f5d0-3290-9b2a-6ba298f245f8 | -8.82948 | -52.04242 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6c457a4-1503-3f82-93a7-e69e7dabc4c9 | -5.88241 | -46.50636 | 2025-08-20 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 060d39a0-4fa5-36db-85a1-da34eed036ac | -10.34368 | -44.90768 | 2025-08-20 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67bf2b47-20b1-3aae-bf46-7a011c68ed3f | -5.28441 | -44.19014 | 2025-08-20 04:08:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 917aa517-fee5-3c07-9cdb-9082a4ac1955 | -5.78388 | -43.71912 | 2025-08-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcfd0b26-c9bc-3648-89b8-00ea370ee343 | -6.52284 | -45.46365 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b17575f5-b37e-3f13-84b6-f8cf0ed93211 | -7.22988 | -44.70146 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0784bebd-135f-3981-be3d-eccb72bccf15 | -7.84516 | -45.11437 | 2025-08-20 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f83e6fa8-1483-3284-be70-d49302c75ae7 | -8.02419 | -47.66851 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 78bf2316-2534-3a1a-b3b2-956ba86d0b06 | -5.68144 | -44.96891 | 2025-08-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8dbb317-4ad1-36b6-9d02-1ed6d3495f30 | -10.24012 | -37.43409 | 2025-08-20 04:08:00 | NOAA-21 | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df17c104-e08c-3505-a4b1-4b5abb9f87be | -5.78299 | -43.89408 | 2025-08-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a8ee7871-4fb4-332f-9313-7bd19b6a57ec | -4.6757 | -43.62112 | 2025-08-20 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 205d72c7-6c07-36c3-8a00-a2d13015205d | -6.13002 | -42.95335 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| e5b7a6bd-4e07-3b28-86d8-70d19670a3fe | -5.64814 | -43.37968 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b4be630-5f3e-3eea-a3ef-a357e2e2df08 | -3.87619 | -40.45124 | 2025-08-20 04:08:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5afd3de9-c316-3ccc-b645-70e98447c22d | -5.98608 | -42.82813 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1f9ee948-0c1c-3fa7-9af3-d0e81d6b0cdd | -8.02968 | -47.66149 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6e5b7403-bd93-3854-8604-da6b523c528a | -5.98581 | -44.13973 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5fe11219-b250-33e5-b338-33c9291f3a11 | -7.64149 | -45.2846 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef6ba38e-04de-3e0d-a120-93d57b540fd2 | -6.45092 | -45.4952 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0a49079e-41bf-3b8f-87eb-a8680b00de74 | -7.11881 | -44.64758 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 526108c4-39de-3e11-8640-5379f16b4ef5 | -6.00005 | -42.82664 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d18bd79f-5cd5-3552-827a-7be96541d1c3 | -4.91044 | -43.23024 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f610e540-9bd4-3668-91ac-3a564c2d5290 | -5.48169 | -42.16823 | 2025-08-20 04:08:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 73e6b861-176f-35dc-ab7f-beb0167c079c | -3.6889 | -44.20802 | 2025-08-20 04:08:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83b87d1b-eb79-3ddc-96ef-8f023906e7af | -6.06494 | -44.11623 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5f21f46-8164-3baa-8bf6-43b60eeb9a59 | -6.86709 | -43.59847 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e4915f0-5082-37a2-b0e3-207e43653f7a | -8.0332 | -47.66599 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3d218e90-c907-3742-ba26-32ae12d73b3b | -7.58873 | -44.39281 | 2025-08-20 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 906e20b1-723e-3cb2-9440-f79cfb9c4600 | -5.63497 | -43.39662 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22a9d07c-985a-3dfd-a0e7-398f17678619 | -5.69205 | -43.54636 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ed93df4-1b70-3f9d-8900-47bbd99a403e | -5.87391 | -48.12003 | 2025-08-20 04:08:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38d91503-69d5-3f7a-bbce-419a549b446f | -7.96913 | -55.29658 | 2025-08-20 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README13.md)
