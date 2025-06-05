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
| 09ad38ed-bddf-3462-b9a6-ae5369aa4766 | -10.29258 | -57.14191 | 2025-06-05 04:34:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a08fb7f2-7ba8-3c63-be0b-dfbf2346888f | -11.44269 | -45.1113 | 2025-06-05 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 855cee1f-ffe9-37f8-bbd5-e9c97190152d | -9.57383 | -48.57062 | 2025-06-05 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fa26b3a-7f94-37ce-9f97-83c0e68d76ea | -12.64841 | -54.12243 | 2025-06-05 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10392cf6-9796-3cda-80cf-13dc3529d20f | -12.38105 | -47.32556 | 2025-06-05 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f77ca6ae-6784-380b-adbe-edc90ee0c086 | -10.49289 | -53.65974 | 2025-06-05 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 978a063c-e4d9-38c9-b1ff-77216950230f | -13.23429 | -47.31195 | 2025-06-05 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a1af662-21c7-321b-a66d-93ce81d28689 | -13.52025 | -56.57028 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 29.7 |
| bd1485c3-c03a-3c31-817a-d817f8b76d53 | -9.5127 | -47.69078 | 2025-06-05 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49075876-a8b8-35a0-b8e9-853bbd81ca76 | -13.50626 | -56.58847 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cce99cfc-2f3b-3215-bcd1-2555e7c79392 | -7.90359 | -50.36462 | 2025-06-05 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 434558bd-2e4e-35a6-9933-00a4ad5c9c90 | -13.53018 | -56.56728 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29246503-9330-3f79-ba82-0a7a26cf286e | -14.73896 | -45.1011 | 2025-06-05 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45ba7fca-db30-3ff2-9d01-0006fdb66abd | -14.15801 | -45.48786 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41c88132-a0d0-396d-a647-fe4def524fdf | -13.51593 | -56.56102 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 41c51d22-8c02-3fc7-88d4-3717500f7ffd | -9.40399 | -48.4151 | 2025-06-05 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1336e3b1-075b-3dc0-9b2e-884a6c844642 | -13.57139 | -44.26526 | 2025-06-05 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c200147b-fb36-358c-b153-4ee5ddf0b8d2 | -13.53382 | -56.57282 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33d29e5b-db3b-30c8-9047-79b5e98c19c2 | -11.7097 | -56.4533 | 2025-06-05 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61bb94b8-9863-3c3b-bac3-ccf4d2e72c26 | -10.69089 | -57.647 | 2025-06-05 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9552d5ad-27ca-3e9b-a684-485b392029a7 | -14.23229 | -45.48423 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a2d71cf4-cc68-3ab8-86f2-cbf2f7b02428 | -7.9042 | -50.36086 | 2025-06-05 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5dcfe1a6-d798-35f0-9ea5-701e3991925f | -13.51295 | -56.55937 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| efbc7589-8ee4-3d7d-bb76-8e25f0b14e2e | -10.67411 | -44.37506 | 2025-06-05 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6538ce13-cf81-3e74-ab11-d457888807af | -7.90823 | -50.35764 | 2025-06-05 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3df768c-f740-31c3-8584-494781556f51 | -10.50078 | -53.66106 | 2025-06-05 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7b7e318b-7608-34e0-bee6-d2b5149a45cc | -11.83657 | -51.29594 | 2025-06-05 04:34:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 523bf34b-a01e-3b81-ab5f-6f13662001e7 | -9.10536 | -48.65165 | 2025-06-05 04:34:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7018cd74-417c-35e8-b035-06b8139e495a | -13.52522 | -56.58723 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2dff47d-3578-3d1c-8f38-a809c43b4999 | -8.947 | -47.30135 | 2025-06-05 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06d39659-d08f-365d-b58d-04463dad739e | -14.22773 | -45.48517 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d2ddf8c-38ac-3c95-8db3-f337d028bc75 | -11.56218 | -47.62247 | 2025-06-05 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81b288f9-7b7a-392f-918c-55f262b39ee9 | -8.46209 | -46.48346 | 2025-06-05 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd977aa1-11ba-3c9d-b86a-0a4fd5a34a65 | -10.7116 | -48.78129 | 2025-06-05 04:34:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c6f4d75-fb66-33df-bf84-dfc450b36fa5 | -13.51923 | -56.55094 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e3c14d1-df53-3fed-9067-2702c589e5da | -13.52288 | -56.55639 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6aa5095f-646e-357a-b602-2a55fbebbf8c | -10.64867 | -49.44026 | 2025-06-05 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fc75922f-2305-3f63-895a-9d74b94a41d0 | -13.52207 | -56.58541 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5df50775-02b0-31b0-b3bf-c63bbabfae50 | -13.51078 | -56.58934 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8964358-a53e-3fe5-ba69-6d418e5f4721 | -13.51508 | -56.56569 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 8aa34485-4078-3b5b-9921-234593445783 | -13.52388 | -56.57585 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 29.7 |
| e5795ca1-00f0-3f65-ae4b-ea8caf1cb941 | -14.22838 | -45.48036 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f16495b-2883-31a6-ba27-d19f2041526b | -11.13323 | -54.22073 | 2025-06-05 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b18bf98c-d926-3ef4-b834-7aac62548390 | -11.83503 | -51.28395 | 2025-06-05 04:34:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6df6ce72-833a-3f12-bbf9-05cb0307475a | -14.23219 | -45.48093 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 99c41184-6c4a-36fd-9ba2-cde7c1cb9335 | -14.22916 | -45.47886 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7fa3420f-4660-3aa0-8c29-4d6cdd8292b5 | -10.29759 | -57.14266 | 2025-06-05 04:34:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bc4275e-fd3c-373d-9f19-9b593d8c0b84 | -11.63323 | -55.38102 | 2025-06-05 04:34:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a6823083-a073-3546-846d-126f25b261f6 | -14.29297 | -47.9915 | 2025-06-05 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74da450c-9d20-3304-97dc-c8b6e9fc6901 | -12.66747 | -58.2154 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ca844406-05f6-3590-a686-ea24623e7431 | -12.67199 | -58.2196 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5c6eac74-fed2-3bf2-b6bd-a45792dd974f | -11.13769 | -53.94737 | 2025-06-05 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d443445-1ea1-3096-a0b3-bceb7208a91c | -9.38858 | -48.40554 | 2025-06-05 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bda421f-04f9-3c39-a497-e979250998d3 | -8.32034 | -47.92258 | 2025-06-05 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e30c1688-9ade-37bd-8cab-e0768a1f6c02 | -8.45186 | -46.48189 | 2025-06-05 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad0590ec-62a1-3a9b-b148-f28264096df0 | -10.76245 | -54.78756 | 2025-06-05 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d0da091-bbda-3ae1-802c-e9feb330e594 | -13.51748 | -56.56018 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| dbef4647-64b7-31ce-b41b-22767145501f | -8.4655 | -46.48397 | 2025-06-05 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8e07aaa-cb46-3546-bafd-0ae9e7b9f265 | -8.72115 | -48.01489 | 2025-06-05 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 258f331b-d5ee-3248-8a0f-6a2385573752 | -11.83847 | -51.28451 | 2025-06-05 04:34:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8211c451-ea17-3580-bebd-8ebf56d54979 | -10.68931 | -48.96706 | 2025-06-05 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cba89d8-483c-38f6-8dcf-e43e51aafc06 | -12.66884 | -58.22016 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 49768019-b795-339f-904d-20f38983635e | -12.66944 | -58.21707 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9fd1a243-2a1a-3024-8cf2-3aa241de127c | -8.31703 | -47.92207 | 2025-06-05 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca9b09db-0392-3442-8d5c-97d34c0f72dd | -11.54322 | -56.4365 | 2025-06-05 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 149ecb51-2515-37e7-b326-1d6a3f382680 | -9.62296 | -49.48986 | 2025-06-05 04:34:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 607e6ac7-9a41-371b-9a15-b3d78dd20a5c | -14.72393 | -45.09387 | 2025-06-05 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b9e0231-90c2-38ce-95cc-2434b24121c6 | -9.71079 | -57.87909 | 2025-06-05 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1862de30-1369-3884-beef-244044389d92 | -13.52582 | -56.55804 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c08af1af-e493-3778-a14e-210cba1fbed4 | -12.65197 | -54.12558 | 2025-06-05 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2eae62fd-7c8d-3e81-a165-94f7e91f1c86 | -12.65324 | -54.11801 | 2025-06-05 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f310a6e6-715d-3673-91cd-46d1d4f00fcd | -9.48263 | -45.45422 | 2025-06-05 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0dee6c0-072c-3679-88ac-fae735f58145 | -10.66951 | -44.3795 | 2025-06-05 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb2942fb-61f2-31e4-9808-9a96737573e5 | -13.5233 | -56.57199 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 4c3299c9-3b30-3df6-b7c0-c74fe52f8c55 | -13.51338 | -56.57507 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 0beea935-8920-3830-b128-00abf60fe6bb | -13.5213 | -56.55721 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf752f67-ca26-3101-a4e5-9784e5c2571a | -14.22468 | -45.48309 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a346228a-f16a-3238-8e95-a0a94ff26ec3 | -13.5266 | -56.58629 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8efa8120-87a2-3d00-addd-765225d2e460 | -13.07033 | -46.74908 | 2025-06-05 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4111c7da-5698-3f7f-aacf-fdba47222623 | -13.09297 | -52.03894 | 2025-06-05 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fdd3594-0672-3332-a026-2af1df3440bc | -13.71336 | -57.47667 | 2025-06-05 04:34:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a84cd306-d1df-3335-9ace-822502791f60 | -10.9442 | -55.33163 | 2025-06-05 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc289220-eb80-3f79-a9bb-1fb2193ea357 | -12.08457 | -54.57649 | 2025-06-05 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 024444bc-b146-3b3f-982a-eedaeb9b09ef | -14.73571 | -45.09547 | 2025-06-05 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e981e25b-9a23-3f1b-9592-85cf1360860e | -13.71714 | -57.48287 | 2025-06-05 04:34:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| da364d5e-3696-3384-809e-edeb36d75d5f | -13.86376 | -44.13137 | 2025-06-05 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 020e229a-b589-36b6-a068-17ce4d4cd61b | -13.53118 | -56.55427 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbcc9fa0-24a3-3616-a6a7-fde782a3e50c | -13.52117 | -56.59021 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e49b97c6-e6dc-3fab-a193-a7fa5bf30178 | -10.65309 | -49.43378 | 2025-06-05 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8ba5e3b7-dbf3-31ef-9018-909543ae2363 | -10.67268 | -44.38507 | 2025-06-05 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc059b27-1df5-3740-8f93-ab45df067929 | -11.62858 | -41.83615 | 2025-06-05 04:34:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 41df9ca3-39a5-3a30-9868-39f4760e3fc5 | -12.7297 | -46.45247 | 2025-06-05 04:34:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e959c2b3-2853-3417-b3b1-4091dba173ef | -13.0709 | -46.74508 | 2025-06-05 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b4081be-cf3f-3b82-8555-4c9a5a89a0a1 | -13.51252 | -56.57978 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2db2979f-3a87-35be-a561-795fce6d7f69 | -13.52298 | -56.58062 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 221b825b-6e5c-39a4-bd5c-8a1ee5bd2f7e | -10.85425 | -46.84776 | 2025-06-05 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50ffc73a-3a7f-3d22-866f-86caf8d4fdd0 | -9.37786 | -48.81992 | 2025-06-05 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0db2df3-c900-30df-9f57-968fc0c77a8a | -14.22457 | -45.47979 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28eb200f-8bfc-30f2-a32f-7e8b8572cca5 | -11.43275 | -45.10041 | 2025-06-05 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f283c12d-ed30-3a11-a38b-ec41f488de46 | -14.23297 | -45.47943 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README9.md)
