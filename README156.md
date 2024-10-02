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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07bf75cb-907b-3128-9742-83407e3841bb | -11.23305 | -60.39054 | 2024-10-02 05:12:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37ccb34a-4b29-329e-9a0c-a3cd60124a98 | -11.22741 | -60.38179 | 2024-10-02 05:12:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0686eb42-6d81-37e0-8b9e-363356153787 | -11.2268 | -60.38556 | 2024-10-02 05:12:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74edb9c2-8526-3116-bcaa-14fbd00c0281 | -11.41008 | -61.37541 | 2024-10-02 05:12:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62dc1746-45f6-31ed-9429-b6c44eb59ce3 | -11.33178 | -60.55911 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c83918e0-97f5-350e-a4ee-4af61650d363 | -11.32833 | -60.5585 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f67cbf3-da12-3bd4-a6d8-2d63fc9072b9 | -11.32077 | -60.56124 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2149c84-10c4-330f-bde9-cf7e184a33bd | -11.32014 | -60.56508 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26feb228-90c9-3a65-a476-72513e5aa04e | -11.3044 | -60.57427 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c2a123e-5010-35f0-a9ab-517994aeba37 | -11.28137 | -60.60594 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b0fa328-ab7e-38dc-ba38-359c8a1626e3 | -11.27637 | -60.5931 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b26c61bb-1f00-3dce-bc55-e69ef6ec9aea | -11.27573 | -60.59693 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 427dc68d-cd7b-3da9-b259-a049a1e4ad4f | -11.27535 | -60.62074 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e517df02-fc19-3565-85e3-de6cfbcd0906 | -11.27291 | -60.59245 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05d9d783-c57a-32c9-8069-396cea556c11 | -11.27228 | -60.59629 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06cf4e21-19a4-3dbc-b603-38fef38a5da1 | -11.27099 | -60.60402 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75842a37-2bd2-3a67-a7de-6bb6320892dd | -11.27036 | -60.60785 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a1206a88-accd-3c60-af2b-9b2f9fadf4f6 | -11.26753 | -60.60344 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f88bb281-4208-3008-95a2-b1c63ec6d4f3 | -11.26471 | -60.59893 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f92c15bf-62e3-31fd-a749-03b7c5c33da9 | -11.26125 | -60.59833 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e1cc654-da47-34d3-8ea3-376302f603de | -11.25843 | -60.59386 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b594ab05-e267-3f76-8be1-11d418b54201 | -11.25779 | -60.59774 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 57d0cedd-1795-3275-b1cc-d0a43cb3fb82 | -11.25432 | -60.59716 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6492a8b4-82a0-32c1-8806-13b259b14da4 | -11.25365 | -60.60114 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0dabae13-a38b-3fbb-93f6-6ea9a3eb2091 | -11.25084 | -60.59667 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f612827d-0d60-3e74-85e6-e6b22bd30238 | -11.25017 | -60.60064 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f300bab6-7fa2-3028-8714-d869f71468d0 | -11.24901 | -60.59727 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 51890bde-8f5e-329e-a8af-ffdbb4c9d43c | -11.24836 | -60.60126 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 29771eb6-7432-3d12-b016-b4582b040831 | -11.24735 | -60.59618 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ea351565-67d8-3383-9419-7742da30fbbd | -11.24669 | -60.60014 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| da64bc92-d094-3672-be12-8fdce2245fcc | -11.24553 | -60.59679 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 260b828d-c3d8-32c2-a071-84b04e7445fa | -11.24488 | -60.60074 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e15bc4b4-67d2-3949-952d-a8de603a53a7 | -11.19805 | -61.28187 | 2024-10-02 05:12:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74a7dee7-812f-3e5d-8cc7-22c7dd875c20 | -11.17982 | -61.2155 | 2024-10-02 05:12:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc4cddc7-72ac-368b-a6cb-1964a2022af8 | -11.17636 | -60.64877 | 2024-10-02 05:12:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c3780ca-f19b-3fb5-ab37-a29c6334aeb1 | -11.15557 | -61.20729 | 2024-10-02 05:12:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a3086cd-4e62-3db2-b3e4-5c6d070729a4 | -11.1527 | -61.20261 | 2024-10-02 05:12:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eadf0a8e-0071-31be-9061-29aca69cecb5 | -11.15201 | -61.20669 | 2024-10-02 05:12:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bcea6a1-b0ec-3a51-a586-d13160d05f4d | -13.28718 | -60.81847 | 2024-10-02 05:12:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15c1a596-03c5-3f26-8390-0963bc040cf7 | -10.63819 | -62.8139 | 2024-10-02 05:12:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0150e4cc-21e7-34f9-834d-23e4e9c9c53a | -10.63734 | -62.8189 | 2024-10-02 05:12:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ae0efce-9dad-3970-abf1-8e7b95e6fa34 | -10.92444 | -62.44841 | 2024-10-02 05:12:00 | NPP-375D | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4740c03-2eef-32ce-a0e9-d898818f8968 | -11.31252 | -62.07243 | 2024-10-02 05:12:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5eb41e52-f4e3-3e63-ba50-f0a9195ad933 | -11.30955 | -62.06736 | 2024-10-02 05:12:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09abf8cf-d20b-357c-990f-b72a5cc62cc4 | -11.30881 | -62.07181 | 2024-10-02 05:12:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 55755fc9-91f7-3a23-9c3c-9239123292b9 | -10.92824 | -62.44912 | 2024-10-02 05:12:00 | NPP-375D | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48387503-5e43-3ecc-8986-570e7f67f2ae | -10.90394 | -62.61711 | 2024-10-02 05:12:00 | NPP-375D | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a353da76-5926-3bdc-b42a-9ad93542201f | -12.26638 | -62.31713 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c37b482c-b5ac-3dcf-815c-62b0e92fe138 | -12.7064 | -63.08038 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8b22e58-e608-3b57-af52-d02533078ab7 | -12.68075 | -63.09078 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2900d631-ac26-30b6-b9ae-9c71cae70bfd | -12.65717 | -63.11163 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57d1a10d-a8d8-389f-ae12-09413219e1b4 | -12.65682 | -63.10974 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 55451e35-2fef-32cf-9d07-98321584c46b | -12.6563 | -63.11653 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4716fd8-bb2c-3ddc-bef2-a1d3da511100 | -12.65598 | -63.11463 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b73b016-b086-311a-aca5-a259a1498f03 | -12.65514 | -63.11954 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 90d5b51c-2e96-340f-bb77-82821b312149 | -12.65296 | -63.10903 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 18.5 |
| d6957f3c-3f86-3483-b7ba-d1eb7bd6d471 | -12.65213 | -63.11392 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c3848c8b-63a9-35cd-91b2-90a4e8af0e5a | -12.65129 | -63.11883 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 310eb13f-e45b-318c-aac0-3d75cd9137db | -12.65045 | -63.12373 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4f2e79d6-0281-300f-b141-8bd7d9c49c24 | -12.64911 | -63.10833 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f9a213b-3d17-3624-a347-ddb3741f4475 | -12.64827 | -63.11322 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 19.6 |
| f74b05ca-6779-360e-9b46-9b9d66d262a0 | -12.64743 | -63.11811 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 19.6 |
| d217b2d7-5e24-35e9-aeca-4c09b1768971 | -12.64659 | -63.12302 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| beb71d1e-22fd-33c0-b15a-5e465fdcc0b5 | -12.64491 | -63.13283 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| cceb24eb-56fe-33c0-8cd3-10b7458e9e95 | -12.64441 | -63.11252 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 43a10016-9ccf-3d06-8237-f5ada1f1f1b8 | -12.64357 | -63.11741 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 671f2cc7-a592-3bf9-828f-0ef1e4d1d9af | -12.64273 | -63.12231 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 870ec5fe-ef49-390c-a307-773d9d077ba6 | -12.64189 | -63.12722 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2b543810-84fa-3400-8ac0-2111ee4a9372 | -12.64104 | -63.13213 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f23398d0-30b5-3f1f-af54-125ce8cfe0c8 | -12.63887 | -63.12161 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccc06687-bab3-3a04-a592-a276c9a11fe9 | -12.63802 | -63.12651 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef86b4c8-6e19-3c21-9c64-2635f9656e38 | -12.63718 | -63.13142 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1ff27638-0199-3cf9-addb-85e66d7ef647 | -12.63332 | -63.13071 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9c98ee26-aff1-37e6-8334-9c5a97380c83 | -12.38746 | -63.00095 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b60ca810-2964-3d44-bacb-4f0bc3bc83a5 | -12.38661 | -63.00579 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e4076ef-7358-30b1-904a-9e160dd6af9d | -12.37507 | -63.00367 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51f2babc-3f41-30a8-9d73-ebda25da52b7 | -12.86303 | -62.84999 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4ff4c734-6ebd-3358-8674-3519944b3eb1 | -12.82909 | -62.88759 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e9c311f-744a-3168-be42-87168f82dae0 | -12.82827 | -62.89228 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 16597564-c1eb-3886-96a9-bb51008e178e | -12.82447 | -62.89162 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b53cafcb-a6ea-3745-91f1-b48766978550 | -12.81204 | -63.00724 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abd8ba65-4fa7-3508-a3ec-224080d11adc | -12.80821 | -63.00654 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bac5330d-8393-320e-b46e-184fd983462e | -12.78016 | -63.03119 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d91291f-8d2d-3431-9fe0-9ef7838b8858 | -12.77843 | -62.91517 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c439eb2-b370-3928-be78-3ece447a1194 | -12.77788 | -63.03345 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 667b9ad9-7dcc-3f9e-baf5-c1e1c0f89a27 | -12.77404 | -63.03277 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa9d0aab-2d0f-37e5-97e7-d3b81c97e154 | -12.75857 | -62.91646 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f4362a66-ada0-3a11-9f9e-35a7fc2eb3d6 | -12.75476 | -62.91578 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ceaa095d-32bb-3168-9a20-e834c4179a8b | -12.75372 | -62.87647 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d538ed4-18f8-393d-9024-c95a458e352f | -12.7529 | -62.88121 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec5073c0-58e9-3756-aadb-ff7372013e50 | -12.7526 | -62.90559 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5cc5816b-6ed1-3e22-8c55-f9a50de0ca6f | -12.75178 | -62.91034 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50931189-4706-3d92-b935-370ebab5df7a | -12.75096 | -62.91508 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5c29b4a-960a-37c4-8600-c171eead8083 | -12.74879 | -62.9049 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 339a8b51-e065-3f80-ab44-3964e004d2c1 | -12.74797 | -62.90965 | 2024-10-02 05:12:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2394d5ac-0901-3418-8c39-eee72a2a7b6e | -13.00242 | -62.71504 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0d3fa399-81f7-3caa-a849-261ee13f6f98 | -12.99867 | -62.71435 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c32b86e5-8bf8-3cf7-bf5d-9ce4f459c6a5 | -12.99788 | -62.71896 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| decc13f0-d8ad-3b1b-94e8-4200b4fb10b9 | -12.98446 | -62.70703 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c32af885-e7b8-3b2b-b17f-93753263bc69 | -12.9839 | -62.68797 | 2024-10-02 05:12:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README157.md)
