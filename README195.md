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

## Dados Diários - Página 195

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 457294c5-7d0c-3ff2-8393-f8b8c42aee05 | -3.8144 | -48.9729 | 2024-10-25 19:05:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| bb889eda-b5c5-3052-91db-3179aea16a73 | -3.9 | -40.7483 | 2024-10-25 19:05:27 | GOES-16 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 246d8a12-f843-3ef6-aef8-79b0b9fee9b8 | -4.0898 | -43.1901 | 2024-10-25 19:05:28 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| c559bb0a-7bc1-3996-a1f1-591a7fc3d6ce | -3.9804 | -45.7977 | 2024-10-25 19:05:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 0577e9b8-d1fc-37f3-b6d4-a992cd4866c9 | -4.029 | -43.9348 | 2024-10-25 19:05:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| d70cfaf4-7e03-3fc9-9fa5-c329df6d7589 | -4.2126 | -44.384 | 2024-10-25 19:05:29 | GOES-16 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 63bc6d17-e03e-331f-ac1a-7e7689e1525b | -4.1416 | -46.8331 | 2024-10-25 19:05:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 2ad20d5e-cd22-35df-8e65-735d7f2a6ef3 | -4.3351 | -48.6292 | 2024-10-25 19:05:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| a26af877-87e4-3060-a510-7624ba076ab6 | -4.5912 | -56.0924 | 2024-10-25 19:05:31 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| a7bd9146-1310-3b5d-9368-ab683f2ff651 | -4.5029 | -45.5917 | 2024-10-25 19:05:31 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 28300f28-7b2a-371d-bd65-ecf57e1b73cb | -4.7445 | -45.6679 | 2024-10-25 19:05:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 543da369-1080-3e20-8b40-3f4fba94f8bd | -4.8735 | -48.5598 | 2024-10-25 19:05:33 | GOES-16 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| ef850be9-e459-344a-b43c-8ea844d66458 | -5.1211 | -45.1722 | 2024-10-25 19:05:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 318.7 |
| 2e031a1c-db06-3e03-b5af-b82cef6acda4 | -5.1129 | -43.8471 | 2024-10-25 19:05:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 8b76c4ac-247a-3719-90d5-7be9241e0861 | -5.1012 | -45.3315 | 2024-10-25 19:05:34 | GOES-16 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 5ecd1250-eb97-3d55-8990-a5c7c851a1be | -5.0769 | -43.6644 | 2024-10-25 19:05:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| e14b6453-b5bd-3c45-b2ae-f4fd525479a9 | -5.2102 | -48.2178 | 2024-10-25 19:05:35 | GOES-16 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 311f00ff-0cc0-3252-ac39-6595a3449d3a | -5.2838 | -48.3218 | 2024-10-25 19:05:35 | GOES-16 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9e30237f-2566-3d17-93bb-7198c694b5e4 | -5.3017 | -41.4526 | 2024-10-25 19:05:35 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 4bf31dbf-df17-37a7-887f-c8e6e97391bd | -5.4447 | -44.4224 | 2024-10-25 19:05:36 | GOES-16 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 57740da8-370a-3fd8-bd2b-8f381c73a950 | -5.7014 | -45.0199 | 2024-10-25 19:05:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 0dbd1413-6e3e-316a-a704-8daa8010480f | -5.5815 | -43.7448 | 2024-10-25 19:05:37 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 1966d606-c245-3e68-82a7-93a964b37166 | -5.7201 | -45.0186 | 2024-10-25 19:05:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 33e584c5-9aed-3365-aa9a-53e3a2c16c24 | -5.7648 | -44.1929 | 2024-10-25 19:05:38 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| b200417b-261b-3e84-bea5-a86699bc7951 | -5.7039 | -49.3066 | 2024-10-25 19:05:38 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 19d1f462-1b5b-33bd-b72e-b639dd9c410d | -5.8961 | -44.16 | 2024-10-25 19:05:38 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| cab6abd7-be39-3304-951c-8c1bb58e720d | -5.9873 | -44.4286 | 2024-10-25 19:05:39 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 17e5611d-36e2-38a7-824e-ec5d9f7eea1f | -6.2744 | -47.8253 | 2024-10-25 19:05:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 179.4 |
| a833df4b-67a9-3e14-9e67-0ea6f2ce545e | -6.2742 | -47.8471 | 2024-10-25 19:05:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 02c17b26-b9fd-3a6a-868d-390383a13b29 | -6.3758 | -39.5189 | 2024-10-25 19:05:41 | GOES-16 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 272ba2d9-27df-3597-a403-6711169c730a | -6.2931 | -47.824 | 2024-10-25 19:05:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 500.8 |
| b9ef50ed-a221-3e4d-a1ed-f36ebaa963ae | -6.5054 | -47.0414 | 2024-10-25 19:05:42 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 03064a77-7d0c-3b6b-97ca-86cf639ee174 | -6.5266 | -62.9483 | 2024-10-25 19:05:43 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| c75c668b-d13a-36f9-86f5-24cf867538d5 | -6.5219 | -60.0457 | 2024-10-25 19:05:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 0952e346-28e5-307c-b312-f9fd4d759383 | -6.7045 | -43.9554 | 2024-10-25 19:05:43 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 866292a8-756f-3744-81e2-cbf8aab42ddc | -7.1092 | -46.5065 | 2024-10-25 19:05:45 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 844eb3d4-2f62-365b-961f-ce1f34db8bce | -7.179 | -38.8281 | 2024-10-25 19:05:45 | GOES-16 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 6d35cfe5-af02-37f0-a6de-66f541ee5d7d | -6.9275 | -60.0303 | 2024-10-25 19:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.9 |
| f4a300ac-0825-3b63-82ce-72bacafbaabc | -6.9952 | -46.6714 | 2024-10-25 19:05:45 | GOES-16 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| b496b47a-d883-34f8-af39-ad0fec2f9139 | -7.2073 | -47.9087 | 2024-10-25 19:05:46 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| dc889f23-e5a9-34c4-862c-cf641536efeb | -7.1673 | -46.3233 | 2024-10-25 19:05:46 | GOES-16 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 866ebb12-f2d8-357a-bab4-2b397ea3782b | -7.218 | -46.8527 | 2024-10-25 19:05:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| bb7f708e-28ed-3472-ad94-5b4972da9cec | -7.1861 | -46.3217 | 2024-10-25 19:05:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 28d5ee47-958c-36f1-8392-10c50ee9ff5d | -7.5542 | -43.6437 | 2024-10-25 19:05:48 | GOES-16 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 7fa04bb7-b8a3-3681-a8b5-fb4a68d4aeb3 | -7.5477 | -45.8417 | 2024-10-25 19:05:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| ae373ca3-a92c-3339-9057-a7761c70513e | -7.8727 | -45.3593 | 2024-10-25 19:05:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 8ced1f0e-0947-33a9-8958-815b41653733 | -9.0635 | -48.0051 | 2024-10-25 19:05:56 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 143.0 |
| d59137c0-30ff-3983-8d6b-00f1e7fb9540 | -9.2024 | -43.3429 | 2024-10-25 19:05:57 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| e8d8260a-3ff6-3212-ba6f-04f7d6ca0c1d | -9.0824 | -48.0032 | 2024-10-25 19:05:57 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 283500d0-b3ca-3f01-a25f-ba406e270a32 | -9.6072 | -42.9371 | 2024-10-25 19:05:59 | GOES-16 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 193.5 |
| dd91f3a0-2691-3b80-ba54-eaf3d90295ac | -9.6082 | -46.7535 | 2024-10-25 19:05:59 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| e034399c-a2df-3834-aedd-e3dd3c1c576d | -9.6816 | -40.6535 | 2024-10-25 19:05:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 110.3 |
| 45c27f5c-b894-3d0c-a736-f205537bd35c | -9.9025 | -44.7455 | 2024-10-25 19:06:01 | GOES-16 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| b8211416-3786-309c-93c7-099d1f891514 | -9.9215 | -44.7431 | 2024-10-25 19:06:01 | GOES-16 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 64a1f210-1930-3dee-8232-18d448ab19b0 | -10.2599 | -47.5023 | 2024-10-25 19:06:03 | GOES-16 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 4ba6e83a-3de6-3e8f-aaad-ced06e78d8fb | -10.2596 | -47.5245 | 2024-10-25 19:06:03 | GOES-16 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 786e5241-cadc-356d-919a-329236f1434e | -10.5948 | -44.261 | 2024-10-25 19:06:05 | GOES-16 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 4085a9db-a864-3e0f-8924-f69f9338c05e | -10.6135 | -44.2817 | 2024-10-25 19:06:05 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 30db30c7-191b-36dd-bd6a-cdfb16cfc2b3 | -10.6139 | -44.2584 | 2024-10-25 19:06:05 | GOES-16 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 0addaf99-7329-32d7-b1d7-7ada069f0a57 | -10.8793 | -47.9378 | 2024-10-25 19:06:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 335ddf80-eff4-3ee6-986f-616c144f7248 | -11.5357 | -43.9853 | 2024-10-25 19:06:10 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 37822138-7b4e-3695-8fd4-90425229c49f | -11.9028 | -43.8348 | 2024-10-25 19:06:12 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| bb73e3ea-5dbd-3ac1-b7d3-3263ae407141 | -11.9642 | -44.6676 | 2024-10-25 19:06:12 | GOES-16 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 4744b470-156b-320d-8da9-6a35d593001c | -12.4612 | -43.7921 | 2024-10-25 19:06:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 2ba7c12e-0d7a-3bff-9a16-a791581d4b7b | -12.9693 | -43.469 | 2024-10-25 19:06:18 | GOES-16 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 4b58bd8f-cceb-37c9-9456-92f51b7e915f | -19.6229 | -56.8968 | 2024-10-25 19:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 157.2 |
| 7820c94a-1148-3ec2-a512-893558343773 | -19.6253 | -56.7709 | 2024-10-25 19:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 222f2728-1f53-3535-9efe-55c82019d3e3 | -19.6225 | -56.9178 | 2024-10-25 19:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 107.3 |
| 435b9ef9-cea4-333d-b62c-cc80c80f3d47 | -19.6453 | -56.7681 | 2024-10-25 19:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.2 |
| df8a47e4-13d4-3447-95c0-85a7b9c30dc3 | -1.0733 | -53.658 | 2024-10-25 19:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| d5a807cf-7413-3f6b-a2fb-218c32e7f231 | -1.1834 | -53.6569 | 2024-10-25 19:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| fd9f2ccd-edc2-34cb-a5da-982a75845e76 | -1.2762 | -52.9275 | 2024-10-25 19:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 68437b34-85d2-32b5-b331-bff07309a268 | -1.1834 | -53.6771 | 2024-10-25 19:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 10639cf6-5a05-3d02-b21b-38be7d4ab14d | -1.382 | -55.847 | 2024-10-25 19:15:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 0fba321a-1287-3309-933d-93b691e81a4c | -2.0232 | -55.7798 | 2024-10-25 19:15:17 | GOES-16 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| a44d5a69-0ea6-36ea-aecc-ac3d145f2c20 | -2.1534 | -54.9256 | 2024-10-25 19:15:17 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| ccb8e84b-dc74-333e-9629-2175bdc4f316 | -2.1129 | -56.6823 | 2024-10-25 19:15:17 | GOES-16 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| b763ab99-d6ec-3cf3-b848-51ca7ffe2de2 | -2.3056 | -46.637 | 2024-10-25 19:15:18 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| ff430120-20c7-3da0-ba7f-a0630761430a | -2.4251 | -49.7186 | 2024-10-25 19:15:19 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 3e0eaf39-faa4-3ce3-8891-d9b82cbc0bc5 | -2.6473 | -49.5013 | 2024-10-25 19:15:20 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 15f9ffff-02c4-3062-8726-7018f3720527 | -2.6473 | -49.5225 | 2024-10-25 19:15:20 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 49ec8e26-8228-3eb5-8468-284357a60731 | -2.6658 | -49.5008 | 2024-10-25 19:15:20 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| aee4b5b3-da8b-37c4-ac08-ef3f6b6fe369 | -2.6297 | -49.247 | 2024-10-25 19:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 35d85538-aa67-31e4-be24-b649610ddb19 | -2.6902 | -43.2537 | 2024-10-25 19:15:20 | GOES-16 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 9b1d35cb-f508-3fc1-bb5c-3e9be62b13f9 | -2.8502 | -44.9905 | 2024-10-25 19:15:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 41e89a49-3d2a-3924-be8e-2d79700463b8 | -2.8684 | -45.0803 | 2024-10-25 19:15:21 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 61718c15-bda0-3cd1-b211-44fd0d3cf2e3 | -2.9578 | -50.4198 | 2024-10-25 19:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| da3418c7-ac12-34b0-93ec-a0f70ee804df | -3.2172 | -50.1811 | 2024-10-25 19:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| bfb1ee6d-0d4b-31ee-81f1-9565063e62c9 | -3.2357 | -50.1805 | 2024-10-25 19:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 33cef4ae-71d5-3f7c-b2d8-ff9fb9f662a5 | -3.6381 | -55.5084 | 2024-10-25 19:15:26 | GOES-16 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 7ade831f-1c4b-3d3e-a624-760a5d838b2e | -3.7572 | -45.8081 | 2024-10-25 19:15:26 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| e657c7d7-f186-34c3-8996-c1872ac6875a | -3.5993 | -51.4619 | 2024-10-25 19:15:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 177.4 |
| 31ea023a-a4e8-3e13-a4c6-5bd1d3a132e1 | -3.8144 | -48.9729 | 2024-10-25 19:15:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 23ed621b-8302-3e0e-9073-2eb708c10eb5 | -3.9406 | -43.1515 | 2024-10-25 19:15:27 | GOES-16 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 88b688e8-907f-3525-ae48-01ea98091171 | -3.9804 | -45.7977 | 2024-10-25 19:15:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 280.8 |
| dd033e3f-294d-3804-9b8a-965dc3788ef7 | -3.9462 | -52.2538 | 2024-10-25 19:15:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 9e5c1a78-a7fa-334f-bf38-dbd519ebd082 | -4.1416 | -46.8331 | 2024-10-25 19:15:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| e9e316ba-9a4a-3fb7-8b3e-b5cda36363d9 | -4.3351 | -48.6292 | 2024-10-25 19:15:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| b5ef3744-8a07-3557-b60f-f8fa36e4d8c6 | -4.3349 | -48.6506 | 2024-10-25 19:15:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| ab692576-6e56-35f2-bfdd-1966f8a55461 | -4.4657 | -42.8877 | 2024-10-25 19:15:30 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |


[Clique aqui para ver as próximas entradas](README196.md)
