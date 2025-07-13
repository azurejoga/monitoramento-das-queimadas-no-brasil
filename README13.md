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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96d67339-ffd3-3c4d-87b2-ffe77fc69067 | -12.02009 | -63.78924 | 2025-07-13 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ae90836-c215-325f-8b45-baaed1f27c25 | -15.56949 | -47.85626 | 2025-07-13 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88c490dd-b8bf-3f9b-b901-527a2a5922ec | -19.08417 | -56.04998 | 2025-07-13 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3de12ff0-623d-3fa9-ad59-7ef49c3bf17c | -14.31547 | -52.7434 | 2025-07-13 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ccd018c-5a4b-3605-bd59-98d692aae6e2 | -12.58139 | -56.97728 | 2025-07-13 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51f1c89c-1902-3497-b88d-f00a40a2c17c | -15.07815 | -48.94369 | 2025-07-13 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f4bd8dbe-37a2-3c23-9983-d26eb80e641b | -14.17406 | -56.30583 | 2025-07-13 04:51:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 12de1970-64d9-3d97-a31d-e6df749a3c1f | -17.69119 | -54.01196 | 2025-07-13 04:51:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65606f8c-3922-3162-bfde-5a448e1e9799 | -14.29548 | -58.65073 | 2025-07-13 04:51:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c77e6db2-e03e-3010-a94c-12143b9a1486 | -17.65362 | -50.48518 | 2025-07-13 04:51:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6afb3cb0-a92b-3fde-afd8-cfb3bc690199 | -12.02612 | -63.78687 | 2025-07-13 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0627678e-d812-3aff-b66b-8773d3b230e2 | -12.02616 | -63.79062 | 2025-07-13 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eacf0c0d-385f-3a4a-8393-1ee4326414d7 | -19.08549 | -56.04211 | 2025-07-13 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7af5f623-4bf9-3fd8-9127-a828b6694447 | -18.26888 | -49.7325 | 2025-07-13 04:51:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b3cc1f0-8c17-3008-9201-755501232019 | -12.0271 | -63.78589 | 2025-07-13 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcc0a54e-56f0-3cc3-ab61-e8ee71792243 | -14.17772 | -56.30648 | 2025-07-13 04:51:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b51f4afd-ab3d-3756-b432-282513d28f48 | -22.65793 | -43.29327 | 2025-07-13 04:53:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 11ee0551-6286-3478-b322-697a4344cba5 | -22.66395 | -43.29385 | 2025-07-13 04:53:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 76c1a24a-8455-346e-841d-4d43af6fd240 | -22.65834 | -43.28859 | 2025-07-13 04:53:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0273d5dc-be95-3786-b528-fc10c332456a | -20.62249 | -54.83827 | 2025-07-13 04:53:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 588a4ca7-174e-37bc-85e0-9ea7b01b6b47 | -22.66435 | -43.28918 | 2025-07-13 04:53:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 604f66e9-5bfc-3da6-92b4-588da77a5633 | -20.62309 | -54.83456 | 2025-07-13 04:53:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 344c0e74-ab8f-37cd-b357-b0ab0afd42bb | -13.8474 | -46.8964 | 2025-07-13 05:00:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 8a5f73d6-c2a6-3531-a06f-840a35b63a9e | -3.97815 | -48.41787 | 2025-07-13 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c9156e6-ae6b-30fc-b0a3-299b10ef6f8a | -4.2881 | -48.06142 | 2025-07-13 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e578c3e5-7839-38e0-a4a2-2cf9f80f268a | -2.91501 | -48.23869 | 2025-07-13 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5dbad3df-959b-3ddc-9139-a6656f8586cc | -3.61842 | -47.54492 | 2025-07-13 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e1a0280c-5a32-389b-936f-520612ef92aa | -3.9786 | -48.41485 | 2025-07-13 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ccfd3a5d-33fb-3cd3-8a80-32f289b528c3 | -2.91456 | -48.2417 | 2025-07-13 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da0eb992-d26e-3b6b-aba4-41953162cd0c | -3.62386 | -47.54561 | 2025-07-13 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22276343-ad98-3b67-ad97-b04ecc13e9a7 | -3.61047 | -47.54684 | 2025-07-13 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05babfbe-b35e-32ad-9e6d-be45c445b650 | -3.7552 | -47.11295 | 2025-07-13 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9270b523-d506-3743-b473-1b769ac968e1 | -2.58491 | -51.9241 | 2025-07-13 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39405a3c-803d-37a7-beea-f966ec6f0eec | -3.75018 | -47.10828 | 2025-07-13 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f77b2ee-eb8b-3047-bff2-0bf172ff6b50 | -3.60994 | -47.55035 | 2025-07-13 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fef439be-a43d-3979-96a9-fea6be09e0bb | -4.29388 | -48.05877 | 2025-07-13 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fc7424c-b1ac-3598-b57c-2014474afec0 | -3.31927 | -48.71416 | 2025-07-13 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a8bc21e-4687-3b4f-ab1b-be397b85334d | -3.61791 | -47.54847 | 2025-07-13 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 85658855-2d1e-33b0-9ea0-20ea47bd7a8a | -3.4038 | -43.37407 | 2025-07-13 05:08:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 315a5984-6d89-3bb4-94c7-fb8425f309d3 | -4.28904 | -48.05492 | 2025-07-13 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 030d66a1-b4dd-3a60-ba21-cee684f3dc47 | -3.62334 | -47.54915 | 2025-07-13 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e7ea127-dfc7-3cb8-a2ad-c954645b9202 | -4.29435 | -48.05555 | 2025-07-13 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa266d4f-6e91-35b4-89d9-d05b35fe2179 | -3.75576 | -47.1092 | 2025-07-13 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ebd6a63a-1e47-3732-ae90-d744d8c3c347 | -3.3968 | -43.37294 | 2025-07-13 05:08:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1fe9bc1-469e-395d-a91b-559d8f630d59 | -2.5857 | -51.91904 | 2025-07-13 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80927b80-28c7-3498-b42a-48941bdf4e58 | -3.31429 | -48.71341 | 2025-07-13 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3d46a15-cb45-3eb1-96e8-31417060112d | -3.75074 | -47.10452 | 2025-07-13 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87cc2576-50e4-3fda-b5dd-631143a847ef | -3.61247 | -47.54782 | 2025-07-13 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4ac6fd0b-5c73-3c7b-8ebc-c7e4133805c0 | -13.8474 | -46.8964 | 2025-07-13 05:10:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| debae05b-6cd6-3969-bdd2-44cb6b3aad21 | -9.2454 | -64.40668 | 2025-07-13 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 880b10f0-4ca4-38c4-931e-c9a9adbeb191 | -8.35197 | -45.64588 | 2025-07-13 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85cc07f1-8844-3cb4-b9f3-6638fb5c8b9e | -9.34187 | -58.83361 | 2025-07-13 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 377ea5f9-b5a7-30b4-8568-1f7438271186 | -9.20697 | -60.81846 | 2025-07-13 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd9ca4d6-a108-3c7e-83b7-c3df61d233d0 | -9.24738 | -58.76478 | 2025-07-13 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a75e06e-c832-3cf8-91c4-2c1e9588b1ad | -6.62974 | -56.28644 | 2025-07-13 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b3e1996-3aa1-3b07-8dd7-dedf6107b8c8 | -4.45356 | -49.00299 | 2025-07-13 05:10:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc8f2f15-95f7-3d96-9e8f-b1c3561c5c17 | -10.502 | -46.47323 | 2025-07-13 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfb5fe8f-4984-3cf1-850a-12a4c0630776 | -10.57066 | -49.12161 | 2025-07-13 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6ab316a-b6ed-3906-ab17-65e97c39c782 | -9.01957 | -61.22644 | 2025-07-13 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 337629ca-e726-3d94-b15b-92462914e867 | -9.10525 | -63.55804 | 2025-07-13 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57010da2-8911-3fe9-8fb3-8f7dfbddd99f | -11.82794 | -47.51074 | 2025-07-13 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b4b0a5f-7feb-33d4-bcf0-93092d461894 | -11.73762 | -48.52695 | 2025-07-13 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 269205e6-c3d6-3cc4-a6d1-7a5009ac204f | -6.44564 | -45.40121 | 2025-07-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66c2d9c1-b081-39db-85bd-a83c93d06da4 | -10.6831 | -48.31192 | 2025-07-13 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 544ef02c-5a2c-3baa-80e2-8f50261abebd | -5.74829 | -44.98558 | 2025-07-13 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fcc98650-54ae-3817-96a5-24f8596e7058 | -5.73509 | -44.98408 | 2025-07-13 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 3ccd1cb7-41c5-3d34-8e5d-ec2be0c763ed | -10.70043 | -48.31216 | 2025-07-13 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d54cad8-3437-36ce-9d5a-013910d8c492 | -9.02109 | -59.54469 | 2025-07-13 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 044f0480-e912-31c7-8f5f-b70051dde5c0 | -10.09533 | -60.49355 | 2025-07-13 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92a4c164-c418-397f-b4f3-803c5ef60d1f | -6.4463 | -45.40117 | 2025-07-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de4f14d6-6f17-3ed1-a0f9-af8f061cfbfd | -5.74243 | -44.9795 | 2025-07-13 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f72f0a03-47a0-3100-ab64-cd56c660d62c | -11.82851 | -47.50613 | 2025-07-13 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4c7dd5b-a903-3f55-b477-96a414ae8c0d | -10.67601 | -56.5486 | 2025-07-13 05:10:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56c0482c-6786-3d59-9422-4f13453757bd | -10.04533 | -59.11012 | 2025-07-13 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00173cff-80c4-3079-99d7-0581432334f8 | -8.89015 | -48.08841 | 2025-07-13 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be0a0cd7-ca81-3338-ab1b-59b863a62a48 | -7.09192 | -44.06679 | 2025-07-13 05:10:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b43af51e-ab83-3a0d-8206-c1737c9337f3 | -9.46394 | -62.19009 | 2025-07-13 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4648529-8b01-34c8-a22a-3289903ce138 | -7.59215 | -63.47057 | 2025-07-13 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d0c6232-e82b-378f-b92a-0228b5aa659d | -6.43916 | -45.40539 | 2025-07-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3008ee1f-52e4-349c-a0ea-76084470531c | -9.91682 | -59.90975 | 2025-07-13 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9442c1e0-c877-3ca3-8f73-dfd3c41b11ff | -10.1336 | -57.77644 | 2025-07-13 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5075f4b7-8b10-3f6b-8c49-71d129a7ec9b | -10.79907 | -49.63321 | 2025-07-13 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 217523ad-ec2a-3181-813d-baad709ad88f | -10.04589 | -59.10659 | 2025-07-13 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d96687dd-dbbb-3dfe-9efb-0fa31887d08d | -7.30873 | -45.32566 | 2025-07-13 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe61b11c-bca1-3d45-ad9b-4a91317965e8 | -7.42807 | -60.02917 | 2025-07-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 935670eb-83e6-3f3a-ba3f-3d4335c1d91c | -10.34293 | -49.92064 | 2025-07-13 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aefbb8d6-2514-37b2-91ed-5690a9409a01 | -10.79427 | -49.62931 | 2025-07-13 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7386a9bf-894a-3c30-bd6f-712ac7e74fc8 | -5.74755 | -44.99089 | 2025-07-13 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 907f492c-b23f-3235-93be-f517c288b77a | -9.31782 | -47.7979 | 2025-07-13 05:10:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d83fb60-21f5-3a3a-bbe7-d65796a8a6a1 | -10.05557 | -59.36269 | 2025-07-13 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38069f28-33dc-353e-a17a-7a4e9cf73d00 | -10.04808 | -59.11419 | 2025-07-13 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a18db4a-c3d0-383d-8cc0-8d7708a7bb1b | -8.35134 | -45.65065 | 2025-07-13 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6e33c7d-b5e1-3d87-b76b-cf058af464f8 | -9.02051 | -59.54831 | 2025-07-13 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5f44957-1b57-38ac-b27f-7a73b13aa436 | -10.50522 | -53.58696 | 2025-07-13 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f94765bd-a984-3df4-8163-8634e8a5ae38 | -5.72246 | -49.10938 | 2025-07-13 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d6f531d-cc2d-33dc-9dcd-7a594566098c | -6.43847 | -45.40545 | 2025-07-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a25f709c-a466-3897-af0e-2bcf21825ecd | -5.32546 | -55.94389 | 2025-07-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eeaf485a-e6fc-3f6a-9670-8b9c34a16596 | -9.34463 | -58.83765 | 2025-07-13 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ed01d1e-1df9-3e8b-afb5-78c6eee74de6 | -9.79883 | -48.56852 | 2025-07-13 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5590e28-be41-3585-872f-5c6b05343daf | -4.78068 | -45.35022 | 2025-07-13 05:10:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README14.md)
