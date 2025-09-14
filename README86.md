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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a246fc79-a27d-334b-ae40-ea5262d46827 | -8.7683 | -46.0373 | 2025-09-14 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| dd486018-514c-3502-aa9a-30532bafcbda | -8.9359 | -46.1995 | 2025-09-14 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| f4f897c4-1329-3d03-8cb8-9e5ce73e0e29 | -11.8672 | -50.4933 | 2025-09-14 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| ac4467c8-1100-3aca-85f9-058dd383b863 | -10.8991 | -45.4656 | 2025-09-14 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| eebb8df8-71bc-3f40-a055-920fc68e47fd | -15.7786 | -53.482 | 2025-09-14 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 129.0 |
| f730838a-bb38-37c9-b179-7b45ba44c468 | -10.7474 | -50.5319 | 2025-09-14 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 44b50dbc-9777-359e-a71f-b487801c0aa7 | -10.7683 | -46.5034 | 2025-09-14 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 18489d4b-5abb-31ab-b7f6-dfff42638ff7 | -12.8208 | -47.1671 | 2025-09-14 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 5ca0e78b-175b-3c3f-a2a9-46f27a7b0eea | -10.9262 | -47.3561 | 2025-09-14 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| e808d94d-1a6a-374b-aa49-ffd19ce4d136 | -8.9976 | -45.8098 | 2025-09-14 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 204.5 |
| d0238c62-6fc5-3f6e-af06-64b5336bff88 | -10.4331 | -50.0093 | 2025-09-14 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| c3a45e54-df97-3104-a9e5-32b0ee208708 | -22.4993 | -50.6273 | 2025-09-14 13:50:00 | GOES-19 | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 175.8 |
| cb1db55e-6240-3f32-9150-9882cdbd9c30 | -16.0061 | -47.9329 | 2025-09-14 13:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 5a2a34ed-d1a5-34d3-9840-2bde522d669c | -14.4307 | -43.2228 | 2025-09-14 13:50:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 164.4 |
| fbc1e663-0868-3127-9f8a-5b3b28d788a2 | -8.9173 | -46.179 | 2025-09-14 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 187.3 |
| cb432895-e8ab-378e-b8df-c7433e15eff7 | -10.9452 | -47.3538 | 2025-09-14 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 700bde3e-b18d-3023-b41a-fcc278538c41 | -8.9079 | -45.457 | 2025-09-14 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.3 |
| ccbbcaef-1d7b-3dd9-a84c-976c4789284d | -8.1383 | -43.6764 | 2025-09-14 13:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 162.3 |
| ff2d1f08-c0e1-389e-83b3-6e2cfdf3857a | -8.1386 | -43.653 | 2025-09-14 13:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 6bbe03af-511d-3181-b3b6-f72681f08bbf | -10.4065 | -50.5884 | 2025-09-14 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 4bf8745e-220b-342f-becd-437f7fd52dbb | -12.7859 | -48.0432 | 2025-09-14 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 4846aa08-5ef8-3572-ad91-9a6cba9d50f6 | -12.8019 | -47.1474 | 2025-09-14 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 21e7f0f9-62d3-3d44-9c8c-3e5c2c1bd34a | -10.5459 | -51.4844 | 2025-09-14 13:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| e9e4ddfa-f84d-3349-b76b-59c65c6bbf4b | -8.6404 | -45.7122 | 2025-09-14 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 66624e45-0723-32a4-ab0a-7d6e12451d6a | -9.976 | -50.3334 | 2025-09-14 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| d6c48cec-b06b-3e0d-a78b-f73f68800b0e | -12.7671 | -48.0236 | 2025-09-14 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| e9f2b519-84db-3f07-afbf-98c3f252a719 | -11.2927 | -50.8143 | 2025-09-14 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a62b4875-3b24-3f06-966c-f06c0da99278 | -8.9979 | -45.7871 | 2025-09-14 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 728b343b-298d-3111-974a-98abcad6f2b2 | -11.8675 | -50.4718 | 2025-09-14 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 202302f8-284a-34c1-bdcc-e19d5e602a12 | -8.9076 | -45.4797 | 2025-09-14 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| e4db1c71-d894-3273-9b27-7b7d6b5f26b6 | -14.329 | -46.0857 | 2025-09-14 13:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 131.2 |
| ab0580f7-2fc6-3c2e-9b07-c8ab9d0f783d | -16.0056 | -47.9555 | 2025-09-14 13:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 69.3 |
| ba9c2064-1ce0-3a5c-a49a-03bf8dac397a | -7.5281 | -47.642 | 2025-09-14 13:50:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 0d3a7e30-e108-36ae-a954-01336e86d0bb | -8.956 | -46.1074 | 2025-09-14 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 265.2 |
| eea2a2a7-5d23-38f3-b73f-46b528a8dd46 | -12.7286 | -48.029 | 2025-09-14 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 51642399-f0c4-3a4b-946d-786cc7d992c4 | -8.6436 | -44.0396 | 2025-09-14 13:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| a22ff311-10be-32de-83d8-87c3b97ca7c8 | -15.1995 | -50.1101 | 2025-09-14 13:50:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 15fb5297-b924-33c4-8e24-1d75e6e1a9a7 | -14.3944 | -52.9034 | 2025-09-14 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 579d3010-013c-3b0a-9be8-c93b28648c4b | -8.9362 | -46.177 | 2025-09-14 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| ba5ec1d1-beea-356d-a90c-fcfd0f990484 | -11.5037 | -43.6373 | 2025-09-14 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 87fc87c4-d209-36c8-978a-f8bf76c38ad0 | -8.9365 | -46.1545 | 2025-09-14 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 083450e7-b626-3056-91f6-bc310ab123a6 | -14.2917 | -45.0964 | 2025-09-14 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 076706dc-a0bc-3f40-89c1-76721ef681b0 | -11.353 | -43.495 | 2025-09-14 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 0fe01615-7d02-34fe-a1f9-23ecca1d0fc4 | -8.7871 | -46.0353 | 2025-09-14 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 2f049c46-43f9-32b3-90f9-f637a03313ff | -14.4783 | -47.3141 | 2025-09-14 13:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 48c22f30-9a65-3ea9-b7a2-63a3f2aa006e | -10.8803 | -45.4452 | 2025-09-14 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 37a6026f-4d78-3ad3-ba64-84a85ef4dbd3 | -12.8212 | -47.1445 | 2025-09-14 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 774cdb07-83bf-3dac-94e0-52203daa50ec | -11.293 | -50.793 | 2025-09-14 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 69c16155-a23c-3e01-927e-6337da2af5a4 | -12.7667 | -48.0459 | 2025-09-14 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| e866b1f6-8a09-33ad-9eea-5a92875d84d9 | -8.9368 | -46.132 | 2025-09-14 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 386.0 |
| fc897469-5e09-329c-9b3e-c2b878a3df4e | -12.7675 | -48.0013 | 2025-09-14 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 86fbd2eb-01c4-3535-8598-091383e0283e | -10.3699 | -50.507 | 2025-09-14 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 121bb326-9cea-3e8e-9081-b9c9a9c21a80 | -10.9182 | -45.463 | 2025-09-14 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 214.0 |
| a0f0ec34-0a8d-367f-a754-6eef1a0b664c | -11.0427 | -49.7283 | 2025-09-14 13:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| da73c6bd-e867-3ea6-9bde-091336e124a0 | -14.2912 | -45.1198 | 2025-09-14 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 0b3348d1-5a6a-37e6-a0fa-a1c77cf3f32d | -13.5879 | -51.6502 | 2025-09-14 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 062b7d49-a1ca-364d-bd89-79c3fbf18023 | -6.9798 | -44.5529 | 2025-09-14 13:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| ee2e4507-f515-33ec-b9f1-c57b5ce2e859 | -15.7333 | -56.2122 | 2025-09-14 13:50:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 3d1af3fc-8af7-33c4-99f2-e4bd70e69de3 | -14.3285 | -46.1088 | 2025-09-14 13:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 161.3 |
| c9b3147f-f2b0-356e-9826-e20d444893bd | -13.5096 | -51.7451 | 2025-09-14 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 4bed0680-f4e9-3742-8924-2933878beafc | -9.7389 | -46.8728 | 2025-09-14 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| ffa0577a-104b-32bb-a5e6-5ff2a4bf717f | -11.2695 | -51.1142 | 2025-09-14 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 9bcbccf1-3496-3ad9-96e2-2fc787aef5fc | -10.3696 | -50.5283 | 2025-09-14 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| b418bdd5-d5b1-36bc-ad57-ab9dc9d06a61 | -13.5876 | -51.6715 | 2025-09-14 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| b34cad5b-20f4-3132-acb1-5a9aa62d74a1 | -9.7579 | -46.8706 | 2025-09-14 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 6c04076b-d971-3c13-b4a0-fdf359b0bc66 | -15.7782 | -53.5031 | 2025-09-14 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 8482d18a-a320-3f7a-9c8d-442ec5db08e4 | -8.9746 | -46.1279 | 2025-09-14 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| e70fe805-6021-3198-8dff-f26ad7395d72 | -8.9371 | -46.1094 | 2025-09-14 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 248.1 |
| eed47eac-bbbd-3b01-a878-a4d479a3370a | -14.3747 | -52.927 | 2025-09-14 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| dab5985a-ecc3-317a-86f9-5a33ff9033a5 | -6.9986 | -44.5512 | 2025-09-14 13:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| e1597d45-6c78-3115-8393-9189aad78c75 | -12.7478 | -48.0263 | 2025-09-14 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 5bc4da5f-7db2-3c9f-be5d-ddcd739f2f15 | -23.0597 | -48.5716 | 2025-09-14 13:50:00 | GOES-19 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 3432738f-0b34-3dc9-bd54-94e7c3f2a8e0 | -12.0856 | -47.5618 | 2025-09-14 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| e3874392-6a07-3e38-8f2c-84236573518d | -14.7524 | -60.2519 | 2025-09-14 14:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 540d1add-538a-38b3-9b8a-fb0f0e03a455 | -12.1048 | -47.5592 | 2025-09-14 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 6394dd15-0cb7-3759-8e1b-bb7080d07707 | -11.0617 | -49.7261 | 2025-09-14 14:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| c5b9b32f-5986-326e-92a3-a7bcca701f75 | -11.293 | -50.793 | 2025-09-14 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 811ae3ee-1a87-3506-b1c7-c1b30ff8489c | -14.4779 | -47.3368 | 2025-09-14 14:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 4ff4600e-7abf-3a46-a31d-e97c2546aecf | -6.9986 | -44.5512 | 2025-09-14 14:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 58762fce-287f-3462-a2f1-0133eff07376 | -14.329 | -46.0857 | 2025-09-14 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 22747d7a-8cfc-3012-ad1c-1291a0b8936e | -8.979 | -45.7892 | 2025-09-14 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 7bb073de-193d-337f-8500-8650f80b155c | -14.7716 | -60.2503 | 2025-09-14 14:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 353edc4d-5a76-3904-a14c-18a7a8884dd1 | -11.2927 | -50.8143 | 2025-09-14 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| ad8bfdd2-fe1c-3752-8de8-e9339238e288 | -10.9182 | -45.463 | 2025-09-14 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 224.6 |
| abd75118-8933-356a-a392-2037bd165c32 | -11.0427 | -49.7283 | 2025-09-14 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3a79b070-4708-3522-8f35-7639a6f2e883 | -10.3696 | -50.5283 | 2025-09-14 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| ef36832d-b282-3c71-bd3b-50eddc84c669 | -12.442 | -46.8847 | 2025-09-14 14:00:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| b757be29-705e-3ee3-88e7-43b8fa439e6b | -8.9368 | -46.132 | 2025-09-14 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 584.2 |
| 5ce9dc4e-72b0-31e4-99eb-3b44e57521bd | -10.75 | -46.4607 | 2025-09-14 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| bb3071a6-8cde-30c8-bfb6-c5220dd10bf1 | -13.5159 | -41.4779 | 2025-09-14 14:00:00 | GOES-19 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 117.0 |
| 62678659-5733-3aa6-b99b-96b6e922312c | -10.3888 | -50.5051 | 2025-09-14 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 37121470-c3cf-3663-ac69-c0cdcc15dc37 | -10.9096 | -47.2023 | 2025-09-14 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| d4d9e5c1-7063-36ee-8e7b-c494c7edded0 | -14.3747 | -52.927 | 2025-09-14 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 0ccfe4bb-cb0f-3c8a-af9a-51e8f009dc4f | -11.2924 | -50.8356 | 2025-09-14 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| d2bc52f6-3186-32a2-9396-435669aa9832 | -10.5459 | -51.4844 | 2025-09-14 14:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| ed213ff8-3bb0-3135-9f55-8429b986435a | -15.7786 | -53.482 | 2025-09-14 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 127.3 |
| a86f234d-a17b-32fb-9797-6212069d3c8d | -8.9979 | -45.7871 | 2025-09-14 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 63a43cc5-c76c-3a8e-b320-fa05d2174737 | -14.4307 | -43.2228 | 2025-09-14 14:00:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 196.7 |
| e4a4dc5e-7305-393f-b84b-f9cd4706e26f | -12.1044 | -47.5816 | 2025-09-14 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 640cb8d3-727f-3ae4-b96b-263b79ab8e21 | -14.2102 | -46.1979 | 2025-09-14 14:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 166.7 |


[Clique aqui para ver as próximas entradas](README87.md)
