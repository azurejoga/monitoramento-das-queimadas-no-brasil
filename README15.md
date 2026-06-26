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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2b8b5e1-e662-3242-8251-c90e4e82d6f9 | -12.76441 | -59.00764 | 2026-06-26 04:53:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c57221f9-2b74-3b7c-aec6-6656e123658b | -13.25957 | -54.42868 | 2026-06-26 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c5599f86-3257-307e-8dde-92843c2c0d68 | -12.55562 | -54.58593 | 2026-06-26 04:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1368f11b-c0c3-31d1-a0a3-defd2a8a9cde | -12.55498 | -54.58974 | 2026-06-26 04:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5cd1b6b-14c9-3ac4-9a85-e35fb8e3e58a | -13.25618 | -54.42811 | 2026-06-26 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 01b4f20a-6a7b-3382-b4e4-6dda5c2b2671 | -11.9411 | -57.70071 | 2026-06-26 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a6d916f-01e2-3296-8bc0-aee53a7d2ebe | -15.60308 | -48.35713 | 2026-06-26 04:53:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f5d23df7-b8e0-3122-9066-32ad125ec246 | -11.91405 | -57.10229 | 2026-06-26 04:53:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0682d15f-e554-301c-b6f6-8ab43e4fe7c0 | -14.83866 | -48.129 | 2026-06-26 04:53:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f178316a-fc63-39fb-9894-65a7eb4432e9 | -13.85648 | -47.14738 | 2026-06-26 04:53:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e65c055a-ac06-3e9d-ae4e-bb4c73163944 | -13.72658 | -54.04834 | 2026-06-26 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 190b4119-69e7-3e82-818a-bc106aed12a1 | -13.72523 | -54.04474 | 2026-06-26 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0885f7fe-f254-30ed-bd60-90f76aa99374 | -14.83986 | -48.13269 | 2026-06-26 04:53:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13a29934-3d91-3f3f-8d8b-30f88294afee | -14.8447 | -48.11413 | 2026-06-26 04:53:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3c802b32-7620-334c-a6c9-d38e4089bfda | -12.76519 | -59.00331 | 2026-06-26 04:53:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 561f9319-2ef2-38f0-8024-d8e9661fd9c1 | -13.73388 | -54.04583 | 2026-06-26 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bd1039e2-805e-3738-bf6f-a4b6d416437c | -11.94175 | -57.69707 | 2026-06-26 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d754f72-2429-3791-a860-06a83a436bab | -14.84265 | -48.12952 | 2026-06-26 04:53:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd616eac-7cbd-3fea-b264-884eca47b1c5 | -14.19351 | -47.6834 | 2026-06-26 04:53:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76195af4-e719-3a37-b874-981548d7cbea | -12.61161 | -57.88401 | 2026-06-26 04:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f18091b4-1b7d-3c87-b5d9-44d93e07b281 | -15.66607 | -49.38549 | 2026-06-26 04:53:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d5bd653-243c-3eb0-be25-51790a61bdb3 | -13.73568 | -54.03493 | 2026-06-26 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 859eeaea-c188-3f5d-9906-ecb1f11a6d17 | -11.91796 | -57.10304 | 2026-06-26 04:53:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 081a03e4-2f7d-34f4-bc0f-c9b3e54780c7 | -13.85235 | -47.14644 | 2026-06-26 04:53:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fceceda-1710-337e-b7c1-bc88ed529c38 | -13.72464 | -54.04839 | 2026-06-26 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24dd5a77-834a-3233-9ffb-11679603dec6 | -13.73233 | -54.03436 | 2026-06-26 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b50b20e-c434-3317-adf2-e0e6a669a9cf | -12.55092 | -54.59295 | 2026-06-26 04:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1025d4df-01fb-3d60-99e8-4e39e1378bb4 | -14.27836 | -47.4165 | 2026-06-26 04:53:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56e7bb81-0b99-37a5-8774-5baa4e84c524 | -12.76495 | -59.00652 | 2026-06-26 04:53:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77a412cb-622d-310c-8da6-66040861142c | -13.73113 | -54.04163 | 2026-06-26 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e67d7e42-bf01-34af-ab44-45abb00f39d8 | -13.27377 | -54.4273 | 2026-06-26 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 801ee2ca-553e-3a0d-9bb8-43642ef3e9fd | -12.69002 | -54.58139 | 2026-06-26 04:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56b7b9e8-a831-3f2f-8014-635d2b5386b9 | -13.45815 | -47.86437 | 2026-06-26 04:53:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de213ead-ac4b-3758-be78-cf7da647a629 | -17.9705 | -44.56522 | 2026-06-26 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b38e61e6-ce45-35bf-857b-8a7c790ab0e3 | -13.86845 | -47.12214 | 2026-06-26 04:53:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33e9df6c-996e-30cc-b16f-b3678db09571 | -15.6397 | -46.43127 | 2026-06-26 04:53:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 170f0b8a-ad47-361f-9776-5ef17fa3b6cd | -13.72641 | -54.03747 | 2026-06-26 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27349686-5cc4-368d-8dcd-0af17b2fb71c | -13.73329 | -54.04948 | 2026-06-26 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6ba66f89-3be9-3417-9a80-a92cf1683594 | -14.63633 | -54.4625 | 2026-06-26 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cfd38b05-85f9-377e-9273-af865eb32a96 | -12.55156 | -54.58913 | 2026-06-26 04:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ac1f3e6-7a00-355c-9f36-04461ffa2b7d | -23.61825 | -53.20582 | 2026-06-26 04:53:00 | NOAA-20 | MARIA HELENA | PARANÁ | Brasil | 4114708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2cee3c81-90bf-34a5-abce-81b2da935941 | -13.07502 | -57.76962 | 2026-06-26 04:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0f1af18-3b69-3827-9f19-1f71e4a897de | -14.87994 | -54.54555 | 2026-06-26 04:53:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ac77ce6-23d2-339c-88fb-f8e85b933352 | -13.27037 | -54.4267 | 2026-06-26 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc34755b-f2d2-324d-b102-c104d602175c | -15.59912 | -48.35661 | 2026-06-26 04:53:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 03bf88e1-e703-3050-9b05-90d21c0326cf | -14.84399 | -48.11947 | 2026-06-26 04:53:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 539d58f6-f674-327e-8c23-a54231127acf | -14.19301 | -47.68703 | 2026-06-26 04:53:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fff9a6ff-119c-3685-b425-837acde2c5bb | -12.54486 | -57.2067 | 2026-06-26 04:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60ea52d8-8847-3dd0-8c08-8e3322e17e52 | -12.54572 | -57.20165 | 2026-06-26 04:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f498ff59-ebc8-390f-8663-5876eeddf13e | -13.92424 | -47.34686 | 2026-06-26 04:53:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bf40a9e-9a80-3c35-8866-3e4087b09b71 | -14.63297 | -54.46193 | 2026-06-26 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 264c6627-6c1a-387e-9d63-f1bd95b1c7ac | -14.90874 | -51.05656 | 2026-06-26 04:53:00 | NOAA-20 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07f02784-724f-3e24-a68d-d9c3c1ef823b | -12.54797 | -57.18828 | 2026-06-26 04:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd739e73-7c0e-3495-8568-584bc8c3a53b | -12.55435 | -54.59354 | 2026-06-26 04:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1da8123c-070d-3279-94c7-25abda8cc125 | -13.84457 | -47.14107 | 2026-06-26 04:53:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62448d08-6e0f-37d6-8e41-f874b0f738fb | -12.54746 | -57.19154 | 2026-06-26 04:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ac5c771-69a4-370f-bd96-9056a5341d19 | -13.25895 | -54.43242 | 2026-06-26 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 07073c01-8a0a-39db-8228-2173e05b63e6 | -14.34956 | -54.5245 | 2026-06-26 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03078eea-4d51-3efd-976e-e8076e3dbea1 | -12.28653 | -57.54715 | 2026-06-26 04:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5082cc0e-28dc-3ad0-93ec-50ed09bcc8ab | -14.6917 | -46.14635 | 2026-06-26 04:53:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7d1c4ef-b160-359f-95e2-92a221d3f7e3 | -17.97013 | -44.56869 | 2026-06-26 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6bfb736-0b98-3aa1-95b7-229a4e0d54a9 | -11.96959 | -57.70584 | 2026-06-26 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca2c395c-d3e5-3444-9075-785a3ae63d9b | -13.06153 | -53.35377 | 2026-06-26 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d83c0ec-a9e2-34c1-baae-be3744f3c5de | -13.26019 | -54.42494 | 2026-06-26 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9f0e0fa1-b746-3a6f-b03d-fb150fe537f4 | -13.26297 | -54.42927 | 2026-06-26 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d1e4af6f-1aba-3f04-885e-103ee953e6a4 | -14.52761 | -49.10888 | 2026-06-26 04:53:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a5660b28-4803-36d7-bae5-1b345950b7d1 | -13.73269 | -54.05312 | 2026-06-26 04:53:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 850862bc-4284-376f-8b70-85dd04acace5 | -14.34895 | -54.52821 | 2026-06-26 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec3ff3be-114a-3036-81c8-a23d3acd2196 | -14.87658 | -54.54498 | 2026-06-26 04:53:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f78896f-6927-3d18-8161-6b4ecb6ce4e5 | -13.87295 | -50.39744 | 2026-06-26 04:53:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b76e3ad4-753f-3836-94b1-a7e6e3f68cdc | -13.26359 | -54.42552 | 2026-06-26 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 63f843e9-fa46-3533-9ec7-b609430760d8 | -28.15148 | -48.81797 | 2026-06-26 04:55:00 | NOAA-20 | IMARUÍ | SANTA CATARINA | Brasil | 4207205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 866a1ef3-29b9-3b7d-900b-2c232057909e | -27.86994 | -49.06737 | 2026-06-26 04:55:00 | NOAA-20 | ANITÁPOLIS | SANTA CATARINA | Brasil | 4201109 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 72614cfd-c529-32e1-b814-55fc67542c7f | -5.7758 | -45.0599 | 2026-06-26 05:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 72d90ac6-85aa-33b1-90d6-68278ee6c626 | -5.7945 | -45.0586 | 2026-06-26 05:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| f9db7973-454b-3763-a9b6-31511212fb80 | -5.7945 | -45.0586 | 2026-06-26 05:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| f02e0385-ef44-3cdb-b13f-81e1181e8714 | -5.7758 | -45.0599 | 2026-06-26 05:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| e81e958d-1cbf-3f49-8529-c4e4955d40e0 | -5.7945 | -45.0586 | 2026-06-26 05:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| f663daf5-c93c-3b32-bf6a-cf43a3e15782 | -5.7758 | -45.0599 | 2026-06-26 05:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 941b383d-a90e-3db3-92ed-9a077a563ce9 | -5.7945 | -45.0586 | 2026-06-26 05:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| a08a420e-8ea6-353d-965f-173999f16773 | -5.7758 | -45.0599 | 2026-06-26 05:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| be8c1a00-9ee6-351a-95d5-3ff13fbf1b7d | -8.44104 | -51.56004 | 2026-06-26 05:36:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75b37c71-5144-3859-bd12-61a20690fdf6 | -8.4476 | -51.56115 | 2026-06-26 05:36:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5239247-cff5-3a7d-8da2-670d410d67f5 | -9.59097 | -56.92277 | 2026-06-26 05:36:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eeded24c-f7a4-32e3-a029-98c8c74be94c | -9.60982 | -56.92536 | 2026-06-26 05:36:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a626ba61-082d-38e5-bcc2-063d78f352d4 | -9.36627 | -50.55122 | 2026-06-26 05:36:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| eae7aec8-1400-3cbe-9e4c-2237e76a036f | -9.18557 | -58.07006 | 2026-06-26 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb8ed9d3-4118-34f2-bcff-4e239bd76b1d | -8.44631 | -51.5594 | 2026-06-26 05:36:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aee369b6-7db3-3b8e-8655-9221335fdb14 | -9.48544 | -57.32554 | 2026-06-26 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53a99eb4-1233-3e1c-bf5d-32e95ef28478 | -10.13137 | -52.11193 | 2026-06-26 05:36:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cc22bca6-c390-3975-8818-a2b39e1038ea | -9.20417 | -58.94085 | 2026-06-26 05:36:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33abe26c-119d-3a0d-a47b-5e2abdffe383 | -8.43975 | -51.55832 | 2026-06-26 05:36:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f633cec-7904-3092-8111-993996716589 | -9.36937 | -50.54716 | 2026-06-26 05:36:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| aec1b251-2370-3086-96db-066e67a62e8c | -9.59568 | -56.92344 | 2026-06-26 05:36:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf5545cd-83ea-3f6f-8c75-00adf8aff478 | -9.18061 | -58.05896 | 2026-06-26 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c58a6b84-bc0b-3e38-9804-8551123dacf2 | -9.48152 | -57.32015 | 2026-06-26 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6345293-6508-37c7-b248-772208970805 | -9.19046 | -58.06651 | 2026-06-26 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bef783c-35ee-353d-a859-c0effdc324b3 | -9.26355 | -59.83313 | 2026-06-26 05:36:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 146d8db7-faeb-3a21-9def-085f2e1ae74a | -9.36705 | -50.54427 | 2026-06-26 05:36:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6ab3a00e-276c-32b7-b99e-7990d8f29f33 | -11.94311 | -57.69905 | 2026-06-26 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README16.md)
