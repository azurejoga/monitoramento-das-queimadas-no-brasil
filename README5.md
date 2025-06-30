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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77bbd6d0-f624-347a-801b-b6b0d5e638d2 | -10.55564 | -52.05439 | 2025-06-30 03:51:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91d8b78e-8566-33dc-b286-db1bf7100a54 | -10.65103 | -44.49408 | 2025-06-30 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1497e15d-8a33-3731-b35c-71a740af787d | -13.43245 | -47.83334 | 2025-06-30 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4750bde-903c-357a-96ff-7fea1f508836 | -8.85845 | -47.95367 | 2025-06-30 03:51:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbb5a878-4c9a-3d66-8482-e3ee325d031f | -13.43771 | -47.83479 | 2025-06-30 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac108e78-2fd9-3d4c-b124-54a4d0e837c1 | -9.14545 | -46.3659 | 2025-06-30 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56034d1d-e53d-357f-b6a2-b2733827e96f | -14.43763 | -45.16084 | 2025-06-30 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28e5f609-9b61-3938-9059-2a139fe7ab6e | -16.67983 | -43.88416 | 2025-06-30 03:51:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a99bfc51-4c0f-3af9-b6d1-99e3ff567756 | -15.72828 | -49.55867 | 2025-06-30 03:51:00 | NPP-375D | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e79c5476-2a21-3706-b6cf-81c8a12effe5 | -9.09427 | -47.96042 | 2025-06-30 03:51:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c95ed594-c6c8-3446-88f9-571d6b7f20eb | -9.14105 | -46.36527 | 2025-06-30 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a09d589-ef06-3fee-a08f-4111f3eed820 | -12.19758 | -49.62914 | 2025-06-30 03:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 022dfbc5-3d88-34c0-9b69-1e35b6a2c9b9 | -9.14628 | -46.36627 | 2025-06-30 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a5e8d86-4db7-36cf-8595-1317cd5994a3 | -12.76307 | -44.40412 | 2025-06-30 03:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f970940-6c78-3ae9-b5db-6e4f3f3d186c | -12.75799 | -44.4075 | 2025-06-30 03:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98ec6e9d-03c2-3725-bd11-942e30baebd9 | -10.65263 | -44.48502 | 2025-06-30 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e9cf7c34-d697-3543-a765-aede4e95c2c0 | -15.78837 | -48.16459 | 2025-06-30 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 271632e9-ea6f-344a-a64e-b28068047418 | -10.80046 | -44.2355 | 2025-06-30 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 8cfb2806-ed8e-3a5b-aaa4-0bf00e3e7974 | -15.56922 | -47.8555 | 2025-06-30 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 449d2b6c-5fb3-353e-8add-5bccd16e70b0 | -12.7623 | -44.40829 | 2025-06-30 03:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5970b05c-ac8d-3c45-bbc8-7fa78aad2b19 | -15.98613 | -41.98832 | 2025-06-30 03:51:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| afbe42c5-ba3d-3e47-9f19-76d7fff7a226 | -12.19661 | -49.63393 | 2025-06-30 03:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4e224916-bc70-3964-b1f6-9d8caa3dac2b | -11.28439 | -41.86403 | 2025-06-30 03:51:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f31d1d6d-b138-3946-a4e8-9cfd5f0d0735 | -9.09274 | -47.96845 | 2025-06-30 03:51:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f575af64-7220-386b-9a29-556116679869 | -10.55718 | -52.04692 | 2025-06-30 03:51:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7885076f-78f1-328d-ba77-c2602c599c12 | -13.47729 | -47.71775 | 2025-06-30 03:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20e1f87b-b879-33db-af5f-6e74c7be996c | -10.80331 | -44.24516 | 2025-06-30 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 04a30425-3f70-35b5-8d54-9bbe87c4bde6 | -10.65183 | -44.48955 | 2025-06-30 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| af9226aa-51e4-3d56-8bbb-ec81a3700039 | -15.72741 | -49.56274 | 2025-06-30 03:51:00 | NPP-375D | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 288f9086-cffd-3b26-8750-4eb530bcf474 | -10.80409 | -44.24074 | 2025-06-30 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| a20046c3-3a58-365a-8d55-9562b1b24eb4 | -15.98869 | -41.98636 | 2025-06-30 03:51:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35ffd107-7777-3556-b294-6f65d7e08c4c | -15.78769 | -48.16799 | 2025-06-30 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 07fe05b7-750d-34c9-943e-0978cf14c48f | -11.84615 | -43.801 | 2025-06-30 03:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a4fd972-7b83-31c5-92f1-69f0878ab0c1 | -12.76384 | -44.39994 | 2025-06-30 03:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c5e87d8-5c00-3c49-a95d-dad5f20c4a72 | -12.19563 | -49.63869 | 2025-06-30 03:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 77740e62-2905-3a34-bb62-89b507ab4c59 | -9.10007 | -47.96156 | 2025-06-30 03:51:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0d32580-aad4-3605-8c2b-8295bcedc808 | -15.98971 | -41.98894 | 2025-06-30 03:51:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f5308a4-8bbd-3c11-9210-c988ada837a1 | -12.20267 | -49.63537 | 2025-06-30 03:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f91fc50-d798-3e74-9c2a-7634531966db | -12.75875 | -44.40332 | 2025-06-30 03:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fc74ab3-d408-3855-acb6-f3ed0297be6f | -10.55152 | -52.038 | 2025-06-30 03:51:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a4ca652-4a9e-3c2f-bb59-20421f0bfca7 | -10.79968 | -44.23993 | 2025-06-30 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 786d6a43-f4e9-33df-9559-ee1ebaee3b8c | -10.7989 | -44.24431 | 2025-06-30 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 8b1c327b-60b0-386f-a48d-8e2dc8e387e8 | -22.78519 | -43.75763 | 2025-06-30 03:53:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 10e94abe-04bf-3b83-9450-6a12394a2d0d | -21.01911 | -50.17207 | 2025-06-30 03:53:00 | NPP-375D | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3da5661d-f994-3581-b382-67e51bc8c2b0 | -17.70673 | -42.72123 | 2025-06-30 03:53:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20f242ca-27fa-3ba6-b79a-d9f9808fc62a | -18.68547 | -47.39072 | 2025-06-30 03:53:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0dd596fe-0ae2-34da-9761-0a62da4f2dc2 | -18.04118 | -39.92643 | 2025-06-30 03:53:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| db2f635b-fb29-3c4a-b00e-ffd757027ede | -22.69191 | -44.97686 | 2025-06-30 03:53:00 | NPP-375D | CACHOEIRA PAULISTA | SÃO PAULO | Brasil | 3508603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0432609b-93aa-3cfd-877a-f3c31cea8902 | -21.66867 | -41.94669 | 2025-06-30 03:53:00 | NPP-375D | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 68a9eb47-9cde-3135-af95-7571cd2513e9 | -18.68656 | -47.38785 | 2025-06-30 03:53:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76c241ed-e69b-3526-be83-82ee1b0bd5a8 | -22.8391 | -43.39043 | 2025-06-30 03:53:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a83cff63-15f5-3863-bdb2-5aec5dfc5eed | -17.70595 | -42.72559 | 2025-06-30 03:53:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dad00378-0573-3ce9-9691-60ae89efcea3 | -22.67596 | -42.85408 | 2025-06-30 03:53:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 32b06fed-d5db-3d90-89d7-9a209562b79f | -22.53932 | -48.81568 | 2025-06-30 03:53:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ffcd400-6d67-3648-8bc0-ca885cf9a901 | -22.91892 | -43.49124 | 2025-06-30 03:53:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e3f4c7d5-d261-36a7-adb7-4ee500ae79ca | -19.71602 | -40.35264 | 2025-06-30 03:53:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4461dcba-8e3c-3c2b-a868-5e973cdb388a | -21.22068 | -44.9627 | 2025-06-30 03:53:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bbc8ea33-38db-33cf-a122-bed021610a8d | -22.67763 | -42.8558 | 2025-06-30 03:53:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ed08c80a-2050-3c44-8914-622192c72fed | -19.68271 | -45.37772 | 2025-06-30 03:53:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9b6ac8c-f0e7-3838-bc6e-94c7de175211 | -21.17821 | -43.97983 | 2025-06-30 03:53:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 065570c4-97d4-3e75-ba14-1e48999dbbbf | -22.71398 | -43.8652 | 2025-06-30 03:53:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 101dcbe6-4a61-3985-b18e-d278a64fc14d | -20.92986 | -49.09988 | 2025-06-30 03:53:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 41c04c22-9878-3e01-87a6-c4fba4589283 | -22.90202 | -43.75257 | 2025-06-30 03:53:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 6cd1df6c-8633-33ee-939d-13890897c731 | -20.93366 | -49.09782 | 2025-06-30 03:53:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 19c02c01-bda0-3be1-bb85-badb869bb1af | -22.71638 | -43.86681 | 2025-06-30 03:53:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 32bad840-e0b0-3d5e-b206-39616da9c3be | -22.96776 | -44.85112 | 2025-06-30 03:53:00 | NPP-375D | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 20ac1711-4dc5-3aab-9a38-584c1aa94ba9 | -22.9673 | -44.85312 | 2025-06-30 03:53:00 | NPP-375D | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 38022b6d-2d59-3542-bd69-cc6e3b247aab | -19.04553 | -48.48394 | 2025-06-30 03:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e42ddd99-2725-3ad8-aeba-20a4c2eb742e | -20.90016 | -43.81969 | 2025-06-30 03:53:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4d7b59c5-e1ca-30b5-962a-9e45787c8ee2 | -17.87297 | -53.2636 | 2025-06-30 03:53:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3aafa170-08d4-3706-9fe7-c2ea04580d5b | -22.92247 | -43.49183 | 2025-06-30 03:53:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 014ccd71-30f3-3043-937c-24a849b97bf5 | -18.68546 | -47.39321 | 2025-06-30 03:53:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45c9133c-138b-30bb-bb1e-8649bb777b10 | -21.17956 | -43.98232 | 2025-06-30 03:53:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f50eb697-a1ac-3bc4-adf9-9a98edecbf93 | -19.26642 | -40.00616 | 2025-06-30 03:53:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 38cd2ccf-9b9d-3691-b5b0-9fdcf3971075 | -19.71935 | -40.35324 | 2025-06-30 03:53:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 61fdb236-b8cc-3e23-86a4-dde699d636e9 | -17.78139 | -42.80795 | 2025-06-30 03:53:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1780877-2894-3026-8f78-9b8ef5fe3795 | -17.8714 | -53.2703 | 2025-06-30 03:53:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6f9c08b8-c715-344b-b330-75dd9766f10f | -17.70608 | -42.72292 | 2025-06-30 03:53:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de823646-0389-3afa-b41e-847d2b7403a4 | -20.92867 | -49.09657 | 2025-06-30 03:53:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e9c3ec5f-b449-38db-988d-8acd009cf328 | -19.71415 | -41.48018 | 2025-06-30 03:53:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 298df46f-f5ea-376b-a707-b0f39bc88f5d | -22.16897 | -45.10351 | 2025-06-30 03:53:00 | NPP-375D | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9d982190-7ef2-36e1-999d-d5940e8bdb75 | -22.71758 | -43.8659 | 2025-06-30 03:53:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 445dde0a-7cb9-3392-b86a-c5d19d1c3edb | -21.52101 | -42.62501 | 2025-06-30 03:53:00 | NPP-375D | LEOPOLDINA | MINAS GERAIS | Brasil | 3138401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b8847768-5517-3646-972f-9840557e0af0 | -21.52319 | -42.62629 | 2025-06-30 03:53:00 | NPP-375D | LEOPOLDINA | MINAS GERAIS | Brasil | 3138401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c3af2aa1-0176-3bed-a83a-15e32cee9e32 | -20.93051 | -49.09673 | 2025-06-30 03:53:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| ea6625c7-acfa-3b90-8ff1-efc843611c31 | -22.67512 | -43.04438 | 2025-06-30 03:53:00 | NPP-375D | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dbdf4a2e-f77c-33d3-a1f8-ffc8a5f6163f | -19.26583 | -40.00982 | 2025-06-30 03:53:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5de32349-9f65-3027-b54b-d9b42509e1ff | -28.58676 | -49.44122 | 2025-06-30 03:55:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 15bb54a8-235f-3df6-a240-969deaeb53be | -23.63201 | -46.42735 | 2025-06-30 03:55:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a7a63af5-fa2c-3499-8891-4320b37042c7 | -23.40638 | -46.55716 | 2025-06-30 03:55:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 38c36a55-d1c4-39e9-8706-862a748efae9 | -23.59332 | -47.43958 | 2025-06-30 03:55:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 80e8a64d-5b63-3cc3-aad3-1953fcb69084 | -10.805 | -44.2319 | 2025-06-30 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 258.4 |
| 723c3605-44f0-3d52-ac63-6094a36238e9 | -10.8046 | -44.2553 | 2025-06-30 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 4692d9db-7048-3075-8444-fc49fc54d5f1 | -12.6319 | -54.2087 | 2025-06-30 04:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 0d885bac-73a7-3e4d-b7ab-346a3f2819b7 | -10.8241 | -44.2292 | 2025-06-30 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 7c1604ed-3ff7-3791-8212-40906d1994e3 | -10.7859 | -44.2346 | 2025-06-30 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| f6a45b2c-ace5-3dd6-b400-fc75d9e1fe14 | -10.8241 | -44.2292 | 2025-06-30 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 9e8d51fe-92d1-32fa-8f07-8e437c9b6714 | -10.8046 | -44.2553 | 2025-06-30 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| c4150a0b-47c2-34f8-9f71-39423f0b8b10 | -12.6319 | -54.2087 | 2025-06-30 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1767eb9b-d18b-3888-bda5-63f9f3f4f939 | -10.7859 | -44.2346 | 2025-06-30 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |


[Clique aqui para ver as próximas entradas](README6.md)
