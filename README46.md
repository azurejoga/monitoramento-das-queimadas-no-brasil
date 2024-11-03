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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93f0d1af-f962-3f58-8f28-cca877bf4178 | -2.93594 | -49.43181 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bca4651f-e6ee-36d6-aad7-70b14f52f8e2 | -2.9354 | -49.43529 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1ca640d-e89c-3610-9002-f91866f9f657 | -2.93179 | -49.50232 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ea889e4-e1bd-3c54-a065-eeff637ba9d8 | -2.90766 | -49.41678 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b423ae5-2984-39c3-8eaf-4a095db7e2fd | -2.90712 | -49.42026 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef1844d8-11b1-3fe4-9a41-5118ae6f357b | -2.90525 | -49.49824 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0854f5ac-f100-3574-9ebf-64c0d7c30c2e | -2.90488 | -49.41278 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd347710-90b8-3afa-bb86-a205317cc244 | -2.90471 | -49.50171 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 323587bc-81e6-32ca-a8f0-df2dca3eb16a | -2.90434 | -49.41627 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df8153d0-54c3-3c8b-918c-3d4f1a344011 | -2.9038 | -49.41975 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d640a938-2af0-36ed-919e-08ea63412c5d | -2.90326 | -49.42323 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4e12f0dc-1b96-354c-9e04-f99c17356a18 | -2.9011 | -49.24017 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7be9958b-6d79-31ff-b935-f50c4b6a5915 | -2.90102 | -49.41576 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2dfa12bc-7307-3f18-beb3-42cfcb49c592 | -2.90048 | -49.41924 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 692b95e9-102d-3956-88f4-eadebe7d3511 | -2.89994 | -49.42271 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| dd3e67ac-ce83-3fec-adce-72b9bd141edc | -2.89941 | -49.4262 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cef918e7-b63f-3836-8851-7691957d7603 | -2.89832 | -49.23615 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83c90462-1215-3cca-a7c1-a632dd09ac50 | -2.89823 | -49.41176 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17ed6b97-448a-3bae-b377-6f86d6759c94 | -2.89777 | -49.23966 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c18a14d-9cc7-3d8e-985c-60bc1df771e8 | -2.8977 | -49.41525 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5eb21e4d-0471-3fd2-b512-b0abd34fa2c8 | -2.89754 | -49.50416 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c7ac13e-13f0-378f-923b-83945b6ca5f8 | -2.89716 | -49.41873 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e397844-e9a8-360c-a243-1cf886b0564d | -2.897 | -49.50763 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ce30ef6-70e1-3397-97ca-76b059b49674 | -2.89682 | -49.46494 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7fd86c4-2ba8-34af-8c89-f6abf06a6dd0 | -2.89662 | -49.42221 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe76bb21-01d2-3f68-8c53-d8dad6a846c1 | -2.89608 | -49.42568 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0c08d66-32d6-3be2-a9b2-7af410a34642 | -2.89545 | -49.40777 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f9ab97a-0c9e-32e4-82be-89e5ffef2239 | -2.8953 | -49.49671 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1010f99-df55-30ea-99a9-8de243005908 | -2.89499 | -49.23564 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dab44538-daeb-3d7b-919e-7db94105dc8d | -2.89491 | -49.41125 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf9d5bbe-b71a-3d12-9572-9f812a6ef66e | -2.89476 | -49.50018 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4aed05de-a97d-36c8-b563-6968e4258e92 | -2.89444 | -49.23914 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b9fab8e-cf49-3b5e-9b43-60c95b5a90f8 | -2.89437 | -49.41473 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d3fcee4-d3e8-33a9-9bae-fb78dfdc2741 | -2.89422 | -49.50365 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 776e5554-7ef4-3889-a8c8-858a006f36bb | -2.89384 | -49.41822 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 654f7b9b-4cf8-30be-a8a2-38b339cf5194 | -2.89276 | -49.42517 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57c48315-1185-3513-9123-15f16a1ab494 | -2.89223 | -49.42865 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ede8642-dde7-3506-829a-25067d66e7f8 | -2.89198 | -49.4962 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1a8cc22-ed90-3465-b9e2-ed70e668c2f7 | -2.89165 | -49.23513 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0369dbd-b4e7-35e7-b750-f63d6284e8c8 | -2.89159 | -49.41074 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f49c28d2-94d5-3f73-8c59-7d6ab10bed6e | -2.89105 | -49.41422 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64c7eec0-e786-34e2-9bef-d4dbd2795a49 | -2.89039 | -49.37441 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c97acf9-2b4a-377c-ac83-e0db619d360d | -2.8889 | -49.42814 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e98120fb-646e-3b11-b3b9-29e8c1efd26e | -2.88866 | -49.49569 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6d94152-88c7-36ab-8bc3-574d093a4760 | -2.88832 | -49.23462 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7874f9df-8595-3a92-8d21-88e3ca9b0aa6 | -2.88827 | -49.41023 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e46a6a9-f61a-3d36-81bf-143d2e04e293 | -3.69025 | -49.21408 | 2024-11-03 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d8b773b7-0af1-31b5-8693-402d3039c8b0 | -3.61005 | -49.31754 | 2024-11-03 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59660aef-7952-341e-b07c-3e607af08d19 | -3.60951 | -49.32104 | 2024-11-03 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17b79910-7a0d-3633-8e00-c251dcf1fe97 | -3.60897 | -49.32457 | 2024-11-03 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88b3ef83-a2fc-3624-b61a-274d11332803 | -3.60671 | -49.31703 | 2024-11-03 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0831f70e-bc0b-3e0b-94ac-d7c424d67477 | -3.60617 | -49.32055 | 2024-11-03 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c77ee520-7ad3-3766-9874-9758ce61ab67 | -3.60563 | -49.32406 | 2024-11-03 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 10d045da-ea26-366d-8f60-6e44e460a5f2 | -3.60338 | -49.31652 | 2024-11-03 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4f10b361-6235-3faf-953d-7fedac6c03f6 | -3.60283 | -49.32005 | 2024-11-03 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d428879c-73b7-357d-90db-9bc8abc60604 | -3.46586 | -49.69857 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cacaa97c-59f1-3ea6-9d1d-d998d6f1f794 | -3.44722 | -49.73117 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d118a5f7-21d6-37b1-9537-0c9fa820ab84 | -3.44668 | -49.73463 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f28b3619-1e70-3155-a8d8-f19ac2ed1787 | -3.35863 | -49.71036 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d410ce88-cbe1-399c-abae-8934b647415e | -3.35168 | -49.22712 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d190fa06-056b-37ff-9ba9-de6a5c2ce296 | -3.27996 | -49.75843 | 2024-11-03 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3367d9a0-7fe5-3d26-8b19-bda51d460da5 | -3.22485 | -49.47658 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f99d6dfb-2976-3510-8233-e4ed0a8c87a1 | -2.58537 | -49.10524 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 214ae54e-0531-3371-af23-52b10a2d664f | -2.58482 | -49.10875 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b088571-adb4-3954-864e-808f32324830 | -2.58149 | -49.10823 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf5982a7-c73e-3d17-824e-0d93f3a9f792 | -2.57876 | -49.12578 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60330c48-1035-3e23-bbcf-c1a501da5b4a | -2.57542 | -49.12526 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54e24740-4cd4-3a04-9652-ff7c0725907a | -2.57512 | -49.21483 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd63954e-0b38-33f6-bb70-066b6761ae76 | -2.57263 | -49.12125 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf863645-bad1-39b6-a58f-29fb52b80ba4 | -2.5693 | -49.12073 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 459ac2f9-35cd-38fb-ba26-039a95f4d398 | -2.56875 | -49.12424 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4134b04e-d235-3dc8-b7b9-61439b19cf25 | -2.56863 | -49.08109 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5730e20a-9fc1-3e9d-b75a-0d8962cb0ffa | -2.56705 | -49.1132 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f54fc9a3-c448-33dc-ace5-98cfa69588e6 | -2.56689 | -49.24575 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 482c5f1f-bbfb-3df6-85dc-d39c7dc6721c | -2.56651 | -49.11671 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3b34cb5-23c8-32f2-8de4-41430870f9e1 | -2.56596 | -49.12022 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bba58ad8-f2dc-3fba-a1c4-ee98fb7669a9 | -2.56542 | -49.12373 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d28969f9-6190-38b3-85ed-373c3b599b1d | -2.56263 | -49.11971 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a62236a9-4b29-3609-8b69-db4534c9a72f | -2.56155 | -48.95008 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 942eeb3d-51e0-31b0-9df8-7eec60649e1e | -2.561 | -48.95362 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a6fce68-95f7-347f-ab0c-35a2c0eba570 | -2.5593 | -49.1192 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 74ab1cc9-d312-37ff-93c4-33b900cb631e | -2.5582 | -48.94957 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4bb0bb3a-c2f1-3c68-853e-f8a417ac5b08 | -2.54523 | -49.2317 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f9e2a2a-44d4-3e42-816b-f0c3ddfda490 | -2.54136 | -49.23468 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa6c4730-e8a0-3b10-80ee-0c1bea33ba12 | -2.53743 | -49.0619 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62785167-d138-3c55-a7d3-f964f920f6c0 | -2.53409 | -49.06139 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bbc6291-d506-3d7b-8fd7-508567caf119 | -2.53184 | -49.05384 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 99717ae1-30a8-3762-bfae-fe7ff2b189d5 | -2.53129 | -49.05735 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 842418f4-9d76-3cc4-9b18-244a9a9b8313 | -2.50053 | -49.03848 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ec5a0ed-4d82-3456-8bfa-9026589fd671 | -2.49729 | -49.08115 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fd8be48a-a010-3aa1-8635-669746fea4a8 | -2.49679 | -49.10622 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2aacc2e5-7c5b-39de-9010-50b214aa1377 | -2.49395 | -49.08064 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d71940cd-b330-3444-a5cf-99853a4eb0d6 | -2.49385 | -49.03745 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 232e8957-f327-3f67-b150-ab1b9d5764e6 | -2.49116 | -49.07662 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bfae5b0-4381-3956-835d-9c33e251af30 | -2.49051 | -49.03694 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ffad09e-1843-39fe-a34a-f6e18c3e2ee0 | -2.45038 | -49.00915 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 854fd799-c158-3fe9-8d94-5503f3d8b5c1 | -2.44758 | -49.00512 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2be02e5f-8264-3d3d-866b-1a5323dd31d7 | -2.44744 | -48.96177 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b751226b-5c35-3228-8871-21e17933c465 | -2.44704 | -49.00864 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 660ab67f-1445-31ac-80a8-5ef6db662a6f | -2.44355 | -48.96478 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README47.md)
