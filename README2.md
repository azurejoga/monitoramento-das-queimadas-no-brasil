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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d659429-440c-30f8-858f-19a8f0c68964 | -6.7107 | -58.95592 | 2026-08-10 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| cdfa06e1-9aaa-3159-9b77-00792b31443d | -8.98231 | -60.54024 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 474a2223-d0c4-3c2e-b52f-9a2b9583db7a | -7.54194 | -55.57231 | 2026-08-10 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 991c249d-426d-3667-9909-d2360407bbb3 | -8.89397 | -60.56829 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| d60e4db7-6a65-38f9-bf67-77fb880353b2 | -10.87917 | -60.73567 | 2026-08-10 00:52:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c1c316e7-6a1c-35aa-8bc0-8661a958a177 | -8.94071 | -60.5163 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 1ad66835-b000-3eb6-b886-09506e4bee1d | -6.1505 | -57.72216 | 2026-08-10 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4c654dbe-d5e6-33cf-b94e-925a2fe2c56f | -6.70922 | -58.94572 | 2026-08-10 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 16ff7e4d-054a-32b0-b9e6-af12635c9874 | -9.81798 | -54.88982 | 2026-08-10 00:52:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| df46adf8-c004-3dd9-af58-05745aaa1cdf | -6.13991 | -57.70488 | 2026-08-10 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| ee5e0b88-f614-3978-a076-64bf9161e274 | -7.66245 | -62.55297 | 2026-08-10 00:52:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 46435753-d5f9-3745-8a6a-f21076ba3d60 | -8.95587 | -60.54403 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 73c6772b-5435-390f-904d-72c47a05f199 | -6.09691 | -57.69888 | 2026-08-10 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| cda2c0ef-cb7a-3f8a-903b-35bbb9a27ae4 | -8.64006 | -63.62383 | 2026-08-10 00:52:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 63b73ae1-b869-38b7-aeb0-78b714bacc7b | -8.95464 | -60.53515 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3070d9d8-61a6-3720-bea6-65a965ab3ace | -8.94316 | -60.53407 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 125.2 |
| a226de7d-4f23-360d-829b-b0d0741660ec | -6.14344 | -57.7296 | 2026-08-10 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cf016f2d-c44f-35b2-9d9c-58d788849e2f | -6.84048 | -56.41845 | 2026-08-10 00:52:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| b2d4c225-3e01-372f-949f-3b0f9ca52536 | -10.93723 | -57.1127 | 2026-08-10 00:52:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 5e5acdf9-1f7c-3c69-b119-779d0ab04d5e | -6.85171 | -56.41667 | 2026-08-10 00:52:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 98db0035-1b17-3d37-9fd1-1940c293d64a | -8.93948 | -60.50742 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 940bc81d-5eb0-333b-ae0b-583ef7886db4 | -8.90278 | -60.56703 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 10b341e7-e1a0-34dc-aced-b9514785df6d | -8.68229 | -62.87976 | 2026-08-10 00:52:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 90f8a734-2a18-39dc-b805-e4e14fbe3b64 | -8.90401 | -60.57591 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 67153f52-52ed-332c-b1d4-e8693c7061b2 | -11.20725 | -54.0262 | 2026-08-10 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 02f98d3e-f6f9-3c25-882d-d71feba793d2 | -6.14168 | -57.71727 | 2026-08-10 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| c404a8c5-54bd-38da-b63e-a80626cf9fc1 | -10.93895 | -57.12441 | 2026-08-10 00:52:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 260722db-7dd5-34b4-9f04-1634ce0a8dfc | -8.9571 | -60.55291 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| ce500fce-45c5-3a07-891d-65321c0fec45 | -11.21978 | -54.02389 | 2026-08-10 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 135bea4f-4abc-3034-ae1b-9205a836a350 | -8.95175 | -60.59621 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 36c2317d-d117-32e1-a0e3-ba17cbdb12d2 | -8.9735 | -60.5415 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d3149ca2-3431-3be9-9498-93e5cd633cd7 | -11.21907 | -54.02969 | 2026-08-10 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| ed58e7bb-e95c-3f2d-b0ee-2aa9da7863ec | -8.90843 | -63.96914 | 2026-08-10 00:52:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 5394e0d3-b9cd-31df-8d34-c779fe3df5e6 | -9.82073 | -54.90731 | 2026-08-10 00:52:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 73eede45-15e5-3bf8-a8a5-aaa36a344932 | -6.87307 | -56.63808 | 2026-08-10 00:52:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| dd4ad15c-2994-3675-a09d-ebbe8f081fb7 | -8.96468 | -60.54276 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 07e77761-fd44-3833-8099-31f1c8b2b3a9 | -8.89766 | -60.59492 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 629085f9-ed2d-3638-b452-98467ca5a9f4 | -9.71799 | -60.20355 | 2026-08-10 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a57a924e-bb66-3ea5-ac28-d976f95f76b2 | -8.95297 | -60.60509 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 33200b0f-a166-3a65-847e-94481fe5ac43 | -11.21041 | -54.04536 | 2026-08-10 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 077665bf-49a8-3756-97b0-0742ab69d968 | -8.94194 | -60.52519 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| b02c82f4-d588-306e-ac79-d547d59bf3ce | -8.16855 | -61.52157 | 2026-08-10 00:52:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 62df0671-d7d6-35ed-bc68-a98d3fd651d0 | -8.9608 | -60.57954 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9858f426-6c90-3e65-81e6-d9b303acf611 | -8.95957 | -60.57066 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 0f799a20-b46b-3f65-b44e-90198abf2bd4 | -7.38317 | -59.98555 | 2026-08-10 00:52:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ae915921-2de3-3e7b-a5e4-ea678b8539e1 | -7.55383 | -55.57047 | 2026-08-10 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| a884be30-2353-37f9-ab49-dcdf475bf4d4 | -7.66121 | -62.5436 | 2026-08-10 00:52:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d7daddc5-a6e5-31d4-aa8f-e5894410dbc9 | -6.15922 | -57.91313 | 2026-08-10 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 63d65560-1689-374e-bc8a-7653a20fe675 | -8.16734 | -61.51266 | 2026-08-10 00:52:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9fc7f111-b1f5-3158-a7ba-ff69f1bef875 | -7.47987 | -63.89214 | 2026-08-10 00:52:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 449add58-0486-3872-9fbb-f8638b2697fd | -8.96345 | -60.53389 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7d65b972-d377-3a98-a3a8-3df7b6b04f04 | -8.93825 | -60.49852 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1a45a0b1-98d8-3845-b481-2f9d3a6a498b | -6.16096 | -57.9253 | 2026-08-10 00:52:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| da37e359-148e-3d93-b854-79fe56266491 | -8.68098 | -62.86991 | 2026-08-10 00:52:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b5c49054-b964-3ac1-9c31-23cffd26651e | -7.68843 | -55.16064 | 2026-08-10 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 1dc5bc41-2e2e-343f-b04f-32f888baf3ee | -9.37621 | -57.36354 | 2026-08-10 00:52:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 50721904-a15a-386e-99f3-b818f2960722 | -11.20653 | -54.03201 | 2026-08-10 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 5b17c1e1-8ca9-3feb-9e47-d2107a9ba0ef | -10.90822 | -56.36701 | 2026-08-10 00:52:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 52f2fd8d-503e-3a58-a4aa-7072cf520e85 | -8.95834 | -60.56179 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 381f221a-5241-38a3-90a7-a4771b69fc1d | -8.89643 | -60.58605 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 861e2fbe-c701-3837-a25c-93d32f62b4a8 | 2.35939 | -60.14961 | 2026-08-10 00:54:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 5f6e8d50-b2cd-3da4-b2cf-195f36fe6b0b | -3.92713 | -59.13507 | 2026-08-10 00:54:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 8398f945-3c72-3f2b-9321-933341866cfc | 2.36089 | -60.13839 | 2026-08-10 00:54:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 694f6473-56b4-3b87-a813-926ab01db1fc | -3.93679 | -59.1337 | 2026-08-10 00:54:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 40eb4163-1d63-3350-af52-5355b0afa10f | -3.93529 | -59.12297 | 2026-08-10 00:54:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 8b711eed-5146-3dad-80d4-101deaeea7c5 | -1.6438 | -54.46825 | 2026-08-10 00:54:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| de8e7b4b-1b22-3956-9fed-5fb5924d7775 | -2.90683 | -54.1427 | 2026-08-10 00:54:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| aa62f321-8bfa-36ac-a8da-d4ca7f805eb1 | -8.9414 | -60.5367 | 2026-08-10 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 52b63ef7-f60b-34a3-95e1-8c804ada128b | -10.9326 | -57.1113 | 2026-08-10 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 745e8c89-3869-3ff6-9d1a-55caeb63670e | -6.8388 | -56.4146 | 2026-08-10 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 2b465efe-cbbb-3050-873f-703b36371759 | -8.8854 | -60.5778 | 2026-08-10 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| edfbed4f-6870-3bfd-9e5f-78c171a02943 | -8.96 | -60.5358 | 2026-08-10 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 1dd01fe2-9eb4-3b37-90bd-80767c383ab9 | -8.9039 | -60.5769 | 2026-08-10 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 142.6 |
| ea7960eb-b1d6-3d0e-840f-9131c155c26e | -7.5488 | -55.5629 | 2026-08-10 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 8d7cb429-d6ce-3baf-bf93-2bebe2ae3251 | -8.9038 | -60.5962 | 2026-08-10 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 0cd2cc14-3c7a-3ff3-abe5-5433b2b4e14e | -6.1476 | -57.7215 | 2026-08-10 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 576c8449-6dac-351b-bf07-777005fb52c8 | -8.9598 | -60.555 | 2026-08-10 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| c57f78bb-e2b3-3e96-9b85-17b375354598 | -8.9041 | -60.5577 | 2026-08-10 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 73c6e6f3-c0f6-3e2f-9836-f85992a0eac3 | -7.5488 | -55.5629 | 2026-08-10 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| e188660f-1ad9-3916-8f2b-9034b551e0f1 | -8.9039 | -60.5769 | 2026-08-10 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 28a9f32a-0975-3b49-ba60-318e42fa25b0 | -6.1476 | -57.7215 | 2026-08-10 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 71dc7c7a-4c7f-315e-9065-132415b1c7c1 | -8.8854 | -60.5778 | 2026-08-10 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| bf02701e-4a55-3bf5-8b00-c5ef66bd39e2 | -8.9414 | -60.5367 | 2026-08-10 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| dde30e78-8c43-3196-956d-aad9e9fafa6a | -8.96 | -60.5358 | 2026-08-10 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 8720caff-bb22-3588-9a22-ccdd3b72467a | -8.9041 | -60.5577 | 2026-08-10 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 51ae4977-0bb2-3534-bb24-ee0f59a53d05 | -8.9598 | -60.555 | 2026-08-10 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| e6d9f709-533a-3dd0-b18b-d13fb8d0ea05 | -6.1476 | -57.7215 | 2026-08-10 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| fd0c3030-3c74-39ff-b81b-b3dc46e10fdf | -8.8854 | -60.5778 | 2026-08-10 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| e7586ac1-0a1e-3653-8737-603434b3121d | -8.9414 | -60.5367 | 2026-08-10 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 3046f196-25b3-3368-9187-ec08129d2264 | -8.9039 | -60.5769 | 2026-08-10 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 98a84c77-ef9b-3394-9fe1-fc791405d810 | -7.5488 | -55.5629 | 2026-08-10 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 15cd337e-5b1f-3afd-a125-82b3e308ace1 | -8.96 | -60.5358 | 2026-08-10 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 1f6262cd-7037-3922-8aca-60ce0e11ac1f | -8.9598 | -60.555 | 2026-08-10 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| f6de1293-55a6-3e16-aad9-00ebe61c8013 | -7.5488 | -55.5629 | 2026-08-10 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| d13b7a22-8efb-3bbd-af1a-0fd0a8bb5437 | -8.9039 | -60.5769 | 2026-08-10 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| c8f07778-4606-3eaf-9d38-3c6623905314 | -8.9414 | -60.5367 | 2026-08-10 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| f188600e-5491-3560-a891-fec2136325d5 | -6.1476 | -57.7215 | 2026-08-10 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 79bdbf76-05af-3420-b3f2-9ca2130aeacd | -8.9598 | -60.555 | 2026-08-10 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 9fe1ab93-51d9-358a-91ae-7b3eb2eb742f | -8.8854 | -60.5778 | 2026-08-10 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 4e852b16-653b-3408-98fc-1018a2f908ad | -8.96 | -60.5358 | 2026-08-10 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |


[Clique aqui para ver as próximas entradas](README3.md)
