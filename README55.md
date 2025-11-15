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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61ee5045-fe11-3bf6-b5b3-2293e5d15ca0 | -12.67945 | -46.76232 | 2025-11-15 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 298ba934-ee1e-3675-8191-7718c2540f95 | -12.995 | -49.79686 | 2025-11-15 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb2a4bae-9e0b-30a8-a9e3-54b2bdd6e488 | -15.30747 | -53.00191 | 2025-11-15 05:18:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8459fc4d-5291-3f4a-96be-88f951b27ff0 | -13.48765 | -46.71587 | 2025-11-15 05:18:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a239af19-077a-36ae-b7ad-b06977ed1381 | -15.30812 | -52.99653 | 2025-11-15 05:18:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84f642b1-e8b8-32c4-bd6f-b0391d92a4df | -12.67806 | -46.7757 | 2025-11-15 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c9be7881-c61b-32ef-95cf-673cee54b814 | -12.84013 | -46.43153 | 2025-11-15 05:18:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 531f8825-6746-3101-ad7a-3c11cf90bcd6 | -12.67251 | -46.76139 | 2025-11-15 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8ac8cb3e-063b-392c-b00f-d72cc21b877b | -12.67875 | -46.76907 | 2025-11-15 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c5b995fe-fb72-30fc-96f8-d142e0a2ddf5 | -12.66003 | -46.74589 | 2025-11-15 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ddc76b65-8607-3cf7-8bfb-fa9bbb722394 | -12.84712 | -46.43338 | 2025-11-15 05:18:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a91d6fba-a324-3dcd-a92e-7cc88de54955 | -14.09627 | -47.87897 | 2025-11-15 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d57e36b5-6f79-3798-92a5-be56ce3b3abf | -8.07 | -43.1216 | 2025-11-15 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 893965cc-c515-3be9-be0c-98585132e544 | -8.0513 | -43.1001 | 2025-11-15 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.5 |
| 3c55919a-b014-3048-8d29-e9e9548f66bd | -3.8397 | -44.4032 | 2025-11-15 05:20:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| bb61f5d9-f8b9-35de-9429-11fa18e00a81 | -8.051 | -43.1237 | 2025-11-15 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 37.3 |
| 4a52b0fc-018f-32c8-849e-63ae9a91cda9 | -8.0703 | -43.0981 | 2025-11-15 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 262.7 |
| dca8bd2f-13ea-3fd7-b756-9df1e6a14112 | -11.8486 | -49.2218 | 2025-11-15 05:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 761dec54-24b7-3795-8068-43c5758b8511 | -12.6745 | -46.7605 | 2025-11-15 05:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 1956b3ae-a35c-31a2-948d-c68ce44935a7 | -11.9175 | -46.2135 | 2025-11-15 05:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| f4c9d2c0-854a-3c67-b669-291b79030041 | -16.56065 | -47.61017 | 2025-11-15 05:20:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9055586-f097-34cd-a193-b048e382a9ad | -16.56122 | -47.60367 | 2025-11-15 05:20:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24128f1d-6b1a-3b73-bd77-ecfce81ba9dd | -18.33225 | -47.18679 | 2025-11-15 05:20:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 535569b3-60f6-345d-b256-9d9a548ed515 | -17.83737 | -50.81177 | 2025-11-15 05:20:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35581ced-4018-3823-8bcb-8fbb82e5df89 | -17.83696 | -50.81596 | 2025-11-15 05:20:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 429f2af4-da53-3a3d-bcca-af07292f02c0 | -16.56023 | -47.61211 | 2025-11-15 05:20:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c70f79b-6bb2-33c2-b0c4-676ca13eaae4 | -16.56085 | -47.60562 | 2025-11-15 05:20:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3250cea6-f3f8-3f00-8414-859318a33ff1 | -18.33948 | -47.18692 | 2025-11-15 05:20:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2855cd1e-f0a0-39d3-a2d0-bbd12b7abecf | -11.8486 | -49.2218 | 2025-11-15 05:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 5bd4307c-1fd3-337b-9b6f-bb98ef221138 | -8.07 | -43.1216 | 2025-11-15 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.5 |
| 9ef96471-4fcd-3002-a2ee-ef3c3dae1c33 | -8.0703 | -43.0981 | 2025-11-15 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.1 |
| ac927c13-f78d-3010-9515-2a68bdbd1713 | -3.8397 | -44.4032 | 2025-11-15 05:30:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 118.9 |
| a4592030-d015-3a08-b47d-eb887809ec5d | -3.1652 | -45.2271 | 2025-11-15 05:30:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 0a435e17-7e62-3d69-b7f9-303051512cac | -3.821 | -44.4041 | 2025-11-15 05:30:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 3d1ea2a2-c415-3cba-aa24-d9a2dbf2d442 | -8.0513 | -43.1001 | 2025-11-15 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 41adc628-bad6-3570-8b8e-11f31211150e | -3.8396 | -44.4261 | 2025-11-15 05:30:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 17240297-7071-3b86-b615-3fc277354025 | -3.1653 | -45.2046 | 2025-11-15 05:30:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 0a659d40-2bf0-3fd2-b74c-1088282938c3 | -11.849 | -49.2 | 2025-11-15 05:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| f8d90dd1-394f-3ebd-8e7f-20fb7c3a4205 | -3.8397 | -44.4032 | 2025-11-15 05:40:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 133.7 |
| d070d2f8-5cd9-33cf-8951-282796f4bb3e | -3.1653 | -45.2046 | 2025-11-15 05:40:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 3686f376-258c-3970-ae77-b28d8db38067 | -8.07 | -43.1216 | 2025-11-15 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| fbb8dfe5-a897-3b47-b425-0fe908f6aa69 | -8.0703 | -43.0981 | 2025-11-15 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 286.2 |
| 653ee3b6-1acd-3a74-817f-b89a07eeb792 | -3.1652 | -45.2271 | 2025-11-15 05:40:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 546053d6-6d5f-33cc-b1af-c063ecf7f40a | -3.8396 | -44.4261 | 2025-11-15 05:40:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| d7d1377f-6790-31a2-a670-028d6e1c8624 | -8.0513 | -43.1001 | 2025-11-15 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 151.2 |
| 83ed1895-ee57-352a-9826-36e0377e05f8 | -3.821 | -44.4041 | 2025-11-15 05:40:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| f374f905-cd43-3a26-bda4-2293d112f990 | -11.8486 | -49.2218 | 2025-11-15 05:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| ef2be6ce-faf7-3b2a-8014-3c3ba9d8721f | -1.64623 | -55.81569 | 2025-11-15 05:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08c0462f-186c-3d5e-9172-5fbb807f557b | -3.53071 | -56.31953 | 2025-11-15 05:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6677a0a2-a2f3-3c5f-80a6-b185720f611d | -2.798 | -52.96656 | 2025-11-15 05:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6570a5a-fd42-3767-9226-2576f119273a | 2.34117 | -51.65128 | 2025-11-15 05:44:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dc59293-bfe8-33f1-a809-87c18dcf51f7 | -1.83253 | -53.8009 | 2025-11-15 05:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fd1d8da-0dc3-3e3a-b282-952548f03fd6 | 2.74906 | -60.36843 | 2025-11-15 05:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6be99a9-ba0d-3878-aea0-05b9db82d6a9 | -4.41493 | -50.81955 | 2025-11-15 05:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60fd6ebc-051d-33b7-bbee-61a488f1d45c | -2.80012 | -52.97037 | 2025-11-15 05:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f8f10f8-bbb4-3a37-8d18-570967e45da8 | -1.83378 | -53.79253 | 2025-11-15 05:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61a3c345-840e-39e8-8186-b4e4e98e2393 | -1.34744 | -54.60951 | 2025-11-15 05:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 74864fb4-963a-3250-98a9-2d2ceba6752d | -1.83315 | -53.79671 | 2025-11-15 05:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62f0f35e-f672-3378-950b-2ee2e4dc56af | -1.62316 | -54.71379 | 2025-11-15 05:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 643ce4b8-29e6-3b5a-861f-a6636ff93423 | -2.88588 | -51.43005 | 2025-11-15 05:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0dc223b9-579a-3878-ab5a-a903ab01062c | -1.34685 | -54.6133 | 2025-11-15 05:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5bdf28ac-db70-3dc7-bc3f-a0764ebe771d | -4.41384 | -50.82702 | 2025-11-15 05:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8cf4d41-02d0-38d6-9fe9-1cf7d1cf46a8 | -1.83333 | -53.8032 | 2025-11-15 05:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dd45aa8-4434-3646-ba3e-5843b47b46ad | -2.79388 | -52.96923 | 2025-11-15 05:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c62c5e3-2614-3591-ad4c-feeca49451ba | -2.79735 | -52.97111 | 2025-11-15 05:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9407b411-811a-3b94-95db-df2e0ba26e0b | 4.01384 | -59.63874 | 2025-11-15 05:44:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a41c9747-e148-3736-a401-b0aec3366c6c | -4.41649 | -50.81853 | 2025-11-15 05:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd50ad27-149f-3978-9f48-6254e20a4b60 | -3.60625 | -54.67518 | 2025-11-15 05:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18ff0dc7-fbae-36b6-aafa-78b8fe40b6e8 | 2.10349 | -60.61996 | 2025-11-15 05:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c1f7cfa-9336-3a13-9c0b-ba719fabe8ae | -1.3425 | -54.60494 | 2025-11-15 05:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21ab94f9-7bda-3929-9bbc-843c1971e258 | 4.01817 | -59.64239 | 2025-11-15 05:44:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a86d7ae8-09a3-3def-bcad-7480afa4ef90 | -1.83528 | -53.7907 | 2025-11-15 05:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f7bbc67-c5e5-31f8-98b2-deed37ee2fd5 | -3.59435 | -54.67706 | 2025-11-15 05:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06459ea6-4ffb-3aba-b1ce-f18b959aff60 | -3.60058 | -54.67422 | 2025-11-15 05:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49a233cb-91ed-3c9f-a740-c150350fdf41 | -4.41545 | -50.82602 | 2025-11-15 05:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52ad74ec-bd7a-3002-85b0-ad4c33d14b3c | -3.52562 | -56.31875 | 2025-11-15 05:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 950dd3b7-8a8b-3635-aaea-228e17e32b05 | 2.75059 | -60.36551 | 2025-11-15 05:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51066df5-d2f3-34cb-8bdd-1f3f70e90386 | 3.16207 | -60.26596 | 2025-11-15 05:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7758997-a690-39e7-bf99-ea7b47399e2c | -2.79317 | -52.9739 | 2025-11-15 05:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 470e4fdc-bfa9-3060-b04d-9ab2b4774221 | 3.1585 | -60.26653 | 2025-11-15 05:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5c62a2c-140d-3213-abe9-829ed0f76323 | 2.34027 | -51.64594 | 2025-11-15 05:44:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fab5b83b-ed5e-3f40-b4d0-7ac71c659561 | -1.3419 | -54.60878 | 2025-11-15 05:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab2962e6-85c6-3b60-8653-6b6088aa431f | 2.75125 | -60.36953 | 2025-11-15 05:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59d01f47-32d9-391d-b269-1384d8f5d235 | -1.83398 | -53.79904 | 2025-11-15 05:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50ebc915-ab39-3a83-8803-1fd4fbf4b732 | -2.80081 | -52.96585 | 2025-11-15 05:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64340ce9-2e80-3d27-af92-af2cc57d0861 | -1.83463 | -53.79486 | 2025-11-15 05:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2ee8621-85f9-3d49-9577-8b4e3859401c | 3.16059 | -60.26753 | 2025-11-15 05:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5cee9538-3e6e-3f10-a48d-bb7a26bd1ab6 | -2.80424 | -52.96779 | 2025-11-15 05:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f9c0169-f914-3aa4-b704-5a69f339c52e | -5.12636 | -55.97011 | 2025-11-15 05:46:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f8c9321e-3832-3014-bc42-f13adeb1cc92 | -5.12587 | -55.97342 | 2025-11-15 05:46:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3820be55-6b89-30e6-bec0-e6efd6ec5aca | -3.8397 | -44.4032 | 2025-11-15 05:50:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 62e1636d-c31f-37bc-9367-0a3283036de3 | -8.0513 | -43.1001 | 2025-11-15 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 200.5 |
| db921c9f-3834-33ec-90ca-adfc000aa317 | -8.0516 | -43.0765 | 2025-11-15 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.5 |
| 31045881-6f10-35b8-a224-a9ad09b22c17 | -3.821 | -44.4041 | 2025-11-15 05:50:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 7c2392a0-d07b-3a52-8038-3bff230a1134 | -8.0706 | -43.0745 | 2025-11-15 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.6 |
| a19ecdf0-98d8-3a9a-8a14-4995a88403bd | -8.051 | -43.1237 | 2025-11-15 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.4 |
| 47a85e53-9de0-33b2-9b79-08599a30d005 | -8.07 | -43.1216 | 2025-11-15 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| acd8f276-fedd-3718-b400-1bd2d82b7f79 | -3.8396 | -44.4261 | 2025-11-15 05:50:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 6b874cde-c592-3daa-abe4-a2974eee4aa8 | -8.0703 | -43.0981 | 2025-11-15 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 398.6 |
| 89cdaba8-73cf-34f5-b0b1-bfcc7c62e193 | -3.8397 | -44.4032 | 2025-11-15 06:00:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |


[Clique aqui para ver as próximas entradas](README56.md)
