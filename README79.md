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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c7b2c5f-fc0d-3860-9496-9aa199bc32bb | -2.76181 | -48.64775 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66c405e1-b672-31eb-afcf-0975e790d741 | -2.76082 | -48.6473 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 91e33f38-9a8a-3a08-bb47-e3d61510a8cb | -2.75514 | -48.69083 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 134ddbaa-4081-3762-b362-d3a7562d2e2a | -2.75404 | -48.69034 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 114ffb04-ef3b-396e-8d04-0e066f3eb6f1 | -2.75018 | -48.40479 | 2024-10-14 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e8a82ee-9c6c-3bf8-8afc-a686298049a1 | -2.74961 | -48.40844 | 2024-10-14 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cbd54a5-5765-321a-a0f3-7787b432afe0 | -2.74677 | -48.40425 | 2024-10-14 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 083fb3f8-7cd3-31f5-8d71-41ae634bc22c | -2.7462 | -48.4079 | 2024-10-14 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da4b3da9-ed61-350e-8651-a3e0ea5554f6 | -2.6966 | -48.70348 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1265eba-34cd-3759-86ec-b5630912aeca | -2.69426 | -48.62966 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9462d170-d5c2-3cf5-863f-7c77a5035542 | -2.69087 | -48.62914 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b3663e0-8eb7-39fa-85b0-56cacc76e17d | -2.69031 | -48.63273 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fdd071c-1ea7-3576-9eef-8077bbfd5d92 | -2.6839 | -48.87296 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b6e9d08-1b9c-346e-b3bd-fcd7351a3f71 | -2.64526 | -48.43005 | 2024-10-14 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ff71a072-0aae-30a4-ab02-bd154d92e5ce | -2.63166 | -48.53924 | 2024-10-14 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7de56ebe-cf52-350b-9d7f-124ba2a4bdb4 | -2.47682 | -48.19141 | 2024-10-14 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5b92897-9486-3e81-9500-a60bcd110405 | -2.47646 | -48.05881 | 2024-10-14 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 99d4292f-5674-3b3e-9738-d2c0f753d357 | -2.47624 | -48.1951 | 2024-10-14 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48037eb5-4d82-36e4-a93c-8523515c7fdd | -2.47588 | -48.06253 | 2024-10-14 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32b202cf-2f1e-33fe-a4e1-3d06e5011580 | -2.4734 | -48.19088 | 2024-10-14 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f6309d0-1dd9-3552-a51e-5fc483fe9b50 | -2.47282 | -48.19458 | 2024-10-14 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 813d54d6-ff46-319f-a5c9-ad6429277684 | -2.41868 | -48.62839 | 2024-10-14 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3584b819-c2f0-3ad7-a3a8-31233762024e | -2.41811 | -48.63197 | 2024-10-14 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca2b0e5f-4f17-3594-9150-1567b46fd705 | -2.32464 | -48.62508 | 2024-10-14 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed91007b-121d-35e2-8e97-4d041a5c46f4 | -2.26195 | -48.47197 | 2024-10-14 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78824128-4755-3f05-83d3-55ce0052f0a8 | -2.26126 | -48.29738 | 2024-10-14 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d1d289c-4fec-3c0e-923b-54ab1743fc4c | -2.17883 | -48.82083 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f39abcc4-952e-3c2e-bdef-65394fcf374d | -2.17827 | -48.82437 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96e8ccc3-3b77-3150-bfee-2136ce67d110 | -2.17547 | -48.82031 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7d87bd9-4ea7-3101-abe7-15d2e753a743 | -2.17444 | -48.33984 | 2024-10-14 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2eb61c0-cdf0-3fa1-a99a-0ac37ecbcf23 | -2.1739 | -48.36576 | 2024-10-14 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b057f9f7-66d9-3b02-a9cc-86c975aeb5dc | -2.17334 | -48.36939 | 2024-10-14 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c7bbb23-e795-3338-b67a-144def6aa002 | -2.1665 | -48.81168 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2cc63d1-19f6-3b63-936f-403cd627f706 | -2.16314 | -48.81116 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13ae3111-4c9c-3b24-ad97-1bb93acde5e2 | -2.15642 | -48.81012 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95f7536f-6b35-3d4d-9e66-f751121f2289 | -2.14353 | -48.80451 | 2024-10-14 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7440d615-e0a6-3f23-a511-adbea95e69b9 | -5.06386 | -48.06097 | 2024-10-14 04:44:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05756f43-1088-3eea-8d21-9ba75124c05c | -5.06326 | -48.06488 | 2024-10-14 04:44:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf9495a3-d363-380c-a5f2-64b94dd3f199 | -5.06034 | -48.06046 | 2024-10-14 04:44:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77f3a950-5e20-3661-b811-e59afe198377 | -5.05974 | -48.06437 | 2024-10-14 04:44:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4a631d4-b970-3891-8c3f-dc0bf5dae4ca | -5.05914 | -48.06826 | 2024-10-14 04:44:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34765a28-f8db-39ac-b361-b0b9dca0ac88 | -5.05622 | -48.06385 | 2024-10-14 04:44:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdf946b8-7618-3311-b939-ee7f85a9d1f2 | -4.90542 | -48.63836 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed383112-3954-34be-8843-2f88775b377f | -4.90198 | -48.63783 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb2b9658-b99e-3513-9901-2228898324ad | -4.71426 | -48.47673 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8fca4a8-7d56-3739-ad20-3549d89742c7 | -4.63792 | -48.74223 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b801953-92f5-3f06-93ef-057ac8885b7f | -4.27815 | -48.22668 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1643ba3b-c040-3a0c-bad0-9be94ae54723 | -4.27757 | -48.23046 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc28ca22-9856-36ef-b6ae-8a4c822bf5d1 | -4.27526 | -48.22236 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f39fe0d-1ed1-3491-bf4d-c913eff0766d | -4.27237 | -48.21804 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a0d31fb9-6c0a-30e2-9955-7b528f3babb9 | -4.27179 | -48.22183 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a6a01508-ed5a-32ac-8e34-0305fe135811 | -4.24924 | -48.25313 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2cf4106-e011-3ae0-81cb-d32c36b2bada | -4.22318 | -47.85943 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cec14255-3a95-3683-b657-55f6711a0748 | -4.21965 | -47.85896 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc508fc2-da33-3ee8-bca9-2f1cb791af7a | -4.21905 | -47.86284 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a778ce9d-06ba-391d-b997-aa6f3fe824e0 | -4.21552 | -47.86237 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e12f52f9-952d-3d99-b9b2-e1363302ee1b | -4.18641 | -48.029 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2deaacfe-2126-30ed-85e2-06ea19c011b8 | -4.18583 | -48.03282 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a8e5905-f045-3034-b105-52a42d33b3ee | -4.18351 | -48.0246 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03bff289-b855-3dbe-85c3-b79b2fed6677 | -4.18292 | -48.02843 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1803b5a4-90de-393a-885b-f367dc984494 | -4.18234 | -48.03225 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3465a66a-1235-35ed-afa1-0758da21b97d | -4.17943 | -48.02786 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e3f8c19-869e-3df5-a422-e898c155b206 | -4.12362 | -48.27661 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cde47d12-c554-3f0b-bbf1-d9624438dd83 | -4.12304 | -48.2804 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abb8bbad-7c98-3834-b689-b5817dfd8ca7 | -4.12246 | -48.2842 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6df931d-b2cb-3fb0-8c4c-036421c137c6 | -4.12188 | -48.26479 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f21fa4c-2052-3af4-9f8f-682f7f358629 | -4.12131 | -48.26853 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02ca0c0b-6e3c-3497-bc3a-2169af298f0e | -4.12074 | -48.27228 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0bf5f49-8fc4-3bd8-8a29-788d10899b4d | -4.12016 | -48.27605 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| caa6e67d-7364-3d0e-ab55-67eb4bf07369 | -4.11984 | -48.24196 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01ba74b4-ddfb-3227-9341-930e2d4202d4 | -4.11976 | -48.26509 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d901e50-f45a-3533-9dc0-01a9f47595b4 | -4.11959 | -48.27982 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cbc1ad37-b252-36cf-acf5-5646a11a2424 | -4.11924 | -48.24578 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6324a46f-a58e-3f9a-9bf6-0df61299efc5 | -4.11901 | -48.28363 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c5108122-901b-325b-958f-175e744a835c | -4.11865 | -48.24956 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05c0c686-20b4-3f18-892a-16da7520b86c | -4.11859 | -48.27258 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3c8dd90-4fe4-3353-a703-17db758bcb9b | -4.118 | -48.27633 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 76f588a0-f5b0-3b69-9a8b-484dc9c99e9e | -4.11741 | -48.28009 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 445ee0e4-f195-3705-b954-a4602e320f6c | -4.11728 | -48.27175 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c642337-7a7f-3739-a30f-dd526f6b97a4 | -4.11697 | -48.23763 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 765d5d80-e774-3704-b4ce-363b67c14844 | -4.11682 | -48.28388 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e6ada598-3809-394d-825d-3ada57a64fec | -4.11671 | -48.27551 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d8837382-96b1-32f9-b3b7-08512059bcd4 | -4.11637 | -48.24144 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| af6ab560-0e48-3228-90c5-e29439731a1f | -4.11622 | -48.28766 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4ee2e9a6-42ce-3efa-8e2e-76a5563acd48 | -4.11613 | -48.27926 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aa7dc416-1d7b-3fac-a493-ccf37b798e5d | -4.11578 | -48.24525 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bac3bf1a-b5dd-3fc7-ac97-e4d489c99ef2 | -4.11556 | -48.28305 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1ace9f3b-0a12-3daf-9388-4e110962b035 | -4.11498 | -48.28683 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ae716251-403d-3055-82fb-5450dbf10d11 | -4.11454 | -48.27579 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e9510d8-4048-3b01-b023-3a5a7bce1c59 | -4.11411 | -48.23326 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 384c4361-016f-31ef-9582-ed0e542a3b5b | -4.11396 | -48.27954 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e76a8b95-39be-32d8-9895-d68ce0edcbd2 | -4.11351 | -48.23711 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| fa3c8ad8-a1c9-3225-9036-a00f35f43ebd | -4.11337 | -48.2833 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c8234315-b321-3975-832d-827a4716c984 | -4.11291 | -48.24092 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 67e6196a-4296-3d93-9c77-8f4280c79b17 | -4.11278 | -48.28708 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 822e594b-6e05-35fc-bf80-61141c1007e4 | -4.11064 | -48.23273 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34d3b692-30e3-3107-88f3-e8a5dda0d28b | -4.1105 | -48.279 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8abe0805-901e-3e07-be3f-d4a9f3d507d2 | -4.11004 | -48.23658 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e6855d8e-476b-3242-a2d4-f5f417520770 | -4.10991 | -48.28275 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 18bb2801-d49c-3cc0-b458-582ac0ee7b66 | -4.10945 | -48.24039 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |


[Clique aqui para ver as próximas entradas](README80.md)
