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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6dbcc4b4-3867-3475-b03a-31314d923885 | -8.13876 | -64.10653 | 2026-08-09 05:48:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d3a2130-eea9-31d7-abdc-aef93500ba81 | -6.85534 | -56.40144 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5f8461e8-b14a-3315-a581-c898f5744862 | -8.67699 | -62.87471 | 2026-08-09 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 98602597-a806-3afe-9503-c2ba23d8342f | -11.79297 | -51.8131 | 2026-08-09 05:48:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 53d88b4e-9d9e-36d9-a26c-3a25d30b1b18 | -8.15534 | -64.08777 | 2026-08-09 05:48:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19521535-144f-3414-816b-7c14c056462c | -6.72081 | -58.93401 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95df327b-0911-3fc6-a862-56df5a0a929b | -9.90609 | -67.0081 | 2026-08-09 05:48:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c91ae3d6-a5e6-364e-83c7-fcd59c877310 | -12.33304 | -53.15364 | 2026-08-09 05:48:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a94bdebe-48de-3f56-8282-78b6783c8816 | -6.8457 | -56.40017 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 19bdca8f-1b0e-3a91-bf6d-76ee48389023 | -6.71112 | -58.9434 | 2026-08-09 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 786ef441-b30d-37ce-8ce5-c22f57944220 | -6.84266 | -56.42113 | 2026-08-09 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 87d1e7c9-242e-3fdd-a9d2-af6da64f11d6 | -14.08899 | -53.99853 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95ae97d1-74c9-3db7-bd49-0911e720c42e | -14.04922 | -53.84465 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 973be72c-1a8d-35f9-92ef-aab51c7ff9f0 | -14.07024 | -53.82754 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 01ab9a68-3027-3935-a0bc-f4b9350faee0 | -14.0819 | -53.99074 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7f2187c-d2e3-3932-82d3-7f25f6e53aca | -13.94653 | -58.114 | 2026-08-09 05:50:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b140c723-a5cc-3f2c-8924-94613de3fb4c | -14.08755 | -53.99693 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32cfe6fe-0009-31f5-a393-6a1dab6abccb | -14.17428 | -53.98793 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e00d2890-44a8-39cd-9187-5ac6ba16544c | -14.02517 | -53.83157 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ba84c3aa-916f-3d53-ab34-6db2ef6f25b4 | -14.09071 | -53.9835 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a38120a7-cc39-3f0f-b246-810a5a568ebd | -14.15538 | -54.01158 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebffe2ce-d5d3-388a-8864-cf48cf65409a | -14.31931 | -54.93026 | 2026-08-09 05:50:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48a41eac-1bfc-3bde-b930-9ae6b72b6fc4 | -14.04294 | -53.84381 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 36a2bf45-8649-366b-afc3-cdac93b0899d | -14.17374 | -53.993 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea118e65-bada-3ef3-9b4b-0f1515417580 | -14.02463 | -53.83653 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e660a353-4cd7-3f14-ac21-e1f219a53569 | -14.31056 | -54.95516 | 2026-08-09 05:50:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4a57b2c-25e5-3840-b969-e361e178f2df | -14.85937 | -60.06285 | 2026-08-09 05:50:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f99f44e5-f161-353c-9e46-2e98b4d8c920 | -14.17021 | -53.99198 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d81554e3-2300-3fb2-a0d9-99a85a70da53 | -13.93638 | -58.118 | 2026-08-09 05:50:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ee95c0cc-e730-3bb0-9bbe-82e82f040f7c | -15.3642 | -53.77739 | 2026-08-09 05:50:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a7662c3-1e42-30fc-88e4-af4dbfe5a2bd | -14.04403 | -53.83397 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f756de8d-6973-3084-b0b0-cb9cbd3a3c23 | -14.16696 | -53.99735 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ec962f4-30f1-36c3-8783-f4d56c3f5720 | -14.01783 | -53.84047 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3b65a7e-4edf-3f3e-a784-46d4aae9e58b | -13.94179 | -58.11335 | 2026-08-09 05:50:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ec5498a2-a40f-3dd8-9386-521a2991830a | -14.08337 | -53.99252 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49a5b8ce-6141-3767-8209-b87b3066cfdb | -14.07133 | -53.81773 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fd4a760-07aa-3a6c-9234-66517356ffb8 | -14.0845 | -53.98259 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aff85600-7365-3438-af1c-b7b028ef527f | -13.93572 | -58.12326 | 2026-08-09 05:50:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f67e71d0-630b-33d5-bf04-77806f674897 | -14.01945 | -53.82553 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f126a33-0a11-3150-8937-529c70f14c01 | -14.84569 | -60.06896 | 2026-08-09 05:50:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5080973-c75c-3ea7-adbf-b10f9aa116a4 | -14.07079 | -53.82265 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ea321ad-3bc6-3fb9-9467-b2db7bbd328e | -14.16106 | -54.01719 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c497e431-e8d4-3392-86b4-43e7f9b02cd7 | -14.85042 | -60.06559 | 2026-08-09 05:50:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb8b48ab-c3c1-39a6-9f56-6ef8375770ea | -13.93032 | -58.12787 | 2026-08-09 05:50:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be88fab8-f705-38cb-a554-68955fee925b | -14.02983 | -53.84723 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| be60f974-149c-366f-a9ed-471c09029c86 | -14.03037 | -53.84232 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 58b3e649-29a8-3dd4-87c0-95006086c844 | -14.08393 | -53.9876 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e2714ee-e744-3346-911a-2c66de3e70e6 | -14.02357 | -53.84631 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 29158fce-00f5-329a-8f4c-d5bc4d899ac2 | -14.04348 | -53.83891 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b5cdce67-2556-335f-af21-e037626c2e0d | -14.01891 | -53.83057 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26fdeabd-22ea-3f7f-86ba-0586345fdf99 | -15.37061 | -53.77812 | 2026-08-09 05:50:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 549799b5-ed67-375c-8b4a-e79ab35c5ba1 | -14.73872 | -56.33237 | 2026-08-09 05:50:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3361fd15-1dc1-3943-ab89-e1f519dd4a25 | -14.0503 | -53.83487 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a9db68f-6128-3ae1-896e-020f4b6e02c9 | -14.32028 | -54.92148 | 2026-08-09 05:50:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a3e6a9b-bfd5-33b9-ae4f-3aaf8fb4ccd3 | -14.01837 | -53.83554 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2153509c-d2ed-3f11-a5c1-96db972817b1 | -14.04976 | -53.83977 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 477bf144-40d1-3b9b-a30e-4bec7298a019 | -14.06969 | -53.83245 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1934cdfa-5062-3ac9-9459-2f932819257e | -13.93098 | -58.12266 | 2026-08-09 05:50:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1a576e00-a17b-3fd9-a572-73d6de5b3a23 | -14.15484 | -54.01641 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e943d117-b914-31c4-a540-095ad238c69b | -13.94113 | -58.11863 | 2026-08-09 05:50:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4d95d787-324a-30d2-84c0-41e54aabc065 | -20.45467 | -57.40179 | 2026-08-09 05:50:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ac672cfc-473d-3a54-8cd1-9a83391b3310 | -14.16751 | -53.99217 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca160964-afee-30c1-b7de-cff7be4fdbae | -14.16963 | -53.99711 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97bd855c-99f9-3907-9b53-a11b645e1f58 | -14.31979 | -54.92588 | 2026-08-09 05:50:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d080aa0-881d-34d4-8ab8-8e4ae7b87c1e | -15.70055 | -54.8354 | 2026-08-09 05:50:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee535237-2f02-353a-9f2e-36f89a5e511a | -20.45429 | -57.40543 | 2026-08-09 05:50:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 59be93f2-aad5-39fd-90ff-4af0bfbf6adb | -14.84621 | -60.06496 | 2026-08-09 05:50:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e063727-b1a3-3ced-8c6a-81f5cadc7d8a | -14.04867 | -53.84966 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3549cac-bce0-38c3-9b7b-0afc285244dc | -14.7383 | -56.33588 | 2026-08-09 05:50:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db10f743-7380-3cc3-9572-2e09171b66d4 | -14.0241 | -53.84142 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b68d5893-39bb-3841-9f20-af64ff83f7fc | -14.08243 | -53.9858 | 2026-08-09 05:50:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8df6f809-048f-3f58-b893-b6217c970c63 | -20.4601 | -57.4024 | 2026-08-09 05:53:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 16381ef3-9218-3c92-a540-da4fb84c1f17 | -22.29591 | -42.61037 | 2026-08-09 06:03:00 | AQUA_M-M | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| bb79bd95-dc86-34e8-ab9b-273ec80e0182 | -20.57368 | -41.921 | 2026-08-09 06:03:00 | AQUA_M-M | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 77120af0-57cc-34f1-bce1-7278e50eceee | -20.57527 | -41.91101 | 2026-08-09 06:03:00 | AQUA_M-M | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.8 |
| 8fc2bba3-1a6f-3d41-b8cb-d29a04a0f188 | -20.3764 | -41.99701 | 2026-08-09 06:03:00 | AQUA_M-M | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| b774cd2b-bbd8-3386-896a-90be0d7944f8 | -5.88546 | -57.64939 | 2026-08-09 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02f32ffc-229f-352a-88b9-ad39a7f87429 | -6.7058 | -58.95169 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85d06ae2-e0bf-31fc-a0c1-06484a356526 | -6.1452 | -57.72511 | 2026-08-09 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 36254f1c-99d5-3d56-b112-d9b539c9903a | -6.83293 | -58.92965 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 010e9cf4-315a-3c58-a9db-d95eb02dc1a1 | -6.71269 | -58.94734 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be9ace2f-b69e-3cb7-9095-22d5fb951f6a | -6.88864 | -58.93741 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34453012-4d0a-35f4-b137-6d59b3a6e4a3 | -6.144 | -57.72142 | 2026-08-09 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 144f91c0-412c-3f5d-ad37-8676334ac671 | -6.8756 | -58.94061 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ea5d45f-242c-36c1-9daf-cc339e8c4f0c | -6.8831 | -58.93174 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ea369ac-96fc-3e41-97d6-dfdd3a4e918f | -6.88862 | -59.89854 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cb23bf0-0410-3073-803f-3038e522b607 | -6.83785 | -58.94013 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a75f70c-9d7e-36b4-a3fc-57bcc339800d | -6.8893 | -58.93253 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bbbf9d7-b135-3f21-83f8-c920695604fe | -6.13853 | -57.72461 | 2026-08-09 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 14db1c74-f214-34c7-8005-6a6bc600c40c | -7.38742 | -59.97386 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35f5fce5-ac07-3ef6-be43-7e2f0193b946 | -7.55241 | -61.15976 | 2026-08-09 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7dae8744-84b5-3da7-acb4-9021089eb6ee | -6.81924 | -56.43538 | 2026-08-09 06:05:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a40abc7-f54a-3659-af51-b5990b7c3623 | -6.82544 | -56.44376 | 2026-08-09 06:05:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 309d9077-8dea-385c-a512-fbe86ab47d1d | -4.95758 | -62.3443 | 2026-08-09 06:05:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bd69402-2fdf-3c14-a433-642c5ec06ff1 | -6.88918 | -59.89446 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 897ac0d8-46cf-3f9b-a336-fc8d7ee72c0f | -6.13934 | -57.71875 | 2026-08-09 06:05:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5f44573c-08a0-322c-a95e-f89276a8d3e8 | -6.88181 | -58.94138 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6036943-fd12-3fb8-a356-097025e7c432 | -6.87498 | -58.9453 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70b1c6b6-2eb6-3e62-9c54-236cea27722a | -7.39329 | -59.97446 | 2026-08-09 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59731e24-a6ed-32aa-90d3-08ad8c4b680d | -6.82641 | -56.4364 | 2026-08-09 06:05:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README23.md)
