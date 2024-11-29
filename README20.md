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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3a87563-deb8-3d01-bf33-812a00919ae3 | -5.71626 | -43.84062 | 2024-11-29 03:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7adcc27-4256-37ee-81e1-09aafdef5849 | -6.85787 | -39.43043 | 2024-11-29 03:42:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2c22202d-81bb-3204-b9b7-bb1c7f04247b | -6.67867 | -34.97501 | 2024-11-29 03:42:00 | NPP-375D | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 79ccf3a3-fb2e-3514-9085-f4e87c435d0c | -6.11474 | -44.91917 | 2024-11-29 03:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db72211a-5ef7-30b1-8282-d63acd809700 | -4.40479 | -47.2668 | 2024-11-29 03:42:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 64ca3968-4802-3b0a-8d71-1ed92c264915 | -4.91955 | -44.52858 | 2024-11-29 03:42:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a800b06-cf89-3a10-ab19-5aa2f786d960 | -6.1183 | -44.91909 | 2024-11-29 03:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f51f52af-e62b-3ef8-9b68-e16144647511 | -5.03973 | -43.62147 | 2024-11-29 03:42:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4428aada-7226-3f3c-9f8c-1877d2f3870d | -5.74844 | -43.39846 | 2024-11-29 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 26f9b5ec-3f85-3adb-9021-17a51fba6bcc | -10.66345 | -36.81678 | 2024-11-29 03:42:00 | NPP-375D | PIRAMBU | SERGIPE | Brasil | 2805307 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| db7a8864-a18b-3e15-9e49-f09d400cf467 | -5.8289 | -39.20667 | 2024-11-29 03:42:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 56a281c8-d9cd-34b0-b0ba-4255440ad5ac | -5.04028 | -43.61826 | 2024-11-29 03:42:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6d0d9e22-928a-344b-92b2-6ceb665ae180 | -5.40554 | -41.5592 | 2024-11-29 03:42:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a1a0f4c6-f476-34ae-a951-5e0849389c83 | -9.44402 | -35.9133 | 2024-11-29 03:42:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f68cf31a-ae7e-3919-b96e-f57728030897 | -5.87753 | -47.31926 | 2024-11-29 03:42:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c64130f0-aace-3189-bb06-b5cf4c127415 | -12.05241 | -39.06927 | 2024-11-29 03:42:00 | NPP-375D | TANQUINHO | BAHIA | Brasil | 2931103 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f7a2624a-f2ff-322c-9976-e70ff7d74d03 | -10.20283 | -42.48111 | 2024-11-29 03:42:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 056eda37-dfba-38a8-b65d-c2d373d270e6 | -5.50929 | -46.25711 | 2024-11-29 03:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed24fa62-d189-3f3e-80f1-eb64a57b9f8f | -4.88244 | -44.64567 | 2024-11-29 03:42:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5abce18-74da-36aa-97c7-1e90203b4a87 | -6.03099 | -38.1239 | 2024-11-29 03:42:00 | NPP-375D | FRANCISCO DANTAS | RIO GRANDE DO NORTE | Brasil | 2403905 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bed3d37c-e74f-3a6d-b36a-63eba9e060d1 | -5.04606 | -43.61589 | 2024-11-29 03:42:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20aa0cd6-9c61-3b95-9f22-e6cab6eaac53 | -6.9064 | -39.42342 | 2024-11-29 03:42:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 211a7b8e-1c60-331c-8a04-861f873890ad | -6.12038 | -44.91995 | 2024-11-29 03:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19121727-4c52-3930-9f71-14b624870b4d | -5.55858 | -44.38408 | 2024-11-29 03:42:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5775cd95-bdb8-30ff-99fe-b43b775f2e26 | -5.22216 | -44.92292 | 2024-11-29 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ef02e6ee-4c3e-32f2-a0f5-438b3564c90f | -5.85424 | -40.8031 | 2024-11-29 03:42:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c31c9b29-9315-315f-879e-b2c27f0d34c1 | -4.87677 | -44.64506 | 2024-11-29 03:42:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbd150f1-da85-3d17-a65b-9b9cb31f144c | -10.78563 | -37.20298 | 2024-11-29 03:42:00 | NPP-375D | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 209ef817-fcc7-3f4b-864e-f85f51e917b9 | -10.41831 | -40.46813 | 2024-11-29 03:42:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d2d67cc4-2950-32ea-be93-d900b66d1b2f | -7.71906 | -35.15666 | 2024-11-29 03:42:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 535862ee-e24c-3d15-8412-6598478276e3 | -6.0697 | -44.1503 | 2024-11-29 03:42:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f4cd66e-078a-393a-be1e-4937067c1b1b | -5.75354 | -43.39934 | 2024-11-29 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8a3c21f-348f-3fa0-ad0b-fad1d34158ef | -5.48274 | -42.07314 | 2024-11-29 03:42:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 94179226-e112-3811-83a5-223740bf6fd4 | -8.12941 | -47.99596 | 2024-11-29 03:42:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0ed46178-0321-3906-bfa3-80d01fc7b010 | -6.67921 | -34.97153 | 2024-11-29 03:42:00 | NPP-375D | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d3788828-2831-381f-b19e-549c2f555c4f | -7.21892 | -39.05363 | 2024-11-29 03:42:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4911c2cc-3322-3524-a132-f292a2b9adf3 | -8.37252 | -44.47544 | 2024-11-29 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54d92b57-e420-3522-9de9-a863e03aecef | -5.55313 | -44.38306 | 2024-11-29 03:42:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0674249e-d4e8-3c5d-b723-8588b16241cf | -6.48927 | -44.68219 | 2024-11-29 03:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ac9ea59-1841-34af-a882-bd804ae66e71 | -6.16185 | -44.42313 | 2024-11-29 03:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a08415a8-6d58-3218-a851-c15f6fe8b103 | -6.86573 | -38.56595 | 2024-11-29 03:42:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3c428df4-3e97-3d22-a5e3-80b05dc0cde0 | -10.19167 | -36.33883 | 2024-11-29 03:42:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d5d71d24-d316-39ab-8b7f-de6a9371d38e | -6.48917 | -44.68119 | 2024-11-29 03:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75e03b55-fc79-390a-9f0e-dc4e9bfa9c92 | -6.4885 | -44.68487 | 2024-11-29 03:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49955b26-248d-34c1-ac6c-7ab2b89ca66a | -7.91296 | -38.42013 | 2024-11-29 03:42:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 023f3541-8a37-3ea0-aa8a-f3ffa4bb40f4 | -5.22927 | -44.91578 | 2024-11-29 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| adf8fb1e-69a8-3aab-aab5-a1148c897468 | -7.07557 | -40.22593 | 2024-11-29 03:42:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5d4452eb-4255-3a47-8231-381b2721b0c3 | -5.76176 | -43.39865 | 2024-11-29 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c548eeb1-35e8-3116-9239-1aa1ae3ba8f1 | -9.44457 | -35.90981 | 2024-11-29 03:42:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 56cf03bc-fe02-373c-a39d-d0fa1d5f10a0 | -5.28257 | -45.12384 | 2024-11-29 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7054863-a21a-3be0-a07e-623d7096ac39 | -8.88339 | -36.60807 | 2024-11-29 03:42:00 | NPP-375D | CAETÉS | PERNAMBUCO | Brasil | 2603207 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5bb30461-c7d2-3e22-9d63-8b0c1907ea0f | -5.75914 | -43.39719 | 2024-11-29 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fa2d728-39dd-378d-af41-0dc6403c5ba3 | -6.11761 | -44.92286 | 2024-11-29 03:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c895f21-2fda-3543-9ebb-5c47f007f452 | -9.3119 | -46.22102 | 2024-11-29 03:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce9d5db0-8c36-3314-aa2d-aec49776be7c | -8.13161 | -47.98468 | 2024-11-29 03:42:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 769411ec-ab0e-3539-b116-733752b17672 | -5.04552 | -43.61907 | 2024-11-29 03:42:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 74409aae-2974-3bc2-802e-7ba9a0ad4e30 | -5.21858 | -44.90988 | 2024-11-29 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccc9f43b-5b08-3340-8bd7-388778c6e428 | -8.12538 | -47.99095 | 2024-11-29 03:42:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 54438019-1509-3ded-bda6-e05289b6482f | -4.68915 | -46.66914 | 2024-11-29 03:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 949cf255-95db-3fe7-bee6-926ed3963914 | -5.935 | -43.78761 | 2024-11-29 03:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 312e0e59-240b-31bc-9353-f21c2bab0f19 | -4.78623 | -46.11995 | 2024-11-29 03:42:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4f8ecb49-3717-3bc9-88e7-6971af6fcc7a | -9.08293 | -49.58136 | 2024-11-29 03:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 61dd2504-fd01-34a4-9417-c629f3457f74 | -5.16737 | -46.16346 | 2024-11-29 03:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 188d2fe1-0562-3ccd-93a5-019e03afdf00 | -5.22356 | -44.91489 | 2024-11-29 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3182a696-ceb6-3ab1-8999-c82993e27465 | -5.54902 | -41.41312 | 2024-11-29 03:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f71efbe8-5880-31cf-b37b-d1727aab1db7 | -6.46007 | -39.29192 | 2024-11-29 03:42:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e71de8bc-93ed-3a7c-b856-f17dc35bc88b | -5.75864 | -43.40018 | 2024-11-29 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c940d07e-5cb9-3df2-9e4b-eba3d254237d | -9.44789 | -35.91034 | 2024-11-29 03:42:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 2b08696c-eb9e-3e41-876a-d721b1531e2e | -5.72151 | -43.84154 | 2024-11-29 03:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b7cf3c11-3fcb-3875-8439-e8b1a9fbd04f | -5.48357 | -42.06826 | 2024-11-29 03:42:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5deda8e1-8f81-3075-9b59-64c7ff5b9108 | -7.98067 | -38.27654 | 2024-11-29 03:42:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3e8fd7b6-0c8e-3f38-8d62-ac8021ffea5e | -5.50401 | -46.25113 | 2024-11-29 03:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1653784-5098-37d9-92ad-76767ff6f25d | -5.40179 | -41.55383 | 2024-11-29 03:42:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 565f3fc8-2867-3cf7-a60f-08f45e2cb4af | -5.75613 | -43.4008 | 2024-11-29 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4325048a-3d58-353f-9780-ad44280724eb | -8.12644 | -47.98531 | 2024-11-29 03:42:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c37a3abf-9419-321f-b97a-481239bda45c | -8.13194 | -47.99218 | 2024-11-29 03:42:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ad13abbc-6045-3c84-9fff-0a9aa0be4128 | -5.76791 | -43.39354 | 2024-11-29 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da9c1380-2bee-3641-af61-2abc0767c02f | -5.37211 | -44.84575 | 2024-11-29 03:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d16d23c6-aef8-3318-93b2-ee8f24ed384c | -7.4451 | -39.8443 | 2024-11-29 03:42:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 10.7 |
| be1b2129-3bc2-3c9b-b206-8714aa9a3370 | -5.97814 | -45.36034 | 2024-11-29 03:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0de6fec2-2c59-306e-9eaa-71f9be40a509 | -5.04082 | -43.61504 | 2024-11-29 03:42:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33e4ed60-d032-334b-a0d8-6420c31dbc34 | -6.48863 | -44.68587 | 2024-11-29 03:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6f3cf24-fbe9-3c2c-8c1c-bebbde9e55e6 | -5.31498 | -43.08268 | 2024-11-29 03:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4b1b846-a8c2-3d12-b51c-1f5bf93ea486 | -5.75103 | -43.39996 | 2024-11-29 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0880d3da-a695-3104-904e-be5c4368ad34 | -4.92931 | -44.52946 | 2024-11-29 03:42:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4f9cb15-5a08-3546-a748-a053ab06a1ae | -6.35732 | -39.7805 | 2024-11-29 03:42:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a441a4bd-f5dd-3dde-b4d4-7a5dc312b086 | -7.00111 | -39.31528 | 2024-11-29 03:42:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1290aff4-0ae4-3415-97ad-1130fcb9d5bf | -6.91821 | -37.8406 | 2024-11-29 03:42:00 | NPP-375D | CAJAZEIRINHAS | PARAÍBA | Brasil | 2503753 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8a49d013-7702-30c2-9d3f-6e69a2c2aacf | -4.92515 | -44.52937 | 2024-11-29 03:42:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4078d705-a776-3bd4-949c-8633167794f0 | -5.89805 | -43.41269 | 2024-11-29 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7912c922-f419-3aa9-a0e8-26d086f11bd6 | -8.28236 | -48.03755 | 2024-11-29 03:42:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ad512dfe-e11c-35d1-a9c1-8cace766d4ac | -4.33676 | -47.57494 | 2024-11-29 03:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bd1ebb55-c4d5-3c34-9c44-8f439f121d14 | -5.75303 | -43.40234 | 2024-11-29 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 670c9bf7-028d-3e29-b1aa-7ed6595cbc42 | -5.86722 | -42.75328 | 2024-11-29 03:42:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5debbcbe-1d53-3dd3-ae36-3d84b58eddb4 | -4.92993 | -44.52594 | 2024-11-29 03:42:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9184194-8c3a-3b58-b73b-b1458badacff | -5.75719 | -43.39482 | 2024-11-29 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94363631-368d-31e0-a765-138315c2891e | -4.92371 | -44.52869 | 2024-11-29 03:42:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b6c3df6-80a6-3218-adbb-87c9f039d84b | -5.27681 | -45.12282 | 2024-11-29 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a05555e0-56f6-34e7-8655-0f0e603e1618 | -7.33071 | -39.10039 | 2024-11-29 03:42:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 50d1e2c0-2291-3660-bd51-3a734272d7da | -7.71764 | -37.01237 | 2024-11-29 03:42:00 | NPP-375D | SUMÉ | PARAÍBA | Brasil | 2516300 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README21.md)
