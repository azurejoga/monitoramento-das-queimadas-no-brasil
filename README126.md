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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87a8d394-956f-34e2-a813-7d6eac81902f | -4.35087 | -43.79356 | 2026-10-07 11:40:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| a5642af8-d98a-3e60-825a-037bafbbc34a | -7.21596 | -44.28764 | 2026-10-07 11:40:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 68dbb984-efa3-3609-b5c2-ec237fc8ccb5 | -6.15359 | -51.73681 | 2026-10-07 11:40:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 7461cb4c-097c-3614-a07a-a07aa6f6d9a2 | -7.88468 | -44.21013 | 2026-10-07 11:40:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 7c456955-e2b3-3238-8a9f-ec1e294a8d7b | -7.56528 | -46.72731 | 2026-10-07 11:40:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ef99e5dd-faa4-3548-8239-ab98f08af4c2 | -7.53755 | -45.87469 | 2026-10-07 11:40:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| b10d021a-ef78-3bf9-b55a-0415f57297e8 | -6.93302 | -43.67139 | 2026-10-07 11:40:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 43.2 |
| fb8dbb35-53ec-3f21-a64c-3e85821494da | -7.88176 | -44.23213 | 2026-10-07 11:40:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f5f82503-0c9f-31c1-ba71-da628abd6c05 | -6.15345 | -51.72668 | 2026-10-07 11:40:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 5d989b47-b5f1-3a88-9dd8-960d530f50e6 | -6.89619 | -45.90842 | 2026-10-07 11:40:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 762bf916-a008-3d79-9aba-c97d753c67e5 | -7.56024 | -46.69963 | 2026-10-07 11:40:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cdb1265d-0b82-341e-bcac-98cffe9c4de2 | -6.31457 | -43.33576 | 2026-10-07 11:40:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 997832ec-e00f-3d07-97d7-515f37752e9b | -5.72376 | -41.68118 | 2026-10-07 11:40:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 24.6 |
| e543735e-5d55-3a61-9163-c4c1a00ece0c | -4.8954 | -43.46633 | 2026-10-07 11:40:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7a1e37ee-e8f2-316b-a1dd-195ac13c98bd | -6.35347 | -42.5745 | 2026-10-07 11:40:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 56bbbda8-16a4-3b1c-a290-3d5a7433ac3f | -6.88123 | -42.91654 | 2026-10-07 11:40:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 074774e5-f337-31d9-a3e2-ca8f9c94d79e | -6.0223 | -42.26827 | 2026-10-07 11:40:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 717e531f-f459-3d3a-9624-d62c2d71fc24 | -6.02418 | -42.25459 | 2026-10-07 11:40:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 35.5 |
| 7eca6786-54ec-3d58-af08-cabac64ce87b | -9.18695 | -45.68418 | 2026-10-07 11:42:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 650d6f87-bc17-38ac-807e-b4122a1cf340 | -11.09409 | -47.59445 | 2026-10-07 11:42:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 439bc061-7fc6-31f3-a4d9-ad6c6fa94f64 | -11.08067 | -45.65232 | 2026-10-07 11:42:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4c3aafec-8009-3241-bfd3-60408d1e0a3e | -11.10283 | -45.68168 | 2026-10-07 11:42:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 8d0b46a8-adde-3231-95a5-9c0202d4bd7e | -11.72823 | -43.64969 | 2026-10-07 11:42:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 3ed5afc1-1f3b-3c0b-941c-e198d3723bb0 | -11.22736 | -45.25409 | 2026-10-07 11:42:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 75f74a6a-7a9c-3813-83a5-f4f182f8c284 | -12.3085 | -47.94707 | 2026-10-07 11:42:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7de5ceee-03e8-3b1e-a578-1930f74ef3ef | -10.46511 | -46.82669 | 2026-10-07 11:42:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 3dc1e2af-f1f3-3b46-9c90-6d2d6ee44ded | -11.79353 | -46.6973 | 2026-10-07 11:42:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 05a8728c-2cf6-3090-8a1e-8cb135b0a2c3 | -8.90325 | -49.96983 | 2026-10-07 11:42:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 77d64c1f-8c5f-31c4-a7bd-4017e4deda3f | -13.09598 | -47.00415 | 2026-10-07 11:42:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 1fa92b6f-afab-3d13-95f4-175183964179 | -9.03781 | -46.87984 | 2026-10-07 11:42:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9578b635-79e9-3981-a55b-66edc9f7c494 | -10.86309 | -50.65834 | 2026-10-07 11:42:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 56b8ed5e-87c9-3c27-88ad-624e2f493a9f | -11.36998 | -46.69145 | 2026-10-07 11:42:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7c4aa0c6-826f-3a91-8433-32268db307bf | -11.37763 | -46.70178 | 2026-10-07 11:42:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 188.9 |
| ec31922c-ddca-3f9d-8c02-e93780af9086 | -8.58944 | -45.67377 | 2026-10-07 11:42:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| bfeb2817-a3d9-3935-8c0c-5c738fa0ed3a | -11.78331 | -46.7053 | 2026-10-07 11:42:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| fbb0ab01-688f-3b9a-b5f0-c390670c4b90 | -11.38656 | -46.70299 | 2026-10-07 11:42:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2f22d202-f1b7-3049-b0fd-3c6c8efaade7 | -10.79811 | -46.56489 | 2026-10-07 11:42:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 64b44583-f221-3061-86cd-4ba1f82b0de0 | -11.06986 | -45.8571 | 2026-10-07 11:42:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| cde34cce-66a9-33b9-9851-ac1fa50775f3 | -8.30388 | -45.47252 | 2026-10-07 11:42:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2b6cd187-8020-3bcc-a65f-7a94819ab584 | -9.25894 | -47.9131 | 2026-10-07 11:42:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b2959b16-138f-318d-ab64-5394282ea465 | -11.73277 | -43.65611 | 2026-10-07 11:42:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| c3bb8bd9-aac4-3341-bdce-5c2747f2049a | -8.44973 | -46.40896 | 2026-10-07 11:42:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 63868ed0-4b7f-3421-bf2c-3ea02da31e92 | -12.17063 | -44.7076 | 2026-10-07 11:42:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1b770b3c-699f-3d68-90f2-de93a4f84005 | -11.80247 | -46.69857 | 2026-10-07 11:42:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2b7e8afa-8cea-3fdd-b958-689623c3b3b9 | -14.26932 | -46.37228 | 2026-10-07 11:42:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a2896bbb-2f4d-3ef4-adc7-ac9bc4bc267b | -8.21622 | -46.35812 | 2026-10-07 11:42:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 4b6e6f0f-3607-35a1-947a-484bc3f8d1c3 | -9.03654 | -46.88872 | 2026-10-07 11:42:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 31f50028-e86f-3cca-b8e1-2bad29e813a7 | -8.44214 | -46.39883 | 2026-10-07 11:42:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| df62322f-e5a3-3bae-9123-686eaf993144 | -12.99488 | -47.06846 | 2026-10-07 11:42:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 4defd3d1-ea02-32a1-a0c9-ce534a7be14b | -15.45111 | -43.94929 | 2026-10-07 11:42:00 | TERRA_M-M | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 96ad24d7-f30a-3a96-b3a0-673513fd9eb0 | -10.49371 | -47.27507 | 2026-10-07 11:42:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1193ddb2-ad62-38b0-84b3-fcce7d63b7c1 | -11.72646 | -43.66309 | 2026-10-07 11:42:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 920ad3db-4012-33c9-8b21-47a75658d28b | -11.14892 | -46.09006 | 2026-10-07 11:42:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 40ac1b9d-5408-3f68-aecb-209a6037b2f7 | -13.23253 | -43.56613 | 2026-10-07 11:42:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a350954e-f807-3fe3-93c9-b5328f7c4776 | -9.94475 | -50.55873 | 2026-10-07 11:42:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 44f62f62-ace7-3eb1-85b8-f2ad4d55746e | -10.99204 | -45.41921 | 2026-10-07 11:42:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 28cef073-2abc-3b48-b0e0-b83ce4c2113f | -8.20989 | -46.33904 | 2026-10-07 11:42:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6bc759be-f306-360f-b38d-75a3b6517cb7 | -11.22169 | -46.23199 | 2026-10-07 11:42:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| da36645e-bee8-36f0-813c-36d49460a0a1 | -11.05626 | -45.82942 | 2026-10-07 11:42:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cd041d8e-ccec-38fe-bd44-7b95aaf255f2 | -14.57458 | -43.82785 | 2026-10-07 11:42:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 60862c48-15b5-3b63-bfc5-3d4e6cb2b52b | -9.80895 | -44.78225 | 2026-10-07 11:42:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6f255060-480c-3675-b4bf-725bd1b9b762 | -15.2493 | -43.26531 | 2026-10-07 11:42:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 3dd14996-4b0c-3d22-b6f7-5d7211c0dd4b | -9.16396 | -45.10978 | 2026-10-07 11:42:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b5f2cf70-83c0-353e-98c4-e40f94329694 | -15.45242 | -43.95607 | 2026-10-07 11:42:00 | TERRA_M-M | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 24.6 |
| a24e60b3-c6f8-3643-8d6c-06b36ed0248e | -12.82583 | -44.45083 | 2026-10-07 11:42:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f443a167-d482-3fae-b63d-a2ca89a532ec | -10.28982 | -47.99266 | 2026-10-07 11:42:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4c6429a4-2318-3e57-add5-371062bf7f2c | -14.16792 | -41.95239 | 2026-10-07 11:42:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 4cfd7dbf-51be-3522-9ab4-bbd1d84cb3f1 | -9.52997 | -46.85269 | 2026-10-07 11:42:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c77ff3b1-4ecb-3388-bf85-c234cba51d5e | -11.08203 | -45.64248 | 2026-10-07 11:42:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| b3411410-ea1f-32f2-ab6b-2e6b5cbf9f63 | -11.07117 | -45.84735 | 2026-10-07 11:42:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 89c302d0-b91e-3e1b-a351-8e2157d27842 | -11.87591 | -44.77649 | 2026-10-07 11:42:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f5775a58-1769-370b-9fe7-5dad40c68b3d | -10.46384 | -46.83569 | 2026-10-07 11:42:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 50c825cc-fe58-3f44-a763-e20f941c6ab9 | -8.30255 | -45.48212 | 2026-10-07 11:42:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| bc2fbb1e-b066-3c34-ad95-985cf9c978c7 | -12.99617 | -47.05923 | 2026-10-07 11:42:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| d5613963-2c61-3f25-a42d-fc45d165c730 | -11.72214 | -43.65477 | 2026-10-07 11:42:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a576066f-94a9-3351-946a-428f94741718 | -9.11485 | -46.3985 | 2026-10-07 11:42:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a080f19e-43f6-3365-94c4-72d05758d9d9 | -8.90739 | -49.96597 | 2026-10-07 11:42:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4815a8a0-c098-372e-8281-1387aa60e548 | -11.78586 | -46.68676 | 2026-10-07 11:42:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| d3915d25-03b6-31ae-92b1-deb6f9a2a9ce | -16.14519 | -43.5189 | 2026-10-07 11:42:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 859ad156-aa45-3cbc-9297-2809ef84838b | -8.71015 | -45.19914 | 2026-10-07 11:42:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| af6a3ea7-006f-3fa2-9626-e87326661208 | -11.26026 | -45.19028 | 2026-10-07 11:42:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1bd4b10c-e12f-36f1-b8fd-f85ed3a65188 | -10.36556 | -46.22355 | 2026-10-07 11:42:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 490f2d35-84f3-349c-be15-9ed3c668eb38 | -9.01493 | -44.84996 | 2026-10-07 11:42:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 9b333252-3b32-3d1e-9a2c-4049335278e2 | -9.62724 | -45.83301 | 2026-10-07 11:42:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ba323c89-af3c-332a-9ba2-119ab2216a54 | -8.90575 | -49.97673 | 2026-10-07 11:42:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 59fe7f1b-680e-36ef-89cd-18ba43cf16c9 | -11.37891 | -46.69261 | 2026-10-07 11:42:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 7e390770-7801-36cf-bab0-1b8feaaa6d7f | -8.44088 | -46.40779 | 2026-10-07 11:42:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 585e5f78-e004-33a7-a9d6-a977bbd552e1 | -9.25717 | -45.64168 | 2026-10-07 11:42:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 67f599bc-8af7-3c37-97dc-579d8669b471 | -11.36869 | -46.70067 | 2026-10-07 11:42:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 59fcccc0-69e0-3a9b-8c97-df3afdd3eb65 | -8.69822 | -45.21749 | 2026-10-07 11:42:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9f430136-e195-36b2-868c-3ac490e40478 | -9.35935 | -42.19974 | 2026-10-07 11:42:00 | TERRA_M-M | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 92c9146d-3e2a-3edd-8dfa-74dd9b0887a3 | -8.21749 | -46.34914 | 2026-10-07 11:42:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 48c8143f-2ea4-3cb9-9d92-fa4c2c35e6d4 | -11.73444 | -43.64272 | 2026-10-07 11:42:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1a31e773-a2e4-3cba-9549-344f5bba96c1 | -10.9747 | -45.40633 | 2026-10-07 11:42:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 95ecf572-7e67-36b8-b261-e75d407ddeb2 | -11.78459 | -46.69603 | 2026-10-07 11:42:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 95e962f2-3b13-32e2-9383-f61141a0aa04 | -11.2204 | -46.24142 | 2026-10-07 11:42:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0f16abe2-707c-383b-a336-0edb4b84cc41 | -16.47409 | -41.81859 | 2026-10-07 11:42:00 | TERRA_M-M | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| d2bb45b2-c73f-3c51-9ca0-b4d209380f5f | -11.06274 | -45.85016 | 2026-10-07 11:42:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 4430084f-7801-3be4-b02c-07b0c53769ae | -7.88782 | -49.83858 | 2026-10-07 11:42:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3e71cf6e-b7c7-3b54-bef6-a065eb4308ef | -11.79115 | -46.57712 | 2026-10-07 11:42:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |


[Clique aqui para ver as próximas entradas](README127.md)
