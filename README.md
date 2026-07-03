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
| ed9eaefd-e69c-3b0e-b347-9c6668e88165 | -17.2639 | -42.6527 | 2026-07-03 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 102.5 |
| cf8a42bb-ab5e-3b7c-8d86-29abb9516e4e | -5.7943 | -45.0813 | 2026-07-03 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| cc9998ff-9d4b-3879-91da-1875f8415017 | -5.8132 | -45.0573 | 2026-07-03 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 4730a4c7-7225-33c0-be78-13e6c2cd5443 | -8.7399 | -48.3205 | 2026-07-03 00:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| e62dfd51-ddbc-39a2-9932-bb97940ba835 | -12.7548 | -44.5428 | 2026-07-03 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| ee8e8a63-d19a-3072-a0fb-95cd86bbf99a | -5.7945 | -45.0586 | 2026-07-03 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 5f1c44f7-39d9-38f0-b7b0-24054b826188 | -5.8058 | -43.7975 | 2026-07-03 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 205.4 |
| 99320e02-3b91-3232-8079-63cdf110e5a9 | -5.8134 | -45.0345 | 2026-07-03 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| d68b6359-4246-311c-8edf-001214396e57 | -12.7359 | -44.5225 | 2026-07-03 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 7d9aac20-3e88-3354-a7a2-5b454707d3ae | -5.7947 | -45.0359 | 2026-07-03 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 9d354728-df60-3179-beae-86f98d5fc1db | -10.9397 | -43.0593 | 2026-07-03 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 81bf342b-8cb4-3fa1-8c0c-c3bad2ec2ee6 | -12.7553 | -44.5194 | 2026-07-03 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 232.3 |
| 55e0819b-5d3f-3105-a5a0-a61fe6c1ae35 | -5.8056 | -43.8207 | 2026-07-03 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 5da69e38-2dae-3e99-a5b3-e59e69dc42bf | -5.7945 | -45.0586 | 2026-07-03 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 154.4 |
| aeb7c9d5-cafe-357c-9be4-fce3925d121f | -5.7947 | -45.0359 | 2026-07-03 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 0a49f599-78dd-32d0-b3a3-f5bea6b226a9 | -12.7359 | -44.5225 | 2026-07-03 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| dc7f6129-dae4-3ee9-8747-725ceabb6f98 | -17.2639 | -42.6527 | 2026-07-03 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 7a568976-f088-3deb-94d6-fe0d85fd9abd | -12.7548 | -44.5428 | 2026-07-03 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b3bd84bb-b1ee-3ca4-b5ad-664545684433 | -5.8132 | -45.0573 | 2026-07-03 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 80204df6-c228-3cda-807f-0cb87bc7f606 | -5.7943 | -45.0813 | 2026-07-03 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| b5df3abe-681b-370a-9672-b2febace6c9e | -5.8134 | -45.0345 | 2026-07-03 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 8454c4fb-4d71-3821-92c7-6e4eb541005c | -12.7553 | -44.5194 | 2026-07-03 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 198.3 |
| c4cbfea2-7e65-31ac-8ca5-5181977d0d88 | -5.8058 | -43.7975 | 2026-07-03 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 6ffebad9-36f5-3814-874f-6a108bd3944f | -5.8132 | -45.0573 | 2026-07-03 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 316d5bdc-524d-3370-b936-a261fa03c6e6 | -5.7945 | -45.0586 | 2026-07-03 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 99f19538-79d4-3c94-b479-f8224aebd5c8 | -12.7548 | -44.5428 | 2026-07-03 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| e94a92b9-b6ba-3f4e-b62f-ea1c99538cc1 | -17.2639 | -42.6527 | 2026-07-03 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 6c5c71a3-d277-3404-be2b-87de6edc9f29 | -12.7359 | -44.5225 | 2026-07-03 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| d83014f7-b893-381e-9199-4b6d4384c954 | -5.7947 | -45.0359 | 2026-07-03 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 1268265c-7914-3d1b-896a-dc7ca6d3eb16 | -5.8134 | -45.0345 | 2026-07-03 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 7ea84c9d-ced5-3802-ba80-ecbaa16017f4 | -10.9397 | -43.0593 | 2026-07-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| ff4bb709-ec49-302e-83a6-6f6cb5e3d9f8 | -5.8058 | -43.7975 | 2026-07-03 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 0f1d5f0b-9ac3-3631-8d1c-9c928a5a0de9 | -10.9588 | -43.0565 | 2026-07-03 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| b70d6d99-a865-326f-8415-898f1b3024b4 | -12.7553 | -44.5194 | 2026-07-03 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| c155a575-b4f4-3aeb-a3c5-a9c712090363 | -5.7945 | -45.0586 | 2026-07-03 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 134.8 |
| b89b21a2-2c32-35f7-a667-ea719771fe4f | -5.7947 | -45.0359 | 2026-07-03 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| c49acdc2-4c39-353d-9858-997a131f9efb | -5.8132 | -45.0573 | 2026-07-03 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| a15b481b-561c-3d20-8eed-f3aa1ce22f06 | -10.9401 | -43.0355 | 2026-07-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 8fa1a2d2-5d02-3e4d-a867-74ea66c56036 | -17.2639 | -42.6527 | 2026-07-03 00:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 9bbec95e-4897-38d9-ac81-3596ba14b23e | -12.7359 | -44.5225 | 2026-07-03 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| b08182b0-42cb-307a-bbe5-601ce7dd657a | -12.7548 | -44.5428 | 2026-07-03 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 910d110d-d1cf-3e02-be7b-1e4a17c1a316 | -12.7553 | -44.5194 | 2026-07-03 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 168.2 |
| f2fcc55b-1746-3254-a546-17284d2bc153 | -5.8134 | -45.0345 | 2026-07-03 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| bb61e065-4fdf-3323-8da0-703018adf94f | -5.8058 | -43.7975 | 2026-07-03 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 4bd2275a-daa8-3d22-adbb-c7319877d465 | -5.7943 | -45.0813 | 2026-07-03 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| f2d9dd55-2a41-3616-a256-df15c367262d | -10.9397 | -43.0593 | 2026-07-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 6e94643c-f435-33f5-8ea4-7958384fcce9 | -10.9588 | -43.0565 | 2026-07-03 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| ac6751ad-4bf6-3656-8b51-7b76882a3c75 | -8.3848 | -48.214802 | 2026-07-03 00:30:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64bf2498-1f56-3fcc-8578-5ad5057e0633 | -10.9031 | -56.844799 | 2026-07-03 00:30:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e44ad86d-9733-3610-a5a4-763a2147a3dc | -5.7923 | -45.0522 | 2026-07-03 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5bc516e-9b30-389c-93f6-d89524065643 | -17.549999 | -53.998798 | 2026-07-03 00:30:00 | METOP-B | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7678f2fd-0041-3d66-991e-65c00e5c21a7 | -10.9381 | -43.066799 | 2026-07-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 254d3612-664f-31c2-8738-774aa9cfc86b | -3.5029 | -48.032299 | 2026-07-03 00:30:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 085c865d-3df2-328f-a661-f3d331422947 | -8.7213 | -48.326302 | 2026-07-03 00:30:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bcbdb478-f470-331f-b13a-2eaf593368d9 | -12.8002 | -47.174801 | 2026-07-03 00:30:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 927eac1d-1f5d-3ae0-9cd8-81e7fd3276b9 | -5.7826 | -45.0546 | 2026-07-03 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa56713a-beac-3e3e-ba6d-5f92f6679ef5 | -10.5844 | -55.410099 | 2026-07-03 00:30:00 | METOP-B | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a470f5df-310d-3e4b-a782-1981a238b68b | -4.0096 | -48.046398 | 2026-07-03 00:30:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4201f352-23ae-362e-bffe-b98c7854c56c | -12.7394 | -44.5154 | 2026-07-03 00:30:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 82fa4fe5-0485-3e8d-b0e6-4b4c39ee33b0 | -11.8503 | -48.2393 | 2026-07-03 00:30:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4f60e1a0-9aa1-36cf-907a-806b8fc2f668 | -5.7916 | -45.007999 | 2026-07-03 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b89910ef-96e8-323d-ac74-d88ea6c75fb9 | -11.3623 | -55.397099 | 2026-07-03 00:30:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ca664db-a68e-30b7-9ed1-a1a9bc045326 | -9.7557 | -47.8666 | 2026-07-03 00:30:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df133fe5-d2e8-3f1e-b5e8-1d1cf2da91a4 | -12.5089 | -48.2691 | 2026-07-03 00:30:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8593f050-b82c-35d9-af82-f8c8cd15af23 | -8.3751 | -48.217201 | 2026-07-03 00:30:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0bd3f871-4957-3e3d-ae5f-901d7f4bfff9 | -17.5532 | -54.0145 | 2026-07-03 00:30:00 | METOP-B | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 621c5c67-5de2-3ab4-bf27-7221be9fa4de | -8.7282 | -48.312599 | 2026-07-03 00:30:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2fc90ffd-b77a-3132-8718-f77ce3b7b1de | -17.5516 | -54.006699 | 2026-07-03 00:30:00 | METOP-B | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3afcc98a-76a1-3312-a838-4d00eb498e58 | -9.7585 | -47.8783 | 2026-07-03 00:30:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c0992b2-f690-3195-8bad-c04a5820e9a6 | -11.5596 | -52.792 | 2026-07-03 00:30:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5aaf4275-ba4c-3a0d-82a4-89c889963208 | -20.430599 | -47.545601 | 2026-07-03 00:30:00 | METOP-B | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9b37e1ef-1582-33f5-b539-d1775e45af36 | -11.7051 | -51.6157 | 2026-07-03 00:30:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 063d4e05-ecd5-3e30-8b0e-5aeb472507b0 | -11.3121 | -54.459099 | 2026-07-03 00:30:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e4dada7-2213-3a98-b18f-6a01d616eacc | -7.6389 | -50.021801 | 2026-07-03 00:30:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20429a3e-a997-3596-b027-35e3ed810688 | -11.3525 | -55.3992 | 2026-07-03 00:30:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 009f0bb6-3625-3b05-81b6-43fc9d88e028 | -11.4204 | -56.049099 | 2026-07-03 00:30:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e19476d-5729-3afe-abec-0ca3a3a34b4b | -5.8019 | -45.0499 | 2026-07-03 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9047e18a-a8ef-33dc-82e7-f4b7800e1829 | -8.7116 | -54.566898 | 2026-07-03 00:30:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9091d986-77a2-355d-92f4-a7557182c7d2 | -3.9999 | -48.048698 | 2026-07-03 00:30:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84bae354-fe00-36a4-8d4c-afe4de94a090 | -9.746 | -47.868999 | 2026-07-03 00:30:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a060f28e-b3a1-3b23-b500-e959834e7f98 | -12.7349 | -44.498001 | 2026-07-03 00:30:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6e035d91-cbb6-3f78-b91c-7c25f65b69ba | -11.7068 | -51.623001 | 2026-07-03 00:30:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b5fc8e0c-7888-36ac-88f9-a747d3201162 | -8.3876 | -48.226299 | 2026-07-03 00:30:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab8beaea-6a4e-38ab-9d57-3056020a30a0 | -5.7968 | -45.028999 | 2026-07-03 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f537254-e6c2-345c-b74e-0da91bfcb3ae | -10.9477 | -43.064201 | 2026-07-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 839adf96-afac-3abb-abf3-36bf3a74d4b3 | -10.9258 | -43.019798 | 2026-07-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 744e7e0b-c56c-35b5-b4fb-ffb3c360f274 | -11.4187 | -56.041 | 2026-07-03 00:30:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91d77514-67dd-3cba-9bdb-1073977bff9d | -11.3219 | -54.456902 | 2026-07-03 00:30:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 697f5672-41ee-3001-b7f3-e4072c8bb549 | -10.1318 | -52.089699 | 2026-07-03 00:30:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 706714d8-8a00-3100-9efe-ae7ccb9c606d | -10.9416 | -43.040798 | 2026-07-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 36706a0b-eeec-39b4-b06c-99e2d7f524aa | -7.0123 | -45.421299 | 2026-07-03 00:30:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56347a2e-1d1a-3d62-8bb8-62f5f7ac6a2c | -11.346 | -55.416698 | 2026-07-03 00:30:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28aa8809-9587-32c0-afa2-ab2f54097782 | -5.773 | -45.056999 | 2026-07-03 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ee775fe-bc1e-3f0a-9d2e-dcab947da070 | -19.5109 | -52.733002 | 2026-07-03 00:30:00 | METOP-B | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 66d6fad8-1f08-3424-bdc2-38aef95351c3 | -8.6235 | -55.0508 | 2026-07-03 00:30:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19b475ca-4fc6-34dc-9e83-f43fa00e5f58 | -4.3392 | -47.746101 | 2026-07-03 00:30:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36c30eef-002e-3867-bb29-9d14b041e460 | -10.5828 | -55.402599 | 2026-07-03 00:30:00 | METOP-B | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8a7f8d4-50bf-3ce0-8c78-f4b787872182 | -5.8012 | -43.806999 | 2026-07-03 00:30:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3e51a8e-9be9-3fce-b9f5-8424ca4f998b | -11.3541 | -55.406898 | 2026-07-03 00:30:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 56f9a64e-6c0a-37aa-8a0b-688802657b75 | -12.4894 | -43.791698 | 2026-07-03 00:30:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
