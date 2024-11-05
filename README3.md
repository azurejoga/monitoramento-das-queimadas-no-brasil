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
| f77b8faf-d438-33af-8c6c-243d52af818b | -2.9217 | -49.3335 | 2024-11-05 00:20:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e349f9ad-a9b5-39fa-88ae-7921e383ca8a | -1.5177 | -51.5173 | 2024-11-05 00:20:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fb70a57-ab54-367b-abb9-33e480b7136b | -2.2147 | -46.422401 | 2024-11-05 00:20:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06b261e9-b81d-32d9-a5c7-5996f3e60bbf | -4.2126 | -44.288601 | 2024-11-05 00:20:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 256b9a85-1062-3f91-9c11-80072e23b1f8 | 0.202 | -51.052601 | 2024-11-05 00:20:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| cfa8289f-e23e-3e7d-a8b8-a5fff879e454 | -5.5345 | -44.478802 | 2024-11-05 00:20:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fc6d63b-5373-3e5e-bd24-e18475e6b7ce | -4.3662 | -47.8755 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58f99904-ac3c-3ce5-aafd-665068cff815 | -5.3 | -43.326599 | 2024-11-05 00:20:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc70652d-13d2-3c7f-9c6c-2848fc6eefe9 | -8.3522 | -43.6367 | 2024-11-05 00:20:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 741129b7-0bce-3fd5-a277-e438d9d96824 | -3.826 | -48.9585 | 2024-11-05 00:20:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c8cc3bf-41f1-3960-9b52-d6e3f3d1720c | -1.5158 | -53.479801 | 2024-11-05 00:20:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d213ab47-2979-3532-a73a-b9e2a06abc48 | -4.8954 | -46.700802 | 2024-11-05 00:20:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 551697b9-687c-3000-8a4e-0957d65be974 | -2.8286 | -49.423599 | 2024-11-05 00:20:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2df8c1ad-e60e-33e8-8dab-a423dc2ffcea | -2.6506 | -46.7547 | 2024-11-05 00:20:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c77e76f-3792-349a-85a2-c89f4994a458 | -2.2746 | -46.823799 | 2024-11-05 00:20:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b425bda4-1ca0-362a-a443-ede22d518ee1 | -2.9418 | -54.648201 | 2024-11-05 00:20:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d984e22-835a-38f2-a309-3a536f9e954b | -13.6332 | -44.498402 | 2024-11-05 00:20:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d4b761ec-344b-39c0-9cdc-71b387943438 | -4.3582 | -48.622002 | 2024-11-05 00:20:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02f43f68-a052-3a8d-9e20-b1439ab71f99 | -4.3778 | -47.238998 | 2024-11-05 00:20:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 318f0735-f9c5-3c99-aeba-29e627a0b820 | -4.8132 | -43.2271 | 2024-11-05 00:20:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffc61982-afe2-378a-a811-63e530513a5d | -1.0388 | -47.786098 | 2024-11-05 00:20:00 | METOP-B | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9e5f49a-d56b-3895-b68e-833407060478 | -4.247 | -48.032799 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3febca84-4d68-3fd1-8137-2c3ddda79ec7 | -11.9888 | -42.895802 | 2024-11-05 00:20:00 | METOP-B | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 61de2026-b437-3a14-a9b1-210ce8d73944 | -1.1456 | -52.012001 | 2024-11-05 00:20:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| da873d68-ad44-3f14-9101-d2aa8e2bc383 | -4.1405 | -46.826 | 2024-11-05 00:20:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64dca3ad-910a-3fa7-b223-d2827b6d8ff6 | -2.7925 | -51.427898 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f7d3a01-ef9c-3c8e-be4b-52bb13c8c467 | -4.0204 | -43.2299 | 2024-11-05 00:20:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1460e865-883a-33b7-955d-7a02f4c7a33e | -6.5222 | -45.917999 | 2024-11-05 00:20:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9094bf58-6e0a-3268-9814-22de46fa1e25 | -2.2305 | -46.6744 | 2024-11-05 00:20:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65187775-5e05-3beb-81e9-5c6135bd4386 | -4.4225 | -45.840801 | 2024-11-05 00:20:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1c4cbfba-f694-3c7d-bf27-7b613ca0734b | -4.365 | -47.2276 | 2024-11-05 00:20:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3c4990d0-d9a7-3a19-ac58-61400de9e9cb | -1.3983 | -52.1768 | 2024-11-05 00:20:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2adbb74c-688b-3308-b3f3-c9636524549b | -2.229 | -46.6675 | 2024-11-05 00:20:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8afe5d60-9b7b-35b8-b1cb-fca6acb45000 | -3.0958 | -50.251301 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c18fe4e4-f97c-374e-841a-2a226f805ae7 | -3.4656 | -45.530899 | 2024-11-05 00:20:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 207d8ac5-d8d5-3df3-8453-29a2dd3e173f | -5.9296 | -43.641899 | 2024-11-05 00:20:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 652667ce-9e86-32a6-a323-a164f1ba3917 | -2.8125 | -51.471699 | 2024-11-05 00:20:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b073158e-abe6-31dd-9c40-352774e63182 | -14.5549 | -42.741699 | 2024-11-05 00:20:00 | METOP-B | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f81b4f04-4e85-3744-8b88-54b970990d0a | -3.2573 | -50.699799 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fa91366-8390-3137-8669-99c394d7c323 | -4.3818 | -43.099499 | 2024-11-05 00:20:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0c6d2ea-ce8e-371a-bf74-f16d76d68a2c | -4.7572 | -44.550999 | 2024-11-05 00:20:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 70a46c54-abe8-3032-ada9-4fd703d418f3 | -15.549 | -43.162102 | 2024-11-05 00:20:00 | METOP-B | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 0dc38dfa-1b4b-3b42-a1c2-94999dfcfa30 | -5.5664 | -42.3004 | 2024-11-05 00:20:00 | METOP-B | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 67cc0e3a-55b6-366e-a371-ca5c69a983fa | -15.0258 | -42.2771 | 2024-11-05 00:20:00 | METOP-B | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 114a64f2-e3d3-3b35-9859-a1ac56326cff | -4.8856 | -46.702999 | 2024-11-05 00:20:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 393f0b18-797e-3cec-83bd-4f6fbde2ae87 | -4.4014 | -43.095001 | 2024-11-05 00:20:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f03a33b9-df1a-30f3-bddb-3dac132518f8 | -8.32 | -43.586601 | 2024-11-05 00:20:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fb591086-41c4-3537-9fb0-f15627262abe | -4.6614 | -43.819599 | 2024-11-05 00:20:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab14ee35-efcf-324f-8a10-020414097d8b | -5.5328 | -44.471199 | 2024-11-05 00:20:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9718bfc-8100-38a3-9a75-faccac1589a7 | -0.8011 | -48.6054 | 2024-11-05 00:20:00 | METOP-B | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7913963-b94e-3aa6-bc7b-b389071935b0 | -2.9503 | -45.4856 | 2024-11-05 00:20:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b374b022-bb04-3ddf-8ee3-e081c8c6a6d2 | -10.9061 | -41.887501 | 2024-11-05 00:20:00 | METOP-B | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 390cfff9-4bc1-320e-9877-2c3031db3a40 | -3.9163 | -45.835701 | 2024-11-05 00:20:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 71afbe53-3bf1-3606-b681-547fafa9af16 | -10.873 | -44.7822 | 2024-11-05 00:20:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5004375-5337-3e2d-bbb7-b74ca630e523 | -2.2222 | -46.683399 | 2024-11-05 00:20:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d34c7705-122f-30fd-a3cf-124d3acd1233 | -2.813 | -52.907501 | 2024-11-05 00:20:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70007b8d-f419-39e4-b240-0f7fc00f7b04 | -3.9749 | -48.151199 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f6eb4fd-092a-3f5f-ad5b-a4f3eb34f800 | -4.561 | -47.825199 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2fd9609-ef9f-351a-aa5c-75d6df5aee55 | -3.102 | -50.233101 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50617769-49a8-3d61-ab64-496bf5b99b25 | -3.0662 | -50.487701 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a760a3d7-8f8c-3749-8b09-7dd2c136b3dc | -3.1821 | -50.5928 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 846f5f43-886a-3ccd-94d5-5e26fe608d05 | -10.9082 | -41.896301 | 2024-11-05 00:20:00 | METOP-B | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 524ffa01-188b-3d80-804d-db79c51afd2a | -3.0785 | -54.480202 | 2024-11-05 00:20:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8857cf20-08d3-3889-9416-9f49ba677495 | -3.9583 | -48.352901 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68371038-a157-382d-899e-886b2728b380 | -4.1173 | -47.959499 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd34b912-b998-3645-b591-abf855cdb852 | -3.4894 | -48.2365 | 2024-11-05 00:20:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f622eca1-a653-3ed5-8a70-1c12bf409223 | -10.3719 | -45.074001 | 2024-11-05 00:20:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a23d548c-35f3-36e1-9680-0401e8f70f04 | -3.6449 | -50.131401 | 2024-11-05 00:20:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da253f85-2f7e-3e73-aa1f-fe3611d5438a | -6.1036 | -43.9492 | 2024-11-05 00:20:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc0e0ae9-a1b3-3d3f-8b80-926a4fd78e6c | -4.0357 | -48.284401 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 292cb536-d78e-395a-b0be-06f16b536891 | -5.3747 | -46.450001 | 2024-11-05 00:20:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 01063dfc-e25a-39d9-b07c-2c14f916179f | -2.6539 | -48.552399 | 2024-11-05 00:20:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a6905fd-63f7-3eb0-9508-6eadb9a1631a | -6.5253 | -45.931801 | 2024-11-05 00:20:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5216ae4-8d2f-3d06-b948-582378232b18 | -3.6991 | -44.611698 | 2024-11-05 00:20:00 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54ed1432-b298-3918-9c68-4fd578906e91 | -3.4738 | -45.5214 | 2024-11-05 00:20:00 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 49150cdc-073e-376f-b414-4709fd2fe642 | -4.386 | -43.117599 | 2024-11-05 00:20:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6bf56018-3000-316d-8557-d05af5552f87 | -5.0581 | -44.1548 | 2024-11-05 00:20:00 | METOP-B | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e114842-4317-399f-9646-a4579998482c | -9.7855 | -43.857101 | 2024-11-05 00:20:00 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 09d0cdce-5f32-32d0-97dc-c872e455d4bc | -8.4953 | -42.0826 | 2024-11-05 00:20:00 | METOP-B | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 00c23488-960e-3cfb-af52-ad9a541e1aa6 | -5.6877 | -45.828602 | 2024-11-05 00:20:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b967e129-18d1-31e3-bb65-57856b3774dd | -2.8006 | -51.4646 | 2024-11-05 00:20:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f2ae9d7-ddf6-3cfa-a38c-093507d6c6f3 | -4.7419 | -45.205601 | 2024-11-05 00:20:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af095b49-22f3-3891-8e46-768e78b71684 | -8.3334 | -43.599899 | 2024-11-05 00:20:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ecf10d15-0a67-33ba-9f1d-d2bfe139b721 | -5.4842 | -47.1656 | 2024-11-05 00:20:00 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f111523c-0023-3f96-9b89-22ec763cc9c9 | -2.2828 | -46.8148 | 2024-11-05 00:20:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a52f842-1b47-324a-b70d-b7c4b354d7cc | -13.6348 | -44.505501 | 2024-11-05 00:20:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a9b34d5-a3c0-316d-bd27-5f9570db1319 | -4.0593 | -46.922901 | 2024-11-05 00:20:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30e110f1-2b45-3d8a-a289-ad72700a8387 | -4.1249 | -46.894001 | 2024-11-05 00:20:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9c90dcdc-82bf-337e-9d8d-5e930521e907 | -3.2415 | -50.536098 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf175310-cce3-3add-8d02-e5cc6b5d2407 | -5.8377 | -43.645699 | 2024-11-05 00:20:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c574b0d0-dc0e-3482-a628-b43825e91174 | -4.0713 | -48.305901 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1207143e-841d-388e-995e-bc32a8221b3c | -3.8994 | -48.365898 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c11d448-9807-337b-a9ec-052f5f3c9ca0 | 0.21 | -51.062801 | 2024-11-05 00:20:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 531d9715-9c0e-3b2f-bb1b-bd62a84e5824 | -4.2346 | -48.529301 | 2024-11-05 00:20:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1ca2bcf-8da2-3581-9c81-ea68e4aa047d | -6.1017 | -43.9412 | 2024-11-05 00:20:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b35ed0ea-6d7d-33a0-a679-5dc9f6fc7fdb | -4.0259 | -48.286598 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e7eac76-f353-3127-bb4d-086bba063308 | -10.2782 | -42.422501 | 2024-11-05 00:20:00 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0ec803eb-1f3f-3405-ac5f-d04dca6c137e | -3.5639 | -47.376598 | 2024-11-05 00:20:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb01da94-3a65-3288-a145-cec4f9dd5212 | -4.7179 | -46.4165 | 2024-11-05 00:20:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0d5a084a-bfb5-35cd-92d1-de9a6f378484 | -2.6555 | -48.559399 | 2024-11-05 00:20:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
