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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 220815b3-2b29-3b69-8d7b-ef946175a852 | -17.0592 | -56.09143 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| fcacf35e-d091-31b0-8cf4-aef674b04a27 | -17.05857 | -56.09599 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a9e1cd50-11de-3bf1-a588-a1996fdc66f1 | -17.05549 | -56.09087 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fb6faf0b-f8d5-34d3-9209-b440b3903fac | -17.05486 | -56.09542 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b1b22c44-1e6b-351e-b13a-f381837a4ea5 | -16.97778 | -56.22903 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5dc80445-d33b-3690-9de9-c4dc4e332d95 | -16.9502 | -56.21118 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 5f1da4ca-a09c-3bd0-a913-a391679de867 | -16.94921 | -56.10987 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1565c996-b2d3-3948-96b3-f1b89dbd69ed | -16.94284 | -56.21007 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6f332092-a55e-376f-b197-c8aa1ac9fd3f | -16.93916 | -56.20951 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 561cd8e6-6a8b-3536-abed-d55a7305eb63 | -16.83779 | -56.08075 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e73aef2c-ea5f-3309-a942-580d14ae5869 | -16.6957 | -55.88258 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4e00b9f9-8396-3b79-850e-e9c30b81a687 | -16.68053 | -55.9366 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8ad9caab-19ca-3d67-82b9-89a3709415f6 | -16.67617 | -55.94062 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e5f888cb-b607-391f-a7be-25532139cbba | -16.67308 | -55.93547 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4e532919-293d-37f2-a54d-a64620534cf6 | -16.67244 | -55.94006 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a4c1d101-33d4-39f5-9a1d-0c9cea86003f | -16.66691 | -55.92518 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a6fc3a8d-98b9-3173-8934-5978de797296 | -16.66318 | -55.92462 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e950f0a7-aac9-36a7-a028-86e22a23a6ce | -16.65882 | -55.92864 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| db9f0593-b6db-385f-8986-34a49c16f398 | -16.64518 | -55.91724 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c28ae6d7-b590-38fd-90e1-a16badd4d4d0 | -16.64392 | -55.92641 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| db50357e-73d3-3fa4-a739-8785e0a7bde0 | -16.63893 | -55.93501 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0d57eee9-416b-33a3-a461-976f5fbab7c9 | -16.6383 | -55.93958 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 06cd2639-ddd8-3137-a0e2-508d359d5abd | -16.63709 | -55.92071 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1c589107-add4-38c0-bfea-7cc12d8ed546 | -16.63647 | -55.92529 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cb029296-18e5-33dd-8f84-35d60af8b61a | -16.63458 | -55.93902 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 57372e8a-7f24-3586-a81f-599c66b739f5 | -16.62403 | -55.93277 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a82bf8b5-dcb9-3c27-8634-b6890c7306ed | -16.61773 | -56.03399 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5f468397-31d2-33f7-857d-4d774e26e861 | -16.61659 | -55.93164 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6cd65b1a-697e-387c-a40d-bb3182c6dc8c | -16.61596 | -55.93622 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d60b2fe0-d911-3727-9f0c-95ddd33c7f96 | -16.6159 | -55.92953 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b968f008-2e3a-3fc4-b8b7-9920462f2897 | -16.61402 | -56.03343 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c5a4cd34-b31b-3a87-ba8c-f791c8382e7e | -16.6134 | -56.03795 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6e583fd5-d1db-32e7-a2a2-06d0a931ea52 | -16.61286 | -55.93108 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5b95907b-9f21-37e1-bcf0-41a284f6a0c0 | -16.61224 | -55.93566 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fcc2629f-12ba-3915-876e-6ab2dae8cf95 | -16.61221 | -55.9915 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3333a326-822f-3525-bae4-23729f6dcb84 | -16.61158 | -55.99604 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 30c0b826-ffc2-366f-86af-4a13197bdb06 | -16.61153 | -55.93355 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 83f82dd0-59eb-36aa-8287-c840f94ebf42 | -16.61032 | -56.03288 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| cd70e684-5d7a-3358-87b3-67de80f3dad2 | -16.60914 | -55.93052 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3103325e-d589-3387-bd77-7c241dc95451 | -16.60852 | -55.9351 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9229dafc-4769-3bc4-b25f-02f26c16af6d | -16.60781 | -55.93299 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cac6eb96-9b61-3c20-9611-05e9d192fca8 | -16.60716 | -55.93756 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 4472c2f9-3ad9-30c5-8f21-7f92417e48a4 | -16.60662 | -56.03231 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5e35d971-9ded-3fd2-b43f-89bcfd1cb988 | -16.606 | -56.03684 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| fbc7455c-da4e-3130-ac4a-acb6c1d8ebd1 | -16.60542 | -55.92995 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 68cd5aea-6ac6-36cb-9665-9168ced15613 | -16.60538 | -56.04136 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d1214f30-e994-3e9a-becf-d4ee8dc57f00 | -16.60169 | -55.98528 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 5c2e25e5-b339-3e1a-ab0b-0e3c9724e8de | -16.60069 | -55.98309 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a9331fe1-9069-3d07-ab4d-60a15f21e31a | -16.60045 | -55.99437 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| e304aacd-28f8-3d2c-a948-f1a7660361cc | -16.60044 | -56.04982 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0e8e20c1-51ae-34b3-8d3a-c62a7dfa66d4 | -16.59983 | -55.99891 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0027e28d-7808-3bbc-831f-0e70584f70a1 | -16.59844 | -56.05204 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0a76a07c-c440-352f-be43-d10aa59090a9 | -16.59674 | -56.04927 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3a616795-63ee-3d14-83e3-05e7245bf3eb | -16.59474 | -56.05149 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e91f2e7c-cf59-3b29-be17-e0fa63c1df87 | -16.59168 | -56.04643 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0b8b707d-3b22-3488-92cf-41d367937b4b | -16.59104 | -56.05094 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c68f7f40-ab5a-3b5c-94fc-5065a718b59e | -16.61901 | -55.99716 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 2095d361-0ead-3838-8039-67c236540404 | -16.61721 | -55.92706 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0095f70f-4b04-3e5a-806a-ed658b3b3d36 | -16.61592 | -55.99205 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3fcc7a56-1931-3a5e-a792-f58616c2c568 | -16.61278 | -56.04247 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5769824a-36ab-338c-9967-00570fe4e565 | -16.61218 | -55.92898 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2e00777c-958b-367f-bdcc-715f7ed0ff45 | -16.60908 | -56.04191 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 826a6606-8bf5-3adb-a271-8dbe50e49d5f | -16.60846 | -56.04643 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| f898a5fa-2803-360f-a207-8ef0f693caae | -16.60473 | -55.92785 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9a0b1981-bcc0-3454-9d3c-f61541afd1a4 | -16.60376 | -55.98818 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| bab9a953-82f6-3212-b4ac-19789625af3f | -16.60311 | -55.99272 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| a7b4bc4a-1751-3a88-9e6d-a2efc0fd1ffc | -16.60291 | -56.03175 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 300b3249-eeeb-3e45-9c4c-5678ff8000be | -16.60229 | -56.03628 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7c55526f-0248-3854-a302-29425623ab5a | -16.60107 | -55.98982 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 351aaa3f-79bb-3ded-8848-72512f7b11fc | -16.60037 | -56.03852 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 4e512419-9654-3054-8b34-0bf638f07391 | -16.59908 | -56.04754 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 37f21af5-ae08-393f-b8fb-89da06265c4a | -16.59859 | -56.03572 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6de4c482-477b-3b53-93c7-42b598aea139 | -16.59797 | -56.04024 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 44fd5b7c-7454-3c0a-821a-d568702d93cf | -16.59674 | -55.9938 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 6204691c-3007-3652-a6ca-4a8a29c303e0 | -16.59538 | -56.04699 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6fba27bd-53cc-3c3e-8f9b-88b768f22bd6 | -16.59304 | -56.04871 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 09d11453-2951-3740-b74b-4ff30acb7783 | -16.58934 | -56.04816 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 6ef9cc72-ada6-3789-ab88-18e1d705a9ca | -16.84561 | -55.82866 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 780f70c3-6b82-3372-8961-bc3097796f81 | -16.84554 | -55.88557 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c8451087-c254-3fa8-b354-a681a9d5eacd | -16.84365 | -55.89946 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f6754cfb-233d-30db-ab5f-e492536c3b05 | -16.84302 | -55.9041 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8c5ebc4b-f42a-3bf6-979d-c3b7ac87bef1 | -16.84239 | -55.90871 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d82ecc55-cffb-3b0a-bc14-4732ef07fa91 | -16.84176 | -55.91333 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 595b96a0-df1b-3782-ac99-92d9c7694084 | -16.84117 | -55.88965 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cb13c762-3c17-3f49-9db3-c4aa6e5955e3 | -16.83999 | -55.81351 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1acdb870-eb67-3e28-9dde-c630aef2a6a1 | -16.83995 | -55.86855 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1c524497-dfd7-3a7b-9663-38a2c0d3884d | -16.83967 | -55.8163 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e3d2b291-a4cb-3f44-a2bb-511912d0bc07 | -16.83928 | -55.90354 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 680f6ad7-8354-3518-ae1c-cac3bbea8a9e | -16.83798 | -55.88246 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 601c4146-f655-3ec9-a3c2-0a2252de6f0d | -16.83733 | -55.88709 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| cd0f538d-b88d-37e3-a65e-8c3a2ca32cea | -16.83592 | -55.81574 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e06060ed-6651-3a05-a29f-a7d4a50114db | -16.83557 | -55.87462 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 19468417-af01-3331-b688-e147380a5243 | -16.83536 | -55.90095 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 913fd455-0e7b-3b1e-b6ee-f95cac7234e1 | -16.83494 | -55.87926 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a3bdcb78-de23-37e5-af5a-6f217d1a982a | -16.8349 | -55.87727 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| bf3fafa4-df9c-3d0d-945f-fc0edb7fd3cc | -16.83405 | -55.91019 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| bc6f4c4a-278c-3ad7-a038-05b40642f4d6 | -16.83368 | -55.88853 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 6bedd46d-15a8-36bc-830d-59cb18a061a6 | -16.83359 | -55.88654 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b4d6877f-de1a-38de-9258-977112e532a8 | -16.83306 | -55.89317 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 3a975fc4-0429-3ab8-87d6-10df06245d82 | -16.83293 | -55.89116 | 2024-10-02 05:12:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |


[Clique aqui para ver as próximas entradas](README144.md)
