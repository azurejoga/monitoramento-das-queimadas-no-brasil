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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7a5f8b0-7476-3796-9173-9a787d43d563 | -9.35746 | -56.34732 | 2024-12-10 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10899d79-8d60-313f-9fbc-3657e3957ddf | -12.24432 | -52.44638 | 2024-12-10 05:18:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6d9cf28-1e37-3852-b505-841459991ac3 | -12.56275 | -58.35781 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 29a38f2d-ff6d-31de-8667-24555a0583f2 | -12.92106 | -55.73484 | 2024-12-10 05:18:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c0e3cd5-2703-320b-9f4c-b9dcef95e12d | -12.05252 | -62.79234 | 2024-12-10 05:18:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f49a53ed-ba14-3da3-82ab-5317ab94dbf6 | -12.5615 | -58.3546 | 2024-12-10 05:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c034dd28-f047-3705-9146-0a95030dfb65 | -4.3774 | -47.7627 | 2024-12-10 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f4d6188b-2159-3dfa-84fa-ec63686c70d8 | -4.3959 | -47.7618 | 2024-12-10 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 16b0aafd-ffb4-3c1d-a12f-4126b673d0a9 | -12.5427 | -58.3362 | 2024-12-10 05:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| da32979d-9055-3c71-8aea-015e8346e7e3 | -12.5425 | -58.3561 | 2024-12-10 05:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 56ce3006-79d8-3a0a-96ba-5bc7e8d53448 | -15.3674 | -53.13328 | 2024-12-10 05:20:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e24294d-550c-3f05-a3f5-fc11da5d7b09 | -15.06408 | -59.65577 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2042b65e-275f-3651-8c96-1fa772a73663 | -16.18454 | -58.17391 | 2024-12-10 05:20:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d0adbac4-9a21-3076-8995-74d91d339dab | -15.37226 | -53.13399 | 2024-12-10 05:20:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdeb6f8b-28ec-3f7e-86bd-b3362d65f830 | -15.08887 | -59.62946 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 697fc1b8-0d52-3dc8-8b75-b4d42aafb889 | -15.07816 | -59.63152 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08fa75e4-93ec-3477-b2b2-172863d1c31e | -15.07872 | -59.62782 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5fec253-d569-3b4b-9cfc-660783065847 | -15.88306 | -53.27468 | 2024-12-10 05:20:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd30ac6a-783e-3c92-a081-fb4f8a82a1c7 | -15.0821 | -59.62836 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6731218-25fe-3e09-ac7d-888bc2e3623e | -15.09225 | -59.63 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 877e0111-e991-30f2-b74a-252cbc344010 | -15.86912 | -53.26737 | 2024-12-10 05:20:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0368047-544e-312c-9604-4f72b8b4fb3e | -15.86617 | -53.26585 | 2024-12-10 05:20:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f342778-f169-3ce0-b5ed-3d0349fc6b06 | -15.17439 | -56.79081 | 2024-12-10 05:20:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20cf299d-ff2f-39b1-9feb-75bbbeac9bab | -14.62153 | -59.60915 | 2024-12-10 05:20:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 004fff4e-82f7-31a9-92a4-8ff343bd5ff4 | -16.15931 | -59.60373 | 2024-12-10 05:20:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b71c453e-c48f-30a3-8549-b5ac0fb9d443 | -15.08943 | -59.62576 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a021fe7-c118-3d7c-844b-4808d31c05c9 | -15.08548 | -59.62893 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea72951c-0397-34a5-9192-0754c6c2328c | -16.2727 | -59.51994 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a6c3649d-0bff-3a9f-9cc6-e0ddaa560704 | -15.06858 | -59.64892 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a490c6fa-6f0c-325c-a883-e28c6a1fc523 | -16.26929 | -59.51939 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 27c0b8ab-4f74-3055-a2ba-6fdc9dcaa3a7 | -15.09169 | -59.63369 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88a23cce-e915-3051-9911-bbbae26eeccc | -15.09056 | -59.64109 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f75e6ff4-bfd5-36c3-b461-f0ab5c4918ca | -15.16264 | -56.47728 | 2024-12-10 05:20:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59adc576-e2b7-35b3-a15f-e7e724c2270b | -15.25625 | -53.57154 | 2024-12-10 05:20:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb7cb690-fe65-3451-99ae-b9d42b014614 | -14.14483 | -60.187 | 2024-12-10 05:20:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36ee3bae-cf4d-3366-a94d-6da41fb2fd88 | -15.08774 | -59.63685 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0e48a9a-7b53-361e-8afd-1b79a9d3c30e | -15.09112 | -59.63739 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2498eb06-4254-36fb-a680-553c4243e420 | -15.06746 | -59.65631 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e0210a6-dde5-3b31-bc44-be09465592fb | -15.08661 | -59.64424 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a34aa09a-c589-3306-a20f-8106e15ad69a | -15.26034 | -53.57724 | 2024-12-10 05:20:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b6cd4e6-49d5-3a83-b419-75f92360a55b | -15.37292 | -53.12851 | 2024-12-10 05:20:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82d5dbff-a0f2-3efa-b887-1f3a4cd25660 | -15.26099 | -53.57201 | 2024-12-10 05:20:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a061bf22-2b35-344b-b3f6-6e0d3c8d4074 | -15.61473 | -59.74539 | 2024-12-10 05:20:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69204a66-314c-3d1c-88e2-75d6249c7543 | -15.08718 | -59.64054 | 2024-12-10 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb650652-084a-370d-835f-6a31957d5d0f | -15.15874 | -56.47669 | 2024-12-10 05:20:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02bc99b8-1656-3f47-af16-6a05bb55bac9 | -12.5427 | -58.3362 | 2024-12-10 05:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 71880fc0-7612-3552-8edc-12aaea9bfc81 | -12.5617 | -58.3347 | 2024-12-10 05:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 4611227e-63fa-3f28-abc4-d3c09e55caad | -4.3959 | -47.7618 | 2024-12-10 05:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| ecbebc89-8ce3-3ab8-849f-d56b47e7a367 | -12.5615 | -58.3546 | 2024-12-10 05:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 07dd7391-2156-38f9-923c-ea6da782ce32 | -2.9859 | -52.8554 | 2024-12-10 05:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 8aadc888-45d5-3a17-82fc-2c40ae493f2a | -12.5425 | -58.3561 | 2024-12-10 05:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 084f41ba-601f-3d46-87d2-6b2ce6502a0e | 4.12684 | -59.95424 | 2024-12-10 05:35:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00278611-1a0a-3d2a-83e3-7de7d59ca432 | -2.45154 | -57.93132 | 2024-12-10 05:37:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfd9f79b-6c48-3628-8d1f-62408d1e7b9d | -2.96652 | -53.72612 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d41f6135-168d-3637-b76b-3d7b87e9b375 | -2.99531 | -52.84768 | 2024-12-10 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 404f82e1-24b9-3662-b5fb-e4773a520467 | -3.46631 | -53.96528 | 2024-12-10 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 184a1dad-9dc8-38d0-b1e7-5ef52fbca4cd | -3.46571 | -53.9693 | 2024-12-10 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee76e7d0-2a1c-3ed6-acc7-43ea7538b96a | -2.22054 | -53.72113 | 2024-12-10 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8487eb27-d978-3290-a28a-7642819e3d8d | -3.1007 | -53.74561 | 2024-12-10 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5792ece-d58b-3190-bdff-b80f9e96e802 | -3.10473 | -53.75932 | 2024-12-10 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98107d27-5b50-383f-b80e-0c1feef4805b | -2.99682 | -53.04195 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7cb4d992-cbea-3a53-a17c-81a0b22d83a0 | -3.52805 | -54.59318 | 2024-12-10 05:37:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afe91521-789b-3879-9f35-a80e2580647a | -3.8334 | -52.35426 | 2024-12-10 05:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 80b644dd-c7ca-36c4-a446-68fd21fbc72e | -3.05613 | -54.24882 | 2024-12-10 05:37:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19f2013e-e45d-3aef-b961-fcb4c1c36a56 | -3.04465 | -54.24751 | 2024-12-10 05:37:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7ac3cc0-0c08-3c9b-8b2a-335b562f0702 | -3.10282 | -53.25655 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e6d90c2-bb33-36e9-872a-1cf93d0be493 | -3.53043 | -54.69366 | 2024-12-10 05:37:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25322efb-79ed-3a55-9c60-e7c73a0c792b | -4.13967 | -53.67565 | 2024-12-10 05:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e4c0197-78e1-3c9e-98eb-d22412c117fc | -4.03792 | -50.8068 | 2024-12-10 05:37:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26cca504-fbaf-3dbf-8aab-6544e0bddf0c | -3.09318 | -54.07922 | 2024-12-10 05:37:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f63656e5-ea42-3ea3-b468-2813038d792f | -2.30869 | -54.00628 | 2024-12-10 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0818d755-43bd-3389-adb0-dc83a485178e | -3.3418 | -53.25309 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 74bd3cff-1b44-31d4-a276-a2d7a9f3d42e | -2.99615 | -53.04652 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 38e14200-cf21-3ca1-8ed4-bb76ee38eed9 | -2.96001 | -53.72944 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69ac6699-410d-36de-b868-38effedb2450 | -2.98725 | -53.02108 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c10b841-0215-3f37-955b-64d03c8a0c2a | -1.49943 | -53.43404 | 2024-12-10 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6c9fa64-916d-38ae-83e7-09fcbe814854 | -3.09743 | -53.25085 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8066c7aa-f607-39c0-98c2-d779321b58d5 | 3.22277 | -61.19174 | 2024-12-10 05:37:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c297e531-5166-33c9-9abe-df7b27ac728b | -2.45201 | -57.92817 | 2024-12-10 05:37:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab8066eb-eced-3797-8170-f41d513787e8 | -2.22101 | -53.72176 | 2024-12-10 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad8e138d-480c-3c6b-aa76-a3cf56d49dfe | -2.99271 | -53.02692 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a8bad64-8ec0-3d8e-b2ed-8ba6234df626 | -3.08799 | -54.07439 | 2024-12-10 05:37:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d745ef5-2539-32c9-81fa-d0cb732b416a | -4.0308 | -50.80553 | 2024-12-10 05:37:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56055c6e-7fb6-30a7-93b9-67c4366e0e51 | -3.10421 | -53.24717 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cebb11c6-4f9f-33a2-9cf5-299e90c0dd59 | -2.30295 | -54.00543 | 2024-12-10 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afb51ca6-c8c7-398e-a0ef-f2e12e8ebab3 | -3.29901 | -51.6329 | 2024-12-10 05:37:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20de3039-1cba-30c2-9b8c-05994f8240fa | -2.98644 | -52.85157 | 2024-12-10 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 782cdb6f-3852-3a04-b15d-582543958dde | 3.22617 | -61.19122 | 2024-12-10 05:37:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ddc7546-9bae-3f6c-81df-9713393e04eb | -2.98573 | -52.85649 | 2024-12-10 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5c7c9c64-2f82-3ab8-a556-9164293888d7 | -3.08875 | -53.22515 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef194b83-fbd6-3291-8eb1-a52cbb7b3a95 | -3.0452 | -54.24379 | 2024-12-10 05:37:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d844aa62-d830-3f2a-b55d-b16ceca29bb2 | -3.06242 | -54.24586 | 2024-12-10 05:37:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01232ae1-e8a1-3ec6-83cb-a98961c5c31d | 3.22734 | -61.19854 | 2024-12-10 05:37:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71ab2a24-5d6f-3d98-9173-2e0955b7104d | -3.52861 | -54.58937 | 2024-12-10 05:37:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1319d59-34c5-3b39-92dd-539e54971d3e | -2.98805 | -53.02025 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0eee1cda-0d76-3497-9b6f-9ca3fc29c081 | -2.99335 | -52.84791 | 2024-12-10 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b99e24df-aa77-30a3-8b1a-4174f843456b | 3.15502 | -60.72115 | 2024-12-10 05:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 554c6ef4-5690-3b3c-822e-d395f9c1542f | -2.95433 | -53.11774 | 2024-12-10 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2924e2be-4f1c-3b9f-8b81-a5fae9d66cca | -3.0504 | -54.24811 | 2024-12-10 05:37:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfb7cf67-834b-3958-9d7a-ea1e31ac5074 | -1.70264 | -52.60754 | 2024-12-10 05:37:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README38.md)
