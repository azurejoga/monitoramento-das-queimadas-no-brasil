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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df9cf36e-71aa-3758-84b9-f1d0a0cd6c61 | -7.4495 | -49.8715 | 2026-06-30 02:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 83abf35d-dfc1-31ba-89fb-ee7fc66be5e1 | -10.9401 | -43.0355 | 2026-06-30 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 4155030f-640d-3280-934d-4aa44a4e6d2f | -13.2643 | -56.7947 | 2026-06-30 02:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 631529e0-84ff-3f68-b621-5963c5658c07 | -10.9401 | -43.0355 | 2026-06-30 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 233.2 |
| 0f82a8bd-0ac3-3e05-888e-e21f427afb0a | -10.9397 | -43.0593 | 2026-06-30 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| ef86f827-9cf3-39a8-9329-278496515bad | -10.9405 | -43.0117 | 2026-06-30 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 44e8607c-89c9-38d2-812e-537e7f37d1f3 | -7.4306 | -49.8942 | 2026-06-30 03:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 80a8a11f-97fd-3966-b89c-b35edc278772 | -13.2643 | -56.7947 | 2026-06-30 03:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 780d8a4f-1971-3150-8a4c-9da6fd027ff7 | -7.4495 | -49.8715 | 2026-06-30 03:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 2f4b9130-1a30-36ee-b608-ad38aeba149d | -9.6037 | -56.9276 | 2026-06-30 03:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 756e6f4e-5c40-3c82-8990-70d445e4102d | -7.4309 | -49.8729 | 2026-06-30 03:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 3929114b-340e-3196-84ed-aef21503f799 | -7.4309 | -49.8729 | 2026-06-30 03:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 03bf5c38-601f-38b0-a806-96515a231263 | -10.9209 | -43.0384 | 2026-06-30 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| a9df7ad9-7ffd-3b41-b4c9-374d49b8b08f | -10.9401 | -43.0355 | 2026-06-30 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 196.9 |
| b3db7284-ca90-36c6-91f2-a8872522a73c | -10.9397 | -43.0593 | 2026-06-30 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 615fb87d-093a-3b26-bb39-c99046a837fa | -10.9593 | -43.0326 | 2026-06-30 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 7ebe7033-d20c-3f5f-80c0-59ed5396a8ce | -13.2643 | -56.7947 | 2026-06-30 03:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 088d7ab4-7e75-36bf-a395-124dd7a9a2b8 | -7.4309 | -49.8729 | 2026-06-30 03:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 15da9656-7442-3336-af2d-b9d029a35f06 | -10.9401 | -43.0355 | 2026-06-30 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 195.5 |
| 44aece76-1913-3542-85df-72e41f05a25c | -10.9397 | -43.0593 | 2026-06-30 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| d260a187-a5ed-3a28-9798-8059115c3be3 | -13.2643 | -56.7947 | 2026-06-30 03:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 153819b1-1e75-3626-9894-6837564458c6 | -10.9593 | -43.0326 | 2026-06-30 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| c650d7e0-359b-3840-891e-0a79724b65fd | -13.2643 | -56.7947 | 2026-06-30 03:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| b74ed970-5e7b-369c-8744-5d44664a47b6 | -7.4309 | -49.8729 | 2026-06-30 03:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| b6b3b2ef-39bb-32dd-98f5-a02f8d166356 | -10.9401 | -43.0355 | 2026-06-30 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 277.9 |
| d318bbc3-f9ad-3d1d-bfe4-a09f47a6a5ef | -10.9397 | -43.0593 | 2026-06-30 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 2be17393-b9f3-3d31-bddd-4c240303af32 | -8.60357 | -45.9891 | 2026-06-30 03:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c61d5faa-83c7-3321-b70c-4075832770c9 | -4.84294 | -42.92867 | 2026-06-30 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dfd9b0b-6e86-38c3-90f9-43f3829513d2 | -8.5967 | -45.98785 | 2026-06-30 03:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3015fe5-edcc-39f5-9f61-ce2d1b416d04 | -10.93565 | -43.032 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b55d6cfa-3399-33e2-989f-f14adee2110d | -9.19574 | -45.32293 | 2026-06-30 03:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1f21bf62-f390-3f8f-8579-90bf4b8ff3e5 | -10.94549 | -43.04331 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 9b53c601-beed-3c75-9d63-a5e56d4a7ad0 | -10.93929 | -43.04587 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 8fb3352a-6b48-34f1-ac1b-e58123a0cf1d | -10.94043 | -43.03682 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 162669b7-e2da-3c1d-9605-f7eee7d73d29 | -9.19404 | -45.32523 | 2026-06-30 03:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| eea90010-0339-391c-9bc0-66f7037bcfa0 | -9.20119 | -45.32992 | 2026-06-30 03:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8924138a-3175-3519-b119-7b834894ec95 | -8.98673 | -45.71981 | 2026-06-30 03:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a91af893-f176-3c7a-b67f-840f7bf7fccf | -10.94137 | -43.03475 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| fc0fd716-207a-3a3e-8b96-204695f0bf15 | -10.93826 | -43.04794 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| f37b9d7d-e9da-38ab-9bc3-d12f4534ce01 | -10.93898 | -43.04422 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 11b7e14c-a2e2-3e44-818d-e9c514cd970e | -9.19945 | -45.33219 | 2026-06-30 03:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1586f44d-7dc5-3041-8ac1-00236a79d40d | -8.98326 | -45.72515 | 2026-06-30 03:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8100b52e-dd5a-334c-a864-668fedba25fd | -4.84905 | -42.92953 | 2026-06-30 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47e74cbb-b736-3f3b-a796-e0e9becc7868 | -8.59798 | -45.9813 | 2026-06-30 03:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d4e948b8-f3b2-3a68-93a7-5cd886652ee8 | -9.20771 | -45.33131 | 2026-06-30 03:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45d0ec4a-b68a-3af3-ac82-c30940acd61b | -9.19467 | -45.32852 | 2026-06-30 03:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6784e232-2a69-3f87-9152-2fa3e87b5cdf | -7.74469 | -44.18083 | 2026-06-30 03:34:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bf0fe267-80ef-33db-8bbf-2e08c26a7000 | -10.94115 | -43.03315 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 683f6276-8c16-3cc3-a074-8cce983e3ca1 | -10.93493 | -43.03568 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 672c1238-baea-3740-b2ed-51631820ac30 | -9.18163 | -45.32572 | 2026-06-30 03:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24efc4fc-a797-37cd-9acf-f95a6a36db1f | -9.20056 | -45.32661 | 2026-06-30 03:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16e9a8aa-3fc6-3e7f-a812-0840dcf8d92d | -10.93448 | -43.04099 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| d0a1917b-ece0-392e-8f26-f611bcde0fcf | -8.98445 | -45.71907 | 2026-06-30 03:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f1367a4-380c-3109-804f-172952a17153 | -10.9342 | -43.03938 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 6dbee53d-a5a0-3a1f-af56-7ed56b484754 | -9.18815 | -45.32712 | 2026-06-30 03:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 34914322-d56f-3d99-b152-7e32ac2a5681 | -9.19293 | -45.3308 | 2026-06-30 03:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1ed76cb5-b9ca-3487-b654-e36fd774336a | -10.93518 | -43.03727 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 00517691-4291-38df-ba53-56add62f3201 | -10.93859 | -43.04959 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 1f822aae-2612-3952-a6ac-bcf7d38ac3e9 | -9.20709 | -45.32796 | 2026-06-30 03:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f17a760c-88fb-342d-97b5-020641e524b9 | -9.18752 | -45.32386 | 2026-06-30 03:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e2c397a8-465c-3b20-a223-86bb475beb50 | -9.18641 | -45.32942 | 2026-06-30 03:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5afbddc7-0d04-3fa1-8d18-e2778de9f8c4 | -9.20597 | -45.33355 | 2026-06-30 03:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c9e26c6-76d7-31e0-a904-f3a13f693aa0 | -10.94449 | -43.04537 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4fb0273c-0132-3e25-adf5-95b74f01a547 | -10.93587 | -43.03358 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| f75f9078-afcf-3bfc-b8a6-3db79e4631a5 | -7.74375 | -44.18582 | 2026-06-30 03:34:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 20da5461-0dad-3913-bd74-3196bcf2ff79 | -10.94521 | -43.04167 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e297454c-72ee-36ba-b0b8-8a8945e6ae47 | -10.94479 | -43.04702 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 88a8dace-3c94-38d9-9be2-0891136fcae8 | -10.94068 | -43.03844 | 2026-06-30 03:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| df44ebfd-7053-311b-8f1d-e55c447b6adf | -15.70373 | -43.75668 | 2026-06-30 03:36:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d11a058d-4c68-3036-8530-8de26775e09c | -16.75197 | -45.8187 | 2026-06-30 03:36:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b466c439-061d-37ba-b033-770e99c7331d | -12.84625 | -44.36039 | 2026-06-30 03:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d621cb7-cf65-3555-8f5f-f784e1e174c9 | -11.91245 | -43.398 | 2026-06-30 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf30cb57-8e7d-33e6-af95-4800bd709ff2 | -11.91944 | -43.39168 | 2026-06-30 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6be55e8e-d057-3d55-8820-a7008cef4d59 | -12.85061 | -44.39631 | 2026-06-30 03:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 620510d7-0d5f-37d9-a736-692f564064af | -15.75717 | -42.53927 | 2026-06-30 03:36:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bca2e17-e3ee-34cc-94db-fbe27f1c1633 | -12.8552 | -44.34417 | 2026-06-30 03:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dafc9237-7f80-3ad5-9050-dc0232c6c981 | -11.91871 | -43.39544 | 2026-06-30 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| aab12708-0d85-3b5d-b29d-a37db9b040d5 | -12.85618 | -44.34053 | 2026-06-30 03:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f0004d86-45d9-341a-b72b-5713f2eaf435 | -12.85606 | -44.33997 | 2026-06-30 03:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1b53f528-1e79-3715-ae35-ac11f6ec8706 | -12.85536 | -44.34474 | 2026-06-30 03:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa81bdeb-5170-35b3-87a7-3e50685053f3 | -17.43927 | -47.16979 | 2026-06-30 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4314cdcc-5689-3a8f-8abe-b46d59404ba5 | -22.17151 | -45.1005 | 2026-06-30 03:38:00 | NOAA-20 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 62f8c130-2f71-3811-bdd7-a1f80d9192b0 | -17.43868 | -47.16074 | 2026-06-30 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bacefb84-845b-3c81-a91b-1dd05317166e | -22.79015 | -49.3452 | 2026-06-30 03:38:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1365208-52b5-3834-be80-834ba2428083 | -17.71404 | -46.77794 | 2026-06-30 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0e685f7-8f39-3e4c-97c4-05e87239a332 | -22.7835 | -49.34585 | 2026-06-30 03:38:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 196b4628-ee3c-33bf-9b8d-91ac6d7d1b82 | -17.44369 | -47.16801 | 2026-06-30 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 816290af-4327-3390-b0ab-c38fcb13a595 | -17.70562 | -46.78688 | 2026-06-30 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4db125d2-81b4-3344-8175-a696bac1d317 | -19.73949 | -44.00035 | 2026-06-30 03:38:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a1167a8-2d62-31e9-ac32-52c4f55ee7a9 | -17.71294 | -46.78292 | 2026-06-30 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 21d9fb22-40e3-3bef-b45c-5b370b081f7f | -17.70675 | -46.78179 | 2026-06-30 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c050e6b0-2ccf-3bb3-9a5e-241baa7493ed | -17.43747 | -47.16619 | 2026-06-30 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 529192ca-267f-39ae-a543-773750d5dba8 | -17.71065 | -46.79326 | 2026-06-30 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d7619728-75b4-3ef0-be58-73bf0214fe8c | -17.70786 | -46.77678 | 2026-06-30 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 85944161-a2a3-3bd1-bdd0-775edd8a4300 | -19.73884 | -44.00348 | 2026-06-30 03:38:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b1d1223-8680-3b71-b857-3163bf060400 | -22.17081 | -45.10367 | 2026-06-30 03:38:00 | NOAA-20 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| de3e3c1f-6891-3bf6-83c3-a8583ec00263 | -17.7118 | -46.78806 | 2026-06-30 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8aff2f61-ab97-35a8-a76f-384d43899a23 | -17.70058 | -46.7806 | 2026-06-30 03:38:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d7597c2-feb2-3cc2-b9c0-a37e3454aa9e | -17.79109 | -42.5147 | 2026-06-30 03:38:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4cd65ecd-9fde-3717-9674-b637b09ccc8e | -17.4405 | -47.16439 | 2026-06-30 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README5.md)
