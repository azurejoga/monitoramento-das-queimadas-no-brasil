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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c622a63b-5b65-3070-bdc3-303eddb076a2 | -6.63646 | -53.37389 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcbe5e3e-657e-36b6-9e2f-e51e1ec7b418 | -7.42743 | -49.26424 | 2025-09-08 05:21:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e58959e2-47dd-3166-91a5-304f889ac01c | -10.16484 | -61.1232 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3694bf5a-b8cb-3031-9ed6-a8008584c5e9 | -12.94222 | -54.76339 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 669c6dae-0cbc-3e3f-bee7-91d98ab5850f | -5.24899 | -57.12476 | 2025-09-08 05:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 72766418-29ad-39ce-9702-0b9eb7a48ede | -8.70255 | -45.31751 | 2025-09-08 05:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0751f143-c875-329d-8934-70b6d380c16f | -9.93365 | -60.51849 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f9043be-6043-35e6-83e1-de15233db943 | -7.8239 | -45.41065 | 2025-09-08 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9060f68a-1d90-3bf4-8169-cbaadfea54c7 | -12.61574 | -56.97971 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9a22e742-50a3-31c6-ac3b-8c8e70085478 | -10.08609 | -59.16561 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eece7361-fc08-36bd-845a-9ca1ca5e6edf | -9.07821 | -46.97601 | 2025-09-08 05:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7316a11-4bd9-3ba7-a08d-e747b2b31297 | -6.20522 | -53.26522 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cf30800-35bf-30bd-b408-f5d49f195a25 | -7.93648 | -61.79469 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffd40dce-9964-3775-bdb7-ca0a7014234f | -9.99938 | -51.64421 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6488845c-f6a7-3e62-84d6-0fd0034697cf | -9.88502 | -56.14277 | 2025-09-08 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4d4c81e5-4e3f-3208-8ecb-6e6433655c55 | -7.40046 | -61.63032 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2d589f17-eec4-39ab-8fcf-3e2ed2f26f3c | -9.09642 | -64.51646 | 2025-09-08 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 109e30be-d713-32c5-9060-7eb264b13286 | -12.62974 | -56.98631 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 13e64172-1af5-38ee-8a2e-231cb25e41dc | -10.14554 | -46.21028 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3092291e-8e9c-3d18-b1bd-b78fb18372a4 | -9.58112 | -48.2933 | 2025-09-08 05:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75f4765c-a473-330e-a51a-a769e9ca0095 | -6.84041 | -52.8488 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ef0858e-b3d5-39ab-a58f-c87f048cfa00 | -11.33651 | -46.57327 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1715747a-b767-34cd-9856-eac53a16293f | -7.39695 | -61.62974 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 77ca68b4-4386-3c58-a067-b2eb1b948f29 | -10.09057 | -59.1808 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e197096-c281-3bb5-9764-9d674eee7ae0 | -9.24547 | -57.06615 | 2025-09-08 05:21:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d58ae94-17ce-3591-90d3-2b762b40f987 | -8.93116 | -45.81287 | 2025-09-08 05:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d53773c-b9b1-33f7-8b00-de64681d5a5f | -6.72485 | -51.96021 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2a6faf03-ee61-3370-bcf6-1dab29684e38 | -11.85837 | -51.05287 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3b5a419-d917-36de-8c58-58b40bdfbd88 | -9.0924 | -64.51576 | 2025-09-08 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 40659e5b-570f-3621-8023-2dbcb06d0cd1 | -12.01499 | -50.38438 | 2025-09-08 05:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78d4204a-e604-3643-97cb-acda105cbf6f | -9.93581 | -60.10644 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58506af0-ae9e-3045-9e0a-e9ff5bde065e | -9.8269 | -47.77114 | 2025-09-08 05:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60022300-854e-38f2-85c9-0fc744f8c9bc | -9.20255 | -67.55544 | 2025-09-08 05:21:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a56a8f3-104d-3276-ae2b-9ec3385eea9c | -9.47066 | -60.49077 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3de81c77-57f9-3436-ae45-6e13b88facd8 | -9.13856 | -46.05677 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7c09139-deed-394a-946e-ccc4ee3d1d64 | -9.30684 | -65.82325 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88192ea4-f8a5-3423-b103-6f851b536955 | -6.87472 | -47.9217 | 2025-09-08 05:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ac6c4885-b760-3cbf-b0c3-61ba8a2af1b7 | -6.63811 | -53.36227 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2770762b-567a-3485-ad6e-068a3f41a89c | -9.85211 | -48.85422 | 2025-09-08 05:21:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8dcaaa54-f490-3685-8668-92c387ddb9e0 | -7.78746 | -50.75459 | 2025-09-08 05:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| baeeda2c-4474-306b-9454-030c94a2e563 | -11.77832 | -60.89194 | 2025-09-08 05:21:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ace76a1-3ae8-38aa-8184-f5c3f2a4bed8 | -10.2873 | -48.80341 | 2025-09-08 05:21:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a35dc8fa-28c7-3685-b1de-85077fbb16f0 | -13.72436 | -46.89166 | 2025-09-08 05:21:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b1398a7-9951-3551-b655-25058381ee49 | -11.33032 | -46.56544 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8912e2cb-be03-3df9-9d95-9a0779a755cc | -12.94951 | -54.80397 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ca6be6d1-40a9-3549-baef-35650fda3fcc | -9.45612 | -56.05068 | 2025-09-08 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d1443935-48ed-3882-965c-2ce02bcd9519 | -7.22425 | -46.19865 | 2025-09-08 05:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bf9e7c4-a383-3769-9205-75db3fa5dd42 | -9.85173 | -53.29987 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cc958e4-98e7-3974-84d3-88edf2272b8b | -11.65617 | -46.88235 | 2025-09-08 05:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fadfb20-f1ac-3cd7-bcad-ecb23d4dff7a | -12.83007 | -52.93488 | 2025-09-08 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8788f4f-1421-3436-9277-9c539a426b17 | -6.95323 | -62.93062 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e48043a-9d05-3bfe-af7a-baefdfd08eef | -7.11903 | -63.07156 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f952746-846e-39bc-8828-3b4e3af9b119 | -6.62923 | -53.3661 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57912346-d890-3017-9e06-fe6fc8bacdfa | -9.24898 | -57.06672 | 2025-09-08 05:21:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c47a4728-bd34-3cc5-9416-cd83b7e04932 | -12.89427 | -47.99939 | 2025-09-08 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c24b253-c276-371b-a501-43d1ead37fa1 | -12.87645 | -47.98026 | 2025-09-08 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a670542a-8a45-3b95-9a2f-0ff02f5f6ad2 | -12.61699 | -56.97105 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 88f0e62e-dbce-3c19-87c7-be76e0714482 | -12.89371 | -48.0045 | 2025-09-08 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03fa27be-c0d5-36e5-8491-5b691a2c073e | -12.72054 | -56.56913 | 2025-09-08 05:21:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3006fb1b-f71c-3d86-bfc0-7982119d6886 | -12.92858 | -54.76933 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f299f00a-b71c-365a-8c01-02aae80bdbc1 | -6.34902 | -55.55803 | 2025-09-08 05:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 84f628b7-c62f-3150-b9dc-7a4f439bc8ac | -9.60934 | -65.19095 | 2025-09-08 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c669c80f-5d29-37cb-a474-3cc1269b10fd | -6.86985 | -47.91501 | 2025-09-08 05:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e0dd3905-4065-3321-b6e7-bb1eb79bb7c2 | -11.0494 | -54.17135 | 2025-09-08 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c91b4abb-c86a-394e-bcae-5ab79452bff6 | -11.2099 | -55.0169 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 205a772c-d7c8-39ba-8100-90223d540766 | -9.33055 | -46.52762 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d1d0db0e-71f6-3d93-b1e9-2a78a88ff872 | -10.00671 | -51.62786 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2e579aa5-6b4f-3fd4-a5b4-6c9d13c07ef3 | -11.79486 | -62.74128 | 2025-09-08 05:21:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad969e00-b07f-3ed2-a541-9dbac693f7d3 | -12.8299 | -52.8981 | 2025-09-08 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 703664b1-798c-3bcd-a226-a819a8502330 | -6.62427 | -53.3417 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d0660de-423b-3268-a754-606b590f55d2 | -7.42793 | -49.26044 | 2025-09-08 05:21:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af670bf7-175e-3d97-a089-07088ccd0a74 | -8.1956 | -50.13416 | 2025-09-08 05:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e6ca8e0-1d3b-313c-9d37-b9c2ac47e9d3 | -7.39631 | -61.63367 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 36c19b45-ddf5-3857-99e7-cbc2ef98805c | -6.63211 | -53.34682 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f811ba7-51e5-3ed7-a940-ec7a01810eb1 | -6.84914 | -52.85015 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f67a593c-0b1e-3613-9083-c10e00c42c3a | -11.21898 | -55.01093 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3560b60-f6db-34f2-a757-0c56d41da6ec | -12.82533 | -52.9342 | 2025-09-08 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44f79fa0-9431-338f-810d-462be21df6d2 | -12.82468 | -52.93932 | 2025-09-08 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 58d21497-a405-3955-a18d-90e29ef41a26 | -7.78634 | -52.12442 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 805a0471-057b-3fd3-8aad-4a78fb6fb719 | -11.86326 | -51.05693 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f91b0d38-681c-3651-93db-4cbffff1ba73 | -11.86623 | -51.05872 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cfcf690c-c0da-3276-aa4c-871bd3f3275a | -11.38563 | -50.41782 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1cf476ec-a10e-3400-accf-12a214dba829 | -7.22971 | -46.20521 | 2025-09-08 05:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6813e666-8247-3c1b-a2a2-a0c6fa151231 | -7.81151 | -52.13456 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8406fcae-02dc-35aa-90b5-a76fe357b08f | -10.1485 | -46.21917 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9aed37a1-d6ba-3bc8-a85c-38d6d927cd6a | -6.62255 | -53.35326 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 551bcb81-e932-3293-8b3f-d469f6745414 | -12.19149 | -53.9081 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 293c979f-e0f2-3007-b24f-b9c79664d585 | -6.82868 | -52.80529 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74534de5-7caa-3e5d-be5a-cd8a9de201be | -10.79835 | -47.73418 | 2025-09-08 05:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c3272119-9d44-3c8f-bdde-999558a2ae78 | -11.0198 | -46.02834 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2126516d-9f0a-3aec-a6db-83a6fe63070e | -9.9484 | -60.14781 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d243d284-3947-319d-ac31-4de9bab5e83a | -10.87842 | -55.71727 | 2025-09-08 05:21:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee7fa5e2-acea-3a65-938d-4489e09d035c | -9.30248 | -65.82246 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e37063cb-bfa9-33af-8339-7a8e2965cb36 | -6.53933 | -49.50953 | 2025-09-08 05:21:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9cc6fa3-562a-316e-b5a7-ad877db256bc | -12.9469 | -54.79182 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75946b1d-451e-3dd0-8b62-684abd59e020 | -12.93904 | -54.78673 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7bf843ed-a237-3029-827c-747506e9b1f6 | -9.43163 | -62.362 | 2025-09-08 05:21:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86f01af3-09f1-351f-8c05-b307fa3b4e65 | -10.41272 | -60.8007 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32d31d3e-eb37-388e-bc67-8c061d0ff46c | -6.63459 | -53.359 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e37bfd97-8988-3c4e-b036-54c19dcdf539 | -6.19683 | -53.26387 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README78.md)
