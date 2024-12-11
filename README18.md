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
| d6841c98-aeca-3a17-b380-13abdbefdf6a | -12.55814 | -58.3633 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 262ce23c-ccbc-3442-bcf9-931e1a77d418 | -11.36255 | -57.7998 | 2024-12-11 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cf7b2c9-1f43-3413-90ea-24570fd1e716 | -11.04569 | -44.57279 | 2024-12-11 04:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e4f3abe-ece5-36d0-83d3-f9698ac4866d | -12.53548 | -58.34281 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bde191ea-05da-3d7a-a54f-4fe43502fb44 | -15.15988 | -56.47467 | 2024-12-11 04:36:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39ce4e4f-5534-3776-bf5f-60cad2c7045b | -12.85611 | -43.81859 | 2024-12-11 04:36:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3857328a-d4f0-32bb-8417-ebd1cab28dc4 | -9.71694 | -54.89008 | 2024-12-11 04:36:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7fb2318d-fd3c-390c-80cf-68bc7c27d960 | -12.54635 | -58.34161 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2a5f3a86-4a32-3bba-b1f8-8c0ba66a6056 | -14.18643 | -40.54787 | 2024-12-11 04:36:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| e86bed8e-5264-3c51-a0d8-246d79934ba4 | -12.84665 | -59.03037 | 2024-12-11 04:36:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbbac3b0-72fb-3bea-95b7-ca6e096b9f42 | -12.55026 | -58.34891 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b03e83fb-e9c0-3002-bf99-0dfca8b25d57 | -12.54275 | -58.36028 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6d34dc67-cf3b-351e-9e85-0b25cf56d19b | -12.54729 | -58.36437 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 79276971-a9dd-3ce7-80b3-113cb7ddc20a | -11.72491 | -57.44069 | 2024-12-11 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac9d7554-b42f-3fe5-aa77-a67645f25657 | -12.54848 | -58.35815 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 01b346be-cdd0-31dc-a8b9-550f1a961ba2 | -15.06525 | -44.08949 | 2024-12-11 04:36:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cdc76d5c-1d6f-34aa-9ebc-2c244b436ee6 | -10.0277 | -53.74799 | 2024-12-11 04:36:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea3adaec-41e6-3409-8a0e-7fa278a32fb8 | -12.55361 | -58.35918 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5707e9a4-4848-3a3f-85b4-11b47a3c61fd | -11.36311 | -57.79679 | 2024-12-11 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af927982-f90e-30d8-9725-f222624af77c | -12.56368 | -57.76379 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dd8491dd-a1c1-3b38-9fd3-6dcfcf83e0a1 | -11.76118 | -44.86846 | 2024-12-11 04:36:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f765efd5-4e8e-3256-96ca-bef7b77fa641 | -12.56385 | -58.36131 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 517ceb5b-f1da-3dde-a090-dd3c9651ea7e | -12.53745 | -57.73352 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39128f0a-65b6-3079-a262-b2ebb6f6d543 | -16.35089 | -43.69538 | 2024-12-11 04:36:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5faa45ae-3a2e-321b-a722-eaf9fbc4c022 | -12.53843 | -57.73535 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a5d0984b-a554-3c17-af70-0e2e6e58ffe9 | -12.53487 | -58.34596 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1d6e7f11-1010-3006-aaa4-c490d141d394 | -12.54789 | -58.36123 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 486b8bee-683e-37d4-9652-9518ac029657 | -11.11639 | -54.64416 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7237edee-f4e5-3446-9fa3-05046de5c859 | -12.55419 | -58.35614 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b9c2232e-bc22-3091-a0ae-77361f41bc4e | -11.45116 | -48.00693 | 2024-12-11 04:36:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3baa5553-dae6-3e01-99d3-c828d63185c9 | -12.70826 | -54.97227 | 2024-12-11 04:36:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cae107a9-8960-3a7b-a764-c5850d861889 | -11.78105 | -55.12704 | 2024-12-11 04:36:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2eeb893c-5c5c-3b19-8d20-778b51a67d72 | -11.10471 | -54.63811 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b1821d7-a179-35c4-9794-d22b9d7d3fd9 | -10.03166 | -53.74865 | 2024-12-11 04:36:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a84fdda0-82f2-3152-a34e-fe995c6fc16e | -12.54183 | -58.33747 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 703af8a9-1b8d-3408-b7c8-db7ae4e3a387 | -11.72337 | -57.43861 | 2024-12-11 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82de5b9c-7431-337b-abf6-84dc0e9ed69f | -11.46541 | -44.96006 | 2024-12-11 04:36:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e106e647-5c54-31b6-ad97-ac5220ddc4c4 | -12.56861 | -57.76473 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ef85db3-5958-31d7-974c-e5248b113400 | -11.12116 | -54.64112 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9251c5b1-f3de-3e8b-9f7a-e07be5c1e003 | -12.53638 | -58.36567 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6ab45a0a-e2a6-39d8-8a6e-428ee51b9da1 | -11.1458 | -54.23155 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75503d26-95cc-3932-885b-739b2f105fa7 | -11.11769 | -54.6366 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 00cacfe0-efce-3d5d-be8f-e1222bdd8fa1 | -11.09495 | -54.62104 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39182bd0-d39e-3aef-9513-d270e87d9d19 | -11.3687 | -57.79491 | 2024-12-11 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b057fe7-7f77-3806-a752-89e87e322faf | -11.36814 | -57.7979 | 2024-12-11 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d202efc1-3c2e-3dff-ab90-a91777d38b43 | -14.57406 | -56.71386 | 2024-12-11 04:36:00 | NOAA-21 | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c4e81f4-485a-35e5-a75a-743e3423558a | -13.25397 | -41.34204 | 2024-12-11 04:36:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c667f1d5-8d59-3824-b8f4-7658540c522a | -12.71152 | -54.97242 | 2024-12-11 04:36:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 688af295-36cf-3bf1-be12-4d7f8134cfe6 | -11.09906 | -54.62173 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4070b435-552c-3a60-836f-ca91a7ce471e | -12.55145 | -58.34274 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 302488e3-0ec5-3711-a8dc-88aa4c85f77f | -9.71623 | -54.89415 | 2024-12-11 04:36:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae674a58-03a5-3e20-b9ab-98bdc7534c35 | -11.10947 | -54.6351 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d872a050-0335-3819-8491-b5cec0325d12 | -11.11358 | -54.63585 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a615a001-c5b9-3934-b8eb-6b6145545a10 | -12.54132 | -57.74022 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c109a1be-dca4-3ae9-bb3e-9491e571694a | -12.71085 | -54.97613 | 2024-12-11 04:36:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d47c67de-2f38-3443-9eec-0491fa58a662 | -15.08677 | -59.64222 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20af1c28-da39-3ef9-a608-81853313d34e | -15.96547 | -57.16626 | 2024-12-11 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e72799cb-1595-366c-834a-c227b46604be | -15.08883 | -59.64251 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2f5db53-fb0d-31d3-9791-358b5be664af | -17.47377 | -47.02161 | 2024-12-11 04:38:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90ba66de-4dd2-3f04-a006-676c2f758092 | -17.47744 | -47.02222 | 2024-12-11 04:38:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 368ff6e8-b2d0-3bb3-ba10-b8b3c08d5f4d | -15.0849 | -59.63436 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f293273-961b-3b5c-bb3d-b97844957029 | -15.08535 | -59.64917 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 91461b87-dfa0-30f6-a7b6-b0248caf8166 | -17.74113 | -54.21498 | 2024-12-11 04:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d02e8cc6-2aed-372e-ba97-92bc111dc4ca | -17.74119 | -56.32479 | 2024-12-11 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 677f0a7a-eeff-383a-adea-bddab968ead5 | -15.08352 | -59.64135 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1ac93f5-8626-307a-94b5-ab08ffe293b0 | -15.08217 | -59.63762 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a0f53e0-054b-3681-81c1-798ebadfae9b | -15.08606 | -59.6457 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 730da759-7cc0-32b5-98f4-94ee685b54ac | -15.08749 | -59.63873 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae5fece6-da84-3cd3-8ddc-3cff97bf4c6c | -17.74511 | -54.21466 | 2024-12-11 04:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e15d70b5-ceab-3dfb-93bc-402dc287d590 | -17.47438 | -47.01709 | 2024-12-11 04:38:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd94c6cc-08be-3227-970c-8e532859021c | -15.08952 | -59.63901 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c1942ba-174e-3761-9606-fbd369d3cb63 | -15.08746 | -59.64949 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dc8e92a4-d039-3ad3-8c98-508855a33aa3 | -15.96993 | -57.16715 | 2024-12-11 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a83fcf9-64cd-3616-8d89-cf89638fc9bf | -15.06944 | -59.65648 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f5bda291-b1cc-3f4e-b31f-c2325941592f | -15.08284 | -59.64483 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| da7237b1-3da4-3b41-98d5-f71a4cdd5e8f | -15.08815 | -59.646 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e49da357-b60c-3874-ad39-8e5c30841d4b | -15.96633 | -57.16168 | 2024-12-11 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea3a3e18-e603-3721-b9cf-b2eee83d9ac3 | -17.74146 | -54.21404 | 2024-12-11 04:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ae5997c-e3e6-302c-bc11-c64f58c0a51d | -15.07933 | -59.65145 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 089ae62f-fbad-3f0d-927e-d4cc0ff94eff | -15.09278 | -59.65064 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c93a55cd-ee1f-34d6-8dbb-2b7f1a7ecb6e | -15.08147 | -59.65178 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96722bd6-59ae-36a6-a0b2-4cda7d0a448d | -18.5005 | -55.13358 | 2024-12-11 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 255627fa-8fd4-38e4-a93c-c41ed1dbc0bb | -18.53053 | -55.95253 | 2024-12-11 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 81673d01-d0df-3c70-bee8-d8f41e6a9973 | -15.07862 | -59.65493 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a4a8ee0b-ccfb-3f63-bcf2-ee7b2d93f039 | -15.09021 | -59.63552 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f62e1309-3d8c-3752-a416-8898135fafe8 | -18.02014 | -53.9982 | 2024-12-11 04:38:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4038cbae-7e77-3d3e-8f55-c61418e22ae3 | -20.79138 | -49.19105 | 2024-12-11 04:38:00 | NOAA-21 | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| be9e988e-08b9-3ff2-9dd3-9676d388c7bb | -15.09598 | -59.65144 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aadae068-2352-3efb-815d-d7f8c83bd841 | -15.09137 | -59.64683 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7229fa8b-9173-3504-b127-f35f761a11b7 | -15.07477 | -59.6576 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7bf48003-aad9-349a-8398-54fd06aba6f9 | -15.07615 | -59.65063 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| be8f5e9f-a851-339c-9c39-e46c9e4511f5 | -17.74189 | -54.21056 | 2024-12-11 04:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0df71eba-820c-3f31-bed9-ec37ed0c31b8 | -15.08078 | -59.65526 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e67200a-0785-3745-a4d2-f06c71f40057 | -15.08146 | -59.64108 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efa66a2e-a8c1-3913-b77c-a48384749bf6 | -15.97439 | -57.16804 | 2024-12-11 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 35295637-c597-372d-944a-fb9953afde7a | -15.0882 | -59.63523 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7ade98a-b694-37ad-97cf-a8cc96676d26 | -15.08421 | -59.63786 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7767f86f-69a4-3b4a-adc5-56f3a407866b | -15.09346 | -59.64716 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc7191e4-481b-3fde-8612-51e65d58aa6f | -15.09066 | -59.65031 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f81a1004-f938-39e0-8fe8-be5c9fba9f77 | -15.07014 | -59.653 | 2024-12-11 04:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README19.md)
