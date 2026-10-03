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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bfcb636-1d99-304d-a644-1ac34db6c058 | 1.7768 | -55.610401 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4050b4dd-62d8-3c79-9058-8e3c5747038f | -2.5715 | -54.7388 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d95b23a-3878-3662-916c-26c9fdfd030b | -3.9125 | -54.424 | 2026-10-03 00:30:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa2c8c07-c64f-3969-be4d-f72aa5c9421d | -11.4637 | -43.407398 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 415e5867-2945-3588-8567-1832024139ea | 1.8074 | -55.565601 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05a9f1eb-6a9b-3c27-9228-fe644efd9146 | -3.6385 | -55.489601 | 2026-10-03 00:30:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9092767d-e9f5-3dc0-9307-8117bb43a034 | -3.0064 | -53.885601 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38cbddbd-7b6f-31fe-960e-25ee932add7f | -4.7189 | -43.27 | 2026-10-03 00:30:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33807298-08fa-38fe-afc8-fe3246028848 | -6.9233 | -49.617199 | 2026-10-03 00:30:00 | METOP-B | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af9dada9-0fe5-3094-8817-0ea5fa0ba611 | -3.6668 | -60.591301 | 2026-10-03 00:30:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ca4b2ba-9ae6-3573-ba94-95af51a7d065 | -6.2049 | -53.262001 | 2026-10-03 00:30:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9d8ab78-19e2-3a34-8d45-f947f3d80d01 | -1.2132 | -54.522301 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6fd44ad-9fac-3d57-9708-779c2b97b76a | 2.3529 | -50.7491 | 2026-10-03 00:30:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e6f7d71a-ab13-3295-a9b9-1b066a4caf8f | -3.9691 | -55.4016 | 2026-10-03 00:30:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cb69d48-217d-3cb3-8908-d014654e0322 | -6.0094 | -53.5345 | 2026-10-03 00:30:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5e30141-a4d8-3429-ab4a-2f0906a1f1c5 | -5.7314 | -45.126999 | 2026-10-03 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ceacb15-e41f-3b5d-8184-2ae2bb9225fa | -4.7819 | -55.715099 | 2026-10-03 00:30:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d64a4846-2bef-36b1-b2ce-b4910d604423 | -11.7827 | -43.5224 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aea6259f-29d4-3b44-8162-22278544fcf2 | -3.7069 | -50.660599 | 2026-10-03 00:30:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a5796bc-7319-36cb-83ab-07a44c81fe52 | -5.7273 | -45.152199 | 2026-10-03 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 27cee195-ad3d-387a-b4ad-e532985c2ab1 | -4.7285 | -43.267601 | 2026-10-03 00:30:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8796cf0-044e-3e35-962a-eb2c0bfa45d5 | -2.8863 | -56.815201 | 2026-10-03 00:30:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 179c7f49-1356-351d-a387-e14a61415009 | -6.2131 | -53.252602 | 2026-10-03 00:30:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab035faf-842b-3a90-8a39-e1f945c77ead | -12.8496 | -44.677898 | 2026-10-03 00:30:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1c3e2f89-c466-3030-aad6-fefeb0c2ce50 | -3.1735 | -54.076302 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4920d9f-9cb7-33ab-83b9-592a4d09ad9d | -3.0031 | -53.870998 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aaa000e-a35e-3235-9a25-7521bc78b8d4 | -2.4113 | -56.810799 | 2026-10-03 00:30:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5903c3e8-5d18-3e50-a7f5-0e7b2d342cbb | -5.8939 | -55.482101 | 2026-10-03 00:30:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07f3489c-071f-3df5-944c-86aca0ea75ab | -11.6386 | -43.562 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d1a53912-effe-3564-b6a3-1e7f2c8cc454 | -3.5837 | -54.519798 | 2026-10-03 00:30:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35a78325-1fb3-354e-b19c-9a94867d7502 | -3.0047 | -53.8783 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa8cc39a-ef8b-303e-bd4b-38d193f734ed | -0.8996 | -47.899101 | 2026-10-03 00:30:00 | METOP-B | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12eafe8e-c3f5-319f-b08b-9c034ac08946 | -3.4121 | -52.819099 | 2026-10-03 00:30:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7253ce71-a7f6-3628-9ddd-06c48f64bc8f | -6.2033 | -53.254799 | 2026-10-03 00:30:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0dbb4b9-9bf1-3550-a497-4b82fa046b01 | -2.8875 | -54.1329 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7243c4b9-98c5-3db5-ba10-446316e0b962 | -4.4366 | -47.9058 | 2026-10-03 00:30:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15cdfac4-6cbb-31af-aa81-febf2cdb7dac | -4.041 | -51.0788 | 2026-10-03 00:30:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c4faebc-0c3f-378b-8e41-51bd1abc08a8 | -5.0969 | -56.2458 | 2026-10-03 00:30:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5a44ebf-9319-38cc-bb85-e514356107f5 | -1.2736 | -54.561501 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42da62a1-58f6-3a72-9562-7b9e7bc4e779 | -6.2288 | -53.141201 | 2026-10-03 00:30:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33658ce2-8912-357d-b2b8-04577894601b | -2.9071 | -54.083199 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26de48b2-2814-356c-afc5-24405c449692 | -11.7325 | -43.410198 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 224f5bc8-9ec0-3d7c-a7d8-5852bc46bde5 | -2.8907 | -54.147301 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2afa6504-74a9-3006-a946-6479b04a746f | -3.1301 | -53.749901 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2c0dc13-1692-3de3-a2b3-15c36c5dcd9c | -3.1152 | -53.73 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36d4e490-ed7f-3cbc-835c-250ee8ff71b9 | -2.1505 | -59.224899 | 2026-10-03 00:30:00 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e7bf3cf3-247f-3ba2-b597-b39612449f0d | -11.7031 | -43.494202 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b93aeba3-73e3-3ec2-b379-c826a41eb0ca | -1.2704 | -54.547199 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de6d1209-45a3-3eba-864d-e8ca9a9d8e3b | -4.45 | -47.9189 | 2026-10-03 00:30:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 292ba6a3-b2c4-35a7-a7fe-f0f0041c5117 | 1.8126 | -55.588902 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed380c01-d2d9-391e-8cab-fba448deff6e | -1.2606 | -54.5494 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd081cac-24df-33f5-a4e7-8a3c6da7c649 | -12.8545 | -44.696499 | 2026-10-03 00:30:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 401880bb-7cf5-30ad-a312-1b76ed24de23 | -5.8524 | -53.479401 | 2026-10-03 00:30:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 151a2891-2b93-3e58-bc41-4c02e0cfad1a | -6.7311 | -44.128899 | 2026-10-03 00:30:00 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b316a2f0-3994-36f0-98f7-fb57fe642917 | -5.737 | -45.149799 | 2026-10-03 00:30:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5accd93d-2966-37fd-9ac7-6bbffa2b3430 | -6.0111 | -53.541698 | 2026-10-03 00:30:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9462f4f3-132d-3fa5-a188-f400dd6bc2b8 | -3.6416 | -55.503201 | 2026-10-03 00:30:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0da36753-4c60-3e32-b6d2-6e41c9acccd0 | 0.6274 | -54.402599 | 2026-10-03 00:30:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 661d4e1c-9ffe-3962-8e18-baba95e0e8eb | -1.1389 | -54.149502 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c8a975f-235e-3842-9cca-7068e2dc05a2 | -11.7133 | -43.415501 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1325337e-b674-318b-8b10-27cec4bf729e | -2.4612 | -56.073002 | 2026-10-03 00:30:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6b5731e-d69c-3f8c-a41d-f3d84d7786f2 | -2.2481 | -51.922199 | 2026-10-03 00:30:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 745ac305-1ea7-3014-aea1-0b59af3b8d62 | -2.5699 | -54.7318 | 2026-10-03 00:30:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4ff0a89-fcad-32c7-92d9-de2662bbf1de | -6.8575 | -59.243401 | 2026-10-03 00:30:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ccb613dd-cbf0-3b14-9955-a7ddacf48417 | -4.1739 | -48.659801 | 2026-10-03 00:30:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5a6d9dc-86a1-3159-ac03-8d3cbec71e58 | -2.93 | -54.093201 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab5cd1d9-b8a8-3a83-8ff4-ba8b8805b8be | -3.1883 | -54.095699 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c26bf355-7d9a-3095-815b-bea48abe4908 | -11.4126 | -43.3699 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8a316b3e-09e3-333e-84bd-00573dd7bda1 | -1.852 | -54.884701 | 2026-10-03 00:30:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ece5b91e-4583-3e56-8080-0841fb6d29dc | -10.8773 | -57.102402 | 2026-10-03 00:30:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3958c521-2f10-3802-9eea-5f76e95b36f6 | -5.8508 | -53.472198 | 2026-10-03 00:30:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83356980-9e06-304b-9523-3ecb8185f71d | -4.2107 | -53.560501 | 2026-10-03 00:30:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff6f3547-b4f5-38e7-962d-a338cda4798c | 1.7913 | -55.591499 | 2026-10-03 00:30:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed3347cf-3d45-3f1f-9dfe-3a883c594274 | -2.9759 | -53.255001 | 2026-10-03 00:30:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 895616d9-a1ee-3d81-9c2b-30a8c0f2f654 | -11.4478 | -43.386101 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 29668cb9-1135-3a3e-97a9-7c85057ed98d | -2.2502 | -51.931301 | 2026-10-03 00:30:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79dff67f-6f76-3b24-9041-0ba5686efae9 | -11.4318 | -43.364601 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1b3d7f19-9f5d-3b2c-843e-637f7fbf5db5 | -3.1752 | -54.0835 | 2026-10-03 00:30:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae4c496e-c9df-3df7-a59f-dcb1bae1ce46 | -1.0748 | -54.093899 | 2026-10-03 00:30:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f229b4e-ff2d-3e45-8185-9eb10867df1e | -13.5348 | -44.097401 | 2026-10-03 00:30:00 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3e1a20b5-a891-3e49-be25-f3298a89f062 | -12.8448 | -44.659199 | 2026-10-03 00:30:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d95136f2-79a9-30da-bb6d-d201503aa1ee | -3.9676 | -55.394798 | 2026-10-03 00:30:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75a86d4e-83b2-32a0-9284-ff77e1fa53f4 | -11.4094 | -43.396599 | 2026-10-03 00:30:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c40a323a-6395-34a4-9897-cb0e692af57c | -3.4093 | -52.8233 | 2026-10-03 00:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| b81dcfb8-b032-32ab-96e2-27950ec3e819 | -11.7174 | -43.4861 | 2026-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.1 |
| c10ba6c3-5488-32c3-a3e3-5a3d77cde7e1 | -2.8855 | -45.4175 | 2026-10-03 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 74e479ba-3f78-3cc7-8271-9fcf547510c4 | -0.9147 | -47.9069 | 2026-10-03 00:40:00 | GOES-19 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 8b42d45a-9f67-3d30-9a4f-bd9d564cce88 | -3.1299 | -53.7633 | 2026-10-03 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| f0ef0148-add2-3621-a9ca-db8ddada8f42 | 1.7854 | -55.6054 | 2026-10-03 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 61df3f09-7863-3a22-b0b7-906670770166 | -11.4315 | -43.3884 | 2026-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| dddb67cb-948e-357b-ac76-f8a416294689 | -11.6977 | -43.5128 | 2026-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 3a3e98c1-8a7d-35f2-b438-d266c9e7c76c | -5.9381 | -43.6714 | 2026-10-03 00:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 29a7400e-7532-3890-b7fe-1e36c6df1409 | -11.7169 | -43.5098 | 2026-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 86914f85-b70b-32b0-93f3-383d4768422b | -11.6391 | -43.5692 | 2026-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 0f25eb05-8de4-3c3a-8ef8-e3a062db612b | -11.6981 | -43.4891 | 2026-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| b3d00d27-5ed3-31c2-8790-b62732e2bf5b | -3.1116 | -53.7436 | 2026-10-03 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 307e762a-1248-39a4-b2df-06c235be93a6 | -2.9266 | -54.0903 | 2026-10-03 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 25a8b62d-f4df-3701-accc-39073bd1b68d | -3.13 | -53.7229 | 2026-10-03 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| acd6ee14-744b-3f69-b35d-52e3aff478e6 | -11.4123 | -43.3913 | 2026-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| b7a4a85c-a4d4-39d9-a537-e10f339eb6ea | -11.793 | -43.5452 | 2026-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.2 |


[Clique aqui para ver as próximas entradas](README7.md)
