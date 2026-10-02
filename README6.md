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
| 5f770320-20cd-3bd6-b7aa-26edc143dffe | -7.5752 | -55.144798 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee35ae75-594e-3025-af18-5ba022d2b5ac | -12.8401 | -51.5075 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 13213716-41fe-3070-bf87-bb5fd741c638 | -10.4177 | -53.785099 | 2026-10-02 00:48:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 633106c1-71ca-356c-89be-deb9215bf5f9 | -12.823 | -51.480801 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d12710d-932c-36a2-992c-5ffeae5209c4 | -7.042 | -55.638 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae682f26-8344-3ff5-8f07-85ae154b914b | -7.2886 | -55.59 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2769219e-9539-3e14-bb7f-5aa5bd0fca82 | -7.7228 | -54.7677 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77ab4346-6ff1-3698-8767-5901fb646761 | -4.3045 | -50.8241 | 2026-10-02 00:48:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffb3e4e6-b7fe-381b-9b25-dee2428c2c34 | -6.667 | -55.0979 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e6ca1a9-a715-3ed9-adfa-a565e93766c5 | -6.8683 | -57.7258 | 2026-10-02 00:48:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f2ec1f4-48b4-339c-9590-1b8559cd8eb8 | -7.4028 | -55.593498 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be2f7861-75f1-3aff-8082-6d4e6d3efb44 | -12.7946 | -51.409599 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f901f9e8-8e80-30ab-81ca-86b8df40a159 | -4.2701 | -50.808701 | 2026-10-02 00:48:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79b2d3dd-39c1-3737-b35f-8389bfb54bb1 | -12.8364 | -51.492901 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cef930e9-8b0a-3e39-8f0f-433a6e2ca9ec | -5.2952 | -55.882599 | 2026-10-02 00:48:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73247c2f-e091-3fa8-ad72-caf5a5a725ef | -11.4852 | -47.507401 | 2026-10-02 00:48:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94704898-6959-36cd-8795-ba1182f68f78 | -7.0593 | -55.623699 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eec21e85-f5e9-37d2-aa6e-aee5487851c4 | -12.814 | -51.404499 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bbc7de0e-fdd9-3056-8697-1f1868906d6f | -4.2743 | -50.783901 | 2026-10-02 00:48:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee3cac87-420a-3b2e-ace8-890b29e9ad6d | -8.1 | -55.3563 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50f2fbe9-7e40-3e35-ac1e-aaac08f13be1 | -6.9151 | -59.283199 | 2026-10-02 00:48:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 633bfcdf-e560-322f-860d-85c889876092 | -6.1728 | -57.7071 | 2026-10-02 00:48:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ee4cc20-0e0e-387c-b6f1-0d31cbd48cc5 | -7.6364 | -55.054501 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb301c2e-1f59-385e-9df1-60c5363273b3 | -6.4961 | -58.530499 | 2026-10-02 00:48:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 01105932-98b2-3f32-b3ad-ac409f9aa842 | -7.4149 | -55.6008 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 650f0488-09eb-3b7c-a81e-3690c49eec44 | -6.9166 | -59.290199 | 2026-10-02 00:48:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82d41eae-ccb2-3803-8880-cd5980834982 | -6.0711 | -57.6236 | 2026-10-02 00:48:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 983b912e-740f-3b9f-a43b-4ff64d0ae013 | -9.5809 | -54.640301 | 2026-10-02 00:48:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97dd3eb3-8f58-3363-98df-503bc05c9fbc | -6.1666 | -57.7248 | 2026-10-02 00:48:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d334dbcc-c05d-369c-b22f-78b9c8dbf638 | -7.281 | -55.602001 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32a60c78-47c2-377e-adb3-c203cc9eeb98 | -7.4172 | -55.610401 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2cec3ce-2475-378f-aca5-00a6b9ae877b | -10.5274 | -57.754799 | 2026-10-02 00:48:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eef73a41-b35f-3d88-95b1-86f590b61e31 | -7.2712 | -55.604301 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7a43d4a-1bae-308e-87b7-4abd244100bc | -4.6893 | -55.758701 | 2026-10-02 00:48:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51d54085-5ab7-3b5f-866f-19c07d983884 | -7.4126 | -55.591202 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 080e1a23-563b-325d-b69b-ef297bceea32 | -11.4661 | -47.512798 | 2026-10-02 00:48:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9bc128fa-7f88-3ba3-91d7-acae81c9ce34 | -7.3872 | -55.221802 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b805fa3-98bb-3a66-a439-8e9fb725d41d | -6.0347 | -57.689602 | 2026-10-02 00:48:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae82310c-d146-3fd1-b5ea-54a8cef87800 | -12.7908 | -51.394798 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4c4557a2-2f62-3861-ac44-572931cf8b2c | -5.8607 | -53.4869 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7b852c4-863a-3a70-8da4-09b84c9fa19a | -10.2507 | -59.035599 | 2026-10-02 00:48:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aff57d75-2cf8-3369-882c-9556d98950c8 | -6.345 | -55.349899 | 2026-10-02 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 089379fd-c365-3119-a94e-a33e865bf9ae | -12.8193 | -51.466099 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7b41b8ec-b37b-3eec-be58-a8fb77e31558 | -6.9264 | -59.287998 | 2026-10-02 00:48:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a8959a2-423a-33c5-9768-a4387f53b704 | -7.0615 | -55.6334 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a451bc3b-f263-35cb-ac6b-7c50d731700c | 1.8037 | -55.6051 | 2026-10-02 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 5442361f-811b-3ddc-82ad-49a1303812e9 | -11.142 | -44.6261 | 2026-10-02 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 18f97a22-b681-35d9-8a73-17d321954b97 | -13.3476 | -43.8776 | 2026-10-02 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 44e5e0f3-9cdf-3a76-8f35-fe848ce15189 | -3.1838 | -54.104 | 2026-10-02 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 5d30b717-cc12-37b8-a4d3-52c7f92d5cde | -11.4695 | -43.4062 | 2026-10-02 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| d490d3b9-bca4-336d-adbe-aa4753d96c9d | 1.7853 | -55.6251 | 2026-10-02 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 0ac2be0f-e9ad-3ca0-8c21-09e1ac336037 | -11.4764 | -47.4645 | 2026-10-02 00:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 2536fb18-39cd-3868-a2d4-0cbff571033d | -7.0477 | -55.6501 | 2026-10-02 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 359eeb04-6444-3bc7-a15b-28b46a83501d | -7.0478 | -55.6302 | 2026-10-02 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 4b293e1e-47f6-34ba-a1d2-0459ecd85a13 | -11.7733 | -43.5719 | 2026-10-02 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 169.8 |
| a3d1ca93-93dc-3073-89f3-79ffe0d2fd8d | -7.1827 | -52.6078 | 2026-10-02 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 9a885d54-97e1-32f7-a192-fc6345969e8e | -4.2676 | -50.7506 | 2026-10-02 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 78b9ebd4-0a39-3960-9acb-55a03d5ae5ee | 1.8221 | -55.5851 | 2026-10-02 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| c5ffb006-4146-3f98-a497-f2b9d99e216b | -7.7405 | -54.8103 | 2026-10-02 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 1019bfba-3dd6-373c-8fdb-55c1d5239a6b | 1.8037 | -55.5854 | 2026-10-02 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| c947d223-adc0-3a6c-b017-388418e4beb2 | -6.0892 | -47.6853 | 2026-10-02 00:50:00 | GOES-19 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 48a83f40-7d3e-3af8-8a95-bfd4db365c80 | -2.0394 | -56.8593 | 2026-10-02 00:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 243e0c80-d083-353c-be8a-4686f909ea98 | -3.0008 | -53.8874 | 2026-10-02 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 001cb42a-b4c9-31b4-b2c7-a7eb5f7fb517 | -11.1424 | -44.6029 | 2026-10-02 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 237.4 |
| 62443a15-dbfb-3368-97ac-7ca9ffa09c30 | -6.8952 | -43.6833 | 2026-10-02 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 46d19d1e-4a98-3c5d-8bdc-fc8ab47c6e21 | -5.8966 | -53.4975 | 2026-10-02 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 08320ce0-684a-3550-94ad-175925cb5497 | -11.7926 | -43.5689 | 2026-10-02 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 178.0 |
| 81feb1e0-0ce4-32be-bd95-f87a9d83ef5d | -10.8154 | -51.0984 | 2026-10-02 00:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 668ce1fa-7c1a-30d4-8b75-8d7628af0ef5 | -11.1615 | -44.6002 | 2026-10-02 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 149.2 |
| eba25dcb-93db-37ee-8be9-79797a37570d | -11.4691 | -43.4299 | 2026-10-02 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.3 |
| ba2652a9-0a64-3276-b87d-229defe9923b | -11.7169 | -43.5098 | 2026-10-02 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 9957e239-096f-3020-93e8-73daab409c1f | -13.3676 | -43.8504 | 2026-10-02 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 508b1ace-ef05-3cc8-97cb-6ef605d33947 | -3.1299 | -53.7633 | 2026-10-02 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 9d9d8223-4583-3293-b3cb-6ae6c4e1ef1c | -4.286 | -50.7707 | 2026-10-02 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 05096a5a-512a-3dcb-b5a2-b55776145bb8 | -3.2767 | -53.84 | 2026-10-02 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 874f6af6-1b7e-3377-b045-323560a3d209 | -3.1299 | -53.7431 | 2026-10-02 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 123e41f7-05db-39c8-908d-a65652f50b3d | -11.7375 | -43.4356 | 2026-10-02 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 824901ab-ed17-3520-92a0-2cd6fd1b0da6 | -6.914 | -43.6816 | 2026-10-02 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| a8deae31-d69d-3fbf-9c47-da54d30d9ddb | -18.6573 | -41.6456 | 2026-10-02 00:50:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.6 |
| 5a8a1607-0a34-3ca4-b9c2-661dbaf70218 | -11.6977 | -43.5128 | 2026-10-02 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| ec5454bd-45e7-34d4-b8b2-7c99dd9951f0 | -4.2953 | -49.1021 | 2026-10-02 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 159.5 |
| aa9815a0-8524-3b35-8c50-0cdfb8182f23 | -7.2704 | -55.5983 | 2026-10-02 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 6e0794ad-3ba2-3f75-bb2a-8db0fe514c31 | -11.7738 | -43.5482 | 2026-10-02 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 4cb7523d-6ca2-30b5-bf24-baf0cde95533 | -2.0577 | -56.8591 | 2026-10-02 00:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 780d7aed-ed5f-3466-8f0c-9c17cc4cd4d6 | -13.1153 | -51.2407 | 2026-10-02 00:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| e038471c-3c9a-360f-85f0-ae3d5f66fd85 | -3.0192 | -53.887 | 2026-10-02 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 8f695c56-e765-387f-bb7c-b75c1c28c5fd | -3.1483 | -53.7628 | 2026-10-02 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 56764b9c-5959-34e8-8e4e-d6d9b02f892c | -2.0393 | -56.8789 | 2026-10-02 00:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 42cb73f0-e3ea-3241-99a3-1397d844e19e | -3.2951 | -53.8395 | 2026-10-02 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 176.8 |
| 2534daf1-6b04-3db9-a252-8e2cca89d284 | -3.1483 | -53.7426 | 2026-10-02 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 5b7941bd-7bfb-3933-a95c-9f7c90970cb2 | -3.0189 | -53.9675 | 2026-10-02 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 27442285-5e2c-3b12-957a-a0e6048d5d44 | -4.2954 | -49.0807 | 2026-10-02 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| b7eeffcc-87d6-36bc-bda1-a1f9e2f7f411 | -7.7219 | -54.8114 | 2026-10-02 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| d0f3f311-759b-398d-a4d8-ff5897f99181 | -7.4031 | -55.2114 | 2026-10-02 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 80da9f30-0a39-3dc1-aa42-0cab65cad55b | -13.3287 | -43.8573 | 2026-10-02 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 157.9 |
| f9a15f92-f054-3909-a99d-6ba7d8cc0a09 | -5.7563 | -45.152 | 2026-10-02 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| dd71bbd0-28bc-3f31-ad16-914db42d57fe | -11.6959 | -43.6077 | 2026-10-02 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 29a4fc0b-0385-32d0-9c0c-22664a78b29a | -3.1839 | -54.0839 | 2026-10-02 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| e0e38d3f-68b5-3023-aa0a-b6e98f2d59f9 | -3.1655 | -54.0844 | 2026-10-02 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 0bf6fd9d-a0d7-3435-bdec-5387a62eeb76 | -3.2766 | -53.8602 | 2026-10-02 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |


[Clique aqui para ver as próximas entradas](README7.md)
