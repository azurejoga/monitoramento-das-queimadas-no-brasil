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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8abd1ae5-f22e-3d13-a000-186f4f124942 | -12.00941 | -42.95049 | 2024-10-29 03:23:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fccb5d37-fd41-3396-a810-770123d855b7 | -12.00337 | -42.94926 | 2024-10-29 03:23:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 77107b18-616c-318f-a2b2-24dc7f10c591 | -11.28808 | -41.86 | 2024-10-29 03:23:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7dd83e07-c71f-3ce1-b264-1740acd63029 | -11.28728 | -41.86412 | 2024-10-29 03:23:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 44a3f616-b2d3-3603-abde-f2482f33f7c0 | -13.24761 | -42.80334 | 2024-10-29 03:23:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d53e0d45-e356-3866-af8d-1ce678c676a8 | -13.55848 | -43.42035 | 2024-10-29 03:23:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf244c48-0727-3f3c-af09-aa6a8f0d0327 | -13.55244 | -43.41903 | 2024-10-29 03:23:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 042aefa3-8838-3c62-af56-f7891a59e62b | -14.47828 | -43.35974 | 2024-10-29 03:23:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| baadb6eb-9e8e-3eda-86d1-b2088ec6892c | -14.47596 | -43.36015 | 2024-10-29 03:23:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 74f2085c-7131-3a8c-a07a-f96fcc9a0d1b | -8.7197 | -44.01723 | 2024-10-29 03:23:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cf376a2-e977-325a-9c78-43bb8094b8d6 | -8.71841 | -44.02386 | 2024-10-29 03:23:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 354fe6bc-8a9f-3dc2-b7f1-c3f505079194 | -11.105 | -43.33789 | 2024-10-29 03:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| a9056dad-4a9c-3192-bec4-610a8b01e2b8 | -11.104 | -43.3429 | 2024-10-29 03:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| e4871e54-4b5c-3813-97ff-1c9149424841 | -11.90854 | -43.81248 | 2024-10-29 03:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2eefa3c9-5a3f-3a16-a1f1-aa94c89f2315 | -11.90743 | -43.81782 | 2024-10-29 03:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff087033-dfa9-300d-8798-f77c67797474 | -11.54359 | -43.98509 | 2024-10-29 03:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30ffdd6a-6554-3733-b932-fa8403735d57 | -11.53712 | -43.98372 | 2024-10-29 03:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ce27b080-7dd6-364d-aeb7-cd1eed3ba208 | -13.30486 | -43.57709 | 2024-10-29 03:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d117071e-ab4a-38e4-8334-b6f317c1cc74 | -13.29874 | -43.57573 | 2024-10-29 03:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 683e1979-a693-3d5f-adde-ad56bf758238 | -12.88786 | -44.61722 | 2024-10-29 03:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08cd914a-2432-37ea-a37c-92a33098b787 | -12.88668 | -44.62288 | 2024-10-29 03:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 669e0e5e-e63a-3ed5-bb7b-4636092e32e9 | -12.879 | -44.62679 | 2024-10-29 03:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 66786c1c-0ee6-3ea3-a5c0-d25d09e468dc | -12.87121 | -44.63119 | 2024-10-29 03:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| efee7193-1cd7-3659-adec-fba8a59c3ba0 | -12.86997 | -44.6371 | 2024-10-29 03:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c629c1ac-515a-3258-a27c-ff2edeab8bc3 | -12.6692 | -43.82172 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b587a2ab-41e5-3fbc-9065-95bebfd4a954 | -12.66816 | -43.82687 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1429258e-9ced-3780-968f-b27f98891117 | -12.66588 | -43.81628 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 37e59856-74d5-3665-a800-d2c474519c70 | -12.6648 | -43.82143 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d62a3f85-f979-3c02-9a92-832ba6291a16 | -12.66395 | -43.8152 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1df01315-538a-3aab-8d11-d9049c43fb92 | -12.66373 | -43.82657 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d8c51a88-0bd7-31fd-9ac5-6093cd4a1911 | -12.66291 | -43.82037 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3ea79d92-3600-325f-a79e-361b18ad6e0e | -12.66187 | -43.82552 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1653f840-0abd-3a9e-8720-b44137704c5c | -12.65852 | -43.82008 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2dc30d8-904b-3b31-b1c5-bed79cb80d9c | -12.65744 | -43.82522 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 624bad18-b292-32f6-94f3-fd9a764ee32d | -12.49516 | -43.79269 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a9b4211-5b42-3ea2-9292-70ac24bb4c6d | -12.4941 | -43.79786 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b055a482-a240-3b14-a91d-db905c79bc52 | -12.44195 | -43.73271 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 094b5eec-ad32-3239-a62b-491e5662d795 | -12.44088 | -43.73779 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 552f9f25-83d6-3985-982f-80181f1d8f75 | -12.43948 | -43.73414 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a55fbe86-ed41-36e2-975c-fafb36178cb5 | -12.43845 | -43.73925 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9faafdd7-4373-3ecc-bae3-9e82f0f42179 | -12.43322 | -43.7327 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cd17602b-d902-3f1a-83e6-6397c1cfca24 | -12.43217 | -43.73787 | 2024-10-29 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b931f15b-dd0c-3258-9918-fecb03ffe4b9 | -12.2302 | -44.68886 | 2024-10-29 03:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4902e621-0f4a-3d27-ab01-df50cc3f0b02 | -12.2248 | -44.68133 | 2024-10-29 03:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ade1f851-f740-3bcd-ad8b-5a32da2bc620 | -12.22359 | -44.68717 | 2024-10-29 03:23:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c928a11-d04d-31cc-8319-5a1f8dbad38a | -14.5962 | -44.26198 | 2024-10-29 03:23:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a5bed930-cbe5-33aa-a980-2a49cd2bcd45 | -14.59513 | -44.26688 | 2024-10-29 03:23:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 307ab5b8-9087-398a-8871-addad49d7873 | -14.59244 | -44.26429 | 2024-10-29 03:23:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aefa0e89-3dd5-3cb8-8efc-646d4c470fd5 | -14.58901 | -44.26497 | 2024-10-29 03:23:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a3684bb-1156-3ab0-83c6-87c8cfdf7275 | -14.16667 | -44.66064 | 2024-10-29 03:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4edbe2ba-3ea4-3035-ab35-4ff4d668514f | -14.1491 | -44.07804 | 2024-10-29 03:23:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 22a96954-8afb-3349-b0dc-a0fa69eae416 | -14.14804 | -44.08308 | 2024-10-29 03:23:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| eb410495-a5ee-35d1-a35e-8bdfa2d263f0 | -14.1429 | -44.07661 | 2024-10-29 03:23:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 688fce06-8545-3a66-a1f7-016aceb34a91 | -14.14182 | -44.08168 | 2024-10-29 03:23:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c98fa1b8-1aa0-3bbc-b281-f50ced1db5cc | -14.12952 | -44.35779 | 2024-10-29 03:23:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 62292d3b-a39e-3a1c-9cd5-cfd23be21041 | -14.12842 | -44.363 | 2024-10-29 03:23:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| acc52ca3-7a59-3e93-a5e4-119120fffde6 | -13.88709 | -43.97556 | 2024-10-29 03:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3f9e2b01-d961-33b5-8e7c-8c376a4098c5 | -13.85914 | -43.98494 | 2024-10-29 03:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a859af53-ffd0-3967-be8d-b4b132c353f8 | -13.85809 | -43.98994 | 2024-10-29 03:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 05ca1449-a62a-3cb1-8811-08e01e0a1efc | -13.85293 | -43.98354 | 2024-10-29 03:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c74758a7-b4d4-35ec-bc6d-4763358875fd | -9.44601 | -44.4803 | 2024-10-29 03:23:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b62effc6-6fbe-303b-a3a3-71164c223d51 | -9.44466 | -44.48725 | 2024-10-29 03:23:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66f6d646-fb93-3aa8-97c3-7956242a4352 | -9.12274 | -44.42121 | 2024-10-29 03:23:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a075ed0a-2039-3bbc-bf4c-2d412b9df5df | -9.12145 | -44.42759 | 2024-10-29 03:23:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce26c122-3a1b-309d-a129-9b9262210781 | -8.76438 | -44.72485 | 2024-10-29 03:23:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebdcb1e1-b906-377a-89d5-128e96c91b54 | -8.76015 | -44.70924 | 2024-10-29 03:23:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| febfe162-3613-3b66-be8d-964a9329842b | -8.75873 | -44.71631 | 2024-10-29 03:23:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 176e6961-b88f-3d3f-988d-d466c5678edd | -8.75631 | -44.70875 | 2024-10-29 03:23:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b9dd0bd-fc3e-3fb1-851b-c092606a56e2 | -8.75495 | -44.71583 | 2024-10-29 03:23:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e813fc7d-325a-3ae3-a885-5730ff49901e | -8.75169 | -44.71479 | 2024-10-29 03:23:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51ece84c-d47b-3d57-9a86-684564f15722 | -10.54628 | -45.14073 | 2024-10-29 03:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f6dd6541-14b2-3550-8da2-e2d7478f3dc8 | -10.54219 | -45.1398 | 2024-10-29 03:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 98e785e1-6db9-31c8-8225-c4d72c693747 | -10.51639 | -44.85004 | 2024-10-29 03:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 65b8149d-5b0d-3473-b19d-ab19d006bbe5 | -10.5148 | -44.84882 | 2024-10-29 03:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 87fe3b69-f0c7-3f09-82fb-1274c4788e15 | -10.45039 | -44.89043 | 2024-10-29 03:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29b0f17b-3cd4-3f42-9d44-c6c5d269d50d | -10.44906 | -44.89691 | 2024-10-29 03:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 31dff4ca-5fa2-3cd8-bfa8-c13d2bc54db4 | -11.40246 | -45.14062 | 2024-10-29 03:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 961d1901-87ad-38d0-86c9-19be875ff48d | -11.401 | -45.14083 | 2024-10-29 03:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d936580-7647-356e-a0cc-b17ae792bf9c | -11.40099 | -45.14778 | 2024-10-29 03:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0397f67d-64ff-33c7-b4a2-a0d431e4f4b7 | -11.39954 | -45.15481 | 2024-10-29 03:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5b3bdefb-209b-301d-9d88-d92d57888162 | -11.39947 | -45.14799 | 2024-10-29 03:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1762a992-4b83-34c4-b008-a8dc85983ec7 | -11.39799 | -45.15498 | 2024-10-29 03:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16ad47bc-2458-3b2f-b961-51361fa62726 | -13.61179 | -45.5812 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8e608d82-899f-30c6-82ed-33d371efc2d1 | -13.61039 | -45.5876 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a9d3d27e-0c4a-3b81-80af-a26abb981180 | -13.609 | -45.59399 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 32719279-4a71-3861-9cb5-1dec2f4901c6 | -13.60497 | -45.57959 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3069287e-fc3a-3df0-8df3-450a9c2bff4d | -13.60468 | -45.58421 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 44d8eafe-8ae1-3d54-89ea-f4fafcb4a776 | -13.60357 | -45.58597 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e954ed2c-755d-38c8-82f3-6eb0eb64869b | -13.60333 | -45.59061 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9cbfdd1a-abd6-3cdc-a0ed-5bd9be8280b2 | -13.60218 | -45.59239 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 79ef6794-1d41-3629-95fa-507d765309bd | -13.60196 | -45.59708 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a8d329ca-b2d8-333f-a3b0-0da76d0fc2c2 | -13.60076 | -45.59888 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 35a07c68-8c8f-3eca-84c4-1daa1b3cebe0 | -13.59784 | -45.58266 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fcf2e703-7228-31f7-bca4-aa3584aa84e9 | -13.59673 | -45.58447 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 500c8416-2732-30d1-bcd3-62c888da4600 | -13.59511 | -45.59559 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 88c63558-3f25-3179-b076-4c245bc9586b | -13.37113 | -45.10951 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4412b123-9398-32f9-8869-2aadb3716fd5 | -13.36982 | -45.11558 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08851ed0-a2b2-37cd-87f3-c05a7be6743b | -13.36893 | -45.10814 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ef288d2-592f-3794-8f01-17a17b8e040f | -13.36766 | -45.11423 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 695e83ef-f30b-3952-94e3-d2b79a3962f8 | -13.36577 | -45.10191 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README24.md)
