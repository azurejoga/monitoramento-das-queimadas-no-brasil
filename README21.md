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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ac8986f-2d74-3d9d-8785-d5bdd2aaf0bf | -8.89851 | -60.55389 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 855bc8e5-b50f-3aae-ac7a-6c1b027c036e | -6.863 | -56.42915 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c6c3908b-9e05-3381-88c4-b11041425d5a | -6.60212 | -58.98878 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c15b07b3-9237-3ddc-b6f5-55a577c503ca | -6.81394 | -56.46407 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10eca277-fae4-356b-a786-aa6ca930705d | -8.97506 | -60.52576 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e48bfcb4-1f01-3d10-8086-ab9de580999b | -11.80423 | -51.78659 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f003b3d-1de1-3fc4-b397-f4ee892f7579 | -6.53743 | -55.18257 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cac1b6f-10d9-34b4-b9a3-fd8c97855d46 | -9.37126 | -57.35931 | 2026-08-16 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ebd40925-eb0e-3a42-b12d-ab6c8e170def | -7.27976 | -44.7214 | 2026-08-16 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6b1ad12-afc0-3cc1-9f40-d8cdcc4e1f4c | -6.8196 | -56.46428 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b76bc4f4-3169-3fe1-ad39-a17a728b30d4 | -8.65849 | -54.73637 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e13cd23-9dad-3853-b028-b34d5d01b29e | -6.95809 | -59.28033 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e96015bf-4592-3221-98bd-22abe9818810 | -6.84921 | -58.97063 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bddde037-f073-3f91-bca5-4147898541e0 | -6.85334 | -58.9785 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a197f3f1-c13d-369d-8eed-93bab01982b9 | -9.27214 | -56.90612 | 2026-08-16 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2826437-9708-3d73-9bf9-63cf2e02c768 | -9.48198 | -51.64436 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cddf28f7-dad7-390e-a9ca-6f134a75d0b8 | -11.48454 | -46.59927 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fabb0038-eba8-34da-b80c-83c169075619 | -8.40866 | -62.66369 | 2026-08-16 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fad3f8e7-cb10-33ae-952b-8d048f3614f7 | -6.62043 | -59.04208 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b11b1ce4-56dc-3f61-b4e5-6db3a3e92cbe | -6.62871 | -59.05825 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c74f654c-ae85-3d16-9620-a89ad64c7fab | -11.06861 | -47.26446 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f8e8e45-7d9c-3d3a-8992-c8bed0ca962e | -6.61852 | -59.05273 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a560bdc6-f8a6-3e66-a754-827aed17f229 | -12.14806 | -50.15543 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 873fd051-e9b0-3c44-aa44-36209208c7c1 | -6.62457 | -59.05016 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 128a8ab6-b7ef-3c3e-996f-25b5e723f45d | -8.26497 | -57.34689 | 2026-08-16 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| abadefe5-91dd-37b7-94e0-75c99b70d040 | -6.82201 | -56.4505 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 32f855aa-e3cb-367b-b8f3-c1fcd0a85ef4 | -8.90528 | -60.57704 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 534af90f-bb74-30bc-b4a2-2803e7fef780 | -12.00704 | -46.42127 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5e30a64-b3f9-3c42-a3c1-a69166ec0cd7 | -9.54425 | -56.80345 | 2026-08-16 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3181a5d2-5c3e-3885-8748-1a285f7aef0c | -11.51488 | -54.63705 | 2026-08-16 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0191a6b7-5698-3252-b756-816a4a713dc0 | -5.68125 | -49.80769 | 2026-08-16 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e7554a2d-1104-3d7b-8a5d-31dd2daa0913 | -11.83153 | -51.95319 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 596dc637-8a8a-3295-8d0e-10665cb36228 | -6.9793 | -56.46527 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb277e6d-1451-3d81-85c1-3c622efd6fa6 | -8.94954 | -60.56702 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd7b410c-2a9c-37b2-96ed-d941d241310e | -6.60616 | -58.98535 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b10a75c-dca1-34cf-a961-852450fa4fed | -7.27348 | -44.67076 | 2026-08-16 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7201b9eb-c888-3680-9ea9-5aed45006347 | -8.96583 | -60.51172 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 317e39ac-394b-35b0-90f7-7f760acb4c5d | -11.46177 | -46.59613 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 52c6749b-acfe-37f4-9b6f-ed8bbbdffa0a | -8.89674 | -60.55873 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c440f417-f7be-38d1-a71a-8d94ccd1f174 | -6.62683 | -59.06881 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| deda9202-3c61-3f76-b7eb-387b6b59a198 | -9.49398 | -51.6128 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd0cdeb4-0f44-3dee-a140-40d504d1edea | -12.45942 | -46.67329 | 2026-08-16 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3450e2d-01f3-37b0-b46d-3f552ba3cf5b | -7.45999 | -55.30749 | 2026-08-16 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18bbd524-9fd3-327f-af11-3890df4c768b | -6.59733 | -58.98451 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b8f947e3-cf58-3610-9f78-b346122b89b9 | -11.21596 | -54.8167 | 2026-08-16 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7512880-af1b-35e0-bca1-a8a9ae3642fc | -6.71065 | -58.94025 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0fcdcd28-ffa7-3e9e-8142-5c0fdbe32c7a | -6.60816 | -58.98616 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63aa4275-9166-3707-bf44-75bbc919c797 | -12.01023 | -46.42675 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| c15fdd71-d7ce-3148-9015-1ad6b9e42327 | -6.83141 | -56.44321 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 524a421f-705b-32ef-900c-c81301611aba | -10.58043 | -53.51258 | 2026-08-16 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd93908d-e399-35ab-bb08-a9726eff91b4 | -8.89657 | -60.59212 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7f389498-af41-3570-abfd-b4dfed3cee7b | -6.7872 | -55.84146 | 2026-08-16 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab1130ae-94e5-3bc9-a505-faf004c22d4e | -6.71124 | -58.93686 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d666d753-4a57-3ed9-9e36-d56fd41367f0 | -6.31781 | -43.61166 | 2026-08-16 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a67ec6f4-7142-3376-afba-6ee76f136c51 | -6.59632 | -59.11409 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cad73977-b8cd-3392-ae47-930685fac722 | -6.82736 | -56.44659 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7b147900-91b8-31b6-8190-85387b1fd476 | -8.35314 | -45.97567 | 2026-08-16 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4606a2e3-525e-3c18-be05-c81d0219a255 | -8.9728 | -60.53789 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d8d96951-468d-3ad1-b842-844241d67172 | -11.87899 | -51.95732 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85faf664-3b9b-3d4d-952a-96e84e524746 | -7.64548 | -42.75425 | 2026-08-16 04:40:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ff614376-4689-3aaf-88e3-ec16e5fced71 | -11.88876 | -50.62383 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e83d5024-6bea-3995-861d-6ff70ac27630 | -7.40897 | -60.01936 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e6fb9ce-dca9-3eec-ab3c-d2db95d7e313 | -12.01592 | -46.44258 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 48aabb2d-0f18-3197-b81b-4a724d239ff8 | -8.54885 | -55.27818 | 2026-08-16 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a66865f9-0255-3178-a781-786fdfaa415b | -8.97306 | -60.50471 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 00290d73-ac39-37cd-af2e-3bf4594d8994 | -6.82282 | -56.44591 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 88bec905-2286-36e8-86a8-042bf59653c1 | -6.82002 | -56.45556 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 24ea96d8-c1f9-39ba-bab4-57dedd095167 | -8.65455 | -54.73574 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e52b0eab-5797-3d85-b62c-84f03dcc97f4 | -9.20714 | -59.67481 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abf57dba-752e-3d27-8147-968b108f9627 | -8.96133 | -60.53578 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 89770c04-03a8-325d-a8d3-ae35410d3cd6 | -11.09413 | -47.24231 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78a97536-d449-337e-8b3a-208a39417fed | -10.52175 | -44.85305 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf2ce94a-7b23-38ec-9ccb-09516f47f642 | -6.63039 | -59.08027 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 02b2e69c-861b-386b-a4e8-6f7d0679c7e9 | -11.07163 | -47.26932 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 75a8ee00-a602-3e37-a98f-3a18ccc01917 | -6.70532 | -58.93906 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ecda8802-9a1d-3785-bc57-a28d5a1b4b7c | -7.24095 | -49.88045 | 2026-08-16 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 936cc0a9-2527-3e5c-83c9-fe5656d04021 | -6.97717 | -59.01438 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cb167b7c-5f2c-3a80-ad6f-380aeb50d9cb | -6.63288 | -59.06627 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6e238afd-d80d-383a-acd9-ee3124317b03 | -11.76127 | -50.15221 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff896d57-1e3c-3966-a142-5a896db02a32 | -12.37625 | -46.43784 | 2026-08-16 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bd3090ad-0ab9-376c-916a-82f04376150d | -8.4153 | -62.66468 | 2026-08-16 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2939a257-9e54-36b5-88fc-de6bdecb7d5e | -7.35121 | -59.59369 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 72672789-b75b-3c5e-9e99-1f85d185f8e8 | -6.63061 | -59.04758 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21582889-c312-31f9-b9c1-fd53dd09294f | -8.46143 | -45.42511 | 2026-08-16 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c84de97-4d59-36eb-b19d-e4e381de0928 | -8.7982 | -47.9241 | 2026-08-16 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e34e948-82d3-3e6e-893f-76b6a2af6685 | -9.2978 | -56.81334 | 2026-08-16 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 262a740d-49a0-33d7-87df-cb9e9003edee | -11.51192 | -54.63181 | 2026-08-16 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5104926-7f07-3820-997e-964388bcad15 | -5.81307 | -50.18077 | 2026-08-16 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e7a6a16-fccc-3e3f-8b27-4445efc7123b | -10.88614 | -50.2936 | 2026-08-16 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4ba6db8-5b9e-3f2f-80d0-4ca1f358b1f3 | -8.96782 | -60.53281 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 739338e6-3bbd-3d28-9322-7b0d8e65f92d | -6.72017 | -58.93366 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0a09ba16-bfdc-33f6-94ba-613ef81f45e3 | -6.7071 | -58.96069 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 52d0dcd9-2e50-3a9a-a6f7-1d573842964a | -7.3925 | -60.00137 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f7dc453d-da1b-300d-b98a-bbb363f3fb6e | -6.59961 | -59.00267 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d72b905d-53f2-3f91-8f34-927efec02562 | -12.57632 | -47.8518 | 2026-08-16 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db06f921-1db3-3c6f-8a2e-b563fb8f79bb | -7.64483 | -42.75907 | 2026-08-16 04:40:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bfd06305-f057-3f69-9247-8a4fff54f2ca | -10.48519 | -50.38012 | 2026-08-16 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a334d66c-d823-36f8-b47b-0fa4785ce103 | -9.25339 | -56.90755 | 2026-08-16 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ab761d4-a8af-3a77-9ccd-a6dbf80d5b0d | -7.36827 | -46.86308 | 2026-08-16 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f4c1b5c-51c2-31b2-a648-906b5b49aa94 | -7.81539 | -44.10402 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README22.md)
