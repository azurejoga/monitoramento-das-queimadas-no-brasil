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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 667e62cb-eee4-3765-b5d7-884de8bb0ce0 | -9.26927 | -43.3278 | 2024-10-25 15:33:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9eec81bd-7616-38a3-bae2-6fae1f17ec53 | -9.21243 | -43.06533 | 2024-10-25 15:33:00 | NPP-375 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a592cacb-08e3-3ee8-b5d8-1128ab663aa5 | -9.21154 | -43.06573 | 2024-10-25 15:33:00 | NPP-375 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ab48df98-c17a-3cfe-ab7b-8c834d319aaf | -9.1998 | -43.34583 | 2024-10-25 15:33:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4e5142f4-9348-3995-bbed-6be889218af7 | -9.19912 | -43.34022 | 2024-10-25 15:33:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 971ec17a-2a1a-393c-a4eb-aaaaf18d0d8c | -8.33187 | -42.81558 | 2024-10-25 15:33:00 | NPP-375 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| cc661ae0-5813-3d53-86ad-9815c99d41b3 | -8.33119 | -42.81031 | 2024-10-25 15:33:00 | NPP-375 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9767e193-9b73-37bc-8f5a-0f2d1e4ae912 | -8.31095 | -42.60267 | 2024-10-25 15:33:00 | NPP-375 | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 32ea522c-a0ac-385d-a681-cdf5a975690b | -8.08428 | -42.39432 | 2024-10-25 15:33:00 | NPP-375 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 1d3e5227-46b8-3bc7-ae64-6f4c3c2a3fbb | -8.07868 | -42.40006 | 2024-10-25 15:33:00 | NPP-375 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 629c0fef-8826-3253-9a42-7365e8db094e | -9.63685 | -43.90808 | 2024-10-25 15:33:00 | NPP-375 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| b5612378-7d87-3427-baa2-2d61fad3300a | -9.63143 | -43.91079 | 2024-10-25 15:33:00 | NPP-375 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 53e40be2-4359-3fd5-b123-cd008bb0c9b1 | -9.6299 | -43.9087 | 2024-10-25 15:33:00 | NPP-375 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 7b355ac7-8aa4-31e6-9f97-ac10ca5ceac2 | -10.68371 | -44.21201 | 2024-10-25 15:33:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1cb1e9f7-d83e-3cce-b153-6e73bf4da47e | -10.68299 | -44.20572 | 2024-10-25 15:33:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 30447d66-423f-3504-970d-ede8111cb4b9 | -5.06994 | -43.67086 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b240b89b-e8b4-30e5-9d4d-bb27ae82bbe9 | -5.06924 | -43.66562 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| d4d32036-0579-32ea-abb1-c138d3b2f1a3 | -5.06874 | -43.6684 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| f444edaa-8b37-3dd0-a719-56e778bffc7e | -5.068 | -43.66315 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1c86fed6-b3f2-35a1-acdf-22852f6a6b2c | -4.93219 | -43.67889 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1f6417c5-c35e-31d1-a980-5f0f0573e406 | -4.80229 | -43.78938 | 2024-10-25 15:33:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 31ffaed5-5535-3725-9042-e96f362ea472 | -4.80212 | -43.79155 | 2024-10-25 15:33:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6386c920-d68e-382d-95c3-336489ee7fc8 | -6.3316 | -43.79153 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5f812ed6-601d-3058-a3d4-9e7a9089527c | -6.04826 | -43.90424 | 2024-10-25 15:33:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 99b2141b-2912-37c0-83bf-531b9f7475e6 | -6.04751 | -43.89845 | 2024-10-25 15:33:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8e248001-acfa-3e62-bec5-238fd67c4ced | -6.04469 | -43.90468 | 2024-10-25 15:33:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 15a6ce9c-0fa2-3488-884d-934e66b389be | -5.74605 | -43.88883 | 2024-10-25 15:33:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b43064f3-0eb8-3f90-98e5-c3411bd4f6e3 | -5.74491 | -43.89245 | 2024-10-25 15:33:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| eeac0a88-92e3-31e5-9437-a0c878c8b0fb | -5.74417 | -43.88679 | 2024-10-25 15:33:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| c8abfb6b-5575-3d24-b82a-90a8b4fe20ad | -5.73946 | -43.88973 | 2024-10-25 15:33:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| c4143b7b-8e30-3cf3-bfa8-f47c3b503938 | -5.72873 | -43.81163 | 2024-10-25 15:33:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9a7e0c45-029a-3eac-bf13-2d77d8f6e35b | -5.72809 | -43.81493 | 2024-10-25 15:33:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 210d08d0-9b20-3b4e-bd9d-8dbbbb34176c | -5.70065 | -43.90075 | 2024-10-25 15:33:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 21daa99e-5b5b-3f57-aa96-256a5ecde493 | -6.2204 | -44.91692 | 2024-10-25 15:33:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4bd4b5de-d4d3-3121-b736-41eef9b9e88a | -5.88834 | -44.15411 | 2024-10-25 15:33:00 | NPP-375 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ad5fcd7e-4a37-3a0f-b7ee-2aa5fc04c09e | -5.88417 | -44.15782 | 2024-10-25 15:33:00 | NPP-375 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| db0900e6-8700-3457-b9e7-d855fbbf9d6d | -5.45053 | -43.3566 | 2024-10-25 15:33:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5e7ade87-d9e0-314a-9f31-9cc02cf135f9 | -5.11444 | -43.85286 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 67528d94-95e7-3cd0-891e-72fc34bba66e | -5.11369 | -43.85036 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| b526961a-f471-30c6-bac7-9ece24b4f8f9 | -5.11369 | -43.84747 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 5fcab282-7eea-3ceb-8a7f-d7d55900fe19 | -5.11297 | -43.84498 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| a344523f-dc56-3b05-a110-5b0f63e31588 | -5.10784 | -43.85639 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e80c5608-f655-3305-9716-a59e4a7e4e63 | -5.10784 | -43.85318 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 424074c7-b832-3216-bf21-634d76a60707 | -5.10708 | -43.85066 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 1addd94a-b12b-3550-8451-356eaeac1674 | -7.64971 | -44.7072 | 2024-10-25 15:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| dc11e119-27c8-3416-b5da-f9533aab90d6 | -7.61471 | -44.0582 | 2024-10-25 15:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 35b7eae6-2d14-32ed-b70e-6f475ce92810 | -7.54285 | -44.03733 | 2024-10-25 15:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7aa8853c-4245-31e7-95a5-f459a825a939 | -7.54203 | -44.03678 | 2024-10-25 15:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ec6c9680-42b5-36a5-80d5-d88be51f0787 | -7.43264 | -44.73354 | 2024-10-25 15:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3b2e3680-c0dc-3b09-8bb2-639a9ceacb6b | -7.42941 | -44.73554 | 2024-10-25 15:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ad6be58b-3b62-33a6-af3c-db67140c5fd3 | -7.42855 | -44.72889 | 2024-10-25 15:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 38c555ba-0065-3087-a753-871e1e3ed59c | -7.40743 | -44.7325 | 2024-10-25 15:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8f41356c-b253-3f9c-8522-966076db4442 | -7.40043 | -44.73397 | 2024-10-25 15:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f4e70c9a-2e35-370a-9311-8339ca8afd64 | -7.23265 | -44.301 | 2024-10-25 15:33:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d5b30ca6-213a-36b0-a67f-0b35b4b27aa8 | -7.10311 | -44.10712 | 2024-10-25 15:33:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6a796de7-794a-3967-9b0e-79ca2c416c00 | -7.36425 | -44.7675 | 2024-10-25 15:33:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| bfa5069e-5483-3ffd-9819-07cbe5f513b2 | -7.3634 | -44.76104 | 2024-10-25 15:33:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 157b4ee0-c2d0-36ff-9d6f-9c847f293187 | -7.36131 | -44.76636 | 2024-10-25 15:33:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 26056ec8-2f05-3419-bb25-11649b8f0ea9 | -7.36052 | -44.75999 | 2024-10-25 15:33:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 795e105d-507f-3699-be9c-3769c6aef981 | -7.304 | -44.97503 | 2024-10-25 15:33:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 37583dd1-77ea-3743-b899-5bfb7fedca2b | -7.30315 | -44.96832 | 2024-10-25 15:33:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9e2bf436-57fc-30e0-8468-0a1aa6a1f352 | -7.29594 | -44.96887 | 2024-10-25 15:33:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9406137b-98ef-3a71-b0e9-7bcec27da1e2 | -7.29392 | -44.97093 | 2024-10-25 15:33:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 80125c6f-1b0a-3604-9e84-979e16066f11 | -7.29306 | -44.96443 | 2024-10-25 15:33:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| deabc82c-fb05-3574-bfef-bff38fd04246 | -7.14988 | -45.23691 | 2024-10-25 15:33:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0ebb4c7c-94c2-3c80-8204-143959ea8bb1 | -6.93483 | -45.0781 | 2024-10-25 15:33:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| ea0b68f0-d3c4-3094-b84a-7ac2188b0dbb | -6.93039 | -45.07702 | 2024-10-25 15:33:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 2cfecc9f-40a1-3c47-9d65-f5e931d209f6 | -6.92755 | -45.07819 | 2024-10-25 15:33:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 1a6033e3-d8ef-367e-8d0f-b879311f86c9 | -6.43767 | -44.86517 | 2024-10-25 15:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 26c0adf0-2fc1-3bc1-a8ee-171df342a66b | -6.43411 | -44.86794 | 2024-10-25 15:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 1d5c28da-3381-3247-bd10-f1bbb90e46b0 | -6.4332 | -44.86116 | 2024-10-25 15:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 011f1bbc-383c-3870-b571-1fcc5b78f9d2 | -8.79509 | -44.72198 | 2024-10-25 15:33:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 90bc4414-9663-31f8-9ac5-821308c59258 | -8.66643 | -45.06517 | 2024-10-25 15:33:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 2a690c98-3cca-314a-a941-cf78ea04e89a | -8.66556 | -45.05787 | 2024-10-25 15:33:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| bb936201-1bca-3fd0-b7b8-00718d4b38eb | -8.66524 | -45.06265 | 2024-10-25 15:33:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 40.5 |
| fb2ef126-c5ec-361a-ad0f-e89bb84104aa | -8.66434 | -45.05542 | 2024-10-25 15:33:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 8385ca44-43cf-3ed1-be41-04051a246200 | -8.66343 | -45.04816 | 2024-10-25 15:33:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| ae2c35e1-ec80-371a-8f16-097fb8b542c2 | -8.65908 | -45.06586 | 2024-10-25 15:33:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 92316db2-7822-3da4-a044-b73ca8840f2f | -8.65822 | -45.05856 | 2024-10-25 15:33:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 5abd6e1a-3e21-32c8-af30-e4ab646b1de1 | -8.6579 | -45.0633 | 2024-10-25 15:33:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 4a810eba-c0ee-30ef-83b4-b2de7e69c0ba | -8.65736 | -45.0513 | 2024-10-25 15:33:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 4f92fd61-e43b-34a4-92dd-f7c0daca6900 | -8.65699 | -45.05603 | 2024-10-25 15:33:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 07baa8e0-da8c-3ffb-8122-37fa482cce40 | -8.65651 | -45.04414 | 2024-10-25 15:33:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 32.0 |
| ec14c1ab-76bc-3a67-93fb-eb55411d09ae | -8.65609 | -45.04882 | 2024-10-25 15:33:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 9779ccc4-ae70-30db-839e-87bed9a3f0cb | -8.52168 | -44.74826 | 2024-10-25 15:33:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 09e64f30-15fa-3c80-9b3c-a63fc9d01221 | -4.98677 | -45.10782 | 2024-10-25 15:33:00 | NPP-375 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8fe225c0-f6fe-3e89-9b4c-873316a03efe | -4.98279 | -45.1107 | 2024-10-25 15:33:00 | NPP-375 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7bee2c25-3303-3fbd-996e-5be3b4a8cfe0 | -4.9797 | -45.10845 | 2024-10-25 15:33:00 | NPP-375 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a59aee48-3aaa-3b2f-9226-c92d197875c1 | -6.50452 | -45.27065 | 2024-10-25 15:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1c3e9546-a865-3676-b90e-0892ddd8103b | -5.98019 | -45.3714 | 2024-10-25 15:33:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 78b45b3f-e85a-36e0-9805-db6ff363a5cb | -5.97791 | -45.37274 | 2024-10-25 15:33:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 091734b7-f21a-3564-aa6c-9d7462c0bbf0 | -5.71153 | -45.01441 | 2024-10-25 15:33:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 2ea0ebbb-8213-3173-8532-3f895fe4015d | -5.70917 | -45.01305 | 2024-10-25 15:33:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 50d6bb16-3030-33a4-9469-a52ebe80a114 | -5.70832 | -45.00656 | 2024-10-25 15:33:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 64d97c5e-d0b6-3a11-8b43-f644b75575e9 | -5.70442 | -45.01486 | 2024-10-25 15:33:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 86656a55-089b-344d-87e7-3ab9ac499c52 | -5.70352 | -45.00835 | 2024-10-25 15:33:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| f08bcdfa-d2ff-3c82-ba41-96ac26dcd304 | -7.10072 | -45.31641 | 2024-10-25 15:33:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6c57054b-cd2d-3616-acf3-ccb7e69051a7 | -6.79561 | -45.2775 | 2024-10-25 15:33:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 816618c7-0ea5-3718-924b-cd709cc2adc3 | -6.78834 | -45.27825 | 2024-10-25 15:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9bd1508e-e5b5-3b2f-8b70-66757ea1a85d | -5.96088 | -35.16204 | 2024-10-25 15:33:00 | NPP-375 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |


[Clique aqui para ver as próximas entradas](README122.md)
