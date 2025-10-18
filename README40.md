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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb597ba8-93e8-33e4-8992-d8762e2b33f8 | -6.27743 | -44.38054 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a252822f-a4f8-3c95-b706-3ea2053df522 | -8.31616 | -43.42117 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c1e0d33f-890f-3189-95b1-440b4edf509e | -4.97093 | -44.61365 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4861b11-adb1-3923-9ce2-50a8c80cf1e2 | -10.51598 | -43.40593 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a3a8617-320d-37f2-8e6c-028486dca852 | -5.75778 | -45.77902 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fdf6b178-c5a1-3e70-9b00-1ac2202bce02 | -10.22915 | -49.68353 | 2025-10-18 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 340536a2-0412-3583-b1a1-e6701ab2ede0 | -5.82509 | -47.53988 | 2025-10-18 04:29:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79a5796a-8cee-3675-b391-7beaf393410d | -7.80288 | -54.93983 | 2025-10-18 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f344322-7657-3e12-a370-d96aba777eaf | -5.86919 | -44.85038 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12437eca-9874-39a7-b6e4-41b26654b20c | -5.85449 | -44.3407 | 2025-10-18 04:29:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d488dd7-e2a3-3a32-affd-a5af991dfdaf | -6.30009 | -44.72705 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 328d8934-25ce-31a3-8221-a4b5f6828af9 | -10.1251 | -44.53728 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c38738e-8792-3999-bbe0-22b1347a6338 | -11.09681 | -44.70404 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| efe0ee67-8d24-3cc5-8135-3321bf57bb63 | -10.68183 | -44.56767 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b47ab99-dd97-3a5a-addb-ac0ce6c2a536 | -8.17301 | -47.0386 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71e624c3-8273-3f63-867e-b9152434d153 | -8.38341 | -46.2459 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56bd9e10-438c-30ce-84bf-bd9c39962d19 | -10.15168 | -44.52906 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| df2eac86-e072-3607-95d9-e40cdcce0f7d | -8.3856 | -46.23192 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a281b6ca-669d-3278-a1b3-cee8cc3c1acd | -10.50195 | -43.44935 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2272756f-7edc-3b8f-8708-2056e536c605 | -9.22224 | -48.58936 | 2025-10-18 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdad9873-d4d6-3d3c-9f43-e1f450da903d | -10.24352 | -44.04266 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f6881a1-e981-3c36-90c4-12317f0c0375 | -6.6128 | -44.21536 | 2025-10-18 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce01dc0b-0f91-3eb4-adc9-a6c048835ef7 | -10.49397 | -43.42509 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e4f5a56-1ba9-335c-8c86-8e8487936165 | -10.2411 | -44.05934 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25243994-d4b0-3455-bd22-f061e4d0ce68 | -5.51614 | -43.87388 | 2025-10-18 04:29:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3722a85c-b03c-3d4e-89f7-0c39f707f322 | -8.61271 | -40.19656 | 2025-10-18 04:29:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 75384f77-b87e-38f8-87a1-5fe0cf91c201 | -5.89959 | -44.76664 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c4a39fc-91ed-3ebc-8b4e-6aa3c6cf2d0b | -4.99067 | -43.85432 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52c2bfa9-c951-3667-a126-38ff39e3072d | -5.93171 | -51.55963 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f97ae5bb-7d56-3a01-b9fe-d46ece088771 | -4.6876 | -45.84888 | 2025-10-18 04:29:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9284b367-f371-3022-8913-eb48362d643a | -8.16636 | -47.03754 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4848420-9f3f-360e-9d09-00e7c6220409 | -9.89001 | -47.64927 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f720e26-787b-3793-bfa6-1e28d1b68943 | -8.36115 | -46.21366 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9cfbe7c5-d052-337c-a458-cfc724e49dce | -8.54427 | -50.0799 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09378a91-4fd3-3852-abc5-75721f6de85b | -6.13996 | -44.45528 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5adeea4e-5422-3bea-b97f-d9e051ef1956 | -6.24168 | -44.96996 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 252c4ffb-30c7-39c3-924b-e471a2890ff7 | -10.48581 | -43.42843 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0af4ab84-ed4e-3895-9f63-46acf943dc1d | -5.25802 | -47.24114 | 2025-10-18 04:29:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 460a2a16-8f66-3345-8d30-7784a8a3cfa6 | -10.85434 | -43.96087 | 2025-10-18 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12c7c083-c586-3ff6-a532-c47afb3190fc | -6.37286 | -45.77969 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1abb394-77d3-378e-b463-6c44e340db13 | -8.78972 | -47.94016 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cab760f-5688-3f94-8bfa-de6bce68163c | -7.14187 | -44.78656 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b92876e7-f214-39d1-9047-0e65c667f0b5 | -6.74613 | -47.37181 | 2025-10-18 04:29:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae09e1cf-0879-3d72-b799-cc81e62a29b5 | -5.6074 | -49.03072 | 2025-10-18 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 750030a4-198c-3ed1-96ce-fde3d5880768 | -8.71987 | -49.60015 | 2025-10-18 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dab7f41b-2ee8-3e72-a5ae-8dbf32f3b35d | -4.03758 | -51.15743 | 2025-10-18 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 187e3e2e-c674-3837-9a0a-0045fa3203c7 | -9.17703 | -46.72676 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ce69ab9-2e6a-389a-81f4-d8be3d9b69de | -5.20891 | -46.1898 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18451250-cab5-3532-b05e-d52565b9c613 | -10.24126 | -44.05692 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32c6dbd3-773a-3fe2-9f4c-6ba9ce7d289c | -10.62674 | -42.29792 | 2025-10-18 04:29:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| badb93fa-f22b-39a2-a7b0-7853c5edc722 | -9.99072 | -48.5484 | 2025-10-18 04:29:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26debfcb-069e-3d59-8426-3fa000439374 | -10.24 | -44.0653 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 821e22b7-cd3c-3b28-a736-369c352b0bd8 | -6.31194 | -44.31729 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3edccd1-537c-3e4c-9b02-1e84a006dbec | -6.49139 | -44.55332 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4367a00a-c935-3a6a-a853-07e6933d6626 | -5.90749 | -44.76049 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43aa9289-c6be-32c6-911d-65e52d586bab | -5.15145 | -46.27298 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4df70dac-50d4-31bb-a89f-2b84de5724b8 | -6.10758 | -45.85186 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c0848df-6396-365e-9e01-060fb3b4d237 | -8.7802 | -47.92738 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3cf319f-50b2-3dc0-b489-7c83ac9a5032 | -7.92961 | -44.13006 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d7676eee-b174-38d0-9f40-a45edf3e4a75 | -6.23522 | -44.15993 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c079fa47-a0ff-360e-8777-3349770db0e2 | -6.95969 | -47.73515 | 2025-10-18 04:29:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28d04505-3f56-3085-934a-708ffc742bff | -8.10486 | -55.08644 | 2025-10-18 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cf5c68b-6dbb-3fb7-b79b-58df17b6988d | -8.23388 | -43.99846 | 2025-10-18 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9a3fb00-7ce2-318b-855c-fc76f2c52c9b | -8.36201 | -44.76794 | 2025-10-18 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 464866e0-4feb-3c6d-a5fc-ecef17794547 | -7.00967 | -41.99229 | 2025-10-18 04:29:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 95894392-bdaf-33c9-b5e6-ef25199bf2a3 | -9.26177 | -43.74084 | 2025-10-18 04:29:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 656a6757-2d00-33d5-92d1-6e8d328d9349 | -6.22924 | -44.64577 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3f86291-81f8-303c-902a-0dbecefaaf12 | -6.87911 | -44.68342 | 2025-10-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b706dc9-7316-37ce-826c-64eb95012d40 | -10.14338 | -44.53608 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce0cd346-c184-39ce-bc55-e29febbdc594 | -6.31797 | -44.31361 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fdf6508-cfa1-3662-8181-3dc81252d3e9 | -6.9821 | -45.58721 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1aedc19e-28b9-3d98-8983-27650612ad0c | -7.96795 | -43.87817 | 2025-10-18 04:29:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fdf9257-2ba1-3fb7-8b94-9a737d55db80 | -10.50901 | -43.42732 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0cfef87-522e-3a32-bb02-60303fdb3fa1 | -10.79052 | -44.09119 | 2025-10-18 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ee03c56-7c09-3693-9579-d3ce386974d7 | -8.17634 | -47.03912 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4e4c284-1ec5-3cd4-803f-9ba05867a764 | -7.2997 | -41.94838 | 2025-10-18 04:29:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 496af2ca-295d-37a2-bdc1-d51a7c85df8e | -5.58303 | -44.18139 | 2025-10-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 26cee770-2ae8-328b-be3d-7ce8ee0dd78f | -7.36647 | -44.23518 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 840d2133-fe9e-3ff1-a109-fe7828c13a2a | -8.29891 | -43.38969 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 88f146a9-052a-3fac-9b0d-3031cd00c2e8 | -9.72456 | -44.54492 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 06f6d621-3ccb-3847-ba8b-28b4837d81f0 | -5.70585 | -44.19197 | 2025-10-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03977b06-53f9-3ccd-9b76-cc9191b94b06 | -6.49556 | -46.15878 | 2025-10-18 04:29:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 864b1415-07d0-3649-9742-6a4bb7f17085 | -6.74556 | -47.37535 | 2025-10-18 04:29:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e3c9861-c078-3678-a977-e61716c862b9 | -6.05663 | -44.52234 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcd22443-b354-3426-8d06-b287e7f04390 | -5.16602 | -45.2183 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3411c51-8cc3-3204-ad84-e8a5c5587557 | -7.85332 | -49.65542 | 2025-10-18 04:29:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43e7e4fa-7179-3c0f-a4cd-041b9085bd81 | -10.43178 | -44.91175 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 010741c0-1891-323e-b626-2fad6e5aaf80 | -5.56073 | -44.14342 | 2025-10-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d66fef4-6905-36c4-99f0-147ba2f764db | -9.91483 | -47.67833 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f060eff2-567a-3f8e-adad-40a5cbe4aa46 | -7.95671 | -44.11795 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d32100fe-caac-30d8-91a6-9fa4775f1531 | -10.08571 | -47.65173 | 2025-10-18 04:29:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 886891c9-1779-32a4-89ea-7dcc8593e0c7 | -7.9685 | -38.28163 | 2025-10-18 04:29:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3fdc3c5b-92da-3e21-9e9b-1dca2226ce69 | -9.26541 | -43.74144 | 2025-10-18 04:29:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 17b98b58-fa38-391b-b031-5d9c5a87d863 | -5.17991 | -46.07168 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57f86941-bfe3-3ead-bd19-4f07cdff08ff | -6.2237 | -47.03967 | 2025-10-18 04:29:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d86d8840-87aa-3385-8548-80507c504b04 | -8.27254 | -48.00369 | 2025-10-18 04:29:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94fcb693-776a-379d-b110-12ff7f7aec06 | -6.52715 | -44.90371 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb2681f0-1250-377b-bae9-f950dfeaec94 | -6.29724 | -44.7229 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1fc1346-3561-3444-abca-b272de6b7c6a | -10.67882 | -45.32524 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a58c5fdd-f1a4-3142-bd32-2b5261f4a5a7 | -8.54355 | -50.08416 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README41.md)
