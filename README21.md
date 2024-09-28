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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32d1a89e-6941-341c-9ad0-3fde96523a1c | -9.5631 | -50.195301 | 2024-09-28 01:08:31 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3d820a5-5ebf-3ba7-9e37-8e56cb280e52 | -9.5436 | -50.199902 | 2024-09-28 01:08:31 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4199cc68-4dde-351f-ad43-f7105defcac1 | -9.5455 | -50.207901 | 2024-09-28 01:08:31 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34c3faf7-1647-3581-adaa-c3ab1880d855 | -10.3594 | -53.785702 | 2024-09-28 01:08:31 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e45701b1-c17c-3cf4-91ea-686e7c9ea7e2 | -10.361 | -53.792801 | 2024-09-28 01:08:31 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 453d9468-9f3a-3464-9612-72e317dec331 | -9.3841 | -50.006199 | 2024-09-28 01:08:33 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d9fbb2a-266d-31d6-8720-73fdedacd035 | -9.3861 | -50.0145 | 2024-09-28 01:08:33 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3517ea50-b655-3508-abc7-d6243a667b4b | -9.388 | -50.022701 | 2024-09-28 01:08:33 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f21e8741-2edc-3a6f-85a2-3c4ef8637af2 | -9.3743 | -50.008598 | 2024-09-28 01:08:33 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4d82dd6-8c42-3be3-9e00-19da3d8cf74d | -9.3763 | -50.0168 | 2024-09-28 01:08:33 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da4f1ce4-85ef-3555-a99c-4573a356cb5d | -9.3782 | -50.025002 | 2024-09-28 01:08:33 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e74af73-6612-3af7-aa5b-690334bd641f | -9.3645 | -50.010899 | 2024-09-28 01:08:33 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f09b2a9-bad0-3060-8bc4-9543408d9f8e | -7.902 | -44.594501 | 2024-09-28 01:08:35 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 04676a49-533b-30a7-82b7-d0952070e855 | -7.8971 | -44.6157 | 2024-09-28 01:08:36 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 06bb64d4-b522-3ebb-a89c-0fae717410d2 | -7.8779 | -44.5807 | 2024-09-28 01:08:36 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b97025a6-c3ff-328b-b114-35059f422ad5 | -7.8827 | -44.5994 | 2024-09-28 01:08:36 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6b645b45-573d-3274-8ca9-735183a06d95 | -7.8876 | -44.5783 | 2024-09-28 01:08:36 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2d9091d8-d5e3-3be3-ba27-5f59f7029dea | -7.8924 | -44.597 | 2024-09-28 01:08:36 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ac3e94fd-0a64-36bd-83fd-77accda568a2 | -7.8829 | -44.559502 | 2024-09-28 01:08:36 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 74bcb484-1efc-328d-8e4c-f3312a16e504 | -7.8874 | -44.618099 | 2024-09-28 01:08:36 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9662d156-a31a-3a05-93d9-3f6d944e4948 | -7.8635 | -44.5644 | 2024-09-28 01:08:36 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 155fe08e-e6e1-3c88-b1a8-f35c3a32346b | -7.8683 | -44.583199 | 2024-09-28 01:08:36 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4ecc29c5-52c4-3d49-b4e9-06d2c4ba6865 | -7.873 | -44.601898 | 2024-09-28 01:08:36 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9732a71c-c760-385e-a481-6e7c08ea9bfc | -7.8778 | -44.620602 | 2024-09-28 01:08:36 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9ee335ba-4c52-3cd5-a02e-d2abc932cd1e | -7.8538 | -44.566799 | 2024-09-28 01:08:36 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8c4240fd-baaf-32d7-9e13-d6b61bc2d226 | -7.8586 | -44.585602 | 2024-09-28 01:08:36 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2bf32caa-139a-3197-90be-499d03f8ebd7 | -7.8633 | -44.604301 | 2024-09-28 01:08:36 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ea10e112-e444-3e23-b9f6-db16bc9dadb4 | -7.8681 | -44.623001 | 2024-09-28 01:08:36 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e5e44737-43b4-3852-b700-cac0e4170a94 | -9.3378 | -50.728699 | 2024-09-28 01:08:36 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b274002-3817-36f6-aa3a-9694280bb686 | -9.3511 | -50.741699 | 2024-09-28 01:08:36 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abd61234-7745-3e3d-b040-f3b2a94ba869 | -9.3529 | -50.749401 | 2024-09-28 01:08:36 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3c94c93-703a-3938-a74c-53aca0522b51 | -9.3396 | -50.736401 | 2024-09-28 01:08:36 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d3fcfa9-4eeb-3b09-a44e-ba7894d8c3a1 | -9.3414 | -50.743999 | 2024-09-28 01:08:36 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caa77104-fc3b-328b-a7b6-44cecf868489 | -9.3432 | -50.751701 | 2024-09-28 01:08:36 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61e24c57-4a43-343b-9586-dd7998a25e6f | -9.3334 | -50.754002 | 2024-09-28 01:08:37 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40dcc8b4-ec88-3933-9e7f-c8cd85422ec3 | -9.3156 | -50.7663 | 2024-09-28 01:08:37 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c3931fd-97e5-3310-afbc-219d0e123647 | -9.3058 | -50.7686 | 2024-09-28 01:08:37 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0901bb7-8e89-3b26-b1a9-86a7a1e86f2a | -9.4445 | -51.4505 | 2024-09-28 01:08:37 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8deca75-b604-3e52-86bc-2d697c44ed0b | -9.4461 | -51.457802 | 2024-09-28 01:08:37 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30b6bf42-39a2-3d5a-9d38-8b15dc28c067 | -9.433 | -51.445499 | 2024-09-28 01:08:38 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ce4c60b-7165-37f3-befd-bdbc9851ea8d | -9.4347 | -51.452801 | 2024-09-28 01:08:38 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2ee8e57-87ba-32cb-a45c-d2b60856eda2 | -8.9788 | -49.8209 | 2024-09-28 01:08:39 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ca78f13-f9e3-37e9-8e54-33336b1c321f | -7.8207 | -45.5397 | 2024-09-28 01:08:41 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7be86da6-b6e2-302b-8008-3fbaeb64d86e | -8.7513 | -49.776199 | 2024-09-28 01:08:42 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 218e7caa-23d0-3df2-8565-edee70afa4a4 | -8.7533 | -49.784801 | 2024-09-28 01:08:42 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88ec689a-dc48-364f-b5eb-d45691b253ce | -9.038 | -51.521999 | 2024-09-28 01:08:44 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb788fc0-034d-3997-81c0-dd97420329a8 | -8.5532 | -49.594501 | 2024-09-28 01:08:45 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8700103-9a36-3918-ae3b-79bf44b2ad37 | -8.5553 | -49.603298 | 2024-09-28 01:08:45 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d549db8-8a5c-359f-8eaf-980fc251024b | -8.5573 | -49.612 | 2024-09-28 01:08:45 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4a41948-6b92-33be-9ca4-c7936cde63ec | -9.5901 | -54.2565 | 2024-09-28 01:08:45 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ddc7e989-4b9a-3b24-b63b-5bd1c7b1397c | -8.7547 | -50.7519 | 2024-09-28 01:08:46 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa6e5dac-777b-3407-9a97-11ef752890f7 | -8.2331 | -49.378201 | 2024-09-28 01:08:49 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1964f092-cd52-3a8f-9c6b-46fb8978d953 | -8.2353 | -49.387199 | 2024-09-28 01:08:49 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fda2e878-d030-36b5-a5ba-a3fdf0867ef8 | -7.1443 | -45.427502 | 2024-09-28 01:08:51 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a2d8770-5627-386f-b117-6f61575cc77e | -7.1485 | -45.444401 | 2024-09-28 01:08:51 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2349f6a0-0fdc-3052-84b6-d26259be8438 | -8.1146 | -49.5303 | 2024-09-28 01:08:52 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71b63934-2856-3ae3-a1dd-a3dfde630a4e | -8.1005 | -49.514702 | 2024-09-28 01:08:52 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 489f4e96-fdde-337b-b36f-7cf2e21062b5 | -8.1027 | -49.523701 | 2024-09-28 01:08:52 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fad9205-872c-3d12-89c2-168a21326982 | -8.1048 | -49.5326 | 2024-09-28 01:08:52 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4d97983-0d61-30fc-b75a-97beb61e2ec5 | -8.8953 | -53.006401 | 2024-09-28 01:08:52 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0ea1f87-d31b-3b36-bc7c-b02454b853bf | -8.8969 | -53.013302 | 2024-09-28 01:08:52 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2e00337-e822-3ed7-a264-c63784089228 | -9.2365 | -54.561298 | 2024-09-28 01:08:52 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6a16c39-fb0b-3b0a-a599-609361bbfde2 | -9.2381 | -54.568501 | 2024-09-28 01:08:52 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e294bec5-666a-38d1-9397-58a9d534c50c | -7.0176 | -45.332199 | 2024-09-28 01:08:53 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d2ead28-d389-37b4-9603-8199ecae3eaa | -7.0219 | -45.3494 | 2024-09-28 01:08:53 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86415145-7fb9-30ed-a02a-e4cec6c8fac9 | -7.3298 | -46.675201 | 2024-09-28 01:08:53 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d8ba05b-f217-35eb-bb63-a50f69ed26a5 | -7.3167 | -46.6637 | 2024-09-28 01:08:53 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a9bdc36-800b-3b25-a648-c3114d73cedd | -7.3201 | -46.677502 | 2024-09-28 01:08:53 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d747c47c-c21e-3dc0-9275-4e09347a0e75 | -7.2607 | -46.603699 | 2024-09-28 01:08:54 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b2f3750-8117-3c2a-8295-0ef6a730c40e | -7.8301 | -49.160702 | 2024-09-28 01:08:55 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 58819f17-5f9e-3922-8f48-87f8f9dc5129 | -7.8203 | -49.162998 | 2024-09-28 01:08:55 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1beb34f2-e48a-3a1a-84ac-affce43b831d | -7.8226 | -49.172501 | 2024-09-28 01:08:55 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 385115a8-1a1e-39fa-951b-f0de56a019b3 | -6.5819 | -44.167801 | 2024-09-28 01:08:55 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6f51366-f5a9-3860-a96e-6835c265afd3 | -6.5723 | -44.1703 | 2024-09-28 01:08:55 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 562786c6-f6a4-3190-beb8-a701f073f3f6 | -6.3216 | -43.421799 | 2024-09-28 01:08:56 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f011d7e7-8659-3688-b110-7814af24e161 | -8.6689 | -53.188599 | 2024-09-28 01:08:56 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c04c55cd-9f50-3e8b-9373-29fb90e29fc1 | -9.3789 | -56.838402 | 2024-09-28 01:08:58 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11a7dc8a-aa2f-36a5-97d6-2a0274202587 | -9.3691 | -56.8405 | 2024-09-28 01:08:58 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ea1fb60-a6aa-3420-8432-ef5e272bf02a | -6.1711 | -43.434399 | 2024-09-28 01:08:59 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87712dc7-63aa-3e2a-bb0d-76c5d93728b0 | -8.5682 | -53.334599 | 2024-09-28 01:08:59 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adf9ee2d-db38-3291-94a0-4f5134a1586a | -8.5698 | -53.341499 | 2024-09-28 01:08:59 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3282517d-458c-33d7-850d-6116ba28ffa5 | -8.5714 | -53.3484 | 2024-09-28 01:08:59 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68f52d95-07cc-38c9-a38e-d315f2bfcbce | -9.2417 | -56.914902 | 2024-09-28 01:09:01 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96202fd8-6468-35b9-8309-2958dbe9e3f9 | -9.2912 | -57.143398 | 2024-09-28 01:09:01 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48fd32d2-a056-3be0-83cf-60af1f86e25b | -9.2933 | -57.152699 | 2024-09-28 01:09:01 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 135aaa3a-2eee-3ebe-99c4-0945e210bf64 | -9.2835 | -57.1548 | 2024-09-28 01:09:01 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 192b9ad5-ae4d-38c6-9dde-ddf5bcbe13e0 | -8.5574 | -54.562 | 2024-09-28 01:09:03 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acdcef61-c6d3-3544-9ce8-fb972a14be60 | -8.559 | -54.569199 | 2024-09-28 01:09:03 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1af0fa9a-4bda-31f0-b3fb-66997c86ba82 | -8.9856 | -57.1511 | 2024-09-28 01:09:06 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ddac122b-1dd0-3942-9e55-7d9a74cb56fe | -6.1782 | -45.429298 | 2024-09-28 01:09:07 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29564b45-8c90-3006-b042-3d0c49922962 | -6.1686 | -45.431702 | 2024-09-28 01:09:07 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 66185ff8-d586-3b06-8acf-48cfab680d3f | -8.3933 | -55.023201 | 2024-09-28 01:09:08 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f14f1fa9-5875-301c-b808-afecaeb970f5 | -8.3067 | -55.004101 | 2024-09-28 01:09:09 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 059559d3-9572-359c-a783-c7f73aad53ff | -9.1454 | -58.894901 | 2024-09-28 01:09:09 | METOP-C | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 406f69d2-7fff-3879-b242-8ace37650621 | -5.7726 | -44.458599 | 2024-09-28 01:09:09 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c679920-6113-39eb-9537-b5956c1b04f7 | -5.7778 | -44.479301 | 2024-09-28 01:09:09 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2254524b-f522-3a75-aa88-2ac28bbe138a | -5.7629 | -44.460999 | 2024-09-28 01:09:10 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dedbca88-c151-3353-9826-4d6244563dc9 | -5.7681 | -44.481701 | 2024-09-28 01:09:10 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8adff34-322b-3cb8-a7ce-6537d1d9a364 | -8.8167 | -58.2173 | 2024-09-28 01:09:12 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e1cdbd5-90ab-33d6-8421-54c0fce00568 | -8.8046 | -58.208801 | 2024-09-28 01:09:12 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README22.md)
