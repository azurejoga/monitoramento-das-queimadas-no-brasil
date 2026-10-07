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

## Dados Diários - Página 211

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4e08476-9f36-3813-867b-edd41a49cb1a | -11.00124 | -45.42881 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ffc3fc4d-b912-3da8-b207-cc30b0b83a10 | -16.19328 | -44.5659 | 2026-10-07 16:37:00 | NPP-375 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f5b8087f-abb9-3621-b03a-fc61a48e66fd | -3.91796 | -44.13678 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 51d10f82-a37d-3869-b320-fc8c299c62a0 | -3.77085 | -41.78373 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 764d7737-56ab-3c2c-bb33-90f1be0808cb | -10.99535 | -45.48637 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e5fa98cf-2641-3341-a670-6c0154daf72c | -6.04589 | -53.48677 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 2bee44df-8b7d-3030-b864-0c37ad854671 | -5.50805 | -42.83194 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 8c6dfec6-ce79-3650-a474-cad5d9753aff | -5.8351 | -53.53072 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3483ec80-e54e-3a83-b0a6-d3d58226cfc7 | -5.48998 | -42.84946 | 2026-10-07 16:37:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 55.9 |
| b0e521eb-ef12-380a-a2f1-8635bcf650a2 | -7.18587 | -55.11137 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 1c7e2dbb-4a89-38a0-b10e-655562b743f1 | -5.77175 | -38.55651 | 2026-10-07 16:37:00 | NPP-375 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 5c7cf234-711b-3eb5-bb91-94f5b3d67159 | -6.65372 | -43.76555 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4a7cee6f-28d6-3e75-96c0-83b39bc2895d | -3.86026 | -42.23257 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| e0a50823-b4d8-3819-bd5b-17a95ad81b6a | -5.96559 | -40.92646 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 210.3 |
| 93b34057-9cf4-3d33-ba2d-7c51208bd6d9 | -4.5738 | -40.72136 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 19.2 |
| b5ea13f8-e016-3524-bb30-914473da7da0 | -5.17046 | -42.68008 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dd0759f3-e761-3aed-b882-5153a47883d2 | -6.59479 | -47.40086 | 2026-10-07 16:37:00 | NPP-375 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b6f4630d-e856-3ad1-bf40-41c6a2194612 | -11.44437 | -47.66156 | 2026-10-07 16:37:00 | NPP-375 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2f4cc7ed-ef5d-3909-a919-f5285348388d | -9.20346 | -46.69616 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| fa9c7832-678f-3940-8da4-1de090b234ea | -5.72825 | -45.14757 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 90da12bf-9e02-3d5a-b7b1-8a1d2f079bf6 | -7.76074 | -54.94151 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 675a544f-d62d-3178-9de6-f541867390ac | -3.20972 | -42.95684 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2823a1d4-05c1-3827-bc94-bce01c4bbc00 | -5.71417 | -41.68427 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| bad237a6-e6a8-3847-95b1-7c48d8f6f447 | -7.21218 | -55.12116 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 7ddcc219-4693-35ae-ac6a-ce2fae4ca013 | -6.33592 | -43.745 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4b42e285-775b-3788-b1e9-71a0f1e602ce | -15.9733 | -40.70348 | 2026-10-07 16:37:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3e0fa698-1a12-3df0-be19-62615e9b4eda | -6.58423 | -41.5974 | 2026-10-07 16:37:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 29.7 |
| c6b22b8c-dbd3-3810-ae84-8a97e2f1e13d | -17.0155 | -45.90667 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 9136ca8a-4e82-3b30-928e-739c1b19f28c | -7.55769 | -47.77871 | 2026-10-07 16:37:00 | NPP-375 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9056030c-d970-34f8-9919-0cf3d5455a26 | -6.06347 | -35.52862 | 2026-10-07 16:37:00 | NPP-375 | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 2a6bbe39-c0ee-36da-8643-c1d839e9db9a | -6.21852 | -52.78556 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bda79979-0750-3df7-8ae5-20a12559644f | -6.05526 | -53.47489 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c977183c-d365-3df9-aec6-ccb1d9c05ab6 | -6.98186 | -40.04072 | 2026-10-07 16:37:00 | NPP-375 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1bd6cac5-f554-3c78-a054-0c64bbad1b76 | -8.22795 | -37.04125 | 2026-10-07 16:37:00 | NPP-375 | SÃO SEBASTIÃO DO UMBUZEIRO | PARAÍBA | Brasil | 2515203 | 25 | 33 | nan | nan | nan | Caatinga | 5.8 |
| eb64c577-8568-3ece-839b-a578bff8cb33 | -6.71736 | -44.11441 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d34a60fc-d298-344d-bfee-fa27434c0e12 | -7.20552 | -55.12515 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 0d3b1f39-3293-3263-94e6-897c97c0ef51 | -16.13106 | -43.74782 | 2026-10-07 16:37:00 | NPP-375 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| af0b49e7-bfc2-3546-9bcd-772339872bf1 | -6.31555 | -43.48357 | 2026-10-07 16:37:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7abfe16d-64c9-3890-9737-50672393072f | -5.73707 | -45.16062 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 3b92cb54-e1e0-3824-8cb2-83fb9405b474 | -3.21192 | -43.68863 | 2026-10-07 16:37:00 | NPP-375 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 664297ff-6ec5-3fe2-8dd7-c3dbcdbe85fc | -6.02505 | -51.72038 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bada598d-e8de-30d1-981d-c4a23804833c | -7.49282 | -44.43653 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8e84f53c-c9d2-349c-bfc7-645eaedd882e | -7.90075 | -54.72082 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| eb590ccd-a54d-3d89-beea-5fef8854f243 | -9.58833 | -48.91772 | 2026-10-07 16:37:00 | NPP-375 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cfbf5da6-0d3a-3c87-aea3-0624b855d52f | -3.8602 | -40.22758 | 2026-10-07 16:37:00 | NPP-375 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| dadf8d76-3d87-3593-9a65-7d43aad6c64d | -7.10947 | -55.72373 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1bfeb24d-4679-3570-bd80-d454a4fe4973 | -6.44806 | -52.67426 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d84ea1b0-de1c-3253-948c-6e5c23b016a9 | -14.85088 | -42.06488 | 2026-10-07 16:37:00 | NPP-375 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 364ebe09-6d4a-394f-8d76-dee7c66403e4 | -3.94478 | -38.49729 | 2026-10-07 16:37:00 | NPP-375 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b1a5b8f1-5585-3b15-abf9-f45e1fd54b7d | -9.95764 | -45.96856 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 83df3a85-8cad-3ab5-879e-a5abd2cca942 | -10.35511 | -46.25447 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| e19a6112-ee2f-3ad2-ac78-da12cbd80545 | -5.73182 | -41.74966 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| fb0dbaf7-9e60-39a0-abce-ac1d7367128f | -10.91906 | -49.61995 | 2026-10-07 16:37:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4f16743d-f1cc-35bf-98ff-fbfdbeb2a6fa | -7.6 | -47.0244 | 2026-10-07 16:37:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 44.2 |
| c0dfb137-09c3-3cb5-93d0-b57979de34d1 | -6.24458 | -53.4632 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9716424b-a2dc-3ef7-98b5-15d0d24fad61 | -6.46755 | -55.46862 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 80ff9ae9-ee20-30a6-8273-ec52af9b44e9 | -8.07433 | -55.29049 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| bc90abcd-c576-359a-a347-b17d25cb23ea | -4.11671 | -41.77756 | 2026-10-07 16:37:00 | NPP-375 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 59.0 |
| 32167ef3-38f1-3b80-8ce6-bec7b795b79f | -7.09612 | -45.3188 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f97ddddc-9971-372e-ac2d-10e16dfebe1d | -7.61807 | -40.48356 | 2026-10-07 16:37:00 | NPP-375 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| fe4ef8c0-945e-3663-a39c-ca818231015b | -7.97619 | -46.9257 | 2026-10-07 16:37:00 | NPP-375 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9f45ea1e-ccdf-3731-ad12-d01fcdcf9e23 | -8.79078 | -47.57966 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d1f3475b-d91c-3f90-921e-0c717a3bf018 | -6.15763 | -52.64992 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0e05fab-0872-31b7-810c-65f124bdc745 | -6.2476 | -44.87272 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6517e6e3-4dae-3f80-9fd0-a3eeb0e2f4ac | -16.97627 | -45.47275 | 2026-10-07 16:37:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f5c5bc25-2c43-32c2-b11e-38fa090d7f35 | -11.06236 | -45.84782 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 221984c4-1da9-3b34-9ffb-fd1a205ad26d | -3.76727 | -41.78429 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 662a2871-afb2-3747-a6f9-d7cae79a3517 | -7.2136 | -44.29128 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 42d55f11-e8ec-378f-90a0-4f76ae44f6d3 | -15.78859 | -40.68652 | 2026-10-07 16:37:00 | NPP-375 | MATA VERDE | MINAS GERAIS | Brasil | 3140555 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 73343252-2161-34df-ac66-d02172637406 | -9.92379 | -44.81071 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 596515ba-cd7e-38c7-a75d-95ce5aa18ee5 | -6.37059 | -43.33176 | 2026-10-07 16:37:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 15967834-99e4-38e4-ad67-ff953d9b431f | -10.3641 | -56.44337 | 2026-10-07 16:37:00 | NPP-375 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 80d69964-8175-31e5-a144-4090f4e6ad8c | -10.88717 | -46.67934 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 264a6f7f-384c-3fb5-bd58-ac1e065686d2 | -5.93606 | -46.63342 | 2026-10-07 16:37:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| b7b20e2d-b74b-30b3-b110-888b8d6efc76 | -6.36946 | -42.91495 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 3e9da438-5cd7-388c-a364-7ae429c1e27e | -8.01064 | -47.1866 | 2026-10-07 16:37:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 4d01ad88-9037-30e7-a440-b0bb68451244 | -11.35825 | -46.64368 | 2026-10-07 16:37:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 993e8bf0-a819-3779-ae91-5fb4642e4be2 | -9.39853 | -47.33732 | 2026-10-07 16:37:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 31e91299-289d-3d16-82bf-402b99418101 | -6.48364 | -52.814 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0b98393f-a96b-3e1b-8c47-eaf5e776124e | -6.20347 | -40.8033 | 2026-10-07 16:37:00 | NPP-375 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 7f14fabe-e359-372e-bbdb-c6f7b27cab4b | -16.70788 | -41.87975 | 2026-10-07 16:37:00 | NPP-375 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| dac4d092-8cbe-3548-bbf2-8c9e8388e211 | -5.49225 | -42.84175 | 2026-10-07 16:37:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 37.2 |
| 51e34e25-7ee0-336f-944d-ab28f90e51ab | -6.5509 | -44.09027 | 2026-10-07 16:37:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f816e7a-e571-3806-b099-f2f132a6b0d1 | -9.96414 | -45.96349 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 109eb8ec-8ea1-3579-a6e9-f5bb8e83c42d | -15.88947 | -40.7256 | 2026-10-07 16:37:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 678bfc04-6ada-3f9d-b7c8-8af5eaa68d71 | -5.86928 | -57.67462 | 2026-10-07 16:37:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f25bf1eb-057d-3035-a0cc-2c901d2ae857 | -11.17175 | -49.48177 | 2026-10-07 16:37:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 805c0439-3e39-3e7a-98bc-a06a27f6acc6 | -8.99972 | -45.93701 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 3cb879fa-4b3f-3b31-be6a-f226da37145f | -6.14289 | -51.69854 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 4eb1dd97-9f0c-3d37-972b-bea87647f01b | -4.3657 | -41.82208 | 2026-10-07 16:37:00 | NPP-375 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 79558ac8-c5fa-326d-b048-14efd2ae93ec | -10.70957 | -51.94408 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 53c72657-3643-3e70-8220-91f23f18d5ae | -16.05978 | -39.85334 | 2026-10-07 16:37:00 | NPP-375 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 4e736ca8-75a7-38f5-af79-32edac0ac020 | -6.19675 | -52.81961 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f0b9713b-ad78-3814-a4f6-b5bddbcfac66 | -7.76863 | -48.2412 | 2026-10-07 16:37:00 | NPP-375 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 047edca6-1490-35e4-b7b7-1abc7ddc702d | -6.0097 | -53.50503 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 57bb0181-22d7-35c2-9f4b-224dec6d23c4 | -8.43112 | -49.87591 | 2026-10-07 16:37:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d02ecaf9-3386-3542-b412-3b8d6e21c6a8 | -4.20751 | -44.61486 | 2026-10-07 16:37:00 | NPP-375 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c655f602-8032-3f5a-8069-d8d738c829d6 | -6.38013 | -42.53394 | 2026-10-07 16:37:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 989017b7-e2e5-33aa-b0e4-108d75d522cd | -6.68079 | -44.94476 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b94e8866-64c9-3b1d-9ef1-d100ed18b58c | -6.13536 | -45.46994 | 2026-10-07 16:37:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README212.md)
