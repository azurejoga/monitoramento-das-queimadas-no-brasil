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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4600ee9-0bbd-3b9c-9e76-43cfeeabf8d0 | -12.322 | -47.1715 | 2026-07-27 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 9db34acd-fe31-3f2e-a90a-c1582f53125c | -13.6988 | -51.9125 | 2026-07-27 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| bf0366b2-c5db-3704-9df9-2345d2cf9c1b | -9.5466 | -47.1167 | 2026-07-27 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| fb450b22-d28c-3d9f-9d42-da8f96c3a689 | -11.4562 | -47.5338 | 2026-07-27 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| adad5866-fae2-3a22-a540-d342c666f49c | -13.1026 | -43.5647 | 2026-07-27 14:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| ab4ae60e-40c8-3572-b074-1abd68eb1bae | -11.4562 | -47.5338 | 2026-07-27 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 202e70fe-4f89-3eb1-9dde-bc3eb755dd64 | -9.5277 | -47.1187 | 2026-07-27 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 69d8cf09-9c51-352a-a526-2b479cd99763 | -12.3216 | -47.194 | 2026-07-27 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 151.7 |
| aae28ad9-96fd-3077-8db0-23c92483751f | -12.0432 | -47.8122 | 2026-07-27 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 6fe61dfa-8bfe-3d83-8748-25c48c98928e | -12.322 | -47.1715 | 2026-07-27 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 63b60048-d37e-37d1-9f14-2b5e19bdfe26 | -13.1026 | -43.5647 | 2026-07-27 14:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| a1a1f425-cfdc-3bf7-bc4b-28be5fc1cbbd | -13.0832 | -43.5681 | 2026-07-27 14:30:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| d1f039e9-216e-3b94-bbcd-6057415da60c | -13.6988 | -51.9125 | 2026-07-27 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 0a60d1e1-cc04-378b-92d3-259d35c87592 | -9.5466 | -47.1167 | 2026-07-27 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 3a026af2-6b1d-32c4-b070-cf2741341e40 | -12.3216 | -47.194 | 2026-07-27 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 153.5 |
| a399f6e8-5ef9-3249-86de-e1c07b1dd541 | -13.1026 | -43.5647 | 2026-07-27 14:30:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| a8872cb0-63b2-3cab-ba44-b4adbe22a126 | -12.3263 | -50.3742 | 2026-07-27 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| f404de44-d507-3758-b247-de365beddc7c | -11.4562 | -47.5338 | 2026-07-27 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 02592630-78b2-3a2b-92a3-e02f2f74473b | -13.1026 | -43.5647 | 2026-07-27 14:40:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 7a659502-e4a6-36e1-858b-b65770398df2 | -11.4753 | -47.5314 | 2026-07-27 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 0e23b0e4-7f56-39d2-a3fe-4413ba4b5642 | -12.3216 | -47.194 | 2026-07-27 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| c4d4eaa5-2a36-36fa-979c-d394ce83a8fc | -11.1542 | -51.2324 | 2026-07-27 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 9303d822-34d8-378c-a64f-87c227c7984d | -7.7093 | -46.499 | 2026-07-27 14:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 50874bb7-7151-30f2-b019-7978f7f7fb50 | -13.1026 | -43.5647 | 2026-07-27 14:50:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 7c7bf4c4-156c-30ba-a4e8-87533982bba9 | -11.1542 | -51.2324 | 2026-07-27 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| f8d11a71-c75c-3ec6-b182-cb659136eea9 | -9.5466 | -47.1167 | 2026-07-27 14:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 60f73dfd-b70c-3bac-8f4c-140f4fde31b3 | -12.3216 | -47.194 | 2026-07-27 14:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 94714ec8-bd80-394c-ad83-ea84d69c49a6 | -12.3259 | -50.3958 | 2026-07-27 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| f2d2f179-1c6e-3214-8935-cdc96d0e0f9c | -12.3216 | -47.194 | 2026-07-27 15:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 8c816005-dbe6-3e8f-9fee-57e505aace18 | -13.3746 | -54.2952 | 2026-07-27 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 4334731a-c1a4-3423-8a2e-2bee2233c2ee | -11.1542 | -51.2324 | 2026-07-27 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 05e7d09f-4932-398e-9f05-d6933ed86eba | -12.3263 | -50.3742 | 2026-07-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b72e3674-0b9a-33ff-b0b6-60dfc3df7147 | -11.5105 | -50.1914 | 2026-07-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 337c9792-bbda-3e36-8467-996d4e005210 | -12.3259 | -50.3958 | 2026-07-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 51824c6c-3745-32c3-b4a8-86c5d9e40b73 | -5.5909 | -42.6929 | 2026-07-27 15:00:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 3a4bc830-133b-3e93-a813-f222678c20e2 | -13.3749 | -54.2745 | 2026-07-27 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 7eb8da5b-0ca6-35bd-b6f9-5d71c69e0b4e | -14.3851 | -58.8756 | 2026-07-27 15:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 9a1b1d78-5d48-3005-8ee3-5425626573f3 | -9.5466 | -47.1167 | 2026-07-27 15:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 921f93f7-0a62-3930-b89b-a4079c785142 | -12.322 | -47.1715 | 2026-07-27 15:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 25b0d653-a951-3bb1-8104-d5ec7021512a | -12.3412 | -47.1688 | 2026-07-27 15:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 647f7aca-201d-3b9b-a317-35cdf90fcdff | -13.1026 | -43.5647 | 2026-07-27 15:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 1a3690b7-9499-3613-acc3-f3744edd0975 | -12.3263 | -50.3742 | 2026-07-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| cdc54b04-ba9c-3b3c-b4c2-453f75b3b0fa | -12.3216 | -47.194 | 2026-07-27 15:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| bac8c377-1ba6-3fb8-adbf-41c2e8ec531d | -11.5105 | -50.1914 | 2026-07-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 703caec2-514b-3317-9a90-0b95f6bb6c5b | -12.3259 | -50.3958 | 2026-07-27 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 7102a379-5c7b-374d-b89e-bce8f648e622 | -9.5466 | -47.1167 | 2026-07-27 15:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| d58a88ce-a176-3d57-9f37-a0ca11b0e243 | -13.1026 | -43.5647 | 2026-07-27 15:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 841339b2-8dd7-32df-966a-89b9d5d40972 | -11.5105 | -50.1914 | 2026-07-27 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| fd6638d3-a383-3b9c-af39-2270a55b95e6 | -12.3216 | -47.194 | 2026-07-27 15:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 19a3bf88-6253-3728-941f-d707e4c754c4 | -20.3255 | -54.0266 | 2026-07-27 15:20:00 | GOES-19 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 52a50c01-48ba-3820-b53a-61b4d37e53b3 | -11.1542 | -51.2324 | 2026-07-27 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.7 |
| a69041b5-55ff-3eb3-a763-208d48ed4f41 | -12.3263 | -50.3742 | 2026-07-27 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 210.1 |
| 7c85ffc5-8f8e-3114-9de8-140e3a254fac | -12.3259 | -50.3958 | 2026-07-27 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 7bada7e5-19c5-3c42-984e-f94d7ecdd4b7 | -5.5909 | -42.6929 | 2026-07-27 15:20:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 110.3 |
| f0df7f0c-fdc5-3eb8-b949-2e19b9e2e8b4 | -13.6988 | -51.9125 | 2026-07-27 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| b542cc1f-81ff-3e54-b773-e12bfb290c69 | -20.3255 | -54.0266 | 2026-07-27 15:30:00 | GOES-19 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 5206540f-87e7-386d-ba65-b4873631e805 | -8.8596 | -65.0308 | 2026-07-27 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| cb9b83d0-42ce-3df5-9556-6abd8106af9c | -12.3259 | -50.3958 | 2026-07-27 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 4cd51800-112c-3e28-8ac0-cee21b7278f1 | -12.3412 | -47.1688 | 2026-07-27 15:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| c9eef4d0-ea9c-3994-bed1-8dfef22c5ebd | -11.5105 | -50.1914 | 2026-07-27 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| bd7936d5-9104-359d-bca7-76f418e84671 | -18.1819 | -52.18 | 2026-07-27 15:30:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 151.9 |
| c801a838-0f32-34e4-b536-4132f83aa3ea | -11.4562 | -47.5338 | 2026-07-27 15:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| dba01280-ed1f-3656-a8d6-5e0243e9ade5 | -12.322 | -47.1715 | 2026-07-27 15:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 0115a7d3-a918-3975-a1c0-16421ab3d4c2 | -20.4793 | -57.3625 | 2026-07-27 15:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 9a3ca54c-ab12-371e-b3f9-90516eaa6990 | -11.4559 | -47.5561 | 2026-07-27 15:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 19f36d65-dc9c-3070-8976-5b35dedbb22a | -5.5909 | -42.6929 | 2026-07-27 15:30:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 135.7 |
| 5313a774-3268-3488-9942-2256e4e9670a | -13.1026 | -43.5647 | 2026-07-27 15:30:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 4042c94f-9cbe-3aa4-934a-8e74f33c183b | -12.3216 | -47.194 | 2026-07-27 15:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 26d215a4-d956-3d2b-ae61-4268141c2584 | -7.6375 | -49.7507 | 2026-07-27 15:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 5bd285c0-d011-3cf1-8cdf-bd3d756ab266 | -20.4793 | -57.3625 | 2026-07-27 15:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 135.2 |
| bf79d21b-c797-3e22-b218-b53ff3f7f06a | -11.4914 | -50.1936 | 2026-07-27 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| d0274eda-b30c-3612-801c-246c92c6f4ba | -11.5105 | -50.1914 | 2026-07-27 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 216.9 |
| 7b3648e4-bfbe-394a-bbb5-662f221b90cb | -12.322 | -47.1715 | 2026-07-27 15:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 5172f3a2-68ad-3d16-b7b9-8228872f639d | -7.6375 | -49.7507 | 2026-07-27 15:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 99f14e0c-0fc5-3f33-a9ca-32630449219f | -11.1542 | -51.2324 | 2026-07-27 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 30fa6047-db35-3dd1-b886-ed1c1d3f63e4 | -20.3255 | -54.0266 | 2026-07-27 15:40:00 | GOES-19 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 5b63e542-cf1e-30b3-ae09-ed80705600eb | -7.7093 | -46.499 | 2026-07-27 15:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 022e9ba6-03af-32ca-b6ed-7bece833576f | -11.1353 | -51.2344 | 2026-07-27 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 3dbf8ef2-a9b7-32b2-9d53-2037e5779c98 | -5.5909 | -42.6929 | 2026-07-27 15:40:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 55338d9e-2d74-3561-8f06-dd5389852745 | -12.3412 | -47.1688 | 2026-07-27 15:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| ef60b64a-c5e7-3c58-8a1c-8c82003b173c | -12.3216 | -47.194 | 2026-07-27 15:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 577f0d68-4e4e-318d-a893-f8847cdf487c | -18.1819 | -52.18 | 2026-07-27 15:40:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 106.3 |
| dfdfcdf5-ab81-3cac-a453-4c302309692a | -12.3259 | -50.3958 | 2026-07-27 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| eab63689-5c4b-3702-afa7-c3edb3ed145f | -12.3263 | -50.3742 | 2026-07-27 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |


