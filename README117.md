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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f29e4d0-38bf-31f5-8762-7e657b106f47 | -11.6334 | -48.3736 | 2024-10-13 11:56:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| d6936aeb-f3d3-342e-b8d3-7339cb2d8aa2 | -11.9251 | -45.7797 | 2024-10-13 11:56:14 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 66fa1946-5120-3321-aa54-65854d5769b8 | -11.9443 | -45.7769 | 2024-10-13 11:56:14 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 0bbed9c4-844b-38bc-82c9-11ed919e59fa | -17.9 | -57.36 | 2024-10-13 12:03:44 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bec018f5-9368-3dd6-a867-3a1b55792ae4 | -12.18 | -50.75 | 2024-10-13 12:04:15 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 576a5749-97f6-347a-8d38-c6a219c345aa | -10.95 | -44.7 | 2024-10-13 12:04:21 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 515a41b0-1d1b-34bb-ba0f-1d41b8734894 | -10.92 | -44.69 | 2024-10-13 12:04:23 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a05293af-9658-3b54-a04d-cb1205fc0070 | -9.9604 | -47.2705 | 2024-10-13 12:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 51dcd64f-0d80-3439-916c-e0ee0c37f91d | -10.1637 | -46.3079 | 2024-10-13 12:06:04 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 86168973-6f92-39e7-a6de-4e962776f240 | -10.1827 | -46.3056 | 2024-10-13 12:06:04 | GOES-16 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 5ac9f122-0f95-3add-8b61-79ef8778ed49 | -10.9311 | -44.6789 | 2024-10-13 12:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 458.6 |
| 7c46c6df-c895-342f-8e3e-e0ac999c89f7 | -10.9502 | -44.6762 | 2024-10-13 12:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 0785becb-2f10-3af7-8efe-dbb96fdbc043 | -10.9315 | -44.6557 | 2024-10-13 12:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| f27ffd30-ba64-3777-9a3e-4f2502067da7 | -10.9116 | -44.7048 | 2024-10-13 12:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 70753c5d-30d7-3836-bc04-8b2e2ae80193 | -11.6334 | -48.3736 | 2024-10-13 12:06:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 63b37376-c76d-3fc8-ac90-afd8d36879c7 | -12.1685 | -50.7147 | 2024-10-13 12:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 3635c829-02e4-3aa9-80ab-8ef63e7ae3b0 | -10.1634 | -46.3304 | 2024-10-13 12:16:04 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 5517983e-219f-36d1-987f-340190cd31f4 | -10.1827 | -46.3056 | 2024-10-13 12:16:04 | GOES-16 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 0edb55db-c55c-3384-8e93-54dad450d21b | -10.1637 | -46.3079 | 2024-10-13 12:16:04 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 3ccdd9fb-8669-3955-8f1c-9b3a63a0d51a | -10.3127 | -46.4923 | 2024-10-13 12:16:05 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| ec36e071-502c-3280-a297-07c0bf092791 | -10.9311 | -44.6789 | 2024-10-13 12:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 429.8 |
| 764794fa-bfc3-3ae2-8ed2-e76952cedf8a | -10.9502 | -44.6762 | 2024-10-13 12:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 502ac87d-ecfa-3821-a1bc-862a12298f5c | -10.9315 | -44.6557 | 2024-10-13 12:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| bc795356-2abf-3eb4-b2f6-d6900d8c72f6 | -11.6334 | -48.3736 | 2024-10-13 12:16:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| a312d936-4f46-3d76-9a7a-4d1d319684e0 | -9.5182 | -47.8269 | 2024-10-13 12:26:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 2d8780d2-f4de-3868-9c4e-c05c5ba03860 | -10.0633 | -44.1692 | 2024-10-13 12:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 227.1 |
| ec88aced-d48e-31c8-bb4a-12cd5a2645ac | -10.1637 | -46.3079 | 2024-10-13 12:26:03 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 48a42649-17ec-384c-98d4-64bab962b992 | -10.9311 | -44.6789 | 2024-10-13 12:26:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 320.7 |
| 28a76879-71cd-3a15-8a42-49bfaa990150 | -10.9502 | -44.6762 | 2024-10-13 12:26:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 25e297df-e13b-33ab-a14e-eab0434f7597 | -10.9315 | -44.6557 | 2024-10-13 12:26:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 0c95fdf5-98f8-3210-a923-c35da25dacb9 | -10.9116 | -44.7048 | 2024-10-13 12:26:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 82e82545-74b9-3020-b7f6-f23187ca6971 | -11.6334 | -48.3736 | 2024-10-13 12:26:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 13874731-e474-33c7-918b-79c50dc497dc | -10.0633 | -44.1692 | 2024-10-13 12:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 197.9 |
| 24c3c969-4d7d-3924-a8ce-e17cb0a2f7fb | -10.2594 | -46.2512 | 2024-10-13 12:36:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 301b6578-7e4e-3701-ba08-2d88d62815de | -10.2597 | -46.2286 | 2024-10-13 12:36:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 0dfc850b-27bb-3be0-bedd-1a31deb21ae6 | -11.6334 | -48.3736 | 2024-10-13 12:36:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 09b042e2-00fb-3257-ad7a-8ed214ebe563 | -12.0737 | -50.6831 | 2024-10-13 12:36:14 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 51458afc-61e6-3fed-8b4f-0da68ef40aa2 | -9.9604 | -47.2705 | 2024-10-13 12:46:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 8852afeb-d718-353f-82f6-52c69647a844 | -10.0633 | -44.1692 | 2024-10-13 12:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 202.6 |
| c6d01702-c9e1-3802-ab5d-ba493eec2e31 | -10.1827 | -46.3056 | 2024-10-13 12:46:04 | GOES-16 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 55569010-75ed-3e6e-bd84-fbb9581f88a0 | -10.1637 | -46.3079 | 2024-10-13 12:46:04 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 038ed947-fb9a-3cd3-8e2e-1841b7807674 | -10.4905 | -49.9604 | 2024-10-13 12:46:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 0b83d671-7e9d-32a3-b805-769816a12eb4 | -11.6334 | -48.3736 | 2024-10-13 12:46:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| e5aa7ef5-4274-3d86-bb1e-e85c35652c1d | -11.633 | -48.3956 | 2024-10-13 12:46:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 0372f34e-04e5-3e51-abfa-5452ae37407e | -11.9443 | -45.7769 | 2024-10-13 12:46:14 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 77625c4f-02c7-3c1b-86ae-0f9c0d08cfe7 | -12.0737 | -50.6831 | 2024-10-13 12:46:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 6d3b9b22-5f65-3a09-b2b2-8a1409491aed | -13.2514 | -51.1168 | 2024-10-13 12:46:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| ef6d80b3-55f3-3b82-8f18-a0045ba70018 | -13.2517 | -51.0953 | 2024-10-13 12:46:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 996a8fe9-d4ce-352b-b8b3-2f433a6b60f1 | -9.4554 | -45.509 | 2024-10-13 12:56:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 43fd2ab6-68b2-359f-988c-13cbff87e045 | -9.4365 | -45.5112 | 2024-10-13 12:56:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| c306230a-bd6b-3464-bcb8-5a4839869f58 | -9.9414 | -47.2727 | 2024-10-13 12:56:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| d7fa1b36-a948-3a96-96d4-a575ce39ea50 | -10.0633 | -44.1692 | 2024-10-13 12:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 196.9 |
| d3975ac6-3dca-3917-ac63-3174d2bea2ea | -10.4716 | -49.9624 | 2024-10-13 12:56:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 68e035ab-f3df-3c61-b2c1-0d9f7fafe2e1 | -10.4905 | -49.9604 | 2024-10-13 12:56:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 0dfa4253-2d44-3cd1-97bf-f96e07e6f902 | -11.7373 | -44.4926 | 2024-10-13 12:56:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| e8e6354e-6bc7-3458-9d00-5ae1694787a9 | -11.6334 | -48.3736 | 2024-10-13 12:56:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 94aec95a-3637-322d-a6ae-5ce3d774f59d | -13.2517 | -51.0953 | 2024-10-13 12:56:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| ee62b493-7a16-3ad3-9047-ed01d1dcda50 | -17.87 | -57.34 | 2024-10-13 13:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 24b3df4a-c471-3002-9d10-707017b3333c | -17.9 | -57.36 | 2024-10-13 13:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| efb4911b-7aa2-37d4-baff-bb7222e7e3c2 | -17.9 | -57.28 | 2024-10-13 13:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bace7927-43f0-3c2b-b119-ab63ef06444b | -17.93 | -57.38 | 2024-10-13 13:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ff81bfa2-92d8-3f57-977f-c3ff9b83e796 | -12.15 | -50.74 | 2024-10-13 13:04:14 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 490767b6-bbdc-3715-9fb8-7dc8f2798b7e | -12.18 | -50.75 | 2024-10-13 13:04:14 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ce1a62b-e93b-3f65-9e3a-6f2a2bd72fdd | -11.28 | -46.07 | 2024-10-13 13:04:20 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3fc3b4ee-fc88-3251-acc5-a6a61eca3cdd | -10.95 | -44.75 | 2024-10-13 13:04:22 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 04c23734-b78a-3c26-afec-8d4e456f531c | -10.95 | -44.7 | 2024-10-13 13:04:22 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bb4f8d45-151a-3957-8c41-90921e5cc86d | 3.5242 | -51.7743 | 2024-10-13 13:04:46 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b1675158-852a-38d2-9959-07602c7c1d58 | -4.4 | -44.48 | 2024-10-13 13:05:02 | MSG-03 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75be10ca-66fa-352a-bb0b-b8dcc5469bc1 | -9.4365 | -45.5112 | 2024-10-13 13:06:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 16f203d9-809e-3a57-b90f-5d1a19e9d489 | -9.4554 | -45.509 | 2024-10-13 13:06:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 825cc957-e7d5-3c88-a19e-e79aa8cdca17 | -9.4373 | -44.1321 | 2024-10-13 13:06:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 206dd205-372f-326f-88d8-7bac6b413203 | -10.0633 | -44.1692 | 2024-10-13 13:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 247.8 |
| 2c815c16-520a-36a9-b761-7fcfd57d1deb | -9.9604 | -47.2705 | 2024-10-13 13:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 95a4c6ae-51a5-3032-9593-c0df40c2bc5e | -9.9414 | -47.2727 | 2024-10-13 13:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 9a609052-992b-3045-ab65-b0fc4f455752 | -10.1827 | -46.3056 | 2024-10-13 13:06:04 | GOES-16 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| bcb35895-7b9b-3fb5-a7f0-50ca69c97f57 | -10.2597 | -46.2286 | 2024-10-13 13:06:04 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 5091eac6-5cfe-3bdd-8914-21d49c8dfa51 | -10.1637 | -46.3079 | 2024-10-13 13:06:04 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| b53ba9a4-15bd-31f1-8174-7a6d2e42dbd6 | -10.5281 | -49.9778 | 2024-10-13 13:06:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 6bcbbb6c-4304-30ab-94d0-311d861dc05f | -10.5283 | -49.9564 | 2024-10-13 13:06:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 3bb3ddfa-f886-3e3c-b42f-7cdbe5bd8b50 | -10.5278 | -49.9993 | 2024-10-13 13:06:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 4606e04d-e6d4-3c6a-90f3-cbf40c6f122e | -10.4905 | -49.9604 | 2024-10-13 13:06:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 2665a375-3334-354a-8e26-b07ea75cb8d9 | -10.4716 | -49.9624 | 2024-10-13 13:06:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 1cb31dcb-9d59-39ee-b7c2-037915e6a0f6 | -10.7572 | -39.3835 | 2024-10-13 13:06:06 | GOES-16 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 101.1 |
| de889d09-e1ff-38db-a532-c4aec6cbd9ce | -10.9506 | -44.653 | 2024-10-13 13:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| c33a9253-b18a-3512-a4f5-ad9d00963569 | -10.9116 | -44.7048 | 2024-10-13 13:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| a5063551-322f-3371-ac63-95f0cff9a735 | -10.9311 | -44.6789 | 2024-10-13 13:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 756.6 |
| 52166742-ca51-3010-9c08-b8e9b1536825 | -10.9307 | -44.7021 | 2024-10-13 13:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1278.7 |
| 7f07a6c9-d0ac-3c1a-885a-380135f71c29 | -10.9502 | -44.6762 | 2024-10-13 13:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 334.6 |
| e577c10a-bc16-36fb-9b7d-a11ef42b4f01 | -10.9315 | -44.6557 | 2024-10-13 13:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 12253a38-df7e-31cb-a1f1-f2c57de4b9e1 | -11.7373 | -44.4926 | 2024-10-13 13:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 70e1b4d0-4b3c-33f9-bc3b-3dfafdfe56fe | -12.1895 | -50.5838 | 2024-10-13 13:06:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 999eef53-b1ff-3da1-8bdf-a9519e300a99 | -12.1704 | -50.5861 | 2024-10-13 13:06:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 5183dd47-8426-30b7-aa65-99452e80e8cd | -12.0737 | -50.6831 | 2024-10-13 13:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 220.8 |
| ac21c8ae-a3d4-3639-977a-d463de1e00e0 | -13.2517 | -51.0953 | 2024-10-13 13:06:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| ca266032-cc8b-3d9d-9aa4-2afd38223e7f | -9.4365 | -45.5112 | 2024-10-13 13:16:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 53f2eceb-ed50-389b-b63c-814dced03718 | -9.4554 | -45.509 | 2024-10-13 13:16:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 50e5c41b-68dc-3562-a308-3c832042809e | -10.0633 | -44.1692 | 2024-10-13 13:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 239.4 |
| eb1f2009-a935-3f5e-a697-d80befe8539f | -9.9414 | -47.2727 | 2024-10-13 13:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 02dcda81-b41e-3634-8e32-3a214ad7363d | -9.9604 | -47.2705 | 2024-10-13 13:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| cd0c6b29-15f6-3314-a0fe-74dee8068be3 | -10.1637 | -46.3079 | 2024-10-13 13:16:04 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |


[Clique aqui para ver as próximas entradas](README118.md)
