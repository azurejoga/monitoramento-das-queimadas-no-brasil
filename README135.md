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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a0160ab-9699-329e-a734-7506c1a395b4 | -10.5908 | -53.9713 | 2026-09-22 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 53e8d5a2-9b74-3aa2-b9c6-8ecb7d52cc57 | -9.8858 | -45.8669 | 2026-09-22 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| e0ed2b53-8354-34b2-8873-9bbf45900f9f | -2.9525 | -57.72 | 2026-09-22 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 48fca9d8-6038-341a-9650-a3dcefb89b14 | -14.6492 | -45.66 | 2026-09-22 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 96ffcf06-f2a2-3a8d-9209-b82e89a65325 | -12.1458 | -47.3974 | 2026-09-22 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 166.7 |
| fc093e91-f256-3bf8-a9fb-afe12a8dc241 | -11.7079 | -50.9811 | 2026-09-22 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.9 |
| ca28d6ca-17d4-3f26-a79d-a9ff3778a99d | -10.7437 | -50.8089 | 2026-09-22 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| b3fdd660-7148-3305-8324-20503e1be1ca | -6.2761 | -47.6287 | 2026-09-22 14:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| d3d2267c-8372-389f-a6ce-3f64c1b0cacb | -3.4009 | -61.0629 | 2026-09-22 14:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| c1a59a27-1305-3fa4-ad48-816ae4e1ba68 | -7.4883 | -46.1165 | 2026-09-22 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 2b2c698e-0ce9-3a77-b629-5ffcfcde84f7 | -13.2983 | -51.7713 | 2026-09-22 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 1728919d-3ce5-3e00-9ae6-7a66af804045 | 4.0425 | -60.4812 | 2026-09-22 14:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 74.7 |
| b3258b47-ec0b-3f09-81cc-802e43a8de11 | -3.3492 | -59.867 | 2026-09-22 14:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 9d0f07d2-9a35-3109-b070-5ef489e6b38e | -2.8791 | -57.8184 | 2026-09-22 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 22b9d083-21dc-3eb0-96bd-4eebe6001680 | -8.6507 | -62.4966 | 2026-09-22 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a86607f4-601c-3bca-b126-f6cac7f3d661 | -10.8858 | -56.196 | 2026-09-22 14:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| b9340b29-d836-327e-8def-dc9e862d23d0 | -7.822 | -61.8084 | 2026-09-22 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 1c570b72-8d97-3e22-9513-e0dd90a6cd06 | -11.1183 | -54.0062 | 2026-09-22 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 07bd1943-80a8-33c2-a7b0-999d5b41de10 | -7.2994 | -59.5343 | 2026-09-22 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 66031d30-0a73-3c9e-bf1c-5151e0c39b75 | -10.6875 | -50.7722 | 2026-09-22 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| c7cb31d0-1d47-3d42-ad48-ca96ab252af0 | -7.5247 | -46.2252 | 2026-09-22 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 50fa3bf6-c1ca-3eba-95ca-4b1313558ed4 | -6.2946 | -47.6493 | 2026-09-22 14:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| f914e54e-7522-3815-b026-bd8f59c32a16 | -5.1439 | -55.9543 | 2026-09-22 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ae2a31bb-ba1e-31a8-8d8b-2d3b6ce7db13 | -11.7675 | -50.804 | 2026-09-22 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 60a3de32-dc48-3655-ad23-cec3fa1c55c2 | -12.6799 | -50.9526 | 2026-09-22 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 136.1 |
| fa5fdd7d-e7bf-3266-8777-b84e03f0c3bd | -8.8105 | -44.2757 | 2026-09-22 14:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 072353bd-52ed-3720-80e4-0d74db687220 | -12.3484 | -50.1779 | 2026-09-22 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 198.1 |
| ef0f8029-dea8-3729-a3d7-b36f4a50ef82 | -11.3925 | -46.7598 | 2026-09-22 14:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 419.7 |
| fdf045d5-c99a-3024-989f-b6eeaa476d3d | -9.3871 | -47.7526 | 2026-09-22 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 13fab148-f3db-3b81-a70a-a1cf806e93b4 | -3.3183 | -57.8677 | 2026-09-22 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| c07dff1d-2aba-3d1e-bb29-b98fae4d643e | -3.2899 | -42.6683 | 2026-09-22 14:10:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| a0180a0e-7953-30d5-9ef5-472297c20acf | -7.1555 | -47.4751 | 2026-09-22 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 71a45035-be7b-335b-87d3-a34ba2da5e9f | -9.9058 | -48.4867 | 2026-09-22 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 03ffcc93-6301-3337-9ebc-b2b27bc01244 | -11.6017 | -46.7993 | 2026-09-22 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 17df5a72-7107-3688-a087-eb93b3b2441b | -6.7989 | -43.9008 | 2026-09-22 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| bb0e4408-8077-300c-9065-7e045e7be9e9 | -5.5717 | -42.7414 | 2026-09-22 14:10:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| c56f2bd6-dd4e-3b76-b0de-547f315c670a | -9.2759 | -46.1852 | 2026-09-22 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 193.2 |
| 2537e3d9-2ba5-3569-926a-5c0e1f81d171 | -3.405 | -59.522 | 2026-09-22 14:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 164.1 |
| 87983fb4-44c5-3129-9e42-e50b13d3af9f | -5.9985 | -45.2476 | 2026-09-22 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| cc999f9d-1ecc-3415-81e0-572cb7be2781 | -2.934 | -57.8174 | 2026-09-22 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| a41c8a1d-c53b-3174-a3b1-d378b199bf5e | -8.6136 | -62.4981 | 2026-09-22 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| c163112c-cbec-3563-884d-5ab1e3e68222 | -13.2033 | -51.7193 | 2026-09-22 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| eb18f4bb-6bdf-3b1b-887b-07f356291524 | -12.0833 | -50.0594 | 2026-09-22 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 24888b7c-20b8-3a1d-95d0-f0706d2e8a96 | -7.0352 | -44.6396 | 2026-09-22 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 2d54bbe0-a184-3fd9-a7ae-92c6aa255786 | -3.3001 | -57.8487 | 2026-09-22 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| b73d684a-ed79-3e4d-a55b-113ca105f869 | -8.7729 | -44.2568 | 2026-09-22 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| a92386c9-1049-3f67-bf1f-1e3759b9eba0 | -2.934 | -57.798 | 2026-09-22 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 172.3 |
| 0c1c406e-644c-3634-acdd-fc19069756db | -6.3198 | -59.9572 | 2026-09-22 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 97dd86b1-8dba-3edb-8b11-87815f85f941 | -8.7916 | -44.2778 | 2026-09-22 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 224.1 |
| bf621588-fbf1-33cc-9b44-c6770b84b407 | -3.2818 | -57.8491 | 2026-09-22 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 91580c92-dd1a-30eb-ac38-9634879fcc9b | -3.4049 | -59.5794 | 2026-09-22 14:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 4b11d95b-2ce3-3560-b816-920e1ad84710 | -7.1745 | -47.4517 | 2026-09-22 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| adc95488-657e-3e13-83bd-dab4dc767194 | -13.3171 | -51.7902 | 2026-09-22 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 4193002c-607b-3854-ab0f-320f0104a052 | -6.1651 | -47.5271 | 2026-09-22 14:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 1973486c-0581-391a-961e-3e945943942d | -6.1653 | -47.5052 | 2026-09-22 14:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 25d6793d-c318-3a36-b65f-d2b060675bc5 | -6.2165 | -45.9518 | 2026-09-22 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 010dd3ba-391a-320b-9bda-c6586b97e477 | -8.6135 | -62.5171 | 2026-09-22 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 36b34de6-0d6b-3f1d-aba8-fd3b09f3a78a | -8.7912 | -44.301 | 2026-09-22 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 102fe98a-f0e2-3c1c-8439-28caf85f9b7d | -5.9333 | -59.9899 | 2026-09-22 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 24eab75a-a039-30a8-a2f8-264d50832568 | -12.3293 | -50.1802 | 2026-09-22 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 33a741b0-2934-36ee-8ee7-ce974dc91660 | -11.269 | -54.0334 | 2026-09-22 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 6b99f349-c894-39ed-b832-beafe6c4fe8a | -12.7995 | -44.2308 | 2026-09-22 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 906a4307-f44a-3156-bfe4-7fc92c3b48da | -11.6793 | -43.4684 | 2026-09-22 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 8f8414d8-08a8-341d-aaa9-b2355641d67b | -8.4797 | -57.6282 | 2026-09-22 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 30378ddc-afa3-33af-a9f1-9c8c70a88de1 | -9.9064 | -48.443 | 2026-09-22 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 15a07e2e-a54c-34c8-a16c-aa75e6018974 | -11.71 | -50.98 | 2026-09-22 14:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e53b97f8-a4c8-3655-b351-67379859b23c | -6.64 | -59.9 | 2026-09-22 14:15:00 | MSG-03 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63b87a51-1118-35b7-bbc6-10a9c3f0467c | -9.8665 | -45.8918 | 2026-09-22 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 8f349d6c-362b-343c-a553-bbe8ddbad07d | -10.6878 | -50.751 | 2026-09-22 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 157.3 |
| e62db25b-3f66-34b5-951b-13e914685fe1 | -12.4208 | -47.0002 | 2026-09-22 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 0bb2d496-e6f8-39c1-92e2-12efbde9e004 | -11.6793 | -43.4684 | 2026-09-22 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 68ed0763-38b3-33bf-8122-2ae696c707fa | -5.8675 | -49.7864 | 2026-09-22 14:20:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 651d58c7-fa23-3fb9-bcf3-b8ef91f0155b | -10.4539 | -51.3038 | 2026-09-22 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 825486ad-2e01-3205-a578-c1136522f58a | -5.1439 | -55.9543 | 2026-09-22 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a2befdf5-ffb0-361c-8801-26b3bcdbe6f4 | -9.8676 | -54.8249 | 2026-09-22 14:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 43f9008d-d39c-3fa0-a4f7-1cb3380f7a87 | -3.2712 | -42.6692 | 2026-09-22 14:20:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d1be3ba0-fe83-3912-81af-bc9909a243a2 | -6.9414 | -42.907 | 2026-09-22 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 155.0 |
| b411322d-93ca-31c2-8379-b3b5707671e4 | -9.2762 | -46.1627 | 2026-09-22 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 432.1 |
| 763952d0-b8d6-3eed-b57f-19bba1f56625 | -6.9416 | -42.8834 | 2026-09-22 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.2 |
| 25337180-9b1a-34f7-b4f5-d1ec61716dd6 | -3.3 | -57.8681 | 2026-09-22 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 4acba0f1-192c-39e3-922d-d332354fd2c0 | -2.9525 | -57.72 | 2026-09-22 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 5ddd33c3-a72c-3d22-95d7-3c55929fd926 | -6.0925 | -57.6847 | 2026-09-22 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 176.3 |
| 4b73b160-ff0a-389b-b11c-8f304071508f | -12.8056 | -54.0462 | 2026-09-22 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 11f3b24e-4499-30cb-a7c8-8bd77f40d07c | -3.7364 | -58.8626 | 2026-09-22 14:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 986fe7da-d7d7-3e48-95a3-23628e0374cf | -10.4541 | -51.2827 | 2026-09-22 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 7538fbb1-7c95-33a8-9a63-46a41f793a7f | -10.6881 | -50.7297 | 2026-09-22 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |
| bb90d4de-dd83-31d5-84cb-495ecf540149 | -9.977 | -50.248 | 2026-09-22 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 793336b4-78b9-39bd-a2bf-c419f9f9866d | -6.9683 | -47.4899 | 2026-09-22 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| fdb3a787-76ae-3a93-bf73-0ce23a3d9011 | -6.1111 | -57.6645 | 2026-09-22 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| a8bfc934-caec-3f96-9088-fd3d0a99db0e | -2.8534 | -60.9206 | 2026-09-22 14:20:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| d2a199fe-0686-33de-af62-9959416522f7 | -5.8676 | -49.7651 | 2026-09-22 14:20:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 82d41d3a-0a0d-34d0-8b6f-673e3037e036 | -10.8858 | -56.196 | 2026-09-22 14:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 7dd95d6b-952c-384e-8218-1c9cfc1a67f1 | -5.9334 | -59.9707 | 2026-09-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 638a3c28-0c40-32d1-9a01-32f1767e221d | -9.152 | -50.0066 | 2026-09-22 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 9d431858-c843-3da7-a50b-f65184e6827a | -8.4983 | -57.6271 | 2026-09-22 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 1faee498-6709-3895-bc2c-d614fe411410 | -11.0052 | -53.996 | 2026-09-22 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 97516c47-f007-3c02-8e60-bacfeffc0044 | -11.3232 | -51.3414 | 2026-09-22 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| c9c608ae-fd13-3200-b461-312503ef364e | -4.6589 | -42.0726 | 2026-09-22 14:20:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 125.4 |
| dc1b812e-5f38-3aa1-864a-908185f4c6e3 | -6.3198 | -59.9572 | 2026-09-22 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| bebaebaa-031a-3bdc-bfbc-5eddae11bbac | -3.6452 | -58.7685 | 2026-09-22 14:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |


[Clique aqui para ver as próximas entradas](README136.md)
