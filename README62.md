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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3b19f8b-1d07-3df8-9094-6643c30882ec | -1.28705 | -55.71564 | 2024-10-26 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51870d08-9cdb-3452-8926-8150b4490410 | -1.28642 | -55.71965 | 2024-10-26 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb536620-0362-3783-9a68-60a9e3317bb0 | -1.2858 | -55.72365 | 2024-10-26 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c50f60a3-3481-3216-a4d5-721293c0b1b3 | -1.21927 | -55.89461 | 2024-10-26 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 098844c8-9366-3f73-8998-9ad07f21330f | -1.21497 | -55.8939 | 2024-10-26 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13718449-ccaf-30a4-863a-dc36faab5bb0 | -2.42987 | -55.64062 | 2024-10-26 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7bd28e13-f317-3c52-b3ab-e38ba11cb06d | -2.36702 | -55.28433 | 2024-10-26 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f9c150f-7a85-38da-9784-6b85714b72df | -2.10965 | -56.67075 | 2024-10-26 04:42:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dc3f1f1-b89b-3bd8-bf28-81852ee0e62c | -2.10519 | -56.66989 | 2024-10-26 04:42:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53612f56-d6a9-3042-96ac-1b2d6c841590 | -2.53774 | -56.75528 | 2024-10-26 04:42:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad5a389b-b0f0-3014-b18f-8af8a0476f5f | 0.62949 | -60.24919 | 2024-10-26 04:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d47442e-e5a6-39f4-bc47-af7a93f5f44e | -2.77478 | -54.72791 | 2024-10-26 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c77edf4-b87c-3269-aa26-482518632b57 | -2.77433 | -54.73396 | 2024-10-26 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| edcd476e-84c1-3b31-8c64-2152150b4c1d | -2.77201 | -54.72375 | 2024-10-26 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0803b6b3-ab44-3024-a285-d30cc71610c2 | -2.77164 | -54.72251 | 2024-10-26 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49d7ff9b-3ec3-3f53-8809-c0b71410f738 | -2.77088 | -54.72731 | 2024-10-26 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14348a57-72ec-3c75-9ba5-8d8df1273578 | -2.75941 | -54.03489 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec5c8746-8466-3009-8dc0-763b4301c084 | -2.68013 | -54.02738 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bd48ac10-e9d5-3ab8-a772-a8100d5e3d4e | -2.67638 | -54.02683 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6aa58048-db1c-3d10-a29d-3e3de37471d9 | -2.6411 | -54.33987 | 2024-10-26 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8d63cf9-3e52-3dcd-af23-04a862057d88 | -2.5689 | -54.0204 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 13296744-b760-3bfd-8171-40602811bc50 | -2.56589 | -54.0153 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 587287bf-341a-354f-a87b-4d329a142d55 | -2.56516 | -54.0198 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9f8c33da-ff43-30e4-b81e-b42bbc04d8a6 | -2.56141 | -54.0192 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c41c75c2-2288-3ab6-a591-d871a8257a52 | -2.56072 | -54.01613 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a4600f7-5e60-3624-a0c7-2c237eb6bd7e | -2.83752 | -53.98618 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fe5e96c-6883-3c52-95bf-36ebe6407b84 | -2.81619 | -54.0239 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51919046-b742-3c14-a1c7-63f7db3c2b8b | -2.80788 | -54.00425 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f66d543-5696-373d-9993-98cbacc92075 | -2.80416 | -54.00366 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52a9af46-6659-3e90-947a-f2f5b05b97d5 | -2.8032 | -54.10473 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ea49f09d-c1ad-3113-bf46-c5bdcaedc1c8 | -2.80043 | -54.00306 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 191d17f1-c431-38dd-9a9b-ddf09287b836 | -2.79945 | -54.10413 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 314edc5a-33ba-33cf-b36d-0a2c24e48362 | -2.79872 | -54.10865 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bffcf170-f4ef-35f5-af6c-391c6e3c2656 | -2.79424 | -54.11257 | 2024-10-26 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a19449dd-f775-36e9-9fd0-f4858025a5a8 | -2.78935 | -54.02419 | 2024-10-26 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4ae01f5-4eaa-3266-b223-307c66755666 | -2.77822 | -54.73461 | 2024-10-26 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7d90a10d-dfa5-3c3a-9738-36a8a7b7ff9e | -2.7759 | -54.72437 | 2024-10-26 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e80b2eb-1f74-3f45-b585-8fdc72b19dd9 | -2.77553 | -54.72313 | 2024-10-26 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b58d61cb-af18-3e90-92a5-c34a3922f5b9 | -5.14654 | -37.74184 | 2024-10-26 04:42:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 5f61c061-e5bc-3101-bd8a-7b54cc0dfb00 | -5.05644 | -40.88829 | 2024-10-26 04:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 83ed3688-4cde-3a1a-af5b-6a9b01be0d7d | -5.0559 | -40.89207 | 2024-10-26 04:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c0a8cf2a-3235-3e8f-aa05-c8f13499edfa | -5.05085 | -40.8874 | 2024-10-26 04:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3c425166-267b-39ba-9098-ddcc5ed5d6ef | -5.05031 | -40.89116 | 2024-10-26 04:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9dd073ce-fc55-3a52-8d32-03df9d4ab6d5 | -3.89616 | -41.04044 | 2024-10-26 04:42:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ffe4d04f-f25f-380f-9cf7-c38ddf4fa94d | -3.89303 | -41.03336 | 2024-10-26 04:42:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 7758b1a9-fe4e-345a-8577-290acdeb8c2d | -3.89254 | -41.03686 | 2024-10-26 04:42:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 1946928b-4fb0-32fa-b5e3-0002d79602c0 | -3.89204 | -41.04032 | 2024-10-26 04:42:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| e0251478-7167-34c4-8e58-d7ed1623ab0a | -3.89176 | -41.03258 | 2024-10-26 04:42:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 20.0 |
| e0e93727-b518-353a-96e1-fefcfd6e2c0a | -3.89124 | -41.03607 | 2024-10-26 04:42:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| e43ec812-a4e2-36fa-9bca-4c8e6b0e3be2 | -3.89072 | -41.03954 | 2024-10-26 04:42:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| aa64b812-442c-3a02-a8e6-eb2f20d2eabc | -2.94304 | -42.71701 | 2024-10-26 04:42:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c5ebec3f-b75d-3080-ab66-29ec5e4f1bca | -2.94226 | -42.72224 | 2024-10-26 04:42:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ee729bb1-c880-383c-9698-b83fac800bdb | -4.92084 | -41.97668 | 2024-10-26 04:42:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fb10403b-3b0b-3fc4-8b89-1d8a7a6b79c2 | -4.92039 | -41.9798 | 2024-10-26 04:42:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 01aaf20d-2b02-3d73-8b7a-df1e6a704c4d | -4.48131 | -42.90342 | 2024-10-26 04:42:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a61ab4aa-41f5-35b6-a564-0f6843b57c62 | -3.47457 | -43.32784 | 2024-10-26 04:42:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| ea84fde6-af46-3a9a-9660-6de14079d53c | -3.47386 | -43.33266 | 2024-10-26 04:42:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 9b59f5a3-40e1-3799-b472-8c55ccbc634b | -3.46924 | -43.33192 | 2024-10-26 04:42:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 028b05df-9417-3c95-9897-15953035ce89 | -3.48453 | -43.32447 | 2024-10-26 04:42:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a94aa816-2e30-3ffc-a934-7955d38e1984 | -3.48382 | -43.32925 | 2024-10-26 04:42:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2f22205c-366b-372c-ac04-03a0f48d0e24 | -3.47848 | -43.33339 | 2024-10-26 04:42:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 9776890f-3553-346f-ae17-acacb094924b | -3.47065 | -43.32232 | 2024-10-26 04:42:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 169ead03-838a-3b53-b143-d655bb6c65ec | -3.46994 | -43.32711 | 2024-10-26 04:42:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| e4a04d02-b4d1-34e0-97df-35883bedff1d | -3.47919 | -43.32856 | 2024-10-26 04:42:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 9709dd77-0906-3b4e-b98f-edf6ae807b48 | -3.4799 | -43.32377 | 2024-10-26 04:42:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| fbaa41f5-f6ec-3a06-9580-d618bd646f54 | -3.47527 | -43.32305 | 2024-10-26 04:42:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 0daa4bb9-2ea4-353b-8507-5859cc5c8b8f | -4.7428 | -43.24987 | 2024-10-26 04:42:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b0950fb-1056-35d5-899b-a3633c927d43 | -4.74203 | -43.25501 | 2024-10-26 04:42:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9431255f-033b-34b2-9a52-a93afa1f25de | -4.39783 | -44.26113 | 2024-10-26 04:42:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6c9e6e1-ad1e-3363-848a-266264b86ffd | -4.22567 | -44.53563 | 2024-10-26 04:42:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e29c6a8b-b8cd-3220-9760-bc8ea2e3b9a6 | -4.22136 | -44.53502 | 2024-10-26 04:42:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 25e8744f-924f-33a1-b824-865d7ed3fe2d | -4.20207 | -44.24656 | 2024-10-26 04:42:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 916335cd-817f-3f4e-88f6-1b2807d8cf63 | -4.19768 | -44.24593 | 2024-10-26 04:42:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7dc9d811-c2b3-356b-a589-55932aaf78ac | -4.19706 | -44.25014 | 2024-10-26 04:42:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7768d62a-0e7b-3474-acaa-73a1e5346777 | -4.19328 | -44.24531 | 2024-10-26 04:42:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b9c93f2-20dc-3191-9155-83b2fd78a450 | -3.45899 | -45.98524 | 2024-10-26 04:42:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc431438-26f4-3119-971c-1d1ecb6dca33 | -3.28824 | -45.7392 | 2024-10-26 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f29ae1f2-6c6d-325c-acd3-6943a5a8e95f | -3.28432 | -45.73863 | 2024-10-26 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 12622b6a-55e2-3b84-8a48-45a97ce2b500 | -3.24554 | -45.80875 | 2024-10-26 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7db9b72f-fb37-3f13-afa1-7caf8e0b38c8 | -3.24164 | -45.80814 | 2024-10-26 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c90253d0-b616-32d1-bed4-9a607e222e21 | -3.24089 | -45.81304 | 2024-10-26 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b486d256-1bbc-3dd0-ab5a-2245fca278a4 | -3.23068 | -45.56038 | 2024-10-26 04:42:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cf63b82-7d5e-3a15-b305-b2a4ca12ae17 | -3.22954 | -45.14766 | 2024-10-26 04:42:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c9dd70c8-d0bf-3cd2-b435-efe62569e50b | -3.22844 | -45.15488 | 2024-10-26 04:42:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 744e97f7-a52a-3db7-9af3-d1081d4e1405 | -3.60619 | -44.97097 | 2024-10-26 04:42:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 987ad37a-418b-3530-91c8-427ecfaebdf4 | -3.60204 | -44.97038 | 2024-10-26 04:42:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 623a6b35-28cd-39e1-b37c-a9c7727c8c28 | -3.61354 | -44.78168 | 2024-10-26 04:42:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0aee878f-7da1-3d55-ac8b-f706c8b016da | -3.60935 | -44.78104 | 2024-10-26 04:42:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1968118d-7f42-3855-a7ac-6d30c6ebc868 | -3.45974 | -45.9804 | 2024-10-26 04:42:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 39917594-a4eb-3c3c-b49f-bba6e1931448 | -3.28901 | -45.73422 | 2024-10-26 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9d39cea8-a7d2-322e-94ad-2a03c6f35a34 | -3.28509 | -45.73363 | 2024-10-26 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 70cc83a1-40e7-35aa-848f-8c4f0a075ff9 | -3.24479 | -45.81364 | 2024-10-26 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 630cea7e-facf-32ab-bddb-b72fa5f59635 | -3.22899 | -45.15127 | 2024-10-26 04:42:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a3e7e50a-b777-3f30-a0fe-2adb23abc4b2 | -3.22547 | -45.14703 | 2024-10-26 04:42:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 4436bd3a-ffd7-3c7e-9d81-620af572fe2c | -3.22492 | -45.15063 | 2024-10-26 04:42:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 24.6 |
| ac5d3c83-1231-3713-88a3-b09d73792d5a | -3.22438 | -45.15422 | 2024-10-26 04:42:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| a43a8d37-befa-344f-bc7d-12d17e951ce8 | -3.9084 | -44.77515 | 2024-10-26 04:42:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41e12d59-4ea0-3006-9053-1c71e41df8c1 | -3.60248 | -45.80816 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ec551807-bd2b-3712-aa7f-c8df3c9ab2e3 | -3.60171 | -45.81314 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 55b41ae3-56c5-3338-b122-c8af52021358 | -3.60094 | -45.81813 | 2024-10-26 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.6 |


[Clique aqui para ver as próximas entradas](README63.md)
