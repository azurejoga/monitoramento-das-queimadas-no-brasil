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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57916a5e-9fa3-3917-a65b-fce512498882 | -4.0617 | -47.08671 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13deb7c5-b6b6-3321-a0ba-4ff3642fb542 | -1.72983 | -45.88275 | 2024-12-22 04:25:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2905a75-ec87-33c5-8636-6a4029dfa812 | -3.9883 | -46.73359 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac399056-61cb-3aeb-ada0-b25367703388 | -4.67289 | -44.07405 | 2024-12-22 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d9b9711-2331-3fc0-adb6-ddd18526fe6c | -2.57058 | -49.46702 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0c07b8e-f89c-3c0e-ab68-e16512736fb0 | -3.50628 | -47.19957 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80266ae4-6ce7-3d38-95a3-e4ac24043184 | -3.87766 | -47.02516 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff0af1f3-b3d8-3f06-91ad-28f6d29b8de8 | -4.37523 | -44.57474 | 2024-12-22 04:25:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 627ccee4-af89-3e6e-99d7-6bc6a1fe7a43 | -2.70995 | -46.14302 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71c0cee0-90cd-3a6e-a1b4-272f7ccbb900 | -3.12892 | -46.61698 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edd88b87-9f5e-38be-8ade-db40aeb1e055 | -1.93894 | -45.63429 | 2024-12-22 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1737fdb8-32b7-3780-89a0-24e869e99b44 | -3.22484 | -45.93809 | 2024-12-22 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 50fd8af3-7814-3fb3-ace8-be49d371ce82 | -4.09673 | -46.73674 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d243f75-63ac-31a8-8be6-a8d0699c20ae | -2.50738 | -51.82518 | 2024-12-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5774ba66-0a66-349b-b30e-13c0075eea63 | 0.00093 | -51.19351 | 2024-12-22 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c870d77b-2f7f-36d3-9d7a-320c1e7f71c6 | -2.05504 | -45.48015 | 2024-12-22 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7b470a4b-dc04-326d-b1e5-d4ce78a59082 | -2.19261 | -49.60098 | 2024-12-22 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b18a226-6085-3aab-842c-a10b30420372 | -2.65395 | -46.10891 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfb287a4-e408-374a-b0fd-79b998af5f6e | -3.45676 | -52.86288 | 2024-12-22 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8651ef1-b5ca-3ddd-b2f6-88d38062ea43 | -5.42451 | -40.74784 | 2024-12-22 04:25:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b25b49ae-fad3-3b39-8ac7-c7b5f8b2f681 | -0.92856 | -47.62035 | 2024-12-22 04:25:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99f7c0bf-8345-366c-9b74-c07a54f82315 | -3.67852 | -47.16849 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cde34985-2d61-3f24-88ae-dcba724831d4 | -2.34107 | -45.73946 | 2024-12-22 04:25:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11574fbe-6b7b-307d-a6cf-ed94aa669b4a | -2.65118 | -46.10496 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc3ebe70-bafb-3631-a600-cec667c03929 | -2.68528 | -54.84365 | 2024-12-22 04:25:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe47e7cf-67a4-3138-87f3-7d5b86b90e33 | -2.02072 | -46.6342 | 2024-12-22 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 130a34da-9b38-34b8-922d-f1f8502011a8 | -3.67134 | -44.70714 | 2024-12-22 04:25:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8649c661-84a2-35ce-96da-df362b549a37 | -1.36976 | -53.70493 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 00204bc0-be22-3ea3-b753-08052e1583b9 | -4.82116 | -44.41294 | 2024-12-22 04:25:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7889227b-7b17-34ad-9c66-0369586bb3d7 | -4.07011 | -50.34996 | 2024-12-22 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40f5f5a2-1227-322b-82c6-0e8e7bc88cc0 | -3.98427 | -46.67239 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b8aff60-c6ab-3204-85ed-fd13f4f2d7be | -4.40413 | -46.11956 | 2024-12-22 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72c889a2-bfcc-3460-bb2f-029aa8d462ff | -1.73314 | -45.88326 | 2024-12-22 04:25:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00e5779c-ac19-39b0-a82f-d6b466167aef | -3.78868 | -43.24502 | 2024-12-22 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b32ffd01-add8-3eb7-b092-32e1466903b5 | -4.86649 | -41.3949 | 2024-12-22 04:25:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 273d50ee-ee21-313d-b076-6001e8cb1a14 | -3.10163 | -54.54872 | 2024-12-22 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fa44607-b48e-3aa4-a6fa-847642aef492 | -4.72507 | -43.25407 | 2024-12-22 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 768493a0-a517-3fae-9ad8-170ecb2e58f6 | -3.91237 | -46.67551 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d49fa160-05e8-3836-903f-7d5661a7a051 | -2.89979 | -54.49724 | 2024-12-22 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f876c92c-88c4-34e3-9319-fb465e5ed45d | -3.98759 | -46.67292 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edf204d1-d7b9-30fd-a1c6-bbceef6c0dee | -4.13998 | -46.11372 | 2024-12-22 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 221ba137-285f-3b1e-b98a-5f99fcd088b9 | -1.37026 | -53.70186 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f9242c60-649b-331a-812a-c8aa1eb5182c | -3.17205 | -46.25423 | 2024-12-22 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5375b9dd-2d3b-3b3c-bdb9-56c73886f8cb | -2.55794 | -46.87681 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 205ae58e-13d1-3a2b-bd14-b73ad1c33d46 | -3.50292 | -47.19908 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e7f14c9-dc82-311c-a756-78c07727fab2 | -3.99331 | -46.74508 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 101eaea3-61a3-350e-9a29-f76c9ec273aa | -3.98775 | -46.73708 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 400523b9-e35f-3f40-a3d8-69442f451511 | -2.57738 | -49.47271 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a3b29ef-4592-3bdd-9fb6-967f44699dc4 | -3.14752 | -46.34594 | 2024-12-22 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aab80a0c-f29a-31da-aed9-e7bef1ac866f | -3.76528 | -47.20001 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd3a3d05-cb21-38be-bd4d-108f80184747 | -4.09953 | -45.30266 | 2024-12-22 04:25:00 | NOAA-21 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b67174d-aa78-3512-ac92-4814936fcf3f | -2.77682 | -54.35415 | 2024-12-22 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d0b850bc-fbaa-35ab-8ea9-de06fb7777f0 | -3.36903 | -51.20744 | 2024-12-22 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15eb1c95-d9ee-35b3-9452-612572d40a0f | -1.26126 | -53.51994 | 2024-12-22 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dfa550d-bf3e-3005-954e-e009da039aa8 | -3.83664 | -46.68142 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5ffe12c-6329-3c6f-beac-becada94f54e | -3.8014 | -46.84042 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de1413ba-61a2-3ac0-abdd-c7acfbc70086 | -4.09725 | -46.81903 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78007e15-ff0c-3b24-a1d1-9d3dd55f32a1 | -2.51712 | -48.37384 | 2024-12-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ebd37bd-9860-3836-a9f9-63de254b2592 | -3.92208 | -46.89512 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcb1c4d4-4df0-323f-a6a6-f376bf1dd5c9 | -1.62459 | -45.83818 | 2024-12-22 04:25:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce7f193f-23c5-392b-916a-51f43c83e53e | -3.17215 | -45.97218 | 2024-12-22 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| addc450b-cfe9-341c-8895-ba5d9142873a | -3.83501 | -46.69183 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdb874da-2a15-338d-9044-60bc9f5704ba | -3.80418 | -46.84444 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0618bea1-2327-3038-bcbc-e2311786991e | -3.91695 | -46.36403 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3da6863-5b8f-3119-a5af-7a68cfa3ac74 | -1.2608 | -53.52282 | 2024-12-22 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d5d8fec-5d1f-3217-bd6a-c5ff14497e3f | -3.75298 | -47.1908 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a148b755-7755-3996-a1cc-ccc996e81f6c | -3.93043 | -46.90715 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed8b8cce-de6e-3bbf-ba2f-894cc1cc28db | -1.31233 | -53.52124 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad60299c-ebd2-35aa-8117-01b48d8734a7 | -1.36733 | -53.68816 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d8ecaf4-12fa-33a8-9a3b-ca25ada3668a | -2.22098 | -53.81224 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a17e372-53f1-3b92-ad78-8f408f40f603 | -2.72663 | -46.188 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b551cbe2-eb69-3092-a01e-a6acec841391 | -2.35314 | -45.5973 | 2024-12-22 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4229863b-b401-3149-b865-8b5eff5ad4f5 | -3.17325 | -53.96305 | 2024-12-22 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e81d0aa-a9d1-3572-a99c-f5832fdb4a28 | -3.9094 | -46.99748 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ad5e338-bad4-3e63-bf6f-829acf2a3b4d | -2.5185 | -54.22511 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef3e23e5-a409-31b4-bdc8-435035ad24a9 | -3.91934 | -46.93424 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6e8bde3-956a-3257-b673-16333f433f73 | -4.27695 | -46.67228 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb5e7da6-2d4b-3fe8-b196-ba73b8af0b2f | -4.10005 | -46.73726 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c04515c-9306-3f43-bab0-dabcfc2387be | -2.93224 | -54.30106 | 2024-12-22 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd2048a8-e202-3cc9-90de-7cf9faddf391 | -3.73894 | -43.94248 | 2024-12-22 04:25:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59d0a93f-a198-3ff3-ba98-e5edc1cb0c49 | -4.01779 | -46.9141 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41f2f7f5-c5d8-3721-a4a5-8d972198c072 | -1.74048 | -45.66262 | 2024-12-22 04:25:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| db31d19b-48a6-3636-afe0-38c27dd86382 | -3.77311 | -47.15029 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3155703e-1606-3b34-96c1-f359bba2c182 | -1.36744 | -53.69357 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2c4471d-414c-343f-a426-4bda6a0849b6 | -2.06342 | -52.05671 | 2024-12-22 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c93353c-69cf-3d38-9c9b-01a6daf6977a | -4.08696 | -46.82094 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee048101-b576-34d2-b1e9-c7a8f06ea14b | -3.17054 | -45.98249 | 2024-12-22 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffc35f91-4b79-37a6-9865-398074cda8dd | -1.85201 | -45.62424 | 2024-12-22 04:25:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86041141-2fc4-3a18-9bba-625e9413a871 | -1.29359 | -53.12526 | 2024-12-22 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f8f4ddbc-3b2c-3a13-88cc-e2638300fcf1 | -3.97432 | -46.67084 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32c5b6ba-b8eb-3549-bd66-54ba75a7e86f | -4.03929 | -46.79914 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd7a228e-4d35-318b-a338-29d3fd32657d | -3.26158 | -48.89013 | 2024-12-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d03881f4-abe2-3434-a421-aa1354f5da58 | -1.30737 | -53.48868 | 2024-12-22 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33f5e41c-6f40-3d69-ba66-e5d1d7ae04d1 | -3.76305 | -47.19238 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae89ff40-f127-35d4-a80c-f232f8e32848 | -4.05667 | -47.0968 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62b49ff8-bff7-3b57-b166-73593eb5b4b1 | -3.91712 | -46.92666 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3221573f-2661-3903-a3e7-f907acf62705 | -2.50162 | -49.06937 | 2024-12-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e841dc8-65e8-3cb7-8dcb-fd0262c2e7cb | -3.81093 | -46.54239 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 298a68e7-8f92-35a7-9161-d0cb18bf9844 | -1.15105 | -53.60009 | 2024-12-22 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e7135e2-4431-3761-86aa-b0dcbfe6f74b | -3.92021 | -46.73377 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README4.md)
