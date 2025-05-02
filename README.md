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
| 20ca74f3-3788-3c5e-8446-23c2899cb3dc | -9.8969 | -37.0677 | 2025-05-02 00:00:00 | GOES-19 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.2 |
| 81c72451-ee05-3f6c-a56f-45f956158c6f | -9.8776 | -37.071 | 2025-05-02 00:10:00 | GOES-19 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 88.1 |
| 5e34c1a0-c338-3c67-8565-2707387c54dc | -9.8776 | -37.071 | 2025-05-02 00:20:00 | GOES-19 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.8 |
| 900d4dc4-4cf8-32b7-9bfb-ee96e9663a73 | -16.31444 | -53.82464 | 2025-05-02 01:09:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e9285dab-fafb-3592-bb7e-38b604396c38 | -13.05005 | -53.73154 | 2025-05-02 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 88ca74ba-61cc-30c5-ba80-0b20f2d3d476 | -13.13804 | -53.25114 | 2025-05-02 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cb1ff515-14a6-3d03-956e-fcb29acd7b58 | -13.04874 | -53.72237 | 2025-05-02 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a089c522-89c1-33f9-b1d8-e9e30164eff3 | -13.04744 | -53.7132 | 2025-05-02 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 7e1664c9-0c35-3f12-8f91-55ffddb93287 | -12.55243 | -57.71249 | 2025-05-02 01:11:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 220f6a07-5525-3f74-aa6f-5aca0dc0efd0 | 1.10755 | -60.51867 | 2025-05-02 01:13:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 06931443-f817-35ca-8ae8-e7f5b46cd8a6 | -6.47553 | -36.15942 | 2025-05-02 03:28:00 | NOAA-21 | CUITÉ | PARAÍBA | Brasil | 2505105 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 54f629af-7bae-3d35-8c94-aeb39cf2bd8e | -4.65064 | -43.19293 | 2025-05-02 03:28:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4129d254-544f-357e-8d52-399d973bc1be | -4.40828 | -37.80995 | 2025-05-02 03:28:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2ab27f05-49e3-337d-9f5d-75827a8a9920 | -5.22437 | -36.14556 | 2025-05-02 03:28:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d329558a-11c5-3794-8c96-780fabbdbadf | -5.65962 | -35.75864 | 2025-05-02 03:28:00 | NOAA-21 | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e29f96e4-bf0a-36f9-896b-9fd86b7e78a3 | -4.8966 | -37.52748 | 2025-05-02 03:28:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1113d049-cfd1-3420-83cd-b031962204bd | -5.1587 | -45.10662 | 2025-05-02 03:28:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 708cd298-d8c0-38fd-bd05-7f22696e9076 | -6.47474 | -36.16413 | 2025-05-02 03:28:00 | NOAA-21 | CUITÉ | PARAÍBA | Brasil | 2505105 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ba8b5694-d130-328a-b6cc-086aed4d77ad | -5.47895 | -35.35686 | 2025-05-02 03:28:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2ec38e22-b874-3838-953b-f6b4ebe6da75 | -5.47712 | -35.36018 | 2025-05-02 03:28:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7ee94a7b-7d90-3d71-a962-71bd7fe439c3 | -5.16564 | -45.10791 | 2025-05-02 03:28:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e6708a9-8c39-32c7-8447-505977998069 | -7.47566 | -34.84442 | 2025-05-02 03:28:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e8542259-c1b9-31b0-b8a2-632f33d9fa54 | -5.66037 | -35.75407 | 2025-05-02 03:28:00 | NOAA-21 | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4fc66716-663d-36b4-aa27-f1626c62f50a | -9.64993 | -35.83596 | 2025-05-02 03:30:00 | NOAA-21 | COQUEIRO SECO | ALAGOAS | Brasil | 2702207 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| cd0c7bd7-9ea2-344a-b54f-6c7cb8cecdb7 | -6.69587 | -42.12755 | 2025-05-02 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e062ab94-e047-3a13-85e3-cf2279fb5021 | -7.9943 | -44.3886 | 2025-05-02 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56fba4d2-c198-3d3c-97fb-73e918ce77da | -9.64773 | -35.82703 | 2025-05-02 03:30:00 | NOAA-21 | COQUEIRO SECO | ALAGOAS | Brasil | 2702207 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 55946524-de5e-35b3-888a-95d13a3e4cd7 | -9.88515 | -37.08121 | 2025-05-02 03:30:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 5c311805-5d6e-3aa8-bdb8-ffc94e6ea471 | -10.97469 | -42.18175 | 2025-05-02 03:30:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b8c2a465-cf40-38bb-82fa-bafb6e965577 | -9.65063 | -35.8318 | 2025-05-02 03:30:00 | NOAA-21 | COQUEIRO SECO | ALAGOAS | Brasil | 2702207 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 443be148-a1be-3ae7-94bd-b6fe3ed9d512 | -7.99559 | -44.39118 | 2025-05-02 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d18359c-aa31-34ec-a9e0-d2a3bccc7e29 | -9.65423 | -35.83242 | 2025-05-02 03:30:00 | NOAA-21 | COQUEIRO SECO | ALAGOAS | Brasil | 2702207 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6c9b115e-5f4b-332f-88e7-70a485a71f36 | -9.88899 | -37.08187 | 2025-05-02 03:30:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3078904d-be82-30f7-9f02-006e676ff699 | -7.99456 | -44.39648 | 2025-05-02 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba862c2e-aabe-3262-930b-0c8526cd942e | -9.88599 | -37.07629 | 2025-05-02 03:30:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 29df402a-2c03-3a12-bc27-24e85dd39d8d | -9.60884 | -37.04076 | 2025-05-02 03:30:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 26aff34e-3f5e-39d6-9461-532961fb9891 | -9.64953 | -35.82803 | 2025-05-02 03:30:00 | NOAA-21 | COQUEIRO SECO | ALAGOAS | Brasil | 2702207 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 17f8357d-5815-396a-a59b-666584fcc361 | -7.99662 | -44.38589 | 2025-05-02 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 120064bc-d5fd-3c7d-a98e-7c7656ee293b | -7.9997 | -44.39501 | 2025-05-02 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9173890-08e5-3e09-8998-4d944e1e1d7f | -10.38689 | -37.13299 | 2025-05-02 03:30:00 | NOAA-21 | CUMBE | SERGIPE | Brasil | 2801900 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5157deb0-0442-33fc-8afa-dc0d4bdc5e84 | -9.64704 | -35.83118 | 2025-05-02 03:30:00 | NOAA-21 | COQUEIRO SECO | ALAGOAS | Brasil | 2702207 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| fe5763ab-f763-314c-8e5f-6d4946cc8ca5 | -9.65283 | -35.84072 | 2025-05-02 03:30:00 | NOAA-21 | COQUEIRO SECO | ALAGOAS | Brasil | 2702207 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a6605e08-d0a6-3aa3-aa47-6b7d67847da6 | -8.37616 | -37.25213 | 2025-05-02 03:30:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0a913f00-0711-3982-83ba-4d9a0d09c750 | -8.07477 | -34.97863 | 2025-05-02 03:30:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 31d786ac-088a-3004-a667-d6e55c7c112b | -9.80292 | -37.48624 | 2025-05-02 03:30:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2bf2db10-7709-35cf-b967-a3cf1beb3ea9 | -8.79612 | -39.77276 | 2025-05-02 03:30:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 7ee4a81a-d792-317f-bb07-06d91c88fd43 | -9.64593 | -35.8274 | 2025-05-02 03:30:00 | NOAA-21 | COQUEIRO SECO | ALAGOAS | Brasil | 2702207 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 74198e4e-8709-324d-b2c0-aa98c280ae43 | -9.64885 | -35.8322 | 2025-05-02 03:30:00 | NOAA-21 | COQUEIRO SECO | ALAGOAS | Brasil | 2702207 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| e6361cfa-056c-3396-91ae-69056169c392 | -9.61268 | -37.04145 | 2025-05-02 03:30:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5786bd6b-d49c-3ef6-a0a0-6b4aedfaf188 | -9.60581 | -37.03527 | 2025-05-02 03:30:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 37ec00e0-aed9-31ba-80d3-5b39fb7a2d22 | -7.99331 | -44.3939 | 2025-05-02 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24b820a7-28b2-3e2b-9f04-46fb68ecf46a | -6.70152 | -42.12859 | 2025-05-02 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9b0689b8-f388-3be5-b470-26929ac4b914 | -8.00095 | -44.39759 | 2025-05-02 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b82a70ba-6457-3c62-98ea-c3ddc253a62d | -10.97996 | -42.18274 | 2025-05-02 03:30:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 08018615-92b9-30c2-96ea-1bac4c46bd8b | -6.69858 | -42.12777 | 2025-05-02 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e19f95f0-c450-395a-92e5-6a942042b1d6 | -9.60662 | -37.03045 | 2025-05-02 03:30:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ab4248ad-98f0-31d6-890b-f741fa56b1a8 | -9.80312 | -37.48939 | 2025-05-02 03:30:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8dd22987-7040-3ced-ba7f-ec85aa05099b | -11.62176 | -38.04987 | 2025-05-02 03:30:00 | NOAA-21 | ACAJUTIBA | BAHIA | Brasil | 2900306 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5811252a-0c33-3576-949e-9301bdfbf653 | -9.60966 | -37.03593 | 2025-05-02 03:30:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 84f8d07f-7bf8-35e8-83e4-764f7ef5e1f9 | -19.71842 | -40.35308 | 2025-05-02 03:32:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 50a29f69-5032-3afb-bc74-b5c8fa3aa77c | -17.1996 | -44.86522 | 2025-05-02 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 998b1120-8efd-3c96-b6bc-b09b0cdaa178 | -15.50001 | -45.93011 | 2025-05-02 03:32:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 706ad92a-d3de-356c-bd3b-0eaaffe188e0 | -20.76601 | -46.76959 | 2025-05-02 03:34:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7815fccf-6c56-35b1-a7d8-ff453c0694e8 | -21.17941 | -43.98293 | 2025-05-02 03:34:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 96d36f5c-7a33-3beb-b1a4-161fc20600dd | -23.61013 | -49.0078 | 2025-05-02 03:34:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6e22672-c6c4-329a-b9dd-7cb32bb18d1a | -29.78003 | -51.17685 | 2025-05-02 03:36:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 066b33fc-9a61-3497-917e-852a3180829a | -4.406 | -37.81011 | 2025-05-02 03:53:00 | NPP-375D | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 28cf6b0c-e9ac-372c-942a-89d842ce59a3 | -8.43267 | -36.20726 | 2025-05-02 03:55:00 | NPP-375D | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fe3716fd-a67d-345c-8012-3963ec5cee31 | -5.16339 | -45.10951 | 2025-05-02 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b94d073c-84ea-35be-bc4b-5f64a0a26ff8 | -9.88398 | -37.07913 | 2025-05-02 03:55:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| d6032de1-de0d-31cc-8e1c-9c1f724cf8ab | -9.61034 | -37.03859 | 2025-05-02 03:55:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 17a97c52-f4fd-30ce-be64-38017f19b437 | -9.80391 | -37.4889 | 2025-05-02 03:55:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 850654d2-090d-36bd-b92d-b8e52c0fa619 | -8.79406 | -39.76961 | 2025-05-02 03:55:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9452af94-7946-3bf6-b2f4-0cd62563f0a5 | -9.60745 | -37.03425 | 2025-05-02 03:55:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c4719d89-1159-3817-99a5-5ae179005934 | -8.07957 | -43.88714 | 2025-05-02 03:55:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 237443e9-8231-301c-bbbc-d7e000d8c1a1 | -5.16063 | -45.10683 | 2025-05-02 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89f75a50-e7e8-39a7-acbe-2c5d44cc972c | -9.64804 | -35.82779 | 2025-05-02 03:55:00 | NPP-375D | COQUEIRO SECO | ALAGOAS | Brasil | 2702207 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| bb750615-8978-378a-8f31-bf3cf293752f | -5.47681 | -35.35632 | 2025-05-02 03:55:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 65f1da26-06e4-367f-9ef2-a2b11dc44984 | -10.38773 | -37.13327 | 2025-05-02 03:55:00 | NPP-375D | CUMBE | SERGIPE | Brasil | 2801900 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 650944fc-e1bb-334a-aa04-ace8469b48c5 | -6.69675 | -42.12613 | 2025-05-02 03:55:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3d8a0fe6-a642-324b-a03d-aa0796842a6d | -4.65114 | -43.19152 | 2025-05-02 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 636709b8-c626-337d-9afc-b6cef80fd638 | -9.88744 | -37.07967 | 2025-05-02 03:55:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 3ec18810-013a-3931-93af-d2a02202186a | -5.15959 | -45.10397 | 2025-05-02 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24378425-1edd-32bf-bc6e-b05c2527a85a | -7.99743 | -44.38581 | 2025-05-02 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 831c0a77-ab85-3f72-8be0-9f4b6d9f21cc | -8.79741 | -39.77015 | 2025-05-02 03:55:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 461b9a30-0d76-374e-8ec3-ac7469882357 | -9.14735 | -40.15936 | 2025-05-02 03:55:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 55207f26-099c-30e7-84f1-c78420021472 | -7.99608 | -44.39359 | 2025-05-02 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7998b10e-84cd-31d2-826d-5fe902ec48ec | -7.9954 | -44.39748 | 2025-05-02 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3104ffe-b97e-3cc1-af65-e8bac96c689e | -6.47625 | -36.16326 | 2025-05-02 03:55:00 | NPP-375D | CUITÉ | PARAÍBA | Brasil | 2505105 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 38222d85-16fc-330d-9aae-8c880a81c45c | -11.62147 | -38.05131 | 2025-05-02 03:55:00 | NPP-375D | ACAJUTIBA | BAHIA | Brasil | 2900306 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 45b64d8b-011f-3139-b468-5d2f2dcbe60c | -8.07381 | -34.9754 | 2025-05-02 03:55:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e4bd4dd5-6862-36bf-90f0-1efdd09ca88b | -4.89674 | -37.52854 | 2025-05-02 03:55:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4f0da401-1b39-3091-8efa-22db2183c666 | -7.99676 | -44.3897 | 2025-05-02 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d65289d-87bd-361c-8692-0d043a68d9f0 | -10.97794 | -42.18021 | 2025-05-02 03:55:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 43b1ebbc-ed0e-3d60-bf28-3b066f98c71b | -8.00382 | -44.39892 | 2025-05-02 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2736b5ac-0bfe-39a9-bf9a-6b4473a87119 | -9.6138 | -37.03911 | 2025-05-02 03:55:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ad3a80e0-6bd8-38e0-bdd9-54bd6b9a2e58 | -5.16422 | -45.10472 | 2025-05-02 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b05bb0f3-ef00-3389-a46a-b281b657903e | -10.97726 | -42.18426 | 2025-05-02 03:55:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b26e5f18-181e-3c5b-a2c9-7114dfbfc2f4 | -9.6474 | -35.83207 | 2025-05-02 03:55:00 | NPP-375D | COQUEIRO SECO | ALAGOAS | Brasil | 2702207 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 23326aef-c4d6-3621-9b5b-46ba7e5a409f | -9.65105 | -35.8326 | 2025-05-02 03:55:00 | NPP-375D | COQUEIRO SECO | ALAGOAS | Brasil | 2702207 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |


[Clique aqui para ver as próximas entradas](README2.md)
