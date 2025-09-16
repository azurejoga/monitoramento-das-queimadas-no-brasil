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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a3873d5-0a02-30a4-acf5-9c84b2fb24aa | -11.0759 | -49.7573 | 2025-09-16 04:51:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3583fd27-4e76-39e1-8fb4-9e4f4106f735 | -15.61703 | -47.37077 | 2025-09-16 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cc81a372-6700-38a2-9880-941fc32ac6d4 | -11.24144 | -49.94874 | 2025-09-16 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e204767f-262b-3059-af26-fc8a196a4e33 | -13.20462 | -47.31054 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ab7760e5-860e-3ec0-930c-1d5f855d0e59 | -8.63425 | -45.68606 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a3123968-82e0-3d0a-bec1-4b1928deeba5 | -10.70792 | -44.74201 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee0a9f93-df17-38a4-94ec-b74d1d8edbfc | -12.86144 | -47.14756 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 911a1121-9444-3e25-b03f-25ba13bd2240 | -10.7131 | -44.74284 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b465a4c7-b166-340d-941c-3f86173196ff | -8.42559 | -47.21112 | 2025-09-16 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfdc3fd6-dd97-3b14-81f7-5af506a41546 | -14.8291 | -51.66786 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3816abe8-afb9-3bd7-8baa-4d1f2ab470b8 | -8.61396 | -46.3962 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f53bd964-e4af-35a7-98f5-969f4f4deafe | -14.82968 | -51.66373 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 40f29bf4-44a7-3452-9488-e12337322a6e | -14.92515 | -51.65718 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84c0365e-f6b5-3297-8a19-c5d420098915 | -11.12252 | -45.33964 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec42a183-0ec7-31fa-80a5-796d0b092536 | -14.85279 | -51.67993 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4552c240-b223-38ec-8c65-06f1c23130dd | -9.48724 | -55.96541 | 2025-09-16 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b850622-f248-3f38-ae74-da9e74c161bd | -8.96363 | -44.19693 | 2025-09-16 04:51:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 295546f1-eb35-3580-8363-244d637ad517 | -14.56238 | -54.50671 | 2025-09-16 04:51:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 19287020-0761-32fa-91b8-77a29ddbf5c0 | -12.54045 | -45.88153 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 2e516ccf-629b-39de-8a60-29d3c09fddd5 | -9.15556 | -46.98043 | 2025-09-16 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7dad304c-9a09-377c-ba47-6c7e4c5800bb | -10.47307 | -45.16108 | 2025-09-16 04:51:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f6a6135-a42c-3248-a1f1-5649fb3912ed | -11.12755 | -45.34031 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c8681e19-055e-3e6e-b838-e7177cc2361c | -10.72298 | -44.75668 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 813bec1b-2c03-30af-9d8c-de0130e697eb | -10.71935 | -46.51338 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 41c8745e-a185-3ae7-b2f3-8f882e24a082 | -10.71412 | -46.51741 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| bd27a7f0-f786-36e9-9ab8-c25ac5e01cf3 | -12.61678 | -47.95922 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bbbe3c6-b506-3146-b7ed-01e7a8432756 | -11.63446 | -46.58662 | 2025-09-16 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b04b0abc-40c6-31dd-a229-0cf4240f3e24 | -12.63146 | -45.76577 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 546364d2-e636-3986-aef2-c7b57815d5d4 | -9.09496 | -44.86518 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 093e407d-4dcd-3678-bb0f-3ac3e5968364 | -10.73843 | -44.76008 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8be415c-824f-3dc1-9a8d-a132fbc7a9d9 | -12.66793 | -47.71378 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 15f56794-d38d-3155-b242-9f81fbdcf10a | -10.40762 | -50.63997 | 2025-09-16 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f7b25391-c2c6-38d1-abd2-a8fe935ba102 | -12.75659 | -47.96523 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 98306dac-224c-3a10-8018-0e666b46c9d0 | -10.20926 | -54.30384 | 2025-09-16 04:51:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd2de02e-495c-382e-9b8d-373ecca5dd0a | -10.95621 | -49.57177 | 2025-09-16 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef8f9ba7-7c97-3fbe-ba98-acf92872a35c | -9.74656 | -55.37874 | 2025-09-16 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5dd99a5a-4540-3f9a-9b46-02d1884de511 | -11.02505 | -45.06546 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fab258fd-1b97-387f-b88b-886321d28a20 | -15.08134 | -52.48813 | 2025-09-16 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 626f8410-9b9b-32fa-8415-efcd07402201 | -12.73839 | -47.20426 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 918b7c64-f9b0-366c-98f3-f5fd785e7532 | -9.70451 | -47.40596 | 2025-09-16 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87b2d57d-9463-34f9-8af9-f41a90c9e066 | -12.69022 | -47.98608 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bbb78795-0443-3049-a048-36466caae556 | -8.58806 | -46.35058 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0ae777d1-0046-3565-8ce2-5f8afb479d41 | -14.84272 | -51.67417 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 24c02a34-c046-3046-b494-4ff28f486827 | -8.39634 | -47.26366 | 2025-09-16 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ee070d5-8aae-31ad-b235-4028b6cd0069 | -12.81163 | -47.24361 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c69d1c94-84b7-3781-9304-70bcbaa0a237 | -12.61791 | -45.75217 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48893e4e-9d77-3a74-a34c-ecbd1501ab18 | -10.74577 | -48.18397 | 2025-09-16 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bcd8cf1-d2b7-3a3d-9629-e6dc0d42e69b | -9.62707 | -62.40661 | 2025-09-16 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc7e29e8-53f5-31a3-9cde-700f8068ee73 | -8.43456 | -55.61992 | 2025-09-16 04:51:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e39ee70-0658-3cc8-874e-17589c13cc7a | -8.4423 | -55.61651 | 2025-09-16 04:51:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5baeb11b-598b-340c-b470-9122a44dddaf | -8.96938 | -44.19414 | 2025-09-16 04:51:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aea055a0-f0f3-395a-ab69-e6a956e282fa | -10.70938 | -44.73854 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e301b171-d889-3a82-804f-1eae7bb450cb | -9.05281 | -44.84234 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c999074-c8d0-3f1b-988b-7097513ac6bb | -8.67501 | -49.93545 | 2025-09-16 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 27cacc9c-625a-34d7-bfb9-d8a60599dd95 | -8.08926 | -50.15276 | 2025-09-16 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3ef47e66-e5e7-3e1b-bac8-3d58706c08e3 | -12.77886 | -47.92928 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d015565d-4b03-3d67-adeb-61b9c2ea0ecd | -8.96869 | -44.19436 | 2025-09-16 04:51:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e561a711-dd61-3212-94ce-1f3f9af7471a | -9.09609 | -44.85659 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d88ed1de-31a9-3740-b174-d1d887de2ce8 | -10.11521 | -45.66575 | 2025-09-16 04:51:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2a11a3b-ff88-3ce1-ab79-e2756bc9e82e | -12.76411 | -47.97475 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0222bd8-b660-342d-9145-6974bc58ecec | -13.78156 | -54.95343 | 2025-09-16 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f25c495-7e8a-3929-b1ed-072b69dda76b | -12.80647 | -47.24778 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| edae1571-fce6-3abb-8c15-6274911e302c | -9.09326 | -44.8389 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed5a17ad-37a1-3c5f-b7c0-051a53639f9d | -8.97571 | -45.75682 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36ee3be4-1dd1-38fa-85a2-c6ee9af968f8 | -14.83562 | -51.67308 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b149fd72-a867-3a63-b732-d154b2c17703 | -11.11136 | -45.34674 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8a4e88d3-d9cc-3c9a-808a-fcd93c545d80 | -11.11514 | -45.31764 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1313f30-8cdb-339b-a32e-a4aec7ccb434 | -10.71623 | -44.7682 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53237e05-8c54-3c31-a821-20e1398de7df | -15.08939 | -52.48136 | 2025-09-16 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9dd31819-0038-38ce-92b0-fdd4cecf7968 | -12.11729 | -44.82802 | 2025-09-16 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 809075ed-74a8-3434-8f48-5665e96310b5 | -8.97397 | -46.22781 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4263f7c0-ebec-311a-a0e7-a890a9005038 | -12.78357 | -47.96019 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3f3cf09-3d8c-3285-bb16-31e94ca3d11b | -11.13449 | -45.32643 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c6c2e81-b547-33b7-8571-85c28f238d97 | -9.53424 | -62.3834 | 2025-09-16 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eea27971-7d89-3016-8655-413e34bda219 | -9.05628 | -44.85461 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c88222f-0714-3b7f-88e9-ab60b1ffd8ff | -12.10144 | -44.82605 | 2025-09-16 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62fc4386-ed6d-39c5-b750-e5284ce4a9e0 | -14.30368 | -49.53355 | 2025-09-16 04:51:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9789a26-16d1-39e9-b8f7-46b485cf4549 | -8.39748 | -47.25573 | 2025-09-16 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27b47d04-b375-3c45-9083-8ff68a74bcdf | -10.7245 | -44.7447 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86c53752-9038-3d0f-b25f-231e653966c6 | -13.00392 | -47.95321 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25dbb0ba-8c2b-325f-be84-a714dfc2c532 | -11.12177 | -45.34538 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6298f5a2-5331-3d59-8717-44312d37298d | -10.7178 | -44.75575 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1af5597b-d16d-3640-bf4b-152fef1b2ea6 | -11.43008 | -46.92493 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81bf3fea-3fa7-3f05-97c1-9c12ddaa391f | -9.13778 | -46.94775 | 2025-09-16 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ee0c650b-2961-3eb8-880e-1123123c4f58 | -10.7285 | -44.7549 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 478e8fc1-afe6-31c9-b725-88377affa177 | -8.99844 | -47.0391 | 2025-09-16 04:51:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75536dc1-9231-3010-a71a-2d1c7326a28b | -8.97976 | -46.25315 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ce730637-81cb-33bc-8f6e-e261ed21e8e6 | -13.5077 | -50.80971 | 2025-09-16 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da7de1ee-1e86-3619-b085-f3257fe821d8 | -12.81339 | -47.23026 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9483967c-751c-34fa-be9c-26955f3e9a00 | -12.44188 | -49.70563 | 2025-09-16 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33cdfdf7-5a66-3510-bb2d-47d5ac545e31 | -12.66356 | -47.71317 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5f87e654-8bd3-3297-8723-12f63e7d7a9e | -12.95214 | -47.96467 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bad462f8-fdf4-30d0-a532-ddb96f30802c | -10.71498 | -44.76844 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2ad99f1-b5d0-3eb6-a70e-95289248af5a | -12.79736 | -47.24706 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 29343f2b-a3b2-3310-9b2c-d9242a261884 | -11.1121 | -45.34104 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5b62bba-6807-3fce-a19c-4e626155e8e5 | -10.72373 | -44.75077 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 54319d38-c2b2-38c5-b342-ae2a5a5220ed | -12.62712 | -45.7583 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1784a1fd-52fa-339a-bc35-4aff65ba5cac | -10.47694 | -45.17079 | 2025-09-16 04:51:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34ef6238-c348-3dcb-8e71-b927bb152cce | -12.80792 | -47.94222 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6926cef4-b003-3f1c-a9cb-f9262cc5f2e1 | -12.60875 | -47.95382 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README77.md)
