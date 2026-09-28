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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26cbd2fc-937c-3ffc-a3ac-7608abc3aafe | -3.8896 | -38.73023 | 2026-09-28 16:26:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2b0f760e-e0fb-36d9-b0d1-0c3ea66ee812 | -9.94391 | -50.23732 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b98a602d-5fdc-3eac-b3e0-b7df8713c741 | -6.73086 | -43.00676 | 2026-09-28 16:26:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 7.6 |
| bce17032-5e86-31b7-831d-9c8f193400bb | -8.66963 | -45.36934 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 4f7397bf-568d-3360-9b0b-0bbea3166054 | -9.94146 | -40.64328 | 2026-09-28 16:26:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| cc8a823c-2448-36be-b18a-8e9fd4acd609 | -10.21013 | -50.01571 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4cef5aa3-2eef-3971-800a-dba0f6c72ee3 | -7.7567 | -44.886 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 131a840e-7d3f-32aa-a0ac-d6bc520d2f66 | -6.68737 | -37.20333 | 2026-09-28 16:26:00 | NOAA-20 | SÃO JOÃO DO SABUGI | RIO GRANDE DO NORTE | Brasil | 2412104 | 24 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 3a883079-c7cd-3b13-bf0d-fe1a68614831 | -7.28987 | -44.31212 | 2026-09-28 16:26:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f8419634-5c46-3891-95a7-f45f58acd22a | -7.39919 | -38.84698 | 2026-09-28 16:26:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| adfc48d7-d51f-34c7-823e-107c97434a8f | -5.33275 | -46.19855 | 2026-09-28 16:26:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0316cc91-6131-3038-9830-a875f6e1f2ac | -9.76924 | -44.83912 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 160.4 |
| feb6046e-6e4b-38c2-98cd-dc3684afbfbe | -7.25284 | -43.36284 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| d5b46c53-6307-316d-a330-b86899a381d7 | -10.79853 | -48.73902 | 2026-09-28 16:26:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 09c51b8a-e94f-3a79-9070-c4e418c1bf7b | -7.63865 | -44.61428 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7da516e6-6645-30ea-b761-c072d5c2ecf7 | -10.98573 | -50.7001 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 80f77286-2f67-336f-8537-38f44967f6d7 | -9.9958 | -50.12254 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 099a9d04-505d-35a3-8971-d24e349814a1 | -4.97951 | -49.6221 | 2026-09-28 16:26:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b6479890-2efb-3404-9f0f-608b2dcc4e92 | -3.55711 | -39.03835 | 2026-09-28 16:26:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 1cd82ecf-7b76-3d51-9b2b-1966947c3e62 | -10.08558 | -50.38589 | 2026-09-28 16:26:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5e7b8ff0-cef9-3836-a511-fd5928548e90 | -9.80057 | -44.83028 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 120a24f0-9f6e-3403-8136-91f1eb3474c5 | -6.5088 | -46.0913 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59d06c37-ca86-3a8a-b0f4-de2371dbe2cb | -10.80645 | -48.7282 | 2026-09-28 16:26:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| bcb6f676-08ed-3be4-bafd-36c49bbc3e86 | -11.19126 | -46.28303 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 259c30e8-710f-339a-b4d6-c9ac377d55ae | -4.34706 | -42.95365 | 2026-09-28 16:26:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 316e6740-141f-3d92-9ebc-1133abb4530e | -7.68234 | -44.88874 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 193.9 |
| ed938f8f-087c-3000-a699-cbe9d025e99e | -7.33227 | -54.99673 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9831c1e4-2914-39b3-af92-ae5d8571aa90 | -8.93377 | -45.05196 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a607608b-62df-3265-b4b2-8eb3d40e55f0 | -6.89146 | -52.47611 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 88f0c116-69d0-31b8-a158-6da5ce0d9700 | -6.32614 | -44.44324 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8aa26bd-80b4-3848-afe8-c2e6095f2c9a | -9.79584 | -44.82273 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| df85da8c-db27-33ba-96a4-6cf136b915f0 | -11.15993 | -50.06252 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c101bac5-c9b6-3213-81f4-70560af8b857 | -11.1448 | -50.06444 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 7689cdc4-311e-3a10-86f9-a20cb6da5ff4 | -5.82047 | -39.28981 | 2026-09-28 16:26:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 8cb15cb6-e0b7-38fe-bb98-72968bc82826 | -8.09824 | -44.00626 | 2026-09-28 16:26:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0cfa9df4-8833-3958-806b-f54dc6ce59d2 | -9.63135 | -46.82104 | 2026-09-28 16:26:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e58db38a-fc79-3a9b-844e-3ebba629f71e | -7.2539 | -43.36986 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| c9e79f92-2bed-3396-a22f-cace0125a68c | -6.0466 | -45.17193 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ec8778f7-d6d4-3ba3-a837-eaad4fec4c84 | -7.14034 | -43.51701 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 17b4a8d5-c9db-371a-ae2a-f434357dddcc | -7.27482 | -45.3375 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 38b66808-5dad-3ade-a698-ef7f1b673b2f | -5.62876 | -45.54218 | 2026-09-28 16:26:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d427b258-ec3a-36d6-8e26-13e44ac99dab | -7.26229 | -43.35784 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 8cccf3e9-34af-3baf-a560-db83318df057 | -10.92734 | -50.70442 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 53a715a9-ba7d-36c9-83b2-872f8998d9f1 | -7.33946 | -38.72326 | 2026-09-28 16:26:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 8492400b-08d3-3ac3-a500-5c5330d8bb1f | -9.93778 | -50.22929 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6b3d9226-106c-3e42-ac96-474a25652850 | -9.51083 | -46.35735 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1a01e97f-1d5f-3283-adb9-97c72f3191d1 | -8.97217 | -44.14595 | 2026-09-28 16:26:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| a91264f1-361b-3c9f-bf2a-0d0de8fa6654 | -3.3363 | -43.33607 | 2026-09-28 16:26:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 13b561f5-d2c5-34c1-9404-1b8b53941552 | -7.89683 | -45.44331 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 17ca30cd-d329-3e7c-8225-91486b7ebfd1 | -7.33412 | -54.99804 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6c80b18e-894f-30a3-b6c3-1b9b32feff04 | -9.57643 | -45.49534 | 2026-09-28 16:26:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ebf4b480-a001-3b0c-9a3e-46a9a4d5ffed | -7.04697 | -44.30078 | 2026-09-28 16:26:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 943e8692-c7af-3fcf-bcdf-e3605b1aecac | -7.71016 | -44.90849 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| e0b32fc7-df15-359b-abb2-96068e268e14 | -11.4706 | -49.75013 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 7675106f-42c2-3ddd-926a-842bfdbbfa27 | -7.20519 | -45.08591 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 715feb52-9c70-30d3-8fe6-8008a386a870 | -11.17741 | -45.13536 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 66e96271-3073-3787-b825-cefb22482318 | -10.20276 | -49.98685 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 8a0583b1-72c0-3749-858c-1abb6ad96d78 | -7.1994 | -45.07085 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 495b931a-697f-37e8-ae58-6ed0b6dba17c | -7.06301 | -42.84773 | 2026-09-28 16:26:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2970d968-e53f-3108-bc91-0ea8f1852494 | -8.79934 | -47.51866 | 2026-09-28 16:26:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 44ac0e65-9d7d-32d2-b68e-e0b9fbb5495b | -8.30469 | -45.42097 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 336c2dd9-aa5f-3fb0-934d-383d8e60ebdf | -9.79643 | -44.82675 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d4c4afe6-5145-3a74-a7d3-6a1b55bf123b | -6.92632 | -46.50424 | 2026-09-28 16:26:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 62d38743-b615-35dd-bf0b-5bbe08eecf99 | -6.00699 | -43.92045 | 2026-09-28 16:26:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ee5c27c-d840-39c5-b948-776100424e16 | -11.4725 | -49.75463 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 988a947b-f755-30b0-98bb-9b9c3ecbddf8 | -9.76687 | -44.84778 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 239.4 |
| adf9ef67-c4e5-30db-a932-a9e01a56664f | -6.46753 | -45.91229 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 1513eabc-5ba9-36dd-8b1b-745a746c7b1a | -10.95706 | -50.684 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| bd495b85-c691-381e-9105-68393d32996c | -10.92693 | -50.70119 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 958ddd9f-51f1-3876-82de-aad8903d3a26 | -7.41521 | -42.62196 | 2026-09-28 16:26:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 5218e532-d6b3-3681-9a6a-ef24c70f6a18 | -10.28539 | -49.96445 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b00af880-dc1c-31fa-900c-15088844eb3c | -10.70954 | -44.42925 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 2714bd9a-72f8-3a40-8bbc-fb228747a53a | -7.25949 | -43.36184 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5d9e79d0-f4ce-3e22-8ae4-52f4398f7355 | -5.73197 | -45.05526 | 2026-09-28 16:26:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 83c06bea-e4a1-3f8d-a87f-6c8922e2ec42 | -7.71723 | -44.88395 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ed7176f9-357c-3c43-ae64-85db88567e78 | -7.21436 | -46.06572 | 2026-09-28 16:26:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 325e782f-9866-3a5a-8710-70be4b255bb5 | -5.55855 | -48.45165 | 2026-09-28 16:26:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a0b8f888-ea1f-3460-b816-346ea1256687 | -10.59036 | -49.99494 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 08dda9a4-401a-3867-a22e-7d4a83d14465 | -3.40353 | -42.97647 | 2026-09-28 16:26:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e18734a6-8421-3a97-9eb7-3840d0679cf0 | -10.97441 | -50.69495 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| c8782da2-f745-399e-8a64-6a8b9e5e0765 | -5.18627 | -37.06965 | 2026-09-28 16:26:00 | NOAA-20 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5ce1a1f7-3dd8-3573-9b7b-835f480c49bd | -11.46684 | -49.74958 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f266fd0c-dcb2-36bd-9b08-09cd6b876a86 | -11.13321 | -50.05394 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| ac267e02-81f6-3af1-8e8e-adc50456d64a | -7.20381 | -44.86121 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2e7ad855-b0fa-3331-82cd-52c0aada698a | -11.15451 | -50.06021 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c14e8657-89e7-3613-bd1e-d67d6a277560 | -10.85608 | -54.07236 | 2026-09-28 16:26:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 30ed0def-b367-3510-aefa-6b1fd305013f | -10.65092 | -50.71304 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4610d42c-2150-3750-b4cd-92309c632e60 | -7.53683 | -50.93102 | 2026-09-28 16:26:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0a98e0c6-7ff4-3327-8b03-1990e962c3a7 | -11.15061 | -50.0697 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 39761238-9037-3cda-a6f8-f139be01a456 | -10.995 | -50.689 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 83dbdbb7-ad67-324a-a4df-7d7671c2cec9 | -7.31341 | -44.58936 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1528190c-2d3f-3059-bc46-161a268ad80a | -11.12252 | -47.72311 | 2026-09-28 16:26:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4b50f6a1-0211-3d09-998c-2441d173457f | -7.34028 | -42.06561 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 57d4c7a3-298b-3b1e-831d-11caedc7dd8d | -6.17055 | -52.83101 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 41d08a64-e78d-3f12-990d-efa4f6a439e8 | -3.2234 | -42.79871 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d5d1b158-c6a9-374e-8197-7160c504a7b1 | -6.3172 | -43.61343 | 2026-09-28 16:26:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 30af4482-971b-3b60-bba2-190fa843e658 | -9.51418 | -46.38151 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 3b31e8ee-61d0-38bd-9ee7-7170303c1286 | -11.47676 | -49.7483 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 6dd846d5-1cd2-371b-9178-d5d6e9bdb691 | -7.53145 | -43.98107 | 2026-09-28 16:26:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 16855a72-70ce-3527-8404-569540aa280d | -4.20775 | -41.76112 | 2026-09-28 16:26:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |


[Clique aqui para ver as próximas entradas](README111.md)
