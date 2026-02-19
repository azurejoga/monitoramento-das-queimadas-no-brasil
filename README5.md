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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a595a42-d322-3281-81c6-be15ab787e7e | 2.68623 | -60.15333 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 428b0960-8f2c-314e-88d9-21c5303257bd | 4.14686 | -60.71778 | 2026-02-19 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9eb6bfd4-779c-3fe9-afc3-90dc9cd443eb | 4.15034 | -60.71722 | 2026-02-19 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c825eede-1af3-32d6-94a4-bbbded9fa954 | 4.20257 | -60.45733 | 2026-02-19 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0df72914-59e3-301e-8c15-1410647b96c7 | 2.51651 | -60.98928 | 2026-02-19 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8589975f-096f-37a3-aa27-d52e8a466502 | 2.69644 | -60.24096 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 68327485-8422-36d9-bb31-9d0466e7375e | 4.06554 | -61.14612 | 2026-02-19 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7fb10c1b-6b5c-362f-8f7c-22d571361996 | 2.53134 | -60.72345 | 2026-02-19 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2dc71fe3-4c59-356e-b999-8b3196b9c766 | 3.92515 | -60.57352 | 2026-02-19 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6e4d83d-c79c-3bce-b882-fbab7721bd4d | 3.92577 | -60.57741 | 2026-02-19 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b8c57e1-af8e-33a2-a96e-83d62b09b652 | 2.43134 | -61.38634 | 2026-02-19 05:46:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70195c27-50db-30d7-a9f1-3f5512d67bd3 | 2.67898 | -60.15451 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2ff22846-e5ee-3180-b8d3-b795a3bb7fce | 2.68986 | -60.15275 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 289900cc-f008-3fd9-ad2a-ff0a0a14feba | 4.05684 | -60.27263 | 2026-02-19 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 513af7e4-9e44-3792-8883-d43ea2e43b3e | 4.05523 | -60.28513 | 2026-02-19 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 31def976-4b95-330b-9f63-20980341eca4 | 3.72553 | -61.13353 | 2026-02-19 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ac006b8-1b65-3364-a59c-37d8f8db0665 | 3.92351 | -60.58572 | 2026-02-19 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b07325e-9854-36d8-882a-92246a756293 | 2.66114 | -60.13594 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb2319cf-2c38-387b-b5ca-436c0665fbe7 | 1.96881 | -61.24463 | 2026-02-19 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85f3805f-039a-3c1a-891b-8629a060338a | 3.07181 | -60.92087 | 2026-02-19 05:46:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b28dd13-4515-38b0-a5c7-5f6f2bd03489 | 2.69939 | -60.23626 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f13b9e6c-0e5d-3453-9aef-52ff21e56c31 | 4.20193 | -60.45339 | 2026-02-19 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 971b5b74-1862-3bbf-afa6-76364f26512a | 3.94557 | -60.56628 | 2026-02-19 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d060510-2267-30f7-920e-54438e139071 | 3.92413 | -60.58961 | 2026-02-19 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0f71008-a6c3-3a97-867c-bfbe438f3bc9 | 2.69578 | -60.23683 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8429a0bc-849e-3781-bb36-71d2f86ade6f | 3.94206 | -60.56684 | 2026-02-19 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 739ac208-610c-3c75-b83a-e53220211da6 | 4.06494 | -61.14239 | 2026-02-19 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10b07c08-1996-3129-9b8c-efb518efa042 | 2.53487 | -60.72289 | 2026-02-19 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 34306f7a-00f0-3529-aaf7-3c906a7c0b9d | 3.31275 | -61.07111 | 2026-02-19 05:46:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe24ed4b-39cc-30b6-a3c7-3c9d994d6df3 | 2.68689 | -60.1575 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 93f88110-b592-38de-bc57-824a1ab0b0a7 | 4.07497 | -60.15909 | 2026-02-19 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db506569-479d-3bf0-9f57-b85945cea3c8 | 2.69052 | -60.15692 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 02b7e22c-178d-32d3-8017-39f85baedadf | 3.9624 | -59.69274 | 2026-02-19 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28def681-5259-3ea6-a195-0adf5018d41b | 2.68821 | -60.16582 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8c931864-d515-3e39-a882-47dd1a114406 | 2.69217 | -60.2374 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c56b61d9-3434-349c-a61c-3a62d7e3eda4 | 2.65684 | -60.13234 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| db113fc7-5259-3a06-9979-7cdb21c1eb28 | 2.78058 | -60.59405 | 2026-02-19 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cfcdc05-09a0-3650-aeec-e76cc41e73d3 | 2.66048 | -60.13177 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d5ea734b-0ac9-3f4d-8091-e4ca8a3cf8b2 | 2.69874 | -60.23213 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9121574a-b01c-34ed-a5ab-284941a543ff | 3.09065 | -60.81529 | 2026-02-19 05:46:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b76a920-d89d-39f1-b583-2056b24e4709 | 4.24438 | -59.79735 | 2026-02-19 05:46:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 27b3fd16-0fd6-3428-b89f-0284e5e81822 | 2.69513 | -60.2327 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9af0206-f1f5-380c-a4b5-52e1d5f48dbf | 2.68327 | -60.15808 | 2026-02-19 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 25fa7bbb-8fa0-383e-94ad-c31cca148762 | 3.70107 | -60.61601 | 2026-02-19 05:46:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b6dcb349-611c-34fb-90fa-882ca22aa928 | 3.08777 | -60.8197 | 2026-02-19 05:46:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9f3a0c2-5cb3-3d14-9222-276f814a740c | -10.74187 | -59.22228 | 2026-02-19 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66c36c94-eca3-3081-a8b3-fe27ccc963b8 | -12.3179 | -57.36413 | 2026-02-19 05:50:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a255468c-7daf-3cc2-ad89-03bda24aa105 | -12.31206 | -57.36686 | 2026-02-19 05:50:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c29810c1-0cd8-3607-b27d-e826a03ac393 | -12.31909 | -57.3652 | 2026-02-19 05:50:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46fffc5f-1b81-3508-a0f9-f248e5bb5abd | -10.66558 | -59.369 | 2026-02-19 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62cf5851-78c4-314a-82d4-bf1c3081787a | -10.67019 | -59.36966 | 2026-02-19 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b396b4d-e87d-3bb3-ba96-210538619653 | -12.31368 | -57.36455 | 2026-02-19 05:50:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3adc026c-a844-3927-8379-fcaaedc58987 | -12.31748 | -57.36744 | 2026-02-19 05:50:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af951683-6def-38ce-91ca-a81500c1a4be | -12.31327 | -57.36794 | 2026-02-19 05:50:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d0b596b-eaf5-349a-b358-78a46481f7ea | -12.31163 | -57.37024 | 2026-02-19 05:50:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5db0b37c-87f4-3fb6-a3d7-1cab3536ac3e | -11.43581 | -60.94091 | 2026-02-19 05:50:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f7f2cb3-b8a7-34d0-9ce8-b5dd29db52aa | -10.67127 | -59.36667 | 2026-02-19 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9699d481-1338-3c06-92a1-6c25ae1c886b | 1.65785 | -60.74718 | 2026-02-19 06:05:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa909783-874b-3ec4-9ca5-30ab1bc12986 | 4.15216 | -60.71997 | 2026-02-19 06:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d51fb515-3830-31c5-b716-7724620628d7 | 2.69576 | -60.24014 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cd37ce6e-c4e8-3c5c-b0db-69ae2d734015 | 4.42779 | -61.07583 | 2026-02-19 06:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c83d0e0-98d6-379d-8c16-fc6bf97347c7 | 2.68055 | -60.15397 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c9de6ef1-afe3-3d35-b6fb-a9212c58c4d7 | 2.68729 | -60.15766 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7303c150-059f-396b-82d5-c4ef41f7c852 | 2.65991 | -60.1315 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42bc39a4-8d4e-3551-b2c0-64fcc7bb8f93 | 2.69879 | -60.23124 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c422f7a-de12-36aa-8643-695257dbb852 | 4.2049 | -60.45802 | 2026-02-19 06:05:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83ae1257-f9cc-3bef-9519-a162343806a8 | 4.147 | -60.72084 | 2026-02-19 06:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cea56279-6c8f-30a6-af2d-2c65d871db1d | 2.78388 | -60.59542 | 2026-02-19 06:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e07d479-e16f-3c1d-a34b-9d316e4a6a1c | 2.69278 | -60.15676 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9228448d-c1bc-3973-8fbe-df8647b96d19 | 4.28739 | -60.00256 | 2026-02-19 06:05:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2ff7020-e510-3440-be26-10525d95d7e3 | 2.68113 | -60.15752 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e2e7e32-0d02-32a3-9181-d524a1967214 | 2.68778 | -60.16374 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8ba6cd1c-61bd-38b7-b5a7-bc8e7f07e2f5 | 2.66051 | -60.1351 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f99b656-c3a1-3708-8237-ab05671c8f7f | 3.09061 | -60.81738 | 2026-02-19 06:05:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8f1e053-f09c-33aa-9001-7c35a82f70e8 | 2.6939 | -60.23567 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 854b141e-73c1-30f3-b61d-d74569b76185 | 4.28262 | -60.00705 | 2026-02-19 06:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19fb7196-fd66-3f83-ae65-c217efd7d2a0 | 4.24622 | -59.79908 | 2026-02-19 06:05:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec4b3179-70bd-39c4-89e0-14dec67a5bb6 | 2.68668 | -60.15408 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 010cd51e-8dbd-38ef-947b-90c1fccf4d0c | 2.68836 | -60.16729 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b9826971-9d51-3095-9fff-b77094ddc56a | 2.68851 | -60.16479 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3579d314-75e7-3215-84b3-65d5b539f3ed | 4.28585 | -60.00467 | 2026-02-19 06:05:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9aa163c-ed5d-33c2-aeb4-8478e0819f23 | 2.68603 | -60.153 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b436cdb0-5001-34eb-b3cd-82afcdfc175e | 2.5311 | -60.72308 | 2026-02-19 06:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73c2c464-cf07-36e8-9216-424db2d983b5 | 2.70002 | -60.23222 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c5cde4e7-ab81-39ee-b3ca-a92f4acb38cb | 2.53695 | -60.72552 | 2026-02-19 06:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ac95778a-265d-3038-959c-b964d28afb17 | 2.68119 | -60.15503 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 15ca8424-1551-3b62-8066-c6255b14c058 | 2.69211 | -60.15567 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0db396b7-e2b4-3844-9c9d-607359b8adc7 | 2.69995 | -60.23834 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7ab8786b-291e-38de-97b6-52ff0467d00a | 4.42827 | -61.07867 | 2026-02-19 06:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e5b379a-3d50-390e-bb9a-57e6f679381a | 2.53641 | -60.72223 | 2026-02-19 06:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3efb3c62-d8ff-3e74-ab2d-33e29c5c5683 | 2.6903 | -60.24101 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c89dcdff-d73c-3c00-904e-73a91bea0f60 | 2.68661 | -60.15658 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 269ed8cc-0263-3a41-96e4-b2515676dfba | 1.6584 | -60.75055 | 2026-02-19 06:05:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9893106-5b16-3cb5-ae87-df2281a37037 | 2.70063 | -60.23575 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5037bb80-9516-313a-bd77-728d5c9f0095 | 2.77856 | -60.59631 | 2026-02-19 06:05:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e863193-d2ea-3cb6-89fc-541f72df1b82 | 2.69506 | -60.24274 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5180c868-ec34-37f3-aa06-79a063fb1751 | 2.69937 | -60.23478 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9a0a01e3-7456-367c-bf3a-859ceda43fdb | 4.20436 | -60.45484 | 2026-02-19 06:05:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f93415b-a1b6-3d9a-9a62-6b91e8ef7f03 | 2.68911 | -60.16835 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4959367f-62ea-351e-bd23-7ea5b64dfdbc | 2.6818 | -60.15857 | 2026-02-19 06:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README6.md)
