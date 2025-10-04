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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| baf9381f-4ed6-3c34-a18a-8565a82772b0 | -9.34454 | -54.52713 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a7ccb1ff-bf55-3e4f-abc7-23d170292679 | -13.18229 | -50.93181 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 42.4 |
| d61664e6-a702-326a-8108-bfb32860c3fa | -7.87385 | -61.68261 | 2025-10-04 05:33:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 465a23c2-5930-33f5-a7e6-d042844f65a0 | -11.41593 | -55.06837 | 2025-10-04 05:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17defce0-a498-3145-9682-c8c34d95b5fe | -9.63297 | -63.24368 | 2025-10-04 05:33:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd8866b0-eb88-3b56-b1d9-3172fbaab9ef | -10.32512 | -50.33884 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 591b2e3e-73eb-35e0-ae75-8cae7df1d6cc | -8.61659 | -54.97985 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11f121d4-d3b4-37c1-921e-4b75ec4c8dad | -14.98369 | -49.97076 | 2025-10-04 05:33:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ac60d2c2-1cd1-38aa-864c-aa6c61700c39 | -9.92633 | -50.90173 | 2025-10-04 05:33:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0473b6a-59bd-3a16-930a-6ae990103c23 | -9.08534 | -63.70162 | 2025-10-04 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a09bf63-0cf2-32b2-9244-7e29a9ec4ea3 | -11.07558 | -62.84484 | 2025-10-04 05:33:00 | NPP-375D | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e555f35e-b1f7-37bd-aad7-b4881eb9f789 | -15.20987 | -56.83678 | 2025-10-04 05:33:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57793bef-3e85-353a-8153-686656f36a18 | -8.62409 | -54.99697 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 125ca253-2435-3a66-92e1-9728d1ff2c4f | -12.94065 | -54.72899 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfbf21be-6ef6-3686-affc-d0874004b707 | -14.80618 | -59.71782 | 2025-10-04 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7292df8-3eca-3b1d-8388-6091fc79c819 | -9.99611 | -60.01239 | 2025-10-04 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a32dd9b4-8958-3dec-a1cc-b7ab0607ebb2 | -9.194 | -59.55105 | 2025-10-04 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03cf064d-87ae-32b5-a582-00a5a71b5aa5 | -10.83388 | -57.19733 | 2025-10-04 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03ed2312-7388-36bc-bcac-dbe0e55b7153 | -8.61395 | -54.96321 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce66ae17-24cb-366e-b44e-ce622feec5a8 | -8.61734 | -54.97449 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c86dd12d-638c-3be6-be6e-8870b868ef75 | -9.93963 | -50.89856 | 2025-10-04 05:33:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9428ab23-6847-370b-8d62-d9d8b7be535c | -15.60993 | -52.47607 | 2025-10-04 05:33:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ae61b48-5b53-35f6-9961-85eb7601b39d | -10.33331 | -50.32783 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4b227647-4c98-37ae-b999-063c2d3dd14a | -9.01622 | -63.58487 | 2025-10-04 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 270baa20-6785-3fd7-b1df-29c9a495d0a3 | -9.01899 | -63.58896 | 2025-10-04 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3ea802d-1ae9-3364-9d0e-5f4ab5adb2bb | -11.12619 | -55.44997 | 2025-10-04 05:33:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e46a7442-0e2d-35e3-adc8-fe308528e6a7 | -9.45723 | -56.65289 | 2025-10-04 05:33:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc2d4ff9-d9b9-3ddd-87c2-c2f9d3d58ef0 | -9.31391 | -54.53471 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a39967e-d982-37d7-ad96-504807b7ca7f | -9.16348 | -65.49072 | 2025-10-04 05:33:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd4c5690-da32-3819-ab6e-226c4c436fbb | -11.96704 | -51.47756 | 2025-10-04 05:33:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d7c6240-fe93-33fc-8305-fd2315eed934 | -9.9479 | -50.2403 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d3c7ad8-e553-39c9-aba5-d9b9b37872b4 | -12.99106 | -53.43391 | 2025-10-04 05:33:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff7d9340-d256-3e97-947f-8899e120e902 | -13.17033 | -50.88786 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e839609-cb82-3c7f-8923-93ae5ee7a5de | -11.81307 | -56.34969 | 2025-10-04 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 398ce206-dafc-3c84-8a97-b3786e471ed2 | -9.92605 | -50.90236 | 2025-10-04 05:33:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a774cfc8-8fb1-3596-b6a7-8ae200e40f4a | -8.62557 | -54.98643 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cecf2f7c-8346-3a3d-87f1-83c19dd9aed0 | -14.75414 | -54.63144 | 2025-10-04 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae1888f6-78b9-3cd9-810f-1fd1512a2102 | -10.05325 | -62.46194 | 2025-10-04 05:33:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef2a8a79-e8a6-3cbd-afd2-31d93e2f81ce | -15.59878 | -52.49411 | 2025-10-04 05:33:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65b9d41f-0e8e-31ac-8489-3218fed9008f | -9.21614 | -62.58453 | 2025-10-04 05:33:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63e2017a-2cdf-3d21-8f55-f0262e4fd54e | -12.30127 | -55.12737 | 2025-10-04 05:33:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 188276c3-508a-3609-9a93-a0d34d847501 | -10.04991 | -62.46141 | 2025-10-04 05:33:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d000eea3-2d4e-3ee5-88a1-8540d696518d | -9.32443 | -54.53309 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25b943f5-afa1-371d-bad1-1589740cf78d | -11.20743 | -54.08926 | 2025-10-04 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb280dd7-3437-30b9-9bb2-c4a1f51bc84a | -8.65121 | -64.13676 | 2025-10-04 05:33:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d64ecad-8639-3175-87a4-71c169898192 | -9.33662 | -54.51942 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20ae3cc3-a076-31a4-9742-50966eebcd85 | -15.58889 | -52.46745 | 2025-10-04 05:33:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8aa848d0-7a30-3254-90fd-3cc3a11d2659 | -11.74006 | -54.72182 | 2025-10-04 05:33:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6283d46b-e307-3fa9-bb08-0a07885a6c66 | -9.34207 | -54.51727 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f8f12ca6-c4cc-3343-a8b2-d0b737059f57 | -8.59286 | -63.25664 | 2025-10-04 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5348e052-4491-32bf-a738-dfdfa78861d9 | -8.70592 | -63.73173 | 2025-10-04 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6c75988-a53a-3d76-b43d-1608ec4c1623 | -15.61281 | -52.48156 | 2025-10-04 05:33:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34a66473-8d68-3c4c-8004-be4822085bd2 | -15.59819 | -52.49963 | 2025-10-04 05:33:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 158bd0bc-d130-3402-b144-06b98bb12ad0 | -10.83668 | -57.17683 | 2025-10-04 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bba78bf-d3b1-39ce-8715-7ca82e81c97a | -8.64016 | -54.59037 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79ac473d-ec10-39c9-bb29-9dc3fe7fe339 | -10.33183 | -50.33969 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d3e3f53b-e8b7-3738-aa1e-1770d33df19f | -14.57237 | -52.47753 | 2025-10-04 05:33:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c6b5e26-f676-3033-8f9c-d935efb22de9 | -7.87775 | -61.67962 | 2025-10-04 05:33:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 136e075e-cb4f-38f5-989f-b7663c9c5762 | -9.08591 | -63.69808 | 2025-10-04 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68316e71-aeb8-389f-b070-7ef237753d16 | -11.74523 | -54.72253 | 2025-10-04 05:33:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed7dd716-2500-3693-8e20-6cf6e43e626d | -11.01125 | -62.84934 | 2025-10-04 05:33:00 | NPP-375D | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82eba53e-a082-36f8-bcec-04f7a619a8b2 | -14.0439 | -53.92851 | 2025-10-04 05:33:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 514c7b11-8528-35b5-a17d-dc0e6fe5586c | -12.30052 | -55.13332 | 2025-10-04 05:33:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d9a7756-a3b6-364a-a571-7e563c3ad6a0 | -10.6439 | -49.14005 | 2025-10-04 05:33:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdc1138c-d105-3037-9fd7-344827a82e79 | -9.66537 | -62.39353 | 2025-10-04 05:33:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96cc99e4-0ee9-3599-b959-b1c5eec72698 | -14.75189 | -54.63983 | 2025-10-04 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 079a1b3a-5a95-3dcb-932b-b579045cb136 | -13.17237 | -50.93031 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a9051f28-f55b-347c-b10a-0b28cc82008b | -8.22156 | -55.20168 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50cf9445-a1b0-3315-bd4c-b8014f148cf0 | -9.45344 | -56.64809 | 2025-10-04 05:33:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33408131-936b-3b62-a672-c8cb71f71d67 | -12.91923 | -54.73114 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4120a8e7-9b44-3950-a3f8-da3dd041b847 | -9.32568 | -54.52399 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8566ca55-9b83-3ae6-97af-b3fd67a51691 | -11.73967 | -54.72489 | 2025-10-04 05:33:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a571bf9-a964-30c1-aaf0-2f84b9a3f2d8 | -9.90892 | -63.5914 | 2025-10-04 05:33:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b84fd9a-6250-3dde-8ea0-d020f8119ac7 | -15.60656 | -52.48062 | 2025-10-04 05:33:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f80596d-b010-3a15-9704-3edbcffb0b4d | -10.36427 | -57.82313 | 2025-10-04 05:33:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c6e6119-68c2-3d09-8959-7de85d927216 | -9.93273 | -50.19588 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 114d2a65-fe77-3a70-9239-7c0e1f6b4b94 | -14.74792 | -54.63793 | 2025-10-04 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1ddc417-036f-3678-aaa0-09e85a8e7835 | -9.93009 | -50.19549 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42b60f6b-57ca-307a-800a-05298bc8d4ee | -9.14157 | -62.37179 | 2025-10-04 05:33:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4bb29a7c-10c5-3a6a-a845-b4cab55c6402 | -9.5295 | -68.2957 | 2025-10-04 05:33:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdc772db-8bb2-3296-9f50-c04b58c41085 | -12.1939 | -61.82964 | 2025-10-04 05:33:00 | NPP-375D | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f659cdf-ff00-3dfa-90a4-e9512fbb624c | -8.62822 | -55.00276 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 661df467-c026-3be7-ab5d-fb6e530d3389 | -10.82526 | -57.19613 | 2025-10-04 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6797df3d-2d6f-31c2-827b-93987833c333 | -16.00913 | -50.93333 | 2025-10-04 05:33:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e77a032-ae5a-3531-bec9-ed35cfd52cad | -13.17559 | -50.93101 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 3b22db17-f3bc-30c4-8119-614b993b233a | -12.47293 | -54.42796 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cad7b01a-f949-38ea-b4bd-60f33efaa43d | -11.06331 | -54.81288 | 2025-10-04 05:33:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f1f0492a-af7c-32ae-8576-594e977c586f | -11.05821 | -54.81224 | 2025-10-04 05:33:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 107010af-d3ff-3632-ba48-e20514de64d6 | -11.90949 | -55.90955 | 2025-10-04 05:33:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c29ed0e-566e-3b87-b781-eedf83de7020 | -9.3358 | -54.52539 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a50f1686-c50d-3bab-931a-e35e6dbc3ca0 | -9.77 | -62.33045 | 2025-10-04 05:33:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72e29e2f-6cbc-316b-a935-30f0f8bcdef0 | -9.92699 | -50.89652 | 2025-10-04 05:33:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03115e90-c4f5-3d44-bd0e-199bb17342c2 | -7.87051 | -61.68209 | 2025-10-04 05:33:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab0423d9-dde9-3b25-8713-5dc67a4bf12a | -12.28425 | -55.13983 | 2025-10-04 05:33:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55b1e1fa-2f75-3deb-a8ff-bbf73c129460 | -8.62482 | -54.99172 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f65eeded-2e6e-3d51-8529-262ee36904fc | -9.71027 | -67.46433 | 2025-10-04 05:33:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55315aac-8886-331a-b7ed-439e33367e3f | -9.33236 | -54.51282 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d01115cf-ec62-361c-84d9-da7fb964d170 | -12.91882 | -54.73442 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a120e6e7-3643-361f-ac35-9c2fb9121383 | -10.29736 | -50.28712 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ed32e08-1461-30e7-a1e0-cdee1e92a557 | -12.38515 | -54.45749 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README131.md)
