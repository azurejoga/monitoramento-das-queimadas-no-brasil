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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b9945b8-1b22-34e6-8c58-bd14f22b555e | -21.77232 | -56.29389 | 2026-07-02 04:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6d2a543c-4396-3700-bfef-d9afa850ac1f | -22.79212 | -49.35057 | 2026-07-02 04:21:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f176fc1b-ed67-3658-a590-7b6eee5e5763 | -18.41266 | -53.28702 | 2026-07-02 04:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1990a035-7fa0-3b4c-bf84-6666d4b4121a | -21.80519 | -52.71957 | 2026-07-02 04:21:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a3f7015-944a-33aa-a139-deaff1e3e028 | -21.76579 | -56.29646 | 2026-07-02 04:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 44322a66-cc15-308b-a598-0375a72a99f9 | -21.77978 | -56.2872 | 2026-07-02 04:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |
| fab3b6dc-ee24-39db-ac70-e9a5fd17e0a4 | -19.50113 | -52.73505 | 2026-07-02 04:21:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd6beb45-75b3-3c3b-9d48-e379f4745f0e | -21.7779 | -56.29555 | 2026-07-02 04:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 84158a46-3c27-342f-8dd7-ca6d84891680 | -21.76769 | -56.28804 | 2026-07-02 04:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dcdfdf2d-89fa-314b-b199-ff378584d333 | -20.48372 | -50.52485 | 2026-07-02 04:21:00 | NPP-375D | PONTALINDA | SÃO PAULO | Brasil | 3540259 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9e1a2882-e64f-3916-b870-57fdfe60ba38 | -23.5627 | -47.51034 | 2026-07-02 04:21:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e92166b3-c67b-35b0-bc92-9f6dee2a66b8 | -12.8548 | -44.3625 | 2026-07-02 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 204.7 |
| 42c74169-a0f5-3b15-bf76-4fa521dffde6 | -10.3857 | -46.6855 | 2026-07-02 04:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 154.3 |
| b1ee19d2-2fa8-3f35-8e81-71c2737fa783 | -10.3667 | -46.6878 | 2026-07-02 04:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 3641eb56-0f4b-39ba-8a9a-49c24e1e4d93 | -12.8552 | -44.3389 | 2026-07-02 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 379.1 |
| c80b8a07-39b7-34b6-bb9a-d615481990ac | -10.3663 | -46.7102 | 2026-07-02 04:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 230.3 |
| d75cd6ea-7cc9-3d76-a0b1-ac777859bd6b | -12.8746 | -44.3357 | 2026-07-02 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 282.4 |
| 197bc6a6-6a31-3514-9b91-1942bed94fbc | -10.3853 | -46.7079 | 2026-07-02 04:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 152.7 |
| c8edb229-77c9-31b7-a02e-fbb370276631 | -12.8741 | -44.3593 | 2026-07-02 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 191.0 |
| 05c04358-a59e-3a05-b7f5-a33051168342 | -12.8557 | -44.3154 | 2026-07-02 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| a0c9edba-8fdd-3c1a-b150-6bde8e1a5c2d | -21.7823 | -56.2976 | 2026-07-02 04:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 483ee0d1-84ab-33ae-9996-4335d2b375ce | -10.9397 | -43.0593 | 2026-07-02 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 8ae6a066-a083-384c-a0f3-c0c6be0600ba | -6.92586 | -43.71699 | 2026-07-02 04:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 28d96586-7b2e-341b-a409-7de6b4ef12e0 | -4.57893 | -48.02628 | 2026-07-02 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13457ab1-8798-3899-9bc4-365fb400c1ab | -4.0027 | -48.05893 | 2026-07-02 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1c8e48a5-482d-352a-8e56-4b7f6b714b90 | -2.4872 | -47.09185 | 2026-07-02 04:36:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67dfb61e-c907-34e4-8b92-51c85eae0626 | -4.28774 | -48.36088 | 2026-07-02 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b074963-11ae-3214-afbf-84c3a8b987cf | -5.8886 | -46.96072 | 2026-07-02 04:36:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ee1532e0-cce0-3c3d-9322-9029b5ef54f5 | -4.34897 | -47.76335 | 2026-07-02 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5059ff1a-7737-34e4-b937-005393d46d17 | -5.79741 | -45.03052 | 2026-07-02 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ef3caf4-f645-3263-8cd4-3bcfef69c8ba | -3.50716 | -48.03399 | 2026-07-02 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86dfde02-9841-39dc-a0cc-cbfdee8698f6 | -5.29805 | -43.70742 | 2026-07-02 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5477c884-97a7-3d51-aa0f-473790e51c0e | -4.25861 | -48.54325 | 2026-07-02 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 855075a3-f552-33ab-8a7a-0403312d5432 | -5.81515 | -43.79284 | 2026-07-02 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43441df7-8ca1-3ed2-ad2c-4b66810b66db | -5.82361 | -47.89116 | 2026-07-02 04:36:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5ab9baf-6668-397d-8fd5-2fc4af49aa3e | -3.41345 | -41.70508 | 2026-07-02 04:36:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 9a1eeb4d-6112-31be-ba79-6ceeec6420bd | -6.91894 | -43.72264 | 2026-07-02 04:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9c0bf7ba-082e-37ca-8a37-48b86f171bdc | -5.46901 | -45.4192 | 2026-07-02 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8e342e0-31c0-3e92-97b6-688ff76a1f1e | -5.78789 | -45.04544 | 2026-07-02 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27063db3-867e-3d0e-b51b-ae44d36ee869 | -3.41286 | -41.70889 | 2026-07-02 04:36:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ccd333c3-5313-32dc-91e3-5b2553a1b3fa | -4.28109 | -48.35981 | 2026-07-02 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a40bded9-3e41-30ad-99f9-b56e9eb85655 | -5.79619 | -45.03851 | 2026-07-02 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e12f313c-bfe2-38dd-b021-abc67a0499e7 | -3.47419 | -39.5829 | 2026-07-02 04:36:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4f6042d7-1d37-3217-88a7-9ec7cad2f358 | -6.47063 | -42.99255 | 2026-07-02 04:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e72be4e-8cce-37b9-822b-f0802936baa0 | -5.29781 | -43.709 | 2026-07-02 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c60d77f7-7ab9-33a3-8e30-e8dacc78c6b7 | -5.79204 | -45.04197 | 2026-07-02 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56900e2b-8f4b-3de9-910d-09dd2869e9f4 | -6.9228 | -43.72321 | 2026-07-02 04:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| afa61fc2-533e-34b1-975b-b935b3bc5bdd | -3.5138 | -48.03502 | 2026-07-02 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d9249b9b-94b3-35c6-a710-3983bb9138aa | -5.47822 | -44.10506 | 2026-07-02 04:36:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f30dc24-e502-329c-ba4b-28690c3b55f0 | -6.91508 | -43.72206 | 2026-07-02 04:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1baabcd1-e771-38ad-a815-246dca0ee0ee | -3.51712 | -48.03554 | 2026-07-02 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a350d631-0451-3eef-9e6a-50229ca88f4a | -6.92666 | -43.72379 | 2026-07-02 04:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3ef19da-22ef-3cea-932a-d5d7347c672e | -3.50661 | -48.03745 | 2026-07-02 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71629589-5cb2-3bf3-b15e-f5e58def4927 | -6.59381 | -43.88594 | 2026-07-02 04:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53d5ccd1-2664-32f2-bcd2-71c96e968f54 | -6.9235 | -43.7184 | 2026-07-02 04:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6a208d1f-9ebc-3bd9-86b4-85242552d2b4 | -7.00279 | -42.76867 | 2026-07-02 04:36:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 40b1606a-50e3-3671-a15a-95c6832173f8 | -3.41823 | -41.70187 | 2026-07-02 04:36:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 5401eba5-55d2-300f-bfe2-7a4e0010fdb2 | -3.41763 | -41.70569 | 2026-07-02 04:36:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| bacf46c5-e1fa-355e-82e3-ec76ee13e0e6 | -7.00885 | -42.78452 | 2026-07-02 04:36:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1c90ee1f-146b-354b-9fbf-4cd62ad963ec | -3.50993 | -48.03798 | 2026-07-02 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 48292837-5eed-3e13-8943-fc0cba745910 | -6.92126 | -43.72124 | 2026-07-02 04:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7370c1fd-11a4-30d9-b827-b1b4e013ad65 | -5.7885 | -45.04145 | 2026-07-02 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ddd6268-cc45-3c23-b9fc-a85a2e5c95f0 | -5.79326 | -45.03399 | 2026-07-02 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f886a0d4-f55d-381e-989a-3fd92e92fe24 | -3.66888 | -48.98115 | 2026-07-02 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37b0cb26-85da-3fe6-b452-32ae351c6772 | -6.57955 | -47.47299 | 2026-07-02 04:36:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3e9d17e-f015-3694-bca8-7b49ca7bd4a7 | -5.81065 | -43.79687 | 2026-07-02 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e49db101-bf1b-3cfc-a46a-b96afc97e328 | -2.48444 | -47.0879 | 2026-07-02 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86ecf0ae-49a6-3bbf-9fdb-f4e0d6952f40 | -5.37421 | -43.37917 | 2026-07-02 04:36:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f822faf3-338b-34d7-ae8f-bde6e8d6fe9c | -5.29402 | -43.70844 | 2026-07-02 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 091c7a26-f266-3b03-8b9b-eac3fb4f3346 | -6.34278 | -43.65468 | 2026-07-02 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20a086d8-fd46-3387-ab6e-9ee6ec813cd0 | -7.00582 | -42.77661 | 2026-07-02 04:36:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f8eff8d0-3f65-3534-9f29-4e639da63377 | -6.25426 | -49.87721 | 2026-07-02 04:36:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a797cb4a-3068-3d0c-8e59-5cba4e6e6458 | -5.82746 | -47.88823 | 2026-07-02 04:36:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5b20d16f-9b41-31b3-aa7d-30dd869efb78 | -5.56202 | -43.82875 | 2026-07-02 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de63e078-150c-3470-877b-85d7927ba983 | -5.37807 | -43.37978 | 2026-07-02 04:36:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56361ebe-b2b7-39b7-8999-3b7f3f6580d4 | -6.93052 | -43.72436 | 2026-07-02 04:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4c68dae-20fb-3c02-907f-0d300b33e032 | -3.47014 | -39.57684 | 2026-07-02 04:36:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 823db3cb-d7b0-37cd-9cb0-9ec48a61789f | -4.00878 | -48.06342 | 2026-07-02 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0839e5cb-682a-31d5-9b70-de6f3b0cd1af | -3.41705 | -41.7095 | 2026-07-02 04:36:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| b3450dd9-f9fe-32f0-b56e-321a0e3d607e | -5.88751 | -46.96772 | 2026-07-02 04:36:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc766926-386d-3d00-b1b5-886cbde7dc50 | -4.57948 | -48.02282 | 2026-07-02 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85185bc7-cb2b-36b4-9cab-31ec71a07f45 | -5.29427 | -43.70687 | 2026-07-02 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd15d357-6a34-37d3-b058-54ce3829f29c | -3.25044 | -50.82002 | 2026-07-02 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b419ba71-81b6-3f09-8cb6-a9c94d04e3d4 | -3.51325 | -48.0385 | 2026-07-02 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d0bcb620-c0a8-3005-8c23-396c4c6c0da1 | -6.25366 | -49.88096 | 2026-07-02 04:36:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c01549d8-d0cf-3ce4-8a9e-16c2f57932e7 | -5.47499 | -45.4155 | 2026-07-02 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 786b613e-1470-3597-b900-9dbac62a22eb | -4.94534 | -48.2441 | 2026-07-02 04:36:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5e5b8d56-c49d-3bc6-9dd0-bd576211d586 | -5.79676 | -43.63252 | 2026-07-02 04:36:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| faedef68-c841-391a-b805-eeb81051ce6d | -6.59001 | -43.88532 | 2026-07-02 04:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe3972e4-1c03-34a1-a6c2-853748172116 | -3.46935 | -39.58213 | 2026-07-02 04:36:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc868d44-54ac-350b-98a3-3f417fcd0ffd | -3.41404 | -41.70127 | 2026-07-02 04:36:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| b8bcca39-b007-345e-8449-75a3e4c96abb | -4.00546 | -48.06292 | 2026-07-02 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b12fa67c-c621-3806-ab3d-b56ada5f2c1f | -7.00226 | -42.77234 | 2026-07-02 04:36:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3acb0090-893e-332a-9672-ae4a54e102c5 | -3.67227 | -48.98168 | 2026-07-02 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90db3ec9-af86-37f4-beb4-bffce8d6c940 | -5.79143 | -45.04596 | 2026-07-02 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d2f4004b-f495-3655-a9d9-c64f7db7e0d7 | -5.7968 | -45.03452 | 2026-07-02 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2403ba1b-eee6-33e4-9d24-7e3bbc3c3941 | -6.9174 | -43.72067 | 2026-07-02 04:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| b5b22230-801e-3b1c-97b6-3b5043dbe263 | -5.88418 | -46.96719 | 2026-07-02 04:36:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8ab16a8f-395a-30d5-9126-f4e2d92da00a | -6.91964 | -43.71782 | 2026-07-02 04:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7f84ae62-654f-3529-9224-331bf0a77599 | -6.99271 | -42.89414 | 2026-07-02 04:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README16.md)
