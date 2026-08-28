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
| 5765ae81-8c7a-3594-9f73-5a12c8375efb | -15.73108 | -51.17653 | 2026-08-28 17:26:00 | NPP-375 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 55c704b6-2589-3d44-93fe-359a5124120d | -9.86546 | -45.84979 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 24016120-2f78-3af1-9427-fa2d313231b1 | -13.79718 | -53.92615 | 2026-08-28 17:26:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2acdc588-8a1a-322a-aaf7-3e0fd3f95341 | -13.25891 | -51.56434 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6e56d1d2-909b-35a8-ac3c-352e1c2660c8 | -11.3232 | -50.69804 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f9a474f4-5902-3848-a843-ddfd8059bc39 | -14.3679 | -53.02011 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 09305528-d9cc-34e6-ada3-88de8813a8aa | -14.58024 | -52.11814 | 2026-08-28 17:26:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 2e6db9ad-2bf2-3834-ad9a-5aa845f04517 | -14.49538 | -40.33215 | 2026-08-28 17:26:00 | NPP-375 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| 3689b5d9-01d1-3e37-b0aa-6a0c0a62af3b | -15.72412 | -48.25519 | 2026-08-28 17:26:00 | NPP-375 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f31ad5c7-6922-3294-9d6c-073d831c3f69 | -9.80104 | -46.33189 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b9eefed2-2e28-3f62-aea2-b015643a7826 | -10.77373 | -50.62687 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 872512b1-af00-3b3f-a062-7433f2702823 | -17.55981 | -51.11454 | 2026-08-28 17:26:00 | NPP-375 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9e508f8c-a837-367a-96d0-e13e76026598 | -11.21376 | -53.99271 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7ce6791b-a022-3437-96b7-edf51b424c6d | -9.85973 | -45.85082 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 43b3bd51-0167-3e47-a681-2c49819d007c | -13.10819 | -50.04771 | 2026-08-28 17:26:00 | NPP-375 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 38cad5cb-ceac-318b-b64f-abfcc02f8bc4 | -14.90989 | -56.32206 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 6238d5be-ad52-35bb-abe8-e0b763d623b9 | -10.76399 | -50.64378 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1372a27f-ffaa-3813-ab14-33057784e31a | -11.24243 | -53.99572 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 21bdd67a-8730-324b-a627-27c8b1ab8b96 | -14.1792 | -52.85595 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 309463d2-cad5-3686-9adb-1d670c498ff3 | -17.59319 | -52.49612 | 2026-08-28 17:26:00 | NPP-375 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fbc25c19-1053-3da2-a269-d8dce11c94d5 | -13.97618 | -54.02421 | 2026-08-28 17:26:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ea9b9d8c-402c-3bcf-a3e7-b2dbb479d468 | -14.90935 | -56.31836 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 7571db50-68b0-32ee-b3a6-934638404a39 | -10.08961 | -46.9887 | 2026-08-28 17:26:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 695740d6-8603-334d-84ad-2b50b87f3838 | -14.1788 | -52.8317 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 52110a67-71e8-33f4-b3e9-6ce3e6638380 | -13.8763 | -53.2417 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| dafadec7-6547-3918-9911-70c5b6e4baf5 | -14.60477 | -53.14614 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8a39bf68-4a06-31b5-ac15-d73b0077effd | -10.9147 | -46.61918 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2b2e546c-89d7-3141-87a6-ce491652dc3e | -11.29478 | -54.03733 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4ab59cae-7117-3778-acba-75fcc4f836d8 | -9.84175 | -45.84965 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 4b75d7c8-0f29-3167-95ae-a0c58e8a6910 | -11.25191 | -45.05386 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8dce99be-899b-36e4-8783-2e8521e1e3b1 | -14.45967 | -53.37751 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ab3ab9f2-dc62-3fe9-9e82-2b6ef54f6a7e | -11.23617 | -54.00063 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c47f5b0d-e195-322d-b968-1d4c2d4e3709 | -16.12445 | -55.87357 | 2026-08-28 17:26:00 | NPP-375 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9ae16313-1b7c-33a4-973c-8f96f1f36955 | -11.70865 | -54.54067 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 5e23ed1c-1990-3d1d-a5ee-f456c3adcecf | -14.54571 | -53.301 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bd3787dd-a1b3-3d25-b742-f868b05826f4 | -14.4731 | -53.19958 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a2e5cb06-3adc-37ab-afd0-55e69be466ad | -11.62612 | -54.5875 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| de951da7-3847-36ab-8c1e-5b6fb444666b | -10.90976 | -46.65141 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea3ccb1f-6889-38b9-8f16-cf28cfe799d2 | -11.37152 | -45.14434 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c3f6099e-fb14-3e29-a7c7-802d277f9cfa | -14.1839 | -48.76283 | 2026-08-28 17:26:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fda5b48e-1883-3700-a68b-f634cddc94a7 | -13.42461 | -51.79625 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c3139780-f8eb-348d-93b8-892c3a0f37bf | -13.86966 | -54.12119 | 2026-08-28 17:26:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 302f9f00-443c-343f-8fc7-8c4f34cdd2b1 | -11.27303 | -54.0332 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 5f3c361a-aff4-36c1-b07a-fc58c432b007 | -10.92258 | -46.63157 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8fcd799a-5018-3f7a-8ddd-04e9e8f8ff78 | -9.84249 | -45.85358 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| f38311c4-9987-3173-a022-2497f8074fff | -12.90791 | -45.86376 | 2026-08-28 17:26:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d59600ef-4e99-3425-a8fd-2357d0ba9227 | -11.51593 | -58.50753 | 2026-08-28 17:26:00 | NPP-375 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 05e65817-1947-3ea6-9200-7c0099292274 | -14.60539 | -53.14996 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 79d4645f-09e4-3c40-ae80-ef38fb1e84ab | -13.87569 | -53.23786 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 0392d933-5b00-346c-8982-d0d30ecf38fe | -9.50375 | -45.66801 | 2026-08-28 17:26:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4611b4ab-b7d5-3ec1-a9c4-77ac5596f8f5 | -14.19377 | -52.8575 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 91c5f90c-7e99-3d66-881c-76c0cf324f4b | -14.17945 | -52.83567 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 25351be4-d432-30ea-be4b-a086c5d1761a | -11.20634 | -55.09529 | 2026-08-28 17:26:00 | NPP-375 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5f1103a2-5303-3ec5-b707-47d57baead77 | -14.18513 | -52.82661 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| abbb1790-8895-3400-b63c-2ac6a5a43185 | -11.23779 | -53.98877 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 4c9516f1-284b-35aa-a396-4fe4622cc427 | -9.51138 | -45.65089 | 2026-08-28 17:26:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 2025faeb-bfc5-3876-a43e-e75c49366799 | -11.02345 | -49.6624 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1f155bae-5ff2-39d4-8d33-a2ce3fb7f6a8 | -13.35304 | -46.90258 | 2026-08-28 17:26:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f56c7dc4-4321-36da-ab5e-b4fa7a8efc15 | -17.59241 | -51.63997 | 2026-08-28 17:26:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 37863a53-73b3-3e11-b6f1-577e01d69602 | -13.87914 | -53.23729 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 44253592-2ca4-3810-b094-39c4b12e2398 | -11.96578 | -45.50003 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 670de238-01d2-36f7-a0ae-7806dbe390f4 | -14.30224 | -53.15404 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7a2d0052-5893-3734-91ca-b6c5440c6b67 | -11.24597 | -45.07401 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0c66a4d4-b5f8-34ce-a49b-6813f24998bf | -14.53302 | -42.05919 | 2026-08-28 17:26:00 | NPP-375 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| d6d5ea7a-2541-339d-971d-66be3b55013d | -11.48207 | -46.94217 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 88eb3610-14b3-3db8-b68e-a56f352f3e45 | -12.78618 | -46.45387 | 2026-08-28 17:26:00 | NPP-375 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a25ad53e-3a06-3f0a-9ce7-9aca4855d413 | -13.40103 | -51.79142 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5ca84abb-fa77-31f3-892d-cb095f77177a | -13.41941 | -51.76487 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 49944388-0fbb-3860-8892-5dbbb68b753c | -11.62497 | -54.58025 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 30e1e2c7-27c1-3a88-ba55-f1b5d3ec7bcc | -9.6914 | -46.56134 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| d18766f2-ced7-3803-bc0e-3ba93498f97d | -11.14447 | -45.5734 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5e49cd2e-cbcd-3754-99de-7e1042043a83 | -11.37657 | -45.13933 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0a63b9e3-6fcd-3d4f-8904-1aa81d136824 | -14.21668 | -45.30403 | 2026-08-28 17:26:00 | NPP-375 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8ca33cec-ee44-3449-9749-fcaa68f1f4db | -14.54289 | -53.30537 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 04f3ae24-f51b-3eeb-bf3e-0326682e9445 | -12.38799 | -48.19563 | 2026-08-28 17:26:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 03761ba4-2016-3597-bdb4-dbee4aa97efb | -11.24781 | -45.06394 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| aa7ec7e7-48e2-3ca7-8fa4-df8fb7f25c0a | -11.21033 | -53.99327 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 74a549f5-654d-330f-9200-204ec011eaab | -14.63793 | -57.0108 | 2026-08-28 17:26:00 | NPP-375 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 8c17cbc0-c587-3d4a-9cbf-cfb78dac3d2a | -17.55621 | -51.11525 | 2026-08-28 17:26:00 | NPP-375 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 1a5b9017-2d71-31d7-a089-32ca6bb9bdae | -14.87444 | -52.60365 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| cc6f2bce-a71b-386e-bd6b-201dd0659092 | -14.47357 | -53.39838 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 64b2f586-9604-3a5e-8cfa-432ffa7e4308 | -15.86227 | -41.96448 | 2026-08-28 17:26:00 | NPP-375 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| e9db15f5-f79b-3b92-83a2-505d53f57385 | -10.88209 | -50.50466 | 2026-08-28 17:26:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| bd4af8d8-2f1e-3117-970b-127e7745cca2 | -12.0842 | -47.18134 | 2026-08-28 17:26:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3757d749-87c2-34fb-a966-2d4a8f0a6012 | -10.9192 | -46.64292 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d3ace78e-d7d5-3a25-8c12-7b5a2055f430 | -15.24203 | -53.86227 | 2026-08-28 17:26:00 | NPP-375 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b8cfba5a-3220-3f06-a93a-31e1664b4903 | -11.17268 | -51.23902 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1a41ad33-9600-364a-b3f8-882e98f8341a | -12.6946 | -48.42713 | 2026-08-28 17:26:00 | NPP-375 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9a8f8bbf-a285-3676-962e-c7bfbd0a28d1 | -14.88685 | -57.99577 | 2026-08-28 17:26:00 | NPP-375 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51e1787e-c7fe-391b-8b22-a16d5f11932d | -13.41204 | -51.76626 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 39272fc5-4bf8-37ce-b217-c0d2171fd38b | -15.73554 | -51.18032 | 2026-08-28 17:26:00 | NPP-375 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 30e065cb-fed6-310d-bbf0-670e7d04d881 | -16.17019 | -58.581 | 2026-08-28 17:26:00 | NPP-375 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 17f70522-f3b4-371c-bb7d-8fe984b082c3 | -13.86322 | -43.64216 | 2026-08-28 17:26:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 78dd25f2-ebf6-32f0-a347-484d8d7151a3 | -15.59304 | -56.07067 | 2026-08-28 17:26:00 | NPP-375 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ba876cac-6a86-3b14-a54d-74c9fa047973 | -13.83336 | -54.04463 | 2026-08-28 17:26:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b79337d6-563c-352c-9b50-7dc56e412288 | -11.96652 | -45.50391 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ea9d9287-414c-3aa2-98a7-1b1b8eb94665 | -13.42311 | -51.76421 | 2026-08-28 17:26:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 60e536d6-ebd0-3e3b-8a8e-aedc892e8026 | -12.22023 | -50.54266 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 043028fd-025e-3c08-84d7-85c1c1d2ec47 | -10.77784 | -50.62616 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8c6164cb-cf53-3bd6-b2be-d71e833791e6 | -11.23677 | -54.00438 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README107.md)
