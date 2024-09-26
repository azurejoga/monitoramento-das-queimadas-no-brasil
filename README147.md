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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74a4bd53-40d4-3095-bcc1-71f813a08f5b | -17.06556 | -56.17194 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| f6c867b4-b305-36e2-9cbf-c9f476885954 | -17.06554 | -56.19412 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 615544c0-0d31-336c-9447-b9f29b253656 | -17.06501 | -56.17554 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 4f2bbd73-e20f-337a-a015-746398f11552 | -17.06498 | -56.19772 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| dd94425c-3fbb-3ce7-b65a-b0c7640ddc30 | -17.06447 | -56.15705 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c1a3c7c3-f2d2-38dc-a5e1-b3292f441423 | -17.06445 | -56.17915 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 663e2f0c-6138-3bbf-859f-b26d96b32169 | -17.06442 | -56.20132 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 559f88a6-daf9-3d5f-bcfe-fc7113b744bc | -17.06392 | -56.16058 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b1be28a1-542e-3d3c-a6e7-2344c0542e86 | -17.06387 | -56.20492 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b990b043-1528-3a52-b752-af75837f1ce2 | -17.06334 | -56.18636 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ab0d8e52-0a32-300f-b3f1-7b87be1d9b03 | -17.06283 | -56.14568 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c787005f-6c6c-3ef9-a38d-66a1b97168cb | -17.06223 | -56.19357 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b4ee166c-dad6-39ec-9904-132924eaedaa | -17.0617 | -56.17499 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 7e7b1fea-2166-3d9d-8cfb-e4d1e9de8b79 | -17.06116 | -56.15649 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1dab6b2f-7bda-3745-82f1-3dfd49cc7625 | -17.06111 | -56.20077 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 599fd20d-0b1e-3220-a24f-322ca7017d06 | -17.06061 | -56.16002 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9c5c7686-53d5-3bf1-88a8-e6329c6a6951 | -17.06005 | -56.16362 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c6c42342-be4c-3b90-950e-cc30f1a7f834 | -17.06003 | -56.1858 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f1b06f8f-1996-3e8f-8aba-7c205e2e104f | -17.0595 | -56.16723 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 62f03f08-32fa-349d-81ec-3cbf83f45f58 | -17.05947 | -56.1894 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| b16aba3c-49d0-31d3-beed-1902751e2d18 | -17.05894 | -56.17083 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| fc36cb4e-41dc-3121-8f98-9b077f10c3d8 | -17.05841 | -56.15233 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 31a18851-7cf3-3e30-926f-36b39edd0111 | -17.05839 | -56.17444 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 728adac8-e5f1-3425-a313-cca978f87b85 | -17.05785 | -56.15594 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5a11a3de-a4e2-3680-a37f-dc8c6ca0e64c | -17.05783 | -56.17804 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e4ec047b-ea21-397b-85b3-495051255eec | -17.0573 | -56.15947 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a5eca2cd-50af-3777-af9c-ef9631117426 | -17.05674 | -56.16307 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 169e2e8b-0b67-39c1-9899-699b2710d4cc | -17.05672 | -56.18525 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d9980fc2-c8a7-356f-8dfe-55352eaa7f30 | -17.05619 | -56.16668 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e4017b71-c0af-37c7-a848-42b9bfecc956 | -17.05616 | -56.18885 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| e99aeaa7-0711-3d70-8b43-6e14f8edbee0 | -17.05507 | -56.17388 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a76b0789-ad86-3e11-ae08-664dda6d177b | -17.05454 | -56.15539 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 00ff9085-d9b5-3653-aa90-2541004f719d | -17.05452 | -56.17749 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 91c9bb12-cf94-317e-bce3-5a8750f7520d | -17.05399 | -56.15892 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0bb41d0d-0128-39a1-ad9c-7db62a31bb94 | -17.05343 | -56.16252 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| dce4ed1c-17fb-3fff-a101-6c79fd19388d | -17.05285 | -56.1883 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 06a4b458-ed20-31b5-8291-ecd66c0ed90d | -17.05232 | -56.16973 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 543136b8-2435-3542-8299-19229e8fb0ea | -17.05176 | -56.17333 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1b50b9d7-2cb6-3d03-a0e0-5944ab484b7c | -17.05116 | -56.15493 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1830a625-e964-3a55-9006-3b8d785a782e | -17.04954 | -56.18774 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 89d6482f-54b5-3b81-8222-76f0626cf677 | -17.04506 | -56.17239 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ccd998bb-5d50-33e3-b076-72ddff3f20e5 | -17.03621 | -56.18569 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 5de82da1-2c77-3a52-8b2c-7e24a6698482 | -17.12348 | -56.19271 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 21e5941f-850d-33e6-9b86-4a4420d373f3 | -17.12073 | -56.18856 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 161db5ae-d4e2-3918-a2c8-453095e4b436 | -17.12017 | -56.19216 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 08d67b00-7f01-3eb9-87d3-2ca76d725a76 | -17.11962 | -56.19576 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 184c94e7-fbd9-3131-a294-48cfe732f83b | -17.11906 | -56.19937 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cda53c39-3626-391f-81f8-581bdfe93b17 | -17.11742 | -56.188 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 10650151-2b25-3a1a-b223-ea99f5ae9b7b | -17.11686 | -56.19161 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8327ceba-1035-3d28-ad44-2d681613ccc1 | -17.11631 | -56.19521 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a5f0b1cb-0988-3b4a-919f-ee60b8c7c628 | -17.11575 | -56.19882 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4891c513-5677-354b-87d4-3b8cb108a9d0 | -17.11519 | -56.20242 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 58b446b0-38bb-3ec6-ac99-f3876ed8b387 | -17.11411 | -56.18745 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2b4a07fc-22da-34bd-98b4-68f330d60419 | -17.11355 | -56.19106 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6507389d-be43-342d-b9d9-31807ef4409e | -17.113 | -56.19466 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e4b069b4-eb0a-39e5-910e-0ebae8781f5e | -17.11244 | -56.19827 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 402bb844-04cc-3bb1-be59-2866e0cef97c | -17.1108 | -56.18689 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9c77e982-d976-3434-8b55-48afbdc03446 | -17.11024 | -56.1905 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 117440d2-b50c-32a1-838a-db2406e56cbf | -17.10969 | -56.1941 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| da32e42a-a101-362f-9751-f62b8d2b7940 | -17.10913 | -56.19771 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2754d87e-2c50-3964-b6f2-a6f88f39646c | -17.10857 | -56.20131 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b35bb19e-8a49-3b32-8217-61e94f0eded2 | -17.10801 | -56.20492 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 65a3cd7a-370a-387d-8bb2-8fd3701c28c0 | -17.10749 | -56.18634 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 20c2a1b5-8c87-38d7-a280-2685a0023e42 | -17.10693 | -56.18995 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a43b355b-08f7-3575-a070-a76df019a8b0 | -17.10637 | -56.19355 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 82f923bf-8b1f-38f5-a612-601ff09863ce | -17.10582 | -56.19715 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8ff32a03-2123-38ae-9219-7c3853834079 | -17.1047 | -56.20436 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1c08ffdd-ecfd-31cf-b313-74cd682bba65 | -17.10418 | -56.18579 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| de6f58a9-7a7a-3939-9ac3-d3be0ac3c68f | -17.10362 | -56.1894 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 806c6cb9-c2fe-32dc-9c20-51d21ba8247c | -17.10306 | -56.193 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e80337f6-3f7a-3306-b0e9-00786db00495 | -17.10251 | -56.1966 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 71660f4b-5a76-3a52-a363-19cd48a0d9d3 | -17.10031 | -56.18884 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4d1f5101-e354-30b0-b707-ae99a2257225 | -17.09975 | -56.19244 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 87498404-f4a6-3936-a247-58abb1a1804d | -17.0992 | -56.19605 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| ed32acb4-d1cb-3b40-ba95-453dd68b2a86 | -17.09864 | -56.19965 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2d638ea3-5df2-348c-a4cb-c66fa7f2964e | -17.09808 | -56.20325 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| fbcf6bfc-355c-3ef2-ab61-84166c701d24 | -17.09752 | -56.20686 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2302013f-c354-3570-b327-3cd16f23e884 | -17.097 | -56.18829 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b8e5add4-e6c1-3b1c-b903-6a0259f88ed1 | -17.09697 | -56.21046 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 90200eb2-e834-3f9e-81a6-25f9067c87c5 | -17.09644 | -56.19189 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| fe293c61-2bcd-3b1f-9ac0-00cfec8467ab | -17.09589 | -56.1955 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d55357e7-9223-3403-9727-905997ff8a9f | -17.09533 | -56.1991 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7a5872cc-a76c-38cf-8e13-91ebc9bf12a8 | -17.09477 | -56.2027 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1b0f910c-ea12-3aa7-bf29-9075cbf1f0cf | -17.09421 | -56.20631 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b2a9b290-8305-39a0-be6b-53f2dd615490 | -17.09369 | -56.18774 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 23.5 |
| 405cd73a-5dd0-33d7-8a21-c9296f933efb | -17.09366 | -56.20991 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b7b0ecf0-2118-3de0-aa6d-9335a3f32b54 | -17.09313 | -56.19134 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 23.5 |
| c16c7984-3360-3971-8af9-aa4ce6d86f38 | -17.09258 | -56.19494 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 2d9e5c84-fcfc-3db8-83ab-dc97caed2285 | -17.09202 | -56.19854 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 73de18a1-2962-3438-859e-a4960aaffc78 | -17.09146 | -56.20215 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 32bc496c-049f-3296-a72e-623f41e243e6 | -17.0909 | -56.20575 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 66ad7c17-6f10-3975-9d68-dbe7b29b353b | -17.09038 | -56.18718 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 23.5 |
| 7898038e-5ca2-3134-9505-ad5ed1b98289 | -17.08982 | -56.19078 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 23.5 |
| c4e01c5d-d5cf-380a-830d-71847b914e72 | -17.08926 | -56.19439 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| ec12eb84-0b2e-3847-8989-e0394a930b1f | -17.08874 | -56.17581 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.3 |
| b6744dd6-88b3-3f96-8c5b-aa20b0dd4bd6 | -17.08871 | -56.19799 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| c1341cc3-93f2-3c2a-a503-6442f1d1053d | -17.08818 | -56.17942 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 4b7b3681-bfbc-3fde-8102-77502431997e | -17.08815 | -56.2016 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 665ed151-f344-3dd3-96fe-5c98f369b894 | -17.08763 | -56.18302 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 09f6a36a-5593-3ad4-8ac1-0138c878cdf6 | -17.08759 | -56.2052 | 2024-09-26 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |


[Clique aqui para ver as próximas entradas](README148.md)
