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
| c6d59a9a-2896-3d59-83d1-561db6b4d3e1 | -20.90512 | -42.57767 | 2025-02-06 03:27:00 | NOAA-21 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 34e6316d-b717-3c81-a0cd-e5753b3d4bcb | -29.85806 | -50.97192 | 2025-02-06 03:29:00 | NOAA-21 | GRAVATAÍ | RIO GRANDE DO SUL | Brasil | 4309209 | 43 | 33 | nan | nan | nan | Pampa | 4.6 |
| 30760858-2ddc-39b6-b31b-0db30f0e866f | -4.32743 | -39.15734 | 2025-02-06 03:46:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 260506a3-b61e-3854-9fd0-7bcd9a68918b | -2.91078 | -40.43976 | 2025-02-06 03:46:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1efba725-ec44-3320-ad9f-fb9291b31fae | -12.41478 | -43.80376 | 2025-02-06 03:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9f3c98f-ada0-385a-82c6-f4553a5acb80 | -11.25269 | -41.90687 | 2025-02-06 03:49:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8ebdb18f-1bbf-3ed1-9fd6-9bb8f7d42bb4 | -13.90661 | -38.94904 | 2025-02-06 03:49:00 | NPP-375D | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 15855cbf-52a8-3345-928c-ed24e9447c25 | -12.10729 | -44.74685 | 2025-02-06 03:49:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65a1c6c4-3559-3e66-b82a-377fd54459de | -8.12185 | -43.13647 | 2025-02-06 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c5b79bc7-8acd-38ab-81c8-1b5aa03b96ce | -7.86449 | -43.12891 | 2025-02-06 03:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 89f2796b-ed51-30d5-b12a-9be547141266 | -6.2162 | -41.52073 | 2025-02-06 03:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 28bc905f-66ee-3809-811c-7c944753d892 | -11.49604 | -43.22224 | 2025-02-06 03:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7316f950-bb95-30a1-b44d-c15c50ba87ec | -13.90112 | -38.94849 | 2025-02-06 03:49:00 | NPP-375D | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a7e4590c-cc35-3485-b067-61ade4e2482c | -12.84842 | -43.82429 | 2025-02-06 03:49:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42f25f31-d9fd-3805-b78e-39d1c9137b3f | -11.58116 | -47.63395 | 2025-02-06 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10b9fb02-b006-30b5-a521-af15d52c6e39 | -10.65226 | -44.49706 | 2025-02-06 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1149c872-d001-322c-89f5-546daeda5a58 | -11.14864 | -42.15321 | 2025-02-06 03:49:00 | NPP-375D | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a3531409-0074-399d-a5f4-fb2f902c3fe8 | -10.77985 | -44.75754 | 2025-02-06 03:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bae9c847-4a16-358d-98f2-ed6991457d31 | -12.48748 | -43.78636 | 2025-02-06 03:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf2c6240-ae6e-3bbe-8f34-00b3400d5833 | -8.12115 | -43.14044 | 2025-02-06 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 85559242-9033-3128-a5b4-d81c3236ce22 | -12.74061 | -44.83469 | 2025-02-06 03:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3db6c4af-c530-348a-b3ca-7c0ae0a730e4 | -10.35974 | -44.84659 | 2025-02-06 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50bb1cd7-fd0b-3c70-bf61-53f18b314c10 | -10.65751 | -44.49344 | 2025-02-06 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 63bacd91-9a32-3df6-ba29-9b34c175ec00 | -11.5866 | -47.63482 | 2025-02-06 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48e13e39-8b69-352d-b0f7-4ecbaeb4fb57 | -6.21764 | -41.519 | 2025-02-06 03:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 803f2930-559d-3489-9c84-d6f5e7bed608 | -12.84908 | -43.82055 | 2025-02-06 03:49:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85b1a333-3f7b-348b-a22f-3d234c810e05 | -12.4916 | -43.78716 | 2025-02-06 03:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6ebca07c-4aa5-3e74-aa62-1599db0f262c | -11.05349 | -46.1225 | 2025-02-06 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b47c804c-691c-3b96-900f-5944dade7c60 | -12.4566 | -43.56505 | 2025-02-06 03:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cb73078-b52f-38b2-a71a-05d410530d1c | -12.84431 | -43.82354 | 2025-02-06 03:49:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62235b15-7c01-3ab1-95fe-166b93c2c54a | -10.35515 | -44.8457 | 2025-02-06 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9828fe6-6b9a-3fcd-959a-5f0121cd9cc1 | -12.8532 | -43.8213 | 2025-02-06 03:49:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a258bf0b-e1d4-379c-a593-646fe2e6a1bc | -10.7807 | -44.75286 | 2025-02-06 03:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 280589d0-c2fe-333f-9179-4cf0ec08e274 | -8.353 | -45.1783 | 2025-02-06 03:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44ef2d3c-eccd-3d4f-94df-21f2566ff106 | -10.65672 | -44.49789 | 2025-02-06 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4dcda9a6-8834-3536-b7e5-16d4dcbc8989 | -10.9513 | -40.73656 | 2025-02-06 03:49:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 090fa62f-dce3-3220-ae9b-865ddad6e3f4 | -12.46067 | -43.5658 | 2025-02-06 03:49:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 081e6f36-db16-37e5-b6c9-009eceec75fd | -13.90328 | -38.94848 | 2025-02-06 03:49:00 | NPP-375D | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 47e22229-3748-35f0-9e2b-b24a82db5995 | -19.43807 | -44.34055 | 2025-02-06 03:51:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b976e4d-ec61-355e-81df-e226f2b955ac | -16.68227 | -43.88369 | 2025-02-06 03:51:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e472cc50-9a13-3106-a520-b9398b9cf212 | -13.99829 | -44.03253 | 2025-02-06 03:51:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad36dd88-a0c6-39e9-93a7-32261a86a0bd | -16.8667 | -40.81815 | 2025-02-06 03:51:00 | NPP-375D | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c4af6714-83ac-3876-b1cb-a9b3477addf3 | -20.18354 | -46.60464 | 2025-02-06 03:51:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46d4c9e5-8d9f-3ef6-a6e6-fd33dec26801 | -13.9942 | -44.03176 | 2025-02-06 03:51:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb62b19d-e61f-3a6c-85b0-8ac63b83e5da | -16.03628 | -42.13731 | 2025-02-06 03:51:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7c025ba0-30d0-33ac-8797-9e5574f94264 | -19.04888 | -42.53492 | 2025-02-06 03:51:00 | NPP-375D | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0fcb3ad3-7688-3840-b62a-39315468d67a | -18.60877 | -44.25624 | 2025-02-06 03:51:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 38f6df32-c77b-3406-af05-a6f40ae7184d | -13.61392 | -42.24216 | 2025-02-06 03:51:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 39cb4191-1c13-3f00-954f-2f20b134ca01 | -16.86332 | -40.81747 | 2025-02-06 03:51:00 | NPP-375D | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 16602d98-5932-3f9a-b067-8c6f5180d56b | -17.09482 | -43.80636 | 2025-02-06 03:51:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc969612-7e09-3432-ab19-6f9fa9d7e15e | -17.62584 | -39.28355 | 2025-02-06 03:51:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 24726577-b1e5-33a6-aa34-55fe21fe3762 | -14.1349 | -41.69201 | 2025-02-06 03:51:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fa538a13-05ec-3e8a-8ce9-4ea61772a9fb | -19.49026 | -43.52935 | 2025-02-06 03:51:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bde6474-3ef2-34a8-8db3-ddc14e2598e0 | -17.64153 | -39.30816 | 2025-02-06 03:51:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 47159cc1-d3b8-399c-9ac2-2ebefbf08fab | -17.98426 | -39.85815 | 2025-02-06 03:51:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ecfa1c64-2c9a-32f0-a6e2-7b3692275235 | -16.86839 | -40.61555 | 2025-02-06 03:51:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8de2b55c-73e1-38c1-9979-bd4d0f9f1971 | -19.96835 | -44.2173 | 2025-02-06 03:51:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 795a7f7f-3aaf-35ac-bab5-8838520324a2 | -16.87176 | -40.61617 | 2025-02-06 03:51:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c4f617ca-f4f5-34c9-bd7e-50f18516484f | -16.85532 | -40.82368 | 2025-02-06 03:51:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c99c0ae2-4d45-3c34-a6e1-a636b9781baf | -15.59764 | -41.21241 | 2025-02-06 03:51:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2079c0ab-7d73-30c6-95bc-a4d18146c8fa | -20.18443 | -46.60011 | 2025-02-06 03:51:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b811ec7-8896-3851-bca2-e22d2113b78a | -17.09379 | -43.80407 | 2025-02-06 03:51:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec55ed02-8215-37b9-b268-0d22886c11e5 | -20.18265 | -46.60918 | 2025-02-06 03:51:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 195f9866-e0d7-33e6-b5fe-57cf3b62633f | -21.31481 | -41.01788 | 2025-02-06 03:51:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a028e78d-a16f-3974-874c-3a22372a2d73 | -16.85871 | -40.82427 | 2025-02-06 03:51:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2f15bdc8-13ed-3bc7-80d2-e5599238a792 | -19.47752 | -40.08385 | 2025-02-06 03:51:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0b062472-71ed-34c8-a416-7058dd66377e | -20.90414 | -42.57873 | 2025-02-06 03:51:00 | NPP-375D | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a230aff2-5c47-3d30-90a9-f0bd31071fa3 | -16.8547 | -40.82741 | 2025-02-06 03:51:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1826a389-d22c-3b7e-956e-409a31580dcb | -15.64492 | -39.1898 | 2025-02-06 03:51:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 569c50d2-e7d5-3d0f-8009-93f000cca7cb | -20.30906 | -40.7511 | 2025-02-06 03:51:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 153f176e-175e-3900-be36-9d4023f08f97 | -22.67545 | -42.85373 | 2025-02-06 03:53:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 905ad429-68a7-3ff0-b8f9-935add8aab44 | -22.84171 | -43.48787 | 2025-02-06 03:53:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a0e44532-4c1c-3448-80dd-38466f98a12b | -22.67477 | -42.85777 | 2025-02-06 03:53:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 849d946e-bf2c-33dd-9dfd-64c66d3128d2 | -29.63258 | -56.64754 | 2025-02-06 03:55:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 6.5 |
| f86dce9a-f98c-375c-a030-a8e790b1d889 | -29.64203 | -56.6381 | 2025-02-06 03:55:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 4.1 |
| 066c182d-9860-3f77-81b9-94760521c6b7 | -29.6355 | -56.63623 | 2025-02-06 03:55:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 4.7 |
| 18324f5a-bc18-3398-8954-63aea88cac0a | -29.62313 | -56.65697 | 2025-02-06 03:55:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 06cc39c4-5e7a-3e78-bbfc-b13098ab9e11 | -29.64826 | -56.64037 | 2025-02-06 03:55:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 14dfedea-e6ce-36c9-ad4b-5cf16c24451f | -29.91442 | -54.35843 | 2025-02-06 03:55:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| f0b6a8c2-d73c-3c28-959a-0552830d3536 | -29.61527 | -56.66056 | 2025-02-06 03:55:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 776ec28b-d055-3d22-bc10-76301f4a81d3 | -29.91232 | -54.35758 | 2025-02-06 03:55:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| ff2fecd2-a741-338a-b06d-8f23b4cfbbd6 | -29.91332 | -54.36277 | 2025-02-06 03:55:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| b8a1d571-2696-3789-a3c5-bbc3ca9c590a | -29.61674 | -56.65508 | 2025-02-06 03:55:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| f6f128c4-ba08-334e-a9a9-ba2d55c2062f | -29.63099 | -56.65333 | 2025-02-06 03:55:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 9c5cdbd4-842d-3d14-903b-c1ac3f61f286 | -29.62297 | -56.65738 | 2025-02-06 03:55:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 7a6a378f-fc10-3f90-85a9-72603683eb87 | -29.61514 | -56.66098 | 2025-02-06 03:55:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 321102f1-b1ed-3963-b9a5-a218256199a9 | -29.62632 | -56.64537 | 2025-02-06 03:55:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| b5cd9f32-65fe-30b6-b33b-c0ca6b0318f7 | -29.63579 | -56.63589 | 2025-02-06 03:55:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 4.1 |
| f847eb85-6151-3307-ab0d-9aef071d73e3 | -29.91124 | -54.36192 | 2025-02-06 03:55:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 3.1 |
| 3124d23b-d707-3f68-973c-da25f31ebaec | -29.61848 | -56.64891 | 2025-02-06 03:55:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 0da5aaef-e08c-3f3e-9ef5-64475a24a639 | -29.61689 | -56.65469 | 2025-02-06 03:55:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| d6f75464-1123-3edf-a242-1a65abc71d23 | -29.64174 | -56.63846 | 2025-02-06 03:55:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 4.7 |
| 2445bef1-9bbd-3e47-8010-a519f44cb9b9 | -29.64797 | -56.64075 | 2025-02-06 03:55:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 1062ecf1-978f-39ae-9a4c-266e4c116179 | -2.12825 | -47.13696 | 2025-02-06 04:10:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96e22a5e-54fe-35b4-a736-5a25294d26a8 | -2.12425 | -47.13628 | 2025-02-06 04:10:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06763948-7d80-3362-9529-0e7b1f316a9a | -3.12123 | -40.9929 | 2025-02-06 04:10:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2b64d9e0-dd34-34b8-be16-97c7131ec7c3 | -2.90991 | -40.43679 | 2025-02-06 04:10:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 916a3c00-733a-3973-8cb4-830b29d5efbe | -6.23535 | -44.83265 | 2025-02-06 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c639e741-018f-330e-9d57-f3b2b333c856 | -7.04446 | -44.40417 | 2025-02-06 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc49277d-fbb9-3b80-ab85-5e5d770c49ed | -8.35133 | -45.17628 | 2025-02-06 04:12:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README3.md)
