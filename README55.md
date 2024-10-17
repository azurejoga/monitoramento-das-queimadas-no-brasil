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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bc8b6e4-85cf-3915-b4c7-8ee657d49ae1 | -9.16088 | -61.89958 | 2024-10-17 05:29:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f757c47-b295-3b2b-aaea-50f6f332662f | -9.16033 | -61.90311 | 2024-10-17 05:29:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba8d77a7-3123-3d7f-8dbe-460bf76e2224 | -9.15978 | -61.90664 | 2024-10-17 05:29:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8d224c03-0285-3c7c-850f-6d33ea47a240 | -9.15924 | -61.91016 | 2024-10-17 05:29:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 67eafe7c-3cdf-3df5-a807-64ab618c1b7f | -9.15754 | -61.89905 | 2024-10-17 05:29:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e96dd6c2-4b14-38cd-ac22-17ab6615cbd7 | -9.15699 | -61.90258 | 2024-10-17 05:29:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c68fcd77-9e07-3eef-ab96-20296b2613a2 | -9.15644 | -61.90612 | 2024-10-17 05:29:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2261db78-8ded-3546-8e3c-afad9cd8230e | -9.15311 | -61.90559 | 2024-10-17 05:29:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 636e7840-51c4-37e2-8362-f73df85f2ab3 | -8.82436 | -62.34998 | 2024-10-17 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70e4a55c-3ca7-3ca1-a0ce-56751163c6e4 | -8.82103 | -62.34945 | 2024-10-17 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97509ac1-417c-3e65-85e0-965ede90272b | -8.82049 | -62.35294 | 2024-10-17 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9025863e-0d99-39be-8d4e-70e4d903499c | -11.8034 | -64.27258 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1c5a2d2-6524-3d83-84e1-b4abea0a2232 | -11.80282 | -64.27616 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b4b1f30-4c7c-3490-8035-05127cce4131 | -11.79931 | -64.24652 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ad391f6-8fc2-3b85-a1ae-6215525337ed | -11.79921 | -64.26867 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fce0ade6-d929-3cf6-a4d0-3971d318e6f2 | -11.79386 | -64.21613 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b283c448-8665-3475-a7b5-4e4e52a6ebd9 | -11.79328 | -64.21972 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b27f63d5-7eab-3a74-bb9d-0956c2dcfd3e | -11.76871 | -64.09435 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06decee4-b373-3349-a431-af205ba47826 | -9.2968 | -65.36652 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc2e61df-0206-36a8-9ef5-15eca903c502 | -9.29326 | -65.36591 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32e6676b-ff05-3772-835c-a89b8d9b5344 | -9.28421 | -65.37664 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0fee5ed-3120-3b42-b083-4546d9083b7f | -9.28065 | -65.37612 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d5f7065-c2bb-3407-9af8-cf63a070ff7d | -10.83418 | -65.02502 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62331bed-c888-3001-88dd-bbd6156f79fc | -10.83011 | -65.02822 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a47834f-ae99-3a62-9450-51ef273aab31 | -10.40023 | -65.37534 | 2024-10-17 05:29:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32bd2b78-44a2-3ccf-b9c8-d585af85650c | -9.38255 | -65.65962 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 729237d4-0cb8-3ab7-aed1-6c8f8d32d0cf | -9.37896 | -65.65903 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3779a124-bff2-3335-9141-aba897ad8881 | -10.91142 | -65.10745 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cf368f6-162d-3a54-b268-1dbddf0e7416 | -10.90919 | -65.10775 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98792d66-05ee-39ee-b895-f1f0f127777a | -10.90797 | -65.10687 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b41d5d0a-7056-3f7a-a62a-6ea6f981aa46 | -11.75733 | -64.81119 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 867f4057-e246-3a3c-a9a4-d37f7aae8b01 | -11.75673 | -64.81487 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 70514b5a-a7f9-3afc-8e73-2ae65313e75a | -11.75394 | -64.81061 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 544cfbe4-e6a3-3c77-8b41-efbb7acd71fd | -11.73461 | -64.97153 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 721fbefb-8f41-3265-9881-a889ddde98b1 | -11.73416 | -64.80347 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 697d580f-9476-33bf-aa02-8160e0c6764a | -11.73016 | -64.80659 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ec7dd4b5-2461-3b27-ae43-18a07372481e | -11.72955 | -64.8103 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9a92ba3-b88f-36f3-b4af-099c65865f9d | -11.72616 | -64.80972 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 356a1781-90c1-397e-b90e-d133eb5b43d9 | -11.6703 | -64.83147 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55369d9f-41e3-3255-95bc-9e306fb30b43 | -11.6697 | -64.83518 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72a63ab1-144b-3504-964a-360050f3633c | -11.66751 | -64.82719 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76e2567e-2d42-3bea-9897-93cb8d1f0828 | -11.6663 | -64.83462 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fe122e4-0a38-3888-ae4f-1605ddccefbe | -11.66569 | -64.83833 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94e2c1c7-3aa2-3b4c-8772-df2977a4aebb | -11.6629 | -64.83404 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5008a319-f08f-3ef1-b0a6-8c4d02a6fad5 | -11.66229 | -64.83775 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5e78023-1483-3b11-bf2a-f222767fd300 | -11.66169 | -64.84146 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac85f95a-1b15-3fd2-8f38-c67d59db5c4b | -11.65889 | -64.83717 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eaf7037d-acb5-3136-85da-ece9498ff684 | -11.65549 | -64.8366 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 43e1d8ae-58f4-3d41-8214-0dfc8a3ddb04 | -11.65209 | -64.83604 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a9034a8-69ee-3880-80bb-127b9e0835a5 | -11.6505 | -64.82433 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 977cb5aa-c5da-3f24-87bc-5037eea96d7f | -11.64989 | -64.82804 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c4a62fa-6672-337b-a832-58608c97672f | -11.64929 | -64.83175 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdcda856-09e0-3868-9f11-8fe135da43d5 | -11.64868 | -64.83546 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0498ff06-530e-3fa1-9993-ecd0b11bc97e | -11.39526 | -64.93111 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c687b3a-44f6-3b37-b609-b3a53eae925e | -11.39184 | -64.93053 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c1df696-a354-35a0-82a5-f30211a08e8b | -11.38843 | -64.92995 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc43847f-c57a-38c9-b9d1-309a87dbe7e6 | -11.38562 | -64.92565 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0161c675-4f74-39de-8882-977c9f0e859a | -11.38501 | -64.92939 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34a2d0ae-f6fd-354a-9b24-2e7cf5894ddb | -11.71849 | -65.2205 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44db7606-8a1f-318d-b23a-3f166285f463 | -11.71505 | -65.21991 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80b8f7cd-0802-3236-aca9-6e1c9e0bf3a6 | -11.71255 | -65.23513 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55221fef-160b-3508-be71-fb505fd07781 | -11.71193 | -65.23894 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 639bb05c-bf53-391b-ba09-956d5e7c640d | -11.71161 | -65.21934 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9df0c15a-972f-384e-8c43-14272ef40285 | -11.70941 | -65.21115 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8fc2be5-9f85-358f-a84c-e9caf81a2452 | -11.70816 | -65.21875 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 894703a7-3a99-30ff-b60a-643b75c498b9 | -11.70566 | -65.23397 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5fb4a44a-f9fa-3137-904a-887ac50548c9 | -11.70504 | -65.23777 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c549ccb-61f4-35a6-a820-8bd1df9dc460 | -11.70441 | -65.24158 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fa67675c-41ba-3fda-a01d-adde1bdf8365 | -11.7041 | -65.22197 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cb27c8a-babd-3464-9bb7-7debd62add69 | -11.7016 | -65.23719 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b62149d8-494e-3604-8c09-2fad8b66d708 | -11.70097 | -65.24099 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc0c4cfb-26d6-32cc-92b2-02564408a4fd | -11.70035 | -65.2448 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d9bbd9ce-79da-3691-86a0-adeeefcce0d7 | -11.69753 | -65.24041 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c15d6bf8-0710-3b12-8fea-8c4d599b453a | -11.6969 | -65.24422 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdd2ff51-1024-398a-b46f-9db6b932b80b | -11.69345 | -65.24364 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81c7195e-fe86-3405-9b96-4b4ed96876a1 | -11.49681 | -65.12139 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f5efb02-3fde-3b4e-94c1-da7ab067af93 | -11.49619 | -65.12518 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ceaeedd9-68e2-3bd7-a9b9-ab98c608f2e0 | -11.49338 | -65.12081 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afa08e58-4737-32a4-bd57-34560bf79eba | -11.49276 | -65.1246 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0015f2e2-dab1-3417-b8a8-1df76b38b9dd | -11.48994 | -65.12022 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 084ba71f-1441-30de-8536-90abe0f9a62b | -11.48932 | -65.12402 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87694db8-ba38-3e3c-8a6c-a35f3320153a | -11.48681 | -65.09639 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dac82282-ed3c-392d-a262-25340198c9d7 | -11.48651 | -65.11964 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4980d621-b6e5-3a28-a384-c5915681f966 | -11.48619 | -65.10017 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ef6eb23-0662-3081-afe5-9739144c72aa | -11.48588 | -65.12344 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5a61f09-f1bb-3f68-b3e4-7c7f7c1e92da | -11.48556 | -65.10395 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ec6fed4-240d-3a2b-b6cb-afe4217752a6 | -11.48432 | -65.1115 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18cd5002-a66f-33ed-9ba0-5195d173b5db | -11.48369 | -65.11529 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8247d639-fe2f-37f6-a9ed-f7cc92c128ed | -11.48307 | -65.11906 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a7fd1c3-61e8-38fd-b601-2cd0a2dda6c1 | -11.48275 | -65.09959 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a56fdc88-78f3-3fb7-94e6-41a704262249 | -11.48213 | -65.10337 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb438b70-71db-3ad6-8431-f907fe40f69f | -11.48151 | -65.10714 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 506657cf-cf04-3a6f-b9e0-0b6eff0fc36f | -11.48088 | -65.11092 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a5a2dd8-ec10-362b-a779-8b4ca5a1bbb7 | -11.48026 | -65.11471 | 2024-10-17 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e68b308-dc2b-3f87-9c9a-1d2ca9879e8d | -9.39478 | -68.98382 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e8643b36-d142-3c29-80c7-7eb1c0f3e88f | -9.39402 | -68.98805 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0fedc999-b208-3cdc-9a24-efd47c809e09 | -9.3904 | -68.98306 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7755f24a-791a-3fa5-9ca4-1d9dd5d1883d | -9.39009 | -68.98463 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2eb9c57-7098-3070-a74c-0b4c548c675f | -9.022 | -69.21769 | 2024-10-17 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5df0128-3598-327e-98c9-cc759dba90cf | -8.62162 | -69.97825 | 2024-10-17 05:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README56.md)
