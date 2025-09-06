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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 246e98ff-0474-38db-a6b2-175b9917d8e3 | -12.9668 | -54.791 | 2025-09-06 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 84b96227-f255-3b2b-83ba-29c0ab119df7 | -21.3776 | -51.724 | 2025-09-06 00:00:00 | GOES-19 | SANTA MERCEDES | SÃO PAULO | Brasil | 3547106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 136.6 |
| d6818df6-abcc-3abf-a48a-0aa4f1bc9add | -8.4828 | -62.7116 | 2025-09-06 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 1cb0c4fc-0d11-360f-b650-cc26761fc8db | -12.5033 | -53.8712 | 2025-09-06 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 5d08f07a-ea93-3d47-bb28-f06710ff53eb | -12.9665 | -54.8116 | 2025-09-06 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| c786cec8-9442-3568-b1d0-224da8b4dd1b | -10.6131 | -44.3051 | 2025-09-06 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| fa02510d-cde7-3094-a37b-49235842cc73 | -12.9856 | -54.8096 | 2025-09-06 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 08a41262-64ef-37c4-8aff-bc7b46f17dd3 | -9.6877 | -49.2902 | 2025-09-06 00:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 9bced974-04ac-328a-a178-456df8ce65b5 | -12.5227 | -53.8485 | 2025-09-06 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| f4181ca0-c101-371b-9753-80cc2ee74bc0 | -9.7041 | -49.4825 | 2025-09-06 00:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 204.8 |
| 14bbf109-f519-3acd-a0ba-df3a25e669ea | -15.7186 | -53.5743 | 2025-09-06 00:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| eb05235c-7c7d-37d2-886d-9aa9cd921dda | -6.5393 | -49.5101 | 2025-09-06 00:00:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 90d06a8b-6421-3f9e-ac87-5fe8fcd0e663 | -12.4843 | -53.8732 | 2025-09-06 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 17e53741-c3e2-32a8-950f-d7bc59e4785a | -13.0041 | -54.8487 | 2025-09-06 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 63fb587e-4943-39a9-b074-70b20efc1673 | -9.7038 | -49.504 | 2025-09-06 00:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 55cd4f05-6d8e-3caf-b9d4-9057d063c128 | -4.4844 | -42.8866 | 2025-09-06 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 60290cf0-9139-3858-abd3-31b513027e17 | -22.2842 | -48.7412 | 2025-09-06 00:00:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.3 |
| ecb8ad47-c3ab-3406-811c-0750fb5fc417 | -22.2633 | -48.7463 | 2025-09-06 00:00:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 155.1 |
| 8e4534a2-1299-3ac3-80f5-1404b5616c49 | -9.6688 | -49.2921 | 2025-09-06 00:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 2915d3af-2720-3e2a-9159-52963e9dac22 | -5.4917 | -60.138 | 2025-09-06 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 44399664-dc3d-3fb6-bba2-384b3ac9e5ea | -12.4846 | -53.8525 | 2025-09-06 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 0a008d7f-b65a-3509-9ffd-feb865feb33a | -6.8095 | -52.8154 | 2025-09-06 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 91ea45f9-071b-3bf3-a350-445f7a84ed87 | -12.5224 | -53.8692 | 2025-09-06 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| e4793d3e-fb82-309b-b7ca-60970c84df4d | -4.5033 | -42.862 | 2025-09-06 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 5623a3a2-cebb-36f0-b9e1-fe3360ae81bc | -6.6913 | -63.1314 | 2025-09-06 00:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 22df09b0-592a-330f-92c4-f8f48069d631 | -3.2516 | -50.8082 | 2025-09-06 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| b5b3948f-224c-3670-8ada-4bc476a1f8a9 | -4.5031 | -42.8854 | 2025-09-06 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 169.3 |
| d4f7eb91-5944-3612-ba1c-9b83e3b2296a | -15.7381 | -53.5717 | 2025-09-06 00:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| f1bfe0a4-c8eb-3759-afd7-4b4fa17aa83a | -15.4562 | -47.1236 | 2025-09-06 00:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0d350fb0-ac5b-31fb-a6ae-8afbaa5c30af | -3.2516 | -50.7873 | 2025-09-06 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 37921a81-bc83-3710-9699-3cd2917c143b | -24.167 | -49.486 | 2025-09-06 00:00:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 95ea8513-ecca-37b8-8edc-fce8df069783 | -24.1449 | -49.5151 | 2025-09-06 00:00:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 706a85ab-d36f-3da9-ad67-d657221cb7ac | -10.5937 | -44.331 | 2025-09-06 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 244f19c0-6885-3129-a2d4-2ccacaeb27cb | -4.5029 | -42.9089 | 2025-09-06 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 550a3f72-0222-3f62-8185-ebfd3d437882 | -21.377 | -51.7464 | 2025-09-06 00:00:00 | GOES-19 | SANTA MERCEDES | SÃO PAULO | Brasil | 3547106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 137.6 |
| af7e056a-9a4d-3d63-95aa-f63bcf4b6f8a | -24.1456 | -49.4915 | 2025-09-06 00:00:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 1536f62c-6000-3e6b-9926-703cbfc1395a | -24.1662 | -49.5097 | 2025-09-06 00:00:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 195.4 |
| efb010f7-965c-3730-b5e2-a526403d4383 | -5.4918 | -60.1189 | 2025-09-06 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 45aa6b15-a78b-3bf3-b103-0c5b839c5db4 | -12.5036 | -53.8505 | 2025-09-06 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 134.4 |
| c712aced-ae29-3d91-910f-3d0242c3fce9 | -10.6128 | -44.3284 | 2025-09-06 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 183.6 |
| afeb6f55-5a47-3678-945c-09e271fa04b4 | -13.0044 | -54.8282 | 2025-09-06 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| b20b3942-e3c6-3d20-9b9a-67622cb39f7c | -10.5937 | -44.331 | 2025-09-06 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 500df8aa-44c4-3474-b8c8-af52aefcbece | -6.1945 | -53.2381 | 2025-09-06 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 0b689b2e-12c2-3b16-9aef-86b7c389276b | -12.5033 | -53.8712 | 2025-09-06 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 7772eca7-8f4a-3f68-b06d-2ef7d6cdd32c | -22.2633 | -48.7463 | 2025-09-06 00:10:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.6 |
| 47754c06-367d-34ef-9d8c-81f945a699b5 | -6.8395 | -62.9013 | 2025-09-06 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 7dbceaa3-0f85-3646-8aef-ee2d5a590a94 | -9.6877 | -49.2902 | 2025-09-06 00:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 0e65e326-6b82-3237-aab6-f2687ed35046 | -3.2516 | -50.7873 | 2025-09-06 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| cbdbee09-63db-344e-b0e5-7a83bc25a022 | -6.5393 | -49.5101 | 2025-09-06 00:10:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 6042a6ac-691d-3593-a275-06be6c9c4809 | -4.5031 | -42.8854 | 2025-09-06 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 5d8d6207-ff82-3886-819d-b6a49d70f1fe | -12.4846 | -53.8525 | 2025-09-06 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| f90d643e-de9f-3dc9-b468-b4f6a4ed62ef | -12.5036 | -53.8505 | 2025-09-06 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 1d29e9e4-6eb3-3bb4-ba67-cf6ff8b3b8dd | -4.5029 | -42.9089 | 2025-09-06 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c97962c5-c2a0-32ce-a0a9-8dc39f36c156 | -13.0044 | -54.8282 | 2025-09-06 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 89c508fd-dce6-31a7-b18e-e0a8fe07563e | -10.6128 | -44.3284 | 2025-09-06 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 184.2 |
| 24b7f5ac-d163-3bf2-bbad-23e26834bd90 | -6.1944 | -53.2585 | 2025-09-06 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 1c0232e5-f517-34a9-9b5d-c68e1e9abc5e | -4.5033 | -42.862 | 2025-09-06 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 612b4cfa-b469-368e-a099-d8b73576eb7f | -12.9856 | -54.8096 | 2025-09-06 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 6f7c1db4-2e77-3ace-b236-9d07c184b473 | -24.167 | -49.486 | 2025-09-06 00:10:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 97b02c56-04a2-31c0-bb85-67175f0887d2 | -15.7186 | -53.5743 | 2025-09-06 00:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 86a0effd-beb5-3ab1-9ee4-5ce6e0674667 | -4.4844 | -42.8866 | 2025-09-06 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 0cbc30ed-9f9b-320b-b3f2-1bd0da28d61b | -15.7381 | -53.5717 | 2025-09-06 00:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| d4c097cb-b4cc-367d-b40e-959e23fd4357 | -5.4917 | -60.138 | 2025-09-06 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| c6eed508-67b4-33e5-9c99-092de2ced7cb | -6.8095 | -52.8154 | 2025-09-06 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 770ae885-35ed-3500-80a8-156183651898 | -24.1449 | -49.5151 | 2025-09-06 00:10:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 202.4 |
| 153960f4-6017-3761-b8ba-37d90f5c8d94 | -10.6131 | -44.3051 | 2025-09-06 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| f75e79a8-6f75-36e6-a572-b5cdf7734032 | -3.2516 | -50.8082 | 2025-09-06 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| c59edafb-bd1d-3a87-a895-3397fdf3cab1 | -12.9668 | -54.791 | 2025-09-06 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| e2f2ae37-bcff-34c3-a06d-9addc0aee5b2 | -12.9665 | -54.8116 | 2025-09-06 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 6aa96319-c762-3003-889d-321ba201ef9b | -13.0047 | -54.8076 | 2025-09-06 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 7f0f4788-fd38-3c22-b43f-4898ca76b625 | -12.5227 | -53.8485 | 2025-09-06 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| f83e6d2d-9988-32ef-9181-5ce8c3dd625b | -5.4918 | -60.1189 | 2025-09-06 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 7a203410-f253-3467-9b7d-e1aedd068be1 | -12.4843 | -53.8732 | 2025-09-06 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| f9fa8085-af26-3415-84a2-3f930cf39848 | -15.4562 | -47.1236 | 2025-09-06 00:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 2f56325d-93eb-334b-b274-366717bc6f3b | -12.5224 | -53.8692 | 2025-09-06 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 3246d321-a9ad-3f23-8fbe-90ef00e58298 | -24.1456 | -49.4915 | 2025-09-06 00:10:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 634df4b9-ec4d-351a-a88b-12c9772c8813 | -9.7041 | -49.4825 | 2025-09-06 00:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 201.1 |
| 97d47866-8075-3118-a99c-1735fbd68a36 | -9.7038 | -49.504 | 2025-09-06 00:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 64f8dc24-e3fe-3da0-9c3a-199fa93055cf | -6.6913 | -63.1314 | 2025-09-06 00:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| fba9f2e1-1799-3997-b015-b15a1839b7be | -24.1662 | -49.5097 | 2025-09-06 00:10:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 02e30e9a-b342-39f1-bdc8-8db4a56b33d2 | -3.2331 | -50.8087 | 2025-09-06 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 28f3fca7-c011-33be-bcf6-1d992bef3d9a | -12.9898 | -44.529301 | 2025-09-06 00:15:00 | METOP-B | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 43cf31d5-92ba-3906-9e31-8b9f36744c17 | -3.1111 | -48.743301 | 2025-09-06 00:15:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92a13e0c-4331-3133-b97b-af3d7d0bd462 | -11.9887 | -53.923 | 2025-09-06 00:15:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e817e8f-4a49-3634-b810-950fa465a014 | -11.8861 | -45.726799 | 2025-09-06 00:15:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7724e2c9-8c8a-31da-a25e-13767b592c87 | -10.0122 | -49.757198 | 2025-09-06 00:15:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e918742-178a-3286-a376-78e1c90768d5 | -3.7784 | -47.914902 | 2025-09-06 00:15:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 675f0dda-887d-3a92-88a3-cb5dbdc17530 | -9.7034 | -48.3666 | 2025-09-06 00:15:00 | METOP-B | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9484cfee-b37a-3acb-a7ab-182eff8718e1 | -13.3553 | -48.1646 | 2025-09-06 00:15:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 646856f5-e8c6-3005-8729-50435e99c634 | -4.171 | -48.101101 | 2025-09-06 00:15:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90436960-df84-3cdb-82bd-2b53406fbb10 | -12.316 | -53.879902 | 2025-09-06 00:15:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca222e24-ec02-3de7-bc53-def8a0ace7b5 | -12.7405 | -48.084499 | 2025-09-06 00:15:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b574b8f-2520-3039-bdac-46cefcc4c15e | -12.7307 | -48.0868 | 2025-09-06 00:15:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c8534123-aef6-3c44-bbbe-5140a28408ae | -8.6757 | -47.287201 | 2025-09-06 00:15:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d5a672e-58cf-3425-a06e-bfe39b27481e | -7.8674 | -52.408401 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b315870d-d60c-3a6d-a40d-86682d00ea13 | -7.6093 | -47.539001 | 2025-09-06 00:15:00 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4191c319-d1c3-39e2-a4d1-b54636a9c0f7 | -5.7835 | -44.770699 | 2025-09-06 00:15:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71cdeaa9-156f-3004-a730-0dec606e3da5 | -5.85 | -51.7309 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 439fe37a-ca24-3b69-ae09-9826e4d365f1 | -11.1924 | -43.6605 | 2025-09-06 00:15:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1cf17cde-d9c4-3bec-808b-d1f9a4e9a1cd | -19.213301 | -44.366299 | 2025-09-06 00:15:00 | METOP-B | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
