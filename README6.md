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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ebe6a92-0875-3563-8d14-8e33561812c9 | -11.38255 | -54.35185 | 2025-10-08 00:52:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 831d8667-444d-3017-a98c-e889e8f85b56 | -14.96771 | -49.92299 | 2025-10-08 00:52:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3d70f876-9fd0-35d2-9eba-772eff6ebb98 | -13.09045 | -47.99969 | 2025-10-08 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d0f6b21d-50e7-33b3-8dbe-a96c0d33bffa | -9.97559 | -48.78992 | 2025-10-08 00:52:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 24fb6498-c9c8-3e68-b525-1f5bd187b9c8 | -10.86718 | -53.7386 | 2025-10-08 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| cb759b52-bf7c-3aea-b27b-e1f3603d4656 | -13.84084 | -51.86929 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6a4229cb-5927-37a1-a9e2-abb87d2a403a | -12.01657 | -45.20218 | 2025-10-08 00:52:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| e21bd4f7-4a72-3409-b888-5446fbcf89c0 | -11.15657 | -54.85917 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 054d450f-9eb1-3a25-9a6c-429730904dc0 | -11.68647 | -51.00956 | 2025-10-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 53670c71-d42f-3487-b5da-77ae773d8e65 | -9.66883 | -49.93165 | 2025-10-08 00:52:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 94db89b1-098e-3e4a-b811-5c24543004df | -11.17728 | -54.87556 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 1fcfa3a1-3933-3764-bcbd-f28bbe0c4cb5 | -11.14876 | -54.86995 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f0b3cb83-d190-3dd7-82a0-40a5fc15d467 | -14.8299 | -48.42364 | 2025-10-08 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 177e1f1c-515b-3f65-904a-6ffc54bcfad3 | -11.18638 | -54.87433 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| ae8ebcd9-9e52-33ab-a909-b60e5591213c | -12.15589 | -51.43903 | 2025-10-08 00:52:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9f584a44-6f97-3d3d-a414-4af8df5bda79 | -13.80629 | -45.79009 | 2025-10-08 00:52:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| d2fb5915-829e-3da9-a338-5a3b5545deb3 | -10.92737 | -51.03572 | 2025-10-08 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 29ce6696-4e50-3fc5-8847-a831662cd366 | -10.64316 | -47.44891 | 2025-10-08 00:52:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 784c100b-989a-3b9a-8f9d-ae15bab35c46 | -9.09499 | -47.95493 | 2025-10-08 00:52:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 53b9bd21-8578-3764-89c6-6426de304e16 | -10.23257 | -52.69855 | 2025-10-08 00:52:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 7fe22fe4-a1ce-3fc7-95c7-0a39d7003104 | -10.47156 | -52.16928 | 2025-10-08 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d86d460a-c2a8-3dc0-bbe3-b6880ce44369 | -11.18767 | -54.88387 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 156.9 |
| 53e68f0b-e3b0-3162-8f93-2b94e1e8a539 | -12.03081 | -45.1996 | 2025-10-08 00:52:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 37.0 |
| afaa20bd-240f-3b17-8b77-cec7070a39e5 | -10.34759 | -51.55826 | 2025-10-08 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| df7939e2-6906-3293-b763-651c32d34692 | -9.8159 | -57.95399 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2ab6c3d6-27f4-3790-89cf-0e149d75656b | -11.15911 | -54.87814 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 88d6006f-9ff0-3d5b-97f0-aed717da6b0e | -10.502 | -49.13971 | 2025-10-08 00:52:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| f7cb46dd-d89e-3900-b202-1370b60736d8 | -13.75012 | -45.76269 | 2025-10-08 00:52:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 80eb13ec-2838-334d-ba7b-bb2b669fce66 | -11.45461 | -50.21121 | 2025-10-08 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 622b37e7-1888-3ae2-a648-a60cbdada255 | -14.50313 | -56.01052 | 2025-10-08 00:52:00 | TERRA_M-M | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b4a5fff0-0abb-3cc9-8a9b-2ecaf9c8a3c1 | -10.90552 | -51.01801 | 2025-10-08 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7792070f-2da6-3526-86b1-c891307dfc6f | -10.97705 | -59.02667 | 2025-10-08 00:52:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a5ff7dec-f69b-3c25-95b4-aced3ace39a2 | -13.72947 | -45.72124 | 2025-10-08 00:52:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| f092f836-5245-3654-bd8d-86f9e2404619 | -12.3786 | -50.30439 | 2025-10-08 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 97a7c8da-fc71-3629-9298-16f3505aad05 | -15.1551 | -52.76329 | 2025-10-08 00:52:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b440905e-e7a0-35c6-b0d2-ffd27f3b86c5 | -14.68762 | -48.41746 | 2025-10-08 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| bd480001-1c05-3fbc-9994-11a903dd3b81 | -14.96131 | -49.94522 | 2025-10-08 00:52:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| daa2906f-c3ae-36a9-bbc9-1fe9931d6ab6 | -11.69432 | -50.99795 | 2025-10-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| eb4925e2-0657-3340-934e-5daebdee258c | -13.46185 | -50.40838 | 2025-10-08 00:52:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f600ba3d-ac49-3377-847c-3df5024f6c2f | -15.20521 | -56.77214 | 2025-10-08 00:52:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1d98ffc2-90cf-3254-afc0-0349452e77ad | -11.12068 | -54.04766 | 2025-10-08 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 5de28d9a-896e-3ffa-9f15-1c4365b6aff2 | -10.91496 | -51.01655 | 2025-10-08 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 1252a23f-57d0-33d5-928f-d4c1e88d4e05 | -13.80999 | -45.81161 | 2025-10-08 00:52:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 1e0e6c3a-8516-35f1-acfa-57e90607e08f | -11.68497 | -50.9994 | 2025-10-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 141.9 |
| c0d5d539-20c1-3f26-8632-7731e65f955b | -12.0211 | -45.22803 | 2025-10-08 00:52:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 672592ef-1041-35e4-9272-86d87ffef7db | -9.39816 | -45.94624 | 2025-10-08 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| fba75a98-56fc-3322-9eb8-4683b8eae950 | -7.35558 | -43.85913 | 2025-10-08 00:52:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 502eda9b-9827-350d-a41e-41d4fde544ca | -11.13186 | -54.88202 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 1f761eff-5a9b-3ea8-82cc-0fac31e373e8 | -9.39478 | -45.95409 | 2025-10-08 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 4827274b-a0fe-3e9f-a5b6-8baf3b6d582e | -11.33584 | -56.21476 | 2025-10-08 00:52:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 737e0eca-3210-3a9d-8ad5-7361bde6d327 | -9.61886 | -54.31891 | 2025-10-08 00:52:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 31e10d28-757d-3f77-ab66-d83e163b4953 | -13.74641 | -45.74073 | 2025-10-08 00:52:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 31f5a128-94ab-37c9-b507-950294e13ac3 | -10.90559 | -50.65565 | 2025-10-08 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d0178125-db7d-334a-8ae7-3e185ff58557 | -12.38824 | -50.30285 | 2025-10-08 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 9993f343-1a6b-34ca-a5e0-ce36d2c93c48 | -11.01662 | -51.21352 | 2025-10-08 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e5f0b2fb-ba62-3823-b738-857779b384ca | -10.43258 | -51.63965 | 2025-10-08 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4fcda40c-3202-3f3a-9b56-823206c7c3a5 | -9.78104 | -48.28782 | 2025-10-08 00:52:00 | TERRA_M-M | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2741fc55-bc84-3397-97a5-5914b7515e9d | -11.1118 | -54.04893 | 2025-10-08 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 2655486f-51c2-31f8-a1e6-13ebb80dd09d | -9.13552 | -50.06439 | 2025-10-08 00:52:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| cfecb721-0d26-3863-8bb0-0838c5b9a908 | -15.17459 | -56.8257 | 2025-10-08 00:52:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 193de838-9965-352f-a000-bb95d3e896d2 | -11.69682 | -46.38475 | 2025-10-08 00:52:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 4481de21-a5ba-31f6-b92e-b3dab02df054 | -11.34414 | -56.20227 | 2025-10-08 00:52:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1ec090d2-6975-3517-b813-025d1b30d896 | -12.30258 | -55.10247 | 2025-10-08 00:52:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2dca403b-47d3-368a-93a8-287f2c650aae | -10.34525 | -58.89231 | 2025-10-08 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3b0afc81-f2bc-356f-9356-fee710d933c0 | -7.8028 | -46.0321 | 2025-10-08 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 9c47231d-1ddc-3b61-ba7e-3bcc6b244b09 | -14.96291 | -49.95589 | 2025-10-08 00:52:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| af1a1b67-9495-3917-a045-687c33e8fe7c | -15.05876 | -57.18099 | 2025-10-08 00:52:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6430130a-524e-3d13-a717-1038bcc209a4 | -13.84974 | -51.86794 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f08e15df-82cf-3a3e-94f1-0855ff344630 | -11.14349 | -54.89981 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 58b14ffc-7e91-3cbf-af6d-de3af3f6c168 | -13.7257 | -45.69905 | 2025-10-08 00:52:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 191.3 |
| 92dacc2c-747e-36c3-a267-eb16466f2032 | -9.76095 | -47.69321 | 2025-10-08 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d13aad36-770a-33e8-9dcd-d40237b9aee7 | -12.39774 | -51.13374 | 2025-10-08 00:52:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c3d44f31-95a2-3948-b3e6-18e10ddb397a | -13.20706 | -51.69633 | 2025-10-08 00:52:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 185d52b6-9bd7-3ee4-a128-9b19f60da054 | -11.11058 | -54.0399 | 2025-10-08 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a99d4eb8-5d95-3fac-b1b2-ba568105def0 | -11.67259 | -50.98048 | 2025-10-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| a5ff531b-be1b-33f3-b6b8-033e65ab1ef2 | -12.39235 | -50.30752 | 2025-10-08 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1afaf82f-fe95-3233-adae-8bdcde3d2364 | -11.69282 | -50.98777 | 2025-10-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 4bbec2b2-9b42-3ad8-816e-95a528eda008 | -14.7001 | -46.08445 | 2025-10-08 00:52:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 23.0 |
| a6b678ae-5489-33a0-8439-6984e8015046 | -11.16948 | -54.88638 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 874de2fe-ac35-37d0-bb6b-c8e2523b08f9 | -13.42168 | -48.86228 | 2025-10-08 00:52:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 48.2 |
| e8395064-e2c3-36bb-aab0-a8de153b8a3a | -14.95498 | -46.83133 | 2025-10-08 00:52:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| e5637d4f-2f52-3fd2-bded-cce83022bd61 | -12.2502 | -47.86304 | 2025-10-08 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 6bfe596f-e417-3db5-b46f-74179ef1ad06 | -14.76615 | -46.01192 | 2025-10-08 00:52:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| eecb3b8e-bf38-3c01-9cd7-77cdcda40107 | -11.17206 | -54.90556 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 825df4d8-f4bf-3030-9192-7534b60d1220 | -11.12656 | -54.91188 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| af5be5b9-f166-327c-ba14-4f470dccddad | -9.63802 | -55.1365 | 2025-10-08 00:52:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f58a0fb4-c781-3fcb-9efa-ccb0aaac09d7 | -12.98215 | -51.10075 | 2025-10-08 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| df0e3d57-58dc-3586-a125-6638100557db | -9.25961 | -56.28547 | 2025-10-08 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b8cea2f5-a154-3bac-b842-ffe596c071a9 | -11.70333 | -46.35535 | 2025-10-08 00:52:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 16060a8e-ae0d-3bf3-b772-9681df2f97d0 | -11.93931 | -51.47515 | 2025-10-08 00:52:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 89b0188c-9ca0-3f9b-b9e5-09ad4e4d8adb | -14.38537 | -46.01497 | 2025-10-08 00:52:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 804d0d73-82cc-37d1-aa26-8b99c7dba0c7 | -13.23753 | -47.1967 | 2025-10-08 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| fb606e94-17e3-3ae2-9c5b-1897fbc13412 | -14.71327 | -48.40776 | 2025-10-08 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1d96fd89-0990-31e1-be28-d4e37326ca83 | -11.17077 | -54.89597 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 5737ea45-2862-3926-aab3-2b80fac7a087 | -8.44763 | -54.71097 | 2025-10-08 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 243e7eba-8cbf-37c7-952a-9fe03e3b2bed | -11.18896 | -54.89344 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 24.5 |
| f944ea51-28b4-331e-8fac-78ac5a2292fe | -11.68195 | -50.97903 | 2025-10-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 231.5 |
| 1f1ec2e4-f4a8-3187-87db-1991038ef545 | -9.69663 | -51.97709 | 2025-10-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 14ab8af4-ea31-3586-8b04-74fc4e975ec9 | -12.15728 | -51.44868 | 2025-10-08 00:52:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bfad1afa-f9c9-3fc6-bfea-194d547ef9f5 | -11.68346 | -50.98922 | 2025-10-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 273.1 |


[Clique aqui para ver as próximas entradas](README7.md)
