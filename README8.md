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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d314fa6-e31f-369b-a4b0-c5a91fc3b9bb | -7.7166 | -48.747501 | 2025-09-03 00:24:00 | METOP-C | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 76b90829-1f1a-30b3-8fc3-ae419453bbb8 | -8.3601 | -48.3134 | 2025-09-03 00:24:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f122c45-edd4-34c9-a915-bc4791bb3b93 | -9.9517 | -51.6217 | 2025-09-03 00:24:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a230257-b4f0-330a-8d7b-fbab36f6fd35 | -6.5731 | -44.566799 | 2025-09-03 00:24:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac9531e9-f5a6-395a-b79a-a3dc82a82ac5 | -8.3698 | -48.311298 | 2025-09-03 00:24:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d10e8a1c-6313-3dd2-a71e-72886c919c73 | -2.1295 | -47.996399 | 2025-09-03 00:24:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d87a488-5028-3654-aacb-a4b76a9849d1 | -9.6224 | -47.8461 | 2025-09-03 00:24:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9936a59-a68e-30dd-8eb0-69e38c58de8f | -11.3769 | -43.565201 | 2025-09-03 00:24:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2669fa9b-2f12-3843-9728-cd30ef8dd522 | -10.9909 | -46.8255 | 2025-09-03 00:24:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da967c8d-775a-380e-a6bd-94298cd28cc7 | -6.9683 | -43.283798 | 2025-09-03 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6c9708a2-f1d5-370f-bd94-b429c297c619 | -7.9244 | -46.528801 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47a13c03-b5ab-375e-9b71-bb47ee4b1108 | -7.4906 | -45.334801 | 2025-09-03 00:24:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42bfa6a6-0c70-3a12-8aa6-1dffaab789a2 | -12.8456 | -48.030201 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4cea78b-5081-3d55-a74e-7263ed6618bc | -12.4867 | -47.490601 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| becc6ab0-b679-3cab-9f75-dc2d1f7427d5 | -11.1104 | -44.665699 | 2025-09-03 00:24:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 77e61e6f-8e29-37e3-9061-7bc26e639848 | -5.6826 | -45.950001 | 2025-09-03 00:24:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc94b9fe-fdef-3e51-bd92-058dddfb8fff | -8.0187 | -44.079399 | 2025-09-03 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4c20f199-1bfa-3ffd-8224-fb7aed735f07 | -6.7194 | -42.2607 | 2025-09-03 00:24:00 | METOP-C | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eb926901-8f63-3392-8152-c33c2bcda574 | -6.977 | -43.098801 | 2025-09-03 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e9f63ab8-17c3-3060-b1ed-33ab48bfa270 | -6.762 | -52.793301 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 652177b7-2758-3c5f-8894-52e78ba33854 | -11.5949 | -52.126202 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 499c117b-d1ce-3f15-bebb-bacf854f29a2 | -14.973 | -50.2033 | 2025-09-03 00:24:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 67406c66-095b-3677-b88b-c83161e8a5de | -2.9353 | -49.458302 | 2025-09-03 00:24:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06e23678-1803-379a-81ac-de0acba2ebf3 | -8.8842 | -45.805 | 2025-09-03 00:24:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 01444e59-370f-3a24-ac4d-914b73a45b5f | -20.405701 | -45.695599 | 2025-09-03 00:24:00 | METOP-C | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1483a560-ffff-31cd-acaf-ff4a21a1a0b9 | -7.0034 | -43.524101 | 2025-09-03 00:24:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 063b682c-7829-35b6-81d3-2c01d2905775 | -13.2699 | -46.837898 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 487f72d6-d88d-369e-88f1-c6e388ca2300 | -11.4816 | -43.210602 | 2025-09-03 00:24:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 765f11fa-0d49-3a41-9374-53a3d102eae9 | -5.8018 | -43.2374 | 2025-09-03 00:24:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ddde104-2293-305d-84eb-ab0dfa68539d | -15.5452 | -48.312 | 2025-09-03 00:24:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7f83dc28-eb81-3110-a371-11dc3f03b811 | -14.9633 | -50.2052 | 2025-09-03 00:24:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1505cd06-7a39-3756-93de-7622ae651d44 | -6.542 | -44.566502 | 2025-09-03 00:24:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7089f4c-351a-3df4-a19c-0b825f45118d | -13.2982 | -46.922901 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f812b3f8-05f5-37b1-8641-1cb564a6ab9f | -7.4709 | -44.840099 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0006a483-93f5-38a6-a931-04f88e5ddba5 | -7.0067 | -43.5382 | 2025-09-03 00:24:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 718e3793-9882-309e-b1d2-caff1163ae00 | -5.8729 | -43.011002 | 2025-09-03 00:24:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ecb3f35e-885f-3855-b78e-8e3bfe318d5a | -4.8484 | -42.7327 | 2025-09-03 00:24:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 405a4a10-5416-3cc1-ba27-de6269cca652 | -10.4691 | -50.3372 | 2025-09-03 00:24:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 130f6779-b52b-3863-a66d-c679d83db14c | -9.5129 | -48.905399 | 2025-09-03 00:24:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8cc1d5a8-0749-32cc-8368-2df20ef13c23 | -11.1325 | -46.344799 | 2025-09-03 00:24:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 95275393-a4ae-3c1d-8ff5-d1432543d535 | -10.5242 | -50.4062 | 2025-09-03 00:24:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d038095-1766-3c06-b787-d245c3e3aa16 | -11.6074 | -52.087299 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 748a1070-1d6b-388e-9092-6b2e50a6d2e7 | -7.693 | -48.7332 | 2025-09-03 00:24:00 | METOP-C | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e4a01c33-bd85-378e-a962-b141fe556046 | -14.7791 | -48.150101 | 2025-09-03 00:24:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c0eaf00b-841f-3c7d-bac3-580633f37180 | -14.6171 | -48.1059 | 2025-09-03 00:24:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9cea908a-951d-3de9-b117-d14fe1602053 | -9.6262 | -47.863602 | 2025-09-03 00:24:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7ec52c6-a141-3d55-a77a-f260fa3fcf64 | -6.7793 | -44.4767 | 2025-09-03 00:24:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54dd9163-5c77-31b3-8b31-091de9429264 | -5.7545 | -45.405998 | 2025-09-03 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f215ea74-7475-3a6f-8f22-c625f37e4566 | -13.5239 | -47.0219 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 03c837c4-30fd-3bc7-9e3a-b5a3b827aceb | -13.491 | -46.817299 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fc8f91cc-0c70-3723-8bc5-ff2bcc983607 | -14.5672 | -48.061199 | 2025-09-03 00:24:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ac25b204-b96c-33b1-b619-7630906b6e3a | -11.026 | -45.070801 | 2025-09-03 00:24:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 44639a80-01bc-3c7b-b524-94bc2ba6771b | -14.6074 | -48.108002 | 2025-09-03 00:24:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f7e08632-0e5d-35a5-959c-350b70ad5c14 | -3.196 | -49.110901 | 2025-09-03 00:24:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ef52788-a756-3b8e-8bd9-b8e8aa80751b | -11.6012 | -52.106701 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90ba9da5-6c8e-31a0-9470-37501fcbb6ce | -6.8257 | -44.769299 | 2025-09-03 00:24:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7085207e-bc15-3e1e-8d2f-31253e4f7ffd | -10.2714 | -46.493801 | 2025-09-03 00:24:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36e1cd06-6829-3276-bea8-1fc976a6fb51 | -4.1541 | -46.7967 | 2025-09-03 00:24:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fa978a08-9bae-3bb9-8c72-56262ff77c61 | -6.3393 | -45.665199 | 2025-09-03 00:24:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d49867bb-8c8f-3955-b079-a77cb9b4d2f0 | -5.4391 | -42.8326 | 2025-09-03 00:24:00 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aa98e74b-ca48-31d6-b9a7-54b18dd2de40 | -6.9667 | -43.2766 | 2025-09-03 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 869c0948-c878-35f2-9bb5-c9b2bef74da8 | -7.9128 | -46.477299 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06754266-51c3-3b82-a246-4fd728a31317 | -10.1128 | -46.240601 | 2025-09-03 00:24:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a47a926-1902-35aa-940b-e3c65c2b2299 | -12.891 | -48.051701 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08a4b6ca-16e3-3e44-b836-1f6005c5e69c | -6.9694 | -44.361301 | 2025-09-03 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f2a7a43-2d71-36d1-ae0b-b30f5ac7b070 | -6.7849 | -52.805698 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9275d6e1-5461-3a09-a885-42ff206d99a9 | -7.4922 | -45.341702 | 2025-09-03 00:24:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8712859f-f736-3e34-9b93-f0ffae3dd8f4 | -7.3783 | -49.403999 | 2025-09-03 00:24:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ecbf3bf-7615-3d86-aa0d-966684995af0 | -10.1172 | -47.4324 | 2025-09-03 00:24:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6878dcef-f02a-350c-929e-55ed73da0f7e | -3.3721 | -47.164101 | 2025-09-03 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7769297-ee53-31e9-a10a-ffed25b39acd | -17.9266 | -47.179501 | 2025-09-03 00:28:00 | METOP-C | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fc49e19e-571d-389a-bb5b-e2b14efc398b | -17.239 | -44.8661 | 2025-09-03 00:28:00 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 683db23a-f935-3bb4-a63e-d7b237c4c748 | -17.3596 | -49.181599 | 2025-09-03 00:28:00 | METOP-C | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f642871e-7f61-31cc-a2c5-abdc46a703b9 | -17.937 | -47.232201 | 2025-09-03 00:28:00 | METOP-C | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 06079fdf-2a60-32ae-a1ac-0ef529f5d9e5 | -18.129299 | -51.745998 | 2025-09-03 00:28:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| edeb9526-5a08-35f2-83e3-72a93a2415ca | -20.8934 | -50.0965 | 2025-09-03 00:28:00 | METOP-C | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6881d553-16d3-3519-b700-891216bfb748 | -17.618299 | -46.707001 | 2025-09-03 00:28:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 711a6490-4287-346e-8755-5ddbee1c6970 | -17.5284 | -47.586601 | 2025-09-03 00:28:00 | METOP-C | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8eb1a2c9-e358-3413-99e9-fb3d5ece4078 | -18.1695 | -46.965801 | 2025-09-03 00:28:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 49895632-bd45-3795-b3d6-2cd2e798d9df | -18.1353 | -51.723301 | 2025-09-03 00:28:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 663520ea-60cb-380a-a36f-adf36ed621f0 | -17.9168 | -47.181499 | 2025-09-03 00:28:00 | METOP-C | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| daa6a391-4b64-3d87-b66a-17cbd311c3a4 | -17.357 | -49.1679 | 2025-09-03 00:28:00 | METOP-C | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 95e6c8a9-a9b2-31b1-a5d1-b02063557417 | -18.065901 | -45.9916 | 2025-09-03 00:28:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dbf4c54f-7741-3e40-b465-a968458eb8d5 | -17.5362 | -46.603199 | 2025-09-03 00:28:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 97aeb25d-a65e-33c2-8863-b8d6ae419d23 | -17.9251 | -47.223598 | 2025-09-03 00:28:00 | METOP-C | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2361f9f5-f5e8-39ea-b79d-00925d5caf1a | -16.294901 | -45.688499 | 2025-09-03 00:28:00 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f4e05efe-189c-3311-90a4-3b0ebc92e76d | -17.5263 | -47.575699 | 2025-09-03 00:28:00 | METOP-C | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 637ccb65-35a1-3494-ac4c-e8b2d40ec3d7 | -17.9286 | -47.189999 | 2025-09-03 00:28:00 | METOP-C | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1c8a2264-4599-315b-a81b-2e6705d3339b | -18.139 | -51.744202 | 2025-09-03 00:28:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7179a946-9bb3-3134-a247-da5f4f624247 | -17.9272 | -47.2342 | 2025-09-03 00:28:00 | METOP-C | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 48453fe7-7cec-36bf-8843-7f51f9746508 | -20.890301 | -50.078602 | 2025-09-03 00:28:00 | METOP-C | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 90d2c609-f30d-34da-a152-11ef01aa2581 | -17.9391 | -47.242802 | 2025-09-03 00:28:00 | METOP-C | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 74a7727c-6224-302e-82f3-d0b1e2496533 | -17.9245 | -47.168999 | 2025-09-03 00:28:00 | METOP-C | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b5d11691-de72-358d-83b1-2aed33ced521 | -17.9328 | -47.211102 | 2025-09-03 00:28:00 | METOP-C | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2056bab3-98cd-3f2e-a599-bb6005ea3ef5 | -20.8806 | -50.080399 | 2025-09-03 00:28:00 | METOP-C | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eb229331-8346-3628-840f-075f578cf4b9 | -20.883699 | -50.098301 | 2025-09-03 00:28:00 | METOP-C | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b7e3463f-dcbb-3869-879b-1ac7df12cd7b | -17.538099 | -46.6129 | 2025-09-03 00:28:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 144a292d-e008-31ab-bede-bd3d6125d0b2 | -17.9349 | -47.2216 | 2025-09-03 00:28:00 | METOP-C | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e2945185-cf6e-3360-b67f-9606e21aeb46 | -17.528299 | -46.615002 | 2025-09-03 00:28:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 71090ea3-f9e6-365d-afdc-1f98dea124d7 | -18.063999 | -45.982601 | 2025-09-03 00:28:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README9.md)
