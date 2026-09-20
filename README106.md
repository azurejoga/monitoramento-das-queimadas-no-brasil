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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5da8b2c-9667-3f8e-9923-556c1401ed6c | -9.96748 | -46.55733 | 2026-09-20 06:25:00 | AQUA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0dcde829-92bd-3b6c-a711-806ae146beb6 | -6.56159 | -42.55145 | 2026-09-20 06:25:00 | AQUA_M-M | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 831fd700-c7a2-38b6-bb6f-ff43322d01de | -11.45077 | -45.37634 | 2026-09-20 06:25:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 74830f5b-f9b8-3398-83c3-f341f65a98bb | -13.02397 | -46.90125 | 2026-09-20 06:25:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 431affe6-7d86-3289-a2e8-32d5028205bb | -12.75688 | -46.2126 | 2026-09-20 06:25:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c87c8ac8-b028-353e-945f-e7139ad16f0b | -12.13251 | -47.05258 | 2026-09-20 06:25:00 | AQUA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 13c24ddb-3bf5-35b2-8490-bfba1e4f7cb7 | -2.45494 | -49.21291 | 2026-09-20 06:25:00 | AQUA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 8fee78a3-e5b8-3ddb-afa7-15c4715476a8 | -9.12605 | -45.7137 | 2026-09-20 06:25:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7dd5e88c-047e-3e1b-a80f-0b085a9855dc | -10.40824 | -48.92812 | 2026-09-20 06:25:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 86bd3bea-02a4-382f-911e-d5c8d085485a | -9.82928 | -46.4348 | 2026-09-20 06:25:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| bc3340e7-2252-31fe-a04e-b36d5ceede06 | -11.49874 | -47.78731 | 2026-09-20 06:25:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9020cdff-0a01-3b6d-8058-370e5f0922ba | -6.35358 | -43.36115 | 2026-09-20 06:25:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8c6924b4-81b0-35a4-bef0-070b8c76b79e | -8.04243 | -46.24998 | 2026-09-20 06:25:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| d6512a19-6335-315f-86be-d82789a971f5 | -10.16844 | -45.5581 | 2026-09-20 06:25:00 | AQUA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d6968eb4-909f-3d1a-bb7d-3c1ef8b6b3ef | -12.27906 | -47.12503 | 2026-09-20 06:25:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e829a0a4-1b43-3231-8937-d799b014d22f | -7.43882 | -44.75986 | 2026-09-20 06:25:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f21f825b-6af9-3383-9ec5-9124e5084dd5 | -11.85608 | -47.65693 | 2026-09-20 06:25:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7c4fd05f-68a6-3eef-a98e-51cf26ca4577 | -11.86721 | -47.65873 | 2026-09-20 06:25:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| da31ad25-1043-3108-a0c8-1b0c55565028 | -9.12217 | -45.73761 | 2026-09-20 06:25:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 954fccd3-7833-3930-8115-09ca84215ad9 | -7.5476 | -45.43485 | 2026-09-20 06:25:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 1d847104-0c92-3dc1-b8df-ed4011f49b6e | -11.08803 | -48.29567 | 2026-09-20 06:25:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| ead46118-c727-3dd9-926b-4733ab57094f | -6.31477 | -47.63624 | 2026-09-20 06:25:00 | AQUA_M-M | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 3cf90794-51bd-3cc3-b3b3-a6247e70bf05 | -7.53937 | -45.42117 | 2026-09-20 06:25:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 4cb21bc7-cf32-39cd-9d2a-0a76b46c60fb | -8.7551 | -48.64981 | 2026-09-20 06:25:00 | AQUA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 40.9 |
| d73c06ab-21f0-330b-963b-47c05d1c4721 | -9.81695 | -46.37949 | 2026-09-20 06:25:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b6199b08-44e6-3843-a6ac-be0342974e06 | -9.12409 | -45.72577 | 2026-09-20 06:25:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 88eac6da-8522-3a14-8425-681689debe4a | -7.75547 | -49.19436 | 2026-09-20 06:25:00 | AQUA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 26.8 |
| de7d2d72-49da-31f8-955d-f22491d84532 | -10.26285 | -50.26911 | 2026-09-20 06:25:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| fc4cdac8-8680-30d6-8464-4632b4a6deb2 | -7.44055 | -44.74893 | 2026-09-20 06:25:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d75db737-6327-378b-a257-f25cad11d498 | -9.76258 | -46.03496 | 2026-09-20 06:25:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5f2863aa-32b0-38cc-a6d9-865c09ac7452 | -12.28471 | -47.11896 | 2026-09-20 06:25:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 02637d7f-1662-36f6-83b3-478d05ae5d90 | -9.6933 | -48.31614 | 2026-09-20 06:25:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| bbb9d13c-9266-3d04-addd-40e04259f21f | -7.43082 | -44.74754 | 2026-09-20 06:25:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| b0c60e01-fe10-3748-9eb5-095f68c70d85 | -10.26739 | -50.24394 | 2026-09-20 06:25:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 5ec943bb-679e-3809-aeae-ae0f86189607 | -7.85711 | -44.84618 | 2026-09-20 06:25:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 90ce8f8f-8a5e-3b03-b0aa-d2c1aa1a773d | -8.76445 | -48.67245 | 2026-09-20 06:25:00 | AQUA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 32365252-7325-35f6-a3f0-77629c413815 | -6.25914 | -42.7172 | 2026-09-20 06:25:00 | AQUA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 7acc6443-af0b-339b-90aa-63b506fad1d6 | -7.16549 | -47.44698 | 2026-09-20 06:25:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2c75c8fb-f085-300f-a064-90ce60720888 | -7.75723 | -44.8345 | 2026-09-20 06:25:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fb41a07c-c8c1-3ae8-887e-9d714d3e392d | -9.78819 | -45.05106 | 2026-09-20 06:25:00 | AQUA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 581de11f-99e2-34c0-b158-701b7d1eb106 | -8.75173 | -48.66981 | 2026-09-20 06:25:00 | AQUA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 21.5 |
| dd7cc499-736a-3637-a351-ca44d106d132 | -2.45537 | -49.20824 | 2026-09-20 06:25:00 | AQUA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 13a6259d-d58c-3685-a2bc-c5b831f3cd71 | -6.31784 | -47.61759 | 2026-09-20 06:25:00 | AQUA_M-M | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| ea9980e8-d903-36fb-9823-88f793146394 | -12.15807 | -47.02956 | 2026-09-20 06:25:00 | AQUA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 1b8dd252-829e-3dd1-a4c2-22b7a34c7568 | -7.54571 | -45.44683 | 2026-09-20 06:25:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 09c1ed63-42f4-3a86-9909-a8d328b9d349 | -8.76799 | -48.65127 | 2026-09-20 06:25:00 | AQUA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 231e14c9-a552-3a2a-ab95-d72b6b117540 | -12.13475 | -47.03928 | 2026-09-20 06:25:00 | AQUA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| bcf3ef3c-358d-3770-a7f4-0517450be35b | -12.76197 | -46.12013 | 2026-09-20 06:25:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4980ae67-a5ab-3c12-9877-e6d61677cc64 | -6.41039 | -42.81758 | 2026-09-20 06:25:00 | AQUA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b8bfeda7-c6a0-3c99-b3e4-5dfde9dd9337 | -11.66328 | -43.41481 | 2026-09-20 06:25:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 87115645-698d-3e3b-a3ea-df4773c8f7fa | -10.10099 | -45.65851 | 2026-09-20 06:25:00 | AQUA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 040085b3-9caa-36b1-8715-0fcf28d5391d | -10.40945 | -48.93347 | 2026-09-20 06:25:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 73c82683-df94-3cfb-876f-df1d07eb339a | -5.21775 | -47.57663 | 2026-09-20 06:25:00 | AQUA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 13fd47f1-7ca6-3d91-9113-7140f7928150 | -6.41181 | -42.80844 | 2026-09-20 06:25:00 | AQUA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| be996fa9-7141-3f2f-b374-424045031785 | -7.52538 | -45.44372 | 2026-09-20 06:25:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 4d84db35-66b0-36aa-b7ca-1a43ddb94157 | -7.16196 | -47.42314 | 2026-09-20 06:25:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 13abfba4-b508-32b9-8ad4-b6e556fd2f73 | -6.56021 | -42.56041 | 2026-09-20 06:25:00 | AQUA_M-M | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 99d24e42-0f2b-3c8b-ad48-ed098ca52664 | -12.75264 | -46.17688 | 2026-09-20 06:25:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 36c46780-c755-39e1-b52c-3775be808a25 | -7.76694 | -44.83605 | 2026-09-20 06:25:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f1fe9788-909c-3024-bd58-ac80d7e7fb3f | -9.83776 | -46.44878 | 2026-09-20 06:25:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ecd1668f-f3f0-3d05-b15b-a59b25d28464 | -11.65447 | -43.41344 | 2026-09-20 06:25:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d3c5c695-2e92-3c8d-be74-845ca0d2394c | -7.5495 | -45.4228 | 2026-09-20 06:25:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 70890246-7229-3490-aaf1-a6af91bf0964 | -11.6619 | -43.4238 | 2026-09-20 06:25:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 205f0601-51f4-3027-9d11-b90800f169e3 | -10.29043 | -50.19644 | 2026-09-20 06:25:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| c5655651-5495-3fc7-b571-09ca8f12a75b | -9.04758 | -48.719 | 2026-09-20 06:25:00 | AQUA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 1d988641-ab8e-35a7-b175-458db8d43a2a | -9.39422 | -40.29959 | 2026-09-20 06:25:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 50.4 |
| 8a1088c0-18dd-35e8-9b15-fb56d1149161 | -11.4762 | -47.78296 | 2026-09-20 06:25:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fc89ae16-0ba3-3b5d-9549-4583029b3001 | -11.85353 | -47.67192 | 2026-09-20 06:25:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 2ec30e0d-46a5-3ddf-b834-1a28c43cbe62 | -11.86467 | -47.67374 | 2026-09-20 06:25:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 60cb7d6b-0247-3756-87c1-f7f914a77989 | -10.92063 | -47.85678 | 2026-09-20 06:25:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3d6c94ce-ce67-3cce-abe1-5dc1b73d0e0b | -10.27469 | -50.26368 | 2026-09-20 06:25:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| aeef556c-ac21-3af0-8e00-2627b8a009dc | -7.42909 | -44.75841 | 2026-09-20 06:25:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ba69e199-1759-38cb-9d20-66700ef41d94 | -7.53745 | -45.43325 | 2026-09-20 06:25:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| bf8a2773-200c-3b8b-83f1-03025f93f583 | -7.5273 | -45.43168 | 2026-09-20 06:25:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 368c6a16-c114-337f-b6c9-d95d9adfdabf | -13.03215 | -46.91571 | 2026-09-20 06:25:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| f357551c-21f3-3e0b-a168-1c1108c990be | -10.78091 | -46.34061 | 2026-09-20 06:25:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 07d7bbd6-ebe2-3289-9d18-a07b9c854230 | -12.76011 | -46.13146 | 2026-09-20 06:25:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| d9786696-3fa0-3ed6-8019-4edebb5b4158 | -10.78379 | -50.86425 | 2026-09-20 06:25:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 9162c4d5-a88d-34c5-b204-4124b5a52ab6 | -9.83994 | -46.43555 | 2026-09-20 06:25:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| dfb8f6ec-3ef2-31d0-8091-ad0544bad998 | -10.78294 | -46.32832 | 2026-09-20 06:25:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f6a6d751-f51d-3f72-9653-468d6b78f946 | -16.72301 | -49.23145 | 2026-09-20 06:27:00 | AQUA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 43.0 |
| f5c9cc26-7b8a-3b38-85a4-ea832d79da95 | -18.68592 | -47.05662 | 2026-09-20 06:27:00 | AQUA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5fad034c-4ab5-32a9-b029-a1178dda13b9 | -15.45908 | -48.43912 | 2026-09-20 06:27:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8444c115-5465-319c-b2f8-a1d3f0679844 | -15.17127 | -48.15342 | 2026-09-20 06:27:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8b73310c-23e9-3c40-9ddd-e6340b27cca1 | -14.69414 | -46.69494 | 2026-09-20 06:27:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 73bacc45-649b-32d6-babd-d64fac2aeb9e | -14.69608 | -46.68336 | 2026-09-20 06:27:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 39d497d9-178b-3e7d-8eff-8f3b6996eeda | -13.88378 | -48.575 | 2026-09-20 06:27:00 | AQUA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 1396e9e0-3abc-33db-afe3-63cb79c8c6ec | -13.88505 | -48.58517 | 2026-09-20 06:27:00 | AQUA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 94ba89d2-ca35-30c7-8f41-f29a805f730b | -14.04925 | -52.08266 | 2026-09-20 06:27:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 371647e3-6306-3ff3-a91f-3c5115253382 | -14.6856 | -46.6886 | 2026-09-20 06:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 255ec76f-6d02-3aa7-9ff1-d8ec88c21e90 | -14.7051 | -46.6852 | 2026-09-20 06:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| cf6719e2-6ed1-39a9-ba69-f4c7d1584b88 | -14.0614 | -52.0788 | 2026-09-20 06:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 149a1916-9fb0-3b7a-b812-891f34e03731 | -14.6856 | -46.6886 | 2026-09-20 06:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 5ff697d3-6843-3659-83d4-7960c3c475b8 | -14.6856 | -46.6886 | 2026-09-20 07:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 59.5 |
| ee16ced5-a642-373b-9b5b-95f7a354306e | -11.08 | -54.02 | 2026-09-20 07:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f0881f8-0030-359b-ad2e-6ef36d091f7f | -11.11 | -54.03 | 2026-09-20 07:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf7acb53-2d76-3520-994a-bd434321871d | -11.1369 | -54.0251 | 2026-09-20 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 39e28325-063b-35ee-bd1c-1fb14418d83a | -11.0994 | -54.008 | 2026-09-20 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| f6760557-03a6-3d89-9fad-537f48adb3cf | -11.118 | -54.0268 | 2026-09-20 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 266.6 |
| 8921f0e3-532d-3ecb-ac46-bc0133e77e7f | -11.0802 | -54.0302 | 2026-09-20 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |


[Clique aqui para ver as próximas entradas](README107.md)
