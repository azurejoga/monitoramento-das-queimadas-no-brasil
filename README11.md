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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ecbf34a-0462-354f-b7ff-026bcd5be993 | -11.92206 | -45.38043 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 835860a3-1a38-3aff-9f12-14b56a616e3a | -18.03977 | -46.04864 | 2025-07-04 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f8dea88-8fca-393f-bed6-8ba4335a198f | -9.2023 | -45.33913 | 2025-07-04 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 949d8a06-f815-3784-a021-940f9754e9be | -9.73826 | -48.3513 | 2025-07-04 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcb40322-ce95-33af-807e-b0ed514c85a7 | -10.75998 | -48.2566 | 2025-07-04 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41569f98-5e48-3c66-a239-b46cc381bed1 | -5.54803 | -43.94514 | 2025-07-04 04:17:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19ec2a32-99b9-3988-a6a5-2e4b74566fea | -11.92367 | -45.39174 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac7d811b-1ad2-3698-9527-12fe5da58e6b | -8.69789 | -44.27769 | 2025-07-04 04:17:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b29e1ddd-512d-3fb0-b211-d054949618d6 | -16.73419 | -46.00143 | 2025-07-04 04:17:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66b3dbe1-1495-3de3-b541-d51f664b31eb | -7.0938 | -49.17598 | 2025-07-04 04:17:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5a9078a6-71c0-3759-adbb-87eb32dda87a | -6.73978 | -43.1758 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8cb70cc6-7bfb-39fd-beb3-a8a5705be22d | -11.91915 | -45.39838 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be384720-d53c-3754-b9ad-aa7814c70867 | -10.75916 | -48.25379 | 2025-07-04 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0b6b993-a4d5-3409-9d2a-438de647ed50 | -11.86312 | -44.86692 | 2025-07-04 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02fb698c-af5e-3938-abc7-cc603ac8d4ed | -11.54181 | -47.86624 | 2025-07-04 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e9e7032-7de5-323e-a22d-1a08e52193b6 | -6.99973 | -43.54463 | 2025-07-04 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5135bb6-2704-346b-af9d-a3fa07505087 | -7.11325 | -47.85014 | 2025-07-04 04:17:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a0d9ef1-7d0b-38de-8f44-4f7588012683 | -8.66682 | -45.75589 | 2025-07-04 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 400d2bb3-434f-3667-803a-c0ea81131f48 | -17.65568 | -46.83205 | 2025-07-04 04:17:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a1ebae97-68b4-3750-ba6c-eb8461246e2a | -6.92121 | -43.05863 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1a06135-ab94-3a35-8b6b-525fa7b9a1b9 | -9.8595 | -46.47941 | 2025-07-04 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3f63030-6230-349d-86ea-aa3d8c3d72e5 | -11.92991 | -45.3744 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7c918dfa-fb64-3c62-b90a-8ee04e552033 | -11.4661 | -47.29905 | 2025-07-04 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 204c4b7c-1bd1-3d5a-bf92-c15641e766c9 | -6.72607 | -44.37563 | 2025-07-04 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 268f75af-493c-344e-8e04-09bbbd61279a | -9.2057 | -45.33969 | 2025-07-04 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d006b3e-0d0d-36b6-9139-5c550592ed26 | -6.33387 | -43.75235 | 2025-07-04 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9382860-1d2b-363f-988b-59b76faabdd2 | -6.02093 | -40.28975 | 2025-07-04 04:17:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0ea0c4f3-2aa0-37b0-96e0-415ad8040843 | -6.73142 | -43.14249 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d6e13a1-aa69-3ee7-918d-8d67f454a22e | -7.19939 | -43.58685 | 2025-07-04 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b55dbcdc-519b-37f1-a108-5a6dffa795b5 | -8.52722 | -54.77237 | 2025-07-04 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f43e3fac-f626-3b6d-b05e-51e4febadc50 | -11.86977 | -44.86055 | 2025-07-04 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7c9e5e8-7b6f-34dd-8765-b74a8b252e37 | -11.5492 | -47.86749 | 2025-07-04 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd42ebdf-a9ce-3e53-9954-79c4647d39e3 | -7.18268 | -44.01348 | 2025-07-04 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e125179-2933-3e84-a9e9-9238af8cc107 | -15.22997 | -47.31273 | 2025-07-04 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2a3cd405-1d7f-35f1-b527-0fcac4016d11 | -8.38492 | -44.05082 | 2025-07-04 04:17:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6827d7d6-524a-3973-90fb-944a86467239 | -16.01 | -47.98431 | 2025-07-04 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6083f93a-68bc-3587-b662-1ecb831e490d | -6.27403 | -43.68224 | 2025-07-04 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ce195ec-3c68-3d65-93a7-e1eae8c25031 | -10.34888 | -47.29573 | 2025-07-04 04:17:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35df58f7-c2bb-3668-8a40-a30a9671db5b | -7.91346 | -44.53961 | 2025-07-04 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7b2f721-1b4a-30c2-a8ca-2f8f2fea0442 | -8.30379 | -49.07859 | 2025-07-04 04:17:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15a3ed8d-d72d-3bbb-8060-1dc3645484f5 | -11.54106 | -47.87064 | 2025-07-04 04:17:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f97e454-e034-335d-9ba7-f881988a469c | -7.66184 | -44.33895 | 2025-07-04 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 803acd0e-92c0-3740-8e0b-8d0de0c5cde8 | -7.94355 | -44.84614 | 2025-07-04 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fa132c5-ee18-38ca-b4fb-c7e487043965 | -7.22014 | -43.09188 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5d4a5bdb-25c2-3eb2-92e3-66a4559778a3 | -8.48921 | -49.85773 | 2025-07-04 04:17:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b10b6d0-2e19-3b1f-9cb1-5db1a6366525 | -7.08335 | -44.17086 | 2025-07-04 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a665bfac-94f0-3260-badb-b6f0b4a14601 | -8.97477 | -49.86043 | 2025-07-04 04:17:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 419a0202-fee5-395b-813e-773e4ee10a4e | -11.48763 | -48.44934 | 2025-07-04 04:17:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a6fd8bb8-52aa-3de3-becc-19e7b329328c | -10.30785 | -57.13838 | 2025-07-04 04:17:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc1b2f76-f7ab-3f5a-8a05-aaca9bc89927 | -7.02504 | -44.04247 | 2025-07-04 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b009e023-cf51-3630-8e5d-aea06902e332 | -9.75475 | -48.27745 | 2025-07-04 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b70a28c-7173-374e-b50f-ee7b8c899cc8 | -8.97548 | -49.85625 | 2025-07-04 04:17:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e846a1f-9129-3d06-ba0a-34f32e1a4553 | -6.60934 | -43.88976 | 2025-07-04 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| c768eb9b-1743-31cc-b809-fb9a77725b61 | -9.61232 | -49.01702 | 2025-07-04 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efcd640d-3b32-33da-84b6-da3feb1f4254 | -7.23178 | -43.1044 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 83303feb-a9a6-3f3d-a53f-c6e79488a5d1 | -6.65924 | -43.17384 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a72fe329-37f4-3545-9f98-dc75774a3858 | -8.97591 | -49.85927 | 2025-07-04 04:17:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2bee086c-40cd-38ef-b7fa-21e67aff010a | -7.6107 | -45.74945 | 2025-07-04 04:17:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31a24c55-af22-34e0-9ed3-23584cdff4d8 | -9.08895 | -48.32724 | 2025-07-04 04:17:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4038fa1a-8c4f-368b-9bf4-0ae88db8161f | -7.22569 | -43.09987 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fee187dc-75e3-3808-9cb0-0d8816649232 | -10.65005 | -44.48797 | 2025-07-04 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4119e21c-68d9-3da7-af72-80e6457eaf5d | -11.92263 | -45.37687 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 67a7bb04-ed03-391a-a2d7-aaa4a21bac61 | -6.50036 | -43.64271 | 2025-07-04 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d8b63b7-0f63-387b-abea-5a878e60cd64 | -11.92148 | -45.38401 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f1645917-ceff-32ba-af63-e7b01ebb5c98 | -7.23342 | -43.09397 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7a25ec95-d234-3257-a039-6d779fd56984 | -7.84142 | -44.21563 | 2025-07-04 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd03c359-6424-3b77-bd54-224222595c04 | -6.9163 | -44.00372 | 2025-07-04 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0051d222-cb06-33b0-b493-d8e395b188e9 | -5.91839 | -43.44737 | 2025-07-04 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 649f23e9-94ab-31cd-b845-b7160d774935 | -11.93197 | -45.40419 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cde017d-13dc-307f-95f2-5189b9c06d25 | -19.71831 | -40.35434 | 2025-07-04 04:17:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4acffac6-c1e0-34a4-9522-1de09241765f | -10.58873 | -49.45704 | 2025-07-04 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ff7ebdb-2346-3705-90d8-a2c82402220e | -6.8475 | -43.31015 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 10a41ba8-7f3b-377d-b333-b682f4284be9 | -6.7458 | -43.13765 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 201ca722-589e-3869-be19-a9e51421a7d9 | -16.03673 | -51.16496 | 2025-07-04 04:17:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb05a651-4950-3b8b-a88a-de1a762720a3 | -8.85482 | -47.95275 | 2025-07-04 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40625b07-b47d-39ce-911d-c1959bb7b8ff | -6.84805 | -43.30668 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 90935948-0802-3208-b11d-a8129b09b641 | -15.98773 | -43.61378 | 2025-07-04 04:17:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5184988e-3b8f-3762-ab96-b6bb1aa02e51 | -14.38753 | -56.3789 | 2025-07-04 04:17:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7447d6c-9cd8-3940-821c-139a92f035a7 | -7.07899 | -43.2156 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8ace7db8-09ff-39cc-b919-08dad3933202 | -10.98041 | -45.10849 | 2025-07-04 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f470215-973c-361c-9745-0c02918d1a10 | -6.28457 | -43.68033 | 2025-07-04 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9209fc88-7075-3a6e-9fc6-8705da0a29f0 | -6.89783 | -47.05175 | 2025-07-04 04:17:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b724479-f5d8-3fac-88d7-6b4d480292c5 | -6.11445 | -46.18478 | 2025-07-04 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d39c23ce-a003-3630-9d02-2769c867b2d9 | -7.22623 | -43.0964 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 9269a192-e2b2-3f8c-841e-8d0b97b29bc0 | -9.79952 | -48.25167 | 2025-07-04 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c21cb2ce-cffe-347e-8633-7fd14d5645d9 | -8.9976 | -47.44492 | 2025-07-04 04:17:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b68ee194-fdf0-3e9d-916f-394fa040754d | -6.84478 | -44.9444 | 2025-07-04 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fb50a9b-9524-3136-8021-2bf8ab8a65db | -6.74365 | -43.17286 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2f0c1532-538f-3857-99ff-10f3a2b5bf40 | -7.22678 | -43.09292 | 2025-07-04 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| d2077883-d6e8-3c57-9b36-89e60e5b0b65 | -8.67375 | -45.75694 | 2025-07-04 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7eaa2818-7530-3652-81cf-3aa4aa115cf5 | -11.62772 | -46.92416 | 2025-07-04 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59aad405-98e9-3870-b5cf-1ed76bc03d8f | -10.98491 | -45.10188 | 2025-07-04 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b9ead14-f26a-3ffd-872a-ba93860674a7 | -6.74525 | -43.14111 | 2025-07-04 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a23f0a71-baae-34ad-831a-2ea0b5634c6b | -7.3044 | -45.36477 | 2025-07-04 04:17:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1def616b-e107-32a9-a318-5fa793f8d9e6 | -10.4757 | -45.11476 | 2025-07-04 04:17:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f29b5780-844b-3443-9c40-65817e661b0a | -9.08503 | -48.32656 | 2025-07-04 04:17:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 093568d0-76fb-3c8e-998e-15b694e9a58f | -16.74107 | -49.26491 | 2025-07-04 04:17:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ab3480b-d5e0-3a74-b2bb-b89a18243e02 | -12.1665 | -45.52836 | 2025-07-04 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72a93e9c-3655-38b5-a6b2-ed908d3af57e | -8.86763 | -47.27798 | 2025-07-04 04:17:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e38618b7-7ce5-3807-871b-809862a0bfec | -9.79475 | -47.74175 | 2025-07-04 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README12.md)
