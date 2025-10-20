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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b640655-02c2-3fad-b994-adf480c4233f | -10.49188 | -43.37189 | 2025-10-20 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 781f464b-11c1-328b-a3ee-e14f679a81a1 | -14.18299 | -51.8197 | 2025-10-20 04:14:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1f66201-88de-300d-a8c0-79d8960427c6 | -10.59537 | -48.00475 | 2025-10-20 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c0c31df-2cf7-3092-8a83-73d894e2bb74 | -8.4241 | -44.11636 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7bb3c60-182a-3d75-863b-e57f7969e3fd | -7.85501 | -49.65654 | 2025-10-20 04:14:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e2b29c0-68bf-3a93-bbbc-1705d4ed536a | -8.42905 | -44.12797 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eab3ed1c-06c9-3d29-8261-bdffd9daeaf6 | -14.19667 | -51.53804 | 2025-10-20 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e849007-e888-3d65-9dd5-375b3e5da8aa | -8.43124 | -44.13554 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b06eb4cd-f647-344a-b912-3e8b629f5c97 | -10.75873 | -47.33987 | 2025-10-20 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 697b60d6-87f0-3348-8408-98d4e065db62 | -8.43456 | -44.1361 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 64324bec-9fa3-39f7-9b63-0e620fc0aee5 | -14.38158 | -52.74817 | 2025-10-20 04:14:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ec8df05-1834-3387-afb8-adb97c2e6c30 | -13.56301 | -41.33625 | 2025-10-20 04:14:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 64f6a1a8-00a2-3497-a1e6-a358442ee33b | -11.61022 | -48.53994 | 2025-10-20 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 502afc04-c555-34cd-b620-d0da0afc8aa6 | -10.87211 | -47.44725 | 2025-10-20 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 14d3fcd4-5587-3ab4-a4a6-b1e90827305e | -8.07171 | -48.01644 | 2025-10-20 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8648125b-21cc-3eb0-a856-f1832ff41094 | -11.00413 | -47.93242 | 2025-10-20 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e324cae7-2164-3849-98ae-df45f9e93598 | -10.87138 | -47.45164 | 2025-10-20 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c083736-03c8-3191-9669-cd4b4e6718d9 | -12.85346 | -43.81785 | 2025-10-20 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8e431123-b974-30da-b655-7962fd47eb78 | -8.43453 | -44.1576 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b794ee5c-1db7-36a9-a382-311b1b0ba51a | -10.59234 | -48.00292 | 2025-10-20 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64a1df37-28ea-39f8-af52-cb3f63aad822 | -8.35031 | -47.29686 | 2025-10-20 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fbcdba3-32d0-301f-96fc-6840412c9ff6 | -11.58421 | -49.54394 | 2025-10-20 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 64913d77-ce85-3eb8-832c-bce535d4442b | -10.76747 | -47.33254 | 2025-10-20 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e85428a1-414d-3fa1-b841-06b447afe9e2 | -10.65934 | -47.6347 | 2025-10-20 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e1b02e5-fdce-3c8c-8953-cb4879af230d | -14.17844 | -51.81879 | 2025-10-20 04:14:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a64c40d5-97d8-37e5-b0a1-a1930fe8be20 | -8.42741 | -44.1169 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9cdc77b6-c58b-3037-9dd3-bc789e797ab8 | -8.42466 | -44.11286 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdb8a7d4-ff55-3493-a8fc-5b83b17338dd | -8.4318 | -44.13204 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4ab9a2bd-4e9a-30f2-984a-367849c4ccc6 | -10.52167 | -43.35499 | 2025-10-20 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35a64ed6-fbe8-31c5-9aab-7e29600b4a60 | -8.07564 | -48.01714 | 2025-10-20 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 09dc1913-254c-3b1b-b26c-1e64a6a618dc | -13.01304 | -43.97019 | 2025-10-20 04:14:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04c41a3c-bf75-3a49-8d3c-2bc9bde67f4d | -10.52498 | -43.35553 | 2025-10-20 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f71fe688-d8dc-30d8-bbb2-0afe5f005fc0 | -11.60637 | -48.53926 | 2025-10-20 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7421ee96-931e-3633-a6ec-c2d7c604d007 | -10.15179 | -42.21129 | 2025-10-20 04:14:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ca7ce4b9-c429-35c4-a3a1-6e0bc10d6b54 | -13.01635 | -43.97073 | 2025-10-20 04:14:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5b49a75-86d6-3b8d-a3c4-d7df7af60a3c | -10.89043 | -47.45033 | 2025-10-20 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce732df7-0ad1-3368-94b0-663174e19727 | -10.76674 | -47.33685 | 2025-10-20 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 45467d56-9f7a-316e-b59b-637c70cb709b | -8.42849 | -44.13147 | 2025-10-20 04:14:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c530ea5c-7b79-3219-ae38-17e95b12949c | -9.56981 | -40.33182 | 2025-10-20 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 1119d805-27f5-33e6-a2fc-ac3ca0be6dcd | -8.236 | -46.24813 | 2025-10-20 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 821c06d7-ba8f-3ac2-8a49-387e933823de | -14.1948 | -51.53593 | 2025-10-20 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81c1342e-f67f-3c67-9f5a-860b9e5cc81c | -10.76238 | -47.34051 | 2025-10-20 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38f16ae6-f7d0-3248-b934-bcbcc47094da | -13.5594 | -41.33568 | 2025-10-20 04:14:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9519d84a-b297-3a67-bfcf-21b000a895d3 | -11.01241 | -47.92915 | 2025-10-20 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 596349cf-9a62-3826-a0c1-c90f254307c9 | -14.41197 | -49.32053 | 2025-10-20 04:14:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17cb9891-4ba6-389a-b96a-b8e262234f2b | -8.07087 | -48.02151 | 2025-10-20 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 657eb032-e656-37f2-8dad-9b910472bc43 | -17.68539 | -52.24737 | 2025-10-20 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b7c3140-d36e-36bf-8abe-b8c7e28d6000 | -17.67846 | -52.23603 | 2025-10-20 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 974f97e6-c392-396a-8c53-f37de67425c1 | -16.90394 | -53.02198 | 2025-10-20 04:17:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd23ee2c-fcde-3226-97a0-1d5a54439696 | -27.36382 | -49.98829 | 2025-10-20 04:17:00 | NOAA-20 | POUSO REDONDO | SANTA CATARINA | Brasil | 4213708 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 63297f1a-4557-32ed-8584-7b3f8547705c | -16.80615 | -53.9324 | 2025-10-20 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35c05ce4-24e7-3404-ac3b-944d3b2e32b6 | -17.68282 | -52.23712 | 2025-10-20 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1d3f6b9-6f13-3184-ac04-7c303a50dd6c | -28.01258 | -51.25298 | 2025-10-20 04:17:00 | NOAA-20 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7bb1d6c6-0eda-3804-82bb-d5a633d8239e | -16.37061 | -49.06665 | 2025-10-20 04:17:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92d10de1-2ea4-3aee-8899-84e674722573 | -21.73636 | -43.44524 | 2025-10-20 04:17:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f624d138-3490-3374-9157-b3a80be4fb9f | -18.25988 | -52.89479 | 2025-10-20 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ffad368-22c5-3ec9-ae55-53d36af4477e | -20.60206 | -45.92149 | 2025-10-20 04:17:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3d393639-499a-394f-85c4-611fc00a7e92 | -21.64398 | -48.39576 | 2025-10-20 04:17:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10176b1a-3147-3005-aca4-251a6f17621f | -16.39968 | -54.82664 | 2025-10-20 04:17:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 661c8c5a-e248-305e-92b2-32ab63a910a6 | -16.40042 | -54.82303 | 2025-10-20 04:17:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ff3ef9c-d0d2-3863-ae03-464c3f5e0d01 | -28.01609 | -51.25383 | 2025-10-20 04:17:00 | NOAA-20 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0c62cf86-7489-35a6-a054-08bf9d984e5a | -21.73518 | -43.44319 | 2025-10-20 04:17:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7b2daabd-f181-35c0-b7ee-fde276b800ea | -19.03934 | -49.69527 | 2025-10-20 04:17:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d9c10d22-6ff9-3c6d-bbb3-bd9dd4213cb7 | -16.25027 | -48.54605 | 2025-10-20 04:17:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e911e1a-02a1-3664-8135-0b69e227ab9e | -19.03852 | -49.69986 | 2025-10-20 04:17:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 826d0b00-a742-3778-918a-bae869c7c444 | -22.30376 | -51.50685 | 2025-10-20 04:17:00 | NOAA-20 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cdbebc24-4683-3623-bd37-21bf1d86c633 | -17.68102 | -52.24634 | 2025-10-20 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56837359-194d-3169-ba6c-7318f83db22d | -23.35639 | -54.3443 | 2025-10-20 04:19:00 | NOAA-20 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 518972eb-3af0-30b4-98f2-f6e3c5b2d9f8 | -23.35708 | -54.34504 | 2025-10-20 04:19:00 | NOAA-20 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8e8e3431-f0bc-334b-ae43-7e92ef6cd5d1 | -6.8774 | -43.5919 | 2025-10-20 04:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 699bd7ea-5362-3d75-9734-8d3678061499 | -6.8962 | -43.5902 | 2025-10-20 04:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 8a1c53e2-e533-3b64-94cb-e0443ce84bca | -2.2527 | -51.9108 | 2025-10-20 04:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 6e7b41c5-a58b-36c2-92f3-a68cc45ffb33 | -6.8777 | -43.5686 | 2025-10-20 04:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 281f5d24-6f66-39d3-8d43-7f24e229c298 | -6.8962 | -43.5902 | 2025-10-20 04:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 1cd530a8-c19d-3f45-9455-5650ea96dfd4 | -2.2527 | -51.9108 | 2025-10-20 04:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 20a5dfd8-9d98-3c88-8c07-328f49091453 | -6.8774 | -43.5919 | 2025-10-20 04:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 121.0 |
| c94254e9-2986-3d34-8314-7c1690da8145 | -14.2056 | -51.5273 | 2025-10-20 04:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 26ab2622-1575-3bcf-be64-b630c382c4b0 | -2.2527 | -51.9108 | 2025-10-20 04:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 99b19eed-87fc-3ab0-b6c4-77fd3114d7cc | -6.8962 | -43.5902 | 2025-10-20 04:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 146.4 |
| be2ea534-3359-3838-b6c5-6d16e08b0c10 | -6.8777 | -43.5686 | 2025-10-20 04:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 5d286cba-4b8a-3211-a114-2278a3c88f48 | -6.8965 | -43.5669 | 2025-10-20 04:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c3402fe5-af73-3166-bbda-581b9cccd71d | -6.8774 | -43.5919 | 2025-10-20 04:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 2a459899-ef41-329c-9aa1-1cbcbaf370ee | -14.2056 | -51.5273 | 2025-10-20 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| d3bb82c5-4680-3d63-92a9-a65dcefbe708 | -2.2527 | -51.9108 | 2025-10-20 04:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 39e54e1f-2a5c-30f0-9d17-a488bf1ab542 | -2.2527 | -51.9108 | 2025-10-20 05:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| d6a491f4-44d2-36cc-a14e-4fa9d4e9143a | 0.97088 | -51.15283 | 2025-10-20 05:01:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47d388a8-ec74-3d4c-902f-0503bb2a2178 | 1.70686 | -55.77362 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0f00e31-a0e5-35de-9d4c-a330e2abe2cc | -3.3334 | -50.22141 | 2025-10-20 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0654ef07-0c91-3d76-9335-d3d110a5c8fa | -2.43488 | -48.61522 | 2025-10-20 05:01:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 071f9eb8-b44e-3cbe-9a6a-46f9a83396bb | 1.0045 | -51.13511 | 2025-10-20 05:01:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9469a52d-4f3c-3bc9-854b-b486c8063acd | -2.25619 | -51.91957 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3a7f0d9-dafc-30af-ac6f-bcd0ccbf10bb | -2.91533 | -52.71671 | 2025-10-20 05:01:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3800c6bf-cf07-3da7-8a53-d29bc508e55f | -2.85743 | -50.73896 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea86012f-d4ec-3717-9082-0172efc31138 | 1.70346 | -55.77414 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12f17ff4-cb00-3ba6-8af7-34462e9220fa | 1.82629 | -55.66208 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd8e11ad-39ee-3018-b534-98b1730fd317 | -2.81564 | -54.38108 | 2025-10-20 05:01:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 052ee7e9-4919-341f-9e07-9b2dcc097ba1 | -2.87176 | -50.72188 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c36ee8de-27da-37d8-bd6f-17019d53afa8 | 1.71196 | -55.7616 | 2025-10-20 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cef1c595-326a-3720-a785-9e4cf9b91af8 | -2.25264 | -51.91903 | 2025-10-20 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f996abd5-ce9c-314f-bca2-77e03c4aabe9 | -2.15212 | -56.65387 | 2025-10-20 05:01:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README15.md)
