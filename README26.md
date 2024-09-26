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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31a9837a-99a0-37fd-acc5-0b053a80f2df | -8.9223 | -54.739399 | 2024-09-26 00:56:33 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad06d69e-ea05-3ede-a968-f52ced9414b7 | -9.3776 | -56.8409 | 2024-09-26 00:56:33 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3826df0-2ca6-361a-95dc-64b1abbe34fc | -9.3795 | -56.8498 | 2024-09-26 00:56:33 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd29d187-4765-321c-8c52-d88e759b0210 | -9.3814 | -56.858799 | 2024-09-26 00:56:33 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d1d689e-cfd9-39d3-9be6-5620327f97a3 | -8.9093 | -54.7271 | 2024-09-26 00:56:33 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37231c6b-4889-341d-90f9-4efee9f17722 | -8.9109 | -54.734299 | 2024-09-26 00:56:33 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16402a5e-a10b-3ed1-9976-33be9b205d66 | -9.3697 | -56.851898 | 2024-09-26 00:56:33 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d997c096-ac57-34b3-91c8-8c53e6194510 | -8.8979 | -54.722 | 2024-09-26 00:56:33 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89a6da0f-d513-382d-9baa-84a265edf04b | -8.7954 | -54.676498 | 2024-09-26 00:56:35 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f4c1837-bbbc-386c-84e5-aacca3ae9efc | -9.3066 | -57.132599 | 2024-09-26 00:56:35 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b71162ca-d8ec-3dfa-abce-c50c97f402d4 | -9.3086 | -57.141899 | 2024-09-26 00:56:35 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43aaa936-1e92-3c0b-94c5-d5129b10863d | -9.2969 | -57.134701 | 2024-09-26 00:56:35 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a034579c-c877-3d09-a1b7-ef0d91e3612f | -9.2988 | -57.144001 | 2024-09-26 00:56:35 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87464574-23bf-3469-ae28-f4bade5642fc | -8.7477 | -54.740002 | 2024-09-26 00:56:36 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03fc8292-098d-3cd2-98c9-0c2ebfc04439 | -8.715 | -54.732101 | 2024-09-26 00:56:36 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48b1a3ab-0253-31d8-8baa-9e40de92daa7 | -8.7068 | -54.741402 | 2024-09-26 00:56:36 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea4cf89d-36df-3a97-971f-fe8fe23b5e74 | -8.7116 | -54.7631 | 2024-09-26 00:56:36 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a8da402-ae1a-3103-aeca-ed523953ca0e | -8.697 | -54.743599 | 2024-09-26 00:56:37 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30bb2a0c-503e-38a5-a178-3e2da0cacf7a | -8.7034 | -54.772499 | 2024-09-26 00:56:37 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35ef485b-85fd-3114-9d59-ef22a39f1739 | -8.705 | -54.7798 | 2024-09-26 00:56:37 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97c3decd-a5a3-35f4-906d-2cfb614ccb76 | -8.7066 | -54.786999 | 2024-09-26 00:56:37 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f940ab8-66a5-33ac-91c5-97c94b2e54b9 | -8.7082 | -54.7943 | 2024-09-26 00:56:37 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8668473-934d-3036-9472-73f9dfede7d3 | -8.692 | -54.767502 | 2024-09-26 00:56:37 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 812b00c7-9278-3bc0-a640-91af0c38a458 | -8.6936 | -54.7747 | 2024-09-26 00:56:37 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea4eb985-a1b8-3b6f-a1e1-db6bba70594f | -8.6952 | -54.782001 | 2024-09-26 00:56:37 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19fc1ca3-8938-3629-8d8d-e239686e394a | -8.6968 | -54.7892 | 2024-09-26 00:56:37 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0afa89fa-3094-3791-ae04-077455594daf | -9.2027 | -57.125801 | 2024-09-26 00:56:37 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0191cfc9-9d85-35e0-b151-20bc06bba269 | -16.3552 | -49.9256 | 2024-09-26 00:56:38 | GOES-16 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 62.5 |
| fd25ee5e-fb00-373d-9e1a-07be4e8ef79b | -16.3749 | -49.9223 | 2024-09-26 00:56:38 | GOES-16 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 3b00a5bb-d9af-3387-b28c-3142f61b43f7 | -8.6861 | -55.021198 | 2024-09-26 00:56:38 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91d2f4b8-9721-3476-9831-6b1f63204b6e | -8.6877 | -55.028599 | 2024-09-26 00:56:38 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1df0c0a-302c-3a28-8f67-9db6080e4f2d | -8.5334 | -54.561298 | 2024-09-26 00:56:39 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6281faab-506c-3a50-9f2d-74f4a2e3df35 | -8.535 | -54.568401 | 2024-09-26 00:56:39 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cafddb6-3d52-3227-9637-8b41df6390fd | -8.5236 | -54.563499 | 2024-09-26 00:56:39 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d79471d-9327-31c6-bf7c-a73bda9a3e18 | -8.5252 | -54.570599 | 2024-09-26 00:56:39 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dde1e6a5-6da3-3544-9ef0-aff3b8302b98 | -8.5268 | -54.577801 | 2024-09-26 00:56:39 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ed0b487-2482-3eb0-adae-43bf5271913d | -8.5284 | -54.5849 | 2024-09-26 00:56:39 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13532026-51f0-388c-b5f6-8709636a2ab0 | -8.5299 | -54.592098 | 2024-09-26 00:56:39 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d9d3c59-e6fc-33e7-9d86-9fdb3154c4dc | -9.5658 | -59.7393 | 2024-09-26 00:56:40 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0c7b753-4708-3b69-b739-19f9007fb88d | -9.5686 | -59.752998 | 2024-09-26 00:56:40 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fadb984a-583a-3ce1-a87d-9b1d627bdd00 | -9.5715 | -59.766701 | 2024-09-26 00:56:40 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec086a50-dc45-3785-810d-c82d77cf710f | -9.5588 | -59.755001 | 2024-09-26 00:56:40 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5dedea5d-bcec-3e6b-8c4a-388509a9c115 | -9.5617 | -59.7687 | 2024-09-26 00:56:40 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3f8a83f-05f3-3c67-a477-060027d683b2 | -6.7331 | -47.205898 | 2024-09-26 00:56:40 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0dc93333-c5c4-3f04-9ae9-bf54bbcf6edb | -8.4496 | -54.647301 | 2024-09-26 00:56:40 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bfc980b-6b9e-3731-ae51-8e43d17bb1ad | -8.4512 | -54.654499 | 2024-09-26 00:56:40 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd1c10ec-5557-3ab1-8bb4-20a70e028872 | -6.7234 | -47.208199 | 2024-09-26 00:56:40 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6d4c76f-9e18-3eb3-8475-bf9bfd79607a | -8.4332 | -54.666 | 2024-09-26 00:56:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4de1c6e9-e61d-336b-8942-f4f8ee77157c | -8.4348 | -54.673199 | 2024-09-26 00:56:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3af6ad50-51c3-34c6-a910-8f709690b4e4 | -8.425 | -54.675301 | 2024-09-26 00:56:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9da57b5-19d3-3c60-97cd-816b00784a00 | -8.4265 | -54.682499 | 2024-09-26 00:56:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 596a313a-f06a-3283-8b60-b717e2c63cb0 | -8.4281 | -54.689602 | 2024-09-26 00:56:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43e44457-d85f-330d-bc46-d43d683b169b | -8.4183 | -54.691799 | 2024-09-26 00:56:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05875a45-7e97-3127-8582-f686dfe920fc | -8.4199 | -54.699001 | 2024-09-26 00:56:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e68bd720-10c2-3f76-95e2-53c11c66d5c2 | -8.5241 | -55.173 | 2024-09-26 00:56:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32f29b84-15ed-3534-a606-8441c981c019 | -8.5257 | -55.180401 | 2024-09-26 00:56:41 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66aa656f-d44f-3be7-92cd-87a2e86d29f1 | -8.5143 | -55.175098 | 2024-09-26 00:56:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b09d8b5f-1cf4-38a4-8be3-579ffb2dffb9 | -8.5159 | -55.182499 | 2024-09-26 00:56:41 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b52fb13c-7555-33a5-a4c7-f137fc5e24c2 | -8.5176 | -55.189999 | 2024-09-26 00:56:41 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e660f43-957c-3593-93dc-2b348ff6d8ad | -8.9364 | -57.124901 | 2024-09-26 00:56:41 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 975e90bf-4f74-359c-8a96-1fc1b8f4ae15 | -8.9383 | -57.133999 | 2024-09-26 00:56:41 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 152e7395-db7e-3574-9379-f4dd6e8352ae | -8.4241 | -54.811401 | 2024-09-26 00:56:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 174ff52d-2e93-3aa7-9325-701bfa7ba65b | -8.4257 | -54.8186 | 2024-09-26 00:56:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33ac6f5f-7378-3eb5-8c67-5e794bdbfe21 | -8.0596 | -53.2202 | 2024-09-26 00:56:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8c7c4c8-9211-3ec9-a3f3-afc9adc6edc3 | -8.0612 | -53.227001 | 2024-09-26 00:56:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff027995-96ce-3658-9651-bc64321a893d | -8.0627 | -53.233898 | 2024-09-26 00:56:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f67a3476-980b-3c8f-8f98-4a0900eb7b5f | -8.435 | -54.9077 | 2024-09-26 00:56:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93f19a46-d33d-3730-9aed-c875df40883e | -8.4366 | -54.915001 | 2024-09-26 00:56:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28395436-d7fa-3890-8851-e6b89309c912 | -16.9729 | -57.931 | 2024-09-26 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.1 |
| a64ce488-fb4c-342d-9fb4-d4b53d39f983 | -16.9732 | -57.9106 | 2024-09-26 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| ec3ea376-3b02-3201-af5c-67073a7b8229 | -16.9922 | -57.9492 | 2024-09-26 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.2 |
| 2acf86a9-2095-389f-adf0-70c1452b38e0 | -16.9925 | -57.9288 | 2024-09-26 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| cef92078-7cdc-3fc2-8807-88e7e2eb2541 | -8.0483 | -53.2155 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60fb5786-a27c-3a5c-9a52-303b5d2280d9 | -8.0498 | -53.222401 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a584be6-b486-3a60-8926-5c06e7309800 | -8.0385 | -53.217701 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c327583-1a04-3870-b268-07b285751ed8 | -8.04 | -53.224602 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebbcdcd2-adca-3ed0-b0cb-ef24db2c3224 | -8.0416 | -53.231499 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f70abe8c-37fb-3dd0-93b1-7bf3d47e051f | -8.0431 | -53.2384 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce0dd6ac-7d94-32c1-b1d6-0940ae7f47e3 | -8.0447 | -53.2453 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdf2b9de-a9df-3ca2-84d2-072d88482d61 | -8.0462 | -53.252201 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23dd6187-b480-3761-a346-2864de68d35d | -8.0302 | -53.226799 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9112770e-ab7f-3cc6-a3fb-bd9b19db67a4 | -8.415 | -55.004002 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d99f16ac-f54c-339f-9fe3-b0ffd271ff34 | -8.4166 | -55.011299 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dfba05c-882e-3b87-8590-b0ae547c4767 | -8.4182 | -55.0186 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5479a117-6122-3eeb-80b7-1136b451eff3 | -8.3892 | -54.933102 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 693ad971-e76a-3bb9-9d73-f93b70951101 | -8.3908 | -54.940399 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 880ed776-dfd4-3bb9-ba28-f176cb57711b | -8.3924 | -54.947701 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 635de988-83c0-3cd7-97cb-3ebdd1e4c8d7 | -8.4052 | -55.0061 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d41a2049-861a-3773-8013-802da9a9f38e | -8.4068 | -55.013401 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5574b0fb-a727-3a19-b91e-0051b06c5ef8 | -8.4084 | -55.020699 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9dfbd9a-e5cc-3508-8d70-7ca8238f9079 | -8.41 | -55.028 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3795e846-29cd-3d6a-8dab-1aabf4dff22b | -8.4117 | -55.0354 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30e0f0a9-6cc0-39f9-80cb-0570ffcbfb89 | -8.381 | -54.9426 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 646e444d-82a5-3571-8771-97f524dd9d66 | -8.3826 | -54.949902 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b762ae16-737b-3bad-99f3-adcc4ac31246 | -8.3938 | -55.0009 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a076b7bf-289c-32b1-9cbf-51e4d64bbfbe | -8.3954 | -55.008301 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92c6f3ab-5577-3a14-b9f6-ad27adb24b57 | -8.397 | -55.015598 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbdf155f-cc89-3094-8ab0-9a2e4bb388ad | -8.3986 | -55.0229 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 599b73aa-6437-3840-b8e6-581df3d33b12 | -8.4067 | -55.059601 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d7e8a46-4e4e-3778-b661-b077dc721d53 | -8.4083 | -55.066898 | 2024-09-26 00:56:42 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README27.md)
