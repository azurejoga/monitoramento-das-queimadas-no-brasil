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
| 20a97ea6-6b80-39ab-ac1d-7c6ab7fab212 | -18.5277 | -56.8161 | 2026-07-21 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.2 |
| 31019906-6476-3426-aba4-8881d0494f50 | -18.5472 | -56.8343 | 2026-07-21 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.5 |
| 4ea7fdaa-1b60-39ca-a3ca-49e4d7c5f30e | -13.3023 | -45.1511 | 2026-07-21 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 83a37cc3-6136-317d-83ac-8d8e570c4374 | -17.8614 | -50.5053 | 2026-07-21 02:20:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 39.3 |
| dc132672-b5f9-346f-a8b0-bdf27eb641d7 | -18.5476 | -56.8135 | 2026-07-21 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 337.1 |
| e873d974-6ef3-3954-b0b3-68448f4956e8 | -19.6142 | -47.6443 | 2026-07-21 02:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 3d01d10a-4e61-3087-bded-4f02324d9d0e | -18.5671 | -56.8317 | 2026-07-21 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.4 |
| d22f8f84-cd4c-3c16-9816-089de4a3d063 | -13.3221 | -45.1246 | 2026-07-21 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 316.7 |
| 37196fa5-478e-3e54-89e7-7997f9b87954 | -13.3028 | -45.1278 | 2026-07-21 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 211.6 |
| 3873f672-d4c9-3963-9289-c0a34aee97fb | -13.3217 | -45.1479 | 2026-07-21 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 228.9 |
| 77f69294-0eeb-3013-af11-78d08af41c17 | -8.7497 | -49.0782 | 2026-07-21 02:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| aeacedb1-5331-3468-9cb5-ef7c5717cb5a | -13.3028 | -45.1278 | 2026-07-21 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 299.0 |
| e4659ace-5bff-3a47-b335-bb10dd873176 | -13.3221 | -45.1246 | 2026-07-21 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 224.3 |
| 5a354cb1-cb0d-3ae7-9358-533371df4b07 | -18.5671 | -56.8317 | 2026-07-21 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 1792fa98-fa8a-319c-b115-9934e7941097 | -13.3217 | -45.1479 | 2026-07-21 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 06e05fb4-8d75-35f9-945e-a5c1afba2002 | -19.6142 | -47.6443 | 2026-07-21 02:30:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 38.4 |
| ea3b4db2-ddd5-36a5-9f5c-f86344f01a17 | -13.3023 | -45.1511 | 2026-07-21 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 208.4 |
| a6f37675-95d0-3af7-bb91-5fc4867b4363 | -18.5675 | -56.8109 | 2026-07-21 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 186.4 |
| db51e1b0-33dd-3bb6-adcd-57416d835af4 | -18.5476 | -56.8135 | 2026-07-21 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 311.3 |
| a336da35-a63a-31f8-bb04-db6a529469a2 | -18.5277 | -56.8161 | 2026-07-21 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.2 |
| aa568590-db2a-3b72-acbe-4e6e1a5959c6 | -18.5472 | -56.8343 | 2026-07-21 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.0 |
| b953b880-8763-319e-b0c3-78e105f51d93 | -13.3221 | -45.1246 | 2026-07-21 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 276.8 |
| 66687f2a-dc50-3389-9d19-5ab8e8348465 | -13.3217 | -45.1479 | 2026-07-21 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 173.8 |
| d32b6905-e16b-3160-aa02-2b3af046b1f2 | -18.5675 | -56.8109 | 2026-07-21 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 67ab88b3-ea25-3402-adf4-156c746c3e9d | -13.3023 | -45.1511 | 2026-07-21 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 156.8 |
| d9c199fd-20e9-35a8-a619-c1ace9d2f595 | -18.5476 | -56.8135 | 2026-07-21 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 356.3 |
| 2833f79c-b8c3-3801-99c9-cc4dc1cfc6b4 | -13.3028 | -45.1278 | 2026-07-21 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 244.8 |
| e4bfe433-c6b9-3eac-b656-03910071f7fa | -18.5472 | -56.8343 | 2026-07-21 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 186.3 |
| 70ed57dc-d15c-34ac-8d65-3cc8e8aa4057 | -18.5671 | -56.8317 | 2026-07-21 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.4 |
| b2b7c9fc-c1b7-3025-8145-c4d40a9c7071 | -18.5476 | -56.8135 | 2026-07-21 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 324.2 |
| abbecfa0-8a89-3bb3-8a31-6804cdf9d606 | -13.3217 | -45.1479 | 2026-07-21 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 169.6 |
| d21eb08c-dab9-30c8-a119-c6d7a7cd4abd | -13.3226 | -45.1013 | 2026-07-21 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 334aef35-c2e5-33a3-902e-c83af93443c5 | -13.3023 | -45.1511 | 2026-07-21 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 160.6 |
| b409a46b-b917-3881-ac0e-7223981755db | -13.3032 | -45.1045 | 2026-07-21 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 38e1d5e1-839e-3647-81d8-21d8159b7b81 | -13.3221 | -45.1246 | 2026-07-21 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 309.3 |
| 911f114c-b211-327b-a092-f8244c1fb0b1 | -13.3028 | -45.1278 | 2026-07-21 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 290.0 |
| e67c9c16-68cd-3d27-a6fe-df80af718bab | -18.5472 | -56.8343 | 2026-07-21 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.8 |
| 03c634c4-287c-3964-90c7-96375830719b | -18.5675 | -56.8109 | 2026-07-21 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.1 |
| dd9e8bf4-aafc-3214-9498-dd0c8e0c4fa7 | -13.3028 | -45.1278 | 2026-07-21 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 303.6 |
| df09cee3-3cbd-3154-b17e-d002cc90157e | -13.3023 | -45.1511 | 2026-07-21 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| e9b84098-d00b-36ee-af03-b7a978c3f423 | -13.3032 | -45.1045 | 2026-07-21 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 26d2a657-d4e2-3118-b836-f53877c9404f | -18.5476 | -56.8135 | 2026-07-21 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 276.2 |
| b10ba51b-3a16-3f06-8ca7-d99977d4681c | -13.3217 | -45.1479 | 2026-07-21 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 0cbc8fe5-481c-3aab-a321-862cf3701b66 | -18.5675 | -56.8109 | 2026-07-21 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 2e11bcf2-bb56-37b7-9ec6-81ab5885802c | -18.5472 | -56.8343 | 2026-07-21 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 163.8 |
| 4ad2b05f-56d9-361a-a91f-8f8721685f9c | -13.3221 | -45.1246 | 2026-07-21 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 263.7 |
| 5cae582f-f2c4-3bc8-9223-7e1eb4fc11ff | -13.3028 | -45.1278 | 2026-07-21 03:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 291.5 |
| f1984be8-a9c5-3b6a-ad7a-5fc003fd491b | -18.5675 | -56.8109 | 2026-07-21 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.9 |
| cf711511-c40c-3122-9f5f-0e9dfdf4c79e | -13.3217 | -45.1479 | 2026-07-21 03:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 5f0e9a08-72f8-3ff3-8740-7ab4d6c53e75 | -18.5476 | -56.8135 | 2026-07-21 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 253.3 |
| 6eeb17e4-c39c-3abb-a697-279d3a645afd | -13.3221 | -45.1246 | 2026-07-21 03:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 319.3 |
| 584c4088-f014-38a7-8035-9cdd4163f4b9 | -18.5472 | -56.8343 | 2026-07-21 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 138.5 |
| 529ace0f-da90-395b-8ce3-1f3ae64b4978 | -13.3023 | -45.1511 | 2026-07-21 03:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 9cfd215c-508f-36b9-a334-0b2c3c6fa9d7 | -13.3 | -45.14 | 2026-07-21 03:15:00 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 679d1cfb-9a39-32d4-98a8-8ee3f6cf7e83 | -13.33 | -45.15 | 2026-07-21 03:15:00 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76df25e4-6ccd-3227-ad5c-c5f6597024fb | -13.3217 | -45.1479 | 2026-07-21 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 5fd6329e-7783-3125-ab2e-a78b56cdd56a | -18.5476 | -56.8135 | 2026-07-21 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 296.9 |
| bb4b8892-8bb5-39ef-805c-8aa1cb272191 | -17.8609 | -50.5275 | 2026-07-21 03:20:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 8e443d62-59ff-3520-b6e7-f4ceb8426722 | -13.3028 | -45.1278 | 2026-07-21 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 322.2 |
| 3183885d-90ab-3879-9e70-9365a68bf290 | -13.3023 | -45.1511 | 2026-07-21 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| cebb665c-a514-35d8-8b38-435a1b0a2334 | -18.5472 | -56.8343 | 2026-07-21 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.5 |
| 4facc99c-0eda-37a3-b090-86e900f4d01e | -17.8614 | -50.5053 | 2026-07-21 03:20:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 2377967e-0155-37a7-b2fc-b3203f19ff69 | -13.3032 | -45.1045 | 2026-07-21 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| d64fb737-bc28-3ece-81e1-d6f74428cef7 | -18.5675 | -56.8109 | 2026-07-21 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.1 |
| 487ebbbd-6f89-3d68-99e2-b74dd92919a6 | -13.3221 | -45.1246 | 2026-07-21 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 191.3 |
| 4ecb3460-0c31-3c5a-8687-6c5587bf2e5b | -22.23597 | -42.5429 | 2026-07-21 03:25:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 3deac1f5-5d65-3d3d-9cbb-1717882326da | -23.29574 | -46.16431 | 2026-07-21 03:25:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5f8959cb-0672-39b8-9081-1b6c951d8eed | -22.71087 | -43.75229 | 2026-07-21 03:25:00 | NPP-375D | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 179f4ef9-6f54-3d96-8cb7-35930c14f2db | -23.28897 | -46.16207 | 2026-07-21 03:25:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| e87d6c6e-e834-32c9-8af7-df3878094113 | -18.5476 | -56.8135 | 2026-07-21 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 257.9 |
| ce384acc-d6b7-3873-b9e8-9648eb5d6565 | -13.3221 | -45.1246 | 2026-07-21 03:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 254.0 |
| 3d5f7236-4461-3c70-828d-0fb3d5d67f34 | -13.3023 | -45.1511 | 2026-07-21 03:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 5c8f4309-0be5-3a1e-a8c2-c543af9e7590 | -18.5472 | -56.8343 | 2026-07-21 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.7 |
| f24081ca-f3b3-302c-8b87-18015202bf28 | -13.3028 | -45.1278 | 2026-07-21 03:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 307.1 |
| 7006074f-102e-3dfc-97b1-07f467855abb | -17.8614 | -50.5053 | 2026-07-21 03:30:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| fb55bbeb-13db-30fd-b34b-574914b8e572 | -13.3217 | -45.1479 | 2026-07-21 03:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 19a0eda4-d37a-3a46-b945-7a37ea384d0f | -17.8808 | -50.524 | 2026-07-21 03:30:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 1110f748-5676-30e7-a229-d72b30b50fc9 | -17.8609 | -50.5275 | 2026-07-21 03:30:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 581239f0-31d3-37ec-9ca2-a60f44a172a5 | -17.8813 | -50.5018 | 2026-07-21 03:30:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 44ffa0c3-c031-3b54-9863-022449799c66 | -18.5675 | -56.8109 | 2026-07-21 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| ca0d85bf-1c78-3a5c-a788-b8001f1eb63d | -18.5472 | -56.8343 | 2026-07-21 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.6 |
| 38cc1424-9a4c-3c8f-be7c-286fb3796d7f | -18.5671 | -56.8317 | 2026-07-21 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.0 |
| 5ed4505d-df71-3f91-8879-77e7a1f041ef | -13.3217 | -45.1479 | 2026-07-21 03:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 8aaa6001-827f-36f5-a714-a992a6857c88 | -13.3221 | -45.1246 | 2026-07-21 03:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 343.8 |
| 8f11ed8b-9824-32eb-813f-7bb63913085e | -13.3032 | -45.1045 | 2026-07-21 03:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 97757480-64a7-3b16-b371-d863eaeb7512 | -13.3023 | -45.1511 | 2026-07-21 03:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 1ca61eb5-007b-3460-b256-d2f2e01aa370 | -17.8609 | -50.5275 | 2026-07-21 03:40:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 70d815ae-9c98-3bb9-8953-76cbe680a7e4 | -13.3226 | -45.1013 | 2026-07-21 03:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| d76f1e23-85c9-3729-a75c-69da96d47c49 | -18.5675 | -56.8109 | 2026-07-21 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.9 |
| 40fa3907-c5f9-3bf5-842b-2026394283fb | -17.8614 | -50.5053 | 2026-07-21 03:40:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 14b3f131-36c1-3582-8787-173217c4ba9d | -13.3028 | -45.1278 | 2026-07-21 03:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 269.6 |
| dfaa395a-2291-38ff-97d0-ab3ee990877e | -17.8813 | -50.5018 | 2026-07-21 03:40:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 68019b45-6990-3558-a4a7-a9e8c4a734d9 | -18.5476 | -56.8135 | 2026-07-21 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 208.6 |
| 40859f51-b573-32e3-82f5-8d3296f50723 | -5.34126 | -43.17964 | 2026-07-21 03:40:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee24d866-d00f-3974-8228-8e4d4ed12127 | -4.30255 | -42.32767 | 2026-07-21 03:40:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d3c7cd75-cb7a-3b3a-b4f9-6535c625f787 | -3.52027 | -42.70232 | 2026-07-21 03:40:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c79ad24a-c5c6-3d55-a800-93de6e95f97d | -5.73882 | -43.27174 | 2026-07-21 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92927b6b-dbac-3a6a-a13f-036762d4cb28 | -6.84343 | -39.37349 | 2026-07-21 03:40:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f8f2180c-1e8b-3079-aeee-360906046647 | -6.30575 | -43.65475 | 2026-07-21 03:40:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6602b256-9074-3c23-9f49-8ccb185306e3 | -5.66897 | -43.57048 | 2026-07-21 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README4.md)
