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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44f47c9c-ca01-324f-ba2d-a1fa7e878911 | -14.8086 | -53.890701 | 2024-10-07 01:21:17 | METOP-C | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6b1edf8f-1444-37f0-9eea-3d1ada42a00a | -14.8102 | -53.897999 | 2024-10-07 01:21:17 | METOP-C | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 94aaac82-08f8-3f62-941a-54f25f966b19 | -14.7843 | -53.919701 | 2024-10-07 01:21:17 | METOP-C | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6a70da99-5e1f-315a-9abc-520c89b7865b | -13.9156 | -50.8424 | 2024-10-07 01:21:19 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7a50fa46-e5d0-3097-9040-7488c6479ba3 | -13.5931 | -50.291599 | 2024-10-07 01:21:22 | METOP-C | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 960b4eaa-aab9-3e68-bdf1-7c497ecbddcc | -13.5958 | -50.302502 | 2024-10-07 01:21:22 | METOP-C | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7c2972a4-dc2f-3c36-b4c0-688ba4e8d420 | -13.5807 | -50.283199 | 2024-10-07 01:21:23 | METOP-C | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c50d4dd5-b7d6-3448-b203-e8a7cb6a88fe | -13.5834 | -50.294102 | 2024-10-07 01:21:23 | METOP-C | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d0e3420f-668f-36bd-a15e-09032de462f6 | -13.5861 | -50.305 | 2024-10-07 01:21:23 | METOP-C | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1d00eaa3-9268-38b2-99f5-219064b3c399 | -13.5888 | -50.315899 | 2024-10-07 01:21:23 | METOP-C | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ea4c64e0-0f8f-36a5-9f56-7a83be96556b | -13.5737 | -50.2967 | 2024-10-07 01:21:23 | METOP-C | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c2aaa7e3-04dd-3d57-bf16-951bbb04ff08 | -13.5764 | -50.307598 | 2024-10-07 01:21:23 | METOP-C | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bea6d8ad-e7d7-31f5-af0c-c2e726ed2021 | -13.5791 | -50.318501 | 2024-10-07 01:21:23 | METOP-C | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ff44b374-765e-3720-9507-95128289bacf | -13.7354 | -51.035999 | 2024-10-07 01:21:23 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 72b60db7-c75d-389e-bcd9-36c3fef1c474 | -13.6062 | -50.8466 | 2024-10-07 01:21:24 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| af6327c3-28b7-3eb6-a9e6-d6b35ba43c08 | -13.6391 | -51.2766 | 2024-10-07 01:21:26 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| edc076f2-85a5-3651-99f5-4e78752f5857 | -13.2721 | -50.624802 | 2024-10-07 01:21:29 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 69216713-4114-3bcf-94bf-3dbd1bd9b8a6 | -13.2624 | -50.6273 | 2024-10-07 01:21:29 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 76ebc0fa-31ac-3fea-a0c1-bcebcba2a28c | -14.9236 | -57.931099 | 2024-10-07 01:21:29 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b46a5b50-5ca9-3872-a554-584d5a73796a | -14.8654 | -57.994801 | 2024-10-07 01:21:31 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5eee4762-bd0c-3479-a32f-bc51644299aa | -14.8672 | -58.002899 | 2024-10-07 01:21:31 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4613e318-9cf0-3ac6-9a39-849fdfc7b224 | -13.3277 | -51.314701 | 2024-10-07 01:21:31 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ab294da6-aeb0-3124-92ab-920b5bfa9236 | -13.33 | -51.324299 | 2024-10-07 01:21:31 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07051f97-2d2f-3b37-be04-13ffcfbbe0ff | -14.8574 | -58.005001 | 2024-10-07 01:21:31 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b94e8167-cb67-3943-b879-bb53d8030f0d | -14.8591 | -58.0131 | 2024-10-07 01:21:31 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7359256-03f8-3b24-835e-67a49ad4fb83 | -14.8608 | -58.021198 | 2024-10-07 01:21:31 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58871173-f911-38eb-8f72-4e8cb4cb5b0a | -14.8626 | -58.0294 | 2024-10-07 01:21:31 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85b71b42-7c39-32a5-9c1c-a40805c2533e | -13.3179 | -51.3172 | 2024-10-07 01:21:31 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2c4a81e5-2848-3a1d-9a3e-f510877409d4 | -13.3202 | -51.326801 | 2024-10-07 01:21:31 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 754cf23f-6b63-3d70-b335-bab0912b64b8 | -13.3105 | -51.329201 | 2024-10-07 01:21:31 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| df306c2f-5a3b-3c48-854a-9f72ffbe6257 | -13.1997 | -51.172001 | 2024-10-07 01:21:32 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c747f5e9-1bb1-3c63-bbf5-b879ad63cc6a | -12.8132 | -50.526501 | 2024-10-07 01:21:36 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c95f066-61c4-3b75-90c1-74008d3d4688 | -12.8159 | -50.5373 | 2024-10-07 01:21:36 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8889c5e8-038a-3bbe-9ebf-883e476a4f84 | -12.8186 | -50.5481 | 2024-10-07 01:21:36 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66de90a7-dd8c-389c-9a76-086346b53080 | -12.8239 | -50.569698 | 2024-10-07 01:21:36 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30420081-9c84-3c45-9986-34a383f040a4 | -12.8265 | -50.580399 | 2024-10-07 01:21:36 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8c62c6a-a131-3694-84b9-8d84c986203c | -12.8007 | -50.5182 | 2024-10-07 01:21:36 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c976788-42f3-33a5-abcb-83fa1997c9ce | -12.7786 | -50.512299 | 2024-10-07 01:21:36 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7089dfbf-f6b9-399e-8430-c45ede82bfa9 | -14.3213 | -57.561901 | 2024-10-07 01:21:38 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95a49cc8-6f87-3fbd-b83b-bb89dce998b7 | -14.323 | -57.569599 | 2024-10-07 01:21:38 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d4b48c77-ce6d-3b5f-a442-a17af87dd5e2 | -14.3246 | -57.577301 | 2024-10-07 01:21:38 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c811fa99-27a8-3308-97d1-f87387a597e3 | -11.926 | -50.078201 | 2024-10-07 01:21:48 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b489beb-f1bf-36e1-b469-0d99e6f65a12 | -11.9162 | -50.0807 | 2024-10-07 01:21:49 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f28e227-e196-3ffd-a94e-93ac81e4be0c | -11.9192 | -50.092602 | 2024-10-07 01:21:49 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33911e7f-5e23-36d8-8f35-cf40ee060e8b | -11.9221 | -50.104401 | 2024-10-07 01:21:49 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9f5098f-aae9-3716-8c2d-89cf71a76909 | -11.9251 | -50.116199 | 2024-10-07 01:21:49 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9b6cc0bf-819b-3294-83bc-bafa0b36e42b | -11.2875 | -51.387699 | 2024-10-07 01:22:04 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ba35acf5-87f5-3308-b946-d766fd460222 | -11.2753 | -51.380001 | 2024-10-07 01:22:04 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ed23b84-b4f3-3e57-9275-4b8fb9ff02ef | -11.2777 | -51.390099 | 2024-10-07 01:22:04 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d183554-da3e-3bf2-bcca-8ca6aa6edf41 | -11.2802 | -51.4002 | 2024-10-07 01:22:04 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a4dd50be-8cb3-38d5-a089-917175dc33e6 | -11.2631 | -51.372299 | 2024-10-07 01:22:04 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d5e821c-468a-32f1-b7be-42a56fad59d4 | -11.2656 | -51.382401 | 2024-10-07 01:22:04 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d56e0570-ac4a-3b5a-b9dc-4b6ea2055005 | -11.268 | -51.392502 | 2024-10-07 01:22:04 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6595f315-18b6-3aa6-a9ba-c4bcde57e95f | -13.145 | -59.687698 | 2024-10-07 01:22:04 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e8e6bb5f-ee84-3288-b2c8-e3088a051f9b | -10.9482 | -52.376499 | 2024-10-07 01:22:13 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| acc81d0d-8b09-3d46-bc8a-06b2cc24e5c8 | -10.9504 | -52.385502 | 2024-10-07 01:22:13 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac8cfb10-5b83-387c-968b-70386b7c1092 | -11.0986 | -54.0103 | 2024-10-07 01:22:17 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 497cca11-c052-3dff-96ca-29c8e5868c0f | -11.0888 | -54.0126 | 2024-10-07 01:22:17 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4987e130-2b5c-3b37-8f4d-e4611d8c3a0d | -11.0906 | -54.020199 | 2024-10-07 01:22:17 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 832d6e5e-9e12-3372-90e7-f127b343b798 | -11.079 | -54.0149 | 2024-10-07 01:22:17 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1628f1e-1cc8-3db4-bb04-4a155207be6e | -11.0808 | -54.022499 | 2024-10-07 01:22:17 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d770a369-2604-3c5d-9d00-7468fbc59c14 | -11.2553 | -60.377499 | 2024-10-07 01:22:38 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 244cd8e8-c365-3f58-a587-adec02d86be0 | -10.8619 | -63.8787 | 2024-10-07 01:22:56 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9e3123e6-fe6c-3fa2-83d6-8b738b7dbd61 | -10.8652 | -63.8946 | 2024-10-07 01:22:56 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a652ec83-13f8-384c-8ce7-9a3f109b9602 | -10.4513 | -63.1134 | 2024-10-07 01:23:00 | METOP-C | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f4d611fd-c9fc-3d42-a2ab-82370ba519d4 | -10.4541 | -63.1273 | 2024-10-07 01:23:00 | METOP-C | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fb26c4ae-8924-348c-9c3b-698f0ea5084b | -10.4416 | -63.115398 | 2024-10-07 01:23:00 | METOP-C | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c8d428e8-e736-3466-9f4a-ec9d61e26bac | -10.4444 | -63.129299 | 2024-10-07 01:23:00 | METOP-C | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bc91ef7c-43f7-3861-b428-4041bf56cbff | -10.3367 | -64.237503 | 2024-10-07 01:23:06 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b5f296a1-fcc1-3598-aed2-662f7fd8b7f3 | -10.327 | -64.239502 | 2024-10-07 01:23:06 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5a7c9b80-0c29-3f77-820f-67b5295d7eda | -3.3225 | -49.143398 | 2024-10-07 01:24:04 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09fc8572-cd20-329b-9fdd-8181c4fef9f0 | -3.265 | -49.117199 | 2024-10-07 01:24:05 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5f77f87-09dd-3858-8b93-2c76990ce3d3 | -3.3254 | -53.382801 | 2024-10-07 01:24:20 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21fd4b0c-43ce-3460-b8d2-dcf33d250acd | -3.0377 | -53.035198 | 2024-10-07 01:24:24 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b831f7d7-4545-3dd3-8d76-954585a26391 | -2.8785 | -52.883598 | 2024-10-07 01:24:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 833baa97-29a7-3cab-81b3-25184d7e8df0 | -2.881 | -52.894299 | 2024-10-07 01:24:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cd80ff4-40f8-3dfa-b379-b7a4ffb7c8b4 | -2.8835 | -52.9049 | 2024-10-07 01:24:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ad44d74-cbed-3fe5-bd83-1e8e48533be2 | -2.8688 | -52.885899 | 2024-10-07 01:24:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a007d659-5fe2-32cd-bfda-82b3dd4801aa | -2.8713 | -52.896599 | 2024-10-07 01:24:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b21c9eaa-8211-3d71-b860-7a5e48604f9e | -2.8738 | -52.9072 | 2024-10-07 01:24:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7b4da38-47da-30e8-90aa-4ff42d522a13 | -2.8763 | -52.917801 | 2024-10-07 01:24:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99cdf8a7-4cac-3be9-8614-64e327d618ca | -2.859 | -52.8881 | 2024-10-07 01:24:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af239c38-634e-31b2-9300-63e106dc5d56 | -2.8615 | -52.8988 | 2024-10-07 01:24:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf4ebf33-5e25-305d-b394-c802d31904bb | -2.864 | -52.909401 | 2024-10-07 01:24:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87d6c80a-a927-3abf-b5ed-78c913d5f9d5 | -2.7786 | -53.2033 | 2024-10-07 01:24:28 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83d6f37f-fe65-389d-be46-a029b9354f2d | -2.7664 | -53.195301 | 2024-10-07 01:24:29 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f58d44e-6222-3175-9318-75ed9c1f484d | -2.7688 | -53.205502 | 2024-10-07 01:24:29 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8afcef77-1cad-394b-80c9-e96f1a5ae4b8 | -2.7712 | -53.215698 | 2024-10-07 01:24:29 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 970d37bb-3b16-3755-bfcb-f5753b08be73 | -4.0747 | -59.119499 | 2024-10-07 01:24:30 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3bf6d24b-ae71-3ac8-97d1-3a2f44ea427e | -4.0763 | -59.126598 | 2024-10-07 01:24:30 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 200547de-0d66-3800-92a6-695f0f5bcf57 | -2.8096 | -54.348099 | 2024-10-07 01:24:32 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17b12766-1a2b-3dbf-b39c-50e9134b97de | -2.8117 | -54.356899 | 2024-10-07 01:24:32 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37855149-57df-35c5-9006-488969ca0c10 | -3.7394 | -59.320999 | 2024-10-07 01:24:36 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3fb4fb0c-1775-35cf-b65c-8936e8a177cf | -3.741 | -59.328201 | 2024-10-07 01:24:36 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dddbe68f-c8e8-3a89-88c4-e08b9b7b6b50 | -2.2204 | -53.677299 | 2024-10-07 01:24:39 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b91f46d-1f11-3a6f-83d8-b407658826f1 | -2.2227 | -53.687 | 2024-10-07 01:24:39 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 239b3d08-129e-370a-bd69-bf0e39bf5929 | -2.2249 | -53.696701 | 2024-10-07 01:24:39 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68a3179c-35d0-3e96-8480-db1d0e164a43 | -2.2106 | -53.679501 | 2024-10-07 01:24:39 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f09b8eab-1941-3030-8ccc-b4018148b3e3 | -2.2129 | -53.689201 | 2024-10-07 01:24:39 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32ea5d24-36a2-3bcc-949d-8457b683656b | -2.2151 | -53.698898 | 2024-10-07 01:24:39 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README24.md)
