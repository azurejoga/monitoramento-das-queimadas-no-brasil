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
| 77645afa-f1b1-3b5f-addb-077510beade1 | -4.09681 | -48.26385 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1c5a3776-4826-33f0-b19a-e495c635a7ce | -4.09618 | -48.26774 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 34f37ef5-08d6-3ded-b918-ed75de970cb4 | -4.09448 | -48.25153 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 54b2cf0f-52be-368d-9a4c-6e749d941721 | -4.09009 | -48.27879 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9326360e-ab74-3626-a6ea-9f299de875ae | -3.94343 | -47.96389 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 03189df9-ecd8-3516-962a-65ea01cd5061 | -3.93992 | -47.95951 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e612be7-ff4f-32de-abe7-073aee6300fd | -3.9393 | -47.96323 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bb5f665e-826c-3ae6-8793-c077bae6934d | -3.9367 | -47.96218 | 2024-10-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c6843d4-ae9a-3daa-ba8a-94f8d85fd64c | -3.91398 | -48.34832 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 95d54f65-d7f3-30ac-aa3a-6f55b6e3f9ae | -3.91333 | -48.35231 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f002fff7-94ba-30de-b0b2-87e545ad1aba | -5.06295 | -48.44237 | 2024-10-09 04:14:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67c83530-6c13-3329-990a-a0690c33eeee | -4.89466 | -48.56374 | 2024-10-09 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d7ae5f5-98ff-3dee-aa80-61756d7df1d0 | -4.82445 | -48.09747 | 2024-10-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4da08118-1401-34d3-a170-ff70abc00203 | -4.52182 | -49.07214 | 2024-10-09 04:14:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 534dbeca-f9af-3900-ab60-49589d4d0cc7 | -4.49056 | -48.11908 | 2024-10-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| d4b7f6e0-76a4-36f7-b59a-374b4cb8468c | -4.38007 | -48.70432 | 2024-10-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4124c592-ec71-3457-b9b5-8ce76d6ab817 | -4.37935 | -48.7086 | 2024-10-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 86a2d1b1-90ea-39ad-968a-30c99ac15b61 | -4.28738 | -48.6362 | 2024-10-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6571ba27-e575-32be-a291-f57315fa3c2e | -4.28669 | -48.64031 | 2024-10-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 219b4d9e-d9e9-3356-88f7-ad8ec8999113 | -4.28083 | -48.62263 | 2024-10-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 83f9d4ae-6ec5-3945-a226-4e322b53de81 | -4.10226 | -48.25674 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74109dbb-52f9-37a3-b5f2-c97d45bf7ea4 | -4.10099 | -48.26464 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5e14c500-5da4-30c4-b5ea-42f0ca129f6f | -4.10036 | -48.26855 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07044dfc-466c-3877-8490-08129d2a0891 | -4.09711 | -48.26726 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4449d9a0-b50c-3a42-9ccb-6f301524cd81 | -4.08588 | -48.27813 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 075854ef-8c04-3a01-9eee-e7e7c20f0d97 | -4.0038 | -48.38243 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3942049-34ed-34b7-940a-42f8457fc34e | -3.99956 | -48.38176 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 797339b9-81da-3aa4-9c03-e46ba2e017c3 | -3.91042 | -48.34355 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe06beed-8359-3f2d-bd61-a53361ab40b3 | -3.90976 | -48.34756 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21517055-571a-3773-9413-6560d773fa82 | -3.9091 | -48.35156 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 791d5d17-2c64-3e87-bbbe-10aa89ef08b3 | -3.90685 | -48.33886 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f32144a9-cee5-374c-b812-1ac8a3f8ad27 | -3.9062 | -48.3428 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 616acd44-1e44-3ba1-9c63-ed2f6d22fa95 | -3.90555 | -48.34675 | 2024-10-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a265f943-b5b4-3ded-b1c7-e88fecc8fdea | -6.26559 | -49.06575 | 2024-10-09 04:14:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c39821a-996d-3788-b319-146276fc725b | -6.23468 | -49.45621 | 2024-10-09 04:14:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0beea903-44db-3ecd-86c4-10029cf30f36 | -5.72591 | -48.97599 | 2024-10-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc66fa23-00e4-31de-9ddd-f8763b076e66 | -5.72434 | -48.97575 | 2024-10-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9860b48-4660-31e9-8aae-dc8d1b43a9c2 | -5.71286 | -49.2787 | 2024-10-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1aa1e47e-c204-330b-b2dd-46008ce8d8da | -5.7115 | -49.3134 | 2024-10-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31e3416f-fc20-344d-82b3-09f33fa98a46 | -5.7092 | -49.27372 | 2024-10-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff3bf996-9530-37f1-8b2d-6b0326a01d87 | -5.70848 | -49.27798 | 2024-10-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18a14b11-5d3a-3465-992f-bef4ce144a55 | -5.43525 | -48.32011 | 2024-10-09 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63f6257f-819e-390d-ace9-b86ce1bd1ff9 | -5.43462 | -48.32388 | 2024-10-09 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c73f770-5f95-3b95-86e7-e2f3c536bf0e | -5.85512 | -48.16043 | 2024-10-09 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 28242e03-c275-31e9-a5f2-4b37fc3e1db1 | -5.85485 | -48.15952 | 2024-10-09 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 46441306-caaf-3325-aaea-490de07984b3 | -5.85451 | -48.16403 | 2024-10-09 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be47dd60-281a-3e1a-8c7b-235e10b59340 | -5.85426 | -48.16313 | 2024-10-09 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4c9d3ca4-f10c-3bb1-98bf-57640671e5f7 | -5.85078 | -48.15888 | 2024-10-09 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b55a93cf-499f-3772-a412-123926700bfe | -5.85019 | -48.16251 | 2024-10-09 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da557328-fed7-3748-916f-f375f4f79412 | -5.52816 | -48.36301 | 2024-10-09 04:14:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3f2ace5-f087-346d-8f05-decff3f585b3 | -5.52718 | -48.3436 | 2024-10-09 04:14:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 599f2246-3ee4-3661-9ba9-5ebd4cbc2084 | -5.4633 | -48.27876 | 2024-10-09 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67b7d980-7bb2-3b50-8aa3-d09d31b41e22 | -5.43399 | -48.32766 | 2024-10-09 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5425feae-e40b-3e23-aa7f-a6afbaed4a77 | -7.90639 | -49.26108 | 2024-10-09 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27cf8100-7dff-3762-a6f0-fd6178b27864 | -7.85758 | -49.65037 | 2024-10-09 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7772df9-46df-37bd-b6c9-f271e3d88de5 | -7.45386 | -49.46951 | 2024-10-09 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 700bb775-c61e-3eae-8db7-50292c236d46 | -7.44008 | -49.68344 | 2024-10-09 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8da380e6-ed38-3e34-a304-3a2ac9639d1a | -7.43936 | -49.68774 | 2024-10-09 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e12504ae-a1a0-383e-9c4d-1daaf33030b4 | -7.4357 | -49.6827 | 2024-10-09 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 339806eb-515d-3216-974a-d0a1e9c43e36 | -7.26943 | -49.48659 | 2024-10-09 04:14:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef7ba9b8-9e5d-3fa1-ae58-bc6fb46cad23 | -7.26661 | -49.48627 | 2024-10-09 04:14:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86663459-b603-356f-b3f5-3ce9fe635337 | -7.26509 | -49.48585 | 2024-10-09 04:14:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c61d628-05c7-39e4-89b8-0d49d441c4ec | -7.11936 | -49.86386 | 2024-10-09 04:14:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdcdac73-c556-3f80-8ef5-41f08f667d08 | -7.11489 | -49.86317 | 2024-10-09 04:14:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb4f2c04-82b5-34f9-9d1f-751703de0316 | -7.01581 | -48.54422 | 2024-10-09 04:14:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88b6a9db-7029-3449-8a86-e528cfbd268e | -7.01172 | -48.54356 | 2024-10-09 04:14:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e12c8d25-29a9-38a8-8938-d5aa52b8110b | -6.57578 | -49.66109 | 2024-10-09 04:14:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7667b9c0-5d98-3e34-909f-df1d12cf3e12 | -6.57496 | -49.66051 | 2024-10-09 04:14:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| acbb05bc-d831-3c8f-97df-350288b391e2 | -2.97994 | -49.52491 | 2024-10-09 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9a5fcc3-30cf-3243-b3f4-aff57c0d2415 | -8.52849 | -48.77686 | 2024-10-09 04:14:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef52be9d-3f8c-3986-821a-22226fc848a4 | -8.52442 | -48.77623 | 2024-10-09 04:14:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0731c04c-ddc1-31d4-ac31-dec2a2fb853b | -8.50175 | -48.6428 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ac22f00-806a-3f2e-9d39-e97cb766e954 | -8.50115 | -48.64628 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f218775c-648c-3af1-88ef-d4162e13de16 | -8.49714 | -48.64556 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 23ef10e9-0325-3a62-ba46-2367faf8daa8 | -8.49653 | -48.64904 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 13.9 |
| eb89b04c-ce20-3765-b933-f2787d8c0cad | -8.49649 | -48.64162 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 52fbbb82-8faa-38fd-a0fb-489098a64a90 | -8.49592 | -48.64506 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 9d23dcce-c91d-3dbd-a681-d07f9c38c3be | -8.49534 | -48.64855 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f4306bb8-3fb0-3dc2-857c-e9034ef39842 | -8.49475 | -48.65205 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 16faffd9-4fcf-327d-b785-32e574fde9dd | -8.49372 | -48.64144 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 25.0 |
| b03b4473-cfc3-37bb-b022-76dc778afff2 | -8.49312 | -48.64489 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 6eabb299-352b-3a7a-89fb-d6b0b44f77b2 | -8.49251 | -48.64837 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 082fb4cc-7342-31f4-b330-094697998c85 | -8.49247 | -48.64094 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 18.6 |
| a3eb6411-ad1d-3630-ada8-c08980857c86 | -8.49189 | -48.64441 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 18.6 |
| ec48f5f0-e567-348e-ade3-cbe346ebd42f | -8.49131 | -48.6479 | 2024-10-09 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 9.4 |
| cc3cb70e-a284-3a8a-ae76-c93a24d729ad | -8.3412 | -49.66146 | 2024-10-09 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e7ba256-b59b-30a7-98be-90dee9db13bf | -8.3032 | -49.23167 | 2024-10-09 04:14:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cadd9ab7-c685-3c35-95cd-69af272bb289 | -8.30252 | -49.23555 | 2024-10-09 04:14:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 654156cb-b8fa-399d-9321-ac7031656164 | -8.13877 | -49.37748 | 2024-10-09 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c29892a-da86-396b-ba00-06212c2f2f64 | -8.0725 | -49.66387 | 2024-10-09 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48e3612e-122e-37f5-94ed-97461def8cdc | -8.07179 | -49.66801 | 2024-10-09 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2592ea5e-0165-3a2a-98b1-73656f63ec2c | -8.06818 | -49.66309 | 2024-10-09 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc297cc6-b0c7-371e-85f4-d37c545fadc7 | -8.06746 | -49.66729 | 2024-10-09 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f644dcb4-dc1b-3cab-89f9-059eea0042ab | -8.03861 | -49.70533 | 2024-10-09 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 360fc0a5-623c-36cb-9cf9-53cbe0238d0e | -3.50117 | -50.27269 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aacda6a7-d34d-36d5-9d83-d16c53d05ee6 | -3.40901 | -50.32817 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e8f9adf7-81ae-3a99-8565-5496998799f3 | -3.40807 | -50.3339 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| abdb7333-2d4b-3773-83be-cc44796543fe | -3.40411 | -50.3274 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1485835c-a54e-39b4-b079-1b73be6d8061 | -3.40318 | -50.33308 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b28b9ede-113c-32c0-ac73-f4551381b747 | -3.33954 | -50.12202 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README79.md)
