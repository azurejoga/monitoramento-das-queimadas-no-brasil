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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df25b277-a160-3012-aa90-ecf123a431d2 | -7.8645 | -54.70315 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35f22765-8a35-31c0-bf35-ce788174117b | -12.55611 | -47.16033 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ebf9c45-c6b2-381e-be0c-079a56433292 | -7.50175 | -44.55411 | 2026-09-29 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbbe46f4-fca2-32ce-b88a-3073d8c3e88e | -12.31492 | -46.4069 | 2026-09-29 04:51:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a6c040d-76a7-3862-a690-00a4c9a8a29a | -11.30007 | -58.3397 | 2026-09-29 04:51:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 476dd239-3425-3173-965a-dc9c46ae64c1 | -10.23586 | -46.53374 | 2026-09-29 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 023d511d-3566-328b-95a3-3ea6f8d3bfcd | -12.00499 | -50.94162 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 08b58780-c5a3-3672-8192-0c11444da2aa | -11.34487 | -54.041 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcf4507d-c08f-3c72-ab6a-8f4eabd9628c | -11.12467 | -50.0715 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f96e97b-4f11-3b24-9a6c-5b5e0edc15cc | -12.71933 | -46.99136 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b780feed-084d-3e7f-bc6c-7bc72bdbc7f1 | -11.18311 | -45.14188 | 2026-09-29 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 446d90ea-5ea5-35d3-bf48-6ebba8d31062 | -8.85823 | -49.88131 | 2026-09-29 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5c6fb786-d61a-342b-9488-fa74cb1714ae | -11.39009 | -43.45209 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6987bba-00c8-3017-bd75-974253768a5b | -10.27451 | -44.63514 | 2026-09-29 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19205194-cc1b-3bbc-8172-11febb896e2a | -10.26267 | -44.6309 | 2026-09-29 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6f2737d2-b91e-35c0-b271-363e1880a9aa | -12.9025 | -52.05145 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbf10d05-5952-3d25-b499-46452a9048ac | -10.81642 | -48.73176 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4a1cb9ff-69c3-377b-aaa1-4a820e66bbae | -11.33877 | -54.12164 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8156753-bed4-34f5-a655-fe198e0af57d | -11.50557 | -47.40591 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1881c42-fdc9-32da-a78a-1fa791a12286 | -10.81182 | -48.7389 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cc57b3c-5378-30d7-8f7b-c424b019e329 | -12.91024 | -52.06773 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63f79b31-e778-363e-9223-ecd7de49d8b5 | -7.46329 | -45.81482 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc1d89cb-281f-3b6c-b6ac-5949b364cac0 | -9.99433 | -50.26817 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d7307ac8-4c3d-39a2-ba84-ff40b42c853e | -11.07147 | -48.88728 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab46e981-575d-3775-bb7a-cbaedd0ec781 | -10.01098 | -50.24929 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9531b0c-feda-3012-992d-fa114a24c19b | -11.99223 | -50.93589 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1ddfeebc-c5c5-3557-ba59-1ab17487357f | -7.51243 | -47.33704 | 2026-09-29 04:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b445b6c-a647-3e1c-b1ce-5b59fb6cdaeb | -14.08407 | -46.31543 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9cf20c0b-4e5c-3873-a3f6-4c15c7b0f5a3 | -12.91146 | -52.06757 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 197c34ff-17ce-38fb-815c-cab817cc467d | -8.68419 | -38.19171 | 2026-09-29 04:51:00 | NPP-375D | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c10fd691-6f2f-37f3-af32-67c176c5a320 | -6.17893 | -53.28564 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba77128d-3836-378a-9170-25ac9b7d0c1b | -10.43101 | -49.37918 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d38ccf09-1774-3236-b6f2-73b21d471403 | -12.70306 | -46.9725 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| daef9478-49dd-394a-a04e-7097601809d5 | -6.99562 | -45.33882 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b08baa63-aee2-336b-8be2-58a42d6adf5d | -13.86361 | -43.99845 | 2026-09-29 04:51:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1fc11c8c-8b15-30cc-9c4c-011fe9736b90 | -12.9364 | -46.65923 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51ba8e35-b729-3634-aaf7-548844335518 | -11.82504 | -46.90026 | 2026-09-29 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fe1590f-3dc3-3367-a342-782b5136b9da | -8.72397 | -44.91062 | 2026-09-29 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7254cf76-6047-3b6a-aebd-4de15b857dda | -11.92848 | -50.88549 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb5878fc-24bd-3132-82bd-0f66e456643d | -10.59402 | -46.21178 | 2026-09-29 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f016043-702b-3359-b473-d8fc5865323a | -8.23796 | -45.43747 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b93d2ed6-93d9-3f34-b2d5-0beccd5f0acc | -12.73367 | -47.2648 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8050a891-772e-33e8-b7e6-56eaaad9d630 | -12.39283 | -50.2198 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cab86d66-fa24-36bb-8617-ae1b5cacb77a | -12.02749 | -50.9452 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03760936-cf6d-3353-bfdd-3d80d7234939 | -8.23043 | -45.40731 | 2026-09-29 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b29b91e8-1ceb-3d72-a192-869e42b98e3d | -13.46777 | -48.58158 | 2026-09-29 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c6f02641-effd-3d3a-8fa6-3b3548752d5c | -13.111 | -47.39989 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8d9bda23-3441-347d-956c-01355c153b48 | -10.70456 | -44.42295 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf8be9dd-023f-3f2e-be43-e74898af1913 | -12.74281 | -47.28004 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b8a7ff2e-c674-3b5a-8180-c7620063f40f | -10.81181 | -48.71618 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 782a1711-d22d-34de-a9a8-d61f9f98a367 | -12.27922 | -50.27458 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7f17460-a83e-38f7-bd28-c1fbde505111 | -12.05998 | -46.4937 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 68678474-fa03-3dcd-8abf-2866b9a9cb96 | -12.75636 | -47.29097 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e4f4f96-6a02-32e6-8e54-e66a5fe4b527 | -7.38498 | -47.01545 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cc3efac-100c-3a77-bafb-99540690f395 | -13.08364 | -47.39482 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 68dd42d8-f0ce-3c9c-b360-cbbad03ffe6f | -11.41687 | -43.45243 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0fc22195-1387-3124-94ac-3aa54cb85519 | -11.42487 | -43.46345 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 5adea721-544d-38e9-b27c-aeffa04b52ff | -10.71005 | -47.82555 | 2026-09-29 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fca056f-625a-3913-9b5e-9879eeeaa6d5 | -13.38747 | -51.32539 | 2026-09-29 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d208051e-a137-3ba7-b9b9-c4725d01cbfe | -11.71523 | -43.45823 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33844027-f728-3e08-b60a-41a7ef41575c | -10.78228 | -48.74915 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 01224ed0-c36d-375a-81b6-8a779972b6a7 | -10.93134 | -47.59344 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5760d924-0e62-3842-86f4-84e6a410b45e | -11.38837 | -43.45344 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35499991-c998-3016-800b-4ea957c05071 | -12.90822 | -52.03749 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 11020927-6bbc-351b-b0b8-a6b54c7c178f | -11.40094 | -45.41761 | 2026-09-29 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47ca13f5-5780-394a-b401-541018f5d9bb | -11.8711 | -47.08742 | 2026-09-29 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15600090-664a-39e4-9a2c-f07b79d7b61e | -6.6921 | -45.64077 | 2026-09-29 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0762f866-d886-3adf-a549-5dd83ad5e810 | -12.00574 | -44.93112 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe1358e6-1bc1-33f7-8d4a-a6bd85d7f0a7 | -7.99574 | -43.25575 | 2026-09-29 04:51:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f8e0bb63-6561-39b1-80ba-9eb767868a25 | -7.6918 | -48.86631 | 2026-09-29 04:51:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aef0ce8b-1fcb-31de-af1d-e7434e629995 | -10.26608 | -44.63393 | 2026-09-29 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e036cca-9ecb-3a43-808d-12c3f5c2e449 | -10.5947 | -46.207 | 2026-09-29 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 33805b76-a5ae-3f8a-9b4d-d6bc83ea0d58 | -9.13155 | -49.975 | 2026-09-29 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09d94e26-8495-3544-890a-d89fb00e92f1 | -12.71537 | -46.99343 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a20492e1-8f83-32e2-98fe-c032ed810c9e | -11.95835 | -50.93394 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e000ac9a-f413-3b7e-9d8f-5e8e0b6999f5 | -10.72003 | -44.43749 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da22c45f-cfbe-3933-900b-78f06584f897 | -7.24669 | -43.37076 | 2026-09-29 04:51:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a0afcbe9-7e06-3956-8232-779d2d93ea16 | -11.38308 | -54.05061 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85a6a0e8-96a7-3240-b66d-aab50f07398d | -12.05917 | -50.93953 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73716a6d-b019-3a20-b39c-aa1143cb8052 | -12.77151 | -50.98729 | 2026-09-29 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71417114-4dcf-3f3f-8635-9d0e1e8349b8 | -12.72043 | -46.98515 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d54c8694-bf2e-34ec-a2ec-f65fa1db331e | -9.08771 | -49.88548 | 2026-09-29 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5af41766-48fb-371e-82f3-a14851770ec7 | -11.95948 | -50.92687 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dde00fd5-aa50-3abb-8da3-714ce0f0bec3 | -14.4889 | -43.26424 | 2026-09-29 04:51:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 099ff705-42ee-30d1-964c-b7e115b87f62 | -11.3596 | -54.04352 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f65813cd-00bb-3e91-be77-5193523641f1 | -7.84771 | -45.81797 | 2026-09-29 04:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fb585b3-50dc-3069-a69a-4b37297af7ef | -12.71494 | -46.99524 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 801df0c8-c525-326d-affa-6a8a1618ec13 | -11.37653 | -54.05555 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b351ac3b-7c8c-3ab5-8b44-b4fa9a6fcf06 | -7.69625 | -48.85976 | 2026-09-29 04:51:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a30ba06-60a8-3c4c-94bc-caceea47b2cf | -12.04303 | -50.95496 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bc53d57-b5bf-3511-91ad-75ae69709f08 | -7.61907 | -47.83074 | 2026-09-29 04:51:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6098b7e0-2e72-347b-89a0-06f1fa9b93c1 | -13.19695 | -48.56273 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0287237-784e-34c6-8d9c-6e302d6e414b | -12.01699 | -50.92533 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2b9d02e7-eb4b-3c71-993e-a319daa211ca | -11.86411 | -50.4655 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74324c68-e035-309d-b3bb-eb817d3ab0ee | -9.95468 | -50.15752 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b48e4982-2613-3f48-8ed4-cbbb60defe13 | -13.10973 | -47.40875 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36e50fee-3ee4-3a8b-b614-91fedb352275 | -12.01029 | -50.94594 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5cb1f02c-57c1-30e0-a440-5f4842e0fd96 | -7.38958 | -46.42484 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80ca180c-722e-3a3c-a1a6-b8063c677c09 | -11.4282 | -43.47384 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c24e22b4-dae8-309d-9681-556b7f86ef5e | -11.53334 | -47.16426 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README39.md)
