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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c543d4d-7dca-3f71-b2cb-ddd5eb130fba | -1.35591 | -54.6343 | 2024-11-28 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cc4b620-ded0-3e11-9515-28833da18c8c | -2.13562 | -47.1598 | 2024-11-28 04:23:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c5052ec-1d06-3d53-82e7-34ece3c9eff5 | -2.73666 | -46.11718 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 122def2c-f630-35b4-b122-dfb6b8c22f72 | -1.20059 | -51.75793 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c885d9b-47e5-3298-a79d-9868fc7470ec | -1.20061 | -53.88306 | 2024-11-28 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f05dbfb-1471-3451-93f3-16ea87e02a6d | -1.66097 | -52.73117 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4144f956-69a3-3e1a-a77e-25f5c6ca2b70 | -1.18933 | -51.77013 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4950d803-c7d2-35d5-a90b-69e8041c4fcb | -8.56415 | -49.20155 | 2024-11-28 04:23:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 418c002c-9f38-3bd0-a20b-a57c0c745e89 | -8.54948 | -47.77213 | 2024-11-28 04:23:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dea5edd4-aee9-3133-9e16-748052ba7ef6 | -2.09305 | -46.32063 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef17d27f-a0db-3db3-867f-723fdaf031f0 | -5.75785 | -46.26352 | 2024-11-28 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14cd0557-efb8-3ebd-86a3-2a5c3ce45921 | -5.93122 | -43.78119 | 2024-11-28 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efd54457-5631-3208-9a04-a682bb31c805 | -2.51205 | -45.19209 | 2024-11-28 04:23:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e934546-b5ff-3764-a015-542abef41a85 | -1.08849 | -53.64783 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29f7d7b1-c00c-3147-94b1-08396d48b3e4 | -2.42196 | -46.26049 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c147b65-2719-3faa-81cc-4d415f8e8970 | 0.97164 | -50.12642 | 2024-11-28 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2b6588c-0ae6-3f01-94f2-6a2a4370d74c | -3.95994 | -54.61075 | 2024-11-28 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46ce4817-54aa-3379-976b-c56af2518ceb | -1.15295 | -53.57631 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22700c5e-629c-3185-adbd-0b8e70f09407 | -1.20805 | -51.74047 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50fe5de2-9bcc-3497-9f13-60ac92f007a3 | -1.36011 | -54.99267 | 2024-11-28 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 605edcae-e8a5-3e23-8ee4-10ea4019179c | -6.17467 | -42.60857 | 2024-11-28 04:23:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 65c61b4f-6952-3afb-b430-4c410195666a | -7.83066 | -48.19006 | 2024-11-28 04:23:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0354ece3-ecd1-3b6e-a106-57cdbc284959 | 0.9924 | -50.26198 | 2024-11-28 04:23:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e559b9e3-0ef8-3a85-90e2-9e36844a662d | -1.36005 | -51.96318 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 236d1f10-9fad-3462-8b7c-51168a3dfa07 | -1.95375 | -48.68781 | 2024-11-28 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 133c403b-35f3-3ba1-a4e8-07709f6e20e6 | -2.59469 | -46.26268 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49fab059-8e25-33bb-a0e7-751af07c0bef | -1.33482 | -52.44296 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b18944e-5bc9-31ef-901c-d3cf624cdc7a | -1.72149 | -46.22324 | 2024-11-28 04:23:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05c92f83-bbde-368e-984a-da36c4ba96eb | -1.58348 | -52.2688 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ccd9e14d-62ed-396e-8915-223edd2b19b4 | -2.46137 | -46.24875 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92fc3457-0edc-3e75-b637-14b5bad0dc77 | -1.53245 | -46.06417 | 2024-11-28 04:23:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd453dda-4fdf-3a65-a375-3be39f70c27e | -1.36974 | -46.90327 | 2024-11-28 04:23:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 711caed1-1624-3b9b-9ef7-894afc4c3ddf | -2.5211 | -47.40643 | 2024-11-28 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3207a5a-1797-3927-a7aa-00664c7925ba | -2.54085 | -46.41203 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9285ce5b-6b7d-3d39-8355-2e63d6f53591 | -2.70834 | -46.21257 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93257200-3e5c-3cf4-92d2-557dfb73b2cb | 0.04635 | -49.53018 | 2024-11-28 04:23:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9621f1d-b514-3697-bf37-c6deb0c94811 | -2.7118 | -46.25241 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4862adfc-916e-3253-ba7c-95becfbfff46 | -1.69719 | -52.63071 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 40e70db9-fc1d-316d-a085-189bcb367bbe | -1.7008 | -52.75917 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dbac39d9-d2a2-3b16-adb2-1f84f8dfc927 | -5.83073 | -44.07574 | 2024-11-28 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8cfe3ff1-c745-3911-aead-3474dd922a36 | -1.66211 | -52.48238 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4b0f67b7-5e24-34a1-96f8-03ade69e827a | -2.62509 | -46.07124 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5400f213-03a0-3019-bd33-7730e3d6a656 | -3.96466 | -54.61478 | 2024-11-28 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0871af6a-1049-333a-9903-a7781c81dc87 | -2.6993 | -46.11843 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebf46992-4990-3aaf-8e3d-74777d467baf | -1.64094 | -52.46345 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f76589e7-898b-38e0-a951-5d9e88f092b8 | -8.55342 | -47.78357 | 2024-11-28 04:23:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b26ba9ab-6797-35ec-9f42-5468714280a1 | -7.81096 | -50.01217 | 2024-11-28 04:23:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39426e5a-ebd3-3002-b87b-ab373404500b | -1.23024 | -51.80493 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c18ad820-5985-38a3-8b33-08a40f6a0bcb | -1.62182 | -52.3735 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61b5ca8e-093a-37df-a38d-43477739be10 | -1.12955 | -54.2204 | 2024-11-28 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdbaf040-957e-3060-8fd3-50f20b4196ea | -2.58353 | -46.98581 | 2024-11-28 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b3a50ba4-8bd6-3f84-a975-27e0f0b9dfd7 | -0.94044 | -47.11193 | 2024-11-28 04:23:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c17b478a-f19f-3ac8-a747-22e3cae916e3 | -2.23849 | -48.52408 | 2024-11-28 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1b32748-efea-3fd3-b351-30d45cb6b4a7 | -6.08829 | -48.03495 | 2024-11-28 04:23:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| df770124-2588-3a0d-b29a-f4c5da2a4186 | -1.44448 | -47.11948 | 2024-11-28 04:23:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12dfbfc7-0507-39fd-8079-79b0e480d560 | -6.171 | -42.60798 | 2024-11-28 04:23:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 880e9679-6f58-385f-8a53-4908a31cf497 | -1.38526 | -53.63449 | 2024-11-28 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b6b765a-220a-3e78-88c5-920e6d3aaa7c | -2.72346 | -46.28642 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db45611f-855f-3677-b751-756e66a13384 | -6.35346 | -47.3049 | 2024-11-28 04:23:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99e31fbc-2a70-3e05-ac80-683f44a34ece | -2.69609 | -46.18208 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4568df91-0740-3676-9a78-8730fd42a72f | -5.98055 | -45.36282 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 9881dc1a-11bc-3d97-95b8-48fe0c12fa93 | -5.26308 | -47.20158 | 2024-11-28 04:23:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b88a2ee-b8d6-35ae-92df-8efbbc340759 | -8.60366 | -47.91988 | 2024-11-28 04:23:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54ba5f51-5822-33b6-b6c4-c2ab46b687a1 | -6.10539 | -43.97051 | 2024-11-28 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d2b8b808-8bbb-367d-a23a-c595e2f3495a | -7.79847 | -49.99664 | 2024-11-28 04:23:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d24e1a9-ae18-3eab-a091-faa704eaf587 | -1.31377 | -51.75585 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c13e03f5-424f-3895-a260-83880042901e | -2.54754 | -46.41306 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b687817a-87bb-37d6-af0a-ed203be67985 | -7.54627 | -47.58219 | 2024-11-28 04:23:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f63a681a-d567-34a0-800a-7b96fdc9ebe7 | 2.08865 | -50.63173 | 2024-11-28 04:23:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15b0f6c1-a9a1-360b-b751-786fbb0ef5af | -2.1232 | -46.41202 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cacb5676-78ac-3123-a08b-cf9177c0803a | -2.5442 | -46.41254 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d93d728-9e7d-3597-b774-a800b901af53 | -6.12069 | -46.59015 | 2024-11-28 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01be10b9-5fe1-3329-859e-96f269f156cf | -2.68127 | -46.27627 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e9e14e7-669f-3851-bd7b-b7a4027e16db | -2.5817 | -46.19596 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ee5a9f1-177c-3d4b-8c31-5784766f9ab2 | -9.17668 | -44.72144 | 2024-11-28 04:23:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9f84327-263c-3da1-8ee8-5cc9b6cf2e23 | -1.64012 | -52.46847 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ba2a4283-b7dc-3124-9c25-f8d71b96c0f4 | -7.00261 | -46.12432 | 2024-11-28 04:23:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 318bad32-dcd1-347d-99c3-9a16fcbd2d40 | -6.56972 | -46.56548 | 2024-11-28 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e1e7d12-cbad-31f9-813c-dfa544b4ce9c | -5.96056 | -43.37185 | 2024-11-28 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 95c6525a-7791-3142-b282-5e542d7054e4 | -2.54919 | -46.40253 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a1d0543-3dfd-3d83-92ab-3036b4c8d8f4 | -1.18405 | -51.77398 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26eb7337-58ea-3abc-af1d-c653e582ba39 | -1.31898 | -51.92675 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a40b8c41-1243-32c1-965b-f552e2417a60 | -0.95843 | -51.65081 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1790ab79-05f4-3296-b252-782fd6a01456 | -5.52162 | -47.58508 | 2024-11-28 04:23:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81c820fa-acc0-3f65-b9bb-8bd99d26ab6b | -2.71902 | -46.2929 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd3b019c-b47c-3d53-acc1-b1204dc3cad5 | -0.873 | -51.72124 | 2024-11-28 04:23:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cca69472-7f28-3063-8883-480937a28c74 | -7.69093 | -42.98359 | 2024-11-28 04:23:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| bbf704f9-2965-37b9-af6a-567c248c7fb0 | -10.03171 | -36.27714 | 2024-11-28 04:23:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e625514e-9a6a-3ffd-a151-edf12c342aee | -1.38011 | -53.63372 | 2024-11-28 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ef7eead-a494-390a-93bb-8d4f936d7b4e | -1.54362 | -46.05546 | 2024-11-28 04:23:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25798a84-17ab-39ff-8b31-69ffde7d7665 | -6.38896 | -47.38338 | 2024-11-28 04:23:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ceed1dc-6bea-3f4d-ad77-45c1df1ffeb4 | -1.15628 | -53.55561 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a1344f3-f656-3b11-abd3-3943cfdecfa9 | -1.33046 | -51.94301 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9cc64abb-b334-3be8-962f-863c5503732b | -1.9976 | -46.30222 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21238d2f-e986-3cb1-bd2f-7be6340bd5c4 | -1.09944 | -54.14836 | 2024-11-28 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1855bf6b-4bd0-321d-9ac4-4b0325c18dea | -6.58899 | -44.17737 | 2024-11-28 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8034b749-d86f-341f-bbb0-e83619d323d2 | -2.69848 | -46.29327 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c5f66e0-5aec-33ce-b6f5-3a556413b751 | -0.88282 | -51.71808 | 2024-11-28 04:23:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f40e8e0-c206-3f8a-a3c1-b65e7950e30f | -2.40803 | -46.17603 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b36de2d-5832-3709-ad45-cbbe1a542113 | -1.58192 | -52.27855 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |


[Clique aqui para ver as próximas entradas](README50.md)
