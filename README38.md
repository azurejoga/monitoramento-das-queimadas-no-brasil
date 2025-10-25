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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81646783-2900-358a-bc48-ea7f3e9b0556 | -12.83679 | -46.6958 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62f899a6-53a5-3483-9f4f-cd79f866b082 | -9.25076 | -45.59442 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0432c478-8642-309a-9f53-153e6d0f1bff | -10.06451 | -47.08438 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd80dd07-1960-3e14-b4af-3eb23bbc6e58 | -11.54715 | -43.15358 | 2025-10-25 04:19:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a1115f96-040c-3c20-a839-f7bc5347afa7 | -10.65773 | -48.0837 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d790aee7-95e6-345d-9e97-071fa97505e3 | -12.9529 | -48.50641 | 2025-10-25 04:19:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79919fb4-3222-3aef-b283-3661d83e0bd8 | -7.37528 | -47.04954 | 2025-10-25 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e2f4efe-10fd-3ce5-aa9c-acc6ca5c3ab0 | -6.64526 | -43.60818 | 2025-10-25 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8127834-fe95-3cc6-a967-8dfbe53860d6 | -11.98843 | -43.31829 | 2025-10-25 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d132b0cd-daff-316e-ae37-6ba7a3408852 | -12.70116 | -46.33262 | 2025-10-25 04:19:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75bdbffd-7a55-389a-83eb-b4c5a04f5e18 | -13.35274 | -47.4125 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2dab3cd6-a99a-3e6a-aaa0-5c91c04e0253 | -12.21363 | -46.51279 | 2025-10-25 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4ed6f16-b5a3-3f68-a1ea-66518e462b28 | -11.85603 | -49.86273 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9709286e-8b63-3a40-a48d-c58566b4ed6d | -12.2565 | -47.44015 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f664c94c-715b-3295-9c6a-eed0cbd1655d | -9.32685 | -46.98 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5670fbe-c44a-3f84-a045-c6b8ab7e0bab | -11.59246 | -45.06693 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc560701-f234-3462-b3dd-4912aaa8436f | -6.99917 | -50.60366 | 2025-10-25 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b0bc008c-5cad-386f-af80-20382b6058a0 | -6.80687 | -45.42734 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b59b42c-5c32-3e46-8928-197e8c74ab1e | -13.20197 | -48.44787 | 2025-10-25 04:19:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| add5cfeb-6e91-343d-97bb-10d9fd3fbf5a | -5.87942 | -49.36909 | 2025-10-25 04:19:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 575d6c81-8dab-3300-8130-3338ddd42b7b | 1.63931 | -55.74866 | 2025-10-25 04:19:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| df85d0c7-23b6-3f48-9d76-b8edab751eab | -11.06124 | -49.62561 | 2025-10-25 04:19:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 39df5908-b2fa-3e18-bef1-d1475e03fc6c | -12.64189 | -44.30268 | 2025-10-25 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66108dfe-5e2b-3652-91b4-7763ea163b58 | -12.48181 | -46.93787 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8197a99c-1aa9-3ab9-bf63-63f2c3297969 | -11.42871 | -44.6773 | 2025-10-25 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 046fbbcc-fb33-3b2e-9563-2647a59980f0 | -12.83352 | -47.24007 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d07495ed-8619-3ab2-9edb-5061a0eb407c | -6.47208 | -44.1284 | 2025-10-25 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a3a419d-4b2f-34a5-a3b5-666796d0c4a2 | -12.1311 | -46.71127 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d96187d7-72b4-34ed-8fd6-a323c1973deb | -6.93651 | -44.88931 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82dff2f8-afe6-3f39-8b3a-c768fe6c3554 | -9.15502 | -49.36922 | 2025-10-25 04:19:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae6b1947-6c22-3cd8-bec7-c36faad5746b | -7.7873 | -45.39488 | 2025-10-25 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd8e53b9-5b9f-3596-819b-22aab573246f | -10.9548 | -50.28973 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcf211f5-675b-3c04-a566-0db7f7aa4802 | -6.80078 | -45.4228 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca9e48d8-6595-3811-9323-669593ed1d63 | -6.90139 | -45.17487 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fef8a6fd-667b-31f8-8961-7ea24879481c | -8.67023 | -44.77495 | 2025-10-25 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 095b30e7-1199-36e3-9d3a-893c27ab5be1 | -12.05904 | -43.98855 | 2025-10-25 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8741a1d1-30d0-3098-a74f-fd2fd4cc24cf | -13.20613 | -44.10663 | 2025-10-25 04:19:00 | NOAA-20 | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40c180d4-cca3-399c-ad09-5794c22ad878 | -12.234 | -47.48622 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 197a1b81-181b-33f1-bb5b-495237c3747e | -8.13443 | -47.04139 | 2025-10-25 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b26a5b12-1639-3375-a159-caceedc0bd4d | -9.32181 | -45.18845 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07e56bb2-48e9-309f-b9dd-189455f1189b | -9.1946 | -46.34749 | 2025-10-25 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c936e2c9-b146-32f6-a3be-ad1e28853e7c | -14.15392 | -44.31877 | 2025-10-25 04:19:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| de44373d-dbb4-3dae-baf4-a483b42f1d53 | -9.09449 | -47.82174 | 2025-10-25 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4129e55-0b8e-31e5-8364-c199d338c670 | -9.19088 | -47.74346 | 2025-10-25 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2450208-d35c-3891-b1d4-2e26ae6cc4f4 | -8.59344 | -44.83013 | 2025-10-25 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9bfcedd-3220-3907-80cf-62a596ecaf82 | -13.00322 | -48.54811 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a485419-d3f9-390b-99f0-e1a33140a979 | -11.57852 | -49.53676 | 2025-10-25 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acdd4869-c9c6-3fdb-92d7-953b55ff65a6 | -10.66237 | -44.71703 | 2025-10-25 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2863a278-f55e-3723-8efa-fee26bd96eba | -6.91739 | -45.1596 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eba864dd-4f27-3e39-80e9-a1cd8199df92 | -9.29921 | -45.18127 | 2025-10-25 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fbe9660-4612-3112-a617-ba6914e17790 | -8.59784 | -44.82372 | 2025-10-25 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15d81c65-f7fc-3aba-9a78-25eab6003f59 | -6.58138 | -48.77079 | 2025-10-25 04:19:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86d40129-863e-3faf-85ad-9566ab01ec45 | -11.95483 | -55.26221 | 2025-10-25 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3f33fd9-71ef-3741-af54-f2e9987c242f | -9.74822 | -47.83717 | 2025-10-25 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c93feee-f32b-356d-b728-8fb0baf9a3e6 | -12.10781 | -46.70739 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7bf7dc2-db98-38e2-899a-3bd8f13c978c | -12.12491 | -46.72854 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfbcf688-8c0d-3de2-a84c-f3aadc6ca998 | -10.4357 | -42.5599 | 2025-10-25 04:19:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dfcdcfe-5325-392d-91aa-eaf9cbb17e0b | -6.99984 | -42.79461 | 2025-10-25 04:19:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 178a71f5-c2cf-3074-a719-6bb119551693 | -13.33282 | -47.93558 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93228495-2d9a-352b-aa78-3f0d6e4fb9f9 | -11.69772 | -47.76204 | 2025-10-25 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f803ec4-e0c7-3bee-8037-661774e0fcba | -13.12381 | -48.58578 | 2025-10-25 04:19:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dc1dabc-c62a-35f3-aae6-50c59ceae9d8 | -9.71613 | -45.42349 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a58aaa6-e3e8-3b3a-971f-fc217b47319b | -6.90525 | -45.17194 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0b36e13-c05b-317d-a844-f9b239f7328b | -12.79689 | -48.67506 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b5e895f-fcf0-3699-afd8-5ce352fdc765 | -12.80041 | -48.67563 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 812d91b4-6b50-3c7d-a8ae-e7a76fd78fee | -10.41495 | -44.49658 | 2025-10-25 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25b034d6-5e6f-36d8-bff6-9fdda7d3b7f4 | -11.05876 | -48.33219 | 2025-10-25 04:19:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04a11668-5ca0-32c9-95cf-99f9e4b13c75 | -7.02618 | -43.92979 | 2025-10-25 04:19:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a9b826d-9331-3f5a-873e-5811e0addbc8 | -12.89854 | -48.58839 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6382b9a7-305d-3aa9-a0f3-8a93bdca6804 | 1.63738 | -55.74257 | 2025-10-25 04:19:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a45ef00e-9b05-32f8-b99c-1581e425f582 | -10.41884 | -44.49355 | 2025-10-25 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b88b2a3-9c65-3fd5-8400-315c1895bbcc | -13.0631 | -43.84628 | 2025-10-25 04:19:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4766aeee-79a3-3ba6-86e2-f99343b478dd | -9.17589 | -48.84839 | 2025-10-25 04:19:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57e73053-9955-3a47-ab4f-1314ad6f2fa7 | -7.99012 | -49.25744 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 022bfaae-149a-3ccb-9c47-6b6560628932 | -9.58023 | -45.18725 | 2025-10-25 04:19:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37216104-f6e6-3e97-a0b2-b6a88f713db6 | -12.04229 | -54.23837 | 2025-10-25 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81fd07dc-9d99-3287-a001-fff9ae03035f | -6.97444 | -46.42855 | 2025-10-25 04:19:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14b9df64-50fa-3d1a-9297-aee30902346a | -12.10838 | -46.70382 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7aa123b4-8683-3999-ba8e-c36e82ab67c1 | -13.00388 | -48.54418 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74b86328-1ecd-3228-80ca-a1bd0bfc1ba2 | -10.91164 | -50.16808 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2d77f7b-5687-3560-9284-44c03bbee8f7 | -11.5591 | -54.5227 | 2025-10-25 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1ebf4e0-9089-3b47-ac28-f2014c5c7f2d | -9.61623 | -46.90181 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96aa15df-3511-3838-a525-6a296a5498a1 | -7.00698 | -43.46807 | 2025-10-25 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ccda801-ac0e-3680-805e-190c2d8d5764 | -9.61738 | -46.90195 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08ecf5af-6e8f-3190-9814-5329838db6e7 | -12.16431 | -47.00986 | 2025-10-25 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0c503af-5ccc-378e-b843-6e3c23c3ef50 | -11.96005 | -47.63959 | 2025-10-25 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7e6df48-f21f-3477-a198-751c4ff37c24 | -12.41943 | -46.88322 | 2025-10-25 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a40a474-c49d-38c7-8887-39b9411ddf91 | -6.11196 | -49.03754 | 2025-10-25 04:19:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15fa43ec-cd95-3f81-b624-52866e97cef8 | -6.91518 | -45.17353 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c1da1b3-3940-3ffa-9aee-1f055403c8e1 | -7.64646 | -42.17282 | 2025-10-25 04:19:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8ced9e29-2d1e-3899-b610-da531ce99b1e | -5.56867 | -49.97857 | 2025-10-25 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 374ceb26-172b-392b-a206-ab4476090ad9 | -8.60674 | -54.95759 | 2025-10-25 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88ab2c8b-7bcd-307c-88c1-056dcad66e94 | -6.91573 | -45.17006 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 58c0f8ca-2bd8-3561-a946-894db80e5310 | -13.42831 | -47.26523 | 2025-10-25 04:19:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1236685-86dc-36f4-a4b6-d9a3e6ca94ac | -7.64454 | -46.88253 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bed62a95-6c33-3310-8391-91b14dc14504 | -12.29583 | -47.45422 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f258dce-fec5-3cc3-9922-f9774c13e2ce | -7.44837 | -47.20357 | 2025-10-25 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c212c268-91e3-3d8d-828b-383c296f80e9 | -13.09593 | -47.0068 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb55c9e3-094c-3b7d-be40-89388e30b6cb | -10.68428 | -48.07543 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b85cd9c8-7f27-34f1-80b3-2004d14472f8 | -6.60921 | -44.20702 | 2025-10-25 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README39.md)
