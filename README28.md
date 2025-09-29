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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec4bcf74-6786-3234-8f41-e1f1c66d722c | -6.08457 | -42.45319 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 39e77235-c4e5-381a-a3f4-45428667a2cf | -6.09746 | -42.65224 | 2025-09-29 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8f799c92-d11c-3062-bc49-eb1677eaf679 | -5.50822 | -42.74281 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 91204c05-6825-3a59-a25e-cd4c6a34e734 | -7.74195 | -46.99461 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7d6c98cd-9ee8-3d90-a9e7-187ed17b1fdf | -8.27163 | -45.50126 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 94fdac54-a21b-3480-b262-fd15e622fac2 | -5.85034 | -45.95186 | 2025-09-29 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a729d3db-b946-3948-9622-721536ea3cdd | -6.77128 | -45.61509 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2b3b3b3-fce6-36c2-9062-25a3c9ae81a7 | -6.46449 | -44.00474 | 2025-09-29 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2982ac1e-5698-3b43-a65f-c64458593a31 | -6.50277 | -44.12403 | 2025-09-29 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b556d9e-b555-3247-a7ad-9979d938bec6 | -6.46539 | -44.22016 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a906404c-b9c9-3c7b-91a7-e39fb7663703 | -5.75256 | -42.87845 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f833e114-4d7c-3def-9aa3-98d70f083d1c | -5.75425 | -42.54285 | 2025-09-29 04:06:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b25030e3-7b7b-3857-9771-e30620008164 | -7.13642 | -45.49633 | 2025-09-29 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b8c04dc-216e-3b0e-9389-6e80dbfee85a | -6.11866 | -43.48154 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70d6dd97-1792-34eb-a23b-a154f5dc30b7 | -4.24802 | -46.95133 | 2025-09-29 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| da8dadd1-5f54-32e3-b802-f607ca63f5e9 | -5.21629 | -43.76898 | 2025-09-29 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a7269ae-9744-36c2-9d88-5c43980d6d73 | -7.46127 | -46.30063 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0238c0b-a9e1-3ac3-84f9-c277cd6a1c40 | -6.61518 | -45.9001 | 2025-09-29 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cbcc525-f3fc-364a-b4e6-eda8288534c3 | -7.73813 | -46.96778 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b032646-8537-3de0-8486-98886fbe40bf | -6.48599 | -44.51063 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4560b63a-17c7-3e6d-bc16-dbaa517d27bc | -4.28983 | -48.27332 | 2025-09-29 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 773b50ad-1826-3336-bcb7-2a0e1500436d | -5.32575 | -42.76299 | 2025-09-29 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a27d34ba-4062-31f6-8ad6-f20d5d1d869c | -7.58522 | -44.7731 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad743be4-ce2b-3155-8c1d-186de07ee1ab | -7.74604 | -46.99526 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0ebe49a-62e3-3522-9a8e-f250fd2b1327 | -5.72114 | -42.83601 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c9c56478-cc57-3f85-9bfa-d1b01f622bbb | -6.46655 | -43.94845 | 2025-09-29 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9a67729-d9e9-3f94-a0a9-155655b2ed95 | -2.96413 | -40.83707 | 2025-09-29 04:06:00 | NOAA-20 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2d6558be-e539-3484-ae8d-ec8419585c09 | -7.72971 | -44.79059 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7ba56a6-e1fb-358c-8e35-8b82144e2373 | -6.11139 | -43.46108 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6de3f0a0-429e-3355-9168-1a7ef20bf8a6 | -6.57684 | -43.4039 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c848f68b-7de9-37a1-9daa-d1b787a9a626 | -6.5255 | -45.17859 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 005efbf1-2c97-33d8-9e73-e35cfdc52303 | -4.44229 | -40.98526 | 2025-09-29 04:06:00 | NOAA-20 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bbefd5ac-7a99-3356-a83d-c75c0f3764b5 | -6.58076 | -45.09689 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8b744d6-6802-3e3a-a0a0-332b9746662b | -5.52199 | -43.87182 | 2025-09-29 04:06:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 54599480-3f25-3058-9b38-7358f7125d16 | -6.4667 | -44.01321 | 2025-09-29 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f739b3ea-a64d-355b-a154-39d4eab727a5 | -8.00529 | -47.04364 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f5df187-6811-321b-9d15-ad871a871a62 | -6.62173 | -44.96056 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8bceb2c0-8b8f-3edd-8d8e-ae09a5d71710 | -7.89697 | -44.59431 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d9722cb5-9b7d-31eb-b77a-5337e6dcf990 | -5.74926 | -42.85548 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4d11a64b-7a05-39e9-8809-09424f8c6b68 | -7.22243 | -44.79411 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 96bc73ab-f20c-35a5-bb55-0e8b651451e2 | -6.74242 | -43.37727 | 2025-09-29 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 093ccbe0-d8c3-3b99-9c74-297b05d60697 | -2.91291 | -48.19766 | 2025-09-29 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bd8f298-b27e-36a8-8f5c-a3c3eb3ea858 | -4.94141 | -45.58932 | 2025-09-29 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ca557bf5-9b53-3a1c-9019-fc539eabeffe | -6.36519 | -43.92476 | 2025-09-29 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cb854065-c2c7-3027-a355-dc9481cf3f8a | -3.34421 | -49.22826 | 2025-09-29 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a2eeed42-ea77-3ba6-a41f-cd8e23215ca3 | -6.11826 | -43.46228 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e05144d1-3389-3c9d-a142-4e1d21a65654 | -3.44942 | -49.2756 | 2025-09-29 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a63366be-5a9b-3064-9889-e72f6e726285 | -5.82578 | -42.79706 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7e3f883a-8442-3370-b8e2-a5dc231476ed | -6.09872 | -44.4908 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02a10172-9e0c-3a37-bf76-490a1d759015 | -5.03138 | -42.54235 | 2025-09-29 04:06:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9f0fda71-abe3-3d70-ba76-8bf93d432564 | -7.5709 | -42.40211 | 2025-09-29 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7a669bf4-b3d6-3eba-a608-ab64505ed2ea | -8.27309 | -45.49234 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ed65373-6b95-3e96-802b-9812114e6bd9 | -5.80352 | -42.84936 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d1ef14d8-3ba4-3646-950a-ba8b1f97594b | -6.48718 | -44.26523 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42e2ca9c-d795-3e50-81a6-8f0e81140acb | -4.54292 | -41.01553 | 2025-09-29 04:06:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f8a12c2d-c97b-3ed1-bd45-dc9125e05e64 | -8.01095 | -47.03176 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 925da7b4-599a-3955-9379-96863fcf27a0 | -6.53751 | -43.82087 | 2025-09-29 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d83f5976-6fad-3b5c-b11b-d8fdfecf6176 | -6.70644 | -44.60412 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 627fd7fe-76c2-3150-a320-fe75e5588ccc | -3.94123 | -49.13152 | 2025-09-29 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b8b43fc-56bb-31b1-8eb1-3d871e9bc8c9 | -8.29129 | -45.48757 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50503454-ace1-312c-90ca-9cd97fe816cc | -6.62135 | -44.95876 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9406d98a-78f1-36a3-85a6-1915fb72e921 | -7.2159 | -44.78874 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5964f59f-0fc6-37d8-a4ed-ca7ed68a9a14 | -7.46685 | -46.29127 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5ad7f6a-8e5a-33f9-a73f-28b5b9a0a732 | -6.11298 | -41.82668 | 2025-09-29 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 52214a60-9e3b-3d94-8910-9b7c13ecefec | -6.61273 | -45.91479 | 2025-09-29 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 716a0d4e-d667-3aad-bd85-334c4fd74570 | -4.56887 | -37.85165 | 2025-09-29 04:06:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 08d0a605-dfa7-383d-bbec-d39a886f2a2b | -7.37143 | -47.03407 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a95e44ee-4f1a-31a8-a915-380a71eda31f | -5.50219 | -44.01537 | 2025-09-29 04:06:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8a9fa780-1671-3b7d-a526-274dabfc90af | -5.82241 | -42.79651 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dfaff221-21a1-394a-a057-641612eefb2e | -5.78592 | -42.64676 | 2025-09-29 04:06:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c9094f50-506d-3265-9f65-355bc65eb62b | -5.85514 | -40.92165 | 2025-09-29 04:06:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 715479c0-1591-395a-b2ae-7ed1229bb5d5 | -7.43634 | -43.03108 | 2025-09-29 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6657b2ba-14ba-3fce-9d62-870c0b8e5dd3 | -6.43584 | -42.82386 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 77918939-96e7-31c3-803b-a7f090d4e913 | -5.81775 | -42.82555 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 77dc2687-684c-3d3c-9ec5-c110078a4cd1 | -7.21935 | -44.76793 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 795f34d4-f0cd-3011-94dc-b2962b327db4 | -6.27271 | -44.06829 | 2025-09-29 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02c7d001-7f69-3e29-a622-7241af0dc4a5 | -6.23906 | -44.47815 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 081e1fdf-6b61-3d0f-b7fe-f9d1e5e1e89b | -6.82737 | -44.8241 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6889d0ee-a6aa-3241-8e19-5fd836e6aac3 | -7.85117 | -44.58793 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eeb0e75b-2490-3814-a612-5b41474d3c0c | -7.80434 | -46.89736 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ae60e085-2c96-375f-8337-3e559ec644dc | -6.09803 | -42.64868 | 2025-09-29 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d278bf7c-9d0f-31ec-bba4-851a909bb9bb | -7.2166 | -44.78455 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d2bc717-c3c4-344f-9db7-7c9c454fc82b | -5.74134 | -42.86167 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9ce27227-cb48-39ce-9513-3b194a1bc9bd | -6.03689 | -44.15917 | 2025-09-29 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c27a240e-17c8-3727-a430-ecabedfdcdb3 | -6.05554 | -42.46306 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 72ca2279-deaf-36c4-9645-dd86b865474f | -2.576 | -48.40386 | 2025-09-29 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f60d5846-7e78-38cc-ad57-5e2c9bd44c3b | -3.3075 | -51.6752 | 2025-09-29 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ba88bd5-b93c-3721-a752-9b4e542b0e28 | -4.50444 | -40.71973 | 2025-09-29 04:06:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 08a208eb-5a74-3b78-a4c4-94e98de8d15a | -7.14017 | -45.49696 | 2025-09-29 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd8b468f-583c-32d2-849c-3a99bba31844 | -6.7402 | -43.36925 | 2025-09-29 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 396321f5-5fd7-3e14-8e65-b624cb316f63 | -5.56696 | -42.1613 | 2025-09-29 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aaa48305-a441-3e02-b0bb-ed22f1a721b7 | -4.30542 | -48.09335 | 2025-09-29 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7f2d3fe-2279-3a06-a274-85b3b67ff4a6 | -6.1296 | -43.47948 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 54db12f9-61ea-32b4-bd0f-8d75ffbd4900 | -6.71504 | -44.59676 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d33b74b6-ee52-311a-be59-937581de0e1d | -7.286 | -42.82684 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 494f3da5-c254-3a79-9e07-1e8b4c4851ef | -5.74041 | -42.6724 | 2025-09-29 04:06:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 89f366ab-0d29-37cc-8101-ca8cb6500a13 | -7.15519 | -45.49942 | 2025-09-29 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe771f16-9eca-3282-8f54-fcd591a498e4 | -3.10029 | -47.01345 | 2025-09-29 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| d23d106d-7d64-3ceb-9f10-39df99fd35c4 | -7.88568 | -44.59644 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 917fc23c-05a1-3452-961d-75e7dde762eb | -7.58052 | -44.80172 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README29.md)
