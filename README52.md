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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdaaa826-60c0-37a5-8f17-d504bc437f46 | -4.09886 | -51.10811 | 2024-10-06 03:53:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a434b469-3f51-345d-a07f-90432ce25ec4 | -4.09744 | -51.10323 | 2024-10-06 03:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0121b110-dc88-3e83-a474-a652dd2ff07b | -13.60789 | -48.13608 | 2024-10-06 03:55:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bb77fbd7-36e6-3351-a795-cd92b5741e79 | -14.0058 | -47.9323 | 2024-10-06 03:55:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9b37192-20ff-3192-b347-693c83bbd48a | -13.34018 | -49.32597 | 2024-10-06 03:55:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b01ad9dc-1321-3e11-a31f-f07a4f5b1c3e | -13.33957 | -49.32905 | 2024-10-06 03:55:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d00ce2e-b743-3c1b-8789-b63990ff9757 | -16.11782 | -50.46447 | 2024-10-06 03:55:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cf0833eb-330d-3d85-9ab2-a3342cab0d1b | -16.4262 | -49.92095 | 2024-10-06 03:55:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 570c5737-d003-3626-a3da-df2fcf3b71db | -16.42566 | -49.86482 | 2024-10-06 03:55:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cc360ad-b3b0-3f66-901b-417e3482aba5 | -16.42552 | -49.92437 | 2024-10-06 03:55:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75f23f2b-e8e7-3ded-b1fb-50c33ae22b10 | -16.425 | -49.86798 | 2024-10-06 03:55:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1fc02ee-9158-3b05-a6b3-87edec487bf4 | -16.42227 | -50.17575 | 2024-10-06 03:55:00 | NPP-375D | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06f155a7-630b-3b0d-8b59-dfcc077721f2 | -16.42154 | -50.17931 | 2024-10-06 03:55:00 | NPP-375D | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf41df3b-54bf-394c-a397-3d6da674c65a | -16.35327 | -49.92834 | 2024-10-06 03:55:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14cbba44-50a2-3f3a-b28b-a44ffd4e2db8 | -16.3526 | -49.93162 | 2024-10-06 03:55:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c93a915-8909-3cf7-a488-1e3d7be1701e | -16.12402 | -50.46215 | 2024-10-06 03:55:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 224d0f94-f8a5-39a3-b978-ca7ce00d856a | -16.11864 | -50.46052 | 2024-10-06 03:55:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb77f794-5bf2-3bc6-8f1f-bc79828bc8b8 | -13.99189 | -44.03464 | 2024-10-06 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46ae9010-028d-3840-a3fd-253232a74504 | -13.89625 | -44.59956 | 2024-10-06 03:55:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d294476f-54b8-3fcb-aeac-d208ea298be4 | -13.89535 | -44.60464 | 2024-10-06 03:55:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 46fa8e09-fc9a-352e-9df7-3c7c9582804a | -13.89444 | -44.60975 | 2024-10-06 03:55:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fce44550-d358-39a6-8593-1f5617996f6d | -13.89234 | -44.59883 | 2024-10-06 03:55:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0de04ebc-c08e-36e4-8d6c-03465addf7f3 | -13.89143 | -44.60394 | 2024-10-06 03:55:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d50cf68-fc1f-3138-8e73-7c6702e64bdb | -13.88451 | -44.59738 | 2024-10-06 03:55:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30d4b86c-bc93-39e0-bb09-4314520b9086 | -14.66043 | -41.96045 | 2024-10-06 03:55:00 | NPP-375D | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 88395015-5d62-3c0d-a399-7f3883bb95cb | -14.6598 | -41.96424 | 2024-10-06 03:55:00 | NPP-375D | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 929196ac-f869-39c1-9c82-8affd542935e | -14.65637 | -41.96368 | 2024-10-06 03:55:00 | NPP-375D | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ea3bce5c-a53a-306e-bae2-6ca6a11f85e3 | -14.39439 | -42.62109 | 2024-10-06 03:55:00 | NPP-375D | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4a60a8cc-5cdf-3e7f-beca-92e4add72e4a | -11.7335 | -44.50293 | 2024-10-06 03:55:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24309f4e-9975-3e0b-9ce1-b4f0b16b45a1 | -11.72482 | -44.50505 | 2024-10-06 03:55:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4378c44-6f8d-3184-a4ca-c55a2557ffa0 | -11.72418 | -44.50861 | 2024-10-06 03:55:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f28fe18a-ab61-3ce8-89db-418903c819ea | -12.0745 | -45.59903 | 2024-10-06 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc4788ca-1622-370d-aacd-32343c158231 | -16.1066 | -50.24138 | 2024-10-06 03:55:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5ad51ef-176e-3c73-a052-631baf401793 | -16.10587 | -50.24496 | 2024-10-06 03:55:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ee4dfa7-d625-3162-966b-bcbf18f703e2 | -16.10133 | -50.23956 | 2024-10-06 03:55:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f83186cf-bf95-3d2f-abc6-4cf85f1c2312 | -16.09673 | -50.2345 | 2024-10-06 03:55:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 968ca400-e595-335e-a97d-45164178a58f | -16.09142 | -50.2329 | 2024-10-06 03:55:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9f96981-626f-33c8-b3b3-8ebf1823e0cc | -16.07547 | -50.22816 | 2024-10-06 03:55:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9bc39a8-a809-36e4-b169-0b7b7e1bf72b | -16.0745 | -50.23288 | 2024-10-06 03:55:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a17c901f-d325-3331-8369-0cfa44d8705a | -15.75834 | -49.93648 | 2024-10-06 03:55:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8dfb7a6-ca82-33b8-9736-8d92b7e05139 | -15.753 | -49.93538 | 2024-10-06 03:55:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12e34b28-d531-3abe-bd79-f21fdcddf0ab | -16.08099 | -50.45092 | 2024-10-06 03:55:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e286df76-5888-32d9-b642-da2123c6ce32 | -16.08019 | -50.45485 | 2024-10-06 03:55:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 62fe37a4-6dd7-3086-bb67-4b6ca1fc2f39 | -16.07548 | -50.4499 | 2024-10-06 03:55:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1f1dcfa-9e9b-308c-88d8-ec77392d8a14 | -16.07471 | -50.4537 | 2024-10-06 03:55:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 18c28800-8b63-3d4d-85f6-17cb5f9a253d | -16.07075 | -50.44511 | 2024-10-06 03:55:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa81d3eb-942b-309c-a7d3-f30f57de0065 | -11.76789 | -37.65538 | 2024-10-06 03:55:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1626a902-5e41-36f3-9c32-aaca9156e439 | -12.7174 | -40.21476 | 2024-10-06 03:55:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 39757c59-2d78-34b2-ac6a-588ef297498b | -14.29631 | -44.65132 | 2024-10-06 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 843fa514-625e-303e-b009-1e4dfc92228d | -14.13572 | -44.72282 | 2024-10-06 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29f97f5b-b710-3bd8-8c2e-d51bad8bda05 | -17.76254 | -39.79794 | 2024-10-06 03:55:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9a25f806-fbcc-36fc-bad8-a7c8bb591d64 | -13.8836 | -44.60252 | 2024-10-06 03:55:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2594c8b-13aa-3897-884c-e15c00ba965b | -18.03977 | -39.92624 | 2024-10-06 03:55:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 34065f5b-8e02-3f15-a983-775f601ab672 | -12.71683 | -40.21832 | 2024-10-06 03:55:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2cb04149-c057-3087-a67a-d7f005ed96c9 | -12.71407 | -40.21422 | 2024-10-06 03:55:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f335d31a-6b57-3199-8ea4-8e886f662b59 | -12.7135 | -40.21777 | 2024-10-06 03:55:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 04ca046b-73af-3da1-980d-2c59458ee5c0 | -12.71017 | -40.21722 | 2024-10-06 03:55:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b2c40672-2271-3751-92cd-77c5ef762fbf | -13.29275 | -39.91567 | 2024-10-06 03:55:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5ce72ea4-2c3a-327c-ac20-7f88d98562b6 | -18.32635 | -41.44714 | 2024-10-06 03:55:00 | NPP-375D | PESCADOR | MINAS GERAIS | Brasil | 3150000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 424bb1b5-894f-31cd-b46a-2cae0aa506a1 | -18.3236 | -41.44291 | 2024-10-06 03:55:00 | NPP-375D | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 0fda0ade-ae61-3561-9b08-4c87d05d8286 | -12.25759 | -41.09913 | 2024-10-06 03:55:00 | NPP-375D | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c164c09d-1c7f-3e4c-8439-75efe7f7c4d0 | -12.2542 | -41.09856 | 2024-10-06 03:55:00 | NPP-375D | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 0ce31ab3-f29a-3d31-baa5-ac5f40e3e821 | -12.25081 | -41.09799 | 2024-10-06 03:55:00 | NPP-375D | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 62eb58ad-7be8-3a16-ba51-cf2db4bfbb13 | -11.98998 | -41.34836 | 2024-10-06 03:55:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 974cbc15-6502-3645-9810-e50765cbbb1c | -13.50185 | -41.37646 | 2024-10-06 03:55:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 48305a81-9126-3f7d-bbe0-8f9ce86e656a | -13.05016 | -40.52164 | 2024-10-06 03:55:00 | NPP-375D | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aaf6400e-e913-3944-bcad-ea11117728a7 | -13.04624 | -40.52467 | 2024-10-06 03:55:00 | NPP-375D | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 98bdf88f-c43a-3971-83c2-c644318e0568 | -17.3809 | -42.65457 | 2024-10-06 03:55:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 980496f6-a79d-3ee6-afeb-83b85a8fb90f | -10.76682 | -42.68782 | 2024-10-06 03:55:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b3d9f7ce-0484-3c87-9874-5e8fbc2bb0b4 | -11.3407 | -41.93755 | 2024-10-06 03:55:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bff5c2f8-2473-3227-9b02-af4a4db677f6 | -11.30248 | -42.08011 | 2024-10-06 03:55:00 | NPP-375D | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 50f4370b-5b64-3f51-9e3a-5bfbd186cc1f | -10.82839 | -42.69742 | 2024-10-06 03:55:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 88fe2152-427f-3d32-82c1-d1b2cbc29348 | -10.84052 | -42.84872 | 2024-10-06 03:55:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 682e3c2f-66b0-37df-a0c6-f424af7d96b2 | -10.83977 | -42.85315 | 2024-10-06 03:55:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db447dab-a683-3a18-9a26-bc75de72479d | -10.83901 | -42.85758 | 2024-10-06 03:55:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22a4b316-7912-38ef-b6e7-8d8ffa7c43a5 | -10.83161 | -42.8563 | 2024-10-06 03:55:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a58b96d0-301e-3ed7-aaaa-2749b09238ab | -13.09117 | -42.42135 | 2024-10-06 03:55:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 33e0ee66-cdcc-35ee-97b9-6c009664aeae | -13.08764 | -42.42074 | 2024-10-06 03:55:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 28f50c3f-3f56-3fb5-a547-baa8bfb0755c | -16.48393 | -43.8158 | 2024-10-06 03:55:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c71e3838-0802-33a1-a06f-6a9a59d87e2e | -16.48318 | -43.81722 | 2024-10-06 03:55:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6398195-d2d4-3826-b76d-b192c06331a9 | -16.34721 | -43.69648 | 2024-10-06 03:55:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f52e4d3-33e7-3564-9bf1-aeea1bd97d70 | -16.29606 | -43.69128 | 2024-10-06 03:55:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffac1364-44f8-30d9-ace1-d7918bfef355 | -16.29498 | -43.69283 | 2024-10-06 03:55:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 257165d9-02da-3173-b7b1-6772e2f144e1 | -17.64184 | -44.40341 | 2024-10-06 03:55:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f84f137-eaf9-3793-9726-28bffa2ed867 | -17.64106 | -44.4079 | 2024-10-06 03:55:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08b739c2-8500-3ce6-87fe-fa2d528d1d2f | -17.63582 | -44.41611 | 2024-10-06 03:55:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9dd03b9d-37c5-3418-a6fe-650227fb7f0e | -17.63506 | -44.42051 | 2024-10-06 03:55:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f30739e-6845-330f-88d8-e5fdfbe02b58 | -17.6345 | -44.40208 | 2024-10-06 03:55:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3883f1e-f3d7-345f-bc9b-3473ae71d6df | -17.63371 | -44.40659 | 2024-10-06 03:55:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b42010f9-fa37-3c98-8687-1f685def5e54 | -17.63215 | -44.41545 | 2024-10-06 03:55:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30b47f9c-5912-3506-a941-81319dd50aa7 | -17.63138 | -44.41986 | 2024-10-06 03:55:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 765318ca-13eb-31f5-9389-a949cb4506d1 | -17.62034 | -44.41793 | 2024-10-06 03:55:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d5529e7a-5e4b-33a7-b414-f22d11707350 | -17.61745 | -44.41282 | 2024-10-06 03:55:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 524e6f5d-7dad-3804-9af6-16320d9ba9ac | -17.61666 | -44.41728 | 2024-10-06 03:55:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 82a95ec9-7842-3c17-b65c-549c98fd0aef | -17.61587 | -44.42175 | 2024-10-06 03:55:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0fbc4f70-e5ce-3eea-ad32-a6685ac1def4 | -17.61509 | -44.4262 | 2024-10-06 03:55:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 841532e1-4324-3987-a149-cc434a549402 | -17.61377 | -44.41216 | 2024-10-06 03:55:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbf86201-064c-39fc-acfc-b79040790739 | -16.68143 | -43.88242 | 2024-10-06 03:55:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87df5600-6ce3-3b74-9941-9f0f479b5146 | -11.72355 | -44.51218 | 2024-10-06 03:55:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2626bd3-72d3-39c1-8f21-cf8ca465ff75 | -11.72079 | -44.50432 | 2024-10-06 03:55:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README53.md)
