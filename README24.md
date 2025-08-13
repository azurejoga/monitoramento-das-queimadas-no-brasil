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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f41c07a2-cf0e-3134-84e6-8663a810dbbd | -9.84596 | -47.82355 | 2025-08-13 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b55cb65f-8e3d-32da-96d2-94ae228af382 | -7.07305 | -59.20074 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 198c3489-f8b8-32db-bf38-8deaea690594 | -7.25831 | -60.63419 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2742e1ce-993e-3861-8a66-914aae542b9a | -8.11461 | -55.57324 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09fcea93-8467-366a-aaeb-bd75e396c063 | -6.87917 | -59.15468 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| caf2ffd8-da7f-3fd6-888b-085bf862141c | -6.90166 | -59.1321 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 11c05970-053b-3753-9df6-9d76f80e1223 | -7.06502 | -59.20377 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e810214-9dfc-3dcd-a940-d4bacf79b5b6 | -6.69147 | -59.13961 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c275272-0b08-3960-a9e1-a95d963ed5c4 | -5.88892 | -57.7476 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 090be603-04e6-3648-97e9-80af0278576f | -6.61709 | -43.88998 | 2025-08-13 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9b14e09d-e45f-37ea-a689-5f11e9ea3fd3 | -6.92929 | -59.14373 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3495ad19-2d28-3bad-b49b-759fd868b1bf | -6.92492 | -59.14742 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| d2947859-1e9f-3865-adbe-7553f4e650aa | -7.13496 | -60.12945 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4da160e8-6c91-3c23-b66f-3a067635a988 | -6.09318 | -59.93666 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 71d12425-c6e5-39fa-81bd-ca13db40dcc1 | -8.62581 | -50.01863 | 2025-08-13 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02735fcd-1e80-336e-b078-6eee857ea75f | -4.95809 | -47.60652 | 2025-08-13 05:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b12dc96a-a0c7-3db4-a741-e05868f39b41 | -7.25598 | -57.63591 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b89d8d11-84e2-3e92-aa96-1d44fb3ff917 | -6.10253 | -59.92821 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10aded29-86d8-39e8-a436-fb25e0f7b5a9 | -6.87536 | -59.13212 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9439d0b0-5f52-3f0d-86a4-095810ea4812 | -8.57363 | -54.71325 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac217244-c153-382b-bb00-532125fc8de2 | -8.89259 | -50.15488 | 2025-08-13 05:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdf5c362-0acb-3200-843f-ba931a58708e | -6.27742 | -53.633 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebe4e37a-1bf0-3244-b5e0-2bf8dcdb59f9 | -7.07078 | -44.93712 | 2025-08-13 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcd77853-f5f6-34ad-b7b3-7e47bdc8dc86 | -5.893 | -57.74443 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 426ce724-6836-3153-8dc7-546ab499a2bc | -6.10561 | -59.93362 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2a99d7bd-bab6-3992-8217-11af0222c63e | -7.03484 | -59.83065 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7fb77c7-3490-387c-b3d1-3bc8b4b12ae2 | -7.2592 | -60.62894 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 96a1d7ad-59fd-3bbd-975f-e56ff5c5d892 | -6.89155 | -59.14799 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.3 |
| b0e5ef3c-17f5-30ef-91a3-c94aa076ba5f | -6.91193 | -59.1382 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| e43c4d0e-6f48-33c4-81ff-18267abacd44 | -5.84753 | -59.92138 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c419504b-6734-3f0c-88e7-ee09786d27c3 | -7.26713 | -60.63037 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56cb7e10-c7cf-3ba7-a654-3e65f3f42055 | -6.8973 | -59.1358 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 339bd8dd-0cb8-3c4e-ad85-7137e72f3711 | -8.11074 | -55.5762 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 283f6892-faf3-3328-8a65-8a8107797a4c | -4.13065 | -54.89753 | 2025-08-13 05:06:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26c1ff2a-4bd8-3fe4-90f7-7e71ae06bf16 | -6.87761 | -59.14125 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 651b75ea-5a93-35a4-b9de-cfe6072b004a | -3.88292 | -54.21417 | 2025-08-13 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b5d8e2a-7af7-3b95-9f2b-af687f262a41 | -6.6178 | -43.88485 | 2025-08-13 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 86d492c6-c43c-35bf-a11e-d5c0027f19e1 | -7.46193 | -59.8861 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e2440f80-03b6-355d-b348-2be1ed1abad4 | -7.03446 | -59.82822 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff99c533-047b-3263-b705-0ad7fc5332c7 | -6.88703 | -59.12967 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9a9aed6f-455e-3d51-89b0-e62b5df07a1c | -6.89871 | -59.12717 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cb62e213-8eac-33ff-ac9c-c58763c406a3 | -7.27823 | -57.6466 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ef84d12-e43f-3405-b1d2-e75816554660 | -8.56345 | -54.68932 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a17ae8b4-9f5b-3148-9359-7c04b54f536c | -6.88789 | -59.14739 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.3 |
| a0407f05-9ac2-30e2-a95e-9005ba931bb4 | -6.07306 | -59.93809 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4a65069-20f9-3427-87ea-4873cb9df225 | -8.12123 | -55.55278 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe47e025-7fb9-3deb-bdad-fdd87a50e63e | -7.25256 | -57.63536 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0887025-57fc-3fe0-9220-592edadf5099 | -9.71846 | -49.47615 | 2025-08-13 05:06:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8e1c16a9-6846-3383-92b4-33c856d54785 | -6.7903 | -59.01508 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac45e81a-789c-3594-8451-bd1e3298817e | -6.87396 | -59.14063 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| d6c3d757-8a24-35e2-9740-cdb60e035310 | -6.92857 | -59.14803 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df1affe8-4f3c-3e43-a000-519175cc10ab | -6.97325 | -59.28795 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84f3eca6-9bb8-3112-a1f6-53358a78af97 | -7.13271 | -60.11922 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c4662e7d-23b5-30e0-87d7-89447b627c33 | -6.88563 | -59.13824 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| c02db289-0123-38ee-b438-e10b91a4cf56 | -9.37141 | -47.62668 | 2025-08-13 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f715e463-dc29-3cb4-bfc4-0d89977289ac | -5.85324 | -52.11092 | 2025-08-13 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df6949a7-0b6a-3275-ad3e-773b915d2541 | -8.12236 | -55.5673 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7e4d13b-e43d-3d03-b0db-b3a85f21f752 | -7.14042 | -60.1205 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d517961-62ff-3e50-bea5-32bd858d9957 | -8.11626 | -55.56275 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c207a7f0-0388-34c9-86ad-daee819f48ba | -6.11028 | -59.92942 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5a263f1-e568-333b-b95c-262220964707 | -5.88607 | -57.74329 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fd0b55d4-d037-3493-9062-d76f99f326a5 | -6.90967 | -59.12902 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8bd95609-ffdd-37fa-866e-31a103e0ea1c | -6.90236 | -59.12779 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 64b03ed6-8fe5-3acd-a44e-bb13315f59a7 | -6.89364 | -59.13519 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| c52ee8c4-fe8d-3c42-8dcf-7b5116805fea | -7.09165 | -60.02605 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d85b5022-8970-38e3-b33b-c315ea7fcda1 | -8.56287 | -54.67055 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02e9b5b4-3adc-3cbe-93c2-3d4e21bc451f | -6.90026 | -59.14068 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 7778288c-38e3-36c1-9ff8-0f5450aba308 | -7.13962 | -60.12528 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ffd08bb-fa54-3c8a-b9e1-badc718adb6d | -6.89591 | -59.14433 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 53b6f014-6198-3976-bdde-206888d44742 | -6.88999 | -59.13457 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 2e994881-db2e-328e-bd30-d507bdc21c1f | -6.90602 | -59.1284 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fb721bb6-94f3-38b8-868f-70f79df7ca3c | -6.61294 | -43.88787 | 2025-08-13 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| eb3e0cb4-8738-3fc5-b005-25d81788dbea | -5.84672 | -59.92624 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a380fd7-19b6-3e7f-8e2c-f3b669921aad | -10.34648 | -50.81203 | 2025-08-13 05:06:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03bb2f38-6698-34d6-be1b-e16762a93fa4 | -4.95971 | -47.59531 | 2025-08-13 05:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8048530b-605c-3017-a234-8d9537ddac61 | -8.56628 | -54.69348 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e3ab4fc9-48f7-3ef3-a0b7-e650ad39c657 | -6.87255 | -59.14917 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9254f180-d88a-3d30-b202-53774c260836 | -7.4621 | -57.65751 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e6d9919-a3b1-3c85-b64b-ed40ec3234df | -9.8408 | -47.82279 | 2025-08-13 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b21df360-d357-3966-89f3-ab7d14bbec7b | -6.91037 | -59.12472 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b87ad462-07c6-3c43-a0fa-a9659ef3d14d | -7.07558 | -44.94685 | 2025-08-13 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5d3d0a33-d983-3ca0-bca6-8f09cdf30c0b | -7.07675 | -44.93825 | 2025-08-13 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b7388c6b-0d72-31b9-8808-adc3ef6fa330 | -7.09856 | -60.032 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a57576e-c8c3-3c28-a97e-62fe3713d241 | -7.26082 | -60.00153 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5a61fde-e6db-390a-a768-fbfd8fe7ad66 | -6.10173 | -59.93302 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 51077ea1-7c43-377d-a212-2361e48c6ddb | -5.8539 | -52.10668 | 2025-08-13 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 678920c7-e472-3cb5-82ab-396a85479c4c | -9.70928 | -49.47473 | 2025-08-13 05:06:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2bf3dc53-4bc6-3656-88cf-2a9b610bbf8d | -7.25318 | -60.00027 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6ef0070d-b411-330a-8671-05e9063dd9f9 | -6.87901 | -59.13274 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a0510040-dd56-3f7d-bd00-404290d4d9dc | -7.07234 | -59.20505 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 531afa88-22e4-3e59-842d-3db322b61246 | -7.46494 | -59.89131 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f0bee205-cd12-38f7-95d9-06773582b054 | -5.85141 | -59.92203 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96ed25f4-8bc9-322f-8f88-c4ab404f9a23 | -7.48981 | -48.3818 | 2025-08-13 05:06:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e7f9c24-ef93-34a7-b16c-4a4be7738301 | -7.11783 | -59.84263 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72ec6d70-c5c6-3cd9-ac86-2871b30c37a6 | -8.11183 | -55.56922 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc33a2fe-8179-34aa-ac39-c1bf63617206 | -5.84957 | -52.11039 | 2025-08-13 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3c630064-dac8-3c51-9f1d-f680e205a937 | -7.076 | -59.20568 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| feddc28b-af64-3ef7-ab67-9d4da4cf4d72 | -5.85077 | -59.90202 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9232c6e1-97d4-3433-9b5d-133ea74506b5 | -5.85465 | -59.90262 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 676355a8-5ad7-33a9-8b8b-6fa26d08fb01 | -8.57589 | -54.72104 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README25.md)
