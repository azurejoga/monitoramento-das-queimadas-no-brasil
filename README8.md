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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6ace7d0-182a-3ab4-ab92-80d6b62f6f75 | -11.96002 | -44.32077 | 2024-12-23 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb4a9cdc-e2bc-306b-a2d3-34f9bb30ee2b | -10.81769 | -40.49316 | 2024-12-23 04:10:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| febc1de9-d3bb-3dde-89cf-03dbf81971b5 | -10.81713 | -40.497 | 2024-12-23 04:10:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f06ed642-4c46-3dec-9ec6-821634e2eb33 | -11.76195 | -44.86744 | 2024-12-23 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6dff3a1a-23a9-3107-adfb-526ae253ac07 | -11.57884 | -44.8692 | 2024-12-23 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df96bdc9-531c-3d33-be3e-a49590ecd76e | -9.73677 | -42.15872 | 2024-12-23 04:10:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 68bc436c-08d4-3344-91bc-b99ed1554c2e | -13.50847 | -44.30269 | 2024-12-23 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a0ad7bf-d464-3601-981d-6aff5a9417af | -10.43044 | -44.88982 | 2024-12-23 04:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 849e9184-a36a-3e9c-81f7-cf40d07db386 | -12.33556 | -43.67693 | 2024-12-23 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2737da9f-7955-3713-8a0c-ed286268106e | -8.97995 | -44.25533 | 2024-12-23 04:10:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faa39d47-067e-30d2-838a-7e394bfaa24c | -12.335 | -43.68047 | 2024-12-23 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b691a13-fbb5-3af7-a3ee-09bddeee3117 | -16.85258 | -39.23546 | 2024-12-23 04:12:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 80c867b4-cee5-39eb-9753-d67dcbbcaab8 | -18.51395 | -53.40094 | 2024-12-23 04:12:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e46bcd5-d300-3ec8-98a9-4a0e1e847c8b | -16.86048 | -39.23672 | 2024-12-23 04:12:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| ac9e0480-11db-3076-95aa-9bd5343301de | -19.34043 | -54.17134 | 2024-12-23 04:12:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 25a2757f-1062-3b80-8ae8-65f4cd4276a1 | -16.85979 | -39.24199 | 2024-12-23 04:12:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| edb0fd21-d428-3699-84f3-0a9fac49ee12 | -19.33448 | -54.17372 | 2024-12-23 04:12:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3750a17d-b869-38c1-801e-93342d82232b | -16.86373 | -39.24262 | 2024-12-23 04:12:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2a16527e-b423-3434-ad2d-a84b5344a081 | -16.86511 | -39.23207 | 2024-12-23 04:12:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f28304a5-8927-3e1f-9033-3e158d73632b | -16.86442 | -39.23735 | 2024-12-23 04:12:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6981b91d-85e5-3191-8f60-3ba28a1d2c4c | -16.86117 | -39.23145 | 2024-12-23 04:12:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 806483f7-05df-34d5-acd1-7ec1d995b617 | -16.86838 | -39.23793 | 2024-12-23 04:12:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e1f5fa4b-0b63-3ee5-8a30-cdafa08b4455 | -18.51457 | -53.39789 | 2024-12-23 04:12:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03f7ef90-dfc2-3a8a-b371-aa89ffd0f4f3 | -16.85653 | -39.23605 | 2024-12-23 04:12:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| ad50a430-f0d9-37cf-aaf1-50131601bddc | -16.85585 | -39.24131 | 2024-12-23 04:12:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| fc8edb1e-0629-31c3-8ad8-ead70d2f5151 | -19.33898 | -54.17821 | 2024-12-23 04:12:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e8b6e777-343e-3132-b920-4e0756818e15 | -19.33971 | -54.17476 | 2024-12-23 04:12:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8736a633-f08e-3116-9510-31b0a1a41916 | -26.42023 | -53.09349 | 2024-12-23 04:14:00 | NOAA-21 | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e7405bde-2292-383d-a912-1d8a34b8a7d0 | -26.42113 | -53.09437 | 2024-12-23 04:14:00 | NOAA-21 | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c43655ba-bb89-3020-ac70-02fcd36076dd | -20.99745 | -51.79301 | 2024-12-23 04:14:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c1b6993a-ff98-3eb1-b57f-8d8954bbee40 | -29.22099 | -51.96673 | 2024-12-23 04:16:00 | NOAA-21 | NOVA BRÉSCIA | RIO GRANDE DO SUL | Brasil | 4313003 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 829c3602-c4d3-35a7-9e42-7327e0ad44cc | -29.87319 | -51.15786 | 2024-12-23 04:16:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| cc65b7f5-b233-3303-858b-0386c372b306 | -4.03029 | -46.79317 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b4b10be-9953-30d5-9d0d-1f9d9c7e0099 | -3.93008 | -46.888 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bdb7949-3a9a-368f-b95c-f23e66c71a90 | -3.80027 | -46.83597 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9fc8cb9-cc14-385f-b09c-ba039278c907 | -1.63745 | -45.85255 | 2024-12-23 04:31:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cad6e678-428d-37ff-9443-e58ed06073cf | -3.85281 | -46.66939 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aee72a7d-4f97-37e4-8e58-2e23ae6c22b2 | -3.80196 | -46.8469 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae4cab1e-f288-3efd-88c6-798f691c4129 | -2.07637 | -52.04755 | 2024-12-23 04:31:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09596c36-0b2e-3f4e-a81e-563e19e61686 | -4.07995 | -46.62261 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b6be22cc-b72d-328c-adf4-a52ebfbbabad | -4.10333 | -46.82288 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0bdafe6-7d9f-3487-b7b7-c1d9bb98d458 | -0.93316 | -46.88693 | 2024-12-23 04:31:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81b7e9c7-53b8-3ab2-bb6e-d05f25230a35 | -3.8094 | -46.71272 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f062860e-29b5-3fab-b2e0-671fc3bb351e | -4.10226 | -46.63317 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc0c4c13-2fb6-3919-9ba1-8becadc0dfda | -3.87916 | -45.16867 | 2024-12-23 04:31:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a03f17a5-32d9-348e-80ac-14c562aea6f8 | -3.99126 | -46.73714 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a157ba20-4c16-38b1-8b29-7b48ed2685f7 | -4.08325 | -46.79841 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c84ac35-9667-3c33-b6f2-86a2715fb3dc | -4.22758 | -43.78575 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a7e2875-146a-36f9-aa20-e74bf16713bb | -4.01247 | -46.33747 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e055a9c4-4bcd-3398-94df-bc9e6c7873d4 | -2.12945 | -53.47793 | 2024-12-23 04:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73d17096-78bf-39b1-aa82-f1a83ca2b8eb | -2.87392 | -45.94131 | 2024-12-23 04:31:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 942a4f09-c9f1-3c60-b1de-a1fc6180526e | -3.91733 | -46.67224 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a8efd2bc-c750-3f22-9693-d4f101e9c9d0 | -4.02191 | -47.05919 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54f654df-bd16-38da-b7e4-2f22db010337 | -3.9962 | -46.92316 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef77eb89-b947-3e89-b547-304bd99759c5 | -3.93217 | -47.02686 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c60b8112-016c-37ac-b364-f54f67f02fd7 | -3.1029 | -54.54813 | 2024-12-23 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbeed7dd-6001-3b83-9caa-a1bde843ec4d | -3.90773 | -47.00888 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4f8745d-2ab7-30fd-833e-2296fecd1e27 | -3.91411 | -46.92464 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7e95e1c-b6d4-387a-96c1-f64f4da1b5c7 | -2.7419 | -46.20338 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9eb1d0f5-dcd5-3e2d-b6aa-99ac80cad0ed | -2.7408 | -46.21041 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5222789e-2177-374b-92b4-d668867c9a9b | -3.14381 | -54.56543 | 2024-12-23 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50d1915d-a183-3421-98f0-b8093c049534 | -4.03515 | -47.03997 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ec91824-8267-3538-89ae-14dbade4b12a | -3.90271 | -46.99747 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2323d50b-f3b3-37a3-8aa8-ac9a8c0c1e1b | -1.93994 | -45.63454 | 2024-12-23 04:31:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4719d339-e02b-332a-9387-836f7d02cf85 | -3.78377 | -47.11031 | 2024-12-23 04:31:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8409c7e0-3bb1-3716-9750-f666e61eb876 | -3.53143 | -52.66997 | 2024-12-23 04:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e50b495-6972-33ff-981a-cd277b7849a0 | -3.9718 | -46.92647 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5767a766-36d8-3a95-bfdc-12beea8c9cb0 | -3.88546 | -47.02687 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18a66b9d-8f5c-3d56-aca4-cd30ed1a2c6c | -3.51028 | -47.1951 | 2024-12-23 04:31:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c25bcfbd-5417-3e54-8db8-f2e50692ca99 | -2.12418 | -50.70523 | 2024-12-23 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bba73f2a-6a68-300c-9a66-2c71c9da5edd | -4.77346 | -46.38197 | 2024-12-23 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a053aa4b-ba88-3144-8ac2-3be8e1561046 | -5.18984 | -43.97248 | 2024-12-23 04:31:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a5bc38d-257d-3f8b-8958-1eaae07a6d84 | -4.05172 | -47.02124 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fdce70b-4742-3ee2-89d6-4320c5620164 | -7.54063 | -35.3022 | 2024-12-23 04:31:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 2e60174c-7d76-3bfe-bee6-faac36dd2971 | -2.64627 | -46.10239 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a219c026-c60d-3504-b95d-8b50af393468 | -3.00122 | -48.12519 | 2024-12-23 04:31:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d94e2cbd-5f25-333b-8621-357004537556 | -4.01194 | -46.56122 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 904f74e0-70d4-3376-82cb-4063481034bd | -6.63645 | -46.64845 | 2024-12-23 04:31:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 357b4781-1c1a-33d9-82d3-5a0ad06b26c9 | -5.9302 | -45.4848 | 2024-12-23 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57be17b7-74d3-37a0-ac6e-21de4a1b9edf | -3.92382 | -47.01492 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ded52df-7c4b-3320-ac8b-db9c2d0988ec | -6.93726 | -43.5298 | 2024-12-23 04:31:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d9a0e821-a2b5-32fa-82a9-d475eb4adf75 | -3.91906 | -47.08866 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af8ae84e-e203-383e-a11f-e603cd1bd2c5 | -4.37647 | -44.00182 | 2024-12-23 04:31:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c3b1692-f9f0-37bb-860b-552ac31b517f | -2.40393 | -53.74535 | 2024-12-23 04:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 31966413-86ac-3747-a91e-dfbe548e00f7 | -2.55263 | -46.93928 | 2024-12-23 04:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d3fc8e7-d4ea-327b-aff0-00a24070627a | -3.97888 | -46.68517 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2729605-cc7c-384a-abd6-69130bc31d14 | -5.82397 | -35.47997 | 2024-12-23 04:31:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 496a48c2-380b-3981-88ce-702f5d2feaae | -6.90828 | -43.53817 | 2024-12-23 04:31:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| fbbc9b85-bca6-3e81-817c-29214b2af37b | -4.00247 | -46.99166 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f57b424a-24b3-3307-a23d-00413305d8de | -3.9935 | -46.74463 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6e29a799-7ec5-34fd-9d04-b1fde5e02458 | -5.35965 | -46.22105 | 2024-12-23 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85a6c7f4-3fa3-3aee-bd17-211de4152c63 | -3.83381 | -46.68794 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c88152c7-bb2c-3d10-b8ac-d471fe2b4d11 | -3.90386 | -47.01182 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22a473ff-3085-324f-95e0-d93a405b97ec | -3.78641 | -46.83734 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5ad0c53-51b7-3492-8d07-4e31857cfed7 | -4.44548 | -45.93056 | 2024-12-23 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 360b6e04-a951-3db7-93ef-376bdfb2e899 | -4.0344 | -50.0601 | 2024-12-23 04:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d8b20aa-7e2e-3f8e-865f-c74317e23d28 | -2.26823 | -46.39839 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9a158b31-3d15-3886-8220-ee951d9ed2a6 | -3.87242 | -46.91475 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b97934d1-e70d-360c-80a9-2f78bb8fe927 | -3.98928 | -46.34515 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3472224-13a8-3fc0-a1d8-36a765d7d0fc | -5.82159 | -35.47917 | 2024-12-23 04:31:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |


[Clique aqui para ver as próximas entradas](README9.md)
