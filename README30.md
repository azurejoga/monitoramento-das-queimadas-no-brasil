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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b45318af-6c69-3b36-94e7-86b8f902db18 | -11.5779 | -52.115 | 2025-06-27 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 209.4 |
| f4c569cf-fcb5-3b8e-9d97-e6eddf67d641 | -6.9793 | -42.8798 | 2025-06-27 05:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.0 |
| 4b650159-f466-3816-9b03-25db6d45ddaa | -6.9791 | -42.9034 | 2025-06-27 05:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 160.1 |
| 8e58b947-7db1-36cd-b618-80897704343e | -11.5782 | -52.094 | 2025-06-27 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 9becd137-f2f4-37af-89bb-706559f77867 | -6.9416 | -42.8834 | 2025-06-27 05:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.9 |
| b62a18ab-a645-3d8e-b989-bbb742733efb | -11.5782 | -52.094 | 2025-06-27 05:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 5265eb59-e178-3b97-9253-050c2e69ea1c | -6.9793 | -42.8798 | 2025-06-27 05:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 142.7 |
| 36cf9c5a-d905-3c2d-9058-31efbc3ebf41 | -6.9791 | -42.9034 | 2025-06-27 05:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.3 |
| 81056bd0-4f69-3290-a168-170e57d023c4 | -6.9602 | -42.9052 | 2025-06-27 05:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 225.1 |
| f35d0724-0cea-32c1-9f25-7e4b638d4251 | -11.5779 | -52.115 | 2025-06-27 05:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 220.5 |
| f4c89355-f052-397f-a432-e2beca478688 | -6.9605 | -42.8816 | 2025-06-27 05:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 249.5 |
| 81c3284d-eade-34d4-8bf5-5ba0fbe241e5 | 2.74884 | -60.36676 | 2025-06-27 05:57:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8dbe73d2-4393-3717-adce-a3ff0e457868 | -11.5779 | -52.115 | 2025-06-27 06:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 193.0 |
| 0859c062-4161-3dcd-8a3d-9a3add3d14e8 | -6.9793 | -42.8798 | 2025-06-27 06:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 141.5 |
| 903412ad-bf26-357b-b53a-3e6d8f13a311 | -6.9791 | -42.9034 | 2025-06-27 06:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 144.8 |
| 59001902-6168-3c78-a5ce-f9e422bd841e | -6.9416 | -42.8834 | 2025-06-27 06:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.0 |
| 19d076b7-96ae-3b41-bd13-5c9a9330fd01 | -6.9602 | -42.9052 | 2025-06-27 06:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 232.2 |
| 351f6548-72b3-35dd-a1d0-43de79e420a6 | -6.9605 | -42.8816 | 2025-06-27 06:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 245.9 |
| f293d8ce-d468-3d7e-81cf-64788a359ebf | -11.5782 | -52.094 | 2025-06-27 06:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 85ecb655-56c3-3eb5-8d9b-cb070d90e8ce | -10.71457 | -59.1312 | 2025-06-27 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cf0356d0-e627-368c-a6c8-afff824934a3 | -9.17234 | -61.40661 | 2025-06-27 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19659a5b-e483-39aa-ad6e-765e00cc2031 | -11.50456 | -61.82577 | 2025-06-27 06:01:00 | NOAA-21 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70d3d7c2-f4ef-392d-befb-eeb40e6797d8 | -10.29648 | -57.12897 | 2025-06-27 06:01:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8920b7a4-1789-35ac-922e-3b52df5b2f49 | -10.30281 | -57.13703 | 2025-06-27 06:01:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d5f07297-2990-3ef5-861c-478a34b96f3a | -10.29996 | -57.12651 | 2025-06-27 06:01:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 332ba2d0-cec7-388a-a06c-402ac8ff70eb | -10.717 | -59.12601 | 2025-06-27 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 52fdfd55-52a6-3db6-b966-b85f99d0d22d | -10.70824 | -59.12992 | 2025-06-27 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 84b6a936-5695-3ad4-920c-350c60cc8830 | -11.50498 | -61.82228 | 2025-06-27 06:01:00 | NOAA-21 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99329a6b-a39d-3e8d-8868-07364b86cb36 | -10.30554 | -57.14188 | 2025-06-27 06:01:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a5562b55-c38a-363d-ba91-265116cf57ac | -10.71006 | -59.13003 | 2025-06-27 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 59f6ea9d-0884-3075-8ee6-60500f42ac49 | -10.71395 | -59.13638 | 2025-06-27 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 771dbee2-10b5-3925-a937-3d6aa7123f35 | -10.71522 | -59.12583 | 2025-06-27 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0aa70a7a-a868-3970-91ea-25bab95e0e7f | -10.71581 | -59.13654 | 2025-06-27 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3e6c1087-017e-307b-8e02-98ad2c891595 | -9.53393 | -63.57417 | 2025-06-27 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe9a43f8-aba7-302e-99ba-d83e47f27eec | -10.30364 | -57.12986 | 2025-06-27 06:01:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eb75dc96-e2f8-39ae-9db3-9ecefa9be8f5 | -10.81314 | -57.75461 | 2025-06-27 06:01:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 75b8ee30-89fa-3212-9212-44db7af1e222 | -10.29565 | -57.1362 | 2025-06-27 06:01:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 80bd77ff-ba2a-3ecd-a119-a9dee5144ce0 | -10.81351 | -57.75397 | 2025-06-27 06:01:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a34af5ce-5221-3c98-9a57-3898580bf969 | -9.2383 | -63.62323 | 2025-06-27 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db5ca9ed-daa1-34f8-8de0-3c0a8ccd6428 | -10.29916 | -57.13381 | 2025-06-27 06:01:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4d366888-2dd3-3c2a-a4e3-eb43159b4931 | -11.83227 | -62.76543 | 2025-06-27 06:01:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06d76658-f132-3750-a780-d250cba88544 | -9.17455 | -61.40566 | 2025-06-27 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a344420c-a0d6-3813-9df2-13a62d2b6e35 | -11.50413 | -61.82926 | 2025-06-27 06:01:00 | NOAA-21 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 136bf821-736b-391f-9e54-a22faac8b5a7 | -10.70946 | -59.13532 | 2025-06-27 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 77561c39-c8e5-32c0-8647-399956129e90 | -10.7164 | -59.13137 | 2025-06-27 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d2ba9fa-a711-3214-99e1-b8a5e61f858b | -9.52924 | -63.57348 | 2025-06-27 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d0760f3-ce4b-3090-a7c2-f331ce1a7dfa | -10.30712 | -57.1274 | 2025-06-27 06:01:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 91b095d3-cb43-3d0e-b774-439f1bc1ac48 | -10.30633 | -57.13461 | 2025-06-27 06:01:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4555f707-1199-3a19-997d-cbc3d2a0c833 | -9.53119 | -63.57777 | 2025-06-27 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 869a4a7b-f4e1-39f0-8fe8-b9b05ba0fffe | -10.81273 | -57.76058 | 2025-06-27 06:01:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 37d6322d-98bc-39f9-baaf-2d50943f902e | -10.7076 | -59.13524 | 2025-06-27 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 75f5b3f4-81f0-37f3-95fe-472d2a037522 | -11.83189 | -62.76854 | 2025-06-27 06:01:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 599efd65-b284-390d-9521-d06b24e749b0 | -14.31491 | -59.89668 | 2025-06-27 06:03:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e4afc9ba-e20b-3b38-a69f-bebb7d83c19c | -12.2882 | -63.74417 | 2025-06-27 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a05ca6ea-5c8c-3e0a-9855-3c5ebefef97c | -12.30982 | -63.73565 | 2025-06-27 06:03:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a43dae6-28d4-31cf-af80-f1306c963fc8 | -11.5779 | -52.115 | 2025-06-27 06:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 176.3 |
| abe6675c-cf66-305c-af44-1c246f910e37 | -6.9791 | -42.9034 | 2025-06-27 06:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 164.8 |
| 4b563471-3a28-3322-af09-05b0f3755c81 | -6.9605 | -42.8816 | 2025-06-27 06:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 197.9 |
| 5921d2a9-7012-377c-90fa-e0408b5c275b | -11.5782 | -52.094 | 2025-06-27 06:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| d15bf5e8-bcad-3196-871d-343bc40d700f | -6.9602 | -42.9052 | 2025-06-27 06:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 277.9 |
| b3d1fd1b-5839-3986-a7a4-4b13a01dd26c | -6.9793 | -42.8798 | 2025-06-27 06:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| 0748fb24-e15e-3271-b6cc-013b6af2a068 | -6.9793 | -42.8798 | 2025-06-27 06:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.8 |
| 11879499-086a-3d62-b939-0030af9e154f | -11.5779 | -52.115 | 2025-06-27 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 167.1 |
| d0de08c9-c2ac-3300-8f94-e59bbe11c083 | -11.5782 | -52.094 | 2025-06-27 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| d768b3bb-62af-3709-8f6a-24e0965e0d78 | -6.9791 | -42.9034 | 2025-06-27 06:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 151.8 |
| 6325132e-e980-3cc2-8ee9-5853900f5313 | -6.9602 | -42.9052 | 2025-06-27 06:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 247.4 |
| 1d2db7a5-0f96-3971-bd79-a7de0168065c | -6.9605 | -42.8816 | 2025-06-27 06:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 227.9 |
| cc017446-b2dc-3c40-8cce-e07ca4222a65 | 2.75275 | -60.36628 | 2025-06-27 06:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2cfdda63-583c-3a42-897d-c8749117a61a | 2.75328 | -60.36412 | 2025-06-27 06:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be09de6d-e00c-3fcc-a0a0-f9124a6e34de | 2.75456 | -60.37133 | 2025-06-27 06:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8bea1acd-32dc-38c0-8529-77383f669a4f | -6.9793 | -42.8798 | 2025-06-27 06:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 118.0 |
| af95a794-bf56-3f20-a2ec-289e459b17e1 | -6.9602 | -42.9052 | 2025-06-27 06:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 250.4 |
| fb1d9e85-385c-36e2-8d71-ca0ef561a725 | -6.9605 | -42.8816 | 2025-06-27 06:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 274.8 |
| 829f56cf-b74b-38eb-b39f-f16b941a4845 | -11.5969 | -52.113 | 2025-06-27 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 30d0c512-c513-3405-9d9a-ea8b843b9d68 | -11.5779 | -52.115 | 2025-06-27 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 7192c498-40b8-307f-8239-7df90593f478 | -6.9791 | -42.9034 | 2025-06-27 06:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.8 |
| 4906608f-bf7a-3b55-9cc8-3efcfa5a9800 | -11.559 | -52.117 | 2025-06-27 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 859ab0d1-3577-347d-bad6-dbaef4807e9a | -6.9793 | -42.8798 | 2025-06-27 06:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 117.0 |
| 84d616e2-33fb-390c-99d1-a56a869ccfd4 | -6.9791 | -42.9034 | 2025-06-27 06:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 171.8 |
| b94c5d3f-86d9-36ca-bc10-ee74c42b67a1 | -6.9605 | -42.8816 | 2025-06-27 06:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 186.4 |
| 9e5abeb8-bf5d-350b-a541-497daf777852 | -11.5779 | -52.115 | 2025-06-27 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 154.5 |
| 254f4eb0-ed3c-3a24-afda-479da909b7d7 | -11.5782 | -52.094 | 2025-06-27 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 3317f7c8-54e3-342e-8e2a-aa7620a42ba2 | -6.9602 | -42.9052 | 2025-06-27 06:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 256.2 |
| d90802cf-a808-3519-ad77-d7adefd3ded3 | -6.9605 | -42.8816 | 2025-06-27 06:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 182.2 |
| 6846f656-1ec5-3ca4-a24e-56e0fe561daa | -6.9791 | -42.9034 | 2025-06-27 06:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 175.9 |
| b5ba0384-a7ed-395a-90d1-4f846cd52c29 | -6.9793 | -42.8798 | 2025-06-27 06:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 120.1 |
| 36c0d449-8a06-3650-8ceb-217107839c9a | -11.5782 | -52.094 | 2025-06-27 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 4185e5ea-466b-343f-8c1d-69d4920813b7 | -6.9602 | -42.9052 | 2025-06-27 06:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 249.6 |
| a10d7e2e-b053-37aa-b730-1b72a2934dab | -11.5779 | -52.115 | 2025-06-27 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 2b1e0ad7-2bee-3c5d-aebf-a39cd915d227 | -11.5779 | -52.115 | 2025-06-27 07:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 122.9 |
| a7f1f4fc-df18-3105-9ff3-8ffaa004b359 | -6.9793 | -42.8798 | 2025-06-27 07:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 126.9 |
| 03dfd352-48b1-3b97-87e5-ac78a768e987 | -6.9605 | -42.8816 | 2025-06-27 07:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 251.8 |
| 3ba4bb47-b721-36b2-86c1-c1f65367775d | -6.9791 | -42.9034 | 2025-06-27 07:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 128.7 |
| e83dba7e-6f3f-3295-bffe-889a0ff022d3 | -6.9602 | -42.9052 | 2025-06-27 07:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 233.7 |
| f09ba06c-72e1-313f-bf62-d3ad78cf6ba8 | -5.93161 | -68.82304 | 2025-06-27 07:07:00 | AQUA_M-M | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 260d85dc-3026-390f-b718-2a5c68d97083 | -6.9791 | -42.9034 | 2025-06-27 07:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 153.5 |
| 969c6ff7-6c5d-37b3-b04d-d39bbfac661a | -6.9793 | -42.8798 | 2025-06-27 07:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 125.4 |
| 80e3a875-8a5e-3e0a-aa8b-4f4d5bf80d5d | -11.5779 | -52.115 | 2025-06-27 07:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 124.7 |
| fa8af6ab-c25c-3ad7-a4cd-9e116db9cfe6 | -11.5782 | -52.094 | 2025-06-27 07:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| f74e786a-fa11-3a6a-85a6-65a64ffac5c8 | -6.9602 | -42.9052 | 2025-06-27 07:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 221.3 |


[Clique aqui para ver as próximas entradas](README31.md)
