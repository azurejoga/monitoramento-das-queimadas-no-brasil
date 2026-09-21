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

## Dados Diários - Página 178

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4b5cc9b-22c7-3f82-9680-848842c267b2 | -10.0526 | -50.2406 | 2026-09-21 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| cd515553-ee59-3257-8c3b-1c3d8bdb55e9 | 1.2059 | -50.7685 | 2026-09-21 16:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 4b2fccae-df11-3b15-8d47-dad5e4f06006 | -10.336 | -50.2119 | 2026-09-21 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| b64d9263-b441-302e-acd0-5c10a4f559aa | -3.1698 | -58.5859 | 2026-09-21 16:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 539d9f18-eaa9-3cb8-a9e1-f1da95083192 | -6.1653 | -47.5052 | 2026-09-21 16:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 163.8 |
| e5fc8e8b-82db-3d99-9dee-4d1e29c76a0a | 1.0212 | -51.1861 | 2026-09-21 16:10:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 81.0 |
| d4c25f95-e1a1-32eb-bb79-bf00d4dfc4fd | -8.1688 | -54.7432 | 2026-09-21 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| c29e53c3-0a1a-3d03-be4f-c56f5f53e215 | -2.9525 | -57.7394 | 2026-09-21 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d5dd166a-3f9a-3d4e-8310-ca18d5c9ac84 | -10.82 | -50.15 | 2026-09-21 16:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5855eeab-422e-36f3-9df3-8f3668068095 | -11.05 | -46.59 | 2026-09-21 16:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08c7c68a-9988-3c36-9a5a-d99fbd77ed76 | -12.35 | -50.2 | 2026-09-21 16:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 447810ce-e12a-310f-b633-0797a6fad315 | -3.34 | -42.74 | 2026-09-21 16:15:00 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55e0b312-0543-3a45-8125-8e8ff04a9252 | -5.74 | -43.72 | 2026-09-21 16:15:00 | MSG-03 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5f2f9d0-b579-3bdd-9270-187c232e283c | -12.32 | -50.18 | 2026-09-21 16:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99053b46-5ae4-3e7c-864e-a5aa4764f3ab | -10.72 | -50.78 | 2026-09-21 16:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d36ba973-f541-3265-80da-5904811e8a32 | -3.35 | -42.79 | 2026-09-21 16:15:00 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e93909a2-7012-3934-a069-7e95facb7869 | -8.8 | -44.28 | 2026-09-21 16:15:00 | MSG-03 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2e15bb5c-f49e-3957-8fbf-cb7c51624f82 | -10.75 | -50.79 | 2026-09-21 16:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 31fdd770-9e50-3fdf-b991-8e057a772aad | -10.85 | -50.16 | 2026-09-21 16:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eff0fb38-69a4-32c1-853c-946f3edc98bd | -12.32 | -50.13 | 2026-09-21 16:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a3ce83b-65ba-3cc8-92b4-55edf83e040b | -5.59 | -45.54 | 2026-09-21 16:15:00 | MSG-03 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44523460-de46-37b5-a4de-cf89f9a486c6 | -6.5451 | -44.8643 | 2026-09-21 16:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 488b74b8-9d7e-3679-80b3-5a89b5681225 | -9.3609 | -48.3251 | 2026-09-21 16:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| bf725811-5989-3692-9b24-6396f2114c8e | -3.0788 | -58.3948 | 2026-09-21 16:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| b44444bb-92ee-308f-abeb-24832bf1fc59 | -2.9157 | -57.7983 | 2026-09-21 16:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 400.8 |
| 792132e5-fa9c-3765-bc7d-4c14a4a1ddc0 | -10.09 | -50.2581 | 2026-09-21 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 987cdd0b-5bf5-3e46-a84f-a1efa5e3aed5 | -1.3373 | -49.2947 | 2026-09-21 16:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 1a9af886-6617-3013-bd57-bd8d11c07b34 | -10.2976 | -50.2585 | 2026-09-21 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 1b57b041-a539-300c-8ce2-bfd89a81e334 | 1.2978 | -50.8923 | 2026-09-21 16:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 1b3b86d4-8b69-3ab1-b6ac-3effd4784157 | -10.4108 | -50.2683 | 2026-09-21 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 0dc22397-19c3-36d4-9e04-6955d27e387f | -6.5571 | -45.5434 | 2026-09-21 16:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 4ed312a8-f59b-3282-89c6-bc40dfbb15de | -10.8093 | -50.1621 | 2026-09-21 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 172.1 |
| d2b0d566-6873-311f-8386-58cc29d386aa | -8.1688 | -54.7432 | 2026-09-21 16:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| d7e64cec-1cb8-35b4-88df-11806935d5fc | -6.2948 | -47.6274 | 2026-09-21 16:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| a36178a6-ddbb-315d-9924-8bb2e064ad30 | -11.0048 | -49.7325 | 2026-09-21 16:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 6d366354-654a-3bee-8830-4ffeb367e178 | 1.2794 | -50.8718 | 2026-09-21 16:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 4b61b4ae-c6ce-319e-aeda-de46ff1b9ddd | -6.2949 | -57.7545 | 2026-09-21 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 6ed5dea9-e20f-325d-9c5b-5bb9f36edd07 | -1.4302 | -48.9529 | 2026-09-21 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| bf26a089-8506-3bb5-9f85-13b9b4ca707c | -0.803 | -48.6825 | 2026-09-21 16:20:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 831f1265-4e77-3abf-9a90-a5280a78526b | -1.4855 | -48.9947 | 2026-09-21 16:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 62a81838-5969-39f2-830d-4a37a877f43b | -2.9157 | -57.8177 | 2026-09-21 16:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 357.5 |
| 40d1222a-2a09-3dd9-8561-6280d02b45cd | -6.392 | -45.1948 | 2026-09-21 16:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 3071a405-6cc8-3b16-8d5e-e6b29c40cbbd | 1.1687 | -50.977 | 2026-09-21 16:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 6969279a-955c-3ab7-99cf-f82c00f2b746 | -10.4102 | -50.311 | 2026-09-21 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| cd67a430-a8e8-3196-bf69-0b80c2571ab2 | -10.2793 | -50.2177 | 2026-09-21 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 78562583-3605-3375-b6ae-a6f1f696c062 | 1.2424 | -50.9346 | 2026-09-21 16:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 69.5 |
| bbdef787-81a6-34ff-8e2e-8ac9ac1f0a56 | -10.7133 | -50.258 | 2026-09-21 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| cd69cc39-c30e-36d1-9fbe-c77d565c1d00 | 1.261 | -50.872 | 2026-09-21 16:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 67d739b0-0e03-3751-b4d9-b26ac9ab68c0 | -10.336 | -50.2119 | 2026-09-21 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 456bfa27-c949-3ff0-b9aa-a51d504ba56c | -10.809 | -50.1836 | 2026-09-21 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| fb4bea5b-f9a3-31d2-851a-6f8ae9918c38 | -8.58 | -44.5552 | 2026-09-21 16:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 157.2 |
| f7d07af5-f8c8-3195-8732-07db4f409561 | -10.3732 | -50.2508 | 2026-09-21 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 10faa2b6-eb33-3cf0-9875-f4ea0bad14c1 | -10.2982 | -50.2158 | 2026-09-21 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| f37d6f02-2975-3263-8615-3a83216e246e | -9.38 | -48.3013 | 2026-09-21 16:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 86d39638-afc2-3183-bc50-c9c178e65007 | -10.0898 | -50.2795 | 2026-09-21 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| e4633ebe-7090-3288-94ca-c361ec1f2c8b | -6.2761 | -47.6287 | 2026-09-21 16:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 9f19501b-c889-3cd3-9f7c-57bbcfb6ac2d | -10.6568 | -50.2426 | 2026-09-21 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 562eda64-f134-3f90-8473-f6d6f8683ef2 | 1.2609 | -50.9344 | 2026-09-21 16:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 69.5 |
| fb492854-6e36-32d0-bd90-f68bcb24c644 | -1.4487 | -48.9526 | 2026-09-21 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 53fa4d49-83a1-3855-90a2-233998cd6dcc | -9.0097 | -69.4036 | 2026-09-21 16:20:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 14bc4ca5-0337-3a10-bdb8-d575ebff6aa7 | -11.3813 | -44.0554 | 2026-09-21 16:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 232.9 |
| 48588e47-09d8-3810-823c-21860e017312 | -6.1653 | -47.5052 | 2026-09-21 16:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 3699ecb6-6bdb-386d-ac01-d2e4fd8de4ab | -6.5634 | -44.9084 | 2026-09-21 16:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 54a0a338-9ae7-369d-8810-48b73d98a92f | -1.4302 | -48.9955 | 2026-09-21 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 7380e047-e64f-331e-92d9-081e337b576d | -8.5989 | -44.5531 | 2026-09-21 16:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| c205d2d4-3996-30dd-be7f-d05d89f4b942 | -10.6883 | -50.7084 | 2026-09-21 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 50e4027b-81ff-3142-b31d-8d5533dd12a9 | -6.1653 | -47.5052 | 2026-09-21 16:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 229.8 |
| 3b970480-5bae-358e-810e-98c361b44fd2 | -2.9157 | -57.8177 | 2026-09-21 16:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 668.0 |
| dd0b9206-b002-3a28-aa22-7ea2cf56ed0f | -10.4294 | -50.2877 | 2026-09-21 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| e9f13d47-9638-315d-b627-307d6c4e7031 | -10.8093 | -50.1621 | 2026-09-21 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 193.2 |
| d4b87122-a094-35f8-bb67-1c3b234a0ed7 | -8.8644 | -68.5034 | 2026-09-21 16:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 681875d3-a5b1-3821-afd3-f03275d4aa0e | -10.3357 | -50.2333 | 2026-09-21 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 63599527-08d9-397f-b391-8711d66374f6 | -6.2761 | -47.6287 | 2026-09-21 16:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 2aed5a92-1ca8-3db3-959b-ed1cdf5a90d9 | 1.2423 | -51.0178 | 2026-09-21 16:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 78.2 |
| c31397b3-2423-3ad8-97ec-b6c239ef59c4 | -2.9526 | -57.7006 | 2026-09-21 16:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 9e1ac34d-8444-324b-985d-c0fd27485b24 | -10.2979 | -50.2372 | 2026-09-21 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| d8f6f463-0ce0-3515-a4b3-9cf3210e909a | -9.7504 | -46.0637 | 2026-09-21 16:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 71dcb410-63f6-3caf-b420-1750700d3035 | -1.4302 | -48.9529 | 2026-09-21 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 14dc7aaf-8c71-30c5-ba36-e738039fc20a | 1.2055 | -51.0182 | 2026-09-21 16:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 6c12a4fd-deb5-3b4b-bd94-3dfc0f59f52a | -10.0714 | -50.2387 | 2026-09-21 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 142.6 |
| e98d3314-1972-3c0f-b434-821869e60ef0 | -2.8974 | -57.8181 | 2026-09-21 16:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| f5622b0a-3157-3733-93ca-18018d7ebe7e | -6.5569 | -45.566 | 2026-09-21 16:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 215.9 |
| 9fc31568-b727-3dd3-9425-847f8ce93373 | 1.2424 | -50.997 | 2026-09-21 16:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 4e0a55c0-a819-3801-9527-b788b359bd71 | -11.4549 | -45.3202 | 2026-09-21 16:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| cba2a1aa-a9b6-3878-ae72-2e8c40187ed9 | -6.5451 | -44.8643 | 2026-09-21 16:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 688.7 |
| 3bf9ac10-6e62-3b17-bef0-3fe08697acfe | 1.0213 | -51.1447 | 2026-09-21 16:30:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 91.2 |
| f3e8c1a3-dfc8-340f-a356-5d6c57b1b2c8 | -1.2267 | -49.2537 | 2026-09-21 16:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 5bcf14d0-a7be-33bb-a470-b06c7b55e72e | -8.58 | -44.5552 | 2026-09-21 16:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 52293e6a-c7a3-3fcb-814a-2b550d10a5bf | -2.9525 | -57.7394 | 2026-09-21 16:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 59cd4664-98a5-31f6-a65a-8d1b0dad4b64 | -1.4487 | -48.9526 | 2026-09-21 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 6b3df269-c791-3e6e-a8c6-03172b9d795f | -6.392 | -45.1948 | 2026-09-21 16:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| ec434f91-77fe-326e-9560-bfaac6304e98 | -0.8583 | -48.7248 | 2026-09-21 16:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 60a869ce-231e-3954-8737-88265035dd8f | -10.6516 | -50.6271 | 2026-09-21 16:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 163e5381-b8ee-307c-95d2-476d87acdadd | -10.809 | -50.1836 | 2026-09-21 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 1d90c987-17f9-3a06-8008-d8e7ca8d8b09 | -2.9157 | -57.7983 | 2026-09-21 16:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 458.8 |
| 111dbb99-6c9c-3f7b-a142-9872fa256007 | -10.336 | -50.2119 | 2026-09-21 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 316608fd-19c7-3aa0-aa7f-15a1e1666f22 | 1.1319 | -51.019 | 2026-09-21 16:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 98a6468d-4311-3c41-bed8-046c18905ae9 | -6.1651 | -47.5271 | 2026-09-21 16:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| f9e3cb5e-9dde-3b45-bde1-50026da25f63 | -10.4102 | -50.311 | 2026-09-21 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| cf5b4f3c-1355-3dc1-8a13-969ba4468aad | 1.0212 | -51.1861 | 2026-09-21 16:30:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 78.5 |


[Clique aqui para ver as próximas entradas](README179.md)
