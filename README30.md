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
| ec7106a8-f997-335f-8726-a0d6afc5a127 | -10.53161 | -50.00101 | 2025-10-29 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9264d4c0-daa4-3059-99f0-46c212f7d2b3 | -10.52443 | -47.74781 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb856e90-bc70-3b24-ae42-ca61a286650d | -7.79193 | -46.43714 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de5e3bab-7935-3e19-b612-4ede206386eb | -9.91594 | -45.93032 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c79700f-ae60-36ed-a550-556a07c8d20a | -10.42473 | -44.99364 | 2025-10-29 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| db9969bb-5c3d-34e7-9c71-99f34951331e | -7.8625 | -44.23028 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15b5e272-1d3d-3688-80d1-bba0b27a9a08 | -6.16436 | -43.75615 | 2025-10-29 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 494393c3-c694-33a6-be55-af16d66b1cc2 | -10.3297 | -47.10049 | 2025-10-29 04:23:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e310d086-f645-3c40-a0e6-3d34595795c8 | -6.93181 | -46.99855 | 2025-10-29 04:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cba66cf3-97dd-3154-a6d0-77aeb620cf67 | -11.61333 | -43.35925 | 2025-10-29 04:23:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f002b05d-5919-3709-9c33-5fdd4bf22f45 | -10.33427 | -47.82373 | 2025-10-29 04:23:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 614b13e8-fcd4-3852-9780-d92039722ccd | -6.17313 | -41.67337 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5b45b158-614e-36ac-8b3c-f8426a84f6da | -5.65541 | -47.82539 | 2025-10-29 04:23:00 | NPP-375D | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fcd1406-90eb-3f8d-bdc9-65da969cc784 | -7.53878 | -47.30257 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ef2d7a9-eddd-30bb-a5aa-b9216328874e | -9.22997 | -46.34431 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c7132e3-eb62-3738-8b4a-66a2574397f7 | -10.98973 | -47.85488 | 2025-10-29 04:23:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f357407-aa46-38e5-b030-350ee206bfed | -9.54073 | -46.92358 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe49f867-6578-30ae-89f9-99eec70ba9f9 | -5.81352 | -50.05983 | 2025-10-29 04:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cbb70d8-a45a-3d1f-a735-693a7a4ce92f | -9.90654 | -44.9154 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 522e70aa-4af2-32aa-9b20-9ea3e5b8c7bf | -6.74311 | -46.55053 | 2025-10-29 04:23:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d8716c8-e2cf-30d3-9a34-ceab8377ccd4 | -6.14399 | -41.56938 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b4fb716b-5fbe-39f4-bf97-5e2838b854e7 | -6.13885 | -41.68121 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f21944a5-3f26-3b70-b866-0ba54362bbf7 | -10.39013 | -45.3023 | 2025-10-29 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18482ad5-2021-3280-8431-c07cd8f26b9b | -7.44904 | -49.40849 | 2025-10-29 04:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef6f31c6-5c1d-3929-9d94-a07082b59de4 | -10.87787 | -48.62296 | 2025-10-29 04:23:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c946c603-102f-3714-83d3-6a9d0288aafe | -5.39585 | -45.13241 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77fdb470-edaf-3eb5-9c67-14a0285faad9 | -8.00013 | -46.20532 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97391d8e-aac9-346e-9be0-abaece8a4346 | -4.96791 | -47.78344 | 2025-10-29 04:23:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd2a36cc-4023-3b45-8255-994e7af405ab | -5.40917 | -45.22042 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c0cf69e-e239-3418-a04f-f2f3183004d0 | -6.17786 | -41.6908 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 684b4c62-729a-3490-a453-1a49f6272e3d | -10.52611 | -50.01003 | 2025-10-29 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ede94e62-56ed-3c75-901c-3014793399bb | -7.12517 | -47.20518 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ee2e67e-996f-364c-af55-eb56d3c35970 | -9.16989 | -46.36393 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd535ab2-a8be-3c07-a8a7-9ff0c9faa971 | -11.18856 | -45.21673 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 443056f2-f906-3b23-ae5e-fc76e74df396 | -9.13453 | -51.2999 | 2025-10-29 04:23:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00694f4d-1436-3d49-9be5-86c9940d42c4 | -11.01235 | -47.73822 | 2025-10-29 04:23:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c59d4f70-e752-3e80-a75f-79ce060019c7 | -10.38238 | -45.30826 | 2025-10-29 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa55a219-4e53-3b84-b81d-2f9ca354c2b4 | -7.53814 | -47.30643 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 990269c8-fbdc-3096-bf04-5c746631a9d3 | -8.54165 | -48.98233 | 2025-10-29 04:23:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1d45498-7816-33e6-a8ee-cca1fc756f8a | -8.2431 | -46.90997 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73a91af6-a114-3936-96d9-3d5406b79413 | -7.7987 | -46.43821 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ddebbbb-8f24-3a74-8e33-6ab6cac0bca4 | -9.43968 | -46.90311 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f4722e8-f6fd-3c8d-981c-53bb8825ff79 | -9.49651 | -46.93883 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f3756a4-f941-3c97-849d-83356ead5510 | -9.93766 | -47.86621 | 2025-10-29 04:23:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 198d4bb5-e8a8-3684-9a86-e75a0f9006c2 | -6.10868 | -42.4716 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8580311e-697e-365e-ab1f-cefc834b03c1 | -9.52188 | -46.9542 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bde86c3-a65d-32a2-872a-49fa7aa0f417 | -7.70096 | -46.90843 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9dfaa2a7-eac0-3481-989d-0fb7db13a95b | -6.26679 | -43.88013 | 2025-10-29 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c931562f-e13d-3f22-8ee2-325bdd5ebf18 | -10.62756 | -47.88585 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba86ad56-d42e-3bc9-a3e8-71f30e539b0e | -10.91091 | -47.80311 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 087d19e5-f7fa-3a9e-8d98-c79b9f622db9 | -10.92287 | -47.59976 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f13607fa-9d02-3e65-901f-7d3ac27c17bb | -7.75907 | -44.71642 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| baaf807b-8ec6-308f-ad78-a721bbbdd6a2 | -7.30939 | -45.67728 | 2025-10-29 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62840842-ab59-312b-85fb-f4e4a81fce5b | -5.61219 | -47.09425 | 2025-10-29 04:23:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 264e8eca-50ee-3a7f-bf75-d899f646333b | -9.15705 | -50.13908 | 2025-10-29 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63214cf2-7890-3030-82e1-ecb5e43da10d | -7.80296 | -46.47614 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38b8b2b4-e4a9-3193-b0fb-538fc703cc52 | -6.48301 | -42.24265 | 2025-10-29 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 420498d7-7c09-3c6a-9db6-b5daff042e62 | -8.19344 | -44.45164 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94810c68-5a03-31a8-90b7-1d7b824610bc | -7.93289 | -45.49739 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad86a7fa-e45f-3708-987a-c2ae3817912a | -5.23689 | -45.13543 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 491c9372-8b1f-3dc1-86c1-7164d94ca407 | -10.85733 | -47.89204 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 150b159e-659b-3733-8b93-11f0b5f5c914 | -5.57304 | -46.5305 | 2025-10-29 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f73cec16-8b15-362d-9938-64b9d3e091ea | -7.79958 | -46.4756 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b053531-d3dc-38ca-aa20-74c868e241dc | -6.965 | -46.23753 | 2025-10-29 04:23:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6dcc8c0d-539f-34c2-8cbc-1318452891a1 | -7.69369 | -46.89612 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f85d6a7-3176-38e4-94be-7728f1cec7ce | -10.85388 | -47.89143 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb4ce536-f652-32a2-9f8f-1fb2a174b363 | -7.35146 | -43.90713 | 2025-10-29 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01c8af6d-7f72-37f3-94f6-3d5cdebda6f5 | -4.63584 | -48.69317 | 2025-10-29 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bd1f6b3-701d-38be-85b2-39869a3cfcd4 | -6.44615 | -46.55309 | 2025-10-29 04:23:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13a189d8-3e36-3ae8-ac3f-22785a7e7e40 | -10.88377 | -47.99152 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62110bc2-5f2f-354b-8055-79c0c1f6e17c | -6.36447 | -44.18924 | 2025-10-29 04:23:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5811c7ec-8ee4-3cd3-9be5-c270affbc927 | -7.85637 | -44.2257 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ece98400-3c7a-389a-afce-136c8cbd6d0a | -10.37121 | -47.14512 | 2025-10-29 04:23:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00b02c40-b7d7-314a-914c-57c9c4c8ab29 | -6.85905 | -46.93225 | 2025-10-29 04:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c06a1d7f-6d9a-3287-95e5-046f88c9deeb | -7.80091 | -46.44599 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdfc424e-9dd1-3e7e-ab3c-eacea5a8da89 | -11.27791 | -45.50952 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 97c059f2-8a8d-30d7-a477-aa87b13641ea | -10.94612 | -47.66891 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e2272a0-4653-3050-8be0-d7611fcb2816 | -7.30884 | -46.7007 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a36aeed9-3277-3a30-a8ec-df236a49e316 | -6.15933 | -41.66728 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2a985e86-cd0c-333a-a900-30e72dae7164 | -6.99066 | -42.78757 | 2025-10-29 04:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a3fd2be0-4b67-3a1b-b1f8-d278df1855cc | -6.29718 | -41.88227 | 2025-10-29 04:23:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| faa7a021-4059-3ed0-a353-2102b3231e5e | -10.51441 | -47.72266 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01dfd2b5-2aab-3702-98d1-ae3d4b39b4d0 | -10.21827 | -45.94353 | 2025-10-29 04:23:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5ff58ab-4b88-354e-9387-a5bd98d3f496 | -8.72392 | -49.76835 | 2025-10-29 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a34ae424-e690-32ac-9e04-1427e998de48 | -6.11115 | -42.4328 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 97312889-4fdd-3a3f-b395-ba8956653ae3 | -5.85607 | -47.69592 | 2025-10-29 04:23:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d174d5d9-8a7d-3ebb-8649-16e137e040dc | -10.49117 | -43.32999 | 2025-10-29 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6bc3b86-08b6-3c9c-893e-c7a9f9e47faa | -5.80307 | -42.56969 | 2025-10-29 04:23:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a9b65f64-be05-3bde-8617-31a96cdaad49 | -11.14005 | -44.94271 | 2025-10-29 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 05f35be7-24be-3684-b690-46df77a2a17e | -9.15353 | -46.40154 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc1f013e-1118-39ae-912f-e046612443ac | -6.14416 | -41.6876 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fb229b08-9fc6-32cf-94ed-987a562a7a93 | -7.79973 | -46.45325 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 989a1804-d7e6-38c8-a3af-7348cc8b5a1f | -10.36782 | -47.14455 | 2025-10-29 04:23:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f76d5c7f-a93e-35f6-95be-1f407ed1c76d | -6.49065 | -42.23979 | 2025-10-29 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bf54ac14-89fb-304e-b818-d9cdd7a45496 | -10.856 | -48.64426 | 2025-10-29 04:23:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20e98d95-e929-3da5-8992-a90d9d8f9f57 | -7.876 | -48.41949 | 2025-10-29 04:23:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06f82044-fdbb-3518-aa8a-bf4428e63d45 | -6.96963 | -49.40188 | 2025-10-29 04:23:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0f994df-bc43-39e2-9068-74e745c68dea | -7.79752 | -46.44546 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee88e149-2203-341d-93f6-70b064999bdf | -11.34372 | -41.67171 | 2025-10-29 04:23:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7d2c391d-bd72-3006-8852-4d3d55e11886 | -10.45436 | -44.55 | 2025-10-29 04:23:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README31.md)
