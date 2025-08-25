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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bc4c2c1-f269-390f-87e7-30bb75b6d0c8 | -19.91826 | -44.62622 | 2025-08-25 04:44:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1c974c91-918f-33b0-9f8c-5a00d33eb042 | -20.01353 | -42.8495 | 2025-08-25 04:44:00 | NPP-375D | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e7141e98-f3c9-345d-bbc4-cc5758ebbbb0 | -21.63271 | -44.01447 | 2025-08-25 04:44:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 1b7aced1-cdfd-3a91-9742-864117a0d188 | -20.45746 | -47.41259 | 2025-08-25 04:44:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 91d42290-595b-39fd-8ab0-a5446dd44f9a | -20.37488 | -46.75943 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d78656b4-9bb3-371f-bc4c-9dfc0867e26d | -17.57871 | -48.73343 | 2025-08-25 04:44:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca4afe4c-69b0-38b1-8405-d47a9ea5ee86 | -14.26848 | -48.03497 | 2025-08-25 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02637db3-6727-34cc-9fdb-61b263b9d906 | -14.23321 | -58.62311 | 2025-08-25 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9dff59d4-2e7c-3a4d-abbe-01223e8ced45 | -14.38667 | -51.94629 | 2025-08-25 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e868e049-86b9-3850-ab65-f74b3a68ed30 | -14.09636 | -53.99025 | 2025-08-25 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d7751b9b-5f58-3b2e-aa4f-62ab83861760 | -15.14288 | -59.58977 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4525e4f5-adb3-340c-9ab3-52a8d47cccde | -14.20718 | -58.62742 | 2025-08-25 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8556adfe-6789-3255-a1cf-a786a1bcc6c1 | -20.29731 | -47.18235 | 2025-08-25 04:44:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 790ed00d-9e9d-3748-a5af-adb418912b90 | -19.36451 | -44.21645 | 2025-08-25 04:44:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf59be05-8a6e-3836-a7d5-b1cae8d7d4d9 | -12.99923 | -56.8979 | 2025-08-25 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2b86e9a-bea6-379f-8f3e-1dad371420da | -14.37446 | -51.9368 | 2025-08-25 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3902eb56-020a-3b1b-91e1-1a72fc1bae4c | -14.30527 | -60.37273 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0093af9b-8705-3429-b2f4-5b5998494b4a | -20.98551 | -45.48498 | 2025-08-25 04:44:00 | NPP-375D | AGUANIL | MINAS GERAIS | Brasil | 3100807 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f6f84f63-bde3-3d3f-bb5c-795fe7e7c991 | -15.08823 | -48.68238 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9c5277f-cae8-32c5-89e8-9ab834c58bd1 | -15.06884 | -48.66679 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ae83e11-f081-3f39-b3ef-ac43fc13095c | -21.27934 | -42.81531 | 2025-08-25 04:44:00 | NPP-375D | DONA EUSÉBIA | MINAS GERAIS | Brasil | 3122900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c4e50a6d-9ebe-321d-9fef-c9d4d616abf6 | -14.78753 | -45.38816 | 2025-08-25 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b369eb60-36ca-3ef6-9577-2f5f8ddf40ee | -19.93258 | -47.49395 | 2025-08-25 04:44:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 640593b5-bebd-3a19-ada3-02f0c8c86890 | -20.72964 | -49.42364 | 2025-08-25 04:44:00 | NPP-375D | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d60bcb7-2b90-3e2a-9bc3-cf72d4ccde40 | -19.73225 | -49.01537 | 2025-08-25 04:44:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b093d7d2-5575-3841-8ad4-ac070a03de07 | -14.64859 | -56.57001 | 2025-08-25 04:44:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a23b45cc-1ed7-39c8-a7db-75924e087369 | -14.10706 | -53.9921 | 2025-08-25 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af78135f-b43b-33c5-b509-a9b82a95ce1d | -20.04626 | -44.48198 | 2025-08-25 04:44:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2dcd4e80-a4e3-3aa1-a190-737424251acc | -14.09992 | -53.99087 | 2025-08-25 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7b2f9454-0885-3fd5-96d6-87310d881159 | -14.69885 | -54.68374 | 2025-08-25 04:44:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c389b42-e1e1-396a-a403-43febdd2cfed | -19.94419 | -50.44504 | 2025-08-25 04:44:00 | NPP-375D | POPULINA | SÃO PAULO | Brasil | 3540408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f10c81cc-2276-3bca-a631-f8d8dfbc48a1 | -14.33579 | -51.96354 | 2025-08-25 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e6d47c0-0a3c-30c0-81a4-e842229c3ebc | -14.47843 | -52.05069 | 2025-08-25 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| baa7d8ea-82ac-39b9-82c9-afdf384aa8a6 | -14.77766 | -48.21748 | 2025-08-25 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b39f621-3b72-349b-90d0-bb6e3fdc2a23 | -14.20872 | -58.62369 | 2025-08-25 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6eee862-50f7-372d-abd9-8262f1ffed64 | -20.3763 | -46.74788 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87f43f85-9c94-3480-b20d-68918590015c | -14.24827 | -58.62081 | 2025-08-25 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48973015-af9d-3061-b1d3-f0f651c32d35 | -17.92423 | -46.07062 | 2025-08-25 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 312432da-6787-3af9-bbb5-2eb2ee18739e | -14.27982 | -60.3712 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adad9e48-9b92-3923-953f-e9247a522a03 | -16.23565 | -48.14786 | 2025-08-25 04:44:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 741d82d6-4b6e-35df-b89b-40b83be02c81 | -21.63206 | -44.02088 | 2025-08-25 04:44:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| c99fa589-658c-3ff4-ac3a-45122ea7ba1b | -14.38391 | -51.94212 | 2025-08-25 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb31d7aa-6d8c-3709-bdd9-788e9a6c942c | -21.41448 | -47.59856 | 2025-08-25 04:44:00 | NPP-375D | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edb0f15f-3c38-3f19-bfec-b1964177957a | -14.97216 | -50.11129 | 2025-08-25 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a3f424f-9890-312e-bc46-e01715b148ad | -15.03628 | -48.52563 | 2025-08-25 04:44:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3bcfa32-4098-3ef8-9cdb-8f45022d3a44 | -20.37392 | -46.76723 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 325883dd-ad54-3bf2-bfdc-a94e575e7a35 | -14.2379 | -58.62405 | 2025-08-25 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f24a6e48-2dc0-30bb-a396-72f667546c83 | -20.27266 | -46.64929 | 2025-08-25 04:44:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a38bab14-0881-34f3-a62a-b407e45236df | -14.26897 | -58.61438 | 2025-08-25 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5674b747-aac7-33d5-a5e0-7970d11166da | -20.36233 | -46.72248 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0235ab8b-ab34-33bd-9316-686a81908334 | -17.91893 | -46.07833 | 2025-08-25 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40d6d33c-a683-3fb3-b7d9-b23c69a413a6 | -15.62416 | -52.70218 | 2025-08-25 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b1f897f-10b2-332f-9bbf-4710b28b0cc9 | -14.92266 | -45.53098 | 2025-08-25 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62c2e4d7-ffd5-366a-bf94-e22e8c26b22f | -16.71166 | -49.08507 | 2025-08-25 04:44:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6bb88c63-04b7-3c8d-b4da-cae6e0bcb6ce | -14.27917 | -60.37455 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b7658f7-17cd-3d97-b3b6-f196b7a2a758 | -14.38783 | -51.93908 | 2025-08-25 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a2706a4-5660-36fd-8d8e-2d0814f21752 | -14.29993 | -60.37209 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28444283-e3e2-3c3b-a6ec-1cb79278a845 | -14.38725 | -51.94268 | 2025-08-25 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65e4e21b-87a2-3a8c-9feb-be38aaf2162c | -21.42257 | -47.59957 | 2025-08-25 04:44:00 | NPP-375D | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19bb248f-8423-3fdc-a149-9ca7c1f8b47a | -15.09463 | -48.71254 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebf26a63-a2cd-3b72-9e2f-17a7534eeec0 | -13.00352 | -56.89864 | 2025-08-25 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f831a68c-cb9b-3ba2-b7e2-872213a539de | -17.57706 | -48.48247 | 2025-08-25 04:44:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a97879d8-dc3f-3359-b018-3bbbb88acfa0 | -18.44783 | -47.55399 | 2025-08-25 04:44:00 | NPP-375D | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8085391-6b91-3b1a-b8ca-3d65cf52b6ef | -15.64414 | -52.72836 | 2025-08-25 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee08bef3-f698-3ea3-a144-c0c8cc414d31 | -19.36653 | -44.22024 | 2025-08-25 04:44:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 903aee47-c736-3015-8369-7aaa872b32aa | -16.41686 | -49.93624 | 2025-08-25 04:44:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47fe1f04-f61b-3717-8ea1-3304e52ceee1 | -17.9184 | -46.08244 | 2025-08-25 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e347329-4d52-379e-b93b-41d79ca2fc6c | -21.72701 | -46.81293 | 2025-08-25 04:44:00 | NPP-375D | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4ea88b53-2305-3ca3-a5c6-5f39c6216ade | -14.75856 | -55.93597 | 2025-08-25 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 511fa4fa-6c76-325e-a195-b7d634976cc7 | -17.83825 | -44.41196 | 2025-08-25 04:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f446f0fb-4bd5-3556-b702-7cfe9b7e2065 | -12.07406 | -63.15127 | 2025-08-25 04:44:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b3421357-4d2e-3ffe-850d-bef3bae05a1c | -14.79109 | -47.93888 | 2025-08-25 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee965dfc-510a-3861-af37-50c45573c6b6 | -20.61248 | -45.02673 | 2025-08-25 04:44:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 229fe2b8-2941-3f3d-a599-c0becb07755b | -15.63859 | -52.71986 | 2025-08-25 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0943bf67-63f7-32f7-b1d8-48b9a623289c | -19.94117 | -47.4902 | 2025-08-25 04:44:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc0398cf-8205-35b0-8dab-48edbc9853a0 | -22.17991 | -46.62683 | 2025-08-25 04:44:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8999d79f-b2f4-38f3-b695-f86f39bacc03 | -19.72652 | -46.46992 | 2025-08-25 04:44:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb2c7a8a-b1e7-3741-9cb6-b4b108f3fbd6 | -18.38909 | -46.83744 | 2025-08-25 04:44:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6333ccc6-2e10-3ec3-ba33-e2248fa3be72 | -17.59398 | -46.1048 | 2025-08-25 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e90bed45-db9a-35b9-b536-e27869d7d4b5 | -14.24358 | -58.61987 | 2025-08-25 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa89dfb8-22d4-3887-8768-876e8242bf56 | -19.6448 | -46.09941 | 2025-08-25 04:44:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db94457b-eb67-30ca-bd15-80d7182e74b3 | -16.48612 | -46.76033 | 2025-08-25 04:44:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c30eceb9-8927-3e98-a33e-f946b041a112 | -15.08123 | -48.65614 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9f8b85ed-373a-3829-9e19-8a165a6a1bb6 | -15.15159 | -59.59755 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a3d9fd2-df07-34fc-ad81-04ad466b1f93 | -15.98278 | -48.06905 | 2025-08-25 04:44:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c75ccac5-5432-3d9f-8983-baeef7bb5878 | -14.65203 | -56.57433 | 2025-08-25 04:44:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6df6c3c9-16ba-3306-bc13-16940f9bffc9 | -20.0475 | -44.4711 | 2025-08-25 04:44:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d8f3aaaa-c1a3-37d6-8896-0ef66a2f842e | -13.00498 | -56.89048 | 2025-08-25 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9325d37-9359-3380-8510-56408919f696 | -19.93655 | -47.49462 | 2025-08-25 04:44:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3418344-b3db-3abe-b441-7952faedb412 | -21.72323 | -46.80829 | 2025-08-25 04:44:00 | NPP-375D | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1778b2ff-83db-327d-b30d-37e319040f5d | -14.10993 | -53.99682 | 2025-08-25 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c9ad741-0864-3692-96b5-2295edbd44af | -15.13837 | -48.63654 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9092061-d7d9-3a0d-8a70-37a0e5e4bd0a | -17.57832 | -45.38931 | 2025-08-25 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ca110d9-91ed-33c2-805f-bdbcba240975 | -15.17694 | -48.19939 | 2025-08-25 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0c53430-384b-33e2-9feb-a864f57a0acd | -20.0139 | -42.846 | 2025-08-25 04:44:00 | NPP-375D | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b7a48288-18e5-3449-8968-908bb77235bd | -14.26009 | -48.04211 | 2025-08-25 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95b41597-faa0-3d2e-bec2-0e4e7720b106 | -13.0007 | -56.88971 | 2025-08-25 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30b3bcec-3aa9-38e0-909c-0c7011d51f55 | -19.94476 | -50.44109 | 2025-08-25 04:44:00 | NPP-375D | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d5f8f9d2-5274-34ca-8de9-0002c295a7e5 | -13.34744 | -54.39001 | 2025-08-25 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad9bb7bc-a70e-3732-8cb1-1e3d9dfb249d | -15.08063 | -48.66026 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README55.md)
