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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 162e694e-3a40-3922-b4e7-266811bc7283 | -3.0566 | -59.9105 | 2025-08-06 08:40:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 4745c713-ec05-37e8-a6fb-a7a61fd3b110 | -8.9039 | -60.5769 | 2025-08-06 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| cac26b02-ac3a-3507-b95e-8b5777126538 | -8.9041 | -60.5577 | 2025-08-06 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 83d8f953-7c76-37a0-bf51-135e7a4e770d | -3.0566 | -59.9105 | 2025-08-06 08:50:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| bb554a88-ee04-3c90-8309-ccc58e7920be | -3.0384 | -59.9108 | 2025-08-06 08:50:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 7f660ea4-019b-3e39-b982-cdb590fa2128 | -8.9041 | -60.5577 | 2025-08-06 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 471fc3dd-bc93-3f64-b4ef-110b77e6f84e | -8.9225 | -60.576 | 2025-08-06 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 06a8ce5f-9439-301d-9bf3-6a321d24b46f | -3.0384 | -59.9108 | 2025-08-06 09:00:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 215d50e8-3d1e-3062-8e51-bb68b7b25810 | -8.9224 | -60.5953 | 2025-08-06 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 253ecda0-48f5-325e-97dc-ed27a1acf232 | -8.9039 | -60.5769 | 2025-08-06 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 0c949124-c3e9-32e1-9d90-b36492a4c312 | -8.9227 | -60.5568 | 2025-08-06 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 54b4ce83-82ee-3117-9fbd-a0523db88f88 | -3.0566 | -59.9105 | 2025-08-06 09:00:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 092326fa-12cc-30bd-828d-8182643eef85 | -8.9038 | -60.5962 | 2025-08-06 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 51a19b1e-cba9-3488-b700-cf6f9c2f2b8e | -3.0566 | -59.9105 | 2025-08-06 09:10:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 12a1368a-7975-340a-876f-34feeb7fa132 | -3.0384 | -59.9108 | 2025-08-06 09:10:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| fc57fc6a-60a7-3ad1-9711-5e501fb30c96 | -3.0566 | -59.9105 | 2025-08-06 09:20:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| fe15cc58-eae6-3ae1-9374-7c39290c7033 | -8.9038 | -60.5962 | 2025-08-06 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| b7456be3-7ace-3448-af98-63219d0f311b | -3.0384 | -59.9108 | 2025-08-06 09:20:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 476cb7e8-f1f4-3ed2-bd4b-d9b7da7dc988 | -8.9224 | -60.5953 | 2025-08-06 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| a25ce06d-09c6-33e7-b76e-7730f3395d99 | -8.9041 | -60.5577 | 2025-08-06 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 9c43fa2c-da8e-3ebf-9b80-7cd48b064c19 | -8.9039 | -60.5769 | 2025-08-06 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 61e6241f-2849-3b8f-9702-b31477d363c0 | -3.0384 | -59.9108 | 2025-08-06 10:20:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| bb43ecb5-1e8a-3fda-8eda-2b31d3abb4b3 | -8.9038 | -60.5962 | 2025-08-06 10:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 37bcd67c-59e2-331c-8311-a5e8364a02c0 | -8.9041 | -60.5577 | 2025-08-06 10:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 154.2 |
| a3457d62-9703-3736-8e67-e0e943cd0baa | -8.9225 | -60.576 | 2025-08-06 10:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| e29c8e4b-9fe4-37fb-b610-47532fc46828 | -8.9227 | -60.5568 | 2025-08-06 10:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 20826de3-ba19-3481-b286-4a67ea3967aa | -8.9039 | -60.5769 | 2025-08-06 10:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 173ae7ff-d5d9-376e-90c8-0d8c39598846 | -8.9224 | -60.5953 | 2025-08-06 10:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| bd4c174f-7748-3dc3-8a41-1c8abb97a3d9 | -8.9041 | -60.5577 | 2025-08-06 10:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 165.6 |
| 006ca545-48fe-3a51-8708-563b506977ca | -8.9039 | -60.5769 | 2025-08-06 10:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 49267744-4cfb-3123-afe7-010fc29d975b | -8.9227 | -60.5568 | 2025-08-06 10:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 994b10cf-f7e9-37a1-b67a-c0f5b37a8b01 | -8.9038 | -60.5962 | 2025-08-06 10:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| b3e1cba5-07ee-3f04-a055-1ebc8f0c3c86 | -3.0384 | -59.9108 | 2025-08-06 10:30:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 02a222cd-ae4c-3c92-9570-df82dd78d133 | -8.9039 | -60.5769 | 2025-08-06 10:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 129.1 |
| a6c0cf89-d912-35ca-aca1-1ed189bf47cf | -8.9041 | -60.5577 | 2025-08-06 10:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 160.0 |
| afbfacae-a455-303e-a295-495eba41ee3e | -8.9042 | -60.5385 | 2025-08-06 10:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| cd8f11f7-1ef2-30d9-a5e3-11d1280720bf | -8.9038 | -60.5962 | 2025-08-06 10:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| cbd34c79-5d51-321b-96db-824cd738d006 | -3.0384 | -59.9108 | 2025-08-06 10:40:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 79873915-20d3-3eaf-861e-899bc2afe88d | -8.9039 | -60.5769 | 2025-08-06 10:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 2e6a74e1-7c33-389e-9ab8-f65979ff564c | -8.9225 | -60.576 | 2025-08-06 10:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 5bceb28c-379b-3998-bde5-0f13909cbdc3 | -8.9041 | -60.5577 | 2025-08-06 10:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 7f0c8bd4-e798-37ed-856b-8e16716f3613 | -8.9227 | -60.5568 | 2025-08-06 10:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 6cde66a5-a692-35dc-959f-73fa7b5779c3 | -8.9038 | -60.5962 | 2025-08-06 10:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 4bf978b0-d77f-3166-8265-13707d2a94f2 | -3.0566 | -59.9105 | 2025-08-06 10:50:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 2175feed-405e-363e-bb97-cb8b3e321e36 | -8.9224 | -60.5953 | 2025-08-06 10:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| cb84023f-b42b-390c-bc28-6d6ac0c283bf | -3.0384 | -59.9108 | 2025-08-06 10:50:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| b4ce98ce-cd7f-37e4-b6e9-4080365e6595 | -8.9039 | -60.5769 | 2025-08-06 11:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 588dcfc7-0e11-3d3f-9462-8426eb595f68 | -8.9041 | -60.5577 | 2025-08-06 11:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 150.3 |
| e8f71647-f935-30c1-8d0e-b5285fdbbaf7 | -8.9038 | -60.5962 | 2025-08-06 11:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| e02788c3-e874-3302-b991-bc9642fcffdf | -3.0384 | -59.9108 | 2025-08-06 11:00:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| d169e486-7488-31bf-b748-eec24b6bc7c2 | -8.9227 | -60.5568 | 2025-08-06 11:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 01ff7c67-74cc-3953-a75c-29ed43bb8967 | -3.0384 | -59.9108 | 2025-08-06 11:10:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 0f0f6088-11ba-3c9b-b2ec-bf024066cb68 | -8.9224 | -60.5953 | 2025-08-06 11:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 69bf70fa-012b-3034-89b3-12f3bbd33381 | -8.9039 | -60.5769 | 2025-08-06 11:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 47819b77-295a-3854-99ad-e874afa0578b | -8.9225 | -60.576 | 2025-08-06 11:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| d566d337-8b27-3e00-8fab-e2642d46e593 | -8.9041 | -60.5577 | 2025-08-06 11:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| ca6e32f6-7327-3f3e-8cd1-cd9436c94567 | -8.9038 | -60.5962 | 2025-08-06 11:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| f17aadb0-5077-3877-b8d7-6b9cd93d3ee0 | -8.9039 | -60.5769 | 2025-08-06 11:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 63894558-3168-3ff2-8d16-538d24a53040 | -8.9041 | -60.5577 | 2025-08-06 11:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| ae4ef3fc-ab68-3b4a-bae3-a66308eec815 | -8.9224 | -60.5953 | 2025-08-06 11:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 751fd5a7-22fa-33a0-a9d5-c0869405843d | -8.9038 | -60.5962 | 2025-08-06 11:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 632ef047-84bc-3f33-bc36-0297e209094b | -8.9227 | -60.5568 | 2025-08-06 11:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 57a911cc-a62e-3f2c-842d-64b938658126 | -8.9225 | -60.576 | 2025-08-06 11:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| da01a9e9-118e-36da-a656-c54d68704de8 | -8.9227 | -60.5568 | 2025-08-06 11:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 85184848-14b3-3e8e-b797-e8773ed477cf | -8.9225 | -60.576 | 2025-08-06 11:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 48b8f7c7-eca9-33b9-916f-37ca6998afd6 | -8.9224 | -60.5953 | 2025-08-06 11:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| b5ddda1e-5432-3556-9fda-6ab7a897f720 | -8.9039 | -60.5769 | 2025-08-06 11:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 1f8884e3-96b3-3afb-a112-9003239b946a | -8.9038 | -60.5962 | 2025-08-06 11:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 629f0178-4635-3639-bac7-e62f28ef75cf | -6.2789 | -45.2716 | 2025-08-06 11:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 7a8484d7-e7ba-3b76-8536-1f4c3efcec13 | -8.9041 | -60.5577 | 2025-08-06 11:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| e5096ae5-679d-39a5-aea3-4ff53dd0dd3b | -8.9038 | -60.5962 | 2025-08-06 11:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| dd55ae3f-e640-3e7d-98ae-2cc5413a5bad | -8.9225 | -60.576 | 2025-08-06 11:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| a7496802-cd2f-3236-9c12-094575d3a8ac | -8.9224 | -60.5953 | 2025-08-06 11:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 43036705-ff4e-307c-b72a-96180c43e740 | -8.9039 | -60.5769 | 2025-08-06 11:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 55496afb-d429-3915-b864-766152c1669e | -8.9041 | -60.5577 | 2025-08-06 11:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 5f0ab9b8-f574-3d4d-a641-b9f47d304a6c | -8.9227 | -60.5568 | 2025-08-06 11:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 85dcd675-3340-303a-b317-82fe97742a0d | -6.2789 | -45.2716 | 2025-08-06 11:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 135.5 |
| bf65a408-c4d1-3d66-b1cf-df6a038f3991 | -8.9039 | -60.5769 | 2025-08-06 12:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 6dff5835-b893-3102-a078-4179f87d8e51 | -8.9038 | -60.5962 | 2025-08-06 12:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 2aa7c9c9-4c46-3de9-8573-0af749e10e4c | -8.9225 | -60.576 | 2025-08-06 12:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 9208aefa-13f5-3121-abef-6555eb18995b | -6.2789 | -45.2716 | 2025-08-06 12:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 46486d56-f362-34ee-856f-89f21082ff75 | -8.9041 | -60.5577 | 2025-08-06 12:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 58052e37-4ee5-3468-b1d5-321201c282e1 | -6.2792 | -45.249 | 2025-08-06 12:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 4cb1c4de-5301-375d-92ac-5ed02394e76f | -8.9224 | -60.5953 | 2025-08-06 12:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 5c68c08b-4dbf-3642-99bd-34be654da6b8 | -8.9227 | -60.5568 | 2025-08-06 12:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 93b30bd3-d8af-334f-b178-707f9a4f570d | -6.2792 | -45.249 | 2025-08-06 12:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 19befa0f-f026-3f5b-b8c4-b4c6e168fc05 | -3.0566 | -59.9105 | 2025-08-06 12:10:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 030605db-2fbe-3ae9-9852-a1e9538bed50 | -8.9225 | -60.576 | 2025-08-06 12:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f300d125-71ab-34d9-9bbb-807fc45f6478 | -8.9227 | -60.5568 | 2025-08-06 12:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 8d27c3ef-a1b8-3784-a158-297e89c2f5c0 | -8.9039 | -60.5769 | 2025-08-06 12:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 01a29000-f6bf-3f00-939c-21d7890c2e59 | -8.9224 | -60.5953 | 2025-08-06 12:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| aa2060f3-37dc-3471-9aa2-4990a9cf58b6 | -3.0384 | -59.9108 | 2025-08-06 12:10:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 88859527-fba6-3bcf-ba66-522678a778e7 | -8.9041 | -60.5577 | 2025-08-06 12:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 79329a72-dfea-396a-995a-a47393efa6bd | -8.9038 | -60.5962 | 2025-08-06 12:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 52af3071-284e-309d-b44f-5c9cb15b6dc9 | -6.2789 | -45.2716 | 2025-08-06 12:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 194.6 |
| ce46f8e0-d217-3439-a89b-7e66a5a64663 | -8.9039 | -60.5769 | 2025-08-06 12:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 0e9e6a2c-8bf7-311a-9fc6-ff5bd5fbec93 | -8.9225 | -60.576 | 2025-08-06 12:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e24cb160-0e2c-3ca6-9227-67dc77e368a6 | -8.9224 | -60.5953 | 2025-08-06 12:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 7264a48d-af48-3751-97b9-9499f921ee2e | -8.9227 | -60.5568 | 2025-08-06 12:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 03594e16-3906-33e2-83f7-a45e3c14804a | -6.2792 | -45.249 | 2025-08-06 12:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |


[Clique aqui para ver as próximas entradas](README32.md)
