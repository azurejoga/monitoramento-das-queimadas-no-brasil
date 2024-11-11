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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d7b43ec-32da-3a1b-be49-2eac82caf273 | -2.68491 | -46.81618 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfdcf4f3-6f06-3d9c-a51f-0b251ea7dfb4 | -2.6357 | -49.89781 | 2024-11-11 04:18:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f7f24ef-3ab3-3d0f-92d4-3cba1259d326 | -2.23008 | -46.43684 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 97fbc1cc-e882-3a1d-9fc6-5a3bff67648e | -2.87425 | -46.66362 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10f677e3-f730-3a07-8fc8-902ae261a3fd | -2.87264 | -46.65095 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51458f13-d3b7-3fc2-9195-bbafdf693a00 | -1.50713 | -52.14351 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbbc4522-ecff-3e3b-9ca6-8a84ed47ccb7 | -2.23248 | -48.39674 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| f42f45b1-b647-3669-9e59-760a1ea10b12 | -1.28989 | -48.01118 | 2024-11-11 04:18:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaa65da8-69db-30c1-849c-f591b483d9da | -2.94983 | -52.56996 | 2024-11-11 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b6d51bd-dd4c-3146-90aa-ec39f2a6a517 | -2.57689 | -46.54094 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a301cdd0-16bf-3d9e-80df-9ef124832f56 | -1.54861 | -51.85344 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db39caf5-7456-3db2-8a56-a4c33dcf42d9 | -2.00458 | -46.21991 | 2024-11-11 04:18:00 | NPP-375D | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99cdd95a-85dd-3a18-9066-50e668ad7481 | -4.90649 | -44.65783 | 2024-11-11 04:18:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55782c7f-0abc-3281-8995-f87e7c70b7b8 | -2.28841 | -48.54425 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e14ad6c7-cbef-36a6-83e9-4ea918644cbf | -3.05881 | -53.88854 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17f34b0d-021d-3111-bf3c-36def6a45ebe | -2.73135 | -54.14223 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ac2e53e2-7452-3416-a107-ec9c775c9b8f | -2.0623 | -46.28456 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 890ac08b-7e51-384f-8ab5-21d5ad56f7c2 | -2.31096 | -53.81807 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74c862bf-23a3-3e76-b969-c780e888b867 | -2.68195 | -46.81155 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcd7a246-1a68-3e6a-ada9-47b2a275058f | -3.09205 | -51.07296 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 96c7ff86-c4d6-3abf-922c-569062266c8b | -4.57438 | -47.06638 | 2024-11-11 04:18:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f44df0f-4281-300a-a06e-66330b403765 | -2.4815 | -46.35228 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2918e04d-2097-3464-b690-ae6e8f9b31e0 | -4.56682 | -49.59554 | 2024-11-11 04:18:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6998113-d227-38df-9d73-9a4624e7d17d | -3.35018 | -42.36174 | 2024-11-11 04:18:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f1de2e1e-4646-356f-82c5-99d0dd170f69 | -3.13424 | -45.96799 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7df7aff0-ca42-38c7-b397-1a45e49dfe80 | -2.99828 | -46.93377 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4286278c-6679-3672-8fff-8b90cdd44200 | -1.40487 | -52.38136 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fb894712-6465-355c-b57d-7077a23abc99 | -2.26992 | -48.71082 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b9367db-7717-3566-9b79-92c8a651c627 | -2.67245 | -46.80157 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c325d5b-343a-3d92-9788-c98fa9dc6aa2 | -3.34139 | -51.6582 | 2024-11-11 04:18:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0814c9cd-49fb-3690-a9aa-af74ddf10b2a | -2.66055 | -49.39251 | 2024-11-11 04:18:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf492b10-899e-3712-ad93-ad3ed68fe3d6 | -3.60759 | -44.26587 | 2024-11-11 04:18:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5222b4a9-a3e6-3a9b-affd-93b7199b5057 | -2.26247 | -48.75723 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 92eb48f3-6b7c-35ec-8e38-7115a721b5b3 | -2.26367 | -46.58211 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e32db374-112c-35fa-9726-97548582f145 | -1.81617 | -50.79921 | 2024-11-11 04:18:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae5b084f-3f06-3b3c-992b-030a04f733e3 | -3.11513 | -45.97655 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 780acead-5257-37f3-ab17-405a0f699344 | -2.06462 | -46.3378 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 434ed335-d655-3312-91c9-8560886becf9 | -4.68293 | -46.37209 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f9bedfd-9730-3178-a97b-b84928d552ad | -2.82308 | -46.65268 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd3a510d-dedd-3f92-87a0-80dcf3bc1f60 | -2.7505 | -49.37143 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8243f960-5c2a-389c-90dd-d6a4bdf53df1 | -2.22161 | -48.85449 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d94c63b-8d48-38bb-b064-e016a5af2263 | -4.69519 | -46.4287 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f709b3b-d5e0-3a59-9e71-c77c1b01d33f | -2.87427 | -45.8941 | 2024-11-11 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a452aa7-9cf8-32bd-a725-648c102e3c52 | -2.84543 | -46.62726 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b33d84e6-7717-32a1-8c1e-b5a19e48b9f8 | -3.14522 | -45.96586 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64d52df0-223f-39e7-9f94-e6b94e96911a | -1.5167 | -54.99747 | 2024-11-11 04:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1782e775-08e0-3fc3-92a9-5edf308ea2d9 | -3.09285 | -51.06802 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7e10d26d-2f48-3fc5-b7b3-b7ce86854018 | -2.42614 | -46.68198 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa589d8e-5581-35b4-9331-2e5cf9c19ba6 | -3.78415 | -47.45608 | 2024-11-11 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0262f67-9fdd-3399-ab1a-c281569ccf51 | -2.31096 | -46.46944 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73135313-87f5-3770-ba8d-7b3278632833 | -2.42644 | -48.79487 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dd3ed8d-a669-3aef-846c-a49bde02363f | -2.23329 | -48.39161 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 4fd2bcf9-aeab-38d3-9a45-6c89e4017688 | -2.6413 | -46.78828 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4933ce24-6186-3cf6-8688-43406f7afa38 | -3.121 | -45.96204 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ad4e196-7885-308d-a8e1-fcd23790e04a | -3.29499 | -45.32916 | 2024-11-11 04:18:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22fe6f78-2755-3e0a-8584-7f20e9d0c6e2 | -2.7548 | -49.34427 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5aabfecd-33ef-370e-b434-5e8c6c817198 | -4.71233 | -46.38833 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9fc7ad66-2541-33c6-acfa-18b2c0a21984 | -2.31162 | -53.81407 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7726c1d1-b89a-39cf-a6bb-0a2ca774e109 | -2.25262 | -46.51393 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 15efcd33-9eef-3370-928a-9158fb091110 | -2.75068 | -49.3715 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d029cc2-0577-3d7e-a6c1-e51a961a6ee9 | -2.24613 | -46.50875 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 812bb41f-306c-31a6-8878-f707878292f4 | -2.5962 | -48.19922 | 2024-11-11 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b50dd27f-c80a-38d1-afb7-67ed7e38f4a9 | -2.19831 | -46.4071 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d84fc12-6630-30fd-9b33-28cf0bd39eba | -3.53064 | -54.08939 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0aa0793-07c6-39be-8378-6a05604862d4 | -2.29486 | -46.52468 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50e8e6c5-f333-39e4-a752-10122f43e2f1 | -4.68354 | -46.36832 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dff4927-c7ca-385b-b166-b437853a54ce | -1.62962 | -52.54313 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05d4e7ba-92be-391e-9301-9ab2958804a4 | -2.06154 | -53.41517 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a18e6539-f4d5-34a2-9641-ded5869dcde9 | -3.53201 | -54.08131 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f28e0136-7d9c-3fad-9b18-88e684bbf3ec | -3.24521 | -45.38052 | 2024-11-11 04:18:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2bc4ee85-44bf-3337-a7b3-f288404172e4 | -1.5152 | -55.00679 | 2024-11-11 04:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97221b47-867f-33d8-8b51-b0fa54508b08 | -2.78892 | -45.96196 | 2024-11-11 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a3428d17-7ed6-3c0a-8200-9d09795baab2 | -2.87081 | -45.89355 | 2024-11-11 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33c75201-54ce-325c-b0a3-2c1875420672 | -3.25081 | -46.45858 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78ff2093-a990-343a-bddb-cc33df18ed30 | -0.89036 | -51.78395 | 2024-11-11 04:18:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97578b4d-c27a-3f4d-ab02-413f46c936a9 | -2.75489 | -49.37218 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70ad959d-41f3-3ca5-b1da-cc8259900ed1 | -3.02234 | -47.96563 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 905864a3-60f5-3053-9900-9bfef74bb9d2 | -1.84626 | -46.57961 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4df4394f-6062-3220-8869-8ba147f00b09 | -2.30137 | -46.52985 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 789aefc2-cfd3-384f-bf2a-14870249a558 | -1.93227 | -46.3602 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbddc184-f574-3342-ac65-3885c69af359 | -4.87348 | -45.77477 | 2024-11-11 04:18:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f52546c5-a281-315c-a9fa-8dde86046077 | -4.58737 | -47.07685 | 2024-11-11 04:18:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54163de2-ffb9-318d-b5a4-7138fc8dd20b | -4.70214 | -46.42981 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 828d6a6b-d293-3441-8825-3334cb876192 | -4.51826 | -45.70068 | 2024-11-11 04:18:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e2555be6-30c9-3704-83ed-d81b6d559b4b | -1.54899 | -52.21495 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b306abd-d8f6-39e8-b11e-cdd37a56c925 | -3.24573 | -46.49012 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 387ee3be-d944-351d-90f4-ba5910e72d60 | -3.23743 | -46.54158 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ee9464c-46ff-382d-8428-ed0e263a09a3 | -2.1006 | -46.52479 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 26e557d3-79af-38c6-8a90-174da50fd688 | -2.71271 | -47.72742 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc598509-40d0-36ec-8afa-13d9e3f95ea4 | -2.46174 | -53.69155 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce305e4c-4df6-36ba-b1da-3e848be997e6 | -2.22452 | -48.39544 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0113f44e-e94a-3d17-9c3a-94cad66fd57e | -2.39386 | -46.76976 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42035520-eb30-3aad-a43e-cfffc8bba6f8 | -3.69057 | -45.23998 | 2024-11-11 04:18:00 | NPP-375D | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73cece77-c063-36e1-94c6-5394a25b594a | -2.72553 | -54.14128 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cc4f6b3-fc10-34e5-a9ef-93a9b7fcf385 | -2.28836 | -46.51951 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 496867f3-6683-3eb3-8ace-943e5d4bff1a | -2.99918 | -49.51699 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 902169f0-aa83-3323-84ce-466a125068fc | -2.38863 | -49.39605 | 2024-11-11 04:18:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca36879c-8f8a-3dc6-a50a-4dc15f1a34e2 | -1.40538 | -52.37811 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a47feac3-045a-35ba-91d8-2f53a29a715c | -0.88475 | -51.78614 | 2024-11-11 04:18:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96a1c185-df37-360d-b9c9-c441adc9fdf5 | -2.60168 | -48.21533 | 2024-11-11 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README33.md)
