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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c2e6b31-64db-3a0a-a1dd-bfe00583bc3b | -10.63892 | -44.74952 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a695899-e58e-3810-9f37-4c914c1c0dc1 | -11.12686 | -50.77514 | 2025-08-08 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0ff0825-d1ab-33ad-afed-da5bd191cb18 | -9.06473 | -45.06867 | 2025-08-08 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bbbfa89c-4007-3a38-9939-06bcb5067bd2 | -12.09354 | -44.7361 | 2025-08-08 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25687e24-57e2-3626-9b29-598bd10bd36a | -10.64111 | -44.74313 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 051c02b9-0473-3247-933a-034a44f3f824 | -8.16473 | -42.41846 | 2025-08-08 04:34:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4bed77b4-3605-3ceb-b1cd-dd721d4477e1 | -11.02624 | -45.07348 | 2025-08-08 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97620025-50e6-384a-820c-0d1b026f5918 | -7.25063 | -44.66708 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 2e52c782-b104-3df4-942b-4f7c1ec10a97 | -7.24782 | -44.63519 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f82df3f-0bc1-3242-981c-5f2e550ade20 | -8.06666 | -49.71571 | 2025-08-08 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f11fb6c-b3c0-3cab-8825-bad8aa9a4a7f | -8.92181 | -60.75073 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbe7bd06-41b0-3ed4-b0fe-33b1a017dbaa | -12.99866 | -47.49524 | 2025-08-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19e54fdc-d1cf-35ef-916f-98d8d0f27c7f | -10.63798 | -44.73779 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e54e4d8-64e0-3b08-bb75-779cb5319265 | -12.57663 | -47.14897 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8b24d06-5f01-3ebb-840a-4c66afb60322 | -12.5402 | -47.1405 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 58985013-bd3b-3911-b33a-9fa3d70a780b | -11.80312 | -44.93111 | 2025-08-08 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9315a79e-6098-3315-906b-93e89a452d0b | -11.02247 | -45.07291 | 2025-08-08 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21b487e6-8434-30a5-9cb3-5be235a38335 | -7.22986 | -44.65474 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 0dd0f584-8d77-3bda-86e2-c017992dc9dc | -7.25374 | -44.33544 | 2025-08-08 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 394358f9-94c6-3237-b119-8e81df22859c | -9.06409 | -45.07302 | 2025-08-08 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 05cd9af5-771e-3c31-bbe9-8552719d2035 | -11.19207 | -55.00999 | 2025-08-08 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f20e5563-6451-3368-b742-46197d5db58c | -11.74579 | -44.95966 | 2025-08-08 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 963c6b45-fba8-35a2-ac21-5e99d927573f | -7.72397 | -45.5173 | 2025-08-08 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57889f47-b90c-30b4-bcb8-ab88c0c0cbfd | -8.5222 | -43.31641 | 2025-08-08 04:34:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6d5e0367-d315-3460-9620-08ffb4e61ffc | -11.44258 | -45.13657 | 2025-08-08 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5767123e-b89a-3e93-9298-bb303478efb3 | -12.5714 | -47.14532 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d4ec0d3-4e74-35b4-9e0f-8a89a806edb9 | -7.39056 | -44.24583 | 2025-08-08 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9e2d680-56a6-3d1e-86bc-effda259465b | -9.93592 | -60.4603 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 283e1126-9d17-312c-8a4f-28fa5aa31795 | -10.43706 | -44.35482 | 2025-08-08 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29cf5db6-e080-3f7b-a5af-90cfe63d8418 | -12.58419 | -47.16997 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f2982ef7-2764-33d9-bc15-4e2d9b3d9e34 | -8.90529 | -60.55192 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5493d64a-1706-35ad-9615-9e9b8e1b1ce5 | -7.67493 | -45.53205 | 2025-08-08 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88880bab-8a9e-3875-965b-ed2a79c5d5a4 | -10.43246 | -44.35914 | 2025-08-08 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f266d357-a684-3111-b22a-5a05197d2e86 | -9.9311 | -60.48447 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3a7e1e8f-b885-3404-9271-9ac029bbc08b | -9.70295 | -61.28756 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b572603-b340-33de-8c9f-dfc2f80aa2da | -9.06778 | -45.07346 | 2025-08-08 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a6afe73-fdf2-3d56-ab3f-09d5c77ec94e | -5.81977 | -59.22693 | 2025-08-08 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c22eecb-5afb-3be4-b525-0f87e9f858bd | -8.98764 | -45.68317 | 2025-08-08 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffd5538c-6b33-394e-a18c-f6a058d0b4c9 | -7.90326 | -45.33521 | 2025-08-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eb607b70-52f1-326c-9c83-882c6276dcb4 | -8.88132 | -44.79161 | 2025-08-08 04:34:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73988992-6aa4-3070-af04-e91aec145909 | -12.09744 | -44.73671 | 2025-08-08 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 95e6dab7-cd5d-3f7d-95d7-c23a34a86634 | -7.52538 | -45.15596 | 2025-08-08 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b5192a3-3885-3032-9035-f49b710ece5d | -11.19488 | -51.43773 | 2025-08-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| be4cee82-e9bf-3594-85ce-cd5eec51bec2 | -9.71263 | -61.30672 | 2025-08-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 98d39e06-b17c-324c-8deb-fe1db7737955 | -9.92986 | -60.49648 | 2025-08-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5aa0150d-1ec0-36df-8187-37ac793f7cb5 | -11.44191 | -45.14121 | 2025-08-08 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d362e20-a3c0-311f-b5b6-8605d124be58 | -6.92998 | -44.6863 | 2025-08-08 04:34:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9792121-85e6-3170-b5f0-53cbb7c73385 | -12.52981 | -47.13888 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 92c71541-824d-306e-81ab-e655071619f0 | -12.575 | -47.18441 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 260d993b-6244-3b7e-bb16-b3ada9826bb4 | -9.07511 | -45.06875 | 2025-08-08 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20979432-3339-3196-bae8-a0f7b5a84ea9 | -8.70827 | -47.86369 | 2025-08-08 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dab05fa-e64e-37ea-8b5d-0cdf554d0a43 | -12.52113 | -47.1256 | 2025-08-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1ec33a38-4ca2-375e-a72e-dd40ade588fd | -10.48033 | -44.38685 | 2025-08-08 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 149843e0-d920-3e55-a63d-e77ab715a565 | -9.07211 | -45.06966 | 2025-08-08 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3bed99a4-95d4-35ac-837b-5273f9834345 | -11.89654 | -44.96417 | 2025-08-08 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33b7d7e2-8985-3caf-8bc4-28aff2a4a917 | -11.7539 | -47.50201 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 306acfd7-bcf0-3200-9f13-a842e6e6ff6e | -7.11097 | -44.22455 | 2025-08-08 04:34:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c7e01652-ef78-3384-8439-e9f05ba8c140 | -9.31546 | -62.64421 | 2025-08-08 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e02bde1-8c97-3b55-8f1d-3b932a53c4ca | -6.95869 | -44.49409 | 2025-08-08 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2687848c-2455-3a63-bef8-b1d9fdc58aa8 | -11.75222 | -47.51305 | 2025-08-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d4fa0a3-7fb3-3b21-98c6-d5d770e92f6b | -10.82831 | -49.37956 | 2025-08-08 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f45e5f76-ecb5-367f-b658-461d3295750d | -7.11676 | -44.21156 | 2025-08-08 04:34:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2374e0be-c068-3f9a-ac2d-d1efb28911a8 | -8.98976 | -45.68692 | 2025-08-08 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c021bdbe-4884-35fa-9e5e-4f11a7efaa57 | -7.15574 | -44.08015 | 2025-08-08 04:34:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9ba8c92-ea4d-31e4-9d3e-04449cddd1fd | -19.30168 | -47.436 | 2025-08-08 04:36:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47882ddd-e489-3a4f-a35c-38e710c5cdb9 | -20.05683 | -47.58438 | 2025-08-08 04:36:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 5b2721bb-9dab-3251-9cb8-2054717fb92c | -19.12789 | -43.52209 | 2025-08-08 04:36:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c1a27c65-1fc5-319a-b29e-8548ab6e9fe8 | -17.57467 | -49.08115 | 2025-08-08 04:36:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d5906b5a-6e70-3795-a941-3f3d6efbeef4 | -15.68648 | -48.96994 | 2025-08-08 04:36:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db3a4840-86ad-3801-9667-b8bd1ff8bb50 | -17.19035 | -46.92335 | 2025-08-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3ea8619-94c3-34f9-8e2f-2ee151f6b833 | -13.03447 | -56.85995 | 2025-08-08 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6937cbb1-9b32-3410-b9fd-19a4d6029514 | -14.36368 | -51.10167 | 2025-08-08 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 187467cc-8f54-3848-9dcd-39b4041c189c | -20.67928 | -44.82317 | 2025-08-08 04:36:00 | NOAA-21 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6ad57495-a0c8-376a-916c-2d1c80bae10b | -21.00573 | -43.27841 | 2025-08-08 04:36:00 | NOAA-21 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| df31c292-3a69-37c8-86a2-813ac454e2ad | -18.91618 | -47.55676 | 2025-08-08 04:36:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 54b5b949-e51b-3713-a63d-b70f239694ea | -14.81347 | -48.41013 | 2025-08-08 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52cd8184-13c3-3e8b-8177-a916c10e4c4a | -20.0648 | -47.58094 | 2025-08-08 04:36:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8396c9e6-b359-368c-96f4-1985fad67a42 | -16.46948 | -43.42466 | 2025-08-08 04:36:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e533bc6-c1e0-371d-bd7d-2df62ab9e437 | -19.19198 | -45.05371 | 2025-08-08 04:36:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94ae94b1-472c-36f1-970e-05837386253b | -14.78283 | -48.00196 | 2025-08-08 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 98d4e18a-3e58-3cdc-a77f-00e2c8a5cdf2 | -13.04286 | -56.8588 | 2025-08-08 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d62acde-ba28-3093-b633-7b02f177fa42 | -19.7731 | -46.56468 | 2025-08-08 04:36:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9766bb9-aa3c-3042-99aa-536e19211b36 | -14.35973 | -51.10477 | 2025-08-08 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1e28805-c10e-3fc8-8112-e9746a41bd3b | -16.74163 | -47.7341 | 2025-08-08 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ef963221-4c98-363a-bf1e-7017bf1737cb | -15.64777 | -47.85388 | 2025-08-08 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2facd3f7-1edd-31b3-8b04-fe3ffcca73ff | -18.8551 | -45.13322 | 2025-08-08 04:36:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a802a210-403d-3d0c-8257-dad6259f85e7 | -20.57294 | -41.72194 | 2025-08-08 04:36:00 | NOAA-21 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| db03150b-1195-364f-94a4-fec61a1a431c | -16.72255 | -49.1301 | 2025-08-08 04:36:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0fcfb571-ac7b-3628-811a-2bc727c3d7ca | -19.95921 | -44.8582 | 2025-08-08 04:36:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d2657dd-5b2a-3044-86bc-630111b4d12e | -18.05167 | -47.94241 | 2025-08-08 04:36:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30807f0c-cda4-3da1-b547-9c64ab2ad152 | -20.70287 | -45.46355 | 2025-08-08 04:36:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfff50cd-dc7d-39dd-8ea6-7ab2ef329742 | -20.05621 | -47.58891 | 2025-08-08 04:36:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 411059ca-385e-37bc-a4ac-52108b00acde | -17.61566 | -46.71254 | 2025-08-08 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c6d9e64-c8ff-39b1-90e4-508c41bda7a4 | -20.06049 | -47.585 | 2025-08-08 04:36:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a4b4a4d8-927c-34ee-ab24-c703eb39b105 | -19.12852 | -43.51652 | 2025-08-08 04:36:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ecfb83e0-24a0-36df-8ec8-3c485e40feb3 | -14.77997 | -47.99762 | 2025-08-08 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c798590d-559e-3746-9167-cab18a6268f9 | -20.06113 | -47.58036 | 2025-08-08 04:36:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 528eb3d8-2acf-3370-8132-d1d6d0109e83 | -13.04195 | -56.86366 | 2025-08-08 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a886a24c-ecd7-3456-ae2a-eff182b295a5 | -16.72775 | -49.13108 | 2025-08-08 04:36:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 48613331-e8e3-3c27-9bf3-9357e23b91c7 | -19.97302 | -44.96059 | 2025-08-08 04:36:00 | NOAA-21 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README17.md)
