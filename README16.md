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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6008d69a-fb9d-3555-be2b-d1ce32e310ec | -5.91219 | -46.24876 | 2025-11-11 04:50:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 69f7bbd0-6f4e-3de1-ad21-98ed152085e8 | -1.64439 | -52.05096 | 2025-11-11 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21b7e423-e928-3e8e-8e21-ac6e86cc3f4c | 0.27879 | -50.31701 | 2025-11-11 04:50:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf7ef674-e1fd-3b24-8e8b-8a62da59d845 | -6.0933 | -41.5732 | 2025-11-11 04:50:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f3e06b0d-5446-35db-84dd-eebf2900e4f4 | -3.89772 | -52.28597 | 2025-11-11 04:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7af4473a-68fd-3fb4-845e-390603073fd5 | -4.73818 | -49.52702 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbde63e7-80ba-3c1d-8980-d13c24c81321 | -3.44639 | -45.53204 | 2025-11-11 04:50:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6e2c87b-21fe-3f06-8559-db424813558b | -6.95477 | -46.35295 | 2025-11-11 04:50:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3001c499-4336-3f81-a559-7e09749ff0e8 | -4.72403 | -46.44779 | 2025-11-11 04:50:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 2a7d112c-cac3-3ac1-b496-e3ce3047c42e | -4.86684 | -46.68511 | 2025-11-11 04:50:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 319593cd-e2b9-311c-bcc9-8237063aee60 | -4.12498 | -52.07494 | 2025-11-11 04:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d21dbaf5-e3c8-3642-b3aa-66ecc27ca074 | -0.85172 | -48.66503 | 2025-11-11 04:50:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47a72c0e-b73f-3b1e-bef0-fa541ec3603b | -2.72069 | -48.34798 | 2025-11-11 04:50:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6f99f2ee-bc50-3ff6-8295-3467b89a0e32 | -2.87175 | -45.43122 | 2025-11-11 04:50:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3391eb88-79b3-3ee3-882a-fb11b7b7b182 | -4.74168 | -49.52762 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd5ef881-cc04-3e6c-b053-067959c4727c | -2.64027 | -49.21655 | 2025-11-11 04:50:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30d3cefd-fd3d-3e7c-914a-47c741adc9ce | -3.63738 | -44.63004 | 2025-11-11 04:50:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 919bd42a-3e38-369c-a0bf-96b130de6ff6 | -5.49138 | -44.03075 | 2025-11-11 04:50:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 432b8061-1336-36f3-ae6d-a1985a5a752c | -2.48306 | -50.25512 | 2025-11-11 04:50:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d57ca32b-f116-320d-b264-4b36bddb9473 | -7.27355 | -42.16693 | 2025-11-11 04:50:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8ad8021e-6316-3769-9f61-27e2d6cfda53 | -4.32144 | -50.76688 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0544068f-6ea6-3fce-9a2f-23dc33f6b1f2 | -4.67973 | -43.24609 | 2025-11-11 04:50:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| baa3a17c-96a7-3bc4-b8fd-3435773fbc8d | -4.87096 | -46.68586 | 2025-11-11 04:50:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ab6b1c0-e11a-3b32-956c-ffd557fb19e5 | -4.90951 | -44.33362 | 2025-11-11 04:50:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fe257964-e845-3e1b-b1b6-9ab4c2f707b5 | -4.43936 | -45.51957 | 2025-11-11 04:50:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 463740cd-6a94-3313-a652-44a40596e26b | -0.91017 | -47.55168 | 2025-11-11 04:50:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38ff4602-8320-3fe7-b683-7d0e67f2dceb | -6.06983 | -45.80968 | 2025-11-11 04:50:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c478ef3-c937-3a0d-9c8e-a7ce63c7b621 | -5.40501 | -45.24422 | 2025-11-11 04:50:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f22d7ee-1ee2-30fe-9db3-4fc5426c6f73 | -4.90541 | -44.32764 | 2025-11-11 04:50:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3397bc75-6962-3436-9ca5-4ce41506020d | -2.64086 | -49.21271 | 2025-11-11 04:50:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f01c37fc-5a8b-3ab0-a7a7-1a41bcaa1767 | -3.77664 | -47.95019 | 2025-11-11 04:50:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b89a281-b299-3677-8e59-36a34e940eb1 | -4.72289 | -46.4554 | 2025-11-11 04:50:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0bcc98bd-7f7d-38a7-b02c-b7a31e531365 | -4.91029 | -44.32828 | 2025-11-11 04:50:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 710600ef-654b-39ef-a6b9-38276c836ad1 | -2.44081 | -46.31064 | 2025-11-11 04:50:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbd3dc0f-f515-385d-99b2-4e82c1162486 | -6.79032 | -47.5922 | 2025-11-11 04:50:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0ee6d48-72c5-3960-b9d2-c3405d027097 | -7.27409 | -42.16294 | 2025-11-11 04:50:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 38bcb920-ca3d-3b40-beed-7c0e4f41bd59 | -3.96567 | -49.29153 | 2025-11-11 04:50:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89f7ee66-cabb-3945-90db-9786939f1240 | -1.64493 | -52.04751 | 2025-11-11 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69e0b2b2-987f-3294-8000-865c596961a9 | -4.20347 | -50.63287 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2304b1c0-7d7b-3765-8f73-a68e98aa7cff | -4.60045 | -45.48996 | 2025-11-11 04:50:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fc5c3b1-5040-377a-9adb-a305e91a8486 | -5.40565 | -45.23977 | 2025-11-11 04:50:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0f7f6fa-edc0-3b66-97e4-551861e4a0df | -4.68011 | -43.24867 | 2025-11-11 04:50:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 356b5e6e-c354-3438-ad6c-17ce795d452d | -2.48977 | -50.25615 | 2025-11-11 04:50:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0014fde1-1cc8-3fa1-bcad-4906ff1999ee | -3.8162 | -46.00679 | 2025-11-11 04:50:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07be98ef-370e-3320-b90c-d1a31ab5b3e5 | -6.08789 | -41.56842 | 2025-11-11 04:50:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8c725d1e-d3f2-3968-97d7-7318b00dcd3f | -4.20683 | -50.63339 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be108a75-5f38-316e-9e19-320aefb455b2 | -3.88696 | -47.17802 | 2025-11-11 04:50:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e11d3dc-7ed7-3034-aa70-a6d059428e4f | -3.88768 | -47.17684 | 2025-11-11 04:50:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac2be394-b1b2-3bc8-ad34-9904920973f7 | -1.49252 | -60.23125 | 2025-11-11 04:50:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11dcefdf-9b2b-312a-adbc-e9d346fa12cb | -5.4037 | -47.25511 | 2025-11-11 04:50:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fee12f5-7584-3eea-b383-d6016335fcb6 | -4.68056 | -43.24544 | 2025-11-11 04:50:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b2c587b1-0c5a-36ff-bbb5-5578fe938372 | -4.17359 | -43.82956 | 2025-11-11 04:50:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5568e9c8-10c0-3300-98bc-4ac507f65cb1 | -4.72346 | -46.45159 | 2025-11-11 04:50:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 195c1300-8bef-3e61-807f-b41f5d144c5c | -2.66164 | -45.42045 | 2025-11-11 04:50:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53f83426-655e-36c9-9ff0-59556b77b039 | -3.71598 | -50.63741 | 2025-11-11 04:50:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08875307-ffde-3233-8d5c-901271e21f05 | -3.72015 | -47.62655 | 2025-11-11 04:50:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d68b5e9-9217-31ec-b5da-fa4764851d8d | -2.48587 | -50.25919 | 2025-11-11 04:50:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f30b020-e3ee-3a77-862c-ed249fcfd3e7 | 0.78711 | -50.23726 | 2025-11-11 04:50:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1a137ef-8552-3466-a6a3-f832cca5804e | -5.49179 | -44.02785 | 2025-11-11 04:50:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88b645c8-580d-395c-8686-1d9ca10c420f | -4.8704 | -46.68968 | 2025-11-11 04:50:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 600461d8-081a-3272-abb0-420e5f979c99 | -5.38134 | -46.36338 | 2025-11-11 04:50:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34310c3f-1368-3c97-ac40-7f65917f8abb | -4.91915 | -50.00021 | 2025-11-11 04:50:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d3992a8-de7b-3c2d-ab95-869aec0677a5 | -5.60769 | -47.28456 | 2025-11-11 04:50:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24cd95c2-cad8-35c5-8a3b-dd25754e1e88 | -3.70136 | -43.51702 | 2025-11-11 04:50:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ab15d15-8f63-3660-8374-01b2ca68ba5a | -4.3209 | -50.77043 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39bf0976-cb88-356c-9a65-61f5403cecca | -4.44074 | -45.51036 | 2025-11-11 04:50:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a70b540f-9565-3431-ad20-67acc43e6fad | -0.795 | -48.65257 | 2025-11-11 04:50:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af77e79d-81c2-34a8-87fc-b26f9d0ea19f | -2.10121 | -56.64137 | 2025-11-11 04:50:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15575c3f-9d6a-3f23-88ce-370254b986b4 | -3.45077 | -45.5327 | 2025-11-11 04:50:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 131f9010-0470-3f03-8b1a-a1f10ed3effe | 0.85794 | -50.0812 | 2025-11-11 04:50:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c15f7ef1-55f5-3c84-9709-918f95c073be | -2.48848 | -47.49719 | 2025-11-11 04:50:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a07edf25-0b09-3738-bb0f-a2875d859a3c | -3.21257 | -43.32452 | 2025-11-11 04:50:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3fe1a1c-ca20-344e-b510-e26ecebb2c19 | -3.76415 | -50.76773 | 2025-11-11 04:50:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5d081dd-2b4e-3a43-aeda-2e102efe857f | -4.1426 | -50.64894 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdb64e75-b810-3aa1-b6df-aeb3ffe9d4c4 | -6.08731 | -41.57259 | 2025-11-11 04:50:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9dc08ba2-1348-3534-8fab-aec4e451249a | -1.64162 | -52.047 | 2025-11-11 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5d799087-0cbc-32cf-9481-cb7d4f7850d3 | -3.71632 | -47.62601 | 2025-11-11 04:50:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8a86022-5687-3e93-bbdd-abd3ee540d4d | -7.29536 | -45.06608 | 2025-11-11 04:50:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7518716-49e7-34e7-8240-12f8002ca88b | -2.48642 | -50.25564 | 2025-11-11 04:50:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d088d816-80bd-3ec3-9a20-3ebfeacbb370 | -2.49032 | -50.2526 | 2025-11-11 04:50:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb7e4559-2262-371f-8a0d-5d466ab5404d | -4.2794 | -50.5345 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b979a07-4f5c-39bb-9c6e-eba5a33572bc | -4.64344 | -50.37923 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13faab56-b306-3dc6-bfd2-f6d6a9156a97 | -5.3856 | -46.36399 | 2025-11-11 04:50:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4b88406-c59b-3002-8c93-09d91a754154 | -1.33839 | -50.65834 | 2025-11-11 04:50:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cf2cb48-d26d-3bd9-b740-6dd5aa201ad3 | -2.48697 | -50.25208 | 2025-11-11 04:50:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f2fe610a-8431-3da3-94be-0b0589bde30b | -4.26192 | -49.03548 | 2025-11-11 04:50:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d268348c-3fdb-3b48-8aa7-41d83f3c1c1b | -2.6708 | -48.3101 | 2025-11-11 04:50:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84291465-7cf0-3ac3-9a2a-03d9af0849cb | -4.71982 | -46.44724 | 2025-11-11 04:50:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 7c3dd941-29d4-3532-bea8-07310dc5d1f6 | -4.27659 | -50.53035 | 2025-11-11 04:50:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07a9c2c8-f1b2-3b9c-bc4f-ae20cd64b0d0 | -1.64108 | -52.05045 | 2025-11-11 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3c925c7a-df00-3be4-9c5f-e9c4e942745f | -2.40479 | -55.58139 | 2025-11-11 04:50:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9762ea4a-c76c-39f2-b2c8-f1a1e19c3f46 | -2.09031 | -47.28851 | 2025-11-11 04:50:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae1e256d-adc6-3409-b903-4476822e1788 | -5.12455 | -45.59712 | 2025-11-11 04:50:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63fa3926-8aaf-36ac-8330-49a6dbea5a61 | -2.10179 | -56.63779 | 2025-11-11 04:50:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d52c3bd-288f-34fa-a4ac-3c040860208d | -3.95442 | -50.52498 | 2025-11-11 04:50:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3ab8cb2e-e445-3d57-926c-a8cbedcfc4bd | -4.90618 | -44.32231 | 2025-11-11 04:50:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7838de8a-88b6-339f-bfdb-1ee45be1d3b2 | -6.09389 | -41.569 | 2025-11-11 04:50:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 28f9cbc9-62c5-3cba-8574-c621d268213f | -4.11281 | -48.72938 | 2025-11-11 04:50:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 835f2a21-c74e-370b-8366-277bd05eba1a | -3.84538 | -50.74807 | 2025-11-11 04:50:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e61eb46f-40d6-3874-af72-38f17555a548 | -2.64374 | -49.21709 | 2025-11-11 04:50:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README17.md)
