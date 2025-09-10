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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7182501f-1c19-3bf6-9c45-0a3c1c6cd136 | -15.05854 | -50.14631 | 2025-09-10 00:30:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 79171c4e-5087-3880-b152-aaef8be0dc88 | -12.18616 | -50.64795 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f0743fb7-8bda-3d05-b6d5-2726dcdee440 | -11.66435 | -46.90959 | 2025-09-10 00:30:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 71004d32-5414-37c4-9a43-87d0c686086d | -11.30077 | -46.4833 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 22488880-1f92-3912-9739-4a84a01d4adf | -11.54532 | -47.31405 | 2025-09-10 00:30:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4f934d04-6c70-382c-9d88-01c36843fc0d | -13.93123 | -48.26443 | 2025-09-10 00:30:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 65a20a7f-fd4d-3c19-b45c-045e84b86ae0 | -12.18467 | -50.63595 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 80a56dc3-89f9-3dab-9ea5-c07ca9e36dc7 | -14.4096 | -47.50909 | 2025-09-10 00:30:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5e2d8211-5e56-3a1f-87e1-dc492ee85c33 | -11.33646 | -46.54317 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 94e3c8e0-4952-370c-aa16-cf8cd1c5ef85 | -15.09319 | -50.09158 | 2025-09-10 00:30:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3c9fc32a-ca6c-3d21-87b1-7da5b9f1544e | -13.97266 | -48.2291 | 2025-09-10 00:30:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 54.3 |
| cddf1d05-a79b-32dc-8309-3ba7991cb90d | -13.97139 | -48.21964 | 2025-09-10 00:30:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5bb52ec7-90d3-30a0-b066-07810633aa5d | -13.14759 | -45.28122 | 2025-09-10 00:30:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 9e304608-39cb-3635-adec-5cf13ca92363 | -13.98118 | -46.66411 | 2025-09-10 00:30:00 | TERRA_M-M | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 770482bd-e899-305e-8286-c45a97f987c2 | -13.64715 | -46.97778 | 2025-09-10 00:30:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e23f97a0-b21e-3659-a4dc-91f0097ddcc8 | -14.55591 | -48.74979 | 2025-09-10 00:30:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5377d09c-2a48-36b6-8590-0453eb85c8c9 | -15.02249 | -50.09495 | 2025-09-10 00:30:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c125558f-8ccc-3067-aa58-93b910f647be | -14.426 | -48.45926 | 2025-09-10 00:30:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9761acd8-4894-357f-89fb-d9084ce29120 | -11.53651 | -47.31534 | 2025-09-10 00:30:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 67fa9ac1-3e83-3a01-b3c8-7fbfa661b88c | -11.94656 | -51.08035 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5d69deb7-615c-3907-9c76-edb6c8ed6259 | -11.57131 | -44.66906 | 2025-09-10 00:30:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 583d446f-d205-35cb-b914-e593ccb8d469 | -14.91269 | -50.11511 | 2025-09-10 00:30:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 537b30c0-d53c-3038-b06d-5e760364b051 | -11.32114 | -46.49886 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f0664919-bee4-3fca-9967-391434c8a8f4 | -12.67726 | -44.96062 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9932a2a5-cf17-3f65-9aac-ac894fdf3c39 | -12.9275 | -54.75778 | 2025-09-10 00:30:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 9036788e-201a-3b09-90de-d27675252e70 | -11.95271 | -46.65842 | 2025-09-10 00:30:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fef4c78d-151f-394b-aeef-4c922924c2a6 | -13.17686 | -47.24941 | 2025-09-10 00:30:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3e610d94-e752-3cb2-8dfb-1c502d8c8cd2 | -14.31802 | -47.31397 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 204117e4-abdc-3118-a494-c84d671421a9 | -10.59685 | -43.29493 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| d7f4794b-2e52-38f6-b57f-de0926e33653 | -14.4247 | -48.44938 | 2025-09-10 00:30:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bb4b3325-1935-366e-a23e-3aac92f3f1af | -13.54071 | -44.13421 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 9585cc43-95a0-39d4-8a4a-40548391264a | -15.09158 | -50.07855 | 2025-09-10 00:30:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 31c92a86-5761-35f8-8683-dd2b93555ffa | -15.05703 | -50.13375 | 2025-09-10 00:30:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 97464676-28b3-3c22-bf79-3d2c3f056920 | -11.95144 | -46.64941 | 2025-09-10 00:30:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c5e49cbb-4652-3c75-b586-e5dae085b839 | -15.04898 | -50.1413 | 2025-09-10 00:30:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6fff2a1e-ef56-3775-91af-c9fe49d34952 | -12.06627 | -51.07845 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 893d8d98-7540-3acb-925e-654bbbfd3cd5 | -11.32501 | -46.52626 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 771750b5-8aeb-3d6e-b6c3-796fe4fd38b9 | -11.32372 | -46.51715 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 224.3 |
| a626e371-258d-3409-9ce6-64bb770bc4e6 | -11.54656 | -47.323 | 2025-09-10 00:30:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 31ab5d79-8565-340e-98a6-3c9199303f9b | -11.43601 | -43.70861 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7a5c7f85-f452-318b-9db1-2557d3766ac1 | -15.05914 | -50.13984 | 2025-09-10 00:30:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 27.4 |
| a0c6b611-e10b-3514-9fc0-d052d52ca2fb | -13.14901 | -45.29091 | 2025-09-10 00:30:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 201a9910-b3f8-3170-b5e5-e81d078396ec | -11.38033 | -43.53276 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 4a93120c-1516-3048-824e-ff31ac1a1137 | -12.99892 | -48.03692 | 2025-09-10 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 49ea9ddf-dff7-334c-89e3-63190cb9391b | -13.19325 | -45.27421 | 2025-09-10 00:30:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 2609de57-e837-32c0-9e15-f95801e13f48 | -13.92863 | -48.24475 | 2025-09-10 00:30:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e1e22a2d-0027-3b4f-be00-56b0cce00b24 | -13.91147 | -47.97817 | 2025-09-10 00:30:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9332acc1-4edd-34b0-b7e4-fb9df06fe5c3 | -12.06784 | -51.09122 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2eccc44b-b3a0-331a-87d7-6059325c3b10 | -13.19465 | -45.28392 | 2025-09-10 00:30:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 465f808f-8de5-399c-bcee-9d26df992686 | -11.4396 | -43.59439 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| ec8ae3a6-5478-3843-9351-68dfac332088 | -11.6631 | -46.90064 | 2025-09-10 00:30:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a7aa4fd9-9a7d-3387-9b97-94237488bccf | -11.33518 | -46.53407 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0a0daa27-2d8a-322b-90af-79051557a424 | -13.17809 | -47.25841 | 2025-09-10 00:30:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c3c82aa7-df1b-3848-bc63-18ad0f9793ab | -14.90253 | -50.11626 | 2025-09-10 00:30:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 6bea116a-64cb-3928-b2d2-87ad5dc5336f | -11.29947 | -46.47413 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d8e582f2-97b0-3df7-8fb4-606748925052 | -11.0339 | -46.03439 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ed468583-f730-3553-8813-a15873ccf36e | -13.20133 | -43.38112 | 2025-09-10 00:30:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d12efd0d-422d-3634-b74a-c41608984742 | -11.45366 | -43.61762 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 5a46a13b-0f6f-3372-81be-40ec3b1697ea | -11.13423 | -46.35207 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 61c990ff-e80b-34da-af97-e4ae9d56f818 | -11.34792 | -46.56014 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 46712403-61c7-3c53-802f-80ad824d72a2 | -14.24444 | -46.69857 | 2025-09-10 00:30:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d79b42fa-4839-3ddd-b1e8-21c0d1e34c47 | -12.08739 | -43.33001 | 2025-09-10 00:30:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 96e579af-1993-3401-96ad-f6310b56b830 | -10.59888 | -43.30846 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| bc0ed15b-74da-37c1-911c-fb535d2da68b | -12.00885 | -51.01504 | 2025-09-10 00:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 871165c5-8afd-3f02-b555-3b258fc65d93 | -11.88148 | -40.94978 | 2025-09-10 00:30:00 | TERRA_M-M | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| b21217a2-91ef-34b9-8820-c317e99c611c | -12.87903 | -47.96594 | 2025-09-10 00:30:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 58ff7231-6c3d-363d-8e37-8ae838120da1 | -11.4415 | -43.60687 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| ffa957cb-6ce4-3930-a156-e271602bab56 | -13.15673 | -45.27984 | 2025-09-10 00:30:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0e608a38-9f5c-364a-896c-eb2c87316cca | -12.18319 | -50.62398 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 7a4d1677-b532-3080-8c50-a557e1af8645 | -11.44339 | -43.61935 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 2d8bd595-87b5-3aae-87a1-52c8ca16ef26 | -10.60276 | -43.3015 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 42.6 |
| dc947aff-da87-3f60-8759-66e54686dcb1 | -11.41517 | -43.57266 | 2025-09-10 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| c6847142-1adc-3a48-861c-1ef73e27f2de | -14.51529 | -53.95047 | 2025-09-10 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 7676c978-4e52-3435-9649-09a5412b5824 | -11.03526 | -46.04385 | 2025-09-10 00:30:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 519e46ed-bd62-3ccd-b270-369481807aaf | -5.59083 | -45.0375 | 2025-09-10 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 3aca9a90-8752-327d-b859-99dd82a900d5 | -11.1279 | -52.02945 | 2025-09-10 00:33:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d3f97dad-c441-3284-9248-e16bed4d0d95 | -5.56085 | -45.18777 | 2025-09-10 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a3208eca-08cd-3f94-b3c6-9f4459fb52ce | -9.43449 | -46.72013 | 2025-09-10 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 91db1aa1-9f3e-39e9-b5b2-da2164ab4cf3 | -9.10085 | -46.97005 | 2025-09-10 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7228e8dc-c00f-36c6-9f86-b50a6163cb01 | -5.5468 | -45.374 | 2025-09-10 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8eb19e32-3768-3cc9-822e-a8ef3b7bdbee | -5.73893 | -45.28656 | 2025-09-10 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a24a00c4-2697-3965-92fc-f44f596d63fc | -7.78925 | -46.10064 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| de1a7857-0a36-3083-a0b9-11612a8eec55 | -5.76281 | -45.52618 | 2025-09-10 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| be5b8eb9-3e61-322f-b47d-0a89fb95a550 | -8.06887 | -48.68727 | 2025-09-10 00:33:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f0cdd1f1-15ef-3bef-b3cb-ff9fe82319e6 | -10.0305 | -51.66833 | 2025-09-10 00:33:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 13ae3331-75fd-3ade-947e-a84f3040d413 | -5.53845 | -42.6678 | 2025-09-10 00:33:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| adbc7e9d-31da-3c9d-8321-8badbea50c4b | -7.19916 | -44.90493 | 2025-09-10 00:33:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 1c36fb44-83fc-3e87-ab5d-1939ed750e9b | -11.11644 | -48.41446 | 2025-09-10 00:33:00 | TERRA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d0b40d7e-e1cf-3ddb-9df6-ac35385a60c6 | -10.02548 | -51.67466 | 2025-09-10 00:33:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| ee9af750-2aab-3df6-ad0a-9ff5808bc0b1 | -8.75049 | -47.10121 | 2025-09-10 00:33:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 930e066d-49df-3ce9-86c2-e3d39464aae1 | -9.06531 | -46.97557 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dd52c367-0b62-3213-be13-5c6d96992a57 | -9.05758 | -49.81314 | 2025-09-10 00:33:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3dad7776-577a-3102-863e-3cb3afd624c6 | -6.87746 | -47.8738 | 2025-09-10 00:33:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d098a9db-f0a5-3f1b-b658-a3d6f7ef8f5d | -10.30458 | -48.80927 | 2025-09-10 00:33:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 64a93ea6-0f50-33e5-a8a7-60e7f1a0adf9 | -5.71711 | -45.41826 | 2025-09-10 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 24778339-a3a0-3b3f-baa6-c3212215aeca | -7.81211 | -47.49979 | 2025-09-10 00:33:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 47d5a4fa-5589-31ea-9cd0-b089463b225a | -7.77433 | -46.06215 | 2025-09-10 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 2aafa081-5c73-3c97-ad9a-d0f63e40f09b | -9.10339 | -46.98814 | 2025-09-10 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5f9c749e-82b4-388d-998a-4eafa8881ba0 | -9.8281 | -46.05282 | 2025-09-10 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| ef1c5b2f-71b6-3a6e-aa75-9a3d8f4eb315 | -9.82948 | -46.06234 | 2025-09-10 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |


[Clique aqui para ver as próximas entradas](README7.md)
