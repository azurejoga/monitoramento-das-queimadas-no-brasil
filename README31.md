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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a48687ff-a740-380e-a745-77d104dbcd77 | -0.4162 | -51.722599 | 2026-10-08 00:48:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 222c7b59-e664-3d15-b501-c142dcaddfce | -4.1539 | -55.1399 | 2026-10-08 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92b30241-888a-344b-9f2d-1d4f8f8d85af | -3.1145 | -53.777302 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b8824e8-896b-3049-b4a2-77793fb6e0a2 | -5.2792 | -60.0867 | 2026-10-08 00:48:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1bd0b34-2b93-3c17-9fd7-d287e6f8e7e0 | -2.6002 | -57.584999 | 2026-10-08 00:48:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 382f564a-1e52-3522-a019-1f7dba2fb483 | -8.3969 | -46.317001 | 2026-10-08 00:48:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 112a9f6e-7248-3c86-b17b-6d6f035e4a0e | -16.866301 | -40.584202 | 2026-10-08 00:48:00 | METOP-C | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0d8943b0-f87b-335a-a728-d5a3d4237654 | -2.7778 | -54.062801 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c88a8ca-02c1-37b1-8bb4-267b33de6f56 | -3.0457 | -54.153999 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5448e85-27a3-3290-8a24-c86481ffdafd | -2.4857 | -58.075699 | 2026-10-08 00:48:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a3a3289-f365-3c82-827c-b362f95672e8 | -14.2316 | -48.547901 | 2026-10-08 00:48:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c5176847-222f-3dd3-83a0-61a019810a09 | -13.5054 | -44.371601 | 2026-10-08 00:48:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7ca03486-0c7c-36b3-a75f-51e8d3e6ad37 | -2.7846 | -54.0928 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25d8da81-643c-3965-8a92-a30468e96016 | -6.8892 | -43.686401 | 2026-10-08 00:48:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a5bef7f1-49ee-3f72-ab9b-99ca0bdc3ccc | -3.017 | -54.072899 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c582bb96-fb7b-3868-8050-18ca79a92b7b | -3.0469 | -53.932499 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37ca9bb4-93af-3623-b359-204d024708ed | -3.3065 | -54.032501 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbb634b4-937b-32dd-87d3-56d4fc68388c | -5.8787 | -50.091599 | 2026-10-08 00:48:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b29526b4-8d9e-314d-af83-41cd204836bb | -8.2137 | -46.370998 | 2026-10-08 00:48:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9de6050-84cd-3516-a069-18b85dec61f5 | -3.0984 | -54.294998 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd242b09-6934-3e9b-ba95-510b57ca0984 | -3.0538 | -54.144299 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3724685-d59d-3cfa-bbcc-5aa1a7f6c6f7 | -2.9317 | -54.0602 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be6fa271-46ac-31d9-9b52-756b04b920a9 | -2.9345 | -54.162701 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a33be969-5e59-3928-9d51-5cb1b732cf6b | -6.0523 | -51.746201 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 125029c6-3028-391f-8af4-5d8b67411563 | -6.0378 | -51.727699 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc177798-08e5-383a-9413-4bb689727930 | -3.7203 | -54.222401 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cec0dcf-0ccd-31a8-9d70-d692403a1fbf | -2.98 | -54.1367 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8302dd8-808d-379e-b4a9-9ca6909592d5 | -3.5257 | -54.680901 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc797d9f-28b2-3413-af2c-7ad2f1f51cf3 | -3.173 | -58.627899 | 2026-10-08 00:48:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb90404f-ce28-3b8c-9827-e4ac2c7c1741 | -1.5268 | -54.539001 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e613d478-5e5d-3b6b-8ee2-c0de5aa87220 | -3.3216 | -50.187599 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4566b999-aa8f-30d5-8d4f-da9f8274d0d5 | -0.4178 | -51.7295 | 2026-10-08 00:48:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c31b7c44-4653-395a-8ff1-c3e6e654876b | -3.0823 | -54.314701 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44b70f9a-6295-30d1-af0c-f70f80fe892b | -2.9795 | -54.089199 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c1c2ce6-cf70-38b4-b9f5-3baa3a9fbc8c | -2.9927 | -54.1021 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 072aa5fb-2ad0-3235-a570-eb2ce8ff1532 | -7.881 | -55.004601 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 237f7815-b752-3931-806e-5f74286a0751 | -3.4719 | -54.625198 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af3c2009-9871-3cd2-b038-a7801981c6b0 | -4.9513 | -55.121399 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea8114aa-b568-3353-98af-0bcea66470b6 | -5.6919 | -53.473499 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 579c1c7b-8094-34e5-9e6f-206f0222bb9e | -5.7683 | -42.069099 | 2026-10-08 00:48:00 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6fb90a4a-b847-3a25-8b27-f47e82b9f57a | -4.2858 | -49.097599 | 2026-10-08 00:48:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceeec7cb-b741-32eb-a6e4-d13cb5cabbf6 | -15.2483 | -49.814098 | 2026-10-08 00:48:00 | METOP-C | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d4f1e063-6831-3ceb-b051-f0d7cf19848f | -3.3693 | -50.482899 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c20aa167-57eb-3bd9-8bf0-f85947a3e2de | -9.8742 | -50.514099 | 2026-10-08 00:48:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5febfece-7640-394e-baf3-5de9f27e82fa | -3.2231 | -54.299801 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98f9cf95-a9d4-3b17-b5b1-c41ac997bb6a | -2.509 | -56.1842 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f70feec-fe33-3f43-9a48-ded54386f5e8 | -16.875 | -40.616699 | 2026-10-08 00:48:00 | METOP-C | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ebcb4707-8ef4-3a5a-a876-9cd4804b3149 | -3.3134 | -54.062801 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e0e565d-5c4c-3209-9d09-86ae561f541a | -2.863 | -54.210499 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69643226-e6f1-34b1-a04d-78f2e13dd2d3 | -2.0416 | -56.2085 | 2026-10-08 00:48:00 | METOP-C | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ace7e0bf-c3df-381b-8cca-fb339866d976 | -3.183 | -50.569302 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21f464bb-f7f1-31ba-a56a-61bd399dddab | -3.6987 | -50.658798 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2c553c9-8f72-3135-818f-08e16ec8ff82 | -2.9812 | -54.096699 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecd12e5d-1378-3f53-8d13-bb7b73b921c6 | -3.5551 | -59.469002 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f06cad3-cbc5-36ff-bd23-b383be5b0b91 | -18.382401 | -41.965099 | 2026-10-08 00:48:00 | METOP-C | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c48110ef-3f00-3f3d-9749-8ebee1dd5b02 | -2.3953 | -57.902699 | 2026-10-08 00:48:00 | METOP-C | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92401412-cb4b-3a1b-9607-1afb7baca1ac | -1.1023 | -54.170502 | 2026-10-08 00:48:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5951798d-4320-336d-9d0d-5f2cfe3760cd | -6.209 | -52.845299 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dce9e6b-1ebf-3c80-bbf3-ea4ac9030175 | -3.2638 | -54.0261 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f74e514-f148-3b9f-b2c2-53999cc58cac | -6.2269 | -52.787899 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d13ca43b-aea3-3d36-ae9b-4f0e6290dab6 | -2.942 | -54.1054 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f3f4981-bc3b-34e3-8fed-f0e66b3dd192 | -3.0199 | -54.0406 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59cc41c8-b6d7-3cba-bbb6-d88b0b97ad3d | -11.0143 | -45.4333 | 2026-10-08 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 51669c69-67b9-32b3-91a1-acfa31b79e34 | -2.4821 | -56.111301 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97f36946-c279-33af-9794-4a236d045967 | -1.4778 | -54.5499 | 2026-10-08 00:48:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c725fe2-583c-3710-be75-2484c6f9f8f5 | -8.0925 | -55.316799 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f27698c4-6f27-3e5f-adfe-9537a8b2c2bb | -3.3031 | -54.017399 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9edd78a1-c299-3d51-ac4d-99736cec6aca | -16.8442 | -41.048599 | 2026-10-08 00:48:00 | METOP-C | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ebac0255-aeae-3ec1-a3ae-e69cf96cb23b | -2.8642 | -49.549198 | 2026-10-08 00:48:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0482c241-abfc-3c79-9f2a-baa7b91cd41d | -2.3766 | -56.144402 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b12b5203-3a0b-32df-b38e-9ab115a31efc | -6.1444 | -47.958 | 2026-10-08 00:48:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ddb18491-7617-3e25-a994-955d48b08b78 | -3.108 | -53.7943 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66fee506-011d-3f2e-b15f-0bc3b539cf69 | -2.9621 | -54.148602 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3aa1eea4-72e2-3277-aada-0ec478232d53 | -6.1377 | -53.076801 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 620cef01-492f-39f5-b6e8-d3505ce9eeed | -3.4733 | -50.0854 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d156c231-0416-3e6e-b1d9-9c3b3a59da5d | -3.3116 | -53.873798 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fb8bd1f-8278-3d38-a4d1-b3a51724b99d | -6.9513 | -45.2892 | 2026-10-08 00:48:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3f48b32-1441-32aa-84bc-116d8adfcfe9 | -11.6332 | -43.710999 | 2026-10-08 00:48:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0625b41a-9619-3c34-8dd8-e207a9ae71e1 | -8.7376 | -45.165401 | 2026-10-08 00:48:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3abc98ca-e166-33db-83a0-e77274ae7dad | -2.8889 | -54.188801 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86e7fe85-4205-36fc-9561-a5440f1e3df4 | -3.044 | -54.1464 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13d3de4b-60e8-3673-ae6f-5eeaa4324248 | -3.0371 | -54.116001 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c20a0183-5b0b-35d6-885b-99048005e355 | -3.5356 | -59.473202 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5348f54-9d77-3b00-9791-83557ee6ebab | -3.5845 | -54.667999 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 233cd667-8496-32c5-b606-b9a687d47d7b | -2.8832 | -54.118401 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d743a4ee-7c90-3b22-be7b-fd988803a18f | -2.9604 | -54.140999 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e2dd3e2-e042-352f-ae89-15c734682347 | -3.3298 | -50.178299 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1fd10ca-b6dc-38e4-b10e-ab37ec2a60c8 | -3.2133 | -54.301998 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8935d5d5-4844-3d4f-85c7-ac1c46ba718c | -3.2604 | -54.011101 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0d0350d-7289-331c-814d-a36f7e93b05f | -3.1911 | -50.560101 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccb519d1-c2a4-3876-a91e-275d48431f16 | -4.2416 | -51.044498 | 2026-10-08 00:48:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb76d8f9-1a54-3c1b-9778-62cd4f5c3975 | -2.8959 | -54.084 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3333e10-343e-3cfd-ac09-63a3601dad35 | -3.0123 | -54.233398 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 559aeed7-27e7-3986-8d9f-28c79e998d8d | -3.0458 | -51.227001 | 2026-10-08 00:48:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6814853-c1fc-3db0-84e3-88640548c566 | -3.07 | -54.260899 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53b28dc2-a12f-3f1a-a51a-d0ec5215ac80 | -0.4064 | -51.7248 | 2026-10-08 00:48:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c3711354-051d-3005-aca5-1d2f605c4776 | -3.1646 | -54.087799 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49b0af1c-d2e2-3321-a135-2035b0d09b2d | -2.5047 | -56.165298 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69cbaa47-9f4c-302e-a5e8-4ddc5d37f45f | -3.1666 | -50.5877 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d625a85-c3d8-32c3-af11-daa011468723 | -2.5701 | -50.685299 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README32.md)
