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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6ec7f25-78fe-32e9-8dfb-0f5f6d53a7dd | -9.11514 | -49.43489 | 2025-06-26 12:06:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 065c2ac5-fe97-33a3-8ab1-5f214d8355fc | -5.48865 | -42.1455 | 2025-06-26 12:06:00 | TERRA_M-T | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 06bb0a16-c112-3deb-a7d0-96fd63e52c0f | -7.17925 | -39.67956 | 2025-06-26 12:06:00 | TERRA_M-T | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| d1befee2-f685-36a9-9248-0cebc945da2b | -6.77661 | -46.33383 | 2025-06-26 12:06:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 7fcc7ccd-6065-3918-b4a4-c2869e05ecfa | -8.80497 | -45.0126 | 2025-06-26 12:06:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 02b891c1-4e74-3af7-92e7-fff451d4fe2f | -8.07276 | -46.97026 | 2025-06-26 12:06:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 80a89d96-3fca-3da3-afc9-471bf101de33 | -6.63777 | -39.36889 | 2025-06-26 12:06:00 | TERRA_M-T | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 5b64bc0f-e131-3d0a-9f9e-802b4bde174a | -8.52085 | -39.57716 | 2025-06-26 12:06:00 | TERRA_M-T | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 1d167d00-5fe3-393d-8a01-c560e9dab57b | -9.12792 | -49.43695 | 2025-06-26 12:06:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| bbdc5da4-cbcd-3637-b67c-cd82b3c0e606 | -8.47854 | -48.26254 | 2025-06-26 12:06:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 09827f2e-c911-3c1e-8b8e-1038a5fea632 | -8.80509 | -44.58688 | 2025-06-26 12:06:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4ca488db-bbe5-3fc6-a436-7cc60acdac6d | -9.1144 | -49.44093 | 2025-06-26 12:06:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 49d2b6c7-7d0d-37ad-8c2e-8aa1f537e71c | -6.21698 | -43.36163 | 2025-06-26 12:06:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7b660b21-96fe-3ba4-b8cc-012d44e38329 | -5.92436 | -43.46878 | 2025-06-26 12:06:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 97d82bea-1b24-390e-85f3-c1b4f2cb99a8 | -6.95643 | -43.41585 | 2025-06-26 12:06:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 15c89ff8-525a-3644-b8d5-f95b65f19cef | -7.02592 | -44.56559 | 2025-06-26 12:06:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e67ebb6b-9864-3308-9af4-7da2d811d4ca | -6.89948 | -47.86182 | 2025-06-26 12:06:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 5d894454-5e8c-3df7-afdd-7c414368fede | -9.11769 | -49.4212 | 2025-06-26 12:06:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 7d2be007-44a3-38f3-9a5d-12f9540689b8 | -8.81429 | -45.01396 | 2025-06-26 12:06:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bf3067af-14d9-35ef-bb8b-994b2cd1c850 | -6.94751 | -43.41457 | 2025-06-26 12:06:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 84fe50d0-7676-32a3-884b-4245cbbd691e | -11.0988 | -46.63419 | 2025-06-26 12:08:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| cce8587b-b239-3435-9324-13f66acef97f | -11.01337 | -45.25067 | 2025-06-26 12:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 048ac2ae-4ee8-3b2a-bb6b-a85c0877d71f | -11.27119 | -42.33501 | 2025-06-26 12:08:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 10692aff-b8a8-3767-b106-8b168fb869f0 | -11.81316 | -47.51863 | 2025-06-26 12:08:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ef9d113a-e025-342a-aa56-37b3f610c3ca | -11.92415 | -47.84801 | 2025-06-26 12:08:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| d43b481f-d87b-3b4b-bd0a-d1b3a81a8c27 | -10.7182 | -47.51096 | 2025-06-26 12:08:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 0269660a-079f-39a8-b707-e4bde9de2bad | -14.2432 | -45.50785 | 2025-06-26 12:08:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 76c65b88-0e05-397c-8678-025891d0e270 | -14.20844 | -45.49274 | 2025-06-26 12:08:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0e50716e-008f-3670-b3b6-ebdae5786d3b | -11.27248 | -42.3258 | 2025-06-26 12:08:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| cf1c4e69-ea86-3af1-a734-3cae31f89b46 | -11.95094 | -47.02526 | 2025-06-26 12:08:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a458f7ac-9c3f-3c0f-913b-4119fed5000b | -11.06711 | -46.64126 | 2025-06-26 12:08:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8cad7902-c4a3-31fa-87c7-b85aa55473f6 | -12.80186 | -44.89892 | 2025-06-26 12:08:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 84f1f618-2f14-3653-b0fd-162fdd74dae9 | -14.207 | -45.50226 | 2025-06-26 12:08:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 79612b19-da5c-31da-9d4e-4d9eecde0fe8 | -11.01484 | -45.24092 | 2025-06-26 12:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 7c86fbbc-33f6-3b4d-9309-e22b3b5c3a4c | -12.48493 | -45.89758 | 2025-06-26 12:08:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 01bb31d3-f102-315b-bb95-7b6dbbff9020 | -14.24604 | -45.48877 | 2025-06-26 12:08:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 69c94b97-d6df-312c-b877-9300a9038487 | -14.24462 | -45.4983 | 2025-06-26 12:08:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 405bd033-5ee4-32d2-a520-b32f96f63cc0 | -10.71613 | -47.52436 | 2025-06-26 12:08:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 104d57ff-f19b-381f-aec7-3632fe1e2739 | -10.72213 | -47.51773 | 2025-06-26 12:08:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 3066388e-72bf-3cf9-926c-170c0ce89ff8 | -14.23558 | -45.49691 | 2025-06-26 12:08:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 9503dbe6-8a0f-3925-8c74-5b3826d18501 | -10.72885 | -47.51274 | 2025-06-26 12:08:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e1b47bf4-1edf-31f0-ab0f-b834807ea8b7 | -11.80183 | -43.78672 | 2025-06-26 12:08:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 3f6fcd8f-98f2-3ec9-a395-d208fa8d83e7 | -13.58828 | -45.25702 | 2025-06-26 12:08:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2075707b-d275-3c70-8ba5-11952201ca3a | -11.07889 | -46.63116 | 2025-06-26 12:08:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| b59a377e-53c4-39c4-9eab-4f4a5f0db3f5 | -14.23415 | -45.50646 | 2025-06-26 12:08:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 7a216c46-aabb-34f2-9e84-94e0d83aacd2 | -11.80053 | -43.79568 | 2025-06-26 12:08:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 9b632f69-2ad8-3fae-9bdc-8ea07a14b295 | -11.81132 | -47.53044 | 2025-06-26 12:08:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 7245505a-049a-3e6c-a014-174d96a41d9d | -14.21605 | -45.50367 | 2025-06-26 12:08:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| ef343452-2713-36fc-b5c6-b6a31da668c3 | -13.04612 | -39.92697 | 2025-06-26 12:08:00 | TERRA_M-T | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 6dea3a79-5a12-338c-b999-b888976bc1d1 | -13.16791 | -45.22888 | 2025-06-26 12:08:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4ce83e9e-bba0-3c58-aff5-deccbbdc0c49 | -9.121 | -49.4528 | 2025-06-26 12:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 1a3b30bb-cfe1-3e87-9993-2cc881fce380 | -9.1213 | -49.4313 | 2025-06-26 12:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 541d4b61-45f5-3d58-a776-2f4bb9b9689d | -14.2247 | -45.5036 | 2025-06-26 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 0bf22e21-9a90-3e45-9de8-46bb2d366d30 | -19.48403 | -45.32436 | 2025-06-26 12:10:00 | TERRA_M-T | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 91142012-666b-375a-ad02-956acef4a817 | -18.00776 | -46.01248 | 2025-06-26 12:10:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 190d731f-fe64-3745-8d9e-692b89f8f7fd | -17.84265 | -42.67455 | 2025-06-26 12:10:00 | TERRA_M-T | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| db2684fc-6100-3dcf-94fe-242ef2d1b575 | -18.00918 | -46.00301 | 2025-06-26 12:10:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 88351145-7eac-398d-b2d8-a416490f8cf4 | -22.12837 | -46.97154 | 2025-06-26 12:12:00 | TERRA_M-T | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9862199c-e544-368a-8070-e5df698bb047 | -9.1213 | -49.4313 | 2025-06-26 12:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 123.9 |
| d2cd475a-9f42-3ed3-af74-185d8b21d850 | -14.2247 | -45.5036 | 2025-06-26 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| bf67c46b-07f9-337b-b6ad-8fa2ec64a617 | -9.121 | -49.4528 | 2025-06-26 12:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 4bacecf3-12c2-3c73-9710-f213d1e2bc73 | -8.3541 | -49.2211 | 2025-06-26 12:30:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| f9094895-77fa-3d18-8a90-15fa8d5df98c | -9.1213 | -49.4313 | 2025-06-26 12:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 3c2b224d-4c25-3544-af0c-3d1bcfe1090f | -14.2247 | -45.5036 | 2025-06-26 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 6074ff78-8730-3c76-9490-9d4cd58c0172 | -9.121 | -49.4528 | 2025-06-26 12:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 67153804-ee1e-39a4-9a6f-fddb63f11666 | -9.1213 | -49.4313 | 2025-06-26 12:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 253cbf6e-3b0c-389f-ab2f-7f5ec6209285 | -14.2247 | -45.5036 | 2025-06-26 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 7f77680e-c012-3ab6-9349-ad0a1a8c6db9 | -9.121 | -49.4528 | 2025-06-26 12:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 60d29046-049b-32a3-8216-10db15100ec0 | -9.121 | -49.4528 | 2025-06-26 12:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 5a8d42cc-9877-3791-a0fb-57259b301ccf | -9.1213 | -49.4313 | 2025-06-26 12:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 159.1 |
| c10e875a-da41-36ba-9ddb-f8ec14242a9f | -14.2247 | -45.5036 | 2025-06-26 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| ba197911-decc-3003-966c-6d8fb75a5aa3 | -9.1025 | -49.4331 | 2025-06-26 13:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 47289ed6-10ed-30e1-b457-3ea53ecf8668 | -9.1213 | -49.4313 | 2025-06-26 13:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 8451d135-8586-3289-9d06-d453889b7366 | -14.2247 | -45.5036 | 2025-06-26 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 8b767049-64be-32cb-aa3e-caab1d45bace | -8.3541 | -49.2211 | 2025-06-26 13:00:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| b469ca6a-627f-3f48-9ff0-773dccd516d9 | -9.121 | -49.4528 | 2025-06-26 13:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| a1cddb1a-8c45-3011-b352-5bae29064950 | -6.118 | -42.5323 | 2025-06-26 13:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 83601cb6-37f0-3715-8f78-5246ad515b18 | -8.8195 | -45.0108 | 2025-06-26 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 0f8121bb-a1fb-37b7-831d-980ab0268314 | -9.1025 | -49.4331 | 2025-06-26 13:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 40e58ac3-57c3-3fb7-b1c9-c356a8feb636 | -9.1213 | -49.4313 | 2025-06-26 13:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 217.1 |
| 323e4c25-3cda-3700-87d4-7addeaa244f5 | -8.8195 | -45.0108 | 2025-06-26 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 8e9318df-d8e9-3439-9a4e-fc5272d07b76 | -14.2247 | -45.5036 | 2025-06-26 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 424329d9-5dae-32ed-8dd1-785a43271ca6 | -9.121 | -49.4528 | 2025-06-26 13:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 3cf87042-1766-3fee-ad08-ba064c556726 | -8.8195 | -45.0108 | 2025-06-26 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| ba74b4e5-7422-357e-908e-7eab2635a2ee | -9.1213 | -49.4313 | 2025-06-26 13:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 249.1 |
| 572de849-d1d6-3402-b5ce-9ee4dc00916d | -9.1025 | -49.4331 | 2025-06-26 13:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| c7f54fea-ec06-3f54-9a76-060747152cd8 | -14.2247 | -45.5036 | 2025-06-26 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| bd2709ce-29b4-3396-b47f-1164eff65e4a | -9.121 | -49.4528 | 2025-06-26 13:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 174.2 |
| c741ac0b-0e18-3a08-abc3-ce3450887187 | -9.121 | -49.4528 | 2025-06-26 13:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 1d1f5c22-bb80-3c1f-810c-dcaa78348648 | -14.2247 | -45.5036 | 2025-06-26 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 180.7 |
| c9ca415c-573e-34ff-bf6f-41ca0e827e9d | -9.1213 | -49.4313 | 2025-06-26 13:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 273.2 |
| 7d34e7d1-3476-38e1-a081-d8c3f71f6053 | -8.8195 | -45.0108 | 2025-06-26 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 1b30408a-996d-30af-8c5c-11a85df69c1a | -9.1025 | -49.4331 | 2025-06-26 13:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| e770706d-0c74-31b9-9793-30b1ce6ae384 | -8.8198 | -44.9879 | 2025-06-26 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 8260cda6-eb97-39ac-9928-aaa839104fda | -9.121 | -49.4528 | 2025-06-26 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 136d2f45-8edd-3805-aada-8560eb16f7ee | -14.2247 | -45.5036 | 2025-06-26 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 6142597c-28a7-3f50-b1d2-af9efd182260 | -9.1213 | -49.4313 | 2025-06-26 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 242.8 |
| 09eca325-1539-3f0b-97e1-8f90a3c00877 | -9.1025 | -49.4331 | 2025-06-26 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| d7ad4b80-1433-36a6-8404-5c676276b0d9 | -8.8195 | -45.0108 | 2025-06-26 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 6a1d40ec-efa9-3e78-bbf0-430049e28cef | -14.2442 | -45.5002 | 2025-06-26 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |


[Clique aqui para ver as próximas entradas](README23.md)
