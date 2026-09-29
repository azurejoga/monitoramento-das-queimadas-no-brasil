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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bd4f516-3e64-3cc1-bce1-a114672775be | -10.79726 | -48.75451 | 2026-09-29 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f61688ed-e167-335a-a3fc-295e2d847504 | -15.9578 | -42.95716 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be76be9a-2275-3329-91a0-9f494bcd3dcb | -15.86995 | -40.45628 | 2026-09-29 04:17:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| f17382a3-3fc4-34b8-85d8-a429f4101daf | -11.44197 | -43.46193 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1472592a-0807-3266-9722-945eb6620da4 | -9.82789 | -48.20633 | 2026-09-29 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2db284f-db15-3aac-97d5-371714bd7d11 | -12.93897 | -46.66786 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2b8261d-e6e9-39d6-b169-697257bf2969 | -15.45835 | -46.14706 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fac5c04b-a222-3442-a6cd-b7f3ad6b7939 | -11.64998 | -43.27754 | 2026-09-29 04:17:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 90b97775-1b70-3b25-b2e5-472fe0ca5b07 | -11.71093 | -43.45655 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c09db8d-0009-3384-bfd1-2346c12236fd | -11.45087 | -43.47061 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 352c85cd-40f3-387a-a548-f6ffa5084244 | -8.87965 | -46.19026 | 2026-09-29 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6050f86-4b00-37ee-9952-94967d5e8cf0 | -11.36838 | -43.36259 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb1ea32b-e22a-3485-98a2-2dc845f6c91f | -15.45229 | -46.14233 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f33c0013-cada-3c03-95db-3a0b0e0baf5d | -11.35081 | -54.04196 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f701fe28-3a85-3268-9073-ca6125855cb8 | -9.78603 | -48.22371 | 2026-09-29 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8064e060-1a22-3566-806a-dd847976542f | -12.27933 | -50.26731 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| edcd364f-ded4-3777-9072-46c4059387a2 | -11.44312 | -43.4767 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e065f7db-b678-3512-9f5c-38abd595f2cd | -9.96054 | -50.13665 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2cdb87ae-41b3-3b55-9dc3-5098baefa7f4 | -15.24937 | -43.27661 | 2026-09-29 04:17:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 1aa43b2b-ea80-3c45-b1b4-d457dfc07ac5 | -11.29383 | -47.67096 | 2026-09-29 04:17:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2fa7ccf0-4bc3-3da4-a882-6532b04a3ab2 | -11.43198 | -43.46035 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aeb9dd70-87f4-33a6-8305-054ec7a48760 | -10.81514 | -48.74255 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8f7f9b2e-2a5e-3c32-a789-aad1bf618211 | -11.34206 | -54.11785 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 812832dc-a126-3cb7-9194-420157877f75 | -11.41969 | -43.4292 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a3403d1a-ce79-3845-abc2-d179434ed875 | -15.3881 | -47.9112 | 2026-09-29 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d40f376-ff48-3f01-882f-dacc0c3d405f | -14.80418 | -45.95917 | 2026-09-29 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51717481-1c94-3f97-9e66-d4c38a1c2806 | -11.40643 | -43.44905 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f30024c4-a319-364e-aa2c-7b0206eef4ab | -11.85969 | -47.07985 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8b23174-d7f4-3d4f-9650-0137e4ed2061 | -12.80293 | -50.58643 | 2026-09-29 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a1fbc6c1-54ab-3f0f-aced-5bffef429a42 | -11.36163 | -54.044 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8475a5c6-529e-3197-8d1f-f4eeef3035b7 | -12.07098 | -46.47036 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b1b60e33-3e60-328f-8f92-a0f2226ee4f0 | -10.27634 | -44.63716 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 795b61fa-cb4e-33db-9273-9b58d19302e2 | -11.1466 | -50.07846 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32924caa-fdac-3f6f-b608-299df52a9d3f | -11.41642 | -43.45061 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c4328b33-8aa2-3eaf-bdf8-6df8c5f1fbea | -11.38608 | -47.44092 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 264917ca-546c-3562-a99b-ebe191196897 | -11.69914 | -43.42169 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71dacc33-4df8-3176-a056-41ef9e2e7ec3 | -19.70477 | -46.18777 | 2026-09-29 04:17:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5998df21-03c4-3043-a667-9b268efb2e8c | -12.0432 | -50.94033 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7f4b7672-15af-356b-afd7-27b65c02463d | -11.42145 | -43.46236 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b4b91581-7f5d-31e7-a20f-da36a7d51e67 | -15.83413 | -42.56079 | 2026-09-29 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4a99942c-b08a-32a2-bdd9-6dad7cd7872c | -11.50113 | -47.40458 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b63f9740-5140-3515-913a-e325a401d9d1 | -11.17855 | -44.78711 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc712512-cd57-3c62-b110-b779f104ba05 | -11.41254 | -43.45366 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 99be6f52-f2bf-399e-b1f9-16138e8424f3 | -9.82457 | -45.25517 | 2026-09-29 04:17:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b6c589e-1366-3a18-bcac-f0db5a715cfa | -11.99963 | -51.00781 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 554c83a4-cd43-341f-9484-2c6c96579e97 | -11.41697 | -43.44704 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c88a275-297b-38c5-8907-5099f3f994c2 | -11.70708 | -44.53895 | 2026-09-29 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4e9a925-e464-3e81-bf37-57c3e5c9d34a | -15.39507 | -47.91238 | 2026-09-29 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87055966-b57b-3e20-9e41-192db5993469 | -9.8323 | -45.27122 | 2026-09-29 04:17:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c081e8fe-76ec-3a75-a6b0-7311bc2de682 | -11.39977 | -43.44801 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7c82c17-f139-37c1-9e2d-0bf783bad6ce | -12.01328 | -50.95694 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6d1cbcb-d452-39c6-8fa3-33d4a21a467b | -11.4103 | -43.446 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f021054-66b7-3d0d-bd69-70a3a2053aa2 | -12.02864 | -50.94648 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 623bfa10-aaa9-30a4-a618-955e5e5a31e8 | -14.08742 | -46.309 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 638ee4c8-0d0f-309f-9459-421c8f580ab8 | -10.27799 | -44.62671 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8bd0dbd-4651-35f6-b431-a6cf1b2311d4 | -11.4453 | -43.46245 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09e7b0f5-bc48-3d83-9bea-c5ed5edcc619 | -14.11827 | -46.28813 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ceb2dd4-da04-392e-8565-d55e1ba8cc5b | -11.36838 | -54.03785 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1940a1b-f00d-39d3-8eb8-86decfa3399b | -15.87393 | -40.45687 | 2026-09-29 04:17:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 59d79718-0cc6-3fac-aacb-c8d902cfaad8 | -11.17469 | -44.79009 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 17743be8-f884-36d5-9e0b-20beb4dbc26e | -11.93578 | -50.88251 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5e86155-02d1-3d8d-bd26-68db610ca799 | -11.71372 | -43.46065 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce10802e-fe9e-3f84-b6fa-b3a7c8a8a808 | -11.41533 | -43.45774 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fd5a7034-7637-303d-8006-914cf49bfa59 | -15.73941 | -46.02858 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1c6f5b9-20c4-372e-b10c-1da09b2b8d2b | -11.17854 | -44.80866 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ab11365-a3e9-3711-960b-2d9cfd662cad | -12.23184 | -39.29612 | 2026-09-29 04:17:00 | NOAA-21 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 962c799e-7bd7-3e63-9926-f51285fa7ac5 | -11.65781 | -43.51731 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 955841fc-c848-3914-b7bf-3cfadeecd171 | -10.70092 | -44.42637 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f70eca63-61ed-3cea-99a6-34dc703bb259 | -13.1146 | -47.40748 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b03db4d8-079f-387f-8e65-ebbc08c5c1a0 | -11.36094 | -54.04761 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 200d67ef-24f9-3f1e-8bb0-5379bc1ca449 | -15.39723 | -47.92096 | 2026-09-29 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d71610c-843b-3ad4-b661-2d14172ac0e0 | -11.41194 | -43.4353 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c7089d0-fc49-36a7-8a32-7cc424da3b94 | -9.14466 | -49.97801 | 2026-09-29 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05c8b7fd-1967-3336-ae5e-887db6b3b0bd | -15.09453 | -53.87554 | 2026-09-29 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a1091e8-a51e-3a41-9309-c270deb2ba28 | -11.4045 | -45.42117 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 192826fb-e01f-3b1a-bed4-873853e862fc | -14.22287 | -48.51052 | 2026-09-29 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f5d024e3-9335-3c6e-98f6-ab02edf2664d | -12.01994 | -50.94489 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d9f45be4-1c46-317a-9486-5df60dd2d27c | -13.45897 | -48.58549 | 2026-09-29 04:17:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5eabdfe-51c5-30d0-8f04-8898f3ad8947 | -11.96376 | -50.9273 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66235345-4b9c-34e8-936e-199038d7813f | -20.83419 | -57.68913 | 2026-09-29 04:17:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| c3da16bd-cd5b-33bc-8de9-c8e8fdbc802e | -12.24236 | -50.42918 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2a85031a-5ec0-3a5c-ad88-10f855e50a6d | -12.10668 | -47.39104 | 2026-09-29 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e818681d-b826-38e1-b65a-ad4f620b6507 | -10.71797 | -44.42553 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f88c53ee-8fdc-39a1-8202-5b1ca3d6bc41 | -12.00351 | -50.98623 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4266e17e-a0df-397e-a652-3cb523bb3953 | -11.39064 | -54.03852 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a1e922d-a841-3bfe-ac95-4c3f5d051ddc | -11.43755 | -43.46853 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3f38439-94e1-3c3a-a6af-290f9bd60370 | -12.90502 | -52.03614 | 2026-09-29 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f927bfec-13b0-3a99-80ed-69471e288715 | -11.7176 | -43.4576 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e9be008-28b8-3674-9a1e-5137f75bafd8 | -11.42423 | -43.46644 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| abf92726-7148-35f3-b439-11a8211037fc | -9.74887 | -48.94532 | 2026-09-29 04:17:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8dacd14-7128-32ca-9ffb-67a3d582f808 | -16.35164 | -42.58301 | 2026-09-29 04:17:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 355d070d-f737-3ef5-9b2b-872ad24ad6df | -11.63056 | -43.49475 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca7f3bd8-c58f-350c-817a-b969f16d1676 | -15.21718 | -46.16498 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a34bdbd-46d5-34c1-8539-19d9f56ba87f | -12.05625 | -50.94272 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ebf52508-22c8-3c71-8bfc-046136e0a17c | -13.44636 | -48.59286 | 2026-09-29 04:17:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6849921-e34c-3a4f-9bba-d65a2d2651c5 | -11.16044 | -50.049 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5be16387-6884-32e1-ad14-9ce62f469951 | -14.86565 | -47.99188 | 2026-09-29 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f0134f7f-7908-3b7d-99a8-58e95a3608c0 | -12.88532 | -44.8169 | 2026-09-29 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19c7b279-fbd3-3a1d-afbb-313cc6767b1f | -13.43832 | -43.83012 | 2026-09-29 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98b690f8-7a2c-39e9-97d3-1463f7a9df75 | -10.95159 | -49.59469 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README27.md)
