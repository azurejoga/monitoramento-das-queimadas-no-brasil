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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e0fe40d-f1c5-30dc-85bb-6f44ed512672 | -6.59153 | -42.28901 | 2024-10-28 03:42:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| fecab60e-df2b-39a8-8d2b-897a40a18c44 | -6.62079 | -42.78465 | 2024-10-28 03:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 697d91bf-cdf0-3280-bd17-2632d6d08938 | -6.59523 | -42.28157 | 2024-10-28 03:42:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7f6cad23-5f0a-39bb-8e03-8f33fe0fdea4 | -6.59235 | -42.2841 | 2024-10-28 03:42:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 46e904e9-22fe-3d6d-a1fd-abb5f6abe2b8 | -6.62271 | -42.79151 | 2024-10-28 03:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e84c0b7e-bc65-3710-9f7f-9c3753af5ca8 | -6.62177 | -42.79683 | 2024-10-28 03:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0c47a7a6-73f2-3d58-9adf-f5981a2f86b4 | -6.61882 | -42.78538 | 2024-10-28 03:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4f6b348f-c41d-322c-be1e-484ba3b63801 | -6.59437 | -42.28646 | 2024-10-28 03:42:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 660f7f48-c8e4-3430-861e-a08601916b82 | -6.6199 | -42.78992 | 2024-10-28 03:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ec444b7e-e7c3-3de8-9e3e-64a938c3f435 | -6.619 | -42.79527 | 2024-10-28 03:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1bd4df9b-997c-3cbb-86e8-66447d9ae467 | -6.58964 | -42.28604 | 2024-10-28 03:42:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b3b949f0-d882-34fe-8f38-c579ddbf1edb | -10.59638 | -44.28062 | 2024-10-28 03:42:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd454e29-abbe-3625-82c3-06c1530561ff | -10.59139 | -44.27974 | 2024-10-28 03:42:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ed841ec-6690-3187-a7aa-8070670afdbf | -10.59035 | -44.28535 | 2024-10-28 03:42:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c03458bd-7c0f-3175-a64b-effea7ba8fa9 | -10.58537 | -44.2844 | 2024-10-28 03:42:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0e7d3b9-b138-32ec-bc5a-afdffcba3832 | -10.57437 | -44.28811 | 2024-10-28 03:42:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68def604-cc89-344a-9e14-c8c8b78170a5 | -10.3795 | -44.17508 | 2024-10-28 03:42:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5c93c20-50cb-35d2-ba25-7d021186c72a | -11.9261 | -43.94171 | 2024-10-28 03:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7997397b-f7de-3516-ad51-a63f27c2407c | -11.92584 | -43.94332 | 2024-10-28 03:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da5698fb-18a3-37a9-a116-773601f87d2a | -5.9352 | -43.66521 | 2024-10-28 03:42:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0188863c-9b42-3164-8cb1-2379172490e9 | -5.93431 | -43.66423 | 2024-10-28 03:42:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a93ec044-15d2-383f-8ca2-e402c46db95b | -5.93061 | -43.66101 | 2024-10-28 03:42:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5ed06e8-71c9-3a3d-b27f-70e0f781f76f | -5.93577 | -43.66199 | 2024-10-28 03:42:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b6bbc38-cf46-3f38-a5e3-fe6f6896a296 | -6.13273 | -44.30417 | 2024-10-28 03:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13036e2b-9da3-3247-b9f7-ed3546fbd68e | -6.13098 | -44.30472 | 2024-10-28 03:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3137bd54-cc89-3899-a8f5-864daac8c291 | -6.12728 | -44.30362 | 2024-10-28 03:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 883239fe-24b5-33bb-aaef-273edf88bff2 | -5.81678 | -44.1299 | 2024-10-28 03:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc4ef0c5-dbfd-3e9d-92b0-4c54146646f7 | -5.8162 | -44.13327 | 2024-10-28 03:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1737e661-d016-3be2-962b-defdae51519c | -5.81561 | -44.13667 | 2024-10-28 03:42:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5100db8b-a58c-3df3-8905-d6ae3d3db0fc | -5.81083 | -44.13243 | 2024-10-28 03:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03c88feb-de52-3549-84e6-d49718befa31 | -5.81023 | -44.13588 | 2024-10-28 03:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a3dc14b-ec0a-33bb-a342-cecf0de3cbee | -9.18649 | -45.21317 | 2024-10-28 03:42:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9c053d7b-d875-314b-9c3d-536937894018 | -9.18582 | -45.21684 | 2024-10-28 03:42:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3638be7e-3ca2-3450-a51b-632516f9ce2d | -9.1811 | -45.21193 | 2024-10-28 03:42:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f4d89cdc-b4e8-3b50-9bc4-daf136be10e0 | -9.18044 | -45.21553 | 2024-10-28 03:42:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5e6e643d-2deb-354b-b40d-10b966c5f894 | -9.17979 | -45.21914 | 2024-10-28 03:42:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| eb8626a2-7490-3202-be3d-092d102eacbc | -9.17908 | -45.22302 | 2024-10-28 03:42:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b3ec85d6-d712-3205-b25d-e0e9b19946b8 | -8.76947 | -44.71697 | 2024-10-28 03:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36076d1a-1431-3d99-863c-c76aadb5d7aa | -8.76886 | -44.7203 | 2024-10-28 03:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0662cdad-0808-361e-8262-d00261c96752 | -8.76824 | -44.72363 | 2024-10-28 03:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e23039f6-4a69-3781-97b6-a72a49dcd50e | -8.76763 | -44.72695 | 2024-10-28 03:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba9c73f3-a963-3501-a6c5-d1c285d76d58 | -8.7619 | -44.70649 | 2024-10-28 03:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb0fd594-81f0-3a86-a3fe-ea3c9ea0473b | -8.76131 | -44.70983 | 2024-10-28 03:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5642fa2b-8ba4-355a-870d-dc0df4c051a8 | -8.76076 | -44.70496 | 2024-10-28 03:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72fa5a0c-ec3c-3dae-9fb3-61c5bcd959f6 | -8.76071 | -44.71317 | 2024-10-28 03:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e067f16e-580d-323b-bd95-9d8c4abd3112 | -8.76014 | -44.70828 | 2024-10-28 03:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 064bc6a8-fb48-3e2e-b50c-fafe50656796 | -8.76012 | -44.71652 | 2024-10-28 03:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10c65f0b-92bf-3557-ad5d-3a774999c0e3 | -8.75952 | -44.71986 | 2024-10-28 03:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3695322b-a249-3bd6-bc79-211217ec0915 | -8.75828 | -44.71829 | 2024-10-28 03:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9da69da1-f0ab-3db2-8caa-80e092e6fd5a | -8.75767 | -44.72162 | 2024-10-28 03:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa0d01fe-6ad4-33db-954f-fa5bf6f950f7 | -7.86913 | -45.40306 | 2024-10-28 03:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ebe62ae-b3dc-3c87-b0b7-6f2cdcb0e50d | -7.86846 | -45.40683 | 2024-10-28 03:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8dc25b61-20c6-3c2a-a7ea-9fdf03d832bb | -7.86554 | -45.40466 | 2024-10-28 03:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e673f84e-bd3d-3365-890e-e81f11ea01df | -9.44332 | -44.48306 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9291dcf7-46fa-3980-9057-5d5064a8feeb | -9.44209 | -44.48199 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d773e051-974f-3b9c-b310-40b5f13c89e5 | -9.44152 | -44.48517 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fa66f39-cace-398b-897a-942d4a17bef4 | -9.44096 | -44.48835 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e57feb2-b8d5-3119-82fd-d1ad9c34a132 | -9.44039 | -44.4915 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69753e74-e835-34da-ab14-b7a357ae9e89 | -9.43877 | -44.4789 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 692723cd-15f9-31f0-acaf-24b8dff30fff | -9.43864 | -44.47157 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27100b1f-3a6d-3d77-8a56-4cc518f0c6d4 | -9.43818 | -44.48205 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1953a49b-a3b7-38c1-98c8-16d214dcd8ac | -9.43808 | -44.4747 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acb47490-4ce9-3e41-a2b1-f2531de457bd | -9.43759 | -44.48519 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c7a6aa4-0d1c-3732-a42d-1aad6a5ff044 | -9.43751 | -44.47785 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1a596c1-a8ae-35a5-a6eb-e2774ce264e7 | -9.43701 | -44.48833 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c036e2b4-2bfd-35ff-9525-4edea3cc915e | -9.43695 | -44.48101 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61c0299e-4f15-376f-a53d-2f82b798f6be | -9.43642 | -44.49148 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bb2c586-8eb4-380a-ab2e-5036ed619df1 | -9.43638 | -44.48415 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a8af096-613e-3483-9272-56c66b710a43 | -9.43582 | -44.4873 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4ee08be-1b50-3b74-b8f4-e7e6f582e613 | -9.43525 | -44.49045 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2737672-e402-3d60-aa27-08b803d02f26 | -9.43477 | -44.47181 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28e9b8d7-6580-3c96-b710-afc5047b774c | -9.43419 | -44.47493 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b704844-b8c4-32a9-a32a-286d1ec86ded | -9.4336 | -44.47806 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db72d40f-19b9-307e-8421-882b72ad005a | -9.43346 | -44.47079 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8a723f8-1ebd-367c-ac02-4d649599c2bd | -9.43302 | -44.48118 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 598f261c-5c84-3007-b109-b25a40f38f2e | -9.4329 | -44.4739 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04d05120-0926-345d-a3ae-c261d78741ad | -9.43243 | -44.48431 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 833104ff-c662-3e79-8cdb-c9fcfd44c99e | -9.43234 | -44.47703 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0c26825-5556-3f95-8bc9-81d759b7a7be | -9.43178 | -44.48016 | 2024-10-28 03:42:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 042b1f3c-c386-3b4e-a2d7-3223b86454be | -10.90028 | -44.61166 | 2024-10-28 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63e3cf22-7f28-39b6-b128-207c375f0c5d | -10.8771 | -44.53911 | 2024-10-28 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1ef1208-a303-3ac0-b3b2-2192ebf1962a | -10.87654 | -44.54211 | 2024-10-28 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00d15e6a-ac78-33e9-88c1-7c28553ccfc4 | -10.87207 | -44.53812 | 2024-10-28 03:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 901aaf78-cc1c-3db7-9a1e-41b07c8c1d49 | -10.82174 | -44.95024 | 2024-10-28 03:42:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5fea499-8747-39ae-a266-ebb8d1f2211a | -10.81656 | -44.94925 | 2024-10-28 03:42:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53d5a4eb-3d8b-3c05-81e2-957ad0bfe23d | -10.64959 | -45.00695 | 2024-10-28 03:42:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d9a67432-ea0b-32a3-82d1-daa9f5327cb1 | -10.649 | -45.01009 | 2024-10-28 03:42:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d8cc8ee4-d64b-32f4-81ff-aed353710725 | -10.64499 | -45.00274 | 2024-10-28 03:42:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c40ade2e-2f03-3534-9f4e-744c1e136a04 | -10.64486 | -45.00386 | 2024-10-28 03:42:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbeb7f88-84d0-3ed2-97dc-7804b4e427cf | -10.64439 | -45.00588 | 2024-10-28 03:42:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a14e315d-c92f-33de-9bb7-9ff8b8cba079 | -10.64428 | -45.00703 | 2024-10-28 03:42:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aad652f3-0554-3b92-bc97-9018d5c0c3db | -10.63976 | -45.00179 | 2024-10-28 03:42:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3316e02c-9bfb-352f-b73a-c21649b7d35b | -10.63963 | -45.00289 | 2024-10-28 03:42:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03c21eb2-7cb2-3c5a-beff-a8fa7a1fc0c2 | -10.09532 | -45.38092 | 2024-10-28 03:42:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db19ed72-603d-33da-9394-ba57b7883bc3 | -11.6236 | -44.96481 | 2024-10-28 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1782e6ce-2848-38da-ad05-4f8771b07990 | -11.623 | -44.96794 | 2024-10-28 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e659658f-ad65-3f3b-8cf3-41e3dbc30eec | -11.62176 | -44.96606 | 2024-10-28 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7b06a08-2780-37ab-b17b-54a431dc9a3a | -11.62117 | -44.96923 | 2024-10-28 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26d7f240-0cea-3683-9008-146652069943 | -6.18299 | -45.44302 | 2024-10-28 03:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d21468c3-5fb9-3813-b46c-40afeab498d6 | -6.17645 | -45.44611 | 2024-10-28 03:42:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README28.md)
