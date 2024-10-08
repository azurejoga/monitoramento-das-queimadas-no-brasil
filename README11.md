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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de0529f1-0068-3896-a84c-a81c7fc69210 | -6.4838 | -43.88546 | 2024-10-08 00:35:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6206512b-45ff-3d27-8847-3ff32645ebca | -6.48254 | -43.87633 | 2024-10-08 00:35:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7f166f38-5d42-3e09-b69a-a9865a5df727 | -6.43385 | -38.84009 | 2024-10-08 00:35:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 37.3 |
| cc0c49a1-8324-3844-964f-467dde7069c8 | -6.43198 | -38.82723 | 2024-10-08 00:35:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 47.5 |
| e1b5d94b-0ea7-37c8-bd09-31fd287b6177 | -6.42325 | -38.84137 | 2024-10-08 00:35:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 4d0f7bb3-498c-3b10-98c9-75ea0cb2ba8d | -6.42137 | -38.82856 | 2024-10-08 00:35:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 35.7 |
| 1dc4e49b-50ee-3e5c-b02d-ca6e77fad492 | -6.31214 | -43.37504 | 2024-10-08 00:35:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| bbc9e753-e766-3888-b7f2-2edfcd2f73e8 | -6.29369 | -41.85966 | 2024-10-08 00:35:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 258aae2d-6347-3030-9fcc-877b600e56c5 | -6.29241 | -41.85061 | 2024-10-08 00:35:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| be94558f-cbbf-3c99-8815-7c14c1490cc6 | -6.25811 | -42.51999 | 2024-10-08 00:35:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 20e6d72a-502c-3c4b-91ed-699303b5c6e6 | -6.07862 | -42.76217 | 2024-10-08 00:35:00 | TERRA_M-M | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 7f52365e-fb20-3eaf-9d48-a71a96364214 | -6.07738 | -42.75333 | 2024-10-08 00:35:00 | TERRA_M-M | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 91874179-a6f1-3d8d-a600-716b4e9daf7b | -5.96718 | -43.28555 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 914eb77d-e5ab-3eba-8c37-be4650bdd518 | -5.88848 | -41.98898 | 2024-10-08 00:35:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a7488c27-a7c4-3456-b65f-411b4e3033e5 | -5.84322 | -42.65482 | 2024-10-08 00:35:00 | TERRA_M-M | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f2d4dd2a-e358-3f8e-bdd6-fd639c6ea44c | -5.77133 | -43.99735 | 2024-10-08 00:35:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0a751e7f-8eed-32d6-829e-151bf1210103 | -5.39128 | -43.57535 | 2024-10-08 00:35:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e30c08a9-7d7c-3d3f-b1d0-b023727a3c2e | -5.13804 | -42.88528 | 2024-10-08 00:35:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9260ccb4-5238-30a6-bddb-4e09592e655c | -5.13681 | -42.87646 | 2024-10-08 00:35:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9b933676-389f-311a-8ba2-531608d1a7e9 | -4.45099 | -42.90903 | 2024-10-08 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| bfeaf9f0-8b48-3702-abd7-1fccc107d4eb | -4.44975 | -42.90019 | 2024-10-08 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 150.3 |
| bbc0cf7e-95c7-363c-a8d7-7e04cb15d650 | -4.41942 | -43.94287 | 2024-10-08 00:35:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 90a58d22-6471-3eaf-9d40-b89ae4febeee | -4.39077 | -43.5405 | 2024-10-08 00:35:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0a2fe524-28fe-3bbe-ad37-a3e8337b6e9e | -4.2472 | -41.92428 | 2024-10-08 00:35:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| def3090c-0404-38fc-a0b1-951c2796b6a2 | -4.13385 | -43.81103 | 2024-10-08 00:35:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5e8bdf39-ed1f-324b-885c-52d80718f222 | -4.13263 | -43.80218 | 2024-10-08 00:35:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 942c4e93-6e94-3503-9076-c5085274efd2 | -4.04542 | -43.23964 | 2024-10-08 00:35:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4591a475-468d-37a9-8f67-d8a4d98e6848 | -4.02522 | -43.2398 | 2024-10-08 00:35:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7040c06f-d6b5-367c-b7a1-e45de776f3e6 | -4.01639 | -43.24105 | 2024-10-08 00:35:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cf963110-ae2d-34f4-a0ad-a7e64ad1173b | -3.94696 | -41.49317 | 2024-10-08 00:35:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d210e005-83e1-3bde-af3b-4e2392028b61 | -3.61808 | -42.75688 | 2024-10-08 00:35:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 9e09ee27-6f2b-367c-97fb-6c2841d9b2c5 | -9.57297 | -45.64283 | 2024-10-08 00:35:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| df458bd7-f796-323e-82de-1a5e5c2485af | -10.52039 | -49.1195 | 2024-10-08 00:35:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 2f1398f6-f610-331e-b31d-9be1226e382b | -11.21248 | -51.36803 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 3980b384-c34e-302c-b5c9-68e4c2d9c97b | -11.25373 | -51.29268 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 78e05736-17b1-3905-beea-81e3d72a2813 | -11.25762 | -51.32751 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| a0531514-214f-37ef-aca8-162b02507388 | -11.31607 | -51.03876 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 4a4a14b6-ec12-3fd2-a305-782babf8241a | -11.3198 | -51.07203 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| e46d81a4-6476-37e6-930d-5698b00caa9c | -13.3791 | -43.76908 | 2024-10-08 00:35:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 374cc1f2-b26c-3d35-ba36-db87a3a64218 | -13.36962 | -43.7704 | 2024-10-08 00:35:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 03b6e662-eecb-3b79-8fb3-5cdf523d4516 | -13.08879 | -46.34088 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9c7329f6-a287-3aac-884d-d89a7aaa8930 | -12.99432 | -46.22071 | 2024-10-08 00:35:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d04a3883-246c-3574-b4ff-17329f3d6ff8 | -12.89884 | -42.78991 | 2024-10-08 00:35:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 1590015a-650d-31ab-bd60-dfdf249ee9ac | -12.86868 | -44.6214 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| e92f8128-01c5-3110-8d4b-a653c55cf451 | -12.8685 | -44.62782 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c3f7ba39-5fda-3aff-b752-cef0013873f0 | -12.86698 | -44.61629 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e83a996d-6823-3ceb-ad75-63ddab6fee9c | -12.58129 | -43.37103 | 2024-10-08 00:35:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| bc287eaa-db25-3f37-aab2-da1954f1242f | -12.57998 | -43.36118 | 2024-10-08 00:35:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bbbca4cb-4b47-3d49-b4b1-2fad8420f876 | -11.91353 | -45.70606 | 2024-10-08 00:35:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 007021a4-989f-3c04-bf85-d7b58594f53f | -11.91192 | -45.69301 | 2024-10-08 00:35:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6e858648-3d8b-3c27-80a1-9b4f23729827 | -11.81479 | -42.80297 | 2024-10-08 00:35:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 40e14e21-e935-3673-951a-ccd9fce5a3eb | -11.77489 | -44.52397 | 2024-10-08 00:35:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 29b89bb8-9ea8-311b-ad66-78687b4d9692 | -11.75126 | -44.49378 | 2024-10-08 00:35:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4b8a44f8-12d7-35ed-9d12-28f4a0ac445e | -10.5596 | -43.80717 | 2024-10-08 00:35:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 56a6b9c2-a9f1-32e3-961a-81716e1e4a14 | -10.47295 | -45.11047 | 2024-10-08 00:35:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| baf75687-80be-3a0e-986a-cfcfd04fd113 | -10.1208 | -45.22766 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8d3ec220-a4b3-3ef3-a18a-e76304429c3d | -10.08061 | -36.20827 | 2024-10-08 00:35:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 8533a543-2fe5-3b86-a035-a457a5e46301 | -10.07719 | -45.28637 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d00dc667-8c41-3825-8d40-aebbae9049a4 | -10.07694 | -36.21468 | 2024-10-08 00:35:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 47cce809-b731-3f7e-b454-a0487b4c14cc | -10.07566 | -45.27472 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 1f95bc4c-8ba3-308b-899d-a7b5af0437c4 | -10.06725 | -45.288 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 0f23af39-dd04-3863-9e5f-9be5bc1137a1 | -10.06569 | -45.2761 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 1bf618b9-f582-3c3d-8157-9a9c089f850b | -10.04445 | -36.40027 | 2024-10-08 00:35:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 56.8 |
| 690327b5-8488-3600-93e9-21e0f457fb6e | -10.03736 | -45.29237 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| bb11eba6-43df-319a-8fe0-ce0787fce076 | -8.53674 | -46.59208 | 2024-10-08 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1e282533-384c-34cc-a251-588b6596633e | -8.53148 | -46.60007 | 2024-10-08 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| e7c31b24-eb25-3ff1-bcc5-d1850494ec0c | -8.5298 | -46.58672 | 2024-10-08 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 30335ae7-88e4-3719-8261-fe79d2254881 | -8.52602 | -46.59347 | 2024-10-08 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b8f9f766-01bd-3947-b317-5385554444af | -7.28756 | -44.97978 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ec86bf2a-5caf-3242-bbe5-3231f3e44dee | -7.27673 | -44.97085 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4548c0b1-4273-3a75-9102-ebeadb1a4eec | -7.26731 | -44.97228 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0c67d06a-ff2f-346c-a75a-f13b2b84d818 | -7.26591 | -44.96195 | 2024-10-08 00:35:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3baf7b85-79e6-305b-b322-d4516afbf742 | -7.09474 | -44.58664 | 2024-10-08 00:35:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fb0924c4-0a9d-382e-a761-23d95765a29b | -7.08551 | -44.588 | 2024-10-08 00:35:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 748beb85-168f-39b3-a4e3-d3ee7c57b8ab | -7.0842 | -44.57824 | 2024-10-08 00:35:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9d0b3d4c-761e-305d-8756-0a51dfb62d7a | -6.93583 | -45.24131 | 2024-10-08 00:35:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d9d3fbd3-41d3-3d63-858b-42f5a2db98ea | -6.89629 | -46.08852 | 2024-10-08 00:35:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| a4ad077a-07f4-3a34-8f10-b620d0fd720c | -6.89473 | -46.07703 | 2024-10-08 00:35:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c3bd6a49-6233-39ed-a2fc-444a55c8d190 | -7.30821 | -42.25029 | 2024-10-08 00:35:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 7f3a2d79-107e-3008-bf3c-6836463473c9 | -6.68013 | -44.64477 | 2024-10-08 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3537287a-b9ba-3a7a-a1a8-65125050d925 | -6.67114 | -47.11419 | 2024-10-08 00:35:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d9b46485-dd74-365b-ba20-07f051d837f8 | -6.6685 | -47.12025 | 2024-10-08 00:35:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a29e9e30-9bc4-3ffc-ac1d-2e33c47004db | -6.66666 | -47.10661 | 2024-10-08 00:35:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 510cb89b-2ea8-3740-ac72-a2ca5fe9cb9a | -6.58015 | -44.1842 | 2024-10-08 00:35:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 2640c9db-6296-3c5a-91f3-18d9e192121b | -6.57888 | -44.17484 | 2024-10-08 00:35:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 5d2fe12a-0775-307e-a23d-d7c72c233d90 | -6.39779 | -46.25893 | 2024-10-08 00:35:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| aac1e8d2-c0d4-3e78-afb3-990094f6797f | -6.36771 | -45.73118 | 2024-10-08 00:35:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cb7bd8ce-4c23-3e7b-ab3d-e4cf5363b815 | -6.33704 | -45.72486 | 2024-10-08 00:35:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 93e3784a-2c10-3fc5-ac6b-35af2738dc04 | -6.05772 | -46.60545 | 2024-10-08 00:35:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 078ba40b-9348-33ab-816c-0a7c3e427d47 | -6.05428 | -46.60004 | 2024-10-08 00:35:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| ec3ac202-1c4d-3884-8da2-a9845c2b06d1 | -6.04739 | -46.60677 | 2024-10-08 00:35:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| d2ed9bcd-fa69-3139-98df-77c03ed53577 | -6.03707 | -46.6082 | 2024-10-08 00:35:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 447e3bc2-6855-39a0-8320-32fab68c4588 | -5.98937 | -44.44344 | 2024-10-08 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d6b25929-ea55-3aea-bf6b-49fa0bc6b699 | -5.98808 | -44.434 | 2024-10-08 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 48a1f8d5-06fb-3ae6-87fa-e6bc9621b20c | -5.92119 | -45.51247 | 2024-10-08 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| dcddcd9c-96e9-3a5c-8ad3-6f30afcdfda4 | -5.9168 | -45.40686 | 2024-10-08 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 52439c7f-1023-32a0-b4c3-c22d9d157a8c | -5.91543 | -45.39661 | 2024-10-08 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 5ab4f2d6-5a68-3498-a8a0-997ee23cac7b | -5.90424 | -46.23219 | 2024-10-08 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 93507fb2-eb22-3d00-99a6-70a1c484b69b | -5.85448 | -44.87389 | 2024-10-08 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 56aacc87-7c7b-3bbd-bb0a-ad58337f1794 | -5.81813 | -44.13313 | 2024-10-08 00:35:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |


[Clique aqui para ver as próximas entradas](README12.md)
