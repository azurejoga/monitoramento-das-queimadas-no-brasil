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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e447c4a-8a2d-3f47-ae62-376d007041ad | -17.73516 | -57.49672 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a8327281-e289-3c36-9d2f-fb1a644aff4b | -17.73433 | -57.50132 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 17932fb1-29e6-3352-b8f4-4385bc7b0840 | -17.73376 | -57.49413 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bd97c07a-dff2-3f3f-b0bb-793b7f89dd55 | -17.73296 | -57.49872 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 37d9c057-4c32-3bd7-aaa6-3afddb65a37c | -17.72347 | -57.48737 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 5d3aca4a-b7d5-3a57-8c78-ae833e7e4123 | -17.71978 | -57.48665 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 96a5684f-d430-330d-99bb-7f4c39f7bda9 | -17.83735 | -57.55669 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 8faba70b-37b4-3c8a-881b-519bbad81d76 | -17.71897 | -57.49125 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 727ea47f-1006-354b-b496-ffabc08cf500 | -17.70049 | -57.48765 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 85870ebc-aa1a-3069-8fe7-7ca0c8ab0f8f | -17.6968 | -57.48693 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 4a128a59-ee45-3e67-86b4-58634ef9cc65 | -17.69391 | -57.48162 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e178f04c-dfb5-3478-b4b8-ce2ead07edac | -17.69022 | -57.4809 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 302f33ba-5c9c-3518-b426-08c26f6d1bac | -17.6894 | -57.48551 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 257ee252-d34a-3108-9183-0630c5b5bb21 | -17.68657 | -57.32947 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 93e02eaf-6381-3a4c-86c8-266903feb9e9 | -17.68652 | -57.48019 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 639e36f2-f4ec-3486-bb29-24002844ad03 | -17.68588 | -57.37616 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bcbbdb54-08c7-3717-86c2-aac136f878ee | -17.68571 | -57.48479 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| fc68ebb7-2079-3cfc-a4d8-5766af4ffb5f | -17.68283 | -57.47947 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| ccbd8e68-bfef-3fa2-8259-0306c6bb3a9e | -17.68201 | -57.48407 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 86d7b2a2-e713-3d4c-b0e8-621a47bfad1b | -17.6812 | -57.48866 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 2d9baf1f-401e-306e-8515-26395d818b6e | -17.67913 | -57.47876 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 22b6d316-f811-32d5-99ed-fa89d06d446a | -17.67832 | -57.48336 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b622651c-1aa1-32d5-bde7-7d8682a4efd3 | -17.6775 | -57.48795 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 4efee2eb-056e-3768-98fa-6cbcc40ccd8e | -17.67462 | -57.48264 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6991118c-5d65-363d-9fbc-f5d2920b2db0 | -17.6738 | -57.48724 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| a4b8f397-7450-341d-858f-afae9089608b | -17.66805 | -57.4766 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8ea18d1b-7239-3c27-8661-789ed570d2f3 | -17.66641 | -57.4858 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.6 |
| 6992d312-1f40-38d9-b9f4-ba0edad3c183 | -17.66598 | -57.46671 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b165ee07-bf0c-32eb-a608-07496bac4bdb | -17.66517 | -57.47129 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ad2dabe7-7676-32ea-8434-c45e1c6d09fb | -17.66353 | -57.48048 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 88720a70-8975-3b81-a70a-e5997e262bbc | -17.66271 | -57.48508 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 17257eb9-bb1b-3b09-8ee0-51b55aae0259 | -17.93351 | -57.5538 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 14ba95f2-a6d9-39fb-959c-9f4e26c44292 | -17.93116 | -57.56724 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| e094409d-e226-354a-beb0-eab58ab3d986 | -17.93055 | -57.54894 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 7c4f5f49-75aa-3780-b16e-d874029d9261 | -17.85598 | -57.60248 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.4 |
| c0786664-20c1-38ac-8e88-e2afb33c2b32 | -17.85049 | -57.61171 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 386b7867-b21c-3711-9552-8660776e3a42 | -17.93365 | -57.53129 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 157933f6-1d8f-37c8-bae1-724553fd418f | -17.93289 | -57.53561 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| d2691d4c-c82a-3af4-9c5d-54581a99d4c5 | -17.93212 | -57.54 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| d2aa9d21-5fc8-3c03-9672-741389f15021 | -17.92999 | -57.53036 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 47af2c33-fbe0-399e-9fb4-890b61f1dd65 | -17.92979 | -57.55326 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| ab4a8be1-bbe1-337c-a3e3-245a02f202e5 | -17.92664 | -57.57125 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| bddea48e-539f-3964-843a-91a2f3fc722e | -17.92633 | -57.52945 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| b306f211-8a8b-3577-926a-4a5c4e388830 | -17.92267 | -57.52854 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 8a9e9ecb-dd0b-3aab-868a-d10f4bd06126 | -17.91901 | -57.52762 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.4 |
| b9d2348c-3593-3f17-85b9-158a16080705 | -17.9164 | -57.56416 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 45b5e5ce-7210-32e7-ab60-94c93286a2c2 | -17.9109 | -57.53026 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 02f74de6-7fb8-330c-bfaa-3c71f8451987 | -17.90499 | -57.52051 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fb1525d4-8ce0-32e1-9024-c48132540c58 | -17.90129 | -57.51984 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c7ab7d69-771c-38d0-be01-a68f68fbb054 | -17.89891 | -57.53332 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| d895458e-b44b-3f83-bd32-d807d58a82a6 | -17.89519 | -57.53277 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0a080010-8bb1-3a49-9e54-c59fbdef36ad | -17.89227 | -57.52767 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| fcb167d2-71f1-30a3-8431-f067a86ce127 | -17.89147 | -57.53222 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 325c7528-f955-355f-bc6f-cc4a86e330f2 | -17.87067 | -57.52023 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0f64bb0c-d3f9-3a32-a218-d904e53f313c | -17.86697 | -57.51956 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c0fa76e7-bac3-39ca-852a-3b480d43616e | -17.84273 | -57.54811 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| c95aa9a7-eb02-3884-8fb6-098fbd8c645b | -17.84221 | -57.61497 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 0d5440e8-84b7-3ceb-b087-fd93bc589df5 | -17.83901 | -57.5475 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.8 |
| d4c9544c-882b-3673-8996-28a0a997e13d | -17.83591 | -57.55441 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 9f1b50f4-46e0-31f7-9f05-d4db27e9fa33 | -17.8109 | -57.58785 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 1f2d7c2d-5736-37ab-b599-60527309bf7c | -17.80846 | -57.60177 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| c9a0a9b5-3ed2-3876-92d2-fe8d045ccb4e | -17.81773 | -57.52703 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4bd42a28-d0a0-3340-882b-e04f72c535f2 | -17.81323 | -57.53092 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 4f8b0753-ca49-3223-8abd-25507f57d7cc | -17.80953 | -57.5302 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f6b10e4d-9835-3403-8fe8-3f248b52d915 | -17.80826 | -57.51568 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 84cb3cb6-e8d9-384d-a0ba-7d263cc06ba9 | -17.80385 | -57.56253 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| de2a969c-0ed3-38e1-b1ac-4e7cfc452340 | -17.7899 | -57.59816 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| b172ea53-b4fd-301b-9400-0d5b231e125b | -17.77787 | -57.51452 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| efd7d8f5-48e2-385d-a1ab-94bac1ab0580 | -17.75404 | -57.51943 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9bd7aa23-e3f0-31bc-9a5f-b7e72d5dca60 | -17.75322 | -57.52403 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 014b86cd-c34a-3f8d-a417-c60a7074cf2d | -17.75239 | -57.52863 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b4ba5cc8-d993-3462-aa22-86d341d2417e | -17.75157 | -57.53325 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0e37f5aa-1782-3fe8-9c29-51e52b378668 | -17.75117 | -57.51411 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 5fd063bb-f515-36db-8a4f-7746631165cf | -17.74869 | -57.52792 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| c289e711-6130-3446-aeec-e12a95183785 | -17.74787 | -57.53253 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 642dd0ad-4616-37b1-8eb0-4098a8be8b03 | -17.74621 | -57.54176 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 10970018-0a93-3bb1-bd59-88fe8664abfb | -17.74582 | -57.5226 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 845f3b51-ded9-319a-b87e-41c6971acbfe | -17.74539 | -57.54637 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8405f09a-fd83-386f-a878-7d8675a0d121 | -17.74499 | -57.5272 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 3aaaca58-8738-3f25-8663-12d3b056c0a5 | -17.74417 | -57.53181 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| f9e5f84d-eb15-3092-a314-4837d279c108 | -17.74334 | -57.53642 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| cd854b45-7d69-3a97-9732-d09ef69a483e | -17.74294 | -57.51728 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7e054a31-119a-35be-a031-dd6b4dca6644 | -17.74165 | -57.51472 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c6584f8b-214f-3f34-a9ad-cf2bd9ee7484 | -17.74129 | -57.52648 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| dc0a2ab9-e9eb-3e5d-aad0-2e755bea44b5 | -17.74046 | -57.53109 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 596e4f1a-91f0-39f0-a290-e5f7e215c94f | -17.73964 | -57.53569 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| cd751477-21fd-3577-8af1-f007244e275c | -17.73924 | -57.51657 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4823ceee-3ba8-3381-a9b8-622f3f3926aa | -17.73795 | -57.51399 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2cc71567-3bfb-3467-b5ae-a0cb2dc5b5f2 | -17.73715 | -57.51861 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| d5bac8a7-53d3-3d3c-9ef9-20191c78ae7a | -17.73555 | -57.51584 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 43715291-0904-3f0f-a518-e0e12e4bf520 | -17.73465 | -57.56342 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 22948d69-e553-3232-b938-f7e3f9137fad | -17.73362 | -57.56095 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 68ffbd07-8ebd-3ca6-bb41-64804370c98d | -16.89254 | -56.75252 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3e027600-2a08-3363-aea5-5641aa4019b6 | -17.85226 | -57.60178 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 2dad9ada-31a4-3e58-b481-bbb30b0e4e25 | -16.88968 | -56.74752 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e2804179-7cd1-3dc7-8c26-14c0d9b5146c | -16.74895 | -56.67381 | 2024-10-26 04:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4997cbaa-1965-3dcd-9c87-15b8a4104465 | -17.9468 | -57.5542 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 759331d9-bff7-3cee-b3f3-a2f06c7b80a5 | -17.94607 | -57.54759 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 97c36ab4-fcd4-3041-a43a-d31e6771bb9e | -17.94596 | -57.55887 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 9631d887-801e-3eeb-89df-a62f5fa9689a | -17.94535 | -57.55171 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.7 |


[Clique aqui para ver as próximas entradas](README88.md)
