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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd4acc7d-3357-33d7-ae6a-9bddc3c108f9 | -6.80539 | -59.42513 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e0534bc-3e28-3c94-a901-02fc33a8faeb | -6.67395 | -58.74329 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 0d0ced03-5fb6-36ea-9088-71c9fa086fbe | -6.66096 | -58.80103 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5356c276-d66f-377e-9663-7d220e0147c2 | -6.79937 | -58.64699 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 923fa5d0-9ec6-3730-8ed2-7476da076774 | -6.7931 | -58.65497 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd7f68f5-e4b3-3ecd-9438-09e1989f8047 | -9.5122 | -60.49529 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0da466c6-957a-327b-8862-a9f9e5d8352d | -6.90198 | -55.70142 | 2026-08-23 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e07a8560-11df-37e2-84e5-a98f3a372d14 | -6.94472 | -59.07224 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a7372548-d232-3c69-9918-b6a2cf756c28 | -6.76253 | -58.66283 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ed1c687-6fac-3bbf-ba06-0f48f4a39abd | -9.58929 | -60.509 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9cde74e7-c862-3d67-9082-252e92f97134 | -10.06185 | -67.55006 | 2026-08-23 05:50:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd4122d4-c096-3e5a-85a5-dfeda78f85ed | -6.66931 | -58.73956 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| eb9c3544-6fba-3784-837b-a1a816c9702b | -6.76328 | -58.68423 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 262a1edb-e179-3a57-b1bb-868fdff41b2a | -6.78684 | -59.4169 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98088219-0439-38aa-b661-333fc244f389 | -8.40294 | -62.68448 | 2026-08-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87f89f36-61e5-3c3d-bee9-54f35978080a | -6.79166 | -59.41764 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 709a9231-b8c2-302c-8c84-7af1891d494f | -9.51944 | -67.16674 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6969601-0655-34ae-ba70-9e75636c4d9d | -9.21626 | -59.7911 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c88308e-c86b-3f1c-8420-10fbbb7fe66a | -8.53888 | -54.84908 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5976310d-c9fd-3a44-82a2-0a11cef41fde | -9.10199 | -60.92641 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 385c25b5-f7eb-384b-9721-64924dc3d706 | -6.85002 | -58.98222 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 603cc7bf-cd7f-304c-b6ac-591489bcd959 | -7.79017 | -61.42265 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d246af73-88d8-3ac6-9e98-e3d7de1710b3 | -9.43004 | -60.48243 | 2026-08-23 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f39e6890-d6a5-3094-b9bf-2db757a0544a | -6.79818 | -58.65572 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ef9e93ec-4a70-31f4-aac2-8c5f4a9a1d02 | -8.40689 | -62.68507 | 2026-08-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a926f79-441e-3910-acb4-d899481892c4 | -8.53491 | -54.84913 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8c05eeea-f75c-37b0-937c-9bcf52b9271a | -9.21306 | -60.76683 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65552287-152a-32c3-917c-5c55ceb28c8e | -6.69574 | -58.73445 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 705c3711-8921-3683-a9a4-c3adb4482f52 | -9.21242 | -60.77159 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9499615-72e4-3d81-aea2-a53b2b238ec6 | -6.86699 | -59.40721 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9a436b31-f0c5-3369-98bd-97f351feea26 | -6.89076 | -59.4061 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00bc7403-3e6f-3e83-b444-75a42e8f149b | -6.76382 | -58.6903 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 491fc4f4-1d14-39b9-8aed-54a65b7a6796 | -7.61612 | -61.61647 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3239f2ba-5e12-362a-a848-f672cfa405f1 | -9.05199 | -65.4504 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75872464-196f-3361-a45f-362294786039 | -6.75746 | -58.66206 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99fb5734-7045-344a-acfd-9440c8a46624 | -6.94747 | -59.06165 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c2d6c202-6af7-30d6-b5b6-d517eb126cfa | -7.62088 | -61.61322 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c3ebd22-e323-3a2b-b4f0-6c23034635a9 | -6.6794 | -58.74102 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2189cafc-769f-34e2-830c-c1c3d8719a76 | -6.76931 | -58.68809 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 282473fe-0b72-3904-9f77-3f16148a719a | -6.702 | -58.72643 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5c3670d8-6bd5-3093-a57e-f3065cd22170 | -6.78469 | -59.43269 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e5e4df9-054e-3ebf-91eb-ac4e9bf4e9f5 | -6.94252 | -59.06087 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4288ef8-e3e8-305b-8064-dd4096b5b202 | -6.75662 | -58.66805 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57b12805-0cc0-327c-952d-047d5d12445b | -7.86579 | -63.77066 | 2026-08-23 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 039fbbc0-6684-35d5-b6e6-e4748c7964af | -9.13786 | -65.95276 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16b656e7-bfc4-3b58-a01c-5a653429c836 | -7.66781 | -63.33364 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9bbecae6-e81e-35d4-bd0d-a9029b4f70fc | -6.88772 | -59.04651 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84e8fa7b-6da7-31bb-97e8-9a2b9be82525 | -6.81383 | -58.65505 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| de0deae5-321b-3014-ae70-5443afe0c71f | -6.80751 | -58.66333 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dd0fa90e-4656-3279-8cab-6cac4570f157 | -9.24628 | -60.79538 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fde0851-2016-351d-a84d-2061e92820f6 | -6.96309 | -59.05829 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 258b1758-82b6-33c9-89ea-c6fbd4cc778d | -6.90135 | -55.70623 | 2026-08-23 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b94a393-7dd1-3e19-83a9-69bac116c958 | -9.10951 | -61.58894 | 2026-08-23 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 709feede-341e-3686-9ed5-4554cced331e | -6.88522 | -59.41061 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1888a6c2-2126-3072-a47b-a6cecc18b354 | -7.81702 | -61.78124 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbdc1e20-02e3-3b25-a59b-70fa7e5b78ee | -8.91844 | -60.72852 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b8fffd0-d921-318f-bd26-9e3fa2db6c65 | -6.87401 | -60.01323 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 30d8a1d7-6be1-3a91-9af3-ccdb9246508e | -7.78479 | -61.43009 | 2026-08-23 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ffbe2f92-4514-3d03-b5b9-da7b5ebd0eda | -6.81298 | -59.6848 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad91e2be-8280-331d-b09b-c53cfdd7f19d | -6.80997 | -58.64532 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29e69aaf-cf2f-35b9-9cbf-2936ff9d88b9 | -9.1452 | -65.95013 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75b89aed-d79f-35fc-856b-2971b44418fe | -6.77936 | -59.75246 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4ed17fa2-c55e-381e-bd22-9859b8d98678 | -9.18904 | -59.45121 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5eff89fe-48ee-39ee-b680-6d7eb3e63a84 | -7.86211 | -63.7701 | 2026-08-23 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75b12fd2-db86-35a4-9609-489bf8706287 | -6.55057 | -58.53248 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a624b55f-fe50-3ce7-873e-7182d0276e1c | -6.69736 | -58.72263 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf0c12e5-a970-306c-9aa6-947a359ad6f3 | -6.75831 | -58.65602 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fffc1998-f11e-3cfd-9d13-069082ad8fd7 | -6.94176 | -59.06647 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6b1e980-5219-3970-bf4e-971b3688aba5 | -8.40148 | -62.69471 | 2026-08-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 541eed40-6183-3fd1-83aa-2d49592661af | -6.95661 | -59.06874 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b3179f24-28fd-3802-bc65-517150fdf6b7 | -6.94101 | -59.07209 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dc0eb52e-cd00-3cd4-9b0a-356474bbbb68 | -7.43427 | -59.78943 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d05eaa00-d294-3214-9c91-2a34ae411d27 | -9.23237 | -60.39027 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45187c67-ad2f-33a8-8d1a-eefc216d540f | -6.76495 | -59.47085 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| be79c646-5c34-338c-b471-4ba3d1ea31e5 | -6.80237 | -59.65713 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4bd3e445-27af-3faa-af1f-28b10726f3b2 | -7.68665 | -63.33647 | 2026-08-23 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5a603e48-f728-3cdb-823a-faa40d7c2fce | -7.50176 | -60.07595 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c41d74e-d49f-3594-bc8a-9fdf021e9afa | -9.17653 | -58.33363 | 2026-08-23 05:50:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb455d09-804c-32e5-a728-e090bb6353fb | -8.53194 | -54.81894 | 2026-08-23 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59618a23-214a-3c2c-8811-641906bca80f | -6.86139 | -59.4119 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 87d9f773-46cd-383f-bc78-605b6577d64b | -6.83906 | -59.9586 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f225221-b78a-3173-b764-a747a09bec06 | -7.67817 | -61.12041 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6f869d1-b2c9-3e81-b322-cac86d7b09d0 | -7.10802 | -59.77892 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e3c7483-3de5-3f1d-8e01-503548cef595 | -9.19479 | -59.44617 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2bec493d-8260-3f59-9f75-73375dda4023 | -9.14125 | -65.95329 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ba9d66c-e110-3142-ae80-2207742ba743 | -6.81037 | -58.64238 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5577de9e-9ade-37e8-b9c0-422506d54a56 | -6.95241 | -59.06244 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8e61f5da-6269-35d0-b4a1-9b5535d7df1f | -6.71168 | -58.73091 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bbd78257-ace4-3be5-a1f8-df32ac977782 | -6.77274 | -59.45076 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba7fd84d-e97d-341c-8e98-8ddb49c61dea | -6.96156 | -59.06945 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b5fb65e0-9c00-398c-8b3e-d38fe3181301 | -6.6911 | -58.73073 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d9f8bb5d-7ea5-35f8-9f0a-6533e1818b67 | -9.40592 | -65.94401 | 2026-08-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f1bc34e-c040-3b3f-a656-17189eb11bb5 | -8.70947 | -62.89534 | 2026-08-23 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a964bef-a632-391b-a4f5-5e7493da0f48 | -9.16263 | -59.45904 | 2026-08-23 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 376a62fb-8e69-3dcb-bf7c-5e909ac310a7 | -6.96882 | -59.05334 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a9d3ece0-0220-3dcf-9780-995a145e749f | -6.7973 | -59.79548 | 2026-08-23 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9311b894-c659-3840-b7a3-49b9525877be | -6.76383 | -58.65368 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd1ad3fa-44b3-3907-93f5-349d118cc063 | -6.84039 | -59.94902 | 2026-08-23 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e99bdd0d-f7a9-3048-b5a0-4d1fcf9e8279 | -6.69614 | -58.73154 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17664859-ab8f-37da-a714-b29b58d12b33 | -6.67476 | -58.73728 | 2026-08-23 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |


[Clique aqui para ver as próximas entradas](README67.md)
