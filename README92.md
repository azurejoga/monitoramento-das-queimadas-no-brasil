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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2354492-147f-38ac-b973-6de6b133b435 | -2.98775 | -54.11913 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c9ab5bf7-f1f6-3df3-8e3b-29cfb835028b | -5.69151 | -53.48381 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3ed1b8c-2496-3906-bfc8-9d775fb71e4f | -11.62706 | -43.69901 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3aa35711-d5e7-3a8c-97c9-c5ee9ed893e5 | -3.60373 | -54.56385 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fd15a3e5-e505-3348-a886-0d8fa3d56b4a | -11.63505 | -43.69891 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a2a4a1d9-bac3-3d62-b444-94e0a8fac427 | -3.24606 | -56.80272 | 2026-10-08 04:46:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb081d4f-9a7f-3282-bc38-098eecd0d50c | -3.27031 | -51.0696 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0fe7d615-507b-3ea9-a22e-b72efa579fcc | -4.264 | -46.39848 | 2026-10-08 04:46:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac8b815f-27db-3073-ab92-9f98ef4ac345 | -9.13366 | -46.66323 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c471978-68a4-3140-b1eb-d62d4f06aa78 | -4.36958 | -54.75098 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d2d22b1-1057-389e-96c2-44d0a350a35b | -5.48634 | -42.83672 | 2026-10-08 04:46:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 54b2838b-3be5-3e9b-a7ff-c4bf95335cbc | -3.02197 | -54.07062 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 57835758-e0b6-38df-a264-5010095c6ec7 | -7.10799 | -42.53225 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c8bfb19c-c3e0-3d39-bfb0-3e934e8c51bd | -3.58763 | -54.66504 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2d519a66-86ea-395b-828c-5db466c21537 | -3.5371 | -59.47335 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41b8aeb0-caa2-3cb2-80c1-73c1d8b7d627 | -3.28162 | -54.04195 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c65eb9dd-22e5-3119-ba87-2d4c8bb6ad2c | -7.38914 | -55.20794 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be288aff-f768-3727-9a5e-5a06b296126e | -5.99099 | -40.93917 | 2026-10-08 04:46:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 79adaabe-53cc-321b-9da0-b8711af7e14a | -5.29873 | -60.10041 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f01314d7-f4eb-3071-850e-bb0b5e2ca02d | -11.24182 | -44.87459 | 2026-10-08 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 658254d9-2e74-3d8a-88a5-8ae9e4d74a8b | -2.99825 | -54.05354 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b9a7115-5030-379f-b3e5-2b34675efed2 | -2.93824 | -54.17649 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1fb5baf1-84d5-3637-8dcb-8704f55aa462 | -5.30096 | -60.08724 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1912222-cb47-343c-991a-c4a1268f5794 | -3.26966 | -54.02242 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ed15d4c8-d7d2-371c-a955-8a26abed6a4c | -5.69559 | -53.48061 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3eadd111-277a-3cf6-901c-0e6135b131c8 | -3.59072 | -54.2407 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 42994474-5196-3e65-9f21-81b37889edea | -6.37839 | -42.53156 | 2026-10-08 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 11962895-7d86-3ffe-9c45-3c034c0b627f | -3.106 | -54.15425 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 641aa812-4dd3-35ce-9619-95d667f8d885 | -3.45039 | -59.82804 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 745d3f14-966c-381a-8d6b-6eacfc5d04f6 | -7.47342 | -42.84696 | 2026-10-08 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e9f11513-9bc0-3948-9247-81e5c04a18f0 | -3.51295 | -59.95094 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 985eef36-7a1c-3fb8-8b1a-d9c1d40c1a80 | -3.20976 | -53.88183 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68311c77-b53f-332d-8e06-2829d37ce913 | -3.72254 | -54.21502 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2569362-792b-3299-aee9-e1b99bf45f96 | -5.73865 | -45.15677 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bc8ccde7-4c29-3408-be25-92f3d032dbfb | -5.89553 | -53.50349 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9bf0aca7-9612-39ee-a818-ba27cb8816d2 | -2.89756 | -54.02619 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58b45522-14b6-3c4a-beff-cdbf91bf62d6 | -3.27719 | -54.04425 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2280fd55-a84d-34c6-a913-0f5b7b2113cd | -11.23467 | -45.24424 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb82de45-9010-3965-8e32-73052d6ba320 | -4.36342 | -55.64762 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40acabed-585c-39c3-b151-fdff66c18bfc | -2.93395 | -54.1468 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fe80339-0718-37ee-b138-1c3af0adedd6 | -2.99666 | -54.03993 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 573ffbf9-5856-3adc-8c01-581189ec8a72 | -3.98216 | -56.2187 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 66395d1d-c6e5-3cd4-b170-a885667e0228 | -9.40629 | -49.00808 | 2026-10-08 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d323bf7f-efe3-351f-b868-700f3dca495c | -3.11184 | -53.76788 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1248fae-9e2e-3e40-9c10-4558067bc920 | -9.37368 | -55.97144 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb50a6ae-4139-366f-bb03-38e440c0ab6d | -6.85101 | -41.76376 | 2026-10-08 04:46:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2399365f-5e7e-351a-bdf5-01a1c0c7732e | -3.59777 | -54.57703 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7d5c10aa-c050-3064-8f56-aa9a2dd7e9e6 | -3.01598 | -54.06076 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c2011435-bf21-348e-aa8a-69c2250a1104 | -4.27305 | -55.71171 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1350160-241a-35c6-8f81-76fa3800303f | -3.59546 | -54.56733 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3642d553-70ba-34d5-a402-9493e06345d4 | -2.78389 | -54.08098 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d8e42ee9-6a68-3b67-8fa6-2c764e3ec4c1 | -2.50057 | -56.12098 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03e508e8-edda-3fa7-aa8a-98903caa776f | -3.30931 | -53.86996 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 107d33db-7bb9-3697-b899-f7cdfbbeb411 | -3.25883 | -54.65705 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5afa8eff-0459-3233-b67b-2be5699121e2 | -6.15953 | -39.44326 | 2026-10-08 04:46:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 8b494728-6e31-34ba-86ce-435c07202555 | -5.25907 | -60.17261 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d49f33da-7bb7-37db-8e12-2c0c4a0c10a7 | -8.38065 | -46.28735 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41003531-1566-3fe4-b38b-a360ff571722 | -2.50226 | -56.16532 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 04788e5e-cdf4-35ef-ae10-915e67b8e210 | -3.50931 | -54.66904 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 469e0d9a-d13b-371c-a712-72cc3af1e0fd | -3.01054 | -54.75258 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fb0acd27-54b7-3575-8e65-aac41dc807b5 | -5.77944 | -52.36099 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5aeae92f-ba29-3bc2-8d32-089c5e4d438c | -8.22936 | -54.73415 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d913295-f37a-3d4f-8031-8928c14a0f4a | -5.82062 | -53.82831 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f0d8314-bdf4-323b-af0a-9595e2ac7a05 | -4.15997 | -55.14004 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 85e8006b-488f-3f23-8c78-df1dc95d96f4 | -2.97807 | -54.10862 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| caeed232-f85c-3a55-88a7-0ebb02f3e781 | -4.15219 | -55.13914 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 236af6b3-2829-3ec3-8771-cfeefc17ec23 | -2.82337 | -57.61 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73521705-7f98-386c-bd1d-1286091c4d7d | -5.75103 | -42.07136 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3ad22810-dc65-302b-aa29-bd51d72a783b | -3.64121 | -58.94073 | 2026-10-08 04:46:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1532153-7d1f-34ea-87fd-3c4c215dedba | -3.16576 | -54.0872 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e50e638-e73c-3c03-bbf9-f44821cb62fe | -8.21346 | -46.37724 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b26ad0c7-7249-391d-9673-72614de849d9 | -2.76186 | -54.10013 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b9600a1b-7cfd-37ce-ab81-14eca0846f23 | -11.22187 | -45.27121 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8a9582b8-7d57-33f0-a298-72e68a2dd4c6 | -2.87809 | -54.877 | 2026-10-08 04:46:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d82096cf-5225-305f-bdec-6686b5dc7ac0 | -4.29486 | -49.09106 | 2026-10-08 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fc5c4146-9f76-3088-860c-8e279728a5fe | -8.72768 | -45.187 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06fb6072-ad65-30cf-83bb-cb8c03149d44 | -3.51364 | -59.32666 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a887ca9c-bce7-3fb7-80ee-c5a9e23e5d5b | -3.02603 | -53.90327 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4181bdf-2dba-3444-a492-c9d7a3b169dc | -5.26395 | -45.4072 | 2026-10-08 04:46:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b0c6fd99-5cfe-3241-83e9-e6a1cf27181f | -8.73138 | -45.16061 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6d7c26af-142e-3b8b-89b5-9bbe2b762501 | -2.93755 | -54.18093 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c391641c-9e34-3616-968a-cd03a0ce5344 | -3.05457 | -53.91207 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 462e12f4-627a-326e-8b2b-2a487f6ab2c0 | -3.57233 | -50.35771 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 390af0f0-e648-3049-9742-d869d13c0aee | -3.68246 | -55.95285 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ecb8f0d3-d561-3c2c-9ef1-fac4b90249fd | -3.27692 | -51.07062 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8609285-4c60-3f96-a2dc-87e260f839e1 | -4.32644 | -48.63156 | 2026-10-08 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d708c8ff-9260-346a-92e5-88e3bf93ba8d | -3.03164 | -54.0811 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cdf93873-87b9-3646-b0a3-3961343eb128 | -6.32593 | -43.35586 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 24b3c6dd-f7e0-31bd-956a-8896ce13b824 | -7.03127 | -45.29552 | 2026-10-08 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35e75991-87c9-34db-abb0-5579aef40f76 | -3.0215 | -54.09742 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7688508a-9ca6-3279-9f44-ebe377e8bac1 | -3.86314 | -50.41394 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 550e79d4-6c98-3117-92b6-9d3957ce1fbf | -5.81646 | -53.83173 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ddd5f9a-9f8c-32e3-9faa-2672315827d7 | -3.98525 | -59.21842 | 2026-10-08 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57dda54c-e431-3623-9340-1351f6b11add | -5.27069 | -55.95522 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a937cd00-ee0a-3657-8520-da394c14d5e1 | -3.10006 | -53.74147 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab773bc3-f1d2-3a9b-8750-05a7e4193abd | -3.54226 | -59.50702 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5314f8f7-eada-385a-9645-c216b7ad10f7 | -2.93893 | -54.17206 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfb00b4a-bdd1-3a8f-bf1d-300e93c55ae1 | -6.03605 | -51.72627 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b0d0214-23f6-32fe-9c8c-8fa4635bbd1e | -4.69504 | -50.64346 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3144c82c-bc1e-36fe-85cc-96d2a45bc3eb | -3.73484 | -59.45331 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README93.md)
