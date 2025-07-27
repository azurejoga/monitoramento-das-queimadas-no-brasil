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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 496e37ba-0047-3c8e-8bff-3a9128e70a3f | -6.65208 | -58.84769 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d09772f-2c6a-3185-b684-411bde279ad6 | -6.68259 | -58.84903 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cbac55e-40fe-38ed-bb49-4ff766febda4 | -6.62864 | -58.83466 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3284436f-6703-3ecd-9d4c-1f4e99133dc7 | -6.66172 | -58.85199 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 73c955fd-2417-3632-93f5-34064e942a67 | -6.65167 | -58.85241 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0652ec41-2a5f-3f6b-b547-95771d3e8d5a | -6.6274 | -58.84336 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bea673e7-b5e5-39b1-bb48-a382f1f2208f | -6.65292 | -58.84381 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38eef731-66ad-3ad2-a6dc-55e2b9913f1f | -6.64458 | -58.83068 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 525c0220-655c-3e4e-8dce-c6a32ab4a413 | -6.63325 | -58.83825 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41f5c1ae-b13c-33e3-909f-e83e5d17a610 | -6.65248 | -58.8448 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94144bc6-3d10-301a-a1b9-12fe8f6914a5 | -6.66004 | -58.83004 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba0dae00-1c74-3ca6-bb6a-94fc7c0b0ae2 | -6.66331 | -58.84044 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 496b3fb8-360a-3fb1-a464-b612a0032264 | -6.62998 | -58.861 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e597c582-9bfc-3445-8636-533b1e1dea9d | -6.65447 | -58.83023 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 880c4862-1186-3f58-99c5-d4f27a16cad8 | -6.65793 | -58.84454 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5304279-aa9a-370f-b616-f081ae241a91 | -6.66673 | -58.85271 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d5aaf94-6d83-3b4a-a00b-de1b489b70cd | -7.90015 | -63.52828 | 2025-07-27 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45a39e76-77e9-34c7-8fc0-3b6b434ff76f | -7.60357 | -61.2145 | 2025-07-27 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| bbb9af7a-4a84-3197-b575-7122a0f74bbf | -10.0434 | -59.10212 | 2025-07-27 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 633bbe86-0f9f-3d12-a39b-26d2cfc66660 | -6.49039 | -56.19958 | 2025-07-27 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d10cfe00-13d9-39ab-8b98-f589faa1d9b0 | -6.53725 | -56.19165 | 2025-07-27 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 38f7a75a-fa90-3580-a98a-ee0bb1e897b2 | -7.60458 | -61.22057 | 2025-07-27 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 50818b6d-8b7a-3717-90f1-d664419e9e33 | -6.62699 | -58.84623 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93d936c9-76fc-30eb-a266-0caa692bbed7 | -7.28997 | -60.18636 | 2025-07-27 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0ea7aa4-0e41-3eeb-8218-9bd2eabee282 | -6.54862 | -56.19757 | 2025-07-27 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07d9a2f1-9298-3a99-9480-8803286aafc4 | -6.48977 | -56.20393 | 2025-07-27 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3ad23cc-f35e-38d1-93ef-e41c5eccbfbe | -7.502 | -63.50732 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b6f53a3-be2c-3d59-b8ff-96f824af8b26 | -6.65001 | -58.82852 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1beeb7d-4897-3bec-94d4-71bac4ac940d | -7.29595 | -60.17748 | 2025-07-27 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dab32d1-3654-3048-a519-c81a41d485e1 | -8.0746 | -63.85891 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47e21438-b398-38b3-9374-2b6833da635e | -6.66833 | -58.84118 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 584ab242-12ab-3049-888b-610318d8fecd | -6.62537 | -58.85749 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9b297347-4910-35e5-9824-ec03b6794ee8 | -6.54263 | -56.19683 | 2025-07-27 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74f5d92c-2ad5-302e-88d2-0610bf7ab7fc | -6.67374 | -58.83904 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 158438f4-3760-3546-9c96-2d45681d5e7d | -6.55403 | -56.2025 | 2025-07-27 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69937348-ae03-3e3f-9aa4-fcaf42308f90 | -6.66993 | -58.82961 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6363bc73-9343-307c-90b8-36cd8d189d21 | -6.65789 | -58.84263 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3811199b-e651-3c2f-bc30-0aec502c2563 | -6.63743 | -58.84476 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4212567-3d78-32dd-918c-3b74b36213e7 | -6.65368 | -58.83606 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29219a03-249f-325c-9687-db97795cc937 | -6.64123 | -58.85386 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f6d26532-98c0-3a06-8ae7-ee899a978737 | -7.60297 | -61.21857 | 2025-07-27 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 53f0de0a-b07f-351b-8490-58aa9a572226 | -6.65051 | -58.85914 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2053b255-3589-36f0-81ba-01c66be37e22 | -6.66371 | -58.83753 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 681f3e58-87fb-3e2e-a51b-c821edada413 | -6.66634 | -58.85558 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc95eca2-ace6-3509-9867-d1a90f7cea06 | -6.62907 | -58.83171 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8c0a4b7-09b7-3e45-9afb-faf4709660e2 | -6.63621 | -58.8532 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8b9a54fb-0aa1-32f9-8616-8595653dc4a8 | -6.6341 | -58.83233 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a77a68e-5e20-393a-9efa-4284cfb02424 | -6.62618 | -58.85186 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc915c94-68c7-3f43-89d4-a0af507c55a2 | -6.63955 | -58.83 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7237eb2-2b89-3e97-8ded-3ea7646f530f | -6.66211 | -58.84913 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 829d40b5-ad09-31cb-b39f-ce249768097e | -7.28927 | -60.1912 | 2025-07-27 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98d0c158-338c-3d4d-9716-df235eb7aa21 | -6.63913 | -58.83296 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63529ccf-b43b-31b2-bb9d-82c46ba8cfe3 | -8.6112 | -64.03988 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54a7e18c-2437-3ac7-9813-541f6dbe812e | -7.60729 | -61.21918 | 2025-07-27 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7ace3631-cb6b-3f72-9b9e-98c7e09fda40 | -6.55462 | -56.19823 | 2025-07-27 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22819ebc-2361-3ac2-9c92-fc6a4dfeb32f | -6.64707 | -58.84694 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9c06961-6e00-32b9-88ba-e8f7b1fde206 | -6.63581 | -58.85603 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| eebaf1b5-0571-31f6-8a61-cd7c5ac527b5 | -10.0426 | -59.10837 | 2025-07-27 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d773c197-bfab-365f-8f67-0be32301667a | -8.60395 | -64.04018 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1e342c4-1cd6-395c-95c8-db026faf2bb0 | -6.64749 | -58.84596 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83f82b52-02ce-3bd2-8684-a6e4c06e3bd2 | -6.64959 | -58.83143 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30cd7b9a-a138-3d41-83b5-10b4004102c1 | -6.66913 | -58.8354 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c33f9ea-1680-30bf-9e20-9814c9300376 | -6.64583 | -58.85743 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3f14bc51-8e15-33ea-9be2-f5d7c0ea2a9f | -7.90083 | -63.52377 | 2025-07-27 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e093c6f-d090-336e-9af4-dec0869ffcf4 | -6.65288 | -58.84188 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5a6528c-8cee-31c5-86a7-5bccdd43bed0 | -6.6567 | -58.85126 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 90df0da2-9620-3cd6-9760-6a3d23a271c2 | -6.64985 | -58.82657 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7793478-1891-33f0-9ca6-b8b5dedabb6d | -8.60816 | -64.035 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 80920683-ca1d-3c14-8d2c-946a01c8bf6d | -10.0363 | -59.1054 | 2025-07-27 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b5192c67-0529-3c93-a82b-f685433106f7 | -10.04106 | -59.1092 | 2025-07-27 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 74823b81-e4a9-3539-925d-ac055a1ef05b | -8.49699 | -64.02861 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6788ea4b-a32a-37d6-a96c-a481d14f7617 | -6.66046 | -58.82714 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df43d083-827d-3f33-888e-beee7b5cfebd | -6.65752 | -58.84742 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 552bc866-4028-3f52-85fb-a7d826b5d7c4 | -10.04148 | -59.10608 | 2025-07-27 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 635bdc4a-5c4e-337f-9270-1c40ad911803 | -8.66526 | -63.85069 | 2025-07-27 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92ff4abc-dd51-34d3-91a4-e86761a88a61 | -6.64416 | -58.83361 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 697ec48a-e10a-36be-b629-7a3e1700e8ea | -6.67535 | -58.82743 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dd57651-aa8e-3bf7-a922-2c64e8bb4a51 | -6.62781 | -58.84047 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4dd4ba4-d613-3a59-9212-7dd15206a52d | -6.66251 | -58.84626 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f836249e-e3ca-34f6-a302-2d0ee6b8c1cd | -6.65209 | -58.84955 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8579bca6-6343-37af-932d-9922a9820f15 | -10.043 | -59.10526 | 2025-07-27 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| efc37788-b9fd-3229-8204-768b683d8352 | -6.68378 | -58.84049 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b336f490-0ac0-3b9b-bee6-ccb48b58a888 | -6.67255 | -58.84765 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0325a5d-b5db-374c-9e61-638139c90b06 | -8.9736 | -61.51001 | 2025-07-27 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fbe1da3-8e34-3b88-aa80-e657d9989aac | -10.03742 | -59.10768 | 2025-07-27 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0372d73c-64af-3e8c-bb3e-09262f59b192 | -7.55727 | -61.41074 | 2025-07-27 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19bd05e2-b9d3-396e-b7c7-20c056b324af | -8.07394 | -63.86327 | 2025-07-27 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cc018a4-1128-3aef-af46-90e9a43db445 | -6.63702 | -58.84762 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 77537b6e-1d2f-3d8a-8f32-f67ca88afd05 | -6.64164 | -58.85103 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e136e0b2-726b-3828-9a79-5d791af17478 | -6.49635 | -56.20048 | 2025-07-27 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 955c61c1-4a17-3d3a-a499-acc90ac00fe2 | -6.65989 | -58.82811 | 2025-07-27 05:48:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6194aee5-ca42-3eac-a22a-e674563e3cd5 | -6.6575 | -58.8468 | 2025-07-27 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 3b7d2cd0-9d29-3482-9907-992d3a26a4ea | -6.639 | -58.8475 | 2025-07-27 05:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 0052aa54-44b6-3346-8b19-7c1c2737fc98 | -11.29886 | -55.11694 | 2025-07-27 05:50:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f7faeb9a-70a3-3731-8a74-f14fdf9f1d95 | -11.94042 | -63.85237 | 2025-07-27 05:50:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7ee8541-a92e-3d9c-b180-49bc302fd19a | -10.05052 | -64.98626 | 2025-07-27 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfa0ad22-0f8f-336c-827d-c1e967425a07 | -11.93655 | -63.8518 | 2025-07-27 05:50:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30a7a441-b5e4-3f18-9a40-378515d057b6 | -11.29813 | -55.1231 | 2025-07-27 05:50:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 148b48b1-6201-3299-95fb-58f727d5e4d9 | -13.45482 | -60.97745 | 2025-07-27 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67251900-eee1-3fd4-8925-1490349c821d | -10.04636 | -64.98977 | 2025-07-27 05:50:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README27.md)
