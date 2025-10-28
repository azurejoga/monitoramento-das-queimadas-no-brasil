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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 418d86dc-3deb-3ff7-90fd-200d96c30a1f | -8.25144 | -46.89962 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da49d744-5101-36a3-bfae-04e0eab5987c | -8.62727 | -44.79974 | 2025-10-28 05:04:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2f13bb9-da8c-3934-b1fd-3778bbea289c | -7.07147 | -44.94522 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 263836cf-5c2b-3c97-9cf0-b1dfa92c50f0 | -7.95597 | -45.49691 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34e0a290-6642-35cb-9613-a051f776cd87 | -4.99263 | -55.93147 | 2025-10-28 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c742847-bf8f-3a12-ad21-01d8654b1a25 | -9.22043 | -48.60063 | 2025-10-28 05:04:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58b2ba10-d04d-3387-a0f6-ae1a1db20197 | -7.94962 | -45.49997 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a7c6e48-21b5-34d3-a60a-aa12945f1ef1 | -12.69399 | -46.31919 | 2025-10-28 05:04:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28f51f11-1678-3c76-bae5-f093d3a19ddc | -13.36459 | -47.38974 | 2025-10-28 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b18acc13-add2-3e01-b570-e53b02370452 | -7.81093 | -46.45814 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4eb2e650-75b9-3e54-87cf-ddbab779d455 | -9.553 | -46.9756 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3638cf90-30f6-3cc5-a285-e24e8121a469 | -13.24426 | -47.96378 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2285ba31-6e40-3426-90a4-c8831e84b5de | -7.85341 | -46.39862 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7a58c80-7276-3793-8ebb-65d317ed6a67 | -13.53137 | -47.16741 | 2025-10-28 05:04:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d5432ca-6a8b-3ea2-8859-d1003928ba4f | -13.32002 | -48.34669 | 2025-10-28 05:04:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aaa09927-6413-3d0e-b5bf-4764f69ae847 | -11.19413 | -51.03754 | 2025-10-28 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27cf85c2-a0cc-3c85-a249-3352fe2433ee | -10.88677 | -48.63831 | 2025-10-28 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9380e39-d7d8-388a-ad82-d46ebdf16d92 | -8.70933 | -47.98176 | 2025-10-28 05:04:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc9b541f-df20-3cfc-b32d-6341802b248f | -13.44789 | -44.10269 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3446fc58-597a-389f-9619-cce8377a271a | -9.95942 | -47.09187 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e007437d-7117-3dcb-bc6f-6ce69808414b | -7.84038 | -46.41219 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 59679a74-6acc-39db-b568-632de20eb602 | -7.45779 | -47.02676 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94b28eb5-0e9d-3715-a6d3-dcbb5e36b41b | -10.32794 | -47.22977 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3ccbb0f-0706-3965-aa04-70b62f7e46b9 | -8.13805 | -47.75637 | 2025-10-28 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e52a2d59-13b7-3dae-9a20-ed1e695722a8 | -9.58864 | -47.85249 | 2025-10-28 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98a4d3a0-351f-3207-b6d4-bff55cd66d1f | -8.57425 | -47.03196 | 2025-10-28 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1fb67c6-b3df-369a-8a3a-a51a14782a81 | -7.94801 | -45.5123 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35754d05-6827-3a9e-83d8-d209551348e3 | -9.46093 | -47.73104 | 2025-10-28 05:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 625097e0-29d3-3c32-8e2b-3ceb94d36684 | -11.13688 | -47.0493 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3397d7a5-ad8c-36e6-9e6b-94aecc3183b0 | -7.81368 | -46.44473 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e432fc8a-6948-3316-ba87-1646535b4b0e | -9.46153 | -46.88891 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d8d477b-67b0-3e5b-b63d-7241b9b08d1c | -8.18532 | -44.44714 | 2025-10-28 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 789e3b4d-e72a-3d74-b6be-cb2a13079ab8 | -7.97229 | -46.75489 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9c82e2db-d095-3a42-a726-bc68cbb6c467 | -8.11739 | -55.29016 | 2025-10-28 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9968676-def3-3232-95ba-6769926d76df | -10.56361 | -49.80045 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 79eb7d5d-9f49-345a-945d-86670fe45bfc | -10.96828 | -50.26267 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe88ca6a-8eea-395c-987c-62cfd9730a62 | -8.31767 | -46.83545 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c3be3f5-6c41-3871-ab2b-f80aa6c39f64 | -7.94304 | -45.50793 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ad06026-c46a-3ae8-aae0-dd6a017290a9 | -10.36845 | -47.17222 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f76506a2-55e4-3a54-9e81-1aa8b2d40c1a | -9.1997 | -47.19229 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5836143-58dc-3a9e-b878-4b5e78596768 | -12.08565 | -45.67315 | 2025-10-28 05:04:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7eb5bf43-279a-3c28-b90e-bf221ea86ea9 | -10.57097 | -49.80451 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b16a104-1657-301f-87bf-6f14c7ad5b77 | -7.89399 | -45.70045 | 2025-10-28 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5773d86e-4d68-3cc5-b607-738d82984b5c | -10.55605 | -49.77882 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21f880ca-2ce4-3374-846d-8d653853d01c | -7.12599 | -55.11333 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 752054c7-694e-3cfc-ae92-b5d44e897128 | -9.23491 | -45.61449 | 2025-10-28 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97602b84-e5cf-385b-b762-393431aeb94c | -10.55933 | -49.83285 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d6ddbf7f-e46d-31a4-a4be-3cb9e9c0f773 | -10.29547 | -47.18355 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 717647ba-6ca8-33bd-a0bb-19848cdc169c | -7.99301 | -46.19508 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef272b12-74f2-3d35-86b5-7f150cfcc947 | -6.12216 | -52.38942 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6a6337a-6026-33bc-bf68-2ee44e330885 | -7.46578 | -47.16056 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e913cf5-776d-3099-a05a-ebfbeedc89f6 | -7.95112 | -45.53389 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3308e173-84f7-34d6-9f52-791a465660ef | -8.16252 | -46.99538 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e3241c6-2e6a-3a05-9bba-15aaa5658c3e | -13.65483 | -47.63683 | 2025-10-28 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a9295c7-4911-31d6-9e48-addad7148b89 | -7.94189 | -45.51626 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad271272-3e3e-3e6b-bf77-12cc8fcebef8 | -7.96691 | -46.7542 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f5039cc0-ed57-33ce-bbc5-6b102ce8011a | -7.00206 | -46.99455 | 2025-10-28 05:04:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdba4e11-9bf3-32bc-ac66-eb889ddd7986 | -7.39136 | -45.1222 | 2025-10-28 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c53cb9f-b407-3d32-8006-a6fdc40b9870 | -13.25486 | -47.96569 | 2025-10-28 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ecf51ec-278b-3a02-babc-126a94cae840 | -9.93952 | -50.88074 | 2025-10-28 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e822a969-3bb0-3981-bd92-134f6a2319d1 | -8.07398 | -45.95544 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f567ac3-02d7-32b7-b633-6a7cb8d536ea | -10.92564 | -50.28029 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecfc8c44-f300-3fef-975d-ac3617ba9b83 | -10.91163 | -50.25162 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d268f62-622b-3c75-8cb9-203d33a535ad | -12.08282 | -46.39754 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32495688-3d41-30ba-8b36-eb29f79cabf0 | -11.15864 | -47.78378 | 2025-10-28 05:04:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80c711d1-325d-3f32-9b94-ae30ae5fdd48 | -12.08306 | -46.39635 | 2025-10-28 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fdbeeeb-7534-3e98-8dfe-221435356119 | -9.58402 | -49.67424 | 2025-10-28 05:04:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26a57750-891c-36f4-9081-159622d45ee0 | -10.92676 | -50.27021 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ad98532-000b-3498-a62c-f72c2673befa | -7.80703 | -46.48595 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3450ea01-160d-301d-b1de-e3019d45a020 | -7.07031 | -44.95387 | 2025-10-28 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9cbd7d43-a4c1-3e77-9dae-8ec2b696dc1e | -8.18156 | -45.71432 | 2025-10-28 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63f969ba-a2d5-3670-ab04-c0e1e74b9518 | -10.28846 | -47.23856 | 2025-10-28 05:04:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79f70e22-31e2-3bb5-866e-e98bb2aa8033 | -8.14685 | -46.9991 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f784b367-511b-3fab-9a8a-2e1738f9c954 | -8.15724 | -46.99437 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fcfbb02-25c1-3167-aba5-e85279a4e5f6 | -13.32041 | -48.34345 | 2025-10-28 05:04:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccb6ec05-5fe0-304d-8ae4-068c2d04e99c | -10.99546 | -50.35956 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 858c365b-0364-3407-b1ba-42c23d01b9b2 | -7.84136 | -46.40487 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77fabaac-5b27-3ed7-94b1-3c6df9c766a2 | -8.51007 | -54.75047 | 2025-10-28 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57c61a78-d4ed-3b5d-83c1-0f5d33ecc71f | -10.85845 | -48.96324 | 2025-10-28 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de4d6449-dbd2-39be-873d-f4f7889bd8a4 | -7.45585 | -47.15582 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf26215e-003b-39aa-8760-3426a272c121 | -10.85896 | -47.91327 | 2025-10-28 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 457c3b20-954f-3a04-bf0a-b9e1017a92af | -6.97566 | -47.33765 | 2025-10-28 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebb24967-895d-3e4d-b565-a687e053102b | -7.81 | -46.4725 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c58ec3c1-7d6f-3061-9c22-78a82ca3d5a7 | -8.6403 | -45.28004 | 2025-10-28 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4e76ca98-ef8b-31a2-995f-00c8d1b7d076 | -7.50871 | -46.28674 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39004099-6bda-3359-bee6-aa37b67100fa | -8.57469 | -47.02858 | 2025-10-28 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22b3f34e-3d0a-3d59-9656-871fac5dc880 | -7.8132 | -46.44836 | 2025-10-28 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0826cc1b-3f38-3e56-8997-dbf944f6b16b | -12.63405 | -45.08519 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81434c7b-1165-3fed-81ab-9bab9c301f45 | -10.73338 | -49.78359 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 78dd4a65-8251-3ebc-a2d6-f57713cfedd1 | -10.55759 | -49.77594 | 2025-10-28 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 8e053ef1-9c1d-3019-a82f-69584f6c1a57 | -7.40868 | -47.7816 | 2025-10-28 05:04:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9bef103-ade8-35d7-a718-4c4739132486 | -9.97096 | -47.17387 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa84cce0-54f0-379d-bc56-7ff1c0f914f3 | -9.45495 | -46.86586 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c4768eb-e21c-375e-9aa7-2b2424d4f1bf | -9.54396 | -46.95986 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc0ec2aa-bbe9-3955-aa7c-17ed2cd2ad35 | -7.97325 | -46.74804 | 2025-10-28 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d615a316-c951-3bd7-af3a-b65da3585ad5 | -9.4782 | -46.90076 | 2025-10-28 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c148fd5-90ae-38e1-a42f-acbc77ad58ea | -12.55252 | -44.93557 | 2025-10-28 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff280fd2-1909-3a5c-b12a-0b83d76a9454 | -8.70894 | -47.98464 | 2025-10-28 05:04:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 774092b5-0d00-318d-b173-572fbb328007 | -7.96807 | -45.5404 | 2025-10-28 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 776df96c-3e50-3875-be54-c7be7b48f0ef | -7.50918 | -46.28318 | 2025-10-28 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README79.md)
