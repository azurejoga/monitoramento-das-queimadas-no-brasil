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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d87449b6-9a96-3fb3-929d-5a0cc629cabc | -9.98089 | -49.48193 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4b13aa5c-e007-3225-93a7-b693bc6b93ce | -9.93654 | -50.0779 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ad2eb9cc-295f-3620-9f15-79141fbe4ff5 | -9.88625 | -50.12987 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9085736f-0fa6-329b-8ef9-766acf6bbf1f | -9.88565 | -50.13355 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 849bc446-0e89-342b-831d-0a8c7e44e754 | -9.88505 | -50.13723 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1cac9f84-9e73-3d8a-ba04-3ed6a6881ea4 | -9.79217 | -50.08399 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdf10c28-eef4-391b-bfda-57b7a2a295cf | -9.78937 | -50.07976 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33aa88c1-f09a-3762-ad36-73b67b6738c7 | -9.78878 | -50.08343 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b698917d-8b24-3321-995a-5071811ee5e1 | -9.77459 | -50.08486 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18344652-b2ce-3c86-ac16-f58567d5ccb1 | -9.77108 | -50.08488 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b32ba9aa-ccb6-3787-ab9e-9cfcd113e199 | -9.76768 | -50.08432 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ecd758e-3175-398d-b2b2-e1dece7decc4 | -9.76709 | -50.08799 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f2ee513-fdf8-39a3-b44a-e44f1207ae56 | -9.7665 | -50.09167 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 000e4ce0-e0f0-3d62-8ece-6d8dbff41d8f | -9.76591 | -50.09534 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec4d894f-7390-3faa-92cb-88d215bf2ba9 | -9.76532 | -50.09901 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b517652-43c9-3da0-8ef2-f188f15b8628 | -9.76473 | -50.10269 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 151992a2-2fc2-3c9f-ac3a-d8b086fda43e | -9.76428 | -50.08376 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d6bb341-3f50-388a-8fe5-1f956f59bf9f | -9.76369 | -50.08743 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba4e8754-eca5-3665-a1be-5e8ebead500f | -9.7631 | -50.09111 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f54cd73d-61b9-36e4-8b5c-69b48cb2747b | -9.76251 | -50.09478 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7d9955d-3740-35db-bafa-77b324c8939d | -9.76192 | -50.09845 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3ce7640-b0b9-36b0-a2b6-0e2ac3dc50a6 | -9.76133 | -50.10213 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f66cdcfd-9860-30fc-b724-da59850ea458 | -9.72998 | -50.12338 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e39a02a-70f0-3916-bff6-6c68a512e9b9 | -9.72658 | -50.12282 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53d07310-2712-350c-abed-b77eb685546c | -9.63158 | -50.10374 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28d84bee-e8bf-3f23-bec6-c55136d9ddc8 | -9.63099 | -50.10742 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 744508b9-3189-37e0-b92a-0284499ad736 | -9.63039 | -50.1111 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a75d6f75-d867-3876-b4f2-05a7bb62f912 | -9.62758 | -50.10685 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3cc1f46-2744-3d73-9ed8-f5bd2973523a | -9.62699 | -50.11054 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4438c72d-af15-32e8-98e8-54709839d77a | -9.60377 | -50.10293 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 411b943d-70f2-3868-814c-cd02c8483770 | -9.60036 | -50.10237 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd58c43b-7d61-3626-82c1-2a0422eea18a | -9.59535 | -50.09021 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67d0714c-1ed0-3f54-8c10-f7e9b64ba9ef | -9.59475 | -50.09389 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1d92d27-bb48-3160-a5b6-e0f6a6de3458 | -9.59416 | -50.09757 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a52fcfa0-9502-3d4c-869b-689499014a86 | -9.58574 | -50.08485 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5a9762f-dec8-374a-9eec-9ad4384c1cb0 | -9.58414 | -50.07327 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b361bc24-5e6e-3280-817a-4a2984ab4cac | -9.54559 | -50.07502 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4f7ab66-09ae-3f30-8f08-3ea0416f8df6 | -9.59922 | -50.17413 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b8c7804-c3f2-372f-9fab-69bb65b3abb7 | -9.59863 | -50.17783 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8424e85a-687d-372b-9712-aea6b284118c | -9.59641 | -50.16988 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dee0d85d-7633-3ac3-9820-f38020e4260c | -9.59581 | -50.17357 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5351b37-26d1-3f7b-a9dd-b2a0d5c21507 | -9.59522 | -50.17727 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db594fea-c90c-3566-9baf-98e6dc15554e | -9.59461 | -50.18096 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0d39733d-c155-38af-9a74-6d8fd8c41115 | -9.5936 | -50.16562 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ce50568-4965-33f6-887a-fa85fe08e5ee | -9.593 | -50.16931 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0cdae23-032c-30fa-a90a-f673d9404602 | -9.5924 | -50.173 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 002c1eb3-1c2c-333e-b6cc-8530dc35adfe | -9.59181 | -50.1767 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09be6ce2-10c2-39c2-8dc8-3b4e114002ed | -9.59121 | -50.1804 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b68e2cbf-64c2-37d6-899b-019c7e4280cf | -9.59079 | -50.16136 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ab5bd6d-1a4d-39bc-a190-9a31081d3868 | -9.59061 | -50.18409 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b487834f-c18e-3587-9408-e845edece86d | -9.59019 | -50.16505 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8dd757c5-ce2f-3070-94dd-e64c3a7b0e4e | -9.58959 | -50.16875 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cbad355-db3c-395e-9390-e1dd8430fa4d | -9.589 | -50.17244 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 845fdb43-5ec4-31c0-b586-3905dd51d569 | -9.5884 | -50.17613 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd376105-bbff-380a-b775-9542811d5afa | -9.5878 | -50.17983 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4517b4c8-e1a1-32b1-9ffa-2077944fd3c3 | -9.5872 | -50.18353 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6011134c-2a0f-3f7f-8d7d-934b883909d6 | -9.587 | -50.2063 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb2cb720-aef3-3511-9245-59f6e697d172 | -9.58679 | -50.16449 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8de07560-8871-3641-88a7-1adec208b2f1 | -9.5864 | -50.21 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 453d9723-3cf4-375c-b7bd-e88b3ae9369d | -9.58619 | -50.16818 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ff7f9d0-075d-3b3b-a161-0d422363e991 | -9.58559 | -50.17188 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 273a0b25-413c-318a-a9b5-92630430f221 | -9.58378 | -50.18297 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0dddb8d1-cb61-30f7-930c-27217470603c | -9.58299 | -50.20944 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9b5fdff-8681-37cd-a5d7-e1d0b69e22e8 | -9.58158 | -50.17501 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88b38e78-2403-3195-936b-a9a46d4e026d | -9.58037 | -50.1824 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85f191e0-99eb-3529-a9b7-dd04a7930244 | -9.57977 | -50.1861 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8228eb1f-93ec-3490-8f61-7fe8a3a2a24e | -9.57837 | -50.21629 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 317b07c7-166c-335b-b813-88c9a63ffc4b | -9.57817 | -50.17445 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 824a105c-46e1-31a6-a602-e9790216506b | -9.57777 | -50.22 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 170fe811-f106-34df-bad4-7a0db67ed1e0 | -9.57756 | -50.17815 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90116479-b845-3f53-b460-b4d299cba3b5 | -9.57716 | -50.2237 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a13ce50-e48a-34a3-9e56-5680e980f1ba | -9.57636 | -50.18554 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b6aa8da-cf37-3094-aba5-e2275126be93 | -9.57475 | -50.17389 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b0e8b32-fff8-3c41-9d75-61b287e3809d | -9.57375 | -50.22314 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ada3633-f89b-3e3a-9128-a40fc97125b7 | -9.57314 | -50.22684 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60d70faf-efa5-30c1-9879-00be5f403bf6 | -9.57033 | -50.22258 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0123ff9b-0a52-360b-8333-cb75c638bbe9 | -9.56973 | -50.22628 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ec11d7ed-991f-3902-99e3-ed0350f93933 | -9.56954 | -50.18442 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a5e39f6-8f59-314b-9349-73048292874b | -9.56912 | -50.22999 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3f820640-08e7-346e-8632-4add992c30e9 | -9.56812 | -50.2146 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9893b3f4-e354-323e-8aa9-9c374616cc16 | -9.56692 | -50.22202 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 96d35216-5010-31e2-95fc-f774606e440e | -9.56631 | -50.22572 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a2a843fb-e993-392b-9795-874adcfbab6e | -9.56471 | -50.21404 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d8b0e3e-32ab-3442-ac77-8a85577ec052 | -9.56411 | -50.21775 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 347e072f-b6fd-381d-b1b9-25cabc5c97fa | -9.5635 | -50.22145 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8cd1c3b2-5dd7-3c87-8e92-d56ded456585 | -9.5619 | -50.20977 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db6c9ccc-3724-395b-b174-871c7745a6b0 | -9.56129 | -50.21348 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ececb2f8-847b-3377-a730-c1087c4cc809 | -9.56069 | -50.21719 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15b69312-86ab-3d16-95f3-80b9e0d340cc | -9.56008 | -50.22089 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf5f37e8-22b9-3657-a9a2-19dac8cdd62c | -9.5597 | -50.2018 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fa00bd6-836b-36e6-bd64-5670779ffe15 | -9.55909 | -50.2055 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 472d2536-b70b-3c80-845a-54cc7f85472c | -9.55849 | -50.20921 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fc1ee97-1edf-350a-a189-9e210aa4793a | -9.55788 | -50.21291 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9aee7f0-6e3b-3a1e-aea1-48798bf453c8 | -9.55727 | -50.21662 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44796104-cc24-3731-8260-ced61fb67ec8 | -9.55667 | -50.22033 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b20db5b-af6e-3f0a-962a-b39739a2e9f6 | -9.55628 | -50.20123 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d978a012-db15-340d-9a37-c3e06d3145d8 | -9.55386 | -50.21606 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c12b4444-6867-3add-a07d-2cc7994e5878 | -9.55325 | -50.21976 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dad7ff36-57d4-3fdb-9252-e5c9fbbeffb4 | -9.54362 | -50.21437 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 692a7fb3-a733-3289-953e-22b67f57ad5a | -9.54081 | -50.21009 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README106.md)
