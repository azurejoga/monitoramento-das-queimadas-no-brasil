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
| 518a1327-30dd-3062-a3e5-0c0e0ca07269 | -15.21563 | -46.17784 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0639e6bf-4b9e-3425-958d-fc5c9f646e75 | -16.44073 | -40.26503 | 2026-09-28 16:24:00 | NOAA-20 | SANTO ANTÔNIO DO JACINTO | MINAS GERAIS | Brasil | 3160306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 50db29fe-4c1b-3a1b-905a-0b2b676a9688 | -15.45633 | -41.44643 | 2026-09-28 16:24:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 2b15665b-eb14-35c3-bf3f-2150a7087cff | -14.3812 | -52.09884 | 2026-09-28 16:24:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2ba8d8be-8678-3a43-97fe-dec5e03a6fe3 | -11.91566 | -49.92293 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e504282f-3c12-3ab0-a445-4ae12fa16b71 | -11.12701 | -42.17464 | 2026-09-28 16:24:00 | NOAA-20 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 71fb4431-0e73-338d-85ab-142b77c1af96 | -16.63252 | -48.46962 | 2026-09-28 16:24:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d99218a6-fc0e-3a32-ae8e-bac6f94d76ee | -12.10604 | -45.2152 | 2026-09-28 16:24:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1f60cb88-4369-3a2d-9597-d74dec9ca83d | -12.62215 | -47.28098 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| e47fdfec-2cc7-389a-81c7-b4c2a6e2478f | -17.34288 | -48.2583 | 2026-09-28 16:24:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1681c64-ad0d-3df0-a426-9c2709f86ece | -12.37526 | -50.23645 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 2c5afa90-9b32-3a37-a213-6545ed6f09fb | -14.45008 | -40.80378 | 2026-09-28 16:24:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 071058c9-6c49-382c-8933-7a25bc551404 | -12.75265 | -47.29764 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bcd0685f-dda0-3218-b10c-9582f6af79da | -11.90694 | -47.02079 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dabab885-6db3-3027-b15e-f04e944ea9e4 | -15.82049 | -42.52051 | 2026-09-28 16:24:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 0d6e93df-98cd-3dc0-b569-199d5756ff57 | -11.89764 | -47.01431 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bcd9aeb5-f5c5-3c27-8441-e328f3a10cea | -12.79287 | -54.07548 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 20e94c61-959f-34b7-8c56-75ba275df87a | -12.59034 | -51.94113 | 2026-09-28 16:24:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e43c72f1-84e1-3bc8-a00a-8238976150d9 | -13.97284 | -53.97494 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 269b930f-320b-3c41-b221-60ab862ccdb4 | -13.34958 | -51.32986 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 93be2599-137d-38a1-b6b3-7be548c25174 | -15.40712 | -47.94035 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 225352b0-8e1e-3aaa-a880-a3d1d38b3190 | -16.11843 | -41.61485 | 2026-09-28 16:24:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| bbd8980e-2e9d-3ca0-b394-9444fc41e235 | -11.87091 | -47.0997 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0f0e3ca9-3954-300b-b3f3-10fe84cb43d2 | -12.31505 | -50.27333 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6b5b1a22-fc65-3c12-b5a8-6af3a8713293 | -14.46366 | -40.5832 | 2026-09-28 16:24:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c9397863-e02f-37e7-b817-92fc186ba629 | -15.40152 | -47.90305 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 39866ef1-c240-3a16-bdc7-b9e3dc28fa91 | -11.86008 | -47.08171 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 264df940-476e-3c47-899b-7ce9c6e72886 | -16.34164 | -47.7007 | 2026-09-28 16:24:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 638696e3-1d8e-337f-b890-bebca6b0eaab | -11.71445 | -43.46191 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 8eede35e-ebc3-3152-832d-240c756f8235 | -15.07942 | -54.62239 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 466f6e6e-524f-3503-88c7-e495b37e19ed | -11.87457 | -47.09531 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 8d862e17-4c72-39fc-8202-b24458429dd2 | -14.08895 | -46.32853 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| beabe7b1-2614-3052-b82b-af105ac2bef8 | -15.17007 | -39.82289 | 2026-09-28 16:24:00 | NOAA-20 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 220cd374-e512-3382-973e-dc87b9ceb040 | -15.1495 | -44.02797 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f48dfeeb-4013-3c33-9c04-9e4a89c8ab6a | -15.40271 | -47.90525 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 57e878d1-0264-3f05-b956-7599fd154fdb | -11.90893 | -49.98515 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e80f8051-8255-3b8d-bff2-55126195c3ca | -12.28715 | -50.26073 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 26e58d6b-129f-35af-8c70-312f70039381 | -11.21501 | -44.76254 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5a81ed9d-bda0-3889-ab6b-672761533982 | -11.63209 | -43.49708 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f3d254d6-1b7e-3ed8-9c38-8276150ac90d | -11.51395 | -47.39781 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 31dffed5-87eb-3a69-a94d-4f761e834796 | -16.34864 | -42.57419 | 2026-09-28 16:24:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8930cde0-e0f4-3594-ab46-da63ed480a6a | -12.43896 | -48.22304 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 02cf8759-7592-3460-a958-e74c6196663e | -11.66841 | -43.5301 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 09c1fce2-9821-364d-a192-38279b4169d4 | -15.20554 | -46.16421 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d902cb38-2ec4-3988-b3d3-1591cfa13902 | -13.21385 | -51.77628 | 2026-09-28 16:24:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1af470c2-6b71-3cf7-9059-3e32be26da2d | -12.15758 | -50.38389 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a9902498-657c-376d-be35-b5f6071abdf9 | -11.44892 | -44.91574 | 2026-09-28 16:24:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 50223a9a-0477-3f8a-a2e9-6f2d42461f1c | -16.50625 | -50.37757 | 2026-09-28 16:24:00 | NOAA-20 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aca28a59-d1db-3a74-99d1-357e2365f3f6 | -11.05654 | -42.9905 | 2026-09-28 16:24:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 29.1 |
| 26420fca-1fd9-364e-af8e-08112c508162 | -13.53712 | -40.84685 | 2026-09-28 16:24:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 32ab67cd-3b72-3f18-9420-c4da857bcf3c | -15.07339 | -54.60934 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 3e4bf2b8-52dd-31f5-8c5d-1bca33d75738 | -12.37941 | -50.23942 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 1b3b1702-768d-3a32-b2b8-43c0c5b08e8f | -11.37872 | -43.38984 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4b8b28ce-65f6-39b4-844f-0e83d96c5836 | -12.36969 | -50.23394 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 51e177bc-d977-36e9-bac2-b4ae5e064ac2 | -14.1382 | -41.45237 | 2026-09-28 16:24:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| de0a85f2-2541-3e8d-9e15-9dbc1822b91d | -12.38526 | -50.23196 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| b2d0d4b3-1565-3e16-9a19-49b191aca01c | -11.90931 | -49.98815 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1ab5522c-c30c-371f-ab86-4b52f21f6b89 | -11.77444 | -47.05534 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e2893bee-b48f-3938-9143-4d1c00cf1ca4 | -12.79562 | -50.58569 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 92de4969-5240-381c-975a-cbd586b05a93 | -12.74732 | -47.28991 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a77d78f2-ce14-38e0-a691-aea99044d7c2 | -11.543 | -47.39 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 047fdcc1-ec36-34ab-91ab-02175331a0a3 | -11.39307 | -45.41671 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 07a3269a-b2f8-3e70-8860-3747fe30aadb | -14.60532 | -40.95321 | 2026-09-28 16:24:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| e06dc64d-1112-31d9-8d51-32c9fce49911 | -15.87631 | -40.76737 | 2026-09-28 16:24:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a8aea960-c8c3-3fae-a6e1-4b76732c825a | -11.3764 | -43.39779 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 6c5632f1-15ba-35f3-be30-c51f5e342978 | -11.68451 | -44.53188 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| edd20f00-9f36-3e6d-99f6-78ccf9bed623 | -12.43595 | -48.22537 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 76f781e7-271c-3e85-835a-5148de979d7e | -15.19979 | -46.18468 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c8841a44-feb8-30b8-a7cb-a18a6c6fd1e6 | -16.35207 | -42.57359 | 2026-09-28 16:24:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| f41cbd06-0e67-3746-87e6-4d0b2af4c356 | -11.91136 | -49.92428 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0b836caf-077d-33f0-8562-1c7414c38dd9 | -15.34274 | -42.16741 | 2026-09-28 16:24:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 8db546a4-2a51-34e1-9710-117d8cced59c | -15.15963 | -43.60532 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 52.8 |
| eb42afa2-f703-344a-8c5c-553cf01931ea | -17.5745 | -46.91326 | 2026-09-28 16:24:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| efc80400-6d39-3506-a684-7430796e33a6 | -12.06436 | -48.5345 | 2026-09-28 16:24:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| f5aff696-d7cf-3b84-b86d-0e495233185a | -15.13715 | -43.62558 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 39.8 |
| a500da85-d5ed-3196-8fa9-1f96365727a0 | -11.50077 | -47.36335 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a226b82a-ba96-3c2a-a3e2-a239de5e4b5c | -15.58954 | -47.91072 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 5ccb9af0-6c75-341a-b711-3f2ed217b250 | -11.45335 | -44.92675 | 2026-09-28 16:24:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cfae0117-9ddb-3700-9d4f-a620be51858f | -11.21647 | -44.7611 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6e12c1ca-6cb8-3125-b0b5-7daed05c79f2 | -12.97315 | -51.08467 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 78b562cc-84c5-3be7-ac7d-34a7d7eb032c | -13.3294 | -46.80831 | 2026-09-28 16:24:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| e5fac750-b4b0-32b7-abd5-ed13e5c94614 | -11.49661 | -47.33208 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 2967b6ef-2036-3c47-a98d-73ee06a87bd7 | -13.36527 | -40.96537 | 2026-09-28 16:24:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 98301cc4-0861-3548-ba83-6a44d30c3f9e | -12.70207 | -47.33322 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 5ec19a11-84cf-325b-973b-496d0647f7a1 | -14.49266 | -45.23442 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 19af5101-da46-3284-a140-e95c3653f573 | -13.08862 | -47.45224 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a23d876f-4203-334b-bc76-be086d375c1b | -15.46526 | -46.15294 | 2026-09-28 16:24:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d3f85b2b-a533-3c24-b7d6-964f6c41c238 | -15.6804 | -47.59365 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 27.0 |
| c4cdf255-98df-3b5c-8edb-37a5f2949a58 | -16.15184 | -42.07887 | 2026-09-28 16:24:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| a850b169-0f2d-3650-9cfe-45bac4341d80 | -11.69379 | -43.48811 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bca4c156-a3fe-355c-9d58-c91cf145a1b3 | -11.51236 | -47.38592 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8e4a8a58-a355-3514-99d4-fc7645d34d48 | -15.68556 | -47.59798 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 20.4 |
| a3790eae-4a66-31fe-80c3-73f0c56dcd8b | -12.37488 | -50.23328 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e4a32924-57e3-3aef-b653-8c2daf64596a | -16.69248 | -50.66632 | 2026-09-28 16:24:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 033315b1-b585-3fbc-add0-c3279a663b4c | -12.79821 | -54.02148 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 1a3e777b-1012-3cf9-ac98-4484b02ec6bd | -15.4486 | -41.44025 | 2026-09-28 16:24:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| ff0d9f72-33bc-36ef-a929-01275c0d7520 | -12.37821 | -50.22993 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| aa3a5e0c-dd88-3c97-8e86-8afa6915d370 | -13.59008 | -51.45118 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 5c2c421d-dba1-3140-816c-ad3b471e7889 | -15.26518 | -47.63082 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f319dbb9-2a19-3155-a875-b9e893abe024 | -12.43257 | -44.16337 | 2026-09-28 16:24:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |


[Clique aqui para ver as próximas entradas](README98.md)
