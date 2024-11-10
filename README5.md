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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 835591ff-217b-3614-b702-418e0ac3e8aa | -1.5347 | -52.2104 | 2024-11-10 00:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 324.5 |
| 10b215d0-ddb9-3da2-ba12-d063e32622a4 | -3.5064 | -44.0294 | 2024-11-10 00:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 9e593862-4527-32cd-9ef6-3219be183811 | -2.2487 | -47.0561 | 2024-11-10 00:40:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 69caf155-9f30-32b8-82a8-384f8222f744 | -3.619 | -47.3388 | 2024-11-10 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 46cf11a8-d9bd-31b0-8e4b-3a1eed7cab4e | -2.2486 | -47.078 | 2024-11-10 00:40:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| c9a31162-bf5e-393e-87a0-2a563b56238f | -2.2672 | -47.0556 | 2024-11-10 00:40:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| c2cc4a58-ee0c-39d0-8758-28f331cbd70b | -8.3967 | -44.1365 | 2024-11-10 00:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 340c1662-a359-38aa-9ddd-2d66580572ea | -2.9249 | -49.3661 | 2024-11-10 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 52b3cccb-3d0e-3c08-9ef7-c045791a43f3 | -3.5818 | -47.3621 | 2024-11-10 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 81b71c74-482e-3d0c-a3f2-85a7a9fa4f1d | -3.2243 | -53.0727 | 2024-11-10 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 205.5 |
| 236cf027-cbcd-3319-9ef2-96f292a182ef | -8.3964 | -44.1597 | 2024-11-10 00:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 5ce64609-5140-3f71-9da9-d414e85aef0a | -3.525 | -44.0286 | 2024-11-10 00:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| ae050f45-7741-3e8c-9c5e-cfe1acebc447 | -3.9668 | -48.1932 | 2024-11-10 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 9a05974d-4f6f-3af3-be64-317fed75d143 | -2.7586 | -49.371 | 2024-11-10 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 9f815c4a-01a9-3b63-bd19-00083a0b0e49 | -3.9669 | -48.1716 | 2024-11-10 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 187.6 |
| fa10ff2d-a8a3-36a3-8c8a-274c3671c4c4 | -2.9442 | -49.1529 | 2024-11-10 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| c9f3c7c0-71ee-3bb5-abb7-ced1e5721452 | -3.2428 | -53.0519 | 2024-11-10 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| e281335f-b1ca-375d-98dd-25b653893346 | -2.7772 | -49.3492 | 2024-11-10 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 5486ce8c-e4ef-3144-b887-5a12d16227f2 | -3.6003 | -47.3614 | 2024-11-10 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 5fd3fdcd-5b26-36b3-95bb-6a4da4f25215 | -2.2075 | -48.3811 | 2024-11-10 00:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c1c5c907-0f53-3aef-ab77-dd75a51d6e8b | -2.2095 | -47.733 | 2024-11-10 00:40:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 8365d7fd-284f-3a49-bd7a-6d8b5b4737fd | 2.8552 | -60.0853 | 2024-11-10 00:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 0596cc1c-2f7a-33c2-aff7-3367bde5c46e | -2.8337 | -49.0496 | 2024-11-10 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 1ce2334b-abf9-3879-be3f-ebb43d9b0a36 | -1.4925 | -55.4508 | 2024-11-10 00:40:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 9a95d0d5-6f0f-3f59-9100-133bad8fa5ee | -3.9624 | -49.0096 | 2024-11-10 00:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 29c24f88-05be-39ac-a667-d83abd8a4be9 | -3.1239 | -50.4358 | 2024-11-10 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 51e0aee9-241a-3650-a8cc-87e9aca5c6e9 | -2.2671 | -47.0775 | 2024-11-10 00:40:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 8b847282-fe39-34fd-be6f-37d38cc3fe19 | -3.6004 | -47.3395 | 2024-11-10 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 259.2 |
| 31c97bad-e2f0-3503-bbb6-a45bf1bf4663 | -2.0953 | -48.8338 | 2024-11-10 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 2684f7e0-2d0f-3ea7-a137-e79a27fb2adb | -3.3097 | -50.136 | 2024-11-10 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 44316cb4-937e-3c95-bdc4-67d88af72c99 | -4.1112 | -45.7018 | 2024-11-10 00:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 6312c985-5d70-365a-9dad-e36c32fbe962 | -3.1095 | -49.4241 | 2024-11-10 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 0f556e77-2de1-37d9-863f-df329688be46 | -3.2244 | -53.0524 | 2024-11-10 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 225.3 |
| b37982af-0f63-3ecf-b63b-6dbed3a4f599 | -3.4383 | -50.2999 | 2024-11-10 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 665510f4-0fba-38db-968f-f926a1a5c4e2 | -2.6202 | -46.7822 | 2024-11-10 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 68628440-8f6c-3f49-948b-747b5d7968e8 | -2.9355 | -51.482 | 2024-11-10 00:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 24573ed4-197f-332b-9384-128355d8a73d | -2.8803 | -51.4628 | 2024-11-10 00:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| e8288a75-0d3d-3425-a77c-3f6421f4d875 | -17.293 | -57.5062 | 2024-11-10 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.4 |
| 8e4dc300-55e8-32cc-8cd9-1fafc5173e05 | -3.1096 | -49.4029 | 2024-11-10 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| d2b79067-92e1-3ffd-844c-03b27d873e43 | -2.0954 | -48.8125 | 2024-11-10 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| ef0740fc-8b59-3797-9428-caf74a892941 | -2.7587 | -49.3497 | 2024-11-10 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 32e426cc-c494-391a-aad4-96d0699678ae | -4.6922 | -45.153 | 2024-11-10 00:40:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| a2627d55-f5e3-379a-85ec-c31ce4722295 | -2.2487 | -47.0561 | 2024-11-10 00:50:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 2db5090b-a7f5-3430-88a7-d9f9feb3816e | -2.6203 | -46.7602 | 2024-11-10 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 52c2935e-4a31-35a6-88b3-ca8e3380030d | -8.3967 | -44.1365 | 2024-11-10 00:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 58343d29-5dac-3476-8ee8-77f71b118c0e | -3.9485 | -48.1508 | 2024-11-10 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| e334e523-ca61-3bf1-a70d-7ec9debb3c52 | -2.2486 | -47.078 | 2024-11-10 00:50:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 00319afc-cd9f-3ae5-9403-a19308d9a0eb | -3.525 | -44.0286 | 2024-11-10 00:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 84c521c2-6c55-38ec-80e4-5ef78081a008 | -2.2671 | -47.0775 | 2024-11-10 00:50:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| d2da1705-3ff7-32cb-9a2c-406c589ec71e | -3.8413 | -44.1283 | 2024-11-10 00:50:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| cacf54ae-ed7c-352b-a33b-8673d9514262 | -3.5064 | -44.0294 | 2024-11-10 00:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| cf61cdb6-0a10-3a23-870a-606c88b3b848 | -2.8802 | -51.4835 | 2024-11-10 00:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 1231350d-17cf-3ff5-84f5-645fed13bd3c | -3.0213 | -53.2607 | 2024-11-10 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 9bbd1711-e6d8-3582-b2b3-35c5ed7edb80 | -3.2427 | -53.0722 | 2024-11-10 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| e0adfc70-5044-304c-be2e-798c708db4c9 | -3.091 | -49.4247 | 2024-11-10 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| fd701909-0ae1-3986-9a62-939728e3f689 | -3.4383 | -50.2999 | 2024-11-10 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| b9c40369-cc38-31b9-9534-29a11c0dd118 | -4.6736 | -45.1541 | 2024-11-10 00:50:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 9370f020-e865-3270-b57a-1c38363e786d | -3.2352 | -50.2855 | 2024-11-10 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 261.1 |
| fbb0b342-f9e0-3018-9271-a7110c9febdb | -3.2168 | -50.2861 | 2024-11-10 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 244.8 |
| c7c298d9-dc30-36c8-a7a6-e4b6ef6eeb1b | -2.8803 | -51.4628 | 2024-11-10 00:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 5fbf072a-cb9b-3ed5-a7f8-dcb660eedba9 | -3.3117 | -45.6706 | 2024-11-10 00:50:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 2826b0b8-be77-3cbc-a28a-ee4472800fd5 | -3.6003 | -47.3614 | 2024-11-10 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 139.5 |
| c16140b8-ae0f-3b85-8469-2bbc69967bac | -3.9668 | -48.1932 | 2024-11-10 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 2fc78bee-b9e7-3b37-b9f3-cc3e6b58f751 | -3.6004 | -47.3395 | 2024-11-10 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 247.6 |
| e3a3fb0a-983a-3bf0-b6e5-3c3441cd1477 | -2.2672 | -47.0556 | 2024-11-10 00:50:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| fe65f7d5-897b-3676-a4f3-50bcb4ff0a4a | -4.2083 | -48.1176 | 2024-11-10 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| a40fdbda-edae-3ab3-b998-5f6c0ae169f0 | -2.9355 | -51.482 | 2024-11-10 00:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 2dc19620-2c3e-3dd7-8326-8ab402e6f32f | -17.313 | -57.4834 | 2024-11-10 00:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.7 |
| e3f526aa-8f10-3e98-b62c-ededdaec2a09 | -2.2095 | -47.733 | 2024-11-10 00:50:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| bf374d03-8007-39eb-ac5e-eeb2fcc54514 | -10.9419 | -40.8053 | 2024-11-10 00:50:00 | GOES-16 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 0dd6bce7-109b-3dc7-bb88-8c318101b7ce | -3.2167 | -50.3071 | 2024-11-10 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a539949c-675b-38c2-a89d-f62195cb38ac | -2.8618 | -51.484 | 2024-11-10 00:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 30d77406-15b1-34d8-b96f-bfbacfafbe75 | -1.5347 | -52.1899 | 2024-11-10 00:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 5ed490e5-e46e-3e38-bf94-4a811d9a09dd | -3.967 | -48.15 | 2024-11-10 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 9bd47900-8921-3049-bef9-36f5513cf187 | -3.2243 | -53.0727 | 2024-11-10 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 170.4 |
| d6bec117-dded-3271-9082-5894d8f75686 | -3.0911 | -49.4034 | 2024-11-10 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ab56ae0b-9e1d-37e7-889d-1428e6ced9c7 | -3.76 | -52.6695 | 2024-11-10 00:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 3f98ddae-397b-3d72-b46f-e7ebd42c21ce | -2.0954 | -48.8125 | 2024-11-10 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 9a48a844-198a-3676-a894-bf10e4727fc6 | -3.1095 | -49.4241 | 2024-11-10 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| cf5c5228-5584-35bd-881a-3c83d2aca96a | -3.2428 | -53.0519 | 2024-11-10 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 29fad47d-9c80-30ab-b616-2259222d7d86 | -4.1112 | -45.7018 | 2024-11-10 00:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 2b93872d-6bfe-3a11-a890-a6574321ba51 | -1.5163 | -52.2106 | 2024-11-10 00:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| a9016e61-f0b9-3e7a-a3c4-2f3534ed2969 | 2.8552 | -60.0853 | 2024-11-10 00:50:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 45.5 |
| cccaf933-0cc9-3ec3-b675-8245ef70d511 | -3.865 | -49.9477 | 2024-11-10 00:50:00 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 160f9dc2-c174-3239-a0dd-80b06d6ea235 | -1.5163 | -52.1901 | 2024-11-10 00:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 1939a8f8-aa96-3988-b1d6-1b4e74330577 | -2.2076 | -48.3596 | 2024-11-10 00:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ad0626fd-a999-3afb-91e6-4fc0984be778 | -5.0535 | -44.2654 | 2024-11-10 00:50:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| b7274074-ae1c-328a-aa37-329278b7dbc4 | -2.0768 | -48.8342 | 2024-11-10 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 2053e560-4b05-3caa-9ef6-ad943a0ba241 | -17.2933 | -57.4857 | 2024-11-10 00:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 165.2 |
| a2afb500-3f05-3c74-a8af-4c08740a6cb3 | -4.8918 | -48.6018 | 2024-11-10 00:50:00 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| ab2de0b2-e442-3fff-934a-3d3979659a2c | -2.4662 | -48.4391 | 2024-11-10 00:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 7c8e9f06-48f0-3186-82b6-dc99b52e8998 | -4.6922 | -45.153 | 2024-11-10 00:50:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 9157c446-ca15-3318-a06b-7f1112782e3c | -1.5347 | -52.2104 | 2024-11-10 00:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 249.7 |
| 0d4ee617-ee08-3865-ba7a-834ae88ef0f3 | -3.9671 | -48.1283 | 2024-11-10 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 00935b87-86b0-330d-a9bc-22ddc70a7036 | -3.9483 | -48.1724 | 2024-11-10 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 144.8 |
| 0812ebb5-a0a0-31ea-9490-7457fa423948 | -3.9669 | -48.1716 | 2024-11-10 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 184.6 |
| bcb6ecef-7e65-35e7-92a1-72dc735a5488 | -4.6924 | -45.1304 | 2024-11-10 00:50:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 5629dd36-7044-317b-8411-223461b3339e | -3.5249 | -44.0516 | 2024-11-10 00:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 9e39070b-0c1c-3e67-9ab9-641157b91284 | -3.2169 | -50.2651 | 2024-11-10 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 738a80b6-81c3-3b99-9453-7cf3415853b6 | -2.0953 | -48.8338 | 2024-11-10 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |


[Clique aqui para ver as próximas entradas](README6.md)
