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
| 1ad6530f-8972-3e2b-9329-dbb84d0623d0 | -7.26074 | -46.05438 | 2024-10-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d52d74e9-5c89-3a55-b98b-b5a07d94618d | -7.26009 | -46.05838 | 2024-10-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9367245a-2527-3354-b0d0-ecea5077f4a7 | -7.21685 | -45.58594 | 2024-10-25 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a6ceae60-64e3-327a-9ed3-ec55069de76d | -7.21623 | -45.58979 | 2024-10-25 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6322e843-3c46-32a6-84ae-e9ccfe994ecb | -7.21338 | -45.58541 | 2024-10-25 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4cf248af-d8d4-300f-a164-865b4eabf672 | -7.0496 | -46.32117 | 2024-10-25 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bd84bbe-16a4-38ea-9e6b-d0516383d55d | -7.04601 | -46.3206 | 2024-10-25 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b20db8c-df48-3875-bf6d-76975435b3da | -7.0236 | -46.12893 | 2024-10-25 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5efca04-379d-358b-a6e6-7c140217cf6b | -7.01572 | -46.42763 | 2024-10-25 04:14:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7e9c29c-6cba-32fd-8e34-c89e3a1d3a92 | -7.01505 | -46.43181 | 2024-10-25 04:14:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3fe0db1-dee5-3faf-9da2-6c375a4019c4 | -7.01299 | -46.43028 | 2024-10-25 04:14:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c9d188ae-5d9f-341c-8abe-4a8550126b59 | -7.01144 | -46.43122 | 2024-10-25 04:14:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00bcaddc-c14f-3394-8a11-7e4faf7bc22e | -7.89398 | -46.73116 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccf689c1-ee7d-326e-9317-282c4bb717bb | -7.01129 | -46.04802 | 2024-10-25 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fbcd3574-86ab-38a6-b2c5-47e5b5c5a6b9 | -6.99928 | -45.98848 | 2024-10-25 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac10a0b7-bf21-39ad-9a29-f867d85dd3c2 | -6.96153 | -46.32914 | 2024-10-25 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 919f1ff0-7626-34eb-bd97-fba8fe7d76ad | -6.85088 | -45.89578 | 2024-10-25 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e176643d-7cf0-3538-a616-9765d060f1ca | -6.85021 | -45.89992 | 2024-10-25 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 368b55e9-ec9c-3076-89d0-41d9da14cbd0 | -6.77518 | -46.24961 | 2024-10-25 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa6fe5bd-22d3-374d-a284-2c191756ef5c | -6.77254 | -45.50769 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4737233f-d36b-3105-b21f-17cf7ae699f0 | -6.7688 | -45.53073 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11c75d4b-5d71-3a7e-aaba-bb6565dd512f | -6.7618 | -45.48626 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2153ffca-e538-3fae-a78a-d02a1b8132f1 | -8.40547 | -46.61961 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a166827-953d-3818-8cac-1a7ed44e3d90 | -8.40256 | -46.61499 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5964092-7f8d-3bd0-b418-2fc836e8293d | -8.3587 | -46.62177 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0886bfec-3dcd-312a-8302-58c6f73ce7a4 | -8.35803 | -46.62589 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1363c945-110f-324a-bbbb-bb4732ae817b | -8.34463 | -46.33068 | 2024-10-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 024de5f7-69f0-3a28-a9f0-ed87347b979e | -7.9206 | -46.43543 | 2024-10-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51c13641-7807-3c56-a59a-7823c711db95 | -7.89441 | -46.68342 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7a082249-8e8a-3153-a32f-e3ce11a1e9c9 | -7.89372 | -46.68763 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 579c5e72-a04c-3ddc-837c-4c27347c1ab8 | -7.86492 | -46.88457 | 2024-10-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95bdbf88-a196-399c-9cc7-dbba14419f0d | -1.49622 | -46.78944 | 2024-10-25 04:14:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22f0d705-ff59-3246-a693-e23177d3d1d1 | -3.30463 | -47.02621 | 2024-10-25 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55145ac6-ee94-3d0f-a825-3fe098cc6a25 | -3.21208 | -46.80088 | 2024-10-25 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 46903e33-cf2d-30ad-8c07-936fec22e920 | -3.2113 | -46.80574 | 2024-10-25 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 1d1d54fe-e97a-3788-a9eb-1db39e4b6a5a | -3.20741 | -46.80515 | 2024-10-25 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 4764fd08-ccc5-3c70-becb-10df2b6ffcc7 | -3.20432 | -46.79966 | 2024-10-25 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5ad8d375-1cbe-3258-a4c7-aa4f8384f2fd | -3.20353 | -46.80455 | 2024-10-25 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 71b50eaa-4dc0-36f2-b62a-b2933bdc5299 | -2.95897 | -47.36481 | 2024-10-25 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05ae1242-7e93-3014-8227-c486394bf3aa | -2.57179 | -47.25176 | 2024-10-25 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a1d617d2-a2ca-35c1-80b0-dabda1c5f032 | -2.57122 | -47.25529 | 2024-10-25 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0a19f0ef-bf20-338d-af5f-b12f1aa9d15c | -2.48456 | -47.27328 | 2024-10-25 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a07208af-136a-327d-b71f-d120ef16b9f3 | -3.18869 | -46.17249 | 2024-10-25 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 965bb92d-f200-3086-bfa8-b2da12dd1142 | -2.73591 | -45.99795 | 2024-10-25 04:14:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef6ac760-4b7d-3476-aac2-c22a4f385e4c | -2.61 | -46.12642 | 2024-10-25 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e667e7ed-c709-3b4c-baef-85aab9873a5a | -2.60927 | -46.13091 | 2024-10-25 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9221a515-42b0-3107-85cd-33337332ec27 | -2.60854 | -46.13543 | 2024-10-25 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3df1ac77-8b19-3f5b-8e6c-2f1981d045ba | -2.46838 | -46.08511 | 2024-10-25 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ca02b5f-eee2-3a0e-94ac-eb03b0d5aa78 | -2.31621 | -46.23647 | 2024-10-25 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d9150af-c15e-3a33-8b2d-95bd4712fbf7 | -2.31242 | -46.23587 | 2024-10-25 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e5cbf03-007c-35c0-be0c-e26b0f60326f | -3.41797 | -46.36337 | 2024-10-25 04:14:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3830e7b2-78a4-34a1-8364-a5f27a320c68 | -3.60542 | -47.25976 | 2024-10-25 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| afb73882-54e9-335e-914a-0f12de14532f | -3.60489 | -47.26312 | 2024-10-25 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4f4129b-f79c-387b-96b2-1f710b0b8a78 | -3.60433 | -47.26661 | 2024-10-25 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bd53e0ee-ac9a-31d7-9770-778bae23a642 | -3.60426 | -47.25922 | 2024-10-25 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bd0c2edb-2bec-30ce-a0a0-21bedb8bbcee | -3.60145 | -47.25919 | 2024-10-25 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af29a79c-1a92-3c4c-996e-eaf51777b68a | -3.60091 | -47.26253 | 2024-10-25 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fad5c5a7-30fa-399c-aec8-b06a61dca2b6 | -3.60036 | -47.26596 | 2024-10-25 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aec64160-4740-32fd-a929-728599a66acb | -3.54844 | -47.36014 | 2024-10-25 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c0e7394-a10a-3209-bb81-04f1e1bbe6a6 | -3.54444 | -47.35951 | 2024-10-25 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 162cf1f5-d0c7-3bc6-9b1b-408501b6b1e0 | -4.77695 | -46.41866 | 2024-10-25 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 15c6f8c5-bc63-3ae9-98c3-2a8055245e48 | -4.77322 | -46.41815 | 2024-10-25 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fbeb4eba-637b-3357-b734-b9a61c75e749 | -4.7725 | -46.42258 | 2024-10-25 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 387ce197-cf72-34cf-ba2b-02e464e1696d | -4.76878 | -46.42204 | 2024-10-25 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 42b5c44f-5de4-3e1c-8190-3377153babee | -3.97639 | -46.39117 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d96780cc-6768-3731-a7fb-84d1eaa093b2 | -3.96095 | -46.41584 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7125acb-0cfb-3097-80e6-467f423357ac | -3.95804 | -46.43414 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 678d9675-f366-3a84-813d-321802bf4a30 | -3.95721 | -46.4152 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f48c4454-60eb-3f81-916f-344b20965212 | -3.95501 | -46.42901 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 2ae21be4-7935-3bc3-a4ca-89a5d28d5162 | -3.9543 | -46.43345 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 70a7242e-bd24-3bae-8e7c-30bae7455b00 | -3.9536 | -46.4379 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a9758b0d-7ff8-393e-b7e9-3129f6950376 | -3.95346 | -46.41457 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f2dd182-27f9-3349-bec2-32c44c506d1a | -3.95127 | -46.42833 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 0c52ee32-dd26-375a-891a-cd528b4c6cce | -3.95056 | -46.43279 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 16feefde-a077-3f1b-b333-891cfa3f7d7f | -3.94985 | -46.43724 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f4fc86b3-b019-3c4a-a1d2-15f68da9b1b7 | -3.94754 | -46.42762 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2f148295-52e3-30a2-9ea6-12279daf6867 | -3.94682 | -46.43212 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e86554b4-4c01-3795-8d62-a0451f8c4317 | -3.9461 | -46.43661 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7eb953db-3bc8-3eb4-a2d0-e9f1db8aac14 | -3.94379 | -46.42698 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8f970b58-e956-3f1f-95ee-fa833c806d6e | -3.94319 | -46.45489 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b959361-ea7e-3248-947b-ab6fe1a83aad | -3.94307 | -46.43149 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bc5e6487-9267-36a6-a238-65cf2e729c98 | -3.94235 | -46.43602 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21c0ee01-7725-31c0-a01e-1f66afc15c02 | -3.94004 | -46.42638 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d1eaaa4-e981-3d3f-b7b1-247006a745b2 | -3.93932 | -46.43087 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51678de3-2efb-3a89-822a-4badb5dc18c7 | -3.93859 | -46.43541 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c41a0ef1-0246-3fb0-a43e-53bc279943aa | -3.93628 | -46.42581 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3dcd1d7-a4c8-3ed3-8242-5a6bdb7b4694 | -3.93556 | -46.4303 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b41717dc-07c4-39ca-8e5f-fc7c62efac41 | -3.86283 | -46.64063 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63b5b794-27f0-316b-9086-d23a016e7437 | -3.85901 | -46.64008 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f6f0b3c-6ee0-3478-8342-6bc5c740acaa | -3.85516 | -46.45058 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68d38211-5256-381f-bacb-baf6bc948659 | -3.85442 | -46.45506 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e4a143f-9bef-3c63-ad3d-4367fec156a1 | -3.8541 | -46.45244 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c00a2037-61e5-3b03-90fa-9e7fa24c6284 | -3.8534 | -46.45687 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 164a4ec0-c0e7-3a97-aad8-d3eefc4d716a | -3.84832 | -46.48899 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8eaa020-ae05-35e0-8af3-e7210075fdc3 | -3.83094 | -46.47668 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f76a0737-b375-3f82-9240-b0d8aa35d889 | -5.01422 | -46.48556 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d7fd8e4-6f4c-3a8d-ba26-99cb80920d82 | -5.0135 | -46.49002 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d3646f7-457e-3865-b6e6-8f7aebf8a2d1 | -4.99643 | -46.47785 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c3ff70e-ff94-3c02-8a00-f1e9d6a4d1ec | -4.989 | -46.47672 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4aba1d0f-81e8-3de4-a917-e73cc99ddc68 | -4.98457 | -46.48051 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README29.md)
