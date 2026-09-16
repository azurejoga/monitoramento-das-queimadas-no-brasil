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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c1ca39f-c535-3d28-915c-df989da195bd | -12.6064 | -50.7691 | 2026-09-16 17:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| a2889c24-7d1c-3eca-a20d-4eade19a7bbe | -8.9239 | -63.3371 | 2026-09-16 17:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 7254bf00-cd30-3c6c-bfbe-7a95e9f577ae | 2.2001 | -50.9397 | 2026-09-16 17:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 60f1c0af-3899-3a66-96f2-457a968e4e62 | -13.2277 | -61.8519 | 2026-09-16 17:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 0cbe8715-39fe-312e-835b-a1a5b8d3a789 | 2.2186 | -50.9393 | 2026-09-16 17:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 7a946c5c-5389-349f-b48a-56b71e64a566 | 2.2186 | -50.9185 | 2026-09-16 17:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 432bd5a2-997e-380f-9ed5-ac71f0d3d3ae | -10.8419 | -60.8202 | 2026-09-16 17:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 70c84154-e261-3f30-a1ea-c86840aae073 | 2.2187 | -50.8977 | 2026-09-16 17:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 55.1 |
| acad96e3-e95b-33ca-9e2e-6a1ec8506d58 | -9.3763 | -50.1139 | 2026-09-16 17:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| b3e9180f-f08c-3c65-b331-a6a5abc40c24 | -2.6968 | -57.5112 | 2026-09-16 17:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 4a751480-b538-3bd7-8b96-8b0abb7a1523 | -12.6826 | -54.6763 | 2026-09-16 17:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| aa6421a3-53f0-33bd-afd1-205f6ba5af92 | -12.6636 | -54.6782 | 2026-09-16 17:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| ef4a4b4b-b0a1-3560-a397-aa892e1cab71 | -2.6601 | -57.5702 | 2026-09-16 17:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 84ecf764-d97e-3ca7-9b1a-2ffe494e650c | -9.5725 | -46.601 | 2026-09-16 17:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| a3d9ad2b-238e-3d79-b949-6b60ca952972 | -3.4279 | -57.9816 | 2026-09-16 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 29a41270-c208-3168-8ebb-3eee609925b0 | -3.3871 | -59.4075 | 2026-09-16 17:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 3c3855d3-5e9d-3eb6-99c7-ed90cbc86219 | -3.4278 | -58.0009 | 2026-09-16 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 111.6 |
| d03aead4-6376-3dce-98c7-9fb02e463250 | -8.5431 | -44.4902 | 2026-09-16 17:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 214.9 |
| 8a23e7c8-3da9-3cb1-badf-43f28db60484 | -3.4278 | -58.0009 | 2026-09-16 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |
| a830c040-b6bc-3711-b528-137fc0f39ebd | 2.2186 | -50.9393 | 2026-09-16 17:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 32941d6d-6fe0-3f1e-b42d-a090ed1c2b1b | 2.2002 | -50.9189 | 2026-09-16 17:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 088e1079-8753-3e14-a657-14bba6f015f1 | -12.6826 | -54.6763 | 2026-09-16 17:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| a1a76750-0bec-39fc-9b62-3f2c76bff374 | -12.6636 | -54.6782 | 2026-09-16 17:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 5a025181-241e-3235-8bbc-5c55c49427fa | -3.4279 | -57.9816 | 2026-09-16 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 48c2656f-caea-3d84-92af-993c7019ea48 | 2.2001 | -50.9397 | 2026-09-16 17:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 65f9baf8-2176-3020-8b78-f4e8c4612876 | -12.1265 | -44.199 | 2026-09-16 17:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| ef494b75-356b-307d-8782-afd54fa0936b | 1.2793 | -50.8926 | 2026-09-16 17:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 250b57fa-f06f-3fa2-a918-a862b5f6679d | -10.8419 | -60.8202 | 2026-09-16 17:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| a4ebd89c-2250-3570-97c6-a1964628d3ac | -9.5927 | -60.5036 | 2026-09-16 17:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| a80dbe04-309b-3d5e-8c27-f8078ff466a5 | -9.3575 | -50.1156 | 2026-09-16 17:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| fd940f2b-e5d1-3df9-8a8e-9d6a819280f1 | -11.2693 | -54.0129 | 2026-09-16 17:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| b95491a5-ae55-32b7-bedd-eae8d4dfe1b5 | -3.4278 | -58.0203 | 2026-09-16 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 7367d81c-9235-31e3-9fa9-ad6c3fcbec3e | -10.8305 | -46.1796 | 2026-09-16 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 456.7 |
| 46c3fd96-52a9-31d1-81ab-6549fcc30eeb | -3.4279 | -57.9622 | 2026-09-16 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 1e30c451-0404-3721-81d8-c90572de6502 | -8.8585 | -44.9149 | 2026-09-16 17:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 127.0 |
| d935e6d1-6197-350b-b927-ab2a78f40ec2 | -9.3572 | -50.137 | 2026-09-16 17:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 3d115ca2-6f0a-3bc4-87df-0b72229a0de2 | 1.2609 | -50.8928 | 2026-09-16 17:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 0f65cba5-561a-38a8-859d-4569586b0513 | -3.4058 | -59.2347 | 2026-09-16 17:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| efb8ec58-25e0-306f-9e11-91601af5757b | -9.376 | -50.1352 | 2026-09-16 17:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 3828f3ec-7041-3032-86f7-cdf4c1b03d57 | -3.3871 | -59.4075 | 2026-09-16 17:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 5b08cdbb-4555-3e2b-8dab-be4d3050d824 | 2.2186 | -50.9185 | 2026-09-16 17:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6a33146a-55da-307a-b4b9-1ce90f539666 | -2.6785 | -57.5115 | 2026-09-16 17:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| d0fff67f-a5ad-3668-904d-fe04ef6c4221 | -12.126 | -44.2225 | 2026-09-16 17:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 158.5 |
| c42a8a01-0fc8-3b0c-9e4a-518fcbe0c3d4 | -9.5725 | -46.601 | 2026-09-16 17:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 340.8 |
| 3d7d7f57-f5a9-3889-b548-ccd52aba3dd7 | -3.4096 | -57.982 | 2026-09-16 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 6427cc73-c0fe-3009-b6cc-25b8039c1005 | -8.5428 | -44.5132 | 2026-09-16 17:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 231.0 |
| cb5ebe98-e181-3997-a60e-baebb0f639d8 | -2.6602 | -57.5119 | 2026-09-16 17:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 73106cc7-bd9d-3c70-8e1b-ed477b25d4d2 | -9.5729 | -46.5786 | 2026-09-16 17:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 74ff5850-d6a0-3dba-96cf-4a47bd7414e8 | 2.2187 | -50.8977 | 2026-09-16 17:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 57.4 |
| bd147ec8-9828-33fe-bacb-82ac43ee35f2 | -2.6601 | -57.5507 | 2026-09-16 17:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| bb75052a-3863-3b61-9808-e477b9764267 | -7.1384 | -42.1529 | 2026-09-16 17:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 358.2 |
| a0a44617-f096-39e1-881d-730d8f5040f3 | -12.6636 | -54.6782 | 2026-09-16 17:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| dfc30d81-f460-38ff-95a9-bf5bedb71fe2 | -11.2693 | -54.0129 | 2026-09-16 17:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 6d84823c-0e63-38d9-ba5f-3e2c6588c70e | -3.3871 | -59.4075 | 2026-09-16 17:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 77c13e0b-ad9d-394f-a756-287270c9d421 | 2.2003 | -50.8981 | 2026-09-16 17:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 72.6 |
| fdb9b5cf-5bcd-3bc4-847a-e4f05ccf76c0 | -3.3137 | -59.4664 | 2026-09-16 17:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| c4cb0751-0928-338c-8748-3d3a65c6179d | -3.314 | -59.3706 | 2026-09-16 17:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| ba9b2125-9826-304f-9529-23615b9e2989 | -2.6602 | -57.5313 | 2026-09-16 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 66a07226-a2b0-3886-a212-7d5ce253dd97 | 0.1747 | -51.4805 | 2026-09-16 17:40:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 1121c5d6-b769-3663-831e-be23114798f8 | -11.3633 | -43.9877 | 2026-09-16 17:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 274.4 |
| 79bfe14a-3eac-313a-87ea-91ae03b81f5f | -8.9239 | -63.3371 | 2026-09-16 17:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 9409a6fb-4a7d-369e-9ab8-c2a1879652d9 | -3.4272 | -58.1945 | 2026-09-16 17:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 106.2 |
| bb77a630-7007-3218-9115-6e50f94bc236 | -2.6785 | -57.5115 | 2026-09-16 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| ca2eb75d-bbca-3145-afe3-b8b33b41df84 | 2.1818 | -50.9193 | 2026-09-16 17:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 17ea2b28-c225-34a6-b6c1-8b214c07d84d | -11.2386 | -43.465 | 2026-09-16 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 413.6 |
| 9a295b35-b1f3-3e67-b9a5-75efaea66c17 | 0.1563 | -51.4599 | 2026-09-16 17:40:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 765b26a5-6263-3fb2-8604-b776af29cd53 | -8.5431 | -44.4902 | 2026-09-16 17:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 372.8 |
| c57157c9-89ef-3a3d-88e5-a6f213a5c5a4 | -13.7006 | -51.8061 | 2026-09-16 17:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| d4c070d3-9702-3962-9fe3-2c8bafaf4515 | -3.4058 | -59.2347 | 2026-09-16 17:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| b65068bc-7c0e-3d0b-a4ef-7ff1e781a297 | -2.6601 | -57.5507 | 2026-09-16 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 1c7e9a54-a9c8-3e78-b790-f054fe0f0584 | -8.5428 | -44.5132 | 2026-09-16 17:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 429.4 |
| 80c14629-c5ee-31aa-aa5b-183e8eb64f93 | -10.5246 | -46.2862 | 2026-09-16 17:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 210.6 |
| 4b72cdd9-c082-31b2-87ba-289d04acabd6 | 2.2187 | -50.8977 | 2026-09-16 17:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 2b84d55e-3e74-3dca-9a5a-aa462ea9fd34 | 1.0767 | -50.9572 | 2026-09-16 17:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 9edd51a3-3c2e-3eda-ad7b-7d9613c6ec54 | 1.2607 | -51.0175 | 2026-09-16 17:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 0c895e19-d290-377f-8d42-7960737ed949 | 2.2002 | -50.9189 | 2026-09-16 17:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a717ac4b-b1bd-3314-81c7-3406adebc841 | 2.2001 | -50.9397 | 2026-09-16 17:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 52b6a27c-721d-312d-a4bb-020a8d4b5b9f | -12.6826 | -54.6763 | 2026-09-16 17:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| a07f70cd-5df3-39aa-90d9-00f74f6c402d | -2.6784 | -57.5698 | 2026-09-16 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 74263999-ae27-3c1f-9fc9-99c30f412220 | -9.5725 | -46.601 | 2026-09-16 17:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |


