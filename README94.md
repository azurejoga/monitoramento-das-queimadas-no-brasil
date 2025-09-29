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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0e6ceb1-1771-3c07-a1d4-40808fec854b | -13.5933 | -48.0593 | 2025-09-29 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 94.3 |
| a54699af-cc21-3633-bb7e-e017a17438ac | -11.4405 | -45.0461 | 2025-09-29 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 866911f2-59b0-3e89-89ec-5eba3f2c31a0 | -15.6127 | -46.2465 | 2025-09-29 13:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 364c8c26-e367-3789-9ff3-83b9ed84260f | -8.1614 | -46.3899 | 2025-09-29 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 6b5cb8b6-3529-34bb-a356-26fe9e6df8ed | -10.4022 | -48.1476 | 2025-09-29 13:50:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 86c1d6c9-7a87-37de-b177-d4562bfea8be | -6.3154 | -43.4548 | 2025-09-29 13:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 224e6f4d-f82b-300e-93fd-0387ecb5f6ca | -7.9006 | -44.6035 | 2025-09-29 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 35d652c7-598f-3816-a7a7-44377aff3710 | -7.8019 | -48.3173 | 2025-09-29 13:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 7e018229-de30-3c60-b7d1-1fce5633cdca | -7.281 | -42.8505 | 2025-09-29 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 00b2d556-1664-3e9a-8851-166edfef0578 | -6.9695 | -43.7695 | 2025-09-29 13:50:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| e64c45b8-f7e0-3d32-9ad6-afbdca542876 | -11.5054 | -43.5426 | 2025-09-29 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 305.1 |
| dd4a6a82-707d-3d59-83e4-304e85cac0e3 | -14.7176 | -45.2057 | 2025-09-29 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 341.6 |
| 78a9b774-20b9-34a7-a9ae-1be434bcb80f | -9.7451 | -47.8027 | 2025-09-29 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| def3cfe7-b893-3602-bb3f-c024ff282885 | -8.2665 | -45.4791 | 2025-09-29 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 729d3386-3e1b-398b-9b2e-78edacb8aa10 | -9.3708 | -47.556 | 2025-09-29 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 6c801b10-2cbf-3656-b302-44b1334ce3ea | -17.7344 | -46.6823 | 2025-09-29 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 778ae1c3-727e-3a71-ac88-c2526501da96 | -14.8906 | -51.0461 | 2025-09-29 13:50:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 26b5afc6-80de-371a-9936-e2bb84bc6eeb | -9.2821 | -45.733 | 2025-09-29 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 4f358799-3af1-3d8c-b272-10d35c8d85bb | -17.7144 | -46.6865 | 2025-09-29 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 189.8 |
| a46f0b80-af35-3ffb-bfb0-5fc55735e413 | -4.5798 | -37.8505 | 2025-09-29 13:50:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 101.9 |
| 0f0fc735-f056-3c0e-a029-a139963797b9 | -7.8163 | -47.0003 | 2025-09-29 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 1c528dad-5eb7-3f90-9ed1-b046e76c25d0 | -9.1102 | -45.8653 | 2025-09-29 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 9441fb2d-a382-3d2e-ad67-96b69e5180ce | -13.3989 | -48.1549 | 2025-09-29 13:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 1792a920-99c8-3d23-a1e3-80583899e3c1 | -13.7695 | -47.9211 | 2025-09-29 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 01e52f6d-0e01-399a-ba37-dce0c9025941 | -7.4488 | -46.299 | 2025-09-29 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 540.9 |
| 77d09a4a-0e4d-37cb-a8b4-85004fc398ef | -8.2848 | -45.5225 | 2025-09-29 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 206.1 |
| c974dcfe-e592-3cb1-bf95-1beb90ed6c48 | -6.2979 | -45.2475 | 2025-09-29 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| cfec5203-b6d5-354d-b663-b2e25fd9060b | -7.6062 | -47.3498 | 2025-09-29 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 7ec69731-0683-3660-87c6-4dbc377c81f3 | -12.9732 | -45.2051 | 2025-09-29 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 135d0363-a4e2-3bc0-9e03-733f5b6282dd | -9.7454 | -47.7806 | 2025-09-29 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| f39f2290-7502-369c-b9a0-d2bb9306706a | -11.3447 | -45.0597 | 2025-09-29 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 0051d7e2-9a52-3546-a84f-f1d3fd56a0b2 | -6.7482 | -43.3704 | 2025-09-29 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 63.3 |
| d2b878de-c62e-3ac1-a572-0687405e10ce | -9.0016 | -51.6875 | 2025-09-29 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 205ad306-c5fa-38a8-9232-bd19340f5bbe | -10.8055 | -45.3637 | 2025-09-29 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| e4fc11ae-9de1-32a7-b384-ca36a6e366c8 | -7.2999 | -42.8486 | 2025-09-29 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 91cd390a-5795-34fe-b0bb-d98913f909bc | -6.4131 | -43.0724 | 2025-09-29 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 7fb1d026-eecd-3eeb-989d-d07c9da1cf2c | -9.7674 | -46.1971 | 2025-09-29 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 53cb138d-0eec-3293-8237-7bf76d8c9d6e | -9.4007 | -54.6984 | 2025-09-29 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| cd9510da-dacd-333d-b66c-d09ad43622f1 | -7.8375 | -46.7766 | 2025-09-29 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| d26f45e1-7f2b-3c22-a201-db8734ae981a | -14.8693 | -47.2032 | 2025-09-29 13:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 4f12050f-46e5-3abc-9017-abc75414c648 | -7.5089 | -44.297 | 2025-09-29 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 31c175b2-3f55-3bc4-ac1f-1d8c010c2fb7 | -7.4573 | -47.2523 | 2025-09-29 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 508f868a-4d39-3eda-9751-3dff872a9301 | -14.698 | -45.2093 | 2025-09-29 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 399.7 |
| d0d39fae-1c1e-3ea7-a594-a17a6f7f9adb | -9.301 | -45.7309 | 2025-09-29 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| bc7690c3-686f-3d24-ae4e-e8c8e98afca3 | -8.9456 | -51.6712 | 2025-09-29 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 3ce3935e-d21a-3166-bbb7-0493b5ae3678 | -5.4258 | -42.2797 | 2025-09-29 13:50:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 18de0039-8e4a-3fa3-a1bd-2c73d14bcdab | -7.2214 | -44.783 | 2025-09-29 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 217b91bd-2846-3756-86be-12eddaab3285 | -12.3569 | -43.2162 | 2025-09-29 13:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| dbc2b351-2438-3369-a6b2-b3824ecd9df0 | -6.0784 | -44.6961 | 2025-09-29 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 987725f2-3049-3d51-bc19-2e25bd50748e | -7.6064 | -47.3278 | 2025-09-29 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 4915b0cc-5259-3e12-82fa-3861109570e7 | -6.4317 | -43.0942 | 2025-09-29 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 524073cc-4dc3-30fe-951f-71198be17436 | -8.2662 | -45.5018 | 2025-09-29 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 884a4ff1-787e-30a8-a4a9-08fb7bc6b94f | -22.6077 | -49.0351 | 2025-09-29 13:50:00 | GOES-19 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 137.8 |
| f4582ef1-3ae2-34b5-a51b-c3f39b7809ce | -9.7864 | -46.1949 | 2025-09-29 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| dc6a10e4-c37f-3c4b-92c1-0a5aef5e3fdc | -9.4194 | -54.697 | 2025-09-29 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| fc00a5aa-b9dc-3437-a707-0fe699c62ca3 | -14.8902 | -51.0678 | 2025-09-29 13:50:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 113.5 |
| c04d1be5-d65b-363b-9a81-3567cb7f13e8 | -11.505 | -43.5663 | 2025-09-29 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 85dcf3fe-9588-3517-8a03-f6d212bf0f40 | -7.5538 | -45.2989 | 2025-09-29 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| de297ce3-b932-37bd-981c-401c968cfd1e | -7.8378 | -46.7544 | 2025-09-29 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 1c9e74f0-08d2-3044-a1d2-4feaee1cce2d | -12.887 | -44.6846 | 2025-09-29 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 3b1641fe-f21b-3c1c-88db-66614a982056 | -7.6275 | -45.428 | 2025-09-29 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 64a5fbb8-0afa-3611-b648-3a2e7a8f43de | -8.5221 | -44.6535 | 2025-09-29 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 1231c67d-ae91-33c6-a1f1-31278e757a00 | -7.8165 | -46.9781 | 2025-09-29 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| c0a0dcde-fc1d-3d03-aff0-e7cb0044b7b4 | -9.1105 | -45.8426 | 2025-09-29 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.1 |
| d0ebd355-e92a-3fe6-9d07-4963c6496f97 | -10.823 | -46.6538 | 2025-09-29 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 6e176d7d-9bd0-3182-a693-208515cad7a4 | -17.4055 | -47.1199 | 2025-09-29 13:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 109.4 |
| c3681eb7-a672-3308-a013-75e10399b8c1 | -9.7945 | -46.9557 | 2025-09-29 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 4fe714c5-1313-39f1-aa89-88567929ba70 | -9.764 | -47.8006 | 2025-09-29 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 8f1d800a-39a6-3b2a-a812-eb683546f00e | -13.2346 | -50.9691 | 2025-09-29 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 3fbcdd7d-cc65-3767-ade3-e0e4d643d1d1 | -11.9059 | -48.0298 | 2025-09-29 13:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 133.6 |
| ac1404d4-d9a4-3cc0-bdb0-f08378221457 | -7.8563 | -46.7749 | 2025-09-29 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 1dfeadfc-a074-385f-b9b7-5f232e5c4c20 | -8.5413 | -44.6284 | 2025-09-29 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 113.7 |
| a3f81674-7837-3ea3-baf7-41621bab36d1 | -6.0609 | -42.608 | 2025-09-29 14:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| f6696705-074a-32ae-9009-a7e382dead8d | -6.5599 | -43.4105 | 2025-09-29 14:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 52.9 |
| 22d333e6-c7a4-314d-a843-f304ba91caa4 | -13.5933 | -48.0593 | 2025-09-29 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 131.9 |
| ccc90b8d-7043-3d8c-ab19-74ea8ed7396d | -7.9006 | -44.6035 | 2025-09-29 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 62f8cb76-b28e-363b-bcf6-edaabf6c4cdf | -7.7414 | -46.9848 | 2025-09-29 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 2937f935-39f7-3007-bdcf-3c07ce1f4537 | -13.38 | -48.1354 | 2025-09-29 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 81b6f728-09b0-35ad-a588-abe5920e8b6b | -6.0623 | -42.466 | 2025-09-29 14:00:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| dd56fbde-60c5-337a-8b81-670c17029b22 | -11.925 | -48.0273 | 2025-09-29 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| b665126c-5cff-323d-8183-77ac06fb91e5 | -8.2848 | -45.5225 | 2025-09-29 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 232.3 |
| 62bfcb25-210a-3d3a-9368-d119974fbcea | -9.3013 | -45.7082 | 2025-09-29 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| e837efb8-7459-34c5-8d02-bfdc5332f3e3 | -5.3507 | -42.2854 | 2025-09-29 14:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 121.3 |
| ec2d7a7f-5b2f-3a5c-812f-29fb1dbbd354 | -10.3896 | -49.0437 | 2025-09-29 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| f7d01ba3-95a7-3550-8ece-1d5b9ca65172 | -10.6429 | -48.5364 | 2025-09-29 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 2415a8ae-a667-34d6-b0f6-964d25ae6970 | -5.7413 | -42.6576 | 2025-09-29 14:00:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 4b20b964-5457-3711-8746-9b6b351f0850 | -8.5224 | -44.6305 | 2025-09-29 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 266a4174-81f9-30d1-aaf7-09622ab75c2c | -9.3199 | -45.7288 | 2025-09-29 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 9065669b-e314-3eb1-bed4-a29af7526341 | -9.7264 | -47.7827 | 2025-09-29 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 8a427950-9e8c-305f-a743-29ffa187c8c1 | -5.7681 | -43.8235 | 2025-09-29 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| f2b7155e-e7e7-3840-a746-4bff27d48386 | -11.9059 | -48.0298 | 2025-09-29 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 02502a77-d3f0-3015-a9bd-650c8fad4250 | -7.9008 | -44.5805 | 2025-09-29 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| e41c8f0e-55ba-3c61-b9a9-94d81ba3dd8c | -11.4409 | -45.0229 | 2025-09-29 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| adabc32b-296b-36b6-b109-525b21c2ab78 | -7.8019 | -48.3173 | 2025-09-29 14:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 4bd05ea7-4b97-3a03-a2a0-4743d58e564d | -9.4194 | -54.697 | 2025-09-29 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 3c859ca9-bc4a-3872-ac00-4f408f4d77dc | -11.383 | -45.0543 | 2025-09-29 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| cde7f6a0-a22d-3110-8053-827546e7d23e | -9.3708 | -47.556 | 2025-09-29 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ba007b77-029d-3020-a712-d2fe99e9021c | -10.2406 | -50.2857 | 2025-09-29 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 43be8020-8035-3e25-a5e4-1f60a99bd6d8 | -7.7416 | -46.9626 | 2025-09-29 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 9b355cf1-1ff2-3b33-998f-3d5aafc9f84b | -5.9185 | -45.839 | 2025-09-29 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |


[Clique aqui para ver as próximas entradas](README95.md)
