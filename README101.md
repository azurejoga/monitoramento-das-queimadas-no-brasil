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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 006cb099-38c1-35fc-b4ea-80f23b914d56 | -12.3993 | -45.0183 | 2025-08-28 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| e11059e4-b813-30fb-bff6-d50cfd85fea5 | -14.3696 | -52.0813 | 2025-08-28 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 33a299f2-ba5f-394a-8576-3bb75a03936b | -12.8998 | -48.1158 | 2025-08-28 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 1c0ff264-4d3c-373f-b490-08ab58effa50 | -12.8032 | -48.1516 | 2025-08-28 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| f91a7701-1b79-361e-950d-30fa7c32f70d | -10.8421 | -60.8009 | 2025-08-28 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| e76f1047-ebf8-3727-a40c-77aac38ab0ff | -13.4208 | -46.9864 | 2025-08-28 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 1dbf7083-8ef6-31b6-9cdd-5baeb150eee1 | -13.5193 | -46.8805 | 2025-08-28 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 93.2 |
| b45096fd-e7ae-3619-92b2-daa3bba31c0b | -11.2378 | -55.0569 | 2025-08-28 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 6d839c46-4e05-3a79-95f5-c8a0e0c897d6 | -12.9961 | -56.9201 | 2025-08-28 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 153.3 |
| 4a84d18d-1d0c-3354-8818-4aa3c83ef1c9 | -6.178 | -44.0688 | 2025-08-28 14:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 6125e968-48b2-3a40-95aa-6b630741566a | -8.8841 | -60.7699 | 2025-08-28 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| fe1e1978-2abb-32f4-bca6-889724e5910b | -9.5424 | -62.3823 | 2025-08-28 14:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 6880ee4a-3d9c-318d-a685-71fa63e342cb | -9.7322 | -64.9067 | 2025-08-28 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 99066c24-4f0d-306a-856c-d8f392317e2c | -10.293 | -64.49 | 2025-08-28 14:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ac27d05d-a544-3f19-8ee5-ac1a4ecdc86d | -9.6797 | -47.0576 | 2025-08-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 56f257dd-db3e-3006-870e-800c178928d0 | -8.9479 | -65.9616 | 2025-08-28 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 4005a0bf-fa62-38c7-98c1-e10946ea6e1e | -6.6759 | -58.846 | 2025-08-28 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| abaa81ce-a5f2-3815-adaf-8f18dbe6db4f | -7.6225 | -42.6738 | 2025-08-28 14:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 115.2 |
| c2c05570-e5fe-3a3c-bdf3-79961ca5d90a | -9.676 | -64.9838 | 2025-08-28 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| ad9affad-ff02-3daa-b7c9-a10282503efc | -10.4549 | -57.9576 | 2025-08-28 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| f67086b0-7e87-3a2f-954d-ba4eef133384 | -7.1917 | -44.0732 | 2025-08-28 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 4b8af576-b954-3642-90b2-ea23652a02bf | -10.3709 | -45.1686 | 2025-08-28 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 5590127a-105b-374b-86a0-6e2ea4c63778 | -12.8224 | -48.1489 | 2025-08-28 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 651f9db8-3273-3510-b431-fe03c8459e53 | -13.5382 | -46.9002 | 2025-08-28 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 3ff36a68-71ec-333b-835c-e3d18b844309 | -11.2189 | -55.0585 | 2025-08-28 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 271fb4b9-6100-3d4f-bdf9-ce7ee9353492 | -11.3526 | -43.5187 | 2025-08-28 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 354abe05-668f-3e09-ae2b-1868909737ac | -8.9664 | -65.961 | 2025-08-28 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| c59fe0e2-fefc-3e7c-950d-922c6af30e3c | -8.0841 | -44.997 | 2025-08-28 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| bcc8ddc8-895d-383b-84c6-b42bd9426878 | -7.9262 | -63.0724 | 2025-08-28 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| d7a52e32-18f6-36be-a889-d3d40fc338f2 | -10.8233 | -60.8019 | 2025-08-28 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| d01c86d0-ada3-3bd9-a8d8-576f78a009c9 | -12.9963 | -56.9 | 2025-08-28 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 5e2045ac-c380-34d9-a859-43eb93bcde99 | -10.8419 | -60.8202 | 2025-08-28 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| ae23f3d7-f343-395c-8244-eb072b935b63 | -13.5386 | -46.8775 | 2025-08-28 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 01f7b177-34f6-3190-81f6-36c9affb28d3 | -14.3309 | -53.2477 | 2025-08-28 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| d0a15107-bb86-3560-a6bb-9a5d164f8230 | -9.1363 | -65.2835 | 2025-08-28 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 36b259ec-9903-363e-8c9c-147fe457cd36 | -11.3517 | -43.566 | 2025-08-28 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 217.7 |
| 4b9af1c4-79f9-329a-8139-717d98168aed | -8.8842 | -60.7507 | 2025-08-28 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 139.6 |
| ff63de13-d36b-356b-9c0f-6522ccf246d9 | -8.7325 | -47.3783 | 2025-08-28 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 1fa0d169-9505-3b8d-b384-e49c9324b4e8 | -13.4204 | -47.009 | 2025-08-28 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| fa717340-df20-3f6e-b517-0c1283f288c8 | -13.0154 | -56.8982 | 2025-08-28 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 182.5 |
| 345d6f3d-b58a-3c99-a7a9-91ae23a3eda9 | -9.4366 | -48.2955 | 2025-08-28 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 78eea050-25e0-3673-8db9-c1a9bbf1fc34 | -11.3669 | -63.2663 | 2025-08-28 14:40:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 7d73c87a-cf46-320a-811a-b9d46680b1ca | -9.5423 | -62.4014 | 2025-08-28 14:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 3c2b5adb-e006-3301-9a3a-3fd9f8d2d88d | -10.2743 | -64.4907 | 2025-08-28 14:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| b96a03ff-3056-388b-99ae-ceaecea9d2fb | -10.308 | -46.8068 | 2025-08-28 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 2c223444-0363-3bc7-a82d-52817913ec5c | -10.8236 | -60.7633 | 2025-08-28 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 43da8135-bc9d-3790-aa6b-2988a71f3e81 | -9.4363 | -48.3174 | 2025-08-28 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 8e5aeea1-7048-3b0d-9e70-e9f4b1a2e719 | -10.4736 | -57.9563 | 2025-08-28 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 7c797506-837e-38f9-afa1-7df6b0682e42 | -7.3357 | -59.6484 | 2025-08-28 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 78305a33-119a-38a0-9d7c-e78855552e4f | -10.8049 | -60.7644 | 2025-08-28 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 1c372561-5942-3b8c-babd-93d704b39bc2 | -13.5571 | -46.9199 | 2025-08-28 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 114.7 |
| f9cef0a8-4617-38eb-85d8-31bb7a4a5a3f | -9.6574 | -64.9845 | 2025-08-28 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| de814abb-6bf3-31f1-8f40-e826a446dd9e | -9.5842 | -45.7665 | 2025-08-28 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 665a9002-4532-3788-8daa-61a0fa3c3211 | -6.4355 | -44.5764 | 2025-08-28 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 143.4 |
| ba2454cc-e872-3d20-ab6b-eb61e0b01c27 | -9.6816 | -48.3139 | 2025-08-28 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| c13e9449-e0db-382a-b20e-92ef0d4bad70 | -10.4738 | -57.9366 | 2025-08-28 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 339048a0-58ce-33f1-99a9-9f7f2fd5989b | -8.4596 | -43.6645 | 2025-08-28 14:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 8dec72b2-be85-32d5-8cfe-01c1f5235c0f | -14.3339 | -51.9157 | 2025-08-28 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 95ba4040-26e0-3027-9d56-c0440f13d99b | -7.192 | -44.0501 | 2025-08-28 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 5be75af7-04ff-3522-b4e4-a7f4fa6e885f | -7.0569 | -44.3623 | 2025-08-28 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 1429fb87-4ff7-3776-ab5c-c91112e1f831 | -8.8921 | -62.4297 | 2025-08-28 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| aa8b388a-0241-3a61-815f-d058acd62824 | -12.6878 | -48.1677 | 2025-08-28 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| d642d672-298f-34ad-a422-433db9c79a6d | -9.6794 | -47.0798 | 2025-08-28 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| a49f6452-1567-3dc0-a46f-0dfc1426faf4 | -13.0863 | -46.3352 | 2025-08-28 14:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 53f2af75-b1cc-36b3-afce-ee5f0bd754df | -8.7322 | -47.4003 | 2025-08-28 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| cf621b9f-b7f8-3d44-bbee-6a135b8b6fce | -6.1595 | -44.0472 | 2025-08-28 14:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 394ec6a5-92af-3a21-b35a-97b172cd6460 | -12.8998 | -48.1158 | 2025-08-28 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b6bbef3f-2a1b-302b-a69f-fadf5cc58d29 | -13.0151 | -56.9184 | 2025-08-28 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 334.3 |
| 2ed4e347-7544-396d-987e-ce00f05858db | -15.191 | -53.79 | 2025-08-28 14:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| c26206d9-0cb3-3f50-bc19-5828fe90fb5b | -6.1372 | -44.417 | 2025-08-28 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 027903c3-c0ad-3532-b47c-cb5cd9523668 | -12.7071 | -48.1651 | 2025-08-28 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 1546aef7-f8cf-33af-97d5-822bc7c7287c | -14.3696 | -52.0813 | 2025-08-28 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| ffa32f1a-6ece-3b2a-912a-dd870c7c8a19 | -8.4407 | -43.6666 | 2025-08-28 14:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 286.5 |
| 550c5e0d-e768-3cd9-b72c-8624bc2160e3 | -8.4403 | -43.69 | 2025-08-28 14:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 113.7 |
| a72c79c5-9d8e-3d53-8138-66580cd90ea8 | -13.1367 | -54.9171 | 2025-08-28 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 43d166bb-1c80-3f74-9bdf-43dd154032df | -9.1362 | -65.3022 | 2025-08-28 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 4bc2fae4-c0c9-3a25-bfe8-ac8e5a2a527a | -9.4372 | -48.2518 | 2025-08-28 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 37495352-987e-3411-a444-de2a5ae4df6a | -9.6759 | -65.0026 | 2025-08-28 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 937de7bd-b1f9-3536-bf9c-06ca91e8eefc | -13.5378 | -46.9229 | 2025-08-28 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 5ce995f9-267e-34b3-afb9-7f52918e8f0b | -12.8613 | -48.1213 | 2025-08-28 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 8e68c478-2aa7-36a4-9516-10499b189f83 | -15.1906 | -53.811 | 2025-08-28 14:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 134.5 |
| acd53484-40f8-3451-a813-ce0f4484e505 | -11.2375 | -55.0772 | 2025-08-28 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 5a7aeae4-3f84-3909-b774-38b5fbff4542 | -14.3699 | -53.2219 | 2025-08-28 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 8bf4f36d-1270-383b-9b06-1e78bb508131 | -6.4357 | -44.5535 | 2025-08-28 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 75d5e060-0215-372e-ac20-f1b7fb482612 | -11.3325 | -43.5689 | 2025-08-28 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 397c2def-10dc-3817-9b32-0d4820ad5e47 | -12.8228 | -48.1267 | 2025-08-28 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |


