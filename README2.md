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
| 1aa1d24f-79b5-35b7-9532-747bb1b50c32 | -13.3882 | -54.328701 | 2026-07-11 01:04:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09aaa266-1121-3468-be29-e84ad4e1827d | -22.909 | -49.164001 | 2026-07-11 01:04:00 | METOP-B | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| af366ff9-f560-308d-b601-1ad2e0c8098a | -12.0832 | -57.114201 | 2026-07-11 01:04:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 21431e58-f32a-33e7-b5a0-643bdb334255 | -10.3755 | -49.546001 | 2026-07-11 01:04:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0fbe7c4-b5d0-30db-ba2e-b70d40f5e223 | -13.392 | -54.343399 | 2026-07-11 01:04:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b7d64537-9153-3e1e-912e-495cd1c38c03 | -12.8359 | -44.3422 | 2026-07-11 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| edeedf23-f34a-3dcf-ae5d-b32f2d3fb3e4 | -10.3822 | -49.5849 | 2026-07-11 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| bce23a5b-d88b-3a38-81f4-5bf9d60b8d9d | -12.8165 | -44.3454 | 2026-07-11 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| e5174f54-35c7-375b-ba2c-e7663b99c421 | -4.3402 | -47.7645 | 2026-07-11 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e360d917-e866-3436-89e5-31cde62af9fe | -12.8548 | -44.3625 | 2026-07-11 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 33fb487d-8fb5-3540-8a94-7b980f28d090 | -12.8359 | -44.3422 | 2026-07-11 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 3e2ba48c-167d-3efc-a3fc-0070d0303119 | -12.8548 | -44.3625 | 2026-07-11 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| f942dc9f-b8a2-3d16-877a-aaf91f231be0 | -4.3402 | -47.7645 | 2026-07-11 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 2e849ddb-2c87-3293-bee5-8adc6773f8d4 | -12.8363 | -44.3186 | 2026-07-11 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 7cfa6d7b-d2cf-36d6-bb76-defeb20d0f79 | -13.3836 | -54.338699 | 2026-07-11 01:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3d50add-0172-37e9-a371-f8cabdba2aee | -12.0851 | -57.1222 | 2026-07-11 01:28:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57f490f5-7b4f-33e7-a27b-23182e6fc24d | -13.4031 | -54.333698 | 2026-07-11 01:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cdd49cfa-406e-38f7-ab8c-cf4b09429db3 | -10.3948 | -49.569401 | 2026-07-11 01:28:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be6e6ce1-6f68-3caf-89b2-84a101dd3e44 | -22.9244 | -49.188301 | 2026-07-11 01:28:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8e7cc5c5-c4af-350a-8cd9-838852683e73 | -13.3864 | -54.350101 | 2026-07-11 01:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ad3b268-c685-3d34-b154-7de2c90f4372 | -12.0949 | -57.1199 | 2026-07-11 01:28:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 99df22cd-cfb1-35e9-ba33-a7ab3148b4d2 | -13.3962 | -54.347599 | 2026-07-11 01:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d82ffaf-2820-3940-b331-6a78917ba339 | -13.3934 | -54.336201 | 2026-07-11 01:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9ca3e00-9db7-370e-b233-b8ed5018113f | -12.8548 | -44.3625 | 2026-07-11 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| dbee2304-aa35-31b4-ad9f-b4ebd92e29f2 | -10.3822 | -49.5849 | 2026-07-11 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 34cd7d80-c682-3506-8f65-cad8e1dfeec3 | -4.3402 | -47.7645 | 2026-07-11 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 56acf2d9-f8b5-36b0-919b-e6a9477317b5 | -12.8359 | -44.3422 | 2026-07-11 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 53a6acdb-d278-3bc3-a32c-403732d30caa | -12.8359 | -44.3422 | 2026-07-11 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 81b9d7fd-d103-37dd-b991-de5d3475d9bc | -4.3402 | -47.7645 | 2026-07-11 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| cc7f9c60-d425-39a4-82a8-b65ccf8c65d1 | -4.3402 | -47.7645 | 2026-07-11 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 836a633f-52be-3118-9844-d8f86a2a3856 | -12.8359 | -44.3422 | 2026-07-11 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| c60e6b23-5c9a-3796-b969-f08c68129c6e | -12.8359 | -44.3422 | 2026-07-11 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 98942050-beb3-3b9c-978e-ba3f16e7d2ff | -12.8548 | -44.3625 | 2026-07-11 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| ffc5fcc4-9799-3088-9026-d14dd5ff4c22 | -12.8359 | -44.3422 | 2026-07-11 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| c8384c51-2a0a-3a2b-a027-1dbca9517a29 | -3.03818 | -40.11884 | 2026-07-11 03:25:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 28a2b791-14c7-37fb-bb49-c60363e4deaf | -3.03748 | -40.12297 | 2026-07-11 03:25:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea9b5296-c745-3941-abdd-9b3fd5e9c3db | -7.01631 | -42.77999 | 2026-07-11 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 114a4e79-10b1-3380-8739-6273130393cc | -6.07584 | -44.00856 | 2026-07-11 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7b85ee3-d3ed-37fc-89cf-0c0175783f38 | -7.01002 | -42.7701 | 2026-07-11 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e8cfc5c3-3322-3104-904b-9d0525c1d68b | -6.08389 | -44.00406 | 2026-07-11 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 64de1230-0587-3c95-9347-09b929ab7e9e | -6.0854 | -44.00474 | 2026-07-11 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cff5dadb-6ba3-361a-8948-9af0229a547f | -6.49959 | -42.2208 | 2026-07-11 03:28:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| a40f82f1-3c7b-3c41-aa3b-b6241a930d64 | -6.49885 | -42.21341 | 2026-07-11 03:28:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| cd628241-a75e-359b-885f-1a6d937df07a | -9.40419 | -37.81816 | 2026-07-11 03:28:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 259e62da-4c33-3aa6-bb95-613e81e9a4f6 | -7.01541 | -42.77672 | 2026-07-11 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 12d74dcf-b1a8-3ca6-932d-aa18fb1c7d2a | -6.48524 | -42.229 | 2026-07-11 03:28:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a2e0bf94-6704-36dd-8672-0f7d3961b4bc | -7.01096 | -42.77338 | 2026-07-11 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a935e9b6-7978-3166-9f50-1b1069981343 | -7.01528 | -42.78539 | 2026-07-11 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 859e139b-5aea-315b-8a3d-920a51b7cdd0 | -7.00992 | -42.7788 | 2026-07-11 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ca0b1144-3457-33bf-8441-7c401a19d68c | -7.01342 | -42.78758 | 2026-07-11 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9b950f6b-fe58-35b8-8810-ab97f4e16608 | -6.0769 | -44.0029 | 2026-07-11 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2013ba53-0c0c-3201-b763-898fe248866d | -4.82091 | -42.97715 | 2026-07-11 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db97a8fe-8047-3ae6-9c53-f4eb28c5248f | -6.49791 | -42.21848 | 2026-07-11 03:28:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 7770717c-7033-3711-b40e-9543f2961868 | -6.5005 | -42.21572 | 2026-07-11 03:28:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| ab912616-1305-31df-a356-5b20ede6fb79 | -6.67002 | -38.8518 | 2026-07-11 03:28:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a287fcac-7c31-3413-bdba-824b544854df | -6.72681 | -44.37266 | 2026-07-11 03:28:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1aed0ad2-3367-3bd3-a597-8e5375659400 | -7.00802 | -42.78096 | 2026-07-11 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 66ec8cac-f1bd-3055-bbe0-8edf7920ae30 | -5.8251 | -43.47995 | 2026-07-11 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 872cf9af-73e2-3ef2-a641-0a2a7b076bfe | -9.85806 | -36.7714 | 2026-07-11 03:28:00 | NOAA-20 | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f58db130-174a-3943-9f34-2c736000dd43 | -5.82687 | -43.47926 | 2026-07-11 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c84f2d5-ea4e-319e-9926-004fc60d9a11 | -5.13321 | -37.56876 | 2026-07-11 03:28:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f4b7bd6a-677c-349e-9568-36dcff21ce00 | -7.01442 | -42.78214 | 2026-07-11 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7827f5bb-4ab3-33af-82e4-c2c0087bb52d | -9.58686 | -35.69316 | 2026-07-11 03:28:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6da25dbe-dcb8-399a-9991-bfa5d469412a | -5.82398 | -43.48613 | 2026-07-11 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ca7f376-e888-3e6f-aba0-be8b22542775 | -7.00902 | -42.77553 | 2026-07-11 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ea1ec58f-30af-340c-826d-1713aefc17dc | -6.48619 | -42.22372 | 2026-07-11 03:28:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f0cefd5f-3c87-3a0f-9360-35db469ee512 | -9.39974 | -37.81734 | 2026-07-11 03:28:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0d0fb7db-d23b-3edd-9331-ca872e8083d0 | -6.49166 | -42.21747 | 2026-07-11 03:28:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3114bfb0-8e2b-3d42-bfa0-002bcba30f8d | -6.49335 | -42.21969 | 2026-07-11 03:28:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| d1583b01-a376-38f3-8e35-90e8f186582f | -6.07735 | -44.00936 | 2026-07-11 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 75771192-9a15-390c-9e5f-7509f0078cbd | -6.49695 | -42.22364 | 2026-07-11 03:28:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 34806601-c32d-3e9e-9f5b-49e7ba9055f4 | -6.67051 | -38.84892 | 2026-07-11 03:28:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 150d01fa-5e19-307e-a3b9-0bc291734e83 | -6.49072 | -42.2225 | 2026-07-11 03:28:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2c7511f8-1fcf-3880-812d-7af97031e46a | -7.62964 | -37.80228 | 2026-07-11 03:28:00 | NOAA-20 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| df396afb-7d6b-3de5-b9b0-e6371d41d0e9 | -6.4871 | -42.21868 | 2026-07-11 03:28:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 81365810-7e93-3231-acfa-d7d0d4e3b4c4 | -6.49241 | -42.22493 | 2026-07-11 03:28:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 9b25daa3-ebe0-34d8-afac-87eb7a2a141c | -5.82571 | -43.48541 | 2026-07-11 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb7a9e41-1271-3454-a97e-f4c7a05e4c65 | -6.48353 | -42.22645 | 2026-07-11 03:28:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1ad06062-e250-3c95-8ebc-673677e9539c | -6.07839 | -44.00366 | 2026-07-11 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b8e03f3-f251-3778-afd0-674e357ecd8d | -6.49425 | -42.21465 | 2026-07-11 03:28:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| e900582b-3299-38cd-b669-79234c80591e | -12.82021 | -44.33876 | 2026-07-11 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6added38-8679-3e15-a62a-7b12d10075b5 | -12.82132 | -44.33342 | 2026-07-11 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2eaa2d73-c1b7-3ed1-bc88-511367641c52 | -13.25587 | -45.11552 | 2026-07-11 03:30:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b444b9bc-42ca-3eb8-ba27-9b461ebe7409 | -12.8498 | -44.36318 | 2026-07-11 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 307d9d4b-f72c-39b2-a3f4-a804007201a3 | -13.43598 | -43.84428 | 2026-07-11 03:30:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 49a3c8b1-aff8-3bf4-99ff-05cc4aed51fc | -13.31578 | -40.4664 | 2026-07-11 03:30:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6b88b084-5a7f-3d79-9a8e-d1ba54c5ab94 | -12.82545 | -44.34552 | 2026-07-11 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d3a6531a-4664-33b2-9526-c3ecde688ea6 | -13.25057 | -45.10809 | 2026-07-11 03:30:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1096291-a225-33d4-a269-64eeb0d20208 | -13.31684 | -40.46074 | 2026-07-11 03:30:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fe0313b9-4081-36e7-81aa-e66c56e21ad5 | -13.25346 | -45.10631 | 2026-07-11 03:30:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6a9c9030-3013-32d9-996c-ffbb0fc85449 | -13.31759 | -40.46128 | 2026-07-11 03:30:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| dedf764a-5a6d-39a2-8df3-0ae673aa4b0f | -12.8278 | -44.34165 | 2026-07-11 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5d4481fd-6b7e-3c65-ab0e-b2a3f139aa25 | -13.25221 | -45.11232 | 2026-07-11 03:30:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aa6e78ed-3a54-3321-ae40-99b54b45dfb4 | -13.24928 | -45.11407 | 2026-07-11 03:30:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 048b1159-5f5f-3ffc-a7d6-3fb9da37207e | -13.25845 | -45.10349 | 2026-07-11 03:30:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47bbfb33-e25a-3279-9e1e-b44d0897a565 | -12.82666 | -44.34702 | 2026-07-11 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 29b0306c-aabb-3c1b-bfea-d12326a93cd1 | -12.84866 | -44.36855 | 2026-07-11 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 17f5ef05-5ed7-3bf8-8651-de1151a2d0ce | -12.82656 | -44.34016 | 2026-07-11 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c93eab66-6b7e-3f89-a7b9-7770120339a7 | -12.84345 | -44.36178 | 2026-07-11 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef46def4-8a3e-3ba0-b1de-0884005934be | -13.25718 | -45.10944 | 2026-07-11 03:30:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README3.md)
