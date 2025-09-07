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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b45e7b36-0edc-36ed-8fa7-febfd2e975fd | -6.59892 | -43.96477 | 2025-09-07 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5df7f6f8-ed30-347f-a143-ff0bb97419cf | -7.02259 | -43.2274 | 2025-09-07 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 482985e9-b919-3635-b66c-4d44f45335f0 | -7.74288 | -48.81904 | 2025-09-07 03:57:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0a09fe2-64e0-3778-87c1-dcad3ab367c0 | -10.60503 | -44.34318 | 2025-09-07 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ebf6f361-ec3e-326e-8e7f-4a8f44fb74b0 | -6.72603 | -45.15318 | 2025-09-07 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00ec9d24-e50d-3796-92eb-7ec353295a11 | -9.59063 | -43.32811 | 2025-09-07 03:57:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 44c5865b-dd6e-316f-af3b-aa92a9558173 | -7.73718 | -48.81791 | 2025-09-07 03:57:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6163d92-5dc3-3f60-b954-52069aebe325 | -6.76453 | -44.21154 | 2025-09-07 03:57:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d0384576-611f-339a-9a81-80973e3c5190 | -7.60857 | -44.66902 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e946f058-83be-381a-b9d9-b7b673cee2a0 | -5.87185 | -46.10176 | 2025-09-07 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2f90728-df7a-3c1d-9427-a2ace4c04951 | -7.40409 | -44.94655 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4224f96-1a15-3281-90bf-acd0a243a17e | -8.5004 | -45.06021 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 096d51db-4d70-3b9a-9d46-614fd800b7ad | -8.9398 | -48.65241 | 2025-09-07 03:57:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5843eaa9-6802-38bd-9eb5-ce0e85acb191 | -6.27086 | -43.49474 | 2025-09-07 03:57:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a944ce80-9535-376e-980a-1d77c168037a | -12.81574 | -48.01347 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4df9f06d-b8fc-3923-bdb7-c7fe56748d9b | -11.15228 | -48.37137 | 2025-09-07 03:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc580b44-04f7-3665-8943-f76de3e5ca8e | -11.15263 | -48.39778 | 2025-09-07 03:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59d34b45-bc2c-3d4c-beb1-2dd2a940e893 | -8.34086 | -48.27714 | 2025-09-07 03:57:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74afa82d-798f-38fa-827a-dfc3204179f9 | -12.00638 | -47.77811 | 2025-09-07 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7c4bdaa-6cfa-31c8-9166-c0b176c876fa | -6.60041 | -43.98162 | 2025-09-07 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c891d63f-0397-356b-b282-6f3a21f19e11 | -6.18857 | -43.36605 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5386d86-0128-3f9b-bd84-ced31b2816ef | -11.40227 | -43.56851 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 97a797c3-07b0-3032-a5be-fe2b6f796d4e | -10.06921 | -49.29496 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| eb007b86-69ba-3e8f-ad33-f2997788fada | -7.74143 | -48.81983 | 2025-09-07 03:57:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3527a1dd-6eb1-3380-8953-441e5dcfaa8d | -6.76521 | -44.20757 | 2025-09-07 03:57:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1f374371-6801-310e-b634-3ad6a84eb1cb | -6.1999 | -43.36755 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f87a85a6-a375-309d-ad68-8d11708112a7 | -6.37475 | -42.98825 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 397c0fd1-415c-335b-8810-e10dd824375e | -6.55968 | -42.9564 | 2025-09-07 03:57:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 506e4b3b-31c3-3532-baf7-ae07ae1dec4c | -10.80851 | -47.72878 | 2025-09-07 03:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b3d5629-8e16-3377-a1ea-cdbe0dd14979 | -11.56894 | -47.7534 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a79a1250-4db6-3d35-81ba-f88b4599ac91 | -12.8505 | -47.99339 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ef585bf-a1d9-39a3-b4fb-50397f5c54d5 | -11.59145 | -37.84615 | 2025-09-07 03:57:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7b738d7d-a67b-3ba2-b526-9d5eafe5ae8d | -6.19905 | -43.59538 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 055046c9-c399-3bd4-a761-1a831c44b449 | -8.48286 | -45.17999 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 124569a7-74f6-3b5a-aaac-aecdd27f4da2 | -6.91985 | -44.3349 | 2025-09-07 03:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d76b8959-43dc-35d0-86be-23cc3240a928 | -6.7044 | -51.4175 | 2025-09-07 03:57:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 719a5f38-65a1-32ca-b50f-8218b151291d | -10.5822 | -48.47565 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dbf75f80-a693-30f5-8f74-bc1679d79a2c | -6.20382 | -43.59224 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44ce9967-47a4-3796-9a2e-fe3360e60a4b | -10.37791 | -44.9661 | 2025-09-07 03:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37a8e21e-795a-3fb6-88a2-4caf79e85625 | -11.58795 | -47.17164 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef42f7e6-3f08-3706-9700-217f88bd52a2 | -8.43106 | -47.30499 | 2025-09-07 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9601dd7-cb79-36d2-b9eb-7e4361dc6ed2 | -7.01102 | -44.94704 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b6e303c-2248-3f10-ab91-af671519ffd8 | -13.06369 | -48.06259 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08e2fec4-c65e-3a0a-92c2-3407175348d8 | -11.14909 | -48.39346 | 2025-09-07 03:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8f79c52-644a-3e36-a79d-9e94472a29f9 | -8.50405 | -45.06531 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8670e2d9-40e4-3a13-9eeb-62472a3b12a2 | -11.84738 | -50.52943 | 2025-09-07 03:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f05d013f-61fe-33e4-803c-2161b5606afe | -6.88552 | -45.59308 | 2025-09-07 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 155d16c2-e4ca-377e-bd47-8f9e01b470c4 | -11.59811 | -47.16356 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 898e60a1-79ee-3983-b571-daebd2c7b66e | -11.59331 | -47.16273 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8bb22844-7aa1-3d09-999b-d68d154a0abf | -13.05048 | -47.12352 | 2025-09-07 03:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b943ec6e-e89d-39af-8084-ad0e7ff5fc4b | -12.93448 | -48.03776 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bce2d676-0b52-3202-8203-0bbeed297eef | -9.8358 | -46.54773 | 2025-09-07 03:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 610b773b-9226-3fd8-918e-97b2ed49039d | -13.01131 | -45.22781 | 2025-09-07 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb02ae35-dad4-371d-a26c-72c439f6b179 | -10.17162 | -46.23956 | 2025-09-07 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 796796f8-af9b-30c3-9294-238ddb05a694 | -5.97256 | -44.73595 | 2025-09-07 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 10c532db-61e1-3284-9589-6a98b86c4d2a | -9.09408 | -46.99207 | 2025-09-07 03:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4376d91d-aae1-32dc-a3de-d52c2dc4dfd8 | -13.00853 | -45.21952 | 2025-09-07 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fd9055d5-213e-326c-8bc0-612e367f6476 | -6.19842 | -43.5991 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9553c8eb-2a38-3036-8de1-fcfe8bbf77c7 | -7.34287 | -44.31264 | 2025-09-07 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 136de0d9-8f1c-3ca9-81fe-d26be4b45c4d | -6.34177 | -43.80096 | 2025-09-07 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a12cd639-9b9a-3428-8bf9-7e3a72b375d0 | -8.45774 | -47.33237 | 2025-09-07 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4bba45b-0b8c-3997-9cc7-bbb949cbd644 | -8.91934 | -45.81444 | 2025-09-07 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 393a0588-2151-3f12-8d04-0bf70eb3e007 | -6.19088 | -43.37745 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fb11de2-66f3-3604-98be-60305a4cdd8e | -11.01982 | -52.04354 | 2025-09-07 03:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4ba97927-e861-3707-b101-92c2f70e4d85 | -7.53907 | -42.52523 | 2025-09-07 03:57:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 80381751-14d3-37e0-a8c3-1712ac105ad2 | -13.02502 | -48.0764 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c72cca86-16ca-3675-a8d2-dbbde945d014 | -8.34697 | -48.27456 | 2025-09-07 03:57:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd651b37-94fc-3842-a7de-991ba4e68af3 | -11.3903 | -43.54698 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6708b6af-db80-3aae-b89e-97d02205e337 | -11.58804 | -37.84561 | 2025-09-07 03:57:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8f1543e0-f454-3b63-9192-dbbc1512c427 | -11.26138 | -46.39997 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3aac1caf-8bd2-331a-b033-a3b5984ec99c | -6.65865 | -44.80648 | 2025-09-07 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7361e20-26b8-3b0a-82eb-f9125b46cf27 | -11.02096 | -52.03791 | 2025-09-07 03:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb9a030c-dc60-306d-be20-4624d5363048 | -12.92938 | -48.03728 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57dd4e3f-0b44-3a36-a78a-e77455379ffc | -12.57492 | -44.62646 | 2025-09-07 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2cd0a78-207f-36dd-8c62-8c124b1ad795 | -7.01616 | -44.95941 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f172b6d8-eebc-3489-a6d9-ddb82f30f2d0 | -13.05264 | -48.06444 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 391c6a16-7d83-3b6f-933e-2ebc739f5146 | -11.94193 | -46.66077 | 2025-09-07 03:57:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c856ccbb-7977-3f39-ad54-928563799109 | -6.38271 | -43.02802 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6b38f6f-8853-3e4b-8526-30b2890f65da | -7.75427 | -48.82127 | 2025-09-07 03:57:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a4e47993-1e9b-354d-9dcf-3ed0d4e25de1 | -10.15535 | -48.74739 | 2025-09-07 03:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cbd4e8c-3ab4-3c1c-b284-2a24e46acb7a | -7.72674 | -44.60927 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62829908-2b42-3504-8bff-61c8c2007197 | -11.39927 | -43.56312 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99130d1d-e33f-32f9-b816-601542d78cc1 | -10.37862 | -44.96213 | 2025-09-07 03:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6da73651-ebe3-3b5e-bd5b-89c482d6cfee | -8.43414 | -47.30448 | 2025-09-07 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b15f16fd-cd5b-3fb7-8632-130ca05cd91b | -11.61357 | -47.16042 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5d50e478-733a-3afe-941e-8b18ad094f0f | -6.72225 | -45.14795 | 2025-09-07 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 446df48f-2ab5-3b37-84f6-76ea73a74e87 | -8.70906 | -47.87061 | 2025-09-07 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18a3127a-656a-3b18-af17-9f5291c4b65e | -5.69165 | -48.14192 | 2025-09-07 03:57:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 65d303ee-bf40-32b1-8095-1711384be68e | -11.60874 | -47.15976 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b64113c3-7f8c-3710-8ed7-e50594cef4d5 | -10.7791 | -46.02365 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2685399b-6c97-3843-9a66-8eb7d33a37ab | -13.04347 | -48.03444 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72d9ce82-08de-32cd-83e6-dbeb7e46afc3 | -11.60291 | -47.16441 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| da58b916-ad5a-3582-a3c7-ba3070b39133 | -8.93354 | -48.65535 | 2025-09-07 03:57:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8ecd758-1754-380c-96a4-7626a96f4d4d | -7.71681 | -44.72453 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75aacab3-1f2a-30f5-9a6c-d646e6a452de | -8.08415 | -44.81135 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 29251018-0f31-30c2-bc52-1a2a37e9e5fb | -11.31013 | -46.54268 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d6d8b106-ee6b-3da5-ac93-ee721f58e447 | -11.60391 | -47.15908 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| dc7ece7e-849a-31a5-b364-5005631e9052 | -11.798 | -44.94462 | 2025-09-07 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 586ea1b5-8d3e-3b0c-9bd1-e7261c15bca8 | -8.89161 | -47.25887 | 2025-09-07 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2a03c31-a399-39d9-b61b-fa8cc9185bd9 | -6.37954 | -42.98389 | 2025-09-07 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README31.md)
