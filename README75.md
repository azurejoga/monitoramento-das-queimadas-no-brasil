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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a572b69-85ce-33ef-a0b2-46070a3a07f4 | -7.449 | -44.6016 | 2026-09-28 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| a8ae502e-8c23-3f87-a9bf-fc73b81863be | -15.1847 | -46.141 | 2026-09-28 13:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 197.2 |
| 0102e5f3-d46b-3d3f-86a2-0614e0da0f79 | -10.7104 | -50.4718 | 2026-09-28 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 5d1b9508-59d4-3db9-bbf7-40e31fd0a260 | -10.2067 | -49.9898 | 2026-09-28 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| fd1b9580-b647-36c1-888d-67eb59d39dc6 | -8.2293 | -45.4375 | 2026-09-28 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 202.4 |
| 2183d82f-3035-34d2-8489-3912f83c63db | -12.155 | -50.352 | 2026-09-28 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 29ff85ae-393a-3f72-974e-815eef2f13c7 | -10.8238 | -60.744 | 2026-09-28 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 473b5afe-a583-3950-a7a7-569fb776f10c | -10.2254 | -50.0093 | 2026-09-28 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 10e6b3ed-8eec-35fb-85bc-65e3bf8e73bb | -13.161 | -48.5437 | 2026-09-28 13:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 9838e616-7db5-3ee7-b075-5d59f62f733f | -7.055 | -42.849 | 2026-09-28 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 106.0 |
| fca89b70-2533-332b-9c1f-49437395eb7b | -8.0169 | -42.8444 | 2026-09-28 13:40:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 114.9 |
| ea23a522-ab88-372d-ab73-e93753cc0940 | -12.1547 | -50.3735 | 2026-09-28 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.1 |
| f1a4a2c5-8716-3685-9567-c7a721083b1b | -9.177 | -61.4073 | 2026-09-28 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| eda7d089-fbdc-3e7e-9380-b150b8a9ace8 | -11.4425 | -44.9303 | 2026-09-28 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 0f71ff7e-ab22-301e-a441-5f2fe9b4db14 | -12.8061 | -54.0048 | 2026-09-28 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 5df3be47-3936-3a85-8d8c-82e672fefdd6 | -10.8187 | -57.2192 | 2026-09-28 13:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 95419ba4-30db-3d3b-9431-3742bd8f5c38 | -9.1337 | -49.9656 | 2026-09-28 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| e98957c9-8c92-35fc-afd7-da8f1518d729 | -10.6889 | -50.6658 | 2026-09-28 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| a4999af2-1520-3cad-8f17-f5c8f1242499 | -12.4351 | -44.1497 | 2026-09-28 13:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 8373946e-df94-36dc-886e-6d742af7bf91 | -8.3608 | -45.4695 | 2026-09-28 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 9fbc2830-ac80-3125-909b-ef29bca8fb9d | -15.6867 | -48.2141 | 2026-09-28 13:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 39e7483f-bedf-3c55-91d8-b926cb3ea29f | -13.0848 | -47.4423 | 2026-09-28 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 92333ef6-b33a-3e82-8ad3-ff4fbbcdd3ec | -10.2065 | -50.0113 | 2026-09-28 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 6ef256c7-f7f5-35da-9553-220d8173fba1 | -11.1181 | -51.1091 | 2026-09-28 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 2fe1344c-0761-324b-af50-508a6d001e7f | -7.449 | -44.6016 | 2026-09-28 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 7298960e-54db-3746-aaa9-a4bcdddd0a0c | -8.2862 | -45.409 | 2026-09-28 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| ad6869c1-c4d8-38a5-813c-6e2c2401f86f | -12.7413 | -47.3133 | 2026-09-28 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 17cf1b64-ea3b-30d4-842f-b3a0b7b7a5c7 | -11.1775 | -44.7832 | 2026-09-28 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 206.9 |
| 2a3892e8-17be-3ffc-8ea0-b3f8933cf902 | -11.5628 | -50.5069 | 2026-09-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| e735cecd-d454-3d82-bd1c-873f10baa1fb | -9.4999 | -46.385 | 2026-09-28 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 159.5 |
| fe8e8474-71cc-30ae-9d6a-94a854e312a9 | -12.3088 | -50.2688 | 2026-09-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| b64bd81b-8980-32dc-8ef0-26bcdf8caae5 | -11.1327 | -50.0624 | 2026-09-28 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| de02694b-bcf6-397b-a2b7-532d6f795b36 | -12.6643 | -47.3245 | 2026-09-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 19a780cf-0809-3eb2-820b-851f645a8cd2 | -12.6263 | -47.3075 | 2026-09-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| e2e52613-eb8a-3fe4-a79a-bbf5bcdb54ac | -11.8641 | -47.1004 | 2026-09-28 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 3bbd991d-3462-3166-94ad-ca88b63a790c | -12.8059 | -54.0255 | 2026-09-28 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| a752d3e0-0091-309f-9bc9-e4b48a615e4e | -12.1547 | -50.3735 | 2026-09-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 4e3fe131-7178-3c67-b41d-e7cd49a6b0eb | -12.8653 | -44.8047 | 2026-09-28 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| fcbf3872-8937-3d58-abf5-bd11edc639f8 | -15.1451 | -43.6088 | 2026-09-28 13:50:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 135.0 |
| 19a626f2-9923-36ef-9162-3e0f43d46d89 | -11.1331 | -50.0409 | 2026-09-28 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 328c5845-a0b9-3d7b-82f2-07930a214178 | -11.1517 | -50.0603 | 2026-09-28 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 3a9f8c23-bb4c-347e-a4a4-f1d9dd29e535 | -13.0848 | -47.4423 | 2026-09-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 3ea5c9a9-8deb-3917-8f34-b84c54b52809 | -15.6867 | -48.2141 | 2026-09-28 13:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 5b3e5354-a817-3633-85e7-1d9a9c32c9ec | -12.7028 | -47.3189 | 2026-09-28 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| cde8634a-8bc2-312a-9040-80cfa251bed1 | -12.7229 | -47.2712 | 2026-09-28 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 1ec06c96-ff3d-3bed-8ed5-63949ed3213c | -8.0361 | -42.8187 | 2026-09-28 13:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| d622fe7a-803e-3ba2-8b7b-583451102df5 | -10.2446 | -49.986 | 2026-09-28 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| cc6dd23f-d089-3d85-9ff3-def2f99c958b | -10.8051 | -60.745 | 2026-09-28 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 0957e9d5-9e42-3d42-b2cb-3e25a1c6fb99 | -12.6451 | -47.3272 | 2026-09-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 5473f67c-c4e0-3892-bb90-d6cea1454007 | -12.6836 | -47.3217 | 2026-09-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 204.0 |
| bf2510b0-5d82-35ec-9081-343995833a4e | -7.4869 | -44.5751 | 2026-09-28 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| b0ed80ba-b826-3979-a146-c42e2e349724 | -12.7417 | -47.2909 | 2026-09-28 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 636ee839-cd35-3ec8-9f42-31d5f4c3e1ed | -11.1966 | -44.7805 | 2026-09-28 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 345.9 |
| b4338f80-0225-3eeb-acf2-03328cde4cfa | -8.0169 | -42.8444 | 2026-09-28 13:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 161.8 |
| 8b5a3900-fb1b-3b4c-b6ac-0d94bd6cef9e | -7.4492 | -44.5786 | 2026-09-28 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 03498613-1a31-31eb-9c13-7675f9d8ebb5 | -12.8851 | -44.7782 | 2026-09-28 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 513152d1-9416-3e92-b402-fc2fea4b262d | -10.8375 | -57.2178 | 2026-09-28 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 63792b8e-f795-37e9-b3cb-503a76fc2bac | -10.2254 | -50.0093 | 2026-09-28 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 24ffc931-8dd7-367f-a16f-f7a08be7a210 | -7.0547 | -42.8726 | 2026-09-28 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 106.8 |
| 9da2de34-1dc1-3fc5-b9c2-f5d7bbabb2cb | -11.2158 | -44.7778 | 2026-09-28 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| f69fd6a7-d8ea-3796-9b56-c73f376c55f7 | -10.4232 | -53.8219 | 2026-09-28 13:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 89ef5778-80ad-39a0-bc32-7e5d16ccacbd | -9.177 | -61.4073 | 2026-09-28 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 8dc9a1df-bdd7-3941-9662-b544b84b9443 | -8.2859 | -45.4317 | 2026-09-28 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| a5ba32cb-f3e5-3f03-b6fb-d7da49768d01 | -12.2311 | -50.3643 | 2026-09-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 758d2183-6326-344a-afad-6e6b8612872c | -12.2502 | -50.362 | 2026-09-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 8e01d068-3804-30b7-967f-0f0fcbcc407f | -15.1847 | -46.141 | 2026-09-28 13:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 4f5727fd-1edd-39c0-91d0-c3bce840974e | -20.1966 | -48.5773 | 2026-09-28 13:50:00 | GOES-19 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 64.3 |
| a7278d1e-f5ef-3d83-ba52-cc86f48881cd | -9.481 | -46.3871 | 2026-09-28 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 147.2 |
| d29921ce-4659-3a7f-bb86-7711646b7abe | -10.8185 | -57.2391 | 2026-09-28 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 2d5e1cca-f4e7-3e84-a14f-6fad894116de | -12.2123 | -50.3451 | 2026-09-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| bb8784cf-ebf1-3c5b-b491-8b346c592a86 | -8.6451 | -45.3489 | 2026-09-28 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| a465bf6b-e6bf-3a87-98d7-50e077ca5719 | -12.6259 | -47.33 | 2026-09-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| d9bad5a5-f3bf-3b40-8e20-ad053be9b94f | -10.2067 | -49.9898 | 2026-09-28 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 87cb7805-80bc-3afc-873d-0a7150223219 | -11.1771 | -44.8064 | 2026-09-28 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 270.7 |
| da13825e-8258-3403-8be1-dd53b663437a | -13.5911 | -51.458 | 2026-09-28 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 9bd23a34-d944-3281-b5c7-ff591cd59885 | -11.5821 | -50.4833 | 2026-09-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| dddd308d-dda1-3da5-bc57-7e5afb38b6d1 | -8.0358 | -42.8423 | 2026-09-28 13:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 331.8 |
| 6b3ec71a-634f-3f9b-aadd-a40df092e2f7 | -8.9633 | -44.1655 | 2026-09-28 13:50:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 39828dd3-3626-36b1-8991-9ad7980985ac | -12.2508 | -50.3189 | 2026-09-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 7a3acd1e-4fa0-33b0-801f-6be9f77aa844 | -9.7485 | -48.9598 | 2026-09-28 13:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 4e7f41ad-0c5d-362a-9643-9274282f2dc2 | -12.1737 | -50.3712 | 2026-09-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 64e72a79-b6d9-30a5-8ed5-f5e670a5dc0c | -8.2293 | -45.4375 | 2026-09-28 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 47451853-a162-353d-97e7-a61022a387a9 | -12.8061 | -54.0048 | 2026-09-28 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 6763de01-f335-3094-b88f-8a73d4207b03 | -11.0988 | -51.1324 | 2026-09-28 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 22c48b47-b0e7-35cf-b77f-072cb8817887 | -10.2257 | -49.9879 | 2026-09-28 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 77f2dcd7-3146-381b-b6d3-c7e6995dda95 | -10.8189 | -57.1993 | 2026-09-28 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| bd445d15-4114-3a43-a4ca-8646eb01a01f | -13.4205 | -51.3304 | 2026-09-28 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 04bc7228-5cc2-324f-ab30-4f25b738af68 | -10.7343 | -48.7661 | 2026-09-28 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 047ff5f2-7d74-3083-aee5-6734b288c73f | -11.2154 | -44.801 | 2026-09-28 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 257.2 |
| 07a0a576-f2f0-3c20-a13c-94896fe77dca | -11.5352 | -47.3678 | 2026-09-28 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 156.1 |
| e4068bf4-aa26-3346-933f-3dd0b7f7a09d | -7.5057 | -44.5733 | 2026-09-28 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 333.9 |
| 0cdf074f-7317-3349-8b49-4891a7e091cb | -11.1958 | -44.8269 | 2026-09-28 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 45b5eaff-f9bb-39f1-9961-c274a7ee58fd | -8.6631 | -45.4152 | 2026-09-28 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| f32997b3-0ace-344c-bec8-0ffddd9c4704 | -12.6878 | -45.0192 | 2026-09-28 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 27080efb-1fe2-3410-8a13-b222377e7d8e | -8.2807 | -54.7158 | 2026-09-28 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 5f8f5afb-fb6b-37c3-a9ec-e308b984811e | -16.6932 | -50.6608 | 2026-09-28 13:50:00 | GOES-19 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 53.5 |
| ca5b344b-beb9-338e-917d-200d4827e1be | -11.1178 | -51.1304 | 2026-09-28 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 77b06883-14c6-3157-accb-d7893cf6831a | -10.8238 | -60.744 | 2026-09-28 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 3c5b21d5-ec1d-303c-82b9-e9f0e38e9837 | -11.771 | -50.5686 | 2026-09-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 264a8f23-04d4-39a0-9306-1f74527551dd | -14.5451 | -40.8669 | 2026-09-28 13:50:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 108.1 |


[Clique aqui para ver as próximas entradas](README76.md)
