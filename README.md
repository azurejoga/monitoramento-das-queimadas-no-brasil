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
| 86660adf-acb1-3511-a9cf-110730a1dc6e | -2.2131 | -46.5954 | 2025-12-18 00:00:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 206.7 |
| f2f94726-8cb2-35ef-82ad-f6a87578ca0f | -2.213 | -46.6174 | 2025-12-18 00:00:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 155.9 |
| d62d4a5e-58d0-3f9e-8cb6-0a28a9532d38 | -2.1945 | -46.5958 | 2025-12-18 00:00:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 48019e25-8439-3a0c-91fb-b4f16fc4cb38 | -3.1518 | -48.1598 | 2025-12-18 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| e5c30573-7e67-34c7-9af7-b666296ecd5e | -2.1945 | -46.6179 | 2025-12-18 00:00:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 7d076b6e-9b66-3305-bb12-9544bc8f02b9 | -3.1519 | -48.1382 | 2025-12-18 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| ac77cf88-24aa-3c27-9931-5a47d222cf2a | -3.1519 | -48.1382 | 2025-12-18 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| d7153fa8-58bd-3b47-a44f-07ff8083758f | -2.1945 | -46.6179 | 2025-12-18 00:10:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 014b1f32-48b4-3f0b-8fab-6957052cddde | -2.1945 | -46.5958 | 2025-12-18 00:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 0f8fb756-a75f-3f70-a222-ec303d10bfca | -2.2131 | -46.5954 | 2025-12-18 00:10:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 0f25b37f-7f09-3869-8f63-dfedf9143f7f | -2.213 | -46.6174 | 2025-12-18 00:10:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 8b8a3de2-addd-3f86-b5fb-6b848389c290 | -3.1518 | -48.1598 | 2025-12-18 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 21d8aa31-27bd-3453-9162-aa33faa9c00c | -2.2665 | -53.6616 | 2025-12-18 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a861f2e4-3916-3514-b6a8-14a3335a21c5 | -2.2131 | -46.5954 | 2025-12-18 00:20:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 128.9 |
| c607f540-c124-3371-8c98-ee355cfcb613 | -9.7008 | -36.2193 | 2025-12-18 00:20:00 | GOES-19 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 63.7 |
| cb63c030-3611-36b9-aac3-0ff2b04347e5 | -2.1945 | -46.6179 | 2025-12-18 00:20:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 60fef243-8666-34e5-867a-ff9337109aff | -3.464 | -44.989 | 2025-12-18 00:20:00 | GOES-19 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 96.1 |
| a55e0337-d3db-3c7d-a53c-d1449b9507aa | -2.1945 | -46.5958 | 2025-12-18 00:20:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| fe138d53-11d3-3ec5-a721-386c310210b4 | -3.4826 | -44.9882 | 2025-12-18 00:20:00 | GOES-19 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| a2289402-727f-3562-88f6-d51e96519e67 | -2.213 | -46.6174 | 2025-12-18 00:20:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 255d88dd-dc16-38a8-ac36-1594ba642847 | -2.1945 | -46.5958 | 2025-12-18 00:30:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| fe9f3912-52f2-3d1e-9e30-b62f6922b1e5 | -2.1945 | -46.6179 | 2025-12-18 00:30:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 8f814993-e2d0-38d7-979e-a40443354b51 | -2.2131 | -46.5954 | 2025-12-18 00:30:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 841e096c-aa79-3508-bac0-35978ac49bc4 | -2.213 | -46.6174 | 2025-12-18 00:30:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| b75505f5-ce80-3c00-b627-6ebafda32a31 | -3.4751 | -44.989201 | 2025-12-18 00:34:00 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6adb8048-f963-3052-aec8-9700c19cf76d | -2.9167 | -49.389 | 2025-12-18 00:34:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc32bf07-c567-361e-8bee-2e3f80aa085d | -2.9848 | -52.373501 | 2025-12-18 00:34:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3deea92-f5e5-33a9-9018-0d8932b2a6f1 | -2.8798 | -45.447399 | 2025-12-18 00:34:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd62a36f-d10f-34c8-8a29-2d94629bc6a1 | -2.2567 | -53.6488 | 2025-12-18 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ea4a1b4-c564-3487-932c-7f2ef90bd261 | -3.259 | -44.68 | 2025-12-18 00:34:00 | METOP-C | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cbd1a7cb-158a-3857-b37d-fab9c9da81c7 | -3.2137 | -45.152 | 2025-12-18 00:34:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 461989a4-6a8e-374d-9342-e819c4c139aa | -2.6681 | -46.901901 | 2025-12-18 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2fa9fe2-b18d-3db2-969c-fed2081dce89 | -2.1999 | -46.615101 | 2025-12-18 00:34:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61469e2b-339a-3e33-8205-d7194bf961d7 | -1.7435 | -47.187901 | 2025-12-18 00:34:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 390f43fb-7760-3853-ae09-ed03af346aa3 | -3.1401 | -48.152302 | 2025-12-18 00:34:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72b0c9cf-c9db-37de-862d-a9bfeab072a7 | -3.6633 | -47.5541 | 2025-12-18 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e46da679-3cb4-3995-8b75-da499676663f | -2.8896 | -45.445202 | 2025-12-18 00:34:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 484c4316-afe7-3e33-ad6c-63a5b6de49b4 | -1.5166 | -47.367802 | 2025-12-18 00:34:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ecaf391-d424-389e-95cb-400ea055c783 | -21.2321 | -49.365002 | 2025-12-18 00:34:00 | METOP-C | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2a011166-0bae-3e1c-867d-72a59b658d68 | -1.515 | -47.361 | 2025-12-18 00:34:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51153ec7-9612-3d98-b8d5-08482fa103c6 | -3.4021 | -49.212601 | 2025-12-18 00:34:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6c41e65-6c47-3a76-aa71-27be677215f4 | -3.7788 | -47.7435 | 2025-12-18 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3734509a-22c7-3e1f-be96-c8d17a594de5 | -2.406 | -44.7817 | 2025-12-18 00:34:00 | METOP-C | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eefa7820-6b5c-3136-8f1b-e303ee210516 | -2.2065 | -46.598999 | 2025-12-18 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61b95aa5-506f-30f0-b2d8-c9e747adc237 | -2.6634 | -46.881401 | 2025-12-18 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a80a009-aee6-30e2-a6bb-26cd125553f9 | -2.2097 | -46.6129 | 2025-12-18 00:34:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89c92209-7738-3634-9d8a-059434b7984c | -3.0706 | -49.385799 | 2025-12-18 00:34:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3f224cf-96de-3af4-83db-749de2d473a1 | -3.212 | -45.144501 | 2025-12-18 00:34:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e83306aa-0b1a-39e9-8696-61e041f06de0 | -2.9945 | -52.3713 | 2025-12-18 00:34:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac9d0ad7-dc0b-3a76-90cf-5f6238265209 | -1.7354 | -45.851898 | 2025-12-18 00:34:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78530d7a-cf2f-30f6-acca-43062e0e63d4 | -2.4078 | -44.7896 | 2025-12-18 00:34:00 | METOP-C | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1af4019e-ac33-3e7d-8d79-6dbf2ebd11df | -2.439 | -47.1618 | 2025-12-18 00:34:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ca3e883-844c-3306-be31-5a12b68ec43b | -1.7451 | -47.194698 | 2025-12-18 00:34:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be332428-491f-3cf3-bd70-d17623645f9a | -2.6665 | -46.8951 | 2025-12-18 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 268ebce0-4420-39e8-9555-c55da596f515 | -2.9134 | -49.374401 | 2025-12-18 00:34:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf0d8a5e-ab2a-3117-beb8-c477bf37ccb3 | -2.665 | -46.888199 | 2025-12-18 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c87dee0-d8b2-37c6-bb26-a7d32c6d22fa | -2.2081 | -46.6059 | 2025-12-18 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9ab1882-24d4-3031-9974-900db0c9f8eb | -2.8133 | -49.205898 | 2025-12-18 00:34:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 726e1ff5-9d58-3783-804f-28dc24c7f128 | -2.8481 | -45.400002 | 2025-12-18 00:34:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2413b4e3-a20d-3f4e-8384-ecca64b010af | -11.9074 | -43.830002 | 2025-12-18 00:34:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f03b91ba-73ff-3d9a-b9f0-0e1d5f916c3a | -11.9057 | -43.822701 | 2025-12-18 00:34:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5dadce7d-acff-39c7-a96a-4ab7ced5f096 | -10.3825 | -36.945599 | 2025-12-18 00:34:00 | METOP-C | MURIBECA | SERGIPE | Brasil | 2804300 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b3fdeb3d-4261-344d-a76b-cd20187d6f0d | -3.6618 | -47.547298 | 2025-12-18 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4171078d-2d28-3ee4-bb98-3671c13a562c | -2.915 | -49.381699 | 2025-12-18 00:34:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbafc5e0-2bdd-31e9-b7b2-cc703a66b6b9 | -2.8067 | -49.131699 | 2025-12-18 00:34:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4373127c-1785-3710-a3bf-5cac3a1cb3e4 | -2.8781 | -45.439999 | 2025-12-18 00:34:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f2cf743-7392-343c-88e9-66e1adad76bf | -2.1983 | -46.608101 | 2025-12-18 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 998785c2-d2e1-365b-b956-7d4f11b3b3c2 | -3.2014 | -49.372299 | 2025-12-18 00:34:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d22267e4-ca38-3736-a845-85add711a43c | -3.1997 | -49.364899 | 2025-12-18 00:34:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87a1c32f-6bd3-3cd8-add3-a3c5e3632fad | -0.898 | -47.9991 | 2025-12-18 00:34:00 | METOP-C | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0bb3a58-4e06-3b62-a687-1b428bcb1fa7 | -3.0722 | -49.393101 | 2025-12-18 00:34:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0041d3a1-e04c-33c7-8bcd-06ad951808c7 | -2.8464 | -45.392601 | 2025-12-18 00:34:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d86eeb55-cb5e-3b5a-93e9-2660b5edf6e7 | -3.4734 | -44.981602 | 2025-12-18 00:34:00 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c25fa1df-f7be-31a0-a78a-9b457ae5ba52 | -2.1967 | -46.6012 | 2025-12-18 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e283aae9-74a9-303c-8fc4-5e293bbbeaca | -2.2049 | -46.591999 | 2025-12-18 00:34:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9304293-8871-3b03-8e5a-711fa978c8e2 | -2.2594 | -53.660999 | 2025-12-18 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6749998d-a0d2-3e1c-bb2e-747abd88a09c | -2.9847 | -45.454899 | 2025-12-18 00:34:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ac8fdfd8-dd25-3515-8f34-4d164b7022c8 | -3.6688 | -45.8265 | 2025-12-18 00:34:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8c5d532c-8afb-34f5-86f8-0163c4c5f023 | -11.7662 | -43.313202 | 2025-12-18 00:34:00 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1747fdf7-1615-3af7-a7a0-2b069221651b | -2.4374 | -47.154999 | 2025-12-18 00:34:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a4bdd72-34ec-3404-a53f-70224aea5441 | -10.3776 | -36.9268 | 2025-12-18 00:34:00 | METOP-C | MALHADA DOS BOIS | SERGIPE | Brasil | 2803807 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 09e57ea6-dfc1-3761-b071-4690a8fcb4b1 | -0.7974 | -47.1105 | 2025-12-18 00:34:00 | METOP-C | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b92a1da-37e1-35fb-8879-751ebdaf87c1 | -2.1152 | -45.352299 | 2025-12-18 00:34:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a35c6f80-d4a4-317b-afc9-a2a5eb4293e2 | -1.6219 | -48.547901 | 2025-12-18 00:34:00 | METOP-C | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31b1f846-fae1-357b-af69-bf58f9491e90 | -0.8965 | -47.992298 | 2025-12-18 00:34:00 | METOP-C | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f17a2977-3197-36ac-b8a8-a1296e896360 | -1.6234 | -48.554699 | 2025-12-18 00:34:00 | METOP-C | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b73a1571-ee2e-3cca-a716-914f2c8d0174 | -4.4599 | -45.767399 | 2025-12-18 00:34:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0dc45e29-e2d0-3aa5-aa99-617b40b3ceda | -11.7644 | -43.305599 | 2025-12-18 00:34:00 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b7d748c-f86f-3010-bfa3-8e0b9d7aa29f | -2.213 | -46.6174 | 2025-12-18 00:40:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| b3fb723e-89e5-31c8-b50c-7199693654c9 | -2.1945 | -46.5958 | 2025-12-18 00:40:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f32eead5-d44a-3725-968c-e7cf93c6e7b5 | -2.1945 | -46.6179 | 2025-12-18 00:40:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| d716bf8b-b6b3-391c-9d6e-67c5c8ddc1e7 | -2.2131 | -46.5954 | 2025-12-18 00:40:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 5eafd657-779f-323d-a5b1-0a9bca66b290 | -2.1945 | -46.6179 | 2025-12-18 00:50:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| d34dee6b-4f7e-3e5d-828a-1eed041e75b1 | -2.2131 | -46.5954 | 2025-12-18 00:50:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 96a9eec9-4a12-38f5-a326-d4d85dc32b41 | -17.8157 | -40.1897 | 2025-12-18 00:50:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 98.5 |
| c03347a0-1bfc-3c09-a450-986cba7f3a42 | -2.1945 | -46.5958 | 2025-12-18 00:50:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| eed3ff96-99c7-37b9-b195-7514ae959777 | -2.213 | -46.6174 | 2025-12-18 00:50:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| bcf2942b-15fc-31e3-882a-be3be250b0ef | -17.7954 | -40.1952 | 2025-12-18 00:50:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 93.0 |
| cd400f4b-ab8d-376b-91aa-b34d3e61e3f0 | -2.2131 | -46.5954 | 2025-12-18 01:00:00 | GOES-19 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| e9a49301-3969-36c4-843c-28e2776909bd | -2.1945 | -46.6179 | 2025-12-18 01:00:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |


[Clique aqui para ver as próximas entradas](README2.md)
