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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fea0a9c-5c28-3070-850e-61ee807e8fb8 | -7.27476 | -39.45078 | 2024-10-30 00:33:00 | TERRA_M-M | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 1f25c874-f02a-3cfa-bece-68b3f7576c43 | -6.98946 | -41.32877 | 2024-10-30 00:33:00 | TERRA_M-M | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 17de0935-e66e-335c-889e-215c6b1fa26f | -6.98818 | -41.31973 | 2024-10-30 00:33:00 | TERRA_M-M | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 4465bff9-5139-3eb9-9f61-5e3625e84e38 | -6.98307 | -41.34812 | 2024-10-30 00:33:00 | TERRA_M-M | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 34ff21f9-b275-3bf7-8d8f-c00bcb3f2475 | -6.98179 | -41.33907 | 2024-10-30 00:33:00 | TERRA_M-M | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 17ca9394-02a0-3549-9962-f478ae2fbaf8 | -6.98052 | -41.33003 | 2024-10-30 00:33:00 | TERRA_M-M | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 61176bee-fde9-3e7b-ab29-40e26350b0b1 | -6.84676 | -42.8168 | 2024-10-30 00:33:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| efc4fd57-206f-3325-a1e6-dd6a45b51fc8 | -6.71925 | -41.11046 | 2024-10-30 00:33:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a79299f7-d779-3bcd-b504-943fd6ccab86 | -6.7126 | -37.49486 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 5def3775-9125-36e4-aae0-7014b11d5bd0 | -6.70129 | -37.49618 | 2024-10-30 00:33:00 | TERRA_M-M | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 3995d857-fc97-3455-a830-7afae4052042 | -6.69499 | -43.05095 | 2024-10-30 00:33:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 87472584-ee5d-3699-ba41-ee956ed0c23b | -6.67431 | -37.46986 | 2024-10-30 00:33:00 | TERRA_M-M | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 73406242-aafa-3d5f-9d89-7607bc3c2b39 | -6.61991 | -42.7704 | 2024-10-30 00:33:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 0f3cbc2c-5193-3640-9fb5-e8df1bc136a3 | -6.55489 | -35.26123 | 2024-10-30 00:33:00 | TERRA_M-M | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 36.7 |
| 9a3c2489-dc81-32d9-a244-320e80548bfe | -6.54724 | -35.2678 | 2024-10-30 00:33:00 | TERRA_M-M | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 0f182f84-e5df-3184-803b-2d3d617fc013 | -6.53571 | -41.57243 | 2024-10-30 00:33:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a796e35d-d85d-35c2-9674-0e4577b07527 | -6.53445 | -41.56347 | 2024-10-30 00:33:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| ccb9db24-8c72-389a-b112-357c2c9b7bd7 | -6.51153 | -43.65452 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 96899463-994b-3c7a-aae6-5bf310e2c938 | -6.46873 | -43.14076 | 2024-10-30 00:33:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2cf8a75c-2d0f-3603-a9f0-6d08a8a165e3 | -6.39772 | -38.91262 | 2024-10-30 00:33:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 755ead90-d512-3ef8-8a0a-63b4d6bd5118 | -6.37438 | -41.73579 | 2024-10-30 00:33:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b139b818-6539-3739-8616-911652d5c7bd | -6.33511 | -41.58603 | 2024-10-30 00:33:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 08c69d8c-a3b7-3113-87bc-f9ad66c15fde | -6.33383 | -41.57701 | 2024-10-30 00:33:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b54542f1-b3a4-3b97-892f-b576e2159f7e | -6.32693 | -43.44952 | 2024-10-30 00:33:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d5e97c3d-83a1-3324-acdb-4c7547d44f45 | -6.21254 | -43.28682 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 397c7937-5a56-30c1-a35e-f69048f93344 | -6.2113 | -43.27782 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 21715e9c-c637-3d15-81d1-1e78ebf7457c | -6.15261 | -41.86818 | 2024-10-30 00:33:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 360a1a58-6f91-3e03-9796-f244c36ba8cb | -6.06562 | -43.62542 | 2024-10-30 00:33:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| daf1692f-83fa-364f-bdec-5b4bd4144933 | -6.05962 | -42.65178 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 9c33a2b5-a5c1-3e8f-a73a-8b6fb3be1e7a | -4.52908 | -42.05585 | 2024-10-30 00:33:00 | TERRA_M-M | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 17538212-5baa-3a28-b0fd-8198e985ebac | -4.52018 | -42.05712 | 2024-10-30 00:33:00 | TERRA_M-M | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ed372810-adc4-34b8-bc80-b40dde209940 | -4.51538 | -43.13609 | 2024-10-30 00:33:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| d16079b3-70bf-3559-91ea-add2233bb9bb | -4.51129 | -42.0584 | 2024-10-30 00:33:00 | TERRA_M-M | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f419dff3-790c-36f0-8da8-5a957ec08274 | -4.50654 | -43.13734 | 2024-10-30 00:33:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| da176759-9a26-3181-abf3-06e2dcf027ba | -4.50531 | -43.1285 | 2024-10-30 00:33:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| ffa87eef-5d10-317f-9f05-d4d0bcc81cdb | -4.49876 | -42.8867 | 2024-10-30 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 87183484-c51c-340e-8dd1-dfb7043ab166 | -4.49754 | -42.8779 | 2024-10-30 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| a168cba9-40f9-38ad-bb00-582c7b6b8114 | -4.48871 | -42.87915 | 2024-10-30 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 043fe4da-2348-3145-89c8-032ad64b2d8f | -4.48748 | -42.87034 | 2024-10-30 00:33:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 17b718f8-b514-39a8-a62c-7fab2b560b04 | -4.35908 | -43.6117 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0949fb04-7130-349b-9c8b-03cdd2c9c93c | -4.35599 | -43.78646 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| a184e66c-1465-301f-b62e-3086da4f51d1 | -4.35474 | -43.77738 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 2f1461a6-ec93-3c97-ab30-cd47bad492c6 | -4.34704 | -43.78769 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 05d84e26-fdb6-3aa3-97a0-c421f2e6e90f | -4.3458 | -43.77863 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 37abc978-10fb-36c3-8686-32fd6fe30ce8 | -4.34455 | -43.76961 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ebab6847-3c5a-32dc-817a-49c6b5ffe413 | -4.3381 | -43.78894 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 31435838-a7ab-3056-b13b-d2d9cfe766b7 | -4.33686 | -43.77992 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 8ec34530-0500-3057-abf4-01f37b489733 | -4.33562 | -43.77089 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e240afe7-628a-3a94-9c6a-45e3954624b9 | -4.33337 | -43.6885 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54789d53-e4b4-3fc3-a8fd-ef81c412e61b | -4.33213 | -43.67952 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ca6b7321-2540-3da7-a00d-5bab6a2ef9e5 | -4.32593 | -43.63464 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| bcea7e5a-96d0-33a1-a6de-8eaa5bcf8c56 | -4.26904 | -43.28856 | 2024-10-30 00:33:00 | TERRA_M-M | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f1151699-482a-3099-aa0b-b5e2e60a9c16 | -4.26251 | -43.44918 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 137.8 |
| f5a6c12e-9f55-3836-a73a-02214e24df47 | -4.26127 | -43.44028 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 7b853680-6d5e-338e-aaf8-6a2827d46887 | -4.25363 | -43.45043 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| ed408ff7-cbed-3dff-80a3-1da5e91b0990 | -4.2524 | -43.44154 | 2024-10-30 00:33:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 61fb2c41-49b8-3fc9-9e1f-29291e9b53cb | -4.14236 | -43.83785 | 2024-10-30 00:33:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 9bdcde81-5e72-3e84-81a3-765d078de187 | -4.14007 | -43.08763 | 2024-10-30 00:33:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| c2dbd955-d332-3b96-968f-a546808d3760 | -4.13884 | -43.07882 | 2024-10-30 00:33:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a1108685-2eef-3b49-ad32-494a9a625a97 | -4.05009 | -43.24744 | 2024-10-30 00:33:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 1ae209eb-72c2-3989-8c9e-8fb59f063c56 | -4.04124 | -43.24868 | 2024-10-30 00:33:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 48569ecd-8a2c-38a8-a7d0-72e3af97f581 | -3.96037 | -41.48065 | 2024-10-30 00:33:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| b53adb5c-ddf2-3b89-aecc-9ff2214bfa12 | -3.95906 | -41.47137 | 2024-10-30 00:33:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 16747b5f-a3c8-301d-892b-4d34983b62ac | -3.9513 | -41.48194 | 2024-10-30 00:33:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |
| b26a665e-2bc4-3c8b-af91-74ec611a5791 | -3.94486 | -41.50181 | 2024-10-30 00:33:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 4c53e48c-bc5a-341f-9175-6e21651c8f56 | -3.94354 | -41.49252 | 2024-10-30 00:33:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| b20fd1ac-e36f-3455-8f8f-f8db2dea34e8 | -3.94223 | -41.48323 | 2024-10-30 00:33:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 28.4 |
| 37925922-77b6-3310-b4f0-9ee330f4dbf3 | -3.9358 | -41.50312 | 2024-10-30 00:33:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 0c1fa3c2-a0eb-336e-acc3-3c816ebf9454 | -3.93448 | -41.49383 | 2024-10-30 00:33:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 127.8 |
| cbd234f1-1fd2-3704-8fc6-615dd3085f41 | -3.93316 | -41.48453 | 2024-10-30 00:33:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 127.4 |
| c0547061-25a0-354a-ade4-e1a6d25364d8 | -3.85162 | -40.70969 | 2024-10-30 00:33:00 | TERRA_M-M | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 4d267a59-1802-393d-ae8d-36aa40901ade | -3.79442 | -41.61137 | 2024-10-30 00:33:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| bc6b1c69-2a14-3545-bb8b-6471fd01f533 | -3.78538 | -41.61267 | 2024-10-30 00:33:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 2c9259d2-e45e-3921-abff-36a0d505850c | -3.78409 | -41.60347 | 2024-10-30 00:33:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 593891c3-f218-3c57-b1ab-a7647d6e941d | -3.75734 | -43.3253 | 2024-10-30 00:33:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd03318b-eca7-3b3d-a05b-a65cc0071949 | -3.53969 | -43.61778 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 67d37702-c7ca-3431-b35c-b7873d800aeb | -3.53081 | -43.61903 | 2024-10-30 00:33:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 81331bcd-5734-360c-8c12-b7ad3283ef0c | -3.47099 | -41.99883 | 2024-10-30 00:33:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 548bdc9f-e9e8-3053-80cb-3fad5d8deb32 | -3.46204 | -42.0001 | 2024-10-30 00:33:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 44.8 |
| b5ef7c36-37db-37ea-93a7-60a9956526b8 | -3.46077 | -41.99107 | 2024-10-30 00:33:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 58bcb328-d03c-301e-8339-049b16500ffc | -3.45436 | -42.01041 | 2024-10-30 00:33:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 29b6c2b6-dee9-32fb-b498-eab5b18d8e9a | -3.45309 | -42.00138 | 2024-10-30 00:33:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| c7e13856-7844-3f3f-99c0-599f438346ab | -3.44542 | -42.01169 | 2024-10-30 00:33:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| c109277d-3a5f-322e-bdba-fdc7c5428d9a | -3.44414 | -42.00264 | 2024-10-30 00:33:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 747003ec-4547-3d30-a98b-932dd64f35d2 | -3.40146 | -41.63547 | 2024-10-30 00:33:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 047665ee-0886-3bd8-b04f-8c0561068ee4 | -3.40014 | -41.62619 | 2024-10-30 00:33:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 1b567fde-2431-3091-8c91-768460b33b5b | -3.04551 | -40.07888 | 2024-10-30 00:33:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 1c334d77-f8e0-3964-8164-f9bb572b283a | -3.04395 | -40.06773 | 2024-10-30 00:33:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 53.5 |
| c17d00e4-9676-307d-972f-590d97c9fbd1 | -3.03408 | -40.06915 | 2024-10-30 00:33:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 0fc79c1f-a1a5-3e95-8ad9-0ee4055c4414 | -8.96082 | -47.62362 | 2024-10-30 00:33:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d2ae687a-f6c5-3bad-b6a3-98d8bc52e36a | -8.95674 | -47.63062 | 2024-10-30 00:33:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| e1d9db5b-4467-3c5b-bbf9-3e5696867811 | -8.9508 | -47.64301 | 2024-10-30 00:33:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 8815eb4f-1752-3929-9fbb-8d7d7cd399b9 | -8.94865 | -47.62526 | 2024-10-30 00:33:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9f94e0cc-3a2a-3247-b5f0-02ce4adb9231 | -8.16049 | -47.16335 | 2024-10-30 00:33:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5f12b2d2-9034-36dc-a2b7-db25395dd665 | -2.16481 | -53.67764 | 2024-10-30 00:35:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| f7a83fa9-367c-3487-8c19-bdb9cc1ae553 | -2.16419 | -53.6826 | 2024-10-30 00:35:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 517b8592-02fa-32b2-a7b7-fd44ee205a96 | -1.67904 | -48.8105 | 2024-10-30 00:35:00 | TERRA_M-M | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6d5b2a6b-3f79-3f51-8a21-07d983e4b165 | -1.57726 | -52.97369 | 2024-10-30 00:35:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| dd5351a4-4456-3d8a-acbe-27afa7b2a016 | -1.54115 | -52.1406 | 2024-10-30 00:35:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 9c0a2cff-2abd-35aa-bcf4-502c95b457fa | -1.53676 | -52.13457 | 2024-10-30 00:35:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |


[Clique aqui para ver as próximas entradas](README11.md)
