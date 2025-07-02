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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42fdc300-5c0c-3072-99f0-bc3de161829e | -2.66164 | -47.39923 | 2025-07-02 04:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91115c42-c4d2-374c-b2aa-49e93e2fbf0e | -6.27411 | -43.67691 | 2025-07-02 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d73aa95e-ac0f-3a3b-9e6d-72718445f9eb | -7.21611 | -43.09214 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d074b1ec-77ba-326b-81b9-88e3a2bbfe29 | -6.29036 | -43.67641 | 2025-07-02 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 51673cb9-08e8-3b49-8df8-360bc0e5598a | -4.31554 | -48.07643 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc26eb3f-6110-3e3a-9358-4e3feed4b524 | -6.84889 | -42.79137 | 2025-07-02 04:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b5aef752-b705-3e7e-9c27-ae75478466b3 | -4.28251 | -48.18975 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a892c6b2-b190-3b22-a1ab-d163afbecba1 | -6.95408 | -42.88659 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 38e1c24e-244a-306d-8183-b0e14f8dd432 | -3.42968 | -52.79786 | 2025-07-02 04:51:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 99149393-360c-3c1e-9882-8702d346f605 | -4.55858 | -48.00229 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de924e43-72dc-3143-a651-720b29d234e2 | -5.62917 | -44.26358 | 2025-07-02 04:51:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ece5e74f-153e-3838-8f45-db09a45319ca | -4.10966 | -47.93533 | 2025-07-02 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a35dee7-6707-3352-a646-90f32b25b5bf | -6.84322 | -42.79066 | 2025-07-02 04:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 797fc155-895c-3aaf-a927-d270acda0a51 | -6.96112 | -43.08334 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96c10697-e78f-3a1e-bcde-eca58ec11936 | -6.27318 | -43.68366 | 2025-07-02 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 8b5dc59b-eecc-36c0-ac0c-3241417da3b4 | -6.2789 | -43.68127 | 2025-07-02 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58510a5c-8578-30dc-b720-31f455326ed7 | -6.27363 | -43.68042 | 2025-07-02 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| dafa1c6a-76e3-38be-bad5-2346d02712df | -2.89554 | -48.02932 | 2025-07-02 04:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18aa05ec-1c8c-3a9c-9ad3-0a3e363d7f93 | -3.3183 | -48.71613 | 2025-07-02 04:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d5616e0-bbc1-3d3f-89f3-54d889f37ad2 | -5.62141 | -43.65916 | 2025-07-02 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cf3dbb1-c5c6-34a8-a846-8af23d960247 | -7.21293 | -43.08882 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 2fe0fa7c-9f17-3ed4-8d37-f8d3f517b1d3 | -3.03403 | -49.43272 | 2025-07-02 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a53b104a-843d-3ba3-9af8-22d1f4fc3c02 | -6.2699 | -43.68004 | 2025-07-02 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3839a796-03ff-3b66-9588-5ed3bbb0410f | -4.18959 | -48.14054 | 2025-07-02 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc2d1a41-de6b-30ad-b516-6fa01089be71 | -5.62155 | -43.65402 | 2025-07-02 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4f24407-6c4e-3bee-939d-b4162f2fdce5 | -7.21188 | -43.09624 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 15b32aa8-a30e-3953-aea1-04664a2ed713 | -3.90228 | -49.08604 | 2025-07-02 04:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4aab1f9-bb78-3127-8760-aaeae73cef55 | -6.27568 | -43.67741 | 2025-07-02 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 288429b5-2601-3184-b430-f441bd927708 | -4.54029 | -48.01884 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 731425b0-4a9b-30c8-b086-d63a20f9ab2f | -6.96666 | -43.08427 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c080983-9756-353f-81c3-ed65605f1c00 | -5.8775 | -44.79707 | 2025-07-02 04:51:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f483515-b55c-306c-9371-53b0f19ee2f4 | -5.62622 | -43.6629 | 2025-07-02 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2871dbda-b4bc-3dfe-9118-090012014988 | -7.21104 | -43.08758 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c31870db-8df9-3686-bbf2-9a38ec26c255 | -6.28991 | -43.67965 | 2025-07-02 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3b81b229-230b-32ad-83f5-b33ed51dfa63 | -5.88161 | -44.80294 | 2025-07-02 04:51:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad05cf73-d239-333b-8e37-79fe4ddc847c | -7.20646 | -43.07934 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b567ef6a-20ad-3d3e-a46d-965b3e38cbfa | -5.07055 | -43.73291 | 2025-07-02 04:51:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bc0f3fc-71b5-3c5b-9eeb-e1ca8ca9e972 | -6.27518 | -43.68086 | 2025-07-02 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 85eb032b-c0eb-34e7-ba26-bd9daa5a9321 | -4.17388 | -42.0272 | 2025-07-02 04:51:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5da53342-2d5e-3a67-be8c-6ce4a669d494 | -5.61617 | -43.65839 | 2025-07-02 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69dcac8b-9d8c-3b69-b246-30c3a31e7028 | -5.91674 | -43.45434 | 2025-07-02 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4ba57e00-633b-318b-b3c3-195141a8cf82 | -5.61662 | -43.65535 | 2025-07-02 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d099fe99-cdd7-315b-8e5e-3d4b0b914fc9 | -5.62596 | -43.66082 | 2025-07-02 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1ca361b-cc1d-3139-877e-46dc64fc48bd | -4.2863 | -48.19032 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fab482f9-3e16-344a-a2cb-fb31cc17a156 | -3.03693 | -49.43713 | 2025-07-02 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18316b6b-1da7-38ec-865c-fea48b0e3f50 | -6.28373 | -43.68537 | 2025-07-02 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6263d5d8-6558-368f-a955-6d70c7c8d73a | -4.55953 | -48.00527 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff7c4215-c5b6-349f-bac6-4a0e2db97931 | -3.31466 | -48.71556 | 2025-07-02 04:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ec2057c-0aa0-3de3-a07c-6fa8e688e998 | -5.62231 | -43.65301 | 2025-07-02 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56ec63c1-0723-3f29-b21f-3047aec08977 | -6.02172 | -49.23021 | 2025-07-02 04:51:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c90fe090-69a6-3678-b703-5e4e27dbf5d8 | -5.62097 | -43.66222 | 2025-07-02 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d16735e9-3402-30bc-889e-5e58e26c6b0a | -7.20546 | -43.08683 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 1cb683e8-0119-36ad-be6a-a0fbeaf496e6 | -3.03632 | -49.44099 | 2025-07-02 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 08f738ec-3203-3929-b84e-03960e525596 | -6.02537 | -49.23077 | 2025-07-02 04:51:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbd83bc6-9cf2-3a00-9ef0-4e5146298051 | -6.29565 | -43.67715 | 2025-07-02 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1755287f-8137-384d-a265-eaed22e3afd7 | -5.62113 | -43.65709 | 2025-07-02 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0a61d50-4c95-3100-99d3-91fc442a4159 | -6.21243 | -44.19852 | 2025-07-02 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 83d9baf9-680d-3fac-8a79-a7962f519c5f | -5.071 | -43.72983 | 2025-07-02 04:51:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7fcd4c6-d9c9-3725-a156-3b23deb4526d | -7.20788 | -43.08435 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| db62e6e7-9d3c-3566-94ac-a16f2c52f823 | -3.20655 | -41.84278 | 2025-07-02 04:51:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8fa47bf-d217-368f-9fa5-1e5f83405246 | -3.03342 | -49.43658 | 2025-07-02 04:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5b89e60-af30-313b-8adc-ea59c1279f03 | -6.28418 | -43.68212 | 2025-07-02 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ff6c124-fc61-36df-ac3c-21dbb344467a | -4.32245 | -48.08222 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5080fd5-e057-31da-bf9a-05a77be5458e | -6.95817 | -42.89864 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 0263fb0c-8d80-3e8a-99bd-104c73359cc2 | -4.03479 | -48.06745 | 2025-07-02 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 378be966-18ac-3449-8829-191336179ea4 | -7.18259 | -43.1735 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7d405902-81b3-3ba9-b7b4-3ff9382c63ef | -6.27845 | -43.68455 | 2025-07-02 04:51:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4bd7ef75-c048-37fe-98a0-720610877a74 | -7.18814 | -43.17418 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 765a2371-1235-3586-befa-1bee74b34b60 | -4.31481 | -48.08114 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a7fdea7-742c-317f-b62d-67683bea3f40 | -7.20683 | -43.09176 | 2025-07-02 04:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 480120c3-99bb-3a75-9bf0-44ca97d06156 | -2.43306 | -48.80178 | 2025-07-02 04:51:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6db8e46f-dd39-3408-8832-10a5cf24b8d1 | -4.37746 | -48.06886 | 2025-07-02 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97a7378c-b7c0-324c-8259-88a5bc810de3 | -11.57859 | -54.56396 | 2025-07-02 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eeb64ccb-8d02-3048-89a2-305ddb686854 | -10.89296 | -56.45266 | 2025-07-02 04:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7e899b2b-f91b-33f6-b5d9-4255a2520383 | -9.22696 | -50.04222 | 2025-07-02 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8706d0a0-60c6-3798-b326-2684e880eafb | -10.88586 | -56.45144 | 2025-07-02 04:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7ce148ba-5437-3f82-bdcf-c7955a2c7a09 | -10.15468 | -53.92271 | 2025-07-02 04:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd00d11d-7bae-3aa5-a481-4ab4b1fb06a4 | -9.23246 | -50.03004 | 2025-07-02 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 521542d8-b525-3836-a3c6-a91258557cb7 | -9.85571 | -44.70161 | 2025-07-02 04:53:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d1ea371-afca-36b9-abdd-3bc666853f5e | -11.23662 | -49.49378 | 2025-07-02 04:53:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b717ee7-6575-39cc-a8cc-b8e8a274d652 | -10.29696 | -57.13494 | 2025-07-02 04:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b0053dd-987c-3749-864a-2efa4aee6402 | -9.2306 | -50.04277 | 2025-07-02 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6463f23-6d45-37a8-8278-c1f1e7b72f0c | -10.99197 | -49.38817 | 2025-07-02 04:53:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86b70b0d-9c2b-34c9-8dfd-de078e2af009 | -9.85053 | -44.70081 | 2025-07-02 04:53:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33bd9001-2ce3-3136-be5b-bbf9f637db83 | -11.74556 | -54.72333 | 2025-07-02 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b782657-0249-3d3f-b78c-d398de437030 | -11.32892 | -51.44757 | 2025-07-02 04:53:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1f8700e-2913-3094-8fdc-2b999e45e14f | -9.23184 | -50.03429 | 2025-07-02 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7763c65-f48e-3280-b452-3fec8072bffa | -9.70232 | -56.1831 | 2025-07-02 04:53:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e40f2a6-1b9b-3476-810d-894df09b330f | -10.86133 | -53.77838 | 2025-07-02 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1325fbc2-3efe-3c25-a6ea-5e12a76d81ce | -10.3036 | -57.14067 | 2025-07-02 04:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1e2bf5c-063c-3334-b20b-1c72a4bacc92 | -9.25615 | -57.52393 | 2025-07-02 04:53:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0b6f87a-0473-3735-ab6f-b1edf9be38a3 | -9.23486 | -50.03908 | 2025-07-02 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2fcd682-f75f-356c-ae4f-9b4d4d373cd6 | -10.89539 | -54.05404 | 2025-07-02 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d092572-878e-3abd-ba58-eeadd29967b2 | -10.87453 | -56.45367 | 2025-07-02 04:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3dd3f358-b224-319d-be78-f812c34a2c08 | -10.88298 | -56.44676 | 2025-07-02 04:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0e7463b0-3e4d-3e49-a8ff-ccd341af2938 | -10.94278 | -54.36949 | 2025-07-02 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1b717b1-e6e4-3b66-a757-07d957c76169 | -11.32653 | -55.21127 | 2025-07-02 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| edbb1919-cab5-3a5b-a4a1-1313cbded5c2 | -10.88519 | -56.45549 | 2025-07-02 04:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| da03aff3-0b0b-3801-8ec7-125031a79d80 | -10.87629 | -53.7484 | 2025-07-02 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b707d9a1-a8d5-3fc5-a074-defa012404e2 | -9.04011 | -63.98912 | 2025-07-02 04:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README14.md)
