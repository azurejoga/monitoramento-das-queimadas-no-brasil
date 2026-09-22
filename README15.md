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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1531a8c3-f5ea-30e9-bec4-37326c9c7594 | -3.4288 | -61.314899 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2653686-39dd-37a6-a645-c1a499dea157 | -6.6132 | -59.9119 | 2026-09-22 01:19:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd5959fb-ca60-309a-bb3c-c45cdc475073 | -6.4626 | -59.974998 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 292a0ae2-6569-3931-8625-ad82255cb98d | -6.2483 | -57.780399 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a247b9b5-99d8-3c93-8c5f-f5c32fff6614 | -15.3642 | -57.3255 | 2026-09-22 01:19:00 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c90f4b9-53a7-3710-a80a-9bd16b2c035d | -8.6127 | -54.6166 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb48de29-7737-3464-bc14-f397b2161164 | -12.1581 | -47.391201 | 2026-09-22 01:19:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4112a8a6-bc1a-3a71-bb02-2f604236e81d | -12.8215 | -54.019798 | 2026-09-22 01:19:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 743291ee-9686-31b1-8ce8-b07e6c9e62e1 | -3.5001 | -59.194801 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23e9a70b-73b9-3fba-9a9b-0be1549f6889 | -3.3046 | -57.856701 | 2026-09-22 01:19:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46096ed1-0920-33dd-b67f-bb2a895d8427 | -7.568 | -57.685501 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e24cf71-8915-384c-93f7-c9655937b0a0 | -3.4768 | -59.587002 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1adeed97-31d4-33a7-9274-3735b6f74ae2 | -7.3206 | -55.218498 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a2685e7-b03b-367d-ab42-bc4cc30658d7 | -3.3063 | -57.863998 | 2026-09-22 01:19:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7cb7bba9-6709-3473-a6cd-96a74e1f2da8 | -3.9261 | -56.052502 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c723ca14-de6b-36e5-af02-3c7ea18565b9 | -3.4106 | -60.197701 | 2026-09-22 01:19:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fb09cbfd-aa39-35ba-a9c0-b1e8ca393dd0 | -3.24 | -60.8036 | 2026-09-22 01:19:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47c9cbcb-78a4-3b45-81ee-ed6189b1a0f9 | -9.8988 | -48.478001 | 2026-09-22 01:19:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 629a4ae2-d6b4-3f42-ad05-90ecce3dd62c | -3.4206 | -61.324299 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e8d37ef7-def1-3d4e-9f19-89b6deba1b89 | -8.2434 | -55.277401 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c494ca9-c69d-3b0c-9736-a9fa1e2354df | -18.727699 | -46.921101 | 2026-09-22 01:19:00 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 583635d4-c0ce-3452-b46d-b26abdc7b5c9 | -6.6964 | -56.1604 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7510ae5d-99b3-3dd2-951b-6d6581517759 | -2.7935 | -59.8904 | 2026-09-22 01:19:00 | METOP-C | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bab88d47-2aab-376a-a880-8767081cd3ca | -10.5349 | -54.487801 | 2026-09-22 01:19:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b46fe6d-a747-3b3d-8c77-5d7f866ac389 | 2.3151 | -60.9114 | 2026-09-22 01:19:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3aa8ce2f-6167-39a5-994d-84b4828210b8 | -7.5924 | -57.702 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fab069d-7381-344d-9c60-432fb3f94963 | -6.6375 | -59.9286 | 2026-09-22 01:19:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 464027e1-2935-3830-9f9d-e82d10609832 | -3.4933 | -59.569 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0daa45f4-4624-307c-8274-68c343fdeb8b | 1.5482 | -55.891602 | 2026-09-22 01:19:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8af7847-4b60-3de7-a55c-668364795774 | -6.514 | -58.305302 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c9a2e0c-7daf-3d6b-9cba-58e3e5b4f871 | 3.306 | -61.269299 | 2026-09-22 01:19:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c4a69150-8564-3ffd-8964-708d973be881 | -7.5696 | -57.692501 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 303df091-cb04-31ba-b530-c01e52d22acd | -3.5149 | -55.486599 | 2026-09-22 01:19:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 630b4750-1522-3f21-9aaf-bac69fe19af2 | -6.3024 | -57.745899 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a88c74f5-305a-39bd-ada7-0277a0f2a018 | -16.991899 | -56.448299 | 2026-09-22 01:19:00 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f8f51311-32ad-3127-9ba8-52c45dab3742 | -3.98 | -60.0271 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed6d0b44-b77d-378f-b64e-5aa0a4fdcc55 | -6.7973 | -59.135899 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1f6a48b5-a94b-3baa-aeb5-fa693511d55e | -2.8656 | -57.787498 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 309113be-3a5c-3c65-a9ba-87dd5dd25cef | -3.4642 | -58.323299 | 2026-09-22 01:19:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 643ef98e-3ccc-39f2-b302-68d41b800a3f | -6.6489 | -59.933399 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b857ae9d-35bb-367c-9253-ed0f8ee6d834 | -6.6827 | -58.455299 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b80ca430-b0ea-3ef5-97e8-d3fe982371d1 | 1.7683 | -60.238098 | 2026-09-22 01:19:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 87c969dc-6f69-32f9-b7d5-e0338c831fb4 | -8.1045 | -55.345299 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c4891fe-1c62-3693-ad0c-35479d5f7423 | -3.0569 | -54.416801 | 2026-09-22 01:19:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d46345d-2530-3b91-bc7d-216148e15321 | -10.5923 | -53.995499 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 206a4b07-d9a4-3012-ab05-f7ae1f5b76b8 | -6.0834 | -57.691799 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa8c9fe2-688d-32a2-a608-752f68b6783f | -6.7822 | -48.671501 | 2026-09-22 01:19:00 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 591608d2-2eb1-307d-957e-69a8bade6e20 | -4.2687 | -55.447498 | 2026-09-22 01:19:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11c604eb-ca2e-39e0-af50-3ff74bd8f696 | -11.4293 | -47.366798 | 2026-09-22 01:19:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5af20abb-0251-3ce8-99a9-6be52f99235e | -12.7866 | -54.0466 | 2026-09-22 01:19:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 82b28792-3fed-3ed7-8bf5-33c989dd03ff | -6.0768 | -57.618698 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96ff8489-b2ab-35a8-aae3-72e2ba10b8f2 | -6.6293 | -59.937801 | 2026-09-22 01:19:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f3c1b078-2d59-35e2-8574-cc8dff426f03 | -8.1065 | -55.3536 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e079c89b-ab0b-31e7-863c-83d35c1f4798 | -3.3992 | -59.518501 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f34e2038-e5b9-35d5-a566-1703f22a1241 | -11.0435 | -54.151699 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a78bebe0-6a44-3f6b-a9e7-bcac84390e45 | -8.9138 | -50.913601 | 2026-09-22 01:19:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62f55ec0-72c8-36ff-8531-e281dce1532c | -3.0666 | -54.414501 | 2026-09-22 01:19:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b41d082a-3a5e-3f93-b458-c8e63fd9ec48 | -6.6473 | -59.926399 | 2026-09-22 01:19:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d8290b31-da2e-309e-89c2-1760ffcf9320 | -8.0967 | -55.3559 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecc3e343-a520-3cf7-a1fa-04ec2d54255f | -6.17 | -57.709301 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3c4b42d-58f3-386f-9aaa-c50127c6afbf | -6.3139 | -60.000801 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5fec4116-075d-3671-b3ec-2e746e51b2ae | -4.2641 | -60.006901 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c04571d-d84f-3cde-a2ec-95e133d47e66 | -7.5974 | -57.678799 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc173c4f-22ea-3fb9-8ff4-cd6fbb61c07d | -4.9674 | -55.830399 | 2026-09-22 01:19:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a692a656-8295-3da5-91ef-262c5f65962b | -3.9041 | -60.596901 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d361d056-9b36-39b6-9a8f-813ee3a012e2 | -3.6837 | -60.579899 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e80e6fba-c4a1-3d2f-a3be-8b55baba9d51 | -12.1424 | -61.162899 | 2026-09-22 01:19:00 | METOP-C | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9b3c3374-cb98-30c8-9808-cd0cdb7c4c88 | -4.6795 | -55.615398 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51f0f180-6c28-3a4d-b5c1-8966f30293fb | -6.0735 | -57.872002 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faef0642-67fb-37cc-b62c-bbff8a2d295c | -8.257 | -55.247799 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| accf4b94-c3d5-3659-9926-3a5687981cd0 | -6.384 | -55.274101 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdb0137f-50fa-3f92-8926-ab26455af33e | -11.3138 | -54.029202 | 2026-09-22 01:19:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8796e4f1-0eec-3c50-af82-6d4c94504340 | -6.2251 | -56.043499 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e791f25-9d12-32be-aea4-ee4ebb08ad0a | 0.7805 | -59.195202 | 2026-09-22 01:19:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9d7705dd-c32b-3e32-bc16-d3745bc8fd9c | -6.342 | -59.9431 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6afef6d4-aabb-395f-b491-fe739797b7bb | -7.6973 | -61.5322 | 2026-09-22 01:19:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de5b8a38-a056-32be-a7a6-cb76c310c65a | -13.2849 | -51.771801 | 2026-09-22 01:19:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 01fe18dd-9f55-3d70-85dc-df19f6fa92aa | -8.6225 | -54.6143 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20bcee7d-5e27-3411-896f-944cc2108190 | -3.3699 | -61.282398 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9106973-6416-37ab-90f5-f25f279e61fa | -14.7561 | -48.437698 | 2026-09-22 01:19:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c4bd2011-b83a-3935-b775-9aa32af35e25 | -11.7503 | -50.815102 | 2026-09-22 01:19:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 94fcade4-5acb-3805-a964-346d5da51707 | -6.103 | -57.687401 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0517e83d-7a17-38a0-b2fd-b0a2fdd1ff03 | -3.9255 | -60.555302 | 2026-09-22 01:19:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e0fac696-63c2-3c7f-a447-5af974abfb00 | -5.7679 | -56.514999 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4591db75-33d7-3a37-a917-a7e377afc5fb | -3.5044 | -59.931999 | 2026-09-22 01:19:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98102df1-be13-330f-ac65-809a598e3c37 | -8.9214 | -50.9436 | 2026-09-22 01:19:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e82f23e-5e6a-3a77-9085-b1976855dd1e | -3.4658 | -58.330299 | 2026-09-22 01:19:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dad76489-c30d-393e-bb20-d97cc5da3ab7 | -3.4985 | -59.187901 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d338b37-05f4-33bf-a7dd-3b46780ed373 | -6.0409 | -57.820301 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17b3527a-a594-3be5-b945-b83d97d6a4dc | -10.6194 | -53.979301 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5e8200f-63aa-39fe-b191-51fae44e2758 | -4.2111 | -59.910599 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 13dfde4d-e6d0-369a-a7ce-4994fe837a14 | -3.4913 | -59.605202 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e94cc0be-55a6-38b8-930e-e9ed2497ec44 | -8.8314 | -50.504101 | 2026-09-22 01:19:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65632cb0-e02b-3695-937b-6cb9d3bed069 | -3.176 | -58.594398 | 2026-09-22 01:19:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d572ddbb-55b3-3eb0-a3a3-6f1c70abbbf7 | -6.1446 | -59.935799 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5b2b902-0af7-3a95-a4d8-a586c8e503dd | -9.5605 | -66.023598 | 2026-09-22 01:19:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 76943ea9-a961-34ff-9fe8-6ba4911f4eac | -4.566 | -54.916302 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b73f896-9c6e-301b-abb0-21ad38be6b36 | -6.0948 | -57.652 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1468dc6e-2480-343d-a14e-6c4e77c99c73 | -3.2965 | -57.866199 | 2026-09-22 01:19:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b939771-9150-3fb5-af0e-3a1201f16454 | -12.8005 | -54.061298 | 2026-09-22 01:19:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)
