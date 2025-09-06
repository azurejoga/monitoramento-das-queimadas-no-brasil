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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4651ef55-a3d8-35db-90b1-d368b28cf6ab | -6.2385 | -42.58776 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ce225368-33e8-346e-8522-0a45a45fed42 | -6.51517 | -43.57812 | 2025-09-06 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e390fd9-b6d3-34ac-addf-49dbacdf7589 | -12.98153 | -54.82215 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a731d4c1-472e-3b94-8ec1-6cff9d565fa9 | -7.41417 | -44.93955 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8d1fbe6-b439-3430-b7cd-f67049bdc3ff | -12.50319 | -53.85824 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 580ca050-9542-3167-a0d3-b89182cb70ac | -5.8673 | -51.72367 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1592996a-b2d5-3140-8172-40cdf9d26753 | -13.01382 | -54.83696 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6cf6af32-a1f1-35ac-ae8b-19be66bf21bf | -6.27173 | -53.44553 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a04c0d4c-65c7-3ee5-a130-76d9e0e97619 | -5.88869 | -51.97108 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c10320e-02f0-3a85-b50a-2834b67079fa | -16.68667 | -44.59064 | 2025-09-06 04:17:00 | NPP-375D | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88a5000c-4838-399b-9e34-1af0cf591007 | -5.99634 | -44.74157 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71d56f10-11a5-36d9-86a3-4c505e8546c2 | -5.9504 | -46.16712 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed311647-6fcc-3647-90ce-7cd8d8663332 | -4.64735 | -46.37261 | 2025-09-06 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1cc2a39-2d7c-3b03-828d-eac160b34398 | -14.11947 | -51.71226 | 2025-09-06 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b66fe262-a174-3a51-bae9-7e0fcb1ffeb0 | -10.6555 | -44.83578 | 2025-09-06 04:17:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 558687af-44ca-3ed4-ba89-1352e81c08d3 | -6.5933 | -44.55041 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d2f8ac9e-d0a8-3aa1-9526-9eeefb2ef67e | -15.07401 | -48.1137 | 2025-09-06 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cc85b24-ac3d-38f6-a04b-ac12e0a743a4 | -9.70083 | -49.48832 | 2025-09-06 04:17:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c539afc7-c7ce-3109-98c8-495d5c60e858 | -7.46356 | -45.19428 | 2025-09-06 04:17:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1cf6c093-944b-3f85-abab-5a6dcf4959a9 | -14.5691 | -48.09115 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8621b11-6e8c-3000-9d3e-cd7ec0f9b299 | -9.0867 | -47.01834 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd0c4bb6-7437-3e39-a9f8-b2ba90354c37 | -3.75413 | -49.05875 | 2025-09-06 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffee9431-8b0d-3ac5-a04e-dbadb7e53911 | -13.85316 | -46.25457 | 2025-09-06 04:17:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 067a35c2-94d8-32d2-b6c0-25f0c0bce2f6 | -8.90977 | -45.77698 | 2025-09-06 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1383e5ff-4497-3836-b873-3ff6ddc66833 | -5.8542 | -43.43416 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 858f1f32-20d2-378b-8993-e7d7f74822d6 | -15.85684 | -52.2887 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 874743e1-1a87-3566-9690-7da632e28136 | -7.28322 | -43.7044 | 2025-09-06 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa5aaaa8-46cd-3cd8-9c1b-70bf081f2566 | -9.08308 | -47.0175 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d32601e-6c68-36dc-b2e1-5ec96f9b32a6 | -13.26798 | -46.81129 | 2025-09-06 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6227e505-9450-3232-a17f-b33544d2e149 | -5.96158 | -44.74414 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9db27131-f2ff-3d03-8b8a-ffd13a0000d9 | -8.90614 | -45.11046 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8fe452a-6dde-3360-8bdb-953ad64ec95e | -9.84601 | -48.8344 | 2025-09-06 04:17:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6772c4e4-49f9-3cbb-9ed4-e519c80d9777 | -12.96139 | -54.80551 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 939d0e35-5bb2-3cef-8337-3fedd6e6c9e4 | -4.7975 | -47.26322 | 2025-09-06 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10074101-0c04-3e9d-b442-b12892f6c59f | -16.29785 | -45.69024 | 2025-09-06 04:17:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 029f15ae-4195-382c-bff3-9a3b41a9f457 | -15.07043 | -48.11303 | 2025-09-06 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f6afa69-106b-3905-ac33-ada17f5a73fc | -13.84731 | -46.26889 | 2025-09-06 04:17:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61efb957-ebd4-32f9-a2af-f4499f71437d | -14.83222 | -48.19357 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5244ca72-249a-36b7-bb12-3af7b4fd18da | -6.54148 | -49.51629 | 2025-09-06 04:17:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8cf01fd-95bd-3250-993c-e8de90448fb8 | -6.98572 | -45.42548 | 2025-09-06 04:17:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aba9255b-b755-3255-b759-515396f75672 | -6.01347 | -46.69027 | 2025-09-06 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ea0c545-6a99-3c04-8b48-11a7596f1e96 | -13.33109 | -51.72489 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d954a4be-35b8-3319-88ed-e785f6ccde70 | -5.61236 | -47.44191 | 2025-09-06 04:17:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62c367c6-4816-37e3-a83d-dde5a5a9ae3a | -5.26433 | -44.45294 | 2025-09-06 04:17:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a49fa7b2-44bd-3cb9-989f-3bdf4e2c8bf0 | -6.91388 | -43.81396 | 2025-09-06 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f16d3e5d-3c9c-321e-89d0-e99b436ae436 | -5.86434 | -52.17383 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c031182-8394-3a29-a2b6-42ddf21b2c35 | -13.90132 | -48.01922 | 2025-09-06 04:17:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e3f33a7-3d2e-3bc6-88a4-63458639fc40 | -14.83298 | -48.18922 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08e8f5a2-68c0-3098-8136-6d6bdea11b90 | -13.01791 | -54.84595 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db3e050a-616d-3b92-b8ac-dca038d246c8 | -6.22271 | -45.63823 | 2025-09-06 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46ce8348-22cb-3028-abf2-5dcf77ba34b3 | -12.99514 | -54.81275 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fdf5d87-4cbe-3499-863c-a7dbe70fa33d | -6.27245 | -53.44151 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d42d1e6-b25a-35aa-adb0-693382a016c3 | -14.12034 | -51.70762 | 2025-09-06 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f606dc63-d803-3109-a5db-25f0e0d74bb5 | -7.00681 | -44.95465 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af8600ad-e90f-3d8c-b588-fb5f1a339493 | -6.55109 | -42.94606 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3b5e29c-a939-3bf1-ae1d-6f795e25b00b | -6.51529 | -43.06495 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db537ed5-b9be-367b-b0da-bd1c0ffff672 | -10.15924 | -46.23774 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8a60c0d-1b91-3ff2-a9fb-6e491121df14 | -6.21409 | -43.57716 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d07be9d-4a8a-333f-afb8-e22f1780bbca | -4.79329 | -47.25941 | 2025-09-06 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 69a57961-994a-39f0-9592-05a69aad9842 | -6.6661 | -48.40066 | 2025-09-06 04:17:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7c1f1d70-0983-39b1-9aac-ab64753ad6d6 | -12.84709 | -48.01734 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ae179ab-c5d2-3bc2-8983-267a0e06333b | -8.69329 | -45.27949 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 613e3788-89d5-31d3-b736-d21daf545d53 | -7.76232 | -50.74504 | 2025-09-06 04:17:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ec80fe03-4ce5-39e5-92f0-7e1372022227 | -6.93078 | -44.96867 | 2025-09-06 04:17:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55fcfb0c-de19-30d0-863a-51fee5e45156 | -7.02343 | -43.23117 | 2025-09-06 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| eadb2e6d-6838-3812-aeea-70bff0d3aafe | -8.90556 | -45.11407 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67c89efa-58f3-32fd-91f4-fcfb971b2670 | -6.6097 | -43.98541 | 2025-09-06 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9054129d-e698-3e73-a5a1-7ccbdc32018a | -7.58802 | -49.28588 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b79521c-2e85-34e3-ae0a-40450a7f08b5 | -14.89396 | -49.45364 | 2025-09-06 04:17:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 09c5c3a4-cdb0-3f44-899a-24fa75b651ae | -8.3682 | -52.56414 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b83330b-2fea-3cd1-bbfe-c009885d19f8 | -5.97896 | -53.59415 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e83acf4-307a-30dd-bd0a-d4b896439c30 | -6.9892 | -45.42606 | 2025-09-06 04:17:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 497ed7c5-26dc-355a-aa84-e18aee1da663 | -5.42026 | -41.14171 | 2025-09-06 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 969f8aa4-cdb6-320a-b2b0-cd635a80af00 | -5.93418 | -43.01605 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d7755721-74a7-36b4-a88b-cc8c9ad6a8a3 | -14.56996 | -48.02106 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc0876bf-c446-31f8-b74d-e505a989b658 | -12.61864 | -56.9906 | 2025-09-06 04:17:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b36f342-f6bc-3b98-89ea-c632dff0fda3 | -10.31508 | -46.41143 | 2025-09-06 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ca39a3e-82c8-317d-a399-3077aa941d3b | -12.92312 | -48.03335 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8caf3de-e798-319c-8806-331e3d98f02f | -12.98468 | -48.04966 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4af93d05-ffee-3c9d-80db-63c56394ea9f | -3.24927 | -50.80051 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 727c470c-8385-365e-aa7f-e877e1586fe1 | -6.91165 | -43.80643 | 2025-09-06 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1a2b272-b640-33df-88cf-c5f799cd19c7 | -5.54809 | -43.06494 | 2025-09-06 04:17:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad1f4278-dd11-3f8c-a2a5-9899d8478b80 | -7.41699 | -44.94375 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bce59b7d-294b-3e1d-b17e-90f80b027aea | -7.17067 | -44.00251 | 2025-09-06 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdda195b-95da-34cf-b699-75bbb7b33512 | -7.13093 | -45.50773 | 2025-09-06 04:17:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ad36d49-30c6-3947-9275-06c893a2237e | -9.40893 | -46.78674 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de773ec7-4aad-3c2c-9bca-c50a50806cb4 | -3.16191 | -48.60764 | 2025-09-06 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f776343b-17c0-3c35-9add-5c3c2a866795 | -13.73481 | -46.91224 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f283e723-ea1a-3457-a0b5-62d155ddd2b5 | -5.93364 | -43.01952 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 224c4805-1248-3838-b3f3-cc35af5ca6f9 | -15.98386 | -42.38696 | 2025-09-06 04:17:00 | NPP-375D | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 16f0a15a-5f19-31e2-bf72-e38764093987 | -13.66736 | -46.95322 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f04f6e88-af90-3925-b8f3-cd56650b8ed8 | -7.81291 | -47.50889 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1040b92a-3abd-36bf-bb81-d49fcfc0d802 | -3.24782 | -50.79968 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| efc80e89-eab3-329c-9451-48186aa460a3 | -5.95153 | -53.79782 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e20c5f7-df75-34a9-81ee-d2a7ae0b2321 | -13.88456 | -48.02965 | 2025-09-06 04:17:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55cb7f74-0308-3119-87db-63aa4861ce2d | -6.23887 | -43.29206 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0c55584-10db-3fcb-b3be-7d2fc74a9612 | -14.58008 | -48.00525 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da13fb3e-cba0-3ef4-b080-80d63a6e8885 | -5.47262 | -44.13288 | 2025-09-06 04:17:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c847c3b2-fe69-3feb-a66e-be2b876ee248 | -7.1718 | -43.99546 | 2025-09-06 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16d79ee6-f9d7-3b51-97a5-622e83966e57 | -10.09013 | -48.07808 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README34.md)
