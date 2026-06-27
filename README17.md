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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa16ceaf-02b7-3e9f-bfde-62c87ca6dae9 | -12.46404 | -58.49649 | 2026-06-27 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 1a8c2437-2013-3374-8b37-77da5ec2735d | -12.45838 | -58.48804 | 2026-06-27 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| dd5a1716-7a21-3c0c-8837-0623e691b7a3 | -12.46515 | -58.48909 | 2026-06-27 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 1598b7ae-ddf3-3b9c-bbdd-1ce7cab26393 | -9.0325 | -61.34099 | 2026-06-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22a62474-b8a4-3d54-b351-773f592f2c94 | -9.5937 | -56.9212 | 2026-06-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8314fae4-06c9-3798-992c-c85c7218d31e | -10.47902 | -47.11916 | 2026-06-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 817a954a-b566-38cf-a7bc-fd68c1e98003 | -12.46233 | -58.48485 | 2026-06-27 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13bc51a5-8360-3e68-9a8f-3fca50322cf5 | -10.90514 | -56.85841 | 2026-06-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d9d2fa66-3e72-3074-91d6-a8223935da6a | -10.7712 | -46.4723 | 2026-06-27 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08a6a711-3ada-342e-a662-5ef4c5f05ec3 | -12.46177 | -58.48856 | 2026-06-27 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 20a2df1f-5fb1-33e0-9318-f09e539724f7 | -11.91255 | -57.41743 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6102c3ea-baf0-3166-9771-a8610b90d09e | -10.93847 | -56.85488 | 2026-06-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 498f55d5-a416-38f2-8e6b-90d6414c1fe3 | -10.90217 | -56.85377 | 2026-06-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5c4a5758-a344-37b3-a57b-9f2244f9f48b | -10.48631 | -47.11435 | 2026-06-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ae1edd42-3271-3957-bb32-cea1bcc4d61c | -9.03431 | -61.3298 | 2026-06-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cfa3d472-bb14-3741-b3ae-21fe4b655690 | -12.45229 | -49.58598 | 2026-06-27 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd17721a-6ad8-35fd-b2f0-890cbc5876cd | -12.45499 | -58.48751 | 2026-06-27 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 64546406-aed3-3330-ac97-853b67845e87 | -11.92015 | -57.41451 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe920d8a-0d03-3b84-a7ce-e9f0ca185db1 | -11.91371 | -57.40945 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ff633b06-5aff-366f-a959-babfb77b69d7 | -12.62495 | -57.88691 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fb92ee46-70d8-3464-af61-444ebbdc5b34 | -12.52019 | -48.28425 | 2026-06-27 05:18:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a94df4c-e1a0-33a9-99d1-6a420cbca85a | -12.44066 | -49.58424 | 2026-06-27 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9e13a8e5-aa74-3d82-a0af-3fa64c42ba0c | -12.62438 | -57.89079 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e8f8e7d0-5c02-344b-b272-b6f4b1743ece | -12.62034 | -57.89415 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b652884a-1c96-3c4e-8f9e-d06266a13d20 | -10.54095 | -53.71049 | 2026-06-27 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56f4ef88-f8b1-34ea-a73a-238addba9fe0 | -12.3645 | -57.7341 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf1c5059-9733-3db8-b887-74c1957e6e98 | -11.87328 | -61.03571 | 2026-06-27 05:18:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e51d48a9-2b3c-385d-a417-a1eb67e52548 | -11.91429 | -57.40545 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a23fc6d7-9fd4-34e7-a897-4c291a0092ab | -10.48369 | -47.07903 | 2026-06-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acf0e551-efc8-3667-b558-093e19aa596c | -12.45214 | -49.58659 | 2026-06-27 05:18:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36e48033-5ddc-37aa-ac05-46171fe49913 | -12.60416 | -57.88367 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d628225a-07ef-36d7-ab14-031a9f6c924a | -12.62149 | -57.88639 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff97a0b6-2529-3a06-9faa-0fd7bbc6347c | -11.90903 | -57.41688 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15a8ca0a-39f5-3711-a915-df639fde6c88 | -11.64711 | -54.89577 | 2026-06-27 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1edc4ffa-7b1a-30f6-868a-1d9d3fa01637 | -10.39006 | -56.71997 | 2026-06-27 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d40dfc29-49eb-3095-b37f-425d4b8d02d1 | -9.19325 | -58.05482 | 2026-06-27 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 053d9b72-b1ff-3e7e-befa-5e63d7e843b7 | -11.64761 | -54.89217 | 2026-06-27 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f4b7514f-74aa-3b71-b94f-aa892def5c59 | -12.45726 | -58.49543 | 2026-06-27 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 9f4fd945-2574-3857-b40f-86311dab953b | -12.61456 | -57.88529 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 94bf9c5d-f297-3283-872f-b5cd7c4d1078 | -11.87924 | -57.81386 | 2026-06-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ddbdd60-abe9-39c1-9905-4bdec80b63e6 | -10.56683 | -46.23326 | 2026-06-27 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 812ba3b3-c57a-3655-bdce-b4ae7391d823 | -9.03712 | -61.33408 | 2026-06-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ee0cb67-4adb-300f-aac3-aa0b3d1b1895 | -11.66042 | -57.25933 | 2026-06-27 05:18:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6386952-f9ff-39d0-b300-c2d086e90b89 | -12.5528 | -54.59031 | 2026-06-27 05:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb63c37b-df6e-3ff0-89e0-23e66a4d51a5 | -10.80759 | -55.865 | 2026-06-27 05:18:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e98dec5f-0407-376a-84b5-58f75cc8f2da | -10.02121 | -59.35192 | 2026-06-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c3c23d4-cb2b-38a7-aeb1-8cc836c0eaf4 | -9.0309 | -61.32926 | 2026-06-27 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd1f782e-3464-35dd-9048-426b0b2e259c | -11.90668 | -57.40836 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4138ec8b-73c4-31c4-b04c-8e19aae1892d | -10.5584 | -46.24521 | 2026-06-27 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3881ed9a-29f9-3ee1-931d-79ba5583c52a | -10.57959 | -57.32053 | 2026-06-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d40bfad-4fa1-3380-8a2a-0499cbeacc09 | -12.79713 | -54.8675 | 2026-06-27 05:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab10415f-bb57-347c-a79b-16ed907ec86f | -12.46799 | -58.49332 | 2026-06-27 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa696ca6-83b0-3f98-8282-27082b172085 | -12.62091 | -57.89027 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 51177fd7-10dc-327f-b635-e244a333c634 | -10.78402 | -54.10561 | 2026-06-27 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 410dba05-891f-3cd5-ab53-1d083d905a51 | -9.59662 | -56.92567 | 2026-06-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 063ff88b-92ce-3156-a566-759bb5987790 | -11.62681 | -59.08382 | 2026-06-27 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 224c0df4-bee1-3f6e-ae57-909a0ae66e24 | -12.46065 | -58.49596 | 2026-06-27 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f2455871-3805-3127-8049-f0d4d5e15dbb | -10.30994 | -57.14486 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba25f1fe-a3dd-3f5a-b948-9f397b5840be | -11.051 | -52.46112 | 2026-06-27 05:18:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3b8b641-dca4-33ce-baf2-1aa3f159fb87 | -10.90157 | -56.85788 | 2026-06-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 698b8f26-f276-380a-8929-ff543bc9c537 | -12.62381 | -57.89468 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 50587e92-858c-3e82-84a6-bb7970939f50 | -12.61398 | -57.88919 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 75b02790-97c0-33e9-9656-bc5240ac37d9 | -10.48504 | -47.12519 | 2026-06-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4e5abfca-aab2-3f73-b272-400bea5519bc | -10.30294 | -57.14383 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3720b082-c1d8-3412-934b-23bffef02457 | -11.96787 | -57.70821 | 2026-06-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fd94b2c-2945-37fa-80b8-214b8bb42e1a | -12.46572 | -58.48538 | 2026-06-27 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f25a5df9-4ceb-37dc-ae53-ab64f0fda2ea | -8.23286 | -47.10885 | 2026-06-27 05:18:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| db3af8ce-56f1-3937-9157-617f2eed754a | -12.45894 | -58.48431 | 2026-06-27 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3664a2f3-6774-3e1f-95ec-364feb78f434 | -10.78924 | -56.7578 | 2026-06-27 05:18:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55efe3c7-9f4e-384a-897a-a7d8836b1327 | -9.58902 | -56.92859 | 2026-06-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4b1c56a1-2b1d-3270-a7fe-ce9bfbb17e6f | -10.30644 | -57.14435 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1891c1c0-df5c-39ad-aa0c-43ce04a76302 | -10.812 | -55.86097 | 2026-06-27 05:18:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55b6f3c4-6220-33b1-8acf-df1b25900edc | -11.90317 | -57.40779 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f77a7ffe-897f-32aa-bfe4-a67d35fe25af | -11.91664 | -57.41398 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 41d5399e-6a16-37ea-af08-e6e9128c5e6f | -10.05357 | -59.12109 | 2026-06-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5759c3f9-f5c9-3c4f-a5ba-596a3c8dbac4 | -9.47406 | -48.07087 | 2026-06-27 05:18:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 44a9611a-756f-3d45-b7c8-01c92ae04a2f | -12.61745 | -57.88973 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 7772f7d5-bfbe-3f6b-85ce-afdbd1ff57a7 | -9.60715 | -56.92726 | 2026-06-27 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c14ace52-d679-3076-8302-9db1010a7e98 | -10.19024 | -48.49799 | 2026-06-27 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e38741c0-022c-386e-b23b-ccfc3c58a659 | -11.90961 | -57.41291 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ae0c24a6-c553-32d6-b819-34dbd53a66f9 | -12.61052 | -57.88864 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ff959787-6d53-30ab-b937-236649f7b2ed | -10.5523 | -46.24414 | 2026-06-27 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 113a4030-3369-3f16-ac6a-fcdde8183a1b | -10.48693 | -47.10905 | 2026-06-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| edc5e975-51a9-322e-b48b-69d798042815 | -11.88212 | -57.81824 | 2026-06-27 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8af3269d-d922-3edc-ab93-49fc3308587a | -10.78984 | -56.75364 | 2026-06-27 05:18:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56df585a-3821-3b29-9aa4-43315a7ef9ad | -10.02452 | -59.35244 | 2026-06-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbeac1d8-c321-32c5-8fae-485a6b5b0287 | -10.4724 | -47.11821 | 2026-06-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| cb46eafb-c6cf-3caa-9420-5e4903971135 | -11.91722 | -57.40999 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2c9ef9b9-26fa-33bc-b9a9-42edfcfbce24 | -10.55164 | -46.24972 | 2026-06-27 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e6ef0aa-49ed-3188-893a-e68c5e1b9dbd | -12.60705 | -57.8881 | 2026-06-27 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d17fb191-839d-371e-8df1-ea647ef19337 | -10.78626 | -56.75309 | 2026-06-27 05:18:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba677e78-6885-386a-8c23-f0ba5dc72568 | -10.57389 | -46.23349 | 2026-06-27 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 393fb049-542d-30f8-9555-8f535306fcca | -10.54038 | -53.7146 | 2026-06-27 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ddc5415f-b294-3540-ab41-d89658fabc51 | -10.47178 | -47.12351 | 2026-06-27 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 46b94166-108f-3983-9160-74aae4bb194a | -12.45387 | -58.4949 | 2026-06-27 05:18:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 6de5ae35-018b-31f3-a551-c54139294c55 | -11.91313 | -57.41344 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3909c042-b6e0-3e8c-95c0-21dd0964f650 | -9.88037 | -52.44589 | 2026-06-27 05:18:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2792799-451e-3887-8db5-bac229fec9bb | -11.9061 | -57.41236 | 2026-06-27 05:18:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5d33f64b-a849-3a5a-bb95-eddf5bbe5472 | -10.47557 | -47.09098 | 2026-06-27 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4bf54e6f-3aa9-376e-a7f9-bced565317dd | -10.5514 | -46.24447 | 2026-06-27 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README18.md)
