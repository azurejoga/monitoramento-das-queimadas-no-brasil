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
| d3764605-6ccd-3ac7-8a65-9d83e856b77e | -11.06316 | -52.50867 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7c503dd-18ee-3fab-a14c-5041c84ca27b | -11.06246 | -52.49008 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fac3881e-c1ee-396d-b887-027dffec2661 | -11.06241 | -52.51315 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7286255c-5931-3138-b0ae-70904149ed1a | -11.06165 | -52.51765 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08690eff-eace-3577-8f37-c87f022ebdcb | -11.06096 | -52.49908 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a140527-b2c0-3f1a-8304-b429c0835bcd | -11.05945 | -52.50805 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efd46b07-6232-3433-b4b6-a37aa51e08e4 | -11.0587 | -52.51254 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d72a420-0786-37c1-957e-5e07b642a052 | -11.05801 | -52.49392 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8ebf002-b4fc-3aa1-9af0-8201bbaba97c | -11.05432 | -52.49327 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6aaaec9b-a924-3ac3-b0fb-af26c3243713 | -11.05137 | -52.48816 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cad3ce61-e70a-35e0-9eb7-6d7f832681e3 | -11.05062 | -52.49265 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79d79fbd-44fa-3cc6-8a6b-aa2c34384939 | -11.04767 | -52.48755 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2a72205-40d4-3b73-8c40-668445023871 | -11.04691 | -52.49203 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1410353-29ab-3902-b3da-982f133a9e5e | -11.07654 | -52.4514 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24122200-c3a7-3606-b18c-1e21da296556 | -11.0758 | -52.45584 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f069a14d-f9dc-34a9-a9bc-b24fab857204 | -11.0736 | -52.44633 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dab6c929-0868-3a59-9ce5-ea201706dd20 | -11.07286 | -52.45075 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a44b4ff8-b8a9-3904-9eb8-e974947fab47 | -11.07212 | -52.45516 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51f14baa-81e2-3485-80f6-94dbfd825c5a | -11.07065 | -52.44127 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c128a8d8-321b-3d4d-a7f9-fa5a7f211c8a | -11.06991 | -52.44569 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45197f4c-ca84-3a0c-9882-cea381db1043 | -11.06917 | -52.45009 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b739fa4e-acb9-3f55-b9c7-7d4d434d5bee | -11.06843 | -52.45449 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 591742f5-92bb-3c80-8f6f-c0bcb33fcd48 | -11.06697 | -52.44061 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| baf4dc3d-22fe-3b79-b508-13963bb1d91b | -11.06623 | -52.44501 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21375e87-d105-3387-be9a-6e762919d76d | -11.06549 | -52.44942 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcb05dd8-69ac-38a2-9e86-a6721a59309d | -11.06475 | -52.45382 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 496bb29e-65e5-34a7-aea3-c74509ce26f7 | -11.06401 | -52.45824 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| a7d2e810-c14c-39ad-8397-8972f171e6af | -11.06328 | -52.43995 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb944ddf-7dea-3c38-a584-c14cf8e35717 | -11.06254 | -52.44435 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61916a76-43f5-37ba-8c02-399e88b7248f | -11.0618 | -52.44876 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0c40af4-6820-300d-9a6f-9a75eaa27840 | -11.06106 | -52.45317 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 807a8d9c-bf27-326a-807c-525225ada45c | -11.06032 | -52.4576 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| fa926a2b-3731-35c0-9dcf-390a87a4457a | -11.05959 | -52.4393 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7416e23f-80b9-372d-ac87-4e750b4d2cee | -11.05885 | -52.44371 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f23679b5-b5f1-37b4-a26f-aa24b1f5d97d | -11.05811 | -52.44813 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a7caf68-6ead-3e8e-ae25-89d5db296613 | -11.05736 | -52.45257 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 830c080f-822c-38d0-ba29-3f680426027e | -11.05662 | -52.45699 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ed9176f3-3885-34da-b117-a70c6fb11626 | -11.05516 | -52.44307 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ff90d98-6f29-3788-bee8-b22650d946c2 | -11.05442 | -52.4475 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f778c747-1683-3c9c-a8a5-c2a8994e417b | -11.05367 | -52.45196 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9a23aa08-a28d-3004-808f-6f11c50ecf6e | -11.05292 | -52.45638 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 819821b1-b32c-3a2c-ac85-fa5077b34cf0 | -11.05072 | -52.44688 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90afb28a-6acb-3046-a9e9-70bd206282fe | -11.04997 | -52.45134 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84f6fbff-11b7-3c0b-9c2d-c141404221c8 | -11.04922 | -52.45576 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd053b2e-cbac-3dc6-8a20-c686cd4ccd4b | -11.04553 | -52.45515 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdd867df-a669-3aa1-bc8a-28e0a17f57ed | -11.07874 | -52.48377 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5305f8c-ab5e-352d-b84a-929c2e9ebecb | -11.07579 | -52.47866 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69292c96-7f17-3354-a7c0-befd8090daed | -11.07506 | -52.46026 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e73f4308-50cb-38dd-8b16-5cba229cfb00 | -11.07505 | -52.4831 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30c9953a-3845-3c1f-8cdd-d3737db95b07 | -11.07432 | -52.46469 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69c8b7e3-9e02-38d9-a12e-99610308abaa | -11.07358 | -52.46913 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 134c6fba-2e8d-3c7d-b5ec-c0b0c28901d6 | -11.07284 | -52.47355 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44b58117-1f9b-3215-b4a7-09cb62ad57a8 | -11.0721 | -52.47798 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6391a572-fd34-3220-9317-dac57b2ad966 | -11.07138 | -52.45958 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56ba4ba0-fc6d-3197-b003-7f18e9141590 | -11.07136 | -52.48243 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57c19312-3a2b-3893-ae7d-e5dbc7ca9c8f | -11.07064 | -52.464 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb551f49-232c-34de-a7df-972b9fed9e8d | -11.06989 | -52.46844 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b280a25c-862f-389e-9ff3-d136bfc7ff71 | -11.06915 | -52.47288 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8133c311-09c6-3f3c-baf4-bbaf6c3c4840 | -11.06841 | -52.47731 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09f99e16-146f-34d4-b36a-cf877b1f0a4f | -11.06769 | -52.45891 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ceaa131-a7eb-3e93-8ff7-aa4869f3e972 | -11.06766 | -52.48177 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d8c4e629-2cec-3a80-ab8d-340cb40bf414 | -11.06695 | -52.46333 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a331305-d1dd-3a42-985e-9ce1bb08f263 | -11.06691 | -52.48624 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9bbb4442-f05b-347e-bea7-dc60b4917219 | -11.06621 | -52.46777 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a58b205c-671a-39d9-ae95-2d1e559f7d4f | -11.06546 | -52.47221 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 428b23ef-6d56-3f76-be0b-8fab917ccaf9 | -11.06472 | -52.47665 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48efe463-9b11-3e78-8d3f-2b81a4e92d25 | -11.06397 | -52.48111 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b8c41742-7723-3ce6-839a-e874940c8228 | -11.06326 | -52.46267 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ffd24d2e-2f17-3ade-b9e9-875958788b7a | -11.06322 | -52.48558 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09d6d06c-cf0f-3887-b08a-e696101f0535 | -11.06252 | -52.46711 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1d60d8c4-df98-31f2-844b-8f6bffedd871 | -11.06177 | -52.47155 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20b4c2b1-2f08-3107-b448-48396d04bc20 | -11.06102 | -52.476 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d79b4e5c-ee74-3a64-9218-8e33c17b9560 | -11.06027 | -52.48046 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5751eecd-a033-3d93-8a93-1aeb0c9b14d3 | -11.05957 | -52.46202 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2bf96e6d-2ad2-3aee-9acf-d27eb61de5c7 | -11.05952 | -52.48494 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d40af279-f686-3677-9e47-a74c679237a5 | -11.05882 | -52.46646 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0aab849d-02d2-3f37-bd94-c26b55a51556 | -11.05808 | -52.4709 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46e62d8c-3af9-34e0-a9c7-9baef7e0bc9a | -11.05733 | -52.47536 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3cf51ca-93c1-36d7-a547-d6e236eeb717 | -11.05658 | -52.47982 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b29fa5f-e5a1-3aa3-b88e-b4e23ee9abf1 | -11.05588 | -52.46138 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50531508-6198-3052-bf65-c821d100bceb | -11.05583 | -52.48429 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 601d36c4-b0af-3648-954a-5fc88d024ac3 | -11.05513 | -52.46582 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 326aace7-e77b-31db-b61e-441e663d2c25 | -11.05438 | -52.47027 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49e9dd43-913e-3278-9939-9b679da9cf57 | -11.05363 | -52.47472 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1548a6ed-0475-3e03-9c4f-26e9969d505b | -11.05288 | -52.47919 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 932cf2a0-43c1-31cb-8442-fe60367f3fe9 | -11.05218 | -52.46076 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 44f6149e-cfe5-3323-8cdd-69b3eacaea50 | -11.05144 | -52.46519 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a7876e56-97f8-3d4d-9636-521589879091 | -11.05068 | -52.46965 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d2ca2eb-3a41-39d9-9210-7d412dca2e82 | -11.04993 | -52.47412 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc572024-5115-3e12-a335-a290d0f603c4 | -11.04918 | -52.47859 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 257c5d95-4055-3b65-aa4d-2b668e5bada1 | -11.04849 | -52.46014 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4c7a1bf-24e7-3a84-bfb6-1d29d472e27b | -11.04842 | -52.48307 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8f48c08-f742-383a-b75e-5e10ea0c15fc | -11.04774 | -52.46456 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79143bee-f800-333a-95f0-9c8f84bd7c1d | -11.04699 | -52.46903 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1ae6bdc-4caa-3569-8869-86f1cf1c3eef | -11.04623 | -52.47351 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b57fed7-4e38-3978-bc1a-c72f440fd030 | -11.04548 | -52.47799 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 891d3810-792d-320b-a12d-9e5c2d777f42 | -11.04479 | -52.45953 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 109982fb-79a2-3912-abbd-86f49bdf8830 | -11.04472 | -52.48247 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e238037-c480-3823-be36-0b9f1783f1a0 | -11.04404 | -52.46395 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a63ef99-bbe1-31a7-8615-28e9b48c4f4c | -11.04329 | -52.46842 | 2024-09-30 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README47.md)
