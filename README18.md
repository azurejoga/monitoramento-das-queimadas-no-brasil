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
| db18f434-f1a7-3287-9927-734b624d6ee0 | -16.8096 | -55.9177 | 2024-10-02 01:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 66c855dd-9ff6-3754-8b1e-649a37ac1bca | -16.8292 | -55.9152 | 2024-10-02 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 124.5 |
| 73e5bffd-69dd-311c-bdde-ac9e08064259 | -16.8295 | -55.8945 | 2024-10-02 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 141.9 |
| c3af5c29-1697-3a74-ab0a-350a8520ac73 | -16.8299 | -55.8737 | 2024-10-02 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| d789a45a-8901-368b-a96e-2212addec9ed | -16.8488 | -55.9128 | 2024-10-02 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| d6889afc-9df1-3772-a1e4-2c8905d79394 | -16.8491 | -55.892 | 2024-10-02 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 109.6 |
| 10314f25-057e-3faa-a58f-79c4e46e93a7 | -16.8695 | -55.848 | 2024-10-02 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| e596b26d-e928-385c-ab2e-1c3d115e3ac4 | -16.8787 | -57.6971 | 2024-10-02 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.0 |
| e0bd5d38-a6c6-34ae-9920-a492ebf593fd | -16.879 | -57.6767 | 2024-10-02 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.0 |
| 72001543-a45b-3b7a-b578-603ad5fb579c | -16.898 | -57.7153 | 2024-10-02 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.6 |
| b5530ca8-af28-344d-bc64-963633c84c11 | -16.8983 | -57.6949 | 2024-10-02 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 234.1 |
| 60abd423-8d6d-3468-9662-fb1c1159c4a8 | -16.8986 | -57.6744 | 2024-10-02 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.0 |
| 0c4021f9-66b9-36c6-a8f1-28c8f96034f9 | -16.9176 | -57.7131 | 2024-10-02 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.2 |
| 7240638b-6aaa-3e31-be0d-0654a876d68f | -17.0499 | -56.7757 | 2024-10-02 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.5 |
| 89fae523-477d-31fa-9f32-27f912fc5cce | -17.0502 | -56.7551 | 2024-10-02 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| aa2fc783-2197-3726-a669-a6140cb8e9c9 | -17.0612 | -56.0931 | 2024-10-02 01:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| defcb087-7f6c-3e1e-a2be-c97db91fe283 | -17.0695 | -56.7733 | 2024-10-02 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.7 |
| f28940d0-c4e0-3b02-81de-56afffe5d220 | -17.0892 | -56.7709 | 2024-10-02 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 57c7130b-260f-3487-b502-513595984dd6 | -17.0895 | -56.7503 | 2024-10-02 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| b0f5ce4b-1111-31df-912f-660a2883607f | -17.1091 | -56.7479 | 2024-10-02 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 7dc5904d-a4ef-34e7-a76b-7583d874ae0f | -17.1577 | -56.1844 | 2024-10-02 01:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.3 |
| 4af69bb8-b0ce-3dbb-9195-c09e5956d0ff | -17.1581 | -56.1637 | 2024-10-02 01:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 98.4 |
| 289fc8bf-b358-351a-bb26-7427a375eaa1 | -17.1971 | -56.1795 | 2024-10-02 01:06:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 5c7351ab-5bf2-355e-b3ff-9d00d357d31c | -17.196 | -56.2417 | 2024-10-02 01:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| bb55eee1-0eea-30cb-adf8-4bcf58ae33d5 | -17.1964 | -56.2209 | 2024-10-02 01:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.3 |
| 57238e14-65ef-3ed3-b980-729bd4bafbde | -19.2317 | -46.8687 | 2024-10-02 01:06:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 7bf0fe63-854f-3f65-b0dc-92969b0da542 | -19.2323 | -46.8452 | 2024-10-02 01:06:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 6ff1dc6d-adc9-3dfc-8eac-b82383e4a6df | -19.2519 | -46.8641 | 2024-10-02 01:06:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 119.7 |
| a6fc460f-2a8e-3607-82d1-1e26f1a56935 | -19.2526 | -46.8406 | 2024-10-02 01:06:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 99d65565-a44c-31c7-93f1-36c7157177fb | -21.3456 | -55.6841 | 2024-10-02 01:07:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 67.8 |
| b6188308-21c9-3f33-99a3-54bfdea174e3 | -22.9006 | -45.1029 | 2024-10-02 01:07:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.8 |
| 8608d172-a86b-344e-bb10-b0b64c38ea45 | -22.9014 | -45.0779 | 2024-10-02 01:07:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.7 |
| 218c8153-d998-3270-b53d-5ef3a65116c4 | -3.2136 | -46.7843 | 2024-10-02 01:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| ac416b3b-eacd-391a-a4cd-745bea8803ab | -7.1794 | -46.9665 | 2024-10-02 01:15:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 6c2c3117-b8c4-3cf6-ac3f-b10a87a57730 | -7.1796 | -46.9444 | 2024-10-02 01:15:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| dab82ae2-c2f8-30d7-b4dd-458e370ecb39 | -8.205 | -44.365 | 2024-10-02 01:15:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 727ffa88-0ced-3b42-8acd-9eab002b11eb | -8.2053 | -44.3419 | 2024-10-02 01:15:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| bdb2bf9f-cc5c-3b17-9bc1-3e875aa596f5 | -8.4643 | -62.7124 | 2024-10-02 01:15:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 6f6da960-7fa7-3836-b51e-6370eef95418 | -9.5584 | -62.7997 | 2024-10-02 01:16:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| d54d7155-10fe-3b2e-bb69-b3c1aea99b60 | -9.9367 | -64.9179 | 2024-10-02 01:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 174.9 |
| 48c53de9-7414-34ad-a0c5-97fe42db5df6 | -9.9368 | -64.8991 | 2024-10-02 01:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 142.8 |
| 9823debe-e342-3864-bc2d-e58417094303 | -9.9553 | -64.9172 | 2024-10-02 01:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 173.1 |
| 3a63b3ad-33af-3499-86e2-02c6fddf2933 | -9.9554 | -64.8984 | 2024-10-02 01:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 172.4 |
| e8a90741-b336-3fe8-ae04-53580d3f2dd3 | -10.626 | -55.8752 | 2024-10-02 01:16:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5937ad26-ae1f-31dc-8e3a-955d5812907f | -11.884 | -43.8142 | 2024-10-02 01:16:12 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 104ab97e-3392-3662-a3a8-5a09c25f4047 | -11.6742 | -65.0172 | 2024-10-02 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| f9814e95-8d5d-3f8a-a2ea-1019dcc23ba7 | -11.6743 | -64.9983 | 2024-10-02 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 0fc2501f-bd44-3721-8348-7f51356ca0cb | -11.6554 | -65.018 | 2024-10-02 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 9640c1f6-14da-3b75-954a-5b6c7671ea86 | -11.6555 | -64.9991 | 2024-10-02 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| d6728a98-d6b7-3f96-8d69-ceeb41e01004 | -11.6556 | -64.9802 | 2024-10-02 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 09e54a04-f55a-380e-9d25-505554f35fcc | -12.4433 | -43.7242 | 2024-10-02 01:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 8e6bc1f9-5ce5-38f4-83f3-996f433ddc6f | -12.2946 | -47.6446 | 2024-10-02 01:16:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| e3770420-1124-3058-82a7-00f42b799e55 | -12.6484 | -63.1214 | 2024-10-02 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 110.7 |
| ec95df7f-df84-3b58-a506-7845b76e4624 | -12.6486 | -63.1022 | 2024-10-02 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| bfa8f2a9-e0cd-32b9-b253-08bf3833e1df | -12.7054 | -63.0798 | 2024-10-02 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 4afaad62-09bf-3ff9-8aac-ed8d775809ca | -12.8593 | -62.7826 | 2024-10-02 01:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0ceab8f5-7c44-3a35-ae48-05e012d96efe | -13.0019 | -51.148 | 2024-10-02 01:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 866347e7-8ede-3559-9ad6-035b79a7be8f | -12.8782 | -62.7815 | 2024-10-02 01:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 3f7ecbd4-73f4-3b14-ad92-04540a7e7e02 | -13.2373 | -48.577 | 2024-10-02 01:16:20 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 0440e3ee-bf91-30d5-9000-1f2fb7dc5e06 | -13.5965 | -51.1367 | 2024-10-02 01:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| ea20fbce-2881-30b8-ada2-0af93fe7da7e | -15.1197 | -55.8307 | 2024-10-02 01:16:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| d9ba6a79-6b1e-36c6-b7d9-a4ba69ca3c57 | -15.139 | -55.8285 | 2024-10-02 01:16:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| b634f385-2b44-3d71-85c3-8a99630a8fb0 | -15.3902 | -55.8409 | 2024-10-02 01:16:33 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 12d4c0a9-ebf6-3e1e-a44c-8c6808224c77 | -16.6868 | -57.4741 | 2024-10-02 01:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.6 |
| 37f7b373-6a23-3253-a450-6be02c1df6aa | -16.6884 | -57.3718 | 2024-10-02 01:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 10ef5cd5-c5c7-304e-9f42-2814729fce7d | -16.6887 | -57.3513 | 2024-10-02 01:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 162.2 |
| 2d36a1f4-9eb8-3529-b2e0-7b5176bac5c4 | -16.689 | -57.3309 | 2024-10-02 01:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.2 |
| 880a3bef-13b9-3342-a77a-ccfbfc024cfa | -16.7082 | -57.3491 | 2024-10-02 01:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| e66b3bd5-2963-3f40-a2d1-03a000144152 | -16.7086 | -57.3286 | 2024-10-02 01:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.8 |
| 69fb68db-062a-37e4-b301-401485ee9238 | -16.7265 | -57.4287 | 2024-10-02 01:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 28ef9644-92ab-3a88-8312-5cb1be2521a5 | -16.7452 | -57.4878 | 2024-10-02 01:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| f74dc748-c2f5-325f-b47d-229f8608f295 | -16.7461 | -57.4265 | 2024-10-02 01:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.5 |
| e4d8d125-0800-3994-ba79-f7c664a2fbc1 | -16.7647 | -57.4856 | 2024-10-02 01:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.1 |
| e96e2702-c86f-3e82-b725-6b7bdf98f70a | -16.8096 | -55.9177 | 2024-10-02 01:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 748b4473-f193-3836-b27d-95563f785b60 | -16.8986 | -57.6744 | 2024-10-02 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.8 |
| 7ec89e22-e559-32be-931b-841b4efa2049 | -16.9179 | -57.6926 | 2024-10-02 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.7 |
| c1f4a671-12ee-381d-81bd-ef29680a605b | -16.8292 | -55.9152 | 2024-10-02 01:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 122.4 |
| 7eb95673-0fe5-3538-9dd5-5d5cf768acad | -16.8295 | -55.8945 | 2024-10-02 01:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 156.4 |
| bc28c436-6aa1-3a40-8974-027e259550ec | -16.8299 | -55.8737 | 2024-10-02 01:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 8e4a9860-555b-33d7-85cd-fe172c813569 | -16.8488 | -55.9128 | 2024-10-02 01:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| 860e5517-8753-364d-9221-17efefe2cb74 | -16.8491 | -55.892 | 2024-10-02 01:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 100.2 |
| 1df58778-fe26-3e6d-8f66-21f71d040332 | -16.8695 | -55.848 | 2024-10-02 01:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 05367bd4-e237-3061-894a-db43b9957de1 | -16.8787 | -57.6971 | 2024-10-02 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.0 |
| b3e9aec5-198f-3bfa-ba0a-8817ef172a03 | -16.879 | -57.6767 | 2024-10-02 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.9 |
| 8fcd71da-7e39-3f8b-9352-3fa5124e6599 | -16.898 | -57.7153 | 2024-10-02 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.0 |
| 14be1d60-221d-33e1-b03c-ee28a947fd6b | -16.8983 | -57.6949 | 2024-10-02 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 218.5 |
| 72d15f6e-0091-3fc8-b58f-0e88bcebb226 | -17.0502 | -56.7551 | 2024-10-02 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| f1f0cbe0-a3bb-38f5-9465-bf33dd7af3ca | -17.0612 | -56.0931 | 2024-10-02 01:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 8bef2818-6d21-3185-96b1-c12d5ce52a2b | -17.0695 | -56.7733 | 2024-10-02 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.2 |
| ed9be2dc-05fd-3640-ac6e-dbec069169ab | -17.0705 | -56.7114 | 2024-10-02 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.8 |
| ddcf568d-3f00-3a5e-a153-4a036ac87082 | -17.0709 | -56.6908 | 2024-10-02 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.5 |
| 3b9c1470-99b8-3cd7-8105-4517665e1e60 | -17.0892 | -56.7709 | 2024-10-02 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.6 |
| cd16fa20-e6da-3aef-96f8-dc246139bb5c | -17.0895 | -56.7503 | 2024-10-02 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 2a935c7f-7477-3bb7-9118-7eff8aa9cd26 | -17.0902 | -56.709 | 2024-10-02 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 5cfa83f9-71ca-3e4c-90a4-b84ad3abe578 | -17.1091 | -56.7479 | 2024-10-02 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| bb9ee198-2f20-3806-bd30-1b32f72cba55 | -17.1577 | -56.1844 | 2024-10-02 01:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.6 |
| 0f319c5d-d9e1-3447-99d9-afe21d12d5a5 | -17.1581 | -56.1637 | 2024-10-02 01:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 58cebcdc-0c5f-32b3-8d2e-3d3ea09e530e | -17.196 | -56.2417 | 2024-10-02 01:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 7c00c6cb-4a5e-3597-9b22-1ddace1d4dfa | -17.1964 | -56.2209 | 2024-10-02 01:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| 6725b7fe-595c-313d-a434-e7a4ff6625fa | -19.2317 | -46.8687 | 2024-10-02 01:16:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 126.6 |


[Clique aqui para ver as próximas entradas](README19.md)
