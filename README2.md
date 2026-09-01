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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28595767-0c97-3774-9ca8-f2922bf5c32c | -6.68 | -55.4 | 2026-09-01 00:15:00 | MSG-03 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f72565f-7888-3f04-8a69-8e203bca49cf | -17.39 | -42.36 | 2026-09-01 00:15:00 | MSG-03 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cb06c368-5d70-3f72-9800-f701fc6e5081 | -10.17 | -50.34 | 2026-09-01 00:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15908eea-96c8-39f8-8959-390ec7b22769 | -7.2879 | -49.848 | 2026-09-01 00:15:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18beae8a-d6dd-3afb-8336-95c1eb8271b6 | -10.7338 | -47.981499 | 2026-09-01 00:15:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e711912a-eb53-33f2-8c0b-52d253afdaa7 | -10.0224 | -44.7108 | 2026-09-01 00:15:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bd72ccad-efcd-37ef-a9fc-7a62bdcac90b | -5.7342 | -43.278702 | 2026-09-01 00:15:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c87a395-37f9-34e2-94bd-7866513ba030 | -17.5247 | -41.320099 | 2026-09-01 00:15:00 | METOP-C | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d600a459-a5ac-3602-bcb0-810da2f40017 | -4.947 | -47.669498 | 2026-09-01 00:15:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ebc7c7a-e299-3ba5-baf2-41491efdd315 | -9.202 | -48.010899 | 2026-09-01 00:15:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 471ff64a-a640-34f4-94d8-02c6bf856886 | -11.4872 | -45.088402 | 2026-09-01 00:15:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7b586ffd-9b4a-3d4d-bc4f-5b1bb3470390 | -18.504801 | -50.919998 | 2026-09-01 00:15:00 | METOP-C | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d15aa016-c964-3e49-9a42-ea286f8d9912 | -4.1643 | -47.838501 | 2026-09-01 00:15:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb0b37f1-aa1a-315f-817c-ea861dd5887b | -11.3069 | -45.203499 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d51da82f-52e2-326e-8d6d-ba20c234841a | -11.3108 | -45.173901 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ebae693-dc4c-3051-b31e-00a2f5c3fd61 | -7.109 | -45.796501 | 2026-09-01 00:15:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8884aa2-eaef-38e0-9366-fa29eb7356c7 | -10.1939 | -50.367901 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 394dceb7-e135-304c-92d7-cefceb0a393e | -6.4035 | -52.192501 | 2026-09-01 00:15:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e41274ff-10fd-30a3-9952-fc92ae244f54 | -11.0929 | -51.499901 | 2026-09-01 00:15:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| af1ef516-b02a-3bcb-9d6f-b1285613475c | -9.4597 | -40.3549 | 2026-09-01 00:15:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9f5f38df-38d6-3baa-aad5-047b7b03de13 | -4.4908 | -46.401199 | 2026-09-01 00:15:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0607a238-e6c4-3ce8-876f-cd8ba3b6ac92 | -17.3785 | -42.373798 | 2026-09-01 00:15:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3a554eec-1a9a-3d05-8790-654d020640ad | -11.3564 | -45.437 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 368c9e28-7ac0-3d2f-8b22-fc4b604440af | -17.3866 | -42.363602 | 2026-09-01 00:15:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 49235d5d-9154-337e-8961-bf4026d0ae1d | -9.5411 | -42.896099 | 2026-09-01 00:15:00 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| acb4a92d-8078-3c6b-a78e-a42eded0ba3a | -11.3544 | -45.427502 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 025b923e-f2e4-31b8-bd7e-533bf78f7932 | -10.13 | -45.878101 | 2026-09-01 00:15:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 620d3e94-1847-3d4b-8350-59c3e8b18f90 | -11.2561 | -45.109299 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 78c8220c-6e2a-3e48-9f04-076fef4550ff | -9.0018 | -39.981201 | 2026-09-01 00:15:00 | METOP-C | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 27342ad7-f109-3d7f-8dfb-5b68cd05409c | -1.0288 | -47.552502 | 2026-09-01 00:15:00 | METOP-C | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 206803d9-4f06-3c59-be29-c7cec1321047 | -10.0392 | -48.708599 | 2026-09-01 00:15:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ed0d1eb-9232-3c5a-a0c7-def4a0715e1e | -11.4794 | -45.099701 | 2026-09-01 00:15:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7df57118-a89e-3f7a-b540-5cc61cd58669 | -11.4755 | -45.081402 | 2026-09-01 00:15:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8240429d-dc3e-3f6c-8024-dd8396f14b7e | -4.4927 | -46.409901 | 2026-09-01 00:15:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| af052e45-519f-3a35-ae05-45909d3cc7f9 | -6.9956 | -52.899399 | 2026-09-01 00:15:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9df630da-49a7-36a9-8671-a81ec50c2f84 | -12.9742 | -45.992599 | 2026-09-01 00:15:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 225f6fb8-b5e8-3c9b-9a5e-0795957db09b | -10.2036 | -50.366001 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d4ba359-db88-3352-9b5b-625a896c13be | -10.1591 | -50.295399 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| af799d8e-faac-30eb-90ad-4789a44df3ea | -10.0152 | -44.677502 | 2026-09-01 00:15:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ad259df5-286b-3e0e-9d97-6c90db07ad51 | -11.1986 | -46.143799 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1e15074e-3a9d-3c02-aebf-6b7923f04a16 | -17.0014 | -39.497898 | 2026-09-01 00:15:00 | METOP-C | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 339dee53-e11f-335c-ba5d-46ef83ccff7e | -5.8418 | -44.901199 | 2026-09-01 00:15:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d566bcd4-79e6-3816-8814-9a67dd57efd7 | -6.3404 | -44.095001 | 2026-09-01 00:15:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98787992-93b5-3d6f-8398-b57e0b0645e0 | -10.163 | -50.3144 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c97279d-aea4-3dd5-b936-5046a43addf3 | -11.3167 | -45.201401 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe7596fd-9dcf-3f10-8d28-df9f9a7a27e5 | -8.8723 | -47.0797 | 2026-09-01 00:15:00 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f14fc2eb-e4ea-38a8-bec7-d096937b93a4 | -10.1959 | -50.327702 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e1b6dae-7a7b-3144-bc06-c26b56dd2636 | -5.8386 | -43.467098 | 2026-09-01 00:15:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad059ca5-ec2c-33c0-a4ae-e0ae40d740f4 | -20.472 | -45.687099 | 2026-09-01 00:15:00 | METOP-C | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dc145be6-c2c1-3355-b2f1-bb27ced2c947 | -3.059 | -39.937199 | 2026-09-01 00:15:00 | METOP-C | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c374ad22-d253-3b7a-bf85-6561add25388 | -7.8818 | -47.086102 | 2026-09-01 00:15:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aed8bcf2-bf55-30f3-8670-4c5fd88b7638 | -11.2052 | -45.110699 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 46f895f5-8022-3949-8a43-0153ae88c2e9 | -11.6553 | -47.612999 | 2026-09-01 00:15:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d035038-7deb-38f7-abc6-62596add9080 | -10.157 | -50.3354 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e584b466-ba2f-33ea-955c-466dc9aafaaf | -11.4813 | -45.108799 | 2026-09-01 00:15:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0f1461b7-5802-34ea-8426-de446b3d19fe | -16.135599 | -52.378502 | 2026-09-01 00:15:00 | METOP-C | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f8757c80-2169-3476-a6a4-299403905eb9 | -4.5926 | -42.927101 | 2026-09-01 00:15:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a58e59e-bd84-3f05-b97c-023b908eec0c | -4.9447 | -47.659 | 2026-09-01 00:15:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d2ecbff4-ca4c-3cd8-a531-64d748086a94 | -5.8809 | -45.583698 | 2026-09-01 00:15:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9a95038-2f7c-3f33-b6a7-811bfa28d5c6 | -5.7357 | -43.285599 | 2026-09-01 00:15:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5bec1e3-d5f1-399b-a0f2-155bd4b2f41e | -7.1071 | -45.7878 | 2026-09-01 00:15:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 653edca4-3a90-33bb-b7fc-22f28251a691 | -6.3421 | -44.102299 | 2026-09-01 00:15:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbb3a270-1bbf-368c-8288-ad93c322084b | -15.7948 | -51.088799 | 2026-09-01 00:15:00 | METOP-C | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ac868571-cdbd-3be0-a1ad-3cacd211de7c | -12.1002 | -44.985901 | 2026-09-01 00:15:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d460bcae-f114-3e9a-95e7-dd0e640f1c17 | -10.8623 | -45.375599 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9b8d5eb1-689d-35e9-ac19-244f74e01405 | -10.19 | -50.348701 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 764b93f1-d778-30a3-91b7-945ca492c05c | -17.315901 | -42.7122 | 2026-09-01 00:15:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1b2cddf6-e06c-3a4a-b4e9-97747ebb6789 | -7.6066 | -44.884899 | 2026-09-01 00:15:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f2e0bdab-8e90-3b00-ad34-c7f16a405462 | -5.5908 | -42.330898 | 2026-09-01 00:15:00 | METOP-C | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d2ed8535-067f-3d23-964e-b2f75aed363e | -10.1803 | -50.3507 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| afbb2164-97c8-3481-b35d-3907212e1199 | -10.0188 | -44.694099 | 2026-09-01 00:15:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dfaa3ebe-0a8a-3137-8b76-77bd1c876c5f | -3.1788 | -48.019501 | 2026-09-01 00:15:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2c44216-357c-320f-ac4b-fa678b00b006 | -6.7577 | -44.5802 | 2026-09-01 00:15:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0737bee0-ec3e-3232-adad-4663dd4c10ac | -15.6593 | -48.724602 | 2026-09-01 00:15:00 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 412102a4-ef1f-3a49-9b2c-30da536630d8 | -11.4774 | -45.0905 | 2026-09-01 00:15:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d7b51366-cfe6-3a69-ac26-40c2e13f5aba | -8.4914 | -44.751099 | 2026-09-01 00:15:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7de1ddda-91ab-30fa-9bbb-2cb34f51166c | -7.001 | -52.925201 | 2026-09-01 00:15:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffd5f0aa-8bc4-3ddc-9574-a29e470b67ac | -10.0605 | -46.659199 | 2026-09-01 00:15:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e99c00d-fb34-3bbb-90a6-a829730c8565 | -10.0286 | -44.692001 | 2026-09-01 00:15:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2b45d2f0-a168-37ee-b367-093d1ae520fb | -14.9666 | -48.153999 | 2026-09-01 00:15:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e12964bd-a87a-33d7-8dfc-b5a0ab074565 | -12.1021 | -44.995098 | 2026-09-01 00:15:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0196ac69-613f-3cd9-8140-81300ec85057 | -2.7196 | -48.807201 | 2026-09-01 00:15:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c0b9fea-b541-3807-bc6c-9c52e87606cb | -11.0587 | -51.5312 | 2026-09-01 00:15:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c7763099-8eb9-34b2-9e31-1b9dfa654afd | -11.1954 | -45.112801 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9e2d0b61-ebe1-3e48-9d55-36248f02827d | -14.9734 | -48.136002 | 2026-09-01 00:15:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 28f80670-1f89-3c9d-8e1e-0d1ca803272f | -7.5448 | -47.326302 | 2026-09-01 00:15:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d282efd4-66aa-3cc2-95da-be7ab6ce065d | -7.9094 | -44.256001 | 2026-09-01 00:15:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d65796e3-e45d-32fe-8cff-c5872cc84d60 | -10.1532 | -50.316399 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9258e5e1-e038-3c60-a8d7-2ba3db8c9df6 | -8.1823 | -45.2146 | 2026-09-01 00:15:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e0166cc3-dbb2-3433-a91a-4c207fcb5b81 | -7.9013 | -44.2658 | 2026-09-01 00:15:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3cf726b5-f415-34a5-b345-4976315bb444 | -11.3088 | -45.2127 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 586bff92-9564-3f21-b2f3-f302bfcac8b7 | -10.1862 | -50.329601 | 2026-09-01 00:15:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d013f66-a6a9-375e-a581-73ca226e3ee9 | -11.3128 | -45.182999 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 00612190-b807-3118-b643-6174290b89f7 | -10.8603 | -45.366402 | 2026-09-01 00:15:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7cbe6a97-8c63-3372-8a17-02cf58a69814 | -7.6083 | -44.892899 | 2026-09-01 00:15:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 667339ed-d5c2-30a1-abd5-6441bf6fee6f | -3.0472 | -39.931099 | 2026-09-01 00:15:00 | METOP-C | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 49bf210b-5d35-32af-b9ee-b3e793656feb | -17.3703 | -42.383999 | 2026-09-01 00:15:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e50ca1be-557d-3252-b684-dd18aab2bc2e | -3.057 | -39.928902 | 2026-09-01 00:15:00 | METOP-C | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d3579fdc-612e-3e2c-8f04-0f92f8189014 | -9.0545 | -45.7817 | 2026-09-01 00:15:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f3d2f05b-0690-386e-a7b7-5ca3ed04db7c | -13.3505 | -43.685001 | 2026-09-01 00:15:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
