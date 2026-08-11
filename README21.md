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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6dfd11f1-a4b0-3101-a0d0-785e11d7cd5f | -11.44473 | -46.67353 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d431d5fc-e1c3-301c-ac93-6eccdf15ff26 | -13.56223 | -46.29499 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ef5a4c2c-898c-3757-a1f7-8971e736e38b | -9.13764 | -50.89931 | 2026-08-11 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d6479f1-d7ed-34a7-86f9-60243fa4e671 | -8.89913 | -60.58258 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfc67277-4bfd-3bf5-83e9-a165e01e3a48 | -10.24663 | -45.86037 | 2026-08-11 05:10:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 744e6b93-6df5-3444-9532-218b6adf7380 | -12.47941 | -45.30999 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd8f4f83-e53d-34db-ab6f-9b3e31e18eef | -10.27478 | -60.53783 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 751d1c7d-4daa-33d1-a944-176e93b51a77 | -13.60962 | -46.31934 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9302e47-127f-360c-9803-79eeaf3c904b | -11.3198 | -45.22421 | 2026-08-11 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6d62e3c-6e52-3675-ab23-6601b480fa89 | -9.47184 | -60.52696 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86e1b488-fdda-360a-a380-bec1868b81f8 | -10.10688 | -46.1977 | 2026-08-11 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5aa9c240-9742-3e12-965b-fb057eda6402 | -13.57585 | -46.27469 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dc3b654e-bedd-31ee-bd1a-c51cb305c7e7 | -6.72256 | -58.93964 | 2026-08-11 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f46d589e-aede-3d37-8296-ae9beba27910 | -8.94983 | -60.53977 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60befee5-8d28-3845-b0ec-9365e2af15bf | -10.07293 | -60.50169 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60e5a941-a22d-37b7-9d6a-88c32608b4a0 | -8.94618 | -60.51138 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb840d63-f2a6-34db-8aba-830814572b02 | -11.24587 | -54.87436 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25dd538a-ac65-37fb-91f1-808e1ebb68d2 | -8.94566 | -60.53901 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61deade6-7b55-34a7-9f2a-a933ae8d7b23 | -9.38798 | -47.44786 | 2026-08-11 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| eed887d1-6d66-3798-b1bb-d4af51a2a487 | -10.73378 | -50.45183 | 2026-08-11 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3999f00c-121b-3ff0-9927-71ec41a672c0 | -11.2442 | -54.84146 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52059387-10e8-359e-8d2d-d4ca2fcff807 | -11.47268 | -46.61997 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7992eeaa-eeb2-39ca-a0c4-8258045f69c7 | -8.36887 | -46.39258 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d95121da-cf47-3571-9dc9-d9e4bec25ae6 | -12.4806 | -45.34763 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8876a45f-f88e-3384-9677-3e01cbf4cee3 | -9.46837 | -60.52246 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77f43eee-e245-32c0-ab0e-27fc0f17790e | -10.24139 | -45.85823 | 2026-08-11 05:10:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a439229a-09ba-3651-97b1-132ad94c1dec | -10.72482 | -47.91167 | 2026-08-11 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3bf2dab8-658e-3c5c-b575-6778f832746d | -11.61092 | -54.65892 | 2026-08-11 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be684eb9-b92d-3e21-a282-9d1d410c9076 | -8.90304 | -60.58382 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d4dc328-dd55-3c8f-b03e-41d0825ca938 | -9.387 | -47.49037 | 2026-08-11 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 50df2cde-1866-34f0-96d9-aa01fb86e5ea | -13.57118 | -46.26685 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b9071de-07ff-35b3-994d-9ad99ce6a772 | -13.65093 | -46.25508 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ceb069c5-a044-3d94-839e-6f9f544b4b28 | -10.41653 | -46.67877 | 2026-08-11 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 453a5f94-4c3d-3ce0-a3d1-1f5cf36a0b8d | -12.45615 | -45.31069 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b0fcea3b-e6e8-3fb3-890d-533f23ccaf05 | -12.45425 | -45.32715 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b057033e-b924-3056-8375-ae19a71c1891 | -12.46207 | -45.30747 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1b9b0bb9-87b8-3cba-ada6-db2e000a65ef | -13.48401 | -43.07636 | 2026-08-11 05:10:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d5f5a485-c336-3b40-8962-500861272e39 | -7.23022 | -43.48648 | 2026-08-11 05:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c33b37c7-a7e4-3688-b923-c4003df71697 | -8.89333 | -60.59005 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d107557-54e6-3a3f-bdec-e2d4b7eac6da | -10.86092 | -50.24865 | 2026-08-11 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 917b980e-277c-3552-8ec1-f56388498653 | -11.45437 | -46.68137 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3478bd63-fe58-37d9-9656-337c622cdaaa | -8.94885 | -60.49614 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6c11d3e-371c-3e9c-9de1-57ead00e51b4 | -12.48848 | -45.28568 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fd1aa80-063b-3be5-b63a-16fc0d790b53 | -12.487 | -45.29829 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8af64980-2273-3ac0-b1c2-3bf2dae8b717 | -8.89753 | -60.59082 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1aa8679a-1cc4-319b-8fa0-5685e2034b91 | -11.97463 | -46.35307 | 2026-08-11 05:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccbd5743-c56b-3ccb-bc0d-edc089ce69df | -11.60758 | -54.65839 | 2026-08-11 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 133c91d9-90ad-3381-9b35-6ea40d5aba75 | -11.96516 | -46.34148 | 2026-08-11 05:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c120fe74-f875-3858-935f-387c1bbc6272 | -11.49434 | -54.60406 | 2026-08-11 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 261f8112-dfe4-3d24-979c-4c7636ab6db8 | -13.48873 | -43.07786 | 2026-08-11 05:10:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5b3a32ad-2c91-3976-a350-7f4bcec217dc | -9.39611 | -47.45992 | 2026-08-11 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 3cf89b6a-e62e-3edf-97c9-c20c4bf777b1 | -13.57541 | -46.27837 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f67037cf-b669-3060-a714-05f7d78ab68e | -11.61148 | -54.65535 | 2026-08-11 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63505d53-a49c-392b-a0d2-d17728c9ab7c | -11.46274 | -46.65393 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d8a45b5-6ba7-3829-b017-9b7bc0f1f5c1 | -11.61409 | -54.65255 | 2026-08-11 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3991a45d-0a12-3f71-b4c5-355f2554579c | -11.88472 | -46.81285 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2bc7f4f5-d83b-3c23-baf9-4031a9784fe4 | -11.23032 | -54.84288 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5d049c8-3123-339f-9a05-01a6795e42d9 | -9.24861 | -60.33475 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00d176b8-a3a9-3440-b62c-1da5e2b9b861 | -8.55701 | -45.34893 | 2026-08-11 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97df16a4-0227-352b-aab0-5b5f05804d42 | -9.38318 | -47.44711 | 2026-08-11 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f7dbc477-29fd-3e9a-9b9d-88fb61669279 | -9.47598 | -60.52772 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f98b05aa-80ea-3e1a-9527-5cd7170e78ec | -13.57161 | -46.26327 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d7db856-39ef-3dcf-89ea-076c8b87f1d1 | -12.48885 | -45.28146 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a600a10f-6816-3578-8156-dd9fb3d1cb99 | -11.1948 | -54.85168 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 058de0a9-7132-3562-8a9f-5358c7027fd2 | -11.46271 | -46.65713 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc88c2e0-0b05-379c-8ab8-9717001ffe0b | -8.95169 | -60.50447 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cbf9a69-0f44-3dac-b474-af70a1e06b87 | -7.38969 | -42.86786 | 2026-08-11 05:10:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 95225455-b03c-35e8-bdcc-28310e65f28d | -10.93693 | -57.11122 | 2026-08-11 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7d98071-daef-3403-8512-7be60d22f06c | -11.48988 | -54.61067 | 2026-08-11 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3749405-0034-3ebb-a9d0-6ae99124bb6b | -7.41029 | -60.00814 | 2026-08-11 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23f5a774-3731-32db-a6af-76e17782bd1e | -13.56859 | -46.28853 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| be6a69bb-3aae-3fbe-99e6-8f01a20ca266 | -8.24025 | -46.24608 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 876d849c-adbf-3484-b3dd-11b40d7464a0 | -11.95986 | -46.34017 | 2026-08-11 05:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89a88b88-a039-3c0e-8587-bf6195006a3f | -10.41557 | -46.64584 | 2026-08-11 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4ecf3325-9a78-30e2-a3da-4fcb5fdf7ac3 | -12.45579 | -45.31069 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 743f5b3b-acb1-35fd-a33f-be68b504f4a8 | -10.93633 | -57.11491 | 2026-08-11 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 358fd533-7409-3bdf-8493-81943645bab8 | -8.95619 | -60.55276 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| adf969d8-4e19-35b6-a2e5-9bfba46c8e31 | -7.39499 | -59.99806 | 2026-08-11 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9712d944-5933-391e-87f3-515931d85f41 | -11.17201 | -54.80085 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 605ae512-c359-36de-a238-7f0618d63e5f | -11.24199 | -54.87735 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b311c50-ac19-3121-a92f-e7d23ad997d8 | -10.88946 | -50.36971 | 2026-08-11 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c06aa98-2e70-3c15-aacb-4b749f5cf7d9 | -9.36906 | -47.51432 | 2026-08-11 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 21af3265-80bf-311a-b1a4-45fe7823de89 | -10.41693 | -46.67574 | 2026-08-11 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1f97f11-d936-316d-84c6-a16c1f1b1a22 | -11.24975 | -54.82784 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84f3c817-0692-34a3-a421-b86f9a2170f7 | -11.24864 | -54.83492 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d615727-3eb7-3a93-a65d-4f616fd58664 | -11.4588 | -46.6884 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 71b372eb-6b0a-309d-9111-56aed55c1e97 | -12.49232 | -45.30312 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3c81345-36e5-3467-9257-cab5ffd10e8f | -12.45428 | -45.32301 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 31212a2d-78a9-3dab-89a0-eafd98482517 | -11.23199 | -54.85403 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a80a2950-0839-3fd6-8967-45352ac012df | -13.55543 | -46.3051 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 76decfbc-823e-37f0-9097-702a41b39686 | -12.46105 | -45.31571 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 37a297dd-0a13-3971-8099-a0652da73e6e | -11.22588 | -54.84942 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1416487-e2c4-3ed3-b157-a44db9c5fcb6 | -12.46156 | -45.3116 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 16d4cfb7-147a-381f-8c4f-902039be3de6 | -7.40806 | -59.99632 | 2026-08-11 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4adfed25-f50b-3bde-9aca-549941f2394f | -8.66007 | -54.95929 | 2026-08-11 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3507ebfd-d45c-3df0-ac0d-cd6d908c8b20 | -13.59554 | -46.2508 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a64c72e-55e5-3942-b843-c76265d8c986 | -9.39467 | -47.4703 | 2026-08-11 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9a7d5a3c-2d3c-371c-bae6-cd592e6094e8 | -9.39203 | -47.454 | 2026-08-11 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a35a5ed8-e35c-33c3-8860-034f6da71302 | -13.57716 | -46.26372 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5ccba54-44b6-3fe1-aa28-be04dcc87b4e | -11.491 | -54.60353 | 2026-08-11 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README22.md)
