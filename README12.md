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
| e3d3099d-4408-32ab-bd09-5694ce5845ca | -9.4338 | -40.30839 | 2025-09-14 03:47:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 925c1ae2-ff13-3bfd-a4c2-53012e1e8c3e | -7.57073 | -44.38391 | 2025-09-14 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12c696b9-074e-3896-827a-a28fbd7cedff | -10.59926 | -44.33436 | 2025-09-14 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c163e3a4-d7ff-352b-b27b-332a3e366f93 | -3.59596 | -47.52026 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| b4b3dc0e-64f3-3a2f-b23a-f51cad7329bb | -9.74828 | -46.86951 | 2025-09-14 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29944b00-9395-3634-91f5-33fef317641c | -7.61744 | -46.71102 | 2025-09-14 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 365eb898-8d45-3812-a046-f4a50d73e873 | -8.06642 | -43.00361 | 2025-09-14 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 310eba04-5dea-3d2d-8e90-e3371f962c06 | -3.22278 | -47.12598 | 2025-09-14 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6252a17-90cc-313a-b32a-3cd3434ee9fe | -9.73885 | -46.04685 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9f9b3e55-d3a3-3586-9c9c-8446c1a463ee | -9.05864 | -47.02714 | 2025-09-14 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad96b789-2603-3d2a-a648-5b9fe9e5e9e4 | -8.17414 | -46.7718 | 2025-09-14 03:47:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d56c5d22-6413-301b-aef5-daad00b94042 | -3.59624 | -47.51229 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 64d39094-7183-32e9-8c48-3eb9ff64bcbc | -8.07926 | -44.51543 | 2025-09-14 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 630fb9fb-cbff-3529-8585-ce7a87f8aad1 | -3.59677 | -47.51548 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 0798efb8-c3ad-34bb-ae47-cc0e1b73732d | -10.76927 | -44.78243 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f124e872-92d8-3fcd-8a52-ad5b3722e676 | -3.21528 | -47.12739 | 2025-09-14 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4d790ee8-5248-31e8-a2f9-6b97b298b248 | -7.61267 | -46.70578 | 2025-09-14 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcea0ace-d9ea-32c0-8e8c-6bac1781d7f6 | -8.67952 | -47.11073 | 2025-09-14 03:47:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 345788b3-0735-33bb-94c9-5f3dc4136125 | -4.45682 | -38.35397 | 2025-09-14 03:47:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 77bdc1b9-b960-35c6-82f4-410a8b2b3f62 | -8.09042 | -44.50703 | 2025-09-14 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa2d525b-767e-3d4f-a640-4bbefe9d74e4 | -8.14077 | -43.6678 | 2025-09-14 03:47:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f018ffe-4b9c-34b6-98f8-5ba39ae1fb33 | -4.82165 | -38.65841 | 2025-09-14 03:47:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 891e3fbe-878e-31ed-aa1e-32895a653723 | -6.98606 | -44.55202 | 2025-09-14 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e21ea4d3-5a45-30a1-9016-75dcea8a1473 | -10.13583 | -47.19443 | 2025-09-14 03:47:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87d95db8-3a8c-39a2-a627-86e501532976 | -8.93906 | -46.04902 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bf3db35b-1459-39bd-8046-4302e4993619 | -4.8034 | -42.74446 | 2025-09-14 03:47:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 9232a0ff-5b42-3580-9b40-9e81097d178c | -10.06933 | -47.15334 | 2025-09-14 03:47:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d051e2a2-6638-3242-a234-e56f31ccc02a | -8.62609 | -40.19859 | 2025-09-14 03:47:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b481541d-a177-362e-b1f9-d7cc943ea16f | -3.89815 | -40.91951 | 2025-09-14 03:47:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d352976d-0b35-3633-8b52-417e55da2254 | -9.8543 | -46.47913 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c25cef26-4670-338d-9a9f-2a764ed0a0c7 | -11.01543 | -43.15582 | 2025-09-14 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8f47a6c-4930-368a-877e-f944065a8bf6 | -8.95835 | -44.44269 | 2025-09-14 03:47:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a7e73ac-540a-3bb3-b716-a29850da430c | -5.67949 | -37.21924 | 2025-09-14 03:47:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ee0f50bd-dd05-39a6-b0d7-6a8caf5ca857 | -4.64118 | -43.18233 | 2025-09-14 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef666d66-2146-3363-a453-697ce89456d1 | -3.60214 | -47.5213 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 515e7126-d217-3fd2-9df4-5e2153a8a020 | -8.98315 | -45.78099 | 2025-09-14 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03f237d3-7c81-3d58-914c-075f5c7f642a | -9.8549 | -46.47589 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f07e8f4-5023-34a1-911c-2126156e4368 | -7.6126 | -46.70636 | 2025-09-14 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77fb6dfd-96b2-34d0-8820-2617b3fe1ef6 | -7.31378 | -43.93396 | 2025-09-14 03:47:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58710b2c-1f20-38e3-b01f-5834f481536b | -7.5055 | -44.67566 | 2025-09-14 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c132cd0-e481-3317-b1da-4ef2b6f10f37 | -7.38438 | -44.04319 | 2025-09-14 03:47:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54941cba-80a2-3553-a76e-2310c1e0f87f | -4.7997 | -42.73949 | 2025-09-14 03:47:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| af3d4274-bdff-3517-a9e5-918bffd49ac8 | -4.70057 | -43.22289 | 2025-09-14 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a357906-4e19-31c1-8ca0-b874e9a72e0b | -7.31297 | -43.93868 | 2025-09-14 03:47:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d44616b3-becc-3db0-bc75-103a65be8276 | -7.6168 | -46.71462 | 2025-09-14 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| daf28557-534a-3ba1-ba61-73f1739bf0b9 | -9.85301 | -43.14151 | 2025-09-14 03:47:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2bfbbe98-28a5-3e2e-9108-91278d1f0f82 | -10.60006 | -44.32986 | 2025-09-14 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4ed6c30f-bbfe-3905-943e-3112167bdaf4 | -3.89864 | -38.40277 | 2025-09-14 03:47:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b655925f-02f2-35d7-a150-0ae18880207f | -6.65737 | -46.08858 | 2025-09-14 03:47:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bd2a839-1716-3f6a-91dd-a45c6cb75663 | -8.95377 | -44.44166 | 2025-09-14 03:47:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 930d6e9a-f925-380b-b34b-a2805ba700df | -7.61196 | -46.70998 | 2025-09-14 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1ba7613-6651-306f-aabf-8a7836b60275 | -8.20423 | -43.76855 | 2025-09-14 03:47:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 20c771af-6f32-33a6-b7e1-4ceec56fae3f | -10.76014 | -44.78071 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e45205f2-4294-36fb-91da-346c6283fa97 | -2.26039 | -47.85349 | 2025-09-14 03:47:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93cd03b4-1829-3fe2-aa1a-d5443919bd0b | -10.7656 | -44.77649 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cb3f2b0-99d7-3bb5-a1c8-1447d333f408 | -9.62937 | -40.61878 | 2025-09-14 03:47:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 94a9fee5-9dad-33c7-a4bd-ab04f325ec7c | -8.62253 | -40.198 | 2025-09-14 03:47:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 27f7d1a4-e13d-3522-a3d7-7e81141ba0b1 | -7.37092 | -44.34401 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1240a8db-781b-3f8c-a051-d0be2f97b559 | -9.49416 | -46.41042 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 588db53a-d5cb-3206-bce6-bef0194ab200 | -3.22805 | -47.13151 | 2025-09-14 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2dfd80d2-14c8-37fc-aa58-02c5b72c660f | -7.61617 | -46.71821 | 2025-09-14 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6285799e-35e2-37e1-b88a-63635cc363d1 | -10.76384 | -44.78646 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bb24803-fce7-32ca-9c9c-b7180906ef3f | -7.02322 | -44.53722 | 2025-09-14 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15116ba9-8393-3e04-8279-245f63a7575c | -8.93849 | -46.0521 | 2025-09-14 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4344918-e521-3533-afaf-e9401d3226d3 | -7.51785 | -47.63816 | 2025-09-14 03:47:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2f08d43-1810-3ca9-9818-8a9301b39ab4 | -10.76196 | -44.77039 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ab626e2-0b72-390c-aa78-209262d679a5 | -3.21452 | -47.13191 | 2025-09-14 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2dec8b05-f620-3871-85ef-0708b23474b5 | -3.08418 | -49.46025 | 2025-09-14 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d3cfbe0-3364-36e2-abbd-b510dbb06cd3 | -3.22387 | -47.63493 | 2025-09-14 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40b1b7d7-279c-3758-83c0-8d2698f4c4e1 | -6.88351 | -45.63981 | 2025-09-14 03:47:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2586c64-e6a7-34f3-b8d4-68800b2fab18 | -9.00215 | -45.76256 | 2025-09-14 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28219b92-85f7-3f3c-ae71-82f999476849 | -8.49922 | -44.7297 | 2025-09-14 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77cdc00a-98f5-33b2-9a96-b7279c0c7265 | -8.13708 | -43.66271 | 2025-09-14 03:47:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cb45f1b5-e9a2-38d4-8520-41ad870a67fe | -6.65675 | -46.09204 | 2025-09-14 03:47:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10e989e9-f0d4-38cf-b1b6-9671e13c5219 | -8.62186 | -40.20207 | 2025-09-14 03:47:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 64219953-7b58-3f8a-84ed-4e1c75d08e60 | -10.13649 | -47.191 | 2025-09-14 03:47:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63d58438-ef09-3514-980f-638e362bb27d | -10.75648 | -44.77471 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 70a83efd-399d-3d07-a768-f1f4dd833891 | -6.88856 | -45.64149 | 2025-09-14 03:47:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93a0ae14-e90c-3b2c-98f3-906f9e191e56 | -5.66344 | -37.21314 | 2025-09-14 03:47:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9fcfa2c8-b42d-37ec-b7e6-5ccfdd2fa96c | -8.49628 | -44.71853 | 2025-09-14 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b7b0614-506f-352d-a150-8fbba225f642 | -10.75188 | -44.69498 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7846dad9-fa55-3a20-aa5d-0220bc2efcdf | -3.22471 | -47.62997 | 2025-09-14 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b79535c-4260-3616-8c57-1dff9f62f3d1 | -8.35506 | -44.7398 | 2025-09-14 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1e21274-0812-333b-bac9-25b6f0053dfe | -7.37294 | -44.34098 | 2025-09-14 03:47:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65fef18c-c422-35b3-9f5f-aa9672a7777f | -9.01869 | -40.34404 | 2025-09-14 03:47:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b268fc46-2020-30c1-8dba-f07a267a1fd8 | -8.50531 | -44.72796 | 2025-09-14 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dadfd63-8545-3098-b2ea-06f6462fa219 | -6.88449 | -45.63427 | 2025-09-14 03:47:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f22f169d-1bbd-30f5-aa27-dc18a7f709f4 | -3.60158 | -47.51809 | 2025-09-14 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| f66626c6-6508-3174-baa5-8192b97187c2 | -7.30753 | -43.94286 | 2025-09-14 03:47:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 27619d7f-276d-3ad8-9610-3b9a09e7c34b | -4.8041 | -42.74023 | 2025-09-14 03:47:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d885714d-2384-3ea1-88b9-3122e26c4b14 | -3.21756 | -47.63422 | 2025-09-14 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef672d61-8641-33ef-8190-ad27b8078665 | -8.49678 | -44.72112 | 2025-09-14 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29a46595-6083-379e-96bc-dd59490fa09e | -7.60586 | -46.71193 | 2025-09-14 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24c1c2eb-0ea3-3f0d-a13a-c803d1227c2b | -2.82322 | -47.72521 | 2025-09-14 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2584583b-098d-382d-a02d-a1f150571753 | -3.31571 | -44.1814 | 2025-09-14 03:47:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06e5943d-8ec8-37ea-95e2-2252e7483410 | -9.11839 | -46.94924 | 2025-09-14 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb59df01-adf8-395d-8d76-d4806094a9e1 | -5.06433 | -40.47137 | 2025-09-14 03:47:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 0a2c5e73-3984-3ad2-afb1-3d80a912bff1 | -2.26021 | -47.8497 | 2025-09-14 03:47:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3b9c411-1780-370b-baca-61050c7d524e | -9.05818 | -47.02768 | 2025-09-14 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37a4a534-dc4b-31d5-9c21-40e8d45f8fda | -9.06343 | -47.03175 | 2025-09-14 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README13.md)
