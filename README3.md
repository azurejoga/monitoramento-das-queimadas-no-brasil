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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0949f8f6-7a1c-3fac-8a70-aa8676f15db9 | -10.9593 | -43.0326 | 2026-07-05 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| b4a27dff-6bb3-385e-9f29-cd888bd649fc | -22.1415 | -47.2951 | 2026-07-05 02:40:00 | GOES-19 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.8 |
| e8d72e3d-d825-30e1-a0e8-3456dc322592 | -13.2404 | -54.3303 | 2026-07-05 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 94e6141d-d12f-3c3b-9ddc-7c9b4a100777 | -22.1422 | -47.2711 | 2026-07-05 02:40:00 | GOES-19 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.4 |
| d4681825-429c-3bed-94f9-95224c5e9595 | -22.1206 | -47.3004 | 2026-07-05 02:40:00 | GOES-19 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.1 |
| 7120d993-69b7-3735-bb96-9d0360217f8a | -13.2404 | -54.3303 | 2026-07-05 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| d9950f98-cabc-33ff-9940-bad44e58cf0d | -13.2407 | -54.3096 | 2026-07-05 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 66429e52-cd46-3b69-b973-af2904822b92 | -10.9593 | -43.0326 | 2026-07-05 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| a87c9f74-7955-38d2-8f3b-464588818f19 | -10.9209 | -43.0384 | 2026-07-05 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 81ed032b-7a23-3489-bda8-af2c213c26ae | -10.9401 | -43.0355 | 2026-07-05 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 808.7 |
| 26adc334-02f3-3330-b235-252c4cda53e7 | -13.2404 | -54.3303 | 2026-07-05 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 532ac204-9177-3432-af0e-e8f6d30e96d4 | -10.9405 | -43.0117 | 2026-07-05 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| ef3c9e0f-8f6a-340e-b39c-d8b91388dc21 | -10.9397 | -43.0593 | 2026-07-05 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 318.2 |
| 567cc386-6458-38a4-84d6-a2e913e7448e | -13.2407 | -54.3096 | 2026-07-05 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 055c858f-bb60-325a-adcc-dd1f0e304cae | -10.9205 | -43.0622 | 2026-07-05 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 3a559c84-85f4-349d-bc6a-7c15b88324eb | -9.60842 | -35.91021 | 2026-07-05 03:21:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| feaca0f6-4a2f-3b38-9dfa-c0889749904e | -10.9405 | -43.0117 | 2026-07-05 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| e820e8ad-e619-3979-927b-86c41fc658f1 | -10.9397 | -43.0593 | 2026-07-05 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 207.6 |
| 39719ae0-5dd3-36b9-a134-24238f686628 | -10.9209 | -43.0384 | 2026-07-05 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| f6867752-6145-34ee-bbba-b09e7b211af4 | -10.9401 | -43.0355 | 2026-07-05 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 565.9 |
| 877740a0-071a-3696-93e6-6b5b60b26109 | -10.9205 | -43.0622 | 2026-07-05 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| d9c167eb-7b91-3990-8d8b-2049240c8a81 | -10.9593 | -43.0326 | 2026-07-05 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 61409d89-cfc3-3282-8cba-f4d934f44327 | -10.9401 | -43.0355 | 2026-07-05 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 340.9 |
| 7f0a9626-06de-319e-a989-a2502e5700b4 | -10.9405 | -43.0117 | 2026-07-05 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| c6fb59ec-2649-357e-aefd-beb8b5195b3d | -10.9397 | -43.0593 | 2026-07-05 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 186.6 |
| 733761af-6808-3263-be75-4d10b8aedad0 | -10.9205 | -43.0622 | 2026-07-05 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 863d8eb8-fa22-35a5-901e-f317dc53d6e2 | -10.9209 | -43.0384 | 2026-07-05 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 79f3da7c-eaed-3303-9625-7ca5f730ab44 | -6.89548 | -43.71788 | 2026-07-05 03:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 775b9ad1-b283-3e7c-8147-eca2ecddad22 | -6.88989 | -43.71695 | 2026-07-05 03:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e923eca0-377e-3dce-a5f6-484010500873 | -8.08418 | -46.71362 | 2026-07-05 03:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c920dbe-3623-3f08-83cd-6615888b07a5 | -6.93583 | -43.71753 | 2026-07-05 03:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71aeb25a-f495-38b5-adc8-19ec47b5ebb9 | -7.18487 | -43.56064 | 2026-07-05 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b22bbbf5-0bf5-3187-9fb6-2e2934050283 | -6.90107 | -43.71883 | 2026-07-05 03:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d694abe3-0cff-31fd-8fbe-dc67aa4818da | -6.89615 | -43.71416 | 2026-07-05 03:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 72607945-1256-36ec-b2a1-e41eb2431de8 | -6.94007 | -43.72607 | 2026-07-05 03:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1afbd925-5b4f-397c-9591-78bf5c3e6685 | -6.94073 | -43.72231 | 2026-07-05 03:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24ffbb59-4e38-32f1-9090-459a7bec4d43 | -6.93517 | -43.72125 | 2026-07-05 03:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 14219c23-0316-3e31-b8f1-c7b6ab7fb888 | -9.60763 | -35.90958 | 2026-07-05 03:40:00 | NOAA-20 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a9e356d0-dd57-3f76-8c5d-eaafb4a6b81e | -6.93093 | -43.71272 | 2026-07-05 03:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd84cf1b-07ec-3bf6-9d51-61a7761da7c2 | -6.90175 | -43.71507 | 2026-07-05 03:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0d7b33d1-5ff6-344b-943b-c6bcf4a599a2 | -6.93649 | -43.71382 | 2026-07-05 03:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf3c3010-0a2e-3354-89c9-ad991bdb57ee | -7.1855 | -43.5571 | 2026-07-05 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ab5b41d-1631-3587-aa82-1ce3b4567819 | -10.92195 | -43.04018 | 2026-07-05 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad142f71-20d1-3ff8-bcc5-eef44e7b6682 | -10.92691 | -43.04119 | 2026-07-05 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7f07e18f-a18e-323b-93dc-5648d2f66a46 | -10.94073 | -43.04996 | 2026-07-05 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 933f1109-5adf-3e34-b6ec-9ebfab49eb6b | -10.93576 | -43.04898 | 2026-07-05 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 7a00fcb1-7ce1-30e4-8201-172ddaa4e8f6 | -11.433 | -46.58451 | 2026-07-05 03:42:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f04f7652-9e57-3303-aaf5-1716b6c438dd | -10.9418 | -43.04418 | 2026-07-05 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 4d2efac6-4cea-3075-bd43-7f1b1ec977a5 | -11.42593 | -46.58774 | 2026-07-05 03:42:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a10cc98b-3113-3858-bb90-9768f5d205f2 | -11.9106 | -43.38364 | 2026-07-05 03:42:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4044f424-d542-3e8b-89e6-6f531cb12ac9 | -10.93079 | -43.048 | 2026-07-05 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.2 |
| b99fd95c-a2bc-32d7-85cf-73b2187034ee | -10.9379 | -43.0374 | 2026-07-05 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 0200a436-b5e0-38ca-8526-9da2fc181b32 | -13.44344 | -43.85022 | 2026-07-05 03:42:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f30c051-8086-3163-95bc-b2604e9c9aa8 | -15.08288 | -44.01268 | 2026-07-05 03:42:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c0a2eb9-67e2-3563-812d-0b7c28a15ae4 | -13.44286 | -43.85319 | 2026-07-05 03:42:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64cb9551-6f94-39ef-a4c7-b39afe583d77 | -11.43601 | -46.60163 | 2026-07-05 03:42:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9f1ee78-41a0-32c5-b1c7-af5f1543a709 | -11.88843 | -43.83351 | 2026-07-05 03:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7e5f6660-c475-36c2-a4a8-3e5601831903 | -11.91556 | -43.38485 | 2026-07-05 03:42:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79b6dc4b-6da1-377a-a318-980d00fb0847 | -11.65926 | -46.7564 | 2026-07-05 03:42:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e274ec64-acd4-3633-a6ea-d2b1362e4196 | -11.92109 | -43.38299 | 2026-07-05 03:42:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4eb3b39-cb75-31f6-88e7-18c84feb5343 | -11.92607 | -43.38406 | 2026-07-05 03:42:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75ca40ed-14a4-3d20-98de-427ff70328b5 | -10.96843 | -48.13175 | 2026-07-05 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d3b42746-23b3-3660-bec2-7783d2e2b707 | -11.91613 | -43.38184 | 2026-07-05 03:42:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 513bb024-7fb6-3b05-9f5b-fee76fd4ad3d | -11.88903 | -43.83032 | 2026-07-05 03:42:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f36ebc85-d261-3c9e-92d9-f1b160af70cc | -12.37087 | -43.893 | 2026-07-05 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60c405aa-02e4-3042-a04a-02c26f1ddc20 | -10.92583 | -43.04701 | 2026-07-05 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ef4caba-2c1d-372c-ac42-92a69a9c5806 | -11.44222 | -46.60272 | 2026-07-05 03:42:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 358f6eae-c4df-356e-856f-8c66269acfb2 | -10.93187 | -43.04219 | 2026-07-05 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 543ed6aa-3792-3a15-bd45-f4e33fa264b7 | -11.43702 | -46.59656 | 2026-07-05 03:42:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 570cf99a-0aba-3c74-8500-eff5a0a5fad1 | -17.62206 | -42.28839 | 2026-07-05 03:45:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7c8299f7-7ac7-302c-81df-4149a033d3da | -17.00532 | -48.28418 | 2026-07-05 03:45:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d8a993c-2a4d-34d8-ba32-b23c1675c06a | -17.26327 | -49.00828 | 2026-07-05 03:45:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f5bc1eff-e6d5-3d62-a294-39aa408f031a | -18.51992 | -42.72952 | 2026-07-05 03:45:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6d1a72c4-f639-3e3f-ba16-c2945f48b6ca | -20.64879 | -42.25209 | 2026-07-05 03:45:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 949f150e-51e0-3ce5-9fde-678fe51aee6a | -19.74155 | -42.18911 | 2026-07-05 03:45:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aa23fdba-49fc-3071-b691-35612a9d07ac | -17.83218 | -41.96452 | 2026-07-05 03:45:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8aa879d3-ad4a-31f0-b62d-d4157df7f57e | -21.13154 | -42.38942 | 2026-07-05 03:45:00 | NOAA-20 | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c1b463c4-40eb-3d9c-bc54-bafc3d55adcf | -20.12707 | -41.30334 | 2026-07-05 03:45:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 768546f1-4c42-39f5-b786-85a4c066bfd1 | -17.8329 | -41.9607 | 2026-07-05 03:45:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 39c0db96-2049-355b-a6b2-ab911a33c454 | -20.12617 | -41.30817 | 2026-07-05 03:45:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 81ce610b-15d5-3be9-be30-28f652892e13 | -10.9401 | -43.0355 | 2026-07-05 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 391.4 |
| 35d9d4ae-1dfa-3087-80e4-26a58c935f23 | -10.9397 | -43.0593 | 2026-07-05 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 187.0 |
| fbc4b1c2-9193-3a74-a1ad-df8953c90746 | -10.9209 | -43.0384 | 2026-07-05 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| e9d023af-d449-31e2-97f4-a8efe0d25523 | -10.9397 | -43.0593 | 2026-07-05 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 29fc3111-2dfa-300b-bd86-b4f750d2ac1b | -10.9209 | -43.0384 | 2026-07-05 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 7cb6967b-fc59-3c9e-9136-039006b448bf | -10.9401 | -43.0355 | 2026-07-05 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 343.2 |
| e6ca7fe9-a223-326c-a6dd-dbea7f578955 | -10.9397 | -43.0593 | 2026-07-05 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| f8773efb-6635-35a0-80d3-23ff6cd2e25f | -10.9209 | -43.0384 | 2026-07-05 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 15be384f-a4a6-3838-abee-027569b6584c | -10.9401 | -43.0355 | 2026-07-05 04:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 253.4 |
| 1a950751-5e5c-3dc2-92bd-c33d341920c9 | -10.9209 | -43.0384 | 2026-07-05 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 7dfc28df-b552-350c-ac75-1d52529ef5d2 | -10.9401 | -43.0355 | 2026-07-05 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 273.7 |
| 5ea45382-8c19-3b09-837c-8d1a2e80f516 | -10.9397 | -43.0593 | 2026-07-05 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| fb066cff-0588-3ef5-a2fb-84893e1c25a5 | -6.8988 | -43.71457 | 2026-07-05 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f185e405-497a-3bb6-9aaf-a0c6fb54c4c4 | -7.53519 | -46.06861 | 2026-07-05 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 85b9d612-bf1f-3261-9df1-773a5aeb3625 | -6.00347 | -47.0065 | 2026-07-05 04:25:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f46e425e-c335-37c9-aecf-2501ca37d373 | -6.9058 | -43.71566 | 2026-07-05 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69171a77-4270-33fa-aaf5-46b1e34cb3c6 | -6.94082 | -43.72098 | 2026-07-05 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e07c1d1f-626b-3275-89c2-2272355490b0 | -6.94023 | -43.7249 | 2026-07-05 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 15325134-f64b-3e08-a8b3-e2f1875a1456 | -4.29015 | -48.35479 | 2026-07-05 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ea4ce852-888b-32e3-9b65-d442623b7242 | -5.93704 | -45.38503 | 2026-07-05 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
