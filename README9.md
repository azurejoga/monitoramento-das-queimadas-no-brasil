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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c069c0f1-0061-3fb6-96c6-24f1834f2799 | -1.75788 | -54.1895 | 2024-12-05 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5b8c8ddc-4683-3804-a729-3a5964e3f9ea | -1.68963 | -52.51586 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39ac2792-a19e-30d3-9d7c-beff1cc22211 | -1.03367 | -53.55787 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd555f06-3413-33d7-837c-18590d1e1f16 | -1.17336 | -53.42958 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10d37033-1e31-37c9-a6e7-3c0aa8163fb9 | -4.40251 | -45.92974 | 2024-12-05 04:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9130ddd3-5a8f-3d04-bdd2-db958e1b7bb1 | -3.51174 | -54.55601 | 2024-12-05 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91950b73-3f89-30a5-b4d0-390ab2d836fd | -6.29809 | -46.44537 | 2024-12-05 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 238b407e-c282-368c-9cca-47dd1165f6c1 | -3.25887 | -53.66428 | 2024-12-05 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 823676f0-be95-316c-b0cf-0e1544a3e5dd | -1.49484 | -52.52934 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7b42c43-5991-3556-8e28-962b393026e4 | -1.6298 | -52.36293 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5008566e-919f-309b-add2-d56cf9de670f | -1.14714 | -53.80901 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89b36266-c349-3951-9640-4aa302a2f5d0 | -1.25995 | -54.53833 | 2024-12-05 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 043090f6-ba10-30eb-92d3-4dbdbc6e6400 | -2.81706 | -53.06828 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e7ec784d-6abe-398f-b6ba-0033aedd8ad0 | -1.038 | -53.55416 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fe55513-3b8f-36cf-993e-70f024b84570 | -4.49284 | -50.23812 | 2024-12-05 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aef53db3-4e10-3e90-a3b9-6273bc16b6b0 | -1.16673 | -53.42429 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17d83271-e5e4-37e0-a027-fbff5220fa93 | -2.15985 | -54.61724 | 2024-12-05 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7dcb2850-0311-3b3a-8078-725c904b5d9e | -1.71308 | -52.45723 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 965dea12-b5ec-3ece-abf4-e67081a6fbf0 | -1.898 | -52.84706 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b20ad59-230f-38ef-88dc-e3c8d63a98b1 | -2.81417 | -53.06382 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7fa89020-f40f-3f9e-b638-911c5765b31b | -1.49531 | -51.9441 | 2024-12-05 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c97daa2b-9b6b-30b4-854d-631cc59dc867 | -6.29412 | -46.44477 | 2024-12-05 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df696a6c-1afa-3e77-8526-2480fd3d7f09 | -2.48089 | -54.03111 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9014e135-60d8-3275-9bcb-b2202c335516 | 0.70375 | -59.87809 | 2024-12-05 04:46:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecf77e6c-866b-3c5b-a7f9-b3131e7bc68c | -2.16605 | -54.628 | 2024-12-05 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1780a56e-0631-3c71-9624-2a4fb479dc6a | -2.74673 | -51.74989 | 2024-12-05 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acd4e43f-0d73-303d-b504-cf8853eec414 | -2.81479 | -53.0599 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 269a5620-e6d6-3397-93f8-f8b1ee83fd52 | -1.33078 | -52.56342 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2b70f2eb-de8b-3050-86ab-4c5fdf93e5ba | -2.82409 | -53.06936 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bca292ae-cba8-312a-b7d7-226cdf7cc596 | -1.3561 | -53.65245 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8009aa61-e876-3a74-b97e-8fb5b085164d | -3.1846 | -54.51457 | 2024-12-05 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b03d1ea-95e7-3b6e-94c0-ab2e5ded9df8 | -1.87802 | -53.29418 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6afa27a1-ea43-32ed-a730-49a67272b4dd | -6.94113 | -43.52497 | 2024-12-05 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf20a98c-acc8-391c-b730-d9ef70710529 | 0.70488 | -59.87485 | 2024-12-05 04:46:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edd512fe-10e5-3b64-8d73-3e59f76c6389 | -1.675 | -52.79013 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49c16314-5efd-3d2d-b29b-763b1f4741e2 | -4.44973 | -46.038 | 2024-12-05 04:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b03893c-a158-3245-abdc-8a1ae6621c8c | 0.16597 | -60.588 | 2024-12-05 04:46:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 27205eb9-feb9-36e6-9197-11a92a064cd4 | -4.64855 | -46.31844 | 2024-12-05 04:46:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f27caad9-e30a-34a1-96d5-cdfe5e7d5fe9 | -2.94975 | -51.40682 | 2024-12-05 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6123af98-d041-31af-b85e-deb849d26712 | -5.58294 | -45.16357 | 2024-12-05 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa1cca23-d6f6-3df8-8d0d-876ded7ad39b | -3.22287 | -53.11779 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 986c11cd-e029-38ce-afe9-9d8c77f44a9c | -1.07987 | -53.45436 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30360c65-a548-3d7e-9f52-e4fcc79ee20c | -6.93881 | -42.83093 | 2024-12-05 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3e8c38b0-702d-38ac-bc7d-821a0814755e | -3.63652 | -54.43846 | 2024-12-05 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13902ed8-51c9-3009-94e2-de6173e24239 | -1.68298 | -54.4462 | 2024-12-05 04:46:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 080e5e8c-ad74-36a8-a70c-b40c7c364ddf | -1.71131 | -52.78773 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbc84839-365c-3f4f-8461-75eebd497c85 | -4.08388 | -50.74596 | 2024-12-05 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52841511-f89c-3421-9f9b-4ca981b5cde9 | -3.18024 | -53.85328 | 2024-12-05 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 091d867c-6375-34e1-979c-06b9a2929cf2 | -2.52529 | -53.98251 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d51a242-c7e5-3bf2-900c-60f3ea9ca3c1 | -1.43635 | -53.8113 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e8445f28-04b9-3070-8346-49b6d14c78e1 | -4.66845 | -47.9244 | 2024-12-05 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5beaa57-aee5-3fc7-a99b-6b5d4993ce04 | -1.177 | -53.43019 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35a85c67-a4c4-3719-aaa4-f60ceb75004c | 0.75251 | -59.65596 | 2024-12-05 04:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae767c5a-d58d-32bb-8a3b-2ed241b9d5de | -5.58375 | -46.09087 | 2024-12-05 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07551dc6-fb88-3a3f-8c8a-5efda1531476 | -1.54501 | -51.64787 | 2024-12-05 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11d97482-6623-35df-8615-aece49c80999 | -1.74964 | -54.19275 | 2024-12-05 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16ed9a00-6092-3427-af50-74142f83e346 | -4.64928 | -46.31361 | 2024-12-05 04:46:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9408f8ae-58c6-32ee-90fe-c14046239d08 | -4.66548 | -47.91982 | 2024-12-05 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4ca25be-d852-3893-9b96-f72e8edc99cc | -3.45272 | -54.34854 | 2024-12-05 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bf631ab6-c00c-3279-ae29-4eb5678620fb | -1.76165 | -54.19012 | 2024-12-05 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 852ab03f-0adc-399d-93d7-37ff705c9bc4 | -4.63982 | -46.29668 | 2024-12-05 04:46:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0afcd2c4-69d9-39fc-b273-98d6d36c124e | -3.18543 | -54.51259 | 2024-12-05 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e3d6dafe-ca8b-364f-a5f5-2b7afb0a2cbe | -3.70936 | -53.75246 | 2024-12-05 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39037814-72c3-3da3-a2c4-9e8d96ad9599 | -1.71723 | -45.7842 | 2024-12-05 04:46:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 78adc9a0-7a59-3301-9766-db53b238edb9 | -1.67122 | -52.74563 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d30977b-ad93-30c2-9766-beed2847594e | -1.96555 | -48.38841 | 2024-12-05 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff97f0d9-fd7e-3d8b-8dc9-b5e68a0708f8 | -1.61936 | -53.83644 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cee9232-316d-39bb-b93b-ae4025f5b557 | -1.25918 | -54.54322 | 2024-12-05 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b31619a1-e080-37da-bd51-8525ede47eec | -1.88095 | -53.29882 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 765ad60b-9f87-31f2-926b-cd6aba9a0526 | -2.45522 | -53.97775 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86832b1d-d0f4-3ae5-a9e9-3a94368bf6aa | -3.18618 | -54.50803 | 2024-12-05 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d42520e-01aa-34e7-8e8c-2fdd0ff262d6 | -2.1699 | -54.6286 | 2024-12-05 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| f54520f3-8080-3365-9d4b-65b92d015b68 | -1.44006 | -53.81185 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 624d5653-b0b9-3531-9069-45f4294a9d98 | -1.08055 | -53.4501 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4596f6e-9079-3c0a-bac2-02d06649701c | -1.88067 | -46.38073 | 2024-12-05 04:46:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b194d3b9-7054-395f-a109-8acecd870943 | -6.91997 | -46.11069 | 2024-12-05 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44073f20-3adb-38ae-b8ed-e48d0c9ebff8 | -2.97925 | -51.19753 | 2024-12-05 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f42f911-8e0c-3348-b408-967ec5265648 | -1.71819 | -45.78679 | 2024-12-05 04:46:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71e5877b-7fde-328c-926b-b077822c935e | -1.08473 | -46.64023 | 2024-12-05 04:46:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efa4586e-8175-3d71-800a-23313368f250 | -1.5882 | -52.29116 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55977cff-2dad-37c0-a817-89556fa0f4cd | -4.40202 | -45.93301 | 2024-12-05 04:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e03ca9d7-dc9a-36e5-a12a-42961f620faf | -1.08284 | -53.45913 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e7869de-7272-3ce4-877d-51f929b5a3e3 | -1.44377 | -53.8124 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a070db5a-f368-38b8-9c50-11da3a751415 | -2.79739 | -51.44712 | 2024-12-05 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24665d19-c019-3a6e-bd6f-205eaf015d84 | -2.82181 | -53.06099 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fdb6deae-8133-3084-8a60-767255fa9af3 | -1.35674 | -53.6483 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80a6826a-4c6e-3d79-98ab-c546ce5b42de | -1.07646 | -53.45079 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6378831-b85f-3632-9628-e80c83741e57 | 1.11808 | -59.58282 | 2024-12-05 04:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6e697af-8923-39cb-b8f9-0397f426cc96 | -2.55718 | -53.99598 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98293c3f-f3ca-372b-9a85-f960ba71ca4e | -1.69465 | -52.64218 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5c0af99-6589-3e76-8c89-bc43553972fe | -1.49137 | -52.5288 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bc93adc-1170-3eb1-a9f9-e963a16e7833 | -2.95308 | -51.40733 | 2024-12-05 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 307666e0-e0eb-3484-9073-1b532f818145 | -4.64465 | -46.31779 | 2024-12-05 04:46:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b36e998f-9365-3251-b019-765444e0695b | -1.70962 | -52.45669 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0655e18b-83c0-3b45-b196-974f9270bfa6 | -2.83007 | -53.05426 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59d470e8-34a9-3dc0-91bb-9763cad5d329 | 0.89624 | -59.3864 | 2024-12-05 04:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 053a048a-26b3-3b27-ba68-daa6fba1247c | -5.58777 | -46.09143 | 2024-12-05 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ee458ca-b2d5-3a6e-963c-6d2b3105183a | -3.18306 | -53.85495 | 2024-12-05 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c120bfa-ba71-35c6-8675-12ac40af452a | -1.879 | -53.31111 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6e35441-d652-31ab-b27e-16268a3f031b | -5.57498 | -45.15827 | 2024-12-05 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README10.md)
