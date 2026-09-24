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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee0c1418-0e3e-344f-95df-a162aa8d1706 | -9.2424 | -47.3938 | 2026-09-24 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2be37027-edc2-3c46-b9b4-4695b7b338bd | -8.29783 | -49.90319 | 2026-09-24 04:46:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 364d967b-1c45-38ab-95b3-cf201f84e78d | -7.09208 | -52.76429 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8681c1a5-4d04-352f-a025-bd658def7e05 | -10.43675 | -46.26682 | 2026-09-24 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93fbffdf-c30b-3bc4-9b3b-08801d91c935 | -6.88931 | -59.2176 | 2026-09-24 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cf781447-e4b0-38b4-84f3-698a44fd5654 | -8.59171 | -54.62455 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 56aa2a29-abf0-3f7f-b182-c7ee97abc406 | -6.60234 | -59.92621 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cf293a29-a30f-3848-9cfc-c0c947021658 | -11.9308 | -50.73867 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5af220f-c577-316b-ae1a-61fdc2c7ea0b | -13.77468 | -52.71178 | 2026-09-24 04:46:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1cf729d6-0b2e-3f5b-b88f-2a4e72ec9b03 | -6.43534 | -59.96427 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3451448a-a3cb-34e2-b04c-49eb98865c1e | -7.89517 | -61.17281 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 206c9074-8704-309a-a796-0fa47d9bd2e5 | -6.07053 | -57.79724 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abca86e5-d3a0-3559-9663-efd3e726ad22 | -12.13889 | -45.62645 | 2026-09-24 04:46:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c93e2c0-21af-3478-9055-39a5347fdaa1 | -11.79686 | -50.06139 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1e407fc-1055-3249-8887-8384231ea27d | -11.25346 | -51.35167 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 879efcb0-9d3c-38e9-8dc4-28284931c9e3 | -12.7732 | -52.83755 | 2026-09-24 04:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8ebd7a8-692e-3cec-a29d-1c7533a9ac7e | -11.24166 | -51.35772 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd5c97e6-97ed-3047-b8df-8a6e4fdb4ae5 | -11.79616 | -50.98225 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea4b0534-83b6-3c53-9848-cd9f9a72ca3b | -12.12917 | -50.74577 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e42d05b2-d6a4-3eff-8cd0-774ff13ebb27 | -11.23293 | -51.38857 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 043972bc-cb3c-3279-8048-6913e8fe3899 | -10.44495 | -46.28395 | 2026-09-24 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a2c82705-ba39-32b7-96c1-407081639cc7 | -10.90291 | -53.95722 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94d3c905-3036-3e98-ba19-52b22d8020f8 | -10.71705 | -48.73275 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7b5d248-b426-312d-a685-f2b92a03de3f | -8.59321 | -54.61604 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3e9f68c-0f92-3e11-a36d-c5511e100af7 | -6.893 | -55.57748 | 2026-09-24 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08e8f844-8c3e-3eef-af2c-45936980eaaf | -13.08263 | -47.40467 | 2026-09-24 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08844110-7afa-3190-be93-4093cfa971aa | -8.15024 | -49.54378 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 161b0de9-25f3-3963-9f78-8f430c884a82 | -10.09303 | -46.06226 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5f42c887-7287-32fb-a76b-6851e91096b8 | -10.10615 | -50.18885 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3da599d0-f320-30ad-9bb5-7c27ebec3baa | -11.99139 | -44.9415 | 2026-09-24 04:46:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2baf428-e6c6-38c1-8b36-962d2c00bfae | -10.14592 | -50.24451 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eefcca41-e5e3-374a-87f1-c5bf67eebea7 | -6.63521 | -59.93011 | 2026-09-24 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d61a98fc-67e7-38cb-a4bb-1f59f29902f5 | -8.36222 | -45.65919 | 2026-09-24 04:46:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ed81379-8dad-3d72-827a-149681c9e7b8 | -9.87273 | -48.31639 | 2026-09-24 04:46:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 439fcb85-0072-390c-8ecc-c34a96b613f7 | -10.07829 | -46.01523 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| c020be88-7edf-3c53-992a-c55017a94500 | -9.53034 | -45.3681 | 2026-09-24 04:46:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58166f90-89d3-3644-bd02-55495b051b5b | -10.70762 | -48.72762 | 2026-09-24 04:46:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c985ce16-3a21-31f7-bb87-f439a8b469d6 | -10.14611 | -50.22188 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53fe2a59-8002-3ea9-8d7d-4dfaa3eca107 | -8.52716 | -47.39181 | 2026-09-24 04:46:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1484ec29-4c7f-37a5-932b-11ae83e04935 | -8.60057 | -54.59993 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 925275cc-c54a-3951-8b9c-aba4dfe623f7 | -9.26424 | -46.25787 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3e0b342a-135c-3ef9-b8d8-c55a6ec502b7 | -5.59431 | -60.19403 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 238b3c91-73aa-33d1-b976-36afc177c6f8 | -8.92245 | -45.95284 | 2026-09-24 04:46:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51e261df-1d3b-3695-b4b7-5ee264917f66 | -10.08302 | -46.0566 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ee3022c9-6573-3964-8a7b-af678badcf15 | -11.6787 | -50.18563 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8239d689-e24f-365e-87fc-908a71779b02 | -6.08317 | -57.6249 | 2026-09-24 04:46:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd3e3276-1c86-315c-86ff-223e42b937e8 | -12.113 | -50.82328 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ce8e04b-7545-3c7d-9b1a-5a18f92f00f9 | -13.78668 | -54.05065 | 2026-09-24 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a68f9cf-a445-3ec0-b084-ae849fb1c886 | -11.2222 | -51.3665 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e08d828-42ff-3081-9786-17ac627af19d | -9.58239 | -46.51576 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 669de243-98df-34f6-a8e1-487f30768899 | -12.13877 | -50.75122 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 34e652ed-d0ee-367a-9b32-6418287850c3 | -10.41567 | -49.3514 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 1bab4e9a-b708-3141-8f8c-d5e3e0a0a4e7 | -9.47478 | -40.33391 | 2026-09-24 04:46:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 67c9622f-f620-3bd8-9f3d-82a2c29b4d9c | -11.12912 | -48.30749 | 2026-09-24 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62eb2251-eb80-3d15-849f-f10c2e05c1f2 | -6.7382 | -59.43016 | 2026-09-24 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ac584f7-2d1c-32fd-877c-c3aa3f8f4cda | -10.09815 | -50.19506 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb14b9df-e09b-376e-9904-2995a4f6ab74 | -10.88401 | -45.07806 | 2026-09-24 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d156167e-adbe-3a4c-8884-dd28b03cfac3 | -12.16801 | -47.36714 | 2026-09-24 04:46:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 273d7f3f-2ad8-3e67-b1a6-2fda28430519 | -13.70479 | -43.66537 | 2026-09-24 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8dca9f89-cad1-37d2-b75a-b98ecd58a8f1 | -10.90727 | -53.9323 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bca7c851-a303-3570-b62c-9530cc3116d4 | -5.85867 | -60.16155 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3ac1cb0-166f-3567-9b11-7c3717bbf14c | -12.33795 | -50.147 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6eda87e0-67af-31f9-922c-7b19e4db5ed7 | -14.69931 | -48.75074 | 2026-09-24 04:46:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51675dad-d8ea-323a-a55e-24b1f659edc8 | -11.23424 | -51.3807 | 2026-09-24 04:46:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c809fe1f-9181-3117-9284-e8a576527580 | -12.14701 | -50.72214 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4835c4e8-f069-320d-b5a4-99c24a3438ce | -11.46788 | -47.3872 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 56ac0ef6-ee72-39fd-b4ce-282f21e53438 | -6.67336 | -58.58242 | 2026-09-24 04:46:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 998a39d2-e547-3458-8a93-c91fcc3322ca | -10.97816 | -54.09694 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 015f05e8-4812-3c3d-8ff1-9faaa10fe84f | -8.92099 | -43.87252 | 2026-09-24 04:46:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec19edc4-7b08-3f38-949f-f62940e520d1 | -11.35324 | -50.23289 | 2026-09-24 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35d760d7-bd43-3aa1-9c2c-1534307a2d2f | -9.98659 | -50.23751 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b273eda6-07fa-390a-9873-15e7c692afba | -10.61813 | -53.99103 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 058d82f9-6ebc-3fef-a706-705354cce065 | -8.12542 | -54.81739 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6acb0191-9a72-3f3f-a522-fca8f457169a | -11.45539 | -47.40038 | 2026-09-24 04:46:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a35ef1f-4b53-37cd-b5b0-69af7322f3e2 | -11.63648 | -50.61825 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ad9719f-02f3-320c-a271-3e46911dfb32 | -9.98999 | -50.23808 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81fea351-fc6a-34fc-ab31-6f0cb6d01059 | -12.15002 | -50.74482 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 131d851c-2a33-3e69-99fe-df5cbfcf1592 | -11.79409 | -50.05724 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9bf79f4a-eee8-3152-a3c4-f5a14fc15a5f | -12.13998 | -50.7438 | 2026-09-24 04:46:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8144551b-3870-3320-b415-5a309c17c04c | -6.43719 | -59.95396 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b196a87e-0c6d-3193-961a-e3f470923c6c | -11.10965 | -48.30067 | 2026-09-24 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1080db4e-d8ab-319a-83e7-f14f140e5cc0 | -8.30007 | -50.85157 | 2026-09-24 04:46:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b76a257-52aa-3bdb-ba0e-b139021a29f6 | -10.11793 | -50.20211 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c9674ffb-1ea8-340c-8ecf-32f99357146c | -6.73613 | -59.42833 | 2026-09-24 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8595e240-f008-35b2-b8e4-4e8dc279f240 | -9.51954 | -46.54579 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa0f38a7-2c6f-3d69-ab25-5b4affe39743 | -9.96595 | -50.25675 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afa2f468-8cab-3295-b901-72c9ec1d1b58 | -10.90603 | -53.93938 | 2026-09-24 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec63f58a-6f36-3317-8264-35f9dc40b62d | -5.90867 | -59.9301 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29f3d51c-e333-341e-b585-93a02a3990aa | -9.57893 | -46.51525 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b761fc21-f2b3-3bec-9129-586d370bac82 | -12.41259 | -46.9539 | 2026-09-24 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50946d21-7f8d-3417-b117-0a171afdddd6 | -8.92027 | -43.87751 | 2026-09-24 04:46:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc84d9fc-455d-3157-b4ab-d5f73e2d1a2b | -9.03659 | -44.94157 | 2026-09-24 04:46:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fcd571c-07c6-3651-ad8d-e44f33796201 | -10.23806 | -49.98222 | 2026-09-24 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c906c02-1c7a-30ed-871f-38b554b2fc1e | -6.45631 | -55.00661 | 2026-09-24 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e893a495-81c4-39f5-a737-e02ed54d6eed | -9.22603 | -47.34353 | 2026-09-24 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00f15345-326e-32ec-880d-718da942126a | -9.14941 | -49.97333 | 2026-09-24 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f427c8ef-776e-3460-bec5-d9079f3257ae | -12.04006 | -50.28629 | 2026-09-24 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d6add23-393c-3d40-bcf3-25f67079d9a3 | -5.91611 | -59.9259 | 2026-09-24 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 483109db-2f5b-3ee8-8be8-8b3d4222d55c | -10.08305 | -46.00758 | 2026-09-24 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b4744b10-4a50-37c1-a7bb-3761614d4e72 | -10.8967 | -51.52158 | 2026-09-24 04:46:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README55.md)
