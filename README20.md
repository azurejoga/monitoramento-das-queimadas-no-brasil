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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c15ad42-78da-30f8-8d13-ef736d42ccc2 | -7.53902 | -55.58287 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4e17d50-8b5a-30fc-b5c6-943aba7b7227 | -8.49378 | -48.81404 | 2026-08-18 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19475b9a-a46a-3415-be1c-21d23894220f | -8.21425 | -55.03329 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2591726c-9e14-3adf-97f9-00dfd3d0cc9d | -6.6742 | -56.16263 | 2026-08-18 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69b86518-452d-3f6f-8629-7567a9fcc189 | -9.47477 | -51.60175 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01ec2814-1b72-31a2-b106-d040912767eb | -4.49332 | -42.56327 | 2026-08-18 04:38:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ffac7449-150e-3346-9177-f5090ab8652b | -6.53022 | -43.12664 | 2026-08-18 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d6abbce-7daf-3c7d-b782-e6ac27123182 | -8.22817 | -55.0419 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 235354be-c445-3a6c-be2c-c8f235ab2464 | -8.36586 | -46.36824 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 007cf665-334b-33a1-9a6f-be4be1793d4e | -8.58705 | -54.70518 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8567ed2a-90f1-3984-8134-df2e309252cd | -4.48965 | -42.56271 | 2026-08-18 04:38:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1991a1d2-88cc-3e85-9f27-73222613aa2b | -9.46272 | -51.6252 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2a77df20-88d9-310a-bcda-1e3508323cf0 | -8.60105 | -50.34171 | 2026-08-18 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39a20abf-82ae-3f6d-98ca-99a7add6bde1 | -4.71925 | -42.76832 | 2026-08-18 04:38:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50c2b80f-76cf-3148-ba69-ed84a94e1fd5 | -8.21983 | -45.78618 | 2026-08-18 04:38:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 949f1a33-4940-3e95-bc68-901978f9a773 | -6.7544 | -59.16566 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b51934fe-ca8a-3f59-82c8-12feba9ecf78 | -7.01108 | -45.90389 | 2026-08-18 04:38:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70e9ee07-b4b9-389d-a3a1-bd634a120d53 | -8.2103 | -55.02658 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9f052ac-7afb-3c1c-909f-104bd439ed65 | -8.56346 | -54.709 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 92d69180-2715-360b-b3e4-544ce28b7fb4 | -8.09967 | -51.66222 | 2026-08-18 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8099c209-2a66-36bd-96c9-546e248a46ae | -3.68181 | -47.65047 | 2026-08-18 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e6667a41-ecd4-3da1-994a-f30c082da137 | -7.46026 | -59.9976 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a732ca33-0557-3d57-8230-b10229f1d6da | -8.52907 | -54.90612 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bfaab47f-4f1e-38cf-979a-f9a7e25a011d | -6.39842 | -54.95094 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a5845b4e-8447-3c3e-9933-a6531ecf64f5 | -9.1388 | -46.01719 | 2026-08-18 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e21f2bf-c6c7-3c41-b2c4-6b0519fc363d | -7.13369 | -47.52043 | 2026-08-18 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d5e7f54-efaa-3c71-ba3b-530088771d0b | -8.55467 | -55.30419 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4a96e8a-6403-3a8a-9bcc-dd4ea498efd7 | -9.79446 | -47.30888 | 2026-08-18 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 092a5e51-5826-37d2-9203-6473f9f1dc06 | -6.17953 | -47.78493 | 2026-08-18 04:38:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 914d397a-38ec-3849-975e-e57b992b71bf | -8.36641 | -46.36475 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a96e6f86-b3fa-3f25-ad8b-187a574c507a | -6.8538 | -59.00202 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a826654-2042-384d-9651-a3d8e747f7e1 | -6.18103 | -47.81857 | 2026-08-18 04:38:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ed950aef-11e4-3300-a464-39ffc3d2d7da | -8.53092 | -54.90329 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0d6143e-e8d3-30b0-94f0-cdd68fd51384 | -9.77565 | -47.29866 | 2026-08-18 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14b62ab5-fefa-39b3-89f0-9089b22631c9 | -6.85278 | -59.00748 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f02d135-91c4-3a72-8f26-83d513b59c7b | -8.49071 | -54.86464 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 92d62309-c4f2-3c74-99f7-50914b2bbb6b | -6.75546 | -59.16013 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ff2651cb-ba18-37f3-ab5f-f9f9b9393c44 | -9.47096 | -51.6475 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 918a2716-feab-3a8c-8f06-7f1ca9ecfa17 | -9.0685 | -50.8297 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 742a0795-5378-3258-9ff0-428ae47d08c1 | -8.6268 | -54.70689 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 72430e60-4ea3-300e-aae2-59a2a83b1048 | -7.2826 | -44.06946 | 2026-08-18 04:38:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34e6419f-7461-3e50-8caa-177053c158e6 | -5.8063 | -43.63944 | 2026-08-18 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba1fcb47-bab2-39c8-b1ee-b4c11457208e | -9.79723 | -47.31291 | 2026-08-18 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b73d72a7-4dc8-384e-83dc-21e8d1118fec | -9.43425 | -48.26036 | 2026-08-18 04:38:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 966d1958-59c2-3b14-bc2d-ba1d3513cfd8 | -6.74425 | -59.18269 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b2fd27be-82b7-3b64-8e69-6cd04e64eb41 | -9.07127 | -50.8591 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2a74870-dc04-3cf1-a584-84338d71a0bd | -7.37858 | -55.48906 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30204c30-cc6f-3015-9a27-5123061aaf71 | -9.13935 | -46.01364 | 2026-08-18 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53cdc558-c3fe-3a07-94fb-457d2125d335 | -7.39596 | -55.48227 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b6a2dd7-28bf-390e-8ec3-839126a61bd3 | -6.74194 | -59.17963 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f61f1d53-0e87-3717-b22d-e7a2639866b1 | -8.64868 | -43.89312 | 2026-08-18 04:38:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bea29d5-be57-3858-a732-98b96c8ff557 | -7.12978 | -47.52343 | 2026-08-18 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d100d8cf-eab0-3bb2-930b-6f92bf152f17 | -8.56963 | -54.71833 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 210461af-ac47-318e-b6b6-66fa855cb0d9 | -7.63814 | -55.62826 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66b0e29b-acd9-36f9-a9ac-0440188a9b95 | -6.53387 | -43.12719 | 2026-08-18 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 597c01ff-57f5-3b98-b808-badcb0116eab | -9.0699 | -50.84427 | 2026-08-18 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| dcd02458-9e29-3ec2-9191-bb7c76541084 | -8.60472 | -50.34233 | 2026-08-18 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f33c2aa3-f681-3846-8f32-816da7ffd7f5 | -6.20817 | -57.7687 | 2026-08-18 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb9aa12d-74f9-3f46-9f32-78236d9495d0 | -6.7685 | -59.45738 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1b74331-37ec-3c61-81d8-dd28f026b927 | -5.26661 | -49.04731 | 2026-08-18 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aef51fb4-e06b-3750-9ab7-316f2f9cded8 | -6.10193 | -57.73215 | 2026-08-18 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed3820d3-0110-3cb2-892a-e0153f14a01e | -8.10936 | -51.65371 | 2026-08-18 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d578db5-e396-3439-ade7-ba56bcfd787d | -8.10286 | -51.66041 | 2026-08-18 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2843d33e-37b2-3a81-8612-3737d3b0ce19 | -7.82525 | -44.09903 | 2026-08-18 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82b2f7b3-3a56-32e7-8c92-aa24999bdd07 | -10.29292 | -48.23541 | 2026-08-18 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9c0a94d-f30b-3201-a17e-3ef41694bb95 | -7.45565 | -46.15636 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 851e8955-87ea-3279-ab6b-e53d5fb04338 | -7.62449 | -45.72594 | 2026-08-18 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a422f05-6c99-38c2-bed1-3a8ffc2edbe0 | -6.16615 | -47.76052 | 2026-08-18 04:38:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98e13af4-3f4d-36d0-9db9-bd194e52ccb7 | -4.30875 | -49.08344 | 2026-08-18 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb2d3a0a-82c6-3452-8ad5-e471f4b4532b | -7.36755 | -55.49046 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3588d74-e162-339d-a6ec-2975f1e8e3f9 | -10.28842 | -48.24207 | 2026-08-18 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bca0e19e-5b15-3807-867d-6d8aeb4afe0e | -6.7441 | -59.16795 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f43e802d-82a3-37ad-bc6c-0ca7e2946c7f | -8.49344 | -48.79475 | 2026-08-18 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffeaf73e-a829-3be0-aa93-5713ea22890f | -9.15281 | -40.1112 | 2026-08-18 04:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 58ba6242-3cbf-3d3f-a454-bf76614bf404 | -8.63166 | -54.70768 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 95da258b-afee-34c4-b2e8-38d178a4968d | -4.48728 | -42.55355 | 2026-08-18 04:38:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ff5127e9-dcb8-3905-8fb8-9f77833bc291 | -7.00248 | -44.83476 | 2026-08-18 04:38:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| edd212f2-7551-3c46-b08d-72e8db071a76 | -6.75299 | -59.1571 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 25ce55f7-34fa-3597-8831-ad0c16fd6f78 | -6.77525 | -59.45868 | 2026-08-18 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16f5803c-c424-3e66-93d6-0bef69cd5510 | -7.36696 | -55.49372 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35399ea7-8c3f-3313-a9eb-d4a13e4dac73 | -8.74335 | -45.30931 | 2026-08-18 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa16b3a6-aa0d-3364-8c31-5eff56e62451 | -8.48787 | -48.8285 | 2026-08-18 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 14.7 |
| ed58ced6-0244-3e1e-a294-0f20a75a63fc | -8.22319 | -55.04092 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| caa1bd47-e2ac-31c4-a34f-072972fb6da2 | -8.48973 | -48.81721 | 2026-08-18 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| db76fa1b-548a-393a-b5f5-17eb1fa6d2ec | -7.6339 | -55.62735 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09c08a57-65da-3fae-89d9-3a7fceaf07c9 | -8.58417 | -54.72111 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 05778e3e-7c61-3c83-8c9c-823ad1261e17 | -8.56866 | -54.69608 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bc68a8cb-c0c5-3ede-b5dd-8d7d64e59cd0 | -8.10849 | -51.65872 | 2026-08-18 04:38:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3a4d9c8-0394-3c11-b7bf-ac9a9ff58cfe | -5.47425 | -45.11697 | 2026-08-18 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7538caff-704b-336e-beaf-beb87b84a192 | -8.48627 | -44.73185 | 2026-08-18 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8544fe6-1d63-3188-8f0c-a2864e7b39c5 | -7.6176 | -55.62762 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60b5a26d-af16-3b1c-82f2-69e288586a99 | -7.3954 | -55.48545 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00fe6f5b-9bf9-3d58-824e-fe67129291d7 | -6.55463 | -44.77476 | 2026-08-18 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91699934-68b9-3b8d-8429-a25a4811a000 | -10.42952 | -47.84723 | 2026-08-18 04:38:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b2f0f7b-5764-396b-87f2-a4887e10059c | -8.57735 | -54.73112 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| bed97fdd-adca-3e1c-b731-b705bd9c4b60 | -8.2132 | -55.0391 | 2026-08-18 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f6803593-ef57-351d-9ab6-d20ba0304c39 | -7.45898 | -46.15688 | 2026-08-18 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b4493b31-ce51-3105-b225-594565beb68c | -6.27284 | -43.27539 | 2026-08-18 04:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c36b21b4-e57d-31c2-81ac-78fffc07b442 | -6.30794 | -55.714 | 2026-08-18 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75af2775-781a-36ed-aee4-ad22ba49c954 | -7.60554 | -60.95753 | 2026-08-18 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README21.md)
