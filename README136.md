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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a541e5f6-f39e-3c6b-8ba8-abcc8c3c1ba6 | -8.7732 | -45.6529 | 2024-10-14 14:25:55 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 85a37e18-fdb8-35d9-ac3a-c46e7034190d | -8.7814 | -46.4847 | 2024-10-14 14:25:56 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 13c7dc06-a1c8-3d67-a163-1759b74bc0f7 | -9.1216 | -46.4265 | 2024-10-14 14:25:57 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 8ddbcb1f-3195-3068-922c-e8ede9289e9d | -9.4175 | -45.5134 | 2024-10-14 14:25:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 56cc67f7-76e4-3658-86ef-e86e43d76fae | -9.4365 | -45.5112 | 2024-10-14 14:25:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| a26ef68a-465e-31d6-9974-b16e2f071144 | -9.4888 | -45.8228 | 2024-10-14 14:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| cc8cda33-1d57-34e1-a5e2-ee5c18d0ea48 | -9.3149 | -46.0908 | 2024-10-14 14:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| e162d5e9-b984-3226-be4a-2995caf17682 | -9.4885 | -45.8454 | 2024-10-14 14:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 1d1ab11e-f0f1-3db3-9662-9c93da3aa130 | -9.437 | -44.1554 | 2024-10-14 14:25:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 021704a1-1ae6-3164-82c2-3a3f06f56dac | -9.418 | -44.1577 | 2024-10-14 14:25:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 11c2cf7c-de56-3fd7-902c-fe2daa5c79f6 | -9.4699 | -45.8249 | 2024-10-14 14:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 22f11721-be9b-3831-bebe-98af16026a2a | -9.6974 | -47.1445 | 2024-10-14 14:26:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 18dc6f6d-5934-3c91-add6-331a340f4058 | -9.9395 | -47.4059 | 2024-10-14 14:26:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| a1641279-510d-3ab4-ae9d-c48813419ae3 | -10.1637 | -46.3079 | 2024-10-14 14:26:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 1361d1d2-a992-3ff0-8f7f-5a3025800531 | -10.183 | -46.283 | 2024-10-14 14:26:03 | GOES-16 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 698ec286-5b4b-329a-b599-b8f71513bcfe | -10.0738 | -47.2798 | 2024-10-14 14:26:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 9c2a5063-0476-3c91-93a3-d380e46d8132 | -10.2641 | -47.2134 | 2024-10-14 14:26:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 9aae36f1-03a5-3b56-844c-fd2d7b353435 | -10.2854 | -47.0551 | 2024-10-14 14:26:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 384.5 |
| 03f96bc8-a40e-3b46-9199-013d61c8331a | -10.2851 | -47.0774 | 2024-10-14 14:26:04 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 5973d4cd-6326-3938-8506-3989cd138814 | -10.9311 | -44.6789 | 2024-10-14 14:26:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 689b19fb-70ad-348c-b1c1-8317ecd56906 | -10.912 | -44.6816 | 2024-10-14 14:26:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 5e9705c4-e730-3b79-95e6-345031eb6c0c | -11.2254 | -44.2186 | 2024-10-14 14:26:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| ed235072-b426-3073-9f16-ff75b69757df | -11.245 | -44.1924 | 2024-10-14 14:26:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 3ce5af74-07ab-3781-8ca6-68c83e9d5ccf | -11.2637 | -44.213 | 2024-10-14 14:26:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| da55b9e2-d634-3fff-9508-23a05d19d658 | -11.7365 | -44.5393 | 2024-10-14 14:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 59a75ba9-99f0-36d7-85c6-c0046d445c1a | -12.1073 | -43.1861 | 2024-10-14 14:26:14 | GOES-16 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 4324c703-88a0-3c3d-979c-a58ea7d67c34 | -12.3997 | -53.1147 | 2024-10-14 14:26:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 05b04bfa-ff7a-3738-bc43-42d81d628e05 | -12.4376 | -53.1315 | 2024-10-14 14:26:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 48ddd4c3-f7ad-3f7f-99e1-2b71cc5b45ba | -12.4182 | -53.1544 | 2024-10-14 14:26:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 48a64cd2-7b0f-353d-a91e-c916d30c9a97 | -12.4185 | -53.1335 | 2024-10-14 14:26:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 63a50167-02ea-3b87-a787-2b410efa773d | -12.5962 | -44.7783 | 2024-10-14 14:26:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 128.3 |
| f85dfbcf-c557-33b9-892c-b9f45198ad5e | -12.4566 | -53.1294 | 2024-10-14 14:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 8c7723dc-6258-3377-a9d5-be987ef33fbc | -12.7626 | -47.1981 | 2024-10-14 14:26:18 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f0c54230-81db-32cc-9040-a512770370e4 | -21.5621 | -48.0058 | 2024-10-14 14:27:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 8bf7153e-c84b-31cf-93a2-7c1f608ed57e | -2.6303 | -49.0767 | 2024-10-14 14:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 9cd9b317-85fd-3f20-b2d6-90ee687b3139 | -2.6119 | -49.0772 | 2024-10-14 14:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 7f06d3a3-7949-39e9-8831-02d8c0713c6d | -2.6118 | -49.0985 | 2024-10-14 14:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| e8b9c6e3-f657-328c-8726-d6e9cc31142e | -3.4169 | -43.3403 | 2024-10-14 14:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 7c966e1b-6cf9-314a-aaff-25a779cc5230 | -3.9416 | -49.4365 | 2024-10-14 14:35:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| a3772c22-19ba-30e0-a368-febd81a5e458 | -3.9219 | -43.1525 | 2024-10-14 14:35:28 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 593fa619-2e75-3a1c-aacf-7971b59d6a5a | -4.1149 | -48.2299 | 2024-10-14 14:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| ee49d909-2235-327c-852f-6c6318cb6b67 | -4.0957 | -42.2969 | 2024-10-14 14:35:29 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| 5587360b-b83d-3f1a-a1b0-43010f589ebe | -4.1148 | -48.2515 | 2024-10-14 14:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| c69a9954-a7d0-39bc-94bf-20e55149c57f | -4.1716 | -48.0327 | 2024-10-14 14:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| ac457f04-bc3b-3ea3-97e5-18d830e4c573 | -4.8648 | -47.1037 | 2024-10-14 14:35:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 8ad20842-69d5-33bb-83d8-e45d8aebf2bc | -5.2485 | -48.0641 | 2024-10-14 14:35:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 45821a33-b37f-3306-bd01-47bf1b0bc17a | -5.3226 | -43.3687 | 2024-10-14 14:35:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 9eba2de9-56e8-3bfe-a040-0920fa207166 | -5.2486 | -48.0424 | 2024-10-14 14:35:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 955cb4e3-48e0-37ee-bcb3-b91c426ebedd | -5.2797 | -46.3725 | 2024-10-14 14:35:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| e335dd32-47d5-3882-9325-3bcf0a9f9641 | -5.2984 | -46.3714 | 2024-10-14 14:35:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 0cff72ad-c228-379b-899d-e35d8279e985 | -5.2799 | -46.3503 | 2024-10-14 14:35:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| cb6b77fc-0e99-35f5-b16f-d9d993a912ca | -5.2985 | -46.3492 | 2024-10-14 14:35:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 633e8e94-5f5b-3afb-a2ed-3a4ee8069149 | -5.7564 | -43.0561 | 2024-10-14 14:35:38 | GOES-16 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 502ce0c8-6fad-3b76-bae3-e2752a209e17 | -5.6938 | -43.7597 | 2024-10-14 14:35:38 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 2f95d512-1d63-3bd6-8950-ca202ffb4709 | -5.675 | -43.7611 | 2024-10-14 14:35:38 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| eda7a173-431b-3b42-b8a6-199d690dacc1 | -5.9971 | -45.4059 | 2024-10-14 14:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| c959e89c-c7e8-3474-af0c-966f7b761f42 | -6.0667 | -45.9852 | 2024-10-14 14:35:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| f5592c34-64ac-3528-88a9-bf4f75d8b58f | -6.0158 | -45.4045 | 2024-10-14 14:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 5b8b3587-9d1f-3854-a5c0-cd0704c53670 | -6.2734 | -43.8994 | 2024-10-14 14:35:41 | GOES-16 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 6f27f4a1-6e22-3a0d-bbcf-ddf6820621d0 | -6.24 | -43.4844 | 2024-10-14 14:35:41 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 069975ae-a1e4-3745-9e38-eb29457925fe | -6.2863 | -42.6125 | 2024-10-14 14:35:41 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 43.8 |
| c87e01f5-bacf-395e-8272-a51af3921560 | -6.6486 | -43.914 | 2024-10-14 14:35:43 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 085888b9-b9d6-3656-8491-7bce0aa2a009 | -6.5385 | -43.6685 | 2024-10-14 14:35:43 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 8beb9904-4697-3f95-8e86-d3fbc7e653c8 | -6.8113 | -42.7542 | 2024-10-14 14:35:44 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 44.3 |
| 1be7a3fc-02bb-31fd-ac1e-fcbde38a1e25 | -6.9313 | -43.8194 | 2024-10-14 14:35:45 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 21a00b95-b25f-3529-afc5-de533c67b483 | -7.1706 | -42.6251 | 2024-10-14 14:35:46 | GOES-16 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| a248822b-85e4-38c4-8e4c-5eb51bfb53bd | -7.1328 | -42.6288 | 2024-10-14 14:35:46 | GOES-16 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| ec06bd98-d61f-3844-97fb-577d480d12de | -7.076 | -42.658 | 2024-10-14 14:35:46 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 133.6 |
| 411301ec-01ce-38de-9a92-93e65cfd6b23 | -7.1708 | -42.6014 | 2024-10-14 14:35:46 | GOES-16 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| 5793d9ec-2074-37ae-a8ce-228ffd096fb5 | -7.0763 | -42.6343 | 2024-10-14 14:35:46 | GOES-16 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 2fac9500-3fff-31bc-a562-429b99f3e185 | -7.0951 | -42.6325 | 2024-10-14 14:35:46 | GOES-16 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 62.7 |
| 14059291-a463-39df-a689-06d0e91e570a | -8.7735 | -45.6303 | 2024-10-14 14:35:55 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 83bb4ea9-0e7b-3838-bd79-86e0b924c379 | -8.7732 | -45.6529 | 2024-10-14 14:35:55 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| dfc72e2d-6cfa-3fa3-918a-7491202dccd0 | -9.1046 | -47.7377 | 2024-10-14 14:35:57 | GOES-16 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| cff51f56-1680-3946-837f-5ef945094535 | -9.4699 | -45.8249 | 2024-10-14 14:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 29a27c43-0425-3aaf-a460-e01c255b0c48 | -9.437 | -44.1554 | 2024-10-14 14:35:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| db7a8bdd-ad50-37da-ba27-f62c5aa1f336 | -9.3149 | -46.0908 | 2024-10-14 14:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| f411d161-cd40-33e0-aa17-bc2d86180612 | -9.4885 | -45.8454 | 2024-10-14 14:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| a1f652c9-0597-3537-8a43-48c2134ab766 | -9.4368 | -45.4884 | 2024-10-14 14:35:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 0ab9d894-58c0-3840-93d1-431d9025f2dc | -9.4365 | -45.5112 | 2024-10-14 14:35:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 198.7 |
| df3a7014-327f-30dd-8d8e-b054421c7d2c | -9.4888 | -45.8228 | 2024-10-14 14:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 9d6c0028-35f0-352e-9a7f-cc84f539129d | -9.4892 | -45.8001 | 2024-10-14 14:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| df29707d-dc45-3261-8e86-82fcb34c4bcb | -9.4175 | -45.5134 | 2024-10-14 14:35:59 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 58182dc3-309d-35dc-a746-1592dea30e73 | -9.4702 | -45.8023 | 2024-10-14 14:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| b6af645c-23ba-375e-9934-12846c6452e6 | -9.418 | -44.1577 | 2024-10-14 14:35:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 54.6 |
| af7ce44a-7674-3ec7-a745-497f4641664e | -9.96 | -47.2928 | 2024-10-14 14:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 4da538ab-149f-3a8f-80bb-3c4e4e803e0b | -9.9787 | -47.3128 | 2024-10-14 14:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 71bf7132-6d14-3a3d-a7c9-4735ec645b77 | -9.9784 | -47.335 | 2024-10-14 14:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 059774da-a8a6-3f89-b262-0428930504ab | -9.8504 | -47.0162 | 2024-10-14 14:36:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 39cc1d9c-f01b-3fad-ad95-98078a096eb5 | -9.9973 | -47.3329 | 2024-10-14 14:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 63f2de57-9259-35c1-938e-f82f51340578 | -9.9597 | -47.315 | 2024-10-14 14:36:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 02155fcc-df48-3b42-8de2-82f9b21a0477 | -10.0738 | -47.2798 | 2024-10-14 14:36:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 942f9a0d-92ab-3f0a-9c35-1e0c47be68e5 | -10.0163 | -47.3308 | 2024-10-14 14:36:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 201.3 |
| 383366d2-40bc-3131-93b0-acc38f7b3330 | -10.9116 | -44.7048 | 2024-10-14 14:36:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 412.9 |
| 395f392d-2b75-395e-844f-1d4912cfb99b | -10.9303 | -44.7253 | 2024-10-14 14:36:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 36d72130-8e28-3995-9e0a-88794e0acb3d | -10.9311 | -44.6789 | 2024-10-14 14:36:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 9bc7420c-de07-3be9-9c9d-43afdb84beea | -11.245 | -44.1924 | 2024-10-14 14:36:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| dc992653-2d65-37a7-b932-082c35e2d278 | -11.2254 | -44.2186 | 2024-10-14 14:36:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| e6b49085-0747-35ae-a09a-7a355153d881 | -11.2637 | -44.213 | 2024-10-14 14:36:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 384fab18-e31a-3cb4-a1f2-b26a2e173085 | -11.7365 | -44.5393 | 2024-10-14 14:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |


[Clique aqui para ver as próximas entradas](README137.md)
