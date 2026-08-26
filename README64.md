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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25d7dc18-5ba8-3186-86c8-c025f042ec40 | -11.42131 | -62.09254 | 2026-08-26 05:29:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 510d0210-5d59-3cd7-bfd8-47ad4489f7ac | -13.16097 | -51.34354 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61c216b0-5b0f-3dfd-947c-8a2c04743b5d | -11.76056 | -54.53046 | 2026-08-26 05:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c50ff726-e6b0-395b-a455-e0d85c319bb7 | -9.38966 | -60.57254 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c3af3da-fa84-3b79-aa84-40f7bc4bb8ba | -13.65724 | -51.84631 | 2026-08-26 05:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33b2002f-4b00-3264-9122-d5033ff3a93b | -14.58653 | -52.0298 | 2026-08-26 05:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95c40083-a38d-3c6e-a0d3-804e3262c763 | -9.44056 | -51.58604 | 2026-08-26 05:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d5a6c139-ac58-330b-a195-59caf1b7dc0b | -9.18298 | -59.38593 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de7dc45d-34aa-35ef-85b2-9b465044e440 | -13.26644 | -51.39122 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 114acae9-311a-3131-86d5-070e2c3d61d2 | -9.39243 | -55.97505 | 2026-08-26 05:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| afb3a471-3e8a-360d-b2f7-2612fecc43da | -13.8627 | -54.06041 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80c47e88-7d28-3c62-8ffd-73f2e907ca14 | -12.07958 | -64.24844 | 2026-08-26 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be072875-113e-325e-839a-9c7786c9350f | -13.24291 | -51.36039 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 4317d5ab-c53b-354e-8e96-59fcd9c6fae5 | -12.75253 | -46.47094 | 2026-08-26 05:29:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ce85411a-eacd-30bf-a1ce-02ce38b910fc | -13.24746 | -51.36794 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 965cc0c8-3555-3c63-ad90-f7493a84dce0 | -9.45946 | -60.53658 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 853b20cc-9633-3c2e-80ee-18fbec5fbd78 | -13.23967 | -51.38773 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 99b3aced-3c68-3f8a-a95c-f017fcb03b7f | -10.76363 | -53.99149 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cc9edd6f-df65-3649-b7eb-b8e6a1f7a608 | -13.24519 | -51.52221 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5157b69c-e62e-3a97-9699-9d036f3b8b95 | -14.31988 | -51.7272 | 2026-08-26 05:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 052d932c-d2fc-3db5-860b-fdff4408b27f | -13.19979 | -51.33815 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| b321ee2a-f1f0-30ce-8b90-6eacc2b281e4 | -10.7653 | -53.98672 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8dd58245-d70f-342b-a613-6ccf74734914 | -10.98678 | -60.78912 | 2026-08-26 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7ebe056-5035-36d9-8d11-c3f7f6f67e59 | -7.62559 | -63.36776 | 2026-08-26 05:29:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84e429d8-42a2-33d4-ba22-69938f4e1cf5 | -13.22406 | -51.36216 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3eaad01d-93fa-3b3f-b69e-30c51e128c51 | -13.36753 | -48.21719 | 2026-08-26 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ba07abaf-5a79-3f81-acd6-98f0cb8f932a | -10.75205 | -54.01084 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22caa84d-a30a-3a0f-97f6-433eee147281 | -9.06615 | -60.43662 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 561cf98f-4c43-32e9-a8db-1bffa5ba0a9b | -13.24969 | -51.52959 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8436c80-e7ab-3454-9699-3ec61f5d1c3a | -13.2421 | -51.36723 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 0fadc6f1-4c96-3766-91d7-a8dddedf2770 | -13.29063 | -51.45985 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 5867f26d-7702-3c14-bcb7-3933d3049993 | -13.30662 | -51.46193 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e9f63c04-815b-38de-b94d-05387d497736 | -11.74731 | -54.53257 | 2026-08-26 05:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b090bfcf-a08a-380e-81ab-c47595df3aad | -13.35939 | -48.23061 | 2026-08-26 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e52ebcd-a454-3819-970d-31361caae7f2 | -12.89808 | -59.91895 | 2026-08-26 05:29:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 462f7c32-4365-3151-818b-6850016a49fd | -12.16312 | -50.59696 | 2026-08-26 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 824c3e43-8668-3012-abef-a8525882f764 | -8.81798 | -62.32798 | 2026-08-26 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bd249fb9-c55e-366f-be7d-2f7fa8a5049d | -13.86425 | -54.06261 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b5bc292-d574-31f1-9e0d-928db4efe307 | -10.7565 | -54.01926 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dd1db0b9-abde-3377-a40c-9fd50a4da08f | -14.79263 | -48.79681 | 2026-08-26 05:29:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d97663b-9a41-3b1b-a557-f1f5cb3082fe | -13.33953 | -48.23009 | 2026-08-26 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e8b3e33-4a01-3b86-b1c7-cb2c6ddb78ce | -11.31188 | -55.20758 | 2026-08-26 05:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4a5bc62-52d4-3f30-a2b7-0a4b85d4e6a7 | -13.2509 | -51.5196 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| da1b2938-59ba-3367-ac7f-5b26a67e598e | -12.72554 | -48.37757 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5c7f9d62-4a94-37f5-847a-42c282101f48 | -10.75518 | -54.01979 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a2fb2857-9296-3998-a818-27ceaeceb812 | -13.23435 | -51.36694 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| f3bb5ec0-0695-37b4-8f7e-144cd586d3b8 | -10.41804 | -57.22783 | 2026-08-26 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 208e15e2-c875-3cdb-b616-7420de13c9bf | -9.45669 | -60.5325 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2afeb5f5-1a0a-3371-82a0-fbf209213dd1 | -13.60906 | -49.01479 | 2026-08-26 05:29:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4bde088f-57d7-378d-93b3-b3bfb15663b6 | -11.75154 | -54.5332 | 2026-08-26 05:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 84d69650-9c69-3a61-9828-cd9222dbf914 | -9.67231 | -55.07861 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a6443d9-b123-3395-8c06-ccdea98db14e | -11.18744 | -54.00212 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7f4b17e-e3d7-3e87-a512-a64f81acf48f | -13.27955 | -51.46187 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d6636bb9-9610-30ad-9ebb-fbe74ee10a8f | -11.96787 | -47.75476 | 2026-08-26 05:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03e6a156-261a-327b-9a15-2b316a9baaf7 | -10.98954 | -60.79322 | 2026-08-26 05:29:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85ac9358-b64f-3798-ab40-e2ab3c957290 | -14.32478 | -51.73125 | 2026-08-26 05:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 809f2134-8c8c-362b-b641-da45cc716c96 | -13.23755 | -51.35969 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| e6385d93-59f7-3dc1-ad58-6a67f59b170b | -10.78608 | -50.92045 | 2026-08-26 05:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13e937f2-f020-31de-937a-87042283fd6f | -13.25532 | -51.39324 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 9935a1d3-5418-3bac-86e5-53121e53dbdb | -7.90507 | -63.68475 | 2026-08-26 05:29:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c92fe752-b8ad-3a93-9b34-ccea1047d66a | -9.60325 | -55.11773 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| b5e770bf-3a0e-37ef-997b-4c23d780ec7b | -12.68299 | -48.40715 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b54d540f-b138-30fe-af13-2940d5775a8e | -8.81352 | -62.31081 | 2026-08-26 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0680ffb9-0125-3fa7-9672-7c6c8c43e9ff | -13.26685 | -51.38782 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 488322fd-1850-316d-a061-154a9e9cb7a0 | -10.99577 | -51.15318 | 2026-08-26 05:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f96aa2d-a3f4-3742-a7a2-921e9b84bdf9 | -9.16718 | -58.33382 | 2026-08-26 05:29:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cafcdff5-37a8-3274-8c7b-c1d5e6383398 | -12.03208 | -46.05056 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| b27ab468-a7dc-38ca-b49c-1a02027a2077 | -12.03377 | -46.03524 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 63ecd3f1-9dd1-32b3-83b4-0d2ea19f26ee | -13.24378 | -51.37856 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ff1ea435-49ce-3ad3-acb4-baa3cf980fa3 | -13.30213 | -51.45448 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 50c1ef6b-1541-3871-8393-32e29798ecbc | -13.23713 | -51.3881 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3a557b7c-c723-3fe6-b3d4-0f681b2ed750 | -13.18947 | -51.33332 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 5a7c27aa-b69c-356f-a7bb-ae3ffe6d8940 | -12.69529 | -48.41358 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2f0be903-45db-3448-bdb9-22e651317bfa | -10.75949 | -54.02044 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 065360d2-27b7-3896-b16e-f1d953a8eb07 | -9.20246 | -59.58238 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b14ef648-dcb1-35ab-9276-20442c70d14e | -13.23472 | -51.38361 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f287d337-0130-347e-96fd-407aec8795bd | -14.79212 | -48.80536 | 2026-08-26 05:29:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 500da956-b875-3a5e-b007-f1a4673e086f | -10.74899 | -54.00964 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0780fcf8-3158-3d24-9f8c-cb5720f748b4 | -10.42544 | -61.21781 | 2026-08-26 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0059f98f-81ec-3733-a4ef-4902209084ee | -9.13935 | -57.56332 | 2026-08-26 05:29:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed4bb99d-e268-3389-b71b-cc3950d85c3e | -13.19852 | -51.34843 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7683793e-6ef6-3ef1-8f28-4f320fa64bd5 | -7.77761 | -61.565 | 2026-08-26 05:29:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9e76582-ece3-39b3-8c95-e58c24203d39 | -10.75218 | -54.0186 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bfd459df-dcc5-3614-877c-cb4430ef659f | -9.13648 | -57.55894 | 2026-08-26 05:29:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7d4b298-c1b8-31bc-9db3-8527fdb14393 | -14.38991 | -51.76164 | 2026-08-26 05:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43adcdf9-a849-3477-83cc-cc481e37452b | -12.03484 | -46.03249 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 48159f92-7d48-3c0a-8756-444419bf1b16 | -13.24479 | -51.52555 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 082c2397-5b4f-3f85-8a28-a04a3da53853 | -13.85485 | -54.05048 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06ae1025-01ee-30a6-8f41-d4d8896835ea | -9.97372 | -48.32835 | 2026-08-26 05:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 393b7a21-aae4-39cd-bd0b-656797eed3b6 | -13.23007 | -51.51344 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bffe0211-74b5-33c3-baa1-1814133f00e0 | -12.0812 | -64.2418 | 2026-08-26 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6721b859-0341-3532-8c38-6518089ca7aa | -13.25049 | -51.52293 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 9d818bda-b313-3093-92c2-816699bb8e09 | -13.22321 | -51.36899 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 451cc51f-d2a2-3696-922b-d6f1b49129dc | -13.85635 | -54.05263 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5ceea411-3e2d-30db-a1bd-1827a3cff2ab | -13.23289 | -51.48995 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c66a7e1b-d635-3660-9086-00910c312329 | -10.76569 | -54.01644 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46b17490-89d4-3cf1-bfa8-302e2e9d86c5 | -9.47807 | -56.91694 | 2026-08-26 05:29:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a13dc7d-a0e9-3378-b2a0-b471700ee7e1 | -13.16675 | -51.34081 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 67a222e3-b59c-38af-a791-be1b7f6c5c83 | -10.01735 | -46.41998 | 2026-08-26 05:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e03ad91-f173-3470-a6b5-b18917d5a0f3 | -7.79584 | -62.39228 | 2026-08-26 05:29:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README65.md)
