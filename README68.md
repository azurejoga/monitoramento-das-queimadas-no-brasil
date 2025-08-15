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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 556271d5-eaf7-3dd1-a5f8-8cc2231664ca | -7.31753 | -60.61855 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e64e916-1543-39f8-ba71-066c89a8a355 | -7.62505 | -63.52017 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfe82b25-53e7-36b6-9b99-29769ebc8a2c | -6.4801 | -62.93721 | 2025-08-15 06:10:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 285bab68-6ed0-38bf-8100-da1d1c84957b | -8.32131 | -70.07378 | 2025-08-15 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38823b91-70a3-38bf-8da7-c767b7446424 | -10.86404 | -62.00026 | 2025-08-15 06:10:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2fa10575-8ed5-3d67-8539-6ea144a5f188 | -9.50632 | -60.5167 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 611f3d42-881e-3fe1-8dde-b3717e37871f | -8.11112 | -61.21286 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45f4d103-cb3d-310d-94a8-fcc68a1f99c7 | -7.53398 | -61.34908 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8a38985f-de57-392d-bbe4-aa7eb6adf8ff | -7.54036 | -61.34578 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 358a4a38-15aa-395b-8e86-48340d82b2c5 | -8.56334 | -63.90793 | 2025-08-15 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00ee2c0a-46ec-34d0-91d0-a06c5a7a853b | -9.18338 | -59.68092 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26a4693f-3d2a-32a1-b8a2-b4c4b3ff3138 | -7.53031 | -61.33167 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 91fe84a7-3905-3a2c-91ab-8243f2b4a1fa | -7.28532 | -64.69872 | 2025-08-15 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 89650a31-2c80-3faa-8ae7-ad8f1925614b | -8.10746 | -61.19461 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03c9799c-05ef-3472-bae0-7ae69aaf98b2 | -9.17158 | -59.66763 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56565198-f1f0-3294-9079-3cabce22e030 | -6.93837 | -59.53069 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 84a6eeb0-2340-3f68-afd6-b07c12c575a9 | -7.88326 | -61.81537 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74eb8fc4-4d7e-395d-a515-9eef0dad11ea | -7.95588 | -61.76645 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 953bbe96-4bc3-3ba2-acf6-3d2009f73985 | -7.31098 | -60.62141 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f35a6e5a-9e81-3c1a-a529-ff82fe5ad04a | -7.31694 | -60.62306 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40274086-3102-397c-8cc3-304ec35e842d | -8.67003 | -62.44661 | 2025-08-15 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92bb1d8c-b2f8-38ea-81a3-ca53320dd1f5 | -6.89845 | -59.15565 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 251bb125-085f-3f07-913e-8b7d77cf202f | -8.10689 | -61.19893 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1983613c-2e88-3533-bb94-f193564088e4 | -7.09297 | -59.22499 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eea0f0cb-6ac8-31aa-b5b7-d9a9865708bc | -6.88931 | -59.14862 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e20f841d-ab34-36fb-bdb8-0ae587aaabb7 | -6.87774 | -59.15881 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16a297eb-6c86-3cfb-b9aa-faedadcc9754 | -6.93704 | -59.54208 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| ef61e80a-5729-3fa8-8772-482067784b4e | -6.93041 | -59.54049 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| a06de4a4-99d6-3d73-99d6-ff1262c59785 | -9.17087 | -59.6733 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3578a18-4b51-39e2-8aa5-08af94eea175 | -7.95122 | -61.75779 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ca57992-94d4-3579-b2e0-eec170068416 | -9.63312 | -63.09206 | 2025-08-15 06:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 165869a9-0355-32f2-8c21-821120bf4603 | -9.49809 | -60.53112 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b93a16ae-7d89-3790-874b-642ba350d097 | -6.90086 | -59.13826 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc6c367a-8cb3-3747-9e98-573dca16e51e | -9.20687 | -59.6547 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01d82dc4-3a4c-3642-93ea-5d0f1ed46643 | -7.07971 | -59.22327 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d9303d84-d9f8-3379-9a7b-1a858799b959 | -9.02409 | -61.22027 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a83248d0-d6b4-3135-ab43-8c481a60104e | -7.08051 | -59.21742 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1978e6b1-1b6a-3f77-a67f-383579a82371 | -7.60182 | -63.50192 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| af09118b-d59a-3110-839f-7227e78b0a26 | -9.18267 | -59.68657 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68f476bb-0931-3fa1-8b38-dfad69c2ac67 | -6.89519 | -59.15537 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26eb8fee-2398-3054-8d81-e06a13539b43 | -8.10208 | -61.18949 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46869e8d-30f2-3269-9476-1a7925474fe8 | -7.32913 | -60.62479 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddbbbd5c-7409-39fa-99e8-87836fe10e27 | -7.80566 | -61.34813 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57a0f2b7-c75b-30b2-bb72-0a174ddd8e9e | -8.10802 | -61.1903 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 729bc2b1-0fc1-35ef-a9ff-c4a4f6b5d5c8 | -7.09729 | -59.21981 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52327d31-e6ed-3690-ba9a-86666b195b63 | -6.8926 | -59.14902 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb5ad0a7-0e5b-3dad-b4d1-5bff01ffd73a | -9.92563 | -60.48419 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88768d1c-9083-3bed-b4f8-e11870ecd4e5 | -8.40093 | -70.4398 | 2025-08-15 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 495ba9dc-80dc-3dfa-8d55-2f30053467de | -7.5356 | -61.33669 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bd29304e-347b-30e5-a0db-02cf39a0ba2a | -7.87136 | -61.81771 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52b4f493-b5ec-38f8-9d38-a91ec057d76e | -6.8819 | -59.15361 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05cb4c41-6582-391e-9eef-3a89e471bd22 | -9.18619 | -59.65845 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 315668c0-54b5-340e-90ea-3b365f172c3a | -7.52923 | -61.33996 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97a55f82-8e2f-3639-b1a3-f1ea58532577 | -9.15834 | -59.66583 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95e4fe41-218e-3246-8713-aac30f648dc2 | -7.53536 | -61.3428 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6b70d456-46a3-3dc7-8ac9-f18497001213 | -9.50188 | -60.55181 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e61c24a0-de37-3e7e-ac2b-67d14ab58824 | -9.3982 | -60.54056 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc6e0841-8237-3411-909c-4ac8135fea69 | -7.61413 | -63.52459 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 671d077f-dfac-324b-8f70-a5013ba004d2 | -7.53506 | -61.34084 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7af55452-7004-3e75-8b5c-570f14897b8a | -7.95746 | -61.75467 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53488cf4-94a9-34a7-99ce-fcc992571ea0 | -8.11169 | -61.20847 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50cd61a2-b02c-3f29-b897-b911c04980d6 | -7.31647 | -60.62663 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73ec90f8-633a-3a7b-90f3-080d2d3b45b5 | -7.53125 | -61.32951 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 890ddf8a-481c-372e-a0f4-f4374ba3aa3a | -9.15904 | -59.66017 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2e573a26-d789-3b97-940a-95466641b8d9 | -6.8918 | -59.15487 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 544b9d40-4e44-3630-a723-fa7cd9138dab | -9.2105 | -59.66125 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 504db60e-8349-3311-ae01-f30779979b60 | -7.52954 | -61.34194 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a95f4c83-eca6-3da7-84a7-6d7b0820dab3 | -7.08992 | -59.22465 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6810ea19-8a06-3a99-83d8-c4621cab9f4f | -9.54323 | -63.57694 | 2025-08-15 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37740e27-2697-3b4d-82f3-a30c9cbd46a2 | -7.28069 | -64.69804 | 2025-08-15 06:10:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4b0c0b58-5b20-3e26-b7b3-86be53cfe509 | -6.87526 | -59.15274 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eec2178d-9d3b-372e-ad3d-397beb8e776f | -7.42681 | -60.02603 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ff67506-b591-3103-a5d3-7be7683d7e50 | -7.94656 | -61.74909 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 177575c0-1196-3f75-8238-cd61e22b53a6 | -6.9115 | -59.13414 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cfb5623-f34a-325d-917c-61b6a1a79a01 | -9.79192 | -61.50107 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ff1cf3d-deef-38db-b29f-d74e8b657e61 | -7.60403 | -63.52314 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0f84d19-8454-3391-8fdc-88191c6e22f1 | -7.88165 | -61.82711 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f28411b-3542-38bd-8e9c-b4f4d7385fd2 | -7.12898 | -60.12665 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b36a20f1-a09b-3bd5-af11-4fbe17d49ccc | -8.91377 | -60.73137 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c869ce77-6652-3972-b673-fba41045fbf3 | -7.94551 | -61.75693 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6797890c-3b6b-34a2-a0fe-9ae244862120 | -8.6014 | -62.66354 | 2025-08-15 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 912b6d26-0967-39e0-b8ff-f7334277a761 | -7.87978 | -61.81533 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a7bdb9d-abdc-3284-bbf5-3a7f0f2be5cf | -9.53805 | -63.57623 | 2025-08-15 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9675e52-2a5d-3f29-910e-a1d3d0508aa5 | -7.53011 | -61.33778 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 57ebdbc5-dba2-3edc-9d67-d59de713ad67 | -9.17016 | -59.67903 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 759a42a6-1280-3116-ad37-e2c9759b2599 | -9.20759 | -59.64903 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 844cc5f9-3f42-35ba-9186-2b5f79a4230c | -7.95069 | -61.76173 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e3c130d-90ef-35be-a2fc-1904f13cfd1d | -6.92325 | -59.14764 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 355f6ed3-b249-38f6-9f83-c49f32520232 | -7.07225 | -59.20472 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88bfd189-3787-319d-8bfa-52c419674ea7 | -6.87643 | -59.83861 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 961e5d10-b585-3098-8535-5f5f600fa5b7 | -6.90337 | -59.14454 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43858855-c29e-36e8-ab1d-fcdfbd6f1b78 | -7.59676 | -63.50118 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f205d9e0-f873-3a98-b01c-380cac2a4c95 | -6.89498 | -59.13178 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd29b256-420c-3421-8148-b88e68cb121c | -9.50504 | -60.52684 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9f3da1aa-98c6-349c-ace6-3e7238d18648 | -7.07543 | -59.20511 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dac209e9-9a2d-3795-9aad-61d49a5f1306 | -6.4857 | -62.93489 | 2025-08-15 06:10:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6e058f8a-4ecb-318d-915f-e62ec1709714 | -6.90261 | -59.15034 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66c1d02d-8506-3e3a-9095-62bbe4c14318 | -9.20657 | -59.63778 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2a28182-a42e-3567-bd35-9a0e68eb6ea5 | -7.96211 | -61.76332 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f97a2708-2228-3393-ae37-c246c0f835fa | -6.90185 | -59.15613 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README69.md)
