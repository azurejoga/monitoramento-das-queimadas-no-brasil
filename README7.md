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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08aa8221-e275-388a-aa34-82e9a9f57968 | 2.76438 | -60.31709 | 2026-01-16 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 761a5d9b-c53a-3ebe-ac04-faf87f39e6e2 | 2.7519 | -60.23265 | 2026-01-16 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbaf1271-2b16-3335-b814-72abcbfe68ad | 2.76528 | -60.32317 | 2026-01-16 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2b53f2bf-066e-3fbb-86e9-f33eb973fc6a | 3.06286 | -60.09948 | 2026-01-16 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 217554d1-ee9e-3fff-abac-3c950cf06125 | 2.75849 | -60.3242 | 2026-01-16 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b05e50f-2095-35b5-9470-12cc6d73606f | 2.75939 | -60.33028 | 2026-01-16 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b89a2b3c-9698-376b-be62-4d44223c14b4 | 4.2476 | -60.78648 | 2026-01-16 04:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2133bbb4-a533-31ce-a8d4-07285c3fefc8 | 2.76707 | -60.33533 | 2026-01-16 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fdfb609d-88c9-3262-b8dd-7388f731ed5b | 2.75759 | -60.31809 | 2026-01-16 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d167c49c-c0d9-3794-91a9-569c418999cc | 2.75811 | -60.32994 | 2026-01-16 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5ac03d62-19c0-3b0b-8bc0-0db837d81366 | -4.76209 | -42.80194 | 2026-01-16 04:44:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 419c4734-29da-37be-ae38-3cba227c1258 | -1.80363 | -53.86736 | 2026-01-16 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4da954de-9969-32cc-a4ff-58cf712b31fa | -8.27606 | -48.18323 | 2026-01-16 04:44:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cf638a0-c4b0-3be7-97ed-dcd192aca136 | -6.8876 | -42.84047 | 2026-01-16 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2161f6ba-b727-3115-82f4-e6cb11317219 | -6.98608 | -42.87117 | 2026-01-16 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 96793525-3849-33f7-939f-3d0b3fdb8076 | -6.98674 | -42.86647 | 2026-01-16 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 69bd8afa-3eee-3561-add4-2435686130b9 | -6.99525 | -42.87248 | 2026-01-16 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 3e0589bd-fcf1-3614-9b7e-339955630f6e | -7.22581 | -43.05231 | 2026-01-16 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 72cc3d96-b484-3f5e-b9b8-c41fc30e28d6 | -6.88694 | -42.84512 | 2026-01-16 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 29698138-b4f6-328c-a783-631e2f9b2114 | -7.23356 | -43.06285 | 2026-01-16 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bb73cb53-b671-34c9-b51e-db7ed541da24 | -7.54488 | -45.52604 | 2026-01-16 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6cc7873-0d27-34c9-a1ed-b9c3373b897b | -1.80556 | -53.86822 | 2026-01-16 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 638b2c47-90cd-3b5b-92aa-0db00e555c0b | -4.21955 | -48.47049 | 2026-01-16 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0db722b6-9936-3c80-8ad8-1cf1a70a24fd | -4.06073 | -38.24524 | 2026-01-16 04:44:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 341b1b6e-58bc-305b-8769-a34afebb9858 | -0.23722 | -50.45899 | 2026-01-16 04:44:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99dff550-a07a-36df-b2c3-21facf2d96e6 | -3.66764 | -39.21441 | 2026-01-16 04:44:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a69c71d2-ad33-376f-b428-c7f2a891f583 | -2.61769 | -45.48673 | 2026-01-16 04:44:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b0f5315-2dbc-321f-9ef6-d43222c81b7e | -6.99592 | -42.86777 | 2026-01-16 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| d03ada94-a1b5-3e2e-9c4c-721327056a8d | -7.99922 | -43.2456 | 2026-01-16 04:44:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 38b9e05c-51b8-3519-8170-3b1c994b9891 | -5.45846 | -46.16986 | 2026-01-16 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1eeee580-b2b0-33b7-91f3-b15a33863e94 | -1.80202 | -53.86379 | 2026-01-16 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0de6589-6ea3-3ead-81e0-950c2f5e43bf | -5.13849 | -37.60234 | 2026-01-16 04:44:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9c57f290-21d2-39ec-9aca-73d041c9ae00 | -8.28006 | -48.18003 | 2026-01-16 04:44:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e5b1f869-69ce-37af-90f4-19c8bd22f6b2 | -5.70017 | -43.14939 | 2026-01-16 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5b4b91e6-5564-33d7-8ecf-c1bb9a3ab34e | -4.67595 | -38.04537 | 2026-01-16 04:44:00 | NPP-375D | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a6529ef5-6748-30bc-a618-2dc613e52bd4 | -7.88955 | -46.75338 | 2026-01-16 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68234346-3c1b-3972-acad-4c129e10c5a7 | -7.22902 | -43.06219 | 2026-01-16 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ae7c77be-2c54-3c63-b730-ca958f5e991c | -4.59571 | -45.99421 | 2026-01-16 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed7d044c-0f63-3508-8d90-295c52427aeb | -0.08883 | -51.27827 | 2026-01-16 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a33b8f8d-9303-3275-9faf-aa2b738606d8 | -3.66614 | -39.2132 | 2026-01-16 04:44:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b3e14b6b-be8e-3229-a4a0-3c5007a691ce | -5.45417 | -46.1736 | 2026-01-16 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72e41ad3-e613-3531-bea4-2d6e030b1986 | -8.27949 | -48.18377 | 2026-01-16 04:44:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72216f55-d406-3ec9-a353-4064956c515c | -8.27263 | -48.18269 | 2026-01-16 04:44:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34ac6ebe-1d87-37a5-803c-2777a521b6d2 | -8.27663 | -48.17949 | 2026-01-16 04:44:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a0f6176-bfd4-3218-aa47-cf8434aafbd6 | -8.00002 | -43.24768 | 2026-01-16 04:44:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fe8fe089-1c87-3918-83a3-0aa1d289864e | -6.883 | -42.83987 | 2026-01-16 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4a359b54-eaf7-371f-963f-83a2838efc87 | -7.54386 | -45.52893 | 2026-01-16 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f087b37c-e7c2-3dea-8b79-dbebb4fdafac | -4.68207 | -38.04632 | 2026-01-16 04:44:00 | NPP-375D | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bbcc534a-82df-3109-adb3-297e995c1a63 | -5.68839 | -44.99431 | 2026-01-16 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bc14b67-d7f3-380a-b75b-aa017d3a9a62 | -8.36703 | -41.78842 | 2026-01-16 04:44:00 | NPP-375D | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fbca8e21-104a-3237-86ac-a44e47ca88f8 | -7.99548 | -43.24705 | 2026-01-16 04:44:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 89027c63-9a75-3227-b56a-d06ab2863b85 | -8.27205 | -48.18643 | 2026-01-16 04:44:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41daa53e-b423-312f-8768-fd69349f13c0 | -5.37994 | -43.19498 | 2026-01-16 04:44:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c8fc3773-8069-3b31-b624-1ad79eab5fe0 | -3.66709 | -39.218 | 2026-01-16 04:44:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| deadd4bf-b18d-38db-8284-56ffd2367137 | -5.13777 | -37.60739 | 2026-01-16 04:44:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5ec7366b-8704-3b19-90de-2db8c53f4564 | -7.22515 | -43.05688 | 2026-01-16 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 770a32b3-4d9a-3c20-ad99-ea8091ef3351 | -6.99658 | -42.86305 | 2026-01-16 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9de243db-8b9d-39b6-a5d6-88c40b2dced4 | -6.043 | -51.89264 | 2026-01-16 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16a516e8-f010-3d8e-a0d4-5838ad5853fc | -6.64743 | -43.431 | 2026-01-16 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82ab8571-161d-3894-8e1c-d793c2fefe45 | -5.68791 | -44.99613 | 2026-01-16 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 234ea2cc-5803-37b5-ba01-31d191c57559 | -2.964 | -54.3413 | 2026-01-16 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 907f05e5-e52c-3528-90b4-2fccfc802f66 | -4.50047 | -46.07913 | 2026-01-16 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 09830b48-4288-3e25-9562-13d986d879bc | -7.23423 | -43.05823 | 2026-01-16 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 41731bab-14a4-369d-97db-b2aa666d1336 | -4.06137 | -38.24082 | 2026-01-16 04:44:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c386acbe-e277-3d99-923a-e88a91fc4a47 | -6.98542 | -42.87589 | 2026-01-16 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| c88900eb-82b0-3bef-8f72-6181a3bbfef0 | -6.43538 | -46.77335 | 2026-01-16 04:44:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3cb803c6-e388-31d8-bb30-1ef68039aacb | -7.22449 | -43.0615 | 2026-01-16 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d981584d-b5fd-32d6-ad44-f618f46417ce | -4.33528 | -48.59537 | 2026-01-16 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56d366a8-d98d-3d10-885a-07e8c7e9c31d | -1.8919 | -45.55458 | 2026-01-16 04:44:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fe84980-51ca-376f-9da8-d4d9a8d75721 | -3.66562 | -39.21684 | 2026-01-16 04:44:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 14bc4a02-16cc-3124-b393-09a38c11044f | -1.16794 | -53.72843 | 2026-01-16 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07289717-788a-3ca5-9033-cc826f2ceb11 | -6.90199 | -42.838 | 2026-01-16 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 806268cc-ad68-3cec-bca6-25f88d3dd796 | -1.80424 | -53.86364 | 2026-01-16 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54dc76a5-3980-3511-946d-6383041a1eae | -4.67538 | -38.04851 | 2026-01-16 04:44:00 | NPP-375D | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8fc7b148-cc74-39b6-8272-2b270895ea45 | -1.80143 | -53.86753 | 2026-01-16 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32518d19-792e-366e-94ca-be400c3f5fb1 | -4.06673 | -38.24615 | 2026-01-16 04:44:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f4fd96e6-6ffc-381d-a563-91c19794c610 | -4.05538 | -38.23993 | 2026-01-16 04:44:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| af957349-8057-38ad-93ad-003c58fc2280 | -7.99468 | -43.24497 | 2026-01-16 04:44:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2e069b0e-148e-3515-9bb4-b33da9e8c333 | -4.06009 | -38.24964 | 2026-01-16 04:44:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 3f474af3-5572-3cbe-a709-94a864677539 | -7.22969 | -43.05757 | 2026-01-16 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 38845f8f-9657-36a3-9f1d-53adb6eba02d | -4.21288 | -48.46946 | 2026-01-16 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc363ab1-236f-33f7-8f12-e3f1477e5719 | -4.21621 | -48.46997 | 2026-01-16 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ca21a30-ca5c-3343-9305-27cb179d6d01 | -8.27548 | -48.18697 | 2026-01-16 04:44:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4ae843a-324b-322f-997c-7cddfb4d34d9 | -4.67605 | -38.04389 | 2026-01-16 04:44:00 | NPP-375D | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 516b03f0-875c-356c-a172-ebe81bdbfe3e | -3.70835 | -41.68636 | 2026-01-16 04:44:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c96d17f7-a8e4-3a2a-be47-b280fea036e9 | -4.74512 | -48.12062 | 2026-01-16 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40752ff4-2e2b-34ad-b34f-ce8caa0b7e3b | -4.21676 | -48.4665 | 2026-01-16 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d72cd9f2-6909-33ab-a901-4d677576fcd2 | -11.95076 | -44.21053 | 2026-01-16 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 729e011c-3110-3787-9985-fc936c59dcd8 | -11.74295 | -48.52184 | 2026-01-16 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5289f15-99fc-3d58-b7e6-0a5966dc58b1 | -8.72327 | -48.31518 | 2026-01-16 04:46:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a18ac309-747e-30e0-88e7-272bfeb5ab82 | -10.79029 | -48.22441 | 2026-01-16 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3af445f3-2bf6-375c-b95f-92fdb0a7ecc6 | -14.48035 | -44.33265 | 2026-01-16 04:46:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 984be349-841e-3da8-adfa-3c624827eef6 | -12.5002 | -46.34423 | 2026-01-16 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4231cd7f-4a1d-3b1d-a606-35e381f7bbc4 | -14.20267 | -57.40719 | 2026-01-16 04:46:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5b807fa-03a7-3ce6-80cd-4388e7b5c9f8 | -11.74519 | -48.52314 | 2026-01-16 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7496060c-67ee-32b5-8154-a819fa1ab6d7 | -12.08936 | -43.76668 | 2026-01-16 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d8a5ee15-69ae-358a-b1fc-e0340c0f4298 | -12.65416 | -46.75039 | 2026-01-16 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07e1db6f-0a1d-3af9-976a-577dbd609248 | -13.62047 | -49.1991 | 2026-01-16 04:46:00 | NPP-375D | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4520e0e5-bba0-3cdd-8abb-329432afaa79 | -10.79379 | -48.22494 | 2026-01-16 04:46:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83118818-a8dd-3652-b1f2-cc8d603490ed | -16.6541 | -43.3511 | 2026-01-16 04:46:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README8.md)
