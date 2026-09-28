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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23ce77f7-51b3-3b2e-afb7-3ee4a279566d | -11.1771 | -44.8064 | 2026-09-28 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 262.6 |
| 05eda7e5-aa04-3cc3-ad6f-f9508e54b96c | -15.1847 | -46.141 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 101.3 |
| f0dd8c40-ccbf-30da-8045-9446579f8b0b | -9.9976 | -50.1179 | 2026-09-28 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| ea857069-ec39-3f49-aac5-db5e04f26526 | -16.6932 | -50.6608 | 2026-09-28 13:10:00 | GOES-19 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 97051030-6991-3dec-9a9b-adf696063a0e | -11.7138 | -50.5752 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| d80a41a8-af9d-39ba-ad18-11623fb9b415 | -12.7417 | -47.2909 | 2026-09-28 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 7ecae9d7-c4f0-3ee5-bad0-ee007e813df0 | -8.3608 | -45.4695 | 2026-09-28 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 0223dd96-4ff3-3e7e-aaac-7994c4a15ed9 | -11.79 | -50.5664 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 89931b38-809c-3b44-81b1-906034268df3 | -8.2291 | -45.4602 | 2026-09-28 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 6a68e46d-b1c2-3260-9db4-16fc010d3441 | -10.2067 | -49.9898 | 2026-09-28 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| eea26a2a-d8a9-3a4a-8946-0f35dca753fe | -12.2119 | -50.3666 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 9bcafa5e-7539-3cc5-abcb-6759036319ed | -11.0767 | -51.3674 | 2026-09-28 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| ebbf6ae7-5767-348a-b4a9-d24c6f385620 | -11.7332 | -50.5516 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 6fba14a6-90fe-3763-b358-039f9fe12981 | -10.7064 | -44.4317 | 2026-09-28 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 074c9019-3cfb-3c48-bcae-b69e3d2afac4 | -11.6951 | -50.556 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 3430d82c-1210-39c2-b2a3-8d6d1775c6b4 | -8.2862 | -45.409 | 2026-09-28 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 268.6 |
| 3867cd7c-282a-3fbc-8eef-4696163d4e32 | -9.9784 | -50.1412 | 2026-09-28 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 159.6 |
| e0efb1aa-bcae-3292-b9c9-d79d35a7766c | -11.809 | -50.5642 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 984f5d2d-acf5-30ee-97ea-9a1a5a257459 | -12.2502 | -50.362 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| b4665abf-0d0c-39b3-b7ce-f5884d3d0096 | -12.6259 | -47.33 | 2026-09-28 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 6902b1f4-f789-3b13-9ef7-2c12920f7a5a | -12.6878 | -45.0192 | 2026-09-28 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 0c952027-2b3f-36ce-9e24-b00661330b95 | -8.2293 | -45.4375 | 2026-09-28 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| faec0bfc-0e80-318c-a873-1aff09b7b627 | -11.5352 | -47.3678 | 2026-09-28 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 164f3651-96f4-35cb-a825-fbdce4b70d63 | -12.3085 | -50.2904 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 3046b439-8882-38df-bca9-cf8542ea69c8 | -12.3088 | -50.2688 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 7de51185-dc6a-3b62-9db1-e117028eaaf0 | -12.6263 | -47.3075 | 2026-09-28 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| e6dcdd98-a70e-3aef-933c-b4bbd2d9c8c7 | -11.1962 | -44.8037 | 2026-09-28 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 394.7 |
| 86f118bf-e0ae-3525-a177-19f1747728d4 | -8.2859 | -45.4317 | 2026-09-28 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 6d4a7cf9-269c-36ed-a958-49be184b040d | -9.9973 | -50.1393 | 2026-09-28 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 0944456f-eebd-32e2-863c-69f81818b543 | -7.449 | -44.6016 | 2026-09-28 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| ac1afdad-1fa9-318f-a8e9-a6895322fe50 | -12.1547 | -50.3735 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 0c1fcc05-c70e-3d5d-8ceb-5b9388ffd3c8 | -8.1664 | -44.4382 | 2026-09-28 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 01afc05c-c72d-3f39-8552-b488f2579a8d | -11.7903 | -50.545 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 273c1cdf-faf6-3475-8711-7f669f03720b | -11.1775 | -44.7832 | 2026-09-28 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 9d5a0f5c-091b-3048-9c45-9f345b1a2e34 | -10.8187 | -57.2192 | 2026-09-28 13:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 7f27793f-c7e5-3f4f-a3a1-805d3021a12c | -11.2154 | -44.801 | 2026-09-28 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 253.5 |
| 6a3f9469-263c-322b-af6d-2980545f8c5c | -11.7329 | -50.573 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 1a6c282e-776f-3777-8ba6-237720bc0220 | -11.1327 | -50.0624 | 2026-09-28 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 296028c1-7cd0-3154-9898-2c3ccd57a698 | -10.7916 | -48.7377 | 2026-09-28 13:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| e37d6e79-b85a-3e95-9e1e-8d19b7796fae | -12.2897 | -50.2712 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8cf50b39-199a-3da5-82ec-2e93b532bf7f | -8.3666 | -46.5263 | 2026-09-28 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 227.9 |
| 730d0aee-f1d9-323b-a788-f24f0e9c6c87 | -12.155 | -50.352 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| ba23b6cd-12a9-33b3-bbe3-58963300f821 | -11.7141 | -50.5538 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| e1346c0f-168d-3eeb-8df5-013f107d41eb | -11.8641 | -47.1004 | 2026-09-28 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| fa9d878a-408a-35f7-b658-3bfcb7875961 | -11.2158 | -44.7778 | 2026-09-28 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| ea796678-2a58-3c22-b1e4-650a0a92697a | -12.4351 | -44.1497 | 2026-09-28 13:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 72628a0a-e813-3a86-ac5e-d28317cd8fb5 | -11.4429 | -44.9072 | 2026-09-28 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 484e9fda-66e7-345c-ba59-784ee6487e93 | -8.4249 | -44.8703 | 2026-09-28 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 7aa34ea8-1240-32d9-99f6-dd61b5866970 | -11.1966 | -44.7805 | 2026-09-28 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 190.3 |
| d7795a88-2e4b-36e0-8101-22b6ea42270c | -7.4869 | -44.5751 | 2026-09-28 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.4 |
| dd75bb70-c107-3581-a6bb-41f279ab3e15 | -12.155 | -50.352 | 2026-09-28 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| b2b8011d-f976-33f0-ad97-d598b3f3ba71 | -15.1847 | -46.141 | 2026-09-28 13:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 5cdb6d95-4595-3890-bf7b-6a9649b5f23a | -8.3608 | -45.4695 | 2026-09-28 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 58e6baeb-8cb8-3e86-b31e-8b86a615232b | -11.077 | -51.3462 | 2026-09-28 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| acc51a3e-010e-3dfe-8cad-9ef3184de224 | -11.7316 | -50.6587 | 2026-09-28 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| b39b665a-9733-3cdc-bec7-e6de8b41977b | -11.058 | -51.3482 | 2026-09-28 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| ebff92ae-8160-37f9-91bd-b594433e399f | -9.481 | -46.3871 | 2026-09-28 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| bc23960f-be08-3c7a-b040-8ac6e7345b55 | -8.1664 | -44.4382 | 2026-09-28 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 402e1dd6-0435-3a04-841b-a3bfda787730 | -8.2291 | -45.4602 | 2026-09-28 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 206.7 |
| d248d0ae-9ad8-35c8-93cf-02355251efd3 | -8.2859 | -45.4317 | 2026-09-28 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 223.8 |
| f22038d9-39b0-314e-b8de-534eeb4ee52b | -12.6451 | -47.3272 | 2026-09-28 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 84a6e66e-94fb-3c4b-8dbe-b2c2d3114905 | -15.0926 | -53.8862 | 2026-09-28 13:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 32bc0b66-6924-3965-b784-57046102b58c | -11.4429 | -44.9072 | 2026-09-28 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| ed380214-2915-3f39-bfd7-33d9702c0916 | -10.8106 | -48.7355 | 2026-09-28 13:20:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 3de66929-55c6-3992-8bdd-04c5c8716e01 | -11.6199 | -50.5004 | 2026-09-28 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 4ccfc2f2-c866-31b8-8423-3ab451d15374 | -16.6932 | -50.6608 | 2026-09-28 13:20:00 | GOES-19 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 6cb9d408-e332-352f-bcbb-ec68e43b10a1 | -12.2897 | -50.2712 | 2026-09-28 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 8efdef73-8c5a-30bd-b055-adb60db90b1f | -11.7828 | -51.0578 | 2026-09-28 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| f2019c50-1375-3aea-8b4d-d98a10793cf3 | -12.6878 | -45.0192 | 2026-09-28 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 84826ed8-3b2d-3ca4-851b-253fe62cf41d | -12.1866 | -50.7767 | 2026-09-28 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| f085c2b1-13bc-3cb5-9ce2-f524abc2232b | -8.2862 | -45.409 | 2026-09-28 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 277.3 |
| e6906364-1aef-3b4a-9fab-c9f55524b064 | -12.7028 | -47.3189 | 2026-09-28 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 136.6 |
| dccb1294-5303-3cc9-89b1-f76b1b4371f8 | -9.4999 | -46.385 | 2026-09-28 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| c0b41438-3028-3982-af04-7304759af3be | -10.2067 | -49.9898 | 2026-09-28 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 9f07efc4-cf5a-3d1d-8e69-a8014ad15d11 | -11.8641 | -47.1004 | 2026-09-28 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 133.8 |
| ef7dc135-85f5-3fc2-8fe9-69646171d36a | -12.7417 | -47.2909 | 2026-09-28 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 31141567-5867-32d2-a8a8-8552aa518c5d | -9.206 | -45.7642 | 2026-09-28 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 73e7dfc5-9e16-3f1e-9e59-6f8c3de10f15 | -13.4205 | -51.3304 | 2026-09-28 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 53dfe0ef-7a4b-3943-b54e-3108880b00b9 | -11.5352 | -47.3678 | 2026-09-28 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 4c3131bc-b80e-35f0-976e-c75ed369c1ce | -11.7313 | -50.68 | 2026-09-28 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| cfd1a41f-1160-3a7a-bd55-3ca1ca03791b | -9.1871 | -45.7663 | 2026-09-28 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 723f7c4e-4be4-3004-b947-43266e3e6143 | -12.1731 | -50.4142 | 2026-09-28 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 2ae58fbf-94ab-3aa9-910d-94fbf8776bbc | -11.0767 | -51.3674 | 2026-09-28 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 4f75bfcf-059c-348c-aea1-14d58705213a | -12.1547 | -50.3735 | 2026-09-28 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 31f7c459-5cf1-3d46-b932-98635b7c3035 | -12.3088 | -50.2688 | 2026-09-28 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 139.5 |
| e03ae9f8-08c4-3d5c-a129-38fddcbf7dc7 | -9.177 | -61.4073 | 2026-09-28 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| bbf32e72-4d30-39d5-b705-84efd01c133b | -11.1331 | -50.0409 | 2026-09-28 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 44851112-f769-368c-8472-682c71e190f8 | -8.2482 | -45.4356 | 2026-09-28 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 54b46faa-0e4a-344e-808f-8a21ad47be3f | -12.2311 | -50.3643 | 2026-09-28 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| cd30341c-c227-3ec9-aa1f-d3c07ef6a875 | -10.8187 | -57.2192 | 2026-09-28 13:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| b05b19c8-4ace-3c79-a30f-c7eca5f04ddf | -8.3666 | -46.5263 | 2026-09-28 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 5368f530-9e9a-399d-b8fa-74aefb9245f6 | -8.2293 | -45.4375 | 2026-09-28 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 603fe082-ad43-3303-a92a-52e529b005c2 | -7.5057 | -44.5733 | 2026-09-28 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 82d579dc-1d15-373f-957c-af7c909d859e | -11.7126 | -50.6608 | 2026-09-28 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| c399352a-4cf4-37c9-9dba-f53a36984bdf | -11.1327 | -50.0624 | 2026-09-28 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 25686f62-abe4-369c-879b-ed396ca6b90b | -12.6643 | -47.3245 | 2026-09-28 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 67c087f5-ee68-3dfa-915a-f3f29a7b810b | -10.2257 | -49.9879 | 2026-09-28 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| b6a4ba99-d019-3da8-9264-9a5791f81454 | -13.0848 | -47.4423 | 2026-09-28 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 27592cd6-23e3-3451-8fed-8f350cfe5be2 | -12.6836 | -47.3217 | 2026-09-28 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 214.8 |
| a8035ebd-269c-3f35-8a2a-de7cad785d58 | -8.3617 | -45.4013 | 2026-09-28 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |


[Clique aqui para ver as próximas entradas](README74.md)
