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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60286825-8c03-3eb8-8a27-5d42fc3adc85 | -7.3807 | -46.24442 | 2026-10-08 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95ecf9b5-f1ea-37ae-99f5-0d38ebc69bea | -3.35015 | -50.4788 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6b121140-55df-3fce-ae91-efd48e19b82e | -10.46609 | -47.24321 | 2026-10-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 86e3b1b3-f71a-3898-9ef0-a8822bf2ba0f | -6.97986 | -40.03002 | 2026-10-08 04:02:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b3f0fa51-099b-335b-8914-ba3085809fa7 | -9.45372 | -44.61887 | 2026-10-08 04:02:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 445bcb23-dfcc-3eeb-8654-fb6ed658b532 | -6.38014 | -42.52975 | 2026-10-08 04:02:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e1a31640-e427-331f-8706-89bb8fe1fc2b | -7.20374 | -45.35826 | 2026-10-08 04:02:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 625bda39-6f41-342f-b25a-2c7c3813a299 | -7.22275 | -44.28046 | 2026-10-08 04:02:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3656d27e-a0a7-36e8-a423-d212b3152544 | -5.72716 | -45.15321 | 2026-10-08 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9b9404a2-99a1-33f0-9bb0-376b19b39d09 | -9.02516 | -46.9121 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 974a747c-ff02-35c7-90ba-c6b2ddde5360 | -4.30392 | -50.78698 | 2026-10-08 04:02:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5dbb25b7-8462-3128-a2db-330b51a99d05 | -8.72908 | -45.15948 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fbc13fb3-6418-36f4-81f7-e25a802779ae | -4.26249 | -46.39651 | 2026-10-08 04:02:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be0cac80-d6dd-38f6-b8a0-73281db33ffa | -8.87795 | -45.60025 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 156f7684-fa15-3b25-8593-b1f4adda91fb | -5.74295 | -45.14892 | 2026-10-08 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e5b5beda-f7db-3444-af74-fd7b18ba0723 | -6.84539 | -39.55636 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 03a10686-54ed-3cb2-8ad7-96375eb90df2 | -7.20918 | -44.33408 | 2026-10-08 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b35bb0fa-b1d6-30ff-a4b4-199e5a80d1ab | -6.83595 | -39.55125 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 96b4c46b-72ae-3421-a0b2-c8df274b5c9c | -9.39979 | -49.01252 | 2026-10-08 04:02:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b66b7f16-dc0d-3419-85e1-28cb3b4c086b | -7.62821 | -45.38348 | 2026-10-08 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c8df339-80ef-3fab-a4bf-5e465186514d | -6.65272 | -47.91112 | 2026-10-08 04:02:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38faf0d0-8d52-3045-803e-52fc95f0884a | -3.17127 | -50.59923 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c18883e4-a4a6-353e-baba-96870ecbfdd2 | -5.96157 | -40.92233 | 2026-10-08 04:02:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e7682f2c-fcd5-33b5-9afc-255ce2076956 | -7.8682 | -44.15107 | 2026-10-08 04:02:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c29a35f5-3024-3fc5-84fb-a8432b130bfa | -7.46214 | -42.85829 | 2026-10-08 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5df75280-9a1d-30bc-9e65-ea2b935ecfbe | -11.62889 | -43.70568 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77fcb29f-ae25-3e48-aa2a-2e5144ac46e2 | -5.7486 | -42.05797 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1ec63eda-d11c-376e-9d28-dda5ed64b429 | -9.90815 | -44.79747 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47b51af6-615f-3306-a9ad-7b7064f4ba88 | -7.2634 | -45.34625 | 2026-10-08 04:02:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9501bbab-a5b6-3f40-bc4d-9f4a7fd63e6d | -6.62842 | -43.72852 | 2026-10-08 04:02:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5123ad74-e5ba-3415-a833-bc2d3c1cf2a7 | -8.21061 | -46.33948 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0454ea67-3bee-34ed-b716-5a3ac682621d | -7.26153 | -39.71639 | 2026-10-08 04:02:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c6dc342c-a4fd-3cdf-8c5d-ff21a85f3fa8 | -4.64321 | -46.33649 | 2026-10-08 04:02:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bc21ea9-2a99-3553-8b91-f40e21b2a7a1 | -4.35319 | -43.80002 | 2026-10-08 04:02:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 6c769675-292b-3b7f-a721-826800ffa9db | -5.71344 | -41.72752 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| edde8c5e-9b3a-3345-bf08-1eaf011c48a9 | -9.1458 | -45.82218 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50ce7a8b-ffb5-3695-800b-7b7f22816cc6 | -11.71945 | -43.65345 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34fe3da4-5838-3389-93ff-0ece45152f6b | -3.86717 | -50.41893 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1ef7a389-5089-3900-b91a-729ae51909f5 | -9.90404 | -44.79666 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d8960636-c634-3603-864e-5ea79b86f792 | -5.04339 | -49.76883 | 2026-10-08 04:02:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f392596-86d7-3dc9-97cd-0faf98d1dc94 | -3.1975 | -50.56702 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 895cf2ff-f283-3d01-bcff-7b6478576392 | -3.25291 | -50.40183 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af6acbe2-6169-3f7e-a511-631127cf92b7 | -10.24488 | -36.33464 | 2026-10-08 04:02:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8e914f13-bed6-3068-8a05-863421c97b9d | -7.14904 | -46.52479 | 2026-10-08 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a5a8dd3-880d-3bc8-8ca3-b1115c4b0b30 | -5.75973 | -42.05978 | 2026-10-08 04:02:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e3a0bf14-ebd5-31ce-8dbc-5b6e13180fce | -5.48554 | -42.86013 | 2026-10-08 04:02:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 28315703-2559-34c7-b329-60e2a3b06417 | -6.59953 | -37.89388 | 2026-10-08 04:02:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 31dcbe6c-ca17-33f8-9531-31356527bf53 | -10.77827 | -46.55702 | 2026-10-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c30a97da-7e0f-3070-b342-88fa2b19f05d | -5.23558 | -38.54983 | 2026-10-08 04:02:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 23c53033-917c-3182-b18d-b1e175911c24 | -6.59677 | -37.88982 | 2026-10-08 04:02:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d4dfd5fd-d9b0-3576-b71e-ceb2a45b416a | -7.4639 | -42.82493 | 2026-10-08 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 78d1640e-ff9e-3482-a4c6-39f4fab1e56d | -11.62969 | -43.70102 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1cd1b60e-a25f-359d-8ec1-2c371e286157 | -8.23498 | -48.58482 | 2026-10-08 04:02:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1e1c8d5-d067-3ec3-ad4b-9fc09b199a15 | -6.8773 | -43.69044 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4fd29f12-b18b-38b6-9a51-46670d376e37 | -8.21386 | -46.37625 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f8c83ab7-e029-3fc9-bc19-a974e41ace9a | -11.63048 | -43.69632 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c0fa01e0-383a-31f5-aa8e-b7f533b7f760 | -6.63069 | -43.73996 | 2026-10-08 04:02:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 48206e76-d364-351e-9154-ef0db976daa1 | -8.73053 | -45.15117 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 85fa454a-13fb-39c0-b8cc-24b9e500a861 | -11.62516 | -43.70488 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 014c0090-07eb-383d-b3f9-1772d7591e08 | -4.34898 | -43.79926 | 2026-10-08 04:02:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3aefbeab-bbe9-3fe9-be69-ed8bd13188d2 | -11.26513 | -45.18696 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43c38252-d075-32d6-b41a-be4787164bd4 | -5.4517 | -42.89419 | 2026-10-08 04:02:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dde651ce-aba3-34a0-95bc-e163ec5829f8 | -7.59245 | -45.29947 | 2026-10-08 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9431af88-f3f7-322f-b1a1-0e2bde1888b4 | -6.98879 | -40.03882 | 2026-10-08 04:02:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 28b6fdad-01e0-3f8e-b336-c181f56b88d4 | -6.88133 | -43.69107 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cc7c0fbe-2767-36a2-b527-883e5cd8ded3 | -8.29002 | -50.26994 | 2026-10-08 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 12f910fa-857e-3657-bf8f-691ab3afe6db | -8.7247 | -45.18452 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 96d9d8a8-526d-35d2-9d77-244edd586e8e | -5.71441 | -41.76716 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 53a99e8b-4313-324e-97c6-2c76fda7b37d | -7.47132 | -42.85014 | 2026-10-08 04:02:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6c34756d-1243-3f90-b4d6-bb6a6b07de69 | -8.71318 | -45.19952 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81ecacfd-9aa0-3a78-a77c-e03f72c80654 | -6.63306 | -43.72566 | 2026-10-08 04:02:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 16774fa3-3f93-3a54-930a-b1a5ae9eb642 | -5.67485 | -46.35238 | 2026-10-08 04:02:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4445e904-dea6-3ae1-b1a6-f6f61ebcf9ab | -5.73545 | -45.15936 | 2026-10-08 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 556928c9-0de6-399a-9ce1-256e2e66da35 | -7.02922 | -45.44545 | 2026-10-08 04:02:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ce2e0f3-9392-3acf-beab-d81a02d964a4 | -9.25505 | -45.63934 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f25b3fe6-a212-37f2-b405-8c69edc33f17 | -3.20521 | -50.56227 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2365d2a9-a8d0-3cc6-a133-367294ac1c08 | -11.77463 | -43.53236 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce52850a-49df-3697-944b-99b2139673d0 | -10.83595 | -48.13492 | 2026-10-08 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 702f3a0a-920f-3908-8016-001895dc9a06 | -7.77462 | -43.81488 | 2026-10-08 04:02:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8690d225-8fa0-3a15-b2e0-6040431e5963 | -8.98769 | -45.91833 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9868064c-f551-35f5-a57b-59b2f65d0398 | -3.8508 | -44.89559 | 2026-10-08 04:02:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55bf612e-f714-33d9-b727-dc9eccd044c3 | -5.49027 | -42.85587 | 2026-10-08 04:02:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 92d4bbbe-aaf0-3bc1-b706-27835ff4652d | -10.46708 | -47.23797 | 2026-10-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7739bfa0-155c-3148-82be-64689f9d184f | -5.17372 | -45.34061 | 2026-10-08 04:02:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea5b4d2c-54a5-3613-b4ff-f180a22ff58b | -9.89315 | -44.81042 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5270a62a-9f1c-3a46-a786-4317b98e8987 | -9.89728 | -44.81112 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 800e5991-9c4d-31c7-ab9a-3e1a3d546fbe | -7.87087 | -44.15483 | 2026-10-08 04:02:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99363c6b-f828-3c9d-b5c7-e3fabe0af9c4 | -3.34352 | -50.47755 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2582422f-e244-3b1d-8abc-09fb95652a4b | -7.20984 | -44.33027 | 2026-10-08 04:02:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9d57b6e-0ffc-32ae-8b0b-c29bd235dd96 | -5.24062 | -50.9185 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 003fe270-5fd5-3419-a808-c8584d633f9f | -5.98829 | -40.93456 | 2026-10-08 04:02:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 305a7cf5-c448-339c-b62b-a9e2934a713e | -7.17653 | -52.61757 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf08b592-2ee2-341c-a2d8-bf7c1358933a | -9.13301 | -46.66391 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8c9243f0-0c03-3705-9cfa-c8d2d7d2d808 | -5.73013 | -45.1633 | 2026-10-08 04:02:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b36bd081-4b40-3c96-a07d-c0af69e96ba9 | -4.72665 | -45.66823 | 2026-10-08 04:02:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25b9f69a-b9f9-3d58-947b-9faaf36db0ba | -5.88869 | -35.72747 | 2026-10-08 04:02:00 | NOAA-20 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1fe934b0-439d-39fd-bc2f-1ce2b4cb5b77 | -6.88597 | -43.68818 | 2026-10-08 04:02:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b3e632fa-a1d4-3556-86b3-9b80cc6a7494 | -11.24392 | -44.87603 | 2026-10-08 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 348f9fdc-bc78-3dc3-8685-aafaaf841824 | -3.86167 | -50.41177 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0a9ff324-4e6d-3570-ac99-e4a4eb3d41c4 | -11.2321 | -46.24382 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README66.md)
