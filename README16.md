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
| dde83554-e4e5-312b-972c-be70f8b6b348 | -7.71454 | -43.78917 | 2026-08-26 04:08:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bef90356-959e-380c-b042-07f77dc6cc68 | -11.16118 | -54.00645 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f864b665-3ce8-3009-9494-7f1d97251144 | -7.4503 | -43.09637 | 2026-08-26 04:08:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 411496b3-375a-3603-a6e1-9d1a34bd3345 | -7.27655 | -44.07932 | 2026-08-26 04:08:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce91d6c9-8b66-3d5a-b3fc-9b80c312ead6 | -11.42757 | -44.52698 | 2026-08-26 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2afcdcf0-cdd2-3a88-9433-e20a0eb15357 | -7.27283 | -44.07873 | 2026-08-26 04:08:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 983733cc-a70a-30bb-82c6-53cbe606e775 | -11.96909 | -47.74952 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d9f9a89-524e-34ca-b811-2742f06f9764 | -7.3122 | -42.98837 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a4439321-2e19-3fa2-9765-16931f03cc68 | -6.91371 | -44.66391 | 2026-08-26 04:08:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bccfe372-1487-3739-a6fa-377a658b75f3 | -12.67194 | -48.42232 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d7d2428-47b1-3fcd-a7e0-1da5b3d58542 | -7.75513 | -44.74816 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1cf3cbc6-0fa3-34e1-af99-2c08be47fbbf | -7.19573 | -42.74594 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 367ba573-5ec8-3cea-ba4f-9611a3e8748d | -11.28648 | -47.07359 | 2026-08-26 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37f114bb-ce1c-3853-980a-f0ad469b8c18 | -12.02581 | -46.02919 | 2026-08-26 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7708e268-cec7-32ed-a82f-b52b6d642b4a | -7.28996 | -44.0907 | 2026-08-26 04:08:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1253c350-c015-397b-a5ec-096adf358b4c | -12.67675 | -40.61129 | 2026-08-26 04:08:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 171ec48c-a530-34e4-8806-ceeafacab9c8 | -11.99467 | -45.92925 | 2026-08-26 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd1b8e41-f3f1-3345-82d6-f80e818336ef | -7.30516 | -42.96385 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 46693094-ae83-35e4-8259-b3a37c3f8b93 | -8.12109 | -47.47203 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a8cff8f8-e24b-3bed-a25f-890cb8031a7c | -11.15694 | -54.00475 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 740627fb-e65b-338d-bcfc-c7290afbfc6a | -7.51188 | -44.95567 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1456347-2c43-3866-b7db-30b8cbee1e3f | -10.76615 | -54.03847 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| bf166b31-5a71-3e0d-bbbf-ab5bde3eaef8 | -10.37617 | -45.06197 | 2026-08-26 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 30.9 |
| c8d4632d-0d19-390f-a054-f7febcac8980 | -7.27031 | -45.35895 | 2026-08-26 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ff79558-62b8-3f07-a277-2190eaebfb6b | -6.35868 | -46.11965 | 2026-08-26 04:08:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 383abdc3-f91d-3eec-b788-5d3944cdabad | -8.84364 | -38.76607 | 2026-08-26 04:08:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f3513bcc-240a-32dd-b0aa-bcba170d17e7 | -6.9565 | -42.10192 | 2026-08-26 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7f18c604-1e18-37be-b00c-4f280991c1dc | -12.76717 | -46.44322 | 2026-08-26 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b264cc4c-10b6-357f-88c8-8754ce453841 | -11.80656 | -47.66997 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c8d3335f-7f7f-39d6-bc10-adcfc0fb1d5c | -12.66079 | -48.41553 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f05a243-6e87-3cf6-aa41-56d4822fcb73 | -7.28012 | -43.02926 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c2a72d95-2c71-37da-bbbb-b47c9684da81 | -7.30489 | -49.54653 | 2026-08-26 04:08:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8da4d80c-89b0-32d4-9d5a-c9ae9e216b30 | -11.81507 | -47.67832 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a8df92b-982b-340e-bf01-bb5541a5140e | -7.86187 | -46.11082 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3394ffd4-1d81-3095-a81a-40bf339becfb | -7.86771 | -46.10635 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60812983-1629-3c58-8e1f-5672f6d18d72 | -12.67679 | -48.4046 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a70cb78e-0f13-3e8a-a87c-a6fc660bf279 | -12.75648 | -46.4576 | 2026-08-26 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c54f097a-9c30-374a-bcd5-9348431f86f6 | -7.45765 | -43.118 | 2026-08-26 04:08:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 96b04b17-300b-360e-9e78-0bb0c0cf436c | -9.56508 | -49.26324 | 2026-08-26 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a45a46df-d10b-33dc-ae76-cecf9522dbe4 | -8.77185 | -49.974 | 2026-08-26 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a5edef8-8209-34ee-9cc6-2a2a81b10218 | -7.1646 | -42.80482 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2e3e52a1-8524-3861-9d19-2456511f4e54 | -8.08335 | -45.90693 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2642f08f-c6f4-3b99-9a00-11edee71b61d | -10.751 | -54.01118 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b1a3473-6ea6-3dbb-a4e5-91243357b60a | -7.74888 | -44.76204 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f39fd609-39af-39c9-8fc5-58d5765d1b39 | -7.09224 | -42.17278 | 2026-08-26 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 71e76b2d-faa5-3dad-8ce6-847c91d88b0d | -7.17954 | -42.73539 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5e53209e-a9d8-3140-ba39-8802ace8d8ce | -12.74972 | -46.47285 | 2026-08-26 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f28c0af0-6757-3af1-976d-dcff1beceaa9 | -6.91291 | -41.52726 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 466f7804-5292-3267-8a57-3057323d7acc | -7.28028 | -44.07992 | 2026-08-26 04:08:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1880a939-dcba-3b92-9862-437e4cb3e9c9 | -11.81749 | -47.65892 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2591f8f-6980-328a-9798-08808970f1f7 | -12.67064 | -48.41259 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 53090149-7bd7-3037-b94e-36160801e78b | -12.758 | -44.25567 | 2026-08-26 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89bfdcf3-a6bb-3bc7-92a8-aec697d6fff0 | -12.74676 | -46.46644 | 2026-08-26 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bfe4ae1d-970d-3e32-ae8e-3e11e6a2e694 | -8.13362 | -47.50831 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c59e35e2-96bf-3e8a-a8b4-239b811c2d4e | -11.49053 | -45.10811 | 2026-08-26 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f16bfabe-889b-347e-8340-31c65f2d042e | -12.76535 | -46.4536 | 2026-08-26 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6c3dfe55-b737-3639-adb7-53c0374a66b3 | -8.81671 | -49.60828 | 2026-08-26 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b57a8648-3384-3337-b8a2-9d6824dbf68b | -11.81372 | -47.68018 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66077dfb-b753-3f0f-8f58-92a9069aa3ee | -8.08684 | -45.91135 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a3b66f0-1acf-3528-ac6c-7de417181c40 | -12.7291 | -48.37285 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b78d898-b68d-3e9d-ab82-4ea50669319a | -7.31154 | -42.99236 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1a9359f5-7ef6-3641-809b-295f16245fe3 | -7.75737 | -44.75847 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 08c4c3e1-62c8-3d7f-8241-8b2198dadf74 | -12.58763 | -47.93393 | 2026-08-26 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e4daca3-ea44-3513-a710-64535fef00da | -12.66165 | -48.41093 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a8bf0f56-88e5-3310-a115-089f310ba13f | -10.58268 | -46.3105 | 2026-08-26 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 460bd591-ff89-38b3-8357-f86b7be0f6bc | -12.73895 | -46.48751 | 2026-08-26 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 328d74bb-cb27-3c04-90a7-4ccd988e249f | -6.25881 | -53.37083 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 09cce686-d48e-304e-944c-4123a03d7f91 | -13.33861 | -48.21156 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b29cc15b-0703-39a8-ac34-4bd0e77d5ac7 | -8.1653 | -46.18921 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c51c956-bd51-3291-8a26-f72cf58c8ba1 | -13.33577 | -48.20225 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f14d1b6a-33a0-31cc-923f-1cc9a423017a | -11.573 | -41.43336 | 2026-08-26 04:08:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dd3f8fe8-e5da-3602-a3d7-450bcd3ce2f9 | -6.25758 | -53.3792 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ec56eb97-3d61-3382-976c-0fff95ec4d8c | -6.59365 | -43.318 | 2026-08-26 04:08:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a2a783bb-28d7-33c0-b76a-99205974aa5c | -10.0387 | -46.04764 | 2026-08-26 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb41355e-a06b-3211-afd3-ba1f8f3be441 | -6.26452 | -53.37849 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6514d2e7-fcd7-3221-95d7-e29b9f94eac2 | -6.29958 | -53.57529 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87fb9e19-93d6-3de1-9e94-2d8a99905665 | -13.363 | -48.20142 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 903ce2df-bb9f-34fa-9fed-7ee42415390d | -13.37036 | -48.21051 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8f68fa8-996d-3de2-97b6-d0e940c18484 | -6.9559 | -42.10561 | 2026-08-26 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6adec7d4-484e-30da-b587-5bb42c2c79d7 | -7.19795 | -42.75427 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6eee9110-190c-3d7a-8936-6f6eca84433c | -8.63708 | -54.74988 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c12f200-f991-35d8-baf6-ecf31d085cfe | -9.59935 | -55.12283 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 12591a26-1752-3dbc-819e-b62177efecb7 | -8.16972 | -46.19383 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f8c83575-c41d-35c4-90a9-eea72832bfbd | -12.66615 | -48.41175 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9761875d-ae6d-3bf9-94a8-ffb04fce1ace | -9.44549 | -51.67416 | 2026-08-26 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9f11818-0407-32a5-a593-aae6b92cafd4 | -7.19287 | -42.7415 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9929cc82-d489-3611-b3e9-1823f7fc016d | -11.33695 | -42.12544 | 2026-08-26 04:08:00 | NOAA-20 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 077e55e0-1c8a-3b31-9ca2-4f4c05fdfc6b | -9.02665 | -50.77928 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 08887502-6434-399a-87ce-6f55ebe451f0 | -11.81978 | -47.65282 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fa14b94-8707-3ee7-ae63-c11112c302d2 | -8.64151 | -54.75149 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dfd26ad3-ab76-3320-acda-963922ec1d44 | -8.76712 | -49.96963 | 2026-08-26 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3d33a67-cf13-3447-b998-75c1bb8f74b1 | -13.33682 | -48.22144 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bdd3e86a-f7a8-30c4-9fe5-5b7a3e2365ce | -12.65855 | -48.41918 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d3591b91-b8ad-35e1-bbae-7695c99dd608 | -10.58203 | -46.31419 | 2026-08-26 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13153b58-95e2-3b1b-8a6a-1b91fcbc59df | -12.65981 | -48.42068 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4269246e-bd61-3a72-bb84-bba47733f1d5 | -12.73388 | -46.46996 | 2026-08-26 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82634582-52c5-3a5e-b287-1b93b07ab96b | -9.65027 | -48.31829 | 2026-08-26 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5a247bd-393c-3d6b-a76d-1279e242381a | -7.44965 | -43.10033 | 2026-08-26 04:08:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 376adc55-009b-3aa1-8320-ec2ff3c46dd4 | -7.44769 | -43.11228 | 2026-08-26 04:08:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 24ae2475-8b9e-316f-9ef6-46346641b887 | -7.20144 | -42.75485 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README17.md)
