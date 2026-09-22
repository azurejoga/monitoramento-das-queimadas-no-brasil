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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 267f7ae2-c456-3d80-92fe-e1a5d920a3ce | -3.713 | -60.5642 | 2026-09-22 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 403a77e3-4bbd-3ab4-97b8-ee391d69395b | -9.977 | -50.248 | 2026-09-22 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| f174af0a-45d8-3d62-b9aa-f0b364eeeea0 | -6.1111 | -57.6645 | 2026-09-22 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 182.5 |
| 414d502d-3212-3f61-91a0-3d6e7b9101f1 | -8.845 | -45.9391 | 2026-09-22 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 94fc6413-12c1-3040-9a98-6ec46f2e3f9a | -10.7248 | -50.8109 | 2026-09-22 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.2 |
| efcbe58f-77a7-3a3c-9d2f-95e3f62bdc1d | -6.5449 | -44.8871 | 2026-09-22 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 10c39e65-911c-382d-84ec-5caa85d2a997 | -6.295 | -47.6055 | 2026-09-22 15:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 14da936b-13c0-3bd0-96ea-045d7f28ee83 | -9.5356 | -47.9349 | 2026-09-22 15:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 04e2f34a-0353-3caa-b30e-5273c23acaa2 | -3.6032 | -60.5853 | 2026-09-22 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a828e2c9-ec54-32b7-a553-2d91a37bec85 | -12.2827 | -50.7226 | 2026-09-22 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 45cbe329-9909-3816-9cfa-0e988d50c925 | 4.1314 | -61.2945 | 2026-09-22 15:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 55481950-fa9f-33dd-8717-d42b8743270b | -10.8746 | -50.9227 | 2026-09-22 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 33928ddb-bd1b-36ab-820c-975fa9b634d2 | -3.3309 | -59.8673 | 2026-09-22 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 2995938b-c6a5-394e-bdae-c2ac8709228d | -6.3134 | -47.6261 | 2026-09-22 15:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 131afef5-964e-3f26-81ec-2c9745c5c243 | -1.9484 | -56.5868 | 2026-09-22 15:20:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 6085d9c3-45e8-309f-b567-ea21a936e308 | 3.0563 | -60.0629 | 2026-09-22 15:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f607b16f-185a-38e9-99f7-a69e77653b01 | -2.5873 | -57.3965 | 2026-09-22 15:20:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 75c1b172-6e0a-3aee-904e-131e795fd1e7 | -6.8985 | -41.6976 | 2026-09-22 15:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 237.0 |
| c58b4bab-78bb-3a37-a45d-e33ee9c028de | -10.379 | -54.3979 | 2026-09-22 15:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 755be66f-bd91-3fae-b147-edfd0a0d39e5 | 3.7498 | -60.4684 | 2026-09-22 15:20:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 935530f2-04ca-38bb-b496-52f49f5c1baa | -5.8159 | -57.7346 | 2026-09-22 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| b667d66c-fbf5-3214-8e1a-89c11dbb9ed3 | -10.6875 | -50.7722 | 2026-09-22 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| b85b4bd1-be5b-39fc-9eef-9201945cbf62 | -3.3138 | -59.4472 | 2026-09-22 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 97b2ea7d-0ed6-3b26-9414-83cf57224196 | -10.8941 | -50.8782 | 2026-09-22 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 5069fa6e-cab2-367e-868d-dc7547ed5861 | -8.8146 | -45.3762 | 2026-09-22 15:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 5a7b9bb5-c3c0-3369-a082-50d1e8eb3d75 | -10.8343 | -54.0933 | 2026-09-22 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| fecda808-36fb-304a-bd47-7082d312a71c | -2.9709 | -57.7197 | 2026-09-22 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| cdc2e1e2-f15a-3ab6-a361-a0c1608f1020 | 2.4397 | -50.9344 | 2026-09-22 15:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 634d9bff-9586-3c79-a1ee-9f7f74340d40 | -6.8448 | -55.5411 | 2026-09-22 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 56cd1858-b1b3-3483-9b09-d261c13477e4 | -8.1304 | -62.8763 | 2026-09-22 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 3e5f6ea7-7af8-3b42-92d7-0d1d732c9bc9 | -3.3311 | -59.8101 | 2026-09-22 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ecca33f5-51a7-3e32-bc74-287a545cbefa | -3.5136 | -59.9401 | 2026-09-22 15:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 5033c358-d9ac-30dc-adbd-7a60d3015b73 | -12.4182 | -45.0385 | 2026-09-22 15:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 251.2 |
| acda6e27-45ea-390c-8630-70965bf0128b | -10.5748 | -46.7296 | 2026-09-22 15:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 204.6 |
| 58957e21-6a9f-3e20-91db-1e4e5bb1d999 | -6.4302 | -59.9724 | 2026-09-22 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 118.4 |
| fe156f42-f4bc-3d0a-9b72-ef32fd00a160 | -3.3321 | -59.4469 | 2026-09-22 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2749069e-56ff-3dbd-9440-d2fcc3879b00 | -6.8031 | -59.1886 | 2026-09-22 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 0d0dbea3-0f86-3eaa-8f18-6f69adc8d7ce | -3.1851 | -59.6982 | 2026-09-22 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 91d57939-c2af-3b67-b7f6-504e0817ad90 | -3.0534 | -61.2767 | 2026-09-22 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 4ffde637-605f-3cc3-a86b-c820b26ce43b | -10.3916 | -50.2916 | 2026-09-22 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a19ef091-837c-3e13-a0dd-7d960b8fe8cd | -9.247 | -57.1488 | 2026-09-22 15:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 100401ce-f9dc-3ec4-98d2-1ef2edc88617 | -2.9997 | -60.8047 | 2026-09-22 15:20:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| a0a9c244-89e1-3bf7-8754-43f21ebe1907 | -7.8715 | -54.7016 | 2026-09-22 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 2fe47828-3b60-3b4b-8b99-c7739fe880d5 | -10.379 | -54.3979 | 2026-09-22 15:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 01d0efef-af35-3094-ac40-47cade8246b5 | -8.3764 | -47.2802 | 2026-09-22 15:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| a2c10f69-f63c-39f9-91b5-de9bfaa6ed19 | -8.8146 | -45.3762 | 2026-09-22 15:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 208.1 |
| aeac302f-a8ac-3825-b82c-d800fb30f018 | -3.4635 | -58.3096 | 2026-09-22 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| a10b471e-e1ba-3c42-9cca-e6c827e5732f | -6.1838 | -47.5258 | 2026-09-22 15:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 96a96d28-8acb-3fa9-b783-d7a73e5aab8c | -3.2817 | -57.8685 | 2026-09-22 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 71ce1b96-5b51-34aa-85da-1029fd7ea481 | -11.1181 | -51.1091 | 2026-09-22 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 084a9043-f8ff-324c-b3f9-d802d81c7417 | -3.1902 | -57.851 | 2026-09-22 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 159d168a-b1c2-3b3a-801e-9b0d75f5eae7 | -6.295 | -57.735 | 2026-09-22 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 04d70165-54ad-355a-a388-8ba9df522820 | 3.9717 | -59.7202 | 2026-09-22 15:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 5fbf11e4-f825-3b46-840b-b6e8859e7f22 | -6.4302 | -59.9724 | 2026-09-22 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 127.2 |
| a7c97405-cd40-35b7-a3c2-a497aaf8f101 | 1.4453 | -50.7655 | 2026-09-22 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 8ab6c27c-6946-38c4-81f1-3e53a2564aa6 | -6.5056 | -45.0723 | 2026-09-22 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 8f8ff29e-0a00-36b5-acea-b17f04579e19 | -2.5687 | -57.494 | 2026-09-22 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| e4f8da92-dcf1-346c-87e0-95ba797aaaa8 | -6.5761 | -45.5194 | 2026-09-22 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 3facd80b-dce4-3645-8533-f00d2d5a901b | -3.3 | -57.8681 | 2026-09-22 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 60d172cd-a888-3ca8-89ff-45fe2d4af09b | -10.6187 | -50.268 | 2026-09-22 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 3db3b9bb-4544-3ddb-96e7-f32dc57a71b3 | -3.713 | -60.5452 | 2026-09-22 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f0e70e6c-59d1-3144-8795-77d24874f9da | -5.9148 | -53.5372 | 2026-09-22 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| da199748-a94e-3187-80fc-f159e6d51e5f | -3.387 | -59.4266 | 2026-09-22 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| cb64f542-a324-3bf4-bd1d-22688e15abe5 | -3.4186 | -61.2895 | 2026-09-22 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 57ac24ad-3e1a-32f3-be58-6921f70773e8 | -6.2916 | -55.2895 | 2026-09-22 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| d61a8784-2e26-34bc-9acf-4f9de6bed891 | -3.4241 | -59.2535 | 2026-09-22 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| c4ac5d1c-fd0c-32ab-a6d7-ced532307fea | -8.2229 | -62.8728 | 2026-09-22 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| f8417637-3ae9-32c1-b843-981c69c2d56d | -10.2976 | -50.2585 | 2026-09-22 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| a27ea8ed-1ada-33ac-aa17-f6d00f1c5fdf | 1.5287 | -55.7468 | 2026-09-22 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| bda854a0-bf88-3c0e-9f4a-94e859f5e611 | -3.331 | -59.8483 | 2026-09-22 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 6a1e5f2f-7417-3406-bacb-1c379255fcfc | -6.9849 | -59.663 | 2026-09-22 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| fc56e813-a232-31f7-80f6-0528e264eda1 | -3.6448 | -58.9031 | 2026-09-22 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 9b2c69f2-2cd4-3bab-b0a7-45586308bb58 | -2.9326 | -58.3397 | 2026-09-22 15:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 9c7a9a3f-4105-3b9f-9b5b-a2df943c1d7d | -2.8534 | -60.9206 | 2026-09-22 15:30:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 0f80d662-18b5-3830-a05b-a00e0796c7b0 | -10.8848 | -50.1754 | 2026-09-22 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 9fa221b8-26eb-3850-b28a-7f72498c020d | -6.7463 | -59.4416 | 2026-09-22 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 3268f9a0-6ec7-3fd7-84ff-744266ada57d | -6.3012 | -59.9962 | 2026-09-22 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 88396da0-a303-375c-ac30-530564cac980 | -5.3838 | -55.8857 | 2026-09-22 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 7eabc89f-717c-3f05-9ee8-3639f4f6a558 | -3.713 | -60.5642 | 2026-09-22 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 31e4ca7e-e1d2-3bf5-a6e7-ea2e0ccc5a87 | -5.8411 | -53.5002 | 2026-09-22 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| fa3a066f-a809-3246-9a58-cc0fb636e5f9 | -6.5243 | -45.0708 | 2026-09-22 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| cdd3455c-3545-3829-acff-75bc4648abd6 | -7.0029 | -49.7551 | 2026-09-22 15:30:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| e4a302e5-7eb8-308e-931b-b19c4f838e8d | -6.3842 | -55.265 | 2026-09-22 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 654f1c53-6de9-3598-90b8-e91488711615 | 1.547 | -55.7466 | 2026-09-22 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 2aeb1de9-5be2-3b17-9ec7-ab43ab877fde | -2.4206 | -58.2905 | 2026-09-22 15:30:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| eb05ebd8-1a57-35f6-a276-3b56a7fdfd4b | 2.7086 | -60.2969 | 2026-09-22 15:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ed00c7b7-641e-3d1a-8682-591b72d6bb03 | -3.2955 | -59.4476 | 2026-09-22 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| bf949d34-3754-3a25-8600-2830e3e0b32f | 1.9497 | -55.8992 | 2026-09-22 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| b974b9bf-d08f-3d2c-ae67-cde7b9bf2ba5 | 3.9168 | -59.7023 | 2026-09-22 15:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 192cc497-9caf-3cdf-8030-e669dacee045 | -3.4003 | -61.2898 | 2026-09-22 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 9cb5433a-d81c-3636-82a4-69045f71d2a9 | -6.728 | -59.423 | 2026-09-22 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 4cfb7981-b305-3754-97bf-e24d0e28482c | -5.6223 | -43.3701 | 2026-09-22 15:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 1f29f1b3-570d-37fd-bd30-c566c2ded645 | -3.6449 | -58.8647 | 2026-09-22 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c29ff8e3-1737-3db1-a47f-e15f85896d10 | -10.6878 | -50.751 | 2026-09-22 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 127.1 |
| b8390af0-2c37-3c8e-9239-ea414257ae1e | -3.5528 | -59.0397 | 2026-09-22 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| a0d7e053-42b4-30be-8298-7bc02675f387 | -5.4363 | -60.2161 | 2026-09-22 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 2493767b-10fa-339a-beec-a9cd2dced32d | -3.6032 | -60.5853 | 2026-09-22 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| afc22711-5e2f-3c69-9cd5-95aa0d6ed821 | -8.9016 | -45.933 | 2026-09-22 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 434945a6-abe0-3d16-a9dc-b862d9f11478 | -12.283 | -50.7011 | 2026-09-22 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 99f41a7a-30e7-39e0-8bdd-61cb16477ead | -9.859 | -46.4114 | 2026-09-22 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 178.3 |


[Clique aqui para ver as próximas entradas](README151.md)
