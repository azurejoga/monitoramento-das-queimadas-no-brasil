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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bdac279-5c9a-3386-ba16-4029e85c4c26 | -10.14066 | -52.40688 | 2026-06-30 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0bf37e9e-57e5-3ac8-8eab-90e72082e0d1 | -11.4723 | -47.41518 | 2026-06-30 04:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 290f34fb-9437-3be2-9723-8f9f16728d12 | -9.17048 | -58.07311 | 2026-06-30 04:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 937b2e0d-184e-3d3d-a272-b623a057066e | -7.10508 | -46.51508 | 2026-06-30 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9df68402-e803-37da-8a7d-5bb13a44aad5 | -7.72495 | -45.91277 | 2026-06-30 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8e26ed5-f789-30de-adcb-f847c8ae7277 | -10.13068 | -52.40527 | 2026-06-30 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4f8a26a3-faad-338c-8039-b84f2daeccec | -7.72553 | -45.90886 | 2026-06-30 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b60ae93-f821-3738-a3fa-4aea05f3fac1 | -9.60429 | -56.93144 | 2026-06-30 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a5a003c7-51db-37a6-a564-9d3aea7bc7c6 | -9.6055 | -56.92441 | 2026-06-30 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 490f6e87-f9d3-30c8-8ed3-63683e107112 | -9.20686 | -45.3303 | 2026-06-30 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2bbfbc6-c981-3203-b378-c52efa1c2882 | -9.08847 | -59.43547 | 2026-06-30 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dddbc843-8122-3393-a61c-d35fea09f3e6 | -10.78427 | -54.10926 | 2026-06-30 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d8e2660-0041-376c-a8f4-9c1a56ea97b2 | -9.74975 | -49.02425 | 2026-06-30 04:55:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83c87d6f-f114-3f9f-a3aa-f0353b18907e | -10.29275 | -50.17835 | 2026-06-30 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42a23a4a-123a-3eda-bd86-88fcc81fc83b | -9.20449 | -45.32724 | 2026-06-30 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 216586fc-73ab-3074-9558-0f44cece0313 | -9.08461 | -59.42943 | 2026-06-30 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bfc23a74-f467-3dd3-8486-49d365a8e7e0 | -11.78403 | -47.57443 | 2026-06-30 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d8f7585-612b-33f0-9ee9-252eedaaee02 | -9.75512 | -49.03774 | 2026-06-30 04:55:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 571c80f7-c06f-3595-9504-123072d0625d | -7.64166 | -50.02432 | 2026-06-30 04:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7acf338a-63e4-32a7-884e-3cdbc6a4016e | -10.13012 | -52.40878 | 2026-06-30 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 167484d1-980a-334b-9d36-2216e60c5022 | -9.60829 | -56.93217 | 2026-06-30 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d741b40a-7fd6-33af-9b2e-373feaa2178a | -4.84914 | -42.92912 | 2026-06-30 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eea8e6b0-a34a-38ed-adb7-b924ffa603cd | -9.21284 | -45.33303 | 2026-06-30 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b37e7489-9904-3b3d-b377-59860ceb22fc | -10.37798 | -49.59376 | 2026-06-30 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07f5ca3a-d2ba-38ce-b460-1821ca6d14ce | -10.93664 | -43.04501 | 2026-06-30 04:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 1f51f5cb-623e-345d-8e09-02fea9bff3c7 | -7.42742 | -49.87648 | 2026-06-30 04:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4ffcb727-52fe-3e7b-b0ae-4ca5809acff4 | -10.29836 | -57.13275 | 2026-06-30 04:55:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bccc0393-0717-3e35-9f63-9d18a283c76c | -10.94202 | -43.04571 | 2026-06-30 04:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 9fc55bcc-c088-340d-8e03-5b1bc2c15cfd | -10.13789 | -52.40284 | 2026-06-30 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc407251-6ce8-32d1-b304-0a6122258743 | -9.18985 | -46.63778 | 2026-06-30 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef680683-2d06-3239-b111-00c597ab7302 | -9.1979 | -45.32904 | 2026-06-30 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eda8fff3-b7a6-36c9-a114-584b30fd60ae | -11.58217 | -47.92409 | 2026-06-30 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5336d62a-4f7a-3adb-a875-3c6d23f85abe | -8.60421 | -45.98576 | 2026-06-30 04:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90d395f2-6ce2-3083-8cb2-e49fef5b0b0e | -9.14833 | -58.24886 | 2026-06-30 04:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3feb889f-3881-3ef0-89a2-f428df73998d | -7.74405 | -44.18862 | 2026-06-30 04:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dc34b65-0446-3423-9d2a-0a09641fd2f0 | -11.78129 | -47.57536 | 2026-06-30 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32eeb066-d230-3277-ad3b-3916ba300cb1 | -9.1531 | -58.29903 | 2026-06-30 04:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a1ad61f-7e0a-3d40-bab5-4acf1bec6fa5 | -9.14868 | -58.29823 | 2026-06-30 04:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5c828bb-db35-3a3e-927b-5cbf66729acd | -10.5912 | -55.42172 | 2026-06-30 04:55:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4570a5c5-95d2-31f9-ad6a-3514aec0f97a | -10.53058 | -48.15608 | 2026-06-30 04:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f77ac3b0-794e-3957-a863-dcf898a932b0 | -9.75148 | -49.03036 | 2026-06-30 04:55:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c96c44cf-226c-3cc4-a44d-58b96f72e9e3 | -10.77337 | -54.11127 | 2026-06-30 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18e27a08-5c45-3d83-99f2-32bb34cf8658 | -9.74852 | -49.02568 | 2026-06-30 04:55:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 211a7866-4ea9-3652-84de-781bb5760571 | -9.19449 | -46.63461 | 2026-06-30 04:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ee320c3-3d04-3dfe-8523-d6729378b5cd | -9.19504 | -46.63082 | 2026-06-30 04:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d87d084-f0df-3770-8f84-1885d3f391c8 | -9.18957 | -45.32329 | 2026-06-30 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31d70cda-72b9-37e5-887b-608a26dc7657 | -9.20238 | -45.32966 | 2026-06-30 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82cc7c69-d9bb-3317-9491-db454befd8f8 | -7.40756 | -46.83086 | 2026-06-30 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96f389d8-2efb-3af8-91be-867ae175c7a9 | -9.58157 | -57.01461 | 2026-06-30 04:55:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ef61887-7edb-314a-93dc-4197765ae931 | -9.15387 | -58.29467 | 2026-06-30 04:55:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7c52fcb-87b5-3ef5-9634-b9f106e137ed | -11.77207 | -46.40781 | 2026-06-30 04:55:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 389d282a-b2b8-33ec-bb71-80d371974c03 | -7.72529 | -45.91165 | 2026-06-30 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb8d5ee4-308d-36c9-aa30-3ef03c27b1dc | -6.50211 | -42.22765 | 2026-06-30 04:55:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4fdd499f-7f3c-3989-a59d-43fffd12baf9 | -10.29898 | -57.12924 | 2026-06-30 04:55:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0083999-68e0-3410-b846-e9fb72f702ab | -11.9226 | -43.39462 | 2026-06-30 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c8683063-3414-37b0-a146-345eb0518208 | -10.94289 | -43.03889 | 2026-06-30 04:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| a67edd2b-5743-3fef-9f79-1e12a3788305 | -9.59566 | -56.93356 | 2026-06-30 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8aaf5166-226c-392c-8b84-dad6ba816ddb | -10.9317 | -43.0409 | 2026-06-30 04:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c140ed22-152f-3f9e-a118-8112031c7ae9 | -10.80407 | -48.575 | 2026-06-30 04:55:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d53683ef-8a8f-3c6e-a47d-fa0bb398a087 | -9.19406 | -45.32392 | 2026-06-30 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93ccfc92-4a2e-307a-9023-0045e67a3e18 | -7.74478 | -44.18354 | 2026-06-30 04:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98085fde-164c-37f2-9e3f-52010bb7f662 | -7.42686 | -49.88006 | 2026-06-30 04:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86c64bc2-328e-34eb-b9e8-b2dd63639680 | -9.19342 | -45.32841 | 2026-06-30 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f91e6d3d-6619-3c2f-9b49-c74e644ac89f | -10.93794 | -43.03478 | 2026-06-30 04:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 2a0221f6-068d-319e-bdb4-10ae0e29f8d2 | -10.94246 | -43.0423 | 2026-06-30 04:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| d2aad32d-4624-366f-811e-5f9b6e941e8d | -6.92176 | -51.94259 | 2026-06-30 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c73facb-a726-3f88-b89f-0e50b8f928d4 | -10.7883 | -54.1061 | 2026-06-30 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 48684084-bf7c-38ba-8c5f-9afea8c2ec1d | -9.75086 | -49.03447 | 2026-06-30 04:55:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4e68d99-4218-3057-bfdd-9c1242cf36a1 | -9.32866 | -58.01857 | 2026-06-30 04:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ce5c5e6-49a2-3dc3-9262-77b305fc35cd | -6.89422 | -43.69575 | 2026-06-30 04:55:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16ebeade-319c-3140-943e-51e7a72905cb | -10.80472 | -48.57053 | 2026-06-30 04:55:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e76d474e-5cc2-3355-82fd-a0ca5fd06858 | -9.32589 | -57.83252 | 2026-06-30 04:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 925eb89e-7de4-38ef-9f14-2a3905a07406 | -9.75152 | -49.03718 | 2026-06-30 04:55:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7fb802f-fa1e-323f-80cf-6b9fce7f0c34 | -10.134 | -52.4058 | 2026-06-30 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f31abaf-2c0a-3b51-91e9-a5c084353007 | -10.12291 | -52.41121 | 2026-06-30 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 34e907d8-2f5c-34f7-8117-26d271afd60c | -6.69346 | -51.96037 | 2026-06-30 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2df23594-fa31-3141-adf5-7764867e340a | -9.20897 | -45.32789 | 2026-06-30 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 591291da-d7c9-33f4-b2c0-400c2fa6cecc | -10.30453 | -57.14475 | 2026-06-30 04:55:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8346866-bdfe-3ee6-b781-05e131368bd9 | -9.08369 | -59.43459 | 2026-06-30 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fc11201-ea9d-3fe9-8c29-96e6a0769f34 | -11.47279 | -47.41175 | 2026-06-30 04:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3a84e7e-5070-3c08-aefe-7b720d52d550 | -10.93708 | -43.0416 | 2026-06-30 04:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 628ba36c-1943-30e5-98b8-16f927cbdc53 | -9.19915 | -46.63139 | 2026-06-30 04:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9111c7f9-4743-3e6c-a16b-2ff007f5cdde | -9.6049 | -56.92792 | 2026-06-30 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 31fe14fa-779c-34f8-a424-e3cb6700fbd0 | -9.31857 | -58.02526 | 2026-06-30 04:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ce10211-e5b4-31ef-b570-08917431203f | -9.32793 | -58.0227 | 2026-06-30 04:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82ee1973-b05e-3f2b-93e5-b744d8190e0f | -9.60768 | -56.93571 | 2026-06-30 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 79228192-4bcb-3b36-9124-8d1fe784cf8e | -9.45092 | -50.84221 | 2026-06-30 04:55:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e29f3f47-1337-39b3-9a90-0c9de50b3583 | -9.13848 | -50.90718 | 2026-06-30 04:55:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f478cb6-831f-3323-a036-ae705b7b841f | -8.7035 | -50.71174 | 2026-06-30 04:55:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b400ccfd-9acd-3029-a65d-264f532eea97 | -9.32361 | -58.02191 | 2026-06-30 04:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5cdb4c1-95ec-3253-9c1c-5c54922d9096 | -10.37858 | -49.58979 | 2026-06-30 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3267179a-bb8f-3a5c-95e7-e7dbaa5bb55d | -11.76381 | -47.33945 | 2026-06-30 04:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4f43a86-d250-3de1-b263-e49c72462816 | -8.20773 | -49.86167 | 2026-06-30 04:55:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc29a157-5616-380a-9b2b-de6690bec17c | -9.45148 | -50.83862 | 2026-06-30 04:55:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac5a72c0-9e60-3b40-9c0d-94b4c812f4d1 | -7.43028 | -49.8805 | 2026-06-30 04:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56b274cf-570f-3c16-8375-7d5fba46ae81 | -10.78549 | -54.10177 | 2026-06-30 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 93a633b2-0230-3c37-af31-0b46439f2b45 | -9.45429 | -50.84273 | 2026-06-30 04:55:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7868c7c2-4dd7-3fc6-bd00-4ecf41a66cc6 | -9.33297 | -58.01938 | 2026-06-30 04:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51021aa5-eb67-36bb-81f9-40abeefcfcf2 | -9.09012 | -59.3985 | 2026-06-30 04:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 220486e3-40dc-391b-88d6-cb25ca7bd646 | -9.75274 | -49.02894 | 2026-06-30 04:55:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README11.md)
