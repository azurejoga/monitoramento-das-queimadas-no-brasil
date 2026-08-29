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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7d2af4c-94e1-3b89-a217-ea5a73be7cda | -11.0443 | -57.2222 | 2026-08-29 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| dd176d8c-f0db-3393-9b41-476fccfb73f3 | -6.7698 | -55.6844 | 2026-08-29 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 3cd35884-7d20-30bf-af8e-d488bec9403b | -6.7699 | -55.6644 | 2026-08-29 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 170.1 |
| 6d0e3f84-9078-3131-8fa2-bae90f7695b1 | -5.4177 | -43.1986 | 2026-08-29 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 9abcedfb-cd70-3917-9b68-0cbad1f148e8 | -20.2295 | -47.3875 | 2026-08-29 01:40:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 532f6c81-9f6d-38a0-8960-7c1e3527a02d | -7.2847 | -45.8652 | 2026-08-29 01:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| c1f61fde-8c5c-3ae8-9e80-6cbf194888f8 | -6.7343 | -55.4671 | 2026-08-29 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 4e17d047-be9b-387e-b988-b045c69bf9d2 | -8.9428 | -63.2797 | 2026-08-29 01:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 4ba13020-81a5-3348-b7d2-d39dda2c090a | -10.4794 | -64.5012 | 2026-08-29 01:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 1af8d3ed-1a1b-39dd-b82d-dce9df5e3995 | -5.8894 | -57.7708 | 2026-08-29 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 2d22a928-5a0d-3b7c-bb45-829a9326e009 | 3.1095 | -60.7081 | 2026-08-29 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.9 |
| ddd8a9be-f098-37a6-8ac3-8c09b2f09d03 | -7.5137 | -55.3051 | 2026-08-29 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 4aae1a92-2a63-35fc-b7ac-a3e47d9dee5b | -11.0252 | -57.2436 | 2026-08-29 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| e7611b59-7720-3f88-824b-d9344348a00e | -6.77 | -55.6445 | 2026-08-29 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| a2102154-182e-3047-b7f7-b320ab0d025d | -8.9613 | -63.279 | 2026-08-29 01:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 111.5 |
| c2e88dd3-0105-361d-a726-477b6786ea33 | -10.4981 | -64.5005 | 2026-08-29 01:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| a46f6dba-9415-343b-8ffc-dc0d5a1810e7 | -20.941 | -57.5694 | 2026-08-29 01:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 69.5 |
| f21ebe34-0416-3a5e-8c7f-faec515705ac | -5.8895 | -57.7513 | 2026-08-29 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 199.0 |
| 18fc5714-807f-323b-ab98-121b81b15b2c | -5.9079 | -57.7506 | 2026-08-29 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| e4df1ed0-6da1-3604-a71d-f6b9e1d5d48c | -10.4795 | -64.4824 | 2026-08-29 01:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 816a4afe-bd03-372c-8ed0-284726b3dd51 | -6.7884 | -55.6635 | 2026-08-29 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 0bb12dc6-1306-3e83-bf9b-a1e977d23cba | -11.0441 | -57.2421 | 2026-08-29 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 789b31e4-8e45-39c0-b95a-4d54b0c11ab7 | -9.51217 | -65.58329 | 2026-08-29 01:45:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 29.5 |
| bfd44945-877b-3bb0-9cfd-0518b2b13828 | -10.47955 | -64.51139 | 2026-08-29 01:45:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 26c3c287-a3ed-3588-9200-00b8b3f8fbe5 | -10.47309 | -64.47367 | 2026-08-29 01:45:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 9b97177c-3628-35db-b038-0f9467d56c6d | -8.82691 | -70.63273 | 2026-08-29 01:45:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2738fafd-2163-39bf-9bed-68d79d5ccb34 | -10.46717 | -64.5068 | 2026-08-29 01:45:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f61beeb6-2f38-360f-8e0f-122657328053 | -8.60219 | -70.22351 | 2026-08-29 01:45:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 2e3b8921-11b7-3e0f-a75a-51d8cd12abe3 | -10.48384 | -64.50366 | 2026-08-29 01:45:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 602b38d6-9504-3622-ac1f-8dd9ca4edebc | -8.59998 | -70.20897 | 2026-08-29 01:45:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 1d072aa2-2098-3802-ae19-ff21bd5ef5b1 | -10.49624 | -64.5084 | 2026-08-29 01:45:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 76444b32-7d6d-3d91-98e6-d8fd3b4113f6 | -11.0443 | -57.2222 | 2026-08-29 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| a2d94446-0c5f-30fd-a207-6a5262d239b3 | -5.8895 | -57.7513 | 2026-08-29 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 143.5 |
| b62c8938-d630-34ff-984a-0a143513329c | -6.7343 | -55.4671 | 2026-08-29 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| d59dc31e-2f12-3f52-bc24-4a7c5cd0a3cb | -7.5139 | -55.2851 | 2026-08-29 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| ad577b50-02b8-358c-a6a1-03a837bc910d | -6.7884 | -55.6635 | 2026-08-29 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| d7689476-b1b1-35a2-ad49-c14682558150 | -5.8894 | -57.7708 | 2026-08-29 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| fb0e81ba-11e0-34e6-b574-fd52f132bb5c | -5.9079 | -57.7506 | 2026-08-29 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 32f3af49-5dc7-3a1e-b16d-de9f5fe4fbde | 3.1095 | -60.7081 | 2026-08-29 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 75.3 |
| adffdaae-6f7b-39c1-8192-a3d69d967fe2 | -8.9613 | -63.279 | 2026-08-29 01:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 45315e98-42ea-3d01-b62e-8e788de8b808 | -8.9428 | -63.2797 | 2026-08-29 01:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 24a289dd-d946-31cd-b5f1-58a1e3dd4c9f | -11.0252 | -57.2436 | 2026-08-29 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 90686a8f-23b7-33a4-b210-e11c665998ad | -10.4981 | -64.5005 | 2026-08-29 01:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 3140bbc6-58ca-367e-959a-294a820511fa | -5.9078 | -57.77 | 2026-08-29 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 94d9358d-c055-3b9c-8751-4e4faa0a0369 | -10.4794 | -64.5012 | 2026-08-29 01:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 645ceb32-ea30-3301-b3e3-6b2ec1236e01 | -11.0254 | -57.2237 | 2026-08-29 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6917df6e-430d-3188-b894-4f2863830373 | -6.77 | -55.6445 | 2026-08-29 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 75dd41c5-9cae-3c16-871b-f5a8c482b24a | -6.7698 | -55.6844 | 2026-08-29 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| adabac2c-ba39-34fe-bf35-d67d07041059 | -10.4795 | -64.4824 | 2026-08-29 01:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 471922f1-68ca-396e-a102-a24840493d56 | -7.2847 | -45.8652 | 2026-08-29 01:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a945c10f-d418-3e49-bfb3-0c73ca4f4609 | -7.5137 | -55.3051 | 2026-08-29 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| ae027e46-d35e-39a3-bc22-44a4ce395f8f | -6.7699 | -55.6644 | 2026-08-29 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 168.8 |
| 06a5573b-aaac-33b7-8a73-1e4b6a7c8f7e | -8.9428 | -63.2797 | 2026-08-29 02:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 65ed4b29-e510-3f43-a05e-f634d86e92b0 | -5.8895 | -57.7513 | 2026-08-29 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 166.8 |
| b3271ccb-0947-3c92-93d9-2a1d939983c6 | -6.7698 | -55.6844 | 2026-08-29 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| d6f4fef8-0e71-3e6c-bf76-2af144f8a738 | -6.77 | -55.6445 | 2026-08-29 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| f0164183-1b7c-3286-bcd9-54081d25eb18 | -7.5137 | -55.3051 | 2026-08-29 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 55f5603a-65c6-3edb-8e0e-dda815291f42 | -6.7699 | -55.6644 | 2026-08-29 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 139.0 |
| c3c2b78b-3750-3864-8ebf-8f4fdaa81254 | -6.7884 | -55.6635 | 2026-08-29 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| f6b10909-e98c-35a2-8a13-56b3d6e1fa0b | -5.9819 | -57.6892 | 2026-08-29 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 99c0ddf1-24d0-3cc3-8400-79eec96b7dba | -6.6317 | -43.73 | 2026-08-29 02:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| a680a4f8-61c9-3683-a91c-c5fbe2b32ef5 | -10.4795 | -64.4824 | 2026-08-29 02:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| b38a0a1b-9768-3316-85d7-03d8134a00e1 | -5.4177 | -43.1986 | 2026-08-29 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 58da9f90-440b-3da4-9658-908fa506872a | -11.0443 | -57.2222 | 2026-08-29 02:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| f4edd82e-c700-3458-93cf-012652257f9f | -8.9613 | -63.279 | 2026-08-29 02:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| a46c73db-65af-3008-8670-058633aff0bb | -10.4981 | -64.5005 | 2026-08-29 02:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ac6258de-a182-3935-8a18-c507c923b072 | -6.6315 | -43.7533 | 2026-08-29 02:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 66c7d948-e753-3d6e-93cf-f4df43a688c7 | 3.1095 | -60.7081 | 2026-08-29 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 2cd6b007-61af-3b87-a93a-c7a9ff6645cc | -5.982 | -57.6697 | 2026-08-29 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 593fc862-159e-339b-9351-5e332c79275e | -7.6069 | -47.2837 | 2026-08-29 02:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 4ce682c4-f0c9-3b99-ba3f-4bd5d158b0e4 | -10.4794 | -64.5012 | 2026-08-29 02:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 6050cbd5-1e2a-31f5-8a64-9d5b1fea3d9c | -5.4179 | -43.1752 | 2026-08-29 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| c6e34f82-b1e5-3213-bd7a-f15b5baa5b2e | -5.9079 | -57.7506 | 2026-08-29 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| ce08738a-77f1-3f74-80cb-204292f5ac63 | -11.0254 | -57.2237 | 2026-08-29 02:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 73b408a4-d47c-35a7-93be-059a390f24ff | -7.4952 | -55.3062 | 2026-08-29 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 5b51a9bd-eb94-3657-ae30-ffc1220a059d | -5.8894 | -57.7708 | 2026-08-29 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 70080c23-d9fe-35af-803c-35d76043c8b6 | -8.9428 | -63.2797 | 2026-08-29 02:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 137.0 |
| a4e73172-5e92-3007-aaf2-1186941b809f | -6.7699 | -55.6644 | 2026-08-29 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 202.7 |
| cd5b07e3-c578-3057-a37d-f5b1fd0a25a5 | -6.7884 | -55.6635 | 2026-08-29 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 909c0eb0-64e4-38d7-a761-718c31b018a1 | -8.9613 | -63.279 | 2026-08-29 02:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 114.3 |
| d2eb33e8-a6e9-3ee5-8e7c-4c0d0c660100 | -5.4179 | -43.1752 | 2026-08-29 02:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 19b2ecd4-5630-3d7d-a29b-1dc9aac6e6a4 | -6.77 | -55.6445 | 2026-08-29 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 53498112-36d8-3311-a1fe-c3c7e573ed78 | -11.0254 | -57.2237 | 2026-08-29 02:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| e6f50578-b1ae-3d0e-bc8d-9f198b76ee87 | -5.9079 | -57.7506 | 2026-08-29 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 274ce382-d8b5-353a-a815-539ef2fd4d63 | -5.982 | -57.6697 | 2026-08-29 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f4b0c007-cd99-31ef-b7f1-2ea21884a688 | -11.0443 | -57.2222 | 2026-08-29 02:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 28350f8a-0d0c-32b6-b638-41e699af3616 | -7.5139 | -55.2851 | 2026-08-29 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| bc849bb9-671f-3ea3-a02c-d3f10e05dfb7 | -7.5137 | -55.3051 | 2026-08-29 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| a3dd7eea-b19c-3760-af96-ec410f2fda5c | -5.4177 | -43.1986 | 2026-08-29 02:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| b02f5a26-97e8-3745-b3da-3b73faead8ba | -5.9819 | -57.6892 | 2026-08-29 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 1787a38d-5714-30f8-bf33-15820d1e19c1 | -10.4794 | -64.5012 | 2026-08-29 02:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 87f0f176-3a3a-37a6-9e89-74352a792a57 | -10.4981 | -64.5005 | 2026-08-29 02:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| ed3233b6-6558-3b3b-b0f7-65fdc97845b5 | 3.1095 | -60.7081 | 2026-08-29 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 72.7 |
| b01398aa-b0ff-3474-bf4e-451cb28dc91f | -5.8894 | -57.7708 | 2026-08-29 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 003a3950-c405-33a8-a6d9-bd661fb39e87 | -10.4795 | -64.4824 | 2026-08-29 02:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 4b7c9b19-4852-3d81-bb03-6b00e118c528 | -5.8895 | -57.7513 | 2026-08-29 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 152.1 |
| e3f54deb-4a94-3b80-815d-a8a3ba948338 | -6.7698 | -55.6844 | 2026-08-29 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 38712112-7e7f-398d-819f-a02b36804225 | -6.6317 | -43.73 | 2026-08-29 02:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 2475af2a-9a86-3ca3-ab7e-097ac9c686ba | -7.5139 | -55.2851 | 2026-08-29 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 1263f299-337f-3ac3-9b87-aae08c8c103f | -14.9383 | -56.342 | 2026-08-29 02:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |


[Clique aqui para ver as próximas entradas](README19.md)
