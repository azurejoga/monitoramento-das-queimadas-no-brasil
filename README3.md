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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0fd4154-63fe-3901-b799-f2d58cb65221 | -23.9839 | -48.91459 | 2024-12-30 04:06:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| edb4fc0c-b3f6-3876-b8f3-1ffce1f4f9ee | -23.98293 | -48.91971 | 2024-12-30 04:06:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1d08616-79fd-3510-8668-3905f9743e0d | -20.9962 | -51.79433 | 2024-12-30 04:06:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c62c51ed-5585-39e1-af89-2f60cfdfaae1 | -19.34056 | -54.17236 | 2024-12-30 04:06:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65dd0f20-549a-3f43-b489-4d7986fad7da | -20.59893 | -51.61146 | 2024-12-30 04:06:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cd25860a-4d46-340e-81f2-a0bf06cd7833 | -24.24169 | -50.74166 | 2024-12-30 04:06:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ea56b500-3432-34cb-ac32-ad9cbb668638 | -19.34152 | -54.16804 | 2024-12-30 04:06:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fef5afe0-5bad-31d2-9bc1-c605082d958e | -29.38373 | -52.65189 | 2024-12-30 04:08:00 | NPP-375D | SINIMBU | RIO GRANDE DO SUL | Brasil | 4320677 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7ea71b9d-5cd5-3143-baf0-1ec55385792b | -29.60462 | -51.98781 | 2024-12-30 04:08:00 | NPP-375D | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5883e10b-7d32-3a0e-b7dd-f79e14e59017 | -29.17054 | -52.01448 | 2024-12-30 04:08:00 | NPP-375D | NOVA BRÉSCIA | RIO GRANDE DO SUL | Brasil | 4313003 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b8f9ce22-dd22-38c5-aa98-9c3072feda7c | -6.96108 | -43.00532 | 2024-12-30 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b2f3763e-ca5f-3172-bed9-e405aaf7bb87 | -6.98765 | -43.02675 | 2024-12-30 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d044dc83-2ee2-3e21-85a9-5683d6d28290 | -1.82851 | -45.69818 | 2024-12-30 04:23:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 844a7fe9-021c-32e3-b332-9f4e70a99438 | -6.97137 | -43.01126 | 2024-12-30 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 71e8e99f-94af-308f-8aa7-bf263b4e71a8 | -6.98631 | -47.08524 | 2024-12-30 04:23:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7b33d77-c04c-3a78-8dcc-aade66409e4b | -8.58181 | -41.12401 | 2024-12-30 04:23:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5f9650bd-e6b8-3b7a-9b78-d55bb07a26ad | -6.96472 | -43.00589 | 2024-12-30 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2c95ec21-a670-3ac8-aed8-cce82b932b9b | -1.64884 | -45.86894 | 2024-12-30 04:23:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9126c802-6559-3052-8b26-31f65c070305 | -6.95743 | -43.00476 | 2024-12-30 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 775b16e5-b099-30aa-8aa6-a2611a9611cf | -1.64606 | -45.86495 | 2024-12-30 04:23:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61c44e0c-372a-3c3d-a64a-08569ba59580 | -1.49851 | -45.83125 | 2024-12-30 04:23:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4abb0f49-b61e-3635-9206-fd60b3460b28 | -5.25161 | -44.9863 | 2024-12-30 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bcfc214-d8a4-3f58-a697-c2d5efabcc84 | -6.98373 | -43.02884 | 2024-12-30 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8c23638c-549f-3d64-ab77-82078e537d2d | -6.988 | -43.02518 | 2024-12-30 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7ed27e84-3a90-35f9-a60c-7e0ec54e2883 | -6.79098 | -47.39304 | 2024-12-30 04:23:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40ff7b83-9770-3053-9037-75e86e4197e9 | -5.25216 | -44.98277 | 2024-12-30 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3c55d3a-cd87-3d6c-a79f-1526d5eaee09 | -5.3794 | -46.29225 | 2024-12-30 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aec80fe1-c371-3d8f-b00d-e61ab1e655c8 | -6.97202 | -43.00702 | 2024-12-30 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 3e61c38b-5775-3db7-a8b6-fcd06a581274 | -5.2555 | -44.98329 | 2024-12-30 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2867372c-0558-3ada-9067-4b54924c6181 | -6.97266 | -43.00276 | 2024-12-30 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3919f1b1-2c8c-375c-a1f5-d50c5dccde91 | -1.65217 | -45.86946 | 2024-12-30 04:23:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37853d19-0f59-37b9-8dbd-f17b7e1cba62 | -6.97567 | -43.00755 | 2024-12-30 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ebeca6ba-a1df-3ab1-8a8a-29fe8d252828 | -6.96837 | -43.00646 | 2024-12-30 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| e9805737-3bc4-3f51-af16-10d11866bf90 | -1.85683 | -45.54014 | 2024-12-30 04:23:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6a4c0b4a-7551-38b8-bc3e-7e4605c6a23e | -6.9495 | -43.00789 | 2024-12-30 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f10be150-925f-3943-bc2f-481945f1585e | -7.66778 | -46.10042 | 2024-12-30 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05139a12-3456-3adb-abfb-62ac60e5889c | -1.82796 | -45.70163 | 2024-12-30 04:23:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c21bb73-1710-3d19-af7f-82905f11f463 | -5.25495 | -44.98681 | 2024-12-30 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 31b2f85e-6007-34b0-b187-4f413608db8e | -1.64274 | -45.86443 | 2024-12-30 04:23:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 057da45e-4202-3de1-b9d4-13e18030c3a7 | -1.85737 | -45.5367 | 2024-12-30 04:23:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8fdf4c97-671c-366f-b51f-26939240f307 | -6.94585 | -43.00732 | 2024-12-30 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dcd8c58c-6852-3410-8d77-5131fc89d2f2 | -7.6711 | -46.10094 | 2024-12-30 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77803c9a-94eb-3a73-b144-e7ce7b842fc4 | -1.64939 | -45.86547 | 2024-12-30 04:23:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee358c68-73a3-39d4-a8c1-31b9e0843946 | -6.96902 | -43.0022 | 2024-12-30 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d35eae09-2124-3529-9277-602326389ae1 | -1.86014 | -45.54065 | 2024-12-30 04:23:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 905e25c1-613d-38df-9dd0-51e21a1cc34d | -1.64661 | -45.86148 | 2024-12-30 04:23:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5d998a53-9816-3fb8-810e-7fb9e0ee2f4e | -1.64329 | -45.86096 | 2024-12-30 04:23:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19f895f4-1bf7-3995-940f-caacbaa2fb12 | -6.95679 | -43.00903 | 2024-12-30 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 983b8a65-5706-3fdf-b9ff-b039e4da4287 | -9.84287 | -37.12212 | 2024-12-30 04:23:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eac55f21-9016-3e85-9a66-36c87cd0200c | -6.98737 | -43.02943 | 2024-12-30 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eb0551c5-f48a-3cdf-b60d-4486da38d735 | -5.25605 | -44.97977 | 2024-12-30 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0e516ef-5c51-3212-9834-756e424ec285 | -9.08587 | -46.3669 | 2024-12-30 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13ea0b46-d4f9-3b24-879b-d9b6ce1bcc72 | -4.89903 | -41.09836 | 2024-12-30 04:25:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 49b05cc8-3701-3f4c-8362-d58feb9e9bbb | -4.90696 | -41.09963 | 2024-12-30 04:25:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 7712de2a-f36b-3f4a-8048-e4e55999a9cb | -4.90548 | -41.10965 | 2024-12-30 04:25:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ca439ff0-10ee-3716-a468-afcf78fc6dd3 | -12.36949 | -52.48828 | 2024-12-30 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93cddceb-a37d-3edc-aa5e-d2ea861f1dea | -10.52559 | -47.96119 | 2024-12-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95b0c1a8-4bc8-32a2-a2fc-e9866f2dc345 | -10.86496 | -42.14453 | 2024-12-30 04:25:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a344ae24-bc7b-359c-8d8f-3b5178827f7e | -12.37162 | -52.49949 | 2024-12-30 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3044ae3-2070-370a-ba63-0f1d70b21487 | -12.36857 | -52.49351 | 2024-12-30 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56579c18-fa2d-3b80-9416-67e10b58e2f0 | -14.13555 | -41.69321 | 2024-12-30 04:25:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4b2dc91b-1af1-3e90-9253-2f0981361729 | -11.84544 | -43.7268 | 2024-12-30 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77ebdbd3-8043-381f-880b-fd33cd9edbb3 | -5.28571 | -42.22048 | 2024-12-30 04:25:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 34dcad1d-bdfe-3f3c-8f65-c718f5a00891 | -12.37345 | -52.48901 | 2024-12-30 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 48e6a9a6-fb51-32e7-93c9-ee59513081e9 | -10.60886 | -44.32375 | 2024-12-30 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2b5d9bc9-b8f1-3f27-b577-9cba021f4138 | -4.90013 | -41.10197 | 2024-12-30 04:25:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 228f7531-ca6e-309f-8915-472ed7d96974 | -12.57156 | -52.52948 | 2024-12-30 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af4a07c1-83e8-3b8b-8fbc-44110643407f | -10.61657 | -44.32073 | 2024-12-30 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be118041-d726-3a55-8489-04b6386330ff | -12.37741 | -52.48975 | 2024-12-30 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7705ef7e-d16e-3eae-86c0-81e295b9d969 | -11.24613 | -44.48283 | 2024-12-30 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff8f07c0-b3fb-3bc7-ac7f-6f0f644938b2 | -12.3765 | -52.49498 | 2024-12-30 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a38f4a4-d3be-39c9-a5e8-58b6e2a1e3dd | -4.90299 | -41.09901 | 2024-12-30 04:25:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e8903cda-2f43-36a5-9098-ddd3768b5bcf | -12.37254 | -52.49424 | 2024-12-30 04:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| abf235bf-9933-3fce-bdca-9a6ef018d0ac | -20.47643 | -53.67527 | 2024-12-30 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c9e0358-79a9-3930-b6f4-b2fc5cbd2073 | -20.47585 | -53.67806 | 2024-12-30 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07377400-0f0a-35d1-bc80-2d2deb7bd521 | -22.10085 | -52.78093 | 2024-12-30 04:27:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6ac58681-6d8c-3fc1-8878-b8da4bc080f4 | -20.99612 | -51.79253 | 2024-12-30 04:27:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5c1b5f9b-dd0e-3653-91a7-f48ea44892de | -29.60459 | -51.98682 | 2024-12-30 04:29:00 | NOAA-20 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 447a99c6-ce16-36bc-ac7e-5bfe233a3b32 | -24.24305 | -50.73905 | 2024-12-30 04:29:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4d757e39-8b93-37a7-a534-c61a9c2750dd | -29.62826 | -51.96712 | 2024-12-30 04:29:00 | NOAA-20 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 44d6bcb7-09fe-3188-a4cc-d81040a61027 | -29.16864 | -52.01538 | 2024-12-30 04:29:00 | NOAA-20 | NOVA BRÉSCIA | RIO GRANDE DO SUL | Brasil | 4313003 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 71c6c263-f7f4-36a9-b113-9f70f11a845f | -29.74958 | -51.13669 | 2024-12-30 04:29:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 571701b1-818e-36bc-9751-0dbff57652ad | -29.60396 | -51.99078 | 2024-12-30 04:29:00 | NOAA-20 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 93a24c73-c6e6-36b4-bfa0-65de0ac2eba2 | -30.92227 | -53.54807 | 2024-12-30 04:31:00 | NOAA-20 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 35c1eac1-4421-38d5-8085-55cae4924524 | -30.14889 | -52.02425 | 2024-12-30 04:31:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| d9a354c8-0db1-3bb1-8d8a-75bfcf5b4d9d | -31.84588 | -52.83422 | 2024-12-30 04:31:00 | NOAA-20 | CERRITO | RIO GRANDE DO SUL | Brasil | 4305124 | 43 | 33 | nan | nan | nan | Pampa | 0.2 |
| f1cad4a3-eb62-3f0e-8cca-528402c15b7b | -31.8492 | -52.83495 | 2024-12-30 04:31:00 | NOAA-20 | CERRITO | RIO GRANDE DO SUL | Brasil | 4305124 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| a7436dfc-6f68-3585-b7e2-fefd8812e8a3 | -2.91036 | -40.48333 | 2024-12-30 04:55:00 | AQUA_M-M | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b62313ca-dd60-3e40-a9bd-a54c7273b005 | -12.40016 | -39.24474 | 2024-12-30 04:57:00 | AQUA_M-M | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6a08333c-62fc-313f-9173-44b447cbe0ef | -7.83188 | -35.16902 | 2024-12-30 04:57:00 | AQUA_M-M | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 8323b9ab-33d1-3b99-b211-cf47f2d7f7e0 | -6.9716 | -43.00409 | 2024-12-30 04:57:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| e9b5f199-a81c-335f-96d4-6cd11aa053b9 | -7.83022 | -35.1809 | 2024-12-30 04:57:00 | AQUA_M-M | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| d913f56b-71dd-375f-bb13-9a5da2835cb6 | -6.96062 | -43.00245 | 2024-12-30 04:57:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 1a1d175f-167c-396d-b4f4-056ece0e0dac | 3.61214 | -60.63013 | 2024-12-30 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5b23551-809f-31b9-86b5-f567c8642ba5 | 3.20972 | -60.17368 | 2024-12-30 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99d41d3c-ecb8-37e8-8770-74662a63823f | -1.64665 | -45.86462 | 2024-12-30 05:16:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d83c7c92-6613-37d5-ada3-0508a329bc3a | 3.6138 | -60.6282 | 2024-12-30 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3e77694b-b4ed-36a0-b014-9d8e43485182 | 3.61148 | -60.62567 | 2024-12-30 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e703e60a-4f20-33c7-a407-3d7c82c3de91 | 4.23525 | -60.88726 | 2024-12-30 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71359165-9a04-3aaf-96a7-c6fd257c556f | -1.64747 | -45.85921 | 2024-12-30 05:16:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README4.md)
