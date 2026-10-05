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
| 16b15742-5a76-3e0d-989b-9ad41a043dd5 | -7.7212 | -45.465801 | 2026-10-05 00:12:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 84ca204d-a3b5-3077-8219-632e69aecf3f | -8.7455 | -44.148602 | 2026-10-05 00:12:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 49483d3f-9e27-3bd7-819b-5c1390d1944c | -10.0752 | -36.2173 | 2026-10-05 00:12:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 25a831f6-8f9d-3cb7-b7e2-c0b8ca161ab3 | -7.6419 | -35.004501 | 2026-10-05 00:12:00 | METOP-C | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5cde74e1-867b-3553-b00d-ec8079508655 | -5.9826 | -53.483299 | 2026-10-05 00:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bbea13b-0f0c-39f9-a2f2-125109ae2e6b | -3.892 | -49.682201 | 2026-10-05 00:12:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d27feca9-f604-39c8-903a-bf9baaea9392 | -6.1779 | -52.788601 | 2026-10-05 00:12:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d804ca15-4ac4-3313-9bad-128403e5c090 | -6.9261 | -43.683998 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 28febb85-7f78-34ea-bc3f-658ab5ccf144 | -6.5989 | -41.555599 | 2026-10-05 00:12:00 | METOP-C | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6e245072-e542-3a4e-ad0d-ad822c307238 | -3.2526 | -54.120899 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5fcc2fe-4c25-3ef8-a322-e4e91c324f23 | -6.9227 | -43.668701 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8231e2de-cd85-30bb-a73a-3841bd795d49 | -2.9237 | -54.092999 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fedd952-5045-3515-9924-21847dbed38c | -6.1875 | -52.786598 | 2026-10-05 00:12:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 163ed7d8-0d63-3b62-ac11-bbf4c81f1ceb | -3.9174 | -38.666698 | 2026-10-05 00:12:00 | METOP-C | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b66c426f-f939-392a-b22a-45e19ffdba7f | -6.4206 | -43.723598 | 2026-10-05 00:12:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03b0567a-6dc5-3411-a264-56376971b3d1 | -7.174 | -41.998199 | 2026-10-05 00:12:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fa79872a-0396-35a9-b569-8a87cfc59eed | -2.9719 | -54.0826 | 2026-10-05 00:12:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c5fc906-2eb2-3241-b28d-6ebc134f2f74 | -6.3366 | -43.349998 | 2026-10-05 00:12:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef81480a-c14a-3b13-90a6-577640452c85 | -3.0934 | -53.677101 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1cb7115-cbcd-34e8-bef5-a9180b4493e5 | -6.3268 | -43.3522 | 2026-10-05 00:12:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f67584f7-3138-3b7f-acfd-5f3f69d7ec8a | -3.0576 | -54.1959 | 2026-10-05 00:12:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72ee4b41-054b-3583-8b17-5d625bfa4763 | -2.9554 | -54.053699 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0c35426-791c-3399-8d76-16d16a95e4de | -16.137699 | -40.699501 | 2026-10-05 00:12:00 | METOP-C | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 174c1b8b-e3c7-3ed2-a872-600130a02a3a | -11.6824 | -43.6432 | 2026-10-05 00:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 97ec4465-5015-366a-b77b-e1bc4b79bf24 | -4.7891 | -42.568199 | 2026-10-05 00:12:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1bb7eeda-04ba-32d8-95a2-f0e58d79074d | -3.1383 | -50.418598 | 2026-10-05 00:12:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c88d214f-7d41-3dff-a710-5139ecd76a53 | -6.6021 | -41.569302 | 2026-10-05 00:12:00 | METOP-C | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8d3fba61-4546-3c99-acca-b2bb5f76df92 | -10.0826 | -36.2052 | 2026-10-05 00:12:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e0f999c0-f4b7-3399-aaa1-276e4f9a1046 | -5.5711 | -49.718498 | 2026-10-05 00:12:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70365c1b-47c6-3606-a883-e14ff190ae70 | -2.9526 | -54.0868 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48087a89-5f58-3216-8be6-f955c75f8456 | -6.8933 | -43.675201 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| df976d4f-45f9-337f-8ab6-e42cbcc272ff | -6.8916 | -43.667599 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 858b7d6c-6c7e-37c4-bbc7-071d2e88e583 | -10.9571 | -45.426701 | 2026-10-05 00:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a3ecea45-c97f-36d4-a468-8f3a97b9b7c7 | -13.5802 | -43.706501 | 2026-10-05 00:12:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1e59fb44-3ec3-3c8b-a5fd-a5a3f2278f3b | -5.9683 | -41.323399 | 2026-10-05 00:12:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b5b3e7e2-e635-3715-ab41-3fc44ff6cca2 | -3.8956 | -49.698101 | 2026-10-05 00:12:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7ac7170-39b7-3c57-b21b-067bff3e8bb5 | -10.9549 | -45.416199 | 2026-10-05 00:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad1ac0eb-5133-33f2-ba98-14f05c6c82e7 | -6.3285 | -43.359501 | 2026-10-05 00:12:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 076a4d22-c549-3150-bf87-40a474345871 | -3.9018 | -49.680099 | 2026-10-05 00:12:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 436d523b-f29d-32b0-a41f-b743f16f36e7 | -6.6103 | -41.5602 | 2026-10-05 00:12:00 | METOP-C | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1c9229f4-5c8f-33dd-99ce-35c9763c76fa | -13.6248 | -44.409199 | 2026-10-05 00:12:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d39beb2d-6d78-3d3a-8db9-402c76aef020 | -2.9211 | -54.126202 | 2026-10-05 00:12:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e81bd1c-fb16-3127-a146-d14bb7f33fd9 | -7.6388 | -34.9921 | 2026-10-05 00:12:00 | METOP-C | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 44488678-9871-3a0d-a36f-fcade8387bda | -3.3062 | -53.361099 | 2026-10-05 00:12:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb93283f-8b0f-3969-a071-155250ff0050 | -3.0838 | -53.6791 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72f0c445-2d97-3b33-8c6e-6f1c926e146d | -11.7099 | -43.628201 | 2026-10-05 00:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 614f0945-2cf9-3e86-ba3d-975b7bdf8589 | -9.4673 | -40.390701 | 2026-10-05 00:12:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b17c74e6-4959-3c25-a96b-e55a5c43f542 | -6.2557 | -35.154499 | 2026-10-05 00:12:00 | METOP-C | TIBAU DO SUL | RIO GRANDE DO NORTE | Brasil | 2414209 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 07b4f73b-0606-3341-850f-db63aabc4b5f | -6.246 | -35.156799 | 2026-10-05 00:12:00 | METOP-C | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4b671640-61e4-38e6-ab6e-2cd3c039a298 | -8.5953 | -45.669498 | 2026-10-05 00:12:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e66587eb-da87-3f93-ab1c-d7eb0d879494 | -13.6289 | -44.429298 | 2026-10-05 00:12:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 18da2953-f5e5-3cb2-8578-a829e1f29009 | -11.702 | -43.638901 | 2026-10-05 00:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 466b41fd-fffd-3a17-a8cd-c4da51d9cbdf | -3.0217 | -54.170502 | 2026-10-05 00:12:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c25ea0f0-b4e5-3162-80bb-5a2e70bc1dd2 | -11.7135 | -43.5023 | 2026-10-05 00:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ec4ee41-df7f-3496-bc01-0e75b0e65604 | -3.1421 | -50.435902 | 2026-10-05 00:12:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac0f753a-6246-3ca6-8329-4823352c063f | -3.0672 | -54.193901 | 2026-10-05 00:12:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9de07dd7-50d0-3746-a667-2ce4edac1ea2 | -10.9669 | -45.424599 | 2026-10-05 00:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ee59aab8-9b18-3963-a33a-29d1d5a17f42 | -6.9014 | -43.665501 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e5782d57-cdfc-3da0-b20f-843d87e77ce3 | -3.2969 | -53.820202 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14d76e52-5a1c-3da3-b9d6-c5abe97b7450 | -6.8997 | -43.657799 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e3115909-ea0b-3839-9254-430dc3495d3a | -8.7474 | -44.157001 | 2026-10-05 00:12:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8fe390ea-8f0a-3744-bd48-7a84ad387c63 | -6.4287 | -43.713799 | 2026-10-05 00:12:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5096df5e-3cb9-3d97-bac6-3d58296579cf | -11.7118 | -43.636799 | 2026-10-05 00:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03faa67c-233d-3404-97ad-6f62f6474f11 | -5.5687 | -49.754601 | 2026-10-05 00:12:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19109e83-a9cb-38aa-9f4b-3ce10da0fe88 | -2.7917 | -54.089001 | 2026-10-05 00:12:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4288d52-27a0-3ef3-a2e9-3fa5b961d306 | -4.6354 | -47.688499 | 2026-10-05 00:12:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffd0d3aa-5efa-3649-a3c0-0f3458e7d4e5 | -3.9213 | -38.683498 | 2026-10-05 00:12:00 | METOP-C | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ad541a95-d2ce-3291-b093-f12199d01e4c | -11.634 | -43.608799 | 2026-10-05 00:12:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1c195de-0324-340b-a811-1ad75d49ae5d | -6.1531 | -43.632198 | 2026-10-05 00:12:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22c5a84a-052c-3070-a4db-6bea86da1b0a | -6.1514 | -43.624699 | 2026-10-05 00:12:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| efd7c099-ea87-35a0-a23e-2f6eeea490fa | -2.9307 | -54.124199 | 2026-10-05 00:12:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d799a03-7c31-331e-8ef2-22cae218bd6d | -3.0777 | -53.7421 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a1af13b-4163-351a-8b0b-4422826f0c83 | -3.0742 | -53.681198 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74404df8-4212-33eb-84ac-b4f3f6e7d92c | -6.9048 | -43.680698 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e8dced22-05ab-3312-869a-0324ca9d9db1 | -7.8913 | -44.186901 | 2026-10-05 00:12:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 433ff010-340e-3b90-ae44-6825f294c0c2 | -5.4731 | -41.233398 | 2026-10-05 00:12:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 847a707d-e6ac-347e-b8e9-ef84f0b068c8 | -5.565 | -49.737499 | 2026-10-05 00:12:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e23005bb-4174-3edf-bf3f-6f614669a1cf | -2.7821 | -54.091 | 2026-10-05 00:12:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbe16946-7145-31d8-a7dd-f03563142adc | -3.7097 | -40.343399 | 2026-10-05 00:12:00 | METOP-C | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 31463e49-1ad8-3b42-aeef-7fce4a69cd83 | -3.0435 | -54.132702 | 2026-10-05 00:12:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4dbdfd5-5626-378d-bffc-8fe03e0ff74e | -3.0191 | -54.2043 | 2026-10-05 00:12:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b337d405-9667-3f2a-a066-4b19b48acba5 | -6.9146 | -43.678501 | 2026-10-05 00:12:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 04bb37ee-f568-32fd-b392-af653d159562 | -4.0672 | -48.953201 | 2026-10-05 00:12:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d580128-8349-3451-9505-d44d0ba6919c | -3.2693 | -54.1506 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d447484a-483e-341a-ae4a-2ecab71fed83 | -7.8815 | -44.189098 | 2026-10-05 00:12:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 07366e2f-d395-3be9-96c8-39997adcc52b | -3.1162 | -53.733799 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcd7cffb-8bee-3b2d-bea9-344ede20855d | -7.7191 | -45.4562 | 2026-10-05 00:12:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a21b5636-8b7b-388f-8643-d3b85c0be25b | -10.9593 | -45.437302 | 2026-10-05 00:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 10dae8ea-973e-3cf7-91b6-2a5e3ef39e2a | -6.3137 | -43.339699 | 2026-10-05 00:12:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0661cb66-7a12-35f4-b10d-f7fa57439657 | -2.7724 | -54.093102 | 2026-10-05 00:12:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a472a728-3411-3cbe-8ca3-e0c1dc9e6b99 | -3.2596 | -54.152599 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 116b2a5f-37c0-3fc9-b826-3a1d29dc6cc5 | -3.8364 | -50.304401 | 2026-10-05 00:12:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af7e186a-976e-376d-bc19-9f0beb8e5869 | -2.9623 | -54.084702 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13d2e0a6-60fd-3354-b774-ebdd652a0956 | -5.9518 | -41.341499 | 2026-10-05 00:12:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6c4aa05f-29aa-3688-8671-d6cf94409290 | -10.0729 | -36.2076 | 2026-10-05 00:12:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c41e6ff9-55d7-3fb7-a788-6f762ce21c96 | -3.2873 | -53.8223 | 2026-10-05 00:12:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41a64742-1110-3e76-86e6-9e9075cbd69e | -8.5931 | -45.659401 | 2026-10-05 00:12:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 35c41a77-1771-318c-bd2e-750a571a3bec | -7.7093 | -45.458302 | 2026-10-05 00:12:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c176d493-1df3-34fb-9b34-492c6a761213 | -3.8266 | -50.306499 | 2026-10-05 00:12:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 390e40e5-4cd8-3e00-8951-23b8a7bbbfc0 | -6.1935 | -52.814999 | 2026-10-05 00:12:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
