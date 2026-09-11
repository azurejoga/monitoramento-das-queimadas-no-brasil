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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01bb9b57-003d-3466-88ed-185069369297 | -14.6026 | -48.8601 | 2026-09-11 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| b3086caf-773e-32c7-96c7-403748ceee98 | -2.7148 | -57.6274 | 2026-09-11 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 3d0be9c1-ebfc-3185-a003-e169be0a339f | -2.7331 | -57.6271 | 2026-09-11 00:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 6eb89bc3-7498-3cac-b5f9-cfafc5bbcadb | -5.9815 | -57.7672 | 2026-09-11 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 2fc8b77f-5bc3-3351-ad24-59e51fc8fc6f | -9.18 | -68.2009 | 2026-09-11 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 141.9 |
| f7388d7f-ff20-3c74-bd39-6295baa6c0a5 | -9.0244 | -65.4181 | 2026-09-11 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 77516eea-0d1b-3418-a304-92972f8bdcf7 | -5.2115 | -45.5498 | 2026-09-11 00:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 974d55cf-5126-3ddb-b897-4578a50c8a0b | -10.7772 | -45.9372 | 2026-09-11 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 7d683f03-d5de-302b-b1bc-c5681730362f | -6.2429 | -51.6939 | 2026-09-11 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 66209833-c39a-39c6-bc3d-d6a8044fbc58 | -4.5229 | -54.9639 | 2026-09-11 00:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| ac587e2d-9d1a-33eb-8f79-16199674bfe2 | -5.7756 | -45.0826 | 2026-09-11 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 9b3016a1-0e3e-39af-91da-4a063066759f | -9.1985 | -68.2004 | 2026-09-11 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 134.1 |
| d7482beb-5e8a-36ee-aea8-e91e2a9807b5 | -9.1799 | -68.2194 | 2026-09-11 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 116.5 |
| f3a9a24f-3319-31ae-a34f-ec273c0d2b47 | -9.043 | -65.4175 | 2026-09-11 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| e68dd52b-17b3-3bc7-9c49-940d2eda5568 | -8.6311 | -66.5101 | 2026-09-11 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 8f9d7ab4-ff44-37ed-ba5b-a4cfb368e0f3 | -9.1984 | -68.2189 | 2026-09-11 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 5b2ee127-ee9e-3918-8ab3-b26e40b0e13c | -2.7148 | -57.6274 | 2026-09-11 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| f77bf17d-8aa5-36d4-a9e7-20ecdfcf83b7 | -9.1984 | -68.2189 | 2026-09-11 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 07a6ad58-bd9f-3ebd-aa74-3214cd75fb20 | -4.5413 | -54.9633 | 2026-09-11 00:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 59d12fae-7b4d-3736-9a0e-e232a1f3ed71 | -8.6311 | -66.5101 | 2026-09-11 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| e0d631e3-3134-3d06-aef8-62261ef76d37 | -9.1799 | -68.2194 | 2026-09-11 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 879eeeb3-6992-3ee8-b786-5e0618eb26f5 | -9.1985 | -68.2004 | 2026-09-11 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 32a01f8c-2067-3a7f-a575-c02460b3bee0 | -2.7331 | -57.6271 | 2026-09-11 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 26e6754d-c1ab-381d-8852-1325efc8cea5 | -2.7332 | -57.6077 | 2026-09-11 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 3ca029c9-48d1-3f49-956e-617f22218190 | -9.18 | -68.2009 | 2026-09-11 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 169.1 |
| 95d3458a-7b09-3306-ab04-c0103c4ec383 | -4.3587 | -47.7853 | 2026-09-11 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 3f18b52a-1683-3d9a-aa94-8e6c2edd3869 | -9.043 | -65.4175 | 2026-09-11 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| ac126109-d899-3649-8fbc-89a5af1231fa | -5.7756 | -45.0826 | 2026-09-11 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| a805e43a-0698-346d-a21d-62fba3ce6514 | -14.6026 | -48.8601 | 2026-09-11 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 94857237-9f03-34ec-8400-519f2f33b7d1 | -2.7148 | -57.6274 | 2026-09-11 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 4f1e2d93-eb23-3a21-9096-f6c4494a7648 | -5.7756 | -45.0826 | 2026-09-11 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 4431af9f-6afb-3f99-a5c3-6b7fb9e03f22 | -2.7331 | -57.6271 | 2026-09-11 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| f5be81cb-0bea-3081-beb7-413155d426e4 | -9.1799 | -68.2194 | 2026-09-11 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 2c669713-d308-3a05-b607-f81b88ca8db0 | -14.6026 | -48.8601 | 2026-09-11 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 101.9 |
| f39c6e36-53c1-3306-bee6-a5c93f35c615 | -19.7822 | -58.062 | 2026-09-11 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 127.8 |
| 94053b6b-a0af-3c5a-899f-cd5307de37bd | -4.5413 | -54.9633 | 2026-09-11 00:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| feec454e-0b6e-3158-bd4a-fa5c27ec053b | -4.3138 | -49.1012 | 2026-09-11 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| f3c61ba6-c3f5-3ab8-bba3-53d3d078411e | -9.1985 | -68.2004 | 2026-09-11 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 10a63895-05f9-31ac-83f2-418db900cda2 | -4.2953 | -49.1021 | 2026-09-11 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| ca44ee39-43d6-3ea9-8d1c-6621b96535b6 | -2.7332 | -57.6077 | 2026-09-11 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 19d87bf3-bf32-32fc-8b4a-1f94e7527a85 | -4.3587 | -47.7853 | 2026-09-11 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| b8d2e2d0-75a8-3e90-940e-b18347ed4bd2 | -9.043 | -65.4175 | 2026-09-11 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 29f2b596-446e-3fae-92ef-3955e24bb35f | -9.1984 | -68.2189 | 2026-09-11 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| de7ee2af-a6d7-358b-bc25-54712c781ed0 | -10.7772 | -45.9372 | 2026-09-11 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 1a195fbd-e20a-3dce-8aad-7a26a7bb5400 | -8.6311 | -66.5101 | 2026-09-11 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 50f4e2fa-62eb-38c9-af9a-dcacf416e388 | -19.8027 | -58.0386 | 2026-09-11 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.4 |
| 04873f31-9e38-34f5-97a4-5c23863717ff | -19.8023 | -58.0593 | 2026-09-11 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 208.7 |
| 0c03500f-1362-35ac-a49a-b44754f0b28b | -9.18 | -68.2009 | 2026-09-11 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 141.0 |
| b3d86a25-7aca-3e8d-bf63-e2d4177ae6c8 | -20.45892 | -57.45562 | 2026-09-11 00:20:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 0329424d-9093-34e0-8413-a8fa5ab04a21 | -19.79696 | -58.07433 | 2026-09-11 00:20:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 208.7 |
| 0b38e7c0-49fe-376a-83f0-50b0e2dc47fd | -19.79499 | -58.05636 | 2026-09-11 00:20:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 200.0 |
| 98606c71-2a39-3932-9f6b-87a7005dca81 | -19.80243 | -58.06822 | 2026-09-11 00:20:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 351.5 |
| 88128884-a07e-3ce7-b856-2d4ce3ad8c3a | -22.27584 | -55.83504 | 2026-09-11 00:20:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6a2b65bb-5c93-3d99-9b0a-ddb9d8fbd833 | -22.26533 | -55.83643 | 2026-09-11 00:20:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 51238f4d-fa89-38f7-9185-f5c795372f45 | -22.26688 | -55.85017 | 2026-09-11 00:20:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 43d65637-0b8b-33cc-97c6-dc3df1446dbf | -22.2774 | -55.84868 | 2026-09-11 00:20:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 30bf9d15-df0f-3fe4-a1d3-f7d090a976b0 | -19.78301 | -58.05778 | 2026-09-11 00:20:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.2 |
| ebbeaeb3-30a6-3a37-99f3-382a85d977e0 | -18.87525 | -48.92822 | 2026-09-11 00:20:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b171cb58-5c60-3900-a7a3-ae8e808714e5 | -19.78107 | -58.03986 | 2026-09-11 00:20:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| f8546d0d-059a-3fd6-a26d-1c17a0fe614b | -20.47047 | -57.4542 | 2026-09-11 00:20:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.5 |
| cb4eeaac-d759-3b2d-8402-335b5c99daae | -20.46742 | -57.44896 | 2026-09-11 00:20:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.4 |
| 151a107d-d40d-322c-abc6-478f753d146c | -20.45708 | -57.43901 | 2026-09-11 00:20:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| d50395c0-5967-30ce-921c-1e4e7b15626f | -20.46915 | -57.46564 | 2026-09-11 00:20:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.0 |
| b64172db-a339-39ba-b31c-b164b0d0faff | -19.81897 | -58.05353 | 2026-09-11 00:20:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.9 |
| 9af6737c-2c22-3578-a687-d1d733de4449 | -20.48072 | -57.46421 | 2026-09-11 00:20:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 91193329-b7b8-31d4-abe4-9129f19540e2 | -19.80059 | -58.05022 | 2026-09-11 00:20:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.9 |
| b0627b65-277c-3374-a9fa-fe2614e0b5a4 | -19.79304 | -58.03844 | 2026-09-11 00:20:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 184ade58-fc9b-3147-965a-db348aa94cd9 | -12.3487 | -48.20699 | 2026-09-11 00:22:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 0983d7c8-f327-3fb2-acf2-89af089bd632 | -14.61003 | -48.87094 | 2026-09-11 00:22:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 46d8adf4-9f58-36e2-a218-d4e82d88ac1e | -9.63163 | -49.01904 | 2026-09-11 00:22:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 9d016956-ebbd-39a9-a7aa-1394067e8fac | -13.50536 | -44.08448 | 2026-09-11 00:22:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 43.0 |
| b97d7888-a36c-3b38-a7ea-2f8d86e923cd | -14.58624 | -48.86065 | 2026-09-11 00:22:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d58f94f0-3909-39d7-90dd-90fcb03fe3a6 | -14.0742 | -45.63902 | 2026-09-11 00:22:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| e45a7cfe-9dfe-308d-a12f-f5aeeff3238f | -14.78701 | -48.0891 | 2026-09-11 00:22:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| df0a298f-9687-3aab-8726-7785736c93b4 | -10.68008 | -50.7988 | 2026-09-11 00:22:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| af9e928c-82f5-3109-ab40-117428159175 | -14.60789 | -48.85722 | 2026-09-11 00:22:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 3f925e78-c999-332d-9cbe-d55036d2fe28 | -13.77572 | -43.63956 | 2026-09-11 00:22:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 41591c63-d117-3cd1-878f-5330e4857dec | -10.6919 | -50.80901 | 2026-09-11 00:22:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c3ca6901-7da9-322c-84b0-608cc8ffe201 | -10.76068 | -45.92997 | 2026-09-11 00:22:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 0b3d3473-96c6-3511-9a30-ec2a7d634282 | -16.87873 | -49.67797 | 2026-09-11 00:22:00 | TERRA_M-M | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f964c4ef-951d-3f7c-8831-49fb85b5da20 | -12.23242 | -51.32936 | 2026-09-11 00:22:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 02458073-3cca-369b-9bce-d0f01fba0d94 | -10.66614 | -49.07857 | 2026-09-11 00:22:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e93f09e1-795e-3104-840a-ece4d4b8bd3b | -10.50615 | -49.53259 | 2026-09-11 00:22:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 62aeabce-71f0-3135-be71-d9064591eb6f | -10.69011 | -50.79723 | 2026-09-11 00:22:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 250ee5d3-7f17-3d76-a0f4-77c8ce0e890f | -14.59923 | -48.8727 | 2026-09-11 00:22:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 84dad12c-cff4-3702-bcba-0c55208312d9 | -10.54618 | -51.35089 | 2026-09-11 00:22:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 71477944-64d2-3e12-ba40-062a277d8d03 | -12.15468 | -64.15157 | 2026-09-11 00:22:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 7e71f451-df92-3606-91f0-9c5563f80622 | -10.53644 | -51.35209 | 2026-09-11 00:22:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 14dcacac-3a25-395a-a065-4850189e8b15 | -10.50388 | -49.51809 | 2026-09-11 00:22:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 2b415528-f14d-3d47-ac98-1cc008db0c1c | -14.61869 | -48.85532 | 2026-09-11 00:22:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 263717d1-ea67-35f4-9f0b-fa318a535f25 | -16.87636 | -49.67227 | 2026-09-11 00:22:00 | TERRA_M-M | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2f3db8e6-b073-356a-af0d-168d258d8f39 | -13.50002 | -48.55627 | 2026-09-11 00:22:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 162b9635-7324-354d-9448-e80b57d2c1bb | -10.67932 | -50.79311 | 2026-09-11 00:22:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| c18c3f21-02ed-34de-a2ac-ec54fe789c88 | -13.4888 | -48.55854 | 2026-09-11 00:22:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5a5e6cb7-bd78-351f-a84b-63a42f3cd843 | -14.60571 | -48.84324 | 2026-09-11 00:22:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d0650cde-fe03-3708-b309-a55dfcb6dbd0 | -13.33383 | -61.66307 | 2026-09-11 00:22:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 16fcbb1f-f8af-318a-a691-66ea50aa33af | -13.76988 | -43.64766 | 2026-09-11 00:22:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 39208505-9da0-325d-af13-0608461137dc | -10.78043 | -45.94937 | 2026-09-11 00:22:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 1cc29fb9-ba02-3d3e-8d55-0f3a26c483ab | -14.85668 | -48.16856 | 2026-09-11 00:22:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 02b26fcd-f52c-321d-bc7e-8391ddb1eea6 | -14.59708 | -48.85899 | 2026-09-11 00:22:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |


[Clique aqui para ver as próximas entradas](README2.md)
