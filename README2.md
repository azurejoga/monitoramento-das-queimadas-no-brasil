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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08b25375-524c-357a-9ab9-21778a2d56ee | -4.426 | -48.9251 | 2025-11-05 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 00807aff-b2b2-321a-8599-3092defd8a7f | -5.4555 | -45.3763 | 2025-11-05 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 856be621-c4c8-3005-8e4f-f36ed9ab912d | -4.482 | -43.2141 | 2025-11-05 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 337.7 |
| 4ce8958b-4a3c-3e35-a514-de35af3e0c21 | -11.2948 | -44.6275 | 2025-11-05 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 326.7 |
| 2fe92d53-4573-388c-b488-0c3ca3f5445e | -4.4635 | -43.1919 | 2025-11-05 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 8e1f3797-70d4-33fa-bad9-d320220b7b40 | -4.4073 | -48.9474 | 2025-11-05 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 5db4798c-9b0a-3c3b-921a-db8895b8a895 | -11.3144 | -44.6014 | 2025-11-05 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e0c2dc8b-5377-35f3-87b3-5026231348af | -3.4714 | -43.616 | 2025-11-05 00:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 237.6 |
| e65b1a92-f52a-3d0d-89c0-5bab6a21b7c5 | -11.2952 | -44.6042 | 2025-11-05 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 641.7 |
| c9079cd1-ea71-376f-9fc5-787b0eff1500 | -1.3006 | -49.1677 | 2025-11-05 00:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| a6a72dc0-e84e-3bad-9c7a-a50bd30e66b2 | -10.3833 | -44.3826 | 2025-11-05 00:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 135.1 |
| c8e6740e-80c6-39dc-b701-b5c01e774449 | -4.2789 | -45.6709 | 2025-11-05 00:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 208.5 |
| 771c70a3-6005-3aaa-9fd0-26689ca45248 | -3.4899 | -43.6383 | 2025-11-05 00:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1045.2 |
| 003e2272-e769-3abb-8185-a43e28591310 | -4.4819 | -43.2374 | 2025-11-05 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 396.8 |
| 1e6eef1e-6936-3652-929e-0593dda15306 | -3.4712 | -43.6392 | 2025-11-05 00:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 341.7 |
| 8e0c6ea4-cbe3-3bd5-ac13-ca10ecf2af29 | -4.2975 | -45.67 | 2025-11-05 00:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 9e7d0cc9-60e4-315f-9645-09d2d63a77a5 | -4.4259 | -48.9465 | 2025-11-05 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 5d919792-2d32-3ee8-bd18-eecbcd723c03 | -18.5117 | -53.5071 | 2025-11-05 00:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 84.5 |
| a63002c5-3e20-363d-a7b3-977ae1ce5675 | -3.5085 | -43.6374 | 2025-11-05 00:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 0fd4fa2c-7f2e-3e5c-8e14-31f425097b8b | -3.49 | -43.6152 | 2025-11-05 00:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 822.5 |
| ad3650bd-6ecb-365b-a507-f27d4599e6c4 | -5.4551 | -45.4214 | 2025-11-05 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 5793f481-7fd4-364b-9553-4db1f803829a | -2.6508 | -48.52 | 2025-11-05 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 86ed9645-7fa8-3bd0-b492-e9f5b5f6a927 | -2.7922 | -50.2986 | 2025-11-05 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 06c3109f-7c5a-3a89-bf58-ab82da2bc341 | -4.4633 | -43.2152 | 2025-11-05 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 486.2 |
| d9acea63-51f8-361d-bfcf-190c95935fb0 | -10.2768 | -36.3057 | 2025-11-05 00:30:00 | GOES-19 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 148.2 |
| 26d4362c-17de-3f0d-9aa7-32d50318149f | -4.4445 | -43.2397 | 2025-11-05 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 92eee378-1339-33c4-8ef2-490438d5d7ee | -3.4714 | -43.616 | 2025-11-05 00:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 208.0 |
| 4d3a9c02-dc2c-3eb3-b95b-3db167ea1960 | -4.4635 | -43.1919 | 2025-11-05 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| ea933e43-e660-3246-aad0-52abf3bd99e3 | -4.4632 | -43.2386 | 2025-11-05 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 442.2 |
| b9306d90-9222-353c-9030-6eee31783d16 | -3.4898 | -43.6614 | 2025-11-05 00:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 7a64cb48-5134-3976-a689-1a2756231656 | -4.426 | -48.9251 | 2025-11-05 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| d1062f75-caa0-3d09-978f-354734e2afa4 | -4.2789 | -45.6709 | 2025-11-05 00:30:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 256.5 |
| 6da77d17-ad18-3ddf-9b3d-910db3d18d4e | -2.7921 | -50.3196 | 2025-11-05 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 750b9695-5f28-35c2-abef-b70485241802 | -4.279 | -45.6485 | 2025-11-05 00:30:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 173.7 |
| 58742397-9352-3749-823b-18ce0d7eb213 | -4.482 | -43.2141 | 2025-11-05 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 263.7 |
| 19ec9831-cc42-3da1-b974-89969daf6593 | -8.2335 | -49.98 | 2025-11-05 00:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| fa38edd8-e1a5-386f-80d1-3230a0bd6b6e | -3.5085 | -43.6374 | 2025-11-05 00:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 4aeaae64-7f6c-395b-a092-5ccdd455e779 | -3.2317 | -46.8716 | 2025-11-05 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 2fc7d14a-ec17-3ceb-8568-239a47cb37d3 | -5.4551 | -45.4214 | 2025-11-05 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 73e5de7b-2394-368f-a3a4-e45882c322f8 | -3.49 | -43.6152 | 2025-11-05 00:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 552.1 |
| 0afbd5e0-3ac9-3658-9a37-7a157dbfee33 | -11.8473 | -43.7256 | 2025-11-05 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| df22c6ea-6e3f-3f67-b588-f76ba59e451d | -3.4899 | -43.6383 | 2025-11-05 00:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 777.5 |
| 1c360a90-aec2-3881-84eb-21e574df77e4 | -4.4259 | -48.9465 | 2025-11-05 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 6f479a9b-983e-3dca-954b-f1663beb77c6 | -3.5087 | -43.6143 | 2025-11-05 00:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 309599b1-d1a9-34ec-a02f-f853ccd97894 | -4.2975 | -45.67 | 2025-11-05 00:30:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 5b23fb98-90cf-3697-8c42-234ef8ede9d3 | -3.4711 | -43.6623 | 2025-11-05 00:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 6a2abc66-309a-30e5-b34d-634e82e37438 | -9.9205 | -44.8124 | 2025-11-05 00:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 3fd30f42-d46c-3e3f-bd08-3361ec5b534a | -4.4819 | -43.2374 | 2025-11-05 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 346.2 |
| d91cafc5-3b8a-335e-8738-7d51178569ec | -5.4553 | -45.3988 | 2025-11-05 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 300.4 |
| b4efd2ec-915d-35ad-b122-7fc92dbd7e1b | -4.2977 | -45.6475 | 2025-11-05 00:30:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 82.2 |
| df622856-ec72-3b33-9ecc-aa5d3a9b77e0 | -1.3006 | -49.1677 | 2025-11-05 00:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 8a539a51-83e0-32e3-88e3-e5b163c9c193 | -4.4446 | -43.2164 | 2025-11-05 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 138.2 |
| df5542e6-9c0c-310c-9f70-8df4a5f24828 | -4.4073 | -48.9474 | 2025-11-05 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 819d28e4-8ea1-3c4d-9f2b-0c69ebccce0d | -1.2822 | -49.168 | 2025-11-05 00:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 45e2918a-50ee-3189-a5df-912091389e87 | -3.4712 | -43.6392 | 2025-11-05 00:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 314.3 |
| fd145814-312d-3f29-9d8d-d0f63d43871c | -3.4899 | -43.6383 | 2025-11-05 00:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 672.1 |
| 8cd8699c-1707-33ed-8850-f29ba767ff45 | -4.279 | -45.6485 | 2025-11-05 00:40:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 159.8 |
| fb61e09f-5568-38dd-921c-32c2f6c4d78f | -5.4366 | -45.4001 | 2025-11-05 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| e0db16a9-a74b-306c-b7e0-27effc2d1180 | -2.6509 | -48.4985 | 2025-11-05 00:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 58744519-5891-379d-aef0-d453a4bde552 | -4.2789 | -45.6709 | 2025-11-05 00:40:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 251.6 |
| e9b708a6-9a4c-39c1-a1f9-55bbad5bdc7b | -3.2317 | -46.8716 | 2025-11-05 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 85b04e3c-d774-3d45-b81d-141382059a72 | -5.4553 | -45.3988 | 2025-11-05 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 377.2 |
| 8cf41156-f951-3b76-985e-23205b0ee9ce | -2.6508 | -48.52 | 2025-11-05 00:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 6a9514c3-67be-3265-94a7-7dcba0de2ad9 | -3.4712 | -43.6392 | 2025-11-05 00:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 271.8 |
| f686581d-65a2-3b4e-b76a-c69b7d287451 | -5.4551 | -45.4214 | 2025-11-05 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| cff3a5e7-035f-3962-a38e-7ef9990bbab4 | -3.49 | -43.6152 | 2025-11-05 00:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 374.9 |
| f7eef175-d335-3d7c-9ff0-1bd6c0bcd7fc | -1.3006 | -49.1677 | 2025-11-05 00:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 5c779eab-3fee-314e-b050-83d02dce4fa6 | -4.4445 | -43.2397 | 2025-11-05 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 70844ec2-cb7b-31c1-806a-7139871fdc49 | -4.4632 | -43.2386 | 2025-11-05 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 421.0 |
| a35f3a64-1d8c-332d-a339-1d1c7c620b15 | -4.4073 | -48.9474 | 2025-11-05 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 7cb26228-3526-3d57-a043-992bfa2288f4 | -7.2891 | -45.4589 | 2025-11-05 00:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 10c198e2-a250-30d2-a963-8541a5395887 | -4.2896 | -46.936 | 2025-11-05 00:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 1164d71f-68a1-3f1c-899a-3314eafaec28 | -4.4258 | -48.9679 | 2025-11-05 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 2ee04fae-5b0b-3d9a-87e3-660fee58f9f5 | -3.4714 | -43.616 | 2025-11-05 00:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 52516bcb-c891-3f78-9cbd-8c06d39873fb | -4.426 | -48.9251 | 2025-11-05 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| f53570ad-f7e6-3628-98b9-f2a77f6e02d1 | -4.4446 | -43.2164 | 2025-11-05 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 22eb128b-85fa-38d4-a5d1-6b66d6d5277d | -3.5085 | -43.6374 | 2025-11-05 00:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| f6fdcec4-643f-31b7-afe6-2159d739637a | -1.2822 | -49.168 | 2025-11-05 00:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| bbd6bea9-51d4-3daa-a846-496eac0beebc | -4.4633 | -43.2152 | 2025-11-05 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 515.7 |
| 265d80c7-ac10-3efa-ad6f-a76050395b34 | -4.2977 | -45.6475 | 2025-11-05 00:40:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 5b489e3f-4232-34a7-a2f9-16ee974aa918 | -4.4819 | -43.2374 | 2025-11-05 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 355.6 |
| a19acf62-3955-3442-bbb7-3fe43b70e15d | -4.4259 | -48.9465 | 2025-11-05 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| c1a5f998-6d61-315f-a827-65c33a4b82d8 | -2.7921 | -50.3196 | 2025-11-05 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 1ba189b3-ff79-30d0-8a76-500df2bdc342 | -4.482 | -43.2141 | 2025-11-05 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 227.6 |
| d53758af-1e06-3567-ab80-0a435b82cbce | -9.687 | -35.9242 | 2025-11-05 00:40:00 | GOES-19 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.5 |
| ad7d64d9-03ee-3f99-a561-54a1a2036c9b | -4.4075 | -48.926 | 2025-11-05 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 9b9b645e-4055-34f9-bd69-ef9e44629e36 | -11.8473 | -43.7256 | 2025-11-05 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 8d521e35-7cef-3b1d-ad0f-a5c9f31b9d8c | -4.2975 | -45.67 | 2025-11-05 00:40:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 108.1 |
| d2012f3d-8279-3600-8732-5799866b1132 | -4.4259 | -48.9465 | 2025-11-05 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| fb0fec83-1987-3496-9f4e-ca3fc1853229 | -3.2317 | -46.8716 | 2025-11-05 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 69a3bab6-f415-305a-80c2-fb4d051ddf67 | -5.4551 | -45.4214 | 2025-11-05 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 66fde136-11a8-3e35-9b93-3337e63714d4 | -4.482 | -43.2141 | 2025-11-05 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 244.9 |
| b501655b-41de-33f7-9aaf-97b381085741 | -4.4819 | -43.2374 | 2025-11-05 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 285.9 |
| e64654a0-540a-30cb-9a39-c203131a7e6e | -4.4632 | -43.2386 | 2025-11-05 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 344.9 |
| 97759122-9193-3521-b3d3-1f7b924b9a2a | -3.2316 | -46.8936 | 2025-11-05 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 63d6da8e-89bc-3f88-b9b8-73ab2679135a | -2.7921 | -50.3196 | 2025-11-05 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| b0c93db8-f1c9-35c6-b484-76dfa6501a0d | -3.49 | -43.6152 | 2025-11-05 00:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 339.7 |
| 14a82ece-efb7-38b6-90c5-6892631e4210 | -5.4553 | -45.3988 | 2025-11-05 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 315.7 |
| 32730cd8-58e3-3ac2-b7ea-3bb306966ec8 | -4.4633 | -43.2152 | 2025-11-05 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 464.8 |
| 8b09a2f7-58a1-3b9f-8cfb-d5c23bb20e54 | -3.4899 | -43.6383 | 2025-11-05 00:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 447.3 |


[Clique aqui para ver as próximas entradas](README3.md)
