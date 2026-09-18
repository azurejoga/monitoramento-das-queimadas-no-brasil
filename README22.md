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
| fc07d8dc-50f7-3d84-8f5c-d772eb85d9f5 | -5.7569 | -45.084 | 2026-09-18 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 3c65765d-26ca-379e-826d-9d654ae68f92 | -2.6125 | -54.7577 | 2026-09-18 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 04413e8a-79c8-3339-b9e3-f218b6efe572 | -19.1806 | -48.7946 | 2026-09-18 03:00:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 149.0 |
| af2567a8-3079-3f4d-936f-97eacd1e2117 | -12.5497 | -50.7332 | 2026-09-18 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| f4209719-62dc-35f6-a849-68bba2325e8e | -12.3015 | -50.7417 | 2026-09-18 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| f7b41a96-ba0c-3010-9e18-4663a676abfc | -19.1812 | -48.7717 | 2026-09-18 03:00:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 239.7 |
| 5e9f56f5-e25e-3bb5-a6df-805d0e72c442 | -9.7177 | -54.8162 | 2026-09-18 03:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 116.1 |
| c09a3129-e112-358d-87e5-b519359ec4fc | -4.5772 | -42.9746 | 2026-09-18 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 2d66d81d-bade-3e65-a4f2-084eea8187c2 | -12.3782 | -50.7111 | 2026-09-18 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 1ad066d0-c1b2-365e-8af9-5e2ff9b52d51 | -2.8101 | -50.4658 | 2026-09-18 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 81c7d1b6-729d-36ec-80af-e7cb52b8a067 | -13.2252 | -42.3414 | 2026-09-18 03:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 92.7 |
| cf479984-d8de-316e-a48a-828b8d14ee20 | -4.5587 | -42.9523 | 2026-09-18 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| bb132744-8d84-3a1b-8616-b548ed991f8f | -12.5688 | -50.7308 | 2026-09-18 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 8fc15473-5ddc-38d1-ab50-beb8b0e473d0 | -6.5174 | -49.8944 | 2026-09-18 03:00:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 8e86dfe4-dd2a-3fcd-b130-f7317726decc | -11.6798 | -54.446 | 2026-09-18 03:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 6adfd95f-9af8-3acd-87f4-fe48d58f3afc | -8.9108 | -62.391 | 2026-09-18 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ae453781-faab-3189-9cbc-1781392eef8f | -3.0465 | -51.3755 | 2026-09-18 03:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4468ef8b-f265-309d-91b9-408bc813c9d6 | -8.8922 | -62.4107 | 2026-09-18 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 806e62e7-696b-38ff-b95c-eca1945a4801 | -2.8285 | -50.4653 | 2026-09-18 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 00218d66-c088-39a0-b1f7-1cb94ca6541c | -12.3786 | -50.6897 | 2026-09-18 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 3e0bd3c8-5744-316d-86c9-a1d21f9c9016 | -3.3638 | -50.4492 | 2026-09-18 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 14edd9b7-de82-3281-bb6e-66c770fe22ce | -13.2446 | -42.3377 | 2026-09-18 03:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 127.9 |
| 67cdd5c4-013a-34d2-a987-831dd67ff3aa | -12.3206 | -50.7394 | 2026-09-18 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| e896771b-d43b-3eac-b222-3e767c74c51a | -2.81 | -50.4868 | 2026-09-18 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ab077233-a730-3364-9352-76f9f2bbc741 | -9.699 | -54.8176 | 2026-09-18 03:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 396695ce-85d1-38f9-a5ac-3f3275df5fa9 | -3.028 | -51.376 | 2026-09-18 03:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| e4da3c9d-0e27-30b4-bb41-83bc9b415bdc | -18.4667 | -49.3001 | 2026-09-18 03:00:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 34766094-7f4e-3ab0-b411-0e1266d4169d | -13.2257 | -42.317 | 2026-09-18 03:00:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 102.8 |
| d6458831-d4bf-33f6-8175-bd6192be1354 | -2.5941 | -54.7581 | 2026-09-18 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 13cfef8a-5773-365b-88d4-4fb95aa47f93 | -9.7179 | -54.796 | 2026-09-18 03:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| d850197d-54ff-3e06-9d9e-92663f9922b1 | -8.9107 | -62.41 | 2026-09-18 03:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 81924b09-586f-3f49-872a-0684bc245860 | -12.3397 | -50.7371 | 2026-09-18 03:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| c125455e-905c-382f-9462-02a8169ba1df | -4.5961 | -42.95 | 2026-09-18 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 62b91966-b41e-3438-a9d4-fd2f78587e20 | -4.596 | -42.9734 | 2026-09-18 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 1e36f59c-99f7-3af5-b458-fa138b56c720 | -11.6798 | -54.446 | 2026-09-18 03:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| eff04aa2-b29a-3cda-b96f-b12a2d686533 | -9.699 | -54.8176 | 2026-09-18 03:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 17e9544f-2f1a-3cad-8048-6835d946bea9 | -3.3823 | -50.4486 | 2026-09-18 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| e51b0745-4041-344f-ac20-23488719a79b | -4.596 | -42.9734 | 2026-09-18 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 6b6dc7c7-3a81-31c3-a9c7-151f185de0be | -2.8101 | -50.4658 | 2026-09-18 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| ff7ed419-95cc-3660-8662-ca499bf32e10 | -6.5174 | -49.8944 | 2026-09-18 03:10:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 9fdb24bb-96f5-3473-8ae8-346154709fd1 | -4.5774 | -42.9512 | 2026-09-18 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 05118435-c871-3b95-83ba-bb9070e5a1e7 | -9.7179 | -54.796 | 2026-09-18 03:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 1ddec744-0fc0-30b1-961b-d6a1f5fb3257 | -11.6609 | -54.4478 | 2026-09-18 03:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 895cc06f-40f8-35ae-b6fc-870f108b2aec | -4.5961 | -42.95 | 2026-09-18 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| ff6f466f-37b4-39f1-ae56-d0521a6b7ae6 | -19.1812 | -48.7717 | 2026-09-18 03:10:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 239.0 |
| 6f378605-90a7-3886-90a6-e5f5186653c0 | -19.1806 | -48.7946 | 2026-09-18 03:10:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 47c5d076-79bd-3338-8af2-d6ec7aee16c0 | -10.6536 | -50.4778 | 2026-09-18 03:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 598af0fd-8960-39aa-9f1d-b1579f1e8a0d | -19.2015 | -48.7675 | 2026-09-18 03:10:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 09f3aaba-89d9-3090-815a-e7f6969f5030 | -13.2446 | -42.3377 | 2026-09-18 03:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 139.0 |
| 7376f9d1-67e7-3774-a12f-0ea71c70cd3d | -12.3206 | -50.7394 | 2026-09-18 03:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 71f00386-a085-375d-9eda-cac77753bef6 | -19.2009 | -48.7904 | 2026-09-18 03:10:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 6f1c337e-565e-3b0a-8748-5e2ffc7147a1 | -13.2257 | -42.317 | 2026-09-18 03:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 1d553cea-f513-3cc8-9e30-62aa9c888049 | -4.5772 | -42.9746 | 2026-09-18 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| e76dbee5-8b79-3fd5-898c-96f510213d2b | -5.7569 | -45.084 | 2026-09-18 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| b381f648-bb43-30b6-8f92-d6f1523b0f4a | -2.81 | -50.4868 | 2026-09-18 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 0a3691e0-0ebd-3f70-9be0-198efeb07a73 | -12.3015 | -50.7417 | 2026-09-18 03:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 80f15cc5-be4c-3218-8c79-765bd413b92a | -3.3638 | -50.4492 | 2026-09-18 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f64207f7-4d79-3870-b381-9cf6fe5383c3 | -13.2451 | -42.3133 | 2026-09-18 03:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 134.3 |
| 6a631887-d26b-3509-81e1-917869b72b8a | -13.2252 | -42.3414 | 2026-09-18 03:10:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 7b60aada-9248-3c8a-ba37-c4c67d749baf | -2.6125 | -54.7577 | 2026-09-18 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 2523d55a-40ec-31e2-914f-df4742126b7a | -4.5587 | -42.9523 | 2026-09-18 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| d1552bbd-9ef1-311b-80ba-0d8a53fb442e | -2.8284 | -50.4863 | 2026-09-18 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 89cf77e6-b925-3a15-8fd9-8f8b61b2a641 | -2.8285 | -50.4653 | 2026-09-18 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| b94b4ac0-cb31-38c7-b743-5ff964ab0637 | -9.7177 | -54.8162 | 2026-09-18 03:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 8c8bb4be-0ec2-3864-bba2-3557607f2783 | -13.22 | -42.32 | 2026-09-18 03:15:00 | MSG-03 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d8460daf-6547-3f87-885c-7555ccb45e2d | -19.17 | -48.78 | 2026-09-18 03:15:00 | MSG-03 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a9aef870-a986-3c4b-aa2f-8436601ba3fd | -8.0799 | -37.68786 | 2026-09-18 03:15:00 | NPP-375D | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 855d391a-5534-3d22-b7a1-d055e7f3646e | -7.28878 | -38.95938 | 2026-09-18 03:15:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 14c9d509-78be-3f67-9f5a-eea8c1589a54 | -7.29546 | -38.9613 | 2026-09-18 03:15:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7224f8c7-46e3-3aae-8af5-e80db6e59df1 | -7.29333 | -38.9671 | 2026-09-18 03:15:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e658ad75-b429-3acc-9fb0-8555b7e5fb33 | -7.35344 | -38.99197 | 2026-09-18 03:15:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d41b2d05-da2f-30ec-a665-b7f5e82bd7bd | -7.28662 | -38.96526 | 2026-09-18 03:15:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 512b8044-515b-3a8b-8209-be51adc32bee | -7.28754 | -38.96582 | 2026-09-18 03:15:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 21cb0c5f-448a-3ffe-875a-8885fa30001c | -7.35304 | -38.99212 | 2026-09-18 03:15:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 64ae8749-af33-38b9-a4a7-51f248539da6 | -7.35425 | -38.98569 | 2026-09-18 03:15:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 285e7682-f879-37de-be81-79bc1ab099a4 | -7.29424 | -38.96766 | 2026-09-18 03:15:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1cfcb1e9-3c6e-370b-843c-fe79aa949a99 | -7.29451 | -38.96073 | 2026-09-18 03:15:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7208b2a7-1fe5-3233-8a82-d7ac7ed7a685 | -13.2451 | -42.3133 | 2026-09-18 03:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 123.6 |
| 33cc42bf-2e7f-3f95-8895-3c49fa7ec739 | -19.2009 | -48.7904 | 2026-09-18 03:20:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 9a7d1d9f-6fce-316a-9d4c-79c9876d526b | -8.8922 | -62.4107 | 2026-09-18 03:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 5c8ba5e4-c5db-3c4e-9fb5-6d8b375e5cce | -10.6536 | -50.4778 | 2026-09-18 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| c21ab104-5bd8-3b03-941f-510a30d21607 | -12.3206 | -50.7394 | 2026-09-18 03:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| fd5276ab-24f6-356e-9471-77adc283977b | -3.3638 | -50.4492 | 2026-09-18 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 4a9980e8-b5bf-38b5-a3c2-7722754203bf | -8.8921 | -62.4297 | 2026-09-18 03:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| f6673f49-5b7d-3508-a9d6-bceb6d33f3c3 | -8.9107 | -62.41 | 2026-09-18 03:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 09bd65fd-28eb-33a8-be3b-59f7de95d3b3 | -2.8101 | -50.4658 | 2026-09-18 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 7e6b355c-5caf-3593-a8f5-ed4b026bec88 | -13.2257 | -42.317 | 2026-09-18 03:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 1f26bcb1-76c8-3440-ac43-b52700985ec8 | -19.1812 | -48.7717 | 2026-09-18 03:20:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 221.7 |
| a61f84ea-9bd8-31b6-9b74-1a5790896e84 | -13.2252 | -42.3414 | 2026-09-18 03:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 89.1 |
| 0c054443-fc3e-3759-bc98-f4210e3b0bc5 | -2.8284 | -50.4863 | 2026-09-18 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 9c82bd05-99c0-3391-a9c5-67d62ac5bc49 | -9.7179 | -54.796 | 2026-09-18 03:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| acd3f233-63e8-3f85-aec0-d5d5cb2de26c | -11.6609 | -54.4478 | 2026-09-18 03:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| be74b399-e937-3fb5-b279-69bb9ccbd60c | -11.6798 | -54.446 | 2026-09-18 03:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| c9d991a1-ab77-3b81-ae17-f3b436e8175f | -2.8285 | -50.4653 | 2026-09-18 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 1c365179-e164-3cf0-b0ba-5d8d0e663a4e | -9.699 | -54.8176 | 2026-09-18 03:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| bb1e710f-4870-37fe-8032-520ec15ef076 | -12.3015 | -50.7417 | 2026-09-18 03:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 7b2c064a-4fc8-32d8-b33e-b0b4e99e3f8b | -19.2015 | -48.7675 | 2026-09-18 03:20:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 94.2 |
| bed83cd9-1fd5-37e7-9983-0baf70f97497 | -2.81 | -50.4868 | 2026-09-18 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| bb3582fe-275d-3ce7-b03d-49d1e3e65787 | -13.2446 | -42.3377 | 2026-09-18 03:20:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 149.7 |
| 0d893fa3-1252-30b1-a617-16d8e63db015 | -12.5497 | -50.7332 | 2026-09-18 03:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |


[Clique aqui para ver as próximas entradas](README23.md)
