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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4c7bcf7-b60c-3c83-b226-43b8aff30dd7 | -4.53235 | -54.9583 | 2026-09-12 05:10:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9806d09-1b45-3fa1-8cf1-93722d0210b6 | -10.55026 | -45.22218 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f032dd32-b389-39be-be0c-f5e2262c698e | -2.72211 | -57.61792 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d5e3dad-8d14-33d0-9b90-4f2bb80fa69b | -8.80447 | -46.93644 | 2026-09-12 05:10:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6fd6fee-05af-3898-b0b9-03eed17e494e | -10.6857 | -54.16287 | 2026-09-12 05:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| e5e9871a-2c39-3fc0-9c0e-9fff6e162af7 | -6.17839 | -57.71409 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d862c638-61af-3b3d-a95d-e0adb36d5c5b | -6.8485 | -55.80413 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2bd9f3d-62f4-344a-95a7-ac1a1bdb4308 | -5.85013 | -51.99988 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e94e0a7-2f1f-3512-b67a-bb95acb3df34 | -5.47837 | -45.12605 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b18caba5-3dd3-3d17-968f-b5a385a1b265 | -6.09773 | -55.64741 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7cfeb6a3-4aba-3687-879d-11bf20655e35 | -4.36353 | -47.78407 | 2026-09-12 05:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f8a70b82-c2ec-3302-a083-f037dcc64b68 | -6.10875 | -57.6315 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 52167fba-8a5d-36ca-9b3c-a2fe71b05b81 | -7.17965 | -45.89093 | 2026-09-12 05:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e0ea92b-7557-3845-ab13-4b51bac86790 | -5.81541 | -53.80789 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3ac4353-906b-33a1-8690-375f5efa4f18 | -9.46838 | -50.31407 | 2026-09-12 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0eab1bb4-562d-38a4-b1c3-459327948d4a | -6.61249 | -58.84631 | 2026-09-12 05:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 38a4b7cd-be83-3435-affd-5106f340817a | -3.86198 | -49.22015 | 2026-09-12 05:10:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7d125905-499c-32fd-ba06-e6389e5e361d | -8.38216 | -47.54962 | 2026-09-12 05:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a87c913b-ad7a-33d1-9177-107abe0e759f | -6.62144 | -51.14097 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a15fef6-cc49-3cea-a4c3-42885546609d | -10.48141 | -51.36361 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22ee1d2d-969e-39d0-8953-94c494ce5cce | -2.67081 | -57.51099 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d47ae067-bd6f-3476-a1ad-4dfa1890a72b | -5.37295 | -56.02875 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b25e1981-bd58-38c5-a8bd-f1dedf8d8512 | -7.17371 | -45.93391 | 2026-09-12 05:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1eb47c4-5ab5-31d5-b474-b45ca9a2e0a9 | -5.97907 | -57.75953 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fee3c0f-22ed-3d24-ab6c-8b6af4ddca28 | -10.51692 | -47.90013 | 2026-09-12 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 949a3839-da9c-3ac5-b6e9-7065253a81c1 | -6.34164 | -55.30436 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 066af7e7-e14c-3041-afe3-49eb99c642fc | -6.23246 | -51.68878 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1772d4f4-d0a0-3e60-8b8c-d2e2d6287621 | -6.28876 | -56.02335 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4abebb9a-0120-3b85-bb6a-d2af7409b7eb | -11.37804 | -46.84549 | 2026-09-12 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 743387fd-7d84-326e-bad4-5e83e81a0223 | -6.08091 | -57.88779 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 212eae40-e23d-35af-bab3-c54f5c3ef6e9 | -10.56361 | -51.35286 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74d68230-d0b8-3fe2-945a-115199818569 | -6.92553 | -55.65008 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19b62bff-7da4-358f-b06d-e066e8b72997 | -9.36789 | -48.41424 | 2026-09-12 05:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91883bff-2c87-3900-9273-2309e2eafdd3 | -6.11079 | -55.63099 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 765b7e67-8841-3597-8d45-1d4659b22ace | -5.97199 | -57.76925 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 661a2c6f-2a4d-34df-aae4-4fba9b7daabe | -10.55746 | -51.34259 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79e47682-2684-30b6-8bb3-ea430547171e | -9.37247 | -55.96717 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8f46091-d36a-3595-be2a-bc0f087bfd11 | -6.33336 | -55.85688 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc875d8d-b38a-3ae6-ba40-ed85f84f2404 | -6.1182 | -55.65411 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9420898-0d1a-3e3b-b646-21aa4e0d5003 | -9.57635 | -55.15663 | 2026-09-12 05:10:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73d24a34-c2ed-320e-8b75-7d59cc394a5c | -10.55701 | -51.34464 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cc3c2f6-5ea6-3d8a-8a1e-7064576c92ad | -6.23891 | -51.69375 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a6b6fa9-c728-3121-ba51-91a490c7183d | -7.1853 | -45.92578 | 2026-09-12 05:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17f5946f-1155-3294-a366-5cbba562c7bb | -6.96162 | -44.54107 | 2026-09-12 05:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5e47b7d0-bf1e-30e4-9a00-2477ba50d48b | -6.88109 | -55.64654 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 659c394a-c8b2-3265-91f6-9d652d2bbc0e | -5.88979 | -52.06397 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 538f17e6-6511-32b9-828b-27b1e4b1301b | -8.11024 | -48.76234 | 2026-09-12 05:10:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28c12020-21d2-33b1-bf29-557acf4f6224 | -6.10112 | -55.64795 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79cecde0-1173-385a-af4b-ec2488813f98 | -8.38799 | -46.30191 | 2026-09-12 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98ec5e07-0390-34f0-ba1b-8ee13e05315d | -6.19772 | -55.26992 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 157441ab-c06c-3619-a917-d84db6ee490a | -11.41049 | -43.94226 | 2026-09-12 05:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a237ecae-46b7-3794-96bc-bd05ecb463d1 | -5.29379 | -55.95899 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f11abd32-138b-3178-bc3b-bc3edead41cc | -10.39433 | -51.48161 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69c32e6e-6a0d-3a49-b497-06a82b07d591 | -7.96616 | -43.99461 | 2026-09-12 05:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5cff8210-5c20-367e-b621-29fa26aafd98 | -7.95919 | -44.00195 | 2026-09-12 05:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca53653f-be75-3527-93ab-b69e8d79dc76 | -6.18733 | -57.72904 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 077af687-8230-3afb-99b2-92421841e5ed | -5.84955 | -52.00364 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2766ab3-38b2-347f-97dd-0cddfaef913a | -6.20108 | -55.27046 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 958ab7a6-70f2-35e8-9ff5-3e7ed59c58ed | -7.11464 | -55.12731 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65270c5b-9361-3fbb-9c8b-406dab7abe40 | -4.36172 | -54.7788 | 2026-09-12 05:10:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 24b0de13-2ded-3321-b3ad-421b3ba6ffb9 | -10.67757 | -49.0765 | 2026-09-12 05:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 770a8206-f858-3756-981a-ae080415e303 | -6.23359 | -51.70498 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c7928dd-e8fb-3e06-971e-b5c6af3f0353 | -6.77205 | -59.43111 | 2026-09-12 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35e4c6c8-e8db-3da3-ab42-2a2111b991f2 | -7.9611 | -44.00679 | 2026-09-12 05:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03028982-b7a6-3019-a226-04678f101e84 | -6.06348 | -57.73297 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a03927ec-0092-3a6f-9971-4eef7bed33ed | -5.60839 | -44.84709 | 2026-09-12 05:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b1f5e67f-d060-39c5-8eec-22493c91e6f2 | -6.14064 | -57.68996 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a05a7f3-5127-39cb-ade1-ca825635dcf4 | -7.30903 | -45.98882 | 2026-09-12 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 219141c0-846f-3577-95f3-f4d849335701 | -8.32107 | -54.77279 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69a11936-cfba-3294-bde9-898b54e848c7 | -9.37088 | -48.41232 | 2026-09-12 05:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dab3cd46-fb14-3ccf-a81b-76b7f551312c | -7.27117 | -46.80571 | 2026-09-12 05:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fa6a33aa-feff-3081-8b4a-5b71cc0b47bc | -6.50231 | -47.59845 | 2026-09-12 05:10:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| be84d2af-5e1a-3005-9359-0bbbf9acbeb5 | -4.86666 | -55.99904 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fff56a73-adfd-32d2-a097-62a9969e4261 | -9.0006 | -50.85925 | 2026-09-12 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf0e12c3-5f8a-3bbe-87ec-0f267b69a9a2 | -5.76178 | -45.09118 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| a7ebb21c-bb30-33c1-b281-d244bc8ffa0e | -8.3194 | -54.76179 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2873d77e-0935-3f68-9418-84ab47040624 | -5.97761 | -57.7682 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5cbd8331-4636-33fc-bfc7-0a6561ee0ba9 | -6.13031 | -57.68369 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74926e07-bf38-3ef2-a6e4-7e6d4126e29f | -5.77043 | -45.09565 | 2026-09-12 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 9f664905-395d-33aa-a041-7afb52215fac | -9.32465 | -45.63938 | 2026-09-12 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8dfbefb2-0f44-3a13-85cf-8876b41226c9 | -8.11558 | -54.78963 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8bf31a6-cd55-3354-af6b-9f9da833b56e | -10.55677 | -51.34718 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42baf1e6-9f53-327c-abed-a4c761af2280 | -5.98013 | -57.76608 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6733c58-eac9-3a50-a2f4-eec9cd7f3eab | -5.79936 | -53.82315 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34aa93ed-6eac-3890-b810-2e07dda13a5c | -6.10789 | -55.6491 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 987bc129-fd0c-3163-933d-f163390ea86c | -9.54404 | -45.47346 | 2026-09-12 05:10:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a982ac0f-17ac-3bde-9821-a4014faa2448 | -4.39981 | -50.95843 | 2026-09-12 05:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44f6af1a-c259-32e4-b515-1bd4f988cc6e | -5.82648 | -53.80252 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b819a3bb-93e2-3448-bb0b-fd8c95e71d6d | -9.36853 | -48.40981 | 2026-09-12 05:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1509356d-8f78-3d07-936e-c3857d499317 | -6.19104 | -57.72962 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8770f107-dea4-352c-8bd4-7abee1653cd5 | -6.32582 | -43.35822 | 2026-09-12 05:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb14ff21-277c-37ad-b62b-d0c34fb19c0e | -4.86891 | -56.00704 | 2026-09-12 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 019216df-6e8e-3419-9486-17bde59c21d5 | -7.17922 | -45.894 | 2026-09-12 05:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e896686-8f8e-3c11-b797-b0afbcc50cee | -8.81908 | -46.91283 | 2026-09-12 05:10:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b2abbdd-1342-360a-8b5f-8d4a6d977cab | -9.80504 | -48.92326 | 2026-09-12 05:10:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42b2a345-aa2d-3e03-8e4c-bc8e6a60b5d9 | -10.48957 | -51.36018 | 2026-09-12 05:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 818ec142-4acc-3a2b-9384-5e4f7e15cef9 | -2.7337 | -57.64415 | 2026-09-12 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| affc6409-7965-317b-ad45-968a09df4353 | -10.34093 | -48.09099 | 2026-09-12 05:10:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 864327db-62d7-377a-accb-64ffea2e87f6 | -6.20557 | -55.26393 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f26f3bfc-96a1-30bd-96a2-f975c7b2a490 | -9.63799 | -49.67862 | 2026-09-12 05:10:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README37.md)
