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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9905f6cc-a5d0-3734-b34d-ce3074b6a282 | -3.07465 | -50.50191 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd4ab33f-0f33-3204-9950-d1d3960313b6 | -3.07404 | -50.50595 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d67a266-1835-3c66-885e-62efedb3cf35 | -3.0717 | -50.49733 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 49d2ea62-8f35-3359-81b1-06dfbff7fa80 | -3.07108 | -50.50136 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7be81d6c-e623-3928-9ec6-251fd5ce9602 | -3.07047 | -50.50539 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80f9d8c3-45da-337f-ae42-45b48ab4d46b | -3.06813 | -50.49678 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64682ae4-548e-3799-bb31-d87d70e199f5 | -2.96319 | -50.52297 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34d77d2d-781d-353e-abd1-03197088d115 | -2.96258 | -50.52698 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c55dee0-95d7-35b8-841c-1992b5050e2b | -2.96196 | -50.53099 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2539f6c-65a7-3994-949d-868791d49896 | -2.96024 | -50.51841 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09a1e621-29c9-30e1-864f-b9f5077d6b29 | -2.95963 | -50.52242 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d799410c-119c-36bd-87b3-cf276f188fe9 | -2.95902 | -50.52643 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63ea3b80-1be4-3d86-bc1b-b3b9699ed0b9 | -2.9584 | -50.53045 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d3fa3e4-29d6-38ea-af18-d9d00172150c | -2.95729 | -50.51381 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 983f6e19-bbaf-30e9-bd79-a653c5e7cb16 | -2.95668 | -50.51785 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 091b9eb4-534f-35bb-b690-d792ed045117 | -2.95607 | -50.52187 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ff3e554-e93f-34f4-8673-bbccc94ac00a | -2.95545 | -50.52589 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62472141-4a83-3196-bd02-9d7a047a71f5 | -2.95484 | -50.5299 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e31cb58-e637-356b-b5e0-a682b7c2e672 | -2.95373 | -50.51325 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| caba6054-1187-3de1-a820-32872dedd4b1 | -2.95312 | -50.5173 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bbbc0bf-a7bb-36a3-94ff-c1344f1c3b65 | -2.9525 | -50.52132 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90cef6b1-56b0-3fc2-a60d-cdb0a15fffc5 | -2.95189 | -50.52534 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b123b20d-f7df-3a8a-922d-bfe8bf25bc6f | -2.95128 | -50.52935 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd7e17f0-3d8c-3eea-8447-3c51ab5349ec | -2.94969 | -50.52562 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e9d20ae-e453-305e-a601-cd11927706ec | -2.92749 | -50.48103 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff0bafea-3904-3378-bc74-6f93d222e795 | -2.86315 | -50.49586 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6cf6d92-aa99-3d4b-a2ce-d24c95c29a3a | -2.82424 | -50.49511 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 513c542d-ee78-3e57-8d4b-3f09f7ffaaf9 | -2.82068 | -50.49458 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8862d1c9-2f9f-336d-b5a6-9f4fccdc1e60 | -3.40289 | -49.53202 | 2024-10-24 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e56d33f-6206-35c8-bc39-950c759be9bd | -3.2456 | -49.75283 | 2024-10-24 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05d18def-651f-3ffd-9182-a73740780d2a | -3.23183 | -49.1156 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d03e46a-267a-3f66-ba77-c146ee7a8e07 | -3.22871 | -49.11024 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b620df40-6974-30fa-a246-51e8ab70f078 | -3.22797 | -49.11502 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b0671a6-1189-3053-b582-ac4e6d1340a1 | -3.22724 | -49.11979 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f576f03d-24f1-3d68-8d2e-3b75c2a40aaa | -3.22411 | -49.11443 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 897fa7d6-1d1c-34ff-b733-788f8805187f | -3.20794 | -49.62439 | 2024-10-24 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3661ec3d-8f42-39a9-aa1a-2100f975db8f | -3.20727 | -49.62886 | 2024-10-24 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 420224a5-f633-309f-bf38-38d32202395d | -3.00439 | -49.0369 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1065451a-b22a-354c-a358-404660385ff6 | -3.00053 | -49.03629 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b26b3f28-260f-3132-b604-f01f76962679 | -2.86791 | -49.45227 | 2024-10-24 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d58fa2ed-4467-3271-af5b-ab203dee23a0 | -2.86721 | -49.45678 | 2024-10-24 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e05dcfe5-0e0d-3a76-9212-c421d77aa122 | -2.86344 | -49.45622 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25a8b599-16d7-34db-a301-53797996dbab | -2.85458 | -49.33829 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27382116-decf-36d2-96ef-ff8d1dfd138a | -2.85388 | -49.34283 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7a7f18a0-da37-3cdf-8dce-2c570060a24f | -2.85009 | -49.34228 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a625fb5e-648b-34db-8e26-30a2bbcb28af | -2.83514 | -49.14317 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8af8333f-cc0d-390a-9d82-e392fd8eb38a | -2.8332 | -49.14501 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71e290c5-6d11-3715-88a8-fb9f885cddad | -2.83278 | -49.13317 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd248a36-50d4-3757-80c0-fdffdea772f2 | -2.80796 | -49.617 | 2024-10-24 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11c60ef2-db48-362e-b9c4-58a98dce97af | -2.80728 | -49.62142 | 2024-10-24 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c29d5e5-7a8c-3bd6-bb8e-a6aa6bc9e524 | -2.75958 | -49.30277 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 913a675f-4d81-32cf-8c03-616cd0369f65 | -2.68773 | -49.32172 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 903f3536-7d99-3e38-9055-f94b358c1092 | -2.68558 | -49.33541 | 2024-10-24 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 649764c2-f536-3ef2-8eb9-f4518368a601 | -2.65805 | -49.51129 | 2024-10-24 04:55:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d473f32-e6b3-3039-8211-28badf7e2900 | -2.6543 | -49.51071 | 2024-10-24 04:55:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae886480-f396-3e9f-b746-b835e52733b5 | -2.63866 | -49.38871 | 2024-10-24 04:55:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8c5f533-1795-363b-90c8-7b9cf5e3818b | -2.54488 | -49.66319 | 2024-10-24 04:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 623119f5-3a91-30fd-a158-e58648a9cb35 | -3.3019 | -50.01281 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c9fd08a-48a9-3e49-81ff-4bbb9ec2e816 | -3.29357 | -50.16341 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dad11577-3df9-372d-a5ce-8a0b186fe157 | -3.26945 | -50.07763 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3c677ba-3fff-38a8-9577-80801a6c16a9 | -3.2658 | -50.07707 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 533ca9d4-5e9b-3a15-ae9e-ed13e5e9f957 | -3.26146 | -50.15422 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2efd712c-968b-3063-882c-f8d9cea1f037 | -3.2559 | -50.1662 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 53c3722c-7fb9-3916-aebc-dc8e69a6b341 | -3.24969 | -50.18245 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1c00f89-77a9-38f7-986e-bb9a765d3e40 | -3.2467 | -50.17769 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edb785f2-bea2-3889-af52-5287d0c58ca9 | -3.24606 | -50.1819 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f6106e9-45eb-3042-a380-018b7b8d00a5 | -3.24542 | -50.1861 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0017d40a-e54b-355d-a07b-8222e11bc900 | -3.24306 | -50.17713 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c22bb420-47b5-3302-95b7-1f7aa0efb340 | -3.22616 | -50.16594 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 99035930-479a-3453-afda-2cb5d425d82c | -3.22306 | -50.16281 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82e01407-1b56-3dd8-b602-723ea046e644 | -3.22253 | -50.16537 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8e48e0ba-8ec5-3a11-b9a4-0e005a5ca606 | -3.2224 | -50.16702 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1b67bae-3448-3d02-9033-21974b568597 | -3.22189 | -50.16958 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7e8ed8a-52f8-32ce-8ff7-a4fc1433bef7 | -3.21942 | -50.16225 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ebf7d224-b63a-3020-8f38-e6f41000a8b2 | -3.21889 | -50.16481 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3697fc1a-b693-3f7a-8c36-5e0ce25ac331 | -3.21876 | -50.16646 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eed41a8b-bfca-30ec-8bc0-55ab17ffa9a4 | -3.21825 | -50.16903 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd57a3c2-ed15-357e-ad89-fff684c5fc00 | -3.2181 | -50.17067 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1734df2a-4179-31ac-b696-78e4f644726b | -3.21762 | -50.17323 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9806ef0e-55f5-36fc-b0f2-5444f29eedc8 | -3.21745 | -50.17485 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 633bb83f-9d48-33a8-808c-18e6ca9f96e0 | -3.21398 | -50.17267 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3451ac01-34e7-3a9f-b498-b12023b49be4 | -3.21381 | -50.1743 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c89f463e-9d5d-3e1b-906e-249009b69be0 | -3.19324 | -50.30996 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf72be69-a0fa-3d9f-8fb4-15fbf4b56eb8 | -3.16339 | -50.37836 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05997eb3-2d55-3d4e-a686-fc3df03f7b1c | -3.16031 | -50.25568 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0cf8605a-03b1-327d-b520-a6dc7f35fcc0 | -3.04563 | -50.27316 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46bbaf79-7a52-3dea-938c-41975f742bd6 | -3.04202 | -50.2726 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 557ef5f4-81d1-310a-902b-e2feded7bb73 | -2.97082 | -50.42508 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 69658de1-e598-3d24-b732-9f3abad45efd | -2.9702 | -50.42913 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 24826634-8814-3f54-a5e3-a2b03facfb9f | -2.96847 | -50.4164 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cf158b4-07c1-3c2d-bf42-6d3d8b4dcde0 | -2.96785 | -50.42047 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0e985b28-abc5-3847-8058-1e622f91157a | -2.96724 | -50.42452 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fd54cd16-6744-3b50-9906-472299584e4f | -2.96682 | -50.41687 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8a2784b4-a48e-397f-bd43-5780d0f83fb2 | -2.96662 | -50.42858 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9b5831fb-4681-3f82-9144-6c4ca67112fb | -2.96618 | -50.42093 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 43a82ad4-be25-3223-9dd3-bebaf06c49d9 | -2.96554 | -50.42498 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9e505875-0362-3a41-94c8-0b18e4b7b145 | -2.96491 | -50.42903 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 43c2788a-9eb5-36f5-a348-c38c2c583c5f | -2.96489 | -50.41585 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8ae3379-8d21-3134-a95f-88ede56dac42 | -2.96428 | -50.41991 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 565ae12d-83db-359c-b85b-b4ef18183fea | -2.96366 | -50.42397 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README64.md)
