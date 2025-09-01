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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48238bca-7c03-3b3e-a398-355dfcea8772 | -15.5867 | -48.321 | 2025-09-01 06:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| eb25f645-bff3-3fb7-8c04-084da5c58355 | -11.0572 | -45.123 | 2025-09-01 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 5f9b240d-b379-3be8-9a80-4139649ac47a | -11.0565 | -45.1691 | 2025-09-01 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| e1e4a3e7-92a7-3196-a72e-0e6d6cb92232 | -7.9539 | -46.4542 | 2025-09-01 06:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 8e9e390e-56dd-3a6c-90c1-08d745ba7d35 | -10.6128 | -44.3284 | 2025-09-01 06:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 29c2fd7a-1aff-3258-9251-5904f64527ac | -7.0948 | -44.3358 | 2025-09-01 06:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 165.3 |
| f5b5864f-f454-3791-a809-39a364c2e276 | -10.5937 | -44.331 | 2025-09-01 06:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 02026917-d694-3af4-b2e7-530e0b07cc75 | -15.5862 | -48.3435 | 2025-09-01 06:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 263.0 |
| 1ae4ca50-88f5-3262-a384-8239aeba6bbf | -11.0565 | -45.1691 | 2025-09-01 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 37eb915a-43d1-3e95-a0ec-f3a65a52fa51 | -15.7116 | -48.8809 | 2025-09-01 06:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| f6d76f66-45cb-3306-8835-8b76a74d68f5 | -10.6128 | -44.3284 | 2025-09-01 06:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| c0c54196-19b0-3b33-9de9-dd8a55c97327 | -10.0434 | -48.0998 | 2025-09-01 06:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 2deeb91a-224c-37b4-8356-d33763fa597b | -12.9387 | -56.9454 | 2025-09-01 06:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| a4f414c9-3637-3b36-896b-f10af2f68631 | -11.0568 | -45.146 | 2025-09-01 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 302.8 |
| 17569d7f-eee4-3604-a8d1-c1caa995aecf | -12.9197 | -56.9471 | 2025-09-01 06:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 30aa3a36-97f8-38a7-9b3e-3bb5d5e9f8a7 | -12.9194 | -56.9672 | 2025-09-01 06:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 116.7 |
| c2ede81b-0c34-35a5-b731-a0bdb4d7c5e8 | -21.7315 | -50.751 | 2025-09-01 06:50:00 | GOES-19 | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.7 |
| 6a123504-2137-3c13-92e1-faa6f7382dc3 | -15.5857 | -48.366 | 2025-09-01 06:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 56.3 |
| d1e2b5c1-2ff0-3b5b-84e3-ee12664b03b4 | -7.0948 | -44.3358 | 2025-09-01 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| b4f7a259-d092-3a99-aa81-c3e2753f60f0 | -12.9385 | -56.9655 | 2025-09-01 06:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 0194f146-fd2d-3e57-8403-8e2e84bed050 | -7.0757 | -44.3606 | 2025-09-01 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| d7a0d758-5eb1-3bc7-8f39-9fcfe3208d57 | -7.076 | -44.3376 | 2025-09-01 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 81b75a08-919a-34a5-b3af-5c45f4af81b6 | -6.8281 | -52.8143 | 2025-09-01 06:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 8b2f7075-3c41-3da1-8ac0-1d47c08c2741 | -7.9539 | -46.4542 | 2025-09-01 06:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 171.5 |
| cbfdebef-c748-3a6b-86bf-95d4a4f1e2f0 | -21.7322 | -50.7283 | 2025-09-01 06:50:00 | GOES-19 | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.7 |
| 9a0e50ad-cef4-3289-972d-e0d210af20c5 | -10.5937 | -44.331 | 2025-09-01 06:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 38db1db6-b889-337c-a064-799f0f61a001 | -7.9351 | -46.4559 | 2025-09-01 06:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| a16498bd-5379-3b41-9453-b57f65d0620e | -7.0946 | -44.3589 | 2025-09-01 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 38a07d50-e07a-3c2a-90c4-4fd63b38da64 | -15.5862 | -48.3435 | 2025-09-01 06:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 112.9 |
| b683740d-73d8-3292-abda-5b9f9fa3d352 | -15.6058 | -48.3402 | 2025-09-01 06:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| c9f5a4ec-58c5-33b5-80af-e7c6db15554c | -15.7289 | -48.9892 | 2025-09-01 06:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 8383c594-69f4-3e2a-b982-1a5669b46d31 | -11.0377 | -45.1487 | 2025-09-01 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 229.3 |
| 4c43089f-5b8e-310c-9180-6e8ae8400290 | -11.0572 | -45.123 | 2025-09-01 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 1b26f6e0-70b8-30a5-bb8e-5c8aabf153a4 | -11.0381 | -45.1256 | 2025-09-01 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 9ab2fc67-a903-32c5-8046-4125d905bb9a | -11.0572 | -45.123 | 2025-09-01 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| dff601cc-f287-3d89-b376-0c4c5103b465 | -10.0434 | -48.0998 | 2025-09-01 07:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| cfdfac6e-c9f8-3710-957d-baf5a2fe3585 | -6.8177 | -45.7025 | 2025-09-01 07:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 3ffc1076-02a3-3029-bffd-cd4d2982389c | -15.5862 | -48.3435 | 2025-09-01 07:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 1fc2a831-0985-3a8b-9fcf-c65c38ae26cb | -15.7116 | -48.8809 | 2025-09-01 07:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 9b74ecd4-5d3d-393e-aff5-a3a2eb759b5a | -7.0946 | -44.3589 | 2025-09-01 07:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 129.2 |
| e00351c0-123e-3350-86f1-3cf4c15e2be9 | -7.0757 | -44.3606 | 2025-09-01 07:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 891d941c-eac3-3cdc-a8f0-092d27d4135b | -11.0568 | -45.146 | 2025-09-01 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 232.4 |
| 7ac79715-093c-387d-a4ec-c86cefa6fcca | -7.076 | -44.3376 | 2025-09-01 07:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 8d3d4d33-242c-3c92-ab33-e86958bb6059 | -12.9385 | -56.9655 | 2025-09-01 07:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 8856bca4-7e4a-3dd9-a393-6e6f8a5b90b4 | -15.6058 | -48.3402 | 2025-09-01 07:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| d3f25bb2-9cfa-3a67-8241-ba85177d8356 | -11.0381 | -45.1256 | 2025-09-01 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 161a23dc-48c5-39e8-9552-e0e7971a6c4b | -10.5937 | -44.331 | 2025-09-01 07:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 84601b60-eb1f-3950-a34a-f2c1985142fb | -15.7112 | -48.9032 | 2025-09-01 07:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| f7290869-cf15-316e-ba4c-54c137dce45a | -7.0948 | -44.3358 | 2025-09-01 07:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 51342fd9-e567-3cdf-ad60-ac62d9b6714b | -11.0377 | -45.1487 | 2025-09-01 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 271.5 |
| 11cff149-6f6f-324b-9ac2-d206c78c73ce | -15.5867 | -48.321 | 2025-09-01 07:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 9501f400-f5db-3cf7-a1c5-c75fb4a2dc4c | -12.9197 | -56.9471 | 2025-09-01 07:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 149.2 |
| c0797c22-be97-3aef-b3bd-b415764d4280 | -10.6128 | -44.3284 | 2025-09-01 07:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 943d48bf-272f-329e-8daa-f737af663aae | -12.9387 | -56.9454 | 2025-09-01 07:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 18d573d2-23e4-30aa-99f7-59a13f620856 | -12.9194 | -56.9672 | 2025-09-01 07:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 45ee2cfe-e2f2-3a8c-a0a8-44ae5e83a4d0 | -12.9197 | -56.9471 | 2025-09-01 07:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 148.0 |
| c61c8241-d852-3fdb-8a18-084d9e757357 | -10.5937 | -44.331 | 2025-09-01 07:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 3af05c4a-cc0a-38d6-8c28-300c9643dda8 | -15.7112 | -48.9032 | 2025-09-01 07:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 844fa621-4888-323b-8638-1f23b07b76ea | -12.9194 | -56.9672 | 2025-09-01 07:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 134.8 |
| ad01417c-35a5-32e4-b08c-5a2faee174fe | -15.7116 | -48.8809 | 2025-09-01 07:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 17576368-16bc-3dd4-8e52-4bb39a54a271 | -7.0757 | -44.3606 | 2025-09-01 07:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 6a5cbbfd-11ce-326b-b8cf-de23370bffdf | -11.0381 | -45.1256 | 2025-09-01 07:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| adfdc13d-d4d4-3a67-82d6-ec24979ef1e2 | -7.076 | -44.3376 | 2025-09-01 07:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 4dad869d-5437-30c7-a40c-64789d795e99 | -11.0377 | -45.1487 | 2025-09-01 07:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 7542a1ee-0fed-3df6-9659-4040569ba4d3 | -15.5862 | -48.3435 | 2025-09-01 07:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 463ffa69-3963-3037-84a9-a516983a3130 | -15.7289 | -48.9892 | 2025-09-01 07:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| dbad4e84-7066-3b24-942b-8c0d9bf8e1bd | -7.0946 | -44.3589 | 2025-09-01 07:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| f81bc72e-3f9d-3827-aba1-83b5794ee7f6 | -10.6128 | -44.3284 | 2025-09-01 07:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| bdcd65ee-a8f0-3085-bc01-2e494c964dbc | -15.5867 | -48.321 | 2025-09-01 07:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 48313de1-a3cf-3e08-8706-261d8641e225 | -12.9385 | -56.9655 | 2025-09-01 07:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 5f009bf1-2abe-367a-868a-92e6b82459c2 | -11.0568 | -45.146 | 2025-09-01 07:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 204.4 |
| 61c6f38a-f00e-31bb-a531-3f1b6c4ed770 | -11.0572 | -45.123 | 2025-09-01 07:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 75f9e947-d3e6-3846-9b4f-df7837871b48 | -7.0948 | -44.3358 | 2025-09-01 07:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| d13a3b68-789a-3e13-a7b9-2b34a6000df4 | -10.0434 | -48.0998 | 2025-09-01 07:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 5220a2d3-fb81-3b1f-b386-29f93a3ba2a7 | -12.9387 | -56.9454 | 2025-09-01 07:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| baf17970-1271-3520-9d3d-ceedb7600bea | -7.09709 | -63.03348 | 2025-09-01 07:12:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6e24a981-66e0-3ef5-a2cf-3dd298da63f4 | -7.68691 | -61.08103 | 2025-09-01 07:12:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| f8038cc5-60b3-3fa8-8d0c-3b12f16e918b | -7.10714 | -63.03489 | 2025-09-01 07:12:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5173f3af-7653-32b8-be56-c978d732735e | -7.28581 | -60.66431 | 2025-09-01 07:12:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| dd627bd5-9b66-3c2d-81fe-7de8382e852e | -9.13945 | -65.83611 | 2025-09-01 07:14:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2b1a7d3c-656d-32b4-af15-e6b04e51b460 | -9.84363 | -65.04964 | 2025-09-01 07:14:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 70b60f63-d0cd-374a-8594-8e5c7279a4aa | -9.34885 | -65.41688 | 2025-09-01 07:14:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1d08693e-e2a3-3773-b22b-3d3bffd221df | -9.12748 | -65.54376 | 2025-09-01 07:14:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0b665e3b-2327-374d-80ab-86dfc780a05b | -9.45797 | -60.56609 | 2025-09-01 07:14:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 039b7603-69e9-3a11-ae67-b4b41e64c890 | -9.01325 | -65.69068 | 2025-09-01 07:14:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 12cbc6df-29a7-362e-b052-f57381b44bea | -8.73623 | -62.39979 | 2025-09-01 07:14:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f9c25792-95bc-30af-9b21-a5841628ad0e | -9.88762 | -65.00575 | 2025-09-01 07:14:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 19f807c4-775d-3b29-b328-ff2170ea264c | -9.14701 | -65.8465 | 2025-09-01 07:14:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 33a20130-f866-3a67-937a-6366eb786b4e | -10.09071 | -68.46918 | 2025-09-01 07:14:00 | AQUA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 762b9f46-80f9-3fd4-8d1e-b82af38660ca | -9.13781 | -65.5358 | 2025-09-01 07:14:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e34e1d5d-d5ff-307d-ab60-dd191c5f8515 | -9.69374 | -65.00565 | 2025-09-01 07:14:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3b68323a-39c3-346a-a29c-8a368d2d0737 | -8.63082 | -62.58475 | 2025-09-01 07:14:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1536f85b-be1e-34a2-92ca-eaa13c7c2f3b | -8.76607 | -61.4178 | 2025-09-01 07:14:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 37fdec9f-8dea-31b7-b0f8-1d1c5c8e08bc | -9.87555 | -65.02414 | 2025-09-01 07:14:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a69c14d5-6f70-327a-8def-9bc9d5cd13f5 | -9.4462 | -60.57005 | 2025-09-01 07:14:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| d505df5f-2d2d-33c2-93ed-b39b88b668d5 | -8.66531 | -62.9252 | 2025-09-01 07:14:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 78e04e4e-5ae2-3353-8ff9-e0ad1c093628 | -8.65949 | -67.24616 | 2025-09-01 07:14:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a06014e3-31b9-3c52-a6f7-d168997b1c79 | -9.17522 | -67.56223 | 2025-09-01 07:14:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 40ba4284-445a-3c9c-bfc5-e733efe84b05 | -9.13646 | -65.54507 | 2025-09-01 07:14:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 705a2d86-312e-3f96-adbd-27d9c0ca2d3a | -9.12882 | -65.5345 | 2025-09-01 07:14:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README98.md)
