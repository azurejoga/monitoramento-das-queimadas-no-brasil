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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 730a8957-af02-3fd5-9bf4-d426436dfa72 | -5.76274 | -47.34243 | 2026-08-01 04:55:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| efd29d6e-bce0-3a32-b2ae-8f679b40d1fc | -6.56875 | -56.53094 | 2026-08-01 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50d96827-961a-3413-aeb6-a69e664b59c2 | -8.96597 | -45.20498 | 2026-08-01 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e0c640c-fa33-3b64-8c05-183ecc7d150a | -3.03564 | -48.40804 | 2026-08-01 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04c0ef9c-3471-303d-a606-e355d5c0d3fb | -7.50155 | -45.84236 | 2026-08-01 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0f65d592-194d-3ac3-a073-72956857254e | -2.60009 | -47.34396 | 2026-08-01 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47fe6da5-a032-3880-9eed-4497ccb60dd6 | -2.95305 | -48.95819 | 2026-08-01 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5ef37f7-6be2-3d88-834c-9810aedefbb0 | -4.65435 | -42.43427 | 2026-08-01 04:55:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 111a39ce-4a6b-31cb-afd1-35eb77432cf3 | -6.56463 | -55.1455 | 2026-08-01 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a52ba42-4dec-3802-8fc3-2b60380747fe | -3.6607 | -49.18781 | 2026-08-01 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afadfcb1-1777-36b9-8139-df0ffac129de | -3.0385 | -48.41231 | 2026-08-01 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33ba95c1-97fe-3dc9-a0af-73b5e8b727b0 | -6.17887 | -55.5269 | 2026-08-01 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1bb839b-aaba-362d-bb66-775edffac03b | -6.64419 | -44.58376 | 2026-08-01 04:55:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16e59da7-9bd2-3721-b7ec-3d59038b7896 | -4.65232 | -42.43073 | 2026-08-01 04:55:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 54e075fd-eebc-3ef7-a216-2a00800260c1 | -6.76213 | -41.01309 | 2026-08-01 04:55:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 31414b08-a5e9-3a70-93d8-1cc01b0b6a89 | -4.37142 | -47.77092 | 2026-08-01 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a3139c85-3b51-38e9-91db-8a6a141de30a | -3.38218 | -52.80265 | 2026-08-01 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6945f1a-4293-3f9a-b1f1-30bb06c48e63 | -6.76298 | -41.00919 | 2026-08-01 04:55:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a9526477-52ca-3985-be43-cdda0dd10f32 | -4.00042 | -43.28891 | 2026-08-01 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 10531ddc-fc83-3656-a5d7-721cf11c81f2 | -5.55762 | -43.97068 | 2026-08-01 04:55:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a5eede71-be9d-3f1e-9ac8-47378755a19d | -6.76242 | -41.0132 | 2026-08-01 04:55:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3caf3295-b54c-31ae-977d-dfb4bbf5aebb | -4.36783 | -47.77036 | 2026-08-01 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 33106db2-634f-30cd-90b5-6764caf52600 | -7.5527 | -43.98702 | 2026-08-01 04:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32e730bd-f192-3451-bb16-464da7a3f488 | -6.76266 | -41.00907 | 2026-08-01 04:55:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 35193058-f573-39f5-8497-909f316c7020 | -3.84864 | -44.09378 | 2026-08-01 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c9bbbbe-3f14-32d5-bc82-50d24a2a1e76 | -6.5594 | -55.15577 | 2026-08-01 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5a2d6f76-c051-3d06-bf4d-6bbefacb73ef | -3.11297 | -47.91145 | 2026-08-01 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9d6534a0-2aa4-38da-858e-7ca4fe18d65c | -6.64777 | -43.91287 | 2026-08-01 04:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 29f944a6-3e84-392f-91ba-0b9739bfebbc | -7.64552 | -45.05067 | 2026-08-01 04:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f74ba73b-e9da-31a3-a3bd-7e2cf0484176 | -7.83539 | -47.09168 | 2026-08-01 04:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83f1bba7-aa05-35d0-b3f2-af6b5754e03c | -6.27026 | -41.87643 | 2026-08-01 04:55:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e6b3024a-1b74-3708-864f-8d10007343fa | -7.25014 | -42.13506 | 2026-08-01 04:55:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 14758bcc-32ab-3e58-bf48-5844251e42b3 | -3.11236 | -47.91536 | 2026-08-01 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7985419c-65b8-3dfb-b10c-29de0c866e81 | -6.56153 | -55.16376 | 2026-08-01 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c9c8533e-22a3-3bd8-9447-2eaa71d30789 | -8.98039 | -45.1686 | 2026-08-01 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a5340419-65f2-3d91-9326-325d0be9f111 | -3.4278 | -49.02374 | 2026-08-01 04:55:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5fafec3-62ee-3897-83ff-0aacc7053d43 | -3.67708 | -49.4783 | 2026-08-01 04:55:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab308ce2-4b26-39f9-8593-00f9b1d656bf | -3.11649 | -47.912 | 2026-08-01 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 749bd94c-9df8-307a-a355-9b9a90e32a9d | -6.01133 | -47.40365 | 2026-08-01 04:55:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f6c3a0f-15b7-3c3b-9ada-80bfb7a06342 | -5.55693 | -43.97543 | 2026-08-01 04:55:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 93bdec42-de73-3e0c-8cd3-fb4cb9ccb4f5 | -8.98193 | -45.16634 | 2026-08-01 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 654e452e-a353-3a3a-9ca8-cfb71d7ddbbd | -6.73464 | -48.25756 | 2026-08-01 04:55:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a0497cd-7647-3041-9479-fec053a1790a | -7.5021 | -45.83849 | 2026-08-01 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f77cc88d-cbb1-3d0a-909d-f9e209733f89 | -7.6506 | -45.04686 | 2026-08-01 04:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89767fc3-2021-32dd-b7f3-ecea6819e241 | -2.94966 | -48.95766 | 2026-08-01 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d62f93b-3c47-3e21-b33f-740f1adc90d2 | -6.56168 | -55.1655 | 2026-08-01 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f6358b4a-d5a1-39c9-a584-bf16d689c6ea | -4.93848 | -41.98473 | 2026-08-01 04:55:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2cb43447-1538-34f0-9019-bd7c0d319d9d | -4.25716 | -38.03901 | 2026-08-01 04:55:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| d0f4fb43-2165-33af-90b2-e97bea6bf2bf | -4.64468 | -43.12438 | 2026-08-01 04:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7936b4eb-ae44-32e6-8b22-5f008b1342f7 | -3.85378 | -44.09014 | 2026-08-01 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72826d60-1f4d-30c8-b54f-db9453672bfd | -6.7632 | -41.00504 | 2026-08-01 04:55:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 297fe055-fe34-3a91-8e6b-5ee426c089e7 | -4.26669 | -38.03452 | 2026-08-01 04:55:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 15.0 |
| fe1411c2-013d-3034-bd4b-2013de1777dc | -3.0554 | -39.93083 | 2026-08-01 04:55:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| da22abc1-7bf5-320c-9798-44f34807e14a | -4.93725 | -41.98421 | 2026-08-01 04:55:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bd3fb5f7-e7ff-3378-bb6c-bb7b882d7b78 | -6.56072 | -41.84008 | 2026-08-01 04:55:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| d6e8025b-14b8-3b7f-9f48-fa335c58c7a0 | -6.15177 | -47.23804 | 2026-08-01 04:55:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2aec59c-6785-3ff0-abee-86cf8ad017ad | -3.03506 | -48.41177 | 2026-08-01 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6a162fb-108b-3755-a89f-8f374cd19bfb | -3.05289 | -48.74302 | 2026-08-01 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d14ef8ca-9f41-3168-b23b-dd3bc5f42216 | -2.89145 | -48.01363 | 2026-08-01 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdd537fb-07c8-356d-89d8-e5fffb7b0bf0 | -6.66952 | -42.56998 | 2026-08-01 04:55:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b1882f21-be6d-3cd3-9860-19c1ef075e1a | -7.24856 | -42.13571 | 2026-08-01 04:55:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd29764a-7492-389d-bffd-f01b237823b4 | -4.36771 | -55.77069 | 2026-08-01 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2df7444-7c09-3574-bbfc-8dafefd99694 | -8.5808 | -45.06771 | 2026-08-01 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd1fff47-b728-3e63-b446-6aa236ca1256 | -5.73085 | -44.50232 | 2026-08-01 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80b22628-205f-3db7-b134-198150e49a9e | -8.31171 | -44.7921 | 2026-08-01 04:55:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da062ef4-1f56-33dc-9800-9533c3285063 | -8.52845 | -48.28979 | 2026-08-01 04:55:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 244a3f9a-a85e-373a-b2c0-5fed5ee2bc91 | -3.51541 | -48.88838 | 2026-08-01 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0737ebbd-291e-3694-86e7-3c45a497f6b5 | -6.66906 | -42.5665 | 2026-08-01 04:55:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b5452dea-75a7-3dfb-af5f-26bbe0583cfd | -2.7897 | -49.52451 | 2026-08-01 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ad8e01db-0928-3384-b5e0-86028af16351 | -6.6518 | -43.91844 | 2026-08-01 04:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 66fa67b9-16ef-367d-b8b3-676d7f0c3be8 | -7.5063 | -45.83915 | 2026-08-01 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b317eb74-a8eb-3348-a8a3-997ba003b7f9 | -7.55199 | -43.99218 | 2026-08-01 04:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35612e06-1ad8-31cd-b7db-710f7a53fbc5 | -8.34914 | -45.98818 | 2026-08-01 04:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86fa4f81-d93f-311d-8d45-8eb950a1ade0 | -4.64926 | -42.43347 | 2026-08-01 04:55:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1362ae42-688a-385e-9b41-73b316ceb9e8 | -5.75288 | -43.26613 | 2026-08-01 04:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c8f4d66-13c0-37dc-a555-18f055d38c4f | -2.88735 | -48.01695 | 2026-08-01 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e914f069-1216-3d82-ae4f-cb3f3f011b95 | -5.73152 | -44.49788 | 2026-08-01 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a83fccd6-899b-3b18-9a9a-eb1fcaf16ef5 | -7.23433 | -44.3708 | 2026-08-01 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| edb7c7ba-49cb-3988-82bf-bc592aac2893 | -6.42365 | -46.20189 | 2026-08-01 04:55:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac16972c-a605-393f-b482-66772a9bb5ee | -6.42264 | -43.71684 | 2026-08-01 04:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aac07389-c2d9-3b4b-90bd-6526e38485a8 | -6.1894 | -46.6972 | 2026-08-01 04:55:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d170ba4-8a79-3dc2-b642-cbea0e2cbc0e | -8.98134 | -45.17062 | 2026-08-01 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9c7e7eb-d282-3c22-8eea-14532a9d5678 | -3.06194 | -39.92737 | 2026-08-01 04:55:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b11a7167-d223-3eb0-96f2-f35f14abd9df | -6.86585 | -44.78801 | 2026-08-01 04:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 273673ab-8bd4-353e-9cfc-f536395b0da0 | -6.42338 | -43.71163 | 2026-08-01 04:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1c80434d-180c-3138-ac84-e3321ac6f6f1 | -6.98897 | -51.30563 | 2026-08-01 04:55:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1b392b9-7c5d-34e5-b185-89445c7311fa | -8.31625 | -44.79297 | 2026-08-01 04:55:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63c1a81f-695f-3ef4-9a07-a4f653094b81 | -4.25805 | -38.03308 | 2026-08-01 04:55:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| b0958b29-116a-34dc-907d-6bf48839c983 | -2.60073 | -47.33989 | 2026-08-01 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6edecc06-d2ba-394f-89e2-5e4479419b62 | -4.25912 | -38.03944 | 2026-08-01 04:55:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 88ba23c7-d0c6-382c-8572-7f07109b2f78 | -3.96603 | -48.12843 | 2026-08-01 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3a445d5-3eee-3604-a690-d93bd911b311 | -6.55526 | -41.83932 | 2026-08-01 04:55:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 91aee277-c806-3a0b-a3df-22119c2b8160 | -2.88795 | -48.0131 | 2026-08-01 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a03b15f1-b2b7-33f5-a9e3-c0e254aa8fad | -7.20022 | -42.96801 | 2026-08-01 04:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 616daea3-4012-345c-b132-b56459077272 | -6.71626 | -44.01649 | 2026-08-01 04:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fc23ba9-b46f-39cf-94b7-6a12ab441530 | -4.25995 | -38.03354 | 2026-08-01 04:55:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 6d9baac4-7ba0-3b15-b22e-f5fec6852111 | -4.64969 | -42.4305 | 2026-08-01 04:55:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5f33a1a7-51b5-361d-bb4b-1ee9eb761e8b | -7.6665 | -45.06255 | 2026-08-01 04:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49b1a725-7649-34b6-9a8a-bbb52017e471 | -8.96781 | -45.20271 | 2026-08-01 04:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 002bdc98-f358-3c75-844d-7ed98561a854 | -5.81387 | -44.75777 | 2026-08-01 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README17.md)
