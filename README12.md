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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b6cc123-74d3-316a-8ff0-96ca9a098d67 | -11.43823 | -43.45298 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 164ce3a0-92e2-3f68-b43a-3793790b8423 | -11.41108 | -43.45378 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c11f41ef-4c79-3951-8eb2-1f0d4471875a | -11.44918 | -43.48735 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a033510a-1b9b-33d0-9fa3-33b10b5a6c8c | -11.18717 | -45.1475 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 62d96fdf-f95b-34c9-94c4-76d5b2f3af77 | -11.40692 | -43.44281 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0527a640-a4ae-38e6-9062-18ec4a85398b | -11.62556 | -41.83265 | 2026-09-29 03:32:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1ad0bbef-6ee8-33b8-ae05-e777eb512659 | -11.42753 | -43.46752 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f0215065-e8f7-38ab-b747-150a8c3a913b | -12.2294 | -39.2981 | 2026-09-29 03:32:00 | NOAA-20 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ca5ef7a0-09a1-325c-91c2-49d6a5ac25f7 | -14.12336 | -46.28859 | 2026-09-29 03:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a6e335b1-62e5-3667-b79d-48227be4e73c | -16.35226 | -42.5877 | 2026-09-29 03:32:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1680a185-7928-312b-86b5-191ce104b819 | -11.4104 | -43.43176 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e95770be-e7af-3ef8-9fed-e0b687ac7252 | -11.42237 | -43.46135 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 242573eb-4674-3a83-a0c5-508c25b69054 | -11.38125 | -43.38545 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82b0ddae-7205-3411-835f-55a95a13c042 | -11.6719 | -44.53777 | 2026-09-29 03:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1bff1e1f-ffbd-3f08-a40a-32d74fb2aa72 | -11.4269 | -43.44547 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0df026d7-97b1-3638-84cb-483ff2986387 | -15.93842 | -42.33737 | 2026-09-29 03:32:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 27d772e4-242b-3880-8e4f-d68e133721e9 | -16.34573 | -42.57951 | 2026-09-29 03:32:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c6335ed-b84c-32b9-8f95-74f489b494c2 | -11.40176 | -43.43672 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 56277181-b9ab-386a-814d-5fec9f6ade99 | -11.45016 | -43.48254 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a69f1150-018d-30ca-9dec-d0c5914db963 | -11.4204 | -43.47102 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 30a5a700-a008-37df-8449-c5404e761b62 | -11.38353 | -43.40598 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66e82afa-c577-3cca-9120-5a4c98ec01cb | -11.41599 | -43.42981 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 58b8f641-4953-3add-9d32-da75b59ff3f4 | -15.17003 | -46.13737 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eff102f7-f300-3c9f-b21d-abfaac8038f7 | -15.83048 | -42.56431 | 2026-09-29 03:32:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 251b12dc-3d93-3805-9cd6-5f1c5e86edff | -15.24257 | -43.26894 | 2026-09-29 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 43.6 |
| dadd2298-b7a2-3994-84eb-5b2d843e8e56 | -11.38523 | -43.46173 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c44a2c7-7f68-321a-9293-501ce6d058c8 | -13.37361 | -44.00989 | 2026-09-29 03:32:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2ff9af88-fad6-35af-8384-62f3a809da34 | -11.41463 | -43.44273 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d9dda0d0-7048-37df-8af9-ebe3997be28c | -11.29903 | -43.5479 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb0ef428-1ab2-3f8a-8068-036b7d9285e8 | -11.40373 | -43.42715 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8827112d-46fc-36f6-934b-e36e1e2624f3 | -11.39718 | -43.43385 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 61907a79-c0ed-3adf-a742-8625a0f4ea9f | -11.41819 | -43.45038 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a21680fd-cd8c-3086-897a-f76abc0a1771 | -11.44596 | -43.47153 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8daa6ae5-a992-3e4a-b47f-71986baaea74 | -15.24654 | -43.27829 | 2026-09-29 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 949421c9-b7af-32f6-b7ea-4edc0fa6a515 | -11.17114 | -44.80116 | 2026-09-29 03:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 6d3224d5-fe3c-3d3e-a234-32c5ca700643 | -11.39528 | -43.44341 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be7ec804-9b33-3dd9-8c84-04cba928fe9d | -15.16869 | -46.14332 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82d7a456-2492-33e7-83c4-20f2afd083de | -11.17357 | -44.80191 | 2026-09-29 03:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| f5b792ed-6fa6-37f3-819f-5faaab8543bd | -12.31605 | -46.41663 | 2026-09-29 03:32:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c4ed17b9-c1f1-3b21-b356-8b12ac41f3cd | -15.44969 | -46.1356 | 2026-09-29 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d8d782e5-31fd-3cf3-a93a-ba7d48180f7b | -15.21699 | -46.18028 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72d01814-8f07-3d9f-9d66-875768ab9f34 | -10.28327 | -44.63832 | 2026-09-29 03:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b097eac5-2f9b-3e9e-b24e-d287867f0da9 | -11.40617 | -43.4208 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd58fbda-50f1-3eaa-9f91-1271d82f3dd8 | -11.39237 | -43.45807 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5eda2b3-ae62-3e62-b655-acce55744438 | -11.40331 | -43.4352 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 268462a4-b635-3295-9d73-2781bc761833 | -14.48382 | -43.26756 | 2026-09-29 03:32:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1247a39a-ff1c-376c-9404-2cc518bd5d45 | -11.402 | -45.42343 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b53f587-97b8-3656-b8b1-5a8c7d4d26ce | -11.4263 | -43.44208 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 931b6906-be6a-352b-b613-d372de7514d4 | -11.42557 | -43.47713 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 51501d19-affe-3a87-985c-c8cdec962153 | -11.41525 | -43.46479 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 595ba732-5118-36ca-a525-5e8ddc8a8e6f | -12.87945 | -44.81026 | 2026-09-29 03:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8d7a553-46fa-3c8f-9c9e-d1695147410a | -11.43209 | -43.45165 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 388d564a-ec68-3e2c-84c7-af1892dc6aa7 | -11.43466 | -43.464 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f7237af9-58a0-362d-b641-50d01d0198bc | -11.41886 | -43.45378 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7c7d22e8-922c-3099-8b50-e75e7dc14e87 | -15.50615 | -41.5737 | 2026-09-29 03:32:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f931599c-edf6-324a-ab74-0424753aa28a | -11.40986 | -43.42849 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17ec66b8-d7bc-3ea1-bba5-94964e5e42b2 | -11.40237 | -43.43997 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c97bfc73-c1e3-3667-8c43-fab33f3f6f4f | -15.24586 | -43.27424 | 2026-09-29 03:32:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 142.2 |
| 515116a0-79ae-30f9-83c3-d139c6e2ab73 | -11.44178 | -43.46049 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9a346425-876e-33c6-b7b6-4faad193e64b | -11.43171 | -43.4785 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| acdc8053-9091-3c43-86cc-473f58560a5f | -11.43759 | -43.44955 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 54229b3a-2a66-3130-ba53-caa33d20677c | -11.7091 | -43.45755 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6d45641-f803-340b-9f9e-ab48d466cb71 | -11.41721 | -43.45518 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 54575738-f9e2-30f8-8459-2eb702665f71 | -11.42949 | -43.45788 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3380fd15-9593-354b-b9dc-97152c228c6d | -13.37292 | -44.0079 | 2026-09-29 03:32:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b0c0299-9d09-34f4-90d4-3ceb00bceb2b | -14.08875 | -46.3139 | 2026-09-29 03:32:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa4ff594-7005-3e11-b8b2-e67ed311f6f4 | -12.00254 | -44.93393 | 2026-09-29 03:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a27aeb1-deac-3113-845c-223e1fbdd540 | -11.41082 | -43.462 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 067c6270-291f-3c4c-bae2-17d5d2eea9e7 | -11.18742 | -45.14964 | 2026-09-29 03:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7efdcf76-9182-3ddd-afcf-ce03d02be7ad | -11.44081 | -43.46532 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d0eafe84-3787-316d-a485-96c7de9c9316 | -12.23198 | -39.29681 | 2026-09-29 03:32:00 | NOAA-20 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 36079a25-333e-352c-a218-05ac950af5d3 | -11.43634 | -43.46265 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 43d25b2b-23e8-317e-a3b7-5801db3621ab | -11.4066 | -43.45093 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ccabb319-914e-3552-ba9e-3ff61b292c0f | -11.40888 | -43.43328 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 36f5c0bb-eda2-3a65-a185-04a00f8405b5 | -11.42114 | -43.43596 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 01f02b15-333c-3060-9179-819204a4f5d8 | -11.42924 | -43.46617 | 2026-09-29 03:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 667a544c-0e9d-31b3-9f78-68ed06fe94ed | -21.05543 | -48.84449 | 2026-09-29 03:34:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 8eef8263-af3c-3c51-8486-b5bd6e138a0f | -19.36163 | -41.50498 | 2026-09-29 03:34:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9b5a8526-6d96-3b45-99e1-6b727529951b | -19.3663 | -41.50616 | 2026-09-29 03:34:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e3b54cab-ece1-312a-94e6-c137178ab83d | -20.31311 | -41.94562 | 2026-09-29 03:34:00 | NOAA-20 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 290e5678-90cf-339b-88dc-3ee7e16c5327 | -20.35341 | -40.98202 | 2026-09-29 03:34:00 | NOAA-20 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cfdcfdd5-8670-3cc5-8cb8-2295b0acffc1 | -18.08405 | -44.38914 | 2026-09-29 03:34:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14a74df4-13b0-3bd9-8202-e8ecb51f2452 | -19.46572 | -40.89172 | 2026-09-29 03:34:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| f34cd6f4-b820-36a3-9ab4-4db30ad19846 | -18.10344 | -44.35581 | 2026-09-29 03:34:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae566535-70ff-3abc-94ae-0fc51d0de767 | -18.49448 | -45.13051 | 2026-09-29 03:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 98f08429-85c0-3973-82c3-a9912165bf83 | -18.57446 | -48.41879 | 2026-09-29 03:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5045350d-0d69-3336-91f5-de98334d2c20 | -17.80193 | -44.43406 | 2026-09-29 03:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba4694eb-6f4d-3fa7-9bfd-8a255fd47101 | -17.61589 | -46.66594 | 2026-09-29 03:34:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cb998ae-54e9-3544-8170-6f53a13e1e56 | -17.77239 | -43.01094 | 2026-09-29 03:34:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3a58a65-0411-3b7f-83ca-099ba0d9ac88 | -18.07938 | -44.38287 | 2026-09-29 03:34:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 078c33ee-4803-3eca-baf0-a6a861563e66 | -18.26824 | -42.21154 | 2026-09-29 03:34:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 4c07f44f-5b6b-3301-84fe-3fc171611f60 | -18.84675 | -41.99343 | 2026-09-29 03:34:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f99a5d33-f893-37b1-a306-fb0357dc2e43 | -18.48269 | -45.12698 | 2026-09-29 03:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfb748cd-43fc-341b-bca7-8f20b12f140d | -21.06602 | -48.83194 | 2026-09-29 03:34:00 | NOAA-20 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9d320c0f-1ecc-30c6-a802-81f5f52e74c4 | -19.4647 | -40.89683 | 2026-09-29 03:34:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 846fe7de-dae1-3688-99ae-98c841c37422 | -20.21299 | -48.56201 | 2026-09-29 03:34:00 | NOAA-20 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c33b6945-6149-3644-8afb-cead2b5976fb | -20.43464 | -46.35005 | 2026-09-29 03:34:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbcab63b-1b0c-3854-8eff-0985020c7b73 | -17.6014 | -43.71531 | 2026-09-29 03:34:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8bb8a93c-92a5-32ee-bda1-100e3ac2eeb2 | -21.05718 | -48.83757 | 2026-09-29 03:34:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ffe709c5-6a39-3e32-a238-e5e8e4922665 | -17.97788 | -44.48853 | 2026-09-29 03:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README13.md)
