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
| 76883a7c-f8b9-3291-b984-7f5a70aaa144 | -3.51139 | -53.80381 | 2024-11-20 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdb84b07-feac-332c-b870-adf66e3dd048 | -3.52555 | -54.68144 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8280f837-c3d1-335d-b61b-91fef634167b | -0.92627 | -51.64451 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7d4d69d-62ca-3e75-8fc4-fbf9b3158baf | -2.90751 | -53.05645 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 83db82ae-5643-3d56-934c-14448496a471 | -2.96224 | -54.16391 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b0e2f1c-da6a-39ed-9343-f8dc8ec4b4eb | -2.35779 | -48.6096 | 2024-11-20 05:14:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b48cbc4a-8f08-3ae3-8193-fa6208d003a7 | -2.74709 | -51.83256 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| ae80bab2-c10a-3173-a64a-4ed68cf4d20b | -3.3434 | -53.30547 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e67a9f76-5698-33e4-b048-a41316a72962 | -1.14732 | -53.51129 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0593eb0-e364-37d2-be9b-1d323462358b | -1.70125 | -52.14738 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c559610-dafa-372f-88f7-cc333be23f31 | -1.14655 | -53.51611 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9faecd1d-823f-3c57-8693-1ea8a7d0ae2f | -1.31521 | -52.39869 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0dfcb1d1-e2cd-32b0-b816-3c2a62ed883c | -3.37329 | -44.43499 | 2024-11-20 05:14:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cbae027a-382c-3150-b8a7-f18c2aaf370d | -3.81284 | -47.79979 | 2024-11-20 05:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 76c23c60-9188-3c54-a816-9d6490d9c148 | -1.88757 | -52.62341 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a125877b-5f85-39ec-9bb4-4792356a6990 | -1.58927 | -50.44294 | 2024-11-20 05:14:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db67a3a8-c612-3e67-948c-22da667c0c19 | -1.7853 | -53.59241 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2162a15-746e-39f7-95f7-358fbce826c0 | -1.66607 | -52.09441 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18340133-2f0d-39d6-b1f6-1756e163b83c | -3.88025 | -46.061 | 2024-11-20 05:14:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a1d327a-2270-3973-aeeb-524654f48be9 | -6.47961 | -47.50055 | 2024-11-20 05:14:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9685175b-3a61-3526-9e6e-7463a5820a5e | -1.22861 | -51.78671 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c704bdcd-9bca-37a2-bbbf-5fddc72ee25a | -1.15037 | -53.51675 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a18c65ca-9126-3549-8f45-1d08a329fea6 | -1.95614 | -53.32329 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50cda357-b9e6-3840-90b8-b3942441c0e9 | -2.62776 | -54.27247 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3999f31-e519-3e8d-9611-04a998fa8e49 | -1.31999 | -54.2137 | 2024-11-20 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 925e59ed-66e3-3193-ab75-6aa9328db43c | -1.1951 | -51.97787 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb43d425-b604-3797-a625-ed1c03f36a10 | -4.38545 | -47.78147 | 2024-11-20 05:14:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 260e6fc1-96c1-3199-8e2b-4dda9c8468ec | -2.85121 | -54.00322 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1677e525-d9f1-3c3c-b3ec-84949cf572e8 | -3.55384 | -45.02123 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 3358ae87-3098-390e-82f0-ebe6c282fc05 | -3.54178 | -54.57557 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 332cd51e-9d4c-3697-a02c-5e0b9a40f352 | -1.36987 | -55.37697 | 2024-11-20 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74d13cbe-88f5-340b-bb52-0fd2b393b119 | -2.9215 | -53.07313 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| a8c864c9-2944-366d-ac52-983ef1b5ad16 | -2.81654 | -54.02654 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb00fe9e-866f-3ec0-b478-98f39c2c87bd | -2.94278 | -54.79866 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ad51bcb4-1f06-35ab-a4a9-d8d6f6a29c3f | -1.73272 | -53.0306 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da17dbbe-6c08-3fde-9185-d3a911cf2c6c | -1.97171 | -53.13991 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa7aac8a-3f2f-384b-ad4e-918e2b3d2642 | -2.81343 | -54.02134 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41f75319-3e35-3936-ae1b-813b1914f875 | -1.45467 | -52.67704 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a311965-3010-3738-bbd3-7a7f4eddd717 | -2.66508 | -46.61256 | 2024-11-20 05:14:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02cecb9d-bdec-388a-aa9a-fe9cf539236d | -1.64338 | -52.66798 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c710c1c1-3632-3dfc-8a52-780db8829fee | -2.90694 | -53.06015 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1d786ff0-e84b-399e-9544-ae92e0aa948d | -2.28493 | -53.63584 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a0da0e0-b86c-3cc4-b1b5-e299c7e90f00 | -1.93387 | -52.99827 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0d82e9c-0270-32ab-8343-2dccb16291c0 | -2.76641 | -54.07814 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5fd996c-c6c4-3183-a152-ae1d00a5e629 | -3.06894 | -49.20501 | 2024-11-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 186431d5-d3fe-3fa9-ad31-8701e0c9f870 | -4.63298 | -49.54258 | 2024-11-20 05:14:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a52145c7-9996-3a17-a57b-88d952ed3ac1 | -1.61187 | -52.41525 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebfa96c3-5042-3281-8800-8bbbb84b86ca | -2.59374 | -54.01602 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 206759cd-ece4-3f23-8b3a-7a0de18e756a | -3.42527 | -53.28955 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14d25786-d6a6-3a3d-970a-a315166c284a | -1.21466 | -51.74837 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2dad42a5-30d6-3a4e-b367-ea97ee41528e | -2.82193 | -54.09368 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec44d5e0-d482-35c7-816f-80f26d3a797e | -1.25879 | -51.76221 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 149b1169-38c2-381f-b047-f4e8f3052529 | -3.50679 | -54.70539 | 2024-11-20 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7961d09e-45a3-3dc7-9086-bf660bec7ada | -2.68832 | -51.80487 | 2024-11-20 05:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58306487-55d4-3ddd-b630-930a9ca1a5b4 | -2.7586 | -54.05333 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21bbe752-32ef-3fe4-8c2f-4e30d2642f19 | -1.81836 | -52.69438 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3cbd9cf-9583-30ae-8a62-a5b29fd4af31 | -4.24529 | -53.67064 | 2024-11-20 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37af6d93-c371-3deb-95f4-219eaea75dbd | -1.04181 | -53.51649 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 867f7e4e-15fa-34ea-8915-f0dc6e47776a | -2.57981 | -51.92257 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aeea6a18-72d7-30fa-8476-1e9adca94621 | -1.45523 | -52.67338 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fe08ff0a-32a1-363b-b97b-fd3a6b5133d1 | -1.89166 | -52.62411 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac3be694-2b01-3cf5-a1c4-f36f713940b5 | -3.77142 | -52.66311 | 2024-11-20 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0add1b7-2fe0-3675-a530-f8a81e0e4c5f | -1.93277 | -54.06318 | 2024-11-20 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d5c7e9a-fb4e-3e2e-8eed-74914c7994f4 | -0.18497 | -51.62901 | 2024-11-20 05:14:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d3ceea1-6bcd-3c6f-a48c-90e86c65cf7e | -3.05157 | -54.41085 | 2024-11-20 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 04aac380-8543-3660-8584-e8619968b5c4 | -2.56629 | -53.99529 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 02871573-1594-3d63-86c3-a4f96d48c4f2 | -1.14154 | -53.66725 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 683ea7a9-c0e9-3c3f-b0d3-ea3d9684f45a | -1.25145 | -53.36274 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb237a59-cb8c-357a-95ed-54724bcb7c40 | -1.63367 | -52.62206 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9240bc99-991a-38da-837b-964fe6cbcdec | -3.47929 | -50.3176 | 2024-11-20 05:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b480c32-c786-3535-9503-085be06b650a | -1.21081 | -51.75904 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c6761bb-8816-35e5-9264-4f4757239fbc | -1.72593 | -52.69873 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40b9ee68-2884-34f3-a0bd-f71c00f6f244 | -0.90882 | -51.78709 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31664685-84c4-3181-a7d7-8299ee9af0a9 | -2.80992 | -54.02321 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6b798687-d744-3e3f-88a9-45759f7f8d90 | -3.77391 | -52.00388 | 2024-11-20 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffb31212-86a2-3dfc-bf30-4372cf651d0d | -1.04523 | -51.745 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cb19dae-bcd3-351c-bca9-c39789f6535a | -0.94941 | -51.72318 | 2024-11-20 05:14:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f1bc729-0da4-39c1-ac6a-61a7c71cf64a | -1.4558 | -52.66976 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b53cd741-8fe0-3aea-9541-7a9814ff682d | -1.86488 | -46.80506 | 2024-11-20 05:14:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f875a223-1acc-372e-aa92-b4d4e206850c | -1.6255 | -52.6208 | 2024-11-20 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 776bfbcd-e959-3d7d-a40a-07751f85d9fd | -3.87399 | -46.06303 | 2024-11-20 05:14:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 787d96e6-db7f-339d-88b9-8229a0dac1a0 | -2.6582 | -48.48415 | 2024-11-20 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6093ec38-29f7-3ab2-8593-0985e1d7a85b | -1.6955 | -53.69034 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e87ca014-7ed7-38fb-815d-e96360367b81 | -2.89335 | -52.43913 | 2024-11-20 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c39904e-a23b-3cad-8a5f-c9901428e699 | -1.44305 | -52.67152 | 2024-11-20 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 437cb4bf-0b4e-34a7-bdf4-7c02aa7549b4 | -1.20282 | -51.76741 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3484ff20-5e63-3e7f-b99a-bd11f18dc69b | -1.41582 | -54.92127 | 2024-11-20 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1fe5036-7535-3364-8629-e27ccb517ebb | -2.25052 | -53.67986 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bba6f857-294f-3532-b843-d373570aab21 | -1.21878 | -51.79356 | 2024-11-20 05:14:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e26d8ad9-603c-32bf-9891-7bdc84a27b3d | -2.59826 | -54.01435 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c2d49681-01e6-389c-ab03-8714eed34430 | -2.346 | -54.78466 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 53f9440a-39b6-3501-b077-01f22ddc7807 | -1.48284 | -51.15979 | 2024-11-20 05:14:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92c932fe-4ac2-31a6-a7cf-78a65286eb99 | -2.21083 | -53.70786 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25f3759b-8d97-3c2f-bd70-fb035b9f571c | -3.19518 | -53.13535 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c54d7e1c-12fe-3bef-84b9-5d3915eb11e7 | -2.2139 | -46.48283 | 2024-11-20 05:14:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20990593-d5ba-3dff-abfd-643e87bb6d74 | -1.60103 | -54.64275 | 2024-11-20 05:14:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c814660-0bb9-3d00-8b77-1cbd6c334f55 | -2.63384 | -54.28256 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef30095a-f9c0-3017-a273-ddba1e45c0a8 | -2.34896 | -54.78939 | 2024-11-20 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c91ca84a-05ac-3be6-aebc-b878a41201e5 | -2.74491 | -54.11712 | 2024-11-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c274fa6b-17c6-340e-ac7b-0b5b971cc54f | -2.91855 | -53.06542 | 2024-11-20 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |


[Clique aqui para ver as próximas entradas](README72.md)
