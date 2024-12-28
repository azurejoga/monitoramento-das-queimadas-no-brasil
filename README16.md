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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17780bb5-1f20-3d0f-af02-a31eb96ac867 | -4.01617 | -46.56486 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c879e3f4-4579-3ee4-a04f-81802f003200 | -3.69497 | -46.61726 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38f92b0d-0fba-3ca7-9ea4-bc3606536a7e | -4.08744 | -47.10142 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c58a8cd5-c274-3f70-a038-60bd707e1fd3 | -6.39379 | -38.91188 | 2024-12-28 04:38:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7058457c-cd11-30f6-8da1-1593a6dcb5e4 | -3.96678 | -46.67627 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c559129b-8cf1-321e-9992-ba112651fe93 | -3.90582 | -46.98177 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9e925b3-4bf9-35c5-895f-e1f7eca39be3 | -2.52183 | -51.85481 | 2024-12-28 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e0eaba2-f2d5-3b2f-9812-8c49958a4631 | -3.93346 | -46.98588 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cfdabc6-0471-30d1-a688-984df438eea9 | -3.84188 | -45.8587 | 2024-12-28 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64255803-0850-3d52-8998-6fdc82567107 | -2.6846 | -54.03201 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4c33a5ea-fa64-31d6-bbe6-98e42dea9ad3 | -3.84305 | -46.49652 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74fc1cd4-f4a5-3d1c-9edf-af68a32bc8eb | -3.83733 | -46.69365 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc63f3fa-ab62-3286-a98a-c570f834df88 | -3.88673 | -46.95647 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd5412c3-c576-3412-80f2-e867b9c761a7 | -4.084 | -47.10088 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e088df9-71e8-3732-a669-213d2796e293 | -3.9753 | -46.34246 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9dfc2be-b2ff-379c-a5de-66bc872a187f | -4.11805 | -46.72268 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9a955cd-9c52-3a6d-8a9e-edc50863b23f | -3.7214 | -47.18631 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be657db3-46ff-39bf-9644-4ca8d6fd335e | -3.9969 | -46.94186 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7be2c17a-918f-3b63-ae3a-f8832d063de7 | -3.83857 | -46.69305 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e906ec4f-1d78-3474-b897-fdf38ae7eeef | -5.57086 | -46.36087 | 2024-12-28 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a8eaa0f-315b-36ec-957c-32e99cb07e7f | -4.01791 | -46.71569 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 793bef1e-5c70-3d13-9ed8-b54a3280feb5 | -4.1316 | -46.68147 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a5e3317-a628-3b47-a964-551ef1592c77 | -4.02618 | -46.54661 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1b9ae62-3f88-31a1-a280-54f7fd530795 | -6.19844 | -41.56291 | 2024-12-28 04:38:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bc0031eb-ba62-3f6d-a70c-d7a8dfe7136c | -3.84142 | -46.69033 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a238f6f-c234-33b7-96ff-ef107bb5b9d7 | -3.90997 | -46.89848 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15deb6c7-0d61-3ebb-8e8c-5c850ce8a21b | -3.90651 | -46.89793 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ecd10771-001b-399d-9bcd-14f54eacc9c0 | -2.17189 | -45.40808 | 2024-12-28 04:38:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0f65471-87c7-3d1c-80c6-9f59881f386c | -3.84082 | -46.69418 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44a346e4-17e3-35cc-af17-328bd993403e | -2.3298 | -45.80371 | 2024-12-28 04:38:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a6514167-dca8-38d1-9fa1-4abe30b808ef | -3.18235 | -46.12981 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73788be0-598e-3889-b598-62fe30cc5c1e | -3.19243 | -45.99186 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdb649d9-bff9-30f9-a516-ac147dc573d5 | -5.2165 | -41.23727 | 2024-12-28 04:38:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fe644f7d-2a16-39d5-abc2-a5bd87346a7c | -4.01202 | -46.9132 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbc936a3-c530-35ab-a89c-bd50022781ee | -3.72083 | -47.18999 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31b10eb6-e7d5-334c-a7e0-e2997867c74c | -3.93288 | -46.9896 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 294b26e3-290e-387e-b6f7-15b90c3c786c | -1.714 | -46.21183 | 2024-12-28 04:38:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 142b8e43-5896-3ae6-95dc-816ebfecd144 | -4.11635 | -46.71061 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4db87855-dfb8-3338-9e22-88fd6ef83373 | -3.90871 | -46.92912 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a83bc100-e71c-3e2c-be25-ba8367c744b3 | -4.11746 | -46.72653 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abd61b3a-7c2b-3616-8c75-6846d4e331bd | -3.88041 | -46.9516 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d7ebc93-25e9-3002-ad1b-67d04c9347fd | -4.00336 | -46.71739 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dce8a89b-c9e7-3290-bec3-cde9a1cba95e | -5.42715 | -44.82906 | 2024-12-28 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ae1b0fc-3503-326e-8faf-6343522826d9 | -4.04274 | -47.04864 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7394aec4-6db2-3173-8615-4875fe4201eb | -3.7349 | -47.34579 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0aaa99e2-33c5-37f7-8a40-5fc89d0cc538 | -2.17111 | -54.43121 | 2024-12-28 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 09d06ea6-90b5-315d-b26a-131d8f432282 | -4.7356 | -44.64954 | 2024-12-28 04:38:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ddd2b88-ad2f-3ed6-840e-b03237469651 | -2.48892 | -54.17001 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa9510fb-8f48-3349-836e-7e3a5b270618 | -4.23555 | -46.79887 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7186d0b6-c8dd-3670-b176-57d2fbc44645 | -5.21071 | -41.24218 | 2024-12-28 04:38:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1216097d-9e2d-395c-901f-7ec73a544e0c | -3.77079 | -46.82338 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09725b59-b58e-3d40-8c1e-b0ca26a2940c | -3.83339 | -46.67324 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02f4781d-f9e9-33b8-9c8d-901258c9997b | -2.37282 | -53.88078 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7607f844-e4cf-3106-afb9-5f17e094b3cd | -3.96098 | -46.6674 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2a90c56-08aa-3a6c-8e40-24406461783a | -4.73952 | -44.65018 | 2024-12-28 04:38:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3366142-58cc-36a3-bc97-921405de2978 | -3.9077 | -46.89035 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d89f0c6a-4e22-3b44-b008-819e2a7ab88c | -4.56646 | -44.11895 | 2024-12-28 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5a41211e-4439-36cb-bd65-118701764a54 | -4.1044 | -46.81069 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61cef45a-5cdd-35ab-8e84-4dcbfd104ac7 | -2.28907 | -45.56762 | 2024-12-28 04:38:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4096223-f633-3d41-a400-69b6c7ea4473 | -3.96212 | -46.68335 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 688756ed-754c-3477-93fd-0523019b7388 | -3.74536 | -47.19004 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e07928c3-9167-3115-8b34-8a140d3ffa3d | -2.26242 | -53.8794 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cf07d3a-6bc7-3430-a6cf-1a5565784ffa | -3.90011 | -47.01901 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5add1c23-51ea-32f3-bf4a-7275e6481521 | -3.73282 | -47.18054 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a1e2931-ca3f-35b7-9c2b-6714d76a7cf0 | -3.8706 | -46.6705 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e4c0406-e6e3-3af5-9784-b8ae4da21421 | -3.87871 | -46.68748 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56781251-35db-3248-b85c-7b3f807160c1 | -3.89986 | -46.98547 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 58c474ed-f669-350c-99f7-13cef1417945 | -6.39686 | -38.9095 | 2024-12-28 04:38:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d64d7bfc-2370-3640-b84b-5f8bc2a4dde2 | -4.00983 | -46.69869 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffa8438d-e511-3427-976d-9c78ff4d44e4 | -5.24021 | -41.38945 | 2024-12-28 04:38:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0604a5bc-3a81-3efc-bc89-abf2e44e0083 | -3.77647 | -47.19056 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b109842c-b30b-36e0-8688-cb1e51aaf7ae | -4.28105 | -46.83614 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 319de671-b23d-35f4-b27c-e387cc74ccda | -3.91676 | -46.97956 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14b84770-e2ab-301d-95b6-3cb5e72b52a0 | -4.54082 | -46.66882 | 2024-12-28 04:38:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53d4b206-f69d-3f13-bbd1-966c58d79d1c | -3.90065 | -46.99247 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a1c064d-c719-38dd-87c0-316ba8c9f338 | -3.93001 | -46.98535 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e510d4cf-8472-3cef-9bf3-2a4859676cce | -3.90526 | -46.92856 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c52dcba0-738c-3256-9445-05571cabcdb3 | -3.91273 | -46.91344 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bdd9b2ae-5f58-3fe5-bb44-3a4af3eb017b | -3.94285 | -46.76278 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a59ee3f5-98d7-3297-a205-31035e615bbb | -1.15262 | -53.59867 | 2024-12-28 04:38:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92394b39-8912-3d5a-8eac-9c9dd4f804ee | -5.57836 | -46.14019 | 2024-12-28 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30c7b7c4-19c9-370c-8395-a5a0f04da05a | -3.86589 | -47.02205 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8d266427-9e87-3bb7-a726-614247127dbf | -3.87696 | -46.95106 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc168eae-89c0-3244-91a4-c510f149b7f9 | -4.504 | -44.23263 | 2024-12-28 04:38:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45dc1a66-4696-3eed-9935-67fd71fabd38 | -4.0697 | -47.0795 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e02e5aaa-c469-3cb8-ad2c-380a2db0d984 | -4.1141 | -46.67881 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc858c09-2d17-35c6-96a5-fa8505740278 | -3.84658 | -46.49702 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4968bf31-47c5-352d-b229-fb89c52c8ac8 | -3.6676 | -53.83769 | 2024-12-28 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9880b61b-7630-3b81-9dac-7612a47fc521 | -4.01854 | -46.54946 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd43e4e1-2933-35c9-9ef4-ae0b8a309a28 | -3.90701 | -47.02008 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f192875-bc29-3826-bd9b-25a99ea1b1d2 | -4.55918 | -45.98762 | 2024-12-28 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| eeae42b6-9be0-3df3-92a6-99c656a808b4 | -3.76223 | -47.21483 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1083150d-04c1-3ea4-b239-178160768a8d | -5.81602 | -42.81138 | 2024-12-28 04:38:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d939f445-ed26-3c48-897d-10c801f8b1b1 | -3.73909 | -47.1853 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4df616e-1f63-319e-9aea-96975ad92961 | -5.373 | -44.8444 | 2024-12-28 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 689adc70-b443-3870-9618-974969b8b4fb | -3.90821 | -46.90974 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 897316df-da16-3c24-9459-5bd94a542d56 | -3.90365 | -46.8936 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6dd1baf-fdfe-3b41-b306-fa8cdfe3a664 | -3.76737 | -47.22689 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd47755d-2fcc-3052-9684-06d0d14e756c | -3.98426 | -46.67891 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b53ac62-0126-3ee1-af55-fd25d7b5b68a | -2.16684 | -54.4305 | 2024-12-28 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README17.md)
