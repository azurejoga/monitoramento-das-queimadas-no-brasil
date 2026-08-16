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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5df4e4c-de62-3e07-8760-aa7dcddf18df | -8.9639 | -60.53244 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e7ca05f6-6cb0-32c1-88cc-ed0daee89dff | -7.58556 | -61.20861 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8e4b8c1-040e-3080-9b77-9c30cca90024 | -9.97855 | -53.9419 | 2026-08-16 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1363f427-36c3-3a7b-9a69-7b218b9267b8 | -8.97492 | -60.51783 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 898dbb6b-51ba-3b94-8f24-55e1c39185e3 | -6.96433 | -59.28092 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90c4ca89-9591-32e4-b789-5990323c20ad | -9.35041 | -62.36991 | 2026-08-16 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9696a5bf-fe9f-3c40-9f39-3d85bfecc010 | -6.84993 | -59.10116 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb71c3eb-c160-3100-9131-5580657ffdc2 | -6.59669 | -59.12178 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8b923cfd-7519-35d9-9508-fa11790e61fd | -9.47154 | -60.55041 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11426b81-5592-3df7-a673-162b9a9792a0 | -6.61024 | -58.98079 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db805c73-5918-318b-b201-749b07cc95c8 | -8.90238 | -60.56248 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 508127cc-371f-3781-993e-d49d8bbc015d | -8.96916 | -60.52137 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 97197ec1-161c-3013-90ec-fe494ddfdfd2 | -8.90348 | -60.60215 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdacc7a1-e97f-30bc-be21-2e842da7ba5c | -7.0647 | -56.65376 | 2026-08-16 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbb68dfd-1d4a-34e2-acb9-87e12ab39252 | -6.59922 | -59.00286 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc1d3652-33d6-3cad-95fb-d3ad190df362 | -7.58612 | -61.20502 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05ffcea2-9fa7-3cf4-a3e6-8317d2574c16 | -6.70016 | -58.95504 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 320a1786-6f9f-385f-9da8-6e43fcc34709 | -8.9516 | -60.56616 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87d25d93-c943-30fb-84fb-4d3965c3078e | -9.54329 | -56.80116 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9533ce6e-d321-3d5a-ae8a-79a69b3559ba | -8.90297 | -60.55863 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 962f22f2-56b2-3556-b4ea-ad9fd7b6a625 | -7.46282 | -55.30719 | 2026-08-16 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5f2bbcf-01bc-3dcc-b74c-5096014e6f7f | -8.94887 | -60.51427 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5364cba9-a7c5-309b-9fd8-687d0bf05281 | -6.70448 | -58.95126 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b453d48-ea7e-3386-a787-d490702868c0 | -8.65821 | -54.73554 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b9f4b7fe-a753-3c8e-afeb-f382d1e5c738 | -7.58445 | -61.2158 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70f8fac8-a936-39c4-85e5-d3fe6c218e14 | -8.95745 | -60.55122 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8eb37554-77c1-30b5-b275-85cddffb82bf | -8.90008 | -60.55422 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3f1609e8-8b2d-33ef-b9b1-5dbe10e1949d | -6.63271 | -59.0797 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9603df6a-0383-367a-889f-cc88009f3ce3 | -6.85951 | -58.9627 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e02f77b9-7537-3647-90d5-6c7962a0fb0d | -8.96568 | -60.52083 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bfe2a409-bf5c-317b-8fd3-4a250c53456f | -8.96857 | -60.52524 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e96857ca-836b-3e2f-b5ab-26fbd3aad8df | -8.95991 | -60.512 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfce496e-347d-3ef2-bc99-5e08331f71e0 | -9.1966 | -60.28859 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b969c822-24ee-3d84-b662-f3873eff5694 | -9.19671 | -59.66916 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6badb9a-6192-30bc-874b-720397cabdd8 | -7.55407 | -61.17784 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3ce43bc1-11f4-310d-9db6-02321092aa8a | -9.37014 | -57.3629 | 2026-08-16 05:36:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cabc21b3-054a-3f26-9a27-01c17a32e89b | -6.62434 | -59.06112 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c762a1f1-350f-3912-83dc-22e660c1d141 | -11.21555 | -54.82379 | 2026-08-16 05:36:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6beebdf0-dbc1-3358-8f4c-faccad0dc57a | -8.89829 | -60.58949 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4eb7558c-dde3-343f-83d9-c4d697b97124 | -8.64981 | -54.72285 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb81ac44-aa56-34e4-b954-5a478232dc19 | -6.62417 | -59.08702 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e84dc952-80d0-3ece-b80f-f5ebb166d3f2 | -8.41149 | -62.66 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e268a09e-e34b-3821-b6ea-366771a63fef | -7.42168 | -60.02959 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edd9b00d-51c9-313b-8330-27446a72e41a | -6.72114 | -58.94043 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 085a15a5-443a-31c1-8572-a41703406cdb | -8.90063 | -60.57405 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5fefef7-9ba4-3822-a2d0-3aff42a980f5 | -6.61959 | -59.04317 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55b54522-ce90-31bb-b627-b815b4fb72e7 | -8.90235 | -60.58617 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b7bfce44-726a-3981-9e0c-90088f57d89d | -9.2716 | -56.90579 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d43cfb5f-dcbf-3f9c-b20c-6e1409130357 | -6.61468 | -59.05107 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cbfa61a-4aa4-38e4-a180-9cfdba831999 | -6.95818 | -59.29704 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03166531-b3b9-329b-a25d-9f0e329dcf26 | -6.71315 | -58.94363 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf95bb4a-06ae-3bc9-b7fd-664774e805b2 | -9.1295 | -66.97494 | 2026-08-16 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 81c18b21-84e9-3716-9104-2cd94d6001ca | -7.42343 | -60.01794 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a86f454-022e-328f-977c-2fb9ff491d43 | -8.43818 | -62.6646 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e7af2ae1-403d-37ee-ad29-10ddf712942a | -7.33454 | -59.60136 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ba5e941-b986-3fa6-ac85-cf482c573fd6 | -10.57898 | -53.51463 | 2026-08-16 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 638ce9e7-4785-35ca-99b7-6ba93ad100cf | -8.96807 | -60.50531 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4a2dd0b3-6508-3f46-ae2c-ed07f7ae57d7 | -7.57724 | -60.87254 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3dfded5-8aa6-3412-acb3-d9b480103b8f | -8.2687 | -57.345 | 2026-08-16 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 347eef93-dcb5-3e84-bcf1-326a33555615 | -6.61047 | -58.97842 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7450919-a83d-383d-a12c-9c37deb9ac4b | -8.95931 | -60.51588 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 50ba5048-b7ee-3928-ace7-fd9cab0379fa | -6.72156 | -58.93438 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fe2f8085-4f33-3374-9c05-d16a9271c1b7 | -6.72613 | -58.93239 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c700c1e6-84cb-3968-812f-80e930675846 | -6.6248 | -59.08282 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8f20d5c1-009b-3fd5-8e16-7ee392a184eb | -6.88112 | -58.94379 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71c061f8-57dd-32fb-93e0-ed1b1bd22e47 | -6.62907 | -59.07915 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7e037b22-2fc3-3a1a-b8fc-120adbae25f1 | -8.25581 | -57.34684 | 2026-08-16 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 784d30ac-2295-3754-9876-9ad6025eb0df | -8.95694 | -60.53136 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0b258649-9f01-3449-903c-c125fc80d474 | -6.6226 | -59.04794 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe0b0790-6cda-3159-a208-d56289f7a80e | -7.38929 | -60.00144 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b94aa54-c7bf-36a2-bd7f-48dc7f3a98e6 | -8.97732 | -60.5147 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b71ac65c-8013-3134-b0c9-f94471d8ba84 | -8.97791 | -60.51082 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f513e0d2-e2c2-3f87-9540-f57c80c873f7 | -7.558 | -61.17476 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f839f09-319e-366d-b25a-378d9f6df571 | -8.97898 | -60.51448 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 25fd19df-ecee-3bf9-8d42-5c4e2b671677 | -6.7179 | -58.93382 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d841a63b-a18a-31e3-bbf1-3fa512c2100a | -7.34292 | -59.59434 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 561e5643-e0ce-3fa3-ab63-5e75bcc1e0b6 | -6.61832 | -59.05162 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5016e802-b4cd-357a-8148-8bead54207cf | -7.4254 | -60.02311 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 054aab43-45fc-397a-8d08-30d9fa4924b8 | -9.1405 | -68.20298 | 2026-08-16 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5816bc80-333f-3ce8-8d40-9ab7af23b27c | -8.64062 | -54.71592 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41afe0b3-3652-30af-9d3d-9165f44ad671 | -8.97086 | -60.5335 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 95ee337e-d1a7-3062-aab6-7a82aeda75a2 | -6.71726 | -58.93812 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e09c28eb-1671-360b-a48d-f56d9dcd51e0 | -11.22579 | -54.82513 | 2026-08-16 05:36:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52e9a2ef-df95-3c21-bc2b-0a346b813f9e | -9.42526 | -60.32986 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a2759d5-30ed-3ebf-b9c5-03cc6bd39f2d | -9.3753 | -62.36306 | 2026-08-16 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 64018652-a3cd-3b7b-beb5-1b24585059a3 | -6.62861 | -59.05746 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c1c902a3-b33b-34d1-abfc-dc71b88999d1 | -8.43158 | -62.68491 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 83c4441b-dc36-36c9-9e49-a24c1153cac7 | -8.98015 | -60.53053 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| feecaf59-1aac-3c5d-9138-3007f241893d | -9.19248 | -60.29204 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaa5005b-d2ef-33c8-98a6-6ac488fc7537 | -9.14412 | -59.64821 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f375f0ab-9c5d-3a42-9e40-e482094769e5 | -13.70778 | -51.88095 | 2026-08-16 05:36:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35fe7ffc-963b-3d89-a86d-e7a8da1abdb9 | -8.97503 | -60.50639 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| e8171167-518d-3d61-8e01-4a5e9b356783 | -8.96679 | -60.53683 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| da0f35bb-3aec-34ae-a753-d9b7728feb7e | -9.47682 | -60.53922 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f62423e-12da-3734-a05c-9b6efd03072a | -6.96072 | -59.28037 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34d5f426-4f9d-39a9-af77-522f69cb5ad4 | -9.0795 | -61.40028 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2cfaa5d8-97f9-3a7f-9c53-897c75cf2c9c | -6.86189 | -58.97186 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 97b38ef9-a996-3e62-aa0a-2a5bcaf2b012 | -7.42371 | -60.01087 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5c68c68-2e0e-384e-87d2-93119bcd682e | -8.97434 | -60.53404 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c6705569-7cdd-3ab0-b8a5-840acf0b47c2 | -7.42142 | -60.00245 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README54.md)
