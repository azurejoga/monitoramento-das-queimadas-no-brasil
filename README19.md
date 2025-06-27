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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0720c457-c044-38eb-bbbf-b9218af97bdf | -11.08357 | -45.28643 | 2025-06-27 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 887f9f40-8bc5-3535-96c1-ad8ff6a7104b | -11.07253 | -55.07449 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e81fd122-e247-3ae4-bd25-8b414e0c3d08 | -11.58003 | -52.11314 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| cfb40d3e-c04c-3581-89d6-94b8803b4cc7 | -10.30183 | -57.13757 | 2025-06-27 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 668ca7e4-6cdb-3798-a0e5-315d0041c394 | -13.15883 | -45.23132 | 2025-06-27 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93167a4e-8879-37a5-b6d9-bbd0bf0a5c6a | -8.61638 | -51.57721 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d545b6d8-c1e2-3bba-8a51-08567d78e501 | -11.17345 | -55.92354 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5962442d-bd24-3329-b3c0-2835df203d40 | -11.95212 | -47.02479 | 2025-06-27 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 056898dc-a571-3d4d-ac82-a0c7bb62ebf4 | -9.36993 | -47.63164 | 2025-06-27 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93f1d37a-f0cb-3960-8383-12aab1ae2e0b | -11.4358 | -54.47654 | 2025-06-27 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 081b6d2b-b42a-34d6-85f8-43054f231c0f | -11.36476 | -48.71367 | 2025-06-27 04:49:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c181543-662f-3ba5-99ff-ea151288069e | -12.02747 | -47.77572 | 2025-06-27 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 41874389-a564-30aa-9ed8-80022f54b9fa | -8.54561 | -55.03894 | 2025-06-27 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f910fa7c-8ccb-3b60-b619-cc376cc3af1f | -9.24344 | -48.75159 | 2025-06-27 04:49:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f36650d-e98b-3047-8330-82f85c24cd77 | -11.0627 | -55.37797 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3c3bca07-4901-3c9e-a464-1e8232eed784 | -10.71526 | -59.12572 | 2025-06-27 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7dc58152-6855-3bc1-9413-ed9f3c10517d | -10.6533 | -44.49137 | 2025-06-27 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 674ce22e-919a-31d2-98c1-4408f4ddeb16 | -11.05616 | -55.3725 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 683cffc7-9c7f-305c-9fcd-eaa6845ba999 | -11.99652 | -47.15481 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71a30c7e-fc06-3a0a-91bf-37a548d69b3b | -8.6186 | -51.58471 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1be72cdf-2cc3-38f0-9897-d7d864d14a05 | -11.1106 | -44.52173 | 2025-06-27 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abcae8bd-cea6-37f1-a630-de7a0301a7f9 | -11.77659 | -55.02792 | 2025-06-27 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46f34a61-29db-3f64-816d-6bbec0b3f5cf | -10.30307 | -57.13034 | 2025-06-27 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6333bab4-caa1-34ed-bb99-1354ecf4b400 | -8.33508 | -55.09294 | 2025-06-27 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94414000-d655-3d87-a1e8-b36b5af0e857 | -11.35777 | -44.89602 | 2025-06-27 04:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b1065b8-cf69-38a8-9097-dce3b551e7c8 | -11.6703 | -46.73437 | 2025-06-27 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3c08db3-bbd6-3b48-a76d-7f871056f480 | -11.80522 | -57.35192 | 2025-06-27 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7240322f-1c68-3322-9dca-7b417be5cdd2 | -10.37287 | -48.30511 | 2025-06-27 04:49:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d68501a9-8487-3c7b-9040-105fe20b18bf | -11.99956 | -47.16265 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d26f37a0-9ae7-323a-860b-c2491aa72e48 | -11.58692 | -44.66798 | 2025-06-27 04:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 780bdba3-54ba-3318-88e1-acc6c0628f4c | -10.80947 | -57.75555 | 2025-06-27 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32907fe2-e49a-3451-b232-ea9bec4cbbdb | -11.99984 | -47.15823 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fe0bfbd-5ae4-3814-aa42-1761f4c19f4a | -11.57504 | -52.12316 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 82101d7f-dd31-3596-8f1e-c9cd8a64d221 | -10.83253 | -53.75186 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb69830a-a58c-30f6-b4f8-f0ecce162aaf | -14.28926 | -41.60007 | 2025-06-27 04:49:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| edea967e-9581-39fd-8c21-34895b6e2668 | -10.87944 | -47.58376 | 2025-06-27 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68b6ece0-e7db-3774-92fc-0983632713ed | -12.00967 | -49.52125 | 2025-06-27 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e791da30-89de-3101-8bb8-6db236ed3b57 | -13.06011 | -51.64296 | 2025-06-27 04:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6796fce-605b-343b-a8fa-b470a9e6fd88 | -11.83939 | -57.86033 | 2025-06-27 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 681ab0cf-425b-35ee-b078-5a1bd2f31b1a | -10.87501 | -53.77048 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7754e77f-9d41-3084-82e6-b9a98f90b594 | -10.29557 | -57.12527 | 2025-06-27 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c49e0aec-0026-3fbd-a098-2fbc83ded569 | -13.04496 | -48.81999 | 2025-06-27 04:49:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 799f50b8-cf71-3bd6-b5f6-ef7516c01c20 | -8.61306 | -51.57668 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b5842448-c368-3763-838e-ac1da0bc7d50 | -10.03004 | -54.32536 | 2025-06-27 04:49:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 082a4f8b-6336-3f0b-9e38-b1195bc7200c | -8.35312 | -49.23264 | 2025-06-27 04:49:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 518a8ae0-7349-385a-bf3d-c4066d7f45ef | -8.43988 | -46.97398 | 2025-06-27 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f92594e7-cabc-33ef-8358-6b5d554029ee | -8.68758 | -48.31238 | 2025-06-27 04:49:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa265974-153d-3940-8b1f-dad369b7aa40 | -12.00341 | -47.16248 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87029ac3-b945-335b-9c47-4195582eadb5 | -12.05177 | -48.07764 | 2025-06-27 04:49:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48dc38bd-5f78-33da-b48a-ad6c2733d727 | -12.13323 | -54.66679 | 2025-06-27 04:49:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d76a3ce3-4f1c-3869-bb11-52358eec3ab2 | -10.64835 | -44.49191 | 2025-06-27 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 720c4332-e88a-389d-912c-465dcf83aae6 | -9.23426 | -50.0323 | 2025-06-27 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d4f7c2d-5ae8-3680-b394-29a6abd8c2d4 | -11.57006 | -52.11152 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 158f1845-1719-3d75-89be-0dee69bfac9d | -11.80754 | -47.52804 | 2025-06-27 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccc4c9e4-92e8-3c42-97ac-abad758586e3 | -9.11753 | -49.44608 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb2c0b1b-5db2-30f7-9803-06fa8c2a8327 | -14.23484 | -45.50197 | 2025-06-27 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e7bae1e-c972-3387-b675-d4237abf4aaa | -11.1854 | -55.92095 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67014c41-963c-306f-af54-86723f421e00 | -10.85733 | -54.04455 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e02883b5-eca0-303f-9c1b-7cf20e2e9d79 | -11.60637 | -47.7641 | 2025-06-27 04:49:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d22aea3-4d69-31eb-832f-c9a83f342368 | -10.871 | -53.77362 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a993b759-65b3-3671-872b-e9d936e31e41 | -12.80752 | -48.73375 | 2025-06-27 04:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d14abd9-b0fd-3beb-9d51-d7ce386f4416 | -10.8722 | -53.76618 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e0658eb-1e51-3f84-8298-eab279948584 | -10.8716 | -53.7699 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 229a4a85-4334-38e1-813c-08871a4638cf | -9.08878 | -47.97114 | 2025-06-27 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba121c69-8c34-3611-ade2-9a183890bdf9 | -12.03121 | -47.77287 | 2025-06-27 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 37670f81-b99b-32a5-9019-3d4315d28b5d | -11.0656 | -55.38285 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a4f96dbb-ffff-311d-a725-dd962c1e5718 | -9.11232 | -49.43345 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 74aa1a4f-2864-3a35-9a6a-5e4f9bb15efb | -13.05379 | -48.81969 | 2025-06-27 04:49:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f5ee8f8-9ff1-39f4-bcaf-bde0af7b739b | -10.54572 | -46.35864 | 2025-06-27 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ceafe999-d9d5-3415-a7ad-27bd54acb63a | -11.1412 | -53.93644 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 604263a9-f60a-33ee-8bf9-e2a458235453 | -12.0006 | -47.1554 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 888bc4d1-0367-354f-b26e-2c2bcb84f098 | -8.62799 | -47.45098 | 2025-06-27 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7118dd9f-d7dc-3e23-ad3e-790a71c3a2db | -11.05613 | -55.37369 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9c9b47a4-0ae6-3265-bbcb-f8784eb41a3f | -9.06901 | -49.42703 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 532e0a13-eab9-3e1e-a1f5-120e54348d84 | -9.37374 | -47.63223 | 2025-06-27 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7dd3d114-8efb-326e-97f0-1fb8294a48ac | -13.06346 | -51.6435 | 2025-06-27 04:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 94e88570-501c-3c06-ba97-085883131eca | -11.06963 | -55.06977 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60a0af8c-96ce-3482-8544-0c456fc644bc | -10.08421 | -48.29958 | 2025-06-27 04:49:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ce6e8b5-5b80-3931-af4a-e2d69199f08c | -9.11869 | -49.4384 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73dffb7a-8d52-3263-9215-d7765aa4877b | -11.18556 | -55.92316 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82c99a6c-a193-31fb-beba-d5814a3d95ce | -10.1525 | -53.91428 | 2025-06-27 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d596adf8-1e43-3afd-a606-c8dcc96a6d5f | -11.50386 | -61.82409 | 2025-06-27 04:49:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3514fc0e-c453-3aab-9c5c-4a165583a59a | -9.07537 | -49.43194 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 015ae2b3-af7f-3593-900a-d4b08267345e | -11.06923 | -55.3835 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5aa5019a-d662-3fe3-84e7-313142474e6c | -10.30025 | -57.12239 | 2025-06-27 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed3ad15e-6873-320d-a5dd-6ca32e7a9875 | -10.82572 | -53.7507 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5cfdc97-db5c-3949-bb1f-ac2598ae94c1 | -11.84333 | -43.79816 | 2025-06-27 04:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36dc6a3a-b155-3c6b-a11a-7616989415cd | -7.14058 | -55.37381 | 2025-06-27 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 073dc729-4ada-3fa6-96ed-f8c9a17a1789 | -9.48053 | -56.0762 | 2025-06-27 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f3d5298-48c1-3fd1-8d22-b48c41b536b5 | -10.82754 | -53.7396 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4d24467-7b51-3e5b-b5ae-59de78d59ce7 | -10.87039 | -53.77734 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1995a64-ae2e-309b-bfd3-2de4295fe26c | -7.63272 | -49.5381 | 2025-06-27 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 160df424-9e75-326d-9c8c-1a9c1cd18b32 | -9.75317 | -48.04167 | 2025-06-27 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd1be683-626b-3ac5-a407-67b35df8648e | -10.82293 | -53.74642 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a1772a0-1669-3a3d-b428-d611057ffa7c | -11.134 | -53.91603 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bf44a44-dc7a-3447-9639-5d1a7b18817f | -10.82931 | -54.05166 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01f4ebce-be26-3562-b53e-caae617d3a70 | -10.83275 | -54.05226 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 999d84f2-1c7d-38df-a2b9-29db773fc171 | -14.28918 | -41.60143 | 2025-06-27 04:49:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ccc3821f-d830-3290-94e3-dc8d5c833492 | -12.81228 | -48.56564 | 2025-06-27 04:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a802d2f-7456-3a42-8088-37956965a642 | -9.07715 | -49.42038 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README20.md)
