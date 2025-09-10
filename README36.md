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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d34960f4-e60e-3f2a-a59e-eb698912ba30 | -11.4431 | -43.59683 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 41d622ac-fd00-3f71-9adc-d0d57cba1ab1 | -16.28794 | -45.68309 | 2025-09-10 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c24ab7c6-da96-3366-85f4-e6f5550356a4 | -11.67327 | -46.90609 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9d793f57-ac96-3a20-bce8-9e16290d92cc | -12.05087 | -51.04444 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d26a6ed-d1a6-30fe-8b8c-6352947185d0 | -21.18952 | -45.1148 | 2025-09-10 04:17:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 231af279-af30-3e20-a327-deacb3f8432f | -16.57292 | -49.22359 | 2025-09-10 04:17:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a5915c9-227b-31aa-a396-327d13abd9ac | -15.27967 | -53.78259 | 2025-09-10 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9407f06d-7283-30ab-a871-36fe4f79e840 | -11.10889 | -48.37038 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c1c7900-43fc-3ea6-aa1e-8ad38817ec04 | -16.46012 | -51.97906 | 2025-09-10 04:17:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26c1ce0e-5081-3b62-a1be-e3168fe78f50 | -15.9323 | -46.3563 | 2025-09-10 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cca40dd-0d11-354b-b9cf-920ed0cdd4b2 | -21.16755 | -44.29929 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 241749e1-c041-37e6-b17c-98b252ae514f | -20.99559 | -47.99315 | 2025-09-10 04:17:00 | NOAA-21 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27a5c602-12be-3213-a3b0-2b5272add755 | -13.97983 | -48.23216 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31bcf444-ddf9-39d5-8022-dbac6cd0d938 | -17.85963 | -44.20528 | 2025-09-10 04:17:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc9270ab-d50b-3457-9c02-d6457497fa43 | -11.43911 | -43.71177 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e3d0366-7642-3af9-b2e1-b07c6250a34b | -16.46662 | -50.6645 | 2025-09-10 04:17:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f06ba975-de99-3218-96f9-5bf7df12698f | -20.38152 | -46.62845 | 2025-09-10 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fd7c5ecc-cb5d-3a7b-902b-35aa71bf8c47 | -11.11602 | -48.41895 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3b9bb48-d8c7-353f-a345-b9379a127398 | -11.41649 | -43.57086 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e5c3c2d-9ffa-31e7-9b57-4db289af5b71 | -21.39697 | -43.87235 | 2025-09-10 04:17:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ea339621-919b-3e73-95c1-c8f1990594ab | -16.03206 | -49.8389 | 2025-09-10 04:17:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0d250a5-9cdc-3f57-8389-80b877f44c98 | -14.85804 | -49.53592 | 2025-09-10 04:17:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2e0f8147-e73b-3fbc-b569-f7929e05d70f | -10.65525 | -48.6078 | 2025-09-10 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a197ca40-f988-33e3-b3c5-d9104ee7e5a1 | -12.13995 | -44.84668 | 2025-09-10 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33449081-a066-39ce-a784-d38bfd4839cc | -13.96731 | -48.23113 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eba95333-85c9-33d1-9995-e6727fccdb2a | -21.92249 | -45.63773 | 2025-09-10 04:17:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7f3004d7-da25-32fd-8954-70f05fa6b4a7 | -12.06603 | -51.06075 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e8c77ff3-2261-30a2-8319-d5e2cf65aa21 | -22.96821 | -47.03042 | 2025-09-10 04:17:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b103a663-4342-3963-8e8f-15243e76361e | -11.94363 | -51.08496 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66ec0f89-b354-3fa7-b857-d13755f8706a | -17.71306 | -44.43673 | 2025-09-10 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9101e0d8-ca1e-3ea6-b7b7-54366c6a6bc5 | -10.97621 | -46.79974 | 2025-09-10 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7cd24ef-6a08-355c-9531-078ef749e9dd | -10.73713 | -48.29026 | 2025-09-10 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5ef01b4-bf11-39cc-b37b-18a1e3046dc3 | -13.9291 | -48.25974 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 47d1bf48-121b-36c5-a79d-d9008134cd78 | -16.28407 | -45.68612 | 2025-09-10 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f8fb38b-2d02-3447-8263-7b38ec563cdd | -17.74899 | -46.16982 | 2025-09-10 04:17:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a4a0ea5-e58e-3730-bf6b-418d305017eb | -23.063 | -51.51718 | 2025-09-10 04:17:00 | NOAA-21 | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1d86b464-e689-309e-a501-a4485a3d2497 | -11.19334 | -48.37523 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f253b8b-eac9-3367-aeaf-23e433e297a3 | -14.35191 | -47.30614 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 980f33d2-e3ae-3bb1-8458-bd00e927b0ac | -11.38485 | -43.53313 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8589fe70-ba88-3072-bb77-c85c87360903 | -14.58226 | -52.11369 | 2025-09-10 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b629fa82-2511-3329-9ca9-1240a55e6714 | -11.45874 | -43.62804 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7a8ed863-5993-3c1a-854f-4bcd92a8033e | -11.49456 | -50.42332 | 2025-09-10 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1314fb1e-3ffc-36a2-984c-d7f2c9b69965 | -11.43209 | -43.62409 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f81fd445-0996-35ae-b78e-06bbdd0ffa40 | -13.3709 | -43.63612 | 2025-09-10 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 18d58e39-c886-336d-bddc-1afa9ea22728 | -14.3127 | -44.87394 | 2025-09-10 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad1c14c4-def5-37a2-acd7-5c37aaeb218d | -14.88754 | -55.86734 | 2025-09-10 04:17:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a70bdfc6-9ed4-3ddf-93ce-1300fa62c53c | -15.13233 | -52.39156 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f9afc3bf-f0d4-3041-92e5-27c74760f859 | -14.92411 | -39.84075 | 2025-09-10 04:17:00 | NOAA-21 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d6cd9c26-a346-362f-b93e-e5569ec30845 | -14.37539 | -47.31413 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9dbd3e17-89a5-3589-acdc-46087bce28ab | -11.75355 | -50.62941 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 529cc67b-d487-358a-8146-74d4b1838d74 | -20.55041 | -47.65694 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e5ed15e-3b6f-38cc-88dd-6b5829b7fcf3 | -16.68915 | -48.52981 | 2025-09-10 04:17:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62a47edb-54b0-33d0-bbd9-90e28e98e2f2 | -12.13776 | -44.83912 | 2025-09-10 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8a39e9c-2645-3b78-8263-f5211ba990e1 | -22.83271 | -46.43106 | 2025-09-10 04:17:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 01b33e36-c056-329c-a315-ae8c66d1e856 | -14.60034 | -52.10065 | 2025-09-10 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ced88423-19d0-31f3-90a5-8854f6b60a63 | -12.20766 | -53.89745 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ba93149-ea18-3e82-80fc-2a52f30f4860 | -16.84189 | -49.16975 | 2025-09-10 04:17:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1182ac6-417b-3aea-8a1c-0d3125b80bfb | -13.27821 | -43.75092 | 2025-09-10 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cac7d492-4566-33d4-85ff-097bcc8f08c5 | -11.48251 | -50.41694 | 2025-09-10 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98bdce99-e113-30e5-bb98-e704d7304800 | -17.50656 | -43.72671 | 2025-09-10 04:17:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbf24853-3f63-33af-89d8-bf6a032c7638 | -16.88643 | -45.75069 | 2025-09-10 04:17:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e11af5e-2f09-3592-aceb-a0541c8fe013 | -11.72663 | -46.70326 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afc95930-f382-3899-8a24-f71442b51de2 | -20.99161 | -47.99632 | 2025-09-10 04:17:00 | NOAA-21 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f90c4bc0-6335-3a1f-a245-6742e0bf01d0 | -10.00943 | -51.70267 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4c892364-da11-3357-9c85-2ef3ee63bc52 | -11.28898 | -53.94881 | 2025-09-10 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aeba0e24-a315-35ae-b01a-fb5e9950e76f | -12.07162 | -51.0799 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61d6e7c6-20f7-32c4-a465-1952ace96ccf | -13.02008 | -48.01764 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06e836d0-c4d9-39d3-b2b3-78cab8874a2c | -12.92239 | -54.76625 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d0fd5a01-0b5f-32c9-b7d1-f83faa4aa70c | -11.24353 | -49.4087 | 2025-09-10 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fb235a50-2e74-3142-98a7-34ed2226354a | -11.6384 | -46.62106 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0505e167-3fd5-3f1d-af6b-7d958de3ba6f | -11.43646 | -43.59578 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8031ed3-f07d-3cc0-a2e2-9412ec9d6b2a | -10.00461 | -51.70214 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b937f34-fc57-34ca-90da-768ee6ae5ff5 | -12.00392 | -50.97871 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bd0bc1f9-5377-3287-b4b3-cc46be7674c9 | -15.60846 | -52.75339 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 203a5883-12c0-3010-b22b-2c12b7eb6018 | -16.462 | -50.66731 | 2025-09-10 04:17:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3c697a25-05fe-35f3-9554-1fbb9cb6699c | -15.22855 | -48.24685 | 2025-09-10 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cc207c5-8c96-3c23-a18e-d61891d77e7b | -10.95594 | -48.14956 | 2025-09-10 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29120388-7d05-3031-b7a5-7739c792c8e0 | -12.88016 | -47.97282 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32933855-fbb0-36e9-ad16-2095d5d19f10 | -13.98039 | -46.65859 | 2025-09-10 04:17:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a978e2d-84a6-3988-97e4-2348e2754ab1 | -23.40808 | -47.2626 | 2025-09-10 04:17:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 24003150-a9e5-372b-b4cd-8124da480bd7 | -15.87669 | -52.19872 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c044c9f-fec4-3d6c-a8f3-8f718c396994 | -11.16021 | -45.27227 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 207f2c3a-897f-3d28-9421-a4746d452904 | -11.95226 | -46.65757 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a600217b-bab5-3aa4-87ea-6588d6b4367a | -11.45983 | -43.62096 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bea95573-69b4-3733-9adb-a85e2968eea3 | -11.13789 | -46.35159 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5154702e-19eb-3c12-832e-47f6a206d8ae | -21.67776 | -41.23975 | 2025-09-10 04:17:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f011fb68-0632-3d49-acda-a1a984465717 | -16.47458 | -50.66597 | 2025-09-10 04:17:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c35aeb4-ca6c-3da7-b79f-995a1317d229 | -15.22571 | -48.24207 | 2025-09-10 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1db7bdea-20b1-325f-b3aa-f34fa5cf92f6 | -11.42482 | -43.58306 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 200d4c35-b17f-37f2-91f1-0cbd240d692a | -14.37884 | -47.31468 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 263f07fc-4e15-36ea-8e50-26d621813c78 | -11.45658 | -49.26943 | 2025-09-10 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b87d4ec-3c31-3425-a55a-b7a5fa463181 | -11.45936 | -50.32532 | 2025-09-10 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e3cb1715-79b1-3241-bcf2-376158db4f8b | -11.32356 | -46.52602 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e28bdb75-21f7-3eb7-a33d-92e28b9c870f | -13.29126 | -51.72711 | 2025-09-10 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 63474d05-badc-3664-9118-110e02971bfb | -12.85422 | -47.97277 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8cd31461-b84d-3219-adf3-348054aa64f3 | -20.52287 | -47.63637 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dad39d58-eaec-3b66-bbd2-862ca856b186 | -11.14131 | -46.35216 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c1d5c8c8-6a84-3eb7-9ad2-990597ed6e5b | -16.4706 | -50.66525 | 2025-09-10 04:17:00 | NOAA-21 | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 01c9b90d-9651-3956-b99a-24e9acea998a | -11.55643 | -49.0425 | 2025-09-10 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b648b86-3335-3c96-baa9-6bf55061cd88 | -17.34108 | -46.72177 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README37.md)
