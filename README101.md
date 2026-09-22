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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f74fefaf-d3b7-3c79-80c7-a2557d13ff9e | -9.8767 | -55.728 | 2026-09-22 05:25:00 | NPP-375D | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a78eab89-4128-3342-8008-5e5871000182 | -15.44098 | -48.46469 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aab8ef93-b136-3d83-9995-145e97bfc2f3 | -7.9481 | -57.29785 | 2026-09-22 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7726ab22-8b8a-3bbb-b3ac-4cbce9571943 | -15.44542 | -48.47923 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffc28151-b54e-34cf-8639-7a6f09cbcb2a | -10.60363 | -54.00011 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23806ea6-d67c-3fb2-84e4-8a051ae1638a | -10.61494 | -53.9837 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 882e1809-4561-308e-8421-13cdf06f6c0a | -15.44389 | -48.43832 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ed30cfe7-8caf-3683-9dbc-2386795c70a2 | -9.97567 | -50.25495 | 2026-09-22 05:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 777015ef-de64-3b38-8b45-ff64347ef19c | -8.20814 | -56.08699 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6682d9f2-a766-39ee-8102-cf45444fed12 | -9.20967 | -60.28846 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 310fb3db-3cb2-3f4e-a502-b2d5fc860bd5 | -10.46375 | -51.30813 | 2026-09-22 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc957138-1bf3-311f-a957-94c5d0b4fc8c | -8.25849 | -55.26615 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8540f110-fe92-3222-9607-5ef0919d1483 | -11.4384 | -47.34886 | 2026-09-22 05:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0a57fe42-092a-3f5c-8e2c-b21dd5d62ac7 | -10.72356 | -54.00217 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7db7a875-7dc4-3a19-8ddc-2b1e62c61889 | -11.43911 | -47.34298 | 2026-09-22 05:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99d6711e-7966-33f7-8450-ea4f516bbdb8 | -9.21499 | -60.84682 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8057686-b991-3019-b0b3-e4637e5e9542 | -8.59958 | -54.62067 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e15bd15c-4a58-3b5b-b44d-78af2df06518 | -7.69071 | -61.53645 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f705346-d49c-355e-b963-20483c678e17 | -10.68492 | -48.70977 | 2026-09-22 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abcb18e0-a43c-3e85-a845-e9646f920421 | -8.92271 | -50.89973 | 2026-09-22 05:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59752140-e221-33ea-8a3a-e837a2ee7e38 | -10.45472 | -51.33886 | 2026-09-22 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d30eefb5-14f7-34fe-b82a-2abb73b92c8a | -10.68989 | -48.71334 | 2026-09-22 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 035e1cbf-ea09-3b44-9501-25c27e2ba5ba | -15.4419 | -48.45634 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0d9b2f8-4119-3454-98be-14838b490606 | -8.91369 | -50.93111 | 2026-09-22 05:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b17f4506-72f1-3aab-8e68-def63954c7fe | -10.45289 | -51.27232 | 2026-09-22 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5035de4f-33a1-317e-83bd-e23bb5cacc91 | -18.03771 | -50.92269 | 2026-09-22 05:25:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 63d1f920-50b0-3b54-bdd4-35b8f73f8b90 | -8.23613 | -55.27096 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a18950b-f14e-33fa-b0c3-7423bfa7e5c4 | -8.60322 | -54.62122 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3ab6a4e-0d07-3589-9dcb-b45d2a662561 | -10.60964 | -53.98616 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 8eddd953-a472-3b33-9f19-fab014117cdc | -11.10742 | -48.32201 | 2026-09-22 05:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ca03a1f0-8c61-3a05-bcde-b24b3e67881f | -8.25718 | -55.29802 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ff93eff-6d71-37d3-9361-3fd107391c3e | -8.54474 | -54.68754 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c52bf17e-72da-3de8-b3a9-27d6e5c8ff4d | -8.23674 | -55.26701 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6472b24b-edcb-316d-98ed-4031c891189f | -18.04218 | -50.93027 | 2026-09-22 05:25:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2f1bb508-5b4a-344e-b576-6a0cca93621e | -8.61416 | -54.62291 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7be5bd1-a14b-3f2b-88fd-c81e4663340a | -7.69476 | -61.53569 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30cf8781-83f3-37b8-8ae5-22ae94b231d0 | -9.87532 | -54.82051 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c419f7f-d3f5-3a5c-9feb-e2356a0649ad | -11.44032 | -47.33293 | 2026-09-22 05:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9a98097f-84a3-399c-bf13-03ecb75a8e0a | -9.11371 | -60.94733 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7983cc4f-4e86-367b-af55-8a85d2daaa6f | -10.69511 | -48.71772 | 2026-09-22 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7170a508-671a-322f-9794-639005efdc2c | -10.68484 | -48.70877 | 2026-09-22 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61eb5cf7-37c1-3e67-ba0a-d6914b045893 | -9.6657 | -54.33031 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db84da32-5e44-3b3a-8d6d-685f1fc22f14 | -18.51687 | -50.31816 | 2026-09-22 05:25:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e8ddf24e-65d2-33ce-814c-b1e00445dfcb | -8.62144 | -54.62404 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df889f01-68ad-34be-8096-28b678d5a86d | -9.30169 | -58.91279 | 2026-09-22 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0a4ba80-b01d-3cd3-b6bf-b248e146bf83 | -11.16296 | -51.11045 | 2026-09-22 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db004bf8-a338-34d6-a122-c60bcecec28e | -8.62019 | -54.63247 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1da38f6b-5440-343d-a9c5-9f01c7c83a46 | -9.65511 | -54.32415 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 220c763c-637e-3bef-b4f5-046bc1ca0b71 | -11.40556 | -46.80122 | 2026-09-22 05:25:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3a13f4a2-7914-3760-b642-f0cf0d8064c0 | -7.70152 | -61.5415 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 32388f76-f1b4-3fd5-87cd-4cb3a5ebce56 | -9.3843 | -47.7571 | 2026-09-22 05:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79163605-5909-338e-9713-667001984829 | -10.61357 | -53.99344 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c33b5c53-7553-3582-b1fe-f9f848aa2691 | -15.44439 | -48.43377 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| de86a43d-1013-3ffc-b3a5-cf7b117e128e | -11.1589 | -51.10474 | 2026-09-22 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 4da8b8e2-78ef-343d-bae5-8e2379b8b6ec | -18.04297 | -50.92331 | 2026-09-22 05:25:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bf4daf0a-aea1-3d23-b1df-65229fd6b06f | -10.72425 | -53.99728 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5eed05a-7be6-3382-bf2a-d987943867e1 | -9.8726 | -55.73139 | 2026-09-22 05:25:00 | NPP-375D | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5937776b-46b3-316e-a295-e4f955ba3f2d | -10.60577 | -53.98559 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4119417d-a1b6-3312-9aff-24e40586389b | -7.97215 | -62.04243 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9b02dc17-500c-3a82-8296-acfdbc52dc75 | -7.70202 | -61.53834 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 123ff613-6fcd-3233-a71f-87394a1277e3 | -7.69099 | -61.53506 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bce0b39-4bca-3169-8a70-da5cf2b23ad9 | -10.84783 | -50.14714 | 2026-09-22 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd6f6610-63c2-353b-abe7-37f36f6c3eec | -11.15012 | -51.09836 | 2026-09-22 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f611b194-7619-3010-80d5-1bb0af1be6be | -8.25558 | -55.26168 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec7307be-a31f-3cc8-aa01-b98be75b9f9d | -8.25327 | -55.25325 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73b104e4-f3a2-3488-9137-7d62d8565620 | -11.40617 | -46.79615 | 2026-09-22 05:25:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e77e0914-ef11-39ec-a506-65d6656edfea | -9.38376 | -47.76126 | 2026-09-22 05:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 562388d4-4735-3128-baeb-bac7c0bc39ab | -9.07945 | -60.43926 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 349bfbfb-171b-358a-92fd-0c371fd3be82 | -11.44584 | -47.33852 | 2026-09-22 05:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c6a5d7b-7604-32ba-add5-737e56bf52af | -9.24182 | -57.15504 | 2026-09-22 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d2c58df-a398-3f6d-a4b0-55b212401699 | -10.84205 | -50.15227 | 2026-09-22 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5910f01d-537d-3d95-8ed8-6ee1de33c6d3 | -10.60434 | -53.99529 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ca36508-ebf8-3e9c-8971-c967cf02c106 | -11.39989 | -46.79518 | 2026-09-22 05:25:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81c76e3e-e206-329f-8bd7-82e9ee29d829 | -10.71443 | -54.01078 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb2821cb-8a13-30ba-9261-4ac546f36d62 | -8.60147 | -54.60793 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 613ec2c7-faf9-3f0d-a2f2-4bb3b4467e60 | -10.32214 | -50.54453 | 2026-09-22 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a419ebec-d3ab-3b1e-ae61-8240cf6ab441 | -8.91813 | -50.89862 | 2026-09-22 05:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da8eb1cf-684d-3ea3-b703-dc36faf1974d | -10.61425 | -53.98858 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 08029cd9-9a19-37ba-a0d6-d521d00ec5b2 | -18.51646 | -50.32196 | 2026-09-22 05:25:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 32be0180-0b6c-3565-885d-80b727d35e65 | -9.84724 | -48.31631 | 2026-09-22 05:25:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf7ef924-115c-3dbb-8c12-4f9dbdf1d585 | -10.68439 | -48.71238 | 2026-09-22 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db87dc56-49c7-314c-bf94-5151c65a8d22 | -9.28018 | -60.62166 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d877140-b632-3d29-9109-1599a0328dd7 | -9.54796 | -47.94972 | 2026-09-22 05:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf527c2e-9d26-382a-9b7e-b328735a5758 | -9.27752 | -60.63757 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3f9e9411-f9f6-333c-a61b-b5b66435cc66 | -8.61352 | -54.62716 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8772b5d3-7c7b-3aec-a2fc-99252b1d9222 | -9.97075 | -50.25426 | 2026-09-22 05:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b5f1807-af1b-3cd3-a25f-9cf4ffbdd936 | -9.28525 | -60.63477 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ded07f03-b30e-3f42-8e8b-4e50f45e89a4 | -9.67559 | -54.34111 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d0844ed-d2cc-3765-aacb-ec7cc7ab00b5 | -10.41853 | -53.79544 | 2026-09-22 05:25:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 533bcc72-fceb-3da7-afd0-bc570194fb59 | -15.5993 | -48.32801 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9f74ee43-2c9c-37b2-aeaf-0f393484d04f | -10.69471 | -48.72074 | 2026-09-22 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07f3e6e4-c3f4-334f-b088-65046ca0918a | -11.41183 | -46.80227 | 2026-09-22 05:25:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c0eaea47-2f63-3694-b95c-50a0ef7d2173 | -7.69825 | -61.53771 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a8e4a08-5c36-3370-9f03-4180f21e65c6 | -10.8664 | -50.16154 | 2026-09-22 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff1d7db4-2006-3bcc-876a-77ae15241cdd | -10.60582 | -53.99229 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9433ea36-0252-37a9-bbaf-d83a95da7da3 | -7.50808 | -61.38241 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77c5d09b-3ca4-3dfa-a5d8-e14c240d1ced | -10.61106 | -53.98314 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 591c3345-ab56-3027-921a-cb89695e3d4a | -8.62748 | -54.63355 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba33446b-0e24-3e96-81f4-8b3458be713f | -9.28084 | -60.61769 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27a0ec57-c38d-32bd-9fc9-a2279be2f99b | -8.61717 | -54.62771 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README102.md)
