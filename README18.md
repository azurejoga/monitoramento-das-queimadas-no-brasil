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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 245418d3-97d2-369d-a8d0-95487f84de88 | -5.78398 | -43.4584 | 2025-06-20 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bfd05ae-f960-3cc3-ba5a-85aadf6baabf | -12.22387 | -45.53086 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf6a99e2-079a-3e91-b40a-ce153f8f5fe3 | -7.38981 | -44.55835 | 2025-06-20 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c290b6b-9a04-38d3-9beb-4808974476e0 | -5.48547 | -42.14406 | 2025-06-20 04:51:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4a231efd-030c-3faf-b17d-9c402f78eef9 | -6.67598 | -44.25105 | 2025-06-20 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24aac6db-a9c8-3f1a-ac86-439144a0145d | -7.02087 | -44.59924 | 2025-06-20 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73ca24a2-434c-3111-a1da-1d19f1289778 | -9.49039 | -56.07781 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e68a1f36-2a49-3a4f-bf4b-11901ce57f5b | -8.12817 | -43.12356 | 2025-06-20 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 338e88b2-49d6-33e1-9407-66bee627480e | -7.38862 | -44.56692 | 2025-06-20 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32d03434-48e0-3247-b22d-3855e88be8b9 | -10.45978 | -47.06062 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 04570702-51e1-389e-a8cc-c6a4fc21a830 | -7.01967 | -44.60792 | 2025-06-20 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c790a565-c856-3ce8-b5df-7735fbe5597c | -8.12763 | -43.12754 | 2025-06-20 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| afe50bc9-5fdf-3275-a0b2-2fd4f0a55997 | -9.92735 | -59.90154 | 2025-06-20 04:51:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de1adce1-69e5-33dc-8803-944a1c7de4a4 | -12.26655 | -44.60465 | 2025-06-20 04:51:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| db3bb8ff-e01c-31a9-8576-52e8b6c8647d | -7.38802 | -45.40876 | 2025-06-20 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 246c6f19-102d-3aac-bb46-3a490aea48ea | -10.73043 | -49.55309 | 2025-06-20 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6a0833ac-c91b-3d47-9a60-73e127293a5b | -11.46928 | -47.29333 | 2025-06-20 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be2e431f-1e22-3f4e-8cf1-c65024c0ae89 | -11.47373 | -47.29396 | 2025-06-20 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 331f633a-ddbb-3d35-8f7e-b71a9e947640 | -9.33164 | -47.83137 | 2025-06-20 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 028791c0-fd4c-3ddd-a9ed-585b6fd6e27a | -4.38194 | -48.07654 | 2025-06-20 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11df0da1-1857-3386-851d-3a476856edd6 | -7.02008 | -44.60498 | 2025-06-20 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3cd2bbe-ea3e-3c44-a7c3-3af7efef6b6a | -12.20828 | -45.53179 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44f5b09a-ad65-3c7e-ad34-f00df44b089e | -9.31412 | -47.79142 | 2025-06-20 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 759fe81d-17b8-3732-be80-2c70cd390d30 | -8.25557 | -44.95739 | 2025-06-20 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ef28e62-5aa9-38c3-968b-a96191a768a7 | -9.87544 | -49.33733 | 2025-06-20 04:51:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ea145b7-f8bf-3157-a41d-df693526d88c | -10.86103 | -53.76849 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ea02144-46dc-33f6-81e6-1c86839a6b65 | -10.16081 | -48.98604 | 2025-06-20 04:51:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5277ffaa-abeb-3278-a89a-0559f1219aea | -9.29872 | -44.72515 | 2025-06-20 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04f349f8-6a2e-32b7-9860-4f158edfcffa | -10.48062 | -47.04105 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| e38b7975-23c8-3d7b-9755-98854e683ef9 | -8.91339 | -49.84948 | 2025-06-20 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58b2fa57-bcc0-30e6-84b2-4319a4d7bf81 | -9.48271 | -56.08062 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8cb48e5e-1a38-3fac-8a61-3dff89bc431e | -6.84923 | -44.28652 | 2025-06-20 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b64d61a3-5659-3ec9-b373-d6d0297de498 | -9.48052 | -56.07212 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 491c831c-83f5-3576-8b9b-248e3bca401a | -8.72488 | -47.98528 | 2025-06-20 04:51:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72c461d8-52ac-365e-8b68-6b932aae32dc | -10.86212 | -53.76151 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d623e2a2-1a56-306d-8c31-1eb7281de447 | -12.21806 | -45.53623 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d07b8a51-64b3-3193-a36e-cf00bced714d | -8.26554 | -44.95877 | 2025-06-20 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a66881f0-fd72-348b-bd65-cb8a2128f1e6 | -11.12951 | -46.67107 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f89969d1-5159-38bc-a867-5fe7caa33cb2 | -9.84798 | -44.70536 | 2025-06-20 04:51:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3c0b0e3-79dd-3bf8-980e-1d33fa49d63c | -10.92844 | -49.27969 | 2025-06-20 04:51:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7d43fbb5-49f5-311f-a8d1-9ecb1cf64c8f | -7.87681 | -47.89375 | 2025-06-20 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c16ce32e-4e6e-3797-a9c8-9141acf6049f | -10.72107 | -45.16093 | 2025-06-20 04:51:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b08e3eb-f8e9-37f7-a487-013bc90cb6ff | -11.4598 | -47.29652 | 2025-06-20 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cc208ee-6c98-32d9-852c-90b95c637269 | -10.36325 | -57.50177 | 2025-06-20 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 076271a9-accd-3aed-a23e-637c8ab94ae0 | -9.95654 | -46.62952 | 2025-06-20 04:51:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 502e1983-dc52-3a90-9a77-5b2c25326c94 | -10.46305 | -48.66156 | 2025-06-20 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e31fb969-fc6f-375d-afec-630721a117fd | -10.86597 | -53.75855 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef28c5e5-a8d6-3964-9508-dd37b09473fa | -7.39337 | -45.40241 | 2025-06-20 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d3bc069-53e5-387d-a6ae-4fc722408130 | -12.21335 | -45.5325 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96d64c37-6189-32c5-a5d0-2cfe1a7e5a09 | -4.54483 | -48.01887 | 2025-06-20 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4346480-4512-30f6-a7a9-0848cb6cdc21 | -4.82237 | -44.35732 | 2025-06-20 04:51:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e377eb78-4618-3ed5-ad5a-53edba01ab07 | -7.3894 | -45.39851 | 2025-06-20 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab50accc-c15a-3650-8bd7-ad294a33aeb0 | -6.67086 | -44.25034 | 2025-06-20 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ab398909-62b4-3df5-81f4-306cb3de92cb | -6.80552 | -44.74839 | 2025-06-20 04:51:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5cdb6e4-a0f7-3a08-8b67-8e823ec5e104 | -6.49334 | -42.84889 | 2025-06-20 04:51:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9676e963-31b9-372d-a0fb-41c153979639 | -10.55855 | -46.95814 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4adaab1-ccac-30f0-8966-1d92d7c14b27 | -10.86487 | -53.76553 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07361a55-49a5-3985-8255-6fd3cc386aee | -6.67168 | -44.24457 | 2025-06-20 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 031f5be4-d4ae-3c12-9727-3463282d761f | -10.86927 | -53.75908 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23f5c7c5-70ea-336e-80c2-260698606c1f | -9.47986 | -56.07608 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1ce46bfc-f3b7-3eef-af6b-d099d25178fe | -12.21917 | -45.52711 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c94903e-40ec-3b78-9d86-e2720ffd778d | -7.23878 | -44.68818 | 2025-06-20 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 712db1fb-3ee1-3688-924b-56955c73ba69 | -7.15825 | -55.45563 | 2025-06-20 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad79cdfc-e25f-3faf-ad6b-659d429e25c6 | -7.5451 | -43.82125 | 2025-06-20 04:51:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69dd2505-4e77-3b1a-8801-2326bde9b38a | -12.21372 | -45.52946 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3320855a-0d4a-3470-bc22-a1a41d3c3198 | -10.9421 | -49.43087 | 2025-06-20 04:51:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 290adb9b-0686-3b05-80c0-145c9332c2bc | -10.54594 | -46.98425 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b476a60-36ca-3125-8db4-1b31a17b2165 | -12.20936 | -45.53232 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20025aac-6c8d-33d4-a5b7-54048418bf8b | -10.4857 | -47.03716 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b351a5b-7e1c-3069-a7d9-7f4049d6f09e | -4.64502 | -47.9668 | 2025-06-20 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62eca209-b45b-3b48-b85a-f1e7c5ec82d1 | -8.64853 | -47.15666 | 2025-06-20 04:51:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3cf8669-4d17-368c-a4dc-bb64a93f482b | -7.60704 | -45.55896 | 2025-06-20 04:51:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad5ac9ba-1af3-3de7-861f-8ede5c1966d4 | -10.48184 | -47.03207 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| a64d6ea0-122c-3735-b546-4fe23a06a228 | -6.67127 | -44.24748 | 2025-06-20 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8645762a-1be4-38ba-8dda-7dbbd5522d9d | -9.30548 | -44.82966 | 2025-06-20 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a08522e6-3355-3271-a99b-135654948fe8 | -9.38241 | -63.42982 | 2025-06-20 04:51:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c7f5e41-0abc-3d30-b13b-ef8e8317b0a2 | -9.49324 | -56.08236 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6084ffc8-a424-344c-b60a-77384be70636 | -9.3146 | -44.72394 | 2025-06-20 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80b43038-452b-3d09-aa76-bed6883ef16c | -8.27013 | -44.96241 | 2025-06-20 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64016fe8-bfb4-3041-8221-c0b417aa5b88 | -10.07761 | -52.7439 | 2025-06-20 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 8efdb124-dbe0-358b-9e28-88df22ec54fb | -10.16151 | -48.98103 | 2025-06-20 04:51:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01c80e07-9405-3d9f-b79b-57693ad7f60c | -7.21242 | -43.06608 | 2025-06-20 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 16e56e54-be42-3ebb-8f16-7bb55b62f3e1 | -9.31467 | -47.78759 | 2025-06-20 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 62bb8651-8b05-3f3a-84e7-10c15c54e5df | -10.47256 | -47.06682 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e47df503-b549-3470-88ca-da492f41515e | -5.49105 | -42.14369 | 2025-06-20 04:51:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3534e26b-6e7f-3a0c-a10b-f2e195cc516e | -10.5271 | -47.58422 | 2025-06-20 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a705c0cf-536a-3d10-b213-233a60b4bfd9 | -11.47432 | -47.28949 | 2025-06-20 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e52a8c1e-278c-3a4a-b14e-af62c432359a | -10.48328 | -47.05485 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 765e8879-d755-3bb2-97ac-243ef8ca24e8 | -10.86321 | -53.75454 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f95271fa-0137-33a8-a34f-0978f108d0d3 | -12.26572 | -44.61154 | 2025-06-20 04:51:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53ca8de5-001d-3d96-b253-159b3aa14ebe | -9.92657 | -59.90274 | 2025-06-20 04:51:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b3265c8-38bf-3ce3-91a8-0b806bfa08eb | -10.45905 | -48.66094 | 2025-06-20 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40a55dfe-b600-3c89-9139-9bb4fb0b8690 | -10.47108 | -47.04431 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 2264e805-79a5-3a2c-b611-ff59ba39beb8 | -5.12664 | -45.02707 | 2025-06-20 04:51:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c817981e-5a84-3004-8038-c7b41fd5761a | -5.49707 | -42.14561 | 2025-06-20 04:51:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| be870457-8f14-31f0-a192-87531b40c6a5 | -9.3358 | -47.83194 | 2025-06-20 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a747e8a6-2e3b-31c0-953f-c6d7dbb5f0d1 | -9.48403 | -56.0727 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 92b25cf5-a60c-36b8-a973-dabfcb5898d8 | -10.83262 | -54.01431 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0499a388-deb1-3215-ab68-a37aed0fe5b5 | -9.87267 | -49.33414 | 2025-06-20 04:51:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8872639b-2a96-3ed9-a1db-b661d83166cb | -9.48622 | -56.08121 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |


[Clique aqui para ver as próximas entradas](README19.md)
