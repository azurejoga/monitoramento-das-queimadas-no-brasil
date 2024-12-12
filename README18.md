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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd27e512-98bd-3946-b987-4d981a4ecb25 | -5.9355 | -48.05402 | 2024-12-12 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e4dff51f-bae6-3880-9bca-a42998ad3619 | -8.40156 | -49.17653 | 2024-12-12 04:16:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae8d9dce-0533-3df8-85a4-f5c4b09eabf4 | -6.93582 | -43.54111 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf3945d6-3fb4-3184-865e-711ee1c86614 | -8.30961 | -55.10896 | 2024-12-12 04:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 054d03dd-baf3-3b3e-a61f-d34942aa4ccf | -10.54235 | -44.68459 | 2024-12-12 04:16:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 100484c1-5e6c-3cf3-8ace-5dc02ff24701 | -12.40809 | -49.68145 | 2024-12-12 04:16:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 788cb403-685a-31a7-b6d9-05e93be2b365 | -7.42509 | -44.73577 | 2024-12-12 04:16:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92dcc8a4-62aa-338c-ba18-5bed6e23629e | -11.20024 | -53.83324 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 146b434f-b6e7-35f8-9127-6e15710cd4f0 | -12.07523 | -48.3991 | 2024-12-12 04:16:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b484062-7b6a-34e1-a3c8-4fa6b6e43cfa | -11.75449 | -41.14075 | 2024-12-12 04:16:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6765c8df-8d56-3154-a069-bf53653ad7f5 | -6.94243 | -43.54214 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 710839d5-4111-3b35-bb4d-8520002b29cd | -12.65446 | -43.97954 | 2024-12-12 04:16:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 661005ee-4867-32a9-b042-be906bf00cc1 | -9.19441 | -49.47796 | 2024-12-12 04:16:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 37ad833b-a4d4-3cc9-ad48-67e8659120f7 | -14.05416 | -43.30493 | 2024-12-12 04:16:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 66f954d1-d2b2-3b92-b93e-b324dffef4b1 | -11.69047 | -48.07836 | 2024-12-12 04:16:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 803dfaa9-44d0-3039-89e9-b39f9a6d2a49 | -6.92915 | -43.51882 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 89e11156-ad0b-3e8f-a417-41ff465d3d24 | -15.06797 | -59.65625 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c6f88e1f-caf6-3af3-aec4-6a755f5ff2c1 | -13.69516 | -54.76051 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 28f29e66-129d-38d5-8186-2fd9b76e09db | -15.07777 | -59.62526 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 04b2316b-ce1a-3d89-bcbb-2be5e37572ef | -12.91829 | -55.05023 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 14ec0d04-aeef-3f70-9a6d-2b3067d7ca5c | -18.05612 | -52.98983 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f2e1b755-88af-33f7-9e63-927d473e5a3d | -18.06412 | -52.97226 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b8f2cf03-8c73-3872-96aa-fe2a0b929ce5 | -15.07987 | -59.63654 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3c9eeef7-7fe5-3ffe-a61f-a8a29350ff65 | -12.5341 | -57.73585 | 2024-12-12 04:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 40abca4d-7c32-305b-ba91-1238b8a100b9 | -18.05165 | -52.98892 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 857b262a-80bf-33df-98ca-dbb2677bf503 | -18.0579 | -52.98057 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0695a907-4944-37a0-bd7a-def6fc019a28 | -18.05435 | -52.97496 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72efe745-ded6-374a-b9c1-adbd59e37358 | -15.09407 | -59.65164 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2f7f0fb0-1202-3729-bb2c-ae974cc27567 | -18.04988 | -52.99815 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e746f6b9-104d-3282-a7c3-a59e5a9edb40 | -15.09024 | -59.63555 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5bad66b0-8bf3-3983-a9d6-1a2456b0c490 | -13.69448 | -54.76398 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9a711d0c-3ec1-39d8-8443-e399fd79e1b5 | -18.04541 | -52.99724 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d98a8fb1-94c3-3845-a4c7-feb77885b0f2 | -12.54185 | -57.73176 | 2024-12-12 04:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a378f1ab-a16b-3e60-ac0d-431bcd3aebe5 | -14.7477 | -52.64803 | 2024-12-12 04:18:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a6d271cf-d398-35ac-a8e7-64134087b254 | -18.05255 | -52.98427 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9b1b72c1-0ddc-3eed-ae1d-18135f98c0c1 | -19.07363 | -47.52851 | 2024-12-12 04:18:00 | NOAA-21 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4257de34-2d61-3ae1-a90c-166cffe3858d | -12.56688 | -57.76325 | 2024-12-12 04:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| ce79391d-aa52-3cbe-aa9d-0ee6ea6728df | -13.70057 | -54.76164 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 031396b7-b428-3a53-87a1-04788ee11299 | -15.0815 | -59.62939 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 37bc5212-37a0-3527-b523-343f32d383dc | -13.06262 | -52.04268 | 2024-12-12 04:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1883b4c2-7f26-3e53-8987-25875004a460 | -14.74583 | -52.65797 | 2024-12-12 04:18:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 559fba9c-fd25-3fd4-b149-a427db1b4845 | -12.56224 | -57.76665 | 2024-12-12 04:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2533e29c-250b-3630-8a20-1a910bd5909e | -15.08865 | -59.64274 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f17cf3da-fe2f-37e9-85ea-da87dd402bac | -14.75046 | -52.65893 | 2024-12-12 04:18:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a40c03cf-1a91-3013-9989-d61237c90265 | -18.0472 | -52.98799 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c2ef5b58-45ee-3f66-ad8e-da44f4d004c4 | -12.54067 | -57.73746 | 2024-12-12 04:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 5b04f2ab-cd9f-35b8-9647-acf81bd2aaa4 | -17.74507 | -56.32515 | 2024-12-12 04:18:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ad495c17-9c52-389a-aca9-4e6e5b10ef46 | -12.92042 | -55.05095 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3bcf760-697c-342b-a9e1-5abd9dc5c199 | -12.57348 | -57.76469 | 2024-12-12 04:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3f53cd8c-996f-33d0-97e6-0528c1de3d6b | -12.92116 | -55.04712 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3acf6621-c05f-33c0-b05b-5b6a30196c67 | -15.08166 | -59.64101 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2fcf4904-41e9-3141-bfb2-f271c9835067 | -15.08689 | -59.63814 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85ebdab3-a7a1-3f58-acfd-cc58f161fedd | -15.08483 | -59.62671 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 07eccad6-f72c-3001-b2e4-7a5b7708ac60 | -12.56887 | -57.76802 | 2024-12-12 04:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| fc4fdce4-ee1e-36ee-9c13-00ae2b6d1a03 | -15.08325 | -59.63383 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 82231b50-6db1-3983-b30b-7c86fd94bcd8 | -18.06679 | -52.95836 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 355a466a-79e2-3d3d-89a2-cc55ab2e8e9e | -15.07825 | -59.64362 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 11d6741d-9da0-3236-95d5-77e7cf49dd82 | -15.08308 | -59.62249 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d7335929-1c8a-354e-b76d-6183269a1e1e | -18.05879 | -52.97593 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f6c397fd-cd42-3940-be86-c671d8cfd8db | -18.03205 | -52.9944 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7ad9ea3-b402-32cf-8541-7315a0b257f4 | -18.07123 | -52.95933 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a589e115-ec15-3070-b77f-b14a68cba2bd | -14.7514 | -52.65392 | 2024-12-12 04:18:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0578a587-6d57-31c6-8f7c-b0f13124bd2a | -13.65436 | -52.93789 | 2024-12-12 04:18:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86d04744-03d4-3494-9184-2240de4257af | -13.69989 | -54.7651 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9d153476-d9e7-3541-a7a5-f7bfa1d89550 | -14.74676 | -52.65301 | 2024-12-12 04:18:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2eeac04a-6c69-3ac3-83fa-323f5241c599 | -18.04095 | -52.99633 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a789d095-56bc-3d64-ace3-96e8fdf3f319 | -18.06681 | -52.98238 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2cdd6a9c-24f4-3d28-b341-dbfdfaa67025 | -18.06236 | -52.95739 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 303b5c44-07c7-3be7-8ebf-cd21b47c2205 | -13.07363 | -52.03461 | 2024-12-12 04:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 188bb341-ff52-3f9d-9b67-ada0ecb4b7d1 | -18.05968 | -52.9713 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| da7c9737-704f-3074-907b-dbb470de43f5 | -18.07035 | -52.96393 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31c87069-00f2-3219-9310-ef69b9e73fc5 | -15.09225 | -59.64703 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28d608c5-1def-32ce-9552-ef522aa492b6 | -14.74864 | -52.64306 | 2024-12-12 04:18:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3783f75e-6e6c-322b-87cc-fa9fe2e23d63 | -15.07664 | -59.65068 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 05e429a0-340c-3c10-9975-95d1f209f25f | -12.91481 | -55.04988 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8ec40dc-4502-3d59-bf38-3eca3e490184 | -18.06057 | -52.96666 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8a39038d-1ecd-3d52-a2f6-c9368250da55 | -18.06323 | -52.97688 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 278e896d-c93e-3a12-81ff-f209377515c2 | -18.06235 | -52.9815 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| aba345de-1c32-30f0-a6f1-639f2e32a26c | -14.75698 | -52.64977 | 2024-12-12 04:18:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b3616975-0a3d-3454-af28-5dec9ec52278 | -12.91752 | -55.05409 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe9623a5-0f59-36d0-888e-e9869191dd78 | -18.05077 | -52.99353 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d5e01865-2d95-3714-ad60-89a96d14d9b2 | -15.07149 | -59.65355 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| db7501f5-3069-3fd9-a000-96f7bba64289 | -15.08707 | -59.64991 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e388dc7b-fac0-3664-a370-a7d1552f216b | -15.06444 | -59.65205 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4a6c43b1-27a0-3db3-b036-13583db7b0e9 | -13.06722 | -52.04351 | 2024-12-12 04:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27cbdc53-bcdb-3c05-9075-633072514116 | -12.91923 | -55.73188 | 2024-12-12 04:18:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a9ab3f55-e624-38e1-b48d-1b6ae014bd1e | -18.04631 | -52.99262 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 92e019c4-9c3b-35be-8c21-e04b07c6fcce | -18.06858 | -52.97315 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af23f1ee-f711-3cf3-bf4c-d0ed4192cf61 | -18.0659 | -52.96299 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 693840bc-60f1-388c-8e0a-147f4f063052 | -15.08525 | -59.64531 | 2024-12-12 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6082b66f-7c83-3590-91ef-396ab859669c | -18.05881 | -52.95181 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79ba9e2b-916e-3621-a6fd-98ce60de9605 | -18.05345 | -52.97962 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82d46108-032e-3743-8453-815cb3c750bc | -14.75605 | -52.65475 | 2024-12-12 04:18:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4a7c96b6-4150-3480-8769-dded7ae39477 | -14.65986 | -50.33022 | 2024-12-12 04:18:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4ef7fa76-cde3-38d7-9b14-9a9d889ff434 | -18.057 | -52.9852 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1b804b17-7e02-3976-a1c7-8c0b68de5689 | -12.91892 | -55.05873 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94809fe1-ee31-3292-be0c-cde5dca88600 | -18.05523 | -52.99443 | 2024-12-12 04:18:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 193e474d-d380-3ce5-b192-7c7bdc628c94 | -12.56566 | -57.76898 | 2024-12-12 04:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 96d8ca4f-01fb-3641-bd0f-16827b71bfee | -13.68838 | -54.76636 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 400b262b-2302-317d-bd6a-a94fe0e5088a | -12.91673 | -55.05799 | 2024-12-12 04:18:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README19.md)
