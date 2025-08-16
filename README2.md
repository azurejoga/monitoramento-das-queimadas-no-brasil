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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd27af4e-51eb-3d09-8a9d-dc4c93eac2b5 | -6.5541 | -43.032501 | 2025-08-16 00:02:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd17ef22-0383-3f30-bc1b-130afc9fbfa1 | -3.8278 | -47.7281 | 2025-08-16 00:02:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fb3f8ad-cd3a-321a-8811-db3da372caa1 | -11.9336 | -44.125301 | 2025-08-16 00:02:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef332afa-997a-320e-a25c-a9ee300ae603 | -13.4178 | -43.685299 | 2025-08-16 00:02:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ec8dcf8f-d579-3e23-96da-6b10fdcef2aa | -11.4148 | -44.6721 | 2025-08-16 00:02:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 06afb9ea-58ea-3dd6-b368-e08897e896ac | -12.8155 | -45.9911 | 2025-08-16 00:02:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05f32d73-68d2-3299-b18d-c822ab6f0c32 | -7.4042 | -44.885101 | 2025-08-16 00:02:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed625656-6cd7-32d7-91b2-cc159c6ce8b7 | -4.9194 | -43.241501 | 2025-08-16 00:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b387a77c-2f16-38d5-bad4-400fc441101e | -11.9306 | -44.1101 | 2025-08-16 00:02:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fb55e6f9-feae-316f-b79b-d5da8e475b76 | -3.9833 | -43.2304 | 2025-08-16 00:02:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3490d319-ea52-3fea-b8f0-84a531954407 | -2.3716 | -47.633301 | 2025-08-16 00:02:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77bca7a2-ecf3-31f0-9a67-e8c1939e9464 | -3.8233 | -47.708 | 2025-08-16 00:02:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c2936d6-2eb1-3d44-a92d-bb868445e3ec | -14.59 | -47.903198 | 2025-08-16 00:02:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ee537cb0-446d-39f0-a602-5adc7327eff3 | -12.5869 | -46.901699 | 2025-08-16 00:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49031b2f-6695-380f-9c99-caff475b6610 | -6.6696 | -43.749298 | 2025-08-16 00:02:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33c4fd45-046f-3d63-af92-8ec6c8903f9d | -4.9142 | -43.2645 | 2025-08-16 00:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97e24031-e4f3-3d77-a4c3-49222e8b89a7 | -13.4247 | -43.6684 | 2025-08-16 00:02:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5c77753f-fbbf-3f97-9e33-f12bd379674e | -3.8181 | -47.730202 | 2025-08-16 00:02:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dc2dc95-edc7-3845-84a2-97ebb0cc7a84 | -5.7532 | -46.6772 | 2025-08-16 00:02:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c6eb86c-8c27-32a8-81f5-61f2a2c3304f | -6.6722 | -43.7612 | 2025-08-16 00:02:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ace6086c-1e35-342c-9e28-8f0ab8e68eef | -12.5671 | -46.955799 | 2025-08-16 00:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ad33cc6-8687-3c8b-b8af-abf324b40ba4 | -7.3812 | -44.920399 | 2025-08-16 00:02:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dfd1f8f1-3e53-3637-a95d-b6c10727cbc1 | -12.5624 | -46.9314 | 2025-08-16 00:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ff27c789-6e3e-3dc7-a20a-596f073292d5 | -12.5966 | -46.899799 | 2025-08-16 00:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 816b3756-576d-3c66-b6cc-069d438a78ba | -14.605 | -47.9319 | 2025-08-16 00:02:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 88accab0-c1d1-34a9-93c3-1eba789c4860 | -9.1725 | -45.314899 | 2025-08-16 00:02:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 590a37e7-2452-3ee5-85e6-c31ad14c9ebf | -12.6058 | -46.948399 | 2025-08-16 00:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e31fc30-cb46-386f-9e10-794d117b599a | -5.1986 | -46.090199 | 2025-08-16 00:02:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4704762c-2726-3eab-85a5-e0516c776b30 | -5.2636 | -36.181301 | 2025-08-16 00:02:00 | METOP-C | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 5d203897-68f5-36bd-bd2c-117013f8a554 | -12.8195 | -46.012199 | 2025-08-16 00:02:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0e4d95cf-c36b-345b-99c2-246eef0c07a0 | -2.3801 | -47.671101 | 2025-08-16 00:02:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 164648ad-25a1-3cfa-8e81-4ce640c94d8c | -12.5915 | -46.9259 | 2025-08-16 00:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f504475-59f1-3b7e-98fd-7607649da834 | -3.9855 | -43.240501 | 2025-08-16 00:02:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03e3678e-0334-3ff4-b76f-4c8977d4e4f6 | -3.77 | -39.192799 | 2025-08-16 00:02:00 | METOP-C | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6ab8c02a-1996-35fc-b5c2-b8b875ae947d | -5.759 | -46.657001 | 2025-08-16 00:02:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2dea3e5-1476-38ca-b111-5412653fbd2b | -13.649 | -44.192699 | 2025-08-16 00:02:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3d4fa100-2921-3a06-9b8e-74b8f45d09a9 | -6.9278 | -43.008499 | 2025-08-16 00:02:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6bd7973b-3ef1-3184-98b4-642e0124f419 | -12.5961 | -46.950298 | 2025-08-16 00:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a7ebabe-885b-37ee-92b6-fcdfa19066fc | -4.9096 | -43.243599 | 2025-08-16 00:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 856dd0ad-32f0-3fe4-88f8-3048ac58d37e | -13.6522 | -44.209099 | 2025-08-16 00:02:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d185152-885d-3528-b339-df42d1e22d39 | -4.9119 | -43.254002 | 2025-08-16 00:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58a3a808-bbd0-3fa0-b24f-878ab7a236b4 | -5.762 | -46.6741 | 2025-08-16 00:10:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| b24fc0da-3a65-343a-b571-b511d633d0f7 | -9.2082 | -59.6354 | 2025-08-16 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 638f5739-6f79-3e4d-b972-d2034d8f4d86 | -9.0531 | -67.4265 | 2025-08-16 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 3be4815f-541b-31b1-b62d-0a30f0606053 | -14.9628 | -54.7351 | 2025-08-16 00:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| c9dec3e0-a532-36b0-b22c-57682d93319b | -9.0346 | -67.427 | 2025-08-16 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8a037ddd-ba84-3d16-9b50-d3b84610375d | -6.5638 | -43.0357 | 2025-08-16 00:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| f8d29cef-f5b8-36b5-bf45-992b663ec722 | -13.4294 | -43.6733 | 2025-08-16 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| dc8faf11-0f03-371c-b9dc-4ee697523d6e | -11.3466 | -55.4326 | 2025-08-16 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 47f01b12-0abf-39c8-a5e1-a7b56d333afa | -7.0404 | -59.6222 | 2025-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| befad394-5fff-394f-b584-6507e4f73277 | -11.2593 | -50.4981 | 2025-08-16 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 4495634f-8136-3398-9048-bc40dc7abaf5 | -6.6142 | -60.0039 | 2025-08-16 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3acd8f34-edda-3f6b-b0d2-c92a45ea614a | -4.9305 | -43.2558 | 2025-08-16 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 9eabda77-238a-3fa2-b0dc-4f68d2655f24 | -7.9333 | -61.7471 | 2025-08-16 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| abcfd107-a2ae-37fd-8354-73452ebcdc4c | -13.4099 | -43.6768 | 2025-08-16 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 8141c796-778a-37f8-b80e-b3c907d95fb5 | -9.518 | -60.5268 | 2025-08-16 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 0b432bc5-32db-3bbb-9206-3c2b668638df | -7.4258 | -60.0292 | 2025-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 9dda8489-298a-3219-bf33-28f011fcace9 | -4.9116 | -43.2803 | 2025-08-16 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 3d31061e-aced-3f3c-ac9b-9c931f551b30 | -6.6326 | -60.0224 | 2025-08-16 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 34a1ec0d-9a05-3dc7-9719-06f98c6f3eaf | -7.0796 | -59.2351 | 2025-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| a1e60bd6-60f5-3968-b610-a7bec9c73ab2 | -7.0981 | -59.2343 | 2025-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5e50cf8d-76e9-3f78-b248-bb3835b5f522 | -13.1265 | -57.1494 | 2025-08-16 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| b6cad0bd-06db-3c1e-993a-2fa971daa4e0 | -6.7811 | -59.8249 | 2025-08-16 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 1410bee3-1220-36a3-9209-e27f0fcf4fc7 | -2.3763 | -47.6636 | 2025-08-16 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 8eeab21b-0ccc-3bc2-af1b-974c2cd8450c | -9.1711 | -59.618 | 2025-08-16 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| f9cd6713-6f31-3f6f-b74f-61e4a4e92194 | -9.1708 | -59.6568 | 2025-08-16 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |
| d926feb2-8c8a-3cf8-a689-2382c680ef54 | -6.9296 | -59.646 | 2025-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 67d24636-ffcb-3b0b-b847-60e0a26a3966 | -9.5179 | -60.5461 | 2025-08-16 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 884677f8-dcaf-382c-8a0e-a1e8fe41a485 | -7.9149 | -61.7288 | 2025-08-16 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 139.8 |
| ad571c6f-ac11-32ca-b207-e26bfe978029 | -9.4992 | -60.547 | 2025-08-16 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 13c71246-3014-39c1-bf62-338ace8bded7 | -9.1523 | -59.6384 | 2025-08-16 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 2d97634d-e74c-359d-be1b-5fb3a779de93 | -13.1077 | -57.131 | 2025-08-16 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 174.6 |
| 2b100a0f-b47d-3928-8b37-e5031f734fd0 | -6.9481 | -59.6452 | 2025-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| adb1c261-4a04-3c68-b123-cc4d7b882b6e | -14.9438 | -54.7166 | 2025-08-16 00:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 68a7e044-42d8-3d18-a75c-602dd682beb2 | -7.0589 | -59.6215 | 2025-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 9c296b33-0953-3030-8a07-463e5a9923be | -14.9441 | -54.6959 | 2025-08-16 00:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| a0286c1e-b182-3c06-a445-2801360a1689 | -7.0797 | -59.2157 | 2025-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 1cbafe07-b7bc-3aef-a3c9-5ebcbddea830 | -13.1267 | -57.1293 | 2025-08-16 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 199.1 |
| 64da1604-120b-3d0d-a722-5de7af779c27 | -9.1709 | -59.6374 | 2025-08-16 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 176.8 |
| 51073cb3-f45f-3ab8-8c5e-40f4cca65a87 | -7.9148 | -61.7478 | 2025-08-16 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 169.9 |
| f5b3693a-c153-327a-a4ab-6c2b091dec4e | -4.9118 | -43.257 | 2025-08-16 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 183.6 |
| 5aca47b0-e6cf-3947-bcb1-87089016c953 | -7.8247 | -61.3327 | 2025-08-16 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 133.9 |
| 4ba10d94-b0aa-3f4d-aed8-0cbe4f10d8a7 | -14.9632 | -54.7143 | 2025-08-16 00:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 58721190-acca-3fa3-af0a-c4db0db76783 | -7.0612 | -59.2358 | 2025-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| b96f907b-67f6-3ef2-8363-1a6a51e19eb3 | -6.7995 | -59.8242 | 2025-08-16 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 2447e11f-b823-36a1-ac2d-26c401133ad7 | -17.615 | -46.684 | 2025-08-16 00:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 75.6 |
| a4b8bcf0-5e75-3eca-9ea5-09ffc69f719a | -9.4994 | -60.5278 | 2025-08-16 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| b0b85d17-2fa4-3f2b-a5bb-f95594393136 | -7.8963 | -61.7485 | 2025-08-16 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 4bf2fc70-453c-3545-8004-3041341f147f | -11.2596 | -50.4767 | 2025-08-16 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 03510294-4ea0-337f-bbc8-20118c578be7 | -13.1074 | -57.1511 | 2025-08-16 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| a5fd82d7-b881-356f-a532-0666724f85ad | -14.9635 | -54.6936 | 2025-08-16 00:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 62b2bdb1-2745-3059-8925-6cb0bb0918b5 | -18.5325 | -50.7384 | 2025-08-16 00:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 0b7fe46e-e9b2-383f-b8f6-fa2d346b0a3c | -11.3655 | -55.431 | 2025-08-16 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 018709f4-4825-3a9d-89bc-e1bf22c236aa | -7.5292 | -61.3254 | 2025-08-16 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| d5715b7a-1237-3713-a732-45a7a1e5c834 | -7.8248 | -61.3137 | 2025-08-16 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 9799e1cd-3eaf-3803-9186-b510a19de090 | -6.6327 | -60.0033 | 2025-08-16 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 168b3eb0-3306-3ac9-b7ae-c4029a7b0bbe | -9.208 | -59.6548 | 2025-08-16 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| c7f945b7-29ed-3e8c-977e-5ab0b930fb7a | -3.8209 | -47.7444 | 2025-08-16 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| a4c946b6-0670-3802-be54-9f4008be61b5 | -11.3468 | -55.4124 | 2025-08-16 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 3f80e1ee-3e3b-3a9a-872c-59b46d442f65 | -9.4994 | -60.5278 | 2025-08-16 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |


[Clique aqui para ver as próximas entradas](README3.md)
