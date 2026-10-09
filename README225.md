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

## Dados Diários - Página 225

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbe8fdc3-25fd-3931-9f36-3315d02c72ca | -3.17 | -58.62849 | 2026-10-09 06:08:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 671a237a-960a-3f2c-8df2-7cf30654b0f9 | -3.0947 | -59.19347 | 2026-10-09 06:08:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ce0743d5-3643-3fa1-bc1f-4da4b1103eb7 | -3.73651 | -59.46083 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 99782914-7be0-3642-95fe-c81a85aa72cf | -9.25356 | -62.30497 | 2026-10-09 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e095243-38af-3620-be6c-4c6c6ed6e516 | -3.44977 | -59.54892 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 80709d84-8182-38a2-892d-1fa6f557ccfc | -8.84456 | -61.46877 | 2026-10-09 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ad26862-c8cf-3b47-b023-164417d2974d | -4.11676 | -59.87952 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbae58ec-6f1b-3c75-94a0-810f40d91d9b | -4.29293 | -60.9549 | 2026-10-09 06:08:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 935473b5-5e93-3db1-bb33-e98da9aa711e | -5.27118 | -60.18095 | 2026-10-09 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb48ec36-339a-3487-95b5-ba0cdee67753 | -8.84567 | -61.45995 | 2026-10-09 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b5d4757-40ce-34a4-95f6-b356cf1f48ea | -7.44527 | -63.55112 | 2026-10-09 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1de737c-4a20-317d-93e7-84e52e8b1e10 | -3.40026 | -60.84267 | 2026-10-09 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 108517dd-51ee-3c49-956d-033fc73e255e | -8.52114 | -67.02523 | 2026-10-09 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cf158ee7-003c-3e5f-8489-cdadd278c6ce | -3.74774 | -59.47306 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 181c6b2e-49b3-3bae-bf22-2f1b21e1f598 | -4.30551 | -60.94983 | 2026-10-09 06:08:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 440b786b-43d8-3b4c-98b9-2ec85d32fbf8 | -3.38619 | -59.43083 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 01fb5ddf-300e-3c6b-89b5-44ad452a3ba6 | -8.71179 | -62.4176 | 2026-10-09 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d8554c9-3953-3f2f-9c76-94049d457904 | -3.18093 | -60.39687 | 2026-10-09 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4d520f60-da96-39cb-b463-8f863bb4b6a4 | -3.08757 | -59.1977 | 2026-10-09 06:08:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3e72f229-e355-3bf1-9132-97fae3f6b44c | -3.73722 | -59.45571 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fc68920d-9d7c-30fd-8bc1-2edede3d02c3 | -3.48639 | -59.38351 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab3d40cb-3b27-3972-9e12-089d568f6b34 | -4.07239 | -59.8426 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5dad8f9a-8a85-3bf2-acfe-57f8082bf759 | -7.44487 | -63.55416 | 2026-10-09 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc7a8f1e-35f5-3f59-928b-d4e972e4b272 | -8.69542 | -62.41157 | 2026-10-09 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a3f9806-7b4a-3b94-8d7b-970c56a48b0f | -3.78132 | -58.59097 | 2026-10-09 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2ed57cc1-3f1e-33bb-9347-b8e050a1ce23 | -8.74648 | -62.62614 | 2026-10-09 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c7d7787-867c-3186-a9ee-4aa00e4e7240 | -6.99471 | -59.10462 | 2026-10-09 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd145054-5b01-370c-b7e5-daf108cd56f1 | -8.52523 | -67.02585 | 2026-10-09 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 752b83aa-891d-383c-8977-3f453fa7a7ec | -9.12087 | -67.82541 | 2026-10-09 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cd689b4-13af-373b-8b83-b371c77762a2 | -3.43793 | -59.54206 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef17b9c0-3644-3af6-a32e-70b0ea174a5f | -6.48797 | -62.85209 | 2026-10-09 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f3a03e0-f75a-36ed-9676-836acb64cd92 | -8.35483 | -62.82615 | 2026-10-09 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00a5a594-5e06-38c2-9a19-8eb22ea0fc57 | -3.78525 | -58.58782 | 2026-10-09 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c4c6bb4e-34fc-3530-8588-519a4c350276 | -3.63323 | -60.62907 | 2026-10-09 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19a78fe4-a955-36bc-b910-b044c76fb939 | -3.54195 | -59.40244 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 43324dcc-b048-32a7-9356-3739c5f67499 | -8.83858 | -61.46791 | 2026-10-09 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de3e4c5e-6ea1-3be7-af51-078cf6558394 | -3.78004 | -59.19445 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f17521dd-e86e-3d11-bc97-c15e428677fd | -3.59163 | -61.61449 | 2026-10-09 06:08:00 | NOAA-21 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed61fcb0-72b8-3416-bb64-d0b1ffb16c54 | -4.29233 | -60.959 | 2026-10-09 06:08:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dc5c62e-796b-337e-9c74-046f6908e7ba | -6.75009 | -69.71456 | 2026-10-09 06:08:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b261d9b6-4be7-382d-b480-c0713948ad96 | -6.84792 | -59.39315 | 2026-10-09 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4ef751b-3427-3b06-84ac-7263f7a670c1 | -3.39967 | -60.8467 | 2026-10-09 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b7e8c2f-a876-36d2-95d0-bd1068c42bf9 | -3.39489 | -61.07767 | 2026-10-09 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfe8e08d-343d-3447-9b48-dd00cb57441a | -7.50174 | -70.05284 | 2026-10-09 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab3e4f4b-8215-37d5-bed9-53534b5b7e2c | -8.70667 | -62.41298 | 2026-10-09 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8791c02e-381a-380d-934a-b78c3208e1d4 | -9.26133 | -60.88576 | 2026-10-09 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6905a501-1ec1-36da-8760-20a85adc7ce2 | -4.12295 | -59.88053 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80d088a9-713d-3fb5-be2b-35359fd0cf09 | -8.83969 | -61.45913 | 2026-10-09 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c6d871e-5c29-3a88-b74d-4e66f23fde40 | -4.06687 | -59.83683 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a5761cfd-1a39-3cc3-859e-b3dd22cca1f3 | -3.98771 | -59.35674 | 2026-10-09 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 56a7e330-c650-3a67-8972-acd16ce60ea4 | -3.59216 | -61.61084 | 2026-10-09 06:08:00 | NOAA-21 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc86b195-c0fa-383b-83ba-3e335c8f789c | -9.11686 | -67.82638 | 2026-10-09 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c59f141e-d6e0-3c73-96fa-df8a949fd5bf | -3.52681 | -59.34697 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 781bf44e-01c2-3eab-af10-745828414828 | -4.1219 | -59.89484 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f660d5cc-13de-34b7-8cf7-267f9bc6d796 | -3.77551 | -58.58405 | 2026-10-09 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39302152-08f8-3774-9ce4-9aeae28debac | -3.59659 | -61.61901 | 2026-10-09 06:08:00 | NOAA-21 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 580d8e31-ee7a-39a8-ab33-e259cf24d05d | -3.527 | -59.57611 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b3c8f0c8-897e-3fe9-a8a6-8de1eb56ad82 | -8.70619 | -62.41673 | 2026-10-09 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a419dd1-5e35-3d8f-ab48-08e7ecd296f0 | -3.15724 | -59.08915 | 2026-10-09 06:08:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 136c5533-2c35-3647-8b93-1480dda39549 | -8.70057 | -62.41598 | 2026-10-09 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ae2dc2e-1aef-3950-9690-ae5adb219928 | -3.49275 | -59.38434 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7efcc32d-4016-3f1b-8f56-130f4d47e8b1 | -3.7502 | -59.47927 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ed4c2e6c-a61b-3cad-bdeb-aef090399e75 | -5.22112 | -60.04862 | 2026-10-09 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0c438c7-f2da-3a4b-9dc6-4506cc116bd9 | -6.49281 | -62.85616 | 2026-10-09 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 010aedc6-f1e6-3b54-9899-685d66fe16c2 | -3.46521 | -59.25819 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3a6bde65-77b2-3f6d-ae5a-0953927e57f0 | -3.78219 | -58.585 | 2026-10-09 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 49afb20d-b6f3-3727-a0fc-cf10b7fd34c4 | -9.09491 | -61.01675 | 2026-10-09 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad5a4b60-3c36-3fba-8b71-56a44f5902d1 | -7.44666 | -63.55503 | 2026-10-09 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a52103ee-9176-3647-9100-fec7c802035c | -9.09551 | -61.01185 | 2026-10-09 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b656d43-1f06-344f-8615-60bcbd3ab7a4 | -8.5201 | -67.03258 | 2026-10-09 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 15ce5d88-4942-3348-9d92-5afd5ff02d7d | -7.44708 | -63.552 | 2026-10-09 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08adbcf5-7c31-3526-98ac-07adfc8aa02f | -7.44958 | -63.55794 | 2026-10-09 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73cae95e-4e0c-3f92-b68a-3b67a567d171 | -3.43166 | -59.54104 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b972cc88-32a9-3ff7-9e85-49d3c3003a37 | -3.17915 | -60.39497 | 2026-10-09 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c95a864-3adf-3b5b-8e87-2f33671a18a9 | -3.7869 | -59.37898 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 24041a76-0aa0-38d8-a5ee-f4474785e5b5 | -9.11695 | -67.82481 | 2026-10-09 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dcdea19-d8f9-3957-bd4a-453cd7068c93 | -6.99803 | -59.10049 | 2026-10-09 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c122fb9-7eed-3f91-93ad-816c673e47f2 | -6.84718 | -59.39899 | 2026-10-09 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d2c441bc-804f-37c1-a541-ff8070fe398e | -3.74204 | -59.44665 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d30687ac-6482-3ae2-b547-07f35c32035c | -3.43429 | -59.54125 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4aeecb0f-4360-301d-959a-73dc9457836e | -3.77463 | -58.59003 | 2026-10-09 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4565fd4b-7747-3a50-a85e-a2e8fba510bf | -9.20596 | -67.81912 | 2026-10-09 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 075dcd6e-2df2-3f1c-8427-c299f91a9c69 | -8.70153 | -62.40847 | 2026-10-09 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad85ebdb-c521-3699-a732-0adfb8e20d4b | -3.74063 | -59.36728 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4c1f05ab-7ed6-3320-a33b-3b999490d795 | -6.64136 | -62.90726 | 2026-10-09 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7ee3f69-60c7-3328-8e3a-f6cfed4dd995 | -3.71028 | -60.54183 | 2026-10-09 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a8d3e9cb-608b-3fe3-a085-1fd42099af70 | -3.53048 | -59.34797 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4d9d52be-dcaa-3e82-8e1d-07f9686cc4ad | -3.71802 | -59.65439 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0474c292-00ef-3eac-a613-338505c61d34 | -9.26196 | -60.88073 | 2026-10-09 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a452b5aa-dc03-36de-b663-7d5b29a34f65 | -6.67907 | -63.02403 | 2026-10-09 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4cd6ada0-2bbc-3b3e-a5b6-68e15768902a | -3.52909 | -59.57648 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ec12acef-f4b6-3188-a0e8-328f8171a85a | -3.52771 | -59.57111 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7ef46d7e-207e-3e1f-ac98-dbd297b05dc7 | -3.50279 | -59.26931 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1dce8f3-b8aa-344f-98f1-9c6cf8265eb7 | -8.34985 | -62.82189 | 2026-10-09 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f469dce-6538-35e5-8564-a39505b1d822 | -3.52984 | -59.57148 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5adf0716-a226-35f5-8cd3-3a836a4fbb78 | -6.08374 | -62.51093 | 2026-10-09 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 493129f8-855f-3a25-aaa7-cc3f7a9f8a0e | -6.48752 | -62.85538 | 2026-10-09 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93941e8e-d025-3f51-8c0a-95958c2f45ac | -3.17854 | -60.39929 | 2026-10-09 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 183f6af3-ed64-3aa9-a5bb-de86d01165ce | -7.44998 | -63.55491 | 2026-10-09 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 650123a4-fe63-32d0-b278-281c04fa8445 | -9.20775 | -60.8726 | 2026-10-09 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README226.md)
