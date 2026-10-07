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

## Dados Diários - Página 209

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b378320d-9d7c-3cbd-8a2b-20be5386c0bb | -11.14126 | -46.10798 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| ff97fce0-9c59-38f1-89ca-34aaf3e8895d | -5.71291 | -41.67641 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 59.9 |
| 2d26c942-52cd-33be-bc48-3bac680b2dae | -10.88285 | -46.67547 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 05b6d421-1e1a-3e67-a4f6-6b25d7828713 | -16.59973 | -40.70963 | 2026-10-07 16:37:00 | NPP-375 | FELISBURGO | MINAS GERAIS | Brasil | 3125606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.6 |
| 8fb8727b-c0e7-3bc5-8395-43850c809d18 | -6.48309 | -52.80919 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1ecdd55c-dd61-315a-8706-d0dc22c2e6a5 | -6.92124 | -41.24084 | 2026-10-07 16:37:00 | NPP-375 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 41db49ae-ebb9-36e4-a5d0-f276747e0f31 | -11.10712 | -45.95466 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| fc159227-0eee-32bf-b24a-4e2c28c825f9 | -4.51242 | -42.89234 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 99675f05-7442-357b-9f49-a0262997bf6c | -4.0222 | -40.92197 | 2026-10-07 16:37:00 | NPP-375 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 4f155aa5-e543-3daf-a2f5-ec635f61fd15 | -3.28481 | -42.58834 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fc6a14ee-f902-334b-9647-ac5a8e9a08f9 | -17.01983 | -45.92344 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4fbc0e2e-f285-3454-8de5-092464ec4638 | -16.23479 | -44.90504 | 2026-10-07 16:37:00 | NPP-375 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b7a8b30-a00c-360b-86a4-8d76ca1730ee | -6.92954 | -43.67102 | 2026-10-07 16:37:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 2ca5b7b9-42f4-3bc3-be9d-54e070c08d8a | -11.15557 | -46.18335 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| b2c59852-7379-3841-939f-8f31c3e3404e | -9.86467 | -46.31048 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c8d984c9-488d-3b43-8ae6-cbaa7ed29f0f | -7.77053 | -43.82117 | 2026-10-07 16:37:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 50d936b9-225f-3c5e-8f00-d1191c22dcdb | -5.96157 | -46.37405 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 316f1805-56d8-3a3b-8e38-d3e331612e86 | -10.49211 | -47.26574 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 2fcb4c96-8658-362d-912e-d501bb668556 | -3.94944 | -40.73109 | 2026-10-07 16:37:00 | NPP-375 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 3734647b-8286-3f1a-96de-a7e1077bf449 | -9.56102 | -45.68814 | 2026-10-07 16:37:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8255dc73-938e-3520-99d2-6f2629b8dbad | -6.22175 | -44.83724 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b93c7631-7e5d-3941-a3c3-4c0d77b0ab5a | -17.03135 | -45.92178 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7efcef72-ce9f-3198-b92b-712727180d2c | -7.88281 | -54.97471 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| c8eefb7d-172d-369c-a27c-6b137be9efd4 | -7.04936 | -44.32085 | 2026-10-07 16:37:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a2265934-0670-3739-a050-6925f5fa95c0 | -9.43597 | -45.82136 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 18dcb85a-9ba5-339c-9016-883e519f13c2 | -6.01899 | -38.43075 | 2026-10-07 16:37:00 | NPP-375 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fd8c2f2a-c56f-3d51-9f80-f5b261b7b7e3 | -9.82985 | -46.24813 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 468336e7-40f7-3599-8c15-71e3228eea45 | -8.24966 | -37.03327 | 2026-10-07 16:37:00 | NPP-375 | SÃO SEBASTIÃO DO UMBUZEIRO | PARAÍBA | Brasil | 2515203 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| df8e1fec-6214-36e2-b587-51f10198ed55 | -5.10305 | -42.92183 | 2026-10-07 16:37:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ae13f0a2-6221-388a-b482-999b49e11e3f | -5.7406 | -38.5774 | 2026-10-07 16:37:00 | NPP-375 | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 4f2e2c44-beff-338f-8ce0-cf866fdf649e | -5.72757 | -45.16569 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 741068fb-c181-35d7-9397-418b80a74f90 | -7.53578 | -45.87771 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6c511f05-f3a4-332d-8bd9-13774147ac00 | -3.67608 | -45.1229 | 2026-10-07 16:37:00 | NPP-375 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a447a2de-9ca5-3339-8a5a-c72d059beebb | -7.49987 | -45.77936 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7ee601dc-48ce-3d18-8571-01bdd6d256dd | -6.97204 | -40.02809 | 2026-10-07 16:37:00 | NPP-375 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 4bce2229-53fa-3471-b777-7ba292ecc350 | -9.95323 | -43.54778 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 08ad6390-3845-3769-8b51-919bb0735fcf | -5.70897 | -37.7146 | 2026-10-07 16:37:00 | NPP-375 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c6760c14-e3cf-3e9f-9c49-967705936548 | -4.97824 | -37.62608 | 2026-10-07 16:37:00 | NPP-375 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 96a0cd5c-bbe0-3f2a-aec3-d59da5f0375c | -6.46221 | -53.69589 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d15a1d63-b578-3e3a-9cbb-8b3c17b9bcd8 | -5.72293 | -41.73906 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 3ea737ec-70c6-3935-ac57-c2f494895063 | -9.9664 | -43.56725 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| cd1e352d-8834-312d-b41b-ecbc03bf767f | -6.68589 | -45.58092 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 853fac8e-951f-339e-a9d2-e2037274d73c | -4.14027 | -40.57278 | 2026-10-07 16:37:00 | NPP-375 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| d23842b5-beb3-3894-b2b4-d5943d53210d | -5.5858 | -47.26318 | 2026-10-07 16:37:00 | NPP-375 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 80c07cc4-f343-3d96-accd-18415e71b6f0 | -6.87453 | -39.46264 | 2026-10-07 16:37:00 | NPP-375 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 16877db5-bc95-3df3-a098-2f399f1e96f8 | -10.51952 | -47.26675 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5de6f594-1ced-309e-9c0f-299bbb8d1d39 | -10.86971 | -47.42843 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6a0d273b-ec45-3c8f-a948-178434304436 | -5.88672 | -57.75308 | 2026-10-07 16:37:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6dc00718-9b57-3eb5-8414-6f2649942d8e | -7.00959 | -44.06026 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cd89f05a-a05c-35ca-9034-733b3ce4c307 | -17.19691 | -43.53696 | 2026-10-07 16:37:00 | NPP-375 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| abd1ab02-8eed-3d85-a12e-f077a5ac74e2 | -10.38085 | -46.2291 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b24b98f0-6349-338d-8c21-f9cf5d1f8bd9 | -5.30903 | -40.80767 | 2026-10-07 16:37:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 14.1 |
| e8a94120-58e7-3429-9559-96d984130146 | -16.37725 | -42.9583 | 2026-10-07 16:37:00 | NPP-375 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e459161a-c4dc-3bd3-8c6f-2eb719a191e8 | -6.19271 | -53.1737 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5189835-48f4-3813-85a8-02935ffc5a32 | -3.39055 | -42.88319 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| eb44b752-b744-3934-aeb3-56cb4a24dc0a | -3.74479 | -41.72089 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 19df0a45-0267-35c9-9ddc-38bbcb019aea | -6.14728 | -51.7301 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 654f61a2-6ed0-321c-afaf-08aec2673f9a | -4.79994 | -42.7455 | 2026-10-07 16:37:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c74fc950-00a4-36b3-8ac5-1c47b7e5d6ba | -4.01411 | -41.76839 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 1d451bdd-fc1a-3b39-909b-0df1e6b25772 | -5.75838 | -42.03701 | 2026-10-07 16:37:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 3b4ca76c-5024-3b3a-bfd3-d14c4c0f9eaf | -6.20417 | -40.80774 | 2026-10-07 16:37:00 | NPP-375 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 5b923358-90ce-320b-a8be-77684d89e619 | -5.37295 | -44.16792 | 2026-10-07 16:37:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 93267999-aeb8-3bf0-96ee-82dcd7d4e5c1 | -4.18833 | -48.64245 | 2026-10-07 16:37:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| f3ef69ac-19cd-3b1c-96ed-0c3114ff1fea | -8.25977 | -54.71332 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5c66288d-7aec-3a7d-ac16-533b749412da | -9.15303 | -45.82684 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 13c49d9f-e938-38f2-bd7a-5c0ebd2e6400 | -5.09623 | -45.8393 | 2026-10-07 16:37:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c45b6efc-8ff6-3ba3-9c3f-0d8df037f5bd | -6.48407 | -52.81721 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e49576dc-ae2f-3238-9ebd-e9710691faba | -11.5196 | -51.4568 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fb87a304-e777-390a-b80d-b5d64ca72ed2 | -5.91527 | -51.93784 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 54200e38-7154-3614-9ef7-ac7cb7213068 | -10.99828 | -45.48188 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| db32b47f-b1c3-32ad-bddd-d72b9d66b709 | -7.7604 | -43.81652 | 2026-10-07 16:37:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 48c27711-dcd8-3c4e-81b6-5fe7bc650229 | -6.13873 | -45.46942 | 2026-10-07 16:37:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e8d053b-c259-31ec-ad2b-e94969aeb329 | -9.9613 | -43.48918 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e6e9a423-842d-3bdd-b684-f995e2fa968a | -5.85111 | -42.65871 | 2026-10-07 16:37:00 | NPP-375 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 32.5 |
| f6d979ff-9758-3b48-b512-8bf69eb86d70 | -6.58682 | -53.0191 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b21f0821-2626-3939-8c49-dca12b96ff34 | -10.99242 | -45.49084 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 72f87ac5-c778-3f3d-94ed-6cac86fed9b1 | -11.38634 | -46.68108 | 2026-10-07 16:37:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 59a71b7d-4cd0-3d4e-8cf8-2b6e27c16b99 | -7.34012 | -44.47847 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bcda6a38-c298-3e14-8244-721e9dfecda3 | -9.14887 | -45.82719 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8ac1da47-0873-36fd-ba35-27262b1e139e | -5.96854 | -41.35101 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 61fcefbe-6a22-34a9-ba94-6d6cd4f3d00a | -9.71589 | -35.92918 | 2026-10-07 16:37:00 | NPP-375 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| d16d0b71-d6e4-3cee-b4aa-1c9663732cf3 | -9.92433 | -44.81437 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 5ac147f0-5e8a-372e-87ec-25407a0184c1 | -8.29969 | -45.465 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 5427af23-8f67-39f6-9a16-f24fb1abaaff | -5.94014 | -46.63681 | 2026-10-07 16:37:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3c393e92-9624-31cf-a6dd-163fd428c70c | -8.76126 | -44.15413 | 2026-10-07 16:37:00 | NPP-375 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 49d6f7f1-74fd-3c84-9c2f-08b653f707d7 | -14.92272 | -41.82989 | 2026-10-07 16:37:00 | NPP-375 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 0f1d0ddd-472c-3cc2-8d2a-907d12a56370 | -2.85982 | -40.22342 | 2026-10-07 16:37:00 | NPP-375 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9d716cab-cca2-3f34-878d-78df4dc0f222 | -3.7032 | -40.83469 | 2026-10-07 16:37:00 | NPP-375 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 8e8aa104-04f9-3d2e-b3bf-66b7d8877496 | -6.61699 | -53.01085 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| da84c987-6fad-3445-8565-0e90cca8508c | -6.25051 | -53.45403 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 749e91f2-cdde-378f-b522-3f390b9429d4 | -6.19858 | -52.83286 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dd3804d8-8c7d-3143-8c46-fc623bd2af3c | -6.20655 | -53.46873 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8820eb18-50e1-3a95-bbe9-7d89949998bf | -7.87739 | -44.23241 | 2026-10-07 16:37:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 8c71e524-9eb0-383b-816c-316547acab10 | -9.95536 | -43.56179 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 4d7b1942-286c-309a-9340-9f9fa13b4811 | -3.81078 | -40.46986 | 2026-10-07 16:37:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 27.1 |
| d538a72e-9056-33aa-b68a-d32f4d3e7efb | -4.35739 | -38.8562 | 2026-10-07 16:37:00 | NPP-375 | BATURITÉ | CEARÁ | Brasil | 2302107 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 4627d1e1-0e95-31fc-9cf1-65789961eba9 | -6.94442 | -45.28281 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| c3edba87-d5c9-3a5b-b16f-293566b503d4 | -5.96686 | -43.87442 | 2026-10-07 16:37:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4df95eef-3b4f-31ad-bf09-538a2b512c45 | -6.22502 | -52.79421 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cb3ac05a-8e20-3680-a68f-b294c8776fe6 | -4.10825 | -39.16267 | 2026-10-07 16:37:00 | NPP-375 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 16.0 |


[Clique aqui para ver as próximas entradas](README210.md)
