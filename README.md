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
| 30438946-35de-3608-aca1-9c69a8862210 | -6.1465 | -57.9165 | 2025-08-04 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| ad10aacb-17eb-3353-a668-9c9f2ea6f6bc | -18.0619 | -51.3063 | 2025-08-04 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 5d153bfc-a56d-3a36-b554-b6299261d340 | -13.6941 | -41.3437 | 2025-08-04 00:00:00 | GOES-19 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 51.5 |
| 32f9e15b-9542-3f11-b425-3209da721118 | -6.1649 | -57.9157 | 2025-08-04 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 4587daf3-c86c-3681-b0fc-489e0f58409f | -4.1182 | -47.6443 | 2025-08-04 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 73c30c83-3cf4-38b8-b717-1021922e7146 | -22.5648 | -42.159 | 2025-08-04 00:00:00 | GOES-19 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 66.9 |
| 064b1aec-46df-3088-975d-e5509238c9d8 | -6.656 | -59.0981 | 2025-08-04 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4509f4b3-322c-38e3-9987-5ede35886729 | -6.6144 | -59.9656 | 2025-08-04 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 61c0e2d4-ccad-3b63-bf91-3fe18a8f9f1d | -7.0208 | -59.8346 | 2025-08-04 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 05c091e3-8a79-3f13-8f96-d91e07eb0902 | -9.3989 | -45.4928 | 2025-08-04 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| e0696041-c028-3d71-b0ab-556ddb480fde | -6.6329 | -59.9649 | 2025-08-04 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.7 |
| f94e0033-82a4-31c1-8762-2e44bbb26add | -6.6328 | -59.9841 | 2025-08-04 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 5546507a-0885-3f8d-806e-f32ade274c9d | -13.6935 | -41.3685 | 2025-08-04 00:00:00 | GOES-19 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 818c722d-d0d8-3da7-83fe-4e47e4ba0ac7 | -8.0132 | -43.1278 | 2025-08-04 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 78a26ca5-fe32-361e-90a2-951ac8bdd4f3 | -1.3187 | -49.3798 | 2025-08-04 00:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| e80ee18c-2493-307e-9b0f-6b1851e3567b | -4.7533 | -44.4445 | 2025-08-04 00:00:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 0517045f-8739-3b6a-90db-e33327cf571c | -4.7346 | -44.4457 | 2025-08-04 00:00:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| c449781b-a48f-32f4-b967-3dabaa3ffc3a | -9.3985 | -45.5156 | 2025-08-04 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 9652564f-1628-393f-b244-20663ddef271 | -6.6328 | -59.9841 | 2025-08-04 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 09d6a3c5-c530-3eb5-a72d-2799729cc102 | -6.6329 | -59.9649 | 2025-08-04 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 6951ee92-66c0-3a4c-8790-428c561da93d | -9.3989 | -45.4928 | 2025-08-04 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 0d1f4d92-57ab-3484-9418-f519c95006a8 | -6.6144 | -59.9656 | 2025-08-04 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d39fcc48-7f2f-3e63-b195-26975476fc35 | -18.0818 | -51.3028 | 2025-08-04 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 281c5bd6-70ab-3184-a6d9-27d4c01e65fe | -9.3985 | -45.5156 | 2025-08-04 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| fc295347-d3b4-39d7-9b81-b30060bf775a | -6.1465 | -57.9165 | 2025-08-04 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 53046f1f-4530-3425-89ce-6e962a534576 | -6.656 | -59.0981 | 2025-08-04 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 727a2c66-dd46-3a24-ae95-6bbff7a86d96 | -7.0208 | -59.8346 | 2025-08-04 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 4c8f7e5f-af21-36ef-9396-0031d8f017a5 | -13.6935 | -41.3685 | 2025-08-04 00:10:00 | GOES-19 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 52.2 |
| a48f39a1-1ec3-3465-8acc-0d8bf2ecb771 | -8.0132 | -43.1278 | 2025-08-04 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 713c6563-d1a6-3b4e-83a0-2b150de44f65 | -6.6559 | -59.1174 | 2025-08-04 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| eb31f3e2-e8ef-3bbb-8560-7cece08347df | -4.7346 | -44.4457 | 2025-08-04 00:10:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 8f3f29ec-074d-3bb6-9721-c651754409f1 | -6.1649 | -57.9157 | 2025-08-04 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 92096f3e-b54d-3b14-9f52-5a9050a9850d | -18.0619 | -51.3063 | 2025-08-04 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 672833b7-479d-3ddd-b3e3-3df76fecac17 | -4.7533 | -44.4445 | 2025-08-04 00:10:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| c5397c9b-6f46-35e2-b558-7c45abff356b | -4.1182 | -47.6443 | 2025-08-04 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 822b8b00-62d5-3de0-9c9b-c1177369b944 | -6.6329 | -59.9649 | 2025-08-04 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 41bdb868-50c5-33fb-825f-08178f58c9f1 | -6.1649 | -57.9157 | 2025-08-04 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 4f62ef08-ca07-328e-bfa4-77815fd1b11d | -6.1465 | -57.9165 | 2025-08-04 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 4772b774-8198-3a5a-8a57-7267c87a69a4 | -6.6328 | -59.9841 | 2025-08-04 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 6705f843-25d2-3aaa-82ad-d01a64701250 | -9.3989 | -45.4928 | 2025-08-04 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| e592d012-3c91-3623-8d3f-7c34b20c5db3 | -18.0818 | -51.3028 | 2025-08-04 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| f7ff3715-5789-3dc7-943b-d1ec91bbc5bb | -22.5648 | -42.159 | 2025-08-04 00:20:00 | GOES-19 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| d70b69d3-fd8f-3dcd-9a12-632622131345 | -4.1182 | -47.6443 | 2025-08-04 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c4a71f19-8672-3837-869c-b750a6555d00 | -18.0619 | -51.3063 | 2025-08-04 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 95.9 |
| d1750679-6680-3da6-89ad-137e273eae69 | -9.3985 | -45.5156 | 2025-08-04 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 100c16d6-4666-3893-b80b-14582019c94d | -6.6144 | -59.9656 | 2025-08-04 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 498e6cf0-dcc3-36b5-b50e-dfefa6e4a2ab | -8.0132 | -43.1278 | 2025-08-04 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| a1792ca3-904b-351d-9106-d6b8b4b626a9 | -6.656 | -59.0981 | 2025-08-04 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| f29a180b-bd99-3287-8c57-a34bb956dc80 | -6.6559 | -59.1174 | 2025-08-04 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 779860e4-9c08-3ee0-af45-4c3d0bda9328 | -4.1368 | -47.6435 | 2025-08-04 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| ddd3b15e-bf21-35e4-9fef-ada5c3a5c155 | -18.0623 | -51.2843 | 2025-08-04 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 388b8347-4e4d-3ff9-bf07-52ffdb05ccbd | -9.3989 | -45.4928 | 2025-08-04 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 87d76c22-bfb1-3d10-967a-9066b6a4d6d1 | -6.6329 | -59.9649 | 2025-08-04 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 615dece7-1c8d-38f9-a0ae-9226719f5447 | -4.7346 | -44.4457 | 2025-08-04 00:30:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 53c556de-28f6-31f4-88d8-9c1405ac58df | -6.1649 | -57.9157 | 2025-08-04 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 30670769-8f6a-351f-aedd-47663acc1094 | -22.5648 | -42.159 | 2025-08-04 00:30:00 | GOES-19 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 61.7 |
| 3ea8022a-5533-3a37-9e36-5d0516c5917a | -4.1368 | -47.6435 | 2025-08-04 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| e88c9edb-8961-3333-ad97-d05bb037ea42 | -9.4387 | -40.3419 | 2025-08-04 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 56.8 |
| 883ad665-47b8-3e3a-b393-e112ea51acc0 | -9.4196 | -40.3447 | 2025-08-04 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 140.3 |
| 06d2ba2f-671c-341a-a03d-d48423aaf2ad | -6.656 | -59.0981 | 2025-08-04 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| f022d000-bc6b-3c6a-888f-4c488205452f | -18.0619 | -51.3063 | 2025-08-04 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 3180842c-a3cb-3cc4-a5d2-e0fb2bfbcb59 | -6.1465 | -57.9165 | 2025-08-04 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 2550d5b2-77ed-3e06-91ca-f9f7125f1e0e | -6.6144 | -59.9656 | 2025-08-04 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| fd41bde3-5aab-38d4-aa52-0369436ca9ba | -4.1182 | -47.6443 | 2025-08-04 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| b1ac42a7-b186-35bb-80ae-f296df32a7a2 | -6.6559 | -59.1174 | 2025-08-04 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| d6c23779-209b-3078-9596-e2814f91ae1f | -6.656 | -59.0981 | 2025-08-04 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| af843b15-5977-364a-8674-fb5ddbc66b10 | -6.6144 | -59.9656 | 2025-08-04 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3c4f9f74-65a3-3507-88ff-217adb28ab7b | -7.0208 | -59.8346 | 2025-08-04 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 7c7c7077-3be9-328f-8929-0ee9a96ab587 | -12.1422 | -43.3707 | 2025-08-04 00:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 55b06f65-a81b-386d-b3fe-dfb130e02574 | -6.6559 | -59.1174 | 2025-08-04 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| bb447e52-b964-3001-92a1-807beaecbc44 | -9.3989 | -45.4928 | 2025-08-04 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 872a7630-82de-307f-895c-7156951c487f | -22.5648 | -42.159 | 2025-08-04 00:40:00 | GOES-19 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 71.8 |
| 2289d009-dd8c-30a9-bc5e-514e04b6114b | -4.1182 | -47.6443 | 2025-08-04 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 888da65e-5756-38a3-b070-5e9085a6e864 | -9.3985 | -45.5156 | 2025-08-04 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 92054bc5-48d7-3702-a0c8-971113d7d0b9 | -18.0619 | -51.3063 | 2025-08-04 00:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 527ab59e-db00-3f48-871f-f34fb8353963 | -6.1465 | -57.9165 | 2025-08-04 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 63b2495d-7038-3ff4-9aaa-f688a8fb88af | -6.1649 | -57.9157 | 2025-08-04 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 46d04bd8-2b6c-3295-bd2e-33314ad76ecf | -6.6329 | -59.9649 | 2025-08-04 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 4ef4c434-9fc8-3506-96ab-1ff77c837c19 | -8.0132 | -43.1278 | 2025-08-04 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 40dbe34b-d16a-3396-ab25-598f3c7fd2c7 | -22.57861 | -42.15646 | 2025-08-04 00:43:00 | TERRA_M-M | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| 20b18e79-a43a-3365-8b53-826158445aa8 | -22.23001 | -47.32261 | 2025-08-04 00:43:00 | TERRA_M-M | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 4d497ce4-1f02-33d4-a741-329f26124a7f | -20.72364 | -47.29374 | 2025-08-04 00:43:00 | TERRA_M-M | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 63fed62c-7f9a-3ac4-ab0c-9b9a0acf4aa2 | -23.3754 | -47.41082 | 2025-08-04 00:43:00 | TERRA_M-M | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 7be565e1-4f34-3805-ade0-1c658ef765e8 | -19.52123 | -46.8967 | 2025-08-04 00:43:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a176a84b-ef09-3b7c-81ee-4a42f09d8962 | -22.56993 | -42.17693 | 2025-08-04 00:43:00 | TERRA_M-M | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 47111756-e855-3930-b3d3-85b2eb86fd7f | -22.90662 | -43.46731 | 2025-08-04 00:43:00 | TERRA_M-M | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 3af7e103-9964-3695-825b-e8781148e4b3 | -24.32145 | -50.84658 | 2025-08-04 00:43:00 | TERRA_M-M | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 94b6d412-b655-30df-82fd-b46b4069eb8a | -22.56676 | -42.15897 | 2025-08-04 00:43:00 | TERRA_M-M | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 62.3 |
| 701e4cad-5277-3bf6-a81a-501d4b0023a1 | -21.15661 | -49.06374 | 2025-08-04 00:43:00 | TERRA_M-M | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 6cc3fcf5-6323-3ade-98c1-61bdca15f85a | -21.15532 | -49.05418 | 2025-08-04 00:43:00 | TERRA_M-M | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.6 |
| f71d5c65-8670-3fdf-99a2-06c198f8ebf1 | -20.0883 | -44.00731 | 2025-08-04 00:43:00 | TERRA_M-M | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| a26ded5b-512e-357d-bde5-1e0d72259c0f | -21.25248 | -43.98361 | 2025-08-04 00:43:00 | TERRA_M-M | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| b447b8c6-ec8b-357c-b34f-85fda7a3a7f2 | -19.52277 | -46.90693 | 2025-08-04 00:43:00 | TERRA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 02de97cd-6b30-3813-aa82-6bef0efb54ea | -15.56388 | -47.08303 | 2025-08-04 00:45:00 | TERRA_M-M | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4713d306-6dc5-3a19-852e-b73759483364 | -13.69638 | -41.36886 | 2025-08-04 00:45:00 | TERRA_M-M | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 52.8 |
| 972d21d7-9239-3e8c-8c21-fc927140babe | -16.42603 | -43.71476 | 2025-08-04 00:45:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 18ec6b7f-57a4-32bc-bda3-0d71d16bcaef | -16.42899 | -43.73219 | 2025-08-04 00:45:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 21.1 |
| a1973c43-7c1d-3ace-921c-c5de4d81d4dd | -15.69896 | -48.99872 | 2025-08-04 00:45:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 580f28b8-d023-3e9f-a5f2-9fe8aac16d96 | -18.06193 | -51.29921 | 2025-08-04 00:45:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| fe9cb514-8a93-3322-b5ec-556efa116a9a | -14.84699 | -48.39198 | 2025-08-04 00:45:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |


[Clique aqui para ver as próximas entradas](README2.md)
