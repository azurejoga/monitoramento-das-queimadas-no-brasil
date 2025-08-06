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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 195995ce-14b9-34ee-afb2-78476c59f117 | -8.9212 | -60.7681 | 2025-08-06 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 1551d82c-e3ea-31b6-bf9a-941bce36b9bd | -7.8385 | -45.0671 | 2025-08-06 00:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 45a15e45-a2ba-38ef-8468-de4dcc6ed7fe | -8.9028 | -60.7498 | 2025-08-06 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 58a76e92-df8c-3ef6-87c3-456a5a6bd6c3 | -13.0728 | -56.8729 | 2025-08-06 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 25dbb68e-6be0-365b-ad50-2d8ef46d9db3 | -13.0538 | -56.8746 | 2025-08-06 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 9e9be320-b6fe-35fa-98d3-f29c3d84fdce | -16.3268 | -50.3481 | 2025-08-06 00:50:00 | GOES-19 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| b1298481-2bcf-3128-8640-88ee9d17c21e | -16.3465 | -50.3449 | 2025-08-06 00:50:00 | GOES-19 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 56364925-e4f5-34f4-9cb3-2423fa558963 | -7.8194 | -45.0917 | 2025-08-06 00:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 144f172b-9e49-310a-9bf4-fb6b9d82c8b2 | -7.8383 | -45.0899 | 2025-08-06 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| b17120ff-6060-3eb1-89ba-6d47ad3e0f70 | -8.9213 | -60.7489 | 2025-08-06 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 90b66477-60e1-38bb-9458-e95e1b158fa5 | -13.0731 | -56.8527 | 2025-08-06 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| d88428b4-b9cd-3c8c-a720-e7d84c47be53 | -6.9492 | -51.6302 | 2025-08-06 00:50:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| c19242a9-5ae0-3885-91ca-fa9962441d25 | -8.9215 | -60.7297 | 2025-08-06 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| ea9080ad-c348-338a-996c-9562ff6e6bd1 | -6.9492 | -51.6302 | 2025-08-06 01:00:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 70cec726-1a54-32c1-80b3-80760a07c7bf | -13.0728 | -56.8729 | 2025-08-06 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 8ec69dad-bf23-39d3-adb9-4da5d828d48c | -8.9212 | -60.7681 | 2025-08-06 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| b6a71c51-92dc-37c0-ac58-1ca4aa5df2b2 | -13.0731 | -56.8527 | 2025-08-06 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| cd577069-bc1d-3b6f-a154-3281fa226b10 | -7.8383 | -45.0899 | 2025-08-06 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 196.7 |
| 37ad24b6-5c62-3586-8da6-f7eeec1f83c0 | -11.4389 | -45.1385 | 2025-08-06 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 155.8 |
| d7553976-8469-3cfe-8e93-75d259c00848 | -8.9213 | -60.7489 | 2025-08-06 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 48ad23fc-b701-3973-9c26-d177a119c6d6 | -13.054 | -56.8545 | 2025-08-06 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 657ac191-a762-3c04-bdad-ff7c1bbb49a8 | -8.9028 | -60.7498 | 2025-08-06 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| ecf6c7cb-fc57-3cab-8ef2-b133920426ea | -8.9215 | -60.7297 | 2025-08-06 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| df53a7a3-c106-34fb-bbfb-48623932a778 | -13.0538 | -56.8746 | 2025-08-06 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 23357b74-1353-399a-92ad-f9aacf8dd506 | -7.8194 | -45.0917 | 2025-08-06 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| b4d8141a-8799-3e64-8e98-bd310f6376bc | -11.4393 | -45.1154 | 2025-08-06 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 68cfdfed-3b1e-325f-bd4d-8c65f1b4c93d | -7.8385 | -45.0671 | 2025-08-06 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| e80ebd9c-08a9-318b-9ea5-85ab2ebaf06f | -13.0728 | -56.8729 | 2025-08-06 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 6370686f-7695-3a0c-9c82-912755572726 | -13.0538 | -56.8746 | 2025-08-06 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| c3b8cb1d-eb9c-3247-a86a-a3362980e853 | -8.9215 | -60.7297 | 2025-08-06 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 8838f101-9725-3524-9000-0a19c743d50c | -11.4393 | -45.1154 | 2025-08-06 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 9824e87c-eae9-3574-be46-ac8b010cf26c | -6.9492 | -51.6302 | 2025-08-06 01:10:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 0d5c4734-3b9c-3a8a-a670-7f797c5d01b8 | -8.9212 | -60.7681 | 2025-08-06 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 34290063-0a2e-30c9-9093-abbb78663f0c | -13.0731 | -56.8527 | 2025-08-06 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| c16b742c-3b81-3031-a0d6-9003184d0eb5 | -8.9213 | -60.7489 | 2025-08-06 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| d6bc5182-d1e0-3a5f-b478-a07de36e3431 | -8.9028 | -60.7498 | 2025-08-06 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9c53111d-36c4-3625-8028-0241726b35a2 | -11.4389 | -45.1385 | 2025-08-06 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 5698a9a0-e4f4-3bf1-911f-e685f3fab531 | -13.054 | -56.8545 | 2025-08-06 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 15ecc5a4-78e4-36f0-9b23-7113b2d2123e | -12.7576 | -44.402 | 2025-08-06 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| d8de91ce-9c61-3a4a-ada3-091ee9c4c429 | -11.4393 | -45.1154 | 2025-08-06 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 09cba011-6c6f-39f2-8073-21421fdaa542 | -8.9212 | -60.7681 | 2025-08-06 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 91c5df12-1487-3719-9058-955131ac6917 | -13.0538 | -56.8746 | 2025-08-06 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 6d0f2611-13f2-35ac-bc65-7d3b67c444ab | -11.4389 | -45.1385 | 2025-08-06 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 724f2e0d-91bc-3167-a9eb-1107ff220529 | -6.9492 | -51.6302 | 2025-08-06 01:20:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 1f2b54b4-2cd1-3360-a5a8-0e9f238d7969 | -13.0731 | -56.8527 | 2025-08-06 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| d75c7caf-ed23-32d1-8050-73b79f5a5ba2 | -13.0728 | -56.8729 | 2025-08-06 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| bf10ad10-2a61-352d-ba51-566eded3ab73 | -8.9213 | -60.7489 | 2025-08-06 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| d96f01e6-5ca1-3138-82ff-f9440a0ddc6f | -13.0728 | -56.8729 | 2025-08-06 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| c3bc19ed-4adf-38e2-b9a8-e86cba81b7a4 | -13.054 | -56.8545 | 2025-08-06 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 9fc542cd-8b99-3d9b-b7ea-82df5ca35ce3 | -13.0731 | -56.8527 | 2025-08-06 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 11e54bec-b996-3cfe-875c-b1ab9bf88ce8 | -13.0538 | -56.8746 | 2025-08-06 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 5c9932a4-56ae-38f7-bfd4-4ea5d7b4bdc9 | -11.4393 | -45.1154 | 2025-08-06 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 592ea250-72e9-328d-8fed-a80b80645e14 | -6.9492 | -51.6302 | 2025-08-06 01:30:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 50bf9fe0-f36a-3d22-a149-534ea8af7cff | -11.4389 | -45.1385 | 2025-08-06 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| abd96884-a963-3ce5-b76d-b409337ebafd | -13.054 | -56.8545 | 2025-08-06 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 7ec8fd55-282d-3607-9c89-2266a9239d7b | -13.0728 | -56.8729 | 2025-08-06 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| f03eac30-eae5-36e2-91c8-acfd5d8c6c24 | -11.4393 | -45.1154 | 2025-08-06 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 2fcbb32f-2c0d-38d5-afb7-ed75ad17f69d | -13.0731 | -56.8527 | 2025-08-06 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 72f86e36-3f44-3a6c-8672-15b52af5c6f8 | -13.0538 | -56.8746 | 2025-08-06 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 0bce3bad-368f-3256-b3b2-c2ca56efb5ce | -11.4389 | -45.1385 | 2025-08-06 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| d1b69c4c-3518-318d-a8f1-b96da3469186 | -6.9492 | -51.6302 | 2025-08-06 01:40:00 | GOES-19 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| b5268549-a8fb-3181-9d35-aef5b1ee275e | -11.4393 | -45.1154 | 2025-08-06 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 30fb84c7-8958-3888-bd8a-496227de287b | -11.4389 | -45.1385 | 2025-08-06 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 08ab38c7-8652-3111-8a13-185fad90a3ed | -13.0538 | -56.8746 | 2025-08-06 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 41823850-3ac1-3b59-8cc8-63d0023166f5 | -13.0731 | -56.8527 | 2025-08-06 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 68e76368-52f7-3995-8abf-53f21f9ba1d1 | -13.0728 | -56.8729 | 2025-08-06 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| f7412a7a-a912-3d61-8afa-fcb3ee90cd01 | -9.693 | -48.8787 | 2025-08-06 02:00:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 20a77e55-1e80-3c3d-a81e-fe9dbcb379dd | -13.054 | -56.8545 | 2025-08-06 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| f21b78c6-ac5a-311f-b517-901aac162b45 | -13.0728 | -56.8729 | 2025-08-06 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9816da65-2848-3347-bb56-a9386553fb34 | -9.6933 | -48.857 | 2025-08-06 02:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 4994b9a6-ffa0-34dd-87cc-748f14cd1692 | -13.0731 | -56.8527 | 2025-08-06 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 6a4da520-35ef-3ddd-9ab6-53ce68e3772f | -11.4389 | -45.1385 | 2025-08-06 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 245c1e60-4212-3045-8ca9-4c14a6ab247e | -11.4393 | -45.1154 | 2025-08-06 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 03445b77-5aa5-3e16-9dac-b3d7327bf03b | -13.0538 | -56.8746 | 2025-08-06 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| abb02130-fd77-3caa-9926-5a1c14ed08de | -8.91119 | -60.53722 | 2025-08-06 02:06:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 160.6 |
| df0be0d8-0c57-3202-b257-ab5587420cbf | -8.91212 | -60.5298 | 2025-08-06 02:06:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 7f049a22-6768-3218-844d-c02106c58c23 | -9.7119 | -48.8768 | 2025-08-06 02:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 3e26fc36-9e19-31d4-8eb8-7f360a15887b | -9.693 | -48.8787 | 2025-08-06 02:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| b9f7a143-a9d1-35d7-a072-9c278bef0f49 | -13.0728 | -56.8729 | 2025-08-06 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| b797bb56-97aa-386b-adac-f5d4a1b87a96 | -13.0731 | -56.8527 | 2025-08-06 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| f8b0ea54-f5a5-3b1b-b19a-cb8a2770b9eb | -11.4389 | -45.1385 | 2025-08-06 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 186535f6-ab14-3720-a837-4d84e2b479fe | -11.4393 | -45.1154 | 2025-08-06 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 939291d7-7aca-3734-9090-9130e3c0448f | -11.4389 | -45.1385 | 2025-08-06 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 078c9330-aa30-3f01-a7b7-6b130fbb28e4 | -13.0728 | -56.8729 | 2025-08-06 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 5bbde743-4d60-3827-a551-706bbae60dfe | -9.693 | -48.8787 | 2025-08-06 02:20:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 6ce444e2-6fef-3b9a-92d7-a746c3de5394 | -13.054 | -56.8545 | 2025-08-06 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| f748041b-5445-3f59-9370-d8bbedb36ea4 | -11.4393 | -45.1154 | 2025-08-06 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| b25f028b-8bc4-38b1-838e-7c00efbbc03d | -13.0538 | -56.8746 | 2025-08-06 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| c7495ed1-00cc-37a5-973e-41be292f6d62 | -13.0731 | -56.8527 | 2025-08-06 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 4484c5b0-cf39-3333-b770-7c58f8af2ae3 | -11.4389 | -45.1385 | 2025-08-06 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| ab263d60-f17b-3cbb-83a9-281b9608f1fb | -13.0538 | -56.8746 | 2025-08-06 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| f284a909-c1ae-3608-b981-65a483cf1f51 | -13.0728 | -56.8729 | 2025-08-06 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 25fb698f-46ed-3990-b03d-17a61e89ea10 | -13.0731 | -56.8527 | 2025-08-06 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 0fb56bf9-3f43-388f-a199-437066975684 | -11.4393 | -45.1154 | 2025-08-06 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 19380815-ee60-34a1-af4e-a699e853fc81 | -13.0731 | -56.8527 | 2025-08-06 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| ea23f7e5-9b2f-3f19-ab02-65065e7aa744 | -13.054 | -56.8545 | 2025-08-06 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 2a48fdbf-9a9d-3339-b509-a2410daf3b3e | -13.0728 | -56.8729 | 2025-08-06 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b2be308e-42d8-3e4c-afa3-b2d832f12692 | -8.9213 | -60.7489 | 2025-08-06 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.8 |
| d52e008c-6d1c-3cad-8877-98b49f935df0 | -11.4389 | -45.1385 | 2025-08-06 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| bced7aeb-50c8-3efb-9f5e-f1483ffc7f69 | -13.0538 | -56.8746 | 2025-08-06 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |


[Clique aqui para ver as próximas entradas](README5.md)
