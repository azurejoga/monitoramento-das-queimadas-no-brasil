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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fa9072f-5821-39d7-954e-f33a4693e8ed | 2.70081 | -60.37047 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 29fb3bb5-b366-31e9-b0bc-9f4d0a36bac6 | 2.69693 | -60.38218 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 506cea96-6e6f-3f4b-b6ff-37713ac067ac | 2.7135 | -60.38296 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 56aa36cf-c82f-34f0-a6e1-0f214736ac70 | 2.70969 | -60.39143 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 427cba1e-17e2-31cc-a064-67ba68781ef0 | 2.69417 | -60.3641 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fc3caf1-9077-3403-ae58-fae1d3107041 | 2.70359 | -60.38865 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d5e2dcb8-df05-361d-9268-3d09bdf649c5 | 2.71297 | -60.37927 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 436854bd-4492-33ac-9f8a-36dbde9a731b | 2.70857 | -60.38411 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e08e46b1-560c-3f5c-8f13-1cfffd034315 | 2.71458 | -60.39033 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79356fcb-a1c6-31f2-8350-e5e1377c8015 | 2.70801 | -60.38046 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5fdb3dbd-e85d-3c9d-a6fd-0837d62159ef | 2.6997 | -60.36321 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 39.0 |
| df40d8f4-77fc-3b55-bcc0-03fc726f42f0 | 2.70267 | -60.34746 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b11c56ce-b368-3a59-baba-720ae070911a | 3.22363 | -59.90659 | 2026-03-11 04:51:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec9ac15d-76be-3540-9cb8-c13e921f91f7 | 2.71244 | -60.37563 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f9fef815-cd09-3dc8-a7c5-6e039000c40f | 2.71585 | -60.36024 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c6da0e3-7156-313d-b6ee-ba9b41847760 | 2.70192 | -60.3777 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 472711be-3bb5-3345-9848-e58ae9290a81 | 2.70356 | -60.35144 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de61a85a-7f2d-32f1-9bfe-6685f17988c0 | 2.69749 | -60.38583 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e6b3a75-35f9-3bfe-a834-10503ab93fe1 | 2.71638 | -60.36386 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 77087054-afee-3c5e-b121-4331a13965ad | 2.70925 | -60.35384 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab2c5445-2823-389a-9aba-29e9a6e920cb | 2.69582 | -60.37493 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 414a91ac-06bc-3f24-be05-758e291c7234 | 2.7085 | -60.38756 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 699967cb-44ea-3e9c-9e0d-17217b8799e4 | 2.71187 | -60.36866 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac930976-bec5-3ffc-8416-a0d71c75ffb8 | 3.22905 | -59.90577 | 2026-03-11 04:51:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 80141e84-84da-303d-bb8d-3c32a3dca73d | 2.69915 | -60.35958 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 00d8fd91-27f7-3d4d-8b81-1fbee62489db | 2.70373 | -60.35473 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 78abc510-1a41-3ce3-84a4-2ffcb35cd0bb | 2.71064 | -60.40223 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7412515-8133-3e79-bdc4-d6cbb1651ed2 | 2.70425 | -60.35836 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b29cd046-91a8-3012-93df-26ac43696614 | 2.70527 | -60.39964 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 978672c6-2ff4-3b4e-8409-0a9282bb4039 | -21.92262 | -51.85369 | 2026-03-11 04:57:00 | NOAA-20 | PRESIDENTE VENCESLAU | SÃO PAULO | Brasil | 3541505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 32a5b93a-8b4a-3b07-a43a-4e4bf72dd832 | -21.02562 | -55.76352 | 2026-03-11 04:57:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58fc89df-910b-3e95-978a-56ea39ee21f6 | 2.6903 | -60.3541 | 2026-03-11 05:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 96.7 |
| eafae318-b03c-3388-a78e-9fe13777b16c | 2.7085 | -60.3539 | 2026-03-11 05:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 130.2 |
| f4e83644-3189-3b32-a01e-29ac6d9e3b0b | 2.7084 | -60.3919 | 2026-03-11 05:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| b45ea10b-250a-3186-8628-d7ba14d2412e | 2.7085 | -60.3729 | 2026-03-11 05:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 162.1 |
| ae8282d8-5adf-3a82-9d46-46d428057cde | 2.6902 | -60.3731 | 2026-03-11 05:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 104.4 |
| d71ae664-1260-3e98-a748-c7ea5bfd502d | 2.68981 | -60.38085 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df9be1ff-238f-3afb-9d49-f015eb3b45e4 | 2.96586 | -60.1571 | 2026-03-11 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43a68467-d222-3c3b-8e69-0716f4aebb63 | 2.25682 | -60.28192 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c721dc9-17c8-39b1-878b-ac24fe716616 | 2.69918 | -60.37109 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56a80e4e-a670-393d-9d5d-5e30d601db00 | 2.77496 | -60.93417 | 2026-03-11 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 692062c2-25c3-37c5-90bd-ffe62bb7e362 | 2.69368 | -60.3595 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49ffd72c-2b1c-3e4d-a34c-c6d39d54fc05 | 2.70468 | -60.38264 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.7 |
| acc80fe3-9dc7-3974-82c3-9e1be407947a | 2.70048 | -60.37917 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.7 |
| be536944-b7ee-3d97-bd22-21f79db379e6 | 3.21734 | -59.90668 | 2026-03-11 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b95aa46-1bd3-316e-a211-2488da421812 | 3.5586 | -60.97738 | 2026-03-11 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6728cef-6a0f-3416-a3ba-72565040106c | 2.69628 | -60.3757 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 368a9718-3854-3e9e-99cd-9d9a8a437a48 | 2.71148 | -60.35669 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c9d5017-f7fd-3b2f-8f5a-005c9209f29e | 2.68657 | -60.36063 | 2026-03-11 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e7aba12-7ec2-319f-b1bd-4af7413cbbc7 | 2.67881 | -60.35777 | 2026-03-11 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 501ff61c-bc50-302c-b192-404415306a0b | 2.70759 | -60.37806 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fbf3e7be-7d1b-38ff-9aca-2e34b6b9d970 | 2.70661 | -60.39475 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fe8217d-d089-314d-b37d-ef2ac320995c | 3.55517 | -60.97792 | 2026-03-11 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 37b81854-b913-358e-a36e-93c8dc845e20 | 2.70339 | -60.37456 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ccc6d528-2f47-3157-a845-665489cca9a1 | 2.68851 | -60.37276 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d33c01bd-a02f-3376-84d8-20a141790fe6 | 2.70565 | -60.36592 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b85714f0-0025-3fe6-b845-b36abc6d1027 | 2.70371 | -60.39933 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1e6c675-05ec-3665-b078-9fa69f4d2ec7 | 2.69983 | -60.37513 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1bf800a2-436b-3b8f-b2aa-c16cb6bfba93 | 2.7063 | -60.36996 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b082e455-ed64-3564-b12a-e89674e7e88e | 2.71307 | -60.3896 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eba07791-c52b-3470-8391-29969ba3ed71 | 2.69498 | -60.3676 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 9f6a02d7-b4f9-321f-ba87-26d5268a082f | 2.70436 | -60.35782 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64929e09-8b54-3a2f-a167-afb3b69dfdf5 | 2.70274 | -60.37052 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36dd4a1f-950c-3ab1-9c64-eccce43303b9 | 2.70823 | -60.38208 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2cc075d0-a30c-34e0-9fda-571e61c54b7b | 3.22458 | -59.90552 | 2026-03-11 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c195582-68a0-33d6-b413-992e71403346 | 2.71243 | -60.38556 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 296d848b-2bbd-3053-aba9-ab39a94f1aab | 2.69467 | -60.38839 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34fe158d-c0f9-321b-b9f4-1c52d4a5e36e | 2.70242 | -60.39128 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23ed4a64-97bb-3803-bcc6-af4caea57d8f | 2.7008 | -60.35839 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 730b3010-5cc5-3278-9a08-780e78a50ba0 | 2.68691 | -60.38547 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55c2116b-a3eb-3823-8c87-1c2d8d296852 | 2.71017 | -60.39418 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 709acc12-a928-3bad-bf6b-cdc39ec98212 | 2.69012 | -60.36007 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a24d405b-d6f8-39de-a404-c603ad0e5f82 | 2.70209 | -60.36647 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 109.6 |
| e3d8881f-6384-32bc-b277-d7c150600e36 | 2.99143 | -60.06421 | 2026-03-11 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b3e9b40-a075-30e7-9860-f6a1a9e276b0 | 2.68948 | -60.35604 | 2026-03-11 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e83a429-a2f4-3cd1-99ca-b51d61a67f63 | 2.69046 | -60.3849 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33f04a92-fa0c-36a1-b797-c276c87306df | 2.70532 | -60.38668 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 214d3226-ad25-3166-80ee-7f0086a8f3d6 | 2.26043 | -60.28146 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f28ffa4f-7d86-3b4a-b4bd-d43122260ac8 | 2.98784 | -60.06478 | 2026-03-11 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 055640c9-22eb-31db-a7fc-d64fc7e0fdd5 | 2.71212 | -60.36074 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f4241b1-fa37-368a-a42c-3a1d7520f3e7 | 3.0012 | -60.03281 | 2026-03-11 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe935ff9-4022-3c16-88f4-4e33de542af6 | 2.70888 | -60.38612 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a1313bd-5d57-36dc-a161-76e2f7fc8668 | 2.68496 | -60.37333 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe22ab1d-06b9-39c7-aebd-dbe7c3b8ffea | 2.69337 | -60.3803 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1ef42d0-645d-3e95-981d-3f92246de4c6 | 3.22029 | -59.9019 | 2026-03-11 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 48f13d2a-bacd-32a7-aac5-ccc523cfbe0d | 2.69822 | -60.38782 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dee4a9bc-46af-36d1-9812-fe770a85f73e | 2.70792 | -60.35726 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7571fa3-1c59-3e90-a901-4494ca25a4c7 | 2.70986 | -60.3694 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88480ca2-2e87-3692-bbce-5df4cb1f9dfb | 2.69854 | -60.36703 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 109.6 |
| c25d47a7-ddc8-3a6b-8e31-db79bfdec0b0 | 2.69757 | -60.38378 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 87333f87-f7f4-3c01-ae90-2f91fdd74ae0 | 2.68916 | -60.3768 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c147de82-08b3-3ea5-93c4-5a993dc51830 | 2.68236 | -60.35719 | 2026-03-11 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bacbc78a-c3f2-3a9d-b0b3-97b52657b364 | 2.69272 | -60.37625 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7c81aef-39fd-39f6-b9b7-483a26be7633 | 2.68592 | -60.35662 | 2026-03-11 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e642de94-cbc4-39c1-85dd-7c600a2177fc | 2.69402 | -60.38433 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8f0efde1-4127-3179-bc04-c9487d0dd555 | 2.68561 | -60.37736 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b27820e-847b-306a-bb77-6d1b56f9c017 | 2.70113 | -60.38321 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.7 |
| e9418bf2-cf94-380b-9d1b-baf1a1fd216e | 2.70403 | -60.3786 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 49175d48-ca93-37cf-8f76-829450b48f77 | 2.70371 | -60.35378 | 2026-03-11 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05cc1347-4e10-380c-bc5e-835862998c9a | 3.22325 | -59.89711 | 2026-03-11 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README5.md)
