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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7aa1c704-a069-3527-97dc-204d2277757c | -17.17289 | -56.1879 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1f1a8c17-b21f-342a-aba8-9076a46927c1 | -17.1722 | -56.19381 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f88a6185-fe58-35b3-97a4-d4aaaf5bb9f2 | -17.17204 | -56.15181 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 672ba90a-1a60-392e-9a8f-2d4bed6d1f97 | -17.1715 | -56.1997 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ac0c2c60-a067-389e-895c-98e50057d8b0 | -17.17134 | -56.15771 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 27bb856c-4393-3f60-a44e-5141eee065ee | -17.17081 | -56.20559 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 51e7fcd0-e083-3b9e-ba49-78028639ae46 | -17.17065 | -56.16362 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 47bd7721-4fc8-3264-b056-ccc589b31a86 | -17.17012 | -56.2115 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| a7e6721f-c2d5-314d-9fa2-017a9b93745d | -17.16996 | -56.16956 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7d85617d-0262-3fa4-9355-faa35011af0b | -17.16943 | -56.21734 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| d2ff6d7d-2ef4-34fe-89da-b48ed1f9d428 | -17.16927 | -56.17547 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8d082c58-607a-3728-bba8-21328555478f | -17.16875 | -56.22317 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c2618228-6bbf-326f-9a48-452c5a2f050f | -17.16858 | -56.18137 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 55d2fd43-02a5-38b5-9f89-9fc1969f54bb | -17.16789 | -56.18727 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 62a1a62a-9325-3741-ab1b-60e9e3c1dcfd | -17.16771 | -56.14525 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 89c28fb9-8de6-383d-84d8-6cb9c4e4966f | -17.1672 | -56.19317 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e6f34bae-2768-3352-98b5-7ff9a1b918de | -17.16702 | -56.15117 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| d3c10018-29e0-352b-8d01-1159bf9e8f7d | -17.16651 | -56.19907 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 7f5e6a4b-582b-3186-b945-1a787514e4f0 | -17.16633 | -56.15709 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| cbb91d6c-9527-3c34-9e87-feace8a46bf6 | -17.16581 | -56.20497 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 5f4ba1da-8ea6-3e8b-bf05-09b458ed752f | -17.16564 | -56.163 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 7fc363e8-53ad-3453-8e77-123852ba7d59 | -17.16512 | -56.21085 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 8f525cb3-4d68-3e65-a7c6-835bfeeff243 | -17.16495 | -56.16893 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| d9ae6600-a5de-3a00-a01e-a4c10022b033 | -17.16444 | -56.21669 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 083c1ef8-1098-31e2-94b5-8e73da1a1d0b | -17.16426 | -56.17485 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 122492c0-db92-399b-805d-ff977fb77b77 | -17.16357 | -56.18074 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 894ae500-0f54-38ed-b0b8-e0961c4b0493 | -17.16288 | -56.18664 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 40f06042-10de-31ac-924f-2e995040be1e | -17.16269 | -56.14461 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d9f88ddd-39b6-3f52-9f7c-023927f9e26b | -17.16219 | -56.19254 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| e387e173-637e-32d9-b53c-00a829361d06 | -17.162 | -56.15054 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 40baeec5-493b-339d-afde-381f50fd3f66 | -17.1615 | -56.19844 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 710c700b-5074-3517-bff2-34c2dd3142d1 | -17.16131 | -56.15646 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| c53542c4-100b-3562-8432-a164cb8a7a29 | -17.16081 | -56.20435 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 772c4490-9f7e-3154-9a9a-c239c04ee419 | -17.16062 | -56.16239 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 6976200a-9fe2-3b71-9bd8-3100a04acf4e | -17.16013 | -56.21021 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 33df3e9e-f3b9-3991-9520-f2ee7a00c652 | -17.15993 | -56.16832 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| bcb08e28-47bc-38ec-93e0-ffedc02bf2d2 | -17.15944 | -56.21605 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| e8794362-10af-3c3d-b5bd-0b7cc729bef3 | -17.15924 | -56.17424 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| ad2bc74b-1fcd-3d25-997f-6973ddcf1544 | -17.15876 | -56.2219 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 36a0b5ce-6e9b-367f-9c8e-ea023eb80f6e | -17.15856 | -56.18014 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 5bf0fda7-0c04-30a6-87ac-5b1f98a4435d | -17.15787 | -56.18603 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 095dbcc2-60d6-3941-92a9-a72b8892e359 | -17.15719 | -56.19193 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 5031900c-81be-319e-9df8-9b98e741e8e6 | -17.1565 | -56.19782 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| cfc9077a-1ca7-3588-9fe9-536eb48746b9 | -17.15629 | -56.15587 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 80699250-1dbf-3f3d-9a81-f7ff4b00fc9d | -17.15581 | -56.20372 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 90e3a63a-a0c1-3b67-9354-84ce9d23a516 | -17.15561 | -56.16179 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 62fa94e5-858b-3de0-aa62-bfe3a5094e01 | -17.15513 | -56.20956 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| dd48f373-4e32-3524-80fc-e128b5ee59d7 | -17.15492 | -56.16771 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5d24a939-a0d5-3e9e-a8fa-f548ef10f30c | -17.15445 | -56.2154 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 0b77f39a-40d5-368b-a66e-83fb9f33f153 | -17.15424 | -56.17362 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| c4dcf923-dcbb-3562-8d1d-feca548c5293 | -17.15355 | -56.17952 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 845f3598-0fef-3688-b75e-0052015c8617 | -17.15287 | -56.18542 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 88b2bf05-0638-3817-a7db-1fc15e9862de | -17.15218 | -56.19131 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| afd9b7ad-eec8-38ff-89de-c8419fb2d4d6 | -17.1515 | -56.19719 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 52d6fd8a-ae46-3770-bfa9-208f2195fb00 | -17.15082 | -56.20306 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| be6d3972-2cb1-357c-a8ea-dddc4f648d18 | -17.15014 | -56.20892 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| d3461288-c842-3eac-a959-ea7154a59642 | -17.14786 | -56.18479 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 24d584f4-4421-3815-8d52-d3be1c395536 | -17.14718 | -56.19068 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 15bafc90-b099-3e0c-a5c0-25f80907f3ec | -17.1465 | -56.19653 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| ea0bd874-b169-37bb-93a4-eb425cf9814a | -17.14582 | -56.2024 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 51c656e9-4db0-3929-a760-5ecd7599ff21 | -17.14514 | -56.20827 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 757b2536-071b-3513-a1f3-72f691b9795d | -17.14285 | -56.18415 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| bdfb2b54-f688-30c6-8c53-4513f87d81fc | -17.14218 | -56.19006 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 394626ab-9e72-3220-909b-2aee3fe9d2f0 | -17.1415 | -56.19592 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e5fab5e8-db83-3d8a-95f1-00751ea7aeda | -17.13947 | -56.2135 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 30fb20c7-2ec4-3e3d-b0d5-383329b7bd11 | -17.13785 | -56.18353 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 23333d98-a5d0-3366-8c8a-d2ce0059d46c | -17.13717 | -56.18943 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 03cdea16-156b-3731-bff5-419d7b37e3ee | -17.13649 | -56.1953 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 18ca4e47-c123-312f-b0b3-7050aa535063 | -17.13284 | -56.18291 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 39403cad-8b9d-3cf2-8c2b-e3d5a7f73e63 | -17.13217 | -56.18881 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 84d18cb7-6f3f-390d-a859-25a4d9b315d7 | -17.1182 | -56.1329 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 21cfe823-1524-3ff5-968f-82fb471dd709 | -17.11317 | -56.13225 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 87dbacbe-7d74-34fe-8217-37b72beaa650 | -17.10845 | -56.73021 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 5a7172ba-c737-3a3a-a583-3148a9c824fb | -17.10746 | -56.40309 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 75e95140-817e-32c8-b2e8-3754be15ff4b | -17.10428 | -56.72417 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 0ecd4a18-9ea9-3297-8b92-9bb5628b6cbd | -17.10363 | -56.7296 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 412b5822-ac12-361c-a4fb-3369653d3692 | -17.10298 | -56.73502 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| aa95acc5-7c05-3088-ad90-733f0565605d | -17.10168 | -56.74584 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3b2464da-a289-36cd-8e48-23d9aef2d20d | -17.1001 | -56.71813 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| c31fc54e-bf7b-396f-8b8d-1fca981d056b | -17.09945 | -56.72356 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| cc23706a-f84c-394b-88b8-529ba5bae016 | -17.09881 | -56.72898 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f6183bdb-d0e5-3191-a763-fd8e412403d7 | -17.09816 | -56.7344 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e4cbc299-9c46-351c-b02d-e93ff05844aa | -17.09528 | -56.71752 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| edd21594-ef23-3469-9e31-6b2153928353 | -17.09463 | -56.72294 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| e46bceb5-bf2c-3263-a6b6-a064d0d1cadd | -17.09398 | -56.72835 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| fdfd8181-f2db-3dff-b92e-fc5219f38478 | -17.09334 | -56.73378 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 63291840-43e4-3917-b500-51c6d3b58c24 | -17.09269 | -56.73919 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 3519f5ca-83db-3221-b1a9-29d820bfb571 | -17.09205 | -56.7446 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 61cb89ea-27b4-3deb-857d-8c16d9810dd1 | -17.0914 | -56.74998 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 26d5361f-b77c-37ac-8f25-bb43b70eb4d0 | -17.09045 | -56.7169 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e842b73b-bfe0-3dfa-92fc-87e683fe8217 | -17.08981 | -56.72231 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 3006fdc6-d2ff-3f62-ba74-084bf442413e | -17.08939 | -56.11716 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ebcea63f-53eb-319f-93e0-b845fd3b607f | -17.08852 | -56.73315 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 17cde33c-40a8-30c1-8a4f-cfbcb83ea873 | -17.08787 | -56.73857 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2d1a38bf-fe67-3923-912d-3986690262f1 | -17.08723 | -56.74397 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 00c3d228-bcfb-38e2-9bc8-500f02e73726 | -17.08659 | -56.74937 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b0ad1a12-337b-3eb0-92f9-439386b30758 | -17.08595 | -56.75477 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 10729a63-13f0-3f08-abdd-8d59c7f4d80b | -17.08562 | -56.71628 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a9bc8c47-0d49-3f84-8493-a72e742c58a2 | -17.0853 | -56.76015 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 57d307b7-ea7e-3f0b-bb15-66dfebfd0722 | -17.08503 | -56.11464 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |


[Clique aqui para ver as próximas entradas](README146.md)
