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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97fefaa0-56aa-30ab-8f2d-c64047178807 | -5.70167 | -43.14782 | 2024-10-22 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b5417741-a0e8-32db-bc41-33a2f1c895bb | -5.69821 | -43.14359 | 2024-10-22 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ab505b56-286f-3d09-a936-96d2ba066299 | -5.69763 | -43.14709 | 2024-10-22 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f915fb40-d963-3a9b-8221-23a3232d1178 | -5.61875 | -42.77411 | 2024-10-22 03:53:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f3455f13-2668-38d0-be08-b98861d1ac14 | -5.61789 | -42.77927 | 2024-10-22 03:53:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 95a145b2-264a-303b-a664-b01ab2408d6c | -5.59245 | -42.93083 | 2024-10-22 03:53:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b5bb5bb0-aa22-3d69-aad3-4c41c7a6ddd4 | -5.45703 | -43.27007 | 2024-10-22 03:53:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ceab7802-2075-38e5-a335-1da24773c44d | -5.43566 | -43.22173 | 2024-10-22 03:53:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c511cb74-f8d2-3f84-97a4-147685f77a93 | -7.80205 | -43.21182 | 2024-10-22 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 07c8f238-db88-3f35-8103-034be1632556 | -7.80138 | -43.20937 | 2024-10-22 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 43498818-5e95-39c7-8fb0-f0355ad0f278 | -4.86322 | -43.24937 | 2024-10-22 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d217aa1-faf9-3182-a4f3-e1c789aa1ec1 | -4.5521 | -43.56877 | 2024-10-22 03:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3ca2f8a4-c414-3b39-8359-dc259d408323 | -4.53534 | -43.27365 | 2024-10-22 03:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fe49699-dd94-31e5-ae77-55060c5f6248 | -4.39897 | -43.57649 | 2024-10-22 03:53:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f31659d-c8ff-3fbb-b77c-59c6a689acc0 | -4.15933 | -43.35839 | 2024-10-22 03:53:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| df9ff7c7-8c81-30f2-9ea3-829a44764cb6 | -4.12336 | -43.34066 | 2024-10-22 03:53:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb7b127f-f6b7-3ab0-9914-4fef4191b129 | -4.76027 | -44.59955 | 2024-10-22 03:53:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 610cc99e-4a1a-3a4a-b4ac-e8f5f1976e14 | -4.6235 | -44.55112 | 2024-10-22 03:53:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc7f03d4-34f0-329b-b10f-2b4f1476c02a | -4.62276 | -44.55564 | 2024-10-22 03:53:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51214cde-0180-335e-a3a4-7e6934c15af0 | -4.18015 | -44.34583 | 2024-10-22 03:53:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa6aedad-20da-3718-9adb-81b6757baef0 | -4.10452 | -44.23438 | 2024-10-22 03:53:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c51039da-37fc-37f7-93b7-db22a3165573 | -5.1256 | -44.34333 | 2024-10-22 03:53:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2874657f-ae15-314a-85a2-bd9b5d9b9dcd | -5.1249 | -44.34763 | 2024-10-22 03:53:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03e3917b-b673-3674-9901-7257f6cc3df2 | -5.1243 | -44.34094 | 2024-10-22 03:53:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d0f8895-0c83-39fc-ba6c-37279f6e4eaa | -5.12357 | -44.3452 | 2024-10-22 03:53:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 502fde2b-8876-39ae-8078-84f7fdf766a4 | -6.39507 | -43.83735 | 2024-10-22 03:53:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2909dda3-fff0-3352-b1c2-98db882267d8 | -5.82946 | -43.65235 | 2024-10-22 03:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 914933c3-2ef5-3ffb-9eed-49858154e8a4 | -5.54259 | -43.94428 | 2024-10-22 03:53:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dfbb451-1d73-30bf-8d9c-86bf2deda5a0 | -6.24043 | -44.15729 | 2024-10-22 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddfb768f-8a82-366d-acf9-d61d6b515e20 | -6.23864 | -44.15766 | 2024-10-22 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3105fe6a-91f3-376a-a3e3-eb20942db0f7 | -6.23682 | -44.15255 | 2024-10-22 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a84beaf-9891-3156-a961-bd9e94e6e85d | -6.23635 | -44.1448 | 2024-10-22 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 720adb58-f009-3d18-be06-737d71c3b71f | -6.23568 | -44.14883 | 2024-10-22 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b38e6acd-2243-3cbc-8f6d-57b52f77f349 | -6.23391 | -44.1438 | 2024-10-22 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b6c21e8-4cec-3cf1-8bf9-a454b983f92e | -6.23323 | -44.14779 | 2024-10-22 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18f83b51-cd11-335e-9aec-9e78f3a77f22 | -6.23205 | -44.14412 | 2024-10-22 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4159099-884a-31cd-8c85-152d03dfb46f | -5.83429 | -44.6612 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab98d5bb-d379-33d9-9da6-563259e8aa40 | -5.8325 | -44.65843 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a1da404-142d-36b8-9206-f0bbadbf4edc | -5.83177 | -44.66283 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc8c37aa-2c47-3736-b1ce-ba8571d50d05 | -5.82981 | -44.66045 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1765755-a726-3865-a1bf-a9d623823507 | -5.82802 | -44.6577 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bef75c9a-c500-31f0-8903-bc961998bc7c | -5.82729 | -44.66209 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77af4f6e-383c-305f-b009-9ead5abb4e13 | -5.68953 | -44.48522 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92e1b38a-0861-3388-ba81-d74a8c531e63 | -5.58999 | -44.87987 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 26310df5-be8b-32f3-baa9-73fcbb003446 | -5.58624 | -44.87437 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 96a387c7-963d-3d94-b192-6e0795aea8b4 | -5.58544 | -44.87901 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2099c6d8-0b5b-37e3-bc60-9ba904b77fe4 | -5.58249 | -44.8689 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| aa31540a-d6db-3f76-a3ac-bdb400793160 | -5.58192 | -44.87112 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b7ee790c-ae96-39fe-991e-04d658580873 | -5.58169 | -44.87352 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 59a2f4ae-6196-3f32-881e-545bc650b739 | -5.58116 | -44.87577 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0400a368-25e2-3658-a302-bcf87c5d0e59 | -5.58089 | -44.87817 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 534a183b-e045-3239-91fa-585ed115659d | -5.57714 | -44.87273 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3b44ae56-85f5-3207-ac08-20dded0616ff | -5.5766 | -44.87498 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e6b3b4bb-15da-3f7b-a4b3-9a9f0724ddf7 | -5.57633 | -44.87738 | 2024-10-22 03:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 70bc4c53-58c8-32c0-94e8-3e501fbb3ae7 | -7.2128 | -44.13885 | 2024-10-22 03:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3506606f-d690-3e21-8b83-fb6fe34cdaa8 | -7.21243 | -44.1388 | 2024-10-22 03:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4aa05f21-b980-380a-a0ba-12ab31a74c1c | -7.21215 | -44.1428 | 2024-10-22 03:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db40cc84-2808-3eeb-8979-c69cd7535536 | -7.21175 | -44.14273 | 2024-10-22 03:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e810d4d-734e-3015-b7be-70764a0f5f7b | -7.20859 | -44.13808 | 2024-10-22 03:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a0b2abe-353d-3a2a-828b-43ad29b9ef18 | -7.20822 | -44.13803 | 2024-10-22 03:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f0bcdd2-cb73-373f-b3e2-308a5dddb087 | -7.20793 | -44.14203 | 2024-10-22 03:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de660557-cfe0-3196-a0c2-81648f9b9067 | -7.20753 | -44.14198 | 2024-10-22 03:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e39ee05a-3eb6-3b52-b12e-db3571a0264c | -4.949 | -45.42169 | 2024-10-22 03:53:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de0f0f87-dc32-320b-a2fd-2cce7504bacf | -4.94813 | -45.42698 | 2024-10-22 03:53:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dea84d13-9aa9-39f5-9d95-252b8c5d762c | -4.94791 | -45.4228 | 2024-10-22 03:53:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0434171d-e238-3e0f-b329-9d796f0ab4ed | -4.94728 | -45.43217 | 2024-10-22 03:53:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ac65495-b9af-30d1-a2f2-fab21e37e69e | -4.947 | -45.42811 | 2024-10-22 03:53:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef01c06a-e503-35a7-b138-7eeffb9bd0ab | -4.94611 | -45.43324 | 2024-10-22 03:53:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 088cc979-11a0-3026-926f-ef614e5eb40e | -4.9304 | -45.84734 | 2024-10-22 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b32017a-69c7-340c-9ed3-52ac5190c8ac | -4.92944 | -45.85304 | 2024-10-22 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6783d2f-1d12-3d92-90bc-a1969e63937b | -4.9067 | -45.83763 | 2024-10-22 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbc12b37-a67a-39af-834b-73b85a2cc7f1 | -4.90571 | -45.84343 | 2024-10-22 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87a21fa1-47d1-3827-8e6d-6fc3eeefdc8d | -4.90475 | -45.84904 | 2024-10-22 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ceff119-0679-3179-a87f-a7aa256c5a85 | -4.90272 | -45.83126 | 2024-10-22 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 070ca2db-5657-3b75-a220-fe7e9d8d0c9e | -4.90174 | -45.83696 | 2024-10-22 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c02f68b5-4626-3de3-b93a-c20e79c5348d | -4.89682 | -45.83608 | 2024-10-22 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b2e59fe-0834-372b-b322-a28c4dc6f42b | -4.89584 | -45.84184 | 2024-10-22 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0de4775c-722f-37d8-b9ad-646700d67734 | -4.89193 | -45.83503 | 2024-10-22 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74742ac5-31a4-3b7c-9465-4b8e70303ce6 | -4.83541 | -45.86478 | 2024-10-22 03:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f2bd3621-b805-3db5-8c1a-5b3d3c7b11c6 | -4.65446 | -45.69059 | 2024-10-22 03:53:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7e37a5c-7753-3649-a34f-ee44412817f3 | -4.64953 | -45.68996 | 2024-10-22 03:53:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f48668e4-119b-3584-bf3e-686e2f516ce6 | -4.6486 | -45.6955 | 2024-10-22 03:53:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29616074-cff3-3cbb-b341-8972014c8698 | -4.62827 | -46.0568 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2145a16a-66d6-377c-ba28-1caec3039413 | -4.6245 | -46.05582 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad5977fd-9ced-3e72-8cd3-7f22f1fea17a | -4.62382 | -46.05996 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46317d98-ddd6-3a3d-a011-f2e0974541cb | -4.62337 | -46.06267 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66c66827-3db6-32b7-ad8c-5f90503687b4 | -4.62228 | -46.0615 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 92f8dc09-6651-31ac-a67c-0d5ef70a6e6f | -4.5641 | -45.14718 | 2024-10-22 03:53:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75337f23-81fe-3f5e-8853-0adb2faaee3f | -4.56305 | -45.81174 | 2024-10-22 03:53:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| fd4dfd56-c08d-32c2-b9aa-9716fe766f8b | -4.56254 | -45.80893 | 2024-10-22 03:53:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8b45dcb2-cab5-3a96-8c53-e4a917148186 | -4.56159 | -45.81473 | 2024-10-22 03:53:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a386fdf3-3ed7-38f6-8496-3c859afddb11 | -4.55911 | -45.80509 | 2024-10-22 03:53:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 39ced97b-0c19-3f34-ab25-31f5804d7b72 | -4.55854 | -45.80231 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cd8be505-f6ff-3e49-9182-dd3dc1514e27 | -4.55814 | -45.81072 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 07477560-37c0-3a99-a0e8-211e6d657056 | -4.55762 | -45.80788 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e1539423-63ec-3184-a4b4-5a20eebe2d93 | -4.5542 | -45.80403 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cfad26a2-3d96-3d55-b8c7-7060e823fa51 | -4.55363 | -45.80124 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d336c727-50a6-3d24-a287-79e4e973fb88 | -4.55271 | -45.8068 | 2024-10-22 03:53:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| ff272ceb-d69d-319d-ba3b-dbb2fe0d43be | -4.42242 | -45.64132 | 2024-10-22 03:53:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3140adf3-097b-3d8f-b0c2-97b0384334a5 | -4.2625 | -45.59208 | 2024-10-22 03:53:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README16.md)
