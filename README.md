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
| 455f21ca-afef-3a87-8e5b-87ae72fef8e8 | -12.5033 | -58.4781 | 2026-05-07 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| c5c75c43-972e-33f1-8a5e-fb93b6594ecc | -12.7819 | -59.0096 | 2026-05-07 00:00:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| d4ad7d7e-eae9-387b-9d09-de711290b818 | -8.8119 | -49.941299 | 2026-05-07 00:05:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4760de8b-75ba-3dc7-a9ec-5c5af725503e | -20.6472 | -43.5098 | 2026-05-07 00:05:00 | METOP-B | CATAS ALTAS DA NORUEGA | MINAS GERAIS | Brasil | 3115409 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f80bc49f-bd5e-326f-8519-348f1c04b1b8 | -10.6363 | -47.998402 | 2026-05-07 00:05:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b5671af-cb81-3cb5-9825-f9a9d4d472e8 | -14.8604 | -48.5425 | 2026-05-07 00:05:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 19be1048-c1b4-3b0b-98d7-d847ae0c5e47 | -9.4012 | -50.673901 | 2026-05-07 00:05:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9833a25c-94a6-3851-9832-3ad7dc630e7d | -12.7616 | -46.954899 | 2026-05-07 00:05:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c924af16-6311-3425-992f-fca9e4ca6acf | -12.9169 | -49.479599 | 2026-05-07 00:05:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9ea42c2-4391-3918-971e-ecb8529a8dcf | -8.8102 | -49.933399 | 2026-05-07 00:05:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44de345c-7d9c-3f57-82a0-03fce7401e66 | -22.0165 | -48.4277 | 2026-05-07 00:05:00 | METOP-B | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f3b8252f-080e-337f-a6ce-1aa271648f9d | -11.7329 | -54.770802 | 2026-05-07 00:05:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22a99a41-7249-3131-acc0-bef464f2b14e | -14.1296 | -45.333801 | 2026-05-07 00:05:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 97e9d22e-d70e-32a4-ab2a-19c2a5163d5b | -14.1312 | -45.3409 | 2026-05-07 00:05:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 65c5ccb0-ad53-3f95-a1a7-8a7912ddeb99 | -18.438 | -54.688801 | 2026-05-07 00:05:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a73068e6-64ce-3de9-a67e-d3d1309586b9 | -8.6375 | -49.519798 | 2026-05-07 00:05:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 674129f0-a30f-32b9-97b7-4019e1bd5da1 | -21.708401 | -48.413502 | 2026-05-07 00:05:00 | METOP-B | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ad5ee716-2758-39da-a61e-36e18229312f | -7.1587 | -48.2323 | 2026-05-07 00:05:00 | METOP-B | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 9f5f6ebf-64b4-3335-97f0-c35ecee20a95 | -10.6379 | -48.005501 | 2026-05-07 00:05:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8935e568-3a1f-3261-b712-d6819d58c35b | -21.706499 | -48.403801 | 2026-05-07 00:05:00 | METOP-B | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 254aa493-edb1-3916-b9ff-2be5e2c60b93 | -12.3417 | -50.004299 | 2026-05-07 00:05:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15f68143-dd1a-3a47-be95-3e28bf4dc13a | -8.7279 | -47.976002 | 2026-05-07 00:05:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0985b54-c2e5-34b2-a025-d11eb3f8a404 | -23.077 | -48.607201 | 2026-05-07 00:05:00 | METOP-B | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 761ab9fc-f232-3bdd-8acd-4a43871caccf | -9.4683 | -47.787998 | 2026-05-07 00:05:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e01624a-7908-342f-b6e9-6537b71fdba8 | -11.6125 | -48.0429 | 2026-05-07 00:05:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1fba8e7-2515-3194-a643-c13f3b3566eb | -13.6513 | -45.543701 | 2026-05-07 00:05:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c71c5a44-59f4-3d8a-86d2-8f6d8c5fe745 | -11.7231 | -54.772701 | 2026-05-07 00:05:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e76fe01a-d76a-3151-8e93-86c60d044549 | -22.012699 | -48.408199 | 2026-05-07 00:05:00 | METOP-B | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a22e4589-dc4d-3653-8f0a-168c9e589715 | -9.4698 | -47.794899 | 2026-05-07 00:05:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6120502a-4abc-3629-9229-662668a23f93 | -11.7363 | -54.787701 | 2026-05-07 00:05:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| addc43ec-8170-3f3d-a195-0eed2ecc134b | -8.7264 | -47.969002 | 2026-05-07 00:05:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fef27078-8f2a-328b-9ae5-cdceefde6461 | -2.6278 | -51.941898 | 2026-05-07 00:05:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f8172d7-5be3-35f2-b972-0a64b365d762 | -5.7777 | -45.113201 | 2026-05-07 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf20723a-e3a0-3476-ac86-0abc2883e53b | -11.6141 | -48.050201 | 2026-05-07 00:05:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2071b051-5a74-355b-a3c5-4d69f366709e | -11.6239 | -48.048 | 2026-05-07 00:05:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 203d0f12-282f-3fc6-bfce-f8e7e3c0fd20 | -21.3328 | -47.073502 | 2026-05-07 00:05:00 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f3ca83bf-c882-3a39-aa00-30bf13d30ec5 | -21.3312 | -47.065201 | 2026-05-07 00:05:00 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 175df6a3-1fa6-3de3-883d-de5a4e6021c7 | -11.6223 | -48.040699 | 2026-05-07 00:05:00 | METOP-B | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ed4e3de-7dc8-34c2-b186-bd4a36f67557 | -20.1094 | -44.995998 | 2026-05-07 00:05:00 | METOP-B | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3f47b27e-ce8e-363b-a4d6-3ea8e04dedc9 | -12.9152 | -49.471199 | 2026-05-07 00:05:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9b28cab-9811-324e-94fc-f1d98c8c440c | -10.5598 | -42.419399 | 2026-05-07 00:05:00 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1beff34d-e6a6-3b7f-87b3-c510f2ca4564 | -12.4937 | -58.418598 | 2026-05-07 00:05:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c06d89ac-d5c7-3d64-a496-b7477e6bb0fa | -12.76 | -46.947899 | 2026-05-07 00:05:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a19c37d3-ec91-30e2-a0d6-dbcb88c22a9a | -14.0431 | -47.597099 | 2026-05-07 00:05:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cf67ae85-18f7-3f68-8dde-7b25d7f855bc | -8.685 | -49.0812 | 2026-05-07 00:05:00 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b031553c-9734-3648-86ff-e89366073035 | -12.3514 | -50.002201 | 2026-05-07 00:05:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13ab1438-6b07-3a0e-8f62-582271861520 | -12.484 | -58.420399 | 2026-05-07 00:05:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 02531b64-4f31-37d5-81f1-e09c5292eaf1 | -7.1021 | -49.919998 | 2026-05-07 00:05:00 | METOP-B | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aa434e1-49da-3591-a67b-3538d2dc87e7 | -10.239 | -52.214199 | 2026-05-07 00:05:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2870d0f1-8fbf-3ab7-ac3f-2e4b5a6a5abe | -22.014601 | -48.4179 | 2026-05-07 00:05:00 | METOP-B | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| dc60b9a8-70a6-3892-9b06-288ce2334aa1 | -5.7796 | -45.1213 | 2026-05-07 00:05:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6109009-07c3-3b32-9d8c-e7f817112d31 | -10.5501 | -42.421799 | 2026-05-07 00:05:00 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f7bdf3a3-85d2-3eb0-8318-b19c313db8e2 | -18.434401 | -54.667702 | 2026-05-07 00:05:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 17dfb4bc-638e-38a2-86ee-8b39432b9e3a | -12.7819 | -59.0096 | 2026-05-07 00:10:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 352466ea-b096-3962-a691-2948c808e84d | -12.5033 | -58.4781 | 2026-05-07 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e636f7e2-b5db-3517-a227-0b3eb9ae0613 | -12.5033 | -58.4781 | 2026-05-07 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| b4f0ab72-5d8f-3317-af48-b9ada487af3d | -7.1513 | -48.2384 | 2026-05-07 00:36:00 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d1db9920-6c01-3f6e-827a-6345f535e5dc | -12.3481 | -50.007801 | 2026-05-07 00:36:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 194188d3-493c-3cef-a81a-e25d919d990b | -13.1848 | -52.686501 | 2026-05-07 00:36:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38fa165d-d66e-341a-bf4a-236c2e53f12c | -11.6078 | -48.052799 | 2026-05-07 00:36:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5a68d64-d267-37f5-b974-84457b8bac40 | -11.6176 | -48.050598 | 2026-05-07 00:36:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7e49ca9-6bd6-326e-a440-639afe5ed57e | -12.4893 | -58.474499 | 2026-05-07 00:36:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a004ab0a-9085-3a32-9e94-376e1a5fcb82 | -11.6192 | -48.057899 | 2026-05-07 00:36:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 774c5707-1ca7-3117-a892-3096d28fff26 | -8.6797 | -49.0882 | 2026-05-07 00:36:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f09cf45c-085b-347b-8029-3b592097d25a | -18.4277 | -54.694099 | 2026-05-07 00:36:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7b0e36a2-d399-3955-a882-550aca92a1ca | -8.3054 | -45.3946 | 2026-05-07 00:36:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3f2a3d51-6939-37bf-9020-93b0718ec73c | -2.6265 | -51.956299 | 2026-05-07 00:36:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf66fd07-2356-380e-af0c-3936d2233c33 | -8.731 | -47.981098 | 2026-05-07 00:36:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a78db8a4-ba45-3334-9ca1-9989a0ed4178 | -12.7561 | -46.964802 | 2026-05-07 00:36:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 578bceea-b3f7-32f9-9886-ba89655456a6 | -8.8054 | -49.937302 | 2026-05-07 00:36:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a112da4-04c6-3aa1-9a34-8f1649b62825 | -2.6245 | -51.947701 | 2026-05-07 00:36:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d65d6cb6-2931-379c-a83e-c414fb9adac5 | -12.3402 | -50.018902 | 2026-05-07 00:36:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8fd352fa-40ad-3a86-a3a3-0911e8785a72 | -10.6416 | -48.008999 | 2026-05-07 00:36:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5cea243a-bf0d-3804-888d-b0ce136609a3 | -18.437401 | -54.692299 | 2026-05-07 00:36:00 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9485c161-8778-3fd1-9b18-75fb125ee92e | -20.6534 | -43.52 | 2026-05-07 00:36:00 | METOP-C | CATAS ALTAS DA NORUEGA | MINAS GERAIS | Brasil | 3115409 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7ddbac32-f44c-370f-b7c9-a444c2c9d386 | -8.7295 | -47.974098 | 2026-05-07 00:36:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ffe6c0c9-48d3-31d1-8739-c1edb4316903 | -21.706301 | -48.426899 | 2026-05-07 00:36:00 | METOP-C | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 55b67310-9eb6-3a6c-9fcb-5edbca71bea4 | -12.7546 | -46.957699 | 2026-05-07 00:36:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3d85d9b-2d11-3711-b9a7-f01c53aa3056 | -21.339001 | -47.0784 | 2026-05-07 00:36:00 | METOP-C | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8b1defe0-6b78-387a-a261-7ec2a8dc038b | -22.013 | -48.434399 | 2026-05-07 00:36:00 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| dab743cd-fb48-364d-85bb-35cd8f58a0f5 | -7.0978 | -49.9291 | 2026-05-07 00:36:00 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d47ce6d-3026-3c29-be0b-ff6b4b99430d | -13.1751 | -52.688499 | 2026-05-07 00:36:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ae23c8b-dc3e-359c-b8a7-d4cd26bf6952 | -9.4097 | -50.685799 | 2026-05-07 00:36:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c6c46de-5088-38ed-aeeb-91655a218c18 | -22.0091 | -48.4142 | 2026-05-07 00:36:00 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2e4e8c4f-c653-3802-bba7-9d8560154bae | -21.704399 | -48.416901 | 2026-05-07 00:36:00 | METOP-C | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bd91c230-a62d-331e-b29e-3dd99828137d | -12.9126 | -49.481899 | 2026-05-07 00:36:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e118c78-72c3-36a5-9af7-98a06882a371 | -14.038 | -47.603298 | 2026-05-07 00:36:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 45cd9791-58e4-3a54-8115-9c3492c56404 | -10.5574 | -42.423302 | 2026-05-07 00:36:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 08bb306b-6ee5-3bcd-88a6-03e0af4e09ae | -9.4077 | -50.6768 | 2026-05-07 00:36:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5db125a8-17f2-35ca-bd8f-50e1e1fb6676 | -8.8072 | -49.9454 | 2026-05-07 00:36:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61c0e837-5d34-38c9-b431-a21e27a0e151 | -11.7281 | -54.792301 | 2026-05-07 00:36:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fba5ce9e-25e5-369c-a073-c319e3684b9e | -22.011101 | -48.424301 | 2026-05-07 00:36:00 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2fd968ba-1cbc-3fb3-9e39-2c4c2ea5b08e | -10.64 | -48.001801 | 2026-05-07 00:36:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d99e0e41-093d-393c-beff-f96c6d7cc0ae | -12.35 | -50.0168 | 2026-05-07 00:36:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7fdb569-b8a6-36f5-97b2-6570d4fc5d0f | -10.5597 | -42.432701 | 2026-05-07 00:36:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c99911e8-985e-306e-8529-d8c755d35871 | -12.7819 | -59.0096 | 2026-05-07 00:40:00 | GOES-19 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 42717ed5-73ee-3115-a334-0bb9478adb5f | -12.5033 | -58.4781 | 2026-05-07 00:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| e4bb563b-306c-3a84-8c5c-d0cf49b06f8b | -12.5033 | -58.4781 | 2026-05-07 01:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 40d505e5-c87d-3b68-a8bf-52ddad8affbf | -18.43686 | -54.71283 | 2026-05-07 01:09:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 59.3 |
| e6bf9fbf-a9a5-320a-813c-95856f94065d | -21.95599 | -57.58883 | 2026-05-07 01:09:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 15.1 |


[Clique aqui para ver as próximas entradas](README2.md)
