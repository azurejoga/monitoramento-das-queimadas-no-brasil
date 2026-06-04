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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 853e734d-c6f3-3598-86f5-0aa857f1590e | -10.4029 | -49.4534 | 2026-06-04 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| a085f604-15aa-3eb5-995f-b18ad9fef5cb | -10.3839 | -49.4554 | 2026-06-04 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| fe35dd79-6535-3624-a9e2-0c65f7e600af | -14.0786 | -53.3832 | 2026-06-04 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| a7b60374-0f29-3b67-a8e7-dbcae2fec85f | -12.2325 | -57.2872 | 2026-06-04 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 8907bc75-1f11-3f6f-8c15-fe4c44234800 | -12.4656 | -58.4612 | 2026-06-04 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 116.1 |
| b9c82845-a1c0-37f8-94b3-67d298b16160 | -3.9867 | -47.9326 | 2026-06-04 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| c359f149-d2b5-3b32-af86-b7f2967d3283 | -14.0919 | -59.3777 | 2026-06-04 00:00:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 46d2b4f0-7ed2-39bb-b899-ce34562a3878 | -12.2327 | -57.2672 | 2026-06-04 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 150.2 |
| f0baf7a0-ae4a-36ea-97d0-afc2c1f54b05 | -11.5502 | -52.7659 | 2026-06-04 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 4cc7890e-9836-3441-8a7e-323f7b9aad90 | -12.2138 | -57.2688 | 2026-06-04 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 148.8 |
| e4b9f608-832c-3e25-8d80-28c1fe52b816 | -4.0053 | -47.9318 | 2026-06-04 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 7bcd260d-266e-3c7b-b036-a252b8c730e8 | -11.5496 | -52.8076 | 2026-06-04 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| c9b7c767-d511-3751-80f3-953d2fcb11f1 | -11.5499 | -52.7867 | 2026-06-04 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 317.5 |
| 1973fa10-e16f-3bd4-a49a-4951a292cf94 | -12.4654 | -58.481 | 2026-06-04 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 37cf6946-7a97-3f68-a446-51f713ea8412 | -11.5309 | -52.7887 | 2026-06-04 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 0014d97f-a5e9-398a-8a81-7d83ea412fa9 | -11.5688 | -52.7848 | 2026-06-04 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| fec9f415-7a00-3858-b417-4342a2444925 | -10.3842 | -49.4338 | 2026-06-04 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 9a311530-758b-38c2-a536-5aac7d1689df | -3.9869 | -47.911 | 2026-06-04 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 32625fcc-a6ae-38df-8564-f3c8997766f8 | -12.2136 | -57.2888 | 2026-06-04 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 198.4 |
| b1675e5f-a34e-3dd8-8af3-13cd598e9281 | -14.0786 | -53.3832 | 2026-06-04 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 60d7819b-04dc-3480-9154-c36068d089a4 | -12.4654 | -58.481 | 2026-06-04 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 39a87618-bcd1-3df8-b95a-7cd686f0f498 | -11.5502 | -52.7659 | 2026-06-04 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| dc634ef0-b150-3892-82b2-cd1c0c215de6 | -12.4656 | -58.4612 | 2026-06-04 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 770e1a8b-b7e1-33c6-ae25-0e5bfba2dd6f | -12.2138 | -57.2688 | 2026-06-04 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 146.9 |
| f283de02-31c4-3f0f-bb5e-4dc5bd68c7ec | -12.2136 | -57.2888 | 2026-06-04 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 173.9 |
| d78a5605-8213-35c3-b465-63c5e1e6338f | -10.3842 | -49.4338 | 2026-06-04 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| c224a703-ab70-3e3e-b3e8-0bbf122e79f7 | -11.5688 | -52.7848 | 2026-06-04 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| b436faf7-c20b-3098-8dff-639611b3a0d1 | -10.3839 | -49.4554 | 2026-06-04 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| a229dd6f-4ab0-3bd8-a88a-560d7e46869d | -12.2327 | -57.2672 | 2026-06-04 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 153.5 |
| 997b70f3-8a94-3d69-a3f9-579dd7edd967 | -11.5496 | -52.8076 | 2026-06-04 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| f11ee9aa-04fc-3193-8498-1a2e64386455 | -14.0919 | -59.3777 | 2026-06-04 00:10:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 106e8230-9fc8-300f-bc42-4a3031967ec8 | -12.2325 | -57.2872 | 2026-06-04 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 131.0 |
| f28ebee8-50fe-377d-bb82-65e6372958f9 | -11.5309 | -52.7887 | 2026-06-04 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 9a0baced-50df-35e6-94a8-1de111e6a455 | -11.5499 | -52.7867 | 2026-06-04 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 243.2 |
| 627f2b37-11e3-32cf-bc70-77bbda7cb95f | -12.2138 | -57.2688 | 2026-06-04 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 263.5 |
| 93c73af5-c571-3c11-98b7-d26dea1aaca2 | -10.3839 | -49.4554 | 2026-06-04 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 7e6cc01e-a10a-356b-b632-f6f92b0aa056 | -14.0919 | -59.3777 | 2026-06-04 00:20:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 38.3 |
| ac53f7ea-83d6-3ae6-b298-1580540c059b | -12.2325 | -57.2872 | 2026-06-04 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 4d9aaff9-01c9-3d5e-b58f-44caa3e8ba34 | -11.5499 | -52.7867 | 2026-06-04 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 299.9 |
| b8a267f4-f1e3-34ac-a1ff-7053051f6bf6 | -12.4656 | -58.4612 | 2026-06-04 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 4dbc6811-ba8a-3ce2-aff4-0c41765bc837 | -11.5688 | -52.7848 | 2026-06-04 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 02df3cd2-c2bd-3dfa-85ba-df273941d17e | -12.2327 | -57.2672 | 2026-06-04 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 230.2 |
| e795ca72-bce5-3079-bd13-d2f0b370a40b | -11.5496 | -52.8076 | 2026-06-04 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 27f5d332-428b-3291-ad90-fdfb231e7bb7 | -11.5309 | -52.7887 | 2026-06-04 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 39cf9808-6f17-3b3e-a2d7-061e7361eead | -12.4654 | -58.481 | 2026-06-04 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| d1178793-fe8a-32d1-abd1-f568e628eafc | -11.5502 | -52.7659 | 2026-06-04 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 2634e908-318f-30c2-bbf2-85db631ed25f | -12.2136 | -57.2888 | 2026-06-04 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 285.0 |
| 1461f11d-35ce-31c4-8ae8-dc90f9b325cf | -11.5548 | -52.784698 | 2026-06-04 00:28:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 56241339-000a-300f-a3eb-910ba508b3b8 | -11.6266 | -55.182201 | 2026-06-04 00:28:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dca286a5-ffd6-30dc-867f-96971a7e105d | -21.2617 | -50.287102 | 2026-06-04 00:28:00 | METOP-B | COROADOS | SÃO PAULO | Brasil | 3512506 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| db990a06-e2b1-3cc5-a55b-92f165fd29d6 | -21.555799 | -48.593399 | 2026-06-04 00:28:00 | METOP-B | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ffad8255-af7f-3e60-9a92-c7153556ae65 | -14.0831 | -53.379299 | 2026-06-04 00:28:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f5411525-2844-3164-9be8-a9246ebe894c | -11.7909 | -52.504299 | 2026-06-04 00:28:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22001aab-e946-3fdf-bf4d-2ade87b67e78 | -10.6709 | -49.688702 | 2026-06-04 00:28:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 673cb22e-e517-323c-9629-319735cbdfb6 | -12.3023 | -47.900799 | 2026-06-04 00:28:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29cdd60c-73cb-338d-8d9b-14bd4c123988 | -10.3845 | -49.436901 | 2026-06-04 00:28:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46a99392-8baf-32a2-80a0-773486bb3750 | -23.0952 | -49.8634 | 2026-06-04 00:28:00 | METOP-B | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 12fd56c8-633f-3dee-b263-2be9f0b30437 | -21.552401 | -48.577999 | 2026-06-04 00:28:00 | METOP-B | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fec25492-88e7-3d0f-9cbd-b55dbb2df750 | -21.5541 | -48.585701 | 2026-06-04 00:28:00 | METOP-B | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1e1eba71-88f4-3253-8ddc-a00afb767e17 | -14.0913 | -59.365002 | 2026-06-04 00:28:00 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2760c497-f83e-3ce2-a6db-2a298298ce3a | -10.6357 | -49.7145 | 2026-06-04 00:28:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3fa3669-ae35-3052-b86e-bc75d42b4a98 | -10.3963 | -49.4431 | 2026-06-04 00:28:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 618d0267-9244-3abd-8655-262753ea1f23 | -12.2381 | -57.262901 | 2026-06-04 00:28:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c06a465-015e-3167-9354-aa285e2d748a | -12.4519 | -58.4632 | 2026-06-04 00:28:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 99c772e1-59bb-3935-bf73-8d58b1e011ed | -12.2066 | -57.258701 | 2026-06-04 00:28:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27e8ac70-e4ad-3c34-ab35-b6b063be32ad | -13.9663 | -53.838299 | 2026-06-04 00:28:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aae386b8-ff51-366c-9d67-6ef62695aadd | -13.968 | -53.845798 | 2026-06-04 00:28:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4cd706f7-db49-37ab-8108-cfd746280f49 | -11.6364 | -55.180099 | 2026-06-04 00:28:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 984c8268-a04b-3bea-b4c6-fc960bac48bc | -16.121901 | -58.492599 | 2026-06-04 00:28:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dd385f0b-781c-3015-b306-194865c17fd8 | -23.430599 | -47.794201 | 2026-06-04 00:28:00 | METOP-B | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fb3cc82b-1e06-3ccf-86ec-8df9d441f142 | -12.4616 | -58.461201 | 2026-06-04 00:28:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6024b202-d9e3-39f9-b38b-c0caba44daee | -12.5631 | -48.341099 | 2026-06-04 00:28:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f6f4876-e419-3a9e-ae9b-bfb65605daa6 | -16.1192 | -58.478401 | 2026-06-04 00:28:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 675ec7ad-b846-3742-a9db-1e0b97557e15 | -5.7132 | -45.0257 | 2026-06-04 00:28:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9164f2a-1e30-3adb-9e2a-0abfcd5a7161 | -12.2262 | -57.254601 | 2026-06-04 00:28:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2fdb3539-c7de-3237-9c3d-48307a3799b4 | -12.4345 | -58.377201 | 2026-06-04 00:28:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f55ffa5a-a505-3095-a25f-1f6df2a041ba | -5.7229 | -45.023399 | 2026-06-04 00:28:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e570a428-2f87-396d-9c2b-e63716118e30 | -11.7562 | -47.056301 | 2026-06-04 00:28:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3cad8f7f-ac25-3cbe-9583-710fa0f67ab8 | -12.2087 | -57.269001 | 2026-06-04 00:28:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0be514c8-5e20-3c01-86d2-299c4adf55ed | -10.3865 | -49.445499 | 2026-06-04 00:28:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2cc27163-083d-3fae-9187-27d61f0745c2 | -16.5977 | -58.223701 | 2026-06-04 00:28:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a41266a6-bef3-366e-88a1-c6566467f52e | -10.5698 | -57.2999 | 2026-06-04 00:28:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35c999b8-3e28-31d4-a8cf-789da2167805 | -11.6347 | -55.172199 | 2026-06-04 00:28:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7cbd496c-fc78-3cf6-845b-6e1da3dd29cc | -12.2283 | -57.2649 | 2026-06-04 00:28:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f394051b-516a-3b32-9044-bc8e1d29ab12 | -11.5517 | -52.770802 | 2026-06-04 00:28:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62e68494-db8a-3aa9-863a-5da71973e5d9 | -12.469 | -58.446899 | 2026-06-04 00:28:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6f0c9ad2-414e-3700-b3a4-57e3b9332846 | -13.9585 | -46.171299 | 2026-06-04 00:28:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 021b4cda-79c5-32bb-b6f1-fd7e2ee99fbc | -9.5283 | -47.751598 | 2026-06-04 00:28:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7cd1803-560c-3c3f-bec7-aa7bfb64c30c | -14.1446 | -58.959801 | 2026-06-04 00:28:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b9ba599d-3462-3a4d-9fe8-9bf1406235c4 | -11.7589 | -47.067501 | 2026-06-04 00:28:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 544694f5-d330-3b80-9752-a1c5a810b058 | -12.1737 | -54.527699 | 2026-06-04 00:28:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44ea17e5-f763-32c3-88fe-e64ce1019a2f | -21.548 | -49.852699 | 2026-06-04 00:28:00 | METOP-B | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7cf3e97c-5e43-34f3-a693-440c1fd19c25 | -11.6065 | -55.328201 | 2026-06-04 00:28:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40605e5c-523d-3735-8def-ec115514ad1c | -11.6048 | -55.320202 | 2026-06-04 00:28:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52fc91c9-50f0-3aa7-bc4b-e4a72c74860a | -12.7376 | -54.190201 | 2026-06-04 00:28:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5c6f734-2a3c-33b9-9b0a-0a8f40134209 | -12.3 | -47.8909 | 2026-06-04 00:28:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec5ec3e9-0774-39df-9865-d28bd1df6f29 | -14.0815 | -53.372002 | 2026-06-04 00:28:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9241b219-e793-316e-a60c-12237012aa21 | -21.549601 | -49.8601 | 2026-06-04 00:28:00 | METOP-B | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a55ba725-4dde-32d7-b09b-64f02d5f589d | -14.0651 | -53.3909 | 2026-06-04 00:28:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 14bcdd96-ea10-3878-8b37-b40fe2eafa77 | -23.132099 | -49.987202 | 2026-06-04 00:28:00 | METOP-B | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README2.md)
