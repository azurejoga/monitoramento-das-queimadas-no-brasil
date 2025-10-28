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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 378bba34-e5f2-3b66-8cf7-471793e4c85b | -15.45166 | -43.64384 | 2025-10-28 04:17:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8057ad79-786f-34d1-a8c9-1e70186ffa83 | -13.36004 | -47.67087 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 798a9c8c-5955-3585-8b6e-2e7b534801cb | -14.66597 | -48.41148 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aded465a-4825-30ad-8077-e53f7cf3d31e | -13.1871 | -48.44709 | 2025-10-28 04:17:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7240075d-5c1a-3370-b431-fc3691c0d482 | -20.12417 | -42.39483 | 2025-10-28 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 03c6817c-1abf-36e4-8804-c31405c065dd | -17.26606 | -45.29132 | 2025-10-28 04:17:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3957c68-db32-36af-a770-94e93c6e4b4b | -13.91081 | -48.47551 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c456b55c-06e8-310a-83c6-e0fd950b13aa | -19.02866 | -42.03622 | 2025-10-28 04:17:00 | NOAA-21 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| d89f73c9-039e-3186-ba59-db0c84ab1d83 | -18.05484 | -45.09311 | 2025-10-28 04:17:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8daf584-3fcc-3def-8f6d-e1bc2a873e7a | -15.17258 | -47.22632 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60ed9dd7-810a-3753-b8fd-ef3ced05695b | -13.65969 | -47.63873 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f566b0ad-2b16-3c4c-8bdf-dcc1a68d02c2 | -13.1843 | -48.45015 | 2025-10-28 04:17:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5f4d238-b307-33a5-bafb-e137c3faef2c | -13.55862 | -47.16064 | 2025-10-28 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4310ee0-d9ba-3878-a8c7-6fd53817efb2 | -13.30285 | -47.0771 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7208ca92-0f0c-3deb-908a-1ae7d541f058 | -13.35976 | -47.39224 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cb890a55-9da1-3ad0-bc22-3b0f957599eb | -14.65581 | -48.40503 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29304981-6c88-3dd0-9d9f-4c75e6dbe7a0 | -13.62688 | -46.4711 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 569a3c17-10f1-3a49-aa00-acf85f7348d0 | -15.54421 | -45.98026 | 2025-10-28 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 87571a34-5287-32ff-83d2-0d26523f41d0 | -13.73835 | -48.42317 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac385145-a6ef-3b17-b1c7-cad42f6bacb8 | -13.26504 | -47.87219 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36fd6120-9eca-36ba-ade9-be2b8866afb6 | -14.76427 | -44.95541 | 2025-10-28 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0433ea8f-e2d2-391f-ac1b-bb777225d820 | -15.48867 | -48.13012 | 2025-10-28 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19def9da-dd5c-3b42-ad66-f5c979e35903 | -13.74096 | -48.41612 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2230e549-2823-3587-86c7-be88cb38c302 | -14.03332 | -46.65203 | 2025-10-28 04:17:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 454bc130-ed22-363c-8b20-deaa411cbd4b | -13.22926 | -47.11004 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9f037be9-c9fc-3584-9d91-6d466856f084 | -14.81516 | -46.71081 | 2025-10-28 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e400c103-3580-31aa-b13e-f8f16d0b26d5 | -14.76048 | -44.95836 | 2025-10-28 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64a96c49-4c0a-3a8f-a26e-dda802f4a016 | -16.74393 | -41.69252 | 2025-10-28 04:17:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2c3e3b53-38ff-3c9a-a039-e56e30f35b8e | -15.23282 | -47.94595 | 2025-10-28 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9601a06b-498d-3827-b553-b08a3c380453 | -15.15652 | -46.60275 | 2025-10-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 312f4909-7f98-3689-8091-efc0bfc656ca | -13.22891 | -47.73528 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0fc3925e-8358-397a-961c-0d732a859725 | -13.22634 | -47.08472 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3b29e73-f32a-334a-b5e9-38309ef0e150 | -19.43607 | -44.76886 | 2025-10-28 04:17:00 | NOAA-21 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c6f6a05-c512-3389-9b87-8f6168b40ac7 | -14.14785 | -45.32567 | 2025-10-28 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c1b32e7-bc69-3e84-a764-773c9fbaf9f9 | -13.63906 | -46.46508 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aee8cdc5-05eb-3436-b60e-422e2192c964 | -14.31248 | -46.51698 | 2025-10-28 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f6bf04cb-8ead-3254-95d3-81dda1629b8b | -13.23345 | -47.10651 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42d041e0-5c8e-35f9-b1d3-b3ac905366ab | -13.37143 | -47.41018 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 286e9472-da9e-30d7-8538-957762179bfe | -14.15114 | -44.24003 | 2025-10-28 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fa853b8-f432-372c-83bd-e43c1dc2f5df | -13.5531 | -49.58021 | 2025-10-28 04:17:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f5002b0-9e9b-3b16-96d9-f984899ebe46 | -13.84583 | -49.05875 | 2025-10-28 04:17:00 | NOAA-21 | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76c58070-5372-3e42-ad26-0af9cd8fdb03 | -13.94345 | -48.41782 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6fc69c8-8525-33b5-a9f9-c091027fe03d | -13.31036 | -47.68973 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90ee901d-209b-30d6-8fe9-6200fdb9c2d4 | -13.24014 | -47.06652 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 52b4f29e-90d1-3054-80a3-a6b1fccfa0b6 | -14.73201 | -47.35875 | 2025-10-28 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3de6a76d-e69c-3b12-a675-840da3a9dbf7 | -13.72167 | -43.91591 | 2025-10-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1c4931a-8258-3148-b677-3fe7185dd666 | -13.23118 | -47.07724 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73321562-1fb4-3a1b-9917-e41be4aa99b5 | -14.81177 | -46.71022 | 2025-10-28 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 463d71f1-690e-3f57-8890-a5fe04cdefa0 | -13.50725 | -46.45052 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f4f391e-2fca-33ab-ab49-ab5d0cf8e2e2 | -14.42291 | -47.85537 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0915bc69-7093-3db7-be0e-4208a5bb758b | -13.1841 | -48.44217 | 2025-10-28 04:17:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b04ccc19-a4cd-3840-acdf-40871e62fbe4 | -15.58665 | -46.59649 | 2025-10-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9c6f0c9-92ea-352e-99c9-f92d87402626 | -15.2312 | -47.95375 | 2025-10-28 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27909afe-5736-380f-8036-42b757d86e43 | -16.28516 | -45.88099 | 2025-10-28 04:17:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dac8b35-3130-3155-8356-f45f32d9fa96 | -13.62667 | -47.03067 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| e62e808a-b5fe-3ea5-b336-1833b2ea7428 | -18.49899 | -43.98415 | 2025-10-28 04:17:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bb84266e-affa-3eaf-ab3c-034c056f5ee6 | -14.90541 | -46.24511 | 2025-10-28 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 945079a4-8f14-387a-a646-997672c53516 | -13.66535 | -47.62706 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7dbbcab-b644-307f-a9c6-b43f91940901 | -15.15709 | -47.94074 | 2025-10-28 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7831c5d0-4f2f-3454-a21c-1afe3f8fbf25 | -19.25206 | -43.66683 | 2025-10-28 04:17:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 968f8c4d-a24f-380b-a2a4-450535beb2ad | -13.22083 | -47.09613 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 550bec2b-8af8-3ea3-80aa-73fdd6cbed99 | -13.63234 | -47.03949 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 1424e5e9-6f26-394f-813c-07e9a5609de1 | -13.54908 | -49.57977 | 2025-10-28 04:17:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9b5a9c2-813e-3ef2-80dd-967f17baa1b3 | -13.18801 | -48.45086 | 2025-10-28 04:17:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7fc204c-b7e8-32fd-9457-5f9cae43bb40 | -14.64123 | -48.40243 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfe2848b-cb50-3906-9888-a6de8eccb5c9 | -14.68346 | -46.35458 | 2025-10-28 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87bdd3b8-3b01-3755-a20b-fd01ce5b141c | -15.56964 | -43.25566 | 2025-10-28 04:17:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6c99816a-cfa5-3b46-81af-138b1549e80f | -15.20331 | -47.21181 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d93358f-1703-3e23-8535-26ad47f56ba3 | -13.94221 | -47.75562 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 91138bda-d7a9-3922-9a45-ebe1e7177710 | -13.66466 | -47.63105 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 191e6fe1-bdb0-33ae-a26d-36cc156fd926 | -19.25896 | -43.66801 | 2025-10-28 04:17:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d024a7d2-e2b6-32d1-b8a3-82529d51fb6e | -13.04847 | -47.55685 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb85bbd4-f324-3aaf-a278-77d4f7bf3be8 | -13.18855 | -48.43854 | 2025-10-28 04:17:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f97ea32-43d4-32d4-9e2b-25dedd9fab0d | -14.76701 | -44.9595 | 2025-10-28 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 529a304a-69f5-3c75-bbc2-0ff0828be74b | -13.25189 | -47.73049 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39aa83a3-0a16-3445-b385-afa313773b9c | -13.2215 | -47.09215 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9bac098d-e880-3e43-99f4-7949b3574972 | -17.37851 | -45.35487 | 2025-10-28 04:17:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b43ab057-464f-387d-ac6e-06f475d57841 | -14.89795 | -46.76338 | 2025-10-28 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 668e01e7-791f-3ea0-a660-c923ce333560 | -13.95016 | -48.4006 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 958c51e2-5b8b-39d4-a9e2-6d85ac653710 | -14.54744 | -47.98006 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 78e48a69-9930-359c-b244-d0dd211ce8c8 | -13.63365 | -47.03155 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 37.1 |
| e093a6ad-7a50-327b-b2cc-9abb4c265f71 | -14.31935 | -44.68921 | 2025-10-28 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f1d90c38-efe6-3ad3-8e1b-7fa0965d115f | -15.46964 | -43.05334 | 2025-10-28 04:17:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 75e6858b-2c0e-3d48-b5f8-121e215f9f97 | -15.16849 | -47.22964 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2879cd6-2bf3-34e0-97db-5e39d9a15bb8 | -13.26865 | -47.87282 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec26b18d-36da-3f91-af51-b72d6cbc89e1 | -14.56522 | -48.00572 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 920ae06b-4241-3ed6-9069-0060995a663f | -13.90851 | -48.37811 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 00b25746-34cc-3deb-9420-229d46c921a4 | -13.55025 | -47.16774 | 2025-10-28 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 86743bb3-c2f6-3dc8-b081-003bfa21ac51 | -13.3564 | -46.47176 | 2025-10-28 04:17:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a28cdf9a-77d3-325a-a06e-8e4db4dd4f3d | -14.76982 | -44.96354 | 2025-10-28 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb371c2f-0138-3004-8546-c7a0d48cd7e8 | -14.53664 | -47.97862 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 887d5e93-67dc-3a59-a64e-7f0832f88948 | -13.47998 | -47.45589 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ac44bac-f4b0-357a-a575-9f5b6564a8a1 | -15.15961 | -46.58398 | 2025-10-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| dcd3b783-4c70-3d30-bb59-031b97ad795d | -14.16027 | -44.70679 | 2025-10-28 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2403c3b-1679-38f5-ae29-823f64a9a70b | -15.15377 | -46.59838 | 2025-10-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b76f711d-f676-3f82-bf4a-92995d94f2e7 | -13.24829 | -47.72989 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 243644f7-f3a6-3e1b-8509-9223555b8234 | -13.95236 | -48.40384 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a631d326-c0cf-3378-9834-85660a404570 | -15.19923 | -47.21505 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| da42751c-f818-3001-8f95-e37fd7d61241 | -13.63504 | -46.46827 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 408871b2-3cf0-3a36-984c-cc80c5513ae8 | -13.31843 | -46.57449 | 2025-10-28 04:17:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README39.md)
