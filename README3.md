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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e27cc450-5fda-3ee2-bf64-4319c61afb5b | -20.16181 | -50.60991 | 2026-01-27 04:42:00 | NPP-375D | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a6d5b9a9-eb0a-31e1-9a34-878e423211a4 | -20.16123 | -50.61362 | 2026-01-27 04:42:00 | NPP-375D | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 41640743-5947-32ae-9467-34e644012cb3 | -19.10177 | -57.7747 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 281cf9bd-5fd2-35de-ab42-61dc2009b6bf | -19.60625 | -57.35121 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d42892d8-b930-3a4e-9ad1-728dcf840cd1 | -19.61213 | -57.37648 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| be49560c-3f60-32b7-8537-b8acc16cba35 | -21.30754 | -49.33789 | 2026-01-27 04:42:00 | NPP-375D | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aeed24a5-75ce-3475-bb4f-b19d40713a9e | -20.92581 | -56.3714 | 2026-01-27 04:42:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b0a1baf0-3d86-3983-b4be-042e2465bcea | -21.99302 | -48.41061 | 2026-01-27 04:42:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1e4cd2d-819f-3471-a0c6-5cbab7dfa923 | -19.72003 | -56.82228 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| f15c3eae-0927-340b-9519-6ea0901a2598 | -21.78913 | -52.73003 | 2026-01-27 04:42:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e244150a-f801-3206-b53c-3af680ff774b | -21.78451 | -52.73701 | 2026-01-27 04:42:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55c42563-e6f9-322b-aa9c-b8e379895d2f | -19.7004 | -56.828 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7f763a5f-ddad-3070-a323-0f17fc425e56 | -19.71515 | -56.82531 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 62963d1b-f6e4-3bf9-8ab0-a2a96cf62ac6 | -20.30186 | -57.82925 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d44fa657-910a-30e1-9535-3a0afc4c3e04 | -19.61297 | -57.37224 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4a492b6a-2676-3119-83c7-3b6110212ae7 | -21.7437 | -52.75299 | 2026-01-27 04:42:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88926cec-2180-35bd-a012-e9f8707a4aa5 | -20.61827 | -50.38725 | 2026-01-27 04:42:00 | NPP-375D | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 709e0e7f-dfa4-3f2f-8d5c-599be349c34f | -20.91793 | -56.36979 | 2026-01-27 04:42:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ad70ee88-5838-38c4-b651-601467926a12 | -19.69788 | -56.82569 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bd9c31b5-2e20-3462-963f-3e5d76317748 | -19.61036 | -57.36284 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 473555cd-931a-3fbe-b134-b0536bd0c994 | -19.34411 | -54.17335 | 2026-01-27 04:42:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a636ce87-7403-39b1-afa4-d79ab5cc206c | -20.84377 | -51.74013 | 2026-01-27 04:42:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 65d59bc3-19c5-3f1c-baec-8b81119ef96b | -21.79648 | -52.7275 | 2026-01-27 04:42:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b4c9636-88a8-3a47-a950-df3e126f9178 | -19.60609 | -57.3619 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e7475691-1ed6-32de-9364-99529ecca935 | -19.70114 | -56.82407 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| dcb551c5-665d-3b7d-b650-8ce7bb3085c3 | -20.64117 | -48.83582 | 2026-01-27 04:42:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5ac4f740-8bf6-3687-bf27-201087d53dd3 | -19.71177 | -56.82051 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5db2a947-043e-346c-bfcf-bc7edfcaf6d7 | -20.30274 | -57.82484 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ab67c4bd-f9e3-3a1b-ae4e-9418bcdfb54c | -19.68602 | -56.92787 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 91556f94-2598-3137-89a0-f1e65a45965b | -21.24437 | -49.36951 | 2026-01-27 04:42:00 | NPP-375D | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1a9c27c8-8b92-3cba-ba75-8c163e59c96e | -19.70201 | -56.82657 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 992b5f3b-e868-3681-b2a2-45305e691ac8 | -19.70527 | -56.82496 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e56f8626-0832-3a07-b0fa-485108b18a17 | -19.7234 | -56.82708 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| f663f011-da4a-3db9-9a35-7a5f827cb65b | -19.60545 | -57.35545 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9c24db1c-1dfb-311d-a455-e7f1ecbc1ffd | -19.60953 | -57.36707 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0f4470d7-542c-3dc5-a6c6-b489607ba1db | -19.60705 | -57.34697 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e565e4cf-bcda-3d34-a360-e32707cddf4b | -21.30408 | -49.33733 | 2026-01-27 04:42:00 | NPP-375D | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 595812cb-a3ae-3f14-837f-5fff6178e1fc | -19.66853 | -56.83752 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 368bea46-7acf-3654-9c45-dee09f6bf46c | -19.66365 | -56.84057 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8de1e7bd-ac0a-3926-9c55-4e6c2bb0165a | -21.78976 | -52.72624 | 2026-01-27 04:42:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31d5c668-9e81-36a3-b10d-cd739c758330 | -21.79312 | -52.72687 | 2026-01-27 04:42:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 407cc7c1-87f3-316e-85cf-500036193a24 | -19.71102 | -56.82443 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1d5802d8-9688-3e00-9d7c-7e54388731df | -20.16238 | -50.60619 | 2026-01-27 04:42:00 | NPP-375D | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9221389f-bb85-3c1d-aa1e-71aeea2a22c5 | -19.7159 | -56.82139 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 0338d087-7b1d-361d-b8ba-241f910df9cf | -19.60692 | -57.35767 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 419b666d-8bbe-3500-b672-1878d0640a11 | -19.70689 | -56.82354 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c1d3fa0d-e262-3302-a864-97836f09b01a | -20.30361 | -57.82043 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 729f0857-e586-3a57-a125-49df2b5128e1 | -19.72752 | -56.82796 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 1a917b6e-8f46-3a17-b131-5a68a56968f1 | -19.71927 | -56.82619 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 40adebb3-e69c-3dd7-a594-38914f2ca98f | -22.03657 | -49.50504 | 2026-01-27 04:42:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8469d974-48a0-3203-9b09-6d6e60152e92 | -20.20271 | -50.56744 | 2026-01-27 04:42:00 | NPP-375D | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b5c2fa4e-c27e-3e70-b06d-a90fb96916f5 | -19.60464 | -57.35969 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 78490a90-cccb-3478-8c7e-3489bda3f2f3 | -19.60859 | -57.34921 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| bb106bb1-7a08-3692-ba49-39965a62e256 | -19.69701 | -56.82318 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9f2d846a-f867-3c9e-90d2-8c71156136c1 | -19.69627 | -56.82711 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3c4d5f58-0a55-3429-a3b6-3be65a4f310c | -18.1612 | -51.12296 | 2026-01-27 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65dc4d42-1625-3ce9-94e8-f71250a4e22d | -23.05386 | -49.09596 | 2026-01-27 04:44:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f37f9832-2d7e-366a-abed-3bab6c28d2c9 | -27.52662 | -52.55863 | 2026-01-27 04:44:00 | NPP-375D | SÃO VALENTIM | RIO GRANDE DO SUL | Brasil | 4319703 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b200bf39-82e0-3320-b755-041720aa8d05 | -23.57115 | -51.54299 | 2026-01-27 04:44:00 | NPP-375D | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e2b682b2-7721-340e-a976-6f2995b5ca1f | -22.87447 | -54.65623 | 2026-01-27 04:44:00 | NPP-375D | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3f83a762-3aec-31ed-8927-b52dd2a84c6c | -27.09743 | -50.5288 | 2026-01-27 04:44:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9cb9934e-8e0e-3d4a-b6fc-8f4400a67b55 | -23.34895 | -52.20209 | 2026-01-27 04:44:00 | NPP-375D | SÃO JORGE DO IVAÍ | PARANÁ | Brasil | 4125308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 25b557b4-c948-345e-8adc-25d9730bc0ff | -27.76336 | -50.38429 | 2026-01-27 04:44:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 89d730d4-67ab-378e-879d-8ccf4c28ae37 | -23.59982 | -48.33597 | 2026-01-27 04:44:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 194c36e5-d280-37e0-a313-111ce192bf06 | -22.87094 | -54.65552 | 2026-01-27 04:44:00 | NPP-375D | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a7a2d261-db53-33ca-adeb-2aad6b5eeea0 | -22.8394 | -48.64813 | 2026-01-27 04:44:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 13768525-4996-32c8-9454-72665246cd1f | -23.59919 | -48.34071 | 2026-01-27 04:44:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a651cf2d-f9dc-3452-b9ac-013120c5be17 | -22.83879 | -48.65257 | 2026-01-27 04:44:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9f8e531b-6ae3-3b5f-b9c3-9ba0953afac0 | -27.62563 | -50.44799 | 2026-01-27 04:44:00 | NPP-375D | CORREIA PINTO | SANTA CATARINA | Brasil | 4204558 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c0fe02ba-e80c-374a-b4f9-a016244a5ec7 | -23.1925 | -51.89046 | 2026-01-27 04:44:00 | NPP-375D | ÂNGULO | PARANÁ | Brasil | 4101150 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d209ed8a-386b-323a-aa8c-a6f567cdb16e | -23.9832 | -47.51123 | 2026-01-27 04:44:00 | NPP-375D | TAPIRAÍ | SÃO PAULO | Brasil | 3553500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c35a0c0c-85d5-3374-89df-2a240a3fb500 | -22.84361 | -48.64433 | 2026-01-27 04:44:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 359f26dc-7ae5-37b2-a8cd-6e1d5f34b220 | -23.00895 | -52.38779 | 2026-01-27 04:44:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 359f971e-d563-350d-946a-1592ccbe2f2e | -22.84001 | -48.64369 | 2026-01-27 04:44:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3c4599ee-456f-362f-8679-5e63f4e7d19a | -22.73491 | -49.34392 | 2026-01-27 04:44:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8033cc2d-c839-318d-8bc3-65e7f0de1ec9 | -23.34835 | -52.20586 | 2026-01-27 04:44:00 | NPP-375D | SÃO JORGE DO IVAÍ | PARANÁ | Brasil | 4125308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 89b8d018-e16e-36a0-b15a-3055efe1d14c | -19.7246 | -56.8198 | 2026-01-27 04:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 55.9 |
| ca3e2a1e-6811-3438-a9b9-c524895be125 | -19.7045 | -56.8226 | 2026-01-27 04:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 77c51912-febe-36d5-a471-7611ee1a9120 | 2.96313 | -60.88565 | 2026-01-27 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7625581-c374-3ec9-86e5-b55e51f26cbc | 2.96267 | -60.88254 | 2026-01-27 04:55:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8256f58-559b-319f-870c-7887a02363da | -11.60311 | -42.06244 | 2026-01-27 04:59:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 017bc860-4365-338a-9f15-749e4cb8ff59 | -11.60277 | -42.06066 | 2026-01-27 04:59:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3e906486-ebee-3635-8b96-a85795c24fac | -10.34927 | -44.83073 | 2026-01-27 04:59:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b736e6d-af1f-3cb0-9094-8d067adeb6be | -11.60976 | -42.06115 | 2026-01-27 04:59:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1e009384-43bd-319b-a889-6ecbf7529bc5 | -12.35104 | -47.89965 | 2026-01-27 04:59:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4087299a-064b-3ae5-88d2-a971a80b4776 | -10.3435 | -44.82994 | 2026-01-27 04:59:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eca8bdcd-4978-3ebc-a746-19bae1eab960 | -11.40115 | -48.44035 | 2026-01-27 04:59:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2d8d787-4b2f-3212-9dc3-538240610dc8 | -10.40889 | -44.64047 | 2026-01-27 04:59:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da6d3a73-166f-3e08-b5d0-9d0f08f3bffc | -19.7246 | -56.8198 | 2026-01-27 05:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 55.2 |
| eb5cb02c-0387-300a-8437-5dea7cacf236 | -19.71651 | -56.82566 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| bfc884c4-3f6f-3172-b08f-d96bf7c3c605 | -19.60917 | -57.3605 | 2026-01-27 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 39a7e850-7de9-3150-aeca-5a4936aa297d | -19.671 | -56.83295 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5bcd3bc8-f426-34e1-8a56-dc1251e96670 | -20.16083 | -50.61248 | 2026-01-27 05:01:00 | NOAA-20 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 11c8e850-c255-333e-a9cd-70415f1a1e4e | -19.60701 | -57.35261 | 2026-01-27 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 989bce82-5987-38d1-8f00-fa8309d064be | -19.4664 | -55.44742 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| b2de4305-d755-3676-98dd-65f457ecd856 | -19.71043 | -56.82083 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a2916928-1897-3fb9-84dc-44e283a2294c | -19.66322 | -56.83917 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 380c084c-b712-3bb9-a064-e6251f5e9b73 | -19.70986 | -56.82451 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 631c71f2-7780-38b5-8369-1a04262ba422 | -19.66378 | -56.83549 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a7480caa-e34b-3511-b44b-4d040f0e8fe2 | -19.46298 | -55.44687 | 2026-01-27 05:01:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |


[Clique aqui para ver as próximas entradas](README4.md)
