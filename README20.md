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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a74210f4-5d75-3a95-8c7a-90f4f9243496 | -7.08898 | -59.18774 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 048426e8-7283-36c3-a66b-0d6039fb2e22 | -11.09056 | -50.50491 | 2025-08-09 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5a104a78-b18e-3673-b397-59c402ad96d5 | -12.55862 | -47.10192 | 2025-08-09 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba6e2cef-59c8-330a-a495-03ab560057f8 | -10.74461 | -48.18465 | 2025-08-09 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7d9d337-1ec4-3e3d-89a2-c151410ebb4f | -9.64111 | -48.33626 | 2025-08-09 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e5bba75-b5ed-300e-a500-f9be7e565336 | -11.79496 | -44.92907 | 2025-08-09 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 706ce7dd-f206-3253-b154-65ea3e53abdc | -12.56654 | -47.12576 | 2025-08-09 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 779e2d69-db13-360a-8fb4-c219be5a71e1 | -12.49601 | -47.50683 | 2025-08-09 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cba26ca-eb11-3554-bfa7-a16b3839620d | -13.05079 | -43.84525 | 2025-08-09 04:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| dfa47f30-afb8-3595-b292-3c057cc92953 | -10.13396 | -57.78106 | 2025-08-09 04:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e20b118e-a03d-3bc9-89b7-e74a49c695c0 | -12.49539 | -47.51109 | 2025-08-09 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b868267-1c31-3990-a624-43e8cb9382de | -11.73814 | -47.50294 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79080fb3-5f35-3308-a0c8-8b059e013c39 | -12.71892 | -47.79462 | 2025-08-09 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be1ebd68-ae16-3928-8f92-d8093967a762 | -7.07116 | -59.19171 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 2e744e8a-7bf6-316c-966e-b40c0fffe0f7 | -11.32126 | -55.21541 | 2025-08-09 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbb1291a-ae5e-389d-a8ce-7db748f2013c | -12.03655 | -44.01793 | 2025-08-09 04:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3376e6eb-d366-3278-af4d-0183dd629945 | -13.04481 | -43.85118 | 2025-08-09 04:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 17c95862-31a0-30bc-bb4d-6af6aec8fe3f | -14.16333 | -43.67185 | 2025-08-09 04:42:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89bd0a24-45df-337c-8f82-576aa53053c1 | -11.74056 | -44.95152 | 2025-08-09 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee418cff-9cb5-315d-8d66-e1711f48a99f | -12.56282 | -47.12527 | 2025-08-09 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bc7d7ca6-03d2-3446-a8e6-a3da81f63fdc | -13.61988 | -48.99052 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a69037c0-4ebd-3ac3-b349-02e55f0d99c5 | -13.60706 | -48.98903 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 91c00b95-6884-3a30-b3c2-815fca643750 | -8.30864 | -55.10041 | 2025-08-09 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c722d35-fdec-312b-8929-e3796455fa02 | -13.6279 | -49.00785 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 23401206-143b-3f0f-85bb-cc4717ff650e | -12.49238 | -47.50628 | 2025-08-09 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 005f76b4-f6d6-35b3-9471-8b1f50ad0289 | -8.77332 | -46.42126 | 2025-08-09 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d64a0534-7af9-3aed-8d43-799898f75281 | -13.04444 | -56.84702 | 2025-08-09 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cfd258c-50af-3d17-885e-71e588b21c04 | -11.73948 | -44.95948 | 2025-08-09 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 028a82ea-5b8e-33a5-8bac-2b98c6112b02 | -13.04725 | -56.8559 | 2025-08-09 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd153c2d-7be2-3f78-a3c4-c29f224b4a1e | -12.56718 | -47.12135 | 2025-08-09 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a3855512-121e-3034-a9ed-e52ab2fa546f | -12.71952 | -46.37199 | 2025-08-09 04:42:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4edc8d1e-b9ec-38a3-8951-80da7e61926e | -13.04798 | -56.85184 | 2025-08-09 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d8b42e9-a082-3e64-a07f-ed2dc2c5c092 | -10.00334 | -48.13034 | 2025-08-09 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9938a24f-7d91-3c09-ad46-f9b65448f446 | -11.73999 | -47.49039 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f65b982c-e296-3cd3-aa40-54fe62d12f08 | -7.06694 | -59.1835 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| b6b0a887-e4c4-3988-82e8-92cdbbff7e88 | -11.77662 | -47.39228 | 2025-08-09 04:42:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91bf305f-f97f-322b-82a8-40e0c82dde75 | -11.7431 | -45.02679 | 2025-08-09 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2949fd1a-2b8c-317e-ac3c-ea50f1b5dd05 | -9.99989 | -48.12984 | 2025-08-09 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3d0f047-ce9f-3892-9233-a6b44de63d03 | -15.26648 | -40.33526 | 2025-08-09 04:42:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5b0f55f5-90c5-3ef9-95b2-409ee939913e | -7.05716 | -59.17462 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f7082be7-92cf-37cb-8b73-503626f80aa1 | -12.56167 | -47.10706 | 2025-08-09 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c735572-ca8c-3529-a406-cf632b2bf2dc | -13.61446 | -49.00992 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e50018d-c8db-3403-9ea2-14f74bd65670 | -13.55028 | -55.25397 | 2025-08-09 04:42:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 36305701-b3fe-3ca6-9b8b-962745949d4f | -11.73455 | -47.50229 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17858a83-ee16-3d94-9087-c8d90d0c0d34 | -7.06887 | -59.1729 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 29cfe4fe-0bd0-3186-b62d-af42256fe262 | -11.73281 | -47.48913 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e27b739-4355-3b89-b951-b9aeaf23a48a | -13.04371 | -56.85109 | 2025-08-09 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68fca7c1-80fa-3fa2-aadb-4baf516e1262 | -8.86999 | -47.4771 | 2025-08-09 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1bc544e-dce3-3c2f-9b75-44a78268d0a2 | -7.08189 | -59.16386 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7cbdc6a3-335a-36b7-abb1-f2db1755d743 | -13.54944 | -55.25882 | 2025-08-09 04:42:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a359ef3b-42c1-3bae-af4d-2a1031d8f2cd | -13.60362 | -48.98846 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8656cce9-be4b-35c8-a8a5-caa2ad4a7c76 | -7.08545 | -59.17569 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 2a9d71a7-ad7c-3838-8072-62fd6666e5be | -8.87553 | -47.46952 | 2025-08-09 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a66fe2a0-a512-388f-9263-4505ee7b0876 | -11.74255 | -45.03076 | 2025-08-09 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e21359c-54f2-37cf-9c8a-0c3f5ddb4f83 | -12.55189 | -47.09602 | 2025-08-09 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c803f4c-c229-3532-a4e3-f0804cd0f1fb | -12.71352 | -47.79477 | 2025-08-09 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fd34bc5-7171-3b5a-827d-770c3d775228 | -10.44623 | -44.34602 | 2025-08-09 04:42:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e01c969-fcc5-3032-9ce1-50666f85212a | -7.0559 | -59.18153 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3330f255-e68c-32cb-b3a0-20a1ea258577 | -10.1206 | -57.77331 | 2025-08-09 04:42:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| beba15ba-3d7d-31e2-afdb-f6f971ebfb76 | -11.25186 | -50.18834 | 2025-08-09 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c3c6104-40c2-3c2a-b1e4-d201395fe6bc | -7.24595 | -60.00038 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c0a83f5-00fa-30d4-83f1-0e761c1e2aac | -12.1006 | -44.73348 | 2025-08-09 04:42:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cca729c7-091d-319e-9071-048e76baa404 | -11.08006 | -50.46358 | 2025-08-09 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d4a1d9b6-c9c1-34d6-a7b9-452e13dce928 | -13.61761 | -49.00589 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc24015a-befa-38f6-a9d0-3a205fc0435d | -13.05064 | -43.84216 | 2025-08-09 04:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3489ac5-c955-36c1-9176-4dcd3f82accc | -13.55112 | -55.24913 | 2025-08-09 04:42:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 924acafd-5312-362e-b315-d26be46a1f2a | -9.86374 | -44.70349 | 2025-08-09 04:42:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 95f0696d-9118-3c89-a8da-902788517b11 | -11.73633 | -45.01405 | 2025-08-09 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8210a9a4-ee49-3dc3-b5ef-fb7382c61f52 | -8.935 | -46.73441 | 2025-08-09 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 867f6598-9644-386f-8759-daaee56adf4d | -12.5934 | -47.17489 | 2025-08-09 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2214c43b-ba8c-3efa-90d1-fe4be5b9a438 | -11.73791 | -47.57919 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd0f40cd-4494-3bb0-9363-95e0a7a01cb5 | -12.72021 | -46.36701 | 2025-08-09 04:42:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ecd09a0d-2958-36e7-a1a1-57a3b17da5fc | -13.55493 | -55.2499 | 2025-08-09 04:42:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b533c1e1-491d-36ea-b41a-cfa74db82a32 | -7.07636 | -59.16297 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0b8d42b4-ac07-37e9-ae2d-ca7cd3f234ea | -7.07017 | -59.1657 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 30e5874d-0d07-3204-92c6-76b4df3b9a56 | -7.08677 | -59.16841 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| eed4a6d7-e7df-35d2-839f-5da9d949e994 | -7.08018 | -59.20497 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 819f13da-e723-3d53-9bca-ff28a5604eda | -11.75078 | -47.49217 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94d3fccb-3cda-396a-84ab-036924b01365 | -11.32431 | -55.22123 | 2025-08-09 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b42a5158-d197-3f12-b04a-d2ace0099a06 | -13.61706 | -49.0096 | 2025-08-09 04:42:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7d2cb76-a4ae-3450-a9be-b6a79edee3b4 | -13.17941 | -43.6858 | 2025-08-09 04:42:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29f7ac97-d84d-3bb8-8221-561f1417a8ef | -9.71361 | -61.29723 | 2025-08-09 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f67345d-e433-31b8-8b3d-378e295b2f1d | -12.10115 | -44.7294 | 2025-08-09 04:42:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c8817ea-b75c-304c-b66b-84efe50e0877 | -11.74717 | -47.49162 | 2025-08-09 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d48335c1-d7a9-3492-aba5-79a1b7be0abd | -13.05225 | -56.85258 | 2025-08-09 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de94add0-4c6d-34b4-a7b4-474d1f0d3b71 | -13.0709 | -43.8302 | 2025-08-09 04:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 49118506-cd3f-323a-ad8f-3d0c587977cd | -9.01691 | -51.11189 | 2025-08-09 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4875cf1-f729-30f1-b444-30c85ae08956 | -9.8666 | -49.96317 | 2025-08-09 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 105ae45d-11d8-383d-8d61-69cd9ffa2499 | -11.93324 | -44.54753 | 2025-08-09 04:42:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9a86c3a7-1a98-37fa-b956-6b797e922289 | -7.06142 | -59.1825 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| a45cf589-697f-3354-a599-ee8c641bf443 | -7.08832 | -59.1914 | 2025-08-09 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 53650acf-3e6b-3a50-9434-260804ab925f | -9.71273 | -61.3018 | 2025-08-09 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 238d592c-f829-39c3-af8a-e11bd6a2b33d | -13.04871 | -56.84777 | 2025-08-09 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 99498c12-36d1-3d87-8dbc-aa84c5efc4d2 | -13.07028 | -43.83505 | 2025-08-09 04:42:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 500b78d5-f2a6-3b7d-80a4-4b4101f46fb7 | -10.44734 | -44.33797 | 2025-08-09 04:42:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2782aba6-288b-32a6-a43c-3584ef26253a | -11.32825 | -55.22196 | 2025-08-09 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9f85523f-1770-37d4-86ee-5404f0ae8b4d | -13.03798 | -56.85844 | 2025-08-09 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bec19007-3fef-35bf-a4ac-941c16a32db4 | -14.11102 | -45.41048 | 2025-08-09 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5472f296-a27b-370d-9718-166c738ca1ba | -10.45805 | -48.81029 | 2025-08-09 04:42:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 050b2620-b97d-3c14-bda9-9a606aa4574a | -9.52013 | -45.4105 | 2025-08-09 04:42:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README21.md)
