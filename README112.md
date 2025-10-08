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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95fc7cc5-b8c9-3986-9891-96212dc32ccc | -5.021 | -43.645 | 2025-10-08 14:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 00ad2204-c251-3fa4-b899-1a1e95eb1b16 | -12.0118 | -45.2161 | 2025-10-08 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 5cfe4f10-21b5-3f89-b8d3-c640102d78cc | -3.9135 | -41.5447 | 2025-10-08 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| 7b6d62b2-673a-3a37-a874-c47dc3e3a270 | -12.4099 | -51.1344 | 2025-10-08 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 148.4 |
| c9745202-07c8-3e42-a676-5c452cf6e0e3 | -11.7656 | -50.932 | 2025-10-08 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| dfdfc9ea-7d25-3f01-b3cd-0236ad5c59be | -7.5463 | -44.3164 | 2025-10-08 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 77109e53-2ada-3b70-9ab7-78dd28902e82 | 0.9293 | -51.1248 | 2025-10-08 14:40:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 3f6bee69-5c71-3925-b906-ccdb64550a38 | -12.8969 | -50.5398 | 2025-10-08 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| a508638d-4139-3c94-88bb-2a68ad3935cf | -3.8945 | -41.5938 | 2025-10-08 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 779f5397-9b5b-3d17-b72b-12434ef5009a | -8.1804 | -43.3445 | 2025-10-08 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 170.2 |
| fc96f649-3aaf-3116-ab56-ede403ba2322 | -4.0627 | -44.5062 | 2025-10-08 14:40:00 | GOES-19 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| cfa63c66-ca27-3491-9956-c4911eed5126 | -11.6888 | -50.9833 | 2025-10-08 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 3f963a25-b8b1-3d85-9bc1-a9c4f66372f4 | -3.2901 | -42.6213 | 2025-10-08 14:40:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 1c270010-07ca-3ae7-b835-3c315b10093f | -7.7922 | -44.2229 | 2025-10-08 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 154.4 |
| eba2a81c-73d1-3c80-81cd-28c9b9b88cb9 | -3.8759 | -41.5708 | 2025-10-08 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 53d23dac-7a9d-328d-8703-1378f9ae727d | -4.0567 | -42.5354 | 2025-10-08 14:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 116.2 |
| 876e2814-c1db-33b0-8bc0-1caf6e25b7c6 | -11.7573 | -51.5059 | 2025-10-08 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c491d1aa-5b8a-3670-9d33-8d6d9bf48751 | -17.5711 | -46.064 | 2025-10-08 14:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 110.6 |
| dd4e404e-6684-3730-9a6a-0511c08e14d8 | -4.0626 | -44.529 | 2025-10-08 14:40:00 | GOES-19 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| f2b620b8-b04f-360f-8fc4-aecd9c2a6569 | -17.284 | -58.0793 | 2025-10-08 14:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 13889e15-58bd-338a-9f9f-3fc8858fea04 | -7.4663 | -43.1144 | 2025-10-08 14:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |
| 730c000b-302a-3682-8bee-55e47c8c40c7 | -13.2662 | -48.0409 | 2025-10-08 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 52fe7a69-77d5-3bd9-bbfb-d66085c87853 | -10.8573 | -53.7425 | 2025-10-08 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 037665ca-06f4-3171-9b41-deafc7e62509 | -11.7466 | -50.9342 | 2025-10-08 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 869abba9-145f-3647-a16e-236fec0a156b | -18.6707 | -43.9005 | 2025-10-08 14:40:00 | GOES-19 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 05d9839e-dd11-3531-a1f9-ae32432073d3 | -8.595 | -46.3246 | 2025-10-08 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| adc60ee8-87e6-3cf5-ba72-4a57b798c516 | -14.8641 | -51.4373 | 2025-10-08 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| b09ee874-7f9b-3a2f-bc56-a693fc5f21ec | -3.8948 | -41.5458 | 2025-10-08 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 135.5 |
| 1ada12cf-0061-39dc-8358-88007728ee5f | -12.6286 | -50.5734 | 2025-10-08 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 42e20e31-2ff4-3e77-981e-a70281363ad6 | -4.0382 | -42.5129 | 2025-10-08 14:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 1652b8bc-856d-3680-91e7-680ab5704f22 | -12.385 | -50.281 | 2025-10-08 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 567c4667-1ebf-34f0-af8d-340472eee221 | -13.2855 | -48.0381 | 2025-10-08 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 674b02aa-bb3c-38eb-afff-0289049e052c | -12.5297 | -54.7326 | 2025-10-08 14:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| aa3e99b4-e88e-323a-99d8-4f6fa4ee225a | -14.8835 | -51.4346 | 2025-10-08 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 0813ce46-e607-34d8-94c5-91aac4b3fc61 | -4.7624 | -43.22 | 2025-10-08 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 8bb062c3-d421-3686-a6ad-6aaa5f24de35 | -3.8048 | -43.9923 | 2025-10-08 14:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 49217a06-8d19-3ca1-ae2c-514aede174f0 | -7.4666 | -43.0909 | 2025-10-08 14:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 126.1 |
| 5981eb9f-e37c-3a76-a7ce-0d66afa39235 | -11.6455 | -44.2731 | 2025-10-08 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 38809687-8b34-30b5-b1a1-80798d39023f | -3.8761 | -41.5468 | 2025-10-08 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 126.5 |
| d430e93c-2c2f-386e-8583-c67312297eca | -18.0388 | -44.9679 | 2025-10-08 14:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 347.0 |
| 7f69deb7-3200-3002-b354-5791d204495f | -17.8611 | -57.6436 | 2025-10-08 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.3 |
| c77f2186-bae8-3cfd-9372-7603334c2975 | -8.5398 | -46.2181 | 2025-10-08 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 75b61039-ff5c-3a80-9dda-882d9db71720 | -17.2637 | -58.1223 | 2025-10-08 14:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 4037c3ef-cd46-3ac7-ac67-8dcaa476d8f7 | -17.3037 | -58.077 | 2025-10-08 14:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| 34c30364-06f3-3a24-aa13-485704b4af2a | -7.2964 | -44.799 | 2025-10-08 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 6ee70238-a27f-37ce-93e0-9a9fde270e1a | -12.3908 | -51.1366 | 2025-10-08 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 75799198-d8ba-3c1d-9e9c-0367e77c5d93 | -12.5109 | -54.714 | 2025-10-08 14:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 163.3 |
| 8f9249ae-286d-348d-a709-a670c32237f8 | -11.4153 | -50.2023 | 2025-10-08 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 0f66fa71-cd20-3c84-8577-8b28c4d5a7e2 | -4.4446 | -43.2164 | 2025-10-08 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 78ee6d40-c345-3e8d-934f-8fbc7aa58217 | -7.8307 | -44.1497 | 2025-10-08 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 95b1786d-7481-3f18-9c31-4550da51de44 | -3.8946 | -41.5698 | 2025-10-08 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| b9a85165-e088-3760-8e22-c45c36e5619c | -10.8524 | -47.2094 | 2025-10-08 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| ce5ea14d-ba9d-3132-bd09-56f20da34e27 | -12.1576 | -51.4399 | 2025-10-08 14:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 183c6f1a-4913-3111-a661-21ca184ea203 | -3.2713 | -42.6457 | 2025-10-08 14:40:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| e35edf7d-5399-3e67-902f-b4fac44a4fbe | -17.304 | -58.0566 | 2025-10-08 14:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.7 |
| 2d6308a1-028b-3714-9419-d6cb70ef2831 | -5.325 | -43.0884 | 2025-10-08 14:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 2593af7c-5193-33b5-ba52-512e6eb544fe | 0.9292 | -51.1455 | 2025-10-08 14:40:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 98.5 |
| b0f2534a-952c-364f-aff5-f2efa3b67a49 | -11.6243 | -50.1998 | 2025-10-08 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 52c011d0-3866-3465-af65-1f04a0eeca5d | -17.9979 | -45.0011 | 2025-10-08 14:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 48948d0d-bcd1-385a-b629-913bd2dd5f73 | -7.7924 | -44.1998 | 2025-10-08 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 64280e1f-52c1-32fd-88fe-a8f32e1d3760 | -11.2024 | -54.8567 | 2025-10-08 14:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 349bee01-2baf-3f87-bd84-f234ad2bf5d9 | -18.0209 | -57.5214 | 2025-10-08 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.8 |
| bebb5790-c33c-3026-9038-2854c3d4ec11 | -10.3665 | -47.9978 | 2025-10-08 14:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 96299360-dfbe-38c9-a39d-f14375b09d5d | -8.5207 | -46.2425 | 2025-10-08 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 7ea00fa6-b492-3f52-9f3d-9560d9285d30 | -3.4366 | -43.1532 | 2025-10-08 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 2c96c5cb-3fdd-3475-b02a-adf09e5a3f36 | -7.8896 | -45.5163 | 2025-10-08 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 210.5 |
| 003fe40f-200e-378e-abf9-b6bb0cdc8d9d | -13.3048 | -48.0352 | 2025-10-08 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| a7d0862c-830e-32e2-8e42-c4b5c7a5ee43 | -14.7184 | -46.0636 | 2025-10-08 14:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 119.2 |
| ae64cbc1-88c6-3d02-a1b4-f2843915270b | -9.1975 | -47.8381 | 2025-10-08 14:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| e1353bc1-1ac4-32ec-a787-b77c10113ce7 | -9.9146 | -49.2456 | 2025-10-08 14:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 2858f79e-58d2-3729-bf94-670f195321e5 | -12.3911 | -51.1153 | 2025-10-08 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 3b249807-2698-3598-b7c2-36961536c463 | -7.4672 | -43.0438 | 2025-10-08 14:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| c75f1725-7d13-39d9-ba07-d025d6de4cd8 | -3.95 | -41.6864 | 2025-10-08 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| c2b7f4a1-5421-35f8-ab6a-d7e6e19d95ce | -11.0098 | -50.7171 | 2025-10-08 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4d50719c-41bb-386a-98a9-09d770311550 | -14.3161 | -52.9764 | 2025-10-08 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| fbbfbc4c-5ca6-3b16-942a-56be5e361bf4 | -14.8447 | -51.4401 | 2025-10-08 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 9c241c9a-831a-379e-b2a2-c1eae4acaddd | -12.5487 | -54.7307 | 2025-10-08 14:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 1be99598-240a-3ebc-b618-8533c4e2fb08 | -7.7736 | -44.2017 | 2025-10-08 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 357787fd-1839-34eb-9fd1-6f4a6dbaa599 | -4.6291 | -43.554 | 2025-10-08 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| a8bdab06-af0a-34be-be00-d5cc493f6285 | -13.3517 | -47.5818 | 2025-10-08 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 9899f269-b0b2-3953-9f8b-7a80ab6527d7 | -12.3655 | -50.3049 | 2025-10-08 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 315b0d79-8404-3acd-a15d-378fcff0f3be | -13.2438 | -47.1714 | 2025-10-08 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| b8a660d9-bf79-35b3-b01c-5c172c2f1acb | -7.7919 | -44.246 | 2025-10-08 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.4 |
| d93dc2dd-c3f2-3a30-b296-937b6627bd0b | -14.8637 | -51.4589 | 2025-10-08 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 1c4e030a-7d58-3645-a8c6-b0b42a2b80bb | -11.7576 | -51.4847 | 2025-10-08 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 69f364d5-843d-355e-93a3-1e0fdd09909b | -4.0569 | -42.5118 | 2025-10-08 14:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 168.4 |
| 849ebe1c-080e-3153-8089-6faea90e9ccd | -3.8573 | -41.5479 | 2025-10-08 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 132.9 |
| 5a6858e8-d5b5-37ec-b1de-c4dc624f1200 | -11.1646 | -54.86 | 2025-10-08 14:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 738f3792-5faf-3fe5-ba43-726a7da4c95b | -17.2837 | -58.0997 | 2025-10-08 14:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 3522346f-e33d-3cd2-ab73-54343a7f0a28 | -10.9109 | -47.1129 | 2025-10-08 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 759517fa-fdfa-3859-8791-f1eac8fa4c10 | -12.5107 | -54.7345 | 2025-10-08 14:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 166.0 |
| fa27a607-0f8e-3286-be30-b8491191edac | -18.0394 | -44.9438 | 2025-10-08 14:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 371.0 |
| b2749033-ef48-3637-a2e6-5f044e094458 | -13.3706 | -47.6013 | 2025-10-08 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| b54775cb-6f06-346e-8fb7-70abf6630aac | -12.6478 | -50.571 | 2025-10-08 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 2b062c68-8f4b-3e27-b1c4-b5e8a77200ee | -12.3846 | -50.3026 | 2025-10-08 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| a6c913b0-39d0-348f-8fb8-3d5c1491b717 | -3.9134 | -41.5687 | 2025-10-08 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 0c17425f-2be5-3c5a-8516-369d44abfa09 | -11.5111 | -51.4693 | 2025-10-08 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 0e928000-ef67-3931-a585-5f0ab47ddd69 | -7.793 | -44.1535 | 2025-10-08 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 081d62cd-c629-3a56-b1a2-efc218b97bc8 | -13.3513 | -47.6042 | 2025-10-08 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 07f8c717-1af0-3da5-974a-f2a0ac2c1db2 | -5.852 | -42.8608 | 2025-10-08 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |


[Clique aqui para ver as próximas entradas](README113.md)
