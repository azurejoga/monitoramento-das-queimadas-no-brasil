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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5019418c-7b6f-33c7-b52f-900fd2b39c33 | -13.18774 | -51.56021 | 2026-09-23 05:06:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 784b22a6-a19d-3b37-b7da-0efbd9441cc1 | -14.63929 | -45.62109 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9c4e1ab-e820-3375-a3c1-f479f783f532 | -12.41722 | -46.97564 | 2026-09-23 05:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 56765c44-e2f5-3d83-88e7-5e727d71c0a8 | -13.8565 | -48.58258 | 2026-09-23 05:06:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c422e947-5ab0-33b5-b7d9-5398ee021a31 | -13.45737 | -46.26559 | 2026-09-23 05:06:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3fdadd5-4a86-3917-94f2-c655ab110078 | -12.06872 | -50.05616 | 2026-09-23 05:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b686836e-6149-3ab2-9e25-c5fbfb5b628f | -14.70614 | -45.59334 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13bbf5d1-dc14-3016-a424-748c35921559 | -10.87471 | -57.17513 | 2026-09-23 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c91caee-c3e0-39b6-85d9-b8be96443676 | -14.60077 | -45.63321 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4c97e177-ad99-3ac6-aab5-955e4757484c | -13.06624 | -47.41045 | 2026-09-23 05:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fe625c78-4fe3-3822-9bd5-4bfa0c20224c | -14.62501 | -45.65244 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfce7b0f-e549-3f8d-b22d-b2e1298d2833 | -13.39376 | -48.03538 | 2026-09-23 05:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2df150d2-97ec-3791-b4a3-7f15f0531702 | -12.41261 | -46.97498 | 2026-09-23 05:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8b3da720-2995-3999-b7c1-5db9399b963b | -14.63408 | -45.62044 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| edd6719b-bcef-3bef-9b13-c16de980842d | -9.34042 | -65.72892 | 2026-09-23 05:06:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ceba3e12-d980-345b-82bd-b7a801d11499 | -13.92754 | -47.83524 | 2026-09-23 05:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75ce368c-8e00-31d0-88b4-5c1b9659cdea | -14.70094 | -45.59247 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f6029fd-3aba-3d7d-8996-9b48808f9a7f | -14.69419 | -45.60439 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6ce35c3-192d-3dec-9e36-a03a85e15645 | -13.05248 | -48.73194 | 2026-09-23 05:06:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 629c7182-4982-32ed-b4b8-de2ae659eff9 | -12.44988 | -48.23761 | 2026-09-23 05:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd935f27-020e-381a-b16c-bf66c5e0a89e | -13.19113 | -51.56636 | 2026-09-23 05:06:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c271ccf9-e5a5-3efe-993e-b3f181ba0314 | -14.70653 | -45.5901 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfdb0274-dda3-3d7c-ab23-1d68f1ad7fbf | -13.92397 | -47.84184 | 2026-09-23 05:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4490c9e6-eb4f-39bb-8811-6d6510e7fcff | -13.2921 | -47.89083 | 2026-09-23 05:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 325ddd00-550d-387f-a3f2-9b9ef3c746c1 | -14.60558 | -45.6371 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 247a4ffa-bbfa-3035-bd90-82e9f62fadbd | -14.70575 | -45.59655 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cf2a808-9199-325b-9ab2-260fdc786588 | -9.33252 | -65.72829 | 2026-09-23 05:06:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fad2b2fa-7110-3d78-af16-77bd9ebdd69c | 2.76911 | -60.27287 | 2026-09-23 05:21:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a8ea8f6-35f3-3309-9e09-873004450980 | 2.07152 | -50.95415 | 2026-09-23 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4803d92-d559-368c-8408-ccb9b785af5a | 4.09975 | -61.00035 | 2026-09-23 05:21:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2011b47e-9d99-30cb-abe0-5b21e18ffce6 | 1.26896 | -50.84293 | 2026-09-23 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b55e245-578e-3057-aeed-2a60b9c4358b | 1.44099 | -50.81306 | 2026-09-23 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b1bdedd-9478-3773-9812-7a32236d1ca9 | 2.77354 | -60.22965 | 2026-09-23 05:21:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c3827d7-8204-39cc-8d9d-45340cc95371 | 1.44169 | -50.8175 | 2026-09-23 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4882028d-3a88-3781-b679-5e10781cc9d6 | 2.73877 | -60.17152 | 2026-09-23 05:21:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a43b95d6-2229-3285-ab16-736b458e5dc2 | 2.08906 | -50.95131 | 2026-09-23 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3848d1ab-9034-3919-b242-bbb1fb6bbd4f | 2.87675 | -60.10101 | 2026-09-23 05:21:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec179d27-6218-3e8c-9288-5bca42ecde43 | 2.77714 | -60.22909 | 2026-09-23 05:21:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53c910dd-8205-3a4d-bf1f-bae2a3685b35 | 2.06851 | -50.96331 | 2026-09-23 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 50fbbc6d-7d20-3c2a-b6d3-392dd840a708 | 3.6781 | -61.86547 | 2026-09-23 05:21:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 99ec01e5-b4a9-3e2f-92e6-77667a0c7ccf | 2.08974 | -50.95555 | 2026-09-23 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb8c3266-f650-3b9f-87a9-7df138d17b3f | 2.06482 | -50.96827 | 2026-09-23 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b65a4ccc-c343-359b-aff5-209ac35ccb46 | 3.67408 | -61.86615 | 2026-09-23 05:21:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41097e02-6696-31bb-92fa-78670e704596 | 2.0759 | -50.95342 | 2026-09-23 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3f390dd-4ce4-3dab-9003-666e0010e1f7 | 1.27488 | -50.85111 | 2026-09-23 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfa82983-fb6e-3c2d-815a-a53a391d3f58 | 2.06413 | -50.96401 | 2026-09-23 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 25880a80-ded4-3b97-9d04-3deda2fb800d | 2.33411 | -50.76709 | 2026-09-23 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 17.2 |
| a3dc0a1b-1458-397e-99f2-b4715d91552a | 2.78075 | -60.22853 | 2026-09-23 05:21:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb0a98ca-37e6-3e93-8d3b-3de51debed87 | 2.78011 | -60.2244 | 2026-09-23 05:21:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b714356e-e9a4-3881-b607-f993afc61881 | 1.44388 | -50.81401 | 2026-09-23 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64802310-9798-3048-b9f7-2f786e256ee9 | 2.77273 | -60.27229 | 2026-09-23 05:21:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c522423-4073-34ef-ba00-3e944bbf71ae | 4.30782 | -59.94601 | 2026-09-23 05:21:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53df1c33-bf0b-3655-aca8-e306267e988e | 2.46752 | -50.97405 | 2026-09-23 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b639e58-38b3-3460-b897-a1803b135a20 | 2.76784 | -60.26457 | 2026-09-23 05:21:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3e2c2dc-7634-3b8f-a428-dd5109e8e27b | 1.28007 | -50.85485 | 2026-09-23 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d05ddf8e-9fdb-3ae6-ac42-28c693d37728 | 2.77145 | -60.26401 | 2026-09-23 05:21:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8774025-7b49-3a24-9ece-612ee6329ce4 | 1.43862 | -50.82708 | 2026-09-23 05:21:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63757f4c-87be-312d-9e62-30d4c91abfaf | -3.03936 | -50.27069 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5658367c-9642-3cb4-a819-b2c51e3cda27 | 1.91122 | -60.58207 | 2026-09-23 05:23:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1853d245-e553-3a78-9bbf-38341414f711 | -3.14323 | -60.63067 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9988d292-975e-3042-a4de-477708da0772 | -3.90562 | -60.59775 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| acd4768c-0d2c-329c-8158-617273b9f38c | -2.95273 | -54.08472 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13280dd7-82f9-3683-a849-a68e53bb4b0e | -9.15192 | -61.18723 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51abf00e-4b67-3898-8216-81471d4ba0c8 | -8.21091 | -56.08797 | 2026-09-23 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ccad72a7-6807-3989-b22a-358440599e37 | -3.70958 | -60.55254 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b88b7b3-cdc8-3ef3-8b01-d8378564fda3 | -3.68001 | -60.60527 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23d5c237-4dd5-3f35-ba38-b4e524fb5081 | -9.55889 | -66.01211 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 680e323e-450f-3854-b177-b3b8b5eb2294 | -9.70756 | -58.13354 | 2026-09-23 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7de8b9b8-a9bc-33ba-a6f8-f49116920b75 | -10.30469 | -50.49385 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 53923246-5a0a-33f7-b996-f5b11cc0461e | -2.76578 | -57.03617 | 2026-09-23 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 39165d71-f046-326b-ade0-eb6dc2f64729 | -3.39286 | -61.06305 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 754b0c09-a1e7-3d62-874e-cb85a7be4fbe | -3.24232 | -53.95177 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42a2d451-1676-322b-b232-018635394ff3 | -10.29329 | -50.49598 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6a5b2384-a337-36bf-83f4-ed4d49719ec6 | -11.13064 | -49.45375 | 2026-09-23 05:23:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bc830b6-4479-32ec-9f1d-c228aa1cdda9 | -10.27559 | -49.97273 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 989c19c6-e9f9-3ef9-a0da-d97934ef40a3 | -11.7872 | -50.97417 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16bf4517-503c-3a2d-87f9-7c27bf125790 | -3.81796 | -52.40001 | 2026-09-23 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3b7907f-3739-3956-a4d2-a964a7d64986 | -4.04687 | -58.92315 | 2026-09-23 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 162962eb-5bc6-33d5-a7d0-c5c82262de60 | -3.58253 | -59.06568 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b4010a5-912b-3dd7-8077-0cd33b517362 | -3.28473 | -57.85624 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cff40598-9a12-33b1-8224-54bd02cb6f6a | -10.29171 | -50.54988 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdb19c8d-97bb-3a65-9f1d-2de307036d07 | -3.62704 | -49.99313 | 2026-09-23 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3c66c37-17a4-3f7e-912f-ad70c706ef0f | -2.97017 | -50.39164 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c855f63-67db-37d8-94cd-8bbef8cc7e35 | -4.51382 | -59.80732 | 2026-09-23 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d76deb6-0f8e-3c31-9457-08a70516167c | -3.38631 | -61.28553 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c73136e6-3202-3391-96ac-69ed22197799 | -11.67492 | -50.88865 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d307fce-f6ec-3f88-9013-b6f25f28afe1 | -8.18362 | -61.18754 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad0d0be9-eaba-31ce-96d0-d87b6a0d9c8c | -3.75591 | -59.40691 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 055a23f1-f6e7-3465-9e00-6befbf0d8083 | -3.14262 | -60.63446 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb97ed28-a386-3c53-8058-a701f64e945e | -10.29716 | -50.55059 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d294f0e7-589b-3511-b0ee-815df94bfcba | -3.277 | -57.86213 | 2026-09-23 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b5ea38c-a281-31df-82a9-824a6a2620ff | -9.4771 | -67.15036 | 2026-09-23 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| febfd2d1-2918-3817-af92-47d358585006 | -1.21592 | -54.55565 | 2026-09-23 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3921e753-ee0b-33bc-9b0e-5e2325c7145f | -4.04644 | -56.31681 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb900fce-0aff-379d-af13-10cc97c19640 | -10.29296 | -50.54967 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72f8814b-885a-331a-8ae9-943f9f6d5182 | -10.30108 | -50.52911 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60bea0c4-d6ca-30fc-8274-da6700bf693c | -8.17964 | -61.19063 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef3e1198-7de9-359c-a46a-90180ecc2172 | -8.20485 | -62.90236 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 90a9ea50-ee45-3c3c-a2d2-297ead639d11 | -3.81939 | -59.00775 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2ba2089-43ec-3e44-b2e2-31ef82ef3f6c | -10.03748 | -50.2187 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README100.md)
