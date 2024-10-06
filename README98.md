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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea6b2cb8-f47c-35d9-817b-444c092ee81c | -3.272 | -49.13638 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cc5d7612-1ce9-359b-b4e4-6cb8ff4b63d9 | -3.27182 | -49.13529 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 56d02ed4-3b3d-32b9-a6ed-88a1657a3f60 | -3.27126 | -49.14151 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f5d541c5-e83f-3ae0-96bc-4ee496c48848 | -3.27103 | -49.14042 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f14c55e6-fc14-3747-b454-eeb0b5a57b86 | -3.27025 | -49.14552 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71207ce5-0a02-33bf-8a75-4342dddf410f | -3.26874 | -49.12519 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c725a288-d72b-388c-927c-976a1421ee58 | -3.26864 | -49.12412 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c382280f-e4cb-30c7-aee4-ce328c6ba1b1 | -3.26798 | -49.13045 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5675d100-57b3-3ad6-b457-8491c411fb43 | -3.26784 | -49.12939 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 62e05f63-b16d-3cd1-a0ed-422f4f553201 | -3.13267 | -49.17976 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af0cd39a-9bfe-3ea4-9487-1bb1a515ed8c | -3.12869 | -49.17395 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3764e10e-f7d9-3949-a182-d27a78b55922 | -2.69335 | -49.06979 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d3c59b90-ed5e-3a3e-9da4-54a23d78ec02 | -2.6886 | -49.06903 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 73755ffa-69e6-3374-8121-3e38ebf928a0 | -2.67375 | -49.10326 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fa931c2-df5b-3465-bd0a-3022a9bfa652 | -2.53365 | -49.02059 | 2024-10-06 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5d7e8ded-e94c-3e95-8149-506565ab2e59 | -3.14952 | -50.22343 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| da8adf08-62f1-3291-b060-aa3be574ed05 | -3.14887 | -50.22778 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d4b4c7b4-2839-3dfa-8dcb-8fdc75bdf64f | -3.14822 | -50.23214 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 23fb8c57-ccd6-385b-8a2f-74d8cd6d0e91 | -3.14511 | -50.22274 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a3b994e9-f043-3c81-84d4-4ca81b93a159 | -3.1407 | -50.22203 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22552da9-2c77-376a-99e2-7cfee2777082 | -3.13329 | -50.4215 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54ef5bc0-f2bf-3a4e-ae38-b30c0bc27bc3 | -3.12892 | -50.4209 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cfab451f-2b98-3daa-a7b7-25471e22db05 | -3.12828 | -50.42518 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1f90c389-f4b7-39af-8c71-c66a0b43ebf0 | -3.12519 | -50.41604 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8704f8df-2555-38f3-84f4-a2fe833517e6 | -3.12455 | -50.42033 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 04884464-946b-3f43-ab8b-9a1e8240b920 | -3.12082 | -50.41547 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fc9fd3d-9707-3491-83b9-53e6d0eb09a1 | -3.12019 | -50.41971 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fdc94c3f-e81a-3d30-a653-65336efe62b6 | -3.11646 | -50.41483 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b81e061-92aa-3f6e-bd7d-0476b0ad9833 | -3.11583 | -50.41905 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7db90a03-f545-38d9-a6a6-976eee341f51 | -3.10772 | -50.47337 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3b6ea407-7e71-31bb-af96-10a7581d46f3 | -3.10463 | -50.46433 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a83d4700-a88d-395e-aa0c-5f0f20897bcc | -3.104 | -50.46855 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e8e57b7d-6153-30e4-8e73-820423eb0ed6 | -3.10091 | -50.4595 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 65a22331-73dd-327f-b5bd-7f63b6ea90d9 | -3.10029 | -50.46367 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0dffca40-291d-37de-bce1-a132c6ac60de | -3.09966 | -50.46787 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a776dd3e-b0d3-310f-a3ad-f077c237e004 | -3.09656 | -50.45884 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| ea62e479-d0fa-31ff-93da-b87b645d5884 | -3.09595 | -50.463 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 87ad1f1a-9fb0-326c-8105-a9566002d90e | -3.09532 | -50.4672 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f5c20d60-7cc4-3d3d-abac-5e4ece201a62 | -2.99191 | -50.28172 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd55a886-c5f8-352f-a74e-53b0818ff0c6 | -2.98819 | -50.27968 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd073acb-4588-346a-960f-44dc44f639f0 | -2.98753 | -50.28101 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30e36726-92f5-3793-b7c2-3285e57730e3 | -2.85415 | -50.47288 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5bf19d3f-7169-317c-b497-bc4928b96c7b | -2.85324 | -50.46233 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ff7534fb-e906-362b-990a-119b09f7ebbb | -2.85263 | -50.46648 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bdb46363-0252-34f3-9d53-c730645df767 | -2.85202 | -50.47062 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 06560ff2-834b-32a5-a298-75598c7eaee6 | -2.85174 | -50.45983 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 58cf8f11-1f12-34e6-868c-a686843bdf06 | -2.8511 | -50.46395 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 20c1a3f0-e464-32c2-b10b-1412ba80819c | -2.85046 | -50.4681 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 70068d27-8f07-3fb6-a0d0-0c645d7da7fb | -2.84983 | -50.47218 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7367ba4e-f7f9-34d5-9804-8b10c55783db | -2.84892 | -50.46164 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5bc850c0-c0ce-3a3e-ac8b-1598293994bf | -2.84831 | -50.46577 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| edc6ff04-a007-32da-9329-2c29a47d8f18 | -2.84771 | -50.46992 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3ea7be9f-801b-3633-acd9-9a278a980f92 | -2.84678 | -50.46327 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6d035fc6-3402-39ff-a41b-050b1ccdc628 | -2.84615 | -50.46739 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9ee9bf3b-98bf-3ae0-82d6-7953217e6adf | -2.8063 | -50.32033 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cfea0c01-59f5-35df-a1f3-612d0920c09d | -2.80567 | -50.3245 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff192b2a-360d-3f5a-b2d5-df93653743f8 | -2.80192 | -50.31973 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3e159e8c-c2be-35e1-a5e2-cb10db3d2973 | -3.50295 | -50.2714 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e3d215e5-83c0-3eb5-b718-4eee8ff8402b | -3.5023 | -50.27575 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3d2b867d-cad0-3405-814d-6cd2e4f649e1 | -3.49852 | -50.27074 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4bd7836c-771d-340b-bff2-64c577143ba0 | -3.49787 | -50.27509 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d9bf1174-a197-38c5-b6b2-d62b1a2044d7 | -3.47045 | -50.33732 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 223ac701-e43f-3981-8ea9-5d918077c63d | -3.46606 | -50.33658 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0254e033-c718-3b4f-a04c-1e13020e071a | -3.45035 | -50.32101 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49fa770e-4e8e-3224-8a26-c6f55ccd0b74 | -3.42943 | -50.1326 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13fdde97-32ff-3c63-8223-5a4211fa3858 | -3.42876 | -50.13698 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aea9413b-2548-3959-bc23-4b93389162b7 | -3.4281 | -50.14131 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 03701dd4-f4cc-3e2a-bd06-e28b4bd37336 | -3.42497 | -50.13188 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 449c45af-2950-320d-8c3c-9e484e18a86b | -3.42329 | -50.38251 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 6addf6cf-f5b0-3404-b1d7-e130311ec170 | -3.42266 | -50.38678 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| bfd90421-c6d3-3e2f-9a39-5ce9d0e55892 | -3.41452 | -50.38111 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 78362421-aaef-334d-91c9-b04ad737ff8f | -3.41361 | -50.38351 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f171a5c5-8ff5-3d47-9861-980c16723386 | -3.41014 | -50.3804 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4754011d-b099-3380-bf56-1831e2d4efad | -3.40988 | -50.37857 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c9d98ba6-7472-3f85-bedc-8febb404c220 | -3.40952 | -50.38464 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| de9bdd28-8953-39d3-b274-f69820820c6e | -3.40923 | -50.3828 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 52bb89ba-906c-3fb6-9533-675775232a0f | -3.40858 | -50.38701 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4a89b968-739a-3871-8aa8-74287387bc1a | -3.40514 | -50.3839 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8e154a5-a0bd-333a-936e-1b4f02af46e2 | -3.40452 | -50.38813 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3db036e6-a7ae-3d77-9dc3-33b95ab12368 | -3.40421 | -50.38628 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 78924ad4-fc3a-3679-8a7c-398d4160b001 | -3.37481 | -50.37305 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 527da1bf-4d80-3386-ba45-b9e5ced01df1 | -3.32148 | -50.07193 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67980660-dd03-3d44-892f-80b0efeac563 | -3.26239 | -50.13096 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b05e5bb-cb0b-3eb6-9b1f-4458aa61ea61 | -3.25894 | -50.21523 | 2024-10-06 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c08c8498-51b9-31e4-a083-741dd95f108c | -3.25793 | -50.13026 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecea5e51-a017-362e-b90e-554d93386238 | -3.24581 | -50.3633 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 725a074d-41cc-37a9-9fe3-cfb08684c585 | -3.24517 | -50.36754 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b221139-7a16-3936-9a1d-be75341413ce | -3.24454 | -50.37178 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e4c9b4f-9ab9-325d-b393-32a4715284f2 | -3.2439 | -50.37602 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5045ed52-5b9e-39c5-83d7-b5ec8703ffe0 | -3.24143 | -50.36261 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ce5eda4-439c-3900-bdce-b754ff28c892 | -3.2408 | -50.36685 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2eb65652-1f9d-3304-88a2-e3259ce2b028 | -3.24016 | -50.37109 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0db3bc8-9287-3fff-b471-a94c932a9078 | -3.23953 | -50.37531 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d8d87cf-77c2-39f6-9947-1398614e7735 | -3.23642 | -50.36616 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| be0801e6-f61c-302b-ba7c-fbe572a9d5c5 | -3.23579 | -50.37038 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 238f2c13-8fde-3c71-9a50-6fcc6f77b795 | -3.23079 | -50.3739 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96944b0e-3e54-3a06-b1a5-f0543ec60496 | -3.22767 | -50.36478 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 502e8c91-48a0-37c3-8fb4-80fb4613b79a | -3.22641 | -50.37321 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 939a4957-683e-3ff1-9a24-212e92e976db | -3.14757 | -50.23652 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1f8e76e2-913a-3c53-acc6-004ba6e50dfd | -3.14446 | -50.22709 | 2024-10-06 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README99.md)
