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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 380d5133-9aba-3c92-a0f6-05ff0773110e | -15.60254 | -59.94098 | 2025-11-28 05:03:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28c219ec-ba97-3992-8ff3-2286dce0c54f | -16.06351 | -59.29501 | 2025-11-28 05:03:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dda2c7ed-88da-34cc-a2f3-5d31414152d6 | -10.27972 | -60.53421 | 2025-11-28 05:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d087de86-7ffc-3cd1-98ce-1b41a810d228 | -9.93669 | -60.7173 | 2025-11-28 05:03:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| facf18e9-e9f7-3d1c-9509-4b33d43d1b1b | -16.05644 | -59.29359 | 2025-11-28 05:03:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fc835cd-e323-3964-9b57-93d691baa7c1 | -15.60332 | -59.93655 | 2025-11-28 05:03:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 482da91e-6b99-3772-a63d-2155f8ff7efe | -16.06071 | -59.29005 | 2025-11-28 05:03:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2bf3765-97b2-3f98-ac5a-fe57c67b2627 | -9.94089 | -60.71803 | 2025-11-28 05:03:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf3d9f04-5cd0-3a30-b469-36b952456744 | -16.19469 | -59.33176 | 2025-11-28 05:03:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b556ee4-1b75-3ecc-ac45-70fefbab62bd | -14.74356 | -60.12733 | 2025-11-28 05:03:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aedac322-3aeb-3bb9-91f3-cc026938707e | -16.138 | -59.96276 | 2025-11-28 05:03:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94f0bf80-daea-34df-bb96-0096c8f906e9 | -16.14243 | -59.95905 | 2025-11-28 05:03:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3b72b74-cf30-3447-8316-246fdcafb753 | -16.09802 | -59.76323 | 2025-11-28 05:03:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c32365a9-b534-3c2d-9406-70c18538e106 | -16.18955 | -53.77989 | 2025-11-28 05:03:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6c15c56-cabd-39ff-84b8-ee20dc86349a | -12.28701 | -64.41103 | 2025-11-28 05:03:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a961b61-e687-39bb-82cc-3100a7096dd6 | -12.28353 | -64.40913 | 2025-11-28 05:03:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 488fdf40-9d6d-3946-a14a-20f791625c8c | -16.14531 | -59.96412 | 2025-11-28 05:03:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2c7c1a7-a0d6-3fb7-b490-80178f1cdee5 | -10.28157 | -60.53359 | 2025-11-28 05:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01c37eb4-b203-358e-84fa-4ad3704eb872 | -21.65195 | -48.62437 | 2025-11-28 05:05:00 | NPP-375D | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed9bb438-c1a7-3bce-84b5-b628335c9418 | -21.64742 | -48.61716 | 2025-11-28 05:05:00 | NPP-375D | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62769556-daf8-3fd5-920d-62495900e0c6 | -21.75667 | -49.03154 | 2025-11-28 05:05:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 185ca49a-879d-39a5-93f6-b8cfacda106f | -21.44277 | -54.56722 | 2025-11-28 05:05:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9412df28-d1d5-3a2e-aefe-1b2d7c2c7aa4 | -20.37865 | -57.94736 | 2025-11-28 05:05:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 382b92f3-bcef-3ef5-a1c5-04b666809595 | -23.02703 | -47.49231 | 2025-11-28 05:05:00 | NPP-375D | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d998d8e7-3b96-351b-bc86-14ce321d00bb | -19.98871 | -49.98865 | 2025-11-28 05:05:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 683cce2b-ce6f-3851-9b45-f4f76d20ae8a | -21.44217 | -54.57163 | 2025-11-28 05:05:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1feb0370-3b07-3ed0-bae4-df4fdd8731af | -20.46034 | -47.47622 | 2025-11-28 05:05:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b74767d5-781e-3af0-bc42-e47334a12411 | -20.38138 | -57.95166 | 2025-11-28 05:05:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| b6af58fc-a661-390b-81f5-cae1378446c9 | -18.15422 | -54.562 | 2025-11-28 05:05:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c672c600-e421-307e-bc1a-fe7597b69e87 | -23.96127 | -49.76829 | 2025-11-28 05:05:00 | NPP-375D | WENCESLAU BRAZ | PARANÁ | Brasil | 4128500 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 93eba87d-9b5a-3b18-9eb8-dd41f80d19c2 | -22.1954 | -56.00858 | 2025-11-28 05:05:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8da92473-be50-30f9-bb21-c78a6ad847d3 | -20.42371 | -57.9441 | 2025-11-28 05:05:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| ac72a3d9-1319-3470-b6dd-45a05ea63afd | -21.65228 | -48.62116 | 2025-11-28 05:05:00 | NPP-375D | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a4022e5-b4f2-3988-baaa-fbcd538a5d7d | -19.98406 | -49.98801 | 2025-11-28 05:05:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e2cab06b-b5cb-3f77-8f02-f9bef90257ec | -21.65261 | -48.61789 | 2025-11-28 05:05:00 | NPP-375D | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d06036c9-f2a7-35bc-a8da-01fd1e770a04 | -20.38198 | -57.94797 | 2025-11-28 05:05:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| bbe33661-3670-3c48-b376-685f0681de07 | -20.46581 | -47.47523 | 2025-11-28 05:05:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4c55b31-f3ae-31f3-8187-3c961741a8d1 | -22.47871 | -49.12509 | 2025-11-28 05:05:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f1ea8ff-c0c6-34af-8f53-c18b25a4b70e | -20.47319 | -55.6004 | 2025-11-28 05:05:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 099aa44e-199d-38f9-92b7-c82223103a19 | -20.43429 | -57.94221 | 2025-11-28 05:05:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 02314f24-bd53-3813-897f-de32c5e6ba4a | -21.44938 | -54.57274 | 2025-11-28 05:05:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bbf8c21-01b0-307d-b61b-932ce487a96f | -20.46976 | -55.59986 | 2025-11-28 05:05:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df42856f-bb3f-3790-a497-952ad14f96ed | -19.98814 | -49.99363 | 2025-11-28 05:05:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 44f3ea58-0f2d-3467-93b1-b871e6791d8d | -21.69112 | -47.95745 | 2025-11-28 05:05:00 | NPP-375D | AMÉRICO BRASILIENSE | SÃO PAULO | Brasil | 3501707 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d27d2d70-db3b-34b1-a80e-c0483372783e | -20.43096 | -57.94161 | 2025-11-28 05:05:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 904cb8db-3c42-3357-9959-15a176fed385 | -22.96106 | -48.69256 | 2025-11-28 05:05:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ddddba99-e172-303e-a971-e83f4e9959b6 | -21.75157 | -49.03109 | 2025-11-28 05:05:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eba06d0d-97fa-387f-8b91-aca3d5f06f9b | -19.98349 | -49.99299 | 2025-11-28 05:05:00 | NPP-375D | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f6c103ff-7df6-339a-abaa-eca874bc6b95 | -21.08564 | -56.12123 | 2025-11-28 05:05:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79bfffc2-c1cd-3591-8345-bc577c3d4ab7 | -20.42704 | -57.9447 | 2025-11-28 05:05:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 965a14ce-88f6-3790-a479-43d0045c74ba | -20.43762 | -57.94281 | 2025-11-28 05:05:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d91f9b43-6f2b-3f05-ba53-1fe8aa175d5e | -22.47395 | -49.12127 | 2025-11-28 05:05:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac35b8e0-eff4-3369-9126-03499393df94 | -20.40552 | -57.92941 | 2025-11-28 05:05:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1c7b3c88-3df2-341f-8511-3ff729ad804e | -20.46544 | -47.47908 | 2025-11-28 05:05:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 729dc54e-899a-3664-86fd-7bd004a2ad51 | -21.68602 | -47.95336 | 2025-11-28 05:05:00 | NPP-375D | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0038ad27-7031-38dc-98fc-86f6088e62f6 | -23.02137 | -47.49154 | 2025-11-28 05:05:00 | NPP-375D | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 99bbc2af-7db9-3d46-8376-90cadfd233a7 | -21.69146 | -47.95391 | 2025-11-28 05:05:00 | NPP-375D | AMÉRICO BRASILIENSE | SÃO PAULO | Brasil | 3501707 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c021e52e-997c-35cb-8084-eeb9686c5ee1 | -22.19197 | -56.00798 | 2025-11-28 05:05:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7d72c32-6507-3e51-8713-46087a665f88 | -22.47903 | -49.12195 | 2025-11-28 05:05:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7c4a84a-903e-30b7-8c82-15baf49a79bf | -18.15771 | -54.56253 | 2025-11-28 05:05:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc9942b6-434f-381b-ad2d-b9f0a8b55f80 | -22.19483 | -56.01251 | 2025-11-28 05:05:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c597bd36-757e-39cb-a6b6-89e3d1b3038e | -21.68567 | -47.95693 | 2025-11-28 05:05:00 | NPP-375D | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ec5ac43-648c-3ba1-8c00-993be25d913f | -22.74735 | -52.13976 | 2025-11-28 05:05:00 | NPP-375D | PARANACITY | PARANÁ | Brasil | 4118105 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6aa7a0a5-251d-3cc5-8874-ccb1e41f61e7 | -20.46028 | -47.4747 | 2025-11-28 05:05:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea842445-62ad-349e-8bd0-e5182b6365c3 | -27.37938 | -51.39888 | 2025-11-28 05:08:00 | NPP-375D | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0a33a179-9a97-3d33-a984-47f19d87523e | -27.13778 | -51.20772 | 2025-11-28 05:08:00 | NPP-375D | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cef4a6b7-25e0-3bbe-bf91-fee21afd2181 | -27.38408 | -51.3993 | 2025-11-28 05:08:00 | NPP-375D | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8b3e700c-f70e-3af2-b81f-89dae8a28b9e | -30.48997 | -52.51593 | 2025-11-28 05:08:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 8298e082-a643-3313-8aee-97791922ccb1 | 4.02538 | -60.7985 | 2025-11-28 05:20:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2aefed2e-ea97-3b9a-9936-7cf6523c4db1 | 3.51786 | -51.4669 | 2025-11-28 05:20:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f92eef6c-0555-3b15-911d-2b5c4650b925 | 2.87214 | -60.26067 | 2025-11-28 05:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2a78dda5-6eb0-374b-b6dc-34bf1c2e4027 | 2.87271 | -60.26432 | 2025-11-28 05:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 46980932-22ed-3df9-9cac-0c242c4dd8e4 | 2.87554 | -60.26014 | 2025-11-28 05:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d226958-1d29-38cf-93a2-d310ad7dab80 | 4.02187 | -60.79896 | 2025-11-28 05:20:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7aa3a715-7389-34a7-b01a-f45eea91586f | 0.46412 | -60.44909 | 2025-11-28 05:22:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 27ec07ab-5e18-34e0-8b1b-0f489092826b | -1.6211 | -54.71247 | 2025-11-28 05:22:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95a40ae6-52ef-38f3-8978-7168e4a2450e | -3.03419 | -50.97798 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb3110fd-beb0-3026-93ce-0a753954927b | -1.36211 | -55.44123 | 2025-11-28 05:22:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65c8fc55-5326-3c27-8e5d-58f05803f94e | -3.83098 | -50.18938 | 2025-11-28 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37ccc3ee-0420-3525-a9d3-47e35f43a0a4 | -2.89704 | -54.00533 | 2025-11-28 05:22:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e711222-aaf5-3529-9114-98b89c5e4586 | -3.2253 | -50.32404 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 60ce6620-cdea-3282-8910-1ea7d95fdef2 | -3.22585 | -50.32045 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bef439b7-53a6-3f8f-b263-cf16801cec6b | -2.5659 | -54.76171 | 2025-11-28 05:22:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 66a0732a-ec05-3cbe-8ade-fa7c98aa2585 | -1.34621 | -55.44366 | 2025-11-28 05:22:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81b02249-beb1-3d41-a508-9e169ff93e9d | -3.06083 | -50.36821 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ebb7a52-2579-3f0e-97b1-39e9e4355167 | -3.02894 | -50.97716 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5ea210f-7fe9-3dba-a9d8-08913815aa02 | -3.38162 | -51.50248 | 2025-11-28 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f60836e1-b1e5-3654-a90f-25666cd1f85c | -2.36985 | -56.11499 | 2025-11-28 05:22:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 304876c0-c491-3384-9ae4-4ea673f4b734 | -4.29875 | -55.61539 | 2025-11-28 05:22:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7cb64ab0-b97a-3fa7-8ceb-2eaf3c5f84da | -3.22644 | -50.31627 | 2025-11-28 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4912d955-00d1-3e1e-98ab-8ab28acb2cb2 | -3.68057 | -51.69616 | 2025-11-28 05:22:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8ebd7e3-2708-34b6-a77b-6d56ec9d2200 | -3.1712 | -48.60713 | 2025-11-28 05:22:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8bd04be-bb56-3240-943f-eeda80670ed7 | -2.74193 | -54.5956 | 2025-11-28 05:22:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e5562dc4-0345-3c11-99c5-887a63329c52 | -3.75891 | -46.9608 | 2025-11-28 05:22:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d0c179b7-2ff0-33c6-9e79-efb7981a8b44 | -2.37756 | -53.92123 | 2025-11-28 05:22:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 798d715e-a914-3b51-845b-90faaa959518 | -1.64521 | -52.03997 | 2025-11-28 05:22:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65a9bc29-1171-343d-a917-d0893485072e | -1.8746 | -60.12336 | 2025-11-28 05:22:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4365d511-c5f0-3506-917f-4eb5037c2c81 | -3.41085 | -53.30541 | 2025-11-28 05:22:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9b60a5a-64b1-364b-b4d1-c14bd739079b | -3.75799 | -46.96693 | 2025-11-28 05:22:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4e938cac-1579-3054-ac8b-72bbd873eda3 | -3.75952 | -46.96118 | 2025-11-28 05:22:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |


[Clique aqui para ver as próximas entradas](README21.md)
