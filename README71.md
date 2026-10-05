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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c73cbe57-c0d9-3934-b4ea-fe2a97c29f25 | -10.40217 | -40.51144 | 2026-10-05 15:54:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ecec778e-fe69-3c68-90c3-3baccb5d85de | -11.64212 | -43.6209 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d66b7437-f72c-3e9b-bee2-a740afde64e8 | -10.34257 | -40.06749 | 2026-10-05 15:54:00 | NOAA-20 | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 95311b06-f06a-3eb1-8010-c7e56b1ca087 | -11.63433 | -43.61733 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1d86d198-d58b-3b37-9964-708c48de0688 | -11.74617 | -43.42477 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 787ca986-031b-3e25-834a-b2b511e448b6 | -11.56183 | -41.74406 | 2026-10-05 15:54:00 | NOAA-20 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| cc3d774b-c5fe-37d7-a08e-458063db96bf | -11.63933 | -43.56287 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 405b4541-a620-3459-aab4-5c42698637ae | -11.63605 | -43.61787 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4625191c-ed9a-3dca-97d1-013bf26c4ccb | -11.63931 | -43.59826 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5184b9af-3fc2-3d45-a43f-f8b06d2ce424 | -10.96961 | -45.41931 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5ff9a86e-f373-3a1e-bdc2-1765d2cee38f | -11.83373 | -43.54086 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| f10a3b0d-69be-33c6-b7b1-92a5ecb0b9ae | -10.9506 | -45.41906 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e58d1fe1-938b-3056-972c-db9992027549 | -11.68412 | -43.65278 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| e49decea-ade4-369c-b14b-793afb07e894 | -11.66548 | -43.64 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9231aabc-2be2-3077-bc88-d6c4bc7e1a21 | -11.63608 | -43.63236 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| d347e5ae-2193-3f73-9a17-7e153bdab0da | -11.108 | -46.09018 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| c8dd16ad-c98d-30b1-a81b-4647afafa73c | -11.82777 | -43.5386 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7c0d3bcd-b86a-3414-aea1-34055ca09407 | -10.06158 | -39.61496 | 2026-10-05 15:54:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 0b9ed8ba-9908-3870-aece-bb412aaebb02 | -9.84519 | -38.92006 | 2026-10-05 15:54:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 278c62e1-f4e2-357e-9b9b-9cd71d91d983 | -11.10735 | -46.08479 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| bc37e380-0398-3dff-a988-8d8af2b33fa3 | -11.67944 | -43.66146 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d12d2ac-525b-3d67-887d-1289a37af4af | -11.11447 | -46.08854 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 3ab44dee-5b64-3efd-8b46-47a9c09621de | -11.72325 | -43.50689 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 132a38b3-643b-3106-84ec-7625719af9e3 | -11.20443 | -47.14311 | 2026-10-05 15:54:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| fcf6e307-3624-3d25-b7db-1e14430eb270 | -11.37907 | -42.54914 | 2026-10-05 15:54:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 8ebd1675-247e-3998-807b-fea5857b15e9 | -10.9726 | -45.44446 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 2562d75f-51f2-3f67-8ff1-8ca32f263d9e | -11.21753 | -47.13433 | 2026-10-05 15:54:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 93c1891a-2f29-3543-a406-4ec026091cf6 | -10.97319 | -45.44947 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| da6686b0-1875-3be0-a73f-321f38602425 | -11.80934 | -43.5271 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ea002406-dea8-36e9-aabb-59530048591c | -11.64867 | -43.62771 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a88f9d75-baf0-3450-9129-404de3642949 | -11.63507 | -43.56421 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 96229c15-a138-337b-83fa-7c608adf6eae | -11.75432 | -43.5415 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d5a4fb37-e3bc-377d-aba3-719fb249d5a6 | -10.75669 | -45.30396 | 2026-10-05 15:54:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5a019bb2-9761-3edb-aaa6-abf66e20ada6 | -12.24888 | -42.11133 | 2026-10-05 15:54:00 | NOAA-20 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 1559dc1b-c963-3a43-ad7a-d0e9ef46d2f3 | -11.21762 | -47.1335 | 2026-10-05 15:54:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3caf9c67-55ff-3afa-aca0-8c1a6855534b | -11.66721 | -43.65464 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 9b835c06-742f-3494-8598-2d77aff5efc3 | -11.67108 | -43.6391 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 550f45c7-f091-334c-9d5b-cdbb9a60b1c4 | -11.74661 | -43.42847 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 76ba2dff-27a2-31f9-87b6-e5dce06137bb | -11.83293 | -43.53439 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| a5b1a417-41c1-33e4-addc-5b1ee6603de2 | -11.64212 | -43.6353 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| d03d2736-07f0-3d8f-b0ec-db92c7ea26a0 | -11.46302 | -43.39732 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5f16607a-91d4-370a-bfc0-abc19ae23235 | -10.96624 | -45.44429 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 4d06a96d-f457-3914-905f-e473aa4c8542 | -10.95986 | -45.44392 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a905d69f-7a45-39d8-b17c-077e09874b88 | -11.66678 | -43.65098 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 06a66e7e-140e-353c-8f15-802b65c3f2e4 | -10.30178 | -39.72684 | 2026-10-05 15:54:00 | NOAA-20 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| dddd4304-2543-3832-8e8f-bf70931da799 | -11.11787 | -46.06046 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 637b4662-9bcb-3607-965e-7690214375b6 | -11.82857 | -43.54511 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2b532932-bcfc-3e90-b0ca-bf62d876b444 | -11.72278 | -43.50314 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| b32dba42-2a6a-390a-979f-6567ca7fbcaa | -12.08687 | -43.41522 | 2026-10-05 15:54:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b3ab4cd8-0942-38e4-8844-afac3df9a91a | -9.3722 | -35.52045 | 2026-10-05 15:54:00 | NOAA-20 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 75974c35-faf9-32e1-80ee-677be38abe93 | -10.95871 | -45.43421 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8980f5d2-2038-35f6-b6c3-15c4a6db60a6 | -9.41929 | -35.98507 | 2026-10-05 15:54:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| f23483b6-b632-3d5b-869f-e57ed5e993c1 | -11.38298 | -47.72158 | 2026-10-05 15:54:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d1cd0654-2a79-3503-a536-491c657e1c2b | -11.82737 | -43.5353 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c5575ec9-451c-39fb-978e-3247f24c2bd3 | -11.20375 | -47.13681 | 2026-10-05 15:54:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d780c24b-d6d5-33e7-a02a-22ced6307e24 | -11.27167 | -45.23504 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d92d333a-7a3c-3192-a9d3-b82d8070a336 | -11.63861 | -43.60528 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 00f1918b-1a1c-3184-ae87-4780f965367c | -11.37865 | -42.54584 | 2026-10-05 15:54:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 2d9b3d81-7bdf-3b91-ab44-69b0fa946a5e | -11.6607 | -43.64788 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 454a2beb-b3ee-3b56-b63e-a27db793bcd0 | -10.97827 | -45.43886 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 41878a2c-dbd7-31fa-b1ba-dc871b374655 | -11.66592 | -43.64375 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 85d7b8bc-1152-39ae-82fa-6b89e55c1100 | -11.63699 | -43.62543 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f956db1f-8e18-3469-8c42-78cf932291e8 | -11.26494 | -45.23124 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5c71ebc0-2ac8-3ade-b5cc-0e9ff355e67f | -11.65748 | -43.60712 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b63e4dae-a588-3270-9f3d-79811152c688 | -10.97887 | -45.4439 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| ef15dca7-8e2b-3108-af9b-b17288fe6a0f | -10.96568 | -45.43962 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 097b957f-8699-3e63-9a23-98847fe288be | -11.63521 | -43.62492 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 48c4a978-362c-3cba-ab58-d2556de8fd88 | -10.51085 | -46.05947 | 2026-10-05 15:54:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a5450f34-ffc0-3881-8fe5-20f10eeb3013 | -11.71629 | -43.49635 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e2940ecc-3938-3ec3-967c-33e2a0c8f544 | -10.97947 | -45.44893 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 6cfee69c-c725-34a7-9fc3-9ba275785074 | -12.08642 | -43.41147 | 2026-10-05 15:54:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a11b5f49-2773-3599-8239-4178e1bfadf8 | -11.71767 | -43.50759 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 82fcf5c4-489f-30c0-8e83-f66cd525e499 | -11.82695 | -43.53194 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3f854576-41ac-37bc-9d3f-35db1e7a20f8 | -11.66153 | -43.6549 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 42101c0d-c21d-3550-9c27-5050dcab21d4 | -10.9604 | -45.39499 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a671c698-b7b4-304c-812c-ce7b5e526cce | -11.83333 | -43.53763 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| e7b328cc-2697-3975-8029-b1174bbc7e1d | -10.9645 | -45.42958 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7a1b67c2-8134-3f71-977d-2d14334e3b5b | -12.16816 | -42.19499 | 2026-10-05 15:54:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a07656da-2946-3c07-8ab9-9cf692aa7238 | -11.11725 | -46.05507 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c636909b-b1f2-3b8e-94ce-04be9a5edc7e | -11.63274 | -43.63722 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| f707c23f-502e-3e06-b689-5683f9c78635 | -11.66636 | -43.64742 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| f84c9810-0406-393b-aa68-4709c8fcb970 | -11.64165 | -43.61711 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 17a72420-4552-3617-8343-2135fbf67a9c | -10.95352 | -45.44394 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e4bc84fd-76d7-3e9b-aa65-5d35afd11120 | -10.17427 | -39.2692 | 2026-10-05 15:54:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ceb9ec25-d363-3f3f-91b2-146feb090d85 | -10.74995 | -45.30008 | 2026-10-05 15:54:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 238c098b-abab-31f6-913b-a6e2017f3226 | -11.67622 | -43.63437 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 137b0313-7dfa-3dbe-9d17-a8efd0a47381 | -10.97379 | -45.45448 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 237f970b-8170-3fda-9d8e-e5aaf4563096 | -11.63477 | -43.62113 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2998adbd-9f2b-37e1-8a33-f47a6d786653 | -11.83253 | -43.53112 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 1bee86e0-4dd1-3cae-823d-bc335533caaa | -10.961 | -45.40002 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 077e13bc-3d29-33dd-9cac-3968825c4c58 | -11.66356 | -43.65554 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 23dae3b2-eeba-3167-a9d9-a9e59d1f6ff9 | -10.96511 | -45.43472 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bff610b4-4ab3-35e9-9787-81fcaef5588b | -11.63652 | -43.62167 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 23dd85ad-485b-3f05-9e77-29bac886da3c | -10.97201 | -45.4395 | 2026-10-05 15:54:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7905d6bf-f8a2-3a42-bbfd-3ea289f6aaf3 | -11.67154 | -43.64302 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fc189eee-718b-34b0-a73d-bcfbdc195d86 | -11.66222 | -43.64489 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 682d5fa3-cb8e-3fe3-be3a-504238b3760b | -11.38561 | -47.72154 | 2026-10-05 15:54:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e2e7413c-17bb-3990-b4ff-ce191ad62238 | -10.62701 | -40.32269 | 2026-10-05 15:54:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4f0cc40f-ffc7-311d-a1cc-707a098551a4 | -11.64306 | -43.62848 | 2026-10-05 15:54:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b453e42f-0549-34ae-b6c7-161609b6ef33 | -10.07233 | -39.16123 | 2026-10-05 15:54:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |


[Clique aqui para ver as próximas entradas](README72.md)
