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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74bd2394-7ccd-30d2-a88c-4f7c5a736686 | 0.9569 | -60.5233 | 2026-02-11 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 632094a9-603e-3f22-9239-f78a3da41613 | 0.9569 | -60.5233 | 2026-02-11 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 691a4bfa-37ba-35e7-8d8e-edc0324f3178 | 0.9569 | -60.5233 | 2026-02-11 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 1835685e-8081-31da-8c97-d0dd58d50530 | 0.957 | -60.5043 | 2026-02-11 00:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 30.6 |
| ceb2b2be-f883-350a-b396-0fbd3015f45e | 0.9569 | -60.5233 | 2026-02-11 00:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 30d62f74-b88b-3bc1-946f-84bcec0ff063 | -17.8399 | -40.0536 | 2026-02-11 00:40:00 | GOES-19 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 99.1 |
| 0ef479e7-b756-3a1c-b85f-2cb4d8b9be5d | -17.8594 | -40.0741 | 2026-02-11 00:40:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 178.9 |
| b18f45f9-3b23-3688-b067-5fa1b8034c86 | -17.8391 | -40.0798 | 2026-02-11 00:40:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 217.5 |
| d0b66132-c280-3c13-8bd0-cf719b22fa7b | 0.9569 | -60.5233 | 2026-02-11 00:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 9d1eba71-fb45-36ed-813f-0fe76951c174 | 0.9569 | -60.5233 | 2026-02-11 00:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 31.8 |
| f4f864ec-cf00-3182-b95f-ab66229882a4 | 3.6234 | -59.9188 | 2026-02-11 01:10:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| acbf6f95-1f94-3efd-9e3d-ad522e384811 | -16.58055 | -58.22165 | 2026-02-11 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 35f1c335-76d1-31aa-b6ce-254c194ee9f3 | 2.7135 | -60.83208 | 2026-02-11 01:28:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 16.2 |
| b3f8a963-46ee-34f2-820b-8bc2d151e5f2 | -10.173 | -36.7002 | 2026-02-11 01:30:00 | GOES-19 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 8860753f-fcd8-3132-a59d-8254fc849c64 | 0.9569 | -60.5233 | 2026-02-11 01:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 929c7193-e773-379a-8b3e-c772b53c822f | 3.38584 | -60.66358 | 2026-02-11 01:30:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 13.9 |
| b21632b9-f046-3b4a-8141-178cc602ac48 | 3.3913 | -60.65783 | 2026-02-11 01:30:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 14.5 |
| ff248dc2-c316-3ab0-8b7f-ae64e30c8555 | 3.67175 | -61.09255 | 2026-02-11 01:30:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 743c34bf-8cb8-3b6b-afdd-85264111c22e | 0.9569 | -60.5233 | 2026-02-11 01:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 110bb52b-cef6-387f-83a5-c7ffb8c95566 | -11.62478 | -37.62067 | 2026-02-11 03:17:00 | NPP-375D | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 569f24b1-3965-3915-bc2d-0cccf4450e15 | -11.62415 | -37.62393 | 2026-02-11 03:17:00 | NPP-375D | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 49f216c9-77b0-3fd3-af85-4bba068b23e5 | -14.83874 | -40.82928 | 2026-02-11 03:19:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 78779d46-a328-3212-8475-885b4eb4a751 | -14.83779 | -40.83175 | 2026-02-11 03:19:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 84fc0813-947d-39d7-9ea4-98215a4f13b4 | -8.69101 | -40.91913 | 2026-02-11 03:19:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7c07d1e0-07c3-304e-a513-65c88a21e02e | -14.83765 | -40.83435 | 2026-02-11 03:19:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4a67d49e-df35-3581-b42c-478b6a042b85 | -9.90716 | -36.37632 | 2026-02-11 03:19:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d46fdb5e-197a-313c-90e4-9af25e5d6fb0 | -8.69225 | -40.91292 | 2026-02-11 03:19:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 573f0c9f-4c1a-368d-87f1-c49f44ae2014 | -9.90219 | -36.37533 | 2026-02-11 03:19:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 73426a3e-826c-36bf-aa3d-33245c1eb95b | 0.9569 | -60.5233 | 2026-02-11 03:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 5d477974-296e-3f2b-ae09-940394b8bcdd | -12.12826 | -38.21084 | 2026-02-11 03:38:00 | NOAA-20 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| df19a87f-37d2-3bd0-9530-320a78c92848 | -12.08372 | -38.09254 | 2026-02-11 03:38:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8e7d47a2-14cd-380f-8a4b-5d39b5352b1a | -8.5511 | -36.61123 | 2026-02-11 03:38:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 021f34cc-1870-3bf5-bb07-9745b98b6af1 | -10.01068 | -36.18797 | 2026-02-11 03:38:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 20ed48bf-54bc-34fa-bade-27c044f35119 | -10.01407 | -36.18853 | 2026-02-11 03:38:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| e49e81a3-3f4f-3c93-9bf9-7b39bb7e7f83 | -12.08223 | -38.0908 | 2026-02-11 03:38:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 66a53725-cc8c-3b37-acaf-45b78d0afab4 | -8.69135 | -40.91343 | 2026-02-11 03:38:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5d7cec36-de52-3527-9491-adf97dd98411 | -7.77708 | -37.19884 | 2026-02-11 03:38:00 | NOAA-20 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ffeb4263-5898-398e-97b8-7b9ea6dc571f | -5.17993 | -39.74326 | 2026-02-11 03:38:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e3fd0457-9f97-3cc2-b6c4-23f63e7b941b | -11.07616 | -43.34628 | 2026-02-11 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88103254-a696-325d-b2bb-adea939c5317 | -7.77515 | -37.19749 | 2026-02-11 03:38:00 | NOAA-20 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 10f8e53d-698b-3c9f-a7c9-345a4bb3e2a7 | -5.18053 | -39.74221 | 2026-02-11 03:38:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 202a5046-4056-3ae7-b543-7e62466016d2 | -11.62162 | -37.62171 | 2026-02-11 03:38:00 | NOAA-20 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| eb5ea336-4545-3d54-91f5-b70b8cb545e0 | -7.78015 | -37.57047 | 2026-02-11 03:38:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ad3be8ae-69b1-3342-a177-e815b7f9cd5a | -8.16876 | -34.95147 | 2026-02-11 03:38:00 | NOAA-20 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 162e0f2f-4d96-3ac2-9364-29b0f423ecf8 | -11.82516 | -38.24955 | 2026-02-11 03:38:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 79d87824-de3e-3cf0-b50f-2a96cf089666 | -6.18606 | -37.94044 | 2026-02-11 03:38:00 | NOAA-20 | ANTÔNIO MARTINS | RIO GRANDE DO NORTE | Brasil | 2400901 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 26d06ad6-cfd3-3725-adec-52e56726a20f | -11.62515 | -37.62231 | 2026-02-11 03:38:00 | NOAA-20 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1a42e515-6ac2-3a5a-8e16-860f35414929 | -10.11641 | -42.16982 | 2026-02-11 03:38:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 752e082b-1466-3403-9e57-8d8122c79e9c | -9.81214 | -38.1068 | 2026-02-11 03:38:00 | NOAA-20 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7e651344-12d5-3f8f-b449-7edee6973e06 | -10.01128 | -36.1843 | 2026-02-11 03:38:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 15457b3c-d392-3b4a-ae26-c4b30f7e5748 | -10.13251 | -42.16219 | 2026-02-11 03:38:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5c570f80-704e-3319-8346-5863a85e56bb | -11.07672 | -43.3433 | 2026-02-11 03:38:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a5652e8-e2be-3d25-914d-9c0fef2c5758 | -11.62126 | -37.62242 | 2026-02-11 03:38:00 | NOAA-20 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7a057055-8129-3d45-9fc2-f67b172a69eb | -10.01467 | -36.18486 | 2026-02-11 03:38:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 012b04d1-b179-3705-b1bc-5dc8a47b1702 | 0.9569 | -60.5233 | 2026-02-11 03:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 9089f601-7078-3aa0-bc04-86426d600b60 | -15.31501 | -39.50609 | 2026-02-11 03:40:00 | NOAA-20 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e139d0b3-ad39-30e2-a7c2-7864f34af070 | -15.42071 | -41.43737 | 2026-02-11 03:40:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 9a3f4caf-2f00-3411-9763-38f809da8457 | -18.47237 | -39.73269 | 2026-02-11 03:40:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 278bd373-f65c-36d7-b837-662412ee4a92 | -15.91193 | -39.17731 | 2026-02-11 03:40:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fbe97683-d3ed-38dc-848f-3a60bbed8b92 | -12.48375 | -43.78769 | 2026-02-11 03:40:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c79e52c-a0b7-35bb-8daa-df7ff32ac578 | -14.83653 | -40.8317 | 2026-02-11 03:40:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 12db5fec-7c2b-33e8-bbd2-1b6ca776037e | -29.77371 | -51.17748 | 2026-02-11 03:44:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 4.4 |
| 25bcda37-e6f8-3309-970e-493e67cc99d5 | 0.9569 | -60.5233 | 2026-02-11 04:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 39.1 |
| ea9f51a8-c753-3ef8-b7e8-d7c5aa77ebd9 | -3.0166 | -41.83536 | 2026-02-11 04:25:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f4d827b1-691f-3534-951b-db29e19b6236 | -4.87786 | -39.04463 | 2026-02-11 04:25:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1416a685-4049-38d8-b75b-555761870666 | -5.66131 | -39.39779 | 2026-02-11 04:25:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2e86e1aa-c1f3-3993-8ff5-8c80ea122496 | -4.87809 | -39.04107 | 2026-02-11 04:25:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 29a1b57e-b73e-3783-bd20-7ab3df63853d | -11.0757 | -43.34157 | 2026-02-11 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ffe0b87-a773-355e-8552-4714c6865bda | -7.77685 | -37.19862 | 2026-02-11 04:27:00 | NOAA-21 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 52a818c4-b696-3d3f-8642-2ecd3d50be1e | -8.69157 | -40.91096 | 2026-02-11 04:27:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e24f9a70-f31b-3a1a-8b45-f48aea360aac | -10.11786 | -42.16693 | 2026-02-11 04:27:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5db2be46-2d55-3c2f-90a7-8aa5484e1b88 | -10.13549 | -42.15857 | 2026-02-11 04:27:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| df4b97a9-d01b-32fc-94eb-de9e855a414d | -5.66749 | -47.50515 | 2026-02-11 04:27:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| e4a4dfa6-d254-3089-8715-e4fc12f92523 | -10.12188 | -42.16751 | 2026-02-11 04:27:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 59b36844-fd6f-3241-bbc4-85f72759ebd9 | -8.69099 | -40.91502 | 2026-02-11 04:27:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 30a0ab9e-8d54-3566-9db1-6a48afe5f5f7 | -11.6227 | -37.62193 | 2026-02-11 04:27:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ec6c21dc-d77c-3906-8959-42867c811a87 | -11.62315 | -37.6181 | 2026-02-11 04:27:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 24195340-34e4-393c-a281-8e67d609eafd | -11.07512 | -43.34417 | 2026-02-11 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 684e3e59-f5b5-3bcc-85c7-36b293a0bca8 | -11.62446 | -37.62016 | 2026-02-11 04:27:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 41feb91a-8fac-3d52-ad80-2a2acc890af8 | -5.60457 | -46.3537 | 2026-02-11 04:27:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 631eac9b-79db-3da4-8123-ef1e327c0b22 | -10.01029 | -36.18147 | 2026-02-11 04:27:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4d3e8347-f2fe-3f0f-b223-2ec5173a496f | 0.9569 | -60.5233 | 2026-02-11 04:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 04b02bca-aeb5-3c01-9dae-2f8a7e204243 | -18.97637 | -52.92984 | 2026-02-11 04:31:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4bc136e0-bb6d-3fbe-96c2-2dba6341f34e | -18.89611 | -56.05402 | 2026-02-11 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| ff97520c-fd17-3129-b141-771b607b8b58 | -20.23853 | -53.01619 | 2026-02-11 04:31:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17d2d0a1-9aa5-3054-b829-c481518f1bff | -24.50818 | -49.97794 | 2026-02-11 04:31:00 | NOAA-21 | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f8643417-0dde-3e74-8699-f3b68b09a8ae | -20.02785 | -52.17914 | 2026-02-11 04:31:00 | NOAA-21 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a84cd797-36ec-32d0-9de0-51c159a9b22d | -20.86356 | -56.04655 | 2026-02-11 04:31:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| caaf2a09-e091-34c3-af28-f3fbb43a3520 | -18.70556 | -54.9842 | 2026-02-11 04:31:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bed14d4-8aeb-3995-b4cd-cf1d0a41337f | -20.72999 | -55.15384 | 2026-02-11 04:31:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f84e5658-6013-3bf8-a575-47e219f5280d | -18.7007 | -54.98734 | 2026-02-11 04:31:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce16e2bf-fcfc-37a5-a4a0-423aa3aad04a | -18.89565 | -56.05596 | 2026-02-11 04:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 284388d7-f2d8-3c8c-bc08-bbc140d6c388 | -20.72927 | -55.1576 | 2026-02-11 04:31:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fc5e47e-f843-3a89-b403-8d50e008f64c | -18.97273 | -52.92912 | 2026-02-11 04:31:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e2277e5-a9b3-3918-a6d8-34760001bba8 | -20.72527 | -55.15673 | 2026-02-11 04:31:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e327c40-147d-3127-b71e-ac09ed7f6060 | -20.86779 | -56.04741 | 2026-02-11 04:31:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c17d0e7f-fc94-37dc-9f99-33a47356550e | -27.48615 | -50.55175 | 2026-02-11 04:33:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f6ab9c60-f6ec-37cb-af58-d3fcc41b5450 | -27.48948 | -50.55237 | 2026-02-11 04:33:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 61212de3-3029-3c3b-9d67-27cabac322a5 | -30.95584 | -54.06059 | 2026-02-11 04:33:00 | NOAA-21 | LAVRAS DO SUL | RIO GRANDE DO SUL | Brasil | 4311502 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 2b69583b-70d9-3459-bfd9-979bd2d64982 | -27.10245 | -50.52629 | 2026-02-11 04:33:00 | NOAA-21 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README2.md)
