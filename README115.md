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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d63a1999-edc6-3562-a446-db877a0bf6be | -8.6053 | -45.14056 | 2024-10-25 12:51:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| e8b96c55-ba5f-31c1-8b44-8328fcb12aa8 | -8.60343 | -45.13429 | 2024-10-25 12:51:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 7fc63149-af62-393c-93a7-f4fb72eb76ab | -8.59616 | -45.12503 | 2024-10-25 12:51:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 43.4 |
| dde14105-30bd-3258-af26-788e1520bf3d | -8.59435 | -45.13918 | 2024-10-25 12:51:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 0600a0b9-06cb-3112-8a7e-b8a811fd4386 | -8.59247 | -45.13299 | 2024-10-25 12:51:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.5 |
| f44207e0-54e4-357f-a899-f587cc85afda | -7.93836 | -44.88926 | 2024-10-25 12:51:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 7a126742-f807-37ab-94b7-7aa17d69242d | -8.05891 | -44.0637 | 2024-10-25 12:51:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 77967d7f-b226-3045-be99-f368c5880600 | -8.05673 | -44.08024 | 2024-10-25 12:51:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| a5d827db-1822-3e6b-88fd-cb022a44383e | -9.89312 | -45.0956 | 2024-10-25 12:51:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| df611b4a-6172-3c03-a610-05457c28442b | -9.89282 | -45.10149 | 2024-10-25 12:51:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 424d462d-6469-3357-8f20-44f51ccc322a | -9.54458 | -45.22375 | 2024-10-25 12:51:00 | TERRA_M-T | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 879a5461-f441-3e81-8f21-37852bca0bdf | -9.54274 | -45.23785 | 2024-10-25 12:51:00 | TERRA_M-T | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 29.4 |
| b3464414-f31b-332f-a3cc-c3333fccc775 | -10.87065 | -44.78802 | 2024-10-25 12:51:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 1da9ab61-042d-3148-b821-d4611f513eb4 | -10.8493 | -44.79581 | 2024-10-25 12:51:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 46c0dbd3-2f8d-357d-bd74-7856cf0dee13 | -10.84731 | -44.78502 | 2024-10-25 12:51:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| e9f7db1e-38b9-33bd-b008-b99449eed5a3 | -9.66325 | -44.39743 | 2024-10-25 12:51:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 1f85e257-fe70-349b-862c-2f6137f60d08 | -12.1039 | -45.72008 | 2024-10-25 12:51:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2e4cab3a-d2cf-35ea-82f4-8f2e676302cb | -7.83426 | -45.42743 | 2024-10-25 12:51:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fa66182b-8254-3188-ae0e-0e3257b0e17c | -7.9436 | -45.69411 | 2024-10-25 12:51:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| b7fdd35b-9d22-32c7-a108-02111ca5cc29 | -7.81404 | -45.5807 | 2024-10-25 12:51:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 0b17e9cd-30b6-3f7a-8f62-3433ac4e5bd2 | -7.53552 | -45.83845 | 2024-10-25 12:51:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| ee77cc23-ec16-39e2-9761-2ac157cd9434 | -7.53388 | -45.85048 | 2024-10-25 12:51:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 6592b7f2-f959-3d32-8309-8a0cee9e0c7b | -7.29114 | -45.7625 | 2024-10-25 12:51:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 57296efd-402e-382a-9183-d1f93502b16f | -4.92386 | -48.5093 | 2024-10-25 12:51:00 | TERRA_M-T | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| f80524a4-7ee8-3d69-b2fc-80a78caae439 | -7.28948 | -45.77457 | 2024-10-25 12:51:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| b12c588c-0321-38e8-aab7-81a37e8fe65f | -7.28858 | -45.54966 | 2024-10-25 12:51:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 63fc1087-6301-3546-b45b-578ee3bb02e5 | -7.18327 | -46.3257 | 2024-10-25 12:51:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1626546b-890b-3760-b191-5852b3f8036f | -7.18176 | -46.33675 | 2024-10-25 12:51:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| e81dfa4f-ddfa-37ad-9cfe-6857ff74fb20 | -7.17348 | -46.32401 | 2024-10-25 12:51:00 | TERRA_M-T | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 757100ac-df45-382a-bbf2-655eaa840f32 | -7.17197 | -46.33513 | 2024-10-25 12:51:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 73c15ca7-f2b2-3ea8-bec9-da167d86bf93 | -9.30801 | -46.16216 | 2024-10-25 12:51:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d3cf6369-6c7a-35fc-b02d-41ac41d3a446 | -9.30638 | -46.17448 | 2024-10-25 12:51:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| b1924c02-049f-32bc-ae58-073acf22fcff | -9.27193 | -46.21268 | 2024-10-25 12:51:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 33d6a7b3-c362-38a1-8981-8db1c0c65525 | -9.2703 | -46.22459 | 2024-10-25 12:51:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 97483cbf-2e53-3e3b-922d-d16165776aab | -9.14917 | -47.10145 | 2024-10-25 12:51:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 10fe0508-60af-3db2-bf1d-6419edced6da | -9.1477 | -47.11202 | 2024-10-25 12:51:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 438cf4ec-9755-349c-a79d-8393e754329e | -8.63052 | -46.95734 | 2024-10-25 12:51:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 18bdc39f-fab2-37a1-bf2f-1f92d7195e96 | -8.62799 | -46.95049 | 2024-10-25 12:51:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 602b4afb-a5a6-3720-a63c-b0f985f335d9 | -8.35808 | -46.62046 | 2024-10-25 12:51:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f6a80e9c-20f3-3a29-ac05-28590ba4b7ab | -9.49959 | -47.22765 | 2024-10-25 12:51:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 5960b698-806c-3f82-95fc-62e3ed32cd16 | -11.43135 | -47.68069 | 2024-10-25 12:51:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6fb53d3d-3a90-35a5-9cf3-3986a13c5f73 | -11.18847 | -47.51065 | 2024-10-25 12:51:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| cdc2a296-1ab9-37e5-8df3-2eb010be0111 | -6.52057 | -47.26109 | 2024-10-25 12:51:00 | TERRA_M-T | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| e3ff158f-f6d9-30b7-b804-808044e11a16 | -7.64022 | -47.15517 | 2024-10-25 12:51:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 1b657d97-3a8d-3ab1-9719-5777ab82bcbc | -7.12628 | -47.19777 | 2024-10-25 12:51:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 4c1ffcad-fa2d-33f3-90b3-4e0a623b4256 | -7.12493 | -47.20757 | 2024-10-25 12:51:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 52def2cb-26ac-336c-b5c7-344e88d9fb6e | -6.92817 | -46.84233 | 2024-10-25 12:51:00 | TERRA_M-T | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 84200271-0da0-3155-9e57-ad726cd16cb2 | -6.66851 | -47.06691 | 2024-10-25 12:51:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 58448653-5584-3f0e-913f-ce7abdf1e9d2 | -9.41291 | -47.84743 | 2024-10-25 12:51:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2e72ef9e-d095-3065-97dd-97c72b8c78c9 | -9.30759 | -48.26462 | 2024-10-25 12:51:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 5d93299b-3f1a-34d1-8127-120f41340108 | -9.29848 | -48.26337 | 2024-10-25 12:51:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| da9cd5bc-49c7-31b5-a08c-e3d23d778dba | -9.29716 | -48.27279 | 2024-10-25 12:51:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fa3a8eb1-dec3-3bd9-a972-95913b55c7c3 | -9.274 | -47.91196 | 2024-10-25 12:51:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a2c1ef7f-e26d-3d7c-a106-cbab50d2b7b4 | -9.26245 | -47.79063 | 2024-10-25 12:51:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f3ccc1e0-475d-320f-8ce6-ce95a84f09c1 | -9.25425 | -48.31841 | 2024-10-25 12:51:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 3dcfaf6c-cac3-342e-ad4b-6ab5ce9bac59 | -9.25292 | -48.32781 | 2024-10-25 12:51:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 4fb771d5-2eaf-3ff3-8c0b-35d0abe36fee | -9.09866 | -47.9839 | 2024-10-25 12:51:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ac1e5958-a02b-382f-a166-419f5d338335 | -9.07759 | -48.00055 | 2024-10-25 12:51:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| cd138ba5-1bef-3fa6-8081-36d7a3c98a2f | -9.07624 | -48.01016 | 2024-10-25 12:51:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 44d35683-a2a1-35bf-b30d-c1115fde01c2 | -9.06839 | -47.9993 | 2024-10-25 12:51:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 40a5680e-adf4-36bf-b8bd-b8093be7beca | -9.06705 | -48.00891 | 2024-10-25 12:51:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 92f8cfcc-5661-362c-a7d1-d427fa2446df | -9.00549 | -47.92529 | 2024-10-25 12:51:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f848e07b-24ea-372d-aedf-85c5fee3bba7 | -9.00414 | -47.93494 | 2024-10-25 12:51:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 0a0395eb-dd8e-3b95-9545-ed2f8898803f | -8.91023 | -48.53651 | 2024-10-25 12:51:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ba18412d-876f-3958-b686-234733db9340 | -9.94881 | -48.94394 | 2024-10-25 12:51:00 | TERRA_M-T | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 0451a46f-75e7-3ac2-9cd3-d8e1035608bd | -9.87066 | -47.72893 | 2024-10-25 12:51:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 49934f9f-10f1-3d80-a8d8-8d5c3f089412 | -9.84451 | -47.57019 | 2024-10-25 12:51:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 2b00e455-55e5-3528-8a1b-ac8ba70cee47 | -9.64279 | -47.9077 | 2024-10-25 12:51:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| a750145b-f3ee-35cc-ab13-a4c5d9e1c586 | -9.62963 | -47.86603 | 2024-10-25 12:51:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c10dd09b-22ba-357e-98b1-e365c386c084 | -9.62364 | -48.50594 | 2024-10-25 12:51:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 63a07530-7783-3db3-8ed4-2dc42d5df525 | -9.48924 | -47.82421 | 2024-10-25 12:51:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 01282e3a-79a7-3cad-a38c-702c8d872d8e | -10.90287 | -47.83166 | 2024-10-25 12:51:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f907d44e-c2f5-3eb5-b607-0c58d90a191b | -10.87291 | -47.80022 | 2024-10-25 12:51:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ed23a711-770d-3d4e-a401-0c9767cc7069 | -10.79421 | -48.4346 | 2024-10-25 12:51:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 6f542503-117a-373d-943e-c3d8b9460e7e | -10.79286 | -48.44421 | 2024-10-25 12:51:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 66027d48-f9c2-35e0-9025-1c2ae94cb55d | -10.69008 | -49.1074 | 2024-10-25 12:51:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 4c3897ba-ffaf-37d7-b8c7-46765f2a27a3 | -10.65277 | -47.92355 | 2024-10-25 12:51:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 49e07bb0-0764-3057-a64b-ad4fd58e833d | -10.50816 | -47.98218 | 2024-10-25 12:51:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d44c964f-3d6a-3618-8fe8-29b289934e1e | -10.33953 | -47.80356 | 2024-10-25 12:51:00 | TERRA_M-T | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ee83f2df-e09a-30fa-a4da-13eee81d3b27 | -10.17588 | -47.90788 | 2024-10-25 12:51:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| d91a71b3-eaa1-361b-861e-5f6b61f17539 | -11.2917 | -48.49209 | 2024-10-25 12:51:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 52a64c0f-6810-34ca-ba27-5d59a22b4c12 | -11.29035 | -48.50187 | 2024-10-25 12:51:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 78cd674c-4afa-3892-9f92-6a82978e3d4c | -11.28253 | -48.49063 | 2024-10-25 12:51:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 87e660fc-fa06-3a93-9820-3bab9b15c546 | -11.02007 | -48.27076 | 2024-10-25 12:51:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ca23691d-d248-34ad-b315-ef84c96ed2cb | -10.95026 | -48.04377 | 2024-10-25 12:51:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0d8c6370-2d51-3e58-aa3b-88c18296b155 | -10.94089 | -48.0427 | 2024-10-25 12:51:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e30bd3c4-e122-3263-aef3-a8f0221f0e84 | -10.93676 | -47.79443 | 2024-10-25 12:51:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3bfa3809-c04c-3b03-904d-5e5e6b3b8c55 | -4.93272 | -48.51055 | 2024-10-25 12:51:00 | TERRA_M-T | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 2ac2aeb8-e3f7-32c3-8c97-0e3cc8eb9e39 | -4.93145 | -48.51941 | 2024-10-25 12:51:00 | TERRA_M-T | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 5e9b04c1-a9d5-3565-8e16-bb7bd4371284 | -4.92259 | -48.51815 | 2024-10-25 12:51:00 | TERRA_M-T | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 88ef2744-92b2-39b5-ba1d-0bb5d10cfef8 | -4.57961 | -48.01302 | 2024-10-25 12:51:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b6a864c5-bd76-3ffa-9097-84a17327d648 | -4.25199 | -48.55439 | 2024-10-25 12:51:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 2421b48c-d69d-3dd5-a22a-9ef9014c1084 | -4.24715 | -48.33771 | 2024-10-25 12:51:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| bb00c33f-9b2d-3a7c-97d6-c020b03816c2 | -6.28756 | -49.01954 | 2024-10-25 12:51:00 | TERRA_M-T | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 913b677b-5827-3a50-99c2-63a67db7f835 | -6.28628 | -49.02838 | 2024-10-25 12:51:00 | TERRA_M-T | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8f8d535d-567e-308f-8c0f-6498c36570c4 | -5.82384 | -48.20928 | 2024-10-25 12:51:00 | TERRA_M-T | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f34d37ae-b2d0-3723-82fe-dc73303e10c1 | -5.21362 | -48.2179 | 2024-10-25 12:51:00 | TERRA_M-T | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 262c9723-722d-3a26-958a-496dd877423a | -5.20472 | -48.21666 | 2024-10-25 12:51:00 | TERRA_M-T | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 508fd4ab-759b-38ee-8756-2b0c93d4202d | -7.84587 | -48.95577 | 2024-10-25 12:51:00 | TERRA_M-T | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3ef33cbb-829d-3e80-97b9-d7a1254f9cb2 | -7.84458 | -48.9647 | 2024-10-25 12:51:00 | TERRA_M-T | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 24.8 |


[Clique aqui para ver as próximas entradas](README116.md)
