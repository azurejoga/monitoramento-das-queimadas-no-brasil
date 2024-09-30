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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fe8ce50-2bba-3ed2-972f-9651c66ce249 | -8.5172 | -44.70593 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5fd10851-397b-3350-b0a6-e11e67b9d19c | -8.51684 | -44.71175 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b8efece5-9d1f-3616-a935-402d9b90cb91 | -8.51657 | -44.71029 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cef95c99-6a68-3e14-afdf-225c478f7e5d | -8.51383 | -44.70683 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e63b4f4-50cd-3b03-ad97-cc2f870f3841 | -8.51353 | -44.70535 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9632850d-bf72-3d49-87f1-7539388ff2f3 | -7.96314 | -44.9947 | 2024-09-30 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e62889b-58f3-3e07-b303-7d94e312ef42 | -9.30221 | -45.6353 | 2024-09-30 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b55f915-d38f-38a1-919a-0a2394bdb29a | -10.73657 | -45.89875 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a42bd02f-1674-3310-8001-87a22e5c966b | -10.70058 | -45.89922 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57f24a7a-617d-371d-a04c-a84540070948 | -10.70013 | -45.85355 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c443711-0560-39f0-b430-f4968de8b8cd | -10.69997 | -45.90332 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45ebbd00-9db7-326d-a7cd-42f5d04c01d5 | -10.69888 | -45.88629 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a601d085-b6d2-3b24-8a1c-164a51a706c4 | -10.69765 | -45.89458 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca741211-2936-3ed1-a6b8-c0af0169b3d1 | -10.69594 | -45.88171 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df88449f-8eb9-3d31-a44e-b95624b4c3c6 | -10.69238 | -45.88124 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 610885ab-e775-3a0f-9469-708cd9c73923 | -10.68943 | -45.87667 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07f2284e-af68-31a4-ad22-a909c2122c94 | -10.68649 | -45.87206 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65e0eb37-38b1-33f1-a11b-457429c9d9c0 | -10.68355 | -45.86742 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98051478-de47-3c46-b00b-2af4efe2b6b4 | -10.68293 | -45.87156 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5871abff-f4e5-3cdd-acca-f8ace1e7a983 | -10.49333 | -45.1321 | 2024-09-30 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 535c144f-6e2b-37f4-8495-21f10b636a5a | -12.21147 | -45.52774 | 2024-09-30 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b44c9ca0-8679-306b-990b-de330fd43719 | -12.10191 | -44.99198 | 2024-09-30 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53404e7d-8b41-3e12-8a9d-d5da32260861 | -12.1012 | -44.99698 | 2024-09-30 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 675deb5f-1d57-39d3-9a9b-c913c899f127 | -12.09812 | -44.99155 | 2024-09-30 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c663e337-371e-3efe-aaf9-5fd0f56cc41b | -12.0974 | -44.99661 | 2024-09-30 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47b6b8fe-3a53-3f53-907b-56e051bab091 | -11.87712 | -45.54539 | 2024-09-30 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ce0ec6b-41df-3924-a7ec-da8ac55be888 | -11.78743 | -45.46763 | 2024-09-30 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72166af2-5b5e-36b1-9b3c-04904a1984db | -11.78506 | -45.458 | 2024-09-30 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5213e67-0b92-30cf-a81c-a3855f3fb9b8 | -11.78442 | -45.46248 | 2024-09-30 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4870c569-16c0-3056-8217-8087d7a949a4 | -11.78141 | -45.4573 | 2024-09-30 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 360ba326-562b-3517-9adf-8736038688f9 | -11.779 | -45.44788 | 2024-09-30 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53d09a18-dd95-3e1d-b70a-280a9b0a04ae | -11.77838 | -45.45226 | 2024-09-30 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ce80ab8-0ec2-37da-b951-7ff4be27c2ee | -11.77624 | -45.54581 | 2024-09-30 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10ac8b0e-74e6-3848-aff5-9592eda5ea8b | -11.77562 | -45.55017 | 2024-09-30 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30698b2f-9621-3668-907d-0241d1d083c5 | -11.76978 | -45.46003 | 2024-09-30 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d509387-418a-3cdd-924e-ae8de84a1b49 | -11.76732 | -45.45098 | 2024-09-30 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b3df8c2-0ef6-3340-a528-05ce399b5e8e | -11.60601 | -44.81631 | 2024-09-30 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 575f0210-8e90-36fc-8c30-25475255cfbd | -11.60533 | -44.82103 | 2024-09-30 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18c187c4-dabb-31c7-8120-9127feb58015 | -11.19315 | -45.73635 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 09f82583-f56a-3ec8-a0b8-5da73748ecf0 | -11.19255 | -45.74053 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 35226287-710b-303c-99ac-afb69600ecdb | -11.19076 | -45.72746 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ef93d516-51de-3c01-a3ce-e066a5671c83 | -11.19016 | -45.73164 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 404dca9b-2ab9-3a30-b17a-fd0e69089003 | -11.18895 | -45.74001 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b693317b-0852-3453-8b86-4228bc3f5733 | -11.18835 | -45.74419 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b33ee134-fa38-30c7-8d02-ced7230017c4 | -11.18657 | -45.73112 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c31823a1-2efe-3b99-ad1c-bc9824b68a20 | -11.18476 | -45.74366 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fedce357-8262-392e-abf5-9a1243227949 | -11.18268 | -45.74437 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1cb6b382-f3cf-3021-a23b-1a7e73348dad | -11.18117 | -45.74313 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f6b71971-ec81-31cc-925e-0742711a8e0c | -11.18057 | -45.7473 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cbacd4a0-206b-3a24-9c9c-4fff45c90c2b | -11.18033 | -45.7355 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d07678c-c194-3c23-9e3c-46c0f69e550b | -11.17971 | -45.73967 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 79520648-8de7-3b9a-912a-c7f02ad876dc | -11.17909 | -45.74383 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 096f503c-83cd-3562-8230-fb496571725e | -11.17846 | -45.748 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3b6bcbe5-50c9-3029-b834-6047440914ed | -11.17818 | -45.73841 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e977a251-ca4a-3922-afa9-3aa931b7f995 | -11.17698 | -45.74676 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5864c2d1-087f-34ad-b3c7-4f7bc7d0e51a | -11.17612 | -45.73913 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4decd15f-5d8f-3af6-b89f-e0d2d5ba3531 | -11.17488 | -45.74746 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a8fac771-bb59-3fd6-b9ba-3a78c97a2307 | -11.17253 | -45.73859 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 806b8345-7e48-3de5-a43e-9b6b20f5049d | -11.17191 | -45.74276 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 494a0bbc-b5a0-3335-9a91-b25ff9176ae7 | -11.17129 | -45.74693 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9482ebe2-33d2-3404-bb5f-9642e6ff611a | -11.17067 | -45.75109 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6435a4b2-f1af-3dc4-ad06-502d3fc2a760 | -11.16894 | -45.73806 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a47ab78b-d692-3fd9-b6be-9b430634b2db | -11.16832 | -45.74223 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e4a4ab7a-d855-3d10-8c63-945bdacebe72 | -11.1677 | -45.74639 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 4b42d6f4-0103-3805-a730-d33d9c57b24f | -11.16708 | -45.75055 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 77e2c93c-5977-37a3-96a8-3969d8c3841c | -11.16473 | -45.74169 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8650605c-2c06-3f55-a17c-0fb16fb0323e | -11.16411 | -45.74585 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 9b28e248-5414-3da2-bc1e-3a38f474925c | -11.16349 | -45.75001 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 43403234-acb5-354a-a0a4-d91c431b9ef0 | -11.16287 | -45.75417 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f480f00-becc-32d5-b32c-0206e3114a6f | -11.16114 | -45.74115 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5de7a9d4-f9b5-338f-bf76-eab06663fa0b | -11.16052 | -45.74531 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f9c81de2-1723-3347-9fa1-978c08834d4f | -11.1599 | -45.74947 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8582cebd-4ae9-39c2-b7d3-245e7279039e | -11.15929 | -45.75364 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 59d4e835-3c79-36b2-8dc3-f18a87da4ed3 | -11.15755 | -45.74061 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69cef2d7-ea99-3280-9d1b-7038490de305 | -11.15693 | -45.74477 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 34b18e22-2629-3f5c-9590-069180a7e222 | -11.15458 | -45.7359 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0e1527c2-aaa4-3721-b39e-ee79712188bd | -11.15396 | -45.74007 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 30215c85-3923-3129-b8fe-8e9613eb28c4 | -11.15334 | -45.74424 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9c12dc63-162d-32b7-8053-5d0cb5b16c93 | -11.15222 | -45.72702 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfcbbd7e-1f3f-3b65-aa84-fa3ba4df67b6 | -11.1516 | -45.73119 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0aa8882b-6eca-3317-97e6-1139825e798a | -11.15099 | -45.73536 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9b6776a6-d7d2-3075-8a42-2eba11bc71b0 | -11.15037 | -45.73952 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7e3355d5-d8e0-3928-88e5-74cce321ae79 | -11.14976 | -45.74369 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 42c0b920-b2ed-3008-b486-030b9f49f024 | -11.14863 | -45.72647 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 844040f0-ba98-3302-9757-05e4c485140f | -11.1474 | -45.73481 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bab06825-dea2-3c36-86bc-9a2ea6eb4578 | -11.14678 | -45.73898 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 47753251-1e71-3df6-961d-b24f5f923123 | -11.14504 | -45.72593 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 93cab90c-9106-373a-bd3c-2a67d127d62f | -11.14442 | -45.7301 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9a757dc1-5a0c-3f08-8937-83ee36a4b20c | -11.14381 | -45.73427 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0939792a-a45e-3f2a-9f0a-8a3de06ef782 | -11.1432 | -45.73843 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 72ed2a29-81e2-3d86-801f-452f29b2f4c9 | -11.14258 | -45.7426 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a92f6ea2-6c18-36aa-a951-1e995f348203 | -11.14083 | -45.72955 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a356ded2-50eb-362b-992d-95760e91a994 | -11.14022 | -45.73372 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 12adb70f-4b28-350d-8101-3c1e727fa59e | -11.13961 | -45.73788 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6836f8e0-ba35-3613-9223-e0eb91ab03c6 | -11.13899 | -45.74205 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 36a961fa-458d-36b8-8396-0c906e03ade3 | -11.13838 | -45.7462 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 761c874a-5121-35b2-8bcf-fdbb463b90a9 | -11.13663 | -45.73317 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8229b002-8d35-3eeb-a415-7885dbe09d81 | -11.13602 | -45.73734 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 48886743-8f1a-3935-b961-a36553f637ac | -11.13541 | -45.7415 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 267c173a-3e39-3a7b-9812-385bb3fcd333 | -11.13479 | -45.74566 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |


[Clique aqui para ver as próximas entradas](README34.md)
