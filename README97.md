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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54c3c150-2f62-34ef-8599-ccb67243931a | -17.86082 | -57.29125 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.8 |
| f0e92a98-593a-32b6-bc72-e16110e84c8d | -17.86001 | -57.29583 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.2 |
| bfffeccd-65a1-31eb-9296-00ffd286b3bf | -17.85838 | -57.30499 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 85b66661-3c7d-3378-af8e-a55924add128 | -17.85793 | -57.28596 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.7 |
| c1cb1de8-d114-35e3-a830-044b9cb7353f | -17.85712 | -57.29054 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.7 |
| 2a0afc7c-3470-3927-a19c-37683e6540ca | -17.85631 | -57.29511 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.5 |
| db0fe82a-54e3-3ac0-ac3a-e666bb0ff5ad | -17.8555 | -57.29969 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.5 |
| cdd66e1d-da9e-3a26-a982-58822138acee | -17.85468 | -57.30427 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 59aa1706-208d-39da-be7c-13ba017abd2a | -17.85342 | -57.28983 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.7 |
| e3281d47-aa82-3782-b038-cc33c92acc41 | -17.85261 | -57.29439 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.5 |
| f405d1af-98e6-31dd-a20d-175e27508b04 | -17.8518 | -57.29897 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.5 |
| 81a14e6c-0ecb-36db-b8eb-6f0321e576dc | -17.85098 | -57.30355 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7fc82084-6718-3bc1-92c8-5336f694aac3 | -17.84972 | -57.28911 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 26407dce-3ae7-3ffb-a68d-b9547218f890 | -17.84891 | -57.29367 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.5 |
| f51a86de-260d-3d04-acd9-dfdd74717a6b | -17.84809 | -57.29826 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.5 |
| 2a917ee7-9930-39eb-8aa1-3fb7c3c5bf8c | -17.84728 | -57.30283 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| c8f0b38e-b83b-3361-afb4-19bf9b271689 | -17.84646 | -57.3074 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 2b1edc35-459b-3c69-be03-a317c43cb0e1 | -17.84602 | -57.28839 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 20adbf80-602f-3162-967d-b1b8302bcc1d | -17.84521 | -57.29296 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.5 |
| ae0c904c-2828-3e58-9bc0-39a493ab3519 | -17.84439 | -57.29754 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.5 |
| 00288e98-be2f-3cdd-9739-30b6ac10b941 | -17.84358 | -57.30211 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 6a50a9aa-1a8a-397b-bd31-1670e3f6e67e | -17.84276 | -57.30669 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| fc9cb5a9-02e5-3274-b217-93e9448ff161 | -17.84233 | -57.28767 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8fca65ef-3698-30f2-b10b-881e9df33790 | -17.84151 | -57.29225 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 25e0ce8b-18b1-33a4-81d1-3a0a2dba033a | -17.84069 | -57.29683 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.4 |
| f587eea6-1125-3803-814b-9969e1887a4f | -17.83988 | -57.3014 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.6 |
| 07e14e4e-fec3-32c9-b59d-d947bd1ad49e | -17.83906 | -57.30597 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.6 |
| 4f78dc13-635d-3361-97ef-dd0e907e3a4b | -17.83824 | -57.31055 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.3 |
| 36250b0e-bac4-3ce8-aeaf-823d388389c4 | -17.83699 | -57.29611 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 0c838b3f-1123-30d6-87a6-8804bbd35f37 | -17.83618 | -57.30068 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.6 |
| 11a679cb-e383-34af-b672-d1da63845f1e | -17.83536 | -57.30525 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.6 |
| e4b99765-a73b-3b47-9b37-e105d162f73b | -17.83454 | -57.30984 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.3 |
| 9f12d08e-1144-3f14-90fb-a214c72f6e16 | -17.83329 | -57.29539 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b9c700d2-affd-3115-827e-c2f681d54cea | -17.83248 | -57.29996 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| c87d6644-5aad-316f-9fe0-04ac6b3ddf6d | -17.83166 | -57.30454 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| fde4be0b-5cd2-36fb-b39d-407d15c4b884 | -17.83084 | -57.30912 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 0d3da3ab-ce29-3ef9-8f68-061765ef469b | -17.82713 | -57.3084 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.4 |
| de8074ad-fef7-3043-b3b5-65fa999bae1f | -17.86614 | -57.28283 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7d0f3d61-d066-3e8d-bdd9-668c0ff3720f | -17.85054 | -57.28454 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 4729bebc-b140-3c72-8fde-912224cfab76 | -17.84684 | -57.28382 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 0c9b3f0e-3741-31a0-8037-815105a17e3f | -18.01967 | -57.35989 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.3 |
| 64d86296-0a4a-3488-91e6-d60e30a46b8d | -18.01041 | -57.3604 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.1 |
| a292fcc0-b891-376d-b1d9-36d4757ce264 | -17.99189 | -57.35679 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| afd0469b-f0df-32fd-83f3-2c21831bbd7c | -17.98738 | -57.36066 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 586fd10d-876c-3cf4-a23f-b5ff5520d8e1 | -18.02313 | -57.35337 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.1 |
| 315c025d-b24a-3883-ac78-f83ce9918938 | -18.02153 | -57.36256 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 4f1cce25-4c7b-3204-826f-116318120abd | -18.02132 | -57.35073 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| ec899b93-3c93-349f-97c7-6c9fa3f08140 | -18.02022 | -57.34807 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 90e7ed03-3a75-3f42-8d3f-c10581ce97ae | -18.01942 | -57.35265 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.1 |
| 41539854-1f73-393d-844d-7cb1ff946ac6 | -18.01572 | -57.35194 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.7 |
| 27c8c76c-8cb8-31bd-93d5-0a4f0f09ee28 | -18.01202 | -57.35121 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.7 |
| e7f12929-bef3-32a7-b7c1-6c416e5db8fd | -18.01121 | -57.35581 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.7 |
| 6af3cd8b-0a14-320f-9015-2eeb4abc6a27 | -18.00992 | -57.34132 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.8 |
| eb365d59-bc00-3449-94c6-468e9f63cfef | -18.00912 | -57.34591 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.8 |
| c3e9a26e-e204-35e1-94a1-5934a294ed9d | -18.00831 | -57.35049 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 67b50142-4bac-310c-95d7-89cb5179e5e9 | -18.00622 | -57.34059 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.8 |
| ba1bc065-7458-30b9-9e3c-c9f3928070f4 | -18.00541 | -57.34518 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.8 |
| 776163bb-add4-3e3b-8740-c1689277a816 | -18.00461 | -57.34977 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 4df0e1b3-117b-33ab-92cd-01bf73e482dc | -18.00381 | -57.35436 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.7 |
| d92d044a-559a-3de7-b351-42db7cd80d58 | -18.00252 | -57.33987 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| f2ba3c72-a9d7-398c-baf4-26d58f1a6127 | -18.0022 | -57.36355 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| a2e41039-dd27-3e7c-94fb-d279f20027fa | -18.00171 | -57.34445 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 7fe663ec-c7e4-3ed9-8bf3-f850b44e85ea | -18.00091 | -57.34905 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.9 |
| bd8924bf-2aea-3e38-b93d-6d56e79ed5a4 | -18.0001 | -57.35365 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.9 |
| 1fa00f9e-6580-33a7-bf49-2d7d38f4d246 | -17.99882 | -57.33915 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 3647d37e-3dac-3ef5-b7f2-4ad606be4926 | -17.99849 | -57.36282 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 36720386-b266-3f3d-b07f-bf4a89a08404 | -17.99801 | -57.34374 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| a13b1455-c106-3307-adcd-45338d890bc0 | -17.99721 | -57.34833 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.9 |
| 7609a73c-bdd6-3779-8bbf-4f9275acb867 | -17.9964 | -57.35292 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.9 |
| e365c7f8-1731-36f7-8db3-215b9fa5a587 | -17.9956 | -57.35751 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 596a240e-92b4-372c-983b-5a69e327980d | -17.99512 | -57.33843 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 95f41206-7b06-3cbd-908f-47262de92429 | -17.99479 | -57.3621 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d00c748b-0952-382f-bebd-a8ff8476e62a | -17.99431 | -57.34302 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 819480b1-f7ed-3125-8c2a-10c4666e623d | -17.9935 | -57.34761 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 70e01357-b932-3f43-9ec5-002b910498f1 | -17.9927 | -57.3522 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 7ce214f6-8fa8-3eaa-b346-e4945224fac2 | -17.99142 | -57.3377 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| ce3efcf6-8895-3083-90de-f449437a3f6a | -17.99108 | -57.36139 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7227199e-2d34-31ee-820f-934630640e4a | -17.99061 | -57.3423 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| a4408cb0-edc7-3430-a704-c263d16f4e1f | -17.9898 | -57.34689 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 56470737-712e-381b-a51f-e1a854cd4c27 | -17.98899 | -57.35147 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 8e1972f3-23ad-3bf6-82dc-c30c79829d85 | -17.98771 | -57.33699 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 6f4fd032-d880-362f-8817-77a316ddbf78 | -17.98691 | -57.34158 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 97a566c2-ff7e-3045-962a-5c6d350caf08 | -18.0242 | -57.35602 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| f2332bd6-935d-3e89-842f-922247bf3878 | -18.02337 | -57.36061 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.3 |
| 5cc1dc7f-99ea-3456-afe4-62d7fc30dbf2 | -18.02254 | -57.36521 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.3 |
| 958493cc-aebc-346d-9731-7495eb08af09 | -18.02073 | -57.36716 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 61138660-e333-34b5-a613-137aad7e2d9c | -18.01884 | -57.36448 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.3 |
| 5c0abb98-e1a8-33db-b9d6-c81cceada53c | -18.01801 | -57.36908 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 8f9c4f3b-35bc-3a56-833d-a4a3f1b22be9 | -18.01718 | -57.37367 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 81fd39fd-48db-3d31-835b-5c1d012b1f9e | -18.01702 | -57.36644 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 0eb29a7b-4528-35ec-b31e-87fc5a045b03 | -18.01622 | -57.37104 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.0 |
| df4ba0a7-6a7d-348c-8fa8-72e966bff4b4 | -18.01492 | -57.35653 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.7 |
| cc41c5d0-9193-3585-89f4-c61f0635a859 | -18.01411 | -57.36112 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.1 |
| b4841477-c4bd-3acf-8e92-b3146eb77fdd | -18.01331 | -57.36572 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 5454be01-373c-3cdc-8f24-78e2f0a96b08 | -18.01251 | -57.37032 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 79992f00-e4bf-360c-9576-df41c4fd6d8e | -18.01171 | -57.37492 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 77fa084c-3cc1-3ad1-a3cf-0789ada2fe79 | -18.00961 | -57.365 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 4ce54ad7-e63b-3670-bb87-f62f0aa3eb5b | -18.0088 | -57.36959 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 4f792afe-7fc6-3ac2-a43e-63121d0a6df4 | -18.008 | -57.3742 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| ab93173e-59ba-3f7e-8f03-8ef243f06f7a | -18.00751 | -57.35509 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.7 |


[Clique aqui para ver as próximas entradas](README98.md)
