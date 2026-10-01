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
| 2775013d-8579-3277-99d6-9afd38618d99 | -6.3665 | -55.1461 | 2026-10-01 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 766b0ec8-3d4f-3529-8718-87d928b945b8 | -12.4544 | -44.1466 | 2026-10-01 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 555.0 |
| 0a4a61cd-ca8e-3f36-8939-663e07cc4f39 | -10.1881 | -49.9703 | 2026-10-01 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| ceaa0567-71e9-3485-9212-6a02dac0a5b4 | -10.9258 | -43.8641 | 2026-10-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 84477e58-d2d5-30a6-a539-f661ff17339f | -7.3965 | -42.6498 | 2026-10-01 14:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 6d8b3240-da9f-3cca-ba62-5f04c523adda | -12.5518 | -47.1837 | 2026-10-01 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 6a42d2f8-1553-3d55-a013-686f210dc89f | -6.1386 | -53.2818 | 2026-10-01 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 38a28118-c805-36b2-9c06-46ff44fd4df4 | -11.6789 | -43.4921 | 2026-10-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| cd8d786d-6ee1-3600-8815-2aed7713a8b5 | -14.377 | -44.7534 | 2026-10-01 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 409.5 |
| b2d13c24-5900-3bdc-8960-a73403522026 | -15.438 | -41.2941 | 2026-10-01 14:30:00 | GOES-19 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 132.4 |
| 996b169f-d944-3b30-a1c4-44697539db91 | -14.5458 | -40.8417 | 2026-10-01 14:30:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 129.8 |
| 8998cf70-c3d2-3343-9b14-1a55e332448c | -9.8803 | -44.9553 | 2026-10-01 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 132.3 |
| bba6a13a-c5e4-319f-ba4a-953991fac464 | -11.3935 | -43.3705 | 2026-10-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 214.3 |
| b7cc9285-9bdd-3109-86fd-e9be3963f0bc | -9.9029 | -50.1487 | 2026-10-01 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 67af569a-ffc9-3d9a-bfb6-2d8f15cd4bdf | -5.9152 | -53.4762 | 2026-10-01 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 723dca01-2801-3b71-840d-47c3e7c82ce8 | -8.6268 | -45.3054 | 2026-10-01 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 10f4c8a9-4945-3688-b66c-f6f81d6547e1 | -10.2824 | -49.9821 | 2026-10-01 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 51df34ea-612e-39db-b03b-6f2d17f76504 | -14.3574 | -44.7569 | 2026-10-01 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 280.2 |
| 7b9c3995-91eb-3081-91eb-f000d58fb5b4 | -11.411 | -43.4625 | 2026-10-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.8 |
| ab4a82b0-ac67-33da-8829-677ba28a095f | -8.206 | -54.7408 | 2026-10-01 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 1f7103a9-3669-36eb-b97a-682ae8f00bc7 | -11.2434 | -44.286 | 2026-10-01 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 532ba0c7-7721-38ec-a406-9db5b00d5d54 | -8.0166 | -42.8681 | 2026-10-01 14:30:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 379030ed-f445-3739-97f3-832b87f88128 | -13.3272 | -43.9285 | 2026-10-01 14:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 187.4 |
| ff6f38eb-d753-3ca1-b6c4-3eb85cd61a04 | -12.4355 | -44.1262 | 2026-10-01 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 302.5 |
| 69226962-3b53-365f-9b58-b44f480129bf | -9.3475 | -45.111 | 2026-10-01 14:30:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 2bd72aaa-938a-3a20-8cc4-990fcfae0955 | -11.6784 | -43.5158 | 2026-10-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 0e1db7fc-c5cf-36a6-971a-8106960f85bf | -8.9292 | -49.792 | 2026-10-01 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 123b7242-89f1-31d9-a4d8-d4527197ac65 | -11.4127 | -43.3675 | 2026-10-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 8a8f5967-b66a-39fd-9766-59cdb977132a | -6.532 | -55.2777 | 2026-10-01 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| bd9bf57a-0dca-3ed1-9d18-8b7102dc7fa8 | -11.3927 | -43.418 | 2026-10-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 185.1 |
| e6373679-9201-322a-865e-70b2a9ec05e7 | -6.8856 | -42.8416 | 2026-10-01 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 20e73d77-e755-3b49-ad13-a89ff2d74b4e | -7.0609 | -42.3274 | 2026-10-01 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 4e833f5d-85ec-30af-82e8-8212d841c2a7 | -11.4106 | -43.4862 | 2026-10-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 212.4 |
| 95569c2c-b5bd-38a8-9d56-a35a43e5d038 | -11.2246 | -44.2654 | 2026-10-01 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 190.4 |
| a5e05c9b-1cc4-35fe-ae33-6f62b139916f | -6.9231 | -42.8616 | 2026-10-01 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 7c184119-aa38-374c-bca0-dad91bf4a02f | -8.6457 | -45.3034 | 2026-10-01 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 72b62f29-a209-31fd-8f71-df6c9203cb1d | -5.8411 | -53.5002 | 2026-10-01 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| afb8eb4a-cce1-39d3-b184-175b642d6738 | -12.2368 | -44.4624 | 2026-10-01 14:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| a71384bb-407d-3fd2-858b-6761327423e9 | -9.8064 | -44.8265 | 2026-10-01 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 280.7 |
| 7bc3ff1d-48f2-37bf-85eb-0d37cf3e2abb | -10.2827 | -49.9606 | 2026-10-01 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 8dbb6cd2-e21c-3e92-a4f1-51b1d6012896 | -15.5175 | -46.1257 | 2026-10-01 14:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 103.7 |
| ba4aa588-99c7-39e2-b77c-b236af4e4240 | -12.9036 | -44.8217 | 2026-10-01 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 228.6 |
| 31dcaf36-9688-37b4-9609-7401a17ca193 | -7.09 | -43.081 | 2026-10-01 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| a2a95c50-3145-3d57-887f-66eac7013ed1 | -11.1041 | -44.6083 | 2026-10-01 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 5a37166e-890d-3769-b221-86a1fe6795b2 | -10.907 | -43.8433 | 2026-10-01 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| df8d64f6-a568-3643-a2bb-406754efe2d3 | -15.6481 | -44.7217 | 2026-10-01 14:30:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 78a16a8c-b604-388d-b96c-c79e0ac62dcb | -9.0598 | -49.8656 | 2026-10-01 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 93fa7959-48d4-363b-897c-4a6b82cc0891 | -5.8412 | -53.4799 | 2026-10-01 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| aa3c4dc9-ea1f-3538-9bb8-bca94fb8834f | -11.2438 | -44.2626 | 2026-10-01 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 224.2 |
| 33a2b0e5-57d2-3d2b-beb9-1c8466b247a7 | -9.9787 | -50.1198 | 2026-10-01 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| a82690c7-4426-3241-9497-f0a493c21c84 | -15.438 | -41.2941 | 2026-10-01 14:40:00 | GOES-19 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 112.9 |
| e2655c07-8fd8-3da9-98ee-38e28ab3f474 | -12.6074 | -47.2878 | 2026-10-01 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| e432f885-994f-30a8-bf96-aae5ff4f0c87 | -9.4813 | -46.3646 | 2026-10-01 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 0582bc33-405e-369e-9b22-f61094492f1a | -5.1252 | -56.0143 | 2026-10-01 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f914aa40-33ec-3324-b791-ee278ae1488d | -6.9231 | -42.8616 | 2026-10-01 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| 0b3d74e8-006b-35ef-b907-41e0fa5513dc | -7.0361 | -42.8508 | 2026-10-01 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 8ef74808-4469-39a1-8ca1-7350b20faa01 | -10.7112 | -45.3075 | 2026-10-01 14:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 70408bed-47a1-3ade-8c73-2e1bddd2fbef | -10.7302 | -45.305 | 2026-10-01 14:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 218.4 |
| 05667a0f-0fcc-39fc-8c79-c6273bf1d78d | -12.2368 | -44.4624 | 2026-10-01 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 469.8 |
| fd7cad3a-3fa4-30b0-ba8c-cc474700bb00 | -9.9976 | -50.1179 | 2026-10-01 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| b6f67a19-2a92-3cc8-81a2-c4dd71d5b339 | -11.2275 | -45.2143 | 2026-10-01 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| e1dd9499-449d-3cf7-9c3e-59d6c53d0a95 | -7.055 | -42.849 | 2026-10-01 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 96.2 |
| f78dde7b-ddb2-3106-a512-c4dfa19f7e92 | -9.9781 | -50.1626 | 2026-10-01 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| d6c5a957-031b-3f21-87e6-bd24f7eeccee | -9.8803 | -44.9553 | 2026-10-01 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 211.3 |
| 887e8873-da33-3abc-9205-958909c10a32 | -9.2054 | -45.8095 | 2026-10-01 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| e97e0d7b-0ec4-3b6b-b033-34bb4cb3ff21 | -11.4106 | -43.4862 | 2026-10-01 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 258.9 |
| f0271dc5-05ab-3943-8980-f254c69f2834 | -9.2243 | -45.8074 | 2026-10-01 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 5e8a86e6-42df-3053-91d7-aaf34e79a7ce | -11.6207 | -43.5248 | 2026-10-01 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 204.4 |
| cdd58d52-800d-312d-9aad-105e7ed244cc | -9.9029 | -50.1487 | 2026-10-01 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 0c2eb106-c826-338e-bd30-8c60fd004100 | -7.3965 | -42.6498 | 2026-10-01 14:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| fd66ed21-60e8-38ac-8f3c-285227f002e9 | -11.2278 | -45.1913 | 2026-10-01 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 6c9a9ce6-43c2-3cfb-8e48-5409f68dbae0 | -9.3475 | -45.111 | 2026-10-01 14:40:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| fba29746-79c0-37f7-818c-65955c95cf6f | -7.7858 | -49.867 | 2026-10-01 14:40:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 97a0776d-b2b9-373e-9dde-e9c15ffda8ce | -6.1386 | -53.2818 | 2026-10-01 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f3dc1554-7dbb-386d-8ed0-d0e112207dcc | -5.9152 | -53.4762 | 2026-10-01 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| ccfda380-557d-349b-9371-bff4192afdd9 | -12.6267 | -47.2851 | 2026-10-01 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 9edf331e-9d21-3829-ba53-46618f1ecf0e | -6.1949 | -53.177 | 2026-10-01 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 22aedde2-6a13-30df-992d-ea5fd6fc6dd2 | -11.6789 | -43.4921 | 2026-10-01 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 270.5 |
| 418438c3-a84f-333b-b99b-00754ede2b7d | -9.9593 | -50.1644 | 2026-10-01 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| cb6ca8a6-923e-3c24-a93f-449624d5dff7 | -11.3927 | -43.418 | 2026-10-01 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 391.8 |
| e6a8f73a-d9ba-3480-a4e2-f19cc1ff14cb | -5.8597 | -53.479 | 2026-10-01 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 134.7 |
| b72dd817-4b36-3afe-87a7-3d023b6f9bbc | -12.2175 | -44.4654 | 2026-10-01 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 27590b35-4e5d-3482-8049-d2261f6fe1fe | -14.3574 | -44.7569 | 2026-10-01 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 182.0 |
| 0f95834f-aa37-33a0-a6b9-acd43f5c39bd | -12.6271 | -47.2626 | 2026-10-01 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 20752b7a-89b9-3c6c-84fe-07abc02c2c20 | -8.8468 | -44.3871 | 2026-10-01 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 1f1bbe16-fb6b-3364-852f-b5cc5f4383d8 | -8.6457 | -45.3034 | 2026-10-01 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 7e53922f-7633-3ed2-9001-933c503cf128 | -11.2246 | -44.2654 | 2026-10-01 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 575a2f69-e0f5-3afb-9d12-6ff682b13314 | -7.4156 | -42.6241 | 2026-10-01 14:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 94.4 |
| 6e6ac5de-e7dd-33e4-99b1-20d656222475 | -11.3935 | -43.3705 | 2026-10-01 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 247.9 |
| f5b5e77e-ce2b-3546-a2a4-5b5b0a98aaae | -13.3462 | -43.9489 | 2026-10-01 14:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 237.8 |
| 33492635-2335-3b62-9e40-cc3d4878ed6c | -15.9722 | -45.9697 | 2026-10-01 14:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 15a20028-7aff-3c79-b820-064f4742e48f | -8.3211 | -44.1447 | 2026-10-01 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 1de21ecc-7761-36f4-bc20-378e14c6d4ec | -7.0547 | -42.8726 | 2026-10-01 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 103.1 |
| 03f3cbf6-d24b-360a-8590-9b9d50c3dd86 | -8.6268 | -45.3054 | 2026-10-01 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 1c9818b8-596f-30c2-805e-471fad9df9a5 | -14.377 | -44.7534 | 2026-10-01 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 89c9ea21-5b09-3226-98d3-9f7f8db67d0d | -5.8411 | -53.5002 | 2026-10-01 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| b8cdf0c2-359f-3e68-a702-a66b54a67dcb | -8.0166 | -42.8681 | 2026-10-01 14:40:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| eef3e9e2-0cbd-309b-a9eb-a852da5703d3 | -7.3967 | -42.6261 | 2026-10-01 14:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| fef21e2e-9fd2-3392-bdb3-bf3006c3b9d4 | -11.2282 | -45.1682 | 2026-10-01 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 948489e4-9a34-3807-93f1-55c24a3cea3e | -7.0359 | -42.8744 | 2026-10-01 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |


[Clique aqui para ver as próximas entradas](README104.md)
