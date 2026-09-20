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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10007dd6-7377-385a-ade4-5321f76a1e50 | -2.71443 | -57.96653 | 2026-09-20 04:38:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 846c252b-d0ec-38e7-9e1b-0167c48f9921 | -4.89501 | -45.62647 | 2026-09-20 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0326f1e8-633c-3638-adaa-97877ff319c3 | -5.50878 | -45.66359 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13bf564c-5b28-3c7f-83dc-7670482ee18f | 1.22035 | -50.98901 | 2026-09-20 04:38:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 58db2998-3510-3ca8-b510-1b8a096e770c | -0.52025 | -49.15186 | 2026-09-20 04:38:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1de2d95a-cbf2-3a9e-bef8-9b4bc6171e43 | -2.88753 | -57.82974 | 2026-09-20 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8340aa0e-77ee-35f9-9236-5ef3015cde2b | -7.02011 | -42.07859 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 16531638-3002-3f82-99c0-755f67545171 | -2.97374 | -54.77185 | 2026-09-20 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8fbf324f-fb09-3801-b82e-d9eb17ec882f | -4.68202 | -46.40399 | 2026-09-20 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 18d43849-1034-3bc3-af93-95b5ec2756e0 | -3.01053 | -54.17909 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10cb96aa-9d89-3e44-b3a4-86aa822d18b4 | -6.80044 | -44.76611 | 2026-09-20 04:38:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5b57e0a-8e28-3f16-b969-5f61713c8b20 | -5.84 | -49.86626 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 94b3f82b-aa5a-31a9-83a8-c7deeaeedb7f | -4.68258 | -46.40045 | 2026-09-20 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 57f8e882-436b-34b8-ba63-a37a2daa31aa | -5.21755 | -47.57532 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7a8fdf5-226e-38ba-8dbf-061d5fddc18b | -3.00545 | -54.18029 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a62c141-e450-3376-90c5-b0b9eff326e1 | -2.61244 | -54.75904 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 22d98805-c660-37e9-8e04-075db5311b9c | -5.41674 | -48.43895 | 2026-09-20 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb938100-9734-30f5-a106-e6f6ab9d9079 | -3.8478 | -45.42365 | 2026-09-20 04:38:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 742970ba-6ef0-3dce-9f99-5e0c5f5ad7b9 | -6.3087 | -47.63441 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af4a6bf4-391a-300f-9206-0b5727531b05 | -5.80087 | -43.76284 | 2026-09-20 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef7abba2-a5c1-31ae-88dd-a1c10e9c2977 | -2.60828 | -54.75678 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 6a5dda0b-a768-3352-86d9-27ec6cccb370 | -3.48046 | -59.59834 | 2026-09-20 04:38:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76410908-2f3a-3aa9-9f41-716542191c87 | -5.79079 | -47.36408 | 2026-09-20 04:38:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b17db67c-2de2-3d2d-b26f-dd891dd318ed | -4.37927 | -55.03364 | 2026-09-20 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b39a32f5-cadc-3ee2-84d1-9c536edd6de2 | -1.6043 | -54.44312 | 2026-09-20 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ae84413-4aa9-3f65-9276-472da85ef571 | -3.54012 | -58.69466 | 2026-09-20 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edcf3607-377e-36ce-b670-f47d93e0d2a2 | -5.35307 | -45.74051 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa99a712-6e3e-38ca-9cdc-61b2d3eefea0 | -5.22471 | -47.57291 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71423b67-ae19-304f-8a8a-10d6042e4d22 | -7.09061 | -42.0812 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 698d46e9-83ef-3e50-8765-e43cca3590f2 | -3.37049 | -50.442 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1189da0-628c-376a-b7f9-4b68b631bd31 | -5.18886 | -49.33558 | 2026-09-20 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b16ef88a-2d4d-3738-b4c1-e71a654474ab | -3.37768 | -50.44315 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74c825db-de48-3ffa-a1cd-6cb1ba33e771 | -2.8815 | -57.79432 | 2026-09-20 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53478d2f-3f99-34f4-91ad-081793a67752 | -4.98343 | -45.14963 | 2026-09-20 04:38:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1401f4f-c043-3461-a6b6-f80b48e915c7 | -3.85877 | -58.89621 | 2026-09-20 04:38:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2bc5fe30-f506-3bbf-8a23-bfc27dbfe606 | -6.59265 | -44.90625 | 2026-09-20 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4acfc63e-c484-3a50-ae3e-b790231cf600 | -4.89845 | -45.62704 | 2026-09-20 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de56f445-571c-3f8b-ae3b-7d1d204df37f | -3.73115 | -54.64904 | 2026-09-20 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a834fab1-6571-3d53-851f-413072cdd325 | -1.80768 | -48.06154 | 2026-09-20 04:38:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32f0563b-83d1-3507-b75b-676167164aed | -2.93968 | -51.97108 | 2026-09-20 04:38:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 539b5115-bf92-3c1e-9673-005bd851cef7 | -3.45254 | -58.21721 | 2026-09-20 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd5a8367-0c3e-3e65-b046-2a705de54922 | -3.49887 | -49.50901 | 2026-09-20 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e2a18bb-2feb-3ce8-ba3c-b9e95628a98a | -3.45043 | -50.59789 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 65e44116-6640-30b6-940b-5b10e249664e | -3.11973 | -51.08861 | 2026-09-20 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ecb8001-e481-30d6-97dd-f4c66ed9467c | -3.59092 | -47.35695 | 2026-09-20 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fb7186ba-e48b-34a2-bd21-341909b72a4b | -1.49738 | -48.93623 | 2026-09-20 04:38:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd6c7f93-6f28-32e6-8aca-9ef19632a0c8 | -2.25217 | -48.75242 | 2026-09-20 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d20bddbe-3a9e-37c9-94ab-1f7f600df738 | -2.60764 | -54.75828 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 133c9c76-e8b6-3b64-8db6-be380cb6f4e9 | -3.45861 | -50.61633 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60211d4c-91e2-3e83-a131-0d9d85fead73 | -5.40739 | -45.84453 | 2026-09-20 04:38:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50217fb2-2425-39fa-afef-7292a99ca961 | -3.75929 | -51.13954 | 2026-09-20 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecfc4319-7cfb-3779-83a4-a0110848e037 | -5.86469 | -51.57325 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e2a9ea7-7980-3f65-bf28-d4eac6624b25 | -6.96841 | -42.58506 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9ed82cba-886a-3dac-b3f7-b3121486c590 | -4.77818 | -48.05373 | 2026-09-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f5a1e0e2-f41d-398c-bf91-c899dacd3765 | -3.38194 | -50.43961 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5954d8de-7120-3e7c-919b-3b415dd861db | -0.51964 | -49.15572 | 2026-09-20 04:38:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8972393-6277-3488-ab4f-8c52dfddf783 | -3.36198 | -50.44904 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b17a0afb-862c-3403-a1d5-23c2d7d6b4ca | -2.96462 | -49.56272 | 2026-09-20 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d852599-3dce-319b-8956-4d5e065e6fa8 | -2.88221 | -57.79012 | 2026-09-20 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9251c5bd-001f-30bb-a894-7bb2fd79ffdd | -3.59423 | -47.35746 | 2026-09-20 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f5ac2c65-6654-3d72-a4de-19ca2eb9b6f5 | -5.66745 | -45.3123 | 2026-09-20 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0c5ec33-6fc4-3f5a-87bd-bd4ab8ee46a7 | -5.66454 | -45.30784 | 2026-09-20 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bf565a8-bae4-3ebc-b623-1e41cc2c64ba | -3.68649 | -60.62906 | 2026-09-20 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee8aface-fb45-3030-a4a8-1c4e9c3fcf84 | -5.41391 | -44.27489 | 2026-09-20 04:38:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0e6ad64-0303-3ab2-ab04-cfde08a26af7 | -4.56505 | -42.97226 | 2026-09-20 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c933888-5437-39dd-8e2a-3bd352854740 | -5.82474 | -47.77421 | 2026-09-20 04:38:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3282764-c99c-3c72-b7be-1fb4995d967b | -6.35695 | -43.36728 | 2026-09-20 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 182a9799-8eb4-3f7e-bb07-fd4082801ae2 | -6.51357 | -46.778 | 2026-09-20 04:38:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca4a27dc-b7e5-3f84-a076-6f82669d04d5 | -4.48425 | -55.4857 | 2026-09-20 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fc96ec34-19f4-363a-9a0b-5c4cb1fc16d3 | -6.53732 | -44.94676 | 2026-09-20 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a7a0b5f-ef2c-3a8b-a6e9-7b076d015de3 | -3.69075 | -60.56489 | 2026-09-20 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4857f5d-8c10-3560-a4b7-26aba6297352 | -2.52614 | -48.26492 | 2026-09-20 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fac91c17-b202-3e7c-b7ec-c5f0b5ad65bd | -5.42426 | -45.73601 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4c7f119-7851-384c-a72c-d7c5d3e44513 | -6.29876 | -47.63285 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b427c612-2081-308f-8f5b-36c89dbdc491 | -3.44976 | -50.60203 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 52fdf95e-f7ad-3548-a2aa-d08cbb18b47f | -4.2599 | -48.63875 | 2026-09-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2a349cd-b95d-3fc1-bded-1c95970a8c6a | -3.45567 | -50.61154 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93313d32-ac0d-3f7f-be96-ddef9843706f | -2.70926 | -57.96114 | 2026-09-20 04:38:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1820da0d-732a-357e-baee-e135a5ff92b8 | -5.40286 | -44.27314 | 2026-09-20 04:38:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08fcbd2a-479f-38a9-bae9-34a6de9bdc96 | -2.87717 | -51.73661 | 2026-09-20 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d73408c5-d46c-3ecb-9985-63631832ce02 | 1.26497 | -50.7372 | 2026-09-20 04:38:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7eba6dbd-df39-378b-894d-520e55b13e63 | -2.82772 | -50.46395 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7cf95c1-8060-377c-9d72-f1ead63f5e38 | -5.8394 | -49.86998 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f76611de-31fa-323f-81cb-0e81f8aff27b | -6.1676 | -47.49452 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e03f141a-5763-33d0-bc72-5b2f94007a0e | -3.73936 | -51.82368 | 2026-09-20 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 01d1bc08-5960-36e7-982d-eaaa18b6a84f | -3.40933 | -50.75998 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0719c55f-9319-3219-ada8-3dcdf9d227a1 | -5.66256 | -43.37363 | 2026-09-20 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96def64e-57e9-3ac3-bfdc-3dfdf3e6dffe | -6.31231 | -41.75568 | 2026-09-20 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 009f6acc-8671-314c-b1b1-a0f9da75ae02 | -5.82823 | -52.05037 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c5bc3c7-f4eb-38ad-933b-b03a3a34db15 | -3.04369 | -46.92834 | 2026-09-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aaf9986a-361b-3657-a348-09d18e052618 | -2.45226 | -49.21323 | 2026-09-20 04:38:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e2006f3f-d38e-3397-8a0d-4146c193e267 | -6.07117 | -47.86951 | 2026-09-20 04:38:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5a3a4e1-4110-3cc9-89ce-067b88a73eb5 | -4.68538 | -46.40451 | 2026-09-20 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6e2680a7-829e-307a-8b4d-0945ed04cf4f | -5.78918 | -51.8619 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 895f60d4-8f92-3e8b-8505-ce1066572f0a | -1.22262 | -55.72183 | 2026-09-20 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c809e4e0-3c00-324b-b375-659e54fbaeca | -5.35405 | -44.83477 | 2026-09-20 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65b94080-1269-3254-98ac-7d3b1d9a86eb | -3.84721 | -45.42737 | 2026-09-20 04:38:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d939572-8b76-3d39-aab0-73c16416af74 | -3.89248 | -49.06788 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 043efd5e-b8ac-3c67-a341-7f9d34bb83e6 | -3.42874 | -50.66317 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37e2ca72-58f1-3281-bd30-cbe372a1766c | -5.40395 | -45.84402 | 2026-09-20 04:38:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README51.md)
