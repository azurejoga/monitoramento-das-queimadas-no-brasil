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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b68b5ba-bd1b-3de4-9842-a4207b5d8222 | -5.34692 | -47.29419 | 2025-09-13 05:25:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 208fb9c5-4e68-3aae-9290-cfc87bd152b8 | -11.8802 | -50.57048 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c8df319a-6a0d-3815-a64c-3b8acb562613 | -11.18082 | -55.09188 | 2025-09-13 05:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bb5fbed-cfaf-3812-8c20-7a80f0b44031 | -9.50131 | -55.9721 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e2019d5f-72a8-3a39-86b0-568306afd084 | -11.15046 | -50.69286 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 12044d85-f7f5-32a2-9c73-a7bc6a2430d3 | -9.24116 | -51.2337 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31e8e95b-41f3-38f3-96c6-e2bf13f0efad | -11.16016 | -51.37497 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4cb65443-e397-30b4-910a-d76c8b368e2d | -11.19477 | -51.42382 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc9639fd-d47c-317a-926a-d80a78110be1 | -10.37197 | -50.49826 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56c49950-9a10-3e86-a64d-6b7024b713c4 | -4.92408 | -55.77771 | 2025-09-13 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6eb98d24-1809-3a4e-b849-4afb19f834f2 | -10.70448 | -54.44412 | 2025-09-13 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c459b732-b6d5-3105-89f1-001c3598802f | -4.53474 | -55.68561 | 2025-09-13 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 368cad27-d7c2-3160-9429-6a1e73b8367e | -11.27779 | -51.13353 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 99c1570a-97ce-329a-a371-6a4ceb0e014e | -11.83914 | -50.55113 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c54ffd6-2203-3256-8583-c5a0a188bfcf | -11.84396 | -50.55741 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27b7c313-4be0-3bb6-8330-2dd52ed71c02 | -11.10301 | -51.44541 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 7ab67e8c-be33-3fbf-8706-defe3f37b5d4 | -10.79144 | -50.54078 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41127740-4427-394b-a3e6-c942936cc5c1 | -9.52112 | -54.63145 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| ea392c18-79ff-34f2-b253-96b107f506fc | -10.65375 | -48.97208 | 2025-09-13 05:25:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c914d8b2-fd78-3ec9-83de-99f820178d77 | -9.8166 | -48.89388 | 2025-09-13 05:25:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b451cb24-222f-3101-8f4b-555ddb843fbc | -11.863 | -50.5589 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2c6720b0-85e8-3696-bee7-b35469f45278 | -10.42163 | -60.79655 | 2025-09-13 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12a6a2d3-e544-3a53-8d2d-128b6846c525 | -11.18199 | -55.0831 | 2025-09-13 05:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fc962bc-d744-378b-bf7d-778427389a5c | -11.11289 | -50.7015 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6c95b42-4034-3048-b8aa-39fdb0f24cf0 | -11.08169 | -51.43066 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 125cb2af-9e8f-3466-8a43-af8680fff44f | -9.90946 | -57.06087 | 2025-09-13 05:25:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fca931e-fa9e-3a93-a93b-449962faf228 | -9.97019 | -50.30026 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cccada8e-d3d9-3c1c-acf1-e27dc861daa6 | -10.33247 | -48.82535 | 2025-09-13 05:25:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de870bd6-f81c-31f6-a891-83b0d8cfceec | -11.14447 | -50.6921 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 33.8 |
| d792bbf1-c6f7-3c1e-b79b-93b06a0a319b | -7.96867 | -55.30283 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ce0d35d-4237-3012-9f9c-60123cf06c38 | -9.12218 | -58.90842 | 2025-09-13 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0084736-f6b4-3061-a02b-ed3680445aea | -9.49417 | -55.96347 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d80c8067-93f6-3067-93f4-0dff693821c1 | -10.40273 | -60.80802 | 2025-09-13 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a839cb9e-f242-3abd-b31c-b337bd389a69 | -11.10084 | -51.43157 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ee05d884-6217-3896-9080-4d4ce799107f | -8.42865 | -55.63437 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d4157e3-11c0-3958-8950-57812afecfbd | -10.50223 | -51.54904 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 992a6a0c-8633-3058-9e4a-ef233e204f2d | -12.00498 | -47.75826 | 2025-09-13 05:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b3714b16-6d4e-3952-851b-4fcdeb1b5ef1 | -9.25673 | -59.40017 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 52beef61-e78d-3838-834d-f005fedc7a79 | -10.00243 | -59.97229 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 781d7224-8503-3abf-b4cb-29425c8cb441 | -11.18854 | -51.42702 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30fc7f40-5c5d-3b9b-8f13-6ff780b1d9b8 | -11.88686 | -50.5666 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 50eb277b-2fdc-3c9f-9bd4-b2453a0fdd39 | -11.83843 | -50.55202 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 458c00ff-22bc-3cbd-a977-71ffb6b37f7b | -9.86916 | -63.40734 | 2025-09-13 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f1cdf9e-27a0-33b2-8f5c-93444e1ef5f4 | -8.09365 | -50.18593 | 2025-09-13 05:25:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b38bfddf-9e2a-3d5e-aada-058c60607f91 | -7.7594 | -61.12025 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ab27f2dd-e7f6-398a-8888-87ab4c8798fc | -11.87356 | -50.57433 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 140b93c4-f026-3ba6-adbd-b4095beecb1f | -11.82623 | -50.5505 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cdd7d692-3fb8-33b1-8e35-131b78da8e66 | -9.90598 | -60.21609 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 986f4186-6a78-3d35-a78c-fcc721c7d8e1 | -11.86692 | -50.5782 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a12ff1bd-87af-3486-ab5d-28be932f56a4 | -11.09781 | -51.44073 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c5d8147f-70e3-3cc4-9e3e-6b612cccfa13 | -9.80597 | -61.52339 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72fd2fa7-e05e-3523-b055-64fcd3dc9127 | -7.27151 | -57.57561 | 2025-09-13 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aeeecb3a-afa6-38bc-8b2b-629936e96b61 | -9.25701 | -57.08172 | 2025-09-13 05:25:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 750dacf7-b3c9-366d-951a-73837f6fa14f | -9.22747 | -51.25095 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c9e10af-b5b6-31e4-8e04-770e15276659 | -11.86082 | -50.57743 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2b6092b1-d7c8-30c3-951d-c9c2b96ec464 | -9.80431 | -61.51234 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc92e9ba-b89c-365b-8d7b-46351a2d9d62 | -9.25095 | -51.24672 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f47d4f1-f4d8-3f89-b08b-fbfc3cd5135a | -5.32628 | -55.88811 | 2025-09-13 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a0f081c-5619-35fd-894c-3930e5bc0915 | -11.19628 | -51.41192 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 000e1d9a-8f2a-398b-bb32-2c9a1b17e72a | -11.17288 | -51.41289 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 0b5bc4bc-dcbe-35b9-b090-ecf9a4bb8744 | -7.32133 | -46.58532 | 2025-09-13 05:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 73147e4b-27e0-30fe-b22e-6e94f4f233cc | -11.07799 | -51.42854 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e3c0ea83-e265-3438-8d2e-6ffa6247da15 | -9.25617 | -57.07024 | 2025-09-13 05:25:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 080a3cc9-d92f-3a8e-bbd6-2d744fca338e | -9.95326 | -51.69078 | 2025-09-13 05:25:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6e164c3-3de4-3a1a-adc9-6b439ecb6555 | -11.3826 | -47.32502 | 2025-09-13 05:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 22328575-7db9-3756-964e-9ba78f415127 | -9.24364 | -51.2145 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f23e733a-fe38-3c0e-b852-2f2e3b335c2b | -10.51278 | -51.55595 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45d8d208-8032-3be3-9d3c-ca7f284b87ea | -11.99695 | -47.76484 | 2025-09-13 05:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| df2b8e19-8bed-39be-b2ca-e14f4f29f143 | -9.24067 | -51.23753 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1828a2b2-248d-3223-b595-a9bc3e8b5ed3 | -9.88466 | -58.33509 | 2025-09-13 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61b3aa0c-e690-367a-a7a5-2a3f32c54616 | -9.24581 | -51.24217 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d232ea7a-11b7-3c99-ac52-c047b43ffddc | -12.12668 | -47.59353 | 2025-09-13 05:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70ddb900-c830-3155-b564-fdc06df50e21 | -7.85913 | -61.1755 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77cbca17-cede-3087-a0b8-da45f93bdb40 | -11.19211 | -55.07561 | 2025-09-13 05:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df30d0fd-7068-32b8-8893-7d4461132d68 | -9.80764 | -61.51288 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e211a398-eb3c-3502-9300-84eef7619268 | -8.47052 | -47.2525 | 2025-09-13 05:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c3173171-c663-326e-bf0d-861cd0c12dd6 | -6.56745 | -50.87321 | 2025-09-13 05:25:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fff3be40-5d77-3213-8141-44b7f3241811 | -8.27787 | -64.05264 | 2025-09-13 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6c529e2d-c6a5-3732-8cea-2edcaa7fa5f5 | -11.18433 | -51.41439 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 7c9d49ca-8710-3768-aa6a-6ae6865fcc7c | -10.0941 | -59.16903 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 415ab6b3-00f4-3b18-94a1-ca2b046ada58 | -10.54248 | -57.0862 | 2025-09-13 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c464005-9841-35eb-b2b4-31e250642497 | -11.8386 | -50.55578 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 698a2531-605f-333e-8e40-cae752e9fa05 | -11.08269 | -51.42279 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 52ce499d-a4d3-38bf-8f2b-5dcf095773a3 | -11.87966 | -50.5751 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 2f933782-2d57-3d90-93f7-26490c718591 | -10.32971 | -48.82471 | 2025-09-13 05:25:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 386b53aa-8c1d-33de-9f4a-03d3b4a54969 | -7.76218 | -61.12426 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8b6b395-c8c4-3f37-a56b-1a8cfcf8b2a5 | -8.27003 | -64.05302 | 2025-09-13 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d39e16de-0b47-36a0-84e8-61c059092a4e | -10.26893 | -57.79768 | 2025-09-13 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54f3f092-0a69-3912-b774-b13bb233aab7 | -11.10463 | -51.44807 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c99b0fd-a82f-33e0-8583-b71e92e6d740 | -11.8264 | -50.55422 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d5c46172-bb40-3caa-93cf-7638f2cce599 | -11.18564 | -51.41021 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 833548ef-b0a5-3bf3-b3b9-a23e0b3bd5b4 | -9.23603 | -51.22895 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd642c87-029b-3aba-b819-1842dd01ab24 | -10.76948 | -50.51961 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5d2efe05-e3bf-3e8f-b78c-2d75e62548c5 | -10.01446 | -50.38853 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28dffb1f-0c32-3efc-92d5-ef21173d71f9 | -9.50596 | -55.96898 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eb91292d-e372-3b1d-8758-da32146f93e2 | -3.44369 | -59.57527 | 2025-09-13 05:25:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2675627c-ca1d-3a89-8333-76c0632c6d75 | -9.5065 | -55.96525 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b4a535d8-0a9b-3953-bf8b-69f46c8c1fe0 | -11.76739 | -51.50846 | 2025-09-13 05:25:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e061f522-d2f1-323f-aa45-2332b29470db | -9.16296 | -60.30166 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1246edca-fe2b-3d06-beb2-78a3970bff58 | -9.49828 | -55.96405 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |


[Clique aqui para ver as próximas entradas](README107.md)
