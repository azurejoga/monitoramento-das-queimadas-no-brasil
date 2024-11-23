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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7a3e24b-720d-3b1f-810a-ab4ff00857a7 | -3.20874 | -42.90952 | 2024-11-23 03:53:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97c56811-744d-30e9-8f94-2ef84b2a7e26 | -3.95016 | -41.49607 | 2024-11-23 03:53:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c0f7a1fc-eb17-3692-bbf7-b0f2d4b21fe2 | -2.08166 | -46.28244 | 2024-11-23 03:53:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62e1650f-8e26-3c33-8562-9e759f8ed2e9 | -2.66436 | -46.15465 | 2024-11-23 03:53:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02662a5d-7929-3dd3-abaa-df4ed9f29393 | -2.70826 | -46.28058 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 38b58b65-ff1f-33a4-b3b9-a10aa8aba760 | -3.14565 | -44.47964 | 2024-11-23 03:53:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e16c19e9-b128-3e20-aa86-fb9ae0917ad8 | -8.34454 | -37.28737 | 2024-11-23 03:53:00 | NPP-375D | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aee022ca-c6a3-348a-84c4-14bc92e7c70c | -4.44734 | -40.60645 | 2024-11-23 03:53:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ba2b0977-ab54-37ac-b4b6-25f62bbbd503 | -1.89521 | -46.4305 | 2024-11-23 03:53:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcfc0d74-f15a-32b0-9b3a-45a9cab7face | -3.60213 | -41.66974 | 2024-11-23 03:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 31493b46-5e54-3a68-bb26-7dd4ac50f349 | -3.14677 | -44.48125 | 2024-11-23 03:53:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e9eece47-4167-3bdb-b716-8b2ac05849a0 | -2.93808 | -48.05667 | 2024-11-23 03:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 465155b4-83d9-3f2c-866f-a84bbf12d47b | -7.05082 | -40.41305 | 2024-11-23 03:53:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 19e367ba-9bd4-33ac-85de-90e600635a4c | -2.08457 | -46.28246 | 2024-11-23 03:53:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 524648fb-5fa9-3202-84b8-e57b9ab3417e | -3.33013 | -45.35058 | 2024-11-23 03:53:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21869b3a-adf2-3f8f-92db-d6bde87dcc76 | -2.14807 | -50.91546 | 2024-11-23 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9b08c673-fa83-3e98-8b0c-0887e7fd8a31 | -2.69994 | -46.10223 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bbbddb7-282f-3641-ad09-ab094cc19fa5 | -1.79489 | -48.4468 | 2024-11-23 03:53:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 305e2fec-cdbc-3d0f-bd0e-816a3961b5e4 | -9.83349 | -36.13281 | 2024-11-23 03:53:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bb80f13c-9f98-3734-85ab-fa9a254b7813 | -2.75948 | -45.93464 | 2024-11-23 03:53:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 60adbb0d-1c21-3177-9a32-764559f7d5fc | -2.79625 | -48.67747 | 2024-11-23 03:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a75bf3bc-6c66-3b45-8ca4-60efabdc4ab0 | -3.63181 | -44.34838 | 2024-11-23 03:53:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d879aa6e-8cc0-32e2-acbc-f15669a54157 | -8.66361 | -36.98029 | 2024-11-23 03:53:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e6df678e-a788-3b91-ada0-32d1aebcbd1c | -2.69402 | -46.26833 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3e0bc9c-ff6a-3827-9a73-132608fe16f6 | -2.64566 | -46.13815 | 2024-11-23 03:53:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a88f8ba-1607-3f98-92a6-1a826c4ed412 | -8.07455 | -34.9781 | 2024-11-23 03:53:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8b341d8f-3d6f-304e-9b3c-cf8e2f657f66 | -2.70772 | -46.25081 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3bbe137-ad54-3f44-92ba-3da8bcbeb4d9 | -4.11463 | -42.47401 | 2024-11-23 03:53:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7d45f4a8-0f82-366f-abc1-e31d0bab6da3 | -2.70509 | -46.26685 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c05c79b-eba9-3b9e-83c0-07dce5a466bf | -6.37086 | -47.15062 | 2024-11-23 03:53:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0ba222c-f997-33cb-9edd-3649dee1303e | -2.70351 | -46.27651 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f3efa3f-b25f-3447-8039-84af73cbcafb | -4.10269 | -42.47202 | 2024-11-23 03:53:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c52f9b1c-c5b7-346e-b317-1cfbeb800aef | -3.14404 | -44.48918 | 2024-11-23 03:53:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6cae1d2-484a-3912-a3a8-3e61f15f3c45 | -3.60419 | -41.67327 | 2024-11-23 03:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 82125686-0218-3e4e-8f11-1bd94abd7213 | -2.70046 | -46.09909 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f63a36e-b618-3a04-aed4-766830d8e9ba | -2.15 | -50.92188 | 2024-11-23 03:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a32ade3-56c6-3032-91dc-7669d4bb7e1d | -7.07458 | -40.00156 | 2024-11-23 03:53:00 | NPP-375D | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0e117e55-17b7-3d16-b4fd-1dcecc305153 | -2.65406 | -46.2482 | 2024-11-23 03:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4db73cc5-8958-3d29-8311-779e1e08bb2d | -4.02806 | -41.79949 | 2024-11-23 03:53:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 51e55e6c-6e98-3653-9d5e-de111b8d1522 | -6.14726 | -46.67662 | 2024-11-23 03:53:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 734e27b1-f54b-3c77-be73-8af137ea34d3 | -3.61105 | -41.67924 | 2024-11-23 03:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 50accdd9-13a5-30d1-85f1-034c6ca35d02 | -4.03113 | -42.19532 | 2024-11-23 03:53:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0d02d2e7-b5d9-3f3a-8af0-9095f0105525 | -0.93473 | -47.55838 | 2024-11-23 03:53:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34c77da4-5f26-3cf4-b79c-1a3c5dfa0fcf | -2.6649 | -46.15142 | 2024-11-23 03:53:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e26a8d3-d282-369b-af4f-3d6625e42aca | -6.18319 | -45.44996 | 2024-11-23 03:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e66bb4b1-160f-3c35-8d61-21b069cfb8e6 | -2.81804 | -45.16271 | 2024-11-23 03:53:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e085636-3d91-39ca-9bf6-fd3a52cd2667 | -1.96085 | -48.38907 | 2024-11-23 03:53:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| badafbd5-5280-32d1-9252-eeed7b92bd5e | -6.14566 | -46.68576 | 2024-11-23 03:53:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ff48b0f0-226d-3b80-9a43-4c8006c30d5e | -5.13128 | -41.55638 | 2024-11-23 03:55:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1f8c57e2-0391-32ae-922b-3fb764240b09 | -5.32547 | -44.78468 | 2024-11-23 03:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 745f30f2-84b7-31f8-a654-7a2f94f89d9d | -4.66126 | -45.67322 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2d458cdf-a5f6-347d-8397-0831f5ed1c3d | -4.4114 | -44.11566 | 2024-11-23 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f3f3801-d0b0-3e5f-a6ff-615585575b99 | -3.9437 | -47.97024 | 2024-11-23 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 36ca4dac-4c5f-3e2a-b63f-ef9577cc0587 | -3.8106 | -51.34074 | 2024-11-23 03:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7e5f8ad-a766-37c0-9fd7-6d143b4a16c8 | -5.15567 | -45.39028 | 2024-11-23 03:55:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 117bfa52-f0dd-380d-91ce-6471aa79712c | -4.03255 | -46.19481 | 2024-11-23 03:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 738b1c97-b525-3511-b48e-737080a609d7 | -4.66445 | -45.67221 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 25da90ec-0d33-3856-ac76-a147d8421e75 | -4.65952 | -45.67154 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c13300d2-6564-3880-b6b1-2806bb2dae83 | -4.01321 | -44.33395 | 2024-11-23 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95ffd1df-60bf-3630-9dd0-82334dbd5fd5 | -4.89887 | -47.41508 | 2024-11-23 03:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c0b6d01-8fff-36d8-ab80-9382697b5a1a | -4.21452 | -46.16034 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10bc4fc8-a319-352a-9193-19802a434fe3 | -5.20425 | -46.81554 | 2024-11-23 03:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d3fd616-5f4f-3485-912b-e2d283975b5a | -5.4684 | -43.24287 | 2024-11-23 03:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 908d18ce-c6b6-35b2-9369-bf2f82d2a939 | -4.55946 | -48.02031 | 2024-11-23 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 043d5876-65a3-3391-968c-716c73b41a46 | -5.44658 | -45.58419 | 2024-11-23 03:55:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ea5f7b3-dcd1-3e31-ad0b-3a5f1bfc76dd | -4.54888 | -45.87643 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9b985cfb-3ecf-3ebb-9ffb-ba1ae7461048 | -6.39879 | -39.12299 | 2024-11-23 03:55:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 09185664-7ac1-3560-80b4-9a116b30f005 | -7.01298 | -39.2241 | 2024-11-23 03:55:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 53fabcbf-c9c5-300f-80b8-60ddd4ff1033 | -3.8556 | -46.95173 | 2024-11-23 03:55:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fd2363c-07e2-3762-9c1e-27fec6a2fb2b | -4.75286 | -45.78922 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea0eaefd-be6a-3335-84f2-6526d3eada2b | -5.1083 | -43.15779 | 2024-11-23 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1cd15cd3-147c-3b5c-96c2-1650209ee9df | -4.60426 | -46.49303 | 2024-11-23 03:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 66bab89e-fb7c-3d5e-9194-7bc98d507706 | -5.16083 | -47.03908 | 2024-11-23 03:55:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86cc882b-2973-34f5-b544-752381ffb2d0 | -5.00994 | -41.96176 | 2024-11-23 03:55:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3e3d7949-8fd3-3560-a59d-e34a0443f857 | -3.92273 | -45.365 | 2024-11-23 03:55:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab24e1c1-6bf8-3f66-8445-e9934964463b | -4.52935 | -42.91537 | 2024-11-23 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| f9e375f9-e103-37eb-acde-c3bf0383d3c4 | -6.5017 | -41.48991 | 2024-11-23 03:55:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 11dbd301-9851-3bca-8a3e-b5b388ed52c3 | -3.95598 | -46.89266 | 2024-11-23 03:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cd2725b-d965-39df-ada3-65b62af1bfd4 | -5.32972 | -45.48783 | 2024-11-23 03:55:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3115f86a-f7fd-3530-8703-3fdf8dafa994 | -4.52587 | -42.91111 | 2024-11-23 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| fff567dc-34f8-396f-a371-7251d6b0a75b | -3.94986 | -47.97137 | 2024-11-23 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 36e291ac-301d-35c2-92dd-29ac20ef5c11 | -4.34124 | -46.01355 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97c4acea-5bb1-3b7d-880a-36f333a837aa | -5.33002 | -44.7855 | 2024-11-23 03:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 521ab8c8-e0b0-3c6f-ac27-7f0463c872c7 | -6.32002 | -39.98106 | 2024-11-23 03:55:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aa95090f-a6c4-3782-b830-afe1446dac5b | -4.41656 | -44.11201 | 2024-11-23 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0ed00ed-98d1-3ab2-bad1-0d456b257fac | -4.7323 | -44.4355 | 2024-11-23 03:55:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1f1f6ac-28c8-3ed5-8b92-d37b5da81b27 | -4.28912 | -44.81261 | 2024-11-23 03:55:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d44a9400-ffd9-3c08-b4e4-df74a9c4bc51 | -5.22648 | -43.73903 | 2024-11-23 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13fcf1b1-c896-3369-83a8-25401fcf98d4 | -4.74936 | -45.7838 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e3fbf1a-1100-3ae4-a763-e4d76063c32c | -5.84836 | -40.80152 | 2024-11-23 03:55:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fbccec89-2639-3f30-94d4-d2bafc979faa | -4.11896 | -43.23188 | 2024-11-23 03:55:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddd07577-0f04-3070-98a9-78d97b35ffe2 | -5.61952 | -43.48061 | 2024-11-23 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13a15ab8-1ebb-3d0d-84ba-52473f00873f | -4.16292 | -46.80872 | 2024-11-23 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5f18d55-6b1d-35e5-a163-dab6a0c0b09e | -5.56936 | -46.28719 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 93793bbd-0a57-3774-b937-468cc1d1877c | -3.00476 | -51.55419 | 2024-11-23 03:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 33815b71-69eb-3f54-ae3d-b1ed5cdc165e | -6.14184 | -38.20716 | 2024-11-23 03:55:00 | NPP-375D | PAU DOS FERROS | RIO GRANDE DO NORTE | Brasil | 2409407 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b0630286-8450-3ba9-bebd-b8f058e0f3bd | -3.54246 | -50.51561 | 2024-11-23 03:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81cfc28e-6794-3f62-8b63-5362bac7e91c | -5.74349 | -46.26186 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43509297-1bff-30bc-ae30-f038f0989ad8 | -4.42141 | -49.11094 | 2024-11-23 03:55:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0259177-c701-39bf-9be2-c2b3b449ec5d | -5.74253 | -46.26752 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README24.md)
